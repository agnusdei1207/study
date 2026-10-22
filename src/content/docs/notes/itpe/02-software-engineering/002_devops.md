---
title: "DevOps"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- DevOps, CI/CD(Continuous Integration/Continuous Delivery), 파이프라인, 관측성(Observability)
- IaC(Infrastructure as Code), DORA 4대 지표, 시프트 레프트(Shift-Left), 플랫폼 엔지니어링, DevSecOps

## Ⅰ. DevOps의 개요

- 핵심 요약 : 개발과 운영의 장벽을 허물어 납품 속도와 서비스 신뢰성을 동시에 극대화하는 엔지니어링 패러다임.
- 개념 : 소프트웨어 개발(Development)과 IT(Information Technology) 운영(Operations) 간의 장벽을 허물고, 조직 문화·협업 프로세스·자동화 도구체계를 통합하여 소프트웨어 납품 속도와 서비스 신뢰성을 극대화하는 엔지니어링 패러다임.
- 배경 및 필요성 : 비즈니스 출시 주기 단축(Time-to-Market) 요구, 마이크로서비스 확산에 따른 배포 빈도 급증, 개발과 운영의 상충된 KPI(Key Performance Indicator, 신규 기능 출시 대비 시스템 안정성)로 인한 사일로(Silo) 문제 해소 필요.
- 주요 목적 : 배포 빈도(Deployment Frequency) 향상, 변경 리드타임(Lead Time for Changes) 단축, 변경 실패율(Change Failure Rate) 감소, 평균 복구 시간 MTTR(Mean Time to Repair) 단축.

## Ⅱ. DevOps의 특징 및 장점

- 핵심 요약 : **협업 문화**와 **CI/CD**·**IaC**·관측성의 결합으로 출시 속도와 서비스 안정성을 함께 높이는 운영 체계.

1. **교차 기능팀** : 개발·운영·테스트의 공동 책임 → 인계 지연 축소와 장애 대응 속도 향상.
2. **CI/CD(Continuous Integration/Continuous Delivery)** : 빌드·시험·배포 자동화 → 작은 변경의 잦은 릴리스와 결함 조기 발견.
3. **IaC(Infrastructure as Code)**와 불변 인프라 : 환경을 코드로 재현 → 설정 편차와 수작업 오류 감소.
4. **관측성(Observability)** : 메트릭·로그·트레이스 연계 → 장애 원인 탐색과 복구 시간 단축.
5. 카나리·블루/그린 배포 : 변경을 단계적으로 노출하고 롤백 → 배포 실패의 영향 범위 축소.
6. **시프트 레프트(Shift-Left)** : 테스트·보안을 개발 초기에 통합 → 늦은 수정 비용과 출시 병목 완화.

## Ⅲ. DevOps의 구조 (흐름)

- 핵심 요약 : Plan부터 Monitor까지 순환하는 무한 루프 생명주기와 CI/CD 파이프라인.
- DevOps 무한 루프 생명주기.

```text
   [Plan] → [Code] → [Build] → [Test]
      ▲                           │
      │       CI/CD Pipeline      ▼
   [Monitor] ← [Operate] ← [Deploy] ← [Release]
```

- 계획 및 코딩(Plan & Code) : Jira, GitHub 기반 애자일 백로그 관리, Git Flow 기반 형상관리 및 브랜치 전략.
- 지속적 통합(Continuous Integration) : SonarQube 정적 코드 분석, 단위/통합 테스트 자동화, 아티팩트 레포지토리(Nexus/Artifactory) 빌드.
- 지속적 전달/배포(Continuous Delivery/Deployment) : Helm, ArgoCD, Spinnaker 기반 무중단 배포(Canary, Blue/Green), IaC 도구(Terraform) 기반 인프라 프로비저닝.
- 운영 및 모니터링(Operate & Monitor) : Prometheus, Grafana, OpenTelemetry 기반 메트릭·로그·트레이스 3대 관측성(Observability) 통합.

## Ⅳ. 전통적 SDLC와의 비교

- 핵심 요약 : 분리·일괄·수작업 체계에서 통합·소규모·자동화 체계로의 패러다임 전환.
- 두 체계의 협업 구조 대조.

```text
[ 전통적 SDLC ]  개발 ──인수인계──▶ 운영   (분리·일괄 릴리스)
[ DevOps ]       개발 ◀──협업·자동화──▶ 운영  (통합·마이크로 릴리스)
```

| 구분 | 전통적 SDLC(Software Development Life Cycle, 폭포수/분리 운영) | DevOps 엔지니어링 체계 |
|---|---|---|
| 조직 구조 | Dev팀과 Ops팀의 물리적·기능적 분리 | 크로스 펑셔널 팀(Cross-functional), 플랫폼 엔지니어링 |
| 릴리스 주기 | 분기 또는 반기 단위 대규모 일괄 배포 | 일단위 또는 시간단위 마이크로 릴리스 |
| 인프라 관리 | 수작업 콘솔 작업, 물리/가상 서버 수동 설정 | 코드로서의 인프라(IaC), 불변 인프라(Immutable Infrastructure) |
| 테스트 범위 | 릴리스 직전 일괄 QA(Quality Assurance) 및 인수 테스트 | 파이프라인 내 시프트 레프트(Shift-Left) 자동화 테스트 |
| 장애 대응 | 장애 발생 시 부서 간 책임 전가 및 사후 분석 | 카오스 엔지니어링(Chaos Engineering), 무중단 자동 롤백 |

## Ⅴ. DevOps의 한계와 방안

- 핵심 요약 : 조직 장벽·도구 파편화·공급망 위험을 **공동 성과 지표**, **내부 개발자 플랫폼**, **DevSecOps**로 관리.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 조직 사일로 잔존 | 부서별 KPI가 상충하면 도구 도입 후에도 인계·책임 분리 지속 | 제품 중심 교차 기능팀, 비난 없는 회고, **DORA(DevOps Research and Assessment)** 지표 공동 관리 | 변경 리드타임, 복구 시간 |
| 도구 파편화 | 다수 도구의 설정·운영 부담이 개발자 인지 부하로 전가 | **내부 개발자 플랫폼(IDP, Internal Developer Platform)**과 표준 셀프서비스 경로 구축 | 환경 준비 시간, 파이프라인 실패율 |
| 보안 검증 병목 | 출시 직전 점검과 외부 의존성 취약점으로 배포 지연·공급망 위험 | **SAST(Static Application Security Testing)**·**SCA(Software Composition Analysis)**를 CI에 통합하고 **SBOM(Software Bill of Materials)** 관리 | 취약점 수정 시간, 미해결 취약점 |

## Ⅵ. DevOps에 대한 기술사적 제언

- 핵심 요약 : 보안 시프트 레프트 의무화와 DORA 지표 기반 성숙도 관리의 병행.
- DevSecOps 및 보안 시프트 레프트(Shift-Left) 의무화 : 파이프라인 내 SAST, DAST, SCA를 게이트웨이 조건으로 자동화하여 취약점 배포 사고 차단.
- 조직 문화와 메트릭 기반의 성숙도 관리 : 단순 툴 도입 지양, DORA 4대 지표(배포 빈도, 변경 리드타임, 변경 실패율, 복구 시간)의 측정을 통한 병목 제거 및 학습 문화 형성.

## Ⅶ. 결론

- 핵심 요약 : DevOps는 도구가 아닌 문화·프로세스·자동화의 통합 체계.
- 요약 : 개발과 운영의 통합과 파이프라인 자동화를 통해 배포 속도와 서비스 신뢰성의 동시 달성을 지향하는 체계.
- 시사점 : 조직 재편과 DORA 지표 기반 측정, DevSecOps 전환의 병행이 지속 가능한 성숙도 확보의 선결 조건.
