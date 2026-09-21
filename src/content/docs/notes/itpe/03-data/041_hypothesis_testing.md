---
author: "Antigravity"
category: "03-data"
date: "2026-09-20T17:00:00+09:00"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
  question_no: "041"
sidebar:
  badge:
    text: "A"
    variant: "note"
  label: "041. 가설검정"
  order: 41
tags:
  - "notes-data"
title: "가설검정 (Hypothesis Testing)"
weight: 41
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 분석·통계</span><span>추론 통계·가설 검정</span><strong>가설검정</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 155" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="155" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Top: Hypothesis Setup -->
  <rect x="15" y="10" width="490" height="26" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" rx="4"/>
  <text x="260" y="27" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">1. 가설 수립: 귀무가설 (H₀: 효과 없음) vs 대립가설 (H₁: 실제 효과 있음)</text>

  <line x1="260" y1="36" x2="260" y2="48" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-hypo)"/>

  <!-- Middle: Test Statistic & Alpha -->
  <rect x="30" y="48" width="460" height="34" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="260" y="64" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-text, #0f172a)">2. 유의수준(α=0.05) 설정 ──▶ 3. 검정통계량(t, z, F, χ²) 산출 및 p-value 계산</text>
  <text x="260" y="76" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">H₀가 참일 때 관측된 표본 차이 이상이 발생할 조건부 확률</text>

  <line x1="260" y1="82" x2="260" y2="94" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-hypo)"/>

  <!-- Bottom: Decision Branch -->
  <rect x="25" y="96" width="225" height="48" fill="var(--color-success-light, #dcfce7)" stroke="var(--color-success, #16a34a)" stroke-width="1.2" rx="4"/>
  <text x="137" y="114" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-success-dark, #15803d)">p-value &lt; α (유의수준 미만)</text>
  <text x="137" y="130" text-anchor="middle" font-size="8.5" fill="var(--color-success-dark, #15803d)">귀무가설 기각 ──▶ 대립가설 채택 (유의미)</text>

  <rect x="270" y="96" width="225" height="48" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2" rx="4"/>
  <text x="382" y="114" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #334155)">p-value ≥ α (유의수준 이상)</text>
  <text x="382" y="130" text-anchor="middle" font-size="8.5" fill="var(--color-text-muted, #64748b)">귀무가설 기각 실패 ──▶ 우연한 변동 가능성</text>

  <defs>
    <marker id="arrow-hypo" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **모집단의 특성에 대한 가설을 수립하고, 표본 데이터를 바탕으로 '관측된 차이가 단순한 표본오차(우연)에 불과하다'는 귀무가설($H_0$)의 발생 확률($p$-value)을 계산하여 기각 여부를 객관적으로 판정하는 추론통계 의사결정 체계**
- 암기: `가-수-통-기-결` = 가설수립($H_0, H_1$) $\to$ 유의수준($\alpha$) 설정 $\to$ 통계량 계산 $\to$ 기각역($p$-value) 비교 $\to$ 최종 결론 판정
- 2대 오류:
  - **제1종 오류($\alpha$, 위양성)**: 참인 귀무가설을 실수로 기각 (유의수준으로 엄격 통제)
  - **제2종 오류($\beta$, 위음성)**: 거짓인 귀무가설을 기각하지 못함 (검정력 $1-\beta$)
  - 상충 관계: $\alpha$를 낮추면 $\beta$가 증가 $\to$ 유일한 해결책은 표본 크기($n$) 확대
- 주의: $p$-value 만능주의 경계 $\to$ 표본 크기($n$)가 극단적으로 커지면 사소한 차이도 $p < 0.001$이 되므로, 효과 크기(Effect Size)와 신뢰구간 병행 검토 필수

## 예상문제

> 데이터 기반 의사결정의 핵심 도구인 통계적 가설검정(Hypothesis Testing)의 개념과 5단계 수행 절차를 기술하고, 제1종 오류($\alpha$)와 제2종 오류($\beta$)의 상충 관계 및 검정력($1-\beta$)을 설명하며, $p$-value의 한계와 실무적 대응 방안을 논하시오. (25점)

## Ⅰ. 불확실성 하에서 과학적 의사결정을 지원하는 가설검정 개요

- 정의: **가설검정(Hypothesis Testing)**은 모집단의 모수에 대한 가설을 세운 후, 표본 추출을 통해 얻은 증거(검정통계량)를 바탕으로 해당 가설의 진위 여부를 확률적으로 검증하여 기각 또는 기각 실패를 결정하는 추론통계 절차
- 목적: 표본의 무작위 변동성에 기인한 착시를 배제하고, 신규 기능 도입(A/B 테스트), 약효 검증, 품질 개선 등의 비즈니스 조치가 실제로 유의미한 효과를 가졌는지 객관적 입증
- 필요성: 단순 평균 비교만으로는 관측된 차이가 '실제 개선'인지 '우연한 표본 추출 오차'인지 구분할 수 없으므로, 수학적으로 오차 발생 확률을 엄격히 통제하는 체계가 필수적임

#### 한줄 요약

- 가설검정은 '우연히 이런 데이터가 나올 확률'을 계산하여, 기준치 이하일 때 우연을 배제하고 인과적 효과를 채택하는 과학적 반증법임

## Ⅱ. 가설검정의 2대 가설 구조 및 방향성

- **귀무가설 ($H_0$, Null Hypothesis)**: "효과가 없다", "차이가 없다", "변화가 없다" (현상 유지, 보수적 입장)
- **대립가설 ($H_1$, Alternative Hypothesis)**: "효과가 있다", "차이가 있다", "개선되었다" (연구자가 입증하려는 주장)

| 검정 방향 | 대립가설 형태 | 기각역(Critical Region) 위치 | 적용 비즈니스 상황 |
|---|---|---|---|
| **양측 검정<br>(Two-tailed)** | $H_1: \mu \neq \mu_0$<br>(차이가 있는지만 검정) | 정규분포의 좌우 양쪽 꼬리에 균등 배분 ($\alpha / 2$) | 신규 UI 적용 후 사용시간의 변동 여부 (증가 또는 감소) |
| **우측 검정<br>(One-tailed)** | $H_1: \mu > \mu_0$<br>(기존보다 큰지 검정) | 분포의 오른쪽 꼬리 한쪽에 집중 ($\alpha$) | 신규 마케팅 캠페인의 구매 전환율 증가 효과 검증 |
| **좌측 검정<br>(One-tailed)** | $H_1: \mu < \mu_0$<br>(기존보다 작은지 검정) | 분포의 왼쪽 꼬리 한쪽에 집중 ($\alpha$) | 시스템 튜닝 후 API 응답 지연시간(Latency) 단축 검증 |

#### 한줄 요약

- 입증하려는 새로운 주장이 대립가설($H_1$)이 되며, 방향성이 특정될 때는 단측검정이 양측검정보다 검정력이 높음

## Ⅲ. 가설검정의 표준 5단계 수행 절차

| 단계 | 수행 작업 | 핵심 판단 및 산출물 |
|---|---|---|
| **1. 가설 수립** | 연구 목적에 따라 $H_0$와 $H_1$의 모수($\mu, p, \sigma^2$) 관계식 정의 | $H_0: \mu_A = \mu_B, \quad H_1: \mu_A > \mu_B$ |
| **2. 유의수준 설정** | 제1종 오류를 범할 최대 허용 확률($\alpha$) 지정 | $\alpha = 0.05$ (신뢰수준 95%) 또는 $\alpha = 0.01$ (신뢰수준 99%) |
| **3. 검정통계량 계산**| 표본 데이터로부터 표준화된 통계량($z, t, F, \chi^2$) 계산 | $t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}$ (t-검정의 경우) |
| **4. p-value 산출** | $H_0$가 참이라는 가정 하에 관측 통계량 이상 극단값이 나올 확률 계산 | $p$-value 계산 (컴퓨터 알고리즘 또는 분포표 활용) |
| **5. 의사결정** | $p \le \alpha$이면 $H_0$ 기각 (유의미), $p > \alpha$이면 $H_0$ 채택 | 통계적 결론 및 비즈니스 조치 보고서 |

#### 한줄 요약

- 가설 설정에서 결론까지의 파이프라인은 데이터를 표준 통계량으로 압축하고 $p$-value를 유의수준과 비교하는 정량적 판정 흐름임

## Ⅳ. 가설검정의 오류 체계: 제1종 오류 vs 제2종 오류

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 120" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="120" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <!-- Header row -->
  <rect x="130" y="10" width="180" height="24" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="220" y="26" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-text, #0f172a)">실제 H₀ 참 (효과 없음)</text>

  <rect x="320" y="10" width="180" height="24" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="410" y="26" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-text, #0f172a)">실제 H₁ 참 (실제 효과 있음)</text>

  <!-- Row 1: H0 Reject -->
  <rect x="15" y="38" width="110" height="34" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="70" y="58" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">H₀ 기각 (채택)</text>

  <rect x="130" y="38" width="180" height="34" fill="var(--color-danger-light, #fee2e2)" stroke="var(--color-danger, #ef4444)" stroke-width="1.2" rx="3"/>
  <text x="220" y="53" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-danger-dark, #b91c1c)">제1종 오류 (α, 위양성)</text>
  <text x="220" y="65" text-anchor="middle" font-size="7.5" fill="var(--color-danger, #ef4444)">효과 없는데 있다고 판정</text>

  <rect x="320" y="38" width="180" height="34" fill="var(--color-success-light, #dcfce7)" stroke="var(--color-success, #16a34a)" stroke-width="1.2" rx="3"/>
  <text x="410" y="53" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-success-dark, #15803d)">올바른 결정: 검정력 (1 - β)</text>
  <text x="410" y="65" text-anchor="middle" font-size="7.5" fill="var(--color-success-dark, #15803d)">실제 효과를 올바르게 탐지</text>

  <!-- Row 2: H0 Accept -->
  <rect x="15" y="76" width="110" height="34" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="70" y="96" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-text, #334155)">H₀ 채택 (기각실패)</text>

  <rect x="130" y="76" width="180" height="34" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="3"/>
  <text x="220" y="91" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-text, #0f172a)">올바른 결정: 신뢰수준 (1 - α)</text>
  <text x="220" y="103" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">효과 없음을 올바르게 수용</text>

  <rect x="320" y="76" width="180" height="34" fill="var(--color-danger-light, #fee2e2)" stroke="var(--color-danger, #ef4444)" stroke-width="1.2" rx="3"/>
  <text x="410" y="91" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-danger-dark, #b91c1c)">제2종 오류 (β, 위음성)</text>
  <text x="410" y="103" text-anchor="middle" font-size="7.5" fill="var(--color-danger, #ef4444)">효과 있는데 놓치는 오류</text>
</svg>
</div>

| 오류 구분 | 정의 및 발생 상황 | 통계적 기호 | 실무적 파급 영향 |
|---|---|---|---|
| **제1종 오류<br>(Type I Error)** | 실제로는 효과가 없는데(귀무가설 참), 우연히 표본 차이가 크게 나와 효과가 있다고 잘못 기각하는 오류 (위양성) | $\alpha$ (유의수준) | 무의미한 기능 배포, 쓸모없는 약품 허가 (조직 자원 낭비 및 오작동 위험) |
| **제2종 오류<br>(Type II Error)** | 실제로 효과가 있는데(대립가설 참), 표본 증거 부족으로 귀무가설을 기각하지 못하고 놓치는 오류 (위음성) | $\beta$ (위음성률) | 혁신적인 신약이나 우수한 UI 개선안을 폐기 (비즈니스 성장 기회 상실) |
| **검정력<br>(Statistical Power)**| 대립가설이 참일 때, 귀무가설을 올바르게 기각하여 실제 존재하는 효과를 정확히 탐지해 낼 확률 | $1 - \beta$ | 통상 산업계 표준으로 **80% ($0.8$) 이상** 확보 권장 |

- **상충 관계 및 해결책**: 유의수준 $\alpha$를 엄격히 낮추면(0.05 $\to$ 0.01) $\beta$가 필연적으로 증가함. $\alpha$와 $\beta$를 동시에 줄여 검정력($1-\beta$)을 높이는 유일한 방법은 **표본 크기($n$)의 확대**임

#### 한줄 요약

- 1종 오류($\alpha$)는 헛다리짚을 위험이고, 2종 오류($\beta$)는 진짜를 놓칠 위험이며, 둘을 동시에 줄이려면 표본 수($n$)를 늘려야 함

## Ⅴ. p-value의 통계적 본질과 오용(p-hacking) 한계

$$p\text{-value} = P(\text{관측된 통계량 또는 그 이상의 극단값} \mid H_0\text{가 참})$$

| 한계 요인 | 원인 및 현상 | 실무적 위험 |
|---|---|---|
| **대규모 표본 왜곡 (Sample Size Bias)** | 표본 수($n$)가 수십만 건 이상이면, 실무적으로 무의미한 0.001% 차이도 $p < 0.0001$로 유의하게 나옴 | 비즈니스 가치가 전혀 없는 미세 변경을 대대적으로 릴리즈하는 오류 |
| **피해킹 (p-hacking)** | 데이터 수집 도중 $p < 0.05$가 나올 때까지 실험을 반복하거나, 유리한 변수만 체리피킹(Cherry-picking) | 위양성(False Positive) 확정 및 재현성 위기(Replication Crisis) |
| **다중 비교 문제 (Multiple Testing)** | 20개의 가설을 동시에 검정하면, 실제로 아무 효과가 없어도 최소 1개 가설이 $p < 0.05$로 나올 확률이 $64\%$에 달함 | 가짜 인사이트 양산 및 A/B 테스트 신뢰도 붕괴 |

#### 한줄 요약

- $p$-value는 데이터 크기에 민감하게 왜곡되므로, 단독으로 판단해서는 안 되며 효과 크기 및 다중 비교 보정이 필수적임

## Ⅵ. 가설검정 실무 실패 사례 및 엔지니어링 대책

| 문제 상황 | 근본 원인 | 실무 엔지니어링 대책 | 개선 효과 |
|---|---|---|---|
| **A/B 테스트 조기 종료로 인한 거짓 성공** | 일일 대시보드를 모니터링하다가 $p < 0.05$가 된 순간 실험을 중단 (Peeking Problem) | **사전 표본 크기 산정(Power Analysis)** 및 **순차 분석(Sequential Testing, SPRT)** 적용 | 다중 관측에 따른 1종 오류 인플레이션 방지 |
| **수십 개 지표 동시 검정 시 우연한 유의성 검출** | 전환율, 체류시간, 클릭수 등 30개 지표를 무차별 검정 | **본페로니 교정(Bonferroni, $\alpha / m$)** 또는 **FDR(False Discovery Rate, Benjamini-Hochberg)** 통제 | 다중 검정의 전체 1종 오류 5% 이내 억제 |
| **p-값은 유의하나 실제 매출 기여 전무** | 표본 100만 명으로 인해 미세한 차이가 $p=0.002$로 도출 | **코헨의 d(Cohen's d)** 등 **효과 크기(Effect Size)** 및 **신뢰구간(Confidence Interval)** 병기 의무화 | 실질적 비즈니스 영향도(Practical Significance) 확인 |
| **검정력 부족으로 혁신 기능 폐기** | 표본 수가 너무 적어($n=50$) 실제 우수한 기능의 $p$-값이 0.12로 나와 기각 실패 | 실험 전 **최소 감지 효과(MDE)** 기반 최소 필요 표본 수($n$) 역산출 후 실험 개시 | 2종 오류 방지 및 검정력 80% 확보 |

#### 한줄 요약

- 순차 분석 도입, 본페로니 다중 검정 보정, 효과 크기 병기(Cohen's d)가 실무 가설검정의 3대 필수 베스트 프랙티스임

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 미국통계학회(ASA)가 2016년 공식 경고했듯이, "단순히 $p < 0.05$를 달성했다는 사실 하나만으로 정책이나 비즈니스 의사결정을 내려서는 안 된다." 빅데이터 환경에서는 표본 수가 수십만~수백만 건에 달하기 때문에, 실무적으로 매출에 아무런 영향이 없는 0.01%의 사소한 차이도 $p < 0.0001$로 유의하게 도출되는 '표본 크기의 함정'이 발생한다. $p$-value는 차이의 존재 유무만 알려줄 뿐, 그 차이가 비즈니스적으로 얼마나 가치 있는지를 알려주지 않는다.
>
> **[나라면 이렇게 쓴다]**
> 실무 엔터프라이즈 A/B 테스트 플랫폼 구축 시 **'통계적 유의성'에서 '실무적 유의성(Practical Significance)'으로 의사결정 기준을 전환**하겠다. 실험 전 최소 감지 효과(MDE)와 사전 검정력 분석(80% 기준)으로 표본 수와 실험 기간을 고정하고, 피킹 문제(Peeking)를 방지하는 순차적 확률비 검정(SPRT)을 적용한다. 또한 최종 리포트에 $p$-value 단독 보고를 금지하고 코헨의 d 효과 크기와 95% 신뢰구간(CI)을 병기하여 비즈니스 손익분기점(ROI)을 초과한 피처만 배포하는 거버넌스를 수립하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: $p$-value 만능주의로 인한 사소한 차이의 과대평가 및 A/B 테스트 조기 종료에 따른 위양성 배포.
- **대응 (개선 방안)**: 최소 감지 효과(MDE) 기반 표본 산정, SPRT 순차 분석 도입 및 효과 크기(Cohen's d)·신뢰구간 병기 의무화.
- **검증 (검증 기준)**: 검정력($1-\beta$) 80% 이상 확보 및 효과 크기 $d \ge 0.2$ 충족 시에만 프로덕션 배포 승인.
- **효과 (실행 효과)**: 무의미한 기능 오배포 100% 차단 및 실제 비즈니스 전환율(CVR) 유의미 개선 검증 신뢰성 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">현행 한계</div>
    <div class="itpe-flow-desc">p-value 만능주의로 인한 사소한 차이 오판 및 위양성 배포</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">개선 방안</div>
    <div class="itpe-flow-desc">SPRT 순차 분석 및 효과크기(Cohen's d)·신뢰구간 병기 표준화</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">검증 기준</div>
    <div class="itpe-flow-desc">검정력 80% 달성 및 실무 효과크기(d ≥ 0.2) 정량 검증 통과</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">실행 효과</div>
    <div class="itpe-flow-desc">착시 릴리즈 100% 방어 및 비즈니스 ROI 입증된 기능만 배포</div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 통계적 가설검정의 정의

- 표본 통계량에 기반하여 "효과가 없다"는 귀무가설($H_0$)의 발생 확률($p$-value)을 계산하고, 이를 유의수준($\alpha$)과 비교하여 **모집단의 특성을 객관적으로 판정하는 추론통계 기법**

### 2. 제1종 오류와 제2종 오류 교차 매트릭스

- **제1종 오류 ($\alpha$, 위양성)**: 실제로는 효과가 없는데(귀무가설 참), 효과가 있다고 잘못 기각 (유의수준 0.05 제약)
- **제2종 오류 ($\beta$, 위음성)**: 실제로는 효과가 있는데(대립가설 참), 효과를 탐지하지 못하고 기각 실패
- **검정력 ($1-\beta$)**: 실제 존재하는 효과를 올바르게 기각하여 탐지할 확률 (산업계 표준 80% 이상)

| 오류 및 척도 | 정의 | 통제 방법 |
|---|---|---|
| 제1종 오류 ($\alpha$) | 참인 귀무가설을 실수로 기각 | 유의수준(통상 0.05)으로 사전 제약 |
| 제2종 오류 ($\beta$) | 거짓인 귀무가설을 기각하지 못함 | 표본 크기($n$) 확대 및 효과 크기 증가 |
| 검정력 ($1 - \beta$) | 실제 효과를 올바르게 탐지할 확률 | 통상 80% ($0.8$) 이상 유지 권장 |

### 3. 차별화 제언

- $p$-hacking 및 표본 과대 왜곡을 극복하기 위해, **본페로니 다중비교 보정**과 **효과 크기(Cohen's d)** 및 **신뢰구간**을 결합한 실무 유의성 평가를 수행함

## 출제 이력과 검증 출처

- 제125회 공식 문제지: 통계적 가설검정 절차와 제1종 오류 및 제2종 오류를 설명하시오
- [American Statistical Association (ASA) Statement on P-Values (2016)](https://amstat.tandfonline.com/doi/full/10.1080/00031305.2016.1154108)
- [Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences](https://www.utstat.toronto.edu/~brunner/oldclass/378f16/readings/CohenPower.pdf)

## 학습 체크

- [ ] 귀무가설($H_0$)과 대립가설($H_1$)의 정의 및 양측/단측 검정의 기각역 차이를 설명할 수 있는가
- [ ] 5단계 가설검정 절차(가설-유의수준-통계량-p값-결정)를 순서대로 제시할 수 있는가
- [ ] 제1종 오류($\alpha$)와 제2종 오류($\beta$)의 상충 관계 및 검정력($1-\beta$)의 개념을 매트릭스로 도식화할 수 있는가
- [ ] $p$-value의 정확한 통계적 정의와 대규모 표본 왜곡 한계를 설명할 수 있는가
- [ ] Ⅶ 결론에서 효과 크기(Effect Size)와 A/B 테스트 순차 분석(Sequential Testing)을 연계할 수 있는가

## 연결 토픽

- [기술통계 vs 추론통계](./036_descriptive_statistics/) · [z-검정](./012_z_test/) · [t-검정](./086_t_test/) · [불편추정량](./011_unbiased_estimator/) · [편향(Bias)](./038_bias/)
