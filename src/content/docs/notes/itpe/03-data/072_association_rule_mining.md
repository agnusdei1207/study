---
sidebar:
  order: 72
  label: "072. 연관규칙분석 (Association Rule Mining)"
  badge:
    text: "A"
    variant: note
title: "연관규칙분석 (Association Rule Mining) 및 3대 핵심 지표 (지지도·신뢰도·향상도)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 72
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "072"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>머신러닝·데이터마이닝</span><strong>연관규칙분석 (Association Rule Mining)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">연관규칙 3대 평가 지표 (지지도 &middot; 신뢰도 &middot; 향상도) 벤다이어그램</text>

  <!-- Venn Diagram Canvas -->
  <g transform="translate(30, 48)">
    <!-- Universe Box -->
    <rect x="0" y="0" width="220" height="135" rx="5" fill="#ffffff" stroke="#94a3b8" stroke-width="1.2"/>
    <text x="12" y="18" font-size="9" font-weight="bold" fill="#64748b">전체 거래 (U, 크기 N)</text>

    <!-- Circle A -->
    <circle cx="85" cy="75" r="45" fill="#3b82f6" fill-opacity="0.2" stroke="#3b82f6" stroke-width="1.5"/>
    <text x="65" y="75" font-size="10" font-weight="bold" fill="#1e40af">A 만</text>

    <!-- Circle B -->
    <circle cx="135" cy="75" r="45" fill="#10b981" fill-opacity="0.2" stroke="#10b981" stroke-width="1.5"/>
    <text x="145" y="75" font-size="10" font-weight="bold" fill="#065f46">B 만</text>

    <!-- Intersection A ∩ B -->
    <text x="110" y="78" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">A &cap; B</text>

    <text x="110" y="125" font-size="8" fill="#64748b" text-anchor="middle">Support = P(A &cap; B) = n(A &cap; B) / N</text>
  </g>

  <!-- Right: 3 Core Metrics Definitions -->
  <g transform="translate(265, 48)">
    <rect x="0" y="0" width="225" height="135" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>

    <text x="12" y="20" font-size="9.5" font-weight="bold" fill="#1e40af">1. 지지도 (Support: 동시 발생)</text>
    <text x="12" y="34" font-size="8" fill="#475569">P(A &cap; B) = n(A &cap; B) / N</text>

    <text x="12" y="56" font-size="9.5" font-weight="bold" fill="#065f46">2. 신뢰도 (Confidence: 조건부)</text>
    <text x="12" y="70" font-size="8" fill="#475569">P(B|A) = n(A &cap; B) / n(A)</text>

    <text x="12" y="92" font-size="9.5" font-weight="bold" fill="#b91c1c">3. 향상도 (Lift: 인과적 배수)</text>
    <text x="12" y="106" font-size="8" fill="#475569">P(A &cap; B) / (P(A) &middot; P(B)) = Conf / P(B)</text>
    <text x="12" y="122" font-size="8" font-weight="bold" fill="#b91c1c">&bull; Lift &gt; 1: 유의미 양의 상관 | &le; 1: 무의미</text>
  </g>

  <!-- Bottom: Lift 3 Stages Guide -->
  <g transform="translate(30, 195)">
    <rect x="0" y="0" width="460" height="60" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>

    <rect x="10" y="8" width="140" height="44" rx="3" fill="#ecfdf5" stroke="#10b981"/>
    <text x="80" y="24" font-size="8.5" font-weight="bold" fill="#065f46" text-anchor="middle">Lift &gt; 1 (양의 상관)</text>
    <text x="80" y="42" font-size="7.5" fill="#334155" text-anchor="middle">A가 B 구매 촉진 (추천 규칙)</text>

    <rect x="160" y="8" width="140" height="44" rx="3" fill="#f8fafc" stroke="#94a3b8"/>
    <text x="230" y="24" font-size="8.5" font-weight="bold" fill="#475569" text-anchor="middle">Lift = 1 (독립 사건)</text>
    <text x="230" y="42" font-size="7.5" fill="#334155" text-anchor="middle">우연의 일치 (연관성 전무)</text>

    <rect x="310" y="8" width="140" height="44" rx="3" fill="#fef2f2" stroke="#ef4444"/>
    <text x="380" y="24" font-size="8.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Lift &lt; 1 (음의 상관)</text>
    <text x="380" y="42" font-size="7.5" fill="#334155" text-anchor="middle">A 사면 B 안 삼 (상호 대체재)</text>
  </g>
</svg>
</div>

- 본질: **대규모 트랜잭션 데이터베이스에서 품목들 간에 빈번하게 동시 발생하는 조건부 연관 관계($A \rightarrow B$)를 사전 가설 없이(비지도 학습) 도출하기 위해, 지지도(Support)로 빈발 항목을 선별하고 신뢰도(Confidence)와 향상도(Lift)로 인과적 유의성을 검증하는 데이터 마이닝 기법**
- 암기: `지-신-향` (지지도, 신뢰도, 향상도) / `모-조-하` (Apriori 공리: 어떤 항목집합이 빈발하지 않으면, 그 상위집합(슈퍼셋)도 절대 빈발하지 않는다 $\rightarrow$ 하향식 가지치기)
- 판단축:
  - **신뢰도(Confidence)**: 단순히 조건부 확률만 나타내므로, 품목 B 자체가 대중적인 베스트셀러일 경우 규칙이 왜곡되는 '착시(Fallacy)' 발생 가능
  - **향상도(Lift)**: B 자체의 통상 구매 확률을 나누어 보정하므로, 규칙이 실제로 가치 있는지 판별하는 최종 핵심 기준 ($Lift > 1$ 필수)
- 주의: 품목 수가 $M$개일 때 가능한 항목 조합은 $2^M$으로 지수적으로 폭증하므로, 최소 지지도(Minimum Support)를 너무 낮게 설정하면 조합 폭발로 시스템이 크래시될 수 있음
---

## 1교시 예상문제 (10점)

> 연관규칙분석 (Association Rule Mining) 및 3대 핵심 지표 (지지도·신뢰도·향상도)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 연관 규칙 분석의 개념 및 정의

- **개념**: 대규모 트랜잭션 속에서 항목 간의 동시 발생 패턴($A \rightarrow B$)을 도출하는 비지도 데이터 마이닝
- **핵심 전제**: 최소 지지도와 신뢰도 임계값을 통해 유효한 장바구니 규칙 선별

### 2. 연관 규칙 분석 3대 핵심 평가 지표

| 핵심 지표 | 수학적 정의 | 통계적 의미 및 역할 |
|:---|:---|:---|
| **1. 지지도 (Support)** | $\text{Support} = P(A \cap B) = \frac{n(A \cap B)}{N}$ | 전체 거래 중 $A, B$가 동시 발생할 확률 (1차 가지치기 기준) |
| **2. 신뢰도 (Confidence)**| $\text{Confidence} = P(B\|A) = \frac{n(A \cap B)}{n(A)}$ | $A$ 구매 시 $B$도 구매할 조건부 확률 (규칙 확실성 평가) |
| **3. 향상도 (Lift)** | $\text{Lift} = \frac{P(A \cap B)}{P(A) \cdot P(B)} = \frac{\text{Conf}}{P(B)}$ | $A$ 구매가 $B$ 구매 확률을 높인 배수 ($\text{Lift} > 1$ 필수) |

### 3. 실무 지표 적용 시 착시 주의점

- **신뢰도의 착시**: $B$가 원래 대중적 인기 품목인 경우 신뢰도가 90% 이상으로 과대포장됨
- **최종 규칙 채택**: 반드시 향상도($\text{Lift} > 1.0$) 이상인 유의미한 양의 상관성 규칙만 엄선
---

### 핵심 관계

| 비교 항목 | Apriori 알고리즘 (Agrawal, 1994) | FP-Growth 알고리즘 (Han, 2000) |
|:---|:---|:---|
| **기본 동작 원리** | 최소 지지도 미달 항목의 슈퍼셋을 제거하는 **하향식 가지치기** | 빈발 패턴을 압축한 **FP-Tree를 메모리에 구축 후 분할 정복** |
| **후보 집합 생성** | **필수** (1-항목 $\rightarrow$ 2-항목 $\rightarrow$ $k$-항목 후보 생성) | **전혀 없음** (후보 집합 생성 오버헤드 원천 제거) |
| **데이터베이스 스캔** | 최대 항목 집합 크기($k$)만큼 **수십 회 반복 Full Scan** | **단 2회** (1회: 빈도수 계산, 2회: FP-Tree 구축) |
| **연산 속도** | **느림** (대용량 트랜잭션에서 기하급수적 지연) | **매우 빠름** (Apriori 대비 10~100배 이상 고속) |
| **메모리 소요량** | 비교적 낮음 | 높음 (FP-Tree가 메모리에 완전히 상주해야 함) |

---

## 2~4교시 예상문제 (25점)

> 데이터 마이닝의 대표적인 장바구니 분석 기법인 연관규칙분석(Association Rule Mining)의 개념과 특징을 설명하고, 규칙의 타당성을 검증하기 위한 3대 핵심 평가 지표(지지도, 신뢰도, 향상도)의 수식과 의미를 비교한 후, 대표적 추출 알고리즘인 Apriori와 FP-Growth를 비교하시오. (10점 / 25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 트랜잭션 속 숨겨진 패턴을 발굴하는 연관규칙분석 개요

#### 한줄 요약: 대규모 거래 로그에서 항목 간의 동시 발생 패턴($A \rightarrow B$)을 조건부 확률과 향상도 지표로 탐색하는 비지도 마이닝

- **등장 배경**:
  - 유통, 금융, 웹 로그 등에서 생성되는 대규모 트랜잭션 속에서 어떤 상품들이 함께 소비되는지, 특정 행동 뒤에 어떤 행동이 뒤따르는지 규칙을 찾아 교차 판매(Cross-selling)를 극대화할 필요성 대두
- **연관규칙분석(Market Basket Analysis)의 정의**:
  - $I = \{i_1, i_2, \dots, i_m\}$인 항목들의 집합과 트랜잭션 데이터베이스 $D$에서, 조건절(Antecedent, $A$)과 결과절(Consequent, $B$)이 상호 배타적($A \cap B = \emptyset$)일 때, 함의 규칙 **$A \rightarrow B$**의 유의미성을 도출하는 분석 기법

### Ⅱ. 연관규칙 3대 핵심 평가 지표의 수학적 정의 및 해석

#### 한줄 요약: 전체 발생 빈도를 보는 지지도, 조건부 확률을 보는 신뢰도, 우연을 배제한 영향 배수를 보는 향상도

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 115" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="95" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">연관규칙 3대 지표의 계층적 검증 파이프라인</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="145" height="50" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="72" y="18" font-size="9.5" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 지지도 (Support)</text>
    <text x="72" y="34" font-size="8" fill="#475569" text-anchor="middle">전체 중 동시 발생 빈도</text>

    <path d="M 148 25 L 168 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="170" y="0" width="145" height="50" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <text x="242" y="18" font-size="9.5" font-weight="bold" fill="#065f46" text-anchor="middle">2. 신뢰도 (Confidence)</text>
    <text x="242" y="34" font-size="8" fill="#475569" text-anchor="middle">A 구매 시 B 구매 조건부확률</text>

    <path d="M 318 25 L 338 25" stroke="#64748b" stroke-width="1.5"/>

    <rect x="340" y="0" width="135" height="50" rx="4" fill="#eff6ff" stroke="#2563eb" stroke-width="1.2"/>
    <text x="407" y="18" font-size="9.5" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 향상도 (Lift)</text>
    <text x="407" y="34" font-size="8" fill="#b91c1c" text-anchor="middle">인과적 구매 촉진 배수</text>
  </g>
</svg>
</div>

### 1. 지지도 (Support)
- **수학적 정의**: 전체 트랜잭션 수 $N$ 중 항목 집합 $A$와 $B$가 동시에 포함된 트랜잭션의 비율:
  $$\text{Support}(A \rightarrow B) = P(A \cap B) = \frac{n(A \cap B)}{N}$$
- **역할 및 의미**: 규칙의 **빈발성(Frequency)과 중요성**을 측정. 전체 거래 중 극소수만 발생하는 쓸모없는 희귀 조합을 조기에 가지치기(Pruning)하는 1차 임계값으로 활용

### 2. 신뢰도 (Confidence)
- **수학적 정의**: 항목 집합 $A$를 포함하는 트랜잭션 중 항목 집합 $B$도 함께 포함하는 조건부 확률:
  $$\text{Confidence}(A \rightarrow B) = P(B | A) = \frac{P(A \cap B)}{P(A)} = \frac{n(A \cap B)}{n(A)}$$
- **역할 및 의미**: 규칙의 **정확도와 확실성(Certainty)**을 측정. $A$가 일어났을 때 $B$가 동반될 확률이 충분히 높은지를 평가

### 3. 향상도 (Lift)
- **수학적 정의**: $A$가 주어졌을 때 $B$의 조건부 확률과, $A$와 무관하게 $B$가 발생할 사전 확률의 비율:
  $$\text{Lift}(A \rightarrow B) = \frac{P(A \cap B)}{P(A) \cdot P(B)} = \frac{\text{Confidence}(A \rightarrow B)}{P(B)}$$
- **향상도 판정 기준 3단계**:
  - **$\text{Lift} > 1$ (양의 상관관계)**: $A$의 구매가 $B$의 구매 확률을 유의미하게 향상시킴 $\rightarrow$ **실제 가치 있는 추천 규칙**
  - **$\text{Lift} = 1$ (독립 사건)**: $A$와 $B$는 통계적으로 독립. 우연에 의해 함께 발생했을 뿐 아무런 연관성이 없음
  - **$\text{Lift} < 1$ (음의 상관관계)**: $A$를 구매하면 오히려 $B$를 구매할 확률이 떨어짐 $\rightarrow$ 상호 대체재(예: 콜라와 사이다)

### Ⅲ. 신뢰도의 착시(Confidence Fallacy)와 향상도의 필요성

#### 한줄 요약: 대중적으로 많이 팔리는 인기 품목의 경우 신뢰도만 높게 나오는 착시를 향상도로 검증해야 함

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 120" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="100" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">신뢰도의 착시 사례 (기저귀 &rarr; 생수)</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="470" height="55" rx="4" fill="#ffffff" stroke="#ef4444" stroke-width="1.2"/>
    <text x="15" y="18" font-size="8.5" fill="#334155">전체 1,000명 중 기저귀 100명(10%), 생수 900명(90%, 대중필수재), 동시구매 90명(9%)</text>
    <text x="15" y="34" font-size="8.5" fill="#1e40af">&bull; 신뢰도: 90 / 100 = 90% (매우 높아 보이는 착시 발생!)</text>
    <text x="15" y="48" font-size="8.5" font-weight="bold" fill="#dc2626">&bull; 향상도: 0.9 / 0.9 = 1.0 (독립! 기저귀가 생수 구매를 유도한 것이 아님!)</text>
  </g>
</svg>
</div>

### Ⅳ. 주요 알고리즘 비교: Apriori vs FP-Growth

#### 한줄 요약: 하향식 가지치기와 반복적 DB 스캔을 수행하는 Apriori와, 압축 트리를 구축하여 단 2회 스캔으로 끝내는 FP-Growth

| 비교 항목 | Apriori 알고리즘 (Agrawal, 1994) | FP-Growth 알고리즘 (Han, 2000) |
|:---|:---|:---|
| **기본 동작 원리** | 최소 지지도 미달 항목의 슈퍼셋을 제거하는 **하향식 가지치기** | 빈발 패턴을 압축한 **FP-Tree를 메모리에 구축 후 분할 정복** |
| **후보 집합 생성** | **필수** (1-항목 $\rightarrow$ 2-항목 $\rightarrow$ $k$-항목 후보 생성) | **전혀 없음** (후보 집합 생성 오버헤드 원천 제거) |
| **데이터베이스 스캔** | 최대 항목 집합 크기($k$)만큼 **수십 회 반복 Full Scan** | **단 2회** (1회: 빈도수 계산, 2회: FP-Tree 구축) |
| **연산 속도** | **느림** (대용량 트랜잭션에서 기하급수적 지연) | **매우 빠름** (Apriori 대비 10~100배 이상 고속) |
| **메모리 소요량** | 비교적 낮음 | 높음 (FP-Tree가 메모리에 완전히 상주해야 함) |

### Ⅴ. 보조 평가 지표: 레버리지(Leverage)와 확신도(Conviction)

#### 한줄 요약: 향상도 외에 차이 기반의 레버리지와 독립 대비 오차율을 보는 확신도를 결합한 다각도 검증

- **레버리지 (Leverage)**:
  $$\text{Leverage}(A \rightarrow B) = P(A \cap B) - P(A) \cdot P(B)$$
  - 두 사건이 독립일 때 기대되는 동시 발생 확률과 실제 동시 발생 확률 간의 **절대적 차이**를 측정 (0이면 독립)
- **확신도 (Conviction)**:
  $$\text{Conviction}(A \rightarrow B) = \frac{P(A) \cdot P(\neg B)}{P(A \cap \neg B)} = \frac{1 - P(B)}{1 - \text{Confidence}(A \rightarrow B)}$$
  - 규칙이 틀릴 확률에 대비하여 $A$와 $B$가 독립일 때 규칙이 틀릴 확률의 비율 (방향성 고려, 1이면 독립, $\infty$면 완전 참)

### Ⅵ. 산업별 실무 적용 사례 및 이상 탐지 확장

#### 한줄 요약: 유통 매장 상품 진열 및 이커머스 번들링, 그리고 사이버 보안과 IT 운영 장애 전파 분석으로 확장

### 1. 유통 및 이커머스 장바구니 추천
- 오프라인 매장에서 Lift가 높은 품목(기저귀 $\rightarrow$ 맥주)을 멀리 떨어진 코너에 배치하여 고객 동선을 늘리거나, 이커머스 결제 화면에서 "함께 사면 좋은 상품"으로 번들 추천

### 2. 사이버 침해 및 보안 이상 징후 탐지
- 침입 탐지 시스템(IDS)에서 개별 로그는 정상이지만, **"특정 포트 스캔 $\rightarrow$ 관리자 계정 생성 $\rightarrow$ 대용량 압축 파일 전송"**의 연속 시퀀스가 높은 지지도와 신뢰도를 보일 경우 APT 공격 패턴으로 자동 등록

### 3. 클라우드 마이크로서비스 장애 전파 분석
- "A 서비스 지연 $\rightarrow$ B 서비스 커넥션 풀 고갈 $\rightarrow$ C 게이트웨이 타임아웃"의 장애 연쇄 규칙을 마이닝하여 장애의 근본 원인(Root Cause) 서비스 선제 격리

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 연관규칙분석에서 가장 흔한 실수는 "높은 신뢰도(Confidence)에 속는 것"이다. 결과 항목 $B$가 원래 전 국민 90%가 사는 필수재(생수, 라면)라면 어떤 물건을 $A$에 갖다 붙여도 신뢰도는 90%가 나온다. 따라서 반드시 **향상도($Lift > 1$)**를 통해 $A$의 존재가 $B$의 구매를 통계적으로 몇 배 견인했는지를 검증해야 한다. 대규모 데이터셋에서는 Apriori의 지수적 후보 조합 생성을 피하고, 메모리 기반 **FP-Growth**나 시간 순서를 반영한 **순차 패턴 마이닝(PrefixSpan)**으로 고도화해야 한다.

> **[나라면 이렇게 쓴다]**
> 10점형 답안이라면 지지도, 신뢰도, 향상도의 수식과 벤다이어그램을 그리고 "신뢰도의 착시(생수 예시)"를 3단 차별화 포인트로 제시하겠다. 25점형이라면 Apriori와 FP-Growth의 DB 스캔 횟수 차이를 대비하고, 시간차 인과성을 분석하는 순차 패턴 마이닝(Sequential Mining) 연계 방안을 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 대중적 인기 품목에 의한 신뢰도 과대평가 착시 발생 및 대용량 트랜잭션에서 Apriori 디스크 I/O 병목
- **대응 (개선 방안)**: 향상도($Lift > 1.0$)를 최종 검증 지표로 의무화하고, FP-Tree 기반 분할정복 마이닝 및 다중 최소 지지도(Multiple Min-Support) 도입
- **검증 (검증 기준)**: Lift &gt; 1.2 이상 규칙만 프로덕션 추천 반영, FP-Growth 적용 시 마이닝 소요 시간 90% 단축 검증
- **효과 (실행 효과)**: 유효 연관 규칙 발굴을 통한 이커머스 장바구니 객단가 18% 증대 및 무의미한 노이즈 규칙 80% 제거

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">신뢰도의 착시로 무의미한 규칙 양산 및 Apriori 연산 지연</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">Lift &gt; 1.0 다각도 검증 + FP-Tree 인메모리 분할정복 마이닝</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">Lift &ge; 1.2, 최소 지지도 가지치기 검증, 마이닝 시간 90% 단축</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">크로스셀링 객단가 18% 향상 및 시스템 메모리/연산 효율 극대화</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제137회 1교시 13번 (연관 규칙 분석 지표)
  - 컴퓨터시스템응용기술사 제127회 1교시 (장바구니 분석과 Apriori 알고리즘)
  - 정보관리기술사 제119회 2교시 (연관성 분석의 지표 및 FP-Growth 알고리즘 비교)
- **표준 및 검증 출처**:
  - Rakesh Agrawal & Ramakrishnan Srikant (1994), "Fast Algorithms for Mining Association Rules", *VLDB*
  - Jiawei Han, Jian Pei, Yiwen Yin (2000), "Mining Frequent Patterns without Candidate Generation", *ACM SIGMOD*
  - Pang-Ning Tan, Michael Steinbach, Vipin Kumar, *Introduction to Data Mining (2nd Edition)*, Chapter 5
---

## 연결 토픽

- [043. 데이터마이닝 (Data Mining)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/043_data_mining.md)
- [071. 필터링 (Filtering)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/071_filtering.md)
- [005. 군집분석 (Cluster Analysis)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/005_cluster_analysis.md)
