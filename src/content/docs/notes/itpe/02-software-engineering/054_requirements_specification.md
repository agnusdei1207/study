---
title: "요구사항 명세(SRS)"
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

## Ⅰ. 요구사항 명세서(SRS)의 개요

- 개념 : 소프트웨어 개발 프로젝트에서 이해관계자 간의 합의를 거쳐 확정된 시스템의 기능적 요구사항, 비기능 품질속성, 인터페이스 및 설계 제약조건을 명확하고 완전하게 문서화한 **공식 기술 문서** (SRS, Software Requirements Specification).
- 배경 및 필요성 : 발주자와 수주자 간의 **계약적 기준선** (Baseline)을 확립하고, 설계자·개발자·테스터에게 **단일한 구현 및 검증 기준** (Single Source of Truth)을 제공하여 분쟁 예방.
- 표준 규격 : **IEEE(Institute of Electrical and Electronics Engineers) 830** (SRS(Software Requirements Specification) 표준 가이드라인), ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission)/IEEE 29148.

## Ⅱ. IEEE 830 표준 기반 SRS의 문서 구성 체계

```text
   1. 소개 (Introduction)
      - 시스템 목적, 범위, 정의 및 약어, 참조 문서
              │
              ▼
   2. 전체 설명 (Overall Description)
      - 제품 조망(Perspective), 기능 요약, 사용자 특성, 제약조건, 가정 및 의존성
              │
              ▼
   3. 구체적 요구사항 (Specific Requirements)
      - 외부 인터페이스 요구사항 (사용자, HW, SW, 통신 인터페이스)
      - 기능적 요구사항 (기능별 입력, 처리 로직, 출력 명세)
      - 비기능적 성능 요구사항 (응답시간, 처리량, 동시 접속자 수)
      - 설계 제약조건 (표준 규격 준수, 사용 언어, 플랫폼 제약)
      - 소프트웨어 품질속성 (신뢰성, 가용성, 보안성, 유지보수성)
```

## Ⅲ. 우수한 SRS가 갖추어야 할 8대 품질 특성

| 품질 특성 | 평가 기준 및 의미 | 위반 시 문제점 |
|---|---|---|
| **정확성** (Correctness) | 실제 소프트웨어가 충족해야 하는 진정한 요구를 정확히 반영 | 잘못된 시스템 구축으로 인한 재작업 발생 |
| **명확성** (Unambiguous) | 모든 용어와 문장이 오직 하나의 의미로만 해석 가능 | 개발자와 발주자 간의 상이한 해석 및 분쟁 |
| **완전성** (Completeness) | 시스템이 수행해야 할 모든 기능, 예외, 제약조건 누락 없음 | 구현 단계에서 미처 정의되지 않은 요구 폭증 |
| **일관성** (Consistency) | 요구사항 간의 충돌이나 상호 모순이 존재하지 않음 | 모듈 간 데이터 규격 및 비즈니스 룰 충돌 |
| **중요도/안정성 순위화** (Ranked) | 각 요구사항의 비즈니스 우선순위와 변경 가능성이 명시됨 | 일정 지연 시 핵심 기능 누락 위험 |
| **검증 가능성** (Verifiable) | 비용 효율적인 방식으로 테스트를 통해 합격 여부를 판별 가능 | 정량 지표 부재로 인수 테스트 불가 판정 |
| **수정 용이성** (Modifiable) | 요구사항의 구조와 스타일이 변경에 유연하게 대응 가능 | 변경 발생 시 연쇄적인 문서 수정 누락 |
| **추적 가능성** (Traceable) | 요구사항의 기원(RFP, Request for Proposal) 및 후속 산출물(설계/코드/테스트)과 양방향 매핑 | 과업 누락 확인 불가, 변경 영향도 분석 마비 |

## Ⅳ. 요구사항 명세(SRS)의 주요 한계점 및 해결 방안

- 요구사항 변경에 따른 명세서 동기화 단절(Documentation Decay) :
  - 한계점 : 프로젝트 초기에 작성된 방대한 분량의 SRS가 개발 도중 발생하는 잦은 기능 변경을 제때 반영하지 못해 실제 코드와 괴리되는 '문서의 박제화' 발생.
  - 해결 방안 : 살아있는 문서화(Living Documentation) 체계를 도입하여 Cucumber, SpecFlow 등을 통해 실행 가능한 명세(Executable Specification)를 작성하고, CI(Continuous Integration) 파이프라인과 실시간 동기화.
- 기술적 실현 가능성(Feasibility) 검증 없는 비현실적 과잉 명세 :
  - 한계점 : 아키텍처 제약, 인프라 비용, 레거시 시스템 연동 난이도를 사전에 고려하지 않은 채 이상적인 요구사항만을 나열하여 개발 단계에서 전면 재설계 위기 직면.
  - 해결 방안 : SRS 작성 단계에 테크니컬 아키텍트(TA)가 참여하여 아키텍처 스파이크(Spike) 및 PoC(Proof of Concept)를 선행 검증하고, 비기능 요구사항에 측정 가능한 SLA(Service Level Agreement) 수치를 필수 명시.
- 자연어의 다의성으로 인한 모호한 표현(TBD, 신속하게 등)의 분쟁 :
  - 한계점 : '신속한 응답', '직관적인 화면' 등 객관적으로 측정할 수 없는 주관적 수식어가 남발되어 납품 검수 시 발주자와 사업자 간 법적 분쟁 초래.
  - 해결 방안 : IEEE 830/29148 표준 명세 가이드라인을 준수하고, 모든 요구사항에 대해 정량적 인수 기준(Acceptance Criteria)과 검증 방법(테스트, 검사, 시연)을 1:1로 사전 정의.

## Ⅴ. 현대 애자일 및 클라우드 환경에서의 기술사적 제언

- User Story와 인수 기준(Acceptance Criteria)을 결합한 실용적 SRS 구축 : 수백 페이지에 달하는 무거운 전통적 SRS 문서를 지양하고, 'As a [사용자], I want to [행위], So that [가치]' 형식의 사용자 스토리와 Gherkin(Given-When-Then) 기반 실행 가능한 명세(BDD, Behavior-Driven Development)를 결합하여 살아있는 문서(Living Documentation)로 진화.
- ALM(Application Lifecycle Management) 도구 기반의 디지털 요구사항 베이스라인 관리 : Jira, Confluence, Polarion 등 요구관리 ALM 도구를 통해 요구사항 변경 이력, CCB 승인 로그, 테스트 케이스 연결을 중앙 집중화하여 공공 감리 수검 및 형상 무결성 자동 보장.
