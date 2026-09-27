---
sidebar:
  order: 136
  label: "136. 상관관계 (Correlation)"
  badge:
    text: "응용"
    variant: note
author: "OpenAI Codex"
category: "03-data"
date: "2026-09-24T17:48:00+09:00"
tags:
  - "notes-data"
weight: 136
title: "상관관계(Correlation)의 의미와 피어슨·스피어만 계수"
extra:
  model: "GPT-6"
  keyword_grade: "응용"
  question_no: "136"
---

## 지식 로드맵 내 현재 위치

데이터베이스 → 통계·데이터 분석 → 변수 간 연관성 분석

## 30초 인출

- 본질: **상관관계는** 두 변수의 연관성 방향과 정도를 나타내는 통계적 개념
- 메커니즘: Pearson은 원자료의 선형 연관성, Spearman은 순위의 단조 연관성을 측정
- 통찰: 한계: 계수 하나만 제시하면 비선형·이상치·교란과 다중검정 영향을 놓침 → 방안: 산점도·계수 종류·표본·교란 검토를 기록하고 인과 판단은 별도로 검증

<details>
<summary>핵심 용어</summary>

- **상관관계(Correlation)** : 두 변수의 변화가 함께 나타나는 통계적 연관성
- **피어슨 상관계수(Pearson Correlation Coefficient)** : 원자료의 선형 연관성 방향과 강도를 나타내는 계수
- **스피어만 순위상관계수(Spearman Rank Correlation Coefficient)** : 순위 사이의 단조 연관성을 나타내는 계수
- **허위상관(Spurious Correlation)** : 인과가 확립되지 않은 두 변수 사이에 관측된 연관성
- **편상관(Partial Correlation)** : 지정한 변수와의 선형 관계를 제거한 뒤 두 변수 간 선형 연관성을 측정하는 방법

</details>

---

## 2~4교시 예상문제 (25점)

> 상관관계의 개념과 주요 계수를 설명하고, Pearson·Spearman의 선택 기준 및 허위상관의 원인과 해석상 유의점을 논하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 상관관계의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **상관관계** 는 두 변수의 값이 함께 변하는 방향과 정도를 나타내는 통계적 연관성 |
| 목적 | 변수 간 관계를 요약해 분석 가설과 후속 검토의 근거 제공 |

## Ⅱ. 상관관계의 특징

| 특징 | 해석상 의미 |
|---|---|
| 방향과 강도 | 계수의 부호와 절댓값은 정의된 연관성의 방향·정도를 요약 |
| 형태 의존 | 선형·단조·비선형 중 어떤 관계를 측정하는지에 따라 계수 선택 |
| 분포·표본 영향 | 이상치·집단 혼합·선택 편향이 같은 자료의 계수를 바꿀 수 있음 |
| 비인과성 | 함께 변한다는 사실만으로 원인·결과는 정해지지 않음 |

## Ⅲ. 자료 구조 확인·계수 산출·해석 프로세스

```text
두 변수의 표본과 생성 맥락 확인 → 산점도·이상치·집단 구조 확인
                                   ↓
                         관계 형태에 맞는 계수 선택
                                   ↓
                    계수·불확실성 산출 → 교란·다중검정 검토
                                   ↓
                         연관성 보고·별도 인과 검증
```

### Pearson과 Spearman의 하위 산출 흐름

```text
Pearson: (X−X̄),(Y−Ȳ) → 공변동 합 → 각 변수 변동 크기로 표준화 → r
Spearman: X,Y를 각각 순위로 변환 → 순위쌍의 Pearson 상관 → ρₛ
```

Pearson의 표본계수는 $r=\frac{\sum_i(x_i-\bar x)(y_i-\bar y)}{\sqrt{\sum_i(x_i-\bar x)^2\sum_i(y_i-\bar y)^2}}$이며 $-1\le r\le1$이다. 계수의 p값은 효과 크기나 인과성 자체가 아니다.

## Ⅳ. Pearson·Spearman 계수의 비교

| 기준 | Pearson $r$ | Spearman $\rho$ |
|---|---|---|
| 입력 | 원자료 값 | 순위로 변환한 값 |
| 관계 | 선형 연관성 | 단조 연관성 |
| 주요 주의점 | 이상치·비선형 구조에 민감 | 순위 변환으로 크기 정보를 일부 사용하지 않음 |
| 해석 | 공분산을 표준편차로 나눈 무차원 값 | 순위 자료의 Pearson 상관계수 |

편상관은 지정한 공변량과의 선형 관계를 제거한 연관성을 나타내지만 미측정 교란을 없애거나 인과성을 보장하지 않는다.

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 비선형 패턴·집단 혼합을 계수 하나가 숨김 | 산점도와 집단별 관계를 먼저 확인하고 적합한 계수 선택 |
| 이상치·표본 선택으로 연관성이 왜곡 | 원자료·표본 추출과 민감도 분석을 함께 보고 |
| 공통 원인·역인과를 인과 효과로 오인 | 시간순서·교란요인·설계 근거를 검토하고 인과 판단은 별도 분석 |
| 많은 변수 쌍을 반복 검사해 우연한 연관 발견 | 사전 가설·다중검정 보정·독립 자료 검증 |

## Ⅵ. 제언

계수 하나로 비선형·이상치·교란을 놓치기 쉽다. 먼저 산점도와 표본 구성을 보고 Pearson·Spearman을 선택한 뒤, 중요한 관계만 별도 설계로 교란과 인과성을 검증한다.

## 출제 이력과 검증 출처

- National Institute of Standards and Technology (NIST), [Correlation](https://www.nist.gov/glossary-term/21291)
- Penn State Eberly College of Science, [Relationships Between Measurement Variables](https://online.stat.psu.edu/stat100/Lesson05)

## 연결 토픽

- 연관 토픽: [인과관계](./139_causation.md), [독립표본 t-검정](./130_independent_t_test.md), [다중회귀분석](./121_multiple_regression_analysis.md)
