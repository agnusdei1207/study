---
title: "3-way handshake"
author: "GPT-6"
date: "2026-09-24T21:25:00+09:00"
tags:
  - "notes-network"
extra:
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 핵심 개념 → 3-way handshake

## 30초 인출

- 본질: **3-way handshake** 는 TCP (Transmission Control Protocol) 양 끝점이 연결 요청과 순서 번호를 교환해 연결 상태를 수립하는 절차
- 메커니즘: 클라이언트 SYN → 서버 SYN-ACK → 클라이언트 ACK 순으로 양쪽의 초기 순서 번호와 도달 가능성을 확인

<details>
<summary>핵심 용어</summary>

- **TCP (Transmission Control Protocol)**: 양 끝점 간 연결 상태와 순서·재전송을 관리하는 전송 계층 프로토콜
- **3-way handshake**: TCP 연결 개시 시 SYN·SYN-ACK·ACK를 교환하는 절차
- **ISN (Initial Sequence Number)**: 각 TCP 끝점이 연결에서 시작하는 순서 번호
- **SYN backlog**: 서버가 SYN을 받은 뒤 최종 ACK를 기다리는 미완료 연결 상태를 관리하는 큐
- **SYN cookie**: SYN flood 상황에서 연결 정보를 큐에 저장하는 부담을 줄이도록 응답 순서 번호에 상태 일부를 부호화하는 기법

</details>

---

## 1교시 예상문제 (10점)

> 3-way handshake의 개념과 핵심 구조 또는 동작을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 정의·목적

| 구분 | 핵심 |
|---|---|
| 정의 | **3-way handshake** 는 TCP 양 끝점이 SYN·SYN-ACK·ACK를 교환해 연결 상태와 초기 순서 번호를 확인하는 절차 |
| 목적 | 양 끝점의 연결 요청·응답 가능성과 송수신 순서 기준을 확인 |

### Ⅱ. 핵심 구조와 작동

```text
클라이언트                         서버
CLOSED                             LISTEN
  └─ SYN, seq=x ───────────────────→
SYN-SENT                           SYN-RECEIVED
  ←──────── SYN-ACK, seq=y, ack=x+1
  └─ ACK, ack=y+1 ─────────────────→
ESTABLISHED                        ESTABLISHED
```

제언: 방화벽·로드밸런서의 연결 상태와 서버 backlog 지표를 함께 점검

---

## 2~4교시 예상문제 (25점)

> 3-way handshake의 구조와 동작을 설명하고, 주요 비교 또는 적용 시 문제와 대응책을 제시하시오. (예상)

---

## 2~4교시 25점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **3-way handshake** 는 TCP 양 끝점이 SYN·SYN-ACK·ACK를 교환해 연결 상태와 초기 순서 번호를 확인하는 절차 |
| 목적 | 양 끝점의 연결 요청·응답 가능성과 송수신 순서 기준을 확인 |

### Ⅱ. 연결 수립과 상태 전이

```text
클라이언트                         서버
CLOSED                             LISTEN
  └─ SYN, seq=x ───────────────────→
SYN-SENT                           SYN-RECEIVED
  ←──────── SYN-ACK, seq=y, ack=x+1
  └─ ACK, ack=y+1 ─────────────────→
ESTABLISHED                        ESTABLISHED
```

### Ⅲ. 각 단계의 확인

| 단계 | 세그먼트 | 확인 |
|---|---|---|
| 1 | SYN, seq=x | 클라이언트 요청과 시작 순서 번호 |
| 2 | SYN-ACK, seq=y, ack=x+1 | 서버 요청 수신·자기 번호·클라이언트 SYN 확인 |
| 3 | ACK, ack=y+1 | 서버 SYN 확인 및 양쪽 연결 상태 수립 |

### Ⅳ. 관련 개념과 구분

| 구분 | 3-way handshake | 4-way handshake |
|---|---|---|
| 시점·목적 | 연결 수립 및 순서 번호 확인 | 각 송신 방향의 정상 종료 확인 |
| 메시지 | SYN → SYN-ACK → ACK | FIN → ACK → FIN → ACK |

### Ⅴ. 연결 수립의 한계와 대응

| 한계 | 대응 |
|---|---|
| SYN flood가 미완료 연결 처리 자원을 소모할 수 있음 | SYN cookie 지원·운영체제 설정과 backlog 용량 확인, 앞단 방어·속도 제한 병행 |
| 새 TCP 연결은 애플리케이션 데이터 전송 전 왕복을 요구 | 연결 재사용을 우선 검토; TCP Fast Open (TFO)은 RFC 7413 동작·상대 지원·재전송 조건 확인 |

### Ⅵ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 핸드셰이크 방어만으로 애플리케이션 요청의 위조·중복을 막을 수 없음 | 연결 계층 방어와 분리해 인증·속도 제한·요청 멱등성을 각 계층에 배치 |

## 출제 이력과 검증 출처

- 제133회 1교시 13번: “TCP(Transmission Control Protocol) 프로토콜의 3-way handshake와 4-way handshake를 설명하시오.”
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293.html)
- [RFC 7413, TCP Fast Open](https://www.rfc-editor.org/rfc/rfc7413.html)
