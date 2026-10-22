---
title: "다중회귀분석"
author: "agnusdei1207"
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

## 연관 키워드

**다중회귀분석(Multiple Regression)**, **OLS(Ordinary Least Squares)**, **VIF**, **R²/Adjusted R²**, **다중공선성**, **Stepwise**, **AIC/BIC**

## Ⅰ. 개요

- 핵심 요약 : **다중회귀분석**은 2개 이상 독립변수의 선형 결합으로 종속변수를 모델링하는 지도학습 기법.
- 목적 : 다변량 인과관계 설명 및 예측.
- 배경 : 단순회귀는 1개 변수만 반영 → 다변량 모델 필요.
- 특징 : OLS 추정, 4대 가정, 변수 선택, 적합도 평가.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **다변량 모델링·OLS·가정 검증**으로 인과관계 정량화.
- **다변량** : 여러 설명변수 동시 반영.
- **OLS** : 잔차 제곱합 최소화로 계수 추정.
- **가정 검증** : 선형성·독립성·등분산성·정규성.
- **적합도** : R², Adjusted R², AIC/BIC.
- **변수 선택** : Forward/Backward/Stepwise.

## Ⅲ. 모델 추정 흐름

- 핵심 요약 : **가정 확인 → OLS 추정 → 적합도 평가 → 변수 선택 → 진단**.
- 회귀식 : $Y = \beta_0 + \beta_1 X_1 + \dots + \beta_k X_k + \epsilon$.
- OLS : $\hat\beta = (X^T X)^{-1} X^T Y$.
- 4대 가정 : 선형성, 독립성, 등분산성, 정규성.

```text
[ 회귀분석 4대 가정 ]

1. 선형성       : X-Y 관계 선형 (산점도)
2. 독립성       : 오차 자기상관 없음 (DW ~ 2)
3. 등분산성     : 오차 분산 일정 (잔차도)
4. 정규성       : 오차 정규분포 (Q-Q, Shapiro-Wilk)
```

```text
[ 변수 선택법 ]

Forward  : 유의 변수 하나씩 추가
Backward : 비유의 변수 하나씩 제거
Stepwise : 전진·후진 번갈아 수행
```

## Ⅳ. 적합도·변수 선택 비교

- 핵심 요약 : **R² vs Adjusted R²** 및 **변수 선택법** 비교.

| 항목 | R² | Adjusted R² |
|---|---|---|
| 정의 | 설명 변동 비율 | 변수 수 페널티 반영 |
| 변수 추가 | 항상 증가 | 무의미 변수 시 감소 |
| 용도 | 설명력 | 모델 비교·선택 |

- 변수 선택 : Forward/Backward/Stepwise, AIC/BIC 기준.
- 다중공선성 진단 : VIF (10 이상 제거).

## Ⅴ. 한계와 방안

- 핵심 요약 : **다중공선성·가정 위반·과적합**을 VIF·강건 표준오차·규제로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 다중공선성 | 변수 간 강한 상관으로 계수 분산 폭발 | VIF 진단, PCR, L1/L2 규제 | VIF |
| 가정 위반 | 이분산·자기상관으로 표준오차 왜곡 | Breusch-Pagan, White Robust SE, 변환 | DW, BP p값 |
| 과적합 | 변수 과다로 미학습 예측 오차 급증 | Adjusted R², AIC/BIC, Cook's Distance | CV 오차 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **편회귀계수 해석·이상치 진단·상호작용** 고려.
- 편회귀계수 : 다른 변수 고정 시 1단위 변화의 평균 변화 (ceteris paribus).
- 상호작용 : 의심 시 교차곱 항 ($X_1 \times X_2$) 투입.
- 이상치 : Cook's Distance > 0.5, Leverage 진단, RANSAC/Huber.

## Ⅶ. 결론

- 핵심 요약 : 다중회귀분석은 **다변량 인과관계 모델링**의 기본으로 가정 검증·다중공선성 대응이 핵심.
- 답안에는 4대 가정, OLS, VIF, 적합도, 한계·대응을 연결.
- 참고 : [scikit-learn LinearRegression](https://scikit-learn.org/stable/modules/linear_model.html).