---
title: "RLHF(Reinforcement Learning from Human Feedback)"
author: "GPT-6"
date: "2026-09-24T00:00:00+09:00"
sidebar:
  order: 45
  label: "045. RLHF"
  badge:
    text: "서브"
    variant: note
tags:
  - "notes-latest-tech"
extra:
  model: "GPT-6"
  keyword_grade: "서브"
---

## 지식 로드맵 내 현재 위치

지식 위치: 대규모 언어모델 적응 → 사람 선호 반영 → **RLHF**

## 30초 인출

- 본질: **RLHF(Reinforcement Learning from Human Feedback)** 는 사람의 선호 피드백으로 언어 모델의 응답 정책을 조정하는 학습 접근
- 메커니즘: 시범 응답으로 SFT → 응답 비교·선호 라벨 → 보상 모델 학습 → 강화학습 정책 갱신·평가

<details>
<summary>핵심 용어</summary>

- **RLHF(Reinforcement Learning from Human Feedback)** : 사람의 선호 피드백을 강화학습 등으로 모델 정책에 반영하는 접근
- **지도 미세조정(Supervised Fine-Tuning, SFT)** : 시범 입력·응답으로 모델을 지도 학습하는 단계
- **선호 자료(Preference Data)** : 같은 입력의 여러 응답을 사람이 비교·순위화한 자료
- **보상 모델(Reward Model)** : 응답에 대한 선호 점수를 추정하도록 학습한 모델
- **근접 정책 최적화(Proximal Policy Optimization, PPO)** : 정책을 제한된 범위에서 갱신하는 강화학습 알고리즘
- **직접 선호 최적화(Direct Preference Optimization, DPO)** : 선호 응답쌍으로 정책을 직접 최적화하는 방법
</details>

---
## 1교시 예상문제 (10점)

> RLHF의 개념과 사람 선호를 반영하는 기본 학습 절차를 설명하시오. (예상·10점)

---
## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **RLHF(Reinforcement Learning from Human Feedback)** 는 사람의 선호 피드백으로 언어 모델의 응답 정책을 조정하는 학습 접근 |
| 목적 | 사람의 선호·지시를 모델의 응답 행동에 반영 |

### Ⅱ. 일반적 학습 흐름

```text
기반 언어 모델
      ↓ 시범 응답 학습
초기 정책(SFT)
      ↓ 후보 응답 생성·비교
사람 선호 라벨
      ↓ 보상 모델 학습
선호 점수 추정
      ↓ PPO 등 정책 최적화
조정된 정책·평가
```

### Ⅲ. 주요 구성

| 구성 | 기능 |
|---|---|
| SFT 정책 | 초기 응답 행동 제공 |
| 선호 자료·보상 모델 | 사람 비교 판단을 점수 신호로 반영 |
| 정책 최적화 | 보상에 맞춰 응답 분포 조정 |

제언: 선호 라벨의 기준·대표성을 점검하고 독립 평가·안전 시험을 병행.

---
## 2~4교시 예상문제 (25점)

> RLHF의 개념과 주요 학습 단계·최적화 방식을 설명하고, 선호 자료·보상·안전성의 평가 방안을 제시하시오. (예상·25점)

---
## 2~4교시 25점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **RLHF(Reinforcement Learning from Human Feedback)** 는 사람의 선호 피드백으로 언어 모델의 응답 정책을 조정하는 학습 접근 |
| 목적 | 사람의 선호·지시를 모델의 응답 행동에 반영 |

### Ⅱ. 일반적 학습 흐름

```text
기반 언어 모델
      ↓ 시범 응답 학습
초기 정책(SFT)
      ↓ 후보 응답 생성·비교
사람 선호 라벨
      ↓ 보상 모델 학습
선호 점수 추정
      ↓ PPO 등 정책 최적화
조정된 정책·평가
```

### Ⅲ. 정책 최적화 방식

| 방식 | 선호 반영 방법 | 구별점 |
|---|---|---|
| 보상 모델+PPO | 보상 모델 점수를 이용해 정책 갱신 | 보상 모델·정책 학습을 분리하는 대표 구성 |
| DPO | 선호 응답쌍으로 정책을 직접 최적화 | 별도 보상 모델·PPO 루프가 필수는 아님 |

### Ⅳ. 품질·위험 평가

| 한계 | 평가·대응 |
|---|---|
| 평가자·지침의 편향이 선호 자료에 반영될 수 있음 | 평가 지침·표본의 대표성과 라벨 일치도 확인 |
| 보상 모델 점수를 과도하게 최적화할 수 있음 | 별도 과업 평가·사람 검토·보상 해킹 시험 |
| 학습 후에도 유해 출력·공격 취약성이 남을 수 있음 | 안전·강건성 시험과 운영 모니터링 |

### Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 선호 기반 추가 학습이 실제 업무 개선보다 비용·복잡성을 키울 수 있음 | SFT 기준선을 먼저 세우고 남은 개선 요구·평가 기준이 확인된 과업에만 선호 최적화를 적용 |

---
## 출제 이력과 검증 출처

- 제139회 2교시 1번: AI 리스크 중 LLM 모델 정렬·안전성 확보 기술
- Ouyang et al., [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155): SFT·선호 자료·보상 모델·PPO 구성 확인
- Rafailov et al., [Direct Preference Optimization](https://arxiv.org/abs/2305.18290): 선호 자료를 이용한 직접 정책 최적화 확인
