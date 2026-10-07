---
title: "스크럼(Scrum)"
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

## Ⅰ. 스크럼(Scrum)의 개요

- 개념 : 요구사항이 불확실하고 빠르게 변화하는 비즈니스 환경에서, 크로스 펑셔널 팀이 1~4주의 짧은 **반복 주기** (Sprint)를 통해 동작 가능한 소프트웨어 **증분** (Increment)을 점진적으로 릴리스하는 대표적인 **애자일** 프로젝트 관리 프레임워크.
- 배경 및 필요성 : 전통적 폭포수 모델의 긴 피드백 주기, 요구사항 변경에 따른 납기 지연, 최종 단계 인도 실패 리스크를 극복하고 빠른 시장 검증(Time-to-Market) 달성.
- 스크럼의 3대 경험주의 기둥 : **투명성** (Transparency), **점검** (Inspection), **적응** (Adaptation).

## Ⅱ. 스크럼 프레임워크 3-5-3 체계도

```text
   [ 제품 백로그 ] ──> [ 스프린트 계획회의 ] ──> [ 스프린트 실행 (1~4주) ] ──> [ 완료된 증분 ]
    (PO, Product Owner가 관리)           - 스프린트 백로그 도출       - 일일 스크럼 (15분)            (DoD, Definition of Done 만족)
                                                         │
                                                         ▼
                                                [ 스프린트 리뷰 (데모) ]
                                                         │
                                                         ▼
                                                [ 스프린트 회고 (KPT) ]
```

- 3가지 역할 (Roles) :
  - **제품 책임자 (Product Owner)** : 비즈니스 가치 극대화, **제품 백로그** 우선순위 결정 및 관리.
  - **스크럼 마스터 (Scrum Master)** : 스크럼 원칙 수호, 팀의 장애물(Impediment) 제거, 코칭.
  - **개발팀 (Developers)** : 교차 기능적이고 자기 조직화(Self-Organizing)된 다기능 개발 전문가 집단.
- 5가지 이벤트 (Events) : **스프린트** (Sprint), **스프린트 계획** (Planning), **일일 스크럼** (Daily), **스프린트 리뷰** (Review), **스프린트 회고** (Retrospective).
- 3가지 산출물 (Artifacts) : 제품 백로그(Product Backlog), **스프린트 백로그** (Sprint Backlog), 증분(Increment).

## Ⅲ. 스크럼 핵심 운영 메커니즘 비교

| 구성요소 | 핵심 활동 및 성과 기준 | 실패 시 증상 |
|---|---|---|
| 제품 백로그 관리 | **DEEP 원칙** (Detailed, Estimated, Emergent, Prioritized) 준수 | 요구사항 우선순위 혼선, 일정 지연 |
| 일일 스크럼 | 15분 스탠드업 미팅: 어제 한 일, 오늘 할 일, 장애 요인 공유 | 단순 보고 자리로 변질, 시간 지연 |
| **완료의 정의** (DoD, Definition of Done) | 빌드, 단위/통합 테스트, 정적 분석, 코드 리뷰, 배포 완료 기준 | 품질 미달 증분 릴리스, 회귀 버그 폭증 |
| 스프린트 회고 | **Keep, Problem, Try** (KPT) 관점에서 프로세스 지속 개선 도출 | 팀 내부 불만 누적, 엔지니어링 성숙도 정체 |

## Ⅳ. 스크럼(Scrum)의 주요 한계점 및 해결 방안

- 스토리 포인트의 개인 성과 지표 악용과 포인트 인플레이션 :
  - 한계점 : 팀의 작업 추정 도구인 스토리 포인트와 스프린트 속도(Velocity)를 경영진이 개발팀의 생산성 평가 지표로 오용함에 따라, 점수 부풀리기 및 기술 부채 방치 초래.
  - 해결 방안 : 벨로시티를 팀의 용량 산정(Capacity Planning) 용도로만 한정하고 조직 KPI(Key Performance Indicator)에서 배제하며, 번다운 차트 대신 리드타임/사이클타임 등 흐름(Flow) 메트릭을 정착.
- 프로덕트 오너(PO)의 역량 부족 및 의사결정 병목(SPOF, Single Point of Failure) :
  - 한계점 : PO가 비즈니스 전결권을 위임받지 못했거나 도메인 이해도가 부족하여 요구사항 정의가 지연되고 개발팀의 문의에 적시 대응하지 못해 스프린트 목표 달성 실패.
  - 해결 방안 : 실질적 의사결정 권한을 가진 전임 PO 임명, INVEST 원칙에 기반한 백로그 정제(Refinement) 세션 정례화, 제품 목표(Product Goal)와 스프린트 목표의 명확한 정렬.
- 스크럼 세레머니의 형식화 및 개발 집중도 저하 :
  - 한계점 : 데일리 스탠드업, 스프린트 계획, 리뷰, 회고 등이 형식적이고 장황한 보고 회의로 변질되어 개발자의 몰입 시간(Deep Work)을 침해하고 회의 피로도 누적.
  - 해결 방안 : 데일리 스크럼 15분 타임박싱 엄수, 비동기 스탠드업 도구(Slack/Teams 봇) 혼용, 스크럼 마스터의 장애물(Impediment) 제거 중심 서번트 리더십(Servant Leadership) 강화.

## Ⅴ. 대규모 엔터프라이즈 환경에서의 기술사적 제언

- 대규모 애자일(SAFe, LeSS) 프레임워크로의 스케일업 : 여러 스크럼 팀이 동시에 참여하는 대형 공공/금융 차세대 사업에서는 팀 간 의존성 조율을 위해 Scrum of Scrums, ART(Agile Release Train) 체계 구축 필수.
- 지표 맹신 방지와 심리적 안전감(Psychological Safety) 확보 : 스토리 포인트(Story Point)나 속도(Velocity)를 팀 간 실적 평가 지표로 오용하지 않고, 지속 가능한 개발 속도 유지와 자유로운 실패 공유 문화 정착이 핵심.
