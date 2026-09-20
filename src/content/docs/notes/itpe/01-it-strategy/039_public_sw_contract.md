---
title: "공공 SW 사업 발주·계약"
author: "OpenAI Codex"
date: "2026-09-21T19:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 소프트웨어 사업관리를 거쳐 발주와 계약으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 사업관리</span>
  <strong>발주·계약</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 공공 SW 사업의 **범위·대가·책임·검수기준**을 경쟁과 계약 절차로 확정
- 절차: 사업계획 → RFP → 과업심의 → 입찰·평가 → 협상·계약 → 수행·변경관리
- 통제: 요구사항 명확화 · 적정 대가 · 기술평가 · 과업변경 심의 · 계약 추적성

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 소프트웨어 사업 발주와 계약의 전체 흐름">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>① 발주 준비</strong><strong>활동</strong><span>사업범위·요구사항·예산·기간 정의</span><strong>산출</strong><span>사업계획서 · RFP 초안</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>② 과업 확정</strong><strong>활동</strong><span>과업내용·사업기간·대가 검토</span><strong>산출</strong><span>과업심의 결과 · RFP</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>③ 사업자 선정</strong><strong>활동</strong><span>공고·제안평가·우선협상</span><strong>산출</strong><span>평가결과 · 협상안</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><div class="itpe-step-detail"><strong>④ 계약·이행</strong><strong>활동</strong><span>범위·대가·기간·검수조건 확정</span><strong>산출</strong><span>계약서 · 사업수행계획서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>⑤ 변경·검수</strong><strong>활동</strong><span>변경 영향분석·과업심의·검수</span><strong>산출</strong><span>변경계약 · 검수결과</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- **RFP(Request for Proposal)**: 사업범위·요구사항·평가기준·계약조건을 제시하는 제안요청서
- **FP(Function Point)**: 사용자 관점의 논리적 기능으로 SW 규모를 측정하는 방법
- **과업심의위원회**: 과업내용의 확정·변경과 이에 따른 계약금액·기간 조정을 심의하는 기구
- **협상에 의한 계약**: 제안서의 기술·가격을 평가하고 우선협상대상자와 협상하여 체결하는 계약방식
- **SLA(Service Level Agreement)**: 서비스 수준과 측정·보고·조치 기준을 합의한 문서
- **Baseline**: 변경통제를 거쳐야 수정할 수 있도록 승인된 범위·요구사항·일정·비용 기준

</details>

## 예상문제

> 공공 SW 사업의 발주·계약 절차를 설명하고, 요구사항 불명확과 과업변경 분쟁을 예방하기 위한 통제방안을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 공공 SW 사업 발주·계약의 개요

> 발주·계약은 사업구상을 **검수 가능한 요구사항과 계약 Baseline**으로 전환하는 통제 활동임.

- 정의: 공공 SW 사업의 범위·요구사항·대가·기간·책임을 명시하고 사업자를 선정하여 계약하는 조달 절차
- 목적: **공정한 사업자 선정 · 적정 대가 · 과업분쟁 예방**

## Ⅱ. 발주·계약의 구성체계와 절차

> RFP의 요구사항이 평가·협상·계약·검수까지 끊기지 않아야 함.

| 단계 | 주요 활동 | 핵심 산출물 |
|---|---|---|
| 발주 준비 | 사업범위·요구사항·예산·기간 정의 | 사업계획서 · RFP 초안 |
| 과업 확정 | 과업내용·사업기간·대가 검토 | 과업심의 결과 · RFP |
| 입찰·평가 | 공고·제안접수·기술·가격평가 | 평가결과 · 우선협상대상자 |
| 협상·계약 | 제안내용·범위·대가·검수조건 조정 | 협상결과 · 계약서 |
| 이행·변경 | 진척·품질관리·변경 영향분석 | 변경심의 · 변경계약 · 검수결과 |

<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Contract Traceability</strong></span> · 요구사항 ↔ 평가항목 ↔ 제안내용 ↔ 계약조항 ↔ 검수기준</div>

## Ⅲ. 핵심 제도와 통제 역할

> 제도명 나열보다 각 제도가 어느 위험을 통제하는지 연결해야 함.

| 통제 | 적용 | 효과 |
|---|---|---|
| **과업내용 확정** | 발주 전 사업계획서·RFP 심의 | 모호한 범위 축소 |
| **협상에 의한 계약** | 기술·가격 평가 후 계약조건 협상 | 기술·가격 균형 |
| **과업변경 심의** | 범위·비용·기간 영향 검토 | 무상 과업변경 방지 |
| **단계별 발주** | 필요 시 설계와 구현을 구분 | 구현 전 상세화 |

## Ⅳ. 일괄발주와 단계별 발주 비교

> 사업 불확실성과 설계 독립성에 따라 발주방식을 선택함.

| 기준 | 일괄발주 | 단계별 발주 |
|---|---|---|
| 범위 | 설계·구현 통합 | 설계 후 구현 분리 |
| 장점 | 책임창구·절차 단순 | 요구사항·아키텍처 상세화 |
| 위험 | 초기 RFP 모호성 | 단계 간 책임·일정 단절 |
| 적합 | 범위·기술이 명확한 사업 | 불확실성·복잡도가 큰 사업 |

## Ⅴ. 문제점·대응책

> 계약문서 간 불일치를 변경통제와 검수 단계까지 추적해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **요구사항 누락** | RFP·제안서·계약서·검수항목 추적 | 범위 누락 통제 |
| **저가·과소산정** | 규모·공수·인프라·운영비 구분 산정 | 대가 근거 명확화 |
| **무상 과업변경** | 영향분석 후 과업심의·변경계약 | 비용·기간 조정 |
| **설계·구현 단절** | 인수기준·설계검증·책임경계 명시 | 책임분쟁 완화 |

## Ⅵ. 계약 Baseline을 지키는 기술사적 제언

`[핵심 통찰]` 공공 SW 계약의 품질은 문서량이 아니라 요구사항이 평가·계약·검수 기준으로 이어지는가에 달려 있음.

`나라면` 협상 종료 전 요구사항별 제안수용 여부·계약조항·검수방법을 매핑하고, 변경은 비용·기간 영향이 승인된 뒤 반영하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 소프트웨어 계약 Baseline 통제 방안">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>문제</strong><span>RFP·제안서·계약서·검수기준 단절</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>대책</strong><span>요구사항별 계약·검수 매핑</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><div class="itpe-step-detail"><strong>변경 통제</strong><span>영향분석 → 과업심의 → 변경계약</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>효과</strong><span>범위·대가·기간·검수책임 일치</span></div></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 공공 SW 사업의 **범위·요구사항·대가·기간·책임**을 명시하고 사업자를 선정하여 계약하는 조달 절차
- 목적: **공정한 선정 · 적정 대가 · 과업분쟁 예방**

### 2. 발주·계약 절차

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 소프트웨어 발주와 계약 절차 요약">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>발주 준비</strong><strong>활동</strong><span>범위·요구사항·예산 정의</span><strong>산출</strong><span>사업계획서 · RFP 초안</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>과업 확정</strong><strong>활동</strong><span>과업내용 심의</span><strong>산출</strong><span>RFP · 심의결과</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>선정·계약</strong><strong>활동</strong><span>평가·협상·계약</span><strong>산출</strong><span>계약 Baseline</span></div></div>
</div>

### 3. 핵심 통제

- **과업심의**: 과업내용 확정·변경과 계약금액·기간 조정
- **추적성**: 요구사항 ↔ 계약조항 ↔ 검수기준 연결

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [국가법령정보센터: 소프트웨어 진흥법](https://www.law.go.kr/법령/소프트웨어진흥법)
- [국가법령정보센터: 소프트웨어사업 계약 및 관리감독에 관한 지침](https://www.law.go.kr/행정규칙/소프트웨어사업계약및관리감독에관한지침)

## 학습 체크

- [ ] Ⅰ. 발주·계약의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ. 발주 준비부터 변경·검수까지 활동·산출물을 연결할 수 있는가?
- [ ] Ⅲ. 과업내용 확정·변경과 협상계약의 통제 역할을 설명할 수 있는가?
- [ ] Ⅳ. 일괄발주와 단계별 발주의 선택 기준을 비교할 수 있는가?
- [ ] Ⅴ~Ⅵ. 요구사항 누락·과소산정·무상변경의 대응책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [POP](./038_pop.md)
- 연관 토픽: [RFP](./049_rfp.md), [소프트웨어 사업 대가산정](./026_software_cost_estimation.md), [협상에 의한 계약 세부기준](./066_negotiated_contract_proposal_evaluation.md), [과업심의 기준](./091_public_sw_cost_and_scope_change_criteria.md)
- 다음 토픽: [부정적 위험 대응 전략](./040_negative_risk_response_strategy.md)
