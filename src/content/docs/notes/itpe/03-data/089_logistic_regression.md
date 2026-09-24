---
sidebar:
  order: 89
  label: "089. 로지스틱 회귀분석 (Logistic Regression)"
  badge:
    text: "A"
    variant: note
title: "로지스틱 회귀분석 (Logistic Regression) 및 오즈비와 시그모이드 수학적 유도"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 89
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "089"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>로지스틱 회귀분석 (Logistic Regression)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" role="img" aria-label="로지스틱 회귀 3단계 유도 및 시그모이드 S자 곡선 매핑">
  <defs>
    <linearGradient id="curveGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="var(--sl-color-accent, #3b82f6)" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="var(--sl-color-accent, #2563eb)" stop-opacity="1.0"/>
    </linearGradient>
    <marker id="arr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="220" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Left Side: 3단계 수식 유도 카드 -->
  <rect x="20" y="25" width="225" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
  <text x="30" y="44" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">1. 오즈 (Odds)</text>
  <text x="30" y="62" font-size="10" fill="var(--sl-color-text, #334155)">Odds = p / (1 - p) ∈ [0, +∞)</text>

  <path d="M 132 75 L 132 87" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#arr)"/>

  <rect x="20" y="87" width="225" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
  <text x="30" y="106" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">2. 로짓 변환 (Logit)</text>
  <text x="30" y="124" font-size="10" fill="var(--sl-color-text, #334155)">ln(Odds) = W^T·X + b = z ∈ (-∞, +∞)</text>

  <path d="M 132 137 L 132 149" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#arr)"/>

  <rect x="20" y="149" width="225" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
  <text x="30" y="168" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">3. 시그모이드 함수 (Sigmoid)</text>
  <text x="30" y="186" font-size="10" font-weight="600" fill="var(--sl-color-accent, #1d4ed8)">p = 1 / (1 + e^-z) ∈ [0, 1]</text>

  <!-- Right Side: Sigmoid S-Curve Plot -->
  <g transform="translate(280, 25)">
    <!-- Axes -->
    <line x1="20" y1="165" x2="210" y2="165" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="1.5"/>
    <line x1="115" y1="15" x2="115" y2="175" stroke="var(--sl-color-gray-3, #94a3b8)" stroke-width="1.5"/>
    <text x="210" y="180" font-size="10" text-anchor="end" fill="var(--sl-color-gray-2, #64748b)">z (선형 결합)</text>
    <text x="110" y="12" font-size="10" text-anchor="end" fill="var(--sl-color-gray-2, #64748b)">확률 p</text>

    <!-- Horizontal Guides: p=1, p=0.5, p=0 -->
    <line x1="20" y1="25" x2="200" y2="25" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-dasharray="3 3"/>
    <text x="15" y="28" font-size="9.5" text-anchor="end" fill="var(--sl-color-gray-3, #94a3b8)">1.0</text>

    <line x1="20" y1="95" x2="200" y2="95" stroke="var(--sl-color-accent, #93c5fd)" stroke-dasharray="4 2"/>
    <text x="15" y="98" font-size="9.5" text-anchor="end" fill="var(--sl-color-accent, #2563eb)">0.5</text>
    <text x="202" y="98" font-size="9" fill="var(--sl-color-accent, #2563eb)">Threshold</text>

    <text x="15" y="168" font-size="9.5" text-anchor="end" fill="var(--sl-color-gray-3, #94a3b8)">0.0</text>

    <!-- Sigmoid S-Curve -->
    <path d="M 25 163 C 65 163, 85 140, 115 95 C 145 50, 165 27, 205 27" fill="none" stroke="url(#curveGrad)" stroke-width="3.5" stroke-linecap="round"/>

    <!-- Center Point (z=0, p=0.5) -->
    <circle cx="115" cy="95" r="4" fill="var(--sl-color-accent, #2563eb)"/>
  </g>
</svg>
</div>

- 본질: **종속변수 $Y$가 성공(1) 또는 실패(0)와 같은 이진 범주형일 때, 일반 선형 회귀의 예측값이 음수나 1을 초과하는 확률 모순을 해결하기 위해, 오즈(Odds)와 로짓(Logit) 변환을 거쳐 시그모이드 함수를 통해 0과 1 사이의 사건 발생 확률을 모델링하는 통계적 분류 기법**
- 암기: `오-로-시-엠` (오즈, 로짓 변환, 시그모이드 함수, 최대우도추정법 MLE) / `오-즈-비` ($e^{\beta_i}$ 배수 증가를 통한 완벽한 설명력)
- 판단축:
  - **선형 회귀**: 연속형 수치 예측, 최소자승법(OLS), 잔차의 정규성 가정, 출력 범위 $(-\infty, +\infty)$
  - **로지스틱 회귀**: 범주형 발생 확률(이진/다항) 예측, 최대우도추정법(MLE), 이진 교차 엔트로피 손실, 출력 범위 $[0, 1]$
- 주의: 로지스틱 회귀의 최대 강점은 단순 예측 정확도가 아니라 **회귀 계수의 완벽한 해석력(Interpretability)**에 있음. 독립변수 $X_i$의 회귀 계수 $\beta_i$에 지수를 취한 **오즈비(Odds Ratio, $e^{\beta_i}$)**를 통해 비즈니스 인과관계를 경영진 및 규제 기관에 수학적으로 명확히 설명할 수 있음
---

## 1교시 예상문제 (10점)

> 로지스틱 회귀분석 (Logistic Regression) 및 오즈비와 시그모이드 수학적 유도의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### [문제] 로지스틱 회귀분석 (Logistic Regression)

#### 1. 로지스틱 회귀분석의 개념 및 도입 배경
- **배경**: 종속변수가 0 또는 1인 이진 분류에서 일반 선형회귀 적용 시 출력이 음수나 1을 초과하는 모순 발생
- **개념**: 독립변수의 선형 결합을 시그모이드 함수에 매핑하여 사건 발생 확률($0 \sim 1$)을 모델링하는 통계 기법

#### 2. 수학적 유도 3단계 파이프라인

| 유도 단계 | 수학적 수식 | 출력 범위 및 핵심 의미 |
|:---|:---|:---|
| **1. 오즈 (Odds)** | $\text{Odds} = \frac{p}{1 - p}$ | $[0, +\infty)$ : 실패 대비 성공 비율 |
| **2. 로짓 변환 (Logit)** | $\ln(\text{Odds}) = W^T X + b = z$ | $(-\infty, +\infty)$ : 선형 결합식과 등호 연결 |
| **3. 시그모이드 (Sigmoid)** | $p = \frac{1}{1 + e^{-z}}$ | $[0, 1]$ : 유효한 사건 발생 확률값 완전 보장 |

#### 3. 회귀계수의 통계적 의미 (오즈비) 및 실무 제언
- **오즈비(Odds Ratio)**: $e^{\beta_i}$는 $X_i$가 1단위 증가할 때 사건 발생 오즈가 몇 배 증가하는지를 나타내어 완벽한 인과적 설명력 제공
- **실무 제언**: 금융·의료 등 규제 환경에서 설명 가능성(XAI)을 확보하기 위한 필수 베이스라인 모델로 운용
---

### 핵심 관계

| 비교 항목 | 선형 회귀 (Linear Regression) | 로지스틱 회귀 (Logistic Regression) |
|:---|:---|:---|
| **종속변수($Y$)의 성격** | **연속형 수치 (Continuous)** (예: 매출액, 주가) | **이진 범주형 (Binary)** (예: 이탈/유지, 부도/정상) |
| **모델 방정식** | $Y = W^T X + b$ | $P(Y=1) = \frac{1}{1 + e^{-(W^T X + b)}}$ |
| **출력값의 범위** | $(-\infty, +\infty)$ (음수 및 무한대 가능) | **$[0, 1]$ (사건 발생 확률로 완전 제한)** |
| **모수 추정 기법** | **최소자승법 (OLS)** (해석적 정규방정식 가능) | **최대우도추정법 (MLE)** (수치적 반복 경사하강법) |
| **손실 함수 (Loss)** | 평균제곱오차 (MSE, Mean Squared Error) | 이진 교차 엔트로피 (Binary Cross Entropy) |
| **계수의 해석** | $X$가 1 증가 시 $Y$의 절대 증가량 | $X$가 1 증가 시 **사건 발생 오즈비($e^\beta$) 배수** |

---

## 2~4교시 예상문제 (25점)

> 머신러닝 분류 알고리즘 중 가장 널리 사용되는 로지스틱 회귀분석(Logistic Regression)의 개념과 도입 배경을 설명하고, 오즈(Odds), 로짓 변환(Logit), 시그모이드 함수(Sigmoid)로 이어지는 3단계 수학적 유도 과정과 회귀계수의 통계적 의미(오즈비)를 서술하시오. (10점 / 25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 선형 회귀의 확률 모순을 극복하는 로지스틱 회귀분석 개요

#### 한줄 요약: 이진 사건의 발생 확률을 0과 1 사이로 안정적으로 제한하기 위해 로짓과 시그모이드 변환을 적용한 분류 모델

- **일반 선형 회귀(Linear Regression)의 한계**:
  - 고객의 이탈 여부(1: 이탈, 0: 유지)를 선형 회귀 모델($Y = W^T X + b$)로 적합하면, 특정 독립변수 값에 따라 예측치 $Y$가 음수($-0.3$)가 되거나 1을 초과($1.5$)하는 수학적 모순이 발생함
  - 또한 오차항이 정규분포를 따르지 않고 이항분포를 따르므로 최소자승법(OLS)의 가정이 붕괴됨
- **로지스틱 회귀의 정의**:
  - 독립변수의 선형 결합을 비선형 함수인 **시그모이드(로지스틱) 함수**에 통과시켜, 임의의 실수 입력값을 항상 $0 \le P(Y=1|X) \le 1$의 유효한 확률값으로 변환하여 분류를 수행하는 통계적 지도학습 기법

### Ⅱ. 로지스틱 회귀의 수학적 유도 3단계 파이프라인

#### 한줄 요약: 확률 $p$에서 시작하여 오즈(비율) $\rightarrow$ 로짓(선형화) $\rightarrow$ 시그모이드(확률 역정리)로 도출되는 3단계 과정

### 1. 1단계: 오즈 (Odds, 승산비)
- 어떤 사건이 일어날 확률($p$)과 일어나지 않을 확률($1 - p$)의 비율:
  $$\text{Odds} = \frac{p}{1 - p} \quad (0 \le p \le 1)$$
  - $p = 0$ 이면 $\text{Odds} = 0$, $p = 1$ 이면 $\text{Odds} \rightarrow +\infty$
  - 값의 범위가 $[0, +\infty)$로 확장되었으나, 여전히 음수 값을 표현할 수 없는 한계 존재

### 2. 2단계: 로짓 변환 (Logit Transformation)
- 오즈에 자연로그($\ln$)를 취하여 값의 범위를 음의 무한대부터 양의 무한대까지 $(-\infty, +\infty)$로 확장:
  $$\text{Logit}(p) = \ln\left(\frac{p}{1 - p}\right) = z$$
- 이제 로짓 값 $z$는 실수 전체 범위를 가지므로, **독립변수들의 선형 결합(Linear Combination)**과 직접 등호로 연결 가능:
  $$\ln\left(\frac{p}{1 - p}\right) = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k = W^T X + b$$

### 3. 3단계: 시그모이드 함수 (Sigmoid / Logistic Function)
- 우리가 최종적으로 구하고자 하는 값은 선형 결합 $z$가 아니라 **사건 발생 확률 $p$**임
- 위 로짓 방정식을 $p$에 대하여 대수적으로 풀면 시그모이드 함수가 유도됨:
  $$\frac{p}{1 - p} = e^z \implies p = e^z (1 - p) = e^z - p \cdot e^z \implies p(1 + e^z) = e^z$$
  $$p = \frac{e^z}{1 + e^z} = \frac{1}{1 + e^{-z}} = \frac{1}{1 + e^{-(W^T X + b)}}$$
- 이로써 모든 실수 입력 $z$에 대해 출력이 정확히 $0 < p < 1$로 제한되는 아름다운 S자 곡선 완성

### Ⅲ. 회귀 계수의 통계적 의미: 오즈비(Odds Ratio)의 해석력

#### 한줄 요약: 독립변수가 1단위 증가할 때 사건 발생 오즈가 몇 배 증가하는지를 나타내는 $e^\beta$의 인과적 설명력

- **오즈비(Odds Ratio, OR)의 수학적 도출**:
  - $X_1$이 $x$일 때: $\text{Odds}_1 = e^{\beta_0 + \beta_1 x}$
  - $X_1$이 $x+1$일 때: $\text{Odds}_2 = e^{\beta_0 + \beta_1 (x + 1)} = e^{\beta_0 + \beta_1 x} \cdot e^{\beta_1}$
  - $\text{Odds Ratio} = \frac{\text{Odds}_2}{\text{Odds}_1} = e^{\beta_1}$
- **오즈비(Odds Ratio, OR)의 해석 기준**:
  - **$\text{OR} = e^{\beta_i} > 1$ ($\beta_i > 0$)**: 독립변수 $X_i$가 1단위 증가할 때 사건 발생 오즈가 $e^{\beta_i}$배 **증가**함 (양의 영향)
    - 예: 연령 변수의 $\beta = 0.182$이면, $e^{0.182} \approx 1.20 \rightarrow$ 나이가 1살 많아질 때마다 대출 연체 오즈가 1.2배(20%) 증가함
  - **$\text{OR} = e^{\beta_i} = 1$ ($\beta_i = 0$)**: $X_i$의 변화가 사건 발생에 아무런 영향을 미치지 않음
  - **$\text{OR} = e^{\beta_i} < 1$ ($\beta_i < 0$)**: $X_i$가 1단위 증가할 때 사건 발생 오즈가 감소함 (음의 영향, 보호 요인)

### Ⅳ. 모델 최적화: 최대우도추정법(MLE)과 이진 교차 엔트로피

#### 한줄 요약: 비선형 S자 곡선으로 인해 최소자승법 대신 우도 함수를 최대화하는 경사하강법 적용

- **우도 함수 (Likelihood Function)**:
  - 관측된 $N$개의 표본 데이터에 대해 베르누이 확률질량함수를 결합:
    $$L(W) = \prod_{i=1}^{N} p_i^{y_i} (1 - p_i)^{1 - y_i} \quad (y_i \in \{0, 1\})$$
- **로그 우도 함수 및 이진 교차 엔트로피 (Binary Cross-Entropy Loss)**:
  - 계산 편의와 언더플로우 방지를 위해 음의 로그 우도(NLL)를 취하여 최소화 문제로 전환:
    $$J(W) = -\frac{1}{N} \sum_{i=1}^{N} \left[ y_i \ln(p_i) + (1 - y_i) \ln(1 - p_i) \right]$$
  - 손실 함수 $J(W)$는 볼록 함수(Convex)이므로 경사하강법(Gradient Descent)으로 전역 최적해(Global Optimum) 수렴 보장

### Ⅴ. 선형 회귀 vs 로지스틱 회귀 심층 비교

#### 한줄 요약: 연속형 값 예측과 이진 확률 분류 간의 목적, 수식, 최적화 방법 및 손실 함수 비교

| 비교 항목 | 선형 회귀 (Linear Regression) | 로지스틱 회귀 (Logistic Regression) |
|:---|:---|:---|
| **종속변수($Y$)의 성격** | **연속형 수치 (Continuous)** (예: 매출액, 주가) | **이진 범주형 (Binary)** (예: 이탈/유지, 부도/정상) |
| **모델 방정식** | $Y = W^T X + b$ | $P(Y=1) = \frac{1}{1 + e^{-(W^T X + b)}}$ |
| **출력값의 범위** | $(-\infty, +\infty)$ (음수 및 무한대 가능) | **$[0, 1]$ (사건 발생 확률로 완전 제한)** |
| **모수 추정 기법** | **최소자승법 (OLS)** (해석적 정규방정식 가능) | **최대우도추정법 (MLE)** (수치적 반복 경사하강법) |
| **손실 함수 (Loss)** | 평균제곱오차 (MSE, Mean Squared Error) | 이진 교차 엔트로피 (Binary Cross Entropy) |
| **계수의 해석** | $X$가 1 증가 시 $Y$의 절대 증가량 | $X$가 1 증가 시 **사건 발생 오즈비($e^\beta$) 배수** |

### Ⅵ. 실무 적용 시 주요 난제와 엔지니어링 극복 방안

#### 한줄 요약: 클래스 불균형에 따른 임계값(Threshold) 튜닝과 다중공선성 방지를 위한 L1/L2 정규화 적용

### 1. 극단적 클래스 불균형 (Class Imbalance)과 임계값 조정
- **문제점**: 사기 거래(FDS)나 암 진단처럼 정상 99%, 이상 1%인 데이터에서 기본 임계값(0.5)을 쓰면 모델이 전부 0으로 예측하여 실제 환자를 놓치는 위음성(FN) 참사 발생
- **해결책**:
  - **비용 민감 임계값(Cost-sensitive Threshold)**: Precision-Recall 곡선을 분석하여 임계값을 0.2~0.3 수준으로 하향 조정하여 재현율(Recall) 극대화
  - 손실 함수에 가중치를 부여하는 `class_weight='balanced'` 적용

### 2. 다중공선성(Multicollinearity)과 정규화(Regularization)
- **문제점**: 독립변수 간 상관관계가 높으면 회귀계수의 분산이 커져 오즈비 부호가 뒤집히는 왜곡 발생
- **해결책**:
  - **L1 Lasso 규제**: 불필요한 변수의 계수를 정확히 0으로 만들어 자동 변수 선택(Feature Selection) 수행
  - **L2 Ridge 규제**: 계수의 크기를 고르게 축소하여 공선성에 의한 이상 팽창 억제

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 머신러닝 현업에서 딥러닝(Deep Learning)이나 XGBoost/LightGBM 같은 트리 앙상블이 유행하지만, 금융 신용평가, 보험 심사, 의료 진단 등 규제 산업(Regulated Industries)에서는 여전히 로지스틱 회귀가 절대적인 표준이다. 그 이유는 회귀계수의 지수승($e^\beta$)인 '오즈비(Odds Ratio)'가 제공하는 투명한 설명력(Explainability) 덕분이다. "귀하의 대출이 거절되었습니다"라는 판정에 대해 "소득 대비 부채비율이 1단위 높아 연체 오즈가 1.5배 상승했기 때문"이라고 설명할 수 있는 모델은 로지스틱 회귀뿐이다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 오즈 $\to$ 로짓 $\to$ 시그모이드의 3단계 수식 전개 파이프라인을 명쾌하게 증명하고, 시그모이드 S자 곡선(Threshold 0.5)을 도식화하겠다. 2교시형이라면 선형 회귀와의 구조적 비교표를 제시하고, 클래스 불균형 시 Threshold 튜닝 전략과 설명 가능한 AI(XAI) 기준선(Baseline)으로서의 역할, 그리고 다항 분류(Softmax)로의 확장 전략을 제언에 부각하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 딥러닝 및 앙상블 모델은 높은 정확도를 제공하나 블랙박스 특성으로 인해 금융소비자보호법, GDPR 등의 설명요구권(Right to Explanation) 충족이 불가함. 또한 무분별한 복잡 모델 적용은 서빙 비용 증가와 과적합 위험 초래.
- **대응 (개선 방안)**: 신규 AI 과제 기획 시 로지스틱 회귀의 오즈비($e^\beta$) 및 Wald 검정($p\text{-value}$) 기반의 인과성 분석을 필수 베이스라인(Baseline)으로 수립하고, 다항 분류 시 소프트맥스 회귀로 단계적 확장.
- **검증 (검증 기준)**: 오즈비 신뢰구간(95% CI) 유효성, 다중공선성 VIF < 10 충족 여부, FDS/암 진단 도메인별 최적 임계값(Threshold) 튜닝을 통한 Recall/F1-score 달성도 검증.
- **효과 (실행 효과)**: 규제 기관 감사 대응 비용 50% 절감, 고객 분쟁 해소 및 AI 신뢰성 확보, 경량 알고리즘 적용으로 인퍼런스 레이턴시 5ms 이내 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">블랙박스 딥러닝 남발로 설명요구권(GDPR 등) 미충족 및 서빙 비용 과다</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">로지스틱 회귀 오즈비 기반 설명 가능 AI(XAI) 1차 베이스라인 의무화</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">오즈비 95% CI 검증, VIF &lt; 10, 불균형 데이터 PR 곡선 최적 임계값</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">규제 대응 리스크 해소, 모델 해석성 100% 확보, 초저지연 서빙 구현</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제124회 1교시 (로지스틱 회귀분석의 개념, 오즈비 및 시그모이드 유도)
  - 컴퓨터시스템응용기술사 제120회 2교시 (선형 분류 기법과 로지스틱 회귀분석)
  - 정보관리기술사 제113회 1교시 (오즈비(Odds Ratio)와 로짓 변환의 통계적 의미)
- **표준 및 검증 출처**:
  - David W. Hosmer Jr. et al., *Applied Logistic Regression (3rd Edition)*, Wiley
  - Trevor Hastie, Robert Tibshirani, Jerome Friedman, *The Elements of Statistical Learning*, Chapter 4
  - Christopher M. Bishop, *Pattern Recognition and Machine Learning*, Chapter 4.3
---

## 연결 토픽

- [036. 기술통계 vs 추론통계 (Descriptive vs Inferential Statistics)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/036_descriptive_statistics.md)
- [043. 데이터마이닝 (Data Mining)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/043_data_mining.md)
- [062. 앙상블 (배깅·부스팅) (Ensemble Learning)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/062_ensemble_bagging_boosting.md)
