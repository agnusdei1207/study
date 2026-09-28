---
title: "OWASP Top 10"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "070. OWASP Top 10"
  badge:
    text: "서브"
    variant: note
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "서브"
---

## 지식 로드맵 내 현재 위치

정보보안 → 애플리케이션 보안 → OWASP 웹 애플리케이션 취약점(OWASP Top 10)

## 30초 인출

- **본질:** 전 세계 수십만 건의 애플리케이션 취약점 분석 데이터와 전문가 설문을 바탕으로 웹 애플리케이션에서 가장 치명적이고 빈번한 상위 10대 보안 위험을 선정한 글로벌 보안 기준
- **메커니즘:** CWE 기반 데이터 수집/분석 → A01(접근통제 실패)부터 A10(예외조건 처리 실패) 범주 정의 → SDLC 단계별 위협 모델링 및 DevSecOps 파이프라인 연계 방어
- 통찰: 단순 10대 항목에 대한 체크리스트 점검에 머무르지 않고, 1위를 유지한 A01 취약점 방어를 위한 서버 측 권한 강제 검증과 신규 대두된 A03 소프트웨어 공급망 보안을 DevSecOps 파이프라인에 내재화하는 체계 구축 필수

<details><summary>핵심 용어</summary>

- **OWASP Top 10:** 웹 애플리케이션 보안 인식 제고를 위해 OWASP 재단이 약 3~4년 주기로 개정 발표하는 10대 보안 위험 목록.
- **A01:2025 Broken Access Control:** 사용자가 인가되지 않은 리소스나 기능에 접근할 수 있는 취약점으로, 2021년에 이어 부동의 1위 유지(SSRF 포함).
- **A03:2025 Software Supply Chain Failures:** 기존 오픈소스 구성요소 취약점을 넘어 CI/CD 파이프라인, 종속성 오염, 서드파티 빌드 전반을 포괄하는 신설 범주.
- **A10:2025 Mishandling of Exceptional Conditions:** 에러, 타임아웃, 예외 상황 발생 시 Fail-Open으로 권한이 풀리거나 시스템 정보가 노출되는 신설 위험.
- **BOLA(Broken Object Level Authorization):** 사용자가 URL 파라미터나 ID 값을 조작하여 타인의 객체/데이터에 비인가 접근하는 결함.

</details>

---

## 2~4교시 예상문제 (25점)

> 웹 애플리케이션 보안 표준인 OWASP Top 10:2025의 주요 개정 내용과 10대 위험 범주를 설명하고, 2021년 대비 변화 분석 및 1위 취약점인 'A01 접근통제 실패'와 신설된 'A03 소프트웨어 공급망 실패'의 실무적 방어 대책을 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 웹 애플리케이션의 개발, 시험, 운영 전주기에서 가장 광범위하게 발생하며 치명적인 피해를 초래하는 상위 10대 보안 위험을 체계화한 OWASP 글로벌 보안 표준 가이드라인 |
| 목적 | 개발자 및 보안팀에게 공통된 보안 언어와 위험 기준을 제시하고, 안전한 소프트웨어 개발 생명주기(S-SDLC) 내재화를 통한 침해사고 사전 예방 |

## Ⅱ. OWASP Top 10의 주요 특징

| 특징 | 세부 내용 | 구현 요소 |
|---|---|---|
| 데이터 기반 실증 통계 | 전 세계 수십만 개 앱의 실제 테스트 데이터(CWE 기반)와 글로벌 보안 전문가 설문 결합 | 커뮤니티 기여 데이터셋, CVSS |
| 포괄적 위험 범주화 | 개별 취약점 단편 나열이 아닌 수십 개의 CWE를 상위 보안 리스크 범주로 그룹화 | CWE 매핑, 공격 패턴 분류 |
| 공급망 및 환경 변화 반영 | 클라우드 네이티브, 오픈소스 확산, 마이크로서비스 환경을 반영하여 2025년 버전 개편 | A03 공급망, A10 예외처리 |
| 컴플라이언스 준거성 | 전자정부 SW 보안약점 가이드, ISMS-P, PCI-DSS 등 국내외 주요 인증 심사의 표준 참조 기준 | 시큐어 코딩 기준 |

## Ⅲ. OWASP Top 10 (2025) 분류 체계 및 SDLC 적용 프로세스

```text
[ 1. 요구사항 및 설계 (Plan & Design) ]
   ├── A01: Broken Access Control (RBAC/ABAC 모델링, SSRF 방어)
   ├── A04: Cryptographic Failures (안전한 암호 알고리즘 선정)
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
   ├── A06: Insecure and Outdated Components (상시 취약점 모니터링)
   └── A09: Security Logging and Alerting Failures (SIEM 로그 감사, 실시간 경보)
```

| 취약점 코드 | 명칭 (2025) | 핵심 위험 내용 | 방어 메커니즘 |
|---|---|---|---|
| A01 | Broken Access Control | 비인가 리소스 접근, BOLA, IDOR, SSRF | 서버 측 인가 강제, 최소 권한 |
| A02 | Security Misconfiguration | 기본 계정 방치, 불필요 기능 개방, 클라우드 오설정 | 설정 자동화, IaC 정적 분석 |
| A03 | Software Supply Chain Failures | 오픈소스 의존성 오염, CI/CD 빌드 파이프라인 변조 | SBOM 생성, SCA 점검, 코드 서명 |
| A04 | Cryptographic Failures | 취약한 암호(DES, MD5), 평문 전송, 키 하드코딩 | AES-GCM, TLS 1.3, KMS 사용 |
| A05 | Injection | SQLi, NoSQLi, OS Command Injection | 매개변수화 쿼리, 입력 화이트리스트 |
| A06 | Insecure and Outdated Components | 패치되지 않은 오픈소스 CVE 취약점 보유 라이브러리 | 자동 패치 관리, 의존성 격리 |
| A07 | Identification & Authentication | 무차별 대입, 크리덴셜 스터핑, 취약한 세션 관리 | 피싱 저항성 패스키, 다중요소인증 |
| A08 | Software & Data Integrity Failures | 서명되지 않은 플러그인, 안전하지 않은 역직렬화 | 전자서명 검증, 직렬화 객체 검증 |
| A09 | Security Logging & Alerting Failures | 침해 흔적 미기록, 경보 지연으로 인한 사고 은닉 | WORM 로그 저장, 중앙 SIEM 연계 |
| A10 | Mishandling of Exceptional Conditions | 오류 발생 시 Fail-Open 전환, 상세 스택트레이스 노출 | Fail-Secure 원칙, 사용자 친화 에러 |

## Ⅳ. OWASP Top 10 2021 대비 2025 주요 변경사항 비교

| 구분 | OWASP Top 10 (2021) | OWASP Top 10 (2025) | 주요 개정 의미 및 배경 |
|---|---|---|---|
| 1위 유지 | A01: Broken Access Control | **A01: Broken Access Control** | 여전히 가장 널리 퍼진 결함으로 1위 유지, SSRF(구 A10)를 A01 하위로 통합 흡수 |
| 순위 상승 | A05: Security Misconfiguration | **A02: Security Misconfiguration** | 클라우드 전환 가속화에 따라 복잡한 설정 오류가 2위로 급상승 |
| 대폭 확대 | A06: Vulnerable Components | **A03: Software Supply Chain Failures** | 단순 라이브러리 취약점을 넘어 빌드/배포 공급망 전반의 신뢰 실패로 전면 확대 개편 |
| 신규 진입 | 해당 없음 (분산 존재) | **A10: Mishandling of Exceptional Conditions** | 예외 상황 및 오류 복구 시 발생하는 우회 및 충돌 결함을 독립 위험 범주로 신설 |

## Ⅴ. OWASP Top 10 대응의 한계와 방안

| 한계 | 방안 |
|---|---|
| 부동의 1위인 A01(접근통제 실패: BOLA/IDOR)은 비즈니스 로직 결함이므로 시그니처 기반 SAST/DAST 도구로 탐지 불가 | URL 파라미터 기반 조회를 금지하고, 모든 API 요청에 대해 호출 주체의 테넌트/사용자 권한을 DB 쿼리 레벨에서 강제하는 서버 측 중앙 인가(PDP/PEP) 프레임워크 구현 |
| A03(소프트웨어 공급망 실패)에서 오픈소스 라이브러리의 깊은 전이적 의존성 및 악성 컴포넌트 은닉 탐지 한계 | CI/CD 파이프라인에 CycloneDX/SPDX 기반 SBOM 자동 생성 및 SLSA 프레임워크 기반 빌드 서명(Cosign) 무결성 검증 강제화 |
| A10(예외 처리 실패)으로 인해 서비스 장애 시 보안 통제가 해제되는 Fail-Open 취약점 및 상세 에러 로그를 통한 정보 유출 | 시스템 장애 시 모든 접근을 차단하는 Fail-Secure(또는 Fail-Close) 정책을 기본값으로 강제하고 사용자에게는 일반화된 에러 코드만 반환 |

## Ⅵ. 제언

```text
[ 사후 체크리스트 보안 ]             [ DevSecOps 내재화 연속 보안 ]
배포 전 일회성 진단 ──┐             ┌── 기획 단계: 위협 모델링 및 시큐어 설계
단순 도구 결과에 의존 ┼─→ [ 침해 노출 ] ─┼── 빌드 단계: SAST/SCA/SBOM 자동 파이프라인
A01/공급망 사각지대 ──┘             └── 런타임: RASP 및 Policy-as-Code 강제
```

| 평가 영역 | 레거시 점검 모델 | 현대적 DevSecOps 모델 | 향후 발전 방향 |
|---|---|---|---|
| 접근 통제 | 클라이언트 UI 숨김 | 서버 측 엄격한 세션 인가 | 제로 트러스트(ZTA) 지속 검증 연동 |
| 공급망 관리 | 개발자 자율 라이브러리 | 중앙 승인 저장소 + SBOM | AI 생성 코드 취약점 자동 감증(AIBOM) |
| 오류 처리 | 화면에 스택 에러 출력 | 중앙 예외 핸들러 + Fail-Secure | 자기 치유(Self-Healing) 마이크로서비스 |

OWASP Top 10:2025는 단순한 웹 취약점 목록이 아닌 클라우드와 소프트웨어 공급망 시대를 관통하는 필수 위험 거버넌스 척도이며, S-SDLC와 DevSecOps를 통해 설계부터 운영까지 전주기 보안 내재화 달성 필수.

## 출제 이력과 검증 출처

- 정보관리기술사 제124회 1교시 (OWASP Top 10 주요 취약점 및 대응 방안)
- 정보관리기술사 제136회 4교시 (소프트웨어 공급망 보안 및 오픈소스 취약점)
- OWASP Foundation: OWASP Top 10:2025 Standard Document
- OWASP A01:2025 Broken Access Control Specification
- NIST SP 800-218: Secure Software Development Framework (SSDF)
