---
title: "요구사항 명세(SRS, Software Requirements Specification)"
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

- 요구사항 명세서(SRS, Software Requirements Specification), IEEE 830, ISO/IEC/IEEE 29148, 기능 요구사항, 비기능 요구사항
- 정확성, 명확성, 완전성, 일관성, 검증 가능성, 추적 가능성, 인수 기준(Acceptance Criteria), Living Documentation

## Ⅰ. 요구사항 명세서(SRS)의 개요

- 핵심 요약 : 확정된 요구사항을 문서화하여 계약적 기준선과 단일한 구현·검증 기준을 제공하는 공식 기술 문서.
- 개념 : 소프트웨어 개발 프로젝트에서 이해관계자 간의 합의를 거쳐 확정된 시스템의 기능적 요구사항, 비기능 품질속성, 인터페이스 및 설계 제약조건을 명확하고 완전하게 문서화한 공식 기술 문서(SRS, Software Requirements Specification).
- 배경 및 필요성 : 발주자와 수주자 간의 계약적 기준선(Baseline)을 확립하고, 설계자·개발자·테스터에게 단일한 구현 및 검증 기준(Single Source of Truth)을 제공하여 분쟁 예방.
- 표준 규격 : IEEE(Institute of Electrical and Electronics Engineers) 830(SRS 표준 가이드라인), ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission)/IEEE 29148.

## Ⅱ. SRS의 특징 (우수한 SRS의 8대 품질 특성)

- 핵심 요약 : 정확성·명확성·완전성·일관성 등 8대 품질 특성을 갖춘 검증 가능한 명세.
1. 정확성(Correctness) : 실제 소프트웨어가 충족해야 하는 진정한 요구의 정확한 반영, 위반 시 재작업 발생.
2. 명확성(Unambiguous) : 모든 용어와 문장이 오직 하나의 의미로만 해석 가능, 위반 시 개발자와 발주자 간의 상이한 해석 및 분쟁.
3. 완전성(Completeness) : 수행해야 할 모든 기능, 예외, 제약조건의 누락 부재, 위반 시 구현 단계에서 미정의 요구 폭증.
4. 일관성(Consistency) : 요구사항 간의 충돌이나 상호 모순의 부재, 위반 시 모듈 간 데이터 규격 및 비즈니스 룰 충돌.
5. 중요도/안정성 순위화(Ranked) : 각 요구사항의 비즈니스 우선순위와 변경 가능성의 명시, 위반 시 일정 지연 상황에서 핵심 기능 누락 위험.
6. 검증 가능성(Verifiable) : 비용 효율적인 방식의 테스트 기반 합격 여부 판별 가능, 위반 시 정량 지표 부재로 인수 테스트 불가 판정.
7. 수정 용이성(Modifiable) : 요구사항의 구조와 스타일의 변경 유연한 대응, 위반 시 변경 발생 시 연쇄적인 문서 수정 누락.
8. 추적 가능성(Traceable) : 요구사항의 기원(RFP, Request for Proposal)과 후속 산출물(설계/코드/테스트)과의 양방향 매핑, 위반 시 과업 누락 확인 불가 및 변경 영향도 분석 마비.

## Ⅲ. SRS의 구조 (흐름)

- 핵심 요약 : IEEE 830 기준의 소개 → 전체 설명 → 구체적 요구사항 3계층 문서 구성.

```text
1. 소개 (Introduction)
   - 시스템 목적, 범위, 정의 및 약어, 참조 문서
     │
     ▼
2. 전체 설명 (Overall Description)
   - 제품 조망, 기능 요약, 사용자 특성
   - 제약조건, 가정 및 의존성
     │
     ▼
3. 구체적 요구사항 (Specific Requirements)
   - 외부 인터페이스 : 사용자, 하드웨어, 소프트웨어, 통신
   - 기능 요구사항 : 입력, 처리 로직, 출력
   - 비기능 : 응답시간, 처리량, 동시 접속자 수
   - 설계 제약조건 : 표준 규격, 언어, 플랫폼
   - 품질속성 : 신뢰성, 가용성, 보안성, 유지보수성
```

```text
[ 요구사항 추적 흐름 (Traceability) ]
RFP(제안요청서) ──> SRS(요구사항 명세서)
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    설계 명세서      소스코드      테스트 케이스
        └──────────────┴──────────────┘
                       │
                       ▼
              양방향 매핑 검증
```

## Ⅳ. 기능 요구사항과 비기능 요구사항의 비교

- 핵심 요약 : 시스템이 '무엇을 하는가'와 '얼마나 잘 수행하는가'의 대비.

| 비교 항목 | 기능 요구사항(Functional Requirement) | 비기능 요구사항(Non-functional Requirement) |
|---|---|---|
| 정의 | 시스템이 수행해야 할 기능, 입력, 처리 로직, 출력 | 품질속성 및 설계 제약조건 |
| SRS상 예시 | 외부 인터페이스(사용자, 하드웨어, 소프트웨어, 통신) 명세 | 응답시간, 처리량, 동시 접속자 수 |
| 관련 품질속성 | 기능 충족 여부로 판별 | 신뢰성, 가용성, 보안성, 유지보수성 |
| 검증 방법 | 기능 테스트를 통한 합격 여부 판별 | SLA(Service Level Agreement) 등 정량 지표 기반 측정 |

## Ⅴ. SRS의 장점과 한계

- 핵심 요약 : 계약 기준선·단일 기준의 장점과 문서 박제화·과잉 명세·모호한 표현의 한계.
- 장점
  1. 발주자-수주자 간 계약적 기준선의 확립.
  2. 설계·개발·테스트 전 단계의 단일한 구현 및 검증 기준 제공.
  3. 요구사항 추적을 통한 변경 영향도 분석 및 과업 누락 방지.
- 한계점 1 : 요구사항 변경에 따른 명세서 동기화 단절(Documentation Decay)
  - 한계점 : 프로젝트 초기에 작성된 방대한 분량의 SRS가 개발 도중 발생하는 잦은 기능 변경을 제때 반영하지 못해 실제 코드와 괴리되는 '문서의 박제화' 발생.
  - 해결 방안 : 살아있는 문서화(Living Documentation) 체계의 도입, Cucumber와 SpecFlow 등을 통한 실행 가능한 명세(Executable Specification) 작성 및 CI(Continuous Integration) 파이프라인과의 실시간 동기화.
- 한계점 2 : 기술적 실현 가능성(Feasibility) 검증 없는 비현실적 과잉 명세
  - 한계점 : 아키텍처 제약, 인프라 비용, 레거시 시스템 연동 난이도를 사전에 고려하지 않은 채 이상적인 요구사항만을 나열하여 개발 단계에서 전면 재설계 위기 직면.
  - 해결 방안 : SRS 작성 단계에 테크니컬 아키텍트(TA) 참여를 통한 아키텍처 스파이크(Spike)와 PoC(Proof of Concept) 선행 검증, 비기능 요구사항에 측정 가능한 SLA(Service Level Agreement) 수치의 필수 명시.
- 한계점 3 : 자연어의 다의성으로 인한 모호한 표현의 분쟁
  - 한계점 : TBD(To Be Defined), '신속한 응답', '직관적인 화면' 등 객관적으로 측정할 수 없는 주관적 수식어가 남발되어 납품 검수 시 발주자와 사업자 간 법적 분쟁 초래.
  - 해결 방안 : IEEE 830/29148 표준 명세 가이드라인의 준수, 모든 요구사항에 대한 정량적 인수 기준(Acceptance Criteria)과 검증 방법(테스트, 검사, 시연)의 1:1 사전 정의.

## Ⅵ. 현대 애자일 및 클라우드 환경에서의 기술사적 제언

- 핵심 요약 : User Story·Gherkin 기반 실행 명세와 ALM 도구 기반 디지털 베이스라인 관리.
- User Story와 인수 기준(Acceptance Criteria)을 결합한 실용적 SRS 구축 : 수백 페이지에 달하는 무거운 전통적 SRS 문서를 지양하고, 'As a [사용자], I want to [행위], So that [가치]' 형식의 사용자 스토리와 Gherkin(Given-When-Then) 기반 실행 가능한 명세(BDD, Behavior-Driven Development)를 결합하여 살아있는 문서(Living Documentation)로의 진화.
- ALM(Application Lifecycle Management) 도구 기반의 디지털 요구사항 베이스라인 관리 : Jira, Confluence, Polarion 등 요구관리 ALM 도구를 통해 요구사항 변경 이력, 변경통제위원회(CCB) 승인 로그, 테스트 케이스 연결을 중앙 집중화하여 공공 감리 수검 및 형상 무결성 자동 보장.

## Ⅶ. 결론

- 핵심 요약 : SRS는 계약과 검증의 기준 문서이며, 실행 가능한 살아있는 문서로의 진화 필요.
- 요약 : 8대 품질 특성을 갖춘 명세를 통한 설계·개발·테스트·감리의 단일 기준 확보.
- 시사점 : BDD 기반 실행 명세와 ALM 추적 관리를 통한 문서 박제화 해소 필요.
