---
sidebar:
  order: 69
  label: "069. 차원 축소 (PCA·다차원척도법)"
  badge:
    text: "A"
    variant: note
title: "차원 축소 (Dimensionality Reduction) 및 PCA·다차원척도법(MDS)"
author: "Antigravity"
date: "2026-09-20T18:25:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 69
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
  question_no: "069"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>머신러닝·데이터마이닝</span><strong>차원 축소 (PCA·다차원척도법)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">차원 축소의 양대 축: 주성분분석(PCA) vs 다차원척도법(MDS)</text>

  <!-- Left: PCA Plot -->
  <g transform="translate(30, 48)">
    <rect x="0" y="0" width="220" height="210" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <rect x="0" y="0" width="220" height="26" rx="6" fill="#eff6ff"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">PCA (주성분분석: 분산 최대화)</text>

    <!-- Axes -->
    <line x1="25" y1="165" x2="200" y2="165" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="25" y1="165" x2="25" y2="40" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="195" y="178" font-size="8.5" fill="#64748b">X₁</text>
    <text x="15" y="45" font-size="8.5" fill="#64748b">X₂</text>

    <!-- Data Points Scatter -->
    <circle cx="50" cy="150" r="3" fill="#93c5fd"/>
    <circle cx="70" cy="135" r="3" fill="#93c5fd"/>
    <circle cx="90" cy="130" r="3" fill="#93c5fd"/>
    <circle cx="110" cy="110" r="3" fill="#93c5fd"/>
    <circle cx="130" cy="100" r="3" fill="#93c5fd"/>
    <circle cx="150" cy="85" r="3" fill="#93c5fd"/>
    <circle cx="170" cy="70" r="3" fill="#93c5fd"/>

    <!-- PC1 Line -->
    <line x1="35" y1="160" x2="190" y2="60" stroke="#2563eb" stroke-width="2"/>
    <text x="175" y="55" font-size="8.5" font-weight="bold" fill="#2563eb">PC1 (Max Var)</text>

    <!-- PC2 Line (Orthogonal) -->
    <line x1="90" y1="75" x2="145" y2="155" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="2,2"/>
    <text x="148" y="150" font-size="8" fill="#dc2626">PC2 ⊥ PC1</text>

    <text x="110" y="195" font-size="8.5" fill="#475569" text-anchor="middle">공분산 고유값 분해 &middot; 직교 투영</text>
  </g>

  <!-- Right: MDS Plot -->
  <g transform="translate(270, 48)">
    <rect x="0" y="0" width="220" height="210" rx="6" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <rect x="0" y="0" width="220" height="26" rx="6" fill="#ecfdf5"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#065f46" text-anchor="middle">MDS (다차원척도법: 거리 보존)</text>

    <!-- Distance Matrix snippet -->
    <rect x="25" y="38" width="170" height="42" rx="3" fill="#f8fafc" stroke="#e2e8f0"/>
    <text x="35" y="52" font-size="8" fill="#475569">고차원 거리 행렬 (d_ij)</text>
    <text x="35" y="66" font-size="7.5" fill="#64748b">A-B: 5.2 | B-C: 3.1 | A-C: 8.0</text>

    <!-- Stress Optimization Arrow -->
    <path d="M 110 82 L 110 98" stroke="#10b981" stroke-width="1.5"/>
    <text x="135" y="93" font-size="7.5" fill="#047857">Stress 최소화</text>

    <!-- 2D Coordinate Map -->
    <rect x="25" y="100" width="170" height="75" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
    <circle cx="55" cy="150" r="5" fill="#10b981"/>
    <text x="65" y="154" font-size="8.5" font-weight="bold" fill="#065f46">A</text>

    <circle cx="115" cy="118" r="5" fill="#10b981"/>
    <text x="125" y="122" font-size="8.5" font-weight="bold" fill="#065f46">B</text>

    <circle cx="170" cy="130" r="5" fill="#10b981"/>
    <text x="178" y="134" font-size="8.5" font-weight="bold" fill="#065f46">C</text>

    <!-- Inter-point lines -->
    <line x1="55" y1="150" x2="115" y2="118" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>
    <line x1="115" y1="118" x2="170" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="2,2"/>

    <text x="110" y="195" font-size="8.5" fill="#475569" text-anchor="middle">개체 간 상대적 비유사도 기하 배치</text>
  </g>
</svg>
</div>

- 본질: **데이터의 변수(특성) 수가 증가함에 따라 발생하는 연산 복잡도 폭증과 공간 희소화(차원의 저주)를 극복하기 위해, 전체 데이터의 정보 변동성(분산)을 최대화하는 직교 축으로 투영(PCA)하거나 개체 간의 거리·근접도 관계를 보존(MDS)하여 핵심 정보를 유지한 채 저차원으로 압축하는 기법**
- 암기: `표-공-고-선-투` (PCA: 표준화, 공분산 행렬 계산, 고유값/고유벡터 분해, 주성분 선택, 투영) / `거-스-좌-최` (MDS: 거리 행렬, 스트레스 지수, 저차원 좌표 배치, 손실 최소화)
- 판단축:
  - **PCA (Principal Component Analysis)**: 변수 간의 선형 상관관계를 분석하여 분산이 가장 큰 직교 기저(Orthogonal Basis)로 투영 $\rightarrow$ 다중공선성 제거 및 머신러닝 전처리 최적
  - **MDS (Multidimensional Scaling)**: 개체 간의 거리(유클리드 또는 순위 서열) 행렬만을 바탕으로 2D/3D 평면에 시각적 포지셔닝 맵 구축 $\rightarrow$ 소비자 선호도 및 인식도 분석 최적
- 주의: PCA는 선형 변환이므로 비선형 매니폴드(Swiss Roll 등) 구조를 보존하지 못하고 뭉개버리며, 변수들의 척도(Scale)에 극도로 민감하므로 분석 전 반드시 Z-Score 표준화(Standardization)를 선행해야 함

## 예상문제

> 데이터 마이닝 및 머신러닝에서 다차원 데이터를 처리할 때 발생하는 차원의 저주(Curse of Dimensionality)의 개념과 차원 축소의 필요성을 설명하고, 대표적인 차원 축소 기법인 주성분분석(PCA)과 다차원척도법(MDS)의 원리, 수학적 메커니즘 및 차이점을 비교하시오. (25점)

## Ⅰ. 차원의 저주를 극복하는 차원 축소(Dimensionality Reduction) 개요

#### 한줄 요약: 데이터의 차원 증가에 따른 희소성과 연산 복잡도를 해결하기 위해 핵심 정보(분산, 거리)를 보존하며 축소하는 기술

- **차원의 저주(Curse of Dimensionality)의 본질**:
  - 특성(Feature) 차원 수 $D$가 증가할수록 데이터가 존재하는 공간의 부피는 $2^D$로 기하급수적으로 팽창함
  - 이로 인해 데이터 포인트 간의 거리가 거의 균일해지며 공간이 극도로 희소(Sparse)해져, 모델이 쉽게 과적합(Overfitting)되고 거리 기반 알고리즘(KNN, K-Means)의 변별력이 상실됨
- **차원 축소의 정의 및 목적**:
  - 원래 데이터 집합이 가진 내재적 차원(Intrinsic Dimension)의 주요 정보를 최소한의 손실로 보존하면서, 관측 변수의 수를 줄여 모델 연산 가속, 노이즈 제거, 다중공선성 해소 및 2D/3D 인간 시각화를 실현함

## Ⅱ. 주성분분석 (PCA, Principal Component Analysis) 원리

#### 한줄 요약: 공분산 행렬의 고유값 분해를 통해 서로 상관관계가 없는 직교 주성분 축을 찾아 분산을 최대화하는 선형 투영 기법

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 115" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="95" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">PCA 5단계 수학적 절차</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="85" height="50" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="42" y="18" font-size="8.5" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 데이터 표준화</text>
    <text x="42" y="35" font-size="7.5" fill="#475569" text-anchor="middle">평균 0, 분산 1</text>

    <path d="M 88 25 L 98 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="100" y="0" width="85" height="50" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="142" y="18" font-size="8.5" font-weight="bold" fill="#1e40af" text-anchor="middle">2. 공분산 행렬</text>
    <text x="142" y="35" font-size="7.5" fill="#475569" text-anchor="middle">Σ 산출 (d×d)</text>

    <path d="M 188 25 L 198 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="200" y="0" width="85" height="50" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="242" y="18" font-size="8.5" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 고유값 분해</text>
    <text x="242" y="35" font-size="7.5" fill="#475569" text-anchor="middle">Σv = λv</text>

    <path d="M 288 25 L 298 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="300" y="0" width="85" height="50" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="342" y="18" font-size="8.5" font-weight="bold" fill="#1e40af" text-anchor="middle">4. 주성분 선별</text>
    <text x="342" y="35" font-size="7.5" fill="#475569" text-anchor="middle">설명분산 85%</text>

    <path d="M 388 25 L 398 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="400" y="0" width="70" height="50" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="435" y="18" font-size="8.5" font-weight="bold" fill="#1e40af" text-anchor="middle">5. 저차원 투영</text>
    <text x="435" y="35" font-size="7.5" fill="#475569" text-anchor="middle">Z = X · W</text>
  </g>
</svg>
</div>

### 1. 수학적 의미: 고유값(Eigenvalue)과 고유벡터(Eigenvector)
- **고유벡터 (Eigenvector, $v$)**: 데이터의 분산이 가장 큰 축의 **방향(Direction)**을 나타냄 (서로 수직인 직교성 보장: $v_1 \perp v_2$)
- **고유값 (Eigenvalue, $\lambda$)**: 해당 고유벡터 방향 축을 따라 데이터가 얼마나 넓게 퍼져있는지, 즉 **분산의 크기(Magnitude of Variance)**를 나타냄
- **설명된 분산 비율 (Explained Variance Ratio)**:
  $$\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^{d} \lambda_j}$$

### 2. 스크리 플롯(Scree Plot)과 주성분 개수 결정
- 주성분 번호에 대응하는 고유값을 꺾은선 그래프로 시각화
- 고유값이 급격히 완만해지는 지점인 **엘보우(Elbow Point)** 또는 누적 설명 분산이 80~90%에 달하는 지점까지의 주성분 개수를 최종 차원 $k$로 채택

## Ⅲ. 다차원척도법 (MDS, Multidimensional Scaling) 원리

#### 한줄 요약: 객체 간의 거리(비유사도) 정보를 보존하면서 저차원 좌표 공간에 객체들을 기하학적으로 배치하는 기법

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 115" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="95" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">다차원척도법(MDS) 손실 최적화 흐름</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="135" height="50" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <text x="67" y="18" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">고차원 거리 행렬 (d_ij)</text>
    <text x="67" y="35" font-size="8" fill="#475569" text-anchor="middle">유클리드 / 설문 순위</text>

    <path d="M 140 25 L 165 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="170" y="0" width="140" height="50" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <text x="240" y="18" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">Stress 지수 최적화</text>
    <text x="240" y="35" font-size="8" fill="#475569" text-anchor="middle">경사하강법 (SMACOF)</text>

    <path d="M 315 25 L 340 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="345" y="0" width="125" height="50" rx="4" fill="#ecfdf5" stroke="#059669" stroke-width="1.2"/>
    <text x="407" y="18" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">저차원 기하 좌표</text>
    <text x="407" y="35" font-size="8" fill="#475569" text-anchor="middle">2D/3D 상대적 배치</text>
  </g>
</svg>
</div>

### 1. 스트레스 지수 (Stress Measure)
- MDS의 적합도(Goodness of Fit)를 평가하는 목적함수:
  $$\text{Stress} = \sqrt{\frac{\sum_{i < j} (d_{ij} - \hat{d}_{ij})^2}{\sum_{i < j} d_{ij}^2}}$$
  - $d_{ij}$: 고차원 공간 상의 실제 거리 (또는 입력된 비유사도)
  - $\hat{d}_{ij}$: 저차원 공간에 배치된 두 점 사이의 유클리드 거리 ($\|x_i - x_j\|$)
- Stress 값이 **0.05 이하**이면 매우 우수, **0.15 이상**이면 저차원 배치의 왜곡이 심함을 의미

### 2. MDS의 2가지 유형
- **계량적 MDS (Classical / Metric MDS)**:
  - 입력 데이터가 비율 척도나 구간 척도로 측정된 실제 수치 거리인 경우 적용 (유클리드 거리 보존)
- **비계량적 MDS (Non-metric MDS, Kruskal)**:
  - 입력 데이터가 순위나 서열 척도(예: "A가 B보다 C에 더 가깝다")인 경우 적용
  - 거리의 절대 수치 대신 **순위 서열(Monotonicity)**만을 보존하도록 단조 회귀(Monotonic Regression)를 결합

## Ⅳ. PCA vs MDS 심층 비교

#### 한줄 요약: 분산 보존 기반의 직교 변환인 PCA와 거리 보존 기반의 기하학적 배치인 MDS의 종합 비교

| 비교 항목 | 주성분분석 (PCA) | 다차원척도법 (MDS) |
|:---|:---|:---|
| **최우선 보존 대상** | 데이터 전체의 **변동성(분산, Information)** | 데이터 개체들 간의 **상대적 거리 및 근접도** |
| **입력 데이터 형태** | 관측치 $\times$ 변수로 이루어진 **원시 데이터 행렬 ($n \times d$)** | 개체 간의 거리로 이루어진 **거리/비유사도 행렬 ($n \times n$)** |
| **연산 알고리즘** | 공분산 행렬의 **고유값 분해(Eigendecomposition) / SVD** | 목적함수(Stress)를 최소화하는 **경사하강법(SMACOF)** |
| **변수 생성 여부** | 원본 변수들의 선형 결합인 **새로운 주성분 변수 생성** | 좌표 축의 의미가 없는 **순수 2D/3D 기하학적 위치 도출** |
| **비계량(서열) 지원** | 미지원 (수치형 연속 데이터 필수) | **지원** (Kruskal의 비계량적 MDS로 순위 데이터 처리) |
| **주요 활용 분야** | 다중공선성 제거, ML 전처리, 잡음 필터링 | 소비자 브랜드 포지셔닝 맵, 심리학 설문 인식도 분석 |

## Ⅴ. 비선형 차원 축소 기법으로의 확장: t-SNE 및 UMAP

#### 한줄 요약: 선형 축소의 한계를 극복하고 복잡한 고차원 매니폴드의 국소적 유사성을 시각화하는 비선형 기법

- **t-SNE (t-Distributed Stochastic Neighbor Embedding)**:
  - 고차원에서 두 점이 이웃일 확률(가우시안 분포)과 저차원에서의 확률(Student-t 분포) 간의 **쿨백-라이블러 발산(KLD)**을 최소화
  - 국소적 군집(Cluster) 구조를 2차원에 시각화하는 데 탁월하나, 전역적 거리 관계(Global Geometry)는 보존되지 않음
- **UMAP (Uniform Manifold Approximation and Projection)**:
  - 리만 기하학과 퍼지 집합론에 기반하여 국소적 구조와 전역적 구조를 동시에 우수하게 보존하며, t-SNE 대비 연산 속도가 압도적으로 빠름

## Ⅵ. 실무 적용 사례 및 다중공선성 해소 전략

#### 한줄 요약: 회귀 모델의 VIF 위험 해소, 소비자 인식 포지셔닝 맵 작성, 유전체 데이터 시각화에서의 실무 구현

### 1. 다중공선성(Multicollinearity) 완전 해소
- 회귀분석 시 변수 간 강한 상관관계로 인해 분산팽창지수(VIF)가 10을 초과하면 회귀계수 부호가 왜곡됨
- PCA를 통해 서로 직교(Orthogonal)하여 상관계수가 정확히 0인 상위 주성분들을 회귀 모델의 독립변수로 투입(PCR, Principal Component Regression)하여 다중공선성을 완벽히 제거

### 2. 마케팅 브랜드 포지셔닝 맵 (MDS)
- 소비자 1,000명에게 10개 자동차 브랜드 간의 '유사한 정도(1~7점)'를 설문 조사하여 $10 \times 10$ 비유사도 행렬 생성
- 비계량적 MDS를 적용하여 2차원 평면에 브랜드를 점으로 배치함으로써, '고급스러움 vs 실용성', '스포티함 vs 안락함'의 숨겨진 축을 발굴

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 차원 축소의 본질적 딜레마는 **"정보 압축률과 비즈니스 해석력(XAI) 간의 교환(Trade-off)"**이다. PCA로 100개 피처를 3개 주성분으로 압축하면 모델 연산 속도는 빨라지고 다중공선성은 사라지지만, "주성분 1이 증가한 원인이 무엇인가?"라는 현업의 질문에 직관적으로 답하기 어렵다. 실무에서는 PCA 적용 시 주성분과 원본 변수 간의 상관계수인 **요인 적재량(Factor Loading)** 매트릭스를 반드시 함께 도출하여, 각 주성분의 도메인적 의미를 규명하는 사후 매핑 작업이 수반되어야 한다.

> **[나라면 이렇게 쓴다]**
> 10점형이라면 PCA(분산 최대화/선형직교)와 MDS(거리 보존/기하배치)의 핵심 5대 비교표를 명확히 작성하겠다. 25점형이라면 교차검증(CV) 시 전체 데이터에 PCA를 먼저 걸어버리는 '데이터 누수(Data Leakage)' 오류를 지적하고, Train 세트에서만 고유벡터를 학습(`fit`)하고 Test 세트에 투영(`transform`)하는 MLOps 파이프라인 무결성을 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 변수 증가에 따른 차원의 저주로 거리 알고리즘 성능 저하 및 다중공선성(VIF > 10)으로 회귀 모델 왜곡
- **대응 (개선 방안)**: 수치형 연속 변수는 PCA를 통해 직교 주성분으로 압축하고, 정성적 설문/인식 데이터는 비계량 MDS로 시각화 매핑
- **검증 (검증 기준)**: PCA 누적 설명 분산 비율(EVR) 85% 이상 확보, MDS Stress 지수 0.05 이하 수렴 검증, 요인 적재량(Factor Loading) 매핑
- **효과 (실행 효과)**: 머신러닝 모델 학습 시간 70% 단축, 다중공선성 원천 해소 및 브랜드 포지셔닝 인식도 시각화

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">차원의 저주로 인한 공간 희소화 및 다중공선성 회귀계수 왜곡</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">PCA 직교 선형 투영 + 비계량 MDS 기하 배치 하이브리드 파이프라인</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">누적 EVR &ge; 85%, Stress &le; 0.05, Train-Only PCA 데이터 누수 차단</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">모델 연산량 70% 절감, 다중공선성 해소 및 비즈니스 해석력(XAI) 확보</div>
  </div>
</div>

---

## 1교시 10점 답안 발췌

### 1. 차원 축소의 개념 및 필요성

- **개념**: 고차원 데이터의 핵심 정보(분산, 거리)를 최대한 보존하면서 저차원 공간으로 변환하는 피처 엔지니어링 기법
- **필요성**: 차원의 저주 극복(과적합 방지 및 거리 변별력 복원), 다중공선성 제거, 모델 연산 가속 및 2차원 시각화

### 2. PCA와 MDS의 메커니즘 비교

| 비교 항목 | 주성분분석 (PCA) | 다차원척도법 (MDS) |
|:---|:---|:---|
| **최우선 보존 대상** | 데이터 전체의 **'분산' 최대화** | 개체 간의 **'상대적 거리' 보존** |
| **입력 데이터** | 원시 특성 행렬 ($n \times d$) | 개체 간 거리/비유사도 행렬 ($n \times n$) |
| **수학적 기법** | 공분산 행렬의 **고유값 분해(SVD)** | 목적함수 **스트레스(Stress) 최소화** |
| **축의 성격** | 서로 직교하는 선형 주성분 축 | 기하학적 임의 좌표 (좌표축 자체 의미 없음) |
| **비계량 지원** | 미지원 (연속형 수치 한정) | **지원** (Kruskal 비계량적 MDS로 순위 데이터 처리) |

### 3. 실무 아키텍처 적용 제언

- **머신러닝 전처리**: 다중공선성 해소를 위해 서로 직교하는 주성분을 생성하는 PCA 적용 및 Factor Loading 매핑
- **정성 데이터 시각화**: 설문 순위 데이터 기반 브랜드 포지셔닝 맵 구축 시 비계량 MDS 적용

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제131회 1교시 (데이터 차원 축소의 필요성과 PCA, MDS 비교)
  - 컴퓨터시스템응용기술사 제123회 1교시 (차원의 저주와 주성분분석(PCA)의 원리)
  - 정보관리기술사 제114회 2교시 (다차원 데이터 시각화 기법과 MDS, t-SNE)
- **표준 및 검증 출처**:
  - Ian T. Jolliffe, *Principal Component Analysis (2nd Edition)*, Springer
  - Joseph B. Kruskal (1964), "Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis", *Psychometrika*
  - Trevor Hastie et al., *The Elements of Statistical Learning*, Chapter 14: Unsupervised Learning

---

## 학습 체크

- [ ] 차원의 저주(Curse of Dimensionality)가 발생할 때 거리 기반 알고리즘이 무력화되는 기하학적 원인은 무엇인가?
- [ ] PCA에서 공분산 행렬의 고유벡터(Eigenvector)와 고유값(Eigenvalue)이 갖는 물리적 의미는 각각 무엇인가?
- [ ] MDS의 목적함수인 스트레스(Stress) 지수의 수식과 판정 기준을 설명할 수 있는가?
- [ ] 계량적 MDS와 비계량적 MDS의 입력 데이터 척도 차이 및 최적화 방식의 차이는 무엇인가?
- [ ] **서술 연습 1**: PCA의 5단계 수행 절차를 수학적 수식(공분산 행렬, 고유값 분해)과 함께 10점형 답안으로 정리하시오.
- [ ] **서술 연습 2**: PCA, MDS, t-SNE의 차원 축소 철학과 수학적 접근 방식을 3각 비교표로 구성하고, 실무 머신러닝 파이프라인에서의 데이터 누수 방지 방안을 25점형으로 서술하시오.

---

## 연결 토픽

- [043. 데이터마이닝 (Data Mining)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/043_data_mining.md)
- [005. 군집분석 (Cluster Analysis)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/005_cluster_analysis.md)
- [044. 벡터 데이터베이스 (Vector Database)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/044_vector_database.md)
