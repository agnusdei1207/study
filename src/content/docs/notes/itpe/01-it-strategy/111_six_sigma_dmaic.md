---
title: "Six Sigma DMAIC"
author: "OpenAI Codex"
date: "2026-09-22T11:25:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
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

Six Sigma의 3.4 DPMO는 장기 공정 이동을 가정한 대표적 품질수준이며, 모든 IT 서비스에 일률 적용하는 의무 기준은 아님.

## Ⅱ. DMAIC 단계별 활동·산출

| 단계 | 활동 | 주요 도구 | 산출 |
|---|---|---|---|
| Define | 문제·고객·범위·목표 정의 | VOC·CTQ·SIPOC | Project Charter |
| Measure | 측정체계 검증·Baseline 측정 | MSA·DPMO·Process Capability | 측정계획·현수준 |
| Analyze | 근본원인 검증 | Pareto·가설검정·회귀 | Vital Few 원인 |
| Improve | 대안 설계·Pilot 검증 | DOE·FMEA·Pilot | 개선안·검증결과 |
| Control | 표준화·감시·대응 | SPC·Control Plan·SOP | 관리계획·표준 |

## Ⅲ. 적용 절차

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

> **[핵심 통찰]** DMAIC의 핵심은 복잡한 통계가 아니라 측정 가능한 문제와 검증된 원인을 연결하고 개선 후 회귀를 막는 것임.

> **나라면** 서비스 로그로 CTQ Baseline을 만들고, 상위 원인만 Pilot으로 검증한 뒤 SLI·Alert·Runbook을 Control Plan에 연결하겠음.

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

- 이전: [110. Programmable Money·AI Agent 결제](./110_programmable_money_ai_agents/)
- 관련: [106. 품질비용](./106_cost_of_quality_coq/) · [113. SW 비용 산정](./113_software_cost_estimation/)
- 다음: [112. CCPM·TOC](./112_critical_chain_toc/)
