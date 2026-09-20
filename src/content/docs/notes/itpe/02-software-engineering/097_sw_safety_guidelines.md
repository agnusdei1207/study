---
title: "SW 안전 (SW안전 확보 지침)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "Gemini 3.8 Flash (High)"
author: "Antigravity"
lastModified: "2026-03-30T10:00:00+09:00"
---

## 큰 그림과 30초 인출

- **본질**: 소프트웨어의 결함이나 오작동이 시스템 물리적 파괴, 인명 사상, 대규모 환경 재해로 이어지는 것을 막기 위해 개발 전 생명주기에 걸쳐 위험원(Hazard)을 선제 식별하고 페일세이프(Fail-Safe) 체계를 구축하는 제도적·공학적 안전 활동이다.
- **메커니즘**: 안전 계획 $\rightarrow$ 위험원 분석(PHA/FMEA/FTA/STPA) $\rightarrow$ 안전 요구사항 도출 $\rightarrow$ 안전 아키텍처 설계(이중화, 격리) $\rightarrow$ 안전 검증(V&V, HIL 결함 주입) $\rightarrow$ 안전 운영 순서로 통제한다.
- **산출물**: SW 안전관리 계획서, 위험원 등록부(Hazard Log), 안전 요구사항 추적표, 안전성 검증 보고서(V&V Report).

<div class="itpe-flow">
  <div class="itpe-flow-steps">
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>1. 안전 계획</strong></span>
      <div class="itpe-step-detail">안전관리 조직 지정 및 안전 보증 계획서(Safety Plan) 작성</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>2. 위험원 분석</strong></span>
      <div class="itpe-step-detail">PHA(예비), FTA(하향식), FMEA(상향식), STPA(상호작용) 분석</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>3. 안전 설계 & 구현</strong></span>
      <div class="itpe-step-detail">Fail-Safe 전이, 하드웨어 와치독, MISRA-C 코딩 표준 준수</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node is-current">
      <span class="itpe-keyword"><strong>Quality Gate</strong></span>
      <div class="itpe-step-detail"><strong>판정 질문</strong><span>모든 위험원이 설계 및 V&V 테스트까지 양방향 추적되는가?</span></div>
      <div class="itpe-flow-branches">
        <div class="itpe-flow-branch"><strong>통과</strong><span>시스템 통합 및 안전성 인증 검증 승인</span></div>
        <div class="itpe-flow-branch"><strong>미통과</strong><span>누락·중복 제거 및 위험원 완화 대책 재설계</span></div>
      </div>
    </div>
  </div>
</div>

---

## 핵심 메커니즘

### (1) SW 품질(Quality) vs SW 보안(Security) vs SW 안전(Safety)

| 구분 | SW 품질 (Quality) | SW 보안 (Security) | SW 안전 (Safety) |
|---|---|---|---|
| **핵심 목적** | 요구사항 명세대로 올바르게 작동하는가(Correctness) | 외부 악의적 공격자로부터 시스템을 보호하는가(Protection) | **오작동 시에도 인명 사상이나 환경 파괴가 없는가(Safety)** |
| **위협 요인** | 기능 미구현, 연산 버그, 사용자 편의성 결여 | 해킹, 악성코드, 데이터 유출, 권한 탈취 | **하드웨어 고장, 센서 오작동, 소프트웨어 데드락, 결함 전파** |
| **주요 활동** | 기능 테스트, 성능 테스트, 사용성 평가 | 취약점 진단, 암호화, 접근 제어, 침입 탐지 | **위험원 분석(Hazard Analysis), 페일세이프, V&V 검증** |
| **대표 표준** | ISO/IEC 25010 | ISO/IEC 27001, ISMS-P | **소프트웨어 진흥법 지침, ISO 26262, IEC 61508** |

### (2) 과학기술정보통신부 'SW안전 확보 지침' 6단계 생명주기
1. **안전 계획**: 대상 시스템의 안전 무결성 등급 평가 및 안전 관리자 지정, 안전 보증 계획 수립.
2. **위험원 분석**: 시스템 가동 중 발생 가능한 모든 위험원(Hazard)을 식별하고 심각도(Severity)와 발생 빈도(Frequency)를 산정하여 위험도 평가.
3. **안전 요구사항 도출**: 식별된 위험원을 허용 가능한 수준(ALARP)으로 제거·완화하기 위한 시스템 및 소프트웨어 기능 요구사항 명세.
4. **안전 아키텍처 설계**: 결함 감내(Fault-Tolerant), 페일세이프(Fail-Safe), 메모리 분리 격리(Memory Protection), 이중화/삼중화(2oo3) 아키텍처 반영.
5. **안전성 검증(V&V)**: MISRA-C/C++ 표준 기반 정적 코드 분석, HIL 환경 기반 결함 주입 시험(FIT), MC/DC 100% 구조적 커버리지 달성.
6. **안전 운영 및 유지보수**: 형상 변경 시 안전성 영향 평가 의무화 및 긴급 이상 징후 발생 시 안전 상태 자동 전이.

### (3) 대표적 위험원 분석 기법 (PHA, FMEA, FTA, STPA)
- **PHA (Preliminary Hazard Analysis)**: 개발 초기 개념 단계에서 잠재 위험 요소를 조기에 식별하는 예비 위험원 분석.
- **FMEA (상향식, Bottom-Up)**: 부품·단위 컴포넌트의 단일 고장 모드가 시스템 전체에 미치는 영향을 순차 추적.
- **FTA (하향식, Top-Down)**: 최상위 참사(Top Event)를 정의하고 불 대수(Boolean Logic)를 통해 근본 원인 조합(Cut Set)을 연역적으로 분석.
- **STPA (System-Theoretic Process Analysis)**: 단순 부품 고장을 넘어 정상 부품들 간의 복잡한 피드백 제어 및 상호작용 오류(Unsafe Control Action, UCA)를 체계적으로 분석하는 시스템 이론 기법.

---

## 실무 적용 및 도입 체크리스트

1. **위험원 등록부(Hazard Log) 운영**: 프로젝트 착수부터 폐기까지 모든 위험원 식별 번호와 완화 조치 상태를 단일 등록부로 추적 관리하는가?
2. **양방향 추적성(Bi-directional Traceability)**: 식별된 위험원 $\rightarrow$ 안전 요구사항 $\rightarrow$ 설계 모듈 $\rightarrow$ V&V 테스트 케이스 간 완벽한 추적 링크가 형성되어 있는가?
3. **하드웨어 와치독(Watchdog) 및 페일세이프 설계**: 프로세서 루프가 멈추거나 응답 지연 발생 시 즉시 시스템을 안전 상태(전원 차단 또는 기계식 브레이크 체결)로 전환하는 기구적 방어선이 구축되어 있는가?
4. **정적 코딩 표준 준수**: 임베디드 소스코드 전반에 걸쳐 포인터 널 참조, 버퍼 오버플로를 유발하는 동적 메모리 할당(malloc)을 금지하고 MISRA-C 룰을 통과하였는가?

---

## 실패 시나리오 및 트러블슈팅

| 위험 | 대책 | 효과 |
|---|---|---|
| **센서 지연으로 로봇 제어기 무한 대기 및 충돌 사고** | 하드웨어 와치독 연동 및 센서 타임아웃 시 즉시 물리 브레이크 체결(Fail-Safe) | 오작동 시 10ms 이내 강제 정지 및 인명 사상 사고 원천 방지 |
| **포인터 널 참조로 인한 제어기 런타임 크래시** | MISRA-C/C++ 표준 정적 분석 의무화 및 동적 메모리 할당 전면 금지 | 런타임 메모리 누수 및 크래시 위험 원천 차단 |
| **신규 패치 배포 후 기존 안전 인터록 기능 무력화** | 형상 변경 시 안전 영향성 평가 의무화 및 회귀 HIL 결함 주입 시험 재수행 | 변경으로 인한 사이드 이펙트 100% 검출 및 안전성 유지 |

---

## 차세대 확장 및 융합

- **복잡계 제어 시스템과 STPA의 표준화**: 도심항공교통(UAM), 자율주행차, 의료용 AI 로봇 등 복합 시스템에서는 개별 부품 고장보다 컴포넌트 간 상호작용 결함이 사고의 주원인이 되므로, ISO 26262/ISO 21448(SOTIF) 규격에서 STPA 적용이 의무화되고 있다.
- **AI 안전(Safety for AI)**: 딥러닝 기반 예측 모델의 확률적 불확실성을 통제하기 위해, 모델 예측값이 신뢰 구간을 벗어날 경우 결정론적 고전 안전 제어기로 즉시 제어권을 넘기는 이중화 안전 가드레일(Safety Wrapper) 기술이 도입되고 있다.

---

## 25점형 실전 답안 프레임워크

### 1단락: SW 안전의 대두 배경 및 개념
- **배경**: 자율주행, 철도, 의료기기 등 사이버-물리 시스템(CPS) 확산에 따라 소프트웨어 오작동이 인명 사고로 직결되는 파국적 위험 급증.
- **정의**: 소프트웨어 결함으로 인한 인명 피해나 환경 재난을 예방하기 위해 SDLC 전 단계에 걸쳐 위험원을 통제하고 안전 무결성을 보증하는 공학 및 제도 체계.

### 2단락: 과기정통부 'SW안전 확보 지침' 생명주기 및 위험원 분석 기법
- **SW안전 6단계 프레임워크**: 안전 계획 $\rightarrow$ 위험원 분석 $\rightarrow$ 안전 요구 $\rightarrow$ 안전 설계 $\rightarrow$ 안전 검증 $\rightarrow$ 안전 운영.
- **위험원 분석 기법 비교**: PHA(초기 예비 분석), FMEA(상향식 단일 고장 모드), FTA(하향식 결함 트리), STPA(시스템 이론 상호작용 제어 분석).

### 3단락: 안전 아키텍처 설계 및 공학적 검증 방안
- **페일세이프(Fail-Safe) 및 결함 감내(Fault-Tolerant)**: 2oo3 삼중화 투표, 와치독 타이머, 메모리 파티셔닝(ARINC 653).
- **엄격한 V&V 검증**: MISRA-C 정적 분석, PIL 단계 MC/DC 100% 커버리지, HIL 단계 결함 주입 시험(FIT).

### 4단락: 실질적 SW 안전 확보를 위한 기술사적 제언
- **형식적 서류 작업을 탈피한 'Hazard Log' 기반 품질 게이트**: 납품 직전 문서를 끼워맞추는 관행을 근절하고, 요구사항 정의 첫 단계부터 공인 안전 엔지니어가 참여하는 위험원 등록부를 개설하여 양방향 추적성이 입증되지 않으면 다음 마일스톤 진입을 불허하는 엄격한 거버넌스를 제언함.

---

## 10점형 핵심 요약

1. **정의**: 소프트웨어 오작동으로 인한 인명 사상 및 물리적 피해를 방지하기 위해 전 생명주기에 걸쳐 위험원을 분석·완화하는 법정 공학 활동.
2. **핵심 메커니즘**:
   - **위험원 분석**: FTA(하향식), FMEA(상향식), STPA(상호작용).
   - **안전 설계**: 페일세이프(Fail-Safe), 하드웨어 와치독, 동적 할당 배제.
3. **실무 핵심**: 위험원 등록부(Hazard Log)를 기반으로 요구사항-설계-V&V 테스트 간 양방향 추적성을 완벽히 확보함.
