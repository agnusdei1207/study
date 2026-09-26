---
title: "4-way handshake"
author: "Gemini 3.8 Flash"
date: "2026-09-24T21:25:00+09:00"
tags:
  - "notes-network"
extra:
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 핵심 개념 → 4-way handshake

## 30초 인출

- 본질: **4-way handshake** 는 TCP (Transmission Control Protocol) 양방향 송신을 각각 종료하는 정상 연결 해제 절차
- 메커니즘: 한쪽 FIN을 상대가 ACK하고, 상대도 송신을 마친 뒤 FIN을 보내면 첫 쪽이 ACK

<details>
<summary>핵심 용어</summary>

- **TCP (Transmission Control Protocol)**: 양 끝점 간 연결 상태와 순서·재전송을 관리하는 전송 계층 프로토콜
- **Half-Close**: 한 방향 송신만 끝난 상태로, 반대 방향 데이터의 수신은 계속 가능한 TCP 상태
- **4-way handshake**: 양 끝점이 FIN과 ACK를 주고받아 TCP의 두 송신 방향을 각각 종료하는 절차
- **TIME-WAIT**: 능동 종료 측이 최종 ACK 뒤 일정 시간 대기해 상대 FIN 재전송에 응답하고 이전 연결의 지연 세그먼트가 새 연결에 섞이는 일을 막는 상태
- **MSL (Maximum Segment Lifetime)**: IP 네트워크에서 세그먼트가 유효할 수 있는 최대 시간

</details>

---

## 1교시 예상문제 (10점)

> TCP 4-way handshake의 개념과 FIN·ACK를 이용한 연결 종료 절차를 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 정의·목적

| 구분 | 핵심 |
|---|---|
| 정의 | **4-way handshake** 는 TCP 양 끝점이 각 방향의 송신 종료를 FIN과 ACK로 개별 확인하는 정상 연결 해제 절차 |
| 목적 | 미전달 데이터의 수신을 마친 뒤 양방향 연결을 종료 |

### Ⅱ. 핵심 구조와 작동

```text
A: 능동 종료                         B: 수동 종료
ESTABLISHED                         ESTABLISHED
    └─ FIN ───────────────────────────→
FIN-WAIT-1                          CLOSE-WAIT
    ←────────────────────────────── ACK
FIN-WAIT-2                          CLOSE-WAIT
                                     (남은 데이터 송신 가능)
    ←────────────────────────────── FIN
TIME-WAIT                           LAST-ACK
    └─ ACK ───────────────────────────→ CLOSED
    │
  2 MSL 대기
    ↓
CLOSED
```

제언: 능동·수동 종료 상태와 FIN/ACK 로그를 함께 대조해 연결 정리 지연을 진단

---

## 2~4교시 예상문제 (25점)

> TCP 4-way handshake의 FIN·ACK 교환과 종료 상태를 설명하고, 3-way handshake와 비교하여 운영 시 주의할 점을 제시하시오. (예상)

---

## 2~4교시 25점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **4-way handshake** 는 TCP 양 끝점이 각 방향의 송신 종료를 FIN과 ACK로 개별 확인하는 정상 연결 해제 절차 |
| 목적 | 미전달 데이터의 수신을 마친 뒤 양방향 연결을 종료 |

### Ⅱ. 종료 순서와 상태

```text
A: 능동 종료                         B: 수동 종료
ESTABLISHED                         ESTABLISHED
    └─ FIN ───────────────────────────→
FIN-WAIT-1                          CLOSE-WAIT
    ←────────────────────────────── ACK
FIN-WAIT-2                          CLOSE-WAIT
                                     (남은 데이터 송신 가능)
    ←────────────────────────────── FIN
TIME-WAIT                           LAST-ACK
    └─ ACK ───────────────────────────→ CLOSED
    │
  2 MSL 대기
    ↓
CLOSED
```

### Ⅲ. 종료 특성

| 관점 | 핵심 |
|---|---|
| 독립 송신 방향 | 각 끝점이 자기 데이터 송신 종료를 별도로 결정하므로 FIN과 ACK 교환이 필요 |
| Half-Close | 한쪽 FIN을 받은 뒤에도 상대 송신이 끝날 때까지 열린 방향의 데이터 수신 가능 |
| TIME-WAIT | 능동 종료 측이 2×MSL 동안 대기해 최종 ACK 재전송에 대응하고 지연 세그먼트와 새 연결을 분리 |

### Ⅳ. 관련 개념과 구분

| 구분 | 3-way handshake | 4-way handshake |
|---|---|---|
| 시점 | 연결 수립 | 정상 연결 종료 |
| 핵심 교환 | SYN, SYN-ACK, ACK | FIN, ACK, FIN, ACK |
| 이유 | 양 끝점의 초기 순서 번호와 도달 확인 | 각 방향의 송신 종료가 독립적 |

### Ⅴ. 적용 한계와 대응

| 한계 | 대응 |
|---|---|
| 짧은 연결을 과도하게 반복하면 TIME-WAIT 소켓과 포트 사용량 증가 | 연결 재사용·풀링을 먼저 검토하고, 실제 튜플·포트 범위와 커널 동작을 측정한 뒤 설정 변경 |
| CLOSE-WAIT 누적은 애플리케이션이 로컬 소켓을 닫지 않는 징후 | 프로세스별 상태 수와 종료 경로를 추적해 닫기 누락·예외 처리를 수정 |

### Ⅵ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 종료 지연은 TCP 상태만으로 애플리케이션의 원인을 확정하기 어려움 | 요청 ID 기준으로 FIN/ACK와 프로세스 소켓 상태를 함께 기록해 장애 원인을 구분 |

## 출제 이력과 검증 출처

- 제133회 1교시 13번: “TCP(Transmission Control Protocol) 프로토콜의 3-way handshake와 4-way handshake를 설명하시오.”
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html)
