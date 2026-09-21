---
title: "정보시스템 운영 성과관리"
author: "Antigravity"
date: "2026-09-22T05:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  keyword_grade: "C"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 시스템 운영 관리·IT 거버넌스를 거쳐 정보시스템 운영 성과관리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>시스템 운영 관리·IT 거버넌스</span>
  <strong>정보시스템 운영 성과관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **정보시스템 운영 성과관리**는 정보시스템의 지속 운영 가치를 판단하고 업무·비용 성과를 높이는 활동
- 메커니즘: 대상 선정 → 성과측정 → 성과평가 → 정비대상 결정·정비계획 환류
- 산출물: 성과측정 결과 · 평가점수 · 정비권고 · 정비계획

<div class="itpe-pipeline is-vertical" role="img" aria-label="정보시스템 운영 성과관리의 대상 선정부터 정비계획까지 세로 흐름">
  <div class="itpe-pipeline-node"><strong>① 대상 선정</strong><div class="itpe-step-detail"><strong>기준</strong><span>제23조의 성과측정 대상·제외대상 식별</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>② 성과측정</strong><div class="itpe-step-detail"><strong>비용</strong><span>40점</span></div><div class="itpe-step-detail"><strong>업무</strong><span>60점</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>③ 성과평가</strong><div class="itpe-step-detail"><strong>주체</strong><span>행정안전부장관</span></div><div class="itpe-step-detail"><strong>산출</strong><span>100점 만점 평가점수</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><strong>④ 정비권고·정비계획</strong><div class="itpe-step-detail"><strong>판정</strong><span>60점 미만 정비권고 가능</span></div><div class="itpe-step-detail"><strong>환류</strong><span>폐기·개선 등 정비계획 수립</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- **정보시스템 운영 성과관리**: 지속 운영 가치를 판단하기 위해 운영 성과측정·평가 결과에 따라 정비대상을 결정하고 업무·비용 성과를 높이는 활동
- **성과측정**: 비용 측면 40점·업무 측면 60점의 지표별 기초데이터로 운영 성과를 측정하는 활동
- **성과평가**: 제출된 성과측정 결과를 행정안전부장관이 검토하여 평가점수를 확정하는 활동
- **정비**: 평가점수에 따라 폐기하거나 통폐합·기능고도화·전면재개발 등의 개선방안을 마련·시행하는 조치

</details>

## 예상문제

> 「전자정부 성과관리 지침」에 따른 정보시스템 운영 성과관리의 개념·절차, 성과측정 지표와 정비 판정기준을 설명하시오. **(미출제 예상·25점)**

## Ⅰ. 지속 운영 가치와 정비대상을 결정하는 성과관리

> 성과측정·평가 결과를 근거로 저성과 정보시스템을 정비하되, 폐기 예외와 서비스 연속성을 함께 통제함.

- 정의: 정보시스템의 지속 운영 가치를 판단하기 위해 운영 성과측정·평가 결과에 따라 **정비대상**을 결정하여 업무·비용 성과를 높이는 활동
- 목적: 운영 성과의 객관적 진단 · 저성과 시스템 정비 · 정보화 투자 효율화

## Ⅱ. 현행 지침의 성과관리 조문 체계

| 단계 | 공식 근거 | 핵심 활동 | 산출 |
|---|---|---|---|
| **대상 선정** | 제23조 | 성과측정 대상·제외대상 식별 | 측정 대상 목록 |
| **성과측정** | 제24조 | 기관이 기초데이터·증빙자료를 수집하여 비용·업무 성과 측정 | 성과측정 결과 |
| **성과평가** | 제25조 | 행정안전부장관이 측정 결과를 검토·평가 | 평가점수 |
| **정보시스템 정비** | 제26조 | 60점 미만 시스템에 점수 구간별 정비권고 | 정비대상·정비권고 |
| **정비계획 수립** | 제27조 | 정비권고 시스템의 폐기·개선 계획 수립 | 정비계획 |

<div class="itpe-trace-band"><span class="itpe-keyword"><strong>통제 원칙</strong></span> · 정비계획에 이용자 불편 방지 · 정보 이관 또는 보존 · 전자정부서비스 연속성 보장 포함</div>

## Ⅲ. 성과측정 구성, 비용 40점·업무 60점

| 측면 | 지표 | 배점 | 측정 초점 |
|---|---|---:|---|
| **비용** | 운영의 적정성 | 10점 | 누적유지보수비÷누적개발비 |
| **비용** | 유지의 용이성 | 10점 | 전년 대비 운영유지비 증감률 |
| **비용** | 비용의 효율성 | 20점 | 전년 대비 활용규모당 운영유지비 증감률 |
| **업무** | 기능 활용도 | 20점 | 기능별 전년 대비 사용량 증감률 |
| **업무** | 업무 성과 달성도 | 40점 | 공통지표 10점 · 고유지표 30점 |
| **합계** | 비용 40점 · 업무 60점 | **100점** | 지표별 환산점수 합산 |

> 세부 구간·환산점수는 현행 지침 별표를 적용하며, 성과측정 데이터·증빙자료의 적정성 검토 결과가 평가점수에 반영될 수 있음.

## Ⅳ. 제26조 평가점수별 정비 판정

<div class="itpe-svg-map">
  <svg viewBox="0 0 520 220" role="img" aria-label="전자정부 정보시스템 운영 성과평가 100점 점수 구간별 정비 판정 체계도">
    <!-- 100 Point Bar -->
    <rect x="20" y="20" width="480" height="35" rx="6" class="itpe-svg-node"></rect>
    <text x="260" y="42" class="itpe-svg-title">종합 평가점수 = 비용 측면(40점) + 업무 측면(60점) [총 100점 만점]</text>

    <!-- Threshold 1: 60+ Points -->
    <rect x="20" y="70" width="150" height="95" rx="6" class="itpe-svg-node is-current"></rect>
    <text x="95" y="92" class="itpe-svg-title">60점 이상 (유지)</text>
    <line x1="30" y1="102" x2="160" y2="102" stroke="var(--sl-color-gray-4)" stroke-width="1"></line>
    <text x="95" y="122" class="itpe-svg-sub">정비권고 비해당</text>
    <text x="95" y="140" class="itpe-svg-sub">지속 운영 및 고도화</text>
    <text x="95" y="156" class="itpe-svg-sub">품질 수준 향상 관리</text>

    <!-- Threshold 2: 40 ~ 60 Points -->
    <rect x="185" y="70" width="150" height="95" rx="6" class="itpe-svg-node"></rect>
    <text x="260" y="92" class="itpe-svg-title">40점 ~ 60점 (개선)</text>
    <line x1="195" y1="102" x2="325" y2="102" stroke="var(--sl-color-gray-4)" stroke-width="1"></line>
    <text x="260" y="122" class="itpe-svg-sub">정비권고 대상</text>
    <text x="260" y="140" class="itpe-svg-sub">통폐합 / 기능 재설계</text>
    <text x="260" y="156" class="itpe-svg-sub">전면 재개발 등 정비</text>

    <!-- Threshold 3: Under 40 Points -->
    <rect x="350" y="70" width="150" height="95" rx="6" class="itpe-svg-node"></rect>
    <text x="425" y="92" class="itpe-svg-title">40점 미만 (폐기)</text>
    <line x1="360" y1="102" x2="490" y2="102" stroke="var(--sl-color-gray-4)" stroke-width="1"></line>
    <text x="425" y="122" class="itpe-svg-sub">원칙: 폐기 권고</text>
    <text x="425" y="140" class="itpe-svg-sub">단, 8대 법정 예외 사유</text>
    <text x="425" y="156" class="itpe-svg-sub">해당 시 폐기 유예</text>

    <!-- Bottom Exception Callout -->
    <rect x="20" y="175" width="480" height="35" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1"></rect>
    <text x="260" y="196" class="itpe-svg-sub" text-anchor="middle">폐기 예외: 법령 근거, 안보/치안, 국민생활 필수, 취약계층 서비스, 3년 미경과 등 심의</text>
  </svg>
</div>

<div class="itpe-flow-map" role="img" aria-label="정보시스템 성과평가 점수가 60점 이상인지 판정하고 60점 미만을 40점 기준으로 나누는 흐름">
  <div class="itpe-flow-node"><strong>성과평가 총점</strong><div class="itpe-step-detail"><strong>만점</strong><span>100점</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>60점 미만인가?</strong><div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>아니요</strong><span>제26조 정비권고 대상 아님</span></div><div class="itpe-flow-branch"><strong>예</strong><span>정비권고 가능 → 40점 기준 판정</span></div></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>60점 미만 점수 구간</strong><div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>40점 미만</strong><span><span class="itpe-keyword"><strong>폐기</strong></span></span></div><div class="itpe-flow-branch"><strong>40점 이상 60점 미만</strong><span>폐기 또는 통폐합·기능고도화·전면재개발 등 개선방안 마련·시행</span></div></div></div>
</div>

| 평가점수 | 제26조 판정 | 후속 조치 |
|---:|---|---|
| **60점 이상** | 제26조제1항의 정비권고 대상 아님 | 지표 결과값 관리 · 운영·관리 수준 향상 |
| **40점 이상 60점 미만** | 정비권고 가능 | 폐기 또는 통폐합·기능고도화·전면재개발 등 개선방안 마련·시행 |
| **40점 미만** | 폐기 정비권고 가능 | 제26조제2항 예외 검토 후 폐기 절차 수행 |

> 40점 미만이라도 법령상 구축·운영 근거, 생명·안보·치안, 국가경제·국민생활, 대국민 서비스, 사회적 약자, 표준 보급시스템, 운영 3년 미경과, 위원회 인정 사유에 해당하면 폐기권고를 하지 않을 수 있음.

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| **기초데이터 오류** | 원천자료·산식·증빙자료 교차검증 | 평가 재현성 확보 |
| **점수만으로 기계적 폐기** | 제26조제2항 폐기 예외 검토 · 위원회 판단 근거 기록 | 필수 서비스 보호 |
| **정비 중 서비스 단절** | 이용자 불편 방지 · 정보 이관·보존 · 서비스 연속성 계획 | 안전한 정비 이행 |

## Ⅵ. 증빙과 서비스 연속성을 확보하기 위한 기술사적 제언

> 평가점수만 제시하지 않고 원천자료·폐기 예외·정비 이행의 판단 근거를 끝까지 추적해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 현행 체계의 판정 단위는 업무·비용 2×2 유형이 아니라 **100점 평가점수와 60점·40점 구간**임.
- 나라면: 지표별 원천자료와 폐기 예외 검토 근거를 함께 보존하여 점수와 정비결정의 감사 추적성을 확보하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준 (Trigger)**: 행정안전부 정보시스템 운영 성과평가 점수가 60점 미만 도출 시 즉시 정비권고 대상으로 지정, 40점 미만 시 폐기 원칙 적용.
- **대응 방안 (Action)**: 40~60점 구간은 통폐합/클라우드 전환/기능고도화 정비계획을 수립하고, 40점 미만은 8대 법정 예외(안보, 취약계층 등) 해당 여부를 위원회 심의 후 데이터 이관·보존 절차를 거쳐 안전 폐기.
- **검증 체계 (Verification)**: 비용 40점(유지보수비 비율) 및 업무 60점(사용량 및 공통/고유 성과지표)의 기초 증빙데이터(로그, 결산서)의 무결성을 전수 교차 감사함.
- **기대 효과 (Impact)**: 유령·저활용 공공시스템 유지보수 예산 낭비 차단, 전자정부 서비스 연속성 및 공공 데이터 안전 이관 보장을 달성함.

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 운영 성과측정·평가 결과에 따라 정비대상을 결정하여 정보시스템의 업무·비용 성과를 높이는 활동
- 목적: 지속 운영 가치 판단 · 저성과 시스템 정비 · 정보화 투자 효율화

### 2. 측정·판정체계

| 구분 | 핵심 기준 | 결과 |
|---|---|---|
| **성과측정** | 비용 40점 · 업무 60점 | 100점 만점 평가점수 |
| **60점 이상** | 제26조 정비권고 기준 비해당 | 지표 결과값 관리 · 수준 향상 |
| **40점 이상 60점 미만** | 정비권고 가능 | 폐기 또는 통폐합·기능고도화·전면재개발 등 개선 |
| **40점 미만** | 폐기 정비권고 가능 | 폐기 예외 검토 · 정비계획 수립 |

## 출제 이력과 검증 출처

- 국가법령정보센터, [전자정부 성과관리 지침](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulId=61899&efYd=0) — 2025년 12월 19일 시행, 행정안전부고시 제2025-71호, 제2조·제23조~제27조
- 국가법령정보센터, [정보시스템 운영 성과측정 지표별 배점 및 환산점수](https://www.law.go.kr/LSW/flDownload.do?bylClsCd=200201&flNm=%5B%EB%B3%84%ED%91%9C%5D+%EC%A0%95%EB%B3%B4%EC%8B%9C%EC%8A%A4%ED%85%9C+%EC%9A%B4%EC%98%81+%EC%84%B1%EA%B3%BC%EC%B8%A1%EC%A0%95+%EC%A7%80%ED%91%9C%EB%B3%84+%EB%B0%B0%EC%A0%90+%EB%B0%8F+%ED%99%98%EC%82%B0%EC%A0%90%EC%88%98%28%EC%A0%9C25%EC%A1%B0%EC%A0%9C1%ED%95%AD+%EA%B4%80%EB%A0%A8%29&flSeq=148844105) — 제25조제1항 관련 현행 별표

> 연혁 주의: 업무·비용 기준값의 2×2 유지관리유형 분류는 폐지된 구 지침 체계이며 현행 판정기준으로 사용하지 않음.

## 학습 체크

- [ ] Ⅰ: 정보시스템 운영 성과관리의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 제23조~제27조의 대상 선정 → 측정 → 평가 → 정비 → 정비계획 흐름을 재현할 수 있는가?
- [ ] Ⅲ: 비용 40점·업무 60점의 지표·배점을 설명할 수 있는가?
- [ ] Ⅳ: 60점·40점 구간별 정비 판정과 40점 미만 폐기 예외를 설명할 수 있는가?
- [ ] Ⅴ: 기초데이터·폐기판단·서비스 연속성 위험의 대책·효과를 제시할 수 있는가?
- [ ] Ⅵ: 평가점수부터 정비 이행까지 감사 추적성을 확보하는 방안을 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [SEM](./078_sem.md)
- 연관 토픽: [시스템 운영 감리](./059_system_operation_audit.md), [IT 투자평가](./016_it_investment_evaluation.md), [공공 클라우드 네이티브 전환](./021_public_cloud_native_transition.md)
- 다음 토픽: [CPM](./081_cpm.md)
