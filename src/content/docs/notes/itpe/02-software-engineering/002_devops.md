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

## Ⅱ. DevOps의 특징

- 핵심 요약 : 문화·프로세스·도구의 통합과 자동화 파이프라인, 코드 기반 인프라, 관측성 확보가 결합된 운영 체계.

1. 개발·운영·테스트를 아우르는 크로스 펑셔널 팀(Cross-functional Team) 중심 조직 운영.
2. 빌드부터 배포까지 자동화된 CI/CD(Continuous Integration/Continuous Delivery) 파이프라인.
3. IaC(Infrastructure as Code)와 불변 인프라(Immutable Infrastructure) 기반 환경 관리.
4. 메트릭·로그·트레이스로 구성되는 관측성(Observability) 통합.
5. 카나리, 블루/그린 등 무중단 배포 전략과 자동 롤백.
6. 테스트·보안의 조기 이동인 시프트 레프트(Shift-Left) 적용.

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

## Ⅴ. DevOps의 장점과 한계

- 핵심 요약 : 납품 속도·신뢰성·회복력 향상의 장점, 조직·툴체인·보안 측면의 성숙도 한계.
- 장점
  1. 배포 빈도 향상과 변경 리드타임 단축을 통한 Time-to-Market 경쟁력 확보.
  2. 자동화 테스트와 관측성 기반의 조기 결함 발견 및 신속 복구.
  3. 개발과 운영의 공동 책임 문화를 통한 품질·안정성 동시 확보.
- 한계점 1 : 조직적 사일로(Silo) 잔존 및 이름뿐인 DevOps 변질
  - 한계점 : 상충되는 KPI와 조직 장벽 미해소 상태에서 기존 인프라팀에 도구만 덧씌워 DevOps팀으로 명칭만 변경하는 안티패턴 발생.
  - 해결 방안 : 제품 중심의 교차 기능팀(Cross-Functional Stream-Aligned Team)으로 조직 재편, DORA(DevOps Research and Assessment) 4대 핵심 지표의 통합 성과 지표 도입, 비난 없는 회고(Blameless Post-Mortem) 문화 정착.
- 한계점 2 : 툴체인 파편화 및 개발자 인지 부하(Cognitive Load) 가중
  - 한계점 : Git, Jenkins, ArgoCD, Terraform, Kubernetes, SonarQube 등 이기종 도구의 파편화로 인프라 관리 스크립트 난립 및 애플리케이션 개발자 인지 부하 극대화.
  - 해결 방안 : 플랫폼 엔지니어링(Platform Engineering) 기반 내부 개발자 플랫폼(IDP, Internal Developer Platform) 구축, 셀프서비스 황금 경로(Golden Path) 템플릿 및 파이프라인-애즈-코드(Pipeline as Code) 표준 확립.
- 한계점 3 : 보안 검증의 병목화 및 소프트웨어 공급망 취약점
  - 한계점 : 전통적 보안 점검의 릴리스 직전 병목 작용, 서드파티 오픈소스 의존성 오염에 따른 공급망 침해(Supply Chain Attack) 위험 상존.
  - 해결 방안 : DevSecOps 체계 전환, SAST(Static Application Security Testing), DAST(Dynamic Application Security Testing), SCA(Software Composition Analysis)의 CI(Continuous Integration) 파이프라인 시프트-레프트(Shift-Left) 통합, SBOM(Software Bill of Materials) 자동 생성 및 SLSA(Supply-chain Levels for Software Artifacts) 프레임워크 준수.

## Ⅵ. DevOps에 대한 기술사적 제언

- 핵심 요약 : 보안 시프트 레프트 의무화와 DORA 지표 기반 성숙도 관리의 병행.
- DevSecOps 및 보안 시프트 레프트(Shift-Left) 의무화 : 파이프라인 내 SAST, DAST, SCA를 게이트웨이 조건으로 자동화하여 취약점 배포 사고 차단.
- 조직 문화와 메트릭 기반의 성숙도 관리 : 단순 툴 도입 지양, DORA 4대 지표(배포 빈도, 변경 리드타임, 변경 실패율, 복구 시간)의 측정을 통한 병목 제거 및 학습 문화 형성.

## Ⅶ. 결론

- 핵심 요약 : DevOps는 도구가 아닌 문화·프로세스·자동화의 통합 체계.
- 요약 : 개발과 운영의 통합과 파이프라인 자동화를 통해 배포 속도와 서비스 신뢰성의 동시 달성을 지향하는 체계.
- 시사점 : 조직 재편과 DORA 지표 기반 측정, DevSecOps 전환의 병행이 지속 가능한 성숙도 확보의 선결 조건.
