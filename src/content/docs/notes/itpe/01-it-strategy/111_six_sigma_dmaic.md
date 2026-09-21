---
title: "Six Sigma DMAIC"
author: "Antigravity"
date: "2026-09-22T11:25:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 품질혁신을 거쳐 Six Sigma DMAIC로 이어지는 위치">
  <span>IT 전략·관리</span><span>품질혁신·프로세스 개선</span><strong>DMAIC</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 고객 요구를 기준으로 기존 프로세스의 결함·변동 원인을 데이터로 개선
- **절차**: Define → Measure → Analyze → Improve → Control
- **통제**: 측정 신뢰성·근본원인 검증·Pilot·Control Plan

<div class="itpe-svg-map">
<svg viewBox="0 0 760 600" role="img" aria-label="DMAIC 순환 구조">
  <defs><marker id="dmaic-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link"></path></marker></defs>
  <circle cx="380" cy="300" r="92" class="itpe-svg-node is-current"></circle>
  <text x="380" y="290" text-anchor="middle" class="itpe-svg-title">DMAIC</text><text x="380" y="325" text-anchor="middle" class="itpe-svg-sub">Data-driven Improvement</text>
  <circle cx="380" cy="80" r="65" class="itpe-svg-node"></circle><text x="380" y="88" text-anchor="middle" class="itpe-svg-title">Define</text>
  <circle cx="595" cy="230" r="65" class="itpe-svg-node"></circle><text x="595" y="238" text-anchor="middle" class="itpe-svg-title">Measure</text>
  <circle cx="515" cy="485" r="65" class="itpe-svg-node"></circle><text x="515" y="493" text-anchor="middle" class="itpe-svg-title">Analyze</text>
  <circle cx="245" cy="485" r="65" class="itpe-svg-node"></circle><text x="245" y="493" text-anchor="middle" class="itpe-svg-title">Improve</text>
  <circle cx="165" cy="230" r="65" class="itpe-svg-node"></circle><text x="165" y="238" text-anchor="middle" class="itpe-svg-title">Control</text>
  <path d="M438 105 C510 125 555 160 570 175" class="itpe-svg-link" marker-end="url(#dmaic-arrow)"></path>
  <path d="M610 295 C610 365 565 410 550 430" class="itpe-svg-link" marker-end="url(#dmaic-arrow)"></path>
  <path d="M450 510 C370 545 310 525 300 515" class="itpe-svg-link" marker-end="url(#dmaic-arrow)"></path>
  <path d="M205 430 C160 385 140 325 145 290" class="itpe-svg-link" marker-end="url(#dmaic-arrow)"></path>
  <path d="M150 165 C175 105 285 75 315 75" class="itpe-svg-link" marker-end="url(#dmaic-arrow)"></path>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **DMAIC(Define, Measure, Analyze, Improve, Control)**: 기존 프로세스 개선을 위한 5단계 문제해결 절차
- **VOC(Voice of Customer)**: 고객 요구·불만·기대
- **CTQ(Critical to Quality)**: 고객 관점에서 중요한 측정 가능한 품질특성
- **DPMO(Defects Per Million Opportunities)**: 백만 결함기회당 결함 수
- **MSA(Measurement System Analysis)**: 측정시스템의 변동·신뢰성을 평가하는 분석
- **SPC(Statistical Process Control)**: 관리도로 프로세스 변동을 감시·통제하는 기법
- **SIPOC(Supplier, Input, Process, Output, Customer)**: 프로세스 범위와 이해관계를 요약하는 도식
- **DOE(Design of Experiments)**: 여러 요인의 효과와 상호작용을 검증하는 실험계획법
- **FMEA(Failure Mode and Effects Analysis)**: 잠재 고장형태와 영향을 분석해 위험을 우선순위화하는 기법
- **SOP(Standard Operating Procedure)**: 표준운영절차
- **SLI(Service Level Indicator)**: 서비스 수준을 측정하는 지표

</details>

## 예상문제

> **(미출제 예상·25점)** Six Sigma의 개념과 DMAIC 단계별 활동·도구·산출물을 설명하고, Lean과의 차이 및 IT 서비스 적용방안을 제시하시오.

## Ⅰ. Six Sigma·DMAIC 개요

> DMAIC는 직관적 처방이 아니라 측정 가능한 CTQ와 검증된 원인에 기반해 기존 프로세스를 개선함

- **정의**: 고객 요구에 미달하는 기존 프로세스의 결함·변동을 데이터로 분석·개선·통제하는 방법론
- **목적**: CTQ 개선·변동 감소·개선성과의 지속

Six Sigma의 3.4 DPMO는 장기 공정 이동(1.5σ Shift)을 가정한 대표적 품질수준(99.99966%)이며, 모든 IT 서비스에 일률 적용하는 의무 기준은 아님.

## Ⅱ. DMAIC 단계별 활동·산출

| 단계 | 활동 | 주요 도구 | 산출 |
|---|---|---|---|
| Define | 문제·고객·범위·목표 정의 | VOC·CTQ·SIPOC | Project Charter |
| Measure | 측정체계 검증·Baseline 측정 | MSA·DPMO·Process Capability | 측정계획·현수준 |
| Analyze | 근본원인 검증 | Pareto·가설검정·회귀 | Vital Few 원인 |
| Improve | 대안 설계·Pilot 검증 | DOE·FMEA·Pilot | 개선안·검증결과 |
| Control | 표준화·감시·대응 | SPC·Control Plan·SOP | 관리계획·표준 |

## Ⅲ. 6시그마 통계적 메커니즘과 DMAIC 파이프라인

```
[6 Sigma 통계적 기준]                         [DMAIC 5단계 로드맵]
 1.5σ Shift 고려 시 3.4 DPMO               Define   : VOC -> CTQ 도출 및 헌장 작성
 LSL        μ        USL                   Measure  : 데이터 수집 및 현수준(DPMO) 산정
 ───┼───────┼───────┼───                   Analyze  : 근본원인(Vital Few) 통계적 규명
   -6σ     0      +6σ                     Improve  : 최적해 도출 및 파일럿 적용
 (합격률 99.99966%)                        Control  : SPC 관리도 및 표준화/SOP 수립
```

<div class="itpe-svg-map">
<svg viewBox="0 0 520 220" role="img" aria-label="6시그마 통계적 정규분포 및 DMAIC 5단계 개선 파이프라인">
  <!-- 배경 바운더리 -->
  <rect x="10" y="10" width="500" height="200" rx="8" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" />

  <!-- 좌측 영역: 6시그마 정규분포 곡선 -->
  <g transform="translate(15, 20)">
    <rect x="0" y="0" width="220" height="175" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
    <text x="110" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">6 Sigma 정규분포 (±6σ)</text>
    
    <!-- 정규분포 곡선 -->
    <path d="M 15 130 C 60 130, 80 120, 95 65 C 105 35, 115 35, 125 65 C 140 120, 160 130, 205 130" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
    
    <!-- 규격선 USL / LSL -->
    <line x1="25" y1="35" x2="25" y2="135" stroke="var(--sl-color-gray-3)" stroke-width="1.5" stroke-dasharray="3,3" />
    <text x="25" y="148" text-anchor="middle" font-size="8.5" fill="var(--sl-color-gray-2)">LSL</text>

    <line x1="110" y1="30" x2="110" y2="135" stroke="var(--sl-color-accent)" stroke-width="1" />
    <text x="110" y="148" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--sl-color-accent)">μ (평균)</text>

    <line x1="195" y1="35" x2="195" y2="135" stroke="var(--sl-color-gray-3)" stroke-width="1.5" stroke-dasharray="3,3" />
    <text x="195" y="148" text-anchor="middle" font-size="8.5" fill="var(--sl-color-gray-2)">USL</text>

    <rect x="25" y="155" width="170" height="18" rx="3" fill="var(--sl-color-accent-low)" stroke="var(--sl-color-accent)" stroke-width="1" />
    <text x="110" y="167" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--sl-color-accent-high)">3.4 DPMO (1.5σ Shift 반영)</text>
  </g>

  <!-- 우측 영역: DMAIC 5단계 파이프라인 -->
  <g transform="translate(250, 20)">
    <rect x="0" y="0" width="250" height="175" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
    <text x="125" y="20" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">DMAIC 5단계 문제해결</text>

    <!-- Step D -->
    <rect x="15" y="30" width="60" height="26" rx="4" fill="var(--sl-color-gray-5)" stroke="var(--sl-color-gray-3)" stroke-width="1" />
    <text x="45" y="47" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--sl-color-text)">Define</text>
    <text x="85" y="47" font-size="9" fill="var(--sl-color-gray-2)">VOC → CTQ, SIPOC</text>

    <!-- Step M -->
    <rect x="15" y="60" width="60" height="26" rx="4" fill="var(--sl-color-gray-5)" stroke="var(--sl-color-gray-3)" stroke-width="1" />
    <text x="45" y="77" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--sl-color-text)">Measure</text>
    <text x="85" y="77" font-size="9" fill="var(--sl-color-gray-2)">MSA, DPMO Baseline</text>

    <!-- Step A -->
    <rect x="15" y="90" width="60" height="26" rx="4" fill="var(--sl-color-gray-5)" stroke="var(--sl-color-gray-3)" stroke-width="1" />
    <text x="45" y="107" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--sl-color-text)">Analyze</text>
    <text x="85" y="107" font-size="9" fill="var(--sl-color-gray-2)">Vital Few 원인 (파레토/회귀)</text>

    <!-- Step I -->
    <rect x="15" y="120" width="60" height="26" rx="4" fill="var(--sl-color-accent-low)" stroke="var(--sl-color-accent)" stroke-width="1" />
    <text x="45" y="137" text-anchor="middle" font-size="9.5" font-weight="bold" fill="var(--sl-color-accent-high)">Improve</text>
    <text x="85" y="137" font-size="9" fill="var(--sl-color-text)">DOE 최적화, Pilot 검증</text>

    <!-- Step C -->
    <rect x="15" y="150" width="60" height="22" rx="4" fill="var(--sl-color-accent-low)" stroke="var(--sl-color-accent)" stroke-width="1" />
    <text x="45" y="165" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--sl-color-accent-high)">Control</text>
    <text x="85" y="165" font-size="9" fill="var(--sl-color-gray-2)">SPC 관리도, SOP 표준화</text>
  </g>
</svg>
</div>

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 서비스 DMAIC 적용 절차">
  <div class="itpe-flow-node"><strong>Define</strong><div class="itpe-step-detail"><strong>활동</strong><span>서비스 문제·CTQ·범위 정의</span></div><div class="itpe-step-detail"><strong>산출</strong><span>Charter·SIPOC</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Measure</strong><div class="itpe-step-detail"><strong>활동</strong><span>로그 신뢰성·Baseline 확인</span></div><div class="itpe-step-detail"><strong>산출</strong><span>측정계획·현수준</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Analyze</strong><div class="itpe-step-detail"><strong>활동</strong><span>장애·지연 원인 가설 검증</span></div><div class="itpe-step-detail"><strong>산출</strong><span>근본원인·영향도</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Improve</strong><div class="itpe-step-detail"><strong>활동</strong><span>대안 Pilot·위험 검증</span></div><div class="itpe-step-detail"><strong>산출</strong><span>개선안·Pilot 결과</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>Control</strong><div class="itpe-step-detail"><strong>활동</strong><span>SLI·Alert·Runbook·표준화</span></div><div class="itpe-step-detail"><strong>산출</strong><span>Control Plan</span></div></div>
</div>

## Ⅳ. Six Sigma·Lean 비교

| 기준 | Six Sigma | Lean |
|---|---|---|
| 초점 | 결함·변동 감소 | 낭비·대기·흐름 개선 |
| 접근 | 통계적 분석·DMAIC | Value Stream·Kaizen |
| 도구 | MSA·가설검정·DOE·SPC | VSM·Kanban·5S |
| 결합 | 복잡한 원인 검증 | 병목 제거·Flow 개선 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 도구 중심 과잉분석 | CTQ·Business Case 우선 | 문제 중심 개선 |
| 측정데이터 불신 | MSA·수집정의·결측 점검 | 분석 신뢰성 확보 |
| 상관관계를 원인으로 오인 | 가설검정·실험·Pilot | 인과 근거 강화 |
| 개선 후 회귀 | Control Plan·Owner·반응계획 | 성과 지속 |

## Ⅵ. 결론·기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]** DMAIC의 성패는 복잡한 통계 기법 구사가 아니라, 고객 관점의 CTQ를 시스템 로그 및 APM 지표와 정확히 연계(MSA)하고, 개선 이후 성과가 원래 상태로 회귀하지 않도록 차단하는 Control Plan의 제도화에 달려 있다.
> 
> **나라면** 현업 VOC와 결제/트랜잭션 지연을 CTQ로 정의하고, APM 분산 추적 로그로 MSA를 수행하겠음. 이후 개선안은 Canary 배포를 통해 통계적 가설 검증(A/B Test)을 진행하고, Control 단계에서는 Prometheus Alerting Rule 및 자동 복구 Runbook과 연동해 모니터링을 무인 자동화하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 프로세스 품질 개선 착수 시 단기 공정능력지수 $C_p \ge 2.0$, $C_{pk} \ge 1.5$ 달성 여부 및 DPMO 3.4 수준 목표 타당성 검토
- **대응 방안**: Lean의 낭비 제거(Lead-time 단축)와 6 Sigma의 변동 제거(Defect 최소화)를 결합한 Lean Six Sigma 체계 구축
- **검증 체계**: 통계적 공정관리(SPC) X-bar 관리도를 통한 이상 원인 조기 감지 및 분기별 MSA 재검증
- **기대 효과**: 대고객 트랜잭션 오류율 99.999% 무결성 유지, SLA 위반 패널티 제로화 및 연간 재작업 품질비용 40% 이상 절감

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 서비스 DMAIC 통제 폐루프">
  <div class="itpe-flow-node"><strong>CTQ Baseline</strong><div class="itpe-step-detail"><strong>증거</strong><span>지연·오류·가용성</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>원인 검증·Pilot</strong><div class="itpe-step-detail"><strong>판정</strong><span>효과·위험·비용</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>운영 통제</strong><div class="itpe-step-detail"><strong>실행</strong><span>SLI·Alert·Runbook</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>Control Review</strong><div class="itpe-step-detail"><strong>환류</strong><span>이탈·재발·다음 개선</span></div></div>
</div>

## 1교시 10점 답안 발췌

- **정의**: 고객 요구에 미달하는 기존 프로세스의 결함·변동을 데이터로 분석·개선·통제하는 방법론
- **목적**: CTQ 개선·변동 감소·개선성과 지속

| 단계 | 핵심 |
|---|---|
| D·M | 문제·CTQ 정의, 측정 신뢰성·Baseline |
| A·I | 근본원인 검증, 대안·Pilot |
| C | SPC·Control Plan·표준화 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [ASQ, DMAIC Process](https://asq.org/quality-resources/dmaic)
- [ASQ, Six Sigma](https://asq.org/quality-resources/six-sigma)

## 학습 체크

- [ ] Ⅰ: Six Sigma·DMAIC의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: DMAIC 단계별 활동·도구·산출을 연결할 수 있는가?
- [ ] Ⅲ: IT 서비스에 DMAIC를 적용할 수 있는가?
- [ ] Ⅳ: Six Sigma와 Lean의 초점·도구를 비교할 수 있는가?
- [ ] Ⅴ: 과잉분석·측정오류·인과오인·회귀의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: SLI·Alert·Runbook 기반 Control 폐루프를 그릴 수 있는가?

## 연결 토픽

- 이전: [110. Programmable Money·AI Agent 결제](./110_programmable_money_ai_agents.md)
- 관련: [106. 품질비용](./106_cost_of_quality_coq.md) · [113. SW 비용 산정](./113_software_cost_estimation.md)
- 다음: [112. CCPM·TOC](./112_critical_chain_toc.md)

