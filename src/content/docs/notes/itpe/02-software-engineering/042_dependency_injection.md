---
title: "의존성 주입(Dependency Injection)"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 객체지향 설계·결합도 관리 → **의존성 주입(Dependency Injection)**

## 30초 인출

- 본질: 객체가 자신이 사용할 협력 객체(의존성)를 내부에서 직접 생성하지 않고, 외부의 조립자(IoC 컨테이너)로부터 주입받아 객체 간 결합도를 낮추는 객체지향 설계 패턴
- 메커니즘: 추상 인터페이스 정의 → 제어의 역전(IoC) 컨테이너에 빈(Bean) 등록 → 생성자 주입(Constructor Injection)을 통한 의존 객체 전달 및 생명주기(Scope) 관리
- 통찰: 필드 주입 남발 시 순환 참조 탐지가 늦어지고 단위 테스트가 어려워지므로 불변성과 완전성을 보장하는 생성자 주입을 표준으로 채택 필수

<details>
<summary>핵심 용어</summary>

- **DI(Dependency Injection, 의존성 주입)** : 객체의 생성 책임과 사용 책임을 분리하여 외부에서 협력 객체를 동적으로 제공하는 디자인 패턴
- **IoC(Inversion of Control, 제어의 역전)** : 프로그램의 제어 흐름과 객체 생명주기 관리 권한이 애플리케이션 코드에서 프레임워크/컨테이너로 역전되는 원리
- **DIP(Dependency Inversion Principle, 의존역전원칙)** : 고수준 모듈이 저수준 모듈의 구체 클래스에 의존하지 않고 둘 다 추상화(인터페이스)에 의존해야 한다는 SOLID 원칙
- **Composition Root** : 애플리케이션 진입점(Main) 근처에서 전체 객체 의존성 그래프를 조립하고 연결하는 중앙 구성 지점
- **Constructor Injection(생성자 주입)** : 객체 생성 시점에 생성자 파라미터로 필수 의존성을 전달하여 불변 객체 생성을 보장하는 최선의 주입 기법

</details>

---

## 2~4교시 예상문제 (25점)

> 의존성 주입의 개념과 동작 구조를 설명하고, 주입 방식의 선택 및 객체 생명주기 관리 시 고려사항을 제시하시오. (25점, 예상)

---

## 2~4교시 25점 답안

## Ⅰ. 의존성 주입의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 클래스 내부에서 `new` 키워드로 협력 객체를 직접 인스턴스화하지 않고, 외부의 조립자(IoC 컨테이너)가 인터페이스 규격에 맞는 구체 구현체를 생성하여 전달(주입)해 주는 설계 패턴 |
| 목적 | 객체 간의 결합도(Coupling) 완화, 코드 재사용성 증대, 모의 객체(Mock) 주입을 통한 단위 테스트 용이성 극대화 |

## Ⅱ. 의존성 주입의 핵심 특징

| 특징 | 의미 |
|---|---|
| 생성과 사용의 분리 | 비즈니스 로직을 수행하는 객체는 사용에만 집중하고 객체 생성 및 와이어링은 컨테이너에 위임 |
| 인터페이스 기반 의존 | 구체 클래스가 아닌 추상화 인터페이스에 의존함으로써 OCP(개방폐쇄원칙) 및 DIP 달성 |
| 불변성 확보 지원 | 생성자 주입(Constructor Injection)을 통해 `final` 필드로 선언하여 객체 생성 후 상태 변조 방지 |
| 테스트 격리성 향상 | 순수 Java/코틀린 단위 테스트 시 프레임워크 없이도 Mock 객체를 직접 주입하여 고속 테스트 가능 |

## Ⅲ. DI 아키텍처 체계 및 동작 메커니즘

### IoC 컨테이너 기반 의존성 주입 및 객체 조립 구조

```text
┌────────────────────────────────────────────────────────────────────────┐
│               [IoC 컨테이너 / Composition Root (Spring ApplicationContext)]│
│                                                                        │
│   [1. 빈(Bean) 스캔 및 등록]                                          │
│     - OrderServiceImpl 등록                                            │
│     - DatabaseOrderRepository 등록 (OrderRepository 구현체)            │
│         │                                                              │
│         ▼                                                              │
│   [2. 의존 관계 분석 및 인스턴스화]                                    │
│     - OrderRepository 인스턴스 생성                                    │
│         │                                                              │
│         ▼                                                              │
│   [3. 생성자 주입 (Constructor Injection) 실행]                         │
│     - new OrderServiceImpl(orderRepositoryInstance) 호출              │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ 의존성 주입 완료된 완성 객체 제공
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        [클라이언트 비즈니스 계층]                      │
│                                                                        │
│  public class OrderServiceImpl implements OrderService {               │
│      private final OrderRepository orderRepository; // 추상화 인터페이스 │
│                                                                        │
│      // 생성자를 통한 필수 의존성 강제 주입                            │
│      public OrderServiceImpl(OrderRepository orderRepository) {        │
│          this.orderRepository = orderRepository;                      │
│      }                                                                 │
│                                                                        │
│      public void placeOrder() {                                        │
│          orderRepository.save(); // 실제 구현체(RDB/NoSQL)에 위임      │
│      }                                                                 │
│  }                                                                     │
└────────────────────────────────────────────────────────────────────────┘
```

### DI 핵심 구성요소 상세 분석

| 구성요소 | 핵심 역할 및 기능 | 통제 관점 |
|---|---|---|
| **Client (소비자)** | 주입받은 협력자의 인터페이스 메서드를 호출하여 비즈니스 로직 실행 | 내부에서 `new`로 구현체를 생성하지 않도록 아키텍처 규칙 검증 |
| **Service Interface** | 클라이언트와 구현체 사이의 행위 계약(Contract) 제공 | 도메인에 종속적이지 않은 안정된 추상 인터페이스 정의 |
| **Service Implementor** | 인터페이스를 실제 구현한 구체 클래스 (RDB, NoSQL, Mock 등) | 상황에 따라 손쉽게 교체 가능하도록 느슨한 결합 유지 |
| **Injector (컨테이너)** | 객체 생성, 의존성 그래프 탐색, 의존성 주입 및 수명주기(Scope) 총괄 | 순환 의존(Circular Dependency) 탐지 및 조기 차단 |

## Ⅳ. 3대 의존성 주입 방식 비교 및 객체 생명주기

### 주입 방식(생성자 vs 수정자 vs 필드) 비교

| 비교 항목 | 생성자 주입 (Constructor) | 수정자 주입 (Setter) | 필드 주입 (Field) |
|---|---|---|---|
| **주입 시점** | **객체 인스턴스 생성 시점 (최초 1회)** | 객체 생성 완료 후 Setter 호출 시 | 객체 생성 후 리플렉션으로 직접 주입 |
| **불변성 (`final`)** | **보장 가능 (`final` 키워드 사용)** | 불변성 보장 불가 (런타임 변경 위험) | 불변성 보장 불가 |
| **의존성 누락 탐지** | **컴파일 타임 / 기동 시점에 즉시 검출** | 런타임에 NullPointerException 발생 | 런타임에 NullPointerException 발생 |
| **순환 참조 탐지** | **애플리케이션 구동 시점에 예외 발생** | 구동 시점 탐지 불가, 런타임 스택오버플로우 | 구동 시점 탐지 불가, 런타임 스택오버플로우 |
| **테스트 편의성** | **순수 단위 테스트에서 `new`로 Mock 주입** | Setter를 일일이 호출해야 함 | 컨테이너 없이 Mock 주입 불가 (리플렉션 필요) |
| **권장 여부** | **절대적 권장 (Best Practice)** | 선택적/가변적 의존성에만 제한적 권장 | **안티패턴 (사용 지양)** |

### 객체 생명주기(Scope) 관리 정책

| 스코프 유형 | 생명주기 및 인스턴스 공유 범위 | 적합한 사용 대상 |
|---|---|---|
| **Singleton (싱글톤)** | 컨테이너 시작부터 종료까지 단 1개의 인스턴스만 공유 (기본값) | 상태를 가지지 않는 무상태(Stateless) 서비스, 리포지토리 |
| **Prototype (프로토타입)** | 컨테이너에 빈을 요청할 때마다 항상 새로운 인스턴스 생성 및 반환 | 요청마다 독립된 내부 상태를 유지해야 하는 가변 객체 |
| **Request / Session** | 웹 요청(Request)마다 또는 웹 세션(Session) 생명주기와 동기화 | 사용자 로그인 정보, HTTP 트랜잭션별 로깅 컨텍스트 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| A 객체와 B 객체가 서로를 참조하여 발생하는 순환 참조(Circular Dependency)로 애플리케이션 기동 실패 | 단일 책임 원칙(SRP)에 입각하여 공통 관심사를 제3의 C 객체로 분리하는 리팩토링 수행 |
| 생성자 파라미터가 5~7개 이상으로 비대해져 코드 가독성 저하 및 객체 책임 과중 신호 | Facade 서비스로 책임을 위임하거나 파라미터 객체(Parameter Object) 패턴으로 그룹화 |
| 싱글톤 빈 내부에서 프로토타입 빈을 주입받을 경우 프로토타입 빈이 재생성되지 않는 스코프 불일치 | ObjectProvider 또는 javax.inject.Provider를 활용하여 필요한 시점에 지연 획득(DL) |

## Ⅵ. 제언

ArchUnit 기반 아키텍처 린팅을 통한 필드 주입 원천 차단 및 컴파일 타임 DI(Dagger/Koin) 도입 검토

### 정적 분석 기반 DI 클린 아키텍처 검증 파이프라인

```text
[개발자 코드 작성 및 PR 생성]
       ↓
[CI 파이프라인 실행: ArchUnit 정적 검증]
  ├─ 1. @Autowired 필드 주입 사용 금지 규칙 검사 (위반 시 빌드 실패)
  ├─ 2. 생성자 주입 표준 및 Lombok @RequiredArgsConstructor 사용 준수 검사
  ├─ 3. Controller → Service → Repository 단방향 계층 의존 규칙 검사
  └─ 4. 서비스 레이어의 외부 인프라 직접 new 생성 방지 검사
       ↓
[품질 게이트 통과 후 머지 승인]
```

### 의존성 주입 방식 선정 의사결정 체계

```text
의존성 주입 대상 객체 식별
       ↓
[해당 협력 객체가 비즈니스 로직 수행에 필수적인가?]
       ├─ 예 ──→ 생성자 주입(Constructor Injection) 채택 (`final` 필드 강제)
       └─ 아니오 ─→ [런타임 중에 동적으로 의존 대상을 변경해야 하는가?]
                         ├─ 예 ──→ 수정자 주입(Setter Injection) 적용
                         └─ 아니오 ─→ 기본값(Default)을 설정하고 생성자 오버로딩 활용
```

### 선택 근거: 런타임 리플렉션 DI와 컴파일 타임 정적 DI 비교

| 구분 | 런타임 리플렉션 DI (Spring DI) | 제언: 컴파일 타임 DI (Dagger / Koin) |
|---|---|---|
| 의존성 해결 시점 | 애플리케이션 런타임 부팅 시 리플렉션 탐색 | 컴파일 타임에 모든 의존 관계 코드 자동 생성 |
| 기동 성능 | 대규모 애플리케이션의 경우 기동 시간 수십 초 소연 | 리플렉션이 없어 즉시 기동, 서버리스(Lambda) 최적화 |
| 오류 검출 시점 | 런타임 부팅 실패 시점에 발견 | 컴파일 에러로 빌드 시점에 완벽히 의존 누락 검출 |

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 1교시: 스프링 프레임워크의 의존성 주입(DI)
- Martin Fowler, Inversion of Control Containers and the Dependency Injection pattern
- Robert C. Martin, Agile Software Development: Principles, Patterns, and Practices (DIP)
- Craig Walls, Spring in Action (6th Edition)

## 연결 토픽

- 이전 토픽: [요구사항 도출](./041_requirements_elicitation.md)
- 연관 토픽: [객체지향 설계원칙 SOLID](./082_solid.md), [AOP](./074_aop.md), [모듈성](./190_modularity.md)
- 다음 토픽: [정렬 알고리즘](./043_sort_algorithm.md)
