---
title: "공급망 보안(Supply Chain Security)"
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

## Ⅰ. 공급망 보안(Supply Chain Security)의 개요

- ** 개념** : 소프트웨어 기획, 소스 개발, 서드파티 오픈소스 반입, 빌드·패키징, 배포 및 운영에 이르는 전 생애주기에서 발생 가능한 위변조와 악성코드 주입을 차단하는 보안 체계.
- ** 배경 및 필요성** : 소프트웨어 개발부터 빌드, 패키징, 배포, 운영에 이르는 전 공급망 단계에서 서드파티 라이브러리 및 오픈소스 취약점을 악용한 오염 사고가 폭증함에 따라, SBOM 및 무결성 서명 체계를 구축하기 위해 대두됨.
- ** 핵심 목적** : 단일 오픈소스 컴포넌트 오염이나 CI/CD 침해로 인해 수천 개의 다운스트림 고객사로 침해가 일괄 확산되는 공급망 파급 효과 차단 및 전주기 신뢰성 보장.

## Ⅱ. 공급망 보안(Supply Chain Security)의 핵심 아키텍처 및 동작 메커니즘

공급망 보안(Supply Chain Security)은(는) 신뢰할 수 있는 보안 구조와 표준화된 절차를 기반으로 동작하며, 세부적인 아키텍처와 구성요소 간의 상호작용 메커니즘은 다음과 같음.

```text
[ 1. 소스 개발 단계 ]
개발자 커밋 ──▶ [ GPG / SSH 커밋 서명 ] ──▶ [ 시크릿 스캐닝 & SAST 검사 ]
                                                    │
                                                    ▼
[ 2. 격리된 빌드 단계 (SLSA Level 3) ]
[ 에펨럴 CI 빌드 러너 ] ◀── [ 무키(Keyless) OIDC 인증 ]
  ├── 1. 허가된 소스코드만 체크아웃
  ├── 2. 사내 미러 레지스트리 의존성만 격리 다운로드
  └── 3. 재현 가능한 빌드(Hermetic Build) 수행
                                                    │
                                                    ▼
[ 3. 아티팩트 서명 및 SBOM 생성 ]
컴파일 완료 ──▶ [ SPDX / CycloneDX SBOM 자동 생성 ]
              ──▶ [ in-toto 메타데이터 (출처 증명 Provenance) 기록 ]
              ──▶ [ Sigstore (Cosign) 기반 아티팩트 서명 ]
                                                    │
                                                    ▼
[ 4. 배포 및 런타임 수락 (Zero Trust Admission) ]
쿠버네티스 클러스터 배포 요청 ──▶ [ OPA Gatekeeper / Kyverno Admission Controller ]
                                 ├── 1. Sigstore 서명 유효성 검증
                                 ├── 2. SLSA Level 3 출처 증명서 확인
                                 └── 3. 미검증 이미지 배포 즉시 거부(Deny)
```

- ** 소스 개발 (Code)** : 커밋 서명 강제, 깃허브 브랜치 보호 규칙, 2인 이상 코드 리뷰(PR) 필수 (Git GPG Signing, Branch Protection Rules).
- ** 의존성 반입 (Dependencies)** : 사내 프라이빗 패키지 미러 운영, 라이선스 및 취약점 검증 후 반입 (Nexus, Artifactory, Socket.dev, Snyk SCA).
- ** 빌드 실행 (Build)** : 독립된 임시 컨테이너에서 네트워크가 격리된 밀폐형(Hermetic) 빌드 수행 (Google Cloud Build, GitHub Hosted Runners (SLSA L3)).
- ** 패키징/증명 (Package)** : 빌드 완료 산출물에 대해 자동화된 출처 증명서(Attestation) 및 SBOM 생성 (CycloneDX, SPDX, in-toto, Cosign).
- ** 배포/운영 (Deploy/Run)** : 쿠버네티스 어드미션 컨트롤러에서 서명 및 정책 미충족 컨테이너 배포 차단 (OPA Gatekeeper, Kyverno, VEX 취약점 필터링).

## Ⅲ. 공급망 보안(Supply Chain Security)의 세부 구성 요소 및 비교 분석

| 비교 항목 | SLSA (Supply-chain Levels for Software Artifacts) | NIST SSDF (Secure Software Development Framework) |
|---|---|---|
| 주도 기관 | 구글, OpenSSF, 리눅스 재단 | 미국 국립표준기술원 (NIST SP 800-218) |
| 프레임워크 성격 | 기술적·아키텍처적 무결성 체크리스트 (Level 1~3) | 전사적 소프트웨어 보안 개발 수명주기 프로세스 가이드라인 |
| 중점 평가 영역 | 소스 무결성, 빌드 플랫폼 격리, 출처 증명(Provenance) 생성 | 조직 준비, 안전한 소프트웨어 보호, 취약점 대응 전반 |
| 검증 방식 | 기계 판독형 in-toto attestation을 통한 자동화 암호학적 검증 | 감사 체크리스트, 자체 인증(Self-Attestation) 서약서 |
| 규제 연계성 | 클라우드 네이티브 DevSecOps 파이프라인 표준 | 미국 백악관 행정명령(EO 14028) 연방정부 소프트웨어 납품 요건 |

- 공급망 보안(Supply Chain Security)은(는) 상기 핵심 비교 지표와 아키텍처 구성을 바탕으로 보안 위협에 대한 방어 효과성을 극대화하며, 기존 레거시 통제 기법 대비 우수한 신뢰성과 운영 효율성을 제공함.

## Ⅳ. 공급망 보안(Supply Chain Security)의 주요 한계점 및 해결 방안

- ** 대규모 레거시 프로젝트의 경우 수만 개의 간접 의존성 관련 보안 한계 및 취약점** : - ** 한계점** : 대규모 레거시 프로젝트의 경우 수만 개의 간접 의존성으로 인해 SBOM 생성 시 취약점이 수천 건 도출되어 조치 불가능.
  - ** 해결 방안** : 취약점의 실제 함수 호출 여부(Reachable Path)를 분석하는 VEX(Vulnerability Exploitability eXchange)를 연동하여 실제 위험한 결함만 95% 이상 압축 필터링.
- ** 개발자 PC 및 빌드 러너 환경에 정적 배포 토큰이 취약점** : - ** 한계점** : 개발자 PC 및 빌드 러너 환경에 정적 배포 토큰이 노출되어 자가 증식 웜(Shai-Hulud 등)에 의한 탈취 위험.
  - ** 해결 방안** : 장기 토큰을 전면 폐기하고 OpenID Connect(OIDC) 기반 단기 자격증명 발급(Sigstore Fulcio / GitHub OIDC) 체계 구축.
- ** 오픈소스 프로젝트 소유자가 사망하거나 계정이 하이재 취약점** : - ** 한계점** : 오픈소스 프로젝트 소유자가 사망하거나 계정이 하이재킹되어 악성 업데이트가 정식 릴리스되는 공격.
  - ** 해결 방안** : 주요 오픈소스에 대해 릴리스 즉시 사내 도입을 차단하고, 24~48시간의 카나리아 격리(Quarantine) 후 동적 행위 검증 거쳐 반입.
- ** 빌드 환경(OS, 컴파일러 버전, 타임스탬프) 차이 관련 보안 한계 및 취약점** : - ** 한계점** : 빌드 환경(OS, 컴파일러 버전, 타임스탬프) 차이로 인해 바이너리 바이트 일치성 검증(Reproducible Builds) 난항.
  - ** 해결 방안** : 빌드 환경 전체를 도커 불변 이미지로 고정하고 SOURCE_DATE_EPOCH 표준 타임스탬프를 적용하여 결정론적 컴파일 보장.

## Ⅴ. 공급망 보안(Supply Chain Security) 적용 및 발전을 위한 기술사적 제언

- ** 컴포넌트 거버넌스 중심의 거버넌스 및 실행 체계 구축** : CI 파이프라인 내 CycloneDX SBOM 생성 및 VEX 문서 실시간 게시 자동화을(를) 적극 추진하여, 신규 취약점(Log4j 등) 발생 시 영향 자산 식별 10분 이내 완료 효과를 극대화해야 함.
- ** 빌드 신뢰성 중심의 거버넌스 및 실행 체계 구축** : SLSA 레벨 3 표준을 충족하는 완전 격리형 에펨럴(Ephemeral) 빌드 환경 구축을(를) 적극 추진하여, 빌드 시점의 악성 백도어 주입(SolarWinds형 공격) 원천 차단 효과를 극대화해야 함.
- ** 런타임 제로트러스트 중심의 거버넌스 및 실행 체계 구축** : 배포 게이트웨이에서 Cosign 서명 및 출처 증명서가 없는 아티팩트 실행 전면 거부을(를) 적극 추진하여, 비인가/변조된 컨테이너 이미지의 프로덕션 배포 100% 방어 효과를 극대화해야 함.
