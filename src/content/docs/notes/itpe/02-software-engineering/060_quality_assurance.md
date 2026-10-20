---
title: "소프트웨어 품질보증(SQA, Software Quality Assurance)"
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

- 소프트웨어 품질보증(SQA, Software Quality Assurance), 품질제어(QC)
- ISO/IEC 25010, CMMI PPQA, 품질 특성, 품질 게이트(Quality Gate)
- Shift-Left, DRE, DORA 지표, QE(Quality Engineering)

## Ⅰ. 소프트웨어 품질보증(SQA)의 개요

- 핵심 요약 : 생명주기 전반의 프로세스 준수를 계획·감시·평가·개선하여 품질 요구사항 충족의 확신을 제공하는 체계적 공학 활동.
- 개념 : 소프트웨어 제품이 사전에 정의된 품질 요구사항 및 표준 규격을 충족한다는 확신을 제공하기 위해 소프트웨어 생명주기(SDLC, Software Development Life Cycle) 전반에 걸쳐 프로세스 준수 여부를 계획, 감시, 평가, 개선하는 체계적 공학 활동(SQA, Software Quality Assurance).
- 배경 및 필요성 : 개발 완료 후의 사후 테스트(QC, Quality Control)만으로는 고품질 소프트웨어를 담보할 수 없으므로, 프로세스 오류의 조기 차단을 통한 결함 유입 원천 예방 체계(QA, Quality Assurance) 필수.
- 주요 목적 : 프로세스 및 산출물의 표준 준수 검증, 결함 예방을 통한 품질 비용 최소화, 이해관계자에 대한 품질 신뢰 제공.

## Ⅱ. SQA의 특징

- 핵심 요약 : 프로세스 중심·예방 지향의 생명주기 전반 활동이며 표준 기반 감사와 이원화된 품질보증 체계.
1. 프로세스 중심·예방(Prevention) 지향 활동.
2. SDLC 전반에 걸친 계획, 감시, 평가, 개선의 반복 수행.
3. 프로세스 품질보증과 제품 품질보증의 이원 체계.
4. 품질 표준 기반 수행 : ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission) 25010, CMMI(Capability Maturity Model Integration)의 PPQA(Process & Product Quality Assurance).
5. 개발 조직에 대한 독립 관점의 객관적 검증과 감사(Audit).

## Ⅲ. SQA의 구조 (흐름)

- 핵심 요약 : SQA-QC-테스팅의 포괄 계층 구조와 품질 활동 사이클.

```text
[ 품질 활동의 계층 구조 ]
[ SQA : 품질보증 (Quality Assurance) ]
 - 프로세스 중심, 예방(Prevention) 지향
 - 표준 수립, 감사, 프로세스 준수 검증
  └─ [ QC : 품질제어 (Quality Control) ]
      - 산출물 중심, 검출(Detection) 지향
      - 코드 리뷰, 아키텍처 인스펙션
       └─ [ Testing : 테스트 ]
           - 실제 실행을 통한 결함 식별·수정
```

```text
[ SQA 활동 사이클 ]
품질 계획 수립
   ↓
표준·절차 정의
   ↓
프로세스 감시 및 감사(Audit)
   ↓
부적합 판정·시정 조치
   ↓
개선 및 표준 갱신 ──> (품질 계획 수립으로 순환)
```

- 프로세스 품질보증(Process QA) : 개발 절차, 표준 가이드라인, 형상관리, 변경 통제 프로세스의 준수 여부에 대한 주기적 감사(Audit).
- 제품 품질보증(Product QA) : 생성된 산출물(명세서, 설계서, 소스코드, 실행 파일)의 품질 기준 부합 여부에 대한 리뷰 및 정량 측정.
- ISO/IEC 25010 기반 8대 소프트웨어 품질 특성 체계

| 품질 특성 | 하위 품질 요소 및 핵심 검증 기준 |
|---|---|
| 기능 적합성(Functional Suitability) | 기능 완전성, 기능 정확성, 기능 적절성 |
| 성능 효율성(Performance Efficiency) | 시간 반응성(응답시간·처리량), 자원 활용성(CPU(Central Processing Unit)·메모리), 용량성 |
| 호환성(Compatibility) | 공존성(Co-existence), 상호운용성(Interoperability) |
| 사용성(Usability) | 적합성 인지성, 학습 용이성, 조작 용이성, 사용자 오류 보호, UI(User Interface) 심미성 |
| 신뢰성(Reliability) | 성숙도, 무고장성, 가용성, 장애 허용성, 회복 용이성(MTBF(Mean Time Between Failures)·MTTR(Mean Time to Repair)) |
| 보안성(Security) | 기밀성, 무결성, 부인방지, 책임추적성, 인증성 |
| 유지보수성(Maintainability) | 모듈성, 재사용성, 분석 용이성, 수정 용이성, 시험 용이성 |
| 이식성(Portability) | 적응성, 설치 용이성, 대체 용이성 |

## Ⅳ. SQA, QC, 테스팅의 비교

- 핵심 요약 : SQA는 프로세스 예방, QC는 산출물 검출, 테스팅은 실행 기반 결함 확인의 역할 분담.

| 비교 항목 | SQA(Quality Assurance) | QC(Quality Control) | 테스팅(Testing) |
|---|---|---|---|
| 초점 | 프로세스 중심 | 산출물 중심 | 실행 기반 동작 검증 |
| 지향점 | 예방(Prevention) | 검출(Detection) | 결함 식별·수정 확인 |
| 주요 활동 | 표준 수립, 감사, 프로세스 준수 검증 | 코드 리뷰, 인스펙션, 정량 측정 | 단위·통합·시스템 테스트 수행 |
| 수행 시점 | 생명주기 전반 | 산출물 생성 이후 | 실행 가능한 빌드 이후 |

## Ⅴ. SQA의 장점과 한계

- 핵심 요약 : 결함 조기 예방과 품질 신뢰 제공의 장점, 관료주의 전락·후반 병목·지표 실효성 부족의 한계가 공존.
- 장점
  1. 프로세스 오류의 조기 차단을 통한 결함 유입 원천 예방.
  2. 표준 준수 검증을 통한 이해관계자 품질 신뢰 제공.
  3. 후행 테스트·재작업 비용의 절감.
- 한계점 1 : 프로세스 통제 위주의 관료주의적 SQA 전락
  - 한계점 : SQA 활동이 제품의 실질적 코드 품질과 사용자 경험 개선보다 표준 절차 체크리스트 준수 및 증빙 서류 징구에만 매몰되어 개발 생산성 저해.
  - 해결 방안 : 단순 감사형 QA에서 개발 엔지니어링 직접 지원형 QE(Quality Engineering)로 전환, CI/CD(Continuous Integration/Continuous Delivery) 파이프라인 내 정적 분석·자동화 테스트 도구 내재화.
- 한계점 2 : 시프트-레프트(Shift-Left) 부재로 인한 후반부 품질 병목
  - 한계점 : 요구사항 및 아키텍처 설계 단계의 결함 예방 활동 부재로 프로젝트 테스트·릴리스 직전 단계에서 중대 아키텍처 결함이 대거 발견, 출시 일정 연기 초래.
  - 해결 방안 : 요구사항 도출·아키텍처 리뷰 단계부터의 SQA 인력 주도 참여, TDD(Test-Driven Development)·BDD(Behavior-Driven Development)와 코드 리뷰 정량화의 조기 강제 등 단계별 품질 게이트(Quality Gate) 확립.
- 한계점 3 : 정량적 품질 지표의 실효성 및 비즈니스 성과 연계 부족
  - 한계점 : 코드 라인 수, 테스트 케이스 실행 건수 등 형식적 지표만 수집하여 실제 시스템 장애율·비즈니스 전환율과의 인과관계 입증 실패.
  - 해결 방안 : 결함 제거 효율(DRE, Defect Removal Efficiency), 결함 밀도, MTBF/MTTR 등 신뢰성 지표 표준화, DORA(DevOps Research and Assessment) 핵심 지표·사용자 만족도 연계 전사 통합 품질 대시보드 운영.

## Ⅵ. 고도화된 SQA 정착을 위한 기술사적 제언

- 핵심 요약 : CI/CD 기반 지속적 품질 게이트 자동화와 독립 조직의 협력적 거버넌스 확립.
- CI/CD 파이프라인 내 지속적 품질(Continuous Quality) 게이트 자동화 : 사후 감리 중심 방식의 탈피, 빌드 시 정적 코드 분석(SonarQube)·보안 취약점 점검(Snyk)·테스트 커버리지 기준 미달 시 자동 배포 중단 등 자동화 품질 게이트웨이 구축.
- 독립적인 SQA 조직과 개발팀 간 협력적 거버넌스 확립 : 품질보증 담당자의 개발팀 일정 압박 종속 방지를 위한 경영진 직속 독립 조직 운영, 단순 규제자가 아닌 품질 엔지니어링 프레임워크·도구를 지원하는 품질 에이블러(Quality Enabler)로의 자리매김.

## Ⅶ. 결론

- 핵심 요약 : SQA는 사후 검출이 아닌 예방 중심의 생명주기 전반 품질 거버넌스.
- 요약 : 프로세스·산출물의 이원 감사와 ISO/IEC 25010 표준 기반으로 품질 확신을 제공하는 체계적 공학 활동.
- 시사점 : 지속적 품질 게이트 자동화와 QE 전환을 통해 관료주의적 감사에서 엔지니어링 협력형 품질 체계로의 진화 필요.
