---
title: "STPA(System Theoretic Process Analysis)"
category: "02-software-engineering"
tags:
  - "STPA"
  - "STAMP"
  - "Safety-Critical"
  - "UCA"
  - "기능안전"
  - "소프트웨어안전"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 안전성 및 품질을 거쳐 STPA로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 안전성·품질</span>
  <strong>STPA(System Theoretic Process Analysis)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 개별 하드웨어·소프트웨어 부품 고장(Failure)이 없더라도 컴포넌트 간 상호작용 불일치와 제어 실패로 터지는 복잡계 참사를 막기 위해, 시스템을 '피드백 제어 구조'로 모델링하고 안전 제약조건 위반을 사전에 찾아내는 시스템 이론 기반 안전성 분석 기법
- 메커니즘: 시스템 손실·위험원 정의 → 계층적 제어 구조 모델링 → 4대 불안전 제어 행위(UCA) 도출 → 손실 시나리오 분석 및 안전 제약조건(Safety Constraint) 소프트웨어 요구사항 반영
- 산출물: 계층적 제어 구조 다이어그램 · UCA 명세서 · 손실 인과 시나리오 분석서 · 안전 제약조건 요구사항 정의서

<div class="itpe-flow-map" role="img" aria-label="STPA 4단계 분석 절차와 피드백 제어 루프">
  <div class="itpe-flow-node">
    <strong>1단계: 분석 목적 및 위험원 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>활동</strong><span>시스템 손실(Losses) 및 시스템 위험원(Hazards) 식별</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 계층적 제어 구조 모델링</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>구조</strong><span>제어기(Controller) ↔ 제어 행위 ↔ 제어 대상(Process) ↔ 피드백</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>3단계: 불안전 제어 행위(UCA) 도출</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>4대 UCA</strong><span>미제공 · 제공(잘못됨) · 타이밍/순서 오류 · 지속 시간 오류</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 손실 시나리오 분석 및 제약조건 수립</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>산출</strong><span>프로세스 모델 불일치 원인 규명 → 안전 제약조건(SRS 반영)</span></div>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **STAMP(System-Theoretic Accident Model and Processes)**: MIT 낸시 레브슨(Nancy Leveson) 교수가 제안한 이론으로, 사고를 단순 사건 연쇄가 아니라 구성요소 간 안전 제약조건 통제 실패(Control Problem)로 정의하는 모델
- **STPA(System Theoretic Process Analysis)**: STAMP 모델을 바탕으로 시스템 개발 초기부터 제어 루프 상의 위험 상호작용을 체계적으로 도출하는 안전 분석 기법
- **불안전 제어 행위(UCA, Unsafe Control Action)**: 특정 상황(Context)에서 발동되어 시스템 위험원으로 직결되는 제어 명령
- **안전 제약조건(Safety Constraint)**: UCA 발생을 방지하기 위해 제어기 및 시스템이 반드시 준수해야 하는 동작 규칙
</details>

## 1. 개요 및 필요성

### 전통적 안전 분석(FTA·FMEA)의 한계와 STPA의 등장 배경

과거의 안전성 분석 기법인 FTA(Fault Tree Analysis)와 FMEA(Failure Mode and Effects Analysis)는 1960년대 기계·전자 부품의 물리적 마모 및 단선 고장(Component Failure)을 분석하기 위해 고안되었다. 그러나 자율주행차, 도심항공교통(UAM), 스마트 팩토리 등 현대의 소프트웨어 집약형 복잡 시스템에서는 **개별 부품이 정상 규격대로 동작함에도 불구하고 시스템 간 상호작용 오류, 통신 지연, 소프트웨어의 잘못된 상황 인지로 인해 대형 참사가 발생**한다(예: 보잉 737 MAX MCAS 참사).

STPA는 사고의 원인을 부품 고장이 아닌 **"동적 피드백 제어 시스템에서 안전 제약조건 강제 실패"**로 재정의하여, 설계 초기 단계에서 컴포넌트 간 상호작용 결함과 소프트웨어 오작동 위험을 사전에 규명한다.

### 안전 분석 기법 간 비교

| 구분 | FTA(결함수 분석) | FMEA(고장형태 영향분석) | STPA(시스템 이론 프로세스 분석) |
|---|---|---|---|
| **기반 이론** | 신뢰성 공학 (사건 연쇄 모델) | 신뢰성 공학 (단일 부품 고장 모델) | 시스템 이론 및 제어 이론 (STAMP) |
| **분석 관점** | 하향식(Top-down) 연역적 분석 | 상향식(Bottom-up) 귀납적 분석 | 하향식 제어 루프 상호작용 분석 |
| **분석 대상** | 하드웨어 부품 고장 연쇄 (AND/OR) | 개별 단위 부품의 고장 모드 | 소프트웨어 제어 로직, 사람, 센서 피드백 상호작용 |
| **소프트웨어 분석** | 매우 제한적 (단순 고장 확률 입력 불가) | 부품 단위 오류로 치환되어 왜곡 | 소프트웨어 제어 알고리즘 및 프로세스 모델 불일치 완벽 분석 |
| **적용 시점** | 상세 설계 완료 후 | 상세 설계 및 제조 단계 | 개념 설계 및 아키텍처 수립 초기 단계부터 적용 가능 |

## 2. 아키텍처 및 핵심 메커니즘

### 피드백 제어 루프 4대 구성요소

STPA에서 시스템은 제어기와 제어 대상 간의 피드백 루프로 모델링된다.

```text
+-------------------------------------------------------------------------+
|                  STPA 기본 제어 루프 및 프로세스 모델                   |
+-------------------------------------------------------------------------+
|                      [ 제어기 (Controller / SW) ]                       |
|                      - 프로세스 모델 (현재 시스템 상태 인지)            |
|                      - 제어 알고리즘 (동작 결정 로직)                  |
|                                    │                                    |
|                                    │ 제어 명령 (Control Action)         |
|     +------------------------------+------------------------------+     |
|     |  [ 4대 불안전 제어 행위 (Unsafe Control Action, UCA) 유형 ] |     |
|     |  ① 미제공 (Not Providing): 위험 회피 명령 미전송             |     |
|     |  ② 제공 (Providing Causes Hazard): 위험 상황에서 잘못 전송   |     |
|     |  ③ 타이밍/순서 오류 (Too Early, Too Late, Out of Order)      |     |
|     |  ④ 지속 시간 오류 (Stopped Too Soon, Applied Too Long)       |     |
|     +------------------------------+------------------------------+     |
|                                    │                                    |
|                                    v                                    |
|                      [ 제어 대상 (Controlled Process) ]                 |
|                                    │                                    |
|                                    └───(센서 피드백 신호 / 계측값)──────>|
+-------------------------------------------------------------------------+
```

### STPA 4단계 상세 절차

<div class="itpe-pipeline-container">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1단계: 분석 기본 정의</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>인명 피해·재산 손실(Losses) 및 이를 유발하는 시스템 위험원(Hazards) 정의</span>
      <strong>산출</strong><span>손실 목록, 위험원 목록, 시스템 수준 안전 제약조건</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2단계: 제어 구조 모델링</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>인간 운전자, 제어기(ECU/SW), 구동기, 센서 간 계층적 제어 루프 다이어그램 작성</span>
      <strong>산출</strong><span>계층적 제어 구조 다이어그램(Hierarchical Control Structure)</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3단계: UCA(불안전 제어 행위) 도출</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>각 제어 명령별 4가지 가이드 워드(Not Providing, Providing, Timing, Duration) 적용하여 UCA 식별</span>
      <strong>산출</strong><span>UCA 테이블 및 소프트웨어 안전 제약조건(Safety Constraints)</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>4단계: 손실 시나리오 분석</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>UCA가 발생하는 인과 메커니즘(센서 결함, 피드백 지연, 프로세스 모델 불일치) 규명</span>
      <strong>산출</strong><span>손실 시나리오 분석서 및 안전 요구사항 명세서(SRS 반영)</span>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 컴포넌트 간 복잡 상호작용으로 도출되는 UCA 조합이 기하급수적으로 폭증 | 핵심 기능 및 고위험 제어 루프를 기준으로 분석 경계를 계층화하고 위험도 기반 우선순위 부여 | 분석 자원 낭비 방지 및 고위험 제어 루프 집중 검증 |
| 센서 지연 또는 패킷 손실로 인한 제어기 내부 인지 상태(Process Model) 왜곡 | 상태 예측 필터(Kalman Filter) 적용 및 피드백 타임아웃 발생 시 안전 정지(Fail-Safe) 로직 강제 | 센서 신호 왜곡 상황에서도 위험 제어 명령 발동 원천 차단 |
| 도출된 안전 제약조건이 단순 보고서에 머물러 실제 소프트웨어 설계에 미반영 | SysML/UML 모델 및 ALM 도구와 연계하여 SRS의 안전 필수 요구사항으로 1:1 양방향 추적 매핑 | 안전 제약조건의 아키텍처 및 소스코드 누락 방지 |

### UCA에서 안전 제약조건 도출 실무 예시

- **상황**: 고속도로 주행 보조 시스템(HDA)의 자동 비상 제동(AEB) 제어기
- **UCA-1**: 전방에 정지 차량이 존재하는 상황에서 AEB 제어기가 제동 명령을 제공하지 않음(Not Providing).
  - ➔ **안전 제약조건**: "AEB 제어기는 전방 장애물과의 충돌 예상 시간(TTC)이 1.5초 이하일 때 반드시 최대 제동 명령을 구동기에 전송해야 한다."
- **UCA-2**: 비상 제동 명령이 발동되었으나 차량이 완전 정지하기 전에 조기 해제됨(Stopped Too Soon).
  - ➔ **안전 제약조건**: "AEB 제어기는 차량 속도가 0km/h에 도달하거나 운전자의 강한 회피 조향 입력이 감지되기 전까지 제동 명령을 중단해서는 안 된다."

## 4. 기술사 답안 차별화 포인트

### 보잉 737 MAX 참사와 STPA의 실증적 가치 제시

답안 작성 시 STPA의 강력한 설득력을 높이려면 **보잉 737 MAX의 MCAS(조종특성화 증강 시스템) 참사 사례**를 반드시 언급한다. MCAS 사고는 센서 하드웨어 고장 자체보다, 소프트웨어가 조종사의 반대 입력보다 우선하여 수평 꼬리날개를 지속적으로 하향 제어한 "불안전 제어 행위(UCA - Applied Too Long & Providing in Wrong Context)"가 근본 원인이었다. STPA를 적용했다면 설계 초기 단계에서 조종사-소프트웨어 간 제어권 충돌 문제를 사전 식별하여 참사를 방지할 수 있었음을 부각하면 고득점을 확보할 수 있다.

### 안전 제약조건의 요구사항(SRS) 및 테스트 케이스 자동 전이 전략

STPA는 일회성 분석 기법이 아니라 개발 생명주기 전체에 통합되어야 한다. 3단계에서 도출된 UCA를 부정(Negation)하여 얻은 '안전 제약조건'은 소프트웨어 요구사항 명세서(SRS)의 안전 요구사항으로 전환되고, 이는 곧바로 HIL(Hardware-In-the-Loop) 및 가상 시뮬레이션의 음의 테스트(Negative Test Case) 시나리오로 직결된다. 이러한 **"STPA → 안전 제약조건 → SRS 요구사항 추적 → 안전성 테스팅" 엔지니어링 파이프라인**을 3단락 또는 전문가 제언으로 제시한다.

## 5. 참고 및 연계 학습

- [소프트웨어 안전성 가이드라인](./097_sw_safety_guidelines.md)
- [요구사항 추적표(RTM)](./102_requirement_traceability_matrix.md)
- [임베디드 소프트웨어 테스트](./089_embedded_sw_test.md)
- [ISO 26262 기능안전성](../../01-it-strategy/076_iso_26262.md)
