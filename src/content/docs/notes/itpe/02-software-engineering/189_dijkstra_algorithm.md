---
title: "다익스트라 알고리즘(Dijkstra Algorithm)"
category: "02-software-engineering"
tags:
  - "다익스트라"
  - "Dijkstra"
  - "최단경로"
  - "우선순위큐"
  - "간선완화"
  - "탐욕법"
  - "OSPF"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 알고리즘과 그래프 이론을 거쳐 다익스트라 알고리즘으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>알고리즘·그래프 이론</span>
  <strong>다익스트라 알고리즘(Dijkstra Algorithm)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 간선의 가중치가 음수가 아닌 유향/무향 그래프에서 단일 시작점으로부터 도달 가능한 다른 모든 정점까지의 최단 경로를 구하기 위해, 미방문 정점 중 시작점과의 거리가 가장 짧은 노드를 탐욕적(Greedy)으로 확정하고 간선 완화(Edge Relaxation)를 반복 수행하여 $O((V+E)\log V)$ 시간에 최단 거리를 산출하는 그래프 알고리즘
- 메커니즘: 시작점 거리 0 및 타 정점 $\infty$ 초기화 $\rightarrow$ 우선순위 큐(Min-Heap)에서 최소 거리 정점 $u$ 추출 및 방문 확정 $\rightarrow$ 인접 정점 $v$ 완화 연산 수행 $\rightarrow$ 갱신된 거리 큐 삽입 및 반복
- 산출물: 최단 거리 배열(`dist[]`) · 직전 방문 선행 노드 테이블(`prev[]`) · 최단 경로 트리(SPT)

<div class="itpe-flow-map" role="img" aria-label="다익스트라 알고리즘 실행 및 간선 완화 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 거리 배열 초기화 및 시작점 적재</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>초기화</strong><span>`dist[start] = 0`, 나머지 $\infty$ 설정 후 Min-Heap에 `(0, start)` 삽입</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 최소 거리 미방문 정점 $u$ 추출 및 확정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>확정</strong><span>우선순위 큐에서 최소 비용 정점을 꺼내어 최단 거리 불변 확정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 인접 정점 $v$ 대상 간선 완화(Relaxation)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>완화</strong><span>`if (dist[v] > dist[u] + w(u,v))` 검증 후 최단 거리 단축 갱신</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 비음수 가중치 및 수렴 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>모든 간선 가중치가 비음수($w \ge 0$)이며 우선순위 큐가 공백 상태로 수렴했는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (최단 거리 산출 완결)</strong>
      <span>최단 경로 트리 확정 $\rightarrow$ OSPF 링크 상태 라우팅 테이블 반영 및 길안내</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (음수 가중치 발견)</strong>
      <span>그리디 가정 붕괴(기확정 노드 거리 번복) $\rightarrow$ 벨만-포드(Bellman-Ford)로 알고리즘 교체</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **간선 완화(Edge Relaxation)**: 정점 $u$를 거쳐 정점 $v$로 가는 경로 비용이 현재 알려진 $v$까지의 최단 거리보다 짧을 경우, $v$의 거리를 더 짧은 값으로 갱신하는 기본 연산 (`dist[v] = min(dist[v], dist[u] + w(u,v))`)
- **탐욕적 선택 속성(Greedy Choice Property)**: 현재 미방문 정점 중 최단 거리가 가장 작은 정점은 다른 우회 경로를 통해 가더라도 더 짧아질 수 없다는 불변조건에 의해 즉시 최적해로 확정하는 성질
- **우선순위 큐 (Min-Heap)**: 최소 거리를 갖는 정점을 $O(\log V)$ 시간에 고속 추출하기 위해 이진 힙 구조를 사용하는 핵심 최적화 자료구조
- **OSPF(Open Shortest Path First)**: 라우터들이 링크 상태 패킷(LSA)을 교환하여 네트워크 토폴로지 전체를 다익스트라 알고리즘으로 연산하는 인터넷 표준 내부 라우팅 프로토콜
</details>

## 1. 개요 및 필요성

### 전수 경로 탐색의 한계와 다익스트라의 탐욕적 접근

그래프에서 시작점으로부터 목적지까지 가능한 모든 경로를 하나씩 확인하는 전수 조사는 $O(V!)$의 계산 폭증을 일으킨다.

컴퓨터 과학자 에츠허르 다익스트라(Edsger Dijkstra)는 "이미 최단 거리가 확정된 정점들의 집합을 점진적으로 확장해 나가는" 탐욕적 기법을 통해, 불필요한 경로 탐색을 배제하고 $O((V+E)\log V)$ 다항 시간 내에 단일 출발점 최단 경로(SSSP)를 완벽히 찾아내는 해법을 제시하였다.

### 구현 방식별 성능 비교: 단순 배열 vs 우선순위 큐

| 비교 항목 | 단순 2차원 인접 행렬 + 배열 | 인접 리스트 + 우선순위 큐 (Min-Heap) | 피보나치 힙 (Fibonacci Heap) |
|---|---|---|---|
| **자료구조** | 1차원 거리 배열 + 2차원 인접 행렬 | 인접 리스트 + 이진 최소 힙 | 인접 리스트 + 피보나치 힙 |
| **최소 정점 탐색** | $O(V)$ 선형 탐색 | **$O(\log V)$ 힙 팝(Pop)** | $O(1)$ 분할 상환 |
| **거리 완화 갱신** | $O(1)$ 단순 대입 | **$O(\log V)$ 힙 푸시(Push)** | $O(1)$ 분할 상환 (Decrease-Key) |
| **전체 시간 복잡도**| **$O(V^2)$** | **$O((V + E) \log V)$** | **$O(E + V \log V)$** |
| **적합한 그래프** | 간선이 매우 많은 **밀집 그래프 ($E \approx V^2$)** | 일반적인 **희소 그래프 ($E \ll V^2$)** | 이론적 연구 (실무 구현 복잡) |

## 2. 아키텍처 및 핵심 메커니즘

### 간선 완화(Edge Relaxation) 메커니즘

```text
+-------------------------------------------------------------------------+
|                  다익스트라 최단 거리 완화(Relaxation) 메커니즘         |
+-------------------------------------------------------------------------+
|                                                                         |
|            [ 정점 u ] ──────── w(u, v) = 3 ────────> [ 정점 v ]         |
|                ▲                                         ▲              |
|                │                                         │              |
|           dist[u] = 4                               기존 dist[v] = 10   |
|                │                                         │              |
|                └─────────────── [ 완화 연산 ] ───────────┘              |
|                                                                         |
|         * 완화 검증 공식:                                               |
|           dist[u] + w(u, v) = 4 + 3 = 7                                 |
|           7 < 10 (기존 거리보다 우회 경로가 더 짧음!)                   |
|                                                                         |
|         * 결과: dist[v]를 7로 갱신하고 우선순위 큐에 (7, v) 푸시!        |
+-------------------------------------------------------------------------+
```

### 다익스트라 핵심 4대 구성요소

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 거리 배열 (`dist[]`)</strong></span>
      <span class="itpe-badge">최적 거리 상태</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>시작점으로부터 각 정점까지의 현재 알려진 최소 비용 기록</li>
        <li>초기값은 시작점 0, 나머지 모든 노드는 무한대($\infty$)로 설정</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 우선순위 큐 (Min-Heap)</strong></span>
      <span class="itpe-badge">탐욕적 선택</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>미방문 정점 중 거리가 가장 짧은 노드를 $O(\log V)$에 추출</li>
        <li>이미 방문 확정된 오래된 값은 스킵(Skip)하여 중복 방지</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 인접 리스트 (`adj[]`)</strong></span>
      <span class="itpe-badge">희소 그래프 최적화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>각 정점에 연결된 간선과 가중치 정보만 메모리에 효율적으로 적재</li>
        <li>불필요한 전체 정점 순회를 제거하여 $O(E)$ 탐색 실현</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 역추적 배열 (`prev[]`)</strong></span>
      <span class="itpe-badge">경로 복원</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>완화가 일어날 때마다 직전 경유 노드를 기록</li>
        <li>목적지에서 시작점까지 역추적하여 최단 경로 전체 시퀀스 복원</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 그래프에 음수 가중치 간선이 포함되어 이미 최단 거리로 확정된 정점의 거리가 번복되는 오답 발생 | 음수 가중치가 존재하는 그래프에서는 벨만-포드(Bellman-Ford) 알고리즘으로 즉시 교체 | 최단 경로 계산의 수학적 정합성 100% 보장 |
| 간선 수가 극도로 많은 완전 그래프($E \approx V^2$)에서 힙 푸시/팝 연산 누적으로 속도 저하 | 간선 밀집도에 따라 단순 1차원 배열 기반 $O(V^2)$ 구현 방식으로 알고리즘 테일러링 | 힙 자료구조 오버헤드 제거 및 연산 속도 개선 |
| 전국 단위 도로망 내비게이션 길안내 시 시작점 기준 전방위 동심원 탐색으로 연산 지연 | 목적지 방향으로 가중치를 유도하는 휴리스틱 기반 A* 알고리즘 및 양방향 다익스트라 도입 | 탐색 노드 수 90% 축소 및 응답 지연 단축 |

## 4. 기술사 답안 차별화 포인트

### OSPF(Open Shortest Path First)의 Link State Update와 연계

다익스트라 알고리즘은 현대 인터넷 백본 통신을 지탱하는 **OSPF 및 IS-IS 라우팅 프로토콜의 핵심 엔진(SPF, Shortest Path First)**이다. 모든 라우터가 LSA(Link State Advertisement)를 교환하여 동일한 링크 상태 데이터베이스(LSDB)를 공유한 뒤, 각 라우터가 자기 자신을 루트(Root)로 삼아 다익스트라 알고리즘을 독립 수행하여 루프 없는 최단 라우팅 테이블을 형성하는 실제 네트워크 연계를 답안에 강조한다.

### 양방향 다익스트라(Bidirectional Dijkstra)와 축약 계층(CH)

현대 지도 플랫폼(Google Maps, TMAP)에서는 수천만 개 교차로를 순수 다익스트라로 탐색할 수 없다. 출발지와 목적지 양쪽에서 동시에 탐색을 시작하여 중간에서 만나는 **양방향 다익스트라(탐색 공간 반경 $r$의 원 2개로 축소 $\rightarrow$ 면적 절반 감소)**와, 주요 간선도로망을 계층적으로 축약(Shortcut)해 두는 **축약 계층(Contraction Hierarchies)** 기법을 기술적 차별화로 제시한다.

## 5. 참고 및 연계 학습

- [최단경로 알고리즘 총론](./175_shortest_path_algorithm.md)
- [최단 경로 알고리즘 A*](./127_a_star_algorithm.md)
- [알고리즘 복잡도 Big-O](./125_algorithm_complexity_big_o.md)
- [최소 신장 트리(MST)](./194_minimum_spanning_tree.md)
