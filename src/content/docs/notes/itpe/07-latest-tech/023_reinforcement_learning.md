---
title: "강화학습(Reinforcement Learning)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "023. 강화학습"
  order: 23
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>최신 기술</span><span>머신러닝 패러다임</span><strong>강화학습</strong></div>

## 30초 인출

- 본질: **강화학습(Reinforcement Learning, RL)** 은 정답 레이블 없이 에이전트(Agent)가 동적 환경(Environment)과 시행착오(Trial-and-Error) 상호작용을 통해 누적 보상(Cumulative Reward)을 최대화하는 최적 행동 정책(Policy)을 학습하는 기계학습 분야
- 메커니즘: 마르코프 결정 과정(MDP)을 수학적 기반으로 현재 상태(S)에서 행동(A)을 취하고, 환경으로부터 즉각적 보상(R)과 다음 상태(S')를 수신하여 벨만 최적 방정식을 통해 가치 함수 및 정책 파라미터 갱신
- 통찰: 보상 함수 설계의 결함으로 인한 보상 해킹(Reward Hacking)과 희소 보상 문제가 빈번하므로 인간 선호도 기반 RLHF, 호기심 기반 내재적 보상 및 PPO 알고리즘 결합 필수

<details><summary>핵심 용어</summary>

- **강화학습 (Reinforcement Learning)** : 에이전트가 보상을 극대화하는 방향으로 순차적 의사결정(Sequential Decision Making) 규칙을 학습하는 방법론.
- **MDP (Markov Decision Process)** : 상태(S), 행동(A), 전이확률(P), 보상(R), 할인율(γ)의 5개 튜플로 순차적 의사결정을 정형화한 수학적 모델.
- **정책 (Policy, π)** : 특정 상태(s)가 주어졌을 때 에이전트가 특정 행동(a)을 선택할 확률 분포 `π(a|s)`.
- **가치 함수 (Value Function, V, Q)** : 현재 상태 또는 상태-행동 쌍에서 시작하여 미래에 얻을 것으로 기대되는 할인된 누적 보상의 기댓값.
- **벨만 방정식 (Bellman Equation)** : 현재 시점의 보상과 다음 시점 가치 함수 간의 재귀적 관계를 표현한 동적 계획법의 핵심 수식.
- **PPO (Proximal Policy Optimization)** : 정책 업데이트 시 이전 정책과의 비율 변화 폭을 일정 범위 내로 클리핑(Clipping)하여 안정적인 수렴을 보장하는 대표적 정책 그래디언트 알고리즘.

</details>

---

## 2~4교시 예상문제 (25점)

> 인공지능 자율 의사결정의 핵심인 '강화학습(Reinforcement Learning)'의 개념과 마르코프 결정 과정(MDP)의 구성요소를 설명하고, 벨만 방정식 기반의 학습 메커니즘, 주요 알고리즘 분류(DQN, Policy Gradient, Actor-Critic) 및 LLM 정렬(RLHF) 적용 방안을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 강화학습의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **강화학습(Reinforcement Learning)** 은 주어진 환경 속에서 자율적인 에이전트가 시행착오를 거치며 얻는 지연된 보상(Delayed Reward) 신호를 기반으로 장기적 누적 보상을 극대화하는 최적의 행동 정책을 학습하는 기계학습 알고리즘 |
| 목적 | 인간의 사전 정답 데이터 없이도 복잡한 동적 환경(게임, 로보틱스, 자율주행, LLM 정렬)에서 최적의 제어 정책 자율 수립 |

## Ⅱ. 강화학습의 핵심 특징 및 타 학습 패러다임 대비 속성

| 구분 | 강화학습의 특징 | 세부 공학적 메커니즘 및 속성 |
|---|---|---|
| **시행착오 (Trial & Error)** | 능동적 데이터 수집 | 사전에 고정된 데이터셋이 아닌 에이전트의 현재 정책에 따라 동적으로 상호작용 데이터 생성 |
| **지연된 보상 (Delayed Reward)** | 신용 할당 문제(Credit Assignment) | 현재의 행동이 즉시 보상으로 이어지지 않고 수백 스텝 뒤의 최종 승패(보상)로 환류됨 |
| **탐험과 활용의 딜레마** | Exploration vs Exploitation | 새로운 가능성을 찾는 탐험(ε-Greedy)과 현재 알고 있는 최적 행동을 선택하는 활용 간의 균형 |
| **마르코프 성질 (Markov Property)** | 미래 상태의 조건부 독립 | 미래 상태 $S_{t+1}$는 오직 현재 상태 $S_t$와 현재 행동 $A_t$에만 의존하며 과거 이력과 무관 |

## Ⅲ. MDP 프레임워크 및 에이전트-환경 상호작용 프로세스

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ 강화학습 에이전트-환경 상호작용 루프 ]                 │
└────────────────────────────────────────────────────────────────────────┘
                                    │
       ┌────────────────────────────┴────────────────────────────┐
       ▼                                                         ▼
 ┌───────────┐      행동 (Action: A_t)                      ┌───────────┐
 │           │ ───────────────────────────────────────────> │           │
 │ 에이전트  │                                              │   환경    │
 │  (Agent)  │ <─────────────────────────────────────────── │(Environment)
 └───────────┘      상태 (State: S_{t+1}) 및 보상 (Reward: R_{t+1}) └───────────┘
       │                                                         │
       ▼                                                         ▼
[ 1. 상태 관측 S_t ] ──> [ 2. 정책 π(a|s) 추론 ] ──> [ 3. 행동 A_t 실행 ]
                                                                 │
                                                                 ▼
[ 5. 정책 갱신 (벨만 최적 방정식) ] ◄── [ 4. 피드백 수신 (R_{t+1}, S_{t+1}) ]
  - Q(s, a) = R + γ max_a' Q(s', a')  (Q-Learning 업데이트)
```

| MDP 구성요소 | 기호 | 공학적 의미 및 역할 |
|---|---|---|
| **상태 (State)** | $S$ | 에이전트가 의사결정을 내리기 위해 관측한 환경의 모든 물리적/논리적 정보 집합 |
| **행동 (Action)** | $A$ | 에이전트가 특정 상태에서 환경에 가할 수 있는 모든 조작 가능한 명령 집합 |
| **전이 확률** | $P(S' \mid S, A)$ | 상태 $S$에서 행동 $A$를 취했을 때 다음 상태 $S'$로 전이될 확률 분포 |
| **보상 함수** | $R(S, A, S')$ | 환경이 에이전트의 행동 결과에 대해 제공하는 즉각적인 스칼라 피드백 수치 |
| **할인율 (Discount)** | $\gamma \in [0, 1)$ | 미래에 받을 보상의 현재 가치를 감가상각하는 계수 (장기 계획 vs 단기 이익 조절) |

## Ⅳ. 주요 강화학습 알고리즘 계열 비교

| 비교 항목 | 가치 기반 (Value-based: DQN) | 정책 기반 (Policy-based: REINFORCE) | 액터-크리틱 (Actor-Critic: PPO/A2C) |
|---|---|---|---|
| **학습 대상** | 행동 가치 함수 $Q(s, a)$ 근사 | 정책 함수 $\pi_\theta(a \mid s)$ 직접 최적화 | 정책망(Actor) + 가치망(Critic) 동시 학습 |
| **행동 공간** | 이산적 행동 공간(Discrete)에 적합 | 연속적 행동 공간(Continuous) 지원 | 이산 및 연속 고차원 행동 공간 완벽 지원 |
| **정책 형태** | 결정론적(Deterministic, Argmax) | 확률론적(Stochastic) | 확률론적 정책 기반 안정적 수렴 |
| **분산 및 수렴성** | 분산 낮음, 과대추정(Overestimation) 편향 | 분산 매우 높음, 국소 최적해 수렴 위험 | 분산 축소(Critic 기준선) 및 빠른 수렴 |
| **대표 알고리즘** | Deep Q-Network, Rainbow | Policy Gradient, REINFORCE | PPO, SAC, DDPG, TRPO |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 복잡한 현실 과업에서 에이전트가 보상 산식의 허점을 파고들어 비정상 행위를 반복하는 보상 해킹(Reward Hacking) | 정량적 수작업 보상 대신 인간의 선호도를 딥러닝 보상 모델(RM)로 학습시키는 RLHF 도입 및 정규화(KL-Divergence) 페널티 부과 |
| 수천만 번의 무작위 탐험이 요구되는 극심한 샘플 비효율성(Sample Inefficiency) | 이전 경험을 버퍼에 저장하고 재사용하는 경험 리플레이(Experience Replay) 및 사전학습 모델의 모방 학습(Imitation Learning) 결합 |

## Ⅵ. 제언

인공지능의 안전성과 인간 의도 부합성을 확보하기 위해 PPO 알고리즘 기반의 RLHF(인간 피드백 강화학습) 파이프라인 구축.

```text
[ 사전학습 완료 언어모델 (SFT Model) ]
                 │
                 ▼
[ 인간 선호도 기반 보상 모델 (Reward Model) 구축 ]
   ├── Step 1: 동일 프롬프트에 대한 모델 응답 쌍(A, B) 인간 선호도 라벨링
   ├── Step 2: Bradley-Terry 모델 기반 보상 신경망 훈련
   └── Step 3: PPO 에이전트가 보상 모델의 점수를 극대화하도록 가중치 미세조정
                 │ (동시에 SFT 원본 모델과의 KL 발산 페널티를 부과하여 언어 왜곡 방지)
                 ▼
[ 유해성 및 환각이 억제된 안전한 정렬(Aligned) LLM 완성 ]
```

| 구분 | 기존 수작업 룰 기반 정렬 | 제언: PPO 기반 RLHF 파이프라인 |
|---|---|---|
| **피드백 형태** | 금지 단어 블랙리스트 if-else 차단 | 인간의 미묘한 선호도 뉘앙스를 보상 점수로 모델링 |
| **언어 유창성** | 하드 룰 차단으로 문맥 파괴 발생 | KL-Divergence 제약으로 고유의 추론 역량 완벽 보존 |
| **적응 속도** | 신규 악의적 표현마다 룰 수기 갱신 | 소량의 선호도 랭킹 데이터 추가 학습으로 즉각 정렬 |

## 출제 이력과 검증 출처

- 제139회 정보관리기술사 2교시 2번: LLM 학습 파이프라인에서 강화학습(RLHF) 기반 미세조정 방안
- Sutton & Barto, "Reinforcement Learning: An Introduction", MIT Press, 2018
- Mnih et al., "Human-level control through deep reinforcement learning", Nature, 2015 (DQN)
- Schulman et al., "Proximal Policy Optimization Algorithms", arXiv 2017 (PPO)

## 연결 토픽

- 상위 토픽: [007 머신러닝](./007_machine_learning.md)
- 연관 토픽: [045 RLHF](./045_rlhf.md), [029 피지컬 AI](./029_physical_ai.md), [035 에이전틱 AI](./035_agentic_ai.md)
