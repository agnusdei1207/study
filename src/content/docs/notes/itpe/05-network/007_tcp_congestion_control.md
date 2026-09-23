---
title: "TCP 혼잡제어(Congestion Control)"
author: "OpenAI Codex"
date: "2026-09-24T21:00:00+09:00"
tags:
  - "notes-network"
extra:
  model: "GPT-6"

---

## 큰 그림과 30초 인출

```text
          ACK·loss·ECN·RTT feedback
       ┌─────────────────────────────┐
       ▼                             │
[Sender: cwnd] ── 전송률 조절 ──▶ [Network queue] ──▶ Receiver
   │                                  │
   ├─ Slow Start: 빠른 탐색            └─ 혼잡 신호
   ├─ Avoidance: 완만한 증가
   └─ Recovery: 감소·재전송

실제 전송창 = min(cwnd, rwnd)
```

- 본질: 송신자가 명시적 예약 없이 ACK·손실·ECN·RTT 피드백으로 경로의 수용량을 탐색하는 폐루프 제어
- 인출: `SS → CA → FR`, 핵심 상태는 `cwnd·ssthresh·RTT`
- 구분: 흐름제어는 receiver 보호, 혼잡제어는 network 보호
- 현대화: Reno만 외우지 않고 CUBIC·QUIC의 손실 탐지와 운영 지표까지 연결

---

## 1교시 예상문제 (10점)

> TCP 혼잡제어의 목적과 cwnd를 이용한 핵심 동작을 설명하시오. (예상)

---

## 1교시 10점 답안

- 정의: TCP 혼잡제어는 송신자가 경로의 혼잡 신호에 따라 혼잡 윈도(cwnd)를 조절하는 폐루프 제어이다.
- 목적: 네트워크 혼잡을 완화하면서 경로 용량을 효율적으로 사용한다.

```text
전송(cwnd) → ACK·RTT·loss·ECN 관측 → cwnd 조정 → 다음 전송량 결정
```

| 구분 | 보호 대상 |
|---|---|
| 흐름제어(rwnd) | 수신자 버퍼 |
| 혼잡제어(cwnd) | 네트워크 경로 |

제언: 처리량과 함께 RTT·손실·재전송을 관찰해 제어 동작을 검증한다.

---

## 2~4교시 예상문제 (25점)

> TCP 혼잡제어의 원리와 상태전이, Slow Start·Congestion Avoidance·Fast Retransmit/Recovery를 설명하고 CUBIC 및 QUIC과 비교한 뒤 운영 고려사항을 논하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. ACK clock으로 경로 수용량을 탐색하는 TCP 혼잡제어 개요

- 정의: TCP 혼잡제어는 송신자가 `cwnd(congestion window)`를 조절하여 ACK가 확인되지 않은 in-flight data를 제한하고 네트워크 혼잡 붕괴를 방지하는 end-to-end 제어
- 목적: 경로 용량을 효율적으로 사용하면서 손실·queue 지연·재전송 폭증 방지
- 필요성: 여러 흐름이 공유 병목으로 동시에 유입되면 queue overflow와 timeout이 연쇄 발생하므로 각 송신자가 피드백에 따라 전송량을 조정해야 함

#### 한줄 요약

- TCP 혼잡제어는 ACK로 증가하고 혼잡 신호로 감소하는 송신측 피드백 제어임

## Ⅱ. 분산·적응·공정성을 지향하는 특징

| 특징 | 구현 | 효과 | 한계 |
|---|---|---|---|
| **End-to-End** | sender가 ACK·loss·ECN 해석 | 망 예약 없이 동작 | 혼잡 원인과 무선 손실 구분 어려움 |
| **ACK clock** | ACK 도착에 맞춰 새 segment 전송 | 경로 배출률 추종 | ACK 압축·지연의 영향 |
| **AIMD 계열** | 증가 후 혼잡 시 multiplicative decrease | 흐름 간 수렴·공정성 | 고 BDP 경로의 회복 지연 |
| **상태 전이** | Slow Start·Avoidance·Recovery | 탐색과 안정 운용 분리 | 전환 임계값 튜닝 필요 |
| **알고리즘 진화** | Reno·CUBIC·delay/model 기반 | 경로별 성능 개선 | 알고리즘 간 공존성 검증 필요 |

#### 한줄 요약

- 혼잡제어는 최대 전송이 아니라 공유 병목에서 안정성과 공정성을 유지하며 가용 용량에 수렴하는 기술임

## Ⅲ. cwnd·ssthresh·수신창으로 구성되는 제어 구조

```text
Application data
      │
      ▼
┌──────── TCP Sender ────────┐
│ send window=min(cwnd,rwnd) │
│ cwnd: 경로 혼잡 한도       │
│ rwnd: 수신 버퍼 한도       │
│ ssthresh: SS/CA 경계       │
└───────────┬───────────────┘
            │ segments
            ▼
      [Router queue/path]
            │ ACK·loss·ECN·RTT
            └───────────────▶ 상태·창 갱신
```

| 상태·신호 | 의미 | 제어 결과 |
|---|---|---|
| **cwnd** | 혼잡제어가 허용하는 in-flight 한도 | 송신률 직접 제한 |
| **rwnd** | receiver가 광고한 buffer 한도 | 흐름제어 제한 |
| **ssthresh** | 지수 증가와 혼잡회피의 경계 | 상태 전환 |
| **duplicate ACK/SACK** | 중간 segment 손실 정황 | timer 전 빠른 복구 |
| **RTO/PTO** | 응답 부재에 대한 timer | 재전송 probe와 보수적 복구 |
| **ECN-CE** | router가 표시한 혼잡 | drop 전 감소 가능 |

#### 한줄 요약

- 송신률은 cwnd와 rwnd 중 작은 값으로 제한되고, cwnd는 경로 피드백에 따라 계속 변함

## Ⅳ. 탐색·회피·복구로 이어지는 TCP 상태전이

```text
연결 시작/timeout
      │
      ▼
[Slow Start] cwnd 빠르게 증가
      │ cwnd ≥ ssthresh
      ▼
[Congestion Avoidance] 완만한 증가
      │ duplicate ACK / loss
      ▼
[Fast Retransmit·Recovery] 손실 segment 재전송, cwnd 감소
      │ recovery ACK
      └──────────────▶ Congestion Avoidance
```

| 단계 | cwnd 동작 | 종료 조건 | 의도 |
|---|---|---|---|
| **Slow Start** | ACK에 따라 빠르게 확대 | ssthresh 도달·혼잡 감지 | 가용 용량 탐색 |
| **Congestion Avoidance** | RTT당 완만한 증가 | 손실·ECN | 안정적 용량 추종 |
| **Fast Retransmit** | duplicate ACK로 누락 추정 후 즉시 재전송 | 손실 segment 전송 | RTO 대기 회피 |
| **Fast Recovery** | ssthresh·cwnd 감소 후 ACK clock 유지 | 새 data ACK | pipeline 붕괴 완화 |
| **Timeout Recovery** | 더 보수적으로 cwnd 축소 | ACK 재수신 | 심한 혼잡에서 재탐색 |

#### 한줄 요약

- ACK가 오면 창을 키우고 손실·ECN이 나타나면 창을 줄이며, duplicate ACK와 timer를 구분해 복구 강도를 달리함

## Ⅴ. 선형·삼차함수·QUIC 복구의 비교

| 구분 | TCP Reno/NewReno | TCP CUBIC | QUIC recovery |
|---|---|---|---|
| **증가 기준** | 선형 AIMD | 시간 기반 cubic window 함수 | RFC 9002 기본은 NewReno 유사, 다른 알고리즘 선택 가능 |
| **강점** | 단순·보수적·기준 알고리즘 | 고속·장거리 경로의 확장성과 안정성 | packet number·ACK delay를 활용한 손실 탐지 |
| **손실 복구** | duplicate ACK·RTO | TCP 복구 체계 + CUBIC 창 제어 | packet/time threshold·PTO |
| **RTT 영향** | RTT가 큰 흐름의 증가가 느림 | Reno 대비 RTT 공정성 개선 지향 | path별 controller·암호화 계층별 loss space |
| **적용 포인트** | 기준 동작 이해 | 현재 널리 배포된 표준 TCP CC | 사용자 공간 transport·HTTP/3 |

#### 한줄 요약

- CUBIC은 cwnd 증가 함수를 바꾸고, QUIC은 packet number와 ACK 정보를 활용해 손실 탐지·복구 구조도 개선함

## Ⅵ. bufferbloat·무선 손실·관측 왜곡에 대한 실무 대책

| 문제 | 원인 | 대책 | 검증 효과 |
|---|---|---|---|
| **높은 처리량·긴 지연** | 과대한 queue가 손실을 늦추며 RTT 증가 | AQM·ECN, queue delay 감시 | throughput과 p95/p99 RTT 균형 |
| **무선 손실을 혼잡으로 오판** | channel error와 queue loss가 동일한 loss 신호 | link-layer 복구·ECN·다중 지표 분석 | 불필요한 cwnd 감소 완화 |
| **고 BDP 활용 저하** | Reno의 느린 선형 회복 | CUBIC 등 경로 특성에 맞는 알고리즘 검증 | 대역폭 활용과 공정성 개선 |
| **다수 짧은 흐름 불리** | slow start 중 전송 종료·incast | pacing·AQM·서비스별 queue 정책 | tail latency와 재전송 감소 |
| **단말·OS별 편차** | CC 알고리즘·kernel·middlebox 차이 | 접속별 RTT·loss·retransmit·CC 상태 수집 | 원인별 성능 분류 |

#### 한줄 요약

- 혼잡제어 운영은 throughput만 보지 않고 queue delay·loss·retransmit·fairness를 함께 관찰해야 함

## Ⅶ. End-to-End 지표로 제어루프를 검증하는 결론

- **[혼잡 신호와 사용자 체감 연결]**: sender의 cwnd가 커도 병목 queue와 application stall이 존재할 수 있으므로 transport telemetry와 서비스 지연을 함께 분석
- 나라면: 경로·접속 유형별로 `RTT 분포, loss/ECN, retransmission, cwnd, delivery rate`를 기준선화하고, AQM·CC 알고리즘 변경을 canary 흐름에 적용한 뒤 공정성과 tail latency가 함께 개선될 때 확대

#### 한줄 요약

- 혼잡제어의 성공은 링크를 가득 채우는 것이 아니라 공유 경로에서 안정적 처리량과 낮은 tail latency를 지속 유지하는 것임

## 1교시 10점 답안 발췌

### 1. 정의와 구조

- TCP 혼잡제어는 ACK·loss·ECN·RTT 피드백으로 cwnd를 조절하여 in-flight data를 제한하는 송신측 폐루프 제어

```text
ACK → cwnd 증가 → 전송 → queue 혼잡 → loss/ECN → cwnd 감소
```

### 2. 핵심 단계

| 단계 | 동작 |
|---|---|
| Slow Start | 경로 용량 빠른 탐색 |
| Congestion Avoidance | 완만한 증가로 안정 추종 |
| Fast Retransmit/Recovery | timer 전 손실 복구와 창 감소 |

### 3. 차별화 제언

- 흐름제어는 receiver, 혼잡제어는 network 보호
- throughput과 함께 queue delay·p99 RTT·loss/ECN·공정성을 검증하고 AQM·pacing·CUBIC을 경로별 적용

## 출제 이력과 검증 출처

- 제137회: KPC 키워드 대응 이력만 확인됨. 공식 문제지 원문과 대조되지 않아 문항 문구·교시·번호를 확정하지 않음
- 제130회: KPC 컴시응 대응 이력
- [RFC 5681, TCP Congestion Control](https://www.rfc-editor.org/info/rfc5681/)
- [RFC 9438, CUBIC for Fast and Long-Distance Networks](https://www.rfc-editor.org/info/rfc9438/)
- [RFC 9002, QUIC Loss Detection and Congestion Control](https://www.rfc-editor.org/rfc/rfc9002.html)

## 연결 토픽

- [슬라이딩 윈도우](./018_sliding_window/) · [WFQ](./008_wfq/) · [QoS](./032_qos/) · [SCTP](./034_sctp/)
