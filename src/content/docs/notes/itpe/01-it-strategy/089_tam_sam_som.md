---
title: "TAM-SAM-SOM"
author: "Antigravity"
date: "2026-09-20T19:32:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "Gemini 3.8 Flash (High)"
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
- 메커니즘: 거시 잠재력 탐색(Top-down) → BM 부합 유효 고객 필터링(Middle-out) → 영업력·단가 기반 수익 산출(Bottom-up)
- 산출: TAM 거시 규모표 · SAM 타깃 고객 명세 · SOM 실행 매출 계획서 · **Unit Economics** 검증서

<div class="itpe-flow-map" role="img" aria-label="TAM 전체시장에서 SAM 유효시장과 SOM 수익시장으로 좁혀지는 3단계 시장 규모 추정 동심원 모델">
  <div class="itpe-flow-node">
    <strong>TAM (Total Addressable Market)</strong>
    <div class="itpe-step-detail"><span>전체 시장 · 산업군 내 이론적 최대 수요 총액 (Top-down)</span></div>
  </div>
  <div class="itpe-flow-arrow">↓<small>비즈니스 모델 및 서비스 도달 한계 필터링</small></div>
  <div class="itpe-flow-node">
    <strong>SAM (Serviceable Addressable Market)</strong>
    <div class="itpe-step-detail"><span>유효 시장 · 자사 솔루션 스펙 및 타깃 도달 가능 시장 (Middle-out)</span></div>
  </div>
  <div class="itpe-flow-arrow">↓<small>영업 파이프라인 및 초기 자원 제약 반영</small></div>
  <div class="itpe-flow-node is-current">
    <strong>SOM (Serviceable Obtainable Market)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>기간</strong><span>초기 1~3년 내 실제 점유 목표</span></div>
      <div class="itpe-flow-branch"><strong>방식</strong><span>고객 수 × <span class="itpe-keyword"><strong>ARPU</strong></span> × 획득률 (Bottom-up)</span></div>
      <div class="itpe-flow-branch"><strong>검증</strong><span><span class="itpe-keyword"><strong>Unit Economics</strong></span> (LTV/CAC ≥ 3)</span></div>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **TAM(Total Addressable Market)**: 특정 제품·서비스 카테고리가 해결 가능한 전 세계 또는 국내 시장의 이론적 최대 수요 총액
- **SAM(Serviceable Addressable Market)**: 자사의 비즈니스 모델, 제품 스펙, 유통 채널, 지리적 영역 내에서 실제 도달 가능한 유효 시장
- **SOM(Serviceable Obtainable Market)**: 초기 1~3년 내 자사의 인력, 자본, 마케팅 자원 제약 하에서 현실적으로 점유 가능한 수익 시장
- **ARPU(Average Revenue Per User)**: 고객 또는 계정당 연간/월간 평균 결제 단가
- **CAC(Customer Acquisition Cost)**: 고객 1개사를 신규 획득하기 위해 소요되는 마케팅 및 영업 총비용
- **LTV(Customer Lifetime Value)**: 고객 1개사가 계약 유지 기간 동안 창출하는 총 기대 수익
- **Unit Economics**: 단위 고객당 수익성 지표로, 건강한 성장을 위해 통상 $LTV/CAC \ge 3$을 충족해야 함
- **BEP(Break-Even Point)**: 총매출이 고정비와 변동비의 합계와 일치하여 손익이 0이 되는 손익분기점

</details>

## 예상문제

> 신규 IT 서비스 사업 기획 및 투자 유치 시 활용되는 시장 규모 추정 프레임워크인 TAM-SAM-SOM의 개념, 3단계 동심원 계층 구조, 하향식(Top-down) 및 상향식(Bottom-up) 추정 방법과 실무 적용 방안을 설명하시오. (10점/25점)

## Ⅰ. 시장 기획의 3단계 여과기, TAM-SAM-SOM의 개요

> 거대 시장의 착시를 걷어내고 **TAM(전체 시장)**에서 **SAM(유효 시장)**을 거쳐 **SOM(수익 시장)**으로 좁혀 단기 실행력을 확보함.

- 정의: 신규 IT 제품 및 디지털 서비스 기획 시 **TAM(Total Addressable Market)**, **SAM(Serviceable Addressable Market)**, **SOM(Serviceable Obtainable Market)**의 3단계 동심원으로 시장 규모를 단계별 여과 추정하는 **사업 타당성 분석 프레임워크**
- 목적: 비현실적 과대 추정 방지 및 단위 경제성(Unit Economics) 기반 객관적 손익분기점(BEP) 달성

## Ⅱ. TAM-SAM-SOM 3단계 계층 구조 및 추정 체계

> 거시 통계에서 비즈니스 모델 제약, 영업 파이프라인 실측치로 좁혀가는 3단계 계층 파이프라인을 운영함.

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
    <div class="itpe-step-detail"><strong>③ SOM (Serviceable Obtainable Market: 수익 시장)</strong><span>초기 1~3년 내 인력·자본 제약 하 실제 점유 시장 → 집중 고객 수 × ARPU × 현실 획득률</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>타당성 정합성</strong></span> · TAM(잠재 한계) ↔ SAM(전략 목표) ↔ SOM(실행 검증: LTV/CAC ≥ 3)</div>

### 3단계 계층 상세 비교표

| 계층 구분 | 개념 및 정의 | 산출 공식 및 기준 | IT 실무 적용 예시 (엔터프라이즈 AI FinOps) |
|---|---|---|---|
| **TAM** | 제품 카테고리가 해결 가능한 이론적 최대 전체 시장 규모 | 전체 잠재 고객 수 × 이상적 연간 지출액 (Gartner/IDC) | 전 세계 클라우드 비용 관리 및 FinOps 시장 (약 50조 원) |
| **SAM** | 자사 솔루션 스펙 및 지리적 도달 범위 내의 유효 시장 | 타깃 고객군 수 × 연간 라이선스 패키지 단가 | 국내 금융·제조 엔터프라이즈 FinOps 시장 (약 3,000억 원) |
| **SOM** | 초기 1~3년 내 영업 인력과 채널로 실제 확보 가능한 수익 시장 | 타깃 집중 고객 수 × **ARPU(Average Revenue Per User)** × 획득률 | 국내 Tier-1 금융사 50개 중 20% 점유 (약 50억 원) |

## Ⅲ. 하향식(Top-down) vs 상향식(Bottom-up) 추정 방법 비교

> 하향식으로 잠재 성장 한계선을 설정하고 상향식으로 즉시 실행 가능한 고객 단가를 도출해 교차 검증해야 함.

| 비교 항목 | 하향식 추정 (Top-down) | 상향식 추정 (Bottom-up) | 가치 기반 추정 (Value Theory) |
|---|---|---|---|
| **추정 기준** | 공신력 있는 시장 통계 리포트 (Gartner, IDC) | 실제 영업 데이터 (**고객 수 × ARPU × 전환율**) | 고객이 솔루션으로 얻는 비용 절감액의 일정 % |
| **주요 활용** | **TAM** 산출, 투자자 대상 장기 비전 제시 | **SOM** 산출, 분기별 영업 및 손익(BEP) 계획 | 시장이 없는 파괴적 신기술 TAM 산출 |
| **핵심 장점** | 적은 공수로 전체 시장 잠재력 조망 용이 | 높은 현실 실현 가능성 및 객관적 검증 가능 | 솔루션의 고유 경제적 가치(ROI) 직접 대변 |
| **치명적 맹점** | "1% 법칙의 오류"(실제 획득 역량과 무관) | 초기 표본 부족 시 전체 확장성 과소평가 위험 | 고객사별 ROI 편차로 단가 표준화 난항 |
| **상호 보완책** | **상향식 SOM 집계 결과를 하향식 SAM/TAM에 역대조하여 현실적 시장 점유율(%) 정합성 검증** |

## Ⅳ. 실무 적용 시 주요 왜곡 요인과 통제 대책

> 단순 비율 곱셈을 금지하고 경쟁사 전환 장벽과 고객 획득 비용을 반영한 실증 모델을 구축해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **TAM 착시 및 부풀리기** | OS 환경, 온프레미스/클라우드 등 스펙 제약으로 SAM/SOM 여과 의무화 | 현실적 사업 목표 수립 및 투자 왜곡 차단 |
| **고객 획득 비용(CAC) 과소평가** | 경쟁사 윈백 비용 및 영업 공수를 반영한 **Unit Economics ($LTV/CAC \ge 3$)** 통제 | 영업 마진율 및 현금흐름 건전성 확보 |
| **정적 추정의 한계** | 몬테카를로 시뮬레이션 기반 시나리오별(Best/Worst) SOM 동적 갱신 | 환경 변화 대응력 및 회복탄력성 확보 |

## Ⅴ. Unit Economics 연계 시장 타당성 검증을 위한 기술사적 제언

> 공허한 TAM 나열을 지양하고 LTV/CAC 비율이 3 이상인 검증된 세그먼트만을 SOM으로 산정해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 투자 심사역이나 경영진이 가장 불신하는 사업계획서는 "전 세계 시장이 100조 원이니 1%만 해도 1조 원"이라는 논리임. TAM은 사업의 성장 한계선(Ceiling)을 보여주는 지표일 뿐이며, 사업의 생존을 결정하는 것은 철저히 바텀업으로 검증된 SOM임.
- 나라면: SOM 산정 시 단순 비율 가정을 배제하고, [고객 생애 가치(LTV) / 고객 획득 비용(CAC)] 비율이 3 이상이고 회수 기간(Payback Period)이 12개월 이내인 고객군만을 SOM 모수로 편입하는 'Unit Economics 연계 SOM 산정 기준'을 의무화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 거시 시장 보고서 인용 위주에서 바텀업 실측 단가와 Unit Economics 검증으로 전환
- 대안: **Unit Economics(LTV/CAC ≥ 3) 기반 SOM 정밀 추정 모델** 확립
- 검증: Top-down 거시 점유율과 Bottom-up 고객 수 교차 일치 · Payback Period ≤ 12개월
- 효과: 과대 투자 예방 · 현실적 손익분기점(BEP) 달성 및 자본 효율성 극대화

<div class="itpe-pipeline is-vertical" role="img" aria-label="Unit Economics 연계 시장 타당성 검증 제언 흐름">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>현행 한계</strong><span>Gartner 보고서 단순 인용 · "1% 점유"식 과대 매출 추정 · CAC 간과</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>개선 대안</strong><span>Bottom-up 기반 SOM 도출 + LTV/CAC ≥ 3 및 회수기간 12개월 필터링</span></div>
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
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>SOM (수익 시장)</strong><span>초기 1~3년 실제 점유: 고객 수 × ARPU (Bottom-up)</span></div></div>
</div>

### 3. 핵심 통제

- **추정 기법 교차 검증**: Top-down(잠재력 파악)과 Bottom-up(실행력 검증)의 상호 역대조
- **단위 경제성 통제**: $LTV/CAC \ge 3$을 충족하는 세그먼트만 SOM으로 인정하여 사업 건전성 확보

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 1교시: 신규 사업 기획 시 활용되는 시장 규모 추정 기법인 TAM-SAM-SOM의 개념 및 특징
- [중소벤처기업부, 기술창업 및 신사업 타당성 분석 가이드라인](https://www.mss.go.kr)
- [Steve Blank, The Startup Owner's Manual: The Step-By-Step Guide for Building a Great Company](https://steveblank.com)

## 학습 체크

- [ ] TAM, SAM, SOM의 3단계 개념과 각각의 차이점을 설명할 수 있는가?
- [ ] Top-down 방식과 Bottom-up 방식의 산출 메커니즘을 비교할 수 있는가?
- [ ] Unit Economics(CAC, LTV)와 SOM 산출의 실무 연계 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [경영환경 분석(SWOT·3C·PEST)](./088_swot_3c_pest.md)
- 연관 토픽: [기술수용모델(TAM)](./092_technology_acceptance_model.md), [SW 비용 산정](./113_software_cost_estimation.md)
- 다음 토픽: [과업심의(과업변경·사업기간 적정성)](./091_public_sw_cost_and_scope_change_criteria.md)
