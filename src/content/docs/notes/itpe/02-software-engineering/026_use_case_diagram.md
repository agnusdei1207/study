---
title: "유스케이스 다이어그램(유스케이스 명세)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 요구공학을 거쳐 유스케이스 다이어그램으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>요구공학</span>
  <strong>유스케이스 다이어그램(유스케이스 명세)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **유스케이스 다이어그램(Use Case Diagram)**은 사용자(액터) 관점에서 시스템이 제공해야 하는 기능적 요구사항과 시스템 경계를 시각적으로 모델링하는 행위 다이어그램
- 메커니즘: **시스템 경계** + **액터(Actor)** + **유스케이스(Use Case)** + **관계(연관, 포함 `<include>`, 확장 `<extend>`, 일반화)**
- 산출/효과: 시스템 개발 범위(Scope) 확정 · 사용자 관점의 요구사항 가시화 · **유스케이스 명세서(Use Case Specification)** 작성을 통한 분석·설계·테스트 기준선 제공

<div class="itpe-flow-map" role="img" aria-label="유스케이스 모델링 흐름">
  <div class="itpe-flow-node"><strong>액터(Actor)</strong><small>시스템 외부 사용자/연계시스템</small></div>
  <div class="itpe-flow-arrow">→ 상호작용 (Association) →</div>
  <div class="itpe-flow-node is-current">
    <strong>유스케이스 (Use Case)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>포함 관계</strong><span>&lt;&lt;include&gt;&gt; 필수 공통 기능</span></div>
      <div class="itpe-flow-branch"><strong>확장 관계</strong><span>&lt;&lt;extend&gt;&gt; 특정 조건부 부가 기능</span></div>
      <div class="itpe-flow-branch"><strong>일반화</strong><span>상위-하위 개념 상속</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 상세화 →</div>
  <div class="itpe-flow-node"><strong>유스케이스 명세서</strong><small>사전/사후조건 · 기본/대안 흐름</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Use Case**: 사용자에게 측정 가능한 가치의 결과를 전달하기 위해 시스템이 수행하는 일련의 작업 흐름
- **Actor**: 시스템과 상호작용하는 외부의 모든 주체 (주 액터: 사용자, 부 액터: 연계 시스템/관리자)
- **&lt;&lt;include&gt;&gt; (포함 관계)**: 하나의 유스케이스가 다른 유스케이스의 실행을 반드시 포함하는 필수적 의존 관계
- **&lt;&lt;extend&gt;&gt; (확장 관계)**: 기본 유스케이스의 특정 확장 지점(Extension Point)에서 조건이 만족될 때만 선택적으로 실행되는 관계
- **Use Case Specification**: 유스케이스 다이어그램의 타원 하나를 상세히 기술한 문서(기본 흐름, 대안 흐름, 예외 흐름 등)

</details>

## 예상문제

> 요구사항 분석 단계에서 사용되는 UML 유스케이스 다이어그램(Use Case Diagram)의 구성요소(액터, 유스케이스, 관계)를 설명하고, 포함(&lt;&lt;include&gt;&gt;)과 확장(&lt;&lt;extend&gt;&gt;) 관계의 명확한 차이점 및 유스케이스 명세서(Use Case Specification)의 핵심 기술 항목을 제시하시오. (25점)

## Ⅰ. 사용자 관점의 기능 요구사항 명세화, 유스케이스 모델링의 개요

> 시스템이 '어떻게(How)' 동작하는가가 아니라 사용자가 시스템을 통해 '무엇(What)'을 얻는가를 정의해야 분석이 산으로 가지 않는다.

- 정의: 시스템이 제공하는 기능과 이를 이용하는 외부 사용자(액터) 간의 상호작용을 다이어그램과 텍스트 명세서로 모델링하는 기법
- 목적: 프로젝트 과업 범위(Scope) 확정, 개발자-사용자 간 의사소통 기준 마련, 인수 테스트 케이스 도출의 근거 제공

## Ⅱ. 유스케이스 다이어그램의 4대 핵심 구성요소 및 관계

> 다이어그램은 큰 그림을 보여주고, 세부적인 입출력과 조건은 유스케이스 명세서에 위임한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="유스케이스 관계 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. 액터 (Actor) — 졸라맨 심볼</strong></span>
    <small>시스템 외부에 위치하며 시스템과 정보를 교환하는 역할 (주 액터, 부 액터)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓ 실선 연관 (Association)</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. 기본 유스케이스 (Base Use Case) — 타원 심볼</strong></span>
    <small>시스템 경계(Subject Boundary 사각형) 내부에서 사용자 목적을 달성하는 작업 단위</small>
  </div>
  <div class="itpe-pipeline-arrow">↓ 점선 화살표 관계</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. 포함(&lt;&lt;include&gt;&gt;) 및 확장(&lt;&lt;extend&gt;&gt;)</strong></span>
    <small>include: 기본 → 피포함 (필수 실행)<br />extend: 확장 → 기본 (조건부 선택 실행, 확장점 명시)</small>
  </div>
</div>

| 관계 유형 | 표기법 (Stereotype) | 화살표 방향 | 핵심 의미 및 동작 조건 |
|---|---|---|---|
| **연관 (Association)** | 실선 (`―`) | 방향성 없거나 단방향 | 액터와 유스케이스 간의 상호작용 통로 |
| **포함 (&lt;&lt;include&gt;&gt;)** | 점선 화살표 + `<<include>>` | **기본 → 포함** | 기본 유스케이스 수행 시 **반드시(100%) 함께 실행**되는 공통 로직 |
| **확장 (&lt;&lt;extend&gt;&gt;)** | 점선 화살표 + `<<extend>>` | **확장 → 기본** | 기본 유스케이스 수행 중 **특정 조건 만족 시에만 선택적 실행** |
| **일반화 (Generalization)**| 실선 + 빈 삼각형 화살표 | 하위 → 상위 | 유스케이스나 액터 간의 상속(Inheritance) 관계 |

## Ⅲ. 포함(&lt;&lt;include&gt;&gt;) vs 확장(&lt;&lt;extend&gt;&gt;)의 완벽 비교

> 두 관계의 화살표 방향과 실행 필수성은 기술사 채점관이 가장 엄격하게 판정하는 핵심 지점이다.

| 비교 항목 | 포함 관계 (&lt;&lt;include&gt;&gt;) | 확장 관계 (&lt;&lt;extend&gt;&gt;) |
|---|---|---|
| **실행 필수성** | **필수적 실행** (기본 실행 시 반드시 호출) | **조건부 선택 실행** (조건 만족 시만 끼어듦) |
| **화살표 출발/도착** | 기본 유스케이스 **→** 포함 유스케이스 | 확장 유스케이스 **→** 기본 유스케이스 |
| **확장점 필요 여부** | 불필요 | **필수** (기본 유스케이스 내 Extension Point 명시) |
| **주요 목적** | 공통 기능 재사용 (중복 제거) | 기본 흐름을 훼손하지 않는 예외/부가 기능 분리 |
| **구체적 사례** | `[주문하기] ──<<include>>──> [로그인]` | `[쿠폰 적용] ──<<extend>>──> [결제하기]` |

## Ⅳ. 유스케이스 명세서(Use Case Specification)의 표준 구조

> 다이어그램은 목차에 불과하며, 실질적인 소프트웨어 설계와 테스트의 기준은 명세서 본문이다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="유스케이스 명세서 기술 항목">
  <div class="itpe-pipeline-node">
    <strong>기본 정보</strong>
    <small>유스케이스명, 식별자, 주 액터, 담당자, 개요</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>사전/사후 조건 (Pre/Post-conditions)</strong></span>
    <small>사전조건: 실행 전 참이어야 할 상태 (예: 로그인 완료)<br />사후조건: 실행 후 보장되는 시스템 상태 (예: 주문DB 저장, 결제 승인)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>이벤트 흐름 (Flow of Events)</strong></span>
    <small>1. 기본 흐름(Happy Path): 오류 없는 이상적 진행 단계<br />2. 대안 흐름(Alternative Flow): 다른 방식으로 목적 달성<br />3. 예외 흐름(Exception Flow): 장애 발생 시 롤백 및 에러 처리</small>
  </div>
</div>

## Ⅴ. 요구사항 추적성 확립을 위한 기술사적 제언

> 유스케이스는 고립된 문서가 아니며, 요구사항 추적표(RTM)를 통해 설계, 코드, 테스트 케이스로 직결되어야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 유스케이스 모델링에서 가장 자주 발생하는 오류는 프로그래밍 순서도처럼 모든 기능 단위를 타원으로 만들어 수십 개의 include/extend로 얽히게 만드는 '기능 분해(Functional Decomposition)'의 함정임. 유스케이스는 사용자에게 완전한 하나의 가치를 전달하는 단위여야 함.
- 나라면: 유스케이스 명세서의 기본 흐름, 대안 흐름, 예외 흐름에서 직접 테스트 시나리오를 1:1로 도출(유스케이스 테스팅)하여 시스템 인수 테스트 케이스로 직결되도록 관리하겠음.

### 실전 답안용 기술사적 제언

- 판정: 과도한 세부 기능 타원화 금지 및 사용자 목적 중심 유스케이스 정립
- 대안: 유스케이스 명세서 기반 **인수 테스트 케이스 자동 도출**
- 검증: 요구사항정의서 ↔ 유스케이스 ↔ 테스트케이스 **RTM 매핑율 100%**
- 효과: 과업 변경 분쟁 예방 및 사용자 요구와 개발 산출물 간 완전한 일치성 달성

<div class="itpe-pipeline is-vertical" role="img" aria-label="유스케이스 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>순서도식 과도한 유스케이스 분할 · 명세서 부실로 개발자 자의적 구현</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>사용자 가치 중심 유스케이스 통합 및 이벤트 흐름(기본/대안/예외) 정형화</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>RTM 추적성 검증 및 유스케이스 기반 인수 테스트(UAT) 커버리지</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>요구사항 누락 제로화 · 발주자-개발자 간 완벽한 합의 형성</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **유스케이스 다이어그램**은 시스템의 기능과 외부 액터의 상호작용을 모델링하여 시스템 경계와 요구 범위를 가시화하는 행위 다이어그램
- 목적: 과업 범위 확정 및 사용자 관점의 인수 테스트 기준선 제공

### 2. 포함 vs 확장 핵심 차이

<div class="itpe-pipeline is-vertical" role="img" aria-label="포함 vs 확장 요약">
  <div class="itpe-pipeline-node"><strong>&lt;&lt;include&gt;&gt; (포함)</strong><small>기본 → 포함 · 필수 실행 · 공통 모듈 재사용</small></div>
  <div class="itpe-pipeline-arrow">↕ 반대 성격</div>
  <div class="itpe-pipeline-node"><strong>&lt;&lt;extend&gt;&gt; (확장)</strong><small>확장 → 기본 · 조건부 실행 · 확장점(Extension Point) 명시</small></div>
</div>

### 3. 핵심 통제

- **명세서 연계**: 사전/사후 조건 및 기본/예외 이벤트 흐름을 상세 명세하여 모호성 제거
- **RTM 추적성**: 비즈니스 요구사항과 유스케이스 간 양방향 추적성 보증

## 출제 이력과 검증 출처

- 제137회 정보관리기술사 1교시: 유스케이스 다이어그램과 관계(&lt;&lt;include&gt;&gt;, &lt;&lt;extend&gt;&gt;)
- Ivar Jacobson, Object-Oriented Software Engineering: A Use Case Driven Approach
- Craig Larman, Applying UML and Patterns: An Introduction to Object-Oriented Analysis and Design

## 학습 체크

- [ ] 유스케이스 다이어그램의 4대 요소(액터, 유스케이스, 시스템 경계, 관계)를 설명할 수 있는가?
- [ ] &lt;&lt;include&gt;&gt;와 &lt;&lt;extend&gt;&gt;의 화살표 방향과 필수 실행 여부를 구분할 수 있는가?
- [ ] 유스케이스 명세서의 이벤트 흐름 3가지(기본, 대안, 예외)를 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [스크럼](./025_scrum.md)
- 연관 토픽: [UML 다이어그램 체계](./020_uml_diagrams.md), [요구공학](./040_requirements_engineering.md)
- 다음 토픽: [SW 규모·비용 산정](./027_sw_cost_estimation.md)
