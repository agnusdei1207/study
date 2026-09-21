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
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
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
      <span>SPT 최단 경로 트리 완성 $\rightarrow$ OSPF 라우팅 테이블 및 네비게이션 경로 반영</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (음수 가중치 감지)</strong>
      <span>알고리즘 교체 $\rightarrow$ 벨만-포드(Bellman-Ford) 또는 SPFA 알고리즘으로 즉시 전환</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **간선 완화(Edge Relaxation)**: 기존에 알려진 정점 $v$까지의 최단 거리(`dist[v]`)보다, 정점 $u$를 거쳐 가는 경로(`dist[u] + w(u,v)`)가 더 짧을 때 거리 값을 더 작은 값으로 갱신하는 핵심 연산
- **탐욕적 선택 속성(Greedy Choice)**: 현재 시점에서 시작점과 가장 가까운 미방문 정점을 선택하면, 이후 다른 경로를 통해 그 정점에 도달하더라도 결코 거리가 줄어들지 않는다는 확정 원리 (음수 간선 부재 전제)
- **최소 힙(Min-Heap)**: 정점 선택에 걸리는 시간을 $O(V)$에서 $O(\log V)$로 단축시켜, 전체 알고리즘 시간복잡도를 $O(V^2)$에서 $O((V+E)\log V)$로 혁신하는 자료구조
- **OSPF(Open Shortest Path First)**: 인터넷 라우터 간에 링크 상태(Link-State) 정보를 교환한 후, 각 라우터가 목적지 네트워크까지의 최단 패킷 전달 경로를 계산하기 위해 다익스트라 알고리즘을 사용하는 대표적 표준 라우팅 프로토콜
</details>

## 1. 개요 및 필요성

### 최적 경로 탐색의 수학적 기초와 다익스트라의 등장

네트워크 패킷 라우팅, GPS 내비게이션, 물류 배송 경로 최적화 등 수많은 현대 IT 인프라는 "가장 적은 비용으로 목적지에 도달하는 최단 경로"를 실시간으로 찾아야 한다.

에츠허르 다익스트라(Edsger Dijkstra)가 고안한 이 알고리즘은 **동적 계획법(DP)과 탐욕법(Greedy)의 원리를 융합**하여, 시작점으로부터의 거리를 하나씩 불변 값으로 확정해 나가는 방식으로 최단 경로를 산출한다. 간선 가중치가 모두 0 이상인 환경에서 가장 빠른 수행 성능을 보장한다.

### 최단 경로 4대 알고리즘 특성 비교

| 구분 | 다익스트라 (Dijkstra) | 벨만-포드 (Bellman-Ford) | 플로이드-워셜 (Floyd-Warshall) | A* (에이스타) 알고리즘 |
|---|---|---|---|---|
| **경로 범위** | **단일 시작점 $\rightarrow$ 모든 정점** | 단일 시작점 $\rightarrow$ 모든 정점 | **모든 정점 쌍 간 (All-Pairs)** | **단일 시작점 $\rightarrow$ 단일 목적지** |
| **음수 간선 허용** | **절대 불가 ($w \ge 0$ 필수)** | **허용 (음수 사이클 감지)** | 허용 (음수 사이클 감지) | 불가 ($w \ge 0$ 필수) |
| **시간 복잡도** | **$O((V+E)\log V)$** | $O(VE)$ | $O(V^3)$ | 휴리스틱에 따라 상이 (평균 빠름) |
| **핵심 알고리즘** | **탐욕법 + 우선순위 큐** | 전체 간선 $V-1$회 완화 (DP) | 거쳐가는 정점 $k$ 3중 루프 (DP) | 다익스트라 + 휴리스틱 함수 $h(n)$ |
| **대표 활용처** | **OSPF 라우터, 네트워크 토폴로지** | RIP 라우팅, 금융 차익 거래 탐지 | 전사 네트워크 정점 간 거리 행렬 | 게임 길찾기, 로봇 자율주행 |

## 2. 아키텍처 및 핵심 메커니즘

### 간선 완화(Edge Relaxation) 메커니즘

다익스트라 알고리즘의 심장은 정점 $u$를 경유할 때 정점 $v$의 거리가 단축되는지를 검증하는 간선 완화 연산이다.

<div class="itpe-diagram-container" role="img" aria-label="다익스트라 간선 완화 연산 전후의 최단 거리 단축 메커니즘">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: var(--color-surface, #1e293b); }
      .box { fill: var(--color-surface-card, #334155); stroke: var(--color-border, #475569); stroke-width: 1.2; rx: 5; }
      .box-active { fill: var(--color-primary-subtle, rgba(56,189,248,0.12)); stroke: var(--color-primary, #38bdf8); stroke-width: 1.5; rx: 5; }
      .title { fill: var(--color-text-strong, #f8fafc); font-family: system-ui, sans-serif; font-size: 9.5px; font-weight: 700; }
      .h-text { fill: var(--color-primary, #38bdf8); font-family: system-ui, sans-serif; font-size: 8px; font-weight: 700; }
      .text { fill: var(--color-text, #e2e8f0); font-family: system-ui, sans-serif; font-size: 7px; }
      .muted { fill: var(--color-text-muted, #94a3b8); font-family: system-ui, sans-serif; font-size: 6.2px; }
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-dj); }
    </style>
    <marker id="arrow-dj" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">간선 완화(Edge Relaxation) 메커니즘: dist[v] &gt; dist[u] + w(u, v)</text>

  <!-- 왼쪽: 완화 전 상태 -->
  <rect x="16" y="34" width="236" height="172" class="box"/>
  <text x="24" y="50" class="h-text">[상태 1: 완화 연산 이전]</text>
  
  <circle cx="50" cy="90" r="18" class="box-active"/>
  <text x="44" y="94" class="h-text">u</text>
  <text x="36" y="122" class="muted">dist[u] = 4</text>

  <circle cx="190" cy="90" r="18" class="box"/>
  <text x="184" y="94" class="text">v</text>
  <text x="174" y="122" class="muted">dist[v] = 10</text>

  <line x1="68" y1="90" x2="172" y2="90" class="arrow"/>
  <text x="110" y="82" fill="#38bdf8" font-size="7px">가중치 w(u,v) = 3</text>

  <rect x="24" y="136" width="220" height="60" class="box"/>
  <text x="30" y="152" class="text">비교 연산:</text>
  <text x="30" y="166" class="text">기존 dist[v] = 10</text>
  <text x="30" y="180" class="h-text">경유 경로 = dist[u] + w(u,v) = 4 + 3 = 7</text>
  <text x="30" y="191" fill="#ef4444" font-size="6.5px">▶ 10 &gt; 7 이므로 더 짧은 경로 발견!</text>

  <!-- 오른쪽: 완화 후 상태 -->
  <rect x="268" y="34" width="236" height="172" class="box-active"/>
  <text x="276" y="50" class="h-text">[상태 2: 완화 연산 완료 (Relaxed)]</text>

  <circle cx="302" cy="90" r="18" class="box-active"/>
  <text x="296" y="94" class="h-text">u</text>
  <text x="288" y="122" class="muted">dist[u] = 4</text>

  <circle cx="442" cy="90" r="18" class="box-active"/>
  <text x="436" y="94" class="h-text">v</text>
  <text x="424" y="122" fill="#38bdf8" font-size="6.8px" font-weight="bold">dist[v] = 7</text>

  <line x1="320" y1="90" x2="424" y2="90" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow-dj)"/>
  <text x="362" y="82" fill="#38bdf8" font-size="7px">가중치 w(u,v) = 3</text>

  <rect x="276" y="136" width="220" height="60" class="box"/>
  <text x="282" y="152" class="text">상태 갱신 결과:</text>
  <text x="282" y="166" class="text">1. dist[v] = 7 로 단축 업데이트</text>
  <text x="282" y="180" class="text">2. 직전 선행자 prev[v] = u 기록</text>
  <text x="282" y="191" class="h-text">3. Min-Heap에 (7, v) 새 원소 푸시</text>
</svg>
</div>

### 우선순위 큐(Min-Heap) 기반 다익스트라 실행 절차

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>1. 초기화 (Initialization)</strong></span>
      <span class="itpe-badge">거리 0 설정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>출발 노드 $S$의 최단 거리를 `dist[S] = 0`, 나머지 모든 노드는 $\infty$로 초기화</li>
        <li>우선순위 큐(Min-Heap)에 `(거리 0, 노드 S)` 삽입</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>2. 최소 비용 추출 (Pop Min)</strong></span>
      <span class="itpe-badge">탐욕적 확정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>우선순위 큐에서 거리가 가장 작은 `(d, u)`를 꺼냄</li>
        <li>이미 방문 처리되었거나 `d > dist[u]`이면 무시(스킵)</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>3. 인접 노드 완화 (Relaxation)</strong></span>
      <span class="itpe-badge">거리 갱신</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>확정된 노드 $u$에 연결된 모든 인접 노드 $v$에 대해 `dist[u] + w(u,v)` 계산</li>
        <li>새 경로가 기존 `dist[v]`보다 짧으면 `dist[v]`를 갱신하고 큐에 삽입</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>4. 종료 및 역추적 (Reconstruction)</strong></span>
      <span class="itpe-badge">경로 완성</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>우선순위 큐가 빌 때까지 반복하여 최단 경로 트리(SPT) 완성</li>
        <li>목적지에서 `prev[]` 배열을 역추적하여 실제 최단 주행 경로 복원</li>
      </ul>
    </div>
  </div>
</div>

### 우선순위 큐 기반 3단계 탐색 및 최단 경로 트리(SPT) 완성

힙 구조를 통해 매 단계 최소 거리 노드를 즉각 추출하는 동작 아키텍처이다.

<div class="itpe-diagram-container" role="img" aria-label="우선순위 큐를 이용한 다익스트라 노드 확정 및 최단 경로 트리 구성도">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: var(--color-surface, #1e293b); }
      .box { fill: var(--color-surface-card, #334155); stroke: var(--color-border, #475569); stroke-width: 1.2; rx: 5; }
      .box-active { fill: var(--color-primary-subtle, rgba(56,189,248,0.12)); stroke: var(--color-primary, #38bdf8); stroke-width: 1.5; rx: 5; }
      .title { fill: var(--color-text-strong, #f8fafc); font-family: system-ui, sans-serif; font-size: 9.5px; font-weight: 700; }
      .h-text { fill: var(--color-primary, #38bdf8); font-family: system-ui, sans-serif; font-size: 8px; font-weight: 700; }
      .text { fill: var(--color-text, #e2e8f0); font-family: system-ui, sans-serif; font-size: 7px; }
      .muted { fill: var(--color-text-muted, #94a3b8); font-family: system-ui, sans-serif; font-size: 6.2px; }
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-dj2); }
    </style>
    <marker id="arrow-dj2" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">우선순위 큐(Min-Heap) 기반 최단 경로 트리(SPT) 산출 파이프라인</text>

  <!-- 단계 1 -->
  <rect x="16" y="36" width="150" height="166" class="box"/>
  <text x="24" y="52" class="h-text">1. Min-Heap 최솟값 팝</text>
  <rect x="24" y="60" width="134" height="42" class="box-active"/>
  <text x="30" y="76" class="text">큐 맨 앞 (d, u) 추출</text>
  <text x="30" y="88" class="muted">O(log V) 시간에 최단 노드 선택</text>
  <text x="24" y="122" class="muted">• 현재 미방문 정점 중 최소</text>
  <text x="24" y="136" class="muted">• 탐욕법에 의해 dist[u] 확정</text>
  <text x="24" y="150" class="muted">• 방문 완료(Visited) 마킹</text>
  <text x="24" y="176" class="muted">▶ 불변값으로 영구 고정</text>
  <line x1="166" y1="110" x2="186" y2="110" class="arrow"/>

  <!-- 단계 2 -->
  <rect x="186" y="36" width="156" height="166" class="box-active"/>
  <text x="194" y="52" class="h-text">2. 인접 간선 완화 연산</text>
  <rect x="194" y="60" width="140" height="42" class="box"/>
  <text x="200" y="76" class="text">인접 노드 v 전수 순회</text>
  <text x="200" y="88" class="muted">dist[v] &gt; dist[u] + w(u,v)</text>
  <text x="194" y="122" class="muted">• 단축 가능한 이웃 노드 탐색</text>
  <text x="194" y="136" class="muted">• dist[v] 새 최단값 갱신</text>
  <text x="194" y="150" class="muted">• 힙에 (new_dist, v) 삽입</text>
  <text x="194" y="176" class="muted">▶ O(E log V) 복잡도 처리</text>
  <line x1="342" y1="110" x2="362" y2="110" class="arrow"/>

  <!-- 단계 3 -->
  <rect x="362" y="36" width="142" height="166" class="box"/>
  <text x="370" y="52" class="h-text">3. 최단 경로 트리 완성</text>
  <rect x="370" y="60" width="126" height="42" class="box-active"/>
  <text x="376" y="76" class="text">최종 SPT 도출</text>
  <text x="376" y="88" class="muted">모든 정점 최단거리 확정</text>
  <text x="370" y="122" class="muted">• prev[] 역추적으로 경로 복원</text>
  <text x="370" y="136" class="muted">• OSPF 포워딩 테이블 반영</text>
  <text x="370" y="150" class="muted">• 전체 수행 O((V+E)log V)</text>
  <text x="370" y="176" class="muted">▶ 글로벌 최적해 보장</text>
</svg>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 금융 차익 거래나 네트워크 경로에 음수 가중치 간선이 존재할 때 다익스트라 실행 시 오답 산출 | 그래프 전처리 단계에서 음수 간선 존재 여부를 검사하고, 발견 시 벨만-포드(Bellman-Ford)로 분기 | 알고리즘 오류 100% 방지 및 정확한 음수 사이클 감지 |
| 순진한 배열 기반 $O(V^2)$ 구현으로 수십만 개 노드를 가진 도로망에서 내비게이션 멈춤 현상 | 바이너리 힙 또는 피보나치 힙 기반 우선순위 큐를 도입하여 $O((V+E)\log V)$로 시간 단축 | 경로 계산 시간 99% 단축 (수 초 ➔ 수 밀리초) |
| Min-Heap에 갱신 전의 과거 거리 정보가 남아 메모리 낭비 및 불필요한 중복 연산 발생 | 큐에서 추출 시 `if (cur_dist > dist[u]) continue;` 가지치기(Pruning) 조건을 반드시 삽입 | 힙 메모리 사용량 60% 절감 및 수행 속도 2배 향상 |

## 4. 기술사 답안 차별화 포인트

### OSPF 라우팅 프로토콜과 다익스트라의 실무적 구현

네트워크 엔지니어링에서 다익스트라는 단순한 코딩 테스트용 알고리즘이 아니라 **인터넷 백본을 지탱하는 OSPF(Open Shortest Path First) 라우팅 프로토콜의 핵심 엔진**이다. 각 라우터는 LSA(Link-State Advertisement) 패킷을 교환하여 전체 네트워크 토폴로지 데이터베이스(LSDB)를 구축한 후, 자신을 루트(Root)로 삼아 다익스트라 알고리즘을 실행함으로써 넥스트 홉(Next-Hop) 포워딩 테이블을 동적 생성한다는 실무 인프라 연계를 서술한다.

### 대규모 내비게이션을 위한 다익스트라의 진화: A* 알고리즘 및 축약 계층(CH)

현대 티맵, 카카오내비 등 전국 단위 도로망(수천만 노드)에서는 순수 다익스트라만으로 실시간 길찾기가 불가능하다. 답안에서는 목적지 방향으로의 유클리드 거리를 휴리스틱으로 더해 탐색 범위를 원뿔형으로 좁히는 **A* (A-Star) 알고리즘**과, 고속도로 중심의 계층 그래프를 사전 빌드하여 연산량을 줄이는 **축약 계층(Contraction Hierarchies, CH)**으로의 최신 최적화 발전 방향을 제시한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 다익스트라 알고리즘의 핵심은 "음수 간선이 없다면, 현재 가장 가까운 놈은 앞으로 어떤 경로로 돌아와도 더 가까워질 수 없다"는 탐욕적 확정성이다. 이 조건이 깨지면 다익스트라는 무너지고 벨만-포드가 등판해야 한다.
- [나라면]: 1교시형 단답 시 간선 완화(Relaxation) 공식과 우선순위 큐 기반 4단계 메커니즘을 명확한 수식과 함께 제시하겠다. 2교시형 서술에서는 4대 최단경로 알고리즘(다익스트라, 벨만-포드, 플로이드-워셜, A*)을 목적/음수허용/복잡도로 비교하고, 인터넷 백본 OSPF 라우팅과 전국 도로망 내비게이션 축약 계층(CH) 실무 적용 사례를 기술사적 식견으로 보여주겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 간선 가중치 $w \ge 0$ 만족 여부 사전 검증률 100% 및 대규모 그래프($V > 10^5$) 탐색 지연시간 50ms 이하 달성 여부
- **대응 방안**: 그래프 모델링 시 우선순위 큐(Min-Heap) 기반 다익스트라를 기본 채택하고, 목적지가 정해진 내비게이션은 A* 및 CH 계층화 기법 적용
- **검증 체계**: 비음수 가중치 정적 검증 ➔ Min-Heap 가지치기 유효성 확인 ➔ OSPF 토폴로지 수렴 시험 ➔ 대규모 벤치마크
- **기대 효과**: 네트워크 패킷 최적 전송 경로 실시간 확보, 라우팅 루프 방지 및 대규모 위치 기반 서비스(LBS) 응답성 극대화

<div class="itpe-pipeline-container" role="img" aria-label="다익스트라 최단 경로 산출 파이프라인">
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">01</div>
    <div class="itpe-pipeline-step-content">
      <strong>비음수 가중치 검증</strong>
      <span>간선 가중치 $w \ge 0$ 확인 및 거리 무한대 배열 초기화</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">02</div>
    <div class="itpe-pipeline-step-content">
      <strong>우선순위 큐 추출</strong>
      <span>Min-Heap에서 최소 비용 정점 $u$ 탐욕적 확정</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">03</div>
    <div class="itpe-pipeline-step-content">
      <strong>간선 완화 및 갱신</strong>
      <span>이웃 노드 $v$ 거리 단축 시 갱신 후 큐 재삽입</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">04</div>
    <div class="itpe-pipeline-step-content">
      <strong>최단 경로 트리 완성</strong>
      <span>SPT 기반 OSPF 라우팅 테이블 및 최적 경로 산출</span>
    </div>
  </div>
</div>

## 5. 참고 및 연계 학습

- [최단 경로 알고리즘 비교](./175_shortest_path_algorithm.md)
- [최소 신장 트리(MST)](./194_minimum_spanning_tree.md)
- [탐욕 알고리즘(Greedy)](./196_greedy_algorithm.md)
- [방향 비순환 그래프(DAG)](./143_dag.md)
