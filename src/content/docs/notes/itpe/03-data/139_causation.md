---
title: "인과관계(Causation)와 인과추론"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 단순 상관관계를 넘어선 진실의 규명, 인과관계와 인과추론 개요

### 가. 인과관계(Causation)의 정의
- **원인** (Cause, 처치 $T$)의 변화가 **결과** (Effect, 결과변수 $Y$)의 변화를 직접적으로 유발하는 필연적인 법칙 관계.
- 두 변수가 단순히 함께 변동하는 통계적 연관성을 의미하는 **상관관계** (Correlation)와 달리, 원인에 대한 **능동적 개입** (Intervention, $do(T)$)이 가해졌을 때 결과가 어떻게 변하는가를 규명함.

### 나. 인과추론(Causal Inference)의 필요성
- 머신러닝의 예측(Prediction)은 상관성에 의존하므로 환경 변화 시 예측 실패(드리프트)를 겪음.
- 가격 인하, 마케팅 프로모션, 신약 처방 등 "우리가 행동을 변경했을 때 어떤 일이 벌어질 것인가?"에 대한 올바른 의사결정을 위해서는 반드시 인과추론이 필요함.

---

## Ⅱ. 인과추론의 양대 이론 프레임워크: 루빈 잠재결과 vs 펄 인과 다이어그램

### 가. 루빈 잠재결과 프레임워크 (Rubin Causal Model, RCM)

```text
[ 잠재적 결과 (Potential Outcomes) 모형 ]
개체(i)에 대하여:
  - Y_i(1) : 처치를 받았을 때(T=1) 나타날 잠재적 결과
  - Y_i(0) : 처치를 받지 않았을 때(T=0) 나타날 잠재적 결과
  * 개별 인과 효과 (Individual Treatment Effect) : tau_i = Y_i(1) - Y_i(0)
```

- **인과추론의 근본적 문제 (Fundamental Problem of Causal Inference)** : 현실 세계에서는 동일한 개체에 대해 $Y_i(1)$과 $Y_i(0)$ 중 오직 하나만 관측 가능하며, 다른 하나는 관측 불가능한 **반사실** (Counterfactual)로 남음.
- 해법 : 개별 효과 대신 집단 전체의 **평균 처치 효과** (ATE, Average Treatment Effect)를 추정:
  $$ATE = E[Y(1) - Y(0)]$$

### 나. 주디아 펄(Judea Pearl)의 인과 그래프(DAG)와 do-연산자

```text
[ 인과적 구조적 인과 모델 (SCM / DAG) ]
       [교란변수 Z] (예: 환자의 연령)
        /        \
       v          v
   [처치 T] ---> [결과 Y] (T: 신약 복용, Y: 완치 여부)
   - Z는 T와 Y 모두에 영향을 미치며 허위 상관을 생성하는 배후 경로(Backdoor Path) 형성
   - do(T=t) 연산: Z -> T 로 향하는 화살표를 강제로 절단(Intervention)하여 순수 인과 효과 격리!
```

---

## Ⅲ. 실험 및 준실험(Quasi-Experiment) 기반 4대 인과추론 기법

| 방법론 | 핵심 작동 메커니즘 | 적용 조건 및 강점 | 한계 및 주의사항 |
| :--- | :--- | :--- | :--- |
| **무작위 대조 시험 (RCT, Randomized Controlled Trial / A/B Test)** | 피험자를 무작위 배정하여 처치군과 대조군의 모든 교란변수($Z$)를 완벽히 균등화 | 인과추론의 골드 스탠다드 (가장 정확) | 윤리적·비용적 한계로 모든 분야에 적용 불가 |
| **성향점수 매칭 (PSM, Propensity Score Matching)** | 관측된 공변량($X$)들을 바탕으로 처치를 받을 확률(성향점수)을 추정 후 유사 개체끼리 1:1 매칭 | 관측 데이터에서 교란변수의 불균형 해소 | 관측되지 않은 숨은 교란변수는 통제 불가 |
| **이중차분법 (DID, Difference-in-Differences)** | 처치 전후의 변화량에서 대조군의 전후 변화량을 차감 ($(\Delta Y_{treat} - \Delta Y_{control})$) | 정책 효과 평가, 시간 경과에 따른 자연 증가분 통제 | **평행 추세 가정** (Parallel Trends) 만족 필수 |
| **도구변수법 (IV, Instrumental Variable)** | 처치($T$)에는 직접 영향을 미치지만, 오차항 및 결과($Y$)와는 독립인 외생적 도구변수($Z$) 활용 | 관측되지 않은 내생성(Endogeneity) 극복 가능 | 유효한 도구변수를 발굴하기가 극도로 어려움 |

---

## Ⅳ. 인과추론(Causal Inference)의 주요 한계점 및 해결 방안

- 관측 불가능한 교란 변수(Unobserved Confounder)로 인한 선택 편향 :
  - 한계점 : 무작위 통제 시험(RCT)이 불가능한 비즈니스 관측 데이터에서 잠재된 외생 변수를 완벽히 통제하지 못해 처리 효과(ATE)가 심각하게 왜곡.
  - 해결 방안 : 도구변수(Instrumental Variables) 기법 적용, 성향점수 매칭(PSM) 및 **역확률 가중치** (IPW, Inverse Probability Weighting), **민감도 분석** (Sensitivity Analysis: Rosenbaum Bounds) 수행.
- 이중차분법(DID) 적용 시 평행 추세 가정(Parallel Trends Assumption) 위반 :
  - 한계점 : 정책 개입이나 프로모션 전 처리군과 통제군의 트렌드가 사전에 다르게 움직였을 경우 DID 추정치가 정책의 순수 효과를 반영하지 못함.
  - 해결 방안 : 사전 기간(Pre-treatment) **이벤트 연구** (Event Study) 플롯 검증, **합성 대조군** (Synthetic Control Method) 기법을 통한 최적 통제군 가중 결합.
- 높은 차원의 복합 상호작용 환경에서 전통적 통계 모델의 표현력 한계 :
  - 한계점 : 교란 요인이 수백 개에 달하고 변수 간 비선형 결합이 존재할 경우 표준 선형 회귀나 성향점수 로지스틱 모델의 적합도 급락.
  - 해결 방안 : 머신러닝과 인과추론을 결합한 **더블 머신러닝** (Double/Debiased Machine Learning: DML) 및 **인과 포레스트** (Causal Forests) 알고리즘 도입.

## Ⅴ. 비즈니스 의사결정 및 데이터 사이언스 실무 제언

- A/B 테스트 불가능 환경에서의 이중차분법(DID) 활용 : 전국 단위 가격 인상이나 법 개정처럼 대조군을 무작위 배정할 수 없는 비즈니스 의사결정에서는, 유사한 인접 국가나 경쟁 플랫폼을 대조군으로 삼아 평행 추세 검증을 거친 DID 모델을 적용해야 함.
- 머신러닝과 Causal AI(Artificial Intelligence)의 결합 (Uplift Modeling) : 단순히 이탈 확률이 높은 고객을 찾는 것이 아니라, "쿠폰을 주었기 때문에 이탈을 멈출 고객(Persuadables)"과 "쿠폰을 주지 않아도 남을 고객"을 구별하는 **업리프트 모델링** (Uplift Modeling)을 CRM(Customer Relationship Management) 마케팅에 도입할 것을 제언함.
