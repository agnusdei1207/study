---
title: "디자인 패턴(프록시 패턴)"
author: "Codex"
date: "2026-09-20T23:49:42+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 아키텍처·설계를 거쳐 디자인 패턴(프록시)으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>아키텍처·설계</span>
  <strong>디자인 패턴(프록시 패턴)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **프록시 패턴(Proxy Pattern)**은 실제 객체(RealSubject)에 대한 대리 객체(Proxy)를 두어 객체 접근을 제어하고 부가 기능을 투명하게 제공하는 구조 디자인 패턴
- 메커니즘: 동일 인터페이스(Subject) 구현 → 클라이언트는 대리자 호출 → 프록시가 사전/사후 처리(지연로딩, 접근제어, 캐싱) 후 실제 객체 위임
- 산출/효과: 실제 비즈니스 로직과 부가 관심사 분리(AOP 기반) · 성능 최적화 · OCP/SRP 준수

<div class="itpe-flow-map" role="img" aria-label="프록시 패턴의 호출 중계 구조">
  <div class="itpe-flow-node"><strong>클라이언트(Client)</strong><div class="itpe-step-detail"><span>인터페이스 호출</span></div></div>
  <div class="itpe-flow-arrow">→ request() →</div>
  <div class="itpe-flow-node is-current">
    <strong>프록시(Proxy)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>사전 처리</strong><span>권한 검증 · 지연 생성</span></div>
      <div class="itpe-flow-branch"><strong>위임 호출</strong><span><span class="itpe-keyword"><strong>RealSubject.request()</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>사후 처리</strong><span>로깅 · 트랜잭션 커밋</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 결과 반환 →</div>
  <div class="itpe-flow-node"><strong>실제 객체(RealSubject)</strong><div class="itpe-step-detail"><span>핵심 비즈니스 로직 수행</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Proxy Pattern**: 특정 객체에 대한 접근을 통제하거나 부가 기능을 부여하기 위해 대리 객체를 제공하는 GoF 디자인 패턴
- **Virtual Proxy(가상 프록시)**: 리소스 소모가 큰 객체의 생성을 실제로 필요한 시점까지 지연(Lazy Initialization)시키는 프록시
- **Protection Proxy(보호 프록시)**: 호출자의 권한에 따라 실제 객체의 메서드 접근 권한을 제어하는 프록시
- **Remote Proxy(원격 프록시)**: 서로 다른 주소 공간에 있는 객체를 로컬 객체처럼 다룰 수 있게 해주는 프록시(RPC/RMI 기반)
- **AOP(Aspect Oriented Programming)**: 핵심 비즈니스 로직과 횡단 관심사(보안, 로깅, 트랜잭션)를 프록시 기반으로 분리하는 기법

</details>

## 예상문제

> GoF 디자인 패턴 중 프록시(Proxy) 패턴의 개념 및 구조를 클래스 다이어그램 기반으로 설명하고, 주요 유형 3가지(가상, 보호, 원격)의 특징과 Spring Framework의 AOP 구현에서 프록시 패턴이 활용되는 방안을 제시하시오. (25점)

## Ⅰ. 객체 접근 제어와 관심사 분리의 핵심, 프록시 패턴의 개요

> 프록시 패턴은 실제 객체의 코드를 변경하지 않고도 접근 제어와 부가 기능을 추가하며, 투명성(Transparency) 확보가 성패를 좌우한다.

- 정의: 실제 객체(RealSubject)에 대한 대리 객체(Proxy)를 두어 객체에 대한 직접 접근을 제어하고 부가 기능을 투명하게 제공하는 **구조 디자인 패턴**
- 목적: 무거운 객체의 **지연 로딩(Lazy Loading)**, 보안 접근 제어, 분산 환경 호출 추상화 및 **횡단 관심사(Cross-cutting Concerns)** 분리

## Ⅱ. 프록시 패턴의 구조 및 주요 유형

> 프록시와 실제 객체는 동일한 인터페이스를 구현하므로 클라이언트는 프록시 존재 여부를 인식하지 않고 투명하게 사용한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="프록시 패턴의 인터페이스 기반 구조">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>Subject (인터페이스)</strong></span>
    <div class="itpe-step-detail"><strong>오퍼레이션 규격</strong><span>RealSubject와 Proxy가 공동 구현하여 Client 의존성 격리</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓ 구현(Implements)</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>Proxy (대리 객체)</strong></span>
    <div class="itpe-step-detail"><strong>호출 가로채기</strong><span>RealSubject 참조 보유, 부가기능 수행 후 실제 호출 위임</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓ 위임(Delegation)</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>RealSubject (실제 객체)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 로직</strong><span>실제 핵심 비즈니스 로직을 수행하는 본체 객체</span></div>
  </div>
</div>

| 유형 | 핵심 동작 메커니즘 | 실무 적용 사례 |
|---|---|---|
| **가상 프록시 (Virtual Proxy)** | 대용량 그래픽이나 DB 커넥션을 실제로 사용하는 순간에 생성 | 고화질 이미지 뷰어 썸네일, JPA 지연 로딩 |
| **보호 프록시 (Protection Proxy)** | 클라이언트의 접근 권한을 확인하여 권한 부여 시에만 위임 | 파일/문서 관리 시스템 권한 통제, API 인가 |
| **원격 프록시 (Remote Proxy)** | 네트워크 통신(마샬링/언마샬링)을 숨기고 로컬 객체처럼 인터페이스 제공 | Java RMI, gRPC 스텁(Stub), 분산 RPC |
| **캐싱 프록시 (Caching Proxy)** | 동일한 요청에 대해 연산 결과를 캐싱하여 실제 호출 생략 | 비용이 큰 외부 API 호출 결과 인메모리 캐싱 |

## Ⅲ. 프록시 패턴 vs 유사 패턴 비교

> 구조는 유사하나 도입 의도(Intent)가 명확히 구분되므로 설계 목적에 맞게 선택해야 한다.

| 비교 항목 | 프록시 (Proxy) | 어댑터 (Adapter) | 데코레이터 (Decorator) |
|---|---|---|---|
| **핵심 의도** | 객체에 대한 **접근 제어 및 위임** | 호환되지 않는 **인터페이스 변환** | 객체에 동적으로 **새로운 책임/기능 추가** |
| **인터페이스 변경** | 동일한 인터페이스 유지 | 다른 인터페이스로 변환 | 동일한 인터페이스 유지 또는 확장 |
| **실제 객체 참조** | 프록시가 내부에서 직접 생성/관리 가능 | 클라이언트가 어댑티 객체를 주입 | 클라이언트가 원본 객체를 감싸서 주입 |

## Ⅳ. 프록시 적용 문제점·대응책

> 프록시 패턴은 선언적 트랜잭션과 AOP의 근간이나, 내부 호출 누락과 프록시 제약에 따른 위험을 통제해야 한다.

### Spring AOP 프록시 구현 방식 비교

| 구분 | JDK Dynamic Proxy | CGLIB Proxy |
|---|---|---|
| **기반 메커니즘** | Java 리플렉션, `java.lang.reflect.Proxy` | 바이트코드 조작(ASM), 서브클래싱(Subclassing) |
| **적용 조건** | 타깃 클래스가 **반드시 인터페이스 구현** | 타깃 클래스가 인터페이스 미구현 시에도 가능 |
| **한계점** | 인터페이스가 없는 구체 클래스는 프록시 생성 불가 | 타깃 클래스나 메서드가 `final`인 경우 오버라이딩 불가 |

### 실무 위험 및 거버넌스 대책

| 위험 | 대책 | 효과 |
|---|---|---|
| **Self-Invocation (내부 메서드 호출 시 프록시 우회)** | 자기 호출 메서드를 별도 서비스 컴포넌트로 분리하거나 `AopContext.currentProxy()` 활용 | 트랜잭션 및 보안 AOP 누락 원천 방지 |
| **CGLIB의 final 제약 및 생성자 제약** | `final` 키워드 지양 규칙 및 Objenesis 라이브러리 연계 프록시 생성 | 런타임 프록시 생성 실패 방지 및 호환성 확보 |
| **지연 로딩 시점의 세션 종료 (LazyInitializationException)** | OSIV 패턴 또는 Fetch Join 기반 사전 조회 쿼리 최적화 | N+1 문제 방지 및 지연 로딩 런타임 에러 근절 |

## Ⅴ. 투명한 접근 통제 중심의 결론

> 무분별한 프록시 중첩은 디버깅 난도를 높이고 스택 트레이스를 오염시키므로 명확한 거버넌스가 필요하다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 프록시 패턴의 진정한 가치는 클라이언트와 실제 객체 모두의 코드를 손대지 않고도 새로운 인프라 로직(트랜잭션, 로깅, 캐시, 보안)을 직교(Orthogonal)하게 주입할 수 있다는 개방 폐쇄 원칙(OCP)의 구현에 있음.
- 나라면: 스프링 기반 프로젝트에서 내부 호출(`self-invocation`)로 인한 트랜잭션 누락 문제를 방지하기 위해 정적 분석 규칙(SonarQube)을 수립하고, 구조적으로 서비스 분리를 유도하겠음.

### 실전 답안용 기술사적 제언

- 판정: 횡단 관심사 분리 필요 시 프록시 패턴 기반 AOP 도입 판정
- 대안: JDK Dynamic Proxy 및 CGLIB의 하이브리드 적용 (Spring Boot 2.x+ CGLIB 기본)
- 검증: 내부 호출 트랜잭션 누락 방지 검증 · 지연 로딩 N+1 문제 사전 차단
- 효과: 비즈니스 코드의 순수성 유지 및 횡단 관심사 중앙 통제 달성

<div class="itpe-pipeline is-vertical" role="img" aria-label="프록시 패턴 아키텍처 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>관심사 혼재</strong><span>비즈니스 코드에 트랜잭션·보안·로깅 등 횡단 관심사 침투</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>AOP 내재화</strong><span>프록시 기반 AOP 구축 및 인터페이스 표준화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>누락 검증</strong><span>내부 호출 방지 단위테스트 및 지연로딩 사전 검증</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>단일 책임</strong><span>단일 책임 원칙(SRP) 준수 및 엔터프라이즈 유지보수성 극대화</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **프록시 패턴(Proxy Pattern)**은 실제 객체에 대한 대리 객체를 두어 접근을 제어하고 지연 생성, 권한 검사, 캐싱을 수행하는 구조 패턴
- 목적: 비즈니스 로직과 시스템 인프라 로직(횡단 관심사)을 분리하여 유지보수성 향상

### 2. 구성체계 및 구조

<div class="itpe-pipeline is-vertical" role="img" aria-label="프록시 구조 요약">
  <div class="itpe-pipeline-node"><strong>Subject Interface</strong><div class="itpe-step-detail"><span>공통 오퍼레이션 규격</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Proxy</strong><div class="itpe-step-detail"><span>사전/사후 처리 · 위임 제어</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>RealSubject</strong><div class="itpe-step-detail"><span>핵심 비즈니스 수행</span></div></div>
</div>

### 3. 핵심 통제

- **가상/보호/원격 프록시**: 리소스 지연 로딩, 보안 인가, 분산 통신 추상화
- **Spring AOP**: 동적 프록시(JDK/CGLIB) 기반 트랜잭션 및 보안 인터셉트

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 1교시: GoF 디자인 패턴 중 프록시(Proxy) 패턴
- Erich Gamma et al., Design Patterns: Elements of Reusable Object-Oriented Software (GoF)
- Rod Johnson, Expert One-on-One J2EE Design and Development

## 학습 체크

- [ ] 프록시 패턴의 클래스 다이어그램(Subject, Proxy, RealSubject)을 그릴 수 있는가?
- [ ] 가상 프록시, 보호 프록시, 원격 프록시의 목적과 차이점을 설명할 수 있는가?
- [ ] Spring AOP에서 JDK Dynamic Proxy와 CGLIB Proxy의 동작 차이를 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [소프트웨어 테스트 종류·레벨](./003_sw_test_types_and_levels.md)
- 연관 토픽: [AOP](./074_aop.md), [의존성 주입](./042_dependency_injection.md)
- 다음 토픽: [리팩토링](./006_refactoring.md)
