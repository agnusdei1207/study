---
title: "NOMA(Non-Orthogonal Multiple Access)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. NOMA(Non-Orthogonal Multiple Access)의 개요

- 개념 : 동일한 시간, 주파수, 공간 무선 자원 상에 서로 다른 사용자의 데이터를 **비직교(Non-Orthogonal)** 방식으로 **전력(Power)** 또는 **코드(Code)** 영역에서 중첩하여 다중 전송하는 차세대 **다중 접속** 기술.
- 배경 및 필요성 : 기존 4G/5G의 **직교 다중 접속(OMA, Orthogonal Multiple Access: OFDMA(Orthogonal Frequency-Division Multiple Access), TDMA(Time Division Multiple Access), CDMA(Code Division Multiple Access))** 방식은 자원 블록 간 간섭을 없애기 위해 직교성을 강제하여 주파수 효율이 샤논 한계(Shannon Capacity Limit)에 수렴하는 구조적 한계 봉착.
- 핵심 목적 : 주파수 대역폭 확대 없는 주파수 스펙트럼 효율의 획기적 개선, **초대규모 사물인터넷(mMTC, massive Machine Type Communications)** 기기의 과밀 동시 접속 수용 및 원거리 단말의 통신 공평성(Fairness) 보장.

## Ⅱ. NOMA의 핵심 아키텍처 및 동작 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ 전력 영역 NOMA 및 SIC 복조 메커니즘 ]              │
│                                                                        │
│   [ 송신단 (기지국: BS) ] : 중첩 코딩 (Superposition Coding)           │
│   - 단말 채널 상태 분석: User 1 (Near-Cell: 양호), User 2 (Far-Cell: 열악)│
│   - 전력 비대칭 할당: P_Far > P_Near (신호가 약한 먼 단말에 더 큰 전력)│
│   - 송신 신호 s = sqrt(P_Near)*x_Near + sqrt(P_Far)*x_Far 동시 방사    │
│                                                                        │
│   [ 수신단 (User 2: 원거리 단말) ]                                     │
│   - 수신 신호에서 P_Far 신호가 압도적이므로 User 1 신호를 단순 잡음 취급│
│   ──► 복잡한 간섭 제거 없이 자신의 신호 x_Far 즉시 복조 완료           │
│                                                                        │
│   [ 수신단 (User 1: 근거리 단말) ] : 연속 간섭 제거 (SIC) 수행         │
│   수신 복합 신호 ──► 1단계: 강한 User 2 신호(x_Far)를 먼저 복조       │
│                  ──► 2단계: 복조된 User 2 신호를 전체 수신 신호에서 감산│
│                  ──► 3단계: 간섭이 제거된 순수 자신의 신호(x_Near) 복조│
└────────────────────────────────────────────────────────────────────────┘
```

- **중첩 코딩 (Superposition Coding)** : 기지국 송신단에서 서로 다른 채널 이득(Channel Gain)을 가진 복수 단말의 데이터를 단일 주파수 블록에 전력 가중치를 달리하여 더해서 동시 송신.
- **전력 할당 원칙** : 채널 환경이 나쁜 셀 경계 단말(Far User)에는 높은 전력($P_2$)을 배분하고, 채널 환경이 우수한 셀 근접 단말(Near User)에는 낮은 전력($P_1$)을 배분.
- **연속 간섭 제거 (SIC: Successive Interference Cancellation)** : 근거리 단말은 수신된 혼합 신호에서 가장 강한 전력을 가진 타인의 신호를 먼저 복조하여 원래 수신 신호에서 감산(Substraction)하는 과정을 순차 반복하여 최종 자신의 신호를 무간섭 복원.

## Ⅲ. NOMA의 세부 유형 및 직교 다중 접속(OMA)과의 비교 분석

| 비교 항목 | OMA (OFDMA / 4G·5G) | NOMA (Power-Domain) | NOMA (Code-Domain: SCMA) |
|---|---|---|---|
| 자원 직교성 | 시간/주파수 완전 직교 | 비직교 (동일 주파수·시간 공유) | 비직교 (다차원 코드북 공유) |
| 다중화 영역 | 주파수 블록 (Subcarrier) | 전력 영역 (Power Domain) | 코드 영역 (Sparse Codebooks) |
| 수신단 복잡도 | 낮음 (단순 FFT 복조) | 높음 (SIC 하드웨어 및 연산 필수)| 매우 높음 (MPA 메시지 전달) |
| 주파수 효율 | 낮음 (직교성 유지 제약) | 매우 높음 (샤논 용량 한계 근접) | 매우 높음 (초고밀도 접속 특화) |
| 동시 접속 수 | 서브캐리어 수에 종속 제한 | 전력 레벨 다중화로 대폭 확장 | 희소 코드 다중화로 극대화 |
| 채널 피드백 | 기본적인 CQI 피드백 | 고정밀 CSI(Channel State Information, 채널 상태 정보) 필수| 정밀 채널 및 코드북 인덱스 |

- **SCMA (Sparse Code Multiple Access)** : 비트열을 다차원 희소 코드북으로 직접 매핑하여 여러 사용자가 동일 자원을 공유하며, 수신단은 MPA(Message Passing Algorithm)를 통해 비직교 신호 분리.

## Ⅳ. NOMA의 주요 한계점 및 해결 방안

- SIC 수신단의 오류 전파(Error Propagation) 및 하드웨어 복잡도 :
  - 한계점 : 1단계에서 타인 신호 복조에 오류가 발생할 경우 감산 오차가 누적되어 이후 모든 자신의 신호 복조가 연쇄 실패하며, 다중 단말 수용 시 SIC 칩 연산량 폭증.
  - 해결 방안 : 단일 자원당 NOMA 페어링 단말 수를 2~3개 이내로 제한(User Clustering), 강력한 저지연 채널 코딩(LDPC/Polar Code) 결합 및 신경망 기반 딥러닝 SIC 디코더 적용.
- 단말 간 채널 이득 차이 부족 시 NOMA 이득 소멸 :
  - 한계점 : 페어링된 두 단말의 채널 환경이 유사할 경우 전력 차이를 두기 어려워 OMA 대비 주파수 효율 개선 효과 미미.
  - 해결 방안 : 기지국 스케줄러가 전 구역 단말 중 채널 이득 차이가 극대화되는 '셀 중심 단말'과 '셀 경계 단말'을 지능적으로 매칭하는 동적 사용자 페어링 알고리즘 구축.

## Ⅴ. NOMA 적용 및 발전을 위한 기술사적 제언

- Massive MIMO(Multiple-Input Multiple-Output) 및 빔포밍과의 결합 (Beam-NOMA) : 공간 다중화(MIMO)로 분리된 개별 빔 내부에서 다시 NOMA 전력 다중화를 적용하여 단위 면적당 전송 용량을 물리적 한계치까지 확장.
- 6G 위성 통신(NTN, Non-Terrestrial Network) 및 초대규모 IoT(Internet of Things) 접속 적용 : 수많은 저전력 센서가 한정된 위성 주파수 대역에 산발적으로 패킷을 전송하는 그랜트 프리(Grant-Free) NOMA 환경 구축을 통해 스케줄링 오버헤드 원천 제거.
- RIS(지능형 반사 표면) 연계를 통한 인위적 채널 환경 제어 : RIS 메타물질을 조작하여 인위적으로 단말 간 채널 차이를 증폭시킴으로써 NOMA의 SIC 복조 성공률을 보장하는 스마트 무선 환경(SMRE) 선제 구현.
