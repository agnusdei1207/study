---
sidebar:
  order: 60
  label: "060. 시계열 AR·MA 모형"
  badge:
    text: "B"
    variant: note
title: "시계열 AR·MA 모형 (자기회귀 및 이동평균 모형) 및 ARIMA"
author: "OpenAI Codex"
date: "2026-09-20T18:00:00+09:00"
tags:
  - "notes-data"
weight: 60
extra:
  model: "GPT-5"
  keyword_grade: "B"
  question_no: "060"

---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>시계열 AR·MA 모형</strong></div>

## 큰 그림과 30초 인출

```text
[AR 모형과 MA 모형의 수식 및 ACF / PACF 식별 패턴]

 1. 자기회귀 모형 (AR(p)): 현재 값이 과거 p개 "자기 관측값"의 선형 결합
    Y_t = c + φ_1*Y_{t-1} + φ_2*Y_{t-2} + ... + φ_p*Y_{t-p} + ε_t
    ┌──────────┬────────────────────────────────────────────────────────┐
    │ ACF 패턴 │ 시차가 증가함에 따라 점진적으로 지수적 감쇄 (Tails off)│
    │ PACF 패턴│ p차수 이후 0으로 급격히 단절 (Cuts off after lag p)   │
    └──────────┴────────────────────────────────────────────────────────┘

 2. 이동평균 모형 (MA(q)): 현재 값이 과거 q개 "백색잡음(오차항)"의 선형 결합
    Y_t = μ + ε_t + θ_1*ε_{t-1} + θ_2*ε_{t-2} + ... + θ_q*ε_{t-q}
    ┌──────────┬────────────────────────────────────────────────────────┐
    │ ACF 패턴 │ q차수 이후 0으로 급격히 단절 (Cuts off after lag q)   │
    │ PACF 패턴│ 시차가 증가함에 따라 점진적으로 지수적 감쇄 (Tails off)│
    └──────────┴────────────────────────────────────────────────────────┘
  * 핵심 전제: 시계열의 평균, 분산, 공분산이 시간에 따라 일정한 '정상성(Stationarity)' 충족 필수
```

- 본질: **시간의 흐름에 따라 순차 관측된 정상 시계열(Stationary Time Series) 데이터의 확률적 자기상관 구조를 수학적으로 모형화하기 위해, 과거 자신의 관측치에 의존하는 자기회귀(AR) 모형과 과거 예측 오차(충격)에 의존하는 이동평균(MA) 모형을 결합한 전통 통계적 예측 체계**
- 암기: `정-식-추-진` (정상성 검정, 모형 식별, 모수 추정, 잔차 진단 - Box-Jenkins 4단계) / `에이-피(AR-PACF절단) vs 엠-에이(MA-ACF절단)`
- 판단축:
  - **AR($p$) 모형**: 과거 시점의 충격이 계수($\phi$)를 타고 미래로 영구히 감쇄하며 전파되는 '관성(Momentum)' 모델링 $\rightarrow$ PACF가 $p$에서 절단
  - **MA($q$) 모형**: 과거 시점의 충격이 정확히 $q$ 시점까지만 영향을 미치고 이후 완전히 소멸하는 '유한 충격(Transitory Shock)' 모델링 $\rightarrow$ ACF가 $q$에서 절단
- 주의: 현실의 대다수 데이터(주가, 트래픽, 전력 사용량 등)는 평균이나 분산이 시간에 따라 변하는 비정상(Non-stationary) 시계열이므로, 직접 적용 시 '허위 회귀(Spurious Regression)'가 발생함. 반드시 차분(Differencing)을 통해 정상화한 후 ARIMA($p, d, q$)로 확장해야 함

## 예상문제

> 시계열 분석에서 사용되는 자기회귀모형(Autoregressive Model)과 이동평균모형(Moving Average Model)의 개념, 수식 및 동작 특성을 설명하고, 정상성(Stationarity)의 조건과 자기상관함수(ACF) 및 편자기상관함수(PACF)를 활용한 모형 식별 방법을 비교하시오. (10점 / 25점)

## Ⅰ. 시간 경과에 따른 자기상관성을 규명하는 시계열 모형 개요

#### 한줄 요약: 과거 관측치와 예측 오차의 확률적 결합을 통해 미래 시계열 값을 예측하는 선형 통계 모형과 정상성 조건

- **시계열 분석의 본질**:
  - 독립변수와 종속변수 간의 관계를 다루는 일반 회귀분석과 달리, **동일한 변수의 시간 경과에 따른 자기 자신과의 상관성(Autocorrelation)**을 분석함
- **정상성(Stationarity, 약정상성) 3대 조건**:
  1. **일정한 평균**: 모든 시점 $t$에 대해 평균이 일정함 ($E[Y_t] = \mu$)
  2. **일정한 분산**: 모든 시점 $t$에 대해 분산이 일정함 ($Var(Y_t) = \sigma^2 < \infty$)
  3. **시차 의존 공분산**: 두 시점 $t, t-k$ 간의 공분산은 절대 시점 $t$가 아닌 오직 시차(Lag, $k$)에만 의존함 ($Cov(Y_t, Y_{t-k}) = \gamma_k$)

## Ⅱ. 자기회귀모형 (AR, Autoregressive Model)

#### 한줄 요약: 현재 시점의 데이터를 과거 $p$개 시점의 자기 자신 관측치들의 가중합과 백색잡음의 합으로 표현하는 모형

- **수학적 정의 (AR($p$))**:
  $$Y_t = c + \sum_{i=1}^{p} \phi_i Y_{t-i} + \epsilon_t = c + \phi_1 Y_{t-1} + \phi_2 Y_{t-2} + \dots + \phi_p Y_{t-p} + \epsilon_t$$
  - $Y_t$: 시점 $t$에서의 관측값
  - $\phi_i$: 시차 $i$에 대한 자기회귀 계수 (영향력의 크기)
  - $\epsilon_t$: 백색잡음(White Noise, $\epsilon_t \sim i.i.d. N(0, \sigma^2)$)
- **핵심 동작 특성**:
  - **영구적 충격 전파**: 과거의 충격 $\epsilon_{t-k}$가 계수 $\phi$의 거듭제곱 형태로 미래 시점까지 점진적으로 감쇄하며 장기적으로 잔류함
  - **정상성 조건 (AR(1))**: $|\phi_1| < 1$ 이어야 시계열이 발산하지 않고 정상성을 만족함 ($\phi_1 = 1$이면 Random Walk 단위근 발생)

## Ⅲ. 이동평균모형 (MA, Moving Average Model)

#### 한줄 요약: 현재 시점의 데이터를 현재 및 과거 $q$개 시점의 백색잡음(예측 오차 충격)들의 선형 결합으로 표현하는 모형

- **수학적 정의 (MA($q$))**:
  $$Y_t = \mu + \epsilon_t + \sum_{j=1}^{q} \theta_j \epsilon_{t-j} = \mu + \epsilon_t + \theta_1 \epsilon_{t-1} + \theta_2 \epsilon_{t-2} + \dots + \theta_q \epsilon_{t-q}$$
  - $\mu$: 시계열의 기저 기대값(평균)
  - $\theta_j$: 시차 $j$에서의 오차항에 대한 이동평균 계수
  - $\epsilon_t$: 시점 $t$에서 발생한 예측 불가능한 외부 충격(Innovation / Shock)
- **핵심 동작 특성**:
  - **유한한 충격 지속**: $t$ 시점에 발생한 충격 $\epsilon_t$는 정확히 $t+q$ 시점까지만 영향을 미치며, $t+q+1$ 시점부터는 영향력이 완전히 0으로 소멸함
  - **자체적 정상성**: 계수 $\theta$의 값과 무관하게 유한 차수 MA 모형은 항상 정상성 조건을 충족함 (단, 과거 관측치로 오차를 복원하기 위한 가역성(Invertibility) 조건 필요: $|\theta_1| < 1$)

## Ⅳ. AR 모형 vs MA 모형 심층 비교 및 ACF/PACF 식별 메커니즘

#### 한줄 요약: 자기상관함수(ACF)와 편자기상관함수(PACF)의 감쇄(Tails-off) 및 절단(Cuts-off) 양상을 통한 모형과 차수 식별

```text
┌───────────────────────────────────┬───────────────────────────────────┐
│        자기회귀모형 (AR(p))        │        이동평균모형 (MA(q))       │
├───────────────────────────────────┼───────────────────────────────────┤
│ - 종속 대상: 과거 '자기 관측값'   │ - 종속 대상: 과거 '오차항(충격)'  │
│ - 충격 지속: 무한히 점진적 감쇄   │ - 충격 지속: q시점 이후 완전 소멸 │
│ - ACF : 지수적 점진 감쇄 (지연)   │ - ACF : q차수 이후 급격 절단(0)   │
│ - PACF: p차수 이후 급격 절단(0)   │ - PACF: 지수적 점진 감쇄 (지연)   │
└───────────────────────────────────┴───────────────────────────────────┘
```

| 비교 항목 | 자기회귀모형 (AR($p$)) | 이동평균모형 (MA($q$)) | 결합모형 (ARMA($p, q$)) |
|:---|:---|:---|:---|
| **기본 수식** | $Y_t = c + \sum \phi_i Y_{t-i} + \epsilon_t$ | $Y_t = \mu + \epsilon_t + \sum \theta_j \epsilon_{t-j}$ | $Y_t = c + \sum \phi_i Y_{t-i} + \epsilon_t + \sum \theta_j \epsilon_{t-j}$ |
| **핵심 철학** | 이전 상태의 관성(Momentum) 모델링 | 예기치 못한 단기적 쇼크(Shock) 모델링 | 관성과 외부 충격을 동시 고려 |
| **ACF 패턴** | **점진적 감쇄 (Tails off)** | **$q$차수 이후 절단 (Cuts off)** | 점진적 감쇄 (Tails off) |
| **PACF 패턴** | **$p$차수 이후 절단 (Cuts off)** | **점진적 감쇄 (Tails off)** | 점진적 감쇄 (Tails off) |
| **충격 지속성** | 무한 감쇄 (Memory fades gradually) | 유한 지속 ($q$ 기간 후 효과 제로) | 무한 감쇄 |
| **모형 차수 결정** | PACF가 0으로 떨어지는 직전 차수 $p$ | ACF가 0으로 떨어지는 직전 차수 $q$ | AIC / BIC 정보 기준 최소화 지점 탐색 |

## Ⅴ. 비정상 시계열 확장을 위한 ARIMA 및 SARIMA 모델링

#### 한줄 요약: 차분(Differencing)을 통해 비정상 시계열을 정상화한 ARIMA($p, d, q$)와 계절성을 반영한 SARIMA

```text
[비정상 시계열의 ARIMA 모델링 파이프라인]

 원시 비정상 시계열 (Y_t) ──▶ 차분(Differencing, d회) ──▶ 정상 시계열 (Δ^d Y_t) ──▶ ARMA(p, q) 적용
 (상승 추세 / 분산 불안정)      1차 차분: ΔY_t = Y_t - Y_{t-1}                           (예측 모델 구축)
```

- **ARIMA($p, d, q$) (Autoregressive Integrated Moving Average)**:
  - $p$: 자기회귀(AR) 차수
  - $d$: 정상 시계열로 만들기 위한 차분(Differencing) 횟수 (보통 1회 또는 2회)
  - $q$: 이동평균(MA) 차수
- **SARIMA (Seasonal ARIMA)**:
  - 주간, 월간, 연간 주기성을 갖는 시계열을 위해 계절 차분과 계절 AR/MA 항을 결합: $\text{ARIMA}(p, d, q) \times (P, D, Q)_s$ ($s$: 계절 주기 길이)

## Ⅵ. Box-Jenkins 방법론과 실무 시계열 분석 프로세스

#### 한줄 요약: 식별(Identification) $\rightarrow$ 추정(Estimation) $\rightarrow$ 진단(Diagnostic Checking) $\rightarrow$ 예측(Forecasting)의 4단계 표준 절차

```text
 [1단계: 모형 식별 (Identification)]
  - ADF(Augmented Dickey-Fuller) 단위근 검정으로 정상성 확인
  - 비정상 시 차분(d) 수행 후 ACF / PACF 플롯을 그려 p, q 후보 차수 도출
           │
           ▼
 [2단계: 모수 추정 (Estimation)]
  - 최대우도추정법(MLE) 또는 최소제곱법(OLS)으로 계수(φ, θ) 추정
  - AIC(Akaike Information Criterion), BIC 최소화 모델 선별
           │
           ▼
 [3단계: 모형 진단 (Diagnostic Checking)]
  - 모델의 잔차(Residual)가 백색잡음(White Noise)을 만족하는지 검증
  - Ljung-Box Q-검정을 수행하여 잔차의 자기상관성 부재(p-value > 0.05) 확인
           │
           ▼
 [4단계: 미래 예측 (Forecasting)]
  - 검증 완료된 모델을 통해 미래 특정 시점의 기대값 및 95% 신뢰구간 산출
```

## Ⅶ. 데이터 아키텍트 관점의 시계열 모델링 및 이상 탐지 제언

#### 한줄 요약: 통계적 시계열 모델(ARIMA)의 설명력과 딥러닝(Transformer)의 비선형 표현력을 결합한 하이브리드 아키텍처 구축

- **전통 시계열 모형의 확고한 가치**:
  - LLM이나 딥러닝 시계열 모형(PatchTST, N-BEATS)이 유행하지만, 데이터센터 트래픽 예측이나 금융 위험 관리에서는 **수학적 해석 가능성과 경량 연산성**을 지닌 AR/MA/ARIMA가 여전히 1차 베이스라인으로 최적임
- **이상치 탐지(Anomaly Detection) 파이프라인 결합**:
  - ARIMA 모델로 미래 $t$ 시점의 예측 신뢰구간($\hat{Y}_t \pm 3\sigma$)을 생성하고, 실제 관측값이 이 구간을 이탈할 경우 즉시 보안/품질 이상 징후로 판정하는 실시간 모니터링 엔진 설계 권장

---

## 1교시 10점 답안 발췌

```text
[문제 7] 자기회귀모형(AR)과 이동평균모형(MA)

1. 자기회귀모형(AR)과 이동평균모형(MA)의 개념
 가. 자기회귀모형(AR): 현재 데이터가 과거 자기 자신의 관측값 선형결합으로 결정되는 모형
 나. 이동평균모형(MA): 현재 데이터가 과거 외부 충격(백색잡음 오차항)들의 선형결합으로 결정되는 모형
 다. 핵심 전제: 시계열의 평균과 분산이 시간에 무관하게 일정한 정상성(Stationarity) 충족

2. 모형별 수식 및 식별 패턴 비교
 ┌──────────────┬────────────────────────────────┬────────────────────────────────┐
 │  구분        │   자기회귀모형 (AR(p))         │   이동평균모형 (MA(q))         │
 ├──────────────┼────────────────────────────────┼────────────────────────────────┤
 │ 기본 수식    │ Y_t = c + Σ φ_i*Y_{t-i} + ε_t  │ Y_t = μ + ε_t + Σ θ_j*ε_{t-j}  │
 │ 충격의 지속성│ 무한히 점진적 감쇄 (관성 반영) │ q 시점 경과 후 완전히 소멸     │
 │ ACF 패턴     │ 지수적 점진 감쇄 (Tails off)   │ q차수 이후 급격 절단 (Cuts off)│
 │ PACF 패턴    │ p차수 이후 급격 절단 (Cuts off)│ 지수적 점진 감쇄 (Tails off)   │
 └──────────────┴────────────────────────────────┴────────────────────────────────┘

3. 실무 모형 식별 및 비정상 시계열 대응
 가. 식별: ACF/PACF 플롯 절단 지점 및 AIC/BIC 정보 기준으로 최적 차수(p, q) 선정
 나. 확장: 비정상 시계열은 차분(d)을 적용한 ARIMA(p, d, q) 모형으로 변환 후 분석
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제138회 1교시 7번 (자기회귀모형과 이동평균모형)
  - 컴퓨터시스템응용기술사 제128회 1교시 (시계열 데이터 분석과 정상성 조건)
  - 정보관리기술사 제118회 2교시 (시계열 분석의 Box-Jenkins 방법론 및 ARIMA)
- **표준 및 검증 출처**:
  - George E. P. Box, Gwilym M. Jenkins et al., *Time Series Analysis: Forecasting and Control (5th Edition)*
  - Rob J. Hyndman & George Athanasopoulos, *Forecasting: Principles and Practice (3rd Edition)*
  - 한국통계학회 통계학 용어집 (시계열 모형, 정상성, 자기상관함수)

---

## 학습 체크

- [ ] 시계열 정상성(Stationarity)을 만족하기 위한 3대 수학적 조건(평균, 분산, 공분산)을 기술할 수 있는가?
- [ ] AR($p$) 모형과 MA($q$) 모형의 수식을 오차항($\epsilon_t$)과 관측값($Y_t$) 관점에서 제시할 수 있는가?
- [ ] ACF와 PACF 플롯을 보고 AR 모형과 MA 모형, 그리고 각각의 차수($p, q$)를 식별하는 규칙을 설명할 수 있는가?
- [ ] ARIMA($p, d, q$)에서 차분($d$)이 필요한 이유와 단위근 검정(ADF Test)의 역할을 서술할 수 있는가?
- [ ] **서술 연습 1**: AR(1)과 MA(1) 모형의 수식을 적고, 외부 충격이 발생했을 때 시차가 지남에 따른 반응의 차이를 10점형 답안으로 비교하시오.
- [ ] **서술 연습 2**: Box-Jenkins 시계열 분석 4단계 절차(식별-추정-진단-예측)를 플로우차트와 함께 25점형으로 서술하시오.

---

## 연결 토픽

- [061. 시계열 실시간 이상치 탐지 (Time Series Realtime Anomaly Detection)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/061_time_series_realtime_anomaly_detection.md)
- [036. 기술통계 vs 추론통계 (Descriptive vs Inferential Statistics)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/036_descriptive_statistics.md)
- [041. 가설검정 (Hypothesis Testing)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/041_hypothesis_testing.md)
