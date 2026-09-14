---
sidebar:
  order: 87
  label: "087. DDoS 공격 기법 및 다단 방어 체계"
  badge:
    text: "기출 · 50%"
    variant: note
title: "분산 서비스 거부 공격 및 계층형 방어 체계 : DDoS 완화"
date: "2026-09-07T14:00:00+09:00"
tags:
  - "notes-network"
weight: 87
extra:
  question_no: "87"
  source_status: "기출"
  source_history: "125회"
  priority: 50
  priority_note: "대역폭 고갈(Volumetric), 프로토콜 상태 고갈(SYN Flood), L7 웹 공격 및 CDN/스크러빙 다단 완화"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **DDoS (Distributed Denial of Service)**: 대규모 분산 봇넷으로 표적 인프라의 대역폭과 세션 자원을 고갈시키는 가용성 침해 공격.
- **Multi-Layer Mitigation (다단 방어 체계)**: 상위 ISP, Anycast CDN, 클라우드 스크러빙 센터, 온프레미스 WAF로 계층 분할 정화하는 아키텍처.

</details>

- 정의/개념: 대용량 볼륨 공격부터 L4 세션 및 L7 애플리케이션 자원 고갈 공격까지 **상위 ISP, Anycast CDN, 스크러빙 센터, WAF를 통해 단계별로 정화하는 다단 방어 체계**
- 배경/필요성: 글로벌 봇넷과 IoT 기기 탈취로 인한 테라비트급(Tbps) 볼륨 공격, TCP 3-Way Handshake 취약점을 노린 프로토콜 상태 고갈(SYN Flood), 정상 트래픽으로 위장한 L7 HTTP/API 공격 등 다차원적 DDoS 공격이 지능화되는 환경에서, 온프레미스 단일 방화벽이나 로컬 보안 장비에만 의존하는 방식은 인입 회선 대역폭 포화와 방화벽 세션 테이블 고갈로 인해 정상적인 대고객 서비스가 전면 마비되는 한계를 노출함에 따라, 상위 티어 ISP(BGP Flowspec), 글로벌 BGP Anycast CDN, 클라우드 스크러빙(Scrubbing) 센터 및 온프레미스 WAF를 유기적으로 연계한 다단 방어(Multi-Layer Mitigation) 아키텍처를 도입하여 **초대용량 볼륨 공격의 글로벌 분산 흡수, 악성 패킷의 정밀 세탁 및 무중단 비즈니스 서비스 연속성**을 달성할 필요

#### 한줄 요약
- BGP Anycast 분산 흡수, 스크러빙 센터 세탁, WAF 정밀 필터링을 통해 서비스 가용성을 보장해야 한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **BGP Anycast Routing**: 동일한 IP 주소를 전 세계 수십 개 데이터센터 PoP에서 동시 광고하여 공격 트래픽을 지리적으로 분산 흡수하는 기술.
- **Scrubbing Center (스크러빙 센터)**: 대규모 인입 트래픽 중 악성 패킷만 선택적으로 제거하고 정상 트래픽만 원본 서버로 전달하는 전문 정화 센터.

</details>

- **계층별 분할 완화(Tiered Mitigation)**: L3/L4 볼륨 공격은 **상위 ISP/CDN에서 흡수하고 L7 웹 공격은 WAF에서 정밀 차단**
- **BGP Anycast 기반 글로벌 분산 흡수**: 단일 표적 IP 트래픽을 수십 개 글로벌 PoP로 분산시켜 **Tbps급 공격을 국소화**
- **오탐(False Positive) 최소화 및 정상 트래픽 보존**: **SYN Cookie, JS Challenge, CAPTCHA**를 통해 악성 봇과 사용자 실시간 선별

#### 한줄 요약
- 계층별 다단 완화, BGP Anycast 분산 흡수, 스크러빙 센터 정화 및 챌린지 검증을 체계적으로 제공해야 한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **SYN Cookie (RFC 4987)**: TCP 3-Way Handshake 시 서버 TCB 메모리를 할당하지 않고 암호화된 시퀀스 번호로 최종 ACK를 검증하는 방어 기술.

</details>

```text
[DDoS 다단 방어 체계]
  │
  ├─ [1단계 외곽] ── Outer Edge
  │     └─ [상위 ISP·CDN] (볼륨 분산과 경계 필터링)
  ├─ [2단계 정화] ── Scrubbing
  │     └─ [스크러빙 센터] (L3·L4 트래픽 정화와 정상 흐름 선별)
  └─ [3단계 원본] ── Origin Defense
        └─ [원본 WAF·게이트웨이] (L7 요청 검사와 속도 제한)
```

- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| **상위 ISP·CDN** | 볼륨 분산과 경계 필터링 |
| **스크러빙 센터** | L3·L4 트래픽 정화와 정상 흐름 선별 |
| **원본 WAF·게이트웨이** | L7 요청 검사와 속도 제한 |

#### 한줄 요약
- 상위 ISP/CDN Anycast, 클라우드 스크러빙 센터, 온프레미스 WAF의 3계층 다단 방어로 인프라를 보호한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **BGP Flowspec (RFC 5575)**: 컨트롤러가 BGP를 통해 라우터 FIB에 세부 패킷 필터링 룰(Src/Dst, 포트 등)과 액션(Drop, Redirect)을 자동 주입하는 기술.

</details>

```text
[DDoS 완화 흐름] (진행 ①→⑤, 이상 감지에서 진입, 각 정화 단계의 악성 판정 시 폐기·통과분만 터널로 원본 전송)
  │
  ├─ [트래픽 이상 감지] (① 텔레메트리로 Baseline 대비 bps·pps 임계치 초과 판정)
  │
  ├─ [스크러빙 센터 우회] (② BGP Flowspec·DNS CNAME으로 인입 경로 절체)
  │
  ├─ [L4 프로토콜 정화] (③ SYN Proxy·Cookie와 UDP 레이트 리미팅 집행)
  │
  ├─ [L7 봇넷 챌린지] (④ JavaScript Challenge·TLS 지문 분석으로 악성 봇 차단)
  │
  └─ [정상 트래픽 터널 전송] (⑤ 정화 통과 패킷만 GRE·IPsec 터널로 원본 서버 전달)
```

분기 결과: 각 정화 단계에서 악성·정상 판정이 갈리며, **BGP Anycast Routing**·**Scrubbing Center** 상위 갈래는 대역폭을 흡수·세탁할 글로벌 인프라 비용을 치르는 대신 Tbps급 공격으로부터 회선 생존을 얻고, **SYN Cookie** 갈래는 연결마다 서버 상태 메모리를 만들지 않아 세션 고갈을 막는 대신 세션 진단 기능 일부를 희생하며, 우회 시점부터는 정상 트래픽도 스크러빙 경로를 타므로 경로 우회 지연과 오탐을 정상 사용자가 함께 겪는 비용이 남는다.

#### 한줄 요약
- BGP 우회 시점부터는 정상 트래픽도 함께 스크러빙 경로를 타므로, 경로 우회 지연과 오탐을 대가로 회선 자체의 생존을 확보한다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **Volumetric vs State-Exhaustion vs Application (L7)**: 대역폭 포화(bps), 세션 테이블 고갈(pps), 웹서버 컴퓨팅 고갈.

</details>

| 비교 항목 | 볼륨형 공격 (Volumetric Attack) | 프로토콜 상태 고갈 (State-Exhaustion) | 애플리케이션 공격 (L7 App Attack) |
|:---|:---|:---|:---|
| 고갈 대상 | 회선 대역폭 | 세션·상태 테이블 | 응용·DB 자원 |
| 공격 기법 | 반사 증폭·UDP Flood | SYN·ACK Flood | HTTP Flood·Slowloris |
| 트래픽 특성 | 대용량 패킷 | 대량 제어 패킷 | 정상 형식의 악성 요청 |
| 방어 대책 | **Anycast·스크러빙** | **SYN Proxy·Cookie** | WAF·챌린지·속도 제한 |

#### 한줄 요약
- 볼륨형은 대역폭 분산, 프로토콜형은 SYN Cookie, L7 공격은 WAF/Rate Limiting으로 방어한다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **Slowloris (슬로우로리스)**: HTTP 헤더 끝(`\r\n\r\n`)을 완성하지 않고 미완성 헤더를 느리게 전송하여 웹서버 스레드 풀을 장시간 고갈시키는 L7 저속 공격.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 500Gbps 이상 초대용량 UDP 반사 공격으로 전용 회선 대역폭 포화 | **`상위 ISP BGP Flowspec` 차단 및 글로벌 Anycast 스크러빙** 우회 | 인입 회선 포화 사전 방지 및 비즈니스 대역폭 보존 |
| 대규모 위조 SYN Flood 공격으로 방화벽/서버 TCB 세션 고갈 | L4 방화벽 전단에 **`하드웨어 기반 SYN Cookie` 및 SYN Proxy 활성화** | 가짜 반개방 세션 저장 방지 및 신규 연결 보장 |
| 정상 트래픽과 동일한 패턴의 L7 Slowloris 및 무차별 웹 크롤링 폭주 | **`L7 클라이언트 지문(JA3/TLS) 분석` 및 비용 기반 레이트 리미팅** | 백엔드 서버 CPU 고갈 차단 및 오탐을 최소화한 정상 수용 |
| 스크러빙 센터 우회 후 직접 원본 서버(Origin) IP로 공격 집중 | **`Origin IP 은폐` 및 스크러빙 PoP IP만 인가하는 Ingress 화이트리스트** | 백엔드 원본 직접 타격 방지 |

#### 한줄 요약
- BGP Flowspec으로 회선을 방어하고, SYN Cookie로 세션 고갈을 방지하며, TLS 지문 분석으로 L7 공격을 무력화해야 한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **eBPF (Extended Berkeley Packet Filter)**: 리눅스 커널 소스코드를 변경하지 않고 샌드박스 프로그램으로 고속 패킷 필터링과 관측성을 제공하는 기술.
- **XDP (eXpress Data Path)**: 네트워크 드라이버 계층에서 패킷을 직접 가로채 커널 스택 오버헤드 없이 초고속 드롭/포워딩을 수행하는 eBPF 기반 프레임워크.

</details>

- 단순 인입 회선 증설이나 단일 장비 방어의 한계를 넘어 글로벌 분산 클라우드 인프라와 엣지 컴퓨팅을 활용하는 **엔터프라이즈 및 인터넷 서비스 제공자(ISP)의 핵심 비즈니스 가용성 방어 표준 프레임워크**로 확립되었다.
- AI/ML 기반 비정상 트래픽 예측 및 eBPF/XDP 기반 커널 바이패스 고속 패킷 드롭 기술과 융합하는 가운데, 실무 DDoS 방어 체계 구축 시에는 **Tbps급 볼륨 공격을 효과적으로 분산시키는 BGP Anycast 스크러빙 센터 연동**, **서버 세션 고갈을 방지하는 하드웨어 가속 SYN Cookie 활성화**, **봇넷의 L7 우회 공격을 차단하는 TLS/JA3 지문 기반 행동 분석 및 WAF 레이트 리미팅**, **오리진(Origin) 직접 타격을 방지하는 원본 IP 은폐와 인그레스 화이트리스트**를 결합하여 안정적인 서비스 탄력성을 확보해야 한다.

#### 한줄 요약
- DDoS 방어는 BGP Anycast 분산 흡수와 스크러빙 센터 세탁 및 WAF 정밀 필터링을 결합한 다단 완화 아키텍처로 구현해야 한다.
