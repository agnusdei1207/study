---
title: "프로젝트 위험관리"
author: "Codex"
date: "2026-09-20T23:30:30+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
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

<div class="itpe-pipeline is-vertical" role="img" aria-label="프로젝트 위험을 식별하고 분석하여 대응하고 다시 감시하는 흐름">
  <div class="itpe-pipeline-node"><strong>식별</strong><div class="itpe-step-detail"><strong>활동</strong><span>원인·불확실 사건·목표 영향 기술</span><strong>산출</strong><span>위험 등록부</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>분석</strong><div class="itpe-step-detail"><strong>활동</strong><span>발생확률·영향·긴급성 평가</span><strong>산출</strong><span>대응 우선순위</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><span class="itpe-keyword"><strong>대응</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>전략·책임자·트리거·조치 지정</span><strong>산출</strong><span>위험 대응계획</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>감시</strong><div class="itpe-step-detail"><strong>활동</strong><span>대응 효과·잔여 위험·2차 위험 점검</span><strong>산출</strong><span>갱신된 등록부 · 위험 보고서</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- `Project Risk Management`: 개별 위험과 전체 프로젝트 위험을 반복 식별·분석·대응·감시하는 관리 체계
- `Risk Register`: 식별된 위험·책임자·분석 결과·대응 내용을 추적하는 프로젝트 문서
- `Residual Risk`: 대응 후에도 남아 감시해야 하는 위험
- `Secondary Risk`: 위험 대응을 실행한 결과 새로 생기는 위험
- `Risk Owner`: 배정된 위험을 지속 감시하고 적절한 대응을 선택·관리하는 사람으로, 세부 조치는 별도 담당자가 실행할 수 있음

</details>

## 예상문제

> 프로젝트 위험관리의 개념과 프로세스를 설명하고, IT 프로젝트에서 발생할 수 있는 부정적 위험과 대응 전략을 제시하시오. (25점)

## Ⅰ. 불확실성을 의사결정 대상으로 바꾸는 위험관리

> 위험은 이미 발생한 이슈가 아니라 발생 여부가 불확실한 사건·조건이며, 위험관리 성패는 목록의 양이 아니라 목표 영향과 대응 책임의 명확성으로 판정함

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

> “일정 지연”처럼 결과만 적으면 대응할 수 없으므로, 원인·불확실 사건·목표 영향을 분리하고 Risk Owner와 트리거를 붙여야 함

| 요소 | 기록 | 판정 |
|---|---|---|
| **원인** | 공급 지연 · 기술 미성숙 · 의사결정 지체 | 통제 가능한 선행 조건 식별 |
| **사건** | 납품 실패 · 결함 급증 · 승인 지연 | 발생 여부가 불확실한 사건 |
| **영향** | 일정·원가·범위·품질 목표 편차 | 우선순위 결정 근거 |
| **통제** | Risk Owner · 트리거 · 대응기한 | 감시 책임·개시 조건 명시 |

## Ⅳ. 부정적 위험 대응 전략과 선택 기준

> 전략은 위험 이름에 기계적으로 붙이는 표가 아니라 위협의 책임 범위·발생확률·영향·수용 기준에 따라 선택하고, 대응 후 잔여·2차 위험까지 등록해야 함

| 전략 | 적용 판단 | 실행 방향 |
|---|---|---|
| **Avoid(회피)** | 위협 제거 또는 목표 보호 가능 | 원인·계획 변경으로 위협 제거 또는 목표를 영향에서 보호 |
| **Mitigate(완화)** | 확률·영향 감소 가능 | 예방·복구 통제로 노출 축소 |
| **Transfer(전가)** | 제3자가 책임 관리에 적합 | 계약·보험으로 책임 이전 |
| **Accept(수용)** | 노출이 허용 범위 안임 | 능동적 예비조치 또는 수동 관찰 |
| **Escalate(상향)** | 프로젝트 권한·범위 밖임 | 상위 조직에 관리 책임 이관 |

- 선택 순서: 먼저 프로젝트 권한·범위를 확인하여 벗어나면 **Escalate**, 내부 관리 대상이면 제거·목표 보호 가능성(**Avoid**), 제3자 관리 적합성(**Transfer**), 확률·영향 감소 가능성(**Mitigate**), 수용 기준 충족 여부(**Accept**)를 각각 검토함
- 조합 원칙: 위험별 주 전략과 Risk Owner를 명확히 하되, 노출 수준·비용효과에 따라 복수 전략과 세부 조치를 조합할 수 있음

## Ⅴ. IT 프로젝트 부정적 위험의 문제점·대응책

> 대응은 위험마다 주 전략과 책임자를 명확히 하고, 필요하면 복수 전략을 조합하며 대책 실행으로 생긴 잔여·2차 위험을 다시 분석해야 함

| 위험 | 대책 | 효과 |
|---|---|---|
| 핵심 기술 검증 실패 | PoC(Proof of Concept) 선행 · 대체 기술 전환 기준 | 전면 재작업 가능성 감소 |
| 외부 서비스 중단 | 다중 공급자 검토 · 복구 절차 시험 | 단일 의존 장애 영향 완화 |
| 요구사항 변경 누적 | 변경 영향 분석 · 승인된 Baseline 반영 | 무승인 범위 확대 억제 |
| 개인정보 유출 | 최소수집·접근통제 · 침해 대응훈련 | 노출 확률·피해 범위 축소 |

## Ⅵ. 등록부 사장화를 막는 감시·재평가

> 대응 실행 여부와 트리거를 주기적으로 확인하지 않으면 위험 등록부는 현황표로 멈추므로, 변화된 노출과 신규·잔여·2차 위험을 다시 의사결정해야 함

- 감시 대상: 대응 조치 상태 · 트리거 · 잔여 위험 · 2차 위험 · 신규 위험
- 갱신 대상: 발생확률·영향 · Risk Owner · 대응전략 · 조치기한
- 종료 기준: 위협 소멸 또는 수용 기준 이내 노출 확인·기록

## Ⅶ. 결론 — 트리거와 책임으로 작동시키는 위험관리

> 좋은 위험관리는 모든 위협을 제거하는 것이 아니라, 어떤 신호에서 누가 어떤 대응을 시작할지 사전에 결정하고 대응 효과를 증거로 재평가하는 것임

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 위험 등록부의 핵심은 위험 개수가 아니라 의사결정 가능성이다. 원인·사건·영향·트리거·책임자가 연결되지 않은 항목은 실행을 만들지 못한다.
- `나라면`: 핵심 위험부터 관측 가능한 트리거와 Risk Owner를 지정하고, 정기 점검에서 대응 실행·잔여 위험을 함께 검토하겠다.

### 실전 답안용 기술사적 제언

- 판정: 위험별 트리거·Risk Owner·대응기한·효과 검증의 연결성
- 대안: 핵심 위험의 선행지표·대응 조치·증적을 등록부에 통합
- 검증: 트리거 발생부터 대응 실행까지의 이력·잔여 위험 재평가
- 효과: 대응 지연·책임 공백·등록부 사장화 감소

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

| 전략 | 판정 | 조치 |
|---|---|---|
| **Avoid** | 위협 제거·목표 보호 가능 | 원인·계획 변경 |
| **Mitigate** | 노출 감소 가능 | 확률·영향 축소 |
| **Transfer** | 제3자 관리 적합 | 계약·보험으로 책임 이전 |
| **Accept** | 수용 기준 이내 | 예비조치·트리거 감시 |
| **Escalate** | 프로젝트 권한 밖 | 상위 조직으로 이관 |

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
- [ ] Ⅲ 기술 구조: 원인·위험 사건·영향과 Risk Owner·트리거·근거를 연결할 수 있는가?
- [ ] Ⅳ 대응: 5개 위협 대응전략을 권한·제거 가능성·제3자 적합성·노출 감소·수용 기준으로 구분할 수 있는가?
- [ ] Ⅴ 적용: IT 위험 4개에 위험·대책·효과를 대응시킬 수 있는가?
- [ ] Ⅵ 감시: 신규·잔여·2차 위험과 Risk Owner·트리거를 점검할 수 있는가?
- [ ] Ⅶ 결론: 트리거·책임·대응 이력·잔여 위험을 연결한 판정·대안·검증·효과를 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [정보시스템 감리](./008_it_audit.md)
- 연관 토픽: [WBS](./007_wbs.md), [PMO](./004_pmo.md), [위험 대응 전략](./040_negative_risk_response_strategy.md), [ISO 31000](./069_iso_31000.md)
- 다음 토픽: [BPR](./010_bpr.md)
