---
title: "오류제어(검출·정정·ARQ)"
author: "OpenAI Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-network"]
sidebar: { badge: { text: "A" } }
extra: { keyword_grade: "A", model: "GPT-5.6 Sol" }
---
<p class="itpe-byline">작성 모델 · GPT-6<br />작성 · 2026.09.24 21:00 KST</p>

## 지식 로드맵 내 현재 위치
<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 통신</span><span>신뢰성 제어</span><strong>오류제어</strong></div>

## 큰 그림과 30초 인출
- 본질: 전송 중 변형된 비트를 검출하고 정정하거나 재전송하여 신뢰성을 회복함
- 메커니즘: 중복 부호·ACK(Acknowledgement)·Timer·Sequence Number를 채널 오류와 지연 특성에 맞춰 결합함
- 산출: 잔류 오류·재전송 지연·중복 트래픽 사이의 통제된 균형임
<div class="itpe-flow itpe-flow--vertical" aria-label="오류제어 흐름">
  <div class="itpe-flow__node"><strong>송신 부호화</strong><small><b>입력:</b> Data</small><small><b>산출:</b> 검사용 Redundancy</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>오류 검출</strong></span><small><b>판정:</b> Parity · Checksum · CRC</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><strong>복구 선택</strong><small><b>대안:</b> FEC 정정 또는 ARQ 재전송</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><strong>신뢰 전달</strong><small><b>산출:</b> 순서 보존 · 잔류 오류 통제</small></div>
</div>
<details><summary>핵심 용어</summary>

- `CRC(Cyclic Redundancy Check)`: 다항식 나눗셈의 나머지로 Burst 오류를 검출함
- `FEC(Forward Error Correction)`: 수신 측 정정을 위해 추가 중복을 전송함
- `ARQ(Automatic Repeat reQuest)`: 오류·손실 프레임을 ACK와 Timer로 재전송함
- `ACK(Acknowledgement)`: ARQ에서는 프레임 수신 성공을, TCP에서는 누적된 다음 기대 순서를 피드백함
</details>

---

## 1교시 예상문제 (10점)
> 오류제어의 개념과 검출·정정·재전송 방식을 설명하시오. (예상)

---

## 1교시 10점 답안
### 1. 정의·목적
- 정의: 오류제어는 검출·정정 부호와 **ARQ(Automatic Repeat reQuest)** 를 사용해 전송 오류를 식별하고 복구하는 방식이다.
- 목적: 잔류 오류와 손실을 줄여 데이터 무결성을 확보한다.

| 방식 | 역할 | 한계 |
|---|---|---|
| **CRC** | 오류 검출 | 자체 정정은 못함 |
| **FEC** | 추가 부호로 수신 측 정정 | 중복 전송량 증가 |
| **ARQ** | ACK·Timer를 사용해 재전송 | RTT와 재전송 지연 |

- 제언: 오류율과 RTT에 맞춰 FEC와 ARQ를 선택하고 시험한다.

---

## 2~4교시 예상문제 (25점)
> 오류 검출·정정과 ARQ의 원리를 설명하고, ARQ 유형을 비교한 뒤 채널 특성별 선택 및 개선 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 중복정보로 신뢰성을 회복하는 오류제어 개요
> 오류제어는 오류를 없애는 기술이 아니라 검출 누락·중복량·재전송 지연의 대가를 채널에 맞게 배분하는 기술임.

- 정의: **오류제어**는 **오류 검출·정정 부호**와 **ARQ(Automatic Repeat reQuest)**로 전송 오류를 식별·복구하는 신뢰성 제어임
- 목적: 잔류 오류와 손실을 통제 → 상위 서비스의 데이터 무결성 확보

## Ⅱ. 검출·정정·재전송 구성과 동작
> 검출은 복구의 출발점이며, 왕복지연이 큰 채널은 FEC를, 오류율이 낮고 피드백이 빠른 채널은 ARQ를 우선함.

| 방식 | 원리 | 강점 | 대가 |
|---|---|---|---|
| Parity | 1 bit 중복 | 단순 | 짝수 오류 누락 |
| Checksum | Word 합 | 구현 용이 | Burst 검출 한계 |
| **CRC** | 생성다항식 나머지 | Burst 검출 | 자체 정정 불가 |
| **FEC** | Code Distance | 무재전송 정정 | 대역폭·연산 |
| **ARQ** | ACK·Timer·Sequence | 적응적 복구 | RTT(Round-Trip Time)·재전송 |

## Ⅲ. ARQ 유형 비교
> Window 크기와 재전송 범위가 링크 이용률과 복구 트래픽을 가르므로 오류율·RTT·수신 버퍼를 함께 보아야 함.

| 축 | Stop-and-Wait | Go-Back-N | Selective Repeat |
|---|---|---|---|
| Window | 1 | 송신 N | 송·수신 N |
| 오류 복구 | 해당 Frame | 오류 이후 전체 | 오류 Frame만 |
| 순서 | 단순 | 누적 ACK | 개별 ACK·재정렬 |
| 적합 | 짧은 RTT | 낮은 오류율 | 긴 RTT·높은 오류율 |

## 기술사적 제언

| 문제 | 해결 방안 |
|---|---|
| 고정된 부호 강도와 재전송 설정은 채널 오류·왕복 지연이 달라질 때 중복 전송이나 복구 지연을 키울 수 있음 | 오류 패턴과 RTT를 측정해 FEC 강도·재전송 범위를 조정하고 오류 주입 시험으로 확인 |

## 출제 이력과 검증 출처
- 제137·138회: 원문 미확보(회차만 확인)
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 6298, Computing TCP's Retransmission Timer](https://www.rfc-editor.org/rfc/rfc6298)
- [ITU-T X.25, LAPB의 Go-Back-N ARQ 절차](https://www.itu.int/rec/T-REC-X.25/en)
- [RFC 3366, Advice to link designers on link Automatic Repeat reQuest](https://www.rfc-editor.org/rfc/rfc3366)
- [RFC 3385, Internet Protocol Small Computer System Interface cyclic redundancy check](https://www.rfc-editor.org/rfc/rfc3385)
- [RFC 6363, Forward Error Correction Framework](https://www.rfc-editor.org/rfc/rfc6363)
- [RFC 1982, Serial Number Arithmetic for Sequence Number Space](https://www.rfc-editor.org/rfc/rfc1982)

## 연결 토픽
- [ARQ](./015_arq/) · [Go-Back-N ARQ](./020_go_back_n_arq/) · [CRC](./068_crc/) · [슬라이딩 윈도우](./018_sliding_window/)
