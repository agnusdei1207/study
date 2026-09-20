---
title: "손실 함수 — Cross-Entropy·MSE(Loss Functions)"
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
[손실 함수] ◀━━ 머리: 회귀(MSE)와 분류(Cross-Entropy)의 오차 정량화 및 역전파 그래디언트 제공
 ┃
 ┣━ Ⅰ 개요 ───── 모델 평가 지표의 미분 불가 한계 → 정답과 예측값의 오차를 연속 미분 가능 함수로 정량화
 ┣━ Ⅱ 수식 ───── MSE($\frac{1}{n}\sum(y-\hat{y})^2$) · BCE($-[y\log\hat{y}+(1-y)\log(1-\hat{y})]$) · CCE($-\sum y_c\log\hat{y}_c$)
 ┣━ Ⅲ 구조 ───── 회귀(선형 출력 $\to$ MSE) vs 이진 분류(Sigmoid $\to$ BCE) vs 다중 분류(Softmax $\to$ CCE)
 ┣━ Ⅳ 특성 ───── 이상치 페널티 민감도(제곱 오차) vs 확률 분포 간 쿨백-라이블러 발산(KLD) 최소화
 ┣━ Ⅴ 비교 ───── MSE vs MAE vs Cross-Entropy 종합 비교표 (태스크, 미분 특성, 이상치 영향)
 ┗━ Ⅵ 실무 ───── Focal Loss(클래스 불균형 완화) · Huber Loss(MSE+MAE 결합 강건 회귀)
```
- 필수 키워드: 손실 함수(Loss Function) · MSE · MAE · 교차 엔트로피(Cross-Entropy) · Softmax · Focal Loss

## 한 줄 본질
- 모델의 예측값과 실제 정답 간의 차이를 정량화하여 역전파(Backprop) 최적화에 필요한 1차 미분 오차 기울기를 제공 → 최적 가중치 수렴 유도 / 태스크별 손실 함수 미스매칭 시 수렴 실패

## 핵심 그림
```text
[회귀 문제: 평균 제곱 오차 (MSE)]           [분류 문제: 교차 엔트로피 (Cross-Entropy)]
  Loss (MSE)                                  Loss (BCE, 정답 y=1 일 때)
   ^                                           ^
   |        \     /                            | \
   |         \   /                             |  \
   |          \_/                              |   ' .
   |                                           |       ' - . _
   +---------------------> 오차 (y - y_hat)     +---------------------> 예측 확률 y_hat
   (제곱 페널티: 큰 오차에 가혹함)               0                      1
                                               (예측 확률이 0에 가까울수록 손실 무한대 폭증)
```

## 핵심 통찰
- 분류 문제에서 MSE 대신 교차 엔트로피(Cross-Entropy)를 사용하는 이유는, Sigmoid/Softmax와 결합했을 때 포화 영역에서도 역전파 오차 기울기($\hat{y} - y$)가 단순 선형으로 깔끔하게 떨어져 기울기 소실 없이 고속 수렴하기 때문임
- 교차 엔트로피의 정보이론적 본질은 실제 정답의 원-핫 분포 $P$와 모델의 예측 확률 분포 $Q$ 사이의 쿨백-라이블러 발산(KLD)을 최소화하는 것과 완벽히 동치임

## 이웃 토픽과 구분
- MSE vs MAE: MSE = 오차를 제곱하므로 큰 오차(이상치)에 민감하게 반응하여 모델을 극단값에 끌려가게 만듦 / MAE = 절대값 오차이므로 이상치에 강건하지만 원점($e=0$)에서 미분 불가능하여 수렴 시 진동 발생

## 이렇게 출제된다
- 미출 대비: "회귀 및 분류 모델의 대표적인 손실 함수(MSE, Cross-Entropy)의 수식 및 특징, 활성화 함수와의 결합 관계" → 요구 포인트: MSE vs MAE 비교, 교차 엔트로피의 확률적 유도, Softmax 결합 시 역전파 미분식
