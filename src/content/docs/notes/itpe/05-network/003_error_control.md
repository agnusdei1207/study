---
title: "오류제어(검출·정정·ARQ)"
author: "OpenAI Codex"
date: "2026-09-20T21:36:00+09:00"
tags: ["notes-network"]
sidebar: { badge: { text: "A" } }
extra: { keyword_grade: "A", model: "GPT-5.6 Sol" }
---
<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 21:36 KST</p>

## 지식 로드맵 내 현재 위치
<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 통신</span><span>신뢰성 제어</span><strong>오류제어</strong></div>

## 큰 그림과 30초 인출
- 본질: 전송 중 변형된 비트를 검출하고 정정하거나 재전송하여 신뢰성을 회복함
- 메커니즘: 중복 부호·ACK·Timer·Sequence Number를 채널 오류와 지연 특성에 맞춰 결합함
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
- `ACK(Acknowledgement)`: 수신 성공과 다음 기대 순서를 송신 측에 피드백함
</details>

## 예상문제
- 오류 검출·정정 원리와 ARQ 유형을 설명하고 채널 특성별 선택 기준과 오류제어 대책을 제시하시오.

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
| **ARQ** | ACK·Timer·Sequence | 적응적 복구 | RTT·재전송 |

## Ⅲ. ARQ 유형 비교
> Window 크기와 재전송 범위가 링크 이용률과 복구 트래픽을 가르므로 오류율·RTT·수신 버퍼를 함께 보아야 함.
| 축 | Stop-and-Wait | Go-Back-N | Selective Repeat |
|---|---|---|---|
| Window | 1 | 송신 N | 송·수신 N |
| 오류 복구 | 해당 Frame | 오류 이후 전체 | 오류 Frame만 |
| 순서 | 단순 | 누적 ACK | 개별 ACK·재정렬 |
| 적합 | 짧은 RTT | 낮은 오류율 | 긴 RTT·높은 오류율 |

## Ⅳ. 채널 적응형 오류제어 결론
> 단일 방식의 강제보다 잔류 오류·Goodput·복구 지연을 함께 측정하여 FEC와 ARQ를 조정하는 Hybrid ARQ가 실무적임.
### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 강한 부호는 오류를 줄이지만 정상 채널에서도 중복 비용을 낸다. 복구 방식은 평균 오류율만이 아니라 RTT와 Burst 길이에 좌우된다.
- `나라면`: 채널별 오류 패턴을 측정하고 서비스 지연 한계를 고정한 뒤 FEC 강도와 재전송 횟수를 조정하겠다.
### 실전 답안용 기술사적 제언
- 판정: 잔류 오류·Goodput·복구 지연의 서비스 허용범위 충족
- 대안: Adaptive FEC와 선택 재전송을 결합한 Hybrid ARQ
- 검증: 정상·Burst 오류 주입 후 누락·중복·순서·지연 확인
- 효과: 과잉 중복과 재전송 폭주를 동시에 억제
<div class="itpe-flow itpe-flow--vertical" aria-label="오류제어 개선">
  <div class="itpe-flow__node"><strong>고정 제어</strong><small><b>문제:</b> 채널 변화와 중복량 불일치</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><strong>채널 적응</strong><small><b>대안:</b> FEC 강도 · Window · 재전송 한도 조정</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><strong>오류 주입</strong><small><b>판정:</b> 잔류 오류 · Goodput · 지연</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><strong>신뢰 전달</strong><small><b>효과:</b> 오류 복구와 자원 효율 균형</small></div>
</div>

## 1교시 10점 답안 발췌
- 정의: **오류제어**는 **오류 검출·정정 부호**와 **ARQ(Automatic Repeat reQuest)**로 전송 오류를 식별·복구하는 신뢰성 제어임
- 목적: 잔류 오류 통제 → 데이터 무결성 확보
<div class="itpe-flow itpe-flow--vertical" aria-label="오류제어 1교시 그림"><div class="itpe-flow__node"><strong>검출</strong><small><b>활동:</b> CRC 판정</small><small><b>산출:</b> 정상·오류</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>복구</strong><small><b>활동:</b> FEC 또는 ARQ</small><small><b>산출:</b> 정정 Data</small></div></div>
| 축 | Go-Back-N | Selective Repeat |
|---|---|---|
| 재전송 | 오류 이후 전체 | 오류 Frame |
| 대가 | 중복 전송 | Buffer·재정렬 |
- 결론: RTT·오류 패턴·지연 한계로 FEC와 ARQ를 선택하고 오류 주입으로 검증함

## 출제 이력과 검증 출처
- 제137·138회: 원문 미확보(회차만 확인)
- [RFC 9293, Transmission Control Protocol](https://www.rfc-editor.org/rfc/rfc9293)
- [RFC 6298, Computing TCP's Retransmission Timer](https://www.rfc-editor.org/rfc/rfc6298)

## 학습 체크
- [ ] Ⅰ 개요: 검출·정정·ARQ의 관계와 목적을 재현할 수 있는가?
- [ ] Ⅱ 표: CRC·FEC·ARQ의 원리·대가를 비교할 수 있는가?
- [ ] Ⅲ 표: 세 ARQ를 Window·재전송·적합 채널로 비교할 수 있는가?
- [ ] Ⅳ 제언: 문제·대안·판정·효과를 연결할 수 있는가?

## 연결 토픽
- [ARQ](./015_arq/) · [Go-Back-N ARQ](./020_go_back_n_arq/) · [CRC](./068_crc/) · [슬라이딩 윈도우](./018_sliding_window/)
