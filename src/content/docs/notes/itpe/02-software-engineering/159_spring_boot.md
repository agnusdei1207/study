---
title: "스프링 부트(Spring Boot)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T10:17:00+09:00"
tags:
  - "notes-software-engineering"
extra:
  model: "Gemini 3.8 Flash"

---

## 답안 골격
```text
[스프링 부트(Spring Boot)] ◀━━ 머리: Ⅶ 내 의견 (관례 우선 설정과 임베디드 WAS 기반 마이크로서비스 표준 런타임 확립)
 ┃
 ┣━ Ⅰ 개요 ───── 레거시 스프링의 복잡한 XML 설정 및 WAS 배포 지연 한계 → 즉시 실행 가능한 단독(Standalone) 엔터프라이즈 프레임워크
 ┣━ Ⅱ 특징 ───── 관례 우선(CoC, Convention over Configuration) · 내장 웹 서버(Tomcat) · 스타터(Starter) 의존성 관리 · 자동 설정
 ┣━ Ⅲ 구조 ───── 3대 핵심 기능: Auto-Configuration(`@EnableAutoConfiguration`) / Starter POM / Actuator(운영 관측성)
 ┣━ Ⅳ 흐름 ───── `main()` 실행 → `SpringApplication.run()` → 클래스패스 라이브러리 감지 → 내장 톰캣 구동 및 빈(Bean) 등록 → 서블릿 서비스 개시
 ┣━ Ⅴ 비교 ───── 전통적 Spring Framework (WAR, 외부 톰캣, XML 설정) vs Spring Boot (JAR, 내장 톰캣, 자동 설정)
 ┗━ Ⅵ 실무 ───── 자동 설정의 블랙박스 디버깅 난항 / 기동 시간(Cold Start) 지연 / GraalVM Native Image 활용
```
- 필수 키워드: 스프링 부트 · 자동 설정(Auto-Configuration) · 스타터(Starter) · 내장 WAS · Actuator · `@SpringBootApplication` · GraalVM
- 기출: 127회 1교시 `스프링 부트(Spring Boot)의 개념 및 주요 특징` → Ⅰ~Ⅵ

## 한 줄 본질
- 수백 줄의 복잡한 XML 설정 파일과 외부 톰캣 WAS 설치 때문에 개발 시작조차 어려웠던 초기 스프링의 설정 지옥 병목 → 의존성 라이브러리를 클래스패스에서 자동 감지하여 관례에 따라 빈을 자동 주입하고 독립 실행형(JAR)으로 구동시키는 클라우드 네이티브 프레임워크 / 내부 동작의 블랙박스화

## 핵심 그림
```text
+-------------------------------------------------------------------------+
|                  스프링 부트(Spring Boot) 3대 핵심 아키텍처             |
+-------------------------------------------------------------------------+
|                                                                         |
|                          [ Spring Boot Application ]                    |
|                                       │                                 |
|          ┌────────────────────────────┼────────────────────────────┐    |
|          v                            v                            v    |
|  [ 1. Starter 의존성 ]       [ 2. Auto-Configuration ]     [ 3. Actuator ]|
|  - pom.xml / build.gradle    - @EnableAutoConfiguration    - 운영 환경 모니터링|
|  - 복잡한 버전 충돌 해결      - @ConditionalOnClass         - /actuator/health|
|  - spring-boot-starter-web   - 클래스패스 자동 스캔        - /actuator/metrics|
|                                       │                                 |
|                                       v                                 |
|                    [ 내장 서블릿 컨테이너 (Embedded WAS) ]               |
|                    - 내장 Tomcat / Jetty / Undertow                     |
|                    - java -jar app.jar 단독 실행 파일 패키징            |
|                                                                         |
+-------------------------------------------------------------------------+
```

## 핵심 용어
- `@ConditionalOnClass`: 특정 라이브러리(예: `Tomcat.class`, `DataSource.class`)가 클래스패스에 존재할 때만 관련 스프링 빈 설정을 자동으로 등록하는 조건부 애너테이션
- Spring Boot Actuator: 애플리케이션의 헬스체크(`/health`), 메트릭 수집(`/metrics`), 스레드 덤프, 환경 변수 조회를 REST 엔드포인트로 노출하는 프로덕션 운영 관측성 모듈

## 핵심 통찰
- 스프링 부트는 스프링 프레임워크와 대립되는 새로운 프레임워크가 아니라, 기존 스프링의 번거로운 보일러플레이트 설정을 관례(Convention) 기반으로 완전히 자동화해 준 "스프링의 래퍼(Wrapper) 도구"임
- 내장 WAS(Embedded Tomcat)를 내장하여 "단일 실행 가능한 Fat JAR"로 패키징할 수 있게 됨으로써, 과거 WAS 설치와 WAR 배포로 이어지던 무거운 절차가 사라지고 Docker 컨테이너 이미지 경량화의 일등공신이 됨
- 부트의 마법 같은 자동 설정(`spring.factories`)이 때로는 원하지 않는 빈을 중복 생성하거나 충돌을 일으키므로, `@SpringBootApplication(exclude = ...)` 또는 `debug=true` 옵션으로 자동 구성 조건을 투명하게 추적할 수 있어야 함

## 이웃 토픽과 구분
- 전통적 스프링(Spring MVC) vs 스프링 부트(Spring Boot): 전통 스프링 = 외부 WAS 설치 필수, WAR 배포, XML/JavaConfig 수작업 설정 / 스프링 부트 = 내장 WAS 탑재, 단독 실행 JAR, 자동 빈 주입

## 문제·원인·대책
- 적용 상황: 수십 개 마이크로서비스로 구성된 클라우드 쿠버네티스 백엔드
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 배포 파이프라인에서 컨테이너 기동 시 스프링 부트 구동 시간(Cold Start)이 15초 소요 | JVM 런타임의 클래스 로딩, 컴포넌트 스캔, 리플렉션 빈 주입 오버헤드 | Spring Boot 3.x 기반 GraalVM Native Image AOT(사전 컴파일) 빌드 적용 | 기동 시간 15초에서 0.1초로 단축 및 메모리 70% 절감 |
| 쿠버네티스 파드(Pod)가 내부 DB 연결 장애로 멈췄는데도 트래픽이 계속 유입되어 500 에러 | 파드의 Liveness/Readiness 프로브가 애플리케이션의 실제 의존성 상태를 모름 | Spring Boot Actuator의 헬스 프로브 그룹(`/actuator/health/readiness`) 쿠버네티스 연동 | 장애 인스턴스 자동 격리 및 트래픽 유입 차단 |

## 이렇게 출제된다
- 제127회 1교시: "스프링 부트(Spring Boot)의 개념 및 주요 특징(Starter, Auto-Configuration, Actuator)을 설명하시오." → 요구 포인트: 스프링 부트 등장 배경 + 3대 핵심 기술 요소 + 전통 스프링 대비 장단점

## 내 의견
- [Actuator 엔드포인트 보안 노출 위험 방어] 개발 편의를 위해 Actuator 전체 설정을 열어두었다가(`/actuator/*`) 외부에 환경 변수(DB 패스워드, API 키)와 힙 덤프가 유출되는 심각한 보안 취약점 발생 → 나라면: 운영 환경에서는 `/health`와 `/info`만 선별적으로 공개하고, 민감 엔드포인트는 내부 관리자 서브넷에서만 접근하도록 Spring Security 및 포트 분리(`management.server.port`)를 강제화
