---
title: "EA·ITA"
author: "Antigravity"
date: "2026-09-22T10:45:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 전사 아키텍처를 거쳐 EA와 ITA로 이어지는 위치">
  <span>IT 전략·관리</span><span>전사 Architecture·거버넌스</span><strong>EA·ITA</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 경영전략과 업무·데이터·응용·기술의 관계를 전사 관점에서 구조화
- **메커니즘**: 원칙 → 현행·목표 Architecture → Gap → 이행계획 → 적합성 통제
- **활용**: 정보화 기획·투자·사업·평가에서 표준화·재사용·상호운용성 확보

<div class="itpe-svg-map">
<svg viewBox="0 0 760 530" role="img" aria-label="전사 아키텍처 구조와 관리체계">
  <rect x="250" y="25" width="260" height="80" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="58" text-anchor="middle" class="itpe-svg-title">경영전략·Architecture 원칙</text>
  <text x="380" y="86" text-anchor="middle" class="itpe-svg-sub">방향·의사결정 기준</text>
  <rect x="45" y="185" width="200" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="145" y="222" text-anchor="middle" class="itpe-svg-title">현행 Architecture</text><text x="145" y="250" text-anchor="middle" class="itpe-svg-sub">As-Is</text>
  <rect x="280" y="185" width="200" height="90" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="380" y="222" text-anchor="middle" class="itpe-svg-title">목표 Architecture</text><text x="380" y="250" text-anchor="middle" class="itpe-svg-sub">To-Be</text>
  <rect x="515" y="185" width="200" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="615" y="222" text-anchor="middle" class="itpe-svg-title">이행계획</text><text x="615" y="250" text-anchor="middle" class="itpe-svg-sub">Transition Plan</text>
  <rect x="190" y="365" width="380" height="100" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="402" text-anchor="middle" class="itpe-svg-title">관리체계·EAMS</text>
  <text x="380" y="432" text-anchor="middle" class="itpe-svg-sub">현행화·품질·성과·적합성·활용</text>
  <path d="M380 105 L145 185 M380 105 L380 185 M380 105 L615 185 M145 275 L300 365 M380 275 L380 365 M615 275 L460 365" class="itpe-svg-link"></path>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **EA(Enterprise Architecture)**: 조직의 전략·업무와 정보기술 구조·관계를 전사 관점에서 관리하는 체계
- **ITA(Information Technology Architecture)**: 전자정부법에서 사용하는 정보기술아키텍처
- **EAMS(Enterprise Architecture Management System)**: Architecture 정보를 등록·관리·활용하는 시스템
- **Gap Analysis**: 현행과 목표 상태의 차이와 전환과제를 식별하는 분석
- **Reference Model**: 기관 간 공통 분류·표준·재사용을 지원하는 참조모형

</details>

## 예상문제

> **(미출제 예상·25점)** EA·ITA의 개념·구성체계와 범정부 EA 참조모형을 설명하고, 실효성 확보를 위한 문제점·대응책을 제시하시오.

## Ⅰ. EA·ITA 개요

> Architecture 산출물을 만드는 활동이 아니라 정보화 의사결정에 지속 활용하는 관리체계임

- **정의**: 조직의 전략·업무와 데이터·응용·기술의 현행·목표 구조 및 이행계획을 전사적으로 관리하는 체계
- **목적**: 전략 정렬·중복 방지·상호운용성·정보자원 투자 효율성 확보

## Ⅱ. 구성체계·수립절차

| 구성 | 핵심 | 산출 |
|---|---|---|
| 방향 | 비전·원칙·범위·Framework | EA 원칙·메타모델 |
| Architecture | 업무·데이터·응용·기술의 As-Is·To-Be | 현행·목표 모델 |
| 이행 | Gap·과제·우선순위·의존성 | Transition Plan |
| 관리 | 조직·절차·EAMS·성과 | 적합성 검토·현행화 기록 |

<div class="itpe-pipeline is-vertical" role="img" aria-label="EA 수립과 활용 절차">
  <div class="itpe-flow-node"><strong>① 방향·원칙</strong><div class="itpe-step-detail"><strong>활동</strong><span>목표·범위·Framework 정의</span></div><div class="itpe-step-detail"><strong>산출</strong><span>EA 원칙·메타모델</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>② 현행·목표 모델</strong><div class="itpe-step-detail"><strong>활동</strong><span>업무·데이터·응용·기술 구조화</span></div><div class="itpe-step-detail"><strong>산출</strong><span>As-Is·To-Be Architecture</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>③ Gap·이행계획</strong><div class="itpe-step-detail"><strong>활동</strong><span>차이·과제·의존성·우선순위 분석</span></div><div class="itpe-step-detail"><strong>산출</strong><span>Transition Plan</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>④ 관리·활용</strong><div class="itpe-step-detail"><strong>활동</strong><span>현행화·적합성·성과·투자 연계</span></div><div class="itpe-step-detail"><strong>산출</strong><span>EAMS·검토결과·성과정보</span></div></div>
</div>

## Ⅲ. 범정부 EA 참조모형 및 4대 아키텍처 연계

```
[전략/성과] ──────── PRM (성과참조모델) : 정보화 투자효율/달성도 평가
     │
[업무 아키텍처] ─── BRM (업무참조모델) : 비즈니스 기능 독립적 분류 체계
     │
[데이터 아키텍처] ─ DRM (데이터참조모델) : 데이터 분류/표준화/상호운용성
     │
[응용 아키텍처] ─── SRM (서비스참조모델) : 컴포넌트 재사용 및 서비스 연계
     │
[기술 아키텍처] ─── TRM (기술참조모델) : 플랫폼/SW/표준기술 인프라 규격
```

<div class="itpe-svg-map">
<svg viewBox="0 0 520 220" role="img" aria-label="범정부 EA 5대 참조모형과 4대 뷰 연계 메커니즘">
  <!-- 배경 바운더리 -->
  <rect x="10" y="10" width="500" height="200" rx="8" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" />
  
  <!-- 상단: PRM -->
  <rect x="25" y="25" width="470" height="32" rx="6" fill="var(--sl-color-accent-low)" stroke="var(--sl-color-accent)" stroke-width="1.5" />
  <text x="260" y="46" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-accent-high)">PRM (성과참조) : 전략목표 정렬 &amp; IT 투자 성과지표 측정</text>

  <!-- 중앙 4대 아키텍처 & 참조모형 -->
  <!-- BA & BRM -->
  <rect x="25" y="70" width="225" height="38" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="137" y="87" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">BA (비즈니스 아키텍처)</text>
  <text x="137" y="101" text-anchor="middle" font-size="9.5" fill="var(--sl-color-gray-2)">업무기능·프로세스 구조</text>
  <line x1="250" y1="89" x2="270" y2="89" stroke="var(--sl-color-accent)" stroke-width="1.5" />
  <rect x="270" y="70" width="225" height="38" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="382" y="87" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">BRM (업무참조모형)</text>
  <text x="382" y="101" text-anchor="middle" font-size="9.5" fill="var(--sl-color-gray-2)">조직독립적 기능 분류 (재정·국방 등)</text>

  <!-- AA/DA & SRM/DRM -->
  <rect x="25" y="118" width="110" height="42" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="80" y="135" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-text)">DA (데이터)</text>
  <text x="80" y="150" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">DRM 연계 (표준)</text>
  
  <rect x="140" y="118" width="110" height="42" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="195" y="135" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-text)">AA (응용)</text>
  <text x="195" y="150" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">SRM 연계 (컴포넌트)</text>

  <rect x="270" y="118" width="110" height="42" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="325" y="135" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-text)">DRM (데이터참조)</text>
  <text x="325" y="150" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">데이터모델/연계체계</text>

  <rect x="385" y="118" width="110" height="42" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="440" y="135" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-text)">SRM (서비스참조)</text>
  <text x="440" y="150" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">재사용 서비스/API</text>

  <!-- TA & TRM -->
  <rect x="25" y="170" width="225" height="30" rx="5" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="137" y="189" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-text)">TA (기술) ── TRM (기술참조모형)</text>

  <rect x="270" y="170" width="225" height="30" rx="5" fill="var(--sl-color-accent-low)" stroke="var(--sl-color-accent)" stroke-width="1" />
  <text x="382" y="189" text-anchor="middle" font-size="10.5" font-weight="bold" fill="var(--sl-color-accent-high)">EAMS 자동화 현행화 폐루프</text>
</svg>
</div>

| 모형 | 영문 | 역할 |
|---|---|---|
| PRM | Performance Reference Model | 정보화 성과 분류·측정 |
| BRM | Business Reference Model | 조직 독립적 업무기능 분류 |
| SRM | Service Reference Model | 응용서비스·컴포넌트 분류·재사용 |
| DRM | Data Reference Model | 데이터 분류·구조·교환·관리 |
| TRM | Technical Reference Model | 기술·표준 분류 |

## Ⅳ. EA·Solution Architecture 비교

| 기준 | EA | Solution Architecture |
|---|---|---|
| 범위 | 전사·기관 | 단위 사업·시스템 |
| 관심 | 전략정렬·표준·포트폴리오 | 요구사항·구조·품질속성 |
| 산출 | 원칙·Reference Model·Roadmap | Solution 구조·Interface·기술선택 |
| 관계 | 원칙·표준·예외 통제 제공 | EA 준수·예외 요청·구현 피드백 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 문서화 자체가 목적 | 투자·사업·평가 Gate와 연계 | 활용성 확보 |
| 현행정보 노후화 | 변경절차·자산정보 자동연계 | 최신성 향상 |
| 상세도 과다 | 의사결정별 최소 산출물 | 관리비용 절감 |
| 표준 경직성 | 예외 승인·기한·회수 절차 | 혁신·통제 균형 |

## Ⅵ. 결론·기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]** EA의 품질은 모델 개수나 장표 분량이 아니라, 실제 예산 배정·신규 사업 심의·변경 의사결정을 얼마나 일관되고 구속력 있게 통제하는가로 평가되어야 한다.
> 
> **나라면** EAMS를 정적인 문서 저장소가 아닌 '실시간 자산 카탈로그(CI/CD 파이프라인 및 CMDB 연동)'로 전환하여 형상 변경 시 메타데이터가 자동 갱신되도록 구성하고, 아키텍처 적합성 검토를 전자정부 사전협의 필수 게이트로 묶어 무단 표준 위반을 차단하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 정보화 사업 기획 및 예산 편성 시 범정부 EA 5대 참조모형(PRM/BRM/SRM/DRM/TRM) 준수율 95% 이상 달성 여부 및 공통 컴포넌트 재사용 타당성 검토 의무화
- **대응 방안**: EAMS 기반 아키텍처 적합성 검토(Review Gate) 제도화, 예외 승인 시 일몰제(최장 2년) 적용 및 기술부채 대장 등록
- **검증 체계**: 단위 프로젝트 검수 단계 감리 시 As-Is/To-Be 산출물과 형상관리(CMDB/EAMS) 동기화 일치율 전수 실사
- **기대 효과**: 범부처 시스템 중복 투자 방지(연간 예산 15% 절감), 데이터 상호운용성 보장 및 전자정부 서비스 무중단 연계 가속화

<div class="itpe-pipeline is-vertical" role="img" aria-label="EA 활용과 현행화 폐루프">
  <div class="itpe-flow-node"><strong>사업·변경 요청</strong><div class="itpe-step-detail"><strong>입력</strong><span>요구사항·Solution·투자안</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>Architecture Review</strong><div class="itpe-step-detail"><strong>판정</strong><span>준수·예외·재사용</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>구현·운영</strong><div class="itpe-step-detail"><strong>증거</strong><span>자산·API·구성정보</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>EAMS 현행화</strong><div class="itpe-step-detail"><strong>환류</strong><span>모델·표준·예외 갱신</span></div></div>
</div>

## 1교시 10점 답안 발췌

- **정의**: 전략·업무와 데이터·응용·기술의 현행·목표 구조 및 이행계획을 전사적으로 관리하는 체계
- **목적**: 전략 정렬·중복 방지·상호운용성·투자 효율성 확보

| 축 | 핵심 |
|---|---|
| Architecture | As-Is·To-Be |
| Transition | Gap·과제·Roadmap |
| Governance | 현행화·적합성·성과·EAMS |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [전자정부법 제46조, 기관별 정보기술아키텍처 도입·운영](https://www.law.go.kr/법령/전자정부법/제46조)
- [행정안전부, 범정부 EA 참조모형 개정안](https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000045&nttId=34410)
- [The Open Group, TOGAF Standard](https://www.opengroup.org/togaf)

## 학습 체크

- [ ] Ⅰ: EA·ITA의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 방향부터 관리·활용까지 구성·산출을 연결할 수 있는가?
- [ ] Ⅲ: PRM·BRM·SRM·DRM·TRM의 역할을 구분할 수 있는가?
- [ ] Ⅳ: EA와 Solution Architecture의 역할 관계를 비교할 수 있는가?
- [ ] Ⅴ: 문서화·노후화·과다 상세·경직성의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: Review부터 EAMS 현행화까지 폐루프를 그릴 수 있는가?

## 연결 토픽

- 이전: [106. 품질비용](./106_cost_of_quality_coq.md)
- 관련: [003. ISP](./003_isp.md) · [001. ISMP](./001_ismp.md)
- 다음: [110. Programmable Money·AI Agent](./110_programmable_money_ai_agents.md)

