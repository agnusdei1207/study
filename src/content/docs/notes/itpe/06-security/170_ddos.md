---
title: "DDoS(Distributed Denial of Service)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T01:00:00+09:00"
tags:
  - "notes-security"
extra:
  model: "Gemini 3.8 Flash"

---

# DDoS(Distributed Denial of Service)

## 핵심 개념
- 여러 대의 분산된 시스템(봇넷, 좀비 PC, 감염된 IoT 장비)을 원격 조종하여 특정 타깃 서버나 네트워크 인프라에 감당할 수 없는 양의 대규모 트래픽을 집중 전송함으로써 시스템 자원을 고갈시키고 정상적인 서비스 제공을 마비시키는 가용성(Availability) 침해 공격.
- 공격 계층에 따라 대역폭 고갈(L3/L4 볼류메트릭), 프로토콜 스택 자원 고갈(L4 연결 자원 소진), 웹 애플리케이션 자원 고갈(L7 트랜잭션 고갈)로 분류됨.

```
+-------------------------------------------------------------+
|                      DDoS 공격 구조 및 계층                   |
+-------------------------------------------------------------+
| [공격자 (Attacker)]                                         |
|         | 공격 명령 전송                                    |
|         v                                                   |
| [C&C 서버 / 마스터 (Master / Handler)]                       |
|         | 분산 공격 지시 하달                               |
|         v                                                   |
| [수천~수십만 대의 좀비 봇 (Botnet / Agent / IoT)]           |
|         | 동시 다발적 대량 패킷 방사                         |
|         v                                                   |
| [피해 서버 (Target Server) / 네트워크 회선 마비]            |
+-------------------------------------------------------------+
```

---

## DDoS 공격 유형 3대 분류

```
+-------------------------------------------------------------+
| 1. 대역폭 고갈 공격 (Volumetric)   | UDP/ICMP Flood, 증폭 공격 (Gbps~Tbps)|
| 2. 프로토콜 고갈 공격 (Protocol)   | TCP SYN Flood, Ping of Death, Smurf |
| 3. 애플리케이션 고갈 공격 (App/L7) | HTTP GET Flood, Slowloris, Slow Read|
+-------------------------------------------------------------+
```

### 1. 볼륨/대역폭 고갈 공격 (Network Layer / L3-L4)
- **UDP / ICMP Flood**: 대량의 비정상 UDP/ICMP 패킷을 타깃으로 무차별 전송하여 회선 대역폭 포화 유발.
- **반사 증폭 공격 (Reflection & Amplification Attack)**:
  - 송신자 IP를 피해자 IP로 변조(Spoofing)한 후, 오픈 리졸버 DNS, NTP, Memcached 서버에 소량의 질의 전송.
  - 반사 서버가 수십~수백 배 증폭된 대용량 응답 패킷을 피해 서버로 집중 전송(DNS Amplification, NTP Monlist 등).

### 2. 프로토콜 자원 고갈 공격 (Transport Layer / L4)
- **TCP SYN Flood**: 3-Way Handshake 과정에서 수많은 `SYN` 패킷을 위조 IP로 전송하고 `ACK`를 보내지 않아, 서버의 백로그 큐(Backlog Queue)를 가득 채워 신규 연결 차단.
- **스머프(Smurf) 공격**: ICMP Echo Request를 네트워크 브로드캐스트 주소로 전송(송신자 IP는 희생자 IP로 위조)하여 네트워크 내 모든 호스트의 응답이 희생자에게 집중되도록 유도.

### 3. 애플리케이션 계층 공격 (Application Layer / L7)
- **HTTP GET / POST Flood**: 정상적인 TCP 세션을 맺은 후 대용량 웹 페이지나 DB 부하가 큰 검색 쿼리를 초당 수천~수만 회 요청하여 웹/WAS/DB 서버 CPU 및 메모리 고갈.
- **슬로우리스(Slowloris)**: HTTP 요청 헤더의 끝(`\r\n\r\n`)을 전송하지 않고 불완전한 헤더를 아주 긴 주기로 쪼개어 전송함으로써 서버의 연결 스레드를 무한 점유.
- **슬로우 리드(Slow HTTP Read)**: 요청은 정상 전송하되 수신 윈도우 크기(TCP Window Size)를 0 또는 극소 크기로 설정하여 응답 수신을 지연시킴으로써 서버 자원 점유.

---

## DDoS 공격 계층별 비교

| 비교 항목 | 볼륨 공격 (Volumetric) | 프로토콜 공격 (Protocol) | L7 웹 애플리케이션 공격 |
|---|---|---|---|
| **대상 계층** | L3 (IP), L4 (UDP) | L4 (TCP 스택) | L7 (HTTP / HTTPS) |
| **소모 자원** | 네트워크 회선 대역폭 (Bps) | OS 백로그 큐, 소켓 테이블 (Pps) | 웹 서버 커넥션 풀, CPU, DB 커넥션 (Qps) |
| **공격 규모** | 수십 Gbps ~ 수 Tbps | 수백만 ~ 수천만 Pps | 수천 ~ 수만 Qps (저대역폭 트래픽) |
| **탐지 난이도** | 트래픽 임계치 초과로 비교적 용이 | 패킷 패턴 분석 필요 | 정상 웹 요청과 구별하기 어려워 탐지 난이도 높음 |

---

## DDoS 방어 및 완화(Mitigation) 기술 체계

```
[외부 대규모 공격 트래픽 유입]
              |
              v
[1. 글로벌 Anycast CDN / 클라우드 스크러빙 센터]
   - 전 세계 에지 PoP으로 트래픽 분산 분기
   - 정상 트래픽만 정제하여 원본 서버(Origin)로 포워딩
              |
              v
[2. 인라인 DDoS 전용 방어 장비 (DDoS Shield)]
   - SYN Cookie: SYN-ACK 시 시퀀스 번호에 암호화 해시를 탑재하여 백로그 큐 소모 없이 연결 검증
   - 임계치 기반 차단 (Rate Limiting) 및 블랙홀 라우팅(Blackholing / RTBH)
              |
              v
[3. 웹 방화벽 (WAF) 및 웹 서버 하드닝]
   - L7 Slow HTTP 공격 대응: 요청 타임아웃(Timeout) 단축 설정
   - CAPTCHA 및 JavaScript 챌린지 검증을 통한 자동화 봇 차단
```

---

## 결론 및 실무 시사점
- 최근 DDoS 공격은 멀티 벡터(Multi-vector) 형태로 볼륨 공격과 정밀한 L7 슬로우 공격이 결합되어 나타남.
- 단일 사내 장비만으로는 테라급 대역폭 공격을 물리적으로 방어할 수 없으므로, ISP와의 협력(RTBH), Anycast 기반 클라우드 스크러빙 센터(Cyber Shelter), CDN 도입을 결합한 하이브리드 완화 체계 구축이 필수적임.
