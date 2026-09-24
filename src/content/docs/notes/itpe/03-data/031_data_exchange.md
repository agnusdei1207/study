---
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
extra:
  keyword_grade: "기초"
  model: "GPT-6"
  question_no: "031"
sidebar:
  badge:
    text: "기초"
    variant: "note"
  label: "031. 데이터 거래소"
  order: 31
tags:
  - "notes-data"
title: "데이터 거래소 (Data Exchange)"
weight: 31
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 활용·경제</span><span>데이터 유통·거래 체계</span><strong>데이터 거래소</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 155" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="155" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Top: Supplier & Consumer -->
  <rect x="15" y="12" width="150" height="36" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="90" y="27" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #0f172a)">데이터 공급자</text>
  <text x="90" y="40" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">금융·통신·유통·의료</text>

  <rect x="355" y="12" width="150" height="36" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="430" y="27" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #0f172a)">데이터 수요자</text>
  <text x="430" y="40" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">AI 기업·핀테크·연구기관</text>

  <line x1="165" y1="30" x2="200" y2="30" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-dex)"/>
  <line x1="355" y1="30" x2="320" y2="30" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-dex)"/>

  <!-- Center Hub: Data Exchange -->
  <rect x="205" y="10" width="110" height="40" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" rx="5"/>
  <text x="260" y="26" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">데이터 거래소</text>
  <text x="260" y="40" text-anchor="middle" font-size="8" fill="var(--color-text, #334155)">품질·가치평가·계약</text>

  <line x1="260" y1="50" x2="260" y2="68" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-dex)"/>

  <!-- Bottom Core Mechanism: Data Clean Room & Compute-to-Data -->
  <rect x="40" y="70" width="440" height="72" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="6"/>
  <rect x="40" y="70" width="440" height="22" fill="var(--color-primary-light, #e0f2fe)" rx="6"/>
  <text x="260" y="85" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">Compute-to-Data 패러다임: 데이터 안심구역 (Data Clean Room)</text>

  <text x="260" y="108" text-anchor="middle" font-size="9" fill="var(--color-danger, #ef4444)" font-weight="bold">🚫 원본 파일(CSV) 다운로드 원천 차단</text>
  <text x="260" y="128" text-anchor="middle" font-size="8.5" fill="var(--color-text, #334155)">폐쇄형 VDI 샌드박스 내 가명 결합·모델 학습 후 통계 분석 결과(Insight)만 안전 반출</text>

  <defs>
    <marker id="arrow-dex" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **데이터 생산자와 수요자 간의 데이터 탐색, 품질 검증, 가치평가, 라이선스 계약 및 안전한 결합·유통을 중개하여 데이터 자산의 유동성을 공급하는 제도적·기술적 종합 플랫폼**
- 암기: `등-평-계-전-결` = 등록(카탈로그) $\to$ 평가(품질·가치) $\to$ 계약(라이선스) $\to$ 전송(안심구역/API) $\to$ 결산(정산)
- 법적 근거: 데이터산업법 제10조(데이터 거래 지원 및 유통체계 구축) 및 개인정보보호법상 가명정보 결합전문기관 연계
- 패러다임 전환: 파일(CSV) 일괄 다운로드 방식에서 **데이터 안심구역(Data Clean Room) 기반 연산 반입(Compute-to-Data)** 방식으로 진화
---

## 1교시 예상문제 (10점)

> 데이터 거래소 (Data Exchange)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 데이터 거래소의 정의

- 데이터산업법에 근거하여 데이터 공급자와 수요자 간에 데이터 탐색, 품질인증, 가치평가, 라이선스 계약 및 안전한 가명 결합을 중개하는 **데이터 유통 플랫폼**

### 2. 핵심 아키텍처 및 Compute-to-Data 메커니즘

- **포털 계층**: 시맨틱 메타데이터 기반 데이터 카탈로그 및 샘플 제공
- **거래 관리**: 스마트 컨트랙트 기반 라이선스 계약 및 에스크로 정산
- **안심 연산**: 원본 다운로드를 전면 차단하고 데이터 안심구역(Data Clean Room) 폐쇄 VDI 제공
- **반출 통제**: 모델 가중치 및 통계 분석 결과(Insight)에 한해 비식별 심사 후 안전 반출

| 구성요소 | 주요 역할 |
|---|---|
| 데이터 카탈로그 | 시맨틱 메타데이터 기반 데이터 탐색 및 샘플 제공 |
| 가치평가·품질인증 | DQC 품질 기준 검증 및 공정 거래 가격 도출 |
| 데이터 안심구역 | 원본 반출 없는 폐쇄 분석 샌드박스 제공 |
| 스마트 계약 | 라이선스 범위, 사용 기간, API 호출당 자동 정산 |

### 3. 차별화 제언

- 파일 유출 위험을 원천 차단하기 위해 **Compute-to-Data(연산 반입)** 및 **연합학습(Federated Learning)** 인프라를 연계하고, 수요자 중심의 **역경매(Data Bounty) 모델**을 활성화함
---

## 2~4교시 예상문제 (25점)

> 데이터 경제 활성화의 핵심 인프라인 데이터 거래소(Data Exchange)의 개념과 법적 기반을 설명하고, 주요 구성요소 및 중개 절차, 데이터 안심구역과의 연계를 통한 원본 유출 방지 및 거래 활성화 방안을 논하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 데이터 자산의 시장 유동성을 창출하는 데이터 거래소 개요

- 정의: **데이터 거래소(Data Exchange)**는 금융, 통신, 유통, 공공 등 다양한 산업 분야에서 생성된 데이터를 상품화하여 등록하고, 수요자가 이를 검색·구매·결합·활용할 수 있도록 중개하며 신뢰성과 안전성을 담보하는 양면 시장(Two-sided Market) 플랫폼
- 목적: 데이터의 비표준화, 품질 불확실성, 가격 산정 난항, 프라이버시 침해 우려로 인한 시장 실패(레몬 마켓)를 해소하고, 합법적이고 안전한 데이터 유통 생태계 확립
- 필요성: AI 및 디지털 전환(DX)의 가속화로 고품질 이종 결합 데이터 수요가 폭증하였으나, 기업 간 개별 직거래는 막대한 법적 계약 비용과 데이터 유출 리스크를 수반함

#### 한줄 요약

- 데이터 거래소는 데이터 공급과 수요 사이의 탐색 비용과 법적·보안적 불확실성을 최소화하는 공인된 유통 허브임

### Ⅱ. 데이터 거래소의 핵심 특징과 법적·제도적 기반

| 핵심 속성 | 기술적·제도적 메커니즘 | 기대 효과 |
|---|---|---|
| **양면 시장 중개** | 공급자(수익화)와 수요자(신규 비즈니스 창출) 간의 네트워크 효과 극대화 | 데이터 거래 생태계 확장 |
| **품질·가치평가 연계** | 공인 데이터 품질인증(DQC) 및 3대 가치평가 모델(원가·시장·수익) 연계 | 신뢰성 확보 및 공정 가격 책정 |
| **안심 연산 환경** | 데이터 안심구역(Clean Room) 연계로 원본 반출 없는 폐쇄 분석 지원 | 원본 무단 복제 및 재판매 원천 차단 |
| **권리 및 라이선스** | 데이터 이용 목적, 기간, 제3자 제공 범위를 규정한 스마트 계약 적용 | 지식재산권 분쟁 방지 |

- **데이터산업진흥 및 이용촉진에 관한 기본법 (데이터산업법 제10조)**: 데이터 거래 활성화 지원 시책 수립, 데이터 안심구역 지정 및 공인 데이터 거래사 육성 근거
- **개인정보 보호법 (제28조의2 가명정보의 처리 등)**: 개인정보 가명처리 후 통계작성, 과학적 연구 목적으로 정보주체 동의 없는 결합·활용 허용
- **금융혁신지원 특별법 (혁신금융서비스)**: 금융보안원 주도 금융데이터거래소(FinDX) 운영 및 이종 산업 결합 인가

#### 한줄 요약

- 데이터 거래소는 데이터산업법과 개인정보보호법에 근거하여 품질, 가치, 보안이 공인된 환경에서 유통을 집행함

### Ⅲ. 데이터 거래소의 4계층 참조 아키텍처

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 155" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="155" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Layer 1: Portal -->
  <rect x="15" y="10" width="490" height="28" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="30" y="28" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">1. 사용자 포털 계층</text>
  <text x="170" y="28" font-size="8.5" fill="var(--color-text, #334155)">상품 검색, 시맨틱 메타데이터 카탈로그, 마켓플레이스, 커뮤니티</text>

  <!-- Layer 2: Trade Management -->
  <rect x="15" y="44" width="490" height="28" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="30" y="62" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">2. 거래 관리 계층</text>
  <text x="170" y="62" font-size="8.5" fill="var(--color-text, #334155)">가치평가 엔진, 전자계약(스마트 컨트랙트), 에스크로 결제·정산</text>

  <!-- Layer 3: Data Services -->
  <rect x="15" y="78" width="490" height="28" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="30" y="96" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">3. 데이터 서비스 계층</text>
  <text x="170" y="96" font-size="8.5" fill="var(--color-text, #334155)">가명 결합 엔진, 결합전문기관 연계, API 게이트웨이, 메타데이터 관리</text>

  <!-- Layer 4: Security & Infrastructure -->
  <rect x="15" y="112" width="490" height="32" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <text x="30" y="132" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">4. 보안 및 인프라 계층</text>
  <text x="170" y="132" font-size="8.5" fill="var(--color-primary-dark, #0369a1)">데이터 안심구역(Data Clean Room), 폐쇄 샌드박스, DRM/워터마킹, 감사 로그</text>
</svg>
</div>

| 계층 | 주요 컴포넌트 | 핵심 기능 |
|---|---|---|
| **포털 계층** | 데이터 카탈로그, 시맨틱 검색 엔진 | 데이터 셋의 스키마, 샘플 데이터, 설명서 열람 및 검색 |
| **거래 관리 계층** | 전자계약 모듈, 에스크로(Escrow) 결제 | 라이선스 조건(단건 구매, 구독제, API 쿼리 종량제) 체결 및 대금 정산 |
| **데이터 서비스 계층**| 결합전문기관 연계 모듈, ETL 파이프라인 | 서로 다른 공급자의 가명정보를 결합키 연계정보(CI 변환키)로 안전 결합 |
| **보안·인프라 계층**| 데이터 안심구역, 개인정보 비식별 솔루션 | 가상 데스크톱(VDI) 폐쇄망 환경 제공, 통계 결과물 익명성 사전 심사 |

#### 한줄 요약

- 데이터 거래소는 카탈로그 포털, 전자계약 관리, 가명 결합 서비스, 보안 인프라 계층의 유기적 결합으로 작동함

### Ⅳ. 데이터 상품 유통 및 거래 수행 5단계 절차

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 62" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="62" fill="var(--color-surface, #f8fafc)" rx="6" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <rect x="8" y="12" width="90" height="38" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="53" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">① 등록·심사</text>
  <text x="53" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">품질·DQC 검증</text>

  <line x1="98" y1="31" x2="108" y2="31" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-prc)"/>

  <rect x="110" y="12" width="92" height="38" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="156" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">② 가치평가</text>
  <text x="156" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">원가·시장·수익</text>

  <line x1="202" y1="31" x2="212" y2="31" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-prc)"/>

  <rect x="214" y="12" width="92" height="38" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="260" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">③ 계약·체결</text>
  <text x="260" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">스마트계약·에스크로</text>

  <line x1="306" y1="31" x2="316" y2="31" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-prc)"/>

  <rect x="318" y="12" width="92" height="38" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="364" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">④ 전송·분석</text>
  <text x="364" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">안심구역·API</text>

  <line x1="410" y1="31" x2="420" y2="31" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-prc)"/>

  <rect x="422" y="12" width="90" height="38" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1" rx="3"/>
  <text x="467" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">⑤ 사후·정산</text>
  <text x="467" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">반출심사·대금정산</text>

  <defs>
    <marker id="arrow-prc" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <polygon points="0 0, 5 2.5, 0 5" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

| 단계 | 수행 작업 | 산출물 및 통제 기준 |
|---|---|---|
| **1. 등록·심사** | 데이터 공급자가 데이터 명세서 및 데이터 프로파일 등록 | 개인정보 포함 여부 전수 검사, DQC 품질 검증 |
| **2. 가치평가** | 희소성, 품질, 대체가능성, 비즈니스 효익 분석 | 공인 가치평가서, 적정 판매 가격 가이드 |
| **3. 계약·체결** | 스마트 컨트랙트 기반 표준 데이터 거래 계약서 작성 | 라이선스 증명서, 에스크로 예치금 영수증 |
| **4. 전송·분석** | 파일 전송 대신 데이터 안심구역 VDI 인스턴스 배정 | 폐쇄 분석 환경, 전용 API 접근 토큰 |
| **5. 사후 심사** | 외부 반출 요청 통계 결과물에 대해 재식별 위험도 평가 | 비식별 적정성 검토 보고서, 정산 내역서 |

#### 한줄 요약

- 등록에서 정산까지의 절차는 특히 개인정보 재식별 방지와 공급자 권리 보호를 위한 단계별 통제 관문을 둠

### Ⅴ. 주요 데이터 거래소 플랫폼 비교

| 플랫폼 | 주관 기관 | 주요 유통 데이터 | 핵심 비즈니스 모델 |
|---|---|---|---|
| **금융데이터거래소<br>(FinDX)** | 금융보안원 | 은행·카드·증권·보험 신용정보, 이종 결합 데이터 | 금융-통신-유통 융합 가명결합 데이터 상품 판매, 유료 정산 |
| **데이터스토어<br>(DataStore)** | 한국지능정보사회진흥원(NIA) | 범용 공공·민간 빅데이터 플랫폼 16대 분야 연계 | 공공 지원 중심, 무료 개방 및 중소·스타트업 바우처 연계 |
| **K-DATA 데이터 안심구역** | 한국데이터산업진흥원(K-DATA) | 공공기관 및 대기업의 비공개 민감 데이터 | 원본 데이터 반출 차단, 공간·좌석 기반 폐쇄망 분석 서비스 |
| **글로벌 클라우드 거래소** | AWS Data Exchange, Snowflake Data Cloud | 글로벌 금융 시계열, 날씨, 마케팅 로그 | 클라우드 네이티브 스토리지 쿼리 공유(Data Sharing), 구독료 과금 |

#### 한줄 요약

- 국내 거래소는 금융보안원·K-DATA 중심의 보안 폐쇄형 결합 모델이며, 글로벌은 스노우플레이크 등 클라우드 직접 쿼리 공유 모델로 발전 중임

### Ⅵ. 데이터 거래소 활성화 저해 요인 및 극복 대책

| 저해 요인 | 발생 원인 | 실무 극복 대책 | 기대 효과 |
|---|---|---|---|
| **원본 데이터 무단 유출 우려** | 파일 다운로드 후 제3자 복제 및 불법 유통 통제 불능 | **Compute-to-Data 패러다임 전환**: 데이터 안심구역 연계 및 연합학습(Federated Learning) 인프라 제공 | 공급자의 데이터 등록 기피 해소 |
| **데이터 가격 책정의 불투명성** | 데이터 특유의 비경합성 및 거래 선례 부족으로 인한 주관적 호가 | 원가법·시장법·수익법 기반 **표준 데이터 가치평가 프레임워크** 연계 의무화 | 거래 교섭 비용 절감 및 성사율 제고 |
| **거래 상품의 유동성 부족 (레몬 마켓)** | 품질 검증 없는 정적 엑셀 파일 난립 및 최신성 결여 | **데이터 품질인증(DQC) 의무화** 및 CDC 기반 실시간 스트리밍 API 상품화 | 지속적인 데이터 소비 생태계 구축 |
| **수요와 공급의 미스매치** | 공급자 중심의 일방적 데이터 업로드 위주 운영 | **수요자 중심 역경매(Data Bounty) 마켓플레이스** 도입 | 실제 산업 현장에서 필요한 AI 학습 데이터 공급 |

#### 한줄 요약

- 안심구역 기반 연산 이동, 공인 가치평가 모델, 수요 기반 역경매 도입이 데이터 거래소 활성화의 3대 열쇠임

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 데이터는 복제 비용이 거의 0에 수렴하는 '비경합적(Non-rivalrous)' 재화이기 때문에, 전통적인 파일 다운로드(CSV/Parquet) 방식의 유통은 필연적으로 원본 유출과 2차 불법 유통으로 이어져 공급자를 시장에서 퇴출시킨다(레몬 마켓화). 따라서 데이터 거래소의 성공은 '데이터를 소유권 이전의 대상'으로 보지 않고 '연산 권한(Access to Computation)을 대여하는 서비스'로 전환하는 패러다임 시프트에 달려 있다.
>
> **[나라면 이렇게 쓴다]**
> 생성형 AI 시대의 데이터 거래소는 단순 데이터 판매 플랫폼에서 'AI 파운데이션 모델 학습 및 연합 샌드박스'로 진화해야 한다. 원본 데이터를 물리적으로 외부로 내보내지 않는 연합학습(Federated Learning) 및 Compute-to-Data 인프라를 구축하고, 수요자는 모델 가중치(Weight)만 반출하도록 통제한다. 또한 블록체인 스마트 컨트랙트를 통해 학습 기여도(샤플리 값, Shapley Value)를 산정하여 데이터 공급자에게 AI 모델 수익을 지속적으로 배당하는 지분형 분배 아키텍처를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 정적 파일 다운로드 방식에 따른 원본 데이터 복제 유출 위험 및 가치산정 난항으로 거래 성사율 저하.
- **대응 (개선 방안)**: 데이터 안심구역 기반 Compute-to-Data 연산 환경 의무화 및 연합학습·스마트 컨트랙트 정산 결합.
- **검증 (검증 기준)**: 원본 데이터 외부 유출 0건(Zero-Leakage) 보장 및 결합 반출 적정성 심사 자동화율 95% 이상 검증.
- **효과 (실행 효과)**: 고가치 핵심 데이터 등록 건수 3배 증가 및 AI 기업의 고품질 결합 데이터 확보 기간 80% 단축.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">현행 한계</div>
    <div class="itpe-flow-desc">파일 다운로드 방식 유통으로 원본 유출 우려 및 거래 기피</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">개선 방안</div>
    <div class="itpe-flow-desc">Compute-to-Data 안심구역 및 연합학습·스마트계약 도입</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">검증 기준</div>
    <div class="itpe-flow-desc">원본 반출 0건 보장 및 비식별 적정성 심사 자동화율 95% 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">실행 효과</div>
    <div class="itpe-flow-desc">민감 데이터 유통 유동성 3배 확대 및 결합 분석 기간 80% 단축</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- 제132회 1교시 2번: 데이터 거래소
- 제127회 4교시 2번: 데이터 커머스(Data Commerce)의 중요성 및 비즈니스 모델
- [데이터산업진흥 및 이용촉진에 관한 기본법 (법률 제18999호)](https://www.law.go.kr/)
- [금융보안원 금융데이터거래소(FinDX) 운영 가이드](https://findx.or.kr/)

## 연결 토픽

- [데이터 가치평가·데이터 자산화](./002_data_valuation/) · [데이터 거버넌스](./006_data_governance/) · [가명정보 처리 가이드라인 개정](./034_pseudonymized_data_guidelines_unstructured/) · [데이터 안심구역](../08-law-policy/002_data_safe_zone/)
