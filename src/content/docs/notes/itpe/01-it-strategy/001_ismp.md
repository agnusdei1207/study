---
title: "ISMP"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 정보화 기획·발주를 거쳐 ISMP로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>정보화 기획·발주</span>
  <strong>ISMP</strong>
</div>

## 큰 그림과 30초 인출

<div class="itpe-flow-map" role="img" aria-label="경영·정책에서 ISP와 ISMP를 거쳐 조달·구축으로 이어지는 흐름">
  <div class="itpe-flow-node"><strong>경영·정책</strong></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>ISP</strong>
    <small>정보화 과제 선정</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>구축 대상 시스템 확정</small></div>
  <div class="itpe-flow-node is-current">
    <strong>ISMP</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>절차</strong><span>착수 → 방향 → 요건 → 구조 → 이행</span></div>
      <div class="itpe-flow-branch"><strong>산출</strong><span>요건 · 아키텍처 · FP · 예산 · RFP</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>조달·구축</strong></div>
</div>

- 본질: 특정 시스템을 **요건 · 아키텍처 · FP · 예산 · RFP**로 구체화하는 발주 기준선
- 인출: `착수 → 방향 → 요건 → 구조 → 이행`
- 통제: `요건 → 아키텍처 → FP → RFP` 추적성 확보

## 예상문제

> 특정 정보시스템 구축사업의 발주 전 위험을 최소화하기 위한 ISMP(Information System Master Plan)의 개념, 방법론 5단계 체계, ISP와의 차이점 및 실무 적용 시 요건-예산-RFP 간 추적성 확보 방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **ISMP 5단계 방법론** | 착수, 방향성 수립, 업무·기술 요건 분석, 구조·요건 정의, 구축사업 이행방안 수립 | Ⅲ 구조·절차 |
| **요건 추적성(Traceability)** | 업무요건 $\rightarrow$ 시스템요건 $\rightarrow$ 아키텍처 $\rightarrow$ FP $\rightarrow$ RFP 연결성 검증 | Ⅴ 실무, Ⅵ 결론 |

## Ⅰ. 구축사업 실패를 방어하는 발주 기준선, ISMP의 개요

- 정의: 특정 SW 및 정보시스템 구축사업을 추진하기 전에 업무와 IT 현황을 분석하고, 요구사항을 FP 산정이 가능한 수준으로 상세화하여 구축 계획, 아키텍처, 예산, RFP를 작성하는 종합 실행 계획
- 배경: 모호한 사업 구상 상태에서 무리하게 턴키 발주하여 발생하는 잦은 과업 변경, 납기 지연, 사업자와 발주처 간의 예산·하자 분쟁 악순환 차단
- 목적: 발주자의 요구사항을 객관적·구체적으로 명세화하여 조달 전제 통일, 공학적 규모 측정을 통한 적정 예산 확보, 분리발주 및 클라우드 우선 도입 검토를 통한 조달 공정성 담보

## Ⅱ. ISMP의 4대 핵심 특징

| 특징 | 세부 내용 및 원리 | 실무적 기여 |
|---|---|---|
| **대상 구체성** | 전사 전략이 아닌 특정 단위 정보시스템으로 범위를 한정하여 정밀 분석 | 구축 사업의 경계 명확화 |
| **요건 상세성** | 기능, 기술, 비기능(성능/보안/가용성) 요건을 검수 가능한 수준으로 정량 기술 | 요구사항 기준선(Baseline) 확립 |
| **산출물 추적성** | 업무요건 $\rightarrow$ 시스템요건 $\rightarrow$ 아키텍처 $\rightarrow$ FP $\rightarrow$ RFP 간 일관성 유지 | 과업 누락 및 예산 왜곡 원천 차단 |
| **조달 연계성** | 구축계획, SW 분리발주 대상 검토, 클라우드 적합성, 공공 발주 RFP 완성 | 즉각적인 조달 집행 가능 |

## Ⅲ. ISMP 구조·절차 및 산출물

<div class="itpe-pipeline" role="img" aria-label="요건에서 아키텍처와 규모·예산을 거쳐 RFP로 이어지는 ISMP 추적 구조">
  <div class="itpe-pipeline-node"><strong>요건</strong><small>업무 · IT · 비기능</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>아키텍처</strong><small>SW · HW · NW · 보안</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>규모·예산</strong><small>FP · TCO</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>RFP</strong><small>범위 · 일정 · 발주</small></div>
</div>
<div class="itpe-trace-band"><strong>RTM</strong> · 요건부터 RFP까지 양방향 추적</div>

| 단계 | 활동 | 산출물 |
|---|---|---|
| **착수** | 조직 · 범위 · WBS · 품질 | 수행계획 |
| **방향** | 환경 · 벤치마킹 · 목표 · 범위 | 범위·방향서 |
| **요건** | 인터뷰 · 프로세스 · 기능 · 비기능 | 요건명세 |
| **구조** | SW · HW · NW · 보안 · 인터페이스 | 아키텍처 · 요건기술서 |
| **이행** | 일정 · FP · 분리발주 · RFP | 이행계획 · 예산 · RFP |

## Ⅳ. 전략계획(ISP) vs 구축실행계획(ISMP) 비교

| 기준 | ISP | ISMP |
|---|---|---|
| **핵심 목적** | 전사 정보화 비전 수립 및 과제 포트폴리오 도출 | 특정 시스템 구축사업의 상세 요건 정의 및 발주 준비 |
| **대상 범위** | 조직 및 업무 전반 (Enterprise-wide) | **단일 특정 정보시스템** (System-specific) |
| **핵심 질문** | "무엇을 왜 추진할 것인가?" (과제 선정) | "어느 범위와 비용으로 어떻게 구축할 것인가?" (기준선) |
| **상세 수준** | 중장기 로드맵, 개략적 개념 모델 (Conceptual) | **기능점수(FP) 산출 수준의 상세 요건 및 아키텍처** |
| **주요 산출물** | 정보화 전략 로드맵, 추진 과제 우선순위 | 상세 요건 기술서, 예산 산출서, **제안요청서(RFP)** |
| **적용 시점** | 중장기 정보화 예산 확보 및 과제 발굴 단계 | 단위 시스템 구축사업 발주 직전 연도 예산 심의 단계 |

## Ⅴ. 실무 고려사항 및 대책

- 적용 상황: 공공 차세대 행정 시스템 구축사업 전 ISMP 수립 및 조달 발주

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **구축 중 과업 변경 분쟁** | 업무요건 기술서와 최종 RFP 간 추적 관계(Traceability) 누락 | 요구사항 추적 매트릭스(RTM)를 통한 '요건-구조-FP-RFP' 전수 매핑 검증 | 과업 누락 및 무상 추가 요구 원천 방지 |
| **예산과 실제 구축비 불일치** | 기획 단계 간이 FP 산정 오차 및 비기능 인프라(클라우드/보안) 비용 누락 | 정규 FP 기법 병행 및 CSP 공인 TCO 계산기 기반 클라우드 인프라 실측 예산 편성 | 예산 부족에 따른 사업 유찰 방지 |
| **상용 SW 분리발주 누락** | SI 사업자의 통합 발주 선호 및 발주처의 조달 편의성 추구 | SW진흥법 제54조에 따른 상용 SW 분리발주 평가 기준표 작성 의무화 | 국산 상용 SW 제값받기 및 생태계 보호 |

## Ⅵ. 결론 및 기술사적 제언

- [핵심 통찰]: ISMP의 성패는 수백 페이지짜리 보고서 두께가 아니라 '업무 요건이 계약문서(RFP)와 예산서에 1:1로 온전히 추적되는가'에 달려 있음. 요건과 계약이 단절된 ISMP는 본 구축사업에서 필연적으로 과업 변경과 사업 파행을 유발함.
- 나라면: ISMP 종료 감리 시 단순 문서 점검을 배제하고, [요건 추적 매트릭스(RTM) 상의 요건 $\rightarrow$ 아키텍처 $\rightarrow$ FP 단가 $\rightarrow$ RFP 과업지시서] 100% 일치율 검증을 '품질 게이트(Quality Gate)'로 강제하여, 완벽한 발주 기준선이 확보된 상태에서만 조달청 공고를 진행하겠음.

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- ISMP(Information System Master Plan)는 특정 정보시스템 구축사업의 성공을 위해 요구사항을 FP 산정 수준으로 구체화하고, 목표 아키텍처와 예산 및 RFP를 수립하는 발주 기준선 정의 활동임.

### 2. 핵심 메커니즘 / 체계
```text
착수 → 방향 → 요건 → 구조 → 이행
                       └─ FP · 예산 · RFP
```
- ISP가 '과제 도출(What to do)'이라면 ISMP는 '발주 기준선 확립(How to build)'을 담당함.

### 3. 차별화 제언
- 구축 사업 중 과업 변경을 원천 차단하기 위해 '요건 $\rightarrow$ 아키텍처 $\rightarrow$ FP $\rightarrow$ RFP' 전수 추적 매트릭스(RTM) 검증을 의무화해야 함.

## 출제 이력과 검증 출처

- 출제 이력: 제138회 정보관리기술사 기출, 제130회·129회 KPC 모의고사
- 검증 출처: 한국지능정보사회진흥원(NIA) '정보시스템 마스터플랜(ISMP) 수립 가이드라인'

## 학습 체크

- [ ] ISMP의 개념 및 ISP와의 차이점 5가지를 설명할 수 있는가?
- [ ] ISMP 5단계 방법론의 단계별 핵심 활동 및 산출물을 제시할 수 있는가?
- [ ] 요건-아키텍처-FP-RFP 간의 추적성(Traceability) 확보 방안을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [IT 전략·관리 개요](./index.md)
- 연관 토픽: [ISP](./003_isp.md), [과업심의(과업변경·사업기간 적정성)](./091_public_sw_cost_and_scope_change_criteria.md)
- 다음 토픽: [ISO/IEC 38500](./002_iso_iec_38500.md)
