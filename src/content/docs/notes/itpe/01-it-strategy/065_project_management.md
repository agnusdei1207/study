---
title: "프로젝트 관리 통합 체계"
author: "Claude Code"
date: "2026-09-29T14:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → 투자·조달·프로젝트 관리 → **프로젝트 관리 통합 체계**

## 30초 인출

- 본질: 프로젝트 관리는 정해진 목표를 합의된 기간·예산·수용 기준 안에서 달성하는 활동이며, 프로그램 관리와 포트폴리오 관리가 그 위에서 편익과 전략 정합을 관리하는 계층
- 메커니즘: 프로젝트는 산출물 인도, 프로그램은 관련 프로젝트와 상시 업무의 조정으로 얻는 편익, 포트폴리오는 프로그램·프로젝트의 선정·우선순위·통제로 전략 목표와 수행 역량에 맞춤
- 통찰: 프로젝트가 산출물 인도로 끝나면 편익 실현이 관리 대상에서 빠지므로, 포트폴리오 선정 때 기대 편익과 수행 역량을 함께 확인하고 그 편익 지표를 프로그램·프로젝트의 성과 보고 기준으로 연결

<details>
<summary>핵심 용어</summary>

- **프로젝트 관리(Project Management)** : 프로젝트 수용 기준과 합의된 제약 안에서 프로젝트 목표를 달성하려고 프로세스·방법·기술·지식·경험을 적용하는 활동
- **프로그램 관리(Programme Management)** : 관련 프로젝트와 상시 업무(BAU)를 조정해 변화의 편익을 얻는 활동
- **포트폴리오 관리(Portfolio Management)** : 조직의 전략 목표와 수행 역량에 맞춰 프로그램·프로젝트를 선정하고 우선순위를 정해 통제하는 활동
- **BAU(Business As Usual)** : 변화 사업과 구별되는 상시 업무
- **산출물(Output)** : 프로젝트가 인도하는 결과물
- **편익(Benefit)** : 변화의 결과로 얻는 유익한 성과로, 프로그램 관리가 목표로 삼는 대상
- **수행 방식(Delivery Approach)** : 프로젝트를 진행하는 방식으로 predictive·incremental·iterative·adaptive·hybrid 등 애자일 포함
- **PMBOK Guide(A Guide to the Project Management Body of Knowledge)** : PMI(Project Management Institute)의 프로젝트 관리 지침서, 8판(2025.11.)은 6가지 핵심 원칙과 7개 성과 영역으로 구성
- **성과 영역(Performance Domain)** : PMBOK Guide 8판이 제시한 핵심 실무 영역으로 Governance·Scope·Schedule·Finance·Stakeholders·Resources·Risk의 7개
- **ISO 21500** : 프로젝트·프로그램·포트폴리오 관리의 조직 맥락과 개념을 규정한 국제표준

</details>

---

## 2~4교시 예상문제 (25점)

> IT 프로젝트 관리의 개념과 관리 체계, 프로젝트·프로그램·포트폴리오 관리의 비교, 한계와 방안을 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 프로젝트 관리의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **프로젝트 관리** 는 프로젝트 수용 기준과 합의된 제약 안에서 목표를 달성하려고 프로세스·방법·기술·지식·경험을 적용하는 활동 |
| 목적 | 프로젝트 목표의 달성과 상위 **프로그램 관리** 와 **포트폴리오 관리** 의 전략 목표 정합 |

## Ⅱ. 산출물에서 편익·전략으로 관리 초점이 넓어지는 계층의 특징

| 특징 | 내용 |
|---|---|
| 관리 초점의 확대 | 프로젝트는 **산출물** , 프로그램은 **편익** , 포트폴리오는 전략 목표에 맞춘 우선순위 |
| 수행 방식 중립 | 프로젝트 수행 방식은 **Delivery Approach** 로서 predictive·incremental·iterative·adaptive·hybrid 중 선택, 애자일 포함 |
| 표준의 분리 | ISO 21502는 프로젝트, ISO 21503은 프로그램, ISO 21504는 포트폴리오 지침이며 **ISO 21500** 은 공통 맥락·개념 |
| 성과 영역 중심 | **PMBOK Guide** 8판은 6가지 핵심 원칙과 7개 **성과 영역** 으로 구성하고 프로세스 안내는 비규범적 방식으로 제시 |

## Ⅲ. 프로젝트·프로그램·포트폴리오의 계층 관계와 프로젝트 관리의 성과 영역

### 3계층 관계

```text
조직 전략 목표
    │
포트폴리오 관리 ── 프로그램·프로젝트의 선정 · 우선순위 · 통제
    │
    ├─ 프로그램 관리 ── 관련 프로젝트와 BAU를 조정해 편익 획득
    │       │
    │       └─ 프로젝트 관리 ── 유한한 기간·예산 안의 산출물 인도
    │
    └─ 프로젝트 관리 ── 프로그램에 속하지 않는 독립 프로젝트
```

### 프로젝트 관리 확대: PMBOK Guide 8판의 원칙과 성과 영역

```text
프로젝트 관리 (PMBOK Guide 8판)
    │
    ├─ 6가지 핵심 원칙 ── Adopt a holistic view · Focus on value · Embed quality
    │                     Lead accountably · Integrate sustainability · Build empowered teams
    │
    └─ 7개 성과 영역 ── Governance · Scope · Schedule · Finance
                        Stakeholders · Resources · Risk
```

## Ⅳ. 프로젝트·프로그램·포트폴리오 관리의 비교

| 비교축 | 프로젝트 관리 | 프로그램 관리 | 포트폴리오 관리 |
|---|---|---|---|
| 관리 대상 | 단일 프로젝트 | 관련 프로젝트와 BAU | 프로그램·프로젝트·기타 활동의 묶음 |
| 관리 초점 | 산출물 인도 | 성과·편익 | 전략 목표와의 정합, 우선순위 |
| 핵심 활동 | 기간·예산·수용 기준 안의 목표 달성 | 관련 프로젝트의 조정 | 선정·우선순위·통제 |
| ISO 지침 | ISO 21502:2020 | ISO 21503:2022 | ISO 21504:2022 |
| PMI 표준 | PMBOK Guide 8판 | The Standard for Program Management 5판 | The Standard for Portfolio Management 4판 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 프로젝트는 산출물 인도를 관리하므로 종료 뒤 편익 실현 여부가 관리 대상에서 빠짐 | 편익을 프로그램 단위로 정의하고 편익 지표를 프로젝트 성과 보고에 연결 |
| 포트폴리오 선정 때 수행 역량을 보지 않으면 동시 수행이 과다해 자원 경합 발생 | 선정 기준에 기대 편익과 함께 조직의 수행 역량 한도 포함 |
| 프로젝트마다 수행 방식이 달라 상위 계층에서 진행 상황을 같은 기준으로 비교하기 어려움 | 7개 성과 영역을 수행 방식과 무관한 공통 보고 축으로 사용 |

## Ⅵ. 제언

포트폴리오 선정 단계에서 기대 편익과 수행 역량을 함께 확인하고, 그 편익 지표를 프로그램·프로젝트의 성과 보고 기준으로 연결

### 편익 지표의 계층 연결

```text
조직 전략 목표
    ↓
포트폴리오: 후보 사업의 기대 편익 · 수행 역량 확인 → 선정
    ↓
프로그램: 편익 지표 정의 · 관련 프로젝트 조정
    ↓
프로젝트: 산출물 인도 + 편익 지표 연결 보고
    ↓
종료 뒤: 프로그램 단위의 편익 실현 확인
```

### 프로젝트 보고 확대: 산출물과 편익 지표

```text
프로젝트 성과 보고
    │
    ├─ 성과 영역별 진행: 범위 · 일정 · 재무 · 위험 (수행 방식 공통)
    │
    └─ 편익 지표: 프로그램이 정의한 지표와의 연결
```

| 구분 | 프로젝트별 독립 관리 | 제언: 편익 지표의 계층 연결 |
|---|---|---|
| 선정 기준 | 프로젝트별 요구 | 기대 편익과 수행 역량 |
| 성과 보고 | 산출물 인도 여부 | 산출물 인도와 편익 지표 |
| 종료 뒤 관리 | 프로젝트 종료와 함께 종료 | 프로그램 단위의 편익 실현 확인 |

## 출제 이력과 검증 출처

- 제135회 3교시 1번: IT 프로젝트 관리(가. IT 프로젝트 관리의 개념, 나. IT 프로젝트 관리 프로세스, 다. IT 프로젝트 관리, 프로그램 관리, 포트폴리오 관리의 비교)
- ISO 21500:2021 Project, programme and portfolio management — Context and concepts; ISO 21502:2020 Guidance on project management; ISO 21503:2022 Guidance on programme management; ISO 21504:2022 Guidance on portfolio management
- PMI, A Guide to the Project Management Body of Knowledge (PMBOK Guide) Eighth Edition(2025.11.); The Standard for Program Management Fifth Edition; The Standard for Portfolio Management Fourth Edition(2017.11.)
- APM(Association for Project Management), 프로젝트·프로그램·포트폴리오 관리의 정의

## 연결 토픽

- 이전 토픽: [AI 에너지 인프라](./060_ai_energy_infrastructure.md)
- 연관 토픽: [ISO 21500](./043_iso_21500.md), [IT 투자평가](./016_it_investment_evaluation.md), [PMO](./004_pmo.md), [EVM](./032_evm.md)
- 다음 토픽: [협상에 의한 계약 제안서 평가](./066_negotiated_contract_proposal_evaluation.md)
