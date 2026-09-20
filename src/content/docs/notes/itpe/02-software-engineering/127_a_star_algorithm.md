---
title: "A* 알고리즘"
category: "02-software-engineering"
tags:
  - "알고리즘"
  - "AStar"
  - "최단경로"
  - "휴리스틱"
  - "다익스트라"
  - "길찾기"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 그래프 알고리즘 및 최단 경로 탐색을 거쳐 A* 알고리즘으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>그래프 알고리즘·최단 경로</span>
  <strong>A* 알고리즘</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 다익스트라(Dijkstra) 알고리즘이 목적지 방향을 고려하지 않고 전방위 동심원으로 노드를 탐색하여 발생하는 시간·메모리 낭비를 제거하기 위해, 시작점부터의 누적 비용 $g(n)$에 목적지까지의 예측 거리인 휴리스틱 $h(n)$을 결합한 평가 함수 $f(n) = g(n) + h(n)$으로 목적지 방향을 지향하여 최단 경로를 찾아내는 휴리스틱 그래프 탐색 기법
- 메커니즘: 시작 노드 우선순위 큐(Open List) 삽입 → $f(n)$ 최소 노드 추출 및 방문 완료(Closed List) 등록 → 인접 노드 $g(n), h(n), f(n)$ 계산 및 완화(Relaxation) → 목표 노드 도달 시 부모 포인터 역추적
- 산출물: 최단 경로 노드 리스트 · 평가 함수 $f(n)$ 매트릭스 · 탐색 비용 리포트

<div class="itpe-flow-map" role="img" aria-label="A* 알고리즘 탐색 절차 및 최단 경로 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 시작 노드 초기화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설정</strong><span>시작 노드 S의 $g(S)=0$, $h(S)$ 계산 $\rightarrow$ Open List(우선순위 큐) 삽입</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 최적 노드 선택 및 확장</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>동작</strong><span>Open List에서 $f(n) = g(n) + h(n)$이 최소인 노드 $n$ 추출 $\rightarrow$ Closed List 등록</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: 목표 도달 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>추출된 노드 $n$이 목표 노드(Goal)인가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (목표 도달)</strong>
      <span>부모 포인터 역추적 $\rightarrow$ 최종 최단 경로 확정 및 반환</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (탐색 지속)</strong>
      <span>인접 노드 비용 갱신 $\rightarrow$ Open List 추가 후 2단계 반복</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **평가 함수 $f(n) = g(n) + h(n)$**: 노드 $n$을 거쳐 목표 노드에 도달할 때의 총 예상 최단 비용
- **실제 비용 $g(n)$**: 시작 노드부터 현재 노드 $n$까지 이동하는 데 소요된 실제 최단 누적 비용
- **휴리스틱 함수 $h(n)$**: 현재 노드 $n$에서 목표 노드까지 도달하는 데 필요한 예상 비용(직선 거리 등)
- **허용성(Admissibility)**: $h(n)$이 실제 목표 도달 비용 $h^*(n)$보다 결코 크지 않은($h(n) \le h^*(n)$) 성질로, 최적의 최단 경로를 보장하기 위한 필수 조건
- **일관성(Consistency/Monotonicity)**: 임의의 두 인접 노드 $n, n'$에 대해 $h(n) \le c(n, n') + h(n')$을 만족하여 한 번 Closed List에 들어간 노드는 재방문하지 않음을 보장하는 성질
</details>

## 1. 개요 및 필요성

### 다익스트라 알고리즘의 한계와 지향성 탐색

네트워크 라우팅이나 내비게이션 길찾기에서 다익스트라(Dijkstra) 알고리즘은 최적의 최단 경로를 완벽히 찾아내지만, **목적지가 어디에 있는지 전혀 고려하지 않는다.** 그 결과 목적지와 정반대 방향에 있는 노드까지 포함하여 시작점 주변의 모든 노드를 전방위 동심원 형태로 탐색하므로, 맵 크기가 커질수록 엄청난 시간과 메모리를 낭비한다.

A* 알고리즘은 다익스트라의 실제 누적 비용 $g(n)$에 목적지 방향을 가리키는 **나침반 역할의 휴리스틱 $h(n)$**을 융합하여, 탐색 방향을 목적지 쪽으로 유도(Best-First Search)함으로써 계산량을 수십~수백 배 절감하면서도 수학적으로 최단 경로를 100% 보장한다.

### 최단 경로 알고리즘 비교

| 구분 | 다익스트라 (Dijkstra) | A* 알고리즘 | 탐욕적 최상 우선 탐색 (Greedy Best-First) |
|---|---|---|---|
| **평가 함수** | $f(n) = g(n)$ ($h(n) = 0$) | $f(n) = g(n) + h(n)$ | $f(n) = h(n)$ ($g(n) = 0$) |
| **탐색 형태** | 시작점 중심 전방위 동심원 확장 | **목적지를 향한 지향성 타원형 확장** | 목적지를 향해 직선으로 돌진 |
| **최적성(최단 보장)** | **100% 최단 경로 보장** | **허용성 만족 시 100% 보장** | 최단 경로 보장 불가 (장애물 우회 시 실패) |
| **완결성** | 보장 | 보장 | 루프에 빠질 위험 존재 |
| **주요 활용 분야** | OSPF 라우팅, 전체 노드 최단거리 | 내비게이션, 게임 길찾기, 로봇 공학 | 빠른 초기 근사 경로 탐색 |

## 2. 아키텍처 및 핵심 메커니즘

### A* 알고리즘 평가 함수 구조

```text
+-------------------------------------------------------------------------+
|                  A* 알고리즘 평가 함수 f(n) = g(n) + h(n) 구조           |
+-------------------------------------------------------------------------+
|                                                                         |
|      [ 시작 노드 S ] ──────── g(n) ────────> [ 현재 노드 n ]            |
|      (출발점에서 n까지 이동한 실제 누적 비용)                            |
|                                                     :                   |
|                                                     : h(n)              |
|                                                     v (예측 휴리스틱)   |
|                                              [ 목표 노드 G ]            |
|                                                                         |
|  * 최적성 보장의 핵심 원리:                                             |
|    - 허용성: h(n) <= h*(n) (절대 실제 잔여 거리보다 과대평가하지 않음) |
|    - h(n) = 0 이면 다익스트라(Dijkstra)와 정확히 일치함                 |
|    - h(n)이 실제 거리 h*(n)에 가까울수록 탐색 영역이 직선으로 수렴함     |
+-------------------------------------------------------------------------+
```

### A* 알고리즘 4대 핵심 자료구조 및 연산

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 열린 목록 (Open List)</strong></span>
      <span class="itpe-badge">탐색 후보군</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>탐색 대상 후보 노드들을 보관하는 최소 힙(Min-Heap) 우선순위 큐</li>
        <li>$f(n)$ 값이 가장 작은 노드를 $O(\log N)$ 시간에 즉시 추출</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 닫힌 목록 (Closed List)</strong></span>
      <span class="itpe-badge">방문 완료</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>이미 최단 거리 계산과 이웃 노드 확장이 완료된 노드 집합</li>
        <li>해시셋(HashSet)으로 구현하여 $O(1)$ 시간에 중복 방문 여부 확인</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 휴리스틱 거리 함수</strong></span>
      <span class="itpe-badge">비용 추정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>맨해튼 거리: 4방향 이동 그리드($|x_1 - x_2| + |y_1 - y_2|$)</li>
        <li>유클리드 거리: 8방향 또는 자유 회전 평면($\sqrt{\Delta x^2 + \Delta y^2}$)</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 경로 역추적 (Backtracking)</strong></span>
      <span class="itpe-badge">결과 산출</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>각 노드가 자신을 방문하게 만든 부모 노드(Parent Pointer) 기록</li>
        <li>목표 도달 시 Goal부터 Start까지 포인터를 따라가며 최단 경로 복원</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 대각선 이동이 가능한 격자 지도에서 맨해튼 거리를 휴리스틱으로 사용하여 최단 경로 탐색 실패 | 이동 제약에 부합하는 허용적 휴리스틱인 옥타일(Octile) 거리 또는 유클리드 거리 적용 | 허용성($h \le h^*$) 회복 및 수학적 최적 최단 경로 100% 보장 |
| 대규모 맵에서 수백만 개 노드가 Open List에 쌓여 메모리 고갈(OutOfMemory) 발생 | 직선 이동 경로를 건너뛰는 JPS(Jump Point Search) 또는 계층적 맵 분할(HPA*) 도입 | 메모리 점유율 90% 절감 및 탐색 속도 10배 향상 |
| 장애물이 ㄷ자 형태로 깊게 파인 함정 구간에서 수만 번의 불필요한 탐색 루프 발생 | 사전 계산된 가시성 그래프(Visibility Graph) 또는 웨이포인트(Waypoint) 내비게이션 메시 연동 | 함정 구간 내 불필요한 노드 확장 방지 및 실시간 응답성 유지 |

## 4. 기술사 답안 차별화 포인트

### 휴리스틱 허용성(Admissibility)과 일관성(Consistency)의 수리적 증명

답안 서술 시 "휴리스틱을 쓰면 빠르다"는 피상적 서술을 넘어, **왜 과대평가하지 않아야($h(n) \le h^*(n)$) 최적성이 보장되는가**를 삼각부등식과 함께 명시한다. 만약 $h(n)$이 실제 거리보다 크면, 알고리즘은 더 짧은 우회 경로가 있음에도 해당 노드의 $f(n)$이 너무 커서 탐색 우선순위에서 배제하여 최단 경로를 놓치게 된다. 또한 일관성($h(n) \le c(n, n') + h(n')$)이 만족되면 한 번 Closed List에 들어간 노드를 절대 재방문할 필요가 없어 탐색 속도가 획기적으로 향상됨을 강조한다.

### JPS(Jump Point Search)와의 실무 결합 제언

게임 개발, 자율주행 AGV 로봇 등 실시간 격자(Grid) 환경에서는 순수 A* 알고리즘의 노드 확장 오버헤드가 치명적이다. 대칭적인 빈 공간을 한 칸씩 탐색하지 않고, 장애물 모서리나 방향 전환 지점(Jump Point)으로 한 번에 수십 칸을 점프하는 **JPS 알고리즘**을 결합하여, 메모리와 CPU 연산량을 극적으로 단축시키는 실무 최적화 기법을 3단락 또는 결론으로 제시한다.

## 5. 참고 및 연계 학습

- [다익스트라 알고리즘](./189_dijkstra_algorithm.md)
- [최소 신장 트리(MST)](./194_minimum_spanning_tree.md)
- [탐욕(Greedy) 알고리즘](./196_greedy_algorithm.md)
- [알고리즘 복잡도 Big-O](./125_algorithm_complexity_big_o.md)
