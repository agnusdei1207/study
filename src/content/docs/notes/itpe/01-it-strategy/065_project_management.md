---
title: "프로젝트 관리"
author: "Antigravity"
date: "2026-09-20T19:50:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 사업 및 조직 관리를 거쳐 프로젝트 관리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>사업 관리·PMO</span>
  <strong>프로젝트 관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **프로젝트 관리(PM)**는 한정된 기간과 자원 내에서 고유한 결과물을 인도하기 위해 삼중 제약(범위·일정·원가·품질)을 통제하며, 상위 **포트폴리오 관리** 및 **프로그램 관리**와 연계되어 전사 비즈니스 가치를 실현하는 거버넌스 체계
- 메커니즘: `포트폴리오(전략 연계) → 프로그램(시너지 편익) → 프로젝트(산출물 완성)` 3계층 수직 정렬 하에 `착수 → 기획 → 실행 → 감시·통제 → 종료` 5대 프로세스 순환
- 산출: 프로젝트 헌장 · **WBS(Work Breakdown Structure)** · 프로젝트 관리 계획서 · **EVM(Earned Value Management)** 분석서 · 인수 확인서

<div class="itpe-flow-map" role="img" aria-label="포트폴리오, 프로그램, 프로젝트 관리 3계층 거버넌스 흐름도">
  <div class="itpe-flow-node">
    <strong>전사 비즈니스 전략 및 투자 심의</strong>
    <small>Doing the right things · 자원 최적 배분</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>3대 계층 거버넌스 수직 정렬</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>포트폴리오</strong><span>전략적 가치 극대화 · 투자 우선순위화 · 위험 분산</span></div>
      <div class="itpe-flow-branch"><strong>프로그램</strong><span>연관 복수 프로젝트 통합 · 시너지 창출 · <span class="itpe-keyword"><strong>비즈니스 편익(Benefits)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>프로젝트</strong><span>단일 고유 산출물 적기 인도 · <span class="itpe-keyword"><strong>삼중 제약(Scope/Time/Cost)</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>PMBOK 7판 가치 인도 시스템(Value Delivery) 완성</strong>
    <small>하이브리드 테일러링 · 데이터 드리븐 PM · 조직 프로세스 자산화</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **PM(Project Management)**: 고유한 목표를 달성하기 위해 지식, 기술, 도구, 기법을 프로젝트 활동에 적용하는 관리 체계
- **포트폴리오 관리(Portfolio Management)**: 전사 전략 목표 달성을 위해 프로젝트, 프로그램, 운영 업무를 하나의 투자 묶음으로 통합 심의·선정하는 활동
- **프로그램 관리(Program Management)**: 개별 관리 시 불가능한 통합 시너지와 편익(Benefits) 창출을 위해 상호 연관된 복수 프로젝트를 묶어 조율하는 활동
- **WBS(Work Breakdown Structure)**: 프로젝트 전체 범위를 관리 가능한 계층적 작업 패키지(Work Package)로 분할한 작업 분류 체계
- **EVM(Earned Value Management)**: 범위, 일정, 원가 데이터를 종합 계측하여 공정 진척도와 비용 성과를 정량적으로 분석·예측하는 기법
- **CCB(Change Control Board)**: 프로젝트 기준선(Baseline) 변경 요구의 타당성을 공식 심의·승인·기각하는 변경통제위원회
- **PMBOK(Project Management Body of Knowledge)**: PMI가 제정한 프로젝트 관리 지식 체계 표준 (7판에서 가치 인도 및 12대 원칙으로 전면 개편)

</details>

## 딸려 나오는 하위 토픽

| 키워드 | 등급 | 학습 역할 및 연결 이유 | 핵심 질문/키워드 |
|---|---|---|---|
| **포트폴리오 관리** | B | 전사 전략과 프로젝트를 연계하여 투자 우선순위와 ROI를 최적화하는 최상위 의사결정 계층 | Doing the right things, 전략 정합성, 자원 배분, PPM |
| **IT 프로젝트 관리** | B | 단일 시스템의 범위, 일정, 원가를 통제하여 고유한 인도물을 생성하는 실행 단위 | Doing things right, 삼중 제약, WBS, EVM, CCB |
| **프로그램 관리** | B | 상호 연관된 복수 프로젝트를 조율하여 개별 프로젝트가 달성할 수 없는 비즈니스 편익을 실현하는 중간 계층 | Doing them together, 편익 실현(Benefits Realization), 의존성 조율 |

## 예상문제

> IT 프로젝트 관리에 대하여 다음을 설명하시오. 가. IT 프로젝트 관리의 개념 및 PMBOK 7판의 가치 인도 체계 나. 포트폴리오 관리, 프로그램 관리, 프로젝트 관리의 개념 비교 및 상호 관계 다. IT 프로젝트 5대 프로세스 그룹 및 실무 파행 방지를 위한 기술사적 통제 방안 (25점)

## Ⅰ. 가치 중심 프로젝트 거버넌스, 프로젝트 관리의 개요

> 프로젝트 관리는 단순 산출물 납품을 넘어 전사 비즈니스 가치를 인도하는 실행 메커니즘이며, 성패는 **WBS 기준선(Baseline)** 통제와 **비즈니스 편익(Benefits) 실현**으로 판정함.

- 정의: 한정된 기간과 자원 제약 내에서 고유한 목표와 제품·서비스를 완성하기 위해 기획, 실행, 감시·통제 기법을 적용하는 **체계적 공학 및 관리 활동**
- 목적: 삼중 제약 균형 달성, 결함 최소화 및 비즈니스 가치 적기 인도

## Ⅱ. 포트폴리오 vs 프로그램 vs 프로젝트 3계층 거버넌스 체계

> 세 계층은 상호 배타적인 것이 아니라, 전략(포트폴리오)에서 시너지(프로그램)를 거쳐 실행(프로젝트)으로 이어지는 수직적 가치 사슬임.

<div class="itpe-pipeline is-vertical" role="img" aria-label="포트폴리오, 프로그램, 프로젝트 3계층 거버넌스 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 포트폴리오 관리 (Portfolio Management)</strong></span>
    <div class="itpe-step-detail"><strong>Doing the right things</strong><span>전사 전략 연계, 투자 가치(ROI) 극대화 및 자원 우선순위 배분</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 프로그램 관리 (Program Management)</strong></span>
    <div class="itpe-step-detail"><strong>Doing them together</strong><span>복수 프로젝트 통합, 그룹 시너지 창출 및 비즈니스 편익 달성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 프로젝트 관리 (Project Management)</strong></span>
    <div class="itpe-step-detail"><strong>Doing things right</strong><span>삼중 제약(Scope/Time/Cost) 내에서 고유 산출물 적기 인도</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Strategic Value Chain</strong></span> · 포트폴리오(투자 전략) ↔ 프로그램(편익 시너지) ↔ 프로젝트(산출물 완결)</div>

### 3대 관리 계층의 비교

| 비교 항목 | 포트폴리오 관리 (Portfolio) | 프로그램 관리 (Program) | 프로젝트 관리 (Project) |
|---|---|---|---|
| **핵심 질문** | Doing the right things? | Doing them together? | Doing things right? |
| **관리 대상** | 전사 프로젝트, 프로그램, 운영 업무 일체 | 상호 연관된 복수의 하위 프로젝트군 | 단일의 고유한 프로젝트 작업 일체 |
| **초점 및 목표** | 전사 전략 정렬, **ROI 극대화**, 위험 분산 | **통합 시너지 창출**, 비즈니스 편익 실현 | **삼중 제약(범위·일정·원가)** 준수 및 산출물 납품 |
| **책임자** | 포트폴리오 매니저, 최고경영진(C-Level) | 프로그램 매니저 (PgMP) | 프로젝트 매니저 (PMP) |
| **핵심 산출물** | 포트폴리오 헌장, 자원 배분 로드맵 | 편익 관리 계획서, 통합 마스터 일정 | **WBS**, 프로젝트 관리 계획서, 결과물 |
| **성공 판정** | 전사 사업 가치 및 재무 성과 달성도 | 집합적 편익(Benefits) 실현 여부 | 산출물 납기 준수, 품질 및 예산 일치 |

## Ⅲ. IT 프로젝트 관리 5대 프로세스 그룹 및 통제 흐름

> 착수부터 종료까지 프로세스는 일회성으로 끝나지 않으며, 감시 및 통제 그룹이 전 주기에 걸쳐 기준선 변경을 감시함.

| 프로세스 그룹 | 주요 수행 활동 | 핵심 산출물 (ITTO) | 실무 통제 기준 |
|---|---|---|---|
| **1. 착수 (Initiating)** | 프로젝트 목적 수립, 초기 타당성 분석, PM 권한 승인 | **프로젝트 헌장(Project Charter)** · 이해관계자 등록부 | 스폰서 공식 서명 확보 |
| **2. 기획 (Planning)** | 범위·일정·원가 베이스라인 확정, 위험/품질 계획 구체화 | **WBS** · 일정 네트워크 공정표 · 프로젝트 관리 계획서 | 기준선(Baseline) 잠금(Freeze) |
| **3. 실행 (Executing)** | 작업 패키지 구현, 팀 빌딩, 품질 보증, 자원 조달 | 작업 인도물(Deliverables) · 변경 요청서(CR) | 품질 기준 충족 여부 점검 |
| **4. 감시/통제 (M&C)** | 실적 계측, 편차 분석, 위험 재평가, **CCB 변경 심의** | 작업 성과 보고서 · **EVM(CPI, SPI)** 지표 | 기준선 대비 편차 10% 이내 통제 |
| **5. 종료 (Closing)** | 고객 인수 검수, 계약 종결, 교훈(Lessons Learned) 정리 | 최종 검수 확인서 · 조직 프로세스 자산(OPA) 갱신 | 미해결 결함 0건 및 자산화 |

## Ⅳ. 예측적(워터폴) vs 적응적(애자일) vs 하이브리드 관리 테일러링

> 프로젝트 특성에 따라 개발 모델을 재단(Tailoring)해야 납기 지연과 품질 결함을 방어할 수 있음.

| 비교 항목 | 예측적 접근법 (Waterfall) | 적응적 접근법 (Agile) | 하이브리드 접근법 (Hybrid) |
|---|---|---|---|
| **요구사항 특성** | 사업 초기 명확히 확정 가능 | 불확실성이 극심하여 잦은 변경 예상 | 핵심 코어는 고정, UI 및 상세 기능은 가변적 |
| **범위 관리** | WBS 기반 엄격한 스코프 베이스라인 | 프로덕트 백로그 기반 스프린트 우선순위화 | **상위 마일스톤 고정 + 하위 백로그 적응** |
| **인도 방식** | 프로젝트 종료 시점 일괄 인도 (Big Bang) | 1~4주 스프린트 단위 점진적 가치 인도 | 릴리즈 단위 단계적 배포 및 조기 가치 검증 |
| **변경 통제** | **CCB 승인 절차**를 통한 변경 엄격 억제 | 스프린트 회고 및 백로그 동적 재배치 | **계약 마일스톤은 CCB, 세부 기능은 애자일 수용** |
| **대표 적용처** | 금융 계정계, 공공 대규모 원장 구축 | 모바일 앱, 빅데이터 분석, AI 서비스 개발 | **대규모 차세대 엔터프라이즈 DX 사업** |

## Ⅴ. 실무 프로젝트 위험 요인 및 기술사적 대책

> 프로젝트 실패의 주원인은 기술 부족보다 비공식적 요구사항 확대와 주관적 공정 보고에 기인함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **범위 크립(Scope Creep) 누적** | 공식 **변경통제위원회(CCB)** 운영 및 WBS 베이스라인 잠금 | 비공식 변경 0건 달성 및 승인된 변경만 일정·예산 보정 |
| **주관적 진척 보고 왜곡** | **EVM 기법** 및 0/100 룰(완전 완료 시에만 가치 인정) 강제 | SPI/CPI 지표 기반 객관적 공정 진척 및 예산 계측 |
| **인터페이스 결함 막판 폭발** | **일일 CI/CD 자동 빌드** 및 주간 인터페이스 통합 테스트 | 결함 조기 발견 및 인터페이스 불일치 리스크 사전 해소 |
| **전략과 무관한 프로젝트 난립** | **포트폴리오 관리(PPM)** 투자 심의 및 비즈니스 케이스 평가 | 전사 전략 정합성 확보 및 고수익 프로젝트 자원 집중 |

## Ⅵ. 엔지니어링 데이터 드리븐 PM 중심의 결론

> 프로젝트 관리는 주관적 보고서 작성을 탈피하여, 실제 코드 저장소와 빌드 파이프라인에서 추출되는 **엔지니어링 메트릭 기반 데이터 드리븐 PM**으로 진화해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 프로젝트 파행은 개발자가 코드를 못 짜서가 아니라, 비공식 구두 요구사항이 누적되어 통제 불능(Scope Creep) 상태에 빠지고 이를 PM이 정량적으로 감지하지 못할 때 발생함.
- 나라면: 프로젝트 룸에 화려한 PPT 보고서 대신 `Git 커밋 빈도 + CI/CD 빌드 성공률 + 지라(Jira) 결함 미해결 번다운 차트 + EVM 지표`를 결합한 실시간 데이터 대시보드를 전광판으로 띄워 객관적 수치로만 진척을 통제하겠음.

### 실전 답안용 기술사적 제언

- 판정: 주관적 보고서보다 형상 및 빌드 기반 정량 데이터 통제 여부로 성패 판정
- 대안: **데이터 드리븐 PMO 대시보드** + **엄격한 CCB 품질 게이트(Quality Gate)** 운영
- 검증: CPI/SPI 지표 0.9 이상 유지 · 스프린트 번다운 완료율 · 미승인 변경 0건
- 효과: 스코프 크립 원천 차단 · 납기 지연 방지 및 PMBOK 7판 가치 인도 체계 완성

<div class="itpe-pipeline is-vertical" role="img" aria-label="데이터 드리븐 프로젝트 관리 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>취약점</strong><span>구두 요구에 의한 스코프 크립, 주관적 공정 왜곡 및 통합 결함 지연 발견</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>데이터 기반</strong><span>Git/CI 연동 데이터 드리븐 PM 및 하이브리드 거버넌스(CCB+스프린트) 확립</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>목표 지표</strong><span>EVM 정량 지표 0.95 이상, WBS 기준선 일치율 100% 및 결함 조기 수렴</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>가치 창출</strong><span>예산·납기 초과 방지, 고품질 산출물 인도 및 전사 비즈니스 가치 실현</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **프로젝트 관리(Project Management)**는 고유한 제품·서비스를 완성하기 위해 착수·기획·실행·통제·종료 프로세스를 적용하여 삼중 제약을 통제하고 가치를 인도하는 체계적 활동
- 목적: 삼중 제약 균형 달성, 결함 방지 및 비즈니스 편익 실현

### 2. 프로젝트, 프로그램, 포트폴리오 3대 관리 체계

<div class="itpe-pipeline is-vertical" role="img" aria-label="프로젝트 관리 3대 체계 요약 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>포트폴리오 관리</strong>
    <div class="itpe-step-detail"><strong>전략 정렬</strong><span>전사 투자 최적화 (Doing the right things)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>프로그램 관리</strong>
    <div class="itpe-step-detail"><strong>시너지 창출</strong><span>복수 프로젝트 통합 편익 (Doing them together)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>프로젝트 관리</strong>
    <div class="itpe-step-detail"><strong>실행 통제</strong><span>삼중 제약 통제 및 산출물 완성 (Doing things right)</span></div>
  </div>
</div>

### 3. 핵심 통제

- **WBS 및 CCB 기준선 관리**: WBS로 작업을 완전 분할하고 기준선 잠금 후, 모든 변경 요구는 공식 **CCB(Change Control Board)**를 통해서만 심의·반영하여 스코프 크립 원천 차단
- **하이브리드 테일러링**: 계약 및 거버넌스는 워터폴 마일스톤으로 통제하고, 개발 상세 구현은 2주 단위 애자일 스프린트로 유연하게 대응

## 출제 이력과 검증 출처

- 제135회 정보관리기술사 3교시 1번: IT 프로젝트 관리의 개념, 5대 프로세스, 프로그램/포트폴리오 관리 비교
- 제125회 정보관리기술사 1교시: PMBOK 7판 핵심 원칙 및 성과 영역
- PMI, 'A Guide to the Project Management Body of Knowledge (PMBOK Guide 7th Edition)'
- ISO 21500:2021, 'Project, programme and portfolio management'

## 학습 체크

- [ ] 프로젝트, 프로그램, 포트폴리오 관리의 차이점과 상호 연결성을 설명할 수 있는가?
- [ ] IT 프로젝트 관리 5대 프로세스 그룹과 주요 산출물(ITTO)을 제시할 수 있는가?
- [ ] 예측적(워터폴), 적응적(애자일), 하이브리드 관리 기법의 장단점을 비교할 수 있는가?
- [ ] 스코프 크립 방지를 위한 CCB와 EVM 기반 공정 통제 방안을 논술할 수 있는가?

## 연결 토픽

- 이전 토픽: [AI 에너지 인프라](./060_ai_energy_infrastructure.md)
- 연관 토픽: [WBS](./007_wbs.md), [EVM](./032_evm.md), [PMO](./004_pmo.md), [ISO 21500](./043_iso_21500.md)
- 다음 토픽: [협상에 의한 계약 제안서 평가](./066_negotiated_contract_proposal_evaluation.md)
