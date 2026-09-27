---
title: "분류 모델 성능지표(혼동행렬·PR/ROC 곡선)"
author: "OpenAI Codex"
date: "2026-09-24T12:40:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  order: 3
  label: "003. 분류 모델 성능지표"
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

07 최신 기술 → 인공지능 → 분류 모델의 오류 분석과 운영 성능 평가

## 30초 인출

- 본질: **혼동행렬(Confusion Matrix)** 은 실제 분류와 예측 분류를 교차 집계해 오탐·미탐을 구분하는 표
- 메커니즘: 네 칸의 집계에서 목적에 맞는 지표를 계산하고, 임계값별 성능과 오류 비용을 함께 비교
- 통찰: 한계: 정확도 하나로는 오탐·미탐의 업무 비용이 가려짐 → 방안: 양성 기준과 오류 비용을 정해 정밀도·재현율 및 임계값 선택
- 핵심 관계: `실제값 × 예측값 → TP·FP·FN·TN → 지표·운영점 선택`

<details>
<summary>핵심 용어</summary>

| 용어 | 설명 |
|---|---|
| **혼동행렬(Confusion Matrix)** | 실제 클래스와 예측 클래스의 조합별 건수를 정리한 표 |
| **정밀도(Precision)** | 양성으로 예측한 사례 중 실제 양성의 비율 |
| **재현율(Recall)** | 실제 양성 사례 중 양성으로 찾아낸 비율 |
| **ROC(Receiver Operating Characteristic) 곡선** | 임계값 변화에 따른 위양성률과 참양성률의 관계를 나타낸 곡선 |
| **PR(Precision-Recall) 곡선** | 임계값 변화에 따른 정밀도와 재현율의 관계를 나타낸 곡선 |
| **AUC(Area Under the Curve)** | 지정된 곡선 아래 면적으로 요약한 값이며 어떤 곡선인지 함께 밝혀야 하는 지표 |

</details>

---

## 2~4교시 예상문제 (25점)

> 분류 모델 성능평가에서 혼동행렬의 구조와 주요 지표, ROC·PR 곡선의 차이 및 임계값 선택 방법을 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 혼동행렬과 성능지표 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 실제 클래스와 예측 클래스의 조합별 건수를 정리한 표 |
| 목적 | 정답률뿐 아니라 오탐·미탐의 종류와 규모를 구분해 모델을 평가 |

## Ⅱ. 네 가지 예측 결과와 지표

```text
                         예측 양성     예측 음성
실제 양성                  TP           FN
실제 음성                  FP           TN

Precision = TP / (TP + FP)
Recall    = TP / (TP + FN)
```

| 지표 | 산식 | 해석 |
|---|---|---|
| Accuracy | `(TP+TN)/(TP+FP+FN+TN)` | 전체 사례 중 맞게 분류한 비율 |
| Precision | `TP/(TP+FP)` | 양성 예측의 정확도 |
| Recall | `TP/(TP+FN)` | 실제 양성의 포착 비율 |
| Specificity | `TN/(TN+FP)` | 실제 음성의 올바른 판별 비율 |
| F1 | `2×Precision×Recall/(Precision+Recall)` | 정밀도와 재현율의 조화평균 |

## Ⅲ. 임계값 변화와 곡선 비교

```text
모델 점수와 임계값
        │ 임계값 적용
        ▼
TP·FP·FN·TN 집계
        │ 임계값을 달리해 반복
        ├────────→ ROC: 위양성률과 참양성률
        └────────→ PR: 정밀도와 재현율
```

| 비교축 | ROC 곡선 | PR 곡선 |
|---|---|---|
| 세로·가로 축 | 참양성률 대 위양성률 | 정밀도 대 재현율 |
| 읽는 관점 | 양성과 음성의 판별 성능 | 양성 탐지의 정확도와 포착률 |
| 유의점 | 낮은 위양성률만으로 실제 오탐 건수를 알 수 없음 | 기준선과 해석이 양성 비율의 영향을 받음 |

**임계값과 지표 선택**

| 업무 상황 | 우선 검토 | 함께 확인할 조건 |
|---|---|---|
| 오탐 검토 비용이 큼 | Precision·위양성 건수 | 놓친 양성의 비용, 처리 용량 |
| 미탐 피해가 큼 | Recall·미탐 사례 | 오탐 처리 부담, 후속 확인 절차 |
| 양성이 희소함 | PR 곡선·양성별 지표 | 운영 분포와 평가 표본의 차이 |
| 임계값 운영 | 비용·용량에 맞는 후보 구간 | 독립 평가자료, 집단별 결과, 운영 변화 |

## Ⅳ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 클래스 비율이 다르면 같은 Accuracy도 의미가 달라짐 | 클래스별 지표와 실제 운영 분포를 함께 보고 |
| F1은 오탐·미탐 비용과 처리 용량을 직접 나타내지 않음 | 업무 비용과 후속 처리 조건을 별도로 반영 |
| 평가 표본과 운영 환경이 달라지면 지표가 변할 수 있음 | 시간·집단별 검증과 운영 결과 재점검 |

## Ⅴ. 제언

후보 임계값을 제한된 운영 범위에서 검증하고 오탐·미탐 비용과 처리 부담을 확인한 뒤 적용 범위 확대.

## 출제 이력과 검증 출처
- 아래 회차·문항은 기존 노트의 기록이며 공식 문제지 원문과 대조하지 못했다.

- 제134회·제135회·제136회 성능지표 관련 내용은 기존 노트의 이력 기록이며, 제136회 산출 예시는 TP=100, FP=5, FN=7, TN=9에서 각 값을 소수점 버림한 계산 기록.
- [scikit-learn, Classification metrics](https://scikit-learn.org/stable/api/sklearn.metrics.html)
- [scikit-learn, Precision-Recall example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html)
- [scikit-learn, ROC example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html)

## 연결 토픽

- [과적합·과소적합](./010_overfitting/) · [교차검증](./178_cross_validation/) · [LLM-as-a-Judge](./093_llm_as_a_judge/) · [AI 신뢰성](./038_ai_trustworthiness/)
