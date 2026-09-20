---
title: "정량적 위험분석"
author: "Codex"
date: "2026-09-20T22:25:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 위험관리를 거쳐 정량적 위험분석으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 위험관리</span>
  <strong>정량적 위험분석</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **정량적 위험분석(Quantitative Risk Analysis)**은 선별된 핵심 위험들이 전체 프로젝트 목표에 미치는 영향을 확률과 금액으로 계량화하는 통계적 위험 평가 기법
- 메커니즘: 위험 데이터·가정 수집 → 민감도·기대화폐가치·의사결정나무·시뮬레이션 적용 → 비용·일정 분포와 대응 우선순위 결정
- 산출: 누적 확률 분포 곡선(S-Curve) · 토네이도 다이어그램 · 비상예비비(Contingency Reserve)

<div class="itpe-flow-map" role="img" aria-label="정량적 위험분석 흐름·예비비 산출 구조">
  <div class="itpe-flow-node">
    <strong>정성적 분석 선별 (P-I Matrix)</strong>
    <div class="itpe-step-detail"><strong>입력</strong><span>위험 등록부 · 비용·일정 추정치 · 상관관계</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>정량적 위험분석 4대 기법</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>민감도</strong><span><span class="itpe-keyword"><strong>토네이도 다이어그램</strong></span> 기반 핵심 변수 우선순위</span></div>
      <div class="itpe-flow-branch"><strong>기댓값</strong><span><span class="itpe-keyword"><strong>EMV(기대화폐가치)</strong></span> = 발생확률(P) × 재무적 영향(I)</span></div>
      <div class="itpe-flow-branch"><strong>시뮬레이션</strong><span><span class="itpe-keyword"><strong>몬테카를로</strong></span> 반복 연산 · 누적 확률 S-Curve</span></div>
      <div class="itpe-flow-branch"><strong>대안 평가</strong><span><span class="itpe-keyword"><strong>의사결정나무</strong></span> 분기별 확률·영향·EMV 비교</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>비상예비비·기준선 반영</strong>
    <div class="itpe-step-detail"><strong>산출</strong><span>목표 달성 확률 · 핵심 영향 변수 · 대안별 EMV · 예비비 근거</span></div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **EMV(Expected Monetary Value)**: 위험의 발생 확률(P)과 영향 금액(I)을 곱해 미래 손익의 통계적 기댓값을 산출하는 기법
- **Monte Carlo Simulation**: 불확실한 입력 변수에 확률분포를 할당하고 수천 번의 난수 연산을 통해 결과 분포를 도출하는 전산 시뮬레이션
- **Tornado Diagram**: 민감도 분석 결과를 변동 폭이 큰 순서대로 수평 막대로 배치하여 핵심 리스크를 식별하는 다이어그램
- **Decision Tree**: 의사결정 노드와 확률 노드의 분기별 조건부 확률·성과를 모델링하여 대안을 비교하는 기법
- **Contingency Reserve(비상예비비)**: 대응 전략이 있는 식별된 위험에 대해 일정 기준선에는 시간, 원가 기준선에는 자금을 배정한 예비분
- **S-Curve(누적 확률 곡선)**: 몬테카를로 시뮬레이션 결과로 특정 예산 또는 일정 내에 프로젝트를 완공할 누적 확률을 나타낸 곡선

</details>

## 예상문제

> 대형 IT 프로젝트의 불확실성을 통제하기 위한 정량적 위험분석(Quantitative Risk Analysis)의 개념, 정성적 위험분석과의 차이점, 4대 핵심 분석 기법(민감도, EMV, 의사결정나무, 몬테카를로)을 설명하고, 몬테카를로 시뮬레이션 기반 비상예비비(Contingency Reserve) 산정 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **01-099 정량적 위험분석 기법** | 민감도 분석(토네이도), 기대화폐가치(EMV), 의사결정나무, 몬테카를로 시뮬레이션 4대 기법 | 본문 전반 (Ⅱ, Ⅲ, Ⅳ) |

## Ⅰ. 불확실성의 통계적 계량화, 정량적 위험분석의 개요

> 정량적 위험분석의 신뢰성은 특정 신뢰수준을 고정하는 데 있지 않고 입력자료·분포·상관관계·가정을 투명하게 검증하는 데 있음.

- 정의: 선별된 위험이 프로젝트 목표에 미치는 영향을 **확률적·수치적 기법**으로 계량화하는 **위험 분석 활동**
- 목적: 비용·일정 목표 달성 가능성 추정 · 핵심 위험과 대응 우선순위 결정

## Ⅱ. 정량적 위험분석 4단계 실행 파이프라인

> 고위험 선별에서 데이터 확률분포 모델링, 컴퓨터 시뮬레이션, 베이스라인 확정으로 이어지는 엄밀한 수학적 파이프라인으로 전개됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="정량적 위험분석 4단계 실행 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 위험 선별·데이터 수집</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>정성 분석 결과·위험 등록부·유사 사업 실적 수집</span></div><div class="itpe-step-detail"><strong>산출</strong><span>분석 대상 위험·데이터 품질 기록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 확률분포 모델링 (3점 추정)</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>낙관치(O)·최빈치(M)·비관치(P), 상관관계·분포 설정</span></div><div class="itpe-step-detail"><strong>산출</strong><span>확률모형·가정 목록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 시뮬레이션 연산 (Monte Carlo)</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>몬테카를로 반복 표본추출·민감도 분석</span></div><div class="itpe-step-detail"><strong>산출</strong><span>누적분포·토네이도 다이어그램</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 결과 해석·의사결정</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>조직 위험선호에 따른 목표 신뢰수준·대응안 선택</span></div><div class="itpe-step-detail"><strong>산출</strong><span>예비비 근거·대응 우선순위</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Contingency Reserve</strong></span> · 조직이 정한 신뢰수준의 비용 분포와 기준 추정치 차이를 근거로 산정</div>

## Ⅲ. 정성적 위험분석 vs 정량적 위험분석 비교

> 정성 분석은 신속한 서열화에 적합하고, 정량 분석은 막대한 예산이 투입되는 의사결정에 필수적인 수치적 근거를 제공함.

| 비교 항목 | 정성적 위험분석 (Qualitative) | 정량적 위험분석 (Quantitative) |
|---|---|---|
| **분석 목적** | 위험의 빠른 우선순위 판정·스크리닝 | **전체 일정·비용의 복합적 재무 손실 수치화** |
| **적용 기법** | **P-I 매트릭스(확률-영향)**, 위험 분류체계(RBS) | **몬테카를로 시뮬레이션, EMV, 토네이도 차트** |
| **산출 결과** | 위험 우선순위 목록, 감시 목록(Watchlist) | **누적 확률 분포(S-Curve), 비상예비비 산출액** |

## Ⅳ. 정량적 위험분석 4대 핵심 기법

> 네 가지 기법은 상호 배타적인 것이 아니라, 민감도 분석으로 변수를 좁히고 EMV·의사결정나무로 대안을 평가하며 몬테카를로로 종합 예비비를 산정하는 보완 관계임.

| 분석 기법 | 핵심 메커니즘 | 실무 적용 역할 |
|---|---|---|
| **민감도 분석 (토네이도)** | 타 변수를 고정하고 특정 위험 변수의 변동 폭이 결과에 미치는 민감도 측정 | 프로젝트 성공을 좌우하는 최상위 핵심 리스크 식별 |
| **기대화폐가치 (EMV)** | 공식: `EMV = \sum (P_i \times I_i)` (확률 × 영향액) | 위협(-)과 기회(+)를 상계하여 순 기대 손익 계산 |
| **의사결정나무 분석** | 의사결정 노드(□)와 확률 노드(○)의 분기별 EMV 비교 | 자체 개발 vs 상용 패키지 도입 등 대안 선정 |
| **몬테카를로 시뮬레이션** | 입력 분포에서 반복 표본추출 후 결과 분포 도출 | 조직이 정한 신뢰수준의 비용·일정 목표 근거 제시 |

## Ⅴ. 동적 비상예비비 거버넌스를 위한 기술사적 제언

> 주요 가정이나 실적이 달라지면 분석모형과 예비비 근거를 다시 검토해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 정량적 위험분석의 치명적인 함정은 '쓰레기를 넣으면 쓰레기가 나온다(GIGO)'는 점임. 실적 데이터가 없는 상태에서 개발자의 낙관적 3점 추정치만 넣으면 왜곡된 결과가 나옴. 과거 유사 프로젝트 실적 데이터를 기반으로 입력을 정규화하고, 프로젝트 진행에 따라 예비비를 동적으로 릴리즈(Release)해야 함.
- 나라면: ALM(형상관리)·이슈 트래커와 연동하여 `스프린트별 실제 결함 발생률과 일정 지연 데이터를 파이썬 몬테카를로 엔진에 자동 입력 → 마일스톤마다 잔여 비상예비비를 실시간 재산정`하는 동적 위험 관리 파이프라인을 구축하겠음.

### 실전 답안용 기술사적 제언

- 판정: 일회성 분석 · 입력 가정 노후화 · 상관관계 누락
- 대안: **CI/CD 파이프라인 연동 기반 동적 몬테카를로 시뮬레이션** 체계 구축
- 검증: 입력 분포·상관관계·가정의 근거와 단계별 예비비 소진 추적
- 효과: 근거 없는 예비비 과다 계상 방지 · 예산 초과(Cost Overrun) 위험 완화

<div class="itpe-pipeline is-vertical" role="img" aria-label="정량적 위험분석 동적 예비비 관리 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>추정 편향 · 1회성 분석 · 입력 가정 노후화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>유사 사업 실적·상관관계 반영 · 마일스톤별 재분석</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>승인 신뢰수준 충족 여부 · 위험 소멸에 따른 예비비 환수</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>비용·일정 목표의 근거 강화 · 예비비 적시 조정</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 선별된 위험이 프로젝트 목표에 미치는 영향을 **확률적·수치적 기법**으로 계량화하는 **위험 분석 활동**
- 목적: 목표 달성 가능성 추정 · 대응 우선순위와 예비비 근거 마련

### 2. 구성체계·방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="정량적 위험분석 4단계 절차 요약">
  <div class="itpe-pipeline-node">
    <strong>위험 선별</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>위험 등록부·분석대상 선정</span></div><div class="itpe-step-detail"><strong>산출</strong><span>대상 위험·자료 목록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>분포 모델링</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>3점 추정·분포·상관관계 설정</span></div><div class="itpe-step-detail"><strong>산출</strong><span>확률모형·가정 목록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>시뮬레이션</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>반복 표본추출·민감도 분석</span></div><div class="itpe-step-detail"><strong>산출</strong><span>누적분포·핵심 영향변수</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>결과 해석</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>조직 위험선호에 따른 목표 신뢰수준 선택</span></div><div class="itpe-step-detail"><strong>산출</strong><span>비용·일정 목표·예비비 근거</span></div>
  </div>
</div>

## 출제 이력과 검증 출처

- Project Management Institute, [Risk by the Numbers](https://www.pmi.org/learning/library/quantitative-risk-analysis-approaches-balance-2296)
- 참고 문항: 제117회 타 종목 문항으로 전해지나 Q-Net 정보관리 공식 문제지 원문은 미확보하여 출제 이력으로 단정하지 않음
- ISO, [IEC 31010:2019 Risk management — Risk assessment techniques](https://www.iso.org/standard/72140.html)

## 학습 체크

- [ ] Ⅰ·Ⅱ: 정의와 입력 → 모델링 → 분석 → 의사결정 흐름을 재현할 수 있는가?
- [ ] Ⅲ: 정성·정량 분석을 목적·기법·산출의 3축으로 비교할 수 있는가?
- [ ] Ⅳ: 민감도·EMV·의사결정나무·몬테카를로의 역할을 구분할 수 있는가?
- [ ] Ⅴ: 입력 분포·상관관계·가정을 검증하고 조직 위험선호에 맞춘 예비비 통제를 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [가치사슬](./072_value_chain.md)
- 연관 토픽: [프로젝트 위험관리](./009_project_risk_management_negative.md), [위험 대응 전략](./040_negative_risk_response_strategy.md), [ISO 31000](./069_iso_31000.md), [EVM](./032_evm.md)
- 다음 토픽: [AHP](./075_ahp.md)
