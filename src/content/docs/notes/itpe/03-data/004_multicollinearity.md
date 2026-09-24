---
title: "다중공선성(등분산성 포함)"
category: "03-data"
tags:
  - "다중공선성"
  - "등분산성"
  - "이분산성"
  - "VIF"
  - "OLS"
  - "Ridge"
  - "Lasso"
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

<div class="itpe-topic-path" role="img" aria-label="데이터 분석에서 회귀모형 진단 및 다중공선성으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>통계 분석·추론</span>
  <strong>다중공선성(등분산성 포함)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 다중회귀분석에서 독립변수 간의 강한 선형 상관관계로 인해 최소자승법(OLS) 회귀계수의 분산이 비정상적으로 팽창하여 계수 해석과 가설검정이 왜곡되는 통계적 결함 현상 (잔차 분산의 비동일성인 이분산성 포함)
- 메커니즘: 다중회귀 기본 가정 검토 $\rightarrow$ VIF 및 잔차 산점도 진단 $\rightarrow$ 분석 목적(설명 vs 예측) 분기 $\rightarrow$ 변수 결합·정규화(Ridge/Lasso)·WLS 보정 $\rightarrow$ 계수 안정성 교차검증
- 산출물: 상관행렬 및 VIF 진단표 · 잔차 진단도(Residual Plot) · 규제 회귀모형 수식 · 교차검증 평가서

<div class="itpe-flow-map" role="img" aria-label="회귀모형 가정 위배 진단 및 통계적 보정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 다중회귀 기본 가정 점검</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>검토</strong><span>가우스-마르코프 가정(선형성, 비공선성, 등분산성, 오차항 정규성·독립성) 수집</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 다중공선성 및 이분산성 진단</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>측정</strong><span>$VIF = 1/(1-R_j^2)$ 계산, 상태지수(CI), Breusch-Pagan 잔차 검정 수행</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 분석 목적별(해석 vs 예측) 보정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>대응</strong><span>해석 목적: 도메인 기반 변수 결합·WLS / 예측 목적: Ridge/Lasso 규제 및 PCA</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 모형 적합성 및 안정성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>모든 독립변수의 VIF &lt; 10이며 잔차 산점도가 특정 패턴 없이 무작위(등분산) 분포를 보이는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (회귀모형 채택)</strong>
      <span>안정적 회귀계수 확정 $\rightarrow$ 비즈니스 인과관계 해석 및 프로덕션 추론 서빙</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (계수 분산 팽창 / 이분산 왜곡)</strong>
      <span>모형 채택 보류 $\rightarrow$ ElasticNet 규제 도입 및 잔차 로그 변환/강건 표준오차 재적용</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `VIF(Variance Inflation Factor)`: 한 독립변수가 다른 독립변수들과의 다중 상관으로 인해 회귀계수 분산이 부풀려지는 정도를 나타내는 지표 ($VIF \ge 10$ 시 공선성 판정)
- `OLS(Ordinary Least Squares)`: 잔차제곱합(RSS)을 최소화하여 모수를 추정하는 방식으로, 기본 가정 위배 시 최적 선형 불편 추정량(BLUE) 성질 상실
- `등분산성(Homoscedasticity)`: 모든 독립변수 값 수준에서 오차항의 분산이 동일하다는 가정 (위배 시 이분산성 발생)
- `Ridge 회귀 (L2 규제)`: 회귀계수 제곱합에 페널티를 부과하여 공선성이 높은 변수들의 계수 크기를 균등하게 축소시키는 기법
- `Lasso 회귀 (L1 규제)`: 회귀계수 절댓값 합에 페널티를 주어 불필요한 계수를 정확히 0으로 수렴시켜 변수 선택을 수행하는 기법
- `WLS(Weighted Least Squares)`: 잔차의 분산이 큰 관측치에는 작은 가중치를 부여하여 이분산성 문제를 해결하는 추정 기법

</details>

---

## 1교시 예상문제 (10점)

> 다중공선성(등분산성 포함)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

```text
1. 다중공선성 및 등분산성의 정의
- 다중공선성: 독립변수 간 강한 선형관계로 인해 OLS 회귀계수 분산이 팽창하고 유의성 검정이 왜곡되는 현상
- 등분산성: 모든 독립변수 수준에서 오차항의 분산이 일정하다는 가우스-마르코프 기본 가정

2. 핵심 진단 수식 및 판정 기준
- VIF (분산팽창계수): VIF_j = 1 / (1 - R_j^2)
  · VIF ≥ 10 : 다중공선성 존재 확정 (보정 조치 필수)
- Breusch-Pagan 검정: 잔차 제곱을 독립변수로 회귀분석 (p < 0.05 시 이분산성 확인)

3. 분석 목적별 해결 대책
- 설명 목적: 도메인 기반 변수 결합(비율/지수화), WLS, White 강건 표준오차
- 예측 목적: Ridge(L2 계수축소), Lasso(L1 변수선택), PCA(주성분회귀)
```
---

### 핵심 관계

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **등분산성(Homoscedasticity)** | 오차항 분산의 동일성, 이분산성, Breusch-Pagan, WLS, White 강건 표준오차 | Ⅱ·Ⅴ |
| **VIF(분산팽창계수)** | $VIF_j = \frac{1}{1-R_j^2}$, 보조 회귀식의 결정계수, 10 이상 임계치 | Ⅲ 진단체계 |
| **규제 회귀분석** | Ridge(L2 축소), Lasso(L1 희소성), ElasticNet(혼합 패널티), 과적합 방지 | Ⅳ·Ⅵ |

---

## 2~4교시 예상문제 (25점)

> 다중회귀분석에서 가우스-마르코프(Gauss-Markov) 기본 가정 중 다중공선성(Multicollinearity)과 등분산성(Homoscedasticity) 위배 시 발생하는 통계적 문제점, 진단 기법(VIF, Breusch-Pagan 등) 및 분석 목적별(해석 vs 예측) 해결 방안을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **등분산성(Homoscedasticity)** | 오차항 분산의 동일성, 이분산성, Breusch-Pagan, WLS, White 강건 표준오차 | Ⅱ·Ⅴ |
| **VIF(분산팽창계수)** | $VIF_j = \frac{1}{1-R_j^2}$, 보조 회귀식의 결정계수, 10 이상 임계치 | Ⅲ 진단체계 |
| **규제 회귀분석** | Ridge(L2 축소), Lasso(L1 희소성), ElasticNet(혼합 패널티), 과적합 방지 | Ⅳ·Ⅵ |

### Ⅰ. 회귀모형의 안정성을 위협하는 다중공선성 및 등분산성 개요

> 독립변수 간 중복 상관은 계수 분산을 팽창시키고 잔차 분산의 불균일은 검정을 왜곡하므로, 예측과 설명 중 어느 목적을 보존할지 먼저 판정해야 함.

- 정의:
  - **다중공선성**: 독립변수들 간에 강한 선형 상관관계가 존재하여, 개별 변수가 종속변수에 미치는 고유한 영향을 통계적으로 분리해내지 못하는 현상
  - **이분산성**: 오차항의 분산이 독립변수의 수준에 따라 일정하지 않고 변하는 현상
- 목적: 통계적 진단(VIF, 잔차도)을 통해 가우스-마르코프 가정을 검증하고, 모형의 분석 목적(인과 해석 vs 단순 예측)에 부합하는 수학적 보정 수행
- 통계적 영향: $R^2$(결정계수)는 비정상적으로 높으나 각 독립변수의 t-검정 p-value는 유의하지 않게 나타나는 모순 발생

### Ⅱ. 다중공선성과 이분산성이 OLS 추정량에 미치는 영향

> 강한 다중공선성은 계수 분산을 키우고, 이분산성은 통상 OLS 표준오차를 왜곡하므로 두 문제의 영향과 대응을 구분한다.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="mc-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Step 1 -->
    <rect x="15" y="20" width="105" height="100" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="15" y="20" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="67" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">① 독립변수 상관</text>
    <text x="67" y="55" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">$X_i \leftrightarrow X_j$ 강한 선형</text>
    <text x="67" y="70" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">상관계수 $r \ge 0.8$</text>
    <text x="67" y="95" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[정보 중복]</text>

    <!-- Arrow 1->2 -->
    <line x1="120" y1="70" x2="138" y2="70" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#mc-arrow)"/>

    <!-- Step 2 -->
    <rect x="140" y="20" width="105" height="100" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="140" y="20" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="192" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">② 역행렬 불안정</text>
    <text x="192" y="55" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">$\det(X^T X) \approx 0$</text>
    <text x="192" y="70" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">특이행렬 근접</text>
    <text x="192" y="95" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[수학적 불안정]</text>

    <!-- Arrow 2->3 -->
    <line x1="245" y1="70" x2="263" y2="70" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#mc-arrow)"/>

    <!-- Step 3 -->
    <rect x="265" y="20" width="110" height="100" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#ca8a04" stroke-width="1.5"/>
    <rect x="265" y="20" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #fefce8)"/>
    <text x="320" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="#ca8a04">③ 계수 분산 팽창</text>
    <text x="320" y="55" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">$\text{Var}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$</text>
    <text x="320" y="70" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">분산팽창 $VIF \ge 10$</text>
    <text x="320" y="95" text-anchor="middle" font-size="7" font-weight="bold" fill="#ca8a04">[SE 극단적 확대]</text>

    <!-- Arrow 3->4 -->
    <line x1="375" y1="70" x2="393" y2="70" stroke="#dc2626" stroke-width="1.5" marker-end="url(#mc-arrow)"/>

    <!-- Step 4 -->
    <rect x="395" y="20" width="110" height="100" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#dc2626" stroke-width="1.5"/>
    <rect x="395" y="20" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #fef2f2)"/>
    <text x="450" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="#dc2626">④ 가설검정 왜곡</text>
    <text x="450" y="55" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">$t = \hat{\beta}/SE \downarrow$</text>
    <text x="450" y="70" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">p-value 유의성 상실</text>
    <text x="450" y="95" text-anchor="middle" font-size="7" font-weight="bold" fill="#dc2626">[제2종 오류 발생]</text>

    <!-- Bottom Summary Box -->
    <rect x="15" y="135" width="490" height="45" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="260" y="152" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">통계적 모순: 모델 전체의 F-검정 및 결정계수($R^2$)는 90% 이상으로 높으나,</text>
    <text x="260" y="167" text-anchor="middle" font-size="7.5" fill="#dc2626">개별 변수의 t-검정은 전부 기각(p &gt; 0.05)되어 핵심 인과변수를 쓸모없다고 오판하는 치명적 오류 발생</text>
  </svg>
</div>

- **다중공선성의 영향**:
  - 회귀계수의 추정치 자체는 여전히 불편(Unbiased)하지만, 분산이 극도로 커져 표본의 작은 변화에도 계수 부호가 반전되는 극도의 불안정성 노출
  - 표준오차($SE$)가 부풀려져 t-통계량($t = \hat{\beta}/SE$)이 감소하므로 실제 중요한 변수의 p-value가 0.05를 초과하여 기각됨
- **이분산성의 영향**:
  - 회귀계수는 여전히 불편 추정량이나 최소 분산을 갖지 못함(BLUE 상실)
  - 통상적인 OLS 표준오차가 왜곡되어 t-검정 및 F-검정의 신뢰구간이 무효화됨

### Ⅲ. 다중공선성 및 등분산성 핵심 진단 기법

> 단일 수치에만 의존하지 않고 다변량 진단 지표와 시각적 잔차 패턴을 교차 점검함.

| 진단 영역 | 진단 도구 | 판정 메커니즘 | 통계적 판정 기준 |
|---|---|---|---|
| **다중공선성** | **상관행렬 (Correlation)** | 독립변수 쌍(Pair) 간의 단순 선형 상관계수 확인 | $r \ge 0.8$ 이상 시 잠재적 공선성 의심 |
| **다중공선성** | **VIF (분산팽창계수)** | $VIF_j = \frac{1}{1-R_j^2}$ (다른 변수들로 $X_j$를 회귀) | $VIF \ge 10$ (보수적 기준 $VIF \ge 5$) 이상 시 공선성 확정 |
| **다중공선성** | **상태지수 (Condition Index)** | $X$ 행렬의 고유값(Eigenvalue) 최대/최소 비율 ($\sqrt{\lambda_{max}/\lambda_i}$) | $CI \ge 30$ 이상 시 심각한 다중공선성 존재 |
| **등분산성** | **잔차 산점도 (Residual Plot)** | 예측값($\hat{Y}$) 대 잔차($e$)의 분포 패턴 시각화 | 부채꼴·나팔형 패턴 시 이분산성 판정 |
| **등분산성** | **Breusch-Pagan / White 검정** | 잔차 제곱을 독립변수들로 회귀분석하여 분산 변동성 검정 | $p < 0.05$ 시 등분산성 귀무가설 기각 (이분산성 확인) |

### Ⅳ. 분석 목적별(해석 vs 예측) 다중공선성 해결 전략

> 인과관계 설명이 목적인지, 정밀한 수치 예측이 목적인지에 따라 처방이 완전히 달라짐.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="st-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Top Problem Node -->
    <rect x="160" y="15" width="200" height="32" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="#dc2626" stroke-width="1.5"/>
    <text x="260" y="32" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#dc2626">다중공선성 식별 (VIF ≥ 10)</text>
    <text x="260" y="42" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">분석 목적 분기 (Branching)</text>

    <!-- 2 Diagonal Arrows Down -->
    <line x1="210" y1="48" x2="130" y2="75" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#st-arrow)"/>
    <line x1="310" y1="48" x2="390" y2="75" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#st-arrow)"/>
    <text x="145" y="60" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">[인과관계 설명]</text>
    <text x="355" y="60" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">[일반화 예측]</text>

    <!-- Left Box: Explanation Focus -->
    <rect x="25" y="80" width="215" height="100" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.2"/>
    <rect x="25" y="80" width="215" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="132" y="95" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">인과 해석 모형 (도메인 중심)</text>
    <text x="132" y="115" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">· 도메인 기반 파생변수 결합</text>
    <text x="132" y="128" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">키, 몸무게 $\rightarrow$ BMI 지수 통합</text>
    <text x="132" y="145" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">· WLS / White 강건 표준오차</text>
    <text x="132" y="158" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">계수 부호 왜곡 방지 및 통계적 검정 복구</text>
    <text x="132" y="173" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#16a34a">목표: 비즈니스 설명력 100% 보존</text>

    <!-- Right Box: Prediction Focus -->
    <rect x="280" y="80" width="215" height="100" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <rect x="280" y="80" width="215" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="387" y="95" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">정밀 예측 모형 (머신러닝 중심)</text>
    <text x="387" y="115" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">· 정규화 회귀 (Ridge/Lasso/ElasticNet)</text>
    <text x="387" y="128" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">L2 계수 축소 / L1 변수 선택 페널티</text>
    <text x="387" y="145" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">· 차원 축소 (PCA 주성분 회귀)</text>
    <text x="387" y="158" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">직교 기저 변환으로 공선성 원천 제거</text>
    <text x="387" y="173" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">목표: RMSE 최소화 및 과적합 방지</text>
  </svg>
</div>

| 비교 항목 | 해석 목적 (인과관계 규명 모형) | 예측 목적 (머신러닝 추론 모형) |
|---|---|---|
| **최우선 가치** | 회귀계수의 부호 및 크기의 통계적 신뢰성 | 미지의 데이터에 대한 일반화 예측 정확도(RMSE 등) |
| **변수 제거/통합** | 도메인 지식 기반 변수 결합 (예: 키와 몸무게 $\rightarrow$ BMI 지수화) | Stepwise 후진 제거법, 변수 중요도 기반 자동 필터링 |
| **규제 기법 적용** | 규제 적용 지양 (계수가 축소 왜곡되어 경제적 해석 불가) | Ridge(L2), Lasso(L1), ElasticNet(L1+L2 혼합) 적극 적용 |
| **차원 축소 기법** | PCA 적용 불가 (주성분 축은 원 변수의 의미 상실) | PCA(주성분회귀), 요인분석(FA)으로 다중공선성 원천 배제 |
| **등분산 보정** | 변수 로그/Box-Cox 변환, WLS, White 강건 표준오차 적용 | 비모수 트리 앙상블(XGBoost, Random Forest) 모델 전환 |

### Ⅴ. 다중공선성 vs 이분산성 vs 자기상관 비교

> 시계열 및 횡단면 데이터에서 자주 발생하는 회귀 가정 위배의 3대 유형을 대비함.

| 구분 | 다중공선성 (Multicollinearity) | 이분산성 (Heteroscedasticity) | 자기상관 (Autocorrelation) |
|---|---|---|---|
| **발생 위치** | 독립변수 공간 ($X$ 행렬 간 상관) | 오차항 분산 공간 ($Var(\epsilon_i) \neq \sigma^2$) | 오차항 간 시계열/공간 상관 ($Cov(\epsilon_i, \epsilon_j) \neq 0$) |
| **가정 위배** | 독립변수 간 선형 독립 가정 위배 | 오차항의 등분산성 가정 위배 | 오차항의 상호 독립성 가정 위배 |
| **핵심 진단** | VIF $\ge 10$, 상태지수(CI) $\ge 30$ | 잔차 나팔형 산점도, Breusch-Pagan | Durbin-Watson (2에서 이탈 시), ACF/PACF |
| **주요 대책** | 변수 결합, Ridge/Lasso, PCA | Box-Cox 변환, WLS, White Robust SE | 차분(Differencing), 시차변수(Lag) 추가, GLS |

### Ⅵ. 다중공선성·회귀모형 문제점·대응책

> 통계적 지표에 매몰되어 도메인 인과관계를 훼손하는 오류를 방지함.

| 위험 | 대책 | 효과 |
|---|---|---|
| VIF 수치만 보고 핵심 정책 변수 기계적 삭제 | 도메인 인과 다이어그램(DAG) 분석 및 결합 변수(파생변수) 설계 | 핵심 비즈니스 설명력 보존 및 모형 타당성 확보 |
| Ridge/Lasso 적용 시 단위 스케일 불일치 | 모델링 파이프라인 내 표준화(StandardScaler) 전처리 의무화 | 모든 변수에 동등한 가중치의 수학적 패널티 부여 |
| 이분산성 방치로 인한 가설검정 왜곡 | 종속변수 로그 변환 및 Huber-White 강건 표준오차(Robust SE) 병행 | 왜곡된 p-value 교정 및 신뢰구간 정상화 |
| 고차 다항 회귀 시 공선성 급증 ($X, X^2$) | 독립변수의 중심화(Centering: $X - \bar{X}$) 선행 처리 | 다항식 간 불필요한 공선성 제거 및 모형 안정화 |

### Ⅶ. 기술사적 제언: 기계적 변수 삭제를 지양하는 공학적 절충

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 다중공선성은 OLS 추정의 수학적 한계일 뿐 데이터 자체의 죄가 아니다. 예측이 목표라면 VIF가 높아도 전체 모형의 예측력에는 지장이 없으므로 Ridge나 트리 기반 앙상블로 우회하면 그만이다. 그러나 정책 수립이나 비즈니스 인과관계 설명이 목표라면, VIF 숫자에 놀라 핵심 변수를 무턱대고 삭제해서는 안 된다. 변수 삭제는 필연적으로 누락변수 편향(Omitted Variable Bias)을 낳기 때문이다.

> **[나라면 이렇게 쓴다]**
> 2교시형 문제라면 회귀모형 개발 표준 지침으로 **'목적 기반 3단계 의사결정 프레임워크'**를 제시하겠다. 1단계에서 VIF $\ge 10$ 진단 시, 2단계에서 '인과 설명형(도메인 변수 결합 + WLS/White SE)'과 '예측 중심형(ElasticNet + PCA)'으로 경로를 명확히 분기하고, 3단계에서 부트스트랩(Bootstrap) 재표본을 통해 회귀계수 부호의 안정성을 교차 검증하는 엔지니어링 절차를 완결하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: VIF 단일 수치보다 **변수의 비즈니스적 가치, 계수 부호의 안정성, 일반화 검증 오차**를 종합 평가하여 조치 방안 결정.
- **대응 방안**: 설명 모형은 도메인 인과 파생변수로 융합하고, 예측 모형은 ElasticNet 정규화 및 PCA로 수렴.
- **검증 체계**: K-Fold 교차검증과 부트스트랩 1,000회 반복을 통해 회귀계수 부호 반전 여부 및 95% 신뢰구간 수렴성 확인.
- **기대 효과**: 핵심 설명 변수의 부당한 탈락(제2종 오류)을 방지하고, 통계적 설명력과 머신러닝 예측 성능의 최적 균형 달성.

<div class="itpe-flow-map" role="img" aria-label="다중공선성 목적 기반 진단 및 보정 거버넌스 파이프라인">
  <div class="itpe-flow-node">
    <strong>가우스-마르코프 진단</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>진단</strong><span>VIF 및 Breusch-Pagan 측정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>분석 목적별 분기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설명</strong><span>파생변수 결합 / WLS</span></div>
      <div class="itpe-flow-branch"><strong>예측</strong><span>Ridge / Lasso / PCA</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node is-current">
    <strong>부트스트랩 안정성 게이트</strong>
    <div class="itpe-step-detail">
      <strong>검증</strong><span>계수 부호 안정 + VIF &lt; 10</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>최적 회귀모형 배포</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>결과</strong><span>신뢰성 높은 인과 분석 및 예측</span></div>
    </div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제132·135회 확인
- **검증 출처**: [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/), [statsmodels VIF 문서](https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html)

## 연결 토픽

- [로지스틱 회귀분석](./089_logistic_regression.md) · [차원 축소(PCA·MDS)](./069_dimensionality_reduction_pca_mds.md) · [이상치](./010_outlier.md) · [데이터 품질관리](./003_data_quality_management.md)
