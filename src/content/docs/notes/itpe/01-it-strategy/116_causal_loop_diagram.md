---
title: "인과루프다이어그램(Causal Loop Diagram)"
author: "OpenAI Codex"
date: "2026-09-22T12:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 시스템 사고와 인과루프다이어그램으로 이어지는 위치">
  <span>IT 전략·관리</span>
  <span>시스템 사고</span>
  <strong>CLD</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 변수 간 인과관계를 닫힌 **Feedback Loop**로 연결해 시스템 행동의 구조적 원인을 설명
- 메커니즘: 변수 → 극성 링크 → 강화·조절 루프 → Delay → Leverage Point
- 산출물: **CLD(Causal Loop Diagram)** · 루프 가설 · 개입·검증 계획

<div class="itpe-svg-map">
<svg viewBox="0 0 760 470" role="img" aria-label="강화 루프와 조절 루프의 인과 구조와 시간 지연">
  <defs>
    <marker id="cld-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link" /></marker>
  </defs>
  <text x="195" y="36" text-anchor="middle" class="itpe-svg-title">강화 루프 R</text>
  <circle cx="195" cy="190" r="54" class="itpe-svg-node is-current" />
  <text x="195" y="184" text-anchor="middle" class="itpe-svg-title">재작업</text>
  <text x="195" y="207" text-anchor="middle" class="itpe-svg-sub">R</text>
  <rect x="65" y="65" width="150" height="64" rx="14" class="itpe-svg-node" />
  <text x="140" y="92" text-anchor="middle" class="itpe-svg-title">결함</text>
  <text x="140" y="114" text-anchor="middle" class="itpe-svg-sub">증가</text>
  <rect x="180" y="310" width="160" height="64" rx="14" class="itpe-svg-node" />
  <text x="260" y="337" text-anchor="middle" class="itpe-svg-title">일정 압박</text>
  <text x="260" y="359" text-anchor="middle" class="itpe-svg-sub">증가</text>
  <path d="M187 128 C260 105 310 145 258 185" class="itpe-svg-link" marker-end="url(#cld-arrow)" />
  <text x="270" y="122" class="itpe-svg-label">+</text>
  <path d="M235 235 C310 255 315 292 286 307" class="itpe-svg-link" marker-end="url(#cld-arrow)" />
  <text x="310" y="266" class="itpe-svg-label">+</text>
  <path d="M202 340 C70 335 35 170 91 124" class="itpe-svg-link" marker-end="url(#cld-arrow)" />
  <text x="54" y="257" class="itpe-svg-label">+</text>

  <text x="565" y="36" text-anchor="middle" class="itpe-svg-title">조절 루프 B</text>
  <circle cx="565" cy="190" r="54" class="itpe-svg-node is-current" />
  <text x="565" y="184" text-anchor="middle" class="itpe-svg-title">품질 Gap</text>
  <text x="565" y="207" text-anchor="middle" class="itpe-svg-sub">B</text>
  <rect x="420" y="65" width="170" height="64" rx="14" class="itpe-svg-node" />
  <text x="505" y="92" text-anchor="middle" class="itpe-svg-title">테스트 강화</text>
  <text x="505" y="114" text-anchor="middle" class="itpe-svg-sub">대응</text>
  <rect x="535" y="310" width="170" height="64" rx="14" class="itpe-svg-node" />
  <text x="620" y="337" text-anchor="middle" class="itpe-svg-title">잔존 결함</text>
  <text x="620" y="359" text-anchor="middle" class="itpe-svg-sub">감소</text>
  <path d="M540 142 L540 132" class="itpe-svg-link" marker-end="url(#cld-arrow)" />
  <text x="555" y="139" class="itpe-svg-label">+</text>
  <path d="M470 129 C395 210 450 300 535 330" class="itpe-svg-link" marker-end="url(#cld-arrow)" />
  <text x="416" y="238" class="itpe-svg-label">− · Delay ║</text>
  <path d="M535 340 C470 330 468 250 520 220" class="itpe-svg-link" marker-end="url(#cld-arrow)" />
  <text x="478" y="300" class="itpe-svg-label">+</text>
  <text x="380" y="435" text-anchor="middle" class="itpe-svg-title">극성은 상관관계가 아니라 원인 변화에 따른 결과의 방향</text>
</svg>
</div>

<details>
<summary>핵심 용어</summary>

- **CLD(Causal Loop Diagram)**: 변수·인과 링크·극성·Feedback Loop를 표현하는 정성적 시스템 모델
- **R(Reinforcing Loop)**: 초기 변화를 같은 방향으로 증폭하는 강화 루프
- **B(Balancing Loop)**: 초기 변화에 맞서 목표·균형으로 접근하는 조절 루프
- **Delay**: 원인 변화와 결과 발현 사이의 시간 지연
- **BOT(Behavior Over Time)**: 주요 변수의 시간에 따른 변화 패턴
- **Leverage Point**: 작은 개입으로 시스템 행동을 크게 바꾸는 구조적 지점

</details>

## 예상문제

> **(미출제 예상·25점)** CLD의 구성요소와 작성절차를 설명하고, 강화·조절 루프의 판정방법·활용 한계·IT 프로젝트 적용방안을 제시하시오.

## Ⅰ. CLD의 개요

> 사건을 나열하지 않고 사건을 반복 생성하는 Feedback 구조를 가설로 표현한다.

- 정의: 시스템 변수의 **인과관계·극성·Feedback Loop·Delay**를 표현하는 정성적 모델
- 목적: 순환 인과구조 이해 · 의도하지 않은 정책효과 탐색 · Leverage Point 도출

## Ⅱ. 구성요소·작성절차

> 좋은 CLD는 변수명·극성·루프 경계가 명확하고 관찰 자료로 검증 가능한 가설이어야 한다.

### 1. 구성요소

| 요소 | 표기 | 판정 |
|---|---|---|
| 변수 | 명사구 | 시간에 따라 증감 가능 |
| 인과 링크 | →, +/− | 같은 방향 `+` · 반대 방향 `−` |
| Feedback Loop | R/B | 닫힌 경로의 전체 극성 |
| Delay | ║ | 효과 발현 시차 |

### 2. 작성절차

<div class="itpe-pipeline is-vertical" role="img" aria-label="인과루프다이어그램 작성절차와 산출물">
  <div class="itpe-pipeline-node"><strong>① 문제·경계 정의</strong><div class="itpe-step-detail"><strong>활동</strong><span>현상·기간·이해관계자 범위 설정</span></div><div class="itpe-step-detail"><strong>산출</strong><span>문제 문장 · 모델 경계</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>② BOT·변수 도출</strong><div class="itpe-step-detail"><strong>활동</strong><span>관찰 패턴과 증감 가능한 변수 식별</span></div><div class="itpe-step-detail"><strong>산출</strong><span>BOT · 변수 목록</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>③ 링크·극성 설정</strong><div class="itpe-step-detail"><strong>활동</strong><span>다른 조건이 같을 때의 변화 방향 판정</span></div><div class="itpe-step-detail"><strong>산출</strong><span>인과 링크 · 근거</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>④ 루프·Delay 식별</strong><div class="itpe-step-detail"><strong>활동</strong><span>폐쇄 경로 극성·시차 판정</span></div><div class="itpe-step-detail"><strong>산출</strong><span>R/B Loop · Delay</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>⑤ 검증·개입 설계</strong><div class="itpe-step-detail"><strong>활동</strong><span>전문가·데이터로 인과 가설 검토</span></div><div class="itpe-step-detail"><strong>산출</strong><span>Leverage Point · 검증계획</span></div></div>
</div>

## Ⅲ. 강화·조절 루프 판정

> 링크 수가 아니라 폐쇄 루프 안의 음의 링크 개수로 전체 극성을 판정한다.

| 기준 | 강화 루프 R | 조절 루프 B |
|---|---|---|
| 음의 링크 | 0개 또는 짝수 | 홀수 |
| 행동 | 변화 증폭 | 변화 억제·목표 추구 |
| 형태 | 성장·쇠퇴 | 수렴·진동 가능 |

### IT 프로젝트 예시

```text
R1 재작업 악순환
결함 +→ 재작업 +→ 일정 압박 +→ 결함

B1 품질 조절
품질 Gap +→ 테스트 강화 −→ 잔존 결함 +→ 품질 Gap
                         ║ Delay
```

## Ⅳ. 문제점·대응책

> CLD는 인과 가설을 공유하는 도구이지 관계의 진실이나 정량 예측을 자동 보장하지 않는다.

| 위험 | 대책 | 효과 |
|---|---|---|
| 상관관계를 인과로 오인 | 데이터·현업 인터뷰 교차검증 | 인과 근거 강화 |
| 변수·경계 과다 | 핵심 루프별 분리 · 경계 명시 | 가독성 확보 |
| Delay 누락 | 정책효과 발현시점 별도 표시 | 과잉 대응 방지 |
| 정량 예측으로 오용 | Stock·Flow 모델로 확장 | 시뮬레이션 가능 |

## Ⅴ. 결론·기술사적 제언

> CLD는 개입 후보를 찾고 Stock·Flow 모델과 실증검증으로 넘기는 탐색도구로 사용해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: CLD의 가치는 화살표 수가 아니라 반복되는 문제를 만드는 폐쇄 루프와 Delay를 드러내는 데 있다.
- 나라면: 악순환을 찾은 뒤 즉시 처방하지 않고 인과 근거·시간지연·부작용 루프를 먼저 검증하여 개입의 역효과를 줄이겠다.

### 실전 답안용 기술사적 제언

<div class="itpe-svg-map">
<svg viewBox="0 0 760 500" role="img" aria-label="인과루프 가설에서 정량 검증과 정책 실행으로 이어지는 품질 게이트">
  <defs><marker id="cld-control-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link" /></marker></defs>
  <rect x="195" y="20" width="370" height="70" rx="14" class="itpe-svg-node" />
  <text x="380" y="48" text-anchor="middle" class="itpe-svg-title">CLD 인과 가설</text>
  <text x="380" y="72" text-anchor="middle" class="itpe-svg-sub">R/B Loop · Delay · Leverage 후보</text>
  <path d="M380 90 L380 130" class="itpe-svg-link" marker-end="url(#cld-control-arrow)" />
  <rect x="195" y="140" width="370" height="70" rx="14" class="itpe-svg-node" />
  <text x="380" y="168" text-anchor="middle" class="itpe-svg-title">인과 근거 검증</text>
  <text x="380" y="192" text-anchor="middle" class="itpe-svg-sub">데이터 · 현업 인터뷰 · 반례</text>
  <path d="M380 210 L380 250" class="itpe-svg-link" marker-end="url(#cld-control-arrow)" />
  <rect x="195" y="260" width="370" height="70" rx="14" class="itpe-svg-node is-current" />
  <text x="380" y="288" text-anchor="middle" class="itpe-svg-title">Model Quality Gate</text>
  <text x="380" y="312" text-anchor="middle" class="itpe-svg-sub">경계 · 극성 · Delay · 반례 판정</text>
  <path d="M380 330 L380 370" class="itpe-svg-link" marker-end="url(#cld-control-arrow)" />
  <rect x="65" y="380" width="285" height="80" rx="14" class="itpe-svg-node" />
  <text x="207" y="408" text-anchor="middle" class="itpe-svg-title">정성 판단 충분</text>
  <text x="207" y="435" text-anchor="middle" class="itpe-svg-sub">소규모 실험 · 모니터링</text>
  <rect x="410" y="380" width="285" height="80" rx="14" class="itpe-svg-node" />
  <text x="552" y="408" text-anchor="middle" class="itpe-svg-title">정량 예측 필요</text>
  <text x="552" y="435" text-anchor="middle" class="itpe-svg-sub">Stock·Flow 모델 · 시뮬레이션</text>
  <path d="M380 355 L207 355 L207 380" class="itpe-svg-link" marker-end="url(#cld-control-arrow)" />
  <path d="M380 355 L552 355 L552 380" class="itpe-svg-link" marker-end="url(#cld-control-arrow)" />
</svg>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 변수 간 **인과관계·극성·Feedback Loop·Delay**를 표현하는 정성적 시스템 모델
- 목적: 반복 문제의 구조적 원인과 Leverage Point 식별

### 2. 4대 구성요소

| 요소 | 표기 | 의미 |
|---|---|---|
| 변수 | 명사구 | 증감 가능한 상태 |
| 인과 링크 | →, +/− | 변화 방향 |
| Feedback Loop | R/B | 강화·조절 |
| Delay | ║ | 효과 발현 시차 |

### 3. 판정·한계

- 음의 링크 0개·짝수: R · 홀수: B
- CLD: 정성적 인과 가설 · Stock·Flow: 정량 시뮬레이션

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [MIT OpenCourseWare, Introduction to Project Dynamics](https://ocw.mit.edu/courses/esd-36-system-project-management-fall-2012/800ceb204ef03177b61e1288533446c1_MITESD_36F12_Lec06.pdf)
- [MIT OpenCourseWare, Introduction to Engineering Systems — Causal Loop Diagrams](https://ocw.mit.edu/courses/esd-00-introduction-to-engineering-systems-spring-2011/816df198baedb3b544ab4148ce86927d_MITESD_00S11_lec02.pdf)

## 학습 체크

- [ ] Ⅰ: CLD의 정의·목적을 두 줄로 재현할 수 있는가?
- [ ] Ⅱ: 변수·링크·루프·Delay의 표기와 판정 기준을 설명할 수 있는가?
- [ ] Ⅱ: 5단계 활동·산출물을 연결할 수 있는가?
- [ ] Ⅲ: 음의 링크 개수로 R/B를 판정하고 IT 예시를 작도할 수 있는가?
- [ ] Ⅳ~Ⅴ: CLD의 4대 위험과 정량 모델 전환 기준을 제시할 수 있는가?

## 연결 토픽

- 이전: [114. 개방형 혁신](./114_open_innovation/)
- 관련: [112. CCPM·TOC](./112_critical_chain_toc/) · [040. 부정적 위험 대응](./040_negative_risk_response_strategy/)
- 다음: [2과목 SW 공학](../02-software-engineering/)
