---
title: "DBSCAN(Density-Based Spatial Clustering of Applications with Noise)"
author: "Gemini 3.8 Flash"
date: "2026-09-24T00:00:00+09:00"
sidebar:
  order: 22
  label: "022. DBSCAN"
  badge:
    text: "기초"
    variant: note
tags:
  - "notes-latest-tech"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

지식 위치: 비지도학습 → 밀도 기반 군집화 → **DBSCAN**

## 30초 인출

- 본질: **DBSCAN(Density-Based Spatial Clustering of Applications with Noise)** 은 이웃 밀도로 임의 형태의 군집과 노이즈를 찾는 군집화 알고리즘
- 메커니즘: Eps 이웃 탐색 → MinPts 기준 핵심점 판정 → 밀도 연결 영역 확장 → 경계점·노이즈 구분

<details>
<summary>핵심 용어</summary>

- **DBSCAN(Density-Based Spatial Clustering of Applications with Noise)** : 점의 이웃 밀도로 군집과 노이즈를 구분하는 알고리즘
- **Eps(ε)** : 한 점의 이웃을 정하는 거리 반경
- **MinPts** : 핵심점 판정을 위해 이웃 안에 요구되는 최소 점 수
- **핵심점(Core Point)** : Eps 이웃 수가 MinPts 이상인 점
- **경계점(Border Point)** : 자체 이웃 수는 부족하지만 핵심점의 이웃에 속하는 점
- **노이즈점(Noise Point)** : 핵심점도 아니고 핵심점의 이웃에도 속하지 않는 점
</details>

---
## 1교시 예상문제 (10점)

> DBSCAN의 개념과 밀도 기반 군집화 절차를 설명하시오. (예상·10점)

---
## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **DBSCAN(Density-Based Spatial Clustering of Applications with Noise)** 은 이웃 밀도로 임의 형태의 군집과 노이즈를 찾는 군집화 알고리즘 |
| 목적 | 군집 수를 미리 정하지 않고 밀도 연결 영역과 낮은 밀도 점을 구분 |

### Ⅱ. 군집 확장 절차

```text
점의 Eps 이웃 탐색
         ↓
이웃 수 ≥ MinPts ?
   ┌─────┴─────┐
  예           아니오
  ↓               ↓
핵심점       경계점 후보·노이즈
  ↓
밀도 연결 이웃으로 군집 확장
```

### Ⅲ. 점 유형

| 유형 | 밀도 조건 |
|---|---|
| 핵심점 | Eps 이웃에 MinPts 이상 |
| 경계점 | 자체 기준은 미달하나 핵심점 이웃에 포함 |
| 노이즈점 | 핵심점·핵심점 이웃에 해당하지 않음 |

제언: 거리 척도와 변수 스케일을 정한 뒤 Eps·MinPts 민감도를 평가하는 설정.

---
## 2~4교시 예상문제 (25점)

> DBSCAN의 개념과 핵심 매개변수, 군집 확장 절차를 설명하고 적용 장점과 한계를 제시하시오. (예상·25점)

---
## 2~4교시 25점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **DBSCAN(Density-Based Spatial Clustering of Applications with Noise)** 은 이웃 밀도로 임의 형태의 군집과 노이즈를 찾는 군집화 알고리즘 |
| 목적 | 군집 수를 미리 정하지 않고 밀도 연결 영역과 낮은 밀도 점을 구분 |

### Ⅱ. 군집 확장 절차

```text
점의 Eps 이웃 탐색
         ↓
이웃 수 ≥ MinPts ?
   ┌─────┴─────┐
  예           아니오
  ↓               ↓
핵심점       경계점 후보·노이즈
  ↓
밀도 연결 이웃으로 군집 확장
```

### Ⅲ. 핵심 매개변수

| 매개변수 | 역할 | 설정 관점 |
|---|---|---|
| Eps(ε) | 이웃 탐색 반경 | 변수 스케일·거리 척도와 함께 검토 |
| MinPts | 핵심점 판정 최소 이웃 수 | 자료 차원·잡음 수준과 함께 검토 |

### Ⅳ. 적용 장점과 한계

| 관점 | 내용 |
|---|---|
| 장점 | 사전 군집 수 불필요, 임의 형태 군집, 노이즈 구분 |
| 한계 | 밀도 차이가 큰 자료에서 단일 Eps로 모든 군집 포착이 어려울 수 있음 |
| 복잡도 영향 | 거리 계산·자료 구조에 따라 수행 비용이 달라질 수 있음 |

### Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 밀도 분포가 서로 다른 군집이 섞이면 하나의 매개변수 조합이 모든 영역에 적합하지 않을 수 있음 | 거리·스케일 표준화와 Eps 민감도 평가를 수행하고, 필요하면 OPTICS 등 밀도 변화를 다루는 대안을 같은 기준 자료에서 비교 |

---
## 출제 이력과 검증 출처

- 제129회 1교시: DBSCAN의 개념과 특징
- 제130회 2교시: K-Means와 DBSCAN 비교
- [scikit-learn, Clustering: DBSCAN](https://scikit-learn.org/stable/modules/clustering.html#dbscan): 핵심·경계·노이즈 점과 매개변수 설명 확인
