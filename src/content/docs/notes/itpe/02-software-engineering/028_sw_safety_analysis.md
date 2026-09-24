---
title: "SW 안전성 분석(FTA·FMEA·HAZOP)"
tags:
  - "notes-software-engineering"
author: "Codex"
date: "2026-09-24T00:00:00+09:00"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-6"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어 공학 → 품질·안전·신뢰성 → **SW 안전성 분석(FTA·FMEA·HAZOP)**

## 30초 인출

- 본질: **SW 안전성 분석**은 자동차, 철도, 항공, 원자력 등 안전 필수(Safety-Critical) 시스템에서 소프트웨어 결함으로 인한 인명 피해나 물리적 재난을 예방하기 위해 위험원(Hazard)을 조기 식별·통제하는 공학 기법
- 메커니즘: 연역적 결함 분석(**FTA**) + 귀납적 고장 모드 분석(**FMEA**) + 가이드워드 공정 분석(**HAZOP**)
- 효과: 위험원 식별 · 위험도(Risk Matrix) 산출 · **안전 요구사항(Safety Requirements)** 도출 · 기능안전(ISO 26262/IEC 61508) 인증 획득

<details>
<summary>핵심 용어</summary>

- **Software Safety(소프트웨어 안전성)**: 소프트웨어가 의도된 기능을 수행하는 것뿐만 아니라, 시스템이 위험한 고장 상태로 전이되지 않도록 보장하는 특성
- **FTA(Fault Tree Analysis)**: 사고(Top Event)에서 출발하여 논리 게이트(AND/OR)를 통해 하위 기본 고장 원인을 규명하는 연역적(Top-down) 기법
- **FMEA(Failure Mode and Effects Analysis)**: 각 부품/모듈의 고장 모드가 상위 시스템에 미치는 영향을 평가하고 RPN을 산출하는 귀납적(Bottom-up) 기법
- **HAZOP(Hazard and Operability Study)**: 설계 의도에 가이드워드(No, More, Less, As well as 등)를 적용하여 비정상적 이탈(Deviation)을 분석하는 기법
- **RPN(Risk Priority Number)**: 심각도(Severity) × 발생빈도(Occurrence) × 검출도(Detection)의 곱으로 위험 우선순위를 수량화한 지수

</details>

---

## 1교시 예상문제 (10점)

> SW 안전성 분석(FTA·FMEA·HAZOP)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 정의·목적

- 정의: **SW 안전성 분석**은 시스템 고장 및 위험원을 조기에 식별하여 소프트웨어로 인한 인명/물리적 재난을 방어하는 공학 기법
- 목적: 잠재적 위험원을 사전에 제거하고 국제 기능안전(ISO 26262/IEC 61508) 인증 충족

### 2. 3대 분석 기법 핵심 비교

```mermaid
flowchart TB
    subgraph F["FTA (연역적 Top-down)"]
        TE["최상위 사고 (Top Event)"] -->|"AND/OR 논리 게이트"| MCS["최소 컷셋 (SPOF 제거)"]
    end
    subgraph M["FMEA (귀납적 Bottom-up)"]
        FM["단위 부품 고장 모드"] -->|"상위 영향 분석"| RP["RPN 산출 (S×O×D)"]
    end
    subgraph H["HAZOP (탐색적)"]
        PV["공정 변수 (속도·전압·데이터)"] -->|"가이드워드 적용"| DE["이탈(Deviation) 도출"]
    end
```

### 3. 핵심 통제

- **최소 컷셋(Minimal Cut Set)**: Top Event를 발생시키는 최소 고장 조합 식별 및 차단
- **Fail-Safe 아키텍처**: 오류 감지 시 시스템을 안전 정지 상태로 전이
---

## 2~4교시 예상문제 (25점)

> 안전 필수(Safety-critical) 시스템에서 소프트웨어 결함으로 인한 재난을 방지하기 위한 소프트웨어 안전성 분석의 필요성을 설명하고, 3대 정형 기법(FTA, FMEA, HAZOP)의 분석 관점 및 절차 비교, 기능안전 표준(ISO 26262, IEC 61508)에서의 적용 방안을 제시하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 인명 피해와 재난을 방어하는 소프트웨어 안전성 분석의 개요

> 기능적 정상 동작(신뢰성)만으로는 부족하며, 예측하지 못한 극한 상황에서도 시스템을 안전 상태(Fail-Safe)로 안착시켜야 한다.

- 정의: 소프트웨어 생명주기 전반에서 시스템 위험원(Hazard)을 조기에 식별하고, 원인과 영향을 분석하여 안전 요구사항을 도출·검증하는 일련의 엔지니어링 활동
- 목적: 잠재적 결함으로 인한 인명 손실, 환경 파괴, 재산 피해 방지, 국제 **기능안전(Functional Safety)** 인증 기준 충족

### Ⅱ. 3대 안전성 분석 기법(FTA, FMEA, HAZOP)의 메커니즘

> 연역적 하향식 분석(FTA)과 귀납적 상향식 분석(FMEA), 프로세스 편차 분석(HAZOP)을 상호 보완적으로 적용한다.

### 3대 안전성 분석 기법(FTA · FMEA · HAZOP) 메커니즘 비교

```mermaid
flowchart TB
    subgraph F["FTA (연역적 Top-down)"]
        TE["최상위 사고 (Top Event)"] -->|"AND/OR 논리 게이트"| MCS["최소 컷셋 (SPOF 제거)"]
    end
    subgraph M["FMEA (귀납적 Bottom-up)"]
        FM["단위 부품 고장 모드"] -->|"상위 영향 분석"| RP["RPN 산출 (S×O×D)"]
    end
    subgraph H["HAZOP (탐색적)"]
        PV["공정 변수 (속도·전압·데이터)"] -->|"가이드워드 적용"| DE["이탈(Deviation) 도출"]
    end
```

| 비교 항목 | FTA (결함 수목 분석) | FMEA (고장 모드 영향 분석) | HAZOP (위험 및 운전성 분석) |
|---|---|---|---|
| **분석 접근법** | **연역적 (Deductive, Top-down)** | **귀납적 (Inductive, Bottom-up)** | **탐색적 (브레인스토밍, Guide Word)** |
| **출발점** | 최상위 재앙적 사고 (Top Event) | 개별 하위 컴포넌트의 고장 모드 | 설계 의도 파라미터 및 프로세스 흐름 |
| **분석 도구** | 논리 게이트(AND, OR), 사건 기호 | FMEA 워크시트, RPN(S × O × D) | 가이드워드 매트릭스 (No, As well as 등) |
| **정량화 여부** | **정량적 확률 계산 가능 (부울 대수)** | 준정량적 (RPN 1~1000점 산출) | 정성적 분석 중심 |
| **적합한 단계** | 아키텍처 및 시스템 전체 위험 분석 | 상세설계 및 단위 컴포넌트 분석 | 요구사항 분석 및 인터페이스 연계 분석 |

### Ⅲ. FTA의 최소 컷셋(Minimal Cut Set)과 FMEA의 RPN 산출

> 안전성 분석의 최종 산출물은 정량적 우선순위에 따른 설계 개선이다.

### 1. FTA 최소 컷셋 (Minimal Cut Set)
- **Cut Set**: 그 안의 모든 기본 사건이 동시에 발생할 때 Top Event를 유발하는 사건들의 집합
- **Minimal Cut Set**: 시스템 고장을 유발하는 최소한의 기본 사건 조합 (더 이상 줄일 수 없는 형태)
- **활용**: 단일 사건으로 사고를 유발하는 Single Point of Failure(1차 Cut Set)를 우선 제거

### 2. FMEA의 RPN (Risk Priority Number) 지수
- **산식**: `RPN = 심각도(Severity, 1~10) × 발생빈도(Occurrence, 1~10) × 검출도(Detection, 1~10)`
- **조치 기준**: 통상 RPN 100점 이상 또는 심각도 9점 이상인 항목에 대해 안전 메커니즘 강제 적용

### Ⅳ. 소프트웨어 안전성 분석 문제점·대응책

> 분석된 위험원은 기능안전 표준(ISO 26262 등)의 ASIL 등급에 맞춰 아키텍처 패턴으로 설계에 반영된다.

### 1. 안전 아키텍처 메커니즘

| 아키텍처 메커니즘 | 동작 원리 | 적용 상황 |
|---|---|---|
| **Fail-Safe (고장 시 안전 보장)** | 고장 발생 시 시스템을 사전에 정의된 무해한 상태(정지, 전원 차단)로 전이 | 일반 제어 시스템의 안전 정지 |
| **Fail-Operational (고장 시 운용 유지)** | 즉시 정지가 위험한 경우 이중화로 기능 지속 제공 | 자율주행, 항공 제어 |
| **1oo2D / 2oo3 (다수결 투표·안전 다중화)** | 서로 다른 알고리즘(N-Version Programming) 결과 비교 및 워치독 모니터링 | 고신뢰 안전 채널 구성 |

### 2. 안전성 분석 실무 위험 및 대응 통제

| 위험 | 대책 | 효과 |
|---|---|---|
| 단일 고장점(SPOF)으로 인한 시스템 마비 | FTA 최소 컷셋(Minimal Cut Set) 분석 및 단일 고장 사건 제거 | 단일 컴포넌트 결함 시 재앙적 사고 예방 |
| 잠재적 부품 고장의 연쇄 영향 간과 | FMEA 기반 RPN 지수 산출 및 고위험군(RPN≥100) 조치 강제 | 부품 단위 고장의 파급 효과 사전 차단 |
| 프로세스 파라미터 이탈로 인한 오동작 | HAZOP 가이드워드 기반 이탈 분석 및 Fail-Safe 메커니즘 구축 | 비정상 제어 입력 시 안전 상태(무해 상태) 안착 |

### Ⅴ. 위험 기반 안전 논증의 결론

> 복잡한 소프트웨어 시스템에서는 전통적 인과관계 분석을 넘어 시스템 공학 기반의 STPA 기법으로 확장해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: FTA와 FMEA는 '단일 부품의 고장'을 전제로 개발된 기계/전자 시대의 유물임. 현대 복잡한 자율주행이나 클라우드 시스템에서는 부품이 고장 나지 않았는데도 컴포넌트 간 상호작용의 타이밍 오류나 비선형 피드백으로 대형 참사가 발생함. 이를 방어하기 위해 MIT의 시스템 이론 기반 안전성 분석인 STPA(System-Theoretic Process Analysis) 도입이 필수적임.
- 나라면: 소프트웨어 안전 요구사항을 RTM(추적표)에 독립 트랙으로 등록하고, 빌드 파이프라인에서 정적 분석(MISRA-C 표준 검증)과 동적 고장 주입 테스트(Fault Injection Testing)를 의무화하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 시스템 위험도 및 기능안전 등급(ISO 26262 ASIL, IEC 61508 SIL)에 따른 안전성 분석 기법 채택 판정
- **대응 방안**: **FTA(연역적 하향)** + **FMEA(귀납적 상향)** 상호보완 분석 및 복잡계 상호작용 분석을 위한 **STPA** 병행 적용
- **검증 체계**: FTA 최소 컷셋 기반 단일 고장점(SPOF) 제로화 및 RPN 100 이상 항목 대상 고장 주입 테스트(Fault Injection) 100% 통과
- **기대 효과**: 잠재 위험원 조기 격리, Fail-Safe 안전 아키텍처 구현 및 기능안전 국제 공인 인증(SIL4/ASIL-D) 획득 달성
---

## 출제 이력과 검증 출처

- 제123회 정보관리기술사 1교시: FTA, FMEA의 비교 및 위험도 평가
- 제128회 정보관리기술사 2교시: 소프트웨어 안전성 분석 기법(HAZOP, STPA)
- ISO 26262 Road vehicles - Functional safety
- IEC 61508 Functional safety of electrical/electronic/programmable electronic safety-related systems

## 연결 토픽

- 이전 토픽: [SW 규모·비용 산정](./027_sw_cost_estimation.md)
- 연관 토픽: [STPA](./108_stpa.md), [기능안전](./188_functional_safety.md)
- 다음 토픽: [메타모픽 테스트](./030_metamorphic_test.md)
