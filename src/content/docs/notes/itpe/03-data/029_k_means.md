---
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
extra:
  keyword_grade: "A"
  model: "GPT-6"
  question_no: "029"
sidebar:
  badge:
    text: "A"
    variant: "note"
  label: "029. K-Means"
  order: 29
tags:
  - "notes-data"
title: "K-Means 군집화 (K-Means Clustering)"
weight: 29
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 분석·마이닝</span><span>비지도 학습·군집 분석</span><strong>K-Means</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 140" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="140" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <rect x="170" y="10" width="180" height="26" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="260" y="27" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #0f172a)">비지도 다차원 데이터셋</text>
  <line x1="260" y1="36" x2="260" y2="48" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-km)"/>

  <rect x="15" y="50" width="145" height="42" fill="var(--color-primary-light, #e0f2fe)" stroke="var(--color-primary, #0284c7)" stroke-width="1" rx="4"/>
  <text x="87" y="66" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">1. 초기화 (K-Means++)</text>
  <text x="87" y="81" text-anchor="middle" font-size="8" fill="var(--color-text, #334155)">거리제곱 확률 중심선정</text>

  <line x1="160" y1="71" x2="180" y2="71" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-km)"/>

  <rect x="185" y="50" width="150" height="42" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="260" y="66" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">2. 최근접 중심 할당</text>
  <text x="260" y="81" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">유클리디안 거리 최소화</text>

  <line x1="335" y1="71" x2="355" y2="71" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-km)"/>

  <rect x="360" y="50" width="145" height="42" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="432" y="66" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--color-text, #0f172a)">3. 중심점 평균 갱신</text>
  <text x="432" y="81" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">군집 내 무게중심 재계산</text>

  <path d="M 432 92 L 432 105 L 260 105" fill="none" stroke="var(--color-primary, #0284c7)" stroke-width="1.2" stroke-dasharray="3 2" marker-end="url(#arrow-km)"/>

  <rect x="130" y="102" width="260" height="26" fill="var(--color-success-light, #dcfce7)" stroke="var(--color-success, #16a34a)" stroke-width="1" rx="4"/>
  <text x="260" y="119" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--color-success-dark, #15803d)">4. 수렴 판정: SSE 변화량 &lt; ε (군집 내 제곱합 최소화 완료)</text>

  <defs>
    <marker id="arrow-km" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <polygon points="0 0, 6 3, 0 6" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **데이터 포인트를 가장 가까운 중심점(Centroid)에 할당하고, 각 군집의 평균 위치로 중심점을 갱신하는 과정을 반복하여 군집 내 제곱합(SSE, Sum of Squared Errors)을 최소화하는 분할 기반 군집화 알고리즘**
- 암기: `초-할-갱-수` = 초기화(K-Means++) $\to$ 할당(최근접 거리) $\to$ 갱신(평균 계산) $\to$ 수렴(SSE 안정화)
- 한계와 대안: 구형(Spherical) 군집 가정 및 이상치 민감 $\to$ K-Medoids(중앙값) 또는 DBSCAN(밀도 기반)
- 최적 $k$ 판정: 엘보우 기법(Elbow Method, SSE 급감 변곡점) + 실루엣 계수(Silhouette Coefficient, 0.5 이상)
---

## 1교시 예상문제 (10점)

> K-Means 군집화 (K-Means Clustering)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. K-Means 군집화의 정의

- 데이터 간 유클리디안 거리를 기반으로 군집 내 오차제곱합(SSE)을 최소화하도록 중심점을 반복 갱신하는 **비지도 분할 군집화 알고리즘**

### 2. K-Means 4단계 수렴 절차 및 목적함수

$$\text{SSE} = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - \mu_i\|^2$$

- **1단계 (초기화)**: K-Means++ 방식으로 기존 중심 간 거리 제곱에 비례하는 확률 기반 $k$개 중심점 선정
- **2단계 (할당)**: 각 데이터를 가장 가까운 중심점에 배정 ($c(j) = \arg\min_i \|x_j - \mu_i\|^2$)
- **3단계 (갱신)**: 군집 내 배정된 데이터의 산술평균으로 중심점 좌표 갱신 ($\mu_i = \frac{1}{|C_i|} \sum x$)
- **4단계 (수렴)**: 중심점 이동 거리 또는 SSE 변화량이 임계치 $\epsilon$ 미만일 때 종료

| 핵심 비교 | K-Means | DBSCAN |
|---|---|---|
| 군집 기준 / 형태 | 평균 중심점 / 볼록한 구형 군집 | 데이터 밀도 (MinPts, Epsilon) / 임의 기하 형태 |
| 파라미터 / 이상치 | $k$ 사전 입력 필수 / 이상치에 매우 취약 | $k$ 불필요 / 노이즈(Noise) 자동 분리 |

### 3. 차별화 제언

- 초기 중심점 편향 방지를 위해 **K-Means++**를 기본 적용하고, **엘보우 변곡점 + 실루엣 계수(0.5 이상)**의 이중 검증으로 비즈니스 수용 가능한 최적 $k$를 결정함
---

## 2~4교시 예상문제 (25점)

> 비지도 학습의 대표적 분할 군집화 기법인 K-Means의 개념, 동작 절차 및 수학적 목적함수를 제시하고, 초기값 민감성 극복 방안(K-Means++)과 최적의 군집 수($k$) 결정 기법 및 DBSCAN과의 비교를 논하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 대용량 데이터 세분화를 위한 K-Means 군집화 개요

- 정의: **K-Means**는 사전 정의된 라벨이 없는 $n$개의 다차원 데이터를 사용자가 지정한 $k$개의 군집으로 묶되, 각 군집 내부의 응집도를 나타내는 군집 내 오차제곱합(SSE)이 최소가 되도록 중심점을 반복 이동시키는 분할 기반 비지도 머신러닝 알고리즘
- 목적: 고객 세분화(Segmentation), 이상 거래 탐지(사전 클러스터링), 추천 시스템의 프로파일링을 위해 데이터의 고유한 패턴을 비지도 방식으로 집단화
- 필요성: 고차원 대용량 데이터에서 계층적 군집화는 $O(n^3)$ 또는 $O(n^2)$의 높은 연산 비용으로 적용이 불가능하므로, $O(nkt)$로 선형에 가깝게 동작하는 K-Means의 확장이 필수적임

#### 한줄 요약

- K-Means는 데이터와 중심점 간 유클리디안 거리를 기반으로 반복적인 할당과 갱신을 통해 최적의 군집 중심을 찾아가는 고속 알고리즘임

### Ⅱ. K-Means의 핵심 속성과 수학적 목적함수(SSE)

$$\text{SSE} = \sum_{i=1}^{k} \sum_{x \in C_i} \|x - \mu_i\|^2$$

- $k$: 사전 지정된 군집의 개수
- $C_i$: $i$번째 군집에 속한 데이터 포인트들의 집합
- $x$: 다차원 데이터 포인트 벡터
- $\mu_i$: $i$번째 군집의 중심점(Centroid, 산술평균 벡터)

| 특성 | 메커니즘 | 실무 장단점 |
|---|---|---|
| **계산 복잡도 ($O(nkt)$)** | 데이터 수($n$), 군집 수($k$), 반복 횟수($t$)에 선형 비례 | - 장점: 수백만 건의 대규모 데이터셋도 실시간 처리 가능<br>- 대안: 초거대 데이터는 Mini-Batch K-Means로 최적화 |
| **기하학적 형태 가정** | 유클리디안 거리 기준으로 등방성(Isotropic) 구형 군집 형성 | - 단점: 초승달, 도넛형, 긴 띠 형태 등 비선형 복합 분포 분할 실패<br>- 대안: 커널 K-Means 또는 DBSCAN 적용 |
| **이상치(Outlier) 민감성** | 중심점 계산 시 산술평균($\mu$)을 사용하므로 극단값에 왜곡 | - 단점: 이상치 하나가 전체 군집 중심을 강하게 편향시킴<br>- 대안: 중앙 객체를 사용하는 K-Medoids(PAM) 채택 |
| **국소 최적해(Local Minima)** | 초기 중심점의 위치에 따라 최종 군집 결과가 달라짐 | - 단점: 매 실행 시마다 클러스터링 결과가 불일치할 위험<br>- 대안: K-Means++ 초기화 알고리즘 의무 적용 |

#### 한줄 요약

- K-Means는 $O(nkt)$의 초고속 연산이라는 강점이 있으나, 구형 군집 가정과 이상치 왜곡이라는 뚜렷한 한계를 가짐

### Ⅲ. K-Means 4단계 수렴 알고리즘 및 K-Means++ 초기화

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 125" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="125" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <rect x="20" y="15" width="220" height="42" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="130" y="31" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">[1. 초기화] K-Means++</text>
  <text x="130" y="47" text-anchor="middle" font-size="8.5" fill="var(--color-text-muted, #64748b)">초기 중심점 상호 간 거리 최대화</text>

  <line x1="240" y1="36" x2="275" y2="36" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-alg)"/>

  <rect x="280" y="15" width="220" height="42" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="390" y="31" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #0f172a)">[2. 할당] 최근접 중심 배정</text>
  <text x="390" y="47" text-anchor="middle" font-size="8.5" fill="var(--color-primary, #0284c7)">c(j) = argmin ||x_j - μ_i||²</text>

  <line x1="390" y1="57" x2="390" y2="70" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-alg)"/>

  <rect x="280" y="72" width="220" height="42" fill="var(--color-surface-card, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1" rx="4"/>
  <text x="390" y="88" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #0f172a)">[3. 갱신] 중심점 재계산</text>
  <text x="390" y="104" text-anchor="middle" font-size="8.5" fill="var(--color-primary, #0284c7)">μ_i = (1 / |C_i|) Σ x</text>

  <line x1="280" y1="93" x2="245" y2="93" stroke="var(--color-primary, #0284c7)" stroke-width="1.5" marker-end="url(#arrow-alg)"/>

  <rect x="20" y="72" width="220" height="42" fill="var(--color-success-light, #dcfce7)" stroke="var(--color-success, #16a34a)" stroke-width="1" rx="4"/>
  <text x="130" y="88" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-success-dark, #15803d)">[4. 수렴] 종료 조건 판정</text>
  <text x="130" y="104" text-anchor="middle" font-size="8.5" fill="var(--color-success-dark, #15803d)">중심 이동 &lt; ε 또는 최대 반복 도달</text>

  <line x1="130" y1="72" x2="130" y2="59" stroke="var(--color-text-muted, #94a3b8)" stroke-width="1.2" stroke-dasharray="3 2" marker-end="url(#arrow-alg)"/>

  <defs>
    <marker id="arrow-alg" markerWidth="5" markerHeight="5" refX="4" refY="2.5" orient="auto">
      <polygon points="0 0, 5 2.5, 0 5" fill="var(--color-primary, #0284c7)"/>
    </marker>
  </defs>
</svg>
</div>

| 단계 | 수행 작업 | 판정 기준 및 수학적 처리 |
|---|---|---|
| **1. 초기화 (Initialization)** | 데이터 공간에서 $k$개의 초기 중심점 선택 | **K-Means++ 방식**: 첫 중심은 무작위 선정 후, 기존 중심과의 거리 제곱($D(x)^2$)에 비례하는 확률로 다음 중심점 선정 (초기 중심 간 거리 최대화) |
| **2. 데이터 할당 (Assignment)** | 모든 데이터 포인트와 $k$개 중심점 간 유클리디안 거리 계산 | $d(x, \mu_i) = \sqrt{\sum_{d=1}^{p} (x_d - \mu_{id})^2}$ 가 최소인 군집으로 인스턴스 배정 |
| **3. 중심점 갱신 (Update)** | 동일 군집에 배정된 모든 데이터 포인트의 각 차원별 산술평균 계산 | 새로운 중심점 $\mu_i$로 좌표 갱신 |
| **4. 수렴 판정 (Convergence)** | 중심점의 이동 거리 또는 SSE의 변화량 측정 | 중심점 이동 거리가 오차 한계(Tolerance, 예: $10^{-4}$) 미만이거나 최대 반복 횟수(Max Iterations) 도달 시 종료 |

#### 한줄 요약

- K-Means는 기댓값-최대화(EM, Expectation-Maximization) 원리에 따라 할당(E-step)과 갱신(M-step)을 반복 수렴시킴

### Ⅳ. 최적 군집 수($k$) 결정을 위한 이중 검증 프레임워크

<div class="itpe-diagram-container" style="max-width: 540px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 120" width="100%" height="auto" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
  <rect x="0" y="0" width="520" height="120" fill="var(--color-surface, #f8fafc)" rx="8" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
  <text x="130" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">1. 엘보우 기법 (Elbow Method)</text>
  <line x1="35" y1="95" x2="225" y2="95" stroke="var(--color-text-muted, #64748b)" stroke-width="1.2"/>
  <line x1="35" y1="95" x2="35" y2="28" stroke="var(--color-text-muted, #64748b)" stroke-width="1.2"/>
  <text x="25" y="32" font-size="8" fill="var(--color-text-muted, #64748b)">SSE</text>
  <text x="220" y="107" font-size="8" fill="var(--color-text-muted, #64748b)">k</text>

  <polyline points="45,35 85,60 125,82 165,88 205,90" fill="none" stroke="var(--color-primary, #0284c7)" stroke-width="2"/>
  <circle cx="125" cy="82" r="4" fill="var(--color-danger, #ef4444)"/>
  <text x="130" y="75" font-size="8" font-weight="bold" fill="var(--color-danger, #ef4444)">변곡점 (k=3)</text>
  <text x="125" y="106" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">k=3</text>

  <text x="385" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-primary-dark, #0369a1)">2. 실루엣 분석 (Silhouette Analysis)</text>
  <line x1="290" y1="95" x2="480" y2="95" stroke="var(--color-text-muted, #64748b)" stroke-width="1.2"/>
  <line x1="290" y1="95" x2="290" y2="28" stroke="var(--color-text-muted, #64748b)" stroke-width="1.2"/>
  <text x="272" y="32" font-size="7.5" fill="var(--color-text-muted, #64748b)">Score</text>
  <text x="475" y="107" font-size="8" fill="var(--color-text-muted, #64748b)">k</text>

  <rect x="315" y="55" width="22" height="40" fill="var(--color-border, #cbd5e1)" rx="2"/>
  <text x="326" y="106" text-anchor="middle" font-size="7.5">2</text>
  <rect x="355" y="40" width="22" height="55" fill="var(--color-success, #16a34a)" rx="2"/>
  <text x="366" y="106" text-anchor="middle" font-size="7.5" font-weight="bold">3</text>
  <text x="366" y="35" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-success, #16a34a)">0.68</text>
  <rect x="395" y="60" width="22" height="35" fill="var(--color-border, #cbd5e1)" rx="2"/>
  <text x="406" y="106" text-anchor="middle" font-size="7.5">4</text>
  <line x1="290" y1="52" x2="480" y2="52" stroke="var(--color-danger, #ef4444)" stroke-width="1" stroke-dasharray="3 2"/>
  <text x="482" y="55" font-size="7" fill="var(--color-danger, #ef4444)">0.5 기준</text>
</svg>
</div>

| 검증 기법 | 측정 지표 및 원리 | 판정 기준 | 한계 및 보완 |
|---|---|---|---|
| **엘보우 기법<br>(Elbow Method)** | $k$를 증가시키며 SSE의 감소율을 그래프로 도식화 | 완만해지기 직전의 꺾이는 변곡점(Elbow Point)을 최적 $k$로 선정 | 완만한 곡선 형태일 경우 명확한 변곡점을 식별하기 어려움 |
| **실루엣 계수<br>(Silhouette Score)** | 군집 내 응집도($a(i)$)와 최근접 이웃 군집과의 분리도($b(i)$) 비율 측정<br>$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$ | - $s(i) \approx 1$: 군집화 완벽<br>- $s(i) \approx 0$: 경계선 위치<br>- $s(i) < 0$: 오분류 (평균 0.5 이상 권장) | 계산 복잡도가 $O(n^2)$으로 대규모 데이터에서 연산 비용 증가 |

#### 한줄 요약

- 최적 $k$는 엘보우 그래프의 변곡점으로 1차 후보군을 좁히고, 실루엣 점수의 평균 및 군집별 편차로 2차 정밀 검증함

### Ⅴ. 비지도 군집화 알고리즘 심층 비교: K-Means vs K-Medoids vs DBSCAN

| 비교 항목 | K-Means | K-Medoids (PAM) | DBSCAN |
|---|---|---|---|
| **군집화 유형** | 분할 기반 (Partitioning) | 분할 기반 (Partitioning) | 밀도 기반 (Density-based) |
| **중심 기준** | 가상의 산술평균점 ($\mu$, Mean) | 군집 내 실제 중앙 데이터 (Medoid) | 데이터 밀집도 (Core, Border, Noise) |
| **사전 $k$ 지정** | 필수 ($k$ 사전 입력) | 필수 ($k$ 사전 입력) | 불필요 (Epsilon, MinPts 지정) |
| **군집 형태** | 볼록한 구형(Spherical) 군집만 가능 | 구형 군집 중심 | 임의의 기하학적 형태(초승달, 도넛) 가능 |
| **이상치 처리** | 이상치에 매우 취약 (중심 왜곡) | 이상치에 강건 (Robust) | 노이즈(Noise)를 이상치로 자동 분리 |
| **시간복잡도** | $O(nkt)$ (가장 빠름) | $O(k(n-k)^2)$ (느림) | $O(n \log n)$ (공간 인덱스 활용 시) |

#### 한줄 요약

- 대규모 수치형 구형 데이터는 K-Means, 이상치가 많은 데이터는 K-Medoids, 복잡한 비선형 분포 및 노이즈 검출은 DBSCAN이 적합함

### Ⅵ. K-Means 실무 적용 시 주요 실패 요인 및 엔지니어링 대책

| 문제 상황 | 근본 원인 | 실무 대책 | 기대 효과 |
|---|---|---|---|
| **특정 특성(Feature)의 군집 지배** | 속성 간 스케일 차이 (예: 연봉 1억 vs 연령 30세 유클리디안 거리 왜곡) | StandardScaler 또는 MinMaxScaler를 통한 사전 데이터 표준화 필수 적용 | 모든 피처의 동등한 가중치 반영 |
| **로컬 옵티멈 수렴에 따른 결과 왜곡** | 무작위 초기 중심 설정 시 가까운 위치에 중심이 중복 배치 | Scikit-learn의 `init='k-means++'`, `n_init=10` 파라미터 적용 (10회 실행 중 최적해 선택) | 전역 최적해에 근접한 안정적 군집 |
| **극단 이상치로 인한 중심점 쏠림** | 금융 사기 거래, 비정상 고액 결제 등 극단치가 평균을 편향 | 군집화 이전 Isolation Forest 또는 Z-Score로 이상치 선행 제거 | 순수 일반 고객 세그먼트 정상화 |
| **대용량 데이터셋 메모리 초과** | 수천만 건 데이터에 대해 전체 행렬 거리를 메모리에 적재 | 미니배치 K-Means (Mini-Batch K-Means) 알고리즘 도입 | 90% 이상의 메모리 절감 및 학습 속도 극대화 |

#### 한줄 요약

- 데이터 표준화(Scaling), K-Means++ 초기화, 사전 이상치 제거는 K-Means 파이프라인의 필수 전처리 단계임

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 머신러닝 엔지니어링에서 수학적 최적해(Global Optimum)와 비즈니스 수용성(Business Feasibility) 사이에는 항상 깊은 간극이 존재한다. 엘보우 기법과 실루엣 분석으로 수학적으로 도출된 최적 군집 수가 $k=8$이라 하더라도, 마케팅 현업 부서에서 동시에 기획·운영할 수 있는 세그먼트 캠페인이 3개뿐이라면 해당 8개 군집 모델은 실무에서 즉시 사장된다.
>
> **[나라면 이렇게 쓴다]**
> 실무 파이프라인 구축 시에는 RFM(Recency, Frequency, Monetary) 피처를 로그 변환 및 StandardScaler로 표준화한 후 K-Means++ 모델을 적용하되, 최적 $k$ 탐색 범위를 현업 실행 역량($k \in [3, 5]$)으로 제한하고, 군집별 핵심 변수 평균 프로파일을 시각화하여 비즈니스 페르소나(Persona)를 현업과 공동 검증하겠다. 또한 확정된 군집 모델을 Feature Store 및 실시간 추론 API와 연계하여 신규 유입 고객의 세그먼트를 10ms 이내 판정하는 실시간 타겟 마케팅 아키텍처를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 피처 스케일 불균형 및 K-Means의 이상치 왜곡 취약성으로 인해 군집 중심 편향 및 현업 비즈니스 수용 불능 발생.
- **대응 (개선 방안)**: 피처 표준화 및 Isolation Forest 사전 정제 파이프라인 구축, K-Means++ 적용 및 현업 운영 제약을 반영한 $k$ 결정.
- **검증 (검증 기준)**: 실루엣 점수 0.5 이상 확보 및 군집별 비즈니스 유의성(고객 행동 차이 $p < 0.01$) 통계적 검증.
- **효과 (실행 효과)**: 고객 세분화 정확도 40% 향상, 타겟 마케팅 전환율(CVR) 2.5배 개선 및 실시간 서빙 지연 10ms 이내 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">현행 한계</div>
    <div class="itpe-flow-desc">스케일 왜곡 및 이상치로 인한 중심 편향과 비즈니스 비수용</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">개선 방안</div>
    <div class="itpe-flow-desc">표준화·정제 파이프라인 + K-Means++ 및 비즈니스 제약 k 선정</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">검증 기준</div>
    <div class="itpe-flow-desc">실루엣 계수 0.5 이상 및 군집 간 행동 유의차(p &lt; 0.01) 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">실행 효과</div>
    <div class="itpe-flow-desc">마케팅 전환율 2.5배 향상 및 세그먼트 추론 레이턴시 10ms 보장</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- 제129회 1교시 5번: K-Means Clustering과 DBSCAN 개념, 구성요소, 장/단점
- [Scikit-learn User Guide, K-means Clustering](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [Arthur, D., & Vassilvitskii, S. (2007). k-means++: The advantages of careful seeding](https://theory.stanford.edu/~sergei/papers/kMeansPP-soda.pdf)

## 연결 토픽

- [군집분석](./005_cluster_analysis/) · [이상치](./010_outlier/) · [차원 축소(PCA·MDS)](./069_dimensionality_reduction_pca_mds/) · [텍스트 마이닝](./015_text_mining/)
