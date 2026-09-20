---
title: "그리디 알고리즘(Greedy Algorithm)"
category: "02-software-engineering"
tags:
  - "탐욕알고리즘"
  - "그리디알고리즘"
  - "Greedy"
  - "지역최적해"
  - "전역최적해"
  - "탐욕적선택속성"
  - "최적부분구조"
  - "근사알고리즘"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 알고리즘 설계 패러다임을 거쳐 그리디 알고리즘으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>알고리즘 설계 패러다임</span>
  <strong>그리디 알고리즘(Greedy Algorithm)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 전체 경우의 수를 전수 검토하거나 이전 선택을 되돌아보지 않고, 매 의사결정 단계마다 당장 눈앞에 보이는 가장 최적의 선택(지역 최적해)을 직진하듯 결정해 나감으로써, '탐욕적 선택 속성'과 '최적 부분 구조'를 만족하는 문제에 대해 다항 시간 내에 전역 최적해(Global Optimum)를 도출하는 고속 알고리즘 설계 패러다임
- 메커니즘: 현재 기준 국소 최적 선택(Selection) $\rightarrow$ 시스템 제약조건 충족 검사(Feasibility) $\rightarrow$ 전체 문제 해결 검사(Solution) $\rightarrow$ 전역 최적성 및 근사비 검증
- 산출물: 최적 의사결정 시퀀스 · 자원 최적화 할당 결과서 · 근사비(Approximation Ratio) 검증 리포트

<div class="itpe-flow-map" role="img" aria-label="그리디 알고리즘 3단계 절차 및 최적성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 선택 절차 (Selection Procedure)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>선택</strong><span>현재 상태에서 특정 기준(예: 최소 비용, 빠른 종료시간)상 가장 유리한 해 선택</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 적절성 검사 (Feasibility Check)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>검증</strong><span>새로 선택된 요소가 문제의 제약조건(시간 중복, 무게 한도 등)을 위반하지 않는지 확인</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 해답 검사 (Solution Check)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>완결</strong><span>모든 입력 처리가 끝나고 전체 문제의 목표가 달성되었는지 확인</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 전역 최적성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>탐욕적 선택 속성과 최적 부분 구조가 성립하여 지역 최적해가 전역 최적해와 일치하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (전역 최적해 확정)</strong>
      <span>알고리즘 수렴 $\rightarrow$ $O(n \log n)$ 고속 최적해 도출 (다익스트라, 크루스칼 완결)</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (지역 최적해 함정)</strong>
      <span>전역 최적해 실패 $\rightarrow$ 동적 계획법(DP) 또는 백트래킹(Branch & Bound)으로 전환</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **탐욕적 선택 속성(Greedy Choice Property)**: 앞선 단계의 탐욕적 선택이 이후의 선택에 나쁜 영향을 주지 않으며, 매 순간의 최선의 선택이 전체 문제의 전역 최적해로 반드시 이어진다는 성질
- **최적 부분 구조(Optimal Substructure)**: 전체 문제의 최적해가 그 안에 포함된 하위 부분 문제들의 최적해들로 구성되는 수학적 성질
- **지역 최적해(Local Optimum) vs 전역 최적해(Global Optimum)**: 당장 현재 단계에서의 부분적 최선책과, 전체 문제 전체를 놓고 보았을 때의 진정한 최종 최적해
- **근사 알고리즘(Approximation Algorithm)**: NP-Hard와 같이 다항 시간 내에 최적해를 구하기 어려운 복잡한 문제에 대해, 그리디 기법을 적용하여 이론적으로 증명된 오차 범위 내의 실용적인 해를 고속 도출하는 기법
</details>

## 1. 개요 및 필요성

### 전수 탐색의 지수 복잡도 한계와 탐욕적 선택의 효용

경우의 수가 기하급수적으로 증가하는 최적화 문제에서 모든 상태 트리를 탐색하는 완전 탐색($O(2^n), O(n!)$)은 실시간 시스템에서 사용이 불가능하다.

그리디 알고리즘은 **"미래를 따지지 않고 당장 눈앞의 최선을 선택"**하는 극단적 단순성과 빠른 연산 속도($O(n \log n)$)를 무기로, 최적해 조건이 수학적으로 증명된 영역(MST, 최단 경로, 허프만 코딩)에서 절대적인 엔지니어링 위력을 발휘한다.

### 최적 알고리즘 설계 4대 패러다임 비교

| 구분 | 그리디 (Greedy) | 동적 계획법 (DP) | 분할 정복 (Divide & Conquer) | 백트래킹 (Backtracking) |
|---|---|---|---|---|
| **선택 메커니즘** | **매 순간 당장 최선인 것 단 1개만 선택** | 모든 소문제의 최적해를 비교/취합 | 문제를 독립된 부분으로 쪼개어 정복 | 가능성을 탐색하다 막히면 되돌아감 |
| **하위 문제 중복**| 하위 문제 중복 없음 | **하위 문제가 빈번하게 중복됨** | 하위 문제가 서로 독립적임 | 상태 공간 트리를 깊이 우선 탐색 |
| **메모이제이션** | **불필요 (이전 선택 캐싱 없음)** | **필수 (DP 테이블에 결과 저장)** | 불필요 | 불필요 (방문 상태 원복) |
| **시간 복잡도** | **매우 빠름 (정렬 $O(n \log n)$)** | 다항 시간 ($O(n^2), O(n \cdot W)$) | $O(n \log n)$ | 지수 시간 ($O(2^n), O(n!)$) |
| **대표 문제** | 다익스트라, 크루스칼, 회의실 배정 | 피보나치, 0/1 배낭, 최장 공통 부분 수열 | 병합 정렬, 퀵 정렬, 이진 탐색 | N-Queen, 미로 찾기, 스도쿠 |

## 2. 아키텍처 및 핵심 메커니즘

### 지역 최적해의 함정과 전역 최적해 괴리

```text
+-------------------------------------------------------------------------+
|                  지역 최적해(Local) vs 전역 최적해(Global)              |
+-------------------------------------------------------------------------+
|                                                                         |
|                          [ 시작 상태 ]                                  |
|                           ／        ＼                                  |
|                       (A: 이득 10)   (B: 이득 5)                        |
|                         │                │                              |
|                         ▼ (그리디 선택: 당장 큰 10 선택!)               |
|                     [ 상태 A ]        [ 상태 B ]                        |
|                      ／    ＼          ／     ＼                        |
|                   (C: +1) (D: +2)   (E: +50) (F: +100)                  |
|                     │                  │                                |
|                     ▼                  ▼                                |
|                 총이득 = 12       총이득 = 105 (전역 최적해 놓침!)      |
|                                                                         |
|  * 교훈: 탐욕적 선택 속성이 증명되지 않은 문제에 그리디를 적용하면      |
|          당장의 이익에 눈이 멀어 거대한 전역 최적해를 놓치게 됨         |
+-------------------------------------------------------------------------+
```

### 대표적인 그리디 성공 및 실패 문제

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 활동 선택 문제</strong></span>
      <span class="itpe-badge">성공 (최적 보장)</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>회의실 하나에 가장 많은 회의를 배정하는 문제</li>
        <li>"종료 시간이 가장 빠른 회의"를 탐욕적으로 선택하면 항상 최적해</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 허프만 압축 코딩</strong></span>
      <span class="itpe-badge">성공 (최적 보장)</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>문자 빈도수에 따라 가변 길이 비트 코드를 할당하는 무손실 압축</li>
        <li>빈도가 가장 낮은 두 노드를 탐욕적으로 묶어 최적 접두어 트리 구성</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 동전 거스름돈 문제</strong></span>
      <span class="itpe-badge">조건부 성공</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>동전 단위가 서로 배수 관계(500, 100, 50, 10)일 때만 그리디 성공</li>
        <li>배수 관계가 깨지면(예: 60원 추가) 그리디는 오답을 내며 DP 필수</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 0/1 배낭 vs 분할 배낭</strong></span>
      <span class="itpe-badge">조건부 성공</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>물건을 쪼갤 수 있는 분할 배낭(Fractional)은 무게당 가치 그리디 성공</li>
        <li>물건을 쪼갤 수 없는 0/1 배낭(Knapsack)은 그리디 불가, DP 필수</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 동전 단위가 서로 배수 관계가 아닐 때(예: 10원, 50원, 60원에서 80원 거슬러주기) 최소 동전 수 산출 실패 | 동전 단위가 비배수인 화폐 체계에서는 동적 계획법(DP)으로 알고리즘 전면 교체 | 최소 동전 수 100% 정확 산출 보장 |
| 물건을 쪼갤 수 없는 0/1 Knapsack 문제에 가치 대비 무게 비율로 그리디를 적용하여 가치 손실 | 0/1 배낭 문제는 2차원 DP 테이블로 풀고, 물건을 쪼갤 수 있는 분할 가능 배낭에만 그리디 적용 | 최적 자원 적재 및 손실 방지 |
| NP-Hard 문제에 휴리스틱 그리디 적용 시 특정 엣지 케이스에서 오차율 폭증 | 근사비(Approximation Ratio)가 수학적으로 증명된 근사 알고리즘(Christofides 등) 적용 | 최악의 경우에도 오차 한계 내 성능 통제 |

## 4. 기술사 답안 차별화 포인트

### 수학적 정당성 증명: 교환 논법(Exchange Argument)과 매트로이드

그리디 알고리즘의 정당성을 증명하는 표준 수학적 기법으로 **교환 논법(Exchange Argument)**을 강조한다. 어떤 임의의 최적해가 존재한다고 가정하고, 그 해의 첫 번째 선택을 그리디 알고리즘의 선택으로 '교환'하더라도 해의 품질이 나빠지지 않음을 귀납적으로 증명하는 방식이다. 또한 대수학의 **매트로이드(Matroid)** 구조를 만족하는 부분 집합 시스템에서는 그리디 알고리즘이 언제나 전역 최적해를 도출함을 이론적 근거로 제시한다.

### 클라우드 인프라 실시간 스케줄링의 사실상 표준

실무 클라우드 인프라(쿠버네티스 Kube-Scheduler, AWS 오토스케일링)에서는 수십만 대의 노드와 파드를 스케줄링할 때 엄밀한 전역 최적해를 찾느라 시간을 지체할 수 없다. 당장 CPU/메모리 여유율이 가장 높은 노드를 밀리초 내에 찾아 파드를 배치하는 **그리디 기반의 가중치 휴리스틱 스케줄러가 대규모 분산 시스템의 실무 표준**임을 결론으로 제시한다.

## 5. 참고 및 연계 학습

- [최단경로 알고리즘 총론](./175_shortest_path_algorithm.md)
- [다익스트라 알고리즘(Dijkstra)](./189_dijkstra_algorithm.md)
- [최소신장트리(MST)](./194_minimum_spanning_tree.md)
- [알고리즘 복잡도 Big-O](./125_algorithm_complexity_big_o.md)
