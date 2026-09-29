---
title: "DeepSeek-R1 (강화학습 기반 추론)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "031. DeepSeek-R1"
  order: 31
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>최신 기술</span><span>추론 특화 LLM</span><strong>DeepSeek-R1</strong></div>

## 30초 인출

- 본질: **DeepSeek-R1** 은 대규모 지도학습(SFT) 데이터 없이도 대규모 강화학습(RL)만으로 모델 스스로 장문 생각의 사슬(Long CoT), 자체 반성(Self-reflection), 오류 정정 능력을 자발적으로 발현(Emergence)시킨 오픈소스 추론 특화 LLM
- 메커니즘: 별도의 가치 신경망(Critic) 없이 동일 프롬프트의 그룹 출력 간 상대적 보상을 계산하는 GRPO 알고리즘을 적용하고, 콜드스타트 SFT와 거부 샘플링을 결합한 다단계 파이프라인 수행
- 통찰: 순수 강화학습(R1-Zero) 시 언어 혼용(Language Mixing)과 가독성 저하가 발생하므로 소량의 양질 콜드스타트 데이터 주입 및 소형 모델로의 지식 증류(Distillation) 결합 필수

<details><summary>핵심 용어</summary>

- **DeepSeek-R1** : 순수 강화학습(RL)과 그룹 상대 정책 최적화(GRPO)를 결합하여 OpenAI o1 수준의 수학·코딩 추론 능력을 달성한 오픈웨이트 모델.
- **DeepSeek-R1-Zero** : 지도 미세조정(SFT)을 완전히 배제하고 오직 강화학습 보상만으로 추론 및 사고 과정을 창발시킨 최초의 실험 모델.
- **GRPO (Group Relative Policy Optimization)** : 별도의 무거운 Critic 모델을 두지 않고 그룹 샘플링의 평균과 표준편차를 기준으로 어드밴티지(Advantage)를 정규화 계산하는 고효율 RL 알고리즘.
- **규칙 기반 보상 (Rule-based Reward)** : 보상 모델(RM)의 해킹 취약점을 방지하기 위해 컴파일러 실행 성공 여부나 수학 정답 일치 여부를 결정론적 코드로 검증하는 보상 체계.
- **아하 모먼트 (Aha Moment)** : 강화학습 도중 모델이 스스로 초기 풀이의 오류를 인지하고 "Wait, wait, let me rethink..."와 같이 재검토를 수행하는 자발적 추론 행동.

</details>

---

## 2~4교시 예상문제 (25점)

> 오픈소스 초거대 추론 모델인 'DeepSeek-R1'의 개념과 등장 배경을 설명하고, 기존 PPO 대비 GRPO 알고리즘의 최적화 메커니즘, 4단계 하이브리드 학습 파이프라인 및 지식 증류(Distillation) 기반 SLM 적용 방안을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. DeepSeek-R1의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **DeepSeek-R1** 은 대규모 인간 레이블링 SFT 데이터셋 없이, 그룹 상대 정책 최적화(GRPO) 기반의 대규모 강화학습을 통해 스스로 장문 Chain-of-Thought(CoT) 및 자가 검증 역량을 발현시킨 차세대 오픈소스 추론 전문 언어모델 |
| 목적 | 폐쇄형 상용 모델(OpenAI o1) 독점 타파, 고비용 인간 선호도 라벨링 의존 탈피, 수학·과학·코딩 복합 다단계 추론의 획기적 정확도 향상 |

## Ⅱ. DeepSeek-R1의 핵심 특징 및 기술적 혁신 속성

| 구분 | DeepSeek-R1의 핵심 특징 | 세부 공학적 메커니즘 및 속성 |
|---|---|---|
| **추론 능력의 자발적 창발** | Self-Evolutionary CoT | 사람의 풀이 예시를 주지 않아도 학습 스텝이 진행됨에 따라 문제 풀이 토큰 길이가 수천 자로 자율 확장 |
| **Critic 배제 메모리 절감** | GRPO 기반 50% 자원 절약 | PPO 필수 요소인 파라미터 크기의 Value Network를 제거하여 GPU VRAM 점유율 대폭 감축 |
| **규칙 기반 결정론적 보상** | 보상 해킹(Reward Hacking) 방지 | 정답이 명확한 수학/코드 문제에 컴파일러 및 파서 기반의 정확도 보상(Accuracy)과 포맷 보상(Format) 적용 |
| **지식 증류의 압도적 효율** | 1.5B ~ 70B 소형 모델로 전이 | 거대 R1 모델이 생성한 80만 건의 추론 궤적 데이터로 소형 모델을 증류하여 경량 모델 추론 SOTA 달성 |

## Ⅲ. DeepSeek-R1 학습 파이프라인 및 GRPO 최적화 아키텍처

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ DeepSeek-R1 4단계 완성 파이프라인 ]                  │
└────────────────────────────────────────────────────────────────────────┘
                                    │
 [ 1단계: 콜드스타트 SFT ] ──> 소량의 수천 건 고품질 가독성 Long-CoT 데이터 파인튜닝
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 2단계: 추론 지향 대규모 강화학습 (Reasoning-oriented RL) ]            │
│   ├── GRPO 알고리즘 적용: 동일 프롬프트에 대해 G=8개 응답 그룹 생성    │
│   ├── 규칙 기반 보상: 수학 정답(Accuracy Reward) + XML 태그(Format)   │
│   └── 어드밴티지 계산: A_i = (R_i - mean(R)) / std(R)                   │
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 3단계: 거부 샘플링 및 전 장르 SFT (Rejection Sampling SFT) ]          │
│   ├── 추론 데이터: 2단계 체크포인트에서 60만 건 정답 추론 궤적 샘플링   │
│   └── 일반 데이터: 글짓기, 번역, 사실 질문 등 20만 건 비추론 데이터 결합│
└────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 4단계: 전 장르 2차 강화학습 (RL for All Scenarios) ]                  │
│   - 추론 보상 + 인간 선호도(Helpfulness/Harmlessness) 정렬 최종 완성   │
└────────────────────────────────────────────────────────────────────────┘
```

| GRPO 연산 단계 | 수학적 메커니즘 | 공학적 효과 |
|---|---|---|
| **그룹 출력 생성** | $o_1, o_2, \dots, o_G \sim \pi_{\theta_{\text{old}}}(q)$ | 단일 질문 $q$에 대해 $G$개의 다채로운 답변 궤적 병렬 샘플링 |
| **상대적 보상 정규화** | $A_i = \frac{r_i - \text{mean}(\{r\})}{\text{std}(\{r\})}$ | 별도 Critic 모델 없이 그룹 내 편차만으로 보상 신호 표준화 |
| **클리핑 정책 업데이트** | $\text{clip}\left(\frac{\pi_\theta}{\pi_{\text{old}}}, 1-\epsilon, 1+\epsilon\right) A_i$ | 급격한 정책 붕괴를 방지하면서 이전 정책 주변에서 안전한 갱신 |
| **KL 발산 페널티** | $\mathbb{D}_{\text{KL}}(\pi_\theta \parallel \pi_{\text{ref}})$ | 기준 모델로부터 지나치게 멀어지는 언어 왜곡 방지 |

## Ⅳ. R1-Zero vs R1 vs 증류(Distilled) 모델 비교

| 비교 항목 | DeepSeek-R1-Zero | DeepSeek-R1 | Distilled Models (1.5B~70B) |
|---|---|---|---|
| **콜드스타트 SFT** | 완전 배제 (0건) | 수천 건의 고품질 가독성 SFT 적용 | R1이 생성한 80만 건 정제 데이터 |
| **학습 방식** | 순수 대규모 강화학습 (Pure RL) | 4단계 SFT + RL 하이브리드 | 순수 지도학습 미세조정 (SFT) |
| **언어 혼용 현상** | 한국어 질문에 영어/중국어로 생각 | 프롬프트 언어와 일치된 일관된 CoT | 일관된 언어로 매끄러운 추론 |
| **가독성 및 서식** | 생각의 사슬이 무질서하고 장황함 | `<think>` 태그 내 정돈된 단계적 사고 | 태스크에 최적화된 간결한 서식 |
| **하드웨어 요구량** | 671B MoE 클러스터 (초대형 인프라) | 671B MoE 클러스터 | 단일 GPU 또는 온디바이스 NPU 구동 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 정답이 명확하지 않은 창작, 법률 해석, 윤리적 딜레마 등 소프트 태스크에서의 보상 정의 곤란 | 정답 매칭 보상 대신 인간 선호도 기반 보상 모델(RM) 및 LLM-as-a-Judge 평가를 4단계에 결합 |
| 추론 과정에서 불필요하게 만 단위 토큰을 소모하여 추론 지연시간(Latency) 및 연산 비용 증가 | 생각의 사슬 길이(Token Length)에 대한 감점 페널티를 보상 함수에 주입하여 효율적 간결 추론 유도 |

## Ⅵ. 제언

수천억 파라미터의 거대 R1 모델을 직접 서비스하기보다, R1의 고품질 추론 궤적으로 도메인 특화 SLM을 증류(Distillation)하여 온프레미스에 배포하는 엔지니어링 전략 구축.

```text
[ DeepSeek-R1 (671B MoE) 교사 모델 ]
                 │
                 ▼
[ 80만 건 고난도 도메인 추론 궤적 데이터 추출 (<think>...</think>) ]
                 │
                 ▼
[ Qwen-2.5 / Llama-3 (7B~14B) 학생 모델 지도 미세조정 (Distillation) ]
                 │
                 ▼
[ 사내 온프레미스 단일 GPU 서빙 (vLLM 가속) 및 OpenAI o1-mini 수준 성능 달성 ]
```

| 구분 | 거대 R1 (671B) 직접 서빙 | 제언: R1 증류 모델 (8B/14B) 서빙 |
|---|---|---|
| **인프라 비용** | 수십억 원대 8-Way H100 노드 필요 | 1천만 원대 단일 GPU 서버에서 즉시 구동 |
| **추론 속도** | 대형 모델 파라미터 로딩으로 지연 발생 | 경량 파라미터로 첫 토큰(TTFT) 즉각 출력 |
| **도메인 특화** | 범용 추론에 특화되어 사내 규정 미숙 | 사내 도메인 데이터와 R1 추론 궤적 결합 파인튜닝 |

## 출제 이력과 검증 출처

- DeepSeek-AI: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning", arXiv 2025
- OpenAI: "Learning to Reason with LLMs (OpenAI o1 System Card)", 2024
- Schulman et al., "Proximal Policy Optimization Algorithms", 2017
- Shao et al., "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models", 2024 (GRPO 원형)

## 연결 토픽

- 상위 토픽: [009 생성형 AI](./009_generative_ai.md)
- 연관 토픽: [039 추론형 언어모델(LRM)](./039_reasoning_model_lrm.md), [023 강화학습](./023_reinforcement_learning.md), [034 sLM](./034_slm.md)
