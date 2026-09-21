---
title: "공공 SW 사업 하도급 제한"
author: "Antigravity"
date: "2026-09-22T08:45:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 소프트웨어 사업 제도를 거쳐 하도급 제한으로 이어지는 위치">
  <span>IT 전략·관리</span><span>공공 SW 사업 제도</span><strong>하도급 제한</strong>
</div>

## 큰 그림과 30초 인출

- **원칙**: 물품 구매금액을 제외한 SW 사업금액의 50% 초과 하도급 제한
- **통제**: 재하도급 제한·국가기관 등의 장에게 사전승인
- **예외**: 물품 설치·유지관리, 신기술·전문기술 등 법정 사유

<div class="itpe-svg-map">
<svg viewBox="0 0 720 520" role="img" aria-label="공공 소프트웨어 사업 하도급 제한 구조">
  <defs><marker id="sub-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link"></path></marker></defs>
  <rect x="240" y="30" width="240" height="80" rx="14" class="itpe-svg-node"></rect>
  <text x="360" y="65" text-anchor="middle" class="itpe-svg-title">국가기관 등의 장</text>
  <text x="360" y="92" text-anchor="middle" class="itpe-svg-sub">사전승인·이행관리</text>
  <rect x="240" y="175" width="240" height="110" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="360" y="212" text-anchor="middle" class="itpe-svg-title">원수급인</text>
  <text x="360" y="242" text-anchor="middle" class="itpe-svg-sub">50% 초과 하도급 제한</text>
  <text x="360" y="267" text-anchor="middle" class="itpe-svg-sub">법정 예외·사전승인</text>
  <rect x="240" y="355" width="240" height="95" rx="14" class="itpe-svg-node"></rect>
  <text x="360" y="392" text-anchor="middle" class="itpe-svg-title">하수급인</text>
  <text x="360" y="422" text-anchor="middle" class="itpe-svg-sub">재하도급 제한</text>
  <path d="M360 110 L360 175" class="itpe-svg-link" marker-end="url(#sub-arrow)"></path>
  <text x="375" y="148" class="itpe-svg-label">승인</text>
  <path d="M360 285 L360 355" class="itpe-svg-link" marker-end="url(#sub-arrow)"></path>
  <text x="375" y="327" class="itpe-svg-label">하도급</text>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **SW(Software)**: 소프트웨어
- **하도급**: 원수급인이 도급받은 사업의 일부를 제3자에게 수행시키는 계약
- **재하도급**: 하수급인이 도급받은 사업을 다시 제3자에게 하도급하는 계약
- **사전승인**: 하도급·재하도급 계약 전에 국가기관 등의 장에게 받는 승인
- **WBS(Work Breakdown Structure)**: 사업 범위를 관리 가능한 작업으로 분해한 구조
- **RTM(Requirements Traceability Matrix)**: 요구사항과 산출물의 추적 관계를 기록한 표

</details>

## 예상문제

> **(미출제 예상·25점)** 소프트웨어진흥법상 공공 SW 사업의 하도급 제한 원칙·예외·승인 절차를 설명하고, 관리상 문제점과 대응책을 제시하시오.

## Ⅰ. 공공 SW 사업 하도급 제한 개요

> 원수급인의 수행 책임을 확보하고 다단계 하도급에 따른 품질·대금 위험을 통제하는 제도

- **정의**: 소프트웨어진흥법 제51조에 따라 공공 SW 사업의 하도급 비율·재하도급·사전승인을 통제하는 제도
- **목적**: 원수급인 책임 강화·다단계 하도급 방지·사업 품질 보호

## Ⅱ. 제한 원칙·예외 및 산정 메커니즘

> 50%는 직접수행 비율을 일률적으로 선언하는 표현보다 산정 기준과 법정 예외를 함께 제시해야 정확함

### 1. 하도급 50% 제한 산정 기준 및 승인 메커니즘

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
  <text x="15" y="24" fill="var(--sl-color-text)" font-size="13" font-weight="bold">공공 SW 하도급 50% 산정 기준 및 사전승인 통제 체계</text>

  <!-- Left: Total Project Scope Breakdown -->
  <g transform="translate(15, 45)">
    <rect x="0" y="0" width="220" height="155" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="6"/>
    <text x="110" y="20" fill="var(--sl-color-text)" font-size="11" font-weight="bold" text-anchor="middle">전체 사업금액 분할 기준</text>

    <!-- Excluded hardware/cots box -->
    <rect x="10" y="32" width="200" height="32" fill="var(--sl-color-bg-sidebar)" stroke="var(--sl-color-hairline)" rx="3"/>
    <text x="110" y="47" fill="var(--sl-color-text-muted)" font-size="9" text-anchor="middle">단순 H/W 및 상용SW 물품구매</text>
    <text x="110" y="58" fill="#ef4444" font-size="8" text-anchor="middle">[산정 모수에서 제외]</text>

    <!-- Target SW Service amount -->
    <rect x="10" y="72" width="200" height="75" fill="var(--sl-color-bg)" stroke="var(--sl-color-text-accent)" stroke-width="1.5" rx="3"/>
    <text x="110" y="88" fill="var(--sl-color-text-accent)" font-size="10" font-weight="bold" text-anchor="middle">순수 SW용역 사업금액 (모수 100%)</text>

    <!-- 50% Direct Execution -->
    <rect x="15" y="96" width="92" height="42" fill="var(--sl-color-bg-sidebar)" stroke="var(--sl-color-text-accent)" rx="2"/>
    <text x="61" y="113" fill="var(--sl-color-text-accent)" font-size="9" font-weight="bold" text-anchor="middle">원수급인 직접수행</text>
    <text x="61" y="128" fill="var(--sl-color-text)" font-size="8" text-anchor="middle">50% 이상 필수</text>

    <!-- 50% Max Subcontract -->
    <rect x="113" y="96" width="92" height="42" fill="var(--sl-color-bg-sidebar)" stroke="#ef4444" rx="2"/>
    <text x="159" y="113" fill="#ef4444" font-size="9" font-weight="bold" text-anchor="middle">하도급 허용 범위</text>
    <text x="159" y="128" fill="var(--sl-color-text)" font-size="8" text-anchor="middle">50% 이하 (사전승인)</text>
  </g>

  <!-- Connectors -->
  <path d="M 245 125 L 265 125" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Right: Control & Exception Architecture -->
  <g transform="translate(275, 45)">
    <!-- Contracting Authority -->
    <rect x="0" y="0" width="230" height="38" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="4"/>
    <text x="115" y="18" fill="var(--sl-color-text)" font-size="10" font-weight="bold" text-anchor="middle">발주기관 (국가기관 등의 장)</text>
    <text x="115" y="30" fill="var(--sl-color-text-accent)" font-size="8" text-anchor="middle">사전승인 및 하도급 적정성 평가</text>

    <!-- Flow down -->
    <path d="M 115 38 L 115 54" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="1.5" marker-end="url(#arrow)"/>

    <!-- Prime Contractor -->
    <rect x="0" y="55" width="230" height="42" fill="var(--sl-color-bg)" stroke="var(--sl-color-text-accent)" stroke-width="1.5" rx="4"/>
    <text x="115" y="73" fill="var(--sl-color-text-accent)" font-size="10" font-weight="bold" text-anchor="middle">원수급인 (대형/중견 SI)</text>
    <text x="115" y="87" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">직접수행 50% 이상 책임 / 대금 직접지급 준수</text>

    <!-- Flow down -->
    <path d="M 115 97 L 115 113" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="1.5" marker-end="url(#arrow)"/>

    <!-- Subcontractor -->
    <rect x="0" y="114" width="230" height="41" fill="var(--sl-color-bg)" stroke="#ef4444" stroke-width="1.5" rx="4"/>
    <text x="115" y="131" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">1차 하수급인 (전문 SW사)</text>
    <text x="115" y="145" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">⛔ 재하도급 원칙적 금지 (법정 예외 제외)</text>
  </g>
</svg>
</svg-diagram>
```

### 2. 제한 원칙 및 예외 상세 비교

| 구분 | 원칙 | 예외·통제 |
|---|---|---|
| 하도급 | 물품 구매금액 제외 SW 사업금액의 50% 초과 제한 | 물품 설치·유지관리, 신기술·전문기술 등 |
| 재하도급 | 하수급인의 재하도급 제한 | 법정 사유·절차에 따른 예외 |
| 승인 | 계약 전 사전승인 | 승인 내용대로 이행·관리 |

## Ⅲ. 하도급 승인·관리 절차

> 신청서의 계약 구조와 실제 수행 구조가 일치하는지를 승인 전·후로 확인함

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 소프트웨어 하도급 승인과 관리 절차">
  <div class="itpe-flow-node"><strong>① 계획·신청</strong><div class="itpe-step-detail"><strong>활동</strong><span>범위·금액·하수급인·수행계획 작성</span></div><div class="itpe-step-detail"><strong>산출</strong><span>승인신청서·계약서안</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>② 적정성 판단</strong><div class="itpe-step-detail"><strong>판단</strong><span>계약·대금·수행능력·사업관리</span></div><div class="itpe-step-detail"><strong>산출</strong><span>판단 결과</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>③ 승인·계약</strong><div class="itpe-step-detail"><strong>판정</strong><span>승인·거절·보완</span></div><div class="itpe-step-detail"><strong>산출</strong><span>승인서·하도급계약</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>④ 이행관리</strong><div class="itpe-step-detail"><strong>점검</strong><span>승인 범위·인력·대금·산출물</span></div><div class="itpe-step-detail"><strong>산출</strong><span>점검·시정 기록</span></div></div>
</div>

## Ⅳ. 문제점·대응책

> 승인서만 확인하면 무단 재하도급·수행주체 변경·대금 지연을 발견하기 어려움

| 위험 | 대책 | 효과 |
|---|---|---|
| 무단 하도급·재하도급 | 계약·투입조직·산출물 교차점검 | 실제 수행주체 확인 |
| 형식적 승인 | 범위·대금·역량 중심 판단 | 승인 실효성 확보 |
| 승인 후 구조 변경 | 변경 사전승인·정기점검 | 계약·현장 일치 |
| 대금 지연 | 지급계획·증빙 추적 | 하수급인 보호 |

## Ⅴ. 산출물 일치성 검증을 위한 기술사적 제언

> 하도급 비율 준수만으로 품질이 보장되지 않으며, 승인된 역할과 실제 산출물 책임의 일치가 핵심임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 하도급 계약 승인은 서류 절차에 불과할 수 있음. 실무에서 빈번한 '외주 인력 파견 위장'이나 '무단 2차 재하도급'을 방지하려면 형상관리 시스템(Git 커밋 로그, 작성자 서명)과 WBS 작업 패키지의 담당자를 실시간 매핑 검증해야 함.
- 나라면: 승인 범위·담당 조직·산출물 책임을 WBS와 RTM에 연결하고, 하도급지킴이를 통한 노임 직불 체계를 의무화하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 물품 제외 순수 SW 금액 기준 50% 초과 여부, 법정 재하도급 예외 요건 충족 및 사전승인 신청 적시성 판정
- **대응 방안**: 소프트웨어진흥법 제51조 기반 사전승인제 준수, 표준하도급계약서 작성 및 조달청 하도급지킴이 직불제 가동
- **검증 체계**: WBS 작업 패키지-형상관리 커밋 기록 간 실제 수행주체 교차 검증, 분기별 정기 현장 감리 점검
- **기대 효과**: 다단계 하도급 마진 누수 차단, 원수급자의 책임 완수 유도 및 중소 전문 SW 개발자의 정당한 처우 보장

<div class="itpe-pipeline is-vertical" role="img" aria-label="하도급 승인과 실제 수행의 일치 검증">
  <div class="itpe-flow-node"><strong>승인 Baseline</strong><div class="itpe-step-detail"><strong>대상</strong><span>범위·금액·조직·역할</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>수행 증거</strong><div class="itpe-step-detail"><strong>확인</strong><span>WBS·산출물·검수·지급</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>일치성 Gate</strong><div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>일치</strong><span>이행·대금 지급</span></div><div class="itpe-flow-branch"><strong>불일치</strong><span>시정·변경승인</span></div></div></div>
</div>

## 1교시 10점 답안 발췌

- **정의**: 공공 SW 사업의 하도급 비율·재하도급·사전승인을 통제하는 제도
- **목적**: 원수급인 책임 강화·다단계 하도급 방지·사업 품질 보호

| 통제 | 핵심 |
|---|---|
| 하도급 | 물품 구매금액 제외 SW 사업금액의 50% 초과 제한 |
| 재하도급 | 원칙적 제한·법정 예외 |
| 승인 | 계약 전 승인·승인 내용 이행관리 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [국가법령정보센터, 소프트웨어진흥법 제51조](https://www.law.go.kr/법령/소프트웨어진흥법/제51조)
- [국가법령정보센터, 소프트웨어진흥법 시행령 제48조](https://www.law.go.kr/법령/소프트웨어진흥법시행령/제48조)
- [국가법령정보센터, 소프트웨어사업 계약 및 관리감독에 관한 지침](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulId=33440&efYd=0)

## 학습 체크

- [ ] Ⅰ: 하도급 제한의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 50% 초과 제한의 산정 기준과 예외를 구분할 수 있는가?
- [ ] Ⅲ: 신청부터 이행관리까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅳ: 무단 하도급·형식적 승인에 대한 대책을 제시할 수 있는가?
- [ ] Ⅴ: 승인 내용과 실제 수행을 검증하는 통제안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [기술수용모델(TAM)](./092_technology_acceptance_model.md)
- 연관 토픽: [공공 SW 계약](./039_public_sw_contract.md), [적정 사업기간·과업심의](./091_public_sw_cost_and_scope_change_criteria.md)
- 다음 토픽: [전문성의 민주화](./098_democratization_of_expertise.md)

