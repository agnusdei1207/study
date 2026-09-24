---
sidebar:
  order: 127
  label: "127. 데이터 커머스 (Data Commerce)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 127
title: "데이터 커머스(Data Commerce) 밸류체인과 DaaS 기반 데이터 유통 생태계"
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "127"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터 경제·거버넌스</span><strong>데이터 커머스</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Provider -->
  <rect x="20" y="30" width="135" height="130" rx="8" fill="#3b82f6" fill-opacity="0.08" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="87" y="52" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 데이터 공급자</text>
  <text x="87" y="75" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">- 금융 (카드 결제)</text>
  <text x="87" y="93" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">- 통신 (유동 인구)</text>
  <text x="87" y="111" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">- 유통 (소비 이력)</text>
  <text x="87" y="140" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">품질정제·가명처리</text>

  <!-- Flow 1 -->
  <path d="M 155 95 L 185 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow127)"/>

  <!-- Exchange Platform -->
  <rect x="185" y="20" width="150" height="150" rx="8" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">2. 데이터 거래소</text>
  <text x="260" y="65" text-anchor="middle" font-size="10" fill="#78350f">- 상품 카탈로그 등록</text>
  <text x="260" y="83" text-anchor="middle" font-size="10" fill="#78350f">- 가치평가 및 가격책정</text>
  <text x="260" y="101" text-anchor="middle" font-size="10" fill="#78350f">- 스마트 계약·라이선스</text>
  <text x="260" y="125" text-anchor="middle" font-size="10" font-weight="bold" fill="#d97706">데이터 안심구역 운영</text>
  <text x="260" y="145" text-anchor="middle" font-size="10" fill="#78350f">DaaS API 구독 제공</text>

  <!-- Flow 2 -->
  <path d="M 335 95 L 365 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow127)"/>

  <!-- Consumer -->
  <rect x="365" y="30" width="135" height="130" rx="8" fill="#10b981" fill-opacity="0.08" stroke="#10b981" stroke-width="1.5"/>
  <text x="432" y="52" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">3. 데이터 수요자</text>
  <text x="432" y="75" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">- AI 스타트업 (학습)</text>
  <text x="432" y="93" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">- 유통/프랜차이즈</text>
  <text x="432" y="111" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">- 상권/마케팅 분석</text>
  <text x="432" y="140" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">신규 비즈니스 창출</text>

  <!-- Bottom Governance -->
  <rect x="20" y="185" width="480" height="60" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="260" y="208" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">거버넌스 및 신뢰 기반: 데이터 산업법 · 개인정보보호법(가명정보 결합) · 데이터 품질인증</text>
  <text x="260" y="228" text-anchor="middle" font-size="10" fill="#64748b">원천 파일(CSV) 다운로드 지양 $\rightarrow$ DaaS API 및 클린룸(Cleanroom) 환경 중심 유통</text>

  <defs>
    <marker id="arrow127" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **기업 및 공공기관이 보유한 원천 데이터를 수집·정제·가공·결합하여 경제적 가치가 있는 상품으로 패키징하고, 공인된 데이터 거래소나 DaaS 플랫폼을 통해 유통·거래하여 지속적인 수익을 창출하는 데이터 경제의 핵심 비즈니스 생태계**
- 암기: `공-거-수-거` (데이터 커머스 4대 축: 공급자, 거래소, 수요자, 거버넌스) / `다-세-안-결` (4대 상품 유형: DaaS API, 원시 데이터셋, 데이터 안심구역, 가명정보 결합 상품) / `원-시-수` (3대 가격산정: 원가법, 시장접근법, 수익접근법)
- 판단축:
  - **데이터 커머스 vs 오픈 데이터**: 영리 목적 유료 라이선스 및 DaaS 과금 vs 공익 목적 무료 전면 개방
  - **파일 직접 다운로드 vs DaaS API**: 1회성 유출 및 불법 재판매 위험 vs 호출 건당 과금 및 사용량 모니터링 통제
- 주의: 데이터는 무한 복제가 가능하므로 단순 CSV 파일 형태로 판매할 경우 2차 재배포 및 스크래핑을 원천 차단하기 어려우며, 반드시 데이터 안심구역이나 API 형태의 통제된 환경으로 유통해야 함
---

## 1교시 예상문제 (10점)

> 데이터 커머스(Data Commerce) 밸류체인과 DaaS 기반 데이터 유통 생태계의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 원천 데이터를 정제·가공·결합하여 경제적 가치가 있는 상품으로 패키징하고 거래소를 통해 유통·수익화하는 데이터 비즈니스 |
| **2. 4대 비즈니스 모델** | - **DaaS API**: 실시간 REST API 호출 및 사용량 과금<br/>- **데이터셋 패키지**: AI 학습용 표준 포맷 판매<br/>- **데이터 안심구역**: 원본 반출 없는 폐쇄 분석 뷰 제공<br/>- **가명정보 결합**: 통신+카드 등 이종 데이터 융합 리포트 |
| **3. 가격 산정 3대 방식** | 원가법(구축 투입비용), 시장접근법(유사 거래사례 비교), 수익접근법(미래 창출 현금흐름 할인) |
| **4. 보안 및 유출 방지** | 무단 복제 및 재판매 방지를 위해 단순 파일 다운로드를 지양하고 데이터 클린룸 및 DaaS API 채택 필수 |
---

### 핵심 관계

| 평가 접근법 | 산정 원리 | 장점 | 단점 및 한계 |
|:---|:---|:---|:---|
| **원가법 (Cost Approach)** | 데이터를 수집, 정제, 저장, 레이블링하는 데 투입된 인건비·인프라 총비용 기준 산정 | 산출 근거가 명확하고 객관적 수치 제시 가능 | 데이터의 미래 경제적 가치나 시장 수요를 전혀 반영하지 못함 |
| **시장접근법 (Market Approach)** | 데이터 거래소 내 유사 데이터 상품의 과거 실제 거래 사례 가격을 비교하여 산정 | 시장 수급 원리 반영, 직관적 이해 용이 | 활성화된 데이터 거래 선례가 절대적으로 부족함 |
| **수익접근법 (Income Approach)** | 해당 데이터를 활용하여 미래에 창출할 수 있는 예상 현금흐름(매출 증대, 비용 절감)을 현재가치로 할인 | 데이터의 본질적 효용 및 부가가치를 가장 정확히 반영 | 미래 수익 추정 및 할인율 적용에 분석가의 주관성 개입 |

---

## 2~4교시 예상문제 (25점)

> 데이터 경제 시대의 새로운 비즈니스 패러다임인 데이터 커머스(Data Commerce)의 개념과 가치사슬(Value Chain), 비즈니스 모델 유형 및 유통 활성화를 위한 법적·기술적 과제를 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 데이터 자산화와 경제적 유통: 데이터 커머스 개요

#### 한줄 요약: 기업 내부의 잠자는 데이터를 가공·결합하여 경제적 가치가 있는 상품으로 표준화하고 안전하게 유통·수익화하는 비즈니스 모델

- **배경**:
  - 디지털 전환(DX)으로 전 산업에서 데이터가 폭발적으로 축적되었으나 사내 활용에만 머물러 데이터 자산 가치 실현 한계
  - AI 모델 학습 및 초개인화 서비스를 위해 자사 데이터뿐만 아니라 이종 산업(금융+통신+유통) 간의 데이터 융합 수요 폭증
- **정의**: 데이터를 단순한 시스템 부산물이 아닌 독립된 경제재(자산)로 인식하여, 생산·가공·품질인증·가격책정·거래·유통 및 사후 관리 전 과정을 포괄하는 비즈니스 활동
- **데이터 자산의 고유 경제적 특성**:
  - **한계비용 제로**: 복제 및 전송 비용이 거의 들지 않아 무한 공급 가능
  - **비경합성(Non-rivalry)**: 한 사용자가 데이터를 소비하더라도 다른 사용자의 소비를 제한하지 않음
  - **가치 감가상각 부재**: 마모되지 않으나, 시간에 따른 진부화(Freshness) 존재

### Ⅱ. 데이터 커머스의 4대 비즈니스 모델 유형

#### 한줄 요약: 가공 형태와 전달 방식에 따른 데이터셋 판매, DaaS API 구독, 데이터 안심구역, 가명 결합 패키지

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="115" height="140" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="72" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. DaaS API</text>
  <text x="72" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Data as a Service</text>
  <text x="72" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">실시간 REST API</text>
  <text x="72" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">호출 건당 과금</text>
  <text x="72" y="135" text-anchor="middle" font-size="10" fill="#64748b">재판매 유출 방지</text>

  <!-- Box 2 -->
  <rect x="140" y="20" width="115" height="140" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="197" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. 정적 데이터셋</text>
  <text x="197" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Batch Dataset</text>
  <text x="197" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">CSV, Parquet 패키지</text>
  <text x="197" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">AI 학습용 대량셋</text>
  <text x="197" y="135" text-anchor="middle" font-size="10" fill="#64748b">1회성 일시불 판매</text>

  <!-- Box 3 -->
  <rect x="265" y="20" width="115" height="140" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="322" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. 안심구역 분석</text>
  <text x="322" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Data Cleanroom</text>
  <text x="322" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">폐쇄 가상 VDI 환경</text>
  <text x="322" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">반출 제한 분석</text>
  <text x="322" y="135" text-anchor="middle" font-size="10" fill="#64748b">민감 의료/금융 데이터</text>

  <!-- Box 4 -->
  <rect x="390" y="20" width="115" height="140" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="447" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">4. 가명결합 패키지</text>
  <text x="447" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Cross-domain</text>
  <text x="447" y="95" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">통신+카드 결합분석</text>
  <text x="447" y="112" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">데이터전문기관 연계</text>
  <text x="447" y="135" text-anchor="middle" font-size="10" fill="#64748b">최고 부가가치 상품</text>
</svg>
</div>

1. **DaaS (Data as a Service) API 모델**:
   - 수요자가 원본 데이터를 소유하지 않고 클라우드 API(REST/GraphQL)를 통해 필요한 시점에 실시간 쿼리 및 결과 수신
   - 종량제(Pay-per-use) 또는 월정액 구독(Subscription) 과금
2. **원시/가공 데이터셋 패키지 판매**:
   - AI 학습용 이미지/텍스트 말뭉치나 시계열 센서 로그를 표준 포맷(Parquet, TFRecord)으로 패키징하여 거래소에서 판매
3. **데이터 안심구역 및 클린룸(Cleanroom) 모델**:
   - 원본 반출이 금지된 민감 데이터(의료, 신용)를 폐쇄된 보안 가상화 환경에 올리고, 분석 모델만 안으로 들여보내 분석 결과치(통계/파라미터)만 외부 반출
4. **이종 데이터 가명정보 결합 패키지**:
   - 데이터전문기관을 통해 통신사의 유동인구 데이터와 카드사의 소비 데이터를 결합하여 완성형 상권 분석 리포트로 납품

### Ⅲ. 데이터 가치평가 및 가격 책정(Pricing) 3대 접근법

#### 한줄 요약: 무형 자산인 데이터의 공정한 거래 가격 산정을 위한 원가법, 시장법, 수익접근법

| 평가 접근법 | 산정 원리 | 장점 | 단점 및 한계 |
|:---|:---|:---|:---|
| **원가법 (Cost Approach)** | 데이터를 수집, 정제, 저장, 레이블링하는 데 투입된 인건비·인프라 총비용 기준 산정 | 산출 근거가 명확하고 객관적 수치 제시 가능 | 데이터의 미래 경제적 가치나 시장 수요를 전혀 반영하지 못함 |
| **시장접근법 (Market Approach)** | 데이터 거래소 내 유사 데이터 상품의 과거 실제 거래 사례 가격을 비교하여 산정 | 시장 수급 원리 반영, 직관적 이해 용이 | 활성화된 데이터 거래 선례가 절대적으로 부족함 |
| **수익접근법 (Income Approach)** | 해당 데이터를 활용하여 미래에 창출할 수 있는 예상 현금흐름(매출 증대, 비용 절감)을 현재가치로 할인 | 데이터의 본질적 효용 및 부가가치를 가장 정확히 반영 | 미래 수익 추정 및 할인율 적용에 분석가의 주관성 개입 |

### Ⅳ. 데이터 커머스 vs 일반 전자상거래(e-Commerce) 비교

#### 한줄 요약: 실물 물리 상품과 무형 디지털 자산의 유통 및 관리 체계 차이

| 비교 항목 | 일반 e-커머스 (Electronic Commerce) | 데이터 커머스 (Data Commerce) |
|:---|:---|:---|
| **거래 대상** | 물리적 실물 재화 (의류, 가전, 식품 등) | **무형의 디지털 데이터셋, API 스트림, 분석 모델** |
| **복제 및 한계비용** | 복제 불가 (추가 생산 비용 발생) | **한계비용 제로 (무한 복제 및 동시 다자 공급 가능)** |
| **물류 및 전달** | 택배, 화물 등 물리적 물류 인프라 | **네트워크 전송 (REST API, SFTP, 클라우드 버킷)** |
| **재고 및 감가상각** | 재고 유지비용 발생, 물리적 마모 및 파손 | 재고 유지비 극소, **시간 경과에 따른 정보 진부화** |
| **법적 규제** | 전자상거래법, 소비자보호법 | **개인정보보호법, 데이터산업법, 저작권법** |
| **반품 및 환불** | 물건 반품 후 환불 가능 | **반품 불가 (한 번 다운로드 시 복수 복제 잔류)** |

### Ⅴ. 데이터 커머스 활성화를 위한 선결 과제

#### 한줄 요약: 가명처리 규제 완화, 데이터 품질인증 체계(DQM), 스마트 계약 기반 지재권 보호

1. **법·제도적 선결 과제**:
   - **가명정보 결합 절차 간소화**: 데이터전문기관의 결합 심사 기간 단축 및 자율적 사후 보고 체계로 전환
   - **데이터 소유권 및 재산권 명문화**: 데이터산업법 상의 '데이터자산 부정취득·사용 금지' 조항의 실효성 확보
2. **기술적 선결 과제**:
   - **데이터 품질 인증(DQC) 의무화**: 정밀도, 완전성, 유효성이 검증되지 않은 결함 데이터의 유통을 원천 차단
   - **프라이버시 강화 기술(PET)**: 차분 프라이버시(Differential Privacy), 동형암호(Homomorphic Encryption) 기반의 무유출 결합 기술
   - **블록체인 스마트 컨트랙트**: 데이터 다운로드 및 API 호출 이력을 위변조 불가한 분산원장에 기록하여 사용량 기반 자동 정산

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 재식별 위험 차단, 무단 재판매 스크래핑 방지, 결함 환불 분쟁 예방

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **가명처리 데이터의 재식별 위험** | 타 공공 데이터와의 결합을 통해 특정 개인의 신원이 역추적될 가능성 | k-익명성($k \ge 5$) 및 l-다양성 검증을 자동화하고 준식별자 노이즈 마스킹 강제 |
| **구매자의 데이터 무단 2차 재유통** | 파일 다운로드 후 제3자에게 유상 판매하거나 오픈소스로 무단 공개 | 원본 파일 다운로드를 금지하고 데이터 클린룸(Cleanroom) 또는 워터마킹(Digital Watermarking) 삽입 |
| **데이터 결함으로 인한 환불 소송** | 제공된 데이터셋의 결측치(Null) 비율이 20%를 초과하여 AI 학습 불가 | 데이터 거래 계약서에 DQC-V(품질인증) 등급 및 SLA(결측율 1% 미만)를 정량 명시 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 많은 기업들이 데이터 거래를 "사내 DB 테이블을 CSV로 덤프 떠서 거래소에 올려놓고 팔리는지 기다리는 것"으로 착각한다.
> 하지만 어떤 기업도 남이 쓰던 쓰레기 덤프 데이터를 비싼 돈 주고 사지 않는다.
> 지속 가능한 데이터 커머스의 본질은 '원시 데이터(Raw Data)' 거래가 아니라 **'가공된 지능과 인사이트(API)'를 구독 형태로 서비스하는 것**이다.
> 데이터 자체를 넘기는 것이 아니라, "질의를 던지면 점수를 반환하는 API"나 "클라우드 클린룸 안에서만 구동되는 분석 뷰"로 상품화해야만 불법 복제를 막고 영속적인 데이터 현금 흐름을 창출할 수 있다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "데이터 클린룸(Data Cleanroom)과 연합학습(Federated Learning)의 결합 모델"을 제언하겠다. 원본 데이터의 물리적 이동 없이 서로 다른 기업 간에 AI 모델 파라미터만 교환하는 '탈중앙화 데이터 커머스' 패러다임을 제시하고, 데이터 자산의 가치를 객관적으로 공시하는 '데이터 재무제표' 제도화 필요성을 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 데이터 자산의 경제적 가치 실현과 전 산업 AI 전환을 위해 안전한 데이터 커머스 유통 생태계 조성이 시급함.
- **대응**:
  1. **유통 패러다임 전환**: 파일 직접 전송을 전면 금지하고 DaaS API 및 데이터 안심구역(Cleanroom) 중심 유통 강제.
  2. **가치평가 체계 표준화**: 원가법과 수익접근법을 절충한 '데이터 가치평가 모델'을 수립하고 공인 평가 기관 연계.
  3. **데이터 품질 게이트 구축**: 국가 공인 데이터 품질인증(DQC) 기준을 충족한 정제 데이터만 카탈로그 등록 허용.
- **검증**: 가명처리 재식별 위험도 평가 0건 달성 및 스마트 계약 기반 API 정산 오차 0% 검증.
- **효과**: 신규 데이터 비즈니스 수익원 창출 및 국가적 데이터 융합 시너지 극대화.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">데이터 고립, 파일 다운로드 시 무단 유출 및 가격 책정 불확실</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">DaaS API 구독화, 데이터 안심구역 도입, 표준 가치평가 적용</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">DQC 품질인증 획득, 스마트 계약 정산 무결성, 재식별 위험 제로</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">데이터 자산 가치 극대화 및 안전한 데이터 유통 생태계 확립</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제127회 정보관리 2교시: 데이터 커머스(Data Commerce)의 개념, 비즈니스 모델 유형 및 활성화를 위한 선결 과제
- **검증 출처**:
  - 과학기술정보통신부, "데이터 산업진흥 및 이용촉진에 관한 기본법 (데이터산업법)"
  - 한국데이터산업진흥원(K-DATA), "데이터 거래 및 가치평가 가이드라인"
---

## 연결 토픽

- 상위 토픽: [03-006 데이터 거버넌스](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/006_data_governance.md)
- 연관 토픽: [03-002 데이터 가치평가](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/002_data_valuation.md), [03-034 비정형 가명정보 처리 가이드라인](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/034_pseudonymized_data_guidelines_unstructured.md)
