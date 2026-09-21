---
sidebar:
  order: 130
  label: "130. 독립표본 t-검정 (Independent t-test)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-data"
weight: 130
title: "독립표본 t-검정(Independent t-test)의 3대 기본 가정과 등분산·이분산(Welch) 통계량 검정"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
  question_no: "130"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>독립표본 t-검정</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Top: Independent Groups -->
  <rect x="25" y="15" width="220" height="45" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="135" y="35" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">표본 집단 A (기존 UI)</text>
  <text x="135" y="50" text-anchor="middle" font-size="10" fill="#64748b">n1, 표본평균 X̄1, 표본분산 s1²</text>

  <rect x="275" y="15" width="220" height="45" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="385" y="35" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">표본 집단 B (신규 UI)</text>
  <text x="385" y="50" text-anchor="middle" font-size="10" fill="#64748b">n2, 표본평균 X̄2, 표본분산 s2²</text>

  <!-- Step 1: Normality -->
  <path d="M 260 60 L 260 80" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow130)"/>
  <rect x="70" y="80" width="380" height="40" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="260" y="100" text-anchor="middle" font-size="11" font-weight="bold" fill="#1e293b">1단계: 정규성 검정 (Shapiro-Wilk Test)</text>
  <text x="260" y="113" text-anchor="middle" font-size="9" fill="#dc2626">정규성 위배 시 ──► 맨-휘트니 U 검정(비모수)으로 즉시 전환</text>

  <!-- Step 2: Equal Variance -->
  <path d="M 260 120 L 260 140" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow130)"/>
  <rect x="70" y="140" width="380" height="40" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="160" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">2단계: 등분산성 검정 (Levene's Test / F-검정)</text>
  <text x="260" y="173" text-anchor="middle" font-size="9" fill="#78350f">모분산 일치 여부 판정 (p &gt;= 0.05 등분산 vs p &lt; 0.05 이분산)</text>

  <!-- Branching Paths -->
  <path d="M 180 180 L 130 205" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow130)"/>
  <path d="M 340 180 L 390 205" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow130)"/>

  <!-- Step 3 Left: Student t -->
  <rect x="15" y="205" width="230" height="60" rx="6" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="130" y="225" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">등분산 충족: 일반 스튜던트 t-검정</text>
  <text x="130" y="242" text-anchor="middle" font-size="10" fill="#1e293b">합동분산(Sp²) 계산 및 적용</text>
  <text x="130" y="257" text-anchor="middle" font-size="9" fill="#64748b">자유도 df = n1 + n2 - 2</text>

  <!-- Step 3 Right: Welch t -->
  <rect x="275" y="205" width="230" height="60" rx="6" fill="#dcfce7" stroke="#10b981" stroke-width="1.5"/>
  <text x="390" y="225" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">등분산 위배: 웰치의 t-검정 (권장)</text>
  <text x="390" y="242" text-anchor="middle" font-size="10" fill="#1e293b">개별 표본분산 사용 (합동분산 배제)</text>
  <text x="390" y="257" text-anchor="middle" font-size="9" fill="#64748b">Welch-Satterthwaite 보정 자유도</text>

  <defs>
    <marker id="arrow130" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **서로 완전히 독립적인 두 모집단으로부터 추출한 연속형 표본 데이터를 바탕으로, 두 집단의 모평균 사이에 통계적으로 유의미한 차이가 있는지를 가설검정하는 모수적 통계 기법이며, 등분산성 만족 여부에 따라 스튜던트 t-검정과 웰치(Welch)의 t-검정으로 수식이 분기됨**
- 암기: `독-정-등` (3대 기본 가정: 독립성, 정규성, 등분산성) / `합-웰-스` (합동분산, 웰치의 t, 스튜던트 t) / `맨-휘-트-니` (정규성 위배 시 비모수 대안)
- 판단축:
  - **등분산 만족 ($p \ge 0.05$)**: 두 집단의 분산을 가중 평균한 합동분산($s_p^2$)을 사용하여 스튜던트 t-검정 수행 ($df = n_1 + n_2 - 2$)
  - **등분산 위배 ($p < 0.05$)**: 분산이 서로 다르므로 각각의 분산을 독립 반영하고 자유도를 보정하는 **웰치의 t-검정(Welch's t-test)** 수행
- 주의: 실무 A/B 테스트 환경에서 두 집단의 분산이 동일할 확률은 희박하므로, 등분산 검정을 무시하고 기계적으로 스튜던트 t-검정을 적용하면 1종 오류(False Positive)가 급증함

## 예상문제

> 독립 표본 t-검정(Independent Two-Sample t-test)과 대응 표본 t-검정(Paired t-test)의 개념, 기본 가정 3가지, 검정통계량 수식 및 차이점을 비교 설명하고, 등분산성 위배 시 적용하는 웰치의 t-검정(Welch's t-test)의 원리를 기술하시오. (25점)

## Ⅰ. 두 집단 간 평균 차이를 규명하는 독립표본 t-검정 개요

#### 한줄 요약: 서로 다른 두 독립 집단(A/B)의 표본평균 차이가 우연인지 실제 효과인지를 두 집단의 표준오차로 나누어 검정하는 기법

- **배경**:
  - 신규 기능 출시, 마케팅 프로모션, UI 개선 시 "A그룹(기존) 대비 B그룹(개선)의 매출액/전환율 평균이 실제로 상승했는가?"를 과학적으로 입증해야 함
  - 표본의 무작위 추출 오차를 배제하고 통계적 유의확률(p-value)을 통해 의사결정의 객관성을 확보하는 핵심 도구
- **정의**: 모집단이 서로 독립적인 두 집단에서 추출된 표본 데이터를 이용하여 모평균 $\mu_1$과 $\mu_2$가 동일한지 여부를 가설검정하는 통계 분석 방법
- **기본 가설 체계**:
  - 귀무가설($H_0$): $\mu_1 = \mu_2$ (두 집단의 모평균은 차이가 없다)
  - 대립가설($H_1$): $\mu_1 \neq \mu_2$ (양측 검정, 두 집단 간 차이가 있다) 또는 $\mu_1 < \mu_2$ (단측 검정)

## Ⅱ. 독립표본 t-검정의 3대 핵심 기본 가정

#### 한줄 요약: 독립성, 정규성, 등분산성이 모두 충족되어야 모수적 스튜던트 t-검정의 유효성이 보장됨

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="20" y="20" width="150" height="120" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="95" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 독립성</text>
  <text x="95" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Independence</text>
  <text x="95" y="92" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">한 집단의 관측치가</text>
  <text x="95" y="108" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">타 집단에 무영향</text>
  <text x="95" y="128" text-anchor="middle" font-size="9" fill="#64748b">실험 설계 단계 통제</text>

  <!-- Box 2 -->
  <rect x="185" y="20" width="150" height="120" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="260" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. 정규성</text>
  <text x="260" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Normality</text>
  <text x="260" y="92" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">각 집단의 데이터가</text>
  <text x="260" y="108" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">정규분포를 따름</text>
  <text x="260" y="128" text-anchor="middle" font-size="9" fill="#64748b">Shapiro-Wilk 검정</text>

  <!-- Box 3 -->
  <rect x="350" y="20" width="150" height="120" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="425" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. 등분산성</text>
  <text x="425" y="70" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">Homogeneity</text>
  <text x="425" y="92" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">두 집단의 모분산이</text>
  <text x="425" y="108" text-anchor="middle" font-size="10" fill="var(--sl-color-text, #334155)">동일함 (σ1² = σ2²)</text>
  <text x="425" y="128" text-anchor="middle" font-size="9" fill="#64748b">Levene의 검정</text>
</svg>
</div>

1. **독립성 (Independence)**: A그룹에 속한 개체와 B그룹에 속한 개체 사이에 어떠한 상관관계나 물리적 결합도 없어야 함 (동일 인물이 두 그룹에 동시 참여 불가)
2. **정규성 (Normality)**: 두 집단 각각의 모집단 분포가 정규분포 $N(\mu_1, \sigma_1^2)$, $N(\mu_2, \sigma_2^2)$를 따라야 함 (단, 중심극한정리에 의해 각 집단 표본 수 $n_1, n_2 \ge 30$ 이상이면 정규성 가정 완화 가능)
3. **등분산성 (Homoscedasticity)**: 두 모집단의 분산이 서로 동일해야 함 ($\sigma_1^2 = \sigma_2^2$). Levene 검정에서 $p < 0.05$로 등분산성이 기각되면 웰치의 t-검정 적용 필수

## Ⅲ. 등분산성 만족 여부에 따른 검정통계량 수식 분기

#### 한줄 요약: 등분산 시 합동분산 스튜던트 공식, 이분산 시 개별 분산 반영 웰치(Welch) 공식

1. **등분산 가정 성립 시 (스튜던트 t-검정)**:
   - 두 집단의 분산이 같으므로 표본 크기로 가중 평균한 **합동분산(Pooled Variance, $s_p^2$)** 산출:

$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}$$

   - **검정통계량 수식**:

$$t = \frac{(\bar{X}_1 - \bar{X}_2) - 0}{\sqrt{s_p^2 \left( \frac{1}{n_1} + \frac{1}{n_2} \right)}}, \quad df = n_1 + n_2 - 2$$

2. **등분산 가정 위배 시 (웰치의 t-검정, Welch's t-test)**:
   - 분산이 다르므로 합동분산을 구하지 않고 각 집단의 표준오차를 분모에 직접 가산:

$$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$

   - **자유도 보정 (Welch-Satterthwaite 근사식)**:

$$df = \frac{\left( \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} \right)^2}{\frac{(s_1^2 / n_1)^2}{n_1 - 1} + \frac{(s_2^2 / n_2)^2}{n_2 - 1}}$$

## Ⅳ. 독립표본 t-검정 vs 대응표본 t-검정 vs 맨-휘트니 U 검정

#### 한줄 요약: 표본 독립성 여부와 정규성 만족 여부에 따른 검정 기법 선택 체계

| 비교 항목 | 독립표본 t-검정 (Independent) | 대응표본 t-검정 (Paired) | 맨-휘트니 U 검정 (Mann-Whitney U) |
|:---|:---|:---|:---|
| **표본 관계** | **완전히 분리된 독립된 두 집단** | **동일 개체의 짝지은 전후 측정** | 완전히 분리된 독립된 두 집단 |
| **통계적 분류** | **모수 검정 (Parametric)** | **모수 검정 (Parametric)** | **비모수 검정 (Non-parametric)** |
| **분석 대상** | 두 집단 각각의 평균 ($\bar{X}_1, \bar{X}_2$) | 차이값 단일 변수 ($D = X_2 - X_1$) | 두 집단 관측치의 **순위합 (Rank Sum)** |
| **자유도 (df)** | $n_1 + n_2 - 2$ (등분산 시) | $n - 1$ | 자유도 없음 (U 통계량) |
| **필수 기본가정** | **정규성 및 등분산성** | **차이값($D$)의 정규성** | 가정 없음 (정규성 불필요) |
| **이상치 민감도** | 극단 이상치에 매우 취약 | 이상치에 취약 | **이상치에 극도로 강건(Robust)** |

## Ⅴ. 실전 A/B 테스트 적용 및 분석 파이프라인

#### 한줄 요약: 트래픽 무작위 분할 $\rightarrow$ 정규성·등분산성 진단 $\rightarrow$ Welch t-검정 $\rightarrow$ 효과 크기(Cohen's d) 판정

1. **무작위 트래픽 분할 (Random Split)**: 유입 사용자를 쿠키/유저ID 해시 기반으로 통제 집단(Control)과 실험 집단(Treatment)에 50:50으로 무작위 배정하여 독립성 확보
2. **사전 진단**: Shapiro-Wilk로 정규성을 확인하고, Levene 검정으로 등분산성을 확인
3. **검정 기법 분기**:
   - 정규성 위배 시: 맨-휘트니 U 검정 실행
   - 정규성 충족 시: 분산 일치 여부와 무관하게 안전성을 위해 **웰치의 t-검정** 기본 실행
4. **효과 크기(Effect Size) 계산**:
   - 표본 수가 수십만 건에 달하면 사소한 0.001% 차이도 $p < 0.05$로 유의하게 나오므로, 실질적 영향력 평가를 위해 **Cohen's d** 병기:

$$d = \frac{|\bar{X}_1 - \bar{X}_2|}{s_p}$$

## Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 등분산성 무시 1종 오류 차단, 소표본 비정규성 대응, p-해킹(p-hacking) 방지

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **A/B 테스트 결과 거짓 개선 (1종 오류)** | 두 집단의 분산 차이가 큼에도 일반 스튜던트 t-검정 수식을 기계적으로 적용 | 분석 파이프라인의 기본 설정을 **웰치의 t-검정(Welch's t-test)**으로 고정 |
| **결제 금액의 극단적 우측 꼬리 비정규성** | 소수 슈퍼 고래 고객의 결제액으로 정규분포 가정 완전히 붕괴 | 로그 변환($\log(X+1)$)을 적용하거나 비모수 검정인 **맨-휘트니 U 검정**으로 전환 |
| **조기 종료로 인한 위양성 (p-hacking)** | 실험 도중 p-value가 0.05 미만으로 떨어지는 순간 성급하게 실험 조기 중단 | 사전에 필요한 최소 표본 크기(Power Analysis)를 확정하고 해당 표본 도달 전 종료 금지 |

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 많은 데이터 분석가들이 통계 패키지에서 기본 옵션(`scipy.stats.ttest_ind(..., equal_var=True)`)을 그대로 두고 분석을 돌려 잘못된 비즈니스 의사결정을 내린다.
> 실제 웹/모바일 A/B 테스트 환경에서 통제군과 실험군의 분산이 완벽히 같을 확률은 0에 수렴한다.
> 세계적인 통계학계의 표준 권고는 **"등분산 검정을 따로 거치지 말고 언제나 웰치의 t-검정을 디폴트로 사용하라"**는 것이다. 웰치의 t-검정은 두 집단의 분산이 같을 때도 스튜던트 t-검정과 동일한 결과를 내며, 분산이 다를 때 1종 오류를 완벽하게 통제하기 때문이다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "현대 빅데이터 A/B 테스트 플랫폼에서의 통계적 함정 극복"을 제언하겠다. 수백만 트래픽 환경에서 발생하는 '대표본의 역설(소수점 단위의 무의미한 차이도 p < 0.05가 되는 현상)'을 방지하기 위해, p-value 단독 의사결정을 금지하고 **신뢰구간(Confidence Interval)**과 **Cohen's d 효과 크기**, 그리고 순환적 베이지안 A/B 테스트 프레임워크를 병행하는 전사 실험 거버넌스를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 온라인 비즈니스의 기능 개편 및 신규 알고리즘 효과 검증을 위해 엄밀한 독립표본 t-검정 파이프라인 구축이 필수적임.
- **대응**:
  1. **웰치 t-검정 표준화**: 사내 A/B 테스트 분석 엔진의 기본 알고리즘을 웰치의 t-검정으로 영구 고정하여 이분산 리스크 배제.
  2. **비모수 가드레일 수립**: 결제액 등 왜도가 심한 지표는 맨-휘트니 U 검정 및 부트스트랩(Bootstrap) 신뢰구간 병행 분석.
  3. **효과 크기 의무 공시**: p-value와 함께 Cohen's d 효과 크기(최소 0.2 이상)를 비즈니스 배포 조건으로 수립.
- **검증**: 제1종 오류율 5% 이내 통제 및 검정력(Power, $1-\beta$) 80% 이상 확보 검증.
- **효과**: 잘못된 기능 배포로 인한 매출 손실 방지 및 데이터 기반 의사결정의 과학적 신뢰성 극대화.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">이분산 무시 스튜던트 t 적용으로 1종 오류 급증, 거짓 개선 배포</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">웰치의 t-검정 디폴트 적용, Cohen's d 효과 크기 평가 결합</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">Levene 분산 진단, p &lt; 0.05 및 검정력 80% 달성 확인</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">과학적 A/B 테스트 의사결정 및 서비스 전환율 개선 확정</div>
  </div>
</div>

---

## 1교시 10점 답안 발췌

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 서로 독립적인 두 모집단으로부터 추출한 표본평균의 차이가 통계적으로 유의미한지 검정하는 모수적 가설검정 기법 |
| **2. 3대 기본 가정** | 표본의 **독립성**(Independence), 각 집단의 **정규성**(Normality), 두 모집단의 **등분산성**(Homoscedasticity) |
| **3. 등분산/이분산 수식** | - **등분산 충족**: 합동분산($s_p^2$) 기반 스튜던트 t-검정 ($df = n_1+n_2-2$)<br/>- **등분산 위배**: 개별 분산 반영 **웰치의 t-검정(Welch's t-test)** 및 보정 자유도 적용 |
| **4. 비모수 대안** | 정규성 가정이 위배된 경우 순위합 기반의 **맨-휘트니 U 검정(Mann-Whitney U Test)** 적용 |

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제131회 정보관리 2교시: 독립 표본 t-검정(Independent t-test)과 대응 표본 t-검정(Paired t-test)의 개념, 기본 가정 및 차이점
- **검증 출처**:
  - Bernard Rosner, "Fundamentals of Biostatistics (8th Edition)", Cengage Learning
  - B. L. Welch, "The generalization of Student's problem when several different population variances are involved", Biometrika

---

## 학습 체크

- [ ] 독립표본 t-검정의 3대 기본 가정(독립성, 정규성, 등분산성)과 위배 시 대응책을 설명할 수 있는가?
- [ ] 등분산 시의 합동분산($s_p^2$) 수식과 이분산 시 웰치의 t-검정 수식의 차이를 비교할 수 있는가?
- [ ] 대규모 A/B 테스트에서 단순 p-value 외에 효과 크기(Cohen's d)를 함께 확인해야 하는 이유를 기술할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-086 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/086_t_test.md)
- 연관 토픽: [03-124 대응 표본 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/124_paired_t_test.md), [03-041 가설검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/041_hypothesis_testing.md)
