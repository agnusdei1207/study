---
title: "BERT(Bidirectional Encoder Representations from Transformers)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "074. BERT"
  order: 74
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>자연어 처리</span><span>언어모델 아키텍처</span><strong>BERT</strong></div>

## 30초 인출

- 본질: **BERT(Bidirectional Encoder Representations from Transformers)** 는 트랜스포머 인코더 블록을 양방향으로 쌓아올려 문장 내 모든 단어의 좌우 양방향 문맥을 동시에 학습하는 자연어 이해(NLU) 특화 사전학습 언어모델
- 메커니즘: 3중 임베딩(Token+Segment+Position) 결합 → 마스크 언어 모델(MLM) 및 다음 문장 예측(NSP) 사전학습 → 하위 과업별 태스크 헤드 결합 미세조정(Fine-Tuning)
- 통찰: 자기회귀 생성이 불가능하고 사전학습과 미세조정 간 마스크 불일치가 존재하므로 문서 이해 및 검색 리랭커 전담 배치와 RoBERTa 동적 마스킹 기법 결합 필수

<details><summary>핵심 용어</summary>

- **BERT** : 트랜스포머의 양방향 자기주의집중 인코더를 활용하여 문맥화된 단어 임베딩을 사전학습하는 딥러닝 모델.
- **마스크 언어 모델(MLM)** : 입력 시퀀스 중 무작위 15% 토큰을 가리고 주변 좌우 양방향 문맥만을 참조하여 원래 단어를 맞히는 빈칸 채우기 학습.
- **다음 문장 예측(NSP)** : 두 개의 문장이 원문에서 실제로 연속하여 이어지는 문장(IsNext)인지 무관한 문장(NotNext)인지 이진 분류하는 학습.
- **[CLS] 토큰** : 시퀀스 맨 앞에 위치하여 문장 전체의 집약된 분류 표현(Classification Embedding)을 담아내는 특수 토큰.
- **양방향 어텐션(Bidirectional Attention)** : 디코더의 인과적 마스킹(Causal Mask) 없이 이전 토큰과 이후 토큰을 동시에 자유롭게 참조하는 완전 어텐션.

</details>

---

## 2~4교시 예상문제 (25점)

> 자연어 처리(NLP) 혁신의 분기점이 된 BERT(Bidirectional Encoder Representations from Transformers)의 개념 및 아키텍처를 설명하고, 사전학습 메커니즘(MLM, NSP), 생성형 디코더 모델(GPT)과의 비교 및 하위 태스크 미세조정 방안을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. BERT의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **BERT** 는 트랜스포머(Transformer)의 인코더 블록을 기반으로 하여, 입력 문장의 좌우 양방향(Bidirectional) 문맥을 동시에 참조하여 사전학습(Pre-training)하는 언어 이해(NLU) 특화 딥러닝 모델 |
| 목적 | 단방향 언어 모델의 문맥 단절 한계 극복, 마스크 언어 모델(MLM)과 다음 문장 예측(NSP)을 통한 범용 언어 표현 학습 및 분류·개체명 인식·검색 등 다운스트림 태스크 성능 극대화 |

## Ⅱ. BERT의 핵심 특징

| 구분 | 주요 특징 | 기술적 설명 및 메커니즘 |
|---|---|---|
| **양방향 인코딩** | 진정한 양방향 (Deep Bidirectional) | 왼쪽에서 오른쪽으로만 읽는 단방향 한계를 넘어, 모든 레이어에서 좌우 문맥 토큰을 동시 참조 |
| **사전학습 목표** | MLM과 NSP의 듀얼 목표 | 문맥 단어 맞히기(MLM)와 문장 간 논리적 인과성 판별(NSP)을 비지도 학습으로 동시 수행 |
| **입력 표현 구조** | 3중 임베딩 (Triple Embedding) | Token Embedding(WordPiece) + Segment Embedding(문장 구분) + Position Embedding(위치) 가산 |
| **전이학습 패러다임**| Pre-train & Fine-tune | 대규모 말뭉치로 사전학습된 단일 가중치 위에 단일 출력 레이어만 추가하여 다양한 NLP 과업 즉시 해결 |

## Ⅲ. BERT 아키텍처 및 사전학습 체계

```text
┌────────────────────────────────────────────────────────────────────────┐
│             [ BERT 양방향 인코더 아키텍처 및 사전학습 파이프라인 ]           │
└────────────────────────────────────────────────────────────────────────┘
 [ 입력 토큰열 ]: [CLS] 사과 [MASK] 맛있는 과일 [SEP] 배도 달다 [SEP]
        │
        ▼ (3중 임베딩 합산: Token + Segment + Position)
 [ E_CLS, E_사과, E_MASK, E_맛있는, E_과일, E_SEP, E_배도, E_달다, E_SEP ]
        │
        ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ [ 다층 양방향 트랜스포머 인코더 블록 (Bidirectional Transformer × L층) ] │
 │   - 모든 토큰이 서로를 완전히 참조하는 Self-Attention 연산 수행         │
 └────────────────────────────────────┬───────────────────────────────────┘
                                      │
         ┌────────────────────────────┴───────────────────────────┐
         ▼ (CLS 토큰 출력 벡터 T_CLS)                              ▼ (MASK 토큰 출력 벡터 T_MASK)
 [ Task 1: 다음 문장 예측 (NSP) ]                         [ Task 2: 마스크 언어 모델 (MLM) ]
   ├── IsNext vs NotNext 이진 분류                          └── 소프트맥스 통과 후 원래 단어
   └── 문장 간 논리적 연속성 학습                             ('는' 토큰 확률 복원: Cross-Entropy)
```

| 구성 요소 | 세부 처리 메커니즘 | 공학적 의미 |
|---|---|---|
| **Token Embeddings** | WordPiece 분절 (30,000 Vocab) | OOV(Out-Of-Vocabulary) 미등록 단어 문제 완벽 해결 |
| **Segment Embeddings** | 문장 A는 0, 문장 B는 1 부여 | 질문-답변(QA)이나 문장 쌍 분류 시 두 문장의 경계 구분 |
| **Position Embeddings** | 학습 가능한 위치 벡터 가산 (최대 512) | 어텐션의 집합 연산 특성에 단어 순서 정보 부여 |
| **MLM 80-10-10 룰** | 15% 대상: 80% [MASK], 10% 랜덤, 10% 원본 | 미세조정 시 [MASK] 부재로 인한 불일치 오차 완화 |

## Ⅳ. 인코더 기반 BERT, 디코더 기반 GPT, 인코더-디코더 T5 비교

| 비교 항목 | BERT (Encoder Only) | GPT (Decoder Only) | T5 (Encoder-Decoder) |
|---|---|---|---|
| **기본 아키텍처** | 양방향 트랜스포머 인코더 | 단방향 자기회귀 디코더 | 인코더-디코더 풀 트랜스포머 |
| **어텐션 메커니즘** | 양방향 어텐션 (양쪽 참조) | 인과적 마스크 어텐션 (과거만 참조) | 인코더(양방향) + 디코더(단방향) |
| **사전학습 목표** | 마스크 언어 모델 (MLM) | 다음 토큰 예측 (Causal LM) | 텍스트 대 텍스트 변환 (Span Denoising) |
| **최적화 과업** | 텍스트 분류, 개체명 인식, 검색 | 대화형 생성, 창의적 글쓰기, 코드 생성 | 번역, 요약, 문맥 변환 |
| **자유 텍스트 생성**| 불가능 (빈칸 채우기만 가능) | 최고 수준의 자유 형식 생성 | 우수한 조건부 생성 |
| **대표 모델** | RoBERTa, ALBERT, ELECTRA | GPT-4, Llama-3, Mistral | T5, BART |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 사전학습 단계에는 빈번하게 등장하는 [MASK] 토큰이 실제 하위 미세조정(Fine-Tuning) 데이터에는 전혀 존재하지 않아 모델 표현력 왜곡 발생 | 마스킹 토큰 대신 생성자가 바꾼 가짜 토큰을 감별하는 판별자(Discriminator) 방식의 ELECTRA 구조 도입 및 RoBERTa의 동적 마스킹(Dynamic Masking) 채택 |
| 이전 시점의 단어를 기반으로 다음 단어를 순차 출력하는 자기회귀 디코더가 결여되어 자유 형식의 장문 텍스트 생성 태스크 수행 원천 불가 | 문서 요약, 대화 생성 등의 과업에는 GPT/Llama 계열의 디코더 모델을 사용하고, BERT는 텍스트 분류 및 검색 리랭커 전담 백본으로 역할 분리 |
| 최대 시퀀스 길이가 512 토큰으로 고정되어 긴 문서 전체를 한 번에 인코딩할 때 문맥이 잘려나가는 트렁케이션(Truncation) 발생 | 윈도우 기반 로컬 어텐션을 적용하여 수만 토큰까지 수용 가능한 Longformer 또는 BigBird 인코더 변형 모델 도입 |

## Ⅵ. 제언

텍스트 이해·의도 분류 및 검색 리랭킹에는 경량화된 RoBERTa/ELECTRA를, 최종 자연어 답변 생성에는 디코더 기반 LLM을 배치하는 NLU-NLG 협력 파이프라인 구축.

```text
[ 사용자 비정형 입력 질의 ]
             │
             ▼
[ 1단계: NLU 인코더 계층 (RoBERTa / ELECTRA) ]
   ├── Intent Classification (질의 의도 정밀 분류)
   ├── Named Entity Recognition (핵심 엔티티 추출)
   └── Dense Retrieval Reranker (검색된 지식 문서 재순위화)
             │
             ▼ (분류된 의도 및 고정밀 검색 문서 전달)
[ 2단계: NLG 디코더 계층 (Llama-3 / GPT-4) ]
   ├── 초장문 문맥 추론 및 자연스러운 문장 생성
   └── 최종 사용자 맞춤형 답변 출력
```

| 구분 | 디코더 단일 모델 올인원 방식 | 제언: BERT(NLU) + LLM(NLG) 분업 |
|---|---|---|
| **의도 분류 지연** | LLM 생성 호출로 수백 ms 지연 | BERT 인코더 경량 추론으로 10ms 이내 완료 |
| **검색 리랭킹 비용** | 토큰당 과금으로 높은 API 비용 | 사내 BERT 리랭커로 무비용 초고속 처리 |
| **시스템 신뢰도** | 프롬프트 기반 분류 시 환각 위험 | 소프트맥스 정량 확률 기반 완벽한 제어 |

## 출제 이력과 검증 출처

- 제123회 정보관리기술사 1교시: BERT의 개념, 특징 및 사전학습 기법
- Jacob Devlin et al. (Google AI Language), BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- Yinhan Liu et al., RoBERTa: A Robustly Optimized BERT Pretraining Approach
- Kevin Clark et al., ELECTRA: Pre-training Text Encoders as Discriminators Rather Than Generators

## 연결 토픽

- 상위 토픽: [054 트랜스포머](./054_transformer.md)
- 연관 토픽: [078 TF-IDF](./078_tf_idf.md), [085 임베딩](./085_embedding.md), [071 초거대 AI](./071_hyperscale_ai.md)
