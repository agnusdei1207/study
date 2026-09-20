---
title: "CCPM(Critical Chain, TOC)"
author: "Antigravity"
date: "2026-09-20T19:33:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 일정 및 자원 관리를 거쳐 CCPM으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 일정·자원 관리</span>
  <strong>CCPM(Critical Chain, TOC)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 골드랫 박사의 **TOC(제약이론)**를 적용하여 개별 안전마진을 회수하고, 자원 제약 기반의 크리티컬 체인과 **3대 버퍼(PB/FB/RB)**로 납기를 통제하는 방법론
- 메커니즘: 50% 공격적 공기 산정 → 자원 경합 해소 및 크리티컬 체인 확정 → PB/FB/RB 배치 → **3-Zone 신호등(녹/황/적)** 버퍼 소진율 관리
- 산출: 크리티컬 체인 네트워크도 · 버퍼 크기 산출서 · 피버 차트(Fever Chart) · 버퍼 소진율 주간 보고서

<div class="itpe-flow-map" role="img" aria-label="전통 일정의 안전마진 낭비 극복 및 CCPM 3대 버퍼 통합 통제 흐름">
  <div class="itpe-flow-node">
    <strong>전통적 일정 낭비 (CPM의 한계)</strong>
    <div class="itpe-step-detail"><span>파킨슨 법칙 (시간 채우기) + 학생 증후군 (막판 미루기)</span></div>
  </div>
  <div class="itpe-flow-arrow">↓<span>안전마진 50% 회수 및 통합</span></div>
  <div class="itpe-flow-node is-current">
    <strong>크리티컬 체인 및 3대 버퍼 체계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>PB</strong><span><span class="itpe-keyword"><strong>프로젝트 버퍼(Project Buffer)</strong></span>: 전체 납기 보증</span></div>
      <div class="itpe-flow-branch"><strong>FB</strong><span><span class="itpe-keyword"><strong>피딩 버퍼(Feeding Buffer)</strong></span>: 비임계 경로 합류 지연 차단</span></div>
      <div class="itpe-flow-branch"><strong>RB</strong><span><span class="itpe-keyword"><strong>자원 버퍼(Resource Buffer)</strong></span>: 병목 자원 사전 대기 알림</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<span>진척도 통제</span></div>
  <div class="itpe-flow-node">
    <strong>3-Zone 버퍼 소진율 관리</strong>
    <div class="itpe-step-detail"><span>녹색(0~33%) 정상 ➔ 황색(34~66%) 원인분석 ➔ 적색(67~100%) 비상개입</span></div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **CCPM(Critical Chain Project Management)**: 엘리 골드랫의 제약이론(TOC)을 기반으로 자원 종속성을 반영하고 버퍼를 중앙 집중 관리하는 일정 관리 기법
- **TOC(Theory of Constraints)**: 시스템의 처리량을 제한하는 유일한 제약 요인(병목)을 찾아 집중 개선하는 경영 공학 이론
- **파킨슨 법칙(Parkinson's Law)**: 어떤 일에 할당된 시간이 주어지면 실제 필요한 공수와 무관하게 그 시간을 모두 써버리는 인간의 행동 경향
- **학생 증후군(Student Syndrome)**: 시험 전날 벼락치기를 하듯 마감 시점이 임박할 때까지 작업을 착수하지 않고 지연시키는 심리적 현상
- **PB(Project Buffer)**: 크리티컬 체인 맨 끝에 배치하여 전체 프로젝트 납기를 보증하는 통합 완충 시간
- **FB(Feeding Buffer)**: 비임계 경로가 크리티컬 체인에 합류하는 지점에 삽입하여 비임계 작업 지연이 주공정으로 전이되는 것을 방어하는 버퍼
- **RB(Resource Buffer)**: 크리티컬 체인 작업 착수 직전에 자원이 즉각 투입될 수 있도록 준비시키는 사전 통보(Alert) 메커니즘
- **Fever Chart(피버 차트)**: 가로축(크리티컬 체인 완료율)과 세로축(버퍼 소진율) 상에 진척 궤적을 표시하여 위험을 조기 경보하는 그래프

</details>

## 예상문제

> 전통적인 임계경로법(CPM)의 한계점과 이를 극복하기 위한 골드랫 박사의 제약이론(TOC) 기반 크리티컬 체인 프로젝트 관리(CCPM, Critical Chain Project Management)의 개념, 핵심 메커니즘, 3대 버퍼(PB, FB, RB)의 역할 및 버퍼 소진율 관리 방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 키워드 | 등급 | 역할 및 핵심 내용 |
|---|---|---|
| **01-115 CCPM(Critical Chain Project Management)** | C | 제약이론(TOC) 기반 자원 제약 반영 크리티컬 체인 도출 및 3대 버퍼(PB, FB, RB) 통합 통제 기법 |

## Ⅰ. 인간 행동 심리와 자원 제약을 극복하는 일정 공학, CCPM의 개요

> 개별 안전마진을 회수해 **파킨슨 법칙**과 **학생 증후군**을 차단하고, **자원 제약(Critical Chain)**과 **3대 버퍼(PB/FB/RB)**로 납기를 보장함.

- 정의: **TOC(Theory of Constraints)** 기반으로 작업 선후행 관계와 자원 제약을 동시 반영한 크리티컬 체인을 도출하고, 통합 버퍼로 납기를 통제하는 **프로젝트 일정 관리 기법**
- 목적: 숨겨진 안전마진 낭비 방지, 멀티태스킹 오버헤드 제거 및 **버퍼 소진율(3-Zone)** 기반 선제적 납기 관리

## Ⅱ. CCPM 3대 버퍼 체계 및 4단계 일정 통제 방법론

> 50% 공격적 공기 산정부터 크리티컬 체인 확정, 버퍼 배치, 3-Zone 신호등 통제로 이어지는 파이프라인을 운영함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="CCPM 4단계 일정 수립 및 버퍼 관리 프로세스">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 50% 공격적 공기 산정</strong></span>
    <div class="itpe-step-detail"><strong>마진 회수</strong><span>개별 작업 안전마진 50% 강제 회수 및 공격적 WBS 수립</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 자원 종속성 분석 및 크리티컬 체인 확정</strong></span>
    <div class="itpe-step-detail"><strong>자원 제약</strong><span>자원 경합 해소 및 자원 제약 반영 최장 경로(Critical Chain) 도출</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 3대 버퍼(PB, FB, RB) 최적 배치</strong></span>
    <div class="itpe-step-detail"><strong>통합 완충</strong><span>체인 끝 PB, 비임계 합류점 FB, 자원 직전 RB 배치</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 3-Zone 신호등 버퍼 소진율 관리</strong></span>
    <div class="itpe-step-detail"><strong>위험 경보</strong><span>체인 진척 대비 버퍼 소진율(Green/Yellow/Red) 실시간 모니터링</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>버퍼 추적성</strong></span> · 50% 공기 절감액 ↔ PB/FB 통합 풀 ↔ Fever Chart 신호등 통제 100% 일치</div>

### CCPM 3대 버퍼 체계

| 버퍼 종류 | 영문 명칭 | 배치 위치 | 핵심 역할 및 운영 기준 |
|---|---|---|---|
| **프로젝트 버퍼** | **PB (Project Buffer)** | 크리티컬 체인의 최종 맨 끝에 배치 | 프로젝트 전체 납기를 보증하며, 회수된 전체 마진의 약 50% 수준을 중앙 집중 할당 |
| **피딩 버퍼** | **FB (Feeding Buffer)** | 비임계 체인이 크리티컬 체인과 합류하는 지점 | 비임계 작업의 지연이 주공정(크리티컬 체인)으로 전이되는 병목 현상을 원천 차단 |
| **자원 버퍼** | **RB (Resource Buffer)** | 크리티컬 체인 작업에 자원이 투입되기 직전 | 물리적 시간이 아닌 '사전 알림(Alert)'으로, 핵심 병목 인력/장비의 즉각 투입 대기 유도 |

## Ⅲ. 전통적 임계경로법(CPM) vs 크리티컬 체인(CCPM) 비교

> CPM은 논리적 선후행과 개별 마진 중심이나, CCPM은 자원 제약과 중앙 집중 버퍼 중심임.

| 비교 항목 | 전통적 임계경로법 (CPM) | 크리티컬 체인 프로젝트 관리 (CCPM) |
|---|---|---|
| **제약 조건 고려** | 작업 간 **논리적 선후행 의존성**만 고려 | 작업 간 논리적 의존성 + **자원 가용성(제약)** 동시 고려 |
| **공기 산정 기준** | 80~90% 달성 확률 (작업자별 숨은 마진 포함) | **50% 달성 확률 (공격적 추정, 마진 회수)** |
| **버퍼 관리 방식** | 개별 작업마다 여유시간(Float/Slack) 분산 배치 | 개별 마진 회수 후 **집중 버퍼(PB, FB)**로 통합 관리 |
| **진척 통제 지표** | 개별 작업 마감일 준수율, EVM (SPI, CPI) | 크리티컬 체인 진척률 대비 **버퍼 소진율(Buffer Consumption)** |
| **인간 행동 통제** | 파킨슨 법칙, 학생 증후군으로 시간 낭비 | 개별 마감일 폐지, 릴레이 주자식 완료 즉시 인계 |

## Ⅳ. 실무 적용 시 주요 왜곡 요인과 통제 대책

> 개발자의 50% 공기 거부감과 다중 프로젝트 자원 경합을 극복하기 위해 심리적 안전감과 DBR을 적용해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **개발자의 50% 공기 단축 저항** | "개별 마감일 미준수는 문책하지 않으며 버퍼가 흡수한다"는 심리적 안전감 제도화 | 정직하고 공격적인 일정 산출 유도 |
| **다중 프로젝트 간 자원 경합** | PMO 차원의 **드럼-버퍼-로프(DBR)** 적용 및 전사 단일 우선순위 큐 강제 | 비효율적 멀티태스킹 근절 |
| **버퍼 관리 형식화** | 도구 연계 **피버 차트(Fever Chart)** 실시간 대시보드 시각화 | 프로젝트 납기 지연 선제 경보 |

## Ⅴ. 성공적 CCPM 정착을 위한 기술사적 제언

> 개별 마감일 요구를 폐지하고 남은 작업 시간(Remaining Duration) 기반 피버 차트를 운영해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 프로젝트가 지연되는 이유는 엔지니어가 게을러서가 아니라, 개별 작업에 숨겨둔 안전 마진이 파킨슨 법칙과 학생 증후군에 의해 흔적도 없이 사라지기 때문임. CCPM은 수학적 일정 계산을 넘어 '인간의 일하는 방식을 바꾼 행동 공학적 혁신'임.
- 나라면: 개발자에게 "언제 끝나느냐"는 마감일을 묻지 않고, 매일 아침 스크럼에서 [남은 예상 작업 시간(Remaining Duration)]만을 수집하겠음. 이를 바탕으로 '피버 차트(Fever Chart)'를 실시간 렌더링하여, 버퍼 소진율이 황색 구역에 진입하는 순간 즉각 서브 개발자를 페어링 투입하는 '동적 버퍼 수호 거버넌스'를 정립하겠음.

### 실전 답안용 기술사적 제언

- 판정: 개별 마감일 압박에서 크리티컬 체인 진척률 및 버퍼 소진율 관리로 전환
- 대안: **Fever Chart 실시간 시각화** 및 **드럼-버퍼-로프(DBR) 멀티 프로젝트 자원 통제**
- 검증: 개별 마진 50% 회수율 100% · 피버 차트 적색 구역 진입 시 24시간 내 자원 투입
- 효과: 프로젝트 전체 공기 25% 단축 · 납기 준수율 98% 달성 및 멀티태스킹 낭비 제거

<div class="itpe-pipeline is-vertical" role="img" aria-label="CCPM 기반 납기 단축 및 버퍼 통제를 위한 기술사적 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>마진 낭비</strong><span>개별 작업자 안전마진 은닉 및 학생 증후군 만연</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>버퍼 통합</strong><span>50% 공격적 공기 산정 및 3대 버퍼(PB/FB/RB) 체계화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>3-Zone 통제</strong><span>Fever Chart 기반 황색 시 분석, 적색 시 자원 집중 투입</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>납기 준수</strong><span>파킨슨 법칙 타파 및 프로젝트 공기 25% 단축 달성</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 골드랫 박사의 **TOC(제약이론)**를 기반으로 자원 제약을 반영한 크리티컬 체인을 도출하고, 개별 안전마진을 회수하여 **프로젝트 버퍼(PB)**와 **피딩 버퍼(FB)**로 통합 통제하는 **일정 관리 기법**
- 목적: **파킨슨 법칙**과 **학생 증후군**으로 인한 낭비를 차단하고 전체 프로젝트 납기 준수율을 극대화

### 2. 구성체계 및 3대 버퍼

<div class="itpe-pipeline is-vertical" role="img" aria-label="CCPM 3대 버퍼 구조 요약">
  <div class="itpe-pipeline-node"><strong>50% 공격적 공기</strong><div class="itpe-step-detail"><span>작업자별 숨은 마진 회수 (릴레이 주자 원칙)</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>크리티컬 체인</strong><div class="itpe-step-detail"><span>선후행 관계 + 자원 제약 반영 최장 경로</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>3대 버퍼 배치</strong><div class="itpe-step-detail"><span>PB(체인 끝 납기보장) · FB(합류점 방어) · RB(자원 알림)</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>3-Zone 관리</strong><div class="itpe-step-detail"><span>Fever Chart: 녹색(정상) · 황색(분석) · 적색(개입)</span></div></div>
</div>

### 3. 핵심 통제

- **통합 버퍼 관리**: 분산된 여유시간을 회수하여 프로젝트 끝과 합류점에 배치
- **신호등 통제**: 버퍼 소진율이 황색/적색 구역 진입 시 즉각 자원 레벨링 및 병목 해소

## 출제 이력과 검증 출처

- 제119회, 제110회, 제102회 KPC 기출: CCPM의 개념, 3대 버퍼 및 버퍼 소진율 관리
- [Eliyahu M. Goldratt, Critical Chain](https://www.toc-goldratt.com)
- [Project Management Institute(PMI), A Guide to the Project Management Body of Knowledge (PMBOK Guide)](https://www.pmi.org)

## 학습 체크

- [ ] 파킨슨 법칙, 학생 증후군의 개념과 CCPM이 이를 해결하는 원리를 설명할 수 있는가?
- [ ] 크리티컬 체인의 3대 버퍼(PB, FB, RB)의 위치, 역할 및 산정 방식을 도식화할 수 있는가?
- [ ] 진척률 대비 버퍼 소진율을 활용한 3-Zone(Green/Yellow/Red) 관리 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [6시그마(Six Sigma) DMAIC](./111_six_sigma_dmaic.md)
- 연관 토픽: [CPM(Critical Path Method)](./081_cpm.md), [EVM(획득가치관리)](./032_evm.md)
- 다음 토픽: [소프트웨어 비용 산정(Software Cost Estimation)](./113_software_cost_estimation.md)
