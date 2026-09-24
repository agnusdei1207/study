---
sidebar:
  order: 143
  label: "143. 추론통계(Inferential Statistics)"
  badge:
    text: "A"
    variant: note
title: "추론통계 (Inferential Statistics)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 143
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "143"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 분석</span><span>통계학 기초</span><span>추론통계</span><strong>추론통계(추정과 검정)</strong></div>

## 큰 그림과 30초 인출

```text
[추론통계 (Inferential Statistics) 아키텍처 개요]

        모집단 (Population: 모수 μ, σ²)
          │                   ▲
          │ 표본추출          │ 통계적 추론 (Inference)
          │ (Sampling)        │ ① 추정: 점추정, 신뢰구간(95% CI)
          ▼                   │ ② 검정: 귀무가설(H0) 기각, p-value
        표본 (Sample: 통계량 X̄, s²)
```

- 본질: **전수조사가 불가능하거나 비효율적인 상황에서 무작위로 추출된 표본(Sample)의 통계량을 분석하여, 확률론적 오차범위 내에서 모집단(Population)의 모수(Parameter)를 과학적으로 추정하고 가설을 검증하는 귀납적 통계 체계**
- 암기: `모-표-추-검` (모집단, 표본, 추정, 검정) / `점-구-귀-대` (점추정, 구간추정, 귀무가설, 대립가설)
- 판단축:
  - **기술통계**: 수집된 데이터 자체의 속성을 요약·정리·시각화 (평균, 중위수, 분산, 왜도, 첨도).
  - **추론통계**: 관측된 표본의 통계량($\bar{X}, s$)을 바탕으로 관측 불가능한 모집단의 미지 모수($\mu, \sigma^2$)를 확률적으로 일반화 (점추정, 신뢰구간, p-value 가설검정).
- 주의: 중심극한정리(CLT)와 무작위 표본추출(Random Sampling)이 전제되지 않으면 표본 편향(Sampling Bias)으로 인해 산출된 p-value와 신뢰구간 전체가 왜곡됨
---

## 1교시 예상문제 (10점)

> 추론통계 (Inferential Statistics)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **정의** | 무작위 표본의 통계량을 분석하여 확률론적 오차범위 내에서 모집단의 미지 모수를 추정하고 가설을 검증하는 통계 체계 |
| **양대 핵심 축** | ① 추정(Estimation): 점추정(불편성, 효율성), 구간추정(95% 신뢰구간) / ② 가설검정: 귀무가설($H_0$) vs 대립가설($H_1$), p-value 판정 |
| **수학적 토대** | 중심극한정리(CLT, $n \ge 30$ 시 $\bar{X} \sim N(\mu, \sigma^2/n)$) 및 표준오차($SE = \sigma/\sqrt{n}$) |
| **기술 vs 추론** | 기술통계는 관측 데이터 요약·정리 / 추론통계는 표본 기반 보이지 않는 모집단 특성 예측 및 일반화 |
| **실무 제언** | 빅데이터 환경의 p-value 역설(표본 과다 시 왜곡) 극복을 위해 효과 크기(Cohen's d) 병행 산출 및 A/B 테스트 최적화 |
---

### 핵심 관계

| 비교 항목 | 기술통계 (Descriptive Statistics) | 추론통계 (Inferential Statistics) |
|:---|:---|:---|
| **기본 목적** | 수집된 관측 데이터의 특징 요약 및 시각화 | 표본을 바탕으로 미지의 모집단 특성 추론 및 일반화 |
| **분석 대상** | 관측 완료된 표본 또는 모집단 전체 데이터 | 관측된 일부 표본 (Sample Data) |
| **수학적 가정** | 확률 분포 가정 불필요 (단순 계산) | 확률 이론, 중심극한정리, 정규분포 가정 필수 |
| **핵심 지표** | 평균, 중위수, 분산, 왜도, 첨도, 사분위수 | 신뢰구간(CI), 검정통계량($z, t, F$), 유의확률($p$-value) |
| **결과의 성격** | 확정적 사실 (현재 상태의 서술) | 확률적 추론 (오차범위를 수반한 일반화) |
| **오류 위험** | 단순 계산 오류 외 이론적 위험 없음 | 표본 편향, 제1종 오류($\alpha$), 제2종 오류($\beta$) 발생 가능 |
| **대표 기법** | 히스토그램, 박스플롯, 피어슨 상관계수 | 독립 t-검정, 대응 t-검정, ANOVA, 회귀분석, 카이제곱 |

---

## 2~4교시 예상문제 (25점)

> 데이터 분석에서 기술통계(Descriptive Statistics)와 추론통계(Inferential Statistics)의 차이점을 비교하고, 추론통계의 핵심 체계인 추정(점추정, 구간추정)과 가설검정의 원리 및 빅데이터 환경에서 발생하는 p-value 역설과 대응 방안을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 모집단 특성 규명을 위한 추론통계(Inferential Statistics) 개요

#### 한줄 요약: 전체를 다 볼 수 없을 때, 수학적으로 추출한 일부분(표본)으로 전체(모집단)의 특성을 확률적으로 밝혀내는 학문

- **배경**:
  - 인구 총조사, 완제품 전수 파괴 검사 등은 시간·비용·물리적 한계로 인해 현실적으로 전수조사 불가능
  - 최소 비용으로 전체의 실태를 정량적으로 파악하기 위해 표본 데이터를 수집하고 이를 기반으로 모집단을 역추정하는 과학적 기법 필요
- **정의**:
  - 모집단에서 추출한 표본의 통계량(Statistic)을 분석하여 모집단의 고유한 특성치인 모수(Parameter)를 점·구간 추정하고, 연구 가설의 진위 여부를 통계적으로 판정하는 분석 방법론
- **핵심 가치**:
  - 데이터 수집 비용 90% 이상 절감 및 신속한 의사결정 지원
  - 표본오차(Sampling Error)의 수학적 정량화를 통한 리스크 통제

### Ⅱ. 추론통계의 수학적 이론 기반

#### 한줄 요약: 대수의 법칙과 중심극한정리(CLT)를 통해 표본 크기가 충분하면 표본평균이 정규분포에 수렴하는 성질 활용

### 1. 중심극한정리 (Central Limit Theorem, CLT)
- 모집단의 분포 형태(정규분포, 왜곡분포, 균일분포 등)와 관계없이, 표본의 크기 $n$이 충분히 클 때($n \ge 30$) 표본평균 $\bar{X}$의 표본분포는 모평균 $\mu$, 표본분산 $\frac{\sigma^2}{n}$을 따르는 정규분포에 근사함:
  $$\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$$

### 2. 표본오차와 표준오차 (Standard Error, SE)
- **표본오차 (Sampling Error)**: 표본 통계량과 모집단 모수 사이의 불가피한 수학적 차이 ($|\bar{X} - \mu|$)
- **표준오차 (Standard Error)**: 표본평균들의 표준편차로, 표본 크기 $n$이 커질수록 반비례하여 오차가 감소함:
  $$SE = \frac{\sigma}{\sqrt{n}} \approx \frac{s}{\sqrt{n}}$$

### 3. 대수의 법칙 (Law of Large Numbers, LLN)
- 표본의 크기 $n$이 무한히 커짐에 따라 표본평균 $\bar{X}$는 모평균 $\mu$에 확률적으로 100% 수렴한다는 정리

### Ⅲ. 추론통계의 2대 핵심 축: 추정과 가설검정 메커니즘

<div class="itpe-diagram-box">
  <div class="itpe-diagram-header">
    <span class="itpe-tag">아키텍처 다이어그램</span>
    <span class="itpe-title">추론통계의 모집단-표본 관계와 2대 축(추정 및 가설검정) 구조</span>
  </div>
  <div class="itpe-diagram-body">
    <svg class="itpe-svg" viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-infer" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--color-text, #333)" />
        </marker>
      </defs>
      <!-- 모집단 박스 -->
      <rect x="20" y="15" width="480" height="60" rx="6" fill="var(--color-bg-secondary, #f0f4f8)" stroke="var(--color-border, #0284c7)" stroke-width="2" />
      <text x="260" y="38" font-size="14" font-weight="bold" text-anchor="middle" fill="var(--color-text, #111)">모집단 (Population)</text>
      <text x="260" y="58" font-size="12" text-anchor="middle" fill="var(--color-text-muted, #555)">관심 대상 전체 집단 ┃ 모수(Parameter: 모평균 μ, 모분산 σ², 모비율 p)</text>

      <!-- 표본추출 화살표 (하향) -->
      <path d="M 120 75 L 120 125" stroke="var(--color-primary, #0284c7)" stroke-width="2" marker-end="url(#arrow-infer)" />
      <text x="135" y="105" font-size="11" fill="var(--color-primary, #0284c7)" font-weight="bold">무작위 표본추출 (Random Sampling)</text>

      <!-- 표본 박스 -->
      <rect x="20" y="130" width="480" height="55" rx="6" fill="var(--color-bg, #ffffff)" stroke="var(--color-border, #0284c7)" stroke-width="2" />
      <text x="260" y="152" font-size="14" font-weight="bold" text-anchor="middle" fill="var(--color-text, #111)">표본 (Sample, 크기 n)</text>
      <text x="260" y="172" font-size="12" text-anchor="middle" fill="var(--color-text-muted, #555)">관측된 실제 데이터 ┃ 통계량(Statistic: 표본평균 X̄, 표본분산 s², 표본비율 p̂)</text>

      <!-- 통계적 추론 화살표 (상향) -->
      <path d="M 400 130 L 400 80" stroke="var(--color-accent, #10b981)" stroke-width="2" marker-end="url(#arrow-infer)" />
      <text x="270" y="105" font-size="11" fill="var(--color-accent, #10b981)" font-weight="bold">통계적 추론 (Statistical Inference)</text>

      <!-- 하단 2대 축 분할 카드 -->
      <rect x="20" y="200" width="230" height="70" rx="5" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5" />
      <text x="135" y="220" font-size="12" font-weight="bold" text-anchor="middle" fill="#1d4ed8">1. 추정 (Estimation)</text>
      <text x="135" y="238" font-size="10" text-anchor="middle" fill="#1e40af">• 점추정: 모수를 단일 값으로 예측 (X̄ = μ)</text>
      <text x="135" y="254" font-size="10" text-anchor="middle" fill="#1e40af">• 구간추정: 95% 신뢰구간 (X̄ ± 1.96 · SE)</text>

      <rect x="270" y="200" width="230" height="70" rx="5" fill="#f0fdf4" stroke="#10b981" stroke-width="1.5" />
      <text x="385" y="220" font-size="12" font-weight="bold" text-anchor="middle" fill="#047857">2. 가설검정 (Hypothesis Testing)</text>
      <text x="385" y="238" font-size="10" text-anchor="middle" fill="#065f46">• 귀무가설(H0) vs 대립가설(H1) 수립</text>
      <text x="385" y="254" font-size="10" text-anchor="middle" fill="#065f46">• p-value < α(0.05) 판정으로 효과 검증</text>
    </svg>
  </div>
  <div class="itpe-diagram-footer">
    표본 데이터로부터 출발하여 미지의 모수를 범위로 좁히는 추정(Estimation)과, 주장의 타당성을 유의확률로 판정하는 가설검정이 결합됨
  </div>
</div>

### 1. 통계적 추정 (Estimation)
- **점추정 (Point Estimation)**: 모수를 단 하나의 수치로 추정. 바람직한 점추정량의 4대 기준:
  1. 불편성(Unbiasedness): 추정량의 기댓값이 참 모수와 일치 ($E(\hat{\theta}) = \theta$).
  2. 일치성(Consistency): 표본 크기가 커질수록 추정량이 참 모수에 수렴.
  3. 효율성(Efficiency): 다른 불편추정량 대비 분산이 가장 작음.
  4. 충분성(Sufficiency): 모집단에 대한 모든 정보를 담고 있음.
- **구간추정 (Interval Estimation)**: 참 모수가 포함될 것으로 기대되는 신뢰구간(Confidence Interval, CI)을 제시.
  - 모분산 $\sigma$를 알고 정규분포를 따를 때의 95% 신뢰구간:
    $$CI_{95\%} = \left[ \bar{X} - 1.96 \frac{\sigma}{\sqrt{n}}, \; \bar{X} + 1.96 \frac{\sigma}{\sqrt{n}} \right]$$
  - 소표본($n < 30$) 및 모분산 미인지 시 t-분포($t_{\alpha/2, n-1}$)를 적용.

### 2. 가설검정 (Hypothesis Testing)
- **가설 수립**:
  - 귀무가설 ($H_0$): 기존 상태 유지, 차이가 없음, 효과가 없음 ($\mu_1 = \mu_2$).
  - 대립가설 ($H_1$): 연구자가 입증하려는 새로운 주장, 차이가 있음 ($\mu_1 \ne \mu_2$).
- **오류 유형**:
  - 제1종 오류 ($\alpha$): 참인 귀무가설을 잘못 기각 (위양성, False Positive). 유의수준으로 제어.
  - 제2종 오류 ($\beta$): 거짓인 귀무가설을 채택 (위음성, False Negative). 검정력($1-\beta$)으로 관리.
- **유의확률 ($p$-value)**:
  - 귀무가설이 참이라는 전제하에, 관측된 표본 통계량 이상의 극단적인 값이 나올 확률.
  - $p\text{-value} < \alpha$ (통상 0.05)이면 $H_0$를 기각하고 $H_1$을 통계적으로 유의하게 채택.

### Ⅳ. 기술통계(Descriptive)와 추론통계(Inferential) 비교

#### 한줄 요약: '데이터 자체의 현재 요약'에 머무는 기술통계와, '보이지 않는 모집단의 미래·본질을 예측'하는 추론통계

| 비교 항목 | 기술통계 (Descriptive Statistics) | 추론통계 (Inferential Statistics) |
|:---|:---|:---|
| **기본 목적** | 수집된 관측 데이터의 특징 요약 및 시각화 | 표본을 바탕으로 미지의 모집단 특성 추론 및 일반화 |
| **분석 대상** | 관측 완료된 표본 또는 모집단 전체 데이터 | 관측된 일부 표본 (Sample Data) |
| **수학적 가정** | 확률 분포 가정 불필요 (단순 계산) | 확률 이론, 중심극한정리, 정규분포 가정 필수 |
| **핵심 지표** | 평균, 중위수, 분산, 왜도, 첨도, 사분위수 | 신뢰구간(CI), 검정통계량($z, t, F$), 유의확률($p$-value) |
| **결과의 성격** | 확정적 사실 (현재 상태의 서술) | 확률적 추론 (오차범위를 수반한 일반화) |
| **오류 위험** | 단순 계산 오류 외 이론적 위험 없음 | 표본 편향, 제1종 오류($\alpha$), 제2종 오류($\beta$) 발생 가능 |
| **대표 기법** | 히스토그램, 박스플롯, 피어슨 상관계수 | 독립 t-검정, 대응 t-검정, ANOVA, 회귀분석, 카이제곱 |

### Ⅴ. 모수 검정(Parametric) vs 비모수 검정(Non-parametric)

#### 한줄 요약: 모집단의 정규분포 가정을 전제하는 모수 검정과, 순위·부호 기반의 비모수 검정

| 구분 | 모수 검정 (Parametric Test) | 비모수 검정 (Non-parametric Test) |
|:---|:---|:---|
| **전제 조건** | 모집단이 정규분포를 따름 (등분산성 충족) | 정규성 가정 불필요, 이상치(Outlier) 다수 존재 |
| **자료 척도** | 등간척도, 비율척도 (연속형 데이터) | 명목척도, 서열척도 (범주형, 순위 데이터) |
| **표본 크기** | 대규모 표본 ($n \ge 30$) 권장 | 소규모 표본 ($n < 30$)에 주로 사용 |
| **검정력** | 가정이 충족될 경우 비모수 대비 검정력 우수 | 가정이 위배되었을 때 더 안전하고 견고함 |
| **단일 표본** | 단일표본 t-검정 (One-sample t-test) | 윌콕슨 부호순위 검정 (Wilcoxon Signed Rank) |
| **두 독립 표본** | 독립표본 t-검정 (Two-sample t-test) | 맨-휘트니 U 검정 (Mann-Whitney U Test) |
| **두 대응 표본** | 대응표본 t-검정 (Paired t-test) | 윌콕슨 부호순위 검정 (대응 표본용) |
| **세 집단 이상** | 일원배치 분산분석 (One-way ANOVA) | 크루스칼-왈리스 검정 (Kruskal-Wallis Test) |

### Ⅵ. 빅데이터 및 AI 시대의 실무 한계와 대책

#### 한줄 요약: 표본이 수천만 건에 달할 때 사소한 노이즈도 유의하다고 판정하는 p-value 역설 극복 및 A/B 테스트 최적화

```text
[빅데이터 환경의 p-value 역설과 효과 크기 병행 체계]

  데이터 수백만 건 유입 ──► 표준오차 SE -> 0 수렴 ──► 검정통계량 t -> 무한대 폭증
                                                            │
                                                            ▼
                           [사소한 0.001% 차이도 p < 0.0001 (통계적 유의) 판정]
                                                            │
                                                            ▼
                           [해결책: 통계적 유의성 + 실질적 유의성(효과 크기) 결합]
                           • Cohen's d / r² 산출로 실제 비즈니스 임팩트 평가
```

- **빅데이터의 p-value 역설 (p-value Paradox)**:
  - 표준오차 $SE = \frac{s}{\sqrt{n}}$에서 표본 수 $n$이 수천만 건으로 폭증하면 $SE$가 0에 수렴하여, 두 집단 간의 실제 차이가 $0.0001$에 불과한 노이즈라도 검정통계량이 치솟아 $p < 0.001$로 기각됨
  - **대응책**: 통계적 유의성($p$-value)만 보지 않고, 비즈니스 실질적 차이를 정량화하는 **효과 크기(Effect Size, Cohen's d)**를 반드시 병행 산출함
- **p-해킹(p-hacking) 및 재현성 위기 방지**:
  - 유의한 $p$-value가 나올 때까지 여러 변수를 조합하고 표본을 임의로 쪼개는 데이터 준설(Data Dredging) 차단
  - 분석 전 가설과 실험 설계를 사전에 등록하는 사전등록제(Preregistration) 및 벤자미니-호흐베르크(FDR) 다중비교 보정 적용
- **A/B 테스트 표본 크기 사전 설계 (Power Analysis)**:
  - 실험 전 검정력 $1-\beta=0.8$, 유의수준 $\alpha=0.05$, 최소 탐지 가능 효과(MDE)를 설정하여 최적 표본 수를 수학적으로 사전 확정

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 머신러닝과 빅데이터의 시대에도 추론통계는 절대 대체되지 않는다. 오히려 수억 건의 로그를 풀스캔하느라 클라우드 비용을 낭비하는 현업 엔지니어링 환경에서, 추론통계 기반의 표본 추출(Sampling)과 신뢰구간 산출은 막대한 비용 절감의 핵심 무기이다. 답안을 작성할 때는 "모집단-표본-추정-가설검정"의 학술적 정의를 완벽히 구조화한 뒤, 반드시 '빅데이터 환경의 p-value 역설'과 '온라인 A/B 테스트 최적화'라는 현대적 실무 이슈로 연결해야 기술사다운 차별화가 완성된다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 모집단과 표본의 통계량 매핑 SVG 다이어그램, 기술통계 vs 추론통계 비교표, 점/구간 추정 및 p-value 판정식을 명확한 표로 압축 제시하겠다. 2교시형이라면 빅데이터 분석 시 전체 스캔 대비 0.1% 무작위 샘플링을 통한 쿼리 비용 99% 절감 방안을 제시하고, 표본 크기 과다에 따른 p-해킹을 방지하기 위해 'Cohen's d 효과 크기'와 'A/B 테스트 검정력 분석(Power Analysis)'을 파이프라인에 필수 게이트로 거는 아키텍처를 제안하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 빅데이터 환경에서 무조건적인 전수 풀스캔은 클라우드 I/O 비용과 분석 지연을 초래하며, 표본 과다 시 사소한 편향도 $p < 0.05$로 왜곡되는 p-value 역설이 발생함.
- **대응**: 표본 추출 단계에서 층화 무작위 추출(Stratified Sampling)로 대표성을 확보하고, 통계적 유의확률($p$-value)과 함께 실질적 영향력인 효과 크기(Cohen's d)를 필수 검증 지표로 병행 도입함.
- **검증**: A/A 테스트를 사전 수행하여 파이프라인의 편향 여부를 영점 조절하고, 최소 탐지 가능 효과(MDE) 기반의 표본 크기 사전 산정으로 검정력 80%를 보장함.
- **효과**: 빅데이터 쿼리 연산 비용 90% 이상 절감 및 데이터 기반 의사결정의 과학적 재현성 100% 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <span class="step-num">1. 현행 한계</span>
    <span class="step-title">빅데이터 전수 스캔·p-역설</span>
    <span class="step-desc">대용량 풀스캔으로 인한 인프라 비용 폭증 및 대규모 표본에 따른 사소한 노이즈 기각 왜곡</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">2. 개선 방안</span>
    <span class="step-title">층화 샘플링 & 효과크기 병행</span>
    <span class="step-desc">대표성 보장 층화 무작위 표본추출 도입 및 p-value와 Cohen's d 효과크기 동시 평가</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">3. 검증 기준</span>
    <span class="step-title">A/A 테스트 & 사전 검정력</span>
    <span class="step-desc">사전 A/A 테스트로 편향 영점 조절 및 최소 탐지 가능 효과(MDE) 기반 최적 표본수 확정</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">4. 실행 효과</span>
    <span class="step-title">비용 절감 및 신뢰 의사결정</span>
    <span class="step-desc">클라우드 분석 비용 90% 절감 및 신제품/기능 배포 판정의 통계적 타당성 100% 보장</span>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제123회 정보관리 2교시: 데이터 통계 분석에서 기술통계(Descriptive Statistics)와 추론통계(Inferential Statistics)의 개념 비교 및 추론통계의 핵심 요소(추정과 검정)
  - 제118회 컴퓨터시스템응용 1교시: 가설검정의 1종 오류와 2종 오류, 유의수준의 관계
- **검증 출처**:
  - Ronald E. Walpole et al., "Probability & Statistics for Engineers & Scientists 9th Edition", Chapters 8-10
  - 한국통계학회 통계학용어사전, 추론통계학 및 가설검정 편
  - David Freedman et al., "Statistics 4th Edition", W.W. Norton & Company
---

## 연결 토픽

- 상위 토픽: [03-080 탐색적 데이터 분석(EDA)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/080_eda.md)
- 연관 토픽: [03-124 대응표본 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/124_paired_t_test.md), [03-130 독립표본 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/130_independent_t_test.md), [03-163 점추정 vs 구간추정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/163_point_vs_interval_estimation.md)
- 확장 토픽: [03-094 A/B 테스트](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/094_ab_testing.md)
