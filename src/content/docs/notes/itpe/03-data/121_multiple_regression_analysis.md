---
title: "다중회귀분석"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 다변량 인과관계 모델링의 표준, 다중회귀분석 개요

### 가. 다중회귀분석(Multiple Regression Analysis)의 정의
- **다중회귀분석** : 하나의 연속형 **종속변수** (반응변수, $Y$)의 변화를 설명하고 예측하기 위해, 두 개 이상의 **독립변수** (설명변수, $X_1, X_2, \dots, X_k$)들의 선형 결합으로 관계성을 모델링하는 대표적인 **지도 학습** 통계 기법.

### 나. 다중 선형 회귀 모형의 수식적 정의
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_k X_k + \epsilon$$
($\beta_0$는 절편, $\beta_j$는 편회귀계수, $\epsilon$은 오차항 $\epsilon \sim N(0, \sigma^2)$).

---

## Ⅱ. 다중회귀분석의 4대 기본 가정 및 OLS 추정

### 가. 오차항($\epsilon$)에 대한 4대 핵심 가정

```text
[ 회귀분석 4대 기본 가정 검증 ]
1. 선형성 (Linearity)   : 종속변수와 독립변수 간의 관계가 선형적이어야 함 (산점도 확인)
2. 독립성 (Independence): 오차항 간에 자기상관이 없어야 함 (더빈-왓슨 d approx 2)
3. 등분산성 (Homoscedasticity): 독립변수 값에 관계없이 오차항의 분산이 일정해야 함 (잔차도)
4. 정규성 (Normality)   : 오차항은 평균이 0인 정규분포를 따라야 함 (Q-Q Plot, Shapiro-Wilk)
```

### 나. 최소제곱법(OLS, Ordinary Least Squares)에 의한 행렬 추정
- 잔차 제곱합($SSE$, Sum of Squared Errors, $e^T e$)을 최소화하는 회귀계수 벡터 $\hat{\beta}$의 해:
  $$\hat{\beta} = (X^T X)^{-1} X^T Y$$
- 만약 독립변수 간 **다중공선성** 이 존재하면 $X^T X$의 행렬식(Determinant)이 0에 가까워져 역행렬 계산 시 회귀계수 분산이 폭발함.

---

## Ⅲ. 모델 적합도 평가 지표 및 변수 선택 방법

### 가. 결정계수($R^2$) vs 수정된 결정계수(Adjusted $R^2$)

```text
[ 결정계수의 함정과 수정 결정계수 ]
- R^2 (결정계수) : 총 변동(SST) 중 회귀선에 의해 설명되는 변동(SSR)의 비율
                   * 치명적 약점: 무의미한 쓰레기 변수를 계속 추가해도 R^2은 무조건 증가함!
- Adj-R^2        : 변수 개수(k)에 대한 페널티를 부여하여 불필요한 변수 추가 시 오히려 감소!
                   Adj-R^2 = 1 - [ (n - 1) / (n - k - 1) ] * (1 - R^2)
```

### 나. 자동 변수 선택법(Stepwise Selection) 비교
- **전진 선택법 (Forward Selection)** : 절편만 있는 모델에서 $F$-통계량이 가장 유의미한 변수를 하나씩 추가.
- **후진 소거법 (Backward Elimination)** : 모든 변수를 포함한 상태에서 가장 기여도가 낮은 변수를 하나씩 제거.
- **단계적 방법 (Stepwise)** : 전진 선택과 후진 소거를 번갈아 수행하여 최적 변수 서브셋 탐색.

---

## Ⅳ. 다중회귀분석의 주요 한계점 및 해결 방안

- 독립변수 간 다중공선성(Multicollinearity)에 따른 회귀계수 추정 왜곡 :
  - 한계점 : 설명변수들 사이에 강한 선형 상관관계가 존재할 경우 최소자승법(OLS)의 분산이 비정상적으로 커져 유의미한 변수가 탈락하거나 부호가 역전되는 현상 발생.
  - 해결 방안 : **VIF** (Variance Inflation Factor, 분산팽창지수) 진단을 통한 변수 제거, **주성분 회귀** (PCR, Principal Component Regression) 적용, **L1/L2 규제** (Ridge, Lasso, ElasticNet)를 통한 계수 안정화.
- 고전적 4대 가정(선형성, 독립성, 등분산성, 정규성) 위반에 따른 추론 무력화 :
  - 한계점 : 잔차의 이분산성(Heteroscedasticity)이나 자기상관(Autocorrelation)이 존재할 경우 표준오차가 과소평가되어 가설검정 신뢰도 상실.
  - 해결 방안 : 브루쉬-패건(Breusch-Pagan) 및 더빈-왓슨(Durbin-Watson) 검정 수행, **이분산 강건 표준오차** (White Robust SE) 사용, 종속변수 로그/Box-Cox 변환.
- **과적합** (Overfitting) 및 이상치(Outlier)에 대한 OLS 추정의 민감성 :
  - 한계점 : 변수를 과다 추가할 경우 결정계수($R^2$)는 증가하나 미학습 데이터에 대한 예측 오차가 급증하고, 소수의 지렛대 점(Leverage Point)이 전체 회귀선을 왜곡.
  - 해결 방안 : 수정 결정계수(Adjusted $R^2$) 및 AIC(Akaike Information Criterion)/BIC(Bayesian Information Criterion) 기반 변수 선택(Stepwise Selection), **쿡의 거리** (Cook's Distance) 기반 이상치 진단 및 로버스트 회귀(RANSAC, Random Sample Consensus; Huber Loss) 적용.

## Ⅴ. 엔터프라이즈 데이터 사이언스 실무 제언

- **편회귀계수** (Partial Regression Coefficient)의 해석 유의 : $\beta_j$는 "다른 모든 독립변수들이 고정되어 있을 때(ceteris paribus), $X_j$가 1단위 증가함에 따른 $Y$의 평균 변화량"을 의미하므로, 변수 간 **상호작용** (Interaction Term)이 의심될 때는 교차곱 항($X_1 \times X_2$)을 모델에 명시적으로 투입해야 함.
- 이상치 및 **영향점** (Influence Point) 진단 : 단 1개의 왜곡된 레코드가 회귀선 전체의 기울기를 뒤흔들 수 있으므로, 쿡의 거리(Cook's Distance $> 0.5$)와 레버리지(Leverage) 통계량을 파이프라인에서 자동 계산하여 이상 영향점을 선제 제거할 것을 제언함.
