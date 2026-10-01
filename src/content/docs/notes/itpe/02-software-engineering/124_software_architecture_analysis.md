---
title: "소프트웨어 아키텍처 분석(정방향/역방향)"
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

## Ⅰ. 소프트웨어 아키텍처 분석의 개요

- **개념** : 소프트웨어 시스템의 아키텍처 설계와 실제 구현된 소스코드 간의 일치성을 검증하고, 시스템의 구조적 무결성, 기술 부채, 아키텍처 침식(Architecture Erosion) 여부를 평가하기 위해 요구사항으로부터 아키텍처를 도출하는 정방향 분석(Forward Analysis)과 기존 소스코드를 역추적하여 실제 아키텍처를 복원하는 역방향 분석(Reverse Analysis)을 수행하는 공학적 분석 체계.
- **배경 및 필요성** : 개발이 진행되면서 마감 일정에 쫓겨 아키텍처 원칙을 무시하고 작성된 '아키텍처 드리프트' 현상이 누적되면, 시스템 구조가 스파게티화되어 유지보수가 불가능해지므로 이를 주기적으로 가시화하고 통제.
- **핵심 목표** : 아키텍처 적합성 검증, 시스템 구조 가시화, 레거시 시스템 현대화의 청사진 확보.

## Ⅱ. 정방향 및 역방향 아키텍처 분석의 순환 사이클

```text
   [ 비즈니스 요구사항 ]
            │
            ▼ (정방향 분석: Forward Analysis)
   [ 의도된 아키텍처 (Conceptual Architecture) ] ── (설계 표준 수립: 레이어드, 클린 아키텍처)
            │                                             │
            ▼                                             ▼ (아키텍처 적합성 검증: Conformance Checking)
   [ 실제 구현 소스코드 (Source Code) ] <────────────── [ 구조적 차이 및 결합도 위반 식별 ]
            │                                             ▲
            ▼ (역방향 분석: Reverse Analysis)             │
   [ 복원된 아키텍처 (As-Built Architecture) ] ───────────┘
```

- **정방향 아키텍처 분석 (Forward Analysis)** : 비즈니스 목표와 품질 시나리오를 바탕으로 아키텍처 패턴을 선정하고 모듈 간의 허용된 의존성 규칙(Dependency Rules)을 수립하는 과정.
- **역방향 아키텍처 분석 (Reverse Analysis)** : 바이트코드, AST(추상 구문 트리), Git 커밋 로그를 파싱하여 클래스 간의 실제 호출 관계와 의존성 구조를 역공학(Reverse Engineering)으로 시각화하고 복원하는 과정.

## Ⅲ. 정방향 분석과 역방향 분석의 비교

| 비교 항목 | 정방향 아키텍처 분석 (Forward) | 역방향 아키텍처 분석 (Reverse) |
|---|---|---|
| 분석의 출발점 | 요구사항 명세서, 비즈니스 드라이버 | 이미 구축된 소스코드, 바이너리, DB 스키마 |
| 주요 산출물 | 개념 아키텍처, SAD(아키텍처 기술서), 유틸리티 트리 | 복원된 컴포넌트 의존 다이어그램, DSM(의존성 구조 매트릭스) |
| 주 목적 | 최적의 품질속성을 보장하는 청사진 설계 | 실제 구현의 아키텍처 규칙 위반 및 아키텍처 침식 탐지 |
| 수행 시점 | 프로젝트 기획 및 초기 아키텍처 설계 단계 | 개발 중 주기적 코드 감사 또는 레거시 차세대 전환 직전 |
| 대표 도구 | Enterprise Architect, PlantUML, Miro | ArchUnit, Structure101, SonarQube, Lattix |

## Ⅳ. 지속 가능한 아키텍처 거버넌스를 위한 기술사적 제언

- **ArchUnit 기반의 '테스트로서의 아키텍처(Architecture-as-Code)' 자동화** : 문서로만 존재하는 아키텍처 규칙은 반드시 무너지므로, `classes().that().resideInAPackage("..service..").should().onlyBeAccessedByClassesThat().resideInAnyPackage("..controller..")`와 같이 아키텍처 계층 규칙을 Java 단위 테스트 코드로 작성하여 CI 파이프라인에서 매 빌드마다 자동 검증 강제.
- **의존성 구조 매트릭스(DSM, Dependency Structure Matrix) 기반 순환 참조 척결** : 역방향 분석을 통해 모듈 간의 순환 의존성(Circular Dependency)을 상삼각 행렬로 시각화하고, 순환 고리를 끊기 위해 의존성 역전 원칙(DIP)을 적용하는 체계적 리팩토링 추진 필수.
