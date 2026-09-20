---
title: "소프트웨어산업진흥법 하도급 구조"
author: "Antigravity"
date: "2026-09-20T19:32:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW 사업 제도를 거쳐 소프트웨어산업진흥법 하도급 구조로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 사업 제도</span>
  <strong>소프트웨어산업진흥법 하도급 구조</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 공공 SW 사업의 턴키 수주 후 다단계 하청 관행을 근절하기 위해 **직접수행 의무(50% 이상)**와 **재하도급 금지**를 법적으로 강제하는 제도
- 메커니즘: 하도급 사전 승인 신청 → 적정성 심사(85점 이상, 대가 82% 보장) → 승인 통보 → **하도급지킴이** 기반 대금 직불
- 산출: 하도급 계약 계획서 · 하도급 적정성 심사결과서 · 사전 승인서 · 전자 직불 이체 내역서

<div class="itpe-flow-map" role="img" aria-label="공공 SW 사업 하도급 50% 직접수행 의무 및 재하도급 금지 구조">
  <div class="itpe-flow-node">
    <strong>공공 발주기관</strong>
    <div class="itpe-step-detail"><span>원도급 계약 체결 · 하도급 적정성 사전 심사</span></div>
  </div>
  <div class="itpe-flow-arrow">↓<small>원도급 계약</small></div>
  <div class="itpe-flow-node is-current">
    <strong>원수급인 (주사업자)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>직접수행</strong><span><span class="itpe-keyword"><strong>50% 이상 의무</strong></span> (주공정 및 핵심 아키텍처)</span></div>
      <div class="itpe-flow-branch"><strong>하도급 한도</strong><span>50% 이내 제한 + 발주처 사전승인 필수</span></div>
      <div class="itpe-flow-branch"><strong>대가 보장</strong><span>원도급 대비 82% 이상 대가 지급 의무</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>1차 하도급 계약 (사전승인 必)</small></div>
  <div class="itpe-flow-node">
    <strong>하수급인 (1차 협력업체)</strong>
    <div class="itpe-step-detail"><span>❌ 재하도급 원칙적 금지 (신기술·특수장비 극히 예외적 허용)</span></div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **소프트웨어 진흥법 제51조**: 공공 소프트웨어 사업의 50% 초과 하도급 금지, 재하도급 제한, 발주처 사전승인을 규정한 핵심 법적 조항
- **직접수행의무(50% 룰)**: 원수급자가 사업금액의 100분의 50을 초과하여 하도급할 수 없도록 규정한 강행 규정
- **재하도급 제한**: 하수급인이 도급받은 사업을 제3자에게 다시 하도급하는 것을 원칙적으로 금지하여 피라미드식 하청을 차단하는 제도
- **하도급 적정성 심사**: 하도급 계약 체결 전 발주기관이 하도급 대금 비율(82% 이상)과 기술 능력을 종합 평가하여 85점 이상 시 승인하는 절차
- **하도급지킴이**: 조달청이 운영하는 공공 SW 사업 하도급 대금 전자 지급 및 실시간 모니터링 시스템
- **위장도급**: 실질적인 프리랜서 인력 파견임에도 불구하고 도급 계약 형식으로 위장하여 50% 직접수행 룰을 회피하는 불법 관행

</details>

## 예상문제

> 소프트웨어 진흥법 상 공공 소프트웨어 사업의 다단계 하도급 제한 규정, 하도급 사전승인 제도의 심사 기준과 절차, 실무적 위장도급 문제점 및 해결 방안을 설명하시오. (25점)

## Ⅰ. 건전한 SW 산업 생태계 확립의 축, 하도급 규제의 개요

> 대형 SI 기업의 통행세 착복과 다단계 피라미드 하청을 차단하기 위해 **50% 이상 직접수행**과 **재하도급 금지**를 법적으로 강제함.

- 정의: **소프트웨어 진흥법 제51조**에 따라 공공 SW 사업 수주 시 50%를 초과한 하도급을 금지하고, 재하도급을 원칙적으로 금지하며 사전에 발주자 승인을 받도록 규정한 **공공 SW 상생 및 품질 보호 제도**
- 목적: 중소 SW 기업 적정 대가 보장, 원수급자 직접수행 책임성 강화 및 부실 구축 방지

## Ⅱ. SW진흥법 하도급 규제 4대 원칙 및 4단계 운영 절차

> 사전 계획서 제출부터 85점 이상 적정성 심사, 승인 통보, 하도급지킴이 직불로 이어지는 통제 파이프라인을 가동함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="SW진흥법 하도급 사전승인 및 대금지급 4단계 절차">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>① 하도급 사전 신청</strong><span>사업 착수 전/후 하도급 계약 계획서, 산출내역서, 협력사 자격 증빙 제출 → 하도급 계획서 · 계약서(초안)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>② 하도급 적정성 심사</strong><span>심사위원회 구성, 대가 비율(82% 룰) 및 기술 인력 역량 계량 평가 → 적정성 평가표 (85점 이상 승인 기준)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>③ 승인 여부 서면 통보</strong><span>접수일로부터 14일 이내 승인, 불승인, 조건부 보완 서면 통보 → 하도급 사전승인 통보서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>④ 계약 체결 및 직불 집행</strong><span>전자계약 체결 및 조달청 '하도급지킴이' 시스템 등록 후 대금 직불 → 기성 대금 전자이체 영수증</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>상생 추적성</strong></span> · 원도급 계약금액 ↔ 하도급 심사 대가율(≥82%) ↔ 하도급지킴이 직불 100% 매핑</div>

### 하도급 규제 4대 핵심 원칙

| 규제 원칙 | 법적 근거 (SW진흥법) | 세부 법적 기준 | 실무 적용 시 유의점 |
|---|---|---|---|
| **50% 초과 하도급 금지** | 제51조 제1항 | 사업금액의 100분의 50을 초과하여 하도급 불가 (**원수급자 50% 이상 직접수행**) | 단순 하드웨어/상용SW 물품 구매액은 모수에서 제외 가능 |
| **재하도급 원칙적 금지** | 제51조 제2항 | 하수급인은 도급받은 SW 사업을 다른 제3자에게 다시 하도급할 수 없음 | 피라미드식 다단계 하도급 원천 차단 |
| **재하도급 예외적 허용** | 시행령 제48조 | 신기술(AI/클라우드), 특수 장비 연계, 상용SW 패키징 등 법정 사유 한정 | 발주처 서면 승인 및 기술적 불가피성 입증 필수 |
| **발주자 사전 승인 의무** | 제51조 제5항 | 하도급 계약 체결 전 발주기관에 계획서를 제출하고 적정성 승인 획득 | 무단 하도급 시 부정당업자 제재 및 계약 해제 사유 |

## Ⅲ. 하도급 적정성 심사 기준 및 직접수행 vs 재하도급 비교

> 하도급 대금 후려치기를 방지하기 위한 정량 평가와 기술 역량 심사를 결합함.

### 1. 하도급 계약 적정성 심사 기준 (100점 만점, 85점 이상 승인)

| 심사 항목 | 배점 | 세부 심사 기준 | 통제 지표 |
|---|---|---|---|
| **하도급 대금의 적정성** | 60점 | 원도급 대금 대비 하도급 대금 지급 비율 | **원도급 대가의 82% 이상 지급 시 만점 (82% 미만 시 감점)** |
| **하수급인의 사업수행능력** | 30점 | 유사 사업 수행 실적, 투입 인력 기술 등급 및 전문성 | 전문 개발 역량 및 포트폴리오 적합성 |
| **하도급 계약 공정성** | 10점 | 표준하도급계약서 사용 여부, 대금 지급보증서 발급 | 불공정 특약 부존재 및 지급보증 완료 |

### 2. 직접수행 의무(50% 룰) vs 예외적 재하도급 비교

| 비교 항목 | 직접수행 의무 (50% 룰) | 예외적 재하도급 허용 |
|---|---|---|
| **제도 취지** | 무책임한 턴키 전매 및 통행세 착복 차단 | 특수 신기술 부재로 인한 사업 중단 방지 |
| **원칙적 성격** | 법률상 강행 규정 (위반 시 입찰 참가자격 제한) | 원칙적 금지, 극히 제한적 예외 승인 |
| **허용 사유** | SW 개발비 전체를 기준으로 50% 이상 직접 공정 수행 | AI/빅데이터 알고리즘, 특수 임베디드, 솔루션 커스터마이징 |
| **통제 방식** | 제안서 및 사업계획서 상 직접수행 계획 명시 | 발주처 사전 타당성 심의 및 승인 공문 확보 |

## Ⅳ. 실무 적용 시 왜곡 요인 및 통제 대책

> 프리랜서 위장도급과 대금 지연 문제를 극복하기 위해 직접 고용 검증과 시스템 기반 직불제를 강화해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **프리랜서 위장도급 만연** | 4대 보험 가입 증빙 기반 정규 상주 인력 검증 및 원도급자 직접 근로계약 의무화 | 불법 파견 근절 및 개발자 근로조건 보호 |
| **하도급 대금 지연·체불** | 조달청 **'하도급지킴이'**를 통한 대금 직불 및 금융권 에스크로 계좌 결제 의무화 | 대금 체불 원천 차단 |
| **형식적 하도급 사전승인** | 외부 감리법인을 통한 '하도급 계약 적정성 사전 감리 검증제' 의무화 | 하도급 심사의 객관성 및 품질 담보 |

## Ⅴ. 하도급 투명성 확보를 위한 기술사적 제언

> 외주 금액 비율 규제를 넘어 Git 형상관리 기반 개발 실명제를 연계해야 진정한 하도급 투명성이 실현됨.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 50% 하도급 규제는 중소기업을 보호하기 위해 도입되었으나, 현장에서는 대형 SI사가 페이퍼컴퍼니나 파견업체를 통해 프리랜서를 도급으로 둔갑시키는 '위장도급의 일상화'를 낳았음. 돈의 흐름만 통제해서는 실제 누가 개발했는지 알 수 없음.
- 나라면: 하도급 관리의 통제 축을 '회계 계약서'에서 'Git 형상관리 기반 소프트웨어 개발 실명제(Contribution Attribution)'로 전환하여, 소스코드 커밋 작성자의 소속과 하도급 승인 명단을 매핑하고, 조달청 하도급지킴이 API와 금융 결제를 연동하여 실제 기여 개발자에게 대금이 직불되도록 설계하겠음.

### 실전 답안용 기술사적 제언

- 판정: 계약서 중심의 형식적 검토에서 소스코드 개발 실명제 및 금융 API 직불로 전환
- 대안: **Git 커밋 기반 SW 개발 실명제** 및 **하도급지킴이 전산 직불 자동화**
- 검증: 하도급 대가 82% 이상 보장률 100% · Git 커밋-승인 명단 일치율 100%
- 효과: 위장도급 완전 근절 · 하도급 대금 체불 제로화 및 공공 SW 품질 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="하도급 투명성 확보를 위한 기술사적 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>현행 한계</strong><span>계약서 서류상 50% 준수 · 현장 프리랜서 편법 위장도급 만연</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>개선 대안</strong><span>Git 커밋 기반 개발 실명제 + 하도급지킴이 금융 API 연계 직불</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>검증 기준</strong><span>원도급 대가 82% 심사 통과 · 감리법인의 하도급 사전검증 100%</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>실행 효과</strong><span>피라미드식 하청 착취 근절 · 중소 SW 전문기업 적정 대가 보장</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **소프트웨어 진흥법 제51조**에 따라 사업금액의 50% 이상 원수급자 직접 수행, 재하도급 원칙적 금지, 발주자 사전승인을 강제하는 **공공 SW 하도급 규제 제도**
- 목적: 대금 후려치기 차단, 중소 전문기업 적정 대가 및 공공 SW 품질 보장

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="하도급 규제 구조 요약">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>원수급자</strong><span>50% 이상 직접수행 (주공정 아키텍처)</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>사전승인</strong><span>대가 82% 이상 · 적정성 평가 85점 이상</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>1차 하도급</strong><span>50% 이내 수행 · ❌ 재하도급 원칙 금지</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>하도급지킴이</strong><span>조달청 시스템 기반 대금 직접 지급</span></div></div>
</div>

### 3. 핵심 통제

- **82% 대가 보장**: 원도급 대금 대비 82% 이상을 하수급인에게 지급해야 사전승인 통과
- **직불제 의무화**: 조달청 하도급지킴이를 통한 발주처 직접 이체로 임금 체불 원천 방지

## 출제 이력과 검증 출처

- 제124회 KPC 모의고사 1교시: 공공 SW 사업의 하도급 제한 규정 및 사전승인 심사 기준
- [과학기술정보통신부, 소프트웨어 진흥법 제51조(하도급 제한 등) 및 시행령 제48조](https://www.law.go.kr)
- [조달청, 공공SW사업 하도급지킴이 이용 및 대금지급 관리지침](https://www.pps.go.kr)

## 학습 체크

- [ ] SW진흥법 제51조의 하도급 4대 핵심 원칙을 설명할 수 있는가?
- [ ] 하도급 계약 적정성 심사의 82% 룰과 85점 합격 기준을 숙지하고 있는가?
- [ ] 프리랜서 위장도급 문제를 방지하기 위한 공학적 해결 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [기술수용모델(Technology Acceptance Model)](./092_technology_acceptance_model.md)
- 연관 토픽: [과업심의(과업변경·사업기간 적정성)](./091_public_sw_cost_and_scope_change_criteria.md), [SW 비용 산정](./113_software_cost_estimation.md)
- 다음 토픽: [전문성의 민주화(Democratization of Expertise)](./098_democratization_of_expertise.md)
