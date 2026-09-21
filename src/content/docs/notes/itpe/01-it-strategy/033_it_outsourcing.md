---
title: "IT 아웃소싱"
author: "Antigravity"
date: "2026-09-21T18:00:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 IT 운영전략과 서비스 관리를 거쳐 IT 아웃소싱으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>IT 운영전략·소싱 거버넌스</span>
  <strong>IT 아웃소싱</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 비핵심 IT 업무를 외부 전문 기업에 위탁하여 비용 최적화와 품질을 도모하되, 아키텍처·보안·데이터의 통제권은 내부 잔존 조직(**RO**)이 유지하는 전략적 소싱 관리 체계.
- 메커니즘: **Make or Buy** 전략 수립 → RFP 및 **SLA/OLA** 계약 체결 → 지식 이전(KT) 및 전환 → 운영 통제 및 체감 품질(**XLA**) 평가 → **Exit Plan(출구 전략)** 실행 및 재소싱.
- 통제: 역량 공동화(Hollowing-out) 방지 · 벤더 종속(**Lock-in**) 탈피를 위한 오픈 아키텍처 · 계약 시 타 사업자 이관 테스트 의무화.

<div class="itpe-flow-map" role="img" aria-label="IT 아웃소싱 Make or Buy 판단부터 생명주기 및 거버넌스 흐름">
  <div class="itpe-flow-node">
    <strong>소싱 타당성 분석</strong>
    <small>전략적 중요도 vs 내부 역량 (Make or Buy)</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>소싱 포트폴리오 확정</small></div>
  <div class="itpe-flow-node is-current">
    <strong>아웃소싱 실무 생명주기</strong>
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
- **ISO 37500**: 산업·규모와 무관하게 아웃소싱의 주요 단계·프로세스·거버넌스를 안내하는 국제표준
- **SLA(Service Level Agreement)**: 발주사와 공급자 간에 합의된 IT 서비스 품질 수준, 가용성 지표 및 미달 시 위약금(Penalty)을 명시한 협약서
- **OLA(Operational Level Agreement)**: 최종 SLA 목표 달성을 지원하기 위해 공급사 내부 팀 및 협력사 간에 맺는 운영 수준 협약서
- **RO(Retained Organization)**: 업무 위탁 후에도 발주사에 잔류하여 아키텍처 기준선, 데이터 보안 및 계약 통제권을 행사하는 내부 잔존 조직
- **Exit Plan(출구 전략)**: 계약 만료 또는 분쟁 발생 시 서비스 연속성을 유지하며 다른 공급사로 전환하거나 인소싱하기 위한 사전 인수인계 계획
- **SIAM(Service Integration and Management)**: 다중 공급자(Multi-vendor)의 이종 IT 서비스를 통합 조율하여 단일 서비스로 제공하는 소싱 관리 모델
- **XLA(eXperience Level Agreement)**: 단순 시스템 가용성을 넘어 실제 최종 사용자가 체감하는 업무 만족도를 측정·관리하는 경험 수준 협약

</details>

## 예상문제

> IT 아웃소싱의 Make or Buy 의사결정과 실무 생명주기를 설명하고, Lock-in·역량 공동화 방지를 위한 거버넌스와 Exit Plan을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 핵심 역량 집중과 비용 최적화, IT 아웃소싱의 개요

> IT 아웃소싱은 개발·운영 업무를 위탁하더라도 IT 거버넌스와 아키텍처 통제권은 **Retained Organization(잔존 조직)**에 유지해야 하며, 성패는 **Lock-in** 없는 **Exit Plan**의 완결성으로 판정함.

- 정의: IT 업무 일부 또는 전부를 외부 전문조직에 위탁하고 계약·서비스 수준으로 성과와 위험을 관리하는 소싱 체계
- 목적: 핵심 역량 집중, 운영 비용 최적화, 서비스 품질 확보

## Ⅱ. IT 아웃소싱 실무 생명주기

> ISO 37500의 수명주기·거버넌스 관점을 답안용으로 전략·선정계약·전환·운영종료 절차로 구조화함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 아웃소싱 실무 생명주기의 단계별 활동과 산출물">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>① 전략 수립</strong></span>
      <strong>활동</strong><span>Make or Buy · 범위·잔존역량 결정</span><strong>산출</strong><span>소싱 전략</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>② 공급자 선정·계약</strong></span>
      <strong>활동</strong><span>RFP · 제안평가 · 책임·SLA 합의</span><strong>산출</strong><span>계약서 · SLA</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>③ 이행·전환</strong></span>
      <strong>활동</strong><span>지식·자산·계정 인계 · 병행운영</span><strong>산출</strong><span>전환계획 · 인수인계서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>④ 운영·종료</strong></span>
      <strong>활동</strong><span>SLA 평가 · 변경통제 · Exit Plan 검증</span><strong>산출</strong><span>성과보고 · 전환·종료계획</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Governance</strong></span> · 발주자와 공급자가 공동으로 성과·위험·변경을 관리하되 최종 통제권은 발주자가 유지</div>

## Ⅲ. IT 소싱 의사결정 모델 (Make or Buy 매트릭스)

> 기업의 전략적 중요도와 내부 기술 역량의 2축 평가를 통해 최적의 소싱 유형을 판정함.

<div class="itpe-diagram-box">
  <svg viewBox="0 0 520 220" width="100%" height="220" role="img" aria-label="IT 소싱 Make or Buy 2x2 매트릭스 다이어그램">
    <!-- Axes and Background Grid -->
    <line x1="80" y1="20" x2="80" y2="180" stroke="var(--sl-color-gray-4)" stroke-width="2"/>
    <line x1="80" y1="180" x2="480" y2="180" stroke="var(--sl-color-gray-4)" stroke-width="2"/>
    <text x="35" y="100" fill="var(--sl-color-gray-2)" font-size="10" font-weight="bold" transform="rotate(-90 40 100)">내부 기술 역량</text>
    <text x="250" y="200" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="10" font-weight="bold">전략적 중요도 (비즈니스 핵심도)</text>
    <text x="175" y="195" fill="var(--sl-color-gray-3)" font-size="9">낮음(Low)</text>
    <text x="375" y="195" fill="var(--sl-color-gray-3)" font-size="9">높음(High)</text>
    <text x="50" y="150" fill="var(--sl-color-gray-3)" font-size="9">낮음</text>
    <text x="50" y="55" fill="var(--sl-color-gray-3)" font-size="9">높음</text>

    <!-- Quadrant Division Lines -->
    <line x1="280" y1="20" x2="280" y2="180" stroke="var(--sl-color-gray-5)" stroke-width="1.5" stroke-dasharray="3,3"/>
    <line x1="80" y1="100" x2="480" y2="100" stroke="var(--sl-color-gray-5)" stroke-width="1.5" stroke-dasharray="3,3"/>

    <!-- Quadrant 1 (Top-Right): High Strategy, High Capability -> Make (Insourcing) -->
    <rect x="290" y="25" width="180" height="70" rx="5" fill="var(--sl-color-blue-low)" stroke="var(--sl-color-blue)" stroke-width="1.5"/>
    <text x="380" y="45" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="11" font-weight="bold">인소싱 (Make)</text>
    <text x="380" y="62" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">핵심 아키텍처 · 데이터 주권</text>
    <text x="380" y="78" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">경쟁우위 핵심 시스템 내재화</text>

    <!-- Quadrant 2 (Top-Left): Low Strategy, High Capability -> Selective / Commercialize -->
    <rect x="90" y="25" width="180" height="70" rx="5" fill="var(--sl-color-green-low)" stroke="var(--sl-color-green)" stroke-width="1.5"/>
    <text x="180" y="45" text-anchor="middle" fill="var(--sl-color-green-high)" font-size="11" font-weight="bold">선택적 소싱 (Selective)</text>
    <text x="180" y="62" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">기술력 있으나 비핵심 영역</text>
    <text x="180" y="78" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">외부 솔루션 활용 및 잉여자원화</text>

    <!-- Quadrant 3 (Bottom-Right): High Strategy, Low Capability -> Co-Sourcing -->
    <rect x="290" y="105" width="180" height="70" rx="5" fill="var(--sl-color-purple-low)" stroke="var(--sl-color-purple)" stroke-width="1.5"/>
    <text x="380" y="125" text-anchor="middle" fill="var(--sl-color-purple-high)" font-size="11" font-weight="bold">코소싱 (Co-Sourcing)</text>
    <text x="380" y="142" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">신기술 파일럿 · 차세대 구축</text>
    <text x="380" y="158" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">원팀 구성 ➔ 내부 역량 이전</text>

    <!-- Quadrant 4 (Bottom-Left): Low Strategy, Low Capability -> Total Buy -->
    <rect x="90" y="105" width="180" height="70" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>
    <text x="180" y="125" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="11" font-weight="bold">전체 위탁 (Total Buy)</text>
    <text x="180" y="142" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">인프라 유지보수 · PC 관리</text>
    <text x="180" y="158" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">표준화 기반 비용 절감 위주</text>
  </svg>
</div>

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

> 내부 역량 공동화와 SLA 착시를 방치하면 발주자의 기술·계약 통제력이 약화됨.

| 위험 | 대책 | 효과 |
|---|---|---|
| **역량 공동화(Hollowing out)** | 아키텍처·데이터·보안 의사결정은 잔존 조직이 담당 | 내부 통제역량 유지 |
| **공급자 종속 (Lock-in)** | 표준 오픈소스 채택, 소스코드 및 설계서 형상관리 의무화 | 계약 만료 시 타 사업자 이관 테스트 통과 |
| **출구 전략 부재** | 계약서에 Exit Plan·전환지원·자료반환 명시 | 서비스 전환 가능성 확보 |
| **수박 SLA 현상** | 단순 가용성 외에 사용자 체감 품질(**XLA**) 병행 측정 | 최종 사용자 체감 만족도 및 장애 체감 시간 단축 |

## Ⅵ. 잔존 조직 거버넌스 중심의 기술사적 제언

> 아웃소싱은 통제를 포기하는 것이 아니라, 고도화된 거버넌스로 외부 전문성을 지휘하는 경영 기술이어야 함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]` 실행을 위탁해도 아키텍처·데이터·보안·계약 판단까지 위탁하면 공급자를 평가하거나 교체할 능력을 잃음.
- `나라면` 잔존 조직(RO)의 기술 통제권을 제도화하고, 계약 만료 6개월 전 실서버 데이터를 기반으로 대체 벤더 또는 내부로의 가상 이관 리허설(Exit Drill)을 계약서 필수 조항으로 못박겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 발주사 단독으로 소스코드 빌드·배포·형상 통제가 가능하고 타 사업자 이관 기간이 30일 이내인지 여부.
- **공학적 대안**: 단일 대형 위탁 탈피, **SIAM(Service Integration and Management)** 기반 멀티벤더 분할 및 **XLA** 결합.
- **검증 절차**: 계약 단계에서 **Exit Plan** 및 전환 지원 의무 조항 명시, 반기별 산출물 최신화 및 역량 공동화 점검.
- **기대 효과**: 공급사 기술 종속 탈피, 핵심 경쟁우위 기술 내재화, 서비스 안정성 및 최종 사용자 체감 만족도 제고.

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 아웃소싱 거버넌스 제언 흐름">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>현행 한계</strong>
      <strong>문제</strong><span>역량 공동화 · Lock-in · SLA 착시</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>개선 대안</strong>
      <strong>대안</strong><span>잔존 조직 권한 · 성과·경험 지표 · Exit Plan</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>검증 기준</strong>
      <strong>판정</strong><span>내부 승인권 · 지식·자료 반환 · 전환 리허설</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>실행 효과</strong>
      <strong>효과</strong><span>통제권 유지 · 소싱 가역성 · 서비스 연속성</span>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **IT 아웃소싱(IT Outsourcing)**은 핵심 역량 집중과 비용 최적화를 위해 IT 기획, 개발, 인프라 운영 업무의 일부 또는 전부를 외부 전문 기업에 위탁하여 **SLA** 기반으로 수행하는 전략적 소싱 관리 체계
- 목적: 핵심 역량 집중, 운영 비용 최적화, 서비스 품질 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 아웃소싱 실무 생명주기 요약">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>전략 수립</strong>
      <span>Make or Buy · RO 설계</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>공급자 선정</strong>
      <span>RFP · SLA/OLA 계약</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>이행·전환</strong>
      <span>지식 이전(KT) · 병행 운영</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>운영·거버넌스</strong>
      <span>SLA 모니터링 · Exit Plan</span>
    </div>
  </div>
</div>

### 3. 핵심 통제

- **역량 공동화 방지**: **Retained Organization(잔존 조직)**이 핵심 아키텍처와 데이터 주권을 전담
- **종속 방지 및 품질 통제**: 계약 시 **Exit Plan(출구 전략)**을 명문화하고, 체감 만족도를 반영하는 **XLA(eXperience Level Agreement)** 병행 운용

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [ISO 37500:2014: Guidance on outsourcing](https://www.iso.org/standard/56269.html)
- [ISO/IEC 20000-1:2018: Service management system requirements](https://www.iso.org/standard/70636.html)

## 학습 체크

- [ ] Ⅰ. IT 아웃소싱의 정의·목적과 잔존 조직의 필요성을 설명할 수 있는가?
- [ ] Ⅱ. 전략·선정계약·전환·운영종료의 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ. 인소싱·코소싱·선택적·전체 아웃소싱의 선택기준을 설명할 수 있는가?
- [ ] Ⅳ. 단일·멀티소싱·MSP를 구조·책임·위험으로 비교할 수 있는가?
- [ ] Ⅴ~Ⅵ. Lock-in·역량 공동화·Exit Plan 부재의 통제방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [EVM](./032_evm.md)
- 연관 토픽: [SLA](./006_sla.md), [ITSM](./044_itsm.md), [PMO](./004_pmo.md), [RFP](./049_rfp.md)
- 다음 토픽: [SWOT 분석](./034_swot_analysis.md)
