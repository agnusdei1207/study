---
title: "비인간 신원(NHI, Non-Human Identities)"
author: "agnusdei1207"
date: "2026-10-24T22:56:33+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 비인간 신원(NHI), 머신 신원(Machine Identity), 서비스 계정, API 키, 비밀키(Secret)
- 단기 자격증명(Just-In-Time), SPIFFE/SPIRE, 고아 계정(Orphaned NHI), 권한 크리프(Permission Creep)
- CIEM(Cloud Infrastructure Entitlement Management), 시크릿 하드코딩, UEBA(User and Entity Behavior Analytics)

## Ⅰ. 비인간 신원(NHI, Non-Human Identities)의 개요

- 핵심 요약 : 사람이 아닌 서비스와 머신이 쓰는 자격 정보를 발견, 보호, 폐기하는 수명주기 관리 체계.
- 개념 : 사람 사용자가 아닌 머신, 애플리케이션, 서비스 계정, API(Application Programming Interface) 키, OAuth(Open Authorization) 토큰, 비밀키, CI(Continuous Integration)/CD(Continuous Delivery) 러너 등 시스템 간 통신과 자원 접근을 위해 발급되는 **머신 신원** (Machine Identity).
- 배경 및 필요성 : 클라우드 네이티브와 MSA(Microservice Architecture), 자동화 파이프라인이 늘면서 비인간 신원의 수가 사람 계정을 크게 웃돌고, MFA(Multi-Factor Authentication)를 적용하기 어려운 데다 수명주기 관리가 부재해 주요 공격 표면으로 떠오름.
- 주요 목적 : 머신 계정의 가시성 확보, 과도한 권한 회수, 정적 비밀키 제거와 신원 수명주기 자동화.

## Ⅱ. 비인간 신원(NHI, Non-Human Identities)의 특징 및 장점

- 핵심 요약 : 사람 중심 통제로 다루기 어려운 신원을 단기 자격 정보와 자동화로 관리해 노출 시간을 줄이는 방식.

1. 다요소 인증 부재 : 기계 간 통신에는 사람이 개입하는 OTP(One-Time Password)나 생체인증을 붙일 수 없음 → 키가 탈취되면 즉시 악용 가능.
2. **정적 시크릿의 동적 전환** (Just-In-Time) : 코드나 환경변수에 고정된 키 대신 **단기 자격증명** 발급 → 키 유출 시 재사용 기간이 수 분에서 수 시간으로 제한.
3. 워크로드 신원 증명 : **SPIFFE/SPIRE** (SPIFFE: Secure Production Identity Framework For Everyone) 기반 X.509 SVID(SPIFFE Verifiable Identity Document)로 컨테이너 워크로드 간 상호 인증 → 고정 IP나 공유 비밀키 의존 감소.
4. 수명주기 자동화 : 신원 생성, 회전, 폐기를 정책으로 처리 → 방치된 계정 감소.

```text
[ 단기 자격증명 발급 흐름 ]

CI/CD 파이프라인 (워크로드)
        ↓ 워크로드 신원 증명
중앙 시크릿 관리 플랫폼
  인증 검증 → 최소 권한 평가
        ↓ 단기 토큰 발급
워크로드가 토큰으로 자원 접근
        ↓ 유효 기간 만료 시 자동 폐기
```

## Ⅲ. 비인간 신원(NHI, Non-Human Identities)의 구성 요소 및 흐름

- 핵심 요약 : 인간 신원은 인사 체계에 묶여 관리되지만 비인간 신원은 생성 주체가 흩어져 있어 수명주기가 방치되기 쉬움.

```text
[ 비인간 신원 수명주기 ]

생성 (소유자 지정)
        ↓
사용 (최소 권한 부여)
        ↓
미사용 감지 (일정 기간 경과)
        ↓
격리 후 폐기
```

| 비교 항목 | 인간 신원 (Human Identity) | 비인간 신원 (NHI) |
| --- | --- | --- |
| 신원 주체 | 임직원, 고객, 협력업체 직원 | 서버, 컨테이너, 함수, CI/CD 러너, API 키 |
| 신원 수량 | 조직 인원에 비례 | 사람 계정을 크게 초과 |
| 인증 수단 | ID·비밀번호와 피싱 저항 MFA | API 키, X.509 인증서, JWT(JSON Web Token), OAuth 시크릿 |
| 주요 침해 원인 | 피싱, 소셜 엔지니어링 | 소스코드 하드코딩 유출, 과다 권한 |
| 수명주기 | 입사·퇴사 절차와 연동 | 생성 후 방치, 소유자 불명 |

- 보안 통제가 사람 사용자의 MFA와 SSO(Single Sign-On)에 집중된 사이, 공격자는 권한이 크고 관리가 느슨한 비인간 신원을 주요 침투 경로로 악용함.

## Ⅳ. 비인간 신원(NHI, Non-Human Identities)의 비교 분석

- 핵심 요약 : 영구 정적 키와 단기 동적 자격증명의 차이는 키 유출 시 피해 기간과 권한 범위를 가름.

| 비교 축 | 정적 시크릿 (영구 키) | 단기 자격증명 (동적 발급) |
| --- | --- | --- |
| 유효 기간 | 무기한 또는 장기간 | 수 분에서 수 시간 |
| 유출 시 영향 | 재사용 공격이 장기간 가능 | 만료 이후 재사용 차단 |
| 저장 위치 | 소스코드, 환경변수에 고정 | 메모리에 일시 주입 |
| 관리 방식 | 수동 교체, 잊히기 쉬움 | 정책 기반 자동 발급과 폐기 |

## Ⅴ. 비인간 신원(NHI, Non-Human Identities)의 한계와 방안

- 핵심 요약 : 하드코딩 유출, 고아 계정, 권한 과다가 주요 한계이며 사전 차단과 자동 회수로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 시크릿 하드코딩 유출 | 테스트용 키를 소스코드에 커밋하여 공개 저장소로 노출 | Git 사전 커밋 훅(TruffleHog, Gitleaks)으로 커밋 차단, 노출 시 즉시 키 폐기 | 탐지된 시크릿 건수 |
| 고아 계정 방치 | 소유자 퇴사나 프로젝트 종료 후에도 관리자 권한 계정이 남음 | 소유자 태깅 의무화, 일정 기간 미사용 시 자동 격리 | 소유자 미지정 계정 비율 |
| 권한 크리프(Permission Creep) | 개발 편의로 전체 관리 권한 부여 → 단일 워크로드 침해 시 클라우드 전체 장악 | CIEM(Cloud Infrastructure Entitlement Management)으로 실제 호출 이력을 분석해 최소 권한 정책으로 자동 축소 | 과다 권한 계정 수 |

## Ⅵ. 비인간 신원(NHI, Non-Human Identities)에 대한 기술사적 제언

- 핵심 요약 : 머신 신원을 전사 IAM의 정식 관리 대상으로 편입하고, 비밀 없는 구조와 행위 감시로 통제를 상시화해야 함.

1. 전사 IAM(Identity and Access Management) 정책에 비인간 신원을 포함하고, CISO(Chief Information Security Officer) 관할 아래 인벤토리 감사를 정례화하는 것이 필요함.
2. 장기 시크릿을 저장소에 두지 않고 워크로드 신원 연동으로 전환하는 비밀 없는 구조(Secretless Architecture)를 신규 시스템의 기본값으로 삼는 것이 바람직함.
3. 평소 호출하지 않던 리전이나 민감 API 호출을 UEBA(User and Entity Behavior Analytics)로 탐지하여 자격 정보를 즉시 무효화하는 자동 대응 체계를 갖추는 것이 필요함.

## Ⅶ. 결론

- 핵심 요약 : 비인간 신원은 사람 계정보다 많고 권한도 큰 신원 집단이므로 수명주기 관리가 보안의 출발점임.
- 시사점 : 단기 자격증명과 최소 권한이 기본값이 될 때 머신 신원의 노출 위험이 실질적으로 줄어듦.
