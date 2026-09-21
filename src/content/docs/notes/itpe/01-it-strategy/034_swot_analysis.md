---
title: "SWOT 분석"
author: "Antigravity"
date: "2026-09-21T18:15:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 환경 및 역량 분석을 거쳐 SWOT 분석으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>환경·역량 분석</span>
  <strong>SWOT 분석</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 조직 내부의 통제 가능한 강점·약점과 외부 통제 불가능한 기회·위협을 사실 기반으로 분석하여 전략적 적합성(**Strategic Fit**)을 달성하는 경영전략 프레임워크.
- 메커니즘: 팩트 수집(PEST·5-Force / VRIO·가치사슬) → **MECE** 분류 → **TOWS 4대 전략(SO·ST·WO·WT)** 교차 도출 → **AHP** 가중치 평가 기반 로드맵 및 WBS 연계.
- 통제: 주관적 나열 배제(Fact & Metric 명시) · 내/외부 통제 가능 여부(**Controllability**) 기준 엄격 적용 · 도출 전략의 WBS 실행 과제 추적성 확보.

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

> SWOT 분석의 개념과 수행절차를 설명하고, TOWS 전략 도출 및 단순 나열식 분석의 대응책을 제시하시오. **(미출제 예상·25점)**

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
      <strong>활동</strong><span>대상·기간·의사결정 목적 정의</span><strong>산출</strong><span>분석 범위</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>② 대내외 팩트 데이터 수집</strong></span>
      <strong>활동</strong><span>외부 PEST·5-Force · 내부 VRIO·가치사슬 분석</span><strong>산출</strong><span>환경·역량 근거</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>③ MECE 기반 SWOT 4분면 분류</strong></span>
      <strong>활동</strong><span>내부 S·W와 외부 O·T 분류</span><strong>산출</strong><span>SWOT 매트릭스</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>④ Cross-SWOT(TOWS) 교차 전략 도출</strong></span>
      <strong>활동</strong><span>SO·ST·WO·WT 조합별 대안 도출</span><strong>산출</strong><span>TOWS 전략대안</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>⑤ 과제 우선순위화 및 로드맵 수립</strong></span>
      <strong>활동</strong><span>효과·실행가능성·위험 평가</span><strong>산출</strong><span>우선과제 · 실행 로드맵</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Strategic Traceability</strong></span> · 환경 분석 Fact부터 TOWS 전략 대안, WBS 실행 과제까지 일관된 양방향 추적</div>

## Ⅲ. Cross-SWOT(TOWS) 4대 전략 도출 매트릭스

> 강점·약점과 기회·위협을 교차 결합하여 4가지 방향의 실행 전략을 구체화함.

<div class="itpe-diagram-box">
  <svg viewBox="0 0 520 220" width="100%" height="220" role="img" aria-label="TOWS 2x2 교차 전략 매트릭스 다이어그램">
    <!-- Outer Frame & Grid -->
    <rect x="20" y="20" width="480" height="185" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>
    <line x1="140" y1="20" x2="140" y2="205" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>
    <line x1="20" y1="65" x2="500" y2="65" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>
    <line x1="320" y1="20" x2="320" y2="205" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>
    <line x1="20" y1="135" x2="500" y2="135" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>

    <!-- Headers Top: External O & T -->
    <text x="80" y="47" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="10" font-weight="bold">구분 / 매핑</text>
    <text x="230" y="42" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="11" font-weight="bold">기회 (Opportunities, O)</text>
    <text x="230" y="57" text-anchor="middle" fill="var(--sl-color-gray-3)" font-size="8.5">시장 성장 · 신기술 등장 · 규제 완화</text>
    <text x="410" y="42" text-anchor="middle" fill="var(--sl-color-red-high)" font-size="11" font-weight="bold">위협 (Threats, T)</text>
    <text x="410" y="57" text-anchor="middle" fill="var(--sl-color-gray-3)" font-size="8.5">경쟁 심화 · 경기 침체 · 규제 강화</text>

    <!-- Headers Left: Internal S & W -->
    <text x="80" y="93" text-anchor="middle" fill="var(--sl-color-green-high)" font-size="11" font-weight="bold">강점 (S)</text>
    <text x="80" y="108" text-anchor="middle" fill="var(--sl-color-gray-3)" font-size="8.5">기술력·자본·브랜드</text>
    <text x="80" y="163" text-anchor="middle" fill="var(--sl-color-purple-high)" font-size="11" font-weight="bold">약점 (W)</text>
    <text x="80" y="178" text-anchor="middle" fill="var(--sl-color-gray-3)" font-size="8.5">인력부족·레거시·비용</text>

    <!-- Cell 1: SO Strategy -->
    <rect x="145" y="70" width="170" height="60" rx="4" fill="var(--sl-color-blue-low)"/>
    <text x="230" y="88" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="10.5" font-weight="bold">SO 전략 (공격적 선점)</text>
    <text x="230" y="104" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9">강점으로 기회를 극대화</text>
    <text x="230" y="118" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">신제품 출시 · 시장 선점 투자</text>

    <!-- Cell 2: ST Strategy -->
    <rect x="325" y="70" width="170" height="60" rx="4" fill="var(--sl-color-green-low)"/>
    <text x="410" y="88" text-anchor="middle" fill="var(--sl-color-green-high)" font-size="10.5" font-weight="bold">ST 전략 (다각화 및 방어)</text>
    <text x="410" y="104" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9">강점으로 외부 위협을 극복</text>
    <text x="410" y="118" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">사업 다각화 · 차별화 방어</text>

    <!-- Cell 3: WO Strategy -->
    <rect x="145" y="140" width="170" height="60" rx="4" fill="var(--sl-color-purple-low)"/>
    <text x="230" y="158" text-anchor="middle" fill="var(--sl-color-purple-high)" font-size="10.5" font-weight="bold">WO 전략 (보완적 우회)</text>
    <text x="230" y="174" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9">약점을 보완하여 기회를 포착</text>
    <text x="230" y="188" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">전략적 제휴 · 아웃소싱 조달</text>

    <!-- Cell 4: WT Strategy -->
    <rect x="325" y="140" width="170" height="60" rx="4" fill="var(--sl-color-red-low)"/>
    <text x="410" y="158" text-anchor="middle" fill="var(--sl-color-red-high)" font-size="10.5" font-weight="bold">WT 전략 (방어적 철수)</text>
    <text x="410" y="174" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9">약점을 최소화하고 위협 회피</text>
    <text x="410" y="188" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">비핵심 매각 · 한계사업 일몰</text>
  </svg>
</div>

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
| **단순 나열식 매몰** | 요인별 객관적 지표·근거 데이터 명시 | 검증 가능한 요인만 유지 |
| **내·외부 개념 혼동** | **통제 가능 여부(Controllability)** 기준 엄격 적용 | 조직 통제 가능=S/W, 통제 불가=O/T 분류 일치 |
| **우선순위 부재** | **AHP(계층화분석법)** 쌍대비교 및 2×2 매트릭스 적용 | 가중치 상위 핵심 과제 선별 완료 |
| **정적 분석의 한계** | 외부 환경 모니터링 주기화 및 반기별 롤링 갱신 | 동적 환경 변화 적시 대응 |

## Ⅵ. 실행 과제 연계 및 추적성 중심의 기술사적 제언

> SWOT의 가치는 4개 상자를 채우는 데 있지 않고, Cross 전략이 예산과 책임자가 명시된 프로젝트로 이어지는 데 있음.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]` SWOT의 약점은 4분면이 아니라 근거 없는 요인과 실행되지 않는 전략이며, TOWS 대안이 책임·자원·성과지표를 가진 과제로 전환되어야 가치가 생김.
- `나라면` 각 요인에 데이터 출처와 유효기간을 붙이고, TOWS 전략을 BSC 4대 관점 KPI 및 WBS 프로젝트로 일대일 매핑하여 분기별 실행률을 모니터링하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 도출된 TOWS 전략 과제가 전사 중장기 예산 및 WBS 작업 패키지로 100% 추적 가능한지 여부.
- **공학적 대안**: 정성적 나열 탈피, **AHP(쌍대비교)** 가중치 산정 + **BSC(Balanced Scorecard)** 연계 로드맵 수립.
- **검증 절차**: 통제 가능성(Controllability)에 의한 S/W vs O/T 분류 검증 및 MECE 교차 검토.
- **기대 효과**: 경영진 의사결정 신뢰도 제고, 대내외 Strategic Fit 달성 및 자원 배분의 최적화.

<div class="itpe-pipeline is-vertical" role="img" aria-label="SWOT 전략 프레임워크 제언 흐름">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>현행 한계</strong>
      <strong>문제</strong><span>주관적 나열 · 내외부 혼동 · 실행과제 단절</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>개선 대안</strong>
      <strong>대안</strong><span>근거·유효기간 부여 · TOWS 교차 · 다기준 평가</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>검증 기준</strong>
      <strong>판정</strong><span>요인 근거 · 전략 연결 · 책임자·자원 · 성과지표</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>실행 효과</strong>
      <strong>효과</strong><span>전략 정합성 · 우선순위 명확화 · 실행력 확보</span>
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

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [Harvard Business School: The Five Competitive Forces That Shape Strategy](https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-five-competitive-forces-that-shape-strategy.aspx)

## 학습 체크

- [ ] Ⅰ. SWOT의 정의·목적과 내부·외부 구분기준을 설명할 수 있는가?
- [ ] Ⅱ. 범위 정의부터 과제 우선순위까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ. SO·ST·WO·WT의 조합과 전략방향을 재현할 수 있는가?
- [ ] Ⅳ. SWOT·3C·PEST·5-Force의 분석범위와 산출을 비교할 수 있는가?
- [ ] Ⅴ~Ⅵ. 근거 없는 나열과 실행과제 단절의 대응책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [IT 아웃소싱](./033_it_outsourcing.md)
- 연관 토픽: [경영환경 분석(SWOT·3C·PEST)](./088_swot_3c_pest.md), [ISP](./003_isp.md), [IT 투자평가](./016_it_investment_evaluation.md), [BSC](./017_bsc.md), [AHP](./075_ahp.md)
- 다음 토픽: [갈등관리](./035_conflict_management.md)
