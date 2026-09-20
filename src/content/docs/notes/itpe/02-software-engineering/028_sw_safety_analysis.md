---
title: "SW 안전성 분석(FTA·FMEA·HAZOP)"
tags:
  - "notes-software-engineering"
author: "Antigravity"
date: "2026-09-20T21:40:00+09:00"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash (High)"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 품질·안전·신뢰성을 거쳐 SW 안전성 분석으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>품질·안전·신뢰성</span>
  <strong>SW 안전성 분석(FTA·FMEA·HAZOP)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **SW 안전성 분석**은 자동차, 철도, 항공, 원자력 등 안전 필수(Safety-Critical) 시스템에서 소프트웨어 결함으로 인한 인명 피해나 물리적 재난을 예방하기 위해 위험원(Hazard)을 조기 식별·통제하는 공학 기법
- 메커니즘: 연역적 결함 분석(**FTA**) + 귀납적 고장 모드 분석(**FMEA**) + 가이드워드 공정 분석(**HAZOP**)
- 산출/효과: 위험원 식별 · 위험도(Risk Matrix) 산출 · **안전 요구사항(Safety Requirements)** 도출 · 기능안전(ISO 26262/IEC 61508) 인증 획득

<div class="itpe-flow-map" role="img" aria-label="SW 안전성 분석 프레임워크">
  <div class="itpe-flow-node"><strong>시스템 위험원 식별</strong><span>PHA · FHA 사전 분석</span></div>
  <div class="itpe-flow-arrow">→ 분석 기법 적용 →</div>
  <div class="itpe-flow-node is-current">
    <strong>3대 안전성 분석 기법</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>FTA</strong><span><span class="itpe-keyword"><strong>연역적 Top-Down (불 대수·Cut Set)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>FMEA</strong><span><span class="itpe-keyword"><strong>귀납적 Bottom-Up (RPN 지수)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>HAZOP</strong><span>가이드워드 기반 이탈 분석</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 안전 통제책 수립 →</div>
  <div class="itpe-flow-node"><strong>안전 무결성 기준 충족</strong><span>Fail-Safe · SIL/ASIL 달성</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Software Safety(소프트웨어 안전성)**: 소프트웨어가 의도된 기능을 수행하는 것뿐만 아니라, 시스템이 위험한 고장 상태로 전이되지 않도록 보장하는 특성
- **FTA(Fault Tree Analysis)**: 사고(Top Event)에서 출발하여 논리 게이트(AND/OR)를 통해 하위 기본 고장 원인을 규명하는 연역적(Top-down) 기법
- **FMEA(Failure Mode and Effects Analysis)**: 각 부품/모듈의 고장 모드가 상위 시스템에 미치는 영향을 평가하고 RPN을 산출하는 귀납적(Bottom-up) 기법
- **HAZOP(Hazard and Operability Study)**: 설계 의도에 가이드워드(No, More, Less, As well as 등)를 적용하여 비정상적 이탈(Deviation)을 분석하는 기법
- **RPN(Risk Priority Number)**: 심각도(Severity) × 발생빈도(Occurrence) × 검출도(Detection)의 곱으로 위험 우선순위를 수량화한 지수

</details>

## 예상문제

> 안전 필수(Safety-critical) 시스템에서 소프트웨어 결함으로 인한 재난을 방지하기 위한 소프트웨어 안전성 분석의 필요성을 설명하고, 3대 정형 기법(FTA, FMEA, HAZOP)의 분석 관점 및 절차 비교, 기능안전 표준(ISO 26262, IEC 61508)에서의 적용 방안을 제시하시오. (25점)

## Ⅰ. 인명 피해와 재난을 방어하는 소프트웨어 안전성 분석의 개요

> 기능적 정상 동작(신뢰성)만으로는 부족하며, 예측하지 못한 극한 상황에서도 시스템을 안전 상태(Fail-Safe)로 안착시켜야 한다.

- 정의: 소프트웨어 생명주기 전반에서 시스템 위험원(Hazard)을 조기에 식별하고, 원인과 영향을 분석하여 안전 요구사항을 도출·검증하는 일련의 엔지니어링 활동
- 목적: 잠재적 결함으로 인한 인명 손실, 환경 파괴, 재산 피해 방지, 국제 **기능안전(Functional Safety)** 인증 기준 충족

## Ⅱ. 3대 안전성 분석 기법(FTA, FMEA, HAZOP)의 메커니즘

> 연역적 하향식 분석(FTA)과 귀납적 상향식 분석(FMEA), 프로세스 편차 분석(HAZOP)을 상호 보완적으로 적용한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="3대 안전성 분석 기법 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. FTA (Fault Tree Analysis) — 연역적 / Top-Down</strong></span>
    <span>사고 발생(Top Event) → AND/OR 논리 게이트 전개 → 최소 컷셋(Minimal Cut Set) 도출</span>
  </div>
  <div class="itpe-pipeline-arrow">↕ 상호 보완</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. FMEA (Failure Mode and Effects Analysis) — 귀납적 / Bottom-Up</strong></span>
    <span>단위 컴포넌트 고장 모드 나열 → 시스템 영향 분석 → 위험우선순위(RPN) 산출 및 조치</span>
  </div>
  <div class="itpe-pipeline-arrow">↕ 상호 보완</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. HAZOP (Hazard and Operability Analysis) — 가이드워드 기반</strong></span>
    <span>설계 의도 변수(온도, 전압, 데이터) + 가이드워드(No, More, Reverse) → 이탈 및 대책 도출</span>
  </div>
</div>

| 비교 항목 | FTA (결함 수목 분석) | FMEA (고장 모드 영향 분석) | HAZOP (위험 및 운전성 분석) |
|---|---|---|---|
| **분석 접근법** | **연역적 (Deductive, Top-down)** | **귀납적 (Inductive, Bottom-up)** | **탐색적 (브레인스토밍, Guide Word)** |
| **출발점** | 최상위 재앙적 사고 (Top Event) | 개별 하위 컴포넌트의 고장 모드 | 설계 의도 파라미터 및 프로세스 흐름 |
| **분석 도구** | 논리 게이트(AND, OR), 사건 기호 | FMEA 워크시트, RPN(S × O × D) | 가이드워드 매트릭스 (No, As well as 등) |
| **정량화 여부** | **정량적 확률 계산 가능 (부울 대수)** | 준정량적 (RPN 1~1000점 산출) | 정성적 분석 중심 |
| **적합한 단계** | 아키텍처 및 시스템 전체 위험 분석 | 상세설계 및 단위 컴포넌트 분석 | 요구사항 분석 및 인터페이스 연계 분석 |

## Ⅲ. FTA의 최소 컷셋(Minimal Cut Set)과 FMEA의 RPN 산출

> 안전성 분석의 최종 산출물은 정량적 우선순위에 따른 설계 개선이다.

### 1. FTA 최소 컷셋 (Minimal Cut Set)
- **Cut Set**: 그 안의 모든 기본 사건이 동시에 발생할 때 Top Event를 유발하는 사건들의 집합
- **Minimal Cut Set**: 시스템 고장을 유발하는 최소한의 기본 사건 조합 (더 이상 줄일 수 없는 형태)
- **활용**: 단일 사건으로 사고를 유발하는 Single Point of Failure(1차 Cut Set)를 우선 제거

### 2. FMEA의 RPN (Risk Priority Number) 지수
- **산식**: `RPN = 심각도(Severity, 1~10) × 발생빈도(Occurrence, 1~10) × 검출도(Detection, 1~10)`
- **조치 기준**: 통상 RPN 100점 이상 또는 심각도 9점 이상인 항목에 대해 안전 메커니즘 강제 적용

## Ⅳ. 소프트웨어 기능안전 표준과 실무 위험 관리

> 분석된 위험원은 기능안전 표준(ISO 26262 등)의 ASIL 등급에 맞춰 아키텍처 패턴으로 설계에 반영된다.

### 1. 안전 아키텍처 메커니즘

<div class="itpe-pipeline is-vertical" role="img" aria-label="안전 아키텍처 메커니즘">
  <div class="itpe-pipeline-node">
    <strong>Fail-Safe (고장 시 안전 보장)</strong>
    <span>고장 발생 시 시스템을 사전에 정의된 무해한 상태(정지, 전원 차단)로 전이</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Fail-Operational (고장 시 운용 유지)</strong>
    <span>자율주행, 항공 제어 등 즉시 정지가 위험한 경우 이중화로 기능 지속 제공</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1oo2D / 2oo3 (다수결 투표 및 안전 다중화)</strong></span>
    <span>서로 다른 알고리즘(N-Version Programming) 결과 비교 및 워치독 모니터링</span>
  </div>
</div>

### 2. 안전성 분석 실무 위험 및 대응 통제

| 위험 | 대책 | 효과 |
|---|---|---|
| 단일 고장점(SPOF)으로 인한 시스템 마비 | FTA 최소 컷셋(Minimal Cut Set) 분석 및 단일 고장 사건 제거 | 단일 컴포넌트 결함 시 재앙적 사고 예방 |
| 잠재적 부품 고장의 연쇄 영향 간과 | FMEA 기반 RPN 지수 산출 및 고위험군(RPN≥100) 조치 강제 | 부품 단위 고장의 파급 효과 사전 차단 |
| 프로세스 파라미터 이탈로 인한 오동작 | HAZOP 가이드워드 기반 이탈 분석 및 Fail-Safe 메커니즘 구축 | 비정상 제어 입력 시 안전 상태(무해 상태) 안착 |

## Ⅴ. 고신뢰성 SW 안전 확보를 위한 기술사적 제언

> 복잡한 소프트웨어 시스템에서는 전통적 인과관계 분석을 넘어 시스템 공학 기반의 STPA 기법으로 확장해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: FTA와 FMEA는 '단일 부품의 고장'을 전제로 개발된 기계/전자 시대의 유물임. 현대 복잡한 자율주행이나 클라우드 시스템에서는 부품이 고장 나지 않았는데도 컴포넌트 간 상호작용의 타이밍 오류나 비선형 피드백으로 대형 참사가 발생함. 이를 방어하기 위해 MIT의 시스템 이론 기반 안전성 분석인 STPA(System-Theoretic Process Analysis) 도입이 필수적임.
- 나라면: 소프트웨어 안전 요구사항을 RTM(추적표)에 독립 트랙으로 등록하고, 빌드 파이프라인에서 정적 분석(MISRA-C 표준 검증)과 동적 고장 주입 테스트(Fault Injection Testing)를 의무화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 도메인 기능안전 표준(ISO 26262 ASIL-D) 기반 전 주기 안전성 분석 판정
- 대안: **FTA(연역) + FMEA(귀납)** 하이브리드 적용 및 **STPA** 상호작용 분석 보강
- 검증: 최소 컷셋 단일 고장점 제로화 · RPN 100 이상 항목 안전 메커니즘 100% 반영
- 효과: 소프트웨어 안전 무결성 인증 통과 및 치명적 시스템 재난 사고 원천 예방

<div class="itpe-pipeline is-vertical" role="img" aria-label="SW 안전성 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>기능 테스트 편중 · 극한 상황 및 다중 고장에 대한 안전 분석 부재</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>FTA/FMEA/HAZOP 연계 위험원 분석 및 Fail-Safe 안전 아키텍처 구현</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>고장 주입 테스트(Fault Injection) 통과 및 RPN 리스크 완화 검증</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>무결점 기능안전 달성 · 인명 및 물리적 자산 피해 원천 차단</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **SW 안전성 분석**은 시스템 고장 및 위험원을 조기에 식별하여 소프트웨어로 인한 인명/물리적 재난을 방어하는 공학 기법
- 목적: 잠재적 위험원을 사전에 제거하고 국제 기능안전(ISO 26262/IEC 61508) 인증 충족

### 2. 3대 분석 기법 핵심 비교

<div class="itpe-pipeline is-vertical" role="img" aria-label="3대 기법 비교 요약">
  <div class="itpe-pipeline-node"><strong>FTA</strong><span>연역적 Top-Down · 사고(Top Event)에서 출발 · 부울 대수</span></div>
  <div class="itpe-pipeline-arrow">↕ 상호 보완</div>
  <div class="itpe-pipeline-node"><strong>FMEA</strong><span>귀납적 Bottom-Up · 부품 고장에서 출발 · RPN 지수</span></div>
  <div class="itpe-pipeline-arrow">↕ 상호 보완</div>
  <div class="itpe-pipeline-node"><strong>HAZOP</strong><span>탐색적 · 가이드워드(No, More, Less) 기반 이탈 분석</span></div>
</div>

### 3. 핵심 통제

- **최소 컷셋(Minimal Cut Set)**: Top Event를 발생시키는 최소 고장 조합 식별 및 차단
- **Fail-Safe 아키텍처**: 오류 감지 시 시스템을 안전 정지 상태로 전이

## 출제 이력과 검증 출처

- 제123회 정보관리기술사 1교시: FTA, FMEA의 비교 및 위험도 평가
- 제128회 정보관리기술사 2교시: 소프트웨어 안전성 분석 기법(HAZOP, STPA)
- ISO 26262 Road vehicles - Functional safety
- IEC 61508 Functional safety of electrical/electronic/programmable electronic safety-related systems

## 학습 체크

- [ ] FTA(연역적)와 FMEA(귀납적)의 분석 방향과 출발점의 차이를 설명할 수 있는가?
- [ ] FMEA에서 RPN(위험우선순위수)을 계산하는 3대 인자(S, O, D)를 설명할 수 있는가?
- [ ] HAZOP의 가이드워드(Guide Word)를 프로세스 파라미터에 적용하는 원리를 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [SW 규모·비용 산정](./027_sw_cost_estimation.md)
- 연관 토픽: [STPA](./108_stpa.md), [기능안전](./188_functional_safety.md)
- 다음 토픽: [메타모픽 테스트](./030_metamorphic_test.md)
