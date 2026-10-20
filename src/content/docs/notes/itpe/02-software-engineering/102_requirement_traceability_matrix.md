---
title: "요구사항 추적표(Requirement Traceability Matrix)"
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

1. 요구사항 추적표(RTM, Requirements Traceability Matrix)
2. 양방향 추적성(Bidirectional Traceability)
3. 전방·후방 추적성
4. 변경 영향도 분석(Change Impact Analysis)
5. 제안요청서(RFP, Request for Proposal)
6. ALM(Application Lifecycle Management)
7. ISO/IEC/IEEE 29148

## Ⅰ. 요구사항 추적표(RTM)의 개요

- 핵심 요약 : 요구사항부터 설계·코드·테스트까지의 산출물 연결 고리를 매트릭스로 구조화한 양방향 추적 관리 도구.
- 개념 : 요구사항 추적표(RTM, Requirements Traceability Matrix)는 소프트웨어 생명주기(SDLC, Software Development Life Cycle) 전반에 걸쳐 고객의 제안요청서(RFP, Request for Proposal) 및 비즈니스 요구사항으로부터 시스템 요구명세서(SRS, Software Requirements Specification), 아키텍처 설계, 소스코드, 단위·통합·인수 테스트 케이스에 이르는 산출물 간의 연결 고리를 매트릭스 형태로 구조화하여 양방향 추적성을 제공하는 엔지니어링 관리 도구.
- 배경 및 필요성 : 요구사항 누락(Omission), Gold Plating(승인되지 않은 임의 구현), 요구사항 변경 시 영향도 파악 불가로 인한 프로젝트 실패 방지.
- 표준 근거 : ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission)/IEEE(Institute of Electrical and Electronics Engineers) 29148(요구공학), CMMI(Capability Maturity Model Integration) Requirements Management(REQM).
- 주요 목적 : 생명주기 전 단계에서 요구사항의 완전성·일관성 검증과 변경 영향도의 즉시 파악.

## Ⅱ. 요구사항 추적표(RTM)의 특징

- 핵심 요약 : 전방 추적을 통한 누락 방지와 후방 추적을 통한 근거 검증을 동시에 지원하는 양방향 추적 체계.

1. 전방 추적성(Forward Traceability) : 요구사항이 설계, 소스코드, 테스트 케이스에 빠짐없이 반영되었는지의 확인 (요구사항 누락 검증).
2. 후방 추적성(Backward Traceability) : 구현된 소스코드와 테스트 케이스가 어느 고객 요구사항에 근거하는지의 역추적 (근거 없는 불필요 기능 구현 방지).
3. 변경 영향도 분석(Change Impact Analysis) : 요구사항 변경 시 수정 대상 설계서, 소스코드 클래스, 재실행 회귀 테스트 케이스의 즉시 특정.
4. 감리 증적자료 활용 : 과업 대비 산출물의 이행 완결성 입증을 위한 1차 검증 도구.

## Ⅲ. 요구사항 추적표(RTM)의 구조 (흐름)

- 핵심 요약 : RFP 요구사항에서 테스트 케이스까지의 순방향 흐름과 그 역방향 검증의 이중 구조.

```text
[ 전방 추적성 (Forward) : 누락 방지 ]
[ RFP 요구사항 ]
   │ REQ-001 (결제)
   ▼
[ SRS 요구스펙 ]
   │ SPEC-101 (카드결제)
   ▼
[ 아키텍처/설계서 ]
   │ PaymentModule
   ▼
[ 소스코드 ]
   │ Payment.java
   ▼
[ 테스트 케이스 ]
 - TC-501 (승인테스트)
```

```text
[ 후방 추적성 (Backward) : Gold Plating 방지 ]
TC-501 승인테스트 결과
   │ 근거 역추적
   ▼
Payment.java (구현 코드)
   ▼
PaymentModule (설계)
   ▼
SPEC-101 (요구 명세)
   ▼
REQ-001 (고객 요구 근거 확인)
```

- 매트릭스 양식 예시 :

| 요구사항 ID | 요구사항 명세 | 설계 산출물 ID | 소스 모듈/클래스 | 테스트 케이스 ID | 검증 상태 |
|---|---|---|---|---|---|
| REQ-001 | 실시간 간편 결제 승인 | SAD-ARC-03, DES-CLS-12 | OrderPayment.java | TC-PAY-01, TC-PAY-02 | Pass (검증 완료) |
| REQ-002 | 결제 실패 시 자동 환불 | SAD-ARC-05, DES-SEQ-08 | RefundManager.java | TC-REF-01 | Pass (검증 완료) |
| REQ-003 | 동시 1,000건 결제 처리 | `SAD-NFR-PERF-01` | HikariCPConfig.java | TC-PERF-10 (부하시험) | Pass (1,200 TPS(Transactions Per Second)) |

## Ⅳ. 수작업 RTM과 ALM 기반 RTM의 비교

- 핵심 요약 : 엑셀 수작업 관리의 동기화 한계를 도구 통합 자동화로 극복하는 방향이 비교의 핵심.

| 비교 항목 | 엑셀 기반 수작업 RTM | ALM(Application Lifecycle Management) 기반 RTM 자동화 |
|---|---|---|
| 관리 방식 | 수작업 업데이트, 산출물 변경의 실시간 미반영 | Jira, Confluence, Git, TestRail 연동 자동 갱신 (Traceability-as-Code) |
| 동기화 | 산출물 변경 누락, 문서와 시스템 간 불일치 심화 (문서 진부화, Document Rot) | 커밋 메시지 기반 요구사항 ID 매핑, 실시간 양방향 링크 |
| 변경 영향도 분석 | 수동 대조로 인한 지연·누락 | 티켓 클릭 한 번으로 설계서, 클래스, 회귀 테스트의 즉시 특정 |
| 애자일 대응 | 폭포수식 전면 추적표의 과도한 관리 부하 | 에픽-사용자 스토리-태스크-테스트 케이스 계층형 추적, DoD(Definition of Done) 연동 |

## Ⅴ. 요구사항 추적표(RTM)의 장점과 한계

- 핵심 요약 : 요구사항 완결성 보증과 감리 방어 효과 대신 문서 관리 부하와 방법론 마찰 수반.

- 장점 :
  1. 요구사항 누락과 Gold Plating의 체계적 방지.
  2. 요구사항 변경 시 수정 대상과 회귀 테스트 범위의 신속한 특정.
  3. 공공 정보시스템 감리에서 과업 이행 완결성 입증의 1차 증적 확보.
- 한계 및 해결 방안 :
  1. 한계 : 엑셀 기반 수작업 관리 시 잦은 산출물 변경의 실시간 미반영으로 문서와 실제 시스템 간 불일치 심화 (문서 진부화, Document Rot). / 해결 방안 : 개발 파이프라인과 통합된 ALM 도구 기반 추적 자동화(Traceability-as-Code) 체계 구축.
  2. 한계 : 스프린트마다 요구사항이 점진 상세화되는 애자일 환경에서 폭포수식 전면 추적표 작성의 과도한 관리 부하. / 해결 방안 : 에픽-사용자 스토리-태스크-테스트 케이스 계층형 추적 모델 적용 및 스프린트 백로그 완료 조건(DoD, Definition of Done)과의 연동.
  3. 한계 : 요구사항 분할 수준(Granularity) 불균형으로 1:N, N:M 복합 매핑 시 영향도 분석(Impact Analysis) 정확도 저하. / 해결 방안 : EARS(Easy Approach to Requirements Syntax) 등 요구사항 작성 표준 템플릿 준수, 기능·비기능 요건별 고유 식별자(ID) 체계화 및 단계별 베이스라인(Baseline) 동결 워크플로우 확립.

## Ⅵ. 기술사적 제언

- 핵심 요약 : ALM 도구 연계 추적 자동화와 감리 증적 활용의 제도화 필요.

- ALM 도구 연계 추적 자동화 : 수작업 엑셀 관리의 동기화 붕괴 방지를 위해 Jira, Confluence, Git Commit, TestRail을 웹훅(Webhook)으로 상호 연결하고, 커밋 메시지에 요구사항 ID(예: `feat(REQ-001): implement payment`) 입력 시 RTM이 실시간 자동 갱신되는 체계 구축 필수.
- 공공 정보시스템 감리의 1차 검증 도구 활용 : 과업 대비 산출물의 이행 완결성 입증을 위해 감리 수검 시 RTM을 1차 검증 도구로 제시, 과업 미이행 판정에 따른 사업비 삭감 및 지체상금 리스크의 선제적 방어.

## Ⅶ. 결론

- 핵심 요약 : RTM은 요구사항과 산출물 간 완결성을 보증하는 핵심 거버넌스 도구.

- RTM은 양방향 추적성을 통해 요구사항 누락과 불필요 구현을 방지하고 변경 영향도 분석의 기준 제공.
- 수작업 문서 관리의 한계 극복을 위해 ALM 기반 추적 자동화와 감리 증적 활용의 병행 필요.
