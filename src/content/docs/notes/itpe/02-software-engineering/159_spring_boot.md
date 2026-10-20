---
title: "스프링 부트(Spring Boot)"
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

- 스프링 부트(Spring Boot), 자동 구성(Auto-Configuration), 스타터 의존성(Starter POMs)
- 내장 웹 서버(Embedded Server), 스프링 부트 액추에이터(Actuator), 관측성(Observability), GraalVM 네이티브 이미지

## Ⅰ. 스프링 부트(Spring Boot)의 개요

- 핵심 요약 : 복잡한 설정의 스프링 프레임워크 진입 장벽을 낮추고, 단독 실행 가능한 프로덕션급 애플리케이션의 신속한 개발을 지원하는 경량화 프레임워크.
- 개념 : 스프링 부트(Spring Boot)란 방대한 XML(Extensible Markup Language) 설정과 복잡한 환경 구성이 요구되던 기존 엔터프라이즈 스프링(Spring) 프레임워크의 진입 장벽을 낮추고, 단독 실행 가능한(Stand-alone) 프로덕션급 스프링 애플리케이션을 최소한의 설정(Opinionated Configuration)으로 신속히 개발할 수 있도록 피보탈(현 VMware)에서 개발한 차세대 스프링 프레임워크.
- 배경 및 필요성 : 마이크로서비스 아키텍처(MSA, Microservice Architecture) 확산에 따른 서비스 단위 경량화, 빠른 프로토타이핑 및 배포, 외장 WAS(Web Application Server, WebLogic·Jeus·Tomcat) 설치·배포 복잡도의 제거 필요.
- 주요 목적 : 자동 구성(Auto-Configuration), 스타터 의존성(Starter POMs), 내장 웹 서버(Embedded Tomcat/Jetty)의 3대 핵심 혁신을 통한 개발 생산성·운영 효율 극대화.

## Ⅱ. 스프링 부트의 특징

- 핵심 요약 : 관례 우선 자동 구성과 스타터 의존성, 내장 서버, 내장 관측성 도구로 구성되는 개발·운영 통합 체계.

1. @SpringBootApplication 기반의 관례 우선(Convention over Configuration) 자동 구성.
2. spring-boot-starter-web 등 스타터 의존성(Starter)을 통한 호환 버전 일괄 관리.
3. 내장 톰캣·제티(Jetty) 내장 웹 서버 포함 실행 가능 단일 jar(Executable Jar) 배포.
4. application.yml 단일 프로퍼티 기반의 외부 설정(Externalized Configuration) 통합.
5. 스프링 부트 액추에이터(Actuator)의 상태·메트릭·환경 엔드포인트 기본 제공.
6. 프로덕션급 기본값(Production-Ready Defaults)을 통한 최소 설정 개발 경험.

## Ⅲ. 스프링 부트의 구조 (흐름)

- 핵심 요약 : @SpringBootApplication의 3대 구성 어노테이션과 @Conditional 조건 평가로 이어지는 자동 구성 엔진의 동작 흐름.
- 부팅 시 자동 구성(Auto-Configuration) 메커니즘.

```text
[ @SpringBootApplication ]
   ├─ 1. @SpringBootConfiguration
   ├─ 2. @ComponentScan
   │    (사용자 빈 스캔)
   └─ 3. @EnableAutoConfiguration
         (자동 구성 엔진 구동)
    │ (spring.factories /
    │  AutoConfiguration.imports)
    ▼
[ @Conditional 계열 조건 평가 ]
  - @ConditionalOnClass
  - @ConditionalOnMissingBean
  - @ConditionalOnProperty
    │ (조건 충족 시 기본 빈 등록)
    ▼
[ 내장 톰캣 구동 및
  ApplicationContext 완성 ]
```

- 스타터 의존성(Starters) : spring-boot-starter-web, spring-boot-starter-data-jpa처럼 관련 라이브러리와 호환 버전을 하나의 의존성 패키지로 묶어 버전 충돌(Jar Hell)의 원천 방지.
- 스프링 부트 액추에이터(Actuator) : 애플리케이션의 상태(Health), 메트릭(Metrics), 환경설정(Env), 스레드 덤프를 HTTP(Hypertext Transfer Protocol) 엔드포인트(/actuator/health)로 노출하여 관측성(Observability) 기본 제공.

## Ⅳ. 전통적 Spring MVC와 Spring Boot의 비교

- 핵심 요약 : 외장 WAS 수작업 구성 체계에서 내장 서버·자동 구성·내장 관측성 체계로의 전환.
- 배포 형태의 구조 대조.

```text
[ 전통적 Spring MVC ]
  빌드(war) → 외장 WAS 배포
  (WebLogic / Jeus / Tomcat 별도 설치)

[ Spring Boot ]
  빌드(fat jar) → java -jar 단독 실행
  (내장 톰캣 포함)
```

| 비교 항목 | 전통적 Spring Framework (Spring MVC) | 스프링 부트 (Spring Boot) |
|---|---|---|
| 설정 방식 | 복잡한 XML 설정 또는 다수의 Java Config 명시 | 자동 구성(@EnableAutoConfiguration), 관례 기반 설정 |
| 의존성 관리 | 개별 라이브러리 및 호환 버전의 수작업 pom.xml 기재 | 스타터(Starter) 의존성을 통한 일괄 버전 해결 |
| 배포 형태 | 외장 WAS에 war 파일 패키징 후 빌드·배포 | 내장 톰캣 포함 실행 가능 단일 fat/uber jar 배포 |
| 인프라 관리 | 외장 WAS의 JVM(Java Virtual Machine) 옵션·스레드 풀 수작업 튜닝 | application.yml 단일 프로퍼티 파일로 내장 서버 튜닝 |
| 운영 관측성 | 별도 사외 APM(Application Performance Monitoring) 라이브러리 연동 필요 | 내장 액추에이터를 통한 프로메테우스 메트릭 즉시 노출 |

## Ⅴ. 스프링 부트의 장점과 한계

- 핵심 요약 : 개발 생산성·운영 효율의 장점, 자동 구성 블랙박스화·JVM 기동 비용·공급망 보안 측면의 한계.
- 장점
  1. 최소 설정의 신속한 애플리케이션 개발과 표준화된 프로젝트 구조.
  2. 스타터 의존성을 통한 버전 충돌 제거와 빌드 안정성 확보.
  3. 내장 서버 기반 단독 실행으로 컨테이너·클라우드 배포 용이.
  4. 액추에이터 내장 관측성을 통한 모니터링 도입 비용 절감.
- 한계점 1 : 자동 구성(Auto-Configuration)의 블랙박스화 및 디버깅 난제
  - 한계점 : @EnableAutoConfiguration이 수많은 빈(Bean)을 암묵적으로 등록하므로, 의존성 충돌이나 예기치 않은 빈 오버라이딩 발생 시 원인 추적의 극도로 난해.
  - 해결 방안 : debug=true 설정을 통한 조건부 평가 보고서(ConditionEvaluationReport) 분석, 충돌 발생 시 @SpringBootApplication(exclude=...)로 불필요한 자동 설정의 명시적 차단.
- 한계점 2 : 무거운 JVM(Java Virtual Machine) 런타임의 느린 기동(Cold Start) 및 높은 메모리 점유
  - 한계점 : 서버리스(AWS Lambda) 환경이나 마이크로서비스 컨테이너 환경에서 수 초 이상의 기동 지연과 수백 MB의 메모리 소비 발생.
  - 해결 방안 : Spring Boot 3.x 기반 GraalVM 네이티브 이미지(AOT(Ahead-Of-Time) 컴파일) 빌드 도입, CDS(Class Data Sharing) 및 프로젝트 CRaC(Coordinated Restore at Checkpoint) 적용.
- 한계점 3 : 스타터(Starter) 비대화에 따른 공급망 보안 위험
  - 한계점 : 편의성 중심의 스타터 패키지 사용 시 실제 미사용의 다수 전이 의존성(Transitive Dependencies) 유입으로 취약점 노출 표면 증가.
  - 해결 방안 : Maven/Gradle 의존성 트리 정기 감사(dependency:tree), 취약점 스캐너(Snyk, OWASP Dependency-Check) 연동, 불필요한 의존성의 exclude 선별 제거.

## Ⅵ. 엔터프라이즈 클라우드 환경을 위한 기술사적 제언

- 핵심 요약 : AOT 네이티브 컴파일 기반 기동 최적화와 액추에이터 엔드포인트 보안 통제의 병행.
- AOT·GraalVM 기반 부팅 시간 최적화 : 마이크로서비스의 오토스케일링·서버리스 환경 대응을 위해 Spring AOT(Ahead-Of-Time) 엔진과 GraalVM Native Image를 도입하여 JVM 워밍업 시간을 수초에서 밀리초 단위로 단축하고 메모리 점유 대폭 절감.
- 액추에이터 엔드포인트의 제로 트러스트 보안 통제 : /actuator/env, /actuator/heapdump 등 민감한 서버 내부 정보 노출 침해 사고 예방을 위해 관리자 전용 사설 포트 분리 및 Spring Security 기반 엄격한 인가 정책 강제.

## Ⅶ. 결론

- 핵심 요약 : 스프링 부트는 설정 부담을 제거한 표준 자바 엔터프라이즈 개발·운영 체계.
- 요약 : 자동 구성, 스타터 의존성, 내장 서버의 3대 혁신을 통한 스프링 개발 생산성과 배포 효율의 동시 확보.
- 시사점 : 자동 구성 블랙박스 통제, 네이티브 컴파일 최적화, 의존성 보안 감사의 병행이 엔터프라이즈 적용 성숙도의 선결 조건.
