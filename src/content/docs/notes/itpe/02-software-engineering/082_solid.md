---
title: "객체지향 설계원칙 SOLID(DIP 포함) (SOLID: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion; DIP: Dependency Inversion Principle)"
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

- SRP(Single Responsibility Principle, 단일 책임 원칙), OCP(Open-Closed Principle, 개방-폐쇄 원칙)
- LSP(Liskov Substitution Principle, 리스코프 치환 원칙), ISP(Interface Segregation Principle, 인터페이스 분리 원칙), DIP(Dependency Inversion Principle, 의존성 역전 원칙), 결합도, 응집도, 헥사고날 아키텍처

## Ⅰ. SOLID 원칙의 개요

- 핵심 요약 : 유지보수 용이하고 확장에 유연한 객체지향 시스템 구축을 위한 5대 설계 원칙.
- 개념 : 로버트 C. 마틴(Uncle Bob)이 정립한 객체지향 소프트웨어 설계의 5대 핵심 원칙으로, 유지보수가 용이하고 유연하며 확장에 열려 있는 객체지향 시스템 구축을 위한 아키텍처 설계 가이드라인(SOLID: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion).
- 배경 및 필요성 : 요구사항 변경에 취약한 소프트웨어의 4대 악취(경직성, 취약성, 부동성, 점착성) 제거 및 지속 가능한 코드베이스 확립.
- 5대 원칙 구성 : SRP(Single Responsibility Principle), OCP(Open-Closed Principle), LSP(Liskov Substitution Principle), ISP(Interface Segregation Principle), DIP(Dependency Inversion Principle).

## Ⅱ. SOLID의 특징

- 핵심 요약 : 책임, 확장성, 치환 계약, 인터페이스 최소화, 추상화 의존의 5원칙 체계.

1. SRP(Single Responsibility Principle, 단일 책임 원칙) : 한 클래스에는 단 하나의 변경 이유만 존재.
2. OCP(Open-Closed Principle, 개방-폐쇄 원칙) : 기존 코드 수정 없는 확장을 지향하는 구조(확장에는 개방, 수정에는 폐쇄).
3. LSP(Liskov Substitution Principle, 리스코프 치환 원칙) : 하위 타입의 상위 타입 완전 대체 가능성(사전/사후조건 계약 준수).
4. ISP(Interface Segregation Principle, 인터페이스 분리 원칙) : 사용하지 않는 메서드에 대한 의존 제거.
5. DIP(Dependency Inversion Principle, 의존성 역전 원칙) : 상위/하위 모듈 모두의 추상화 의존.

## Ⅲ. SOLID의 구조 (흐름)

- 핵심 요약 : 5원칙의 계층 체계와 DIP 기반 의존성 방향 역전 구조.
- SOLID 5대 설계 원칙 체계.

```text
[ SOLID 5대 설계 원칙 ]
 ├─ [ SRP ] 단일 책임 원칙
 │    - 클래스는 단 하나의 변경 이유만 가짐
 ├─ [ OCP ] 개방-폐쇄 원칙
 │    - 확장에는 열려(Open), 수정에는 닫혀(Closed)
 ├─ [ LSP ] 리스코프 치환 원칙
 │    - 하위 타입은 상위 타입을 완벽히 대체 가능
 ├─ [ ISP ] 인터페이스 분리 원칙
 │    - 사용하지 않는 메서드에 의존하지 않음
 └─ [ DIP ] 의존성 역전 원칙
      - 상위/하위 모듈 모두 추상화에 의존
```

- DIP 적용 의존성 방향.

```text
[ OrderService (고수준 모듈) ]
        │ 의존
        ▼
<<interface>> [ Repository (추상화) ]
        ▲                  ▲
        │ 구현             │ 구현
[MariaDbRepository]  [InMemoryRepository]
(구체 클래스가 아닌 추상화에 의존 = DIP)
```

## Ⅳ. SOLID 5대 원칙 위반 사례와 올바른 설계의 비교

- 핵심 요약 : 원칙별 위반 징후와 올바른 해결 설계의 대비를 통한 적용 기준.

| 원칙 | 핵심 개념 | 위반 징후 및 문제점 | 올바른 해결 설계 |
|---|---|---|---|
| SRP (Single Responsibility) | 한 클래스는 하나의 책임만 담당 | User 엔티티가 인증, DB(Database) 저장, 이메일 발송까지 모두 처리 | UserService, UserRepository, EmailSender로 책임 분리 |
| OCP (Open-Closed) | 기존 코드 수정 없이 새 기능 확장 | 결제 수단 추가 시 기존 결제 메서드 내부 if-else 추가 | PaymentStrategy 인터페이스 정의 후 구현 클래스 추가 |
| LSP (Liskov Substitution) | 부모의 계약(사전/사후조건) 준수 | 정사각형(Square)이 직사각형(Rectangle)을 상속하여 너비/높이 규칙 위배 | 상속 대신 별도 인터페이스 분리 또는 합성(Composition) |
| ISP (Interface Segregation) | 클라이언트 맞춤형 인터페이스 분리 | 복합기에서 프린트만 필요한 클라이언트의 팩스/스캔 메서드까지 구현 강제 | Printable, Scannable, Faxable 인터페이스로 분리 |
| DIP (Dependency Inversion) | 구체 클래스가 아닌 인터페이스에 의존 | OrderService의 new MariaDbRepository() 직접 생성 결합 | OrderService -> <<interface>> Repository <- MariaDbRepo |

## Ⅴ. SOLID 원칙의 장점과 한계

- 핵심 요약 : 유연성·테스트 용이성 이점, 교조적 적용과 레거시 리스크·성능 오버헤드의 한계.
- 장점

  1. 낮은 결합도와 높은 응집도에 기반한 변경 영향 최소화.
  2. 인터페이스 중심 설계를 통한 단위 테스트 및 모킹(Mocking) 용이성.
  3. 확장 지향 구조를 통한 신규 기능 추가 비용의 안정화.
- 한계점 1 : 원칙의 교조적 적용으로 인한 과도한 엔지니어링(Over-Engineering)
  - 한계점 : 단순한 CRUD(Create, Read, Update, Delete) 시스템이나 변경 가능성 희박 도메인에 대한 맹목적 적용 시 불필요한 계층·인터페이스 양산 및 코드 복잡도 급증.
  - 해결 방안 : YAGNI(You Aren't Gonna Need It) 및 KISS 원칙과의 균형 유지, 핵심 비즈니스 도메인과 변경 빈도 높은 영역으로의 선별적 적용.
- 한계점 2 : 레거시 모놀리식 시스템에서의 SOLID 리팩토링 리스크
  - 한계점 : 강결합·스파게티 코드로 얽힌 대규모 레거시에 대한 DIP·OCP 무리한 적용 시 예기치 않은 사이드 이펙트 및 회귀 버그 유발.
  - 해결 방안 : 마이크로 리팩토링 및 스트랭글러 피그(Strangler Fig) 패턴 도입, 높은 단위 테스트 커버리지 선확보 후 점진적 인터페이스 추출 및 의존성 주입 전환.
- 한계점 3 : 추상화 계층 증가에 따른 런타임 간접 참조 오버헤드
  - 한계점 : 빈번한 가상 메서드 테이블(vtable) 탐색 및 객체 인스턴스화로 인한 초저지연(Ultra-Low Latency) 요구 임베디드·금융 시스템의 성능 저하.
  - 해결 방안 : 프로파일링 기반 성능 크리티컬 패스 식별, 컴파일 타임 최적화(인라인화, 템플릿 메타프로그래밍) 및 도메인 모델 내 값 객체(Value Object) 활용.

## Ⅵ. 클린 코드 및 아키텍처 관점의 기술사적 제언

- 핵심 요약 : DIP 기반 인프라 독립성 확보와 원칙 적용 강도의 균형 관리.
- DIP를 통한 고수준 비즈니스 로직의 인프라 독립성 확보 : 헥사고날 아키텍처의 포트-어댑터 구조 적용을 통한 핵심 도메인의 추상화된 포트 전용 의존, DB나 외부 API(Application Programming Interface) 등 하위 구현체의 어댑터 주입 방식으로 기술 스택 변경 시 도메인 무영향 달성.
- 원칙의 교조주의적 적용 경계 관리 : SOLID 원칙의 극단적 적용에 따른 클래스·인터페이스 과다 분할 시 파일 수와 간접 참조 계층 폭증으로 가독성 저하 가능, 시스템 변경 빈도와 복잡도에 비례한 균형적 적용 유지.

## Ⅶ. 결론

- 핵심 요약 : SOLID는 변경에 유연한 객체지향 설계의 최소 원칙이자 아키텍처 품질의 기준선.
- 요약 : 책임 분리, 확장 지향, 계약 준수, 인터페이스 최소화, 추상화 의존의 5원칙 통합 체계.
- 시사점 : 선별적 적용, 레거시 점진 전환, 성능 크리티컬 경로 예외 관리가 실무 적용 성패의 분기점.
