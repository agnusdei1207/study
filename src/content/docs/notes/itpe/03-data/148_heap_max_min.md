---
sidebar:
  order: 148
  label: "148. 힙 (Max·Min Heap)"
  badge:
    text: "기초"
    variant: note
title: "힙(Heap) 자료구조와 우선순위 큐(PQ) 및 힙 정렬(Heap Sort)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 148
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "148"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>자료구조·알고리즘</span><span>트리 구조</span><strong>힙(Max·Min Heap)</strong></div>

## 큰 그림과 30초 인출

```text
[최대 힙(Max Heap) 트리 논리 형태 및 1차원 배열 물리 매핑]

        [완전 이진 트리(CBT) 논리 구조]          [1차원 연속 배열 물리 매핑 (1-based)]
                 [90] (idx: 1)             인덱스: [0]  [1]  [2]  [3]  [4]  [5]  [6]
                ╱    ╲                      값   :  -   [90] [70] [80] [30] [50] [60]
             [70]    [80]                                 │    │
            ╱   ╲    ╱                                    │    └── 좌: 2*2=4, 우: 2*2+1=5
         [30]  [50] [60]                                  └─────── 좌: 2*1=2, 우: 2*1+1=3
         (4)   (5)  (6)

  * 인덱스 계산 공식 (포인터 오버헤드 0% 달성):
    - 부모 노드: Math.floor(i / 2)
    - 왼쪽 자식: 2 * i (비트 연산: i << 1)
    - 오른쪽 자식: 2 * i + 1 (비트 연산: (i << 1) | 1)
```

- 본질: **힙은 우선순위가 가장 높은 원소를 빠르게 찾는 완전 이진 트리 기반 자료구조로, 부모와 자식 사이의 힙 순서만 유지해 최대·최소 원소 조회를 O(1), 삽입·삭제를 O(log n)에 지원**
- 암기: `완-대-반-배` (완전이진트리, 대소관계, 반정렬, 1차원배열매핑) / `업-인-다운-델` (Up-Heap 삽입, Down-Heap 삭제)
- 판단축:
  - **Max Heap**: 부모 $\ge$ 자식, 루트가 전체 최댓값 (내림차순 정렬, 상위 Top-K 추출).
  - **Min Heap**: 부모 $\le$ 자식, 루트가 전체 최솟값 (Dijkstra 최단경로, Prim MST, 지연 타이머 휠).
- 주의: 힙은 부모-자식 간 상하 대소 관계만 정의될 뿐 형제(Sibling) 노드 간 좌우 순서는 없으므로(반정렬 상태), 임의 원소 탐색은 $O(N)$의 선형 시간이 소요됨
---

## 1교시 예상문제 (10점)

> 힙의 정의와 목적, 완전 이진 트리 및 힙 순서의 구조, 기본 연산을 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **정의** | 최댓값/최솟값을 $O(1)$에 추출하기 위해 부모-자식 간 대소 관계를 유지하는 완전 이진 트리(CBT) 기반 반정렬 자료구조 |
| **배열 매핑** | 1-based: 부모 = `⌊i/2⌋`, 좌측 자식 = `2i`, 우측 자식 = `2i+1`; 0-based 구현은 별도 인덱스 식 사용 |
| **핵심 연산** | ① 삽입(Up-Heap, $O(\log N)$): 맨 끝 리프 추가 후 부모와 비교 승격 / ② 삭제(Down-Heap, $O(\log N)$): 루트 반환 후 마지막 원소를 루트로 이동하여 강등 |
| **힙 vs BST** | 힙은 루트 극값 조회와 우선순위 큐에 적합 / 균형 이진 탐색 트리는 키 순서 검색·범위 탐색에 적합 |
| **실무 제언** | 상위 K개 유지에는 크기 K 힙을 활용해 전체 정렬보다 적은 메모리로 후보를 관리 |
---

### 핵심 관계

| 구분 | 최대 힙 (Max Heap) | 최소 힙 (Min Heap) |
|:---|:---|:---|
| **정의** | 부모 노드의 키 $\ge$ 자식 노드의 키 | 부모 노드의 키 $\le$ 자식 노드의 키 |
| **루트 노드** | 트리 내 **최댓값 (Maximum)** 위치 ($heap[1]$) | 트리 내 **최솟값 (Minimum)** 위치 ($heap[1]$) |
| **시간복잡도** | 최댓값 조회 $O(1)$, 삽입/삭제 $O(\log N)$ | 최솟값 조회 $O(1)$, 삽입/삭제 $O(\log N)$ |
| **주요 응용** | 내림차순 힙 정렬, OS 최고 우선순위 프로세스 선점, Top-K 랭킹 | Dijkstra 최단경로, Prim 최소신장트리(MST), 타이머 휠 이벤트 스케줄러 |
| **정렬 연계** | 오름차순(Ascending) 정렬 시 최대 힙 구성 후 역순 배치 | 내림차순(Descending) 정렬 시 최소 힙 활용 |

---

## 2~4교시 예상문제 (25점)

> 자료구조 힙(Heap)의 개념과 특징을 설명하고, 최대 힙(Max Heap)과 최소 힙(Min Heap)의 차이점 및 원소의 삽입(Up-Heap)과 삭제(Down-Heap) 연산 과정을 시간복잡도와 함께 제시하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 최댓값·최솟값 고속 추출을 위한 힙(Heap) 개요

#### 한줄 요약: 완전 이진 트리(CBT) 구조를 활용하여 부모 노드가 항상 자식 노드보다 크거나 작도록 유지하는 반정렬 자료구조

- **배경**:
  - 일반 배열이나 연결 리스트로 우선순위 큐(Priority Queue)를 구현할 경우 삽입 또는 삭제 연산 중 하나는 반드시 $O(N)$의 선형 탐색 비용이 발생하여 고속 처리가 불가능한 병목 발생
  - 극값(최댓값/최솟값) 탐색을 $O(1)$에 처리하고, 삽입과 삭제를 $O(\log N)$에 완결하기 위한 트리 구조 필요
- **정의**:
  - 완전 이진 트리(CBT)의 형태적 특성을 유지하면서, 부모 노드의 키와 자식 노드의 키 사이에 일정한 대소 관계를 엄격히 만족하는 비선형 자료구조
- **핵심 가치**:
  - 루트 노드에 항상 전체의 극값(Extreme Value)이 위치하여 $O(1)$ 즉시 참조 가능
  - 연결 리스트 포인터가 불필요하여 1차원 배열로 완벽히 사상되며, CPU L1/L2 캐시 지역성(Spatial Locality) 극대화

### Ⅱ. 힙의 트리 논리 구조와 1차원 배열 물리 매핑 아키텍처

<div class="itpe-diagram-box">
  <div class="itpe-diagram-header">
    <span class="itpe-tag">아키텍처 다이어그램</span>
    <span class="itpe-title">최대 힙(Max Heap)의 완전 이진 트리 구조 및 1차원 배열 물리 인덱스 사상</span>
  </div>
  <div class="itpe-diagram-body">
    <svg class="itpe-svg" viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-heap" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--color-text, #333)" />
        </marker>
      </defs>
      <!-- 좌측: 논리 트리 구조 -->
      <text x="130" y="25" font-size="13" font-weight="bold" text-anchor="middle" fill="var(--color-primary, #0284c7)">[트리 논리 구조 (CBT)]</text>
      <!-- 간선들 -->
      <line x1="130" y1="55" x2="80" y2="105" stroke="var(--color-border, #94a3b8)" stroke-width="2" />
      <line x1="130" y1="55" x2="180" y2="105" stroke="var(--color-border, #94a3b8)" stroke-width="2" />
      <line x1="80" y1="125" x2="50" y2="175" stroke="var(--color-border, #94a3b8)" stroke-width="2" />
      <line x1="80" y1="125" x2="110" y2="175" stroke="var(--color-border, #94a3b8)" stroke-width="2" />
      <line x1="180" y1="125" x2="160" y2="175" stroke="var(--color-border, #94a3b8)" stroke-width="2" />

      <!-- 노드들 (원형) -->
      <!-- 루트 (1) -->
      <circle cx="130" cy="45" r="18" fill="#dbeafe" stroke="#2563eb" stroke-width="2" />
      <text x="130" y="50" font-size="12" font-weight="bold" text-anchor="middle" fill="#1e40af">90</text>
      <text x="130" y="20" font-size="9" text-anchor="middle" fill="#2563eb">[1]</text>

      <!-- 2레벨 (2, 3) -->
      <circle cx="80" cy="115" r="16" fill="#f1f5f9" stroke="#64748b" stroke-width="2" />
      <text x="80" y="119" font-size="11" font-weight="bold" text-anchor="middle" fill="#1e293b">70</text>
      <text x="60" y="115" font-size="9" text-anchor="middle" fill="#64748b">[2]</text>

      <circle cx="180" cy="115" r="16" fill="#f1f5f9" stroke="#64748b" stroke-width="2" />
      <text x="180" y="119" font-size="11" font-weight="bold" text-anchor="middle" fill="#1e293b">80</text>
      <text x="200" y="115" font-size="9" text-anchor="middle" fill="#64748b">[3]</text>

      <!-- 3레벨 (4, 5, 6) -->
      <circle cx="50" cy="185" r="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
      <text x="50" y="189" font-size="10" font-weight="bold" text-anchor="middle" fill="#334155">30</text>
      <text x="32" y="185" font-size="9" text-anchor="middle" fill="#94a3b8">[4]</text>

      <circle cx="110" cy="185" r="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
      <text x="110" y="189" font-size="10" font-weight="bold" text-anchor="middle" fill="#334155">50</text>
      <text x="128" y="185" font-size="9" text-anchor="middle" fill="#94a3b8">[5]</text>

      <circle cx="160" cy="185" r="14" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5" />
      <text x="160" y="189" font-size="10" font-weight="bold" text-anchor="middle" fill="#334155">60</text>
      <text x="178" y="185" font-size="9" text-anchor="middle" fill="#94a3b8">[6]</text>

      <!-- 우측: 1차원 배열 물리 매핑 -->
      <text x="380" y="25" font-size="13" font-weight="bold" text-anchor="middle" fill="var(--color-primary, #0284c7)">[1차원 배열 물리 매핑 (1-Based)]</text>

      <!-- 배열 테이블 헤더 및 셀 -->
      <rect x="255" y="45" width="250" height="50" rx="4" fill="var(--color-bg-secondary, #f0f4f8)" stroke="var(--color-border, #0284c7)" stroke-width="1" />
      <!-- 구분선들 -->
      <line x1="290" y1="45" x2="290" y2="95" stroke="#cbd5e1" stroke-width="1" />
      <line x1="326" y1="45" x2="326" y2="95" stroke="#cbd5e1" stroke-width="1" />
      <line x1="362" y1="45" x2="362" y2="95" stroke="#cbd5e1" stroke-width="1" />
      <line x1="398" y1="45" x2="398" y2="95" stroke="#cbd5e1" stroke-width="1" />
      <line x1="434" y1="45" x2="434" y2="95" stroke="#cbd5e1" stroke-width="1" />
      <line x1="470" y1="45" x2="470" y2="95" stroke="#cbd5e1" stroke-width="1" />
      <line x1="255" y1="70" x2="505" y2="70" stroke="#cbd5e1" stroke-width="1" />

      <!-- 인덱스 번호 -->
      <text x="272" y="62" font-size="10" text-anchor="middle" fill="#64748b">[0]</text>
      <text x="308" y="62" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb">[1]</text>
      <text x="344" y="62" font-size="10" text-anchor="middle" fill="#64748b">[2]</text>
      <text x="380" y="62" font-size="10" text-anchor="middle" fill="#64748b">[3]</text>
      <text x="416" y="62" font-size="10" text-anchor="middle" fill="#64748b">[4]</text>
      <text x="452" y="62" font-size="10" text-anchor="middle" fill="#64748b">[5]</text>
      <text x="488" y="62" font-size="10" text-anchor="middle" fill="#64748b">[6]</text>

      <!-- 저장된 값 -->
      <text x="272" y="86" font-size="11" text-anchor="middle" fill="#94a3b8">-</text>
      <text x="308" y="86" font-size="11" font-weight="bold" text-anchor="middle" fill="#1e40af">90</text>
      <text x="344" y="86" font-size="11" text-anchor="middle" fill="#1e293b">70</text>
      <text x="380" y="86" font-size="11" text-anchor="middle" fill="#1e293b">80</text>
      <text x="416" y="86" font-size="11" text-anchor="middle" fill="#334155">30</text>
      <text x="452" y="86" font-size="11" text-anchor="middle" fill="#334155">50</text>
      <text x="488" y="86" font-size="11" text-anchor="middle" fill="#334155">60</text>

      <!-- 인덱스 수식 박스 -->
      <rect x="255" y="110" width="250" height="95" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
      <text x="265" y="130" font-size="11" font-weight="bold" fill="#0f172a">인덱스 연산 수식 (비트 연산 최적화):</text>
      <text x="265" y="150" font-size="10" fill="#334155">• 부모 노드: Math.floor(i / 2)  (i >> 1)</text>
      <text x="265" y="170" font-size="10" fill="#334155">• 좌측 자식: 2 * i               (i &lt;&lt; 1)</text>
      <text x="265" y="190" font-size="10" fill="#334155">• 우측 자식: 2 * i + 1           ((i &lt;&lt; 1) | 1)</text>

      <!-- 하단 설명 배너 -->
      <rect x="20" y="225" width="480" height="42" rx="4" fill="#ecfdf5" stroke="#10b981" stroke-width="1" />
      <text x="260" y="243" font-size="11" font-weight="bold" text-anchor="middle" fill="#065f46">핵심 메커니즘: 완전 이진 트리(CBT) 특성상 빈 공간(Hole)이 없으므로 배열에 1:1 매핑됨</text>
      <text x="260" y="258" font-size="10" text-anchor="middle" fill="#047857">포인터 변수 낭비가 전혀 없고 캐시 지역성(Spatial Locality)이 극도로 우수함</text>
    </svg>
  </div>
  <div class="itpe-diagram-footer">
    CBT의 빈틈없는 구조 덕분에 배열 인덱스의 2배 및 1/2 계산만으로 트리 탐색을 수행하여 포인터 역참조 오버헤드를 원천 제거함
  </div>
</div>

### Ⅲ. 힙의 2대 유형: 최대 힙(Max Heap) vs 최소 힙(Min Heap)

#### 한줄 요약: 루트 노드에 전체 최댓값이 위치하는 Max Heap과 최솟값이 위치하는 Min Heap의 비교

| 구분 | 최대 힙 (Max Heap) | 최소 힙 (Min Heap) |
|:---|:---|:---|
| **정의** | 부모 노드의 키 $\ge$ 자식 노드의 키 | 부모 노드의 키 $\le$ 자식 노드의 키 |
| **루트 노드** | 트리 내 **최댓값 (Maximum)** 위치 ($heap[1]$) | 트리 내 **최솟값 (Minimum)** 위치 ($heap[1]$) |
| **시간복잡도** | 최댓값 조회 $O(1)$, 삽입/삭제 $O(\log N)$ | 최솟값 조회 $O(1)$, 삽입/삭제 $O(\log N)$ |
| **주요 응용** | 내림차순 힙 정렬, OS 최고 우선순위 프로세스 선점, Top-K 랭킹 | Dijkstra 최단경로, Prim 최소신장트리(MST), 타이머 휠 이벤트 스케줄러 |
| **정렬 연계** | 오름차순(Ascending) 정렬 시 최대 힙 구성 후 역순 배치 | 내림차순(Descending) 정렬 시 최소 힙 활용 |

### Ⅳ. 힙 핵심 연산: 삽입(Up-Heap)과 삭제(Down-Heap)

#### 한줄 요약: 리프에 추가 후 상향 승격하는 Up-Heap과, 루트 제거 후 마지막 원소를 내려보내는 Down-Heap

```text
[1. 원소 삽입 (Up-Heap / Percolate-Up)]
  - Step 1: CBT 규칙 유지를 위해 트리의 맨 마지막 리프(배열의 size + 1)에 신규 노드 추가
  - Step 2: 신규 노드와 부모 노드(i / 2)의 키 값 비교
  - Step 3: 신규 노드가 부모보다 크면(Max Heap 기준) Swap 수행
  - Step 4: 부모가 더 크거나 루트에 도달할 때까지 상향 반복 ──► 시간복잡도: O(log N)

[2. 원소 삭제 (Down-Heap / Percolate-Down / Heapify)]
  - Step 1: 루트 노드(최댓값/최솟값) 추출 및 반환
  - Step 2: 트리의 맨 마지막 리프 노드를 빈 루트 자리(heap[1])로 이동 및 힙 크기 1 감소
  - Step 3: 루트 자리로 온 노드와 두 자식 노드(2*i, 2*i+1) 중 더 큰 자식과 비교
  - Step 4: 자식이 더 크면 Swap 수행 후 리프 방향으로 하향 반복 ──► 시간복잡도: O(log N)
```

| 연산 유형 | 주요 수행 단계 | 시간복잡도 | 공간복잡도 |
|:---|:---|:---:|:---:|
| **Peek (극값 조회)** | 배열 1번 인덱스(`heap[1]`) 값을 즉시 읽어 반환 | $O(1)$ | $O(1)$ |
| **Insert (삽입)** | 마지막 인덱스에 저장 $\rightarrow$ `parent = i >> 1`과 비교하며 Swap 상향 전파 | $O(\log N)$ | $O(1)$ |
| **Delete (삭제)** | 루트 추출 $\rightarrow$ 마지막 인덱스 값을 `heap[1]`에 복사 $\rightarrow$ 자식과 Swap 하향 전파 | $O(\log N)$ | $O(1)$ |
| **Build (Heapify)** | $N$개 임의 배열의 내부 노드($\lfloor N/2 \rfloor$부터 1까지) 역순 Down-Heap 적용 | $O(N)$ | $O(1)$ |

### Ⅴ. 힙(Heap)과 이진 탐색 트리(BST) 비교

#### 한줄 요약: 극값 추출에 특화된 반정렬 힙과, 전구간 키 탐색에 특화된 전정렬 BST의 구조적 차이

| 비교 항목 | 힙 (Heap) | 이진 탐색 트리 (BST) |
|:---|:---|:---|
| **트리 형태** | 항상 **완전 이진 트리(CBT)** 형태 엄격 유지 | 형태 보장 없음 (AVL, Red-Black Tree로 균형화 필수) |
| **정렬 조건** | 부모-자식 간 상하 대소 관계만 성립 (좌우 순서 무관, 반정렬) | `Left < Parent < Right`의 엄격한 좌우 전정렬 |
| **물리적 저장** | 포인터가 필요 없는 **1차원 연속 배열** 매핑 | 노드당 2개 이상의 **메모리 참조 포인터** 필수 |
| **캐시 지역성** | 배열 연속 할당으로 CPU L1/L2 캐시 적중률 극대화 | 포인터 체이싱(Pointer Chasing)으로 인한 캐시 미스 빈번 |
| **최대/최소 탐색** | **$O(1)$** (루트 노드 직결) | $O(\log N)$ (최좌측/최우측 리프까지 하향 순회) |
| **임의 키 탐색** | **$O(N)$** (반정렬 상태이므로 전수 순회 필요) | **$O(\log N)$** (이진 분할 탐색) |
| **주요 활용** | 우선순위 큐(PQ), 실시간 작업 스케줄링, Top-K 스트리밍 | 데이터베이스 인덱스(B-Tree 계통), 동적 사전(Dictionary) |

### Ⅵ. 힙 정렬(Heap Sort)과 하향식 Heapify의 수학적 분석

#### 한줄 요약: 단순 단일 삽입 반복($O(N \log N)$) 대비 하향식 Heapify가 선형 시간($O(N)$)을 달성하는 수학적 원리

### 1. 상향식 단일 삽입 vs 하향식 Bottom-Up Heapify
- $N$개의 임의 데이터를 빈 힙에 하나씩 `Insert`하면 매번 $O(\log i)$ 소요:
  $$\sum_{i=1}^N \log i \approx O(N \log N)$$
- 반면, 주어진 $N$개 배열을 그대로 두고 리프 노드를 제외한 내부 노드인 $\lfloor N/2 \rfloor$번째부터 1번 루트까지 역순으로 `Down-Heap`을 적용하면:
  - 높이 $h$에 있는 노드의 수는 최대 $\lceil N/2^{h+1} \rceil$개이며, 각 노드의 이동 거리는 $h$임
  $$\text{Total Work} = \sum_{h=0}^{\lfloor \log N \rfloor} \frac{N}{2^{h+1}} \times O(h) = O\left(N \sum_{h=0}^\infty \frac{h}{2^h}\right) = O(2N) = O(N)$$
- 따라서 정렬되지 않은 임의 배열로부터 힙을 초기 구축(Build Heap)할 때는 반드시 **하향식 Bottom-Up Heapify**를 적용해야 함

### 2. 힙 정렬 (Heap Sort) 알고리즘과 복잡도
1. 주어진 입력 배열을 Bottom-Up Heapify로 최대 힙 구성 ($O(N)$).
2. 루트 노드(최댓값)와 힙의 마지막 원소를 교환(Swap)하고 힙의 유효 크기를 1 감소.
3. 교환되어 루트로 이동한 새 원소에 대해 Down-Heap을 수행하여 힙 성질 복원 ($O(\log N)$).
4. 힙의 크기가 1이 될 때까지 $N-1$회 반복.
- **복잡도 판정**: 최선, 평균, 최악 모두 **$O(N \log N)$**의 시간복잡도를 완벽히 보장하며, 추가 메모리가 필요 없는 제자리 정렬(In-Place Sort)임. 단, 동일 키의 상대적 위치가 보존되지 않는 **불안정 정렬(Unstable Sort)**임.

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 힙은 "완벽한 정렬을 포기함으로써 극값 추출의 극단적 속도($O(1)$)를 얻어낸" 엔지니어링 타협의 정수이다. 모든 키를 정렬하려면 $O(N \log N)$이 들지만, "지금 당장 처리해야 할 1등 작업"만 필요한 스케줄러나 랭킹 시스템에서는 전체 정렬이 불필요한 낭비이다. 기술사 답안에서는 힙의 CBT 특성과 1차원 배열 인덱스 매핑 공식을 비트 연산(`>> 1`, `<< 1`)과 연계하여 하드웨어 친화적 특성을 부각하고, 실무에서 대용량 스트리밍 데이터를 처리할 때 "크기 $K$의 Min Heap을 유지하여 메모리 폭증 없이 실시간 Top-K를 추출하는 파이프라인 아키텍처"를 제시하면 최상위 득점을 얻을 수 있다.

> **[나라면 이렇게 쓴다]**
> 1교시형 문제라면 CBT 트리 구조와 1차원 배열 매핑 SVG 다이어그램, Up-Heap/Down-Heap 절차, 힙 vs BST 비교표를 간결하고 밀도 있게 구성하겠다. 2교시형 문제라면 Build Heap의 $O(N)$ 수학적 유도 과정을 수식으로 명확히 입증하고, 실시간 분산 스트리밍 환경에서 전체 데이터를 메모리에 올리지 않고 크기 $K$의 최소 힙만으로 처리하는 Top-K 아키텍처와, Dijkstra의 키 감소 연산을 $O(1)$ 분할 상환 시간으로 최적화하는 피보나치 힙(Fibonacci Heap)의 의의를 기술사적 제언으로 연결하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 초당 수십만 건의 이벤트 스트림에서 상위 랭킹(Top-K)을 산출할 때, 매번 전체 정렬(`Arrays.sort`)을 수행하면 CPU 100% 포화 및 메모리 고갈(OOM)이 발생함.
- **대응**: 크기가 $K$로 고정된 최소 힙(Min Heap)을 메모리에 유지하여, 신규 데이터 유입 시 루트(현재 $K$위 점수)와 비교 후 $O(\log K)$로 교체 투입하는 슬라이딩 윈도우 힙 아키텍처를 적용함.
- **검증**: 분할 상환 연산 프로파일링을 통해 힙 크기 $K$ 대비 메모리 점유율을 상시 모니터링하고, 그래프 탐색 가중치 갱신 빈도가 높을 경우 피보나치 힙(Fibonacci Heap) 도입 타당성을 벤치마크함.
- **효과**: 정렬 연산 시간복잡도를 $O(N \log N)$에서 $O(N \log K)$로 99% 이상 단축하고, 메모리 사용량을 $O(N)$에서 $O(K)$로 고정 격리 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <span class="step-num">1. 현행 한계</span>
    <span class="step-title">전체 정렬 연산 병목</span>
    <span class="step-desc">대용량 스트리밍 데이터 유입 시 매번 전체 정렬을 수행하여 CPU 포화 및 응답 지연</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">2. 개선 방안</span>
    <span class="step-title">크기 K Min-Heap 파이프라인</span>
    <span class="step-desc">크기 K의 Min Heap을 유지하여 루트(K위)보다 큰 값만 교체 갱신하는 메모리 격리</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">3. 검증 기준</span>
    <span class="step-title">처리량 및 힙 높이 감시</span>
    <span class="step-desc">초당 유입 TPS 대비 다운힙 수행 지연율 진단 및 O(log K) 상수 시간 유지 검증</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">4. 실행 효과</span>
    <span class="step-title">실시간 Top-K 고속 추출</span>
    <span class="step-desc">연산 비용 99% 절감 및 메모리 O(K) 고정 기반 무중단 실시간 랭킹 서빙 체계 확립</span>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제124회 정보관리 2교시: 자료구조 힙(Heap)의 개념, 유형(최대/최소 힙) 및 삽입/삭제 연산 과정
  - 제90회 정보관리 1교시: 우선순위 큐와 힙 자료구조
- **검증 출처**:
  - Thomas H. Cormen et al., "Introduction to Algorithms (CLRS 4th Edition)", Chapter 6 Heapsort
  - Robert Sedgewick & Kevin Wayne, "Algorithms 4th Edition", Section 2.4 Priority Queues
  - Donald E. Knuth, "The Art of Computer Programming Vol 3: Sorting and Searching"
---

## 연결 토픽

- 상위 토픽: [03-027 트리·이진 탐색 트리](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/027_binary_search_tree.md)
- 선수 토픽: [03-058 선형 vs 비선형 자료구조](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/058_linear_vs_nonlinear_data_structures.md)
- 후속 토픽: [04-001 프로세스 스케줄링](file:///C:/workspace/study/src/content/docs/notes/itpe/04-computer-system/001_process_scheduling.md), [03-149 분산 데이터베이스](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/149_distributed_database.md)
