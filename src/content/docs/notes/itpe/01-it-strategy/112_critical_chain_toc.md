---
title: "CCPM·TOC"
author: "OpenAI Codex"
date: "2026-09-22T11:45:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 일정과 자원관리를 거쳐 CCPM으로 이어지는 위치">
  <span>IT 전략·관리</span><span>일정·자원관리</span><strong>CCPM·TOC</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 작업 의존성과 자원 제약을 함께 반영한 Critical Chain 중심 일정관리
- **메커니즘**: 개별 안전여유 통합 → PB·FB 배치 → RB 알림 → Buffer 상태 통제
- **목적**: 다중작업·학생증후군·파킨슨 법칙으로 인한 일정지연 완화

<div class="itpe-svg-map">
<svg viewBox="0 0 780 520" role="img" aria-label="Critical Chain과 프로젝트 피딩 자원 버퍼 배치">
  <defs><marker id="ccpm-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link"></path></marker></defs>
  <rect x="35" y="185" width="105" height="70" rx="12" class="itpe-svg-node"></rect><text x="87" y="228" text-anchor="middle" class="itpe-svg-title">A</text>
  <rect x="200" y="185" width="105" height="70" rx="12" class="itpe-svg-node"></rect><text x="252" y="228" text-anchor="middle" class="itpe-svg-title">B</text>
  <rect x="365" y="185" width="105" height="70" rx="12" class="itpe-svg-node is-current"></rect><text x="417" y="215" text-anchor="middle" class="itpe-svg-title">C</text><text x="417" y="240" text-anchor="middle" class="itpe-svg-sub">RB</text>
  <rect x="530" y="185" width="105" height="70" rx="12" class="itpe-svg-node"></rect><text x="582" y="228" text-anchor="middle" class="itpe-svg-title">D</text>
  <rect x="665" y="185" width="90" height="70" rx="12" class="itpe-svg-node is-current"></rect><text x="710" y="215" text-anchor="middle" class="itpe-svg-title">PB</text><text x="710" y="240" text-anchor="middle" class="itpe-svg-sub">납기 보호</text>
  <rect x="200" y="365" width="105" height="70" rx="12" class="itpe-svg-node"></rect><text x="252" y="408" text-anchor="middle" class="itpe-svg-title">E</text>
  <rect x="365" y="365" width="105" height="70" rx="12" class="itpe-svg-node"></rect><text x="417" y="395" text-anchor="middle" class="itpe-svg-title">FB</text><text x="417" y="420" text-anchor="middle" class="itpe-svg-sub">합류 보호</text>
  <path d="M140 220 L200 220" class="itpe-svg-link" marker-end="url(#ccpm-arrow)"></path>
  <path d="M305 220 L365 220" class="itpe-svg-link" marker-end="url(#ccpm-arrow)"></path>
  <path d="M470 220 L530 220" class="itpe-svg-link" marker-end="url(#ccpm-arrow)"></path>
  <path d="M635 220 L665 220" class="itpe-svg-link" marker-end="url(#ccpm-arrow)"></path>
  <path d="M305 400 L365 400" class="itpe-svg-link" marker-end="url(#ccpm-arrow)"></path>
  <path d="M417 365 L417 255" class="itpe-svg-link" marker-end="url(#ccpm-arrow)"></path>
  <text x="335" y="145" class="itpe-svg-label">Critical Chain: 작업·자원 의존성</text>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **TOC(Theory of Constraints)**: 시스템 성과를 제한하는 제약을 식별·활용·개선하는 접근
- **CCPM(Critical Chain Project Management)**: 작업·자원 의존성과 통합 Buffer로 일정을 관리하는 기법
- **PB(Project Buffer)**: Critical Chain 끝에서 프로젝트 납기를 보호하는 시간 Buffer
- **FB(Feeding Buffer)**: 비임계 Chain의 지연이 Critical Chain에 전파되지 않게 보호하는 Buffer
- **RB(Resource Buffer)**: Critical Chain 작업의 핵심자원을 제때 준비시키는 알림
- **Fever Chart**: Chain 진척과 Buffer 소진의 관계를 표시한 관리도
- **CPM(Critical Path Method)**: 작업 선후행 관계에서 프로젝트 기간을 결정하는 경로를 분석하는 기법
- **WIP(Work in Progress)**: 동시에 진행 중인 작업량
- **EVM(Earned Value Management)**: 범위·일정·원가 성과를 통합 측정하는 기법

</details>

## 예상문제

> **(미출제 예상·25점)** CCPM의 개념과 Critical Chain 도출·Buffer 관리방식을 설명하고, CPM과 비교하여 문제점·대응책을 제시하시오.

## Ⅰ. CCPM 개요

> 작업별 납기보다 전체 Chain의 흐름과 보호 Buffer를 관리해 프로젝트 납기를 통제함

- **정의**: TOC 기반으로 작업 의존성과 자원 제약을 반영한 Critical Chain을 도출하고 통합 Buffer로 일정을 관리하는 기법
- **목적**: 자원 경합·다중작업·분산 안전여유로 인한 전체 일정지연 완화

## Ⅱ. Critical Chain·Buffer 체계

| 요소 | 위치 | 역할 |
|---|---|---|
| Critical Chain | 작업·자원 제약 반영 핵심 Chain | 프로젝트 완료일 결정 |
| PB | Critical Chain 끝 | 전체 납기 보호 |
| FB | 비임계 Chain 합류점 | 합류 지연 전파 차단 |
| RB | 핵심자원 투입 전 | 자원 준비 알림 |

Buffer 크기는 작업 불확실성·추정방식·위험 데이터를 반영해 정하며 일률적인 절반 규칙을 강제하지 않음.

## Ⅲ. CCPM 적용 절차

<div class="itpe-pipeline is-vertical" role="img" aria-label="CCPM 일정 수립과 통제 절차">
  <div class="itpe-flow-node"><strong>① 작업·자원 분석</strong><div class="itpe-step-detail"><strong>활동</strong><span>선후행·자원가용성·경합 식별</span></div><div class="itpe-step-detail"><strong>산출</strong><span>자원제약 Network</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>② Critical Chain 도출</strong><div class="itpe-step-detail"><strong>활동</strong><span>자원 Leveling·다중작업 제거</span></div><div class="itpe-step-detail"><strong>산출</strong><span>Critical Chain 일정</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>③ Buffer 설계</strong><div class="itpe-step-detail"><strong>활동</strong><span>PB·FB 크기·RB 알림 정의</span></div><div class="itpe-step-detail"><strong>산출</strong><span>Buffer Plan</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>④ Buffer 통제</strong><div class="itpe-step-detail"><strong>판정</strong><span>진척 대비 소진 추세·예외 원인</span></div><div class="itpe-step-detail"><strong>산출</strong><span>Fever Chart·조치계획</span></div></div>
</div>

## Ⅳ. CPM·CCPM 비교

| 기준 | CPM | CCPM |
|---|---|---|
| 제약 | 작업 선후행 중심 | 작업·자원 의존성 |
| 여유 | 작업별 Float | PB·FB 통합 Buffer |
| 진척 | 작업 일정·Critical Path | Chain 진척·Buffer 소진 |
| 강점 | 논리적 일정 분석 | 자원경합·행동요인 통제 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 공격적 추정 강요 | 추정 근거·범위·위험 합의 | 일정 신뢰 확보 |
| Buffer를 예비시간으로 소진 | 변경승인·소진원인 기록 | Buffer 목적 보호 |
| 다중 프로젝트 자원경합 | Portfolio 우선순위·WIP 제한 | Multitasking 감소 |
| 신호등 임계치 기계 적용 | 추세·잔여위험·복구계획 병행 | 오판 방지 |

## Ⅵ. 결론·기술사적 제언

> **[핵심 통찰]** CCPM의 성패는 일정을 강제로 줄이는 데 있지 않고 제약자원이 한 번에 가장 중요한 작업을 끝내도록 흐름을 보호하는 데 있음.

> **나라면** 남은 작업시간과 Buffer 소진 추세를 함께 보고, 적색 여부가 아니라 제약자원·복구계획·잔여위험을 근거로 자원 재배치를 결정하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="CCPM Buffer 상태 기반 의사결정">
  <div class="itpe-flow-node"><strong>Chain 진척·Buffer 소진</strong><div class="itpe-step-detail"><strong>증거</strong><span>잔여시간·소진추세</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>제약·원인 분석</strong><div class="itpe-step-detail"><strong>판정</strong><span>자원경합·변경·재작업</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>조치 분기</strong><div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>회복 가능</strong><span>현 계획 유지·감시</span></div><div class="itpe-flow-branch"><strong>회복 곤란</strong><span>자원집중·범위·순서 조정</span></div></div></div>
</div>

## 1교시 10점 답안 발췌

- **정의**: 작업 의존성과 자원 제약을 반영한 Critical Chain을 도출하고 통합 Buffer로 일정을 관리하는 기법
- **목적**: 자원경합·다중작업·분산 안전여유로 인한 전체 일정지연 완화

| Buffer | 역할 |
|---|---|
| PB | Critical Chain 끝에서 납기 보호 |
| FB | 비임계 Chain 합류 지연 차단 |
| RB | 핵심자원 투입 준비 알림 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- Eliyahu M. Goldratt, *Critical Chain*
- [PMI, Critical Chain Method](https://www.pmi.org/learning/library/critical-chain-project-management-7986)

## 학습 체크

- [ ] Ⅰ: CCPM 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: Critical Chain과 PB·FB·RB의 위치·역할을 그릴 수 있는가?
- [ ] Ⅲ: 작업·자원 분석부터 Buffer 통제까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅳ: CPM과 CCPM의 제약·여유·진척 기준을 비교할 수 있는가?
- [ ] Ⅴ: 추정강요·Buffer 오용·자원경합·임계치 오판의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: Buffer 상태에 따른 조치 분기를 제시할 수 있는가?

## 연결 토픽

- 이전: [111. Six Sigma DMAIC](./111_six_sigma_dmaic/)
- 관련: [081. CPM](./081_cpm/) · [032. EVM](./032_evm/)
- 다음: [113. SW 비용 산정](./113_software_cost_estimation/)
