---
title: "베이즈 정리"
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

## Ⅰ. 확률적 추론의 핵심인 베이즈 정리(Bayes' Theorem) 개요

### 가. 베이즈 정리의 정의
- **베이즈 정리** : 새로운 데이터나 증거(Evidence)가 관측되었을 때, 이를 바탕으로 특정 사건의 **사전 확률** (Prior Probability)을 **사후 확률** (Posterior Probability)로 갱신(Update)하는 **조건부 확률** 정리.
- 빈도주의(Frequentist) 관점의 '무한 반복 시행에서의 빈도'와 달리, 불확실성 하에서 증거에 기반하여 주관적 믿음의 정도(Degree of Belief)를 합리적으로 갱신해 나가는 베이지안 확률론의 수학적 토대.

### 나. 베이즈 정리의 수식적 구조
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)} = \frac{P(B|A) \cdot P(A)}{\sum_{i} P(B|A_i)P(A_i)}$$

---

## Ⅱ. 베이즈 정리의 4대 핵심 구성 요소 및 작동 메커니즘

### 가. 수식 구성 요소별 의미

```text
[ 베이즈 정리 구성 메커니즘 ]
                  가능도 (Likelihood)  사전확률 (Prior)
                       P(B|A)      *    P(A)
  사후확률 P(A|B) = --------------------------------
                                 P(B)
                        정규화 상수 (Evidence)
```

| 구성 요소 | 기호 표기 | 통계적 의미 및 역할 | 구체적 예시 (스팸 필터링) |
| :--- | :--- | :--- | :--- |
| **사후 확률 (Posterior)** | $P(A\|B)$ | 새로운 증거 $B$가 주어졌을 때 가설 $A$가 참일 조건부 확률 | 특정 단어("무료")가 포함된 메일이 스팸일 확률 |
| **사전 확률 (Prior)** | $P(A)$ | 새로운 증거를 관측하기 전 가설 $A$에 대해 기존에 알고 있던 기저 확률 | 전체 수신 메일 중 일반적인 스팸 메일의 비율 |
| **가능도 (Likelihood)** | $P(B\|A)$ | 가설 $A$가 참이라고 가정할 때 증거 $B$가 나타날 조건부 확률 | 실제로 스팸 메일인 것들 중에서 "무료"라는 단어가 나타날 확률 |
| **주변 우도 (Evidence)** | $P(B)$ | 가설과 무관하게 증거 $B$ 자체가 전체에서 관측될 총 확률 (정규화 상수) | 전체 모든 메일 중에서 "무료"라는 단어가 나타날 총 확률 |

### 나. 베이즈 갱신(Bayesian Updating) 프로세스
- 초기 사전확률 $P(A) \rightarrow$ 1차 데이터 $B_1$ 관측 $\rightarrow$ 사후확률 $P(A|B_1)$ 산출 $\rightarrow$ 이 사후확률이 다음 단계의 새로운 사전확률 로 전이 $\rightarrow$ 2차 데이터 $B_2$ 관측 $\rightarrow$ 연속적인 지식 축적 및 신뢰도 향상.

---

## Ⅲ. 베이즈 정리의 공학적 응용 분야

### 가. 나이브 베이즈 분류기 (Naive Bayes Classifier)
- 모든 특성(Feature)들이 상호 독립(Conditionally Independent)이라는 '순진한(Naive)' 가정을 적용하여 다차원 결합 확률 계산을 단순 곱셈으로 해결:
  $$P(C_k|x_1, \dots, x_n) \propto P(C_k) \prod_{i=1}^n P(x_i|C_k)$$
- 텍스트 문서 분류, 스팸 메일 필터링, 실시간 악성 트래픽 탐지에서 초경량·고속 연산 제공.

### 나. A/B 테스트 및 강화학습(MAB)
- **베이지안 A/B 테스트** : 전통적인 $p$-value 검정의 고정 표본 크기 제약을 벗어나, 실험 진행 중에도 실시간으로 A안이 B안보다 우수할 사후 확률을 추적.
- **톰슨 샘플링(Thompson Sampling)** : 멀티암드 밴딧(MAB) 문제에서 각 슬롯머신의 보상 확률 사후 분포로부터 샘플링하여 탐색(Exploration)과 활용(Exploitation)의 최적 균형 달성.

---

## Ⅳ. 베이즈 정리 적용 시 주요 한계점 및 해결 방안

- 사전 확률(Prior Probability) 설정의 주관성 및 모델 편향 :
  - 한계점 : 사전 확률 선택에 분석가의 주관이 개입되어 잘못된 무정보 사전분포(Non-informative Prior) 설정 시 사후 확률이 심각하게 왜곡됨.
  - 해결 방안 : 대규모 역사적 데이터 기반의 실증적 베이즈(Empirical Bayes) 추정 도입, 사전분포 민감도 분석(Sensitivity Analysis)을 필수적으로 수행.
- 고차원 복합 결합확률의 사후분포 해석적 적분 불가(Tractability) :
  - 한계점 : 변수가 증가할수록 정규화 상수인 주변우도(Marginal Likelihood) 계산을 위한 고차원 다중 적분이 해석적으로 불가능하여 계산 마비 발생.
  - 해결 방안 : 마르코프 연쇄 몬테카를로(MCMC, Metropolis-Hastings, Gibbs Sampling) 알고리즘 또는 변분 추론(Variational Inference, VI) 기반 근사 기법 활용.
- 나이브 베이즈(Naive Bayes)의 조건부 독립 가정 위배 :
  - 한계점 : 모든 특징(Feature)이 클래스 조건부 독립이라는 강력한 비현실적 가정으로 인해 특징 간 강한 상관관계가 존재할 경우 사후확률이 과도하게 0 또는 1로 수렴.
  - 해결 방안 : 특징 간 상관성을 명시적 그래프 구조로 모델링하는 베이지안 네트워크(Bayesian Network) 도입 또는 라플라스 평활화(Laplace Smoothing) 적용.

---

## Ⅴ. 머신러닝 및 데이터 실무 관점의 제언

- 사전분포(Prior) 선택의 객관성 확보 : 사전확률을 임의로 잘못 설정하면 적은 데이터 환경에서는 사후확률이 크게 왜곡될 수 있으므로, 정보가 없을 때는 무정보 사전분포(Non-informative Prior)나 켤레 사전분포(Conjugate Prior)를 수학적으로 엄밀히 적용해야 함.
- 사후분포 근사 계산 기법(MCMC) 활용 : 고차원 파라미터 공간에서는 주변 우도 $P(B)$의 적분 계산이 불가능하므로, MCMC(Markov Chain Monte Carlo) 또는 변분 추론(Variational Inference) 알고리즘을 결합한 확률적 프로그래밍(Stan, PyMC) 체계를 구축할 것을 제언함.
