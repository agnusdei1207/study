---
title: "SW 안전성 분석(FTA·FMEA·HAZOP) (SW: Software; FTA: Fault Tree Analysis; FMEA: Failure Mode and Effects Analysis; HAZOP: Hazard and Operability Study)"
author: "Antigravity"
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

## Ⅰ. SW 안전성 분석의 개요

- 개념 : 소프트웨어가 탑재된 임베디드, 자율주행, 철도, 의료기기, 원자력 등 **안전 필수** (Safety-Critical) 시스템에서 소프트웨어 결함이나 예외 상황이 인명 피해나 막대한 재산 손실을 초래하지 않도록 잠재적 위험 요소를 식별, 분석, 통제하는 공학적 분석 체계.
- 배경 및 필요성 : 단순한 기능 테스트만으로는 복합 시스템 환경의 예기치 않은 **위험** (Hazard)을 예방할 수 없으므로, 시스템 수준의 위험도 분석 및 **기능안전** (ISO(International Organization for Standardization) 26262, IEC(International Electrotechnical Commission) 61508) 표준 준수 필수.
- 대표적 3대 기법 : **하향식 결함수 분석** (FTA, Fault Tree Analysis), **상향식 고장모드 영향분석** (FMEA, Failure Mode and Effects Analysis), **공정 가이드워드 기반 위험성 분석** (HAZOP, Hazard and Operability Study).

## Ⅱ. 3대 안전성 분석 기법의 메커니즘

```text
[ FTA: 하향식(Deductive) ]     [ FMEA: 상향식(Inductive) ]      [ HAZOP: 가이드워드 기반 ]
       [ Top Event: 화재 ]           [ 부품/단위 모듈 고장 ]          [ 프로세스 파라미터 (유량) ]
              │                               │                               │
         ┌────┴────┐                          ▼                               ▼
      [AND]      [OR]                 [ 시스템 영향 분석 ]            [ 가이드워드 결합 (MORE) ]
     ┌──┴──┐    ┌──┴──┐                       │                               │
     A     B    C     D                       ▼                               ▼
    (원인 결함 조합 탐색)            [ 위험우선순위(RPN, Risk Priority Number) 산출 ]       [ 이탈(Deviation) 원인/대책 ]
```

- **FTA (Fault Tree Analysis)** : 시스템의 최상위 사고(Top Event)에서 시작하여 **불 대수** (Boolean Logic: AND/OR 게이트)를 통해 **기본 사상** (Basic Event)과 최소 **컷셋** (Minimal Cut Set)을 도출하는 하향식 연역 분석.
- **FMEA (Failure Mode and Effects Analysis)** : 개별 부품이나 소프트웨어 단위 모듈의 고장 모드를 나열하고, **심각도** (S), **발생빈도** (O), **검출난이도** (D)의 곱으로 **위험우선순위** (RPN = S x O x D)를 계산하는 상향식 귀납 분석.
- **HAZOP (Hazard and Operability Study)** : 프로세스 변수(온도, 압력, 데이터 유입량 등)에 **가이드워드** (No, More, Less, As Well As, Reverse 등)를 결합하여 설계 의도에서 벗어난 **이탈** (Deviation)을 분석.

## Ⅲ. FTA, FMEA, HAZOP의 비교 분석

| 비교 항목 | FTA (결함수 분석) | FMEA (고장모드 영향분석) | HAZOP (위험성평가) |
|---|---|---|---|
| 분석 접근법 | 하향식 (Top-Down, 연역적) | 상향식 (Bottom-Up, 귀납적) | 브레인스토밍 기반 가이드워드 접근 |
| 분석 시작점 | 최상위 재앙적 사고 (Top Event) | 하위 단위 구성요소/모듈의 고장 | 정상 공정/프로세스의 파라미터 |
| 위험 정량화 | 컷셋(Cut Set), 고장 확률 계산 | 위험우선순위(RPN = S x O x D) | **위험 매트릭스** (심각도/빈도 등급) |
| 주요 장점 | 복합 결함(다중 원인 조합) 분석 탁월 | 단일 고장 모드의 체계적 전수 검사 | 예상치 못한 운용 편차 및 이상 징후 발굴 |
| 주요 한계 | 대규모 시스템 시 결함수 트리 거대화 | 복합 결함(다중 장애) 분석 한계 | 참여 전문가 역량 및 시간에 의존 |

## Ⅳ. SW 안전성 분석의 주요 한계점 및 해결 방안

- 복잡 분산 시스템에서의 정적 분석 기법 적용 한계 :
  - 한계점 : 수백만 라인의 코드와 분산 통신 환경에서 하드웨어 중심의 고전적 기법(FTA, FMEA)만으로는 컴포넌트 간 상호작용 오류나 타이밍 이슈에 기인한 위험원 식별 불가.
  - 해결 방안 : 시스템 이론 기반 사고 모델링(STAMP/STPA)을 도입하여 제어 루프 상의 안전 제약 조건 위반을 분석하고, 모델 기반 시스템 엔지니어링(MBSE) 도구와 연계한 위험원 분석 자동화.
- 소프트웨어의 체계적 결함(Systematic Fault) 특성과 고장률 추정 한계 :
  - 한계점 : 소프트웨어 결함은 부품 마모가 아닌 설계/구현 오류에 기인하므로, 하드웨어식 확률적 고장률($\lambda$) 기반 안전도 산출 공식이 성립하지 않음.
  - 해결 방안 : 정량적 고장률 계산 대신 기능안전 표준(ISO 26262, IEC 61508)의 ASIL(Automotive Safety Integrity Level)/SIL(Safety Integrity Level) 등급별 안전 무결성 프로세스(정적 분석, MC/DC 검증, 정형 기법) 준수 및 방어적 아키텍처(Fault-Tolerant, Fail-Safe) 설계.
- 분석 결과의 사후 문서화 및 개발 생명주기와의 단절 :
  - 한계점 : 안전성 분석이 개발 초기 아키텍처 설계와 실시간 연동되지 않고, 프로젝트 종료 시점에 인증 획득을 위한 사후 끼워맞추기식 요식 행위로 전락.
  - 해결 방안 : 요구사항 관리 도구(Jira/Polarion)를 활용하여 위험원(Hazard)-안전 요구사항(Safety Requirements)-아키텍처 설계-테스트 케이스 간 추적성 매트릭스(Traceability Matrix)를 실시간 동기화.

## Ⅴ. 고신뢰성 SW 시스템 구축을 위한 기술사적 제언

- STPA(시스템 이론 프로세스 분석)로의 확장 적용 : 구성요소의 단일 고장뿐만 아니라 구성요소 간 상호작용의 불일치 및 제어 루프 결함으로 발생하는 현대 복잡 시스템의 안전성 분석을 위해 STAMP 기반의 STPA 기법 병행 도입 권장.
- 안전 무결성 기준(SIL / ASIL)과의 엄격한 연계 : 식별된 위험도에 따라 요구되는 안전 등급(ASIL A~D, SIL 1~4)을 확정하고, 이에 상응하는 아키텍처 이중화(Fail-Safe, Fault-Tolerant) 및 MC/DC 테스트 강제화 필요.
