---
title: "스프링 부트(Spring Boot)"
category: "02-software-engineering"
tags:
  - "스프링부트"
  - "SpringBoot"
  - "AutoConfiguration"
  - "Starter"
  - "Actuator"
  - "내장서버"
date: "2026-09-28T18:35:00+09:00"
author: "Antigravity"
sidebar:
  badge:
    text: "기초"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 소프트웨어 개발·운영 → 스프링 부트(Spring Boot)

## 지식 위치

소프트웨어공학 > 애플리케이션 프레임워크 > 스프링 부트(Spring Boot)

## 30초 인출

- 본질: 복잡한 XML 기반 설정과 WAS 배포 절차를 제거하고 단독 실행 가능한 상용화 수준의 스프링 애플리케이션을 신속히 개발할 수 있도록 지원하는 프레임워크
- 메커니즘: Starter 의존성 주입 → `@EnableAutoConfiguration` 및 `@Conditional` 어노테이션 기반 자동 설정 적용 → 내장 서블릿 컨테이너(Tomcat/Undertow) 패키징 및 단일 실행 JAR(Fat JAR) 구동
- 통찰: 블랙박스 자동 설정에 과도하게 의존할 경우 Bean 충돌 및 의도치 않은 메모리 점유가 발생하므로 Actuator 및 Condition Evaluation Report를 활용한 런타임 구성 투명성 확보 필수

<details>
<summary>핵심 용어</summary>

- **Spring Boot** : 스프링 프레임워크를 기반으로 설정의 간소화, 의존성 자동화, 단독 실행(Stand-alone) 환경을 제공하는 프레임워크
- **Starter 의존성 (Spring Boot Starter)** : 특정 도메인/기술(웹, 데이터베이스, 보안 등)에 필요한 라이브러리 및 호환 버전을 하나의 의존성으로 묶어 제공하는 메이븐/그레이들 패키지
- **자동 설정 (Auto-Configuration)** : 클래스패스(Classpath)에 존재하는 라이브러리와 정의된 프로퍼티를 감지하여 스프링 Bean을 조건부 자동 등록하는 메커니즘
- **내장 서블릿 컨테이너 (Embedded Tomcat)** : 외장 WAS(WebLogic, Jeus) 설치 없이 애플리케이션 JAR 내부에 톰캣을 내장하여 `java -jar` 명령으로 즉각 실행 가능한 구조
- **Spring Boot Actuator** : 애플리케이션의 헬스체크(`/health`), 메트릭 수집(`/metrics`), 환경설정 조회(`/env`) 등 상용 운영 관측 기능을 제공하는 모듈
</details>

---

## 2~4교시 예상문제 (25점)

> 엔터프라이즈 자바 개발에서 Spring Boot의 등장 배경과 핵심 3대 기술(Starter, Auto-Configuration, Embedded Server)의 동작 원리를 설명하고, 클라우드 네이티브 MSA 환경에서의 Actuator 보안 및 운영 최적화 방안을 제시하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 복잡하고 방대한 엔터프라이즈 스프링 애플리케이션의 초기 설정과 보일러플레이트 코드를 최소화하고, 독립 실행 가능한 프로덕션급 서비스를 신속히 구축하도록 돕는 프레임워크 |
| 목적 | "설정보다 관례(Convention over Configuration)" 철학 구현, 신속한 프로토타이핑 및 마이크로서비스 아키텍처(MSA) 배포 단위 경량화 달성 |

## Ⅱ. 핵심 특징

| 특징 | 세부 내용 |
|---|---|
| 의존성 관리 단순화 (Starter) | `spring-boot-starter-web` 등 사전 검증된 버전 호환 라이브러리 번들을 제공하여 의존성 충돌 해소 |
| 조건부 자동 구성 (Auto-Config) | `@ConditionalOnClass`, `@ConditionalOnMissingBean` 등을 통해 개발자가 재정의하지 않은 빈을 지능형 자동 등록 |
| 독립 단일 파일 배포 (Fat JAR) | 서블릿 컨테이너(Tomcat, Jetty)를 내장하여 외부 WAS 배포 과정 없이 컨테이너 이미지 경량화 가능 |
| 운영 관측성 내장 (Actuator) | 쿠버네티스 프로브(Liveness/Readiness) 및 프로메테우스 메트릭 수집 엔드포인트를 표준 규격으로 제공 |

개발자는 비즈니스 로직 작성에만 집중할 수 있도록 인프라성 설정을 자동화한 엔터프라이즈 자바 표준.

## Ⅲ. 체계·프로세스

```text
[1. 프로젝트 의존성 로드]
  pom.xml / build.gradle: spring-boot-starter-web 선언
       │
       ▼ (Starter BOM 기반 라이브러리 및 전이 의존성 버전 자동 결정)
[2. 스프링 부트 애플리케이션 기동]
  @SpringBootApplication (@Configuration + @EnableAutoConfiguration + @ComponentScan)
       │
       ▼
[3. Auto-Configuration 자동 설정 평가]
  META-INF/spring/...AutoConfiguration.imports 스캔
  ┌────────────────────────────────────────────────────────┐
  │ 조건부 어노테이션 검사:                                │
  │ - @ConditionalOnClass (예: Servlet.class, Tomcat.class) │
  │ - @ConditionalOnMissingBean (개발자가 직접 등록했는가?) │
  │   ├─ [미등록] ──► 프레임워크 기본 Bean 자동 등록        │
  │   └─ [직접등록] ─► 사용자 정의 Bean 우선 채택 (재정의)  │
  └────────────────────────────────────────────────────────┘
       │
       ▼
[4. 내장 톰캣 서버 부트스트래핑 및 실행]
  Embedded Tomcat 생성 → DispatcherServlet 등록 → 포트(8080) 리스닝 시작
```

의존성 선언부터 조건부 어노테이션 평가, 우선순위 Bean 등록, 내장 컨테이너 초기화로 이어지는 부트스트래핑 프로세스.

## Ⅳ. 종류·비교

| 비교 항목 | 전통적 Spring Framework (Spring MVC) | Spring Boot 프레임워크 |
|---|---|---|
| **설정 방식** | web.xml, root-context.xml 등 방대한 XML/자바 설정 | 자동 설정(Auto-Configuration) 및 `application.yml` 단일화 |
| **배포 패키징** | WAR 파일 빌드 후 외장 WAS(Tomcat/WebLogic)에 수동 배포 | 단일 실행 가능 Fat JAR (`java -jar`) 내장 톰캣 구동 |
| **의존성 관리** | 각 서드파티 라이브러리 버전 간의 호환성을 수동 검증 | Starter POM을 통해 사전 검증된 버전 셋 자동 주입 |
| **운영 모니터링** | JMX 수동 설정 또는 별도 모니터링 에이전트 개발 필요 | Spring Boot Actuator 기본 내장으로 즉각적 REST API 관측 |
| **클라우드 적합성** | 무거운 WAS 구조로 컨테이너 기동 지연 및 확장성 제한 | 경량 프로세스로 도커 컨테이너화 및 빠른 오토스케일링에 최적 |

### 핵심 어노테이션 구성 비교

| 어노테이션 | 역할 및 의미 |
|---|---|
| **@SpringBootApplication** | `@Configuration`, `@EnableAutoConfiguration`, `@ComponentScan`을 포괄하는 부트 진입점 |
| **@ConditionalOnClass** | 클래스패스 상에 특정 클래스가 존재할 때만 설정을 활성화 |
| **@ConditionalOnMissingBean** | 사용자가 동일한 타입의 Bean을 명시적으로 등록하지 않았을 때만 기본 Bean을 주입 |
| **@ConfigurationProperties** | `application.yml`의 계층형 프로퍼티 값을 자바 객체(POJO)에 타입 세이프(Type-Safe)하게 바인딩 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 내부 자동 구성의 복잡한 조건문으로 인해 원치 않는 Bean이 등록되거나 덮어쓰여지는 블랙박스 문제 | 기동 시 `--debug` 옵션을 활성화하여 Condition Evaluation Report를 검토하고 필요 시 `@SpringBootApplication(exclude=...)` 명시 |
| Actuator 엔드포인트(`/actuator/env`, `/heapdump`)의 외부 노출로 인한 DB 패스워드 및 민감 데이터 유출 위험 | Spring Security를 연동하여 Actuator 전용 포트 분리 및 RBAC 인가 통제, 노출 항목(`management.endpoints.web.exposure.include`) 최소화 |
| JVM 런타임의 높은 메모리 사용량과 느린 콜드 스타트(Cold Start)로 서버리스(Serverless) 환경 적용 한계 | Spring Boot 3+의 GraalVM Native Image 컴파일(AOT)을 적용하여 기동 속도 밀리초 단위 단축 및 메모리 절감 |

## Ⅵ. 제언

클라우드 네이티브 MSA 전환 시 12-Factor 원칙에 따라 설정을 환경변수로 분리하고, GraalVM 네이티브 빌드와 쿠버네티스 프로브를 결합한 탄력적 컨테이너 수명주기 거버넌스 확립 필요.

```text
[Spring Boot 클라우드 네이티브 배포 아키텍처]
  소스 코드 → GraalVM Native Image 빌드 → 경량 OCI 이미지 생성 → Kubernetes Pod 배포 (Actuator Probe 연동)
```

| 검증 단계 | 개발/빌드 단계 | 배포/운영 단계 |
|---|---|---|
| 핵심 통제 | 자동 구성 리포트 검토 및 AOT 정적 분석 | Actuator 엔드포인트 보안 인증 및 메트릭 수집 |
| 운영 목표 | 불필요한 스타터 제거 및 Fat JAR 용량 최적화 | Liveness/Readiness 기반 무중단 롤링 업데이트 |

---

## 출제 이력과 검증 출처

- 정보관리기술사 127회 2교시: 마이크로서비스 환경에서 Spring Boot 기반 애플리케이션 구축 및 운영 관측성(Actuator) 확보 방안

## 연결 토픽

- [서비스 지향 아키텍처(SOA)](./187_soa.md)
- [CI/CD 지속적 통합 및 배포](./095_ci_cd.md)
- [마이크로서비스 아키텍처(MSA)](./035_msa.md)
- [API 게이트웨이(API Gateway)](./075_api_gateway.md)
