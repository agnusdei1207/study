---
title: "객체지향 설계원칙 SOLID(DIP 포함) (SOLID: Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion; DIP: Dependency Inversion Principle)"
author: "Antigravity"
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

## Ⅰ. SOLID 원칙의 개요

- 개념 : **로버트 C. 마틴** (Uncle Bob)이 정립한 객체지향 소프트웨어 설계의 5대 핵심 원칙으로, 유지보수가 용이하고 유연하며 확장에 열려 있는 객체지향 시스템을 구축하기 위한 아키텍처 설계 가이드라인 (SOLID: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion).
- 배경 및 필요성 : 요구사항 변경에 취약한 소프트웨어의 **4대 악취** (경직성, 취약성, 부동성, 점착성)를 제거하고 지속 가능한 코드베이스를 확립.
- 5대 원칙 구성 : SRP, OCP, LSP, ISP(Interface Segregation Principle), DIP.

## Ⅱ. SOLID 5대 설계 원칙 체계 및 상호 작용

```text
   [ SRP: 단일 책임 원칙 ] ────── 클래스는 단 하나의 변경 이유만을 가져야 함
          │
   [ OCP: 개방-폐쇄 원칙 ] ────── 확장에는 열려 있고(Open), 수정에는 닫혀 있어야(Closed) 함
          │
   [ LSP: 리스코프 치환 원칙 ] ── 하위 타입은 상위 타입을 완벽히 대체 가능해야 함
          │
   [ ISP: 인터페이스 분리 원칙 ] ─ 클라이언트는 자신이 사용하지 않는 메서드에 의존하지 않아야 함
          │
   [ DIP: 의존성 역전 원칙 ] ──── 상위 수준 모듈은 하위 수준 모듈에 의존해서는 안 되며,
                                  둘 다 추상화(인터페이스)에 의존해야 함
```

## Ⅲ. SOLID 5대 원칙 상세 분석 및 위반 해결

| 원칙 | 핵심 개념 | 위반 징후 및 문제점 | 올바른 해결 설계 |
|---|---|---|---|
| **SRP** (Single Responsibility) | 한 클래스는 하나의 책임만 담당 | User 엔티티가 인증, DB(Database) 저장, 이메일 발송까지 모두 처리 | UserService, UserRepository, EmailSender로 책임 분리 |
| **OCP** (Open-Closed) | 기존 코드 수정 없이 새 기능 확장 | 결제 수단 추가 시 기존 결제 메서드 내부에 if-else 추가 | PaymentStrategy 인터페이스 정의 후 구현 클래스 추가 |
| **LSP** (Liskov Substitution) | 부모의 계약(사전/사후조건) 준수 | 정사각형(Square)이 직사각형(Rectangle)을 상속받아 너비/높이 규칙 위배 | 상속 대신 별도 인터페이스 분리 또는 **합성** (Composition) |
| **ISP** (Interface Segregation) | 클라이언트 맞춤형 인터페이스 분리 | 복합기에 프린트만 필요한 클라이언트가 팩스/스캔 메서드까지 구현 강제 | Printable, Scannable, Faxable 인터페이스로 잘게 분리 |
| **DIP** (Dependency Inversion) | 구체 클래스가 아닌 인터페이스에 의존 | OrderService가 new MariaDbRepository() 직접 생성 결합 | OrderService -> <<interface>> Repository <- MariaDbRepo |

## Ⅳ. SOLID 원칙의 주요 한계점 및 해결 방안

- 원칙의 교조적 적용으로 인한 과도한 엔지니어링(Over-Engineering) :
  - 한계점 : 단순한 CRUD(Create, Read, Update, Delete) 시스템이나 변경 가능성이 희박한 도메인에 SOLID를 맹목적으로 적용하여 불필요한 계층과 인터페이스가 양산되고 코드 복잡도 급증.
  - 해결 방안 : YAGNI(You Aren't Gonna Need It) 및 KISS 원칙과의 균형 유지, 핵심 비즈니스 도메인과 변경 빈도가 높은 영역에 한정하여 선별적 적용.
- 레거시 모놀리식 시스템에서의 SOLID 리팩토링 리스크 :
  - 한계점 : 클래스 간 강결합 및 스파게티 코드로 얽힌 대규모 레거시 코드에 DIP나 OCP를 무리하게 적용할 경우 예기치 않은 사이드 이펙트 및 회귀 버그 유발.
  - 해결 방안 : 마이크로 리팩토링 및 스트랭글러 피그(Strangler Fig) 패턴 도입, 높은 단위 테스트 커버리지를 선 확보한 후 점진적 인터페이스 추출 및 의존성 주입 전환.
- 추상화 계층 증가에 따른 런타임 간접 참조 오버헤드 :
  - 한계점 : 빈번한 가상 메서드 테이블(vtable) 탐색 및 객체 인스턴스화로 인해 초저지연(Ultra-Low Latency)을 요구하는 임베디드 및 금융 시스템에서 성능 저하.
  - 해결 방안 : 프로파일링 기반 성능 크리티컬 패스 식별, 컴파일 타임 최적화(인라인화, 템플릿 메타프로그래밍) 및 도메인 모델 내 값 객체(Value Object) 적극 활용.

## Ⅴ. 클린 코드 및 아키텍처 관점의 기술사적 제언

- DIP를 통한 고수준 비즈니스 로직의 인프라 독립성 확보 : 헥사고날 아키텍처의 포트-어댑터 구조를 적용하여 핵심 도메인은 오직 추상화된 포트에만 의존하게 하고, DB나 외부 API(Application Programming Interface) 같은 하위 구현체는 어댑터로 주입받음으로써 기술 스택 변경 시 도메인 무영향 달성.
- 원칙의 교조주의적 적용 경계 : SOLID 원칙을 극단적으로 적용하여 클래스와 인터페이스를 과도하게 잘게 쪼개면 시스템의 파일 수와 간접 참조 계층이 폭증하여 오히려 가독성을 해칠 수 있으므로, 시스템의 변경 빈도와 복잡도에 비례하여 균형 있게 적용하는 아키텍처적 유연성 유지.
