---
title: "DevOps"
description: "DevOps의 개념, 특징, 구조, 전통적 SDLC와의 비교, 한계와 방안, 제언"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드

- DevOps
- CI/CD(Continuous Integration/Continuous Delivery), 파이프라인, 관측성(Observability)
- IaC(Infrastructure as Code), DORA 4대 지표, 시프트 레프트(Shift-Left), 플랫폼 엔지니어링, DevSecOps

## Ⅰ. DevOps의 개요

- 핵심 요약 : 개발과 운영의 장벽을 허물어 배포 속도와 서비스 신뢰성을 함께 높이는 엔지니어링 패러다임.
- 개념 : 소프트웨어 개발(Development)과 IT 운영(Operations) 사이의 장벽을 허물고, 조직 문화·협업 프로세스·자동화 도구를 통합해 소프트웨어 납품 속도와 서비스 신뢰성을 높이는 **DevOps** 엔지니어링 패러다임.
- 배경 및 필요성 : 출시 주기 단축(Time-to-Market) 요구와 마이크로서비스 확산으로 배포 빈도가 급증했으나, 개발은 변경 속도를, 운영은 안정성을 우선하는 상충된 목표 때문에 조직이 사일로(Silo)로 나뉘는 문제가 생겼다.
- 주요 목적 : 배포 빈도 향상, 변경 리드타임 단축, 변경 실패율 감소, 평균 복구 시간(MTTR, Mean Time to Repair) 단축.

## Ⅱ. DevOps의 특징 및 장점

- 핵심 요약 : 협업 문화와 **CI/CD** (Continuous Integration/Continuous Delivery)·**IaC** (Infrastructure as Code)·**관측성** (Observability)의 결합으로 출시 속도와 서비스 안정성을 함께 높이는 운영 체계.

1. 교차 기능팀 : 개발·운영·테스트가 공동 책임을 짐 → 인계 지연 축소와 장애 대응 속도 향상.
2. 지속적 통합과 배포 : 빌드·시험·배포를 자동화 → 작은 변경의 잦은 릴리스와 결함의 조기 발견.
3. **IaC** (Infrastructure as Code, 코드로 인프라를 정의하고 관리하는 방식) : 환경을 코드로 재현 → 설정 편차와 수작업 오류 감소.
4. **관측성** (Observability, 메트릭·로그·트레이스로 시스템 내부 상태를 파악하는 능력) : 장애 원인 탐색과 복구 시간 단축.
5. 카나리 배포와 블루·그린 배포 : 변경을 단계적으로 노출하고 즉시 롤백 → 배포 실패의 영향 범위 축소.
6. **시프트 레프트** (Shift-Left, 테스트와 보안을 개발 초기로 앞당기는 것) : 늦은 수정 비용과 출시 병목 완화.

## Ⅲ. DevOps의 구조 (흐름)

- 핵심 요약 : 계획에서 모니터링까지 순환하는 생명주기와, 그 안에서 코드 변경을 운반하는 CI/CD 파이프라인 구조.

```text
[ DevOps 생명주기 순환 ]

[계획 Plan] · [코딩 Code]
      ↓
[빌드 Build] · [시험 Test]
      ↓  CI 구간
[릴리스 Release] · [배포 Deploy]
      ↓  CD 구간
[운영 Operate] · [모니터링 Monitor]
      ↓
피드백 → 다음 계획
```

```text
[ CI/CD 파이프라인 상세 ]

계획·코딩 : 백로그 관리·Git 형상관리·브랜치 전략
      ↓
지속적 통합 : 정적 분석·단위/통합 테스트 자동화·아티팩트 저장
      ↓
지속적 전달·배포 : Helm·ArgoCD 무중단 배포·Terraform 인프라 프로비저닝
      ↓
운영·모니터링 : Prometheus·Grafana·OpenTelemetry 메트릭·로그·트레이스 통합
```

## Ⅳ. 전통적 SDLC와의 비교

- 핵심 요약 : 분리·일괄·수작업 체계에서 통합·소규모·자동화 체계로의 패러다임 전환.

```text
[ 전통적 SDLC ] 개발 ──인수인계──▶ 운영
                  (분리·일괄 릴리스)
[ DevOps ]      개발 ◀──협업·자동화──▶ 운영
                  (통합·소규모 릴리스)
```

| 구분 | 전통적 SDLC (Software Development Life Cycle, 폭포수·분리 운영) | DevOps 엔지니어링 체계 |
| --- | --- | --- |
| 조직 구조 | 개발팀과 운영팀의 기능적 분리 | 교차 기능팀, 플랫폼 엔지니어링 |
| 릴리스 주기 | 분기 또는 반기 단위 대규모 일괄 배포 | 일 단위 또는 시간 단위의 소규모 릴리스 |
| 인프라 관리 | 수작업 콘솔 작업과 서버 수동 설정 | 코드로 관리하는 인프라(IaC), 불변 인프라 |
| 테스트 범위 | 릴리스 직전 일괄 QA(Quality Assurance) | 파이프라인 안의 자동화 테스트와 시프트 레프트 |
| 장애 대응 | 부서 간 책임 전가와 사후 분석 | 카오스 엔지니어링, 자동 롤백 |

## Ⅴ. DevOps의 한계와 방안

- 핵심 요약 : 조직 장벽, 도구 파편화, 공급망 보안 위험을 공동 성과 지표·내부 개발자 플랫폼·DevSecOps로 관리해야 한다.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 조직 사일로 잔존 | 부서별 목표가 상충하면 도구를 도입해도 인계와 책임 분리가 지속 | 제품 중심 교차 기능팀 구성, 비난 없는 회고, DORA(DevOps Research and Assessment) 지표 공동 관리 | 변경 리드타임, 복구 시간 |
| 도구 파편화 | 다수 도구의 설정과 운영 부담이 개발자에게 전가 | 내부 개발자 플랫폼(IDP, Internal Developer Platform)과 표준 셀프서비스 경로 구축 | 환경 준비 시간, 파이프라인 실패율 |
| 보안 검증 병목 | 출시 직전 점검과 외부 의존성 취약점이 배포를 지연 | SAST(Static Application Security Testing)와 SCA(Software Composition Analysis)를 CI에 통합하고 SBOM(Software Bill of Materials) 관리 | 취약점 수정 시간, 미해결 취약점 수 |

## Ⅵ. DevOps에 대한 기술사적 제언

- 핵심 요약 : 보안 시프트 레프트의 의무화와 DORA 4대 지표 기반 성숙도 관리를 병행해야 한다.
- 파이프라인 안에서 SAST, DAST(Dynamic Application Security Testing), SCA를 배포의 게이트 조건으로 자동 실행해 취약점이 운영에 나가는 것을 차단하는 **DevSecOps** 체계를 의무화하는 것이 바람직하다.
- 도구 도입 자체보다 배포 빈도·변경 리드타임·변경 실패율·복구 시간의 추이를 측정해 병목을 찾는 방식이 성숙도 관리에 효과적이다. 측정 결과를 처벌이 아닌 학습의 근거로 쓰는 문화가 함께 있어야 한다.
- 플랫폼 엔지니어링 관점에서 내부 개발자 플랫폼을 구축해 개발자가 인프라 복잡도를 인지하지 않고 비즈니스 로직에 집중하도록 하는 것이 지속 가능한 DevOps 정착의 열쇠다.

## Ⅶ. 결론

- 핵심 요약 : DevOps는 도구가 아닌 문화·프로세스·자동화가 통합된 엔지니어링 체계.
- 조직 재편과 DORA 4대 지표 기반 측정, DevSecOps 전환을 병행하는 것이 지속 가능한 성숙도를 확보하는 선결 조건이다.