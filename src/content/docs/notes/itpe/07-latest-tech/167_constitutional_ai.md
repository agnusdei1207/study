---
title: "Constitutional AI (RLAIF)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags: ["notes-latest-tech"]
sidebar:
  label: "167. Constitutional AI (RLAIF)"
  order: 167
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>인공지능·AI 윤리</span><span>초거대 언어모델 정렬(Alignment)</span><strong>Constitutional AI (RLAIF)</strong></div>

## 30초 인출

- 본질: **Constitutional AI** (RLAIF: Reinforcement Learning from AI Feedback)는 인간 라벨러의 수기 피드백 대신 명문화된 헌법(규범 원칙)을 바탕으로 AI가 스스로 응답을 비판·수정하고 선호도를 평가하여 모델을 자율 정렬하는 안전 기술
- 메커니즘: 1단계 지도학습(헌법 기반 비판-수정 반복 파인튜닝) → 2단계 강화학습(AI 평가자의 헌법 선호도 판정 기반 보상 모델 학습 및 PPO/DPO 최적화)
- 통찰: AI 선호 판정에 의존 시 원칙 간 우선순위 충돌로 무해한 질문까지 차단하는 과잉 거절(False Refusal)이 발생하므로 다층 헌법 스코어링 및 적응형 탈옥 방어 레드팀 자동화 체계 구축 필요

<details><summary>핵심 용어</summary>

- **Constitutional AI (CAI)** : 앤트로픽(Anthropic)이 제안한 기술로, 헌법(규범 규칙 목록)을 프롬프트로 주입하여 AI가 자체 피드백을 생성하는 정렬 프레임워크.
- **RLAIF (AI 피드백 강화학습)** : RLHF의 인간 피드백(Human Feedback)을 대형 언어 모델의 AI 피드백으로 대체한 기법.
- **비판 및 수정 (Critique & Revision)** : 초기 생성된 유해/미흡 응답을 헌법 규칙에 비추어 문제점을 스스로 지적하고 안전하게 다시 작성하는 과정.
- **과잉 거절 (Helpfulness vs Harmlessness)** : 안전성(무해성)을 지나치게 강조하여 위험하지 않은 일반적 질문조차 거절해 버리는 유용성 저하 현상.
- **DPO (Direct Preference Optimization)** : 별도의 복잡한 보상 모델 학습 없이 선호도 데이터셋에서 손실 함수로 정책 모델을 직접 미세조정하는 기법.

</details>

---

## 2~4교시 예상문제 (25점)

> 생성형 대규모 언어모델(LLM)의 안전성과 윤리성을 확보하기 위한 정렬(Alignment) 기법인 Constitutional AI(RLAIF)의 개념과 2단계 학습 파이프라인(지도학습, 강화학습)을 설명하고, 기존 RLHF와의 비교 및 과잉 거절(Over-refusal) 극복을 위한 공학적 방안을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. Constitutional AI의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 인간 라벨러의 방대한 수작업 평가 대신, 사전에 정의된 명문화된 규범(헌법 원칙)을 프롬프트로 제공하여 AI가 자기 비판(Critique)과 수정(Revision), 선호도 평가를 자동 수행하도록 하는 모델 정렬 기술 |
| 목적 | 인간 작업자의 트라우마(유해 콘텐츠 노출) 방지, 정렬 비용과 소요 시간의 획기적 절감, 명확하고 투명한 안전 가이드라인 거버넌스 확립 |

## Ⅱ. Constitutional AI의 헌법적 원칙 체계 및 특징

| 구분 | 세부 내용 | 주요 특징 및 효과 |
|---|---|---|
| **헌법 원칙 출처** | 세계인권선언, 플랫폼 안전 가이드라인, 딥마인드 SparQ 규범 등 | 인간 보편 가치를 반영한 자연어 규칙 목록 구성 |
| **비판-수정 (Critique)** | "이 응답이 특정 집단에 유해한지 비판하고 안전하게 수정하시오" | 모델 내부의 잠재 능력을 활용한 고품질 안전 교정 데이터 자체 생성 |
| **자율 선호 판정** | 모델이 생성한 두 후보 응답 중 헌법에 더 부합하는 응답 자동 선택 | 수만 건의 선호도 라벨을 수시간 내에 초고속 대량 구축 |
| **투명한 제어성** | 원칙 추가·삭제·수정만으로 모델의 안전 행동을 프로그래밍하듯 통제 | 블랙박스 인간 피드백 대비 규제 대응 및 감사 용이성 제공 |

## Ⅲ. Constitutional AI 2단계 파이프라인 프로세스

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ Constitutional AI 2단계 파이프라인: SL 정제 및 RLAIF 강화학습 ]      │
└────────────────────────────────────────────────────────────────────────┘

  [ 1단계: 지도학습 기반 비판 및 수정 (SL Phase: Critique & Revision) ]
   - 레드팀 유해 프롬프트 인입 ──> 초기 유해 응답 생성
                 │
                 ▼ (헌법 원칙 $C_i$ 주입: "유해성을 지적하고 개선하시오")
   - 자기 비판 (Critique) ──> 안전하게 정제된 수정 응답 (Revision) 생성
                 │
                 ▼ (수정된 <프롬프트, 수정 응답> 쌍 수집)
   - 지도학습 미세조정 (SL-CAI Model 구축)
                 │
                 ▼
  [ 2단계: AI 피드백 기반 강화학습 (RL Phase: RLAIF) ]
   - 프롬프트에 대해 SL-CAI 모델이 두 개의 응답 ($y_1, y_2$) 생성
                 │
                 ▼ (피드백 모델에 헌법 원칙 제시: "어느 응답이 더 원칙을 준수하는가?")
   - AI 피드백 선호도 라벨링 ($y_1 \succ y_2$)
                 │
                 ▼
   - AI 선호도 데이터셋 기반 보상 모델(RM) 학습 (또는 DPO 적용)
                 │
                 ▼
   - PPO 강화학습 알고리즘으로 최종 정책 모델 파라미터 최적화
                 │
                 ▼
  [ 무해하면서도 유용한(Harmless & Helpful) 최종 Claude 모델 완성 ]
```

| 파이프라인 단계 | 엔지니어링 세부 수행 내용 | 핵심 산출물 및 기법 |
|---|---|---|
| **레드팀 프롬프팅** | 유해 행위(해킹, 폭력, 혐오 등)를 유도하는 수만 건의 적대적 프롬프트 수집 | Red-Teaming 데이터셋 |
| **자기 수정 (SL)** | 체인 오브 소트(CoT) 방식으로 헌법 원칙을 대조하여 비판 후 재작성 | SFT용 안전 정제 데이터 |
| **선호도 생성 (RLAIF)**| AI 판별 모델이 헌법 텍스트를 참고하여 두 응답의 승/패 확률 산출 | 바이너리 선호도(Preference) 데이터 |
| **보상 함수 최적화** | 브래들리-테리(Bradley-Terry) 확률 모델을 바탕으로 보상 점수 수렴 | AI 피드백 기반 보상 모델(RM) |
| **정책 강화학습** | KL 페널티를 적용하여 원래 언어 능력 유지와 함께 보상 극대화 | PPO(Proximal Policy Optimization) |

## Ⅳ. RLHF vs Constitutional AI (RLAIF) vs DPO 비교

| 비교 항목 | RLHF (인간 피드백 강화학습) | Constitutional AI (RLAIF) | DPO (직접 선호 최적화) |
|---|---|---|---|
| **선호 평가 주체** | 크라우드소싱 인간 라벨러 | 헌법 프롬프트를 수신한 AI 모델 | 인간 또는 AI 선호 데이터셋 |
| **구축 비용 및 시간**| 막대한 비용(수십억 원), 수개월 소요 | 매우 저렴, 수일 이내 완료 | 별도 RM이 없어 연산 비용 50% 절감 |
| **일관성 및 투명성**| 평가자마다 주관적 편차 및 모순 큼 | 헌법 텍스트 기반 일관된 잣대 적용 | 선호 데이터 품질에 전적 의존 |
| **인간 윤리 문제** | 작업자의 정신적 트라우마 심각 | 완전 자동화로 인간 심리 피해 없음 | 데이터 수집 방식에 따라 상이 |
| **알고리즘 구조** | SFT $\rightarrow$ RM 학습 $\rightarrow$ PPO 정책 학습 | SL Critique $\rightarrow$ RM 학습 $\rightarrow$ PPO | 선호 데이터로 폐루프 없이 직접 Loss 최소화 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 무해성(Harmlessness)을 과도하게 추구하여 "칼로 사과 깎는 법" 등 일상적이고 무해한 질문까지 거절하는 과잉 거절(Over-refusal) 발생 | 헌법 원칙 내에 '유용성(Helpfulness)'과 '맥락 분별(Context Discrimination)'을 상위 원칙으로 명시하고 양성-음성 경계 데이터 미세조정 |
| AI 피드백 평가 모델 자체의 편향(Bias)이나 환각이 선호도 데이터에 그대로 전이되어 비정상적 보상 해킹(Reward Hacking) 유발 | 소량의 고품질 골드 표준셋을 인간 전문가가 직접 교차 검증하고 다수 평가 모델의 앙상블 투표(Ensemble Voting) 메커니즘 적용 |
| 복잡한 다단계 다국어 난독화 및 페르소나 탈옥(Jailbreak) 프롬프트에 헌법 필터링이 우회 무력화되는 보안 취약점 | 가상 레드팀 에이전트(Automated Red-Teaming)를 파이프라인에 결합하여 새로운 탈옥 수법을 자율 생성하고 헌법을 실시간 동적 갱신 |

## Ⅵ. 제언

안전성과 유용성의 황금비율을 달성하기 위해 헌법 원칙을 정적으로 고정하지 않고, '자동 레드팀 공격 + 헌법 동적 진화 + DPO 경량 정렬'이 유기적으로 결합된 지속적 정렬(Continuous Alignment) 아키텍처 구축 필요.

```text
[ 자율 적대적 공격 생성기 (Automated Red-Team Agent) ]
                 │
                 ▼ (취약점 및 탈옥 패턴 발견)
[ 헌법 동적 진화 엔진 (Evolving Constitution) ]
   ├── Step 1: 발견된 취약점에 대응하는 신규 안전 조항 자동 입안
   ├── Step 2: 인간 거버넌스 위원회의 원칙 승인 (승인 완료 즉시 반영)
   └── Step 3: 합성 선호도 데이터셋 즉시 생성
                 │
                 ▼
[ DPO (Direct Preference Optimization) 무중단 카나리 파인튜닝 ]
                 │
                 ▼
[ 유용성을 훼손하지 않는 지능형 제로데이 안전 모델 배포 ]
```

| 구분 | 정적 1회성 RLHF | 제언: 진화형 Constitutional DPO |
|---|---|---|
| **원칙 수정** | 원칙 변경 시 수만 건 인간 라벨링 재수행 | 헌법 텍스트 수정 후 수시간 내 자동 재학습 |
| **거절 정확도** | 획일적 거절로 사용자 불만 가중 | 맥락 기반 분별력 학습으로 정밀 안전 제어 |
| **파이프라인 복잡도**| 불안정한 PPO 강화학습 루프 튜닝 필요 | DPO 손실 함수 단독 직접 최적화로 안정화 |
| **신규 위협 대응** | 사후 사고 발생 후 수기 패치 | 자동 레드팀 기반 선제적 제로데이 방어 |

## 출제 이력과 검증 출처

- Yuntao Bai et al. (Anthropic), "Constitutional AI: Harmlessness from AI Feedback" (arXiv:2212.08073)
- Rafael Rafailov et al., "Direct Preference Optimization: Your Language Model is Secretly a Reward Model" (NeurIPS 2023)
- Paul F. Christiano et al., "Deep reinforcement learning from human preferences" (NeurIPS 2017)

## 연결 토픽

- 상위 토픽: [156 자연어 처리(NLP)](./156_nlp.md)
- 연관 토픽: [146 데이터 어노테이션](./146_data_annotation.md), [168 AI 학습용 데이터 구축 및 활용](./168_data_ai_training_utilization.md)
