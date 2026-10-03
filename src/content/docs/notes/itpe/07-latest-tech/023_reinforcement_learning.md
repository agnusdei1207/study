---
title: "강화학습(Reinforcement Learning)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 강화학습(Reinforcement Learning)의 개요

- 개념 : **에이전트** (Agent)가 동적인 **환경** (Environment) 내에서 명시적인 정답(Label) 없이 시행착오(Trial and Error)를 통해 상호작용하며, 주어진 **상태** (State)에서 미래에 획득할 **누적 보상** (Cumulative Return)을 최대화하는 최적의 행동 **정책** (Policy)을 학습하는 머신러닝 패러다임.
- 배경 및 필요성 : 지도학습처럼 대량의 정답 레이블을 구축하기 어렵거나, 체스/바둑, 자율주행, 로봇 제어, LLM 정렬처럼 일련의 연속된 의사결정(Sequential Decision Making)과 시간 지연된 보상이 지배하는 복합 환경을 해결하기 위해 발전함.
- 핵심 목적 : 장기적 가치(Value)의 수학적 극대화, **마르코프 결정 과정** (MDP) 기반의 최적 정책 도출, 미지의 환경 탐험(Exploration)과 기존 지식 활용(Exploitation) 간의 최적 균형 달성.

## Ⅱ. 강화학습(Reinforcement Learning)의 핵심 아키텍처 및 동작 메커니즘

강화학습은 에이전트와 환경 간의 상호작용 루프와 마르코프 결정 과정(MDP), **벨만 최적 방정식** (Bellman Optimality Equation)을 기반으로 동작함.

```text
[ 강화학습 에이전트-환경 상호작용 루프 ]

                    보상 (Reward, R_t)
            ┌────────────────────────────────┐
            │                                │
            ▼                                │
  +-------------------+  행동 (Action, A_t)  +-------------------+
  |   에이전트        | ──────────────────►  |    환 경          |
  |   (Agent)         |                      | (Environment)     |
  +-------------------+ ◄──────────────────  +-------------------+
                          상태 (State, S_t)

[ MDP 5대 핵심 요소 ]
1. 상태 집합 (S)     : 환경의 현재 상태 표현
2. 행동 집합 (A)     : 에이전트가 취할 수 있는 모든 행동
3. 전이 확률 (P)     : 상태 s에서 행동 a를 취했을 때 s'로 전이할 확률 P(s'|s, a)
4. 보상 함수 (R)     : 상태 s에서 행동 a 수행 시 즉각 주어지는 보상 R(s, a)
5. 할인율 (gamma, γ) : 미래 보상의 현재 가치를 감쇄시키는 비율 (0 <= γ < 1)
```

- **가치 함수(Value Function)** : 상태 가치 함수 `V(s)`와 행동 가치 함수 `Q(s, a)`로 나뉘며, 특정 상태나 행동에서 출발하여 정책을 따랐을 때 얻을 기대 누적 할인 보상 표현.
- **벨만 방정식(Bellman Equation)** : 현재의 즉각 보상과 다음 상태의 기대 가치 간의 재귀적(Recursive) 관계를 정의하여 동적 계획법(DP) 및 신경망 학습의 토대 형성.
- **탐험과 이용(Exploration vs Exploitation)** : 더 나은 보상을 찾기 위해 새로운 행동을 시도하는 탐험(Epsilon-greedy)과 현재까지 최선으로 알려진 행동을 취하는 이용 간의 상충 관계 조율.
- **정책 경사법(Policy Gradient)** : 가치 함수를 거치지 않고 신경망 파라미터 `theta`를 직접 경사 상승법(Gradient Ascent)으로 갱신하여 최적 정책 `pi_theta(a|s)`를 직접 학습.

## Ⅲ. 강화학습(Reinforcement Learning)의 세부 구성 요소 및 비교 분석

| 알고리즘 패밀리 | 핵심 메커니즘 | 장점 | 단점 및 병목 | 대표 알고리즘 |
| --- | --- | --- | --- | --- |
| **가치 기반 (Value-based)** | Q-함수를 근사하고 탐욕적(Greedy)으로 최선의 행동 선택 | 샘플 효율성이 높고 Off-Policy 학습으로 리플레이 버퍼 활용 | 이산 행동 공간에 국한, 연속 행동 공간 제어 불가 | Q-Learning, DQN, Rainbow DQN |
| **정책 기반 (Policy-based)** | 정책 자체를 확률 분포 신경망으로 직접 모델링하여 파라미터 갱신 | 연속적인 행동 공간(로봇 관절 제어) 지원, 확률적 정책 학습 | 높은 분산(Variance), 샘플 비효율성 | REINFORCE, TRPO |
| **액터-크리틱 (Actor-Critic)** | 정책을 학습하는 Actor와 가치 함수로 보상을 평가하는 Critic 결합 | 분산을 대폭 감소시키면서 안정적인 학습 및 고속 수렴 | 두 개의 신경망 동시 학습에 따른 튜닝 난이도 | A2C/A3C, PPO, SAC, DDPG |
| **모델 기반 (Model-based)** | 환경의 전이 확률과 보상 모델 자체를 신경망으로 학습하여 가상 시뮬레이션 | 극도로 높은 샘플 효율성, 상상(Imagination) 기반 계획 | 월드 모델의 오류가 정책으로 전이(Model Exploitation) | MuZero, World Models, Dreamer |

- 대규모 상용 환경 및 LLM 정렬에서는 안정성과 수렴성이 뛰어난 **PPO** (Proximal Policy Optimization) 가 사실상의 표준 알고리즘으로 안착함.

## Ⅳ. 강화학습(Reinforcement Learning)의 주요 한계점 및 해결 방안

- 수백만 번 이상의 환경 상호작용을 요구하는 극심한 샘플 비효율성(Sample Inefficiency) :
  - 한계점 : 현실 세계 로봇에 직접 적용할 경우 모터 마모, 파손, 천문학적 학습 시간 소요.
  - 해결 방안 : Isaac Gym 등 고성능 물리 시뮬레이터(Sim-to-Real), 사전 수집된 로그 데이터를 학습하는 **오프라인 강화학습** (Offline RL) 도입.
- 보상 해킹(Reward Hacking) 및 의도치 않은 비정상적 기행 학습 :
  - 한계점 : 설계자가 미처 예상하지 못한 보상 함수의 허점을 악용하여 목표는 달성하지 않고 보상 점수만 무한 루프로 획득하는 현상.
  - 해결 방안 : 정밀한 **형상화** (Reward Shaping), **역강화학습** (Inverse RL) 및 인간 피드백 기반 보상 모델(RLHF) 결합.
- 하이퍼파라미터 및 무작위 시드에 대한 극단적인 학습 불안정성 :
  - 한계점 : 동일한 코드와 데이터라도 초기화 시드에 따라 정책이 발산하거나 성능 편차가 극심함.
  - 해결 방안 : 정책 업데이트 폭을 수학적으로 제한하는 PPO 클리핑(Clipping), 다중 환경 병렬 벡터화(Vectorized Env).

## Ⅴ. 강화학습(Reinforcement Learning) 적용 및 발전을 위한 기술사적 제언

- LLM 사고 사슬(CoT) 및 추론 능력 향상을 위한 강화학습(GRPO/RL) 적극 도입 : DeepSeek-R1-Zero와 같이 지도 미세조정(SFT) 없이 대규모 강화학습만으로 모델의 자체 비평 및 추론 경로 최적화 실현.
- 로보틱스 파운데이션 모델을 위한 Sim-to-Real 도메인 무작위화(Domain Randomization) : 시뮬레이션 내의 마찰력, 조명, 무게를 무작위로 변동 학습시켜 실세계 배포 시 간극 최소화.
- 자율주행 및 기간망 제어를 위한 안전 강화학습(Safe RL) 가드레일 필수 수립 : 보상 최대화 외에 안전 제약 조건(Safety Bounds)을 라그랑주 승수법으로 수식화하여 물리적 충돌 원천 방지.
