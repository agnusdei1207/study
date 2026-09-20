---
title: "데이터 차원 축소(Data Dimensionality Reduction)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "기출 · 70%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "131회"
  priority: 70
  priority_note: "[출제(KPC):131]"
---

## 답안 골격
```text
[데이터 차원 축소] ◀━━ 머리: Ⅶ 내 의견 (차원의 저주 극복 및 모델 해석력 향상을 위한 선형·비선형 축소 기법의 목적별 하이브리드 적용 전략)
 ┃
 ┣━ Ⅰ 개요 ───── 고차원 특성 데이터 증가에 따른 차원의 저주(Curse of Dimensionality), 연산 복잡도 폭증 및 과적합(Overfitting) 발생
 ┣━ Ⅱ 목적 ───── 데이터 시각화(2D/3D) · 학습 속도 개선 · 노이즈 제거 · 다중공선성(Multicollinearity) 해소 · 모델 일반화 성능 제고
 ┣━ Ⅲ 분류 ───── 특성 선택(Feature Selection: Filter, Wrapper, Embedded) vs 특성 추출(Feature Extraction: 선형, 비선형)
 ┣━ Ⅳ 기법 ───── 선형 추출(PCA, LDA, SVD) + 비선형 추출(t-SNE, UMAP, 오토인코더) + 특성 선택(LASSO, RFE, 분산 임계치)
 ┣━ Ⅴ 비교 ───── PCA vs LDA vs t-SNE vs UMAP (비지도/분산최대화/선형 vs 지도/클래스분리최대화/선형 vs 비지도/지역구조보존/시각화용비선형 vs 비지도/전역·지역구조균형/고속비선형)
 ┗━ Ⅵ 실무 ───── 고유값 분산 설명력(Explained Variance Ratio) 누적 임계점 선정 / 정보 손실률 관리 / 비선형 기법의 새로운 데이터 투영 불가 한계
```
- 필수 키워드: 차원의 저주(Curse of Dimensionality) · 특성 선택(Feature Selection) · 특성 추출(Feature Extraction) · PCA · LDA · t-SNE · UMAP · 분산 보존
- 배점 전략: 10점 = Ⅰ 개요 및 차원의 저주 → Ⅲ 차원 축소 양대 분류(선택 vs 추출) 체계도 → Ⅴ 대표 기법 4종(PCA/LDA/t-SNE/UMAP) 비교표 / 25점 = Ⅰ~Ⅶ 전개, PCA 고유값 분해(Eigendecomposition) 수학적 원리 및 UMAP 매니폴드 구조 전개
- 기출: 131회 `데이터 차원 축소` → Ⅰ~Ⅴ

## 한 줄 본질
- 변수가 너무 많아 공간이 텅 비고 모델이 길을 잃는 차원의 저주를 풀기 위해, 핵심 분산과 정보 구조만 압축 추출하여 계산 효율과 예측력을 극대화하는 데이터 정제 기술

## 핵심 그림
```text
[데이터 차원 축소의 양대 분류 및 대표 알고리즘 체계]

                     [데이터 차원 축소 기법]
                                │
        ┌───────────────────────┴───────────────────────┐
        ▼                                               ▼
  [특성 선택 (Feature Selection)]             [특성 추출 (Feature Extraction)]
  - 기존 변수 중 최적 부분집합 선정           - 기존 변수를 조합해 새 저차원 공간 투영
  - 해석력(Interpretability) 우수            - 정보 보존율 우수, 원본 의미 상실
        │                                               │
  ┌─────┼─────────────┐                   ┌─────────────┼─────────────┐
  ▼     ▼             ▼                   ▼             ▼             ▼
[Filter] [Wrapper] [Embedded]          [선형 기법]   [비선형 기법]   [딥러닝]
- 카이제곱 - RFE      - LASSO(L1)       - PCA(분산)   - t-SNE(시각화) - Autoencoder
- 피어슨   - 전진선택 - Ridge(L2)       - LDA(분류)   - UMAP(매니폴드)
```

## 핵심 용어
- 차원의 저주(Curse of Dimensionality): 차원이 증가함에 따라 데이터 공간의 부피가 기하급수적으로 커져 데이터 밀도가 희박(Sparse)해지고 과적합 및 거리 왜곡이 발생하는 현상
- 주성분 분석(PCA: Principal Component Analysis): 데이터의 분산(Variance)이 가장 큰 방향의 직교 벡터(주성분 축)를 찾아 고유값 분해(Eigendecomposition)를 통해 저차원으로 선형 투영하는 비지도 기법
- UMAP(Uniform Manifold Approximation and Projection): 리만 기하학과 위상수학을 기반으로 고차원 데이터의 로컬 및 글로벌 매니폴드 구조를 모두 보존하면서 t-SNE보다 빠른 속도로 축소하는 비선형 기법

## 핵심 통찰
- "선택(Selection)이냐 추출(Extraction)이냐": 도메인 해석과 규제 대응이 핵심인 의료/금융 데이터는 특성 선택(Filter/LASSO)을, 대규모 비정형 임베딩과 연산 효율화는 특성 추출(PCA/오토인코더)을 채택
- 엘보우 차트(Elbow Chart)와 스크리 플롯(Scree Plot): 주성분의 누적 분산 설명력(Explained Variance Ratio)이 85~90% 이상 도달하는 최소 차원을 수학적으로 결정해야 정보 왜곡 방지
- 시각화의 진화: PCA(선형, 전역 분산) → t-SNE(비선형, 국소 군집 왜곡 방지) → UMAP(비선형, 전역 연결성 보존 및 고속 대용량 처리)

## 이웃 토픽과 구분
- PCA vs LDA: PCA는 정답 라벨 없이 전체 데이터의 분산이 최대가 되는 축을 찾는 비지도 선형 축소 / LDA는 클래스 간 분산(Between-class)은 최대화하고 클래스 내 분산(Within-class)은 최소화하는 지도 선형 축소

## 문제·원인·대책
- 적용 상황: 유전자 발현 데이터(변수 20,000개, 샘플 500개) 기반 질병 분류 모델 구축
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 모델 학습 시 100% 암기(과적합) 발생하여 검증 데이터에서 성능 급락 | 변수 수(p)가 샘플 수(n)보다 훨씬 커서 발생하는 p>>n 고차원 희소성 | LASSO(L1 규제) 기반 유의미 변수 선별 및 1차 PCA 차원 축소 | 검증셋 정확도 65%에서 91%로 대폭 향상 |
| 20,000개 변수 연산으로 인한 모델 서빙 지연(Latency 3초 이상) | 고차원 행렬곱 연산에 따른 CPU 메모리 및 연산 병목 | 분산 설명력 90% 기준 50차원으로 PCA 축소 투영 | 추론 지연시간 50ms 미만으로 60배 단축 |
| 차원 축소 후 변수의 생물학적 의미 해석 불가 | 선형/비선형 조합 투영으로 원본 유전자 명칭 소실 | SHAP(Shapley Additive exPlanations) 결합 및 특성 중요도(Feature Importance) 역추적 | 의료진 납득 가능한 설명력(XAI) 확보 |

## 이렇게 출제된다
- 제131회 1교시: "머신러닝에서 차원의 저주 개념과 데이터 차원 축소(Data Dimensionality Reduction) 기법의 유형 및 특징을 설명하시오." → 요구 포인트: Ⅰ 차원의 저주 발생 배경 + Ⅲ 특성 선택 vs 특성 추출 분류 + Ⅴ PCA vs LDA vs UMAP 비교

## 내 의견
- [대규모 LLM 임베딩 벡터 서빙을 위한 2단계 양자화-차원축소 파이프라인 구축] 최근 1536차원 이상의 대규모 벡터 검색(RAG) 환경에서는 단순 저장 공간뿐만 아니라 밀집 벡터(Dense Vector)의 코사인 유사도 연산 비용이 최대 병목 → 나라면: 1단계로 Matryoshka Representation Learning(MRL) 및 PCA로 벡터 차원을 절반(768차원)으로 무손실 압축하고, 2단계로 Product Quantization(PQ)을 결합하여 ANN 검색 속도를 5배 향상시키고 인메모리 인덱스 비용을 75% 절감하는 아키텍처 구현
