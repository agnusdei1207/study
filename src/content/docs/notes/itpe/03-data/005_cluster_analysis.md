---
title: "군집분석"
author: "agnusdei1207"
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

## 연관 키워드

- 군집분석(Cluster Analysis), 비지도 학습(Unsupervised Learning), 응집도·분리도, K-Means, 계층적 군집
- DBSCAN, GMM, 덴드로그램, 엘보우 기법, 실루엣 계수, 고차원의 저주

## Ⅰ. 군집분석의 개요

- 핵심 요약 : 레이블 없는 데이터에서 유사도 기반으로 군집을 형성하는 비지도 학습 기법.
- 개념 : 레이블(Target Label)이 없는 다차원 데이터셋에서 개체 간 유사도(Similarity)·거리(Distance)를 측정하여 유사한 속성의 객체를 동일 군집으로 묶고 상이한 객체를 서로 다른 군집으로 분할하는 비지도 학습(Unsupervised Learning) 기법.
- 배경 및 필요성 :
  1. 정답 레이블이 없는 데이터의 탐색적 구조 파악 수요.
  2. 고객 세분화(Customer Segmentation), 이상치 탐지(Anomaly Detection), 문서 분류, 공간 데이터 분석 등 데이터 탐색·전처리 활용의 확대.
- 주요 목적 : 군집 내 응집도(Cohesion) 극대화와 군집 간 분리도(Separation) 극대화의 동시 달성.

## Ⅱ. 군집분석의 특징

- 핵심 요약 : 응집도·분리도 원칙 아래 4대 방법론과 데이터 속성별 거리 척도의 조합.

1. 군집 내 응집도(Cohesion) 극대화 : 동일 군집에 속한 데이터 포인트 간 거리의 최소화.
2. 군집 간 분리도(Separation) 극대화 : 서로 다른 군집 간 거리의 최대화.
3. 4대 방법론 : 분할적(Partitioning), 계층적(Hierarchical), 밀도 기반(Density-Based), 모델 기반(Model-Based) 군집화.
4. 거리 척도의 데이터 속성별 선택 :
   - 연속형 수치 데이터 : 유클리디안 거리(Euclidean), 맨해튼 거리(Manhattan), 마할라노비스 거리(공분산 반영).
   - 이진·범주형 데이터 : 자카드 유사도(Jaccard), 해밍 거리(Hamming).
   - 텍스트·임베딩 벡터 : 코사인 유사도(Cosine Similarity).

```text
[ 군집분석 4대 방법론 ]
 ├─ 분할적(Partitioning) : K-Means, K-Medoids
 ├─ 계층적(Hierarchical) : 병합형, 덴드로그램
 ├─ 밀도 기반(Density)   : DBSCAN, OPTICS
 └─ 모델 기반(Model)     : GMM (EM 알고리즘)
```

## Ⅲ. 군집분석의 구조 (흐름)

- 핵심 요약 : 4대 방법론의 분류 체계와 엘보우·실루엣 기반 최적 군집 수(K) 결정 흐름.

```text
[ 엘보우 기법 (Elbow Method) ]
 WSS (군집 내 제곱합)
  | \
  |  \
  |   \___  <-- 엘보우 포인트 (최적 K)
  +---------> K (군집 수)

[ 실루엣 분석 (Silhouette Analysis) ]
 s(i) = (b(i) - a(i)) / max(a(i), b(i))
 - a(i) : 동일 군집 내 평균 거리
 - b(i) : 가장 가까운 타 군집과의 평균 거리
 - 범위 : -1 ~ +1 (1에 가까울수록 이상적)
```

- 군집 타당성 평가 지표 :
  1. 실루엣 계수(Silhouette Coefficient) : 군집 내 응집도 a(i)와 최근접 타 군집 분리도 b(i)의 정규화 평가, 0.5 이상이면 타당한 구조로 판단.
  2. 데이비스-볼딘 지수(Davies-Bouldin Index) : 군집 간 거리 대비 군집 내 분산 비율의 합산, 값이 작을수록 우수한 군집화.
  3. 칼린스키-하라바츠 지수(Calinski-Harabasz Index) : 군집 간 분산과 군집 내 분산의 비율, 값이 클수록 명확한 분리.

## Ⅳ. 군집분석 4대 방법론의 비교

- 핵심 요약 : 속도 중심의 분할적, 시각화 중심의 계층적, 임의 형태 대응의 밀도 기반, 확률 해석의 모델 기반.

| 분류 | 대표 알고리즘 | 동작 원리 및 거리 측정 | 장점 | 단점 및 한계 |
|---|---|---|---|---|
| 분할적(Partitioning) | K-Means | 사전 군집 수 K 설정 후 중심점(Centroid)과의 거리 기반 반복 재할당 | 계산 복잡도 O(tKn)의 속도, 대용량 처리 적합 | 구형(Spherical) 군집만 탐색, 이상치 민감, K 사전 지정 필요 |
| 계층적(Hierarchical) | Agglomerative(병합형) | 각 개체에서 시작해 거리(단일, 완전, 평균, 와드 연결법)에 따라 순차 병합 | 군집 수 사전 지정 불필요, 덴드로그램 시각화 제공 | 계산 복잡도 O(n³) 또는 O(n²)로 대용량 데이터 적용 곤란 |
| 밀도 기반(Density-Based) | DBSCAN(Density-Based Spatial Clustering of Applications with Noise) | 반경(ε) 내 최소 데이터 수(MinPts) 이상의 고밀도 영역 연결 | 비선형·기하학적 임의 형태 군집 탐색, 노이즈(이상치) 자동 분류 | 데이터 밀도가 다양한 경우 성능 저하, 하이퍼파라미터 민감 |
| 모델 기반(Model-Based) | GMM(Gaussian Mixture Model) | 여러 가우시안 확률 분포의 혼합 가정하에 EM(Expectation-Maximization) 알고리즘으로 모수 추정 | 소프트 군집화(소속 확률 제공), 타원형 군집 표현 가능 | 국소 최적해(Local Minimum) 수렴 위험, 초기값 의존성 |

## Ⅴ. 군집분석의 장점과 한계

- 핵심 요약 : 탐색적 분석·세분화의 장점과 K 설정 주관성·차원의 저주·비구형 형태 처리의 한계.

- 장점
  1. 레이블 없는 데이터의 탐색적 분석 및 전처리 수단.
  2. 고객 세분화·이상치 탐지 등 폭넓은 실무 활용.
  3. 방법론·거리 척도의 다양한 선택지.

- 한계점 1 : 사전 군집 수(K) 설정의 주관성 및 최적값 결정 난제
  - 한계점 : 엘보우(Elbow) 기법의 굴곡점 판정 모호, 실루엣(Silhouette) 계수의 볼록한(Convex) 구형 구조 편향으로 비선형 군집 평가 왜곡.
  - 해결 방안 : Gap Statistic 통계량·갭 검정 적용, 밀도 기반 계열의 DBSCAN과 HDBSCAN(Hierarchical Density-Based Spatial Clustering of Applications with Noise) 및 계층적 클러스터링 앙상블을 통한 군집 수 사전 지정 자동화.
- 한계점 2 : 고차원의 저주(Curse of Dimensionality)로 인한 거리 척도 왜곡
  - 한계점 : 데이터 차원 증가에 따른 유클리드 공간 내 모든 관측치 간 거리의 균일화, 군집 간 경계 붕괴 및 계산 복잡도 폭증.
  - 해결 방안 : UMAP(Uniform Manifold Approximation and Projection), t-SNE(t-distributed Stochastic Neighbor Embedding), 오토인코더(Autoencoder) 기반 비선형 매니폴드 차원 축소의 선행 적용, 코사인 유사도 등 방향성 기반 척도 대체.
- 한계점 3 : 이상치 및 비구형(Non-spherical) 군집 형상 처리 한계
  - 한계점 : K-Means 등 중심 기반 알고리즘의 노이즈·이상치에 의한 군집 중심 과도 편향, 도넛형·초승달형 등 복잡한 기하학적 형태의 식별 실패.
  - 해결 방안 : 중앙값 기반 K-Medoids(PAM, Partitioning Around Medoids) 또는 GMM, 스펙트럴 클러스터링(Spectral Clustering) 채택.

## Ⅵ. 군집분석 도입을 위한 기술사적 제언

- 핵심 요약 : 특성 스케일링 선행, 사전 차원 축소, 비즈니스 실행 가능성 확보.
- 특성 스케일링(Feature Scaling)의 절대성 : 유클리디안 기반 거리의 변수 단위(Scale) 취약성을 감안한 군집화 전 표준화(StandardScaler) 또는 정규화(MinMaxScaler)의 필수 선행.
- 차원의 저주(Curse of Dimensionality) 극복 : 고차원 희소 데이터의 거리 균일화 현상 대비 t-SNE, UMAP, Autoencoder 기반 사전 차원 축소의 결합.
- 비즈니스 실행 가능성(Actionability) 확보 : 수학적으로 분리된 군집의 현업 타깃 마케팅·정책 활용을 위한 군집별 프로파일링 및 특성 해석 워크숍의 병행.

## Ⅶ. 결론

- 핵심 요약 : 군집분석은 방법론·척도·평가 지표의 목적적 조합과 도메인 해석이 성패를 좌우.
- 요약 : 응집도·분리도 원칙과 4대 방법론, 실루엣 등 타당성 평가의 결합 체계.
- 시사점 : 스케일링·차원 축소 등 전처리와 비즈니스 실행 가능성 검증의 필수 병행.
