---
title: "스택(Stack) 자료구조"
author: "Antigravity"
date: "2026-09-20T23:49:42+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 알고리즘·자료구조를 거쳐 스택으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>알고리즘·자료구조</span>
  <strong>스택(Stack) 자료구조</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **스택(Stack)**은 한쪽 끝에서만 자료의 삽입과 삭제가 일어나는 **후입선출(LIFO: Last In First Out)** 선형 자료구조
- 메커니즘: **Top** 포인터를 통한 **Push**(삽입), **Pop**(삭제), **Peek**(조회) 연산 (모두 **O(1)** 상수 시간)
- 산출/효과: 함수 호출 스택 관리 · 괄호 검사 · 후위 표기법 연산 · DFS(깊이우선탐색) 및 브라우저 뒤로가기 구현

<div class="itpe-flow-map" role="img" aria-label="스택 자료구조의 LIFO 동작 흐름">
  <div class="itpe-flow-node"><strong>Push(데이터)</strong><div class="itpe-step-detail"><span>Top 증가 및 데이터 삽입</span></div></div>
  <div class="itpe-flow-arrow">→ Top 포인터 조작 →</div>
  <div class="itpe-flow-node is-current">
    <strong>스택(Stack) 메모리</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Top 위치</strong><span><span class="itpe-keyword"><strong>항상 최상단 노드 가리킴</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>LIFO 원칙</strong><span>가장 나중에 들어온 자료가 먼저 나감</span></div>
      <div class="itpe-flow-branch"><strong>복잡도</strong><span><span class="itpe-keyword"><strong>Push/Pop O(1)</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ Top 감소 및 반환 →</div>
  <div class="itpe-flow-node"><strong>Pop() 결과</strong><div class="itpe-step-detail"><span>최상단 데이터 추출</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- **LIFO(Last In First Out)**: 가장 최근에 저장된 항목이 가장 먼저 인출되는 입출력 규칙
- **Top 포인터**: 스택의 가장 위에 있는 자료의 위치를 가리키는 변수 (비어있을 때 -1 또는 null)
- **Push / Pop**: 스택 최상단에 데이터를 삽입하거나, 최상단 데이터를 꺼내 반환하는 연산
- **Stack Overflow**: 고정된 스택 용량을 초과하여 Push를 시도할 때 발생하는 메모리 오류
- **Call Stack(호출 스택)**: 프로그램 실행 중 함수 호출 시 복귀 주소와 지역 변수를 관리하는 런타임 스택

</details>

## 예상문제

> 스택(Stack) 자료구조의 개념 및 LIFO 특성을 설명하고, 기본 연산(Push, Pop) 메커니즘, 배열 및 연결리스트 구현 방식 비교, 시스템 소프트웨어 및 알고리즘에서의 대표적 응용 사례 4가지를 제시하시오. (25점)

## Ⅰ. 후입선출(LIFO) 원칙의 선형 자료구조, 스택의 개요

> 스택은 접근 지점을 Top 하나로 제한하며 Push·Pop·Peek 연산을 O(1)에 수행함.

- 정의: 데이터의 삽입과 삭제가 **Top이라 불리는 한쪽 끝에서만** 이루어지는 **후입선출(LIFO) 형태의 선형 자료구조**
- 목적: 작업 역순 복원, 상태 저장 및 복귀, 재귀적 호출 흐름 관리를 메모리 오버헤드 없이 **O(1)** 상수 시간에 수행

## Ⅱ. 스택의 핵심 연산 메커니즘 및 구현 방식 비교

> 스택 구현은 고정 크기 배열 방식과 동적 연결 리스트 방식으로 나뉘며 메모리 제약에 따라 선택한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="스택 기본 연산 흐름">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① Push(Item)</strong></span>
    <div class="itpe-step-detail"><strong>삽입 연산</strong><span>isFull() 확인 및 Overflow 방지 후 Top 증가, 데이터 저장</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② Peek()</strong></span>
    <div class="itpe-step-detail"><strong>단순 조회</strong><span>isEmpty() 확인 후 데이터 삭제 없이 최상단 데이터 반환</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ Pop()</strong></span>
    <div class="itpe-step-detail"><strong>추출 연산</strong><span>isEmpty() 확인 후 Underflow 방지, 데이터 반환 및 Top 감소</span></div>
  </div>
</div>

### 스택 구조 및 호출 스택(Call Stack) 프레임

<div class="itpe-svg-wrapper">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" class="itpe-svg">
    <!-- Background -->
    <rect width="520" height="220" fill="var(--sl-color-bg-subtle, #f8fafc)" rx="8" />
    
    <!-- Left: LIFO Operation Model -->
    <text x="25" y="24" class="itpe-svg-label" fill="var(--sl-color-text-accent, #2563eb)">[LIFO 연산 메커니즘]</text>
    
    <!-- Stack container -->
    <rect x="35" y="45" width="110" height="155" rx="4" fill="none" stroke="var(--sl-color-border, #94a3b8)" stroke-width="2" stroke-dasharray="155 0 0 110" />
    <!-- Stack base indicator -->
    <line x1="30" y1="200" x2="150" y2="200" stroke="var(--sl-color-text-muted, #64748b)" stroke-width="3" />
    <text x="90" y="213" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">Stack Bottom (Base)</text>

    <!-- Element 1 -->
    <rect x="42" y="160" width="96" height="32" rx="4" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    <text x="90" y="180" class="itpe-svg-sub" font-size="12" fill="var(--sl-color-text, #334155)" text-anchor="middle">Data [0]</text>

    <!-- Element 2 -->
    <rect x="42" y="120" width="96" height="32" rx="4" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    <text x="90" y="140" class="itpe-svg-sub" font-size="12" fill="var(--sl-color-text, #334155)" text-anchor="middle">Data [1]</text>

    <!-- Element 3 (Top) -->
    <rect x="42" y="80" width="96" height="32" rx="4" fill="var(--sl-color-bg-accent, #eff6ff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1.5" />
    <text x="90" y="100" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">Data [2] (Top)</text>

    <!-- Top Pointer Arrow -->
    <path d="M 175 96 L 145 96" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="2" marker-end="url(#arrow)" />
    <text x="180" y="100" class="itpe-svg-label" font-size="11" font-weight="700" fill="var(--sl-color-primary, #3b82f6)">Top Pointer</text>

    <!-- Push/Pop Action Labels -->
    <text x="90" y="48" class="itpe-svg-label" font-size="11" font-weight="700" fill="var(--sl-color-success, #10b981)" text-anchor="middle">Push ↓  ↑ Pop</text>

    <!-- Right: Call Stack Frame -->
    <text x="270" y="24" class="itpe-svg-label" fill="var(--sl-color-text-accent, #2563eb)">[함수 호출 스택 프레임(Stack Frame) 구조]</text>
    
    <!-- Call Stack container -->
    <rect x="270" y="45" width="225" height="155" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    
    <!-- Frame 1 (Main) -->
    <rect x="278" y="152" width="209" height="42" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1" />
    <text x="288" y="169" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-text, #1e293b)">main() Frame</text>
    <text x="288" y="185" class="itpe-svg-sub" font-size="11" fill="var(--sl-color-text-muted, #64748b)">지역변수, 초기화 정보</text>

    <!-- Frame 2 (Func A) -->
    <rect x="278" y="102" width="209" height="42" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1" />
    <text x="288" y="119" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-text, #1e293b)">calculate() Frame</text>
    <text x="288" y="135" class="itpe-svg-sub" font-size="11" fill="var(--sl-color-text-muted, #64748b)">매개변수, 복귀주소(main)</text>

    <!-- Frame 3 (Func B - Active) -->
    <rect x="278" y="52" width="209" height="42" rx="4" fill="var(--sl-color-bg-accent, #eff6ff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1.5" />
    <text x="288" y="69" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-primary, #3b82f6)">parse() Frame (Active)</text>
    <text x="288" y="85" class="itpe-svg-sub" font-size="11" fill="var(--sl-color-text, #334155)">지역변수, 복귀주소(calculate)</text>
  </svg>
</div>

| 비교 항목 | 배열(Array) 기반 스택 | 연결 리스트(Linked List) 기반 스택 |
|---|---|---|
| **메모리 할당** | 정적 고정 할당 (컴파일/생성 시점) | 동적 노드 할당 (런타임 필요 시점) |
| **장점** | 구현이 매우 단순, 데이터 접근 속도 빠름 | **Stack Overflow 없음** (메모리 허용 한도 내 무한) |
| **단점** | 크기 제한으로 **Stack Overflow** 위험 | 노드별 포인터 오버헤드 발생 (메모리 추가 소모) |
| **연산 복잡도** | Push: O(1), Pop: O(1) | Push: O(1), Pop: O(1) |

## Ⅲ. 스택의 주요 컴퓨터 시스템 및 알고리즘 응용 분야

> 스택은 단순한 이론적 구조를 넘어 OS 커널부터 컴파일러, 웹 브라우저까지 시스템의 근간을 이룬다.

| 응용 분야 | 스택의 구체적 역할 및 동작 원리 |
|---|---|
| **함수 호출 스택 (Call Stack)** | 함수 호출 시 복귀 주소(Return Address), 매개변수, 지역변수를 **스택 프레임(Stack Frame)**에 Push하고 복귀 시 Pop |
| **컴파일러 수식 파싱** | 중위 표기법(Infix)을 후위 표기법(Postfix)으로 변환하고, 연산자를 스택에 임시 저장하여 우선순위 평가 |
| **문법 괄호 유효성 검사** | 열린 괄호(`(`, `{`, `[`) 발견 시 Push, 닫힌 괄호 발견 시 Pop하여 짝 일치 여부 검증 |
| **실행 취소(Undo) / 브라우저 뒤로가기** | 사용자의 직전 작업 상태를 스택에 기록하여 역순 복원 수행 |
| **그래프 DFS (깊이 우선 탐색)** | 인접 정점 방문 시 역추적(Backtracking)을 위해 방문 경로를 스택에 저장 |

## Ⅳ. 스택 사용 문제점·대응책

> 깊은 재귀는 스택 고갈을, 경계 검사 없는 스택 버퍼 쓰기는 메모리 손상을 일으키므로 서로 다른 위험으로 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **Stack Overflow (스택 고갈)** | 무한 재귀 종료 조건(Base Case) 검증 및 재귀를 **반복문(Iteration)**으로 변환 | 프로세스 비정상 종료(Crash) 원천 방지 |
| **Stack Buffer Overflow (메모리 변조)** | 안전한 문자열 함수(`strncpy`) 사용, **Stack Canary**, ASLR 강제 | 악의적 리턴 주소 변조 및 원격 코드 실행 차단 |
| **Stack Underflow (공백 상태 인출)** | Pop/Peek 실행 전 `isEmpty()` 사전 조건 검증 필수화 | 널 포인터 참조 및 시스템 패닉 방지 |

## Ⅴ. 메모리 경계 통제 중심의 결론

> 시스템의 신뢰성을 확보하기 위해서는 런타임 스택 메모리 한계와 스택 프레임 수명주기에 대한 철저한 통제가 필수적이다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 스택의 O(1) 고속 연산은 '캐시 친화도(Cache Locality)' 덕분임. CPU 레지스터와 L1 캐시가 Top 근처의 스택 메모리를 매우 빠르게 읽을 수 있기 때문임. 그러나 깊은 재귀 호출은 이 캐시를 무너뜨리고 스택 오버플로우를 유발함.
- 나라면: 대용량 데이터 트리 탐색 시 언어 수준의 재귀 호출(콜스택 사용)을 금지하고, 힙 메모리에 명시적인 사용자 정의 스택(Explicit Stack)을 할당하여 OS 스택 한계(보통 1~8MB)를 우회하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 재귀 호출 깊이(Depth)의 결정성 여부 및 콜 스택 임계치(기본 OS 1~8MB) 초과 가능성 판정
- **대응 방안**: 불확실한 재귀를 **반복문(Iteration)**으로 변환하고, 대규모 탐색은 **힙(Heap) 기반 명시적 스택(Explicit Stack)**으로 전환
- **검증 체계**: 컴파일러 보안 옵션(Stack Canary, DEP) 적용 및 정적 분석 도구를 통한 스택 프레임 최대 깊이 프로파일링
- **기대 효과**: 스택 고갈(Stack Overflow) 비정상 종료 예방 및 버퍼 오버플로우 메모리 변조 취약점 원천 차단

<div class="itpe-pipeline is-vertical" role="img" aria-label="스택 메모리 안정성 확보 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>고갈 위험</strong><span>과도한 재귀 호출로 인한 스택 오버플로우 및 메모리 변조 위험</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>힙 스택 전환</strong><span>명시적 힙 스택 전환 및 스택 카나리(Canary) 방어 체계화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>한계 모니터링</strong><span>스택 한계선 모니터링 및 경계 검사 단위 테스트 100%</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>안정성 확보</strong><span>런타임 안정성 보장 및 시스템 보안 취약점 원천 제거</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **스택(Stack)**은 Top을 통해서만 데이터 삽입과 삭제가 이루어지는 **후입선출(LIFO)** 선형 자료구조
- 목적: 함수 호출 복귀, 상태 역순 복원, 수식 연산을 **O(1)** 시간 복잡도로 수행

### 2. 핵심 메커니즘

<div class="itpe-pipeline is-vertical" role="img" aria-label="스택 동작 요약">
  <div class="itpe-pipeline-node"><strong>Push(X)</strong><div class="itpe-step-detail"><span>Top 증가 후 데이터 저장</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Peek()</strong><div class="itpe-step-detail"><span>Top 위치 데이터 단순 조회</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Pop()</strong><div class="itpe-step-detail"><span>Top 데이터 반환 후 Top 감소</span></div></div>
</div>

### 3. 핵심 통제

- **오버플로우 방어**: 무한 재귀를 반복문으로 치환하고 힙 메모리 기반 커스텀 스택 활용
- **보안 통제**: 스택 버퍼 오버플로우 방지를 위한 Stack Canary 및 경계 검사 강제

## 출제 이력과 검증 출처

- 제132회 정보관리기술사 1교시: 스택(Stack)과 큐(Queue) 자료구조 비교
- 제138회 정보관리기술사 1교시: 스택 자료구조와 시스템 호출 스택
- Thomas H. Cormen, Introduction to Algorithms (CLRS), Elementary Data Structures (Stacks and Queues)

## 학습 체크

- [ ] 스택의 LIFO 원칙과 Top 포인터의 동작을 그림으로 설명할 수 있는가?
- [ ] 배열 기반 스택과 연결 리스트 기반 스택의 장단점을 비교할 수 있는가?
- [ ] 콜 스택(Call Stack)에서 스택 오버플로우가 발생하는 원인과 방지 대책을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [블랙박스 테스트](./008_black_box_test.md)
- 연관 토픽: [선형 자료구조](./053_linear_structure.md), [BST](./001_bst.md)
- 다음 토픽: [형상관리](./011_configuration_management.md)
