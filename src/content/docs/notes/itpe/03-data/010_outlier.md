---
title: "이상치(탐지 기법·노이즈 구분 포함)"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
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
  <div class="itpe-flow-node"><strong>원천 데이터 수집</strong><small>센서 · 금융 거래 로그 · 의료 데이터</small></div>
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

> 데이터 전처리 및 이상 징후 탐지를 위한 이상치(Outlier)와 노이즈(Noise)의 개념 및 차이점을 비교하고, 통계적·거리/밀도·머신러닝 기반 3대 탐지 알고리즘(IQR, LOF, Isolation Forest) 및 분석 목적에 따른 4대 처리 전략을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **이상치 탐지(Outlier Detection)** | 비정상 패턴과 이상 데이터를 자동으로 식별하는 알고리즘 파이프라인 | Ⅲ 탐지 기법 |
| **노이즈(Noise)** | 데이터 측정 및 통신 과정에서 발생하는 무작위 오차(Random Error) 및 필터링 기법 | Ⅱ 차이 비교 |

## Ⅰ. 데이터 왜곡의 주범이자 사기 탐지의 신호탄, 이상치의 개요

> **한줄 요약:** 이상치는 정상 분포에서 극단적으로 이탈한 관측치로, 단순 제거 대상인 노이즈와 달리 고가치 정보를 내포할 수 있음.

- 정의: 대부분의 데이터가 따르는 정상적 분포나 규칙에서 현저하게 벗어나, 다른 메커니즘에 의해 생성된 것으로 의심되는 관측치 (Hawkins, 1980)
- 양면성:
  1. **데이터 품질 저하 요인**: 평균, 분산, 회귀계수를 극단적으로 왜곡하여 머신러닝 모형의 일반화 성능을 파괴
  2. **비즈니스 핵심 가치 요인**: 신용카드 부정사용(FDS), 네트워크 침입(IDS), 제조 설비 고장 예지 등 이상치 자체가 모형화의 핵심 타깃
- 분류: 단일 변수 기준의 글로벌 이상치(Global), 특정 조건 하에서의 맥락적 이상치(Contextual), 순차적 패턴에 의해 판정되는 집단적 이상치(Collective)

## Ⅱ. 이상치(Outlier) vs 노이즈(Noise) 비교

> **한줄 요약:** 노이즈는 제거해야 할 무작위 오차이고, 이상치는 의미 분석이 필요한 식별 가능한 극단치임.

| 비교 기준 | 이상치 (Outlier) | 노이즈 (Noise) |
|---|---|---|
| **개념적 본질** | 정상 범위에서 크게 벗어난 '유효하거나 유의미한' 관측값 | 측정, 전송, 입력 과정에서 유입된 '무작위적 무의미한' 오차 |
| **정보 가치** | 잠재적 고가치 신호(사기, 고장, 특이현상) 내포 가능 | 분석에 방해만 되는 순수 불순물 (Zero Value) |
| **발생 원인** | 희귀 이벤트 발생, 시스템 침입, 구조적 변경 | 센서 정밀도 한계, 통신 잡음, 환경 진동 |
| **처리 기본 원칙** | 원인 규명 선행 $\to$ 도메인 목적에 따라 보존/격리/변환 | 평활화(Smoothing), 필터링(Kalman 등)으로 사전 제거 |
| **대표 사례** | 1회 1,000만원 결제(이상치), 제조 설비 진동 급증 | 센서 계측 시 $\pm 0.05$ 미세 진동 오차 |

## Ⅲ. 이상치 탐지 3대 핵심 알고리즘 체계

> **한줄 요약:** 단변량 통계(IQR), 다변량 밀도(LOF), 트리 격리(Isolation Forest)를 결합하여 탐지함.

<div class="itpe-pipeline" role="img" aria-label="이상치 3대 탐지 알고리즘">
  <div class="itpe-pipeline-node"><strong>통계 기반</strong><small>IQR / Z-Score</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>거리·밀도 기반</strong><small>Mahalanobis / LOF</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>머신러닝 기반</strong><small>Isolation Forest / AE</small></div>
</div>

| 기법 | 핵심 동작 수식 및 원리 | 주요 특징 및 장단점 |
|---|---|---|
| **IQR (사분위수 범위)** | 하한: $Q_1 - 1.5 \times IQR$, 상한: $Q_3 + 1.5 \times IQR$<br>($IQR = Q_3 - Q_1$) | 정규분포 가정이 불필요하고 이상치에 강건(Robust)하나, 1차원 단변량에 한정됨 |
| **Z-Score / ESD** | $Z = \frac{x - \mu}{\sigma}$, $|Z| > 3$ 시 이상치 판정 | 계산이 단순하나 평균과 표준편차 자체가 극단치에 왜곡되는 취약성 존재 |
| **마할라노비스 거리** | $D_M(x) = \sqrt{(x-\mu)^T \Sigma^{-1} (x-\mu)}$ | 변수 간 상관관계를 반영한 다차원 거리 측정, 고차원 역행렬 계산 필요 |
| **LOF (Local Outlier Factor)** | 데이터 포인트 $p$의 국소 도달 밀도와 $k$-최근접 이웃들의 밀도 비율 | 밀도가 불균일한 클러스터 환경에서도 이상치를 정밀 탐지 (비율 $> 1$ 시 이상치) |
| **Isolation Forest** | 무작위로 축과 분할점을 선택해 이진 트리를 구축할 때, **이상치는 루트 노드 근처에서 조기 격리(Short Path Length)**됨 | 고차원 대용량 데이터에 선형 시간($O(n)$)으로 동작, 현대 현업 표준 모델 |

## Ⅳ. 이상치 탐지 및 처리 5단계 절차

> **한줄 요약:** 탐지 후 무조건 삭제하지 않고 원인 분류 후 도메인 규칙에 따라 처리 방식을 확정함.

| 단계 | 활동 내용 | 통제 기준 |
|---|---|---|
| **1. 탐색적 분석 (EDA)** | 산점도(Scatter Plot), 상자수염그림(Boxplot), 왜도/첨도 확인 | 데이터 왜곡 및 극단치 존재 시각적 확인 |
| **2. 탐지 알고리즘 실행** | 단변량(IQR) 및 다변량(Isolation Forest) 파이프라인 가동 | 이상치 후보군(Anomaly Candidate) 추출 |
| **3. 원인 분류 (Root Cause)** | 단순 입력/시스템 오류인지, 실제 비즈니스 사건인지 도메인 검증 | 오류(Error) vs 유효 극단치(Valid Event) 분리 |
| **4. 이상치 처리 전략 적용** | 삭제, 대체, 클리핑, 강건 모델링 중 목적에 맞게 적용 | 데이터 손실 최소화 및 모델 왜곡 방지 |
| **5. 모델 영향도 검증** | 처리 전후의 모델 성능(MAE, RMSE, F1-Score) 및 계수 안정성 대조 | 과대적합 방지 및 일반화 능력 검증 |

## Ⅴ. 분석 목적에 따른 4대 이상치 처리 전략

> **한줄 요약:** 인과 분석은 윈저화나 삭제를, 이상 탐지는 별도 모델 분리를, 머신러닝은 강건 회귀를 선택함.

| 처리 전략 | 구체적 처리 기법 | 적합한 분석 상황 | 주의사항 및 트레이드오프 |
|---|---|---|---|
| **삭제 (Trimming)** | 판정된 이상치 레코드를 분석 데이터셋에서 영구 제외 | 명백한 시스템 오류, 통계적 오염 제거 필요 시 | 표본 크기 감소 및 표본 선택 편향(Selection Bias) 유발 |
| **대체 (Imputation)** | 정상 범위의 평균, 중앙값(Median), 최빈값 또는 보간법으로 대체 | 결측치와 결합된 오류 데이터 | 데이터 분산이 인위적으로 축소되어 표준오차 과소추정 |
| **클리핑 (Winsorizing)** | 상한/하한 임계치를 벗어난 값을 상한값(99%) 또는 하한값(1%)으로 치환 | 금융 데이터 등 극단치 분포를 유지하면서 스케일 안정화 시 | 데이터 왜곡 없이 극단적 경사 하강 수렴 실패 방지 |
| **강건 모델링 (Robust)** | 이상치에 둔감한 Huber Loss, RANSAC, 트리 앙상블 모형 적용 | 이상치를 삭제할 수 없으나 예측 성능을 유지해야 할 때 | 이상치의 영향력을 수식적으로 완화(Down-weighting) |

## Ⅵ. 실무 고려사항 및 장애 대책

> **한줄 요약:** 자동 삭제로 인한 핵심 사기 신호 유실과 차원의 저주를 파이프라인 격리로 방어함.

- 적용 상황: 카드 결제 FDS(이상거래탐지시스템) 및 반도체 공정 센서 이상 감지

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **사기 거래 데이터 오삭제** | 전처리 엔지니어가 이상 거래를 단순 노이즈로 오인하여 일괄 Trimming | 이상치 탐지 파이프라인과 지도학습 분류 파이프라인 분리 | FDS 학습용 핵심 불균형 데이터 보존 |
| **고차원 센서 거리 균일화** | 수백 개 센서 변수 동시 투입 시 유클리디안 거리 분별력 상실 | Autoencoder 잠재 벡터 복원 오차(Reconstruction Error) 기반 탐지 | 차원의 저주 극복 및 복합 이상치 탐지 |
| **스트리밍 지연 발생** | 초당 수만 건 트래픽에 복잡한 군집 기반 탐지 알고리즘 적용 | 경량화된 Half-Space Trees 또는 온라인 Isolation Forest 적용 | 실시간성(Latency < 10ms) 보장 |

## Ⅶ. 결론 및 기술사적 제언

> **한줄 요약:** 이상치 처리는 기계적 정제가 아니라 도메인 지식과 머신러닝이 결합된 의사결정 파이프라인이어야 함.

- [핵심 통찰]: 데이터 엔지니어링에서 가장 위험한 행위는 탐지된 이상치를 '평균을 갉아먹는 귀찮은 존재'로 보고 DELETE 문을 날리는 것임. 이상치는 비즈니스의 사각지대, 새로운 고객 세그먼트, 또는 시스템 장애의 전조 증상일 가능성이 높음.
- 나라면: 데이터 전처리 단계에서 '이상치 격리 큐(Anomaly Quarantine Queue)'를 구축하여, 탐지된 이상치 데이터를 원천 보존하고, SHAP/LIME 기반 XAI(설명가능 인공지능)를 연동해 이상치로 판정된 원인 피처를 현업 분석가에게 대시보드로 자동 제공하는 체계를 수립하겠음.

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 이상치(Outlier)는 정상적 분포 패턴에서 현저하게 벗어난 관측치이며, 노이즈(Noise)는 정보 가치가 없는 무작위 측정 오차임.

### 2. 핵심 메커니즘 / 체계
```text
[입력 데이터] ──▶ [탐지] IQR (Q1-1.5*IQR ~ Q3+1.5*IQR) / LOF / Isolation Forest
                     │
                     ▼
[처리 분기] 오류 ──▶ 삭제(Trimming) / 윈저화(Winsorizing)
            신호 ──▶ FDS 격리 보존 / Autoencoder 복원오차 모델링
```
- 통계, 거리/밀도, 머신러닝 3대 기법으로 식별 후 분석 목적에 따라 차등 처리함.

### 3. 차별화 제언
- 이상치를 기계적으로 삭제하지 않고 XAI 기반 이상 원인을 규명하며, 실시간 환경에서는 Autoencoder 복원 오차 기반 파이프라인을 구축해야 함.

## 출제 이력과 검증 출처

- 출제 이력: 제139회·136회 정보관리기술사 기출, 제102회 KPC 모의고사
- 검증 출처: 한국데이터산업진흥원(K-DATA) ADP 가이드, Scikit-learn Anomaly Detection Documentation

## 학습 체크

- [ ] 이상치(Outlier)와 노이즈(Noise)의 본질적 차이를 설명할 수 있는가?
- [ ] IQR 수식과 Isolation Forest의 핵심 격리 원리를 제시할 수 있는가?
- [ ] 삭제, 대체, 윈저화, 강건 모형 등 4대 처리 전략의 트레이드오프를 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [동시성 제어(병행제어)](./009_concurrency_control.md)
- 연관 토픽: [군집분석](./005_cluster_analysis.md), [다중공선성](./004_multicollinearity.md), [시계열 실시간 이상치 탐지](./061_time_series_realtime_anomaly_detection.md)
- 다음 토픽: [불편추정량(Unbiased Estimator)](./011_unbiased_estimator.md)
