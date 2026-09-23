---
sidebar:
  order: 121
  label: "121. 다중회귀분석 (Multiple Regression Analysis)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 121
title: "다중회귀분석(Multiple Regression Analysis)의 모형 추정과 다중공선성 진단 및 정규화 해법"
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "121"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>다중회귀분석</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Independent Variables Group -->
  <rect x="20" y="25" width="160" height="150" rx="8" fill="#3b82f6" fill-opacity="0.08" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="100" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">독립변수군 (X)</text>
  <rect x="35" y="60" width="130" height="26" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="100" y="77" text-anchor="middle" font-size="11" fill="#1e293b">X1 (마케팅 예산)</text>
  <rect x="35" y="95" width="130" height="26" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="100" y="112" text-anchor="middle" font-size="11" fill="#1e293b">X2 (할인율)</text>
  <rect x="35" y="130" width="130" height="26" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="100" y="147" text-anchor="middle" font-size="11" fill="#1e293b">X3 (매장 면적)</text>

  <!-- Coefficients & Path -->
  <path d="M 165 73 L 330 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow121)"/>
  <text x="240" y="78" font-size="10" font-weight="bold" fill="#2563eb">β1 (편회귀계수)</text>

  <path d="M 165 108 L 330 105" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow121)"/>
  <text x="240" y="103" font-size="10" font-weight="bold" fill="#2563eb">β2 (편회귀계수)</text>

  <path d="M 165 143 L 330 115" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow121)"/>
  <text x="240" y="135" font-size="10" font-weight="bold" fill="#2563eb">β3 (편회귀계수)</text>

  <!-- Dependent Variable -->
  <rect x="330" y="65" width="165" height="75" rx="8" fill="#10b981" fill-opacity="0.12" stroke="#10b981" stroke-width="1.5"/>
  <text x="412" y="90" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">종속변수 (Y)</text>
  <text x="412" y="110" text-anchor="middle" font-size="11" fill="#1e293b">총 매출액 + ε (오차)</text>
  <text x="412" y="128" text-anchor="middle" font-size="10" fill="#64748b">F-검정 / t-검정 유의성</text>

  <!-- Diagnosis Bottom -->
  <rect x="20" y="190" width="475" height="55" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="257" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">모형 신뢰성 진단: VIF &gt;= 10 (다중공선성) 판정 시 변수 정제</text>
  <text x="257" y="232" text-anchor="middle" font-size="10" fill="#78350f">수정된 R² 평가 · 잔차 4대 기본 가정(정규성·등분산성·독립성·선형성) 충족 필수</text>

  <defs>
    <marker id="arrow121" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **하나의 연속형 종속변수($Y$)의 변화를 두 개 이상의 독립변수($X_1, X_2, \dots, X_k$)들의 선형 결합으로 설명하고 예측하는 지도학습 통계 모형으로, 다른 독립변수들의 영향을 통제한 상태에서 특정 변수의 순수한 한계 기여도(편회귀계수 $\beta_k$)를 산출하는 분석 기법**
- 암기: `선-정-등-독` (4대 잔차 기본가정: 선형성, 정규성, 등분산성, 독립성) / `편-수-에-티` (편회귀계수, 수정된 결정계수 Adj $R^2$, F-검정 모형 유의성, t-검정 계수 유의성) / `공-브-릿-라` (다중공선성, VIF 10 이상, Ridge L2, Lasso L1)
- 판단축:
  - **단순회귀 vs 다중회귀**: 독립변수 1개 vs 2개 이상 (다차원 외생변수 통제 및 교란 요인 분리)
  - **결정계수($R^2$) vs 수정된 결정계수(Adjusted $R^2$)**: 변수 추가 시 맹목적 증가 vs 표본수와 변수 수 페널티 반영(과적합 방지)
  - **Ridge vs Lasso**: 독립변수 간 다중공선성 완화(가중치 축소) vs 불필요한 계수를 완전히 0으로 만들어 변수 선택(Feature Selection)
- 주의: 독립변수 간 상관관계가 높을 때 발생하는 **다중공선성(Multicollinearity)**을 방치하면, 회귀계수의 분산이 폭증하여 부호가 반대로 뒤집히거나 t-검정 결과가 왜곡되는 치명적 분석 오류 발생
---

## 1교시 예상문제 (10점)

> 다중회귀분석(Multiple Regression Analysis)의 모형 추정과 다중공선성 진단 및 정규화 해법의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 종속변수($Y$)의 변화를 2개 이상의 독립변수($X_k$) 선형 결합으로 설명하고, 외생변수를 통제한 순수 편회귀계수($\beta_k$)를 추정하는 지도학습 통계 모형 |
| **2. 4대 기본 가정** | 잔차의 **선형성**(Linearity), **정규성**(Normality), **등분산성**(Homoscedasticity), **독립성**(Independence, Durbin-Watson) |
| **3. 다중공선성 및 VIF** | - 독립변수 간 강한 상관성으로 계수 분산 폭증 및 부호 역전 유발<br/>- 판별: 분산팽창인수 $\text{VIF} = 1/(1-R^2) \ge 10$ 이상 시 공선성 확정 |
| **4. 해결 방안** | - VIF 10 이상 변수 제거 및 PCA 차원 축소<br/>- **Ridge(L2)** 계수 축소 또는 **Lasso(L1)** 불필요 변수 계수 0 축소 적용 |
---

### 핵심 관계

| 비교 항목 | OLS (최소자승법) | Ridge 회귀 (L2 정규화) | Lasso 회귀 (L1 정규화) | ElasticNet |
|:---|:---|:---|:---|:---|
| **페널티 항** | 없음 | $\lambda \sum_{j=1}^p \beta_j^2$ (L2 노름) | $\lambda \sum_{j=1}^p \|\beta_j\|$ (L1 노름) | $r \cdot \text{L1} + (1-r) \cdot \text{L2}$ |
| **목적 함수** | $\min \sum (Y_i - \hat{Y}_i)^2$ | $\text{RSS} + \lambda \|\beta\|_2^2$ | $\text{RSS} + \lambda \|\beta\|_1$ | RSS + 혼합 규제 페널티 |
| **계수 축소 방식** | 페널티 없이 잔차만 최소화 | 계수 크기를 0에 가깝게 축소 (절대 0은 안 됨) | **중요하지 않은 계수를 정확히 0으로 수렴** | L1과 L2의 장점 절충 |
| **변수 선택 기능** | 미지원 (모든 변수 유지) | 불가 (모든 변수 보존) | **자동 변수 선택 (Feature Selection)** | 상관 변수 그룹 단위 선택 |
| **적합한 상황** | 독립변수 간 상관이 없는 이상적 환경 | **다중공선성이 심하고 변수 간 크기가 고를 때** | **불필요한 설명변수가 많아 희소(Sparse) 모델 필요 시** | 변수 수가 샘플 수보다 많고 고상관인 경우 |

---

## 2~4교시 예상문제 (25점)

> 다중회귀분석(Multiple Regression Analysis)의 기본 가정 4가지와 회귀계수 추정 원리를 설명하고, 다중공선성(Multicollinearity)의 문제점과 판별 기준(VIF) 및 정규화 회귀(Ridge, Lasso)를 통한 해결 방안을 기술하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 복합 인과관계를 규명하는 다중회귀분석 개요

#### 한줄 요약: 다수의 독립변수를 동시에 투입하여 상호 교란 요인을 통제하고 종속변수에 미치는 순수한 개별 영향력을 분리 추정하는 통계 모형

- **배경**: 현실의 경제·경영·기술 현상은 단 하나의 원인으로 발생하지 않으며, 단일 변수만 분석할 경우 다른 외생변수의 영향이 혼재되어 잘못된 인과관계(심슨의 역설 등)를 도출할 위험 존재
- **정의**: 하나의 연속형 종속변수($Y$)와 둘 이상의 연속형/더미 독립변수($X_1, X_2, \dots, X_k$) 간의 관계를 최소자승법(OLS: Ordinary Least Squares)으로 모델링하는 통계적 분석 기법
- **수학적 모형 식**:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon$$

  - $Y$: 종속변수 (반응변수, 결과)
  - $\beta_0$: 절편 (모든 $X$가 0일 때의 $Y$ 기댓값)
  - $\beta_k$: **편회귀계수(Partial Regression Coefficient)**. 다른 모든 독립변수가 고정된 상태에서 $X_k$가 1단위 증가할 때 $Y$의 평균 변화량
  - $\epsilon$: 오차항 (모형으로 설명되지 않는 잔차, $\epsilon \sim N(0, \sigma^2)$)

### Ⅱ. 다중회귀분석의 4대 잔차 기본 가정

#### 한줄 요약: 가우스-마르코프 정리에 따라 OLS 추정량이 최량선형불편추정량(BLUE)이 되기 위한 잔차(Residual)의 4대 전제 조건

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="115" height="140" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="72" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 선형성</text>
  <text x="72" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Linearity</text>
  <text x="72" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">X와 Y 관계가</text>
  <text x="72" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">선형 결합 만족</text>
  <text x="72" y="135" text-anchor="middle" font-size="10" fill="#64748b">잔차 산점도 무패턴</text>

  <!-- Box 2 -->
  <rect x="140" y="20" width="115" height="140" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="197" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. 정규성</text>
  <text x="197" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Normality</text>
  <text x="197" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">오차항 ε가</text>
  <text x="197" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">정규분포를 따름</text>
  <text x="197" y="135" text-anchor="middle" font-size="10" fill="#64748b">Q-Q Plot / S-W 검정</text>

  <!-- Box 3 -->
  <rect x="265" y="20" width="115" height="140" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="322" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. 등분산성</text>
  <text x="322" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Homoscedasticity</text>
  <text x="322" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">X 수준과 무관히</text>
  <text x="322" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">오차 분산 일정</text>
  <text x="322" y="135" text-anchor="middle" font-size="10" fill="#64748b">B-P / White 검정</text>

  <!-- Box 4 -->
  <rect x="390" y="20" width="115" height="140" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="447" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">4. 독립성</text>
  <text x="447" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Independence</text>
  <text x="447" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">오차항 간의</text>
  <text x="447" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">자기상관 없음</text>
  <text x="447" y="135" text-anchor="middle" font-size="10" fill="#64748b">더빈-왓슨(d ≈ 2)</text>
</svg>
</div>

1. **선형성 (Linearity)**: 독립변수들의 변화에 따른 종속변수의 기대치가 선형적인 결합 형태여야 함 (잔차 산점도가 0을 중심으로 무작위 분포)
2. **정규성 (Normality)**: 오차항 $\epsilon$은 평균이 0이고 분산이 $\sigma^2$인 정규분포 $N(0, \sigma^2)$를 따라야 함 (Q-Q 플롯, 샤피로-윌크 검정으로 확인)
3. **등분산성 (Homoscedasticity)**: 모든 독립변수 값의 영역에서 오차항의 분산이 동일해야 함 (위배 시 가중최소자승법 WLS 또는 로그 변환 필요)
4. **독립성 (Independence)**: 어떤 관측치의 오차항도 다른 관측치의 오차항과 상관관계를 갖지 않아야 함 (시계열 데이터에서 더빈-왓슨 검정 $d \approx 2$ 만족 필수)

### Ⅲ. 모형의 적합도 평가와 통계적 유의성 검정

#### 한줄 요약: 전체 모형을 검정하는 F-검정과 수정된 $R^2$, 개별 계수를 검정하는 t-검정의 2중 평가 체계

1. **결정계수($R^2$) vs 수정된 결정계수(Adjusted $R^2$)**:
   - 일반 결정계수($R^2$): 총 변동 중 회귀모형이 설명하는 비율($SSR / SST$). 무의미한 독립변수를 계속 추가하기만 해도 $R^2$은 무조건 단조 증가하는 치명적 맹점 보유
   - **수정된 결정계수(Adjusted $R^2$)**: 표본 크기($n$)와 독립변수 개수($k$)를 반영하여 페널티를 부과한 지표로, 다중회귀의 실제 설명력 비교 시 필수 채택

$$\text{Adjusted } R^2 = 1 - \left[ \frac{(1 - R^2)(n - 1)}{n - k - 1} \right]$$

2. **모형 유의성 검정 (F-검정)**:
   - 귀무가설($H_0$): $\beta_1 = \beta_2 = \dots = \beta_k = 0$ (모든 독립변수가 무의미함)
   - 대립가설($H_1$): 적어도 하나의 회귀계수는 0이 아님
   - $p < 0.05$일 때 모형 전체가 통계적으로 유의하다고 판정하며, F-검정을 통과하지 못하면 개별 계수 해석은 무의미함
3. **개별 회귀계수 유의성 검정 (t-검정)**:
   - 귀무가설($H_0$): $\beta_j = 0$ (해당 변수는 종속변수에 영향을 주지 않음)
   - 검정통계량: $t = \frac{\hat{\beta}_j}{\text{SE}(\hat{\beta}_j)}$
   - $p < 0.05$일 때 해당 변수가 종속변수에 통계적으로 유의미한 영향력을 행사한다고 확증

### Ⅳ. 다중공선성(Multicollinearity)의 문제점과 VIF 판별

#### 한줄 요약: 독립변수 간의 강한 선형 상관성으로 인해 회귀계수의 분산이 팽창하고 추정치가 심각하게 왜곡되는 현상

1. **발생 원인과 주요 문제점**:
   - 원인: '전용면적'과 '공급면적', '키'와 '몸무게'처럼 독립변수들끼리 높은 상관성을 보일 때 발생
   - **문제점 1 (추정량 분산 폭증)**: 계수의 표준오차가 극단적으로 커져 실제 유의한 변수도 t-검정에서 불채택($p > 0.05$)되는 왜곡 발생
   - **문제점 2 (부호 역전 현상)**: 상식적으로 양(+)의 영향이어야 할 변수가 음(-)의 회귀계수로 추정되는 비논리적 결과 초래
   - **문제점 3 (모형 불안정)**: 표본 데이터가 조금만 바뀌어도 회귀계수 수치가 급변함
2. **다중공선성 판별 기준**:
   - **상관계수 행렬**: 독립변수 간 상관계수 $|r| \ge 0.8$ 이상이면 의심
   - **분산팽창인수 (VIF, Variance Inflation Factor)**:

$$\text{VIF}_j = \frac{1}{1 - R_j^2}$$

   - $R_j^2$: 변수 $X_j$를 종속변수로 두고 나머지 $k-1$개 독립변수들로 회귀분석했을 때의 결정계수
   - **판정 기준**:
     - $\text{VIF} < 5$: 다중공선성 문제 없음
     - $5 \le \text{VIF} < 10$: 주의 필요 (경미한 공선성)
     - **$\text{VIF} \ge 10$**: 심각한 다중공선성 존재 $\rightarrow$ 변수 제거, 차원 축소 또는 정규화 회귀 필수 적용

### Ⅴ. 다중공선성 극복을 위한 정규화 회귀분석(Regularization) 비교

#### 한줄 요약: 손실함수에 가중치 페널티를 부과하여 분산을 줄이고 예측 안정성을 높이는 Ridge, Lasso, ElasticNet

| 비교 항목 | OLS (최소자승법) | Ridge 회귀 (L2 정규화) | Lasso 회귀 (L1 정규화) | ElasticNet |
|:---|:---|:---|:---|:---|
| **페널티 항** | 없음 | $\lambda \sum_{j=1}^p \beta_j^2$ (L2 노름) | $\lambda \sum_{j=1}^p \|\beta_j\|$ (L1 노름) | $r \cdot \text{L1} + (1-r) \cdot \text{L2}$ |
| **목적 함수** | $\min \sum (Y_i - \hat{Y}_i)^2$ | $\text{RSS} + \lambda \|\beta\|_2^2$ | $\text{RSS} + \lambda \|\beta\|_1$ | RSS + 혼합 규제 페널티 |
| **계수 축소 방식** | 페널티 없이 잔차만 최소화 | 계수 크기를 0에 가깝게 축소 (절대 0은 안 됨) | **중요하지 않은 계수를 정확히 0으로 수렴** | L1과 L2의 장점 절충 |
| **변수 선택 기능** | 미지원 (모든 변수 유지) | 불가 (모든 변수 보존) | **자동 변수 선택 (Feature Selection)** | 상관 변수 그룹 단위 선택 |
| **적합한 상황** | 독립변수 간 상관이 없는 이상적 환경 | **다중공선성이 심하고 변수 간 크기가 고를 때** | **불필요한 설명변수가 많아 희소(Sparse) 모델 필요 시** | 변수 수가 샘플 수보다 많고 고상관인 경우 |

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 이상치 왜곡(Cook's Distance), 다중공선성 자동 제거 파이프라인, 과적합 방지

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **소수 이상치로 인한 기울기 왜곡** | 지렛대점(High Leverage Point)이나 외딴 이상치가 OLS 제곱합을 왜곡 | 쿡의 거리(**Cook's Distance > 1.0**) 또는 DFFITS로 영향점을 판별하여 결측/이상 처리하거나 Huber 로버스트 회귀 적용 |
| **다중공선성으로 인한 부호 역전** | 수십 개 지표를 무차별 투입하여 변수 간 다중공선성 발생 | VIF 기반 단계적 변수 제거(RFE)를 수행하거나 PCA(주성분분석)를 적용하여 직교 주성분으로 변환 후 회귀 적합 |
| **변수 과다로 인한 테스트 성능 폭락** | 학습 데이터에만 과적합(Overfitting)되어 실제 서빙 시 오차 급증 | K-Fold 교차 검증과 함께 Lasso 정규화($\lambda$ 튜닝)를 적용하여 복잡도 페널티 강제 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 머신러닝 시대에 딥러닝이나 XGBoost 같은 블랙박스 고성능 모델이 쏟아져 나오지만, 금융(신용평가), 의료, 법률, 공공 정책 영역에서 여전히 다중회귀분석이 독점적 지위를 누리는 이유는 **'설명 가능성(Explainability)'과 '편회귀계수의 한계 효과 해석력'** 때문이다.
> 하지만 실무 엔지니어들이 가장 많이 저지르는 실수는 "일단 모든 컬럼을 회귀식에 밀어 넣고 $R^2$이 높으면 성공으로 착각하는 것"이다.
> 다중공선성 진단(VIF)과 잔차의 4대 기본 가정을 검증하지 않은 다중회귀 모델은 완전히 가짜 인과관계를 양산하는 위험한 분석이다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "현대적 MLOps 파이프라인 내에서의 다중회귀 자동화 검증 체계"를 제언하겠다. 모델 학습 파이프라인에 VIF 자동 스크리닝(VIF $\ge 10$ 자동 탈락)과 Durbin-Watson 자기상관 검증을 CI/CD 파이프라인의 품질 게이트로 내재화하고, 고차원 데이터셋에 대해서는 Lasso/ElasticNet 기반의 Feature Store 정제 아키텍처를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 빅데이터 기반 예측 시스템에서 변수 간 복합 교란 요인을 통제하고 해석 가능한 모델을 구축하기 위해 다중회귀분석이 표준적으로 활용되어야 함.
- **대응**:
  1. **사전 VIF 파이프라인 구축**: 모델 학습 전 변수 간 상관행렬 및 VIF를 산출하여 10 이상의 변수는 주성분분석(PCA) 또는 삭제 처리.
  2. **정규화 기법 표준화**: 고차원 희소 데이터는 Lasso, 다중공선성이 존재하는 고밀도 데이터는 Ridge/ElasticNet을 하이퍼파라미터($\lambda$) 튜닝과 함께 도입.
  3. **잔차 4대 가정 자동 진단**: 모델 배포 전 Shapiro-Wilk, Breusch-Pagan, Durbin-Watson 검정을 자동 실행하는 통계 검증 게이트 구축.
- **검증**: Adjusted $R^2$ 개선율, F-검정 $p < 0.001$, VIF 전수 5 미만 유지 검증.
- **효과**: 회귀계수의 부호 왜곡 방지, 과적합 차단 및 비즈니스 의사결정의 설명 가능성 100% 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">다중공선성 방치로 계수 부호 역전, R² 맹신에 따른 과적합</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">VIF 진단, 잔차 4대 가정 검증, Lasso/Ridge 정규화 적용</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">VIF &lt; 5, F-검정 및 t-검정 유의성(p &lt; 0.05), 더빈-왓슨 d ≈ 2</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">해석 가능한 고신뢰 회귀 모델 도출 및 실무 예측 오차 최소화</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제124회 정보관리 2교시: 다중회귀분석(Multiple Regression Analysis)의 기본 가정과 다중공선성 판별 및 해결 방안
- **검증 출처**:
  - Gareth James et al., "An Introduction to Statistical Learning (ISLR 2nd Edition)", Springer
  - Douglas C. Montgomery et al., "Introduction to Linear Regression Analysis (6th Edition)", Wiley
---

## 연결 토픽

- 상위 토픽: [03-036 기술통계](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/036_descriptive_statistics.md)
- 연관 토픽: [03-004 다중공선성](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/004_multicollinearity.md), [03-089 로지스틱 회귀분석](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/089_logistic_regression.md), [03-086 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/086_t_test.md)
