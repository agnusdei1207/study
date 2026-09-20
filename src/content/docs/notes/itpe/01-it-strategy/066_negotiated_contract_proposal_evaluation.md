---
title: "협상에 의한 계약 제안서평가 세부기준"
author: "Antigravity"
date: "2026-09-20T19:32:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW 조달 및 계약 제도를 거쳐 협상에 의한 계약 제안서평가 세부기준으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 조달·계약 제도</span>
  <strong>협상에 의한 계약 제안서평가 세부기준</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **협상에 의한 계약 제안서평가 세부기준**은 공공 소프트웨어 사업자 선정 시 최저가 덤핑에 따른 부실화를 방지하고, **기술능력평가(80~90%)**와 **입찰가격평가(10~20%)**를 종합 심사하여 기술 우수 기업을 낙찰자로 선정하는 조달청 공식 계약 기준
- 메커니즘: `정량평가(재무/실적) + 정성평가(기술/관리)`를 거쳐 동점·근소 차이 방지를 위해 **차등점수제**를 적용하고, 가격 점수와 합산하여 1위 기업과 기술·과업 협상 진행
- 산출: 정량평가 채점표 · 정성 기술능력평가서 · 차등점수 산출표 · 우선협상대상자 결정서 · 기술협상 합의서

<div class="itpe-flow-map" role="img" aria-label="협상에 의한 계약 제안서 평가 및 낙찰 절차도">
  <div class="itpe-flow-node">
    <strong>입찰 공고 및 제안서 접수</strong>
    <small>e-발주시스템 접수 · 제안서 분량 상한제(200쪽)</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>종합 기술·가격 평가 (100점)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>기술(80~90점)</strong><span>정량(재무/실적 10~20점) + 정성(기술/관리 70~80점)</span></div>
      <div class="itpe-flow-branch"><strong>변별력 강화</strong><span><span class="itpe-keyword"><strong>차등점수제</strong></span> (순위별 고정 점수차 강제 부여)</span></div>
      <div class="itpe-flow-branch"><strong>가격(10~20점)</strong><span>기재부 평점산식 적용 · 80% 하한율 보장</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>우선협상대상자 선정 및 계약 체결</strong>
    <small>기술 협상 및 과업 확정 → 소프트웨어 제값주기 달성</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **협상에 의한 계약**: 다수의 입찰자로부터 제안서를 제출받아 기술과 가격을 종합 평가하여 협상을 통해 국가에 가장 유리한 사업자를 선정하는 계약 방식
- **기술능력평가**: 입찰자의 경영상태·수행실적을 보는 '정량평가'와 시스템 아키텍처·기능구현·사업관리 역량을 심사하는 '정성평가'의 합산 평가
- **차등점수제**: 기술평가 위원들의 점수 편차가 미미하여 저가 투찰자가 기술 1위를 역전하는 왜곡을 방지하고자, 순위별로 고정된 점수 차이를 강제 부여하는 제도
- **RFP(Request for Proposal)**: 발주기관이 입찰 참가자에게 요구하는 요구사항, 평가 기준, 계약 조건을 명시한 제안요청서
- **e-발주시스템**: 제안서 제출, 평가위원 자동 추첨, 온라인 평가 및 결과 공개 전 과정을 전자화한 조달청 공공 조달 플랫폼
- **PoC(Proof of Concept)**: 제안서에 명시된 핵심 아키텍처와 신기술의 구현 가능성을 사전에 실제 코드로 검증하는 기술 실증

</details>

## 예상문제

> 공정한 경쟁과 기술 중심 공공 SW 사업자 선정을 위해 개정된 '조달청 협상에 의한 계약 제안서평가 세부기준'의 주요 개정 내용, 기술능력평가의 정량·정성 평가 항목, 차등점수제의 도입 배경 및 실무 적용 효과, 평가위원의 전문성·공정성 확보 방안을 설명하시오. (25점)

## Ⅰ. 기술 중심 공공 조달과 공정 경쟁의 기준, 개요

> 협상에 의한 계약 제안서평가 세부기준은 공공 SW의 부실화를 방지하고 기술력 기반의 정당한 대가를 보장하는 조달 통제 장치이며, 성패는 **기술 변별력 확보(차등점수제)**와 **평가 투명성**으로 판정함.

- 정의: 공공 정보화 사업 등 전문성과 기술성이 요구되는 사업에서 기술능력(80~90%)과 입찰가격(10~20%)을 종합 심사하여 최적 사업자를 선정하는 **조달청 계약 평가 지침**
- 목적: 저가 덤핑 방지, 우수 IT 기업 선정 및 공정 경쟁 환경 조성

## Ⅱ. 제안서평가 세부기준 최근 개정 방향 및 평가 배점 체계

> 단순 가격 경쟁을 원천 차단하고 기술력 중심의 평가 체계로 제도를 고도화함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="협상에 의한 계약 종합 배점 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 기술능력평가 (80~90점)</strong></span>
    <div class="itpe-step-detail"><strong>평가 구성</strong><span>정량(신용등급, 실적) + 정성(방법론, 아키텍처, 기능 요구사항, WBS, 보안)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 기술 변별력 보정 : 차등점수제 적용</strong></span>
    <div class="itpe-step-detail"><strong>변별력 강화</strong><span>순위별 고정 점수차(0.5~3점) 강제 부여로 가격 점수 역전 현상 차단</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 입찰가격평가 (10~20점)</strong></span>
    <div class="itpe-step-detail"><strong>덤핑 방지</strong><span>기재부 계약예규 평점산식 적용 및 80% 미만 투찰 시 감점 체감 산식</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Fair Procurement Loop</strong></span> · 사전 제안서 분량 통제 ↔ 당일 위원 무작위 추첨 ↔ 차등점수 집계 ↔ 실명 공개</div>

### 최근 주요 개정 방향

| 개정 방향 | 주요 개정 내용 | 실무 기대 효과 |
|---|---|---|
| **기술 변별력 강화** | **차등점수제** 적용 기준 및 차등 폭 명문화 | 기술 1위 업체의 억울한 가격 역전 패배 방지 |
| **평가 공정성 제고** | 평가위원 당일 새벽 무작위 자동 추첨, 평가 결과 및 채점위원 실명 공개 | 사전 불법 로비 원천 차단 및 채점 책임성 확보 |
| **입찰 부담 완화** | 제안서 분량 상한제(예: 200페이지 이내) 및 요약서(50페이지) 의무화 | 제안서 '쪽수 늘리기' 경쟁 지양 및 작성 비용 절감 |
| **부정행위 감점 확대** | 불공정 행위, 사후 하도급 위반, 허위 기재 적발 시 감점 강화 | 공공 입찰 시장 질서 교란 행위 엄단 |

## Ⅲ. 기술능력평가 세부 구성요소 및 차등점수제 심층 분석

> 정량 심사는 객관적 재무 건전성을 보고, 정성 평가는 실제 시스템 구축 능력을 심사함.

| 평가 구분 | 평가 주체 | 주요 평가 세부 지표 | 배점 비중 예시 |
|---|---|---|---|
| **정량적 평가** | 조달청 / 발주기관 담당자 | 경영상태(신용평가등급), 최근 3개년 유사 실적, 중소기업 참여 가점 | 10점 ~ 20점 |
| **정성적 평가** | 전문 평가위원회 (외부위원 7~9인) | 개발 전략, 요구사항 분석, 아키텍처 설계, 프로젝트 관리, 품질보증, 보안 | 70점 ~ 80점 |
| **입찰 가격 평가** | 기획재정부 계약예규 산식 | 입찰가격이 추정가격의 80% 이상/미만 여부에 따른 체감 산식 | 10점 ~ 20점 |

### 차등점수제 도입 배경 및 동작 원리
- **도입 배경**: 평가위원들이 온정주의로 인해 1위와 2위 업체에 0.1~0.5점의 극소 편차만 부여할 경우, 가격 투찰에서 만점을 받은 덤핑 업체가 기술 1위 업체를 역전하여 낙찰받는 폐단 발생
- **동작 원리**: 기술평가 순위가 확정되면, 원점수와 무관하게 1순위는 만점(예: 80점), 2순위는 고정 차등폭 감점(예: 77점), 3순위는 74점 등으로 **순위별 고정 점수차를 강제 부여**하여 기술력 우수 업체의 수주를 제도적으로 보증

## Ⅳ. 적격심사 낙찰제 vs 협상에 의한 계약 비교

> 단순 규격품 구매와 고난도 소프트웨어 개발 사업은 낙찰자 선정 철학이 근본적으로 다름.

| 비교 항목 | 적격심사 낙찰제 | 협상에 의한 계약 |
|---|---|---|
| **주요 적용 대상** | 규격이 표준화된 상용 물품 구매, 단순 전산 소모품 | **소프트웨어 개발**, ISP/ISMP, 차세대 DX 컨설팅 |
| **낙찰자 결정 방식** | 예정가격 이하 **최저가 입찰자 순**으로 결격 사유 심사 | **기술(80~90%) + 가격(10~20%) 종합 1위**와 협상 |
| **기술 평가 방식** | 최소 기준 충족 여부(Pass/Fail) 위주 | 기술 제안서의 독창성, 아키텍처, 방법론 심층 채점 |
| **가격 경쟁 폐단** | 덤핑 투찰 가능성 상존 | 기술 점수 비중이 높아 기술력 우수 기업 절대 유리 |
| **협상 절차 유무** | 별도 과업 협상 없이 낙찰 즉시 계약 | 우선협상대상자와 제안 내용, 일정, 상세 과업 협상 |

## Ⅴ. 실무 평가 시 위험 요인 및 기술사적 대책

> 제안서의 겉포장이나 피티 전문 강사의 언변에 현혹되지 않도록 기술 중심의 실증 검증이 병행되어야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **기술 1위 업체의 가격 역전** | 순위별 고정 점수차를 부여하는 **차등점수제 의무화** | 기술 1위 업체의 최종 낙찰 성공률 보장 |
| **평가위원 사전 결탁 및 로비** | **e-발주시스템 당일 새벽 무작위 자동 추첨** 및 실명 공개 | 로비 접촉 원천 차단 및 위원별 채점 공정성 확보 |
| **제안서 허위 기재 및 과장** | 제안서 내용을 **계약서 강제 편입** 및 위반 시 부정당업자 제재 | 제안 기능의 실제 검수 일치율 100% 확보 |
| **전문 외주 발표자(피티 강사) 폐단** | **사업관리자(PM) 직접 발표 의무화** 및 기술 역량 심층 질의 | PM 실무 총괄 검증 및 제안서 허수 배제 |

## Ⅵ. 실증 검증(PoC) 기반 기술평가 전환 중심의 결론

> 문서 중심의 '페이퍼 제안서 평가'를 탈피하여, 실제 핵심 아키텍처와 코드를 검증하는 **PoC 라이브 실증 평가**로 진화해야 공공 소프트웨어 사업의 실패를 원천 차단할 수 있음.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 화려한 그래픽의 제안서와 전문 프리젠터의 유창한 발표는 개발 역량을 대변하지 못함. 제안서 분량을 대폭 줄이고 기술평가 배점의 일부를 '현장 라이브 PoC'와 '제안 PM의 아키텍처 심층 방어'로 전환하는 것이 공공 SW 성공의 지름길임.
- 나라면: 고난도 AI·빅데이터 사업 제안서 평가 기준에 `제안 발표 시 실제 샘플 데이터를 활용한 알고리즘 라이브 시연 및 깃허브(Git) 기반 코드 정적 분석 결과 제출`을 필수 항목으로 반영하도록 발주 기준을 수립하겠음.

### 실전 답안용 기술사적 제언

- 판정: 제안서 문서 분량보다 실제 수행 PM 역량 및 기술 실증성으로 판정
- 대안: **차등점수제 전면 적용** + **제안 PM 필수 발표** + **사전 PoC 라이브 시연 결합**
- 검증: 평가위원 실명제 감사 기록 · PM 직접 질의응답 충실도 평가 · 가격 역전 0건
- 효과: 덤핑 부실 사업자 배제 · 기술 우수 기업 정당 수주 및 공공 정보화 성공률 극대화

<div class="itpe-pipeline is-vertical" role="img" aria-label="기술 중심 제안서 평가 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>취약점</strong><span>온정주의 채점에 따른 가격 역전, 페이퍼 제안서 과장 및 외주 발표자 폐단</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>공정 평가</strong><span>차등점수제 강제화, 제안 PM 직접 발표 및 핵심 아키텍처 라이브 PoC 실사</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>목표 지표</strong><span>순위별 유의미한 점수차 확보 및 제안 내용의 계약서 100% 편입</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>가치 창출</strong><span>SW 제값주기 실현, 기술 우수 기업 선정 및 공공 정보화 품질 완성</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **협상에 의한 계약 제안서평가 세부기준**은 공공 정보화 사업에서 기술능력(80~90%)과 입찰가격(10~20%)을 종합 평가하여 최적 사업자를 선정하는 조달청 공식 계약 기준
- 목적: 최저가 덤핑 낙찰 폐단 극복, 공정 경쟁 확보 및 SW 품질 보증

### 2. 종합 평가 배점 및 차등점수제 체계

<div class="itpe-pipeline is-vertical" role="img" aria-label="제안서평가 종합 배점 체계 요약">
  <div class="itpe-pipeline-node">
    <strong>기술능력평가 (80~90점)</strong>
    <div class="itpe-step-detail"><strong>종합 심사</strong><span>정량(10~20점) + 정성(70~80점) 합산</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>차등점수제 적용</strong>
    <div class="itpe-step-detail"><strong>변별력 확보</strong><span>순위별 고정 점수차 부여로 가격 역전 차단</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>입찰가격평가 (10~20점)</strong>
    <div class="itpe-step-detail"><strong>가격 심사</strong><span>80% 하한선 평점산식 적용</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>우선협상대상자 결정</strong>
    <div class="itpe-step-detail"><strong>협상 체결</strong><span>종합 1위 업체와 기술 및 과업 협상</span></div>
  </div>
</div>

### 3. 핵심 통제

- **차등점수제**: 기술평가 편차가 작을 때 발생하는 저가 투찰자의 가격 역전을 방지하기 위해 순위별 고정 점수차를 강제 적용하여 기술 1위 업체 수주 보장
- **제안 PM 직접 발표**: 외주 전문 강사의 대리 발표를 금지하고, 실제 프로젝트를 총괄할 **PM(Project Manager)**이 직접 발표 및 기술 질의에 응답하도록 의무화

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 1교시: 조달청 협상에 의한 계약 제안서평가 세부기준 개정 주요 내용 및 기술평가 변별력 강화 방안
- 제124회 정보관리기술사 2교시: 공공 SW 사업 발주 체계 및 제안서 기술평가 기준
- 조달청, '협상에 의한 계약 제안서평가 세부기준 (조달청 지침 제2024호)'
- 기획재정부, '계약예규 협상에 의한 계약체결기준'

## 학습 체크

- [ ] 협상에 의한 계약의 기술능력평가와 입찰가격평가 배점 비중을 설명할 수 있는가?
- [ ] 기술평가 정량 항목과 정성 항목의 세부 평가 기준을 구분할 수 있는가?
- [ ] 차등점수제의 도입 배경과 산출 메커니즘을 설명할 수 있는가?
- [ ] 제안서평가 세부기준 개정의 4대 핵심 방향(변별력, 공정성, 부담 완화, 감점)을 논술할 수 있는가?

## 연결 토픽

- 이전 토픽: [프로젝트 관리](./065_project_management.md)
- 연관 토픽: [제안요청서(RFP)](./049_rfp.md), [공공 SW 사업 발주·계약](./039_public_sw_contract.md), [SW 사업 대가산정](./026_software_cost_estimation.md)
- 다음 토픽: [공공 소프트웨어 제값주기](./091_public_sw_cost_and_scope_change_criteria.md)
