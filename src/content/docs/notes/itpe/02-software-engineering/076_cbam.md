---
title: "CBAM(Cost Benefit Analysis Method)"
description: "소프트웨어 아키텍처 대안 간의 비용, 비즈니스 편익, ROI를 정량적으로 평가하여 최적의 기술 전략 우선순위를 도출하는 경제성 평가 모델"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
    variant: "note"
extra:
  series: "itpe"
  topic: "02-software-engineering"
  sub_topic: "architecture"
  order: 76
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어공학 → 소프트웨어 아키텍처 및 구현 → 아키텍처 평가 → **CBAM(Cost Benefit Analysis Method)**

---

## 30초 인출

- 본질: **CBAM(Cost Benefit Analysis Method)** 은 카네기멜론대 SEI에서 제안한 아키텍처 평가 기법으로, ATAM 분석 결과를 기반으로 아키텍처 전략별 투입 비용과 품질 속성 향상에 따른 비즈니스 편익(ROI)을 정량화하여 최적의 투자 우선순위를 도출하는 경제성 평가 모델
- 메커니즘: 품질 시나리오 가중치 부여 → 전략별 유틸리티 변화량($\Delta U$) 계측 → 총 편익($b_i$) 산출 → 구현 비용($C_i$) 추정 → 투자수익률($ROI_i = b_i / C_i$) 순위 결정
- 통찰: 주관적인 효용 곡선 산정 및 단기 구축 비용 중심의 평가로 인해 총소유비용(TCO) 왜곡이 발생할 수 있으므로 민감도 분석과 클라우드 FinOps 연계 라이프사이클 비용 모델을 통합 구축해야 객관적인 의사결정 타당성을 확보할 수 있음

<details>
<summary>핵심 용어</summary>

- **ATAM(Architecture Tradeoff Analysis Method)** : 아키텍처 품질 속성 간의 기술적 상충 관계와 위험 요소를 식별하는 선행 분석 기법
- **유틸리티 함수(Utility Function)** : 시스템 품질 응답 수준(응답 시간, 가용성 등)에 대한 이해관계자의 주관적 만족도를 0~100 수치로 정량화한 효용 곡선
- **아키텍처 전략(Architectural Strategy)** : 품질 시나리오를 달성하기 위해 적용되는 설계 전술, 패턴, 아키텍처 대안
- **편익(Benefit)** : 아키텍처 전략 적용 시 얻게 되는 품질 향상에 비즈니스 중요도 가중치를 곱하여 합산한 총 효용 증분
- **ROI(Return on Investment)** : 아키텍처 전략 도입에 따른 총 편익을 투입 비용으로 나눈 투자 대비 경제성 지표

</details>

---

## 2~4교시 예상문제 (25점)

> 소프트웨어 아키텍처 대안의 경제적 타당성을 평가하는 CBAM(Cost Benefit Analysis Method)의 개념과 평가 프로세스를 설명하고, ATAM과의 연계 구조, 핵심 편익/비용 산정 수식 및 실무 적용 시의 한계 극복 방안을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | ATAM으로 도출된 아키텍처 전략들에 대해 투입 비용(Cost)과 기대 비즈니스 편익(Benefit)을 정량화하여 경제적 ROI 기반으로 우선순위를 결정하는 SEI 표준 아키텍처 평가 모델 |
| 목적 | 한정된 예산과 일정 제약 하에서 비즈니스 가치를 극대화하는 아키텍처 전략 선별 및 엔지니어링 의사결정의 객관적 근거 확보 |

## Ⅱ. 핵심 특징

기술적 타당성 중심의 아키텍처 분석을 경제학적 투자 가치 분석으로 확장하여 경영진과 엔지니어링 간 의사소통 지원.

| 특징 | 핵심 내용 | 비즈니스 및 엔지니어링 의미 |
|---|---|---|
| **ATAM 후속 연계성** | ATAM 6단계에서 식별된 품질 시나리오와 아키텍처 전략을 입력물로 직접 활용 | 기술적 트레이드오프 분석을 재무적 ROI 평가로 자연스럽게 전환 |
| **정량적 효용 모델링** | 최악(Worst), 현재(Current), 기대(Desired), 최고(Best) 수준의 유틸리티 곡선화 | 추상적 품질 요구를 0~100 사이의 명확한 수치 효용으로 변환 |
| **ROI 기반 우선순위화** | 총 편익과 투입 비용의 비율을 계산하여 예산 제약 하 최대 효과 전략 선정 | 기술적 우수성뿐만 아니라 비용 효율성(Cost-effectiveness) 입증 |
| **불확실성 관리** | 가중치, 비용 추정 오차에 대한 민감도 분석(Sensitivity Analysis) 병행 | 환경 변화에 따른 투자 위험 완화 및 의사결정 신뢰성 향상 |

## Ⅲ. 체계·프로세스

CBAM의 경제성 평가 흐름도 및 단계별 실행 체계.

```text
+---------------------------------------------------------------------------------------------------------+
|                                    CBAM 9단계 아키텍처 평가 체계 프레임워크                             |
+---------------------------------------------------------------------------------------------------------+
                                                                                                           
  [ATAM 결과물 인계] ──> (1) 시나리오 정리 (Collate Scenarios)                                            
                                  │                                                                        
                                  ▼                                                                        
                         (2) 시나리오 정제 (Refine Scenarios: 자극-환경-응답 구체화)                       
                                  │                                                                        
                                  ▼                                                                        
                         (3) 시나리오 우선순위화 (Prioritize Scenarios: 비즈니스 가중치 W_j 부여)          
                                  │                                                                        
                                  ▼                                                                        
                         (4) 유틸리티 부여 (Assign Utility: 최악, 현재, 기대, 최고 점수 매핑)              
                                  │                                                                        
                                  ▼                                                                        
                         (5) 아키텍처 전략 및 반응 수준 도출 (Develop Architectural Strategies)           
                                  │                                                                        
                                  ▼                                                                        
                         (6) 기대 효용 보간 (Determine Derived Utility: U_ij 도출)                         
                                  │                                                                        
                                  ▼                                                                        
                         (7) 총 편익 계산 (Calculate Total Benefit: b_i = Σ W_j * ΔU_ij)                   
                                  │                                                                        
                                  ▼                                                                        
                         (8) 전략별 비용 추정 (Estimate Cost: C_i 도출)                                    
                                  │                                                                        
                                  ▼                                                                        
                         (9) ROI 산출 및 최종 전략 선택 (Calculate ROI = b_i / C_i, 의사결정)              
```

- **핵심 정량 산출 수식 및 평가 메커니즘**:
  1. **전략 $S_i$의 시나리오 $j$에 대한 유틸리티 증분 ($\Delta U_{ij}$)** :
     $$\Delta U_{ij} = U_{ij} - U_{current, j}$$
     (전략 적용 후 도달하는 기대 유틸리티에서 현재 유틸리티를 차감)
  2. **전략 $S_i$의 총 편익 ($b_i$)** :
     $$b_i = \sum_{j} \left( W_j \times \Delta U_{ij} \right)$$
     ($W_j$: 시나리오 $j$의 상대적 비즈니스 중요도 가중치)
  3. **전략 $S_i$의 투자수익률 ($ROI_i$)** :
     $$ROI_i = \frac{b_i}{C_i}$$
     ($C_i$: 전략 $S_i$를 구현하고 운영하는 데 소요되는 총비용)

## Ⅳ. 종류·비교

#### SEI 3대 아키텍처 평가 방법론(SAAM vs ATAM vs CBAM) 비교

| 비교 항목 | SAAM (Software Architecture Analysis Method) | ATAM (Architecture Tradeoff Analysis Method) | CBAM (Cost Benefit Analysis Method) |
|---|---|---|---|
| **분석 초점** | 아키텍처 변경 용이성 및 기능 실체화 | 품질 속성 간 상호작용 및 기술적 트레이드오프 | 아키텍처 전략별 경제성, 비용 대비 편익(ROI) |
| **평가 대상** | 컴포넌트 구조의 모듈성 및 변경 영향도 | 민감점, 절충점, 리스크, 비리스크 | 비즈니스 편익($b_i$), 개발/운영 비용($C_i$), ROI |
| **입력 자료** | 기능 요구사항 및 변경 시나리오 | 비즈니스 동인, 품질 속성 유틸리티 트리 | ATAM 결과 시나리오, 아키텍처 전략 후보군 |
| **주요 역할** | 단일 아키텍처의 설계 검증 | 상충하는 품질 간 최적의 기술 타협점 발견 | 예산 제약 내에서 실행할 최종 전략 투자 결정 |
| **평가 관점** | 엔지니어링 관점 | 엔지니어링 및 시스템 아키텍트 관점 | 엔지니어링 및 경영/재무 의사결정권자 관점 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 이해관계자의 주관적 성향에 따라 유틸리티 곡선과 시나리오 가중치($W_j$) 왜곡 발생 | 델파이(Delphi) 기법 및 AHP(쌍대비교법)를 결합하여 다자간 합의 기반 가중치 객관화 |
| 초기 개발 비용($C_i$)만 산정하여 클라우드 운영비, 기술부채 등 라이프사이클 총소유비용(TCO) 누락 | FinOps 체계 및 3~5개년 운영 TCO 추정 모델을 결합하여 비용 산정 범위 전주기화 |
| 시장 환경 및 비즈니스 우선순위 급변 시 기존 CBAM 산출 결과의 유효성 상실 | 분기별 애자일 아키텍처 리뷰 회차를 두고 민감도 분석(Sensitivity Analysis)을 주기적 재수행 |

## Ⅵ. 제언

CBAM 평가를 일회성 프로젝트로 끝내지 않고 ATAM 기술 검증과 FinOps 비용 거버넌스를 결합한 전사 아키텍처 투자 의사결정 파이프라인으로 체계화할 필요가 있음.

```text
[ATAM 기술 리스크 분석] ──> [CBAM 경제성 ROI 평가] ──> [FinOps TCO 실시간 검증] ──> [애자일 백로그 반영]
 (품질 상충/전략 도출)         (편익/비용 매트릭스 확정)       (클라우드 실측 비용 추적)       (우선순위 스프린트 실행)
```

| 관리 영역 | 실행 지침 | 목표 산출물 |
|---|---|---|
| **평가 연계** | ATAM 리스크 분석 직후 동일 이해관계자 참여 하에 CBAM 착수 | ATAM-CBAM 연계 아키텍처 평가 보고서 |
| **비용 거버넌스** | 개발 공수(FP/COCOMO)와 클라우드 인프라 예측 비용 동시 반영 | 3개년 아키텍처 TCO 시뮬레이션 표 |
| **우선순위 실행** | ROI 순위와 기술적 선행 의존성을 매핑하여 애자일 백로그 편성 | 분기별 아키텍처 로드맵 및 실행 백로그 |

---

## 출제 이력

- 제125회 정보관리기술사 1교시: CBAM(Cost Benefit Analysis Method)의 개념 및 절차
- 제114회 컴퓨터시스템응용기술사 2교시: 소프트웨어 아키텍처 평가 기법인 ATAM과 CBAM의 비교 및 경제성 분석
- 제101회 정보관리기술사 4교시: 아키텍처 재설계 시 비용 편익 분석을 위한 CBAM 방법론

## 참고 자료

- Rick Kazman, Jai Asundi, Mark Klein, "Making Architecture: The CBAM Steps and ROI Calculation" (SEI Technical Report)
- Len Bass, Paul Clements, Rick Kazman, "Software Architecture in Practice (4th Edition)"
- Carnegie Mellon University SEI, Architecture Tradeoff and Cost-Benefit Analysis Method Series

## 연결 토픽

- [소프트웨어 아키텍처](./056_software_architecture.md)
- [아키텍처 스타일](./057_architecture_style.md)
- [소프트웨어 비용 산정](./027_sw_cost_estimation.md)
- [ATAM](./014_atam.md)
