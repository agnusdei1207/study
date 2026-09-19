---
title: "3-way handshake"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:35:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기출 · 72%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "133회"
  priority: 72
  priority_note: "[출제:133]"
---

## 답안 골격
```text
[3-way handshake] ◀━━ 머리: Ⅶ 내 의견 (SYN Cookie 및 TCP Fast Open을 통한 보안성 및 연결 지연 개선)
 ┃
 ┣━ Ⅰ 개요 ───── 비신뢰적 IP망 위에서 신뢰성 있는 가상 회선 수립 → 초기 순서 번호(ISN) 동기화
 ┣━ Ⅱ 특징 ───── 양방향 순서 번호 동기화(SYN), 전이중 연결 수립, 버퍼 및 윈도우 협상, 신뢰성 보장
 ┣━ Ⅲ 구조 ───── 클라이언트 상태(CLOSED → SYN_SENT → ESTABLISHED) + 서버 상태(LISTEN → SYN_RCVD → ESTABLISHED)
 ┣━ Ⅳ 흐름 ───── ① Client SYN (ISN_c 전송) → ② Server SYN-ACK (ISN_s 및 ACK_c+1 전송) → ③ Client ACK (ACK_s+1 전송)
 ┣━ Ⅴ 비교 ───── 3-way handshake vs UDP 무연결 (1 RTT 사전 지연 vs 0 RTT 즉시 전송)
 ┗━ Ⅵ 실무 ───── SYN Flooding 공격(백로그 큐 고갈) / 초기 연결 지연(1 RTT Overhead)
```
- 필수 키워드: ISN(초기 순서 번호) · SYN · SYN-ACK · ACK · SYN_SENT · SYN_RCVD · ESTABLISHED · SYN Cookie · TCP Fast Open
- 배점 전략: 10점 = Ⅰ → Ⅲ 시퀀스 다이어그램 및 시퀀스/ACK 번호 계산도 → Ⅴ UDP 비교표 / 25점 = 133회 1교시 13번 기출 완벽 대응 (3-way와 4-way 상호 대조 및 SYN Flooding 방어 메커니즘 상세)
- 기출: 133회 1교시 13번 `TCP(Transmission Control Protocol) 프로토콜의 3-way handshake와 4-way handshake를 설명하시오.` → Ⅰ~Ⅴ

## 한 줄 본질
- 서로 다른 컴퓨터가 임의로 데이터를 보내면 수신측이 패킷의 시작 순서와 수용 가능 여부를 모르는 혼란 → 송신측과 수신측이 각자의 난수 초기 순서 번호(ISN)를 SYN-ACK 3단계로 상호 교환하고 확인 응답을 완결 → 순서 보장과 신뢰성 있는 전이중 파이프라인 수립 / 1 RTT 연결 설정 지연 발생 및 가짜 SYN을 쏟아붓는 SYN Flooding 디도스 취약점 노출

## 핵심 그림
```text
[ TCP 3-way handshake 연결 수립 시퀀스 및 상태 전이 ]

  [ 클라이언트 (Client) ]                                [ 서버 (Server) ]
        CLOSED                                                LISTEN (대기 중)
          |                                                     |
          |----------- 1. SYN (seq = ISN_c) ------------------->|
      SYN_SENT                                               SYN_RCVD (백로그 큐 할당)
          |                                                     |
          |<---------- 2. SYN-ACK (seq = ISN_s, ack = ISN_c+1) -|
          |                                                     |
     ESTABLISHED                                                |
          |----------- 3. ACK (ack = ISN_s+1) ----------------->|
          |                                                ESTABLISHED (연결 완료!)
          |                                                     |
          |=============== 실제 애플리케이션 데이터 전송 ========>|
```

## 핵심 용어
- ISN(Initial Sequence Number): TCP 연결 수립 시 양측이 각각 독립적으로 생성하는 32비트 초기 순서 번호. 이전 연결의 지연 패킷과의 혼동 및 스푸핑 공격을 막기 위해 0이 아닌 암호학적 의사 난수로 생성
- SYN 백로그 큐(Backlog Queue): 1단계 SYN 패킷을 받은 서버가 3단계 최종 ACK가 올 때까지 미완결 연결(Half-open Connection) 상태로 TCB 자원을 보관해 두는 커널 메모리 큐
- SYN Cookie: 2단계에서 서버가 메모리 자원을 할당하지 않고, 클라이언트의 IP/포트와 타임스탬프를 암호화 해시한 값을 ISN_s로 삼아 돌려보냄으로써 백로그 큐 고갈을 원천 무력화하는 방어 기술

## 핵심 통찰
- 왜 2단계(2-way)가 아니라 3단계인가? → A가 B에게 "내 번호 동기화해줘(SYN)" 하고 B가 "알았다(ACK)" 하는 것은 A→B 방향의 편도 연결만 확인된 것이며, B→A 방향의 연결을 위해 B의 ISN을 A가 "확인했다(ACK)"는 3번째 신호가 필수적이기 때문
- 웹 브라우징에서 3-way handshake는 첫 데이터를 보내기도 전에 무조건 왕복 지연 1 RTT를 소비하므로, 단거리 통신에서도 최소 수십 밀리초의 지연 유발
- 이를 극복하기 위해 구글은 첫 핸드셰이크에 쿠키를 발급받아 재방문 시 1단계 SYN 패킷에 HTTP 요청 데이터를 바로 실어 보내는 TCP Fast Open(RFC 7913)을 제정

## 이웃 토픽과 구분
- 3-way handshake vs 4-way handshake: 3-way는 통신을 시작하며 ISN을 맞추는 3단계 / 4-way는 통신을 종료하며 양방향 잔여 데이터를 안전하게 회수하는 4단계

## 문제·원인·대책
- 적용 상황: 웹 서버를 대상으로 한 대규모 SYN Flooding DDoS 공격
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 정상 사용자의 웹 사이트 접속 불능 | 위조된 IP로 대량의 가짜 SYN을 보내 서버 백로그 큐를 가득 채움 | 리눅스 커널 파라미터 `net.ipv4.tcp_syncookies = 1` 활성화 | 미완결 소켓 메모리 할당을 제거하여 무제한 SYN 공격 방어 |
| 모바일 웹 로딩 첫 화면 지연(Latency) | 매 HTTP 연결마다 1 RTT의 핸드셰이크 지연 누적 | TCP Fast Open(TFO) 활성화 또는 HTTP/3(QUIC 0-RTT) 도입 | 재접속 시 핸드셰이크 단계에서 데이터 즉시 전송 |

## 이렇게 출제된다
- 제133회 1교시 13번: "TCP(Transmission Control Protocol) 프로토콜의 3-way handshake와 4-way handshake를 설명하시오." → 요구 포인트: 3-way 동작 절차, 상태 전이(LISTEN, SYN_RCVD, ESTABLISHED), ISN과 ACK 번호 증분 규칙, 연결 수립의 목적

## 내 의견
- [HTTP/3(QUIC) 시대로의 전송 계층 패러다임 전환] TCP의 3-way handshake는 TLS 암호화 핸드셰이크(1~2 RTT)와 결합되어 최초 연결 시 최대 3 RTT의 극심한 지연 발생 → 나라면: 신규 대고객 웹 서비스 구축 시 UDP 기반에 TLS 1.3을 일체형으로 통합한 HTTP/3(QUIC)를 프론트엔드 역방향 프록시에 전면 적용하여, 첫 연결 지연을 1 RTT로 줄이고 재접속 시 0-RTT 즉시 전송을 구현

## 찾아볼 것
- RFC 793의 TCP 상태 전이도(FSM)와 RFC 7913 TCP Fast Open(TFO) 옵션 규격
