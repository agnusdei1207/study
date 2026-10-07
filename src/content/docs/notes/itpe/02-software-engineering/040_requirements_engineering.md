---
title: "요구공학"
author: "Antigravity"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 요구공학의 개요

- 개념 : 소프트웨어 개발 프로젝트에서 이해관계자의 모호하고 복잡한 요구(Needs)를 체계적으로 발견, 분석, 명세, 검증 및 변경 관리하여 검증 가능한 **요구사항 명세서** (SRS, Software Requirements Specification)로 완성해 나가는 체계적인 공학적 프로세스.
- 배경 및 필요성 : 소프트웨어 결함의 상당수가 요구사항 단계에서 유입되며, 개발 후반부로 갈수록 결함 수정 비용이 지수함수적으로 증가(Boehm의 법칙)하므로 조기 결함 차단 필수.
- 표준 체계 : **ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission)/IEEE(Institute of Electrical and Electronics Engineers) 29148** (요구공학 국제표준).

## Ⅱ. 요구공학의 4대 핵심 프로세스 및 피드백 루프

```text
   [ 요구사항 도출 ] ──> [ 요구사항 분석 ] ──> [ 요구사항 명세 ] ──> [ 요구사항 검증 ]
   (Elicitation)        (Analysis)           (Specification)      (Validation)
    - 인터뷰, 워크숍     - 타당성, 충돌 해결   - SRS 작성           - 인스펙션, 리뷰
    - 프로토타이핑       - DFD(Data Flow Diagram), UML(Unified Modeling Language) 모델링    - 정형/비정형 명세   - 인수 기준 정의
          ▲                                                             │
          └───────────────────── (변경 관리 및 피드백) ────────────────┘
```

- **요구사항 도출 (Elicitation)** : 고객, 사용자, 도메인 전문가 등 이해관계자로부터 잠재된 요구사항을 수집.
- **요구사항 분석 (Analysis)** : 도출된 요구의 모호성, 중복성, 상충(Conflict)을 해결하고 기능적/비기능적 요구로 분류하여 모델링.
- **요구사항 명세 (Specification)** : 정형화된 서식을 통해 구현자와 발주자가 오해 없이 합의할 수 있도록 SRS 작성.
- **요구사항 검증 (Validation)** : 명세서가 사용자의 실제 의도를 반영하고 있는지, 완결성/일관성/검증가능성을 인스펙션을 통해 검토.
- **요구사항 관리 (Management)** : 베이스라인 수립, **변경 통제** (CCB), **요구사항 추적성** (RTM, Requirements Traceability Matrix) 유지.

## Ⅲ. 기능적 요구사항과 비기능적 요구사항의 비교

| 구분 | 기능적 요구사항 (Functional) | 비기능적 요구사항 (Non-Functional) |
|---|---|---|
| 개념 | 시스템이 '무엇(What)'을 수행해야 하는가에 대한 동작 정의 | 시스템이 동작할 때 만족해야 하는 '품질(How Well)' 및 제약조건 |
| 주요 예시 | 결제 승인, 회원가입, 상품 검색, 영수증 출력 | 응답시간(1초 이내), 동시 접속자 수(1만명), 가용성(99.99%), 보안성 |
| 도출 주체 | 주로 현업 비즈니스 사용자, 업무 실무자 | 시스템 아키텍트, 보안 담당자, 인프라 엔지니어 |
| 검증 방식 | 단위/통합/인수 기능 테스트 (Pass/Fail) | 성능/부하 테스트, 스트레스 테스트, 보안성 진단, 가용성 측정 |
| 아키텍처 영향 | 개별 컴포넌트 내부 로직 및 데이터 모델에 영향 | 시스템 전체 아키텍처 스타일 및 인프라 구조를 결정 |

## Ⅳ. 요구공학의 주요 한계점 및 해결 방안

- 요구사항의 불명확성과 지속적인 과업 변경(Scope Creep) :
  - 한계점 : 고객조차 본인이 원하는 시스템의 모습을 명확히 정의하지 못하여 개발 진행 중 지속적으로 요구사항이 변하고, 이는 납기 지연과 개발팀의 피로도로 직결.
  - 해결 방안 : 프로토타이핑(Prototyping) 및 애자일 유저 스토리 맵핑을 통해 요구사항을 조기 가시화하고, 변경통제위원회(CCB)와 형상 통제 절차를 통한 공식 변경 영향도 평가 제도화.
- 자연어 명세의 모호성으로 인한 이해관계자 간 해석 왜곡 :
  - 한계점 : 텍스트 중심 자연어로 서술된 요구사항은 다의적 해석의 여지가 많아 발주자, 설계자, 개발자, 테스터 간의 상호 이해가 어긋나 중대 결함 유발.
  - 해결 방안 : BDD(Behavior-Driven Development)의 Gherkin 문법(Given-When-Then), 의사결정 테이블(Decision Table), 상태 전이 다이어그램 등 준정형·정형 명세 기법을 병행하여 모호성 원천 제거.
- 개발 생명주기 전반에 걸친 요구사항 추적성(Traceability) 단절 :
  - 한계점 : 요구사항 변경 시 설계, 소스코드, 테스트 케이스 간의 영향 분석이 수작업 문서로 관리되어 누락과 불일치가 빈발.
  - 해결 방안 : Jira, Confluence, Git을 통합한 ALM(Application Lifecycle Management) 도구를 기반으로 요구사항부터 테스트까지 1:N 양방향 추적 매트릭스(RTM)를 실시간 자동 연동 관리.

## Ⅴ. 요구공학 성공을 위한 기술사적 제언

- 비기능 요구사항의 정량적 SLA(Service Level Agreement)화 : '빠른 속도'나 '편리한 화면' 같은 주관적 서술을 배제하고, '동시 사용자 5,000명 기준 TPS(Transactions Per Second) 1,500 이상, 평균 응답 1.2초 이하'와 같이 테스트 가능한 정량적 지표로 작성 의무화.
- 양방향 요구사항 추적표(RTM) 관리의 자동화 : 요구사항(SRS) - 아키텍처 설계(SAD, Software Architecture Description) - 소스코드(Git Commit) - 테스트 케이스(TC)를 Jira, ALM 도구와 연계하여 변경 발생 시 영향도 분석(Impact Analysis)이 즉각 가능하도록 인프라 지원.
