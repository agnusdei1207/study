---
title: "STPA(System Theoretic Process Analysis)"
description: "부품의 물리적 고장이 없더라도 복잡한 컴포넌트 간 상호작용 및 소프트웨어 제어 오류로 인한 사고를 예방하는 시스템 이론 기반 위험 분석(STPA) 기법"
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
  sub_topic: "safety"
  order: 108
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어공학 → 소프트웨어 안전 및 품질 → 위험 분석 기법 → **STPA(System Theoretic Process Analysis)**

---

## 30초 인출

- 본질: **STPA(System-Theoretic Process Analysis)** 는 MIT의 낸시 레브슨(Nancy Leveson) 교수가 제안한 STAMP(사고 인과 모델) 이론에 기반하여, 개별 구성요소의 고장이 발생하지 않더라도 컴포넌트 간 비정상적 상호작용, 제어 루프의 타이밍 결함, 불완전한 소프트웨어 제어 동작(UCA)으로 인해 발생하는 시스템 사고를 식별하는 차세대 위험 분석 기법
- 메커니즘: 분석 목적(손실/위험원) 정의 → 계층적 제어 구조(Control Structure) 모델링 → 4대 불안전 제어행위(UCA) 식별 → 손실 시나리오(Loss Scenario) 작성 및 시스템 안전 제약(Safety Constraint) 도출
- 통찰: FTA, FMEA와 같은 전통적 신뢰성 분석 기법은 부품의 '물리적 고장(Failure)'에만 치중하여 소프트웨어의 비고장성 논리/제어 상호작용 결함을 간과하므로 자율주행, 스마트 철도 등 복합 시스템에서는 STPA 기반의 제어 피드백 루프 검증이 필수적임

<details>
<summary>핵심 용어</summary>

- **STAMP (System-Theoretic Accident Model and Processes)** : 안전을 부품의 신뢰성 문제가 아닌 '동적 제어 및 제약조건의 시행 문제'로 파악하는 시스템 이론적 사고 모델
- **불안전 제어행위 (UCA: Unsafe Control Action)** : 특정 맥락(Context) 하에서 시스템을 위험원(Hazard) 상태로 전이시키는 부적절한 제어 명령
- **제어 구조 (Control Structure)** : 제어기(Controller), 제어 동작(Control Action), 제어 대상(Controlled Process), 피드백(Feedback)으로 구성된 순환 다이어그램
- **정신적 모델 / 공정 모델 (Process Model)** : 제어기가 제어 대상을 올바르게 지휘하기 위해 머릿속(메모리)에 가지고 있는 현재 상태에 대한 믿음(Belief)
- **손실 시나리오 (Loss Scenario)** : 왜 UCA가 발생했는지, 그리고 제어 명령이 올바르게 내려졌음에도 왜 안전 제어가 실패했는지를 설명하는 인과 체인

</details>

---

## 2~4교시 예상문제 (25점)

> 안전-치명적(Safety-Critical) 소프트웨어 복합 시스템의 위험 분석을 위한 STPA(System Theoretic Process Analysis)의 개념과 도입 배경을 설명하고, 전통적 위험 분석(FTA/FMEA)과의 비교, STPA 4단계 분석 절차 및 4대 UCA(Unsafe Control Action) 유형을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 복잡한 소프트웨어 및 인간-기계 상호작용 시스템에서 구성요소의 단일 고장이 없어도 제어 명령의 결함이나 피드백 지연으로 발생하는 사고를 방지하기 위한 제어 이론 기반 위험 분석 기법 |
| 목적 | 소프트웨어 논리 결함, 통신 지연, 제어기 공정 모델 불일치로 인한 시스템 손실 선제 예방 및 아키텍처 안전 제약조건(Safety Constraints) 도출 |

## Ⅱ. 핵심 특징

하드웨어 신뢰성(Reliability)과 시스템 안전성(Safety)을 엄격히 구분하여 분석.

| 핵심 영역 | STPA 분석 관점 | 공학적 기대 효과 |
|---|---|---|
| **비고장 위험 분석 (Non-failure Hazards)** | 모든 부품이 규격대로 정상 작동해도 상호작용 오류로 사고 발생 가능 | 소프트웨어 제어 결함 및 타이밍 오류 선제 도출 |
| **제어 루프 기반 (Control Loop)** | 제어기 $\rightarrow$ 제어 동작 $\rightarrow$ 액추에이터 $\rightarrow$ 센서 $\rightarrow$ 피드백의 피드백 제어 관점 | 제어기 내부 공정 모델과 실제 상태 간 괴리 탐지 |
| **맥락 중심 UCA 도출** | "명령어 자체"가 아니라 "명령어가 인가된 상황(Context)"을 함께 분석 | 고속 주행 중 역추진 등 상황 의존적 위험 통제 |
| **안전 제약의 선순환** | 분석 결과를 추상적 위험 목록이 아닌 구체적 엔지니어링 제약조건으로 변환 | 소프트웨어 요구사항 명세서(SRS)에 직접 반영 |

## Ⅲ. 체계·프로세스

STPA 4단계 분석 프로세스 및 계층적 제어 구조(Control Structure).

```text
[STPA 계층적 제어 구조 및 피드백 제어 체계]
[1] 분석 목적 정의 (손실 L, 위험원 H) ──> [2] 제어 구조 모델링 ──> [3] UCA 식별 ──> [4] 손실 시나리오 도출

  ── [STPA 기본 피드백 제어 구조 모델] ───────────────────────────────────────────────────────────────────

  +───────────────────────────────────────────────────+
  | 제어기 (Controller : 인간 운전자 / 자율주행 SW)   |
  |                                                   |
  |  [ 제어 알고리즘 ]                                |
  |  [ 공정 모델 (Process Model : 제어 대상의 상태) ] |
  +─────────────────────────┬─────────────────────────+
                            │ 제어 명령 (Control Actions : 제동, 가속, 조향)
                            ▼
  +───────────────────────────────────────────────────+
  | 제어 대상 / 액추에이터 (Controlled Process)        |
  | (브레이크 모터, 차량 구동계, 밸브 등)             |
  +─────────────────────────┬─────────────────────────+
                            │ 상태 피드백 (Feedback : 차속, 장애물 거리 센서)
                            ▼
                 (제어기로 피드백 루프 연결)
```

- **STPA 4단계 실행 프로세스**:
  1. **분석 목적 정의** : 시스템 수준의 인명 손실(L-1), 물리적 충돌(H-1) 등 수용 불가한 사고와 위험원 정의.
  2. **제어 구조 모델링** : 제어기와 제어 대상 간의 제어 명령(Control Action) 및 피드백 신호의 계층적 흐름도 작성.
  3. **UCA (불안전 제어행위) 식별** : 각 제어 명령에 대해 4대 가이드워드를 결합하여 위험을 유발하는 맥락(Context) 분석.
  4. **손실 시나리오 작성 및 안전 제약 도출** : 왜 UCA가 발생했는지(센서 고장, 공정 모델 오류 등) 원인을 추적하고, 이를 방지하기 위한 소프트웨어 안전 요구사항 도출.

## Ⅳ. 종류·비교

#### 전통적 위험 분석(FTA/FMEA) vs STPA 상세 비교

| 비교 항목 | FTA (Fault Tree Analysis) | FMEA (Failure Mode & Effects) | STPA (System Theoretic Analysis) |
|---|---|---|---|
| **이론적 기반** | 신뢰성 공학 (사건 연쇄 모델) | 신뢰성 공학 (부품 고장 분석) | **시스템 이론 및 사이버네틱스 (STAMP)** |
| **주요 분석 대상**| 부품의 하드웨어적 물리 고장 | 개별 부품의 고장 모드 | **컴포넌트 간 상호작용 및 제어 오류** |
| **소프트웨어 적합성**| 낮음 (SW는 마모/고장나지 않음) | 낮음 (기능적 상호작용 표현 불가) | **매우 높음 (SW 논리 및 타이밍 결함 특화)** |
| **사고 관점** | 부품 고장의 인과적 조합 | 부품 단일 고장의 치명도 | **제어 피드백 루프의 제약조건 미달** |
| **분석 방향** | 톱다운(Top-down) 연역적 분석 | 바텀업(Bottom-up) 귀납적 분석 | **탑다운 계층적 제어 구조 분석** |

#### 4대 UCA(Unsafe Control Action) 유형 및 가이드워드

| UCA 유형 | 가이드워드 의미 | 자율주행 차량 예시 |
|---|---|---|
| **제어 미제공 (Not Providing)** | 위험을 방지하기 위해 필요한 제어를 내리지 않음 | 전방 장애물이 나타났으나 긴급 제동 명령을 내리지 않음 |
| **위험 제어 제공 (Providing Unsafely)** | 제어 명령을 제공하여 오히려 위험을 초래함 | 고속도로 주행 중 파킹(P) 기어 체결 명령을 제공함 |
| **시점/순서 오류 (Wrong Timing/Order)** | 너무 일찍, 너무 늦게, 혹은 잘못된 순서로 제어함 | 충돌 0.1초 직전에 너무 늦게 에어백 전개 명령을 내림 |
| **지속시간 오류 (Stopped too soon / Applied too long)** | 제어를 너무 일찍 중단하거나 너무 오래 유지함 | 교차로 통과가 끝나지 않았는데 조향 복귀를 너무 일찍 중단함 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 대규모 복합 시스템 모델링 시 수백 개 이상의 제어 루프와 수천 개의 UCA가 도출되어 분석 공수 급증 | 위험도 기반 스코핑(Scoping)을 수행하여 인명 피해와 직결된 핵심 안전-치명 제어 루프에 분석 집중 |
| 분석가의 주관적 도메인 지식에 의존하여 제어기 내부 공정 모델(Process Model) 누락 발생 | XSTAMPP 등 전용 STPA 정형 분석 소프트웨어를 활용하여 UCA 및 시나리오 자동 생성 지원 |
| 도출된 안전 제약조건(Safety Constraints)이 실제 소프트웨어 개발팀의 코드로 구현되지 못하고 방치 | 안전 제약조건을 고유 ID로 명문화하고 요구사항 추적표(RTM)에 등록하여 단위 테스트 케이스로 강제 바인딩 |

## Ⅵ. 제언

STPA는 자율주행, 도심항공교통(UAM), 원자력 등 고신뢰성 복합 시스템의 필수 위험 분석 도구이므로, ISO 26262/ISO 21448(SOTIF) 국제표준과 연계하여 소프트웨어 안전 라이프사이클의 전반부에 선제 적용할 필요가 있음.

```text
[시스템 아키텍처 수립] ──> [STPA 제어 구조 분석] ──> [UCA 및 안전제약 도출] ──> [SOTIF 기능안전 설계 반영]
  (센서-제어기-액추에이터)      (피드백 타이밍/상호작용)      (소프트웨어 SRS 변환)         (Fail-Operational 구현)
```

| 관리 영역 | 권장 실천 지침 | 핵심 관리 지표 |
|---|---|---|
| **국제 표준 연계** | ISO 21448(SOTIF, 의도된 기능의 안전성) 분석 도구로 STPA 채택 | 성능 한계 및 환경 인지 결함 선제 제거율 90% |
| **요구사항 통합** | STPA 안전 제약을 시큐어 코딩 및 가드 로직 코드로 직접 변환 | 제어 피드백 오류로 인한 시스템 아웃라이어 제로 달성 |
| **검증 자동화** | 도출된 손실 시나리오를 HIL(Hardware-in-the-Loop) 결함 주입 테스트 케이스로 변환 | ASIL-D 기능안전 시험 적합 판정 획득 |

## 출제 이력과 검증 출처

- 제130회 정보관리기술사 4교시: 시스템 이론 기반 사고 모델(STAMP)과 위험 분석 기법인 STPA의 절차 및 UCA
- 제120회 정보관리기술사 1교시: STPA(System Theoretic Process Analysis)의 4대 불안전 제어행위(UCA)
- Nancy G. Leveson, Engineering a Safer World: Systems Thinking Applied to Safety (MIT Press)
- John Thomas, Nancy Leveson, STPA Handbook (MIT PSAS)
- ISO 21448:2022 Road vehicles - Safety of the intended functionality (SOTIF)

## 연결 토픽

- [SW 안전성 분석](./028_sw_safety_analysis.md)
- [SW안전 확보 지침](./097_sw_safety_guidelines.md)
- [기능 안전](./188_functional_safety.md)
- [임베디드 SW 테스트](./089_embedded_sw_test.md)
- [요구사항 추적표](./102_requirement_traceability_matrix.md)
