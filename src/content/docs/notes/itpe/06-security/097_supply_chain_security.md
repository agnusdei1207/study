---
title: "공급망 보안(Supply Chain Security)"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  order: 97
  label: "097. 공급망 보안(Supply Chain Security)"
  badge:
    text: "기초"
    variant: note
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"

---

## 지식 로드맵 내 현재 위치

소프트웨어 보안 → 전주기 SDLC 보안 → 공급망 보안(Supply Chain Security)

## 30초 인출

- **본질:** 소프트웨어 개발, 빌드, 패키징, 유통 및 운영 전 수명주기에서 오픈소스 의존성, CI/CD 파이프라인, 빌드 산출물의 출처(Provenance)와 무결성을 지속 검증하는 보안 활동.
- **메커니즘:** 소스코드 커밋 서명 → 격리된 빌드 환경에서 위변조 방지 빌드(SLSA) → 기계 판독형 SBOM(SPDX/CycloneDX) 생성 및 암호학적 서명(Sigstore) → 런타임 배포 시 정책 검증(OPA).
- 통찰: 단순 정적 SBOM 수집만으로는 XZ Utils와 같은 악성 백도어를 적발할 수 없으므로, VEX 기반 실제 악용성 평가, SLSA 레벨 인증, 동적 행위 분석의 삼위일체 결합 필수.

<details><summary>핵심 용어</summary>

- **소프트웨어 공급망 보안**: 소프트웨어 제품을 구성하는 오픈소스, 타사 라이브러리, 빌드 도구 및 배포 채널의 변조 위험을 통제하는 보안 영역.
- **SBOM(Software Bill of Materials)**: 소프트웨어를 구성하는 모든 오픈소스 및 상용 컴포넌트의 명칭, 버전, 라이선스, 해시값을 명시한 디지털 명세서.
- **SLSA(Supply-chain Levels for Software Artifacts)**: 구글과 OpenSSF가 주도하는 소프트웨어 아티팩트의 변조 방지 및 출처 무결성 보증 프레임워크(Level 1~3).
- **VEX(Vulnerability Exploitability eXchange)**: SBOM에 명시된 특정 취약점이 해당 애플리케이션 실행 환경에서 실제로 악용 가능한지 여부를 기계 판독형으로 전달하는 표준.
- **Sigstore**: 개발자가 복잡한 개인키 관리 없이 OpenID Connect(OIDC)를 통해 아티팩트에 짧은 유효기간의 디지털 서명을 부여하는 오픈소스 공증 플랫폼.
</details>

---

## 2~4교시 예상문제 (25점)

> 소프트웨어 공급망(Software Supply Chain)의 생애주기별(개발·빌드·배포·운영) 보안 위협을 분석하고, 제로트러스트 원칙을 적용한 공급망 보안 아키텍처와 핵심 프레임워크(SLSA, SBOM/VEX, NIST SSDF)의 연계 구축 방안을 제시하시오. (기출·제136회 4교시 4번)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 소프트웨어 기획, 소스 개발, 서드파티 오픈소스 반입, 빌드·패키징, 배포 및 운영에 이르는 전 생애주기에서 발생 가능한 위변조와 악성코드 주입을 차단하는 보안 체계 |
| 목적 | 단일 오픈소스 컴포넌트 오염이나 CI/CD 침해로 인해 수천 개의 다운스트림 고객사로 침해가 일괄 확산되는 공급망 파급 효과 차단 및 전주기 신뢰성 보장 |

## Ⅱ. 소프트웨어 공급망 보안의 핵심 특징 및 공격 표면

| 특징 | 세부 내용 | 주요 공격 표면 및 위협 사례 |
|---|---|---|
| 신뢰의 전이성 악용 | 하위 오픈소스 패키지의 신뢰가 상위 엔터프라이즈 솔루션으로 무검증 전이 | 타이포스쿼팅, 종속성 혼동, 의존성 하이재킹 |
| 빌드 파이프라인 은닉 | 소스코드 저장소가 아닌 CI/CD 러너 메모리나 릴리스 패키징 시점에 악성코드 주입 | SolarWinds 사태, XZ Utils 백도어(CVE-2024-3094) |
| 장기 잠복 사회공학 | 신뢰받는 기여자로 위장하여 수년간 활동 후 메인테이너 권한 탈취 | 오픈소스 1인 관리자 피싱, 프로젝트 지분 인수 |
| 기계 자격증명 남용 | 빌드 자동화를 위해 CI/CD에 주입된 영구 API 토큰(NPM/AWS) 탈취 | Shai-Hulud 자가 증식 웜, Travis CI 토큰 유출 |
| 가시성의 극단적 결여 | 수천 개의 간접 의존성(Transitive Dependencies)으로 인해 사내 소프트웨어 성분 파악 난항 | Log4j 사태(CVE-2021-44228) 시 자산 식별 지연 |

## Ⅲ. 제로트러스트 기반 소프트웨어 공급망 보안 아키텍처

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

| SDLC 생애주기 | 단계별 공급망 통제 | 핵심 구현 기술 및 표준 |
|---|---|---|
| 소스 개발 (Code) | 커밋 서명 강제, 깃허브 브랜치 보호 규칙, 2인 이상 코드 리뷰(PR) 필수 | Git GPG Signing, Branch Protection Rules |
| 의존성 반입 (Dependencies) | 사내 프라이빗 패키지 미러 운영, 라이선스 및 취약점 검증 후 반입 | Nexus, Artifactory, Socket.dev, Snyk SCA |
| 빌드 실행 (Build) | 독립된 임시 컨테이너에서 네트워크가 격리된 밀폐형(Hermetic) 빌드 수행 | Google Cloud Build, GitHub Hosted Runners (SLSA L3) |
| 패키징/증명 (Package) | 빌드 완료 산출물에 대해 자동화된 출처 증명서(Attestation) 및 SBOM 생성 | CycloneDX, SPDX, in-toto, Cosign |
| 배포/운영 (Deploy/Run) | 쿠버네티스 어드미션 컨트롤러에서 서명 및 정책 미충족 컨테이너 배포 차단 | OPA Gatekeeper, Kyverno, VEX 취약점 필터링 |

## Ⅳ. 공급망 보안 프레임워크 비교: SLSA vs NIST SSDF

| 비교 항목 | SLSA (Supply-chain Levels for Software Artifacts) | NIST SSDF (Secure Software Development Framework) |
|---|---|---|
| 주도 기관 | 구글, OpenSSF, 리눅스 재단 | 미국 국립표준기술원 (NIST SP 800-218) |
| 프레임워크 성격 | 기술적·아키텍처적 무결성 체크리스트 (Level 1~3) | 전사적 소프트웨어 보안 개발 수명주기 프로세스 가이드라인 |
| 중점 평가 영역 | 소스 무결성, 빌드 플랫폼 격리, 출처 증명(Provenance) 생성 | 조직 준비, 안전한 소프트웨어 보호, 취약점 대응 전반 |
| 검증 방식 | 기계 판독형 in-toto attestation을 통한 자동화 암호학적 검증 | 감사 체크리스트, 자체 인증(Self-Attestation) 서약서 |
| 규제 연계성 | 클라우드 네이티브 DevSecOps 파이프라인 표준 | 미국 백악관 행정명령(EO 14028) 연방정부 소프트웨어 납품 요건 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 대규모 레거시 프로젝트의 경우 수만 개의 간접 의존성으로 인해 SBOM 생성 시 취약점이 수천 건 도출되어 조치 불가능 | 취약점의 실제 함수 호출 여부(Reachable Path)를 분석하는 VEX(Vulnerability Exploitability eXchange)를 연동하여 실제 위험한 결함만 95% 이상 압축 필터링 |
| 개발자 PC 및 빌드 러너 환경에 정적 배포 토큰이 노출되어 자가 증식 웜(Shai-Hulud 등)에 의한 탈취 위험 | 장기 토큰을 전면 폐기하고 OpenID Connect(OIDC) 기반 단기 자격증명 발급(Sigstore Fulcio / GitHub OIDC) 체계 구축 |
| 오픈소스 프로젝트 소유자가 사망하거나 계정이 하이재킹되어 악성 업데이트가 정식 릴리스되는 공격 | 주요 오픈소스에 대해 릴리스 즉시 사내 도입을 차단하고, 24~48시간의 카나리아 격리(Quarantine) 후 동적 행위 검증 거쳐 반입 |
| 빌드 환경(OS, 컴파일러 버전, 타임스탬프) 차이로 인해 바이너리 바이트 일치성 검증(Reproducible Builds) 난항 | 빌드 환경 전체를 도커 불변 이미지로 고정하고 SOURCE_DATE_EPOCH 표준 타임스탬프를 적용하여 결정론적 컴파일 보장 |

## Ⅵ. 제언

```text
[ 전사 엔드투엔드 공급망 신뢰 체인 구축 로드맵 ]

  [ 1단계: 가시성 확보 ]            [ 2단계: 파이프라인 불변화 ]         [ 3단계: 제로트러스트 집행 ]
+----------------------------+     +-------------------------------+     +-------------------------------+
| • 전 제품 SBOM 자동 추출   | ──> | • SLSA Level 3 격리 빌드 구축 | ──> | • OPA 기반 배포 차단 강제     |
| • 사내 패키지 미러링 구축  |     | • Sigstore 기반 서명 파이프라인|     | • VEX 실시간 취약점 거버넌스  |
+----------------------------+     +-------------------------------+     +-------------------------------+
```

| 추진 영역 | 엔지니어링 실행 과제 | 기대 효과 |
|---|---|---|
| 컴포넌트 거버넌스 | CI 파이프라인 내 CycloneDX SBOM 생성 및 VEX 문서 실시간 게시 자동화 | 신규 취약점(Log4j 등) 발생 시 영향 자산 식별 10분 이내 완료 |
| 빌드 신뢰성 | SLSA 레벨 3 표준을 충족하는 완전 격리형 에펨럴(Ephemeral) 빌드 환경 구축 | 빌드 시점의 악성 백도어 주입(SolarWinds형 공격) 원천 차단 |
| 런타임 제로트러스트 | 배포 게이트웨이에서 Cosign 서명 및 출처 증명서가 없는 아티팩트 실행 전면 거부 | 비인가/변조된 컨테이너 이미지의 프로덕션 배포 100% 방어 |

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 4교시 4번 (소프트웨어 공급망 보안 설명 및 제로트러스트 기반 공급망 보안 아키텍처)
- NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1
- OpenSSF, Supply-chain Levels for Software Artifacts (SLSA) v1.0 Specification
- CISA & NSA, Defending Continuous Integration / Continuous Delivery (CI/CD) Pipelines

## 연결 토픽

- XZ Utils 백도어 (CVE-2024-3094)
- Shai-Hulud npm 웜
- EU CRA (사이버복원력법)
- CrowdStrike 대규모 장애
