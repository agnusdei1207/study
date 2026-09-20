---
title: "IT서비스 산업 특수성"
author: "Codex"
date: "2026-09-20T19:32:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5.6 Sol"
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
- 메커니즘: 모호한 RFP와 저가 턴키 계약이 다단계 외주화로 이어지는 악순환을 **소프트웨어 진흥법** 4대 제도 장치로 통제하고 상용 SaaS로 전환
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
    <small>과업심의 의무화 · 50% 초과 하도급 제한 · 상용 SaaS 우선 도입</small>
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

> 국내 IT서비스(SI/SM) 산업의 고유한 특수성(무형성, 비분리성, 이질성, 주문생산성)과 구조적 문제점을 설명하고, 소프트웨어 진흥법에 기반한 4대 제도적 개선 방안 및 상용 SaaS 중심의 산업 고부가가치화 전략을 논하시오. (25점)

## Ⅰ. 인적 지식 집약과 주문 생산의 딜레마, IT서비스 산업의 개요

> IT서비스 산업은 소프트웨어의 무형성과 주문생산성으로 인해 심각한 정보 비대칭을 내포하며, 생태계 정상화의 성패는 단순 인력 관리가 아닌 **과업의 명확한 상세화**와 **결과물 가치 기반 대가 지급**으로 판정함.

- 정의: 일반 제조업과 달리 **무형성(Intangibility)**, **비가시성**, **주문생산성**과 높은 인적 의존성을 지녀 다단계 하도급과 헤드카운팅 관행이 발생하기 쉬운 **국내 IT서비스(SI/SM) 산업의 구조적 특성**
- 목적: 불공정 거래 관행 개선 및 엔지니어 처우 개선 → **소프트웨어 진흥법 제도 개선**과 **상용 SaaS 전환**을 통한 소프트웨어 생태계 고부가가치화

## Ⅱ. 국내 IT서비스 산업의 구조적 악순환 파이프라인

> 모호한 발주가 원수급자의 저가 수주와 다단계 하도급으로 전이되며 말단 엔지니어의 처우 악화와 품질 결함으로 귀결됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="국내 IT서비스 다단계 하도급 악순환 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 발주자 (수요처)</strong></span>
    <small>모호한 RFP · 짧은 사업 기간 · 예산 삭감 턴키 발주 · 무상 과업 추가<br />→ 불완전한 과업 요구사항</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 대형 SI 원수급자 (수주사)</strong></span>
    <small>관리 마진 취득 후 응용 개발 전면 외주화 (1차 하도급 집행)<br />→ 프로젝트 총괄 및 관리 기능 한정</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 중소 전문 소프트웨어사 (수급인)</strong></span>
    <small>단가 인하 압박 · 모듈별 재하도급 분할 및 인력 파견(2차 하도급)<br />→ 수익성 악화 및 R&D 투자 여력 상실</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 말단 프리랜서 및 개발자 (실행자)</strong></span>
    <small>열악한 개발 환경 · 과도한 야근/철야 · 잦은 이탈 · 시스템 결함 누적<br />→ 시스템 오픈 파행 및 운영 장애 발생</small>
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

## Ⅴ. 소프트웨어 진흥법 기반 4대 제도적 개선 장치

> 법제도적 강제를 통해 다단계 하도급을 차단하고 기능점수 기반의 정당한 대가 지급 체계를 정착시킴.

| 법제도 개선 장치 | 주요 법적 규정 내용 | 실무적 기대 효과 |
|---|---|---|
| **하도급 제한 및 사전승인제** | 소프트웨어 사업의 **50%를 초과하여 하도급할 수 없으며**, 재하도급은 원칙적 금지 | 중간 착취 페이퍼컴퍼니 퇴출 및 원수급자의 책임 수행 강화 |
| **제안요청서 요구사항 상세화** | 공공 SW 발주 시 요구사항을 세부 기능 및 데이터 단위까지 명세 의무화 | 깜깜이 입찰 방지 및 과업 범위 모호성에 따른 분쟁 예방 |
| **과업심의위원회 설치 의무화** | 발주자의 과업 변경 요구 시 공인 위원회 심의를 거쳐 계약금액·기간 조정 | **무상 과업 추가 관행 철폐** 및 정당한 개발 대가 지급 보장 |
| **투입인력(헤드카운팅) 관리 금지** | 사업 수행 시 특정 개발자 상주나 인력 명단 제출 요구를 법적으로 금지 | **기능점수(FP)** 기반 가치 계약 유도 및 개발자 자율성 보장 |

## Ⅵ. 상용 SaaS 우선 도입과 컴포저블 IT 조달을 위한 기술사적 제언

> 밑바닥부터 새로 개발하는 전통적 맞춤형 SI 방식은 필연적으로 예산 초과와 장애를 초래하므로, 상용 SaaS 우선 도입과 컴포저블 조달로의 체질 개선이 필수적임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 한국 IT서비스 산업의 가장 큰 비극은 이미 글로벌 표준으로 잘 만들어진 ERP, 그룹웨어, CMS가 있음에도 불구하고 공공과 대기업이 '우리 기관만의 특수성'을 앞세워 수백억짜리 맞춤형 SI로 발주하는 점임. 이것이 하도급 피라미드와 엔지니어 갈아넣기의 원흉임.
- 나라면: 공공 및 금융 정보화 사업 발주 시 `기검증된 상용 클라우드 SaaS 도입 가능성을 사전 검토하도록 의무화(SaaS 우선 도입 원칙) → 고유 핵심 업무만 API 기반 마이크로서비스로 분할 발주`하는 컴포저블 IT 조달 거버넌스를 수립하겠음.

### 실전 답안용 기술사적 제언

- 판정: 1회성 맞춤형 SI 용역을 탈피하고 상용 SaaS 중심 생태계 확립
- 대안: **상용 SaaS 우선 도입 원칙 및 API 기반 마이크로서비스 컴포저블 조달** 체계 정착
- 검증: 상용 솔루션·SaaS 도입률 50% 이상 달성 · 과업 변경 시 계약금액 조정률 100%
- 효과: 다단계 하도급 마진 누수 원천 차단 · 국내 소프트웨어 기업의 글로벌 SaaS 경쟁력 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT서비스 산업 고부가가치화 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>1회성 맞춤 개발 고수 · 저가 턴키 다단계 하도급 피라미드 · 헤드카운팅 M/M 정산</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>소프트웨어 진흥법 철저 준수(과업심의·하도급 제한) + 공공 상용 클라우드 SaaS 우선 도입제</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>불법 파견 재하도급 적발 0건 · 기능점수(FP) 기반 대가 산정 100% 준수</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>개발자 처우 개선 및 이탈 방지 · 고품질 소프트웨어 자산 축적 및 산업 생태계 선순환</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 소프트웨어의 **무형성**, **비분리성**, **주문생산성**으로 인해 발주자-수주자 간 정보 비대칭이 크고, 다단계 하도급과 헤드카운팅(M/M) 관행이 발생하는 **국내 IT서비스(SI/SM) 산업의 구조적 특성**
- 목적: 불공정 거래 관행 개선 및 엔지니어 권익 보호 → **소프트웨어 진흥법 4대 장치**를 통한 산업 고부가가치화

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="소프트웨어 진흥법 4대 핵심 개선 장치 요약">
  <div class="itpe-pipeline-node"><strong>하도급 제한</strong><small>50% 초과 하도급 제한 · 재하도급 원칙적 금지</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>요구사항 상세화</strong><small>발주 전 제안요청서 기능/데이터 상세 명세 의무화</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>과업심의 의무화</strong><small>과업 변경 시 위원회 심의를 통한 대가·기간 조정</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>헤드카운팅 금지</strong><small>투입인력 관리 금지 · 기능점수(FP) 대가 산정</small></div>
</div>

### 3. 핵심 통제

- **하도급지킴이 연계**: 조달청 관리 시스템을 통한 하도급 대금 직불제 검증
- **상용 SaaS 우선 도입**: 1회성 용역 SI를 탈피하고 기검증된 클라우드 솔루션 조달 의무화

## 출제 이력과 검증 출처

- 제124회 정보관리기술사(KPC) 1교시: 한국 IT서비스 산업의 특수성과 법제도적 개선 방안
- 제110회 2교시: 공공 SW 사업 생태계 정상화 및 하도급 구조 개선
- 과학기술정보통신부, [소프트웨어 진흥법 및 하도급 제한 고시](https://www.msit.go.kr)
- 소프트웨어정책연구소(SPRi), [SW 산업 생태계 현황 및 구조 개선 보고서](https://spri.kr)

## 학습 체크

- [ ] IT서비스 산업의 4대 고유 서비스 속성(무형성, 비분리성, 이질성, 소멸성)을 설명할 수 있는가?
- [ ] 다단계 하도급 피라미드와 헤드카운팅 대가 산정의 구조적 폐단을 설명할 수 있는가?
- [ ] 소프트웨어 진흥법의 4대 핵심 개선 장치(하도급 제한, 요구사항 상세화, 과업심의, 투입인력 관리 금지)를 제시할 수 있는가?
- [ ] 맞춤형 구축(SI)에서 상용 SaaS 및 컴포저블 IT 조달로의 전환 전략을 논술할 수 있는가?

## 연결 토픽

- 이전 토픽: [CoE](./082_coe.md)
- 연관 토픽: [SW 사업 대가산정](./026_software_cost_estimation.md), [과업심의 기준](./091_public_sw_cost_and_scope_change_criteria.md), [하도급 구조](./097_software_industry_subcontracting_structure.md)
- 다음 토픽: [경영환경 분석](./088_business_environment_analysis.md)
