---
title: "정량적 위험분석"
author: "Codex"
date: "2026-09-20T19:32:00+09:00"
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
- 메커니즘: 3점 추정(낙관/최빈/비관)에 기초하여 **몬테카를로 시뮬레이션** 및 **EMV(Expected Monetary Value)**를 수행하고 **S-Curve**를 도출
- 산출: 누적 확률 분포 곡선(S-Curve) · 토네이도 다이어그램 · 비상예비비(Contingency Reserve)

<div class="itpe-flow-map" role="img" aria-label="정량적 위험분석 흐름 및 예비비 산출 구조">
  <div class="itpe-flow-node">
    <strong>정성적 분석 선별 (P-I Matrix)</strong>
    <small>확률-영향 매트릭스 기반 상위 고위험군 도출</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>3점 추정 및 확률분포 부여</small></div>
  <div class="itpe-flow-node is-current">
    <strong>정량적 위험분석 4대 기법</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>민감도</strong><span><span class="itpe-keyword"><strong>토네이도 다이어그램</strong></span> 기반 핵심 변수 우선순위</span></div>
      <div class="itpe-flow-branch"><strong>기댓값</strong><span><span class="itpe-keyword"><strong>EMV(기대화폐가치)</strong></span> = 발생확률(P) × 재무적 영향(I)</span></div>
      <div class="itpe-flow-branch"><strong>시뮬레이션</strong><span><span class="itpe-keyword"><strong>몬테카를로</strong></span> 반복 연산 및 누적 확률 S-Curve</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>신뢰수준(P80) 기준선 확정</small></div>
  <div class="itpe-flow-node">
    <strong>비상예비비 및 기준선 반영</strong>
    <small>P80 예산 - P50 예산 = 비상예비비(Contingency Reserve) 확보</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **EMV(Expected Monetary Value)**: 위험의 발생 확률(P)과 영향 금액(I)을 곱해 미래 손익의 통계적 기댓값을 산출하는 기법
- **Monte Carlo Simulation**: 불확실한 입력 변수에 확률분포를 할당하고 수천 번의 난수 연산을 통해 결과 분포를 도출하는 전산 시뮬레이션
- **Tornado Diagram**: 민감도 분석 결과를 변동 폭이 큰 순서대로 수평 막대로 배치하여 핵심 리스크를 식별하는 다이어그램
- **Decision Tree**: 의사결정 노드와 기회 노드의 분기별 조건부 확률 및 보상을 모델링하여 최적 경로를 선택하는 기법
- **Contingency Reserve(비상예비비)**: 식별된 기지-미지의 위험(Known-Unknowns)을 수용하기 위해 원가 및 일정 기준선에 포함되는 예비 자금
- **S-Curve(누적 확률 곡선)**: 몬테카를로 시뮬레이션 결과로 특정 예산 또는 일정 내에 프로젝트를 완공할 누적 확률을 나타낸 곡선

</details>

## 예상문제

> 대형 IT 프로젝트의 불확실성을 통제하기 위한 정량적 위험분석(Quantitative Risk Analysis)의 개념, 정성적 위험분석과의 차이점, 4대 핵심 분석 기법(민감도, EMV, 의사결정나무, 몬테카를로)을 설명하고, 몬테카를로 시뮬레이션 기반 비상예비비(Contingency Reserve) 산정 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **01-099 정량적 위험분석 기법** | 민감도 분석(토네이도), 기대화폐가치(EMV), 의사결정나무, 몬테카를로 시뮬레이션 4대 기법 | 본문 전반 (Ⅱ, Ⅲ, Ⅳ) |

## Ⅰ. 불확실성의 통계적 계량화, 정량적 위험분석의 개요

> 정량적 위험분석은 정성적 평가의 주관성을 극복하고 불확실성을 화폐 가치로 치환하며, 성패는 단순 최빈값(P50) 나열이 아닌 **통계적 신뢰수준(P80)**에 기반한 **비상예비비 확보**로 판정함.

- 정의: 정성적 분석에서 선별된 핵심 위험들이 프로젝트 전체 일정과 비용 목표에 미치는 영향을 **확률분포(Probability Distribution)**와 **몬테카를로 시뮬레이션(Monte Carlo Simulation)**을 통해 수치화하는 **위험 통제 활동**
- 목적: 주관적 편향을 배제하고 프로젝트 성공 확률 도출 → 수학적 근거 기반의 **비상예비비(Contingency Reserve)** 및 완충 일정 확정

## Ⅱ. 정량적 위험분석 4단계 실행 파이프라인

> 고위험 선별에서 데이터 확률분포 모델링, 컴퓨터 시뮬레이션, 베이스라인 확정으로 이어지는 엄밀한 수학적 파이프라인으로 전개됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="정량적 위험분석 4단계 실행 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 위험 선별 및 데이터 수집</strong></span>
    <small>P-I Matrix 상위 고위험 선별 · 유사 사업 실적 데이터 수집<br />→ 정량 분석 대상 위험 목록</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 확률분포 모델링 (3점 추정)</strong></span>
    <small>낙관치(O), 최빈치(M), 비관치(P) 추정 · 삼각/베타 분포 할당<br />→ 확률분포 매개변수 정의서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 시뮬레이션 연산 (Monte Carlo)</strong></span>
    <small>난수 발생 기반 수천 회 반복 시뮬레이션 · 민감도 분석 수행<br />→ 누적 확률 S-Curve · 토네이도 차트</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 비상예비비 및 베이스라인 확정</strong></span>
    <small>조직 위험 수용도(P80) 기준선 적용 · 비상예비비 확정<br />→ 원가/일정 기준선(Baseline) 갱신</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Contingency Reserve</strong></span> · P80(신뢰수준 80% 예산) - P50(단순 합산 예산) = 정량적 비상예비비 도출</div>

## Ⅲ. 정성적 위험분석 vs 정량적 위험분석 비교

> 정성 분석은 신속한 서열화에 적합하고, 정량 분석은 막대한 예산이 투입되는 의사결정에 필수적인 수치적 근거를 제공함.

| 비교 항목 | 정성적 위험분석 (Qualitative) | 정량적 위험분석 (Quantitative) |
|---|---|---|
| **분석 목적** | 위험의 빠른 우선순위 판정 및 스크리닝 | **전체 일정·비용의 복합적 재무 손실 수치화** |
| **측정 척도** | 서열 척도 (상/중/하, 1~5점 점수) | **비율 척도 (확률 %, 손실 금액, 지연 일수)** |
| **적용 기법** | **P-I 매트릭스(확률-영향)**, 위험 분류체계(RBS) | **몬테카를로 시뮬레이션, EMV, 토네이도 차트** |
| **분석 대상** | 식별된 모든 프로젝트 위험 | **정성 분석을 거쳐 선별된 핵심 고위험군** |
| **산출 결과** | 위험 우선순위 목록, 감시 목록(Watchlist) | **누적 확률 분포(S-Curve), 비상예비비 산출액** |

## Ⅳ. 정량적 위험분석 4대 핵심 기법

> 네 가지 기법은 상호 배타적인 것이 아니라, 민감도 분석으로 변수를 좁히고 EMV·의사결정나무로 대안을 평가하며 몬테카를로로 종합 예비비를 산정하는 보완 관계임.

| 분석 기법 | 핵심 메커니즘 | 실무 적용 역할 |
|---|---|---|
| **민감도 분석 (토네이도)** | 타 변수를 고정하고 특정 위험 변수의 변동 폭이 결과에 미치는 민감도 측정 | 프로젝트 성공을 좌우하는 최상위 핵심 리스크 식별 |
| **기대화폐가치 (EMV)** | 공식: `EMV = \sum (P_i \times I_i)` (확률 × 영향액) | 위협(-)과 기회(+)를 상계하여 순 기대 손익 계산 |
| **의사결정나무 분석** | 의사결정 노드(□)와 기회 노드(○)의 분기별 EMV를 비교 | 자체 개발 vs 상용 패키지 도입 등 전략적 대안 선정 |
| **몬테카를로 시뮬레이션** | 난수를 생성하여 수천 회 반복 연산 후 누적 확률 곡선 도출 | 신뢰수준(P80 등) 기반의 비상예비비 및 완료 확률 제시 |

## Ⅴ. 동적 비상예비비 거버넌스를 위한 기술사적 제언

> 사업 착수 시 1회 수행하는 정적 시뮬레이션은 무용지물이므로, 개발 진척 및 스프린트 실적과 연동된 동적 재산정 체계가 필수적임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 정량적 위험분석의 치명적인 함정은 '쓰레기를 넣으면 쓰레기가 나온다(GIGO)'는 점임. 실적 데이터가 없는 상태에서 개발자의 낙관적 3점 추정치만 넣으면 왜곡된 결과가 나옴. 과거 유사 프로젝트 실적 데이터를 기반으로 입력을 정규화하고, 프로젝트 진행에 따라 예비비를 동적으로 릴리즈(Release)해야 함.
- 나라면: ALM(형상관리) 및 이슈 트래커와 연동하여 `스프린트별 실제 결함 발생률과 일정 지연 데이터를 파이썬 몬테카를로 엔진에 자동 입력 → 마일스톤마다 잔여 비상예비비를 실시간 재산정`하는 동적 위험 관리 파이프라인을 구축하겠음.

### 실전 답안용 기술사적 제언

- 판정: 일회성 착수 보고용 문서화를 탈피하고 실시간 동적 예비비 통제 확립
- 대안: **CI/CD 파이프라인 연동 기반 동적 몬테카를로 시뮬레이션** 체계 구축
- 검증: **신뢰수준 P80 기준선** 준수율 및 단계별 예비비 소진율 추적 100%
- 효과: 근거 없는 예비비 과다 계상 방지 · 예산 초과(Cost Overrun) 리스크 원천 차단

<div class="itpe-pipeline is-vertical" role="img" aria-label="정량적 위험분석 동적 예비비 관리 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>주관적 3점 추정 편향 · 착수 시 1회성 분석 후 방치 · 예비비 단순 최빈값(P50) 의존</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>과거 실적 데이터 정규화 + 몬테카를로 P80 신뢰수준 기반 동적 예비비 거버넌스 수립</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>마일스톤별 위험 소멸에 따른 예비비 환수율 검증 · S-Curve 성공 확률 80% 유지</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>통계적 근거 기반 예산 편성 · 스폰서 신뢰성 확보 및 공정 지연 사전 예방</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 정성적 분석을 통해 선별된 핵심 위험들이 프로젝트 전체에 미치는 영향을 **확률분포**와 **몬테카를로 시뮬레이션**으로 수치화하는 **정량적 위험 평가 기법**
- 목적: 주관적 판단 배제 및 프로젝트 성공 확률 도출 → 객관적 근거 기반의 **비상예비비(Contingency Reserve)** 산정

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="정량적 위험분석 4단계 절차 요약">
  <div class="itpe-pipeline-node"><strong>위험 선별</strong><small>P-I Matrix 상위 고위험 항목 도출</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>분포 모델링</strong><small>3점 추정(낙관/최빈/비관) 및 삼각·베타 분포</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>시뮬레이션</strong><small>몬테카를로 난수 반복 연산 · S-Curve 도출</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>예비비 확정</strong><small>P80 신뢰수준 예산 - P50 예산 = 비상예비비</small></div>
</div>

### 3. 핵심 통제

- **민감도 분석(토네이도)**: 핵심 영향 인자를 시각적으로 도출하여 우선 통제
- **신뢰수준(P80) 적용**: 단순 최빈값(P50)의 50% 실패 확률을 극복하고 80% 신뢰선으로 안전마진 확보

## 출제 이력과 검증 출처

- 제123회 정보관리기술사(KPC) 1교시: 프로젝트 위험관리에서 정량적 위험분석의 개념, 필요성 및 분석 기법
- 제117회 2교시: 프로젝트 위험 분석 기법 및 몬테카를로 시뮬레이션
- PMI, [PMBOK Guide 7th Edition - Perform Quantitative Risk Analysis](https://www.pmi.org)
- ISO/IEC 31010, [Risk management - Risk assessment techniques](https://www.iso.org)

## 학습 체크

- [ ] 정성적 위험분석과 정량적 위험분석의 차이점을 척도, 기법, 산출물 관점에서 비교할 수 있는가?
- [ ] 민감도 분석(토네이도 차트)과 기대화폐가치(EMV)의 수식 및 메커니즘을 설명할 수 있는가?
- [ ] 몬테카를로 시뮬레이션의 난수 생성과 누적 확률 S-Curve 도출 원리를 설명할 수 있는가?
- [ ] P50과 P80을 비교하여 비상예비비(Contingency Reserve)를 산출하는 공학적 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [가치사슬](./072_value_chain.md)
- 연관 토픽: [프로젝트 위험관리](./009_project_risk_management_negative.md), [위험 대응 전략](./040_negative_risk_response_strategy.md), [ISO 31000](./069_iso_31000.md), [EVM](./032_evm.md)
- 다음 토픽: [AHP](./075_ahp.md)
