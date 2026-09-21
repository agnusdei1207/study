---
title: "요구사항 도출 기법(Requirements Elicitation)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
author: "Antigravity"
date: "2026-09-21T16:36:00+09:00"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 요구공학과 요구사항 개발을 거쳐 요구사항 도출 기법으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>요구공학 · 요구사항 개발</span>
  <strong>요구사항 도출 기법</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **Requirements Elicitation(요구사항 도출)**은 이해관계자의 표현된 요구와 업무에 숨은 요구를 발견하는 활동
- 메커니즘: 이해관계자 식별 → 목적과 불확실성에 맞는 기법 조합 → 사실·가정·갈등 확인
- 산출: 출처가 식별된 요구 후보 · 용어집 · 미결정 쟁점 · 확인 기록

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 도출의 준비부터 확인까지의 흐름">
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>① 범위·정보원 식별</strong></span><span><b>활동</b> 목표·업무·권한·이해관계자 분석<br /><b>산출</b> 이해관계자 지도 · 도출 계획</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>② 기법 조합·수행</strong></span><span><b>활동</b> 인터뷰·JAD·관찰·프로토타이핑<br /><b>산출</b> 사실 · 요구 후보 · 가정 · 갈등</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>③ 확인·합의</strong></span><span><b>활동</b> 재진술·시나리오 검토·충돌 조정<br /><b>산출</b> 확인 요구 · 결정 근거 · 미결정 목록</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Requirements Elicitation(요구사항 도출)**: 이해관계자와 업무 환경에서 요구·제약·가정을 발견하고 확인하는 요구사항 개발 활동
- **Stakeholder(이해관계자)**: 시스템에 영향을 주거나 결과의 영향을 받는 요구의 출처·승인자
- **JAD(Joint Application Development)**: 사용자·개발자·의사결정자가 촉진자와 집중 합의하는 워크숍 기법
- **Prototype(프로토타입)**: 추상 요구를 조기 모형으로 가시화하여 이해 차이와 누락을 확인하는 수단
- **Observation(관찰)**: 실제 업무와 예외를 현장에서 살펴 언어화되지 않은 요구를 발견하는 기법

</details>

## 예상문제

> 요구사항 도출의 개념을 설명하고, 주요 도출 기법의 특징과 선택 기준 및 도출 과정의 품질 확보 방안을 제시하시오.

## Ⅰ. 잠재 요구를 검증 가능한 요구 후보로 바꾸는 요구사항 도출

> 도출은 요청을 받아 적는 활동이 아니라 목적과 업무 증거를 교차 확인하는 탐색이며, 성패는 기법의 수보다 출처·가정·갈등의 명시성으로 판정함.

- 정의: **이해관계자**와 운영 환경에서 **요구·제약·가정**을 발견하여 **요구 후보**로 구조화하는 요구사항 개발 활동
- 목적: 표현된 요청과 실제 업무의 간극 식별 → 누락·오해·충돌을 줄인 합의 가능한 요구 확보

## Ⅱ. 불확실성에 맞춰 조합하는 도출 기법

> 한 기법은 한 종류의 편향만 줄이므로 넓이·깊이·현장성·가시화 중 필요한 증거를 기준으로 상호 보완함.

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" style="max-width: 520px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="elicit-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Left: Elicitation Techniques Grid -->
  <rect x="15" y="15" width="230" height="190" rx="8" fill="var(--sl-color-blue-subtle, #eff6ff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1.5" filter="url(#elicit-shadow)"/>
  <text x="25" y="36" font-size="11.5" font-weight="700" fill="var(--sl-color-blue-high, #2563eb)">다차원 요구 도출 기법 조합</text>

  <rect x="25" y="46" width="98" height="42" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="32" y="63" font-size="10.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">심층 인터뷰</text>
  <text x="32" y="78" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">의사결정·심층 탐색</text>

  <rect x="135" y="46" width="98" height="42" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="142" y="63" font-size="10.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">설문조사</text>
  <text x="142" y="78" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">대규모 통계 경향</text>

  <rect x="25" y="96" width="98" height="42" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="32" y="113" font-size="10.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">현장 관찰</text>
  <text x="32" y="128" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">암묵·그림자 업무</text>

  <rect x="135" y="96" width="98" height="42" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="142" y="113" font-size="10.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">JAD 워크숍</text>
  <text x="142" y="128" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">충돌 집중 합의</text>

  <rect x="25" y="146" width="208" height="48" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1.5"/>
  <text x="35" y="166" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #7c3aed)">프로토타이핑 (UI/UX Mockup)</text>
  <text x="35" y="182" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">추상적 상호작용의 시각적 피드백 즉시 검증</text>

  <!-- Arrow -->
  <path d="M 248 110 L 272 110" fill="none" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="2"/>

  <!-- Right: Verification Gate & Output -->
  <rect x="275" y="15" width="230" height="190" rx="8" fill="var(--sl-color-green-subtle, #f0fdf4)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="1.5" filter="url(#elicit-shadow)"/>
  <text x="288" y="36" font-size="11.5" font-weight="700" fill="var(--sl-color-green-high, #16a34a)">도출 품질 게이트 &amp; 확정 산출</text>

  <rect x="288" y="48" width="204" height="42" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="1"/>
  <text x="298" y="65" font-size="10" font-weight="700" fill="var(--sl-color-text, #1f2937)">1. 출처(Source) 명시화</text>
  <text x="298" y="80" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">누가 어떤 권한으로 요구했는가?</text>

  <rect x="288" y="98" width="204" height="42" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="1"/>
  <text x="298" y="115" font-size="10" font-weight="700" fill="var(--sl-color-text, #1f2937)">2. 가정(Assumption) 분리</text>
  <text x="298" y="130" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">사실과 추정의 엄격한 식별 통제</text>

  <rect x="288" y="148" width="204" height="46" rx="4" fill="var(--sl-color-accent-subtle, #f5f3ff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1"/>
  <text x="298" y="166" font-size="10" font-weight="700" fill="var(--sl-color-accent-high, #5b21b6)">3. 충돌 조정 &amp; 확정 요구 후보</text>
  <text x="298" y="182" font-size="8.5" fill="var(--sl-color-text, #374151)">미결정 안건 소유자·기한 강제 지정</text>
</svg>
</div>

| 기법 | 적합 조건 | 활동 | 산출·주의점 |
|---|---|---|---|
| **인터뷰** | 의사결정 근거·예외의 깊이 탐색 | 개방형 질문 후 폐쇄형 확인 | 발언 근거 · 질문자 편향 통제 |
| **설문조사** | 다수 집단의 경향 확인 | 표본·문항 설계 후 정량 수집 | 응답 분포 · 심층 맥락 보완 |
| **JAD** | 부서 간 요구 충돌의 집중 합의 | 촉진자가 의제·시간·결정권 통제 | 합의안 · 소수 의견과 미결정 기록 |
| **관찰** | 실제 업무·우회가 언어화되지 않음 | 현장 행동과 업무 산출물 대조 | 업무 흐름 · 관찰 효과 통제 |
| **프로토타이핑** | 화면·상호작용 요구가 추상적임 | 조기 모형으로 과업 수행 확인 | 피드백 · 완성품 오인 방지 |

## Ⅲ. 발견에서 합의까지 이어지는 도출 통제

> 도출 품질은 회의 횟수가 아니라 각 요구가 출처·목적·확인 결과를 가지며 미해결 충돌이 결정권자에게 전달되는지로 검증함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 도출의 품질 통제 절차">
  <div class="itpe-pipeline-node"><strong>도출 준비</strong><span><b>활동</b> 목표·범위·정보원·기법·질문 설계<br /><b>산출</b> 도출 계획 · 질문지 · 업무 자료 목록</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>증거 수집</strong><span><b>활동</b> 발언과 관찰 사실을 분리하고 예외·가정 기록<br /><b>산출</b> 원시 기록 · 요구 후보 · 용어집</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>정제·분류</strong><span><b>활동</b> 중복 병합, 유형 분류, 충돌 식별<br /><b>산출</b> 구조화 요구 · 충돌·미결정 목록</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>확인·결정</strong><span><b>활동</b> 재진술·시나리오·프로토타입으로 이해 검증<br /><b>산출</b> 확인 요구 · 결정 근거 · 후속 조치</span></div>
</div>

## Ⅳ. 요구사항 도출 문제점·대응책

> 요구 누락과 충돌은 문서 양으로 해결되지 않으며 출처 추적·다중 기법 교차 확인·결정 규칙을 품질 게이트로 두어야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **대표자 편향 (요구 왜곡)** | 관리자·실무자 등 **역할별 표본화 및 익명 설문** 병행 | 특정 계층 왜곡 방지 및 실무 현장 요구사항 100% 반영 |
| **암묵 요구 누락 (기능 결함)** | **현장 관찰(Observation) 및 프로토타이핑** 결합 | 미표현된 잠재 요구 발굴 및 정상·예외 시나리오 완전성 확보 |
| **요구 충돌 방치 (일정 지연)** | **JAD 워크숍** 및 이해관계자별 의사결정권·기한 명시 | 부서 간 이견 조기 해소 및 미결정 안건 0건 달성 |
| **해결책 고착 (과잉 투자)** | 사용자 구현 요청을 **근본 목적·비즈니스 문제**로 재정의 | 불필요한 과잉 스펙 제거 및 최적의 공학적 대안 도출 |

## Ⅴ. 증거·합의 중심 도출의 결론

> 도출 종료는 의견을 모두 받은 시점이 아니라 요구별 출처와 확인 상태가 보이고 남은 쟁점의 책임자와 기한이 정해진 시점임.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 사용자는 해결책을 말하기 쉽고 실제 필요는 업무 행동과 예외에 숨어 있다. 발언·관찰·프로토타입을 교차하면 표현된 요청과 문제를 분리할 수 있다.
- `나라면`: 역할별 정보원과 검증 기법을 함께 배치하고, 회의록보다 요구별 출처·가정·미결정 상태가 보이는 저장소를 운영하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 단일 기법 의존 금지, 출처(Source) 미식별 및 가정 미검증 요구의 분석 단계 유입 차단 판정
- **대응 방안**: 심층 인터뷰 + 현장 관찰 + UI 프로토타이핑 삼각 검증 기법 적용 및 JAD 워크숍 합의
- **검증 체계**: 요구별 출처·목적·인수기준 100% 매핑 확인 및 미결정 충돌 안건의 책임자·의결 기한 강제화
- **기대 효과**: 암묵 요구 발굴률 40% 향상, 부서 간 이해 충돌 조기 종식 및 하류 공정 재작업 비용 60% 절감

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 도출 개선 제언">
  <div class="itpe-pipeline-node"><strong>현행 한계</strong><span><b>문제</b> 대표자 인터뷰와 회의록 의존으로 암묵 요구·충돌 누락</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>교차 도출</strong><span><b>대안</b> 역할별 인터뷰 · 관찰 · 프로토타입 증거 결합</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>도출 게이트</strong><span><b>판정</b> 출처·목적·가정·확인 상태와 갈등 소유자 완비</span></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>실행 결과</strong><span><b>효과</b> 합의 요구 확보 · 명세와 추적의 신뢰 가능한 입력 제공</span></div>
</div>

## 1교시 10점 답안 발췌

- 정의: **Requirements Elicitation(요구사항 도출)**은 **이해관계자**와 운영 환경에서 **요구·제약·가정**을 발견해 요구 후보로 구조화하는 활동
- 목적: 표현된 요청과 실제 업무의 간극 식별 → 누락·오해·충돌을 줄인 요구 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 도출 1교시 핵심 흐름"><div class="itpe-pipeline-node"><strong>정보원 식별</strong><span><b>활동</b> 역할·업무·권한 파악<br /><b>산출</b> 이해관계자 지도</span></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>교차 도출</strong><span><b>활동</b> 인터뷰·관찰·프로토타입 조합<br /><b>산출</b> 요구 후보·가정·갈등</span></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>확인·합의</strong><span><b>활동</b> 재진술·충돌 조정<br /><b>산출</b> 확인 요구·미결정 목록</span></div></div>

| 위험 | 대책 | 효과 |
|---|---|---|
| **대표자 편향** | 역할별 인터뷰 및 익명 설문 병행 | 핵심 사용자 역할별 요구사항 균형 반영 |
| **암묵 요구 누락** | 현장 관찰 및 화면 프로토타이핑 병행 | 미표현된 숨은 요구 발굴 및 예외 시나리오 완비 |

- 결론: 요구별 출처·가정·확인 상태와 미결정 책임자를 통제하여 명세와 추적의 신뢰 가능한 입력을 확보함

## 출제 이력과 검증 출처

- [ISO/IEC/IEEE 29148:2018 — Requirements engineering](https://www.iso.org/standard/72089.html)
- [IIBA, A Guide to the Business Analysis Body of Knowledge](https://www.iiba.org/career-resources/a-business-analysis-professionals-foundation-for-success/babok/)

## 학습 체크

- [ ] Ⅰ·정의와 목적: 이해관계자·요구·제약·가정·요구 후보의 관계를 두 줄로 재현할 수 있는가
- [ ] Ⅱ·기법 선택: 인터뷰·설문·JAD·관찰·프로토타이핑을 적합 조건과 주의점으로 비교할 수 있는가
- [ ] Ⅲ·도출 흐름: 준비→수집→정제→확인의 활동과 산출물을 각각 재현할 수 있는가
- [ ] Ⅳ·품질 통제: 네 실패 유형의 대책과 판정 기준을 연결할 수 있는가
- [ ] Ⅴ·기술사적 판단: 출처·목적·가정·확인 상태를 도출 게이트로 설명할 수 있는가

## 연결 토픽

- 이전 토픽: [요구공학](./040_requirements_engineering.md)
- 연관 토픽: [요구사항 명세](./054_requirements_specification.md), [요구사항 추적표(RTM)](./102_requirement_traceability_matrix.md)
- 다음 토픽: [의존성 주입(DI)](./042_dependency_injection.md)
