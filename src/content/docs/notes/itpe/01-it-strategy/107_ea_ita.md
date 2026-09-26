---
title: "EA·ITA"
author: "Codex"
date: "2026-09-27T00:24:59+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "서브"
extra:
  model: "GPT-6"
  keyword_grade: "서브"
---

## 지식 로드맵 내 현재 위치
현재 위치: IT 전략·관리 → **EA** ·ITA


## 30초 인출

- 본질: **EA·ITA** 는 조직의 업무·데이터·응용·기술 구조를 전사 관점에서 정리·관리하는 아키텍처
- 메커니즘: 현행·목표 구조의 비교를 통한 차이 식별과 이행과제·관리기준 설정

<details>
<summary>핵심 용어</summary>

- **EA·ITA** : 조직의 업무·데이터·응용·기술 구조를 전사 관점에서 정리·관리하는 정보기술 아키텍처
- **EA(Enterprise Architecture)** : 경영 전략과 비즈니스·데이터·응용·기술 인프라 간의 관계를 전사 관점에서 설계·통제하는 종합 청사진
- **ITA(Information Technology Architecture)** : 정보화 자원을 체계적으로 기획·도입·운영하기 위한 공공 부문 정보기술 아키텍처
- **EAMS(Enterprise Architecture Management System)** : 전사 아키텍처 메타모델과 산출물 정보를 등록·검색·활용하는 관리 시스템
- **Gap 분석(Gap Analysis)** : 현행(As-Is)과 목표(To-Be) 아키텍처 간의 격차를 식별하여 전환 이행 과제를 도출하는 분석 기법
- **Reference Model** : 기관 간 아키텍처 연계와 컴포넌트 재사용을 지원하는 표준 참조 모형 체계(PRM·BRM·SRM·DRM·TRM)
- **PRM(Performance Reference Model)** : 정보화 성과의 분류와 측정을 돕는 성과 참조모형
- **BRM(Business Reference Model)** : 업무기능을 공통 기준으로 분류하는 업무 참조모형
- **SRM(Service Reference Model)** : 서비스·응용 컴포넌트의 분류와 재사용을 돕는 서비스 참조모형
- **DRM(Data Reference Model)** : 데이터의 분류·구조·교환·관리 기준을 나타내는 데이터 참조모형
- **TRM(Technical Reference Model)** : 기술 구성과 표준을 분류하는 기술 참조모형

</details>

---

## 1교시 예상문제 (10점)

> EA·ITA의 개념과 구성체계에 관하여 설명하시오. (예상·10점)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **EA·ITA** 는 조직의 업무·데이터·응용·기술 구조를 전사 관점에서 정리·관리하는 아키텍처 |
| 목적 | 중복 투자 감소와 정보자원 간 일관성·상호운용성 향상 |

### Ⅱ. 참조모형과 아키텍처 뷰

```text
기관의 EA 아키텍처 뷰
    ├─ 업무 ↔ BRM: 업무 참조
    ├─ 데이터 ↔ DRM: 데이터 참조
    ├─ 응용 ↔ SRM: 서비스 참조
    └─ 기술 ↔ TRM: 기술 참조

PRM: 각 뷰의 성과 연결·측정
```

### Ⅲ. 핵심 통제

| 축 | 핵심 통제 방안 |
|---|---|
| **아키텍처** | 업무·데이터·응용·기술의 현행과 목표 구조를 일관된 기준으로 작성 |
| **이행** | **Gap 분석** 결과를 이행과제·우선순위와 연결 |
| **관리** | 사업 변경 때 관련 아키텍처 정보를 갱신하고 준수 여부 검토 |

제언: 주요 투자·사업 심의에 EA 원칙 준수 여부와 예외 사유의 공동 검토를 포함

---

## 2~4교시 예상문제 (25점)

> **(예상·25점)** EA·ITA의 개념·구성체계·수립 및 관리방안을 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. EA·ITA 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **EA·ITA** 는 조직의 업무·데이터·응용·기술 구조를 전사 관점에서 정리·관리하는 아키텍처 |
| 목적 | 중복 투자 감소와 정보자원 간 일관성·상호운용성 향상 |

## Ⅱ. 구성체계·수립절차

| 구성 | 핵심 | 산출 |
|---|---|---|
| 방향 | 비전·원칙·범위·Framework | **EA** 원칙·메타모델 |
| Architecture | 업무·데이터·응용·기술의 As-Is·To-Be | 현행·목표 모델 |
| 이행 | Gap·과제·우선순위·의존성 | Transition Plan |
| 관리 | 조직·절차· **EAMS** ·성과 | 적합성 검토·현행화 기록 |

```text
EA 방향·원칙 설정
    ↓
현행·목표 아키텍처 모델링
    ↓
차이 분석·이행계획
    ↓
자산 관리·투자 의사결정 활용
```

## Ⅲ. 범정부 EA 참조모형 및 4대 아키텍처 연계

```text
기관의 EA 아키텍처 뷰
    ├─ 업무 ↔ BRM: 업무 참조
    ├─ 데이터 ↔ DRM: 데이터 참조
    ├─ 응용 ↔ SRM: 서비스 참조
    └─ 기술 ↔ TRM: 기술 참조

PRM: 각 뷰의 성과 연결·측정
```

| 모형 | 역할 |
|---|---|
| **PRM** (Performance Reference Model) | 정보화 성과 분류·측정 |
| **BRM** (Business Reference Model) | 조직 독립적 업무기능 분류 |
| **SRM** (Service Reference Model) | 응용서비스·컴포넌트 분류·재사용 |
| **DRM** (Data Reference Model) | 데이터 분류·구조·교환·관리 |
| **TRM** (Technical Reference Model) | 기술·표준 분류 |

참조모형의 역할은 기관 아키텍처의 관점별 분류·비교 지원. **PRM** 은 성과 관점의 모형이며 다른 모형과의 일대일 대응은 전제하지 않는 구조.

## Ⅳ. EA·Solution Architecture 비교

| 기준 | **EA** | Solution Architecture |
|---|---|---|
| 범위 | 전사·기관 | 단위 사업·시스템 |
| 관심 | 전략정렬·표준·포트폴리오 | 요구사항·구조·품질속성 |
| 산출 | 원칙·Reference Model·Roadmap | Solution 구조·Interface·기술선택 |
| 관계 | 원칙·표준·예외 통제 제공 | **EA** 준수·예외 요청·구현 피드백 |

## Ⅴ. 한계·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 문서화 자체가 목적 | 투자·사업·평가 Gate와 연계 | 활용성 확보 |
| 현행정보 노후화 | 변경절차·자산정보 자동연계 | 최신성 향상 |
| 상세도 과다 | 의사결정별 최소 산출물 | 관리비용 절감 |
| 표준 경직성 | 예외 승인·기한·회수 절차 | 혁신·통제 균형 |

## Ⅵ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 담당자의 기억에 의존하는 현행화로 인한 투자 심의 기준정보의 노후화 | 시스템 변경·사업 종료 절차에 아키텍처 갱신 책임과 확인 시점을 포함 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [전자정부법 제46조, 기관별 정보기술아키텍처 도입·운영](https://law.go.kr/lsLinkCommonInfo.do?lsJoLnkSeq=1018863537)
- [정보기술아키텍처 도입·운영 지침](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000244120)
- [행정안전부, 범정부 **EA** 참조모형 개정안](https://www.mois.go.kr/frt/bbs/type001/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000045&nttId=34410)
- [The Open Group, TOGAF Standard](https://www.opengroup.org/togaf)

## 연결 토픽

- 이전: [106. 품질비용](./106_cost_of_quality_coq.md)
- 관련: [003. ISP](./003_isp.md) · [001. ISMP](./001_ismp.md)
- 다음: [110. Programmable Money·AI Agent](./110_programmable_money_ai_agents.md)
