---
title: "군집분석(Clustering)"
category: "03-data"
tags:
  - "군집분석"
  - "Clustering"
  - "KMeans"
  - "DBSCAN"
  - "GMM"
  - "실루엣계수"
  - "비지도학습"
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
extra:
  model: "GPT-6"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 분석에서 비지도학습 및 군집분석으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>비지도학습·데이터마이닝</span>
  <strong>군집분석(Clustering)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 정답 레이블(Target)이 없는 다차원 데이터셋에서 객체 간 유사도·거리·밀도를 측정하여, 군집 내 응집도(Cohesion)와 군집 간 분리도(Separation)를 극대화하는 비지도 기계학습 탐색 기법
- 메커니즘: 전처리 및 거리 척도 정의 $\rightarrow$ 군집 알고리즘(분할·계층·밀도·모델) 적용 $\rightarrow$ 최적 군집 수($k$) 결정(Elbow/Silhouette) $\rightarrow$ 군집 타당성 평가 $\rightarrow$ 세그먼트 프로파일링
- 산출물: 군집 할당 레이블 · 덴드로그램(Dendrogram) / 엘보우 곡선도 · 실루엣 타당성 평가서 · 세그먼트별 고객 페르소나 정의서

<div class="itpe-flow-map" role="img" aria-label="군집분석 모델링 및 타당성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 고차원 데이터 전처리 및 거리 척도 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>전처리</strong><span>변수 표준화(Z-score), 거리 척도(Euclidean, Cosine, Mahalanobis) 선정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 4대 군집화 알고리즘 학습</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분할(K-Means)</strong><span>중심점 거리 최소화, 대용량 구형 군집</span></div>
      <div class="itpe-flow-branch"><strong>계층(Hierarchical)</strong><span>Dendrogram, Ward 최소분산 결합</span></div>
      <div class="itpe-flow-branch"><strong>밀도(DBSCAN)</strong><span>$\epsilon$-이웃 및 MinPts, 비선형·노이즈 분리</span></div>
      <div class="itpe-flow-branch"><strong>모델(GMM)</strong><span>EM 알고리즘, 가우시안 확률적 소프트 할당</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 최적 군집 수($k$) 탐색</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>탐색</strong><span>Elbow Method(SSE 급감점), Davies-Bouldin Index(DBI) 최소화 지점 분석</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 군집 타당성 및 비즈니스 해석력 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>평균 실루엣 계수가 유효 범위($s(i) \ge 0.5$)에 있고, 도메인 페르소나 설명력이 확보되는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (최적 군집 모델 확정)</strong>
      <span>군집 레이블링 완료 $\rightarrow$ 타깃 마케팅 캠페인 및 FDS 이상 거래 탐지 룰셋 배포</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (군집 중첩 / 무의미한 분할)</strong>
      <span>모델 재학습 $\rightarrow$ PCA 차원 축소 선행, 거리 척도 재조정 및 DBSCAN/GMM 전환</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Cohesion(응집도)`: 동일 군집 내 데이터 포인트들이 중심점 또는 서로 간에 얼마나 가깝게 밀집되어 있는가를 나타내는 척도
- `Separation(분리도)`: 서로 다른 군집 간의 경계 거리가 얼마나 명확하게 떨어져 있는가를 나타내는 척도
- `K-Means`: 중심점(Centroid)과 데이터 간의 오차제곱합(SSE)을 최소화하도록 군집을 반복적으로 갱신하는 대표적 분할 군집화 알고리즘
- `DBSCAN`: 반경($\epsilon$) 내 최소 데이터 개수(MinPts)를 기준으로 밀집된 영역을 연결해 임의 형상의 군집을 찾고 노이즈를 필터링하는 밀도 기반 알고리즘
- `GMM(Gaussian Mixture Model)`: 데이터가 여러 가우시안 분포의 혼합체로 구성되었다고 가정하고 EM(Expectation-Maximization) 알고리즘으로 확률적 소속도를 구하는 모델 기반 알고리즘
- `Silhouette Coefficient`: 데이터 개체별 응집도($a$)와 가장 가까운 타 군집과의 분리도($b$)를 조합한 $[-1, 1]$ 범위의 내부 타당성 평가 지표

</details>
---

## 1교시 예상문제 (10점)

> 군집분석(Clustering)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

```text
1. 군집분석(Clustering)의 정의 및 목적
- 정의: 정답 레이블 없이 객체 간 거리와 유사도를 기반으로 군집 내 응집도와 군집 간 분리도를 극대화하는 비지도학습 탐색 기법
- 목적: 고객 세분화(Segmentation), 이상 패턴 탐지(FDS), 데이터 축약

2. 4대 군집 유형 및 핵심 차이
- 분할 기반: K-Means (중심점 기반 거리 최소화, 구형 군집, 대용량 적합)
- 계층적   : Ward/병합형 (Dendrogram 트리 구조, 사전 k 불필요, 계산 복잡)
- 밀도 기반: DBSCAN (Epsilon/MinPts 반경, 비선형 임의 형상 탐지, 노이즈 필터링)
- 모델 기반: GMM (EM 알고리즘 기반 가우시안 확률적 소프트 할당)

3. 타당성 평가 및 최적 k 결정
- Elbow Method: SSE 감소율이 완만해지는 꺾임점 선정
- Silhouette 계수: s(i) = (b(i) - a(i)) / max(a(i), b(i)), 전체 평균 0.5 이상 권장
```
---

### 핵심 관계

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **K-Means 군집화** | 중심점 반복 갱신, SSE 최소화, K-Means++, 국소 최적해 한계 | Ⅲ·Ⅵ |
| **밀도 기반 군집화(DBSCAN)** | Epsilon, MinPts, Core/Border/Noise Point, 임의 형상 탐지 | Ⅲ·Ⅴ |
| **군집 타당성 평가** | 실루엣 계수($s(i)$), 엘보우 기법(Elbow Method), 데이비스-볼딘 지수(DBI) | Ⅳ·Ⅴ |

---

## 2~4교시 예상문제 (25점)

> 레이블이 없는 대규모 데이터에서 고객 세분화 및 이상 패턴 탐지를 위한 군집분석(Cluster Analysis)의 개념, 거리 척도, 주요 4대 군집 유형(분할, 계층, 밀도, 모델)을 비교하고, 최적 군집 수($k$) 결정 기법 및 타당성 평가 지표를 설명하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **K-Means 군집화** | 중심점 반복 갱신, SSE 최소화, K-Means++, 국소 최적해 한계 | Ⅲ·Ⅵ |
| **밀도 기반 군집화(DBSCAN)** | Epsilon, MinPts, Core/Border/Noise Point, 임의 형상 탐지 | Ⅲ·Ⅴ |
| **군집 타당성 평가** | 실루엣 계수($s(i)$), 엘보우 기법(Elbow Method), 데이비스-볼딘 지수(DBI) | Ⅳ·Ⅴ |

### Ⅰ. 데이터에 내재된 숨은 구조를 찾는 군집분석의 개요

> 정답 레이블 없이 객체 간 다차원 유사성을 측정해 동질적 하위 집단으로 분할하는 비지도학습 기법임.

- 정의: 주어진 $N$개의 다변량 관측 데이터에 대해 사전 정의된 클래스 정보 없이, 데이터 간의 거리(Distance) 또는 유사도(Similarity)에 기초하여 동일 군집 내 응집성과 타 군집 간 분리성을 최대화하는 패턴 탐색 활동
- 목적: 고객 세분화(Segmentation), 추천 시스템 협업 필터링, 이미지 분할, 노이즈 제거 및 이상금융거래(FDS) 이상치 군집 분리
- 분류(Classification)와의 비교: 분류는 사전에 정답 레이블(Ground Truth)이 주어지는 지도학습이나, 군집분석은 정답 없이 데이터 자체의 공간적 분포를 군집화하는 비지도학습임

### Ⅱ. 데이터 유형별 거리 및 유사도 척도 체계

> 데이터의 척도(수치형 vs 범주형)에 적합한 거리 함수를 선택해야 왜곡 없는 유사도를 측정할 수 있음.

| 데이터 유형 | 대표 거리/유사도 척도 | 수식 및 핵심 원리 | 실무 적용 특성 |
|---|---|---|---|
| **연속형 (수치)** | **유클리디안 거리 (Euclidean)** | $d(x,y) = \sqrt{\sum (x_i - y_i)^2}$ | 피타고라스 정리 기반 최단 직선거리, 스케일링 필수 |
| **연속형 (수치)** | **맨해튼 거리 (Manhattan)** | $d(x,y) = \sum |x_i - y_i|$ | 격자형 경로 거리 ($L_1$ Norm), 이상치 영향 둔감 |
| **다변량 상관** | **마할라노비스 거리 (Mahalanobis)** | $d(x,y) = \sqrt{(x-y)^T \Sigma^{-1} (x-y)}$ | 변수 간 공분산($\Sigma$)을 반영하여 상관관계가 있는 데이터의 통계적 거리 측정 |
| **텍스트·고차원** | **코사인 유사도 (Cosine)** | $\cos(\theta) = \frac{x \cdot y}{\|x\| \|y\|}$ | 벡터의 크기가 아닌 사잇각 방향성 기반 유사도 (문서 분류) |
| **범주형 (이진)** | **자카드 유사도 (Jaccard)** | $J(A,B) = \frac{|A \cap B|}{|A \cup B|}$ | 교집합 크기를 합집합 크기로 나눈 비율 (장바구니 분석) |

### Ⅲ. 군집분석 4대 유형 및 알고리즘 아키텍처 비교

> 대규모 정형 데이터는 분할 기반, 노이즈가 많은 비선형 공간은 밀도 기반, 중첩 허용은 모델 기반을 채택함.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Type 1: Partitioning -->
    <rect x="15" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="15" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="72" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">분할 기반</text>
    <circle cx="72" cy="65" r="18" fill="none" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <circle cx="72" cy="65" r="2.5" fill="#dc2626"/>
    <text x="72" y="105" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">K-Means / Medoids</text>
    <text x="72" y="125" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">중심점 거리 최소화</text>
    <text x="72" y="140" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">구형(Spherical) 군집</text>
    <text x="72" y="155" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">이상치에 민감</text>
    <text x="72" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">대규모 정형 데이터</text>

    <!-- Type 2: Hierarchical -->
    <rect x="140" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="140" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="197" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">계층적</text>
    <!-- Dendrogram sketch -->
    <path d="M 175 75 L 175 60 L 220 60 L 220 75 M 197 60 L 197 50" fill="none" stroke="var(--color-primary, #2563eb)" stroke-width="1.2"/>
    <text x="197" y="105" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">Ward / 병합형</text>
    <text x="197" y="125" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">Dendrogram 트리</text>
    <text x="197" y="140" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">k 사전 지정 불필요</text>
    <text x="197" y="155" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">$O(n^2)$ 연산 복잡도</text>
    <text x="197" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">소규모 탐색 분석</text>

    <!-- Type 3: Density-based -->
    <rect x="265" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.5"/>
    <rect x="265" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="322" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">밀도 기반</text>
    <!-- Irregular shape + noise -->
    <path d="M 295 70 Q 320 50 345 70" fill="none" stroke="#16a34a" stroke-width="3"/>
    <circle cx="340" cy="52" r="2" fill="#dc2626"/>
    <text x="322" y="105" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">DBSCAN / OPTICS</text>
    <text x="322" y="125" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">$\epsilon$ 반경 + MinPts</text>
    <text x="322" y="140" text-anchor="middle" font-size="6.5" fill="#16a34a">임의 형상 완벽 분리</text>
    <text x="322" y="155" text-anchor="middle" font-size="6.5" fill="#dc2626">노이즈 자동 필터링</text>
    <text x="322" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">지리/공간·FDS 이상치</text>

    <!-- Type 4: Model-based -->
    <rect x="390" y="15" width="115" height="190" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="390" y="15" width="115" height="24" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="447" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">모델 기반</text>
    <!-- Ellipse overlap -->
    <ellipse cx="440" cy="65" rx="18" ry="10" fill="none" stroke="#ca8a04" stroke-width="1.2" transform="rotate(-20 440 65)"/>
    <ellipse cx="455" cy="68" rx="15" ry="9" fill="none" stroke="var(--color-primary, #2563eb)" stroke-width="1.2" transform="rotate(30 455 68)"/>
    <text x="447" y="105" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">GMM (가우시안 혼합)</text>
    <text x="447" y="125" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">EM 확률적 소프트 할당</text>
    <text x="447" y="140" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">타원형 다양한 공분산</text>
    <text x="447" y="155" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">군집 간 중첩 허용</text>
    <text x="447" y="185" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">확률적 고객 프로파일</text>
  </svg>
</div>

| 비교 항목 | 분할 기반 (Partitioning) | 계층적 (Hierarchical) | 밀도 기반 (Density-based) | 모델 기반 (Model-based) |
|---|---|---|---|---|
| **대표 알고리즘** | **K-Means**, K-Medoids | 병합형(Agglomerative), Ward | **DBSCAN**, OPTICS | **GMM (가우시안 혼합)** |
| **군집 형성 방식** | 중심점을 반복 이동하여 군집 할당 | 가까운 개체를 순차 병합하여 트리 형성 | 밀집 구역을 연결하고 희소 영역을 노이즈화 | 확률분포(가우시안)를 따르는 하위 모집단 분리 |
| **군집 수($k$) 지정** | 사전에 $k$를 반드시 입력해야 함 | 덴드로그램 컷팅으로 사후 결정 | 사전에 $k$를 지정하지 않음 ($\epsilon, MinPts$) | 사전에 컴포넌트 수($k$) 지정 필요 |
| **군집 형상** | 볼록한 구형(Spherical) 군집에 한정 | 트리 깊이에 따른 다양한 계층 구조 | 초승달, 도넛 등 임의의 기하학적 형상 탐지 | 타원형, 다양한 공분산 형태의 유연한 군집 |
| **이상치 처리** | 이상치에 극도로 취약 (중심점 왜곡) | 이상치가 단독 리프 노드로 분리 | 노이즈 포인트로 자동 완벽 분리 | 이상치에 둔감한 강건 공분산 추정 가능 |
| **계산 복잡도** | $O(t \cdot k \cdot n)$ (대규모 데이터 적합) | $O(n^2 \log n) \sim O(n^3)$ (대용량 불가) | $O(n \log n) \sim O(n^2)$ | $O(t \cdot k \cdot n \cdot d^2)$ (EM 수렴 시간 소요) |

### Ⅳ. 군집 타당성 평가 및 최적 군집 수($k$) 결정

> 정답이 없는 비지도학습의 특성상 내부 평가 지표와 시각적 꺾임목을 종합하여 $k$를 결정함.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <rect x="5" y="5" width="510" height="170" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Left: Elbow Method Graph -->
    <rect x="15" y="15" width="240" height="150" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="135" y="32" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">Elbow Method (SSE 꺾임목)</text>
    <!-- Axes -->
    <line x1="45" y1="135" x2="230" y2="135" stroke="var(--color-text, #1e293b)" stroke-width="1"/>
    <line x1="45" y1="135" x2="45" y2="45" stroke="var(--color-text, #1e293b)" stroke-width="1"/>
    <text x="235" y="138" font-size="6.5" fill="var(--color-text-muted, #64748b)">k</text>
    <text x="40" y="42" text-anchor="end" font-size="6.5" fill="var(--color-text-muted, #64748b)">SSE</text>
    <!-- Curve -->
    <path d="M 55 50 Q 85 105 110 115 T 215 130" fill="none" stroke="#dc2626" stroke-width="2"/>
    <!-- Elbow point -->
    <circle cx="110" cy="115" r="4" fill="#dc2626"/>
    <line x1="110" y1="115" x2="110" y2="135" stroke="#dc2626" stroke-width="1" stroke-dasharray="2,2"/>
    <text x="110" y="145" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#dc2626">k=3 (Elbow)</text>
    <text x="145" y="95" font-size="6.5" font-weight="bold" fill="#dc2626">팔꿈치 급감점</text>

    <!-- Right: Silhouette Plot Graph -->
    <rect x="265" y="15" width="240" height="150" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="385" y="32" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">Silhouette Plot (실루엣 계수)</text>
    <!-- Bars -->
    <text x="275" y="55" font-size="7" fill="var(--color-text, #334155)">군집 1</text>
    <rect x="310" y="46" width="130" height="12" rx="2" fill="#16a34a"/>
    <text x="445" y="55" font-size="6.5" fill="#16a34a">s=0.78</text>

    <text x="275" y="78" font-size="7" fill="var(--color-text, #334155)">군집 2</text>
    <rect x="310" y="69" width="105" height="12" rx="2" fill="var(--color-primary, #2563eb)"/>
    <text x="420" y="78" font-size="6.5" fill="var(--color-primary, #2563eb)">s=0.62</text>

    <text x="275" y="101" font-size="7" fill="var(--color-text, #334155)">군집 3</text>
    <rect x="310" y="92" width="80" height="12" rx="2" fill="#ca8a04"/>
    <text x="395" y="101" font-size="6.5" fill="#ca8a04">s=0.51</text>

    <!-- Average line -->
    <line x1="380" y1="40" x2="380" y2="120" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,2"/>
    <text x="380" y="132" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#dc2626">평균 실루엣 점수 = 0.64 (&ge; 0.5 우수)</text>
    <text x="385" y="152" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">$s(i) = [b(i)-a(i)] / \max(a, b)$</text>
  </svg>
</div>

1. **엘보우 기법(Elbow Method)**: 군집 수 $k$를 증가시키면서 군집 내 오차제곱합(SSE)의 감소 폭이 둔화되는 팔꿈치(Elbow) 꺾임점을 최적의 $k$로 선정
2. **실루엣 계수(Silhouette Coefficient)**:
   - 수식: $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$ (단, $a(i)$는 군집 내 평균 거리, $b(i)$는 가장 가까운 타 군집과의 평균 거리)
   - 판정: $s(i) \to 1$일수록 완벽한 분리, $s(i) \approx 0$은 군집 경계 중첩, $s(i) < 0$은 잘못된 군집 할당 판정 (전체 평균 0.5 이상 권장)
3. **데이비스-볼딘 지수(DBI)**: 군집 내 거리 대비 군집 간 거리의 비율을 계산하며, 수치가 작을수록 우수한 군집화로 평가

### Ⅴ. K-Means vs DBSCAN 심층 비교

> 형상의 유연성과 노이즈 처리 능력에서 뚜렷한 대비를 이룸.

| 비교 기준 | K-Means 군집화 | DBSCAN 군집화 |
|---|---|---|
| **기본 가정** | 군집들이 구형이며 분산이 유사하다고 가정 | 밀도가 높은 영역이 연속적으로 이어져 있다고 가정 |
| **주요 하이퍼파라미터**| 군집 수($k$) | 탐색 반경($\epsilon$, Epsilon), 최소 포인트 수($MinPts$) |
| **비선형 패턴 탐지** | 분할 실패 (동심원, 복합 곡선 분할 불가) | 완벽 분리 (임의 형상 군집 추적 가능) |
| **노이즈 처리** | 모든 포인트를 강제로 군집에 귀속 (이상치 왜곡 심각) | 밀도가 낮은 점을 Noise(-1)로 분리 배제 |
| **초기값 의존성** | 초기 중심점 위치에 따라 국소해(Local Minima) 함정 | 파라미터가 동일하면 항상 일관된 결정론적 결과 산출 |

### Ⅵ. 군집분석 문제점·대응책

> 알고리즘의 통계적 가정 위배와 차원의 저주로 인한 분석 실패를 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 차원의 저주로 인한 거리 변별력 상실 | PCA 또는 t-SNE 기반 주성분 추출 후 군집화 수행 | 거리 왜곡 방지 및 클러스터링 계산 비용 대폭 절감 |
| K-Means 초기값 의존성 (국소 최적해) | 점 간 거리에 비례하여 초기점을 분산시키는 K-Means++ 적용 | 최적 중심점 수렴 속도 단축 및 일관된 군집 결과 도출 |
| 비선형 기하학 군집의 구형 왜곡 | DBSCAN·스펙트럴 군집화 비교 | 비선형 패턴·노이즈 구분 개선 |
| 수학적 타당성 대비 도메인 해석 불가 | 군집별 핵심 변수 평균치 및 결정트리(Decision Tree) 기반 규칙 추출 | 현업 마케터가 활용 가능한 비즈니스 페르소나 확보 |

### Ⅶ. 기술사적 제언: 수학적 분리도를 넘어 비즈니스 액션으로의 연결

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 높은 실루엣 점수만으로는 쓸 수 있는 군집이 되지 않는다. 아무리 수학적으로 군집 간 분리도가 우수해도, 세분화된 그룹이 비즈니스 현업에서 마케팅 캠페인이나 FDS 차단 룰로 전환되지 못하면 공허한 분석에 불과하다. 진정한 비지도학습의 가치는 알고리즘의 타당성 지표($s(i) \ge 0.5$)와 함께, **각 군집의 결정 규칙(Decision Rules)을 비즈니스 페르소나로 설명해내는 설명가능성(Interpretability)**에 있다.

> **[나라면 이렇게 쓴다]**
> 2교시 논술이라면 고차원 이기종 데이터 환경에서 **'2단계 앙상블 군집화 파이프라인'**을 제시하겠다. 1단계로 PCA/t-SNE를 통해 차원의 저주를 극복한 뒤, 2단계에서 DBSCAN으로 비선형 노이즈를 먼저 걸러내고 잔여 정제 데이터에 대해 K-Means++를 적용하겠다. 최종적으로 각 군집을 Target으로 하는 분류 결정트리(Decision Tree)를 적합시켜, 현업이 즉시 실행 가능한 고객군별 핵심 규칙(If-Then Rule)을 도출하는 실전 전략을 완결하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 통계적 내부 타당성(평균 실루엣 계수 $\ge 0.5$)과 함께 **도메인 설명가능성 및 비즈니스 실행 가능성(Actionability)**을 모델 배포 승인 필수로 판정.
- **대응 방안**: K-Means++로 초기 수렴성을 확보하고, 비선형·노이즈 환경에서는 DBSCAN을 병행 적용하여 알고리즘 편향 극복.
- **검증 체계**: Elbow Method, Silhouette Plot, Davies-Bouldin Index(DBI) 3대 타당성 지표 교차 검증 및 군집별 변수 프로파일링 수행.
- **기대 효과**: 무의미한 군집 중첩을 95% 이상 제거하고, 고객 세그먼트별 정밀 타깃 마케팅 전환율 3배 증대 달성.

<div class="itpe-flow-map" role="img" aria-label="군집분석 모델링 및 비즈니스 액션 파이프라인">
  <div class="itpe-flow-node">
    <strong>차원 축소 및 거리 표준화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>전처리</strong><span>PCA 주성분 + Z-score 변환</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>K-Means++ / DBSCAN 학습</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>모델링</strong><span>Elbow 최적 k + 노이즈 분리</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node is-current">
    <strong>실루엣 타당성 게이트</strong>
    <div class="itpe-step-detail">
      <strong>판정</strong><span>실루엣 점수 &ge; 0.5 + 비즈니스 설명력</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>세그먼트 룰셋 배포</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>활용</strong><span>타깃 캠페인 및 FDS 정책 탑재</span></div>
    </div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제134·139회 확인 · 제128회는 KPC 보조자료이며 공식 원문 미확보
- **검증 출처**: [scikit-learn Clustering Guide](https://scikit-learn.org/stable/modules/clustering.html), [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/)

## 연결 토픽

- [K-Means](./029_k_means.md) · [차원 축소(PCA·MDS)](./069_dimensionality_reduction_pca_mds.md) · [이상치](./010_outlier.md) · [다중공선성](./004_multicollinearity.md)
