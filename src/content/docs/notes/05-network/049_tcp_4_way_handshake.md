---
title: "4-way handshake"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:35:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기출 · 74%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "133회"
  priority: 74
  priority_note: "[출제:133]"
---

## 답안 골격
```text
[4-way handshake] ◀━━ 머리: Ⅶ 내 의견 (TIME_WAIT 상태 제어 및 소켓 재사용 설정을 통한 대규모 트래픽 병목 해소)
 ┃
 ┣━ Ⅰ 개요 ───── 전이중(Full-Duplex) TCP 세션의 양방향 데이터 무손실 종료 절차
 ┣━ Ⅱ 특징 ───── 양방향 독립 종료(Half-Close), FIN/ACK 플래그 교환, TIME_WAIT 안전 대기(2MSL)
 ┣━ Ⅲ 구조 ───── 클라이언트 상태(ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED) + 서버 상태
 ┣━ Ⅳ 흐름 ───── ① 클라이언트 FIN 송신 → ② 서버 ACK 송신 → ③ 서버 잔여 데이터 후 FIN 송신 → ④ 클라이언트 최종 ACK
 ┣━ Ⅴ 비교 ───── 3-way handshake vs 4-way handshake (연결 수립 3단계 vs 연결 종료 4단계)
 ┗━ Ⅵ 실무 ───── 과도한 TIME_WAIT 소켓 누수로 로컬 포트 고갈 / 지연 도착 패킷 충돌
```
- 필수 키워드: 전이중 종료 · Half-Close · FIN_WAIT_1/2 · CLOSE_WAIT · TIME_WAIT · 2MSL · SO_REUSEADDR
- 배점 전략: 10점 = Ⅰ → Ⅲ 상태 전이도 및 시퀀스 다이어그램 → Ⅴ 3-way vs 4-way 비교표 / 25점 = 133회 1교시 13번 기출 완벽 대응 (3-way와 4-way 상호 대조 및 TIME_WAIT 해결책 상세)
- 기출: 133회 1교시 13번 `TCP(Transmission Control Protocol) 프로토콜의 3-way handshake와 4-way handshake를 설명하시오.` → Ⅰ~Ⅴ

## 한 줄 본질
- 양방향으로 동시에 데이터를 쏘는 전이중 통신에서 일방적으로 연결을 끊으면 반대편에서 날아오던 잔여 데이터가 유실되는 문제 → 송수신 양측이 각자의 송신 스트림을 독립적으로 닫고 확인 응답을 교환(FIN-ACK, FIN-ACK)하는 4단계 종료 수행 → 잔여 패킷의 안전한 도착과 연결의 우아한 종료(Graceful Close) 보장 / 먼저 종료한 쪽에 남는 TIME_WAIT 소켓 누적에 따른 서버 포트 고갈 위험

## 핵심 그림
```text
[ TCP 4-way handshake 연결 종료 시퀀스 및 상태 전이 ]

  [ 클라이언트 (Active Close) ]                      [ 서버 (Passive Close) ]
       ESTABLISHED                                       ESTABLISHED
            |                                                 |
            |-------- 1. FIN (seq=u) ------------------------>|
        FIN_WAIT_1                                        CLOSE_WAIT
            |                                                 |
            |<------- 2. ACK (ack=u+1) -----------------------| (Half-Close 상태)
        FIN_WAIT_2                                            | (서버 잔여 데이터 계속 전송)
            |                                                 |
            |<------- 3. FIN (seq=w, ack=u+1) ----------------|
            |                                              LAST_ACK
            |-------- 4. ACK (ack=w+1) ---------------------->|
        TIME_WAIT (2MSL 대기!)                                |
            |                                               CLOSED
          CLOSED (타이머 만료 후 소켓 소멸)
```

## 핵심 용어
- Half-Close(절반 종료): 클라이언트가 "나는 더 이상 보낼 데이터가 없다(FIN)"고 선언했으나, 서버가 아직 보내지 못한 잔여 데이터를 마저 다 보낼 수 있도록 한쪽 방향 채널만 열어두는 상태
- TIME_WAIT: 능동적으로 연결 종료를 요청한(Active Close) 단말이 마지막 4번째 ACK를 보낸 뒤, 패킷 유실로 서버가 FIN을 재전송할 경우에 대비해 2MSL 동안 소켓을 닫지 않고 기다리는 상태
- 2MSL(Maximum Segment Lifetime): 패킷이 네트워크 상에서 살아남을 수 있는 최대 수명(MSL, 보통 1~2분)의 2배 동안 대기하여, 이전 세션의 지연 패킷이 다음 새 연결에 섞여 들어가는 것을 방지

## 핵심 통찰
- 연결을 맺을 때는 SYN과 ACK를 묶어서 보낼 수 있어 3단계(3-way)로 끝나지만, 끊을 때는 서버 쪽에 아직 처리 중인 데이터가 남아 있을 수 있어 ACK와 FIN을 분리해 보내야 하므로 반드시 4단계(4-way)가 됨
- 만약 클라이언트가 TIME_WAIT 대기 없이 즉시 소켓을 닫아버리면, 마지막 ACK가 유실되었을 때 서버는 평생 LAST_ACK 상태에 갇혀 자원을 회수하지 못하는 데드락 발생
- 대규모 API 게이트웨이나 웹 프록시 서버에서 수만 건의 연결을 맺고 끊으면 수많은 소켓이 TIME_WAIT 상태로 남아 사용할 수 있는 가용 포트(약 6만 개)가 순식간에 고갈

## 이웃 토픽과 구분
- 3-way handshake vs 4-way handshake: 3-way는 통신을 시작할 때 ISN(초기 순서 번호)을 교환하는 3단계 / 4-way는 통신을 끝낼 때 잔여 데이터 유실 없이 양방향 채널을 닫는 4단계

## 문제·원인·대책
- 적용 상황: 대규모 트래픽을 처리하는 API 프록시 서버의 포트 고갈 장애
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 신규 소켓 생성 실패 (`Cannot assign requested address`) | 서버가 먼저 Close하여 수만 개의 TIME_WAIT 소켓이 로컬 포트 점유 | 커널 파라미터 `tcp_tw_reuse = 1` 및 Keep-Alive 활성화 | 안전한 범위 내에서 TIME_WAIT 소켓을 재사용하고 연결 유지 |
| 서버 프로세스에 CLOSE_WAIT 소켓 무한 누적 | 애플리케이션 개발자가 소켓 `close()` 함수 호출 누락 | 소켓 타임아웃 예외 처리 및 `close()` 명시적 호출 버그 수정 | 자원 누수를 차단하고 소켓 정상 해제 완료 |

## 이렇게 출제된다
- 제133회 1교시 13번: "TCP(Transmission Control Protocol) 프로토콜의 3-way handshake와 4-way handshake를 설명하시오." → 요구 포인트: 양 핸드셰이크의 시퀀스 다이어그램, 상태 전이, Half-Close의 필요성, TIME_WAIT의 역할 비교

## 내 의견
- [HTTP Keep-Alive 활성화를 통한 불필요한 핸드셰이크 제거] 모든 HTTP 요청마다 3-way로 맺고 4-way로 끊는 것은 RTT 지연과 커널 포트 낭비의 주범 → 나라면: 클라이언트와 서버 간 HTTP/1.1 Persistent Connection(Keep-Alive) 또는 HTTP/2 단일 TCP 멀티플렉싱을 필수 적용하여 소켓 종료 빈도를 90% 이상 억제하고 서버 처리량 극대화

## 찾아볼 것
- 리눅스 커널의 `net.ipv4.tcp_fin_timeout` 값 조정 및 위험성
