---
title: "군집분석"
author: "agnusdei1207"
date: "2026-10-25T00:09:44+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 군집분석(Cluster Analysis), 비지도 학습(Unsupervised Learning), 응집도·분리도, K-Means, 계층적 군집
- DBSCAN, GMM, 덴드로그램, 엘보우 기법, 실루엣 계수, 고차원의 저주

## Ⅰ. 군집분석의 개요

- 핵심 요약 : 레이블 없는 데이터에서 유사도 기반으로 군집을 형성하는 비지도 학습 기법.
- 개념 : 레이블(Target Label)이 없는 다차원 데이터에서 개체 간 유사도와 거리를 측정해 비슷한 객체끼리 한 군집으로 묶고 서로 다른 객체는 분리하는 **비지도 학습** (Unsupervised Learning) 기반의 **군집분석** (Cluster Analysis).
- 배경 및 필요성 :
  1. 정답 레이블이 없는 데이터의 구조를 탐색적으로 파악할 필요가 있음.
  2. 고객 세분화, 이상치 탐지, 문서 분류, 공간 데이터 분석 등 데이터 탐색과 전처리 활용이 넓어짐.
- 주요 목적 : 군집 내 응집도(Cohesion)를 높이고 군집 간 분리도(Separation)를 키우는 것.

## Ⅱ. 군집분석의 특징

- 핵심 요약 : 응집도·분리도 원칙 아래 4대 방법론과 데이터 속성별 거리 척도를 조합하는 분석 체계.

1. 응집도 극대화 : 동일 군집의 데이터 포인트 간 거리를 최소화 → 군집의 내부 동질성 확보.
2. 분리도 극대화 : 서로 다른 군집 간 거리를 최대화 → 군집의 경계 명확화.
3. 4대 방법론 : 분할적(Partitioning), 계층적(Hierarchical), 밀도 기반(Density-Based), 모델 기반(Model-Based) 군집화로 데이터 형태에 맞게 선택하며, 밀도 기반의 **DBSCAN** (Density-Based Spatial Clustering of Applications with Noise)과 모델 기반의 **GMM** (Gaussian Mixture Model)이 대표 알고리즘임.
4. 거리 척도의 속성별 선택 :
   - 연속형 수치 데이터는 유클리디안(Euclidean)·맨해튼(Manhattan) 거리와 공분산을 반영한 마할라노비스(Mahalanobis) 거리를 사용.
   - 이진·범주형 데이터는 자카드 유사도(Jaccard)와 해밍 거리(Hamming)를 사용.
   - 텍스트·임베딩 벡터는 코사인 유사도(Cosine Similarity)를 사용.

```text
[ 군집분석 4대 방법론 ]

 분할적 (Partitioning)
   예: K-Means, K-Medoids
 계층적 (Hierarchical)
   예: 병합형, 덴드로그램
 밀도 기반 (Density-Based)
   예: DBSCAN, OPTICS
 모델 기반 (Model-Based)
   예: GMM, 가우시안 혼합 모델
```

## Ⅲ. 군집분석의 구조 (흐름)

- 핵심 요약 : 최적 군집 수(K)를 엘보우 기법으로 후보를 좁히고 실루엣 계수로 교차 확인하는 결정 흐름.

```text
[ 최적 군집 수(K) 결정 흐름 ]

 변수 스케일링 (표준화·정규화)
          ↓
 후보 K 범위 설정
          ↓
 엘보우 기법: WSS 굴곡점 탐색
          ↓
 실루엣 계수로 타당성 교차 확인
          ↓
 최적 K 확정 후 도메인 해석
```

```text
[ 엘보우 기법 (Elbow Method) ]

 WSS (군집 내 제곱합)
  |  \
  |   \____  <- 굴곡점 (후보 K)
  +--------------> K (군집 수)
```

- 군집 타당성 평가 지표 :
  1. **실루엣 계수** (Silhouette Coefficient) : s(i) = (b(i) − a(i)) / max(a(i), b(i)), 범위는 −1에서 1이며 1에 가까울수록 이상적. 통상 0.5 이상이면 비교적 타당한 구조로 봄.
  2. 데이비스-볼딘 지수(Davies-Bouldin Index) : 군집 간 거리 대비 군집 내 분산 비율의 합으로, 값이 작을수록 우수함.
  3. 칼린스키-하라바츠 지수(Calinski-Harabasz Index) : 군집 간 분산과 군집 내 분산의 비율로, 값이 클수록 분리가 명확함.

## Ⅳ. 군집분석 4대 방법론의 비교

- 핵심 요약 : 속도 중심의 분할적, 시각화 중심의 계층적, 임의 형태 대응의 밀도 기반, 확률 해석의 모델 기반으로 구분.

| 분류 | 대표 알고리즘 | 동작 원리 및 거리 측정 | 장점 | 단점 및 한계 |
|---|---|---|---|---|
| 분할적(Partitioning) | K-Means | 사전 군집 수 K를 정하고 중심점(Centroid)과의 거리로 반복 재할당 | 계산이 빠르고 대용량 처리에 적합 | 구형 군집만 탐색, 이상치에 민감, K 사전 지정 필요 |
| 계층적(Hierarchical) | 병합형(Agglomerative) | 개체에서 출발해 단일·완전·평균·와드 연결법 기준으로 순차 병합 | 군집 수 사전 지정 불필요, 덴드로그램 시각화 제공 | 계산 복잡도가 높아 대용량 데이터 적용 곤란 |
| 밀도 기반(Density-Based) | DBSCAN(Density-Based Spatial Clustering of Applications with Noise) | 반경(ε) 내 최소 데이터 수(MinPts) 이상인 고밀도 영역을 연결 | 임의 형태 군집 탐색, 노이즈 자동 분류 | 밀도가 다양하면 성능 저하, 하이퍼파라미터에 민감 |
| 모델 기반(Model-Based) | GMM(Gaussian Mixture Model) | 가우시안 분포의 혼합을 가정하고 EM(Expectation-Maximization) 알고리즘으로 모수 추정 | 소프트 군집화(소속 확률 제공), 타원형 군집 표현 가능 | 국소 최적해 수렴 위험, 초기값 의존성 |

## Ⅴ. 군집분석의 한계와 방안

- 핵심 요약 : K 설정의 주관성, 고차원에서의 거리 왜곡, 이상치와 비구형 형태 처리의 한계를 보완 기법과 전처리로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 군집 수(K) 설정의 주관성 | 엘보우 굴곡점 판정이 모호하고, 실루엣 계수는 구형 구조에 편향되어 비선형 군집 평가가 왜곡됨 | Gap Statistic 기반 갭 검정 적용, DBSCAN·HDBSCAN(Hierarchical Density-Based Spatial Clustering of Applications with Noise) 같은 밀도 기반 방법 병행 | 군집 수 추정치의 안정성 |
| **고차원의 저주** (Curse of Dimensionality) | 차원이 늘면 모든 관측치 간 거리가 균일해져 군집 경계가 붕괴하고 계산량이 급증 | UMAP(Uniform Manifold Approximation and Projection), t-SNE(t-distributed Stochastic Neighbor Embedding), 오토인코더(Autoencoder)로 선행 차원 축소, 코사인 유사도 같은 방향성 척도 활용 | 차원 축소 후 실루엣 계수 |
| 이상치 및 비구형 군집 | K-Means는 이상치에 의해 군집 중심이 편향되고, 도넛형·초승달형 같은 형태를 식별하지 못함 | 중앙값 기반 K-Medoids(PAM, Partitioning Around Medoids), GMM, 스펙트럴 클러스터링(Spectral Clustering) 채택 | 군집별 크기와 이상치 비율 |

## Ⅵ. 군집분석 도입에 대한 기술사적 제언

- 핵심 요약 : 스케일링과 차원 축소 등 전처리의 선행, 군집의 현업 실행 가능성 확보.
- 유클리디안 거리는 변수 단위에 민감하므로, 군집화 전에 표준화(StandardScaler)나 정규화(MinMaxScaler)를 반드시 적용하는 것이 기본 원칙임.
- 고차원 희소 데이터는 거리 자체가 의미를 잃기 쉬우므로, t-SNE·UMAP·오토인코더 기반의 사전 차원 축소를 군집화와 결합하는 설계가 바람직함.
- 수학적으로 분리된 군집이 실제 마케팅과 정책에 쓰이려면 군집별 프로파일링과 특성 해석 워크숍을 현업과 함께 운영해야 함.

## Ⅶ. 결론

- 핵심 요약 : 군집분석은 방법론·척도·평가 지표의 목적에 맞는 조합과 도메인 해석이 성패를 좌우하는 기법.
- 시사점 : 스케일링·차원 축소 같은 전처리와 비즈니스 실행 가능성 검증을 함께 갖출 때 군집 결과가 의사결정에 쓰임.
