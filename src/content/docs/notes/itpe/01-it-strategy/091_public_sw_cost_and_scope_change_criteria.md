---
title: "과업심의(과업변경·사업기간 적정성)"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW 사업 제도를 거쳐 과업심의로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 사업 제도</span>
  <strong>과업심의(과업변경·사업기간 적정성)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 공공 SW 사업의 비현실적 납기와 무상 과업 추가를 방지하기 위해 발주 전 **사업기간 적정성**과 수행 중 **과업변경**을 법적으로 심의하는 제도
- 메커니즘: 발주 전 공기 산정 검증(사전) → 변경 요청 발생 → **과업심의위원회** 의결(경미/중대) → **FP(기능점수)** 재산정 및 계약 변경(금액·기간 조정)
- 산출: 적정 사업기간 검토서 · 과업변경 요청서 · 과업심의 의결서 · 변경계약서

<div class="itpe-flow-map" role="img" aria-label="발주 전 사업기간 적정성 심의에서 사업 수행 중 과업변경 심의 및 계약금액 조정으로 이어지는 흐름">
  <div class="itpe-flow-node">
    <strong>사전 통제: 사업기간 적정성 심의</strong>
    <div class="itpe-step-detail"><span>발주 전 입찰공고 단계 · 법정 개발 공기 산출식 검증</span></div>
  </div>
  <div class="itpe-flow-arrow">↓<small>계약 체결 및 사업 착수</small></div>
  <div class="itpe-flow-node is-current">
    <strong>사후 통제: 과업심의위원회 (SW진흥법 제50조)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>구성</strong><span>외부 민간 전문가 과반수 (기술사·교수 등)</span></div>
      <div class="itpe-flow-branch"><strong>판정</strong><span>경미한 변경(무상) vs 중대한 과업 변경(유상)</span></div>
      <div class="itpe-flow-branch"><strong>신청</strong><span>발주기관 의무 및 수급 사업자 직접 청구권</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>의결 집행</small></div>
  <div class="itpe-flow-node">
    <strong>계약 변경 및 대가 증액</strong>
    <div class="itpe-step-detail"><span><span class="itpe-keyword"><strong>FP 재산정</strong></span> 계약금액 증액 + <span class="itpe-keyword"><strong>CPM</strong></span> 공기 연장</span></div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **소프트웨어 진흥법 제50조**: 공공 SW사업의 과업내용 변경 및 계약금액·기간 조정을 객관적으로 심의하기 위한 과업심의위원회 설치·운영 법적 조항
- **사업기간 적정성 심의**: 발주 전 사업 규모(FP), 구현 난이도, 행정 절차 등을 종합 고려하여 사업기간의 타당성을 심의하는 제도(소프트웨어 진흥법 제45조)
- **과업변경 심의**: 사업 수행 중 요구사항 변동 발생 시 타당성, 경미 여부, 계약금액 증액 및 공기 연장을 의결하는 심의
- **FP(Function Point)**: 소프트웨어 기능 규모를 객관적으로 측정하여 변경에 따른 추가 계약금액을 산정하는 기준
- **CPM(Critical Path Method)**: 주공정상의 지연 일수를 정량 분석하여 추가 개발 공기를 과학적으로 산정하는 기법
- **RTM(Requirements Traceability Matrix)**: 제안요청서 대비 변경된 요구사항의 형상과 영향을 추적하는 매트릭스
- **수급인 직접 청구권**: 발주자가 심의위 개최를 회피할 경우 수급 사업자가 직접 과업심의위 소집을 요구할 수 있는 법적 권리

</details>

## 예상문제

> 공공 SW 사업에서 빈번히 발생하는 과업 변경 및 불합리한 사업 기간 단축을 방지하기 위한 과업심의위원회 제도의 법적 근거, 사업기간 적정성 심의와 과업변경 심의의 절차 및 기준, 계약금액 조정 방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 키워드 | 등급 | 역할 및 핵심 내용 |
|---|---|---|
| **01-095 사업 기간 적정성·과업 변경 심의** | C | 발주 전 사업기간 산정 적정성 검증(SW진흥법 제45조)과 수행 중 과업 변경 심의(제50조)의 통합 절차 및 산출물 |

## Ⅰ. 공공 SW 제값 받기와 공기 보장의 핵심, 과업심의의 개요

> 발주 전 **사업기간 적정성**을 사전 검증하고, 수행 중 **과업변경 심의**를 통해 **FP(Function Point)** 기반 대가 증액과 공기 연장을 법적으로 보장함.

- 정의: **소프트웨어 진흥법 제50조**에 근거하여 발주 전 개발 공기의 타당성을 검증하고, 사업 수행 중 과업 변경 발생 시 객관적으로 타당성을 심의하여 계약금액 및 기간 조정을 의결하는 **공공 SW 법정 심의 제도**
- 목적: 무상 과업 추가 방지, 적정 개발 공기 확보 및 소프트웨어 품질·안전성 확보

## Ⅱ. 과업심의위원회 구성 및 5단계 심의 절차

> 외부 전문가 과반수로 구성된 위원회가 요청부터 영향도 분석, 의결, 변경계약까지 표준화된 파이프라인으로 처리함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 SW 과업심의 5단계 처리 프로세스">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>① 과업변경 요청</strong><span>법령 개정, 정책 변경, 상세 요구사항 도출에 따른 변경 요청 → 과업변경 요청서 (발주자 또는 수급 사업자 제출)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>② 영향도 분석</strong><span>증감 기능점수(FP) 측정, 아키텍처 영향도, 공기 지연 분석 → 영향도 분석서 · FP 증감표 · CPM 일정 분석서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>③ 과업심의위원회 개최</strong><span>외부 전문가 과반수 구성 위원회 소집 및 안건 심의 → 타당성 평가 · 경미/중대 판정 · 추가 예산/공기 심의</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>④ 심의결과 통보</strong><span>접수 후 14일 이내 심의 의결 결과를 수급인에게 서면 통보 → 과업심의 의결서 · 심의결과 통보서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>⑤ 공식 계약 변경</strong><span>국가계약법/지방계약법에 따른 계약금액 증액 및 공기 연장 → 수정 계약서 체결 · 추가 대가 정산</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>심의 구속력</strong></span> · 과업심의 의결서 ↔ 국가계약법 수정계약 ↔ 대가 증액 100% 반영 의무</div>

## Ⅲ. 사업기간 적정성 심의 vs 과업변경 심의 비교

> 발주 전에는 비현실적 납기 단축을 막고, 사업 착수 후에는 무상 과업 추가를 차단하는 사전·사후 2중 통제선 역할을 수행함.

| 구분 | 사업기간 적정성 심의 | 과업변경 심의 |
|---|---|---|
| **법적 근거** | **소프트웨어 진흥법 제45조**, 사업기간 산정 가이드 | **소프트웨어 진흥법 제50조**, SW사업 계약편집요령 |
| **심의 시점** | 사업 발주 전 (입찰 공고 전 사전 의무 심의) | 사업 수행 중 (요구사항 추가·변경 발생 시 수시) |
| **심의 대상** | 사업 규모 대비 개발 공기 타당성, 휴일/테스트 기간 반영 | 과업 변경의 타당성, 경미/중대 판정, 금액 및 공기 조정 |
| **신청 주체** | 발주기관 (의무 사항) | 발주기관 또는 수급 사업자 (**수급인 직접 청구권**) |
| **의결 효력** | 부적정 시 사업기간 재산정 후 입찰 공고 | 의결 결과에 따른 계약 변경(금액 증액, 기간 연장) 강제 |
| **핵심 도구** | 개발공기 산정 공식 ($공기 = C \times FP^{0.32}$) | 증감 **FP(기능점수)** 재산정 및 **CPM** 주공정 일정 분석 |

## Ⅳ. 경미한 과업 변경 vs 중대한 과업 변경 판정 기준

> 기능점수 증가와 구조적 변경 여부에 따라 대가 지급 의무가 판정되므로 객관적 기준이 필수적임.

| 구분 | 경미한 과업 변경 | 중대한 과업 변경 |
|---|---|---|
| **개념 정의** | 기본 아키텍처나 DB 구조 변동 없이 단순 UI 문구·배치 보완 | 신규 비즈니스 로직 추가, DB 엔티티 신설, 외부 연계 인터페이스 신설 |
| **기능점수(FP)** | 데이터 및 트랜잭션 기능점수 변동 없음 (0 FP) | **데이터/트랜잭션 기능점수 유의미하게 증가 (ΔFP > 0)** |
| **계약금액 조정** | 계약금액 변동 없음 (통상 하자보수 및 상호 협의) | **FP 재산정에 따른 계약금액 증액 의무 발생** |
| **사업기간 영향** | 기존 공기 내 소화 가능 (공기 연장 없음) | **CPM** 분석 결과에 따라 추가 개발 및 테스트 기간 연장 |
| **처리 절차** | 사업관리자(PM) 간 서면 합의로 신속 처리 가능 | **과업심의위원회 공식 안건 상정 및 의결 필수** |

## Ⅴ. 과업심의 실효성 확보를 위한 기술사적 제언

> 발주처의 심의위 개최 기피를 방지하기 위해 예비비 사전 확보와 요구사항 확정 게이트웨이를 강제해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 과업심의위원회가 법률로 제정되었음에도 현장에서 작동하지 못하는 근본 원인은 '심의를 열어 증액을 의결해도 발주처에 줄 돈(예산)이 없기' 때문임. 예비비가 없으면 발주자는 감사를 두려워해 개최 자체를 묵살함.
- 나라면: 기획재정부 총사업비 관리지침을 개정하여 공공 SW 사업 예산 편성 시 '과업변경 예비비(낙찰차액 등 10%)' 편성을 의무화하고, 착수 3개월 시점에 '요구사항 동결(Scope Freeze) 마일스톤'을 두어 이후 모든 변경은 과업심의위를 자동 경유하도록 시스템화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 발주처 선의에 기댄 운영에서 예산 편성 및 마일스톤 기반 자동 심의 체계로 전환
- 대안: **과업변경 예비비(10%) 사전 편성 제도화** 및 **요구사항 동결 게이트웨이** 도입
- 검증: 수급인 심의 청구 접수율 100% · 접수 후 14일 이내 의결 이행률 100%
- 효과: 무상 과업 추가 관행 완전 근절 · 적정 대가 보장 및 공공 SW 품질 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="과업심의 실효성 확보를 위한 기술사적 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>현행 한계</strong><span>추가 예비비 미확보로 심의위 개최 기피 · 사업자의 무상 야근 감내</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>개선 대안</strong><span>총사업비 내 10% 과업변경 예비비 의무화 + 착수 후 Scope Freeze 게이트</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>검증 기준</strong><span>수급인 직접 청구권 보장 · RTM 기반 변경 전후 형상 및 FP 전수 감사</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>실행 효과</strong><span>무상 과업 근절 · 정당한 대가 지급 및 공공 SW 시스템 안정성 제고</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **소프트웨어 진흥법 제50조**에 따라 발주 전 적정 공기를 검증하고, 수행 중 과업 변경 시 **FP(Function Point)** 기반 계약금액 및 기간 조정을 심의·의결하는 **법정 심의 제도**
- 목적: 불합리한 공기 단축 및 무상 과업 추가 방지, 공정 계약 질서 확립 및 공공 SW 품질 보장

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="과업심의 2단계 연계 체계 요약">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>사전: 사업기간 적정성</strong><span>발주 전 공기 공식 검증 (SW진흥법 제45조)</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>수행: 변경 영향도 분석</strong><span>증감 FP 측정 · CPM 공기 지연 분석</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>사후: 과업심의위 의결</strong><span>외부 전문가 과반수 · 계약금액/기간 조정</span></div></div>
</div>

### 3. 핵심 통제

- **수급인 직접 청구권**: 발주자의 심의 회피를 방지하고 사업자가 직접 심의위원회 소집 청구 가능
- **계약 변경 강제**: 의결 결과에 따라 국가계약법상 계약금액 증액 및 공기 연장 집행 의무화

## 출제 이력과 검증 출처

- 제128회 KPC 모의고사 1교시: 공공 SW 사업 과업심의위원회의 역할 및 심의 기준
- 제124회 정보관리기술사 기출 유사: 소프트웨어 과업변경 및 계약금액 조정 제도
- [과학기술정보통신부, 소프트웨어 진흥법 제45조(소프트웨어사업의 적정 사업기간 산정 등) 및 제50조(소프트웨어사업 과업내용의 변경)](https://www.law.go.kr)
- [한국소프트웨어산업협회(KOSA), SW사업 대가산정 가이드](https://www.sw.or.kr)

## 학습 체크

- [ ] 사업기간 적정성 심의와 과업변경 심의의 시점 및 법적 근거를 설명할 수 있는가?
- [ ] 과업심의위원회의 위원 구성 자격기준과 수급인의 직접 청구권을 숙지하고 있는가?
- [ ] 경미한 과업 변경과 중대한 과업 변경의 판정 기준 및 대가 산정 메커니즘을 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [TAM-SAM-SOM](./089_tam_sam_som.md)
- 연관 토픽: [SW 분리발주 및 계약제도](./039_public_sw_contract.md), [소프트웨어 비용 산정](./113_software_cost_estimation.md)
- 다음 토픽: [기술수용모델(Technology Acceptance Model)](./092_technology_acceptance_model.md)
