---
title: "몬테카를로 트리 탐색 MCTS(Monte Carlo Tree Search)"
date: "2026-09-20T11:00:00+09:00"
tags:
  - "notes-basic-theory"
sidebar:
  badge:
    text: "B · 기출 · 60%"
extra:
  source_status: "기출"
  source_history: "135회"
  priority: 60
  priority_note: "[출제:135]"
---

## 답안 골격
```text
[MCTS] ◀━━ 머리: Ⅶ 내 의견 (신경망 가치망과 하이브리드 결합을 통한 롤아웃 연산 병목 제거)
 ┃
 ┣━ Ⅰ 개요 ───── 방대한 게임 상태 트리 한계 → 무작위 시뮬레이션(롤아웃)과 통계 기반의 비대칭적 휴리스틱 트리 탐색
 ┣━ Ⅱ 4단계 ──── 선택(Selection: UCB1) → 확장(Expansion) → 시뮬레이션(Simulation/Rollout) → 역전파(Backpropagation)
 ┣━ Ⅲ 수식 ───── UCB1 = $\bar{X}_j + C \sqrt{\frac{\ln n}{n_j}}$ (활용 Exploitation + 탐색 Exploration 균형)
 ┣━ Ⅳ 흐름 ───── 4단계 루프 반복을 통한 방문 횟수 $N(s, a)$ 및 가치 $Q(s, a)$ 누적 수렴
 ┣━ Ⅴ 비교 ───── Minimax(Alpha-Beta Pruning) vs MCTS (정적 평가 함수 필수 vs 시뮬레이션 기반 범용 평가)
 ┗━ Ⅵ 실무 ───── 알파고(AlphaGo) 착수 결정 · 자율주행 차량 경로 계획 · 다중 에이전트 전술 의사결정
```
- 필수 키워드: 선택(Selection) · 확장(Expansion) · 시뮬레이션(Simulation) · 역전파(Backpropagation) · UCB1(Upper Confidence Bound)
- 배점 전략: 10점 = Ⅰ 개요 → Ⅱ 4단계 라이프사이클 도해 → Ⅲ UCB1 수식 및 변수 의미 → Ⅴ 미니맥스와의 비교

## 한 줄 본질
- 완벽한 휴리스틱 평가 함수를 만들 수 없는 초거대 상태 공간 탐색 한계 해결 → UCB1 공식으로 유망 노드를 편향 선택하고 무작위 롤아웃 결과로 노드 가치를 역전파 갱신 → 비대칭적 고효율 트리 탐색 / 무작위 시뮬레이션 연산 비용

## 핵심 그림
```text
 1. 선택(Selection)   2. 확장(Expansion)   3. 시뮬레이션(Simulation)  4. 역전파(Backprop)
       [Root]               [Root]                [Root]                 [Root] (N+1, Q+v)
       /    \               /    \                /    \                 /    \
     ( )    [ ]           ( )    [ ]            ( )    [ ]             ( )    [ ]
            /                    /                     /                      /
          *( )*                ( )                   ( )                    ( ) (N+1, Q+v)
         (UCB1)                 |                     |                      ^
                               [New]                 [New]                   |
                                                       | (무작위 롤아웃)       |
                                                      ( )                    |
                                                       |                     |
                                                      [승리/패배: v] --------'
```

## 핵심 통찰
- 미니맥스(Minimax) 알고리즘은 인간 전문가가 작성한 정적 평가 함수(Evaluation Function)에 절대적으로 의존하지만, MCTS는 게임 종료 시점까지의 시뮬레이션 승패 통계만으로 스스로 가치를 평가하므로 도메인 지식 의존성을 탈피함
- UCB1 공식의 앞 항($\bar{X}_j$)은 승률이 높은 노드를 집중적으로 파고드는 '활용(Exploitation)'을, 뒷 항($C \sqrt{\ln n / n_j}$)은 방문 횟수가 적은 미지의 노드를 살펴보는 '탐색(Exploration)'을 제어함
- 바둑과 같이 분기 계수(Branching Factor)가 수백에 달하는 게임에서 트리를 대칭적으로 모두 펼치지 않고 승률이 높은 분기만 깊게 파고드는 비대칭적 트리 성장(Asymmetric Tree Growth)을 달성함

## 이웃 토픽과 구분
- MCTS vs Minimax (Alpha-Beta 가지치기):
| 비교 항목 | MCTS (Monte Carlo Tree Search) | Minimax (알파-베타 가지치기) |
|---|---|---|
| 평가 메커니즘 | 시뮬레이션 결과의 통계적 평균(승률) | 중간 리프 노드의 정적 평가 함수 |
| 트리 성장 형태 | 유망한 경로 위주의 비대칭적 확장 | 정해진 깊이까지의 전면적 대칭 탐색 |
| 적합 도메인 | 평가 함수 작성이 어려운 바둑, 전략 게임 | 평가 함수가 명확한 체스, 틱택토 |

## 문제·원인·대책
- 적용 상황: 복잡한 교통 교차로 자율주행 차량 경로 의사결정
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 실시간 제어 주기(수십 ms) 내 탐색 미완료 | 무작위 롤아웃 시뮬레이션의 스텝 수가 길어 지연 시간 초과 | 시뮬레이션 끝까지 가지 않고 사전 학습된 가치 신경망(Value Network)으로 즉시 평가 | 연산 지연 단축 및 실시간성 확보 |
| 초기 무작위 탐색 시 비현실적 경로 진입 | 도메인 물리 법칙을 무시한 완전 무작위 롤아웃으로 인한 평가 노이즈 | 정책망(Policy Network)을 통한 상위 후보 액션 필터링(PUCT 적용) | 탐색 효율 및 유효성 향상 |

## 이렇게 출제된다
- 제135회 1교시: "몬테카를로 트리 탐색(MCTS)의 4단계 및 UCB1 알고리즘의 역할" → 요구 포인트: Selection-Expansion-Simulation-Backpropagation 도식, UCB1 수식 유도, 활용과 탐색의 트레이드오프

## 내 의견
- [신경망 가치망과 하이브리드 결합을 통한 롤아웃 연산 병목 제거] 순수 MCTS는 끝까지 시뮬레이션을 수행해야 하므로 컴퓨팅 자원 소모가 막대하고 상태 공간이 깊은 현실 문제에서 시간 내 수렴이 불가능함 → 나라면: 알파고 제로(AlphaGo Zero) 아키텍처와 같이 롤아웃 시뮬레이션을 제거하고 잔차 신경망(ResNet) 기반의 가치망(Value Net)과 정책망(Policy Net)을 결합한 PUCT 알고리즘을 도입하여 1회의 신경망 순전파로 상태 가치와 사전 확률을 즉시 인출하도록 최적화
