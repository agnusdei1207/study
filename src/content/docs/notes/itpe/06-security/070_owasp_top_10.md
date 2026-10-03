---
title: "OWASP Top 10"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. OWASP Top 10의 개요

- 개념 : 웹 애플리케이션의 개발, 시험, 운영 전주기에서 가장 광범위하게 발생하며 치명적인 피해를 초래하는 **상위 10대 보안 위험**을 체계화한 **OWASP** 글로벌 보안 표준 가이드라인.
- 배경 및 필요성 : 웹 애플리케이션 및 API를 대상으로 빈발하는 심각한 보안 취약점 패턴을 통계적으로 집계하여, 개발자 및 보안 관리자가 **시큐어 코딩**과 SDLC 전주기에서 우선순위화된 보안 대책을 구현할 수 있도록 가이드라인으로 제시됨.
- 핵심 목적 : 개발자 및 보안팀에게 공통된 보안 언어와 위험 기준을 제시하고, **안전한 소프트웨어 개발 생명주기** (S-SDLC) 내재화를 통한 침해사고 사전 예방.

## Ⅱ. OWASP Top 10의 핵심 아키텍처 및 동작 메커니즘

OWASP Top 10은(는) 신뢰할 수 있는 보안 구조와 표준화된 절차를 기반으로 동작하며, 세부적인 아키텍처와 구성요소 간의 상호작용 메커니즘은 다음과 같음.

```text
[ 1. 요구사항 및 설계 (Plan & Design) ]
   ├── A01: Broken Access Control (RBAC/ABAC 모델링, SSRF 방어)
   ├── A04: Cryptographic Failures (안전한 암호 알고리즘 선정)
   ├── A06: Insecure Design (위협 모델링, 안전한 설계 패턴)
   └── A07: Identification and Authentication Failures (MFA/패스키 설계)
       │
       ▼
[ 2. 개발 및 빌드 (Code & Build) ]
   ├── A03: Software Supply Chain Failures (SCA, SBOM 생성, 서명 검증)
   ├── A05: Injection (PreparedStatement, ORM 파라미터 바인딩)
   └── A10: Mishandling of Exceptional Conditions (Fail-Secure 예외 처리)
       │
       ▼
[ 3. 배포 및 인프라 (Deploy & Test) ]
   ├── A02: Security Misconfiguration (IaC 보안 검사, 불필요 포트 차단)
   └── A08: Software and Data Integrity Failures (자동 업데이트 서명 검증)
       │
       ▼
[ 4. 운영 및 모니터링 (Operate & Monitor) ]
   └── A09: Security Logging and Alerting Failures (SIEM 로그 감사, 실시간 경보)
```

- A01 : **Broken Access Control** (비인가 리소스 접근, BOLA, IDOR, SSRF).
- A02 : **Security Misconfiguration** (기본 계정 방치, 불필요 기능 개방, 클라우드 오설정).
- A03 : **Software Supply Chain Failures** (오픈소스 의존성 오염, CI/CD 빌드 파이프라인 변조).
- A04 : **Cryptographic Failures** (취약한 암호(DES, MD5), 평문 전송, 키 하드코딩).
- A05 : **Injection** (SQLi, NoSQLi, OS Command Injection).
- A06 : **Insecure Design** (위협 모델링 부재, 설계 단계의 보안 통제 결여, 안전하지 않은 비즈니스 로직).
- A07 : **Identification & Authentication** (무차별 대입, 크리덴셜 스터핑, 취약한 세션 관리).
- A08 : **Software & Data Integrity Failures** (서명되지 않은 플러그인, 안전하지 않은 역직렬화).
- A09 : **Security Logging & Alerting Failures** (침해 흔적 미기록, 경보 지연으로 인한 사고 은닉).
- A10 : **Mishandling of Exceptional Conditions** (오류 발생 시 **Fail-Open** 전환, 상세 스택트레이스 노출).

## Ⅲ. OWASP Top 10의 세부 구성 요소 및 비교 분석

| 구분 | OWASP Top 10 (2021) | OWASP Top 10 (2025) | 주요 개정 의미 및 배경 |
|---|---|---|---|
| 1위 유지 | A01: Broken Access Control | A01: Broken Access Control | 여전히 가장 널리 퍼진 결함으로 1위 유지, SSRF(구 A10)를 A01 하위로 통합 흡수 |
| 순위 상승 | A05: Security Misconfiguration | A02: Security Misconfiguration | 클라우드 전환 가속화에 따라 복잡한 설정 오류가 2위로 급상승 |
| 대폭 확대 | A06: Vulnerable Components | A03: Software Supply Chain Failures | 단순 라이브러리 취약점을 넘어 빌드/배포 공급망 전반의 신뢰 실패로 전면 확대 개편 |
| 신규 진입 | 해당 없음 (분산 존재) | A10: Mishandling of Exceptional Conditions | 예외 상황 및 오류 복구 시 발생하는 우회 및 충돌 결함을 독립 위험 범주로 신설 |

- OWASP Top 10은(는) 상기 핵심 비교 지표와 아키텍처 구성을 바탕으로 보안 위협에 대한 방어 효과성을 극대화하며, 기존 레거시 통제 기법 대비 우수한 신뢰성과 운영 효율성을 제공함.

## Ⅳ. OWASP Top 10의 주요 한계점 및 해결 방안

- 한계점 : 부동의 1위인 A01(접근통제 실패: BOLA/IDOR)은 비즈니스 로직 결함이므로 시그니처 기반 SAST/DAST 도구로 탐지 불가.
  - 해결 방안 : URL 파라미터 기반 조회를 금지하고, 모든 API 요청에 대해 호출 주체의 테넌트/사용자 권한을 DB 쿼리 레벨에서 강제하는 **서버 측 중앙 인가** (PDP/PEP) 프레임워크 구현.
- 한계점 : A03(소프트웨어 공급망 실패)에서 오픈소스 라이브러리의 깊은 전이적 의존성 및 악성 컴포넌트 은닉 탐지 한계.
  - 해결 방안 : CI/CD 파이프라인에 **CycloneDX/SPDX** 기반 SBOM 자동 생성 및 **SLSA 프레임워크** 기반 빌드 서명(Cosign) 무결성 검증 강제화.
- 한계점 : A10(예외 처리 실패)으로 인해 서비스 장애 시 보안 통제가 해제되는 Fail-Open 취약점 및 상세 에러 로그를 통한 정보 유출.
  - 해결 방안 : 시스템 장애 시 모든 접근을 차단하는 **Fail-Secure** (또는 Fail-Close) 정책을 기본값으로 강제하고 사용자에게는 일반화된 에러 코드만 반환.

## Ⅴ. OWASP Top 10 적용 및 발전을 위한 기술사적 제언

- 기획 단계 기반 보안 아키텍처 수립 : **위협 모델링** 및 시큐어 설계을(를) 체계적으로 도입하여 통제 수준을 강화해야 함.
- 빌드 단계 기반 보안 아키텍처 수립 : **SAST/SCA/SBOM** 자동 파이프라인을(를) 체계적으로 도입하여 통제 수준을 강화해야 함.
- 런타임 기반 보안 아키텍처 수립 : **RASP** 및 Policy-as-Code 강제을(를) 체계적으로 도입하여 통제 수준을 강화해야 함.
