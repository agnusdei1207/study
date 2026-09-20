---
title: "UML 다이어그램 체계(구조·행위, 활동 다이어그램)"
tags:
  - "notes-software-engineering"
author: "Antigravity"
date: "2026-09-20T21:40:00+09:00"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash (High)"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 아키텍처·설계를 거쳐 UML 다이어그램 체계로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>아키텍처·설계</span>
  <strong>UML 다이어그램 체계(활동 다이어그램)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **UML(Unified Modeling Language)**은 객체지향 소프트웨어 시스템의 산출물을 가시화, 명세화, 구축, 문서화하기 위한 OMG 표준 통합 모델링 언어
- 메커니즘: **구조 다이어그램(7종)**(정적 구조: Class, Component 등) + **행위 다이어그램(7종)**(동적 흐름: Use Case, **Activity**, Sequence 등)
- 산출/효과: 이해관계자 간 명확한 의사소통 · 아키텍처 가시화 · **활동 다이어그램(Activity Diagram)**을 통한 복잡한 비즈니스 로직 및 병렬 워크플로우 완벽 명세

<div class="itpe-flow-map" role="img" aria-label="UML 2.5 다이어그램 체계 분류">
  <div class="itpe-flow-node"><strong>UML 2.5 체계 (14종)</strong><span>OMG 표준 통합 모델링 언어</span></div>
  <div class="itpe-flow-arrow">→ 관점별 이원화 →</div>
  <div class="itpe-flow-node is-current">
    <strong>다이어그램 분류</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>구조 다이어그램 (7종)</strong><span><span class="itpe-keyword"><strong>Class · Component · Deployment</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>행위 다이어그램 (7종)</strong><span><span class="itpe-keyword"><strong>Use Case · Activity · State</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>상호작용 하위군</strong><span>Sequence · Communication</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 비즈니스 프로세스 상세화 →</div>
  <div class="itpe-flow-node"><strong>활동 다이어그램</strong><span>Action · Fork/Join · Swimlane</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **UML(Unified Modeling Language)**: Booch, Rumbaugh, Jacobson의 방법론을 통합하여 OMG에서 표준화한 객체지향 모델링 언어
- **Structural Diagram(구조 다이어그램)**: 시스템의 정적 개념, 관계, 물리적 배치를 표현하는 7종의 다이어그램
- **Behavioral Diagram(행위 다이어그램)**: 시스템 내부 요소들의 동적 행위, 시간 경과에 따른 상태 변화를 표현하는 7종의 다이어그램
- **Activity Diagram(활동 다이어그램)**: 시스템 내부 처리 과정의 제어 흐름과 데이터 흐름, 병렬 처리를 표현하는 행위 다이어그램
- **Swimlane(스윔레인)**: 활동 다이어그램에서 각 액션의 수행 주체(역할, 부서, 시스템)를 열이나 행으로 구분하는 영역

</details>

## 예상문제

> UML(Unified Modeling Language) 2.x의 14가지 다이어그램 체계를 구조(Structural)와 행위(Behavioral) 관점으로 분류하여 설명하고, 비즈니스 프로세스 모델링에 사용되는 활동 다이어그램(Activity Diagram)의 주요 구성요소와 포크/조인(Fork/Join) 표기법을 제시하시오. (25점)

## Ⅰ. 소프트웨어 설계 시각화의 국제 표준, UML의 개요

> 복잡한 소프트웨어 시스템을 자연어로만 기술하면 모호성과 오해가 발생하므로, 정형화된 시각적 표준 언어로 명세해야 한다.

- 정의: 객체지향 시스템을 모델링하기 위해 산출물을 시각적으로 가시화(Visualizing), 명세화(Specifying), 구축(Constructing), 문서화(Documenting)하는 표준 모델링 언어(ISO/IEC 19505)
- 목적: 분석가·설계자·개발자·고객 간의 공통 언어 확립, 구현 전 아키텍처 검증, 유지보수 용이성 및 설계 추적성 확보

## Ⅱ. UML 2.x 14종 다이어그램 체계

> 시스템의 정적 청사진을 나타내는 구조 다이어그램과 동적 실행 흐름을 나타내는 행위 다이어그램으로 체계화된다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="UML 2.x 다이어그램 분류">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>구조 다이어그램 (7종) — 정적 구조</strong></span>
    <span>1. Class(클래스/관계) 2. Object(객체 인스턴스) 3. Package(모듈 구조)<br />4. Component(컴포넌트/인터페이스) 5. Composite Structure(복합체 구조)<br />6. Deployment(배치/인프라 노드) 7. Profile(UML 확장 메커니즘)</span>
  </div>
  <div class="itpe-pipeline-arrow">↕ 상호 보완</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>행위 다이어그램 (7종) — 동적 흐름</strong></span>
    <span>1. Use Case(요구기능/액터) 2. <span class="itpe-keyword"><strong>Activity(업무 흐름/병렬)</strong></span> 3. State Machine(상태 전이)<br /><strong>[상호작용 다이어그램군]</strong> 4. Sequence(시간순 메시지 교환) 5. Communication(객체 간 관계 중심)<br />6. Timing(시간 제약/상태) 7. Interaction Overview(상호작용 개요)</span>
  </div>
</div>

## Ⅲ. 활동 다이어그램(Activity Diagram)의 구조 및 구성요소

> 전통적 순서도(Flowchart)를 객체지향 관점으로 확장하여 병렬 처리와 책임 주체를 명확히 표현한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="활동 다이어그램 주요 흐름 예시">
  <div class="itpe-pipeline-node">
    <strong>Initial Node (시작 노드)</strong>
    <span>채워진 검은 원(●) · 활동의 시작점</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ Control Flow</div>
  <div class="itpe-pipeline-node">
    <strong>Action / Activity Node (액션 노드)</strong>
    <span>모서리가 둥근 사각형 · 원자적 연산 또는 복합 작업 수행</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ Fork Node</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>Fork Node (동기화 분기: 굵은 가로선)</strong></span>
    <span>단일 입력 흐름을 2개 이상의 동시 병렬 실행 흐름으로 분할</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ 병렬 처리 수행</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>Join Node (동기화 결합: 굵은 가로선)</strong></span>
    <span>모든 병렬 흐름이 완료될 때까지 대기 후 단일 흐름으로 합류</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ Control Flow</div>
  <div class="itpe-pipeline-node">
    <strong>Activity Final Node (종료 노드)</strong>
    <span>테두리가 있는 채워진 원(◎) · 모든 흐름 종료</span>
  </div>
</div>

| 구성요소 | 표기법 심볼 | 설명 및 역할 |
|---|---|---|
| **Action Node** | 모서리가 둥근 사각형 | 더 이상 분할할 수 없는 최소 단위의 실행 단계 |
| **Control Flow** | 실선 화살표 (`→`) | 액션 간의 실행 제어 흐름 전달 |
| **Decision / Merge** | 마름모 (`◇`) | 조건에 따른 분기(가드 조건 `[조건]`) 및 분기 흐름 결합 |
| **Fork Node** | 굵은 직선 (1:N) | 병렬 처리를 위해 단일 흐름을 여러 개의 동시 흐름으로 분기 |
| **Join Node** | 굵은 직선 (N:1) | 모든 병렬 흐름이 도달할 때까지 동기화 대기 후 진행 |
| **Swimlane (스윔레인)** | 수직/수평 분할 구획선 | 액션을 수행하는 주체(예: 고객, 주문시스템, 결제사)를 역할별로 구분 |

## Ⅳ. 주요 행위 다이어그램 간의 비교 및 실무 위험 관리

> 시스템 모델링 시 표현하려는 관점에 따라 가장 적합한 다이어그램을 선택해야 한다.

### 1. 주요 행위 다이어그램 비교

| 비교 항목 | 유스케이스 다이어그램 | 순차 다이어그램 (Sequence) | 활동 다이어그램 (Activity) | 상태 다이어그램 (State) |
|---|---|---|---|---|
| **주요 관점** | 시스템 **외부 기능 요구** | 객체 간 **시간순 메시지 교환** | 시스템 내부 **업무 처리 절차** | 단일 객체의 **상태 변화 생명주기** |
| **적합한 단계** | 요구사항 분석 초기 | 상세 분석 및 설계 단계 | 비즈니스 프로세스 분석 | 복잡한 생명주기를 갖는 엔티티 |
| **병렬 표현** | 불가능 | 가능하나 복잡함 | **Fork/Join으로 매우 우수** | 동시성 복합 상태로 표현 |
| **주요 활용** | 과업 범위 확정 | API 시퀀스, 인터페이스 설계 | 업무 흐름도, 알고리즘 로직 | 주문/결제 상태 머신 설계 |

### 2. UML 모델링 실무 위험 및 대응 통제

| 위험 | 대책 | 효과 |
|---|---|---|
| 코드 변경 시 UML 다이어그램 동기화 누락 | PlantUML/Mermaid 기반 Docs-as-Code 및 Git 연동 | 설계 문서 최신성 및 형상 일관성 유지 |
| 비즈니스 병렬 흐름 표기 오류(데드락) | 활동 다이어그램 내 Fork-Join 쌍 일치성 및 완료 조건 검증 | 동시성 흐름 설계 오류 및 교착상태 사전 차단 |
| 14종 전 다이어그램 작성에 따른 공수 낭비 | 분석·설계 목적별 핵심 3종(Class, Sequence, Activity) 선별 표준화 | 모델링 생산성 향상 및 실효적 의사소통 집중 |

## Ⅴ. 모델 기반 엔지니어링(MBSE)을 위한 기술사적 제언

> UML 다이어그램은 그림 그리기가 아니며, 소스코드와 100% 동기화되는 소프트웨어 자산이어야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 현업에서 UML이 사장된 이유는 '그려놓고 코드가 바뀌면 문서를 갱신하지 않아 문서가 쓰레기가 되는' 동기화 실패 때문임. 현대에는 14종 다이어그램을 모두 그리는 대신, 의사소통에 필수적인 3종(Class, Sequence, Activity)만 선별 작성하고, Mermaid나 PlantUML처럼 '코드로 관리하는 다이어그램(Docs-as-Code)' 체계로 전환해야 함.
- 나라면: CI/CD 파이프라인에서 Git 커밋 시 Markdown 내 Mermaid 다이어그램을 자동 렌더링하도록 설정하고, 소스코드 변경 시 아키텍처 문서가 함께 버전 관리되도록 체계화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 과도한 전 다이어그램 작성 지양, 핵심 3종(클래스, 시퀀스, 활동) 집중 표준화
- 대안: **PlantUML/Mermaid** 기반 Docs-as-Code 환경 구축 및 버전 관리 일원화
- 검증: 요구사항-UML-코드 간 RTM 추적성 100% 검증 · 형상 일치성 확보
- 효과: 모델링 작성 공수 60% 절감 · 아키텍처 문서의 최신성 및 신뢰성 유지

<div class="itpe-pipeline is-vertical" role="img" aria-label="UML 모델링 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>형식적 다이어그램 작성 · 구현 후 코드와 모델의 영구적 괴리</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>Docs-as-Code(PlantUML/Mermaid) 도입 및 핵심 3종 다이어그램 선별</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>Git 브랜치 연동 문서 자동 빌드 및 RTM 양방향 추적성 점검</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>설계 의사소통 표준화 · 살아 숨쉬는 아키텍처 문서 자산화 달성</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **UML(Unified Modeling Language)**은 객체지향 시스템의 산출물을 시각적으로 가시화, 명세화, 구축, 문서화하는 표준 모델링 언어
- 목적: 설계 의사소통 표준화 및 아키텍처 구조·동적 행위의 사전 검증

### 2. 구조(7종) vs 행위(7종) 체계 요약

<div class="itpe-pipeline is-vertical" role="img" aria-label="UML 2체계 요약">
  <div class="itpe-pipeline-node"><strong>구조 다이어그램 (7종)</strong><span>Class · Component · Deployment · Package 등 (정적 구조)</span></div>
  <div class="itpe-pipeline-arrow">↕ 상호 보완</div>
  <div class="itpe-pipeline-node"><strong>행위 다이어그램 (7종)</strong><span>Use Case · Activity · Sequence · State 등 (동적 실행)</span></div>
</div>

### 3. 활동 다이어그램 핵심 통제

- **Fork / Join**: 굵은 가로선을 통해 병렬 흐름의 분기와 동기화 대기를 정형화
- **Swimlane**: 처리 주체(부서, 시스템)별 책임 구획선 명확화

## 출제 이력과 검증 출처

- 제137회 정보관리기술사 1교시: UML 2.x 다이어그램 체계 및 활동 다이어그램
- ISO/IEC 19505:2012 Information technology - OMG Unified Modeling Language (OMG UML)
- Martin Fowler, UML Distilled: A Brief Guide to the Standard Object Modeling Language (3rd Edition)

## 학습 체크

- [ ] UML 2.x의 14개 다이어그램을 구조(7종)와 행위(7종)로 빠짐없이 분류할 수 있는가?
- [ ] 활동 다이어그램에서 Fork 노드와 Join 노드의 차이를 그림으로 설명할 수 있는가?
- [ ] 시퀀스 다이어그램과 활동 다이어그램의 모델링 관점 차이를 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [오픈소스 라이선스](./018_open_source_license.md)
- 연관 토픽: [클래스 다이어그램](./045_class_diagram.md), [유스케이스 다이어그램](./026_use_case_diagram.md)
- 다음 토픽: [Open API](./022_open_api.md)
