---
sidebar:
  order: 61
  label: "061. 시계열 실시간 이상치 탐지"
  badge:
    text: "기초"
    variant: note
title: "시계열 실시간 이상치 탐지 (Time Series Real-time Anomaly Detection)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 61
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "061"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>시계열 실시간 이상치 탐지</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <!-- Dynamic Band Background -->
  <rect x="15" y="15" width="490" height="250" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="38" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">시계열 실시간 이상치 탐지: 동적 임계 밴드 & 2-Tier 파이프라인</text>

  <!-- Plot Area -->
  <rect x="35" y="55" width="450" height="135" rx="4" fill="#ffffff" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>

  <!-- Dynamic Band Shading -->
  <path d="M 45 110 Q 110 80, 180 100 T 320 90 T 400 70 T 475 80 L 475 145 Q 400 135, 320 150 T 180 160 T 110 140 T 45 150 Z" fill="#3b82f6" fill-opacity="0.1"/>

  <!-- Upper/Lower Threshold Lines -->
  <path d="M 45 110 Q 110 80, 180 100 T 320 90 T 400 70 T 475 80" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="325" y="68" font-size="9" fill="#ef4444">Upper Band (μ + 3σ)</text>

  <path d="M 45 150 Q 110 140, 180 160 T 320 150 T 400 135 T 475 145" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="325" y="162" font-size="9" fill="#ef4444">Lower Band (μ - 3σ)</text>

  <!-- Center Trend (EWMA) -->
  <path d="M 45 130 Q 110 110, 180 130 T 320 120 T 400 102 T 475 112" fill="none" stroke="#2563eb" stroke-width="1.5"/>

  <!-- Data Stream Curve with Anomaly Spike -->
  <path d="M 45 130 L 80 125 L 115 112 L 150 138 L 180 128 L 220 118 L 250 125 L 280 62 L 310 122 L 350 118 L 390 100 L 430 108 L 475 115" fill="none" stroke="#0f172a" stroke-width="2"/>

  <!-- Anomaly Alert Marker -->
  <circle cx="280" cy="62" r="5" fill="#dc2626"/>
  <circle cx="280" cy="62" r="9" fill="none" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="2,2"/>
  <rect x="250" y="44" width="76" height="16" rx="3" fill="#dc2626"/>
  <text x="288" y="55" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">★ Outlier (Alert)</text>

  <!-- Bottom Pipeline Flow -->
  <g transform="translate(30, 205)">
    <rect x="5" y="5" width="95" height="42" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="52" y="22" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 스트림 유입</text>
    <text x="52" y="36" font-size="8.5" fill="#475569" text-anchor="middle">Kafka / IoT 센서</text>

    <path d="M 102 26 L 118 26" stroke="#64748b" stroke-width="1.5" marker-end="url(#arr-anom)"/>

    <rect x="120" y="5" width="105" height="42" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="172" y="22" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">2. 슬라이딩 윈도우</text>
    <text x="172" y="36" font-size="8.5" fill="#475569" text-anchor="middle">Flink RocksDB</text>

    <path d="M 227 26 L 243 26" stroke="#64748b" stroke-width="1.5"/>

    <rect x="245" y="5" width="105" height="42" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="297" y="22" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 2-Tier 추론</text>
    <text x="297" y="36" font-size="8.5" fill="#475569" text-anchor="middle">EWMA + AutoEnc</text>

    <path d="M 352 26 L 368 26" stroke="#64748b" stroke-width="1.5"/>

    <rect x="370" y="5" width="90" height="42" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="415" y="22" font-size="10" font-weight="bold" fill="#991b1b" text-anchor="middle">4. 선제 격리</text>
    <text x="415" y="36" font-size="8.5" fill="#475569" text-anchor="middle">FDS 차단 / Pager</text>
  </g>
</svg>
</div>

- 본질: **지속적으로 유입되는 고속 스트리밍 데이터에서 시간적 순서와 자기상관성을 반영하여, 정상 분포 패턴을 벗어나는 돌발 스파이크나 시퀀스 왜곡을 슬라이딩 윈도우와 머신러닝 모델을 통해 수 밀리초(ms) 단위의 초저지연으로 탐지·격리하는 선제적 관측 체계**
- 암기: `유-창-점-역` (스트림 유입, 슬라이딩 창, 이상 점수 산출, 역치 판정) / `통-기-심` (통계적 EWMA/3-Sigma, 머신러닝 Isolation Forest, 딥러닝 AutoEncoder)
- 판단축:
  - **포인트 이상치(Point Anomaly)**: 특정 한 시점의 단발성 급증·급감 (예: CPU 100% 스파이크)
  - **컨텍스트 이상치(Contextual Anomaly)**: 값 자체는 정상 범위이나 특정 시간대 맥락상 비정상 (예: 새벽 3시 대규모 송금)
  - **집단 이상치(Collective Anomaly)**: 개별 포인트는 정상이지만 연속된 시퀀스 조합이 비정상 패턴을 형성 (예: 평탄화 고원 현상)
- 주의: 고정 정적 임계값(Static Threshold)은 출퇴근 시간대 트래픽 증가나 계절적 변동을 이상치로 오판하여 극심한 알람 피로(Alert Fatigue)를 유발하므로, 최근 윈도우의 평균과 분산을 실시간 추종하는 **동적 임계 밴드(Dynamic Band)** 적용이 필수적임

## Ⅰ. 사후 배치 분석을 극복하는 시계열 실시간 이상치 탐지 개요

#### 한줄 요약: 데이터 발생 즉시 스트리밍 처리하여 보안 침해, 설비 고장, 금융 사기 피해를 골든타임 내에 선제 차단하는 저지연 탐지 기술

- **등장 배경**:
  - 기존 일일/시간 단위 배치(Batch) 분석은 이미 장애나 사기 거래가 발생한 후 수 시간 뒤에야 결과를 인지하는 구조적 한계(사후 약방문)를 노출함
  - 초 단위로 변하는 금융 트랜잭션과 초당 수만 건의 IoT 센서 신호 속에서 피해를 방지하려면 **데이터 인입 즉시 수십 ms 이내에 이상을 판정**해야 함
- **시계열 이상치 탐지의 정의**:
  - 시간에 따라 순차적으로 기록된 데이터 스트림에서, 정상적인 시계열의 추세(Trend), 계절성(Seasonality), 자기상관 구조와 통계적·기능적으로 부합하지 않는 비정상적인 관측치나 시퀀스를 탐지하는 기술

## Ⅱ. 시계열 데이터 이상치의 3대 유형 분류

#### 한줄 요약: 단일 시점의 스파이크(포인트), 시간적 맥락과의 불일치(컨텍스트), 비정상 시퀀스 패턴(집단)으로 대별

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 140" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="120" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">시계열 이상치의 3대 핵심 유형 분류</text>

  <!-- 3 Boxes -->
  <g transform="translate(25, 45)">
    <!-- Box 1 -->
    <rect x="0" y="0" width="150" height="70" rx="5" fill="#ffffff" stroke="#ef4444" stroke-width="1.2"/>
    <text x="75" y="20" font-size="10.5" font-weight="bold" fill="#b91c1c" text-anchor="middle">1. 포인트 이상치</text>
    <text x="75" y="38" font-size="9" fill="#334155" text-anchor="middle">단일 시점 극단적 스파이크</text>
    <text x="75" y="54" font-size="8" fill="#64748b" text-anchor="middle">CPU 100%, 0V 전압 강하</text>

    <!-- Box 2 -->
    <rect x="160" y="0" width="150" height="70" rx="5" fill="#ffffff" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="235" y="20" font-size="10.5" font-weight="bold" fill="#b45309" text-anchor="middle">2. 컨텍스트 이상치</text>
    <text x="235" y="38" font-size="9" fill="#334155" text-anchor="middle">상황/시간 맥락상 비정상</text>
    <text x="235" y="54" font-size="8" fill="#64748b" text-anchor="middle">새벽 3시 대규모 이체 급증</text>

    <!-- Box 3 -->
    <rect x="320" y="0" width="150" height="70" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="395" y="20" font-size="10.5" font-weight="bold" fill="#1d4ed8" text-anchor="middle">3. 집단 이상치</text>
    <text x="395" y="38" font-size="9" fill="#334155" text-anchor="middle">연속 시퀀스 조합 결함</text>
    <text x="395" y="54" font-size="8" fill="#64748b" text-anchor="middle">센서 고착(Freezing), 심박 지연</text>
  </g>
</svg>
</div>

| 이상치 유형 | 특징 및 판정 기준 | 전형적 사례 | 탐지 난이도 |
|:---|:---|:---|:---:|
| **포인트 이상치 (Point)** | 데이터 전체 분포의 상/하한 임계 범위를 단일 시점에 크게 벗어남 | 정전으로 인한 센서 전압 0V 추락, 초당 로그인 시도 10만 건 폭증 | 낮음 (경량 통계로 즉시 검출) |
| **컨텍스트 이상치 (Contextual)** | 배경 문맥(Context: 요일, 시간대, 온도 등)을 고려해야만 이상 여부가 판단됨 | 평일 낮 100건 접속은 정상이지만, 주말 새벽 3시에 100건 접속은 해킹 의심 | 중간 (시간 특성 파생 변수 필요) |
| **집단 이상치 (Collective)** | 하나하나의 측정치는 정상 범위 내에 있으나, 연속된 시간 순서의 조합이 비정상 | 심전도(ECG) 파형에서 특정 구간의 심박 패턴 지연, 센서 고착(Freezing) | 높음 (시퀀스 딥러닝 모형 요구) |

## Ⅲ. 실시간 이상치 탐지 3대 알고리즘 계열 심층 분석

#### 한줄 요약: 초경량 통계 기법(EWMA, 3-Sigma), 비지도 트리 머신러닝(iForest), 심층 시퀀스 모델(AutoEncoder)의 단계별 체계

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 130" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="110" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">실시간 이상치 탐지 알고리즘 스펙트럼 (지연시간 vs 표현력)</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="150" height="65" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/>
    <text x="75" y="18" font-size="10" font-weight="bold" fill="#15803d" text-anchor="middle">[통계적 기법]</text>
    <text x="75" y="34" font-size="8.5" fill="#334155" text-anchor="middle">EWMA, 3-Sigma, CUSUM</text>
    <text x="75" y="50" font-size="8" fill="#166534" text-anchor="middle">초저지연 (&le; 1ms)</text>

    <path d="M 152 32 L 168 32" stroke="#64748b" stroke-width="1.5"/>

    <rect x="170" y="0" width="150" height="65" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="245" y="18" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">[머신러닝 기법]</text>
    <text x="245" y="34" font-size="8.5" fill="#334155" text-anchor="middle">Isolation Forest, RRCF</text>
    <text x="245" y="50" font-size="8" fill="#1e3a8a" text-anchor="middle">다변량 비선형 (5~50ms)</text>

    <path d="M 322 32 L 338 32" stroke="#64748b" stroke-width="1.5"/>

    <rect x="340" y="0" width="140" height="65" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.2"/>
    <text x="410" y="18" font-size="10" font-weight="bold" fill="#6b21a8" text-anchor="middle">[딥러닝 기법]</text>
    <text x="410" y="34" font-size="8.5" fill="#334155" text-anchor="middle">LSTM-AutoEncoder, TranAD</text>
    <text x="410" y="50" font-size="8" fill="#581c87" text-anchor="middle">시퀀스 패턴 (50~300ms)</text>
  </g>
</svg>
</div>

### 1. 통계적 기법 (Statistical Methods)
- **EWMA (지수 이동평균 기반 관리도)**:
  - 과거 관측치에 지수적으로 감소하는 가중치를 부여하여 현재 시점의 국소적 기대값($\hat{\mu}_t$)을 실시간 갱신:
    $$\hat{\mu}_t = \alpha Y_t + (1 - \alpha) \hat{\mu}_{t-1} \quad (0 < \alpha \le 1)$$
  - 이동 표준편차($\hat{\sigma}_t$)를 결합하여 동적 관리 한계선($\hat{\mu}_t \pm L \cdot \hat{\sigma}_t$)을 설정하고 이탈 시 이상 판정
- **CUSUM (Cumulative Sum)**:
  - 시계열의 평균값이 기준값에서 미세하게 지속적으로 이탈하는 '평균의 미세 편차'를 누적합으로 증폭시켜 신속히 검출

### 2. 머신러닝 기법 (Machine Learning Methods)
- **Isolation Forest (격리 포레스트)**:
  - "이상치는 정상 데이터에 비해 데이터 수가 적고 속성 공간에서 고립되어 있다"는 원리 활용
  - 무작위 속성과 분할점을 선택하여 이진 트리를 구성할 때, 이상치는 루트 노드에 가까운 얕은 깊이(Path Length)에서 조기 고립됨
  - **RRCF (Robust Random Cut Forest)**: 스트리밍 환경에 맞추어 트리를 동적으로 추가·삭제할 수 있는 실시간 전용 확장 알고리즘
- **One-Class SVM**:
  - 정상 데이터만을 감싸는 최소 초구(Hypersphere)를 학습하고, 구 바깥으로 유입되는 데이터를 이상치로 분류

### 3. 딥러닝 기법 (Deep Learning Methods)
- **LSTM / GRU AutoEncoder**:
  - 인코더가 시계열 시퀀스를 잠재 표현(Latent Vector)으로 압축하고, 디코더가 이를 원래 시계열로 복원
  - 정상 데이터로만 학습된 모델은 이상치가 들어왔을 때 제대로 복원하지 못하므로, **재구성 오차(Reconstruction Error, $\|Y_t - \hat{Y}_t\|^2$)**가 급증함
- **Transformer 기반 이상 탐지 (TranAD)**:
  - Self-Attention 메커니즘을 통해 장기 의존성(Long-term dependency)과 변수 간 다변량 상관관계를 동시에 파악

## Ⅳ. 탐지 알고리즘 계열별 상세 비교

#### 한줄 요약: 연산 지연 시간, 자원 소모량, 다변량 지원 여부, 해석 용이성 관점의 트레이드오프

| 비교 항목 | 통계적 기법 (EWMA, 3-Sigma) | 머신러닝 기법 (Isolation Forest) | 딥러닝 기법 (LSTM AutoEncoder) |
|:---|:---|:---|:---|
| **연산 레이턴시** | **극도로 낮음 ($\le 1\text{ms}$)** | **낮음 ($5 \sim 50\text{ms}$)** | 보통 ($50 \sim 300\text{ms}$, GPU 권장) |
| **학습 데이터 요구** | 사전 학습 불필요 (온라인 즉시 계산) | 소량의 비지도 데이터로 고속 학습 | 대량의 정상 시계열 학습 데이터 필수 |
| **다변량(Multivariate)**| 단변량 중심 (다변량 시 공분산 복잡) | 우수 (수십 개 피처 동시 처리) | **최상** (수백 개 센서 간 상호작용 포착) |
| **시퀀스 패턴 탐지** | 단발성 포인트 이상치에 특화 | 정적 다차원 분포 중심 (시차 반영 한계) | **최상** (복잡한 시퀀스 집단 이상치 검출) |
| **해석 가능성(XAI)** | **명확** (통계 공식 기반 사유 제시) | 보통 (분기 속성 기여도 산출 가능) | 낮음 (블랙박스 신경망) |
| **콘셉트 드리프트** | 파라미터($\alpha$)로 빠른 자동 적응 | 주기적 트리 재생성(RRCF) 필요 | 모델 재학습(Fine-tuning) 파이프라인 필수 |

## Ⅴ. 스트리밍 이상치 탐지 파이프라인 엔드투엔드 아키텍처

#### 한줄 요약: Kafka 인입, Flink 슬라이딩 윈도우 집계, 2단계 계층형 모델 추론, 실시간 알림 엔진의 유기적 결합

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 220" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="200" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">실시간 스트리밍 이상 탐지 엔드투엔드 아키텍처</text>

  <!-- Left: Ingestion -->
  <rect x="30" y="55" width="100" height="135" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
  <text x="80" y="75" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">스트리밍 인입</text>
  <text x="80" y="98" font-size="8.5" fill="#334155" text-anchor="middle">IoT / FDS 로그</text>
  <rect x="40" y="115" width="80" height="26" rx="3" fill="#eff6ff" stroke="#93c5fd"/>
  <text x="80" y="132" font-size="9" font-weight="bold" fill="#2563eb" text-anchor="middle">Kafka / Kinesis</text>

  <!-- Arrow -->
  <path d="M 132 122 L 158 122" stroke="#64748b" stroke-width="1.5"/>

  <!-- Middle: Stream Engine -->
  <rect x="160" y="55" width="115" height="135" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
  <text x="217" y="75" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">스트림 처리 엔진</text>
  <text x="217" y="98" font-size="8.5" fill="#334155" text-anchor="middle">Apache Flink</text>
  <text x="217" y="125" font-size="8" fill="#475569" text-anchor="middle">Sliding Window</text>
  <text x="217" y="145" font-size="8" fill="#475569" text-anchor="middle">RocksDB State</text>
  <text x="217" y="165" font-size="8" fill="#475569" text-anchor="middle">Watermark 정렬</text>

  <!-- Split Arrows -->
  <path d="M 277 105 L 303 85" stroke="#16a34a" stroke-width="1.5"/>
  <path d="M 277 140 L 303 160" stroke="#9333ea" stroke-width="1.5"/>

  <!-- Right: 2-Tier Reasoning -->
  <rect x="305" y="55" width="180" height="60" rx="4" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.2"/>
  <text x="395" y="74" font-size="9.5" font-weight="bold" fill="#15803d" text-anchor="middle">Tier 1: 경량 통계 필터 (99% 통과)</text>
  <text x="395" y="92" font-size="8.5" fill="#334155" text-anchor="middle">EWMA / Z-Score (&lt; 1ms 판정)</text>

  <rect x="305" y="130" width="180" height="60" rx="4" fill="#faf5ff" stroke="#9333ea" stroke-width="1.2"/>
  <text x="395" y="149" font-size="9.5" font-weight="bold" fill="#6b21a8" text-anchor="middle">Tier 2: 정밀 심층 신경망 (의심 1%)</text>
  <text x="395" y="167" font-size="8.5" fill="#334155" text-anchor="middle">LSTM AutoEncoder (GPU 가속)</text>
</svg>
</div>

- **슬라이딩 윈도우(Sliding Window) 상태 관리**:
  - Apache Flink의 RocksDB 상태 백엔드를 활용하여 각 시계열 키(센서 ID, 계좌 번호)별로 최근 $N$개의 윈도우 상태를 메모리에 유지
  - 늦게 도착한 데이터(Late-arriving data)는 워터마크(Watermark) 처리를 통해 정렬 후 탐지 엔진으로 유입

## Ⅵ. 산업별 실무 적용 사례 및 장애 방지 전략

#### 한줄 요약: 스마트 제조, 금융 사기, 클라우드 APM에서의 실전 적용과 알람 피로(Alert Fatigue) 극복 방안

### 1. 산업 도메인별 적용 사례
- **스마트 팩토리 반도체/사출 공정**:
  - 설비 모터 진동 및 온도 센서 데이터를 초당 1,000회 수집
  - RRCF(Robust Random Cut Forest)를 통해 베어링 마모 징후를 설비 고장 수일 전에 감지(예지보전, Predictive Maintenance)
- **금융 결제 이상거래 탐지 시스템 (FDS)**:
  - 고객의 과거 거래 지역, 송금 금액, 디바이스 핑거프린트의 시계열 패턴을 추적
  - 평소 행동과 다른 컨텍스트 이상치 발생 시 결제를 즉시 보류(Pending)하고 추가 본인인증 요구
- **대규모 클라우드 인프라 (AIOps)**:
  - 수천 대 마이크로서비스 인스턴스의 CPU, 메모리, 레이턴시 메트릭을 EWMA 기반 동적 밴드로 감시하여 오토스케일링 선제 트리거

### 2. 알람 피로(Alert Fatigue) 및 오탐 방지 엔지니어링 전략
- **지속성 검증 (Persistence Check)**:
  - 단 1회의 임계치 초과로 즉시 경보를 울리지 않고, 최근 3~5회 연속 윈도우에서 임계값을 초과했을 때만 최종 Alert 발송
- **동적 가변 윈도우 적용**:
  - 평시에는 윈도우 크기를 넓혀 연산 부하를 줄이고, 이상 징후 감지 시 윈도우를 세분화하여 정밀 진단 모드로 동적 전환

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 시계열 이상치 탐지는 "단일 알고리즘의 정확도" 문제가 아니라 **"지연시간(Latency)과 연산 비용(Cost) 사이의 계층형 파이프라인 설계"** 문제다. 모든 스트림을 딥러닝(AutoEncoder/TranAD)에 쏟아부으면 백프레셔로 파이프라인이 즉시 마비된다. Flink 레벨에서 가벼운 EWMA 통계 필터로 99%의 정상 데이터를 1ms 내에 걸러내고, 남은 1%의 의심 구간만 GPU 워커로 넘기는 2-Tier 구조가 엔터프라이즈의 표준 해법이다.

> **[나라면 이렇게 쓴다]**
> 답안 3단에 "정적 임계값의 한계(알람 피로) vs EWMA 기반 동적 임계 밴드($\mu_t \pm 3\sigma_t$)"를 그래프와 수식으로 대비하고, 4단 기술사 제언에 "Tier-1 통계 필터(Edge) + Tier-2 딥러닝 추론(Cloud/GPU)"의 2계층 아키텍처와 Persistence Check(연속 $N$회 초과 시 경보 발송) 전략을 구조도로 명문화하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 단순 정적 임계값(Static Threshold) 기반 알람은 계절성 및 자연 증가 트래픽을 이상으로 오판하여 운영팀의 심각한 알람 피로(Alert Fatigue) 유발
- **대응 (개선 방안)**: EWMA 기반 동적 밴드와 지속성 검증(Persistence Check)을 도입하고, 스트림 처리기(Tier 1)와 GPU AI 엔진(Tier 2)의 2단계 계층형 필터링 파이프라인 구축
- **검증 (검증 기준)**: 오탐율(False Positive Rate) 0.1% 이하 유지, 엔드투엔드 탐지 레이턴시 50ms 이내 보장, 백프레셔 발생 여부 지속 모니터링
- **효과 (실행 효과)**: 고비용 인프라 자원 소모 80% 절감, 골든타임 내 이상 징후 조기 격리로 장애 복구 시간(MTTR) 70% 단축

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">정적 임계치 오탐 폭증 및 전수 딥러닝 시 백프레셔 발생</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">2-Tier 하이브리드 필터링 (EWMA 1차 + AutoEncoder 2차)</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">오탐율 &le; 0.1%, 탐지 레이턴시 &le; 50ms, 지속성 3회 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">알람 피로 해소, 추론 자원 80% 절감 및 MTTR 70% 단축</div>
  </div>
</div>

---

## 1교시 예상문제 (10점)

> 시계열 실시간 이상치 탐지 (Time Series Real-time Anomaly Detection)의 정의, 목적, 핵심 메커니즘을 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 정의·목적

- 정의: 고속 스트림 데이터에서 시간 순서와 자기상관성을 반영하여 정상 패턴 이탈을 초저지연(수 ms)으로 검출하는 선제적 품질·보안 관측 체계
- 목적: 연속 시계열에서 정상 추세·계절성·자기상관을 벗어난 값을 빠르게 찾아 장애나 이상 거래에 대응한다.

### 2. 핵심 관계

| 비교 항목 | 통계적 기법 (EWMA) | 딥러닝 기법 (AutoEncoder) |
|:---|:---|:---|
| **처리 레이턴시** | 극도로 낮음 (1ms 이내) | 보통 (50~300ms, GPU 요구) |
| **탐지 대상** | 단발성 포인트 이상치 | 복합 시퀀스 및 집단 이상치 |
| **다변량 지원** | 단변량 중심 | 수백 개 센서 다변량 지원 |
| **판정 메커니즘** | 동적 관리한계선($\mu \pm 3\sigma$) | 재구성 오차(Reconstruction Error) |

### 핵심 관계

| 비교 항목 | 통계적 기법 (EWMA) | 딥러닝 기법 (AutoEncoder) |
|:---|:---|:---|
| **처리 레이턴시** | 극도로 낮음 (1ms 이내) | 보통 (50~300ms, GPU 요구) |
| **탐지 대상** | 단발성 포인트 이상치 | 복합 시퀀스 및 집단 이상치 |
| **다변량 지원** | 단변량 중심 | 수백 개 센서 다변량 지원 |
| **판정 메커니즘** | 동적 관리한계선($\mu \pm 3\sigma$) | 재구성 오차(Reconstruction Error) |

- 제언: EWMA 등 경량 선별과 정밀 모델의 2단계를 적용하고 경보 임계값·드리프트·복구 조치를 함께 검증한다.
---

## 2~4교시 예상문제 (25점)

> 스마트 팩토리, 금융 사기 탐지(FDS), IT 인프라 모니터링 등 다양한 산업 분야에서 중요성이 증가하고 있는 시계열 데이터 실시간 이상치 탐지(Real-time Anomaly Detection)의 개념과 이상치의 3가지 유형을 설명하고, 주요 탐지 알고리즘(통계, 머신러닝, 딥러닝) 및 실시간 스트리밍 아키텍처를 제시하시오. (25점)

---

## 2~4교시 25점 답안

### Ⅰ. 시계열 실시간 이상치 탐지의 개요 및 3대 이상치 유형

1. **개념**: 고속 스트림 데이터에서 시간 순서와 자기상관성을 반영하여 정상 패턴 이탈을 초저지연(수 ms)으로 검출하는 선제적 품질·보안 관측 체계
2. **3대 이상치 유형**:
   - **포인트 이상치**: 단일 시점의 급격한 스파이크 (예: CPU 100% 급증)
   - **컨텍스트 이상치**: 특정 시간대/상황 맥락상 비정상 (예: 새벽 3시 대규모 이체)
   - **집단 이상치**: 개별 값은 정상이나 연속 시퀀스 패턴이 비정상 (예: 센서 고착)

### Ⅱ. 시계열 이상치 탐지 알고리즘 계열 비교

| 비교 항목 | 통계적 기법 (EWMA) | 딥러닝 기법 (AutoEncoder) |
|:---|:---|:---|
| **처리 레이턴시** | 극도로 낮음 (1ms 이내) | 보통 (50~300ms, GPU 요구) |
| **탐지 대상** | 단발성 포인트 이상치 | 복합 시퀀스 및 집단 이상치 |
| **다변량 지원** | 단변량 중심 | 수백 개 센서 다변량 지원 |
| **판정 메커니즘** | 동적 관리한계선($\mu \pm 3\sigma$) | 재구성 오차(Reconstruction Error) |

### Ⅲ. 엔드투엔드 실시간 스트리밍 아키텍처

1. **파이프라인**: Kafka(수집) $\to$ Flink 슬라이딩 윈도우(집계) $\to$ 2-Tier 추론 $\to$ 알림/차단
2. **2-Tier 계층형 필터링**: 1차 EWMA 경량 필터(99% 통과) + 2차 AutoEncoder 정밀 분석(1%)
3. **동적 임계값**: 지수이동평균을 중심 추세선으로 추종하여 계절성 변동에 따른 오탐 원천 차단

### Ⅳ. 실무 장애 예방 및 아키텍처 제언

1. **알람 피로 극복**: 3회 연속 윈도우 초과 시 경보 발송(Persistence Check)으로 노이즈 제거
2. **콘셉트 드리프트 대응**: 윈도우 통계치 실시간 갱신 및 지속 학습(MLOps) 파이프라인 확립
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제140회 4교시 4번 (시계열 데이터에서 실시간 이상치 탐지)
  - 컴퓨터시스템응용기술사 제132회 2교시 (AIOps 기반 인프라 이상 징후 실시간 탐지)
  - 정보관리기술사 제127회 1교시 (이상치 탐지 기법과 Isolation Forest)
- **표준 및 검증 출처**:
  - Charu C. Aggarwal, *Outlier Analysis (2nd Edition)*, Chapter 9: Time Series Anomaly Detection
  - Fei Tony Liu et al. (2008), "Isolation Forest", *IEEE ICDM*
  - Apache Flink Official Documentation, "Stateful Stream Processing & Event Time Windows"
---

## 연결 토픽

- [060. 시계열 AR·MA 모형 (Time Series AR·MA Model)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/060_time_series_ar_ma_model.md)
- [010. 이상치 (Outlier)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/010_outlier.md)
- [054. 데이터 관측가능성 (Data Observability)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/054_data_observability.md)
