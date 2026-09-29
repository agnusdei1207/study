---
title: "트랜스포머(Transformer)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "054. 트랜스포머"
  order: 54
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>인공지능</span><span>딥러닝 아키텍처</span><strong>트랜스포머(Transformer)</strong></div>

## 30초 인출

- 본질: **트랜스포머(Transformer)** 는 순환(RNN)이나 합성곱(CNN)을 배제하고 셀프 어텐션(Self-Attention) 메커니즘만으로 시퀀스 데이터 내 모든 토큰 간의 상관관계를 병렬 계산하는 딥러닝 신경망 아키텍처
- 메커니즘: 토큰 및 위치 인코딩 결합 → Q, K, V 선형 투영 → 스케일드 닷 프로덕트 어텐션 및 소프트맥스 가중 합산 → 멀티헤드 통합 → FFN 및 잔차 정규화
- 통찰: 시퀀스 길이 증가 시 O(N^2) 연산 및 KV 캐시 메모리 병목이 발생하므로 FlashAttention 하드웨어 최적화와 Grouped-Query Attention(GQA)을 결합한 경량 서빙 구현 필수

<details><summary>핵심 용어</summary>

- **트랜스포머(Transformer)** : 어텐션 메커니즘을 전면에 내세워 자연어와 시계열, 비전 데이터를 대규모 병렬 처리하는 표준 신경망.
- **셀프 어텐션(Self-Attention)** : 동일 시퀀스 내의 모든 단어 쌍 간의 문맥적 연관성을 쿼리(Q)와 키(K)의 내적으로 직접 계산하는 연산.
- **멀티헤드 어텐션(Multi-Head Attention)** : 어텐션을 여러 개의 부분 공간(Head)으로 분할하여 다양한 의미론적 관계를 독립적으로 포착하는 구조.
- **위치 인코딩(Positional Encoding)** : 순차 처리를 하지 않는 트랜스포머에서 단어 간의 순서 정보를 벡터에 주입하는 삼각함수 또는 회전(RoPE) 기법.
- **Grouped-Query Attention(GQA)** : Key와 Value 헤드를 여러 Query 헤드가 공유하여 추론 시 KV 캐시 메모리를 획기적으로 절감하는 기법.

</details>

---

## 2~4교시 예상문제 (25점)

> 현대 초거대 AI의 근간이 되는 트랜스포머(Transformer) 아키텍처의 핵심 원리와 셀프 어텐션(Self-Attention) 연산 메커니즘을 설명하고, 전통 순환신경망(RNN)과의 구조적 비교 및 긴 문맥 처리 시의 계산 복잡도 한계 극복 방안을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 트랜스포머(Transformer)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **트랜스포머(Transformer)** 는 순환(Recurrence) 구조를 완전히 배제하고, 어텐션(Attention) 메커니즘만을 활용하여 시퀀스 내 토큰 간의 전역적 상호작용을 병렬 처리하는 딥러닝 인코더-디코더 모델 |
| 목적 | 순차 계산 병목 제거를 통한 GPU 대규모 분산 학습 가속화 및 장기 의존성(Long-term Dependency) 기울기 소실 문제의 근본적 해결 |

## Ⅱ. 트랜스포머의 핵심 특징

| 구분 | 주요 특징 | 기술적 설명 및 메커니즘 |
|---|---|---|
| **학습 병렬화** | 순환 없는 완전 병렬 처리 | 시퀀스 전체를 한 번에 행렬 연산으로 투입하여 이전 시점의 은닉 상태를 대기할 필요 없음 |
| **장기 기억력** | 상수 시간 O(1) 경로 거리 | 임의의 두 단어 간 참조 거리가 1로 고정되어 문서 내 거리가 먼 단어 간 문맥도 손실 없이 포착 |
| **다차원 인지** | 멀티헤드 어텐션 (MHA) | h개의 독립된 어텐션 헤드가 문법적, 의미론적, 인과적 관계를 서로 다른 부분공간에서 동시 학습 |
| **위치 보존** | 위치 인코딩 (Position Embedding) | 순서 정보가 없는 집합 연산 특성을 보완하기 위해 사인·코사인 주기함수 또는 RoPE 벡터 가산 |

## Ⅲ. 트랜스포머 아키텍처 및 셀프 어텐션 연산 체계

```text
┌────────────────────────────────────────────────────────────────────────┐
│             [ 트랜스포머 인코더-디코더 블록 아키텍처 및 어텐션 흐름 ]       │
└────────────────────────────────────────────────────────────────────────┘
          [ 인코더 (Encoder) ]                     [ 디코더 (Decoder) ]
                   │                                         │
                   ▼                                         ▼
        [ 토큰 + 위치 인코딩 ]                    [ 출력 토큰 + 위치 인코딩 ]
                   │                                         │
                   ▼                                         ▼
        ┌─────────────────────┐                   ┌─────────────────────┐
        │ Multi-Head Self-Attn │                   │ Masked Self-Attention│
        └──────────┬──────────┘                   └──────────┬──────────┘
                   │ Add & LayerNorm                         │ Add & LayerNorm
                   ▼                                         ▼
        ┌─────────────────────┐                   ┌─────────────────────┐
        │ Feed Forward Network│                   │ Cross Multi-Head Attn│◄──[ K, V ]
        └──────────┬──────────┘                   └──────────┬──────────┘
                   │ Add & LayerNorm                         │ Add & LayerNorm
                   ▼                                         ▼
        [ 인코더 출력 (K, V) ]                    ┌─────────────────────┐
                                                  │ Feed Forward Network│
                                                  └──────────┬──────────┘
                                                             │ Add & LayerNorm
                                                             ▼
                                                  [ 선형층 & Softmax 확률 ]
```

| 연산 단계 | 세부 수학적 메커니즘 | 공학적 의미 |
|---|---|---|
| **선형 투영** | Q = X * W_Q, K = X * W_K, V = X * W_V | 입력 토큰을 쿼리, 키, 밸류 공간으로 분할 매핑 |
| **스케일드 내적** | S = (Q * K^T) / sqrt(d_k) | 쿼리와 키의 유사도 내적 및 차원 크기 정규화 (기울기 안정화) |
| **소프트맥스 가중** | A = softmax(S) | 모든 토큰에 대한 정규화된 어텐션 가중치 확률 분포 생성 |
| **밸류 가중 합산** | Output = A * V | 높은 유사도를 가진 토큰의 정보만을 선택적으로 집약 |

## Ⅳ. 전통 순환신경망(RNN/LSTM)과 트랜스포머 비교

| 비교 항목 | 순환신경망 (RNN / LSTM) | 어텐션 기반 트랜스포머 (Transformer) |
|---|---|---|
| **처리 구조** | 시점별 t_1 → t_2 순차 처리 (Sequential) | 전체 시퀀스 토큰 일괄 행렬 연산 (Parallel) |
| **정보 전달 거리** | O(N) 순차 전달 (거리 비례 정보 손실) | O(1) 직접 참조 (전역적 어텐션 맵) |
| **학습 시간 복잡도** | 시퀀스 길이에 따른 직렬 병목 발생 | GPU 코어를 활용한 대규모 분산 병렬 학습 |
| **시간·메모리 복잡도** | O(N) 선형 증가 (메모리 부담 적음) | O(N^2) 제곱 증가 (초장문맥 시 메모리 폭증) |
| **장기 의존성 한계** | 기울기 소실/폭주(Vanishing Gradient) | 잔차 연결(Residual)과 어텐션으로 완벽 해결 |
| **현대 파운데이션 적용** | 레거시 시계열 분석에 국한 | GPT, BERT, Llama, ViT 등 모든 거대 모델의 표준 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 시퀀스 길이 N이 증가함에 따라 어텐션 맵 계산 및 GPU HBM 메모리 점유율이 O(N^2)으로 폭증하여 문맥 창 확장 제한 | SRAM 타일링(Tiling) 및 연산 재계산(Recomputation)을 통해 HBM 접근을 최소화하는 FlashAttention-2/3 도입 및 회전 위치 임베딩(RoPE) 적용 |
| 자기회귀(Autoregressive) 생성 시 매 토큰 생성마다 이전 Key-Value 텐서를 캐싱하는 KV Cache 메모리 폭증 및 서빙 병목 | Key-Value 헤드를 공유하는 Grouped-Query Attention(GQA) 및 Multi-Query Attention(MQA) 구조 채택으로 캐시 크기 75% 절감 |
| 긴 시퀀스를 처리할 때 단일 GPU 메모리 용량을 초과하는 OOM(Out of Memory) 현상 발생 | GPU 클러스터 간 링 토폴로지 통신으로 어텐션 연산을 분산 수행하는 RingAttention 및 Context Parallelism 기법 적용 |

## Ⅵ. 제언

GQA 구조와 FlashAttention 커널 최적화, PagedAttention 메모리 가상화를 결합하여 128K 이상의 초장문맥을 초저지연으로 서빙하는 고효율 추론 아키텍처 구축.

```text
[ 사용자 초장문맥 입력 (128K 토큰) ]
                  │
                  ▼
[ 트랜스포머 고성능 추론 엔진 ]
   ├── Step 1: RoPE(Rotary Position Embedding) 기반 외삽(Extrapolation)
   ├── Step 2: GQA (Grouped-Query Attention) 적용으로 KV 캐시 메모리 1/8 압축
   ├── Step 3: FlashAttention-3 GPU SRAM IO 최적화 (HBM 메모리 병목 0화)
   └── Step 4: vLLM PagedAttention 가상 메모리 관리 (단편화 제거)
                  │
                  ▼
[ 초저지연 고처리량 텍스트 생성 응답 ]
```

| 구분 | 표준 Multi-Head Attention (MHA) | 제언: GQA + FlashAttention 최적화 |
|---|---|---|
| **메모리 복잡도** | HBM 빈번한 접근으로 O(N^2) 지연 | SRAM 내부 타일링 연산으로 선형 수준 단축 |
| **KV 캐시 용량** | 헤드 수만큼 비례하여 캐시 폭증 | 4~8개 쿼리가 1개 KV 공유하여 75% 이상 절감 |
| **동시 서빙량** | 긴 문맥 처리 시 배치 크기 1로 급감 | 메모리 단편화 제거로 동시 처리량 4배 향상 |

## 출제 이력과 검증 출처

- 제131회 정보관리기술사 1교시: Transformer의 Self-Attention 구조와 연산 과정
- Ashish Vaswani et al. (Google Brain), Attention Is All You Need
- Tri Dao et al., FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning
- Joshua Ainslie et al., GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

## 연결 토픽

- 상위 토픽: [079 인공신경망과 딥러닝](./079_deep_learning.md)
- 연관 토픽: [074 BERT](./074_bert.md), [071 초거대 AI](./071_hyperscale_ai.md), [073 멀티모달](./073_multimodal.md)
