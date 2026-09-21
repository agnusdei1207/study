---
sidebar:
  order: 124
  label: "124. 대응 표본 t-검정 (Paired t-test)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-data"
weight: 124
title: "대응 표본 t-검정(Paired t-test)의 차이값(D) 분석과 사전·사후 효과 검증"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
  question_no: "124"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>대응 표본 t-검정</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Paired Table Left -->
  <rect x="20" y="20" width="280" height="150" rx="8" fill="#3b82f6" fill-opacity="0.08" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="160" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">동일 개체 전후 측정 및 차이값(D) 산출</text>

  <rect x="35" y="55" width="250" height="100" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="45" y="75" font-size="10" font-family="monospace" fill="#64748b">개체ID   튜닝전(X1)  튜닝후(X2)  차이값(D)</text>
  <text x="45" y="95" font-size="10" font-family="monospace" fill="#1e293b">#1       150 ms      110 ms      -40 ms</text>
  <text x="45" y="113" font-size="10" font-family="monospace" fill="#1e293b">#2       320 ms      280 ms      -40 ms</text>
  <text x="45" y="131" font-size="10" font-family="monospace" fill="#1e293b">#3        80 ms       50 ms      -30 ms</text>
  <text x="45" y="147" font-size="10" font-family="monospace" fill="#059669">개체 간 고유 편차(잡음 분산) 완벽 제거!</text>

  <!-- Transform Arrow -->
  <path d="M 305 95 L 340 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow124)"/>

  <!-- Right: One-sample t-test on D -->
  <rect x="345" y="20" width="155" height="150" rx="8" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="422" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">단일 표본 t-검정</text>
  <text x="422" y="68" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">차이값 평균: D̄</text>
  <text x="422" y="88" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">표준오차: sD / √n</text>
  <text x="422" y="112" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">t = (D̄ - 0) / SE</text>
  <text x="422" y="135" text-anchor="middle" font-size="10" fill="#64748b">자유도 df = n - 1</text>
  <text x="422" y="152" text-anchor="middle" font-size="10" fill="#2563eb">검정력(Power) 극대화</text>

  <!-- Bottom Key Diagnostic -->
  <rect x="20" y="185" width="480" height="60" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="208" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">핵심 전제: 원본 변수 X1, X2가 아닌 오직 '차이값(D)'만이 정규분포를 만족해야 함</text>
  <text x="260" y="228" text-anchor="middle" font-size="10" fill="#78350f">정규성 위배 시 비모수 검정인 윌콕슨 부호순위 검정(Wilcoxon Signed-Rank Test)으로 즉시 전환</text>

  <defs>
    <marker id="arrow124" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **동일한 실험 대상(개체)에 대해 어떤 처리(인덱스 튜닝, 캐시 적용 등)를 가하기 전(Pre)과 가한 후(Post)를 1:1로 짝지어 측정한 두 데이터의 차이값($D = X_{\text{post}} - X_{\text{pre}}$)의 평균이 통계적으로 0인지 여부를 검정하는 모수적 가설검정 기법**
- 암기: `동-짝-차-정` (동일 개체, 짝지은 표본, 차이값 D, 차이값의 정규성) / `디-에스-엔-마일` (검정통계량 $t = \bar{D} / (s_D / \sqrt{n})$, 자유도 $df = n-1$) / `윌-콕-슨` (정규성 위배 시 윌콕슨 부호순위 비모수 전환)
- 판단축:
  - **대응 표본 t-검정 vs 독립 표본 t-검정**: 동일 집단의 전후 비교(종속 표본, $df=n-1$) vs 완전히 다른 두 집단 비교(독립 표본, $df=n_1+n_2-2$)
  - **모수 vs 비모수**: 차이값 정규성 충족(대응 t-검정) vs 정규성 위배(윌콕슨 부호순위 검정)
- 주의: $X_{\text{pre}}$와 $X_{\text{post}}$ 각각의 분포가 정규분포를 따를 필요는 전혀 없으며, 오직 두 값의 산술적 차이인 **차이값($D$)만이 정규분포를 만족**하면 됨

## 예상문제

> 대응 표본 t-검정(Paired t-test)과 독립 표본 t-검정(Independent t-test)의 개념, 기본 가정 및 차이점을 비교 설명하고, IT 성능 튜닝 효과 검증 시 차이값($D$)의 정규성 검정 및 비모수 대안을 기술하시오. (25점)

## Ⅰ. 개체 간 편차를 제거하는 대응 표본 t-검정 개요

#### 한줄 요약: 동일 대상의 처리 전·후 차이값($D$)을 단일 변수로 축약하여 개체 고유 분산을 제거하고 효과 유의성을 검정하는 기법

- **배경**:
  - 서로 다른 서버나 사용자를 비교하면 개체 간의 기본 하드웨어 성능이나 숙련도 차이(외생적 잡음 분산)가 너무 커서 시스템 변경의 순수한 효과를 통계적으로 입증하기 어려움
  - 표본 크기가 작은 상황에서도 높은 검정력(Power)을 확보할 수 있는 짝지은 실험 설계(Paired Design)의 필요성 대두
- **정의**: 두 조건에서 짝지어 측정된 종속적인 두 표본에 대해, 각 쌍의 차이값($D = X_2 - X_1$)들의 평균이 0인지를 검정하는 통계 기법
- **수학적 본질**: 두 집단 검정이 아니라, '차이값($D$)'이라는 단 하나의 표본 변수에 대해 $\mu_D = 0$인지를 검정하는 **단일 표본 t-검정(One-sample t-test)**과 동일함

## Ⅱ. 대응 표본 t-검정의 핵심 가설 및 통계량 수식

#### 한줄 요약: 귀무가설 $\mu_D = 0$을 기준으로 차이값 평균의 표준오차 대비 t-통계량을 계산하여 기각 여부 판정

1. **가설 설정**:
   - 귀무가설($H_0$): $\mu_D = 0$ (처리 전후의 모평균 차이가 없다, 효과 없음)
   - 대립가설($H_1$): $\mu_D \neq 0$ (양측 검정, 처리 전후에 유의한 차이가 있다) 또는 $\mu_D < 0$ (단측 검정, 응답시간이 단축되었다)
2. **검정통계량 수식**:

$$t = \frac{\bar{D} - \mu_{D_0}}{s_D / \sqrt{n}} = \frac{\bar{D}}{s_D / \sqrt{n}}$$

  - $D_i = X_{2i} - X_{1i}$: $i$번째 개체의 전후 차이값
  - $\bar{D} = \frac{1}{n}\sum_{i=1}^n D_i$: 표본 차이값들의 산술 평균
  - $s_D = \sqrt{\frac{\sum (D_i - \bar{D})^2}{n - 1}}$: 차이값들의 표본 표준편차
  - $n$: 측정된 짝(Pair)의 총 개수
  - **자유도 (Degrees of Freedom)**: $df = n - 1$

## Ⅲ. 핵심 전제 조건: 차이값($D$)의 정규성 검증

#### 한줄 요약: 원본 데이터의 분포와 상관없이 차이값들의 집합($D$)이 정규분포를 따라야 모수 검정 성립

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="20" y="20" width="230" height="140" rx="6" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="135" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 정규성 만족 (p &gt;= 0.05)</text>
  <text x="135" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Shapiro-Wilk 검정 충족</text>
  <text x="135" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">모수 통계 검정 적용</text>
  <text x="135" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">대응 표본 t-검정 수행</text>
  <text x="135" y="145" text-anchor="middle" font-size="10" fill="#64748b">검정력 최대, 평균 차이 확정</text>

  <!-- Box 2 -->
  <rect x="270" y="20" width="230" height="140" rx="6" fill="#fee2e2" stroke="#ef4444" stroke-width="1.5"/>
  <text x="385" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">2. 정규성 위배 (p &lt; 0.05)</text>
  <text x="385" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">이상치, 심각한 치우침 발생</text>
  <text x="385" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">비모수 통계 검정 전환</text>
  <text x="385" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#b91c1c">윌콕슨 부호순위 검정</text>
  <text x="385" y="145" text-anchor="middle" font-size="10" fill="#64748b">중위수 순위 기반 강건 검정</text>
</svg>
</div>

1. **정규성 검정 절차**:
   - 샤피로-윌크(Shapiro-Wilk) 검정 또는 콜모고로프-스미르노프(K-S) 검정을 통해 차이값 집합 $\{D_1, D_2, \dots, D_n\}$의 정규성 검증
   - $p \ge 0.05$이면 정규성 가정을 만족하므로 대응 표본 t-검정 진행
2. **비모수 대안: 윌콕슨 부호순위 검정 (Wilcoxon Signed-Rank Test)**:
   - 표본 크기가 작고($n < 30$) 차이값의 정규성이 기각된 경우 채택
   - 차이값의 절대 크기에 순위를 매기고 부호(+/-)를 결합하여 중위수(Median)의 차이를 검정함으로써 이상치 왜곡 방지

## Ⅳ. 대응 표본 t-검정 vs 독립 표본 t-검정 비교

#### 한줄 요약: 표본의 종속성 여부, 자유도 산정, 오차 분산 제거 효과에 따른 명확한 구분

| 비교 항목 | 대응 표본 t-검정 (Paired t-test) | 독립 표본 t-검정 (Independent t-test) |
|:---|:---|:---|
| **표본 관계** | **종속 표본 (동일 개체의 짝지은 측정)** | **독립 표본 (완전히 분리된 서로 다른 두 집단)** |
| **실험 설계 예시** | 동일 웹서버 20대의 튜닝 전 vs 후 응답시간 | 신규 알고리즘 그룹(A) vs 기존 알고리즘 그룹(B) |
| **분석 대상** | **차이값 단일 변수 ($D = X_2 - X_1$)** | 두 집단 각각의 변수 ($X_A, X_B$) |
| **자유도 (df)** | **$n - 1$** (쌍의 개수 - 1) | **$n_1 + n_2 - 2$** (등분산 가정 시) |
| **고유 편차 제거** | **개체 간 고유 차이를 완전히 통제** (검정력 극대) | 집단 간 개체 편차가 오차항에 그대로 잔류 |
| **필수 가정** | **차이값($D$)의 정규성** | 두 집단 각각의 정규성 및 **등분산성** |
| **비모수 대안** | 윌콕슨 부호순위 검정 (Signed-Rank) | 맨-휘트니 U 검정 (Mann-Whitney U) |

## Ⅴ. 분석 단계별 파이프라인

#### 한줄 요약: 짝지은 표본 수집 $\rightarrow$ 차이값 $D$ 산출 $\rightarrow$ 정규성 검정 $\rightarrow$ t-통계량 계산 $\rightarrow$ 유의성 판정

1. **표본 수집 (Paired Sampling)**: 동일한 $n$개 개체(쿼리, 서버 등)에 대해 처리 전($X_1$)과 처리 후($X_2$) 데이터를 누락 없이 1:1 매칭 수집
2. **차이값 계산**: 모든 관측치에 대해 $D_i = X_{2i} - X_{1i}$를 계산하여 단일 차이값 벡터 생성
3. **정규성 검정**: 차이값 $D$에 대해 Shapiro-Wilk 검정 수행 ($p \ge 0.05$ 확인)
4. **검정통계량 및 p-value 산출**: t-분포표($df = n-1$)를 기준으로 검정통계량 $t$ 및 유의확률 $p$ 계산
5. **가설 기각 및 결론 도출**: $p < 0.05$이면 귀무가설을 기각하고 "튜닝 효과가 통계적으로 유의미하다"고 확증

## Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 이월 효과(Carryover Effect) 통제, 소표본 이상치 왜곡, A/B 테스트와의 오용 방지

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **쿼리 복잡도 차이로 독립 t-검정 기각 실패** | 쿼리별 기본 실행 시간이 10ms~5000ms로 상이하여 분산이 과대해짐 | 동일 쿼리 1:1 매칭을 통한 **대응 표본 t-검정**으로 전환하여 쿼리 간 편차 제거 |
| **차이값 정규성 위배 ($p < 0.01$)** | 특정 쿼리의 락(Lock) 경합으로 비정상 극단 차이값 발생 | 비모수 검정인 **윌콕슨 부호순위 검정**으로 전환하여 순위 기반 중위수 차이 검정 |
| **시간 흐름에 따른 외생변수 개입 (이월 효과)** | 전후 측정 사이에 전체 시스템 트래픽이나 데이터양이 자연 증가 | 전후 단순 비교 대신 동시간대 트래픽을 분할하는 독립 표본 A/B 테스트를 병행 |

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 엔지니어들이 가장 흔하게 범하는 통계적 실수는 "서버 20대의 튜닝 전 응답시간과 튜닝 후 응답시간을 독립 표본 t-검정으로 돌려버리는 것"이다.
> 서버마다 CPU 부하, 처리하는 API 성격이 천차만별이기 때문에 독립 표본으로 돌리면 분산이 너무 커져서 실제 튜닝 효과가 있어도 $p=0.3$으로 나와서 기각에 실패한다.
> 대응 표본 t-검정은 '개별 개체의 고유 편차'를 수학적으로 완전히 지워버림으로써, **소수의 표본($n=15$)만으로도 순수한 시스템 개선 효과를 입증**할 수 있는 가장 경제적이고 강력한 도구이다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "단순 전후 비교(대응 t-검정)와 A/B 테스트(독립 t-검정)의 적재적소 엔지니어링 전략"을 제시하겠다. 인덱스 최적화나 커널 파라미터 튜닝처럼 정적 환경의 성능 개선은 대응 표본 t-검정으로 잡음을 제거하여 검증하고, 추천 알고리즘이나 UI 개편처럼 사용자 행동 패턴이 개입되는 동적 영역은 이월 효과를 배제하기 위해 독립 표본 A/B 테스트를 채택하는 하이브리드 검증 프레임워크를 수립하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 시스템 튜닝 및 인프라 변경 전후의 성능 개선을 엄밀하게 증명하기 위해 개체 간 편차를 통제하는 대응 표본 t-검정이 적용되어야 함.
- **대응**:
  1. **사전·사후 짝 설계**: 동일 테스트 쿼리셋 또는 동일 서버를 기준으로 전후 성능 데이터를 1:1 페어링 수집.
  2. **정규성 판정 게이트**: 차이값($D$)에 대해 Shapiro-Wilk 검정을 자동 수행하여 정규성 충족 시 대응 t-검정, 위배 시 윌콕슨 검정 자동 분기.
  3. **효과 크기(Effect Size) 병기**: 단순 p-value뿐만 아니라 코헨의 $d$ (Cohen's $d$)를 함께 산출하여 실질적 성능 개선 규모 정량화.
- **검증**: Shapiro-Wilk $p \ge 0.05$, t-통계량 $p < 0.01$, Cohen's $d \ge 0.8$ (큰 효과) 확인.
- **효과**: 적은 테스트 표본으로도 높은 검정력 확보 및 시스템 튜닝의 객관적 신뢰성 보장.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">개체 간 고유 편차로 튜닝 효과 분산 매몰, 독립 검정 오류</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">대응 표본 전후 짝 설계, 차이값(D) 추출 및 t-검정 적용</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">차이값 정규성 검증(p &gt;= 0.05), 유의수준 p &lt; 0.01 달성</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">잡음 분산 원천 제거 및 극소수 표본으로 성능 개선 완벽 입증</div>
  </div>
</div>

---

## 1교시 10점 답안 발췌

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 동일 대상의 처리 전후를 1:1로 매칭하여 측정한 차이값($D = X_2 - X_1$)의 평균이 0인지를 검정하는 종속 표본 모수 통계 기법 |
| **2. 가설 및 통계량** | - 귀무가설: $H_0: \mu_D = 0$ (차이 없음)<br/>- 통계량: $t = \bar{D} / (s_D / \sqrt{n})$, 자유도: $df = n - 1$ |
| **3. 독립 t-검정과의 차이** | 독립 t-검정이 두 독립 집단의 평균($df = n_1+n_2-2$)을 비교하는 반면, 대응 t-검정은 개체 간 고유 편차를 제거하여 검정력을 극대화 |
| **4. 정규성 위배 대책** | 차이값 $D$가 정규성을 만족하지 못할 경우 비모수 검정인 **윌콕슨 부호순위 검정(Wilcoxon Signed-Rank Test)** 적용 |

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제131회 정보관리 2교시: 대응 표본 t-검정(Paired t-test)과 독립 표본 t-검정(Independent t-test)의 개념, 기본 가정 및 차이점
- **검증 출처**:
  - Douglas C. Montgomery, "Design and Analysis of Experiments (10th Edition)", Wiley
  - Sheldon M. Ross, "Introduction to Probability and Statistics for Engineers and Scientists", Academic Press

---

## 학습 체크

- [ ] 대응 표본 t-검정에서 개체 간 고유 분산이 제거되는 수리적 원리를 설명할 수 있는가?
- [ ] 정규성 가정이 적용되는 대상이 $X_1, X_2$ 원본 데이터가 아닌 '차이값($D$)'임을 설명할 수 있는가?
- [ ] 차이값의 정규성이 기각되었을 때 적용하는 비모수 대안인 윌콕슨 부호순위 검정의 원리를 기술할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-086 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/086_t_test.md)
- 연관 토픽: [03-130 독립 표본 t-검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/130_independent_t_test.md), [03-041 가설검정](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/041_hypothesis_testing.md)
