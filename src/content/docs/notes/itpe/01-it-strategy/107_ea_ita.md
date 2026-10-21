---
title: "EA·ITA (EA: Enterprise Architecture; ITA: Information Technology Architecture)"
author: "agnusdei1207"
date: "2026-10-01T22:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "LongCat 2.5 Preview Free"
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

- 핵심 요약 : 조직의 비즈니스 비전 달성을 위해 업무·데이터·애플리케이션·기술 인프라 간 상호 관계를 종합 조망하고 표준화된 아키텍처 기준선을 수립·관리하는 전사적 아키텍처 체계.
- 개념 : 조직의 비즈니스 비전과 전략을 달성하기 위해 업무, 데이터, 애플리케이션, 기술 인프라 등 전사 정보화 구성요소 간의 상호 관계를 종합적으로 조망하고 표준화된 아키텍처 기준선을 수립·관리하는 전사적 아키텍처(EA·ITA) 체계.
- 배경 및 필요성 : 정보시스템의 무분별한 개별 도입으로 인한 전사적 비효율, 시스템 간 데이터 연계 곤란, 중복 투자를 방지하기 위해 미국 클링거-코헨 법(Clinger-Cohen Act) 및 한국 전자정부법 상 공공 EA 도입 의무화.
- 주요 목적 : 비즈니스와 IT(Information Technology)의 전략적 정렬, 정보자원의 상호운용성 확보, 중복 투자 방지 및 정보시스템 라이프사이클 거버넌스 확립.

## Ⅱ. EA·ITA의 특징 및 장점

- 핵심 요약 : **4대 아키텍처**와 참조모델로 정보자원을 함께 조망하여 정렬·재사용·중복 투자 방지에 기여한다.

1. **BA·DA·AA·TA 분해** : 업무부터 기술까지 연결 관계를 보여 **전사적 영향 분석**을 돕는다.
2. **참조모델 표준화** : PRM·BRM·SRM·DRM·TRM으로 공통 분류 기준을 제공하여 **상호운용성**을 높인다.
3. **As-Is/To-Be 갭 분석** : 현행과 목표의 차이를 구체화하여 **단계별 이행 계획**을 수립한다.
4. **정보자원 목록화** : 중복 시스템과 공통 서비스를 식별하여 **재사용·투자 효율**을 높인다.
5. **정합성 검토** : 신규 사업을 아키텍처 원칙에 비추어 판단하여 **비즈니스·IT 정렬**을 유지한다.

## Ⅲ. EA·ITA의 구조 (흐름)

- 핵심 요약 : 비즈니스→데이터→응용→기술 4대 아키텍처 뷰의 계층적 구조와 갭 분석 기반 이행 체계.
- EA 4대 아키텍처 뷰의 계층 구조.

```text
[비즈니스 아키텍처 (BA)]
   조직의 경영 목표, 업무 프로세스, 조직 기능 정의
          ↓
[데이터 아키텍처 (DA)]
   전사 데이터 모델(개념/논리/물리),
   데이터 표준, 데이터 흐름 정의
          ↓
[응용 아키텍처 (AA)]
   비즈니스를 지원하는 소프트웨어 컴포넌트,
   서비스 구조, 인터페이스
          ↓
[기술 아키텍처 (TA)]
   하드웨어(HW), 네트워크(NW), OS, 미들웨어, 보안 인프라
   기술 표준 및 기술참조모델(TRM)
```

```text
[As-Is 아키텍처] ──(갭 분석)──→ [To-Be 아키텍처]
        │                              │
        └────── 전사 이행 계획 ──────────┘
                (Transition Plan)
```

- 아키텍처 매트릭스 : As-Is 아키텍처(현재)와 To-Be 아키텍처(목표) 간의 갭(Gap) 분석을 통해 단계별 전사 이행 계획(Transition Plan) 도출.

## Ⅳ. 범정부 EA 5대 참조모델의 비교

- 핵심 요약 : 성과·업무·서비스·데이터·기술 5개 참조모델의 표준화 대상과 기능 비교.
- 범정부 EA 참조모델(Reference Models)의 대비.

| 참조모델 | 영문 약어 | 핵심 정의 및 표준화 대상 |
|---|---|---|
| 성과참조모델(Performance Reference Model) | PRM | 정보화 사업의 성과 측정 지표 및 비즈니스 기여도 평가 기준 표준화 |
| 업무참조모델(Business Reference Model) | BRM | 정부 기능 및 공공기관의 업무 기능을 기관 독립적으로 분류·정의 |
| 서비스참조모델(Service Reference Model) | SRM | 업무를 지원하는 공통 응용 서비스 컴포넌트의 기능적 분류 및 표준화 |
| 데이터참조모델(Data Reference Model) | DRM | 전사 데이터의 상호운용을 위한 공통 표준 단어, 용어, 도메인 표준화 |
| 기술참조모델(Technology Reference Model) | TRM | 정보 인프라를 구성하는 소프트웨어, 하드웨어 기술 요소의 표준 분류 체계 |

## Ⅴ. EA·ITA 추진의 한계와 방안

- 핵심 요약 : **문서화 과잉**, 현행 구성과의 괴리, 실행 권한 부족을 운영 절차와 자동 갱신으로 해결한다.

| 한계 | 방안 |
|---|---|
| 산출물 작성 자체가 목적이 되면 **선반용 EA**로 방치됨 | 핵심 의사결정에 쓰이는 모델·원칙부터 유지하는 **경량 EA** 적용 |
| 신규 시스템 반영이 늦어 실제 구성과 모델 사이에 **드리프트** 발생 | 배포·자원 변경 절차와 EAM 등록을 연결하고 변경 이력을 정기 검증 |
| ARB의 검토 권한이 약하면 부서별 임의 기술 도입이 확산 | 투자 심의·설계 검토에 **EA 정합성** 기준을 포함하고 예외 승인 절차 마련 |

## Ⅵ. 현대적 EA의 실효적 발전을 위한 기술사적 제언

- 핵심 요약 : 살아있는 아키텍처로 전환, 디지털 플랫폼 정부 허브 연계, 클라우드 네이티브 수용.

- 정적 산출물 문서에서 살아있는 아키텍처(Living Architecture)로 전환 : 보고용 캐비닛 문서로 사장되는 과거 관행을 극복하기 위해 클라우드 리소스 및 API(Application Programming Interface)와 실시간 동기화되는 자동화된 메타데이터 카탈로그 구축.
- 공공 디지털 플랫폼 정부(DPG, Digital Platform Government) 허브와의 연계 : 부처별 사일로를 타파하고 범정부 데이터 레이크 및 공통 서비스를 재사용할 수 있도록 SOA(Service-Oriented Architecture) 및 오픈 API 거버넌스 확립.
- 클라우드 네이티브 및 MSA(Microservice Architecture) 아키텍처 수용 : 거대하고 경직된 전통적 EA 프레임워크를 탈피하여 분산된 도메인별 자율성을 보장하면서 전사 보안 및 통신 표준만 통제하는 가벼운 EA(Lightweight EA) 지향.

## Ⅶ. 결론

- 핵심 요약 : EA·ITA는 4대 아키텍처 뷰와 5개 참조모델로 전사 표준화를 달성하되 실무 활용과 자동 동기화가 관건.
- 요약 : EA·ITA는 조직의 비즈니스 비전 달성을 위해 업무, 데이터, 애플리케이션, 기술 인프라 간 상호 관계를 종합 조망하고 표준화된 아키텍처 기준선을 수립·관리하는 전사적 아키텍처 체계.
- 시사점 : 살아있는 아키텍처로 전환, 디지털 플랫폼 정부 허브 연계, 클라우드 네이티브 수용을 통해 실효성 확보 필요.
