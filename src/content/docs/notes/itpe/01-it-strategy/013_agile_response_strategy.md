---
title: "애자일 대응 전략"
author: "Codex"
date: "2026-09-20T19:12:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 개발 전략·방법론을 거쳐 애자일 대응 전략으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>개발 전략·방법론</span>
  <strong>애자일 대응 전략</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 급변하는 불확실한 비즈니스 환경에서 요구사항 변경을 수용하고 가치 중심의 반복 개발을 수행하는 전략
- 메커니즘: 전통 코어의 안정성(Mode 1)과 디지털 혁신의 속도(Mode 2)를 결합한 **Bimodal IT** 및 **SAFe** 전사 확장
- 산출: 타임투마켓(Time-to-Market) 단축, 고객 피드백 즉시 환류, 스프린트 단위 **잠재 배포 가능 제품(Increment)** 인도

<div class="itpe-flow-map" role="img" aria-label="엔터프라이즈 바이모달 IT 애자일 대응 체계">
  <div class="itpe-flow-node">
    <strong>비즈니스 환경 변화 및 불확실성</strong>
    <small>요구사항 잦은 변경 · 빠른 시장 출시 압박</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>바이모달 IT (Bimodal IT) 운영 체계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Mode 1 (안정)</strong><span>코어 기간계 · 폭포수(Waterfall) · 엄격한 통제 및 데이터 무결성</span></div>
      <div class="itpe-flow-branch"><strong>Mode 2 (민첩)</strong><span>대고객 디지털 앱 · 애자일(Scrum/Kanban) · 2주 단위 배포 및 혁신</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>엔터프라이즈 애자일 (SAFe / Agile PMO)</strong>
    <small>스프린트 단위 가치 검수 · DoD 준수 · 자기조직화 팀 확립</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Agile(애자일)**: 사전 계획 준수보다 작동하는 소프트웨어와 고객 협력, 변화 대응을 중시하는 개발 철학
- **Bimodal IT(바이모달 IT)**: 예측 가능성과 안정성의 Mode 1과 신속성과 혁신의 Mode 2를 공존시키는 전략
- **Mode 1**: 코어 ERP, 계정계 등 무장애와 데이터 정합성을 최우선으로 하는 전통적 폭포수 방식
- **Mode 2**: 모바일 채널, 대고객 앱 등 빠른 출시와 고객 피드백이 핵심인 애자일 반복 개발 방식
- **Sprint(스프린트)**: 작동 가능한 소프트웨어를 만들기 위해 설정하는 통상 1~4주의 짧은 개발 반복 주기
- **Backlog(백로그)**: 제품에 구현해야 할 모든 요구사항과 기능을 비즈니스 가치 순으로 정렬한 목록
- **Increment(제품 증분)**: 스프린트 동안 완성되어 즉시 배포 가능한 상태에 도달한 작동 소프트웨어 결과물
- **DoD(Definition of Done, 완료 정의)**: 단위 테스트 통과, 코드 리뷰 완료 등 증분이 갖춰야 할 엄격한 품질 완료 기준
- **SAFe(Scaled Agile Framework)**: 대규모 엔터프라이즈 조직에서 다수의 스크럼 팀 간 의존성을 조율하는 확장 프레임워크
- **Burndown Chart**: 남은 작업량 대비 경과 시간을 시각화하여 스프린트 목표 달성 여부를 조기 판단하는 차트

</details>

## 예상문제

> 엔터프라이즈 애자일(Agile) 전환의 개념과 필요성을 설명하고, 가트너의 바이모달 IT(Bimodal IT) 기반 도입 전략, 폭포수 모델과의 비교 및 공공·대규모 금융 조직의 계약·거버넌스 대응 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **바이모달 IT (Bimodal IT)** | 안정 중심의 Mode 1(폭포수)과 속도 중심의 Mode 2(애자일) 공존 전략 | Ⅲ 절 |
| **대규모 애자일 (SAFe)** | Scaled Agile Framework, 전사 다수 스크럼 팀 간 의존성 조율 | Ⅲ 절, Ⅵ 절 |
| **애자일 계약 테일러링** | 고정가 턴키 계약 탈피, 스프린트 단위 가치 검수 계약 모델 | Ⅴ 절, Ⅵ 절 |

## Ⅰ. 불확실성 시대의 생존 전략, 애자일 대응의 개요

> 애자일 대응 전략은 변경을 통제 대상이 아닌 가치 창출의 기회로 수용하며, 성패는 문서 분량이 아닌 **작동하는 소프트웨어의 지속적 인도**로 판정함.

- 정의: 사전에 모든 요구사항을 확정할 수 없다는 전제하에, 짧은 주기(Sprint)의 반복과 점진적 개발을 통해 고객 피드백을 신속히 반영하는 **민첩한 프로젝트 및 조직 운영 전략**
- 목적: 시장 출시 속도 단축, 불확실성 조기 제거 및 비즈니스 적응력 확보

## Ⅱ. 애자일 스프린트 구성체계 및 4단계 반복 이행 방법론

> 각 스프린트는 백로그 우선순위화에서 출발하여 일일 동기화와 시연을 거치며, 완료 정의(DoD)를 통과한 제품 증분만을 다음 주기로 인도함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="애자일 4단계 스프린트 반복 이행 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 비전 수립 및 백로그 정제 (Backlog Refinement)</strong></span>
    <small>사용자 스토리 도출 · 비즈니스 가치 평가 · 스토리 포인트 산정<br />→ 프로덕트 백로그(Product Backlog)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 스프린트 계획 및 확정 (Sprint Planning)</strong></span>
    <small>팀 속도(Velocity) 기반 범위 확정 · 작업(Task) 분해<br />→ 스프린트 백로그(Sprint Backlog) · 번다운 차트</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 스프린트 실행 및 일일 점검 (Daily Scrum)</strong></span>
    <small>15분 스탠드업 · 장애 요인(Impediment) 제거 · 지속적 통합(CI)<br />→ 칸반 보드 갱신 · 일일 빌드 결과</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 스프린트 리뷰 및 회고 (Review & Retrospective)</strong></span>
    <small>이해관계자 데모 시연 · 피드백 수렴 · 프로세스 개선 도출<br />→ 배포 가능 제품 증분(Increment) · 회고 개선 과제</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>DoD(Definition of Done)</strong></span> · 사용자 스토리 ↔ 단위/통합 테스트 자동화 ↔ 잠재 배포 가능 제품 검증</div>

## Ⅲ. 엔터프라이즈 바이모달(Bimodal) IT 구조 및 SAFe 체계

> 핵심 코어의 무장애와 대고객 혁신의 민첩성을 동시에 달성하기 위해 2개 모드를 API 계층으로 연계함.

| 구분 | Mode 1 (안정 중심 IT) | Mode 2 (민첩 중심 IT) | 연계 및 확장 (Enterprise) |
|---|---|---|---|
| **핵심 목표** | 예측 가능성, 무장애 가동, 데이터 무결성 | 타임투마켓, 혁신, 고객 경험(CX) | 2개 모드 간 느슨한 결합(Loose Coupling) |
| **적용 대상** | 코어 ERP, 계정계, 공공 대규모 행정망 | 대고객 모바일 채널, 마이데이터, AI 챗봇 | 표준 REST API / 이벤트 브로커 연계 |
| **개발 방법론** | 전통적 폭포수(Waterfall) 모델 | 스크럼(Scrum), 칸반(Kanban) | **SAFe(Scaled Agile Framework)** 거버넌스 |
| **배포 주기** | 반기/연간 단위 대규모 일괄 배포 | 1~2주 스프린트 단위 빈번한 배포 | 릴리즈 트레인(Agile Release Train) 조율 |
| **조직 구조** | 기능 중심 수직 계층 조직 | 교차 기능(Cross-functional) 전담팀 | 전사 Agile CoE 및 PMO의 지원 |

## Ⅳ. 폭포수(Waterfall) vs 애자일(Agile) 비교

> 폭포수가 범위 고정-일정/비용 변동 모델이라면, 애자일은 일정/비용 고정-범위 유연 모델임.

| 비교 항목 | 전통적 폭포수 (Waterfall) | 애자일 (Agile) |
|---|---|---|
| **접근 방식** | 선형 순차적 (Linear Sequential) | 반복·점진적 (Iterative & Incremental) |
| **요구사항 관리** | 초기 분석 단계에서 전수 확정 및 동결 | 백로그(Backlog) 기반 동적 우선순위 재조정 |
| **가치 전달 시점** | 프로젝트 최종 종료 시점 일괄 전달 | 매 스프린트 종료 시 동작하는 증분(Increment) 전달 |
| **품질 검증** | 후반부 통합 테스트 단계에서 집중 검증 | 스프린트마다 지속적 통합·테스트(CI/CD) 자동화 |
| **변화 비용** | 단계 후반으로 갈수록 기하급수적 증가 | 짧은 피드백 주기를 통해 변경 비용 한도 통제 |

## Ⅴ. 실무 위험 분석 및 통제 대책

> 고정가 계약 충돌과 품질 부채 누적을 차단하기 위해 계약 테일러링과 완료 정의(DoD)를 강제해야 함.

| 위험 | 원인 | 통제 | 검증 |
|---|---|---|---|
| **고정가 턴키 계약 충돌** | 사전 요구사항 확정을 전제로 하는 국가계약법 및 확정가 발주 관행 | 총액 계약 내에서 백로그 우선순위 조정을 허용하는 '애자일 표준계약 템플릿' 적용 | 과업 변경 심의 분쟁 0건 |
| **관리자의 통제 상실감** | WBS 기반 진척률 보고에 익숙한 전통적 경영진의 진척 불신 | 번다운 차트(Burndown Chart) 및 정례 데모 시연회(Sprint Review) 운영 | 스프린트 데모 합격률 100% |
| **품질 부채 (Technical Debt)** | 빠른 기능 출시에 매몰되어 리팩토링 및 자동화 테스트 누락 | 스프린트 완료 정의(DoD)에 단위 테스트 커버리지 및 정적 분석 필수화 | 코드 커버리지 기준 준수 및 결함 조기 격리 |

## Ⅵ. 비즈니스 민첩성 중심의 기술사적 제언

> 애자일의 본질은 스탠드업 미팅을 여는 형식적 모방(Fake Agile)이 아니라 경영진과 현업, 개발팀이 실패를 용인하고 피드백을 공유하는 거버넌스 개혁에 있음.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 엔터프라이즈 조직에서 애자일 전환이 실패하는 가장 큰 이유는 개발팀만 스크럼을 돌리고 상위 의사결정권자는 여전히 1년짜리 고정 WBS와 산출물 문서를 요구하는 '거버넌스 불일치'에 있음.
- 나라면: 전면 전환의 충격을 피하기 위해 코어 시스템은 폭포수, 고객 접점은 스크럼을 적용하는 바이모달 IT 구조로 착수하고, 공공·금융 계약 환경에 맞춰 스프린트 단위 완료 정의(DoD) 기반 기성 검수 방식을 정립하겠음.

### 실전 답안용 기술사적 제언

- 판정: 부분적 개발 방법론 변경을 넘어 전사 거버넌스 및 계약 체계 개혁
- 대안: **바이모달 IT 아키텍처** 및 **DoD 기반 애자일 용역 계약 테일러링**
- 검증: 스프린트별 동작 가능한 증분 검수율 100% · 테스트 자동화 파이프라인 통과
- 효과: 시장 요구 대응 리드타임 단축 및 과업 변경 분쟁 원천 차단

<div class="itpe-pipeline is-vertical" role="img" aria-label="엔터프라이즈 애자일 거버넌스 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>고정가 턴키 계약 관행 · WBS 산출물 중심 감사 · Fake Agile 양산</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>바이모달 IT(Mode 1/2) 분리 + DoD 기반 스프린트 기성 검수 계약</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>사용자 스토리별 DoD 충족 여부 · CI/CD 테스트 자동화 통과율</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>고객 피드백 즉시 반영 · 과업 변경 분쟁 예방 · 출시 리드타임 단축</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **애자일(Agile)** 대응 전략은 요구사항 변경을 수용하고 짧은 반복 주기를 통해 작동하는 소프트웨어를 지속 인도하는 **민첩한 경영·개발 전략**
- 목적: 시장 출시 속도 단축, 불확실성 조기 제거 및 비즈니스 적응력 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="애자일 스프린트 4단계 요약">
  <div class="itpe-pipeline-node"><strong>백로그 정제</strong><small>스토리 도출 · 우선순위화</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>스프린트 계획</strong><small>스프린트 백로그 확정</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>스프린트 실행</strong><small>일일 스크럼 · CI/CD 연계</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>리뷰 및 회고</strong><small>DoD 검수 · 증분(Increment) 인도</small></div>
</div>

### 3. 핵심 통제

- **바이모달 IT(Bimodal IT)**: 코어 기간계의 안정성(Mode 1)과 디지털 채널의 민첩성(Mode 2)의 이원화 공존
- DoD(Definition of Done): 테스트 자동화 및 코드 품질 기준을 만족한 작동 소프트웨어만 배포 허용

## 출제 이력과 검증 출처

- 제131회 정보관리기술사 1교시: 애자일 방법론의 핵심 가치 및 스프린트 운영
- 제129회 정보관리기술사 2교시: 엔터프라이즈 환경에서의 바이모달 IT 및 애자일 전환 전략
- [Agile Alliance: Manifesto for Agile Software Development](https://agilemanifesto.org/)
- [Gartner Research: Bimodal IT Framework](https://www.gartner.com)

## 학습 체크

- [ ] 애자일 선언문의 4대 핵심 가치와 12대 실행 원칙을 설명할 수 있는가?
- [ ] 바이모달 IT(Mode 1 vs Mode 2)의 특성과 업무 적용 기준을 비교할 수 있는가?
- [ ] 폭포수 모델과 애자일 모델의 범위, 일정, 비용 역삼각형 구조를 도식화할 수 있는가?

## 연결 토픽

- 이전 토픽: [FinOps](./012_finops.md)
- 연관 토픽: [WBS](./007_wbs.md), [PMO](./004_pmo.md)
- 다음 토픽: [IT 투자평가·투자관리](./016_it_investment_evaluation.md)
