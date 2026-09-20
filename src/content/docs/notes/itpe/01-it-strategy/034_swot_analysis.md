---
title: "SWOT 분석"
author: "Antigravity"
date: "2026-09-20T19:29:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash (High)"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 환경 및 역량 분석을 거쳐 SWOT 분석으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>환경·역량 분석</span>
  <strong>SWOT 분석</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **SWOT 분석(Strengths, Weaknesses, Opportunities, Threats)**은 내부 역량(강점·약점)과 외부 환경(기회·위협)을 객관적 사실 기반으로 분석하여 **TOWS 매트릭스**를 통해 4대 전략 대안을 도출하는 경영전략 프레임워크
- 메커니즘: 거시환경(**PEST**)과 산업경쟁(**5-Force**)으로 기회·위협을 식별하고 가치사슬과 **VRIO**로 강점·약점을 규명한 뒤 교차 결합(SO, ST, WO, WT)
- 산출: SWOT 4분면 매트릭스 · Cross-SWOT(TOWS) 전략 과제 · **AHP** 기반 우선순위 로드맵

<div class="itpe-flow-map" role="img" aria-label="SWOT 대내외 환경 분석부터 TOWS 교차 및 로드맵 수립 흐름">
  <div class="itpe-flow-node">
    <strong>대내외 팩트 데이터 수집</strong>
    <small>내부: 가치사슬 · VRIO / 외부: PEST · 5-Force</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>MECE 기반 팩트 분류</small></div>
  <div class="itpe-flow-node is-current">
    <strong>TOWS 교차 전략 매트릭스</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>SO</strong><span><span class="itpe-keyword"><strong>강점-기회</strong></span>: 공격적 시장 선점 및 신기술 투자</span></div>
      <div class="itpe-flow-branch"><strong>ST</strong><span><span class="itpe-keyword"><strong>강점-위협</strong></span>: 핵심 역량 레버리지 및 다각화 방어</span></div>
      <div class="itpe-flow-branch"><strong>WO</strong><span><span class="itpe-keyword"><strong>약점-기회</strong></span>: 파트너십 및 아웃소싱 통한 역량 보완</span></div>
      <div class="itpe-flow-branch"><strong>WT</strong><span><span class="itpe-keyword"><strong>약점-위협</strong></span>: 비핵심 자산 정리 및 리스크 회피</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>우선순위화 및 실행 과제 확정</small></div>
  <div class="itpe-flow-node">
    <strong>전략 실행 로드맵</strong>
    <small><span class="itpe-keyword"><strong>AHP</strong></span> 평가 · BSC 연계 KPI · WBS 프로젝트 배정</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **SWOT 분석(Strengths, Weaknesses, Opportunities, Threats)**: 기업 내부의 강점·약점과 외부의 기회·위협을 사실 기반으로 분석하여 전략 방향을 수립하는 프레임워크
- **TOWS 매트릭스(Threats, Opportunities, Weaknesses, Strengths Matrix)**: SWOT 요인을 상호 교차 매핑하여 SO, ST, WO, WT 4가지 실행 전략을 구체화하는 기법
- **PEST(Political, Economic, Social, Technological)**: 기업을 둘러싼 거시적 외부 환경 요인을 4가지 차원에서 분석하는 기법
- **5-Force**: 산업 내 경쟁 강도, 진입장벽, 대체재 위협, 공급자/구매자 교섭력을 평가하는 마이클 포터의 미시 산업 분석 모델
- **VRIO(Value, Rarity, Inimitability, Organization)**: 내부 자원의 가치, 희소성, 모방불가능성, 조직화를 평가하여 지속적 경쟁우위를 판단하는 모델
- **가치사슬(Value Chain)**: 기업의 주활동과 지원활동을 계층적으로 분석하여 내부 강점과 병목 약점을 식별하는 분석 기법
- **MECE(Mutually Exclusive, Collectively Exhaustive)**: 항목들이 상호 중복 없이 전체를 누락 없이 포괄하도록 구조화하는 논리적 분류 원칙
- **AHP(Analytic Hierarchy Process)**: 다수의 의사결정 기준과 전략 과제 간의 쌍대비교를 통해 정량적 우선순위를 도출하는 계층화 분석법
- **Strategic Fit(전략적 적합성)**: 외부 환경의 기회·위협과 조직 내부의 강점·약점 자원이 최적으로 정렬되는 상태

</details>

## 예상문제

> 기업의 정보전략계획(ISP) 수립 시 활용되는 SWOT 분석의 개념과 수행 절차를 설명하고, 4대 Cross-SWOT(TOWS) 전략 도출 메커니즘 및 단순 나열식 한계 극복을 위한 공학적 통제 방안을 논하시오. (25점)

## Ⅰ. 대내외 경영환경의 전략적 교차, SWOT 분석의 개요

> SWOT 분석은 주관적 브레인스토밍이 아닌 사실(Fact) 기반의 대내외 데이터를 교차하여 **Strategic Fit**을 달성하는 기법이며, 완성도는 **TOWS** 전략이 실제 **WBS** 과제로 연결되는 추적성으로 판정함.

- 정의: 조직 내부의 통제 가능한 강점(S)·약점(W)과 외부 환경의 기회(O)·위협(T)을 객관적 사실 기반으로 분석하여 **TOWS 매트릭스**를 통해 실행 전략을 도출하는 프레임워크
- 목적: 대내외 전략적 적합성 확보, 실행 가능한 전략 과제 도출

## Ⅱ. SWOT 분석 구성체계 및 5단계 추진 프로세스

> 대내외 팩트 데이터 수집에서 출발하여 MECE 분류를 거쳐 TOWS 교차 전략을 도출하고 AHP 기반의 우선순위 로드맵으로 완성함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="SWOT 분석 5단계 추진 프로세스 파이프라인">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>① 분석 범위 및 전략 목표 수립</strong></span>
      <span>분석 대상(전사/사업부/IT) 정의 · 전략적 지향점 확정 (분석 범위 정의서)</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>② 대내외 팩트 데이터 수집</strong></span>
      <span>외부 PEST/5-Force · 내부 VRIO/가치사슬 분석 데이터 집계 (대내외 환경 팩트북)</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>③ MECE 기반 SWOT 4분면 분류</strong></span>
      <span>통제 가능성 기준 엄격 적용 (내부=S/W, 외부=O/T) (SWOT 매트릭스 초안)</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>④ Cross-SWOT(TOWS) 교차 전략 도출</strong></span>
      <span>SO(공격), ST(방어), WO(보완), WT(철수) 1:1 교차 결합 (TOWS 교차 전략표)</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>⑤ 과제 우선순위화 및 로드맵 수립</strong></span>
      <span>AHP 쌍대비교 · 시급성/난이도 매트릭스 · BSC 연계 KPI 설정 (전략 과제 정의서 및 실행 로드맵)</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Strategic Traceability</strong></span> · 환경 분석 Fact부터 TOWS 전략 대안, WBS 실행 과제까지 일관된 양방향 추적</div>

## Ⅲ. Cross-SWOT(TOWS) 4대 전략 도출 매트릭스

> 강점·약점과 기회·위협을 교차 결합하여 4가지 방향의 실행 전략을 구체화함.

| 전략 유형 | 핵심 접근법 | 실행 질문 및 전략 방향 | 대표적 IT 실행 과제 |
|---|---|---|---|
| **SO 전략 (공격적 선점)** | 강점을 활용하여 시장 기회를 적극적으로 포착 | "우리의 핵심 역량으로 어떤 기회를 조기 장악할 것인가?" | 생성형 AI 기반 차별화 대고객 서비스 선제 개발 |
| **ST 전략 (다각화 및 방어)** | 내부 강점을 레버리지하여 외부 위협 요인 극복 | "글로벌 빅테크의 위협에 어떤 특화 강점으로 맞설 것인가?" | 데이터 주권 기반 온프레미스 보안 특화 거버넌스 구축 |
| **WO 전략 (보완적 우회)** | 외부 기회를 잡기 위해 내부 약점을 신속 보완 | "급증하는 시장 수요에 대응해 어떤 역량을 외부에서 조달할 것인가?" | 클라우드 네이티브 SaaS 도입을 통한 레거시 탈피 |
| **WT 전략 (방어적 철수)** | 내부 약점을 최소화하고 외부 위협을 피해 생존 | "가장 취약한 부분의 손실을 줄이기 위해 무엇을 정리할 것인가?" | 비수익 한계 정보시스템 일몰(Sun-setting) 및 아웃소싱 |

## Ⅳ. 전략 환경 분석 도구 비교 (SWOT vs 3C vs PEST vs 5-Force)

> PEST와 5-Force, 3C가 분석의 원천 재료를 제공하며, SWOT은 이를 종합 요리하는 통합 프레임워크로 작동함.

| 비교 항목 | SWOT 분석 | 3C 분석 | PEST 분석 | 5-Force 분석 |
|---|---|---|---|---|
| 분석 초점 | 내부 역량과 외부 환경의 종합적 교차 | 고객, 경쟁사, 자사의 3자 역학 관계 | 거시적 환경 (정치·경제·사회·기술) | 산업 내 미시적 경쟁 강도 및 매력도 |
| 공간 범위 | 내부 + 외부 (종합 매핑) | 내부 + 외부 (미시 시장 중심) | 외부 환경 전용 (거시 트렌드) | 외부 환경 전용 (산업 미시 생태계) |
| 주요 산출물 | SO, ST, WO, WT 4대 실행 전략 | 차별적 가치 제안 및 포지셔닝 | 기회/위협(O/T)의 거시적 배경 | 5대 경쟁 세력의 교섭력 평가 |
| SWOT과의 관계 | **최종 통합 프레임워크** | S/W 및 미시 O/T 도출의 핵심 입력 | 외부 O/T 도출의 거시적 팩트 원천 | 외부 O/T 도출의 산업 경쟁 팩트 원천 |

## Ⅴ. 실무 SWOT 분석의 실패 요인과 공학적 통제 방안

> 주관적 나열식 오류와 내외부 개념 혼동을 차단하지 못하면 SWOT은 공허한 말장난에 그침.

| 위험 | 대책 | 효과 |
|---|---|---|
| **단순 나열식 매몰** | 객관적 지표·통계 데이터 실증 및 핵심 요인 5개 이내 압축 | 각 요인별 객관적 증빙 데이터 확보율 100% |
| **내·외부 개념 혼동** | **통제 가능 여부(Controllability)** 기준 엄격 적용 | 조직 통제 가능=S/W, 통제 불가=O/T 분류 일치 |
| **우선순위 부재** | **AHP(계층화분석법)** 쌍대비교 및 2×2 매트릭스 적용 | 가중치 상위 핵심 과제 선별 완료 |
| **정적 분석의 한계** | 시나리오 플래닝 결합 및 분기별 SWOT 정기 롤링 | 분기별 환경 변화 반영 및 전략 업데이트 |

## Ⅵ. 실행 과제 연계 및 추적성 중심의 기술사적 제언

> SWOT의 가치는 4개 상자를 채우는 데 있지 않고, Cross 전략이 예산과 책임자가 명시된 프로젝트로 이어지는 데 있음.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 실무 ISP 컨설팅에서 SWOT이 비판받는 주된 이유는 누구나 알 만한 상식적 단어를 나열한 뒤 보고서용으로 방치하기 때문임. PEST와 가치사슬에서 뽑아낸 정량적 팩트를 바탕으로 TOWS 전략을 도출하고, 이를 BSC 관점의 KPI와 1:1로 매핑해야만 살아있는 전략이 됨.
- 나라면: 전략 계획 수립 시 `통제 가능성 기준에 따른 S/W와 O/T 분리 검증 → TOWS 전략별 AHP 가중치 부여 → 상위 3개 핵심 과제에 대해 담당 부서, 예산, 마일스톤(WBS) 강제 지정`을 전략 프레임워크의 완성 조건으로 확립하겠음.

### 실전 답안용 기술사적 제언

- 판정: 피상적 나열 탈피 및 객관적 팩트 기반 TOWS 실행 과제화
- 대안: **PEST/가치사슬-SWOT-TOWS-AHP** 4단계 연계 프레임워크 적용
- 검증: 통제 가능성 기반 분류 오류 0건 · 도출 과제-BSC KPI 1:1 매핑 완료
- 효과: 전략 수립의 객관성 확보 및 한정된 IT 자원의 최적 투자 집중

<div class="itpe-pipeline is-vertical" role="img" aria-label="SWOT 전략 프레임워크 제언 흐름">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>현행 한계</strong>
      <span>주관적 나열 · 내외부 개념 혼동 · 실행 과제 단절</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>개선 대안</strong>
      <span>통제 가능성 기준 MECE 분류 + TOWS 교차 + AHP 우선순위화</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>검증 기준</strong>
      <span>팩트북 연계율 100% · BSC 관점 전략 맵 추적성 확보</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>실행 효과</strong>
      <span>전략적 정합성(Strategic Fit) 달성 · 지속 가능한 경쟁 우위 확보</span>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **SWOT 분석(Strengths, Weaknesses, Opportunities, Threats)**은 내부 역량(강점·약점)과 외부 환경(기회·위협)을 객관적 사실 기반으로 분석하여 **TOWS 매트릭스**를 통해 실행 전략을 도출하는 경영전략 프레임워크
- 목적: 대내외 전략적 적합성 확보, 실행 가능한 전략 과제 도출

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="SWOT 분석 프로세스 요약">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>팩트 수집</strong>
      <span>PEST · 5-Force · 가치사슬</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>MECE 분류</strong>
      <span>통제 가능성 기준 S/W vs O/T</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>TOWS 교차</strong>
      <span>SO, ST, WO, WT 전략 도출</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>과제 확정</strong>
      <span>AHP 우선순위 및 로드맵 수립</span>
    </div>
  </div>
</div>

### 3. 핵심 통제

- **TOWS 4대 전략**: SO(공격적 선점), ST(다각화·차별화), WO(역량 보완), WT(리스크 회피·철수)
- **한계 극복**: 주관성 배제를 위한 팩트 기반 데이터 검증 및 **AHP(Analytic Hierarchy Process)** 가중치 평가 적용

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 1교시: SWOT 분석 및 전략 도출 방안
- 제99회, 제81회, 제80회 정보관리기술사 기출
- Michael E. Porter, [Competitive Strategy: Techniques for Analyzing Industries and Competitors](https://www.hbs.edu)
- ISO, [ISO 31000:2018, Risk management — Guidelines](https://www.iso.org)

## 학습 체크

- [ ] SWOT의 4가지 요소를 통제 가능 여부(내부/외부)와 영향(긍정/부정)의 2×2 축으로 구분할 수 있는가?
- [ ] SO, ST, WO, WT 4대 Cross 전략의 개념과 대표적 실행 과제를 설명할 수 있는가?
- [ ] PEST, 5-Force, 가치사슬 분석과 SWOT 간의 데이터 입력 및 통합 관계를 도식화할 수 있는가?
- [ ] 실무 SWOT의 한계인 단순 나열식을 극복하기 위한 공학적 통제 방안(AHP 등)을 서술할 수 있는가?

## 연결 토픽

- 이전 토픽: [IT 아웃소싱](./033_it_outsourcing.md)
- 연관 토픽: [경영환경 분석(SWOT·3C·PEST)](./088_swot_3c_pest.md), [ISP](./003_isp.md), [IT 투자평가](./016_it_investment_evaluation.md), [BSC](./017_bsc.md), [AHP](./075_ahp.md)
- 다음 토픽: [갈등관리](./035_conflict_management.md)
