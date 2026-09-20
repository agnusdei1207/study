---
title: "추상 클래스와 인터페이스(Abstract Class & Interface)"
category: "02-software-engineering"
tags:
  - "OOP"
  - "추상클래스"
  - "인터페이스"
  - "다형성"
  - "DIP"
  - "ISP"
  - "디폴트메서드"
date: "2026-09-20T22:47:00+09:00"
author: "기술사 수험생"
extra:
  model: "Antigravity-v2"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 객체지향 설계와 원칙을 거쳐 추상 클래스와 인터페이스로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>객체지향 설계·SOLID 원칙</span>
  <strong>추상 클래스와 인터페이스</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 객체지향 프로그래밍에서 구체적 구현을 감추고 공통 규약과 뼈대를 정의함으로써 다형성(Polymorphism)을 실현하고, 모듈 간 결합도를 낮추어 유연한 확장을 지원하는 핵심 추상화 메커니즘
- 메커니즘: 도메인 공통 속성·행위 식별 $\rightarrow$ 인터페이스(CAN-DO) 규약 명세 $\rightarrow$ 추상 클래스(IS-A) 템플릿 구현 $\rightarrow$ 구체 클래스 상속 및 다형적 인젝션 $\rightarrow$ 동적 바인딩 실행
- 산출물: UML 클래스 다이어그램 · 인터페이스 API 규약서 · 템플릿 기반 추상 클래스 · 다형적 구현체(Concrete Classes)

<div class="itpe-flow-map" role="img" aria-label="추상화 설계 파이프라인 및 결합도 판정 게이트">
  <div class="itpe-flow-node">
    <strong>1단계: 도메인 분석 및 공통 추상화 도출</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>추출</strong><span>도메인 모델 간 공통 상태(필드)와 공통 행위(오퍼레이션)를 식별하여 상위 계층화</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 추상 타입 분리 (IS-A vs CAN-DO)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설계</strong><span>핵심 뼈대 확장은 추상 클래스(Single), 외부 연동 규약은 인터페이스(Multi)로 배정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 인터페이스 분리 원칙(ISP) 정제</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>정제</strong><span>단일 비대한 인터페이스를 클라이언트별 전용 인터페이스로 쪼개 불필요한 구현 배제</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 의존성 역전(DIP) 및 결합도 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>고수준 비즈니스 모듈이 구체 클래스가 아닌 인터페이스나 추상 타입에만 의존하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (느슨한 결합도 달성)</strong>
      <span>DIP 및 OCP 원칙 충족 $\rightarrow$ 테스트용 Mock 객체 주입 가능 및 런타임 동적 교체 보장</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (강한 결합도 / 구체 클래스 의존)</strong>
      <span>변경 파급 효과 발생 $\rightarrow$ 인터페이스 추출(Extract Interface) 및 DI(의존성 주입) 리팩토링</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `추상 클래스(Abstract Class)`: 하나 이상의 추상 메서드를 포함할 수 있으며, 상태(필드)와 구체 메서드를 통해 하위 클래스의 공통 뼈대를 제공하는 클래스 (`extends`, 단일 상속)
- `인터페이스(Interface)`: 클래스가 지켜야 할 행위 규약(Contract)을 선언하며, 다중 구현을 지원해 객체 간 결합도를 최소화하는 타입 (`implements`, 다중 구현)
- `다형성(Polymorphism)`: 동일한 인터페이스나 상위 타입 참조변수로 서로 다른 구체 객체의 메서드를 동적으로 호출(동적 바인딩)하는 객체지향 특성
- `DIP(Dependency Inversion Principle)`: 상위 모듈이 하위 모듈의 구현에 의존하지 않고 둘 다 추상화(인터페이스)에 의존해야 한다는 원칙
- `ISP(Interface Segregation Principle)`: 클라이언트는 자신이 사용하지 않는 메서드에 의존하지 않아야 하며, 인터페이스를 작고 명확하게 분리해야 한다는 원칙
- `Default Method(디폴트 메서드)`: 자바 8부터 인터페이스에 도입된 기본 구현 메서드로, 기존 구현체를 깨뜨리지 않고 하위 호환성을 유지하며 기능을 추가하는 기법

</details>

## 예상문제

> 객체지향 설계에서 유연성과 확장성을 확보하기 위해 사용되는 추상 클래스(Abstract Class)와 인터페이스(Interface)의 개념, 내부 동작 메커니즘, 구조적 차이점을 비교하고, 자바 8 이후 인터페이스의 변화(디폴트 메서드 등)에 따른 설계 전략을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| 객체지향 설계 원칙 | SOLID, DIP(의존성 역전), ISP(인터페이스 분리), OCP(개방 폐쇄) | Ⅰ·Ⅳ |
| 디자인 패턴 적용 | 템플릿 메서드 패턴(추상 클래스), 전략 패턴·어댑터 패턴(인터페이스) | Ⅱ·Ⅴ |
| 최신 언어 스펙 진화 | Default/Static Method, 함수형 인터페이스(@FunctionalInterface), 람다 식 | Ⅲ·Ⅵ·Ⅶ |

## Ⅰ. 객체지향 추상화와 다형성의 핵심 도구 개요

> 추상 클래스는 '무엇인가(IS-A)'라는 상속 계층의 정체성과 뼈대를 공유하고, 인터페이스는 '무엇을 할 수 있는가(CAN-DO)'라는 외부와의 통신 규약을 정의함.

- 정의:
  - **추상 클래스**: 인스턴스화할 수 없으며 하위 클래스에 구현을 강제하는 추상 메서드와 공통 상태/기본 구현을 함께 제공하는 클래스
  - **인터페이스**: 구현부가 없는 메서드들의 명세(자바 8 이전 기준)로서, 클래스가 외부와 소통하는 표준 규격(Contract)을 선언하는 추상 타입
- 목적: 구현 세부사항과 인터페이스의 분리를 통한 결합도(Coupling) 최소화 및 런타임 다형성(Polymorphism) 보장
- 필요성: 시스템 변경 시 하위 모듈의 수정이 상위 모듈로 전파되는 파급 효과(Ripple Effect) 차단

## Ⅱ. 추상 클래스와 인터페이스의 구조적 설계 메커니즘

> 설계 목적과 상속 계층에 따라 상호 보완적인 구조로 배치됨.

```text
[추상 클래스 구조 (IS-A)]               [인터페이스 구조 (CAN-DO)]
┌────────────────────────┐              ┌────────────────────────┐
│ abstract class Animal  │              │ interface Flyable      │
│  - String name; (상태) │              │  - fly(); (행위 규약)  │
│  + sleep() { 기본구현 } │              └───────────┬────────────┘
│  + abstract makeSound()│                          │ implements
└───────────┬────────────┘                          │
            │ extends                               ▼
┌───────────▼────────────┐              ┌────────────────────────┐
│ class Dog extends ...  │              │ class Bird implements  │
│  + makeSound() { 멍멍 }│              │  Flyable { fly() {..} }│
└────────────────────────┘              └────────────────────────┘
```

- **추상 클래스의 템플릿 메서드 패턴(Template Method)**: 상위 추상 클래스에서 전체 알고리즘 흐름을 `final` 메서드로 제어하고, 변경되는 세부 단계만 추상 메서드로 열어두어 하위 클래스가 오버라이딩하도록 유도
- **인터페이스의 전략 패턴(Strategy Pattern)**: 교체 가능한 비즈니스 알고리즘을 인터페이스로 캡슐화하여 런타임에 동적으로 주입(Dependency Injection)받아 실행

## Ⅲ. 추상 클래스 vs 인터페이스 핵심 비교

> 두 기술은 배타적 선택이 아니라, 골격 구현(Skeletal Implementation) 패턴처럼 함께 조합하여 사용될 때 최상의 유연성을 제공함.

| 비교 항목 | 추상 클래스 (Abstract Class) | 인터페이스 (Interface) |
|---|---|---|
| 관계의 본질 | IS-A 관계 ("~의 일종이다", 정체성) | CAN-DO 관계 ("~을 할 수 있다", 행위 명세) |
| 상속 방식 | 단일 상속만 지원 (`extends`) | 다중 구현 지원 (`implements`) |
| 멤버 변수 (상태) | 인스턴스 변수, 생성자, static 필드 보유 가능 | `public static final` 상수만 허용 |
| 접근 제어자 | `public`, `protected`, `private` 등 모두 지원 | 기본적으로 모든 메서드가 `public` |
| 생성자 보유 여부 | 생성자 보유 가능 (`super()` 호출로 초기화) | 생성자 보유 불가 (인스턴스 상태 없음) |
| 다이아몬드 문제 | 발생 불가 (단일 상속 제약) | 다중 상속 가능 (디폴트 메서드 충돌 시 수동 해결) |
| 주 활용 목적 | 관련 클래스 간의 코드 재사용 및 기본 뼈대 제공 | 모듈 간 느슨한 결합도 및 교체 가능한 행위 규약 정의 |

## Ⅳ. 자바 8 이후 인터페이스의 진화와 다이아몬드 문제 해결

> 인터페이스에 기본 구현이 가능해지면서 하위 호환성 유지와 함수형 프로그래밍 지원이 대폭 강화됨.

```text
               ┌───────────────────────┐
               │ interface A           │
               │  - default void log() │
               └───────────┬───────────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
┌─────────────────────────┐ ┌─────────────────────────┐
│ interface B extends A   │ │ interface C extends A   │
│  - default void log() B │ │  - default void log() C │
└────────────┬────────────┘ └────────────┬────────────┘
             │                           │
             └─────────────┬─────────────┘
                           ▼
              ┌─────────────────────────┐
              │ class D implements B, C │ ──> 다이아몬드 상속 충돌!
              │ + void log() {          │     해법: 컴파일러가 수동 재정의
              │     B.super.log();      │     또는 완전 재구현 강제
              │   }                     │
              └─────────────────────────┘
```

1. **디폴트 메서드(Default Method)**:
   - 배경: 자바 8에서 `Collection` 인터페이스에 `stream()`, `forEach()`를 추가할 때 기존 모든 서드파티 라이브러리가 깨지는 것을 방지하기 위해 도입
   - 충돌 해결 규칙: 클래스가 항상 이긴다(Class-wins rule). 인터페이스 간 중복 시 하위 클래스에서 명시적으로 오버라이딩 필수
2. **정적 메서드(Static Method) 및 Private 메서드**:
   - 인터페이스 자체에 유틸리티 메서드를 배치할 수 있게 되었으며, 자바 9부터는 인터페이스 내부 코드 재사용을 위한 `private` 메서드 지원
3. **함수형 인터페이스(@FunctionalInterface)**:
   - 단 하나의 추상 메서드(SAM: Single Abstract Method)만을 갖는 인터페이스로, 람다 식(Lambda Expression)과 메서드 참조의 타깃 타입으로 동작

## Ⅴ. 설계 패턴: 골격 구현(Skeletal Implementation) 패턴

> 인터페이스로 규약을 정의하고, 추상 클래스로 기본 구현을 제공하여 다중 상속의 유연성과 코드 재사용성을 동시에 달성함.

```text
[Interface (List)] ─────────────────────┐ (다중 구현 가능)
        ▲                               │
        │ implements                    ▼
[Abstract Class (AbstractList)] <── [Concrete Class (CustomList)]
 (공통 기본 구현 제공)                 (필요한 특수 기능만 오버라이딩)
```

- **이펙티브 자바 권고**: 인터페이스와 추상 골격 구현 클래스를 함께 제공함으로써 인터페이스의 장점(다중 구현)과 추상 클래스의 장점(구현 편의성)을 모두 흡수
- **적용 사례**: Java Collections Framework의 `List` 인터페이스 $\rightarrow$ `AbstractList` 추상 골격 $\rightarrow$ `ArrayList` 구현체

## Ⅵ. 객체지향 추상화 설계 위험 관리

> 과도한 상속과 비대한 인터페이스로 인한 시스템 경직성을 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 취약한 기반 클래스 문제 (Fragile Base Class) | 상속 대신 조합(Composition over Inheritance) 원칙 적용 | 상위 클래스 내부 변경이 하위 클래스 오작동으로 전파되는 결함 방지 |
| 인터페이스 오염 (Fat Interface) | ISP(인터페이스 분리 원칙)에 따라 역할별로 작게 쪼개어 정의 | 불필요한 빈 메서드 오버라이딩 방지 및 모듈 응집도 향상 |
| 디폴트 메서드 남용으로 인한 모호성 | 비즈니스 핵심 로직은 디폴트 메서드에서 배제하고 인터페이스 간 충돌 시 명시적 지정 | 다이아몬드 상속 모호성 제거 및 컴파일 타임 에러 조기 차단 |
| 런타임 캐스팅 에러 (ClassCastException) | 추상 타입과 제네릭(Generics)을 결합하여 컴파일 타임 타입 검증 | 무분별한 `instanceof` 다운캐스팅 제거 및 타입 안전성 확보 |

## Ⅶ. 기술사적 제언: 변화에 유연한 아키텍처를 위한 추상화 전략

> "상속은 강력하지만 결합도를 높이고, 인터페이스는 유연하지만 구조를 파편화할 수 있다."

### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 실무에서 추상 클래스는 단일 도메인의 명확한 뼈대와 공통 상태가 존재할 때만 보수적으로 사용해야 하며, 대부분의 컴포넌트 간 협력은 인터페이스를 매개로 설계해야 유연한 단위 테스트와 확장이 가능함.
- `나라면`: 상속 계층의 깊이를 최대 2단계 이내로 엄격히 제한하고, 프레임워크 뼈대를 제공하는 경우를 제외하고는 인터페이스 기반의 DI 구조를 디폴트 설계 표준으로 수립하겠음.

### 실전 답안용 기술사적 제언
- 판정: 객체지향 시스템의 유지보수성은 **DIP(의존성 역전 원칙)** 준수 여부와 **인터페이스 분리도**에 의해 판가름 남
- 대안: 역할 기반 소형 인터페이스 정의 $\rightarrow$ 의존성 주입(DI) 파이프라인 구성 $\rightarrow$ 공통 골격 필요 시에만 추상 클래스 병행
- 검증: 아키텍처 린트(ArchUnit)를 통한 구체 클래스 직접 참조 차단 및 모의 객체(Mock) 단위 테스트 커버리지 80% 이상 확보
- 효과: 신규 비즈니스 요구사항 추가 시 기존 코드 수정 없이 플러그인 방식으로 확장 가능(OCP 달성)

```text
[현행 한계] ─────────> [개선 방안] ─────────> [검증 기준] ─────────> [실행 효과]
구체 클래스 직접 참조   인터페이스 추출 & DI   ArchUnit 규칙 강제      결합도 최소화
비대한 인터페이스 난립   ISP 기반 세분화 분할   단위 Mock 테스트 통과   OCP 기반 확장성 확보
```

## 1교시 10점 답안 발췌

```text
1. 추상 클래스와 인터페이스의 정의
- 추상 클래스: 추상 메서드와 구현 메서드/상태를 함께 가질 수 있는 단일 상속(IS-A) 기반의 뼈대 클래스
- 인터페이스: 객체가 수행해야 할 행위 규약(CAN-DO)을 명세하는 다중 구현 기반의 표준 추상 타입

2. 핵심 메커니즘 및 속성 비교
┌─────────────────┬───────────────────────┬───────────────────────┐
│ 구분            │ 추상 클래스           │ 인터페이스            │
├─────────────────┼───────────────────────┼───────────────────────┤
│ 관계 & 상속     │ IS-A 관계 / 단일 상속 │ CAN-DO 관계 / 다중구현│
│ 멤버 & 상태     │ 인스턴스 변수, 생성자 │ 상수만 가능 (static)  │
│ 주요 설계 패턴  │ 템플릿 메서드 패턴    │ 전략 패턴, 어댑터     │
└─────────────────┴───────────────────────┴───────────────────────┘

3. 자바 8 이후의 진화 및 아키텍처적 시사점
- 디폴트 메서드(Default Method) 도입으로 기존 구현체 하위 호환성 유지하며 기능 확장 지원
- 권장 설계: 인터페이스로 행위 규약을 선언하고, 추상 골격 클래스(Skeletal Implementation)를 조합하여 유연성과 재사용성을 동시 달성
```

## 출제 이력과 검증 출처

- **공식 출제 이력**: 정보관리기술사 제108회 1교시 단답형 (객체지향 추상화와 다형성), 제119회 2교시 논술형 (인터페이스와 추상 클래스 비교 및 자바 디폴트 메서드)
- **표준 및 권고 기준**: [Oracle Java Language Specification (Interfaces)](https://docs.oracle.com/javase/specs/jls/se17/html/jls-9.html), Joshua Bloch, Effective Java 3rd Edition (Item 20: 인터페이스를 정의한 뒤 골격 구현 클래스를 제공하라)

## 학습 체크

- [ ] [Ⅰ 개요]: IS-A와 CAN-DO 관점에서 추상 클래스와 인터페이스의 본질을 구분하였는가?
- [ ] [Ⅲ 비교]: 상속 방식, 멤버 상태 보유, 생성자 유무의 차이를 도표로 명확히 제시하였는가?
- [ ] [Ⅳ 진화]: 자바 8 디폴트 메서드의 도입 배경과 다이아몬드 상속 충돌 해결 규칙을 기술하였는가?
- [ ] [Ⅴ 패턴]: 골격 구현(Skeletal Implementation) 패턴을 통해 두 개념을 조화시키는 대안을 제시하였는가?

## 연결 토픽

- [객체지향 설계 원칙(SOLID)](./002_solid/) · [디자인 패턴(GoF)](./003_design_pattern/) · [클래스 다이어그램](./013_class_diagram/) · [의존성 주입(DI)](./159_spring_boot/)
