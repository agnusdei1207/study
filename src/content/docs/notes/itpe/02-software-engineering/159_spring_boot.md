---
title: "스프링 부트(Spring Boot)"
category: "02-software-engineering"
tags:
  - "스프링부트"
  - "SpringBoot"
  - "자동설정"
  - "AutoConfiguration"
  - "Starter"
  - "Actuator"
  - "내장WAS"
  - "마이크로서비스"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 애플리케이션 아키텍처와 백엔드 프레임워크를 거쳐 스프링 부트로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>애플리케이션 아키텍처·백엔드 프레임워크</span>
  <strong>스프링 부트(Spring Boot)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 수백 줄의 복잡한 XML 환경설정과 외부 웹 애플리케이션 서버(WAS) 배포의 번거로움을 해결하기 위해, '관례 우선 설정(Convention over Configuration)'과 내장 서블릿 컨테이너를 기반으로 즉시 실행 가능한(Standalone) 단일 JAR 애플리케이션을 신속하게 빌드·구동하는 클라우드 네이티브 자바 프레임워크
- 메커니즘: `@SpringBootApplication` 메인 메서드 실행 $\rightarrow$ Starter 의존성 분석 $\rightarrow$ `@EnableAutoConfiguration` 조건부 빈 자동 등록 $\rightarrow$ 내장 톰캣(Tomcat) 컨테이너 기동 및 포트 바인딩 $\rightarrow$ 런타임 상태 진단 및 서비스 개시
- 산출물: 실행 가능한 단일 Fat JAR(`app.jar`) · 의존성 명세서(`build.gradle`/`pom.xml`) · 구성 프로파일(`application.yml`)

<div class="itpe-flow-map" role="img" aria-label="스프링 부트 기동 및 자동 구성 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 프로젝트 부트스트랩 및 Starter 주입</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>해결</strong><span>`spring-boot-starter-web` 등 사전 검증된 호환 라이브러리 세트 자동 주입</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 클래스패스 스캔 및 조건부 자동 구성</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>등록</strong><span>`@ConditionalOnClass` 기반으로 DB 드라이버 유무를 감지하여 DataSource 자동 생성</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 내장 웹 서버(Embedded WAS) 기동</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>바인딩</strong><span>별도 WAS 설치 없이 내장 톰캣(Tomcat)을 띄우고 서블릿 디스패처 등록</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 애플리케이션 헬스 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>모든 필수 스프링 빈이 충돌 없이 등록되고 Actuator 헬스체크가 UP 상태인가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (기동 완료)</strong>
      <span>HTTP 포트 활성화 $\rightarrow$ 쿠버네티스 Readiness 프로브 통과 및 트래픽 유입 허용</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (빈 순환참조 / 포트 충돌)</strong>
      <span>구동 중단 $\rightarrow$ `debug=true` 모드로 자동 설정 조건 분석 및 의존성 exclude 수정</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Auto-Configuration(자동 설정)**: 개발자가 일일이 빈(Bean)을 설정하지 않아도, 클래스패스에 존재하는 라이브러리와 프로퍼티 설정을 바탕으로 최선의 기본 구성을 자동 등록하는 기능
- **Starter POM**: 특정 목적(예: 웹, JPA, 보안)에 필요한 여러 라이브러리와 권장 버전을 하나의 의존성으로 묶어 버전 충돌을 방지하는 메이븐/그레이들 패키지
- **Embedded WAS(내장 서블릿 컨테이너)**: 애플리케이션 내부에 톰캣(Tomcat), 제티(Jetty), 언더토(Undertow)를 내장하여 `java -jar` 명령어로 단독 구동할 수 있도록 지원하는 구조
- **Spring Boot Actuator**: 프로덕션 운영 환경에서 애플리케이션의 가용성, CPU/메모리 메트릭, 스레드 상태, 환경변수 등을 REST 엔드포인트로 노출하는 관측성(Observability) 모듈
</details>

## 1. 개요 및 필요성

### 레거시 스프링의 "설정 지옥"과 마이크로서비스 전환 장벽

전통적인 스프링 프레임워크(Spring Framework)는 유연한 엔터프라이즈 환경을 제공했으나, 프로젝트 초기 구축 시 수백 줄에 달하는 XML 설정 파일 작성과 복잡한 라이브러리 버전 간 의존성 충돌 문제(Dependency Hell)로 개발 생산성을 심각하게 저하시켰다. 또한 운영 환경마다 별도의 톰캣이나 제우스(JEUS) 등 외장 WAS를 설치하고 WAR 파일을 배포해야 해 클라우드 컨테이너화에 큰 장애가 되었다.

스프링 부트는 **관례 우선 설정(CoC, Convention over Configuration)**과 **내장 WAS**를 통해 이러한 보일러플레이트 설정을 제거하고, 개발자가 순수 비즈니스 로직 구현에만 집중할 수 있는 표준 클라우드 네이티브 런타임을 제공한다.

### 전통적 Spring Framework vs Spring Boot 비교

| 구분 | 전통적 스프링 (Spring Framework) | 스프링 부트 (Spring Boot) |
|---|---|---|
| **설정 방식** | 복잡한 XML 또는 `@Configuration` 자바 코드 수작업 설정 | **`@EnableAutoConfiguration` 기반 관례적 자동 설정** |
| **의존성 관리** | 각 서드파티 라이브러리 버전을 일일이 지정 및 호환성 검증 | **Starter 의존성을 통한 검증된 버전 세트 자동 관리** |
| **배포 패키징** | WAR(Web Application Archive) 패키징 | **내장 WAS가 포함된 단일 실행 Fat JAR** |
| **실행 환경** | 외장 WAS(WebLogic, JEUS, Tomcat) 사전 설치 및 구성 필수 | **JRE만 있으면 `java -jar app.jar`로 단독 실행 가능** |
| **운영 모니터링** | 서드파티 APM 도구 수동 연동 필요 | **Spring Boot Actuator를 통한 표준 운영 엔드포인트 기본 내장** |

## 2. 아키텍처 및 핵심 메커니즘

### 스프링 부트 3대 핵심 아키텍처

```text
+-------------------------------------------------------------------------+
|                  스프링 부트(Spring Boot) 핵심 구성 구조                |
+-------------------------------------------------------------------------+
|                                                                         |
|                       [ Spring Boot Application ]                       |
|                                    │                                    |
|          ┌─────────────────────────┼─────────────────────────┐          |
|          v                         v                         v          |
|  [ 1. Starters ]         [ 2. Auto-Config ]        [ 3. Actuator ]      |
|  - starter-web           - @ConditionalOnClass     - /actuator/health   |
|  - starter-data-jpa      - @ConditionalOnMissing   - /actuator/metrics  |
|  - 의존성 버전 자동 조정 - 클래스패스 스캔 빈 등록 - 운영 관측성 및 프로브 |
|                                    │                                    |
|                                    v                                    |
|                   [ 내장 서블릿 컨테이너 (Embedded WAS) ]               |
|                   - 내장 Tomcat / Jetty / Undertow                      |
|                   - 단일 Fat JAR 패키징 및 컨테이너 배포 최적화         |
+-------------------------------------------------------------------------+
```

### 스프링 부트 3대 핵심 기둥

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① Starter 의존성</strong></span>
      <span class="itpe-badge">호환성 보장</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>복잡한 서드파티 라이브러리 간 버전 충돌을 완벽히 해결</li>
        <li>`spring-boot-starter-web` 하나로 Spring MVC, Jackson, Tomcat 일괄 주입</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 자동 설정 (Auto-Configuration)</strong></span>
      <span class="itpe-badge">설정 제로화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>`@ConditionalOnClass` 등 조건부 어노테이션으로 라이브러리 자동 감지</li>
        <li>개발자가 커스텀 빈을 정의하면 기본 자동 구성을 자동으로 양보</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 액추에이터 (Actuator)</strong></span>
      <span class="itpe-badge">프로덕션 관측성</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>애플리케이션의 런타임 메트릭, 스레드 덤프, 환경 변수 자동 노출</li>
        <li>쿠버네티스 Liveness/Readiness 헬스체크와 완벽한 규격 연계</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| JVM 런타임의 리플렉션 빈 주입 및 클래스 로딩으로 컨테이너 기동 시간(Cold Start)이 15초 이상 지연 | Spring Boot 3.x 기반 GraalVM Native Image 사전 컴파일(AOT) 빌드 파이프라인 도입 | 기동 시간 0.1초 단축 및 컨테이너 메모리 70% 절감 |
| 자동 구성(Auto-Configuration)이 내부적으로 의도치 않은 빈을 중복 생성하여 충돌 및 메모리 낭비 | `application.yml`에 `debug: true`를 활성화하여 조건 평가 리포트를 확인하고 `exclude` 옵션 적용 | 빈 주입 투명성 확보 및 기동 안정성 보장 |
| 개발 편의를 위해 Actuator 전체 엔드포인트를 노출했다가 환경변수(DB 패스워드 등) 및 힙 덤프 유출 | 운영 환경에서 민감 엔드포인트를 비활성화하고 관리용 내부 포트(`management.server.port`) 분리 강제 | 기밀 정보 외부 노출 100% 원천 차단 |

## 4. 기술사 답안 차별화 포인트

### GraalVM 기반의 네이티브 이미지(AOT) 전환과 서버리스 생태계 확장

스프링 프레임워크의 고질적 한계는 동적 리플렉션과 CGLIB 프록시 기반의 느린 구동 시간(Cold Start)이었다. 최신 **Spring Boot 3.x**는 GraalVM AOT(Ahead-Of-Time) 컴파일을 공식 지원하여 빌드 시점에 모든 빈 의존성을 정적으로 확정하고 네이티브 기계어로 직접 컴파일한다. 이를 통해 JVM 없이 단 0.1초 만에 기동되는 초경량 컨테이너를 생성함으로써, **AWS Lambda 등 서버리스(Serverless) FaaS 환경과 쿠버네티스 오토스케일링(HPA)**에 즉각 반응할 수 있는 차세대 클라우드 네이티브 아키텍처 역량을 피력한다.

### 쿠버네티스 네이티브 프로브(Probe) 연동 체계

스프링 부트 Actuator의 `/actuator/health`는 단순한 성공/실패 응답을 넘어 **Liveness(생존 여부)와 Readiness(트래픽 수신 준비 여부)**를 분리 관리한다. DB 연결 실패 시 Readiness만 비활성화하여 트래픽 유입만 차단하고 인스턴스 불필요 재시작을 방지하는 지능적 복원력(Resilience) 설계 패턴을 실무적 강점으로 서술한다.

## 5. 참고 및 연계 학습

- [메시지 큐(Message Queue)](./140_message_queue.md)
- [성능 요구사항(Performance Requirement)](./149_performance_requirement.md)
- [서비스 워커(Service Worker)](./147_service_worker.md)
- [CBD(Component Based Development)](./128_cbd.md)
