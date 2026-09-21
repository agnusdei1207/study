---
title: "TAM-SAM-SOM"
author: "Antigravity"
date: "2026-09-22T07:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 사업 타당성 및 시장 분석을 거쳐 TAM-SAM-SOM으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>사업 타당성·시장 분석</span>
  <strong>TAM-SAM-SOM</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 거대 시장 착시를 배제하고 전체 시장(**TAM**)에서 유효 시장(**SAM**), 실제 점유 가능한 수익 시장(**SOM**)으로 좁히는 3단계 추정 모델
- 메커니즘: 전체 수요 정의 → 제품·지역·채널 제약 반영 → 자원·경쟁·영업역량 반영 → 상향식·하향식 교차검증
- 산출: 시장 경계 · 고객 세그먼트 · 시장규모 근거 · 점유 시나리오

<div class="itpe-svg-map" role="img" aria-label="TAM 안에 SAM, SAM 안에 SOM이 포함되는 시장 범위 모델">
  <svg viewBox="0 0 640 440" role="img" aria-label="TAM SAM SOM 중첩 시장 구조">
    <rect class="itpe-svg-node" x="40" y="30" width="560" height="360" rx="28" />
    <rect class="itpe-svg-node" x="110" y="105" width="420" height="245" rx="24" />
    <rect class="itpe-svg-node is-current" x="195" y="180" width="250" height="125" rx="22" />
    <text class="itpe-svg-title" x="320" y="70" text-anchor="middle">TAM</text>
    <text class="itpe-svg-sub" x="320" y="94" text-anchor="middle">전체 잠재시장</text>
    <text class="itpe-svg-title" x="320" y="145" text-anchor="middle">SAM</text>
    <text class="itpe-svg-sub" x="320" y="169" text-anchor="middle">서비스 가능시장</text>
    <text class="itpe-svg-title" x="320" y="230" text-anchor="middle">SOM</text>
    <text class="itpe-svg-sub" x="320" y="257" text-anchor="middle">현실적 획득시장</text>
    <text class="itpe-svg-label" x="320" y="285" text-anchor="middle">고객 수 × 단가 × 획득 가능성</text>
  </svg>
</div>

<details>
<summary>핵심 용어</summary>

- **TAM(Total Addressable Market)**: 특정 제품·서비스 카테고리가 해결 가능한 전 세계 또는 국내 시장의 이론적 최대 수요 총액
- **SAM(Serviceable Addressable Market)**: 자사의 비즈니스 모델, 제품 스펙, 유통 채널, 지리적 영역 내에서 실제 도달 가능한 유효 시장
- **SOM(Serviceable Obtainable Market)**: 자사의 경쟁력·채널·자원 제약을 반영하여 현실적으로 획득 가능한 시장
- **ARPU(Average Revenue Per User)**: 고객 또는 계정당 연간/월간 평균 결제 단가
- **CAC(Customer Acquisition Cost)**: 고객 1개사를 신규 획득하기 위해 소요되는 마케팅 및 영업 총비용
- **LTV(Customer Lifetime Value)**: 고객 1개사가 계약 유지 기간 동안 창출하는 총 기대 수익
- **Unit Economics**: 고객·계정 등 단위당 수익과 획득·서비스 비용을 비교하는 사업성 지표
- **BEP(Break-Even Point)**: 총매출이 고정비와 변동비의 합계와 일치하여 손익이 0이 되는 손익분기점

</details>

## 예상문제

> TAM·SAM·SOM의 개념과 추정방법을 설명하고, 시장규모 과대추정을 방지하기 위한 검증방안을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 시장 기획의 3단계 여과기, TAM-SAM-SOM의 개요

> 거대 시장의 착시를 걷어내고 **TAM(전체 시장)**에서 **SAM(유효 시장)**을 거쳐 **SOM(수익 시장)**으로 좁혀 단기 실행력을 확보함.

- 정의: 신규 IT 제품 및 디지털 서비스 기획 시 **TAM(Total Addressable Market)**, **SAM(Serviceable Addressable Market)**, **SOM(Serviceable Obtainable Market)**의 3단계 동심원으로 시장 규모를 단계별 여과 추정하는 **사업 타당성 분석 프레임워크**
- 목적: 시장 경계 명확화 · 과대추정 방지 · 실행 가능한 매출가설 수립

## Ⅱ. TAM-SAM-SOM 3단계 계층 구조 및 추정 체계

> 거시 통계에서 비즈니스 모델 제약, 영업 파이프라인 실측치로 좁혀가는 3단계 계층 파이프라인을 운영함.

### 1. 3단계 시장 여과 구조 및 추정 방식 교차검증

```xml
<svg-diagram>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="220" style="background:var(--sl-color-bg-sidebar);border:1px solid var(--sl-color-hairline);border-radius:8px;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--sl-color-text-accent)"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="15" y="24" fill="var(--sl-color-text)" font-size="13" font-weight="bold">TAM-SAM-SOM 3단계 여과 및 Top-Down / Bottom-Up 교차검증</text>

  <!-- Left: Concentric Circles (TAM, SAM, SOM) -->
  <g transform="translate(15, 45)">
    <!-- TAM Outer Circle/Box -->
    <rect x="0" y="0" width="220" height="155" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="8"/>
    <text x="110" y="20" fill="var(--sl-color-text)" font-size="11" font-weight="bold" text-anchor="middle">TAM (전체 시장)</text>
    <text x="110" y="34" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">글로벌/국내 전체 잠재 시장 규모</text>

    <!-- SAM Middle Box -->
    <rect x="25" y="45" width="170" height="100" fill="var(--sl-color-bg-sidebar)" stroke="var(--sl-color-text-accent)" stroke-width="1.5" rx="6"/>
    <text x="110" y="65" fill="var(--sl-color-text-accent)" font-size="11" font-weight="bold" text-anchor="middle">SAM (유효 시장)</text>
    <text x="110" y="78" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">자사 BM·솔루션 스펙 도달 시장</text>

    <!-- SOM Inner Box -->
    <rect x="50" y="90" width="120" height="50" fill="var(--sl-color-bg)" stroke="#ef4444" stroke-width="2" rx="4"/>
    <text x="110" y="112" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">SOM (획득 시장)</text>
    <text x="110" y="128" fill="var(--sl-color-text)" font-size="8" text-anchor="middle">실제 획득 가능 시장 (단기)</text>
  </g>

  <!-- Center Arrow -->
  <path d="M 245 120 L 265 120" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Right: Top-Down vs Bottom-Up Validation Box -->
  <g transform="translate(275, 45)">
    <rect x="0" y="0" width="230" height="155" fill="var(--sl-color-bg)" stroke="var(--sl-color-text-accent)" stroke-width="1.5" rx="6"/>
    <rect x="0" y="0" width="230" height="24" fill="var(--sl-color-text-accent)" opacity="0.1" rx="6 6 0 0"/>
    <text x="115" y="17" fill="var(--sl-color-text-accent)" font-size="11" font-weight="bold" text-anchor="middle">상향식 실측 및 단위 경제학 검증</text>

    <!-- Top-Down Note -->
    <text x="12" y="42" fill="var(--sl-color-text)" font-size="10" font-weight="bold">① 하향식(Top-Down) 한계선 설정</text>
    <text x="22" y="56" fill="var(--sl-color-text-muted)" font-size="9">• 산업 리포트 거시 통계 기반 천장(Ceiling) 파악</text>

    <!-- Bottom-Up Formula -->
    <text x="12" y="76" fill="var(--sl-color-text)" font-size="10" font-weight="bold">② 상향식(Bottom-Up) SOM 산출</text>
    <text x="22" y="90" fill="#ef4444" font-size="9" font-weight="bold">• SOM = 타깃 고객 수 × ARPU × 획득률</text>

    <!-- Unit Economics -->
    <text x="12" y="112" fill="var(--sl-color-text)" font-size="10" font-weight="bold">③ Unit Economics 수익성 검증</text>
    <text x="22" y="126" fill="var(--sl-color-text)" font-size="9">• <tspan fill="var(--sl-color-text-accent)" font-weight="bold">LTV > 3 × CAC</tspan> 만족 여부 확인</text>
    <text x="22" y="140" fill="var(--sl-color-text-muted)" font-size="8">• PoC 전환율 · 고객 이탈률(Churn) 실측 반영</text>
  </g>
</svg>
</svg-diagram>
```

### 2. 3단계 계층 상세 비교

<div class="itpe-pipeline is-vertical" role="img" aria-label="TAM-SAM-SOM 3단계 계층 구조 및 산출 체계">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>① TAM (Total Addressable Market: 전체 시장)</strong><span>산업 보고서 기준 이론적 최대 수요 총액 → 거시 통계 인용 · 잠재 모수 × 이상 단가</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>② SAM (Serviceable Addressable Market: 유효 시장)</strong><span>자사 BM · 솔루션 스펙 · 지리적 도달 가능 영역 → 타깃 세그먼트 고객 수 × 패키지 단가</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>③ SOM (Serviceable Obtainable Market: 획득 시장)</strong><span>경쟁력·채널·자원 제약 하 실제 획득 가능 시장 → 집중 고객 수 × 단가 × 획득 가능성</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>타당성 정합성</strong></span> · TAM의 범위에서 SAM 제약을 차감하고, SOM은 실제 영업·자원 근거로 검증</div>

| 계층 | 범위 | 산출 근거 |
|---|---|---|
| **TAM** | 제품군의 전체 잠재 수요 | 산업통계 · 잠재 고객 수 × 지출액 |
| **SAM** | 제품·지역·채널로 서비스 가능한 수요 | 타깃 고객 수 × 적용 가능한 단가 |
| **SOM** | 경쟁·자원 조건에서 획득 가능한 수요 | 영업 파이프라인 · 전환근거 · 단가 |

## Ⅲ. 하향식(Top-down) vs 상향식(Bottom-up) 추정 방법 비교

> 하향식으로 잠재 성장 한계선을 설정하고 상향식으로 즉시 실행 가능한 고객 단가를 도출해 교차 검증해야 함.

| 기준 | 하향식(Top-down) | 상향식(Bottom-up) |
|---|---|---|
| **입력** | 산업통계 · 시장보고서 | 고객 수 · 단가 · 전환근거 |
| **활용** | TAM·SAM의 잠재 범위 추정 | SOM의 실행 가능성 추정 |
| **한계** | 실제 획득역량 과대평가 | 초기 표본으로 시장 과소평가 |
| **보완** | 상향식 결과와 점유율 역검증 | 하향식 시장 경계와 교차검증 |

## Ⅳ. 문제점·대응책

> 단순 비율 곱셈을 금지하고 경쟁사 전환 장벽과 고객 획득 비용을 반영한 실증 모델을 구축해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **TAM 착시·부풀리기** | 제품·지역·채널 제약으로 SAM·SOM 범위 재산정 | 현실적 사업 목표 수립 |
| **고객 획득 비용 과소평가** | CAC·서비스원가·해지율을 함께 검토 | 수익성 왜곡 방지 |
| **정적 추정** | 실제 영업·전환 데이터를 반영해 주기적 갱신 | 예측 정확도 향상 |

## Ⅴ. 근거 기반 시장규모 검증을 위한 기술사적 제언

> SOM은 TAM의 임의 비율이 아니라 고객 목록·단가·채널·전환근거로 설명할 수 있어야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 투자 심사역이나 경영진이 가장 불신하는 사업계획서는 "전 세계 시장이 100조 원이니 1%만 해도 1조 원"이라는 논리임. TAM은 사업의 성장 한계선(Ceiling)을 보여주는 지표일 뿐이며, 사업의 생존을 결정하는 것은 철저히 바텀업으로 검증된 SOM임.
- 나라면: SOM을 고객 세그먼트별 수량·가격·전환가설로 산정하고 실제 영업결과와의 편차를 기록해 다음 추정에 반영하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 거시 보고서 단순 인용 여부 판정, 유닛 이코노믹스($LTV > 3 \times CAC$) 및 초기 손익분기점(BEP) 달성 가능성
- **대응 방안**: Top-down(성장 한계선)과 Bottom-up(실행 영업 모수)의 교차검증 체계 구축, 타깃 세그먼트별 실측 단가 적용
- **검증 체계**: 시장 경계 정의, 경쟁사 윈백 비용 반영, 분기별 실제 영업 전환율과 SOM 가설 간 편차 추적
- **기대 효과**: 시장 규모 과대 추정에 따른 데스밸리(Death Valley) 사전 예방, 자본 효율성 극대화 및 신규 IT 서비스 성공률 제고

<div class="itpe-pipeline is-vertical" role="img" aria-label="Unit Economics 연계 시장 타당성 검증 제언 흐름">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>현행 한계</strong><span>Gartner 보고서 단순 인용 · "1% 점유"식 과대 매출 추정 · CAC 간과</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>개선 대안</strong><span>고객 수·단가·전환근거 기반 상향식 SOM 도출</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>검증 기준</strong><span>실제 PoC 전환율 · 고객사 윈백 비용 반영 · Top-down 역검증 매핑</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>실행 효과</strong><span>현실적 BEP 달성 · 초기 자본 고갈(Death Valley) 극복 및 신규 사업 성공</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 신규 IT 사업 기획 시 전체 시장(**TAM**), 서비스 가능 유효 시장(**SAM**), 조기 실현 가능한 수익 시장(**SOM**)으로 시장 규모를 3단계 동심원으로 여과 추정하는 **사업 타당성 분석 프레임워크**
- 목적: 거대 시장 착시 배제 및 Unit Economics 기반 손익분기점(BEP) 달성

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="TAM-SAM-SOM 3단계 구성 요약">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>TAM (전체 시장)</strong><span>산업군 이론상 최대 총수요 (Top-down)</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>SAM (유효 시장)</strong><span>자사 BM · 스펙 부합 도달 시장 (Middle-out)</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>SOM (획득 시장)</strong><span>현실적 획득 가능: 고객 수 × 단가 × 획득 가능성</span></div></div>
</div>

### 3. 핵심 통제

- **추정 기법 교차 검증**: Top-down(잠재력 파악)과 Bottom-up(실행력 검증)의 상호 역대조
- **단위 경제성 통제**: CAC·LTV·서비스원가·해지율을 함께 검토하여 사업성 확인

## 출제 이력과 검증 출처

- 참고 문항: 제134회 출제 자료로 알려져 있으나 Q-Net 정보관리 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- Steve Blank & Bob Dorf, *The Startup Owner's Manual*

## 학습 체크

- [ ] TAM, SAM, SOM의 3단계 개념과 각각의 차이점을 설명할 수 있는가?
- [ ] Top-down 방식과 Bottom-up 방식의 산출 메커니즘을 비교할 수 있는가?
- [ ] Unit Economics(CAC, LTV)와 SOM 산출의 실무 연계 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [경영환경 분석(SWOT·3C·PEST)](./088_swot_3c_pest.md)
- 연관 토픽: [기술수용모델(TAM)](./092_technology_acceptance_model.md), [SW 비용 산정](./113_software_cost_estimation.md)
- 다음 토픽: [과업심의(과업변경·사업기간 적정성)](./091_public_sw_cost_and_scope_change_criteria.md)

