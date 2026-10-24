---
title: "기계학습(Machine Learning)"
author: "agnusdei1207"
date: "2026-10-24T23:15:09+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 기계학습(Machine Learning), 지도학습, 비지도학습, 강화학습, 자기지도학습
- 특징 공학, 경사 하강법, 데이터 드리프트, 개념 드리프트, MLOps, XAI

## Ⅰ. 기계학습(Machine Learning)의 개요

- 핵심 요약 : 규칙을 사람이 코딩하는 대신 데이터에서 패턴을 학습해 성능을 높이는 인공지능의 핵심 분야.
- 개념 : 컴퓨터가 **데이터** (Experience E)로부터 통계적 패턴과 규칙을 스스로 학습하여, 주어진 **작업** (Task T)에 대한 **성능 지표** (Performance P)를 지속 개선하는 **기계학습** (Machine Learning) 분야.
- 배경 및 필요성 : 전통 알고리즘으로 풀기 어려운 비선형·고차원 문제(음성 인식, 컴퓨터 비전, 자연어 처리)가 늘었고, 클라우드 연산력과 빅데이터 인프라가 발전하면서 전 산업의 핵심 엔진으로 자리잡음.
- 주요 목적 : 데이터 기반 예측과 의사결정 자동화, 복잡한 패턴 인식 비용 절감, 환경 변화에 맞춘 지속적 모델 최적화.

## Ⅱ. 기계학습(Machine Learning)의 특징 및 장점

- 핵심 요약 : 규칙 대신 데이터로부터 모델을 얻는 방식이, 명시 규칙이 불가능한 문제를 푸는 능력과 데이터 증가에 따른 성능 개선으로 이어짐.

1. 규칙의 자동 도출 : 입력과 정답의 쌍에서 매핑 함수를 학습 → 사람이 규칙을 일일이 작성하는 비용 감소.
2. 데이터 확장성 : 학습 데이터가 늘수록 **일반화** (Generalization) 성능이 개선 → 데이터 자산이 곧 경쟁력.
3. 지속 적응 : 재학습 파이프라인으로 환경 변화를 반영 → 운영 중 모델 성능 유지.

## Ⅲ. 기계학습(Machine Learning)의 구조 (흐름)

- 핵심 요약 : 데이터 수집에서 배포와 재학습까지 이어지는 순환형 파이프라인과, 규칙 중심에서 데이터 중심으로 바뀐 패러다임.
- **특징 공학** (Feature Engineering) : 원시 데이터에서 수치형 특성을 추출하고 결측치 보정, 원-핫 인코딩, 차원 축소(PCA, Principal Component Analysis)로 모델 입력을 만드는 단계.
- **경사 하강법** (Gradient Descent) : 손실 함수의 기울기를 따라 파라미터를 갱신하는 최적화 방식으로, Adam과 SGD 계열이 대표적.

```text
[ 패러다임 전환 ]

전통 프로그래밍
데이터 + 규칙 → 결과

기계학습
데이터 + 결과 → 규칙(모델)
```

```text
[ 엔드투엔드 머신러닝 파이프라인 ]

데이터 수집 (레이블링 포함)
   ↓
특징 공학 (결측 처리, 인코딩, 차원 축소)
   ↓
모델 학습 (손실 함수 최소화)
   ↓
검증 (K-Fold 교차 검증, 과적합 점검)
   ↓
배포 및 서빙 (API, 모니터링)
   ↓
재학습 트리거 (드리프트 감지)
```

- **MLOps** (Machine Learning Operations) : 모델 레지스트리, 피처 스토어, 성능 모니터링을 결합해 드리프트 발생 시 지속적 재학습(CT, Continuous Training)을 트리거하는 운영 체계.

## Ⅳ. 기계학습(Machine Learning)의 비교

- 핵심 요약 : 정답 레이블의 유무와 학습 목표에 따라 네 가지 패러다임이 나뉘며, 실무에서는 이를 결합한 복합 파이프라인이 주류.

| 학습 패러다임 | 핵심 원리와 데이터 형태 | 대표 알고리즘 | 주요 활용 |
| --- | --- | --- | --- |
| **지도학습** (Supervised Learning) | 레이블이 있는 데이터로 입력과 출력의 매핑 함수 학습 | 선형회귀, 로지스틱 회귀, SVM(Support Vector Machine), Random Forest, CNN(Convolutional Neural Network) | 스팸 필터링, 질병 진단, 객체 인식 |
| **비지도학습** (Unsupervised Learning) | 정답 없이 데이터의 구조와 유사도로 군집화 | K-Means, DBSCAN, PCA, Autoencoder | 고객 세분화, 이상거래 탐지(FDS, Fraud Detection System), 차원 축소 |
| **강화학습** (Reinforcement Learning) | 환경과 상호작용하며 보상을 최대화하는 정책 학습 | Q-Learning, DQN(Deep Q-Network), PPO(Proximal Policy Optimization) | 자율주행, 로봇 제어, 게임 AI, RLHF(Reinforcement Learning from Human Feedback) |
| **자기지도학습** (Self-Supervised Learning) | 데이터 자체에서 의사 레이블을 만들어 사전 학습 | Masked Autoencoder, BERT(Bidirectional Encoder Representations from Transformers), SimCLR | 대규모 파운데이션 모델 사전 학습 |

- 산업 현장에서는 자기지도 사전 학습으로 표현을 얻은 뒤 소량의 지도학습 데이터로 미세조정하는 **복합 파이프라인** 이 주류임.

## Ⅴ. 기계학습(Machine Learning)의 한계와 방안

- 핵심 요약 : 블랙박스 신뢰성, 데이터 드리프트, 데이터 편향을 설명 기법과 지속 모니터링, 공정성 점검으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 블랙박스 특성 | 딥러닝과 앙상블의 추론 과정을 해석하기 어려워 금융·의료 등 고위험 도입 거부 | **XAI** (Explainable Artificial Intelligence, 설명가능 AI) 기법인 SHAP, LIME(Local Interpretable Model-agnostic Explanations) 적용 | 피처별 기여도, 설명 충실도 |
| 데이터 드리프트와 개념 드리프트 | 사용자 행동이나 경제 충격으로 입력 분포와 정답 관계가 변해 배포 초기 성능이 급락 | 입력 분포 거리(KL-Divergence, PSI)를 실시간 추적하고 **자동 재학습 파이프라인** (CT) 가동 | 분포 거리, 성능 저하율 |
| 훈련 데이터의 편향 | 과거의 불평등이 반영된 데이터로 학습해 인종·성별·지역에 따른 불공정 판정 발생 | 공정성 지표(Disparate Impact, Equalized Odds) 모니터링, 리샘플링, **적대적 디바이어싱** (Adversarial Debiasing) 적용 | 집단별 오류율 격차 |

## Ⅵ. 기계학습(Machine Learning)에 대한 기술사적 제언

- 핵심 요약 : 알고리즘 튜닝보다 데이터 품질에 투자하고, MLOps 성숙도와 비즈니스 지표를 함께 설계하는 것이 운영 가치를 키움.
- 데이터 중심 전환 : 코드와 알고리즘 튜닝보다 데이터 일관성, 라벨 노이즈 제거, 합성 데이터 증강을 체계화하는 엔지니어링에 무게를 둬야 함.
- 플랫폼 내재화 : 수작업 스크립트를 벗어나 피처 스토어, CI/CD/CT 자동화, 모델 레지스트리를 표준화한 전사 MLOps 플랫폼을 MLOps 성숙도 단계에 맞춰 단계적으로 구축하는 것이 바람직함.
- 비즈니스 지표 연결 : F1-Score나 RMSE 같은 엔지니어링 지표에 그치지 않고, 비용 절감액과 전환율 같은 KPI(Key Performance Indicator)를 손실 함수 설계에 반영할 필요가 있음.

## Ⅶ. 결론

- 핵심 요약 : 기계학습은 데이터에서 규칙을 얻는 방식으로, 데이터 품질과 운영 체계가 성능을 결정하는 기술.
- 시사점 : 모델 개발보다 데이터와 운영의 지속성이 성과를 좌우하므로, 파이프라인 전 주기를 함께 설계하는 역량이 핵심 경쟁력이 됨.
