---
title: "FOCUS (FinOps 비용 데이터 표준)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "미출 · 65%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "미출"
  source_history: ""
  priority: 65
  priority_note: "시사·트렌드"
---

## 답안 골격
```text
[FOCUS (FinOps 비용 데이터 표준)] ◀━━ 머리: Ⅶ 내 의견 (FOCUS 표준 스키마 기반의 멀티 클라우드 비용 통합 ETL 파이프라인 및 자동 쇼백(Showback) 체계 구축)
 ┃
 ┣━ Ⅰ 개요 ───── 멀티 클라우드 간 청구서 용어·데이터 형식의 극심한 파편화 해소 → FinOps 재단 주도의 단일 오픈 비용 표준 규격
 ┣━ Ⅱ 특징 ───── 리눅스 재단 FinOps Foundation 주도 · 벤더 중립적 단일 스키마 · 표준화된 컬럼 정의(BilledCost, EffectiveCost) · 다중 CSP 지원
 ┣━ Ⅲ 구조 ───── 표준 데이터셋 계층 (청구자 정보 ↔ 서비스 분류 ↔ 리소스 식별 ↔ 가격 및 사용량 ↔ 할인 및 청구 금액)
 ┣━ Ⅳ 흐름 ───── ① 이종 CSP(AWS, Azure, GCP) 청구 데이터 수집 → ② FOCUS 변환 ETL 매핑 → ③ 정규화된 데이터 레이크 적재 → ④ 통합 FinOps 대시보드 시각화
 ┣━ Ⅴ 비교 ───── 독자적 CSP 청구서 vs FOCUS 표준 규격 (벤더 종속적 컬럼·커스텀 파서 필요 vs 표준 SQL 단일 쿼리 가능 및 분석 도구 상호운용성)
 ┗━ Ⅵ 실무 ───── CSP별 할인 모델(RI, SP, CUD)의 복잡한 amortization 상이 / 온디맨드 정가와 실효 비용의 갭 / 레거시 SaaS 비용 통합 한계
```
- 필수 키워드: FOCUS · FinOps Open Cost and Usage Specification · FinOps Foundation · 멀티 클라우드 비용 표준 · BilledCost · EffectiveCost · 데이터 스키마
- 배점 전략: 10점 = Ⅰ 개요 → Ⅲ FOCUS 핵심 표준 컬럼 체계 도식 → Ⅴ 이종 CSP 비교 / 25점 = Ⅰ~Ⅶ 전개, FOCUS 1.0/1.1 스펙 상세(ChargeCategory, ListCost, EffectiveCost) 및 멀티 클라우드 비용 거버넌스 구축 전략 상술
- 기출: 미출제. 예상: "멀티 클라우드 환경의 이종 비용 청구 데이터를 단일 스키마로 표준화하는 오픈소스 규격 FOCUS(FinOps Open Cost and Usage Specification)의 개념, 핵심 컬럼 규격 및 기대효과를 설명하시오."

## 한 줄 본질
- AWS, Azure, GCP 등 클라우드 서비스 공급자마다 제각각인 청구서(Billing CSV)의 컬럼 명칭, 할인 계산법, 사용량 단위를 하나의 오픈소스 공통 스키마로 통일하여 멀티 클라우드 비용을 단일 SQL로 분석할 수 있게 하는 데이터 표준 규격 → 이종 클라우드 비용 분석 비용 절감 및 FinOps 자동화 / 신규 CSP 기능 출시 시 표준 반영의 시차

## 핵심 그림
```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                    [ FOCUS 표준 기반 멀티 클라우드 비용 정규화 파이프라인 ]              │
│                                                                                         │
│   [ 이종 클라우드 원천 청구 데이터 (Raw Billing Data) ]                                 │
│   ┌───────────────────────┐ ┌───────────────────────┐ ┌───────────────────────────────┐ │
│   │ AWS Cost & Usage (CUR)│ │ Azure Cost Details    │ │ GCP Cloud Billing Export      │ │
│   │ • lineItem/Unblended  │ │ • costInBillingCurr   │ │ • cost, usage.amount          │ │
│   │ • product/servicecode │ │ • meterCategory       │ │ • service.description         │ │
│   └───────────┬───────────┘ └───────────┬───────────┘ └───────────────┬───────────────┘ │
│               │                         │                             │                 │
│               └────────────────────┐    │    ┌────────────────────────┘                 │
│                                    ▼    ▼    ▼                                          │
│   [ FOCUS 변환 엔진 (Normalization Engine) ] ── [ FinOps Foundation Open Standard ]    │
│   ┌─────────────────────────────────────────────────────────────────────────────────┐   │
│   │                             [ 핵심 표준 컬럼 매핑 ]                             │   │
│   │ • ProviderName     : AWS / Azure / GCP (공급자 표준 명칭)                       │   │
│   │ • ServiceCategory  : Compute / Storage / Network / Database (표준 카테고리)     │   │
│   │ • BilledCost       : 인보이스에 실제 청구된 금액 (송장 일치)                    │   │
│   │ • EffectiveCost    : 약정 할인(RI/SP)을 기간 분할 상각(Amortized)한 실질 비용   │   │
│   │ • ChargeCategory   : Usage(사용료), Purchase(약정구매), Tax, Adjustment         │   │
│   │ • ResourceId       : 클라우드 리소스 고유 식별자 (ARN, Resource URI)            │   │
│   └────────────────────────────────────────┬────────────────────────────────────────┘   │
│                                            │                                            │
│                                            ▼ 단일 쿼리 가능 (Single Pane of Glass)      │
│   [ 통합 FinOps 데이터웨어하우스 및 BI 대시보드 ]                                       │
│   • "SELECT ServiceCategory, SUM(EffectiveCost) FROM billing GROUP BY 1" (단일 SQL)     │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

## 핵심 용어
- EffectiveCost: 선납 약정 할인(AWS Savings Plans, Azure Reservations) 비용을 실제 자원을 소비한 날짜와 리소스에 비례하여 균등 상각(Amortize) 배분한 실질적 사용 비용
- BilledCost: 클라우드 서비스 제공자가 매월 발송하는 공식 세금계산서/청구서(Invoice)에 찍히는 실제 현금 지출 금액
- ChargeCategory: 비용의 성격을 나타내는 표준 분류 코드로 Usage(종량제 사용), Purchase(예약 약정 일시불 구매), Refund(환급), Tax(세금) 등으로 구분

## 핵심 통찰
- 멀티 클라우드의 가장 큰 장벽은 '비용 언어가 다르다는 것'임 → AWS는 Unblended Cost, Azure는 PreTaxCost, GCP는 Cost라고 부르며 할인 계산 방식도 제각각이라 엑셀 취합에만 매달 수백 시간을 낭비하던 문제를 FOCUS가 종결함
- BilledCost와 EffectiveCost의 분리가 핵심임 → 1년 치 약정을 일시불로 1억 원 긁었을 때, 재무팀은 그달의 BilledCost(1억)를 봐야 하고, 엔지니어링팀은 매일 27만 원씩 상각된 EffectiveCost를 봐야 정확한 원가 배분이 됨
- FinOps 도구 벤더의 종속을 깨뜨림 → FOCUS 표준 덕분에 특정 고가 SaaS FinOps 솔루션에 묶이지 않고, 조직 내부의 빅쿼리(BigQuery)나 스노우플레이크(Snowflake)에서 직접 자사 데이터로 비용 분석을 수행할 수 있음

## 이웃 토픽과 구분
- FOCUS vs FinOps 프레임워크: FinOps 프레임워크 = 문화, 조직, 프로세스(Inform-Optimize-Operate)를 다루는 운영 철학 / FOCUS = 그 프레임워크를 동작시키기 위한 '비용 데이터 스키마 규격 표준'

## 문제·원인·대책
- 적용 상황: AWS와 Azure를 동시 사용하는 금융 핀테크 기업의 클라우드 비용 통합 분석
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 매월 말 두 CSP의 청구서를 통합 엑셀로 정리하는 데 5영업일 소요 | 컬럼 명칭, 리전 표기, 할인 상각 방식의 상호 불일치 | 데이터 레이크에 FOCUS 1.0 오픈 스키마 변환 파이프라인 도입 | 비용 정산 소요시간 2시간으로 단축 |
| 특정 부서의 대규모 약정 구매로 인해 당월 서버 비용이 수억 원 튀어 보임 | 일시불 구매 금액(BilledCost)의 상각 처리 미흡 | FOCUS의 EffectiveCost 지표를 기준으로 12개월 분할 상각 쇼백(Showback) 적용 | 부서별 정확한 클라우드 원가 배분 달성 |

## 이렇게 출제된다
- 미출제. 예상: "멀티 클라우드 환경의 이종 비용 청구 데이터를 단일 스키마로 표준화하는 오픈소스 규격 FOCUS(FinOps Open Cost and Usage Specification)의 개념, 핵심 컬럼 규격 및 FinOps 도입 기업의 기대효과를 설명하시오." → 요구 포인트: Ⅰ 멀티 클라우드 비용 파편화 배경 + Ⅲ FOCUS 1.0 핵심 스키마(BilledCost vs EffectiveCost 등) 도식 + Ⅵ 통합 FinOps 파이프라인 구축 효과

## 내 의견
- [공공 클라우드 전환 사업의 'FOCUS 기반 다중 CSP 통합 비용 검증' 의무화] 국내 공공기관들이 네이버클라우드, KT클라우드, NHN클라우드를 멀티로 채택하면서 각기 다른 청구서 양식 때문에 예산 정산 시 극심한 행정 낭비 발생 → 나라면: 행정안전부 및 KISA 지침에 공공 클라우드 사업자의 청구 데이터 제공 시 FOCUS 규격을 준수한 데이터 익스포트를 의무 조항으로 명시하여, 단일 공공 대시보드에서 전 부처의 클라우드 소비를 한눈에 통제하는 국가 차원의 FinOps 거버넌스 완성
