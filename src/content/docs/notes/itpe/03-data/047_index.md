---
sidebar:
  order: 47
  label: "047. 인덱스 (Index)"
  badge:
    text: "A"
    variant: note
title: "데이터베이스 인덱스 (Index) 및 클러스터드·논클러스터드 인덱스"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 47
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "047"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>물리적 데이터베이스 설계·튜닝</span><strong>인덱스</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-box" role="img" aria-label="데이터베이스 인덱스 탐색 및 클러스터드 대 논클러스터드 비교 개요도">
<svg viewBox="0 0 520 230" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-idx" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
    <filter id="shadow-idx" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="rgba(0,0,0,0.1)"/>
    </filter>
  </defs>

  <!-- SELECT 질의 -->
  <rect x="15" y="15" width="490" height="35" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5" filter="url(#shadow-idx)"/>
  <text x="260" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">클라이언트 SELECT 질의 (WHERE 조건절 조건 검색)</text>
  <text x="260" y="44" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">테이블 풀 스캔 O(N) 대신 B+Tree 인덱스 수직 탐색 O(log N) 수행</text>

  <path d="M 260 50 L 260 70" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2" marker-end="url(#arrow-idx)"/>

  <!-- B+Tree 인덱스 탐색 계층 -->
  <rect x="15" y="70" width="490" height="42" rx="6" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="260" y="87" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">B+Tree 계층 인덱스 탐색 구조</text>
  <text x="260" y="102" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">[루트 블록 Root] ──▶ [브랜치 블록 Branch] ──▶ [리프 블록 Leaf (양방향 링크)]</text>

  <!-- 분기 경로 -->
  <path d="M 145 112 L 145 130" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-idx)"/>
  <path d="M 375 112 L 375 130" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-idx)"/>

  <!-- 좌측: 클러스터드 -->
  <rect x="15" y="132" width="235" height="55" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="132" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">클러스터드 인덱스 (Clustered)</text>
  <text x="132" y="165" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">- 리프 블록 = 실제 데이터 행 자체 (사전식)</text>
  <text x="132" y="177" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="#10b981" text-anchor="middle">물리적 정렬 일치 · 테이블당 1개 · 랜덤 I/O 0회</text>

  <!-- 우측: 논클러스터드 -->
  <rect x="270" y="132" width="235" height="55" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5"/>
  <text x="387" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">논클러스터드 인덱스 (Non-Clustered)</text>
  <text x="387" y="165" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">- 리프 블록 = 인덱스 키 + 물리 주소(RID/PK)</text>
  <text x="387" y="177" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="#ef4444" text-anchor="middle">논리적 정렬 · 테이블당 복수 개 · 힙 테이블 랜덤 I/O</text>

  <!-- 하단 트레이드오프 바 -->
  <rect x="15" y="195" width="490" height="24" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="260" y="211" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">트레이드오프: 초고속 조회(SELECT) vs DML(INSERT/UPDATE/DELETE) 페이지 분할(Page Split) 비용</text>
</svg>
</div>

- 본질: **데이터 검색 속도를 비약적으로 향상시키기 위해 테이블의 특정 컬럼 값을 B+Tree 구조로 정렬하여 별도 저장하고, 해당 행의 물리적 위치(RID 또는 클러스터드 키)를 매핑해 둔 물리적 색인 구조**
- 암기: `루-브-리` = 루트 블록 · 브랜치 블록 · 리프 블록 / `클(물리정렬/단1개/사전) vs 논(논리정렬/다수/책뒤찾아보기)`
- 인덱스 스캔 4대 방식:
  - **Index Range Scan**: 수직 탐색 후 리프 블록 수평 스캔 (일반적 $>, <, \text{BETWEEN}$)
  - **Index Unique Scan**: 단건 일치 탐색 ($=$, 고유 인덱스)
  - **Index Full Scan**: 인덱스 리프 블록 전체 순차 스캔
  - **Index Fast Full Scan**: 멀티 블록 I/O로 인덱스 세그먼트 전수 고속 스캔 (정렬 보장 안 됨)
- 주의: 인덱스는 조회(SELECT)를 가속하는 대가로 삽입·수정·삭제(DML) 시 리프 노드 분할(Page Split) 및 재배치 비용을 수반함
---

## 1교시 예상문제 (10점)

> 데이터베이스 인덱스 (Index) 및 클러스터드·논클러스터드 인덱스의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. 데이터베이스 인덱스의 정의

- 테이블의 검색 성능 향상을 위해 특정 컬럼 값을 B+Tree 구조로 정렬 저장하고 해당 튜플의 물리 주소(RowID)를 매핑해 둔 **물리적 색인 구조**

### 2. 클러스터드 vs 논클러스터드 인덱스 핵심 비교

- **물리적 구조 요약**:
  - 클러스터드 인덱스: 리프 블록 = 실제 데이터 페이지 (물리 정렬 일치, 테이블당 1개, 사전식)
  - 논클러스터드 인덱스: 리프 블록 = 키 + RID 포인터 (논리 정렬, 테이블당 복수 개, 책뒤 색인)

| 구분 | 클러스터드 인덱스 (Clustered) | 논클러스터드 인덱스 (Non-Clustered) |
|---|---|---|
| **물리 정렬 여부** | **실제 데이터 블록이 키 순서로 정렬됨** | 데이터는 정렬되지 않은 힙(Heap)에 존재 |
| **테이블당 개수** | **단 1개만 생성 가능** | **복수 개 생성 가능** |
| **I/O 메커니즘** | 리프 블록에서 추가 테이블 접근 없음 | 인덱스 스캔 후 RID로 테이블 **랜덤 I/O** 발생 |
| **장점 / 단점** | 범위 검색(BETWEEN) 최고 속도 / DML 부담 | DML 영향 적음 / 랜덤 액세스 오버헤드 |

### 3. 차별화 제언

- 테이블 랜덤 I/O를 원천 차단하기 위해 **커버링 인덱스(Covering Index)**를 적극 활용하고, 인덱스 컬럼 좌변 가공 금지 및 **선택도 10% 이내 컬럼 중심의 복합 인덱스 순서 최적화**를 강제함
---

## 2~4교시 예상문제 (25점)

> 관계형 데이터베이스의 핵심 접근 경로인 인덱스(Index)의 개념과 B+Tree 기반 동작 구조를 설명하고, 클러스터드 인덱스(Clustered Index)와 논클러스터드 인덱스(Non-Clustered Index)의 물리적 구조, I/O 매커니즘 및 장단점을 비교하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 대용량 풀 스캔 한계를 극복하는 데이터베이스 인덱스 개요

- 정의: **인덱스(Index)**는 데이터베이스 테이블에 저장된 튜플의 검색 속도를 향상시키기 위해, 하나 이상의 컬럼 값을 정렬된 상태로 유지하고 해당 행의 물리적 저장 위치(Row ID 또는 기본키)를 연결해 둔 물리적 접근 구조
- 목적: 전체 테이블의 디스크 블록을 전수 읽어 들이는 테이블 풀 스캔(Full Table Scan)의 선형 시간복잡도($O(N)$)를 이진/다원 탐색 기반의 로그 시간복잡도($O(\log N)$)로 단축하여 I/O 비용 최소화
- 필요성: 수천만 건 이상의 대용량 테이블에서 특정 조건의 단건 또는 소량 레코드를 인출할 때, 인덱스가 없으면 디스크 I/O 포화 및 버퍼 캐시 오염으로 전체 시스템 장애로 전이됨

#### 한줄 요약

- 인덱스는 책의 맨 뒤에 있는 '색인(찾아보기)'처럼, 원하는 데이터를 빠르게 찾기 위해 키 값과 위치를 미리 정렬해 둔 구조임

### Ⅱ. B+Tree 인덱스의 물리적 계층 구조 및 탐색 메커니즘

<div class="itpe-diagram-box" role="img" aria-label="B+Tree 인덱스 물리 계층 및 힙 테이블 접근 흐름도">
<svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-btree" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
  </defs>

  <!-- 루트 블록 -->
  <rect x="200" y="15" width="120" height="35" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="260" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">Root Block</text>
  <text x="260" y="44" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">키 분기: 100 | 200</text>

  <path d="M 230 50 L 140 70" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-btree)"/>
  <path d="M 290 50 L 380 70" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-btree)"/>

  <!-- 브랜치 블록 -->
  <rect x="80" y="70" width="120" height="32" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="140" y="86" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Branch Block</text>
  <text x="140" y="97" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">키: 30 | 70</text>

  <rect x="320" y="70" width="120" height="32" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="380" y="86" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Branch Block</text>
  <text x="380" y="97" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">키: 120 | 160</text>

  <path d="M 110 102 L 70 120" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-btree)"/>
  <path d="M 170 102 L 200 120" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-btree)"/>
  <path d="M 350 102 L 320 120" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-btree)"/>
  <path d="M 410 102 L 450 120" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-btree)"/>

  <!-- 리프 블록 양방향 연결 리스트 -->
  <rect x="15" y="122" width="110" height="38" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="70" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Leaf Block 1</text>
  <text x="70" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">키: 1~29 + RID</text>

  <path d="M 125 141 L 140 141" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <path d="M 140 141 L 125 141" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>

  <rect x="140" y="122" width="110" height="38" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="195" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Leaf Block 2</text>
  <text x="195" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">키: 30~69 + RID</text>

  <path d="M 250 141 L 265 141" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>

  <rect x="265" y="122" width="110" height="38" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="320" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Leaf Block 3</text>
  <text x="320" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">키: 70~99 + RID</text>

  <path d="M 375 141 L 390 141" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>

  <rect x="390" y="122" width="115" height="38" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="447" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Leaf Block 4</text>
  <text x="447" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">키: 100~119 + RID</text>

  <!-- 하단 힙 테이블 랜덤 액세스 -->
  <path d="M 195 160 L 195 185" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 3" marker-end="url(#arrow-btree)"/>
  <text x="210" y="175" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#ef4444">Table Access by RID</text>

  <rect x="15" y="185" width="490" height="28" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="260" y="202" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">힙(Heap) 테이블 데이터 블록 ── RID(File#, Block#, Slot#) 기반 디스크 랜덤 I/O</text>
</svg>
</div>

| 계층 블록 | 보관 데이터 | 역할 및 특징 |
|---|---|---|
| **루트 블록<br>(Root Block)** | 최상위 분기 기준 키 값 + 자식 브랜치 블록의 물리 주소 포인터 | 인덱스 탐색이 시작되는 단일 진입점, 메모리 버퍼 캐시에 상시 핀(Pin) 고정 |
| **브랜치 블록<br>(Branch Block)** | 하위 브랜치 또는 리프 블록을 가리키는 라우팅 키 값 + 자식 블록 포인터 | 탐색 공간을 수십~수백 분의 1로 좁혀주는 중간 분기 디렉토리 ($M$-way Fan-out) |
| **리프 블록<br>(Leaf Block)** | 실제 정렬된 인덱스 키 값 + 테이블 레코드 물리 주소 포인터(**RowID / PK**) | 키 순서대로 정렬되어 있으며, 블록 간 양방향 포인터(Double Linked List)로 범위 스캔 최적화 |

- **B-Tree vs B+Tree 차이점**:
  - B-Tree: 루트 및 브랜치 블록에도 실제 데이터 레코드 포인터를 보관하므로 블록당 키 저장 수가 감소하고 트리 깊이가 증가함
  - B+Tree: 브랜치는 순수 라우팅 키만 보관하고 모든 데이터 포인터는 리프 블록에만 집중 배치하므로 대량 범위 스캔(Range Scan)에 압도적으로 유리함

#### 한줄 요약

- B+Tree 인덱스는 루트에서 리프로 내려가는 수직적 탐색($O(\log N)$)과 리프 간을 이동하는 수평적 범위 스캔을 결합한 구조임

### Ⅲ. 클러스터드 인덱스 vs 논클러스터드 인덱스 심층 비교

<div class="itpe-diagram-box" role="img" aria-label="클러스터드 대 논클러스터드 인덱스 물리 구조 비교도">
<svg viewBox="0 0 520 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <!-- 클러스터드 영역 -->
  <rect x="15" y="15" width="235" height="150" rx="8" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="132" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">클러스터드 인덱스 (영어 사전)</text>

  <rect x="30" y="45" width="205" height="28" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="132" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Root / Branch 블록</text>

  <path d="M 132 73 L 132 88" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>

  <rect x="30" y="88" width="205" height="65" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="132" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">리프 블록 = 실제 데이터 행 자체</text>
  <text x="132" y="122" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">[101: 홍길동, 30세, 서울]</text>
  <text x="132" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">[102: 이순신, 45세, 부산]</text>
  <text x="132" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#10b981" text-anchor="middle">★ 물리적 정렬 일치 (추가 I/O 없음)</text>

  <!-- 논클러스터드 영역 -->
  <rect x="270" y="15" width="235" height="150" rx="8" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5"/>
  <text x="387" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">논클러스터드 인덱스 (책 뒤 색인)</text>

  <rect x="285" y="45" width="205" height="28" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="387" y="62" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Root / Branch 블록</text>

  <path d="M 387 73 L 387 88" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>

  <rect x="285" y="88" width="205" height="34" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="387" y="102" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">리프: 인덱스 키 + RID (포인터)</text>
  <text x="387" y="115" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">[홍길동 ──▶ File 1, Block 5]</text>

  <path d="M 387 122 L 387 132" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2 2"/>

  <rect x="285" y="132" width="205" height="26" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="#ef4444" stroke-width="1"/>
  <text x="387" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#ef4444" text-anchor="middle">힙(Heap) 테이블 블록 (랜덤 I/O 발생)</text>
</svg>
</div>

| 비교 항목 | 클러스터드 인덱스 (Clustered Index) | 논클러스터드 인덱스 (Non-Clustered Index) |
|---|---|---|
| **물리적 데이터 배치** | 인덱스의 리프 페이지가 **곧 실제 테이블 데이터 블록** | 인덱스 리프와 테이블 데이터 블록이 **물리적으로 분리** |
| **정렬 상태** | 실제 테이블 데이터가 인덱스 키 순서대로 물리적 정렬 | 테이블 데이터는 정렬되지 않은 힙(Heap)에 무작위 저장 |
| **테이블당 개수** | **오직 1개만 생성 가능** (물리적 정렬은 하나만 가능) | **테이블당 여러 개(수십 개) 생성 가능** |
| **리프 블록 내용** | 실제 테이블의 모든 컬럼 데이터 전체 | 인덱스 키 컬럼 값 + 행의 물리 주소(**RID / PK**) |
| **범위 검색 (BETWEEN)**| **압도적으로 빠름** (정렬된 연속 블록 순차 I/O) | 보통 (인덱스 스캔 후 건건이 테이블 랜덤 I/O 발생) |
| **DML 오버헤드** | **매우 높음** (중간 삽입 시 데이터 블록 재정렬 및 이동) | 상대적으로 낮음 (인덱스 리프 블록만 갱신) |
| **기본 생성 규칙** | MySQL InnoDB: Primary Key가 클러스터드 인덱스로 기본 지정 | 보조 인덱스(Secondary Index) 생성 시 기본 적용 |

#### 한줄 요약

- 클러스터드 인덱스는 데이터 자체가 가나다순으로 정렬된 '영어사전'이고, 논클러스터드 인덱스는 본문과 별도로 분리된 '책 뒤 색인'임

### Ⅳ. 인덱스 선정 및 설계 4대 핵심 기준

| 설계 기준 | 기술적 판단 논리 | 실패 시 발생하는 현상 |
|---|---|---|
| **선택도 (Selectivity)** | 선택도 = $\frac{1}{\text{카디널리티}} \times 100\%$. 선택도가 10% 이하일 때만 인덱스 손익분기점(Break-even Point) 통과 | 성별(남/여)처럼 선택도가 50%인 컬럼에 인덱스 생성 시 테이블 풀 스캔보다 느려짐 |
| **복합 인덱스 컬럼 순서**| 첫 번째 컬럼이 `=` 조건이어야 인덱스 레인지 스캔의 시작점과 끝점을 명확히 결정 | 범위 검색 컬럼(예: 날짜)을 선두에 두면 뒤따르는 `=` 컬럼이 인덱스 필터로 격하 |
| **커버링 인덱스 (Covering)**| SELECT 절의 모든 컬럼을 복합 인덱스에 포함시켜 테이블 랜덤 액세스 완전 소거 | 대량 데이터 조회 시 `TABLE ACCESS BY INDEX ROWID` 병목으로 인한 I/O 급증 |
| **데이터 갱신 빈도** | INSERT/UPDATE/DELETE가 잦은 컬럼은 인덱스 생성 지양 | 매 트랜잭션마다 인덱스 리프 분할(Page Split) 및 락 경합 발생 |

#### 한줄 요약

- 인덱스는 선택도가 우수한 컬럼을 선두로 두고, `=` 조건을 앞세우며, 커버링 인덱스를 통해 랜덤 I/O를 원천 제거해야 함

### Ⅴ. 인덱스 미사용(Full Scan 유발) 안티패턴 및 튜닝 방안

| 안티패턴 원인 | 잘못된 SQL 예시 | 올바른 튜닝 SQL |
|---|---|---|
| **인덱스 컬럼의 좌변 가공** | `WHERE SUBSTR(ORDER_NO, 1, 4) = '2026'` | `WHERE ORDER_NO LIKE '2026%'` 또는 함수 기반 인덱스(FBI) 생성 |
| **데이터 타입 불일치 (묵시적 형변환)** | `WHERE CUST_ID = 1005` (CUST_ID가 VARCHAR2) | `WHERE CUST_ID = '1005'` (타입 일치로 자동 변환 함수 제거) |
| **부정형 조건 사용** | `WHERE STATUS != 'CANCEL'` | `WHERE STATUS IN ('ORDER', 'PAY', 'DELIVER')` (긍정형 변환) |
| **NULL 조건 검색** | `WHERE EMAIL IS NULL` (B+Tree는 NULL 미색인) | DEFAULT 값 설정 후 검색 또는 NULL 허용 복합 인덱스 설계 |
| **선두 와일드카드 LIKE** | `WHERE NAME LIKE '%동'` | 역방향 문자열 인덱스(Reverse Index) 또는 n-gram 전문 검색 활용 |

#### 한줄 요약

- 인덱스 컬럼을 함수로 감싸거나 타입을 불일치시키면 옵티마이저는 인덱스를 타지 못하고 전체 테이블을 뒤지게 됨

### Ⅵ. 인덱스 실무 운영 시 주요 장애 요인 및 대책

| 문제 상황 | 근본 원인 | 실무 엔지니어링 대책 | 개선 효과 |
|---|---|---|---|
| **배치 데이터 대량 적재(Bulk Insert) 시 지연** | 테이블당 10개 이상의 인덱스로 인해 매 행마다 인덱스 리프 분할(Page Split) 발생 | 적재 전 `ALTER INDEX UNUSABLE`로 비활성화 후 적재 완료 시 `REBUILD` 일괄 수행 | 적재 속도 5배 이상 가속 |
| **인덱스 파편화로 인한 버퍼 캐시 낭비** | 잦은 DELETE/UPDATE로 인해 리프 블록 내 빈 공간(Empty Space) 증가 | 주기적 `REBUILD` 또는 `COALESCE` 작업을 수행하여 인덱스 블록 압축 정리 | 인덱스 I/O 30% 절감 |
| **불필요한 미사용 인덱스 방치** | 개발 단계에서 임시 생성된 인덱스가 방치되어 DML 트랜잭션 락 유발 | DBMS 딕셔너리(`v$object_usage`) 기반 3개월 미사용 인덱스 모니터링 후 DROP | DML 락 경합 및 디스크 공간 회수 |
| **클러스터드 인덱스 키 갱신에 따른 페이징 락** | 클러스터드 키 컬럼을 UPDATE하여 물리 데이터 행의 대규모 재배치 발생 | 클러스터드 인덱스 키는 불변(Immutable) 속성(순차 증가 ID)으로만 선정 | 행 이동(Row Migration) 방지 |

#### 한줄 요약

- 벌크 적재 시 인덱스 언유저블 처리, 주기적 리빌드, 미사용 인덱스 정리가 실무 인덱스 유지보수의 3대 철칙임

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 인덱스는 "공짜 점심(Free Lunch)"이 아니다. 개발 현장에서 쿼리 튜닝 요구가 들어올 때마다 신규 인덱스를 마구 추가하다 보면, 테이블 하나의 인덱스가 15~20개에 달해 쓰기(DML) 지연과 데드락의 주범이 된다. 인덱스 엔지니어링의 최고 경지는 무조건적인 인덱스 추가가 아니라, 기존 복합 인덱스의 순서를 조정하거나 뒤에 컬럼을 덧붙여 기존 인덱스를 다목적으로 재활용(Consolidation)하고, 초다빈도 핵심 쿼리는 커버링 인덱스로 랜덤 I/O를 원천 차단하는 데 있다.

> **[나라면 이렇게 쓴다]**
> 25점 답안 3단락 차별화로 "인덱스 수명주기 거버넌스(Index Lifecycle Governance) 및 자율운영 인덱스(Auto-Indexing)"를 제시하겠다. 개발-운영 파이프라인에서 CI/CD 정적 분석으로 컬럼 좌변 가공 및 부정형 조건을 사전 차단하고, 운영 환경에서는 DBMS 통계 딕셔너리(`v$object_usage`, `sys.dm_db_index_usage_stats`)를 연계하여 90일 이상 미호출된 '좀비 인덱스'를 자동 선별·폐기하는 자동화 아키텍처를 제시한다.

### 실전 답안용 기술사적 제언

- **[인덱스 남발에 따른 DML 성능 저하와 버퍼 오염 한계]**: 무분별한 보조 인덱스 생성은 페이지 분할(Page Split) 및 쓰기 지연시간 급증 초래
- **[실무 최적화 방안]**: 선두 컬럼 등가(`=`) 우선 배치, 초다빈도 조회 쿼리의 **커버링 인덱스(Covering Index)** 전환, 배치 적재 시 `UNUSABLE/REBUILD` 파이프라인 정립
- **[인덱스 거버넌스 체계 구축]**: DBMS 성능 뷰를 활용한 미사용 인덱스 자동 추적·삭제 및 정기적인 인덱스 재구성(`REBUILD/COALESCE`) 자동화 배치 운용

<div class="itpe-flow-map" role="group" aria-label="인덱스 설계 최적화 및 거버넌스 4단계 흐름">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">1</div>
    <div class="itpe-flow-step__title">현행 한계</div>
    <div class="itpe-flow-step__desc">인덱스 남발로 인한 DML 페이지 분할 병목 및 랜덤 I/O 급증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">2</div>
    <div class="itpe-flow-step__title">개선 방안</div>
    <div class="itpe-flow-step__desc">복합 인덱스 통합 + 커버링 인덱스 적용 및 미사용 인덱스 DROP 거버넌스</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">3</div>
    <div class="itpe-flow-step__title">검증 기준</div>
    <div class="itpe-flow-step__desc">선택도 &le; 10%, TABLE ACCESS BY ROWID 0회 달성, DML 지연 &lt; 10ms</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">4</div>
    <div class="itpe-flow-step__title">실행 효과</div>
    <div class="itpe-flow-step__desc">조회 쿼리 디스크 I/O 70% 절감 및 DML 트랜잭션 락 경합 원천 차단</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- 제136회 2교시 5번: 데이터베이스 인덱스를 설명하고, 클러스터드 인덱스와 논클러스터드 인덱스를 비교하여 설명하시오
- [Oracle Database Database Concepts, Overview of Indexes](https://docs.oracle.com/en/database/oracle/oracle-database/19/cncpt/indexes-and-index-organized-tables.html)
- [Microsoft SQL Server Documentation, Clustered and Nonclustered Indexes Described](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/clustered-and-nonclustered-indexes-described)

## 연결 토픽

- [데이터베이스 분할](./021_db_partitioning_sharding/) · [B-Tree·B+Tree](./111_b_tree/) · [데이터베이스 튜닝](./088_database_tuning/) · [옵티마이저(RBO·CBO)](./091_optimizer/)
