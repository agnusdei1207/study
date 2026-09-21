---
title: "애자일(Agile) 방법론"
category: "02-software-engineering"
tags:
  - "Agile"
  - "애자일"
  - "스크럼"
  - "Scrum"
  - "XP"
  - "스프린트"
  - "개발방법론"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 개발 프로세스 및 방법론을 거쳐 애자일 방법론으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>개발 프로세스·방법론</span>
  <strong>애자일(Agile) 방법론</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 불확실성이 높고 요구사항이 급변하는 시장 환경에서 초기 고정 계획에 매몰되는 실패를 방지하기 위해, 1~4주 단위의 짧은 이터레이션(Sprint)을 반복하며 '동작하는 소프트웨어 증분'을 조기에 출시하고 고객 피드백을 지속 반영하는 적응형(Adaptive) 개발 패러다임
- 메커니즘: 비전 수립 → 제품 백로그(Product Backlog) 우선순위화 → 스프린트 계획 및 개발(일일 스탠드업, CI/CD) → 동작 소프트웨어 시연(Sprint Review) → 프로세스 개선(회고) 반복
- 산출물: 제품 백로그 · 스프린트 백로그 · 잠재적 출시 가능 제품 증분(Increment) · 스프린트 번다운 차트(Burndown Chart)

<div class="itpe-flow-map" role="img" aria-label="애자일 개발 이터레이션 및 피드백 루프">
  <div class="itpe-flow-node">
    <strong>1단계: 제품 백로그 수립 및 우선순위화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>주체</strong><span>제품 책임자(PO)가 비즈니스 가치 기반 사용자 스토리 정제</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 스프린트 계획 및 실행 (1~4주)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>실천</strong><span>일일 스탠드업 미팅 · TDD · 페어 프로그래밍 · 지속적 통합(CI)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: 스프린트 리뷰 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>완료 정의(DoD)를 충족하고 동작하는 소프트웨어 증분인가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Pass)</strong>
      <span>이해관계자 승인 → 프로덕션 즉시 배포 가능 증분 확정</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (Fail)</strong>
      <span>미완료 스토리 백로그 재등록 → 다음 스프린트 재계획</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **애자일 선언문(Agile Manifesto)**: 2001년 17인의 소프트웨어 지도자들이 발표한 선언으로, 공정과 도구보다 '개인과 상호작용', 포괄적 문서보다 '동작하는 소프트웨어', 계약 협상보다 '고객과의 협력', 계획 준수보다 '변화에 대한 대응'을 강조
- **스프린트(Sprint)**: 1주에서 4주 사이의 고정된 기간(Time-box) 동안 계획된 기능 목록을 완전히 개발·테스트하여 배포 가능한 증분을 만들어내는 기본 개발 단위
- **완료 정의(DoD, Definition of Done)**: 단순히 개발 코드를 작성한 것을 넘어, 단위 테스트 100% 통과, 코드 리뷰 완료, 배포 파이프라인 통과 등 팀 전체가 합의한 '완전한 완료'의 체크리스트
- **제품 증분(Increment)**: 이전 스프린트들의 결과물에 현재 스프린트에서 완료된 백로그 항목들이 통합되어 즉시 출시 가능한 상태의 소프트웨어 조각
</details>

## 1. 개요 및 필요성

### 폭포수 모델의 한계와 애자일 패러다임의 출현

과거 대규모 계획 중심의 폭포수(Waterfall) 모델은 요구사항 분석부터 최종 인도까지 수개월에서 수년이 소요된다. 이 기간 동안 비즈니스 환경과 고객의 요구가 급변하면, 완성된 소프트웨어는 막대한 비용과 시간을 들였음에도 **시장에서 아무도 쓰지 않는 소프트웨어로 전락(요구 불일치 참사)**한다.

애자일 방법론은 불확실성을 피할 수 없는 현실로 인정하고, **요구사항 변경을 적극적으로 환영(Embrace Change)**한다. 짧은 주기로 실행 가능한 소프트웨어를 만들어 실제 사용자에게 보여주고 피드백을 흡수함으로써, 프로젝트 후반부 대형 실패 리스크를 조기에 제거하고 가치 전달 속도를 극대화한다.

### 애자일 vs 폭포수 방법론 비교

| 구분 | 애자일 방법론 (Agile) | 폭포수 모델 (Waterfall) |
|---|---|---|
| **기본 철학** | 가변적 범위(Variable Scope), 적응형(Adaptive) | 고정된 범위(Fixed Scope), 예측형(Predictive) |
| **요구사항 관리** | 개발 진행 중 지속적 변경 및 우선순위 재조정 | 초기 요구사항 동결(Baseline), 변경 통제 엄격 |
| **인도 방식** | 1~4주 단위의 점진적·반복적 릴리스 | 프로젝트 최종 단계에서 일괄 릴리스(Big-Bang) |
| **고객 참여** | 스프린트 리뷰 및 일상적인 지속적 협력 | 착수(요구정의) 및 최종 인수 단계에 집중 |
| **성공 측정 지표** | 실제 비즈니스 가치 및 동작하는 소프트웨어 | 사전 수립된 일정·예산·계획 준수율 |

## 2. 아키텍처 및 핵심 메커니즘

### 애자일 4대 핵심 선언 (Agile Manifesto)

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="ag-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Background Frame -->
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="26" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">애자일 선언문 4대 가치 (우측 가치에 더 높은 우선순위 부여)</text>

    <!-- 4 Rows Comparison -->
    <!-- Row 1 -->
    <rect x="20" y="38" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="117" y="58" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">공정과 도구 (Processes & Tools)</text>
    <line x1="220" y1="54" x2="295" y2="54" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#ag-arrow)"/>
    <text x="257" y="50" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">보다</text>
    <rect x="305" y="38" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <text x="402" y="58" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">개인과 상호작용 (Individuals)</text>

    <!-- Row 2 -->
    <rect x="20" y="76" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="117" y="96" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">포괄적인 문서 (Documentation)</text>
    <line x1="220" y1="92" x2="295" y2="92" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#ag-arrow)"/>
    <text x="257" y="88" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">보다</text>
    <rect x="305" y="76" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <text x="402" y="96" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">동작하는 소프트웨어 (Working SW)</text>

    <!-- Row 3 -->
    <rect x="20" y="114" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="117" y="134" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">계약 협상 (Contract Negotiation)</text>
    <line x1="220" y1="130" x2="295" y2="130" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#ag-arrow)"/>
    <text x="257" y="126" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">보다</text>
    <rect x="305" y="114" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <text x="402" y="134" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">고객과의 협력 (Collaboration)</text>

    <!-- Row 4 -->
    <rect x="20" y="152" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="117" y="172" text-anchor="middle" font-size="8" fill="var(--color-text-muted, #64748b)">계획 준수 (Following a Plan)</text>
    <line x1="220" y1="168" x2="295" y2="168" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#ag-arrow)"/>
    <text x="257" y="164" text-anchor="middle" font-size="7" fill="var(--color-primary, #2563eb)">보다</text>
    <rect x="305" y="152" width="195" height="32" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <text x="402" y="172" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">변화에 대응 (Responding to Change)</text>

    <!-- Bottom Principle -->
    <text x="260" y="202" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">좌측의 가치를 배제하는 것이 아니며, 우측 항목에 더 높은 실천적 우선순위를 둠</text>
  </svg>
</div>

### 애자일 실천 프레임워크 4대 축

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="sp-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Background -->
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    
    <!-- Stage 1: Product Backlog -->
    <rect x="15" y="20" width="105" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="15" y="20" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="67" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">① 제품 백로그</text>
    <text x="67" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">PO 요구사항 정제</text>
    <text x="67" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">사용자 스토리 관리</text>
    <text x="67" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[비즈니스 가치순]</text>

    <!-- Arrow 1 -> 2 -->
    <line x1="120" y1="72" x2="138" y2="72" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#sp-arrow)"/>

    <!-- Stage 2: Sprint Planning -->
    <rect x="140" y="20" width="105" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="140" y="20" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="192" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">② 스프린트 계획</text>
    <text x="192" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">스프린트 백로그 확정</text>
    <text x="192" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">팀 작업량 추정</text>
    <text x="192" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[1~4주 타임박스]</text>

    <!-- Arrow 2 -> 3 -->
    <line x1="245" y1="72" x2="263" y2="72" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#sp-arrow)"/>

    <!-- Stage 3: Sprint Execution -->
    <rect x="265" y="20" width="110" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <rect x="265" y="20" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="320" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">③ 스프린트 개발</text>
    <text x="320" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">일일 스탠드업(15분)</text>
    <text x="320" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">TDD / CI 파이프라인</text>
    <text x="320" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">[번다운 차트 관리]</text>

    <!-- Arrow 3 -> 4 -->
    <line x1="375" y1="72" x2="393" y2="72" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#sp-arrow)"/>

    <!-- Stage 4: Review & Retro -->
    <rect x="395" y="20" width="110" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="395" y="20" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="450" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">④ 리뷰 및 회고</text>
    <text x="450" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">동작 SW 시연</text>
    <text x="450" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">프로세스 KPT 개선</text>
    <text x="450" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[출시 가능 증분]</text>

    <!-- Bottom Feedback Loop -->
    <path d="M 450 125 L 450 155 L 67 155 L 67 135" fill="none" stroke="var(--color-accent, #0284c7)" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#sp-arrow)"/>
    <rect x="170" y="165" width="180" height="22" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-accent, #0284c7)" stroke-width="1"/>
    <text x="260" y="179" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-accent, #0284c7)">지속적 피드백 및 다음 이터레이션 반복</text>
  </svg>
</div>

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 스크럼 (Scrum)</strong></span>
      <span class="itpe-badge">관리 프레임워크</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>3대 역할: 제품 책임자(PO), 스크럼 마스터(SM), 개발팀</li>
        <li>5대 이벤트: 스프린트, 계획, 일일 스탠드업, 리뷰, 회고</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 익스트림 프로그래밍 (XP)</strong></span>
      <span class="itpe-badge">엔지니어링 실천</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>테스트 주도 개발(TDD), 페어 프로그래밍, 지속적 리팩토링</li>
        <li>지속적 통합(CI)을 통한 코드 품질 및 기술 부채 조기 통제</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 칸반 (Kanban)</strong></span>
      <span class="itpe-badge">흐름 최적화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>작업 흐름의 시각화 및 진행 중 작업 제한(WIP Limit)</li>
        <li>병목 구간 해소 및 리드 타임(Lead Time) 단축에 집중</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 대규모 애자일 (SAFe / LeSS)</strong></span>
      <span class="itpe-badge">엔터프라이즈 확장</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>수십~수백 개 팀 간 의존성을 정렬하는 Release Train(ART)</li>
        <li>전사 포트폴리오 전략과 팀 단위 스프린트의 일관성 동기화</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 스프린트 주기는 도는데 회귀 테스트가 수작업으로 지연되어 릴리스 배포 마비 | XP 실천법(TDD, 단위/통합 테스트 자동화)을 도입하고 완료 정의(DoD)에 CI 파이프라인 통과 명시 | 배포 주기 단축 및 릴리스 품질 상시 보장 |
| 경영진과 현업 부서가 스프린트 도중 일방적으로 요구사항을 추가하여 스프린트 파산 | PO에게 우선순위 단일 결정권을 부여하고, 진행 중인 스프린트 스코프는 변경 불가(스프린트 잠금) 강제 | 개발팀의 집중도 보장 및 스프린트 목표 달성률 향상 |
| 고정 금액·고정 범위 중심의 전통적 SI 계약 제도와 애자일의 가변 범위 충돌 | 계약 시 기능점수(FP) 단가 기반 반복 계약 또는 과업심의위원회 연계를 통한 유연한 범위 조정 체계 수립 | 법적 분쟁 방지 및 합법적 애자일 계약 이행 |

## 4. 점검 및 합격 기준 (Checklist & Exit Criteria)

### 애자일 스프린트 완료 정의(DoD) 체크리스트

| 점검 영역 | 상세 검증 항목 | 합격 기준 |
|---|---|---|
| **개발 검증** | 사용자 스토리 수용 조건(Acceptance Criteria) 충족 | 기획자/PO 기능 동작 승인 |
| **품질 검증** | 단위/통합 테스트 자동화 통과 및 커버리지 달성 | C1 커버리지 80% 이상 충족 |
| **코드 검증** | SonarQube 정적 분석 및 동료 코드 리뷰(PR) 승인 | 블로커/크리티컬 결함 0건 |
| **운영 검증** | 스테이징 환경 자동 배포 및 스모크 테스트 통과 | 배포 파이프라인 100% 녹색 통과 |

## 5. 기대 효과 및 미래 전망

- **기대 효과**:
  - **비즈니스 민첩성(Time-to-Market)**: 수개월의 출시 대기 시간을 수주 단위로 단축하여 시장 선점.
  - **프로젝트 리스크 조기 헷지**: 동작하는 소프트웨어를 조기에 검증하여 릴리스 단계 대형 결함 유출 방지.
- **미래 전망**:
  - 생성형 AI 어시스턴트(Copilot)를 결합하여 백로그 분해 및 스토리 포인트 추정 자동화.
  - 플랫폼 엔지니어링 및 GitOps 기반의 셀프서비스 인프라를 통한 스프린트 내 무중단 배포 일상화.

## 6. 결론 및 실전 팁

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**  
> 많은 조직이 매일 아침 서서 15분 회의를 하고 포스트잇을 붙이는 것만으로 스스로 애자일을 실천한다고 착각하는 '형식적 애자일(Fake Agile)'의 함정에 빠진다. 진정한 애자일은 프로세스 행사에 있는 것이 아니라, **익스트림 프로그래밍(XP)의 엄격한 엔지니어링 규율(TDD, CI/CD, 자동화된 테스트 파이프라인, 지속적 리팩토링)**이 톱니바퀴처럼 맞물려 돌아갈 때만 성립한다. 엔지니어링 역량이 없는 애자일은 단지 '통제되지 않는 무질서'일 뿐이다.

> **[나라면 이렇게 쓴다]**  
> 애자일 방법론 문제가 출제되면, 단순히 스크럼의 3-5-3 규칙(3대 역할, 5대 이벤트, 3대 산출물)만 서술하는 것은 합격권의 기본일 뿐이다. 차별화를 위해 3단락에서 **구글 DORA 4대 핵심 지표(배포 빈도, 변경 리드타임, 변경 실패율, 서비스 복구시간 MTTR)**를 제시하여 애자일 성숙도를 정량적으로 측정·평가하는 엔터프라이즈 운영 거버넌스를 제언하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 스프린트 종료 시점에 '완료 정의(DoD)' 충족 여부를 엄격히 판정하며, 미완료 백로그 항목은 스프린트 리뷰 전 출시 증분에서 전면 제외.
- **대응 방안**: 스크럼 관리 프로세스에 XP의 엔지니어링 실천법(TDD, CI/CD 자동화)을 필수 내재화하여 기술 부채 누적 원천 방지.
- **검증 체계**: DORA 4대 지표(배포 빈도 주 1회 이상, 리드타임 1일 이내 등)를 대시보드화하여 분기별 애자일 성숙도 실사 수행.
- **기대 효과**: 요구사항 변경 수용 리드타임을 70% 단축하고, 릴리스 결함 밀도를 0.2건/FP 이하로 유지하여 비즈니스 적응성 극대화.

<div class="itpe-flow-map" role="img" aria-label="애자일 거버넌스 및 성숙도 개선 파이프라인">
  <div class="itpe-flow-node">
    <strong>스프린트 실행</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>개발</strong><span>XP 기반 TDD / CI 자동화</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>완료 정의 (DoD) 검증</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>게이트</strong><span>품질/보안 기준 100% 통과</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node is-current">
    <strong>DORA 성숙도 측정</strong>
    <div class="itpe-step-detail">
      <strong>평가</strong><span>배포 빈도 및 리드타임 계측</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>지속적 조직 개선</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>결과</strong><span>비즈니스 가치 즉시 전달</span></div>
    </div>
  </div>
</div>

## 7. 참고 및 연계 학습

- [스크럼(Scrum) 프레임워크](./025_scrum.md)
- [칸반(Kanban) 방법론](./090_kanban.md)
- [CI/CD 지속적 통합 및 배포](./095_ci_cd.md)
- [테스트 자동화(Test Automation)](./091_test_automation.md)

