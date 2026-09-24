---
sidebar:
  order: 62
  label: "062. 앙상블 (배깅·부스팅)"
  badge:
    text: "A"
    variant: note
title: "앙상블 학습 (Ensemble Learning) 및 배깅(Bagging)과 부스팅(Boosting)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 62
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "062"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>머신러닝·데이터마이닝</span><strong>앙상블 (배깅·부스팅)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">앙상블 양대 축: 배깅(Bagging) vs 부스팅(Boosting)</text>

  <!-- Left Side: Bagging -->
  <g transform="translate(30, 48)">
    <rect x="0" y="0" width="220" height="210" rx="6" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <rect x="0" y="0" width="220" height="26" rx="6" fill="#eff6ff"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#1e40af" text-anchor="middle">배깅 (Bagging: 분산 감소)</text>

    <!-- Raw Data -->
    <rect x="60" y="35" width="100" height="22" rx="3" fill="#f1f5f9" stroke="#94a3b8"/>
    <text x="110" y="50" font-size="9" fill="#334155" text-anchor="middle">원시 데이터 (D)</text>

    <!-- Bootstrap Samples -->
    <path d="M 80 57 L 40 75" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 110 57 L 110 75" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 140 57 L 180 75" stroke="#64748b" stroke-width="1.2"/>

    <rect x="15" y="75" width="50" height="20" rx="2" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="40" y="89" font-size="8.5" fill="#1e40af" text-anchor="middle">D1 (복원)</text>
    <rect x="85" y="75" width="50" height="20" rx="2" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="110" y="89" font-size="8.5" fill="#1e40af" text-anchor="middle">D2 (복원)</text>
    <rect x="155" y="75" width="50" height="20" rx="2" fill="#eff6ff" stroke="#93c5fd"/>
    <text x="180" y="89" font-size="8.5" fill="#1e40af" text-anchor="middle">D3 (복원)</text>

    <!-- Parallel Trees -->
    <path d="M 40 95 L 40 112" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 110 95 L 110 112" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 180 95 L 180 112" stroke="#64748b" stroke-width="1.2"/>

    <rect x="15" y="112" width="50" height="24" rx="3" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="40" y="128" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">Tree 1</text>
    <rect x="85" y="112" width="50" height="24" rx="3" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="110" y="128" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">Tree 2</text>
    <rect x="155" y="112" width="50" height="24" rx="3" fill="#dbeafe" stroke="#3b82f6"/>
    <text x="180" y="128" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">Tree 3</text>

    <text x="110" y="152" font-size="8.5" fill="#64748b" text-anchor="middle">병렬 독립 훈련 (Parallel)</text>

    <!-- Aggregation -->
    <path d="M 40 136 L 90 165" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 110 136 L 110 165" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 180 136 L 130 165" stroke="#64748b" stroke-width="1.2"/>

    <rect x="25" y="165" width="170" height="32" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="110" y="180" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">최종 집계: 다수결 / 평균</text>
    <text x="110" y="192" font-size="8" fill="#475569" text-anchor="middle">과적합 방지, 노이즈에 강건</text>
  </g>

  <!-- Right Side: Boosting -->
  <g transform="translate(270, 48)">
    <rect x="0" y="0" width="220" height="210" rx="6" fill="#ffffff" stroke="#ef4444" stroke-width="1.2"/>
    <rect x="0" y="0" width="220" height="26" rx="6" fill="#fef2f2"/>
    <text x="110" y="18" font-size="11" font-weight="bold" fill="#991b1b" text-anchor="middle">부스팅 (Boosting: 편향 감소)</text>

    <!-- Model 1 -->
    <rect x="15" y="42" width="55" height="30" rx="3" fill="#fee2e2" stroke="#ef4444"/>
    <text x="42" y="58" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">Model 1</text>
    <text x="42" y="69" font-size="7.5" fill="#b91c1c" text-anchor="middle">오차 식별</text>

    <!-- Arrow 1 -->
    <path d="M 70 57 L 85 57" stroke="#b91c1c" stroke-width="1.5"/>

    <!-- Model 2 -->
    <rect x="85" y="42" width="55" height="30" rx="3" fill="#fee2e2" stroke="#ef4444"/>
    <text x="112" y="58" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">Model 2</text>
    <text x="112" y="69" font-size="7.5" fill="#b91c1c" text-anchor="middle">오답 가중</text>

    <!-- Arrow 2 -->
    <path d="M 140 57 L 155 57" stroke="#b91c1c" stroke-width="1.5"/>

    <!-- Model 3 -->
    <rect x="155" y="42" width="50" height="30" rx="3" fill="#fee2e2" stroke="#ef4444"/>
    <text x="180" y="58" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">Model 3</text>
    <text x="180" y="69" font-size="7.5" fill="#b91c1c" text-anchor="middle">잔차 적합</text>

    <text x="110" y="92" font-size="8.5" fill="#64748b" text-anchor="middle">순차 직렬 보정 (Sequential)</text>

    <!-- Weights α -->
    <text x="42" y="115" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">w₁</text>
    <text x="112" y="115" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">w₂</text>
    <text x="180" y="115" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">w₃</text>

    <path d="M 42 120 L 95 165" stroke="#ef4444" stroke-width="1.2"/>
    <path d="M 112 120 L 112 165" stroke="#ef4444" stroke-width="1.2"/>
    <path d="M 180 120 L 125 165" stroke="#ef4444" stroke-width="1.2"/>

    <!-- Final Weighted Sum -->
    <rect x="25" y="165" width="170" height="32" rx="4" fill="#fef2f2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="110" y="180" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">최종 예측: F(x) = Σ α_m · h_m(x)</text>
    <text x="110" y="192" font-size="8" fill="#475569" text-anchor="middle">예측력 극대화, 과적합 주의</text>
  </g>
</svg>
</div>

- 본질: **복수의 약한 학습기(Weak Learner)를 결합하여 단일 모델이 갖는 높은 편향(과소적합) 또는 높은 분산(과적합)의 한계를 극복하고, 모델의 일반화 예측 성능(Generalization Performance)을 극대화하는 집단 지성 기반 머신러닝 기법**
- 암기: `약-부-병-다` (배깅: 약한 학습기, 부트스트랩 복원추출, 병렬 독립 학습, 다수결 취합) / `순-가-잔-결` (부스팅: 순차 학습, 오차 가중치 갱신, 잔차 적합, 가중 선형 결합)
- 판단축:
  - **배깅(Bagging - Random Forest)**: 서로 다른 표본으로 학습한 독립 모델들의 결과를 평균화하여 **분산(Variance)을 감소**시킴 $\rightarrow$ 노이즈에 강건, 과적합 방지 최적
  - **부스팅(Boosting - XGBoost, LightGBM, CatBoost)**: 이전 모델이 틀린 오답 샘플을 다음 모델이 집중 보정하여 **편향(Bias)을 감소**시킴 $\rightarrow$ 복잡한 비선형 경계 적합 최적, 노이즈에 민감
- 주의: 부스팅 계열은 학습 데이터의 이상치(Outlier)까지 외워버려 과적합(Overfitting)될 위험이 크므로, 최대 깊이(`max_depth`) 제한, 학습률(`learning_rate`) 축소, 조기 종료(`early_stopping`) 등 규제(Regularization) 하이퍼파라미터 튜닝이 필수적임
---

## 1교시 예상문제 (10점)

> 앙상블 학습 (Ensemble Learning) 및 배깅(Bagging)과 부스팅(Boosting)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 앙상블 학습(Ensemble Learning)의 개념 및 목적

- **개념**: 복수의 약한 학습기(Weak Learner)를 결합하여 단일 강한 학습기(Strong Learner)를 도출하는 집단 지성 기반 머신러닝 기법
- **목적**: 단일 모델의 편향(과소적합) 또는 분산(과적합)을 줄여 일반화 오차 최소화 ($\text{Error} = \text{Bias}^2 + \text{Variance} + \epsilon$)

### 2. 배깅(Bagging)과 부스팅(Boosting)의 메커니즘 비교

| 비교 항목 | 배깅 (Bagging) | 부스팅 (Boosting) |
|:---|:---|:---|
| **훈련 방식** | 병렬 독립 학습 (Parallel) | 순차 가중 보정 (Sequential) |
| **오차 제어** | **분산(Variance) 감소** | **편향(Bias) 감소** |
| **표본 추출** | 복원추출 (Bootstrap, OOB 36.8%) | 전체 데이터 사용 + 오답 샘플 가중치 상향 |
| **이상치 민감도** | 둔감 (다수결 취합으로 노이즈에 강건) | 극도로 민감 (이상치 잔차 학습 시 과적합 위험) |
| **대표 모델** | Random Forest, Extra Trees | XGBoost, LightGBM, CatBoost |

### 3. 실무 아키텍처 적용 및 튜닝 제언

- **모델 선택**: 결측치와 노이즈가 많은 원천 데이터는 배깅 우선 적용, 정제된 테이블 데이터 성능 극대화에는 부스팅 선별 적용
- **과적합 방어**: 부스팅 적용 시 `learning_rate` 축소(0.01~0.05), 트리 깊이 제한(`max_depth` 3~6) 및 `early_stopping` 설정 필수
---

### 핵심 관계

| 비교 항목 | 배깅 (Bagging) | 부스팅 (Boosting) |
|:---|:---|:---|
| **기본 동작 방식** | 부트스트랩 표본을 추출하여 복수의 모델을 **병렬 독립 훈련** | 이전 모델의 오차/잔차를 반영하여 모델을 **순차적으로 직렬 훈련** |
| **편향-분산 타깃** | **분산(Variance) 축소** (개별 트리의 과적합 상쇄) | **편향(Bias) 축소** (기저 모델의 과소적합 해결) |
| **학습 데이터셋** | 원본에서 무작위 복원 추출된 부분 데이터셋 | 모든 트리가 전체 데이터셋을 사용하되 샘플/잔차 가중치 변경 |
| **이상치(Outlier) 영향** | 다수결 평균으로 희석되므로 **이상치에 강건(Robust)** | 틀린 이상치에 가중치를 집중하여 **과적합 위험 매우 높음** |
| **연산 병렬화** | **완전 병렬화 가능** (GPU/멀티코어 분산 학습 용이) | **원칙적으로 직렬** (트리 내 노드 분할 단계에서만 부분 병렬) |
| **튜닝 민감도** | 하이퍼파라미터에 덜 민감 (기본값도 준수) | 하이퍼파라미터(`learning_rate`, `depth`)에 극도로 민감 |
| **대표 알고리즘** | Random Forest, Extra Trees | XGBoost, LightGBM, CatBoost, AdaBoost |

---

## 2~4교시 예상문제 (25점)

> 머신러닝에서 예측 성능을 극대화하기 위해 널리 사용되는 앙상블 학습(Ensemble Learning)의 개념과 필요성을 설명하고, 대표적 접근법인 배깅(Bagging)과 부스팅(Boosting)의 동작 메커니즘, 편향-분산 트레이드오프 관점의 차이점 및 발전 모델(Random Forest, XGBoost, LightGBM)을 비교하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 단일 모델의 한계를 극복하는 앙상블 학습(Ensemble Learning) 개요

#### 한줄 요약: 복수의 약한 학습기를 결합하여 일반화 오차(Generalization Error)를 최소화하는 머신러닝 기법

- **단일 학습기(Single Estimator)의 구조적 한계**:
  - 단일 결정 트리(Decision Tree)는 깊이가 깊어지면 학습 데이터에 지나치게 특화되어 과적합(High Variance)이 발생하고, 깊이가 얕으면 데이터를 충분히 표현하지 못해 과소적합(High Bias)에 빠짐
  - 실세계의 복잡하고 노이즈가 많은 정형 데이터를 단일 모델로 완벽히 분류하는 것은 이론적으로 불가능에 가까움
- **앙상블 학습의 정의 및 철학**:
  - 여러 개의 약한 학습기(Weak Learner, 무작위 추측보다 조금 나은 성능을 보이는 기저 모델)를 결합하여 훨씬 강력한 하나의 강한 학습기(Strong Learner)를 구축하는 알고리즘
- **편향-분산 트레이드오프(Bias-Variance Tradeoff) 관점의 오차 분해**:
  $$\text{Expected Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$$
  - **배깅**: 분산($\text{Variance}$)을 낮추는 방향으로 오차 감소
  - **부스팅**: 편향($\text{Bias}$)을 낮추는 방향으로 오차 감소

### Ⅱ. 배깅 (Bagging, Bootstrap Aggregating) 메커니즘

#### 한줄 요약: 부트스트랩 표본 추출과 병렬 독립 학습을 거쳐 다수결 투표로 분산을 축소하는 앙상블

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 115" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="95" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">배깅의 3단계 파이프라인 (부트스트랩 $\to$ 병렬학습 $\to$ 집계)</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="145" height="50" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="72" y="18" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 부트스트랩 (Bootstrap)</text>
    <text x="72" y="35" font-size="8.5" fill="#475569" text-anchor="middle">N개 복원 추출 (OOB 36.8%)</text>

    <path d="M 148 25 L 168 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="170" y="0" width="145" height="50" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="242" y="18" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">2. 병렬 독립 학습</text>
    <text x="242" y="35" font-size="8.5" fill="#475569" text-anchor="middle">B개 독립 트리 분산 훈련</text>

    <path d="M 318 25 L 338 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="340" y="0" width="135" height="50" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="407" y="18" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 집계 (Aggregation)</text>
    <text x="407" y="35" font-size="8.5" fill="#475569" text-anchor="middle">Hard/Soft 투표 및 평균</text>
  </g>
</svg>
</div>

### 1. 부트스트랩(Bootstrap)의 통계적 특성
- 원본 데이터가 $N$개일 때, 복원 추출로 $N$개를 뽑을 때 특정 데이터가 한 번도 선택되지 않을 확률:
  $$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = \frac{1}{e} \approx 0.368 \quad (36.8\%)$$
- 이 선택되지 않은 36.8%의 데이터를 **OOB(Out-Of-Bag)** 데이터라고 부르며, 별도의 검증 세트 없이 모델의 일반화 성능을 자체 검증하는 데 활용함

### 2. 대표 구현체: 랜덤 포레스트 (Random Forest)
- 배깅의 기본 구조에 **'피처 무작위성(Feature Randomness)'**을 추가한 모델
- 각 노드를 분할할 때 전체 $D$개의 속성 중 무작위로 $d = \sqrt{D}$ (분류) 또는 $d = D/3$ (회귀)개의 특성만 선택하여 최적 분할을 수행
- 트리 간의 상관계수(Correlation)를 낮춤으로써 앙상블의 분산 감소 효과를 극대화함

### Ⅲ. 부스팅 (Boosting) 메커니즘

#### 한줄 요약: 앞선 모델의 예측 오차를 분석하여 가중치를 갱신하거나 잔차를 순차적으로 적합하는 편향 축소 앙상블

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 115" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="95" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">부스팅 알고리즘 진화 계보</text>

  <g transform="translate(25, 42)">
    <!-- AdaBoost -->
    <rect x="0" y="0" width="80" height="48" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="40" y="20" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">AdaBoost</text>
    <text x="40" y="35" font-size="8" fill="#7f1d1d" text-anchor="middle">오차 가중치</text>

    <path d="M 82 24 L 98 24" stroke="#64748b" stroke-width="1.5"/>

    <!-- GBM -->
    <rect x="100" y="0" width="80" height="48" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="140" y="20" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">GBM</text>
    <text x="140" y="35" font-size="8" fill="#7f1d1d" text-anchor="middle">잔차 적합</text>

    <path d="M 182 24 L 198 24" stroke="#64748b" stroke-width="1.5"/>

    <!-- XGBoost -->
    <rect x="200" y="0" width="85" height="48" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="242" y="20" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">XGBoost</text>
    <text x="242" y="35" font-size="8" fill="#7f1d1d" text-anchor="middle">2차 테일러/정규화</text>

    <path d="M 287 24 L 303 24" stroke="#64748b" stroke-width="1.5"/>

    <!-- LightGBM -->
    <rect x="305" y="0" width="85" height="48" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="347" y="20" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">LightGBM</text>
    <text x="347" y="35" font-size="8" fill="#7f1d1d" text-anchor="middle">리프중심 분할</text>

    <path d="M 392 24 L 408 24" stroke="#64748b" stroke-width="1.5"/>

    <!-- CatBoost -->
    <rect x="410" y="0" width="70" height="48" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="445" y="20" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">CatBoost</text>
    <text x="445" y="35" font-size="8" fill="#7f1d1d" text-anchor="middle">범주형 특화</text>
  </g>
</svg>
</div>

### 1. 그래디언트 부스팅(GBM)의 잔차(Residual) 학습 원리
- 모델 $m-1$까지의 예측값을 $F_{m-1}(x)$라고 할 때, 손실 함수 $L(y, F(x))$를 최소화하기 위해 새로운 모델 $h_m(x)$는 **음의 그래디언트(Pseudo-residual)**를 타깃으로 삼아 학습:
  $$r_{im} = -\left[ \frac{\partial L(y_i, F(x_i))}{\partial F(x_i)} \right]_{F(x) = F_{m-1}(x)}$$
- 다음 모델을 학습률($\eta$)과 함께 선형 누적: $F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)$

### 2. 최신 부스팅 알고리즘 3대장 비교
- **XGBoost (Extreme Gradient Boosting)**:
  - 1차 미분(Gradient)과 2차 미분(Hessian)을 활용한 테일러 급수 최적화
  - 가중치 감소(L1/L2 Regularization)를 목적함수에 내장하여 과적합 완화
- **LightGBM**:
  - 균형 분할(Level-wise) 대신 최대 손실을 줄이는 **리프 중심 분할(Leaf-wise)** 채택으로 압도적인 속도와 높은 정확도 달성
  - 히스토그램 기반 빈(Bin) 변환과 GOSS(단면 경사 표본 추출)로 메모리 절감
- **CatBoost**:
  - 범주형 변수가 많은 테이블 데이터에 특화, 데이터 누수(Data Leakage)를 원천 차단하는 정렬된 타깃 인코딩(Ordered Target Statistics) 적용

### Ⅳ. 배깅 vs 부스팅 심층 비교

#### 한줄 요약: 병렬 독립 학습과 분산 축소를 지향하는 배깅, 순차 의존 학습과 편향 축소를 지향하는 부스팅의 종합 비교

| 비교 항목 | 배깅 (Bagging) | 부스팅 (Boosting) |
|:---|:---|:---|
| **기본 동작 방식** | 부트스트랩 표본을 추출하여 복수의 모델을 **병렬 독립 훈련** | 이전 모델의 오차/잔차를 반영하여 모델을 **순차적으로 직렬 훈련** |
| **편향-분산 타깃** | **분산(Variance) 축소** (개별 트리의 과적합 상쇄) | **편향(Bias) 축소** (기저 모델의 과소적합 해결) |
| **학습 데이터셋** | 원본에서 무작위 복원 추출된 부분 데이터셋 | 모든 트리가 전체 데이터셋을 사용하되 샘플/잔차 가중치 변경 |
| **이상치(Outlier) 영향** | 다수결 평균으로 희석되므로 **이상치에 강건(Robust)** | 틀린 이상치에 가중치를 집중하여 **과적합 위험 매우 높음** |
| **연산 병렬화** | **완전 병렬화 가능** (GPU/멀티코어 분산 학습 용이) | **원칙적으로 직렬** (트리 내 노드 분할 단계에서만 부분 병렬) |
| **튜닝 민감도** | 하이퍼파라미터에 덜 민감 (기본값도 준수) | 하이퍼파라미터(`learning_rate`, `depth`)에 극도로 민감 |
| **대표 알고리즘** | Random Forest, Extra Trees | XGBoost, LightGBM, CatBoost, AdaBoost |

### Ⅴ. 기타 앙상블 기법: 스태킹(Stacking) 및 보팅(Voting)

#### 한줄 요약: 단순 결과 취합인 보팅과 서로 다른 모델의 예측값을 메타 모델의 피처로 재학습하는 스태킹

- **보팅 (Voting)**:
  - 서로 다른 알고리즘(SVM, 로지스틱 회귀, 랜덤 포레스트 등)을 동일한 데이터로 학습시킨 뒤 다수결(Hard Voting) 또는 확률 평균(Soft Voting)으로 취합
- **스태킹 (Stacking)**:
  - 1단계 기본 모델들(Base Learners)의 예측 결과를 새로운 독립변수(Feature)로 구성
  - 2단계 메타 모델(Meta Learner)을 통해 최종 종속변수를 예측하는 다층 앙상블 (K-Fold 교차 검증을 통한 데이터 누수 방지 필수)

### Ⅵ. 실무 머신러닝 파이프라인에서의 모델 선정 및 튜닝 전략

#### 한줄 요약: 데이터 노이즈 수준, 피처 수, 연산 지연 한계에 따른 합리적 알고리즘 선택 및 과적합 방어

### 1. 실무 워크로드별 알고리즘 선택 가이드라인
- **데이터에 라벨 노이즈 및 이상치가 많은 경우**:
  - 부스팅 대신 **랜덤 포레스트(배깅)**를 기본 베이스라인으로 채택 (이상치에 흔들리지 않는 안정성 확보)
- **수백만 건 이상의 대용량 정형 테이블 데이터**:
  - 메모리 효율과 학습 속도가 가장 빠른 **LightGBM** 또는 **XGBoost Hist** 모드 채택
- **텍스트/카테고리 피처가 대다수인 전자상거래 추천/검색**:
  - 원-핫 인코딩 없이 고성능을 내는 **CatBoost** 적용

### 2. 부스팅 과적합 방지를 위한 4대 튜닝 규칙
1. **학습률 축소와 조기 종료**: `learning_rate`를 0.01~0.05 수준으로 낮추고, 검증 손실이 개선되지 않을 때 멈추는 `early_stopping_rounds` 설정
2. **트리 깊이(max_depth) 제한**: 부스팅 트리의 깊이를 3~6 수준의 얕은 트리로 고정하여 복잡도 억제
3. **서브샘플링(Subsample) 및 컬럼 샘플링(Colsample_bytree)**: 0.7~0.8 수준으로 설정하여 매 트리마다 데이터와 피처를 일부만 무작위 사용하여 다양성 확보
4. **정규화 파라미터 적용**: XGBoost의 `reg_alpha`(L1), `reg_lambda`(L2) 패널티 부여

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 캐글(Kaggle) 등 대회에서는 무조건 최신 부스팅(LightGBM, CatBoost)과 스태킹이 승리하지만, **운영 프로덕션 환경의 머신러닝 시스템에서는 서빙 지연시간(Latency)과 모델 유지보수성(XAI)**이 본질적인 승부처다. 트리 수천 개가 얽힌 부스팅은 10ms SLA를 맞추기 어렵고 과적합 위험이 크다. 노이즈가 많은 초기 데이터에는 랜덤 포레스트를 베이스라인으로 깔고, 검증된 정제 파이프라인 위에서 정규화 파라미터(L1/L2)를 엄격히 제한한 부스팅을 적용하는 것이 실무 아키텍처의 정답이다.

> **[나라면 이렇게 쓴다]**
> 1교시 10점형이라면 배깅(병렬/분산감소)과 부스팅(순차/편향감소)의 구조도를 대칭으로 배치하고 편향-분산 트레이드오프 수식을 명시하겠다. 25점형이라면 Treelite/ONNX를 활용한 트리 컴파일 서빙 가속 및 SHAP을 연계한 설명가능성(XAI) 확보 방안을 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 부스팅 앙상블의 무분별한 도입 시 학습 데이터 이상치 과적합 발생 및 온라인 서빙 시 트리 순회 레이턴시 급증
- **대응 (개선 방안)**: 노이즈 데이터는 배깅(랜덤 포레스트) 우선 채택, 부스팅 적용 시 `early_stopping`과 깊이 제한을 강제하고 Treelite 컴파일 서빙 체계 구축
- **검증 (검증 기준)**: 검증 데이터와 테스트 데이터 간 오차 격차 5% 이내 유지, 온라인 추론 지연시간 10ms 이내 준수, SHAP 기반 기여도 해석 검증
- **효과 (실행 효과)**: 과적합 방지를 통한 실무 일반화 정확도 15% 향상, 모델 추론 응답 속도 10배 가속 및 규제 기관 대응 투명성 확보

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">단일 모델 과적합/과소적합 및 부스팅 도입 시 서빙 레이턴시 병목</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">데이터 특성별 배깅/부스팅 선별 + Treelite C 컴파일 서빙 가속</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">Train-Test 오차 격차 &le; 5%, 추론 응답 &le; 10ms, SHAP XAI 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">일반화 예측 성능 15% 향상, 서빙 레이턴시 10배 단축 및 투명성 확보</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제126회 1교시 (머신러닝 앙상블 기법 중 배깅과 부스팅 비교)
  - 컴퓨터시스템응용기술사 제120회 1교시 (앙상블 학습의 개념 및 랜덤 포레스트)
  - 정보관리기술사 제115회 2교시 (머신러닝의 편향-분산 트레이드오프와 앙상블 기법)
- **표준 및 검증 출처**:
  - Leo Breiman (1996), "Bagging Predictors", *Machine Learning*
  - Jerome H. Friedman (2001), "Greedy Function Approximation: A Gradient Boosting Machine", *Annals of Statistics*
  - Tianqi Chen & Carlos Guestrin (2016), "XGBoost: A Scalable Tree Boosting System", *ACM KDD*
---

## 연결 토픽

- [038. 편향 (Bias)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/038_bias.md)
- [043. 데이터마이닝 (Data Mining)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/043_data_mining.md)
- [068. 잭나이프·부트스트랩 (Jackknife & Bootstrap)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/068_jackknife_bootstrap.md)
