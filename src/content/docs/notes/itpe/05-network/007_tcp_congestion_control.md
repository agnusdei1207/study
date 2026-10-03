---
title: "TCP 혼잡제어(TCP Congestion Control)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. TCP 혼잡제어(TCP Congestion Control)의 개요

- 개념 : 네트워크 내부의 라우터/스위치 버퍼 오버플로우로 인한 패킷 손실과 지연 폭증을 방지하기 위해, 송신 측이 네트워크의 혼잡 상태를 감지하여 **전송 윈도우(CWND)** 크기를 동적으로 조절하는 **전송 계층(L4)** 종단 간 트래픽 제어 기술.
- 배경 및 필요성 : 1980년대 초 인터넷에서 패킷 손실로 인한 맹목적 재전송이 네트워크 전체를 마비시키는 '혼잡 붕괴(Congestion Collapse)' 현상이 발생하면서, 네트워크 자원의 공정한 공유와 안정적 수렴을 위한 알고리즘이 필수화됨.
- 핵심 목적 : 네트워크 가용 대역폭의 최대 활용, 다중 연결 간의 공평성(Fairness) 보장, 네트워크 패킷 낭비 및 **버퍼블로트(Bufferbloat)** 현상 방지.

## Ⅱ. TCP 혼잡제어(TCP Congestion Control)의 핵심 아키텍처 및 동작 메커니즘

전통적 TCP 혼잡제어는 슬로우 스타트, 혼잡 회피, 빠른 재전송, 빠른 복구의 4단계 유한 상태 머신으로 동작하며, 최근에는 손실 기반(Loss-based)에서 지연 기반(Delay-based) 및 모델 기반(BBR)으로 발전함.

```text
[ TCP 전통적 혼잡제어 상태 전이 및 윈도우 제어 메커니즘 ]

  CWND (혼잡 윈도우 크기)
    ▲
    │                      [3 Duplicate ACKs] -> Fast Retransmit
    │                           │
    │                      |\   │  Fast Recovery (CWND = ssthresh)
    │                     /  \  ▼  /-----------------
    │                    /    \   /  (AIMD: 1 RTT당 +1 MSS)
    │                   /      \_/
    │      Slow Start  /        ssthresh (새 임계치 = CWND / 2)
    │      (지수적 증가)
    │        /│
    │       / │ ssthresh (초기 혼잡 임계치 도달)
    │      /  │
    │     /   └--------> 혼잡 회피 (Congestion Avoidance: 선형 증가)
    │    /
    └───┴───────────────────────────────────────────────────► 시간(Time)

* 현대 알고리즘 패러다임:
  1. Loss-based: Reno, NewReno, CUBIC (패킷 손실 시 혼잡 판정)
  2. Model-based: Google BBR (BtlBw 대역폭과 RTprop 최소지연 동시 측정)
```

- **슬로우 스타트(Slow Start)** : 연결 초기 또는 타임아웃 발생 시 CWND를 1 MSS(최대 세그먼트 크기)부터 시작하여 매 RTT마다 윈도우를 2배씩 지수적으로 급격히 증가.
- **혼잡 회피(Congestion Avoidance)** : CWND가 임계치(ssthresh)에 도달하면 네트워크 과부하를 방지하기 위해 매 RTT마다 1 MSS씩 완만하게 선형 증가(Additive Increase).
- **빠른 재전송(Fast Retransmit)** : 타임아웃 만료 전이라도 동일한 3개의 중복 ACK(3 Duplicate ACKs)를 수신하면 패킷 손실로 간주하고 즉시 재전송.
- **빠른 복구(Fast Recovery)** : 3 Dup ACK 감지 시 CWND를 1로 떨어뜨리지 않고 절반으로 줄인 후 슬로우 스타트를 건너뛰고 혼잡 회피 단계로 즉시 복귀(Multiplicative Decrease).

## Ⅲ. TCP 혼잡제어(TCP Congestion Control)의 세부 구성 요소 및 비교 분석

| 비교 항목 | TCP Reno | TCP CUBIC (리눅스 기본) | Google BBR (BBRv2/v3) | DCTCP (데이터센터용) |
|---|---|---|---|---|
| 혼잡 감지 메트릭 | 패킷 손실 (3 Dup ACK) | 패킷 손실 (3 Dup ACK) | 최소 왕복시간(RTT) 및 최대 대역폭 | ECN (스위치 큐 조기 마킹) |
| 윈도우 증가 함수 | 선형 증가 (AIMD) | 3차 함수(Cubic Function) 곡선 | 전송률(Pacing Rate) 모델 제어 | ECN 비율에 비례한 감소 제어 |
| 초고속망 적응성 | BDP가 큰 LFN망에서 극도로 취약 | 초고속망에서 빠른 대역폭 수렴 | BDP 무관하게 최적 동작 | 초저지연 데이터센터 최적화 |
| 버퍼블로트 내성 | 취약 (버퍼 가득 채운 후 드롭) | 취약 (대용량 라우터 버퍼 점유) | 우수 (버퍼에 큐를 쌓지 않음) | 극히 우수 (초소형 큐 유지) |
| 주요 사용 환경 | 전통 레거시 시스템, 교육용 표준 | 대다수 리눅스/안드로이드 OS | 유튜브, 구글 클라우드, QUIC | 프라이빗 분산 클라우드 내부망 |

- CUBIC이 높은 **대역폭 지연 곱(BDP)** 환경에서 안정적인 3차 함수 수렴을 제공한다면, BBR은 버퍼블로트를 근본적으로 억제하여 현대 클라우드와 모바일 환경의 지연시간을 혁신함.

## Ⅳ. TCP 혼잡제어(TCP Congestion Control)의 주요 한계점 및 해결 방안

- 손실 기반 알고리즘의 버퍼블로트(Bufferbloat) 현상 :
  - 한계점 : 라우터의 대용량 버퍼가 가득 찰 때까지 계속 윈도우를 확장하여 패킷 손실은 없으나 RTT 지연시간이 수백 ms로 폭증.
  - 해결 방안 : 스위치 측 능동적 큐 관리(AQM: CoDel, FQ-CoDel, PIE) 도입 및 송신단 BBR 알고리즘 전환.
- 무선 채널의 비혼잡성 랜덤 손실(Random Loss) 오인 :
  - 한계점 : Wi-Fi/셀룰러 환경의 일시적 페이딩 손실을 혼잡으로 판단하여 CWND를 반토막 내어 처리량 급락.
  - 해결 방안 : 패킷 손실 유무 대신 물리 계층 전송률 모델을 추정하는 BBR 적용 및 L2 HARQ 결합.
- 초대형 BDP(Bandwidth-Delay Product) 망에서의 느린 복구 속도 :
  - 한계점 : 100Gbps 이상의 초고속 회선에서 손실 후 Reno식 AIMD 회복 시 원래 전송률 도달에 수 시간 소요.
  - 해결 방안 : CUBIC의 시간 기반 3차 함수 복구 적용 및 대용량 패킷 페이싱(Packet Pacing) 메커니즘 강제.

## Ⅴ. TCP 혼잡제어(TCP Congestion Control) 적용 및 발전을 위한 기술사적 제언

- 엔드포인트 및 CDN 인프라의 BBRv2/v3 알고리즘 도입 확대 : 비디오 스트리밍 및 클라우드 게이밍의 지연 민감 트래픽 품질 개선을 위해 리눅스 커널의 BBR 모듈 전면 배포 권장.
- 데이터센터 내부 초저지연 패브릭을 위한 DCTCP/RoCE v2 ECN 최적화 : AI 분산 학습 클러스터의 패킷 드롭 방지를 위해 스위치 ECN 임계치와 결합된 혼잡제어 파라미터 튜닝 필수.
- HTTP/3(QUIC) 기반 전송 계층 현대화 추진 : TCP 커널 종속성을 탈피하고 사용자 공간에서 연결별 혼잡제어 알고리즘을 유연하게 교체할 수 있는 차세대 웹 프로토콜 적극 채택.
