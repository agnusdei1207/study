---
title: "데이터 마이닝"
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

## Ⅰ. 대용량 데이터 속 숨은 지식 발견, 데이터 마이닝의 개요

### 가. 데이터 마이닝(Data Mining)의 정의
- 대규모의 축적된 정형·비정형 데이터베이스로부터 통계학, 인공지능, 머신러닝 알고리즘 및 데이터베이스 관리 기술을 융합하여, 사전에 알려지지 않았으나(Previously Unknown) 비즈니스적으로 유용하고 실행 가능한(Actionable) 패턴, 규칙, 상관관계를 자동으로 발굴하는 지식 발견(KDD, Knowledge Discovery in Databases) 프로세스.

### 나. KDD 5단계 프로세스

```text
[ 지식 발견(KDD) 5단계 프로세스 ]
[원천 데이터] ---> [선택 (Selection)]     : 분석 목적에 맞는 대상 데이터셋 추출
                         |
                         v
                  [전처리 (Preprocessing)] : 결측치 정제, 이상치 제거, 노이즈 필터링
                         |
                         v
                  [변환 (Transformation)]  : 정규화, 차원 축소, 파생변수 생성
                         |
                         v
                  [마이닝 (Data Mining)]   : 분류, 군집, 연관규칙 모델 적용
                         |
                         v
                  [평가 (Evaluation)]     : 패턴 해석, 비즈니스 타당성 검증 -> [지식 도출]
```

---

## Ⅱ. 데이터 마이닝의 핵심 기법 및 알고리즘 분류

### 가. 지도 학습 vs 비지도 학습 마이닝 분류

```text
[ 데이터 마이닝 기법 체계도 ]
+---------------------------------------+---------------------------------------+
|        지도 학습 (Supervised)         |       비지도 학습 (Unsupervised)      |
+---------------------------------------+---------------------------------------+
| [분류 (Classification)]: 이탈예측, 부도  | [군집화 (Clustering)]: 고객 세분화    |
| - Decision Tree, Random Forest, SVM   | - K-Means, DBSCAN, 계층적 군집        |
| [회귀 (Regression)]: 매출 예측, 가격   | [연관규칙 (Association)]: 장바구니분석|
| - 선형회귀, Ridge, Lasso, GBDT        | - Apriori, FP-Growth                  |
+---------------------------------------+---------------------------------------+
```

### 나. 4대 마이닝 태스크 세부 비교

| 마이닝 태스크 | 분석 목적 | 대표 알고리즘 | 실제 비즈니스 적용 사례 |
| :--- | :--- | :--- | :--- |
| **분류 (Classification)** | 데이터를 사전에 정의된 이산적 클래스 레이블 중 하나로 할당 | 의사결정나무, XGBoost, 로지스틱 회귀 | 금융 대출 사기 탐지(FDS), 통신사 고객 해지 예측 |
| **회귀 (Regression)** | 독립변수들을 기반으로 연속적인 수치형 타깃 값을 예측 | 다중선형회귀, 서포트 벡터 회귀(SVR) | 주택 실거래가 예측, 일별 전력 수요량 예측 |
| **군집 (Clustering)** | 타깃 레이블 없이 데이터 간 유사도를 측정하여 자율적으로 그룹화 | K-Means, GMM, 밀도 기반 DBSCAN | 타깃 마케팅을 위한 VIP 고객 군집 세분화 |
| **연관분석 (Association)** | 트랜잭션 내 아이템 간의 동시 발생 패턴($X \rightarrow Y$) 도출 | Apriori, FP-Growth, Eclat | 이커머스 장바구니 교차 판매(Cross-selling) 추천 |

---

## Ⅲ. 산업 표준 데이터 마이닝 방법론: CRISP-DM

### 가. CRISP-DM 6단계 사이클

```text
[ CRISP-DM 순환 프로세스 ]
1. 비즈니스 이해 (Business Understanding) <---> 2. 데이터 이해 (Data Understanding)
                     |                                       |
                     +-------------------+-------------------+
                                         |
                                         v
                             3. 데이터 준비 (Data Preparation)
                                         |
                                         v
                             4. 모델링 (Modeling)
                                         |
                                         v
                             5. 평가 (Evaluation) ---> (성공 시 배포, 미달 시 1단계 재귀)
                                         |
                                         v
                             6. 배포 (Deployment)
```

---

## Ⅳ. 데이터 마이닝의 현대적 진화 및 실무 제언

- **설명 가능한 AI(XAI)의 융합** : 복잡한 딥러닝이나 앙상블 모델이 산출한 마이닝 결과가 '블랙박스'로 남아 현업이 신뢰하지 못하는 문제를 해결하기 위해, SHAP(Shapley Additive Explanations) 및 LIME을 도입하여 개별 예측의 원인 기여도를 투명하게 제공해야 함.
- **DataOps 및 MLOps 파이프라인 통합** : 데이터 마이닝을 일회성 주피터 노트북 분석으로 끝내지 않고, 데이터 인입부터 모델 재학습, 서빙, 성능 모니터링까지 자동화된 End-to-End 파이프라인(Kubeflow, MLflow)을 구축할 것을 제언함.
