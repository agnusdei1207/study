---
title: "XGBoost·LightGBM(XGBoost and LightGBM)"
date: "2026-09-20T11:00:00+09:00"
tags:
  - "notes-basic-theory"
sidebar:
  badge:
    text: "C · 미출 · 50%"
extra:
  source_status: "미출"
  source_history: ""
  priority: 50
  priority_note: "-"
---

## 답안 골격
```text
[GBM 고도화 라이브러리] ◀━━ 머리: 2차 테일러 근사 기반 정밀 최적화(XGBoost)와 히스토그램 리프 중심 고속화(LightGBM)
 ┃
 ┣━ Ⅰ 개요 ───── 전통 GBM 학습 속도 지연 한계 → 2차 도함수 최적화 및 히스토그램 기반 메모리/속도 혁신
 ┣━ Ⅱ 수식 ───── XGBoost 2차 테일러 전개 목적함수: $\text{Obj} \approx \sum [g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i)] + \Omega(f_t)$
 ┣━ Ⅲ 기술 ───── XGBoost(정밀 탐색, L1/L2 규제 내장) vs LightGBM(GOSS 샘플링, EFB 피처 결합)
 ┣━ Ⅳ 분할 ───── Level-wise(균형 깊이 우선: XGBoost 기본) vs Leaf-wise(손실 최대 감소 리프 우선: LightGBM)
 ┣━ Ⅴ 비교 ───── 전통 GBM vs XGBoost vs LightGBM 종합 비교표
 ┗━ Ⅵ 실무 ───── 정형 테이블 캐글 챔피언 모델 · 대규모 데이터셋 학습 시간 대폭 단축
```
- 필수 키워드: 2차 테일러 전개 · 헤시안($h_i$) · GOSS · EFB · Leaf-wise 트리 성장 · 히스토그램

## 한 줄 본질
- 이전 트리의 오차를 순차 보정하는 그래디언트 부스팅의 극심한 학습 지연을 2차 도함수(Hessian) 정규화와 히스토그램 기반 샘플링으로 해결 → 정형 데이터 최고 수준의 정확도와 초고속 훈련 / 소량 데이터 과적합 위험

## 핵심 그림
```text
[XGBoost: Level-wise (균형 성장)]          [LightGBM: Leaf-wise (손실 최대 감소)]
              O                                        O
            /   \                                    /   \
           O     O                                  O     O
          / \   / \                                      / \
         O   O O   O                                    O   O
      (동일 깊이 레벨 일괄 분할)                            / \
      (트리 균형 유지, 과적합 억제)                        O   O  (손실 감소 큰 노드만 심층 분할)
```

## 핵심 통찰
- XGBoost는 손실 함수를 2차 테일러 전개하여 1차 미분(Gradient)뿐만 아니라 2차 미분(Hessian) 정보를 함께 사용하여 최적 분할점과 가중치를 수학적으로 더 정밀하고 빠르게 계산함
- LightGBM은 연속형 특성을 구간(Bin)으로 나누는 히스토그램 알고리즘과 함께, 그래디언트가 큰 중요한 데이터만 남기는 GOSS와 희소 특성을 묶는 EFB를 통해 메모리 사용량을 획기적으로 줄이고 학습 속도를 수배 가속함

## 이웃 토픽과 구분
- XGBoost vs LightGBM:
| 비교 항목 | XGBoost | LightGBM |
|---|---|---|
| 트리 분할 방식 | Level-wise (균형 깊이 성장) | Leaf-wise (리프 중심 비대칭 성장) |
| 목적함수 최적화 | 2차 테일러 근사 + 정규화 내장 | 히스토그램 기반 고속 분할 |
| 핵심 가속 기술 | 캐시 인식(Cache-aware) 블록화 | GOSS (데이터 샘플링), EFB (피처 결합) |
| 최적 환경 | 중소 규모 고정밀 데이터셋 | 대규모 초고용량 빅데이터 |

## 이렇게 출제된다
- 미출 대비: "그래디언트 부스팅의 진화인 XGBoost와 LightGBM의 기술적 차이점 및 가속화 원리(Level-wise vs Leaf-wise)" → 요구 포인트: 2차 테일러 전개 수식, GOSS/EFB 개념, 트리 분할 전략 차이
