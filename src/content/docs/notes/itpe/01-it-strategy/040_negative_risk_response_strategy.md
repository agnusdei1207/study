---
title: "부정적 위험 대응 전략"
author: "OpenAI Codex"
date: "2026-09-21T19:45:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 위험관리를 거쳐 부정적 위험 대응 전략으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 위험관리</span>
  <strong>부정적 위험 대응 전략</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 프로젝트 목표를 저해하는 **위협(Threat)**의 노출도를 허용수준 이하로 통제
- 전략: 회피(Avoid) · 전가(Transfer) · 완화(Mitigate) · 수용(Accept) · 상위보고(Escalate)
- 통제: 위험책임자 · 실행조건(Trigger) · 비상대책 · 잔여위험 · 2차위험 재평가

<div class="itpe-svg-map">
  <svg viewBox="0 0 720 600" role="img" aria-label="부정적 위험 분석부터 대응과 재평가까지의 폐쇄 루프">
    <defs><marker id="risk-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z"></path></marker></defs>
    <rect x="190" y="25" width="340" height="80" rx="14" class="itpe-svg-node"></rect><text x="360" y="58" class="itpe-svg-title">위험 식별·분석</text><text x="360" y="84" class="itpe-svg-sub">원인 · 확률 · 영향 · 긴급성</text>
    <path d="M360 105 V145" class="itpe-svg-link" marker-end="url(#risk-arrow)"></path>
    <rect x="110" y="150" width="500" height="135" rx="14" class="itpe-svg-node is-current"></rect><text x="360" y="183" class="itpe-svg-title">대응 전략 선택</text><text x="360" y="216" class="itpe-svg-sub">회피 · 전가 · 완화 · 수용 · 상위보고</text><text x="360" y="250" class="itpe-svg-sub">관리 가능성 · 비용효과 · 위험 허용수준</text>
    <path d="M360 285 V325" class="itpe-svg-link" marker-end="url(#risk-arrow)"></path>
    <rect x="190" y="330" width="340" height="90" rx="14" class="itpe-svg-node"></rect><text x="360" y="363" class="itpe-svg-title">대응 실행</text><text x="360" y="391" class="itpe-svg-sub">책임자 · Trigger · 예비비 · 비상대책</text>
    <path d="M360 420 V460" class="itpe-svg-link" marker-end="url(#risk-arrow)"></path>
    <rect x="160" y="465" width="400" height="90" rx="14" class="itpe-svg-node"></rect><text x="360" y="498" class="itpe-svg-title">재평가</text><text x="360" y="526" class="itpe-svg-sub">잔여위험 · 2차위험 · 대응효과</text>
    <path d="M160 510 H75 V65 H185" class="itpe-svg-link" marker-end="url(#risk-arrow)"></path>
  </svg>
</div>

<details>
<summary>핵심 용어</summary>

- **P-I Matrix(Probability-Impact Matrix)**: 발생확률과 영향으로 위험의 상대적 우선순위를 판단하는 도구
- **EMV(Expected Monetary Value)**: 발생확률과 금전적 영향을 곱한 기대화폐가치
- **Risk Owner**: 위험을 감시하고 대응전략의 선택·실행을 책임지는 사람
- **Trigger**: 비상대책 실행 또는 상위보고를 시작하는 사전 정의 조건
- **Contingency Reserve**: 식별된 위험의 대응에 사용하는 예산·일정 예비량
- **Residual Risk**: 대응 후에도 남은 잔여위험
- **Secondary Risk**: 위험 대응으로 새롭게 발생한 2차위험

</details>

## 예상문제

> 프로젝트의 부정적 위험 대응 전략을 설명하고, 대응 실행 후 잔여위험과 2차위험의 관리방안을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 부정적 위험 대응 전략의 개요

> 대응전략의 목적은 위험을 없다고 선언하는 것이 아니라 **위험 노출도와 책임을 통제 가능한 상태로 만드는 것**임.

- 정의: 프로젝트 목표에 부정적 영향을 주는 불확실성에 대해 대응방식·책임자·실행조건·자원을 정하는 활동
- 목적: **위험 노출도 감소 · 의사결정 적시성 · 목표 보호**

## Ⅱ. 5대 대응 전략

> 하나의 위험에도 복수 전략을 조합할 수 있으며, 대응 후 위험도 다시 평가함.

| 전략 | 핵심 | 적용 예 |
|---|---|---|
| **회피(Avoid)** | 원인 제거·계획 변경으로 위협 제거 | 미검증 기술 제외 |
| **전가(Transfer)** | 제3자에게 책임·재무영향 배분 | 보험 · 보증 · 계약 |
| **완화(Mitigate)** | 발생확률·영향 감소 | PoC · 이중화 · 테스트 |
| **수용(Accept)** | 위험을 인정하고 감시·대비 | Trigger · 비상대책 · 예비비 |
| **상위보고(Escalate)** | 범위·권한 밖 위험을 상위 이관 | 법·예산·전사 정책 위험 |

## Ⅲ. 전략 선택 기준

> P-I 등급만으로 자동 결정하지 않고 관리 가능성과 비용효과를 함께 판단함.

| 판단 기준 | 확인 질문 | 의사결정 |
|---|---|---|
| **통제 가능성** | 원인·확률·영향을 바꿀 수 있는가? | 회피·완화 |
| **책임 배분** | 제3자가 더 잘 관리할 수 있는가? | 전가 |
| **비용효과** | 대응비용이 위험감소 편익에 부합하는가? | 완화·수용 조정 |
| **권한 범위** | 프로젝트 책임자가 결정할 수 있는가? | 상위보고 |
| **허용수준** | 대응 후 위험이 임계치 이내인가? | 수용 또는 추가 대응 |

## Ⅳ. 대응 계획·실행·재평가 절차

> 전략명보다 누가·언제·무엇으로 실행할지가 중요함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="부정적 위험 대응 계획과 실행 절차">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>① 위험 분석</strong><strong>활동</strong><span>원인·확률·영향·긴급성 평가</span><strong>산출</strong><span>Risk Register</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>② 전략 선정</strong><strong>활동</strong><span>대안·비용효과·권한 검토</span><strong>산출</strong><span>대응전략</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>③ 실행계획</strong><strong>활동</strong><span>Risk Owner·Trigger·자원 지정</span><strong>산출</strong><span>대응계획 · Contingency Plan</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>④ 실행·감시</strong><strong>활동</strong><span>대책 실행·상태·예비비 감시</span><strong>산출</strong><span>이슈·성과정보</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><div class="itpe-step-detail"><strong>⑤ 재평가</strong><strong>활동</strong><span>잔여·2차위험·대응효과 검토</span><strong>산출</strong><span>갱신 Risk Register</span></div></div>
</div>

## Ⅴ. 위협과 기회 대응 비교

> 불확실성의 방향은 다르지만 소유자·실행조건·감시는 공통임.

| 대응 목적 | 위협 | 기회 |
|---|---|---|
| 제거·확정 | 회피(Avoid) | 활용(Exploit) |
| 제3자 활용 | 전가(Transfer) | 공유(Share) |
| 확률·영향 조정 | 완화(Mitigate) | 증대(Enhance) |
| 현 상태 인정 | 수용(Accept) | 수용(Accept) |
| 권한 밖 이관 | 상위보고(Escalate) | 상위보고(Escalate) |

## Ⅵ. 문제점·대응책

> 대응책 자체가 새로운 위험을 만들 수 있으므로 실행 후 재평가가 필수임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **Risk Register 방치** | 정기 검토·Trigger 상태 갱신 | 대응 적시성 확보 |
| **전가 후 책임 공백** | 수용기준·SLA·감사권 명시 | 잔여 책임 명확화 |
| **수용 남용** | Risk Owner·비상대책·예비비 지정 | 수동 대응 방지 |
| **2차위험 누락** | 대응 실행 후 재식별·재평가 | 파생위험 통제 |

## Ⅶ. 잔여·2차위험 폐쇄루프 제언

`[핵심 통찰]` 대응전략은 위험의 종료 선언이 아니라 위험 노출도를 바꾸는 개입이므로, 실행 직후 잔여위험과 2차위험을 다시 등록해야 함.

`나라면` 각 위험에 Risk Owner·Trigger·대응예산·검증지표를 붙이고, Trigger 도달과 대응 실행 후 두 차례 재평가하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="잔여위험과 2차위험의 폐쇄루프 통제">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>문제</strong><span>대응 실행을 위험 종료로 오인</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>대책</strong><span>잔여·2차위험 재식별</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><div class="itpe-step-detail"><strong>판정</strong><span>노출도 · Trigger · 대응효과 · 예비비</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>효과</strong><span>위험책임·대응시점·잔여노출 명확화</span></div></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 프로젝트의 위협에 대해 대응방식·책임자·실행조건·자원을 정하는 위험 대응 활동
- 목적: **위험 노출도 감소 · 목표 보호**

### 2. 5대 전략

| 전략 | 핵심 |
|---|---|
| 회피 | 원인 제거·계획 변경 |
| 전가 | 제3자에게 책임·재무영향 배분 |
| 완화 | 발생확률·영향 감소 |
| 수용 | 감시·비상대책·예비비 |
| 상위보고 | 범위·권한 밖 위험 이관 |

### 3. 핵심 통제

- **실행성**: Risk Owner · Trigger · 자원 · 비상대책 지정
- **폐쇄루프**: 대응 후 Residual Risk·Secondary Risk 재평가

## 출제 이력과 검증 출처

- 제139회 정보관리기술사 1교시 4번: IT 프로젝트에서 발생할 수 있는 부정적 위험과 대응 전략
- [PMI: PMBOK Guide—Eighth Edition](https://www.pmi.org/standards/pmbok)
- [PMI: Lexicon of Project Management Terms](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf)
- [ISO: ISO 31000 Risk management](https://www.iso.org/iso-31000-risk-management.html)

## 학습 체크

- [ ] Ⅰ. 부정적 위험 대응의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ. 회피·전가·완화·수용·상위보고의 차이를 사례로 설명할 수 있는가?
- [ ] Ⅲ. 전략 선택 시 통제 가능성·비용효과·권한·허용수준을 판단할 수 있는가?
- [ ] Ⅳ. Risk Owner·Trigger·Contingency Plan을 연결할 수 있는가?
- [ ] Ⅴ~Ⅶ. 잔여위험과 2차위험의 폐쇄루프를 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [공공 SW 사업 발주·계약](./039_public_sw_contract.md)
- 연관 토픽: [프로젝트 위험관리](./009_project_risk_management_negative.md), [ISO 31000](./069_iso_31000.md), [정량적 위험분석](./073_quantitative_risk_analysis.md), [EVM](./032_evm.md)
- 다음 토픽: [DRS](./042_drs.md)
