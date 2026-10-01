---
title: "비인간 신원(NHI, Non-Human Identities)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 비인간 신원(NHI, Non-Human Identities)의 개요

- **개념** : 사람 사용자가 아닌 머신, 애플리케이션, 서비스 어카운트, API 키, OAuth 토큰, 비밀키, CI/CD 러너 등 시스템과 시스템(M2M) 간의 통신 및 자원 접근을 위해 발급되는 디지털 신원(Machine Identity).
- **배경 및 필요성** : 클라우드 네이티브, 마이크로서비스(MSA), 자동화 파이프라인의 폭발적 증가로 비인간 신원(NHI)의 수가 인간 직원의 10~50배를 초과하였으며, MFA 적용 불가, 수명주기 관리 부재로 인해 최우선 공격 표면으로 부상.
- **핵심 목적** : 머신 및 서비스 계정의 가시성(Inventory) 확보, 과도한 권한(Permission Creep) 회수, 정적 비밀키 제거 및 기계 신원의 수명주기 자동화.

## Ⅱ. 비인간 신원(NHI, Non-Human Identities)의 핵심 아키텍처 및 동작 메커니즘

NHI 보안은 시스템에 분산된 모든 비인간 신원을 식별(Discovery)하고, 시크릿 볼트를 통해 안전하게 주입(Inject)하며, 사용 후 단기 토큰을 즉시 파기(Rotation)하는 라이프사이클로 제어됨.

```text
[ 비인간 신원(NHI) 보안 관리 및 단기 토큰 주입 프로세스 ]

  [ CI/CD 파이프라인 / 쿠버네티스 파드 (머신 워크로드) ]
                          │
                          ▼ 1. 워크로드 신원 증명 (SPIFFE / OIDC 토큰 제시)
  +-------------------------------------------------------------+
  | 중앙 시크릿/머신 신원 관리 플랫폼 (HashiCorp Vault, CyberArk)|
  |  - Step 1: 워크로드 무결성 및 플랫폼 인증 검증              |
  |  - Step 2: 요청된 작업에 필요한 최소 권한 평가              |
  |  - Step 3: 장기 정적 키 대신 "단기 임시 자격증명" 동적 생성|
  +------------------------------┬------------------------------+
                                 │ 2. 임시 토큰(TTL: 15분) 발급
                                 ▼
  [ 워크로드 메모리 주입 ] ──(DB 쿼리 실행)──> [ 클라우드 프로덕션 DB ]
                                                     │
                                                     ▼
  * 15분 후 토큰 자동 만료(Revoke) -> 키 유출 시에도 재사용 공격 원천 차단!
```

- **비인간 신원(NHI)의 폭증** : 서비스 계정(GCP Service Account, AWS IAM Role), CI/CD Secret, 깃허브 PAT(Personal Access Token), SSH 키 등 다양화.
- **MFA 적용 불가의 구조적 결함** : 기계 간 자동화 통신 특성상 사람이 개입하는 스마트폰 OTP나 생체인증(MFA)을 적용할 수 없어 키 탈취 시 즉각 악용.
- **정적 시크릿의 동적 임시 자격증명 전환** : 소스코드나 환경변수에 고정된 영구 키 대신, Vault 연계를 통해 수 분~수 시간만 유효한 단기 토큰(Just-In-Time) 발급.
- **SPIFFE/SPIRE 기반 머신 신원 표준화** : IP나 정적 비밀키 대신 암호학적 X.509 SVID(SPIFFE Verifiable Identity Document)를 통해 컨테이너 워크로드 간 상호 인증.

## Ⅲ. 비인간 신원(NHI, Non-Human Identities)의 세부 구성 요소 및 비교 분석

| 비교 항목 | 인간 신원 (Human Identity) | 비인간 신원 (Non-Human Identity, NHI) |
| --- | --- | --- |
| 신원 주체 | 임직원, 고객, 외부 협력업체 개발자 | 서버, 컨테이너, Lambda 함수, CI/CD 러너, API 키 |
| 신원 수량 | 조직 임직원 수에 비례 (통상 수천 개) | 인간 수의 10~50배 폭증 (수만~수십만 개) |
| 인증 메커니즘 | ID/PW + 피싱 저항 MFA (FIDO2, OTP) | API Key, X.509 인증서, JWT, OAuth Secret (MFA 불가) |
| 주요 침해 원인 | 피싱, 소셜 엔지니어링, 크리덴셜 스터핑 | GitHub 소스코드 하드코딩 유출, 권한 과다 부여 |
| 수명주기 관리 | 입사-발령-퇴사 프로세스 일치 (HR 연동) | 생성 후 방치(Orphaned), 소유자 불명, 무기한 유효 |

- 보안 통제가 인간 사용자(MFA, SSO)에 집중된 사이, 해커들은 취약하고 권한이 막강하며 관리가 방치된 비인간 신원(API 키, 서비스 계정)을 최우선 침투 경로로 악용함.

## Ⅳ. 비인간 신원(NHI, Non-Human Identities)의 주요 한계점 및 해결 방안

- **공개 코드 저장소(GitHub) 및 빌드 로그 내 시크릿 하드코딩 유출** :
  - **한계점** : 개발자가 테스트용 AWS 키나 DB 비밀번호를 소스코드에 커밋하여 수 분 내에 다크웹 스캐너에 털리는 사고 빈발.
  - **해결 방안** : Git 프리커밋 훅(TruffleHog, Gitleaks)을 통해 시크릿 포함 시 커밋을 강제 차단하고, 저장소 시크릿 스캔 시 즉시 키 자동 폐기(Revocation).
- **소유자 불명 및 퇴사자가 생성한 고아 계정(Orphaned NHI) 방치** :
  - **한계점** : 프로젝트 완료 후에도 서비스 계정이 삭제되지 않고 수년간 관리자 권한을 보유한 채 침투 통로로 악용.
  - **해결 방안** : NHI 보안 태세 관리(NHI-SPM) 도구를 도입하여 모든 머신 계정에 소유자(Owner) 태깅을 강제하고, 90일 미사용 시 자동 격리.
- **기계 간 통신에서 과도한 관리자 권한 부여(권한 크리프)** :
  - **한계점** : 개발 편의를 위해 머신 계정에 'AdministratorAccess' 또는 'Full Control'을 부여하여 단일 파드 침해 시 클라우드 전체 장악.
  - **해결 방안** : CIEM(Cloud Infrastructure Entitlement Management)을 통해 실제 사용된 최소 API 호출만 역추적하여 최소 권한 정책으로 자동 다운그레이드.

## Ⅴ. 비인간 신원(NHI, Non-Human Identities) 적용 및 발전을 위한 기술사적 제언

- **'머신 신원 전담 거버넌스(Machine Identity Management)' 수립** : 전사 IAM 정책에 비인간 신원을 정식 관리 대상으로 포함하고 CISO 관할 하에 인벤토리 감사 정례화.
- **비밀 없는 환경(Secretless Architecture) 구현** : 영구적인 시크릿을 저장소에 두지 않고 클라우드 네이티브 워크로드 신원 연동(AWS IAM Roles for Service Accounts) 전면 전환.
- **비인간 신원의 이상 행위 실시간 모니터링** : 기계 계정이 평소 호출하지 않던 비정상 리전이나 민감 API(예: IAM CreateUser)를 호출할 때 즉시 토큰을 무효화하는 AI UEBA 연동.
