---
title: "소프트웨어 비용 산정(Software Cost Estimation)"
author: "Antigravity"
date: "2026-09-22T10:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW 사업 관리와 소프트웨어 비용 산정으로 이어지는 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 사업 관리</span>
  <strong>SW 비용 산정</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 개발 기능을 **FP(Function Point)**로 수량화하여 예산·계약대가의 공통 기준 마련
- 메커니즘: 경계 설정 → 5대 기능 측정 → 5대 보정 → 개발원가 산정
- 산출물: FP 산정서 · 개발원가 · 직접경비 · SW 개발비

<div class="itpe-svg-map">
<svg viewBox="0 0 760 430" role="img" aria-label="기능점수 측정에서 소프트웨어 개발비 산정까지의 구조">
  <defs>
    <marker id="sw-cost-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link" />
    </marker>
  </defs>
  <rect x="250" y="18" width="260" height="62" rx="14" class="itpe-svg-node" />
  <text x="380" y="44" text-anchor="middle" class="itpe-svg-title">요구사항·애플리케이션 경계</text>
  <text x="380" y="65" text-anchor="middle" class="itpe-svg-sub">측정 범위 확정</text>
  <path d="M380 80 L380 118" class="itpe-svg-link" marker-end="url(#sw-cost-arrow)" />
  <rect x="75" y="125" width="270" height="92" rx="14" class="itpe-svg-node" />
  <text x="210" y="153" text-anchor="middle" class="itpe-svg-title">데이터 기능</text>
  <text x="210" y="178" text-anchor="middle" class="itpe-svg-sub">ILF · EIF</text>
  <text x="210" y="199" text-anchor="middle" class="itpe-svg-label">내부 보유 · 외부 참조 데이터</text>
  <rect x="415" y="125" width="270" height="92" rx="14" class="itpe-svg-node" />
  <text x="550" y="153" text-anchor="middle" class="itpe-svg-title">트랜잭션 기능</text>
  <text x="550" y="178" text-anchor="middle" class="itpe-svg-sub">EI · EO · EQ</text>
  <text x="550" y="199" text-anchor="middle" class="itpe-svg-label">입력 · 출력 · 조회</text>
  <path d="M380 105 L210 105 L210 125" class="itpe-svg-link" marker-end="url(#sw-cost-arrow)" />
  <path d="M380 105 L550 105 L550 125" class="itpe-svg-link" marker-end="url(#sw-cost-arrow)" />
  <path d="M210 217 L210 252 L380 252" class="itpe-svg-link" />
  <path d="M550 217 L550 252 L380 252" class="itpe-svg-link" />
  <path d="M380 252 L380 263" class="itpe-svg-link" marker-end="url(#sw-cost-arrow)" />
  <rect x="250" y="270" width="260" height="62" rx="14" class="itpe-svg-node is-current" />
  <text x="380" y="296" text-anchor="middle" class="itpe-svg-title">보정 기능점수</text>
  <text x="380" y="317" text-anchor="middle" class="itpe-svg-sub">규모 · 연계 · 성능 · 다중사이트 · 보안</text>
  <path d="M380 332 L380 366" class="itpe-svg-link" marker-end="url(#sw-cost-arrow)" />
  <rect x="160" y="375" width="440" height="42" rx="12" class="itpe-svg-node" />
  <text x="380" y="402" text-anchor="middle" class="itpe-svg-title">개발원가 + 이윤 + 직접경비 = SW 개발비</text>
</svg>
</div>

<details>
<summary>핵심 용어</summary>

- **FP(Function Point)**: 사용자에게 제공되는 논리적 기능의 규모 측정 단위
- **ILF(Internal Logical File)**: 애플리케이션 경계 내부에서 유지하는 데이터 기능
- **EIF(External Interface File)**: 다른 애플리케이션이 유지하고 측정 대상이 참조하는 데이터 기능
- **EI(External Input)**: 경계 밖에서 들어와 내부 데이터·동작을 변경하는 트랜잭션 기능
- **EO(External Output)**: 처리·계산을 포함해 경계 밖으로 정보를 제공하는 트랜잭션 기능
- **EQ(External Inquiry)**: 중요한 처리 없이 입력에 대응한 정보를 조회하는 트랜잭션 기능

</details>

## 예상문제

> **(미출제 예상·25점)** SW 비용 산정 접근법을 비교하고, 기능점수 방식의 측정 절차·개발비 구성·산정 위험과 대응책을 설명하시오.

## Ⅰ. SW 비용 산정의 개요

> 요구사항을 측정 가능한 규모와 비용으로 변환해야 예산·계약·변경관리의 기준이 성립한다.

- 정의: SW의 **규모·공수·기간**을 추정하여 개발·운영에 필요한 비용을 산정하는 활동
- 목적: 적정 예산·계약대가 확보 · 변경비용 산정 · 사업 타당성 판단

## Ⅱ. 비용 산정 접근법과 FP 산정 체계

> 초기에는 유사사례로 범위를 잡고, 요구사항이 구체화되면 작업분해·모형 기반 추정으로 정밀화한다.

### 1. 비용 산정 접근법

| 접근법 | 기준 | 적용 |
|---|---|---|
| 하향식 | 전문가 판단 · 유사사례 | 초기 개략 견적 |
| 상향식 | **WBS(Work Breakdown Structure)** 작업별 공수 | 상세 범위 확정 후 |
| 모형식 | FP · **COCOMO(Constructive Cost Model)** | 데이터 기반 검증 |

### 2. FP 측정·대가 산정 메커니즘

```
[5대 기능 식별] ──> [미보정 FP] ──> [5대 보정계수] ──> [보정 FP] ──> [개발원가] ──> [총 SW 개발비]
 - 데이터: ILF, EIF                    - 규모/연계복잡성          × 단가(605,784원)    + 이윤(최대 25%)
 - 트랜잭션: EI, EO, EQ                - 성능/다중사이트/보안                         + 직접경비
```

<div class="itpe-svg-map">
<svg viewBox="0 0 520 220" role="img" aria-label="기능점수 기반 SW 개발비 산출 파이프라인">
  <!-- 배경 바운더리 -->
  <rect x="10" y="10" width="500" height="200" rx="8" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" />

  <!-- 1. 5대 기능 식별 -->
  <g transform="translate(25, 25)">
    <rect x="0" y="0" width="145" height="80" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
    <text x="72" y="20" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-text)">1. 5대 기능 식별</text>
    <text x="72" y="40" text-anchor="middle" font-size="9" fill="var(--sl-color-accent)">데이터: ILF, EIF</text>
    <text x="72" y="58" text-anchor="middle" font-size="9" fill="var(--sl-color-accent)">트랜잭션: EI, EO, EQ</text>
    <text x="72" y="73" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2)">→ 미보정 기능점수(UFP)</text>
  </g>

  <!-- 화살표 1 -> 2 -->
  <line x1="170" y1="65" x2="190" y2="65" stroke="var(--sl-color-accent)" stroke-width="1.5" />

  <!-- 2. 5대 보정계수 -->
  <g transform="translate(190, 25)">
    <rect x="0" y="0" width="145" height="80" rx="5" fill="var(--sl-color-accent-low)" stroke="var(--sl-color-accent)" stroke-width="1.5" />
    <text x="72" y="20" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-accent-high)">2. 5대 보정계수</text>
    <text x="72" y="38" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text)">① 규모 (소규모~대규모)</text>
    <text x="72" y="52" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text)">② 연계복잡성 ③ 성능요구</text>
    <text x="72" y="66" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text)">④ 다중사이트 ⑤ 보안성</text>
  </g>

  <!-- 화살표 2 -> 3 -->
  <line x1="335" y1="65" x2="355" y2="65" stroke="var(--sl-color-accent)" stroke-width="1.5" />

  <!-- 3. 보정 FP 및 개발원가 -->
  <g transform="translate(355, 25)">
    <rect x="0" y="0" width="135" height="80" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
    <text x="67" y="20" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-text)">3. 개발원가 산출</text>
    <text x="67" y="40" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">보정 FP (AFP)</text>
    <text x="67" y="58" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--sl-color-text)">× 605,784원/FP</text>
    <text x="67" y="73" text-anchor="middle" font-size="8" fill="var(--sl-color-accent)">(2025 개정단가)</text>
  </g>

  <!-- 수직 연결 -->
  <line x1="422" y1="105" x2="422" y2="125" stroke="var(--sl-color-accent)" stroke-width="1.5" />

  <!-- 하단 최종 산출식 -->
  <g transform="translate(25, 125)">
    <rect x="0" y="0" width="465" height="65" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-accent)" stroke-width="1.5" />
    <text x="232" y="25" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-accent-high)">최종 SW 개발비 = 개발원가 + 이윤(최대 25%) + 직접경비</text>
    <text x="232" y="45" text-anchor="middle" font-size="9.5" fill="var(--sl-color-gray-2)">직접경비: 엔지니어링 출장여비, 전산소모품, 도입SW 라이선스 등 실비 반영</text>
  </g>
</svg>
</div>

<div class="itpe-pipeline is-vertical" role="img" aria-label="기능점수 측정과 소프트웨어 개발비 산정 절차">
  <div class="itpe-pipeline-node"><strong>① 측정 범위 설정</strong><div class="itpe-step-detail"><strong>활동</strong><span>사용자 관점 애플리케이션 경계 확정</span></div><div class="itpe-step-detail"><strong>산출</strong><span>측정 범위 · 경계</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>② 기능 식별</strong><div class="itpe-step-detail"><strong>활동</strong><span>ILF · EIF · EI · EO · EQ 분류</span></div><div class="itpe-step-detail"><strong>산출</strong><span>기능 목록</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>③ 기능점수 산정</strong><div class="itpe-step-detail"><strong>활동</strong><span>정통법 복잡도 또는 간이법 평균 가중치 적용</span></div><div class="itpe-step-detail"><strong>산출</strong><span>미보정 기능점수</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>④ 개발원가 산정</strong><div class="itpe-step-detail"><strong>활동</strong><span>FP 단가 · 5대 보정계수 적용</span></div><div class="itpe-step-detail"><strong>산출</strong><span>보정 기능점수 · 개발원가</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>⑤ 개발비 확정</strong><div class="itpe-step-detail"><strong>활동</strong><span>이윤 · 직접경비 합산</span></div><div class="itpe-step-detail"><strong>산출</strong><span>SW 개발비 산정서</span></div></div>
</div>

### 3. 현행 기능점수 방식의 핵심 식

```text
개발원가 = 기능점수 × 기능점수당 단가 × 5대 보정계수
SW 개발비 = 개발원가 + 이윤 + 직접경비
```

- 5대 보정계수: **규모 · 연계복잡성 · 성능요구수준 · 다중사이트 운영성 · 보안성**
- 2025년 개정판 기능점수당 단가: **605,784원**

## Ⅲ. 주요 산정 모형 비교

> 모형의 우열보다 산정 시점에 확보 가능한 입력과 추정 목적의 일치가 중요하다.

| 기준 | FP | LOC | COCOMO |
|---|---|---|---|
| 입력 | 사용자 기능 | 코드 라인 | 코드 규모 · 비용동인 |
| 장점 | 언어 독립 · 조기 측정 | 측정 단순 | 공수·기간 추정 |
| 한계 | 경계·기능 판정 편차 | 언어·구현 종속 | 보정 데이터 필요 |

## Ⅳ. 문제점·대응책

> 산식보다 측정 경계·기능 식별·변경 추적의 일관성이 견적 신뢰도를 결정한다.

| 위험 | 대책 | 효과 |
|---|---|---|
| 경계 불일치 | 애플리케이션 경계 합의 · 검토 | 중복·누락 방지 |
| 기능 분류 편차 | 측정 규칙 · 교차검증 적용 | 산정 재현성 확보 |
| 비기능 비용 누락 | 5대 보정계수 근거 기록 | 사업 특성 반영 |
| 범위 변경 미정산 | **RTM(Requirements Traceability Matrix)**과 증분 FP 연계 | 변경대가 근거 확보 |

## Ⅴ. 결론·기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]** 아무리 정밀한 공학적 FP 산식도 불명확한 시스템 경계와 과업 변경을 흡수하지 못한다. 견적의 신뢰성은 초기 산정의 정확도보다, 개발 생애주기 동안 발생하는 요구사항 변경을 RTM과 증분 FP로 추적하여 대가로 연결하는 과업심의 연계성에 달려 있다.
> 
> **나라면** RFP 기획 단계에서는 간이법 FP로 예산을 편성하되, 분석·설계 완료 단계에서 정통법 FP로 전수 재측정하여 과업 Baseline을 확정하고, 변경 발생 시 10% 이상 규모 증감에 대해 과업심의위원회를 즉각 소집하여 계약금액 조정을 신청하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 분석/설계 완료 시점 상세 FP 측정을 통해 기획 예산 대비 변동폭 ±10% 초과 시 즉시 계약 변경 및 과업심의 의무 상정
- **대응 방안**: 5대 보정계수(규모, 연계, 성능, 사이트, 보안) 적용 시 객관적 정량 증적(연계 인터페이스 명세서, 보안성 검토 결과 등) 첨부 제도화
- **검증 체계**: 전문 감리법인 및 공공 SW 대가 전문위원회의 교차 검증(Cross-Check)을 통한 기능 분류(ILF/EIF/EI/EO/EQ) 왜곡 방지
- **기대 효과**: 공공 SW 사업 제값 받기 정착, 잦은 과업 추가에 따른 개발사 적자 리스크 원천 차단 및 납기 품질 보장

<div class="itpe-svg-map">
<svg viewBox="0 0 760 500" role="img" aria-label="기능점수 재산정과 변경통제를 결합한 비용 산정 개선안">
  <defs>
    <marker id="sw-cost-control-arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link" />
    </marker>
  </defs>
  <rect x="190" y="20" width="380" height="70" rx="14" class="itpe-svg-node" />
  <text x="380" y="47" text-anchor="middle" class="itpe-svg-title">기획단계 개략 견적</text>
  <text x="380" y="70" text-anchor="middle" class="itpe-svg-sub">유사사례 · 간이 FP</text>
  <path d="M380 90 L380 130" class="itpe-svg-link" marker-end="url(#sw-cost-control-arrow)" />
  <rect x="190" y="140" width="380" height="70" rx="14" class="itpe-svg-node" />
  <text x="380" y="167" text-anchor="middle" class="itpe-svg-title">분석·설계단계 재산정</text>
  <text x="380" y="190" text-anchor="middle" class="itpe-svg-sub">경계 · 5대 기능 · 보정근거 검증</text>
  <path d="M380 210 L380 250" class="itpe-svg-link" marker-end="url(#sw-cost-control-arrow)" />
  <rect x="190" y="260" width="380" height="70" rx="14" class="itpe-svg-node is-current" />
  <text x="380" y="287" text-anchor="middle" class="itpe-svg-title">비용 Baseline 확정</text>
  <text x="380" y="310" text-anchor="middle" class="itpe-svg-sub">FP 산정서 · 예산 · 계약범위 일치</text>
  <path d="M380 330 L380 370" class="itpe-svg-link" marker-end="url(#sw-cost-control-arrow)" />
  <rect x="70" y="380" width="270" height="80" rx="14" class="itpe-svg-node" />
  <text x="205" y="408" text-anchor="middle" class="itpe-svg-title">변경 없음</text>
  <text x="205" y="433" text-anchor="middle" class="itpe-svg-sub">Baseline 유지</text>
  <rect x="420" y="380" width="270" height="80" rx="14" class="itpe-svg-node" />
  <text x="555" y="408" text-anchor="middle" class="itpe-svg-title">변경 발생</text>
  <text x="555" y="433" text-anchor="middle" class="itpe-svg-sub">RTM → 증분 FP → 계약 조정</text>
  <path d="M380 355 L205 355 L205 380" class="itpe-svg-link" marker-end="url(#sw-cost-control-arrow)" />
  <path d="M380 355 L555 355 L555 380" class="itpe-svg-link" marker-end="url(#sw-cost-control-arrow)" />
</svg>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: SW의 **규모·공수·기간**을 추정하여 개발·운영 비용을 산정하는 활동
- 목적: 적정 예산·계약대가 확보 · 변경비용 산정

### 2. FP 기반 개발비 산정

```text
경계 설정 → ILF·EIF·EI·EO·EQ 측정 → 5대 보정 → 개발원가
개발원가 + 이윤 + 직접경비 = SW 개발비
```

### 3. 핵심 고려사항

- 애플리케이션 경계와 기능 분류의 일관성
- 보정계수 근거와 FP 산정서의 추적성
- 범위 변경 시 증분 FP 재산정

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [한국인공지능·소프트웨어산업협회, SW사업 대가산정 가이드(2025년 개정판)](https://www.sw.or.kr/site/sw/ex/board/View.do?bcIdx=63607&cbIdx=276)
- [ISO, ISO/IEC 14143-1:2007 Functional size measurement](https://www.iso.org/standard/42188.html)

## 학습 체크

- [ ] Ⅰ: SW 비용 산정의 정의·목적을 구분해 쓸 수 있는가?
- [ ] Ⅱ: FP 5대 기능과 5대 보정계수를 각각 재현할 수 있는가?
- [ ] Ⅱ: 개발원가와 SW 개발비의 구성을 식으로 설명할 수 있는가?
- [ ] Ⅲ: FP·LOC·COCOMO를 입력·장점·한계로 비교할 수 있는가?
- [ ] Ⅳ~Ⅴ: 산정 위험 4개와 재산정·변경통제 방안을 연결할 수 있는가?

## 연결 토픽

- 이전: [112. CCPM·TOC](./112_critical_chain_toc.md)
- 관련: [026. SW 사업 대가산정](./026_software_cost_estimation.md) · [091. 과업심의](./091_public_sw_cost_and_scope_change_criteria.md)
- 다음: [114. 개방형 혁신](./114_open_innovation.md)

