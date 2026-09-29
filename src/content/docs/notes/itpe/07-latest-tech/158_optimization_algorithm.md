---
title: "최적화 알고리즘(Optimization Algorithm)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags: ["notes-latest-tech"]
sidebar:
  label: "158. 최적화 알고리즘(Optimization Algorithm)"
  order: 158
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>머신러닝·딥러닝</span><span>손실 함수 및 최적화</span><strong>최적화 알고리즘(Optimization Algorithm)</strong></div>

## 30초 인출

- 본질: **최적화 알고리즘** (Optimization Algorithm)은 손실 함수(Loss Function)의 값을 최소화하기 위해 역전파로 계산된 기울기(Gradient)를 바탕으로 모델 파라미터를 반복 갱신하는 수치 최적화 기법
- 메커니즘: 미니배치 순전파 손실 계산 → 역전파 1·2차 모멘텀 산출 → 학습률 스케줄러 적용 → 분리된 가중치 감쇠(AdamW) 적용 파라미터 업데이트
- 통찰: Adam 옵티마이저에 단순 L2 규제화를 적용하면 적응형 학습률과 결합되어 가중치 감쇠 효과가 왜곡되므로 가중치 감쇠를 기울기 갱신과 완전 분리한 AdamW 체계 구축 필요

<details><summary>핵심 용어</summary>

- **경사하강법 (Gradient Descent)** : 목적 함수의 기울기 반대 방향으로 파라미터를 일정 보폭(학습률)만큼 이동시키는 기본 최적화 알고리즘.
- **모멘텀 (Momentum)** : 과거 기울기의 지수 이동 평균을 반영하여 진동을 억제하고 관성을 주어 안장점(Saddle Point)을 탈출하는 기법.
- **Adam (Adaptive Moment Estimation)** : 1차 모멘텀(관성)과 2차 모멘텀(기울기 제곱 평균 기반 적응형 학습률)을 결합한 대표적 최적화기.
- **AdamW (Decoupled Weight Decay)** : Adam에서 L2 정규화가 적응형 그래디언트에 의해 희석되는 수학적 결함을 해결하기 위해 가중치 감쇠를 분리한 알고리즘.
- **학습률 웜업 (Warmup)** : 학습 초기 가중치 급변을 방지하기 위해 학습률을 0에서 목표치까지 서서히 선형 증가시키는 안정화 기법.

</details>

---

## 2~4교시 예상문제 (25점)

> 딥러닝 모델 학습의 핵심인 최적화 알고리즘(Optimizer)의 발전 계보(SGD, Momentum, RMSprop, Adam)를 설명하고, Adam의 L2 정규화 결함과 이를 극복한 AdamW의 가중치 감쇠 분리 메커니즘 및 학습률 스케줄링 전략을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 최적화 알고리즘의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 딥러닝 역전파(Backpropagation) 단계에서 산출된 손실 함수의 1계·2계 도함수(기울기) 정보를 활용하여 목적 함수를 최소화하는 방향으로 신경망 가중치($\theta$)를 점진적 갱신하는 수치 알고리즘 |
| 목적 | 안장점(Saddle Point) 및 국소 최솟값(Local Minima) 탈출, 학습 수렴 속도 가속화 및 테스트 데이터셋에 대한 일반화 성능 극대화 |

## Ⅱ. 최적화 알고리즘의 발전 계보 및 핵심 특징

| 진화 방향 | 핵심 알고리즘 | 수식 및 갱신 특징 |
|---|---|---|
| **기본 경사하강** | SGD (확률적 경사하강법) | $\theta_{t+1} = \theta_t - \eta g_t$, 무작위 미니배치 샘플링으로 빠른 연산 지원 |
| **방향(관성) 개선** | Momentum, NAG | 과거 그래디언트의 누적 관성($v_t = \gamma v_{t-1} + \eta g_t$) 반영, 협곡 진동 억제 |
| **보폭(학습률) 개선**| AdaGrad, RMSprop | 그래디언트 제곱합 누적으로 자주 변하는 피처는 작은 보폭, 드문 피처는 큰 보폭 적용 |
| **관성 + 보폭 융합** | Adam | 1차 모멘트($m_t$)와 2차 모멘트($v_t$)를 바이어스 보정 후 동시 적용 |
| **정규화 분리** | AdamW | L2 페널티를 손실 함수가 아닌 가중치 갱신식에 직접 분리 적용 ($\theta_{t+1} = \theta_t(1 - \eta \lambda) - \dots$) |

## Ⅲ. 최적화 알고리즘 파이프라인 및 AdamW 가중치 갱신 프로세스

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ AdamW 옵티마이저의 분리형 가중치 감쇠(Decoupled Weight Decay) 파이프라인 ] │
└────────────────────────────────────────────────────────────────────────┘

  [ 미니배치 데이터 입력 ($x, y$) ] ──> [ 순전파 손실 계산: $L(\theta)$ ]
                                                │
                                                ▼ (역전파 미분)
                                  [ 현재 시점 기울기: $g_t = \nabla_\theta L(\theta_t)$ ]
                                                │
                 ┌──────────────────────────────┴──────────────────────────────┐
                 ▼ (1차 모멘텀: 방향 추적)                                     ▼ (2차 모멘텀: 보폭 조정)
  [ 1차 모멘트 지수평균 ]                                       [ 2차 모멘트 지수평균 ]
  $m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$                   $v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$
                 │                                                             │
                 ▼                                                             ▼
  [ 1차 바이어스 보정: $\hat{m}_t = \frac{m_t}{1 - \beta_1^t}$ ]  [ 2차 바이어스 보정: $\hat{v}_t = \frac{v_t}{1 - \beta_2^t}$ ]
                 │                                                             │
                 └──────────────────────────────┬──────────────────────────────┘
                                                ▼
                        [ 학습률 스케줄러 적용 보폭: $\frac{\eta_t}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$ ]
                                                │
                                                ▼ (★ 가중치 감쇠 분리 적용)
                        [ 파라미터 갱신: $\theta_{t+1} = \theta_t - \eta_t \lambda \theta_t - \frac{\eta_t}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$ ]
```

| 연산 단계 | 수학적 메커니즘 | 공학적 효과 |
|---|---|---|
| **기울기 산출** | 손실 함수에 대한 가중치 편미분 벡터 $g_t$ 계산 | 역전파 자동 미분(Autograd) |
| **모멘텀 갱신** | $\beta_1=0.9, \beta_2=0.999$ 설정 기반 지수 감쇄 평균 누적 | 노이즈 상쇄 및 부드러운 궤적 형성 |
| **0점 편향 보정** | $t$ 초기 시점 $m_t, v_t$가 0으로 편향되는 수학적 왜곡 제거 | 학습 초기 발산 방지 |
| **분리 가중치 감쇠** | 적응형 학습률 $\sqrt{\hat{v}_t}$와 무관하게 원래 가중치에 직접 비례 감쇠 | 표준 L2 정규화 본래 의도 완벽 복원 |

## Ⅳ. 주요 딥러닝 최적화 알고리즘 비교

| 비교 항목 | SGD + Momentum | RMSprop | Adam | AdamW |
|---|---|---|---|---|
| **핵심 메커니즘** | 속도 벡터(관성) 반영 | 이동평균 기반 적응형 학습률 | 관성(1차) + 적응형(2차) 결합 | Adam + 가중치 감쇠 분리 |
| **학습률 조정** | 수동 스케줄러에만 의존 | 파라미터별 자동 크기 조정 | 파라미터별 자동 크기 조정 | 파라미터별 자동 크기 조정 |
| **하이퍼파라미터** | $\eta, \gamma$ (모멘텀 계수) | $\eta, \gamma, \epsilon$ | $\eta, \beta_1, \beta_2, \epsilon$ | $\eta, \beta_1, \beta_2, \epsilon, \lambda$ |
| **가중치 감쇠** | L2 정규화와 완벽히 동치 | L2 정규화 시 스케일 왜곡 | L2 정규화 시 심각한 왜곡 | 분리된 가중치 감쇠 완벽 작동 |
| **일반화 성능** | 튜닝 시 최상 (수렴 느림) | 중간 | 종종 SGD보다 일반화 낮음 | 트랜스포머/LLM에서 표준 채택 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 전통 Adam에서 L2 정규화 결합 시 그래디언트가 큰 가중치는 덜 감쇠되고 작은 가중치는 과감쇠되는 왜곡 발생 | 손실 함수에 L2 텀을 더하지 않고 가중치 업데이트 식에서 직접 감쇠율을 곱하는 AdamW 알고리즘 전면 적용 |
| 학습 초기 큰 학습률로 인한 가중치 파괴 및 그래디언트 폭주(Exploding Gradient) 현상 | 선형 학습률 웜업(Linear Warmup)을 최초 수천 스텝에 적용하고 그래디언트 클리핑(Gradient Clipping, Norm $\le 1.0$) 병행 |
| 고정된 학습률 사용 시 손실 함수 골짜기(Valley) 주변에서 수렴하지 못하고 맴도는 진동 발생 | 코사인 감쇄(Cosine Annealing) 스케줄러 적용 및 지수 이동 평균(EMA: Exponential Moving Average) 가중치 체크포인트 유지 |

## Ⅵ. 제언

초거대 언어모델(LLM) 및 대규모 딥러닝 학습의 수렴 안정성을 위해 AdamW 기반 분리형 감쇠와 코사인 학습률 스케줄러를 결합한 종합 최적화 파이프라인 구축 필요.

```text
[ LLM 사전학습(Pre-training) 시작 ]
                 │
                 ▼
[ 학습률 스케줄링 전략 (Cosine Annealing with Warmup) ]
   ├── 구간 1: Warmup Phase (0 ~ 2,000 Step: $\eta = 0 \rightarrow 1e-4$)
   ├── 구간 2: Cosine Decay Phase (2,000 ~ 100,000 Step: $\eta \rightarrow 1e-5$)
   └── 구간 3: Minimum LR Cooldown Phase
                 │
                 ▼
[ AdamW 옵티마이저 실행 ($\beta_1=0.9, \beta_2=0.95, Weight Decay=0.1$) ]
   ├── Step 1: FP16/BF16 혼합 정밀도 그래디언트 언더플로우 방지 (GradScaler)
   ├── Step 2: Global Gradient Norm $\le 1.0$ 초과분 자동 클리핑
   └── Step 3: ZeRO-Stage 3 분산 옵티마이저 상태 메모리 샤딩
                 │
                 ▼
[ 대규모 GPU 클러스터 무손실 고속 수렴 달성 ]
```

| 구분 | 고정 학습률 Adam | 제언: Warmup-Cosine AdamW 파이프라인 |
|---|---|---|
| **수렴 안정성** | 초기 그래디언트 폭주로 학습 붕괴 빈번 | Warmup 구간을 통해 안정적 파라미터 안착 |
| **일반화 능력** | 과도한 훈련 손실 감소 대비 검증 오차 큼 | 분리 가중치 감쇠로 일반화 갭(Generalization Gap) 최소화 |
| **후반부 튜닝** | 고정 보폭으로 미세 최적점 주변 배회 | 코사인 스케줄러를 통해 딥 로컬 미니마 정밀 수렴 |
| **대규모 분산** | 단일 노드 옵티마이저 상태 메모리 포화 | ZeRO/FSDP 결합 옵티마이저 상태 분산 샤딩 지원 |

## 출제 이력과 검증 출처

- 제123회 정보관리기술사 1교시: 딥러닝의 최적화 알고리즘 발전 과정과 Adam
- Ilya Loshchilov & Frank Hutter, "Decoupled Weight Decay Regularization" (ICLR 2019, AdamW 원저작)
- Diederik P. Kingma & Jimmy Ba, "Adam: A Method for Stochastic Optimization" (ICLR 2015)

## 연결 토픽

- 상위 토픽: [162 인공신경망](./162_neural_network.md)
- 연관 토픽: [144 귀납적 추론과 머신러닝](./144_inductive_reasoning_and_machine_learning.md), [154 엔트로피 지수](./154_entropy_index.md)
