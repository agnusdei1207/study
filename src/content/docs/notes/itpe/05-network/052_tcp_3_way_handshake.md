---
title: "3-way handshake"
author: "agnusdei1207"
date: "2026-10-24T22:48:45+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- TCP 3-Way Handshake, SYN, ACK, 초기 시퀀스 번호(ISN)
- SYN_SENT, SYN_RCVD, ESTABLISHED, 백로그 큐
- SYN 플러딩, SYN 쿠키, TCP Fast Open, 윈도우 스케일, SACK, 타임스탬프

## Ⅰ. TCP 3-Way Handshake의 개요

- 핵심 요약 : 세 번의 SYN·ACK 교환으로 초기 시퀀스 번호와 통신 옵션을 맞춰 신뢰성 있는 연결을 수립하는 절차.
- 개념 : 데이터 전송 전에 클라이언트와 서버가 SYN(Synchronize)과 ACK(Acknowledgment) 플래그, **초기 시퀀스 번호** (ISN, Initial Sequence Number)를 세 단계로 교환해 연결을 수립하는 절차(**TCP 3-Way Handshake**).
- 배경 및 필요성 : 패킷이 유실·지연·역전될 수 있는 IP(Internet Protocol) 네트워크에서 순서를 복원하고 중복 수신을 막으려면, 송수신 양단의 상태를 전송 전에 맞춰야 함.
- 주요 목적 : 양단의 ISN 동기화, 수신 윈도우 크기와 MSS(Maximum Segment Size), SACK(Selective Acknowledgment), 타임스탬프 등 통신 옵션의 사전 협상.

## Ⅱ. TCP 3-Way Handshake의 특징 및 장점

- 핵심 요약 : 연결 전에 상태와 옵션을 합의해 이후 데이터 전송의 순서와 품질을 보장하는 구조.

1. 시퀀스 동기화 : 양방향 ISN을 교환하고 상대의 값을 확인 → 패킷 순서 복원과 중복 제거의 기준 확보.
2. 옵션 협상 : SYN에 MSS, 윈도우 스케일, SACK 허용, 타임스탬프를 실어 보냄 → 단말 능력에 맞는 전송 조건 확정.
3. 세 번째 ACK의 데이터 탑재 : 마지막 ACK에 첫 데이터를 함께 실을 수 있음 → 첫 요청까지의 지연 단축.

## Ⅲ. TCP 3-Way Handshake의 구조 (흐름)

- 핵심 요약 : 클라이언트와 서버가 각각 SYN_SENT·SYN_RCVD를 거쳐 같은 시점에 ESTABLISHED로 수렴하는 흐름.

```text
[ 3-Way Handshake 메시지 흐름 ]

1. 클라이언트 → 서버 : SYN (seq = x)
          ↓
2. 서버 → 클라이언트 : SYN+ACK
   (seq = y, ack = x+1)
          ↓
3. 클라이언트 → 서버 : ACK (ack = y+1)
          ↓
연결 수립, 양방향 데이터 전송
```

```text
[ 상태 전이 ]

클라이언트          서버
CLOSED              LISTEN
   ↓ SYN 전송          ↓ SYN 수신
SYN_SENT            SYN_RCVD
   ↓ SYN+ACK 수신      ↓ ACK 수신
ESTABLISHED         ESTABLISHED
```

| 핵심 파라미터 | 표준 | 기능 및 역할 | 성능·보안 영향 |
| --- | --- | --- | --- |
| ISN (초기 시퀀스 번호) | RFC 793, RFC 6528 | 패킷 순서 정렬과 중복 제거의 기준선 | 예측 불가능한 값을 써야 시퀀스 예측 공격을 막을 수 있음 |
| MSS (최대 세그먼트 크기) | RFC 879 | IP 단편화를 피하기 위한 TCP 페이로드 상한 | MTU에서 헤더를 뺀 값 (일반 이더넷 기준 1,460바이트) |
| 윈도우 스케일 | RFC 7323 | 16비트 수신 윈도우의 한계를 확장 | 대역폭 지연 곱이 큰 장거리 고속망의 처리량 향상 |
| SACK 허용 | RFC 2018 | 유실된 세그먼트만 선택적으로 재전송 | 불필요한 전체 재전송과 혼잡 완화 |
| 타임스탬프 | RFC 7323 | RTT(Round-Trip Time) 측정과 시퀀스 번호 재사용 판별 | 고속망에서 오래된 세그먼트 오인 방지 |

- **백로그 큐** (Backlog Queue) : 커널은 SYN_RCVD 상태의 미완결 연결을 담는 SYN 큐와, 3-Way Handshake가 끝나 애플리케이션의 `accept()`를 기다리는 Accept 큐를 나누어 관리.

## Ⅳ. TCP 3-Way Handshake와 전송 방식의 비교

- 핵심 요약 : 최초 데이터 전송 시점을 앞당기는 방향으로 TFO와 QUIC이 발전했으며, 그만큼 상태 저장과 재전송 위험의 관리가 추가로 필요해짐.

| 비교 축 | 일반 TCP 3-Way | TCP Fast Open (TFO, RFC 7413) | QUIC 프로토콜 |
| --- | --- | --- | --- |
| 첫 데이터 시점 | 연결 수립 후 1 RTT 이후 | 재접속 시 SYN에 데이터 포함 | 최초 접속 1 RTT, 재접속 0 RTT |
| 재접속 조건 | 없음 | 이전 접속에서 받은 쿠키 보유 | 세션 재개 정보 보유 |
| 주요 위험 | 연결 상태 고갈 공격 | SYN 데이터 재전송과 일부 중간 장비의 차단 | 0 RTT 데이터의 재전송 공격 |
| 암호화 | 별도 TLS(Transport Layer Security) 핸드셰이크 필요 | 별도 TLS 핸드셰이크 필요 | 전송 계층과 암호화를 통합 |

- 선택 기준 : 호환성이 최우선이면 일반 TCP를, 재접속이 잦은 모바일 웹이면 TFO를, 암호화와 지연을 함께 줄여야 하면 QUIC을 검토.

## Ⅴ. TCP 3-Way Handshake의 한계와 방안

- 핵심 요약 : 연결 상태를 공격자가 고갈시키는 구조와 연결 수립에 드는 왕복 지연이 핵심 한계이며, 상태를 줄이는 설계와 연결 재사용으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| **SYN 플러딩** (SYN Flooding) DDoS(Distributed Denial of Service) | 위조 IP로 SYN만 대량 전송 → SYN 큐가 차서 정상 접속 차단 | **SYN 쿠키** (SYN Cookie, 상태 저장 없이 ISN에 해시를 인코딩하고 3단계 ACK에서 검증), 백로그 튜닝, 방화벽 SYN 프록시 | SYN_RCVD 상태 수, 백로그 드롭 수 |
| 연결 수립의 왕복 지연 | 연결 수립에 최소 1 RTT가 필요하고 TLS가 추가 왕복을 요구 → 짧은 요청의 응답 지연 | TCP Fast Open 적용, 커넥션 재사용, TLS 세션 재개, 장기적으로 QUIC 검토 | TTFB(Time To First Byte), 연결 재사용률 |

## Ⅵ. TCP 3-Way Handshake에 대한 기술사적 제언

- 핵심 요약 : 연결 수립 비용을 서버 상태가 아닌 프록시와 재사용 구조에서 흡수하고, 전송 프로토콜은 점진적으로 전환하는 방향.

웹 서버와 WAS(Web Application Server)는 SYN 쿠키와 백로그 설정을 조직의 표준 템플릿으로 두되, 구체적인 값은 부하 시험으로 정하는 것이 바람직하다. 짧은 연결이 많은 서비스는 로드밸런서나 리버스 프록시가 클라이언트 연결을 종단하고 백엔드와는 커넥션 풀을 유지하는 오프로딩 구조를 택해 백엔드의 핸드셰이크 부담을 줄이는 것이 효과적이다. 장기적으로는 연결 수립과 암호화를 함께 끝내는 QUIC 전환을 점진적으로 검토하되, UDP를 차단하는 망이 남아 있으므로 TCP 경로를 함께 유지하는 이중 운영을 전제로 계획해야 한다.

## Ⅶ. 결론

- 핵심 요약 : TCP 3-Way Handshake는 신뢰성 있는 연결의 출발점이지만, 연결 상태 자체가 공격 표면이 되는 양면성을 가짐.
- 시사점 : SYN 쿠키처럼 서버 상태를 줄이는 설계와 연결 재사용이 성능과 보안을 함께 높이는 열쇠다.
