---
title: "로우코드·노코드(LCNC, Low-Code/No-Code)"
author: "agnusdei1207"
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

## 연관 키워드

- 로우코드·노코드(LCNC, Low-Code/No-Code), 시민 개발자(Citizen Developer), 드래그 앤 드롭(Drag-and-Drop)
- 비주얼 개발 환경, 워크플로우 엔진(BPMN, Business Process Model and Notation), API(Application Programming Interface)
- 섀도우 IT(Shadow IT), 벤더 락인(Vendor Lock-in), 2-스피드 IT(Two-Speed IT), CoE(Center of Excellence)

## Ⅰ. 로우코드·노코드(LCNC)의 개요

- 핵심 요약 : 시각적 개발 환경으로 개발 장벽을 낮추는 노코드와 전문 개발 생산성을 높이는 로우코드의 결합 체계.
- 개념 : 로우코드·노코드(LCNC, Low-Code/No-Code)의 두 방식은 다음과 같은 구분.
  1. 노코드(No-Code) : 프로그래밍 언어에 대한 지식이 전혀 없는 현업 실무자(시민 개발자, Citizen Developer)가 시각적인 드래그 앤 드롭(Drag-and-Drop) 인터페이스와 GUI(Graphical User Interface) 설정만으로 애플리케이션을 즉시 구축하는 플랫폼.
  2. 로우코드(Low-Code) : 전문 개발자가 복잡한 보일러플레이트 코딩 없이 기본 로직과 UI(User Interface)를 시각적으로 자동 생성하고, 복잡한 비즈니스 규칙과 외부 연동에 한해서만 최소한의 핸드 코딩(Hand-coding)을 결합하는 생산성 극대화 개발 플랫폼.
- 배경 및 필요성 : 전 세계적인 소프트웨어 전문 개발 인력 부족 해소, 비즈니스 현업의 신규 요구사항 출시 속도(Time-to-Market) 획기적 단축.
- 대표 솔루션
  1. Microsoft Power Apps
  2. OutSystems
  3. Mendix
  4. AppSheet

## Ⅱ. 로우코드·노코드(LCNC)의 특징

- 핵심 요약 : 비주얼 빌더·워크플로우 엔진·커넥터·자동 배포의 풀스택 추상화.

1. 드래그 앤 드롭 UI 빌더(Visual Form Builder).
2. 비주얼 비즈니스 로직 및 워크플로우 엔진(BPMN(Business Process Model and Notation) 기반).
3. 원클릭 데이터 모델링(Dataverse/RDB(Relational Database) 자동 생성).
4. 사전 구축된 커넥터(Open API, SAP, Salesforce 연동).
5. 원클릭 자동 배포 : 웹, iOS, Android 동시 서빙의 완전 관리형 클라우드 런타임.

## Ⅲ. 로우코드·노코드(LCNC)의 구조 (흐름)

- 핵심 요약 : 개발자→비주얼 개발 환경→관리형 런타임의 개발 흐름과 코어 Pro-Code 영역과의 하이브리드 연계.
- LCNC 플랫폼 아키텍처 및 작업 흐름.

```text
[ 시민 개발자 (No-Code) ]
[ 전문 개발자 (Low-Code) ]
   │
   ▼
[ LCNC 비주얼 개발 환경 ]
 - 드래그 앤 드롭 UI 빌더
   (Visual Form Builder)
 - 비주얼 비즈니스 로직 및
   워크플로우 엔진 (BPMN)
 - 원클릭 데이터 모델링
   (Dataverse / RDB 자동 생성)
 - 사전 구축된 커넥터
   (Open API, SAP, Salesforce 연동)
   │
   ▼ (원클릭 자동 배포)
[ 완전 관리형 클라우드 런타임 ]
 - 웹, iOS, Android 동시 서빙
```

- 2-스피드 IT 하이브리드 아키텍처.

```text
[ 코어 시스템 : 전문 개발팀 (High-Code) ]
 - 고성능 트랜잭션·분산 인프라
 - Pro-Code (REST(Representational
   State Transfer) API 등)
        │ (API 연계)
        ▼
[ LCNC 플랫폼 : 현업 (Low/No-Code) ]
 - UI/워크플로우 오케스트레이션
 - 업무 자동화·이벤트 페이지
```

## Ⅳ. 전통적 코딩, 로우코드, 노코드의 비교

- 핵심 요약 : 사용자·방식·속도·유연성·종속성이 단계적으로 대비되는 3개 개발 방식.

| 비교 항목 | 전통적 개발 (High-Code) | 로우코드 (Low-Code) | 노코드 (No-Code) |
|---|---|---|---|
| 주요 사용자 | 숙련된 전문 소프트웨어 엔지니어 | 전문 개발자 및 IT(Information Technology) 실무자 | 현업 비즈니스 실무자 (시민 개발자) |
| 개발 방식 | IDE(Integrated Development Environment)에서 수작업 텍스트 코딩 | 시각적 모델링 + 커스텀 코드 확장 | 순수 100% 드래그 앤 드롭 비주얼 설정 |
| 개발 속도 | 수개월 소요 (느림) | 수일 ~ 수주 (매우 빠름) | 수시간 ~ 수일 (가장 빠름) |
| 아키텍처 유연성 | 완벽한 자유도 (어떤 복잡 로직도 구현) | 플랫폼이 허용하는 범위 내에서 확장 가능 | 극도로 제한적 (플랫폼 템플릿에 종속) |
| 벤더 락인 (Lock-in) | 오픈소스 표준 채택 시 락인 없음 | 플랫폼 전용 런타임 종속성 높음 | 완벽한 플랫폼 종속 (이전 불가) |

## Ⅴ. 로우코드·노코드(LCNC)의 장점과 한계

- 핵심 요약 : 개발 기간 단축·인력 부족 해소의 장점과 벤더 종속·섀도우 IT·확장성 한계의 공존.

- 장점
  1. 수시간~수주 수준의 개발 기간 단축을 통한 Time-to-Market 확보.
  2. 소프트웨어 개발 인력 부족 해소 및 현업 주도의 업무 자동화 활성화.
  3. 보일러플레이트 제거를 통한 전문 개발자 생산성 극대화.

- 한계점 1 : 특정 상용 플랫폼에의 강력한 종속(Vendor Lock-in)
  - 한계점 : LCNC 플랫폼 고유의 메타데이터와 독자적 런타임에 결속되어, 타 플랫폼으로의 마이그레이션 불가 및 라이선스 비용 인상에 취약.
  - 해결 방안 : 표준 언어(Java, JS) 및 컨테이너(Docker) 이미지 추출을 지원하는 개방형 플랫폼 선별, 핵심 데이터베이스의 표준 RDB 독립 격리 저장.
- 한계점 2 : 섀도우 IT(Shadow IT) 발생 및 보안·컴플라이언스 통제 불능
  - 한계점 : 현업 부서가 IT 부서의 승인 없이 독자적으로 앱을 개발하여 개인정보 유출, 인증 미비, 사내 데이터 거버넌스 위반 등 보안 사각지대 양산.
  - 해결 방안 : 전사 LCNC 거버넌스 프레임워크 수립, 배포 전 보안 취약점 점검 자동화, 사내 SSO(Single Sign-On) 연동 및 시민 개발자(Citizen Developer) 승인 프로세스 의무화.
- 한계점 3 : 복잡한 비즈니스 로직 및 대규모 트래픽 처리 시 확장성 한계
  - 한계점 : 시각적 드래그 앤 드롭 빌더만으로는 고난도 알고리즘 구현 불가, 대규모 동시 요청 시 런타임 성능 병목 발생.
  - 해결 방안 : 복잡한 계산 및 코어 도메인은 전문 개발자가 REST(Representational State Transfer) API 등 Pro-Code로 개발하고, LCNC는 UI/워크플로우 오케스트레이션에만 활용하는 2계층 하이브리드 아키텍처 적용.

## Ⅵ. 엔터프라이즈 도입을 위한 기술사적 제언

- 핵심 요약 : CoE 기반 전사 거버넌스와 2-스피드 IT 협력 모델의 구축.
- 섀도우 IT(Shadow IT) 방지를 위한 전사 거버넌스 체계 수립 : 현업 부서가 IT 부서의 통제 없이 제각각 LCNC 앱을 만들어 사내에 배포하면 보안 취약점, 개인정보 유출, 데이터 사일로가 심화되므로, 사내 LCNC CoE(Center of Excellence) 조직을 구축한 데이터 접근 권한과 보안 검수의 중앙 통제.
- LCNC와 전문 개발팀의 2-스피드 IT(Two-Speed IT) 협력 모델 구축 : 핵심 코어 트랜잭션과 고성능 분산 인프라는 전문 개발팀이 전통적인 고품질 코딩(High-Code)으로 구축하고, 변경이 빈번한 사내 업무 자동화나 고객 설문 이벤트 페이지는 LCNC로 현업이 자체 개발하도록 역할의 구조적 분담.

## Ⅶ. 결론

- 핵심 요약 : LCNC는 개발 민주화의 생산성 수단이되 거버넌스·하이브리드 설계가 전제된 기술.
- 요약 : 시민 개발자의 신속한 앱 구축과 전문 개발의 코어 역량을 2-스피드 IT로 분담하는 체계.
- 시사점 : CoE 중앙 통제, 개방형 플랫폼 선별, Pro-Code와의 역할 분리가 엔터프라이즈 도입 성패의 핵심.
