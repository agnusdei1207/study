---
title: "소프트웨어 품질보증(SQA, Software Quality Assurance)"
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

## Ⅰ. 소프트웨어 품질보증(SQA)의 개요

- 개념 : 소프트웨어 제품이 사전에 정의된 품질 요구사항 및 표준 규격을 충족한다는 확신을 제공하기 위해, **소프트웨어 생명주기** (SDLC, Software Development Life Cycle) 전반에 걸쳐 체계적인 프로세스 준수 여부를 계획, 감시, 평가, 개선하는 체계적인 공학 활동 (SQA, Software Quality Assurance).
- 배경 및 필요성 : 개발 완료 후의 **사후 테스트** (QC, Quality Control)만으로는 고품질 소프트웨어를 담보할 수 없으며, 프로세스의 오류를 조기에 차단하여 결함 유입을 원천 예방하는 **품질 관리** (QA, Quality Assurance) 체계 필수.
- 품질 표준 : **ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission) 25010** (시스템 및 SW(Software) 품질 모델), **CMMI**(Capability Maturity Model Integration) Process & Product Quality Assurance(PPQA).

## Ⅱ. SQA, QC, 테스팅의 개념적 계층 및 차이점

```text
   ┌────────────────────────────────────────────────────────┐
   │ [ SQA: 품질보증 (Quality Assurance) ]                  │
   │  - 프로세스 중심, 예방(Prevention) 지향                │
   │  - 표준 수립, 감사, 프로세스 준수 검증                │
   │                                                        │
   │  ┌──────────────────────────────────────────────────┐  │
   │  │ [ QC: 품질제어 (Quality Control) ]               │  │
   │  │  - 산출물 중심, 검출(Detection) 지향            │  │
   │  │  - 코드 리뷰, 아키텍처 인스펙션                 │  │
   │  │                                                  │  │
   │  │  ┌────────────────────────────────────────────┐  │  │
   │  │  │ [ Testing: 테스트 ]                        │  │  │
   │  │  │  - 실제 실행을 통한 결함 식별 및 수정     │  │  │
   │  │  └────────────────────────────────────────────┘  │  │
   │  └──────────────────────────────────────────────────┘  │
   └────────────────────────────────────────────────────────┘
```

- **프로세스 품질보증 (Process QA)** : 개발 절차, 표준 가이드라인, 형상관리, 변경 통제 프로세스가 적절히 준수되고 있는지 주기적으로 **감사** (Audit).
- **제품 품질보증 (Product QA)** : 생성된 산출물(명세서, 설계서, 소스코드, 실행 파일)이 품질 기준에 부합하는지 리뷰 및 정량 측정.

## Ⅲ. ISO/IEC 25010 기반 8대 소프트웨어 품질 특성

| 품질 특성 | 하위 품질 요소 및 핵심 검증 기준 |
|---|---|
| **기능 적합성** (Functional Suitability) | 기능 완전성, 기능 정확성, 기능 적절성 |
| **성능 효율성** (Performance Efficiency) | 시간 반응성(응답시간/처리량), 자원 활용성(CPU(Central Processing Unit)/메모리), 용량성 |
| **호환성** (Compatibility) | 공존성(Co-existence), 상호운용성(Interoperability) |
| **사용성** (Usability) | 적합성 인지성, 학습 용이성, 조작 용이성, 사용자 오류 보호, UI(User Interface) 심미성 |
| **신뢰성** (Reliability) | 성숙도, 무고장성, 가용성, 장애 허용성, 회복 용이성(MTBF(Mean Time Between Failures)/MTTR(Mean Time to Repair)) |
| **보안성** (Security) | 기밀성, 무결성, 부인방지, 책임추적성, 인증성 |
| **유지보수성** (Maintainability) | 모듈성, 재사용성, 분석 용이성, 수정 용이성, 시험 용이성 |
| **이식성** (Portability) | 적응성, 설치 용이성, 대체 용이성 |

## Ⅳ. 소프트웨어 품질보증(SQA)의 주요 한계점 및 해결 방안

- 프로세스 통제 위주의 관료주의적 SQA 전락 :
  - 한계점 : SQA 활동이 제품의 실질적 코드 품질과 사용자 경험 개선보다는 표준 절차 체크리스트 준수 및 증빙 서류 징구에만 매몰되어 개발 생산성을 저해.
  - 해결 방안 : 단순 감사형 QA에서 개발 엔지니어링을 직접 지원하는 QE(Quality Engineering)로 전환하고, CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인 내에 정적 분석 및 자동화 테스트 도구를 내재화하여 지원.
- 시프트-레프트(Shift-Left) 부재로 인한 후반부 품질 병목 :
  - 한계점 : 요구사항 및 아키텍처 설계 단계의 품질 결함 예방 활동이 부재하여, 프로젝트 테스트 및 릴리스 직전 단계에서 중대 아키텍처 결함이 대거 발견되어 출시 일정 연기 초래.
  - 해결 방안 : 요구사항 도출 및 아키텍처 리뷰 단계부터 SQA 인력이 주도적으로 참여하여 품질 속성을 검증하고, TDD(Test-Driven Development)/BDD(Behavior-Driven Development) 및 코드 리뷰 정량화를 조기 강제하는 단계별 품질 게이트(Quality Gate) 확립.
- 정량적 품질 지표의 실효성 및 비즈니스 성과 연계 부족 :
  - 한계점 : 단순 코드 라인 수, 테스트 케이스 실행 건수 등 형식적 지표만 수집하여 실제 시스템 장애율이나 비즈니스 전환율과의 인과관계를 입증하지 못함.
  - 해결 방안 : 결함 제거 효율(DRE, Defect Removal Efficiency), 결함 밀도, MTBF/MTTR 등 신뢰성 지표를 표준화하고, DORA(DevOps Research and Assessment) 핵심 지표 및 사용자 만족도와 연계된 전사 통합 엔지니어링 품질 대시보드 운영.

## Ⅴ. 고도화된 SQA 정착을 위한 기술사적 제언

- CI/CD 파이프라인 내 '지속적 품질(Continuous Quality)' 게이트 자동화 : 과거 사후 감리에 치중하던 SQA 방식을 탈피하여, 빌드 시 정적 코드 분석(SonarQube), 보안 취약점 점검(Snyk), 테스트 커버리지 기준 미달 시 자동으로 배포를 중단하는 자동화된 품질 게이트웨이 구축 필수.
- 독립적인 SQA 조직과 개발팀 간의 협력적 거버넌스 확립 : 품질보증 담당자가 개발팀 내부의 일정 압박에 종속되지 않도록 경영진 직속의 독립 조직으로 운영하되, 단순한 규제자가 아닌 품질 엔지니어링 프레임워크와 도구를 지원하는 '품질 에이블러(Quality Enabler)'로 자리매김해야 함.
