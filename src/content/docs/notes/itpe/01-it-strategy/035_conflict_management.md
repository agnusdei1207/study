---
title: "갈등관리"
author: "Antigravity"
date: "2026-09-21T18:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 조직과 이해관계자 관리를 거쳐 갈등관리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 관리·이해관계자</span>
  <strong>갈등관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 프로젝트 이해관계자 간의 견해차를 조기에 감지하고, 파괴적인 관계 갈등은 차단하되 생산적인 과업 갈등은 유도하여 팀 성과와 품질을 극대화하는 관리 기법.
- 메커니즘: 갈등 징후 감지 → 사람과 문제의 분리 → **Thomas-Kilmann 5대 모드(협력·경쟁·타협·회피·수용)** 선택 실행 → **PoC 실증 및 ADR(아키텍처 결정기록)** 합의 → 기준선 반영.
- 통제: 감정 비난 차단(Fact 기반) · 기술 논쟁 시 **Disagree and Commit** 원칙 적용 · 회의 직후 액션 아이템 RACI 및 WBS 공식 변경 통제.

<div class="itpe-flow-map" role="img" aria-label="갈등 발생 감지부터 Thomas-Kilmann 모델 적용 및 기준선 반영 흐름">
  <div class="itpe-flow-node">
    <strong>갈등 발생 징후 감지</strong>
    <small>요구사항 범위 · 자원 경합 · 아키텍처 견해차</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>사람과 문제의 분리 (Fact 규명)</small></div>
  <div class="itpe-flow-node is-current">
    <strong>Thomas-Kilmann 5대 갈등 대응 모델</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>협력</strong><span><span class="itpe-keyword"><strong>Collaborating</strong></span>: 양측 관심사를 통합</span></div>
      <div class="itpe-flow-branch"><strong>경쟁</strong><span><span class="itpe-keyword"><strong>Competing</strong></span>: 긴급·보안·안전 원칙 관철 (Zero-sum)</span></div>
      <div class="itpe-flow-branch"><strong>타협</strong><span><span class="itpe-keyword"><strong>Compromising</strong></span>: 상호 양보를 통한 현실적 절충</span></div>
      <div class="itpe-flow-branch"><strong>회피</strong><span><span class="itpe-keyword"><strong>Avoiding</strong></span>: 사소한 이슈 방치 및 감정 냉각기 확보</span></div>
      <div class="itpe-flow-branch"><strong>수용</strong><span><span class="itpe-keyword"><strong>Accommodating</strong></span>: 장기 파트너십 보호를 위한 양보</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>기술 검증(PoC) 및 합의 도출</small></div>
  <div class="itpe-flow-node">
    <strong>프로젝트 기준선 반영</strong>
    <small><span class="itpe-keyword"><strong>ADR</strong></span> 문서화 · WBS 및 RACI 갱신 · 재발 방지 모니터링</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **갈등관리(Conflict Management)**: 프로젝트 이해관계자 간의 충돌과 견해차를 조기에 진단하고 조직의 목표 달성에 기여하도록 조정하는 관리 기법
- **Thomas-Kilmann 모델(TKI)**: 자기주장성과 협조성의 2차원 축을 기반으로 갈등 대응 행동을 5가지 유형(협력, 경쟁, 타협, 회피, 수용)으로 구조화한 프레임워크
- **Assertiveness(자기주장성)**: 갈등 상황에서 자신의 입장, 목표, 관심사를 관철하려는 성향의 강도
- **Cooperativeness(협조성)**: 갈등 상황에서 타인의 관심사와 요구를 배려하고 충족시키려는 성향의 강도
- **과업 갈등(Task Conflict)**: 프로젝트 목표, 요구사항 범위, 아키텍처 기술 스택 등에 대한 생산적이고 건설적인 업무상 이견
- **관계 갈등(Relationship Conflict)**: 성격 차이, 의사소통 스타일, 상호 불신에서 기인하는 파괴적인 감정적 대립
- **프로세스 갈등(Process Conflict)**: 역할 분담(R&R)과 업무 수행 절차, 자원 배분 방식을 둘러싼 절차적 마찰
- **ADR(Architectural Decision Record)**: 기술 아키텍처 갈등 발생 시 최종 의사결정의 맥락, 대안 비교, 채택 이유를 명시한 공학적 의사결정 문서
- **하버드 협상 원칙(PON)**: 사람과 문제를 분리하고, 입장이 아닌 본질적 이해관계에 집중하여 객관적 기준을 통해 상호 이익을 창출하는 협상 프레임워크

</details>

## 예상문제

> 프로젝트 갈등의 유형을 설명하고, Thomas–Kilmann 5대 대응모드와 상황별 적용 및 중재방안을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 위기를 팀 성장의 기회로 전환하는 갈등관리의 개요

> 갈등관리는 이견을 제거하는 활동이 아니라 관계 갈등의 영향을 줄이고 과업 이견을 근거 기반 의사결정으로 전환하는 활동임.

- 정의: 프로젝트 목표 달성 과정에서 발생하는 이해관계자 간의 대립과 이견을 조기에 식별하고 **Thomas-Kilmann 모델**을 통해 조정하는 **프로젝트 관리 프로세스**
- 목적: 관계 갈등 조기 차단, 생산적 과업 갈등 유도, 팀 결속력 강화

## Ⅱ. 갈등의 3대 유형과 주요 발생 원인

> 과업 갈등은 근거 기반 토론으로 전환하고, 관계 갈등은 감정 확산을 줄이며, 프로세스 갈등은 역할·절차를 명확히 하여 관리함.

| 갈등 유형 | 핵심 원인 및 성격 | 프로젝트에 미치는 영향 | 관리 및 통제 방향 |
|---|---|---|---|
| **과업 갈등 (Task)** | 요구사항 범위, 아키텍처 설계, 기술 스택 선정에 대한 이견 | 적정 수준 유지 시 창의적 대안 발굴 및 품질 향상 | 적극적 기술 토론 및 **PoC** 실증 검증 유도 |
| **관계 갈등 (Relationship)** | 성격 차이, 의사소통 스타일 불일치, 상호 불신 및 감정 대립 | 팀 사기 저하, 의사소통 단절, 생산성 급락 | 중립적 중재 · 행동규칙 · 필요 시 개별 상담 |
| **프로세스 갈등 (Process)** | 과업 수행 절차, 책임 할당(R&R), 자원 배분 기준에 대한 마찰 | 작업 지연, 책임 전가(핑퐁), 일정 병목 발생 | **RACI 매트릭스** 정립 및 공식 워크플로우 확정 |

## Ⅲ. Thomas-Kilmann 5대 갈등 해결 모델 아키텍처

> **자기주장성(Assertiveness)**과 **협조성(Cooperativeness)**의 2차원 축을 기준으로 상황에 맞는 최적의 모드를 선택함.

<div class="itpe-diagram-box">
  <svg viewBox="0 0 520 230" width="100%" height="230" role="img" aria-label="Thomas-Kilmann 5대 갈등 해결 모델 2차원 매트릭스 다이어그램">
    <!-- Axes and Background Grid -->
    <line x1="80" y1="20" x2="80" y2="190" stroke="var(--sl-color-gray-4)" stroke-width="2"/>
    <line x1="80" y1="190" x2="480" y2="190" stroke="var(--sl-color-gray-4)" stroke-width="2"/>
    <text x="35" y="105" fill="var(--sl-color-gray-2)" font-size="10" font-weight="bold" transform="rotate(-90 40 105)">자기주장성 (Assertiveness)</text>
    <text x="280" y="210" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="10" font-weight="bold">협조성 (Cooperativeness)</text>
    <text x="110" y="205" fill="var(--sl-color-gray-3)" font-size="9">낮음(비협조적)</text>
    <text x="410" y="205" fill="var(--sl-color-gray-3)" font-size="9">높음(협조적)</text>
    <text x="45" y="160" fill="var(--sl-color-gray-3)" font-size="9">낮음</text>
    <text x="45" y="45" fill="var(--sl-color-gray-3)" font-size="9">높음</text>

    <!-- 1. Competing (Top-Left): High Assertive, Low Cooperative -->
    <rect x="90" y="25" width="170" height="65" rx="5" fill="var(--sl-color-red-low)" stroke="var(--sl-color-red)" stroke-width="1.5"/>
    <text x="175" y="45" text-anchor="middle" fill="var(--sl-color-red-high)" font-size="11" font-weight="bold">경쟁 (Competing)</text>
    <text x="175" y="62" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9.5">긴급 대응 · 보안 규정 관철</text>
    <text x="175" y="78" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">Win-Lose 독단적 결정</text>

    <!-- 2. Collaborating (Top-Right): High Assertive, High Cooperative -->
    <rect x="295" y="25" width="170" height="65" rx="5" fill="var(--sl-color-blue-low)" stroke="var(--sl-color-blue)" stroke-width="1.5"/>
    <text x="380" y="45" text-anchor="middle" fill="var(--sl-color-blue-high)" font-size="11" font-weight="bold">협력 (Collaborating)</text>
    <text x="380" y="62" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9.5">핵심 쟁점 통합 · 장기 신뢰</text>
    <text x="380" y="78" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">Win-Win 시너지 대안 탐색</text>

    <!-- 3. Compromising (Center): Mid Assertive, Mid Cooperative -->
    <rect x="195" y="75" width="165" height="55" rx="5" fill="var(--sl-color-green-low)" stroke="var(--sl-color-green)" stroke-width="1.5"/>
    <text x="277" y="95" text-anchor="middle" fill="var(--sl-color-green-high)" font-size="11" font-weight="bold">타협 (Compromising)</text>
    <text x="277" y="110" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9">납기 임박 · 상호 양보 절충안</text>
    <text x="277" y="122" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">현실적 차선책 합의</text>

    <!-- 4. Avoiding (Bottom-Left): Low Assertive, Low Cooperative -->
    <rect x="90" y="115" width="170" height="65" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1.5"/>
    <text x="175" y="135" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="11" font-weight="bold">회피 (Avoiding)</text>
    <text x="175" y="152" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="9.5">사소한 쟁점 · 감정 냉각기</text>
    <text x="175" y="168" text-anchor="middle" fill="var(--sl-color-gray-3)" font-size="8.5">판단 유예 및 후속 관찰</text>

    <!-- 5. Accommodating (Bottom-Right): Low Assertive, High Cooperative -->
    <rect x="295" y="115" width="170" height="65" rx="5" fill="var(--sl-color-purple-low)" stroke="var(--sl-color-purple)" stroke-width="1.5"/>
    <text x="380" y="135" text-anchor="middle" fill="var(--sl-color-purple-high)" font-size="11" font-weight="bold">수용 (Accommodating)</text>
    <text x="380" y="152" text-anchor="middle" fill="var(--sl-color-gray-1)" font-size="9.5">관계 보존 우선 · 과실 인정</text>
    <text x="380" y="168" text-anchor="middle" fill="var(--sl-color-gray-2)" font-size="8.5">Lose-Win 전략적 양보</text>
  </svg>
</div>

| 대응 모드 | 행동적 특성 | 최적 적용 상황 (Best Practice) | 주의점 및 부작용 |
|---|---|---|---|
| **협력 (Collaborating)** | 자기주장과 협조성이 모두 높은 Win-Win 대안 추구 | 양측의 쟁점이 모두 중요하여 타협할 수 없고 시간이 충분할 때 | 많은 시간과 높은 신뢰, 커뮤니케이션 비용 소요 |
| **경쟁 (Competing)** | 자신의 입장을 강하게 관철하는 독단적·비협조적 접근 | 보안 규정 준수, 긴급 장애 복구 등 타협 불가능한 원칙 준수 시 | 패자의 반발, 팀워크 훼손 및 적대감 유발 위험 |
| **타협 (Compromising)** | 중간 수준의 주장과 협조를 통한 상호 절충안 마련 | 마감 시한이 임박하고 동등한 권한을 가진 당사자 간 대립 시 | 미봉책에 그쳐 차후 동일 이슈가 재발할 위험 |
| **회피 (Avoiding)** | 갈등을 인지하고도 개입을 유예하거나 뒤로 미룸 | 쟁점이 사소하거나 당사자들의 격앙된 감정 냉각이 필요할 때 | 방치 시 문제가 확대되어 통제 불능 상태 초래 |
| **수용 (Accommodating)** | 자신의 주장을 접고 상대방의 요구를 전폭 수용 | 자신이 틀렸음을 인정하거나 장기적 파트너십 보호가 우선일 때 | 수용자의 발언권 위축 및 박탈감 누적 |

## Ⅳ. 갈등 중재와 해결의 5단계 엔지니어링 프로세스

> 비언어적 징후 포착에서 출발하여 사람과 문제를 분리하고, 팩트 기반의 합의안을 프로젝트 기준선에 반영하여 사후 재발을 차단함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="갈등 중재 5단계 엔지니어링 프로세스 파이프라인">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>① 갈등 조기 감지 (Detection)</strong></span>
      <strong>활동</strong><span>회의·이슈·업무지연에서 징후 확인</span><strong>산출</strong><span>갈등 이슈</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>② 사람과 문제의 분리 (Separation)</strong></span>
      <strong>활동</strong><span>사실·해석·감정·요구 구분</span><strong>산출</strong><span>쟁점·사실 목록</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>③ 본질적 이해관계 분석 (Analysis)</strong></span>
      <strong>활동</strong><span>입장 뒤의 관심사·제약 확인</span><strong>산출</strong><span>이해관계·선택기준</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>④ 상황별 대응모드 실행 (Resolution)</strong></span>
      <strong>활동</strong><span>대응모드 선택 · 필요 시 PoC·ADR</span><strong>산출</strong><span>합의안·결정기록</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <span class="itpe-keyword"><strong>⑤ 제도화 및 기준선 반영 (Institutionalization)</strong></span>
      <strong>활동</strong><span>책임·계획·후속조치 갱신</span><strong>산출</strong><span>변경계획 · 이행점검</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Fact-based Decision</strong></span> · 사람과 문제를 분리하고 PoC 실증 데이터와 ADR 문서로 객관적 합의 도출</div>

## Ⅴ. Thomas-Kilmann 모델 vs 하버드 협상 원칙(PON) 비교

> TKI가 상황에 따른 '행동 양식의 선택'이라면, 하버드 협상 원칙은 '협력(Collaborating)을 구체적으로 실천하는 기술'임.

| 비교 항목 | Thomas-Kilmann 모델 (TKI) | 하버드 협상 원칙 (PON) |
|---|---|---|
| 기본 관점 | 상황과 성향에 따른 5가지 행동 양식의 유연한 선택 | 원칙 기반의 접근을 통해 상호 윈-윈(Win-Win) 창출 |
| 핵심 메시지 | 모든 모드는 고유의 쓰임새가 있으며 상황에 맞춰야 함 | 입장에 얽매이지 말고 상호 숨겨진 이익에 집중하라 |
| 접근 메커니즘 | 자기주장성(Assertiveness) vs 협조성(Cooperativeness) 매트릭스 | 4대 원칙 (사람 분리, 이해관계 집중, 대안 개발, 객관적 기준) |
| 주 활용 상황 | 팀 내부의 일상적 성향 진단 및 갈등 국면 판정 | 복잡한 계약 협상, 대규모 범위 변경, 대외 이해관계 분쟁 |
| 상호 관계 | 갈등의 현재 위치와 최적 모드를 진단하는 도구 | 협력(Collaborating) 모드를 실행하기 위한 실천 방법론 |

## Ⅵ. 실무 갈등관리 실패 요인과 공학적 통제 방안

> 감정 대립과 구두 합의의 번복을 방어하지 못하면 프로젝트는 치명적인 정치적 소모전에 휘말림.

| 위험 | 대책 | 효과 |
|---|---|---|
| **감정적 비난 전이** | 사실·해석·감정을 분리하고 중립적 회의규칙 적용 | 쟁점 중심 논의 |
| **PM의 일방적 강요** | 부하 테스트, 벤치마크 결과 등 객관적 수치 기반 의사결정 | 팀원의 심리적 저항 및 태업 방지 확인 |
| **결정 장애·방임** | 결정권자·기한·에스컬레이션 경로 명시 | 결정 지연 방지 |
| **합의안 사후 파기** | 중재 회의 직후 액션 아이템, 책임자, 기한 명시 회의록 배포 | WBS 및 RACI 기준선 공식 반영 완료 |

## Ⅶ. 심리적 안전감과 데이터 기반 중재 중심의 기술사적 제언

> 갈등의 부재는 평화가 아닌 무관심의 증거이며, 진정한 고성과 팀은 과업 갈등을 자유롭게 분출할 수 있는 심리적 안전감 위에서 탄생함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]` 갈등을 없애려 하면 위험정보까지 침묵할 수 있으므로, 과업 이견은 근거와 실험으로 다루고 인신공격·보복은 분리 통제해야 함.
- `나라면` 쟁점별 결정권자·기한·객관적 기준을 먼저 정하고, 기술대안은 필요한 수준의 PoC와 ADR로 비교한 뒤 결정과 후속조치를 추적하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 갈등 발생 후 프로젝트 일정에 미치는 지연이 3영업일 이내이고 도출된 합의안이 ADR로 100% 문서화되는지 여부.
- **공학적 대안**: 감정적 논쟁 배제, 기술 스택 갈등 시 PoC 실측 성능 벤치마크 + **Disagree and Commit** 원칙 적용.
- **검증 절차**: 합의된 의사결정 사항의 WBS 작업 패키지 및 RACI 매트릭스 반영 여부를 주간 PMO 회의에서 점검.
- **기대 효과**: 파괴적 관계 갈등 원천 차단, 심리적 안전감(Psychological Safety)에 기반한 고품질 아키텍처 수렴.

<div class="itpe-pipeline is-vertical" role="img" aria-label="갈등관리 거버넌스 제언 흐름">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>현행 한계</strong>
      <strong>문제</strong><span>감정 전이 · 권위적 강요 · 결정 장애</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>개선 대안</strong>
      <strong>대안</strong><span>사실·관심사 분리 · 객관적 기준 · 결정권·기한</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>검증 기준</strong>
      <strong>판정</strong><span>결정근거 · 책임자 · 후속조치 · 계획 반영</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>실행 효과</strong>
      <strong>효과</strong><span>건설적 과업갈등 · 결정지연 축소 · 심리적 안전</span>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **갈등관리(Conflict Management)**는 프로젝트 목표 달성 과정에서 발생하는 이해관계자 간의 대립과 이견을 조기에 식별하고 **Thomas-Kilmann 모델**을 통해 조정하는 **프로젝트 관리 프로세스**
- 목적: 관계 갈등 조기 차단, 생산적 과업 갈등 유도, 팀 결속력 강화

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="갈등관리 프로세스 요약">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>징후 감지</strong>
      <span>PR 리뷰 · 스탠드업 미팅</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>사람·문제 분리</strong>
      <span>감정 배제 · 이슈 로그 등록</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>모드 실행</strong>
      <span>Thomas-Kilmann 5대 모드</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>공학적 검증</strong>
      <span>PoC 실증 · ADR 기록</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail">
      <strong>제도화</strong>
      <span>WBS · RACI 기준선 반영</span>
    </div>
  </div>
</div>

### 3. 핵심 통제

- **Thomas-Kilmann 5대 모드**: 협력(Win-Win), 경쟁(긴급 원칙), 타협(절충), 회피(사소한 문제), 수용(관계 보존)
- **공학적 통제**: **ADR(Architectural Decision Record)** 작성 및 **Disagree and Commit** 원칙 적용으로 결정 장애 극복

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [The Myers-Briggs Company: Thomas–Kilmann Conflict Mode Instrument](https://www.themyersbriggs.com/en-US/Products-and-Services/TKI)
- [Harvard Program on Negotiation: Principled Negotiation](https://www.pon.harvard.edu/daily/negotiation-skills-daily/principled-negotiation-focus-interests-to-create-value/)

## 학습 체크

- [ ] Ⅰ~Ⅱ. 과업·관계·프로세스 갈등의 차이와 관리방향을 설명할 수 있는가?
- [ ] Ⅲ. Assertiveness·Cooperativeness 축과 5대 대응모드를 재현할 수 있는가?
- [ ] Ⅳ. 감지부터 계획 반영까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅴ. TKI와 원칙중심 협상을 목적·메커니즘·적용상황으로 비교할 수 있는가?
- [ ] Ⅵ~Ⅶ. 감정 전이·강요·결정 장애·합의 파기의 대응책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [SWOT 분석](./034_swot_analysis.md)
- 연관 토픽: [터크만 팀 발달 모델](./028_tuckman_team_development_model.md), [PMO](./004_pmo.md), [프로젝트 관리](./065_project_management.md), [부정적 위험 대응 전략](./040_negative_risk_response_strategy.md)
- 다음 토픽: [NIST AI RMF](./036_nist_ai_rmf.md)
