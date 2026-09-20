---
title: "분류 모델 성능지표(혼동행렬·PR/ROC 곡선)"
author: "OpenAI Codex"
date: "2026-09-20T17:40:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5"
  keyword_grade: "A"
---

## 큰 그림과 30초 인출

```text
                    예측 Positive      예측 Negative
실제 Positive          TP                 FN
실제 Negative          FP                 TN

Precision = TP/(TP+FP)     Recall = TP/(TP+FN)
F1 = 2PR/(P+R)             Specificity = TN/(TN+FP)

threshold 이동 → TP·FP·FN·TN 변화 → PR/ROC 곡선 → 비용 기준 선택
```

- 본질: 실제값과 예측값의 일치·오류를 네 칸으로 분해하여 모델의 오류 종류와 비용을 판단
- 인출: `실양 TP/FN, 실음 FP/TN`
- 선택: FP 비용이 크면 Precision, FN 비용이 크면 Recall, 불균형 양성 탐지는 PR 곡선을 중점 검토
- 주의: Accuracy·F1·AUC 하나만으로 배포 가능성을 판정하지 않음

## 예상문제

> 혼동행렬을 활용한 분류 모델 성능평가 원리와 주요 지표를 설명하고, PR 곡선과 ROC 곡선을 비교한 뒤 불균형 데이터의 임계값 선정 방안을 논하시오. (25점)

## Ⅰ. 오류 유형을 분리하는 혼동행렬 개요

- 정의: **혼동행렬(Confusion Matrix)**은 실제 class와 예측 class의 조합을 TP·FP·FN·TN으로 집계하여 분류 결과와 오류 유형을 구조화한 표
- 목적: 정확도 하나로 숨겨지는 오탐·미탐을 분리하고 Precision·Recall·F1·Specificity·FPR 등 목적별 지표 산출
- 필요성: 양성이 희소한 데이터에서는 모두 음성으로 예측해도 Accuracy가 높아질 수 있으므로 업무 비용에 맞는 오류 지표가 필요

#### 한줄 요약

- 혼동행렬은 모델의 정답률을 보는 표가 아니라 어떤 오류를 얼마나 만들었는지 해석하는 기준표임

## Ⅱ. 클래스·임계값·비용에 종속되는 평가 특징

| 특징 | 의미 | 실무 판단 |
|---|---|---|
| **오류 분리** | FP와 FN을 별도 계수 | 오탐·미탐 비용을 따로 반영 |
| **Positive 기준** | 어떤 class를 양성으로 정했는지에 따라 값 변화 | target class 명시 |
| **Threshold 종속** | 임계값 이동 시 네 칸과 지표 변화 | 운영점과 곡선을 함께 평가 |
| **분포 종속** | Accuracy·Precision은 prevalence 영향 | 실제 운영 class 비율로 검증 |
| **다중분류 확장** | class별 one-vs-rest matrix | macro·micro·weighted 평균 구분 |
| **비용 기반 선택** | 지표 최대와 사업 손실 최소가 다를 수 있음 | cost matrix·capacity constraint 반영 |

#### 한줄 요약

- 지표값은 모델 고유 점수가 아니라 class 정의·데이터 분포·임계값·오류 비용의 함수임

## Ⅲ. TP·FP·FN·TN과 파생 지표 구조

```text
                         Predicted
                   Positive     Negative
Actual  Positive      TP           FN      → TP+FN (실제 양성)
        Negative      FP           TN      → FP+TN (실제 음성)
                      ↓            ↓
                    TP+FP        FN+TN
                  (예측 양성)   (예측 음성)
```

| 지표 | 산식 | 답하는 질문 |
|---|---|---|
| **Accuracy** | `(TP+TN)/(TP+FP+FN+TN)` | 전체 중 맞춘 비율은? |
| **Precision** | `TP/(TP+FP)` | 양성 예측 중 실제 양성은? |
| **Recall/TPR** | `TP/(TP+FN)` | 실제 양성 중 찾아낸 것은? |
| **Specificity/TNR** | `TN/(TN+FP)` | 실제 음성 중 걸러낸 것은? |
| **FPR** | `FP/(FP+TN)` | 실제 음성 중 오탐한 것은? |
| **F1** | `2·Precision·Recall/(Precision+Recall)` | Precision·Recall의 조화평균은? |

#### 한줄 요약

- 분모가 예측 양성이면 Precision, 실제 양성이면 Recall이라는 기준으로 공식을 복원함

## Ⅳ. 혼동행렬 산출에서 운영 임계값까지의 평가 절차

```text
① target class·업무 오류비용·운영용량 정의
          ↓
② 독립 test set에서 probability/score 예측
          ↓
③ threshold 적용 → TP·FP·FN·TN 집계
          ↓
④ 지표와 PR/ROC curve·subgroup 결과 산출
          ↓
⑤ 비용·용량·안전조건을 만족하는 operating point 선택
          ↓
⑥ 운영 분포·drift·오류비용 감시 후 threshold 재검증
```

### 제136회 계산형

조건: `TP=100, FP=5, FN=7, TN=9`, 결과는 %로 표시하고 소수점 버림

| 지표 | 계산 | 결과 |
|---|---|---:|
| Accuracy | `(100+9)/(100+5+7+9)` | **90%** |
| Precision | `100/(100+5)` | **95%** |
| Recall | `100/(100+7)` | **93%** |
| Specificity | `9/(9+5)` | **64%** |
| F1 | `2×100/(2×100+5+7)` | **94%** |

#### 한줄 요약

- 계산 후 숫자만 쓰지 않고 낮은 Specificity처럼 어떤 오류가 남았는지 해석해야 답안이 완성됨

## Ⅴ. 전체 순위와 희소 양성 품질을 보는 ROC·PR 비교

| 구분 | ROC curve | PR curve |
|---|---|---|
| **축** | FPR(x) - TPR/Recall(y) | Recall(x) - Precision(y) |
| **관점** | 양성·음성 전체의 순위 판별 | 양성 탐지의 정확성과 포착률 |
| **baseline** | random classifier의 diagonal | 양성 prevalence에 영향 |
| **강점** | threshold 전반의 판별력 비교 | 희소 양성·불균형 문제에서 오탐 영향 표현 |
| **주의** | 음성이 매우 많으면 낮은 FPR이 FP 건수를 숨길 수 있음 | dataset prevalence가 바뀌면 해석도 변함 |
| **선택** | 전반적 ranking 평가 | fraud·defect·disease 등 양성 탐지 평가 |

#### 한줄 요약

- ROC는 전체 class 순위능력을, PR은 양성 예측의 품질을 강조하므로 불균형 양성 문제에서는 PR을 함께 봄

## Ⅵ. 지표 최적화와 사업 손실의 불일치를 막는 고려사항

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **Accuracy 역설** | 다수 class가 지표를 지배 | confusion matrix·PR-AUC·class별 recall 병행 | 소수 class 실패 노출 |
| **F1 맹신** | FP·FN 비용을 동일하게 취급 | F-beta·cost matrix·expected loss 적용 | 업무 손실 기준 선택 |
| **평가 분포 불일치** | test set과 운영 prevalence·시간대 차이 | 시간·집단·지역별 slice와 out-of-time 평가 | 일반화 위험 확인 |
| **threshold 고정** | drift와 처리 capacity 변화를 미반영 | score calibration·운영량·비용 기반 재조정 | 경보량과 탐지 품질 균형 |
| **다중분류 평균 왜곡** | micro·macro·weighted의 class 가중 방식 차이 | class별 표와 평균 방식을 함께 명시 | 소수 class 성능 은폐 방지 |

#### 한줄 요약

- 모델 선택은 최고 F1을 찾는 문제가 아니라 오류 비용·처리용량·집단별 안전조건을 만족하는 운영점을 찾는 문제임

## Ⅶ. 지표-비용-운영결과의 폐루프로 완성하는 결론

- **[모델 metric을 업무 outcome으로 연결]**: offline 점수가 좋아도 오탐 처리인력·미탐 손실·사용자 피해가 악화될 수 있으므로 지표와 업무 결과를 공동 모니터링
- 나라면: `class별 confusion matrix + PR/ROC + calibration + 오류비용`으로 후보 threshold를 정하고, canary 배포 후 오탐량·미탐사건·처리시간·집단별 성능이 기준을 충족할 때 확대

#### 한줄 요약

- 성능평가의 완성 기준은 높은 단일 점수가 아니라 오류비용과 안전조건을 만족하는 threshold를 운영에서 지속 검증하는 상태임

## 1교시 10점 답안 발췌

### 1. 구조와 공식

```text
실양: TP / FN     실음: FP / TN
Precision=TP/(TP+FP), Recall=TP/(TP+FN)
F1=2PR/(P+R)
```

### 2. 제136회 계산 결과

| Accuracy | Precision | Recall | Specificity | F1 |
|---:|---:|---:|---:|---:|
| 90% | 95% | 93% | 64% | 94% |

### 3. 차별화 제언

- Accuracy 역설을 피하고 불균형 양성 문제는 PR 곡선과 class별 지표를 중점 평가
- 오류 비용과 운영 처리용량을 반영해 threshold를 정하고 drift 시 재검증

## 출제 이력과 검증 출처

- 제134회: 머신러닝 성능지표
- 제135회 1교시 1번: PR 곡선과 ROC 곡선 비교
- 제136회 3교시 5번: TP=100, FP=5, FN=7, TN=9 기반 혼동행렬 성능지표 계산
- [scikit-learn, metrics API](https://scikit-learn.org/stable/api/sklearn.metrics.html)
- [scikit-learn, Precision-Recall example and averaging](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)
- [scikit-learn, multiclass ROC and micro averaging](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

## 학습 체크

- [ ] 실제 양성 행에 TP·FN, 실제 음성 행에 FP·TN을 배치함
- [ ] 분모 기준으로 Precision·Recall 공식을 복원함
- [ ] 제136회 수치를 계산하고 Specificity까지 해석함
- [ ] PR과 ROC를 축·적용·불균형 관점으로 비교함
- [ ] threshold를 비용·용량·집단별 안전조건과 연결함

## 연결 토픽

- [과적합·과소적합](./010_overfitting/) · [교차검증](./178_cross_validation/) · [LLM-as-a-Judge](./093_llm_as_a_judge/) · [AI 신뢰성](./038_ai_trustworthiness/)
