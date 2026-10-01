---
title: "DevOps"
author: "Antigravity"
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

## Ⅰ. DevOps의 개요

- **개념** : 소프트웨어 개발(Development)과 IT 운영(Operations) 간의 장벽을 허물고, 조직 문화·협업 프로세스·자동화 도구체계를 통합하여 소프트웨어 납품 속도와 서비스 신뢰성을 극대화하는 엔지니어링 패러다임.
- **배경 및 필요성** : 비즈니스 출시 주기 단축(Time-to-Market), 마이크로서비스 확산으로 인한 배포 빈도 급증, 개발과 운영의 상충된 KPI(신규 기능 출시 vs 시스템 안정성)로 발생하는 사일로(Silo) 문제 해결.
- **핵심 목표** : 배포 빈도 향상(Deployment Frequency), 변경 리드타임 단축(Lead Time for Changes), 변경 실패율 감소(Change Failure Rate), 평균 복구 시간 단축(MTTR).

## Ⅱ. DevOps의 무한 루프 생명주기 및 핵심 파이프라인

```text
   [ Plan ] ──> [ Code ] ──> [ Build ] ──> [ Test ]
      ▲                                       │
      │              CI/CD Pipeline           ▼
   [ Monitor ] <── [ Operate ] <── [ Deploy ] <── [ Release ]
```

- **계획 및 코딩(Plan & Code)** : Jira/GitHub를 통한 애자일 백로그 관리, Git Flow 기반 형상관리 및 브랜치 전략.
- **지속적 통합(Continuous Integration)** : SonarQube 정적 코드 분석, 단위/통합 테스트 자동화, 아티팩트 레포지토리(Nexus/Artifactory) 빌드.
- **지속적 전달/배포(Continuous Delivery/Deployment)** : Helm, ArgoCD, Spinnaker를 활용한 무중단 배포(Canary, Blue/Green), IaC(Terraform) 기반 인프라 프로비저닝.
- **운영 및 모니터링(Operate & Monitor)** : Prometheus, Grafana, OpenTelemetry를 활용한 메트릭·로그·트레이스 3대 관측성(Observability) 통합.

## Ⅲ. 기존 SDLC와 DevOps의 패러다임 비교

| 구분 | 전통적 SDLC (폭포수/분리 운영) | DevOps 엔지니어링 체계 |
|---|---|---|
| 조직 구조 | Dev팀과 Ops팀의 물리적·기능적 분리 | 크로스 펑셔널 팀(Cross-functional), 플랫폼 엔지니어링 |
| 릴리스 주기 | 분기 또는 반기 단위 대규모 일괄 배포 | 일단위 또는 시간단위 마이크로 릴리스 |
| 인프라 관리 | 수작업 콘솔 작업, 물리/가상 서버 수동 설정 | 코드로서의 인프라(IaC), 불변 인프라(Immutable Infrastructure) |
| 테스트 범위 | 릴리스 직전 일괄 QA 및 인수 테스트 | 파이프라인 내 시프트 레프트(Shift-Left) 자동화 테스트 |
| 장애 대응 | 장애 발생 시 부서 간 책임 전가 및 사후 분석 | 카오스 엔지니어링(Chaos Engineering), 무중단 자동 롤백 |

## Ⅳ. 성공적인 DevOps 정착을 위한 기술사적 제언

- **DevSecOps 및 보안 시프트 레프트(Shift-Left) 의무화** : 빠른 배포 속도로 인해 취약점이 배포되는 사고를 막기 위해 파이프라인 내 SAST, DAST, SCA(오픈소스 취약점 점검)를 게이트웨이 조건으로 자동화.
- **조직 문화와 메트릭 기반의 성숙도 관리** : 단순한 툴 도입에 그치지 않고 DORA 4대 지표(배포 주기, 리드타임, 변경 실패율, 복구 시간)를 측정하여 지속적인 병목 제거 및 학습 문화 형성 필요.
