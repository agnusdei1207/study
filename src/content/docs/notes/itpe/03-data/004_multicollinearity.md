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
date: "2026-09-20T23:50:43+09:00"
author: "Codex"
extra:
  model: "GPT-5.6 Sol"
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
      <strong>판정 질문</strong><span>모든 독립변수의 VIF < 10이며 잔차 산점도가 특정 패턴 없이 무작위(등분산) 분포를 보이는가?</span>
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

## 예상문제

> 다중회귀분석에서 가우스-마르코프(Gauss-Markov) 기본 가정 중 다중공선성(Multicollinearity)과 등분산성(Homoscedasticity) 위배 시 발생하는 통계적 문제점, 진단 기법(VIF, Breusch-Pagan 등) 및 분석 목적별(해석 vs 예측) 해결 방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **등분산성(Homoscedasticity)** | 오차항 분산의 동일성, 이분산성, Breusch-Pagan, WLS, White 강건 표준오차 | Ⅱ·Ⅴ |
| **VIF(분산팽창계수)** | $VIF_j = \frac{1}{1-R_j^2}$, 보조 회귀식의 결정계수, 10 이상 임계치 | Ⅲ 진단체계 |
| **규제 회귀분석** | Ridge(L2 축소), Lasso(L1 희소성), ElasticNet(혼합 패널티), 과적합 방지 | Ⅳ·Ⅵ |

## Ⅰ. 회귀모형의 안정성을 위협하는 다중공선성 및 등분산성 개요

> 독립변수 간 중복 상관은 계수 분산을 팽창시키고 잔차 분산의 불균일은 검정을 왜곡하므로, 예측과 설명 중 어느 목적을 보존할지 먼저 판정해야 함.

- 정의:
  - **다중공선성**: 독립변수들 간에 강한 선형 상관관계가 존재하여, 개별 변수가 종속변수에 미치는 고유한 영향을 통계적으로 분리해내지 못하는 현상
  - **이분산성**: 오차항의 분산이 독립변수의 수준에 따라 일정하지 않고 변하는 현상
- 목적: 통계적 진단(VIF, 잔차도)을 통해 가우스-마르코프 가정을 검증하고, 모형의 분석 목적(인과 해석 vs 단순 예측)에 부합하는 수학적 보정 수행
- 통계적 영향: $R^2$(결정계수)는 비정상적으로 높으나 각 독립변수의 t-검정 p-value는 유의하지 않게 나타나는 모순 발생

## Ⅱ. 다중공선성과 이분산성이 OLS 추정량에 미치는 영향

> 강한 다중공선성은 계수 분산을 키우고, 이분산성은 통상 OLS 표준오차를 왜곡하므로 두 문제의 영향과 대응을 구분한다.

```text
[독립변수 간 다중공선성 발생] ──> [X'X 역행렬 불안정 (Det ≈ 0)] ──> [계수 분산 Var(β) 급증]
                                                                        │
                                                                        ▼
                                                       [t-값 급감 및 p-value 폭증]
                                                       (유의한 변수가 무의미하게 탈락)
```

- **다중공선성의 영향**:
  - 회귀계수의 추정치 자체는 여전히 불편(Unbiased)하지만, 분산이 극도로 커져 표본의 작은 변화에도 계수 부호가 반전되는 극도의 불안정성 노출
  - 표준오차($SE$)가 부풀려져 t-통계량($t = \hat{\beta}/SE$)이 감소하므로 실제 중요한 변수의 p-value가 0.05를 초과하여 기각됨
- **이분산성의 영향**:
  - 회귀계수는 여전히 불편 추정량이나 최소 분산을 갖지 못함(BLUE 상실)
  - 통상적인 OLS 표준오차가 왜곡되어 t-검정 및 F-검정의 신뢰구간이 무효화됨

## Ⅲ. 다중공선성 및 등분산성 핵심 진단 기법

> 단일 수치에만 의존하지 않고 다변량 진단 지표와 시각적 잔차 패턴을 교차 점검함.

| 진단 영역 | 진단 도구 | 판정 메커니즘 | 통계적 판정 기준 |
|---|---|---|---|
| **다중공선성** | **상관행렬 (Correlation)** | 독립변수 쌍(Pair) 간의 단순 선형 상관계수 확인 | $r \ge 0.8$ 이상 시 잠재적 공선성 의심 |
| **다중공선성** | **VIF (분산팽창계수)** | $VIF_j = \frac{1}{1-R_j^2}$ (다른 변수들로 $X_j$를 회귀) | $VIF \ge 10$ (보수적 기준 $VIF \ge 5$) 이상 시 공선성 확정 |
| **다중공선성** | **상태지수 (Condition Index)** | $X$ 행렬의 고유값(Eigenvalue) 최대/최소 비율 ($\sqrt{\lambda_{max}/\lambda_i}$) | $CI \ge 30$ 이상 시 심각한 다중공선성 존재 |
| **등분산성** | **잔차 산점도 (Residual Plot)** | 예측값($\hat{Y}$) 대 잔차($e$)의 분포 패턴 시각화 | 부채꼴·나팔형 패턴 시 이분산성 판정 |
| **등분산성** | **Breusch-Pagan / White 검정** | 잔차 제곱을 독립변수들로 회귀분석하여 분산 변동성 검정 | $p < 0.05$ 시 등분산성 귀무가설 기각 (이분산성 확인) |

## Ⅳ. 분석 목적별(해석 vs 예측) 다중공선성 해결 전략

> 인과관계 설명이 목적인지, 정밀한 수치 예측이 목적인지에 따라 처방이 완전히 달라짐.

| 비교 항목 | 해석 목적 (인과관계 규명 모형) | 예측 목적 (머신러닝 추론 모형) |
|---|---|---|
| **최우선 가치** | 회귀계수의 부호 및 크기의 통계적 신뢰성 | 미지의 데이터에 대한 일반화 예측 정확도(RMSE 등) |
| **변수 제거/통합** | 도메인 지식 기반 변수 결합 (예: 키와 몸무게 $\rightarrow$ BMI 지수화) | Stepwise 후진 제거법, 변수 중요도 기반 자동 필터링 |
| **규제 기법 적용** | 규제 적용 지양 (계수가 축소 왜곡되어 경제적 해석 불가) | Ridge(L2), Lasso(L1), ElasticNet(L1+L2 혼합) 적극 적용 |
| **차원 축소 기법** | PCA 적용 불가 (주성분 축은 원 변수의 의미 상실) | PCA(주성분회귀), 요인분석(FA)으로 다중공선성 원천 배제 |
| **등분산 보정** | 변수 로그/Box-Cox 변환, WLS, White 강건 표준오차 적용 | 비모수 트리 앙상블(XGBoost, Random Forest) 모델 전환 |

## Ⅴ. 다중공선성 vs 이분산성 vs 자기상관 비교

> 시계열 및 횡단면 데이터에서 자주 발생하는 회귀 가정 위배의 3대 유형을 대비함.

| 구분 | 다중공선성 (Multicollinearity) | 이분산성 (Heteroscedasticity) | 자기상관 (Autocorrelation) |
|---|---|---|---|
| **발생 위치** | 독립변수 공간 ($X$ 행렬 간 상관) | 오차항 분산 공간 ($Var(\epsilon_i) \neq \sigma^2$) | 오차항 간 시계열/공간 상관 ($Cov(\epsilon_i, \epsilon_j) \neq 0$) |
| **가정 위배** | 독립변수 간 선형 독립 가정 위배 | 오차항의 등분산성 가정 위배 | 오차항의 상호 독립성 가정 위배 |
| **핵심 진단** | VIF $\ge 10$, 상태지수(CI) $\ge 30$ | 잔차 나팔형 산점도, Breusch-Pagan | Durbin-Watson (2에서 이탈 시), ACF/PACF |
| **주요 대책** | 변수 결합, Ridge/Lasso, PCA | Box-Cox 변환, WLS, White Robust SE | 차분(Differencing), 시차변수(Lag) 추가, GLS |

## Ⅵ. 다중공선성·회귀모형 문제점·대응책

> 통계적 지표에 매몰되어 도메인 인과관계를 훼손하는 오류를 방지함.

| 위험 | 대책 | 효과 |
|---|---|---|
| VIF 수치만 보고 핵심 정책 변수 기계적 삭제 | 도메인 인과 다이어그램(DAG) 분석 및 결합 변수(파생변수) 설계 | 핵심 비즈니스 설명력 보존 및 모형 타당성 확보 |
| Ridge/Lasso 적용 시 단위 스케일 불일치 | 모델링 파이프라인 내 표준화(StandardScaler) 전처리 의무화 | 모든 변수에 동등한 가중치의 수학적 패널티 부여 |
| 이분산성 방치로 인한 가설검정 왜곡 | 종속변수 로그 변환 및 Huber-White 강건 표준오차(Robust SE) 병행 | 왜곡된 p-value 교정 및 신뢰구간 정상화 |
| 고차 다항 회귀 시 공선성 급증 ($X, X^2$) | 독립변수의 중심화(Centering: $X - \bar{X}$) 선행 처리 | 다항식 간 불필요한 공선성 제거 및 모형 안정화 |

## Ⅶ. 기술사적 제언: 기계적 변수 삭제를 지양하는 공학적 절충

> "다중공선성은 OLS 추정의 수학적 한계일 뿐이며, 비즈니스 목적에 부합하는 변수 엔지니어링이 통계적 기법보다 우선한다."

### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 다중공선성은 OLS 추정의 수학적 한계일 뿐 데이터 자체의 죄가 아님. 예측이 목표라면 VIF가 높아도 예측력에 악영향이 적으므로 Ridge나 트리 기반 앙상블로 우회하면 되지만, 인과관계 설명이 목표라면 도메인 지식에 기반한 변수 재설계가 반드시 선행되어야 함.
- `나라면`: 회귀모형 개발 표준 지침에 '1단계 탐색적 진단(VIF/잔차도) $\rightarrow$ 2단계 목적 분기(설명모형: 변수통합/WLS, 예측모형: Ridge/ElasticNet) $\rightarrow$ 3단계 교차검증 기반 계수 안정성 평가'를 규정하여 데이터 분석가의 자의적 변수 삭제를 통제하겠음.

### 실전 답안용 기술사적 제언
- 판정: 단일 VIF 임계치보다 **변수의 비즈니스적 가치, 계수 부호의 안정성, 일반화 검증 오차**를 종합 평가하여 조치 방안을 결정함
- 대안: 설명 모형은 도메인 인과 파생변수로 융합하고, 예측 모형은 ElasticNet 정규화 및 PCA로 수렴시킴
- 검증: 재표본에서 계수 부호·크기 안정성과 교차검증 오차 확인
- 효과: 핵심 변수의 부당한 탈락을 방지하고, 통계적 설명력과 머신러닝 예측 성능의 최적 균형 달성

```text
[현행 한계] ─────────> [개선 방안] ─────────> [검증 기준] ─────────> [실행 효과]
기계적 변수 삭제       분석 목적별 분기 대응  VIF < 10 충족           핵심 설명력 보존
통계적 검정 왜곡       ElasticNet & Robust SE 부트스트랩 부호 검증    모형 일반화 성능 극대화
```

## 1교시 10점 답안 발췌

```text
1. 다중공선성 및 등분산성의 정의
- 다중공선성: 독립변수 간 강한 선형관계로 인해 OLS 회귀계수 분산이 팽창하고 유의성 검정이 왜곡되는 현상
- 등분산성: 모든 독립변수 수준에서 오차항의 분산이 일정하다는 가우스-마르코프 기본 가정

2. 핵심 진단 수식 및 판정 기준
┌─────────────────────────────────────────────────────────────┐
│ VIF (분산팽창계수): VIF_j = 1 / (1 - R_j^2)                  │
│  - VIF ≥ 10 : 다중공선성 존재 확정 (보정 필요)               │
│ Breusch-Pagan 검정: 잔차 제곱을 독립변수로 회귀 (p < 0.05)   │
└─────────────────────────────────────────────────────────────┘

3. 분석 목적별 해결 대책
- 설명 목적: 도메인 기반 변수 결합(비율/지수화), WLS, White 강건 표준오차
- 예측 목적: Ridge(L2 계수축소), Lasso(L1 변수선택), PCA(주성분회귀)
```

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제132·135회 확인
- **검증 출처**: [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/), [statsmodels VIF 문서](https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html)

## 학습 체크

- [ ] [Ⅰ 개요]: 다중공선성과 등분산성의 정의 및 가우스-마르코프 가정 위배 영향을 기술하였는가?
- [ ] [Ⅲ 진단]: VIF 수식($1/(1-R_j^2)$)과 임계치(10), Breusch-Pagan 검정의 원리를 제시하였는가?
- [ ] [Ⅳ 전략]: 설명 목적과 예측 목적에 따른 해결 방안(변수 결합 vs Ridge/Lasso/PCA)을 비교하였는가?
- [ ] [Ⅵ 통제]: 핵심 변수 오삭제 방지 및 스케일링 전처리를 포함한 위험 관리 대책을 기술하였는가?

## 연결 토픽

- [로지스틱 회귀분석](./089_logistic_regression.md) · [차원 축소(PCA·MDS)](./069_dimensionality_reduction_pca_mds.md) · [편향](./038_bias.md) · [데이터 품질관리](./003_data_quality_management.md)
