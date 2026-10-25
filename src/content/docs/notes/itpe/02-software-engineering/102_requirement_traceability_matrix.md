---
title: "요구사항 추적표(RTM, Requirements Traceability Matrix)"
description: "양방향 추적성·전방/후방·변경 영향도·ALM 자동화, 문서 부패·애자일 부하·분할 불균형 한계와 방안"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드

- 요구사항 추적표(RTM, Requirements Traceability Matrix)
- 양방향 추적성(Bidirectional Traceability)
- 전방·후방 추적성
- 변경 영향도 분석(Change Impact Analysis)
- 제안요청서(RFP, Request for Proposal)
- ALM(Application Lifecycle Management)
- ISO/IEC/IEEE 29148

## Ⅰ. 요구사항 추적표(RTM)의 개요

- 핵심 요약 : 요구사항부터 설계·코드·테스트까지의 산출물 연결을 매트릭스로 관리하는 양방향 추적 도구.
- 개념 : 소프트웨어 생명주기 전반에 걸쳐 제안요청서(RFP, Request for Proposal)와 비즈니스 요구사항이 시스템 요구명세서(SRS, Software Requirements Specification), 설계, 소스코드, 테스트 케이스까지 이어지는 연결을 매트릭스로 기록하여 **양방향 추적성** (Bidirectional Traceability)을 확보하는 요구사항 추적표(RTM, Requirements Traceability Matrix).
- 배경 및 필요성 : 요구사항이 빠지거나(누락), 승인되지 않은 기능이 임의로 구현되거나(Gold Plating), 변경의 영향 범위를 알 수 없어 프로젝트가 실패하는 것을 막기 위해 필요하다.
- 표준 근거 : ISO/IEC/IEEE 29148(요구공학 표준)과 CMMI(Capability Maturity Model Integration)의 요구사항 관리(REQM, Requirements Management) 영역.
- 주요 목적 : 생명주기 전 단계에서 요구사항의 완전성과 일관성을 검증하고, 변경의 영향을 즉시 파악하는 것.

## Ⅱ. 요구사항 추적표(RTM)의 특징 및 장점

- 핵심 요약 : 전방 추적으로 누락을 막고 후방 추적으로 근거를 검증하는 양방향 추적 체계.

1. **전방 추적성** (Forward Traceability) : 요구사항이 설계, 소스코드, 테스트 케이스에 빠짐없이 반영되었는지 확인 → 요구사항 누락 검증.
2. **후방 추적성** (Backward Traceability) : 구현된 코드와 테스트가 어느 요구사항에서 왔는지 역추적 → 근거 없는 기능, 즉 Gold Plating 방지.
3. **변경 영향도 분석** (Change Impact Analysis) : 요구사항이 바뀌면 수정할 설계서, 코드 모듈, 회귀 테스트 대상을 즉시 특정 → 변경 비용 예측 가능.
4. 감리 증적 : 과업 대비 산출물의 이행 완결성을 보여 주는 1차 증적 → 감리 대응 근거 확보.

## Ⅲ. 요구사항 추적표(RTM)의 구조 (흐름)

- 핵심 요약 : RFP 요구사항에서 테스트 케이스까지의 순방향 연결과, 그 역방향 검증의 이중 구조.

```text
[ 전방 추적 (누락 방지) ]
[ RFP 요구사항 ] REQ-001
      ↓
[ SRS 명세 ] SPEC-101
      ↓
[ 설계서 ] PaymentModule
      ↓
[ 소스코드 ] Payment.java
      ↓
[ 테스트 케이스 ] TC-501
```

```text
[ 후방 추적 (근거 검증) ]
[ TC-501 테스트 결과 ]
      ↓ 근거 역추적
[ Payment.java ]
      ↓
[ PaymentModule ]
      ↓
[ SPEC-101 ] → [ REQ-001 ]
```

- 매트릭스 양식 예시 :

| 요구사항 ID | 요구사항 명세 | 설계 산출물 ID | 소스 모듈·클래스 | 테스트 케이스 ID | 검증 상태 |
| --- | --- | --- | --- | --- | --- |
| REQ-001 | 실시간 간편 결제 승인 | SAD-ARC-03, DES-CLS-12 | OrderPayment.java | TC-PAY-01, TC-PAY-02 | 통과 |
| REQ-002 | 결제 실패 시 자동 환불 | SAD-ARC-05, DES-SEQ-08 | RefundManager.java | TC-REF-01 | 통과 |
| REQ-003 | 대량 동시 결제 처리 | SAD-NFR-PERF-01 | HikariCPConfig.java | TC-PERF-10 (부하 시험) | 통과 (목표 충족) |

## Ⅳ. 수작업 RTM과 ALM 기반 RTM의 비교

- 핵심 요약 : 엑셀 수작업 관리의 동기화 한계를 도구 연계 자동화로 극복하는 방향이 비교의 핵심이다.
- 비교 대상 : 엑셀 수작업 RTM과, 이슈 관리·형상관리·테스트 도구를 묶는 **ALM** (Application Lifecycle Management, 애플리케이션 생명주기 관리) 기반 RTM.

| 비교 항목 | 엑셀 기반 수작업 RTM | ALM 기반 RTM 자동화 |
| --- | --- | --- |
| 관리 방식 | 사람이 직접 갱신하여 산출물 변경이 즉시 반영되지 않음 | 이슈, 형상, 테스트 도구와 연동하여 자동 갱신 |
| 동기화 | 문서와 시스템 간 불일치가 누적 (문서 부패, Document Rot) | 커밋 메시지의 요구사항 ID로 링크를 자동 생성 |
| 변경 영향도 분석 | 수동 대조로 지연과 누락 발생 | 요구사항 항목에서 연결된 설계, 코드, 테스트를 한 번에 조회 |
| 애자일 대응 | 전체 추적표 작성과 유지 부담이 큼 | 에픽, 사용자 스토리, 태스크, 테스트 케이스의 계층 추적과 완료 정의(DoD, Definition of Done) 연동 |

## Ⅴ. 요구사항 추적표(RTM)의 한계와 방안

- 핵심 요약 : 요구사항 완결성 보증과 감리 증적이라는 장점에 비해, 문서 관리 부하와 개발 방법론과의 마찰이 한계로 따른다.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 문서 부패 | 엑셀 수작업으로 변경이 누락되어 문서와 실제 시스템이 어긋남 | 개발 파이프라인과 통합된 ALM 도구 기반의 추적 자동화(Traceability-as-Code) | 추적 링크 누락 건수, 문서 최신성 점검 결과 |
| 애자일 환경의 관리 부하 | 스프린트마다 요구사항이 구체화되어 폭포수식 전체 추적표를 유지하기 어려움 | 에픽, 스토리, 테스트 케이스의 계층형 추적 모델 적용, 완료 정의(DoD)와 연동 | 추적 갱신 소요 시간 |
| 분할 수준 불균형 | 요구사항 단위가 들쭉날쭉해 1:N, N:M 매핑이 복잡해지고 영향도 분석 정확도 저하 | EARS(Easy Approach to Requirements Syntax) 같은 작성 템플릿, 고유 식별자 체계, 단계별 베이스라인 동결 | 복합 매핑 비율, 베이스라인 변경 건수 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : ALM 연계 추적 자동화와 감리 증적으로서의 RTM 활용을 제도로 정착시키는 방향.
- 엑셀 관리의 동기화 붕괴를 막기 위해 이슈 관리, 소스 저장소, 테스트 도구를 웹훅으로 연결하고, 커밋 메시지에 요구사항 ID(예: `feat(REQ-001): implement payment`)를 적으면 RTM이 자동 갱신되는 체계를 기본으로 삼아야 한다.
- 공공 정보시스템 감리에 대비하여 RTM을 과업 이행 완결성을 보이는 1차 증적으로 제출할 수 있도록 상시 관리해야 하며, 이를 통해 과업 미이행 판정에 따른 사업비 삭감 위험을 사전에 줄여야 한다.

## Ⅶ. 결론

- 핵심 요약 : RTM은 요구사항과 산출물 사이의 완결성을 보증하는 핵심 거버넌스 도구.
- 시사점 : 양방향 추적으로 누락과 불필요 구현을 함께 막고, 자동화된 추적과 감리 증적 활용을 병행해야 실효성이 확보된다.