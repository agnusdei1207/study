---
title: "적대적 공격(Adversarial Attack)"
author: "Antigravity"
date: "2026-09-28T23:45:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "018. 적대적 공격(Adversarial Attack)"
  badge:
    text: "기초"
    variant: note
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

정보보안 → 인공지능 보안 → 적대적 공격 및 모델 강건성 확보

## 30초 인출

- **본질:** 인공지능 머신러닝 모델의 결정 경계(Decision Boundary) 취약점을 악용하여 인간의 눈에는 식별되지 않는 미세한 노이즈(섭동)를 주입해 오분류를 유도하는 공격
- **메커니즘:** 손실 함수 기울기 기반 입력 최적화($x_{adv} = x + \epsilon \cdot \text{sign}(\nabla_x L(\theta, x, y))$)를 통해 FGSM, PGD, C&W 적대적 예제 생성
- 통찰: 적대적 훈련 시 일반 정확도 하락과 기울기 마스킹 착시를 극복하기 위해 TRADES 정규화 손실 함수와 오토인코더 입력 정제 파이프라인 도입 필수

<details>
<summary>핵심 용어</summary>

- **적대적 예제 (Adversarial Example):** 정상 입력에 사람이 인지할 수 없을 정도의 정밀한 미세 노이즈($\delta$)를 합성하여 모델이 엉뚱한 레이블로 확신을 갖고 오분류하게 만든 데이터
- **섭동 (Perturbation, $\epsilon$):** 원본 입력 벡터에 가해지는 조작량으로, $L_\infty, L_2, L_0$ 노름(Norm) 제약 범위 내에서 최적화
- **FGSM (Fast Gradient Sign Method):** 모델 손실 함수의 입력에 대한 그래디언트 부호 방향으로 1회 스텝 이동하여 고속으로 적대적 예제를 생성하는 단일 스텝 기법
- **PGD (Projected Gradient Descent):** 작은 스텝 크기로 그래디언트 방향 갱신 후 $\epsilon$-볼(ball) 영역 내부로 반복 사영(Projection)하는 가장 강력한 1차 표준 공격
- **전이성 (Transferability):** 모델 A에서 생성된 적대적 예제가 모델 구조나 가중치가 다른 모델 B에서도 동일하게 오분류를 유발하는 블랙박스 공격의 핵심 속성
</details>

---
## 2~4교시 예상문제 (25점)

> 인공지능(AI) 모델에 대한 적대적 공격(Adversarial Attack)의 수학적 원리와 공격 유형을 분류하고, 주요 공격 알고리즘(FGSM, PGD, C&W)의 메커니즘 비교와 함께 모델 강건성 확보를 위한 방어 기법 및 엔지니어링 한계 극복 방안을 설명하시오. (예상·25점)

---
## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **적대적 공격(Adversarial Attack)** 은 머신러닝·딥러닝 모델의 고차원 선형성 및 비선형 결정 경계의 취약점을 분석하여, 육안으로 구별하기 힘든 미세한 섭동(Perturbation)을 입력에 주입함으로써 오분류 및 비정상 동작을 유발하는 AI 보안 위협 |
| 목적 | 자율주행 표지판 인식 오류 유도, 안면인식 출입통제 우회, AI 악성코드 탐지기 회피 등 모델의 기밀성·무결성·가용성 침해 |

학습 단계의 데이터 중독(Poisoning)과 구별되며, 이미 학습이 완료된 모델의 추론(Inference) 단계에서 결정 경계를 교란하는 회피(Evasion) 공격이 대표적임.

## Ⅱ. 적대적 공격의 특징 및 분류 체계

| 분류 기준 | 공격 유형 | 기술적 특징 |
|---|---|---|
| **공격자의 지식** | **화이트박스 (White-box)** | 모델 아키텍처, 가중치($\theta$), 손실 함수 기울기($\nabla_x L$)를 완전 파악 후 최적화 |
| | **블랙박스 (Black-box)** | 모델 내부를 알 수 없고 입출력 질의(Query) 결과 또는 전이성(Transferability) 악용 |
| **공격 목표** | **표적 공격 (Targeted)** | 입력 $x$를 공격자가 사전에 지정한 특정 클래스 $y_{target}$으로 오분류 유도 |
| | **비표적 공격 (Untargeted)** | 정답 $y_{true}$가 아닌 임의의 다른 오분류 결과를 유도 |
| **적용 시점** | **회피 공격 (Evasion)** | 배포된 모델의 추론 단계에서 입력값 조작 (적대적 예제) |
| | **중독 공격 (Poisoning)** | 학습 데이터셋에 백도어(Backdoor) 트리거를 심어 모델 자체를 오염 |

## Ⅲ. 적대적 공격 수학적 원리 및 프로세스

```text
[적대적 예제(Adversarial Example) 생성 및 사영 프로세스]

   원본 입력 (x)                     섭동 합성 (x + delta)             모델 오분류 유도
 +----------------+                 +---------------------+          +------------------+
 | 정상 정지 표지판| --(+)--------> | 미세 노이즈 추가    | -------> | 제한속도 100km/h |
 | (Stop Sign)    |   ^             | (사람 눈에는 동일)  |          | 오분류 판정      |
 +----------------+   |             +---------------------+          +------------------+
                      |                        |
             [그래디언트 섭동 최적화]          v
              delta = eps * sign(Grad)     [Epsilon-ball 사영(Projection)]
              (손실 함수 L을 최대화)       Clip(x + delta, [0, 1])
```

### 1. 주요 공격 알고리즘의 동작 수식

| 알고리즘 | 수학적 생성 메커니즘 | 알고리즘 특징 |
|---|---|---|
| **FGSM**<br>(Goodfellow, 2014) | $x_{adv} = x + \epsilon \cdot \text{sign}(\nabla_x L(\theta, x, y))$ | 그래디언트 부호 방향으로 1단계 점프. 연산이 매우 빠르나 섭동이 다소 큼 |
| **PGD**<br>(Madry, 2017) | $x^{t+1} = \Pi_{x+S}(x^t + \alpha \cdot \text{sign}(\nabla_x L(\theta, x^t, y)))$ | 작은 보폭 $\alpha$로 $k$회 반복 전진 후 $\epsilon$-Ball 내부로 사영($\Pi$). 1차 최강 공격 |
| **C&W**<br>(Carlini & Wagner) | $\min ||\delta||_p + c \cdot f(x + \delta)$ s.t. $x+\delta \in [0, 1]$ | 최적화 문제로 정식화하여 $L_2, L_\infty, L_0$ 노름 최소화. 방어 기법 100% 무력화 |

## Ⅳ. 주요 적대적 공격 알고리즘 비교

| 비교 항목 | FGSM (Fast Gradient) | PGD (Projected Gradient) | C&W (Carlini-Wagner) | DeepFool |
|---|---|---|---|---|
| **최적화 방식** | 1회 단일 스텝 연산 | 다단계 반복 사영 연산 | 라그랑주 승수 기반 최적화 | 최근접 결정경계 직교 사영 |
| **연산 비용** | 극도로 낮음 ($O(1)$ 백워드) | 보통 ($O(k)$ 백워드 패스) | 매우 높음 (수백 회 최적화 반복) | 보통 |
| **섭동 정밀도** | 거침 (노이즈 인지 가능) | 정밀함 (제어된 $\epsilon$) | 극도로 정밀 (인간 지각 불가) | 이론상 최소 섭동 크기 |
| **노름 기준** | $L_\infty$ | $L_\infty, L_2$ | $L_0, L_2, L_\infty$ | $L_2, L_\infty$ |
| **방어 회피율** | 보통 (기초 방어로 차단) | 매우 높음 (표준 강건성 벤치마크) | 최상 (대부분의 방어 우회) | 높음 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| **적대적 훈련 시 일반 정확도 급락(Accuracy-Robustness Trade-off)**<br>학습 데이터에 PGD 적대적 예제를 포함시키는 적대적 훈련(Adversarial Training) 적용 시, 적대적 공격에 대한 방어력은 상승하나 클린 데이터(정상 입력)에 대한 기본 분류 정확도가 $5 \sim 15\%$ 하락 | **TRADES 손실 함수 및 앙상블 가중치 정규화**<br>자연 손실(Natural Loss)과 적대적 정규화 손실(Robust Loss) 간의 가중치를 제어하는 $\text{TRADES} = L(f(x), y) + \beta \cdot \max D_{KL}(f(x) \parallel f(x_{adv}))$ 목적 함수를 적용하여 정상 정확도 보존과 강건성 간의 최적 파레토 프론티어(Pareto Frontier) 달성 |
| **기울기 마스킹(Gradient Masking) 방어 착시 및 블랙박스 전이 공격**<br>입력 양자화나 디펜시브 디스틸레이션(Defensive Distillation) 적용 시 그래디언트가 0이 되어 공격이 막힌 것처럼 보이나, 공격자가 대체 모델(Surrogate)을 구축한 전이성 공격 시 100% 무력화 | **입력 무작위화 변환 및 오토인코더 정제 파이프라인(Defense-GAN)**<br>입력 이미지에 무작위 리사이징·패딩(Random Resizing/Padding)을 적용해 그래디언트 계산을 교란하고, 오토인코더(Autoencoder)를 전면에 배치하여 고주파 적대적 노이즈를 입력 단계에서 제거 후 모델에 입력 |

## Ⅵ. 제언

```text
[신뢰할 수 있는 AI(Robust AI) 구현을 위한 심층 방어 아키텍처]

 +--------------------+     +---------------------+     +--------------------+
 | 1. 입력단 정제     | --> | 2. 모델 강건화      | --> | 3. 런타임 모니터링 |
 | 오토인코더/랜덤화  |     | TRADES 적대적 훈련  |     | 불확실성/OOD 탐지  |
 +--------------------+     +---------------------+     +--------------------+
```

| 방어 계층 | 주요 적용 기술 | 보안 확보 목표 |
|---|---|---|
| **데이터/입력단** | Randomization, Feature Squeezing, MagNet | 모델 진입 전 고주파 노이즈 1차 필터링 |
| **모델 아키텍처** | TRADES, PGD-Adversarial Training | 결정 경계를 완만하게 확장하여 강건성 내재화 |
| **추론/서빙단** | 마하비라 거리 기반 OOD(Out-of-Distribution) 감시 | 비정상적 질의 패턴 및 고확신 오분류 즉각 격리 |

단일 방어 알고리즘에 의존하는 대신, 입력 정제, 적대적 손실 훈련, 런타임 이상 탐지가 결합된 종합 MLSecOps 파이프라인 구축 권장.

---
## 출제 이력과 검증 출처

- 정보관리기술사 120회, 126회, 131회 적대적 공격(FGSM/PGD) 및 AI 모델 보안
- NIST AI 100-2e2025 Adversarial Machine Learning: A Taxonomy and Terminology
- Goodfellow et al. Explaining and Harnessing Adversarial Examples (ICLR 2015)
- Madry et al. Towards Deep Learning Models Resistant to Adversarial Attacks (ICLR 2018)

## 연결 토픽

- [LLM 보안 리스크](./002_llm_security_risks/)
- [블록체인 보안](./021_blockchain_security/)
