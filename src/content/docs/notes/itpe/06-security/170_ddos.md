---
title: "DDoS(Distributed Denial of Service)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. DDoS(Distributed Denial of Service)의 개요

- 개념 : 다수의 분산된 **감염 단말** (봇넷, 좀비 PC(Personal Computer), IoT(Internet of Things) 기기)을 동원하여 표적 시스템, 네트워크 회선, 웹 애플리케이션에 정상 용량을 초과하는 대규모 악성 트래픽을 집중 전송함으로써, **가용성** (Availability)을 파괴하고 정상적인 서비스 제공을 마비시키는 분산 서비스 거부 공격.
- 배경 및 필요성 : 공격 도구의 대중화, Mirai 등 IoT 봇넷의 양산, **DDoS(Distributed Denial of Service)-as-a-Service** (부터/스트레서 사이트) 범죄 비즈니스화로 인해 기가급(Gbps)을 넘어 테라급(Tbps) 공격이 일상화됨.
- 핵심 목적 : 기업의 대고객 서비스를 마비시켜 막대한 금전적 손실과 브랜드 신뢰도 추락을 유발하고, **랜섬 디도스** (RDDoS)를 통한 암호화폐 갈취 또는 타깃 침투를 은폐하는 연막작전으로 악용.

## Ⅱ. DDoS(Distributed Denial of Service)의 핵심 아키텍처 및 동작 메커니즘

DDoS 공격은 네트워크 대역폭을 고갈시키는 L3/L4 볼륨 공격, 시스템 자원(TCP(Transmission Control Protocol) 스택)을 고갈시키는 프로토콜 공격, 그리고 백엔드 웹 WAS(Web Application Server)/DB(Database)를 마비시키는 L7 애플리케이션 공격으로 분류됨.

```text
[ DDoS 공격 유형별 3단계 분류 및 클라우드 스크러빙 방어 메커니즘 ]

 +----------------------------------------------------------------------+
 | 1. 네트워크 대역폭 고갈 (L3/L4 볼륨 공격)                            |
 |  * UDP Flood, ICMP Flood                                             |
 |  * DNS / NTP / Memcached 증폭 반사 공격 (수백 Gbps ~ 수 Tbps)        |
 | -------------------------------------------------------------------- |
 | 2. 시스템 자원 고갈 (L4 프로토콜 공격)                               |
 |  * TCP SYN Flood (백로그 큐 고갈), TCP Flag 조작, Ping of Death      |
 | -------------------------------------------------------------------- |
 | 3. 웹 애플리케이션 고갈 (L7 공격)                                    |
 |  * HTTP GET/POST Flood, Slowloris, Slow Read (서버 스레드 점유)      |
 |  * 대규모 DB 검색 질의 유발 (CC Attack, DB 커넥션 풀 고갈)           |
 +----------------------------------+-----------------------------------+
                                    |
                                    v
 [ 글로벌 BGP Anycast 클라우드 스크러빙 센터 (Anycast Scrubbing Center) ]
  * 전 세계 수십 개 에지 PoP에서 공격 트래픽을 분산 흡수
  * 하드웨어 필터(L3/L4) -> 볼륨 공격 즉각 폐기 (Null Route / BGP Flowspec)
  * L7 심층 검사 -> 캡차(CAPTCHA), 자바스크립트 챌린지, 행동 분석으로 봇 차단
                                    |
                                    v (정제된 청정 트래픽만 전달)
  [ 고객사 원본 서버 (Origin Server) : 무중단 정상 서비스 유지! ]
```

- **증폭 반사 공격(Amplification & Reflection)** : 출발지 IP(Internet Protocol)를 희생자 IP로 스푸핑한 후 DNS(Domain Name System), NTP(Network Time Protocol), SSDP 서버에 작은 요청을 전송하여, 크게 팽창된 응답 트래픽이 희생자에게 쏟아지도록 유도.
- **TCP SYN(Synchronize) 플루딩(SYN Flood)** : TCP 3-Way Handshake 과정에서 SYN 패킷만 대량 발송하고 최종 ACK(Acknowledgment)를 보내지 않아 서버의 연결 대기 큐(Backlog Queue)를 가득 채워 정상 접속을 불능화.
- **슬로우 공격(Slowloris / Slow HTTP Read)** : 소량의 트래픽만으로 HTTP(Hypertext Transfer Protocol) 헤더나 본문을 극도로 느린 속도로 전송하여 웹 서버의 연결 스레드를 장시간 점유함으로써 신규 연결을 차단하는 지능형 L7 공격.
- **클라우드 스크러빙(Scrubbing Center)** : 회선 대역폭을 초과하는 대규모 공격을 방어하기 위해 트래픽을 글로벌 분산 Anycast 클라우드로 우회시켜 정화 후 원본 서버로 전달.

## Ⅲ. DDoS(Distributed Denial of Service)의 세부 구성 요소 및 비교 분석

| 비교 항목 | **대역폭 고갈** (볼륨 공격) | **자원 고갈** (프로토콜 공격) | **웹 애플리케이션** (L7 공격) |
| --- | --- | --- | --- |
| 대상 계층 | L3/L4 네트워크 계층 | L4 전송 계층 (OS(Operating System) 커널 스택) | L7 애플리케이션 계층 |
| 대표 공격 | UDP(User Datagram Protocol) Flood, DNS/NTP 증폭 반사 | TCP SYN Flood, RST(Reset) Flood | HTTP GET Flood, Slowloris, Slow Read |
| 트래픽 규모 | 수십 Gbps ~ 수 Tbps (대규모) | 중간 (패킷 수 PPS 중심) | 극소량 (수 Mbps 미만으로도 마비) |
| 공격 원리 | 네트워크 대역폭 파이프 초과 | OS TCP 백로그 큐 소진 | WAS 스레드 풀 및 DB 커넥션 점유 |
| 핵심 대응 | 클라우드 스크러빙, BGP(Border Gateway Protocol) Anycast | SYN Cookie, 연결 임계치 설정 | WAF(Web Application Firewall), CAPTCHA, 레이트 리미팅, CDN(Content Delivery Network) |

- DDoS 공격은 볼륨성과 지능형 L7 공격이 혼합된 복합 벡터(Multi-vector) 형태로 전개되므로, 회선 확충에 의존하지 않고 클라우드 기반 스크러빙과 WAF의 다층 방어가 필수적임.

## Ⅳ. DDoS(Distributed Denial of Service)의 주요 한계점 및 해결 방안

- 공격 트래픽 규모가 조직의 보유 인터넷 회선 대역폭 초과 :
  - 한계점 : 기업이 보유한 회선 대역폭을 크게 초과하는 볼륨 공격이 유입되면 사내 방화벽 장비에 도달하기도 전에 상위 ISP(Internet Service Provider) 라우터에서 회선 전체 포화.
  - 해결 방안 : 온프레미스 장비 단독 방어를 포기하고 BGP Anycast 기반 글로벌 클라우드 DDoS 완화 서비스(Cloudflare, Akamai)로 트래픽 사전 흡수.
- 정상 사용자와 위장된 L7 봇 트래픽의 구별 난제 :
  - 한계점 : 공격자가 헤드리스 브라우저(Puppeteer)를 동원하여 정상 브라우저 헤더를 흉내 내며 웹 검색을 수행하면 WAF가 정상 요청으로 오인.
  - 해결 방안 : 자바스크립트 챌린지 검증, 마우스 궤적 및 타이핑 지연 분석(비지도 학습 AI(Artificial Intelligence) 행위 프로파일링)을 통한 봇 식별.
- 랜섬 디도스(RDDoS) 협박 및 지불 유혹 :
  - 한계점 : 몸값을 지불하지 않으면 대규모 디도스 공격을 감행하겠다는 협박 메일 수신 시 비즈니스 연속성 우려로 패닉 발생.
  - 해결 방안 : 사전 비상 대응 훈련 수립, KISA(Korea Internet & Security Agency) 사이버대피소 사전 연동 등록, 협박범과의 협상 전면 거부 원칙 고수.

## Ⅴ. DDoS(Distributed Denial of Service) 적용 및 발전을 위한 기술사적 제언

- SYN Cookie 및 임계치 기반 커널 하드닝 : 운영체제 레벨에서 'sysctl net.ipv4.tcp_syncookies=1'을 활성화하여 백로그 큐 없이 암호학적 쿠키로 연결을 검증하여 SYN Flood 무력화.
- API(Application Programming Interface) 게이트웨이 레벨의 속도 제한(Rate Limiting) 강제 : IP, 토큰, 사용자별로 초당 허용 요청 수(RPS)를 제약하는 토큰 버킷(Token Bucket) 알고리즘을 적용하여 비정상 API 플루딩 차단.
- 통신사(ISP) 간 BGP Flowspec 기반 백본 즉각 차단 체계 : DDoS 공격 패킷의 IP, 포트, 패킷 크기 특성을 BGP Flowspec 룰로 ISP 라우터에 자동 전파하여 최외곽 백본에서 공격 트래픽을 즉각 널(Null) 라우팅.
