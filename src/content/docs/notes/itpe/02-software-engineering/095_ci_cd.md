---
title: "CI/CD(Continuous Integration/Continuous Delivery)"
description: "개발자의 코드 변경을 빈번하게 자동 통합, 테스트하고 검증된 빌드를 운영 환경까지 지속적으로 배포하는 CI/CD 파이프라인의 개념, 핵심 단계, 지속적 제공과 배포 비교 및 DORA 지표"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
    variant: "note"
extra:
  series: "itpe"
  topic: "02-software-engineering"
  sub_topic: "devops"
  order: 95
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어공학 → 빌드·배포·운영 → **CI/CD(Continuous Integration/Continuous Delivery)**

---

## 30초 인출

- 본질: **CI/CD** 는 소프트웨어 개발 생애주기에서 개발자들의 코드 변경 사항을 중앙 저장소에 수시로 자동 병합·테스트(CI)하고, 품질 게이트를 통과한 실행 산출물을 스테이징(CDelivery) 또는 프로덕션(CDeployment) 환경까지 무인 자동 배포하는 데브옵스(DevOps) 핵심 엔지니어링 실천법
- 메커니즘: Git Push 이벤트 감지 → 정적 분석 및 단위/통합 테스트 자동 실행(CI) → 컨테이너 이미지 패키징 및 레지스트리 푸시 → 카나리/블루그린 무중단 배포(CD) → 롤백 및 모니터링 연동
- 통찰: 배포 자동화에만 집중하고 자동화된 테스트 신뢰도와 카나리 롤백 메커니즘을 소홀히 하면 결함의 전파 속도만 가속되므로 브랜치 전략(Trunk-based)과 Quality Gate 및 DORA 4대 핵심 지표 관리를 결합한 전주기 딜리버리 거버넌스가 필수적임

<details>
<summary>핵심 용어</summary>

- **지속적 통합 (CI: Continuous Integration)** : 모든 개발자가 하루에도 여러 번 메인 브랜치에 코드를 통합하고 자동 빌드/테스트를 수행하는 실천법
- **지속적 제공 (CD: Continuous Delivery)** : 통합 테스트를 통과한 코드가 언제든 프로덕션에 배포될 수 있는 릴리스 가능 상태를 유지하되, 최종 배포는 수동 승인하는 방식
- **지속적 배포 (CD: Continuous Deployment)** : 모든 테스트와 품질 게이트를 통과한 빌드를 사람의 개입 없이 실제 운영 환경으로 완전 자동 릴리스하는 방식
- **품질 게이트 (Quality Gate)** : 테스트 커버리지, 코드 스멜, 보안 취약점 기준을 정의하여 미달 시 파이프라인 진행을 차단하는 통제 지점
- **DORA 지표** : DevOps 연구 조직이 정의한 배포 빈도, 변경 리드 타임, 서비스 복구 시간, 변경 실패율의 4대 소프트웨어 전달 성능 지표

</details>

---

## 2~4교시 예상문제 (25점)

> 데브옵스(DevOps) 가치 실현을 위한 CI/CD(지속적 통합/지속적 배포)의 개념과 파이프라인 4단계 프로세스를 설명하고, 지속적 제공(Continuous Delivery)과 지속적 배포(Continuous Deployment)의 비교, 브랜치 전략(Git-Flow vs Trunk-Based) 및 성공적인 운영을 위한 DORA 4대 지표 관리 방안을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 애플리케이션의 개발부터 빌드, 테스트, 패키징, 배포에 이르는 소프트웨어 전달 전 과정을 자동화 파이프라인으로 구축하여 지속적으로 인도하는 엔지니어링 실천 체계 |
| 목적 | "통합 지옥(Integration Hell)" 해소, 릴리스 주기 단축, 배포 위험 최소화, 비즈니스 아이디어의 신속한 시장 출시(Time-to-Market) 달성 |

## Ⅱ. 핵심 특징

작은 단위의 잦은 변경(Small Batch)과 자동화된 피드백 루프를 통해 개발과 운영의 병목 제거.

| 핵심 영역 | 세부 메커니즘 | 실무 적용 방안 |
|---|---|---|
| **빈번한 통합 (Continuous Integration)** | 하루에도 수차례 메인 트렁크(Trunk)로 코드 병합 및 충돌 사전 방지 | 롱리브드 브랜치 지양, PR 단위 자동 빌드/테스트 트리거 |
| **품질 검증 자동화 (Quality Gate)** | 단위, 통합, 보안 취약점, 정적 분석 린트를 파이프라인 단계별 통제 | SonarQube, Snyk 보안 검사, JaCoCo 커버리지 기준 미달 시 빌드 실패 |
| **불변 인프라 산출물 (Immutable Artifact)** | 단 1회 빌드된 컨테이너 이미지를 모든 환경(Dev $\rightarrow$ Stg $\rightarrow$ Prod)에 동일 배포 | Docker Image 태그 기반 환경별 설정(ConfigMap) 분리 주입 |
| **무중단 점진 릴리스 (Zero-downtime)** | 롤링 업데이트, 블루-그린, 카나리(Canary) 배포 기법 연계 | ArgoCD, Spinnaker 연동 GitOps 기반 안전 배포 |

## Ⅲ. 체계·프로세스

CI/CD 통합 파이프라인의 4단계 실행 체계 및 GitOps 배포 흐름도.

```text
[CI/CD 파이프라인 및 GitOps 배포 체계]
[1] 소스 코드 작성            [2] 지속적 통합 (CI)             [3] 패키징 & 레지스트리
  +─────────────────────+       +─────────────────────+       +─────────────────────+
  | 개발자 Git Push     | ────> | GitHub Actions /    | ────> | Docker Image 빌드   |
  | (Trunk-based PR)    |       | Jenkins 파이프라인  |       | 컨테이너 레지스트리 |
  +─────────────────────+       | - 정적 분석 & Lint  |       | (Harbor / ECR 푸시) |
                                | - 단위/통합 테스트  |       +──────────┬──────────+
                                | - SonarQube 게이트  |                  │
                                +─────────────────────+                  ▼
                                                              [4] 지속적 제공 / 배포 (CD)
                                                              +─────────────────────────────────────────+
                                                              | GitOps 배포 엔진 (ArgoCD)                |
                                                              | Manifest Git Repo 감시 및 동기화         |
                                                              +────────────────────┬────────────────────+
                                                                                   │
                                ┌──────────────────────────────────────────────────┴────────────────────┐
                                ▼                                                                       ▼
                 [지속적 제공 (Continuous Delivery)]                     [지속적 배포 (Continuous Deployment)]
                 * 스테이징 배포 ──> [승인 버튼] ──> 프로덕션            * 테스트 통과 즉시 ──> 프로덕션 자동 배포
                 * 카나리 트래픽 5% ──> 검증 후 전면 전환                * 무인 자동 롤백 (SLO 위반 시)
```

- **CI/CD 파이프라인 4단계 프로세스**:
  1. **코드 커밋 및 브랜치 병합(Commit & Merge)** : 개발자가 로컬 테스트 완료 후 작은 단위로 메인 브랜치에 Pull Request 제출.
  2. **자동 빌드 및 테스트(Build & Test Gate)** : CI 서버가 즉시 가상 컨테이너를 가동하여 컴파일, 단위/통합 테스트, 정적 코드 분석 수행.
  3. **산출물 패키징(Artifact Packaging)** : 모든 품질 기준을 통과한 빌드를 불변 컨테이너 이미지로 빌드하고 고유 커밋 해시로 태깅하여 저장소에 등록.
  4. **무중단 배포 및 모니터링(Deploy & Observe)** : ArgoCD 등 배포 엔진이 쿠버네티스 클러스터에 신규 버전을 카나리 방식으로 배포하고 메트릭 이상 유무 감시.

## Ⅳ. 종류·비교

#### 지속적 제공(Continuous Delivery) vs 지속적 배포(Continuous Deployment) 비교

| 비교 항목 | 지속적 제공 (Continuous Delivery) | 지속적 배포 (Continuous Deployment) |
|---|---|---|
| **프로덕션 배포 방식** | **수동 승인 (Manual Trigger: 원클릭 배포)** | **완전 자동 배포 (Fully Automated Trigger)** |
| **파이프라인 범위** | 개발 $\rightarrow$ 스테이징 자동 배포, 프로덕션 배포 대기 | 개발 $\rightarrow$ 스테이징 $\rightarrow$ 프로덕션 전 구간 무인 자동화 |
| **적합한 비즈니스** | 금융, 결제, 공공 등 컴플라이언스 및 승인 결재 필수 도메인 | 웹 서비스, SaaS, B2C 스타트업 등 고속 실험 도메인 |
| **요구 전제조건** | 안정적인 스테이징 환경 및 신뢰할 수 있는 자동화 테스트 | **완벽한 카나리 배포, 자동 롤백, 실시간 관측성 인프라 필수** |

#### 브랜치 전략(Git-Flow vs Trunk-Based) 비교

| 비교 항목 | Git-Flow | Trunk-Based Development |
|---|---|---|
| **브랜치 수명** | 장기 생존 브랜치 다수 (`develop`, `feature`, `release`) | 단기 생존 브랜치 (수 시간~하루 내 Main으로 병합) |
| **통합 주기** | 몇 주 또는 몇 달 단위 릴리스 시점에 통합 | 하루에도 수차례 메인 트렁크(Trunk)로 즉시 통합 |
| **충돌 위험도** | 머지 시점에 대규모 충돌(Big Bang Merge) 빈발 | 지속적인 잦은 병합으로 충돌 극소화 |
| **CI/CD 적합성** | 배포 주기가 길어 고속 CI/CD 구현에 비효율적 | **클라우드 네이티브 고속 지속 배포의 표준 권장 모델** |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 자동화 테스트의 실행 시간이 수십 분 이상 지연되어 개발자의 빠른 피드백 루프 단절 | 테스트 병렬화(Test Sharding), 도커 레이어 캐싱, 영향도 기반 증분 테스트 적용 |
| 완전 자동 배포 시 런타임 잠재 결함이 운영 환경 전체로 일시에 확산되는 대형 장애 위험 | 카나리 배포(Argo Rollouts) 및 에러율 기반 자동 롤백(Prometheus 연동) 파이프라인 구축 |
| 소스코드 및 CI 설정 파일(YAML)에 API 키, DB 비밀번호 등 시크릿(Secret) 정보 유출 위험 | HashiCorp Vault, AWS Secrets Manager 등 전용 비밀정보 관리소 연동 및 Git 시크릿 스캐너 도입 |

## Ⅵ. 제언

CI/CD의 궁극적 목표는 배포 속도와 안정성의 동시 달성이므로, DORA(DevOps Research and Assessment) 4대 핵심 지표를 조직의 KPI로 설정하고 지속적으로 파이프라인 병목을 개선할 필요가 있음.

```text
[개발 리드타임 단축] ──> [배포 빈도 극대화] ──> [카나리 롤백 신뢰성] ──> [DORA 엘리트 등급 달성]
 (Trunk-based PR)          (하루 수십 회 배포)      (MTTR 10분 이내 복구)        (글로벌 고성과 조직)
```

| DORA 4대 핵심 지표 | 설명 | 고성과 조직(Elite) 기준 |
|---|---|---|
| **배포 빈도 (Deployment Frequency)** | 운영 환경에 코드가 성공적으로 릴리스되는 빈도 | 온디맨드 (하루에 수차례 이상 배포) |
| **변경 리드 타임 (Lead Time for Changes)** | 커밋 생성 시점부터 운영 환경 배포까지 소요된 시간 | 1시간 이내 |
| **서비스 복구 시간 (Time to Restore Service)** | 운영 장애 발생 시 정상 상태로 복구되는 데 걸리는 시간 (MTTR) | 1시간 이내 |
| **변경 실패율 (Change Failure Rate)** | 배포 후 롤백, 핫픽스, 패치가 필요했던 배포의 비율 | 0~15% 이하 유지 |

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 2교시: DevOps의 핵심인 CI/CD 파이프라인 구축 단계 및 지속적 제공과 지속적 배포의 비교
- 제121회 정보관리기술사 1교시: Git 브랜치 전략 중 Trunk-Based Development의 개념 및 장점
- Nicole Forsgren, Jez Humble, Gene Kim, Accelerate: The Science of Lean Software and DevOps
- Jez Humble, David Farley, Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation
- Martin Fowler, Continuous Integration

## 연결 토픽

- [DevOps](./002_devops.md)
- [무중단 배포](./007_zero_downtime_deployment.md)
- [테스트 자동화](./091_test_automation.md)
- [OpenTelemetry](./096_opentelemetry.md)
