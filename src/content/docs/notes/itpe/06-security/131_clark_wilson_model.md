---
title: "Clark and Wilson 모델"
author: "agnusdei1207"
date: "2026-10-24T23:08:40+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "131"
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- Clark and Wilson 모델, 무결성 모델, 직무 분리(Separation of Duties), 변환 절차(TP)
- 무결성 검증 절차(IVP), 제약 데이터(CDI), 비제약 데이터(UDI), 인증 규칙, 강제 규칙
- Biba 모델, Bell-LaPadula 모델, 감사 추적, 상업적 무결성

## Ⅰ. Clark and Wilson 모델의 개요

- 핵심 요약 : 직무 분리와 검증된 프로그램을 통해서만 데이터를 바꾸도록 강제하는 상업용 무결성 모델.
- 개념 : 금융, 회계, 공급망 등 상업 환경에서 비인가 변경과 내부자의 권한 오남용을 막기 위해 **직무 분리** (Separation of Duties), **변환 절차** (TP, Transformation Procedure), **무결성 검증 절차** (IVP, Integrity Verification Procedure)를 정의한 형식 무결성 모델.
- 배경 및 필요성 : Bell-LaPadula 모델은 기밀성, Biba 모델은 계층적 무결성에 초점을 두어 복식 부기, 데이터 간 일관성, 감사 추적 같은 상업 시스템의 무결성 요구를 충분히 표현하지 못함.
- 주요 목적 : 데이터를 직접 고치지 못하게 하고, 승인된 프로그램으로만 변경하게 하며, 업무 처리에 둘 이상의 주체를 거치게 하여 사기와 데이터 훼손을 방지.

## Ⅱ. Clark and Wilson 모델의 특징 및 장점

- 핵심 요약 : 데이터 분류, 직무 분리, 감사 기록이 결합되어 부정과 오류를 구조적으로 차단하는 방식.

1. 데이터 분리 : 보호 대상 **제약 데이터** (CDI, Constrained Data Item)와 검증 전 **비제약 데이터** (UDI, Unconstrained Data Item)를 구분 → UDI는 검증을 거쳐야만 CDI로 승격되어 무결성 경계가 명확해짐.
2. 직무 분리 : 거래의 생성, 승인, 실행, 감사를 서로 다른 주체가 맡도록 강제 → 한 사람이 단독으로 부정 거래를 완결하기 어려움.
3. 감사 추적 : 모든 TP 실행 내역을 추가 전용(Append-only) 로그로 기록 → 사후 부인 방지와 책임 추적이 가능.

## Ⅲ. Clark and Wilson 모델의 구조 (흐름)

- 핵심 요약 : 사용자가 승인된 TP만 실행하고, IVP가 CDI의 일관성을 상시 확인하는 3자 관계 구조.
- **인증 규칙** (Certification Rules) : TP가 CDI를 유효한 상태에서 다른 유효한 상태로만 바꾸도록 보장하는 규칙.
- **강제 규칙** (Enforcement Rules) : 사용자가 허가된 TP만 실행하도록 제한하는 규칙.

```text
[ 사용자 - TP - 데이터 관계 ]

사용자 (직무에 따라 TP 실행 권한)
   ↓
변환 절차 (TP, 승인된 프로그램만)
   ↓
제약 데이터 (CDI) 변경
   ↑
무결성 검증 절차 (IVP, 일관성 점검)
```

```text
[ 데이터 승격 흐름 ]

외부 입력 (UDI, 미검증)
   ↓
TP 내부 검증 (입력값 확인)
   ↓
제약 데이터 (CDI) 승격
```

## Ⅳ. Clark and Wilson 모델과 주요 보안 모델의 비교

- 핵심 요약 : Biba와 Bell-LaPadula가 단일 속성 규칙에 집중하는 데 비해, Clark and Wilson은 절차와 주체를 함께 통제하여 상업 업무에 맞음.

| 비교 항목 | Clark and Wilson 모델 | Biba 모델 | Bell-LaPadula 모델 |
| --- | --- | --- | --- |
| 보안 목표 | 상업적 무결성 | 무결성 | 기밀성 |
| 핵심 규칙 | 직무 분리, TP·IVP, 주체-TP-객체 바인딩 | Simple Integrity (No Read Down), *-Integrity (No Write Up) | Simple Security (No Read Up), *-Property (No Write Down) |
| 데이터 변경 | 검증된 TP를 통해서만 가능 | 낮은 무결성 주체의 상위 객체 쓰기 금지 | 높은 등급 주체의 하위 객체 쓰기 금지 |
| 주요 적용 | 회계 시스템, 원장, ERP | 운영체제 무결성 수준 (예: Windows MIC) | 다단계 보안 (MLS, Multi-Level Security) |

## Ⅴ. Clark and Wilson 모델의 한계와 방안

- 핵심 요약 : 절차 복잡성, 직무 분리 병목, 입력 검증 결함을 모듈화, 비상 우회 절차, 정적 분석으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 모든 로직을 TP로 모델링하는 복잡성 | 분산 마이크로서비스 환경에서 TP 규칙 정의와 검증 공수가 큼 | 도메인 주도 설계(DDD)의 애그리게이트와 사가(Saga) 패턴으로 TP를 모듈화 | TP 검증 소요 시간 |
| 직무 분리의 운영 병목 | 소규모 조직이나 장애 상황에서 분리가 유지되면 업무가 마비 | 비상 시 단독 실행을 허용하는 Break-Glass 절차와 즉시 감사 기록 | 비상 우회 건수 |
| UDI에서 CDI로의 입력 검증 결함 | 인젝션 취약점이 있는 TP를 거치면 잘못된 데이터가 CDI로 승격 | TP 진입점의 입력값 화이트리스트 검증과 정적 분석(SAST) | 검증 누락 취약점 수 |

## Ⅵ. Clark and Wilson 모델에 대한 기술사적 제언

- 핵심 요약 : 모델의 규칙을 ITGC 통제와 접근 정책에 대응시켜 감사 가능한 형태로 운영하는 방향이 바람직함.
- 회계 시스템을 운영하는 조직은 프로그램 변경 관리, 개발과 운영 환경 분리, 배치 작업 승인 절차를 Clark and Wilson의 TP·IVP 규칙과 1:1로 대응시켜 SOX(Sarbanes-Oxley Act) 내부통제 감사에 쓰는 것이 좋다.
- API 게이트웨이에서는 역할뿐 아니라 요청 시간, 위치, 이전 거래 이력 같은 속성을 평가하는 ABAC(Attribute-Based Access Control)를 적용하여 직무 분리를 위반하는 거래를 호출 단계에서 차단하는 것이 바람직하다.
- 블록체인 기반 기록은 변경 불가성을 제공하지만, 입력 검증과 승인 절차는 여전히 TP 설계로 보완해야 하므로 적용 범위를 신중히 정해야 한다.

## Ⅶ. 결론

- 핵심 요약 : Clark and Wilson 모델은 사용자, 프로그램, 데이터의 3자 관계로 상업적 무결성을 정의한 모델.
- 시사점 : 트랜잭션 무결성과 내부통제 설계의 참조 모델로 여전히 유효하며, 현대 환경에서는 속성 기반 통제와 결합해 쓰는 것이 현실적.
