---
title: "EA/ITA(Enterprise Architecture/Information Technology Architecture)"
author: "Antigravity"
date: "2026-09-20T19:33:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 전사 아키텍처 및 IT 거버넌스를 거쳐 EA/ITA로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>전사 아키텍처·IT 거버넌스</span>
  <strong>EA/ITA</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 비즈니스 목표와 IT 자원(데이터·응용·기술·보안)의 상호 관계를 구조화된 청사진으로 정의하여 중복 투자를 방지하는 전사 설계 프레임워크
- 메커니즘: 기본 모델(5대 뷰) 수립 → **5대 참조모델(PRM/BRM/DRM/ARM/TRM)** 정렬 → 현행-목표 갭 분석 → **EAMS** 기반 거버넌스
- 산출: 전사 아키텍처 정의서 · 5대 뷰 모델링 명세서 · 갭 분석 및 이행 로드맵 · 아키텍처 적합성 검토서

<div class="itpe-flow-map" role="img" aria-label="EA/ITA의 아키텍처 모델, 5대 참조모델, 관리체계 3대 축과 거버넌스 순환 흐름">
  <div class="itpe-flow-node">
    <strong>경영 전략 및 비즈니스 비전</strong>
    <div class="itpe-step-detail"><span>전사 비즈니스 목표 · 아키텍처 수립 원칙</span></div>
  </div>
  <div class="itpe-flow-arrow">↓<small>전사 청사진 수립</small></div>
  <div class="itpe-flow-node is-current">
    <strong>EA/ITA 3대 핵심 구성 축</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>모델</strong><span><span class="itpe-keyword"><strong>5대 뷰</strong></span> (BA · DA · AA · TA · SA) / As-Is → To-Be</span></div>
      <div class="itpe-flow-branch"><strong>참조</strong><span><span class="itpe-keyword"><strong>5대 참조모델</strong></span> (PRM · BRM · DRM · ARM · TRM)</span></div>
      <div class="itpe-flow-branch"><strong>관리</strong><span>아키텍처 위원회 · 적합성 심의 · <span class="itpe-keyword"><strong>EAMS 포털</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>실행 및 진화</small></div>
  <div class="itpe-flow-node">
    <strong>Living Architecture as Code</strong>
    <div class="itpe-step-detail"><span>중복 투자 배제 · 상호운용성 확보 · Git/API 실시간 동기화</span></div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **EA(Enterprise Architecture)**: 조직의 업무와 이를 지원하는 정보기술 간의 관계를 종합적으로 정리한 전사적 청사진
- **ITA(Information Technology Architecture)**: 정보기술아키텍처로, 정보시스템의 효율적 도입 및 운영을 위한 기술적 아키텍처 체계
- **5대 아키텍처 뷰(BA/DA/AA/TA/SA)**: 비즈니스(BA), 데이터(DA), 응용(AA), 기술(TA), 보안(SA) 관점의 구조적 모델
- **5대 참조모델(Reference Model)**: 범정부 차원의 성과(PRM), 업무(BRM), 데이터(DRM), 서비스(ARM), 기술(TRM) 표준 분류 체계
- **EAMS(Enterprise Architecture Management System)**: 아키텍처 산출물을 등록·저장하고 신규 사업의 적합성을 심의하는 전사 포털 시스템
- **Living Architecture as Code**: 정적 문서 중심의 EA를 탈피하여 IaC 코드와 API 카탈로그를 실시간 크롤링해 현행화하는 현대적 아키텍처 체계

</details>

## 예상문제

> 전사적 아키텍처인 EA/ITA(Enterprise Architecture/Information Technology Architecture)의 개념, 기본모델·참조모델·관리체계의 3대 구성요소, 범정부 5대 참조모델의 특성, 클라우드 및 MSA 환경에서의 실무적 진화 방향을 설명하시오. (25점)

## Ⅰ. 비즈니스와 IT의 통합 청사진, EA/ITA의 개요

> 사일로(Silo) 시스템의 중복 투자를 방지하고, **비즈니스(BA)**부터 **인프라(TA)**까지 전사 자원의 **상호운용성(Interoperability)**을 보장함.

- 정의: 조직의 경영 목표를 지원하기 위해 비즈니스 구조(BA), 데이터(DA), 애플리케이션(AA), 기술 인프라(TA), 보안(SA) 간의 유기적 관계를 체계화하고 **As-Is**에서 **To-Be**로의 이행 경로를 제시하는 **전사 종합 아키텍처 프레임워크**
- 목적: 중복 투자 제거, 상호운용성 확보 및 표준 기반 IT 거버넌스 확립

## Ⅱ. EA/ITA 3대 구성 축 및 4단계 이행 방법론

> 전사 청사진 수립에서 표준 참조모델 매핑, 이행 로드맵 도출, EAMS 거버넌스로 이어지는 파이프라인을 가동함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="EA/ITA 4단계 이행 방법론 및 산출물">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>① EA 방향 및 원칙 수립</strong><span>기업 비전 연계 아키텍처 원칙(재사용, 연계성, 표준화) 정의 → EA 헌장 · 프레임워크 정의서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>② 5대 도메인 모델링 (As-Is / To-Be)</strong><span>BA(업무), DA(데이터), AA(응용), TA(기술), SA(보안) 뷰 설계 → 현행 및 목표 아키텍처 모델링 명세서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>③ 갭 분석 및 정보화 이행 로드맵</strong><span>현행-목표 간 아키텍처 갭(Gap) 식별, 우선순위별 프로젝트 도출 → 갭 분석서 · 중장기 정보화 이행 로드맵</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>④ 거버넌스 및 EAMS 운영</strong><span>신규 정보화 사업 기획 시 EAMS 내 기술 표준 적합성 사전 심의 → 아키텍처 적합성 검토서 · EAMS 저장소</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>아키텍처 정렬</strong></span> · 비즈니스 목표 ↔ 5대 뷰(BA/DA/AA/TA/SA) ↔ 5대 참조모델 ↔ EAMS 적합성 100% 매핑</div>

### EA/ITA 3대 핵심 구성 축

| 핵심 구성 축 | 세부 구성 요소 | 주요 역할 및 가치 |
|---|---|---|
| **1. 아키텍처 모델** | **5대 아키텍처 뷰 (BA, DA, AA, TA, SA)**<br>- As-Is(현행), To-Be(목표), Transition Plan(이행계획) | 전사 비즈니스와 IT 자원의 현재 상태와 미래 목표를 시각화한 구조적 설계도 |
| **2. 참조 모델** | **범정부 5대 참조모델 (PRM, BRM, DRM, ARM, TRM)** | 조직 간 공통 언어와 표준 분류 체계를 제공하여 벤치마킹과 공통 컴포넌트 재사용 촉진 |
| **3. 아키텍처 관리체계** | **조직, 프로세스, 시스템**<br>- 아키텍처 위원회, 적합성 심의 프로세스, EAMS 시스템 | 신규 IT 투자 시 표준 준수를 강제하고 시스템 변경 사항을 상시 현행화하는 통제 기구 |

## Ⅲ. 범정부 5대 참조모델(Reference Model) 체계

> 성과부터 업무, 데이터, 서비스, 기술로 하향 전개되는 계층적 표준화 분류 프레임워크를 제공함.

| 참조모델 | 영문 명칭 | 정의 및 핵심 관리 내용 | 상호 연계 역할 |
|---|---|---|---|
| **PRM** | Performance Reference Model | 정보화 투자의 투입, 프로세스, 산출, 최종 비즈니스 효과를 계량화하는 성과 지표 체계 | BRM 업무의 성공 여부를 측정 |
| **BRM** | Business Reference Model | 정부 및 기업의 조직 구조와 무관하게 수행하는 모든 업무 기능을 계층적으로 표준화한 체계 | DRM 데이터와 ARM 서비스의 기준점 |
| **DRM** | Data Reference Model | 기관 간 데이터 공유 및 상호운용을 위한 공통 데이터 분류, 표준 용어·코드, 메타데이터 체계 | 업무(BRM) 간 데이터 교환 매개 |
| **ARM** | Application Reference Model | 독립적으로 수행 가능한 업무 소프트웨어 기능 및 공통 응용 서비스 컴포넌트 분류 체계 | 데이터(DRM)를 처리하는 서비스 모듈 |
| **TRM** | Technical Reference Model | 정보시스템 구축 시 사용 가능한 기술 표준, 통신 프로토콜, 소프트웨어 솔루션 표준 프로파일 | 서비스(ARM)를 구동하는 인프라 표준 |

## Ⅳ. 전사 아키텍처(EA) vs 솔루션 아키텍처(SA) 비교

> EA는 전사적 중복 방지와 표준화의 거시 청사진이며, SA는 단위 프로젝트의 성공적 구현 설계임.

| 비교 항목 | 전사 아키텍처 (EA, Enterprise Architecture) | 솔루션 아키텍처 (SA, Solution Architecture) |
|---|---|---|
| **조망 관점** | 전사적(Enterprise-wide) 거시적 전체 조망 | 단일 시스템 또는 특정 프로젝트 미시적 조망 |
| **핵심 목적** | IT 투자 효율화, 중복 방지, 전사 표준화, 상호운용성 | 비즈니스 요구 기능의 성공적 구현, 시스템 성능 최적화 |
| **시간 축** | 중장기적(3~5년) 비전 및 단계적 이행 로드맵 | 프로젝트 구축 기간 및 단기 운영 릴리즈 주기 |
| **표준 강제력** | 전사 아키텍처 원칙 및 기술 참조모델(TRM) 표준 제정 | EA가 정한 표준 프로파일 준수 하에 기술 스택 선정 |
| **주요 역할자** | Chief Enterprise Architect, 전사 IT 거버넌스 조직 | Lead Solution Architect, 시스템 엔지니어 |

## Ⅴ. 현대적 EA 거버넌스 진화를 위한 기술사적 제언

> 캐비닛 속의 '죽은 EA 문서'를 탈피하고 클라우드 IaC와 API 카탈로그를 실시간 연동하는 Living Architecture로 진화해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: EA/ITA가 현업에서 외면받은 가장 큰 이유는 수백 페이지의 아키텍처 문서를 수작업으로 작성하여 '잉크가 마르기도 전에 현실과 괴리되는 죽은 문서화'에 빠졌기 때문임. 클라우드와 MSA 환경에서 아키텍처는 문서가 아니라 '살아 숨 쉬는 코드'여야 함.
- 나라면: 과거의 하향식 문서 입력형 EAMS를 전면 개편하여, 개발자의 Git 리포지토리, 테라폼(IaC) 구성 파일, API 게이트웨이 라우팅 정보를 자동으로 크롤링하여 전사 아키텍처 토폴로지를 실시간 렌더링하는 'Living Architecture as Code' 플랫폼을 구축하고, 신규 프로젝트 예산 편성 시 아키텍처 API 재사용률을 핵심 평가지표로 의무화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 정적 문서 중심의 사후 관리에서 코드 기반 실시간 동적 아키텍처 거버넌스로 전환
- 대안: **Living Architecture as Code 플랫폼 구축** 및 **신규 사업 예산 심의 연계**
- 검증: 아키텍처 자동 현행화율 100% · 공통 API 컴포넌트 재사용률 40% 이상 달성
- 효과: IT 자원 중복 개발 원천 차단 · 클라우드 네이티브 환경의 민첩한 비즈니스 적응력 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="EA/ITA 현대화 및 실효성 확보를 위한 기술사적 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>현행 한계</strong><span>수작업 문서 갱신 부담 · 프로젝트 종료 후 방치되는 죽은 EA</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>개선 대안</strong><span>Git/IaC/API 게이트웨이 실시간 크롤링 기반 Living Architecture</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>검증 기준</strong><span>신규 사업 예산 편성 시 EAMS 적합성 및 TRM 준수 검증 100%</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <div class="itpe-step-detail"><strong>실행 효과</strong><span>중복 투자 제로화 · 전사 데이터 및 서비스 상호운용성 극대화</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 비즈니스(BA), 데이터(DA), 응용(AA), 기술(TA), 보안(SA) 간의 유기적 관계를 체계화하여 중복 투자를 방지하고 상호운용성을 극대화하는 **전사 종합 아키텍처 관리 체계**
- 목적: 사일로화 방지 및 표준 기반 IT 거버넌스 확립 통한 비즈니스 전략 정합성 달성

### 2. 구성체계 및 3대 축

<div class="itpe-pipeline is-vertical" role="img" aria-label="EA/ITA 3대 구성 축 요약">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>아키텍처 모델</strong><span>5대 뷰(BA/DA/AA/TA/SA) · As-Is / To-Be</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>5대 참조모델</strong><span>PRM(성과) · BRM(업무) · DRM(데이터) · ARM(서비스) · TRM(기술)</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>관리체계</strong><span>아키텍처 위원회 · EAMS 적합성 심의</span></div></div>
</div>

### 3. 핵심 통제

- **참조모델 정렬**: 범정부 5대 참조모델 준수를 통한 기관 간 공통 서비스 재사용 및 데이터 연계
- **Living Architecture**: 클라우드 IaC 및 API 카탈로그 자동 연동을 통한 아키텍처 상시 현행화

## 출제 이력과 검증 출처

- 제119회, 제81회, 제80회 KPC 기출: 전사 아키텍처(EA)의 구성요소 및 참조모델 연계
- [행정안전부, 범정부 정보기술아키텍처(EA) 구축 및 운영 가이드라인](https://www.mois.go.kr)
- [The Open Group, TOGAF Standard 10th Edition](https://www.opengroup.org)

## 학습 체크

- [ ] EA/ITA의 3대 핵심 구성 축(아키텍처 모델, 참조모델, 관리체계)을 설명할 수 있는가?
- [ ] 범정부 5대 참조모델(PRM, BRM, DRM, ARM, TRM)의 정의와 상호 연계 구조를 도식화할 수 있는가?
- [ ] Living Architecture as Code 관점에서 현대적 EA 발전 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [품질비용(Cost of Quality)](./106_cost_of_quality_coq.md)
- 연관 토픽: [ISP(정보전략계획)](./003_isp.md), [ISMP(정보시스템마스터플랜)](./001_ismp.md)
- 다음 토픽: [프로그래머블 머니 (AI 에이전트의 경제 주체화)](./110_programmable_money_ai_agents.md)
