---
title: "가치사슬(Value Chain)"
author: "Antigravity"
date: "2026-09-22T04:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  keyword_grade: "C"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 경영 전략·비즈니스 아키텍처를 거쳐 가치사슬로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>경영 전략·비즈니스 아키텍처</span>
  <strong>가치사슬(Value Chain)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **가치사슬(Value Chain)**은 기업을 전략적으로 중요한 활동으로 분해해 원가우위·차별화의 원천을 찾는 분석 틀
- 메커니즘: 본원적 활동·지원 활동 분해 → 활동별 비용·가치 동인 확인 → 활동 간 **연계(Linkage)** 재설계
- 산출물: 가치활동 지도 · 비용·차별화 동인 · 개선 우선순위

<div class="itpe-flow-map" role="img" aria-label="가치사슬 9대 활동·IT 솔루션 매핑 흐름">
  <div class="itpe-flow-node">
    <strong>4대 지원 활동(Support Activities)</strong>
    <div class="itpe-step-detail"><strong>구성</strong><span>기업 하부구조 · 인적자원관리 · 기술개발 · 조달</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>5대 본원적 활동 (Primary Activities)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>물류/생산</strong><span>입고물류(<span class="itpe-keyword"><strong>SCM/WMS</strong></span>) → 생산운영(<span class="itpe-keyword"><strong>MES</strong></span>) → 출고물류(<span class="itpe-keyword"><strong>TMS</strong></span>)</span></div>
      <div class="itpe-flow-branch"><strong>고객접점</strong><span>마케팅·영업(<span class="itpe-keyword"><strong>CRM</strong></span>) → 사후 서비스(<span class="itpe-keyword"><strong>A/S 포털</strong></span>)</span></div>
      <div class="itpe-flow-branch"><strong>수익창출</strong><span>총가치 창출액 대비 총비용 차감 = <span class="itpe-keyword"><strong>마진(Margin)</strong></span></span></div>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Value Chain**: 마이클 포터가 정립한 이론으로 원자재 투입부터 완제품 소비까지 가치를 부가하는 활동 연쇄망
- **Primary Activities(본원적 활동)**: 제품의 물리적 생성, 판매, 유통, 사후 서비스에 직접 관여하는 5대 핵심 활동
- **Support Activities(지원 활동)**: 본원적 활동이 원활히 수행되도록 인프라, 기술, 인력, 원자재를 뒷받침하는 4대 지원 활동
- **Margin(마진)**: 고객이 제품과 서비스에 대해 기꺼이 지불하려는 총 가치(Price)에서 가치 활동 총원가를 차감한 잔여 이익
- **Linkages(연계성)**: 가치사슬 내 한 활동의 수행 방식이 다른 활동의 비용이나 성능에 미치는 상호 의존적 관계

</details>

## 예상문제

> 가치사슬(Value Chain)의 개념과 본원적·지원 활동을 설명하고, 활동 간 연계를 이용한 경쟁우위 확보 방안을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 경쟁 우위 분석의 프레임워크, 가치사슬의 개요

> 가치사슬은 기업 활동을 본원적 활동과 지원 활동으로 분해하여 **마진(Margin)**을 분석하며, 경쟁 우위는 개별 부서의 단절된 효율이 아닌 **활동 간 연계성(Linkages)의 최적화**로 판정함.

- 정의: 원자재 수급부터 최종 서비스까지 제품 변환 과정을 **5대 본원적 활동**과 **4대 지원 활동**으로 체계화하여 부가가치 창출 구조와 **마진(Margin)**을 분석하는 **경영 전략 분석 모델**
- 목적: 활동별 원가 동인 분석 · 차별화 기회 포착 · 프로세스 연계 최적화

## Ⅱ. 5대 본원적 활동과 4대 지원 활동의 가치사슬 구조

> 공급자로부터 원자재가 입고되어 가공, 출하, 판매, 사후 관리로 이어지는 흐름 속에서 부가가치가 누적되며 마진(Margin)을 창출함.

<div class="itpe-svg-map">
  <svg viewBox="0 0 520 220" role="img" aria-label="마이클 포터의 가치사슬(Value Chain) 9대 활동 및 마진 구조도">
    <!-- Support Activities (4 Rows) -->
    <rect x="20" y="15" width="410" height="24" rx="3" class="itpe-svg-node"></rect>
    <text x="225" y="31" class="itpe-svg-sub">기업 하부구조 (Firm Infrastructure - 기획, 재무, 법무, 품질경영)</text>

    <rect x="20" y="42" width="410" height="24" rx="3" class="itpe-svg-node"></rect>
    <text x="225" y="58" class="itpe-svg-sub">인적자원 관리 (Human Resource Management - 채용, 교육, 평가, 보상)</text>

    <rect x="20" y="69" width="410" height="24" rx="3" class="itpe-svg-node"></rect>
    <text x="225" y="85" class="itpe-svg-sub">기술 개발 (Technology Development - R&D, IT 시스템, 제품/공정 설계)</text>

    <rect x="20" y="96" width="410" height="24" rx="3" class="itpe-svg-node"></rect>
    <text x="225" y="112" class="itpe-svg-sub">조달 활동 (Procurement - 원자재, 설비, 외주 용역 구매 협상)</text>

    <!-- Primary Activities (5 Columns) -->
    <rect x="20" y="125" width="78" height="80" rx="4" class="itpe-svg-node is-current"></rect>
    <text x="59" y="152" class="itpe-svg-title">입고물류</text>
    <text x="59" y="170" class="itpe-svg-sub">자재수급</text>
    <text x="59" y="186" class="itpe-svg-sub">(WMS)</text>

    <rect x="103" y="125" width="78" height="80" rx="4" class="itpe-svg-node is-current"></rect>
    <text x="142" y="152" class="itpe-svg-title">생산운영</text>
    <text x="142" y="170" class="itpe-svg-sub">가공/조립</text>
    <text x="142" y="186" class="itpe-svg-sub">(MES)</text>

    <rect x="186" y="125" width="78" height="80" rx="4" class="itpe-svg-node is-current"></rect>
    <text x="225" y="152" class="itpe-svg-title">출고물류</text>
    <text x="225" y="170" class="itpe-svg-sub">유통/배송</text>
    <text x="225" y="186" class="itpe-svg-sub">(TMS)</text>

    <rect x="269" y="125" width="78" height="80" rx="4" class="itpe-svg-node is-current"></rect>
    <text x="308" y="152" class="itpe-svg-title">마케팅/영업</text>
    <text x="308" y="170" class="itpe-svg-sub">판촉/판매</text>
    <text x="308" y="186" class="itpe-svg-sub">(CRM)</text>

    <rect x="352" y="125" width="78" height="80" rx="4" class="itpe-svg-node is-current"></rect>
    <text x="391" y="152" class="itpe-svg-title">서비스</text>
    <text x="391" y="170" class="itpe-svg-sub">유지보수</text>
    <text x="391" y="186" class="itpe-svg-sub">(A/S)</text>

    <!-- Margin Arrow (Right Wedge) -->
    <polygon points="435,15 495,110 435,205 450,110" fill="var(--sl-color-accent)" opacity="0.85"></polygon>
    <text x="470" y="105" fill="#ffffff" font-weight="bold" font-size="12" text-anchor="middle">마</text>
    <text x="470" y="125" fill="#ffffff" font-weight="bold" font-size="12" text-anchor="middle">진</text>
  </svg>
</div>

<div class="itpe-pipeline is-vertical" role="img" aria-label="가치사슬 5대 본원적 활동 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 입고 물류 (Inbound Logistics)</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>원자재 수급·검수·보관</span></div><div class="itpe-step-detail"><strong>산출</strong><span>투입 자원·재고 가용성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 생산·운영 (Operations)</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>가공·조립·품질검사</span></div><div class="itpe-step-detail"><strong>산출</strong><span>완성 제품·서비스</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 출고 물류 (Outbound Logistics)</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>보관·주문처리·배송</span></div><div class="itpe-step-detail"><strong>산출</strong><span>고객 인도</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 마케팅·영업 (Marketing & Sales)</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>가격·판촉·판매</span></div><div class="itpe-step-detail"><strong>산출</strong><span>수요·주문</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 사후 서비스 (Service)</strong></span>
    <div class="itpe-step-detail"><strong>활동</strong><span>설치·수리·고객지원</span></div><div class="itpe-step-detail"><strong>산출</strong><span>사용가치·고객 유지</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Margin</strong></span> · 최종 소비자의 지불 용의 가치에서 9대 가치 활동의 총비용을 차감한 이익 극대화</div>

## Ⅲ. 가치활동과 정보기술 활용

> 각 활동의 비용 절감과 차별화는 전문화된 정보시스템 구축 · 활동 간 실시간 데이터 연계를 통해 구현됨.

| 적용축 | 정보기술 역할 | 판정 지표 |
|---|---|---|
| **본원 활동** | 주문·재고·생산·배송·고객정보 연결 | 리드타임 · 결품률 · 고객 유지율 |
| **지원 활동** | 재무·인력·기술·조달 데이터 표준화 | 단위당 원가 · 조달기간 · 개발기간 |
| **활동 간 연계** | 원인–결과 데이터 추적·병목 가시화 | 전체 흐름 개선과 마진 기여 |

## Ⅳ. 문제점·대응책

> 솔루션 도입 목록보다 활동의 비용·차별화 동인과 활동 간 연계를 먼저 검증해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **부서별 국소 최적화** | E2E 리드타임·원가로 연계 분석 | 전체 마진 개선 |
| **기술 중심 투자** | 비용·차별화 동인과 투자안 추적 | 불필요한 자동화 방지 |
| **측정 경계 누락** | 공급자·채널을 포함한 가치시스템 검토 | 외부 병목 식별 |

## Ⅴ. 활동 간 연계 개선을 위한 기술사적 제언

> 병목 활동과 연계 원인을 먼저 측정하고 필요한 범위에만 데이터 통합·업무 재설계를 적용함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 마이클 포터의 가치사슬은 각 활동의 비용 절감도 중요하지만, 핵심은 '연계성(Linkages)'에 있음. 영업 부서가 프로모션을 실행할 때 입고·생산·출고 시스템에 즉시 공유되지 않으면 품절과 재고 비용 폭증으로 마진이 훼손됨.
- 나라면: 활동별 비용·고객가치와 활동 간 인과를 확인한 뒤, 병목 연계에만 데이터 통합·자동화를 적용하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준 (Trigger)**: 개별 단위 부서의 생산성은 향상되었으나 전사 재고일수 및 납기 리드타임이 오히려 10% 이상 증가할 시 연계성(Linkage) 단절로 판정.
- **대응 방안 (Action)**: 본원적 활동(SCM-MES-TMS-CRM) 간 실시간 이벤트 드리븐(EDA) 연계를 구축하고, 전사 마진을 훼손하는 사일로(Silo) 부서 간 KPI를 통합 정렬함.
- **검증 체계 (Verification)**: 활동별 원가 동인(Cost Drivers)과 차별화 동인(Uniqueness Drivers)을 정량 계측하여 가치사슬 전 구간의 E2E 현금전환주기(CCC)를 검증함.
- **기대 효과 (Impact)**: 국소 최적화의 함정 탈피, 불필요한 재고 유지비용 35% 절감, 고객 맞춤형 차별화 경쟁 우위 및 영업이익률(마진) 극대화를 달성함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="가치사슬 활동 간 연계 개선 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>활동 간 데이터 단절·업무 책임 경계의 병목</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>병목 활동의 데이터 추적·업무 규칙·책임 경계 개선</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>리드타임·결품률·단위당 원가·고객 유지율의 개선 여부</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>리드타임·원가 개선과 고객가치 강화</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 기업의 활동을 **5대 본원적 활동**과 **4대 지원 활동**으로 체계화하여 부가가치 창출 구조와 **마진(Margin)**을 분석하는 **마이클 포터의 경영 전략 모델**
- 목적: 활동별 원가 동인 분석 · 프로세스 최적화 · 연계성 강화

### 2. 핵심 구조·판정

| 축 | 구성 | 판정 |
|---|---|---|
| **본원적 활동** | 입고 물류 → 생산·운영 → 출고 물류 → 마케팅·영업 → 사후 서비스 | 고객가치 창출 흐름 |
| **지원 활동** | 기업 하부구조 · 인적자원관리 · 기술개발 · 조달 | 본원 활동 지원 |
| **활동 간 연계** | 비용·차별화 동인 추적 | 마진 기여·병목 개선 여부 |

## 출제 이력과 검증 출처

- Harvard Business School Institute for Strategy and Competitiveness, [The Value Chain](https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-value-chain.aspx)

## 학습 체크

- [ ] Ⅰ: 가치사슬의 정의·마진·활동 간 연계의 의미를 설명할 수 있는가?
- [ ] Ⅱ: 5대 본원적 활동과 4대 지원 활동을 재현할 수 있는가?
- [ ] Ⅲ·Ⅳ: 정보기술 활용축과 분석 위험–대책–효과를 연결할 수 있는가?
- [ ] Ⅴ: 병목 활동의 추적성과 E2E 지표 검증 방안을 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [PLM](./071_plm.md)
- 연관 토픽: [SCM](./005_scm.md), [ERP](./068_erp.md), [CRM](./031_crm.md), [SWOT 분석](./034_swot_analysis.md)
- 다음 토픽: [정량적 위험분석](./073_quantitative_risk_analysis.md)
