---
sidebar:
  order: 57
  label: "057. DevSecOps"
  badge:
    text: "기출 · 70%"
    variant: note
title: "DevSecOps"
date: "2026-09-07T10:00:00+09:00"
tags:
  - "notes-software"
weight: 57
extra:
  question_no: "057"
  source_status: "기출"
  source_history: "128회, 134회, 135회"
  priority: 70
  priority_note: "128•134•135회 반복, 보안 내재화 핵심"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **DevSecOps**: 개발(Dev), 보안(Sec), 운영(Ops)의 통합으로 소프트웨어 생애주기 전반에 걸쳐 보안을 기본 내재화(Security by Design)하는 공학 체계.
- **Shift-Left Security**: 배포 직전 사후에 보안을 점검하던 방식에서 벗어나, 기획/코딩/빌드 초기 단계로 보안 검증을 전진 배치하는 패러다임.

</details>

- 정의/개념: 기획부터 운영까지 파이프라인 전 단계에 보안을 내재화하는 **시프트 레프트(Shift-Left) 및 자동 보안 게이트(SAST/DAST/SCA)** 통합 체계
- 배경/필요성: 배포 직전 또는 사후 보안 점검에 따른 **취약점 조기 발견 실패, 아키텍처 재설계 비용 폭증 및 배포 승인 지연 병목 한계**

#### 한줄 요약
- 코딩 단계부터 파이프라인 전체에 보안 검증을 내재화하여 배포 병목과 보안 위협을 제거한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **SAST / DAST / SCA**: 정적 코드 분석(SAST), 동적 모의 침투(DAST), 오픈소스 라이브러리 취약점 분석(SCA)의 3대 보안 검증 체계.
- **Security Gate(보안 게이트)**: CVSS 기준 Critical/High 취약점 발견 시 CI/CD 빌드 및 배포를 자동으로 차단하는 무관용 품질 관문.

</details>

- 보안 검증을 개발 초기로 전진 배치하는 **Shift-Left Security** 원칙
- **SAST, DAST, SCA 및 컨테이너 이미지 스캔** 기반의 다계층 자동화 보안 검사
- 보안 정책을 코드로 정의하고 위반 시 빌드를 차단하는 **Policy as Code 및 자동 보안 게이트**

#### 한줄 요약
- 보안을 앞당기면 수정 비용은 줄지만 개발 흐름이 게이트에서 멈출 위험이 생기므로, 내재화의 성패는 도구 성능보다 오탐 관리에 달린다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **SBOM(Software Bill of Materials)**: 애플리케이션에 포함된 모든 오픈소스 컴포넌트, 버전, 라이선스 목록을 기록한 소프트웨어 자재명세서.

</details>

```text
[DevSecOps 보안 내재화 체계]
  │
  ├─ [Code 단계] (시큐어 코딩·Secret 유출 차단)
  │
  ├─ [Build 단계] (SAST 정적분석·SCA 오픈소스 취약점)
  │
  ├─ [Package 단계] (Trivy 컨테이너 이미지 CVE 검증)
  │
  ├─ [Deploy 단계] (Policy as Code·보안 게이트 집행)
  │
  └─ [Operate 단계] (DAST 동적분석·RASP 런타임 방어)
```
- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| Code | **SonarLint·Gitleaks**로 시큐어 코딩과 Secret 차단 |
| Build | **SAST·SCA**로 코드 취약점과 SBOM 분석 |
| Package | **Trivy**로 컨테이너 이미지 CVE 검증 |
| Deploy | **Policy as Code**로 비인가 자원 차단 |
| Operate | **DAST·RASP**로 런타임 위협 탐지·차단 |

#### 한줄 요약
- 보안 검사는 커밋·CI·CD·운영 네 지점에 나뉘어 배치되며 각 지점이 잡을 수 있는 결함의 종류가 다르므로, 어느 하나가 나머지를 대신하지 못한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **Fail-Secure**: 보안 검증 실패 시 파이프라인을 즉각 차단(Fail-Close)하여 취약한 코드가 운영 환경으로 단 1줄도 유입되지 않도록 방어하는 원칙.

</details>

```text
[DevSecOps 보안 게이트 흐름] (진행 ①→⑥, CVSS 심각도·라이선스 판정에서 갈림)
  │
  ├─ [커밋 단계] (① Pre-commit이 Secret 스캔 통과 후 Git 코드 커밋)
  │
  ├─ [CI 단계] (② SonarQube(SAST) 소스 분석 & Snyk(SCA) 오픈소스 CVE 스캔 실행)
  │
  ├─ [패키징 단계] (③ Docker 빌드 후 Trivy가 컨테이너 이미지 스캔 수행)
  │
  ├─ [보안 게이트 판정] (④ Critical 취약점(CVSS 9.0 이상)·미승인 라이선스(GPL 등) 발견 시 Fail-Secure로 즉시 차단)
  │
  ├─ [CD 단계] (⑤ 통과 시 ArgoCD가 K8s 클러스터에 배포 실행, OPA Gatekeeper로 정책 검증)
  │
  └─ [Ops 단계] (⑥ OWASP ZAP(DAST) 동적 침투 및 Falco 런타임 감시, 이상이면 보안 이슈 리포트와 함께 개발자 피드백)
```

분기 결과: 보안 게이트에서 갈리므로, 미승인·심각도 발견 갈래는 빌드를 즉각 차단해 취약 코드의 운영 유입 비용을 막는 대신, 오탐이 반복되면 개발 흐름이 멈추는 대기 비용이 함께 커진다

#### 한줄 요약
- 커밋·CI·CD·운영 네 지점은 각각 다른 결함을 잡으므로, 앞 지점에서 막을수록 수정은 싸지지만 오탐으로 개발을 멈추는 비용은 함께 커진다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **SAST vs DAST vs IAST vs RASP**: 정적 코드 분석(화이트박스), 외부 동적 공격(블랙박스), 상호작용 분석(에이전트), 런타임 자가보호(앱 내부 방어).

</details>

| 보안 검증 기술 | 분석 대상 및 방식 | 장점 | 단점 |
|:---|:---|:---|:---|
| SAST (정적 분석) | **소스 코드 원문 (Whitebox)** | 컴파일 전 조기 결함 발견 (Shift-Left) | 오탐(False Positive) 다소 높음 |
| SCA (오픈소스 분석) | **의존성 라이브러리 및 SBOM** | 알려진 오픈소스 CVE 취약점 즉시 식별 | 제로데이 미공개 취약점 탐지 불가 |
| DAST (동적 분석) | **실행 중인 애플리케이션 (Blackbox)** | 인증/세션 등 실제 런타임 취약점 검증 | 코드 상의 취약점 정확한 라인 미제공 |
| RASP (런타임 자가보호) | **JVM/CLR 내부 에이전트 인터셉트** | SQL Injection 등 실제 공격 실시간 차단 | 런타임 애플리케이션 성능 오버헤드 |

#### 한줄 요약
- SAST/SCA는 개발/빌드 단계 조기 탐지, DAST/RASP는 배포/운영 단계 실시간 방어에 적합하다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **Security Champion**: 개발팀 내부에 지정된 보안 멘토로서, 팀원들의 시큐어 코딩을 지원하고 보안팀과의 소통 가교 역할을 하는 인재.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| SAST 도구의 과도한 오탐(False Positive)으로 빌드 지연 | **취약점 룰셋 커스터마이징 및 정기 오탐 제외(Exclusion) 등록** | 개발자 신뢰도 확보 및 빌드 병목 해소 |
| 오픈소스 라이브러리 취약점(CVE) 폭증 | **Snyk / Dependabot 기반 취약 라이브러리 자동 PR 및 패치** | CVE 노출 시간 극소화 및 패치 자동화 |
| 개발자의 보안 도구 우회 및 무력화 시도 | **보안 챔피언(Security Champion) 제도 및 Git 보호 브랜치 강제** | 팀 내 보안 문화 내재화 및 비인가 배포 차단 |
| 컨테이너 내부 루트(Root) 권한 실행 취약점 | **Kyverno Policy as Code로 `runAsNonRoot: true` 강제** | 컨테이너 탈옥(Breakout) 공격 원천 방어 |

#### 한줄 요약
- 보안 게이트를 앞당기면 수정 비용은 줄지만 오탐이 파이프라인을 멈추는 비용이 새로 생기므로, 룰셋을 정제해 차단 기준을 좁히고 보안 챔피언에게 예외 판단을 맡겨 속도를 되산다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **소프트웨어 공급망 보안(Software Supply Chain Security)**: 오픈소스 라이브러리, 빌드 파이프라인, 컨테이너 레지스트리 등 소프트웨어 생성부터 배포 전반의 무결성을 보장하고 위변조를 방지하는 체계(예: SLSA 표준).
- **런타임 애플리케이션 자가 보호(Runtime Application Self-Protection, RASP)**: 애플리케이션 런타임 엔진 내부에 상주하여 악의적인 페이로드 실행을 실시간 탐지하고 즉시 차단하는 보안 기술.
- **공통 취약점 및 노출(Common Vulnerabilities and Exposures, CVE)**: 널리 알려진 소프트웨어 및 라이브러리의 보안 결함에 표준화된 고유 번호를 부여하여 관리하는 공개 보안 데이터베이스.

</details>

- **차세대 발전 전망**: SLSA 프레임워크 기반의 **소프트웨어 공급망 보안** 체계 및 eBPF 커널 레벨 실시간 위협 탐지와 **런타임 애플리케이션 자가 보호(RASP)** 기술이 통합된 지능형 보안 플랫폼으로 진화하는 추세.
- **실무 공학적 통찰**: 보안 도구의 높은 오탐률(False Positive)로 인한 개발 병목을 차단하기 위해, **보안 챔피언(Security Champion)** 제도를 운영하고 **CVE** 위험도(CVSS)에 따른 유연하고 실효성 있는 품질 게이트 거버넌스 수립 필요.

#### 한줄 요약
- DevSecOps는 공급망 무결성(SLSA) 및 eBPF 런타임 방어와 융합되어 보안을 가속하되, 오탐 튜닝과 보안 챔피언 중심의 팀 거버넌스가 안착의 핵심이다.
