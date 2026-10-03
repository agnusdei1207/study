---
title: "추론통계(Inferential Statistics)의 표본 기반 추정과 검정"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 불확실성 하의 과학적 의사결정, 추론통계의 개요

### 가. 추론통계의 정의
- 연구 대상 전체인 모집단(Population)을 전수 조사할 수 없을 때, 모집단으로부터 대표성 있게 추출된 표본(Sample) 데이터를 바탕으로 확률 이론(Probability Theory)을 적용하여 모집단의 모수(평균, 비율, 분산)를 과학적으로 추정(Estimation)하거나 가설을 검정(Hypothesis Testing)하는 통계적 분석 방법.
- 수집된 데이터 자체의 특성을 기술하는 **기술통계(Descriptive Statistics)** 와 대조됨.

---

## Ⅱ. 추론통계의 양대 축: 추정(Estimation)과 가설검정(Hypothesis Testing)

```text
[ 추론통계의 양대 체계 ]
                      [추론통계 (Inferential Statistics)]
                                      |
         +----------------------------+----------------------------+
         |                                                         |
         v                                                         v
   [1. 추정 (Estimation)]                                    [2. 가설검정 (Testing)]
   - 모수가 대략 얼마일 것인가?                              - 가설 주장이 참인가 거짓인가?
   +---> 점추정 (Point): 단일 수치 (mu-hat = X-bar)     +---> 귀무가설 H0 vs 대립가설 H1
   +---> 구간추정 (Interval): 신뢰구간 (95% CI)              +---> p-value vs 유의수준 alpha 판정
```

### 가. 점추정 vs 구간추정의 비교

| 구분 | 개념 및 메커니즘 | 장점 | 트레이드오프 및 한계 |
| :--- | :--- | :--- | :--- |
| **점추정 (Point Estimation)** | 표본 통계량(표본평균 $\bar{X}$, 표본비율 $\hat{p}$)을 모수의 추정치로 단일 수치 제시 | 결과가 간결하고 직관적 | 추정치가 참값과 정확히 일치할 확률은 사실상 0이며, 오차의 크기를 알 수 없음 |
| **구간추정 (Interval Estimation)** | 모수가 포함될 것으로 기대되는 상한과 하한의 구간을 신뢰수준($1-\alpha$)과 함께 제시 | 추정의 신뢰도와 불확실성(오차 한계)을 동시에 표현 | 구간이 너무 넓으면 비즈니스 의사결정의 유용성 저하 |

### 나. 95% 신뢰구간(Confidence Interval)의 정확한 통계적 의미
- "모수가 해당 구간 안에 존재할 확률이 95%이다"는 **틀린 해석** (모수는 고정된 상수임).
- **올바른 해석** : "동일한 방식으로 표본 추출과 신뢰구간 계산을 100번 반복 수행한다면, 그중 95개의 구간이 참 모수를 포함할 것이다."

---

## Ⅲ. 모수적 추론(Parametric) vs 비모수적 추론(Non-parametric)

```text
[ 데이터 조건에 따른 추론 기법 매핑 ]
모집단 분포 가정이 만족되는가? (정규성, n >= 30)
   |-- YES (모수적 추론) : z-검정, 독립/대응 t-검정, ANOVA, Pearson 상관
   +-- NO  (비모수적 추론): Mann-Whitney U, Wilcoxon 부호순위, Kruskal-Wallis, Spearman 상관
```

---

## Ⅳ. 추론통계(Inferential Statistics)의 주요 한계점 및 해결 방안

- 모수적 추정 시 모집단 분포 가정 위반에 따른 검정 통계량 왜곡 :
  - 한계점 : 정규성, 등분산성, 독립성 가정이 충족되지 않은 데이터에 모수적 모델을 무리하게 적용하여 신뢰구간 및 유의확률($p$)이 왜곡되어 잘못된 의사결정 유도.
  - 해결 방안 : 적합도 검정(Goodness-of-fit test) 선행, 가정 위반 시 순위 기반 비모수 검정(Kruskal-Wallis, Wilcoxon)으로 전환, 부트스트랩(Bootstrap) 재표본추출 기법 병행.
- 표본 추출 편향(Sampling Bias)으로 인한 모집단 대표성 상실 :
  - 한계점 : 편의 표본추출(Convenience Sampling)이나 자발적 참여자 편향으로 인해 표본이 모집단을 대표하지 못하여 추론 결과의 외적 타당도(External Validity) 훼손.
  - 해결 방안 : 층화 표본추출(Stratified Sampling) 및 군집 표본추출(Cluster Sampling) 등 확률적 표본 설계 적용, 사후 성향 점수 가중치(Post-stratification Weighting) 보정.
- **p-해킹(p-hacking)** 및 재현성 위기(Replication Crisis) :
  - 한계점 : 유의미한 결과($p < 0.05$)가 나올 때까지 데이터를 변형하거나 가설을 사후 조작(HARKing)하여 통계적 결론의 과학적 재현성 상실.
  - 해결 방안 : 사전 등록제(Pre-registration) 준수, 효과 크기(Effect Size) 및 신뢰구간 동시 보고 의무화, 베이지안 추론(Bayesian Inference: 사후 확률 분포 평가) 병행.

## Ⅴ. 데이터 엔지니어링 및 A/B 테스트 실무 제언

- **표본 크기($n$)** 결정 공식의 사전 적용 : A/B 테스트를 기획할 때 감으로 며칠간 돌리지 말고, 오차 한계($E$), 유의수준($\alpha=0.05$), 표본분산($s^2$)을 대입하여 필요한 최소 표본 수 $n = \left( \frac{Z_{\alpha/2} \cdot s}{E} \right)^2$를 사전에 수학적으로 도출해야 함.
- **재현성 위기(Replication Crisis)** 방어 : 빅데이터 환경에서 무수히 많은 변수 쌍에 대해 가설검정을 무차별 수행하면 1종 오류에 의해 우연한 가짜 상관이 $p < 0.05$로 무더기 검출되므로, FDR(False Discovery Rate - Benjamini-Hochberg) 교정 기법을 파이프라인에 필수 적용할 것을 제언함.
