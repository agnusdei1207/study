---
title: "시스템 운영·유지보수 감리"
author: "OpenAI Codex"
date: "2026-09-22T03:15:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "GPT-5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략 관리에서 정보시스템 감리와 운영 품질을 거쳐 시스템 운영 유지보수 감리로 이어지는 지식 위치">
  <span>IT 전략·관리</span><span>정보시스템 감리·운영 품질</span><strong>운영·유지보수 감리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 독립된 제3자가 운영·유지보수의 효율성·안전성·계약이행을 증적으로 점검
- 운영: 서비스·장애·성능·용량·백업·DR·보안·사용자 지원
- 유지보수: SR·변경·결함·시험·배포·형상·계약범위

<div class="itpe-svg-map">
<svg viewBox="0 0 760 560" role="img" aria-label="운영 감리와 유지보수 감리가 증적 검증과 개선조치로 연결되는 구조">
  <defs><marker id="arrow-operation-audit" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <rect class="itpe-svg-node" x="55" y="30" width="290" height="126" rx="14" />
  <text class="itpe-svg-title" x="200" y="65" text-anchor="middle">운영 감리</text>
  <text class="itpe-svg-sub" x="200" y="94" text-anchor="middle">SLA · 장애 · 성능 · 용량</text>
  <text class="itpe-svg-sub" x="200" y="122" text-anchor="middle">백업 · DR · 보안 · 지원</text>
  <rect class="itpe-svg-node" x="415" y="30" width="290" height="126" rx="14" />
  <text class="itpe-svg-title" x="560" y="65" text-anchor="middle">유지보수 감리</text>
  <text class="itpe-svg-sub" x="560" y="94" text-anchor="middle">SR · 변경 · 결함 · 시험</text>
  <text class="itpe-svg-sub" x="560" y="122" text-anchor="middle">배포 · 형상 · 계약범위</text>
  <path class="itpe-svg-link" d="M200 156 V215 H330" marker-end="url(#arrow-operation-audit)" />
  <path class="itpe-svg-link" d="M560 156 V215 H430" marker-end="url(#arrow-operation-audit)" />
  <rect class="itpe-svg-node is-current" x="190" y="226" width="380" height="108" rx="14" />
  <text class="itpe-svg-title" x="380" y="261" text-anchor="middle">독립적 증적 검증</text>
  <text class="itpe-svg-sub" x="380" y="290" text-anchor="middle">문서 · 설정 · Log · Ticket · Interview</text>
  <text class="itpe-svg-sub" x="380" y="316" text-anchor="middle">표본 · 재수행 · 교차대조</text>
  <path class="itpe-svg-link" d="M380 334 V390" marker-end="url(#arrow-operation-audit)" />
  <rect class="itpe-svg-node" x="190" y="400" width="380" height="108" rx="14" />
  <text class="itpe-svg-title" x="380" y="435" text-anchor="middle">발견사항·개선조치</text>
  <text class="itpe-svg-sub" x="380" y="464" text-anchor="middle">영향도 · 시급성 · 원인 · 권고</text>
  <text class="itpe-svg-sub" x="380" y="490" text-anchor="middle">조치계획 · 이행확인 · 잔여위험</text>
</svg>
</div>

<details>
<summary>핵심 용어</summary>

- **SLA(Service Level Agreement)**: 서비스 수준과 측정·보고·책임을 합의한 문서
- **ITSM(IT Service Management)**: IT 서비스를 계획·제공·운영·개선하는 관리체계
- **SR(Service Request)**: 사용자 또는 운영자가 공식 절차로 등록한 서비스 요청
- **RTO(Recovery Time Objective)**: 중단 후 서비스를 복구해야 하는 목표시간
- **RPO(Recovery Point Objective)**: 복구 시 허용 가능한 데이터 손실 시점
- **CAATs(Computer-Assisted Audit Techniques)**: 데이터·Log 분석 등에 사용하는 컴퓨터 기반 감사기법

</details>

## 예상문제

> 시스템 운영 감리와 유지보수 감리의 개념·점검영역을 비교하고, 증적 기반 감리절차 및 문제점·대응책을 설명하시오. **(미출제 예상·25점)**

## Ⅰ. 가동 후 효율성·안전성·계약이행을 검증하는 독립 활동

> 운영·유지보수 감리는 체크리스트 확인이 아니라 통제가 실제 작동하고 결과가 추적되는지 증적으로 판단하는 활동임.

- 정의: 독립된 제3자가 정보시스템 운영·유지보수의 효율성·안전성·계약이행을 종합 점검하고 개선을 권고하는 활동
- 목적: **서비스 연속성·운영통제 실효성·변경 품질·계약 투명성** 확보

## Ⅱ. 운영 감리와 유지보수 감리 비교

| 기준 | 운영 감리 | 유지보수 감리 |
|---|---|---|
| 대상 | 운영기획·관제·지원·인프라 | 기능변경·추가·보완·폐기 |
| 초점 | 가용성·성능·보안·연속성 | 요구·변경·결함·형상·계약 |
| 증적 | SLA·Log·Ticket·백업·훈련 | SR·승인·Commit·시험·배포 |
| 시험 | 표본복원·장애기록 재수행 | 변경 추적·회귀시험·형상감사 |
| 결과 | 운영통제 개선 | 변경품질·과업이행 개선 |

## Ⅲ. 핵심 점검영역

| 영역 | 점검사항 | 증적 |
|---|---|---|
| 서비스 | SLA·Incident·Problem·사용자지원 | SLA 보고·Ticket·RCA |
| 성능·용량 | 병목·추세·임계치·증설 | APM·용량계획 |
| 연속성 | 백업·복구·DR·RTO·RPO | 복원기록·훈련결과 |
| 보안 | 계정·변경·취약점·Log | 권한목록·패치·감사로그 |
| 유지보수 | SR·영향분석·시험·배포·형상 | 승인·Commit·Test Result |
| 계약 | 범위·인력·성과·검수·변경 | 계약·작업내역·검수결과 |

## Ⅳ. 증적 기반 감리절차

<div class="itpe-pipeline is-vertical" role="img" aria-label="운영 유지보수 감리의 계획부터 이행확인까지 절차">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>① 계획</strong><strong>활동</strong><span>범위·위험·기준·표본·일정 확정</span><strong>산출</strong><span>감리계획서 · 점검표</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>② 증적수집</strong><strong>활동</strong><span>문서·설정·Log·Ticket·Interview 확보</span><strong>산출</strong><span>Evidence Inventory</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>③ 검증</strong><strong>활동</strong><span>표본검사·재수행·교차대조·원인분석</span><strong>산출</strong><span>발견사항 · 근거</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>④ 평가·보고</strong><strong>활동</strong><span>영향도·시급성·원인·권고 합의</span><strong>산출</strong><span>감리보고서 · 조치계획</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>⑤ 이행확인</strong><strong>활동</strong><span>시정조치·재시험·잔여위험 확인</span><strong>산출</strong><span>조치확인서</span></div></div>
</div>

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 문서와 실제 운영 불일치 | Log·설정·Ticket 교차대조 | 증적 신뢰성 향상 |
| 백업 성공만 확인 | 격리환경 표본복원·복구시간 측정 | 복구 가능성 확인 |
| SLA 평균값의 장애 은폐 | 구간·서비스별 SLI 재계산 | 품질 왜곡 감소 |
| 구두 변경·무상과업 | SR-승인-Commit-배포 추적 | 범위·책임 명확화 |
| 운영계 시험 위험 | 사전 승인·격리·Rollback·관찰자 | 서비스 영향 통제 |

## Ⅵ. Evidence Traceability 기반 제언

`[핵심 통찰]` 운영 감리의 품질은 자료량이 아니라 하나의 장애·변경 사건이 승인부터 조치·시험·종결까지 끊김 없이 추적되는가에 달려 있음.

`나라면` 위험기반 표본을 선정해 SLA 보고값을 원시 Log로 재계산하고, 백업은 격리환경에서 복원하며, SR은 Commit·Test·배포기록까지 연결해 통제의 실효성을 판정하겠음.

<div class="itpe-svg-map">
<svg viewBox="0 0 760 470" role="img" aria-label="운영 유지보수 감리 증적 추적 구조">
  <defs><marker id="arrow-audit-trace" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <rect class="itpe-svg-node" x="190" y="25" width="380" height="72" rx="14" />
  <text class="itpe-svg-title" x="380" y="57" text-anchor="middle">Event·SR</text><text class="itpe-svg-sub" x="380" y="82" text-anchor="middle">장애 · 요청 · 변경 필요</text>
  <path class="itpe-svg-link" d="M380 97 V145" marker-end="url(#arrow-audit-trace)" />
  <rect class="itpe-svg-node" x="190" y="153" width="380" height="72" rx="14" />
  <text class="itpe-svg-title" x="380" y="185" text-anchor="middle">승인·실행</text><text class="itpe-svg-sub" x="380" y="210" text-anchor="middle">영향분석 · 작업 · Commit</text>
  <path class="itpe-svg-link" d="M380 225 V273" marker-end="url(#arrow-audit-trace)" />
  <rect class="itpe-svg-node is-current" x="190" y="281" width="380" height="72" rx="14" />
  <text class="itpe-svg-title" x="380" y="313" text-anchor="middle">검증·배포</text><text class="itpe-svg-sub" x="380" y="338" text-anchor="middle">Test Result · 형상 · 배포기록</text>
  <path class="itpe-svg-link" d="M380 353 V401" marker-end="url(#arrow-audit-trace)" />
  <rect class="itpe-svg-node" x="190" y="409" width="380" height="48" rx="14" />
  <text class="itpe-svg-title" x="380" y="440" text-anchor="middle">성과확인·종결·감사추적</text>
</svg>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 독립된 제3자가 정보시스템 운영·유지보수의 효율성·안전성·계약이행을 점검하고 개선을 권고하는 활동
- 목적: **서비스 연속성·통제 실효성·변경 품질·계약 투명성** 확보

### 2. 점검영역

| 운영 | 유지보수 |
|---|---|
| SLA·장애·성능·용량 | SR·영향분석·승인 |
| 백업·DR·보안·지원 | 변경·시험·배포·형상 |

### 3. 핵심 통제

- **Evidence Cross-check**: 보고서와 원시 Log·설정·Ticket 교차검증
- **End-to-end Traceability**: SR → 승인 → Commit → Test → 배포 → 종결

## 출제 이력과 검증 출처

- 제137회 정보관리기술사: 시스템 운영 및 유지보수 감리 관련 문제
- [국가법령정보센터, 정보시스템 감리기준](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000243290)
- [국가법령정보센터, 정보시스템 구축·운영 지침](https://www.law.go.kr/LSW/admRulInfoP.do?admRulSeq=2000000063674)

## 학습 체크

- [ ] Ⅰ: 운영·유지보수 감리의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 운영 감리와 유지보수 감리를 대상·초점·증적으로 비교할 수 있는가?
- [ ] Ⅲ: 서비스·성능·연속성·보안·유지보수·계약 점검사항을 제시할 수 있는가?
- [ ] Ⅳ: 계획부터 이행확인까지 활동과 산출물을 연결할 수 있는가?
- [ ] Ⅴ: 문서불일치·백업·SLA·구두변경 위험의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: Evidence Traceability를 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [기술 주권](./058_technology_sovereignty.md)
- 연관 토픽: [정보시스템 감리](./008_it_audit.md), [SLA](./006_sla.md), [DR](./042_disaster_recovery_system.md)
- 다음 토픽: [AI 에너지 인프라](./060_ai_energy_infrastructure.md)
