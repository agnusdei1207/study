---
title: "기술수용모델(TAM)"
author: "OpenAI Codex"
date: "2026-09-22T08:20:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "B"
extra:
  model: "GPT-5"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 변화관리를 거쳐 기술수용모델로 이어지는 위치">
  <span>IT 전략·관리</span><span>변화관리·사용자 수용</span><strong>TAM</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 기술을 유용하고 쉽게 느끼는지가 수용 의도를 형성
- **메커니즘**: 외부 변수 → PU·PEOU → 태도·BI → 실제 사용
- **활용**: 수용 저해요인 진단 → UX·업무 적합성·조직 지원 개선

<div class="itpe-svg-map">
<svg viewBox="0 0 760 500" role="img" aria-label="기술수용모델의 인과구조">
  <defs><marker id="tam-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link"></path></marker></defs>
  <rect x="35" y="205" width="150" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="110" y="240" text-anchor="middle" class="itpe-svg-title">외부 변수</text><text x="110" y="270" text-anchor="middle" class="itpe-svg-sub">품질·교육·지원</text>
  <rect x="245" y="65" width="180" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="335" y="100" text-anchor="middle" class="itpe-svg-title">PEOU</text><text x="335" y="130" text-anchor="middle" class="itpe-svg-sub">인지된 용이성</text>
  <rect x="245" y="345" width="180" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="335" y="380" text-anchor="middle" class="itpe-svg-title">PU</text><text x="335" y="410" text-anchor="middle" class="itpe-svg-sub">인지된 유용성</text>
  <rect x="485" y="205" width="110" height="90" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="540" y="240" text-anchor="middle" class="itpe-svg-title">태도</text><text x="540" y="270" text-anchor="middle" class="itpe-svg-sub">Attitude</text>
  <rect x="635" y="95" width="90" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="680" y="130" text-anchor="middle" class="itpe-svg-title">BI</text><text x="680" y="160" text-anchor="middle" class="itpe-svg-sub">사용 의도</text>
  <rect x="635" y="335" width="90" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="680" y="370" text-anchor="middle" class="itpe-svg-title">사용</text><text x="680" y="400" text-anchor="middle" class="itpe-svg-sub">Actual Use</text>
  <path d="M185 225 L245 135" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
  <path d="M185 275 L245 365" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
  <path d="M335 155 L335 345" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
  <path d="M425 110 C500 110 500 205 500 205" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
  <path d="M425 390 C500 390 500 295 500 295" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
  <path d="M595 235 C625 210 640 175 650 165" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
  <path d="M425 390 C555 470 620 220 650 175" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
  <path d="M680 185 L680 335" class="itpe-svg-link" marker-end="url(#tam-arrow)"></path>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **TAM(Technology Acceptance Model)**: 기술 수용을 신념·태도·의도·사용 관계로 설명하는 모델
- **PU(Perceived Usefulness)**: 사용이 직무 성과를 높인다고 믿는 정도
- **PEOU(Perceived Ease of Use)**: 사용에 큰 노력이 들지 않는다고 믿는 정도
- **BI(Behavioral Intention)**: 기술을 사용하려는 행동 의도
- **UTAUT(Unified Theory of Acceptance and Use of Technology)**: 성과기대·노력기대·사회적 영향·촉진조건을 통합한 수용 모델

</details>

## 예상문제

> **(미출제 예상·25점)** 기술수용모델의 개념과 인과구조를 설명하고, 한계와 조직의 신기술 수용 촉진방안을 제시하시오.

## Ⅰ. TAM 개요

> 기술 자체의 우수성보다 사용자가 느끼는 유용성·용이성이 수용 행동을 좌우함

- **정의**: 정보기술 수용을 <span class="itpe-keyword"><strong>PU</strong></span>와 <span class="itpe-keyword"><strong>PEOU</strong></span> 중심의 신념·태도·의도·사용 관계로 설명하는 모델
- **목적**: 사용자 수용 저해요인 진단·실제 사용 촉진

## Ⅱ. TAM 인과구조·적용

> PEOU는 직접 경로뿐 아니라 PU를 높이는 경로로도 수용 의도에 영향을 줌

| 단계 | 분석 | 개선 |
|---|---|---|
| 외부 변수 | 시스템 품질·교육·지원 | UX·성능·지원체계 |
| PEOU | 학습·조작 부담 | 절차 단순화·온보딩 |
| PU | 업무 성과 기여 | 업무 연계·성과 가시화 |
| 태도·BI | 선호·사용 의도 | 파일럿·사용자 참여 |
| 실제 사용 | 빈도·기능·지속성 | 로그·인터뷰 기반 개선 |

:::note[모델 해석]
원형 TAM은 태도를 포함하며, 후속 연구·실무 모형은 PU에서 BI로 가는 직접 경로를 강조하거나 태도를 생략하기도 함. 답안에서는 적용한 경로를 명확히 표시함.
:::

## Ⅲ. TAM·UTAUT 비교

> TAM은 핵심 신념을 간결하게 진단하고, UTAUT는 조직·사회적 조건까지 넓혀 설명함

| 기준 | TAM | UTAUT |
|---|---|---|
| 중심 | PU·PEOU | 성과기대·노력기대·사회적 영향·촉진조건 |
| 강점 | 간결한 인과구조 | 조직 맥락·조절요인 반영 |
| 적용 | 초기 수용성 진단 | 전사 확산·정착 분석 |

## Ⅳ. 문제점·대응책

> 설문 의도만 측정하면 실제 사용과 업무성과를 과대평가할 수 있음

| 위험 | 대책 | 효과 |
|---|---|---|
| 자기보고 편향 | 설문·사용 로그 교차검증 | 의도와 행동 구분 |
| 조직 맥락 누락 | 사회적 영향·지원조건 보완 | 현장 설명력 강화 |
| 단기 수용만 측정 | 도입 전·후 반복 측정 | 수용 변화 추적 |
| 사용량을 성과로 오인 | 업무 KPI·품질과 연계 | 가치 실현 검증 |

## Ⅴ. 결론·기술사적 제언

> **[핵심 통찰]** 사용 빈도는 수용의 결과일 뿐 가치의 증거가 아님. PU·PEOU 개선이 업무성과로 이어지는지 함께 검증해야 함.

> **나라면** 파일럿에서 설문·사용 로그·업무성과를 함께 측정하고, 저해요인별 개선 후 재검증하는 수용성 Quality Gate를 운영하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="TAM 기반 수용성 품질 게이트">
  <div class="itpe-flow-node"><strong>수용성 진단</strong><div class="itpe-step-detail"><strong>측정</strong><span>PU·PEOU·BI</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>행동 검증</strong><div class="itpe-step-detail"><strong>증거</strong><span>사용 로그·현업 인터뷰</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>가치 검증</strong><div class="itpe-step-detail"><strong>판정</strong><span>업무 KPI·품질 개선</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>Quality Gate</strong><div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>통과</strong><span>확산·정착</span></div><div class="itpe-flow-branch"><strong>미통과</strong><span>UX·업무·지원 개선</span></div></div></div>
</div>

## 1교시 10점 답안 발췌

- **정의**: 정보기술 수용을 PU·PEOU 중심의 신념·태도·의도·사용 관계로 설명하는 모델
- **목적**: 사용자 수용 저해요인 진단·실제 사용 촉진

| 요소 | 의미 |
|---|---|
| PU | 업무 성과에 도움이 되는가 |
| PEOU | 쉽게 배워 사용할 수 있는가 |
| BI·사용 | 사용할 의도와 실제 행동 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [Davis, Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology](https://doi.org/10.2307/249008)
- [Davis·Bagozzi·Warshaw, User Acceptance of Computer Technology](https://doi.org/10.1287/mnsc.35.8.982)
- [Venkatesh et al., User Acceptance of Information Technology: Toward a Unified View](https://doi.org/10.2307/30036540)

## 학습 체크

- [ ] Ⅰ: TAM의 정의·목적을 PU·PEOU로 설명할 수 있는가?
- [ ] Ⅱ: 외부 변수에서 실제 사용까지의 인과경로를 그릴 수 있는가?
- [ ] Ⅲ: TAM과 UTAUT의 적용 차이를 비교할 수 있는가?
- [ ] Ⅳ: 설문 편향·조직 맥락·성과 오인의 대책을 제시할 수 있는가?
- [ ] Ⅴ: 설문·로그·업무성과를 결합한 검증안을 제시할 수 있는가?

## 연결 토픽

- 이전: [091. 적정 사업기간·과업심의](./091_public_sw_cost_and_scope_change_criteria/)
- 관련: [047. 디자인 씽킹](./047_design_thinking/) · [089. TAM·SAM·SOM](./089_tam_sam_som/)
- 다음: [097. SW 사업 하도급 구조](./097_software_industry_subcontracting_structure/)
