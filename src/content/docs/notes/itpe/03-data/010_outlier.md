---
title: "이상치(탐지 기법·노이즈 구분 포함)"
author: "Codex"
date: "2026-09-20T19:54:48+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="데이터 분석에서 데이터 전처리 및 이상치 탐지로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 전처리·정제</span>
  <strong>이상치(탐지 기법·노이즈 구분 포함)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 데이터의 일반적 분포나 정상 패턴에서 현저하게 벗어난 관측치로, 단순 측정 오류(노이즈)일 수도 있고 이상금융거래(FDS)나 시스템 장애 같은 고가치 신호(Novelty)일 수도 있는 핵심 데이터
- 3대 탐지: 통계적 기법(Z-Score, IQR Boxplot), 밀도·거리 기법(Mahalanobis, LOF), 머신러닝 기법(Isolation Forest, One-Class SVM)
- 4대 처리: 삭제(Trimming), 대체(Imputation), 클리핑(Winsorizing), 강건 모형(Robust Estimation)

<div class="itpe-flow-map" role="img" aria-label="이상치 및 노이즈 탐지에서 분석 목적별 처리 흐름">
  <div class="itpe-flow-node"><strong>원천 데이터 수집</strong><div class="itpe-step-detail"><span>대상</span><span>센서 · 금융 거래 로그 · 의료 데이터</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>이상치 vs 노이즈 구분</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>노이즈(Noise)</strong><span>무작위 무의미 변동 · 백색 잡음 (제거 대상)</span></div>
      <div class="itpe-flow-branch"><strong>이상치(Outlier)</strong><span>분포 이탈 관측치 · 오류 or 핵심 신호 판정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>탐지 알고리즘 적용</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>단변량</strong><span>$IQR = Q3 - Q1$, $Z\text{-}Score > 3$</span></div>
      <div class="itpe-flow-branch"><strong>다변량</strong><span>Mahalanobis 거리 · LOF (국소 밀도)</span></div>
      <div class="itpe-flow-branch"><strong>ML 기반</strong><span>Isolation Forest · Autoencoder 복원오차</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>분석 목적별 처리 (삭제 / 대체 / 윈저화 / FDS 격리)</strong></div>
</div>

## 예상문제

<details><summary>핵심 용어</summary>

- `IQR(Interquartile Range)`: 사분위 범위로 단변량 극단값을 판정
- `LOF(Local Outlier Factor)`: 이웃과의 국소 밀도 차이로 이상 정도를 산출
- `Isolation Forest`: 짧은 분할 경로를 이용해 이상치를 격리
- `Winsorizing`: 극단값을 정한 경계값으로 치환

</details>

> 데이터 전처리 및 이상 징후 탐지를 위한 이상치(Outlier)와 노이즈(Noise)의 개념 및 차이점을 비교하고, 통계적·거리/밀도·머신러닝 기반 3대 탐지 알고리즘(IQR, LOF, Isolation Forest) 및 분석 목적에 따른 4대 처리 전략을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **이상치 탐지(Outlier Detection)** | 비정상 패턴과 이상 데이터를 자동으로 식별하는 알고리즘 파이프라인 | Ⅲ 탐지 기법 |
| **노이즈(Noise)** | 데이터 측정 및 통신 과정에서 발생하는 무작위 오차(Random Error) 및 필터링 기법 | Ⅱ 차이 비교 |

## Ⅰ. 데이터 왜곡의 주범이자 사기 탐지의 신호탄, 이상치의 개요

> 이상치는 정상 분포에서 극단적으로 이탈한 관측치로, 단순 제거 대상인 노이즈와 달리 고가치 정보를 내포할 수 있음.

- 정의: 대부분의 데이터가 따르는 정상적 분포나 규칙에서 현저하게 벗어나, 다른 메커니즘에 의해 생성된 것으로 의심되는 관측치 (Hawkins, 1980)
- 양면성:
  1. **데이터 품질 저하 요인**: 평균, 분산, 회귀계수를 극단적으로 왜곡하여 머신러닝 모형의 일반화 성능을 파괴
  2. **비즈니스 핵심 가치 요인**: 신용카드 부정사용(FDS), 네트워크 침입(IDS), 제조 설비 고장 예지 등 이상치 자체가 모형화의 핵심 타깃
- 분류: 단일 변수 기준의 글로벌 이상치(Global), 특정 조건 하에서의 맥락적 이상치(Contextual), 순차적 패턴에 의해 판정되는 집단적 이상치(Collective)

## Ⅱ. 이상치(Outlier) vs 노이즈(Noise) 비교

> 노이즈는 제거해야 할 무작위 오차이고, 이상치는 의미 분석이 필요한 식별 가능한 극단치임.

| 비교 기준 | 이상치 (Outlier) | 노이즈 (Noise) |
|---|---|---|
| **개념적 본질** | 정상 범위에서 크게 벗어난 '유효하거나 유의미한' 관측값 | 측정, 전송, 입력 과정에서 유입된 '무작위적 무의미한' 오차 |
| **정보 가치** | 잠재적 고가치 신호(사기, 고장, 특이현상) 내포 가능 | 분석에 방해만 되는 순수 불순물 (Zero Value) |
| **발생 원인** | 희귀 이벤트 발생, 시스템 침입, 구조적 변경 | 센서 정밀도 한계, 통신 잡음, 환경 진동 |
| **처리 기본 원칙** | 원인 규명 선행 $\to$ 도메인 목적에 따라 보존/격리/변환 | 평활화(Smoothing), 필터링(Kalman 등)으로 사전 제거 |
| **대표 사례** | 1회 1,000만원 결제(이상치), 제조 설비 진동 급증 | 센서 계측 시 $\pm 0.05$ 미세 진동 오차 |

## Ⅲ. 이상치 탐지 3대 핵심 알고리즘 체계

> 단변량 통계(IQR), 다변량 밀도(LOF), 트리 격리(Isolation Forest)를 결합하여 탐지함.

<div class="itpe-pipeline" role="img" aria-label="이상치 3대 탐지 알고리즘">
  <div class="itpe-pipeline-node"><strong>통계 기반</strong><div class="itpe-step-detail"><span>방식</span><span>IQR · Z-Score</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>거리·밀도 기반</strong><div class="itpe-step-detail"><span>방식</span><span>Mahalanobis · LOF</span></div></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>머신러닝 기반</strong><div class="itpe-step-detail"><span>방식</span><span>Isolation Forest · Autoencoder</span></div></div>
</div>

| 기법 | 핵심 동작 수식 및 원리 | 주요 특징 및 장단점 |
|---|---|---|
| **IQR (사분위수 범위)** | 하한: $Q_1 - 1.5 \times IQR$, 상한: $Q_3 + 1.5 \times IQR$<br>($IQR = Q_3 - Q_1$) | 정규분포 가정이 불필요하고 이상치에 강건(Robust)하나, 1차원 단변량에 한정됨 |
| **Z-Score / ESD** | $Z = \frac{x - \mu}{\sigma}$, $|Z| > 3$ 시 이상치 판정 | 계산이 단순하나 평균과 표준편차 자체가 극단치에 왜곡되는 취약성 존재 |
| **마할라노비스 거리** | $D_M(x) = \sqrt{(x-\mu)^T \Sigma^{-1} (x-\mu)}$ | 변수 간 상관관계를 반영한 다차원 거리 측정, 고차원 역행렬 계산 필요 |
| **LOF (Local Outlier Factor)** | 데이터 포인트 $p$의 국소 도달 밀도와 $k$-최근접 이웃들의 밀도 비율 | 값이 클수록 주변보다 희박함을 뜻하나 임계값은 오염률·검증자료·업무비용으로 결정 |
| **Isolation Forest** | 무작위 축·분할점으로 만든 트리에서 짧은 평균 경로를 이상 신호로 사용 | 비용은 트리 수·서브샘플 크기·깊이·특성 수에 좌우되므로 처리량 실측 필요 |

## Ⅳ. 이상치 탐지 및 처리 5단계 절차

> 탐지 후 무조건 삭제하지 않고 원인 분류 후 도메인 규칙에 따라 처리 방식을 확정함.

| 단계 | 활동 내용 | 통제 기준 |
|---|---|---|
| **1. 탐색적 분석 (EDA)** | 산점도(Scatter Plot), 상자수염그림(Boxplot), 왜도/첨도 확인 | 데이터 왜곡 및 극단치 존재 시각적 확인 |
| **2. 탐지 알고리즘 실행** | 단변량(IQR) 및 다변량(Isolation Forest) 파이프라인 가동 | 이상치 후보군(Anomaly Candidate) 추출 |
| **3. 원인 분류 (Root Cause)** | 단순 입력/시스템 오류인지, 실제 비즈니스 사건인지 도메인 검증 | 오류(Error) vs 유효 극단치(Valid Event) 분리 |
| **4. 이상치 처리 전략 적용** | 삭제, 대체, 클리핑, 강건 모델링 중 목적에 맞게 적용 | 데이터 손실 최소화 및 모델 왜곡 방지 |
| **5. 모델 영향도 검증** | 처리 전후의 모델 성능(MAE, RMSE, F1-Score) 및 계수 안정성 대조 | 과대적합 방지 및 일반화 능력 검증 |

## Ⅴ. 분석 목적에 따른 4대 이상치 처리 전략

> 인과 분석은 윈저화나 삭제를, 이상 탐지는 별도 모델 분리를, 머신러닝은 강건 회귀를 선택함.

| 처리 전략 | 구체적 처리 기법 | 적합한 분석 상황 | 주의사항 및 트레이드오프 |
|---|---|---|---|
| **삭제 (Trimming)** | 판정된 이상치 레코드를 분석 데이터셋에서 영구 제외 | 명백한 시스템 오류, 통계적 오염 제거 필요 시 | 표본 크기 감소 및 표본 선택 편향(Selection Bias) 유발 |
| **대체 (Imputation)** | 정상 범위의 평균, 중앙값(Median), 최빈값 또는 보간법으로 대체 | 결측치와 결합된 오류 데이터 | 데이터 분산이 인위적으로 축소되어 표준오차 과소추정 |
| **클리핑 (Winsorizing)** | 상한·하한 임계치를 벗어난 값을 경계값으로 치환 | 금융 데이터 등 극단값 영향 완화가 필요할 때 | 꼬리 분포와 평균·분산을 바꾸므로 원본 보존·민감도 비교 필요 |
| **강건 모델링 (Robust)** | 이상치에 둔감한 Huber Loss, RANSAC, 트리 앙상블 모형 적용 | 이상치를 삭제할 수 없으나 예측 성능을 유지해야 할 때 | 이상치의 영향력을 수식적으로 완화(Down-weighting) |

## Ⅵ. 실무 고려사항 및 장애 대책

> 자동 삭제로 인한 핵심 사기 신호 유실과 차원의 저주를 파이프라인 격리로 방어함.

- 적용 상황: 카드 결제 FDS(이상거래탐지시스템) 및 반도체 공정 센서 이상 감지

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **사기 거래 데이터 오삭제** | 전처리 엔지니어가 이상 거래를 단순 노이즈로 오인하여 일괄 Trimming | 이상치 탐지 파이프라인과 지도학습 분류 파이프라인 분리 | FDS 학습용 핵심 불균형 데이터 보존 |
| **고차원 센서 거리 균일화** | 수백 개 센서 변수 동시 투입 시 거리 분별력 약화 | 차원 축소·특성 선택 후 Isolation Forest·Autoencoder 후보를 검증자료로 비교 | 데이터량·정상학습 가정에 맞는 탐지기 선택 |
| **스트리밍 지연 발생** | 초당 수만 건 트래픽에 복잡한 군집 기반 탐지 알고리즘 적용 | 경량화된 Half-Space Trees 또는 온라인 Isolation Forest 적용 | 실시간성(Latency < 10ms) 보장 |

## Ⅶ. 결론 및 기술사적 제언

> 이상치 처리는 기계적 정제가 아니라 도메인 지식과 머신러닝이 결합된 의사결정 파이프라인이어야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 데이터 엔지니어링에서 가장 위험한 행위는 탐지된 이상치를 '평균을 갉아먹는 귀찮은 존재'로 보고 DELETE 문을 날리는 것임. 이상치는 비즈니스의 사각지대, 새로운 고객 세그먼트, 또는 시스템 장애의 전조 증상일 가능성이 높음.
- 나라면: 데이터 전처리 단계에서 '이상치 격리 큐(Anomaly Quarantine Queue)'를 구축하여, 탐지된 이상치 데이터를 원천 보존하고, SHAP/LIME 기반 XAI(설명가능 인공지능)를 연동해 이상치로 판정된 원인 피처를 현업 분석가에게 대시보드로 자동 제공하는 체계를 수립하겠음.

### 실전 답안용 기술사적 제언
- 판정: 오류와 유효 사건을 구분한 뒤 처리
- 대안: 원본 보존·격리 큐·도메인 검토 결합
- 검증: 탐지 정밀도·재현율과 처리 전후 모델 성능 측정
- 효과: 사기·고장 신호 유실 방지
<div class="itpe-flow-map" role="img" aria-label="이상치 처리 제언"><div class="itpe-flow-node"><strong>현행 한계</strong><span>문제: 탐지 즉시 삭제</span></div><div class="itpe-flow-arrow">↓</div><div class="itpe-flow-node"><strong>개선안</strong><span>대안: 원본 격리·도메인 판정</span></div><div class="itpe-flow-arrow">↓</div><div class="itpe-flow-node is-current"><strong>검증·효과</strong><span>판정: 정밀도·재현율·성능 비교</span><span>효과: 핵심 신호 보존</span></div></div>

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 이상치(Outlier)는 정상적 분포 패턴에서 현저하게 벗어난 관측치이며, 노이즈(Noise)는 정보 가치가 없는 무작위 측정 오차임.
- 목적: 오류와 유효 희귀사건을 분리하여 통계 왜곡을 줄이고 사기·고장 신호를 보존함.

### 2. 핵심 메커니즘 / 체계
```text
[입력 데이터] ──▶ [탐지] IQR (Q1-1.5*IQR ~ Q3+1.5*IQR) / LOF / Isolation Forest
                     │
                     ▼
[처리 분기] 오류 ──▶ 삭제(Trimming) / 윈저화(Winsorizing)
            신호 ──▶ FDS 격리 보존 / Autoencoder 복원오차 모델링
```
- 통계, 거리/밀도, 머신러닝 3대 기법으로 식별 후 분석 목적에 따라 차등 처리함.

| 판정 대상 | 대책 | 검증 |
|---|---|---|
| 명백한 오류 | 삭제·대체 | 처리 전후 분포 |
| 유효 극단값 | 보존·강건 모형 | 민감도·모델 성능 |
| 이상 사건 | 격리·조사 | 정밀도·재현율 |

### 3. 적용 제언
- 이상치를 기계적으로 삭제하지 않고 원인을 규명하며, 실시간 환경에서는 지연·정밀도·재현율을 기준으로 통계·트리·신경망 후보를 비교해야 함.
- 결론: 탐지 점수만으로 삭제하지 말고 원인·업무비용·검증지표를 거쳐 처리 방식을 결정해야 함.

## 출제 이력과 검증 출처

- [scikit-learn, Novelty and Outlier Detection](https://scikit-learn.org/stable/modules/outlier_detection.html)
- [NIST/SEMATECH, Exploratory Data Analysis](https://www.itl.nist.gov/div898/handbook/eda/eda.htm)

## 학습 체크

- [ ] Ⅰ·Ⅱ 정의·비교: 이상치와 노이즈를 정보가치·원인·처리 기준으로 비교한다.
- [ ] Ⅲ 탐지: IQR·LOF·Isolation Forest의 원리와 임계·비용 조건을 설명한다.
- [ ] Ⅳ·Ⅴ 처리: 원인 판정 5단계와 삭제·대체·Winsorizing·강건 모형의 손실을 비교한다.
- [ ] Ⅵ·Ⅶ 판단: 자동 삭제 위험과 격리·업무 검증 Gate를 재현한다.

## 연결 토픽

- 이전 토픽: [동시성 제어(병행제어)](./009_concurrency_control.md)
- 연관 토픽: [군집분석](./005_cluster_analysis.md), [다중공선성](./004_multicollinearity.md), [시계열 실시간 이상치 탐지](./061_time_series_realtime_anomaly_detection.md)
- 다음 토픽: [불편추정량(Unbiased Estimator)](./011_unbiased_estimator.md)
