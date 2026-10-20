---
title: "의존성 주입(Dependency Injection)"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- 의존성 주입(DI, Dependency Injection), 제어의 역전(IoC, Inversion of Control), DI 컨테이너
- SOLID, DIP(Dependency Inversion Principle), 생성자 주입(Constructor Injection), 순환 참조(Circular Dependency), Mock 테스트

## Ⅰ. 의존성 주입(DI)의 개요

- 핵심 요약 : 의존 객체를 외부 컨테이너로부터 주입받아 결합도를 낮추는 객체지향 설계 패턴.
- 개념 : 객체가 자신이 사용할 의존 객체(Dependency)를 내부에서 직접 생성(new)하지 않고, 외부의 조립기(컨테이너)로부터 주입(Injection)받도록 하여 객체 간의 결합도를 낮추는 객체지향 설계 패턴이자 제어의 역전(IoC, Inversion of Control)의 대표적 구현체(DI, Dependency Injection).
- 배경 및 필요성 : 클래스 내부에서 구현체를 직접 생성하면 구현 클래스에 강하게 결합되어 모듈의 교체·확장·단위 테스트(Mocking)가 불가능해지는 문제 해결 필요.
- 설계 원칙 연계 : 객체지향 5대 원칙(SOLID(Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)) 중 의존성 역전 원칙(DIP, Dependency Inversion Principle)의 실천적 기법.

## Ⅱ. 의존성 주입의 특징

- 핵심 요약 : IoC 구현, 결합도 최소화, 3가지 주입 방식을 갖는 설계 기법.

1. 제어의 역전(IoC, Inversion of Control)의 대표적 구현체.
2. 외부 컨테이너로부터의 의존 객체 주입으로 결합도 최소화.
3. SOLID 중 의존성 역전 원칙(DIP, Dependency Inversion Principle)의 실천 기법.
4. 인터페이스 기반 주입으로 단위 테스트(Mocking) 용이.
5. 3가지 주입 방식(생성자, 수정자, 필드) 지원.
6. DI 컨테이너의 빈(Bean) 생명주기 관리.

## Ⅲ. 의존성 주입의 구조 (흐름)

- 핵심 요약 : DI 컨테이너가 인터페이스 타입의 구현체를 생성하여 클라이언트에 주입하는 구조.
- DI 컨테이너와 클라이언트의 관계.

```text
[ DI 컨테이너 (Spring IoC/Guice) ]
 - 빈(Bean) 생명주기 관리
 - MariaDbRepository 생성 후 주입
   │ (인터페이스를 통한 주입)
   ▼
[ 클라이언트 클래스 ]
   │ (의존)
   ▼
<<interface>> Repository
   ▲ (구현)
   │
[ MariaDbRepository ]
```

- DI 적용 전후의 결합 구조 비교.

```text
[ DI 적용 전후 구조 비교 ]
(적용 전 - 강한 결합)
클라이언트 클래스 ── new 직접 생성 ──> MariaDbRepository

(적용 후 - 느슨한 결합)
DI 컨테이너 ── 인터페이스 타입 주입 ──> 클라이언트 클래스
                                            ▲
                                   <<interface>> Repository
                                            ▲ 구현
                                   MariaDbRepository
```

- 생성자 주입(Constructor Injection) : 필수적인 의존성을 생성자의 매개변수로 전달받는 방식. 불변성(Immutable) 확보, 누락 시 컴파일 에러 발생, 순환 참조 감지 가능 (가장 권장).
- 수정자 주입(Setter Injection) : 선택적인 의존성을 변경할 수 있도록 Setter 메서드를 제공하는 방식. 런타임에 의존성 교체가 가능하나 객체 상태가 불완전해질 위험 존재.
- 필드 주입(Field Injection) : @Autowired 어노테이션으로 필드에 직접 주입. 코드가 간결하나 순수 자바 단위 테스트 작성이 어렵고 DI 프레임워크에 강하게 결합되는 안티패턴.

## Ⅳ. 3가지 주입 방식의 비교

- 핵심 요약 : 불변성·테스트 용이성·순환 참조 감지 관점에서 생성자 주입의 우위.

| 주입 방식 | 불변성 (Immutability) | 테스트 용이성 | 순환 참조 감지 | 권장 여부 |
|---|---|---|---|---|
| 생성자 주입 | 완벽 보장 (final 필드 선언 가능) | 프레임워크 없이 순수 POJO(Plain Old Java Object) Mock 주입 가능 | 애플리케이션 구동 시점에 즉시 예외 발생 | 최우선 권장 (Best Practice) |
| 수정자 주입 | 보장 불가 (이후 재설정 가능) | Mock 주입 가능하나 메서드 호출 필요 | 런타임 호출 시점까지 지연될 수 있음 | 선택적 의존성에 한해 사용 |
| 필드 주입 | 보장 불가 (리플렉션 의존) | DI 프레임워크 없이는 Mock 주입 불가 | 구동 시점 감지 어려움 | 사용 지양 (Anti-pattern) |

## Ⅴ. 의존성 주입(DI)의 장점과 한계

- 핵심 요약 : 테스트 용이성과 유연한 교체의 장점, 기동 지연·순환 참조·추적 난이도의 한계.
- 장점
  1. 인터페이스 기반 주입으로 구현체의 유연한 교체·확장.
  2. 생성자 주입의 불변성(Immutability) 확보 및 컴파일 타임 검증.
  3. 프레임워크 비의존 순수 POJO Mock 기반 단위 테스트 가능.
- 한계점 1 : 런타임 리플렉션 및 컨테이너 기동 지연(Cold Start)
  - 한계점 : 대규모 엔터프라이즈 애플리케이션에서 수천 개의 빈(Bean)을 런타임에 동적으로 스캔하고 리플렉션을 통해 주입할 경우 서버 기동 시간과 메모리 사용량이 급증하여 서버리스 환경에 치명적.
  - 해결 방안 : 컴파일 타임 의존성 주입 도구(Dagger 2, Micronaut, Quarkus)를 채택하거나, Spring Boot 3+의 AOT(Ahead-of-Time) 컴파일 및 GraalVM 네이티브 이미지 빌드를 적용하여 기동 지연 해소.
- 한계점 2 : 순환 의존성(Circular Dependency) 발생 및 아키텍처 오염
  - 한계점 : 클래스 A가 B를 참조하고 B가 다시 A를 참조하는 순환 참조 구조가 형성되면 컨테이너 초기화 실패(`BeanCurrentlyInCreationException`)를 유발하고 강한 결합도 초래.
  - 해결 방안 : 필드 주입을 금지하고 생성자 주입(Constructor Injection)을 강제하여 애플리케이션 구동 시점에 순환 참조를 즉각 탐지하며, 도메인 이벤트(ApplicationEventPublisher) 기반 발행/구독 모델로 의존성 단절 리팩토링.
- 한계점 3 : DI 컨테이너 추상화 뒤에 은닉된 객체 생명주기 추적 난이도
  - 한계점 : 객체의 생성과 소멸이 컨테이너에 의해 자동으로 제어되므로, 소스코드만 보고 실제 런타임에 어떤 구현체가 주입되는지 직관적 추적이 어렵고 디버깅 복잡도 상승.
  - 해결 방안 : 프로파일(@Profile)과 조건부 설정(@Conditional)의 무분별한 남용을 제한하고, 정적 아키텍처 분석 도구(ArchUnit)를 CI(Continuous Integration)에 연동하여 계층 간 의존성 규칙을 자동 검증.

## Ⅵ. 대규모 애플리케이션 아키텍처에서의 기술사적 제언

- 핵심 요약 : 생성자 주입 표준화와 도메인 계층의 프레임워크 독립성 유지의 2대 제언.
- 생성자 주입과 Lombok @RequiredArgsConstructor 표준화 : final 필드 선언과 롬복을 결합하여 보일러플레이트 코드를 제거하면서도 객체의 불변성을 확립하고, NullPointerException을 원천 차단하는 코딩 표준 수립.
- 도메인 계층의 프레임워크 독립성 유지 : 클린 아키텍처나 헥사고날 아키텍처 관점에서, 핵심 도메인 엔티티와 유스케이스는 특정 DI 컨테이너(Spring 등)의 어노테이션에 오염되지 않도록 순수 Java/코틀린 표준으로 유지하는 아키텍처 경계 통제 필요.

## Ⅶ. 결론

- 핵심 요약 : DI는 결합도 최소화와 테스트 용이성을 실현하는 IoC의 핵심 실천 기법.
- 요약 : 인터페이스 기반 주입과 컨테이너 관리로 유연하고 테스트 가능한 객체지향 설계를 실현하는 기법.
- 시사점 : 생성자 주입 표준화와 도메인 계층 프레임워크 독립성 유지로 지속 가능한 아키텍처 경계 확보 필요.
