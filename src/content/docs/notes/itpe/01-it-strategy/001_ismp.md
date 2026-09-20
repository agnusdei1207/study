---
title: "ISMP"
author: "Codex"
date: "2026-09-20T19:27:50+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5 Codex"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 정보화 기획·발주를 거쳐 ISMP로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>정보화 기획·발주</span>
  <strong>ISMP</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **ISMP(Information System Master Plan)**는 **ISP(Information Strategy Planning)** 선정 시스템을 조달 가능한 **Baseline**으로 구체화
- 메커니즘: 요건 → 아키텍처 → 규모·예산 → **RFP(Request for Proposal)**를 **RTM(Requirements Traceability Matrix)**으로 연결
- 산출: 요건명세 · 목표 아키텍처 · **FP(Function Point)** · 예산 · RFP

<div class="itpe-flow-map" role="img" aria-label="경영·정책에서 ISP와 ISMP를 거쳐 조달·구축으로 이어지는 흐름">
  <div class="itpe-flow-node"><strong>경영·정책</strong></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>ISP</strong>
    <div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>산출</strong><span>정보화 과제 · 구축 대상</span></div></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>ISMP</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>절차</strong><span>착수 → 방향성 → 요건 → 구조 → 이행</span></div>
      <div class="itpe-flow-branch"><strong>통제</strong><span><span class="itpe-keyword"><strong>RTM</strong></span> 기반 양방향 추적</span></div>
      <div class="itpe-flow-branch"><strong>산출</strong><span>아키텍처 · <span class="itpe-keyword"><strong>FP</strong></span> · 예산 · <span class="itpe-keyword"><strong>RFP</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>조달·구축</strong>
    <div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>입력</strong><span>확정된 발주 Baseline</span></div></div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **ISMP(Information System Master Plan)**: 특정 시스템의 요건·구조·예산을 발주 가능한 수준으로 구체화
- **ISP(Information Strategy Planning)**: 조직의 정보화 방향과 투자 과제를 선정하는 상위 계획
- **IT(Information Technology)**: 업무 목표를 정보시스템으로 구현하는 기술 영역
- **Baseline**: 승인된 범위·요건·비용의 변경 통제 기준
- **RTM(Requirements Traceability Matrix)**: 요건과 설계·비용·계약 산출물의 양방향 연결을 검증
- **아키텍처**: 요건을 응용·데이터·기술 구성과 관계로 배치한 목표 구조
- **요건명세**: 기능·데이터·비기능 요구를 설계·검수 가능한 수준으로 정의
- **FP(Function Point)**: 사용자 관점 기능을 기준으로 소프트웨어 규모를 산정
- **RFP(Request for Proposal)**: 범위·요건·평가·계약 조건을 제시하는 제안 요청 문서

</details>

## 예상문제

> ISMP(Information System Master Plan)의 개념과 방법론 체계를 설명하고, 단계별 활동·산출물, ISP와의 차이 및 구축사업 이행방안의 실효성 확보 방안을 제시하시오. (25점)

## Ⅰ. 발주 Baseline을 수립하는 ISMP의 개요

> ISMP는 **특정 정보시스템**의 요건을 실행 가능한 발주 **Baseline**으로 전환하며, 완성도는 **Traceability**로 판정한다.

- 정의: **특정 정보시스템**의 요건을 **FP 산정 수준**으로 상세화하여 발주 **Baseline**을 수립하는 활동
- 목적: 요건-아키텍처-예산-**RFP** 간 **Traceability** 확보 → 과업 변경·조달 분쟁 예방

## Ⅱ. ISMP 구성체계 및 5단계 방법론

> 각 단계는 `입력 → 활동 → 산출물`로 이어지며, 최종 RFP가 최초 요건을 잃지 않아야 방법론이 닫힌다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="ISMP 구성체계와 5단계 방법론의 활동 및 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 프로젝트 착수</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>범위 · 조직 · 일정 · 품질계획</span>
      <strong>산출</strong><span>수행계획서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 정보시스템 방향성 수립</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>환경·현황 · 목표 · 추진 범위</span>
      <strong>산출</strong><span>범위·방향성 정의서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 업무 및 IT 요건 분석</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>업무 · 기능 · 데이터 · 비기능 요건 분석</span>
      <strong>산출</strong><span>업무·IT 요건 목록</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 정보시스템 구조 및 요건 정의</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>목표 아키텍처 · 인터페이스 · 상세 요건 정의</span>
      <strong>산출</strong><span>아키텍처 · 요건명세서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 구축사업 이행방안 수립</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>일정 · FP · 예산 · 발주전략 수립</span>
      <strong>산출</strong><span>이행계획 · 예산서 · RFP</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>RTM</strong></span> · 요건 ↔ 아키텍처 ↔ FP·예산 ↔ RFP 양방향 추적</div>

## Ⅲ. ISP와 ISMP의 비교

> **ISP**는 투자 과제를 선택하고, **ISMP**는 선택된 시스템을 **발주 Baseline**으로 확정한다.

| 기준 | ISP | ISMP |
|---|---|---|
| 질문 | 무엇을 왜 추진할 것인가 | 무엇을 어느 범위·비용으로 구축할 것인가 |
| 대상 | 조직·업무 전반 | 특정 정보시스템 |
| 상세 | 전략·개념 수준 | 상세 요건·**FP 산정 수준** |
| 산출 | 정보화 과제 · 우선순위 · 로드맵 | 요건명세 · 아키텍처 · 예산 · **RFP** |
| 종료 | 투자 과제 선정 | 발주 Baseline 확정 |

## Ⅳ. 구축사업 이행방안의 실효성 확보

> 조달 전 **Quality Gate**에서 범위·비용·계약의 연결성을 검증해야 구축 단계의 변경비용을 앞단에서 차단할 수 있다.

| 위험 | 원인 | 통제 | 검증 |
|---|---|---|---|
| 과업 변경 | 요건-RFP 단절 | **RTM** 전수 점검 | 미반영 요건 없음 |
| 예산 왜곡 | 기능 규모·인프라 비용 혼재 | **FP**·인프라·운영비 분리 | 규모·단가·예산 일치 |
| 구조 불일치 | 요건-아키텍처 별도 설계 | 요건별 구성요소 매핑 | 미할당·중복 제거 |
| 발주 분쟁 | 수용기준·책임 불명확 | 검수조건·발주단위 명시 | 요건별 검수 가능 |

## Ⅴ. Traceability 중심의 기술사적 제언

> 보고서 분량이 아니라 요건에서 계약까지 이어지는 **Traceability**를 통과 조건으로 삼아야 ISMP가 조달 통제장치로 작동한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: ISMP의 성패는 보고서 두께가 아니라 업무 요건이 아키텍처·예산·계약문서에 1:1로 추적되는가에 달려 있음. 이 연결이 끊기면 구축 단계에서 과업 변경과 예산 분쟁이 다시 발생함.
- 나라면: 종료 검토 때 문서별 완성도만 보지 않고, RTM(Requirements Traceability Matrix)의 `요건 → 아키텍처 → FP·예산 → RFP` 전수 매핑을 Quality Gate로 강제하겠음.

### 실전 답안용 기술사적 제언

- 판정: 산출물 존재보다 요건별 종단 Traceability 확인
- 대안: **RTM** 기반 종료 **Quality Gate** 운영
- 검증: 미매핑 요건 없음 · 중복 과업 제거 · 비용 근거 일치
- 효과: 조달 전 Baseline 확정 → 과업 변경·유찰·분쟁 예방

<div class="itpe-pipeline is-vertical" role="img" aria-label="RTM 기반 ISMP 종료 Quality Gate 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>산출물별 분절 검토 · 계약 연계 누락</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>RTM 기반 종료 Quality Gate</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>요건 → 아키텍처 → FP·예산 → RFP 전수 추적</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>Gate 통과 후 발주 · 변경비용 사전 차단</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **ISMP(Information System Master Plan)**는 특정 정보시스템의 요건을 **FP(Function Point) 산정 수준**으로 상세화하여 발주 **Baseline**을 수립하는 활동
- 목적: 요건과 **RFP(Request for Proposal)** 정합성 확보 → 과업 변경·예산 분쟁 예방

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="ISMP 5단계 구성체계 및 방법론 요약">
  <div class="itpe-pipeline-node">
    <strong>착수</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>범위 · 조직 · 일정 정의</span><strong>산출</strong><span>수행계획서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>방향성</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>환경 · 현황 · 목표 · 범위 분석</span><strong>산출</strong><span>범위·방향성 정의서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>요건 분석</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>업무 · IT · 비기능 요건 도출</span><strong>산출</strong><span>업무·IT 요건 목록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>구조·요건 정의</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>목표 아키텍처 · 인터페이스 · 상세요건 정의</span><strong>산출</strong><span>아키텍처 · 요건명세서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>이행방안</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>일정 · FP · 예산 · 발주전략 수립</span><strong>산출</strong><span>이행계획 · 예산서 · RFP</span></div>
  </div>
</div>

### 3. RTM·Quality Gate

<div class="itpe-flow-map" role="img" aria-label="RTM으로 요건부터 RFP까지 추적하고 Quality Gate에서 발주 여부를 판정하는 핵심 통제">
  <div class="itpe-flow-node">
    <span class="itpe-keyword"><strong>RTM(Requirements Traceability Matrix)</strong></span>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>추적 경로</strong><span>요건 ↔ 아키텍처 ↔ FP·예산 ↔ RFP</span></div>
      <div class="itpe-flow-branch"><strong>확인</strong><span>누락 · 고립 · 불일치 탐지</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>Quality Gate</strong></span>
    <div class="itpe-step-detail"><strong>판정 질문</strong><span>모든 요건이 RFP까지 양방향 추적되는가?</span></div>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>통과</strong><span>발주 Baseline 확정 → 조달 진행</span></div>
      <div class="itpe-flow-branch"><strong>미통과</strong><span>누락·불일치 보완 → RTM 재검증</span></div>
    </div>
  </div>
</div>

## 출제 이력과 검증 출처

- 제138회 정보관리기술사 2교시: ISP 정의·목적, 수행방법론, ISP·ISMP 비교
- 한국지능정보사회진흥원(NIA), [ISP·ISMP 수립 공통가이드 제9판](https://nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=28088&cbIdx=99835&parentSeq=28088)

## 학습 체크

- [ ] Ⅰ 개요: ISMP를 `특정 시스템 · FP 산정 수준 · 발주 Baseline`으로 정의하고 목적을 말할 수 있는가?
- [ ] Ⅱ 방법론: 5단계를 순서대로 쓰고, 각 단계의 **활동과 산출물**을 한 쌍으로 재현할 수 있는가?
- [ ] Ⅲ 비교: ISP와 ISMP를 `질문 · 대상 · 상세 · 산출 · 종료` 5개 축으로 비교할 수 있는가?
- [ ] Ⅳ 통제: `요건 ↔ 아키텍처 ↔ FP·예산 ↔ RFP`의 RTM과 Quality Gate 검증 기준을 설명할 수 있는가?
- [ ] Ⅴ 제언: 문서 분량이 아닌 Traceability를 ISMP 종료 조건으로 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [IT 전략·관리 개요](./index.md)
- 연관 토픽: [ISP](./003_isp.md), [과업심의](./091_public_sw_cost_and_scope_change_criteria.md)
- 다음 토픽: [ISO/IEC 38500](./002_iso_iec_38500.md)
