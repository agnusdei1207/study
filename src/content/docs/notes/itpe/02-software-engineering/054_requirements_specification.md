---
title: "요구사항 명세(SRS·IEEE 830·명세 품질 특성)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
author: "Antigravity"
date: "2026-09-20T21:40:00+09:00"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 요구공학을 거쳐 요구사항 명세로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>요구공학 · 분석·설계</span>
  <strong>요구사항 명세</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **요구사항 명세(Requirements Specification)**는 시스템이 수행해야 할 기능적 요구사항과 준수해야 할 비기능적 품질속성을 이해관계자 간에 모호함 없이 공식 계약 문서(SRS)로 구체화하는 공학적 활동
- 메커니즘: **표준 템플릿(IEEE 830, ISO/IEC/IEEE 29148)** + **8대 우수 특성(정확성·명확성·완전성·일관성·순위화·검증가능성·수정가능성·추적성)** + **품질 시나리오 정량화**
- 산출/효과: 소프트웨어 요구사항 명세서(SRS) · 발주자-개발자 간 분쟁 차단 · BDD 기반 실행 가능한 명세(Living Documentation) 구축

<div class="itpe-flow-map" role="img" aria-label="요구사항 명세 프로세스 및 품질 체계">
  <div class="itpe-flow-node"><strong>도출·분석 요구</strong><span>비즈니스·사용자 니즈</span></div>
  <div class="itpe-flow-arrow">→ 표준 규격화 및 명세 →</div>
  <div class="itpe-flow-node is-current">
    <strong>명세서 (SRS) 표준 구조</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>표준 구조</strong><span><span class="itpe-keyword"><strong>서론 · 전반적 설명 · 세부 요구사항</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>8대 품질 특성</strong><span><span class="itpe-keyword"><strong>정·명·완·일·순·검·수·추</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>명세 기법</strong><span>자연어 vs 정형(Z/VDM) vs BDD(Gherkin)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 공식 기준선(Baseline) 확정 →</div>
  <div class="itpe-flow-node"><strong>아키텍처 및 검수</strong><span>추적성 기반 무결점 인도</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **SRS(Software Requirements Specification)**: 시스템이 수행해야 할 모든 기능적·비기능적 요구사항을 정의한 기술 계약 기준선 문서
- **IEEE 830**: 소프트웨어 요구사항 명세서의 전통적 권고 실천 지침 (서론, 전반적 설명, 세부 요구사항 3대 섹션)
- **ISO/IEC/IEEE 29148**: IEEE 830을 공식 대체하여 시스템 및 소프트웨어 생애주기 전반의 요구공학을 포괄하는 국제 표준
- **Verifiable(검증가능성)**: 유한하고 비용 효율적인 시험/검사를 통해 요구사항 충족 여부를 정량적으로 판정할 수 있는 특성
- **Living Documentation(살아있는 명세)**: 코드와 분리된 문서 대신 BDD(Given-When-Then) 테스트 코드를 통해 매 빌드마다 자동 검증되는 동기화된 명세 체계

</details>

## 예상문제

> 소프트웨어 개발의 기술적 계약 기준선이 되는 요구사항 명세서(SRS)의 표준 구조(IEEE 830 및 ISO/IEC/IEEE 29148)를 설명하고, 우수 명세서의 8대 품질 특성 및 모호한 명세로 인한 실무 분쟁 통제 방안을 제시하시오. (25점)

## Ⅰ. 기술적 계약 기준선(Baseline), 요구사항 명세의 개요

> 검증할 수 없는 문장은 요구사항이 아니며, 명세서의 모호함은 반드시 하류 공정의 재작업 비용 폭증으로 귀결된다.

- 정의: 이해관계자 간에 합의된 시스템의 기능, 비기능 품질속성, 제약조건을 표준화된 서식과 정밀한 표현으로 기술한 공식 기술 계약 문서
- 목적:
  - **소통의 단일 진실원천(SSOT)**: 발주자와 개발팀 간의 주관적 해석 차이 원천 배제
  - **검수 판정 기준 제공**: 정량적 인수 조건(Acceptance Criteria) 명문화를 통한 준공 분쟁 차단
  - **설계·테스트 기준선**: RTM 기반으로 아키텍처 설계와 테스트 케이스 도출의 근간 확립

## Ⅱ. 표준 명세서 구조: IEEE 830 및 ISO/IEC/IEEE 29148

> 명세서는 단순 기능 나열이 아니라, 시스템의 맥락과 외부 인터페이스를 아우르는 3대 섹션으로 구성된다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="SRS 표준 목차 3대 섹션">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. 서론 (Introduction)</strong></span>
    <span>시스템 목적, 프로젝트 범위, 용어 정의, 참조 규격 및 표준 명시</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. 전반적 설명 (Overall Description)</strong></span>
    <span>제품 조망, 주요 기능 개요, 사용자 특성 및 역량, 일반 제약조건, 가정 및 의존성</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. 세부 요구사항 (Specific Requirements)</strong></span>
    <span>• 기능적 요구사항 (입력, 처리 로직, 출력, 예외 처리)<br />• 외부 인터페이스 (사용자 UI, H/W, S/W, 통신 프로토콜)<br />• 비기능 품질속성 (성능 TPS/응답시간, 가용성, 보안 암호화, 유지보수성)</span>
  </div>
</div>

## Ⅲ. 우수 명세서의 8대 품질 특성 및 작성 기법 비교

> 우수한 SRS는 "정·명·완·일·순·검·수·추" 8가지 공학적 품질 특성을 엄격히 충족해야 한다.

### 1. 우수 SRS 8대 품질 특성 (IEEE 830)

| 품질 특성 | 공학적 의미 | 위반 안티패턴 |
|---|---|---|
| **정확성 (Correct)** | 실제 시스템이 충족해야 할 진정한 니즈와 100% 일치 | 잘못된 업무 산식을 기술하여 오작동 유발 |
| **명확성 (Unambiguous)** | 모든 문장이 단 하나의 의미로만 해석되어 다의성 배제 | "적절한 속도로 신속하게 처리한다" |
| **완전성 (Complete)** | 모든 기능, 제약, 예외 처리, 비기능 속성이 누락 없이 포함 | 정상 흐름만 적고 네트워크 타임아웃 예외 누락 |
| **일관성 (Consistent)** | 요구사항 상호 간에 충돌이나 모순이 존재하지 않음 | 앞쪽엔 50건 페이징, 뒤쪽엔 무한 스크롤 명세 |
| **순위화 (Ranked)** | 비즈니스 중요도 및 안정성 기준 우선순위 부여 | 모든 요구사항을 1순위로 지정하여 일정 조율 불가 |
| **검증가능성 (Verifiable)** | 비용 효율적인 시험/측정을 통해 충족 여부 판정 가능 | "사용하기 편리해야 한다" (정량 지표 부재) |
| **수정가능성 (Modifiable)** | 중복 서술 없이 목차와 구조가 체계화되어 변경 용이 | 동일 요구사항이 10군데 중복 산재 |
| **추적가능성 (Traceable)** | 요구사항 출처 및 후속 산출물(설계, 코드, 시험)과 1:1 매핑 | 요구사항 고유 ID가 없어 테스트 누락 |

### 2. 명세 작성 기법 3종 비교

| 비교 항목 | 비정형 명세 (자연어) | 정형 명세 (Formal Spec) | 실행 가능한 명세 (BDD) |
|---|---|---|---|
| **작성 도구** | MS-Word, Confluence 등 | Z, VDM, Petri-Net 등 수학 기호 | Gherkin (Given-When-Then) |
| **가독성/이해도** | 누구나 쉽게 읽음 (최상) | 전문가만 해독 가능 (최악) | 비즈니스 담당자·개발자 모두 공유 (우수) |
| **모호성** | **해석 차이 발생 위험 높음** | 완벽한 엄밀성 (모호성 제로) | 구체적 실행 예시로 모호성 극소화 |
| **검증 방식** | 수기 인스펙션 | 수학적 정리 증명 (Prover) | **CI 파이프라인 자동 테스트 검증** |

## Ⅳ. 명세 불명확 위험 및 실무 통제 대책

> 모호한 정성적 서술은 준공 검수 파행과 과업 분쟁을 초래하므로 정량적 시나리오로 통제해야 한다.

| 위험 | 대책 | 효과 |
|---|---|---|
| **모호한 성능 검수 분쟁** | **SEI 품질속성 시나리오 (자극-환경-반응-측정)** 수치 명세 | 주관적 해석 차단 및 객관적 검수 합격선 확보 |
| **변경 영향도 파악 불가** | 요구사항 고유 ID 기반 **요구사항 추적표(RTM)** 전산화 | 변경 영향 분석 시간 80% 단축 및 구현 누락 방지 |
| **사문화된 종이 문서** | **Cucumber/Playwright BDD** 연계 살아있는 명세(Living Doc) 도입 | 코드-명세 간 100% 실시간 동기화 보장 |

## Ⅴ. BDD 기반 Living Documentation 관점의 기술사적 제언

> 파일 서버에 잠자는 수백 쪽짜리 워드 문서는 죽은 문서이며, 코드로 실행되고 검증되는 살아있는 명세로 진화해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: SI 프로젝트에서 가장 빈번한 분쟁은 "원했던 것은 이런 화면이 아니었다" 또는 "이 정도 성능은 나와야 하는 것 아니냐"는 식의 명세 모호성에서 출발함. 자연어로 쓰인 요구사항은 읽는 사람의 경험과 이해관계에 따라 완전히 다르게 해석됨. 이를 해결하는 유일한 길은 '실행 가능한 명세(Specification by Example)'임. BDD의 Given-When-Then 문법으로 구체적 데이터 입출력 시나리오를 작성하면 기획자, 개발자, 테스터가 동일한 멘탈 모델을 공유할 수 있음.
- 나라면: 착수 단계에서 비기능 요구사항을 ISO 25010 기반으로 분류하고, 모든 성능 및 가용성 요구에 대해 SLA(응답시간 95th 백분위수, TPS, MTTR)를 명문화하며, 인수 조건(Acceptance Criteria)을 Jira-Git-BDD 테스트 코드로 100% 연동해 CI 빌드 통과를 준공 검수 증적으로 활용하겠음.

### 실전 답안용 기술사적 제언

- 판정: 자연어 명세의 모호성 극복 및 실행 가능한 명세 거버넌스 확립
- 대안: **SEI 품질속성 시나리오 정량화 + BDD(Living Documentation) 파이프라인**
- 검증: Given-When-Then 시나리오 자동 테스트 통과율 100% 및 RTM 전수 검증
- 효과: 검수 분쟁 제로화 · 명세-코드 간 불일치 원천 해소

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 명세 현대화 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>자연어 명세의 모호성으로 인한 준공 분쟁 및 문서 사문화 발생</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>정량적 품질속성 시나리오 수립 및 BDD 기반 Living Documentation 전환</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>CI 연동 인수 테스트 100% 통과 및 요구사항-테스트 간 RTM 양방향 추적</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>발주자-개발자 간 완벽한 신뢰 구축 및 납기 내 무장애 인도 달성</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **요구사항 명세(SRS)**는 시스템이 수행해야 할 기능 및 제약조건을 표준화된 규격으로 작성한 기술 계약 기준선
- 목적: 모호성 제거, 단일 진실원천(SSOT) 확보, 객관적 인수 검수 기준 수립

### 2. 우수 SRS 8대 품질 특성

<div class="itpe-pipeline is-vertical" role="img" aria-label="8대 특성 요약">
  <div class="itpe-pipeline-node"><strong>내용적 무결성</strong><span>정확성(Correct) · 명확성(Unambiguous) · 완전성(Complete) · 일관성(Consistent)</span></div>
  <div class="itpe-pipeline-arrow">↕ 관리 및 검증 통제</div>
  <div class="itpe-pipeline-node"><strong>공학적 관리성</strong><span>순위화(Ranked) · 검증가능성(Verifiable) · 수정가능성(Modifiable) · 추적가능성(Traceable)</span></div>
</div>

### 3. 핵심 통제

- **검증가능성(Verifiable)**: 모든 정성적 표현을 정량 지표(TPS, 응답시간)로 수치화
- **RTM 추적성**: 요구사항 ID를 설계-코드-시험과 1:1 매핑하여 누락 차단

## 출제 이력과 검증 출처

- 제130회 정보관리기술사 1교시: 요구사항명세서(SRS)에 기술되어야 하는 항목
- IEEE Std 830-1998, Recommended Practice for Software Requirements Specifications
- ISO/IEC/IEEE 29148:2018 Systems and software engineering - Life cycle processes - Requirements engineering

## 학습 체크

- [ ] IEEE 830 표준 명세서의 3대 섹션(서론, 전반적 설명, 세부 요구사항)을 제시할 수 있는가?
- [ ] 우수한 요구사항 명세서의 8대 품질 특성(정·명·완·일·순·검·수·추)을 설명할 수 있는가?
- [ ] 비정형 명세(자연어)와 실행 가능한 명세(BDD)의 차이점 및 장단점을 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [선형 구조](./053_linear_structure.md)
- 연관 토픽: [요구공학](./040_requirements_engineering.md), [요구사항 도출](./041_requirements_elicitation.md), [요구사항 추적표(RTM)](./102_requirement_traceability_matrix.md)
- 다음 토픽: [TA vs AA](./055_ta_vs_aa.md)
