---
title: "EfficientNet"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  order: 137
  label: "137. EfficientNet"
  badge:
    text: "응용"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "응용"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

<div class="itpe-topic-path" aria-label="지식 경로">
  <span class="itpe-path-step">최신 기술</span>
  <span class="itpe-path-chevron">›</span>
  <span class="itpe-path-step">인공지능 및 컴퓨터 비전</span>
  <span class="itpe-path-chevron">›</span>
  <span class="itpe-path-step">합성곱 신경망(CNN) 경량화</span>
  <span class="itpe-path-chevron">›</span>
  <span class="itpe-path-step">EfficientNet</span>
</div>

## 30초 인출
- 본질: 합성곱 신경망(CNN)의 3대 확장 요소인 네트워크 깊이(Depth), 너비(Width), 입력 해상도(Resolution)를 수학적 복합 계수(Compound Coefficient)로 균형 있게 동시 스케일링한 고효율 이미지 분류 모델 계열
- 메커니즘: MNAS 기반 경량 베이스라인 모델(B0) 탐색 → 2단계 복합 스케일링 법칙(Compound Scaling Law) 수립 → 자원 제약 계수 $\phi$ 확장에 따른 B1~B7 모델 계열화 → 고효율 추론 달성
- 통찰: 임의의 단일 차원 확장 시 조기 성능 포화 및 연산 비효율이 발생하므로 세 차원의 연산량 증가율을 $2^\phi$로 통제하는 기하학적 균형 스케일링 및 타깃 NPU 컴파일 필수

<details><summary>핵심 용어</summary>

- **EfficientNet:** Google Research에서 제안한 아키텍처로, 복합 스케일링 기법을 통해 기존 ConvNet 대비 최대 8.4배 적은 파라미터로 최고 수준의 Top-1 정확도를 달성한 CNN 모델군
- **복합 스케일링(Compound Scaling):** 네트워크의 깊이($\alpha$), 너비($\beta$), 해상도($\gamma$)를 단일 복합 계수($\phi$)에 맞추어 $\alpha \cdot \beta^2 \cdot \gamma^2 \approx 2$의 제약식으로 비례 확장하는 방법론
- **MBConv(Mobile Inverted Bottleneck Convolution):** 저차원 입력 → 1x1 점별 확장 → 3x3/5x5 깊이별 분리 합성곱(Depthwise Separable Conv) → SE(Squeeze-and-Excitation) → 1x1 투영 잔차 연결 구조
- **Squeeze-and-Excitation(SE):** 전역 풀링으로 채널별 통계량을 압축(Squeeze)하고 완전연결층을 통해 채널 간 중요도 가중치를 자가 재조정(Excitation)하는 어텐션 모듈
- **MNAS(Multi-objective Neural Architecture Search):** 정확도와 실기기 추론 지연시간(Latency)을 동시에 최적화하는 강화학습 기반 신경망 구조 자동 탐색 기법

</details>

---

## 2~4교시 예상문제 (25점)
> 합성곱 신경망의 효율적 확장을 제시한 EfficientNet의 개념, 핵심 요소 기술(베이스라인 B0, MBConv 블록, 복합 스케일링 원리), 기존 단일 축 스케일링과의 비교 및 산업적 적용 방안을 설명하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. EfficientNet의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 네트워크의 깊이(Depth), 너비(Width), 해상도(Resolution)를 독립적으로 늘리는 대신 일정한 고정 비율로 균형 있게 동시 확장하는 복합 스케일링 기반의 고효율 합성곱 신경망(CNN) |
| 목적 | 한정된 컴퓨팅 자원(FLOPs/Memory) 제약 하에서 파라미터 낭비를 방지하고, 모델 용량(Capacity)과 일반화 표현력을 수학적으로 최적화 |

## Ⅱ. EfficientNet의 핵심 특징

| 특징 영역 | 주요 특성 | 기술적 구현 내용 |
|---|---|---|
| **수학적 균형 확장** | 복합 계수 $\phi$ 기반 스케일링 | $d = \alpha^\phi, w = \beta^\phi, r = \gamma^\phi$ 수식을 통해 연산량 증가를 엄밀히 $2^\phi$ 배로 제어 |
| **고효율 백본 구조** | MBConv + SE 블록 융합 | Depthwise Separable Conv로 파라미터를 줄이고 Squeeze-and-Excitation으로 채널 어텐션 강화 |
| **최적 베이스라인** | MNAS 기반 B0 모델 탐색 | 정확도와 모바일 기기 레이턴시를 다중 목적 함수로 결합하여 초기 기준망 B0 도출 |
| **압도적 파라미터 효율** | Top-1 정확도 84.3% 달성 | 기존 GPipe 대비 8.4배 작고 추론 속도가 6.1배 빠른 B7 모델을 통해 최고 성능 입증 |

## Ⅲ. EfficientNet 아키텍처 및 복합 스케일링 메커니즘

### 1. 베이스라인 모델(B0) 및 MBConv 블록 구조
```text
+-----------------------------------------------------------------------------------+
|                        EfficientNet-B0 및 MBConv 블록 상세                        |
+-----------------------------------------------------------------------------------+
|  [EfficientNet-B0 스테이지 파이프라인]                                            |
|    입력 (224x224x3) ──> Conv3x3 ──> MBConv1 (3x3) ──> MBConv6 (3x3, 5x5 반복)     |
|    ──> Conv1x1 & Pooling & FC ──> 출력 (1000 Class 분류)                         |
+-----------------------------------------------------------------------------------+
                               │
                               ▼
+-----------------------------------------------------------------------------------+
|  [MBConv6 블록 내부 데이터 연산 흐름]                                             |
|                                                                                   |
|    입력 텐서 (H x W x C)                                                          |
|       │                                                                           |
|       ▼                                                                           |
|    [1x1 Conv 확장] ──> 채널을 6배 확장 (H x W x 6C)                              |
|       │                                                                           |
|       ▼                                                                           |
|    [3x3 or 5x5 Depthwise Conv] ──> 공간적 특징 추출 (H/s x W/s x 6C, Swish 활성화) |
|       │                                                                           |
|       ▼                                                                           |
|    [Squeeze-and-Excitation (SE)] ──> 채널별 중요도(가중치) 재조정                  |
|       │                                                                           |
|       ▼                                                                           |
|    [1x1 Conv 축소 (Linear)] ──> 원래 채널로 투영 (H/s x W/s x C)                  |
|       │                                                                           |
|       ▼ (Residual Connection: stride=1 && input_c==output_c 일 때 덧셈)           |
|    출력 텐서 = [입력 텐서 + 변환 텐서]                                           |
+-----------------------------------------------------------------------------------+
```

### 2. 복합 스케일링(Compound Scaling) 수식 및 제약조건
```text
[복합 스케일링 수식 체계]
  - 깊이(Depth):      d = α^φ   (레이어 수 확장)
  - 너비(Width):      w = β^φ   (채널 수 확장)
  - 해상도(Resolution): r = γ^φ   (입력 이미지 크기 확장)

[최적화 제약 조건]
  α · β^2 · γ^2 ≈ 2   (단, α ≥ 1, β ≥ 1, γ ≥ 1)
  (FLOPs 는 깊이에 비례(d), 너비의 제곱에 비례(w^2), 해상도의 제곱에 비례(r^2)하므로
   전체 모델의 연산량은 대략 2^φ 배로 정밀하게 증가)
```

## Ⅳ. 단일 축 확장과의 비교 및 B0~B7 모델 패밀리

### 1. 단일 축 확장(Single-dimension Scaling) 대비 비교
| 비교 방식 | 확장 방식 및 대상 | 장점 | 치명적 한계 |
|---|---|---|---|
| **Depth 확장 (ResNet)** | 망의 깊이(레이어 수)만 확장 | 풍부하고 복잡한 특징 포착 가능 | 망이 깊어질수록 그래디언트 소실 및 정확도 향상 조기 포화 |
| **Width 확장 (WideResNet)** | 레이어의 채널(너비)만 확장 | 미세 단위 특징 학습 용이, 병렬 연산 우수 | 채널만 과도하게 증가 시 극도로 얕은 특징에 머물고 성능 한계 도달 |
| **Resolution 확장** | 입력 이미지 픽셀 크기만 확장 | 미세한 시각 패턴 검출 유리 | 고해상도 연산량 급증 대비 수용 영역(Receptive Field) 부족으로 포화 |
| **복합 스케일링 (EfficientNet)** | Depth, Width, Resolution 동시 확장 | 세 요소 간 상호 보완으로 연산 효율 및 정확도 극대화 | 단일 축 최적화 대비 하이퍼파라미터 탐색 복잡도 존재 |

### 2. EfficientNet B0 ~ B7 모델군 사양 비교
| 모델명 | 입력 해상도 ($R$) | 파라미터 수 (Params) | 연산 복잡도 (FLOPs) | ImageNet Top-1 정확도 |
|---|---|---|---|---|
| **EfficientNet-B0** | 224 x 224 | 5.3M | 0.39B | 77.1% |
| **EfficientNet-B2** | 260 x 260 | 9.2M | 1.0B | 80.1% |
| **EfficientNet-B4** | 380 x 380 | 19M | 4.2B | 82.9% |
| **EfficientNet-B7** | 600 x 600 | 66M | 37B | 84.3% |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| **고해상도 모델(B6, B7)의 추론 지연시간(Latency) 증가**<br />큰 입력 해상도로 인해 메모리 접근 비용(MACs)이 급증하여 모바일/임베디드 실시간 서빙 저해 | 엣지 디바이스에서는 B0~B3 경량 모델 우선 채택, 채널 분할 및 Fused-MBConv가 적용된 EfficientNetV2 아키텍처로 고도화 |
| **Depthwise Conv 연산의 특정 GPU 하드웨어 가속 비효율**<br />NVIDIA 텐서 코어 등 하드웨어는 일반 Conv 대비 연산 강도가 낮은 Depthwise Conv에서 메모리 대역폭 병목 발생 | 텐서 컴파일러(TensorRT)를 통한 수직 레이어 융합(Vertical Layer Fusion) 및 연산자 커널 튜닝 적용 |
| **학습 수렴 난이도 및 긴 학습 시간**<br />스케일링이 커질수록 규제(Regularization) 강도 조정이 어렵고 과적합 위험 증가 | Stochastic Depth(Drop-path), AutoAugment, 라벨 스무딩(Label Smoothing) 기법을 모델 규모에 맞춰 동적 조절 |

## Ⅵ. 제언

EfficientNet은 영상 분류를 넘어 객체 탐지(EfficientDet), 의미론적 분할(Segmentation)의 공통 백본으로 활용되며, 모바일 엣지부터 거대 클라우드 비전 시스템까지 확장 가능한 비전 표준 아키텍처 구축 필수.

```text
[EfficientNet 백본] ──> [객체 탐지: EfficientDet (BiFPN)] ──> [엣지 서빙: TensorRT INT8 양자화]
```

| 진화 단계 | 1세대 EfficientNet (V1) | 2세대 EfficientNet (V2) |
|---|---|---|
| **핵심 블록** | 순수 MBConv (Depthwise 위주) | Fused-MBConv (표준 Conv와 결합하여 학습 가속) |
| **스케일링 전략** | 고정 비율 복합 스케일링 | 점진적 학습(Progressive Learning: 이미지 크기 동적 조절) |
| **학습 속도** | 대형 모델 학습 시 긴 훈련 소요 | V1 대비 최대 11배 빠른 훈련 속도 및 경량 파라미터 구현 |

---

## 출제 이력과 검증 출처
- 정보관리기술사 제137회 대비 모의검증 및 딥러닝 영상 인식 아키텍처
- Mingxing Tan, Quoc V. Le (Google Research): EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks (ICML 2019)
- Mingxing Tan, Quoc V. Le: EfficientNetV2: Smaller Models and Faster Training (ICML 2021)

## 연결 토픽
- EfficientDet
- 파라미터(Parameter)
- 컴퓨터 비전
- 지능형 CCTV
