---
title: "프로젝트 위험관리"
author: "Claude Code"
date: "2026-09-21T12:40:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Claude Opus 5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="정보 전략과 관리에서 프로젝트 통제를 거쳐 프로젝트 위험관리로 이어지는 지식 위치">
  <span>정보 전략·관리</span>
  <span>프로젝트 통제</span>
  <strong>프로젝트 위험관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **프로젝트 위험관리(Project Risk Management)**는 아직 발생하지 않은 불확실성을 미리 찾아 목표에 미칠 위협은 줄이고 기회는 키우는 반복 통제
- 메커니즘: 계획 → 식별 → 정성·정량 분석 → 대응계획 → 대응 실행 → 감시·재식별
- 산출물: 위험관리 계획서 · **위험 등록부(Risk Register)** · 위험 보고서 · 대응 조치·잔여 위험

<div class="itpe-svg-map">
<svg viewBox="0 0 520 520" role="img" aria-label="위험 식별, 분석, 대응계획, 감시가 중앙 피드백 루프를 중심으로 같은 방향으로 순환하는 프로젝트 위험관리 고리">
  <defs><marker id="arrow-risk-cycle" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <path class="itpe-svg-link" d="M321 135 Q 390 136 395 199" marker-end="url(#arrow-risk-cycle)" />
  <path class="itpe-svg-link" d="M395 321 Q 390 384 321 385" marker-end="url(#arrow-risk-cycle)" />
  <path class="itpe-svg-link" d="M199 385 Q 130 384 125 321" marker-end="url(#arrow-risk-cycle)" />
  <path class="itpe-svg-link" d="M125 199 Q 130 136 199 135" marker-end="url(#arrow-risk-cycle)" />
  <circle class="itpe-svg-node" cx="260" cy="100" r="70" />
  <text class="itpe-svg-title" x="260" y="92">식별</text><text class="itpe-svg-sub" x="260" y="116">원인·사건·영향</text>
  <circle class="itpe-svg-node" cx="430" cy="260" r="70" />
  <text class="itpe-svg-title" x="430" y="252">분석</text><text class="itpe-svg-sub" x="430" y="276">확률·영향 평가</text>
  <circle class="itpe-svg-node" cx="260" cy="420" r="70" />
  <text class="itpe-svg-title" x="260" y="412">대응계획</text><text class="itpe-svg-sub" x="260" y="436">전략·책임자</text>
  <circle class="itpe-svg-node" cx="90" cy="260" r="70" />
  <text class="itpe-svg-title" x="90" y="252">감시</text><text class="itpe-svg-sub" x="90" y="276">잔여·2차 위험</text>
  <circle class="itpe-svg-node is-current" cx="260" cy="260" r="58" />
  <text class="itpe-svg-title" x="260" y="250">Feedback</text><text class="itpe-svg-title" x="260" y="274">Loop</text>
</svg>
</div>

<details>
<summary>핵심 용어</summary>

- **Project Risk Management(프로젝트 위험관리)**: 개별 위험과 전체 프로젝트 위험을 반복 식별·분석·대응·감시하는 관리 체계
- **Risk Register(위험 등록부)**: 식별된 위험·책임자·분석 결과·대응 내용을 추적하는 프로젝트 문서
- **Residual Risk(잔여 위험)**: 대응 후에도 남아 감시해야 하는 위험
- **Secondary Risk(2차 위험)**: 위험 대응을 실행한 결과 새로 생기는 위험
- **Risk Owner(위험 책임자)**: 위험을 감시하고 대응전략을 선택·관리하는 사람

</details>

## 예상문제

> IT 프로젝트에서 발생할 수 있는 부정적 위험(Negative Risk)과 대응 전략 (제139회 정보관리기술사 1교시)

- 심화 변형: 리스크 대응계획 수립 절차와 위협·기회 대응전략을 설명하시오. (제134회 정보관리기술사 4교시)

## Ⅰ. 불확실성을 의사결정 대상으로 바꾸는 위험관리

> 위험은 이미 발생한 **이슈**가 아니라 발생 여부가 **불확실한 사건·조건**이며, 위험관리 성패는 목록의 양이 아니라 목표 영향과 대응 책임의 명확성으로 판정함

- 정의: **프로젝트 위험관리(Project Risk Management)**는 프로젝트 목표에 긍정적·부정적 영향을 줄 수 있는 불확실한 사건·조건을 식별·분석·대응·감시하는 관리 활동
- 목적: 위협 노출 감소·기회 실현 가능성 증대
- 구분: 위험은 미래의 불확실성, 이슈는 이미 발생해 해결이 필요한 현재 문제

## Ⅱ. PMBOK 6th Edition의 7개 위험관리 프로세스

> 아래 7개 프로세스는 PMBOK Guide Sixth Edition 기준이며, 일회성 순서가 아니라 감시 결과로 새 위험을 식별하고 분석·대응을 반복하고 정량 분석은 프로젝트 필요에 따라 선택함

<div class="itpe-pipeline is-vertical" role="img" aria-label="PMBOK 프로젝트 위험관리 7개 프로세스">
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>① Plan Risk Management</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>방법·역할·범주·기준 정의</span><strong>산출</strong><span>위험관리 계획서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>② Identify Risks</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>개별 위험·원인·영향 식별</span><strong>산출</strong><span>위험 등록부 · 위험 보고서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>③ Perform Qualitative Risk Analysis</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>발생확률·영향 평가 · 우선순위 지정</span><strong>산출</strong><span>우선순위·Risk Owner</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>④ Perform Quantitative Risk Analysis</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>전체 목표 영향 수치 분석</span><strong>산출</strong><span>비용·일정 위험 분석 결과</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>⑤ Plan Risk Responses</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>전략·조치·책임자·트리거 결정</span><strong>산출</strong><span>대응계획 · 등록부 갱신</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>⑥ Implement Risk Responses</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>합의된 대응 실행</span><strong>산출</strong><span>조치 결과 · 변경 요청</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>⑦ Monitor Risks</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>대응 효과·잔여·2차·신규 위험 감시</span><strong>산출</strong><span>업무성과정보 · 문서 갱신</span></div></div>
</div>

## Ⅲ. 부정적 위험을 실행 가능하게 기술하는 구조

> “일정 지연”처럼 결과만 적으면 대응할 수 없으므로, **원인·불확실 사건·목표 영향**을 분리하고 **Risk Owner**와 **트리거**를 붙여야 함

<div class="itpe-svg-map">
<svg viewBox="0 0 520 560" role="img" aria-label="원인에서 불확실 사건, 목표 영향으로 이어지는 위험 기술 구조와 그 아래 Risk Owner·트리거·대응기한 세 가지 통제 분기">
  <defs><marker id="arrow-risk-statement" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <rect class="itpe-svg-node" x="50" y="10" width="420" height="86" rx="14" />
  <text class="itpe-svg-title" x="260" y="36">원인</text>
  <text class="itpe-svg-sub" x="260" y="60">공급 지연 · 기술 미성숙 · 의사결정 지체</text>
  <text class="itpe-svg-label" x="260" y="80">통제 가능한 선행 조건 식별</text>
  <path class="itpe-svg-link" d="M260 96 V 122" marker-end="url(#arrow-risk-statement)" />
  <rect class="itpe-svg-node" x="50" y="124" width="420" height="86" rx="14" />
  <text class="itpe-svg-title" x="260" y="150">사건</text>
  <text class="itpe-svg-sub" x="260" y="174">납품 실패 · 결함 급증 · 승인 지연</text>
  <text class="itpe-svg-label" x="260" y="194">발생 여부가 불확실한 사건</text>
  <path class="itpe-svg-link" d="M260 210 V 236" marker-end="url(#arrow-risk-statement)" />
  <rect class="itpe-svg-node" x="50" y="238" width="420" height="86" rx="14" />
  <text class="itpe-svg-title" x="260" y="264">영향</text>
  <text class="itpe-svg-sub" x="260" y="288">일정·원가·범위·품질 목표 편차</text>
  <text class="itpe-svg-label" x="260" y="308">우선순위 결정 근거</text>
  <path class="itpe-svg-link" d="M260 324 V 350" marker-end="url(#arrow-risk-statement)" />
  <rect class="itpe-svg-node is-current" x="50" y="352" width="420" height="52" rx="14" />
  <text class="itpe-svg-title" x="260" y="374">통제 3</text>
  <text class="itpe-svg-label" x="260" y="394">감시 책임·개시 조건 명시</text>
  <path class="itpe-svg-link" d="M260 404 V 416 H 90 V 528 M 90 440 H 120 M 90 484 H 120 M 90 528 H 120" />
  <rect class="itpe-svg-node" x="120" y="422" width="340" height="36" rx="10" />
  <text class="itpe-svg-sub" x="290" y="440">Risk Owner · 감시 책임자</text>
  <rect class="itpe-svg-node" x="120" y="466" width="340" height="36" rx="10" />
  <text class="itpe-svg-sub" x="290" y="484">트리거 · 대응 개시 조건</text>
  <rect class="itpe-svg-node" x="120" y="510" width="340" height="36" rx="10" />
  <text class="itpe-svg-sub" x="290" y="528">대응기한 · 조치 완료 시점</text>
</svg>
</div>

## Ⅳ. 부정적 위험 대응 전략과 선택 기준

> 전략은 위험 이름에 기계적으로 붙이는 표가 아니라 위협의 책임 범위·발생확률·영향·수용 기준에 따라 선택하고, 대응 후 잔여·2차 위험까지 등록해야 함

<div class="itpe-svg-map">
<svg viewBox="0 0 520 380" role="img" aria-label="위협 대응전략 다섯 가지를 권한 범위, 위협 제거, 제3자 관리, 확률·영향 감소, 수용 기준의 순서로 검토하는 선택 분기">
  <rect class="itpe-svg-node is-current" x="110" y="10" width="300" height="58" rx="14" />
  <text class="itpe-svg-title" x="260" y="32">위협 대응전략 5</text>
  <text class="itpe-svg-label" x="260" y="54">선택 판정 기준</text>
  <path class="itpe-svg-link" d="M260 68 V 80 H 70 V 344 M 70 104 H 100 M 70 164 H 100 M 70 224 H 100 M 70 284 H 100 M 70 344 H 100" />
  <rect class="itpe-svg-node" x="100" y="84" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="104">프로젝트 권한·범위 밖 → Escalate</text>
  <rect class="itpe-svg-node" x="100" y="144" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="164">위협 제거·목표 보호 가능 → Avoid</text>
  <rect class="itpe-svg-node" x="100" y="204" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="224">제3자 관리가 적합 → Transfer</text>
  <rect class="itpe-svg-node" x="100" y="264" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="284">확률·영향 감소 가능 → Mitigate</text>
  <rect class="itpe-svg-node" x="100" y="324" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="344">수용 기준 이내 → Accept</text>
</svg>
</div>

| 전략 | 적용 판단 | 실행 방향 |
|---|---|---|
| **Avoid(회피)** | 위협 제거 또는 목표 보호 가능 | 원인·계획 변경으로 위협 제거 또는 목표를 영향에서 보호 |
| **Mitigate(완화)** | 확률·영향 감소 가능 | 예방·복구 통제로 노출 축소 |
| **Transfer(전가)** | 제3자가 책임 관리에 적합 | 계약·보험으로 책임 이전 |
| **Accept(수용)** | 노출이 허용 범위 안임 | 능동적 예비조치 또는 수동 관찰 |
| **Escalate(상향)** | 프로젝트 권한·범위 밖임 | 상위 조직에 관리 책임 이관 |

- 조합 원칙: 위험별 주 전략과 Risk Owner를 명확히 하되, 노출 수준·비용효과에 따라 복수 전략과 세부 조치를 조합할 수 있음

## Ⅴ. IT 프로젝트 부정적 위험의 문제점·대응책

> 대응은 위험마다 주 전략과 책임자를 명확히 하고, 필요하면 복수 전략을 조합하며 대책 실행으로 생긴 **잔여·2차 위험**을 다시 분석해야 함

<div class="itpe-svg-map">
<svg viewBox="0 0 520 288" role="img" aria-label="IT 프로젝트 부정적 위험이 발생하는 기술·외부·요구사항·보안 네 영역과 공통 목표 영향">
  <rect class="itpe-svg-node is-current" x="60" y="8" width="400" height="58" rx="14" />
  <text class="itpe-svg-title" x="260" y="32">IT 프로젝트 위협 4</text>
  <text class="itpe-svg-label" x="260" y="54">목표 영향 · 일정·원가·범위·품질 편차</text>
  <path class="itpe-svg-link" d="M260 66 V 78 H 70 V 255 M 70 99 H 100 M 70 151 H 100 M 70 203 H 100 M 70 255 H 100" />
  <rect class="itpe-svg-node" x="100" y="80" width="400" height="38" rx="10" />
  <text class="itpe-svg-sub" x="300" y="99">기술 · 핵심 기술 검증 실패</text>
  <rect class="itpe-svg-node" x="100" y="132" width="400" height="38" rx="10" />
  <text class="itpe-svg-sub" x="300" y="151">외부 · 서비스 중단</text>
  <rect class="itpe-svg-node" x="100" y="184" width="400" height="38" rx="10" />
  <text class="itpe-svg-sub" x="300" y="203">요구사항 · 변경 누적</text>
  <rect class="itpe-svg-node" x="100" y="236" width="400" height="38" rx="10" />
  <text class="itpe-svg-sub" x="300" y="255">보안 · 개인정보 유출</text>
</svg>
</div>

| 위험 | 대책 | 효과 |
|---|---|---|
| 핵심 기술 검증 실패 | **PoC(Proof of Concept)** 선행 · 대체 기술 전환 기준 | 전면 재작업 가능성 감소 |
| 외부 서비스 중단 | 다중 공급자 검토 · 복구 절차 시험 | 단일 의존 장애 영향 완화 |
| 요구사항 변경 누적 | 변경 영향 분석 · 승인된 **Baseline** 반영 | 무승인 범위 확대 억제 |
| 개인정보 유출 | 최소수집·**접근통제** · 침해 대응훈련 | 노출 확률·피해 범위 축소 |

## Ⅵ. 등록부 사장화를 막는 감시·재평가

> 대응 실행 여부와 트리거를 주기적으로 확인하지 않으면 **위험 등록부**는 현황표로 멈추므로, 변화된 노출과 신규·잔여·2차 위험을 다시 의사결정해야 함

<div class="itpe-flow-map" role="img" aria-label="감시 대상을 모아 노출 수준을 재평가하고 수용 기준 통과 여부에 따라 종료와 갱신·재식별로 갈라지는 통제 흐름">
  <div class="itpe-flow-node">
    <strong>감시</strong>
    <div class="itpe-step-detail"><strong>대상</strong><span>대응 조치 상태 · 트리거 · 잔여 위험 · 2차 위험 · <span class="itpe-keyword"><strong>신규 위험</strong></span></span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>재평가</strong></span>
    <div class="itpe-step-detail"><strong>판정 질문</strong><span>남은 노출이 <span class="itpe-keyword"><strong>수용 기준</strong></span> 이내인가?</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass"><strong>통과</strong><span>위협 소멸·수용 기준 이내 확인 → 종료·기록</span></div>
    <div class="itpe-flow-branch is-fail"><strong>미통과</strong><span>발생확률·영향 · Risk Owner · 대응전략 · 조치기한 갱신 → 재식별</span></div>
  </div>
</div>

## Ⅶ. 결론 — 트리거와 책임으로 작동시키는 위험관리

> 좋은 위험관리는 모든 위협을 제거하는 것이 아니라, 어떤 신호에서 누가 어떤 대응을 시작할지 사전에 결정하고 대응 효과를 증거로 재평가하는 것임

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 위험 등록부의 핵심은 위험 개수가 아니라 의사결정 가능성이다. 원인·사건·영향·트리거·책임자가 연결되지 않은 항목은 실행을 만들지 못한다.
- `나라면`: 핵심 위험부터 관측 가능한 트리거와 Risk Owner를 지정하고, 정기 점검에서 대응 실행·잔여 위험을 함께 검토하겠다.

### 실전 답안용 기술사적 제언

- 판정: 등록된 위험 개수가 아니라 **트리거**·**Risk Owner**·대응 이력의 연결 여부가 성패를 가름
- 대안: 원인·사건·영향에 관측 가능한 트리거와 Risk Owner를 붙여 등록부를 의사결정 문서로 운영
- 검증: 대응 실행 이력과 잔여·2차 위험 재평가 기록의 존재 여부
- 효과: 위협이 이슈로 전환되기 전 대응 개시 · 감시 공백 제거

<div class="itpe-pipeline is-vertical" role="img" aria-label="작동하는 위험관리 개선 흐름">
  <div class="itpe-pipeline-node"><strong>현행 한계</strong><div class="itpe-step-detail"><strong>문제</strong><span>위험명·등급만 기록 · 실행 책임 불명확</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>개선안</strong><div class="itpe-step-detail"><strong>대안</strong><span>원인·사건·영향·트리거·Risk Owner 연결</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>검증 기준</strong><div class="itpe-step-detail"><strong>판정</strong><span>대응 실행 이력·잔여 위험 재평가</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>실행 효과</strong><div class="itpe-step-detail"><strong>효과</strong><span>위협의 이슈 전환 전 의사결정</span></div></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **부정적 위험(Negative Risk)**은 발생하면 프로젝트 목표에 부정적 영향을 주는 불확실한 사건·조건
- 목적: 위협 노출·프로젝트 목표 편차 가능성 감소

### 2. 부정적 위험 대응 전략

<div class="itpe-svg-map">
<svg viewBox="0 0 520 380" role="img" aria-label="위협 대응전략 다섯 가지를 권한 범위, 위협 제거, 제3자 관리, 확률·영향 감소, 수용 기준의 순서로 검토하는 선택 분기">
  <rect class="itpe-svg-node is-current" x="110" y="10" width="300" height="58" rx="14" />
  <text class="itpe-svg-title" x="260" y="32">위협 대응전략 5</text>
  <text class="itpe-svg-label" x="260" y="54">선택 판정 기준</text>
  <path class="itpe-svg-link" d="M260 68 V 80 H 70 V 344 M 70 104 H 100 M 70 164 H 100 M 70 224 H 100 M 70 284 H 100 M 70 344 H 100" />
  <rect class="itpe-svg-node" x="100" y="84" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="104">프로젝트 권한·범위 밖 → Escalate</text>
  <rect class="itpe-svg-node" x="100" y="144" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="164">위협 제거·목표 보호 가능 → Avoid</text>
  <rect class="itpe-svg-node" x="100" y="204" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="224">제3자 관리가 적합 → Transfer</text>
  <rect class="itpe-svg-node" x="100" y="264" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="284">확률·영향 감소 가능 → Mitigate</text>
  <rect class="itpe-svg-node" x="100" y="324" width="400" height="40" rx="10" />
  <text class="itpe-svg-sub" x="300" y="344">수용 기준 이내 → Accept</text>
</svg>
</div>

- 실행 방향: **Avoid(회피)** 원인·계획 변경 · **Mitigate(완화)** 예방·복구 통제 · **Transfer(전가)** 계약·보험 · **Accept(수용)** 예비조치·관찰 · **Escalate(상향)** 상위 조직 이관

### 3. 대응 후 통제

- Risk Owner·트리거·대응기한 지정
- 잔여 위험·2차 위험 재식별·등록
- 대응 효과 감시 후 전략 조정

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 4교시: "IT 프로젝트 관리에서 리스크 대응에 대하여 설명하시오."
  - 가. 리스크 대응 계획 수립 절차
  - 나. 위협에 대한 대응 전략
  - 다. 기회에 대한 대응 전략
- 제138회 정보관리기술사 1교시: "프로젝트 위험관리"
- 제139회 정보관리기술사 1교시: "IT 프로젝트에서 발생할 수 있는 부정적 위험(Negative Risk)과 대응 전략"
- [PMI, PMBOK Guide Sixth Edition](https://www.pmi.org/-/media/pmi/documents/public/pdf/pmbok-standards/pmbok-guide-6th-edition-5th-printing.pdf)
- [PMI Lexicon of Project Management Terms, Version 5.0](https://www.pmi.org/-/media/pmi/documents/registered/pdf/pmbok-standards/pmi-lexicon-pm-terms.pdf)
- [PMI, Risk Management in Portfolios, Programs, and Projects](https://www.pmi.org/standards/risk-management)

## 학습 체크

- [ ] Ⅰ 개요: 프로젝트 위험을 불확실한 사건·조건으로 정의하고 이슈와 구분할 수 있는가?
- [ ] Ⅱ 프로세스: PMBOK 6th Edition의 7개 프로세스와 반복 관계를 재현할 수 있는가?
- [ ] Ⅲ 기술 구조: 원인 → 사건 → 영향 사슬을 그리고 통제 3개(Risk Owner·트리거·대응기한)를 하위 분기로 붙일 수 있는가?
- [ ] Ⅳ 대응: 5개 위협 대응전략을 권한·제거 가능성·제3자 적합성·노출 감소·수용 기준의 선택 순서로 배열하고 실행 방향을 붙일 수 있는가?
- [ ] Ⅴ 적용: 기술·외부·요구사항·보안 4개 위협 영역에 대책과 효과를 1:1로 대응시킬 수 있는가?
- [ ] Ⅵ 감시: 감시 대상을 재평가 판정 질문에 연결하고 통과(종료·기록)·미통과(갱신·재식별) 분기를 재현할 수 있는가?
- [ ] Ⅶ 결론: 트리거·책임·대응 이력·잔여 위험을 연결한 판정·대안·검증·효과를 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [정보시스템 감리](./008_it_audit.md)
- 연관 토픽: [WBS](./007_wbs.md), [PMO](./004_pmo.md), [위험 대응 전략](./040_negative_risk_response_strategy.md), [ISO 31000](./069_iso_31000.md)
- 다음 토픽: [BPR](./010_bpr.md)
