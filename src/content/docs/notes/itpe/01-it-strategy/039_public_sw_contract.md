---
title: "공공 SW 사업 발주·계약"
author: "Antigravity"
date: "2026-09-21T19:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 소프트웨어 사업관리를 거쳐 발주와 계약으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 사업관리</span>
  <strong>발주·계약</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 공공 소프트웨어 사업의 **범위·대가·기간·책임**을 법령에 따라 객관적으로 명시하고, 기술 평가와 협상을 통해 사업자를 선정하여 검수 기준선을 확정하는 조달 관리 체계.
- 메커니즘: 발주 준비(FP 대가·적정기간 산정) → **과업심의위원회(발주 전 과업 확정)** → 입찰공고 및 기술·가격 평가(협상에 의한 계약) → 기술협상 및 계약 체결 → 사업 수행 및 **과업변경심의(추가 대가·기간 반영)** → 최종 검수.
- 통제: 요구사항 상세화(RFP 모호성 제거) · 헤드카운팅 투입공수 산정 금지 · 무상 과업변경 차단 · 요구사항 추적표(RTM) 기반 계약-검수 일치성 확보.

<div class="itpe-flow-map" role="img" aria-label="공공 소프트웨어 사업 발주와 계약의 전체 흐름">
  <div class="itpe-flow-node">
    <strong>① 발주 기획 및 준비</strong>
    <small>FP 기능점수 산정 · 적정 사업기간 산정 · RFP 초안</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>소프트웨어진흥법 제50조</small></div>
  <div class="itpe-flow-node">
    <strong>② 과업심의위원회 심의</strong>
    <small>과업 내용 확정 · 적정 사업기간 및 대가 심의</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>입찰 공고 (나라장터)</small></div>
  <div class="itpe-flow-node is-current">
    <strong>③ 사업자 선정 및 계약</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>제안평가</strong><span>기술(90%) + 가격(10%) 평가</span></div>
      <div class="itpe-flow-branch"><strong>기술협상</strong><span>요구사항 수용 여부 및 조건 조정</span></div>
      <div class="itpe-flow-branch"><strong>계약확정</strong><span>계약 Baseline · 사업수행계획서</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>수행 중 변경 요구 발생 시</small></div>
  <div class="itpe-flow-node">
    <strong>④ 이행 및 과업변경심의</strong>
    <small>과업변경 심의 → 계약금액·기간 조정 → 최종 납품 검수</small>
  </div>
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

<div class="itpe-diagram-box">
  <svg viewBox="0 0 520 220" width="100%" height="220" role="img" aria-label="공공 SW 사업 발주 계약 5단계 생명주기 및 과업심의 추적성 다이어그램">
    <!-- Pipeline Boxes -->
    <rect x="15" y="20" width="85" height="90" rx="5" fill="var(--sl-color-blue-low)" stroke="var(--sl-color-blue)" stroke-width="1.5"/>
    <text x="57" y="42" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="10" font-weight="bold">① 발주 준비</text>
    <text x="57" y="60" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="8.5">FP 대가 산정</text>
    <text x="57" y="75" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">사업기간 산정</text>
    <text x="57" y="90" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">RFP 초안 작성</text>

    <!-- Arrow 1 -->
    <line x1="100" y1="65" x2="115" y2="65" stroke="var(--sl-color-gray-3)" stroke-width="2"/>

    <rect x="115" y="20" width="85" height="90" rx="5" fill="var(--sl-color-green-low)" stroke="var(--sl-color-green)" stroke-width="1.5"/>
    <text x="157" y="42" text-anchor="middle" fill="var(--sl-color-green-high)" font-size="10" font-weight="bold">② 과업 확정</text>
    <text x="157" y="60" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="8.5">과업심의위 심의</text>
    <text x="157" y="75" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">RFP 요구 확정</text>
    <text x="157" y="90" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">입찰 공고</text>

    <!-- Arrow 2 -->
    <line x1="200" y1="65" x2="215" y2="65" stroke="var(--sl-color-gray-3)" stroke-width="2"/>

    <rect x="215" y="20" width="85" height="90" rx="5" fill="var(--sl-color-purple-low)" stroke="var(--sl-color-purple)" stroke-width="1.5"/>
    <text x="257" y="42" text-anchor="middle" fill="var(--sl-color-purple-high)" font-size="10" font-weight="bold">③ 입찰·평가</text>
    <text x="257" y="60" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="8.5">기술(90%)+가격</text>
    <text x="257" y="75" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">차등점수제 적용</text>
    <text x="257" y="90" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">우선협상자 선정</text>

    <!-- Arrow 3 -->
    <line x1="300" y1="65" x2="315" y2="65" stroke="var(--sl-color-gray-3)" stroke-width="2"/>

    <rect x="315" y="20" width="85" height="90" rx="5" fill="var(--sl-color-blue-low)" stroke="var(--sl-color-blue)" stroke-width="1.5"/>
    <text x="357" y="42" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="10" font-weight="bold">④ 기술 협상</text>
    <text x="357" y="60" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="8.5">과업 범위 조율</text>
    <text x="357" y="75" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">검수 기준 확정</text>
    <text x="357" y="90" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">계약 체결</text>

    <!-- Arrow 4 -->
    <line x1="400" y1="65" x2="415" y2="65" stroke="var(--sl-color-gray-3)" stroke-width="2"/>

    <rect x="415" y="20" width="90" height="90" rx="5" fill="var(--sl-color-red-low)" stroke="var(--sl-color-red)" stroke-width="1.5"/>
    <text x="460" y="42" text-anchor="middle" fill="var(--sl-color-red-high)" font-size="10" font-weight="bold">⑤ 이행·변경</text>
    <text x="460" y="60" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="8.5">과업변경심의</text>
    <text x="460" y="75" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">금액·기간 조정</text>
    <text x="460" y="90" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">최종 인수 검수</text>

    <!-- Traceability Band below -->
    <rect x="15" y="130" width="490" height="70" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>
    <text x="260" y="152" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="10.5" font-weight="bold">계약 추적성(Contract Traceability) 매핑 구조</text>
    <text x="260" y="172" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="10">RFP 요구사항 식별자(REQ-01) ➔ 제안서 수용표 ➔ 기술협상 합의서 ➔ 계약서 명시 ➔ WBS 과업 ➔ 단위/인수 검수표</text>
    <text x="260" y="190" text-anchor="middle" fill="var(--sl-color-red-high)" font-size="9.5">통제: 변경 요구 발생 시 사업자 단독 무상 변경 금지 ➔ 과업변경심의위원회 의결 후 변경계약 체결</text>
  </svg>
</div>

| 단계 | 주요 활동 | 핵심 산출물 |
|---|---|---|
| **발주 준비** | 사업범위·요구사항·예산·기간 정의, FP 대가 산정 | 사업계획서 · RFP 초안 · 적정기간 산정서 |
| **과업 확정** | 발주 전 과업내용·사업기간·대가 검토 심의 | 과업심의 결과서 · 확정 RFP |
| **입찰·평가** | 공고·제안접수·기술평가(90%)+가격평가(10%) | 기술평가 결과표 · 우선협상대상자 선정 |
| **협상·계약** | 제안내용·범위·대가·검수조건 조정 및 합의 | 기술협상 합의서 · 최종 계약서 |
| **이행·변경** | 진척·품질관리·변경 발생 시 과업변경심의 | 과업변경 심의의결서 · 변경계약서 · 검수조서 |

<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Contract Traceability</strong></span> · 요구사항 ↔ 평가항목 ↔ 제안내용 ↔ 계약조항 ↔ 검수기준</div>

## Ⅲ. 핵심 제도와 통제 역할

> 제도명 나열보다 각 제도가 어느 위험을 통제하는지 연결해야 함.

| 통제 제도 | 법적 근거 및 실무 적용 내용 | 핵심 기대 효과 |
|---|---|---|
| **발주 전 과업심의** | 소프트웨어진흥법 제50조 (발주 전 사업계획·RFP 필수 심의) | 모호한 요구사항 사전 제거, 부실 발주 차단 |
| **적정 사업기간 산정** | 소프트웨어사업 계약 및 관리감독에 관한 지침 (개발기간 산정식 적용) | 무리한 납기 설정 방지, 개발 품질 및 안전 확보 |
| **협상에 의한 계약** | 국가계약법 시행령 제43조 (기술 90%, 가격 10% 비중 확대) | 덤핑 저가입찰 방지 및 기술 우수 사업자 선정 |
| **과업변경 심의** | 계약 체결 후 변경 발생 시 사업자 신청 권리 보장 | 무상 과업변경(추가 요구) 방지 및 예산·기간 증액 |
| **헤드카운팅 금지** | 투입인력 등급·인원수 기준 대가 산정 및 근태 관리 금지 | 투입공수 관리 폐해 탈피, 기능·산출물 중심 계약 전환 |

## Ⅳ. 일괄발주와 단계별 발주 비교

> 사업 불확실성과 설계 독립성에 따라 발주방식을 선택함.

| 기준 | 일괄발주 (Turn-key) | 단계별 발주 (설계·구현 분할) |
|---|---|---|
| **범위** | 분석·설계·구현·테스트를 단일 사업으로 통합 | 1단계: 분석·설계(요구정의) / 2단계: 개발·구현 |
| **장점** | 책임 창구 단일화, 조달 행정 절차 간소화 | 요구사항 및 아키텍처 상세화 후 구현비 산출 |
| **위험** | 초기 RFP 모호성으로 인한 잦은 과업변경 및 분쟁 | 단계 간 책임 단절, 사업자 변경 시 학습비용 발생 |
| **적합 대상** | 범위와 기술 스택이 이미 명확한 표준화 사업 | 불확실성이 크고 신기술(클라우드·AI) 결합된 대규모 사업 |

## Ⅴ. 문제점·대응책

> 계약문서 간 불일치를 변경통제와 검수 단계까지 추적해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **요구사항 누락** | RFP·제안서·계약서·검수항목 추적표(RTM) 필수 작성 | 범위 누락 통제 |
| **저가·과소산정** | 기능점수(FP) 기반 단가 산정 및 기술평가 차등점수제 도입 | 대가 근거 명확화 |
| **무상 과업변경** | 사업자 과업변경 신청권 보장 및 과업심의위 심의 의무화 | 비용·기간 현실적 증액 |
| **설계·구현 단절** | 상세 설계 산출물 검수 기준 강화 및 인수 인계 기간 보장 | 책임분쟁 완화 |

## Ⅵ. 계약 Baseline을 지키는 기술사적 제언

> 공공 SW 사업 분쟁의 근본 원인은 기술 실패가 아닌 '모호한 계약과 무상 변경'에 있으므로, 엄격한 계약 Baseline 관리가 핵심임.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]` 공공 SW 계약의 품질은 문서량이 아니라 요구사항이 평가·계약·검수 기준으로 이어지는가에 달려 있음.
- `나라면` 기술협상 단계에서 요구사항별 수용 여부와 검수 방법을 일대일 매핑한 요구사항 추적표(RTM)를 계약서 별첨으로 확정하고, 발주처 구두 요구는 과업심의 접수 전까지 일체 작업을 거부하도록 공정 프로세스를 제도화하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 사업 시작 전 요구사항 상세화율 90% 이상 확보 및 모든 과업변경 건의 과업심의위원회 의결 반영률 100%.
- **공학적 대안**: 설계-구현 분할발주 확대 적용 및 기능점수(FP) 기반 정량적 대가 산정 체계 정착.
- **검증 절차**: 발주 전 과업심의 의결서 준수 여부 및 최종 검수 시 RTM 기반 일대일 테스트 합격 검증.
- **기대 효과**: 공공 SW 사업의 유찰 및 파행 방지, 적정 대가 보장을 통한 SW 생태계 선순환 구축.

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
