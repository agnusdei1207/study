---
title: "신경망(Neural Network)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags: ["notes-latest-tech"]
sidebar:
  label: "162. 신경망(Neural Network)"
  order: 162
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>인공지능·기계학습</span><span>인공신경망 및 딥러닝</span><strong>신경망(Neural Network)</strong></div>

## 30초 인출

- 본질: **신경망** (Neural Network)은 생물학적 뉴런의 시냅스 결합 구조를 수학적으로 모사하여 입력층, 은닉층, 출력층의 선형 결합($Wx+b$)과 비선형 활성화 함수를 통해 복잡한 비선형 관계를 학습하는 인공지능 모델
- 메커니즘: 순전파(Forward Propagation) 연산으로 예측값 출력 → 목적 함수(Loss) 계산 → 연쇄 법칙(Chain Rule) 기반 역전파(Backpropagation) 기울기 산출 → 가중치 파라미터 최적화 갱신
- 통찰: 은닉층이 깊어질수록 역전파 도중 기울기가 0으로 수렴하는 기울기 소실(Vanishing Gradient)과 과적합이 발생하므로 He 초기화, ReLU/GELU 활성화, 잔차 연결(ResNet) 및 배치/레이어 정규화 결합 체계 구축 필요

<details><summary>핵심 용어</summary>

- **퍼셉트론 (Perceptron)** : 입력 벡터에 가중치를 곱하고 편향을 더한 뒤 활성화 함수를 거쳐 출력을 내는 최소 단위 인공신경망.
- **보편 근사 정리 (Universal Approximation Theorem)** : 비선형 활성화 함수를 갖춘 단 하나의 은닉층만으로도 어떤 연속 함수든 임의의 정밀도로 근사할 수 있다는 수학적 정리.
- **연쇄 법칙 (Chain Rule)** : 합성함수의 미분을 각 구성 함수의 편미분 곱으로 분해하여 출력층에서 입력층 방향으로 오차 기울기를 전파하는 수학 공식.
- **기울기 소실 (Vanishing Gradient)** : 심층 신경망에서 활성화 함수의 미분값이 1 미만일 때 층을 거슬러 올라갈수록 기울기가 지수적으로 감소하여 학습이 정체되는 현상.
- **잔차 연결 (Residual Connection)** : 입력 $x$를 층의 출력에 직접 더해주는 스킵 연결($y = F(x) + x$)을 통해 기울기가 감쇄 없이 하위 계층으로 직접 흐르도록 하는 기술.

</details>

---

## 2~4교시 예상문제 (25점)

> 인공지능 딥러닝 혁신의 근간인 인공신경망(Artificial Neural Network)의 수학적 동작 메커니즘(순전파, 역전파, 연쇄 법칙)을 설명하고, 심층 신경망 학습 시 발생하는 기울기 소실(Vanishing Gradient) 및 과적합(Overfitting)의 원인과 이를 해결하기 위한 현대 공학적 기법을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 인공신경망의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 인간 뇌의 신경세포 네트워크를 모방하여 다수의 인공 뉴런(노드)이 가중치(Weight)로 연결된 층(Layer) 구조를 이루고, 비선형 활성화 함수와 역전파 학습을 통해 입출력 간 복합 매핑을 근사하는 기계학습 모델 |
| 목적 | 이미지 인식, 음성 처리, 자연어 이해 등 전통적 선형 알고리즘으로 해결 불가능한 고차원 비선형 문제의 특징 자동 추출 및 패턴 분류 |

## Ⅱ. 인공신경망의 핵심 구성 요소 및 보편 근사 특징

| 구성 요소 | 수학적 표현 및 연산 | 주요 역할 및 특징 |
|---|---|---|
| **인공 뉴런 (노드)** | $z = \sum_{i=1}^n w_i x_i + b = W^T X + b$ | 다수의 입력 신호에 가중치를 곱하고 편향(Bias)을 합산하는 선형 변환 |
| **비선형 활성화 함수** | $a = \sigma(z)$ (ReLU, GELU, Sigmoid 등) | 신경망에 비선형 표현력(Non-linearity)을 부여하여 다층 구조의 효용성 보장 |
| **손실 함수 (Loss)** | $L(y, \hat{y})$ (MSE, Cross-Entropy) | 모델 예측값과 실제 정답 간의 오차를 수치화하여 최적화 목표 제시 |
| **보편 근사 정리** | $\forall f \in C(K), \ |F(x) - f(x)| < \epsilon$ | 충분한 은닉 노드가 주어지면 임의의 복잡한 연속 함수를 완전 근사 가능 |

## Ⅲ. 인공신경망 순전파-역전파 학습 파이프라인

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 인공신경망 순전파 예측 및 역전파(Backpropagation) 오차 전파 프로세스 ]│
└────────────────────────────────────────────────────────────────────────┘

  [ 1. 순전파 계층 (Forward Pass) ]
  입력 벡터 $X$ ──> [ 은닉층 1: $z_1 = W_1 X + b_1$ ] ──> $a_1 = \sigma(z_1)$
                          │
                          ▼
                    [ 은닉층 2: $z_2 = W_2 a_1 + b_2$ ] ──> $a_2 = \sigma(z_2)$
                          │
                          ▼
                    [ 출력층: $\hat{y} = \sigma(W_o a_2 + b_o)$ ]
                          │
                          ▼
  [ 2. 손실 산출 (Loss Computation) ]
   - 오차 계산: $L = \text{CrossEntropy}(y, \hat{y})$
                          │
                          ▼ (연쇄 법칙 역방향 전파)
  [ 3. 역전파 계층 (Backward Pass via Chain Rule) ]
   ├── 출력층 기울기: $\frac{\partial L}{\partial W_o} = \frac{\partial L}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z_o} \cdot \frac{\partial z_o}{\partial W_o}$
   ├── 은닉층 2 기울기: $\frac{\partial L}{\partial W_2} = \frac{\partial L}{\partial a_2} \cdot \frac{\partial a_2}{\partial z_2} \cdot \frac{\partial z_2}{\partial W_2}$
   └── 은닉층 1 기울기: 하위 층으로 오차 그래디언트 지속 전파
                          │
                          ▼
  [ 4. 파라미터 갱신 (Optimizer Update: AdamW / SGD) ]
   - $W_{new} = W_{old} - \eta \cdot \frac{\partial L}{\partial W}$
```

| 학습 단계 | 세부 연산 내용 | 핵심 수학 기법 |
|---|---|---|
| **순전파 (Forward)** | 계층별 행렬 곱연산($W \cdot X$)과 활성화 함수 통과 | 텐서 곱셈 (GEMM 가속) |
| **오차 평가 (Loss)** | 예측 확률 분포와 정답 원-핫 벡터 간 크로스 엔트로피 계산 | Kullback-Leibler 발산 최소화 |
| **역전파 (Backward)** | 계산 그래프(Computational Graph)를 따라 국소 미분값 역방향 누적 곱 | 연쇄 법칙 (Chain Rule) |
| **가중치 최적화** | 학습률과 1·2차 모멘텀을 적용하여 전역 최적점으로 가중치 이동 | AdamW, 모멘텀 경사하강법 |

## Ⅳ. 주요 활성화 함수 비교 분석

| 비교 항목 | 시그모이드 (Sigmoid) | 렐루 (ReLU) | 젤루 (GELU) |
|---|---|---|---|
| **수학 공식** | $\sigma(z) = \frac{1}{1 + e^{-z}}$ | $f(z) = \max(0, z)$ | $f(z) = z \cdot \Phi(z) = z \cdot P(X \le z)$ |
| **출력 범위** | $0.0 \sim 1.0$ (항상 양수) | $[0, \infty)$ (비음수) | 약 $[-0.17, \infty)$ (음수 영역 완만) |
| **도함수 최댓값**| $0.25$ ($z=0$일 때) | $1.0$ ($z > 0$일 때) | 연속적 미분 가능 곡선 |
| **기울기 소실** | 심각함 (층이 깊어지면 미분값 소멸) | 양수 영역에서 기울기 1 유지로 극복 | 음수 영역에서도 미세 기울기 유지로 극복 |
| **Dying 노드** | 없음 | 음수 입력 시 뉴런 완전 영구 사망 | 입력 확률에 따른 부드러운 통과로 해결 |
| **대표 활용** | 로지스틱 회귀, 이진 분류 출력층 | CNN, 전통적 심층 신경망(ResNet) | BERT, GPT-4 등 트랜스포머/LLM 표준 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 시그모이드/tanh 사용 시 역전파 단계에서 미분값이 누적 곱해지며 입력층 근처 기울기가 0이 되는 기울기 소실 발생 | ReLU/GELU 활성화 함수 적용, He/Xavier 가중치 초기화 및 입력을 직접 출력에 바이패스하는 잔차 연결(Residual Connection) 도입 |
| 과도하게 깊은 신경망이 훈련 데이터의 무작위 노이즈까지 암기하여 테스트 데이터 성능이 급락하는 과적합(Overfitting) 발생 | 학습 도중 무작위로 뉴런을 비활성화하는 드롭아웃(Dropout $\approx 0.2\sim 0.5$) 적용, L2 가중치 감쇠 및 검증 손실 기준 조기 종료(Early Stopping) 결합 |
| 수억 개 가중치 파라미터 간의 복잡한 비선형 상호작용으로 인해 인공신경망의 판단 근거를 사람이 역추적할 수 없는 블랙박스 문제 | 특징 맵의 중요도를 시각화하는 Grad-CAM 적용 및 샤플리 값 기반 기여도 분석(SHAP/LIME) 설명가능 AI(XAI) 파이프라인 결합 |

## Ⅵ. 제언

현대 초거대 인공신경망의 안정적 수렴을 위해 개별 기법을 단편적으로 적용하지 않고, '정규화 + 잔차 연결 + 적응형 옵티마이저'가 유기적으로 결합된 표준 심층 블록 아키텍처 구축 필요.

```text
[ 이전 레이어 활성화 출력 ($x$) ]
              │
              ├─────────────────────────────────────────┐ (Residual Skip Connection)
              ▼                                         │
[ 정규화 계층 (Pre-LayerNorm / RMSNorm) ]               │
              │                                         │
              ▼                                         │
[ 선형 변환 및 비선형 활성화 (Linear + GELU) ]           │
              │                                         │
              ▼                                         │
[ 규제화 계층 (Dropout: p=0.1) ]                        │
              │                                         │
              ▼                                         │
[ 잔차 가산 (Residual Addition: $y = x + F(x)$) ] <─────┘
              │
              ▼
[ 100층 이상의 초심층 네트워크에서도 기울기 소실 없이 안정적 수렴 달성 ]
```

| 구분 | 초기 다층 퍼셉트론 (MLP) | 제언: 현대 심층 신경망 표준 블록 |
|---|---|---|
| **활성화 함수** | Sigmoid (미분 최댓값 0.25) | GELU (부드러운 비선형 확률 통과) |
| **가중치 초기화** | 무작위 정규분포 (분산 폭발/소실) | He / Kaiming 분산 보존 초기화 |
| **신호 전파** | 단순 직렬 통과 (10층 이상 학습 불가) | 잔차 스킵 연결로 수백 층 무손실 전파 |
| **내부 공변량 변화** | 입력 분포 변화로 학습 불안정 | Pre-LayerNorm 적용으로 계층별 입력 안정화 |

## 출제 이력과 검증 출처

- 제118회 정보관리기술사 1교시: 인공신경망의 활성화 함수(Activation Function) 종류 및 특징
- David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams, "Learning representations by back-propagating errors" (Nature 1986)
- Kaiming He et al., "Deep Residual Learning for Image Recognition" (CVPR 2016, ResNet 원저작)

## 연결 토픽

- 상위 토픽: [144 귀납적 추론과 머신러닝](./144_inductive_reasoning_and_machine_learning.md)
- 연관 토픽: [145 뉴로모픽 칩](./145_neuromorphic_chip.md), [158 최적화 알고리즘](./158_optimization_algorithm.md)
