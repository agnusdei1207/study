---
title: "스프링 부트(Spring Boot)"
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

## Ⅰ. 스프링 부트(Spring Boot)의 개요

- 개념 : **스프링 부트** (Spring Boot) 란 방대한 XML(Extensible Markup Language) 설정과 복잡한 환경 구성이 요구되던 기존 엔터프라이즈 스프링(Spring) 프레임워크의 진입 장벽을 낮추고, 단독 실행 가능한(Stand-alone) 프로덕션급 스프링 애플리케이션을 최소한의 설정(Opinionated Configuration)으로 신속히 개발할 수 있도록 피보탈(현 VMware)에서 개발한 차세대 스프링 프레임워크.
- 배경 및 필요성 : **마이크로서비스 아키텍처** (MSA, Microservice Architecture) 확산에 따른 서비스 단위 경량화, 빠른 프로토타이핑 및 배포, 외장 WAS(WebLogic, Jeus, Tomcat) 설치 및 배포 복잡도 제거.
- 3대 핵심 혁신 : 자동 구성(Auto-Configuration), 스타터 의존성(Starter POMs), **내장 웹 서버** (Embedded Tomcat/Jetty)

## Ⅱ. 스프링 부트의 핵심 아키텍처 및 자동 구성 메커니즘

```text
   [ @SpringBootApplication ]
               │
   ┌───────────┴─────────────────────────────────────────┐
   │ 1. @SpringBootConfiguration : 스프링 부트 설정 클래스│
   │ 2. @ComponentScan           : 사용자 빈(Bean) 스캔  │
   │ 3. @EnableAutoConfiguration : 자동 구성 엔진 구동   │
   └───────────────────────┬─────────────────────────────┘
                           │ (spring.factories / AutoConfiguration.imports)
                           ▼
   ┌─────────────────────────────────────────────────────┐
   │ [ @Conditional 계열 어노테이션 평가 ]              │
   │  - @ConditionalOnClass (H2, JPA 클래스 존재 시)     │
   │  - @ConditionalOnMissingBean (사용자 정의 빈 부재 시)│
   │  - @ConditionalOnProperty (설정 프로퍼티 활성 시)    │
   └───────────────────────┬─────────────────────────────┘
                           │ (조건 충족 시 기본 빈 자동 등록)
                           ▼
   [ 내장 Tomcat 구동 및 Spring ApplicationContext 완성 ]
```

- **스타터 의존성** (Starters) : `spring-boot-starter-web`, `spring-boot-starter-data-jpa`처럼 관련된 라이브러리와 호환 버전들을 하나의 의존성 패키지로 묶어 버전 충돌(Jar Hell)을 원천 방지.
- **스프링 부트 액추에이터** (Actuator) : 애플리케이션의 상태(Health), 메트릭(Metrics), 환경설정(Env), 스레드 덤프를 HTTP(Hypertext Transfer Protocol) 엔드포인트(`/actuator/health`)로 노출하여 관측성(Observability) 기본 제공.

## Ⅲ. 전통적 Spring MVC와 Spring Boot의 비교

| 비교 항목 | 전통적 Spring Framework (Spring MVC) | 스프링 부트 (Spring Boot) |
|---|---|---|
| 설정 방식 | 복잡한 XML 설정 또는 다수의 Java Config 명시 | 자동 구성(@EnableAutoConfiguration), 관례 기반 설정 |
| 의존성 관리 | 개별 라이브러리 및 호환 버전을 수작업으로 pom.xml 기재 | 스타터(Starter) 의존성을 통한 일괄 버전 의존성 해결 |
| 배포 형태 | 외장 WAS에 war 파일 형태로 패키징하여 빌드 및 배포 | 내장 톰캣이 포함된 실행 가능한 단일 fat/uber jar 배포 |
| 인프라 관리 | 외장 WAS의 JVM(Java Virtual Machine) 옵션, 스레드 풀 수작업 튜닝 | `application.yml` 단일 프로퍼티 파일로 내장 서버 튜닝 |
| 운영 관측성 | 별도의 사외 APM(Application Performance Monitoring) 라이브러리 연동 및 개발 필요 | 내장된 Spring Boot Actuator를 통해 프로메테우스 메트릭 즉시 노출 |

## Ⅳ. 스프링 부트(Spring Boot)의 주요 한계점 및 해결 방안

- **자동 구성** (Auto-Configuration)의 블랙박스화 및 디버깅 난제 :
  - 한계점 : `@EnableAutoConfiguration`이 수많은 빈(Bean)을 암묵적으로 등록하므로, 의존성 충돌이나 예기치 않은 빈 오버라이딩 시 원인 추적 극도로 난해.
  - 해결 방안 : `debug=true` 설정을 통한 조건부 평가 보고서(ConditionEvaluationReport) 분석, 충돌 발생 시 `@SpringBootApplication(exclude=...)`로 불필요한 자동 설정 명시적 차단.
- 무거운 JVM 런타임으로 인한 느린 시작 시간(Cold Start) 및 높은 메모리 점유 :
  - 한계점 : 서버리스(AWS Lambda) 환경이나 마이크로서비스 컨테이너 환경에서 수 초~수십 초의 기동 지연과 기본 수백 MB의 메모리 소비 발생.
  - 해결 방안 : Spring Boot 3.x 기반 **GraalVM 네이티브 이미지** (AOT 컴파일) 빌드 도입, CDS(Class Data Sharing) 및 프로젝트 **CRaC** (Coordinated Restore at Checkpoint) 적용.
- 의존성 관리의 스타터(Starter) 비대화로 인한 공급망 보안 위험 :
  - 한계점 : 편의성을 위한 스타터 패키지 사용 시 실제로 사용하지 않는 수많은 **전이 의존성** (Transitive Dependencies)이 유입되어 취약점 노출 표면 증가.
  - 해결 방안 : Maven/Gradle 의존성 트리 정기 감사(`dependency:tree`), 취약점 스캐너(Snyk, OWASP Dependency-Check) 연동 및 불필요한 의존성 `exclude` 선별 제거.

## Ⅴ. 엔터프라이즈 클라우드 환경을 위한 기술사적 제언

- 컨테이너 가상화 및 **CDS/AOT** 기반 부팅 시간 최적화 : 마이크로서비스의 오토스케일링 및 서버리스 환경에 대응하기 위해, 스프링 부트 3.x의 Spring AOT(Ahead-Of-Time) 엔진과 GraalVM Native Image를 도입하여 JVM 워밍업 시간을 수초에서 수십 밀리초($ms$) 단위로 단축하고 메모리 사용량 $70\%$ 절감.
- 액추에이터 엔드포인트에 대한 제로 트러스트 보안 통제 : `/actuator/env`, `/actuator/heapdump` 등 민감한 서버 내부 정보가 외부에 노출될 경우 심각한 침해 사고가 발생하므로, 관리자 전용 사설 포트로 분리하거나 Spring Security를 통해 엄격한 인가 정책 강제 필수.
