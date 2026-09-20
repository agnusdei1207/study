---
title: "SW사업 대가산정"
author: "OpenAI Codex"
date: "2026-09-21T16:10:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW사업 관리를 거쳐 SW사업 대가산정으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW사업 관리</span>
  <strong>SW사업 대가산정</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 사업유형과 작업범위에 맞는 산정방식을 선택하여 예산·발주·계약의 적정 대가를 산출
- 메커니즘: 범위 확정 → 규모·공수 산정 → 비용 구성 → 검증 → 계약 반영
- 통제: 요구사항·산정내역·계약범위의 Traceability와 과업변경 심의

<div class="itpe-pipeline is-vertical" role="img" aria-label="SW사업 범위 확정부터 계약 및 변경 통제로 이어지는 대가산정 흐름">
  <div class="itpe-pipeline-node"><strong>사업범위 확정</strong><div class="itpe-step-detail"><strong>입력</strong><span>요구사항 · 업무범위 · 품질조건</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>산정방식 선택</strong><div class="itpe-step-detail"><strong>판정</strong><span>기획 · 개발 · 운영 · 유지관리</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><strong>규모·공수 및 비용 산정</strong><div class="itpe-step-detail"><strong>산출</strong><span>FP · 투입공수 · 직접경비 · 사업비</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>발주·계약 및 변경 통제</strong><div class="itpe-step-detail"><strong>통제</strong><span>산정근거 검증 · 과업변경 심의 · 계약조정</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- **FP(Function Point)**: 사용자 관점의 논리적 기능을 기준으로 SW 규모를 측정하는 단위
- **ILF(Internal Logical File)**: 대상 애플리케이션 내부에서 유지되는 논리적 데이터 그룹
- **EIF(External Interface File)**: 다른 애플리케이션이 유지하고 대상 애플리케이션이 참조하는 논리적 데이터 그룹
- **EI(External Input)**: 외부 입력으로 내부 데이터 또는 처리 상태를 변경하는 기능
- **EO(External Output)**: 처리 결과를 외부로 제공하는 출력 기능
- **EQ(External Inquiry)**: 별도 파생처리 없이 데이터를 조회하는 기능
- **Traceability**: 요구사항부터 규모·비용·계약범위까지 근거를 추적할 수 있는 성질

</details>

## 예상문제

> SW사업 대가산정의 개념과 사업유형별 산정방식을 설명하고, FP 기반 개발비 산정 절차 및 과업변경 통제방안을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 적정 대가 지급을 위한 SW사업 대가산정의 개요

> 대가산정은 최저 견적을 만드는 계산이 아니라, 사업범위와 비용근거를 연결하여 발주자·사업자의 계약 Baseline을 세우는 활동임.

- 정의: SW사업의 예산수립·발주·계약에 필요한 적정 사업비를 사업유형별 기준으로 산출하는 활동
- 목적: 예산 적정성 확보 · 불공정 계약 방지 · 과업변경 분쟁 예방
- 근거: **소프트웨어 진흥법 제46조**의 적정 대가 지급 · KOSA의 **SW사업 대가산정 가이드**

## Ⅱ. 사업유형별 대가산정 체계

> 산정방식은 하나로 고정하지 않고 산출물의 명확성·측정 가능성·운영 특성에 따라 선택함.

| 사업 | 산정 기준 | 주요 산출 |
|---|---|---|
| **기획·컨설팅** | 직무별 투입공수 | 직접인건비 · 제경비 · 기술료 · 직접경비 |
| **SW개발** | FP 또는 투입공수 | 개발원가 · 직접경비 |
| **SW유지관리** | 유지관리 대상·업무범위 | 유지관리비 |
| **SW운영** | 운영업무·투입공수 | 운영비 |
| **개발·운영 통합** | 개발비와 운영비 각각 산정 후 합산 | 통합 사업비 |

## Ⅲ. FP 기반 SW개발비 산정 절차

> 요구사항이 기능 단위로 식별되어야 규모를 측정할 수 있으며, 각 단계의 활동과 산출근거를 함께 남겨야 함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="FP 기반 SW개발비 산정 단계별 활동과 산출물">
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>① 측정범위 정의</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>애플리케이션 경계 · 측정목적 확정</span><strong>산출</strong><span>측정범위 정의서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>② 기능 식별</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>ILF · EIF · EI · EO · EQ 식별</span><strong>산출</strong><span>기능 목록</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>③ 기능규모 산정</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>기능별 복잡도·가중치 적용</span><strong>산출</strong><span>기능점수 산정내역</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>④ 개발원가 산정</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>현행 가이드의 단가·보정기준 적용</span><strong>산출</strong><span>SW개발원가</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>⑤ 사업비 확정</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>직접경비·기타 비용 합산 및 검증</span><strong>산출</strong><span>사업비 산정서</span></div></div>
</div>

## Ⅳ. FP 방식과 투입공수 방식 비교

> 기능범위가 명확하면 FP, 기능 식별이 곤란하고 전문가 작업량이 핵심이면 투입공수가 적합함.

| 기준 | FP 방식 | 투입공수 방식 |
|---|---|---|
| **측정대상** | 사용자 기능규모 | 인력·기간 |
| **적합사업** | 요구사항이 구체화된 개발 | 기획·컨설팅 · 기능 식별 곤란 작업 |
| **강점** | 기술·인력과 분리된 규모 비교 | 작업량 중심 산정 용이 |
| **통제** | 기능 중복·누락 검증 | 직무·공수·산출물 검증 |

## Ⅴ. 대가산정의 문제점·대응책

> 오차 자체보다 산정근거가 계약과 단절될 때 무상과업·예산초과·분쟁으로 확대됨.

| 위험 | 대책 | 효과 |
|---|---|---|
| **범위 누락** | 요구사항·기능목록·FP 내역 추적 | 무상과업 방지 |
| **공수 부풀림** | 직무·기간·산출물 교차검증 | 과다산정 억제 |
| **과업변경 미반영** | 과업심의위원회 심의 후 대가·기간 조정 | 계약분쟁 예방 |

## Ⅵ. 변경비용을 통제하는 기술사적 제언

> 초기 산정값을 고정하는 것보다 변경된 요구사항을 기능규모와 계약대가에 일관되게 반영하는 통제가 중요함.

`[핵심 통찰]` 대가산정의 성패는 최초 금액의 정밀도보다 요구사항 변경이 규모·비용·계약에 동일하게 반영되는지에 달려 있음.

`나라면` 요구사항별 기능목록과 산정내역을 계약항목에 연결하고, 승인된 과업변경만 재산정하여 Baseline을 갱신하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 변경에 따른 SW사업 대가 재산정 통제 흐름">
  <div class="itpe-pipeline-node"><strong>변경요청</strong><div class="itpe-step-detail"><strong>입력</strong><span>추가 · 삭제 · 수정 요구사항</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>영향분석</strong><div class="itpe-step-detail"><strong>판정</strong><span>기능규모 · 공수 · 일정 · 품질 영향</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>과업변경 심의</strong><div class="itpe-step-detail"><strong>통제</strong><span>범위 타당성 · 계약금액 · 계약기간 검토</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><strong>Baseline 갱신</strong><div class="itpe-step-detail"><strong>효과</strong><span>산정근거와 계약범위 일치</span></div></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: SW사업의 예산수립·발주·계약에 필요한 적정 사업비를 사업유형별 기준으로 산출하는 활동
- 목적: 예산 적정성 확보 · 불공정 계약 방지 · 과업변경 분쟁 예방

### 2. 산정체계

| 사업 | 기준 |
|---|---|
| **기획·컨설팅** | 투입공수 |
| **SW개발** | FP · 투입공수 |
| **유지관리·운영** | 업무범위 · 투입공수 |

### 3. 핵심 통제

- **Traceability**: 요구사항 ↔ 기능목록 ↔ 규모·공수 ↔ 사업비 ↔ 계약범위
- **과업변경 심의**: 변경 범위의 타당성 검토 후 계약금액·기간 조정

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [KOSA: SW사업 대가산정 가이드 2025년 개정판](https://www.sw.or.kr/site/sw/ex/board/View.do?bcIdx=63607&cbIdx=276)
- [국가법령정보센터: 소프트웨어 진흥법 제46조](https://www.law.go.kr/법령/소프트웨어진흥법/제46조)
- [국가법령정보센터: 소프트웨어 진흥법 제50조](https://www.law.go.kr/법령/소프트웨어진흥법/제50조)

## 학습 체크

- [ ] Ⅰ. 대가산정의 정의·목적·법적 근거를 재현할 수 있는가?
- [ ] Ⅱ. 기획·개발·유지관리·운영의 산정기준을 구분할 수 있는가?
- [ ] Ⅲ. FP 산정 5단계의 활동·산출을 연결할 수 있는가?
- [ ] Ⅳ. FP와 투입공수를 측정대상·적합사업·통제로 비교할 수 있는가?
- [ ] Ⅴ~Ⅵ. 범위 누락·공수 부풀림·과업변경의 대응책과 Baseline 갱신을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [범정부 AI 공통기반](./025_pan_government_ai_common_infrastructure.md)
- 연관 토픽: [ISMP](./001_ismp.md), [RFP](./049_rfp.md), [공공 SW사업 발주·계약](./039_public_sw_contract.md)
- 다음 토픽: [Active-Active 스토리지 DR](./027_active_active_storage_dr.md)
