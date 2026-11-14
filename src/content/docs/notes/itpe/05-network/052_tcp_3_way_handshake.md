---
title: "3-way handshake"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "052"
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- TCP 3-Way Handshake, SYN, ACK, 초기 시퀀스 번호(ISN)
- SYN_SENT, SYN_RCVD, ESTABLISHED, 백로그 큐
- SYN 플러딩, SYN 쿠키, 커넥션 재사용

## Ⅰ. TCP 3-Way Handshake의 개요

- 핵심 요약 : 세 번의 SYN·ACK 교환으로 양단의 시퀀스 기준과 전송 조건을 맞추는 TCP 연결 수립 절차.
- 개념 : 데이터 전송에 앞서 두 종단이 SYN(Synchronize)과 ACK(Acknowledgment)를 세 단계로 교환해 **초기 시퀀스 번호** (ISN, Initial Sequence Number)를 동기화하는 절차(**TCP 3-Way Handshake**).
- 배경 및 필요성 : IP(Internet Protocol) 네트워크에서는 패킷의 유실·지연·순서 역전이 발생하므로, 수신측이 정상 데이터를 판별할 순서 기준이 전송 전에 필요.
- 주요 목적 : 양방향 시퀀스 기준선의 일치, MSS(Maximum Segment Size) 등 전송 옵션의 사전 협상, 양단 연결 상태의 일치.

## Ⅱ. TCP 3-Way Handshake의 특징 및 장점

- 핵심 요약 : 연결 전에 상태와 옵션을 합의해 이후 데이터 전송의 순서·품질·지연을 함께 관리하는 구조.

1. 시퀀스 동기화 : 양단이 각자의 ISN을 알리고 상대값을 확인 (ack = x+1) → 순서 복원과 중복 제거의 기준 확보 효과.
2. 옵션 협상 : SYN 세그먼트에 MSS, 윈도우 스케일(Window Scale), SACK(Selective Acknowledgment) 허용을 실어 교환 → 양단 능력에 맞는 전송 조건 확정 효과.
3. 3회 최소 구조 : 세 번째 ACK에 애플리케이션 데이터를 함께 실을 수 있음 → 첫 요청까지의 왕복 지연 절감 효과.

## Ⅲ. TCP 3-Way Handshake의 구조 (흐름)

- 핵심 요약 : 세 개의 메시지로 능동 개설측과 수동 개설측이 같은 시점에 ESTABLISHED로 수렴하는 흐름.

```text
[ 3-Way 메시지 흐름 ]

1. A → B : SYN (seq = x)
        ↓
2. B → A : SYN+ACK
   (seq = y, ack = x+1)
        ↓
3. A → B : ACK (ack = y+1)
        ↓
연결 수립 (ESTABLISHED)
```

```text
[ 능동 개설측 상태 전이 ]

CLOSED
   ↓ SYN 전송
SYN_SENT
   ↓ SYN+ACK 수신, ACK 전송
ESTABLISHED
```

```text
[ 수동 개설측 상태 전이 ]

LISTEN
   ↓ SYN 수신, SYN+ACK 전송
SYN_RCVD
   ↓ ACK 수신
ESTABLISHED
```

- **백로그 큐** (Backlog Queue) : 커널이 SYN_RCVD 상태의 미완결 연결을 담는 큐와 수립 완료 후 애플리케이션 수용 대기 큐로 구분해 관리하는 구조.

## Ⅳ. TCP 3-Way Handshake와 4-Way Handshake의 비교

- 핵심 요약 : 3-Way는 상태를 여는 수립 절차, 4-Way는 방향별로 닫는 해제 절차로 교환 횟수와 결합 방식이 다름.

| 비교 축 | 3-Way (수립) | 4-Way (해제) |
| --- | --- | --- |
| 교환 횟수 | 3회 | 4회 |
| 결합 방식 | SYN과 ACK를 한 세그먼트로 결합 | 종료 시점이 방향마다 달라 FIN(Finish)과 ACK 분리 |
| 상태 목표 | 양단 동시 ESTABLISHED | 능동측 TIME_WAIT 경유 후 CLOSED |
| 직후 동작 | 즉시 양방향 데이터 전송 | 잔여 데이터 전송 후 종료 |

- 선택 기준 : 수립은 표준 3-Way를, 해제는 데이터 무결성을 위해 FIN 기반 4-Way를 사용하는 상호 보완 절차로 대체 관계가 아님.

## Ⅴ. TCP 3-Way Handshake의 한계와 방안

- 핵심 요약 : 연결 상태를 겨냥한 자원 고갈 공격과 수립 왕복 지연을 상태 절감 설계와 재사용으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| **SYN 플러딩** (SYN Flooding) | 위조 발신지로 SYN만 대량 전송 → 미완결 연결 큐 포화와 정상 접속 거부 | **SYN 쿠키** (SYN Cookie, 연결 상태 저장 없이 ISN에 검증값을 넣고 최종 ACK에서 확인), SYN 프록시 | SYN_RCVD 수, 큐 드롭 수 |
| 수립 왕복 지연 | 최소 1 RTT(Round-Trip Time)에 TLS(Transport Layer Security) 왕복이 추가 → 짧은 트랜잭션의 응답 지연 | 커넥션 풀과 Keep-Alive 재사용, TLS 세션 재개 | 연결 재사용률, TTFB(Time To First Byte) |

## Ⅵ. TCP 3-Way Handshake에 대한 기술사적 제언

- 핵심 요약 : 수립 비용을 서버 상태가 아닌 표준 설정과 프록시 구조에서 흡수하고 전송 프로토콜 전환을 단계 준비하는 방향.

1. 서비스 운영 조직은 SYN 쿠키 전환 기준과 백로그 크기를 부하 시험 기반 표준 템플릿으로 관리.
2. 플랫폼 조직은 로드밸런서가 외부 연결을 종단하고 백엔드는 커넥션 풀을 유지하는 오프로딩 구조로 수립 부담을 흡수.
3. 아키텍처 조직은 연결 수립과 암호화를 함께 줄이는 QUIC 전환을 TCP 경로 병행 전제로 단계 검토.

## Ⅶ. 결론

- 핵심 요약 : TCP 3-Way Handshake는 신뢰성 전송의 출발점이자 연결 상태가 공격 표면이 되는 지점.
- 시퀀스 동기화의 원리를 지키면서 연결 상태 부담을 구조적으로 줄이는 설계가 고성능 서비스의 조건.
