---
title: "트랜스포머(Transformer)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 트랜스포머(Transformer)의 개요

- 개념 : 기존 **순환 신경망** (RNN, Recurrent Neural Network)과 **합성곱** (CNN, Convolutional Neural Network)의 순차적(Sequential) 처리 방식을 완전히 배제하고, 시퀀스 내 모든 토큰 간의 상호 연관성을 동시에 계산하는 **셀프 어텐션** (Self-Attention) 메커니즘을 핵심 기반으로 설계된 현대 인공지능 및 거대언어모델(LLM, Large Language Model)의 표준 인공신경망 아키텍처.
- 배경 및 필요성 : RNN(Recurrent Neural Network)은 이전 시점(t-1)의 은닉 상태를 순차적으로 전달받아야 하므로 병렬 학습이 불가능하고, 문장이 길어질수록 초기 정보가 소실되는 **장기 의존성** (Long-term Dependency) 문제가 심각하여 구글의 "Attention Is All You Need"(2017) 논문을 통해 제안됨.
- 핵심 목적 : 시퀀스 데이터의 **전역적 문맥** (Global Context) 모델링, 대규모 GPU(Graphics Processing Unit) 분산 병렬 학습 극대화, 자연어 처리를 넘어 컴퓨터 비전(ViT, Vision Transformer), 로보틱스(VLA, Vision-Language-Action)에 이르는 단일 백본 통합.

## Ⅱ. 트랜스포머(Transformer)의 핵심 아키텍처 및 동작 메커니즘

트랜스포머는 입력 토큰들을 Query, Key, Value 벡터로 투영하여 내적 어텐션을 수행하는 **스케일드 닷 프로덕트 어텐션**과 멀티헤드 어텐션(MHA, Multi-Head Attention)으로 구성됨.

```text
[ 트랜스포머 스케일드 닷 프로덕트 및 멀티헤드 어텐션(MHA) 메커니즘 ]

  입력 시퀀스 X (N x d_model)
        │
        ├─────────────────► Q = X · W_Q  (Query: 찾고자 하는 질문)
        ├─────────────────► K = X · W_K  (Key: 토큰들의 식별 레이블)
        └─────────────────► V = X · W_V  (Value: 토큰들이 가진 실제 정보)
                                  │
                                  ▼
+-----------------------------------------------------------------+
| 스케일드 닷 프로덕트 어텐션 (Scaled Dot-Product Attention)       |
|                                                                 |
|   어텐션 맵 (유사도) : S = (Q · K^T) / sqrt(d_k)                |
|   소프트맥스 확률   : A = Softmax( S + Mask )                  |
|   최종 문맥 출력    : Attention(Q, K, V) = A · V                |
+--------------------------------┬--------------------------------+
                                 │
                                 ▼
+-----------------------------------------------------------------+
| 멀티헤드 어텐션 (Multi-Head Attention, MHA)                     |
|  - h개의 독립된 헤드로 나누어 서로 다른 표현 공간(Subspace) 학습|
|  - MultiHead(Q,K,V) = Concat(head_1, ... head_h) · W_O          |
+--------------------------------┬--------------------------------+
                                 │
                                 ▼
+-----------------------------------------------------------------+
| 잔차 연결 및 피드포워드 (Add & Norm ──► FFN, Feed-Forward Network ──► Add & Norm) |
|  - Residual Connection (x + Sublayer(x)) + RMSNorm / LayerNorm  |
|  - Position-wise Feed-Forward Network (SwiGLU / GeLU 활성화)     |
+-----------------------------------------------------------------+
```

- **Query, Key, Value 메커니즘** : 정보 검색 시스템처럼 질의(Query)와 대상(Key) 간의 유사도를 코사인 내적으로 산출하고, 이를 가중치로 삼아 내용(Value)을 가중 합산.
- **스케일링 인자(`sqrt(d_k)`)** : 차원이 커질수록 내적 결과값이 극단적으로 커져 소프트맥스의 기울기가 소실(Vanishing Gradient)되는 현상을 방지하기 위해 정규화.
- **멀티헤드 어텐션(MHA)** : 단일 어텐션 대신 여러 개의 헤드(예: 32개)로 병렬 투영하여 문법적 관계, 의미론적 관계, 수식 관계 등 다양한 문맥을 동시에 포착.
- **위치 인코딩(Positional Encoding)** : 순차 처리가 없는 트랜스포머의 특성상 토큰의 어순 정보를 주입하기 위해 절대적 사인/코사인 인코딩 또는 RoPE(회전 위치 임베딩) 적용.

## Ⅲ. 트랜스포머(Transformer)의 세부 구성 요소 및 비교 분석

| 비교 항목 | 인코더-디코더 (Vanilla Transformer, T5) | 인코더 전용 (Encoder-only, BERT) | 디코더 전용 (Decoder-only, GPT, Llama) |
| --- | --- | --- | --- |
| **어텐션 마스킹** | 인코더: 양방향 / 디코더: 인과적 마스킹 | 모든 토큰 간 양방향(Bidirectional) 어텐션 | 미래 토큰을 가리는 인과적 마스킹(Causal Mask) |
| **주요 학습 목표**| Seq2Seq 기계 번역, 요약 | 마스크드 언어 모델 (MLM / 중간 빈칸 맞추기) | 다음 토큰 예측 (Autoregressive Next-Token) |
| 장점 | 입력과 출력이 상이한 변환 태스크 최적화 | 문맥 전체에 대한 깊은 양방향 언어 이해 | 자유로운 텍스트 생성, Few-shot 인컨텍스트 학습 |
| 단점 | 복합 구조로 인한 연산 및 서빙 복잡도 | 텍스트 생성 작업 불가 (분류/추출에 한정) | 이전 토큰만 참조 가능 (단방향 제약) |
| **대표 모델** | Google T5(Text-to-Text Transfer Transformer), BART | BERT(Bidirectional Encoder Representations from Transformers), RoBERTa(Robustly Optimized BERT Pretraining Approach) | GPT(Generative Pre-trained Transformer)-4o, Llama 3, Claude 3.5, DeepSeek-V3 |

- 현대 생성형 AI(Artificial Intelligence) 혁명은 구조가 단순하고 확장성(Scaling Law)이 뛰어난 **디코더 전용** (Decoder-only) 아키텍처로 완전히 수렴함.

## Ⅳ. 트랜스포머(Transformer)의 주요 한계점 및 해결 방안

- 시퀀스 길이(N)에 대해 O(N^2)으로 폭증하는 어텐션 연산 및 메모리 복잡도 :
  - 한계점 : 컨텍스트 길이가 128k, 1M으로 증가할 때 어텐션 행렬의 크기가 기하급수적으로 폭증하여 GPU VRAM(Video Random-Access Memory) 고갈(OOM, Out of Memory).
  - 해결 방안 : IO-Aware 기법으로 HBM(High Bandwidth Memory) 접근을 최소화하는 **FlashAttention-3** 도입 및 긴 문맥 분산 처리를 위한 **RingAttention** 적용.
- 추론 시 순차적 토큰 생성으로 인한 KV(Key-Value) 캐시 메모리 대역폭 병목 :
  - 한계점 : 이전 생성 토큰들의 Key, Value를 캐싱해야 하므로 동시 사용자가 많을 때 GPU 메모리 대역폭 고갈.
  - 해결 방안 : **Multi-Query Attention** (MQA), **Grouped-Query Attention** (GQA), **Multi-head Latent Attention** (MLA) 등 압축 어텐션 도입.
- 순환 구조 부재로 인한 상대적 위치 추론 및 외삽(Extrapolation) 한계 :
  - 한계점 : 학습된 컨텍스트 길이보다 긴 입력이 들어왔을 때 모델의 어텐션이 무너지는 현상.
  - 해결 방안 : 복소수 평면 회전을 이용하는 **RoPE** (Rotary Position Embedding) 및 주파수 보간(YaRN) 스케일링 기법 적용.

## Ⅴ. 트랜스포머(Transformer) 적용 및 발전을 위한 기술사적 제언

- FlashAttention 및 커널 융합(Kernel Fusion) 서빙 인프라 필수 구축 : 소프트웨어 알고리즘뿐만 아니라 하드웨어 SRAM(Static Random-Access Memory)과 HBM 간의 메모리 계층 구조를 최적화하는 서빙 스택 내재화.
- KV 캐시 압축 및 투영 기술(MLA)을 적용한 추론 가속화 : DeepSeek-V3처럼 저차원 잠재 공간으로 Key/Value를 압축 투영하여 동시 처리 배치 크기 극대화.
- 비전(ViT, Vision Transformer) 및 로보틱스(VLA) 분야로의 단일 멀티모달 트랜스포머 통합 : 텍스트 토큰과 시각 패치(Patch) 토큰을 단일 트랜스포머 레이어에서 통합 처리하는 통합 인텔리전스 설계.
