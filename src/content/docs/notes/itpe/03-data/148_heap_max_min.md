---
sidebar:
  order: 148
  label: "148. 힙 (Max·Min Heap)"
  badge:
    text: "B"
    variant: note
title: "힙(Heap) 자료구조와 우선순위 큐(PQ) 및 힙 정렬(Heap Sort)"
author: "OpenAI Codex"
date: "2026-09-20T18:20:00+09:00"
tags:
  - "notes-data"
weight: 148
extra:
  model: "GPT-5"
  keyword_grade: "B"
  question_no: "148"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>자료구조·알고리즘</span><strong>힙(Max·Min)</strong></div>

## 큰 그림과 30초 인출

```text
[최대 힙(Max Heap) 트리 구조와 1차원 배열 물리 매핑]

        [트리 논리 형태: 부모 >= 자식]               [1차원 배열 물리 매핑 (1-based)]
                 [90] (idx: 1)              인덱스:  [0]  [1]  [2]  [3]  [4]  [5]  [6]
                ╱    ╲                       값   :  -   [90] [70] [80] [30] [50] [60]
             [70]    [80]                                  │    │
            ╱   ╲    ╱                                     │    └── 좌: 2*2=4, 우: 2*2+1=5
         [30]  [50] [60]                                   └─────── 좌: 2*1=2, 우: 2*1+1=3
         (4)   (5)  (6)

  * 인덱스 계산 메커니즘 (CBT 특성 활용):
    - 부모 노드: Math.floor(i / 2)
    - 왼쪽 자식: 2 * i (비트 연산: i << 1)
    - 오른쪽 자식: 2 * i + 1 (비트 연산: (i << 1) | 1)
```

- 본질: **최댓값 또는 최솟값을 $O(1)$의 시간복잡도로 추출하기 위해 부모와 자식 간의 대소 관계를 유지하는 완전 이진 트리(CBT, Complete Binary Tree) 기반 자료구조로, 포인터 오버헤드 없이 1차원 연속 배열에 매핑하여 캐시 지역성(Cache Locality)과 우선순위 큐(PQ)를 구현하는 핵심 기술**
- 암기: `완-대-반-배` (완전이진트리, 대소관계, 반정렬/느슨한정렬, 배열매핑) / `업-인-다운-델` (Up-Heap 삽입, Down-Heap 삭제)
- 판단축:
  - **Max Heap**: 부모 $\ge$ 자식, 루트가 전체 최댓값 (내림차순 정렬, 상위 랭킹 추출)
  - **Min Heap**: 부모 $\le$ 자식, 루트가 전체 최솟값 (Dijkstra 최단경로, 지연 작업 스케줄링)
- 주의: 힙은 부모-자식 간 상하 대소 관계만 정의될 뿐 형제(Sibling) 노드 간 좌우 순서는 없으므로(반정렬 상태), 임의 원소 탐색은 $O(N)$의 선형 시간이 소요됨

## 예상문제

> 자료구조 힙(Heap)의 개념과 특징을 설명하고, 최대 힙(Max Heap)과 최소 힙(Min Heap)의 차이점 및 원소의 삽입(Up-Heap)과 삭제(Down-Heap) 연산 과정을 시간복잡도와 함께 제시하시오. (25점)

## Ⅰ. 최댓값·최솟값 고속 추출을 위한 힙(Heap) 개요

#### 한줄 요약: 완전 이진 트리(CBT) 구조를 활용하여 부모 노드가 항상 자식 노드보다 크거나 작도록 유지하는 반정렬(Semi-sorted) 자료구조

- **배경**: 배열이나 연결 리스트로 우선순위 큐(PQ)를 구현할 경우 삽입 또는 삭제 시 $O(N)$의 선형 탐색 비용이 발생하여 고속 처리가 불가능한 병목 해결
- **정의**: 완전 이진 트리(CBT)의 형태를 유지하면서, 부모 노드의 키와 자식 노드의 키 사이에 일정한 대소 관계를 만족하는 비선형 자료구조
- **핵심 가치**: 루트 노드에 항상 극값(Extreme Value)이 위치하여 $O(1)$에 탐색 가능하며, 삽입 및 삭제 연산은 트리 높이에 비례하는 $O(\log N)$에 완결됨

## Ⅱ. 힙의 2대 유형과 구조적 특성

#### 한줄 요약: 루트에 최댓값이 위치하는 Max Heap과 최솟값이 위치하는 Min Heap의 비교

```text
 [최대 힙 (Max Heap)]                    [최소 힙 (Min Heap)]
         [90] (Root: Max)                         [10] (Root: Min)
        ╱    ╲                                   ╱    ╲
     [70]    [80]                             [30]    [20]
     Key(Parent) >= Key(Child)                Key(Parent) <= Key(Child)
```

| 구분 | 최대 힙 (Max Heap) | 최소 힙 (Min Heap) |
|:---|:---|:---|
| **정의** | 부모 노드의 키가 자식 노드의 키보다 크거나 같은 힙 | 부모 노드의 키가 자식 노드의 키보다 작거나 같은 힙 |
| **루트 노드** | 전체 트리에서 가장 큰 값 (Maximum) | 전체 트리에서 가장 작은 값 (Minimum) |
| **응용 분야** | 내림차순 힙 정렬, OS 스케줄러(우선순위 최고 작업 할당), Top-K 랭킹 | Dijkstra 최단경로, Prim MST, 허프만 코딩, 타이머 휠 |
| **시간복잡도** | 최댓값 조회 $O(1)$, 삽입 $O(\log N)$, 삭제 $O(\log N)$ | 최솟값 조회 $O(1)$, 삽입 $O(\log N)$, 삭제 $O(\log N)$ |

## Ⅲ. 힙 연산 메커니즘: 삽입(Up-Heap)과 삭제(Down-Heap)

#### 한줄 요약: 마지막 리프에 추가 후 상향 승격하는 Up-Heap과, 루트 제거 후 마지막 원소를 내려보내는 Down-Heap

```text
 [1. 삽입 연산: Up-Heap (Percolate-Up)]
  Step 1: CBT 규칙에 따라 트리의 맨 마지막 리프 위치에 신규 노드 추가
  Step 2: 신규 노드와 부모 노드의 키 값 비교
  Step 3: 신규 노드가 부모보다 크면(Max Heap 기준) Swap 수행
  Step 4: 부모가 더 크거나 루트에 도달할 때까지 상향 반복 -> 시간: O(log N)

 [2. 삭제 연산: Down-Heap (Percolate-Down / Heapify)]
  Step 1: 루트 노드 추출 (최댓값 또는 최솟값 반환)
  Step 2: 트리의 맨 마지막 리프 노드를 빈 루트 자리로 이동
  Step 3: 자식 노드들 중 더 큰 자식(Max Heap 기준)과 비교
  Step 4: 자식이 더 크면 Swap 수행 후 하향 반복 -> 시간: O(log N)
```

| 연산 유형 | 주요 수행 단계 | 시간복잡도 | 공간복잡도 |
|:---|:---|:---:|:---:|
| **Peek (조회)** | 배열 인덱스 1번(`heap[1]`) 값을 즉시 읽어 반환 | $O(1)$ | $O(1)$ |
| **Insert (삽입)** | 마지막 인덱스에 저장 $\rightarrow$ `parent = i / 2`와 비교하며 Swap 상향 전파 | $O(\log N)$ | $O(1)$ |
| **Delete (삭제)** | 루트 추출 $\rightarrow$ 마지막 인덱스 값을 `heap[1]`에 복사 $\rightarrow$ 자식과 Swap 하향 전파 | $O(\log N)$ | $O(1)$ |
| **Build (Heapify)** | $N$개 임의 배열의 내부 노드($\lfloor N/2 \rfloor$부터 1까지) 역순 Down-Heap 적용 | $O(N)$ | $O(1)$ |

## Ⅳ. 힙(Heap)과 이진 탐색 트리(BST)의 비교

#### 한줄 요약: 극값 추출에 특화된 반정렬 힙과, 전구간 키 탐색에 특화된 전정렬 BST의 메커니즘 차이

| 비교 항목 | 힙 (Heap) | 이진 탐색 트리 (BST) |
|:---|:---|:---|
| **트리 형태** | 항상 **완전 이진 트리(CBT)** 유지 | 균형 보장 없음 (AVL, Red-Black Tree로 균형화) |
| **정렬 조건** | 부모-자식 간 상하 대소 관계만 존재 (좌우 순서 무관) | `Left Child < Parent < Right Child`의 엄격한 좌우 정렬 |
| **물리 구현** | 포인터 없는 **1차원 연속 배열** (공간 낭비 전무) | 노드당 2개 이상의 **참조 포인터(Node Pointer)** 필요 |
| **캐시 효율** | CPU L1/L2 캐시 적중률(Locality) 극도로 우수 | 포인터 추적(Pointer Chasing)으로 캐시 미스 빈번 |
| **최대/최소 탐색** | $O(1)$ (루트 노드 직결) | $O(\log N)$ (최좌측/최우측 리프까지 하향 탐색) |
| **임의 키 탐색** | $O(N)$ (전체 노드 순회 필요) | $O(\log N)$ (이진 분할 탐색) |
| **주요 목적** | 우선순위 큐(PQ), 실시간 스케줄링 | 인덱스(B-Tree 계통), 동적 사전(Dictionary) |

## Ⅴ. 힙 정렬(Heap Sort)과 힙 생성(Heapify)의 수학적 분석

#### 한줄 요약: 상향식 단일 삽입($O(N \log N)$) 대비 하향식 Heapify가 선형 시간($O(N)$)을 달성하는 수학적 근거

### 1. 상향식(Top-Down) vs 하향식(Bottom-Up) Heapify
- $N$개의 데이터를 하나씩 `Insert`하면 매번 $O(\log i)$ 소요 $\rightarrow \sum_{i=1}^N \log i \approx O(N \log N)$
- 반면, 리프 노드를 제외한 $\lfloor N/2 \rfloor$번째 노드부터 역순으로 `Down-Heap`을 적용하면:
  $$\sum_{h=0}^{\lfloor \log N \rfloor} \frac{N}{2^{h+1}} \times O(h) = O\left(N \sum_{h=0}^\infty \frac{h}{2^h}\right) = O(2N) = O(N)$$
- 따라서 초기 힙 빌드는 반드시 **Bottom-Up Heapify**를 적용해야 함

### 2. 힙 정렬 (Heap Sort) 알고리즘
1. 주어진 배열을 Bottom-Up Heapify로 최대 힙 구성 ($O(N)$)
2. 루트(최댓값)와 힙의 마지막 원소를 Swap하고 힙 크기를 1 감소
3. 새 루트에 대해 Down-Heap 수행 ($O(\log N)$)
4. 힙 크기가 1이 될 때까지 $N-1$회 반복
- **총 시간복잡도**: 최선, 평균, 최악 모두 **$O(N \log N)$** 보장 (추가 메모리 불필요, In-Place Sort)

## Ⅵ. 실무 아키텍처 응용 사례: 대용량 Top-K 스트리밍

#### 한줄 요약: 대규모 데이터셋에서 크기 $K$의 Min Heap을 유지하여 메모리 폭증 없이 상위 K개를 실시간 추출

```text
 [Top-K 스트리밍 집계 파이프라인]
  초당 100만 건 유입 ──► [크기 K의 Min Heap 유지] ──► 새 데이터 X 유입
                                 │
                 ┌───────────────┴───────────────┐
                 ▼ (X <= heap[1])                ▼ (X > heap[1])
             [즉시 폐기 (Drop)]              [루트 교체 후 Down-Heap]
             - 메모리: O(K)                  - 연산: O(log K)
             - 전체 정렬 불필요              - 상위 K개 실시간 보장
```

- **실무 문제**: 1,000만 명의 동시 접속자 중 실시간 랭킹 Top-100을 산출할 때, 매번 전체 정렬을 수행하면 CPU 100% 포화 발생
- **해결 방안**: 크기가 100인 **최소 힙(Min Heap)**을 생성하여, 루트(100위의 점수)보다 큰 점수만 힙에 교체 투입함으로써 $O(N \log K)$로 연산 비용을 99.9% 절감

## Ⅶ. 기술사적 제언: 포인터 기반 피보나치 힙(Fibonacci Heap)의 의의

#### 한줄 요약: 다익스트라(Dijkstra) 알고리즘의 키 감소(Decrease-Key) 연산을 $O(1)$ 분할 상환 시간으로 최적화하는 고급 자료구조

- **배경**: 표준 이진 힙에서 특정 노드의 가중치를 갱신하는 `Decrease-Key` 연산은 $O(\log N)$ 소요
- **피보나치 힙의 혁신**:
  - 지연 통합(Lazy Consolidation) 기법을 사용하여 트리를 즉시 병합하지 않고 루트 목록에 단순 연결
  - `Insert`, `Decrease-Key`, `Merge` 연산을 분할 상환(Amortized) **$O(1)$**에 수행
  - 네트워크 라우팅 프로토콜(OSPF) 및 대규모 그래프 탐색에서 Dijkstra 알고리즘의 시간복잡도를 $O(V \log V + E)$로 단축시키는 핵심 토대 제공

---

## 1교시 10점 답안 발췌

```text
1. 힙(Heap)의 정의
  - 최댓값/최솟값을 O(1)에 추출하기 위해 부모-자식 간 대소 관계를 유지하는 완전 이진 트리(CBT) 기반의 반정렬 자료구조.

2. 힙의 2대 유형 및 핵심 연산
  가. 유형: Max Heap(부모 >= 자식, 루트=최댓값), Min Heap(부모 <= 자식, 루트=최솟값).
  나. 핵심 연산:
    - 삽입: 마지막 리프 추가 후 부모와 비교하며 Up-Heap (O(log N)).
    - 삭제: 루트 추출 후 마지막 리프를 루트로 이동하여 자식과 비교하며 Down-Heap (O(log N)).
    - 배열 매핑: 부모=i/2, 좌측자식=2i, 우측자식=2i+1 (포인터 없는 1차원 연속 배열).

3. 힙(Heap) vs BST 비교
  - 힙은 CBT 기반 극값 추출(O(1)) 및 PQ 구현 특화, BST는 좌우 엄격 정렬 기반 임의 키 검색(O(log N)) 특화.
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제124회 정보관리 2교시: 자료구조 힙(Heap)의 개념, 유형(최대/최소 힙) 및 삽입/삭제 연산 과정
  - 제90회 기출
- **검증 출처**:
  - Thomas H. Cormen et al., "Introduction to Algorithms (CLRS 4th Edition)", Chapter 6 Heapsort
  - Robert Sedgewick, "Algorithms 4th Edition", Priority Queues

---

## 학습 체크

- [ ] 완전 이진 트리(CBT)의 1차원 배열 인덱스 매핑 공식(부모, 좌/우 자식)을 제시할 수 있는가?
- [ ] Up-Heap과 Down-Heap의 동작 절차를 도식화하고 시간복잡도를 설명할 수 있는가?
- [ ] Bottom-Up 방식의 Heapify가 $O(N)$을 달성하는 수학적 원리를 설명할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-027 트리·이진 탐색 트리](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/027_binary_search_tree.md)
- 연관 토픽: [03-058 선형 vs 비선형 자료구조](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/058_linear_vs_nonlinear_data_structures.md), [04-001 프로세스 스케줄링](file:///C:/workspace/study/src/content/docs/notes/itpe/04-computer-system/001_process_scheduling.md)
