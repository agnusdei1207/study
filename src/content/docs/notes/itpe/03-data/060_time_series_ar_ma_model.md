---
title: "시계열 AR·MA 모델"
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

## Ⅰ. 고전 시계열 분석의 근간, AR 및 MA 모델의 개요

### 가. AR·MA 시계열 모델의 정의
- 시간에 따라 순차적으로 관측된 시계열 데이터의 자기상관성(Autocorrelation)을 수학적으로 모델링하여 미래 값을 예측하는 고전 통계적 시계열 분석 기법.
- **AR (자기회귀)** : 과거 자신의 관측값들의 선형 결합으로 현재 값을 설명.
- **MA (이동평균)** : 과거에 발생한 무작위 백색잡음(오차항)들의 선형 결합으로 현재 값을 설명.

### 나. 시계열 정상성(Stationarity)의 전제 조건
- AR 및 MA 모델을 적용하기 위해서는 시계열이 **약정상성(Weak Stationarity)** 을 만족해야 함:
  1. 시간에 무관하게 **평균이 일정** ($E[X_t] = \mu$).
  2. 시간에 무관하게 **분산이 일정** ($Var(X_t) = \sigma^2$).
  3. 공분산은 시점 $t$가 아닌 오직 **시차(Lag, $k$)에만 의존** ($Cov(X_t, X_{t+k}) = \gamma_k$).

---

## Ⅱ. AR, MA 및 결합 모델(ARMA, ARIMA)의 수학적 원리

### 가. 모델별 수식 정의 및 파라미터 의미

```text
[ AR vs MA 모델 수식 구조 ]
- AR(p) 모델 : X_t = c + phi_1 X_{t-1} + phi_2 X_{t-2} + ... + phi_p X_{t-p} + epsilon_t
  (현재 값은 과거 p개 시점의 자기 자신 값들과 백색잡음의 합)

- MA(q) 모델 : X_t = mu + epsilon_t + 	heta_1 epsilon_{t-1} + 	heta_2 epsilon_{t-2} + ... + 	heta_q epsilon_{t-q}
  (현재 값은 과거 q개 시점에 발생한 예측 오차(Shock)들의 충격 흡수 합)
```

### 나. 자기상관함수(ACF)와 편자기상관함수(PACF)를 통한 차수 결정

```text
[ ACF와 PACF 패턴에 따른 차수(p, q) 식별 매트릭스 ]
모델 유형         ACF (자기상관함수)             PACF (편자기상관함수)
------------------------------------------------------------------------
AR(p)             지수적 감소 또는 감쇠 진동      시차 p 이후 급격히 절단 (Cut-off at p)
MA(q)             시차 q 이후 급격히 절단         지수적 감소 또는 감쇠 진동 (Cut-off at q)
ARMA(p, q)        지수적 감소 (둘 다 절단 없음)    지수적 감소 (둘 다 절단 없음)
```

### 다. ARIMA(p, d, q)로의 확장
- 비정상(Non-stationary) 시계열을 $d$번 **차분(Differencing)** 하여 정상 시계열로 변환한 후, $ARMA(p, q)$ 모델을 적용하는 통합 모델:
  $$\Phi(B)(1 - B)^d X_t = \Theta(B) \epsilon_t$$

---

## Ⅲ. 시계열 모델의 적합도 평가 및 진단

### 가. 잔차 진단 (Residual Diagnostics)
- 모델 적합 후 잔차(Residual)는 어떠한 자기상관도 남아 있지 않은 **백색잡음(White Noise)** 이어야 함 $\rightarrow$ **융-박스 검정(Ljung-Box Test)** 을 통해 $p$-value $> 0.05$인지 검증.

### 나. 정보 기준(Information Criteria)을 통한 최적 모델 선택
- **AIC (Akaike Information Criterion)** 및 **BIC (Bayesian Information Criterion)** : 모델의 설명력(가능도)에 파라미터 개수에 대한 페널티를 부과하여 과적합을 방지하고 가장 작은 AIC/BIC 값을 갖는 차수 조합을 채택.

---

## Ⅳ. 데이터 사이언스 및 시스템 운영 실무 제언

- **딥러닝 시계열 모델과의 앙상블** : 현대 시계열 예측에서 LSTM이나 PatchTST, TFT 등 복잡한 딥러닝 모델이 주목받고 있으나, 선형적 추세와 명확한 주기성을 가진 데이터에서는 ARIMA가 훨씬 가볍고 뛰어난 일반화 성능을 보이므로, ARIMA(선형 성분) + 딥러닝(비선형 잔차 학습) 하이브리드 파이프라인을 설계할 것.
- **실시간 드리프트 대응** : 시계열 모델은 계절성 변화나 외부 충격(코로나, 금융 위기 등 구조적 변화)에 취약하므로, 고정된 모델을 영구 사용하지 말고 주기적으로 파라미터를 자동 재학습(Rolling-window Retraining)시키는 MLOps 파이프라인을 구축할 것을 제언함.
