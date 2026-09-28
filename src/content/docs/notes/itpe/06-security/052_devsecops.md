---
title: "DevSecOps"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "052. DevSecOps"
  badge:
    text: "기초"
    variant: note
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

안전한 소프트웨어 개발 → 개발·보안·운영 통합 → CI/CD 내재화 보안(DevSecOps)

## 30초 인출

- **본질:** 소프트웨어 개발 및 배포 주기(SDLC) 전반에 보안 통제를 좌측으로 이동(Shift-Left)시켜 자동화된 CI/CD 파이프라인 내에 내재화하는 개발·보안·운영 통합 문화이자 기술 체계
- **메커니즘:** 계획(위협모델링) → 코딩(시크릿스캔) → 빌드(SAST/SCA) → 시험(DAST/IAST) → 배포(IaC보안/이미지서명) → 운영(RASP/CWPP) → 피드백
- 통찰: 단순 정적 도구 도입에 그치지 않고 개발자 경험(DX)을 해치지 않는 배포 게이트웨이 임계치 설계, Policy-as-Code(OPA), SBOM 기반 공급망 투명성 확보가 통합된 엔지니어링 문화 확립 필수

<details><summary>핵심 용어</summary>

- **DevSecOps:** Development, Security, Operations의 합성어로, 보안을 사후 검증이 아닌 개발 초기부터 지속적으로 자동 통합하는 방법론.
- **Shift-Left(시프트 레프트):** 보안 결함 발견 및 조치 시점을 운영/배포 단계에서 기획/개발 초기 단계로 앞당겨 수정 비용을 절감하는 원칙.
- **SAST / DAST:** 정적 애플리케이션 보안 테스팅(소스코드 분석)과 동적 애플리케이션 보안 테스팅(실행 중 블랙박스 진단).
- **SCA(Software Composition Analysis):** 오픈소스 라이브러리의 취약점(CVE) 및 라이선스 준수 여부를 분석하는 도구.
- **Policy-as-Code(PaC):** 보안 및 컴플라이언스 규칙을 코드(예: Rego, OPA)로 정의하여 배포 파이프라인에서 자동으로 강제 집행하는 기법.
- **NIST SSDF(SP 800-218):** 안전한 소프트웨어 개발을 위해 조직, 소프트웨어 보호, 안전한 소프트웨어 생산, 취약점 대응을 제시한 표준 프레임워크.

</details>

---

## 2~4교시 예상문제 (25점)

> CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용 방안에 대하여 설명하고, 파이프라인 병목 현상 및 오탐(False Positive) 극복을 위한 운영 전략을 제시하시오. (기출·제135회 2교시 2번)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 소프트웨어 개발 수명주기(SDLC) 전 과정에 보안을 통합하고, CI/CD 파이프라인의 각 단계에 자동화된 보안 검증 게이트를 구축하여 배포 속도와 보안성을 동시에 달성하는 패러다임 |
| 목적 | 보안 결함의 조기 발견(Shift-Left)을 통한 수정 비용 최소화, 릴리즈 병목 해소, 소프트웨어 공급망 보안 및 컴플라이언스 상시 충족 |

## Ⅱ. DevSecOps의 주요 특징

| 특징 | 세부 내용 | 구현 요소 |
|---|---|---|
| 보안의 조기 착수 (Shift-Left) | 릴리즈 직전 감사가 아닌 개발 초기 코딩 및 빌드 단계에서 취약점 사전 차단 | IDE 린터, Pre-commit Hook, 위협 모델링 |
| 자동화된 보안 게이트 | 수동 검토를 최소화하고 CI/CD 파이프라인 내에서 기준 미달 시 자동 빌드 중단 | Quality Gate, OPA(Open Policy Agent) |
| 공유 책임 모델 (Shared Responsibility) | 보안팀 단독 책임에서 개발·운영·보안 전원이 공동 책임을 지는 엔지니어링 문화 정착 | 보안 챔피언(Security Champion) 육성 |
| 코드형 정책 (Policy-as-Code) | 보안 규정 및 클라우드 인프라 보안 규칙을 코드로 작성하여 형상 관리 및 버전 추적 | Terraform, Checkov, Kyverno, Rego |

## Ⅲ. CI/CD 파이프라인 내 DevSecOps 아키텍처 및 단계별 통제 프로세스

```text
[ 1. Plan & Code ] ── Pre-commit Hook (Gitleaks, TruffleHog) ── IDE 플러그인
       │  (시크릿 하드코딩 탐지, 위협 모델링)
       ▼ Git Push
[ 2. Build ] ──────── SAST (SonarQube, Semgrep) + SCA (Snyk, Dependency-Check)
       │  (소스코드 취약점 정적 분석, 오픈소스 CVE 분석, SBOM 생성)
       ▼ Docker Build
[ 3. Test ] ───────── Container Scan (Trivy) + DAST (OWASP ZAP) + IAST
       │  (컨테이너 이미지 CVE 스캔, 런타임 엔드포인트 모의 침투)
       ▼ Registry Push & Cosign 서명
[ 4. Release/Deploy ]─ IaC Scan (Checkov, tfsec) + Policy Gate (OPA Gatekeeper)
       │  (클라우드 인프라 설정 오류 검증, 쿠버네티스 배포 승인)
       ▼ Production Deploy
[ 5. Operate & Monitor ] ── RASP / CWPP / CSPM + SIEM 피드백 루프
```

| CI/CD 단계 | 통제 활동 | 적용 기술 및 도구 |
|---|---|---|
| 1. Plan & Code | 시크릿 키 누출 차단, 시큐어 코딩 가이드 준수 | GitLeaks, Pre-commit, IDE Linter |
| 2. Build | 소스코드 결함 분석, 서드파티 오픈소스 취약점 및 라이선스 점검 | SonarQube, Snyk, Syft (SBOM 생성) |
| 3. Test | 컨테이너 이미지 레이어 스캔, 구동 중인 앱 동적 취약점 진단 | Trivy, Grype, OWASP ZAP, Contrast IAST |
| 4. Deploy | 인프라 설정 오류(IaC) 점검, 이미지 무결성 전자서명 검증 | Checkov, Cosign, OPA Gatekeeper |
| 5. Operate | 런타임 자가 방어, 클라우드 워크로드 이상 탐지, 취약점 피드백 | RASP, Falco, Datadog, Prometheus |

## Ⅳ. DevSecOps 보안 테스트 도구 비교

| 구분 | SAST (정적 테스트) | DAST (동적 테스트) | IAST (상호작용 테스트) | SCA (소프트웨어 구성 분석) |
|---|---|---|---|---|
| 점검 대상 | 소스코드, 바이트코드 | 실행 중인 웹 애플리케이션 | 런타임 에이전트 + 트래픽 | 오픈소스 의존성 라이브러리 |
| 수행 단계 | 코딩 및 빌드 단계 | 테스트 및 스테이징 단계 | 테스트 및 QA 단계 | 빌드 및 패키징 단계 |
| 장점 | 코드 전체 커버리지, 조기 발견 | 실제 공격자 시각 검증, 오탐 적음 | 높은 정확도, 실행 경로 추적 | 알려진 CVE 및 라이선스 즉시 식별 |
| 단점 | 높은 오탐률, 실행 맥락 미반영 | 소스 위치 파악 불가, 스캔 지연 | 에이전트 설치 부담, 성능 영향 | 제로데이 미공개 취약점 탐지 불가 |
| 대표 도구 | SonarQube, Checkmarx | OWASP ZAP, Burp Suite | Contrast Security, Veracode | Snyk, Black Duck, Trivy |

## Ⅴ. DevSecOps 구축 및 운영의 한계와 방안

| 한계 | 방안 |
|---|---|
| SAST 도구의 높은 오탐(False Positive)과 장시간 소요로 인해 CI/CD 빌드가 지연되고 개발자 반발 초래 | 전체 재검사 대신 Git Diff 기반 증분 분석(Incremental Scan)을 적용하고, 위험도 임계치(Critical/High만 차단) 기반 퀄리티 게이트 세분화 |
| 오픈소스 라이브러리의 깊은 전이적 의존성(Transitive Dependency) 및 컨테이너 베이스 이미지 취약점 폭증 | CycloneDX/SPDX 기반 SBOM 자동 생성 및 의존성 트리 내 미사용 함수 필터링(Reachability Analysis) 도구 도입 |
| 보안 통제가 개발 속도를 저해하는 관료적 승인 절차로 변질되어 파이프라인 우회(Bypass) 발생 | Policy-as-Code(OPA) 기반 자동 승인 규칙 수립 및 개발 부서 내 '보안 챔피언' 육성을 통한 일상적 코드 리뷰 내재화 |

## Ⅵ. 제언

```text
[ 전통적 폭포수 보안 ]                 [ 클라우드 네이티브 DevSecOps ]
개발 완료 후 사후 진단 ──┐             ┌── 전 개발 단계 Shift-Left 자동화
일방적 취약점 조치 요구 ┼─→ [ 릴리즈 지연 ] ─┼── SBOM 및 Policy-as-Code 배포 게이트
배포 직전 롤백 빈번 ───┘             └── RASP/CWPP 연계 런타임 폐루프 피드백
```

| 평가 영역 | 전통적 보안 검증 체계 | 성숙된 DevSecOps 체계 | 향후 발전 방향 |
|---|---|---|---|
| 수정 비용 | 배포 후 발견으로 30~100배 증가 | 코딩 단계 즉시 수정으로 최소화 | 생성형 AI 기반 취약점 자동 패치(Auto-PR) |
| 배포 주기 | 보안 검수로 수주~수개월 지연 | 분/시간 단위 자동 배포 달성 | eBPF 기반 초경량 런타임 무간섭 보안 |
| 공급망 신뢰 | 외부 컴포넌트 무검증 도입 | SLSA 프레임워크 레벨 충족 | 양자 내성 암호 기반 빌드 서명 체계 |

DevSecOps는 단순히 보안 도구를 파이프라인에 추가하는 것을 넘어, 보안을 고속 릴리즈의 필수 조력자로 전환하는 조직 문화의 혁신이며, NIST SSDF 및 SLSA 공급망 보안 표준과 결합하여 완전한 디지털 신뢰성 실현 필수.

## 출제 이력과 검증 출처

- 정보관리기술사 제135회 2교시 2번 (CI/CD 파이프라인에서 DevSecOps 적용방안)
- 정보관리기술사 제127회 2교시 (Shift-Left 기반 DevSecOps 구현 방안)
- NIST SP 800-218: Secure Software Development Framework (SSDF) Version 1.1
- OpenSSF: Supply-chain Levels for Software Artifacts (SLSA) Framework
- OWASP DevSecOps Guideline and Top 10
