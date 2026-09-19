---
title: "Transformer"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:43:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "기출 · 81%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "137회"
  priority: 81
  priority_note: "[출제:137]"
---

## 답안 골격
```text
[Transformer] ◀━━ 머리: Ⅶ 내 의견 (선형 어텐션(FlashAttention)과 MoE를 결합한 초장문맥 실시간 추론 최적화)
 ┃
 ┣━ Ⅰ 개요 ───── 순차 처리 순환신경망(RNN)의 기울기 소실·병렬화 불가 한계 → 어텐션만으로 시퀀스를 병렬 처리하는 혁신 신경망
 ┣━ Ⅱ 특징 ───── 완전 병렬 처리(No Recurrence) · 셀프 어텐션(Self-Attention) · 장거리 의존성 해결 · 스케일링 법칙 성립
 ┣━ Ⅲ 구조 ───── 인코더-디코더 + 멀티헤드 어텐션(MHA) + 위치 인코딩(Positional Encoding) + FFN + 잔차 연결/LayerNorm
 ┣━ Ⅳ 흐름 ───── ① 입력 토큰 임베딩 + 위치 정보 합성 → ② Q, K, V 선형 투영 → ③ 스케일드 닷 프로덕트 어텐션 → ④ FFN 거쳐 출력
 ┣━ Ⅴ 비교 ───── RNN vs LSTM vs Transformer (순차 처리/장거리 소실 vs 게이트 제어 vs 전역 병렬 셀프 어텐션)
 ┗━ Ⅵ 실무 ───── 시퀀스 길이 제곱에 비례하는 연산 복잡도($O(N^2)$) / 긴 문맥 처리 시 GPU 메모리(KV Cache) 폭증
```
- 필수 키워드: 트랜스포머(Transformer) · 셀프 어텐션(Self-Attention) · 멀티헤드 어텐션(MHA) · 스케일드 닷 프로덕트 · 쿼리/키/값(Q, K, V) · 플래시어텐션(FlashAttention)
- 배점 전략: 10점 = Ⅰ 개요 → Ⅲ 인코더-디코더 블록 구조도 → Ⅳ 스케일드 닷 프로덕트 어텐션 수식 / 25점 = Ⅰ~Ⅶ 전개, Attention Is All You Need 메커니즘과 $O(N^2)$ 메모리 병목 해소 기술 집중
- 기출: 137회 1교시 7번 `트랜스포머(Transformer)와 MoE(Mixture of Experts)를 설명하시오.` → Ⅰ~Ⅴ

## 한 줄 본질
- 단어를 하나씩 순서대로 읽어야만 해서 GPU 병렬 학습이 불가능했던 순환신경망(RNN)의 치명적 병목 → 문장 내 모든 단어 간의 상호 연관도를 한 번에 행렬 연산으로 계산하는 셀프 어텐션 메커니즘 구축 → 현대 거대 언어모델(LLM)의 대규모 병렬 사전학습 가능 / 시퀀스 길이에 비례해 연산량과 메모리가 2차 곡선($O(N^2)$)으로 폭증

## 핵심 그림
```text
[트랜스포머 셀프 어텐션(Self-Attention) 및 멀티헤드 연산 흐름]
                [ 입력 토큰 임베딩 + Positional Encoding ]
                                     |
              +----------------------+----------------------+
              |                      |                      |
              v (선형 투영 W_Q)       v (선형 투영 W_K)       v (선형 투영 W_V)
          [ Query (Q) ]          [ Key (K) ]            [ Value (V) ]
              |                      |                      |
              +----------+-----------+                      |
                         v                                  |
          [ Q * K^T (유사도 행렬 내적) ]                    |
                         v                                  |
          [ 스케일링: / sqrt(d_k) ]                          |
                         v                                  |
          [ Softmax (어텐션 가중치 확률 분포) ]              |
                         |                                  |
                         +-----------------+----------------+
                                           v
                        [ 가중 합산: Attention(Q,K,V) = Softmax(...) * V ]
                                           |
                                           v
                        [ 멀티헤드 결합 (Concat) 및 선형 변환 W_O ]
```

## 핵심 용어
- 스케일드 닷 프로덕트 어텐션: $\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$ 수식으로, 쿼리와 키의 내적 값을 차원의 제곱근으로 나누어 기울기 소실을 방지하고 밸류와 가중 합산하는 연산
- 멀티헤드 어텐션(MHA): 어텐션을 단일 채널로 계산하지 않고 $h$개의 독립된 헤드로 나누어 병렬 수행함으로써 문법적 관계, 의미적 관계 등 서로 다른 위치의 다양한 특징을 동시에 포착
- 위치 인코딩(Positional Encoding / RoPE): 트랜스포머가 단어를 한 번에 병렬 처리하기 때문에 잃어버리는 순서 정보를 삼각함수(Sin/Cos)나 회전 위치 임베딩(RoPE)을 통해 주입하는 기법

## 핵심 통찰
- 트랜스포머의 위대함은 인간의 뇌 구조 모사에서 온 것이 아니라, "GPU 하드웨어의 대규모 행렬 곱셈 가속기(Tensor Core)에 가장 완벽하게 들어맞는 아키텍처"라는 공학적 최적화에서 비롯됨
- 어텐션 맵의 시간 및 공간 복잡도가 문맥 길이 $N$의 제곱($O(N^2)$)에 비례하므로, 긴 문맥 처리를 위해서는 GPU HBM과 SRAM 간의 I/O를 최적화하는 플래시어텐션(FlashAttention)이 필수적
- 현재의 GPT, LLaMA, Claude 등 모든 최신 생성형 AI는 오리지널 트랜스포머의 "디코더 온리(Decoder-only)" 변형 구조를 바탕으로 발전

## 이웃 토픽과 구분
- Transformer vs RNN: RNN은 시계열 스텝 $t$마다 은닉 상태(Hidden State)를 순차 갱신하므로 병렬화 불가 / Transformer는 시퀀스 전체를 단일 텐서 연산으로 한 번에 병렬 처리

## 문제·원인·대책
- 적용 상황: 수만 토큰의 긴 법률 문서를 트랜스포머 모델로 처리 중 GPU VRAM Out-of-Memory(OOM) 발생
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 시퀀스 길이가 8K를 넘어가면 VRAM 소모량이 기하급수적으로 폭증 | 어텐션 행렬($N \times N$) 적재에 따른 $O(N^2)$ 메모리 복잡도 | FlashAttention-2/3 적용 및 타일링(Tiling) 기반 SRAM 연산 | 메모리 점유율 $O(N)$ 선형 감소 및 속도 3배 향상 |
| 디코딩 추론 시 토큰 생성마다 이전 모든 KV 값을 재계산하여 지연 발생 | 자기회귀(Autoregressive) 생성 특성에 따른 중복 연산 | KV 캐싱(KV Cache) 및 PagedAttention(vLLM) 기법 적용 | 중복 연산 제거 및 메모리 단편화 해소 |
| 100K 이상의 초장문맥에서 모델이 앞부분 문맥을 망각(Lost in the Middle) | 정적 위치 인코딩의 문맥 외삽(Extrapolation) 한계 | RoPE(Rotary Position Embedding) 및 YaRN 문맥 확장 적용 | 128K~1M 초장문맥에서도 검색 정확도 유지 |

## 이렇게 출제된다
- 제137회 1교시 7번: "트랜스포머(Transformer)와 MoE(Mixture of Experts)를 설명하시오." → 요구 포인트: 트랜스포머 기본 구조(인코더-디코더, 셀프 어텐션) + MoE 희소 라우팅 결합 메커니즘

## 내 의견
- [FlashAttention과 GQA를 결합한 엔터프라이즈 트랜스포머 서빙 최적화] 기업 실무에서 최신 LLM을 온프레미스에 서빙할 때 가장 큰 장벽은 KV 캐시로 인한 VRAM 고갈임 → 나라면: 멀티헤드 어텐션(MHA) 대신 키와 밸류 헤드를 묶어 공유하는 그룹 쿼리 어텐션(GQA) 아키텍처 모델을 채택하고, 추론 엔진에 FlashAttention 커널을 강제 활성화하여 단일 GPU로 동시 처리 가능한 동시 접속자 수(Concurrent Batches)를 4배 이상 확장

## 찾아볼 것
- Attention Is All You Need 원문 논문(Vaswani et al.) 및 FlashAttention-2의 온라인 소프트맥스(Online Softmax) 타일링 기법
