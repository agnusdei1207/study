---
sidebar:
  order: 86
  label: "086. t-검정 (t-test)"
  badge:
    text: "A"
    variant: note
title: "t-검정 (Student's t-test) 및 독립표본·대응표본 가설검정"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 86
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "086"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>t-검정 (t-test)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">t-검정 통계량 구조 및 3대 핵심 유형 비교</text>

  <!-- Formula Box -->
  <g transform="translate(30, 48)">
    <rect x="0" y="0" width="460" height="60" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="20" y="24" font-size="10.5" font-weight="bold" fill="#1e40af">t-통계량 = (표본평균 - 기준모평균) / 표본표준오차</text>
    <text x="20" y="44" font-size="10" fill="#0f172a">t = (X̄ - μ₀) / (s / √n),   자유도: df = n - 1</text>
  </g>

  <!-- 3 Types Boxes -->
  <g transform="translate(30, 120)">
    <!-- Type 1 -->
    <rect x="0" y="0" width="145" height="95" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="0" y="0" width="145" height="24" rx="5" fill="#eff6ff"/>
    <text x="72" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 단일표본 (One-sample)</text>
    <text x="10" y="38" font-size="8" fill="#334155">&bull; 대상: 집단 1개 vs 기준값</text>
    <text x="10" y="52" font-size="8" fill="#334155">&bull; H₀: μ = μ₀</text>
    <text x="10" y="68" font-size="7.5" fill="#64748b">예: 신규 캐시 응답이 SLA 50ms 이하인가?</text>

    <!-- Type 2 -->
    <rect x="155" y="0" width="150" height="95" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="155" y="0" width="150" height="24" rx="5" fill="#eff6ff"/>
    <text x="230" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">2. 독립표본 (Two-sample)</text>
    <text x="165" y="38" font-size="8" fill="#334155">&bull; 대상: 독립 집단 A vs B</text>
    <text x="165" y="52" font-size="8" fill="#334155">&bull; H₀: μ₁ = μ₂ (등분산/Welch)</text>
    <text x="165" y="68" font-size="7.5" fill="#64748b">예: UI A안 vs B안 체류시간 차이 검증</text>

    <!-- Type 3 -->
    <rect x="315" y="0" width="145" height="95" rx="5" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <rect x="315" y="0" width="145" height="24" rx="5" fill="#eff6ff"/>
    <text x="387" y="16" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 대응표본 (Paired)</text>
    <text x="325" y="38" font-size="8" fill="#334155">&bull; 대상: 동일 개체 전/후</text>
    <text x="325" y="52" font-size="8" fill="#334155">&bull; H₀: μ_D = 0 (차이 검정)</text>
    <text x="325" y="68" font-size="7.5" fill="#64748b">예: DB 인덱스 튜닝 전 vs 후 쿼리 시간</text>
  </g>

  <!-- Bottom Banner -->
  <g transform="translate(30, 225)">
    <rect x="0" y="0" width="460" height="35" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="12" y="16" font-size="8" fill="#475569">&bull; 모분산(σ²)을 모를 때 표본표준편차(s)로 대체하며, 자유도가 커질수록 표준정규분포에 수렴</text>
    <text x="12" y="28" font-size="8" fill="#475569">&bull; 전제조건: 독립성, 정규성(위배 시 비모수 분기), 등분산성(위배 시 Welch's t-test 적용)</text>
  </g>
</svg>
</div>

- 본질: **모집단의 분산($\sigma^2$)을 알 수 없는 현실 상황에서, 표본표준편차($s$)와 자유도($df$)에 기반한 t-분포를 이용하여 두 집단 간 평균의 차이가 단순한 표본오차에 의한 것인지 통계적으로 유의미한지를 판별하는 대표적인 모수적 가설검정 기법**
- 암기: `단-독-대` (단일표본, 독립표본, 대응표본) / `모-자-표-피` (모분산 미지, 자유도 df, 표본표준오차, p-value 기각 판정)
- 판단축:
  - **독립표본 t-검정**: 상호 독립된 두 집단 비교 $\rightarrow$ 사전 등분산 검정(Levene) 필수, 분산 다를 시 Welch's t-test 적용
  - **대응표본 t-검정**: 동일 개체의 전/후 차이값($D_i = X_{1i} - X_{2i}$) 비교 $\rightarrow$ 개체 간 고유 편차가 소거되어 통계적 검정력(Power)이 훨씬 높음
- 주의: t-검정은 표본의 정규성(Normality)을 전제하므로, 소표본($n < 30$)에서 왜도가 심할 경우 1종 오류가 급증함. Shapiro-Wilk 검정으로 정규성을 확인하고, 정규성 위배 시 비모수 검정(Mann-Whitney U 검정, Wilcoxon 부호순위 검정)을 적용해야 함

## Ⅰ. 모분산 미지 상황을 극복하는 t-검정(Student's t-test) 개요

#### 한줄 요약: 모분산을 모를 때 표본분산을 사용하여 소표본에서도 정확한 평균 차이를 검정할 수 있도록 고안된 통계 기법

- **등장 배경**:
  - 전통적인 z-검정은 중심극한정리에 기반하여 모집단의 표준편차($\sigma$)를 알고 있어야 적용 가능함
  - 그러나 현실의 비즈니스 및 엔지니어링 데이터에서 모분산($\sigma^2$)을 사전에 알고 있는 경우는 사실상 존재하지 않음
  - 1908년 윌리엄 고셋(William Gosset, 필명 Student)이 양조 공정 소표본 실험에서 모분산 대신 표본표준편차($s$)를 대입할 때 발생하는 오차를 보정한 **t-분포(t-distribution)**를 발표하면서 확립됨
- **t-검정의 정의**:
  - 모집단의 분산이 알려지지 않은 상황에서, 표본에서 계산된 표본평균($\bar{X}$)과 표본표준편차($s$)를 이용하여 모평균에 대한 가설을 검정하는 모수적 통계 추론 방법

## Ⅱ. t-검정의 핵심 수학적 구조: t-분포와 자유도($df$)

#### 한줄 요약: 표본 크기에 따라 꼬리가 두터워지는 t-분포를 통해 소표본의 추정 불확실성을 수학적으로 보정

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 135" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="115" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">표준정규분포(Z)와 t-분포의 두터운 꼬리(Fat Tail) 비교</text>

  <!-- Plot Area -->
  <g transform="translate(60, 42)">
    <line x1="0" y1="65" x2="400" y2="65" stroke="#94a3b8" stroke-width="1.2"/>
    <line x1="200" y1="65" x2="200" y2="5" stroke="#94a3b8" stroke-width="1.2"/>

    <!-- Normal Curve N(0, 1) -->
    <path d="M 50 65 Q 150 64, 180 30 Q 200 8, 220 30 Q 250 64, 350 65" fill="none" stroke="#2563eb" stroke-width="2"/>
    <text x="205" y="18" font-size="8" font-weight="bold" fill="#2563eb">정규분포 Z ~ N(0, 1)</text>

    <!-- t-distribution (df=3) -->
    <path d="M 30 63 Q 130 58, 170 36 Q 200 18, 230 36 Q 270 58, 370 63" fill="none" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="245" y="35" font-size="8" fill="#ef4444">t-분포 (df=3: Fat Tail)</text>

    <text x="200" y="78" font-size="8" fill="#64748b" text-anchor="middle">0 (중심값)</text>
  </g>
</svg>
</div>

### 1. 자유도(Degrees of Freedom, $df$)의 개념
- 통계량을 계산할 때 독립적으로 자유롭게 변할 수 있는 데이터 관측치의 개수
- 크기 $n$인 표본에서 표본평균 $\bar{X}$가 고정되면, 마지막 $n$번째 데이터는 자동으로 결정되므로 자유도는 **$df = n - 1$**이 됨

### 2. t-통계량의 기본 수식
$$t = \frac{\bar{X} - \mu_0}{\frac{s}{\sqrt{n}}} \sim t(n - 1)$$
- $\bar{X}$: 표본평균, $\mu_0$: 귀무가설의 기준 모평균
- $s$: 표본표준편차 ($s = \sqrt{\frac{1}{n-1}\sum (X_i - \bar{X})^2}$)
- $s / \sqrt{n}$: 표본표준오차 (Standard Error of the Mean, SEM)

## Ⅲ. t-검정의 3대 핵심 유형 및 수식 분석

#### 한줄 요약: 기준값 비교(단일표본), 두 독립 집단 비교(독립표본), 전/후 짝지은 비교(대응표본)의 구조적 차이

### 1. 단일표본 t-검정 (One-sample t-test)
- **적용 목적**: 특정 단일 표본 집단의 평균이 알려진 모평균 기준값과 같은지 검증
- **수식**: $t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}$, 자유도 $df = n - 1$

### 2. 독립표본 t-검정 (Independent Two-sample t-test)
- **적용 목적**: 서로 다른 두 독립 모집단에서 추출한 표본들의 평균 차이($\mu_1 - \mu_2$)를 검증
- **등분산 만족 시 (Pooled t-test)**:
  $$t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \quad s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}, \quad df = n_1 + n_2 - 2$$
- **이분산 시 (Welch's t-test)**:
  - 두 집단의 분산이 다를 때 Satterthwaite 근사식을 이용해 자유도를 재계산하여 1종 오류 억제

### 3. 대응표본 t-검정 (Paired-sample t-test)
- **적용 목적**: 동일한 대상에게 실험 처치를 가하기 전과 후의 변화 차이($D_i = X_{1i} - X_{2i}$)를 검증
- **수식**:
  $$t = \frac{\bar{D} - \mu_D}{\frac{s_D}{\sqrt{n}}}, \quad df = n - 1$$
  - $\bar{D}$: 차이값들의 표본평균, $s_D$: 차이값들의 표본표준편차
- **특징**: 두 변수 간의 높은 상관성(Correlation)을 활용하여 개체 간의 고유 변동을 상쇄시키므로, 독립표본 t-검정 대비 훨씬 강력한 검정력을 발휘함

## Ⅳ. 가설검정 방법 간 비교 (t-검정 vs z-검정 vs 분산분석 ANOVA)

#### 한줄 요약: 모분산 인지 여부, 표본의 크기, 비교 집단의 수에 따른 통계 검정 도구 선택 기준

| 비교 항목 | t-검정 (Student's t-test) | z-검정 (Z-test) | 분산분석 (ANOVA, F-test) |
|:---|:---|:---|:---|
| **모분산($\sigma^2$) 인지 여부**| **모름** (표본분산 $s^2$로 대체) | **반드시 알아야 함** | 모름 (표본분산 활용) |
| **비교 집단 수** | **1개 또는 2개 집단** | 1개 또는 2개 집단 | **3개 이상의 복수 집단** |
| **검정 통계량 분포**| **t-분포 (자유도 $df$)** | **표준정규분포 ($Z \sim N(0, 1)$)**| **F-분포 ($df_1, df_2$)** |
| **소표본($n < 30$) 대응**| **완벽 대응** (두터운 꼬리로 보정) | 불가 (정규성 위배 시 왜곡) | 정규성 만족 시 가능 |
| **주요 활용 분야** | A/B 테스트, 전후 성능 비교 | 대규모 여론조사 (비율 검정) | 마케팅 채널별(A, B, C) 매출 비교 |

## Ⅴ. t-검정의 3대 전제 조건과 사전 검정 파이프라인

#### 한줄 요약: 정규성, 등분산성, 독립성 가정의 충족 여부를 확인하고 위배 시 대체 검정으로 분기

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 120" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="100" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">t-검정 3대 전제 조건 판정 및 분기 흐름</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="145" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="72" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 독립성 검정</text>
    <text x="72" y="34" font-size="7.5" fill="#334155" text-anchor="middle">무작위 표본 추출</text>
    <text x="72" y="47" font-size="7.5" fill="#64748b" text-anchor="middle">Durbin-Watson</text>

    <path d="M 148 27 L 168 27" stroke="#64748b" stroke-width="1.5"/>

    <rect x="170" y="0" width="145" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="242" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">2. 정규성 검정</text>
    <text x="242" y="34" font-size="7.5" fill="#334155" text-anchor="middle">Shapiro-Wilk</text>
    <text x="242" y="47" font-size="7.5" fill="#dc2626" text-anchor="middle">위배 시 &rarr; 비모수 검정</text>

    <path d="M 318 27 L 338 27" stroke="#64748b" stroke-width="1.5"/>

    <rect x="340" y="0" width="135" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="407" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 등분산성 검정</text>
    <text x="407" y="34" font-size="7.5" fill="#334155" text-anchor="middle">Levene 검정</text>
    <text x="407" y="47" font-size="7.5" fill="#2563eb" text-anchor="middle">위배 시 &rarr; Welch's t</text>
  </g>
</svg>
</div>

## Ⅵ. IT 및 데이터 엔지니어링 실무 응용

#### 한줄 요약: A/B 테스트 의사결정, 데이터베이스 튜닝 전후 검증, p-해킹(Peeking) 방지 엔지니어링

### 1. 신규 알고리즘 A/B 테스트 (독립표본 t-검정)
- 추천 알고리즘 v1(Control)과 v2(Treatment)에 각각 무작위 할당된 10,000명 사용자의 1인당 매출액(ARPU) 차이 검증
- 등분산성 위배 시 Welch's t-test를 호출하여 $p < 0.05$일 때 신규 알고리즘 전면 롤아웃 결정

### 2. 데이터베이스 인덱스 튜닝 전후 검증 (대응표본 t-검정)
- 피크 시간대 실제 운영 쿼리 200개를 추출하여 튜닝 전 실행시간과 인덱스 추가 후 실행시간을 1:1 매핑
- 환경 변화(CPU 부하, 네트워크 지연)의 영향을 상쇄하고 순수 인덱스 효과에 의한 지연시간 단축($\bar{D} > 0$)을 입증

### 3. A/B 테스팅의 함정: 피킹(Peeking)과 P-해킹 방지
- 실험 도중 매일 p-value를 확인하다가 우연히 $p < 0.05$가 되는 순간 실험을 조기 종료하면 실제로는 차이가 없는데 유의하다고 오판하는 제1종 오류가 최대 30%까지 급증
- 사전에 최소 표본 크기($N$)를 파워 분석(Power Analysis)으로 확정하거나, 연속 가설검정(Sequential Testing) 프레임워크 적용 필수

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 빅데이터 시대에 t-검정 적용 시 가장 주의할 점은 **"표본 크기가 커지면 p-value는 무조건 0으로 수렴한다"**는 사실이다. 표본이 100만 건이면 응답 속도 0.001ms 단축도 $p < 0.0001$로 나와 통계적으로 유의하다고 판정된다. 따라서 실무 의사결정에서는 단순 p-value 통과 여부에 매몰되지 말고, 실제 개선 폭의 실질적 가치를 나타내는 **효과 크기(Cohen's d)**와 신뢰구간(Confidence Interval)을 반드시 병기해야 한다.

> **[나라면 이렇게 쓴다]**
> 10점형 답안이라면 t-통계량 공식과 3대 유형(단일, 독립, 대응)의 차이를 명확한 표로 작성하겠다. 25점형이라면 정규성(Shapiro-Wilk)과 등분산성(Levene) 사전 검정 파이프라인을 그리고, A/B 테스트 시 조기 종료로 인한 1종 오류(Peeking Problem) 방지 방안을 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 모분산 인지 전제의 z-검정 오류 적용 및 빅데이터 환경에서 p-value 착시로 인한 무의미한 기능 배포
- **대응 (개선 방안)**: 모분산 미지 시 t-분포 기반 검정 적용, 등분산 위배 시 Welch's t-test 자동 분기 및 효과 크기(Cohen's d) 병행 평가
- **검증 (검증 기준)**: Shapiro-Wilk 정규성 검증(p &gt; 0.05), Levene 등분산 검증, Cohen's d &ge; 0.2 (실질적 유의미성) 확보
- **효과 (실행 효과)**: A/B 테스트 의사결정 신뢰도 95% 확보 및 가짜 성능 개선에 따른 불필요한 배포 비용 절감

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">모분산 미인지 상태 z-검정 오류 및 대규모 표본 p-value 착시</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">자동 분기 t-검정 파이프라인 (Welch's t) + Cohen's d 효과크기 산출</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">정규성/등분산성 사전 검정 통과, p &lt; 0.05, Cohen's d &ge; 0.2</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">A/B 테스트 및 DB 튜닝 전후 성능 검증의 통계적 타당성 완결</div>
  </div>
</div>
---

## 1교시 예상문제 (10점)

> t-검정 (Student's t-test) 및 독립표본·대응표본 가설검정의 정의, 목적, 핵심 메커니즘을 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. 정의·목적

- 정의: 표본분산($s^2$)과 자유도($df=n-1$)에 따른 t-분포를 이용하여 평균 차이의 유의성을 검정
- 목적: 모분산을 모를 때 표본분산과 t-분포를 이용해 평균에 대한 가설을 검정한다.

### 2. 핵심 관계

| 비교 항목 | t-검정 (Student's t-test) | z-검정 (Z-test) |
|:---|:---|:---|
| **모분산 인지 여부** | 모름 (표본표준편차 $s$ 사용) | 알고 있음 (모표준편차 $\sigma$) |
| **표본 크기** | 소표본($n<30$) 및 대규모 범용 | 대규모 표본($n \ge 30$) 한정 |
| **기준 분포** | t-분포 (자유도 $n-1$) | 표준정규분포 $N(0, 1)$ |
| **꼬리 두께** | 중심 낮고 꼬리 두터움 (Fat Tail) | 꼬리가 얇음 |

### 핵심 관계

| 비교 항목 | t-검정 (Student's t-test) | z-검정 (Z-test) |
|:---|:---|:---|
| **모분산 인지 여부** | 모름 (표본표준편차 $s$ 사용) | 알고 있음 (모표준편차 $\sigma$) |
| **표본 크기** | 소표본($n<30$) 및 대규모 범용 | 대규모 표본($n \ge 30$) 한정 |
| **기준 분포** | t-분포 (자유도 $n-1$) | 표준정규분포 $N(0, 1)$ |
| **꼬리 두께** | 중심 낮고 꼬리 두터움 (Fat Tail) | 꼬리가 얇음 |

- 제언: 독립성·정규성·등분산 가정을 확인하고 표본 설계에 맞는 t-검정 유형과 효과 크기를 보고한다.
---

## 2~4교시 예상문제 (25점)

> 데이터 분석 및 A/B 테스트에서 널리 활용되는 가설검정 기법인 t-검정(Student's t-test)의 개념과 도입 배경을 설명하고, z-검정과의 차이점, 3가지 주요 유형(단일표본, 독립표본, 대응표본)의 수식 및 특징을 비교한 후, 가설검정 시 충족해야 할 전제조건을 서술하시오. (25점)
---

## 2~4교시 25점 답안

### Ⅰ. 모분산 미지 상황의 해결사, t-검정의 개념 및 배경

1. **배경**: 모집단의 분산($\sigma^2$)을 알 수 없는 현실에서 표준정규분포 기반 z-검정 적용 불가
2. **정의**: 표본분산($s^2$)과 자유도($df=n-1$)에 따른 t-분포를 이용하여 평균 차이의 유의성을 검정

### Ⅱ. t-검정 vs z-검정 핵심 비교

| 비교 항목 | t-검정 (Student's t-test) | z-검정 (Z-test) |
|:---|:---|:---|
| **모분산 인지 여부** | 모름 (표본표준편차 $s$ 사용) | 알고 있음 (모표준편차 $\sigma$) |
| **표본 크기** | 소표본($n<30$) 및 대규모 범용 | 대규모 표본($n \ge 30$) 한정 |
| **기준 분포** | t-분포 (자유도 $n-1$) | 표준정규분포 $N(0, 1)$ |
| **꼬리 두께** | 중심 낮고 꼬리 두터움 (Fat Tail) | 꼬리가 얇음 |

### Ⅲ. t-검정 3대 유형 수식 및 특성

1. **단일표본**: $t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}$ (기준값과 표본평균 비교)
2. **독립표본**: $t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{1/n_1 + 1/n_2}}$ (A/B 테스트, 등분산 만족 시/Welch)
3. **대응표본**: $t = \frac{\bar{D} - \mu_D}{s_D / \sqrt{n}}$ (동일 개체 전/후 튜닝 성능 비교)

### Ⅳ. 실무 가설검정 전제조건 및 아키텍처 제언

1. **전제조건**: 정규성(Shapiro-Wilk 위배 시 비모수 분기), 등분산성(Levene 위배 시 Welch 적용)
2. **아키텍처 제언**: 빅데이터 표본 과다 시 p-value 착시를 극복하기 위해 효과 크기(Cohen's d) 병행 산출
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제132회 2교시 1번 (중심극한정리, t-검정, z-검정)
  - 컴퓨터시스템응용기술사 제131회 1교시 (독립표본 t-검정과 대응표본 t-검정)
  - 정보관리기술사 제121회 1교시 (가설검정의 오류와 t-검정)
- **표준 및 검증 출처**:
  - Student [William Sealy Gosset] (1908), "The Probable Error of a Mean", *Biometrika*
  - Douglas C. Montgomery & George C. Runger, *Applied Statistics and Probability for Engineers (7th Edition)*
  - 한국통계학회 통계학 용어집 (t-검정, 자유도, 웰치의 t-검정)
---

## 연결 토픽

- [041. 가설검정 (Hypothesis Testing)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/041_hypothesis_testing.md)
- [036. 기술통계 vs 추론통계 (Descriptive vs Inferential Statistics)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/036_descriptive_statistics.md)
- [012. z-검정 (z-test)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/012_z_test.md)
