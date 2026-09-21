---
title: "AI 거버넌스 플랫폼"
author: "Antigravity"
date: "2026-09-21T23:30:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략 관리에서 AI 거버넌스를 거쳐 AI 거버넌스 플랫폼으로 이어지는 지식 위치">
  <span>IT 전략·관리</span><span>AI 거버넌스</span><strong>AI 거버넌스 플랫폼</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 거버넌스 **정책·책임·위험기준**을 AI 수명주기의 통제점과 증적으로 구현
- 흐름: AI 자산 등록 → 위험평가 → 개발·검증 → 승인·배포 → 운영감시·사고대응
- 증적: **AI Inventory·System Card·평가결과·승인기록·운영로그**

<div class="itpe-svg-map">
<svg viewBox="0 0 760 650" role="img" aria-label="AI 거버넌스 정책이 수명주기 통제와 감사 증적으로 구현되는 플랫폼 구조">
  <defs><marker id="arrow-ai-gov" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <rect class="itpe-svg-node is-current" x="130" y="24" width="500" height="82" rx="14" />
  <text class="itpe-svg-title" x="380" y="58" text-anchor="middle">거버넌스 정책·책임</text>
  <text class="itpe-svg-sub" x="380" y="84" text-anchor="middle">위험기준 · 역할 · 승인 · 예외 · 규제 의무</text>
  <path class="itpe-svg-link" d="M380 106 V146" marker-end="url(#arrow-ai-gov)" />
  <rect class="itpe-svg-node" x="130" y="154" width="500" height="92" rx="14" />
  <text class="itpe-svg-title" x="380" y="188" text-anchor="middle">Governance Control Plane</text>
  <text class="itpe-svg-sub" x="380" y="216" text-anchor="middle">AI Inventory · 위험평가 · 승인 · 예외관리</text>
  <path class="itpe-svg-link" d="M380 246 V286" marker-end="url(#arrow-ai-gov)" />
  <rect class="itpe-svg-node" x="130" y="294" width="500" height="92" rx="14" />
  <text class="itpe-svg-title" x="380" y="328" text-anchor="middle">Lifecycle Gate</text>
  <text class="itpe-svg-sub" x="380" y="356" text-anchor="middle">데이터 · 모델 · 프롬프트 · 배포 검증</text>
  <path class="itpe-svg-link" d="M380 386 V426" marker-end="url(#arrow-ai-gov)" />
  <rect class="itpe-svg-node" x="130" y="434" width="500" height="92" rx="14" />
  <text class="itpe-svg-title" x="380" y="468" text-anchor="middle">Runtime Control</text>
  <text class="itpe-svg-sub" x="380" y="496" text-anchor="middle">성능·편향·보안 감시 · Human Oversight · 사고대응</text>
  <path class="itpe-svg-link" d="M380 526 V566" marker-end="url(#arrow-ai-gov)" />
  <rect class="itpe-svg-node" x="130" y="574" width="500" height="58" rx="14" />
  <text class="itpe-svg-title" x="380" y="610" text-anchor="middle">감사 증적 · 지속 개선</text>
</svg>
</div>

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

<div class="itpe-svg-map">
  <svg viewBox="0 0 520 220" role="img" aria-label="AI 거버넌스 플랫폼 4계층 아키텍처">
    <!-- Layer 1: Policy Plane -->
    <rect x="20" y="15" width="480" height="42" rx="6" class="itpe-svg-node is-current"></rect>
    <text x="260" y="32" class="itpe-svg-title">1. 정책 및 관리 계층 (Governance Policy Plane)</text>
    <text x="260" y="48" class="itpe-svg-sub">ISO/IEC 42001(AIMS) 정책 · 책임(RACI) · 윤리기준 · 예외 심의</text>

    <!-- Layer 2: Control Plane -->
    <rect x="20" y="65" width="480" height="42" rx="6" class="itpe-svg-node"></rect>
    <text x="260" y="82" class="itpe-svg-title">2. 자산 및 위험 통제 계층 (Asset & Risk Control Plane)</text>
    <text x="260" y="98" class="itpe-svg-sub">AI Inventory · NIST AI RMF 영향평가 · 고/중/저 위험등급 분류</text>

    <!-- Layer 3: Pipeline & Gate -->
    <rect x="20" y="115" width="480" height="42" rx="6" class="itpe-svg-node is-current"></rect>
    <text x="260" y="132" class="itpe-svg-title">3. 수명주기 게이트 계층 (Lifecycle Quality Gate Plane)</text>
    <text x="260" y="148" class="itpe-svg-sub">데이터 Lineage · 모델 편향/성능 검증 · System Card 승인 · CI/CD 연동</text>

    <!-- Layer 4: Runtime & Evidence -->
    <rect x="20" y="165" width="480" height="42" rx="6" class="itpe-svg-node"></rect>
    <text x="260" y="182" class="itpe-svg-title">4. 런타임 감시 및 증적 계층 (Runtime & Audit Evidence Plane)</text>
    <text x="260" y="198" class="itpe-svg-sub">환각/드리프트 감시 · Human Oversight 개입 · 감사 로그 추적</text>
  </svg>
</div>

| 계층 | 핵심 기능 | 주요 증적 |
|---|---|---|
| 관리체계 | 정책·역할·책임·위험기준·예외 | 정책·RACI·위험수용 기록 |
| 통제평면 | AI 자산·위험평가·승인·변경관리 | AI Inventory·승인 이력 |
| 수명주기 연계 | 데이터·모델·프롬프트·배포 Gate | Lineage·평가결과·System Card |
| 운영통제 | 성능·편향·보안 감시·Human Oversight | 운영로그·경보·개입 기록 |
| 증적관리 | 의무-통제-증적 매핑·감사·개선 | 통제목록·감사추적·개선조치 |

## Ⅲ. AI 수명주기 통제 프로세스

> 각 단계는 활동과 산출물을 함께 관리하고, 위험 변화가 발생하면 이전 단계로 환류함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="AI 거버넌스 플랫폼의 수명주기 통제 프로세스">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>① 등록·분류</strong><strong>활동</strong><span>목적·소유자·영향대상·사용환경 식별</span><strong>산출</strong><span>AI Inventory · 위험등급</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>② 설계·개발</strong><strong>활동</strong><span>데이터·모델·보안·인적감독 통제 설계</span><strong>산출</strong><span>통제계획 · Lineage</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>③ 검증·승인</strong><strong>활동</strong><span>성능·공정성·안전·보안·준수 평가</span><strong>산출</strong><span>평가결과 · System Card · 승인기록</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>④ 배포·운영</strong><strong>활동</strong><span>버전통제·모니터링·사용자 고지·인적개입</span><strong>산출</strong><span>배포기록 · 운영로그 · 경보</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>⑤ 사고·변경</strong><strong>활동</strong><span>영향평가·중단·완화·재승인·폐기</span><strong>산출</strong><span>사고기록 · 개선조치 · 폐기증적</span></div></div>
</div>

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
| Shadow AI | AI Inventory·접근경로 등록 | 미승인 사용 식별 |
| 형식적 승인 | 위험기반 Gate·예외 만료·재승인 | 책임 있는 출시 판단 |
| 개발·규제 증적 단절 | 의무-통제-증적 매핑 | 감사 추적성 확보 |
| 운영 중 성능·위험 변화 | 지속 감시·Human Oversight·사고대응 | 영향 확산 억제 |

## Ⅵ. 증적 기반 Quality Gate 제언

### 학습자 통찰 메모 — 답안 밖

`[핵심 통찰]` AI 거버넌스의 성패는 원칙의 수가 아니라, 각 위험에 책임자·통제점·판정기준·증적이 연결되어 실제 배포 판단을 바꾸는가에 달려 있음.

`나라면` 고위험 AI는 선언적 체크리스트로 승인하지 않고, 사용맥락별 필수 증적을 확인하는 Quality Gate와 예외 만료일을 두어 미충족 항목이 해소될 때만 배포하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준 (Trigger)**: 고위험 AI 모델의 데이터 리니지(Lineage) 누락, 또는 환각(Hallucination)·편향성 검증 미달 시 배포 파이프라인 자동 차단(Hard Gate).
- **대응 방안 (Action)**: Policy-as-Code 기반 자동 검증 도구(CI/CD Gatekeeper)를 연동하고, 미충족 시 Human Oversight 승인위원회 재심의를 강제함.
- **검증 체계 (Verification)**: ISO/IEC 42001(AIMS) 및 EU AI Act 기준 System Card 증적의 완결성과 런타임 데이터 드리프트 지표(PSI > 0.25)를 실시간 감사함.
- **기대 효과 (Impact)**: Shadow AI 및 규제 위반 과징금 리스크 원천 차단, AI 시스템의 전사적 신뢰성 및 추적성 100% 확보를 달성함.

<div class="itpe-svg-map">
<svg viewBox="0 0 760 440" role="img" aria-label="AI 거버넌스 증적 기반 품질 게이트의 통과와 보완 분기">
  <defs><marker id="arrow-ai-qg" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <rect class="itpe-svg-node" x="170" y="24" width="420" height="76" rx="14" />
  <text class="itpe-svg-title" x="380" y="56" text-anchor="middle">위험·의무 식별</text>
  <text class="itpe-svg-sub" x="380" y="82" text-anchor="middle">사용맥락 · 영향대상 · 규제 요구</text>
  <path class="itpe-svg-link" d="M380 100 V142" marker-end="url(#arrow-ai-qg)" />
  <rect class="itpe-svg-node is-current" x="170" y="150" width="420" height="86" rx="14" />
  <text class="itpe-svg-title" x="380" y="182" text-anchor="middle">Evidence Quality Gate</text>
  <text class="itpe-svg-sub" x="380" y="210" text-anchor="middle">통제 수행 · 판정기준 충족 · 증적 완결</text>
  <path class="itpe-svg-link" d="M300 236 V282 H170 V318" marker-end="url(#arrow-ai-qg)" />
  <path class="itpe-svg-link" d="M460 236 V282 H590 V318" marker-end="url(#arrow-ai-qg)" />
  <text class="itpe-svg-label" x="210" y="276" text-anchor="middle">통과</text>
  <text class="itpe-svg-label" x="550" y="276" text-anchor="middle">미통과</text>
  <rect class="itpe-svg-node" x="50" y="326" width="240" height="76" rx="14" />
  <text class="itpe-svg-title" x="170" y="358" text-anchor="middle">승인·배포</text>
  <text class="itpe-svg-sub" x="170" y="384" text-anchor="middle">운영감시 · 재평가</text>
  <rect class="itpe-svg-node" x="470" y="326" width="240" height="76" rx="14" />
  <text class="itpe-svg-title" x="590" y="358" text-anchor="middle">보완·재검증</text>
  <text class="itpe-svg-sub" x="590" y="384" text-anchor="middle">통제 수정 · 예외 심의</text>
</svg>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: AI 정책·책임·위험기준을 AI 자산·개발·배포·운영 통제와 증적관리로 구현하는 플랫폼
- 목적: **책임성·추적성·규제 대응·운영위험 통제**

### 2. 구성

| 영역 | 핵심 |
|---|---|
| 관리체계 | 정책·역할·위험기준 |
| 통제평면 | 자산·평가·승인·예외 |
| 수명주기 | 데이터·모델·배포 Gate |
| 운영·증적 | 감시·사고·감사추적 |

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
