---
title: "로지스틱 회귀"
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

## Ⅰ. 확률 기반 이진 분류의 초석, 로지스틱 회귀(Logistic Regression) 개요

### 가. 로지스틱 회귀의 정의
- **로지스틱 회귀** : 독립변수들의 선형 결합을 바탕으로 특정 사건이 발생할 확률($0 \le P(Y=1|X) \le 1$)을 추정하고, 이를 사전에 정의된 임계값(Threshold, 통상 0.5)과 비교하여 **이진 분류** (Binary Classification)를 수행하는 통계적·머신러닝 알고리즘.
- 선형 회귀(Linear Regression)의 종속변수가 $-\infty$에서 $+\infty$까지 발산하여 확률을 모델링할 수 없는 수학적 한계를 **시그모이드** (Sigmoid) 함수를 통해 극복함.

---

## Ⅱ. 로지스틱 회귀의 수학적 메커니즘: 승산비, 로짓, 시그모이드

### 가. 3단계 수학적 유도 과정

```text
[ 로지스틱 회귀 수학적 변환 흐름 ]
1. 승산 (Odds)     : P / (1 - P)            -> 성공 확률 / 실패 확률 (범위: 0 ~ infty)
                         |
                         v (자연로그 취함)
2. 로짓 (Logit)    : ln(P / (1 - P)) = w^T X + b  -> 범위를 (-infty ~ +infty)로 확장하여 선형 결합 매핑
                         |
                         v (P에 대해 역함수 정리)
3. 시그모이드 함수 : P = 1 / (1 + e^{-(w^T X + b)}) -> 선형 출력을 다시 (0 ~ 1) 확률값으로 압축!
```

### 나. 시그모이드(로지스틱) 함수의 그래프 및 수식
$$\sigma(z) = \frac{1}{1 + e^{-z}} \quad (z = w^T x + b)$$

```text
  sigma(z)
    1.0 |                    ************** (성공 확정)
        |                ***
    0.5 |--------------* (결정 경계 z=0)
        |           ***
    0.0 | ********** (실패 확정)
        +----------------------------------------> z (w^T x + b)
               -4   -2    0    2    4
```

---

## Ⅲ. 모델 학습 및 최적화: 교차 엔트로피 손실과 경사하강법

### 가. 이진 교차 엔트로피 손실 함수 (Binary Cross-Entropy Loss)
- 선형 회귀의 평균제곱오차(MSE, Mean Squared Error)를 로지스틱에 적용하면 비볼록(Non-convex) 함수가 되어 수많은 국소 최적점(Local Minima)에 갇힘 $\rightarrow$ **로그 우도** (Log-Likelihood)를 극대화 하는 볼록(Convex) 손실 함수 사용:
  $$\mathcal{L}(w) = -\frac{1}{n} \sum_{i=1}^n \left[ y_i \ln(\hat{y}_i) + (1 - y_i) \ln(1 - \hat{y}_i) \right]$$

### 나. 승산비(Odds Ratio)의 비즈니스 해석력
- 특정 독립변수 $X_j$가 1단위 증가할 때 성공 **승산** (Odds)이 몇 배 증가하는가를 나타내는 지표:
  $$Odds\;Ratio = e^{w_j}$$
- 금융 신용평가, 의료 질병 예측에서 "소득이 100만 원 증가할 때 대출 상환 성공 확률 승산이 $e^{0.3} = 1.35$배 증가한다"와 같은 강력한 **설명력** (Explainability) 제공.

---

## Ⅳ. 로지스틱 회귀의 주요 한계점 및 해결 방안

- 선형 결정 경계(Linear Decision Boundary)로 인한 비선형 관계 모델링 한계 :
  - 한계점 : 독립변수와 로짓(Logit) 간의 선형 관계를 가정하므로 XOR(Exclusive OR) 문제와 같은 비선형 피처 상호작용 및 복합 패턴 학습 불가.
  - 해결 방안 : 다항 피처(Polynomial Features) 생성 및 상호작용 항 추가, 커널 트릭 적용, 트리 기반 앙상블(XGBoost, LightGBM) 또는 심층 신경망 모델과의 결합.
- 다중공선성(Multicollinearity)에 따른 회귀계수 왜곡 및 과적합 :
  - 한계점 : 독립변수 간 강한 상관관계가 존재할 경우 계수 추정치의 분산이 급증하여 가중치 해석이 불가능해지고 모델 일반화 성능 저하.
  - 해결 방안 : VIF(Variance Inflation Factor, 분산팽창지수) 10 이상 변수 제거, L1/L2 규제(Ridge, Lasso, ElasticNet)를 통한 가중치 수축(Shrinkage) 및 피처 선택 자동화.
- 극심한 클래스 불균형(Class Imbalance) 환경에서의 다수 클래스 편향 :
  - 한계점 : 사기 탐지(FDS, Fraud Detection System)나 장애 예측 등 희귀 클래스(극소수) 데이터에서 다수 클래스로 편향 예측하여 재현율(Recall) 급락.
  - 해결 방안 : 언더샘플링/오버샘플링(SMOTE, Synthetic Minority Over-sampling Technique), 비용 민감 학습(Cost-sensitive Learning: 손실함수 클래스 가중치 부여), 결정 임계치(Threshold Tuning) 최적화.

## Ⅴ. 엔터프라이즈 분류 모델링 관점의 실무 제언

- 규제 회귀(L1/L2)를 통한 과적합 방지 : 고차원 희소 데이터(텍스트 분류, 원-핫 인코딩 피처)에서는 특정 가중치가 무한대로 발산할 수 있으므로, `penalty='l1'`(Lasso - 불필요 피처 자동 0 처리) 또는 `penalty='l2'`(Ridge - 가중치 분산 억제)를 필수 활성화해야 함.
- 비즈니스 목적에 따른 임계값(Threshold) 튜닝 : 기본값 0.5에 안주하지 말고, 암 진단이나 금융 사기 탐지(FDS)와 같이 위음성(False Negative - 미탐)의 비용이 치명적인 도메인에서는 임계값을 0.2~0.3 수준으로 낮추어 재현율(Recall)을 극대화하는 ROC(Receiver Operating Characteristic)-PR(Precision-Recall) 곡선 기반 최적화 수행을 제언함.
