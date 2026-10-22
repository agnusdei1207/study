---
title: "다차원 척도법(MDS, Multidimensional Scaling)"
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

**MDS(Multidimensional Scaling)**, **계량적/비계량적**, **스트레스(Stress)**, **PCoA**, **t-SNE/UMAP**, **포지셔닝 맵(Perceptual Map)**

## Ⅰ. 개요

- 핵심 요약 : **MDS**는 객체 간 유사도/비유사도를 저차원 좌표로 시각화하는 차원 축소 기법.
- 목적 : 고차원 객체 관계를 2D/3D 포지셔닝 맵으로 표현.
- 배경 : 브랜드·제품 간 심리적 거리 시각화 필요 → MDS.
- 특징 : 계량적(Metric)/비계량적(Non-metric), 스트레스 평가, PCoA.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **차원 축소·포지셔닝 맵·유사도 시각화**로 인지 구조 파악.
- **차원 축소** : 고차원 → 2D/3D 시각화.
- **포지셔닝 맵** : 소비자 인지 브랜드 위치 표현.
- **유연한 입력** : 수치 거리 또는 순위 데이터.
- **해석 보조** : Property Fitting으로 축 의미 부여.
- **다양한 변형** : Classical, Non-metric, Landmark.

## Ⅲ. 적합도 평가 흐름

- 핵심 요약 : **스트레스 값**으로 저차원 배치 적합도 평가.
- 스트레스 산식 : $\sqrt{\sum(d_{ij}-\hat d_{ij})^2 / \sum d_{ij}^2}$.
- 기준 : ≤0.05 우수, 0.05~0.10 양호, 0.10~0.20 보통, >0.20 불량.

```text
[ 계량적 vs 비계량적 MDS ]

계량적 : 수치 거리 입력, 고유값 분해(PCoA), 선형 적합
비계량적 : 순위 입력, Kruskal Stress 최소화, 단조 보존
```

## Ⅳ. 계량적 vs 비계량적 비교

- 핵심 요약 : **입력 척도·적합 원리·해법** 비교.

| 항목 | 계량적 MDS | 비계량적 MDS |
|---|---|---|
| 입력 척도 | 구간/비율 (수치) | 순서 (서열) |
| 적합 원리 | $d_{ij} \approx \delta_{ij}$ | 순위 단조 보존 |
| 해법 | 고유값 분해 (PCoA) | Kruskal Stress 경사하강법 |
| 적용 사례 | 도시 간 실제 거리 | 브랜드 선호 순위 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **O(N³) 복잡도·국소 최적해·해석 부재**를 Landmark·t-SNE·Property Fitting으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 시간 복잡도 | N 수만 건 시 거리 행렬 연산 폭증 | Landmark MDS, t-SNE/UMAP 대체 | 연산 시간 |
| 국소 최적해 | 초기 배치 민감, 왜곡된 맵 | Classical Scaling 초기값, Multi-start | 스트레스 |
| 축 의미 해석 부재 | 추상 공간 축의 비즈니스 의미 없음 | Property Fitting으로 속성 벡터 중첩 | 해석 가능성 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **축 명명·Landmark·대체 기법**으로 실무 적용.
- 축 비즈니스 명명 : 도메인 전문가가 X/Y축 의미 부여.
- 빅데이터 : Landmark MDS 또는 t-SNE/UMAP 대체.
- $O(n^2)$ 메모리 한계 : 수만 건 초과 시 대체 기법.

## Ⅶ. 결론

- 핵심 요약 : MDS는 **유사도 시각화 차원 축소** 기법으로 스트레스·해석이 핵심.
- 답안에는 계량/비계량 비교, 스트레스 기준, 한계·대응을 연결.
- 참고 : [scikit-learn MDS](https://scikit-learn.org/stable/modules/manifold.html#multidimensional-scaling).