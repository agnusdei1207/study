---
title: "SW 안전 (SW안전 확보 지침)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "Gemini 3.8 Flash"
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

## 핵심 메커니즘과 SW안전 프레임워크

<div style="max-width: 520px; margin: 1.5rem auto;">
  <!-- SVG: SW안전 확보 지침 생명주기 및 위험원 완화 아키텍처 -->
  <svg viewBox="0 0 520 220" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" style="display: block; font-family: system-ui, -apple-system, sans-serif;">
    <!-- 배경 -->
    <rect width="520" height="220" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #e2e8f0)" stroke-width="1"/>
    
    <!-- 영역 1: 위험원 분석 & 도출 (SDLC 초기) -->
    <rect x="15" y="15" width="235" height="190" rx="6" fill="var(--color-bg-card, #ffffff)" stroke="var(--color-primary, #3b82f6)" stroke-width="1.2"/>
    <text x="132" y="32" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--color-primary, #3b82f6)">위험원 분석 및 안전 요구</text>
    <text x="132" y="46" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">Hazard 식별 및 ALARP 위험도 완화</text>

    <!-- 4대 분석 기법 그리드 -->
    <g transform="translate(25, 55)">
      <rect x="0" y="0" width="102" height="34" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
      <text x="51" y="15" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--color-text, #0f172a)">PHA (예비분석)</text>
      <text x="51" y="27" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">초기 잠재위험 식별</text>

      <rect x="112" y="0" width="102" height="34" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
      <text x="163" y="15" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--color-text, #0f172a)">FMEA (상향식)</text>
      <text x="163" y="27" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">단위 고장 영향추적</text>

      <rect x="0" y="42" width="102" height="34" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
      <text x="51" y="57" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--color-text, #0f172a)">FTA (하향식)</text>
      <text x="51" y="69" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">최상위 참사 원인도출</text>

      <rect x="112" y="42" width="102" height="34" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
      <text x="163" y="57" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--color-text, #0f172a)">STPA (복잡계)</text>
      <text x="163" y="69" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">상호작용 결함제어</text>

      <!-- 산출물: Hazard Log -->
      <rect x="0" y="85" width="214" height="42" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-primary, #3b82f6)" stroke-width="1.2"/>
      <text x="107" y="102" text-anchor="middle" font-size="9" font-weight="700" fill="var(--color-primary, #3b82f6)">단일 진실 공급원: Hazard Log</text>
      <text x="107" y="117" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">위험원 ID ↔ 안전 요구사항 ↔ 설계 모듈 맵핑</text>
    </g>

    <!-- 연결 화살표 -->
    <path d="M 252 110 L 268 110" stroke="var(--color-primary, #3b82f6)" stroke-width="1.5"/>

    <!-- 영역 2: 안전 아키텍처 & 검증 (SDLC 후기) -->
    <rect x="270" y="15" width="235" height="190" rx="6" fill="var(--color-bg-card, #ffffff)" stroke="var(--color-accent, #10b981)" stroke-width="1.2"/>
    <text x="387" y="32" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--color-accent, #10b981)">안전 아키텍처 및 V&V 검증</text>
    <text x="387" y="46" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">Fail-Safe 전이 및 결함 주입 시험</text>

    <!-- 아키텍처 및 검증 3단 -->
    <g transform="translate(280, 55)">
      <!-- 1. Fail-Safe 설계 -->
      <rect x="0" y="0" width="214" height="38" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
      <text x="107" y="15" text-anchor="middle" font-size="9" font-weight="700" fill="var(--color-text, #0f172a)">안전 아키텍처 (Fail-Safe & Redundancy)</text>
      <text x="107" y="29" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">2oo3 투표, 하드웨어 와치독, 메모리 파티셔닝</text>

      <!-- 2. 안전 코딩 표준 -->
      <rect x="0" y="45" width="214" height="38" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
      <text x="107" y="60" text-anchor="middle" font-size="9" font-weight="700" fill="var(--color-text, #0f172a)">정적 분석 (MISRA-C / C++)</text>
      <text x="107" y="74" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">동적 메모리(malloc) 전면 금지, 널 포인터 검증</text>

      <!-- 3. V&V 검증 -->
      <rect x="0" y="90" width="214" height="38" rx="4" fill="var(--color-bg, #f1f5f9)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
      <text x="107" y="105" text-anchor="middle" font-size="9" font-weight="700" fill="var(--color-text, #0f172a)">HIL 결함 주입 시험 (Fault Injection)</text>
      <text x="107" y="119" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">MC/DC 100% 달성 및 최악 시간 분석(WCET)</text>
    </g>
  </svg>
</div>

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

## 실전 합격 전략 및 기술사적 제언

### 학습자 통찰 메모 — 답안 밖
- **[핵심 통찰]**: SW 안전은 일반 SW 품질(버그 없음)이나 정보보안(침입 방지)과 명확히 구분되어야 한다. SW 안전의 핵심 척도는 "소프트웨어가 오작동하거나 멈추더라도 사람을 다치게 하거나 물리적 파괴를 일으키지 않는가(Fail-Safe)"이다.
- **나라면**: 답안 1단락에 품질/보안/안전의 3자 비교표를 명확히 제시하고, 2단락에 4대 위험원 분석 기법(PHA, FTA, FMEA, STPA)과 Hazard Log 중심의 양방향 추적성 구조를 도해화하겠다. 4단락에서는 생성형 AI/자율주행 환경에서 복잡계 상호작용 결함을 잡는 STPA 및 Safety Wrapper 가드레일을 기술사적 제언으로 연결하겠다.

### 실전 답안용 기술사적 제언
- **판정 기준**: 식별된 고위험도 위험원(Hazard Severity Class 1~2)의 완화율 100% 및 안전 필수 코드의 MC/DC 커버리지 100% 달성.
- **대응 방안**: 시스템 개발 초기부터 위험원 등록부(Hazard Log)를 가동하고, 2oo3 삼중화 투표 메커니즘과 하드웨어 독립 와치독 타이머를 적용한 Fail-Safe 아키텍처 설계.
- **검증 체계**: HIL(Hardware-in-the-Loop) 시뮬레이터 기반 물리적 단선·단락 및 센서 노이즈 결함 주입 시험(FIT)을 통해 10ms 이내 안전 상태 전이 검증.
- **기대 효과**: 제어 소프트웨어 단일 장애점(SPOF) 원천 배제 및 재난급 물리적 사고 예방을 통한 최고 수준의 기능 안전성(ASIL-D / SIL-4) 보증.

<div style="background: var(--color-bg-subtle, #f8fafc); border: 1px solid var(--color-border, #e2e8f0); border-radius: 6px; padding: 0.85rem; font-size: 0.85rem; margin-top: 1rem;">
  <strong>실전 제언 파이프라인 요약</strong>: <code>Hazard Log Registration</code> → <code>Safety Architecture (Fail-Safe)</code> → <code>MISRA-C & MC/DC 100%</code> → <code>HIL Fault Injection Testing</code>
</div>
