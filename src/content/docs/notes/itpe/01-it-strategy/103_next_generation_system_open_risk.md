---
title: "차세대 시스템 오픈 리스크"
author: "Antigravity"
date: "2026-09-22T09:45:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 전환관리를 거쳐 차세대 시스템 오픈 리스크로 이어지는 위치">
  <span>IT 전략·관리</span><span>전환관리·사업위험</span><strong>오픈 리스크</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 신·구 시스템 절체 중 데이터·업무·연계·성능 중단 위험 통제
- **메커니즘**: 리허설 → Cut-over → Go/No-Go → 안정화
- **핵심**: 롤백 가능 시점 전에 증적 기반으로 계속·중단을 판정

<div class="itpe-pipeline is-vertical" role="img" aria-label="차세대 시스템 오픈 리스크 통제 흐름">
  <div class="itpe-flow-node"><strong>리허설</strong><div class="itpe-step-detail"><strong>검증</strong><span>절차·시간·데이터·복구</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Cut-over</strong><div class="itpe-step-detail"><strong>실행</strong><span>업무중단·백업·이행·절체</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>Go/No-Go</strong><div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>Go</strong><span>신규 시스템 가동</span></div><div class="itpe-flow-branch"><strong>No-Go</strong><span>Rollback 실행</span></div></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>안정화</strong><div class="itpe-step-detail"><strong>통제</strong><span>모니터링·장애·현업 지원</span></div></div>
</div>

<details>
<summary>약어·전문용어</summary>

- **Cut-over**: 구 시스템에서 신 시스템으로 업무·데이터·연계를 전환하는 절차
- **Dry Run**: 본 전환과 유사한 조건에서 수행하는 모의이행
- **Go/No-Go**: 가동 지속 또는 롤백을 결정하는 의사결정 Gate
- **Rollback**: 전환 실패 시 검증된 이전 상태로 복구하는 활동
- **ETL(Extract, Transform, Load)**: 데이터를 추출·변환·적재하는 처리
- **BCP(Business Continuity Plan)**: 중단 상황에서도 핵심 업무를 지속·복구하기 위한 계획

</details>

## 예상문제

> **(미출제 예상·25점)** 차세대 시스템 Cut-over의 주요 오픈 리스크를 설명하고, 단계별 통제와 Go/No-Go·Rollback 의사결정 방안을 제시하시오.

## Ⅰ. 차세대 시스템 오픈 리스크 개요

> Cut-over는 기술 배포가 아니라 업무·데이터·조직을 동시에 전환하는 고위험 변경임

- **정의**: 차세대 시스템 가동 과정에서 업무중단·데이터 오류·성능저하·연계장애를 예방·대응하는 전환 위험관리
- **목적**: 전환 무결성·서비스 연속성·복구 가능성 확보

## Ⅱ. Cut-over 단계별 통제 및 타임라인 아키텍처

> 업무 동결부터 롤백 한계시각(Point of No Return)과 종합 판정까지 시간 역산 타임라인을 통제함.

### 1. Cut-over 런북 타임라인 및 롤백 한계점(Point of No Return) 구조

```xml
<svg-diagram>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="220" style="background:var(--sl-color-bg-sidebar);border:1px solid var(--sl-color-hairline);border-radius:8px;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--sl-color-text-accent)"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#ef4444"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="15" y="24" fill="var(--sl-color-text)" font-size="13" font-weight="bold">차세대 시스템 Cut-over 타임라인 및 Go/No-Go 롤백 한계선</text>

  <!-- Timeline Base Bar -->
  <g transform="translate(15, 55)">
    <!-- Phase 1: Freeze & Backup -->
    <rect x="0" y="0" width="100" height="45" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="4"/>
    <text x="50" y="18" fill="var(--sl-color-text)" font-size="9" font-weight="bold" text-anchor="middle">① 업무동결·백업</text>
    <text x="50" y="32" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">00:00 ~ 02:00 (2h)</text>

    <!-- Phase 2: ETL Migration & Verification -->
    <rect x="105" y="0" width="125" height="45" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="4"/>
    <text x="167" y="18" fill="var(--sl-color-text)" font-size="9" font-weight="bold" text-anchor="middle">② 데이터 이행·대사</text>
    <text x="167" y="32" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">02:00 ~ 04:30 (2.5h)</text>

    <!-- Phase 3: Interface & Smoke Test -->
    <rect x="235" y="0" width="100" height="45" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="4"/>
    <text x="285" y="18" fill="var(--sl-color-text)" font-size="9" font-weight="bold" text-anchor="middle">③ 연계·스모크테스트</text>
    <text x="285" y="32" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">04:30 ~ 05:30 (1h)</text>

    <!-- Point of No Return Line -->
    <line x1="340" y1="-10" x2="340" y2="135" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3"/>
    <text x="340" y="-14" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">Point of No Return (05:30)</text>

    <!-- Phase 4: Decision & Open -->
    <rect x="345" y="0" width="145" height="45" fill="var(--sl-color-bg)" stroke="var(--sl-color-text-accent)" stroke-width="1.8" rx="4"/>
    <text x="417" y="18" fill="var(--sl-color-text-accent)" font-size="9" font-weight="bold" text-anchor="middle">④ Go/No-Go 판정</text>
    <text x="417" y="32" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">05:30 ~ 06:00 (30m)</text>
  </g>

  <!-- Branching: Go vs No-Go -->
  <!-- Go Path -->
  <g transform="translate(365, 120)">
    <path d="M 0 0 L 25 0" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#arrow)"/>
    <rect x="30" y="-18" width="105" height="36" fill="var(--sl-color-bg)" stroke="#10b981" stroke-width="1.5" rx="4"/>
    <text x="82" y="-2" fill="#10b981" font-size="9" font-weight="bold" text-anchor="middle">✅ GO 판정</text>
    <text x="82" y="12" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">09:00 대고객 오픈</text>
  </g>

  <!-- No-Go Path -->
  <g transform="translate(365, 175)">
    <path d="M 0 -15 L 25 0" fill="none" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow-red)"/>
    <rect x="30" y="-18" width="105" height="36" fill="var(--sl-color-bg)" stroke="#ef4444" stroke-width="1.5" rx="4"/>
    <text x="82" y="-2" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">⛔ NO-GO (Rollback)</text>
    <text x="82" y="12" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">구 시스템 원복 (09:00 이전)</text>
  </g>

  <!-- Note box on bottom left -->
  <g transform="translate(15, 135)">
    <rect x="0" y="0" width="315" height="55" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" rx="4"/>
    <text x="10" y="18" fill="var(--sl-color-text-accent)" font-size="9" font-weight="bold">핵심 통제 원칙: 롤백 소요시간 역산</text>
    <text x="10" y="32" fill="var(--sl-color-text-muted)" font-size="8">• 구 시스템 복구 소요시간(약 3.5시간)을 09:00 영업개시에서 역산</text>
    <text x="10" y="46" fill="#ef4444" font-size="8" font-weight="bold">• 05:30 초과 시 신규 시스템 가동 중단 불가 → 강제 롤백 의결</text>
  </g>
</svg>
</svg-diagram>
```

### 2. 단계별 통제 활동 및 산출물

| 단계 | 활동 | 산출 |
|---|---|---|
| 계획 | 범위·순서·의존성·책임 정의 | Cut-over 계획·RACI |
| 리허설 | 모의이행·대사·성능·복구 검증 | 리허설 결과·보완목록 |
| 실행 | 동결·백업·이행·절체·Smoke Test | 실행로그·대사결과 |
| 판정 | Go/No-Go·Rollback 결정 | 판정서·복구 승인 |
| 안정화 | 모니터링·장애·현업지원 | 상황보고·종료기준 |

## Ⅲ. 핵심 리스크·통제

| 위험 | 대책 | 효과 |
|---|---|---|
| 데이터 누락·불일치 | 건수·금액·참조무결성 대사 | 이행 무결성 확인 |
| 성능 저하 | 업무량 기반 부하·용량 시험 | 병목 사전 제거 |
| 대내외 연계 단절 | E2E(End-to-End) 합동 시험 | 인터페이스 연속성 확보 |
| 업무 절차 혼선 | 사용자 리허설·비상업무 절차 | 현업 대응력 확보 |
| 복구 실패 | 백업 복원·Rollback 리허설 | 복구 실행성 확보 |

## Ⅳ. Big-Bang vs Phased 전환 비교

| 기준 | Big-Bang | Phased |
|---|---|---|
| 전환 | 일괄 절체 | 업무·채널별 순차 절체 |
| 장점 | 이중운영·동기화 기간 최소화 | 영향 범위 분산 |
| 위험 | 실패 영향 집중 | 신·구 정합성·장기 이중운영 |
| 선택 | 강한 결합·단일 전환창 | 분리 가능한 도메인·점진 검증 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 일정 압박에 따른 강행 | 사전 승인된 판정기준·권한 | 의사결정 독립성 |
| 리허설과 운영환경 차이 | 운영 규모·순서·권한 재현 | 실행오차 축소 |
| 판정 증적 분산 | 통합 상황판·단일 승인기록 | 판단 근거 확보 |
| 롤백 시간 부족 | 역산 일정·중단시점 설정 | 복구 가능성 보호 |

## Ⅵ. 전환 통제 및 롤백 의사결정을 위한 기술사적 제언

> 성공적인 오픈은 장애가 없는 오픈이 아니라, 불확실성을 조기에 드러내고 되돌릴 수 있을 때 중단하는 오픈임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 현업 경영진과 사업단은 수백억 원의 예산과 일정이 걸린 상태에서 'No-Go(롤백)' 버튼을 누르는 것을 극도로 두려워함. 따라서 주관적 판단을 배제하기 위해 'Point of No Return(롤백 한계시각)'을 사전에 못 박고, 4대 대사(데이터 건수/금액, E2E 연계, 스모크 테스트, 부하 임계치) 미충족 시 자동으로 롤백이 발동되는 독립적 의사결정 헌장을 제정해야 함.
- 나라면: 업무 중요도별 Go/No-Go 기준과 Rollback 결정시점을 사전 승인하고, 데이터·성능·연계·현업 증적이 한 화면에 모인 경우에만 가동을 승인하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 4대 무결성 지표(데이터 대사율 100%, E2E 거래 성공률, 목표 TPS 달성, 현업 승인) 및 롤백 한계시각 도달 여부
- **대응 방안**: 업무 개시 시각 기준 롤백 소요시간 역산(Point of No Return), 3회 이상의 실전 Dry Run 모의훈련 실시
- **검증 체계**: 단일 런북(Runbook) 기반 분 단위 실시간 상황실 관제, PMO·감리·현업 공동 참여 Go/No-Go 서명제 운영
- **기대 효과**: 개통 첫날 대규모 전산 마비 사태 원천 차단, 대고객 서비스 연속성 및 금융/공공 신뢰도 유지

<div class="itpe-svg-map">
<svg viewBox="0 0 760 500" role="img" aria-label="Go No-Go와 Rollback 판정 구조">
  <rect x="245" y="25" width="270" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="62" text-anchor="middle" class="itpe-svg-title">판정 증적</text><text x="380" y="92" text-anchor="middle" class="itpe-svg-sub">데이터·성능·연계·업무</text>
  <rect x="245" y="180" width="270" height="90" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="380" y="217" text-anchor="middle" class="itpe-svg-title">Rollback 결정시점</text><text x="380" y="247" text-anchor="middle" class="itpe-svg-sub">복구 소요시간 역산</text>
  <rect x="70" y="350" width="240" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="190" y="387" text-anchor="middle" class="itpe-svg-title">Go</text><text x="190" y="417" text-anchor="middle" class="itpe-svg-sub">가동·안정화</text>
  <rect x="450" y="350" width="240" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="570" y="387" text-anchor="middle" class="itpe-svg-title">No-Go</text><text x="570" y="417" text-anchor="middle" class="itpe-svg-sub">Rollback·원인 보완</text>
  <path d="M380 115 L380 180 M315 270 L190 350 M445 270 L570 350" class="itpe-svg-link"></path>
  <text x="225" y="315" class="itpe-svg-label">기준 충족</text><text x="505" y="315" class="itpe-svg-label">미충족·시간 도달</text>
</svg>
</div>

## 1교시 10점 답안 발췌

- **정의**: 차세대 시스템 가동 과정에서 업무중단·데이터 오류·성능저하·연계장애를 예방·대응하는 전환 위험관리
- **목적**: 전환 무결성·서비스 연속성·복구 가능성 확보

| 구간 | 통제 |
|---|---|
| 오픈 전 | Dry Run·대사·부하·복구 시험 |
| 오픈 중 | 실행로그·Go/No-Go·Rollback |
| 오픈 후 | 상황실·모니터링·종료기준 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [NIST SP 800-34 Rev.1, Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/final)
- [AWS Prescriptive Guidance, Cutover runbook](https://docs.aws.amazon.com/prescriptive-guidance/latest/cutover-runbook/)

## 학습 체크

- [ ] Ⅰ: 오픈 리스크의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 계획부터 안정화까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ: 데이터·성능·연계·현업·복구 위험의 통제를 제시할 수 있는가?
- [ ] Ⅳ: Big-Bang·Phased 선택기준을 비교할 수 있는가?
- [ ] Ⅴ: 일정 압박·환경 차이·롤백 시간 부족의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: 증적 기반 Go/No-Go 판정 구조를 그릴 수 있는가?

## 연결 토픽

- 이전 토픽: [지능정보기술 감리 실무 가이드](./102_intelligent_information_technology_audit_guide.md)
- 연관 토픽: [부정적 위험 대응](./040_negative_risk_response_strategy.md), [클라우드 전환사업 감리](./104_cloud_migration_project_audit.md)
- 다음 토픽: [클라우드 전환사업 감리](./104_cloud_migration_project_audit.md)

