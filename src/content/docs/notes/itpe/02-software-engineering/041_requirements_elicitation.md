---
title: "요구사항 도출 기법(Requirements Elicitation)"
author: "Codex"
date: "2026-09-20T19:30:40+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
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
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>① 범위·정보원 식별</strong></span><small><b>활동</b> 목표·업무·권한·이해관계자 분석<br /><b>산출</b> 이해관계자 지도 · 도출 계획</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>② 기법 조합·수행</strong></span><small><b>활동</b> 인터뷰·JAD·관찰·프로토타이핑<br /><b>산출</b> 사실 · 요구 후보 · 가정 · 갈등</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>③ 확인·합의</strong></span><small><b>활동</b> 재진술·시나리오 검토·충돌 조정<br /><b>산출</b> 확인 요구 · 결정 근거 · 미결정 목록</small></div>
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
  <div class="itpe-pipeline-node"><strong>도출 준비</strong><small><b>활동</b> 목표·범위·정보원·기법·질문 설계<br /><b>산출</b> 도출 계획 · 질문지 · 업무 자료 목록</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>증거 수집</strong><small><b>활동</b> 발언과 관찰 사실을 분리하고 예외·가정 기록<br /><b>산출</b> 원시 기록 · 요구 후보 · 용어집</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>정제·분류</strong><small><b>활동</b> 중복 병합, 유형 분류, 충돌 식별<br /><b>산출</b> 구조화 요구 · 충돌·미결정 목록</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>확인·결정</strong><small><b>활동</b> 재진술·시나리오·프로토타입으로 이해 검증<br /><b>산출</b> 확인 요구 · 결정 근거 · 후속 조치</small></div>
</div>

## Ⅳ. 도출 실패 유형과 품질 확보 방안

> 요구 누락과 충돌은 문서 양으로 해결되지 않으며 출처 추적·다중 기법 교차 확인·결정 규칙을 품질 게이트로 두어야 함.

| 실패 유형 | 원인 | 통제 방안 | 판정 기준 |
|---|---|---|---|
| 대표자 편향 | 관리자·강한 발언자에 출처 집중 | 역할별 표본화 · 익명 설문 병행 | 핵심 사용자 역할별 확인 기록 |
| 암묵 요구 누락 | 인터뷰만 수행 | 관찰 · 업무 문서 분석 · 프로토타입 조합 | 정상·예외 시나리오 반영 |
| 요구 충돌 방치 | 결정권·우선순위 기준 부재 | JAD · 결정권자 · 결정 기한 명시 | 소유자·기한 없는 미결정 0건 |
| 해결책 고착 | 사용자의 구현안만 수용 | 목적·문제·대안 분리 | 구현 수단이 아닌 필요·제약 기술 |

## Ⅴ. 증거와 의사결정이 남는 도출 거버넌스

> 도출 종료는 의견을 모두 받은 시점이 아니라 요구별 출처와 확인 상태가 보이고 남은 쟁점의 책임자와 기한이 정해진 시점임.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 사용자는 해결책을 말하기 쉽고 실제 필요는 업무 행동과 예외에 숨어 있다. 발언·관찰·프로토타입을 교차하면 표현된 요청과 문제를 분리할 수 있다.
- `나라면`: 역할별 정보원과 검증 기법을 함께 배치하고, 회의록보다 요구별 출처·가정·미결정 상태가 보이는 저장소를 운영하겠다.

### 실전 답안용 기술사적 제언

- 판정: 단일 기법 의존과 출처 없는 요구가 누락·오해의 핵심 원인
- 대안: 역할별 인터뷰에 관찰·프로토타입을 조합하고 갈등 소유자 지정
- 검증: 요구별 출처·목적·확인 상태와 미결정 소유자·기한 점검
- 효과: 암묵 요구 가시화 · 충돌 조기 결정 · 명세 재작업 감소

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 도출 개선 제언">
  <div class="itpe-pipeline-node"><strong>현행 한계</strong><small><b>문제</b> 대표자 인터뷰와 회의록 의존으로 암묵 요구·충돌 누락</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>교차 도출</strong><small><b>대안</b> 역할별 인터뷰 · 관찰 · 프로토타입 증거 결합</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>도출 게이트</strong><small><b>판정</b> 출처·목적·가정·확인 상태와 갈등 소유자 완비</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>실행 결과</strong><small><b>효과</b> 합의 요구 확보 · 명세와 추적의 신뢰 가능한 입력 제공</small></div>
</div>

## 1교시 10점 답안 발췌

- 정의: **Requirements Elicitation(요구사항 도출)**은 **이해관계자**와 운영 환경에서 **요구·제약·가정**을 발견해 요구 후보로 구조화하는 활동
- 목적: 표현된 요청과 실제 업무의 간극 식별 → 누락·오해·충돌을 줄인 요구 확보
- 핵심 흐름: 정보원·범위 식별 → 인터뷰·JAD·관찰·프로토타이핑 조합 → 재진술·충돌 조정·확인
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

- [요구공학(요구사항 유형 포함)](./040_requirements_engineering/)
- [요구사항 명세(SRS·IEEE 830·명세 품질 특성)](./054_requirements_specification/)
- [요구사항 추적표(Requirement Traceability Matrix)](./102_requirement_traceability_matrix/)
- [Agile 방법론](./119_agile_methodology/)
