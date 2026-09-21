---
title: "기술수용모델(TAM)"
author: "Antigravity"
date: "2026-09-22T08:20:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "Gemini 3.8 Flash"
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

## Ⅱ. TAM 인과구조 및 변화관리 매핑

> PEOU는 직접 경로뿐 아니라 PU를 높이는 경로로도 수용 의도에 영향을 줌

### 1. TAM 상세 인과 메커니즘 및 피드백 루프

```xml
<svg-diagram>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="220" style="background:var(--sl-color-bg-sidebar);border:1px solid var(--sl-color-hairline);border-radius:8px;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--sl-color-text-accent)"/>
    </marker>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#3b82f6"/>
    </marker>
  </defs>

  <!-- Title -->
  <text x="15" y="24" fill="var(--sl-color-text)" font-size="13" font-weight="bold">TAM 인과구조 및 조직 변화관리 연계도</text>

  <!-- External Variables -->
  <g transform="translate(15, 65)">
    <rect x="0" y="0" width="95" height="90" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="6"/>
    <text x="47" y="25" fill="var(--sl-color-text-accent)" font-size="10" font-weight="bold" text-anchor="middle">외부 변수</text>
    <text x="47" y="45" fill="var(--sl-color-text)" font-size="9" text-anchor="middle">• 시스템 품질</text>
    <text x="47" y="60" fill="var(--sl-color-text)" font-size="9" text-anchor="middle">• 교육/훈련 지원</text>
    <text x="47" y="75" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">• 최고경영진 의지</text>
  </g>

  <!-- PEOU (Top) -->
  <g transform="translate(145, 45)">
    <rect x="0" y="0" width="105" height="55" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="6"/>
    <text x="52" y="22" fill="var(--sl-color-text-accent)" font-size="10" font-weight="bold" text-anchor="middle">PEOU (용이성)</text>
    <text x="52" y="38" fill="var(--sl-color-text)" font-size="9" text-anchor="middle">"배우기 쉽다"</text>
    <text x="52" y="49" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">UI/UX 직관성</text>
  </g>

  <!-- PU (Bottom) -->
  <g transform="translate(145, 120)">
    <rect x="0" y="0" width="105" height="55" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="6"/>
    <text x="52" y="22" fill="#ef4444" font-size="10" font-weight="bold" text-anchor="middle">PU (유용성)</text>
    <text x="52" y="38" fill="var(--sl-color-text)" font-size="9" text-anchor="middle">"업무성과 향상"</text>
    <text x="52" y="49" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">생산성/시간절감</text>
  </g>

  <!-- Attitude (A) -->
  <g transform="translate(285, 80)">
    <rect x="0" y="0" width="95" height="60" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="6"/>
    <text x="47" y="24" fill="var(--sl-color-text)" font-size="10" font-weight="bold" text-anchor="middle">태도 (Attitude)</text>
    <text x="47" y="42" fill="var(--sl-color-text-muted)" font-size="9" text-anchor="middle">긍정적/부정적</text>
    <text x="47" y="53" fill="var(--sl-color-text-muted)" font-size="8" text-anchor="middle">심리적 선호도</text>
  </g>

  <!-- Intention (BI) & Actual Use (AU) -->
  <g transform="translate(415, 45)">
    <rect x="0" y="0" width="90" height="55" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" rx="6"/>
    <text x="45" y="24" fill="var(--sl-color-text-accent)" font-size="10" font-weight="bold" text-anchor="middle">BI (이용의도)</text>
    <text x="45" y="42" fill="var(--sl-color-text-muted)" font-size="9" text-anchor="middle">사용 계획 수립</text>
  </g>

  <g transform="translate(415, 120)">
    <rect x="0" y="0" width="90" height="55" fill="var(--sl-color-bg)" stroke="#10b981" stroke-width="2" rx="6"/>
    <text x="45" y="24" fill="#10b981" font-size="10" font-weight="bold" text-anchor="middle">Actual Use</text>
    <text x="45" y="42" fill="var(--sl-color-text)" font-size="9" text-anchor="middle">실제 지속 사용</text>
  </g>

  <!-- Connecting Arrows -->
  <!-- Ext -> PEOU -->
  <path d="M 110 95 L 140 75" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- Ext -> PU -->
  <path d="M 110 125 L 140 145" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- PEOU -> PU (Core Path!) -->
  <path d="M 197 100 L 197 115" fill="none" stroke="#ef4444" stroke-width="2" marker-end="url(#arrow)"/>
  <!-- PEOU -> Attitude -->
  <path d="M 250 75 L 280 95" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- PU -> Attitude -->
  <path d="M 250 145 L 280 125" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- PU -> BI (Direct link) -->
  <path d="M 250 155 C 340 185 380 90 410 75" fill="none" stroke="#3b82f6" stroke-width="1.8" stroke-dasharray="3,3" marker-end="url(#arrow-blue)"/>
  <!-- Attitude -> BI -->
  <path d="M 380 100 L 410 80" fill="none" stroke="var(--sl-color-text-accent)" stroke-width="1.5" marker-end="url(#arrow)"/>
  <!-- BI -> Actual Use -->
  <path d="M 460 100 L 460 115" fill="none" stroke="#10b981" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Note -->
  <text x="15" y="198" fill="var(--sl-color-text-muted)" font-size="9">※ PEOU → PU 간접 경로 및 PU → BI 직접 경로(파란점선)가 신기술 도입 시 강력한 결정요인으로 작동함</text>
</svg>
</svg-diagram>
```

### 2. 인과단계별 분석 및 개선방안

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

## Ⅲ. TAM vs UTAUT 비교

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

## Ⅴ. 다차원 수용성 검증을 위한 기술사적 제언

> 사용 빈도는 수용의 결과일 뿐 가치의 증거가 아님. PU·PEOU 개선이 업무성과로 이어지는지 함께 검증해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 사용자의 '사용 의도(BI)' 설문은 사회적 바람직성 편향이 개입하기 쉬움. 따라서 정량적 시스템 로그(DAU, MAU, 세션 유지시간, 주요 기능 사용률)와 업무 KPI 개선액을 결합한 객관적 증거 중심의 변화관리가 필수적임.
- 나라면: 파일럿 단계에서 설문·로그·업무성과를 삼각 측정(Triangulation)하고, 수용성 Quality Gate를 통과한 부서부터 단계적으로 전사 확산하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 인지된 유용성(PU) 및 용이성(PEOU) 지수, 실제 사용 로그(접속률/기능도달률) 및 업무 KPI 달성도 판정
- **대응 방안**: 사용자 중심 UX 리디자인, 현업 챔피언 중심의 단계별 온보딩 교육 및 촉진조건(기술지원 핫라인) 마련
- **검증 체계**: 설문조사–시스템 로그–업무 성과 간 삼각 검증(Triangulation), 도입 전·중·후 3단계 시계열 추적
- **기대 효과**: 막대한 SI/ERP 투자 후 방치되는 사장화(Shelfware) 리스크 방지 및 디지털 전환 투자 대비 가치(ROI) 극대화

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

- 이전 토픽: [적정 사업기간·과업심의](./091_public_sw_cost_and_scope_change_criteria.md)
- 연관 토픽: [디자인 씽킹](./047_design_thinking.md), [TAM-SAM-SOM](./089_tam_sam_som.md)
- 다음 토픽: [SW 사업 하도급 구조](./097_software_industry_subcontracting_structure.md)

