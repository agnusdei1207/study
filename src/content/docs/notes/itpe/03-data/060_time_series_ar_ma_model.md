---
sidebar:
  order: 60
  label: "060. 시계열 AR·MA 모형"
  badge:
    text: "기초"
    variant: note
title: "시계열 AR·MA 모형 (자기회귀 및 이동평균 모형) 및 ARIMA"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 60
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "060"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>시계열 AR·MA 모형</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-box" role="img" aria-label="AR 및 MA 시계열 모형 구조 및 ACF PACF 식별 패턴도">
<svg viewBox="0 0 520 230" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-ts" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
    <filter id="shadow-ts" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="rgba(0,0,0,0.1)"/>
    </filter>
  </defs>

  <!-- AR 모형 카드 -->
  <rect x="15" y="15" width="235" height="150" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" filter="url(#shadow-ts)"/>
  <text x="132" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">자기회귀 모형: AR(p)</text>
  <text x="132" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">과거 "자기 관측치"의 선형 결합 (관성)</text>
  <text x="132" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">Y_t = c + Σ φ_i · Y_{t-i} + ε_t</text>

  <line x1="25" y1="75" x2="240" y2="75" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>

  <rect x="25" y="85" width="215" height="30" rx="3" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="35" y="104" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-foreground, #0f172a)">ACF: 지수적 점진 감쇄 (Tails off)</text>

  <rect x="25" y="122" width="215" height="30" rx="3" fill="rgba(37, 99, 235, 0.08)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.2"/>
  <text x="35" y="141" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">PACF: p차수 이후 절단 (Cuts off)</text>

  <!-- MA 모형 카드 -->
  <rect x="270" y="15" width="235" height="150" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow-ts)"/>
  <text x="387" y="35" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#10b981" text-anchor="middle">이동평균 모형: MA(q)</text>
  <text x="387" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">과거 "외부 충격(오차항)"의 선형 결합</text>
  <text x="387" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">Y_t = μ + ε_t + Σ θ_j · ε_{t-j}</text>

  <line x1="280" y1="75" x2="495" y2="75" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>

  <rect x="280" y="85" width="215" height="30" rx="3" fill="rgba(16, 185, 129, 0.08)" stroke="#10b981" stroke-width="1.2"/>
  <text x="290" y="104" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" font-weight="700" fill="#10b981">ACF: q차수 이후 절단 (Cuts off)</text>

  <rect x="280" y="122" width="215" height="30" rx="3" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="290" y="141" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-foreground, #0f172a)">PACF: 지수적 점진 감쇄 (Tails off)</text>

  <!-- 하단 정상성 및 ARIMA 확장 바 -->
  <rect x="15" y="175" width="490" height="42" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="260" y="193" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">전제: 정상성(Stationarity: 평균·분산 일정) 필수 ── 비정상 시 차분(d) 후 ARIMA(p, d, q) 확장</text>
  <text x="260" y="208" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">식별 공식: AR은 PACF 절단(p), MA는 ACF 절단(q) ── Box-Jenkins 4단계 절차 적용</text>
</svg>
</div>

- 본질: **시간의 흐름에 따라 순차 관측된 정상 시계열(Stationary Time Series) 데이터의 확률적 자기상관 구조를 수학적으로 모형화하기 위해, 과거 자신의 관측치에 의존하는 자기회귀(AR) 모형과 과거 예측 오차(충격)에 의존하는 이동평균(MA) 모형을 결합한 전통 통계적 예측 체계**
- 암기: `정-식-추-진` (정상성 검정, 모형 식별, 모수 추정, 잔차 진단 - Box-Jenkins 4단계) / `에이-피(AR-PACF절단) vs 엠-에이(MA-ACF절단)`
- 판단축:
  - **AR($p$) 모형**: 과거 시점의 충격이 계수($\phi$)를 타고 미래로 영구히 감쇄하며 전파되는 '관성(Momentum)' 모델링 $\rightarrow$ PACF가 $p$에서 절단
  - **MA($q$) 모형**: 과거 시점의 충격이 정확히 $q$ 시점까지만 영향을 미치고 이후 완전히 소멸하는 '유한 충격(Transitory Shock)' 모델링 $\rightarrow$ ACF가 $q$에서 절단
- 주의: 현실의 대다수 데이터(주가, 트래픽, 전력 사용량 등)는 평균이나 분산이 시간에 따라 변하는 비정상(Non-stationary) 시계열이므로, 직접 적용 시 '허위 회귀(Spurious Regression)'가 발생함. 반드시 차분(Differencing)을 통해 정상화한 후 ARIMA($p, d, q$)로 확장해야 함
---

## 1교시 예상문제 (10점)

> 시계열 AR·MA 모형 (자기회귀 및 이동평균 모형) 및 ARIMA의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 자기회귀모형(AR)과 이동평균모형(MA)의 개념

- **자기회귀모형 (AR)**: 현재 데이터가 과거 자기 자신의 관측치 선형결합으로 결정되는 모형 (관성 반영)
- **이동평균모형 (MA)**: 현재 데이터가 과거 외부 충격(백색잡음 오차항)들의 선형결합으로 결정되는 모형 (유한 충격)
- **핵심 전제**: 시계열의 평균과 분산이 시간에 무관하게 일정한 **정상성(Stationarity)** 충족 필수

### 2. 모형별 수식 및 식별 패턴 비교

| 구분 | 자기회귀모형 (AR($p$)) | 이동평균모형 (MA($q$)) |
|---|---|---|
| **기본 수식** | $Y_t = c + \sum \phi_i Y_{t-i} + \epsilon_t$ | $Y_t = \mu + \epsilon_t + \sum \theta_j \epsilon_{t-j}$ |
| **충격 지속성** | 무한히 점진적 감쇄 (관성 유지) | $q$ 시점 경과 후 완전히 소멸 |
| **ACF 패턴** | **지수적 점진 감쇄 (Tails off)** | **$q$차수 이후 급격 절단 (Cuts off)** |
| **PACF 패턴** | **$p$차수 이후 급격 절단 (Cuts off)** | **지수적 점진 감쇄 (Tails off)** |

### 3. 차별화 제언

- 비정상 시계열은 차분($d$)을 거쳐 **ARIMA($p, d, q$)**로 변환하고, 경량 통계 모형(ARIMA)을 1차 신뢰 밴드 이상 탐지 엔진으로 활용하여 실시간성을 극대화함
---

## 2~4교시 예상문제 (25점)

> 시계열 분석에서 사용되는 자기회귀모형(Autoregressive Model)과 이동평균모형(Moving Average Model)의 개념, 수식 및 동작 특성을 설명하고, 정상성(Stationarity)의 조건과 자기상관함수(ACF) 및 편자기상관함수(PACF)를 활용한 모형 식별 방법을 비교하시오. (10점 / 25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 시간 경과에 따른 자기상관성을 규명하는 시계열 모형 개요

- **시계열 분석의 본질**:
  - 독립변수와 종속변수 간의 관계를 다루는 일반 회귀분석과 달리, **동일한 변수의 시간 경과에 따른 자기 자신과의 상관성(Autocorrelation)**을 분석함
- **정상성(Stationarity, 약정상성) 3대 조건**:
  1. **일정한 평균**: 모든 시점 $t$에 대해 평균이 일정함 ($E[Y_t] = \mu$)
  2. **일정한 분산**: 모든 시점 $t$에 대해 분산이 일정함 ($Var(Y_t) = \sigma^2 < \infty$)
  3. **시차 의존 공분산**: 두 시점 $t, t-k$ 간의 공분산은 절대 시점 $t$가 아닌 오직 시차(Lag, $k$)에만 의존함 ($Cov(Y_t, Y_{t-k}) = \gamma_k$)

#### 한줄 요약

- 과거 관측치와 예측 오차의 확률적 결합을 통해 미래 시계열 값을 예측하는 선형 통계 모형과 정상성 조건임

### Ⅱ. 자기회귀모형 (AR, Autoregressive Model)

- **수학적 정의 (AR($p$))**:
  $$Y_t = c + \sum_{i=1}^{p} \phi_i Y_{t-i} + \epsilon_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + \epsilon_t$$
  - $Y_t$: 시점 $t$에서의 관측값
  - $\phi_i$: 시차 $i$에 대한 자기회귀 계수 (영향력의 크기)
  - $\epsilon_t$: 백색잡음(White Noise, $\epsilon_t \sim i.i.d. N(0, \sigma^2)$)
- **핵심 동작 특성**:
  - **영구적 충격 전파**: 과거의 충격 $\epsilon_{t-k}$가 계수 $\phi$의 거듭제곱 형태로 미래 시점까지 점진적으로 감쇄하며 장기적으로 잔류함
  - **정상성 조건 (AR(1))**: $|\phi_1| < 1$ 이어야 시계열이 발산하지 않고 정상성을 만족함 ($\phi_1 = 1$이면 Random Walk 단위근 발생)

#### 한줄 요약

- 현재 시점의 데이터를 과거 $p$개 시점의 자기 자신 관측치들의 가중합과 백색잡음의 합으로 표현하는 모형임

### Ⅲ. 이동평균모형 (MA, Moving Average Model)

- **수학적 정의 (MA($q$))**:
  $$Y_t = \mu + \epsilon_t + \sum_{j=1}^{q} \theta_j \epsilon_{t-j} = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q}$$
  - $\mu$: 시계열의 기저 기대값(평균)
  - $\theta_j$: 시차 $j$에서의 오차항에 대한 이동평균 계수
  - $\epsilon_t$: 시점 $t$에서 발생한 예측 불가능한 외부 충격(Innovation / Shock)
- **핵심 동작 특성**:
  - **유한한 충격 지속**: $t$ 시점에 발생한 충격 $\epsilon_t$는 정확히 $t+q$ 시점까지만 영향을 미치며, $t+q+1$ 시점부터는 영향력이 완전히 0으로 소멸함
  - **자체적 정상성**: 계수 $\theta$의 값과 무관하게 유한 차수 MA 모형은 항상 정상성 조건을 충족함 (가역성 조건: $|\theta_1| < 1$)

#### 한줄 요약

- 현재 시점의 데이터를 현재 및 과거 $q$개 시점의 백색잡음(외부 충격)들의 선형 결합으로 표현하는 모형임

### Ⅳ. AR 모형 vs MA 모형 심층 비교 및 ACF/PACF 식별 메커니즘

<div class="itpe-diagram-box" role="img" aria-label="ACF 및 PACF 식별 패턴 도해">
<svg viewBox="0 0 520 160" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <!-- AR(1) 패턴 -->
  <rect x="15" y="15" width="240" height="135" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.2"/>
  <text x="135" y="33" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">AR(p) 식별 지문</text>
  <text x="25" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">- ACF : 지수적 점진 감쇄 (Tails off)</text>
  <text x="25" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-accent, #2563eb)">- PACF: Lag p 이후 급격 절단 (Cuts off)</text>
  <!-- PACF 절단 미니 바 차트 -->
  <line x1="30" y1="110" x2="230" y2="110" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <rect x="50" y="85" width="12" height="25" fill="var(--sl-color-accent, #2563eb)"/>
  <text x="56" y="125" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">1</text>
  <rect x="80" y="95" width="12" height="15" fill="var(--sl-color-accent, #2563eb)"/>
  <text x="86" y="125" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">p</text>
  <line x1="115" y1="108" x2="115" y2="112" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2"/>
  <text x="145" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#ef4444">&gt; p 이후 0으로 절단</text>

  <!-- MA(1) 패턴 -->
  <rect x="265" y="15" width="240" height="135" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="#10b981" stroke-width="1.2"/>
  <text x="385" y="33" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#10b981" text-anchor="middle">MA(q) 식별 지문</text>
  <text x="275" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="#10b981">- ACF : Lag q 이후 급격 절단 (Cuts off)</text>
  <text x="275" y="68" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">- PACF: 지수적 점진 감쇄 (Tails off)</text>
  <!-- ACF 절단 미니 바 차트 -->
  <line x1="280" y1="110" x2="480" y2="110" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <rect x="300" y="85" width="12" height="25" fill="#10b981"/>
  <text x="306" y="125" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">1</text>
  <rect x="330" y="92" width="12" height="18" fill="#10b981"/>
  <text x="336" y="125" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">q</text>
  <line x1="365" y1="108" x2="365" y2="112" stroke="#10b981" stroke-width="2"/>
  <text x="395" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#ef4444">&gt; q 이후 0으로 절단</text>
</svg>
</div>

| 비교 항목 | 자기회귀모형 (AR($p$)) | 이동평균모형 (MA($q$)) | 결합모형 (ARMA($p, q$)) |
|:---|:---|:---|:---|
| **기본 수식** | $Y_t = c + \sum \phi_i Y_{t-i} + \epsilon_t$ | $Y_t = \mu + \epsilon_t + \sum \theta_j \epsilon_{t-j}$ | $Y_t = c + \sum \phi_i Y_{t-i} + \epsilon_t + \sum \theta_j \epsilon_{t-j}$ |
| **핵심 철학** | 이전 상태의 관성(Momentum) 모델링 | 예기치 못한 단기적 쇼크(Shock) 모델링 | 관성과 외부 충격을 동시 고려 |
| **ACF 패턴** | **점진적 감쇄 (Tails off)** | **$q$차수 이후 절단 (Cuts off)** | 점진적 감쇄 (Tails off) |
| **PACF 패턴** | **$p$차수 이후 절단 (Cuts off)** | **점진적 감쇄 (Tails off)** | 점진적 감쇄 (Tails off) |
| **충격 지속성** | 무한 감쇄 (Memory fades gradually) | 유한 지속 ($q$ 기간 후 효과 제로) | 무한 감쇄 |
| **모형 차수 결정** | PACF가 0으로 떨어지는 직전 차수 $p$ | ACF가 0으로 떨어지는 직전 차수 $q$ | AIC / BIC 정보 기준 최소화 지점 탐색 |

#### 한줄 요약

- AR은 PACF가 $p$에서 잘리고, MA는 ACF가 $q$에서 잘리는 특성을 통해 모형과 차수를 감별함

### Ⅴ. 비정상 시계열 확장을 위한 ARIMA 및 SARIMA 모델링

- **ARIMA($p, d, q$) (Autoregressive Integrated Moving Average)**:
  - $p$: 자기회귀(AR) 차수
  - $d$: 정상 시계열로 만들기 위한 차분(Differencing) 횟수 (보통 1회 또는 2회)
  - $q$: 이동평균(MA) 차수
- **SARIMA (Seasonal ARIMA)**:
  - 주간, 월간, 연간 주기성을 갖는 시계열을 위해 계절 차분과 계절 AR/MA 항을 결합: $\text{ARIMA}(p, d, q) \times (P, D, Q)_s$ ($s$: 계절 주기 길이)

#### 한줄 요약

- 차분($d$)을 통해 비정상 시계열을 정상화한 ARIMA와 계절성을 반영한 SARIMA로 실무 예측을 확장함

### Ⅵ. Box-Jenkins 방법론과 실무 시계열 분석 프로세스

<div class="itpe-diagram-box" role="img" aria-label="Box-Jenkins 4단계 시계열 분석 프로세스">
<svg viewBox="0 0 520 80" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-bj" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
  </defs>

  <!-- 1단계 -->
  <rect x="15" y="15" width="110" height="50" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="70" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">1. 모형 식별</text>
  <text x="70" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">ADF 단위근 검정</text>
  <text x="70" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="7.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">ACF / PACF 분석</text>

  <path d="M 125 40 L 140 40" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-bj)"/>

  <!-- 2단계 -->
  <rect x="140" y="15" width="110" height="50" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="195" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">2. 모수 추정</text>
  <text x="195" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">MLE / OLS 추정</text>
  <text x="195" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="7.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">AIC / BIC 최소화</text>

  <path d="M 250 40 L 265 40" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-bj)"/>

  <!-- 3단계 -->
  <rect x="265" y="15" width="115" height="50" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="322" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">3. 잔차 진단</text>
  <text x="322" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">Ljung-Box Q-검정</text>
  <text x="322" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="7.5" fill="#10b981" text-anchor="middle">백색잡음 여부 확인</text>

  <path d="M 380 40 L 395 40" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-bj)"/>

  <!-- 4단계 -->
  <rect x="395" y="15" width="110" height="50" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="#10b981" stroke-width="1.5"/>
  <text x="450" y="34" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#10b981" text-anchor="middle">4. 미래 예측</text>
  <text x="450" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">점 예측치 산출</text>
  <text x="450" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="7.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">95% 신뢰구간 생성</text>
</svg>
</div>

| 단계 | 주요 활동 내용 | 검증 및 평가 도구 |
|---|---|---|
| **1. 모형 식별 (Identification)** | 단위근 검정으로 정상성 확인, 비정상 시 차분 수행 후 ACF/PACF로 $p, q$ 후보 차수 도출 | ADF Test, ACF/PACF Plot |
| **2. 모수 추정 (Estimation)** | 최대우도추정법(MLE)으로 계수 추정 및 정보 기준 최소화 모델 선별 | AIC, BIC |
| **3. 모형 진단 (Diagnostic)** | 모델 잔차(Residual)가 백색잡음인지 자기상관성 부재 검증 | Ljung-Box Q-Test |
| **4. 미래 예측 (Forecasting)** | 최종 검증된 모델로 미래 시점의 기대값 및 95% 신뢰구간 산출 | RMSE, MAPE |

#### 한줄 요약

- 식별, 추정, 진단, 예측의 4단계 Box-Jenkins 절차를 통해 최적 모형을 과학적으로 도출함

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> "최신 딥러닝이 유행해도 통계적 시계열 모형의 수학적 투명성과 경량 연산성은 대체 불가능하다." 데이터센터 트래픽이나 서버 CPU 사용률의 이상 탐지 파이프라인에서 무거운 Transformer 시계열 모델(PatchTST)을 매 초 실행하면 추론 비용과 지연시간이 감당되지 않는다. 반면 ARIMA 모델은 수 밀리초 내에 미래 기대값과 $3\sigma$ 신뢰구간을 산출하므로 실시간 이상 탐지의 1차 방어선으로 최적이다. 통계 모형의 설명력과 딥러닝의 비선형 표현력을 결합하는 하이브리드 아키텍처가 엔지니어링의 정답이다.

> **[나라면 이렇게 쓴다]**
> 25점 답안 4단락 차별화로 "통계 시계열(ARIMA) + 딥러닝 융합 기반의 실시간 이상치 탐지 파이프라인"을 제시하겠다. 1계층에서 경량 ARIMA/SARIMA로 정상 시계열의 $3\sigma$ 신뢰 밴드(Confidence Band)를 실시간 생성하여 95%의 통상 데이터를 고속 필터링하고, 신뢰 밴드를 벗어난 이상 징후 구간에 한해 2계층 Autoencoder/LSTM 딥러닝 모델로 심층 원인 분석을 수행하는 2단계 하이브리드 관측 아키텍처를 제언한다.

### 실전 답안용 기술사적 제언

- **[비정상 시계열 직접 적용 시 허위 회귀 한계]**: 추세와 계절성을 지닌 시계열을 전처리 없이 적용할 경우 가짜 상관관계 및 예측 신뢰도 왜곡 발생
- **[실무 최적화 방안]**: ADF 단위근 검정과 1차 차분을 거쳐 정상성을 확보한 후 Box-Jenkins 4단계 표준 절차에 따라 AIC/BIC 최소 모델 선정
- **[실시간 이상치 탐지 파이프라인 연계]**: ARIMA 기반 미래 예측 신뢰구간($\hat{Y}_t \pm 3\sigma$)을 생성하고 실제 관측치 이탈 시 즉시 경보를 발행하는 실시간 모니터링 엔진 구현

<div class="itpe-flow-map" role="group" aria-label="시계열 모델링 최적화 4단계 흐름">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">1</div>
    <div class="itpe-flow-step__title">현행 한계</div>
    <div class="itpe-flow-step__desc">비정상 시계열 미차분 시 허위 회귀 발생 및 모델 차수 임의 선정 오류</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">2</div>
    <div class="itpe-flow-step__title">개선 방안</div>
    <div class="itpe-flow-step__desc">ADF 단위근 검정 + 차분(d) 후 ACF/PACF 및 AIC 최소화 기반 Box-Jenkins 적용</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">3</div>
    <div class="itpe-flow-step__title">검증 기준</div>
    <div class="itpe-flow-step__desc">Ljung-Box 잔차 독립성 p &gt; 0.05 통과, MAPE &lt; 5% 신뢰구간 형성</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">4</div>
    <div class="itpe-flow-step__title">실행 효과</div>
    <div class="itpe-flow-step__desc">서버 트래픽 이상치 실시간 탐지율 98% 달성 및 장애 선제 차단</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- 정보관리기술사 제138회 1교시 7번: 자기회귀모형과 이동평균모형
- 컴퓨터시스템응용기술사 제128회 1교시: 시계열 데이터 분석과 정상성 조건
- George E. P. Box, Gwilym M. Jenkins et al., *Time Series Analysis: Forecasting and Control (5th Edition)*
- Rob J. Hyndman & George Athanasopoulos, *Forecasting: Principles and Practice (3rd Edition)*

## 연결 토픽

- [시계열 실시간 이상치 탐지](./061_time_series_realtime_anomaly_detection/) · [기술통계 vs 추론통계](./036_descriptive_statistics/) · [가설검정](./041_hypothesis_testing/)
