---
title: "IT 아웃소싱"
author: "Codex"
date: "2026-09-20T19:28:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 IT 운영전략과 서비스 관리를 거쳐 IT 아웃소싱으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>IT 운영전략·소싱 거버넌스</span>
  <strong>IT 아웃소싱</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **IT 아웃소싱(IT Outsourcing)**은 핵심 비즈니스 집중과 비용 최적화를 위해 IT 기획·개발·운영 업무의 일부 또는 전부를 외부 전문 기업에 위탁하여 **SLA** 기반으로 수행하는 전략적 소싱 기법
- 메커니즘: 전략적 중요도와 내부 역량에 따른 **Make or Buy** 분석을 거쳐, **ISO 37500** 생명주기 4단계(전략 → 조달 → 전환 → 운영·거버넌스)를 밟고 **Exit Plan**으로 완결
- 산출: 소싱 전략서 · 제안요청서(**RFP**) · **SLA(Service Level Agreement)** 협약서 · 인수인계서 · 출구 전략서(**Exit Plan**)

<div class="itpe-flow-map" role="img" aria-label="IT 아웃소싱 Make or Buy 판단부터 생명주기 및 거버넌스 흐름">
  <div class="itpe-flow-node">
    <strong>소싱 타당성 분석</strong>
    <small>전략적 중요도 vs 내부 역량 (Make or Buy)</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>소싱 포트폴리오 확정</small></div>
  <div class="itpe-flow-node is-current">
    <strong>ISO 37500 아웃소싱 생명주기</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>전략</strong><span>비즈니스 케이스 · 잔존 조직(<span class="itpe-keyword"><strong>RO</strong></span>) 설계</span></div>
      <div class="itpe-flow-branch"><strong>조달</strong><span>제안 기술평가 · <span class="itpe-keyword"><strong>SLA</strong></span>/<span class="itpe-keyword"><strong>OLA</strong></span> 계약 체결</span></div>
      <div class="itpe-flow-branch"><strong>전환</strong><span>지식 이전(KT) · 자산 인계 · 병행 운영</span></div>
      <div class="itpe-flow-branch"><strong>운영</strong><span>성과 모니터링 · <span class="itpe-keyword"><strong>XLA</strong></span> 연계 · 출구 전략(<span class="itpe-keyword"><strong>Exit Plan</strong></span>)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>계약 만료 및 성과 평가</small></div>
  <div class="itpe-flow-node">
    <strong>재소싱 및 출구 실행</strong>
    <small>재계약 · 신규 공급사 전환 · 인소싱(Back-sourcing)</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **IT 아웃소싱(IT Outsourcing)**: IT 기획, 개발, 운영, 유지보수 업무의 일부 또는 전부를 외부 전문 기업에 위탁하여 계약 및 서비스 수준으로 통제하는 경영 방식
- **Make or Buy**: 내부 직접 수행(Make)과 외부 위탁 구매(Buy)의 타당성을 전략적 중요도와 내부 역량을 기준으로 판정하는 의사결정 프레임워크
- **ISO 37500**: 조직의 아웃소싱 생명주기 4단계(전략, 조달, 전환, 거버넌스)와 관리 프로세스를 규정한 국제 표준 가이드라인
- **SLA(Service Level Agreement)**: 발주사와 공급자 간에 합의된 IT 서비스 품질 수준, 가용성 지표 및 미달 시 위약금(Penalty)을 명시한 협약서
- **OLA(Operational Level Agreement)**: 최종 SLA 목표 달성을 지원하기 위해 공급사 내부 팀 및 협력사 간에 맺는 운영 수준 협약서
- **RO(Retained Organization)**: 업무 위탁 후에도 발주사에 잔류하여 아키텍처 기준선, 데이터 보안 및 계약 통제권을 행사하는 내부 잔존 조직
- **Exit Plan(출구 전략)**: 계약 만료 또는 분쟁 발생 시 서비스 연속성을 유지하며 다른 공급사로 전환하거나 인소싱하기 위한 사전 인수인계 계획
- **SIAM(Service Integration and Management)**: 다중 공급자(Multi-vendor)의 이종 IT 서비스를 통합 조율하여 단일 서비스로 제공하는 소싱 관리 모델
- **XLA(eXperience Level Agreement)**: 단순 시스템 가용성을 넘어 실제 최종 사용자가 체감하는 업무 만족도를 측정·관리하는 경험 수준 협약

</details>

## 예상문제

> IT 아웃소싱의 의사결정 모델(Make or Buy)과 ISO 37500 기반 생명주기 4단계를 설명하고, 공급자 종속(Lock-in) 및 내부 역량 공동화(Hollowing out) 방지를 위한 SLA 거버넌스와 출구 전략(Exit Plan)을 제시하시오. (25점)

## Ⅰ. 핵심 역량 집중과 비용 최적화, IT 아웃소싱의 개요

> IT 아웃소싱은 개발·운영 업무를 위탁하더라도 IT 거버넌스와 아키텍처 통제권은 **Retained Organization(잔존 조직)**에 유지해야 하며, 성패는 **Lock-in** 없는 **Exit Plan**의 완결성으로 판정함.

- 정의: 기업의 핵심 비즈니스 집중과 비용 최적화를 위해 IT 기획, 개발, 운영 업무의 일부 또는 전부를 외부 전문 기업에 위탁하여 **SLA** 기반으로 수행하는 전략적 소싱 관리 체계
- 목적: **Retained Organization** 중심의 IT 통제권 확립 및 운영 생산성 극대화 → 벤더 종속 방지 및 서비스 품질 담보

## Ⅱ. IT 아웃소싱 구성체계 및 ISO 37500 생명주기 4단계

> 아웃소싱은 단순 계약 체결로 끝나지 않으며, 전략 수립에서 출발하여 조달, 전환, 거버넌스 및 종료 시점의 출구 전략으로 이어지는 전 수명주기 프로세스임.

<div class="itpe-pipeline is-vertical" role="img" aria-label="ISO 37500 기반 IT 아웃소싱 4단계 생명주기 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 전략 수립 (Strategy)</strong></span>
    <small>Make or Buy 분석 · 소싱 범위 확정 · 잔존 조직(RO) 설계<br />→ 아웃소싱 전략 기획서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 공급자 선정 및 계약 (Procurement)</strong></span>
    <small>RFP 발행 · 기술 제안평가 · SLA 및 OLA 계약 체결<br />→ 제안평가서 · SLA 협약서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 이행 및 전환 (Transition)</strong></span>
    <small>업무 지식 이전(KT) · IT 자산 및 계정 인계 · 병행 운영<br />→ 업무 인수인계서 · 전환 완료 보고서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 운영 및 거버넌스 (Governance)</strong></span>
    <small>SLA 성과 모니터링 · 페널티/크레딧 정산 · Exit Plan 갱신<br />→ 월간 SLA 보고서 · 출구 전략서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Dual Governance</strong></span> · 전략-전술-운영 3계층 협의체 가동 및 위탁 종료 시 인소싱 가역성 보증</div>

## Ⅲ. IT 소싱 의사결정 모델 (Make or Buy 매트릭스)

> 기업의 전략적 중요도와 내부 기술 역량의 2축 평가를 통해 최적의 소싱 유형을 판정함.

| 소싱 유형 | 핵심 메커니즘 | 적용 대상 영역 | 통제 주안점 |
|---|---|---|---|
| **인소싱 (Make)** | 핵심 비즈니스 로직과 거버넌스를 내부 인력으로 전담 개발·운영 | 전사 아키텍처, 데이터 주권, 핵심 차별화 시스템 | 내부 인력 역량 유지 및 조직 경직성 방지 |
| **코소싱 (Co-Sourcing)** | 발주사 인력과 외주 전문 인력이 원팀으로 결합하여 프로젝트 수행 | 신기술(클라우드·AI) 파일럿 도입, 차세대 재구축 | 외부 기술의 내부 내재화 및 책임 분계점 명시 |
| **선택적 아웃소싱 (Buy)** | 인프라, 보안관제, 유지보수 등 표준화된 특정 영역만 분할 위탁 | SOC 보안관제, 클라우드 MSP 인프라 운영 | 공급자 간 인터페이스 관리 및 **SIAM** 체계 가동 |
| **전체 아웃소싱 (Total)** | 전산실 전체 인프라와 운영 업무를 단일 대형 SI 기업에 일괄 위탁 | 레거시 ERP 운영, 비핵심 계열사 전산실 통합 | **벤더 종속(Lock-in)** 방지 및 출구 전략 의무화 |

## Ⅳ. 전통적 아웃소싱 vs 멀티소싱(SIAM) vs 클라우드 관리형 서비스(MSP) 비교

> 단일 공급자 종속의 위험을 회피하기 위해 다중 전문 벤더를 조율하는 **SIAM**과 클라우드 **MSP** 모델로 진화함.

| 비교 항목 | 전통적 아웃소싱 (Single ITO) | 멀티소싱 (SIAM 기반) | 클라우드 관리형 서비스 (MSP) |
|---|---|---|---|
| 소싱 구조 | 단일 대형 SI 기업에 전산실 일괄 위탁 | 영역별 Best-of-breed 벤더 다수 + SIAM 통합자 | 퍼블릭 클라우드 인프라 전문 운영 위탁 |
| 책임 소재 | 단일 주사업자가 포괄적 책임 | **SIAM(Service Integration)** 조직이 핑퐁 조정 | CSP(인프라)와 MSP(운영)의 공동 책임 모델 |
| 유연성 | 계약 변경이 경직되고 신기술 도입 지연 | 우수 벤더 수시 교체 가능, 최신 기술 수용 용이 | 클라우드 네이티브 도구 기반 고도의 자동화 |
| 관리 복잡도 | 상대적으로 단순함 (단일 창구) | 매우 높음 (벤더 간 의존성 및 인터페이스 통제) | 클라우드 API 및 FinOps 비용 통제 요구 |
| 주요 위험 | **벤더 종속(Lock-in)**, 내부 역량 공동화 | 벤더 간 책임 전가, 통합 관리자 역량 부족 | 클라우드 보안 설정 오류, 비용 폭증(Bill Shock) |

## Ⅴ. 아웃소싱 실무 실패 요인과 공학적 통제 방안

> 내부 역량 공동화와 수박 SLA 현상을 차단하지 못하면 발주사는 통제권을 완전히 상실함.

| 위험 요인 | 발생 원인 | 공학적·관리적 통제 대책 | 검증 지점 |
|---|---|---|---|
| **역량 공동화 (Hollowing out)** | 모든 기술 검토를 외주사에 일임하여 내부 판단력 상실 | 아키텍처, 데이터 모델, 보안 통제는 **잔존 조직(RO)** 전담 | 기술 검토 및 형상 변경의 내부 승인율 100% |
| **공급자 종속 (Lock-in)** | 벤더 고유 프레임워크 사용 및 독점적 산출물 점유 | 표준 오픈소스 채택, 소스코드 및 설계서 형상관리 의무화 | 계약 만료 시 타 사업자 이관 테스트 통과 |
| **출구 전략 부재** | 계약 종료 시 공급자의 인수인계 비협조로 업무 마비 | 계약서에 **Exit Plan** 지원 조항 명시 및 전환 비용 지급 연계 | 업무 인수인계 기간 및 지식 이전 산출물 완성 |
| **수박 SLA 현상** | 겉으로는 지표 달성(녹색)이나 실 사용자는 불만족(적색) | 단순 가용성 외에 사용자 체감 품질(**XLA**) 병행 측정 | 최종 사용자 체감 만족도 및 장애 체감 시간 단축 |

## Ⅵ. 잔존 조직 거버넌스 중심의 기술사적 제언

> 아웃소싱은 통제를 포기하는 것이 아니라, 고도화된 거버넌스로 외부 전문성을 지휘하는 경영 기술이어야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: IT 아웃소싱의 성패는 수탁 업체의 기술력보다 위탁 발주사 내부 잔존 조직(Retained Organization)의 기술 판단력에 좌우됨. 모든 실무를 넘기더라도 시스템 아키텍처 승인권과 데이터 주권은 반드시 내부가 쥐고 있어야 함.
- 나라면: 아웃소싱 RFP 작성 단계부터 `ISO 37500 표준 준수 요구 → 잔존 조직(RO)의 아키텍처 형상 승인권 명시 → 수박 현상 방지를 위한 XLA 도입 → 계약 만료 6개월 전 출구 전략(Exit Plan) 상세 이행서 제출 의무화`를 조달 규격서에 확정하겠음.

### 실전 답안용 기술사적 제언

- 판정: 일방적 업무 위탁 탈피 및 잔존 조직(RO) 주도의 능동적 거버넌스 확립
- 대안: **RO-SIAM-공급사** 3계층 거버넌스 체계 및 **XLA** 결합형 계약 제도화
- 검증: 잔존 조직 전결권 준수율 100% · 출구 전략(Exit Plan) 사전 검증 통과
- 효과: 벤더 종속(Lock-in) 방지 및 비즈니스 변화에 따른 소싱 가역성 보장

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 아웃소싱 거버넌스 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>내부 역량 공동화 · 벤더 종속(Lock-in) · 수박 SLA 착시</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>잔존 조직(RO) 강화 + XLA 도입 + Exit Plan 계약 의무화</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>아키텍처 내부 승인권 · 지식 이전 매뉴얼 · 다중 벤더 조율</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>소싱 가역성 확보 · 비용 최적화 · 고품질 서비스 영속</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **IT 아웃소싱(IT Outsourcing)**은 핵심 역량 집중과 비용 최적화를 위해 IT 기획, 개발, 인프라 운영 업무의 일부 또는 전부를 외부 전문 기업에 위탁하여 **SLA** 기반으로 수행하는 전략적 소싱 관리 체계
- 목적: **Retained Organization(잔존 조직)** 중심의 IT 거버넌스 확립 및 운영 효율화 → **벤더 종속(Lock-in)** 방지 및 서비스 품질 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="ISO 37500 기반 IT 아웃소싱 생명주기 요약">
  <div class="itpe-pipeline-node"><strong>전략 수립</strong><small>Make or Buy · RO 설계</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>공급자 선정</strong><small>RFP · SLA/OLA 계약</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>이행·전환</strong><small>지식 이전(KT) · 병행 운영</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>운영·거버넌스</strong><small>SLA 모니터링 · Exit Plan</small></div>
</div>

### 3. 핵심 통제

- **역량 공동화 방지**: **Retained Organization(잔존 조직)**이 핵심 아키텍처와 데이터 주권을 전담
- **종속 방지 및 품질 통제**: 계약 시 **Exit Plan(출구 전략)**을 명문화하고, 체감 만족도를 반영하는 **XLA(eXperience Level Agreement)** 병행 운용

## 출제 이력과 검증 출처

- 제123회 정보관리기술사 1교시: IT 아웃소싱의 유형 및 계약 시 고려사항
- ISO, [ISO 37500:2014, Guidance on outsourcing](https://www.iso.org)
- ISO/IEC, [ISO/IEC 20000-1:2018, Information technology — Service management](https://www.iso.org)

## 학습 체크

- [ ] Make or Buy 의사결정 매트릭스 4개 분면(인소싱, 코소싱, 선택적, 전체)을 설명할 수 있는가?
- [ ] ISO 37500의 4단계 생명주기(전략, 조달, 전환, 거버넌스)를 도식화할 수 있는가?
- [ ] 벤더 종속(Lock-in)과 역량 공동화(Hollowing out)의 발생 원인 및 통제 대책을 제시할 수 있는가?
- [ ] 전통적 SLA와 사용자 경험 기반 XLA(eXperience Level Agreement)의 차이점을 서술할 수 있는가?

## 연결 토픽

- 이전 토픽: [EVM](./032_evm.md)
- 연관 토픽: [SLA](./006_sla.md), [ITSM](./044_itsm.md), [PMO](./004_pmo.md), [RFP](./049_rfp.md)
- 다음 토픽: [SWOT 분석](./034_swot_analysis.md)
