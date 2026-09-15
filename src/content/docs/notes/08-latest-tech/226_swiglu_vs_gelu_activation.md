---
sidebar:
  order: 226
  label: "226. SwiGLU•GELU 활성화 함수 비교"
  badge:
    text: "미출 · 50%"
    variant: note
title: "SwiGLU•GELU 활성화 함수 비교 (Activation Functions)"
date: "2026-09-15T11:58:00+09:00"
tags:
  - "notes-latest_tech"
weight: 226
extra:
  question_no: "226"
  source_status: "미출"
  source_history: ""
  priority: 50
  priority_note: "LLM 피드포워드 활성화•연산량 선택"
---

## Ⅰ. 개요

- **정의**: 트랜스포머(Transformer) 피드포워드 신경망(FFN)에서 단일 선형 변환 후 정규분포 기반 비선형성을 적용하는 GELU와, 스위시(Swish) 게이트와 값 경로의 원소별 곱(Element-wise Product)을 통해 입력 적응적 신호 제어를 수행하는 SwiGLU 활성화 함수
- **배경 및 필요성**: 기존 GELU 기반 단일 경로 FFN의 입력 문맥에 따른 동적 특징 선택 한계와 표현력 정체를 극복하고, 매개변수 수를 보정한 동일 계산 예산 하에서 더 빠른 학습 수렴과 높은 벤치마크 성능을 달성하는 최신 LLM(LLaMA, Mistral 등) 아키텍처를 구현하기 위해 도입됨

## Ⅱ. 특징

- **입력 적응적 곱셈 게이팅(Multiplicative Gating)**: SwiGLU는 $\text{Swish}(xW) \otimes (xV)$ 구조를 통해 입력 데이터의 중요도에 따라 활성화 신호의 통과량을 동적으로 스케일링
- **GELU의 단순성 및 연산 효율**: GELU는 단일 행렬 곱셈 후 비선형 함수를 적용하여 구현이 단순하고 메모리 대역폭 소모가 적음
- **파라미터 보정 은닉 차원 스케일링**: SwiGLU 도입 시 3개의 가중치 행렬이 필요하므로, 기존 $4d$ 대신 약 $\frac{8}{3}d$로 은닉 차원을 축소하여 전체 파라미터 수 유지

## Ⅲ. 구조 및 구성요소

```text
[활성화 함수 아키텍처 비교]
├── [입력 계층]
│   └── [입력 특징]
├── [GELU 단일 경로]
│   └── [GELU 투영]
├── [SwiGLU 이중 게이트 경로]
│   ├── [게이트 투영]
│   ├── [값 투영]
│   └── [요소별 결합]
└── [출력 투영 계층]
    └── [출력 투영]
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 계층 | 구성요소 | 핵심 역할 |
|:---|:---|:---|
| 입력 | 입력 특징 벡터 ($x$) | 트랜스포머 멀티헤드 어텐션(MHA) 정규화 계층을 통과한 토큰별 $d_{model}$ 차원 임베딩 |
| GELU 경로 | 단일 확장 투영 ($W_1$) | $d_{model}$ 차원을 $4d_{model}$ 은닉 차원으로 확장하고 $\text{GELU}(z) = z \cdot \Phi(z)$ 비선형 함수 적용 |
| SwiGLU 경로 | 게이트 투영 ($W$) | 입력을 선형 변환한 후 $\text{Swish}_\beta(z) = z \cdot \sigma(\beta z)$ 활성화를 적용하여 게이트 마스크 생성 |
| SwiGLU 경로 | 값 투영 ($V$) | 비선형 활성화 없이 게이트 신호와 원소별로 곱해질 독립적인 선형 특징 벡터 생성 |
| SwiGLU 경로 | 요소별 결합 ($\otimes$) | 게이트 벡터와 값 벡터 간 Hadamard 곱을 수행하여 입력 문맥 기반 동적 신호 통과 제어 |
| 출력 투영 | 다운 프로젝션 ($W_2$) | 은닉 차원의 활성화된 특징 벡터를 다시 원래의 $d_{model}$ 차원으로 축소 복원 |

## Ⅳ. 흐름도

```text
[토큰 임베딩 입력] (① 이전 어텐션 블록의 정규화된 은닉 상태 $x$ 수신)
       │
       ▼
[경로별 선형 투영] (② GELU 단일 경로 투영 vs SwiGLU 병렬 게이트(W) 및 값(V) 투영)
       │
       ▼
[비선형 활성화 및 게이팅] (③ GELU 연산 적용 vs Swish 게이트와 값 벡터의 원소별 곱 연산)
       │
       ▼
[출력 다운 프로젝션] (④ 중간 은닉 차원을 원래 모델 차원 $d_{model}$로 축소 변환)
       │
       ▼
[잔차 연결 및 정규화] (⑤ 입력 $x$와의 Residual Add 및 RMSNorm 수행 후 다음 레이어로 전달)
```

- 분기 결과: 연산 결과 출력 텐서의 정밀도와 수렴 손실(Loss)을 확인하여 안정적 그래디언트 흐름이 검증되면 다음 트랜스포머 블록으로 전이하고, 수치 오버플로 발생 시 FP16/BF16 스케일링 보정

## Ⅴ. 종류 및 비교

| 구분 | GELU (Gaussian Error Linear Unit) | SwiGLU (Swish Gated Linear Unit) | ReLU (Rectified Linear Unit) |
|:---|:---|:---|:---|
| 수학적 수식 | $x \cdot \Phi(x) \approx x \cdot \sigma(1.702x)$ | $\text{Swish}_1(xW) \otimes (xV)$ | $\max(0, x)$ |
| FFN 가중치 행렬 수 | 2개 (Up, Down) | 3개 (Gate, Up, Down) | 2개 (Up, Down) |
| 표준 은닉 차원 폭 | $4d_{model}$ | $\frac{8}{3}d_{model} \approx 2.67d_{model}$ | $4d_{model}$ |
| 표현력 및 수렴 속도 | 중간 수준 (단일 비선형 매핑) | 매우 우수 (입력 적응적 게이팅) | 낮음 (음수 영역 그래디언트 소실) |
| 주요 채택 모델 | GPT-2, GPT-3, BERT, ViT | LLaMA 1/2/3, Mistral, PaLM, Gemma | 원조 Transformer (2017), 초기 CNN |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 기대효과 |
|:---|:---|:---|
| SwiGLU 채택 시 3개 행렬 곱셈으로 인해 기존 $4d$ 은닉 차원을 유지할 경우 총 파라미터 수가 50% 급증 | 은닉 차원을 $\frac{2}{3} \times 4d = \frac{8}{3}d_{model}$로 축소하고 하드웨어 친화적 256의 배수로 올림 정렬 | 동일한 파라미터 수 및 FLOPs 예산 하에서 표현력 극대화 |
| 분기된 Gate와 Up 투영의 개별 커널 호출로 인한 GPU 글로벌 메모리 읽기/쓰기 대역폭 병목 | Triton 또는 CUDA 기반 융합 커널(Fused SwiGLU Kernel)을 적용하여 온칩 SRAM 내에서 단일 패스 처리 | 메모리 대역폭 오버헤드 해소 및 추론 지연시간 20~30% 단축 |
| bfloat16 학습 시 Swish 함수의 시그모이드 지수 연산에서 발생하는 국소적 언더플로 및 정밀도 손실 | 지수 연산 클램핑(Clamping) 및 수치적으로 안정한 $\text{x} \cdot \text{sigmoid}(x)$ 내장 최적화 함수 활용 | 학습 도중 Loss 발산 방지 및 안정적인 초장기 사전 학습 보장 |

## Ⅶ. 결론

- **기술 위상/발전**: SwiGLU는 LLaMA, PaLM, Mistral, DeepSeek 등 현대 프론티어 LLM의 피드포워드 신경망(FFN)에서 사실상의 표준(De Facto Standard)으로 안착하였으며, MoE(Mixture of Experts) 아키텍처의 개별 전문가 FFN 단위로도 전면 채택되는 추세
- **실무 적용/통제**: 차세대 거대 언어 모델 설계 시 파라미터 예산 유지를 위해 은닉 차원을 $\frac{8}{3}d$로 정밀 보정하고, 3중 행렬 곱셈에 따른 메모리 병목을 극복하기 위해 FlashAttention 및 Triton 융합 SwiGLU 커널을 기본 탑재하여 학습 및 추론 효율을 극대화 필요
