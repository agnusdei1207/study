---
title: "z-검정(z-test)"
category: "03-data"
tags:
  - "z검정"
  - "zTest"
  - "가설검정"
  - "표준정규분포"
  - "AB테스트"
  - "효과크기"
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
extra:
  model: "GPT-6"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 통계 분석에서 가설검정 및 z-검정으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>통계 분석·추론</span>
  <strong>z-검정(z-test)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 모분산($\sigma^2$)을 알고 있거나 대표본 정규근사 조건을 만족할 때, 표본 통계량과 기준 모수 간의 편차를 표준정규분포($\mathcal{N}(0, 1)$)와 대조하여 귀무가설의 기각 여부를 판정하는 모수 가설검정 기법
- 메커니즘: 가설 수립($H_0, H_1$) 및 유의수준($\alpha$) 확정 $\rightarrow$ 전제조건 검증 $\rightarrow$ z-통계량 산출 $\rightarrow$ 표준정규분포 기각역 및 p-값 비교 $\rightarrow$ 효과크기(Cohen's d) 병행 판정
- 산출물: 통계적 가설 명세서 · z-통계량 및 p-value 결과표 · 95% 신뢰구간(CI) 보고서 · A/B 테스트 의사결정서

<div class="itpe-flow-map" role="img" aria-label="z-검정 가설 수립 및 의사결정 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 연구 가설 및 유의수준($\alpha$) 수립</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>가설</strong><span>귀무가설($H_0: \mu = \mu_0$)과 대립가설($H_1$) 설정, $\alpha=0.05$ 확정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: z-검정 전제조건 및 통계량 계산</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>모평균 검정</strong><span>$z = (\bar{X} - \mu_0) / (\sigma / \sqrt{n})$ (모분산 $\sigma^2$ 기지)</span></div>
      <div class="itpe-flow-branch"><strong>모비율 검정</strong><span>$z = (\hat{p} - p_0) / \sqrt{p_0(1-p_0)/n}$ (A/B 테스트 CTR)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 표준정규분포 임계치 대조</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>임계치</strong><span>양측검정 임계치 $|z| > 1.96$ (단측 $z > 1.645$) 및 p-value 산출</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 통계적 유의성 및 효과크기 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>$p < 0.05$로 귀무가설을 기각하며, 최소 검출 가능 효과(MDE)를 충족하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (귀무가설 기각 / 기능 채택)</strong>
      <span>신규 알고리즘/UI 배포 승인 $\rightarrow$ 95% 신뢰구간 및 비즈니스 전환율 개선 반영</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (유의한 차이 없음 / 기각 실패)</strong>
      <span>배포 보류 $\rightarrow$ 기능 롤백 또는 추가 표본 수집 후 재검정(Sequential Testing)</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `z-statistic(z-통계량)`: 표본 통계량과 가설상의 기준 모수 간의 차이를 표준오차($SE$) 단위로 나눈 표준화 점수
- `p-value(유의확률)`: 귀무가설이 참이라는 가정 하에서 관측된 결과 이상의 극단적인 값이 나타날 확률 ($p < \alpha$ 시 기각)
- `기각역(Critical Region)`: 귀무가설을 기각하기로 사전에 결정한 검정 통계량의 영역 (양측 $\alpha=0.05$ 시 $\pm 1.96$ 외곽)
- `MDE(Minimum Detectable Effect)`: 비즈니스적으로 가치 있는 변화로 인정할 수 있는 최소한의 개선 효과 크기
- `Cohen's d(효과크기)`: 두 집단 간 평균 차이를 표준편차로 나눈 표준화된 척도로, 표본 크기($n$)와 무관한 실제 차이의 강도 측정

</details>
---

## 1교시 예상문제 (10점)

> z-검정(z-test)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. z-검정(z-test)의 정의 및 전제조건

- **정의**: 검정 통계량이 표준정규분포($\mathcal{N}(0, 1)$)를 따른다고 가정하고 표본 차이의 통계적 유의성을 검정하는 모수적 기법
- **전제조건**: 표본의 독립 무작위 추출(IID), 모분산($\sigma^2$) 기지 또는 대표본 모비율 정규근사($np \ge 10, n(1-p) \ge 10$) 충족

### 2. 검정 통계량 수식 및 t-검정과의 비교

| 검정 구분 | 검정 통계량 산출 수식 | t-검정 대비 핵심 차이 |
|---|---|---|
| **단일표본 평균** | $z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$ | 모분산 $\sigma^2$ 기지 조건 (미지 시 t-검정 원칙) |
| **독립표본 비율 (A/B)** | $z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\bar{p}(1-\bar{p})(1/n_1 + 1/n_2)}}$ | 대규모 표본(CTR 비교)에서 표준정규분포 근사 적용 |

### 3. 빅데이터 환경 실무 유의점: 'p-값의 함정' 극복

- 표본 크기가 방대하면 비즈니스적으로 무의미한 미세 차이도 $p < 0.05$가 되므로, 반드시 효과크기(Cohen's d)와 최소 검출 가능 효과(MDE), 95% 신뢰구간을 병행 평가해야 함.
---

## 2~4교시 예상문제 (25점)

> 대규모 A/B 테스트 및 시스템 성능 개선 효과 검증을 위한 z-검정(z-test)의 개념, 전제조건, 검정 통계량 산출식(평균 검정, 비율 검정)을 제시하고, t-검정과의 차이점 및 빅데이터 환경에서 p-값(p-value) 해석 시 유의사항을 논하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **모비율 z-검정 (Proportion z-test)** | A/B 테스트 전환율(CVR), 클릭률(CTR) 비교를 위한 표준정규분포 검정 | Ⅲ 검정 유형 |
| **z-검정 vs t-검정 비교** | 모분산 기지/미지, 정규분포 vs t-분포, 자유도 반영 여부 비교 | Ⅳ 모델 비교 |
| **빅데이터 p-value의 함정** | 대규모 표본에서 극미한 차이의 유의성 왜곡, MDE 및 효과크기 병행 대책 | Ⅵ 실무 대책 |

### Ⅰ. 대규모 표본 기반 모수 검정의 표준, z-검정의 개요

> 평균 z-검정은 모분산 기지가 원칙이고 대표본에서 모분산 미지 z 사용은 t의 정규근사임.

- 정의: 검정 통계량이 귀무가설($H_0$) 하에서 표준정규분포($\mathcal{N}(0, 1)$)를 따른다고 가정할 수 있을 때, 표본 통계치와 기준 모수 간의 편차를 표준오차 단위로 표준화하여 유의성을 검정하는 기법
- 필수 전제조건:
  1. 표본이 무작위적이고 상호 독립적으로 추출되어야 함 (IID 가정)
  2. 평균 z-검정은 모집단 분산($\sigma^2$)을 알아야 함. 모분산 미지이면 t-검정이 원칙이며, 대표본 정규근사는 왜도·꼬리·의존성을 함께 확인함
  3. 비율 z-검정은 귀무가설 아래 성공·실패 기대도수가 정규근사를 지지할 만큼 충분($np_0 \ge 10, n(1-p_0) \ge 10$)해야 함
- 활용 목적: 새로운 IT 인프라 도입 전후 응답시간 비교, 이커머스 UI 개선 A/B 테스트 전환율 검증, 제조 공정 불량률 관리

### Ⅱ. 가설검정의 오류 체계 및 판정 기준

> 제1종 오류와 제2종 오류는 역의 관계에 있으므로 유의수준과 검정력의 조화가 필수적임.

<svg viewBox="0 0 520 165" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="가설검정 오류 체계 2x2 매트릭스" role="img">
  <!-- Headers -->
  <text x="130" y="22" font-family="system-ui, sans-serif" font-size="9.5" fill="#8b949e" text-anchor="middle">실제 진실: H0 참 (효과 없음)</text>
  <text x="370" y="22" font-family="system-ui, sans-serif" font-size="9.5" fill="#8b949e" text-anchor="middle">실제 진실: H0 거짓 (효과 있음)</text>

  <!-- Row 1: Fail to Reject -->
  <g transform="translate(15, 32)">
    <!-- H0 True & Retained: Correct -->
    <rect width="240" height="55" rx="4" fill="#21262d" stroke="#3fb950" stroke-width="1"/>
    <text x="12" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#3fb950">옳은 결정 (1 - α)</text>
    <text x="12" y="36" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">H0 채택: 효과 없음을 올바르게 확인</text>
    <text x="12" y="48" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e">신뢰수준: 통상 95% (α = 0.05)</text>

    <!-- H0 False & Retained: Type II Error -->
    <rect x="250" width="240" height="55" rx="4" fill="#21262d" stroke="#f85149" stroke-width="1"/>
    <text x="262" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#f85149">제2종 오류 (Type II Error, β)</text>
    <text x="262" y="36" font-family="system-ui, sans-serif" font-size="8.5" fill="#ff7b72">H0 채택: 실제 효과가 있는데 놓침 (위음성)</text>
    <text x="262" y="48" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e">허용 한계: 통상 β = 0.20 (20%)</text>
  </g>

  <!-- Row 2: Reject H0 -->
  <g transform="translate(15, 95)">
    <!-- H0 True & Rejected: Type I Error -->
    <rect width="240" height="55" rx="4" fill="#21262d" stroke="#f85149" stroke-width="1"/>
    <text x="12" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#f85149">제1종 오류 (Type I Error, α)</text>
    <text x="12" y="36" font-family="system-ui, sans-serif" font-size="8.5" fill="#ff7b72">H0 기각: 효과 없는데 있다고 오판 (위양성)</text>
    <text x="12" y="48" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e">유의수준: 통상 α = 0.05 (5% 통제)</text>

    <!-- H0 False & Rejected: Power -->
    <rect x="250" width="240" height="55" rx="4" fill="#21262d" stroke="#58a6ff" stroke-width="1"/>
    <text x="262" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#58a6ff">검정력 (Statistical Power, 1 - β)</text>
    <text x="262" y="36" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">H0 기각: 실제 존재하는 효과를 올바르게 발견</text>
    <text x="262" y="48" font-family="system-ui, sans-serif" font-size="8" fill="#58a6ff">권장 기준: 80% 이상 (Power $\ge 0.80$)</text>
  </g>
</svg>

- **제1종 오류 ($\alpha$)**: 실제로 효과가 없는데 효과가 있다고 잘못 판단할 확률 (통상 $\alpha = 0.05$ 고정)
- **제2종 오류 ($\beta$)**: 실제로 효과가 존재하는데 차이를 발견하지 못하고 놓칠 확률 (통상 $\beta = 0.20$ 허용)
- **검정력 ($1-\beta$)**: 대립가설이 참일 때 이를 올바르게 기각하여 효과를 발견할 확률 (통상 80% 이상 확보)

### Ⅲ. z-검정의 핵심 유형 및 검정통계량 산출식

> 연속형 평균 비교와 이항 비율 비교에 따라 분모의 표준오차($SE$) 공식이 달라짐.

| 검정 유형 | 귀무가설 ($H_0$) | 검정 통계량 ($z$) 산출 수식 | 표준오차 ($SE$) |
|---|---|---|---|
| **단일표본 평균 검정** | $\mu = \mu_0$ | $z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$ | $SE = \frac{\sigma}{\sqrt{n}}$ |
| **독립 두 표본 평균 검정** | $\mu_1 - \mu_2 = 0$ | $z = \frac{(\bar{X}_1 - \bar{X}_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$ | $SE = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}$ |
| **단일표본 비율 검정** | $p = p_0$ | $z = \frac{\hat{p} - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$ | $SE = \sqrt{\frac{p_0(1-p_0)}{n}}$ |
| **독립 두 표본 비율 검정 (A/B)** | $p_1 - p_2 = 0$ | $z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\bar{p}(1-\bar{p})(\frac{1}{n_1} + \frac{1}{n_2})}}$ | 합동비율: $\bar{p} = \frac{x_1 + x_2}{n_1 + n_2}$ |

### Ⅳ. z-검정 vs t-검정 핵심 비교

> 모분산의 인지 여부와 표본의 크기가 두 검정 기법을 가르는 핵심 기준임.

| 비교 항목 | z-검정 (z-test) | t-검정 (t-test) |
|---|---|---|
| **모분산 ($\sigma^2$)** | **알고 있음 (Known)** 또는 모비율 정규근사 | **모름 (Unknown)** $\rightarrow$ 표본분산($s^2$) 사용 |
| **참조 분포** | 표준정규분포 $\mathcal{N}(0, 1)$ | Student t-분포 ($t(df)$, 자유도 $df = n-1$) |
| **표본 크기 ($n$)** | 주로 대규모 표본 ($n \ge 30$)에 적합 | 소표본($n < 30$)에서도 엄격한 통계적 검정 가능 |
| **분포의 형태** | 일정한 종 모양 (두터운 꼬리 없음) | 자유도에 따라 형태 변화 (소표본일수록 두터운 꼬리) |
| **대표 적용 도메인** | 이커머스 A/B 테스트(대규모 CTR 비교), 공정 관리 | 신약 임상시험(소표본), 추천 모델 성능 개선 검증 |

### Ⅴ. 통계적 가설검정 5단계 수행 절차

> 가설 설정부터 통계량 계산, 임계치 판정 및 효과크기(Effect Size) 보고로 마감함.

<svg viewBox="0 0 520 180" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="표준정규분포 기각역 및 양측검정 임계치 시각화" role="img">
  <!-- Curve Base Axis -->
  <line x1="30" y1="140" x2="490" y2="140" stroke="#8b949e" stroke-width="1.5"/>
  <text x="260" y="155" font-family="system-ui, sans-serif" font-size="9" fill="#8b949e" text-anchor="middle">z = 0 (평균)</text>
  <text x="130" y="155" font-family="system-ui, sans-serif" font-size="9" fill="#f85149" text-anchor="middle">-1.96</text>
  <text x="390" y="155" font-family="system-ui, sans-serif" font-size="9" fill="#f85149" text-anchor="middle">+1.96</text>

  <!-- Left Rejection Area Fill -->
  <path d="M 40 140 Q 90 140, 130 115 L 130 140 Z" fill="rgba(248,81,73,0.3)"/>
  <!-- Right Rejection Area Fill -->
  <path d="M 390 115 Q 430 140, 480 140 L 390 140 Z" fill="rgba(248,81,73,0.3)"/>

  <!-- Bell Curve -->
  <path d="M 40 140 Q 150 140, 260 25 Q 370 140, 480 140" fill="none" stroke="#58a6ff" stroke-width="2"/>

  <!-- Critical Lines -->
  <line x1="130" y1="25" x2="130" y2="140" stroke="#f85149" stroke-width="1.5" stroke-dasharray="3,3"/>
  <line x1="390" y1="25" x2="390" y2="140" stroke="#f85149" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- Area Labels -->
  <text x="260" y="90" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold" fill="#3fb950" text-anchor="middle">채택역 (1 - α = 0.95)</text>
  <text x="85" y="110" font-family="system-ui, sans-serif" font-size="8.5" fill="#f85149" text-anchor="middle">기각역 (α/2=0.025)</text>
  <text x="435" y="110" font-family="system-ui, sans-serif" font-size="8.5" fill="#f85149" text-anchor="middle">기각역 (α/2=0.025)</text>
  <text x="260" y="170" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e" text-anchor="middle">양측 유의수준 α = 0.05 기준: |z| &gt; 1.96 일 때 귀무가설 기각 (p &lt; 0.05)</text>
</svg>

1. **가설 수립**: 검증하고자 하는 차이를 대립가설($H_1$)로 두고, 기존 현상 유지를 귀무가설($H_0$)로 명시
2. **유의수준 및 검정력 설정**: $\alpha=0.05$ 설정 및 필요한 최소 표본 크기($n$)를 사전 산정 (Power Analysis)
3. **전제조건 확인**: 표본 독립성, 이상치 존재 여부, 비율 검정 시 최소 성공/실패 기대도수($\ge 10$) 점검
4. **검정통계량 및 p-value 산출**: 표본 데이터로 $z$-값 계산 후 정규분포 누적확률을 통해 p-value 도출
5. **의사결정 및 효과크기 보고**: $p < 0.05$ 시 귀무가설 기각, 단 Cohen's $d$ 효과크기와 95% 신뢰구간 병기

### Ⅵ. z-검정 실무 위험 관리 및 장애 대책

> 빅데이터 환경의 'p-값의 함정'과 다중 비교 오류를 효과크기와 본페로니 보정으로 차단함.

| 위험 | 대책 | 효과 |
|---|---|---|
| p-값의 함정 (p-Hacking) | 통계적 유의성과 함께 **효과크기(Effect Size, Cohen's d)** 및 MDE 병기 | 수백만 트래픽 하 미세 차이(0.001%)로 인한 무의미한 배포 방지 |
| 다중 검정 거짓양성 (FWE) | 본페로니 보정($\alpha / k$) 또는 FDR(False Discovery Rate) 보정 | 복수 지표 동시 검정 시 발생하는 제1종 오류 급증 차단 |
| 조기 종료 편향 (Peeking) | 유의해지는 순간 멈추지 않고 순차적 검정(Sequential Testing) 적용 | A/B 테스트 중간 확인으로 인한 의사결정 왜곡 원천 방지 |
| 모분산 미지 상태에서 z-검정 오용 | 모분산 미지 시 원칙적으로 t-검정 수행 (대표본 시 t 정규근사 명시) | 소표본에서의 1종 오류 팽창 방지 및 엄밀한 통계 검정 보장 |

### Ⅶ. 기술사적 제언: p-값의 허상을 넘어 비즈니스 실익 중심으로

> "빅데이터 시대에 $p < 0.05$는 데이터 양만 늘리면 무조건 달성할 수 있는 통계적 허상이다. 기술사는 효과크기와 신뢰구간으로 비즈니스 임팩트를 증명해야 한다."

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 데이터가 넘쳐나는 빅데이터 시대에 $p < 0.05$를 얻는 것은 너무나 쉬운 일이다. 통계적으로 유의미하다는 사실이 비즈니스적으로 가치 있다는 뜻은 아니다.
>
> **[나라면 이렇게 쓴다]**
> 전사 A/B 테스트 플랫폼에 자동화된 검정 파이프라인을 구축할 때, z-검정 알고리즘과 함께 최소 검출 가능 효과(MDE: Minimum Detectable Effect) 사전 계산기를 탑재하고, 본페로니 보정과 95% 신뢰구간 시각화를 기본 대시보드에 강제하여 통계적 오판으로 인한 자원 낭비를 방지하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: p-값 단독 판정을 엄격히 금지하고, **통계적 유의성, 효과크기(MDE), 비즈니스 ROI**의 3박자가 일치할 때만 프로덕션 배포를 승인
- **대응 방안**: MDE 기반 사전 표본 설계 $\rightarrow$ 순차 검정(Sequential Testing) 엔진 적용 $\rightarrow$ 95% 신뢰구간 및 Cohen's $d$ 시각화
- **검증 체계**: 검정력 80% 이상 충족 여부 및 다중 지표 검정 시 False Discovery Rate 5% 이내 통제
- **기대 효과**: 조기 중단 편향을 차단하고, 실제 매출과 전환율 개선으로 이어지는 고부가가치 의사결정 체계 확립

<div class="itpe-flow-map" role="img" aria-label="가설검정 거버넌스 고도화 실행 로드맵">
  <div class="itpe-flow-node">
    <strong>1단계: 현행 한계 인식</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-fail"><strong>문제</strong><span>대규모 표본 하 p-값 맹신으로 인한 무의미한 미세 차이(0.001%) 기능 배포</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 아키텍처 개선 방안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>기술 적용</strong><span>MDE 사전 산정 + 순차 검정(Sequential) + Cohen's d 효과크기 및 신뢰구간 병기</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 정량 검증 기준</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>KPI 지표</strong><span>통계적 검정력 80% 이상 확보, False Discovery Rate 5% 이내 유지</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 궁극적 실행 효과</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>가치 창출</strong><span>조기 피킹 편향 원천 차단 및 실질적 비즈니스 전환율·매출 증대 달성</span></div>
    </div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **공식 출제 이력**: 정보관리기술사 제132회 1교시 단답형 (z-검정과 t-검정 비교), 제127회 2교시 논술형 (A/B 테스트 통계 검정과 p-value 해석 시 유의점)
- **표준 및 레퍼런스**: NIST/SEMATECH e-Handbook of Statistical Methods (Tests of Means & Proportions), Evan Miller A/B Testing Mathematics Guide

## 연결 토픽

- [t-검정](./086_t_test.md) · [가설검정](./041_hypothesis_testing.md) · [중심극한정리](./014_central_limit_theorem.md) · [불편추정량](./011_unbiased_estimator.md)
