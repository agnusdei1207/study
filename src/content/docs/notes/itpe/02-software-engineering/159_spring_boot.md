---
title: "스프링 부트(Spring Boot)"
description: "자동 구성·스타터·내장 서버·액추에이터, 전통적 Spring 비교, 블랙박스·기동 지연·공급망 위험 한계와 방안"
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

- 스프링 부트(Spring Boot), 자동 구성(Auto-Configuration), 스타터 의존성(Starter POMs)
- 내장 웹 서버(Embedded Server), 스프링 부트 액추에이터(Actuator), 관측성(Observability), GraalVM 네이티브 이미지

## Ⅰ. 스프링 부트의 개요

- 핵심 요약 : 복잡한 설정의 스프링 프레임워크 진입 장벽을 낮추고, 단독 실행 가능한 애플리케이션을 빠르게 만드는 경량화 프레임워크.
- 개념 : **스프링 부트** (Spring Boot)란 XML(Extensible Markup Language) 설정 중심이던 기존 스프링(Spring) 프레임워크의 진입 장벽을 낮추고, 단독 실행 가능한 프로덕션급 애플리케이션을 최소 설정으로 개발하도록 돕는 프레임워크.
- 배경 및 필요성 : 마이크로서비스 아키텍처(MSA, Microservice Architecture)의 확산으로 서비스 단위의 빠른 빌드와 배포가 요구되었고, 외장 WAS(Web Application Server) 설치와 배포 절차의 복잡도를 줄일 필요가 생김.
- 주요 목적 : **자동 구성** (Auto-Configuration), **스타터 의존성** (Starter POMs), **내장 웹 서버** (Embedded Server)의 세 가지 장치로 개발 생산성과 운영 효율을 높임.

## Ⅱ. 스프링 부트의 특징

- 핵심 요약 : 관례 우선의 자동 구성과 스타터 의존성, 내장 서버, 내장 관측성이 하나의 개발·운영 체계로 묶인 구조.

1. 관례 우선 구성 : `@SpringBootApplication` 한 번의 선언으로 기본 구성을 적용 → 반복 설정 코드 제거.
2. 스타터 의존성 : 관련 라이브러리와 호환 버전을 묶어 제공 → 버전 충돌 감소와 빌드 안정성 확보.
3. 내장 서버 : 톰캣(Tomcat) 등을 포함한 실행 가능 단일 jar 배포 → 외장 WAS 설치 없이 컨테이너 배포 용이.
4. 외부 설정 통합 : `application.yml` 한 파일로 설정을 관리 → 환경별 설정 분리가 쉬움.
5. 액추에이터 : 상태, 메트릭, 환경 정보를 HTTP 엔드포인트로 기본 노출 → 모니터링 도입 비용 절감.

## Ⅲ. 스프링 부트의 구조 (흐름)

- 핵심 요약 : 어노테이션 세 가지가 자동 구성 엔진을 구동하고, 조건 평가를 거쳐 기본 빈이 등록되는 흐름.
- 부팅 시 자동 구성 메커니즘의 흐름.

```text
[ @SpringBootApplication ]
  - @SpringBootConfiguration
  - @ComponentScan (사용자 빈 스캔)
  - @EnableAutoConfiguration
      ↓
[ 자동 구성 후보 목록 로드 ]
  - AutoConfiguration.imports
      ↓
[ @Conditional 계열 조건 평가 ]
  - @ConditionalOnClass
  - @ConditionalOnMissingBean
  - @ConditionalOnProperty
      ↓
[ 조건 충족 시 기본 빈 등록 ]
```

- 스타터 의존성(Starter) : spring-boot-starter-web, spring-boot-starter-data-jpa처럼 기능 단위로 라이브러리를 묶어 의존성 충돌을 줄임.
- 액추에이터(Actuator) : `/actuator/health`처럼 상태와 메트릭을 HTTP 엔드포인트로 노출해 관측성(Observability)을 기본 제공.

## Ⅳ. 전통적 Spring Framework와 Spring Boot의 비교

- 핵심 요약 : 외장 WAS 중심의 수작업 구성에서 내장 서버와 자동 구성 중심의 배포 체계로 전환.

```text
[ 전통 Spring MVC ]
  war 빌드 → 외장 WAS 배포
  (Tomcat 등 별도 설치·튜닝)

[ Spring Boot ]
  jar 빌드 → java -jar 단독 실행
  (내장 Tomcat 포함)
```

| 비교 항목 | 전통적 Spring Framework (Spring MVC) | Spring Boot |
| --- | --- | --- |
| 설정 방식 | XML 또는 다수의 Java 설정을 직접 작성 | 자동 구성과 관례 기반 기본값 |
| 의존성 관리 | 라이브러리별 호환 버전을 직접 기재 | 스타터 의존성으로 일괄 해결 |
| 배포 형태 | 외장 WAS에 war 파일 배포 | 내장 서버를 포함한 단일 jar 실행 |
| 서버 튜닝 | 외장 WAS의 JVM과 스레드 풀 수작업 조정 | 설정 파일에서 내장 서버 값 지정 |
| 운영 관측성 | 별도 APM(Application Performance Monitoring) 연동 필요 | 액추에이터로 메트릭 기본 노출 |

## Ⅴ. 스프링 부트의 한계와 방안

- 핵심 요약 : 개발 생산성과 배포 효율이라는 장점, 자동 구성의 블랙박스화와 JVM 기동 비용, 의존성 보안이라는 한계.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 자동 구성의 블랙박스화 | 암묵적으로 등록된 빈이 많아 충돌과 오버라이딩의 원인 추적이 어려움 | 조건 평가 보고서 확인, `exclude`로 불필요한 자동 구성 명시적 차단 | 빈 충돌 건수 |
| JVM 기동 지연과 메모리 점유 | 서버리스나 소규모 컨테이너에서 기동이 느리고 메모리를 많이 씀 | GraalVM 네이티브 이미지(AOT, Ahead-Of-Time 컴파일) 검토, 클래스 데이터 공유 적용 | 기동 시간, 메모리 사용량 |
| 스타터 비대화에 따른 공급망 위험 | 미사용 전이 의존성이 유입되어 취약점 노출 면이 넓어짐 | 의존성 트리 정기 감사, 취약점 점검 도구 연동, 불필요한 의존성 제외 | 취약 의존성 수 |

## Ⅵ. 엔터프라이즈 클라우드 환경을 위한 기술사적 제언

- 핵심 요약 : AOT 네이티브 컴파일 기반 기동 최적화와 액추에이터 엔드포인트 보안 통제의 병행.
- 오토스케일링과 서버리스 환경을 운영하는 플랫폼 팀은 Spring AOT 엔진과 GraalVM 네이티브 이미지 빌드를 선택 적용해 JVM 워밍업 시간을 줄이는 방향을 검토해야 한다. 기동 특성이 중요한 서비스부터 적용하는 것이 현실적이다.
- 보안 담당 조직은 액추에이터 엔드포인트에서 환경 변수나 힙 덤프처럼 민감한 정보가 노출되지 않도록 관리 전용 포트를 분리하고, 스프링 시큐리티(Spring Security) 기반 인가 정책을 강제해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 스프링 부트는 설정 부담을 줄인 자바 엔터프라이즈 개발과 운영의 표준 체계.
- 시사점 : 자동 구성의 가시화, 네이티브 컴파일 검토, 의존성 보안 감사를 병행해야 엔터프라이즈 적용 성숙도가 확보.