---
title: "활성화 함수 — ReLU·Sigmoid·Tanh(Activation Functions)"
date: "2026-09-20T11:00:00+09:00"
tags:
  - "notes-basic-theory"
sidebar:
  badge:
    text: "C · 미출 · 30%"
extra:
  source_status: "미출"
  source_history: ""
  priority: 30
  priority_note: "-"
---

## 답안 골격
```text
[비선형 활성화 함수] ◀━━ 머리: 신경망의 비선형 표현력 부여와 기울기 소실 방지를 위한 활성화 함수 진화
 ┃
 ┣━ Ⅰ 개요 ───── 선형 계층 단순 중첩 한계 → 가중합에 비선형 변환을 적용하여 복잡한 함수 근사 역량 부여
 ┣━ Ⅱ 발전 ───── [Sigmoid: (0, 1) 확률] ➔ [Tanh: (-1, 1) 영점 중심화] ➔ [ReLU: max(0, z) 기울기 보존]
 ┣━ Ⅲ 수식 ───── $\sigma(z)=\frac{1}{1+e^{-z}}$ · $\tanh(z)=\frac{e^z-e^{-z}}{e^z+e^{-z}}$ · $\text{ReLU}(z)=\max(0, z)$
 ┣━ Ⅳ 한계/극복 ─ Sigmoid 기울기 소실($\sigma'\le 0.25$) $\to$ ReLU 도입 $\to$ Dying ReLU $\to$ Leaky ReLU / GELU
 ┣━ Ⅴ 비교 ───── Sigmoid vs Tanh vs ReLU vs GELU 종합 비교표 (출력 범위, 도함수, 주요 용도)
 ┗━ Ⅵ 실무 ───── 이진 분류 출력층(Sigmoid) · 은닉층 표준(ReLU/GELU) · 트랜스포머 LLM(GELU, SwiGLU)
```
- 필수 키워드: 비선형성(Non-linearity) · 시그모이드 · Tanh · ReLU · 기울기 소실 · Dying ReLU · GELU

## 한 줄 본질
- 활성화 함수가 없으면 100층을 쌓아도 1개의 선형 회귀에 불과하므로 비선형 굴절을 부여해 심층 신경망의 복잡한 패턴 표현을 가능하게 함 → 보편적 함수 근사 달성 / 포화 구간 미분 소멸 및 뉴런 사멸 상충

## 핵심 그림
```text
[Sigmoid: (0, 1)]            [Tanh: (-1, 1)]             [ReLU: max(0, z)]
       f(z)                         f(z)                        f(z)
        ^                            ^                           ^       /
      1 |       .----              1 |         .--               |      /  (미분값=1)
        |     /                      |       /                   |     /
    0.5 +----+ (변곡점)            0 +------+ (Zero-centered)    |    /
        |   /                        |     /                     |   /
      0 +--'----> z               -1 |--.-'-----> z            0 +--+-----> z
        (미분 최대 0.25)             (미분 최대 1.0)              (음수 미분 0: Dying ReLU)
```

## 핵심 통찰
- 활성화 함수는 반드시 비선형(Non-linear)이어야 하며, 선형 함수 $f(x)=cx$를 쓰면 $W_2(W_1 x) = (W_2 W_1)x = W' x$가 되어 층을 아무리 깊게 쌓아도 단층 퍼셉트론과 수학적으로 동일해짐
- ReLU는 양수 영역에서 도함수가 항상 1이므로 역전파 기울기가 전혀 감쇄되지 않아 초심층망 훈련을 가능하게 만들었으나, 음수 입력 시 기울기가 0이 되어 뉴런이 영구히 죽는 'Dying ReLU'가 발생할 수 있음
- 최신 트랜스포머 LLM에서는 입력에 확률적 정규분포 가중치를 곱해 부드럽게 0으로 수렴시키는 GELU 및 SwiGLU가 표준으로 자리 잡음

## 이웃 토픽과 구분
- 활성화 함수 종합 비교:
| 비교 항목 | Sigmoid | Tanh | ReLU | GELU |
|---|---|---|---|---|
| 수식 | $\frac{1}{1+e^{-z}}$ | $\frac{e^z-e^{-z}}{e^z+e^{-z}}$ | $\max(0, z)$ | $z \cdot \Phi(z)$ |
| 출력 범위 | $(0, 1)$ | $(-1, 1)$ | $[0, \infty)$ | 약 $(-0.17, \infty)$ |
| 원점 대칭 | 아니오 (Zero-centered 아님) | 예 (Zero-centered) | 아니오 | 아니오 |
| 기울기 소실 | 극심함 ($\sigma' \le 0.25$) | 존재함 ($\tanh' \le 1$) | 양수 구간 완전 해결 | 양수 구간 완전 해결 |
| 주 활용처 | 이진 분류 최종 출력층 | 과거 순환 신경망(RNN) | CNN/일반 심층망 은닉층 | BERT, GPT 등 트랜스포머 |

## 이렇게 출제된다
- 미출 대비: "인공신경망 활성화 함수의 필요성과 Sigmoid, Tanh, ReLU의 특성 비교 및 기울기 소실 관점의 발전 과정" → 요구 포인트: 비선형성 부여 이유, 도함수 그래프 분석, ReLU의 장단점(Dying ReLU)
