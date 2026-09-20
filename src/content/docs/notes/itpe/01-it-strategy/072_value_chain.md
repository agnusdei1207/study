---
title: "가치사슬(Value Chain)"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 경영 전략 및 비즈니스 아키텍처를 거쳐 가치사슬로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>경영 전략·비즈니스 아키텍처</span>
  <strong>가치사슬(Value Chain)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **가치사슬(Value Chain)**은 기업의 활동을 **5대 본원적 활동**과 **4대 지원 활동**으로 분해하여 각 단계의 부가가치와 **마진(Margin)**을 극대화하는 전략 분석 모델
- 메커니즘: 조달·설계·생산·유통의 **상호 연계성(Linkages)**을 분석하고 각 활동에 **ERP·SCM·MES·CRM** 등 IT 시스템을 매핑하여 최적화
- 산출: 가치활동 정의서 · 원가 동인 분석표 · 활동기준원가(ABC) · IT 가치사슬 혁신 로드맵

<div class="itpe-flow-map" role="img" aria-label="가치사슬 9대 활동 및 IT 솔루션 매핑 흐름">
  <div class="itpe-flow-node">
    <strong>4대 지원 활동 (Support Activities)</strong>
    <small>기업 하부구조(ERP) · 인적자원(e-HR) · 기술개발(PLM) · 조달(SRM)</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>전방위 후속 지원 및 데이터 인프라</small></div>
  <div class="itpe-flow-node is-current">
    <strong>5대 본원적 활동 (Primary Activities)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>물류/생산</strong><span>입고물류(<span class="itpe-keyword"><strong>SCM/WMS</strong></span>) → 생산운영(<span class="itpe-keyword"><strong>MES</strong></span>) → 출고물류(<span class="itpe-keyword"><strong>TMS</strong></span>)</span></div>
      <div class="itpe-flow-branch"><strong>고객접점</strong><span>마케팅·영업(<span class="itpe-keyword"><strong>CRM</strong></span>) → 사후 서비스(<span class="itpe-keyword"><strong>A/S 포털</strong></span>)</span></div>
      <div class="itpe-flow-branch"><strong>수익창출</strong><span>총가치 창출액 대비 총비용 차감 = <span class="itpe-keyword"><strong>마진(Margin)</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>디지털 전환 및 생태계 확장</small></div>
  <div class="itpe-flow-node">
    <strong>디지털 가치그물 (Value Web)</strong>
    <small>실시간 이벤트 기반 다자간 플랫폼 협력 생태계</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Value Chain**: 마이클 포터가 정립한 이론으로 원자재 투입부터 완제품 소비까지 가치를 부가하는 활동 연쇄망
- **Primary Activities(본원적 활동)**: 제품의 물리적 생성, 판매, 유통, 사후 서비스에 직접 관여하는 5대 핵심 활동
- **Support Activities(지원 활동)**: 본원적 활동이 원활히 수행되도록 인프라, 기술, 인력, 원자재를 뒷받침하는 4대 지원 활동
- **Margin(마진)**: 고객이 제품과 서비스에 대해 기꺼이 지불하려는 총 가치(Price)에서 가치 활동 총원가를 차감한 잔여 이익
- **Linkages(연계성)**: 가치사슬 내 한 활동의 수행 방식이 다른 활동의 비용이나 성능에 미치는 상호 의존적 관계
- **Value Web(가치그물)**: 1차원 선형 공급망을 넘어 개방형 API와 데이터 메시로 다자간 참여자가 실시간 협업하는 디지털 생태계

</details>

## 예상문제

> 기업의 경쟁 우위 확보를 위한 마이클 포터(Michael E. Porter)의 가치사슬(Value Chain) 모델의 개념, 5대 본원적 활동과 4대 지원 활동의 구성요소 및 IT 솔루션 매핑 방안을 설명하고, 전통적 선형 가치사슬 대비 디지털 가치그물(Value Web)의 차이점과 실무 전환 전략을 제시하시오. (25점)

## Ⅰ. 경쟁 우위 분석의 프레임워크, 가치사슬의 개요

> 가치사슬은 기업 활동을 본원적 활동과 지원 활동으로 분해하여 **마진(Margin)**을 분석하며, 경쟁 우위는 개별 부서의 단절된 효율이 아닌 **활동 간 연계성(Linkages)의 최적화**로 판정함.

- 정의: 원자재 수급부터 최종 서비스까지 제품 변환 과정을 **5대 본원적 활동**과 **4대 지원 활동**으로 체계화하여 부가가치 창출 구조와 **마진(Margin)**을 분석하는 **경영 전략 분석 모델**
- 목적: 활동별 원가 동인 분석 및 차별화 기회 포착 → 프로세스 연계 최적화를 통한 **경쟁 우위(Competitive Advantage)** 확보

## Ⅱ. 5대 본원적 활동의 순차적 가치 창출 파이프라인

> 공급자로부터 원자재가 입고되어 가공, 출하, 판매, 사후 관리로 이어지는 흐름 속에서 부가가치가 누적됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="가치사슬 5대 본원적 활동 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 입고 물류 (Inbound Logistics)</strong></span>
    <small>원자재 수급 · 하역 검수 · 창고 보관 · 재고 통제<br />→ 자재 입고 전표 · WMS 재고 마스터</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 생산 및 운영 (Operations)</strong></span>
    <small>원자재 가공 · 부품 조립 · 공정 검사 · 설비 유지보수<br />→ 완제품 검사성적서 · MES 제조 실적</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 출고 물류 (Outbound Logistics)</strong></span>
    <small>완제품 포장 · 출하 배차 · 물류 거점 유통 · 배송 추적<br />→ 출하 송장 · TMS 운송 지시서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 마케팅 및 영업 (Marketing & Sales)</strong></span>
    <small>가격 책정 · 광고 프로모션 · 영업 채널 운영 · 수주 계약<br />→ 고객 견적서 · CRM 수주 명세서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 사후 서비스 (Service)</strong></span>
    <small>설치 시운전 · 부품 교체 수리 · 고객 불만(VOC) 대응<br />→ A/S 작업 내역서 · 고객 만족도 보고서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Margin</strong></span> · 최종 소비자의 지불 용의 가치에서 9대 가치 활동의 총비용을 차감한 이익 극대화</div>

## Ⅲ. 가치사슬 9대 활동과 IT 엔터프라이즈 솔루션 매핑

> 각 활동의 비용 절감과 차별화는 전문화된 정보시스템 구축 및 활동 간 실시간 데이터 연계를 통해 구현됨.

| 분류 | 9대 세부 활동 | 핵심 수행 역할 | 매핑 IT 솔루션 |
|---|---|---|---|
| **본원적 활동** | **입고 물류** | 원자재 입고, 보관 및 재고 관리 | **SCM(공급망관리)**, WMS(창고관리), RFID |
| **본원적 활동** | **생산 운영** | 조립 가공, 품질 검사, 공정 제어 | **MES(제조실행시스템)**, 스마트팩토리, IoT |
| **본원적 활동** | **출고 물류** | 완제품 보관, 배송 라우팅, 유통 | **TMS(배차관리)**, 물류 자동화 풀필먼트 |
| **본원적 활동** | **마케팅/영업** | 시장 분석, 판촉, 주문 접수 | **CRM(고객관계관리)**, 마케팅 자동화 |
| **본원적 활동** | **서비스** | 현장 설치, 무상 보증, 사후 유지보수 | AI 컨택센터, 원격 진단 A/S 포털 |
| **지원 활동** | **기업 하부구조** | 전사 기획, 재무/회계, 법무 통제 | **ERP(전사적자원관리)**, EIS(경영정보) |
| **지원 활동** | **인적자원 관리** | 핵심 인재 채용, 직무 교육, 성과 보상 | e-HRM, LMS(학습관리시스템) |
| **지원 활동** | **기술 개발** | 신제품 연구개발(R&D), 장비 엔지니어링 | **PLM(제품수명주기관리)**, CAD/CAE |
| **지원 활동** | **조달 활동** | 원자재 구매, 공급사 협상, 외주 계약 | 전자조달(e-Procurement), SRM(공급사관리) |

## Ⅳ. 전통적 선형 가치사슬 vs 디지털 가치그물(Value Web) 비교

> 1차원적인 공급자 주도(Push) 선형 사슬에서 다자간 실시간 협업과 고객 수요 기반(Pull)의 가치그물로 진화함.

| 비교 항목 | 전통적 선형 가치사슬 (Value Chain) | 디지털 가치그물 (Value Web) |
|---|---|---|
| **구조 형태** | 1차원 순차적 단계별 선형 파이프라인 | **다자간 연결 분산형 네트워크/플랫폼** |
| **가치 동인** | 물리적 공장 설비, 원자재, 노동력 | **데이터, 알고리즘, API, 네트워크 효과** |
| **운영 방식** | 공급자 중심의 밀어내기(**Push**) 모델 | 고객 수요 기반의 실시간 당기기(**Pull**) 모델 |
| **참여자 관계** | 수직 계열화 및 폐쇄적 원청-하청 계약 | 개방형 생태계 기반 수평적 파트너십 |
| **비즈니스 예시** | 전통 제조 자동차, 중공업 생산 라인 | 스마트 모빌리티 플랫폼, 커머스 생태계 |

## Ⅴ. 이벤트 기반 가치그물(Event-Driven Value Web) 구축을 위한 기술사적 제언

> 가치사슬의 분절된 사일로를 방치하면 채찍효과(Bullwhip Effect)가 발생하므로, 전사 이벤트 버스 기반의 실시간 연계가 필수적임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 마이클 포터의 가치사슬은 각 활동의 비용 절감도 중요하지만, 핵심은 '연계성(Linkages)'에 있음. 영업 부서가 프로모션을 실행할 때 입고·생산·출고 시스템에 즉시 공유되지 않으면 품절과 재고 비용 폭증으로 마진이 훼손됨.
- 나라면: 아파치 카프카(Kafka) 기반의 실시간 이벤트 버스를 전사 가치사슬 활동 사이에 구축하여 `고객 주문 이벤트 발생 → SCM 재고 자동 확인 → MES 긴급 생산 스케줄링 → 협력사 전자조달 발주`가 1초 내에 동기화되는 실시간 가치그물 아키텍처를 제시하겠음.

### 실전 답안용 기술사적 제언

- 판정: 단절된 선형 프로세스를 배제하고 전사 실시간 연계성 확립
- 대안: **EDA(Event-Driven Architecture) 기반 실시간 디지털 가치그물** 구축
- 검증: 활동 간 데이터 전달 레이턴시 1초 미만 · 주문-생산 연계 오류 0건
- 효과: 채찍효과 제거 · 재고 보유 비용 25% 절감 및 총마진 극대화

<div class="itpe-pipeline is-vertical" role="img" aria-label="가치사슬 디지털 가치그물 전환 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>활동 간 데이터 사일로 · 야간 배치 연계에 따른 주문-생산 시차 발생 · 마진 잠식</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>전사 이벤트 버스(Kafka) 중심 실시간 EDA 가치그물 구축 및 기간계(ERP-SCM-CRM) 연계</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>본원적 활동 간 종단간(End-to-End) 트랜잭션 추적성 확보 · 결품 발생률 0%</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>고객 수요에 즉각 반응하는 민첩한 제조 유통 달성 · 경쟁 우위 및 기업 마진 극대화</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 기업의 활동을 **5대 본원적 활동**과 **4대 지원 활동**으로 체계화하여 부가가치 창출 구조와 **마진(Margin)**을 분석하는 **마이클 포터의 경영 전략 모델**
- 목적: 활동별 원가 동인 분석 및 프로세스 최적화 → 활동 간 연계성(Linkages) 강화를 통한 **경쟁 우위(Competitive Advantage)** 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="가치사슬 5대 본원 활동 요약">
  <div class="itpe-pipeline-node"><strong>입고 물류</strong><small>원자재 수급 · 보관 (SCM / WMS)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>생산 운영</strong><small>부품 가공 · 조립 검사 (MES / IoT)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>출고 물류</strong><small>완제품 배송 · 유통 라우팅 (TMS)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>마케팅/영업</strong><small>가격 결정 · 판촉 수주 (CRM)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>사후 서비스</strong><small>설치 시운전 · 수리 (AI A/S 포털)</small></div>
</div>

### 3. 핵심 통제

- **9대 활동 IT 매핑**: 지원활동(ERP/PLM/HR/조달)과 본원활동의 긴밀한 연계
- **디지털 가치그물 전환**: 실시간 이벤트 버스(Kafka)를 통한 선형 사슬의 다자간 네트워크화

## 출제 이력과 검증 출처

- 제124회 정보관리기술사(KPC) 1교시: 마이클 포터의 가치사슬 모델의 주활동/지원활동 및 IT를 통한 혁신 방안
- Michael E. Porter, [Competitive Advantage: Creating and Sustaining Superior Performance](https://www.hbs.edu)

## 학습 체크

- [ ] 가치사슬의 정의와 마진(Margin)의 산출 원리를 설명할 수 있는가?
- [ ] 5대 본원적 활동과 4대 지원 활동의 명칭을 누락 없이 열거할 수 있는가?
- [ ] 각 활동별로 매핑되는 대표 엔터프라이즈 IT 솔루션(SCM, MES, TMS, CRM, ERP 등)을 제시할 수 있는가?
- [ ] 전통적 선형 가치사슬과 디지털 가치그물(Value Web)의 차이점을 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [PLM](./071_plm.md)
- 연관 토픽: [SCM](./005_scm.md), [ERP](./068_erp.md), [CRM](./031_crm.md), [SWOT 분석](./034_swot_analysis.md)
- 다음 토픽: [정량적 위험분석](./073_quantitative_risk_analysis.md)
