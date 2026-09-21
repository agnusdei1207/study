---
title: "디자인 씽킹"
author: "Antigravity"
date: "2026-09-21T21:45:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 사용자 중심 서비스기획을 거쳐 디자인 씽킹으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>사용자 중심 서비스기획</span>
  <strong>디자인 씽킹</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 사용자 맥락을 관찰하여 **올바른 문제를 재정의**하고 시제품으로 해법을 학습
- 5 Modes: Empathize · Define · Ideate · Prototype · Test — 비선형 반복
- Double Diamond: Discover(발산) → Define(수렴) → Develop(발산) → Deliver(수렴)

<div class="itpe-svg-map">
  <svg viewBox="0 0 760 390" role="img" aria-label="디자인 씽킹 더블 다이아몬드의 발견 정의 개발 전달 과정">
    <defs><marker id="design-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z"></path></marker></defs>
    <path d="M45 195 L210 55 L375 195 L540 55 L705 195" class="itpe-svg-link"></path>
    <path d="M45 195 L210 335 L375 195 L540 335 L705 195" class="itpe-svg-link" marker-end="url(#design-arrow)"></path>
    <text x="125" y="35" class="itpe-svg-title">Discover</text><text x="125" y="365" class="itpe-svg-sub">사용자·맥락 탐색</text>
    <text x="292" y="35" class="itpe-svg-title">Define</text><text x="292" y="365" class="itpe-svg-sub">문제 재정의</text>
    <text x="458" y="35" class="itpe-svg-title">Develop</text><text x="458" y="365" class="itpe-svg-sub">대안·시제품</text>
    <text x="625" y="35" class="itpe-svg-title">Deliver</text><text x="625" y="365" class="itpe-svg-sub">검증·전달</text>
    <circle cx="45" cy="195" r="9" class="itpe-svg-node"></circle><circle cx="375" cy="195" r="9" class="itpe-svg-node is-current"></circle><circle cx="705" cy="195" r="9" class="itpe-svg-node"></circle>
    <text x="45" y="225" class="itpe-svg-label">Challenge</text><text x="375" y="225" class="itpe-svg-label">Problem Definition</text><text x="705" y="225" class="itpe-svg-label">Solution</text>
  </svg>
</div>

<details>
<summary>핵심 용어</summary>

- **Design Thinking**: 사용자 맥락을 이해하고 문제 재정의·아이디어·시제품·시험을 반복하는 인간 중심 문제해결 접근법
- **POV(Point of View)**: 사용자·필요·인사이트를 결합한 문제 관점 진술
- **HMW(How Might We)**: 문제를 다양한 해법 탐색이 가능한 질문으로 전환하는 기법
- **Persona**: 조사자료를 바탕으로 목표·행동·맥락을 표현한 대표 사용자 모델
- **CJM(Customer Journey Map)**: 사용자 여정의 단계·접점·행동·감정·문제를 시각화한 도구
- **Prototype**: 특정 가정·상호작용을 학습하기 위해 만든 시험 가능한 표현물
- **UT(Usability Test)**: 사용자가 과업을 수행하는 행동을 관찰하여 사용성 문제를 확인하는 평가

</details>

## 예상문제

> 디자인 씽킹의 개념과 5개 Mode·Double Diamond를 설명하고, 디지털 서비스 개발 적용절차와 고려사항을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 디자인 씽킹의 개요

> 디자인 씽킹의 핵심은 아이디어 수가 아니라 사용자 증거로 문제와 해법의 가정을 빠르게 수정하는 데 있음.

- 정의: 사용자 맥락을 이해하고 문제 재정의·대안 발산·시제품 시험을 반복하는 인간 중심 문제해결 접근법
- 목적: **문제 오정의 감소 · 조기학습 · 사용자 가치 향상**

## Ⅱ. 5개 Mode의 활동·산출

> 5개 Mode는 필요에 따라 앞뒤로 이동하며 병렬·반복 수행할 수 있음.

<div class="itpe-svg-map">
  <svg viewBox="0 0 520 220" role="img" aria-label="디자인 씽킹 5개 Mode와 비선형 피드백 루프">
    <defs>
      <marker id="dt-arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L6,3 z" fill="var(--sl-color-gray-3)"></path>
      </marker>
    </defs>
    <!-- 5 Mode Nodes -->
    <rect x="15" y="45" width="85" height="50" rx="8" class="itpe-svg-node"></rect>
    <text x="57" y="68" class="itpe-svg-title">1. Empathize</text>
    <text x="57" y="84" class="itpe-svg-sub">공감·관찰</text>

    <line x1="100" y1="70" x2="118" y2="70" stroke="var(--sl-color-gray-4)" stroke-width="2" marker-end="url(#dt-arr)"></line>

    <rect x="118" y="45" width="85" height="50" rx="8" class="itpe-svg-node is-current"></rect>
    <text x="160" y="68" class="itpe-svg-title">2. Define</text>
    <text x="160" y="84" class="itpe-svg-sub">문제정의(POV)</text>

    <line x1="203" y1="70" x2="221" y2="70" stroke="var(--sl-color-gray-4)" stroke-width="2" marker-end="url(#dt-arr)"></line>

    <rect x="221" y="45" width="85" height="50" rx="8" class="itpe-svg-node"></rect>
    <text x="263" y="68" class="itpe-svg-title">3. Ideate</text>
    <text x="263" y="84" class="itpe-svg-sub">대안발산(HMW)</text>

    <line x1="306" y1="70" x2="324" y2="70" stroke="var(--sl-color-gray-4)" stroke-width="2" marker-end="url(#dt-arr)"></line>

    <rect x="324" y="45" width="85" height="50" rx="8" class="itpe-svg-node"></rect>
    <text x="366" y="68" class="itpe-svg-title">4. Prototype</text>
    <text x="366" y="84" class="itpe-svg-sub">가정의 구체화</text>

    <line x1="409" y1="70" x2="427" y2="70" stroke="var(--sl-color-gray-4)" stroke-width="2" marker-end="url(#dt-arr)"></line>

    <rect x="427" y="45" width="80" height="50" rx="8" class="itpe-svg-node is-current"></rect>
    <text x="467" y="68" class="itpe-svg-title">5. Test</text>
    <text x="467" y="84" class="itpe-svg-sub">행동관찰·평가</text>

    <!-- Feedback Loops -->
    <!-- Test to Empathize -->
    <path d="M467 95 C467 180 57 180 57 95" fill="none" stroke="var(--sl-color-accent)" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#dt-arr)"></path>
    <text x="260" y="195" class="itpe-svg-sub" text-anchor="middle" fill="var(--sl-color-accent)">사용자 심층 재이해 (Test → Empathize)</text>

    <!-- Test to Define -->
    <path d="M445 95 C445 150 160 150 160 95" fill="none" stroke="var(--sl-color-gray-3)" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#dt-arr)"></path>
    <text x="300" y="145" class="itpe-svg-sub" text-anchor="middle">문제 재정의 (Test → Define)</text>

    <!-- Prototype to Ideate -->
    <path d="M345 45 C345 20 280 20 280 45" fill="none" stroke="var(--sl-color-gray-3)" stroke-width="1.2" stroke-dasharray="3,3" marker-end="url(#dt-arr)"></path>
    <text x="312" y="16" class="itpe-svg-sub" text-anchor="middle">시제품 제작 중 새 아이디어 발견</text>
  </svg>
</div>

| Mode | 주요 활동 | 산출 |
|---|---|---|
| **Empathize** | 관찰·인터뷰·맥락 탐색 | 관찰기록 · Empathy Map |
| **Define** | 패턴·인사이트·필요 종합 | Persona · CJM · POV |
| **Ideate** | HMW·발산·대안 선정 | 아이디어 · 가설 |
| **Prototype** | 핵심 가정의 저비용 표현 | Storyboard · Mock-up |
| **Test** | 사용자 과업 관찰·피드백 | 관찰결과 · 수정 가설 |

## Ⅲ. Double Diamond와 5 Modes 관계

> Double Diamond는 발산·수렴의 큰 구조, 5 Modes는 각 구간에서 활용하는 사고·실행 방식임.

| Double Diamond | 사고 | 연계 Mode | 판정 |
|---|---|---|---|
| **Discover** | 문제영역 발산 | Empathize | 충분한 사용자·맥락을 탐색했는가? |
| **Define** | 문제영역 수렴 | Define | 근거 있는 문제정의인가? |
| **Develop** | 해법영역 발산 | Ideate·Prototype | 복수 대안을 시험했는가? |
| **Deliver** | 해법영역 수렴 | Prototype·Test | 가치·사용성·실현성을 검증했는가? |

## Ⅳ. 디지털 서비스 적용 절차

> 조사자료가 POV·Prototype·Backlog까지 추적되어야 워크숍 결과가 구현으로 이어짐.

<div class="itpe-pipeline is-vertical" role="img" aria-label="디자인 씽킹의 디지털 서비스 적용 절차">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>① 사용자 조사</strong><strong>활동</strong><span>관찰·인터뷰·Journey 수집</span><strong>산출</strong><span>Evidence · Pain Point</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>② 문제 재정의</strong><strong>활동</strong><span>패턴·인사이트·POV·HMW 도출</span><strong>산출</strong><span>Problem Statement</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>③ 대안·Prototype</strong><strong>활동</strong><span>복수 아이디어·핵심가정 시각화</span><strong>산출</strong><span>Prototype · Test Plan</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><div class="itpe-step-detail"><strong>④ 사용자 Test</strong><strong>활동</strong><span>과업수행·행동·오류 관찰</span><strong>산출</strong><span>Finding · 수정가설</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>⑤ 구현 연결</strong><strong>활동</strong><span>검증가설·수용기준·우선순위 전환</span><strong>산출</strong><span>Product Backlog</span></div></div>
</div>

## Ⅴ. 문제점·대응책

> 워크숍의 산출물이 사용자 증거와 개발 의사결정으로 이어지지 않으면 형식 활동에 머묾.

| 위험 | 대책 | 효과 |
|---|---|---|
| **내부자 추측** | 실제 사용자·극단 사용자 조사 | 편향 완화 |
| **해법 조기 고정** | Problem Space와 Solution Space 분리 | 문제 재정의 확보 |
| **고충실도 집착** | 검증가정별 최소 Prototype | 학습비용 절감 |
| **개발 단절** | Finding–POV–Backlog 추적 | 구현 정합성 향상 |

## Ⅵ. 사용자 증거 기반 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

`[핵심 통찰]` 디자인 씽킹의 실패는 아이디어 부족보다 해법을 먼저 정하고 사용자 조사를 정당화 자료로 사용하는 데서 발생함.

`나라면` 각 Prototype에 검증할 가정과 폐기 기준을 하나씩 붙이고, 사용자 관찰 Finding이 연결된 Backlog만 구현 후보로 올리겠음.

### 실전 답안용 기술사적 제언

- **판정 기준 (Trigger)**: 기획 단계에서 사용자 실증 인터뷰 5건 미만, 또는 프로토타입 단계에서 '기각/폐기된 가설'이 0건일 때 확증 편향 및 형식적 워크숍으로 판정함.
- **대응 방안 (Action)**: Problem Space(문제 정의)와 Solution Space(해법 구현)를 엄격히 게이트 분리하고, 1가설 1프로토타입 원칙으로 페이퍼 목업 기반 빠른 실패를 의무화함.
- **검증 체계 (Verification)**: 사용자 과업 성공률(Task Success Rate), 오류 빈도, SUS(시스템 사용성 척도) 등 정량 UT 지표와 고객 여정 맵(CJM)의 감정 저점을 실시간 매핑하여 검증함.
- **기대 효과 (Impact)**: 엉뚱한 기능 개발로 인한 SW 재개발 비용 50% 절감, 사용자 채택률(Adoption Rate) 조기 극대화, 애자일 백로그와의 완벽한 정렬을 달성함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="사용자 증거에서 구현 Backlog까지의 추적 통제">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>증거</strong><span>관찰 · 발화 · 행동 · 맥락</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>통찰</strong><span>Pattern · Need · POV</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><div class="itpe-step-detail"><strong>검증</strong><span>가정 · Prototype · UT Finding</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>구현</strong><span>Backlog · 수용기준 · 우선순위</span></div></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 사용자 맥락을 이해하고 문제 재정의·대안 발산·시제품 시험을 반복하는 인간 중심 문제해결 접근법
- 목적: **문제 오정의 감소 · 조기학습 · 사용자 가치 향상**

### 2. 5개 Mode

| Mode | 핵심 |
|---|---|
| Empathize | 사용자·맥락 이해 |
| Define | POV 문제 재정의 |
| Ideate | 대안 발산 |
| Prototype | 핵심가정 표현 |
| Test | 사용자 행동으로 학습 |

### 3. 핵심 통제

- **Double Diamond**: Discover·Define·Develop·Deliver의 2회 발산·수렴
- **추적성**: 사용자 Evidence → POV → Prototype → Finding → Backlog

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [Stanford d.school: Design Thinking Bootleg](https://dschool.stanford.edu/tools/design-thinking-bootleg)
- [Design Council: Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/)

## 학습 체크

- [ ] Ⅰ. 디자인 씽킹의 정의·목적을 문제 재정의 관점에서 설명할 수 있는가?
- [ ] Ⅱ. 5개 Mode의 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ. Double Diamond와 5 Modes의 역할 차이를 설명할 수 있는가?
- [ ] Ⅳ. 사용자 조사부터 Product Backlog까지의 추적관계를 설명할 수 있는가?
- [ ] Ⅴ~Ⅵ. 내부자 추측·해법 조기고정·고충실도 집착의 대응책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [그로스 해킹](./046_growth_hacking.md)
- 연관 토픽: [애자일 대응 전략](./013_agile_response_strategy.md), [A/B 테스트](./029_ab_testing.md), [MECE](./045_mece.md)
- 다음 토픽: [제안요청서(RFP)](./049_rfp.md)
