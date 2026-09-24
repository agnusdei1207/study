---
sidebar:
  order: 136
  label: "136. 상관관계 (Correlation)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 136
title: "상관관계(Correlation)의 통계적 척도와 허위상관 배제 및 피어슨·스피어만 검정"
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "136"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>상관관계</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Plot 1: r = +1.0 -->
  <rect x="20" y="20" width="145" height="155" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="92" y="40" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">r = +0.95 (양의 상관)</text>
  <line x1="35" y1="150" x2="150" y2="150" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="35" y1="55" x2="35" y2="150" stroke="#cbd5e1" stroke-width="1"/>
  <circle cx="50" cy="135" r="3" fill="#2563eb"/>
  <circle cx="70" cy="115" r="3" fill="#2563eb"/>
  <circle cx="90" cy="100" r="3" fill="#2563eb"/>
  <circle cx="110" cy="80" r="3" fill="#2563eb"/>
  <circle cx="130" cy="65" r="3" fill="#2563eb"/>
  <text x="92" y="165" text-anchor="middle" font-size="9" fill="#64748b">X 증가 시 Y 선형 증가</text>

  <!-- Plot 2: r = 0.0 -->
  <rect x="187" y="20" width="145" height="155" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="260" y="40" text-anchor="middle" font-size="11" font-weight="bold" fill="#475569">r = 0.00 (상관 없음)</text>
  <line x1="202" y1="150" x2="317" y2="150" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="202" y1="55" x2="202" y2="150" stroke="#cbd5e1" stroke-width="1"/>
  <circle cx="220" cy="80" r="3" fill="#64748b"/>
  <circle cx="240" cy="130" r="3" fill="#64748b"/>
  <circle cx="260" cy="70" r="3" fill="#64748b"/>
  <circle cx="280" cy="120" r="3" fill="#64748b"/>
  <circle cx="300" cy="95" r="3" fill="#64748b"/>
  <text x="260" y="165" text-anchor="middle" font-size="9" fill="#64748b">무작위 분포 또는 비선형</text>

  <!-- Plot 3: r = -0.90 -->
  <rect x="355" y="20" width="145" height="155" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="427" y="40" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">r = -0.90 (음의 상관)</text>
  <line x1="370" y1="150" x2="485" y2="150" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="370" y1="55" x2="370" y2="150" stroke="#cbd5e1" stroke-width="1"/>
  <circle cx="385" cy="65" r="3" fill="#dc2626"/>
  <circle cx="405" cy="85" r="3" fill="#dc2626"/>
  <circle cx="425" cy="105" r="3" fill="#dc2626"/>
  <circle cx="445" cy="120" r="3" fill="#dc2626"/>
  <circle cx="465" cy="140" r="3" fill="#dc2626"/>
  <text x="427" y="165" text-anchor="middle" font-size="9" fill="#64748b">X 증가 시 Y 선형 감소</text>

  <!-- Bottom Insight -->
  <rect x="20" y="190" width="480" height="55" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">핵심 교훈: 상관관계 != 인과관계 (Correlation is not Causation)</text>
  <text x="260" y="232" text-anchor="middle" font-size="10" fill="#78350f">앤스컴 콰르텟: 수치 r만 보지 말고 반드시 산점도 시각화 및 제3의 잠복변수(허위상관) 통제 필수</text>
</svg>
</div>

- 본질: **두 연속형 또는 순위 확률변수 간에 한 변수가 변화할 때 다른 변수가 함께 증가하거나 감소하는 통계적 연관성의 방향과 강도를 -1부터 +1 사이의 무차원 표준화 수치로 나타내는 척도이며, 결코 두 변수 간의 원인과 결과(인과관계)를 보장하지 않음**
- 암기: `피-스-켄-편` (4대 상관계수: 피어슨 모수/선형, 스피어만 비모수/순위, 켄달 타우 일치도, 편상관계수 통제) / `앤-허-잠` (주의점: 앤스컴 콰르텟, 허위 상관 Spurious Correlation, 잠복변수 통제)
- 판단축:
  - **피어슨($r$) vs 스피어만($\rho$)**: 연속형 정규분포 및 선형 관계 vs 서열/순위 척도, 극단치 존재 또는 비선형 단조 관계
  - **상관관계 vs 인과관계**: 두 사건의 대칭적 동시 관측($Corr(X,Y) = Corr(Y,X)$) vs 비대칭적 원인-결과 및 개입 효과($X \rightarrow Y$)
- 주의: 제3의 공통 원인(잠복변수)이 개입하면 실제 아무 인과가 없음에도 통계적으로 $r \ge 0.9$ 이상의 극단적 **허위 상관(Spurious Correlation)**이 발생하므로 비즈니스 의사결정 시 맹목적 신뢰 금지
---

## 1교시 예상문제 (10점)

> 상관관계(Correlation)의 통계적 척도와 허위상관 배제 및 피어슨·스피어만 검정의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 두 변수 간의 통계적 선형/단조적 연관성의 방향과 강도를 -1부터 +1 사이로 표준화한 무차원 척도 |
| **2. 주요 유형** | - **피어슨**: 연속형 정규분포 선형 상관계수 (모수)<br/>- **스피어만**: 순위 척도 기반 단조 상관계수 (비모수, 이상치 강건)<br/>- **편상관계수**: 제3 잠복변수를 통제한 순수 상관 |
| **3. 인과관계와의 차이** | 상관관계는 대칭적 동시 관측($Corr(X,Y)=Corr(Y,X)$)인 반면, 인과관계는 비대칭적 원인-결과 개입 효과 |
| **4. 허위 상관 주의** | 공통 잠복변수로 인한 가짜 상관에 속지 않기 위해 산점도 시각화 및 편상관 통제 필수 |
---

### 핵심 관계

| 비교 항목 | 공분산 (Covariance) | 상관관계 (Correlation) | 인과관계 (Causation) |
|:---|:---|:---|:---|
| **정의** | 두 변수가 함께 변화하는 경향성 | 공분산을 표준화한 **연관성의 강도 및 방향** | 한 변수가 다른 변수를 **직접 일으키는 원인-결과** |
| **수치 범위** | $-\infty \sim +\infty$ | **$-1.0 \le r \le +1.0$** | 방향성 및 처치 효과(ATE) 크기 |
| **단위 의존성** | 측정 단위에 비례 (단위 존재) | **무차원 수치 (단위 없음)** | 결과 변수의 단위 |
| **대칭성** | $Cov(X, Y) = Cov(Y, X)$ | **$Corr(X, Y) = Corr(Y, X)$** | **비대칭 ($X \rightarrow Y \neq Y \rightarrow X$)** |
| **개입(Intervention)**| 개입 시 결과 예측 불가 | 개입 시 결과 예측 불가 | **원인 $X$를 조작 시 결과 $Y$ 변화 보장** |

---

## 2~4교시 예상문제 (25점)

> 상관관계(Correlation)와 인과관계(Causation)의 개념적 차이를 설명하고, 상관분석의 주요 계수(피어슨, 스피어만) 비교 및 허위 상관(Spurious Correlation)의 발생 원인과 판별 방안을 기술하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 통계적 연관성의 기초 척도: 상관관계 개요

#### 한줄 요약: 두 변수가 서로 얼마나 밀접하게 함께 움직이는지 선형적 연관성의 방향과 크기를 -1과 +1 사이로 표준화한 척도

- **배경**:
  - 마케팅, 금융, 헬스케어 등 모든 데이터 분석에서 "두 지표가 함께 움직이는가?"를 규명하는 것은 가설 수립의 첫 단계임
  - 공분산(Covariance)은 측정 단위(cm, kg 등)에 따라 수치가 제각각이어서 객관적 비교가 불가능하므로, 표준편차로 나눈 표준화 지표 필요
- **정의**: 두 확률변수 $X$와 $Y$ 간의 통계적 공변(Covariation) 패턴을 측정하는 척도로, $-1 \le r \le 1$ 범위의 값을 가짐
- **핵심 통계적 성질**:
  - **무차원 수치**: 단위에 무관하게 직관적 비교 가능
  - **대칭성**: $Corr(X, Y) = Corr(Y, X)$ (원인과 결과의 방향성이 없음)
  - **선형성 국한**: 피어슨 상관계수는 오직 직선 형태의 관계만 측정 가능

### Ⅱ. 상관계수의 4대 주요 유형

#### 한줄 요약: 모수적 선형 피어슨, 비모수적 순위 스피어만/켄달, 제3변수를 통제하는 편상관계수

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="115" height="120" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="72" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">1. 피어슨 (Pearson)</text>
  <text x="72" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">모수 통계</text>
  <text x="72" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">연속형 정규분포</text>
  <text x="72" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">엄격한 선형 관계</text>
  <text x="72" y="128" text-anchor="middle" font-size="8" fill="#64748b">이상치에 민감</text>

  <!-- Box 2 -->
  <rect x="140" y="20" width="115" height="120" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="197" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#0284c7">2. 스피어만 (Spearman)</text>
  <text x="197" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">비모수 통계</text>
  <text x="197" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">서열/순위 척도</text>
  <text x="197" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">단조(Monotonic)</text>
  <text x="197" y="128" text-anchor="middle" font-size="8" fill="#64748b">이상치에 강건</text>

  <!-- Box 3 -->
  <rect x="265" y="20" width="115" height="120" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="322" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#059669">3. 켄달 (Kendall Tau)</text>
  <text x="322" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">비모수 통계</text>
  <text x="322" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">순위 쌍 일치도</text>
  <text x="322" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">소표본 고정밀</text>
  <text x="322" y="128" text-anchor="middle" font-size="8" fill="#64748b">동순위 처리에 우수</text>

  <!-- Box 4 -->
  <rect x="390" y="20" width="115" height="120" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="447" y="45" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">4. 편상관 (Partial)</text>
  <text x="447" y="70" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">제3 변수 통제</text>
  <text x="447" y="90" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">외생 교란 배제</text>
  <text x="447" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #334155)">순수 상관 추출</text>
  <text x="447" y="128" text-anchor="middle" font-size="8" fill="#64748b">허위 상관 검출</text>
</svg>
</div>

1. **피어슨 상관계수 (Pearson $r$)**:
   - 두 연속형 변수가 모두 정규분포를 따를 때, 두 변수 간의 선형 관계 강도를 측정:

$$r = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum (X_i - \bar{X})^2} \sqrt{\sum (Y_i - \bar{Y})^2}} = \frac{Cov(X, Y)}{s_X s_Y}$$

2. **스피어만 순위상관계수 (Spearman $\rho$)**:
   - 원시 데이터의 수치 대신 순위(Rank)를 매겨 피어슨 상관계수를 계산한 비모수 척도로, 비선형이지만 단조 증가/감소하는 관계 및 이상치에 강건
3. **켄달의 타우 (Kendall's $\tau$)**:
   - 모든 가능한 순서쌍 간의 일치 쌍(Concordant)과 불일치 쌍(Discordant)의 비율 차이를 측정하며, 소표본($n < 30$)에서 스피어만보다 정확
4. **편상관계수 (Partial Correlation)**:
   - 제3의 잠복변수 $Z$의 영향을 선형적으로 제거(잔차화)한 상태에서 $X$와 $Y$ 사이의 순수한 상관관계를 분리 산출

### Ⅲ. 상관계수의 유의성 검정 (Hypothesis Testing)

#### 한줄 요약: 표본 상관계수 $r$이 우연이 아닌 모상관계수 $\rho \neq 0$임을 입증하는 t-검정

- **가설 설정**:
  - 귀무가설($H_0$): $\rho = 0$ (모집단에서 두 변수 간 상관관계가 없다)
  - 대립가설($H_1$): $\rho \neq 0$ (모집단에서 두 변수 간 상관관계가 존재한다)
- **검정통계량 수식**:

$$t = \frac{r \sqrt{n - 2}}{\sqrt{1 - r^2}}, \quad df = n - 2$$

- **해석 주의점**: 표본 크기 $n$이 수만 건 이상으로 매우 커지면, 아무 의미 없는 $r = 0.05$의 사소한 상관성도 $p < 0.001$로 통계적 유의성이 채택되므로, 실질적 상관 강도($|r| \ge 0.4$)를 반드시 병행 평가해야 함

### Ⅳ. 상관관계 vs 공분산 vs 인과관계 3대 개념 비교

#### 한줄 요약: 척도의 표준화 여부와 인과적 방향성의 존재 여부에 따른 명확한 구분

| 비교 항목 | 공분산 (Covariance) | 상관관계 (Correlation) | 인과관계 (Causation) |
|:---|:---|:---|:---|
| **정의** | 두 변수가 함께 변화하는 경향성 | 공분산을 표준화한 **연관성의 강도 및 방향** | 한 변수가 다른 변수를 **직접 일으키는 원인-결과** |
| **수치 범위** | $-\infty \sim +\infty$ | **$-1.0 \le r \le +1.0$** | 방향성 및 처치 효과(ATE) 크기 |
| **단위 의존성** | 측정 단위에 비례 (단위 존재) | **무차원 수치 (단위 없음)** | 결과 변수의 단위 |
| **대칭성** | $Cov(X, Y) = Cov(Y, X)$ | **$Corr(X, Y) = Corr(Y, X)$** | **비대칭 ($X \rightarrow Y \neq Y \rightarrow X$)** |
| **개입(Intervention)**| 개입 시 결과 예측 불가 | 개입 시 결과 예측 불가 | **원인 $X$를 조작 시 결과 $Y$ 변화 보장** |

### Ⅴ. 허위 상관(Spurious Correlation)과 앤스컴 콰르텟

#### 한줄 요약: 제3의 공통 원인으로 인한 통계적 착시와 수치 맹신의 위험성

1. **허위 상관 (Spurious Correlation)의 메커니즘**:
   - 사례: "아이스크림 판매량($X$)"과 "해수욕장 익사 사고 건수($Y$)" 간에 $r = 0.92$의 강한 양의 상관이 관측됨
   - 원인: 두 변수 사이에 인과가 있는 것이 아니라, '여름철 기온 상승'이라는 **공통 잠복변수(Confounder)**가 양쪽을 동시에 증가시킨 것임
   - 판별법: 기온을 통제한 편상관분석을 수행하면 순수 상관계수는 0으로 수렴함
2. **앤스컴 콰르텟 (Anscombe's Quartet)의 교훈**:
   - 1973년 프랜시스 앤스컴이 고안한 4개의 서로 다른 데이터셋은 평균, 분산, 회귀선, 상관계수($r = 0.816$)가 소수점까지 완벽히 일치함
   - 그러나 산점도를 그려보면 (1) 정상 선형, (2) 2차 곡선, (3) 단 하나의 극단 이상치, (4) 수직선 데이터로 완전히 다름
   - **엔지니어링 원칙**: 수치 상관계수만 보지 말고 반드시 **데이터 시각화(산점도)**를 병행해야 함

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 이상치로 인한 상관계수 뻥튀기 방지, 비선형 관계 포착, 잠복변수 통제

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **소수 이상치로 인해 r=0.1이 r=0.8로 급상승** | 극단 지렛대점(Leverage)이 피어슨 제곱합 오차를 왜곡 | 로버스트한 **스피어만 순위상관계수**로 전환하거나 사분위수(IQR) 기반 이상치 필터링 |
| **$U$자형 곡선 관계를 '무상관'으로 오판** | 피어슨 상관계수의 선형성(Linearity) 가정 한계 | 데이터 산점도 확인 후 다항식 변환 또는 상호정보량(Mutual Information) 비선형 지표 도입 |
| **허위 상관 기반 마케팅 집행으로 예산 낭비** | 앱 체류 시간과 결제액 간의 잠복변수(유저 충성도) 미통제 | 충성도 등급을 공변량으로 통제하는 **편상관분석** 또는 무작위 A/B 테스트 검증 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 빅데이터 시대에 데이터가 많아질수록 가장 흔하게 발생하는 함정은 "아무런 상관이 없는 수천만 개 지표들 사이에서 우연히 발견되는 허위 상관(Spurious Correlation)"이다.
> 데이터베이스에 있는 모든 컬럼을 전수 교차하여 상관계수 히트맵(Heatmap)을 돌리면, 우연히 $r \ge 0.8$이 넘는 지표가 수백 개씩 쏟아져 나온다.
> 엔지니어와 분석가는 이를 "위대한 데이터 발견"으로 착각하기 쉽지만, 통계적으로 다중 비교(Multiple Testing)에 의한 우연의 일치일 뿐이다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "상관분석에서 인과추론(Causal Inference)으로의 패러다임 전환"을 제언하겠다. 상관분석은 오직 '탐색적 가설 발굴' 단계에만 제한하고, 실제 시스템 변경이나 비즈니스 정책 결정 단계에서는 무작위 대조군 A/B 테스트(RCT)나 인과 다이어그램(DAG) 기반의 교란요인 통제를 의무화하는 전사 의사결정 거버넌스를 수립하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 데이터 분석 시 단순 상관관계를 인과관계로 오인하여 발생하는 정책 실패와 예산 낭비를 방지하기 위한 체계적 검증이 필수적임.
- **대응**:
  1. **산점도 시각화 의무화**: 상관계수 산출 시 Anscombe's Quartet 왜곡을 배제하기 위해 산점도 시각화 파이프라인 필수 결합.
  2. **비모수 계수 병행 산출**: 정규성 위배 및 이상치 리스크를 방어하기 위해 피어슨과 스피어만 계수를 상호 대조.
  3. **편상관 기반 잠복변수 통제**: 강한 상관관계 발견 시 주요 공변량을 통제한 편상관계수를 산출하여 허위 상관 여부 검증.
- **검증**: 상관계수 t-검정 $p < 0.01$ 및 편상관 분석 전후 상관계수 유지율 검증.
- **효과**: 가짜 상관관계에 기반한 오판 차단 및 고신뢰성 비즈니스 피처 도출.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">피어슨 r 수치 맹신, 이상치 왜곡, 잠복변수로 인한 허위상관 오판</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">산점도 병행 검증, 스피어만 비모수 대조, 편상관계수 통제</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">t-검정 유의성(p &lt; 0.01), 편상관 유지율 검증, 비선형 여부 확인</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">허위 상관 배제 및 신뢰성 높은 비즈니스 인사이트 도출</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제128회 정보관리 1교시: 상관관계(Correlation)와 인과관계(Causation)의 차이점 및 상관계수의 유형과 통계적 검정
- **검증 출처**:
  - F. J. Anscombe, "Graphs in Statistical Analysis", The American Statistician
  - Douglas C. Montgomery, "Applied Statistics and Probability for Engineers", Wiley
---

## 연결 토픽

- 상위 토픽: [03-036 기술통계](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/036_descriptive_statistics.md)
- 연관 토픽: [03-139 인과관계](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/139_causation.md), [03-121 다중회귀분석](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/121_multiple_regression_analysis.md)
