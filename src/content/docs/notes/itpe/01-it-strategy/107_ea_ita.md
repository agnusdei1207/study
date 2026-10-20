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

## Ⅱ. EA·ITA의 특징

- 핵심 요약 : 4대 아키텍처 뷰 분해와 참조모델 기반 표준화, As-Is·To-Be 갭 분석을 통한 이행 관리.

1. 4대 아키텍처 뷰 분해 : BA(Business Architecture), DA(Data Architecture), AA(Application Architecture), TA(Technology Architecture)로 계층적 분해.
2. 참조모델(Reference Model) 기반 표준화 : PRM, BRM, SRM, DRM, TRM 5개 참조모델로 표준 체계 구축.
3. As-Is·To-Be 갭(Gap) 분석 : 현재 아키텍처와 목표 아키텍처 간 차이를 분석하여 이행 계획 도출.
4. 법적 의무화 : 클링거-코헨 법, 전자정부법 등 공공 부문 EA 도입 법적 근거 보유.
5. 전사 라이프사이클 거버넌스 : 신규 시스템 도입 시 EA 정합성 검토를 통한 통제.

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

## Ⅴ. EA·ITA 추진의 장점과 한계

- 핵심 요약 : 전사적 표준화와 중복 투자 방지의 장점, 선반용 아키텍처화와 형상 불일치의 한계.

- 장점
  1. 정보시스템의 전사적 표준화와 상호운용성 확보.
  2. 중복 투자 방지와 정보자원의 효율적 관리.
  3. 비즈니스 전략과 IT 전략의 정렬(Alignment) 가능.

- 한계점 1 : 방대한 문서화로 인한 선반용 아키텍처화
  - 한계점 : 4대 아키텍처(BA, DA, AA, TA) 매트릭스 산출물 작성을 위한 작업에만 매몰되어 구축 후 실무 활용 없이 방치.
  - 해결 방안 : 최소 실행 가능 EA(Lightweight/Agile EA) 지향, 산출물 수량 축소 및 핵심 의사결정 원칙 중심으로 재편.

- 한계점 2 : 현행 시스템과의 형상 불일치(Drift) 지속
  - 한계점 : 신규 프로젝트가 긴급하게 추진되면서 EA 등록 없이 시스템이 배포되어 To-Be 모델과 실제 아키텍처 간 괴리 심화.
  - 해결 방안 : CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인 및 클라우드 프로비저닝 시 EAM(Enterprise Architecture Management) 시스템과 형상 자동 동기화.

- 한계점 3 : 아키텍처 거버넌스의 실행 통제력 부재
  - 한계점 : 아키텍처 원칙 준수 여부를 강제할 수 있는 조직적 권한(ARB, Architecture Review Board)이 없어 부서별 임의 기술 스택 도입 난립.
  - 해결 방안 : IT 투자 심의 및 감리 단계에서 EA 정합성 검토 의무화, 표준 준수 시 사업 승인 패스트트랙(Fast-track) 제공.

## Ⅵ. 현대적 EA의 실효적 발전을 위한 기술사적 제언

- 핵심 요약 : 살아있는 아키텍처로 전환, 디지털 플랫폼 정부 허브 연계, 클라우드 네이티브 수용.

- 정적 산출물 문서에서 살아있는 아키텍처(Living Architecture)로 전환 : 보고용 캐비닛 문서로 사장되는 과거 관행을 극복하기 위해 클라우드 리소스 및 API(Application Programming Interface)와 실시간 동기화되는 자동화된 메타데이터 카탈로그 구축.
- 공공 디지털 플랫폼 정부(DPG, Digital Platform Government) 허브와의 연계 : 부처별 사일로를 타파하고 범정부 데이터 레이크 및 공통 서비스를 재사용할 수 있도록 SOA(Service-Oriented Architecture) 및 오픈 API 거버넌스 확립.
- 클라우드 네이티브 및 MSA(Microservice Architecture) 아키텍처 수용 : 거대하고 경직된 전통적 EA 프레임워크를 탈피하여 분산된 도메인별 자율성을 보장하면서 전사 보안 및 통신 표준만 통제하는 가벼운 EA(Lightweight EA) 지향.

## Ⅶ. 결론

- 핵심 요약 : EA·ITA는 4대 아키텍처 뷰와 5개 참조모델로 전사 표준화를 달성하되 실무 활용과 자동 동기화가 관건.
- 요약 : EA·ITA는 조직의 비즈니스 비전 달성을 위해 업무, 데이터, 애플리케이션, 기술 인프라 간 상호 관계를 종합 조망하고 표준화된 아키텍처 기준선을 수립·관리하는 전사적 아키텍처 체계.
- 시사점 : 살아있는 아키텍처로 전환, 디지털 플랫폼 정부 허브 연계, 클라우드 네이티브 수용을 통해 실효성 확보 필요.
