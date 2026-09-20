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
      <strong>통과 (안전 무결성 달성)</strong>
      <span>양산 배포 승인 $\rightarrow$ 인명 사고 리스크를 허용 가능한 극소 수준으로 통제</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (FTTI 초과 / 고장 전파)</strong>
      <span>출하 차단 $\rightarrow$ 하드웨어 진단 커버리지 개선 및 비상 안전 제동 로직 재설계</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **IEC 61508**: 모든 산업군 전기/전자/프로그래머블 전자 시스템의 기능안전을 총괄하는 최상위 모태(Umbrella) 국제 표준 규격
- **ISO 26262**: IEC 61508을 자동차 양산 전장(E/E) 시스템의 특성에 맞추어 테일러링한 자동차 기능안전 국제 표준
- **HARA(Hazard Analysis and Risk Assessment)**: 고장으로 인해 발생할 수 있는 위험 상황을 심각도, 노출빈도, 통제가능성으로 분석하여 ASIL 등급을 산출하는 기법
- **FTTI(Fault Tolerant Time Interval)**: 시스템에 결함이 발생한 시점부터 위험 사건(사고)이 실제로 발생하기 전까지 시스템을 안전 상태로 되돌려야 하는 최대 허용 시간 간격
- **MC/DC(Modified Condition/Decision Coverage)**: 복합 조건식에서 각 개별 조건이 다른 조건에 영향을 받지 않고 전체 결과에 독립적으로 영향을 미침을 입증하는 최고 수준의 테스트 커버리지
</details>

## 1. 개요 및 필요성

### "모든 시스템은 고장 난다"와 기능안전의 본질

자동차 자율주행, 원자력 제어기, 항공기 전자장비, 의료기기 등 인간의 생명과 직결되는 미션 크리티컬 시스템은 단 한 줄의 코드 버그나 메모리 비트 플립 고장만으로도 대참사를 초래한다.

기능안전은 "절대 고장 나지 않는 완벽한 시스템"이라는 비현실적 이상을 배제하고, **"반드시 고장이 발생한다는 전제하에 결함을 실시간 진단하여 인명 피해가 없는 안전 상태(Safe State)로 즉각 유도"**하는 엔지니어링 표준 체계이다.

### 기능안전 vs 의도된 기능의 안전(SOTIF) vs 차량 사이버보안 비교

| 구분 | 기능안전 (ISO 26262) | 의도된 기능의 안전 (SOTIF / ISO 21448) | 차량 사이버보안 (ISO/SAE 21434) |
|---|---|---|---|
| **위험 원인** | **E/E 부품 오작동 및 시스템 고장 (결함)** | **부품 고장 없음 (환경 인식 한계 및 AI 성능 부족)** | **외부 공격자의 악의적 네트워크 침투** |
| **대표 사례** | 제동 ECU 메모리 소프트 에러로 먹통 | 폭우·눈길로 인한 라이다/카메라 보행자 미인식 | 무선 OTA 패킷 변조를 통한 원격 핸들 조작 |
| **대응 기술** | **듀얼 락스텝, 워치독, Fail-Safe 전이** | 센서 퓨전, AI 코너 케이스 학습, ODD 제한 | 보안 부팅, 침입탐지(IDS), 암호화 통신 |
| **위험 지표** | **ASIL (A ~ D 등급)** | 미인지 위험 영역 축소 (Area 2/3 최소화) | CAL (사이버보안 보증 레벨) |

## 2. 아키텍처 및 핵심 메커니즘

### 기능안전 수명주기 및 위험원 분석 체계

```text
+-------------------------------------------------------------------------+
|                  기능안전(Functional Safety) 핵심 프레임워크             |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 1. 위험원 분석 및 위험 평가 (HARA) ]                                 |
|    - 심각도(Severity, S0~S3) + 노출확률(Exposure, E0~E4) + 통제가능성(C0~C3)|
|                           │                                             |
|                           v                                             |
|  [ 2. 안전 무결성 등급(ASIL) 결정 ]                                      |
|    - IEC 61508: SIL 1 ~ SIL 4 / ISO 26262: ASIL QM, A, B, C, D (최고)   |
|                           │                                             |
|                           v                                             |
|  [ 3. 안전 요구사항 도출 및 V-모델 개발 ]                               |
|    - 체계적 결함(버그) 방지: MISRA-C 코딩 표준, 100% MC/DC 커버리지    |
|    - 우발적 결함(하드웨어) 대응: 듀얼 락스텝 코어, ECC 메모리, 워치독   |
|                           │                                             |
|                           v                                             |
|  [ 4. 결함 발생 시 안전 상태(Safe State) 천이 ]                         |
|    - FTTI(결함 허용 시간 간격) 이내 Fail-Safe 또는 Fail-Operational 달성|
+-------------------------------------------------------------------------+
```

### 모태 규격과 산업별 파생 표준 체계

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 모태 규격: IEC 61508</strong></span>
      <span class="itpe-badge">공통 원천</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>전기/전자/프로그래머블 전자기기 전반의 기능안전 총괄</li>
        <li>위험도에 따라 SIL 1부터 최고 수준 SIL 4까지 등급 규정</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 자동차: ISO 26262</strong></span>
      <span class="itpe-badge">차량 전장</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>양산 승용차 및 상용차 E/E 시스템의 기능안전 국제 표준</li>
        <li>ASIL A~D 등급별 소프트웨어 개발 및 검증 기법 차등 적용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 항공: DO-178C</strong></span>
      <span class="itpe-badge">항공기 소프트웨어</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>민간 항공기 탑재 소프트웨어 인증의 사실상 표준(FAA 승인)</li>
        <li>DAL A~E(Design Assurance Level) 등급 체계 및 엄격한 검증</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 철도 & 의료: EN 50128 / IEC 62304</strong></span>
      <span class="itpe-badge">철도 신호·의료기기</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>EN 50128: 철도 제어 및 통신 소프트웨어 안전성 무결성 규격</li>
        <li>IEC 62304: 인체 생명 유지 의료기기 소프트웨어 수명주기 프로세스</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 제어 SW 복합 조건문 분기 누락으로 인한 급발진 사고(체계적 결함) 발생 | MISRA-C 시큐어 코딩 규칙 정적 검사 및 100% MC/DC 구조적 커버리지 동적 검증 의무화 | 소프트웨어 분기 결함 100% 사전 격리 |
| 우주 방사선(중성자)에 의한 메모리 단일 비트 플립(우발적 결함)으로 ECU 크래시 | 하드웨어 ECC(Error Correcting Code) 메모리 및 듀얼 코어 락스텝(Lockstep) 아키텍처 적용 | 런타임 하드웨어 결함 즉시 자가 복구 |
| 센서 고장 감지 후 안전 상태 천이 지연으로 비상 제동 실패 및 추돌 사고 발생 | 결함 허용 시간 간격(FTTI, 100ms 내외) 이내 안전 상태 전이 메커니즘을 RTOS 최우선 태스크 할당 | 인명 피해 리스크 허용 수준 이하 통제 |

## 4. 기술사 답안 차별화 포인트

### 자율주행 패러다임: Fail-Safe에서 Fail-Operational로의 진화

과거 운전자가 탑승하는 수동 차량은 고장 시 전원을 차단하고 비상 정지하는 **Fail-Safe(고장 시 정지)**로 충분했다. 그러나 운전자가 핸들을 잡지 않는 **레벨 3 이상 자율주행 및 UAM(도심항공교통)**에서는 고속도로 한복판에 차가 멈추면 대형 연쇄 추돌로 이어진다. 따라서 단일 고장이 발생해도 최소한 갓길로 안전하게 자율 이동할 수 있도록 시스템 기능을 유지하는 **Fail-Operational(축소 운전 지속) 이중화 아키텍처**로의 전환을 기술적 통찰로 제시한다.

### 안전 통합 거버넌스: ISO 26262 + ISO 21448(SOTIF) + ISO 21434(사이버보안)

현대 SDV(Software Defined Vehicle)에서는 기능안전만으로 안전을 보장할 수 없다. 고장 없는 AI 비전 인식 한계를 다루는 **SOTIF**와 외부 해킹 위협을 막는 **사이버보안**이 삼위일체로 결합된 **'통합 안전-보안 수명주기(Unified Safety & Security Lifecycle)'** 거버넌스를 결론으로 제언한다.

## 5. 참고 및 연계 학습

- [SW 안전성 분석(Safety Analysis)](./028_sw_safety_analysis.md)
- [STPA(System-Theoretic Process Analysis)](./108_stpa.md)
- [SW 안전성 진단 가이드](./137_sw_safety_diagnosis_guide.md)
- [소프트웨어 테스트 커버리지](./118_test_coverage.md)
