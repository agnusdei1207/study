---
title: "디자인 패턴(프록시 패턴)"
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

- 디자인 패턴, GoF(Gang of Four), 프록시 패턴(Proxy Pattern), 구조 패턴(Structural Pattern)
- 대리 객체(Proxy), 지연 로딩(Lazy Loading), 원격/가상/보호/스마트 프록시, AOP(Aspect-Oriented Programming)

## Ⅰ. 디자인 패턴과 프록시 패턴의 개요

- 핵심 요약 : 반복적 설계 문제의 모범 사례인 디자인 패턴 중, 대리 객체를 통한 접근 제어와 기능 위임을 수행하는 프록시 패턴.
- 개념 : 소프트웨어 설계 과정에서 반복적으로 발생하는 구조적 문제에 대해 재사용 가능한 객체 간 관계와 설계를 정형화한 모범 사례(Best Practice)이자, 그중 실제 객체에 대한 대리 객체(Proxy)를 두어 접근을 제어하고 부가 기능을 위임하는 구조 패턴.
- 배경 및 필요성 : 원본 객체 코드 수정 없이 접근 제어, 지연 로딩(Lazy Loading), 보안 검증, 로깅, 트랜잭션 등 공통 관심사의 투명한 분리 필요.
- 주요 목적 : 단일 책임 원칙(SRP, Single Responsibility Principle)과 개방-폐쇄 원칙(OCP, Open-Closed Principle)의 충족 및 공통 관심사 모듈화.
- GoF(Gang of Four) 3대 분류 : 생성(Creational) 5종, 구조(Structural) 7종(프록시 포함), 행위(Behavioral) 11종.

## Ⅱ. 프록시 패턴의 특징

- 핵심 요약 : 공통 인터페이스 기반 투명성과 접근 제어, 무수정 확장이 결합된 구조 패턴.
- GoF 디자인 패턴 3대 분류 구조.

```text
[ GoF(Gang of Four) 디자인 패턴 3대 분류 ]
 생성(Creational) 5종  ── 객체 생성 방식의 정형화
 구조(Structural) 7종  ── 객체 결합 구조, 프록시 패턴 포함
 행위(Behavioral) 11종 ── 객체 간 상호작용·책임 분배
```

1. 클라이언트가 프록시와 실제 객체를 동일하게 다루는 공통 Subject 인터페이스 구현.
2. 원본 객체 코드 수정 없이 부가 기능 추가 가능한 개방-폐쇄 원칙(OCP) 준수.
3. 접근 제어, 캐싱, 지연 로딩 등 사전/사후 처리의 가로채기(Interception) 수행.
4. GoF(Gang of Four) 구조(Structural) 패턴 7종 중 하나로 분류.
5. 런타임 동적 프록시(Dynamic Proxy) 생성 기반의 AOP(Aspect-Oriented Programming) 구현 근간.

## Ⅲ. 프록시 패턴의 구조 (흐름)

- 핵심 요약 : 클라이언트 요청을 프록시가 가로채 사전/사후 처리 후 실제 객체로 위임하는 간접 참조 구조.
- 프록시 패턴 클래스 협력 구조.

```text
[Client]
   │ 1. Subject 인터페이스로 요청
   ▼
[Proxy] (대리 객체)
   │ 2. 사전/사후 처리 후 호출 위임
   ▼
[RealSubject] (원본 객체)

* Proxy와 RealSubject는 공통 인터페이스
  <<interface>> Subject를 구현
```

- Subject 인터페이스 : 클라이언트가 프록시와 실제 객체를 동일한 방식으로 다루도록 하는 공통 추상 메서드 정의.
- RealSubject : 실제 비즈니스 로직을 수행하는 핵심 원본 객체.
- Proxy : RealSubject에 대한 참조의 내부 보유, 클라이언트 요청의 가로채기 및 사전/사후 처리(인증, 캐싱, 지연 로딩) 후 호출 위임.

## Ⅳ. 프록시 패턴 유형별 비교

- 핵심 요약 : 원격·가상·보호·스마트 프록시가 역할과 적용 사례에서 구분되는 유형 체계.

| 유형 | 핵심 역할 | 적용 사례 |
|---|---|---|
| 원격 프록시(Remote Proxy) | 서로 다른 주소 공간의 객체에 대한 로컬 대리인 역할 | gRPC 스텁, Java RMI(Remote Method Invocation), 분산 RPC(Remote Procedure Call) 클라이언트 |
| 가상 프록시(Virtual Proxy) | 생성 비용이 큰 고용량 객체의 생성을 실제 사용 시점까지 지연 | 고해상도 그래픽 이미지 로딩, 대용량 문서 프리뷰 |
| 보호 프록시(Protection Proxy) | 클라이언트 권한에 따른 실제 객체 메서드 접근 제어 | 관리자 권한 인가, 엔터프라이즈 리소스 접근 통제 |
| 스마트 프록시(Smart Proxy) | 객체 접근 시 부가적인 로깅, 참조 카운팅, 락킹 자동 수행 | Spring AOP 트랜잭션 프록시, C++ 스마트 포인터 |

## Ⅴ. 프록시 패턴의 장점과 한계

- 핵심 요약 : 공통 관심사 분리·무수정 확장의 장점, 런타임 오버헤드·Self-Invocation·디버깅 저하의 한계.
- 장점
  1. 원본 객체 수정 없이 접근 제어·부가 기능 추가.
  2. 공통 관심사의 프록시 집중을 통한 단일 책임 원칙(SRP) 충족.
  3. 지연 로딩 및 캐싱을 통한 자원 사용 효율화.
- 한계점 1 : 간접 호출 계층 추가에 따른 런타임 성능 오버헤드
  - 한계점 : 프록시 개입에 따른 메서드 호출 스택 심화, 동적 프록시(Dynamic Proxy) 사용 시 리플렉션(Reflection) 비용 기반 응답 지연 발생.
  - 해결 방안 : 바이트코드 조작(CGLIB, ByteBuddy, ASM) 기반 사전 컴파일·클래스 생성 기법 적용, 불필요한 프록시 중첩(Chaining) 지양 및 핫패스(Hot Path) 캐싱 적용.
- 한계점 2 : 프록시 내부 호출(Self-Invocation) 시 부가 기능 누락
  - 한계점 : 객체 내부의 자기 메서드 직접 호출(this.method()) 시 프록시 계층 미경유로 트랜잭션(@Transactional), 보안, 캐싱 등 AOP 부가 기능 미동작 결함 발생.
  - 해결 방안 : 의존성 자기 주입(Self-Injection) 기반 프록시 재경유 리팩토링, 호출 메서드의 별도 서비스 빈(Bean) 분리, 필요 시 AspectJ 컴파일/로드타임 위빙(CTW/LTW, Compile-Time Weaving/Load-Time Weaving) 적용.
- 한계점 3 : 스택 트레이스 비대화 및 디버깅 가시성 저하
  - 한계점 : 동적 생성 프록시 인스턴스로 인한 예외 스택 트레이스 비대화, 비즈니스 로직 결함 원인 지점 추적 및 디버깅 난이도 증가.
  - 해결 방안 : 인터페이스 분리 원칙(ISP, Interface Segregation Principle) 준수, 상관 ID(Correlation ID) 기반 통합 로깅 및 프록시 실행 전후 메트릭 모니터링 표준화.

## Ⅵ. 프록시 패턴 적용 시 기술사적 제언

- 핵심 요약 : 성능 크리티컬 경로의 위빙 기법 선택과 Self-Invocation 방지 설계의 병행.
- 성능 오버헤드와 디버깅 복잡도 완화 : 프록시 계층의 스택 깊이 증가 및 리플렉션 비용 감안, 성능 크리티컬 모듈에 대한 AspectJ 컴파일 타임 위빙 또는 바이트코드 조작(CGLIB) 선택 적용.
- 순환 참조 및 프록시 우회(Self-Invocation) 주의 : 동일 클래스 내부 직접 호출 시 트랜잭션·보안 애노테이션 누락 방지를 위한 구조적 분리 설계 필수 준수.

## Ⅶ. 결론

- 핵심 요약 : 프록시 패턴은 투명한 간접 계층으로 공통 관심사를 분리하는 구조 패턴.
- 요약 : 공통 인터페이스 기반 대리 객체를 통해 접근 제어·지연 로딩·부가 기능을 원본 객체 무수정으로 확장하는 패턴.
- 시사점 : 런타임 오버헤드, Self-Invocation, 디버깅 가시성 이슈의 사전 설계 대응이 안정적 적용의 전제 조건.
