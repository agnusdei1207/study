---
title: "EfficientDet"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  order: 136
  label: "136. EfficientDet"
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
  <span class="itpe-path-step">컴퓨터 비전 및 딥러닝</span>
  <span class="itpe-path-chevron">›</span>
  <span class="itpe-path-step">객체 탐지(Object Detection)</span>
  <span class="itpe-path-chevron">›</span>
  <span class="itpe-path-step">EfficientDet</span>
</div>

## 30초 인출
- 본질: 가중 양방향 피처 피라미드(BiFPN)와 객체 탐지 전용 복합 스케일링(Compound Scaling)을 적용하여 최소 연산량(FLOPs)으로 최고 수준의 정확도(mAP)를 달성한 고효율 객체 탐지 모델 계열
- 메커니즘: 입력 영상 → EfficientNet 백본 다중 스케일 피처(P3~P7) 추출 → BiFPN 양방향 가중치 융합 반복 → Class 및 Box 예측 헤드 분기 → Non-Maximum Suppression(NMS) 위치 확정
- 통찰: 이론적 FLOPs 감소에도 불구하고 복잡한 BiFPN의 다단계 텐서 결합이 엣지 NPU 가속기에서 메모리 대역폭 병목을 유발하므로 타깃 하드웨어 전용 텐서 컴파일 및 레이어 융합(Op Fusion) 필수

<details><summary>핵심 용어</summary>

- **EfficientDet:** Google Brain에서 제안한 경량·고정밀 객체 탐지 아키텍처로, 복합 스케일링을 통해 D0부터 D7까지 자원 제약별 최적 모델을 제공
- **BiFPN(Weighted Bi-directional Feature Pyramid Network):** 상하향 및 하상향 경로를 모두 구축하고 노드별 중요도 가중치를 학습하여 다중 스케일 특징을 융합하는 고효율 피라미드 네트워크
- **고속 정규화 융합(Fast Normalized Fusion):** Softmax 대신 연산량이 적은 정규화 나눗셈($\frac{w_i}{\epsilon + \sum w_j}$)을 적용하여 피처 융합 속도를 극대화한 방식
- **복합 스케일링(Compound Scaling):** 단일 계수 $\phi$를 기반으로 백본, BiFPN 폭/깊이, 예측 헤드, 입력 해상도를 균형 있게 동시 확장하는 기법
- **mAP(mean Average Precision):** 객체 탐지 모델의 정밀도와 재현율을 종합하여 검출 성능을 측정하는 대표적인 표준 평가지표

</details>

---

## 2~4교시 예상문제 (25점)
> 경량 고성능 객체 탐지 아키텍처인 EfficientDet의 개념, 양대 핵심 기술(BiFPN, 객체 탐지용 복합 스케일링), FPN 계열과의 구조적 비교 및 실시간 엣지 서빙 시 고려사항을 설명하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. EfficientDet의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | EfficientNet을 백본으로 삼아 가중 양방향 피처 피라미드(BiFPN)와 해상도·네트워크 규모를 조화롭게 확장하는 복합 스케일링을 결합한 1-Stage 객체 탐지 아키텍처 |
| 목적 | 객체 탐지 분야의 연산 복잡도와 메모리 사용량을 대폭 절감하면서도, 다양한 크기의 물체 검출 정확도(mAP)를 동시 극대화 |

## Ⅱ. EfficientDet의 핵심 특징

| 특징 영역 | 주요 특성 | 기술적 구현 내용 |
|---|---|---|
| **가중 양방향 피라미드** | BiFPN 기반 다중 해상도 융합 | 단방향 정보 전달의 한계를 극복하고 상하향/하상향 크로스 스케일 연결 반복 |
| **고속 가중치 정규화** | Fast Normalized Fusion 연산 | 지수 연산이 큰 Softmax 대신 0~1 사이로 정규화된 가중치 나눗셈을 통해 연산 지연 최소화 |
| **탐지용 복합 스케일링** | $\phi$ 기반의 4대 요소 동시 확장 | 백본(EfficientNet), BiFPN 폭/깊이, 박스/클래스 헤드, 입력 해상도를 단일 수식으로 확장 |
| **극단적 파라미터 효율** | 동일 mAP 기준 FLOPs 획기적 절감 | 기존 YOLOv3, RetinaNet 대비 최대 4~9배 적은 연산량과 파라미터로 상위 성능 달성 |

## Ⅲ. EfficientDet 아키텍처 및 BiFPN 융합 프로세스

### 1. EfficientDet 전체 시스템 아키텍처
```text
+-----------------------------------------------------------------------------------+
|                        EfficientDet (D0 ~ D7) 구조도                              |
+-----------------------------------------------------------------------------------+
|  [입력 영상] : R_input = 512 + phi * 128 (phi: 0 ~ 7)                             |
|       │                                                                           |
|       ▼                                                                           |
|  [EfficientNet 백본 네트워크] (B0 ~ B7)                                           |
|       │ ──> P3 (저수준 세부 특징)                                                 |
|       │ ──> P4                                                                    |
|       │ ──> P5                                                                    |
|       │ ──> P6                                                                    |
|       │ ──> P7 (고수준 의미 특징)                                                 |
+-----------------------------------------------------------------------------------+
                               │
                               ▼
+-----------------------------------------------------------------------------------+
|  [반복 가중 양방향 피처 피라미드: BiFPN 레이어] (D_bifpn = 3 + phi 회 반복)      |
|                                                                                   |
|    P7 ───(↓)───> [ P6 td ] ───(↓)───> [ P5 td ] ───(↓)───> [ P4 td ]              |
|                   │                     │                     │                   |
|                   ▼                     ▼                     ▼                   |
|    P3 ──────────> [ P3 out ] ──(↑)──> [ P4 out ] ──(↑)──> [ P5 out ] ──(↑)──> P7 |
|    (단방향 노드 제거, 양방향 잔차 연결, Fast Normalized Fusion 가중치 적용)        |
+-----------------------------------------------------------------------------------+
                               │
                               ▼
+-----------------------------------------------------------------------------------+
|  [공유 예측 헤드 (Shared Class & Box Prediction Net)]                             |
|    - Class Prediction Net  ──> 클래스 확률 분포 (Focal Loss 학습)                 |
|    - Box Prediction Net    ──> Bounding Box 회귀 좌표 (Smooth L1 Loss 학습)       |
+-----------------------------------------------------------------------------------+
```

### 2. Fast Normalized Fusion 연산 메커니즘
```text
[입력 피처 I_1 (가중치 w_1)] ──┐
                              ├──> O = Σ (w_i / (ε + Σ w_j)) * I_i ──> Swish 활성화
[입력 피처 I_2 (가중치 w_2)] ──┘
(Softmax 지수 연산 없이 GPU/NPU 상에서 초고속 병렬 계산 수행)
```

## Ⅳ. 피처 피라미드(FPN) 구조 비교 및 복합 스케일링 체계

### 1. FPN 계열 아키텍처 진화 비교
| 비교 항목 | 기존 FPN (Feature Pyramid) | PANet (Path Aggregation) | NAS-FPN | BiFPN (EfficientDet) |
|---|---|---|---|---|
| **연결 방향** | 단순 상하향(Top-down) 단방향 | 상하향 + 하상향 순차 연결 | 신경망 아키텍처 탐색(NAS) 불규칙 | 최적화된 양방향 정규 연결 |
| **노드 처리** | 1개 입력 엣지 노드 단순 통과 | 단순 합(Sum) 연산 결합 | 복잡한 비대칭 노드 결합 | 정보 기여 적은 단일 입력 제거 |
| **특징 가중치** | 동일 가중치(단순 합산) | 동일 가중치 단순 연결 | 비정형 결합 | 학습 가능한 정규화 가중치($w_i$) |
| **연산 효율** | 보통 | 연산량 및 지연시간 증가 | 불규칙 구조로 하드웨어 비효율 | 잔차 경로 추가 및 연산 최소화 |

### 2. EfficientDet 복합 스케일링(Compound Scaling) 수식 체계
| 확장 구성요소 | 스케일링 수식 ($ \phi $: 사용자 지정 계수) | 물리적 의미 |
|---|---|---|
| **백본 네트워크** | EfficientNet-$B\phi$ ($ \phi = 0 \sim 7 $) | ImageNet으로 사전 훈련된 기본 특징 추출기 |
| **BiFPN 폭 ($W$)** | $W_{bifpn} = 64 \times (1.35^\phi)$ | 피라미드 내 피처 맵 채널 수의 지수적 확장 |
| **BiFPN 깊이 ($D$)** | $D_{bifpn} = 3 + \phi$ | 양방향 피라미드 반복 횟수의 선형적 확장 |
| **탐지 헤드 깊이** | $D_{head} = 3 + \lfloor \phi / 3 \rfloor$ | 클래스 및 박스 예측 컨볼루션 레이어 수 확장 |
| **입력 해상도 ($R$)** | $R_{input} = 512 + \phi \times 128$ | 영상 입력 픽셀 크기 선형 증가 (512x512 ~ 1536x1536) |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| **이론적 FLOPs 대비 실제 엣지 서빙 지연(Latency) 상이**<br />BiFPN의 잦은 텐서 분기 및 결합(Concat/Split)으로 인해 GPU/NPU의 메모리 대역폭 병목(Memory-bound) 발생 | TensorRT/OpenVINO 기반 텐서 융합(Operator Fusion) 적용 및 하드웨어 특화 컴파일러를 통한 메모리 복사 최소화 |
| **고해상도(D6, D7) 모델에서의 초고용량 VRAM 요구**<br />스케일링 계수가 높아질수록 입력 해상도가 1536x1536에 달해 배치 크기 제약 및 학습 시간 폭증 | 그라디언트 누적(Gradient Accumulation), FP16/BF16 혼합 정밀도 학습 및 경량 D0~D3 위주의 실무 채택 |
| **초소형 객체(Small Object) 검출 성능의 국소적 저하**<br />P3 이상의 다운샘플링 피처만 활용하므로 극단적으로 작은 원거리 객체 감지율 미흡 | 저수준 고해상도 피처 P2를 피라미드에 추가 연결하는 커스텀 BiFPN 확장 또는 슬라이딩 윈도우 추론 기법 병행 |

## Ⅵ. 제언

EfficientDet은 모델 크기와 지연시간 간의 명확한 트레이드오프 기준을 제공하므로, 엣지(D0~D2)부터 클라우드 관제(D5~D7)까지 단일 아키텍처 기반의 계층적 AI 시스템 구축 필수.

```text
[엣지 디바이스: EfficientDet-D0/D1] ──(이상 객체 1차 탐지)──> [클라우드 서버: EfficientDet-D6/D7 정밀 분석]
```

| 적용 영역 | 엣지 온디바이스 (D0 ~ D2) | 클라우드 대규모 서버 (D5 ~ D7) |
|---|---|---|
| **주요 타깃** | 자율주행 임베디드, 스마트 CCTV, 모바일 | 초고해상도 위성 영상 분석, 대규모 관제 센터 |
| **요구 조건** | 초당 30fps 이상 실시간성, 저전력 구동 | 최대 mAP 정밀도 달성 및 다중 채널 동시 분석 |
| **최적화 기법** | INT8 양자화, 하드웨어 NPU 가속 컴파일 | 멀티 GPU 배치 분산 추론 및 고정밀 FP16 서빙 |

---

## 출제 이력과 검증 출처
- 정보관리기술사 제136회 대비 모의검증 및 컴퓨터 비전 객체 탐지 아키텍처
- Mingxing Tan, Ruoming Pang, Quoc V. Le (Google Brain): EfficientDet: Scalable and Efficient Object Detection (CVPR 2020)
- Tsung-Yi Lin et al.: Feature Pyramid Networks for Object Detection (CVPR 2017)

## 연결 토픽
- EfficientNet
- 파라미터(Parameter)
- 지능형 CCTV
- 복합 스케일링(Compound Scaling)
