---
title: "선형 구조(Linear Structure)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
author: "Antigravity"
date: "2026-09-21T16:36:00+09:00"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 자료구조와 알고리즘을 거쳐 선형 구조로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>자료구조 · 알고리즘</span>
  <strong>선형 구조</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **선형 구조(Linear Structure)**는 데이터 요소 간의 관계가 1:1로 연결되어 유일한 선행자와 후속자를 갖는 일차원적 순서 나열 자료구조
- 메커니즘: **임의 접근 구조(배열, 순차 리스트)** + **참조 연결 구조(연결 리스트)** + **입출력 제약 구조(스택-LIFO, 큐-FIFO, 덱-양방향)**
- 산출/효과: CPU 캐시 공간 지역성(Spatial Locality) 극대화 · 링 버퍼(원형 큐)를 통한 메모리 재활용 및 제로 카피 스트리밍 버퍼 구현

<div class="itpe-flow-map" role="img" aria-label="선형 자료구조 체계도">
  <div class="itpe-flow-node"><strong>선형 데이터</strong><span>1:1 연속 나열</span></div>
  <div class="itpe-flow-arrow">→ 접근 방식 및 제약 분기 →</div>
  <div class="itpe-flow-node is-current">
    <strong>선형 자료구조 분류</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>비제약</strong><span><span class="itpe-keyword"><strong>배열(Array) · 리스트(ArrayList/LinkedList)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>제약(LIFO/FIFO)</strong><span><span class="itpe-keyword"><strong>스택(Stack) · 큐(Queue) · 덱(Deque)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>버퍼 최적화</strong><span>원형 큐(Ring Buffer) 모듈로 연산</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 하드웨어 캐시 및 버퍼링 →</div>
  <div class="itpe-flow-node"><strong>시스템 최적화</strong><span>배압 제어 · 초저지연 I/O 큐</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Linear Structure(선형 구조)**: 데이터 요소 간에 1:1 선행·후속 관계를 갖는 순차적 자료구조
- **Circular Queue(원형 큐)**: 선형 큐의 잘못된 포화(False Overflow)를 해결하기 위해 모듈로(`% Size`) 연산으로 시작과 끝을 연결한 링 버퍼
- **Spatial Locality(공간 지역성)**: 최근 접근한 메모리의 인접 영역이 연속 참조될 가능성이 높아 CPU 캐시 적중률이 극대화되는 하드웨어 특성
- **Backpressure(배압)**: 큐 버퍼 상한 도달 시 생산자의 유입 속도를 능동적으로 제어하여 OOM 크래시를 방지하는 리액티브 메커니즘
- **ArrayList vs LinkedList**: 연속된 물리 배열 기반 $O(1)$ 임의 접근 vs 힙 포인터 체인 기반 $O(1)$ 중간 삽입/삭제 구조

</details>

## 예상문제

> 데이터 요소 간 1:1 관계를 갖는 선형 자료구조(Linear Structure)의 개념을 설명하고, 배열, 연결 리스트, 스택, 큐의 동작 메커니즘과 시간복잡도를 비교하며, 원형 큐의 포화 판별 수식 및 실무 운영 위험 통제 방안을 제시하시오. (25점)

## Ⅰ. 1:1 순서 보장과 메모리 배치, 선형 구조의 개요

> 현대 고성능 시스템의 병목은 알고리즘 점근 복잡도보다 CPU 캐시 적중률과 큐 버퍼링 제어에서 발생한다.

- 정의: 데이터 요소 간의 앞뒤 순서가 일렬(1:1)로 연결되어, 첫 번째와 마지막 원소를 제외한 모든 원소가 유일한 선행자와 후속자를 갖는 자료구조
- 목적: 순차적 데이터 처리, 함수 호출 스택 관리, 비동기 메시지 버퍼링, 하드웨어 메모리 친화적 임의 접근 보장

## Ⅱ. 선형 자료구조 핵심 분류 및 메커니즘

> 메모리 연속성 여부와 입출력 제약 조건에 따라 구조적 특성과 사용 목적이 명확히 분기된다.

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" style="max-width: 520px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="lin-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Left: Stack & Queue Constraints -->
  <rect x="15" y="15" width="235" height="190" rx="8" fill="var(--sl-color-blue-subtle, #eff6ff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1.5" filter="url(#lin-shadow)"/>
  <text x="25" y="36" font-size="11.5" font-weight="700" fill="var(--sl-color-blue-high, #2563eb)">입출력 제약 구조 (스택 vs 큐)</text>

  <!-- Stack Box -->
  <rect x="25" y="48" width="100" height="92" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="75" y="68" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-blue-high, #2563eb)">스택 (LIFO)</text>
  <rect x="35" y="76" width="80" height="18" rx="2" fill="var(--sl-color-blue-subtle, #eff6ff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="0.8"/>
  <text x="75" y="89" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1f2937)">Top: Push/Pop</text>
  <rect x="35" y="98" width="80" height="16" rx="2" fill="var(--sl-color-gray-5, #e5e7eb)"/>
  <text x="75" y="110" text-anchor="middle" font-size="8" fill="var(--sl-color-text-muted, #4b5563)">Bottom (폐쇄)</text>
  <text x="75" y="132" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">호출스택·파싱</text>

  <!-- Queue Box -->
  <rect x="135" y="48" width="105" height="92" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="1"/>
  <text x="187" y="68" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-green-high, #16a34a)">큐 (FIFO)</text>
  <rect x="143" y="76" width="89" height="18" rx="2" fill="var(--sl-color-green-subtle, #f0fdf4)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="0.8"/>
  <text x="187" y="89" text-anchor="middle" font-size="8" fill="var(--sl-color-text, #1f2937)">Rear: Enqueue</text>
  <rect x="143" y="98" width="89" height="18" rx="2" fill="var(--sl-color-green-subtle, #f0fdf4)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="0.8"/>
  <text x="187" y="111" text-anchor="middle" font-size="8" fill="var(--sl-color-text, #1f2937)">Front: Dequeue</text>
  <text x="187" y="132" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">비동기 버퍼링</text>

  <rect x="25" y="148" width="215" height="46" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1"/>
  <text x="32" y="165" font-size="9" font-weight="700" fill="var(--sl-color-text, #1f2937)">캐시 친화성: ArrayList &gt;&gt; LinkedList</text>
  <text x="32" y="182" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">연속 메모리 공간 지역성으로 L1/L2 적중률 극대화</text>

  <!-- Right: Circular Queue (Ring Buffer) -->
  <rect x="265" y="15" width="240" height="190" rx="8" fill="var(--sl-color-purple-subtle, #f5f3ff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1.5" filter="url(#lin-shadow)"/>
  <text x="275" y="36" font-size="11.5" font-weight="700" fill="var(--sl-color-accent, #7c3aed)">원형 큐 (Circular Queue / Ring Buffer)</text>
  <text x="275" y="52" font-size="9" fill="var(--sl-color-text-muted, #4b5563)">선형 큐의 False Overflow 극복 (모듈로 연산)</text>

  <!-- Circular Visual -->
  <circle cx="385" cy="108" r="42" fill="none" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="12" stroke-dasharray="24 4"/>
  <circle cx="385" cy="108" r="30" fill="var(--sl-color-bg-card, #ffffff)"/>
  <text x="385" y="105" text-anchor="middle" font-size="9" font-weight="700" fill="var(--sl-color-accent-high, #5b21b6)">Size: N</text>
  <text x="385" y="118" text-anchor="middle" font-size="8" fill="var(--sl-color-text-muted, #4b5563)">Ring</text>

  <rect x="275" y="158" width="220" height="38" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1"/>
  <text x="282" y="172" font-size="8.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">포화 판별: (Rear + 1) % Size == Front</text>
  <text x="282" y="186" font-size="8" fill="var(--sl-color-accent-high, #5b21b6)">공백과 구분 위해 1칸을 비워두고 만석 판정</text>
</svg>
</div>

<div class="itpe-pipeline is-vertical" role="img" aria-label="선형 구조 분류 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. 접근 제약 없는 구조 (자유로운 탐색)</strong></span>
    <span>• 배열 (Array): 연속 메모리 배치, 인덱스 오프셋 기반 $O(1)$ 임의 접근<br />• 순차 리스트 (ArrayList): 동적 가변 배열, 캐시 공간 지역성 압도적 우수<br />• 연결 리스트 (LinkedList): 노드 포인터 체인, 선행자 확보 시 $O(1)$ 중간 삽입/삭제</span>
  </div>
  <div class="itpe-pipeline-arrow">↕ 무결성 보장을 위한 입출력 제약 부여</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. 접근 제약 구조 (엄격한 순서 보장)</strong></span>
    <span>• 스택 (Stack): Top 한쪽 끝에서만 입출력되는 후입선출 (LIFO: 백트래킹, 실행 스택)<br />• 큐 (Queue): Rear 삽입, Front 삭제가 일어나는 선입선출 (FIFO: 작업 대기열)<br />• 덱 (Deque): 양쪽 끝(Front, Rear)에서 모두 삽입/삭제 가능한 양방향 결합형</span>
  </div>
</div>

## Ⅲ. 4대 선형 구조 복잡도 및 원형 큐 수식 메커니즘

> 선형 큐의 메모리 단편화 문제를 해결하기 위해 원형 큐의 모듈로 판별식이 필수적으로 사용된다.

### 1. 4대 선형 자료구조 시간복잡도 비교

| 자료구조 | 임의 접근 (Access) | 순차 탐색 (Search) | 삽입 (Insertion) | 삭제 (Deletion) | 주요 활용 분야 |
|---|---|---|---|---|---|
| **배열 (Array)** | **$O(1)$** | $O(N)$ | $O(N)$ | $O(N)$ | 룩업 테이블, 정적 고정 버퍼 |
| **연결 리스트** | $O(N)$ | $O(N)$ | **$O(1)^*$** | **$O(1)^*$** | 삽입/삭제 잦은 동적 리스트 |
| **스택 (Stack)** | $O(N)$ | $O(N)$ | **$O(1)$ (Push)** | **$O(1)$ (Pop)** | 함수 복귀 주소, 문법 파싱 |
| **큐 (Queue)** | $O(N)$ | $O(N)$ | **$O(1)$ (Enqueue)** | **$O(1)$ (Dequeue)** | OS 스케줄러, 메시지 브로커 |

> \* 연결 리스트의 $O(1)$ 삽입/삭제는 대상 노드의 포인터를 이미 확보한 경우에 한함.

### 2. 원형 큐(Circular Queue) 모듈로 수식

- **선형 큐 한계**: Dequeue 후 앞단 공간이 비어 있어도 `Rear == Size - 1`이면 삽입 불가능(False Overflow)
- **포인터 이동식**: `Next_Pointer = (Current_Pointer + 1) % Size`
- **공백 판별식**: `Front == Rear`
- **포화 판별식**: `(Rear + 1) % Size == Front` (공백과 포화 구분을 위해 반드시 1칸을 공백으로 유지)

## Ⅳ. 선형 구조 운영 위험 및 실무 통제 대책

> 메모리 제약 없는 큐와 캐시 미스를 유발하는 연결 리스트는 운영 장애의 주요 원인이 된다.

| 위험 | 대책 | 효과 |
|---|---|---|
| **큐 폭증으로 인한 OOM (Crash)** | **바운디드 큐(Bounded Queue)** 강제 및 리액티브 **배압(Backpressure)** 적용 | 힙 메모리 고갈 원천 차단 및 시스템 생존 보장 |
| **캐시 미스(Cache Miss) 병목** | LinkedList 대신 **ArrayList** 표준화 및 객체 풀링(Object Pooling) | CPU 공간 지역성 확보로 대량 순회 속도 3~5배 향상 |
| **선형 큐 잘못된 포화 고갈** | **원형 큐(Ring Buffer / LMAX Disruptor)** 구조 채택 | 가비지 컬렉션(GC) 제거 및 마이크로초 단위 초저지연 달성 |

## Ⅴ. 하드웨어 캐시 지역성과 배압 제어 관점의 기술사적 제언

> 이론적 시간복잡도보다 현대 CPU의 캐시 아키텍처와 분산 시스템의 배압 거버넌스를 결합해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 알고리즘 책에서는 삽입/삭제가 빈번할 때 LinkedList가 $O(1)$로 우수하다고 가르치지만, 현대 64비트 CPU 환경에서는 완전히 틀린 조언임. LinkedList의 노드는 힙 메모리 사방에 흩어져 있어 접근할 때마다 L1/L2 캐시 미스를 유발함. 반면 ArrayList는 메모리가 연속되어 있어 64바이트 캐시 라인(Spatial Locality)에 의해 미리 CPU로 올라옴. 10만 건 이하의 일반적 연산에서는 메모리 시프트 비용을 감수하더라도 ArrayList가 LinkedList보다 훨씬 빠름.
- 나라면: 엔터프라이즈 백엔드 표준 가이드라인에서 무분별한 LinkedList 사용을 금지하고 ArrayList를 기본 컬렉션으로 강제하되, 메시지 큐는 용량 제한이 없는 `LinkedBlockingQueue`를 엄격히 금지하고 반드시 크기가 고정된 `ArrayBlockingQueue`에 배압(429 Too Many Requests) 정책을 연동하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 언바운디드 큐(무제한 버퍼) 운영 환경 전면 금지, 메모리 공간 지역성(Spatial Locality) 최적화 판정
- **대응 방안**: 순차 순회/조회는 ArrayList 표준화, 고성능 메시지 큐는 원형 링 버퍼(Disruptor) 및 바운디드 큐 배압(Backpressure) 적용
- **검증 체계**: APM 기반 큐 적재 임계치(80%) 초과 알람 및 CPU L1/L2 캐시 미스율 프로파일링 정기 검증
- **기대 효과**: 힙 메모리 고갈(OOM) 원천 차단, 트랜잭션 처리 지연 80% 단축 및 GC 부하 없는 초저지연 버퍼링 달성

<div class="itpe-pipeline is-vertical" role="img" aria-label="선형 구조 엔터프라이즈 최적화 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>언바운디드 큐로 인한 OOM 및 포인터 체인으로 인한 캐시 미스 성능 저하</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>연속 메모리(ArrayList/원형 큐) 기반 설계 및 배압 제어 파이프라인 구축</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>큐 임계치 초과 시 트래픽 스로틀링 검증 및 CPU 캐시 적중률 95% 이상</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>서버 다운 없는 안정적 트래픽 수용 및 고성능 스트리밍 I/O 완성</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **선형 구조(Linear Structure)**는 데이터 요소들이 1:1의 선행·후속 관계로 순차 나열되는 자료구조
- 목적: 엄격한 순서 보장, 효율적 메모리 인덱싱, 비동기 버퍼링 제어

### 2. 원형 큐 핵심 수식

<div class="itpe-pipeline is-vertical" role="img" aria-label="원형 큐 요약">
  <div class="itpe-pipeline-node"><strong>포인터 이동</strong><span>`Next = (Current + 1) % Size`</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>공백·포화 판별</strong><span>공백: `Front == Rear` / 포화: `(Rear + 1) % Size == Front`</span></div>
</div>

### 3. 핵심 통제

- **False Overflow 극복**: 모듈로 연산 기반 링 버퍼를 활용해 메모리 재활용
- **배압(Backpressure)**: 큐 크기 상한 설정으로 OOM 방지 및 가용성 유지

## 출제 이력과 검증 출처

- 제131회 정보관리기술사 1교시: 자료구조에서 선형 구조와 비선형 구조의 비교
- Thomas H. Cormen, Introduction to Algorithms (CLRS) - Elementary Data Structures
- LMAX Disruptor High Performance Alternative to Bounded Queues

## 학습 체크

- [ ] 선형 자료구조의 정의와 선형 큐의 '잘못된 포화(False Overflow)' 원인을 설명할 수 있는가?
- [ ] 원형 큐의 공백 판별식과 포화 판별식을 수식으로 정확히 제시할 수 있는가?
- [ ] ArrayList와 LinkedList를 CPU 캐시 공간 지역성 관점에서 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [비선형 구조](./052_non_linear_structure.md)
- 연관 토픽: [정렬 알고리즘](./043_sort_algorithm.md), [BST](./001_bst.md)
- 다음 토픽: [요구사항 명세](./054_requirements_specification.md)
