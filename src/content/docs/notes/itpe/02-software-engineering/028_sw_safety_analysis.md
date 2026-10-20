---
title: "SW 안전성 분석(FTA·FMEA·HAZOP) (SW: Software; FTA: Fault Tree Analysis; FMEA: Failure Mode and Effects Analysis; HAZOP: Hazard and Operability Study)"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- SW 안전성 분석, Safety-Critical, 기능안전(Functional Safety), ISO 26262, IEC 61508
- FTA(Fault Tree Analysis), FMEA(Failure Mode and Effects Analysis), HAZOP(Hazard and Operability Study), RPN, STPA, STAMP, SIL, ASIL, MC/DC

## Ⅰ. SW 안전성 분석의 개요

- 핵심 요약 : 안전 필수 시스템에서 소프트웨어 결함 기인 위험을 식별·분석·통제하는 FTA·FMEA·HAZOP 3대 분석 체계.
- 개념 : SW(Software)가 탑재된 임베디드, 자율주행, 철도, 의료기기, 원자력 등 안전 필수(Safety-Critical) 시스템에서 소프트웨어 결함이나 예외 상황이 인명 피해나 막대한 재산 손실을 초래하지 않도록 잠재적 위험 요소를 식별·분석·통제하는 공학적 분석 체계.
- 배경 및 필요성 : 단순한 기능 테스트만으로는 복합 시스템 환경의 예기치 않은 위험(Hazard)을 예방할 수 없으므로, 시스템 수준의 위험도 분석 및 기능안전 표준(ISO(International Organization for Standardization) 26262, IEC(International Electrotechnical Commission) 61508) 준수 필요.
- 주요 목적 : 위험원의 조기 식별과 안전 요구사항 도출, FTA·FMEA·HAZOP 3대 기법의 체계적 적용, 안전 무결성 등급 입증.

## Ⅱ. SW 안전성 분석의 특징

- 핵심 요약 : 하향식 FTA, 상향식 FMEA, 가이드워드 기반 HAZOP의 상호 보완적 3대 기법 체계.

1. FTA(Fault Tree Analysis) : 최상위 사고(Top Event)에서 시작하여 불 대수(Boolean Logic, AND/OR 게이트)를 통해 기본 사상(Basic Event)과 최소 컷셋(Minimal Cut Set)을 도출하는 하향식 연역 분석.
2. FMEA(Failure Mode and Effects Analysis) : 개별 부품이나 소프트웨어 단위 모듈의 고장 모드를 나열하고, 심각도(S), 발생빈도(O), 검출난이도(D)의 곱으로 위험우선순위(RPN, Risk Priority Number)를 계산하는 상향식 귀납 분석.
3. HAZOP(Hazard and Operability Study) : 프로세스 변수(온도, 압력, 데이터 유입량)에 가이드워드(No, More, Less, As Well As, Reverse)를 결합하여 설계 의도에서 벗어난 이탈(Deviation)을 분석하는 기법.
4. 기능안전 표준 연계 : ISO 26262, IEC 61508의 안전 무결성 등급별 프로세스 요구사항과 연동.

## Ⅲ. SW 안전성 분석의 구조 (흐름)

- 핵심 요약 : FTA는 하향식 결함수 전개, FMEA는 상향식 영향 분석, HAZOP는 파라미터와 가이드워드 결합 이탈 분석의 구조.
- 3대 기법의 분석 메커니즘.

```text
[ 3대 안전성 분석 기법의 메커니즘 ]
[ FTA: 하향식(Deductive) ]
   Top Event -> AND/OR 게이트 조합
      -> 기본 사상 -> 최소 컷셋 도출
[ FMEA: 상향식(Inductive) ]
   부품/모듈 고장 -> 시스템 영향 분석
      -> 위험우선순위(RPN) 산출
[ HAZOP: 가이드워드 기반 ]
   파라미터(유량) x 가이드워드(MORE)
      -> 이탈(Deviation) 원인/대책 도출
```

- FTA 결함수의 계층적 전개 구조.

```text
[ FTA 결함수 구조 ]
        [ Top Event : 최상위 사고 ]
                   │
              < OR 게이트 >
              /           \
[ 기본 사상 : 센서 오류 ]   [ 기본 사상 : SW 예외 미처리 ]
              └── 최소 컷셋(Minimal Cut Set) 도출 ──┘
```

## Ⅳ. FTA·FMEA·HAZOP의 비교

- 핵심 요약 : 분석 접근법(하향식·상향식·가이드워드)과 시작점, 위험 정량화 방식의 차이.

| 비교 항목 | FTA (결함수 분석) | FMEA (고장모드 영향분석) | HAZOP (위험성평가) |
|---|---|---|---|
| 분석 접근법 | 하향식 (Top-Down, 연역적) | 상향식 (Bottom-Up, 귀납적) | 브레인스토밍 기반 가이드워드 접근 |
| 분석 시작점 | 최상위 재앙적 사고 (Top Event) | 하위 단위 구성요소/모듈의 고장 | 정상 공정/프로세스의 파라미터 |
| 위험 정량화 | 컷셋(Cut Set), 고장 확률 계산 | 위험우선순위(RPN = S x O x D) | 위험 매트릭스 (심각도/빈도 등급) |
| 주요 장점 | 복합 결함(다중 원인 조합) 분석 탁월 | 단일 고장 모드의 체계적 전수 검사 | 예상치 못한 운용 편차 및 이상 징후 발굴 |
| 주요 한계 | 대규모 시스템 시 결함수 트리 거대화 | 복합 결함(다중 장애) 분석 한계 | 참여 전문가 역량 및 시간에 의존 |

## Ⅴ. SW 안전성 분석의 장점과 한계

- 핵심 요약 : 체계적 위험 정량화의 장점과 복잡 분산 시스템·소프트웨어 고유 특성 반영의 한계.
- 장점
  1. FTA의 복합 결함(다중 원인 조합) 분석력.
  2. FMEA의 단일 고장 모드 체계적 전수 검사.
  3. HAZOP의 예상치 못한 운용 편차·이상 징후 발굴.
- 한계점 1 : 복잡 분산 시스템에서의 정적 분석 기법 적용 한계
  - 한계점 : 수백만 라인의 코드와 분산 통신 환경에서 하드웨어 중심의 고전적 기법(FTA, FMEA)만으로는 컴포넌트 간 상호작용 오류나 타이밍 이슈에 기인한 위험원 식별 불가.
  - 해결 방안 : 시스템 이론 기반 사고 모델링(STAMP, System-Theoretic Accident Model and Processes)과 STPA(System-Theoretic Process Analysis)를 도입하여 제어 루프 상의 안전 제약 조건 위반을 분석하고, 모델 기반 시스템 엔지니어링(MBSE, Model-Based Systems Engineering) 도구와 연계한 위험원 분석 자동화.
- 한계점 2 : 소프트웨어의 체계적 결함(Systematic Fault) 특성과 고장률 추정 한계
  - 한계점 : 소프트웨어 결함은 부품 마모가 아닌 설계/구현 오류에 기인하므로, 하드웨어식 확률적 고장률($\lambda$) 기반 안전도 산출 공식의 성립 불가.
  - 해결 방안 : 정량적 고장률 계산 대신 기능안전 표준(ISO 26262, IEC 61508)의 ASIL(Automotive Safety Integrity Level)/SIL(Safety Integrity Level) 등급별 안전 무결성 프로세스(정적 분석, MC/DC(Modified Condition/Decision Coverage) 검증, 정형 기법) 준수 및 방어적 아키텍처(Fault-Tolerant, Fail-Safe) 설계.
- 한계점 3 : 분석 결과의 사후 문서화 및 개발 생명주기와의 단절
  - 한계점 : 안전성 분석이 개발 초기 아키텍처 설계와 실시간 연동되지 않고, 프로젝트 종료 시점에 인증 획득을 위한 사후 끼워맞추기식 요식 행위로 전락.
  - 해결 방안 : 요구사항 관리 도구(Jira/Polarion)를 활용하여 위험원(Hazard)-안전 요구사항(Safety Requirements)-아키텍처 설계-테스트 케이스 간 추적성 매트릭스(Traceability Matrix)의 실시간 동기화.

## Ⅵ. 고신뢰성 SW 시스템 구축을 위한 기술사적 제언

- 핵심 요약 : STPA 확장, 안전 무결성 등급 연계, 추적성 실시간 관리의 3대 제언.
- STPA 기법으로의 확장 적용 : 구성요소의 단일 고장뿐만 아니라 구성요소 간 상호작용의 불일치 및 제어 루프 결함으로 발생하는 현대 복잡 시스템의 안전성 분석을 위해 STAMP 기반의 STPA 기법 병행 도입 권장.
- 안전 무결성 기준(SIL/ASIL)과의 엄격한 연계 : 식별된 위험도에 따라 요구되는 안전 등급(ASIL A~D, SIL 1~4)을 확정하고, 이에 상응하는 아키텍처 이중화(Fail-Safe, Fault-Tolerant) 및 MC/DC 테스트 강제화 필요.
- 위험원-안전 요구사항 추적성의 실시간 관리 : 추적성 매트릭스 자동 동기화를 통해 분석 결과의 개발 생명주기 상시 반영 필요.

## Ⅶ. 결론

- 핵심 요약 : SW 안전성 분석은 3대 기법과 STPA의 보완적 적용으로 기능안전 표준 준수를 담보하는 체계.
- 요약 : FTA·FMEA·HAZOP의 상호 보완적 적용과 STPA 확장을 통해 복잡 시스템의 위험원을 체계적으로 통제하는 체계.
- 시사점 : 안전 무결성 등급 연계와 추적성 자동화를 통해 사후 요식 행위가 아닌 생명주기 상시의 안전 확보 필요.
