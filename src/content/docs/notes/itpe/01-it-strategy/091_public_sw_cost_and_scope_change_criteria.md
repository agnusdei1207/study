---
title: "적정 사업기간·과업심의"
author: "OpenAI Codex"
date: "2026-09-22T07:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW 사업관리를 거쳐 적정 사업기간과 과업심의로 이어지는 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 사업관리</span>
  <strong>적정 사업기간·과업심의</strong>
</div>

## 큰 그림과 30초 인출

- **적정 사업기간**: 발주 전에 과업 수행기간을 산정해 계약에 반영
- **과업심의**: 과업 확정·변경과 그에 따른 계약금액·기간 조정을 심의
- **통제 흐름**: 과업·기간 산정 → 과업 확정 → 변경 영향분석 → 심의 → 계약 Baseline 갱신

<div class="itpe-pipeline is-vertical" role="img" aria-label="적정 사업기간 산정과 과업심의 흐름">
  <div class="itpe-flow-node">
    <strong>발주 전</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>과업·기간 산정</span></div>
    <div class="itpe-step-detail"><strong>산출</strong><span>과업내용서·사업기간 산정서</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>과업심의</strong>
    <div class="itpe-step-detail"><strong>판단</strong><span>과업 확정·변경과 계약 영향</span></div>
    <div class="itpe-step-detail"><strong>산출</strong><span>심의 결과·조치계획</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>계약·계획 반영</strong>
    <div class="itpe-step-detail"><strong>통제</strong><span>범위·금액·기간·RTM 갱신</span></div>
  </div>
</div>

<details>
<summary>약어·전문용어</summary>

- **SW(Software)**: 소프트웨어
- **FP(Function Point)**: 사용자 관점의 기능 규모 측정 단위
- **RTM(Requirements Traceability Matrix)**: 요구사항과 설계·구현·시험·계약 산출물의 추적표
- **Baseline**: 승인 후 변경통제 대상이 되는 기준 상태
- **과업심의위원회**: 공공 SW 사업의 과업 확정·변경 등을 심의하는 위원회

</details>

## 예상문제

> **(미출제 예상·25점)** 공공 SW 사업의 적정 사업기간 산정과 과업심의 제도를 설명하고, 수행 중 과업 변경을 통제하는 방안을 제시하시오.

## Ⅰ. 적정 사업기간·과업심의 개요

> 발주 전에는 **적정 사업기간**을 계약에 반영하고, 수행 중에는 **과업심의위원회**를 통해 범위 변경과 계약 영향을 통제함

- **정의**: 공공 SW 사업의 수행기간을 합리적으로 산정하고, 과업 확정·변경과 계약 조정을 심의하는 제도
- **목적**: 무리한 일정·무상 과업 확대·계약 분쟁 예방

## Ⅱ. 과업 확정·변경 통제 절차

> 산정·심의 결과가 계약과 사업관리 Baseline까지 이어져야 실질적 통제가 됨

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 소프트웨어 과업 확정과 변경 통제 5단계">
  <div class="itpe-flow-node">
    <strong>① 과업·기간 산정</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>요구사항·기초자료·FP·유사사업·특이사항 검토</span></div>
    <div class="itpe-step-detail"><strong>산출</strong><span>과업내용서·사업기간 산정서</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>② 과업 확정</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>범위·산출물·검수기준 심의</span></div>
    <div class="itpe-step-detail"><strong>산출</strong><span>확정 과업·심의 결과</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>③ 변경요청·영향분석</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>범위·비용·기간·품질 영향 분석</span></div>
    <div class="itpe-step-detail"><strong>산출</strong><span>변경요청서·영향분석서</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>④ 변경 심의</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>승인·조건부 승인·불가</span></div>
    <div class="itpe-step-detail"><strong>산출</strong><span>심의 결과·조치계획</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>⑤ 계약·Baseline 갱신</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>계약금액·기간·범위·RTM 반영</span></div>
    <div class="itpe-step-detail"><strong>산출</strong><span>변경계약·갱신 계획서</span></div>
  </div>
</div>

## Ⅲ. 적정 사업기간과 과업심의 비교

> 적정 사업기간은 발주 전 일정의 현실성을, 과업심의는 과업과 계약 변경의 정당성을 통제함

| 구분 | 적정 사업기간 | 과업심의 |
|---|---|---|
| 근거 | 소프트웨어진흥법 제45조 | 소프트웨어진흥법 제50조 |
| 시점 | 발주·계약 전 | 과업 확정·변경 시 |
| 판단 | 과업 대비 수행기간 적정성 | 과업·금액·기간 조정 필요성 |
| 산출 | 사업기간 산정서 | 심의 결과·조치계획 |

:::note[시행시점 확인]
2026년 9월 현재 시행 조문과 2027년 2월 12일 시행 예정 개정 조문을 구분해야 함.
:::

## Ⅳ. 과업 변경 영향분석

> 변경 여부보다 변경이 범위·비용·일정·품질에 미치는 영향을 함께 판단하는 것이 핵심임

| 영향축 | 확인 항목 | 반영 대상 |
|---|---|---|
| 범위 | 요구사항·산출물·검수기준 | 과업내용서·RTM |
| 규모·비용 | 기능 규모·인프라·운영비 | 산정서·계약금액 |
| 일정 | 선후행 작업·임계경로·인력 | 일정 Baseline |
| 품질·위험 | 시험 범위·보안·운영 영향 | 품질계획·위험등록부 |

과업을 임의로 경미·중대로 나누거나 FP 증감만으로 유상·무상을 단정하지 않고, 계약조건과 관련 법령에 따라 종합 판단함.

## Ⅴ. 문제점·대응책

> 과업 변경을 문서·심의·계약으로 연결하지 않으면 수행 현장의 합의가 분쟁으로 전환됨

| 위험 | 대책 | 효과 |
|---|---|---|
| 구두 변경 | 변경요청 서면화 | 책임·근거 확보 |
| 영향 누락 | 범위·비용·일정·품질 통합 분석 | 연쇄 영향 조기 식별 |
| 심의 후 미반영 | 계약·Baseline·RTM 동시 갱신 | 승인 내용과 수행 일치 |
| 시행시점 혼동 | 현행·시행 예정 조문 분리 확인 | 법적용 오류 예방 |

## Ⅵ. 결론·기술사적 제언

> **[핵심 통찰]** 과업심의의 성패는 회의 개최가 아니라 심의 결과가 계약과 사업관리 Baseline에 반영되는가에 달려 있음.

> **나라면** 변경요청마다 범위·비용·일정·품질 영향표를 첨부하고, 심의 통과 후 계약·RTM·시험기준이 함께 갱신되어야 변경을 실행하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="과업 변경의 실행 통제 방안">
  <div class="itpe-flow-node">
    <strong>변경요청</strong>
    <div class="itpe-step-detail"><strong>근거</strong><span>요구사항·사유·요청자</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>통합 영향분석·심의</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>범위·비용·일정·품질</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>계약 Baseline 갱신</strong>
    <div class="itpe-step-detail"><strong>반영</strong><span>계약·계획·RTM</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>구현·시험·검수</strong>
    <div class="itpe-step-detail"><strong>검증</strong><span>승인 과업과 산출물 일치</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

- **정의**: 공공 SW 사업의 수행기간을 산정하고 과업 확정·변경과 계약 조정을 심의하는 제도
- **목적**: 무리한 일정·무상 과업 확대·계약 분쟁 예방

| 구분 | 핵심 |
|---|---|
| 적정 사업기간 | 발주 전 수행기간 산정·계약 반영 |
| 과업심의 | 과업 확정·변경과 계약 영향 심의 |
| 사후 통제 | 계약·Baseline·RTM 동시 갱신 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [국가법령정보센터, 소프트웨어진흥법](https://www.law.go.kr/LSW/lsInfoP.do?lsId=000751)
- [국가법령정보센터, 소프트웨어진흥법 시행령](https://www.law.go.kr/LSW/lsInfoP.do?lsId=003989)
- [국가법령정보센터, 소프트웨어사업 계약 및 관리감독에 관한 지침](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000223356&chrClsCd=)
- [국가법령정보센터, 행정기관 및 공공기관 정보시스템 구축·운영 지침](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulId=33489&efYd=0)

## 학습 체크

- [ ] Ⅰ: 적정 사업기간과 과업심의의 목적을 설명할 수 있는가?
- [ ] Ⅱ: 과업 확정·변경 5단계의 활동과 산출을 연결할 수 있는가?
- [ ] Ⅲ: 두 제도의 시점·판단·산출 차이를 비교할 수 있는가?
- [ ] Ⅳ: 변경 영향을 범위·비용·일정·품질로 분석할 수 있는가?
- [ ] Ⅴ: 과업 변경 위험에 대한 대책·효과를 제시할 수 있는가?
- [ ] Ⅵ: 심의 결과를 계약 Baseline까지 연결하는 통제안을 제시할 수 있는가?

## 연결 토픽

- 이전: [089. TAM·SAM·SOM](./089_tam_sam_som/)
- 관련: [001. ISMP](./001_ismp/) · [039. 공공 SW 계약](./039_public_sw_contract/) · [113. SW 비용 산정](./113_software_cost_estimation/)
- 다음: [092. 기술수용모델](./092_technology_acceptance_model/)
