---
title: "랙스케일 AI 시스템 (GB200 NVL72·Vera Rubin NVL72)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 랙스케일 AI 시스템의 개요

- 개념 : 단일 서버 섀시(Chassis)의 물리적 한계를 넘어, **랙(Rack)** 전체를 하나의 거대한 단일 슈퍼컴퓨터 가속 노드로 통합 설계하여 수십~수백 개의 최신 GPU(Graphics Processing Unit)/NPU(Neural Processing Unit)와 CPU(Central Processing Unit), 스케일업 인터커넥트, 액체 냉각(Direct-to-Chip Liquid Cooling), 통합 전력 버스바를 단일 패키지로 구성한 차세대 AI(Artificial Intelligence) 인프라 아키텍처.
- 배경 및 필요성 : 수천억~수조 개 파라미터 기반 **거대언어모델(LLM, Large Language Model)** 및 멀티모달 AI의 사전학습과 초고속 추론 시, 기존 노드 간 InfiniBand/Ethernet 스케일아웃 네트워크의 대역폭 한계와 지연 시간 병목을 극복하기 위해 등장.
- 핵심 목적 : 랙 내부 전 노드 간 페타바이트급 양방향 통신 대역폭 확보, 단일 랙당 메가와트(MW)급 전력 밀도 수용, 액체 냉각을 통한 낮은 **PUE**(Power Usage Effectiveness)의 고효율 데이터센터 구현.

## Ⅱ. 랙스케일 AI 시스템(GB200 NVL72 기준) 핵심 아키텍처 및 동작 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 랙스케일 AI 시스템 (GB200 NVL72 아키텍처) ]                         │
│                                                                        │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 18개 컴퓨트 트레이 (Compute Tray)                              │   │
│   │  - 총 36개 Grace CPU + 72개 Blackwell GPU                     │   │
│   │  - 30TB 통합 고속 메모리 (LPDDR5X + HBM3E)                    │   │
│   │  - 다이렉트 액체 냉각(DLC) 콜드 플레이트 장착                  │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │ NVLink 구리선 백플레인 (5,000+ 케이블)│
│                                   ▼                                    │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ 9개 NVLink 스위치 트레이 (Switch Tray)                         │   │
│   │  - 72개 GPU 간 130 TB/s All-to-All 양방향 NVLink 5 패브릭      │   │
│   │  - GPU당 1.8 TB/s 단일 주소 공간(Single Memory Space) 풀링     │   │
│   └────────────────────────────────────────────────────────────────┘   │
│   │ 전력/냉각: 48V DC 버스바 (최대 120kW/Rack) + CDU 냉각수 순환   │   │
└────────────────────────────────────────────────────────────────────────┘
```

- **컴퓨트 및 스위치 트레이 분리 설계** : 컴퓨트 트레이와 초고속 스위치 트레이를 직교 분리 배치하고, 후면 패시브 구리선(Over-the-Surface Copper) 백플레인으로 직접 연결하여 광모듈 없이 신호 감쇠 극소화 및 전력 20kW 절감.
- **단일 GPU 가상화 풀링** : 72개 GPU가 하나의 논리적 GPU 메모리 풀처럼 동작하여 수조 파라미터 모델을 **텐서 병렬화(Tensor Parallelism)** 할 때 네트워크 오버헤드 없이 제로 레이턴시에 근접한 연산 수행.

## Ⅲ. 주요 랙스케일 AI 시스템 비교 분석 (GB200 NVL72 vs Vera Rubin NVL72)

| 비교 항목 | GB200 NVL72 (Blackwell 기반) | Vera Rubin NVL72 (Rubin 기반 차세대) | 기존 HGX H100 (8-GPU 노드 클러스터) |
| :--- | :--- | :--- | :--- |
| **GPU/가속기 구성** | 72 Blackwell GPUs (18 트레이) | 72 Rubin GPUs (Vera CPU 결합) | 8 Hopper GPUs per Node |
| **인터커넥트 패브릭** | NVLink 5 (GPU당 1.8 TB/s, 총 130 TB/s) | NVLink 6 (차세대 PAM4 광/전 인터커넥트) | NVLink 4 (GPU당 900 GB/s) |
| **메모리 기술** | HBM3E (최대 192GB per GPU) | HBM4 (2048-bit 베이스 다이 직접 적층) | HBM3 (80GB per GPU) |
| **AI 연산 성능** | 1.4 ExaFLOPS FP4 (추론 특화) | 3.5+ ExaFLOPS 추정 (극대화된 FP4/FP2) | 32 PFLOPS FP8 |
| **냉각 아키텍처** | 전면 다이렉트 수랭식(DLC, Liquid-to-Air/Water) | 고도화된 수랭 및 마이크로 채널 직접 냉각 | 공랭(Air Cooling) 또는 하이브리드 수랭 |
| **단일 랙 전력 소비** | 약 100 kW ~ 120 kW per Rack | 140 kW ~ 160 kW per Rack 예상 | 약 10 kW ~ 15 kW per Rack |

## Ⅳ. 랙스케일 AI 시스템의 주요 한계점 및 해결 방안

- 단일 랙 120kW 초고전력 밀도와 데이터센터 인프라 수용 한계 :
  - 한계점 : 기존 상용 데이터센터는 랙당 5~15kW 수준으로 설계되어 있어 120kW 초고밀도 랙 배치 시 수전 용량 초과 및 전력 공급선 소손 위험.
  - 해결 방안 : 48V DC 중앙 버스바 시스템 구축, 전력 분배 장치(PDU, Power Distribution Unit)의 고효율 직류 변환 적용 및 데이터센터 모듈러 전력 분할 배치.
- 냉각수 **누수(Leakage)** 리스크 및 CDU(Cooling Distribution Unit) 단일 장애점 :
  - 한계점 : 고가의 GPU 트레이 내 냉각수 누수 시 영구적 하드웨어 파손 발생 및 냉각 루프 순환 펌프 고장 시 즉각적 열폭주(Thermal Throttling) 발생.
  - 해결 방안 : 진공 흡입 방식 음압 냉각 시스템(Negative Pressure) 적용으로 누수 원천 방지, 2N 이중화 펌프 CDU 및 유전체 냉각수(Dielectric Fluid) 검토.
- **초고밀도 중량** (Rack당 1.3톤 이상)에 따른 건축 구조적 하중 초과 :
  - 한계점 : 기존 엑세스 플로어(이중 바닥)의 단위 면적당 하중 허용치를 초과하여 바닥 붕괴 위험 및 랙 운반 경로 제한.
  - 해결 방안 : 슬래브 직배치(Slab-on-Grade) 시공, 랙 무게 분산 프레임 설치 및 AI 전용 신축 데이터센터 하중 설계 기준(2,000kg/m² 이상) 상향.

## Ⅴ. 랙스케일 AI 도입을 위한 기술사적 제언

- 데이터센터 상면·전력·냉각 인프라의 전면 재설계 선행 : 랙스케일 AI 시스템은 단순한 서버 교체가 아닌 데이터센터 유틸리티의 전면 개조를 수반하므로, 장비 도입 전 변전 설비, 냉각탑, 액체-액체 CDU 배관망 및 하중 구조를 사전 진단하고 리트로핏(Retrofit) 로드맵을 수립해야 함.
- 초고밀도 팟 단위 **장애 격리(Fault Domain)** 아키텍처 수립 : 72개 GPU가 단일 NVLink 도메인으로 결속되어 있으므로 단일 스위치 트레이 장애가 전체 랙 연산 중단으로 확산되지 않도록 하이퍼바이저 없는 베어메탈 오케스트레이션 및 체크포인팅(Checkpointing) 저장 주기를 초단위로 단축할 것을 제언함.
