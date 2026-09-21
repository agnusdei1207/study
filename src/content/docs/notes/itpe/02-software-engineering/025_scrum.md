---
title: "스크럼(Scrum)"
tags:
  - "notes-software-engineering"
author: "Antigravity"
date: "2026-09-20T23:53:43+09:00"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 개발 방법론을 거쳐 스크럼으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>개발 방법론</span>
  <strong>스크럼(Scrum)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **스크럼(Scrum)**은 불확실성이 높은 프로젝트 환경에서 1~4주의 짧은 반복 주기인 **스프린트(Sprint)**를 통해 동작 가능한 소프트웨어를 점진적으로 출시하는 경험주의 기반 애자일 프레임워크
- 메커니즘: **3대 역할(PO, SM, Dev)** + **5대 이벤트(Sprint, Planning, Daily, Review, Retro)** + **3대 산출물(PB, SB, Increment)**
- 산출/효과: 고객 피드백 조기 수용 · 개발 리스크 분산 · 비즈니스 가치 전달 속도(Time-to-Market) 극대화

<div class="itpe-flow-map" role="img" aria-label="스크럼 프레임워크 동작 프로세스">
  <div class="itpe-flow-node"><strong>제품 백로그</strong><span>우선순위화된 요구사항 (PO 소유)</span></div>
  <div class="itpe-flow-arrow">→ 스프린트 계획 →</div>
  <div class="itpe-flow-node is-current">
    <strong>스프린트 (1~4주)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>일일 스크럼</strong><span>15분 기립 미팅 · 장애 제거</span></div>
      <div class="itpe-flow-branch"><strong>개발 활동</strong><span><span class="itpe-keyword"><strong>스프린트 백로그 구현</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>투명성·점검·적응</strong><span>경험주의 3대 기둥 실천</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 리뷰 &amp; 회고 →</div>
  <div class="itpe-flow-node"><strong>잠재적 출시 가능 제품 증분</strong><span>완료의 정의(DoD) 충족 산출물</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Scrum**: 복잡한 적응형 문제를 해결하며 최상의 가치를 창출하도록 돕는 가벼운 애자일 프레임워크
- **Product Owner (PO)**: 제품의 가치를 극대화하고 제품 백로그의 우선순위를 결정하는 최종 의사결정자
- **Scrum Master (SM)**: 스크럼 원칙을 전파하고 개발팀의 장애(Impediment)를 제거하는 서번트 리더
- **Sprint(스프린트)**: 동작 가능한 제품 증분을 만들기 위한 1개월 이하의 고정된 기간(Time-box)
- **DoD(Definition of Done, 완료의 정의)**: 증분이 제품으로서 요구되는 품질 기준을 충족했음을 보증하는 공식 체크리스트

</details>

## 예상문제

> 애자일 개발 방법론의 대표적인 프레임워크인 스크럼(Scrum)의 3대 경험주의 기둥(투명성, 점검, 적응)을 설명하고, 3대 역할, 5대 이벤트, 3대 산출물의 상호 작용 구조 및 성공적인 스크럼 정착을 위한 완료의 정의(DoD)의 역할을 제시하시오. (25점)

## Ⅰ. 불확실성을 극복하는 경험적 프로세스, 스크럼의 개요

> 스크럼은 미래를 예측하여 완벽한 계획을 세우는 것이 아니라, 잦은 점검과 적응을 통해 올바른 제품을 찾아가는 프레임워크다.

- 정의: 복잡한 적응형 문제(Complex Adaptive Problems)를 해결하면서 높은 비즈니스 가치를 전달하기 위한 **경험주의(Empiricism)** 기반 애자일 프레임워크
- 목적: 변화하는 고객 요구에 민첩 대응, 릴리스 주기 단축, 팀 자율성과 협업 문화 증진, 프로젝트 가시성 확보

## Ⅱ. 스크럼의 3-5-3 체계 구조

> 스크럼은 3가지 역할(Role), 5가지 이벤트(Event), 3가지 산출물(Artifact)의 유기적 결합으로 완성된다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="스크럼 3-5-3 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3대 역할 (Accountabilities)</strong></span>
    <span>1. Product Owner (가치 극대화, 백로그 소유)<br />2. Scrum Master (프로세스 촉진, 장애 제거, 서번트 리더십)<br />3. Developers (동작 가능한 제품 증분 개발 전문가)</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ 산출물 생성 및 관리</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3대 산출물 (Artifacts)</strong></span>
    <span>1. Product Backlog (제품 목표 약속)<br />2. Sprint Backlog (스프린트 목표 약속)<br />3. Increment (완료의 정의 DoD 약속)</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ 이벤트 수행 주기</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>5대 이벤트 (Events)</strong></span>
    <span>1. The Sprint (모든 이벤트의 컨테이너)<br />2. Sprint Planning (스프린트 계획)<br />3. Daily Scrum (일일 15분 점검)<br />4. Sprint Review (이해관계자 검토/피드백)<br />5. Sprint Retrospective (팀 프로세스 개선 회고)</span>
  </div>
</div>

### 스크럼(Scrum) 생명주기 및 3-5-3 프로세스 루프

<div class="itpe-svg-wrapper">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" class="itpe-svg">
    <!-- Background -->
    <rect width="520" height="220" fill="var(--sl-color-bg-subtle, #f8fafc)" rx="8" />
    
    <!-- Title -->
    <text x="20" y="24" class="itpe-svg-label" fill="var(--sl-color-text-accent, #2563eb)">[Scrum 3대 산출물 및 스프린트(1~4주) 실행 사이클]</text>

    <!-- 1. Product Backlog -->
    <rect x="18" y="48" width="88" height="150" rx="5" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    <text x="62" y="70" class="itpe-svg-title" font-size="11.5" font-weight="700" fill="var(--sl-color-text, #1e293b)" text-anchor="middle">제품 백로그</text>
    <text x="62" y="86" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">Product Backlog</text>
    <line x1="26" y1="96" x2="98" y2="96" stroke="var(--sl-color-border, #e2e8f0)" />
    <text x="62" y="115" class="itpe-svg-sub" font-size="9.5" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">PO가 우선순위화</text>
    <text x="62" y="132" class="itpe-svg-sub" font-size="9.5" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">요구사항 목록</text>
    <rect x="25" y="150" width="74" height="22" rx="3" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="62" y="165" class="itpe-svg-label" font-size="9" fill="var(--sl-color-text, #334155)" text-anchor="middle">제품 목표</text>

    <!-- Arrow to Sprint Planning -->
    <line x1="106" y1="120" x2="122" y2="120" stroke="var(--sl-color-text-muted, #94a3b8)" stroke-width="1.5" marker-end="url(#arrow)" />

    <!-- 2. Sprint Planning -->
    <rect x="122" y="75" width="78" height="90" rx="5" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1.2" />
    <text x="161" y="98" class="itpe-svg-title" font-size="11" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">스프린트 계획</text>
    <text x="161" y="115" class="itpe-svg-sub" font-size="9.5" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">Planning</text>
    <line x1="130" y1="125" x2="192" y2="125" stroke="var(--sl-color-border, #e2e8f0)" />
    <text x="161" y="142" class="itpe-svg-sub" font-size="9" fill="var(--sl-color-text, #334155)" text-anchor="middle">목표 합의</text>
    <text x="161" y="155" class="itpe-svg-sub" font-size="9" fill="var(--sl-color-text, #334155)" text-anchor="middle">태스크 분해</text>

    <!-- Arrow to Sprint Loop -->
    <line x1="200" y1="120" x2="216" y2="120" stroke="var(--sl-color-text-muted, #94a3b8)" stroke-width="1.5" marker-end="url(#arrow)" />

    <!-- 3. Sprint Execution Loop (Middle) -->
    <rect x="216" y="48" width="165" height="150" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-accent, #8b5cf6)" stroke-width="1.5" />
    <text x="298" y="68" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-accent, #8b5cf6)" text-anchor="middle">스프린트 (1~4주 Timebox)</text>
    
    <!-- Daily Scrum mini loop -->
    <circle cx="298" cy="115" r="32" fill="none" stroke="var(--sl-color-accent, #8b5cf6)" stroke-width="1.5" stroke-dasharray="5 3" />
    <text x="298" y="112" class="itpe-svg-title" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #8b5cf6)" text-anchor="middle">일일 스크럼</text>
    <text x="298" y="126" class="itpe-svg-sub" font-size="9" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">15분 (Daily)</text>
    
    <!-- Sprint Backlog tag -->
    <rect x="226" y="162" width="145" height="26" rx="4" fill="var(--sl-color-bg-accent, #eff6ff)" />
    <text x="298" y="179" class="itpe-svg-label" font-size="9.5" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">스프린트 백로그 (Goal 보증)</text>

    <!-- Arrow to Review/Retro -->
    <line x1="381" y1="120" x2="397" y2="120" stroke="var(--sl-color-text-muted, #94a3b8)" stroke-width="1.5" marker-end="url(#arrow)" />

    <!-- 4. Review & Retro -->
    <rect x="397" y="52" width="105" height="68" rx="5" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    <text x="449" y="70" class="itpe-svg-title" font-size="10.5" font-weight="700" fill="var(--sl-color-text, #1e293b)" text-anchor="middle">스프린트 리뷰</text>
    <text x="449" y="85" class="itpe-svg-sub" font-size="9" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">데모 및 고객 피드백</text>
    <line x1="405" y1="92" x2="493" y2="92" stroke="var(--sl-color-border, #e2e8f0)" />
    <text x="449" y="107" class="itpe-svg-title" font-size="10" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">스프린트 회고</text>

    <!-- 5. Potentially Releasable Increment -->
    <rect x="397" y="130" width="105" height="68" rx="5" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-success, #10b981)" stroke-width="1.5" />
    <text x="449" y="152" class="itpe-svg-title" font-size="11" font-weight="700" fill="var(--sl-color-success, #10b981)" text-anchor="middle">제품 증분</text>
    <text x="449" y="168" class="itpe-svg-sub" font-size="9.5" fill="var(--sl-color-text, #334155)" text-anchor="middle">Increment (출시가능)</text>
    <rect x="407" y="174" width="85" height="18" rx="3" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="449" y="186" class="itpe-svg-label" font-size="9" font-weight="700" fill="var(--sl-color-success, #10b981)" text-anchor="middle">DoD(완료정의) 통과</text>
  </svg>
</div>

| 산출물 | 내포된 약속 (Commitment) | 핵심 통제 내용 |
|---|---|---|
| **제품 백로그 (Product Backlog)** | **제품 목표 (Product Goal)** | 제품의 미래 상태를 정의하며, PO가 가치 기반 우선순위 정렬 |
| **스프린트 백로그 (Sprint Backlog)** | **스프린트 목표 (Sprint Goal)** | 이번 스프린트에서 완수할 단일 비즈니스 목적 및 개발 태스크 |
| **제품 증분 (Increment)** | **완료의 정의 (Definition of Done)** | 릴리스 가능한 품질 수준을 완벽히 만족한 소프트웨어 실체 |

## Ⅲ. 전통적 폭포수 모델 vs 스크럼 프레임워크 비교

> 두 방법론은 요구사항 고정과 일정 관리의 접근 방식에서 근본적인 차이를 보인다.

| 비교 항목 | 전통적 폭포수 모델 (Waterfall) | 스크럼 프레임워크 (Scrum) |
|---|---|---|
| **기반 철학** | 계획 주도형 (Predictive, 통제 중심) | **경험주의 (Empirical, 점검·적응)** |
| **삼각 제약 (Iron Triangle)** | **요구사항(범위) 고정**, 일정/비용 변동 | **일정(Timebox)/비용 고정**, 범위(Scope) 변동 |
| **가치 인도 시점** | 프로젝트 최종 종료 시점 (빅뱅) | **매 스프린트 종료 시점 (점진적 출시)** |
| **고객 참여** | 요구분석 및 최종 인수 시점에 국한 | **매 스프린트 리뷰마다 지속적 참여 및 피드백** |
| **리스크 노출** | 후반부 통합 및 테스트 시 폭증 | **초기부터 조기 분산 및 완화** |

## Ⅳ. 스크럼 운영 문제점·대응책

> 스크럼이 단순한 '날림 개발'로 전락하지 않기 위한 가장 강력한 공학적 안전장치가 DoD이다.

### 1. 백로그 정제와 완료의 정의(DoD)

<div class="itpe-pipeline is-vertical" role="img" aria-label="백로그 정제와 완료의 정의">
  <div class="itpe-pipeline-node">
    <strong>제품 백로그 정제</strong>
    <span>제품 백로그 항목을 더 작고 명확하게 분해 · 설명·순서·크기 지속 보완</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ 스프린트 개발 수행</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>DoD (Definition of Done: 완료의 정의)</strong></span>
    <span>조직이 제품 증분에 요구하는 품질 상태를 공식 정의 · 충족한 작업만 증분에 포함</span>
  </div>
</div>

### 2. 스크럼 프로젝트 실무 위험 및 대응 통제

| 위험 | 대책 | 효과 |
|---|---|---|
| 형식적 일일 미팅(좀비 스크럼) 및 몰입 저하 | 스프린트 목표(Sprint Goal) 중심 15분 타임박스 운영 및 장애 제거 집중 | 팀 주도성 및 비즈니스 가치 몰입도 향상 |
| 불명확한 품질 기준으로 결함 누적 | DoD(코드리뷰, 단위/통합테스트, 정적분석) 체크리스트 엄격 적용 | 잠재적 출시 가능한 고품질 제품 증분 확보 |
| 스프린트 도중 무분별한 과업 추가 및 변경 | 스프린트 타임박스 보호 규칙 적용 및 차기 스프린트 백로그 이관 | 개발팀 개발 집중도 유지 및 일정 예측 가능성 확보 |

## Ⅴ. 경험주의 정착 중심의 결론

> 단일 스크럼을 넘어 다수 팀이 참여하는 엔터프라이즈 환경에서는 스케일드 애자일(SAFe, LeSS) 거버넌스가 필요하다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 스크럼을 도입하고도 실패하는 조직의 공통점은 "형식만 흉내 내는 좀비 스크럼(Zombie Scrum)"임. 매일 모여 15분 동안 어제 한 일, 오늘 할 일을 기계적으로 읊기만 할 뿐 스프린트 목표(Sprint Goal)에 대한 주도적 몰입이 없음. 스크럼 마스터는 단순 진행자가 아니라 조직의 구조적 장애를 타파하는 변화 관리자여야 함.
- 나라면: 스프린트 기간 동안에는 PO조차도 스프린트 백로그를 함부로 변경할 수 없도록 '스프린트 타임박스 보호 규칙'을 엄격히 적용하여 개발팀의 몰입도를 보호하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 프로젝트 요구사항 변동성 및 시장 출시 속도(Time-to-Market) 긴급도에 따른 스크럼 프레임워크 채택 판정
- **대응 방안**: **완료의 정의(DoD)** 체크리스트(코드리뷰, 단위테스트, 정적분석) 엄격화 및 스프린트 타임박스 보호 규칙 강제
- **검증 체계**: 스프린트 번다운 차트(Burn-down Chart) 및 속도(Velocity) 안정성 모니터링, 매 스프린트 동작하는 증분 검증
- **기대 효과**: 형식적 좀비 스크럼 탈피, 고객 피드백 반영 리드타임 50% 단축 및 지속가능한 고품질 소프트웨어 적시 출시 달성

<div class="itpe-pipeline is-vertical" role="img" aria-label="스크럼 조직 성숙도 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>형식적 스크럼 미팅 · DoD 부재로 인한 품질 결함 누적</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>엄격한 DoD 확립 및 서번트 리더십 기반 장애 제거 체계화</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>스프린트 목표 달성률 90% 이상 및 증분 릴리스 가능성 검증</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>팀 자율성 극대화 · 지속가능한 고품질 증분 전달 체계 완성</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **스크럼(Scrum)**은 1~4주의 스프린트를 통해 잠재적으로 출시 가능한 제품 증분을 점진적으로 완성하는 경험주의 애자일 프레임워크
- 목적: 변화하는 시장 요구에 민첩 대응하고 지속적인 비즈니스 가치 조기 인도

### 2. 스크럼 3-5-3 체계 요약

<div class="itpe-pipeline is-vertical" role="img" aria-label="스크럼 3-5-3 요약">
  <div class="itpe-pipeline-node"><strong>3대 역할</strong><span>PO (가치 결정) · SM (장애 제거) · Developers (개발)</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>3대 산출물</strong><span>제품 백로그 · 스프린트 백로그 · 제품 증분(DoD)</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>5대 이벤트</strong><span>스프린트, 계획, 일일 스크럼, 리뷰, 회고</span></div>
</div>

### 3. 핵심 통제

- **완료의 정의(DoD)**: 품질 타협 없는 제품 증분 판정 기준선
- **Time-boxing**: 모든 이벤트의 최대 시간을 고정하여 집중력 및 효율 극대화

## 출제 이력과 검증 출처

- 제123회 정보관리기술사 1교시: 스크럼의 3대 역할 및 5대 이벤트
- 제129회 정보관리기술사 2교시: 애자일 스크럼의 성공 요인과 DoD의 중요성
- Ken Schwaber, Jeff Sutherland, The Scrum Guide (2020)

## 학습 체크

- [ ] 스크럼의 3대 경험주의 기둥(투명성, 점검, 적응)을 설명할 수 있는가?
- [ ] PO, SM, Developers의 핵심 책임과 차이점을 설명할 수 있는가?
- [ ] 제품 백로그 정제와 DoD(Definition of Done, 완료의 정의)의 역할을 구분할 수 있는가?

## 연결 토픽

- 이전 토픽: [정보은닉](./024_information_hiding.md)
- 연관 토픽: [칸반](./090_kanban.md), [애자일 방법론](./119_agile_methodology.md)
- 다음 토픽: [유스케이스 다이어그램](./026_use_case_diagram.md)
