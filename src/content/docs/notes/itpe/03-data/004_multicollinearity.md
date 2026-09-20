---
title: "다중공선성(등분산성 포함)"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 분석에서 회귀모형 진단 및 다중공선성으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>통계 분석·추론</span>
  <strong>다중공선성(등분산성 포함)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 독립변수 간 강한 선형 상관관계로 인해 회귀계수 추정치의 분산이 팽창하고 개별 변수의 해석력이 훼손되는 현상(다중공선성) 및 잔차 분산의 동일성 위배(이분산성) 문제
- 진단: VIF($1/(1-R_j^2)$), 상태지수(CI), 잔차 산점도, Breusch-Pagan 검정
- 대책: 변수 제거·결합, Ridge/Lasso 규제회귀, PCA 차원축소, WLS(가중최소제곱법), Robust SE

<div class="itpe-flow-map" role="img" aria-label="회귀모형 가정 위배 진단 및 다중공선성 대응 흐름">
  <div class="itpe-flow-node"><strong>다중회귀 기본 가정 검증</strong><small>선형성 · 정규성 · 등분산성 · 비공선성</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>가정 위배 진단</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>다중공선성</strong><span>VIF > 10 · 상태지수 > 30 · 상관계수 > 0.8</span></div>
      <div class="itpe-flow-branch"><strong>이분산성</strong><span>잔차 깔때기 패턴 · Breusch-Pagan 검정 유의</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>통계적 대응 및 정규화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>해석 목적</strong><span>변수 선택(Stepwise) · 파생변수 결합 · WLS</span></div>
      <div class="itpe-flow-branch"><strong>예측 목적</strong><span>Ridge/Lasso 규제 · PCA · 변수 스케일링</span></div>
    </div>
  </div>
</div>

## 예상문제

> 다중회귀분석에서 가우스-마르코프(Gauss-Markov) 기본 가정 중 다중공선성(Multicollinearity)과 등분산성(Homoscedasticity) 위배 시 발생하는 통계적 문제점, 진단 기법(VIF, Breusch-Pagan 등) 및 분석 목적별(해석 vs 예측) 해결 방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **등분산성(Homoscedasticity)** | 오차항의 분산이 모든 독립변수 값에 대해 일정하다는 가정 및 이분산성(Heteroscedasticity) 대책 | Ⅱ 핵심 특징, Ⅴ 비교 |
| **VIF(분산팽창계수)** | $VIF_j = \frac{1}{1-R_j^2}$ 수식 기반 독립변수 간 다중공선성 정량 진단 지표 | Ⅲ 진단체계 |

## Ⅰ. 회귀모형의 안정성을 위협하는 다중공선성 및 등분산성의 개요

> **한줄 요약:** 독립변수 간 중복 상관은 계수의 분산을 팽창시키고, 잔차 분산의 불균일은 유의성 검정을 왜곡함.

- 다중공선성 정의: 회귀모형 내 둘 이상의 독립변수 사이에 강한 선형관계가 존재하여, $(X^TX)^{-1}$ 역행렬 계산이 불안정해지고 OLS 회귀계수 분산이 급증하는 현상
- 등분산성 정의: 오차항 $\epsilon_i$의 분산이 독립변수 $X$의 모든 수준에서 일정하다는 가정($Var(\epsilon_i|X) = \sigma^2$)으로, 위배 시 BLUE(최량선형비편향추정량) 성립 불가
- 공통 영향: 모형 전체의 결정계수($R^2$)와 F검정은 유의하게 나오나, 개별 계수의 t검정 유의확률이 떨어지거나 부호가 역전되어 의사결정을 심각하게 오도함

## Ⅱ. 다중공선성 및 이분산성이 미치는 통계적 영향

> **한줄 요약:** 회귀계수의 표준오차를 부풀려 유의미한 변수를 기각하거나 가설검정을 무효화함.

| 현상 | 통계적 메커니즘 | 실무적 의사결정 위험 |
|---|---|---|
| **회귀계수 분산 팽창** | $Var(\hat{\beta}_j) = \frac{\sigma^2}{\sum(x_{ij}-\bar{x}_j)^2} \times VIF_j$ 급증 | 표준오차 증가로 인해 유의미한 변수가 비유의적으로 판정됨 |
| **계수 부호 및 크기 불안정** | 데이터 표본이 소량 변경되어도 계수 값이 극단적으로 변동 | 상식과 반대되는 회귀계수 부호(음/양 역전) 발생으로 비즈니스 혼란 |
| **F검정과 t검정의 불일치** | 전체 모형의 $F$ 통계량은 유의하나 개별 계수의 $t$ 통계량은 비유의 | 변수 기여도 식별 불가 및 잘못된 변수 제거 발생 |
| **이분산성에 따른 검정 왜곡** | 오차 분산이 비균일하여 OLS 표준오차가 과소 또는 과대 추정 | 신뢰구간이 왜곡되어 귀무가설의 1종/2종 오류 발생 |

## Ⅲ. 다중공선성 및 등분산성 진단 체계

> **한줄 요약:** 상관계수 행렬, VIF, 상태지수로 다중공선성을 잡고, 잔차도와 Breusch-Pagan 검정으로 이분산성을 진단함.

<div class="itpe-pipeline" role="img" aria-label="회귀 진단 파이프라인">
  <div class="itpe-pipeline-node"><strong>상관행렬</strong><small>Pearson $r > 0.8$</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>VIF 진단</strong><small>$VIF > 10$ 판정</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>상태지수(CI)</strong><small>고유값 비율 > 30</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>잔차 진단</strong><small>Breusch-Pagan</small></div>
</div>

| 진단 항목 | 수식 및 진단 기준 | 판정 결과 및 한계 |
|---|---|---|
| **상관계수 행렬** | 변수 간 단순 상관계수 $|r| \ge 0.8$ | 1:1 관계만 탐지 가능, 3개 이상 변수의 결합 공선성 탐지 불가 |
| **공차(Tolerance)** | $Tol_j = 1 - R_j^2 < 0.1$ | 다른 변수들에 의해 해당 변수가 90% 이상 설명됨을 의미 |
| **분산팽창계수(VIF)** | $VIF_j = \frac{1}{1 - R_j^2} \ge 10$ (엄격 시 5) | 계수 분산이 독립일 때 대비 10배 이상 팽창, 다중공선성 확정 |
| **상태지수(Condition Index)** | $CI = \sqrt{\lambda_{max} / \lambda_k} \ge 30$ | 데이터 행렬 $X$의 특이값 불균형으로 인한 수치해석적 불안정 확인 |
| **Breusch-Pagan / White 검정** | 잔차 제곱을 독립변수에 회귀시켜 카이제곱 검정 | $p < 0.05$ 시 등분산성 기각, 이분산성(Heteroscedasticity) 확인 |

## Ⅳ. 분석 목적별(해석 vs 예측) 해결 방안

> **한줄 요약:** 인과 해석이 목적이면 변수 정비와 WLS를, 예측 성능이 목적이면 규제 회귀와 PCA를 적용함.

| 대응 기법 | 동작 원리 및 수식 | 적용 목적 | 실무적 트레이드오프 |
|---|---|---|---|
| **변수 제거 및 선택** | VIF가 높은 변수 중 비즈니스 중요도가 낮은 변수 제거 | 해석 중심 | 중요한 매개변수나 교란요인 누락(Omitted Variable Bias) 위험 |
| **변수 결합(Feature Engineering)** | 강한 상관 변수들을 비율·차이·합성지수로 통합 | 해석 중심 | 개별 변수 자체의 독립적 한계효과 분석은 불가 |
| **Ridge 회귀 (L2)** | $\min \sum(y-X\beta)^2 + \lambda \sum \beta_j^2$ | 예측 중심 | 계수 분산 축소로 예측 안정화, 변수 수는 유지(계수 0 불가) |
| **Lasso 회귀 (L1)** | $\min \sum(y-X\beta)^2 + \lambda \sum |\beta_j|$ | 예측 중심 | 상관 변수 중 임의 하나만 선택하고 나머지를 0으로 만들어 변수 선택 |
| **주성분 회귀(PCR)** | 상관 변수들을 직교하는 주성분(PCA)으로 변환 후 회귀 | 예측 중심 | 완벽한 직교성으로 공선성 원천 제거, 주성분의 비즈니스 해석 난해 |
| **가중최소제곱법(WLS)** | 이분산 오차 분산의 역수($1/\sigma_i^2$)를 가중치로 부여 | 등분산 위배 해결 | 개별 오차 분산 추정 오류 시 모형 성능 저하 가능 |

## Ⅴ. 다중공선성 vs 이분산성 vs 자기상관 비교

> **한줄 요약:** 다중공선성은 독립변수 간의 문제이며, 이분산성과 자기상관은 잔차(오차항)의 문제임.

| 비교 기준 | 다중공선성 (Multicollinearity) | 이분산성 (Heteroscedasticity) | 자기상관 (Autocorrelation) |
|---|---|---|---|
| **발생 위치** | 독립변수 공간 ($X$ 행렬 간 상관) | 오차항 분산 공간 ($Var(\epsilon_i) \neq \sigma^2$) | 오차항 간 시계열/공간 상관 ($Cov(\epsilon_i, \epsilon_j) \neq 0$) |
| **가정 위배** | 독립변수 간 완전 선형 독립 가정 위배 | 오차항의 등분산성 가정 위배 | 오차항의 상호 독립성 가정 위배 |
| **핵심 진단** | VIF, 상태지수(CI), 상관행렬 | 잔차 산점도, Breusch-Pagan, White | Durbin-Watson, 잔차 ACF/PACF |
| **주요 대책** | 변수 정비, Ridge/Lasso, PCA | Box-Cox 변환, WLS, White Robust SE | 차분(Differencing), 시차변수 추가, GLS |

## Ⅵ. 실무 고려사항 및 분석 장애 대책

> **한줄 요약:** VIF 수치에 매몰되어 도메인 핵심 변수를 맹목적으로 삭제하는 오류를 방지해야 함.

- 적용 상황: 금융 신용평가 모형(CSS) 구축 및 공공 정책 효과 분석 회귀모형 개발

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **핵심 정책 변수 오삭제** | VIF > 10 기준을 절대 규칙으로 기계적 적용 | 도메인 인과 다이어그램(DAG) 분석, 결합 변수 생성 | 핵심 설명변수 보존 및 모형 타당성 확보 |
| **Ridge 적용 시 스케일 왜곡** | 변수 간 단위 차이(소득 vs 연령)로 패널티 불균등 부과 | 모델링 파이프라인 내 표준화(StandardScaler) 필수 적용 | 모든 독립변수에 동등한 규제 강도 반영 |
| **이분산 잔차 방치로 검정 오류** | 소득 등 스케일 비례형 데이터의 분산 팽창 미진단 | 로그 변환(Log Transform) 및 Huber-White 강건 표준오차 적용 | 유의확률 검정의 신뢰도 회복 |

## Ⅶ. 결론 및 기술사적 제언

> **한줄 요약:** 통계적 진단 수치는 도구일 뿐이며, 비즈니스 인과관계와 모델링 목적에 맞춘 공학적 절충이 필수적임.

- [핵심 통찰]: 다중공선성은 OLS 추정의 수학적 한계일 뿐 데이터 자체의 죄가 아님. 예측이 목표라면 VIF가 높아도 예측력에 악영향이 적으므로 Ridge나 트리 기반 앙상블로 우회하면 되지만, 인과관계 설명이 목표라면 도메인 지식에 기반한 변수 재설계가 반드시 선행되어야 함.
- 나라면: 회귀모형 개발 표준 지침에 '1단계 탐색적 진단(VIF/잔차도) $\rightarrow$ 2단계 목적 분기(설명모형: 변수통합/WLS, 예측모형: Ridge/ElasticNet) $\rightarrow$ 3단계 교차검증 기반 계수 안정성 평가'를 규정하여 데이터 분석가의 자의적 변수 삭제를 통제하겠음.

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 다중공선성은 독립변수 간 강한 선형관계로 인해 회귀계수 분산이 팽창하여 해석이 불안정해지는 현상이며, 등분산성은 오차항의 분산이 동일해야 한다는 회귀 기본 가정임.

### 2. 핵심 메커니즘 / 체계
```text
[진단] VIF = 1 / (1 - R_j^2) ≥ 10  &  Breusch-Pagan (p < 0.05)
  │
  ├─ 설명 목적: 변수 결합 · Stepwise 선택 · WLS 가중회귀
  └─ 예측 목적: Ridge(L2) · Lasso(L1) · PCA 주성분회귀
```
- VIF와 상태지수로 다중공선성을 잡고, 잔차도로 이분산성을 진단함.

### 3. 차별화 제언
- VIF 수치만으로 핵심 변수를 기계적으로 제거하지 말고, 설명 모형과 예측 모형의 목적을 분리하여 ElasticNet 규제 및 Robust SE를 복합 적용해야 함.

## 출제 이력과 검증 출처

- 출제 이력: 제135회·132회 정보관리기술사 기출, 제124회 KPC 모의고사
- 검증 출처: NIST/SEMATECH e-Handbook of Statistical Methods, 한국통계학회 회귀분석론 표준 교재

## 학습 체크

- [ ] 다중공선성과 등분산성의 개념 및 회귀 가정 위배 시 문제점을 설명할 수 있는가?
- [ ] VIF 수식($1/(1-R_j^2)$)과 판정 임계치(10 이상)를 제시할 수 있는가?
- [ ] 해석 목적과 예측 목적에 따른 다중공선성 해결 방안(Ridge/Lasso/PCA/WLS)을 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [데이터 품질관리](./003_data_quality_management.md)
- 연관 토픽: [로지스틱 회귀분석](./089_logistic_regression.md), [차원 축소(PCA·MDS)](./069_dimensionality_reduction_pca_mds.md), [편향](./038_bias.md)
- 다음 토픽: [군집분석(Clustering)](./005_cluster_analysis.md)
