---
title: "DDoS(Distributed Denial of Service)"
description: "분산된 다수의 봇넷 및 반사 서버를 동원하여 네트워크 대역폭, 시스템 자원 및 애플리케이션 서비스 용량을 고갈시켜 정상 서비스를 마비시키는 분산 서비스 거부 공격"
tags:
  - "notes-security"
  - "ddos"
  - "network-security"
  - "scrubbing-center"
  - "bgp-flowspec"
categories:
  - "ITPE"
date: "2026-03-31T00:00:00+09:00"
author: "Antigravity"
model: "Gemini 3.8 Flash"
draft: false
sidebar:
  order: 170
---

## 지식 로드맵 내 현재 위치

- 정보보안 → 네트워크 보안 → 가용성 위협 → DDoS(Distributed Denial of Service)

```text
[공격자 (C2 마스터)] ──> [좀비 PC / IoT 봇넷 (Mirai 등)]
                                   │
                                   ├── L3/L4 볼륨형: UDP/DNS/NTP 반사 증폭 공격 (대역폭 고갈)
                                   ├── L4 프로토콜형: TCP SYN Flooding (백로그 큐 고갈)
                                   └── L7 애플리케이션형: HTTP Slowloris / RUDY (커넥션 풀 고갈)
                                   │
                                   ▼
                 [Anycast 스크러빙 센터 ──> BGP Flowspec 정제 ──> 클린 트래픽 전달]
```

---

## 30초 인출

- **본질:** 악성코드에 감염된 대규모 봇넷(Botnet) 또는 제3의 취약 서버를 이용하여 표적 시스템의 대역폭, 운영체제 연결 큐, 애플리케이션 스레드를 고갈시켜 가용성을 침해하는 공격.
- **메커니즘:** IP 스푸핑 기반 UDP 증폭 요청 전송 → 희생자 IP로 수십~수백 배 증폭된 응답 집중 → 백본 회선 포화 및 커넥션 풀 고갈 → 정상 클라이언트 타임아웃 장애 유발.
- **통찰:** 온프레미스 방화벽만으로는 수백 Gbps 이상의 회선 포화 공격을 물리적으로 방어할 수 없으므로, BGP Anycast 기반의 글로벌 클라우드 스크러빙 센터와 BGP Flowspec 상류 차단 연계 필수.

---

## 2~4교시 예상문제 (25점)

> 최근 테라비트(Tbps)급으로 대형화되는 DDoS 공격의 유형을 OSI 계층별(L3/L4 볼륨형, L4 상태형, L7 저속/고속 애플리케이션형)로 분류하고, 클라우드 스크러빙 센터와 BGP 기반 연동 완화 아키텍처를 제시하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 인터넷에 분산 배치된 다수의 에이전트(좀비 PC, IoT 기기)를 원격 조종하여 표적 시스템에 비정상적인 대용량 트래픽 또는 고비용 질의를 집중시킴으로써 가용성(Availability)을 파괴하는 공격 |
| 목적 | 단순 회선 마비뿐 아니라 랜섬 디도스(RDoS)를 통한 금전 갈취, 지능형 지속 위협(APT)의 데이터 유출을 은폐하기 위한 기만전술(Smokescreen)로 활용 |

- 최근 Mirai 변종 및 Memcached 반사 공격으로 1~3 Tbps 이상의 초대형 볼륨 공격과 함께, 정상 트래픽으로 위장한 L7 저속 공격(Slowloris)이 융합된 다계층 복합 공격 형태로 진화.

---

## Ⅱ. DDoS 공격의 핵심 특징 및 계층별 위협 분류

### 1. DDoS 공격의 핵심 특징

| 특징 | 설명 | 기술적 영향 |
|---|---|---|
| 분산성 및 비대칭성 | 적은 공격 자원으로 막대한 피해 유발 | 증폭 계수(NTP 556배, Memcached 5만배)를 활용하여 공격자 대역폭 대비 폭발적 트래픽 생성 |
| 출발지 주소 위조 (Spoofing) | 비연결성 UDP 프로토콜 악용 | 역추적을 차단하고 반사 서버(Reflector)가 피해자 IP로 일제히 응답하도록 유도 |
| 복합 다계층화 (Multi-Vector) | L3 대역폭과 L7 웹 공격 동시 감행 | 대역폭 공격으로 보안 장비의 CPU를 포화시킨 후 정밀 L7 공격으로 DB 서버 마비 |
| 저속 공격의 은밀성 | 소량의 트래픽으로 임계치 탐지 회피 | Slowloris, RUDY 등 패킷 단위를 최소화하여 장기간 세션을 점유하고 웹 스레드 고갈 |

### 2. OSI 7계층별 DDoS 공격 분류

```text
[DDoS 공격 계층 분류]
  ├── 1. L3/L4 볼륨형 공격 (Volumetric)   ──> UDP Flooding, ICMP Flooding, DNS/NTP/Memcached 반사 증폭
  ├── 2. L4 상태 고갈형 (Protocol State) ──> TCP SYN Flooding, ACK Flooding, TCP Reset Flooding
  └── 3. L7 애플리케이션형 (Application) ──> HTTP GET/POST Flood, Slowloris, Slow HTTP POST, Hash DoS
```

---

## Ⅲ. DDoS 방어 아키텍처 및 단계별 완화 프로세스

### 1. BGP Anycast 기반 클라우드 스크러빙 완화 아키텍처

```text
+-----------------------------------------------------------------------------------------+
|                               클라우드 스크러빙 DDoS 완화 아키텍처                         |
+-----------------------------------------------------------------------------------------+
  [공격 봇넷 (수 Tbps)] ────────┐
                               ├──> [글로벌 BGP Anycast PoP 분산] ──> [스크러빙 센터 (Scrubbing)]
  [정상 사용자 요청] ───────────┘            │                                  │
                                             ▼                                  ├── L3/L4: SYN Cookie, Rate Limiting
                                    [전 세계 엣지로 분산]                       ├── L7: JS Challenge, CAPTCHA
                                                                                └── BGP Flowspec (상류 ISP 차단)
                                                                                        │
                                                                                        ▼ (클린 트래픽만 인입)
                                                                             [기업 데이터센터 / 원본 서버]
+-----------------------------------------------------------------------------------------+
```

### 2. DDoS 탐지 및 대응 4단계 생명주기 프로세스

| 단계 | 수행 작업 | 핵심 적용 기술 |
|---|---|---|
| 1. 이상 탐지 (Detection) | 트래픽 임계치 초과 및 프로토콜 플로우(NetFlow/sFlow) 이상 감시 | Baseline 트래픽 분석, 비정상 패킷 PPS/BPS 급증 모니터링 |
| 2. 트래픽 전환 (Diversion) | 공격 대상 IP의 트래픽을 상류 정화 센터로 우회 유도 | BGP Route Announcement, DNS Anycast CNAME 변경 |
| 3. 패킷 정화 (Scrubbing) | 정상 요청과 공격 패킷 분리 및 공격 패킷 차단/폐기 | SYN Proxy, Cookie 검증, L7 HTTP 심층 검사, DPI |
| 4. 클린 포워딩 (Re-injection) | 정제된 정상 트래픽만을 원본 서버(Origin)로 안전 전달 | GRE(Generic Routing Encapsulation) 터널, mTLS 터널 |

---

## Ⅳ. DDoS 공격 유형(볼륨형 vs 프로토콜형 vs L7 애플리케이션형) 비교

### 1. 3대 DDoS 공격 유형 비교

| 비교 항목 | L3/L4 볼륨형 공격 | L4 프로토콜 상태 고갈형 | L7 애플리케이션형 공격 |
|---|---|---|---|
| 주요 표적 | 네트워크 인터페이스 및 백본 회선 대역폭 | 방화벽, L4 스위치, OS 커널 연결 테이블 | 웹 애플리케이션 서버(WAS), 데이터베이스 |
| 대표 공격 기법 | NTP/DNS/SSDP 반사 증폭, UDP Flood | TCP SYN Flood, FIN/RST Flood | HTTP GET Flood, Slowloris, RUDY |
| 트래픽 특성 | 기가~테라비트(Gbps/Tbps) 대규모 패킷 | 높은 초당 패킷 수 (High PPS) | 정상 패킷과 구별 불가한 소량 저속 트래픽 |
| 방어 메커니즘 | BGP Anycast 분산, 클라우드 스크러빙 센터 | SYN Cookie, 연결 제한, 커널 파라미터 튜닝 | WAF, 행위 기반 봇 감지, 자바스크립트 챌린지 |
| 온프레미스 한계 | 회선 자체가 포화되어 방어 장비 도달 불가 | 세션 테이블 메모리 오버플로우로 장비 다운 | 정상 브라우저 위장 시 시그니처 차단 불가 |

---

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 공격 규모가 수 Tbps 이상으로 폭증할 경우 사내 인입 회선 물리적 용량(10Gbps 등)을 초과하여 온프레미스 보안 장비 전면 무력화 | 공격 트래픽을 데이터센터 진입 전에 전 세계 엣지 네트워크로 분산 흡수하는 글로벌 Anycast CDN 및 대용량 클라우드 스크러빙 서비스로 인프라 전환 |
| 정상적인 HTTP 클라이언트와 동일하게 위장하여 헤더를 천천히 전송하는 L7 저속 공격(Slowloris)은 임계치 기반 차단 정책을 완벽 우회 | 리버스 프록시(Nginx/HAProxy) 앞단에서 최소 요청 전송 속도(`client_body_timeout`)를 강제하고 HTTP Keep-Alive 시간제한 및 비동기 이벤트 루프(Epoll) 아키텍처 적용 |
| ISP 단계에서 공격 트래픽 완화를 위해 RTBH(Blackhole 라우팅)를 적용할 경우 피해 서버의 정상 트래픽까지 100% 폐기되어 공격자의 서비스 중단 목적 달성 | 목적지 IP뿐 아니라 출발지 IP, 프로토콜, 포트, 패킷 길이 등 다차원 세부 룰을 BGP 라우터에 실시간 주입하여 공격 패킷만 선별 폐기하는 BGP Flowspec(RFC 5575) 구축 |

---

## Ⅵ. 제언

### 1. 다계층 심층 DDoS 방어 아키텍처

```text
[글로벌 인터넷] ──> [상류 ISP BGP Flowspec 차단] ──> [클라우드 스크러빙 (Tbps 흡수)]
                                                              │
                                                              ▼
[원본 방화벽 (Stateful)] <──(GRE 터널 암호화)─── [L7 WAF (정상 봇 검증 및 속도제한)]
         │
         ▼
[백엔드 서버: 커널 SYN Cookie 활성화, Keep-Alive 타임아웃 단축, Auto-scaling 연동]
```

### 2. DDoS 방어 기술 및 서비스 종합 비교 평가

| 완화 기술 | 완화 역량 | 구축 비용 | 레이턴시 영향 | 주 방어 대상 |
|---|---|---|---|---|
| 온프레미스 안티 DDoS 장비 | 수십 Gbps 한계 | 고가 (하드웨어) | 없음 (로컬 인라인) | L4 상태 고갈, 중소규모 볼륨 공격 |
| KISA 사이버대피소 | 중규모 (수백 Gbps) | 무료 (중소기업 지원) | 약간 증가 (DNS CNAME 전환) | 공공/중소기업 대상 중규모 공격 |
| 글로벌 클라우드 스크러빙 | 수십 Tbps (무제한급) | 월 구독형 (종량제) | 거의 없음 (Anycast 엣지 종단) | 글로벌 엔터프라이즈, 테라비트급 초대형 공격 |
| BGP Flowspec (RFC 5575) | 라우터 하드웨어 속도 | 네트워크 인프라 연계 | 없음 | ISP 레벨 반사 증폭 및 프로토콜 Flooding |

- 현대 DDoS 방어는 단일 장비로 불가능하므로, BGP Anycast 클라우드 스크러빙을 1선에 배치하고, L7 WAF와 커널 튜닝을 유기적으로 결합한 다계층 방어망 구축 필수.

---

## 출제 이력과 검증 출처

- 컴퓨터시스템응용기술사 119회 2교시 (DDoS 공격의 유형별 메커니즘과 클라우드 스크러빙 센터)
- 정보관리기술사 128회 1교시 (Slowloris 및 Slow HTTP POST 공격 원리와 대응 기술)
- 정보관리기술사 132회 3교시 (BGP Flowspec을 활용한 DDoS 상류 완화 아키텍처)
- RFC 5575 Dissemination of Flow Specification Rules
- NIST SP 800-189 Resilient Interdomain Traffic Exchange: BGP Security and DDoS Mitigation
