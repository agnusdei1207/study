---
sidebar:
  order: 7
  label: "007. TCP 혼잡제어"
  badge:
    text: "기초"
    variant: note
title: "TCP 혼잡제어(TCP Congestion Control)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 7
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
  question_no: "007"
---

## 지식 로드맵 내 현재 위치

지식 위치: 네트워크 → 전송 계층 → **TCP 혼잡제어**

## 30초 인출

- 본질: **TCP 혼잡제어** : 송신자가 경로의 혼잡 신호에 맞춰 미확인 데이터 양을 조절하는 피드백 제어
- 메커니즘: **cwnd** 증가로 경로 용량 탐색 → 손실·혼잡 표시 시 감소·복구 → 이후 다시 탐색
- 통찰: 단말의 흐름 제어(Flow Control)와 달리 네트워크 망 내부의 버퍼 오버플로와 전송 정체를 방지하기 위해 손실 기반(Loss-based) 알고리즘에서 대역폭·지연 적(BDP) 모델링 기반(BBR)으로 진화하여 처리율을 극대화하는 것이 핵심임.

<details>
<summary>핵심 용어</summary>

- **TCP(Transmission Control Protocol)** : 순서·확인 응답·재전송을 제공하는 연결형 전송 프로토콜
- **혼잡 윈도(cwnd, Congestion Window)** : 송신자가 경로 혼잡을 고려해 허용하는 미확인 데이터의 상한
- **수신 윈도(rwnd, Receive Window)** : 수신자가 버퍼 용량을 근거로 광고하는 수용 한도
- **느린 시작(Slow Start)** : 초기 경로 용량을 탐색하며 혼잡 윈도를 빠르게 늘리는 단계
- **혼잡 회피(Congestion Avoidance)** : 경로를 더 조심스럽게 탐색하는 단계
- **빠른 재전송(Fast Retransmit)** : 중복 ACK 등으로 손실을 추정해 타이머 전에 재전송하는 기법
- **빠른 회복(Fast Recovery)** : 빠른 재전송 뒤 혼잡 윈도를 조정하며 데이터 전송을 재개하는 기법
- **ECN(Explicit Congestion Notification)** : 패킷 손실 전에 네트워크 혼잡을 표시할 수 있는 기법
- **CUBIC** : 혼잡 윈도 증가에 3차 함수를 사용하는 TCP 혼잡제어 알고리즘

</details>

---

## 2~4교시 예상문제 (25점)

> TCP 혼잡 제어(TCP Congestion Control)의 필요성, 전통적 4단계 메커니즘(Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery) 및 현대 BBR(Bottleneck Bandwidth and RTT) 알고리즘을 비교 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. TCP 혼잡 제어(TCP Congestion Control)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 송신측이 네트워크 경로 상의 혼잡 상태를 능동적으로 감지하여 데이터 송신률(혼잡 윈도우 크기, cwnd)을 적응적으로 조절하는 전송 계층 제어 기법 |
| 목적 | 중간 라우터의 버퍼 오버플로로 인한 대량 패킷 폐기 방지, 네트워크 자원의 공평한(Fairness) 공유 및 전체 처리율 극대화 |

## Ⅱ. TCP 혼잡 제어(TCP Congestion Control)의 특징

| 특징 | 상세 내용 |
|---|---|
| 종단 간 추론(End-to-End)| 라우터의 명시적 피드백 없이 수신측 ACK 도착 타이밍과 패킷 손실 여부만으로 혼잡 판단 |
| 승법적 감소 가법적 증가| 패킷 정상 수신 시 cwnd를 선형 증가(AI)시키고 혼잡 발생 시 절반으로 급감(MD)시켜 수렴 보장 |
| 두 개의 윈도우 제한| 송신 가능 데이터 크기는 `min(cwnd, rwnd)`로 결정되어 흐름 제어와 혼잡 제어 동시 만족 |
| 능동적 혼잡 회피 진화| 단순 패킷 Drop 감지 방식(Reno/Cubic)에서 RTT 변화 및 보틀넥 모델 기반(Vegas/BBR)으로 발전 |

## Ⅲ. TCP 혼잡 제어(TCP Congestion Control)의 체계·프로세스

**전통적 TCP 혼잡 제어 4단계 동작 메커니즘**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ 전통적 TCP 혼잡 제어 곡선 ]                  │
│                                                                        │
│ cwnd (윈도우 크기)                                                     │
│   ▲                                                                    │
│   │                 (3 Dup ACK: 빠른 재전송/회복)                      │
│   │                      /\                                            │
│   │          혼잡 회피  /  \ 혼잡 회피                                 │
│   │         ┌──────────┘    \──────────►                               │
│   │        /                / (새로운 ssthresh = cwnd / 2)             │
│   │       / (ssthresh)                                                 │
│   │      /                                                             │
│   │     /  Slow Start (지수적 증가: RTT당 2배)                         │
│   │    /                                                               │
│   └───┴──────────────────────────────────────────────────────► 시간(t) │
└────────────────────────────────────────────────────────────────────────┘
```

| 단계 | 동작 조건 | cwnd 크기 변화 공식 | 핵심 동작 설명 |
|---|---|---|---|
| **Slow Start (느린 시작)** | cwnd < ssthresh | `cwnd = cwnd + 1 MSS` (ACK 수신마다) | 초기 기동 시 윈도우 크기를 RTT마다 2배씩 지수 함수적으로 급격히 증가 |
| **Congestion Avoidance (혼잡 회피)** | cwnd >= ssthresh | `cwnd = cwnd + 1/cwnd` (RTT당 1 MSS 증가) | 패킷 손실 임계치 도달 후 보수적으로 선형 증가(Additive Increase) 수행 |
| **Fast Retransmit (빠른 재전송)** | 3 Duplicate ACK 수신 | 타이머 만료 전 즉시 패킷 재전송 | 타임아웃까지 대기하지 않고 손실 패킷을 즉시 복구 |
| **Fast Recovery (빠른 회복)** | 빠른 재전송 이후 | `ssthresh = cwnd/2, cwnd = ssthresh + 3` | cwnd를 1로 떨어뜨리지 않고 혼잡 회피 단계부터 다시 선형 증가 시작 |

## Ⅳ. TCP 혼잡 제어(TCP Congestion Control)의 종류·비교

| 비교 항목 | 손실 기반 혼잡 제어 (TCP CUBIC) | 모델 기반 혼잡 제어 (BBR) |
|---|---|---|
| **개발 주체** | Linux 표준 기본 알고리즘 (Sangtae Ha et al.) | Google (Neal Cardwell et al.) |
| **혼잡 감지 기준** | 라우터 버퍼 오버플로로 인한 **패킷 손실(Packet Loss)**| 채널 대역폭(Max Bandwidth) 및 **최소 RTT(Min RTT)** |
| **버퍼블로트 영향** | 버퍼를 가득 채운 후 드롭하므로 지연 시간 폭증 | 보틀넥 큐를 채우지 않아 버퍼블로트 원천 해소 |
| **고대역-고지연망 (LFN)**| cwnd 회복에 오랜 시간 소요 (성능 저하) | 채널 대역폭을 즉각 포화시켜 초고속 전송 보장 |
| **기존 트래픽 공평성**| 전통적 Reno 계열과 친화적 공존 | 손실 기반 트래픽 대역폭을 압도하는 경향 존재 |

## Ⅴ. TCP 혼잡 제어(TCP Congestion Control)의 한계와 방안

| 한계 | 방안 |
|---|---|
| 대용량 라우터 버퍼로 인해 패킷 손실 전 지연만 극심하게 증가하는 버퍼블로트(Bufferbloat) 발생 | 라우터 계층 CoDel, FQ-CoDel, RED 등 능동 큐 관리(AQM) 기술 병행 적용 |
| 무선 통신망에서 페이딩/핸드오버로 인한 랜덤 비트 손실을 네트워크 혼잡으로 오인하여 cwnd 급감 | 무선 구간 BBR 알고리즘 도입 및 L2 HARQ 결합으로 무선 손실 은폐 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
글로벌 멀티 클라우드 환경 및 대용량 CDN 서버 구축 시, Linux 커널의 기본 혼잡 제어 알고리즘을 `sysctl -w net.ipv4.tcp_congestion_control=bbr`로 전환하여 태평양 횡단 해저 케이블과 같은 긴 RTT 환경에서 대역폭 활용률을 최대 10배 개선.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ Google BBR (Bottleneck Bandwidth and RTT) 동작 상태 천이 ]          │
│                                                                        │
│   ┌───────────────┐     대역폭 포화 감지       ┌───────────────┐       │
│   │ [ STARTUP ]   ├──────────────────────────►│ [ DRAIN ]     │       │
│   │ 윈도우 급속확장│                           │ 버퍼 큐 비우기│       │
│   └───────────────┘                           └───────┬───────┘       │
│           ▲                                           │ 큐 비움 완료  │
│           │                                           ▼               │
│           │ 최소 RTT 유효기간 만료             ┌───────────────┐       │
│           └───────────────────────────────────┤ [ PROBE_BW ]  │◄──┐   │
│                                               │ 가용대역폭탐색│   │   │
│   ┌───────────────┐   10초마다 주기적 진입    └───────┬───────┘   │   │
│   │ [ PROBE_RTT ] │◄──────────────────────────────────┘           │   │
│   │ 윈도우를 4로  │                                               │   │
│   │ 줄여 Min RTT  ├───────────────────────────────────────────────┘   │
│   │ 정밀 실측     │ Min RTT 갱신 완료                                 │
│   └───────────────┘                                                   │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 세대 | 대표 프로토콜 | 핵심 메커니즘 | 주요 한계점 |
|---|---|---|---|
| **1세대 (손실 기반)** | Tahoe, Reno, NewReno | AIMD, 3-Dup ACK 기반 cwnd 반감 | 타임아웃 시 성능 급락, LFN 미지원 |
| **2세대 (수식 최적화)** | BIC-TCP, CUBIC | 3차 함수 기반 빠른 cwnd 회복 | 대용량 버퍼 환경에서 버퍼블로트 유발 |
| **3세대 (측정/모델 기반)**| Vegas, FAST, BBR v1/v2 | RTT 측정 및 대역폭-지연 곱(BDP) 모델링 | 경쟁 손실 기반 흐름과의 공평성 튜닝 요구 |

## 출제 이력과 검증 출처

- IETF RFC 5681: TCP Congestion Control
- IETF RFC 8312: CUBIC for Fast Long-Distance Networks
- ACM Queue: BBR: Congestion-Based Congestion Control (Google, 2016)

## 연결 토픽

- 상위 토픽: [017 OSI 7 계층](./017_osi_7_layer.md)
- 연관 토픽: [018 슬라이딩 윈도우](./018_sliding_window.md), [008 WFQ](./008_wfq.md)
