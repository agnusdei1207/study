---
title: "기능안전(Functional Safety)"
category: "02-software-engineering"
tags:
  - "기능안전"
  - "FunctionalSafety"
  - "IEC61508"
  - "ISO26262"
  - "ASIL"
  - "HARA"
  - "MCDC"
  - "FailSafe"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 임베디드와 미션 크리티컬 안전 공학을 거쳐 기능안전으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>임베디드·미션 크리티컬 안전 공학</span>
  <strong>기능안전(Functional Safety)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 전기·전자·프로그래머블(E/E/PE) 시스템의 하드웨어 고장이나 소프트웨어 결함으로 인한 오작동이 발생하더라도 인명 피해나 환경 재앙으로 번지지 않도록, 사전에 위험도를 분석하고 시스템을 허용 가능한 안전 상태(Safe State)로 전이시키는 국제 표준 기반 안전 무결성 공학 체계
- 메커니즘: 위험원 분석 및 위험 평가(HARA) $\rightarrow$ 안전 무결성 등급(SIL/ASIL) 결정 $\rightarrow$ 안전 목표 및 안전 요구사항 도출 $\rightarrow$ V-모델 기반 체계적 결함 방지(MISRA, MC/DC) $\rightarrow$ 안전 상태(Fail-Safe) 천이
- 산출물: 위험원 분석 보고서(HARA) · 안전 요구사항 명세서(SRS) · 안전 케이스(Safety Case) · 기능안전 감사/평가 보고서

<div class="itpe-flow-map" role="img" aria-label="기능안전 개발 생명주기 및 안전 상태 천이 판정 절차">
  <div class="itpe-flow-node">
    <strong>1단계: 위험원 분석 및 위험 평가 (HARA)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>심각도(S), 노출확률(E), 통제가능성(C) 기반 잠재적 위험 식별</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 안전 무결성 등급(ASIL) 결정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>할당</strong><span>위험도 매트릭스에 따라 ASIL QM, A, B, C, D(최고 위험) 부여</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 안전 메커니즘 구현 및 V-검증</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>검증</strong><span>듀얼 락스텝 코어, 워치독, MISRA 정적 분석, 100% MC/DC 커버리지</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 결함 허용 및 안전 상태 천이 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>결함 발생 시 결함 허용 시간 간격(FTTI) 이내에 안전 상태(Safe State)로 전이하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (기능안전 인증 획득)</strong>
      <span>Safety Case 승인 $\rightarrow$ 양산 배포 및 현장 안전 모니터링 가동</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (FTTI 초과 / 위험 전파)</strong>
      <span>아키텍처 재설계 $\rightarrow$ 하드웨어 중복화(Redundancy) 및 비상 정지 회로 보강</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **HARA(Hazard Analysis and Risk Assessment)**: 시스템의 오작동으로 인한 위험원을 식별하고, 심각도(S), 노출확률(E), 통제가능성(C)을 조합하여 위험도를 정량화하는 분석 활동
- **ASIL(Automotive Safety Integrity Level)**: 차량 기능안전 표준인 ISO 26262에서 정의한 안전 무결성 등급으로, QM(품질관리)부터 A, B, C, D(가장 엄격)까지 5단계로 분류
- **FTTI(Fault Tolerant Time Interval)**: 시스템에 결함이 발생한 시점부터 위험한 사고(Hazard)로 전이되기 전까지 안전 메커니즘이 안전 상태로 전환을 완료해야 하는 허용 한계 시간
- **MC/DC(Modified Condition/Decision Coverage)**: 복합 조건식 내 각 개별 조건이 다른 조건에 영향을 받지 않고 전체 결정문의 결과를 독립적으로 변경함을 검증하는 고신뢰성 테스트 커버리지 기준
</details>

## 1. 개요 및 필요성

### 전장화의 가속과 생명 직결 미션 크리티컬 결함

자율주행차, 도심항공교통(UAM), 원자력 제어기, 의료 로봇 등 현대 시스템은 소프트웨어의 판단에 인간의 생명을 전적으로 위임하고 있다. 고속도로를 100km/h로 질주하는 차량의 조향(Steering)이나 제동(Brake) ECU 소프트웨어에 널 포인터 역참조나 메모리 누수가 발생한다면 즉각 대형 참사로 이어진다.

기능안전(Functional Safety)은 결함이 전혀 없는 소프트웨어는 불가능하다는 공학적 전제하에, **"결함이 발생하더라도 정해진 시간(FTTI) 내에 위험을 탐지하여 안전 상태로 전이시키는 안전 무결성 보증 체계"**를 확립한다.

### 산업 도메인별 기능안전 국제 표준 체계

| 산업 도메인 | 표준 규격 | 안전 무결성 척도 | 주요 요구사항 및 특징 |
|---|---|---|---|
| **기본 모표준** | **IEC 61508** | **SIL 1 ~ SIL 4** | 전기·전자·프로그래머블 시스템 전반의 기본 안전 표준 |
| **자동차 전장** | **ISO 26262** | **ASIL QM, A, B, C, D** | 차량 E/E 시스템 대상, V-모델 전주기 개발 및 ASIL D 최고 요구 |
| **철도 제어** | **IEC 62278 (EN 50128)**| **SIL 0 ~ SIL 4** | 열차 신호 및 궤도 제어 시스템 소프트웨어 안전 규격 |
| **항공 우주** | **DO-178C** | **DAL A ~ DAL E** | 항공기 탑재 소프트웨어 검증, DAL A 등급 시 100% MC/DC 강제 |
| **의료 기기** | **IEC 62304** | **Class A, B, C** | 환자 생명 위해도에 따른 의료용 소프트웨어 생명주기 표준 |

## 2. 아키텍처 및 핵심 메커니즘

### HARA 3요소 및 ASIL 매트릭스 아키텍처

ISO 26262의 ASIL 등급은 심각도, 노출확률, 통제가능성의 3차원 위험 매트릭스를 통해 결정된다.

<div class="itpe-diagram-container" role="img" aria-label="HARA 위험원 분석 3대 파라미터 및 ASIL 위험 등급 결정 아키텍처">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: var(--color-surface, #1e293b); }
      .box { fill: var(--color-surface-card, #334155); stroke: var(--color-border, #475569); stroke-width: 1.2; rx: 5; }
      .box-active { fill: var(--color-primary-subtle, rgba(56,189,248,0.12)); stroke: var(--color-primary, #38bdf8); stroke-width: 1.5; rx: 5; }
      .title { fill: var(--color-text-strong, #f8fafc); font-family: system-ui, sans-serif; font-size: 9.5px; font-weight: 700; }
      .h-text { fill: var(--color-primary, #38bdf8); font-family: system-ui, sans-serif; font-size: 8px; font-weight: 700; }
      .text { fill: var(--color-text, #e2e8f0); font-family: system-ui, sans-serif; font-size: 7px; }
      .muted { fill: var(--color-text-muted, #94a3b8); font-family: system-ui, sans-serif; font-size: 6.2px; }
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-fs); }
    </style>
    <marker id="arrow-fs" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">위험원 분석 및 위험 평가(HARA)와 ASIL 등급 산출 아키텍처</text>

  <!-- 1. HARA 3대 평가 파라미터 -->
  <rect x="16" y="34" width="220" height="172" class="box"/>
  <text x="24" y="50" class="h-text">HARA 3대 위험 평가 지표</text>

  <rect x="24" y="58" width="204" height="34" class="box-active"/>
  <text x="30" y="72" class="text">1. 심각도 (Severity: S0 ~ S3)</text>
  <text x="30" y="84" class="muted">S3: 치명상 및 다수 사망 위험 직결</text>

  <rect x="24" y="98" width="204" height="34" class="box"/>
  <text x="30" y="112" class="text">2. 노출 확률 (Exposure: E0 ~ E4)</text>
  <text x="30" y="124" class="muted">E4: 고속 주행 등 일상적 고빈도 노출 환경</text>

  <rect x="24" y="138" width="204" height="34" class="box-active"/>
  <text x="30" y="152" class="text">3. 통제 가능성 (Controllability: C0 ~ C3)</text>
  <text x="30" y="164" class="muted">C3: 운전자가 브레이크 등으로 회피 불가능</text>

  <text x="24" y="196" class="muted">조합: S3 + E4 + C3 ➔ 최고 위험 수준 결정</text>

  <!-- 결합 화살표 -->
  <line x1="236" y1="120" x2="260" y2="120" class="arrow"/>

  <!-- 2. ASIL 등급 계층 결과 -->
  <rect x="264" y="34" width="240" height="172" class="box-active"/>
  <text x="272" y="50" class="h-text">ASIL(Automotive Safety Integrity Level) 등급</text>

  <rect x="272" y="58" width="224" height="26" style="fill:rgba(239,68,68,0.18); stroke:#ef4444; stroke-width:1.2; rx:4;"/>
  <text x="280" y="73" fill="#ef4444" font-size="7.5px" font-weight="bold">ASIL D (최고 등급): 조향/제동 ECU, 100% MC/DC 강제</text>

  <rect x="272" y="88" width="224" height="26" class="box"/>
  <text x="280" y="103" class="text">ASIL C: 차간 거리 유지(ACC), 긴급 제동 보조(AEB)</text>

  <rect x="272" y="118" width="224" height="26" class="box"/>
  <text x="280" y="133" class="text">ASIL B: 스마트 크루즈 컨트롤, 에어백 전개 제어</text>

  <rect x="272" y="148" width="224" height="24" class="box"/>
  <text x="280" y="163" class="text">ASIL A: 후방 카메라, 차선 이탈 경고(LDW)</text>

  <rect x="272" y="176" width="224" height="22" class="box"/>
  <text x="280" y="190" class="muted">QM (Quality Management): 비안전 인포테인먼트, 내비게이션</text>
</svg>
</div>

### 기능안전 핵심 메커니즘

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① Fail-Safe & Fail-Operational</strong></span>
      <span class="itpe-badge">안전 상태 전이</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>Fail-Safe: 고장 시 기능을 즉시 차단하고 안전하게 정지 (일반 차량 제동)</li>
        <li>Fail-Operational: 고장 후에도 최소 기능을 계속 유지 (자율주행 조향)</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 듀얼 코어 락스텝 (Lockstep)</strong></span>
      <span class="itpe-badge">하드웨어 고장 탐지</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>동일한 명령어를 실행하는 두 개의 독립 CPU 코어 결과를 클록 단위 대조</li>
        <li>알파 입자나 전자기 노이즈로 인한 비트 반전(Bit-flip) 결함을 즉각 감지</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ MISRA C / 시큐어 코딩</strong></span>
      <span class="itpe-badge">체계적 결함 방지</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>동적 메모리 할당(`malloc`) 및 재귀 호출(Recursion) 전면 금지 규칙 적용</li>
        <li>정적 분석 도구(QAC, Coverity)로 런타임 예외 가능성을 컴파일 시점 차단</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ MC/DC 테스트 커버리지</strong></span>
      <span class="itpe-badge">정밀 검증</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>복합 조건식 `(A or B) and C`의 각 조건이 결과에 미치는 독립적 영향 검증</li>
        <li>ASIL D 및 DO-178C DAL A 등급 통과를 위한 법적 필수 검증 항목</li>
      </ul>
    </div>
  </div>
</div>

### 결함 허용 시간 간격(FTTI)과 안전 상태(Safe State) 전이 시계열

안전 메커니즘은 결함 발생부터 사고로 이어지기 전의 골든타임(FTTI) 이내에 작동해야 한다.

<div class="itpe-diagram-container" role="img" aria-label="결함 발생, 결함 탐지 시간, 결함 처리 시간 및 FTTI 안전 상태 전이 시계열 다이어그램">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: var(--color-surface, #1e293b); }
      .box { fill: var(--color-surface-card, #334155); stroke: var(--color-border, #475569); stroke-width: 1.2; rx: 5; }
      .box-active { fill: var(--color-primary-subtle, rgba(56,189,248,0.12)); stroke: var(--color-primary, #38bdf8); stroke-width: 1.5; rx: 5; }
      .title { fill: var(--color-text-strong, #f8fafc); font-family: system-ui, sans-serif; font-size: 9.5px; font-weight: 700; }
      .h-text { fill: var(--color-primary, #38bdf8); font-family: system-ui, sans-serif; font-size: 8px; font-weight: 700; }
      .text { fill: var(--color-text, #e2e8f0); font-family: system-ui, sans-serif; font-size: 7px; }
      .muted { fill: var(--color-text-muted, #94a3b8); font-family: system-ui, sans-serif; font-size: 6.2px; }
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-ft); }
      .time-bar { stroke: #38bdf8; stroke-width: 2.5; }
    </style>
    <marker id="arrow-ft" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">FTTI(Fault Tolerant Time Interval) 및 안전 상태(Safe State) 천이 메커니즘</text>

  <!-- 타임라인 축 -->
  <line x1="30" y1="95" x2="490" y2="95" class="time-bar"/>
  
  <!-- 지점 1: 정상 운영 -->
  <circle cx="50" cy="95" r="5" fill="#38bdf8"/>
  <text x="35" y="80" class="h-text">정상 상태</text>
  <text x="30" y="112" class="muted">정상 제어 수행</text>

  <!-- 지점 2: 결함 발생 (Fault) -->
  <circle cx="150" cy="95" r="5" fill="#eab308"/>
  <text x="132" y="80" fill="#eab308" font-size="7.5px" font-weight="bold">결함 발생 (t0)</text>
  <text x="130" y="112" class="muted">센서 고장/메모리 비트반전</text>

  <!-- 지점 3: 결함 탐지 (Detected) -->
  <circle cx="270" cy="95" r="5" fill="#38bdf8"/>
  <text x="250" y="80" class="h-text">결함 탐지 (t1)</text>
  <text x="250" y="112" class="muted">워치독/락스텝 감지</text>

  <!-- 지점 4: 안전 상태 전이 완료 (Safe State) -->
  <circle cx="390" cy="95" r="5" fill="#10b981"/>
  <text x="360" y="80" fill="#10b981" font-size="7.5px" font-weight="bold">안전 상태 천이 (t2)</text>
  <text x="360" y="112" class="muted">비상 정지/감속 완료</text>

  <!-- 지점 5: 위험 사고 발생 한계 (Hazard) -->
  <circle cx="470" cy="95" r="5" fill="#ef4444"/>
  <text x="445" y="80" fill="#ef4444" font-size="7.5px" font-weight="bold">사고 발생 (t_haz)</text>
  <text x="445" y="112" class="muted">전복/충돌 위험</text>

  <!-- FTTI 구간 표시 -->
  <line x1="150" y1="135" x2="470" y2="135" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
  <text x="255" y="148" fill="#ef4444" font-size="7.5px" font-weight="bold">&lt;------- FTTI (결함 허용 시간 간격: 허용 최대 한계) -------&gt;</text>

  <!-- 실제 조치 구간 -->
  <rect x="150" y="160" width="240" height="42" class="box-active"/>
  <text x="160" y="175" class="h-text">실제 안전 메커니즘 동작 시간 = [결함 탐지 시간] + [결함 처리 시간]</text>
  <text x="160" y="188" class="text">안전 판정 공식: (t_detect + t_reaction) &lt; FTTI ➔ 반드시 FTTI 이내에 안전 상태 진입 완료</text>
  <text x="160" y="196" class="muted">결함이 사고로 이어지는 것을 100% 사전에 물리적으로 차단</text>
</svg>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| ASIL D 시스템에서 하드웨어 단일 결함(비트 반전)으로 CPU 연산 오류가 제어기에 그대로 전파 | 듀얼 코어 락스텝(Lockstep) MCU 도입 및 ECC(오류 정정 코드) 메모리 하드웨어 적용 | 단일 고장 탐지율(SPFM) 99% 이상 달성 |
| 복잡한 C++ 포인터 연산 및 동적 메모리(`malloc`) 누수로 런타임 힙 고갈 및 스티어링 락다운 | MISRA C:2012 코딩 표준 강제화 및 정적 검사 도구를 통한 빌드 단계 컴파일 차단 | 포인터 런타임 메모리 오류 100% 원천 예방 |
| 레벨 3 이상 자율주행 중 제동/조향 결함 시 Fail-Safe(단순 정지) 적용으로 고속도로 후방 추돌 | 이중화 제어기를 갖춘 Fail-Operational(기능 지속) 구조로 설계하여 안전 갓길 자율 정차 유도 | 2차 대형 교통사고 위험율 제로화 |

## 4. 기술사 답안 차별화 포인트

### Fail-Safe에서 Fail-Operational (자율주행 레벨 4/5)로의 패러다임 전환

과거 레벨 2 자율주행까지는 고장 시 운전자에게 제어권을 넘기고 비상 정지하는 **Fail-Safe**로 충분했다. 그러나 운전자의 개입이 없는 완전 자율주행(레벨 4/5)이나 로보택시에서는 고장 시 멈춰 서면 그 자체가 도로 위의 치명적 장애물이 된다. 답안에서는 고장이 발생해도 최소 10초 이상 조향과 제동을 유지하며 갓길로 대피시키는 **Fail-Operational (이중화 아키텍처)**의 필연적 요구를 강조한다.

### SOTIF (ISO 21448)와 기능안전의 융합

전통적 기능안전(ISO 26262)은 '부품의 고장'을 다룬다. 그러나 인공지능 자율주행은 **카메라나 라이다가 고장 나지 않았음에도, 역광이나 폭설로 인해 장애물을 인식하지 못하는 "의도된 기능의 한계"**가 발생한다. 기술사 답안에서는 기능안전(ISO 26262)과 이를 보완하는 **SOTIF(Safety of the Intended Functionality, ISO 21448)**의 통합 프레임워크를 결론으로 제시하여 최신 전장 엔지니어링 식견을 뽐낸다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 기능안전은 "소프트웨어가 버그 없이 완벽해야 한다"는 이상론이 아니라, "반드시 고장이 날 텐데 그때 어떻게 안전하게 죽일 것인가(Safe State)"를 규정하는 냉철한 엔지니어링이다. FTTI라는 시간 제약 안에서 탐지-처리가 끝나는가가 생사를 가른다.
- [나라면]: 1교시형 단답 시 HARA 3요소(심각도 S, 노출확률 E, 통제가능성 C)와 ASIL 등급(QM, A~D)을 명쾌히 표로 제시하겠다. 2교시형 서술에서는 고장 시간표(FTTI)를 도식화하고, 자율주행 시대로 가면서 Fail-Safe(단순 정지)에서 Fail-Operational(기능 지속)로 진화하는 아키텍처와, 시스템 고장이 없어도 환경 한계로 사고가 나는 SOTIF(ISO 21448)의 융합을 기술사적 해법으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: ASIL D 핵심 제어 경로의 MC/DC 테스트 커버리지 100% 달성 및 안전 메커니즘 조치 시간 &lt; FTTI 검증 완료 여부
- **대응 방안**: 시스템 레벨 HARA 분석을 통해 ASIL을 분배하고, MISRA 준수 정적 분석과 듀얼 락스텝 하드웨어를 결합한 안전 상태 천이 체계 구축
- **검증 체계**: HARA 위험성 평가 ➔ V-모델 단위/통합 검증 ➔ 결함 주입 테스트(FIT) ➔ 독립 공인기관 Safety Case 감사
- **기대 효과**: 미션 크리티컬 시스템의 인명 사고율 제로화, 글로벌 기능안전 공인 인증(TÜV) 획득 및 PL(제조물 책임) 리스크 원천 차단

<div class="itpe-pipeline-container" role="img" aria-label="기능안전 엔지니어링 생명주기 파이프라인">
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">01</div>
    <div class="itpe-pipeline-step-content">
      <strong>HARA 위험 분석</strong>
      <span>심각도·노출·통제 평가 기반 ASIL(A~D) 등급 확정</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">02</div>
    <div class="itpe-pipeline-step-content">
      <strong>안전 요구사항 도출</strong>
      <span>FTTI 산출 및 Fail-Safe/Operational 메커니즘 설계</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">03</div>
    <div class="itpe-pipeline-step-content">
      <strong>V-검증 및 MC/DC</strong>
      <span>MISRA 정적 분석과 결함 주입(FIT) 100% 커버리지 검증</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">04</div>
    <div class="itpe-pipeline-step-content">
      <strong>Safety Case 인증</strong>
      <span>안전 논증 보고서 승인 및 양산 배치 모니터링 가동</span>
    </div>
  </div>
</div>

## 5. 참고 및 연계 학습

- [소프트웨어 안전성 진단 가이드](./137_sw_safety_diagnosis_guide.md)
- [화이트박스 테스트(MC/DC)](./013_white_box_test.md)
- [카오스 테스트(Chaos Engineering)](./176_chaos_test.md)
- [V-모델(V-Model)](./002_v_model.md)
