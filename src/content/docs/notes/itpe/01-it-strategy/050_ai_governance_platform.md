---
title: "AI 거버넌스 플랫폼"
author: "Codex"
date: "2026-09-21T23:47:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "GLM-5.3-Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략 관리에서 AI 거버넌스를 거쳐 AI 거버넌스 플랫폼으로 이어지는 지식 위치">
  <span>IT 전략·관리</span><span>AI 거버넌스</span><strong>AI 거버넌스 플랫폼</strong>
</div>

## 30초 인출

- 본질: 거버넌스 정책·책임·위험기준을 AI 수명주기 전반의 통제점과 감사 증적으로 구현하는 통합 통제 플랫폼
- 메커니즘: AI 자산 등록(Inventory) → 위험평가(NIST AI RMF) → 파이프라인 검증(Lineage/편향) → 배포 게이트(System Card) → 런타임 감시 및 Human Oversight
- 판정 기준: 고위험 AI 모델의 데이터 Lineage 100% 확보 및 런타임 드리프트(PSI > 0.25) 경보 시 즉각적 개입 증적 존재 여부

<details>
<summary>핵심 용어</summary>

- **AIMS(Artificial Intelligence Management System)**: AI의 책임 있는 개발·제공·사용을 위한 방침·목표·프로세스의 관리체계
- **AI Inventory**: 조직이 개발·구매·운영하는 AI 시스템의 목적·소유자·위험등급·상태 목록
- **System Card**: AI 시스템의 목적·범위·성능·한계·위험·평가결과를 기록한 증적
- **Policy-as-Code**: 정책의 판정 규칙을 코드화하여 개발·배포 과정에서 반복 검증하는 방식
- **Human Oversight**: 위험도와 영향에 따라 사람이 검토·승인·중단할 수 있도록 한 통제
- **Lineage**: 데이터·모델·프롬프트·배포 버전의 생성과 변경 관계를 추적하는 정보
- **MLOps(Machine Learning Operations)**: ML 모델의 개발·배포·운영을 연결하는 실무체계
- **LLMOps(Large Language Model Operations)**: LLM 서비스의 프롬프트·평가·배포·운영을 관리하는 실무체계

</details>

## 예상문제

> AI 거버넌스 플랫폼의 개념과 구성체계를 설명하고, AI 수명주기 통제 프로세스 및 운영상 문제점·대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. AI 거버넌스 정책을 실행 통제로 전환하는 플랫폼

> AI 거버넌스 플랫폼은 선언적 원칙을 **승인 Gate·운영 통제·감사 증적**으로 전환하여 AI 위험을 수명주기 전반에서 관리함.

- 정의: 조직의 AI 정책·책임·위험기준을 AI 자산·개발·배포·운영 통제와 증적관리로 구현하는 통합 플랫폼
- 목적: **책임성·추적성·규제 대응·운영위험 통제**
- 기준: **ISO/IEC 42001:2023**의 AIMS와 **NIST AI RMF(Artificial Intelligence Risk Management Framework)**의 Govern·Map·Measure·Manage를 조직 환경에 맞게 적용

## Ⅱ. AI 거버넌스 플랫폼 구성체계

> 관리체계·통제평면·개발도구를 분리하고, 공통 식별자와 증적으로 연결해야 정책과 실행의 단절을 방지할 수 있음.

```mermaid
flowchart TD
    L1["정책·관리 계층"] --> L2["자산·위험 통제 계층"] --> L3["수명주기 게이트 계층"] --> L4["런타임 감시·증적 계층"]
```

| 계층 | 핵심 기능 | 주요 증적 |
|---|---|---|
| 관리체계 | 정책·역할·책임·위험기준·예외 | 정책·RACI·위험수용 기록 |
| 통제평면 | AI 자산·위험평가·승인·변경관리 | AI Inventory·승인 이력 |
| 수명주기 연계 | 데이터·모델·프롬프트·배포 Gate | Lineage·평가결과·System Card |
| 운영통제 | 성능·편향·보안 감시·Human Oversight | 운영로그·경보·개입 기록 |
| 증적관리 | 의무-통제-증적 매핑·감사·개선 | 통제목록·감사추적·개선조치 |

## Ⅲ. AI 수명주기 통제 프로세스

> 각 단계는 활동과 산출물을 함께 관리하고, 위험 변화가 발생하면 이전 단계로 환류함.

```mermaid
flowchart TD
    S1["① 등록·분류"] --> S2["② 설계·개발"] --> S3["③ 검증·승인"] --> S4["④ 배포·운영"] --> S5["⑤ 사고·변경"]
```

## Ⅳ. Data Governance·MLOps·AI Governance 비교

> 세 영역은 대체관계가 아니라 데이터 품질, 생산운영, 책임통제를 분담하는 결합관계임.

| 기준 | Data Governance | MLOps·LLMOps | AI Governance Platform |
|---|---|---|---|
| 초점 | 데이터 품질·보호 | 개발·배포·운영 | 책임·위험·준수 |
| 대상 | 데이터·메타데이터 | 모델·프롬프트·파이프라인 | AI 시스템·사용맥락 |
| 통제 | 표준·품질·권한 | 버전·시험·배포·감시 | 위험평가·승인·감독·증적 |
| 연계 | Lineage 제공 | Lifecycle Gate 실행 | 정책·판정기준 제공 |

## Ⅴ. 문제점·대응책

> 도구 도입보다 AI 자산 식별, 책임 배정, 통제 증적의 연결이 먼저임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **Shadow AI** | AI Inventory·접근경로 등록 | 미승인 사용 식별 |
| **형식적 승인** | 위험기반 Gate·예외 만료·재승인 | 책임 있는 출시 판단 |
| **개발·규제 증적 단절** | 의무-통제-증적 매핑 | 감사 추적성 확보 |
| **운영 중 성능·위험 변화** | 지속 감시·Human Oversight·사고대응 | 영향 확산 억제 |

## Ⅵ. 증적 기반 Quality Gate 제언

### 학습자 통찰 메모 — 답안 밖

`[핵심 통찰]` AI 거버넌스의 성패는 원칙의 수가 아니라, 각 위험에 책임자·통제점·판정기준·증적이 연결되어 실제 배포 판단을 바꾸는가에 달려 있음.

`나라면` 고위험 AI는 선언적 체크리스트로 승인하지 않고, 사용맥락별 필수 증적을 확인하는 Quality Gate와 예외 만료일을 두어 미충족 항목이 해소될 때만 배포하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준 (Trigger)**: 고위험 AI 모델의 데이터 리니지(Lineage) 누락, 또는 환각(Hallucination)·편향성 검증 미달 시 배포 파이프라인 자동 차단(Hard Gate).
- **대응 방안 (Action)**: Policy-as-Code 기반 자동 검증 도구(CI/CD Gatekeeper)를 연동하고, 미충족 시 Human Oversight 승인위원회 재심의를 강제함.
- **검증 체계 (Verification)**: ISO/IEC 42001(AIMS) 및 EU AI Act 기준 System Card 증적의 완결성과 런타임 데이터 드리프트 지표(PSI > 0.25)를 실시간 감사함.
- **기대 효과 (Impact)**: Shadow AI 및 규제 위반 과징금 리스크 원천 차단, AI 시스템의 전사적 신뢰성 및 추적성 100% 확보를 달성함.

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: AI 정책·책임·위험기준을 AI 자산·개발·배포·운영 통제와 증적관리로 구현하는 플랫폼
- 목적: **책임성·추적성·규제 대응·운영위험 통제**

### 2. 구성 계층

```mermaid
flowchart TD
    L1["정책·관리 계층"] --> L2["자산·위험 통제 계층"] --> L3["수명주기 게이트 계층"] --> L4["런타임 감시·증적 계층"]
```

### 3. 핵심 통제

- **Risk-based Gate**: 사용맥락과 영향에 따라 평가·승인 강도 차등화
- **Evidence Traceability**: 의무 → 통제 → 평가결과 → 승인기록 연결

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [ISO, ISO/IEC 42001:2023 AI management systems](https://www.iso.org/standard/42001)
- [NIST, AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [European Commission, AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## 학습 체크

- [ ] Ⅰ: 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 관리체계·통제평면·수명주기·운영·증적 계층을 구분할 수 있는가?
- [ ] Ⅲ: 등록부터 사고·변경까지 활동과 산출물을 연결할 수 있는가?
- [ ] Ⅳ: Data Governance·MLOps·AI Governance의 역할을 비교할 수 있는가?
- [ ] Ⅴ: 위험-대책-효과 세 쌍을 제시할 수 있는가?
- [ ] Ⅵ: 증적 기반 Quality Gate를 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [제안요청서(RFP)](./049_rfp.md)
- 연관 토픽: [NIST AI RMF](./036_nist_ai_rmf.md), [AI 프라이버시 위험관리 모델](./054_ai_privacy_risk_management_model.md)
- 다음 토픽: [AI 고속도로](./051_ai_highway.md)
