---
title: "SW 안전성 분석(FTA·FMEA·HAZOP)"
description: "결함수·고장모드·위험운전성 분석, 기능안전 표준 연계, STPA 보완, 등급 기반 설계 제언"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드

- SW 안전성 분석, Safety-Critical, 기능안전(Functional Safety), ISO 26262, IEC 61508
- FTA(Fault Tree Analysis), FMEA(Failure Mode and Effects Analysis), HAZOP(Hazard and Operability Study), RPN, STPA, STAMP, SIL, ASIL, MC/DC

## Ⅰ. SW 안전성 분석의 개요

- 핵심 요약 : 안전 필수 시스템에서 소프트웨어 결함에 기인한 위험을 식별·분석·통제하는 3대 분석 체계(결함수 분석, 고장모드 영향 분석, 위험성 평가).
- 개념 : 소프트웨어(SW, Software)가 탑재된 임베디드, 자율주행, 철도, 의료기기 등 **안전 필수 시스템** (Safety-Critical System)에서 결함이나 예외 상황이 인명 피해나 재산 손실로 이어지지 않도록 잠재적 위험 요소를 식별·분석·통제하는 공학적 분석 체계.
- 배경 및 필요성 : 기능 테스트만으로는 복합 시스템 환경에서 예기치 않게 발생하는 위험(Hazard)을 예방하기 어려우므로, 시스템 수준의 위험도 분석과 **기능안전** (Functional Safety) 표준인 ISO(International Organization for Standardization) 26262, IEC(International Electrotechnical Commission) 61508의 준수가 필요함.
- 주요 목적 : 위험원의 조기 식별과 안전 요구사항 도출, 3대 기법의 체계적 적용, 안전 무결성 등급의 입증.

## Ⅱ. SW 안전성 분석의 특징 및 장점

- 핵심 요약 : 하향식 FTA, 상향식 FMEA, 가이드워드 기반 HAZOP이 상호 보완하며 기능안전 표준과 연동되는 구조.

1. **FTA** (Fault Tree Analysis, 결함수 분석) : 최상위 사고(Top Event)에서 시작해 AND·OR 게이트로 기본 사상과 최소 컷셋(Minimal Cut Set)을 도출하는 하향식 연역 분석 → 다중 원인이 얽힌 사고 경로를 드러냄.
2. **FMEA** (Failure Mode and Effects Analysis, 고장모드 영향 분석) : 부품이나 SW 모듈의 고장 모드를 나열해 심각도(S), 발생도(O), 검출도(D)의 곱인 위험우선순위(RPN, Risk Priority Number)를 계산하는 상향식 귀납 분석 → 단일 고장을 빠짐없이 점검.
3. **HAZOP** (Hazard and Operability Study, 위험 및 운전성 분석) : 온도·압력·데이터 유입량 같은 프로세스 변수에 No, More, Less, Reverse 등의 가이드워드를 결합해 설계 의도에서 벗어난 이탈(Deviation)을 분석 → 예상치 못한 운용 편차 발굴.
4. 기능안전 표준 연계 : ISO 26262와 IEC 61508의 안전 무결성 등급별 프로세스 요구사항과 연동 → 인증 근거의 일관성 확보.

## Ⅲ. SW 안전성 분석의 구조 (흐름)

- 핵심 요약 : FTA는 하향식 결함수 전개, FMEA는 상향식 영향 분석, HAZOP는 파라미터와 가이드워드를 결합한 이탈 분석의 구조.

```text
[ 3대 기법의 분석 방향 ]

FTA : 최상위 사고 → 기본 사상 (하향식)
   ↓
FMEA : 부품·모듈 고장 → 시스템 영향 (상향식)
   ↓
HAZOP : 파라미터 × 가이드워드 → 이탈 (가이드워드)
```

```text
[ FTA 결함수 구조 ]

최상위 사고 (Top Event)
   ↓
OR 게이트
   ▶ 기본 사상 : 센서 오류
   ▶ 기본 사상 : SW 예외 미처리
   ↓
최소 컷셋 (Minimal Cut Set) 도출
```

## Ⅳ. FTA·FMEA·HAZOP의 비교

- 핵심 요약 : 분석 접근법(하향식, 상향식, 가이드워드)과 시작점, 위험 정량화 방식이 기법마다 다르다.

| 비교 항목 | FTA (결함수 분석) | FMEA (고장모드 영향 분석) | HAZOP (위험 및 운전성 분석) |
| --- | --- | --- | --- |
| 분석 접근법 | 하향식 (Top-Down, 연역적) | 상향식 (Bottom-Up, 귀납적) | 전문가 토의 기반의 가이드워드 접근 |
| 분석 시작점 | 최상위 재해성 사고 (Top Event) | 하위 구성요소·모듈의 고장 | 정상 공정의 프로세스 파라미터 |
| 위험 정량화 | 컷셋 분석과 고장 확률 계산 | 위험우선순위(RPN = S×O×D) | 위험 매트릭스 (심각도·빈도 등급) |
| 주요 장점 | 복합 결함(다중 원인 조합) 분석에 강함 | 단일 고장 모드의 체계적 전수 점검 | 예상치 못한 운용 편차와 이상 징후 발굴 |
| 주요 한계 | 대규모 시스템에서 결함수 트리가 거대화 | 복합 결함(다중 장애) 분석에 한계 | 참여 전문가의 역량과 시간에 의존 |

## Ⅴ. SW 안전성 분석의 한계와 방안

- 핵심 요약 : 분산 시스템의 상호작용 위험, 소프트웨어 고유의 체계적 결함, 개발 생애주기와의 단절이라는 세 한계를 STPA 확장, 등급별 프로세스, 추적성 관리로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 복잡 분산 시스템에 대한 고전 기법 한계 | 수많은 코드와 분산 통신 환경에서 컴포넌트 간 상호작용 오류나 타이밍 이슈를 FTA·FMEA만으로 식별하기 어려움 | STAMP(System-Theoretic Accident Model and Processes) 기반의 STPA(System-Theoretic Process Analysis)로 제어 루프의 안전 제약 위반을 분석하고, MBSE(Model-Based Systems Engineering) 도구와 연계 | 제어 루프 분석 커버리지 |
| 소프트웨어의 체계적 결함 특성 | 결함이 부품 마모가 아닌 설계·구현 오류에서 비롯되어, 하드웨어식 고장률(λ) 기반 안전도 산출이 성립하지 않음 | 고장률 계산 대신 **안전 무결성 등급** (ASIL, Automotive Safety Integrity Level / SIL, Safety Integrity Level)별 프로세스를 준수하고, MC/DC(Modified Condition/Decision Coverage) 검증과 Fault-Tolerant·Fail-Safe 설계를 적용 | 등급별 프로세스 준수율 |
| 사후 문서화와 생애주기 단절 | 안전성 분석이 설계와 실시간으로 연동되지 않아 인증 직전의 요식 문서로 전락 | 요구사항 관리 도구로 위험원, 안전 요구사항, 아키텍처, 테스트 케이스 간 추적성 매트릭스를 동기화 | 추적 누락 건수 |

## Ⅵ. 고신뢰성 SW 시스템 구축을 위한 기술사적 제언

- 핵심 요약 : STPA의 병행 도입, 안전 무결성 등급과 설계의 연계, 분석의 생애주기 편입이라는 세 방향으로 안전성 분석을 상시 체계화.
- STPA의 병행 적용 : 구성요소의 단일 고장뿐 아니라 구성요소 간 상호작용의 불일치와 제어 루프 결함까지 다루기 위해, FTA·FMEA와 함께 STPA를 병행하는 것이 바람직하다.
- 등급 기반 설계 연계 : 위험도 평가 결과로 ASIL A~D 또는 SIL 1~4 등급을 확정하고, 그 등급에 맞춘 이중화 아키텍처와 MC/DC 검증을 의무화해야 한다.
- 안전 분석의 생애주기 편입 : 안전 분석을 인증 직전의 문서 작업이 아니라 아키텍처 설계 회의의 상시 의사결정 절차로 편입해 사후 끼워맞추기를 막는 거버넌스를 갖춰야 한다.

## Ⅶ. 결론

- 핵심 요약 : SW 안전성 분석은 3대 기법과 STPA의 보완적 적용으로 기능안전 표준 준수를 담보하는 체계.
- 시사점 : 안전 무결성 등급 연계와 분석의 생애주기 편입을 통해 인증 대응이 아닌 상시 안전 확보가 가능해짐.