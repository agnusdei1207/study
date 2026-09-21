---
author: "Antigravity"
category: "03-data"
date: "2026-09-20T16:45:00+09:00"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
  question_no: "036"
sidebar:
  badge:
    text: "A"
    variant: "note"
  label: "036. 기술통계 vs 추론통계"
  order: 36
tags:
  - "notes-data"
title: "기술통계 vs 추론통계 (Descriptive vs Inferential Statistics)"
weight: 36
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 분석·통계</span><span>통계학 기초·데이터 분석 방법론</span><strong>기술통계 vs 추론통계</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 160" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="160" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Top: Raw Data Input -->
  <rect x="160" y="10" width="200" height="26" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="260" y="27" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #0f172a)">원천 관측 데이터 (4대 척도: 명·서·등·비)</text>
  <line x1="260" y1="36" x2="260" y2="48" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-stat)"/>

  <!-- Left: Descriptive Statistics -->
  <rect x="15" y="48" width="240" height="100" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <rect x="15" y="48" width="240" height="22" fill="var(--color-primary-light, #e0f2fe)" rx="4"/>
  <text x="135" y="63" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">[기술통계] 현재 표본 자체 요약·기술</text>
  <text x="25" y="85" font-size="8.5" fill="var(--color-text, #0f172a)">• 중심위치: 평균, 중앙값(이상치 강건), 최빈값</text>
  <text x="25" y="102" font-size="8.5" fill="var(--color-text, #0f172a)">• 산포도: 분산, 표준편차, 사분위범위(IQR)</text>
  <text x="25" y="119" font-size="8.5" fill="var(--color-text, #0f172a)">• 형태: 왜도(비대칭도), 첨도(꼬리 두께)</text>
  <text x="25" y="137" font-size="8" fill="var(--color-text-muted, #64748b)">🎯 목적: EDA 탐색 및 데이터 왜곡 탐지</text>

  <!-- Right: Inferential Statistics -->
  <rect x="265" y="48" width="240" height="100" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <rect x="265" y="48" width="240" height="22" fill="var(--color-success-light, #dcfce7)" rx="4"/>
  <text x="385" y="63" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-success-dark, #15803d)">[추론통계] 표본으로 모집단 모수 일반화</text>
  <text x="275" y="85" font-size="8.5" fill="var(--color-text, #0f172a)">• 모수 추정: 점추정(MLE 불편성), 구간추정(CI)</text>
  <text x="275" y="102" font-size="8.5" fill="var(--color-text, #0f172a)">• 가설 검정: 귀무가설($H_0$) vs 대립가설($H_1$)</text>
  <text x="275" y="119" font-size="8.5" fill="var(--color-text, #0f172a)">• 분석 기법: t-검정, ANOVA, 카이제곱, 회귀</text>
  <text x="275" y="137" font-size="8" fill="var(--color-success-dark, #15803d)">🎯 목적: 확률적 유의성(p-value) 입증</text>

  <defs>
    <marker id="arrow-stat" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **수집된 표본 데이터의 중심, 산포, 형태를 수치와 시각화로 요약·정리하는 '기술통계'와, 확률 이론을 기반으로 표본 통계량으로부터 미지의 모집단 모수를 추정하고 가설을 검정하는 '추론통계'의 상호보완적 데이터 분석 체계**
- 암기: `명-서-등-비` (4대 척도: 명목 · 서열 · 등간 · 비율) / `중-산-형` (기술통계: 중심위치 · 산포도 · 형태) / `추-검` (추론통계: 추정 · 검정)
- 4대 척도와 통계 연산:
  - 명목(Nominal): 최빈값, 빈도 분석, 카이제곱 검정
  - 서열(Ordinal): 중앙값, 사분위수, 순위 상관계수(Spearman)
  - 등간(Interval): 산술평균, 표준편차 (절대영점 부재, 덧셈/뺄셈 가능)
  - 비율(Ratio): 기하/조화평균, 변동계수, 사칙연산 전체 가능
- 주의: 척도에 맞지 않는 연산(서열 척도에 산술평균 계산)이나 이상치 왜곡에 대한 주의 필수

## 예상문제

> 통계학의 4가지 측정 척도(명목, 서열, 등간, 비율)를 정의하고, 기술통계(Descriptive Statistics)와 추론통계(Inferential Statistics)의 개념, 주요 기법 및 차이점을 비교하여 머신러닝 데이터 전처리 관점에서의 실무 고려사항을 논하시오. (25점)

## Ⅰ. 데이터 분석의 양대 기둥, 기술통계와 추론통계 개요

- 정의:
  - **기술통계(Descriptive Statistics)**: 수집된 데이터의 특성을 도표, 그래프, 대표 수치 지표(평균, 분산 등)를 통해 객관적으로 요약·기술(Describe)하는 통계 기법
  - **추론통계(Inferential Statistics)**: 표본(Sample)에서 관측된 결과를 확률 이론과 표본 분포 이론을 활용하여 미지의 모집단(Population) 전체의 특성(모수)을 일반화하여 추론(Infer)하는 통계 기법
- 목적: 방대한 원시 데이터의 내재적 패턴을 신속히 파악(기술)하고, 불확실한 미래 의사결정 및 가설의 진위를 과학적 확률로 검증(추론)
- 필요성: 기술통계 없이 추론통계로 직행하면 이상치나 분포 왜곡으로 잘못된 모델이 수립되며, 추론통계 없는 기술통계는 수집된 표본을 벗어난 일반화된 통찰을 도출할 수 없음

#### 한줄 요약

- 기술통계는 '눈앞의 데이터를 요약하는 나침반'이고, 추론통계는 '표본 너머의 전체를 꿰뚫어 보는 망원경'임

## Ⅱ. 통계학의 기반: 4가지 측정 척도(Scales of Measurement)

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 62" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="62" fill="var(--color-surface, #f8fafc)" rx="6" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- 4 Step Scale Flow -->
  <rect x="10" y="12" width="112" height="38" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="66" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">① 명목 척도</text>
  <text x="66" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">단순 구분·최빈값</text>

  <line x1="122" y1="31" x2="136" y2="31" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-scale)"/>

  <rect x="138" y="12" width="112" height="38" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="194" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">② 서열 척도</text>
  <text x="194" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">순서·중앙값</text>

  <line x1="250" y1="31" x2="264" y2="31" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-scale)"/>

  <rect x="266" y="12" width="112" height="38" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="322" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">③ 등간 척도</text>
  <text x="322" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">간격일정·산술평균</text>

  <line x1="378" y1="31" x2="392" y2="31" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-scale)"/>

  <rect x="394" y="12" width="116" height="38" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1" rx="3"/>
  <text x="452" y="27" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">④ 비율 척도</text>
  <text x="452" y="41" text-anchor="middle" font-size="7.5" fill="var(--color-primary-dark, #0369a1)">절대0·사칙연산 전체</text>

  <defs>
    <marker id="arrow-scale" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <polygon points="0 0, 5 2.5, 0 5" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

| 척도 구분 | 정의 및 특성 | 허용 수학 연산 | 대표 중심치 및 기법 | 실무 적용 예시 |
|---|---|---|---|---|
| **명목 척도<br>(Nominal)** | 관측 대상의 특성을 분류·구분하기 위해 부여한 이름이나 기호 (순서 없음) | $=, \neq$ (빈도 수 계산) | 최빈값(Mode), 빈도분석, 카이제곱 검정 | 성별, 혈액형, HTTP 상태코드 |
| **서열 척도<br>(Ordinal)** | 분류뿐만 아니라 대상 간의 상대적 순서나 서열(Rank)이 존재하는 척도 | $=, \neq, <, >$ (대소 비교) | 중앙값(Median), 사분위수, 순위상관 | 직급, 학점(A~F), 만족도(리커트 5점) |
| **등간 척도<br>(Interval)** | 순서뿐만 아니라 속성 간의 간격이 동일한 척도 (임의의 0점, 절대영점 없음) | $+ , -$ (덧셈, 뺄셈 가능) | 산술평균(Mean), 표준편차, 피어슨 상관 | 섭씨 온도(℃), IQ 지수, 지표 연도 |
| **비율 척도<br>(Ratio)** | 등간격 속성에 절대적 기준이 되는 '절대 영점(True Zero)'이 존재하는 척도 | $+ , -, \times, \div$ (사칙연산) | 기하평균, 조화평균, 변동계수, 회귀 | 매출액, 연령, CPU 사용률, 응답 지연(ms) |

#### 한줄 요약

- 척도는 명목(분류) $\to$ 서열(순서) $\to$ 등간(간격) $\to$ 비율(비율)로 갈수록 정보량이 많아지고 허용되는 수학 연산이 확장됨

## Ⅲ. 기술통계의 3대 축: 중심위치, 산포도, 분포형태

| 축 | 세부 지표 | 수학적 수식 및 정의 | 해석 및 실무 활용 |
|---|---|---|---|
| **중심경향치** | **산술평균 (Mean)** | $\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i$ | 전체 데이터의 물리적 균형점, 극단 이상치에 매우 취약 |
| | **중앙값 (Median)** | 순서대로 정렬했을 때 정중앙에 위치한 값 | 이상치에 강건(Robust), 소득·자산 등 편향 데이터 대표값 |
| | **최빈값 (Mode)** | 데이터 중 빈도수가 가장 높은 값 | 범주형 데이터(명목 척도)의 유일한 중심치 |
| **산포도** | **분산 및 표준편차** | $s^2 = \frac{\sum (X_i - \bar{X})^2}{n-1}, \quad s = \sqrt{s^2}$ | 평균으로부터 떨어진 평균 거리, 데이터 변동성 측정 |
| | **사분위범위 (IQR)** | $IQR = Q_3 (75\%) - Q_1 (25\%)$ | 박스플롯(Boxplot)의 기본, 이상치 판정($Q_1 - 1.5IQR$ 미만) |
| | **변동계수 (CV)** | $CV = (s / \bar{X}) \times 100\%$ | 단위가 다른 두 집단의 상대적 산포도 비교 |
| **분포형태** | **왜도 (Skewness)** | $\gamma_1 = E\left[\left(\frac{X-\mu}{\sigma}\right)^3\right]$ | - $\gamma_1 > 0$: 오른쪽 꼬리 (평균 > 중앙값)<br>- $\gamma_1 < 0$: 왼쪽 꼬리 (평균 < 중앙값) |
| | **첨도 (Kurtosis)** | $\gamma_2 = E\left[\left(\frac{X-\mu}{\sigma}\right)^4\right] - 3$ | - $\gamma_2 > 0$: 정규분포보다 뾰족함 (Fat-tail 리스크)<br>- $\gamma_2 < 0$: 완만하고 평평한 분포 |

#### 한줄 요약

- 기술통계는 평균 하나만 보는 함정을 피하기 위해 '중심값(평균/중앙값)', '흩어짐(표준편차/IQR)', '비대칭(왜도/첨도)'을 삼위일체로 확인해야 함

## Ⅳ. 추론통계의 2대 축: 모수 추정과 가설 검정

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 120" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="120" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Top Center: Population to Sample -->
  <rect x="170" y="10" width="180" height="26" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <text x="260" y="27" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">모집단 모수(μ, σ²) ──▶ 표본 통계량(X̄, s²)</text>

  <!-- Left: Estimation -->
  <line x1="210" y1="36" x2="140" y2="52" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" marker-end="url(#arrow-infer)"/>
  <rect x="25" y="52" width="225" height="58" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="137" y="68" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">1. 모수 추정 (Estimation)</text>
  <text x="137" y="84" text-anchor="middle" font-size="8" fill="var(--color-primary-dark, #0369a1)">• 점추정: 불편추정량 (X̄ ──▶ μ)</text>
  <text x="137" y="98" text-anchor="middle" font-size="8" fill="var(--color-primary-dark, #0369a1)">• 구간추정: 95% 신뢰구간 (CI = X̄ ± 1.96·SE)</text>

  <!-- Right: Hypothesis Testing -->
  <line x1="310" y1="36" x2="380" y2="52" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" marker-end="url(#arrow-infer)"/>
  <rect x="270" y="52" width="225" height="58" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="382" y="68" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">2. 가설 검정 (Hypothesis Testing)</text>
  <text x="382" y="84" text-anchor="middle" font-size="8" fill="var(--color-success-dark, #15803d)">• 귀무가설(H₀: 무효) vs 대립가설(H₁: 유의)</text>
  <text x="382" y="98" text-anchor="middle" font-size="8" fill="var(--color-success-dark, #15803d)">• p-value &lt; 0.05 시 귀무가설 기각 (채택)</text>

  <defs>
    <marker id="arrow-infer" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <polygon points="0 0, 5 2.5, 0 5" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

| 영역 | 핵심 기법 | 동작 메커니즘 | 실무 의사결정 |
|---|---|---|---|
| **모수 추정<br>(Estimation)** | **점추정 (Point)** | 표본 통계량으로 모수를 단일 값으로 제시 (예: 표본평균 $\bar{X}$로 모평균 $\mu$ 추정) | 불편성, 효율성, 일치성을 만족하는 추정량(MLE 등) 선정 |
| | **구간추정 (Interval)** | 모수가 포함될 범위를 신뢰수준($1-\alpha$)과 함께 제시: $\bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}$ | 표본오차를 고려한 현실적 구간 예측 (예: 95% 신뢰구간) |
| **가설 검정<br>(Testing)** | **t-검정 (t-Test)** | 두 집단의 평균 차이가 통계적으로 유의미한지 검정 | A/B 테스트 신규 UI 도입 효과 검증 |
| | **분산분석 (ANOVA)** | 3개 이상 집단 간의 평균 차이 검정 ($F$-분포 활용) | 마케팅 채널 3종 간의 매출액 차이 비교 |
| | **카이제곱 검정** | 두 범주형 변수 간의 독립성/적합도 검정 ($\chi^2$-분포) | 성별에 따른 구매 상품 카테고리 선호도 차이 분석 |
| | **회귀분석** | 독립변수와 종속변수 간의 함수적 인과관계 도출 | 마케팅 비용 증가에 따른 매출액 변화량 예측 |

#### 한줄 요약

- 추론통계는 표본의 우연한 변동을 제거하고, $p$-value와 신뢰구간을 통해 모집단의 참된 진실을 통계학적으로 입증함

## Ⅴ. 기술통계 vs 추론통계 심층 비교

| 비교 항목 | 기술통계 (Descriptive Statistics) | 추론통계 (Inferential Statistics) |
|---|---|---|
| **연구 대상** | 수집된 관측 데이터 자체 (표본 내 국한) | 관측되지 않은 모집단 전체 (일반화 지향) |
| **핵심 목적** | 데이터의 구조, 패턴, 이상치 요약 및 시각화 | 표본에 기반한 모집단 모수 추정 및 가설 검증 |
| **수학적 도구** | 사칙연산, 백분위수, 분산, 상관계수, 차트 | 확률 이론, 표본 분포($t, z, F, \chi^2$), 중심극한정리 |
| **오차 개념** | 데이터 자체의 측정 오차만 고려 | 표본 추출에 필연적인 **표본오차(Sampling Error)** 통제 |
| **표현 산출물** | 히스토그램, 박스플롯, 요약 통계표 (평균, SD) | 신뢰구간(CI), 유의확률($p$-value), 기각역, 회귀식 |
| **분석 프로세스**| 데이터 분석의 1단계 (탐색적 데이터 분석, EDA) | 데이터 분석의 2단계 (확증적 데이터 분석, CDA) |

#### 한줄 요약

- 기술통계는 표본을 설명하고, 추론통계는 모집단을 일반화하며, 둘은 선후 관계의 상호보완적 파이프라인을 이룸

## Ⅵ. 머신러닝 데이터 전처리 및 분석 실무 장애 요인 및 대책

| 문제 상황 | 근본 원인 | 실무 대응 방안 | 기대 효과 |
|---|---|---|---|
| **'평균의 함정'으로 인한 비즈니스 오판** | 소득·자산 등 극단적 고액 이상치가 포함되어 평균을 심각하게 상향 왜곡 | 중심치로 산술평균 대신 **중앙값(Median)**을 채택하고, **IQR 기반 이상치 탐지** 병행 | 실제 대다수 고객의 실태 정확 반영 |
| **선형 회귀 모델의 잔차 정규성 위반** | 왜도($\gamma_1 > 2$)가 심한 긴 꼬리 데이터(매출액, 트래픽)를 원형 그대로 입력 | **로그 변환($\log(x+1)$)** 또는 **Box-Cox 변환**을 적용하여 정규분포 대칭화 | 회귀 모델 선형성 확보 및 결정계수($R^2$) 향상 |
| **서열 척도 데이터의 무분별한 사칙연산** | 만족도 설문(1~5점)을 연속형 비율 척도로 착각하여 다중회귀 분석 적용 | 순서형 특성을 보존하는 **순서형 로지스틱 회귀(Ordinal Logistic)** 모델 채택 | 척도 오류 없는 수학적 정합성 보장 |
| **A/B 테스트에서 거짓 양성(False Positive) 채택** | 기술통계상 신규 UI 매출이 높게 나왔으나 추론통계적 유의성 검정 누락 | **독립표본 t-검정**을 수행하여 $p$-value $< 0.05$ 검증 후 프로덕션 배포 | 우연한 변동에 따른 섣부른 릴리즈 방지 |

#### 한줄 요약

- 척도에 맞는 변환(로그 변환), 이상치에 강건한 지표(중앙값), 통계적 유의성 검정($p$-value)이 데이터 왜곡을 막는 3대 원칙임

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 통계학에서 프랜시스 앤스컴이 제시한 '앤스컴 콰르텟(Anscombe's Quartet)'은 데이터 엔지니어링과 데이터 사이언스에 가장 묵직한 교훈을 준다. 4개의 데이터셋이 평균(9.0), 분산(11.0), 상관계수(0.816), 회귀선($y = 3 + 0.5x$)이 소수점 둘째 자리까지 완벽히 일치하지만, 실제로 산점도를 그려보면 직선, 포물선, 이상치 1개에 의한 가짜 상관 등 완전히 다른 데이터다. 요약 수치(기술통계)만 보고 모델링을 진행하면 현실과 완전히 동떨어진 재앙적 알고리즘이 배포된다.
>
> **[나라면 이렇게 쓴다]**
> 실무 MLOps 파이프라인의 데이터 수집·수집 검증 단계에 자동화된 데이터 프로파일링(Great Expectations, YData Profiling)을 기본 탑재하겠다. 4대 측정 척도를 자동 분류하고 왜도·첨도 및 박스플롯 IQR 기반 이상치를 탐지하는 **EDA 자동화 게이트**를 두고, A/B 테스트나 신규 피처 배포 시에는 기술통계적 개선치뿐만 아니라 독립표본 t-검정과 부트스트랩을 통한 $p$-value($p < 0.05$) 검증을 통과해야만 머지되는 **'확증 통계 배포 거버넌스'**를 구축하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 단순 평균값 중심의 데이터 해석으로 인한 이상치 왜곡 및 추론통계적 유의성 검증 부재에 따른 A/B 테스트 오류.
- **대응 (개선 방안)**: 중앙값·IQR 기반 로버스트 지표 병기, 왜도 피처 로그 변환 및 독립표본 t-검정 기반 배포 게이트웨이 확립.
- **검증 (검증 기준)**: 데이터 왜도 $|\gamma_1| < 1.0$ 정규화 달성 및 가설 검정 유의확률 $p < 0.05$ 통계적 유의성 검증.
- **효과 (실행 효과)**: 이상치 왜곡에 따른 잘못된 비즈니스 릴리즈 100% 차단 및 머신러닝 예측 정확도($R^2$) 25% 개선.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">현행 한계</div>
    <div class="itpe-flow-desc">평균의 함정 왜곡 및 가설검정 없는 A/B 테스트 거짓양성</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">개선 방안</div>
    <div class="itpe-flow-desc">로버스트 지표(중앙값·IQR) 표준화 및 t-검정 배포 게이트웨이</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">검증 기준</div>
    <div class="itpe-flow-desc">피처 왜도 1.0 미만 정규화 및 p-value &lt; 0.05 유의성 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">실행 효과</div>
    <div class="itpe-flow-desc">우연적 변동 오배포 0건 방어 및 회귀 모델 예측성 25% 향상</div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 기술통계와 추론통계의 정의

- **기술통계**: 수집된 표본 데이터의 중심, 산포, 형태를 수치와 차트로 요약·기술하는 기법
- **추론통계**: 확률 이론과 표본 분포를 기반으로 표본 통계량으로부터 모집단의 모수를 추정하고 가설을 검정하는 기법

### 2. 4대 측정 척도 체계

- **명목 (Nominal)**: 단순 분류 $\to$ 빈도, 최빈값 (성별, 혈액형)
- **서열 (Ordinal)**: 순서 존재 $\to$ 중앙값, 사분위수 (만족도, 직급)
- **등간 (Interval)**: 동일 간격 (절대0 부재) $\to$ 덧셈/뺄셈, 산술평균, 표준편차 (온도, IQ)
- **비율 (Ratio)**: 절대 영점 존재 $\to$ 사칙연산 전체, 기하평균, 변동계수 (매출액, 연령)

| 구분 | 기술통계 (Descriptive) | 추론통계 (Inferential) |
|---|---|---|
| 분석 대상 | 표본 데이터 자체 (Sample) | 모집단 전체 (Population) |
| 핵심 기법 | 평균, 중앙값, 분산, 왜도, 박스플롯 | 점/구간 추정, t-검정, ANOVA, 회귀분석 |
| 주안점 | 데이터 요약 및 이상치 탐색 | 표본오차 극복 및 일반화 검증 ($p$-value) |

### 3. 차별화 제언

- 단순 평균의 함정을 극복하기 위해 **중앙값과 IQR**을 병기하고, 피처 왜도 해소를 위한 **로그 변환** 및 **통계적 유의성 검정($p < 0.05$)**을 전처리 표준으로 정립함

## 출제 이력과 검증 출처

- 제124회 1교시 2번: 통계학의 4가지 척도를 구분하고 다중회귀분석과 로지스틱회귀분석 비교
- 제123회 공식 문제지: 기술통계와 추론통계
- [OpenIntro Statistics (David Diez et al.)](https://www.openintro.org/book/os/)
- [Stevens, S. S. (1946). On the Theory of Scales of Measurement (Science)](https://www.science.org/doi/10.1126/science.103.2684.677)

## 학습 체크

- [ ] 4대 측정 척도(명목, 서열, 등간, 비율)의 수학적 연산 범위와 대표 통계량을 구분할 수 있는가
- [ ] 중심경향치(평균, 중앙값, 최빈값)와 산포도(분산, IQR)의 이상치 민감도를 비교할 수 있는가
- [ ] 왜도(Skewness)와 첨도(Kurtosis)의 기하학적 의미 및 머신러닝 데이터 전처리 활용 방안을 아는가
- [ ] 추론통계의 2대 축인 모수 추정(점/구간)과 가설 검정($p$-value)의 메커니즘을 설명할 수 있는가
- [ ] Ⅶ 결론에서 앤스컴 콰르텟 극복을 위한 EDA 결합 전략을 제시할 수 있는가

## 연결 토픽

- [표본추출](./032_sampling/) · [불편추정량](./011_unbiased_estimator/) · [가설검정](./041_hypothesis_testing/) · [z-검정](./012_z_test/) · [t-검정](./086_t_test/)
