---
sidebar:
  order: 139
  label: "139. 인과관계 (Causation)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 139
title: "인과관계(Causation)의 3대 성립 조건과 인과추론(Causal Inference) 및 A/B 테스트"
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "139"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>인과관계</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Top Title -->
  <text x="260" y="25" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">교란변수 통제 실패(허위상관) vs 무작위 대조 실험(A/B 테스트 인과확정)</text>

  <!-- Left: Confounded Spurious Correlation -->
  <rect x="20" y="40" width="225" height="135" rx="6" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
  <text x="132" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">교란요인(Z) 방치: 허위상관</text>

  <rect x="87" y="72" width="90" height="25" rx="3" fill="#ffffff" stroke="#ef4444" stroke-width="1"/>
  <text x="132" y="88" text-anchor="middle" font-size="9" fill="#1e293b">Z: 여름철 기온</text>

  <path d="M 110 97 L 65 125" stroke="#ef4444" stroke-width="1.5" marker-end="url(#arrow139)"/>
  <path d="M 155 97 L 200 125" stroke="#ef4444" stroke-width="1.5" marker-end="url(#arrow139)"/>

  <rect x="35" y="125" width="70" height="25" rx="3" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="70" y="141" text-anchor="middle" font-size="9" fill="#1e293b">X: 아이스크림</text>

  <rect x="160" y="125" width="70" height="25" rx="3" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="195" y="141" text-anchor="middle" font-size="9" fill="#1e293b">Y: 익사사고</text>

  <path d="M 105 137 L 160 137" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="132" y="152" text-anchor="middle" font-size="8" fill="#b91c1c">인과관계 없음! (가짜)</text>

  <!-- Right: Randomized Controlled Trial (RCT) -->
  <rect x="275" y="40" width="225" height="135" rx="6" fill="#dcfce7" stroke="#10b981" stroke-width="1.5"/>
  <text x="387" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">무작위 배정(RCT/A/B): 인과성립</text>

  <rect x="330" y="72" width="115" height="25" rx="3" fill="#ffffff" stroke="#10b981" stroke-width="1"/>
  <text x="387" y="88" text-anchor="middle" font-size="9" font-weight="bold" fill="#047857">개입: do(X=할인쿠폰)</text>

  <path d="M 387 97 L 387 115" stroke="#10b981" stroke-width="1.5" marker-end="url(#arrow139)"/>

  <rect x="290" y="125" width="85" height="25" rx="3" fill="#ffffff" stroke="#10b981" stroke-width="1"/>
  <text x="332" y="141" text-anchor="middle" font-size="9" fill="#1e293b">X: 쿠폰 무작위</text>

  <path d="M 375 137 L 405 137" stroke="#10b981" stroke-width="2" marker-end="url(#arrow139)"/>

  <rect x="405" y="125" width="80" height="25" rx="3" fill="#ffffff" stroke="#10b981" stroke-width="1"/>
  <text x="445" y="141" text-anchor="middle" font-size="9" fill="#1e293b">Y: 순매출 증가</text>

  <text x="387" y="165" text-anchor="middle" font-size="8" fill="#047857">교란변수 Z의 영향 완전 차단</text>

  <!-- Bottom 3 Conditions Summary -->
  <rect x="20" y="185" width="480" height="75" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="35" y="208" font-size="11" font-weight="bold" fill="#1e293b">인과관계 성립 3대 조건:</text>
  <text x="35" y="228" font-size="10" fill="#334155">1. 시간적 선행성(X가 Y보다 먼저 발생) ┃ 2. 통계적 공변성(X가 변하면 Y도 변화)</text>
  <text x="35" y="246" font-size="10" fill="#2563eb">3. 비허위성(Non-spuriousness): 제3의 교란변수 Z를 통제해도 순수 영향력 유지</text>

  <defs>
    <marker id="arrow139" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **어떤 변수(원인 $X$)의 변화가 다른 변수(결과 $Y$)의 변화를 필연적으로 유발하는 비대칭적 종속 관계이며, 단순히 두 변수가 함께 움직이는 상관관계를 넘어 원인 변수에 인위적으로 개입(Intervention, $do(X)$)했을 때 결과의 변화를 수학적으로 보장하는 성질**
- 암기: `시-공-비` (인과관계 성립 3대 조건: 시간적 선행성, 공변성, 비허위성) / `알-디-피` (3대 인과추론 기법: RCT/A/B 테스트, 이중차분법 DID, 성향점수 매칭 PSM)
- 판단축:
  - **상관관계 ($P(Y|X)$)**: 단순 관측 데이터의 수동적 연관성 측정, 대칭적 구조, 교란요인에 취약
  - **인과관계 ($P(Y|do(X))$)**: 능동적 개입(Intervention)에 따른 결과의 인과적 변화, 비대칭 구조, 교란 통제 필수
- 주의: 데이터 웨어하우스의 대용량 관측 데이터를 아무리 정밀하게 회귀분석하더라도, 무작위 실험(RCT)이나 철저한 준실험 통제 없이 상관관계를 인과관계로 단정하여 정책을 집행하면 막대한 예산 낭비와 역효과 발생
---

## 1교시 예상문제 (10점)

> 인과관계(Causation)의 3대 성립 조건과 인과추론(Causal Inference) 및 A/B 테스트의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 한 변수(원인)의 변화가 다른 변수(결과)를 필연적으로 유발하는 비대칭 관계이며, 원인 개입 시 결과 변화를 보장하는 성질 |
| **2. 3대 성립 조건** | - **시간적 선행성**: 원인이 결과보다 앞서 발생<br/>- **통계적 공변성**: 두 변수의 동시 변화<br/>- **비허위성**: 제3 교란변수 통제 시에도 관계 유지 |
| **3. 상관관계와의 차이** | 상관관계는 조건부 관측 $P(Y|X)$이자 대칭적인 반면, 인과관계는 능동적 개입 $P(Y|do(X))$이자 비대칭적 유향 관계 |
| **4. 입증 기법** | 모든 잠재적 교란변수를 무력화하는 **무작위 대조군 실험(RCT / A/B 테스트)**이 골드 스탠다드 |
---

### 핵심 관계

| 비교 항목 | 상관관계 (Correlation) | 인과관계 (Causation) |
|:---|:---|:---|
| **수학적 표현** | 조건부 확률 $P(Y | X)$ | **개입 확률 $P(Y | do(X))$** |
| **방향성** | **대칭적 ($X \leftrightarrow Y$)** | **비대칭 유향 그래프 ($X \rightarrow Y$)** |
| **목적** | 현상 관측 및 수동적 패턴 예측 | **비즈니스 개입, 처방, 정책 수립** |
| **주요 질문** | "$X$가 일어났을 때 $Y$의 값은?" | **"우리가 $X$를 바꾸면 $Y$가 어떻게 변할까?"** |
| **검증 도구** | 피어슨 상관계수, 회귀분석 $R^2$ | **무작위 A/B 테스트 (RCT), DID, DAG** |
| **주요 함정** | 제3 잠복변수로 인한 허위상관 위험 | 무작위화 실패 시 선택 편향 발생 |

---

## 2~4교시 예상문제 (25점)

> 데이터 분석 및 머신러닝 의사결정에서 상관관계(Correlation)와 인과관계(Causation)의 차이점을 비교하고, 인과관계가 성립하기 위한 3대 조건과 인과추론(Causal Inference) 기법(A/B 테스트, 준실험 설계)을 설명하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 단순 예측을 넘어 행동의 결과를 규명하는 인과관계 개요

#### 한줄 요약: 원인 변수에 대한 조작과 개입(Intervention)이 결과 변수의 실질적 변화를 유발함을 수학적으로 증명하는 관계

- **배경**:
  - 머신러닝 모델은 수천 개 피처의 상관관계를 학습하여 "무엇이 일어날지(Prediction)"는 잘 맞추지만, "우리가 쿠폰을 뿌리면 매출이 늘어날지(Prescription)"라는 정책 결정 질문에는 대답하지 못함
  - 상관관계에 의존한 잘못된 비즈니스 개입으로 인해 마케팅 예산이 낭비되고 역선택이 발생하는 문제를 극복하기 위해 인과추론 부상
- **정의**: 한 변수의 값이 변화함에 따라 다른 변수의 값이 직접적으로 유도되는 필연적 메커니즘으로, 원인 변수를 통제·조작했을 때 결과 변수가 반응하는 관계

### Ⅱ. 인과관계 성립을 위한 3대 필수 조건 (존 스튜어트 밀)

#### 한줄 요약: 시간적 선행성, 통계적 공변성, 제3의 변수에 의해 설명되지 않는 비허위성

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="20" y="20" width="150" height="120" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="95" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 시간적 선행성</text>
  <text x="95" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Temporal Precedence</text>
  <text x="95" y="92" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">원인(X)이 결과(Y)보다</text>
  <text x="95" y="108" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">시간상 반드시 앞섬</text>
  <text x="95" y="128" text-anchor="middle" font-size="9" fill="#64748b">역인과관계 배제</text>

  <!-- Box 2 -->
  <rect x="185" y="20" width="150" height="120" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="260" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. 통계적 공변성</text>
  <text x="260" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Covariation</text>
  <text x="260" y="92" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">X가 변화할 때</text>
  <text x="260" y="108" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Y도 통계적으로 변화</text>
  <text x="260" y="128" text-anchor="middle" font-size="9" fill="#64748b">상관관계 존재 필수</text>

  <!-- Box 3 -->
  <rect x="350" y="20" width="150" height="120" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="425" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. 비허위성</text>
  <text x="425" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Non-spuriousness</text>
  <text x="425" y="92" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">외생 교란변수(Z)를</text>
  <text x="425" y="108" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">완전히 통제함</text>
  <text x="425" y="128" text-anchor="middle" font-size="9" fill="#64748b">순수 인과 효과 증명</text>
</svg>
</div>

1. **시간적 선행성 (Temporal Precedence)**:
   - 원인($X$)은 결과($Y$)보다 시간적으로 앞서 발생해야 함
   - 예: '광고 노출($X$)' 이후에 '구매($Y$)'가 발생해야 인과 성립 (구매 후 광고 본 것은 인과 불가)
2. **통계적 공변성 (Covariation of Cause and Effect)**:
   - 원인 변수가 변할 때 결과 변수도 유의미하게 함께 변해야 함 ($Corr(X, Y) \neq 0$)
3. **비허위성 (Non-spuriousness / 외생변수 통제)**:
   - 두 변수 사이의 관계가 제3의 교란변수($Z$)에 의해 우연히 유발된 가짜가 아니어야 함 (가장 입증하기 어려운 핵심 조건)

### Ⅲ. 인과추론(Causal Inference)의 3대 핵심 방법론

#### 한줄 요약: 무작위 배정 실험(A/B 테스트), 인과 그래프(DAG), 준실험 설계

1. **무작위 대조군 실험 (RCT, Randomized Controlled Trial / A/B Test)**:
   - **원리**: 사용자를 동전 던지기처럼 무작위로 실험군(A)과 대조군(B)에 50:50 배정
   - **효과**: 관측된 변수뿐만 아니라 우리가 미처 모르는 모든 잠재적 교란요인($Z$)의 분포를 두 집단 간에 완벽히 균등하게 상쇄시킴으로써 순수한 처치 효과(ATE, Average Treatment Effect) 측정
   - **위상**: 인과관계를 입증하는 과학계와 IT 업계의 **골드 스탠다드(Gold Standard)**
2. **인과 다이어그램 (Causal DAG, Directed Acyclic Graph)**:
   - 주디아 펄(Judea Pearl) 교수가 정립한 그래프 모델로, 변수 간의 인과적 흐름을 유향 비순환 그래프로 시각화
   - **백도어 기준(Backdoor Criterion)**을 적용하여 어떤 교란변수를 통제해야 가짜 상관 경로가 닫히는지 수학적으로 증명
3. **준실험 설계 (Quasi-Experiment)**:
   - 윤리적/물리적 제약으로 무작위 배정이 불가능할 때 관측 데이터로부터 인과를 추출하는 기법
   - **이중차분법 (DID, Difference-in-Differences)**: 정책 적용 집단과 미적용 집단의 사전-사후 변화량의 차이를 비교하여 순수 효과 분리
   - **성향점수 매칭 (PSM, Propensity Score Matching)**: 처치를 받을 확률(성향점수)이 유사한 개체끼리 1:1 매칭하여 선택 편향 제거

### Ⅳ. 상관관계 vs 인과관계 상세 비교

#### 한줄 요약: 데이터 관측의 수동성과 정책 개입의 능동성 차이

| 비교 항목 | 상관관계 (Correlation) | 인과관계 (Causation) |
|:---|:---|:---|
| **수학적 표현** | 조건부 확률 $P(Y | X)$ | **개입 확률 $P(Y | do(X))$** |
| **방향성** | **대칭적 ($X \leftrightarrow Y$)** | **비대칭 유향 그래프 ($X \rightarrow Y$)** |
| **목적** | 현상 관측 및 수동적 패턴 예측 | **비즈니스 개입, 처방, 정책 수립** |
| **주요 질문** | "$X$가 일어났을 때 $Y$의 값은?" | **"우리가 $X$를 바꾸면 $Y$가 어떻게 변할까?"** |
| **검증 도구** | 피어슨 상관계수, 회귀분석 $R^2$ | **무작위 A/B 테스트 (RCT), DID, DAG** |
| **주요 함정** | 제3 잠복변수로 인한 허위상관 위험 | 무작위화 실패 시 선택 편향 발생 |

### Ⅴ. 반사실(Counterfactual) 추론 프레임워크

#### 한줄 요약: "만약 내가 쿠폰을 받지 않았더라면 구매했을까?"를 가상으로 비교하는 인과 분석의 철학

- **잠재적 결과 모형 (Potential Outcomes Framework, Rubin Causal Model)**:
  - 개체 $i$에 대해 처치를 받았을 때의 결과 $Y_i(1)$과 받지 않았을 때의 결과 $Y_i(0)$ 가정
  - 개별 인과 효과: $\tau_i = Y_i(1) - Y_i(0)$
  - **인과추론의 근본적 문제 (Fundamental Problem of Causal Inference)**: 동일한 개체에 대해 $Y_i(1)$과 $Y_i(0)$을 동시에 관측할 수 없음 (한쪽은 반사실로 남음)
  - **해법**: 개별 효과 대신 집단 단위의 **평균 처치 효과 (ATE, Average Treatment Effect)**를 무작위 실험(RCT)을 통해 산출:

$$\text{ATE} = E[Y(1) - Y(0)] = E[Y(1) | T=1] - E[Y(0) | T=0]$$

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 선택 편향(Selection Bias), 역인과관계(Reverse Causality), 공변량 불균형 극복

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **쿠폰 지급 고객의 높은 결제액이 가짜 효과로 판명** | 원래 결제 의향이 높은 충성 고객이 쿠폰을 적극 다운로드한 **선택 편향(Selection Bias)** | 쿠폰 자동 지급 대상을 유저 ID 해시로 무작위 분할하는 **A/B 테스트** 강제 |
| **운동을 많이 하는 사람이 병원비가 더 많이 나오는 모순** | 몸이 아픈 사람이 건강을 위해 운동을 시작한 **역인과관계(Reverse Causality)** | 원인과 결과의 시점 데이터를 분리하여 시간적 선행성($X_{t-1} \rightarrow Y_t$) 강제 검증 |
| **규제 전면 시행으로 대조군이 없어 효과 검증 난항** | 모든 고객에게 동시에 정책이 적용되어 A/B 테스트 불가 | 규제 미적용 유사 그룹을 대조군으로 선정하는 **이중차분법(DID)** 또는 합성대조군(Synthetic Control) 적용 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 지난 10년간 IT 업계는 "빅데이터와 딥러닝이 있으면 상관관계만으로 충분하다"는 빅데이터 만능주의에 취해 있었다.
> 하지만 딥러닝이 아무리 복잡한 비선형 상관관계를 찾아내도, 그것은 관측 데이터의 패턴일 뿐 **"시스템에 개입했을 때 어떤 나비효과가 발생할지"**는 절대 알려주지 못한다.
> 튜링상 수상자 주디아 펄이 설파했듯, AI가 단순한 수동적 예측가(Passive Predictor)를 넘어 진정한 지능형 의사결정자(Decision Maker)로 진화하려면 **'인과의 사다리(Ladder of Causation: 연관 $\rightarrow$ 개입 $\rightarrow$ 반사실)'**의 최고 단계로 올라서야 한다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "데이터 과학 조직의 A/B 테스트 플랫폼 내재화와 인과추론 MLOps"를 제언하겠다. 관측 데이터 기반의 상관분석은 오직 '가설 발굴 단계'에만 사용하도록 거버넌스를 제한하고, 프로덕션 배포는 사내 A/B 테스트 플랫폼(Experimentation Platform)을 통해 인과적 처치 효과(ATE)가 통계적으로 확증된 경우에만 롤아웃하는 '실험 중심 제품 엔지니어링 문화'를 구축하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 비즈니스 개입의 성공 확률을 담보하고 거짓 상관관계로 인한 자원 낭비를 차단하기 위해 인과추론 프레임워크 도입이 필수적임.
- **대응**:
  1. **A/B 테스트 플랫폼 표준화**: 신규 피처 배포 시 무작위 대조군 실험(RCT)을 전사 배포 파이프라인의 필수 품질 게이트로 수립.
  2. **인과 다이어그램(DAG) 모델링**: 데이터 분석 전 도메인 전문가와 함께 교란요인을 DAG로 도식화하고 통제 공변량 확정.
  3. **준실험 분석 파이프라인 구축**: 실험이 불가능한 전사 정책 변경은 이중차분법(DID)과 성향점수 매칭(PSM) 라이브러리를 표준 템플릿화.
- **검증**: 무작위 분할 시 SRM(Sample Ratio Mismatch) 0.1% 미만 및 평균 처치 효과(ATE) $p < 0.01$ 유의성 검증.
- **효과**: 잘못된 기능 배포에 따른 비용 손실 원천 차단 및 데이터 기반 의사결정의 과학적 성공 보장.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">관측 상관관계 맹신, 선택 편향으로 잘못된 비즈니스 개입 실패</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">인과관계 3대 조건 검증, 무작위 A/B 테스트 및 준실험(DID) 도입</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">무작위 배정 SRM 검증, 처치 효과(ATE) p &lt; 0.01 유의성 확보</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">과학적 인과 입증 및 확실한 비즈니스 ROI 창출 의사결정 완성</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제128회 정보관리 2교시: 상관관계(Correlation)와 인과관계(Causation)의 차이점 및 인과관계 입증을 위한 3대 조건과 추론 기법
- **검증 출처**:
  - Judea Pearl & Dana Mackenzie, "The Book of Why: The New Science of Cause and Effect", Basic Books
  - Guido W. Imbens & Donald B. Rubin, "Causal Inference for Statistics, Social, and Biomedical Sciences", Cambridge University Press
---

## 연결 토픽

- 상위 토픽: [03-036 기술통계](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/036_descriptive_statistics.md)
- 연관 토픽: [03-136 상관관계](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/136_correlation.md), [03-041 가설검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/041_hypothesis_testing.md), [03-130 독립 표본 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/130_independent_t_test.md)
