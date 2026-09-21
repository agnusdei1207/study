---
title: "SW 규모·비용 산정(FP·LOC·COCOMO)"
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

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 공공 SW·거버넌스를 거쳐 SW 규모·비용 산정으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>공공 SW·거버넌스</span>
  <strong>SW 규모·비용 산정</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **SW 규모·비용 산정**은 소프트웨어 개발 프로젝트의 공수, 일정, 소요 예산을 합리적으로 예측하여 예산 왜곡과 사업 부실을 방지하는 정량적 측정 체계
- 메커니즘: 규모 측정(**LOC, FP, 스토리 포인트**) → 노력(Man-Month) 추정(**COCOMO II, Putnam, 기능점수 단가법**) → 개발 원가 산출
- 산출/효과: 합리적 발주 예산 확정 · 과업 변경 대가 산정 기준선(Baseline) 마련 · 개발 생산성 평가

<div class="itpe-flow-map" role="img" aria-label="SW 규모 및 비용 산정 프로세스">
  <div class="itpe-flow-node"><strong>소프트웨어 요구사항</strong><span>기능 및 비기능 요구명세</span></div>
  <div class="itpe-flow-arrow">→ 규모 측정 모델 →</div>
  <div class="itpe-flow-node is-current">
    <strong>규모 산정 기법</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>LOC</strong><span>라인 수 기반 (언어 의존적)</span></div>
      <div class="itpe-flow-branch"><strong>기능점수(FP)</strong><span><span class="itpe-keyword"><strong>사용자 관점 논리적 기능 수량화</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>COCOMO</strong><span><span class="itpe-keyword"><strong>규모 + 비용동인 기반 공수 계산</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 투입 공수 및 원가 도출 →</div>
  <div class="itpe-flow-node"><strong>사업 대가 확정</strong><span>SW 사업 대가산정 가이드 준수</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Function Point (기능점수, FP)**: 사용자가 요구한 기능의 논리적 크기를 데이터 기능(ILF, EIF)과 트랜잭션 기능(EI, EO, EQ)으로 측정하는 표준 기법
- **LOC(Lines of Code)**: 원시 소스코드의 총 라인 수를 기준으로 소프트웨어 규모를 측정하는 전통적 기법
- **COCOMO (Constructive Cost Model)**: Boehm이 제안한 모델로, 규모(KLOC)와 프로젝트 복잡도(비용동인)를 수학 공식에 대입해 공수(M/M)를 산출하는 기법
- **COCOMO II**: 현대 소프트웨어 공학(객체지향, 재사용, RAD)을 반영하여 Application Composition, Early Design, Post-Architecture 3단계로 발전된 모델
- **SW사업 대가산정 가이드**: 과학기술정보통신부와 한국소프트웨어산업협회(KOSA)에서 공공 SW 사업의 예산 수립 및 계약 대가를 산정하기 위해 고시한 표준 기준

</details>

## 예상문제

> 소프트웨어 규모 및 비용 산정 기법의 발전 과정을 설명하고, LOC 기법, COCOMO 모델의 프로젝트 유형(Organic, Semi-detached, Embedded), 기능점수(Function Point)의 5대 기능 구성요소 및 공공 SW 사업 대가산정 가이드에 따른 FP 단가법 적용 방안을 제시하시오. (25점)

## Ⅰ. 합리적 예산 수립과 발주 정상화의 초석, SW 비용 산정의 개요

> 소프트웨어는 비가시적 특성으로 인해 과소 산정 시 사업 파행을, 과대 산정 시 예산 낭비를 초래하므로 과학적 정량 산정이 필수적이다.

- 정의: 소프트웨어 개발에 소요되는 규모, 투입 공수(Man-Month), 일정, 직접비 및 간접비를 수학적·통계적 모델을 통해 사전에 추정하는 공학적 활동
- 목적: 합리적인 발주 예산 편성, 프로젝트 일정 및 자원 계획 수립, 과업 변경 시 객관적 추가 대가 산정 근거 확보

## Ⅱ. 3대 주요 비용 산정 기법: LOC, COCOMO, 기능점수(FP)

> 규모 측정 단위가 원시 코드 라인 수(LOC)에서 사용자 관점의 논리적 기능 단위(FP)로 진화하였다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="SW 비용 산정 모델 계층">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. LOC 기반 기법 (원시 코드 라인 수)</strong></span>
    <span>낙관치, 비관치, 기대치를 가중 평균(PERT 산식)하여 규모 산정 (언어·숙련도 편차 극심)</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ 공학적 발전</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. COCOMO 모델 (수학적 공수 산정)</strong></span>
    <span>MM = a × (KLOC)^b × EAF (Organic, Semi-detached, Embedded 프로젝트 유형별 가중치)</span>
  </div>
  <div class="itpe-pipeline-arrow">↓ 사용자 기능 관점 전환</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. 기능점수(FP) 기법 (국제 표준 ISO/IEC 20926)</strong></span>
    <span>데이터 기능(ILF, EIF) + 트랜잭션 기능(EI, EO, EQ) (언어 독립적, 조기 산정 가능)</span>
  </div>
</div>

| 비교 항목 | LOC 기법 | COCOMO 기법 | 기능점수 (Function Point) |
|---|---|---|---|
| **측정 기준** | 소스코드 물리적 라인 수 | KLOC + 15~17개 비용동인 계수 | **사용자 관점 논리적 기능 수** |
| **적용 시점** | 구현 중반~종료 시점 (사후적) | 기본 설계 이후 | **기획, 요구분석 초기 단계부터 가능** |
| **언어 독립성** | 언어에 종속적 (C vs Python 편차) | 언어에 종속적 | **완벽한 언어 독립성 (동등 비교 가능)** |
| **특성·근거** | 구현 후 측정 용이 | 경험 데이터 보정 필요 | 국제 표준·공공 대가산정 가이드에서 활용 |

## Ⅲ. 기능점수(FP)의 5대 기능 구성요소와 산정 체계

> 공공 SW 사업의 대가산정 가이드는 기능점수를 단일 표준으로 채택하고 있다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="기능점수 5대 기능 구성도">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>데이터 기능 (Data Functions)</strong></span>
    <span>1. 내부논리파일(ILF): 시스템 내부에서 유지·관리하는 논리적 데이터 그룹<br />2. 외부연계파일(EIF): 타 시스템에서 유지되며 현재 시스템이 참조만 하는 데이터</span>
  </div>
  <div class="itpe-pipeline-arrow">↕ 상호 작용</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>트랜잭션 기능 (Transaction Functions)</strong></span>
    <span>1. 외부입력(EI): 내부 데이터를 등록, 수정, 삭제하는 트랜잭션<br />2. 외부출력(EO): 수학적 계산이나 파생 데이터를 포함하여 외부로 출력<br />3. 외부조회(EQ): 단순 검색을 통해 데이터를 외부로 표출하는 트랜잭션</span>
  </div>
</div>

### 기능점수(FP) 5대 기능 분류 및 개발비 산정 메커니즘

<div class="itpe-svg-wrapper">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" class="itpe-svg">
    <!-- Background -->
    <rect width="520" height="220" fill="var(--sl-color-bg-subtle, #f8fafc)" rx="8" />
    
    <!-- Title -->
    <text x="20" y="24" class="itpe-svg-label" fill="var(--sl-color-text-accent, #2563eb)">[기능점수(FP) 5대 기능 요소 분류 및 대가 산정 흐름]</text>

    <!-- 1. Data Functions (Left) -->
    <rect x="18" y="48" width="145" height="150" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1.2" />
    <text x="90" y="70" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">데이터 기능 (2종)</text>
    <line x1="28" y1="80" x2="153" y2="80" stroke="var(--sl-color-border, #e2e8f0)" />
    
    <!-- ILF -->
    <rect x="26" y="90" width="129" height="46" rx="4" fill="var(--sl-color-bg-accent, #eff6ff)" />
    <text x="34" y="108" class="itpe-svg-title" font-size="11" font-weight="700" fill="var(--sl-color-primary, #3b82f6)">ILF (내부논리파일)</text>
    <text x="34" y="125" class="itpe-svg-sub" font-size="9.5" fill="var(--sl-color-text, #334155)">내부 유지·관리 데이터</text>

    <!-- EIF -->
    <rect x="26" y="142" width="129" height="46" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="34" y="160" class="itpe-svg-title" font-size="11" font-weight="700" fill="var(--sl-color-text, #1e293b)">EIF (외부연계파일)</text>
    <text x="34" y="177" class="itpe-svg-sub" font-size="9.5" fill="var(--sl-color-text-muted, #64748b)">타 시스템 참조 데이터</text>

    <!-- Arrow from Data to Transaction -->
    <line x1="163" y1="123" x2="178" y2="123" stroke="var(--sl-color-text-muted, #94a3b8)" stroke-width="1.5" />

    <!-- 2. Transaction Functions (Center) -->
    <rect x="178" y="48" width="165" height="150" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-accent, #8b5cf6)" stroke-width="1.2" />
    <text x="260" y="70" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-accent, #8b5cf6)" text-anchor="middle">트랜잭션 기능 (3종)</text>
    <line x1="188" y1="80" x2="333" y2="80" stroke="var(--sl-color-border, #e2e8f0)" />

    <!-- EI -->
    <rect x="186" y="88" width="149" height="32" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="194" y="103" class="itpe-svg-sub" font-size="10.5" font-weight="600" fill="var(--sl-color-text, #1e293b)">EI (외부입력): CUD</text>
    <text x="194" y="115" class="itpe-svg-label" font-size="9" fill="var(--sl-color-text-muted, #64748b)">데이터 등록/수정/삭제</text>

    <!-- EO -->
    <rect x="186" y="124" width="149" height="32" rx="4" fill="var(--sl-color-bg-accent, #eff6ff)" />
    <text x="194" y="139" class="itpe-svg-sub" font-size="10.5" font-weight="600" fill="var(--sl-color-accent, #8b5cf6)">EO (외부출력): 계산/파생</text>
    <text x="194" y="151" class="itpe-svg-label" font-size="9" fill="var(--sl-color-accent, #8b5cf6)">수학적 통계/리포트</text>

    <!-- EQ -->
    <rect x="186" y="160" width="149" height="32" rx="4" fill="var(--sl-color-bg-subtle, #f1f5f9)" />
    <text x="194" y="175" class="itpe-svg-sub" font-size="10.5" font-weight="600" fill="var(--sl-color-text, #1e293b)">EQ (외부조회): 단순검색</text>
    <text x="194" y="187" class="itpe-svg-label" font-size="9" fill="var(--sl-color-text-muted, #64748b)">단순 데이터 조회 출력</text>

    <!-- Arrow to Formula Box -->
    <line x1="343" y1="123" x2="358" y2="123" stroke="var(--sl-color-success, #10b981)" stroke-width="1.5" marker-end="url(#arrow)" />

    <!-- 3. Cost Calculation Formula Box (Right) -->
    <rect x="358" y="48" width="146" height="150" rx="6" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-success, #10b981)" stroke-width="1.5" />
    <text x="431" y="70" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-success, #10b981)" text-anchor="middle">SW 개발비 산정</text>
    <line x1="368" y1="80" x2="494" y2="80" stroke="var(--sl-color-border, #e2e8f0)" />
    <text x="431" y="100" class="itpe-svg-sub" font-size="10.5" font-weight="600" fill="var(--sl-color-text, #1e293b)" text-anchor="middle">총 기능점수 (FP)</text>
    <text x="431" y="118" class="itpe-svg-sub" font-size="11" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">×</text>
    <text x="431" y="134" class="itpe-svg-sub" font-size="10" font-weight="600" fill="var(--sl-color-text, #334155)" text-anchor="middle">FP당 단가 (원)</text>
    <text x="431" y="150" class="itpe-svg-sub" font-size="11" fill="var(--sl-color-text-muted, #64748b)" text-anchor="middle">×</text>
    <rect x="368" y="158" width="126" height="28" rx="4" fill="var(--sl-color-bg-accent, #ecfdf5)" />
    <text x="431" y="176" class="itpe-svg-label" font-size="9.5" font-weight="700" fill="var(--sl-color-success, #10b981)" text-anchor="middle">보정계수 (규모·연계·품질)</text>
  </svg>
</div>

### 공공 SW 사업 기능점수 단가법 산식
- **SW 개발비** = 기능점수(FP) × 해당 연도 기능점수당 단가 × 보정계수 + 직접경비 + 이윤

## Ⅳ. 소프트웨어 비용 산정 문제점·대응책

> 요구사항 불명확성과 정치적 예산 삭감이 프로젝트 부실의 가장 큰 원인이다.

| 위험 | 대책 | 효과 |
|---|---|---|
| 요구사항 조기 고정 실패로 인한 비용 오차 | 기획 시 간이법(평균 복잡도 FP) 적용 후 ISMP/설계 시 정밀법 재산정 | 프로젝트 단계별 산정 정밀도 및 예산 현실성 확보 |
| 비기능 요구사항 누락 및 대가 왜곡 | 성능·보안·품질 요구수준에 따른 법정 품질 보정계수 전면 반영 | 비기능 구현 공수 정당 보상 및 시스템 품질 보증 |
| 무상 과업 변경으로 인한 사업자 부실화 | 요구사항 추적표(RTM) 및 변경 FP 기반 과업심의위원회 공식 상정 | 과업 변경에 대한 정당한 추가 대가 수령 및 공정 계약 달성 |

## Ⅴ. 추정 근거·변경 정산 중심의 결론

> 비용 산정은 계약을 위한 요식 행위가 아니라, 소프트웨어 산업의 공정 생태계를 지키는 법적 안전장치여야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 기능점수(FP)가 만능은 아님. 고난도 AI 알고리즘 개발이나 대규모 분산 아키텍처 리팩토링은 사용자 인터페이스 상 FP가 거의 나오지 않는 'FP의 맹점'이 존재함. 이러한 연구개발형 또는 인프라성 사업에서는 투입공수 방식(M/M)이나 헤드카운트 모델을 병행 적용하는 유연성이 요구됨.
- 나라면: 공공 사업 발주 시 ISP/ISMP 단계에서 도출된 상세 요구사항 명세서를 기반으로 1차 기능점수를 산출하고, 구축 사업 완료 시점의 실제 구현 FP와 비교하여 변경된 과업에 대해 법정 대가를 정산하는 '사후 정산형 계약 거버넌스'를 정착시키겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 프로젝트 단계별 요구명세 구체화 수준에 따른 산정 기법 차등 적용 (기획/발주: 간이 FP, 상세설계: 정밀 FP)
- **대응 방안**: 과학기술정보통신부/KOSA **SW사업 대가산정 가이드** 단가법 표준 준수 및 **과업심의위원회** 연계 변경 대가 지급 보장
- **검증 체계**: ILF/EIF 및 EI/EO/EQ 복잡도 매트릭스 100% 검증 및 법정 4대 품질 보정계수(규모, 연계, 성능, 다국어) 객관적 산출
- **기대 효과**: 소프트웨어 개발 사업자 적정 대가 보장, 무상 과업 변경 관행 타파 및 공정 소프트웨어 생태계 기반 고품질 산출물 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="SW 비용 산정 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>주먹구구식 예산 책정 · 과업 변경에 대한 대가 미지급 및 사업 부실</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>FP 기반 객관적 규모 측정 표준화 및 변경 FP 법정 대가 지급 의무화</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>KOSA 가이드라인 검증 · ILF/EIF 및 EI/EO/EQ 복잡도 매트릭스 검증</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>공정 소프트웨어 거래 생태계 확립 · 적정 대가 보장을 통한 품질 혁신</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **SW 규모·비용 산정**은 요구사항을 기반으로 크기(FP/LOC)를 정량화하고 투입 공수와 사업비를 수학적 모델로 산출하는 활동
- 목적: 합리적인 발주 예산 편성 및 과업 변경에 따른 객관적 정산 기준 확보

### 2. 기능점수(FP) 5대 기능 구성

<div class="itpe-pipeline is-vertical" role="img" aria-label="FP 5대 구성 요약">
  <div class="itpe-pipeline-node"><strong>데이터 기능</strong><span>ILF (내부논리파일) · EIF (외부연계파일)</span></div>
  <div class="itpe-pipeline-arrow">↕</div>
  <div class="itpe-pipeline-node"><strong>트랜잭션 기능</strong><span>EI (외부입력) · EO (외부출력) · EQ (외부조회)</span></div>
</div>

### 3. 핵심 통제

- **COCOMO 모델**: KLOC 기반 수학적 공수 산정 및 비용동인(Cost Driver) 반영
- **가이드라인 준수**: 과기정통부 및 KOSA 소프트웨어 사업 대가산정 가이드 준수
- **위험 통제**: 간이법/정밀법 단계별 적용 및 과업심의위원회 연계로 대가 보장

## 출제 이력과 검증 출처

- 제132회 정보관리기술사 1교시: 기능점수(Function Point)의 데이터 및 트랜잭션 기능
- 제137회 정보관리기술사 2교시: 소프트웨어 사업 대가산정 가이드 및 FP 단가법 적용 절차
- 과학기술정보통신부 / 한국소프트웨어산업협회(KOSA), SW사업 대가산정 가이드 (2025년판)

## 학습 체크

- [ ] LOC, COCOMO, 기능점수(FP)의 측정 기준과 장단점을 비교할 수 있는가?
- [ ] 기능점수의 5대 기능(ILF, EIF, EI, EO, EQ)의 개념과 차이를 설명할 수 있는가?
- [ ] 공공 SW 대가산정 가이드에서 기능점수 단가법의 계산 공식을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [유스케이스 다이어그램](./026_use_case_diagram.md)
- 연관 토픽: [기능점수](./130_function_point.md), [과업심의위원회](./048_task_deliberation_committee.md)
- 다음 토픽: [SW 안전성 분석](./028_sw_safety_analysis.md)
