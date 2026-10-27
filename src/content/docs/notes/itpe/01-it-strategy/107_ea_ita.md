---
title: "EA·ITA (EA: Enterprise Architecture; ITA: Information Technology Architecture)"
author: "agnusdei1207"
date: "2026-10-24T23:53:59+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "107"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- EA(Enterprise Architecture, 전사 아키텍처), ITA(Information Technology Architecture)
- BA(Business Architecture), DA(Data Architecture), AA(Application Architecture), TA(Technology Architecture)
- 클링거-코헨 법(Clinger-Cohen Act), 전자정부법
- 성과참조모델(PRM, Performance Reference Model), 업무참조모델(BRM, Business Reference Model)
- 서비스참조모델(SRM, Service Reference Model), 데이터참조모델(DRM, Data Reference Model)
- 기술참조모델(TRM, Technology Reference Model), 갭(Gap) 분석
- EAM(Enterprise Architecture Management), ARB(Architecture Review Board)

## Ⅰ. EA·ITA의 개요

- 핵심 요약 : 업무, 데이터, 애플리케이션, 기술 인프라의 관계를 전사 차원에서 조망하고 아키텍처 기준선을 세워 관리하는 체계.
- 개념 : 조직의 비즈니스 비전과 전략을 달성하도록 업무, 데이터, 응용, 기술 인프라 등 정보화 구성요소의 상호 관계를 종합적으로 조망하고, 표준화된 아키텍처 기준선을 수립·관리하는 **전사 아키텍처** (EA, Enterprise Architecture)와 그 하위 정보기술 관점의 **정보기술 아키텍처** (ITA, Information Technology Architecture) 체계.
- 배경 및 필요성 : 정보시스템이 부서별로 무분별하게 도입되면 전사 비효율, 시스템 간 데이터 연계의 어려움, 중복 투자가 생긴다. 이를 막기 위해 미국은 클링거-코헨 법(Clinger-Cohen Act)으로 정보기술 투자의 관리 체계를 법제화했고, 한국은 전자정부법에 근거해 공공 부문의 아키텍처 수립을 요구한다.
- 주요 목적 : 비즈니스와 IT의 전략적 정렬, 정보자원의 상호운용성 확보, 중복 투자 방지, 정보시스템 생애주기 거버넌스 확립.

## Ⅱ. EA·ITA의 특징 및 장점

- 핵심 요약 : 4대 아키텍처와 참조모델로 정보자원을 함께 조망해 정렬, 재사용, 중복 투자 방지에 기여한다.

1. BA·DA·AA·TA 분해 : 업무부터 기술까지의 연결 관계를 한 장에서 보여줌 → 변경의 전사적 영향 분석 가능.
2. 참조모델 표준화 : PRM, BRM, SRM, DRM, TRM으로 공통 분류 기준 제공 → 시스템 간 상호운용성 향상.
3. As-Is/To-Be 갭 분석 : 현행과 목표의 차이를 구체화 → 단계별 이행 계획 수립.
4. 정보자원 목록화 : 중복 시스템과 공통 서비스 식별 → 재사용과 투자 효율 향상.
5. 정합성 검토 : 신규 사업을 아키텍처 원칙에 비추어 판단 → 비즈니스와 IT의 정렬 유지.

## Ⅲ. EA·ITA의 구조 (흐름)

- 핵심 요약 : 비즈니스, 데이터, 응용, 기술의 4대 아키텍처가 위에서 아래로 계층을 이루고, 갭 분석으로 이행 계획을 도출하는 구조.
- EA 4대 아키텍처 뷰는 상위 업무 목표가 하위 기술 선택을 규정하는 계층으로 연결된다.

```text
[ 비즈니스 아키텍처 (BA) ]
  경영 목표, 업무 프로세스, 조직 기능
      ↓
[ 데이터 아키텍처 (DA) ]
  전사 데이터 모델 (개념·논리·물리)
  데이터 표준, 데이터 흐름
      ↓
[ 응용 아키텍처 (AA) ]
  업무를 지원하는 소프트웨어 컴포넌트
  서비스 구조, 인터페이스
      ↓
[ 기술 아키텍처 (TA) ]
  HW, NW, OS, 미들웨어, 보안 인프라
  기술 표준과 기술참조모델 (TRM)
```

```text
[ As-Is 아키텍처 ]
      ↓
  갭 (Gap) 분석
      ↓
[ To-Be 아키텍처 ]
      ↓
  전사 이행 계획 (Transition Plan)
```

- **갭 분석** (Gap Analysis, 현행과 목표 아키텍처의 차이를 찾는 분석): 차이의 크기와 우선순위로 단계별 이행 계획을 도출하는 과정.
- **참조모델** (Reference Model, 공통 분류 기준을 정한 표준 모델): 범정부 EA에서 업무·서비스·데이터·기술을 같은 언어로 분류하게 하는 장치.

## Ⅳ. 범정부 EA 5대 참조모델의 비교

- 핵심 요약 : 성과, 업무, 서비스, 데이터, 기술 5개 참조모델이 각각 표준화하는 대상이 다르다.

| 참조모델 | 영문 약어 | 표준화 대상 |
| --- | --- | --- |
| 성과참조모델 (Performance Reference Model) | PRM | 정보화 사업의 성과 측정 지표와 비즈니스 기여도 평가 기준 |
| 업무참조모델 (Business Reference Model) | BRM | 정부와 공공기관의 업무 기능을 기관 독립적으로 분류 |
| 서비스참조모델 (Service Reference Model) | SRM | 업무를 지원하는 공통 응용 서비스 컴포넌트의 기능 분류 |
| 데이터참조모델 (Data Reference Model) | DRM | 전사 데이터 상호운용을 위한 표준 단어, 용어, 도메인 |
| 기술참조모델 (Technology Reference Model) | TRM | 정보 인프라를 구성하는 소프트웨어와 하드웨어 기술 분류 |

## Ⅴ. EA·ITA 추진의 한계와 방안

- 핵심 요약 : 문서화 과잉, 실제 구성과의 괴리, 실행 권한 부족을 경량 운영, 자동 동기화, 심의 연계로 해결한다.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 산출물 작성이 목적이 되는 **선반용 EA** | 보고서만 쌓이고 의사결정에 쓰이지 않음 | 핵심 의사결정에 쓰는 모델과 원칙부터 유지하는 경량 EA 적용 | 의사결정 반영 건수 |
| 신규 시스템 반영 지연에 따른 **드리프트** (Drift) | 실제 구성과 모델이 어긋나 아키텍처 신뢰도 하락 | 배포와 자원 변경 절차를 EAM 등록과 연결하고 변경 이력을 정기 검증 | 모델과 실제 구성의 불일치 건수 |
| **ARB** (Architecture Review Board, 아키텍처 검토 위원회)의 권한 약화 | 부서별 임의 기술 도입 확산 | 투자 심의와 설계 검토에 EA 정합성 기준을 포함하고 예외 승인 절차 운영 | 예외 승인 건수 |

## Ⅵ. 현대적 EA의 실효적 발전을 위한 기술사적 제언

- 핵심 요약 : EA를 살아 있는 아키텍처로 바꾸고, 디지털플랫폼정부 체계와 연계하며, 클라우드 네이티브 원칙을 수용하는 것이 발전의 방향이다.

1. 살아 있는 아키텍처로의 전환 : 보고용 문서로 머물던 EA를 클라우드 자원과 **API** (Application Programming Interface)의 현황과 동기화되는 메타데이터 카탈로그로 운영하여 모델이 실제 구성을 따라가게 한다.
2. 디지털플랫폼정부와의 연계 : 2023년 4월 발표된 디지털플랫폼정부 실현계획의 방향에 맞추어, 부처별로 나뉜 서비스를 공통 서비스로 재사용할 수 있도록 **SOA** (Service-Oriented Architecture, 서비스 지향 아키텍처)와 개방형 API 거버넌스를 확립한다.
3. 클라우드 네이티브 원칙 수용 : 거대하고 경직된 프레임워크 대신, 도메인별 자율성을 보장하는 **MSA** (Microservice Architecture)를 전제로 전사 보안과 통신 표준만 통제하는 **경량 EA** (Lightweight EA)를 지향한다.

## Ⅶ. 결론

- 핵심 요약 : EA·ITA는 4대 아키텍처 뷰와 5개 참조모델로 전사 표준화를 달성하는 체계이며, 실무 활용과 자동 동기화가 성패를 가른다.
- 시사점 : 아키텍처는 문서가 아니라 실제 구성과 함께 살아 움직여야 가치가 있으므로, 기준선 관리가 투자 심의에 연결되어야 한다.