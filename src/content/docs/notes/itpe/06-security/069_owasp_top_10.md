---
title: "OWASP Top 10 (OWASP: Open Worldwide Application Security Project)"
author: "agnusdei1207"
date: "2026-10-24T23:01:31+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "069"
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- OWASP Top 10, 시큐어 코딩, S-SDLC, 위협 모델링, 공급망 실패, Injection
- SAST, DAST, SCA, SBOM, SLSA, 중앙 인가(PDP, PEP)
- Fail-Secure, RASP, Policy-as-Code

## Ⅰ. OWASP Top 10의 개요

- 핵심 요약 : 웹 애플리케이션에서 가장 빈발하고 피해가 큰 보안 위험 열 가지를 정리한 공통 기준.
- 개념 : 웹 애플리케이션과 API에서 빈발하고 피해가 큰 보안 위험 열 가지를 집계한 **OWASP Top 10** (Open Worldwide Application Security Project가 발간하는 상위 10대 위험 목록).
- 배경 및 필요성 : 취약점 사례를 통계로 집계해, 개발자와 보안 관리자가 위험의 우선순위를 같은 기준으로 논의할 필요가 생김. 이에 따라 **시큐어 코딩** (Secure Coding)과 소프트웨어 개발 생명주기(SDLC, Software Development Life Cycle) 전 단계의 대응 기준으로 활용.
- 주요 목적 : 공통 위험 언어 제공과 **안전한 소프트웨어 개발 생명주기**(S-SDLC, Secure Software Development Life Cycle) 내재화를 통한 침해 사고 예방.

## Ⅱ. OWASP Top 10의 특징 및 장점

- 핵심 요약 : 데이터 기반의 위험 순위와 주기적 개정이 우선순위 중심의 점검을 가능하게 하는 구조.

1. 공통 언어 : 개발, 운영, 보안 조직이 같은 위험 목록을 기준으로 대화 → 점검 항목의 중복과 누락 감소.
2. 데이터 기반 개정 : 취약점 집계 결과를 주기적으로 반영 → 새 위험 유형과 아키텍처 변화를 목록에 반영.
3. 전 주기 적용 : 설계, 개발, 배포, 운영 단계별로 대응 항목을 제시 → 사후 패치 비용 감소와 선제적 대응.

## Ⅲ. OWASP Top 10의 구조 (흐름)

- 핵심 요약 : 열 개 위험을 설계, 개발, 배포, 운영의 생명주기 단계에 배치해 단계별 통제를 설계하는 구조.

```text
[ 1. 설계 ]
  A01 Broken Access Control
  A04 Cryptographic Failures
  A06 Insecure Design
  A07 Authentication Failures
   ↓
[ 2. 개발·빌드 ]
  A03 Software Supply Chain
  A05 Injection
  A10 예외 처리 실패
   ↓
[ 3. 배포·설정 ]
  A02 Security Misconfiguration
  A08 무결성 실패
   ↓
[ 4. 운영·모니터링 ]
  A09 로깅·경보 실패
```

- A01 : **Broken Access Control** (비인가 리소스 접근, BOLA(Broken Object Level Authorization), IDOR(Insecure Direct Object Reference), SSRF(Server-Side Request Forgery)).
- A02 : **Security Misconfiguration** (기본 계정 방치, 불필요 기능 개방, 클라우드 설정 오류).
- A03 : **Software Supply Chain Failures** (오픈소스 의존성 오염, CI/CD(Continuous Integration/Continuous Delivery) 빌드 파이프라인 변조).
- A04 : **Cryptographic Failures** (취약한 알고리즘 사용, 평문 전송, 키 하드코딩).
- A05 : **Injection** (SQL Injection, NoSQL Injection, OS Command Injection).
- A06 : **Insecure Design** (위협 모델링 부재, 설계 단계 통제 결여).
- A07 : **Authentication Failures** (무차별 대입, 크리덴셜 스터핑, 취약한 세션 관리).
- A08 : **Software or Data Integrity Failures** (서명되지 않은 플러그인, 안전하지 않은 역직렬화).
- A09 : **Security Logging and Alerting Failures** (침해 흔적 미기록, 경보 지연에 따른 사고 은닉).
- A10 : **Mishandling of Exceptional Conditions** (오류 시 Fail-Open 전환, 상세 스택 트레이스 노출).

## Ⅳ. OWASP Top 10의 비교

- 핵심 요약 : 2021판과 2025판의 차이는 설정, 공급망 등 클라우드와 빌드 환경의 위험이 커지고 SSRF가 접근 통제로 통합된 변화.

| 구분 | OWASP Top 10 (2021) | OWASP Top 10 (2025) | 변화의 의미 |
| --- | --- | --- | --- |
| 1위 유지 | A01 Broken Access Control | A01 Broken Access Control | SSRF(2021 A10)가 A01 하위로 통합 |
| 순위 상승 | A05 Security Misconfiguration | A02 Security Misconfiguration | 클라우드 전환으로 설정 오류 비중 상승 |
| 범위 확대 | A06 Vulnerable and Outdated Components | A03 Software Supply Chain Failures | 라이브러리 취약점에서 빌드·배포 공급망 신뢰 실패로 확대 |
| 신규 진입 | 별도 범주 없음 | A10 Mishandling of Exceptional Conditions | 예외 처리와 복구 과정의 결함을 독립 범주로 신설 |

## Ⅴ. OWASP Top 10의 한계와 방안

- 핵심 요약 : 접근 통제, 공급망, 예외 처리의 세 한계를 중앙 인가, 구성 목록 자동화, 안전한 기본값으로 통제하는 구조.

```text
[ 예외 발생 시 기본 동작 ]

정상 경로 → 인가 검사 → 허용 또는 차단
   ↓ 예외 발생
Fail-Open : 검사 생략 후 허용 (위험)
Fail-Secure : 차단 후 일반 오류 응답
```

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| A01 접근 통제 결함 | 비즈니스 로직 결함이라 시그니처 기반 SAST(Static Application Security Testing)와 DAST(Dynamic Application Security Testing)로 탐지가 어려움 | 모든 요청의 권한을 DB 쿼리 수준에서 강제하는 중앙 인가 구조, PDP(Policy Decision Point)와 PEP(Policy Enforcement Point) 적용 | 인가 검사가 누락된 API 건수 |
| A03 공급망 실패 | 깊은 전이 의존성과 은닉된 악성 컴포넌트 탐지 한계 | CI/CD 파이프라인에 SBOM(Software Bill of Materials) 자동 생성, SCA(Software Composition Analysis) 점검, SLSA(Supply-chain Levels for Software Artifacts) 기반 빌드 서명 검증 | SBOM 생성 빌드 비율 |
| A10 예외 처리 실패 | 장애 시 보안 통제가 해제되는 Fail-Open과 상세 오류의 정보 노출 | 기본값을 Fail-Secure로 정하고 사용자에게는 일반화된 오류 코드만 반환 | 예외 경로 점검 누락 건수 |

## Ⅵ. OWASP Top 10에 대한 기술사적 제언

- 핵심 요약 : 위험 목록을 점검표가 아닌 설계, 개발, 운영 전 주기의 의사결정 기준으로 내재화.

1. 기획 단계에서 위협 모델링을 필수 산출물로 두고, 설계 리뷰에서 접근 통제와 인증 흐름을 먼저 검증한다.
2. 개발 조직은 정적 분석과 의존성 점검을 빌드 파이프라인의 기본 단계로 두되, 도구로 잡기 어려운 로직 결함은 코드 리뷰와 침투 테스트로 보완한다.
3. 운영 단계에서는 실행 중 공격을 막는 RASP(Runtime Application Self-Protection)와 Policy-as-Code 기준을 전사에 통일하고, 로그 체계를 함께 묶어 사고 징후를 조기에 포착한다.

## Ⅶ. 결론

- 핵심 요약 : OWASP Top 10은 웹 보안 위험을 공통 언어로 정리한 출발점이며, 효과는 전 주기 내재화에서 나옴.
- 시사점 : 위험 목록을 체크리스트로만 쓰지 않고 설계, 빌드, 운영 단계의 대응 기준과 연결하는 것이 중요.
