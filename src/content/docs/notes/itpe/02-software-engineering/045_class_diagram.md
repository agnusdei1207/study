---
title: "클래스 다이어그램(Class Diagram)"
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

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 UML 정적 모델과 객체지향 구조를 거쳐 클래스 다이어그램으로 이어지는 지식 위치"><span>소프트웨어 공학</span><span>UML · 정적 구조 모델</span><strong>클래스 다이어그램</strong></div>

## 큰 그림과 30초 인출

- 본질: **UML(Unified Modeling Language) Class Diagram**은 분류자의 특성과 관계를 표현하는 정적 구조 모델
- 메커니즘: 클래스의 이름·속성·오퍼레이션을 구획하고 연관·일반화·실체화·의존 관계를 연결함
- 산출: 책임·다중성·탐색 방향·생명주기 소유권이 명시된 설계 모델

<div class="itpe-pipeline is-vertical" role="img" aria-label="클래스 다이어그램의 클래스 내부와 외부 관계">
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>클래스 구획</strong></span><span><b>구성</b> 이름 · 속성 · 오퍼레이션<br /><b>표기</b> 가시성 · 타입 · 매개변수</span></div><div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>관계 명세</strong></span><span><b>구성</b> 연관 · 일반화 · 실체화 · 의존<br /><b>표기</b> 다중성 · 역할 · 탐색 방향</span></div><div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>소유권 판정</strong></span><span><b>구성</b> 집약 · 합성<br /><b>판정</b> 공유 여부 · 생명주기 종속</span></div>
</div>

<details><summary>핵심 용어</summary>

- **UML(Unified Modeling Language)**: 소프트웨어 구조와 행위를 공통 기호로 명세·시각화하는 모델링 언어
- **Multiplicity(다중성)**: 관계 끝에서 허용되는 인스턴스 수 범위를 나타내는 제약
- **Generalization(일반화)**: 하위 분류자가 상위 분류자의 특성을 상속하는 is-a 관계
- **Realization(실체화)**: 구현 분류자가 명세 분류자의 계약을 수행하는 관계
- **Aggregation(집약)**: 부분이 전체와 독립적으로 존재하고 공유될 수 있는 약한 전체-부분 관계
- **Composition(합성)**: 부분이 한 전체에 배타적으로 속하고 생명주기를 함께하는 강한 전체-부분 관계

</details>

## 예상문제

> UML 클래스 다이어그램의 구성요소와 관계 표기법을 설명하고, 집약과 합성을 비교한 후 정적 구조 모델의 품질 확보 방안을 제시하시오.

## Ⅰ. 객체지향 시스템의 정적 구조 모델

> 클래스 다이어그램은 코드 목록이 아니라 책임과 관계 제약을 합의하는 모델이며, 정확성은 기호 수보다 다중성과 소유권의 일관성으로 판정함.

- 정의: **클래스**의 특성과 **정적 관계**를 **UML 표기법**으로 명세하는 구조 다이어그램
- 목적: 책임·타입·관계 제약의 공통 이해 확보 → 설계·구현·검증 간 구조 정합성 유지

## Ⅱ. 클래스의 3단 구획과 가시성

> 구획에는 의사결정에 필요한 도메인 특성만 남기고 기계적으로 생성되는 접근자는 생략해야 모델의 책임 경계가 보임.

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" style="max-width: 520px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="cd-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Left: 3-Compartment Class Box -->
  <rect x="15" y="15" width="220" height="190" rx="6" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="2" filter="url(#cd-shadow)"/>
  
  <!-- Section 1: Name -->
  <rect x="15" y="15" width="220" height="42" rx="6" fill="var(--sl-color-blue-subtle, #eff6ff)"/>
  <text x="125" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-text-muted, #4b5563)">&lt;&lt;Entity&gt;&gt;</text>
  <text x="125" y="49" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--sl-color-blue-high, #2563eb)">Order</text>
  <line x1="15" y1="57" x2="235" y2="57" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1.5"/>

  <!-- Section 2: Attributes -->
  <text x="25" y="75" font-size="9.5" fill="var(--sl-color-text, #1f2937)">- orderId: String</text>
  <text x="25" y="93" font-size="9.5" fill="var(--sl-color-text, #1f2937)">- orderDate: Date</text>
  <text x="25" y="111" font-size="9.5" fill="var(--sl-color-text, #1f2937)"># totalAmount: Money</text>
  <line x1="15" y1="122" x2="235" y2="122" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1.5"/>

  <!-- Section 3: Operations -->
  <text x="25" y="142" font-size="9.5" fill="var(--sl-color-text, #1f2937)">+ calculateTotal(): Money</text>
  <text x="25" y="160" font-size="9.5" fill="var(--sl-color-text, #1f2937)">+ cancel(): Boolean</text>
  <text x="25" y="178" font-size="9.5" fill="var(--sl-color-text, #1f2937)">~ notifyUser(): void</text>
  <text x="25" y="196" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">가시성: +Public, -Private, #Protected, ~Package</text>

  <!-- Right: 6 Key Relationships -->
  <rect x="255" y="15" width="250" height="190" rx="8" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1.5" filter="url(#cd-shadow)"/>
  <text x="268" y="36" font-size="11.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">UML 6대 관계 표기법</text>

  <!-- Rel 1: Generalization -->
  <line x1="270" y1="58" x2="350" y2="58" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <polygon points="350,53 362,58 350,63" fill="none" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <text x="372" y="61" font-size="9.5" fill="var(--sl-color-text, #1f2937)">일반화 (is-a 상속)</text>

  <!-- Rel 2: Realization -->
  <line x1="270" y1="84" x2="350" y2="84" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5" stroke-dasharray="4 3"/>
  <polygon points="350,79 362,84 350,89" fill="none" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <text x="372" y="87" font-size="9.5" fill="var(--sl-color-text, #1f2937)">실체화 (인터페이스 구현)</text>

  <!-- Rel 3: Composition -->
  <polygon points="270,110 279,105 288,110 279,115" fill="var(--sl-color-text, #1f2937)" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <line x1="288" y1="110" x2="362" y2="110" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <text x="372" y="113" font-size="9.5" font-weight="700" fill="var(--sl-color-red-high, #dc2626)">합성 (생명주기 종속)</text>

  <!-- Rel 4: Aggregation -->
  <polygon points="270,136 279,131 288,136 279,141" fill="none" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <line x1="288" y1="136" x2="362" y2="136" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <text x="372" y="139" font-size="9.5" fill="var(--sl-color-text, #1f2937)">집약 (독립적 부분-전체)</text>

  <!-- Rel 5: Association -->
  <line x1="270" y1="162" x2="362" y2="162" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <text x="372" y="165" font-size="9.5" fill="var(--sl-color-text, #1f2937)">연관 (1 .. * 구조적 참조)</text>

  <!-- Rel 6: Dependency -->
  <line x1="270" y1="188" x2="354" y2="188" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5" stroke-dasharray="4 3"/>
  <polyline points="346,183 356,188 346,193" fill="none" stroke="var(--sl-color-text, #1f2937)" stroke-width="1.5"/>
  <text x="372" y="191" font-size="9.5" fill="var(--sl-color-text, #1f2937)">의존 (일시적 파라미터 사용)</text>
</svg>
</div>

| 구획 | 표기 | 판정 |
|---|---|---|
| 이름 | 스테레오타입 · 클래스명 | 추상화 수준과 역할 식별 |
| 속성 | `가시성 이름: 타입` | 상태와 정보은닉 경계 |
| 오퍼레이션 | `가시성 이름(매개변수): 반환타입` | 외부에 제공하는 책임 |

- **가시성**: Public `+` · Private `-` · Protected `#` · Package `~`
- **추상 표기**: 추상 클래스·오퍼레이션은 이탤릭체, 인터페이스는 스테레오타입 등 UML 표기 적용

## Ⅲ. 관계의 의미와 표기

> 관계는 선 모양을 외우는 데서 끝나지 않고 참조 지속성·계약 이행·상속·소유권 중 무엇을 뜻하는지 코드와 일치해야 함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="시험장에서 재현하는 UML 클래스와 관계 기호">
  <div class="itpe-pipeline-node"><strong>Order</strong><span><b>속성</b> -orderNo: String<br /><b>오퍼레이션</b> +total(): Money</span></div>
  <div class="itpe-pipeline-arrow"><strong>◆ 합성</strong><br /><span>다중성 1 : 1..*</span><br />↓</div>
  <div class="itpe-pipeline-node"><strong>OrderItem</strong><span><b>소유</b> Order에 배타적으로 귀속<br /><b>생명주기</b> Order와 함께 생성·삭제</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>관계 기호</strong><span><b>일반화</b> ──▷ · <b>실체화</b> - -▷<br /><b>집약</b> ◇── · <b>합성</b> ◆──</span></div>
</div>

| 관계 | 표기 | 의미 | 검증 질문 |
|---|---|---|---|
| **Association** | 실선 | 구조적 참조 | 다중성·역할·탐색 방향이 맞는가 |
| **Dependency** | 점선 화살표 | 일시적 사용 | 매개변수·지역 사용에 그치는가 |
| **Generalization** | 실선·빈 삼각형 | 특성 상속 | 치환 가능한 is-a 관계인가 |
| **Realization** | 점선·빈 삼각형 | 계약 구현 | 명세의 오퍼레이션을 이행하는가 |
| **Aggregation** | 전체 쪽 빈 마름모 | 공유 가능한 부분 | 부분이 독립·공유 가능한가 |
| **Composition** | 전체 쪽 채운 마름모 | 배타적 소유 | 부분의 생명주기가 전체에 종속되는가 |

## Ⅳ. 집약과 합성의 경계 판정 및 실무 위험 대책

> 전체-부분이라는 말만으로 합성을 선택하면 안 되며, 배타적 소유와 생성·삭제 책임이 모두 성립할 때만 강한 생명주기 관계를 표시함.

| 기준 | 집약 | 합성 |
|---|---|---|
| 소유 | 공유 가능 | 한 전체에 배타적 |
| 생명주기 | 부분 독립 | 전체에 종속 |
| 이동 | 다른 전체로 이전 가능 | 소유 경계 안에서 관리 |
| 표기 | 빈 마름모 | 채운 마름모 |
| 구현 판단 | 일반 참조로 충분한지 확인 | 생성·삭제·무결성 규칙 동반 |

### 실무 클래스 모델링 위험 및 대책

| 위험 | 대책 | 효과 |
|---|---|---|
| **집약·합성 소유권 혼동** | 객체 생명주기(Lifecycle) 종속성 기준 배타적 소유 엄격 판정 | 메모리 누수 및 고아 객체(Orphan) 발생 원천 차단 |
| **다중성(Multiplicity) 누락** | `1..*`, `0..1` 등 양방향 다중성 명시 및 Nullable 제약 검증 | 런타임 NullPointerException 및 데이터 정합성 결함 예방 |
| **과도한 상속 결합 (is-a 왜곡)** | 상속보다 합성(Composition over Inheritance) 원칙 우선 적용 | 클래스 폭발 방지 및 유연한 객체 확장성 확보 |

## Ⅴ. 모델과 구현의 양방향 정합성

> 클래스 다이어그램의 가치는 문서 완성이 아니라 구현 변화 뒤에도 핵심 책임·다중성·소유권이 유지되는 데 있음.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 집약과 합성의 차이는 마름모 색이 아니라 누가 부분의 생명주기를 소유하는가에 있다. 소유권이 모호하면 삭제와 무결성 정책도 모호해진다.
- `나라면`: 핵심 도메인 클래스와 관계 제약만 모델링하고, 코드 리뷰에서 다중성·상속·합성의 구현 정합성을 함께 확인하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 장식적 관계선 배제, 객체 생명주기 배타적 소유(합성)와 다중성(`1..*`, `0..1`) 표기 필수 판정
- **대응 방안**: 상속(Generalization) 남용 지양 및 합성(Composition over Inheritance) 기반 유연한 설계 원칙 적용
- **검증 체계**: 모델-코드 간 정적 분석(ArchUnit) 자동 검증 및 다중성 불일치/고아 객체 참조 여부 PR 게이트 통제
- **기대 효과**: 객체지향 무결성 확보, 런타임 NullPointerException 예방 및 시스템 리팩토링 유지보수성 50% 향상

<div class="itpe-pipeline is-vertical" role="img" aria-label="클래스 다이어그램 품질 개선 제언"><div class="itpe-pipeline-node"><strong>표기 중심 모델</strong><span><b>문제</b> 다중성·역할·소유권 해석 불일치</span></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>관계 의미 규칙</strong><span><b>대안</b> 참조 지속성·치환성·생명주기 질문 적용</span></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>모델-코드 대조</strong><span><b>판정</b> 관계·다중성·생성·삭제 규칙 일치</span></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>정적 구조 정합성</strong><span><b>효과</b> 변경 영향과 무결성 경계 명료화</span></div></div>

## 1교시 10점 답안 발췌

- 정의: **UML(Unified Modeling Language) Class Diagram**은 **클래스**의 특성과 **정적 관계**를 명세하는 구조 다이어그램
- 목적: 책임·타입·관계 제약의 공통 이해 확보 → 설계와 구현의 구조 정합성 유지

<div class="itpe-pipeline is-vertical" role="img" aria-label="클래스 다이어그램 1교시 핵심 그림"><div class="itpe-pipeline-node"><strong>Order</strong><span><b>속성</b> -orderNo: String<br /><b>오퍼레이션</b> +total(): Money</span></div><div class="itpe-pipeline-arrow"><strong>◆ 합성</strong><br /><span>다중성 1 : 1..*</span><br />↓</div><div class="itpe-pipeline-node"><strong>OrderItem</strong><span><b>소유</b> Order에 배타적으로 귀속<br /><b>생명주기</b> Order와 함께 생성·삭제</span></div></div>

| 관계 | 기호 | 의미 |
|---|---|---|
| 일반화·실체화 | `──▷` · `- -▷` | 상속 · 계약 구현 |
| 집약·합성 | `◇──` · `◆──` | 독립 생명주기 · 종속 생명주기 |
| 연관·의존 | `──` · `- ->` | 구조적 참조 · 일시적 사용 |

- 결론: **Multiplicity(다중성)**와 생명주기 소유권을 코드와 대조하여 관계의 의미를 보존함

## 출제 이력과 검증 출처

- [Object Management Group, UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/About-UML)
- [Object Management Group, UML resources](https://www.omg.org/uml/)

## 학습 체크

- [ ] Ⅰ·정의와 목적: 클래스·정적 관계·UML 표기법의 관계를 두 줄로 재현할 수 있는가
- [ ] Ⅱ·구획: 이름·속성·오퍼레이션 형식과 네 가시성 기호를 쓸 수 있는가
- [ ] Ⅲ·관계: 여섯 관계의 선 표기·의미·검증 질문을 연결할 수 있는가
- [ ] Ⅳ·비교: 집약과 합성을 소유·생명주기·이동·구현으로 비교할 수 있는가
- [ ] Ⅴ·제언: 모델과 코드의 네 대조 대상을 설명할 수 있는가

## 연결 토픽

- 이전 토픽: [정렬 알고리즘](./043_sort_algorithm.md)
- 연관 토픽: [UML 다이어그램](./020_uml_diagrams.md), [객체지향 설계원칙 SOLID](./082_solid.md), [모듈성](./190_modularity.md)
- 다음 토픽: [AI Native 개발 플랫폼](./046_ai_native_dev_platform.md)
