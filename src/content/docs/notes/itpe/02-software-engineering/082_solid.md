---
title: "객체지향 설계원칙 SOLID(DIP 포함)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
date: "2026-09-20T22:00:00+09:00"
lastmod: "2026-09-20T22:00:00+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

> **소프트웨어공학 > 객체지향 및 아키텍처 설계 > 객체지향 설계원칙 SOLID**

---

## 1. 큰 그림 및 30초 인출 공식

```
               [ 객체지향 5대 설계 원칙 (SOLID) 구조 ]
  ┌────────────────────────────────────────────────────────┐
  │ 1. SRP (단일 책임)   : 변경의 이유는 오직 하나         │
  │ 2. OCP (개방-폐쇄)   : 확장은 열리고 수정은 닫힘       │
  │ 3. LSP (리스코프 치환): 상위 타입 대체 무결성 보장     │
  │ 4. ISP (인터페이스 분리): 클라이언트 맞춤형 분할       │
  │ 5. DIP (의존관계 역전): 추상화에 의존, 구현체 역전     │
  └────────────────────────────────────────────────────────┘
```

> **30초 인출 공식 (키워드 체인)**:  
> **Uncle Bob 5원칙** ➔ **SRP (단일 액터)** ➔ **OCP (추상화 다형성)** ➔ **LSP (계약에 의한 설계)** ➔ **ISP (인터페이스 세분화)** ➔ **DIP (고수준 중심 의존 역전)** ➔ **클린/헥사고날 아키텍처**

- **본질**: **SOLID**는 변경 요구사항이 발생했을 때 **기존의 검증된 코드를 뜯어고치지 않고(OCP), 새로운 코드만 안전하게 덧붙여 확장할 수 있게 만드는 객체지향 5대 설계 원칙**
- **메커니즘**: 단일 책임 분리(SRP) ➔ 인터페이스 맞춤 분할(ISP) ➔ 다형성 치환(LSP) ➔ 고수준 코어 중심 의존 역전(DIP) ➔ 사이드이펙트 없는 무중단 확장(OCP)
- **산출물**: 고응집·저결합 클래스 다이어그램 · 클린/헥사고날 아키텍처 포트 규격 · Mock 테스트 가능한 단위 코드베이스

---

## 2. 핵심 용어 정리

| 용어 | 영문 표기 | 핵심 정의 및 설명 |
|---|---|---|
| **SRP** | Single Responsibility Principle | 하나의 클래스는 오직 하나의 단일 책임(하나의 액터 및 변경 사유)만 가져야 한다는 원칙 |
| **OCP** | Open-Closed Principle | 소프트웨어 개체는 확장에 대해서는 열려 있어야 하고, 수정에 대해서는 닫혀 있어야 한다는 원칙 |
| **LSP** | Liskov Substitution Principle | 하위 클래스는 상위 클래스의 책임을 온전히 수행할 수 있어야 하며 대체 가능해야 한다는 원칙 |
| **ISP** | Interface Segregation Principle | 클라이언트는 자신이 사용하지 않는 메서드에 의존하지 않도록 인터페이스를 작게 분리해야 한다는 원칙 |
| **DIP** | Dependency Inversion Principle | 고수준 모듈은 저수준 모듈에 의존해서는 안 되며, 둘 다 추상화(인터페이스)에 의존해야 한다는 원칙 |
| **의존성 주입** | Dependency Injection (DI) | 객체가 직접 의존 대상을 생성하지 않고 외부(컨테이너)로부터 주입받아 결합도를 낮추는 기법 |
| **제어의 역전** | Inversion of Control (IoC) | 프로그램의 제어 흐름 주도권이 개발자 코드에서 프레임워크나 런타임 컨테이너로 넘어가는 현상 |
| **계약에 의한 설계** | Design by Contract (DbC) | 사전조건 약화 금지, 사후조건 강화 보장 등 상하위 클래스 간의 계약 무결성을 명시하는 기법 |
| **코드 스멜** | Code Smell | 가독성 저하, 중복, 강결합 등 잠재적 버그와 유지보수 비용을 증가시키는 나쁜 코드 징후 |
| **헥사고날 아키텍처** | Hexagonal Architecture | DIP 원리를 시스템 아키텍처로 확장하여 도메인 코어와 외부 인프라를 포트와 어댑터로 격리하는 구조 |

---

## 3. 25점형 답안 프레임워크

### Ⅰ. 객체지향 설계원칙 SOLID의 개요

#### 1. SOLID 원칙의 정의 및 지향점
- **정의**: 시스템 변경에 유연하게 대처하고 코드의 재사용성과 테스트 용이성을 극대화하기 위해 객체지향 설계에서 준수해야 할 5가지 구조적 원칙.
- **지향점**:
  - **응집도 극대화**: 단일 목적 중심의 모듈 구성(SRP, ISP).
  - **결합도 최소화**: 구체 구현 대신 추상화된 규격 중심 결합(DIP, OCP).
  - **신뢰성 보장**: 다형성 활용 시 런타임 계약 무결성 유지(LSP).

```
   [고객 요구사항의 빈번한 변경]
                 │
                 ▼
 ┌────────────────────────────────────────────────────────┐
 │           SOLID 5대 원칙 기반 아키텍처 설계            │
 │  SRP(단일 책임)  ISP(인터페이스 분리) ──▶ 응집도 극대화 │
 │  DIP(의존 역전)  OCP(개방-폐쇄)     ──▶ 결합도 최소화 │
 │  LSP(치환 원칙)                    ──▶ 다형성 무결성 │
 └────────────────────────────────────────────────────────┘
                 │
                 ▼
   [사이드이펙트 제로화 / 유연한 확장성 / TDD 환경 확보]
```

---

### Ⅱ. SOLID 5대 핵심 원칙 상세 분석

#### 1. 5대 원칙 매핑 및 코드 스멜 비교
| 원칙 | 핵심 메커니즘 | 위반 시 발생하는 코드 스멜 (Smell) | 공학적 해결 방안 |
|---|---|---|---|
| **SRP** (단일 책임) | 한 클래스는 하나의 변경 이유(단일 액터)만 책임짐 | 거대 만능 객체(God Object), 엉뚱한 로직 수정에 따른 연쇄 결함 | 클래스 역할 분리, 파사드(Facade) 도입 |
| **OCP** (개방-폐쇄) | 기능 확장은 다형성으로 열고, 기존 코드는 폐쇄 | 신규 기능 추가 시 기존 `if-else`/`switch` 조건문 대량 수정 | 인터페이스 추출, 전략(Strategy) 패턴 적용 |
| **LSP** (리스코프 치환) | 서브타입은 언제나 슈퍼타입으로 완전히 치환 가능 | `instanceof` 타입 분기 남발, 하위 클래스에서 상위 예외 던짐 | 상속 대신 합성(Composition) 사용, 인터페이스 분리 |
| **ISP** (인터페이스 분리) | 클라이언트는 미사용 메서드에 강제 의존하지 않음 | 빈 껍데기 메서드 구현(`throw UnsupportedException`), 인터페이스 비대화 | 역할 인터페이스(Role Interface)로 잘게 분할 |
| **DIP** (의존관계 역전) | 고수준 정책이 저수준 기술 구현체에 종속되지 않음 | 비즈니스 로직 내부 `new DBRepository()` 강결합 | 인터페이스 소유권 역전, 생성자 DI 주입 |

---

### Ⅲ. 의존관계 역전 원칙(DIP) 심층 분석

#### 1. 전통적 의존 vs DIP 의존 구조 비교

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="220" style="background: var(--vp-c-bg-alt); border: 1px solid var(--vp-c-border); border-radius: 8px;">
  <defs>
    <marker id="solid-arrow-r" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#e06c75" />
    </marker>
    <marker id="solid-arrow-b" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--vp-c-brand)" />
    </marker>
    <marker id="solid-arrow-impl" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#10b981" />
    </marker>
  </defs>

  <!-- Title Header -->
  <rect x="15" y="10" width="490" height="24" rx="4" fill="var(--vp-c-bg)" stroke="var(--vp-c-border)" />
  <text x="260" y="26" font-size="10.5" font-weight="700" fill="var(--vp-c-brand)" text-anchor="middle">의존관계 역전 원칙(DIP) 구조 비교 : 직접 의존 vs 추상화 의존</text>

  <!-- Left Side: Traditional Coupling -->
  <rect x="15" y="42" width="235" height="165" rx="6" fill="var(--vp-c-bg)" stroke="var(--vp-c-border)" stroke-width="1.2" />
  <text x="132" y="60" font-size="9.5" font-weight="700" fill="#e06c75" text-anchor="middle">[전통적 구조] 상위가 하위에 직접 종속</text>
  <line x1="25" y1="67" x2="240" y2="67" stroke="var(--vp-c-border)" stroke-dasharray="2 2" />

  <rect x="35" y="76" width="195" height="34" rx="4" fill="var(--vp-c-bg-alt)" stroke="var(--vp-c-border)" />
  <text x="132" y="90" font-size="8.5" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">OrderService (고수준 정책)</text>
  <text x="132" y="102" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">핵심 비즈니스 주문 로직</text>

  <!-- Dependency Arrow Down -->
  <line x1="132" y1="110" x2="132" y2="136" stroke="#e06c75" stroke-width="1.8" marker-end="url(#solid-arrow-r)" />
  <text x="156" y="127" font-size="7.5" fill="#e06c75">직접 의존 (new)</text>

  <rect x="35" y="140" width="195" height="34" rx="4" fill="var(--vp-c-bg-alt)" stroke="var(--vp-c-border)" />
  <text x="132" y="154" font-size="8.5" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">MySQLRepository (저수준 구현)</text>
  <text x="132" y="166" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">특정 RDBMS SQL 쿼리 종속</text>

  <text x="132" y="194" font-size="7.5" fill="#e06c75" text-anchor="middle">DB 변경 시 비즈니스 수정 불가피 · Mock 불가</text>

  <!-- Right Side: DIP Applied -->
  <rect x="270" y="42" width="235" height="165" rx="6" fill="var(--vp-c-bg)" stroke="var(--vp-c-brand)" stroke-width="1.2" />
  <text x="387" y="60" font-size="9.5" font-weight="700" fill="var(--vp-c-brand)" text-anchor="middle">[DIP 적용] 둘 다 추상화(인터페이스)에 의존</text>
  <line x1="280" y1="67" x2="495" y2="67" stroke="var(--vp-c-border)" stroke-dasharray="2 2" />

  <rect x="290" y="74" width="195" height="32" rx="4" fill="var(--vp-c-bg-alt)" stroke="var(--vp-c-border)" />
  <text x="387" y="88" font-size="8.5" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">OrderService (고수준 정책)</text>
  <text x="387" y="100" font-size="7.5" fill="var(--vp-c-brand)" text-anchor="middle">인터페이스 소유권 보유</text>

  <!-- Dependency Arrow to Interface -->
  <line x1="387" y1="106" x2="387" y2="116" stroke="var(--vp-c-brand)" stroke-width="1.8" marker-end="url(#solid-arrow-b)" />

  <rect x="290" y="118" width="195" height="32" rx="4" fill="var(--vp-c-bg)" stroke="var(--vp-c-brand)" stroke-width="1.2" />
  <text x="387" y="131" font-size="8" fill="var(--vp-c-brand)" text-anchor="middle">&lt;&lt;interface&gt;&gt; OrderRepositoryPort</text>
  <text x="387" y="143" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">추상화된 데이터 저장 규격</text>

  <!-- Implementation Arrow from Bottom -->
  <line x1="387" y1="168" x2="387" y2="154" stroke="#10b981" stroke-width="1.8" stroke-dasharray="3 3" marker-end="url(#solid-arrow-impl)" />

  <rect x="290" y="170" width="195" height="30" rx="4" fill="var(--vp-c-bg-alt)" stroke="var(--vp-c-border)" />
  <text x="387" y="184" font-size="8" font-weight="700" fill="#10b981" text-anchor="middle">MySQL / Mongo / Mock (저수준 구현체)</text>
  <text x="387" y="194" font-size="7" fill="var(--vp-c-text-2)" text-anchor="middle">DI 컨테이너가 런타임 주입 (IoC)</text>
</svg>
</div>

#### 2. DIP 구현 핵심 메커니즘
- **인터페이스 소유권의 역전**: `OrderRepository` 인터페이스는 인프라 패키지가 아닌, 비즈니스 도메인 패키지에 함께 위치하여 비즈니스 계층이 인터페이스의 형태를 주도함.
- **제어의 역전(IoC) 및 의존성 주입(DI)**: 런타임에 프레임워크 컨테이너(Spring 등)가 구현체를 외부에서 주입함으로써 비즈니스 코드는 순수 POJO 상태를 유지하며 단위 테스트(Mocking)가 완벽히 가능해짐.

---

### Ⅳ. SOLID 적용 시 3대 위험 및 대응 전략

| 위험 | 대책 | 효과 |
|---|---|---|
| **원칙의 맹목적 적용으로 인한 클래스 및 인터페이스 폭증** | YAGNI 원칙 병행 및 도메인 복잡도에 따라 빈번한 변경 영역에 선별 적용 | 불필요한 추상화 오버헤드 방지 및 코드 탐색성 유지 |
| **상속 오용으로 인한 LSP 파괴 및 런타임 예외 발생** | '상속보다는 합성(Composition over Inheritance)' 설계 지침 표준화 | 다형성 계약 준수 및 런타임 다운캐스팅 결함 차단 |
| **하위 구현체 변경 시 비즈니스 레이어 오염** | 헥사고날 포트-어댑터 패턴 및 생성자 기반 DI 아키텍처 강제 | 인프라 변경 시 도메인 코드 보존율 100% 확보 |

---

### Ⅴ. 결론: DIP 기반 현대적 클린·헥사고날 아키텍처로의 진화

### 학습자 통찰 메모 — 답안 밖

```text
[핵심 통찰]
SOLID 원칙의 5가지 요소 중 가장 강력한 파급력을 지닌 원칙은 OCP와 DIP이다.
DIP(의존관계 역전)는 단순히 스프링 프레임워크의 `@Autowired`나 생성자 주입을 쓰는 기법이 아니라,
"비즈니스 도메인 규칙이 데이터베이스나 외부 통신 기술 같은 세부 구현체에 휘둘리지 않도록 격리하는 소프트웨어의 헌법"이다.
DIP를 클래스 레벨에서 시스템 아키텍처 레벨로 스케일업한 것이 바로 엉클 밥의 '클린 아키텍처(Clean Architecture)'이자 앨리스터 코번의 '헥사고날(Ports & Adapters) 아키텍처'이다.
기술사 답안에서는 5대 원칙을 각각 나열하는 데 그치지 않고, DIP를 중심으로 전체 원칙이 어떻게 유기적으로 결합하여 아키텍처 독립성을 달성하는지 보여주어야 한다.

[나라면 이렇게 쓴다]
1단락: SOLID 5대 원칙의 도입 목적(변경에 유연한 고응집·저결합 구조) 제시.
2단락: 5대 원칙별 메커니즘과 위반 코드 스멜 표 제시, DIP의 의존 역전 메커니즘 도식화.
3단락: DIP 기반 헥사고날(포트-어댑터) 아키텍처 연계 및 과도한 추상화 방지를 위한 실용적 엔지니어링 거버넌스 제언.
```

### 실전 답안용 기술사적 제언

- **판정 기준**: 신규 기능 추가 또는 외부 벤더 API 변경 시, 핵심 도메인 서비스 클래스 코드에 `import` 변경이나 메서드 수정이 발생하는지 여부를 기준으로 아키텍처 결합도를 판정해야 함.
- **대응 방안**: 비즈니스 코어가 외부 인프라 기술에 종속되지 않도록 **인바운드/아웃바운드 포트(인터페이스)를 코어 내부에 두고 어댑터가 이를 실체화하는 헥사고날 아키텍처**를 전면 표준화해야 함.
- **검증 체계**: ArchUnit 등 아키텍처 검증 도구를 CI 파이프라인에 통합하여, 도메인 레이어가 인프라 레이어를 직접 참조하는 코드 커밋을 빌드 단계에서 원천 차단해야 함.
- **기대 효과**: 데이터베이스 교체나 외부 API 규격 변경 시 도메인 비즈니스 로직 수정 제로화(0%)를 달성하고, 완벽한 Mocking 기반의 고속 단위 테스트 환경을 보장함.

<div style="margin: 1rem 0; padding: 0.8rem 1rem; background: var(--vp-c-bg-alt); border-left: 4px solid var(--vp-c-brand); border-radius: 4px; font-size: 0.88rem; line-height: 1.6;">
<strong>객체지향 설계 거버넌스 파이프라인</strong>: <code>SRP 단일 책임 정립</code> ➔ <code>ISP 인터페이스 세분화</code> ➔ <code>DIP 포트 규격화</code> ➔ <code>LSP 다형성 치환 보장</code> ➔ <code>OCP 무중단 확장 달성</code>
</div>

---

## 4. 1교시 10점형 대비 핵심 요약

```text
- S (단일 책임): 한 클래스는 단 하나의 변경 이유(단일 액터)만 가짐
- O (개방-폐쇄): 기능 확장은 열고(Open), 기존 코드 수정은 닫음(Closed)
- L (리스코프 치환): 하위 클래스는 상위 클래스의 계약을 만족하며 완벽히 대체 가능해야 함
- I (인터페이스 분리): 클라이언트 특화형으로 인터페이스를 잘게 분할하여 불필요한 의존 배제
- D (의존관계 역전): 고수준 모듈이 저수준 모듈에 의존하지 않고, 둘 다 추상화에 의존함
```

---

## 5. 기출 분석 및 출제 경향

| 회차 및 교시 | 문제 유형 | 핵심 출제 포인트 |
|---|---|---|
| **제113회 1교시** | 단답형 | 객체지향 5대 설계 원칙(SOLID)의 개념 및 각각의 특징 |
| **제121회 2교시** | 서술형 | 의존관계 역전 원칙(DIP)의 메커니즘과 제어의 역전(IoC), 의존성 주입(DI)과의 관계 |
| **제127회 1교시** | 단답형 | 리스코프 치환 원칙(LSP)의 계약 조건과 위반 시 발생하는 문제점 |
| **제131회 3교시** | 서술형 | 클린 아키텍처 및 헥사고날 아키텍처에서 SOLID 원칙이 구현되는 방식 비교 |

---

## 6. 실전 시험 팁

- **SOLID 5원칙 표 작성 시 스멜(Smell) 병기**: 원칙 명칭과 설명만 쓰지 말고, 위반 시 나타나는 코드 스멜(God Object, if-else 폭증, instanceof 남발 등)을 함께 쓰면 실무 경험을 확실히 어필할 수 있음.
- **DIP 화살표 방향 강조**: 전통적 의존성과 DIP 역전 의존성을 그릴 때 고수준 모듈과 저수준 모듈이 공통 인터페이스를 향해 화살표가 모이는 구조를 정확히 도해할 것.
- **실무 사례 연계**: 결제 게이트웨이(PG사 전환), 데이터베이스 마이그레이션(RDB ➔ NoSQL) 등의 실제 변경 시나리오를 예시로 제시하면 답안의 차별성이 두드러짐.

---

## 7. 연관 토픽 맵

- **선행 토픽**: 객체지향 패러다임(OOP), 디자인 패턴(GoF)
- **유사/비교 토픽**: GRASP 패턴, 코드 리팩토링, 코드 스멜
- **후속/연계 토픽**: IoC/DI, 헥사고날 아키텍처, 클린 아키텍처, 마이크로서비스 아키텍처(MSA)
