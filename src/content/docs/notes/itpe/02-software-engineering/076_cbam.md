---
title: "CBAM(Cost Benefit Analysis Method)"
author: "Antigravity"
date: "2026-09-27T00:24:59+09:00"
tags:
  - "소프트웨어공학"
  - "아키텍처평가"
  - "CBAM"
  - "ATAM"
  - "ROI"
  - "FinOps"
sidebar:
  badge:
    text: "서브"
    variant: "note"
extra:
  model: "GPT-6"
  keyword_grade: "서브"
---


## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 소프트웨어 개발·운영 → CBAM(Cost Benefit Analysis Method)

> **로드맵 경로** : 소프트웨어공학 > 소프트웨어 아키텍처 및 구현 > 아키텍처 평가 > CBAM(Cost Benefit Analysis Method)

---

## 30초 인출

- 본질: **CBAM(Cost Benefit Analysis Method)** 은 아키텍처 대안의 비용·편익·불확실성을 비교해 투자 대안을 고르는 평가 방법
- 메커니즘: 품질 시나리오별 중요도와 유틸리티 변화로 편익을 추정 → 전략별 비용과 비교 → 예산 제약을 고려해 선택
- 통찰: 한계: 전략 편익만으로 투자 순서를 정하면 구현 비용과 불확실성을 놓침 → 방안: 시나리오별 효용 변화에 중요도를 반영하고 비용 가정과 함께 비교

<details>
<summary>핵심 용어</summary>

- **CBAM(Cost Benefit Analysis Method)** : 아키텍처 전략들의 투입 비용 대비 비즈니스 효용을 정량화하여 ROI 기준 최적 대안을 도출하는 SEI 평가 기법
- **SEI(Software Engineering Institute)** : CBAM 방법을 개발·발표한 카네기멜론대학교 소프트웨어공학 연구기관
- **ATAM(Architecture Tradeoff Analysis Method)** : 아키텍처 품질속성 간의 상호작용과 위험·절충점을 분석하는 방법
- **ROI(Return on Investment)** : 편익을 투자 비용과 비교해 투자 대안의 효율을 나타내는 비율
- **SAAM(Software Architecture Analysis Method)** : 시나리오를 이용해 소프트웨어 아키텍처의 변경 영향 등을 분석하는 방법
- **유틸리티 함수(Utility Function)** : 품질 속성 달성 수준(응답 시간, 가용성 등)에 대해 이해관계자가 느끼는 주관적 만족도를 0~100 점수로 환산한 값
- **품질 속성 시나리오(Quality Attribute Scenario)** : 자극(Stimulus), 환경, 응답, 응답 척도(Response Measure)로 구성된 아키텍처 요구사항 구체화 도구
- **FinOps(Cloud Financial Operations)** : 클라우드 인프라 아키텍처 변경에 따른 실시간 비용과 비즈니스 가치를 추적·최적화하는 재무 거버넌스

</details>

---

## 2~4교시 예상문제 (25점)

> 소프트웨어 아키텍처 대안의 비용과 편익을 평가하는 CBAM의 목적과 수행 절차를 설명하고, 전략별 경제성 비교 및 의사결정 시 유의점을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. CBAM의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | CBAM은 아키텍처 대안의 비용·편익·불확실성을 비교하는 경제성 평가 방법 |
| 목적 | 제한된 자원에서 구현할 아키텍처 전략의 선택 지원 |

## Ⅱ. CBAM의 특징

| 특징 | 평가에 필요한 판단 |
|---|---|
| 품질 시나리오의 효용 | 이해관계자 중요도와 현재·기대 응답 수준 |
| 전략별 경제성 | 효용 변화와 구현·운영 비용의 같은 단위 비교 |
| 불확실성 공개 | 가중치·반응·비용 가정에 따른 순위 변화 확인 |

## Ⅲ. CBAM 비용·편익 산정과 전략 선택 절차

**의사결정 프레임워크**

```text
품질 시나리오·중요도 가중치
    ↓
전략별 기대 효용 변화·편익 B 산정
    ↓
전략별 구현 비용 C 추정
    ↓
편익/비용 비율: B / C
    ↓ 예산·일정 제약
아키텍처 전략 우선순위 결정
```

**핵심 산출 수식**
1. **아키텍처 전략 $S_i$의 총 편익 ($b_i$)** :
   $$b_i = \sum_j \left( W_j \times (U_{ij} - U_{current, j}) \right)$$
   - $W_j$: 시나리오 $j$의 비즈니스 중요도 가중치.
   - $U_{ij} - U_{current, j}$: 전략 $S_i$ 적용 시 개선되는 유틸리티 증분 ($\Delta U$).
2. **편익/비용 비율과 순편익 기반 ROI의 구분** :
   $$\text{B/C}_i = \frac{b_i}{C_i},\qquad \text{ROI}_i = \frac{b_i-C_i}{C_i} \quad (C_i: \text{전략 } S_i \text{ 도입에 드는 총비용})$$
   CBAM 원문에서 ROI를 정의하는 방식과 일반 재무적 ROI의 비용 포함 범위가 다를 수 있으므로, 실제 비교에서는 편익·비용의 산정 단위와 분모를 명시.

**수행 단계**

| 단계 | 단계명 | 핵심 활동 및 주요 산출물 |
|---|---|---|
| 1 | 시나리오 수집 | 이해관계자에게 품질 시나리오 수집 |
| 2 | 시나리오 정제 | 측정 가능한 반응 수준과 상황 구체화 |
| 3 | 시나리오 우선순위화 | 중요 시나리오 선정 |
| 4 | 유틸리티 부여 | 현재·기대 수준에 대한 효용 평가 |
| 5 | 전략과 반응 수준 도출 | 각 아키텍처 전략이 시나리오에 미칠 반응 추정 |
| 6 | 기대 유틸리티 보간 | 유틸리티 반응 곡선에서 기대 수준의 효용 산정 |
| 7 | 총 편익 계산 | 시나리오별 가중 편익 합산 |
| 8 | ROI 기반 선택 | 비용과 예산 제약을 고려해 실행 전략 선택 |

## Ⅳ. SAAM·ATAM·CBAM의 비교

| 비교 항목 | SAAM | ATAM | CBAM |
|---|---|---|---|
| **평가 초점** | 변경 시나리오의 아키텍처 영향 | 품질속성 간 상호작용·위험 | 전략의 비용·편익·불확실성 |
| **주요 목적** | 아키텍처 수정용이성(Modifiability) 중심 평가 | 비기능 품질 속성 간의 **기술적 상충(트레이드오프) 분석** | 아키텍처 전략의 **경제적 비용-편익(ROI) 분석** |
| **분석 대상** | 변경 요구의 구조 영향 | 품질 요구 간 충돌·위험 | 전략별 비용 대비 편익 |
| **활용** | 변경 영향 이해 | 구조적 위험·절충점 분석 | 구현 전략의 경제성 비교 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 이해관계자의 주관적 효용 판단 | 가중치·효용 가정의 근거 기록과 민감도 비교 |
| 전략의 기대 반응 과대평가 | 측정 근거와 추정 범위를 함께 기록 |
| 개발·운영 비용 누락 | 기간별 비용 항목과 추정 불확실성 명시 |
| ROI만으로 위험·일정 간과 | 경제성 외 위험·일정 제약 병행 검토 |

## Ⅵ. 제언

투자 규모가 큰 전략부터 시나리오 효용·비용의 근거 범위를 공개하고 핵심 가정 변화에 따른 순위 민감도 확인.

## 출제 이력과 검증 출처

- [SEI, Using Economic Considerations to Choose Among Architecture Design Alternatives (CBAM)](https://insights.sei.cmu.edu/library/using-economic-considerations-to-choose-among-architecture-design-alternatives/)
- [SEI, Making Architecture: The CBAM Steps and ROI Calculation](https://www.sei.cmu.edu/documents/696/2002_005_001_14084.pdf)
---

## 연결 토픽

- [소프트웨어 아키텍처](./056_software_architecture.md) : 품질 속성을 달성하기 위한 기본 구조 설계
- [아키텍처 스타일](./057_architecture_style.md) : 패턴별 품질 속성 트레이드오프 분석
- [소프트웨어 개발비용 산정](./027_sw_cost_estimation.md) : CBAM의 투입 비용($C$)을 정량화하는 기능점수(FP) 및 COCOMO 모델
