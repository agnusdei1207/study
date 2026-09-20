---
title: "IT서비스 산업 특수성"
author: "OpenAI Codex"
date: "2026-09-22T06:40:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 IT 산업 생태계 및 SW 진흥 정책을 거쳐 IT서비스 산업 특수성으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>IT 산업 생태계·SW 진흥 정책</span>
  <strong>IT서비스 산업 특수성</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **IT서비스 산업 특수성**은 소프트웨어의 무형성·주문생산성으로 인해 정보 비대칭과 다단계 하도급, 헤드카운팅 대가 산정이 발생하는 국내 SI/SM 산업의 구조적 고유 속성
- 메커니즘: 모호한 과업과 저가 계약이 하도급·품질 위험으로 전이되는 구조를 **소프트웨어 진흥법**의 과업·하도급·계약 통제로 완화
- 산출: 하도급 사전 승인서 · 요구사항 상세 명세서 · 과업심의 의결서 · 기능점수(FP) 산정서

<div class="itpe-flow-map" role="img" aria-label="국내 IT서비스 산업 구조와 제도 개선 흐름">
  <div class="itpe-flow-node">
    <strong>소프트웨어 고유 서비스 속성</strong>
    <small>무형성(Intangibility) · 비분리성 · 이질성 · 소멸성 · 주문생산성</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>구조적 정보 비대칭 발생</small></div>
  <div class="itpe-flow-node is-current">
    <strong>국내 IT서비스 산업 구조적 현안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>거래구조</strong><span>피라미드형 <span class="itpe-keyword"><strong>다단계 하도급</strong></span> 및 중간 마진 누수</span></div>
      <div class="itpe-flow-branch"><strong>대가산정</strong><span>투입 인력 머릿수 중심의 <span class="itpe-keyword"><strong>헤드카운팅(M/M)</strong></span> 관행</span></div>
      <div class="itpe-flow-branch"><strong>과업통제</strong><span>모호한 요구사항에 따른 무상 과업 추가 및 잦은 변경</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>소프트웨어 진흥법 개정 및 패러다임 전환</small></div>
  <div class="itpe-flow-node">
    <strong>산업 생태계 고부가가치화</strong>
    <small>과업심의 · 하도급 제한·사전승인 · 상용SW 직접구매</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **IT서비스(SI/SM)**: 고객의 비즈니스 요구에 맞추어 정보시스템을 기획·구축(SI)하고 운영·유지보수(SM)하는 용역 산업
- **Intangibility(무형성)**: 소프트웨어 개발 완료 전까지 물리적 실체와 동작 상태를 눈으로 확인할 수 없는 특성
- **Headcounting(헤드카운팅)**: 결과물의 기능 가치가 아닌 투입된 엔지니어의 인원수와 투입 기간(M/M)을 기준으로 대가를 산정하는 방식
- **과업심의위원회**: 공공 SW 사업에서 발주자의 과업 내용 변경 및 사업 기간 연장 요구를 객관적으로 심의하여 계약금액을 조정하는 법정 기구
- **하도급 제한**: 원수급자가 사업의 50%를 초과하여 하도급할 수 없도록 법적으로 제한하고 재하도급을 원칙적으로 금지하는 규정
- **Composable IT**: 1회성 맞춤 개발 대신 검증된 상용 클라우드 SaaS와 기성 모듈을 API로 조합하여 조달하는 현대적 방식

</details>

## 예상문제

> IT서비스 산업의 특성과 구조적 문제점을 설명하고, 공공 소프트웨어사업의 공정한 계약·수행을 위한 대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 인적 지식 집약과 주문 생산의 딜레마, IT서비스 산업의 개요

> IT서비스 산업은 소프트웨어의 무형성과 주문생산성으로 인해 심각한 정보 비대칭을 내포하며, 생태계 정상화의 성패는 단순 인력 관리가 아닌 **과업의 명확한 상세화**와 **결과물 가치 기반 대가 지급**으로 판정함.

- 정의: 일반 제조업과 달리 **무형성(Intangibility)**, **비가시성**, **주문생산성**과 높은 인적 의존성을 지녀 다단계 하도급과 헤드카운팅 관행이 발생하기 쉬운 **국내 IT서비스(SI/SM) 산업의 구조적 특성**
- 목적: 불공정 거래 관행 개선, 엔지니어 처우 보장 및 SW 생태계 고부가가치화

## Ⅱ. 국내 IT서비스 산업의 구조적 악순환 파이프라인

> 모호한 발주가 원수급자의 저가 수주와 다단계 하도급으로 전이되며 말단 엔지니어의 처우 악화와 품질 결함으로 귀결됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="국내 IT서비스 다단계 하도급 악순환 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 발주자 (수요처)</strong></span>
    <div class="itpe-step-detail"><strong>모호한 발주</strong><span>모호한 RFP, 짧은 사업 기간, 예산 삭감 및 무상 과업 추가</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 대형 SI 원수급자 (수주사)</strong></span>
    <div class="itpe-step-detail"><strong>외주 전가</strong><span>관리 마진 취득 후 응용 개발 전면 외주화(1차 하도급 집행)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 중소 전문 소프트웨어사 (수급인)</strong></span>
    <div class="itpe-step-detail"><strong>단가 압박</strong><span>단가 인하 압박 및 모듈별 재하도급 분할·인력 파견(2차 하도급)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 말단 프리랜서 및 개발자 (실행자)</strong></span>
    <div class="itpe-step-detail"><strong>품질 저하</strong><span>열악한 환경, 야근/철야, 잦은 이탈 및 결함 누적에 따른 장애 발생</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>악순환의 고리</strong></span> · 저가 수주 ↔ 중간 마진 누수 ↔ 개발자 처우 악화 ↔ 시스템 품질 저하의 구조적 반복</div>

## Ⅲ. IT서비스의 4대 고유 속성 및 산업적 영향

> 서비스 마케팅의 4대 속성이 IT 프로젝트에 투영되며 품질 통제와 대가 산정의 난제를 야기함.

| 서비스 고유 속성 | 공학적·산업적 세부 내용 | 파생되는 구조적 문제점 |
|---|---|---|
| **무형성 (Intangibility)** | 개발 완료 전까지 물리적 실체 확인 불가 (비가시성) | 발주자와 수주자 간 요구사항 해석 차이 및 분쟁 빈발 |
| **비분리성 (Inseparability)** | 서비스의 생산과 소비가 현장에서 동시에 진행 | 발주자의 잦은 개입, 상주 개발 강요, 현장 구두 과업 추가 |
| **이질성 (Heterogeneity)** | 투입 인력의 숙련도에 따라 소프트웨어 품질 편차 극심 | 생산성의 불확실성 증대 및 객관적 품질 표준화 한계 |
| **소멸성 (Perishability)** | 유휴 인력의 생산 능력을 재고로 보관 불가 | 비가동 인력 유지비 부담 및 프로젝트성 고용 불안정 심화 |
| **주문생산성 (Customization)** | 특정 고객만을 위한 단일 1회성 맞춤 시스템 구축 | 재사용성 결여 및 복제에 따른 한계비용 체감 법칙 미작동 |

## Ⅳ. 제조업 vs 패키지 SW vs IT서비스 산업 비교

> 패키지 SW가 한계비용 0의 무한 복제 확장성을 갖는 반면, IT서비스는 인력 비례형 용역 구조에 머묾.

| 비교 항목 | 전통 제조업 (H/W) | 패키지 소프트웨어 (COTS / SaaS) | IT서비스 산업 (SI / SM) |
|---|---|---|---|
| **생산 방식** | 공장 설비 기반 대량 물리 생산 | 디지털 코드 일회 제작 후 복제 배포 | 고객 맞춤형 1회성 주문 용역 개발 |
| **한계 비용** | 원자재 및 조립 물류비 지속 소요 | **거의 0에 수렴 (Zero Marginal Cost)** | **인력 투입(M/M)에 정비례하여 증가** |
| **수익 모델** | 제품 판매 단가 × 판매 수량 | 라이선스 판매 또는 클라우드 정기 구독료 | 투입공수(M/M) 또는 고정가 턴키 계약 |
| **글로벌 확장성** | 생산 설비 및 공급망 구축 필요 | **글로벌 시장 대상 무한 확장 가능** | 물리적 투입 가능 인력 풀(Pool)에 종속 |
| **가치 동인** | 원가 절감, 생산 수율, SCM 최적화 | 사용자 경험(UX), 제품 완성도, PMF | 프로젝트 관리(PM), 개발 역량, 발주처 관리 |

## Ⅴ. 문제점·대응책

> 법제도적 강제를 통해 다단계 하도급을 차단하고 기능점수 기반의 정당한 대가 지급 체계를 정착시킴.

| 문제 | 대응책 | 효과 |
|---|---|---|
| **다단계 하도급** | 법 제51조의 50% 초과 하도급 제한·사전승인·재하도급 제한 적용 | 원수급자 책임 강화 |
| **과업 범위 불명확** | 상세 요구사항 작성·과업심의위원회 확정 | 분쟁 예방 |
| **무상 과업 변경** | 변경 심의 후 계약금액·기간 조정 | 정당한 대가·기간 확보 |
| **상용SW 일괄구축** | 직접구매 대상 검토·분리발주 | 전문기업 참여·제품 선택권 확보 |

> 하도급 비율·재하도급에는 법정 예외가 있으므로 사업유형과 승인 요건을 함께 확인함.

## Ⅵ. 맞춤개발 범위를 통제하는 기술사적 제언

> 민간·상용 소프트웨어 활용 가능성을 먼저 검토하고 차별 업무만 맞춤개발하여 과업·비용 위험을 줄임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 맞춤개발 자체가 문제가 아니라 표준 기능과 차별 업무의 경계를 정하지 않은 채 모든 요구를 한 계약에 묶는 것이 비용·변경 위험을 키움.
- 나라면: 민간·상용 소프트웨어 적용 가능성을 먼저 검토하고, 차별 업무만 명확한 인터페이스와 검수기준으로 분리하겠음.

### 실전 답안용 기술사적 제언

- 판정: 표준 기능·차별 업무·연계 범위·검수기준
- 대안: 상용SW 직접구매 검토 · 맞춤개발 최소화 · 인터페이스 기반 분리
- 검증: 요구사항–계약–검수 추적성 · 변경 심의·대가 조정 증적
- 효과: 중복개발·과업변경·하도급 위험 완화

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT서비스 산업 고부가가치화 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>취약점</strong><span>1회성 맞춤 개발 고수, 저가 턴키 다단계 하도급 및 헤드카운팅 정산</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>과업심의·하도급 통제 · 상용SW 직접구매 검토 · 차별 업무 분리</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>요구사항–계약–검수 추적성 · 변경 심의·하도급 승인 증적</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>가치 창출</strong><span>개발자 처우 개선, 고품질 SW 자산 축적 및 산업 생태계 선순환 달성</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 소프트웨어의 **무형성**, **비분리성**, **주문생산성**으로 인해 발주자-수주자 간 정보 비대칭이 크고, 다단계 하도급과 헤드카운팅(M/M) 관행이 발생하는 **국내 IT서비스(SI/SM) 산업의 구조적 특성**
- 목적: 불공정 관행 개선, 엔지니어 권익 보호 및 산업 고부가가치화

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 소프트웨어사업의 계약·수행 통제 요약">
  <div class="itpe-pipeline-node">
    <strong>하도급 제한</strong>
    <div class="itpe-step-detail"><strong>구조 개선</strong><span>50% 초과 하도급 제한 및 재하도급 원칙적 금지</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>요구사항 상세화</strong>
    <div class="itpe-step-detail"><strong>범위 통제</strong><span>RFP 기능·데이터·품질 요구사항 상세화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>과업심의 의무화</strong>
    <div class="itpe-step-detail"><strong>변경 통제</strong><span>과업 변경 시 위원회 심의를 통한 대가·기간 조정</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>상용SW 직접구매</strong>
    <div class="itpe-step-detail"><strong>조달 통제</strong><span>직접구매 대상·분리발주·제외사유 검토</span></div>
  </div>
</div>

### 3. 핵심 통제

- **하도급지킴이 연계**: 조달청 관리 시스템을 통한 하도급 대금 직불제 검증
- **상용SW 직접구매 검토**: 직접구매 대상과 제외사유를 확인하고 맞춤개발 범위를 최소화

## 출제 이력과 검증 출처

- 참고 문항: 회차별 출제 정보는 Q-Net 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- 국가법령정보센터, [소프트웨어 진흥법](https://www.law.go.kr/lsInfoP.do?lsId=000751) — 제50조 과업심의위원회·제51조 하도급 제한
- 국가법령정보센터, [소프트웨어사업 계약 및 관리감독에 관한 지침](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000223356&chrClsCd=)

## 학습 체크

- [ ] IT서비스 산업의 4대 고유 서비스 속성(무형성, 비분리성, 이질성, 소멸성)을 설명할 수 있는가?
- [ ] 다단계 하도급 피라미드와 헤드카운팅 대가 산정의 구조적 폐단을 설명할 수 있는가?
- [ ] 소프트웨어 진흥법의 하도급 제한·과업심의와 상용SW 직접구매 제도를 설명할 수 있는가?
- [ ] 표준 기능과 차별 업무를 구분하여 맞춤개발 범위를 통제하는 방안을 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [CoE](./082_coe.md)
- 연관 토픽: [SW 사업 대가산정](./026_software_cost_estimation.md), [과업심의 기준](./091_public_sw_cost_and_scope_change_criteria.md), [하도급 구조](./097_software_industry_subcontracting_structure.md)
- 다음 토픽: [IT 역량체계(ITS-NCS)](./087_it_job_competency_system.md)
