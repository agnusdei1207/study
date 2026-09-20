---
title: "ISMP"
author: "Antigravity"
date: "2026-09-20T20:27:33+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash (High)"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 정보화 기획·발주를 거쳐 ISMP로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>정보화 기획·발주</span>
  <strong>ISMP</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **ISMP(Information System Master Plan)**는 **ISP(Information Strategy Planning)**가 선정한 정보화 과제를 조달 가능한 **Baseline**으로 구체화
- 메커니즘: 요구사항 분석 → 아키텍처 정의 → 규모·예산 산정 → **RFP(Request for Proposal)** 도출 과정을 **RTM(Requirements Traceability Matrix)**으로 연결
- 산출물: 요구사항 명세서 · 목표 아키텍처 · **FP(Function Point)** 기반 예산서 · RFP

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

- **ISMP(Information System Master Plan)**: 특정 시스템의 요구사항·구조·예산을 발주 가능한 수준으로 구체화하는 마스터플랜
- **ISP(Information Strategy Planning)**: 조직의 비전 달성을 위해 정보화 방향과 투자 과제를 선정하는 상위 전략 계획
- **Baseline(기준선)**: 승인된 범위·요구사항·비용의 공식적인 변경 통제 기준
- **RTM(Requirements Traceability Matrix)**: 요구사항이 설계·비용·계약 산출물에 빠짐없이 반영되었는지 양방향으로 검증하는 추적 매트릭스
- **FP(Function Point)**: 사용자 관점의 논리적 기능을 기준으로 소프트웨어 규모와 비용을 산정하는 기법
- **RFP(Request for Proposal)**: 발주자가 제안사에게 시스템 구축 범위·요구사항·평가·계약 조건을 제시하는 제안요청서

</details>

## 예상문제

> ISMP(Information System Master Plan)의 개념과 방법론 체계를 설명하고, 단계별 활동·산출물, ISP와의 차이 및 구축사업 이행방안의 실효성 확보 방안을 제시하시오. (25점)

## Ⅰ. 발주 Baseline을 수립하는 ISMP의 개요

> ISMP는 특정 정보시스템의 요구사항을 실행 가능한 조달 Baseline으로 전환하며, 품질 성패는 산출물 두께가 아닌 Traceability로 판정함

- 정의: 특정 정보시스템의 요구사항을 **FP 산정 수준**으로 상세화하여 조달을 위한 발주 **Baseline**을 수립하는 활동
- 목적: 과업 범위 기준선 확정 및 조달 분쟁·과업 변경 차단

## Ⅱ. ISMP 구성체계 및 5단계 방법론

> 각 단계는 입력 → 활동 → 산출물로 빈틈없이 전개되며, 최초 업무 요구사항이 최종 RFP까지 단절 없이 이어져야 방법론이 완성됨

<div class="itpe-pipeline is-vertical" role="img" aria-label="ISMP 구성체계와 5단계 방법론의 활동 및 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 프로젝트 착수</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>사업 범위 · 조직 · 일정 · 품질 통제 계획 수립</span>
      <strong>산출</strong><span>수행계획서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 정보시스템 방향성 수립</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>내외부 환경 · 업무 현황 · 목표 모델 · 추진 범위 정의</span>
      <strong>산출</strong><span>범위·방향성 정의서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 업무 및 IT 요건 분석</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>업무 기능 · 데이터 · 비기능(보안·성능) 요구사항 도출 및 명세화</span>
      <strong>산출</strong><span>업무·IT 요건 목록</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 정보시스템 구조 및 요건 정의</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>목표 아키텍처 수립 · 내외부 인터페이스 및 상세 요구사항 정의</span>
      <strong>산출</strong><span>목표 아키텍처 명세서 · 요구사항 명세서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 구축사업 이행방안 수립</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>추진 일정 · FP 기반 예산 산정 · 분할 발주 등 발주전략 수립</span>
      <strong>산출</strong><span>이행계획서 · 예산서 · RFP</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>RTM</strong></span> 추적 경로: 요구사항 ↔ 아키텍처 ↔ FP·예산 ↔ RFP</div>

## Ⅲ. ISP와 ISMP의 차이점

> ISP는 전사 관점의 투자 과제를 선정하고, ISMP는 선택된 개별 시스템을 발주 Baseline으로 구체화함

| 비교축 | ISP | ISMP |
|---|---|---|
| 목적 | 정보화 과제·투자 우선순위 선정 | 발주 범위·비용 기준선(Baseline) 확정 |
| 대상 범위 | 전사 조직 및 업무 전반 | 특정 정보시스템 구축 사업 |
| 분석 상세도 | 전략 및 개념적 아키텍처 수준 | 상세 요구사항 및 **FP 산정 가능 수준** |
| 핵심 산출물 | 정보화 과제 목록 · 우선순위 · 중장기 로드맵 | 상세 요구사항 명세서 · 목표 아키텍처 · 예산서 · **RFP** |
| 종료 기준 | 최적 투자 과제 선정 및 경영진 승인 | 발주 Baseline 확정 |

## Ⅳ. 구축사업 이행방안의 실효성 확보 (조달 위험 통제)

> 조달 전 Quality Gate에서 범위·비용·계약의 연결성을 선제적으로 검증해야 구축 단계의 예산 초과 및 과업 변경을 방지할 수 있음

| 위험 | 대책 | 효과 |
|---|---|---|
| 잦은 과업 변경 | **RTM** 기반 요구사항 전수 점검 | 미반영 요구사항 및 과잉 설계 제거 |
| 예산 왜곡 및 초과 | **FP**와 인프라·운영 비용 분리 산정 | 기능 규모와 예산 일치 확보 |
| 구조적 불일치 | 요구사항별 아키텍처 구성요소 1:1 매핑 | 누락 및 중복 제거 |
| 발주·계약 분쟁 | RFP 내 검수조건 및 발주단위 명시 | 명확한 검수 및 책임 소재 확정 |

## Ⅴ. Traceability 중심의 기술사적 제언

> ISMP의 실효성은 방대한 문서가 아니라, 최초 요구사항이 계약 기준(RFP)까지 훼손 없이 연결되는 Traceability 통제에 있음

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: ISMP의 성패는 보고서의 두께가 아니라, 사용자의 업무 요구사항이 목표 아키텍처, 예산, 계약 문서(RFP)로 단절 없이 추적되는가에 달려 있다. 이 연결고리가 끊어지면 구축 단계에서 100% 과업 변경과 예산 분쟁이 발생한다.
- `나라면`: ISMP 산출물 검수 시 단순 양식 채우기를 넘어, RTM 기반의 `요구사항 → 아키텍처 → FP·예산 → RFP` 전수 추적 매핑을 조달 전 Quality Gate 통과 조건으로 강제하겠다.

### 실전 답안용 기술사적 제언

- 판정: ISMP 종료 기준은 단순 산출물 존재 유무가 아니라, 요구사항별 종단 Traceability 확보 여부임
- 대안: **RTM** 기반 발주 전 종료 **Quality Gate** 운영 강제
- 검증: 미매핑 요구사항 없음 · 과잉 설계 파악 · 예산 산출 근거의 1:1 일치 여부 점검
- 효과: 조달 전 명확한 Baseline 확정 → 구축 시 과업 변경, 사업 유찰, 분쟁의 원천 차단

<div class="itpe-pipeline is-vertical" role="img" aria-label="RTM 기반 ISMP 종료 Quality Gate 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>산출물별 분절적 검토 및 계약 연계 누락</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>RTM 기반 종료 Quality Gate 운영</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>요구사항 → 아키텍처 → FP·예산 → RFP 전수 추적</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>명확한 Baseline 기반 발주 확정 및 변경비용 차단</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. ISMP의 정의 및 목적

- 정의: **ISMP(Information System Master Plan)**는 특정 정보시스템의 요구사항을 **FP 산정 수준**으로 구체화하여 발주 **Baseline**을 수립하는 활동
- 목적: 명확한 과업 범위 확정을 통한 과업 변경 및 조달 분쟁 예방

### 2. ISMP 구성체계 및 5단계 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="ISMP 5단계 구성체계 및 방법론 요약">
  <div class="itpe-pipeline-node">
    <strong>착수</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>범위 · 일정 · 품질계획 수립</span><strong>산출</strong><span>수행계획서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>방향성 수립</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>업무 현황 · 목표 · 추진 범위 정의</span><strong>산출</strong><span>방향성 정의서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>요구사항 분석</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>업무 · IT · 비기능 요구사항 도출</span><strong>산출</strong><span>업무·IT 요건 목록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>구조·요구사항 정의</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>목표 아키텍처 및 상세 요구사항 정의</span><strong>산출</strong><span>아키텍처 · 요구사항 명세서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>이행방안 수립</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>일정 · FP 예산 · 발주전략 도출</span><strong>산출</strong><span>이행계획서 · 예산서 · RFP</span></div>
  </div>
</div>

### 3. RTM 기반 발주 Quality Gate

<div class="itpe-flow-map" role="img" aria-label="RTM으로 요구사항부터 RFP까지 추적하고 Quality Gate에서 발주 여부를 판정하는 핵심 통제">
  <div class="itpe-flow-node">
    <span class="itpe-keyword"><strong>RTM(Requirements Traceability Matrix)</strong></span>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>추적 경로</strong><span>요구사항 ↔ 아키텍처 ↔ FP·예산 ↔ RFP</span></div>
      <div class="itpe-flow-branch"><strong>확인</strong><span>누락 · 고립 · 불일치 · 과잉설계 탐지</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>Quality Gate</strong></span>
    <div class="itpe-step-detail"><strong>판정 질문</strong><span>모든 요구사항이 RFP까지 양방향 추적되는가?</span></div>
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
- [ ] Ⅲ 비교: ISP와 ISMP를 `목적 · 대상 범위 · 분석 상세도 · 핵심 산출물 · 종료 기준` 5개 축으로 비교할 수 있는가?
- [ ] Ⅳ 통제: `위험 · 대책 · 효과`를 기준으로 구축사업 이행방안의 조달 위험 통제 방안을 설명할 수 있는가?
- [ ] Ⅴ 제언: 문서 분량이 아닌 Traceability 중심의 RTM 기반 Quality Gate를 통과 조건으로 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [IT 전략·관리 개요](./index.md)
- 연관 토픽: [ISP](./003_isp.md), [과업심의](./091_public_sw_cost_and_scope_change_criteria.md)
- 다음 토픽: [ISO/IEC 38500](./002_iso_iec_38500.md)
