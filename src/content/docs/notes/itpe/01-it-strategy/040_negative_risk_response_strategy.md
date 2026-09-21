---
title: "부정적 위험 대응 전략"
author: "Antigravity"
date: "2026-09-21T19:45:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 위험관리를 거쳐 부정적 위험 대응 전략으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 위험관리</span>
  <strong>부정적 위험 대응 전략</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 프로젝트 목표 달성을 위협하는 부정적 리스크에 대해 영향도와 발생확률을 허용 한도 이내로 통제하기 위한 체계적 전략 수립 및 실행 관리 체계.
- 메커니즘: 위험 식별 및 정량/정성 평가(**P-I Matrix**) → 5대 대응 전략(**회피·전가·완화·수용·상위보고**) 수립 → **Risk Owner** 배정 및 **Trigger**(발동조건) 정의 → 실행 및 **잔여위험·2차위험(Secondary Risk)** 폐쇄 루프 재평가.
- 통제: 위험 전가 시 계약 SLA 명시 · 수용 시 비상대책(Contingency Plan) 및 예비비(Reserve) 확보 · 대응책 실행으로 파생되는 2차 위험 선제 감시.

<div class="itpe-flow-map" role="img" aria-label="부정적 위험 분석부터 대응과 재평가까지의 폐쇄 루프">
  <div class="itpe-flow-node">
    <strong>위험 식별 및 P-I 분석</strong>
    <small>원인 식별 · 발생 확률(P) 및 영향도(I) 평가 · 우선순위 도출</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>위험 노출도 및 권한 평가</small></div>
  <div class="itpe-flow-node is-current">
    <strong>5대 부정적 위험 대응 전략 선택</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>회피(Avoid)</strong><span>원인 제거 · 설계 변경 · 신기술 제외 (고P-고I)</span></div>
      <div class="itpe-flow-branch"><strong>전가(Transfer)</strong><span>보험 가입 · 전문 외주 위탁 · SLA 체결 (저P-고I)</span></div>
      <div class="itpe-flow-branch"><strong>완화(Mitigate)</strong><span>PoC 실증 · 이중화 · 코드리뷰 강화 (고P-저I)</span></div>
      <div class="itpe-flow-branch"><strong>수용(Accept)</strong><span>능동적(예비비 확보) / 수동적(관찰) (저P-저I)</span></div>
      <div class="itpe-flow-branch"><strong>상위보고(Escalate)</strong><span>프로젝트 권한 밖 전사/법적 위험 이관</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>Risk Owner 지정 및 Trigger 감시</small></div>
  <div class="itpe-flow-node">
    <strong>실행 및 잔여/2차 위험 재평가</strong>
    <small>Contingency Plan 실행 · 잔여위험(Residual) 및 2차위험(Secondary) 환류</small>
  </div>
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

| 전략 | 핵심 메커니즘 | 적용 대상 및 사례 |
|---|---|---|
| **회피 (Avoid)** | 프로젝트 계획을 변경하여 위험 원인을 원천 차단하거나 제거 | 미검증 신기술 제외, 요구사항 범위 축소, 공급사 교체 |
| **전가 (Transfer)** | 위험의 재무적·운영적 책임을 제3자에게 이전 (위험 자체 미제거) | 이행보증보험 가입, 고난도 인프라 전문 외주 위탁, SLA 위약금 |
| **완화 (Mitigate)** | 위험의 발생 확률이나 영향도를 허용 임계치 이하로 선제 감소 | 프로토타입(PoC) 사전 검증, 서버 이중화 구축, 조기 통합 테스트 |
| **수용 (Accept)** | 위험을 인정하고 능동적(예비비/비상대책) 또는 수동적으로 대기 | 우발사태 예비비(Contingency Reserve) 편성, 잔여 경미 위험 모니터링 |
| **상위보고 (Escalate)** | 프로젝트 관리자(PM) 권한 밖의 프로그램/포트폴리오/조직 차원 이관 | 법률·규제 위반 위험, 전사 사업 철수, 대규모 예산 삭감 |

## Ⅲ. P-I 매트릭스 기반 전략 선택 기준

> 발생확률(P)과 영향도(I)의 2축 평가를 기반으로 비용 효율적인 최적 전략을 도출함.

<div class="itpe-diagram-box">
  <svg viewBox="0 0 520 220" width="100%" height="220" role="img" aria-label="P-I 매트릭스 기반 5대 부정적 위험 대응 전략 다이어그램">
    <!-- Axes and Labels -->
    <line x1="80" y1="20" x2="80" y2="180" stroke="var(--sl-color-gray-4)" stroke-width="2"/>
    <line x1="80" y1="180" x2="480" y2="180" stroke="var(--sl-color-gray-4)" stroke-width="2"/>
    <text x="35" y="100" fill="var(--sl-color-gray-2)" font-size="10" font-weight="bold" transform="rotate(-90 40 100)">발생 확률 (Probability)</text>
    <text x="280" y="200" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="10" font-weight="bold">영향도 (Impact)</text>
    <text x="175" y="195" fill="var(--sl-color-gray-3)" font-size="9">낮음(Low)</text>
    <text x="375" y="195" fill="var(--sl-color-gray-3)" font-size="9">높음(High)</text>
    <text x="50" y="145" fill="var(--sl-color-gray-3)" font-size="9">낮음</text>
    <text x="50" y="55" fill="var(--sl-color-gray-3)" font-size="9">높음</text>

    <!-- Quadrant 1 (Top-Right): High P, High I -> Avoid -->
    <rect x="290" y="25" width="180" height="70" rx="5" fill="var(--sl-color-red-low)" stroke="var(--sl-color-red)" stroke-width="1.5"/>
    <text x="380" y="45" text-anchor="middle" fill="var(--sl-color-red-high)" font-size="11" font-weight="bold">회피 (Avoid)</text>
    <text x="380" y="62" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9.5">원인 원천 제거 · 범위 축소</text>
    <text x="380" y="78" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">프로젝트 계획 변경 필수</text>

    <!-- Quadrant 2 (Top-Left): High P, Low I -> Mitigate -->
    <rect x="90" y="25" width="180" height="70" rx="5" fill="var(--sl-color-blue-low)" stroke="var(--sl-color-blue)" stroke-width="1.5"/>
    <text x="180" y="45" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="11" font-weight="bold">완화 (Mitigate)</text>
    <text x="180" y="62" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9.5">확률/영향 선제 감소</text>
    <text x="180" y="78" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">PoC 실증 · 이중화 · 리뷰 강화</text>

    <!-- Quadrant 3 (Bottom-Right): Low P, High I -> Transfer -->
    <rect x="290" y="105" width="180" height="70" rx="5" fill="var(--sl-color-purple-low)" stroke="var(--sl-color-purple)" stroke-width="1.5"/>
    <text x="380" y="125" text-anchor="middle" fill="var(--sl-color-purple-high)" font-size="11" font-weight="bold">전가 (Transfer)</text>
    <text x="380" y="142" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9.5">제3자 책임 배분 · 위험 이전</text>
    <text x="380" y="158" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">보험 가입 · 외주 위탁 · SLA</text>

    <!-- Quadrant 4 (Bottom-Left): Low P, Low I -> Accept -->
    <rect x="90" y="105" width="180" height="70" rx="5" fill="var(--sl-color-green-low)" stroke="var(--sl-color-green)" stroke-width="1.5"/>
    <text x="180" y="125" text-anchor="middle" fill="var(--sl-color-green-high)" font-size="11" font-weight="bold">수용 (Accept)</text>
    <text x="180" y="142" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9.5">잔여 위험 인정 및 감시</text>
    <text x="180" y="158" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">예비비 확보 · Trigger 대기</text>

    <!-- Special: Escalate Band -->
    <rect x="360" y="1" width="115" height="20" rx="3" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1"/>
    <text x="417" y="14" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9" font-weight="bold">권한 초과 ➔ 상위보고</text>
  </svg>
</div>

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

| 대응 목적 | 위협 (Threat) | 기회 (Opportunity) |
|---|---|---|
| 제거·확정 | **회피 (Avoid)** | **활용 (Exploit)** |
| 제3자 활용 | **전가 (Transfer)** | **공유 (Share)** |
| 확률·영향 조정 | **완화 (Mitigate)** | **증대 (Enhance)** |
| 현 상태 인정 | **수용 (Accept)** | **수용 (Accept)** |
| 권한 밖 이관 | **상위보고 (Escalate)** | **상위보고 (Escalate)** |

## Ⅵ. 문제점·대응책

> 대응책 자체가 새로운 위험을 만들 수 있으므로 실행 후 재평가가 필수임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **Risk Register 방치** | 정기 주간 회의체 및 Trigger 상태 롤링 갱신 | 대응 적시성 확보 |
| **전가 후 책임 공백** | 외주 계약 시 수용기준·SLA·감사권 명시 | 잔여 책임 명확화 |
| **수용 남용** | Risk Owner 지정 및 비상대책·예비비(Contingency Reserve) 연계 | 수동 대응 방지 |
| **2차위험 누락** | 대응책 도입 즉시 2차위험 재식별 및 Risk Register 등록 | 파생위험 통제 |

## Ⅶ. 잔여·2차위험 폐쇄루프 제언

> 대응전략은 위험의 종료 선언이 아니라 위험 노출도를 바꾸는 개입이므로, 실행 직후 잔여위험과 2차위험을 다시 등록해야 함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]` 대응전략은 위험의 종료 선언이 아니라 위험 노출도를 바꾸는 개입이므로, 실행 직후 잔여위험과 2차위험을 다시 등록해야 함.
- `나라면` 각 위험에 Risk Owner·Trigger·대응예산·검증지표를 붙이고, Trigger 도달과 대응 실행 후 두 차례 재평가하여 예비비 소진율과 잔여 위험 노출도를 매주 경영진에게 가시화하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 대응 전략 실행 후 산출된 잔여 위험(Residual Risk) 노출도가 조직 허용 한도(Risk Tolerance) 이내인지 여부.
- **공학적 대안**: 정량적 P-I 평가 기반 5대 전략 매핑 및 대응책 도입으로 파생되는 **2차 위험(Secondary Risk)**의 동시 식별 체계 가동.
- **검증 절차**: 사전 정의된 **Trigger**(발동조건) 감시 및 비상대책(Contingency Plan)의 유효성을 도상 훈련으로 검증.
- **기대 효과**: 사후 수습형 장애 대응 탈피, 선제적 비용 최적화 및 프로젝트 성공률 극대화.

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
