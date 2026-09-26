---
title: "DevOps"
author: "Codex"
date: "2026-09-27T00:24:59+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GPT-6"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어 공학 → 빌드·배포·DevOps → **DevOps**

## 30초 인출

- 본질: **DevOps**는 개발과 운영이 함께 소프트웨어를 만들고 운영하며 지속적으로 전달하는 협업 방식
- 메커니즘: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor 무한 루프 피드백
- 효과: 리드타임 단축 · 배포 빈도 극대화 · 장애 복구 시간(MTTR) 단축 · 고객 가치 조기 실현

<details>
<summary>핵심 용어</summary>

- **DevOps**: 소프트웨어 개발과 IT 운영 간의 소통, 협업, 통합을 강조하는 조직 문화이자 방법론
- **CI/CD(Continuous Integration/Continuous Delivery)**: 코드 통합, 테스트, 빌드, 배포 전 과정을 자동화하는 파이프라인
- **IaC(Infrastructure as Code)**: 인프라 구성을 코드로 정의·버전 관리하여 프로비저닝을 자동화하는 기술
- **CALMS**: Culture(문화), Automation(자동화), Lean(린), Measurement(측정), Sharing(공유)의 DevOps 성공 프레임워크
- **DORA(DevOps Research and Assessment)**: 소프트웨어 전달·운영 성과를 조사하고 측정 지침을 제공하는 연구 조직
- **SRE(Site Reliability Engineering)**: 소프트웨어 공학적 접근법을 적용해 시스템 신뢰성과 운영 가용성을 관리하는 실천 모델

</details>

---

## 1교시 예상문제 (10점)

> DevOps의 개념과 목적, 지속적 전달의 핵심 메커니즘을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. DevOps 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **DevOps** 는 개발과 운영이 협력해 변경을 지속적으로 전달·운영하는 방식 |
| 목적 | 변경을 더 빠르고 안전하게 전달하고 운영 피드백을 개발에 반영 |

### Ⅱ. 지속 전달과 피드백

```text
계획·코드
    ↓
빌드·테스트
    ↓
릴리스·배포
    ↓
운영·관측

운영 피드백 → 다음 계획
```

**실천 기반**

- **CALMS 실천**: 문화·자동화·린·측정·공유의 결합, DORA 지표로 전달 성능 점검
- SRE 연계: **Error Budget(에러 예산)**을 통한 혁신 속도와 서비스 신뢰성의 정량적 통제
- 한 줄 제언: 배포 속도와 안정성 지표를 함께 관찰하고 팀이 후속 개선을 결정할 수 있게 공유
---

## 2~4교시 예상문제 (25점)

> DevOps의 개념과 등장 배경을 설명하고, 개발·운영 협업과 지속적 전달의 핵심 활동, 도입 시 조직·기술 측면의 고려사항을 제시하시오. (25점, 예상)

---

## 2~4교시 25점 답안

## Ⅰ. 개발과 운영 장벽을 극복하는 DevOps의 개요

> **DevOps**의 핵심은 개발·운영 협업과 배포·운영 피드백의 지속적 연결.

| 구분 | 핵심 |
|---|---|
| 정의 | **DevOps** 는 개발과 운영이 협력해 변경을 지속적으로 전달·운영하는 방식 |
| 목적 | 변경을 더 빠르고 안전하게 전달하고 운영 피드백을 개발에 반영 |

## Ⅱ. CALMS 실천과 전달 파이프라인

> 도구 자동화와 함께 개발·운영 협업, 측정, 공유가 작동해야 하는 운영 방식.

```text
계획·코드
    ↓
빌드·테스트
    ↓
릴리스·배포
    ↓
운영·관측

운영 피드백 → 다음 계획
```

- 개발 영역(Plan~Test)은 **지속적 통합(CI)**, 운영 영역(Release~Monitor)은 **지속적 배포(CD)**·**SRE** 관측성이 담당하며 Monitor 결과가 다음 Plan으로 환류됨

| 구성요소 | 핵심 기술 및 프레임워크 | 달성 목표 |
|---|---|---|
| **Culture** | Blameless Postmortem, 원팀(One-team) | 심리적 안전감 확보, 책임 전가 방지 |
| **Automation** | Jenkins, GitHub Actions, ArgoCD, Terraform(**IaC**) | 수작업 휴먼 에러 원천 차단 |
| **Lean** | Wip(재공) 제한, 스몰 배치(Small Batch) | 배포 단위 축소로 변경 위험 통제 |
| **Measurement** | DORA의 현행 전달 성능 지표(변경 리드타임, 배포 빈도, 배포 실패 복구시간, 변경 실패율, 배포 재작업률) | 처리량·불안정성에 대한 개선 근거 |
| **Sharing** | 내부 지식 포털, 엔지니어링 커뮤니티 | 성공/실패 사례 전사 전파 |

## Ⅲ. 전통적 운영 모델과 DevOps 비교

> 작은 변경의 잦은 배포와 빠른 관측·복구를 통해 변경 위험을 낮추는 접근.

| 비교 항목 | 전통적 분리 모델 (Waterfall/Silo) | DevOps 협업 모델 |
|---|---|---|
| **조직 구조** | 개발팀과 운영팀의 엄격한 분리 | 크로스 펑셔널 팀(Cross-functional Team), SRE |
| **배포 주기** | 분기·월 단위 대규모 빅뱅 배포 | 일 단위 다회 지속 배포(Micro Batch) |
| **책임 소재** | "개발은 기능 개발, 운영은 가용성 유지" | "You build it, you run it" 전 주기 공동 책임 |
| **인프라 관리** | 엔지니어 수작업 GUI/CLI 구성 | Git 기반 선언적 **IaC** 및 GitOps |
| **장애 대응** | 장애 발생 시 원인 규명 및 문책 중심 | 비난 없는 사후 분석(Blameless) 및 시스템 보완 |

## Ⅳ. DevOps 도입 한계·대응책

> 도구만 도입하고 조직 문화와 평가 체계를 바꾸지 않으면 '도구 사일로'가 심화되므로 체계적인 거버넌스가 필요하다.

| 위험 | 대책 | 효과 |
|---|---|---|
| **배포 막바지 보안 병목** | SAST/DAST 자동화를 CI/CD 파이프라인에 내재화하는 **DevSecOps** 전환 | 보안 결함 조기 식별 및 배포 지연 차단 |
| **조직 KPI 상충 및 저항** | 개발-운영 간 갈등을 중재하는 **에러 예산(Error Budget)** 제도화 | 변경 속도와 서비스 신뢰성의 수학적 균형 확보 |
| **인프라 구성 불일치 (Drift)** | 콘솔 직접 수정을 금지하고 Git PR 기반 선언적 **IaC(GitOps)** 강제 | 환경 간 불일치 제거 및 배포 멱등성 보장 |

## Ⅴ. 기술사적 제언 — 공동 지표에 따른 개선

| 한계 | 해결 방안 |
|---|---|
| CI/CD 도구를 도입해도 개발·운영 간 인수인계와 장애 대응이 끊김 | 배포·운영 지표를 함께 관찰하고, 변경 실패와 복구 경험을 다음 개발·배포 과정에 반영 |
---

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 1교시: DevOps의 장점과 단점
- DORA(DevOps Research and Assessment), State of DevOps Report
- [DORA, Software delivery performance metrics](https://dora.dev/guides/dora-metrics/)
- Google SRE Book, Site Reliability Engineering: How Google Runs Production Systems

## 연결 토픽

- 이전 토픽: [BST](./001_bst.md)
- 연관 토픽: [무중단 배포](./007_zero_downtime_deployment.md), [CI/CD](./095_ci_cd.md)
- 다음 토픽: [소프트웨어 테스트 종류·레벨](./003_sw_test_types_and_levels.md)
