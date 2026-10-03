---
title: "앙상블 배깅·부스팅"
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

## Ⅰ. 집단 지성을 통한 머신러닝 성능 극대화, 앙상블(Ensemble) 개요

### 가. 앙상블 학습(Ensemble Learning)의 정의
- **앙상블 학습** : 단일 모델(Weak Learner) 하나를 학습시키는 대신, 복수의 약한 학습기들을 결합하여 더 강력하고 일반화 성능이 뛰어난 단일 **강한 학습기** (Strong Learner)를 구축하는 머신러닝 방법론.
- "다수의 의견이 한 명의 전문가보다 낫다"는 콩도르세의 배심원 정리에 기반함.

### 나. 앙상블의 양대 축: 배깅(Bagging) vs 부스팅(Boosting)
- **배깅(Bagging)** : 모델들을 병렬적·독립적 으로 학습시켜 예측값의 분산(Variance)을 축소 (과적합 방지).
- **부스팅(Boosting)** : 모델들을 순차적·의존적 으로 학습시켜 이전 모델의 오차를 보정함으로써 편향(Bias)을 축소 (정확도 극대화).

---

## Ⅱ. 배깅(Bagging)과 부스팅(Boosting)의 핵심 메커니즘 비교

### 가. 학습 방식 및 오차 감소 구조 비교

```text
[ 배깅 (Bagging - 병렬 학습) ]
[원천 데이터] ---> 부트스트랩 샘플링 D1, D2, D3
                  |---> Model 1 (독립 학습) ---\
                  |---> Model 2 (독립 학습) ----> [보팅 / 평균화] ---> 최종 결과 (분산 감소)
                  |---> Model 3 (독립 학습) ---/

[ 부스팅 (Boosting - 순차적 가중치 전파) ]
[원천 데이터] ---> [Model 1] ---> 오차(잔차) 계산 ---> 가중치 부여 D2
                                                       |
                                                       v
                                     [Model 2] ---> 오차 계산 ---> 가중치 부여 D3
                                                                   |
                                                                   v
                                                 [Model 3] ---> 최종 결합 (편향 감소)
```

### 나. 배깅 vs 부스팅 심층 기술 비교

| 비교 항목 | 배깅 (Bagging, Bootstrap Aggregating) | 부스팅 (Boosting) |
| :--- | :--- | :--- |
| 학습 프로세스 | 병렬적(Parallel) 독립 학습 | 순차적(Sequential) 반복 학습 |
| 샘플링 기법 | 복원 추출(Bootstrap Sampling, 약 63.2% 반영) | 이전 모델이 틀린 데이터에 더 높은 가중치 부여 또는 잔차(Residual) 학습 |
| 오차 감소 초점 | **분산(Variance) 감소** $\rightarrow$ 과적합 방지 | **편향(Bias) 감소** $\rightarrow$ 예측 정확도 극대화 |
| 결합 방식 | 단순 투표(Voting, 분류) 또는 산술 평균(회귀) | 각 학습기의 성능에 비례한 가중합(Weighted Sum) 결합 |
| 이상치 민감도 | 이상치에 강건(Robust)함 | 이상치에 민감(틀린 이상치에 가중치가 계속 폭증하여 과적합 위험) |
| 대표 알고리즘 | **Random Forest** / Extra Trees | **AdaBoost** / **Gradient Boosting (GBM)** / **XGBoost** / **LightGBM** / **CatBoost** |

---

## Ⅲ. 현대 트리 부스팅 알고리즘의 진화: XGBoost vs LightGBM vs CatBoost

| 세부 비교 항목 | XGBoost | LightGBM | CatBoost |
| :--- | :--- | :--- | :--- |
| 트리 분할 방식 | 수평 분할 (Level-wise, 레벨 단위 균형 확장) | 수직 분할 (Leaf-wise, 손실 감소 최대 리프 우선) | 대칭 트리 (Symmetric Tree / Oblivious) |
| 학습 속도 및 메모리 | 중간 (정렬 기반 탐색으로 메모리 소모) | 극도로 빠름 (히스토그램 기반, 메모리 절감) | 중간~빠름 |
| 범주형 변수 처리 | 원-핫 인코딩 사전 수행 필요 | 범주형 정수 변환 지원 | 순서형 타깃 통계량(Target Encoding) 내장 |
| 과적합 위험 | 가지치기(Pruning) 및 정규화(L1, L2) 강력 | 소표본 데이터에서 과적합 위험 큼 | 과적합 방지 성능 탁월 |

---

## Ⅳ. 앙상블 기법(배깅·부스팅) 적용 시 주요 한계점 및 해결 방안

- 부스팅의 순차 학습 구조로 인한 훈련 시간 지연 및 이상치 과적합 :
  - 한계점 : Gradient Boosting 계열은 이전 트리의 잔차(Residual)를 순차적으로 학습하므로 병렬 처리가 어렵고 노이즈와 이상치에 과도하게 가중치를 부여하여 과적합 위험.
  - 해결 방안 : 히스토그램 기반 분할 및 GOSS(Gradient-based One-Side Sampling)를 적용한 LightGBM 채택, 조기 종료(Early Stopping) 및 학습률(Shrinkage) 감쇠 튜닝.
- 복잡한 앙상블 모델의 블랙박스화 및 설명 가능성(XAI) 부재 :
  - 한계점 : 수백 개의 약분류기가 결합되어 개별 예측 결과에 대한 비즈니스 인과관계 규명 및 금융/의료 등 규제 산업에서의 컴플라이언스 대응 곤란.
  - 해결 방안 : 샤플리 값 기반 SHAP(SHapley Additive exPlanations) 및 LIME 프레임워크를 연동하여 특성별 기여도 및 로컬/글로벌 설명력 확보.
- 대규모 서빙 환경에서의 모델 복잡도로 인한 추론 레이턴시 증가 :
  - 한계점 : 실시간 추천 및 이상거래 탐지(FDS)에서 수백 개의 트리 모델을 순회 추론 시 P99 응답시간이 수십 밀리초(ms)를 초과하여 SLA 위배.
  - 해결 방안 : Treelite, ONNX Runtime 등 컴파일러 기반 추론 가속기 도입, 트리 앙상블을 단일 신경망이나 룩업 테이블로 증류(Knowledge Distillation)하여 서빙.

---

## Ⅴ. 엔터프라이즈 머신러닝 파이프라인 실무 제언

- 베이스라인 모델 선택 전략 : 정형(Tabular) 테이블 데이터셋에서는 딥러닝보다 LightGBM 또는 CatBoost가 압도적인 학습 속도와 최고의 벤치마크 성능을 나타내므로, 우선적인 앙상블 표준 엔진으로 채택할 것.
- 스태킹(Stacking) 도입 시 데이터 누수(Data Leakage) 차단 : 배깅과 부스팅 모델들의 예측값을 메타 모델(Meta-Learner)에 입력으로 사용하는 스태킹 앙상블을 적용할 때는, 반드시 K-Fold 교차 검증 예측값(Out-of-Fold Predictions)을 피처로 사용하여 과적합을 방지해야 함을 제언함.
