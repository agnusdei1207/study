---
title: "군집분석(Clustering)"
author: "Codex"
date: "2026-09-20T19:36:54+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 분석에서 비지도학습 및 군집분석으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>비지도학습·데이터마이닝</span>
  <strong>군집분석(Clustering)</strong>
</div>

<details>
<summary>핵심 용어</summary>

- `Cohesion·Separation`: 군집 내부 거리는 줄이고 군집 사이 거리는 늘리는 품질 기준
- `K-Means`: 중심점까지의 제곱거리 합을 반복 최소화하는 분할 군집화
- `DBSCAN(Density-Based Spatial Clustering of Applications with Noise)`: 밀도 연결성과 잡음을 함께 판정하는 군집화
- `GMM(Gaussian Mixture Model)`: 혼합분포의 사후확률로 소속을 정하는 모델 기반 군집화
- `Silhouette Coefficient`: 응집도와 최근접 타 군집 분리도를 결합한 내부 타당성 지표

</details>

## 큰 그림과 30초 인출

- 본질: 정답 레이블(Target)이 없는 데이터에서 객체 간 거리·유사도·밀도를 측정하여, 군집 내 동질성(Cohesion)과 군집 간 이질성(Separation)을 극대화하는 비지도학습 탐색 기법
- 4대 유형: 분할기반(K-Means), 계층적(Ward), 밀도기반(DBSCAN), 모델기반(GMM)
- 평가: 엘보우 차트(SSE), 실루엣 계수(Silhouette Coefficient), 데이비스-볼딘 지수

<div class="itpe-flow-map" role="img" aria-label="군집분석 모델링 및 알고리즘 분기 체계">
  <div class="itpe-flow-node"><strong>라벨 없는 고차원 데이터</strong><small>스케일링 · 거리척도 정의(Euclidean / Cosine)</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>군집 알고리즘 분기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분할(K-Means)</strong><span>중심점 기반 거리 최소화 · 구형 군집</span></div>
      <div class="itpe-flow-branch"><strong>계층(Hierarchical)</strong><span>Dendrogram · Ward 최소분산 연결</span></div>
      <div class="itpe-flow-branch"><strong>밀도(DBSCAN)</strong><span>$\epsilon$-이웃 및 MinPts · 임의 형상 탐지</span></div>
      <div class="itpe-flow-branch"><strong>모델(GMM)</strong><span>EM 알고리즘 · 가우시안 확률적 소속</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>군집 타당성 평가 & 프로파일링</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>타당성</strong><span>실루엣 점수 ($s(i) \to 1$) · Elbow Method</span></div>
      <div class="itpe-flow-branch"><strong>비즈니스</strong><span>고객 페르소나 세분화 · 타깃 마케팅</span></div>
    </div>
  </div>
</div>

## 예상문제

> 레이블이 없는 대규모 데이터에서 고객 세분화 및 이상 패턴 탐지를 위한 군집분석(Cluster Analysis)의 개념, 거리 척도, 주요 4대 군집 유형(분할, 계층, 밀도, 모델)을 비교하고, 최적 군집 수($k$) 결정 기법 및 타당성 평가 지표를 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **군집화(Clustering)** | 관측치 간 유사성을 기반으로 상호 배타적 또는 중첩된 부분집합으로 분할하는 머신러닝 프로세스 | Ⅰ 개요, Ⅳ 절차 |
| **실루엣 계수(Silhouette Coefficient)** | 군집 내 응집도($a$)와 최근접 이웃 군집 간 분리도($b$)를 측정한 $[-1, 1]$ 범위의 타당성 지표 | Ⅴ 평가 기법 |

## Ⅰ. 데이터에 내재된 숨은 구조를 찾는 군집분석의 개요

> **한줄 요약:** 정답 레이블 없이 객체 간 다차원 유사성을 측정해 동질적 하위 집단으로 분할하는 비지도학습 기법임.

- 정의: 주어진 $N$개의 다변량 관측 데이터에 대해 사전 정의된 클래스 정보 없이, 데이터 간의 거리(Distance) 또는 유사도(Similarity)에 기초하여 동일 군집 내 응집성과 타 군집 간 분리성을 최대화하는 패턴 탐색 활동
- 목적: 고객 세분화(Segmentation), 추천 시스템의 협업 필터링, 이미지 분할(Segmentation), 노이즈 제거 및 이상금융거래(FDS) 군집 기반 탐지
- 분류(Classification)와의 차이: 분류는 사전에 정답(Ground Truth)이 존재하여 오분류율을 최소화하는 지도학습이나, 군집분석은 정답 없이 데이터 자체의 기하학적·밀도적 분포를 규명하는 비지도학습임

## Ⅱ. 군집분석의 거리 척도 및 핵심 특징

> **한줄 요약:** 데이터의 속성 형태(연속형, 범주형, 텍스트)에 부합하는 거리 척도 선정이 군집 품질을 좌우함.

| 거리 척도 | 수식 및 원리 | 특성 및 적합 데이터 |
|---|---|---|
| **유클리디안 (Euclidean)** | $d(x, y) = \sqrt{\sum (x_i - y_i)^2}$ | 연속형 다차원 공간의 최단 직선거리, 변수 스케일에 극도로 민감 |
| **맨해튼 (Manhattan)** | $d(x, y) = \sum |x_i - y_i|$ | 격자형 도로망 거리, 이상치(Outlier) 영향이 유클리디안보다 적음 |
| **마할라노비스 (Mahalanobis)** | $d(x, y) = \sqrt{(x-y)^T \Sigma^{-1} (x-y)}$ | 변수 간 상관관계($\Sigma$)를 고려한 거리, 공분산 구조 반영 |
| **코사인 (Cosine)** | $\cos(\theta) = \frac{x \cdot y}{\|x\| \|y\|}$ | 벡터의 크기가 아닌 방향성(각도) 측정, 텍스트 마이닝 및 TF-IDF |

## Ⅲ. 군집분석 4대 유형 비교

> **한줄 요약:** 구형 데이터는 K-Means, 계층 구조는 Ward, 복잡한 비선형 형상은 DBSCAN, 중첩 확률은 GMM을 선택함.

<div class="itpe-pipeline" role="img" aria-label="군집분석 4대 핵심 알고리즘">
  <div class="itpe-pipeline-node"><strong>분할기반</strong><small>K-Means / Medoids</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>계층적</strong><small>Dendrogram / Ward</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>밀도기반</strong><small>DBSCAN / OPTICS</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>모델기반</strong><small>GMM (EM 알고리즘)</small></div>
</div>

| 비교 항목 | 분할기반 (K-Means) | 계층적 (Hierarchical) | 밀도기반 (DBSCAN) | 모델기반 (GMM) |
|---|---|---|---|---|
| **핵심 알고리즘** | 중심점 할당 $\to$ 갱신 반복 | 응집형(Bottom-up) / 분할형 | $\epsilon$-이웃 반경 내 MinPts 밀도 | 다변량 정규분포 혼합 (EM) |
| **군집 수($k$) 지정** | 필수 사전 지정 | 불필요 (Dendrogram 절단) | 불필요 (밀도 파라미터 결정) | 성분 수($K$) 사전 지정 |
| **군집 형성 형태** | 볼록한 구형(Spherical) | 연결법(Single/Ward)에 좌우 | 기하학적 임의 형상 탐지 | 타원형 및 중첩 군집 허용 |
| **이상치 처리** | 이상치에 취약(중심점 왜곡) | 이상치 분리 가능하나 왜곡 | 노이즈 포인트 자동 분류 | 이상치에 민감(확률 왜곡) |
| **시간 복잡도** | $O(N \cdot k \cdot t)$ (대규모 유리) | $O(N^2)$ 또는 $O(N^3)$ (소규모) | $O(N \log N)$ (Spatial Index) | $O(N \cdot K \cdot t)$ (수렴 지연) |

## Ⅳ. 군집분석 5단계 수행 절차

> **한줄 요약:** 전처리 및 거리 정의에서 출발하여 최적 $k$ 탐색, 군집화 및 비즈니스 프로파일링으로 완결함.

| 단계 | 주요 활동 내용 | 핵심 산출물 및 주의사항 |
|---|---|---|
| **1. 탐색 및 전처리** | 결측치 처리, 이상치 정제, 표준화(Z-Score / MinMax) | 단위 편차 제거 필수 (스케일링 누락 시 특정 변수 왜곡) |
| **2. 거리 및 척도 정의** | 데이터 속성 분석 후 유클리디안, 코사인 등 거리 함수 확정 | 거리 행렬(Distance Matrix) |
| **3. 최적 군집 수($k$) 도출** | Elbow 기법(SSE 급감점 탐색), Silhouette 지표 분석 | $k$별 SSE 그래프 및 실루엣 플롯 |
| **4. 군집 모델 학습** | 선택된 알고리즘(K-Means, DBSCAN 등) 학습 및 클러스터 할당 | 군집 라벨(Cluster ID) 할당 테이블 |
| **5. 타당성 평가 및 해석** | 군집 간 분리도 검증, 군집별 평균 특성 분석(Profiling) | 군집별 페르소나 정의서 및 비즈니스 액션 플랜 |

## Ⅴ. 군집 타당성 평가(Cluster Validity) 지표

> **한줄 요약:** 응집도와 분리도를 종합 평가하는 내부 지표(실루엣, 엘보우)로 최적 모형을 검증함.

| 평가 지표 | 계산 공식 및 판정 기준 | 통계적 의미 |
|---|---|---|
| **실루엣 계수 (Silhouette)** | $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$ | $a(i)$: 군집 내 평균 거리, $b(i)$: 최근접 타 군집 평균 거리. $1$에 가까울수록 완벽, $0$은 경계, 음수는 오분류 |
| **엘보우 기법 (Elbow Method)** | $SSE = \sum_{k=1}^K \sum_{x \in C_k} \|x - \mu_k\|^2$ | 군집 수 $k$ 증가에 따른 군집 내 제곱합(SSE) 감소율이 급격히 완만해지는 팔꿈치(Elbow) 지점 선택 |
| **데이비스-볼딘 (DBI)** | $R_{ij} = \frac{s_i + s_j}{d(c_i, c_j)}$ 의 최대값 평균 | 군집 내 산포 대비 군집 간 거리 비율. 값이 작을수록 우수한 군집화 |
| **ARI (Adjusted Rand Index)** | 외적 정답 라벨이 존재할 때 일치율 우연 보정 | $-1 \le ARI \le 1$, 지도학습 벤치마크 평가 시 활용 |

## Ⅵ. 실무 고려사항 및 분석 장애 대책

> **한줄 요약:** 차원의 저주, 초기값 수렴 실패, 비선형 형상 왜곡을 PCA와 K-Means++로 방어함.

- 적용 상황: 수백 개 행동 로그를 가진 1,000만 사용자 대상 이커머스 마케팅 세분화

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **차원의 저주 (Curse of Dim)** | 변수가 수십~수백 개일 때 모든 점 간 거리가 균일화 | PCA 또는 t-SNE로 중요 차원 축소 후 군집화 | 거리 변별력 복원 및 계산 속도 대폭 개선 |
| **K-Means 초기값 함정** | 무작위 중심점 선택으로 인한 국소 최적해(Local Minima) | K-Means++ 알고리즘(점 간 최대 거리 기반 초기화) 기본 적용 | 최적해 수렴 안정성 확보 |
| **비선형 복잡 군집 왜곡** | K-Means가 초승달·도넛형 비선형 군집을 강제로 구형 분할 | DBSCAN, Spectral Clustering, 고차원 커널 기법 적용 | 실제 복합 패턴 및 잡음(Noise)의 정확한 분리 |

## Ⅶ. 결론 및 기술사적 제언

> **한줄 요약:** 군집분석은 통계적 군집 형성에 그치지 않고 비즈니스 액션이 가능한 실용적 페르소나를 도출해야 함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 높은 실루엣 점수만으로는 쓸 수 있는 군집이 되지 않는다. 수학적 분리도와 도메인 설명가능성이 함께 확보되어야 한다.
- `나라면`: PCA로 거리 변별력을 복원하고 K-Means++로 안정화한 뒤, 군집별 대표 특성과 업무 행동을 함께 검증하겠다.

### 실전 답안용 기술사적 제언

- 판정: 내부 타당성과 반복 표본 안정성, 현업 행동 가능성을 함께 충족해야 운영 군집으로 승인
- 대안: 스케일링·차원 축소 → 복수 알고리즘 후보 학습 → 군집 프로파일과 담당 업무 연결
- 검증: 실루엣·DBI, 재표본화 군집 일치도, 캠페인 반응률을 Quality Gate로 측정
- 효과: 우연한 분할과 해석 불가능 군집 제거 → 재현 가능한 세분화 확보

<div class="itpe-flow-map" role="img" aria-label="군집분석 개선안과 검증 흐름">
  <div class="itpe-flow-node"><strong>현행 한계</strong><span>문제: 단일 점수·단일 알고리즘 의존</span></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>개선안</strong><span>대안: 전처리·후보 비교·업무 프로파일 결합</span></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>승인 Gate</strong><span>판정: 타당성·안정성·행동 가능성 동시 충족</span></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>운영 효과</strong><span>효과: 재현 가능한 고객 세분화</span></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 군집분석(Clustering)은 정답 레이블이 없는 데이터에서 객체 간 거리·유사성을 측정하여 군집 내 동질성과 군집 간 이질성을 최대화하는 비지도학습 탐색 기법임.

### 2. 핵심 메커니즘 / 체계
```text
[입력] 스케일링/거리정의 ──▶ [알고리즘] 분할 / 계층 / 밀도 / 모델
                                          │
[평가] 실루엣 s(i) = (b-a)/max(a,b) ── [도출] 비즈니스 페르소나
```
- Elbow Method와 실루엣 계수로 최적 군집 수 $k$를 결정함.

### 3. 적용 제언
- 고차원 데이터의 차원의 저주를 해결하기 위해 PCA 차원 축소를 선행하고, K-Means++ 초기화를 적용하여 국소해 수렴을 방어해야 함.

## 출제 이력과 검증 출처

- [scikit-learn, Clustering](https://scikit-learn.org/stable/modules/clustering.html)
- [NIST/SEMATECH e-Handbook, Cluster Analysis](https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc44.htm)

## 학습 체크

- [ ] Ⅰ·Ⅱ 정의와 척도: 비지도학습의 목적과 데이터 유형별 거리 척도 4개를 재현한다.
- [ ] Ⅲ 알고리즘 비교: K-Means·계층·DBSCAN·GMM을 군집 수, 형상, 이상치 기준으로 비교한다.
- [ ] Ⅳ·Ⅴ 수행과 평가: 전처리부터 프로파일링까지 5단계와 실루엣 산식을 연결한다.
- [ ] Ⅵ·Ⅶ 대책과 판단: 차원의 저주·초기값·비선형 형상 대책과 운영 승인 Gate를 설명한다.

## 연결 토픽

- 이전 토픽: [다중공선성(등분산성 포함)](./004_multicollinearity.md)
- 연관 토픽: [K-Means](./029_k_means.md), [차원 축소(PCA·MDS)](./069_dimensionality_reduction_pca_mds.md), [이상치](./010_outlier.md)
- 다음 토픽: [데이터 거버넌스(Data Governance)](./006_data_governance.md)
