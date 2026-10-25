---
title: "객체지향 설계원칙 SOLID(DIP 포함) (SOLID: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion; DIP: Dependency Inversion Principle)"
description: "5대 원칙, 의존성 방향 역전, 위반 사례 비교, 교조적 적용·레거시·성능 한계와 방안, 헥사고날 아키텍처 제언"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드

- SRP(Single Responsibility Principle, 단일 책임 원칙), OCP(Open-Closed Principle, 개방-폐쇄 원칙)
- LSP(Liskov Substitution Principle, 리스코프 치환 원칙), ISP(Interface Segregation Principle, 인터페이스 분리 원칙), DIP(Dependency Inversion Principle, 의존성 역전 원칙), 결합도, 응집도, 헥사고날 아키텍처

## Ⅰ. SOLID 원칙의 개요

- 핵심 요약 : 유지보수가 쉽고 확장에 유연한 객체지향 시스템을 위한 다섯 가지 설계 원칙.
- 개념 : 로버트 C. 마틴(Robert C. Martin)이 정립한 객체지향 설계 원칙 다섯 가지를 묶은 **SOLID 원칙** (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)으로, 변경에 유연한 구조를 만드는 설계 가이드라인이다.
- 배경 및 필요성 : 요구사항 변경에 취약한 소프트웨어가 보이는 경직성, 취약성, 부동성, 점착성이라는 설계 악취를 제거해 지속 가능한 코드베이스를 확보할 필요.
- 주요 목적 : 결합도를 낮추고 응집도를 높여 변경이 미치는 영향 범위를 줄이는 것.

## Ⅱ. SOLID의 특징 및 장점

- 핵심 요약 : 책임, 확장성, 치환 계약, 인터페이스 최소화, 추상화 의존의 다섯 원칙이 맞물린 체계.

1. **단일 책임 원칙** (SRP, Single Responsibility Principle) : 클래스는 변경 이유가 하나뿐임 → 변경이 한 곳에 국한되어 영향 범위 축소.
2. **개방-폐쇄 원칙** (OCP, Open-Closed Principle) : 확장에는 열려 있고 수정에는 닫혀 있음 → 신규 기능 추가 시 기존 코드의 회귀 버그 위험 감소.
3. **리스코프 치환 원칙** (LSP, Liskov Substitution Principle) : 하위 타입이 상위 타입의 사전·사후 조건을 지켜 대체 가능함 → 다형성을 안전하게 사용.
4. **인터페이스 분리 원칙** (ISP, Interface Segregation Principle) : 사용하지 않는 메서드에 의존하지 않음 → 불필요한 구현 강제 제거.
5. **의존성 역전 원칙** (DIP, Dependency Inversion Principle) : 상위 모듈과 하위 모듈이 모두 추상화에 의존함 → 구현을 바꿔도 상위 로직이 흔들리지 않음.

## Ⅲ. SOLID의 구조 (흐름)

- 핵심 요약 : 다섯 원칙의 계층 체계와, DIP가 의존성의 방향을 뒤집는 구조.

```text
[ SOLID 5대 설계 원칙 ]
   ↓
[ SRP ] 변경 이유는 하나
[ OCP ] 확장에는 열림, 수정에는 닫힘
[ LSP ] 하위 타입은 상위 타입을 대체 가능
[ ISP ] 쓰지 않는 메서드에 의존하지 않음
[ DIP ] 상위·하위 모듈 모두 추상화에 의존
```

- DIP 적용 전후의 의존성 방향.

```text
[ OrderService (고수준 모듈) ]
   ↓ 의존
[ Repository 인터페이스 ]
   ↑ 구현
  구현체: MariaDb, InMemory
```

## Ⅳ. SOLID 원칙 위반 사례와 올바른 설계의 비교

- 핵심 요약 : 원칙별 위반 징후와 올바른 설계를 대비해 적용 기준을 드러냄.

| 원칙 | 핵심 개념 | 위반 징후 및 문제점 | 올바른 설계 |
| --- | --- | --- | --- |
| SRP (Single Responsibility) | 한 클래스는 하나의 책임만 담당 | User 엔티티가 인증, DB 저장, 이메일 발송을 모두 처리 | UserService, UserRepository, EmailSender로 책임 분리 |
| OCP (Open-Closed) | 기존 코드 수정 없이 새 기능 확장 | 결제 수단 추가 시 기존 결제 메서드에 if-else 추가 | PaymentStrategy 인터페이스를 정의하고 구현 클래스 추가 |
| LSP (Liskov Substitution) | 부모의 계약(사전·사후 조건) 준수 | 정사각형(Square)이 직사각형(Rectangle)을 상속해 너비와 높이 규칙 위배 | 상속 대신 인터페이스 분리 또는 합성(Composition) |
| ISP (Interface Segregation) | 클라이언트 맞춤형 인터페이스 분리 | 프린트만 필요한 클라이언트가 팩스와 스캔 메서드 구현을 강제받음 | Printable, Scannable, Faxable 인터페이스로 분리 |
| DIP (Dependency Inversion) | 구체 클래스가 아닌 인터페이스에 의존 | OrderService가 new MariaDbRepository()로 구체 클래스에 직접 결합 | OrderService → 인터페이스 Repository ← MariaDbRepository |

## Ⅴ. SOLID 원칙의 한계와 방안

- 핵심 요약 : 유연성과 테스트 용이성의 이점, 교조적 적용과 레거시 리스크, 간접 참조 비용의 한계.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 교조적 적용에 따른 과도한 설계 | 단순 CRUD나 변화 가능성이 낮은 영역에 맹목 적용 → 불필요한 계층과 인터페이스 증가 | YAGNI(You Aren't Gonna Need It)와 KISS(Keep It Simple, Stupid) 원칙과의 균형, 변경이 잦은 영역에 선별 적용 | 변경 빈도 대비 추상화 수 |
| 레거시 모놀리식 시스템의 리팩터링 위험 | 강결합된 코드에 DIP나 OCP를 한꺼번에 적용하면 예기치 않은 부작용과 회귀 버그 발생 | 스트랭글러 피그(Strangler Fig) 패턴으로 점진 전환, 단위 테스트 커버리지를 먼저 확보한 뒤 인터페이스 추출 | 회귀 결함 건수 |
| 추상화 계층에 따른 간접 참조 비용 | 가상 호출과 객체 생성이 늘어 초저지연이 필요한 임베디드·금융 시스템의 성능 저하 | 프로파일링으로 성능 임계 경로를 식별하고, 해당 구간만 인라인화나 값 객체 활용 | 임계 경로 지연 시간 |

## Ⅵ. 클린 코드 및 아키텍처 관점의 기술사적 제언

- 핵심 요약 : 헥사고날 구조로 도메인의 인프라 독립성을 확보하고, 원칙 준수를 도구와 리뷰로 공유하는 방향.
- 핵심 비즈니스 로직이 데이터베이스나 외부 API를 직접 알지 않도록 포트와 어댑터로 나누는 **헥사고날 아키텍처** (Hexagonal Architecture)를 기본 구조로 채택하는 것이 좋다. 그러면 저장소나 외부 연동 기술이 바뀌어도 도메인 코드는 영향을 받지 않는다.
- 설계 리뷰에서 원칙 위반을 자동으로 검사하는 정적 분석 도구와 체크리스트를 도입하면, 팀 전체가 같은 기준으로 원칙을 해석하고 적용하게 된다.

## Ⅶ. 결론

- 핵심 요약 : SOLID는 변경에 유연한 객체지향 설계의 최소 원칙이자 아키텍처 품질의 기준선.
- 시사점 : 선별 적용, 레거시의 점진 전환, 성능 임계 경로의 예외 관리가 실무 적용의 성패를 가른다.