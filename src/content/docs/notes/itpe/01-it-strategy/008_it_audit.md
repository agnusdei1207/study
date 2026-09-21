---
title: "정보시스템 감리"
author: "Antigravity"
date: "2026-09-21T12:40:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="정보 전략과 관리에서 사업 통제를 거쳐 정보시스템 감리로 이어지는 지식 위치">
  <span>정보 전략·관리</span>
  <span>사업 품질·독립 통제</span>
  <strong>정보시스템 감리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **정보시스템 감리**는 발주자·사업자와 독립된 제3자가 공공 정보시스템의 구축·운영을 기준에 맞춰 점검하고 문제를 실제로 고치게 만드는 법정 통제
- 메커니즘: 법정 대상 판정 → 독립 감리법인 선정 → 계획·현장감리 → 감리보고서 → 사업자 개선 반영·조치 확인
- 산출물: 감리계획서 · 감리보고서 · 시정조치 결과와 증적

<div class="itpe-pipeline is-vertical" role="img" aria-label="발주기관 감리법인 사업자가 감리 결과를 개선으로 닫는 흐름">
  <div class="itpe-pipeline-node"><strong>발주자</strong><div class="itpe-step-detail"><strong>책임</strong><span>감리 발주 · 업무 개입·간섭 금지 · 결과 반영 요구</span><strong>산출</strong><span>감리계약 · 대상자료</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current"><span class="itpe-keyword"><strong>감리법인</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>계획 · 현장감리 · 개선사항 도출</span><strong>산출</strong><span>감리계획서 · 감리보고서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>사업자</strong><div class="itpe-step-detail"><strong>책임</strong><span>감리결과 반영 · 조치 증적 제출</span><strong>산출</strong><span>시정조치 결과</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>조치 확인</strong></span><div class="itpe-step-detail"><strong>판정</strong><span>개선사항 반영·증적 충족 여부</span><strong>효과</strong><span>감리결과의 실제 반영 확인</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- **정보시스템 감리**: 독립된 제3자가 정보시스템 구축·운영을 종합 점검하고 문제를 개선하도록 하는 제도
- **감리법인**: 「전자정부법」 제58조에 따라 등록하고 감리원이 감리업무를 수행하는 법인
- **상주감리**: 현장 상주 또는 주기적 투입으로 위험요소·산출물 검토·자문을 수행하는 감리
- **현장감리**: 계획한 점검항목에 따라 자료검토·인터뷰·시험 등 증거를 확보하는 감리 수행 구간
- **감리 검사기준서**: 점검항목·검토항목·검증방법을 사업 특성에 맞게 구체화한 현장감리 작업 기준

</details>

## 예상문제

> 정보시스템 구축 사업의 성공적인 수행을 위해 정보시스템 감리와 PMO(전자정부사업관리 위탁)를 활용하여 사업관리를 수행하고 있다. 이와 관련하여 다음을 설명하시오. 가. 정보시스템 감리의 법적 근거 나. PMO의 정의와 역할 다. PMO 대상 사업의 범위 라. PMO와 상주감리의 비교 (제136회 정보관리기술사 2교시)

## Ⅰ. 독립적 제3자 통제, 정보시스템 감리

> 정보시스템 감리는 발주자의 관리업무를 대신하는 조직이 아니라 **독립된 제3자** 점검이며, 성패는 지적 수보다 **감리결과**의 실제 반영으로 판정함

- 정의: **정보시스템 감리**는 발주자·사업자 등의 이해관계로부터 독립된 자가 정보시스템의 **효율성·안전성**을 위해 구축·운영을 종합 점검하고 문제점을 개선하도록 하는 활동
- 목적: 사업 위험 조기 발견, 결함 잔존·재작업 감소

## Ⅱ. 전자정부법령과 감리기준의 통제 구조

> 법은 감리 대상·독립성·**감리결과 반영 의무**를 정하고, 고시 「**정보시스템 감리기준**」은 감리의 업무범위·절차·준수사항을 구체화하여 점검의 실효성을 닫음

<div class="itpe-svg-map">
<svg viewBox="0 0 520 576" role="img" aria-label="전자정부법이 시행령에 위임하고 정보시스템 감리기준이 이를 구체화하는 3계층 법령 통제 구조와 각 계층의 통제 항목 트리">
  <defs><marker id="arrow-audit-law" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <rect class="itpe-svg-node is-current" x="20" y="8" width="470" height="44" rx="12" />
  <text class="itpe-svg-title" x="255" y="30">「전자정부법」 제57조~제59조 · 통제 4</text>
  <path class="itpe-svg-link" d="M45 52 V205 M45 79 H75 M45 121 H75 M45 163 H75 M45 205 H75" />
  <rect class="itpe-svg-node" x="75" y="62" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="79">감리 실시 대상 확정</text>
  <rect class="itpe-svg-node" x="75" y="104" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="121">감리업무 개입·간섭 금지</text>
  <rect class="itpe-svg-node" x="75" y="146" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="163">감리결과 사업 반영 의무</text>
  <rect class="itpe-svg-node" x="75" y="188" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="205">감리법인 등록 · 성실 의무</text>
  <path class="itpe-svg-link" d="M465 52 V232" marker-end="url(#arrow-audit-law)" />
  <text class="itpe-svg-label" x="437" y="140">위임</text>
  <rect class="itpe-svg-node" x="20" y="238" width="470" height="44" rx="12" />
  <text class="itpe-svg-title" x="255" y="260">같은 법 시행령 제71조·제72조 · 통제 2</text>
  <path class="itpe-svg-link" d="M45 282 V351 M45 309 H75 M45 351 H75" />
  <rect class="itpe-svg-node" x="75" y="292" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="309">의무감리 대상 판정</text>
  <rect class="itpe-svg-node" x="75" y="334" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="351">감리법인 업무범위 · 절차</text>
  <path class="itpe-svg-link" d="M465 282 V384" marker-end="url(#arrow-audit-law)" />
  <text class="itpe-svg-label" x="433" y="330">구체화</text>
  <rect class="itpe-svg-node" x="20" y="390" width="470" height="44" rx="12" />
  <text class="itpe-svg-title" x="255" y="412">「정보시스템 감리기준」 · 통제 3</text>
  <path class="itpe-svg-link" d="M45 434 V545 M45 461 H75 M45 503 H75 M45 545 H75" />
  <rect class="itpe-svg-node" x="75" y="444" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="461">감리 업무범위 규정</text>
  <rect class="itpe-svg-node" x="75" y="486" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="503">계획 · 현장감리 · 보고 절차</text>
  <rect class="itpe-svg-node" x="75" y="528" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="545">감리원 준수사항</text>
</svg>
</div>

- 적용관계: 「전자정부법」 제64조의2에 따라 전자정부사업관리를 위탁한 경우에도 모든 사업이 감리에서 제외되는 것은 아니며, 같은 법 **제57조제1항 단서**와 **시행령 제71조제2항**이 정한 사업만 **의무감리** 예외에 해당함
- 예외범위: 대국민·기관 공동사용 사업 중 사업비 1억 원 이상 5억 원 미만인 사업 · 사업기간 5개월 미만인 정보시스템 구축사업

## Ⅲ. 계약에서 조치 확인까지의 감리 수행체계

> 아래 흐름은 NIA 2022 감리 수행가이드를 압축한 대표 수행 흐름이며, 모든 사업에 동일한 공식 5단계 명칭을 강제하는 절차가 아님

<div class="itpe-pipeline is-vertical" role="img" aria-label="정보시스템 감리 수행 절차">
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>① 계약·계획</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>대상·범위·일정·감리원 편성</span><strong>산출</strong><span>감리계약 · 감리계획서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>② 착수·예비조사</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>사업 현황·산출물·위험 분석</span><strong>산출</strong><span>점검항목 · 검사기준서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>③ 현장감리</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>자료검토 · 인터뷰 · 시험 · 증거 확보</span><strong>산출</strong><span>감리 발견사항</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>④ 보고</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>발견사항 검토 · 개선사항 확정</span><strong>산출</strong><span>감리보고서</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>⑤ 조치 확인</strong></span><div class="itpe-step-detail"><strong>활동</strong><span>사업자 반영 결과·증적 재검토</span><strong>산출</strong><span>조치 확인 결과</span></div></div>
</div>

## Ⅳ. PMO와 상주감리의 역할 경계

> PMO는 발주기관의 사업관리·의사결정을 계속 지원하고, 상주감리는 독립된 관점에서 위험·산출물을 점검하므로 두 역할을 섞으면 **감리 독립성**이 약해짐

<div class="itpe-svg-map">
<svg viewBox="0 0 520 348" role="img" aria-label="발주기관이 PMO에 사업관리를 위탁하고 상주감리는 독립 위치에서 결과를 보고하며, 두 주체가 사업자를 각각 관리하고 점검하는 역할 경계">
  <defs><marker id="arrow-audit-role" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <rect class="itpe-svg-node" x="130" y="10" width="260" height="44" rx="12" />
  <text class="itpe-svg-title" x="260" y="32">발주기관 · 사업 책임</text>
  <path class="itpe-svg-link" d="M200 54 V92 H125 V126" marker-end="url(#arrow-audit-role)" />
  <text class="itpe-svg-label" x="163" y="80">위탁</text>
  <path class="itpe-svg-link" d="M395 130 V92 H320 V58" marker-end="url(#arrow-audit-role)" />
  <text class="itpe-svg-label" x="357" y="80">감리 결과 보고</text>
  <rect class="itpe-svg-node" x="15" y="130" width="220" height="70" rx="12" />
  <text class="itpe-svg-title" x="125" y="155">PMO</text>
  <text class="itpe-svg-sub" x="125" y="180">사업관리·의사결정 지원</text>
  <rect class="itpe-svg-node is-current" x="285" y="130" width="220" height="70" rx="12" />
  <text class="itpe-svg-title" x="395" y="155">상주감리</text>
  <text class="itpe-svg-sub" x="395" y="180">독립 점검 · 개선 권고</text>
  <path class="itpe-svg-link" d="M125 200 V270 H200 V286" marker-end="url(#arrow-audit-role)" />
  <text class="itpe-svg-label" x="163" y="258">일정·위험 관리</text>
  <path class="itpe-svg-link" d="M395 200 V270 H320 V286" marker-end="url(#arrow-audit-role)" />
  <text class="itpe-svg-label" x="357" y="258">산출물·위험 점검</text>
  <rect class="itpe-svg-node" x="130" y="290" width="260" height="44" rx="12" />
  <text class="itpe-svg-title" x="260" y="312">사업자 · 구축 수행</text>
</svg>
</div>

| 비교축 | **PMO(Project Management Office)** | **상주감리** |
|---|---|---|
| 목적 | 발주기관 사업관리·의사결정 지원 | 독립적 점검·개선 권고 |
| 업무 | 일정·위험·품질관리 · 보고·조정 | 위험요소·산출물 검토 · 자문 |
| 위치 | 발주기관 관리·감독 지원 | 발주자·사업자와 독립된 제3자 |

- 법적 적용: **전자정부사업관리 위탁**은 감리와 같은 제도가 아니며, 의무감리 제외 여부는 사업별로 「전자정부법」 제57조제1항 단서와 시행령 제71조제2항의 조건을 확인함

## Ⅴ. 검사기준서와 조치 증적의 확인 판정

> **검사기준서**가 계약·법령·기술기준과 연결되고 각 개선사항에 **조치 증적**이 대응해야 감리가 문서 검토를 넘어 실제 품질 통제로 작동함

<div class="itpe-flow-map" role="img" aria-label="감리 개선사항과 조치 증적의 확인 판정">
  <div class="itpe-flow-node"><strong>검증 대상</strong><div class="itpe-step-detail"><strong>대상</strong><span>검사기준서 · <span class="itpe-keyword"><strong>감리 발견사항</strong></span> · 시정조치 증적</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><span class="itpe-keyword"><strong>조치 확인 판정</strong></span><div class="itpe-step-detail"><strong>판정 질문</strong><span>개선사항별 반영 결과와 객관적 증거가 대응하는가</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass"><strong>통과</strong><span>조치 확인 · 결과 기록</span></div>
    <div class="itpe-flow-branch is-fail"><strong>미통과</strong><span>보완 요구 · 증거 재확인</span></div>
  </div>
</div>

## Ⅵ. 감리 실효성의 문제점·대응책

> 독립성 훼손·검사기준 부실·미조치 종결을 각각 책임 분리·근거 추적·증적 확인으로 통제해야 함

<div class="itpe-svg-map">
<svg viewBox="0 0 520 278" role="img" aria-label="감리 실효성을 지키는 독립 수행, 근거 추적, 조치 이행 3개 통제 지점이 확보 증거와 확정 개선사항을 주고받으며 이어지는 통제 체인">
  <defs><marker id="arrow-audit-risk" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <text class="itpe-svg-label" x="260" y="18">감리 실효성 통제 3</text>
  <rect class="itpe-svg-node" x="80" y="28" width="360" height="52" rx="12" />
  <text class="itpe-svg-title" x="260" y="48">독립 수행</text>
  <text class="itpe-svg-sub" x="260" y="68">감리업무 개입·간섭 차단</text>
  <path class="itpe-svg-link" d="M260 80 V118" marker-end="url(#arrow-audit-risk)" />
  <text class="itpe-svg-label" x="330" y="103">확보 증거</text>
  <rect class="itpe-svg-node" x="80" y="122" width="360" height="52" rx="12" />
  <text class="itpe-svg-title" x="260" y="142">근거 추적</text>
  <text class="itpe-svg-sub" x="260" y="162">검사기준 ↔ 발견사항 ↔ 증거</text>
  <path class="itpe-svg-link" d="M260 174 V212" marker-end="url(#arrow-audit-risk)" />
  <text class="itpe-svg-label" x="337" y="197">확정 개선사항</text>
  <rect class="itpe-svg-node is-current" x="80" y="216" width="360" height="52" rx="12" />
  <text class="itpe-svg-title" x="260" y="236">조치 이행</text>
  <text class="itpe-svg-sub" x="260" y="256">담당자 · 기한 · 조치 증적</text>
</svg>
</div>

| 위험 | 대책 | 효과 |
|---|---|---|
| 감리업무 개입 | **감리법인 독립성**·보고 경로 명시 | 점검 결과 왜곡 방지 |
| 형식적 점검 | **검사기준**·발견사항·증거 연결 | 누락·자의적 판정 감소 |
| 미조치 종결 | 개선사항별 담당자·기한·**증적** 확인 | 결함의 운영 전이 감소 |

## Ⅶ. 결론 — 증거 기반 조치 확인으로 닫는 감리

> **감리보고서** 작성이 종료점이 아니라 **개선사항**과 실제 시스템·산출물의 대응을 확인하는 것이 최종 품질 판정임

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 감리는 지적사항 목록을 만드는 일이 아니라 독립된 증거로 문제를 드러내고, 개선사항이 실제 산출물에 반영되었는지 확인하는 활동이다.
- `나라면`: 위험이 큰 점검항목부터 계약 근거·검증방법·발견 증거·조치 증적을 하나의 추적표로 연결하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 감리보고서상 지적사항(개선권고)에 대한 시정조치 완료 여부 판정 시 단순 확인서가 아닌 객관적 실증 증적(소스코드 수정 diff, 재시험 합격 로그, 성능측정치) 100% 확보 필수
- **대응 방안**: 감리 독립성 보장을 위한 발주자/사업자 업무 개입 금지 규정 준수 및 3단계 감리(요구정의/설계/종료)별 종료 판정 게이트 엄격 운영
- **검증 체계**: 감리기준서 기반 점검항목-검증방법-발견사항-조치증적 간 1:1 종단 추적표 작성 및 조치확인 감리 의무화
- **기대 효과**: 형식적 페이퍼 감리 탈피, 소프트웨어 결함의 운영 이관율 90% 차단 및 공공 정보시스템 대국민 서비스 안정성 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="증거 기반 감리 개선 흐름">
  <div class="itpe-pipeline-node"><strong>현행 한계</strong><div class="itpe-step-detail"><strong>문제</strong><span>점검표·발견사항·조치 결과 분리</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>개선 대안</strong><div class="itpe-step-detail"><strong>대안</strong><span>근거·검증방법·발견 증거·조치 증적 연결</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>검증 기준</strong><div class="itpe-step-detail"><strong>판정</strong><span>개선사항별 반영 결과·증적 대응</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>실행 효과</strong><div class="itpe-step-detail"><strong>효과</strong><span>감리결과의 실제 시스템 반영</span></div></div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **정보시스템 감리**는 발주자·사업자와 독립된 제3자가 정보시스템 구축·운영을 종합 점검하고 문제점을 개선하도록 하는 활동
- 목적: 사업 위험 조기 발견, 결함 잔존·재작업 감소

### 2. 법적 통제 구조

<div class="itpe-svg-map">
<svg viewBox="0 0 520 576" role="img" aria-label="전자정부법이 시행령에 위임하고 정보시스템 감리기준이 이를 구체화하는 3계층 법령 통제 구조와 각 계층의 통제 항목 트리">
  <defs><marker id="arrow-audit-law-quick" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <rect class="itpe-svg-node is-current" x="20" y="8" width="470" height="44" rx="12" />
  <text class="itpe-svg-title" x="255" y="30">「전자정부법」 제57조~제59조 · 통제 4</text>
  <path class="itpe-svg-link" d="M45 52 V205 M45 79 H75 M45 121 H75 M45 163 H75 M45 205 H75" />
  <rect class="itpe-svg-node" x="75" y="62" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="79">감리 실시 대상 확정</text>
  <rect class="itpe-svg-node" x="75" y="104" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="121">감리업무 개입·간섭 금지</text>
  <rect class="itpe-svg-node" x="75" y="146" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="163">감리결과 사업 반영 의무</text>
  <rect class="itpe-svg-node" x="75" y="188" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="205">감리법인 등록 · 성실 의무</text>
  <path class="itpe-svg-link" d="M465 52 V232" marker-end="url(#arrow-audit-law-quick)" />
  <text class="itpe-svg-label" x="437" y="140">위임</text>
  <rect class="itpe-svg-node" x="20" y="238" width="470" height="44" rx="12" />
  <text class="itpe-svg-title" x="255" y="260">같은 법 시행령 제71조·제72조 · 통제 2</text>
  <path class="itpe-svg-link" d="M45 282 V351 M45 309 H75 M45 351 H75" />
  <rect class="itpe-svg-node" x="75" y="292" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="309">의무감리 대상 판정</text>
  <rect class="itpe-svg-node" x="75" y="334" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="351">감리법인 업무범위 · 절차</text>
  <path class="itpe-svg-link" d="M465 282 V384" marker-end="url(#arrow-audit-law-quick)" />
  <text class="itpe-svg-label" x="433" y="330">구체화</text>
  <rect class="itpe-svg-node" x="20" y="390" width="470" height="44" rx="12" />
  <text class="itpe-svg-title" x="255" y="412">「정보시스템 감리기준」 · 통제 3</text>
  <path class="itpe-svg-link" d="M45 434 V545 M45 461 H75 M45 503 H75 M45 545 H75" />
  <rect class="itpe-svg-node" x="75" y="444" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="461">감리 업무범위 규정</text>
  <rect class="itpe-svg-node" x="75" y="486" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="503">계획 · 현장감리 · 보고 절차</text>
  <rect class="itpe-svg-node" x="75" y="528" width="320" height="34" rx="10" />
  <text class="itpe-svg-sub" x="235" y="545">감리원 준수사항</text>
</svg>
</div>

### 3. 핵심 판정

- 독립성: 발주자·사업자의 업무 개입 배제
- 실효성: 감리 발견사항과 시정조치 증적의 대응 확인

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 2교시: "정보시스템 구축 사업의 성공적인 수행을 위해 정보시스템 감리와 PMO(전자정부사업관리 위탁)를 활용하여 사업관리를 수행하고 있다. 이와 관련하여 다음을 설명하시오."
  - 가. 정보시스템 감리의 법적 근거
  - 나. PMO의 정의와 역할
  - 다. PMO 대상 사업의 범위
  - 라. PMO와 상주감리의 비교
- [국가법령정보센터, 「전자정부법」 제57조~제59조](https://www.law.go.kr/법령/전자정부법) — 2026년 8월 28일 시행, 법률 제21394호
- [국가법령정보센터, 「전자정부법 시행령」 제71조](https://www.law.go.kr/법령/전자정부법시행령) — 의무감리 대상·전자정부사업관리 위탁 시 예외 범위
- [국가법령정보센터, 「정보시스템 감리기준」](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000243290)
- [한국지능정보사회진흥원, 2022년 정보시스템 감리 발주·관리 가이드·감리 수행 가이드 개정본](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=24365&cbIdx=99860)
- [한국지능정보사회진흥원, PMO 도입·운영 가이드 2.1](https://nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=23222&cbIdx=99852)

## 학습 체크

- [ ] Ⅰ 개요: 정보시스템 감리를 독립된 제3자·구축·운영 종합 점검·문제 개선의 네 요소로 정의할 수 있는가?
- [ ] Ⅱ 법적 근거: 법 → 시행령 → 감리기준의 3계층 트리에 감리 대상·독립성·결과 반영·자격 통제를 배치하고 PMO 위탁 시 의무감리 예외 조건을 설명할 수 있는가?
- [ ] Ⅲ 수행체계: 대표 수행 흐름에서 계약·계획부터 조치 확인까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅳ 역할 경계: 발주기관·PMO·상주감리·사업자 사이의 위탁·보고·관리·점검 화살표를 그리고, PMO와 상주감리를 목적·업무·위치의 3축으로 비교할 수 있는가?
- [ ] Ⅴ 확인 판정: 개선사항과 조치 증적의 대응 여부를 통과·미통과로 판정할 수 있는가?
- [ ] Ⅵ 문제점·대응책: 독립 수행·근거 추적·조치 이행 통제 체인의 각 지점에 감리업무 개입·형식적 점검·미조치 종결 위험을 대응시키고 대책·효과를 연결할 수 있는가?
- [ ] Ⅶ 결론: 근거·검증방법·발견 증거·조치 증적을 연결한 판정·대안·검증·효과 네 줄을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [WBS](./007_wbs.md)
- 연관 토픽: [PMO](./004_pmo.md), [시스템 운영·유지보수 감리](./059_system_operation_audit.md), [클라우드 전환사업 감리](./104_cloud_migration_project_audit.md)
- 다음 토픽: [프로젝트 위험관리](./009_project_risk_management_negative.md)
