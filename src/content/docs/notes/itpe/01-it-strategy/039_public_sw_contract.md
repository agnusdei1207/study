---
title: "공공 SW 사업 발주·계약"
author: "Codex"
date: "2026-09-20T19:34:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW 정책과 계약 제도를 거쳐 공공 SW 사업 발주·계약으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 정책·계약 제도</span>
  <strong>공공 SW 사업 발주·계약</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **공공 SW 사업 발주·계약**은 요구사항 불명확성과 저가 덤핑 투찰을 근절하기 위해 분석·설계와 개발을 분리하는 **단계별 발주**와 기술 변별력을 강화하는 **차등점수제**를 적용하는 법정 공공 조달 체계
- 메커니즘: 1단계 기획·설계 발주로 상세 요구사항과 기능점수(**FP**)를 확정한 후, 2단계 본개발에서 **기술 90% : 가격 10%** 및 차등점수제로 우수 사업자를 선정하여 계약 체결
- 산출: 상세 제안요청서(**RFP**) · 기능점수 산정서 · 과업심의위원회 의결서 · 기술협상서 및 공정 계약서

<div class="itpe-flow-map" role="img" aria-label="공공 SW 사업 단계별 발주 및 차등점수제 업체 선정 흐름">
  <div class="itpe-flow-node">
    <strong>1단계: 기획·설계 분리 발주</strong>
    <small>ISMP · 요구사항 상세화 · 아키텍처 설계</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>정밀 기능점수(FP) 및 상세 RFP 확정</small></div>
  <div class="itpe-flow-node is-current">
    <strong>2단계: 본개발 발주 및 제안평가</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>제도</strong><span><span class="itpe-keyword"><strong>단계별 발주</strong></span>(설계·개발 분리) · 과업심의위원회</span></div>
      <div class="itpe-flow-branch"><strong>평가</strong><span>기술 90% : 가격 10% 확대 · <span class="itpe-keyword"><strong>차등점수제</strong></span> 적용</span></div>
      <div class="itpe-flow-branch"><strong>협상</strong><span>우선협상대상자 선정 · 요구사항 과업 기준선 확정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>공정 계약 체결 및 개발 착수</small></div>
  <div class="itpe-flow-node">
    <strong>공공 SW 품질 및 납기 완수</strong>
    <small>과업 변경 분쟁 차단 · 정당 대가 지급 · SW 생태계 정상화</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **공공 SW 사업 발주·계약**: 소프트웨어 진흥법에 의거하여 요구사항을 구체화하고 적정 대가와 기술 중심 선정을 보장하는 공공 조달 체계
- **단계별 발주(분할발주)**: 분석·설계(1단계)와 시스템 구현(2단계)을 별도 사업으로 분리 발주하여 요구사항 모호성을 사전 해소하는 제도
- **차등점수제**: 기술능력평가 시 심사위원 점수 인플레이션(0.1점 차)으로 인한 저가 덤핑 낙찰을 방지하기 위해 기술 순위별로 고정 점수차(0.5~3점)를 강제 부여하는 제도
- **협상에 의한 계약**: 다수의 입찰자로부터 제안서를 제출받아 기술과 가격을 종합 평가하고 우선협상대상자와 협상을 거쳐 계약하는 방식
- **과업심의위원회**: 공공 SW 사업의 사업기간 적정성 심의 및 사업 추진 중 과업 변경 여부와 계약금액 조정을 법적으로 의무 심의하는 위원회
- **FP(Function Point)**: 소프트웨어의 논리적 기능 규모를 측정하여 개발 대가와 일정을 산정하는 기준
- **RFP(Request for Proposal)**: 발주기관이 입찰 참가자에게 사업 범위, 상세 요구사항, 제안서 작성 기준을 제시하는 제안요청서
- **헤드카운팅(Head-counting)**: 소프트웨어 사업 대가를 투입 인력의 등급과 머릿수(M/M)로 산정하거나 현장 출근을 강제하는 구태 관행
- **PoC(Proof of Concept)**: 1단계 설계에서 도출된 신기술이나 아키텍처의 실현 가능성을 사전 시제품으로 실증하는 절차

</details>

## 예상문제

> 공공 소프트웨어 사업의 요구사항 불명확과 저가 덤핑 문제를 해결하기 위한 발주·계약 제도 개선방안(단계별 발주, 기술평가 90:10 확대, 차등점수제, 과업심의위원회)을 설명하고, 실무 적용 시의 한계점과 극복 대책을 논하시오. (25점)

## Ⅰ. 공공 SW 품질 확보와 생태계 정상화를 위한 발주·계약 제도의 개요

> 공공 SW 발주·계약 제도는 모호한 RFP로 인한 잦은 과업 변경과 저가 투찰을 방지하는 법정 장치이며, 성패는 **요구사항 상세화**와 기술 우수 사업자를 보호하는 **차등점수제**의 실효적 작동으로 판정함.

- 정의: 공공 정보화 사업 추진 시 요구사항을 사전에 상세화하고 기술 우수 사업자가 정당한 대가를 받도록 보장하는 **소프트웨어 진흥법** 기반의 **공공 조달 및 계약 체계**
- 목적: **단계별 발주** 기반 요구사항 확정 및 **차등점수제** 적용 기술 변별력 확보 → 잦은 과업 변경과 저가 덤핑 근절 및 납기·품질 보증

## Ⅱ. 공공 SW 발주·계약 혁신의 4대 핵심 제도 체계

> 4대 제도가 상호 결합하여 범위 고정과 기술 중심 낙찰을 실현함.

| 핵심 제도 | 법적 근거 및 주요 내용 | 도입 목적 및 기대 효과 |
|---|---|---|
| **단계별 발주 (분할발주)** | SW 진흥법 제44조 / 분석·설계(1단계)와 구현·검수(2단계) 분리 | 요구사항 미확정 상태의 조기 개발 착수 방지 및 과업 변경 최소화 |
| **협상에 의한 계약** | 국가계약법 시행령 제43조 / 기술평가와 가격평가 종합 합산 | 단순 최저가 낙찰을 배제하고 기술력과 가격을 종합 협상 |
| **기술평가 비중 확대** | 기술 90% : 가격 10% (기존 80:20에서 기술평가 비중 상향) | 저가 덤핑 입찰자의 가격 우위 왜곡 차단 |
| **차등점수제** | 조달청 협상에 의한 계약 세부기준 / 순위별 고정 점수차(0.5~3점) 부여 | 심사위원 점수 인플레이션(0.1점 차) 무력화 및 기술 우위 사업자 낙찰 |

## Ⅲ. 단계별 발주 및 업체 선정 아키텍처

> 1단계 설계에서 상세 요구와 FP를 뽑아 2단계 RFP에 담고, 차등점수제로 본개발사를 선정함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 SW 단계별 발주 및 제안평가 프로세스 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 1단계: 기획·설계 발주 및 과업심의</strong></span>
    <small>ISMP 수립 · 사업기간 적정성 심의 · 분할발주 확정<br />→ 과업심의위원회 의결서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 요구사항 상세화 및 아키텍처 설계</strong></span>
    <small>화면·DB 설계 · 기능점수(FP) 정밀 산정 · 상세 RFP 확정<br />→ 상세 요구사항 명세서 · FP 산정서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 2단계: 본개발 입찰 공고</strong></span>
    <small>상세 RFP 첨부 · 나라장터 사전 규격 공개(5일 이상)<br />→ 입찰 공고문 · 제안요청서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 제안서 평가 및 차등점수제 적용</strong></span>
    <small>기술능력평가(90%) + 입찰가격평가(10%) · 순위별 고정 격차 부여<br />→ 기술평가 결과표 · 우선협상대상자 선정</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 기술협상 및 최종 계약 체결</strong></span>
    <small>과업 범위 기준선 확정 · 기술협상 수행 · SLA 체결<br />→ 기술협상록 · 최종 계약서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Scope Traceability</strong></span> · 1단계 설계 산출물이 2단계 RFP로 100% 반영되고 기술 우수 기업이 최종 낙찰</div>

## Ⅳ. 일괄 발주 vs 단계별(분할) 발주 비교

> 일괄 발주가 행정 편의적인 반면, 단계별 발주는 요구사항 변경 리스크를 사전에 제거함.

| 비교 항목 | 일괄 발주 방식 (Turn-key) | 단계별 분할 발주 방식 (설계·개발 분리) |
|---|---|---|
| 발주 형태 | 분석, 설계, 구현, 검수를 단일 사업자에게 일괄 위탁 | 1단계(분석·설계)와 2단계(구현·검수)를 분리 발주 |
| 요구사항 확정도 | RFP 공고 시점에 요구사항이 추상적이고 모호함 | 1단계 종료 시점에 화면, DB, 상세 기능이 100% 확정됨 |
| 과업 변경 위험 | 개발 진행 중 잦은 과업 변경 및 분쟁 빈발 | 2단계 본개발 착수 시 과업 변경 요인이 최소화됨 |
| 책임 소재 | 단일 주사업자가 전체 수명주기 책임 (명확함) | 설계 사업자와 개발 사업자 간 책임 전가 위험 잔존 |
| 발주 행정 소요 | 1회의 입찰 및 계약으로 행정 절차 간소 | 2회의 입찰 및 검수가 필요하여 전체 일정 장기화 |
| 적합 사업 | 단순 레거시 재구축, 패키지 도입, 표준화된 사업 | 대규모 차세대, 신규 업무 시스템, 기술 복잡도 높은 사업 |

## Ⅴ. 실무 공공 SW 발주·계약의 실패 요인과 공학적 대책

> 설계-개발 간 책임 단절과 차등점수 격차 왜곡을 방어하지 못하면 제도의 취지가 훼손됨.

| 위험 요인 | 발생 원인 | 공학적·관리적 통제 대책 | 검증 지점 |
|---|---|---|---|
| 설계-개발 책임 단절 | 1단계 설계자가 비현실적 아키텍처 납품 후 철수 | 1단계 검수 시 **PoC(개념검증)** 의무화 및 2단계 감수·자문 계약 연계 | 구현 불가능한 설계 0건 검증 |
| 차등점수 격차 왜곡 | 과도한 차등폭(3점)으로 정량 점수 우수 기업 역전 | 사업 규모·난이도에 맞춘 적정 차등폭(0.5~1.5점) 탄력 적용 | 합리적이고 공정한 기술 변별력 확인 |
| 과업심의위원회 무력화 | 발주기관의 형식적 서면 심의 및 과업 변경 미개최 | 과업심의 의무화 위반 시 감사 지적 명시 및 조달청 계약 변경 연동 | 부당한 무상 과업 추가 0건 유지 |
| 헤드카운팅 관행 회귀 | 기능점수(FP) 발주 후 현장에서 투입 인력 명단·등급 요구 | 인력 관리 조항 계약서 배제 의무화 및 산출물 기반 검수 정착 | 투입 공수 간섭 배제 및 생산성 보장 |

## Ⅵ. 공정한 소프트웨어 생태계 완성 중심 기술사적 제언

> 공공 SW 사업 부실은 개발사 역량 부족 이전에 불명확한 RFP와 덤핑 입찰 제도에서 기인하므로, 요구사항 상세화와 제값 주기 풍토가 선행되어야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 공공 SW 사업의 고질적인 납기 지연과 품질 저하는 결국 발주기관이 무엇을 만들지 모른 채 사업자를 뽑고, 최저가 투찰자가 낙찰되는 구조적 결함에서 비롯됨. 기획·설계 분할 발주로 요구사항을 먼저 고정하고, 차등점수제로 기술 우수 기업을 낙찰시키는 것이 유일한 해법임.
- 나라면: 공공 정보화 사업 기획 시 `ISMP 기반 기능·비기능 요구사항 100% 명세화 → 기술 90% 및 1.0점 차등점수제 적용 → 과업 변경 발생 시 과업심의위원회 의결을 통한 계약금액 자동 조정`을 조달 규격서에 확정하겠음.

### 실전 답안용 기술사적 제언

- 판정: 행정 편의적 일괄 발주 탈피 및 요구사항 상세화 기반 공정 계약 확립
- 대안: **단계별 발주 + 기술평가 90:10 + 차등점수제 + 과업심의 연동** 패키지 적용
- 검증: 본개발 착수 전 요구사항 확정률 100% · 과업 변경 계약금액 조정률 100%
- 효과: 과업 변경 분쟁 원천 차단 및 공공 정보시스템 품질·납기 보증

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 SW 발주·계약 혁신 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>모호한 RFP · 저가 덤핑 투찰 · 무상 과업 변경 강요</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>설계·개발 분할발주 + 기술 90% 및 차등점수제 + 과업심의 의무화</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>상세 RFP 기반 정밀 FP 산출 · 순위별 고정 격차 부여</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>제값 주는 공공 SW 생태계 확립 · 고품질 디지털 행정 완성</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **공공 SW 사업 발주·계약**은 요구사항 불명확성과 저가 덤핑 투찰을 근절하기 위해 분석·설계와 개발을 분리하는 **단계별 발주**와 기술 변별력을 강화하는 **차등점수제**를 적용하는 법정 공공 조달 체계
- 목적: **요구사항 상세화** 및 기술 중심 평가 체계 확립 → 잦은 과업 변경과 저가 덤핑 근절 및 납기·품질 보증

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 SW 발주·계약 프로세스 요약">
  <div class="itpe-pipeline-node"><strong>1단계 설계</strong><small>요구사항 상세화 · 정밀 FP 산정</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>2단계 공고</strong><small>상세 RFP 첨부 · 사전 규격 공개</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>제안 평가</strong><small>기술 90% + 차등점수제(고정 격차)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>기술 협상</strong><small>과업 기준선 확정 · 공정 계약 체결</small></div>
</div>

### 3. 핵심 통제

- **단계별 발주**: 분석·설계(1단계)로 요구사항 확정 후 구현(2단계) 분리 발주
- **차등점수제**: 기술능력평가 순위 간 0.5~3점의 고정 격차 강제 부여로 저가 투찰 방어 및 기술 우위 사업자 낙찰

## 출제 이력과 검증 출처

- 제122회 정보관리기술사 기출 맥락: 협상에 의한 계약체결 기준과 차등점수제
- 제121회 정보관리기술사 기출 맥락: 공공 SW사업 발주제도 개선방안
- 과학기술정보통신부, [소프트웨어 진흥법 및 공공 소프트웨어사업 제안요청서 작성 매뉴얼](https://www.msit.go.kr)
- 조달청, [협상에 의한 계약 제안서평가 세부기준](https://www.pps.go.kr)

## 학습 체크

- [ ] 단계별 분할 발주와 일괄 발주의 장단점을 요구사항 관리 관점에서 비교할 수 있는가?
- [ ] 기술평가 90% 확대와 차등점수제가 저가 덤핑 투찰을 방지하는 원리를 설명할 수 있는가?
- [ ] 과업심의위원회의 법적 역할과 사업기간 적정성 심의의 필요성을 서술할 수 있는가?
- [ ] 설계-개발 분할 발주 시 발생하는 책임 단절 문제를 극복하기 위한 공학적 대책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [POP](./038_pop.md)
- 연관 토픽: [RFP](./049_rfp.md), [소프트웨어 사업 대가산정](./026_software_cost_estimation.md), [협상에 의한 계약 세부기준](./066_negotiated_contract_proposal_evaluation.md), [과업심의 기준](./091_public_sw_cost_and_scope_change_criteria.md)
- 다음 토픽: [부정적 위험 대응 전략](./040_negative_risk_response_strategy.md)
