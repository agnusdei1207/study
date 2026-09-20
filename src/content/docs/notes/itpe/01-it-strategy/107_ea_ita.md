---
title: "EA·ITA"
author: "OpenAI Codex"
date: "2026-09-22T10:45:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
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

## Ⅲ. 범정부 EA 참조모형

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

> **[핵심 통찰]** EA의 품질은 모델 개수가 아니라 투자·변경 의사결정을 얼마나 일관되게 바꾸는가로 판단해야 함.

> **나라면** 신규사업 심의 시 원칙·재사용·데이터·기술표준의 준수·예외를 기록하고, 운영 자산과 EAMS 차이를 주기적으로 검증해 현행화를 최소비용으로 유지하겠음.

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

- 이전: [106. 품질비용](./106_cost_of_quality_coq/)
- 관련: [003. ISP](./003_isp/) · [001. ISMP](./001_ismp/)
- 다음: [110. Programmable Money·AI Agent](./110_programmable_money_ai_agents/)
