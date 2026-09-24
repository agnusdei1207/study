---
sidebar:
  order: 122
  label: "122. 다차원척도법 (MDS)"
  badge:
    text: "기초"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 122
title: "다차원척도법(MDS, Multidimensional Scaling)의 거리 보존 원리와 스트레스(Stress) 적합도 진단"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "122"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>다차원척도법</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Distance Matrix (Left) -->
  <rect x="20" y="25" width="200" height="150" rx="8" fill="#3b82f6" fill-opacity="0.08" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="120" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 객체 간 거리/비유사도 행렬</text>
  <rect x="35" y="60" width="170" height="100" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="50" y="80" font-size="10" font-family="monospace" fill="#64748b">     A   B   C   D</text>
  <text x="50" y="100" font-size="10" font-family="monospace" fill="#1e293b">A [  0   2   8   9 ]</text>
  <text x="50" y="118" font-size="10" font-family="monospace" fill="#1e293b">B [  2   0   7   8 ]</text>
  <text x="50" y="136" font-size="10" font-family="monospace" fill="#1e293b">C [  8   7   0   3 ]</text>
  <text x="50" y="154" font-size="10" font-family="monospace" fill="#1e293b">D [  9   8   3   0 ]</text>

  <!-- Transform Arrow -->
  <path d="M 225 100 L 275 100" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow122)"/>
  <text x="250" y="92" text-anchor="middle" font-size="10" fill="#64748b">MDS 투영</text>

  <!-- Perceptual Map (Right) -->
  <rect x="285" y="25" width="215" height="150" rx="8" fill="#10b981" fill-opacity="0.08" stroke="#10b981" stroke-width="1.5"/>
  <text x="392" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">2. 2차원 지각도 (Perceptual Map)</text>
  <!-- Axes -->
  <line x1="305" y1="110" x2="480" y2="110" stroke="#cbd5e1" stroke-width="1"/>
  <line x1="392" y1="58" x2="392" y2="160" stroke="#cbd5e1" stroke-width="1"/>
  <!-- Points -->
  <circle cx="340" cy="85" r="4" fill="#2563eb"/>
  <text x="340" y="78" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">A</text>
  <circle cx="355" cy="95" r="4" fill="#2563eb"/>
  <text x="365" y="95" font-size="10" font-weight="bold" fill="#2563eb">B</text>
  <circle cx="450" cy="125" r="4" fill="#059669"/>
  <text x="450" y="120" text-anchor="middle" font-size="10" font-weight="bold" fill="#059669">C</text>
  <circle cx="465" cy="140" r="4" fill="#059669"/>
  <text x="475" y="140" font-size="10" font-weight="bold" fill="#059669">D</text>

  <!-- Bottom Stress Diagnosis -->
  <rect x="20" y="190" width="480" height="55" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">적합도 평가 지표: 스트레스(Stress) &lt; 0.05 우수, &gt;= 0.15 부적합</text>
  <text x="260" y="232" text-anchor="middle" font-size="10" fill="#78350f">고차원의 비유사성 거리를 2차원 평면 좌표 간 유클리드 거리로 최대한 일치 보존</text>

  <defs>
    <marker id="arrow122" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **개체들 간의 유사성/비유사성(거리) 데이터를 기반으로 원본 고차원의 복잡한 다변량 관계를 2차원 또는 3차원 공간상의 점(좌표)으로 축소 배치하여 인간이 직관적으로 이해할 수 있는 공간 지각도(Perceptual Map)를 생성하고, 원본 거리와 축소 거리 간의 불일치를 스트레스(Stress) 값으로 최소화하는 비지도 시각화 기법**
- 암기: `계-비-스-지` (계량적 MDS, 비계량적 MDS, 스트레스 값, 지각도) / `영-오-일-일오` (Stress 판정 기준: 0.05 이하 우수, 0.10 보통, 0.15 이상 열악)
- 판단축:
  - **계량적 MDS (Metric)**: 거리의 절대적 수치 비율을 보존하려는 등간/비율 척도 기반 변환
  - **비계량적 MDS (Non-metric)**: 거리의 절대값이 아닌 대소 서열(Rank Order) 순서만을 보존하는 서열 척도 기반 변환 (Shepard 다이어그램 활용)
  - **MDS vs PCA**: 거리 보존(Distance Preserving) vs 분산 극대화(Variance Maximizing)
- 주의: MDS는 좌표 공간상에 점들을 배치할 뿐 생성된 X축과 Y축에 자동으로 이름표(레이블)를 부여하지 않으므로, 축의 비즈니스적 의미는 분석가의 도메인 지식이나 다변량 회귀분석(속성 피팅)을 통해 객관화해야 함
---

## 1교시 예상문제 (10점)

> 다차원척도법(MDS, Multidimensional Scaling)의 거리 보존 원리와 스트레스(Stress) 적합도 진단의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 개체 간의 거리/비유사도 행렬을 입력받아 원본 거리를 최대한 보존하면서 2차원/3차원 평면 좌표로 투영하는 비지도 시각화 기법 |
| **2. 2대 유형** | - **계량적(Metric)**: 구간/비율 척도 기반 실제 거리 비율 보존<br/>- **비계량적(Non-metric)**: 서열 척도 기반 거리 순위(단조성) 보존 (Shepard Plot) |
| **3. Stress 판정** | - 수식: $\text{Stress} = \sqrt{\sum (d_{ij} - \hat{d}_{ij})^2 / \sum d_{ij}^2}$<br/>- 기준: 0.05 이하(우수), 0.10(양호), 0.15 이상(부적합) |
| **4. 핵심 차별점** | PCA가 분산 극대화 선형 변환인 반면, MDS는 쌍대 거리 보존 기하학적 복원에 집중 |
---

### 핵심 관계

| 비교 항목 | 계량적 MDS (Metric MDS) | 비계량적 MDS (Non-metric MDS) |
|:---|:---|:---|
| **입력 데이터 척도** | **구간/비율 척도** (실제 물리적 거리, 수치 유사도) | **순위/서열 척도** (선호 순위, 상대적 친숙도) |
| **거리 보존 방식** | 원본 거리의 수치적 크기와 선형 비례 관계 유지 | 거리의 대소 서열($d_{ij} < d_{kl} \Rightarrow \hat{d}_{ij} < \hat{d}_{kl}$) 단조성 보존 |
| **목적 함수** | Classical Scaling (Strain) 최소화 | Kruskal의 Stress (단조 변환 잔차) 최소화 |
| **적합성 평가 도구** | 고유값 기여율 및 잔차 상관계수 | **셰퍼드 다이어그램 (Shepard Diagram)** 단조성 |
| **주요 적용 사례** | 도시 간 실제 이동 거리 지도 복원, 유전자 서열 거리 | 소비자 브랜드 선호도, 감성 품질 평가, 심리 척도 |

---

## 2~4교시 예상문제 (25점)

> 다차원척도법(MDS, Multidimensional Scaling)의 개념과 유형(계량적, 비계량적)을 설명하고, 모형의 적합도 판정 기준인 스트레스(Stress)의 계산 원리와 해석 기준 및 마케팅/데이터 분석에서의 활용 방안을 기술하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 고차원 인식을 공간 좌표로 복원하는 다차원척도법 개요

#### 한줄 요약: 객체 간의 거리나 유사도 행렬만을 입력받아 2차원 평면의 점(Point) 좌표로 복원하여 지각도를 산출하는 비지도 기법

- **배경**:
  - 소비자의 브랜드 이미지나 심리적 선호도는 수십 개의 복잡한 잠재 속성으로 얽혀 있어 수치형 설문만으로 구조를 파악하기 어려움
  - 객체 간 "어느 것이 더 비슷한가?"라는 단순 비교 데이터로부터 객체의 공간적 상대 위치를 시각화할 수 있는 수리통계적 방법론 요구
- **정의**: $n$개 개체 간의 쌍대 거리(Proximity/Dissimilarity) 행렬을 기반으로, 저차원(주로 2D/3D) 유클리드 공간상에 각 개체의 좌표를 산출하여 원본 거리 관계를 최대한 보존하는 차원 축소 기법
- **핵심 목표**: 고차원 거리 행렬 $D$와 저차원 좌표 간 거리 행렬 $\hat{D}$ 사이의 불일치(오차)를 최소화하는 최적 좌표계 발견

### Ⅱ. MDS의 2대 핵심 유형: 계량적 vs 비계량적 MDS

#### 한줄 요약: 거리의 정량적 크기를 보존하는 계량적(Metric) MDS와 서열 순서만 보존하는 비계량적(Non-metric) MDS

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1: Metric MDS -->
  <rect x="25" y="20" width="225" height="140" rx="8" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="137" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 계량적 MDS (Metric MDS)</text>
  <text x="137" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">- 입력: 등간척도 / 비율척도</text>
  <text x="137" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">- 원리: 실제 거리 수치 비율 보존</text>
  <text x="137" y="110" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">- 알고리즘: 고전적 주좌표분석(PCoA)</text>
  <text x="137" y="135" text-anchor="middle" font-size="10" fill="#64748b">거리의 절대적 차이 선형 반영</text>

  <!-- Box 2: Non-metric MDS -->
  <rect x="270" y="20" width="225" height="140" rx="8" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="382" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">2. 비계량적 MDS (Non-metric MDS)</text>
  <text x="382" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">- 입력: 서열척도 (순위 데이터)</text>
  <text x="382" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">- 원리: 순서(Rank Order) 단조성 보존</text>
  <text x="382" y="110" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">- 알고리즘: Kruskal 알고리즘</text>
  <text x="382" y="135" text-anchor="middle" font-size="10" fill="#64748b">Shepard 다이어그램 단조 회귀</text>
</svg>
</div>

| 비교 항목 | 계량적 MDS (Metric MDS) | 비계량적 MDS (Non-metric MDS) |
|:---|:---|:---|
| **입력 데이터 척도** | **구간/비율 척도** (실제 물리적 거리, 수치 유사도) | **순위/서열 척도** (선호 순위, 상대적 친숙도) |
| **거리 보존 방식** | 원본 거리의 수치적 크기와 선형 비례 관계 유지 | 거리의 대소 서열($d_{ij} < d_{kl} \Rightarrow \hat{d}_{ij} < \hat{d}_{kl}$) 단조성 보존 |
| **목적 함수** | Classical Scaling (Strain) 최소화 | Kruskal의 Stress (단조 변환 잔차) 최소화 |
| **적합성 평가 도구** | 고유값 기여율 및 잔차 상관계수 | **셰퍼드 다이어그램 (Shepard Diagram)** 단조성 |
| **주요 적용 사례** | 도시 간 실제 이동 거리 지도 복원, 유전자 서열 거리 | 소비자 브랜드 선호도, 감성 품질 평가, 심리 척도 |

### Ⅲ. 모형의 적합도 판정 기준: 스트레스(Stress)

#### 한줄 요약: 원본 고차원 거리와 저차원 평면 좌표 간 거리의 불일치 잔차를 정규화한 손실 함수

1. **스트레스 수식 (Kruskal's Stress-1)**:

$$\text{Stress} = \sqrt{ \frac{\sum_{i < j} (d_{ij} - \hat{d}_{ij})^2}{\sum_{i < j} d_{ij}^2} }$$

  - $d_{ij}$: 원본 고차원 공간에서의 개체 $i$와 $j$ 사이의 실제 거리 (또는 단조 변환 거리)
  - $\hat{d}_{ij}$: 저차원 지각도상에 배치된 개체 $i$와 $j$ 사이의 유클리드 좌표 거리
  - 분자는 거리 차이의 제곱합(불일치 오차), 분모는 척도 불변성을 위한 정규화 인수
2. **스트레스 값에 따른 모형 적합도 판정 기준**:

| 스트레스(Stress) 값 | 적합도 판정 | 실무 해석 및 조치 가이드 |
|:---|:---:|:---|
| **0.00** | 완전 일치 (Perfect) | 원본 거리와 완벽히 일치 (인위적 데이터 의심) |
| **0.05 이하** | **우수 (Excellent)** | 왜곡 없이 신뢰할 수 있는 매우 이상적인 지각도 |
| **0.05 ~ 0.10** | **양호 (Good)** | 실무 분석에서 채택 가능한 신뢰도 수준 |
| **0.10 ~ 0.15** | **보통 (Fair)** | 대략적인 군집 형태는 파악 가능하나 미세 거리 왜곡 존재 |
| **0.15 이상** | **열악 (Poor / Unacceptable)** | 2차원 투영 왜곡 극심 $\rightarrow$ 3차원으로 차원 확대 필요 |

### Ⅳ. MDS vs PCA vs t-SNE 3대 차원축소 기법 비교

#### 한줄 요약: 거리 보존의 MDS, 분산 극대화의 PCA, 국소 이웃 보존의 t-SNE

| 비교 항목 | MDS | PCA | t-SNE |
|:---|:---|:---|:---|
| **학습 유형** | 비지도 거리 축소 | 비지도 선형 변환 | 비지도 비선형 매니폴드 |
| **입력 데이터** | **쌍대 거리/비유사도 행렬 ($n \times n$)** | 피처-샘플 데이터 행렬 ($n \times p$) | 샘플 데이터 행렬 또는 확률 행렬 |
| **최적화 목표** | **점과 점 사이의 거리 불일치 최소화** | **데이터의 전체 분산 극대화** | **국소적 이웃 확률 분포(KL-발산) 최소화** |
| **해석 가능성** | 축 해석 주관적 (거리 관계만 유효) | 주성분 고유벡터로 축 해석 명확 | 축의 의미 없음 (군집 시각화 전용) |
| **주요 용도** | 마케팅 브랜드 포지셔닝 맵, 심리학 | 차원 축소 전처리, 노이즈 제거 | 고차원 딥러닝 임베딩 군집 시각화 |

### Ⅴ. MDS 분석 파이프라인 및 지각도 도출 절차

#### 한줄 요약: 거리 행렬 구축 $\rightarrow$ 저차원 초기 좌표 배치 $\rightarrow$ Stress 최소화 반복 최적화 $\rightarrow$ 지각도 시각화

1. **거리 행렬 산출**: 설문조사(유사도 7점 척도)나 고차원 벡터 데이터로부터 유클리드, 맨해튼, 코사인 거리를 계산하여 $n \times n$ 행렬 구성
2. **초기 저차원 좌표 설정**: 무작위 난수 배치 또는 고전적 MDS(주좌표분석 고유값 분해) 결과를 초기 좌표로 지정
3. **반복 최적화 (SMACOF 알고리즘)**: 저차원 좌표 거리와 원본 거리의 오차를 계산하고, 경사하강법으로 Stress를 최소화하는 방향으로 좌표를 반복 갱신
4. **차원 수 결정 (Scree Plot)**: 차원 수(1차원, 2차원, 3차원)를 늘려가며 Stress 값의 급격한 하강이 멈추는 엘보우 포인트(Elbow Point) 선택 (통상 2차원 채택)
5. **공간 지각도 시각화 및 군집 도출**: 2차원 평면에 개체들을 산점도로 시각화하고 근접 군집을 식별

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 축 레이블링 주관성 배제(속성 피팅), 국소 최솟값 회피, 3차원 확장

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **축(Axis) 해석의 독단적 주관성** | MDS는 수학적으로 좌표만 도출할 뿐 축의 속성 명칭을 제공하지 않음 | MDS 좌표를 종속변수로 두고 원본 속성 변수들과 **다변량 회귀분석(Property Fitting)**을 수행하여 통계적으로 유의한($p < 0.01$) 속성 방향 벡터 표시 |
| **실행 시마다 지각도 형태 왜곡** | 경사하강법 탐색 시 초기 무작위 좌표에 의해 국소 최솟값(Local Minimum)에 갇힘 | 고전적 MDS(Classical PCoA)의 해석적 해를 초기 좌표로 주입하는 SMACOF 알고리즘 적용 |
| **2차원 Stress가 0.20 초과** | 평가 대상의 잠재 속성이 3개 이상 분산되어 2차원 평면 표현 한계 봉착 | 3차원 MDS로 확장하여 3D 인터랙티브 차트로 시각화하거나 불필요한 이질 개체 제거 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> MDS는 "데이터 간의 거리(Distance)만 알고 속성(Feature)은 모를 때" 진가를 발휘하는 독보적인 분석 도구이다.
> 소비자가 "A차와 B차는 비슷한데 C차는 다르다"고 느낄 때, 소비자는 자신이 연비 때문에 그렇게 느끼는지 디자인 때문인지 말로 설명하지 못한다.
> MDS는 이러한 **인간의 잠재적 멘탈 모델(Mental Model)을 수학적 공간 좌표계로 복원**해내는 강력한 무기이다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "현대 빅데이터 및 LLM 임베딩 공간 분석에서의 MDS 활용"을 제언하겠다. 수천 차원의 고밀도 벡터 공간에서 임베딩 간의 코사인 거리 행렬을 MDS로 축소하여 의미적 지식 맵을 구축하는 방법론을 제시하고, 축 해석의 한계를 극복하기 위해 다변량 속성 피팅(Property Fitting)을 통계적 품질 기준으로 수립하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 비정형 설문 및 다변량 심리 척도 데이터에서 잠재적 인식 구조를 시각화하기 위해 다차원척도법 도입이 필수적임.
- **대응**:
  1. **척도별 기법 분기**: 수치형 거리는 계량적 MDS, 선호 서열 데이터는 Shepard 다이어그램 기반의 비계량적 MDS 적용.
  2. **속성 피팅 객관화**: 축의 임의 해석을 방지하기 위해 속성 변수와의 회귀분석을 통해 방향 벡터를 지각도에 병기.
  3. **차원 결정 표준화**: Scree Plot 분석을 통해 Stress $\le 0.10$을 만족하는 최적 차원(2D 또는 3D) 확정.
- **검증**: Kruskal Stress-1 0.10 이하 달성 및 Shepard 다이어그램의 단조 증가 적합도 검증.
- **효과**: 경쟁 제품 간 브랜드 포지셔닝 명확화 및 시장 내 미충족 니즈(White Space) 식별.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">다속성 잠재 구조 파악 불가, 직관적 브랜드 지각도 부재</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">MDS 거리 보존 좌표 투영 및 속성 피팅 회귀 결합</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">Stress &lt; 0.10 만족, Shepard 다이어그램 단조성 확인</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">소비자 멘탈 모델 시각화 및 최적 마케팅 포지셔닝 수립</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제123회 정보관리 1교시: 다차원척도법(MDS)의 개념과 유형(계량적/비계량적) 및 적합도 판정 척도인 스트레스(Stress)
- **검증 출처**:
  - Joseph B. Kruskal, "Multidimensional scaling by optimizing goodness of fit to a nonmetric hypothesis", Psychometrika
  - Trevor Hastie et al., "The Elements of Statistical Learning (2nd Edition)", Springer
---

## 연결 토픽

- 상위 토픽: [03-069 차원 축소(PCA·MDS)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/069_dimensionality_reduction_pca_mds.md)
- 연관 토픽: [03-016 데이터 시각화](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/016_data_visualization.md), [03-005 군집 분석](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/005_cluster_analysis.md)
