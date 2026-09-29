---
title: "애자일 전환 전략"
author: "Claude Code"
date: "2026-09-29T22:40:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → 디지털 혁신·전략 → **애자일 전환 전략**

## 30초 인출

- 본질: 애자일 전환 전략은 팀 단위로 쓰던 애자일 방식을 조직의 구조·예산·리더십까지 넓혀 요구 변화에 빠르게 대응하도록 바꾸는 계획
- 메커니즘: 팀은 Sprint 단위로 Increment를 만들고, 여러 팀은 가치 흐름 단위로 묶어 계획을 맞추며, 예산은 프로젝트 대신 가치 흐름에 배정
- 통찰: 팀마다 Definition of Done이 다르면 Sprint마다 나오는 Increment의 품질·보안 수준이 갈라져 확산할수록 통합 위험이 커지므로 파일럿에서 검증한 공통 Definition of Done의 충족을 팀 추가 조건으로 설정

<details>
<summary>핵심 용어</summary>

- **애자일 전환 전략** : 애자일 가치와 원칙을 팀 운영에서 조직 구조·예산·리더십으로 넓히는 전환 계획
- **Agile Manifesto(애자일 선언)** : 개인과 상호작용, 작동하는 소프트웨어, 고객과의 협력, 변화에 대응을 각각 프로세스와 도구, 포괄적인 문서, 계약 협상, 계획 준수보다 더 가치 있게 보는 2001년 선언
- **Scrum(스크럼)** : 복잡한 문제에 대해 적응적 해법으로 가치를 만들도록 돕는 경량 프레임워크
- **Sprint(스프린트)** : Scrum에서 한 달 이하로 고정한 작업 주기로, 목표는 Sprint Goal 하나
- **Product Backlog(제품 백로그)** : Scrum에서 제품 개선에 필요한 작업 목록으로 Product Goal을 약속 대상으로 가짐
- **Increment(증분)** : Sprint마다 이전 Increment에 더해지고 충분히 검증된, 사용 가능한 결과물
- **Definition of Done(완료 정의)** : Increment가 제품에 요구되는 품질 기준을 충족한 상태를 밝힌 공식 기술
- **SAFe(Scaled Agile Framework)** : 여러 애자일 팀을 Agile Release Train 단위로 묶고 예산까지 다루는 확장 프레임워크
- **ART(Agile Release Train)** : 개발 가치 흐름의 솔루션을 증분 방식으로 개발·전달하는, 장기 운영되는 애자일 팀들의 묶음
- **Lean Budgets(린 예산)** : 프로젝트 대신 가치 흐름에 자금을 배정하는 SAFe의 재무 거버넌스 방식
- **LeSS(Large-Scale Scrum)** : 하나의 Product Backlog와 Product Owner를 여러 팀이 공유하는 Scrum 확장 방식

</details>

---

## 2~4교시 예상문제 (25점)

> 애자일 전환 전략에 대하여 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 애자일 전환 전략의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **애자일 전환 전략** 은 애자일 가치와 원칙을 팀 운영에서 조직의 구조·예산·리더십으로 넓히는 전환 계획 |
| 목적 | 요구 변화에 대한 대응 속도 향상과 가치 전달 주기 단축 |

## Ⅱ. 팀 운영에서 조직으로 확장되는 애자일의 특징

| 특징 | 의미 |
|---|---|
| 가치·원칙 기반 | **Agile Manifesto** 의 4가지 가치와 12가지 원칙에서 출발 |
| 짧은 주기의 전달 | 작동하는 소프트웨어를 몇 주에서 몇 달 사이, 짧은 주기를 선호해 자주 전달 |
| 경험적 통제 | **Scrum** 의 투명성(Transparency)·검사(Inspection)·적응(Adaptation) |
| 조직 차원의 변화 | 팀 운영에 더해 여러 팀의 정렬과 재무 방식의 변경 |

## Ⅲ. 애자일 전환의 3계층 체계

```text
리더십·재무 거버넌스 ── 예산 배정 단위, 성과 검토 (SAFe: Lean Budgets)
    │
조직 구조 ── 가치 흐름 단위로 묶은 여러 팀 (SAFe: ART, LeSS: 공유 Product Backlog)
    │
팀 운영 ── Scrum: Product Owner · Scrum Master · Developers, Sprint 이벤트
```

### 팀 운영 확대: Sprint 한 주기

```text
Product Backlog (Product Goal)
    ↓
Sprint Planning → Sprint Backlog (Sprint Goal)
    ↓
Sprint 진행 (Daily Scrum 15분)
    ↓
Increment (Definition of Done 충족)
    ↓
Sprint Review: 결과 점검과 이후 조정 결정
    ↓
Sprint Retrospective: 품질·효과 향상 방법 계획 → 다음 Sprint
```

## Ⅳ. 확장 방식 비교: Scrum·LeSS·SAFe

| 비교축 | Scrum | LeSS | SAFe |
|---|---|---|---|
| 확장 단위 | Scrum Team, 통상 10명 이하 | 최대 8개 팀(팀당 8명), **LeSS Huge** 는 한 제품에 수천 명까지 | **ART** 통상 50~125명, ART를 늘려 확장 |
| 정렬·점검 방식 | Sprint Planning·Daily Scrum·Sprint Review·Sprint Retrospective | 공통 Sprint, 다중 팀 Sprint Planning, Overall Retrospective | Planning Interval과 ART 이벤트 |
| 공통 기준 | Sprint마다 Increment와 Definition of Done | 단일 Product Backlog·Product Owner, 공통 Definition of Done | 개발 가치 흐름 단위의 ART 운영 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 팀은 Sprint로 일하지만 예산이 프로젝트 단위로 남아 범위·비용 고정 방식과 충돌 | 프로젝트가 아닌 가치 흐름에 배정하는 **Lean Budgets** 방식으로 예산 단위 전환 |
| 팀별 Definition of Done이 달라 Increment의 품질 편차가 통합 시점에 드러남 | LeSS처럼 팀이 공유하는 공통 Definition of Done 적용 |
| 리더가 Sprint 결과 대신 계획 준수를 평가하면 팀 자율성이 형식에 그침 | 팀 확산 전에 경영진·관리자 교육을 먼저 수행하는 SAFe Implementation Roadmap 순서 적용 |
| 여러 팀이 한 제품을 만들 때 팀 간 의존으로 작업 대기 발생 | 가치 흐름 단위로 팀을 묶어 ART 또는 공유 Product Backlog로 정렬 |

## Ⅵ. 제언

팀 수가 아닌 파일럿 팀의 Increment가 공통 Definition of Done을 충족했는지를 확산 조건으로 삼고, 조건을 충족한 뒤 가치 흐름 단위로 팀과 예산을 넓히는 방식

### 파일럿에서 확산까지의 조건부 확대

```text
파일럿 팀 Sprint 운영
    ↓
Increment가 공통 Definition of Done을 충족했는가
    ├─ 미충족 → 기준·운영 보완 후 재검증, 팀 추가 보류
    └─ 충족 → 가치 흐름 단위로 팀 추가
                  ↓
              예산·성과 검토 단위를 가치 흐름으로 전환
```

### 공통 Definition of Done 확대: 보안 기준 포함

```text
공통 Definition of Done
    │
    ├─ 기능 기준 ── 수용 조건 충족, 통합 테스트 통과
    │
    ├─ 품질 기준 ── 회귀 테스트·성능 기준 통과
    │
    └─ 보안 기준 ── 취약점 점검 결과 조치, 비밀정보 노출 없음
```

| 구분 | 팀 수 기준 확산 | 제언: 완료 정의 충족 기준 확산 |
|---|---|---|
| 확산 판단 | 도입 팀 수와 교육 이수 | 파일럿 Increment의 Definition of Done 충족 |
| 품질·보안 편차 발견 | 통합·검수 시점 | Sprint 종료 시점 |
| 팀 추가 조건 | 일정 도래 | 기준 충족 후 가치 흐름 단위로 추가 |

## 출제 이력과 검증 출처

- 제132~140회 정보관리기술사 공식 문제지에서 애자일 전환을 직접 묻는 문항 없음
- Agile Manifesto(2001), Manifesto for Agile Software Development의 4가지 가치·12가지 원칙
- Scrum Guide(Schwaber·Sutherland) — Scrum 정의, 팀 구성, 이벤트, 산출물과 약속
- LeSS 프레임워크(LeSS Company) — LeSS·LeSS Huge 구성
- SAFe(Scaled Agile, Inc.) — ART, Lean Budgets, Implementation Roadmap

## 연결 토픽

- 이전 토픽: [FinOps](./012_finops.md)
- 연관 토픽: [디지털 트랜스포메이션(DX)](./020_digital_transformation.md), [IT 투자평가·투자관리](./016_it_investment_evaluation.md), [스크럼](../02-software-engineering/025_scrum.md), [애자일 방법론](../02-software-engineering/119_agile_methodology.md)
- 다음 토픽: [IT 투자평가·투자관리](./016_it_investment_evaluation.md)
