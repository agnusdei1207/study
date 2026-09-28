---
title: "ITSM"
author: "Claude Code"
date: "2026-09-28T16:02:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Opus 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → IT 서비스 관리·운영 거버넌스 → **ITSM**

## 30초 인출

- 본질: ITSM(IT Service Management)은 IT를 장비가 아닌 고객이 쓰는 서비스 단위로 보고, 서비스의 설계·전환·운영·개선을 관리하는 체계
- 메커니즘: 서비스 수준 합의를 기준으로 장애 복구(Incident) → 원인 제거(Problem) → 변경 승인(Change) → 배포(Release)를 기록으로 잇고 결과를 개선에 반영
- 통찰: 원인 분석 없이 복구만 하면 장애가 반복되므로 반복 장애의 Problem 등록과 해결 변경 추적

<details>
<summary>핵심 용어</summary>

- **ITSM(IT Service Management)** : IT를 고객이 이용하는 서비스 단위로 설계·전환·운영·개선하는 관리 체계
- **ITIL(Information Technology Infrastructure Library)** : 서비스 가치 시스템과 실천 활동(Practice)을 제시하는 ITSM 모범 실무 프레임워크
- **ISO/IEC 20000-1** : 서비스 관리 시스템(SMS)의 수립·운영·유지·개선 요구사항을 정한 인증용 국제표준
- **SMS(Service Management System)** : 서비스 관리의 방침·목표·프로세스를 통합해 운영하는 경영 시스템
- **SLA(Service Level Agreement)** : 서비스 제공자와 고객이 합의한 서비스 수준과 측정·보고 기준
- **Incident** : 서비스의 계획되지 않은 중단이나 품질 저하. 관리 목표는 신속한 서비스 복구
- **Problem** : 하나 이상의 Incident를 일으키는 근본 원인. 관리 목표는 원인 제거와 재발 방지
- **KEDB(Known Error Database)** : 원인이 밝혀진 오류와 임시 우회책(Workaround)을 기록한 지식 저장소
- **Change** : 서비스에 영향을 주는 구성요소의 추가·수정·제거. 위험 평가 후 승인
- **CAB(Change Advisory Board)** : 변경의 영향·위험을 검토해 승인 결정을 돕는 자문 기구
- **CMDB(Configuration Management Database)** : 구성항목(CI)의 속성과 상호 관계를 관리하는 데이터베이스

</details>

---

## 2~4교시 예상문제 (25점)

> ITSM(IT Service Management)의 개념과 운영 체계를 설명하고, 운영 시 한계와 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. ITSM의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **ITSM(IT Service Management)** 은 IT를 고객이 이용하는 서비스 단위로 설계·전환·운영·개선하는 관리 체계 |
| 목적 | 합의한 서비스 수준의 안정적 제공과 반복 장애·변경 실패의 감소 |

## Ⅱ. 기술 운영 관리와 구별되는 ITSM의 특징

| 특징 | 의미 |
|---|---|
| 서비스 단위 관리 | 장비 가동률보다 고객의 서비스 이용 결과를 기준으로 관리 |
| 합의 기반 | **SLA** 로 약속한 수준을 운영·보고의 기준으로 사용 |
| 활동 간 연계 | 복구·원인 분석·변경·배포를 분리하되 기록으로 연결 |
| 생애주기 관리 | 설계·전환·운영·개선의 반복 |

## Ⅲ. ITSM 운영 체계와 장애·변경 연계 흐름

### ITSM 운영 체계

```text
ITSM
    │
    ├─ 기준 ── SLA: 고객과 합의한 서비스 수준
    │
    ├─ 관리 체계
    │     ├─ ITIL 4 ── 실천 지침
    │     └─ ISO/IEC 20000-1 ── SMS 요구사항
    │
    ├─ 운영 활동
    │     ├─ 해결 ── Incident·Problem·서비스 요청
    │     └─ 전환 ── Change·Release·Deployment
    │
    └─ 기반 ── Service Desk·CMDB·KEDB
```

### 운영 활동 확대: 장애에서 개선까지의 흐름

```text
서비스 중단 발생
    ↓
Incident: 기록·우선순위·서비스 복구
    ↓ 반복·중대 장애
Problem: 근본 원인 분석·KEDB 등록
    ↓ 해결책 확정
Change: 영향·위험 평가 후 승인
    ↓
Release·Deployment: 배포와 CMDB 갱신
    ↓
재발 여부 확인 후 Problem 종료
```

## Ⅳ. ITIL 4와 ISO/IEC 20000-1의 역할 비교

| 구분 | ITIL 4 | ISO/IEC 20000-1 |
|---|---|---|
| 성격 | 모범 실무 지침 | 인증용 요구사항 표준 |
| 핵심 구조 | 서비스 가치 시스템(지도 원칙·거버넌스·서비스 가치 사슬·실천 활동·지속적 개선)과 4가지 관점(조직과 사람·정보와 기술·파트너와 공급자·가치 흐름과 프로세스) | SMS의 계획·운영·성과 평가·개선 조항 |
| 적용 방식 | 조직에 맞춰 선택·조정 | 요구사항 충족 여부를 심사 |
| 활용 | 운영 활동의 설계 방법 | 관리 체계의 적합성 입증 |

ITIL 4는 활동을 어떻게 할지, ISO/IEC 20000-1은 무엇을 갖춰야 하는지를 제시하는 보완 관계. 2026년부터 ITIL(Version 5)이 Foundation부터 단계적으로 공개되고 ITIL 4 과정과 자격도 병행 유지

## Ⅴ. ITSM 운영의 한계와 방안

| 한계 | 방안 |
|---|---|
| 장애 복구 후 원인 분석 없이 종료되어 재발 반복 | 반복·중대 장애의 **Problem** 등록 기준과 원인 제거 책임자 지정 |
| 원인 해결책이 변경으로 이어지지 않아 **KEDB** 에 머묾 | Problem 기록과 해결 **Change** 의 연결 및 재발 확인 후 종료 |
| 모든 변경의 **CAB** 심의로 승인 병목 | 위험 기준의 표준·일반·긴급 변경 구분과 표준 변경 사전 승인 |
| 배포 후 **CMDB** 미갱신으로 영향 분석 오류 | 배포 결과와 CMDB 대조를 배포 완료 조건으로 설정 |

## Ⅵ. 제언

반복 장애를 Problem으로 등록해 원인 해결 변경까지 한 기록으로 추적하고, 재발이 확인되지 않을 때만 Problem을 종료하는 운영 기준 수립

### 장애 원인 추적 책임 구조

```text
Problem 기록
    │
    ├─ 서비스 데스크 ── 반복 장애의 연결·등록
    │
    ├─ Problem 담당자 ── 원인 분석과 해결책 확정
    │
    └─ 변경 관리자 ── 해결 변경의 승인·배포 확인
```

### Problem 담당자 확대: 종료 판정 절차

```text
해결 변경 배포 완료
    ↓
관찰 기간 동안 같은 유형 장애 발생 확인
    ├─ 재발 → 원인 재분석
    └─ 재발 없음 → KEDB 갱신 후 Problem 종료
```

### 선택 근거: 복구 중심 운영과의 비교

| 구분 | 복구 중심 운영 | 제언: 원인 추적 연결 운영 |
|---|---|---|
| 성과 기준 | 장애 복구 시간 | 복구 시간과 재발 건수 |
| 장애 종료 시점 | 서비스 복구 직후 | 원인 해결 변경의 재발 확인 후 |
| 기록 연결 | Incident 단독 | Incident·Problem·Change 연결 |
| 책임 | 운영팀 복구 | Problem 담당자의 원인 제거 |

## 출제 이력과 검증 출처

- 제133회 2교시 3번: ISO/IEC 20000 기준의 ITSM 개념과 서비스 설계·구축·전환 활동
- [ISO/IEC 20000-1:2018 — Service management system requirements](https://www.iso.org/standard/70636.html)
- [PeopleCert: ITIL 4 Foundation](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-foundation-2565) — 서비스 가치 시스템, 4가지 관점, 7개 지도 원칙
- [PeopleCert: ITIL Foundation (Version 5)](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-5-foundation-version-50-4154), [ITIL (Version 5) 안내](https://www.peoplecert.org/news-and-announcements/itil-version-5-explained) — 단계적 공개, ITIL 4 자격 유지

## 연결 토픽

- 이전 토픽: [ISO 21500](./043_iso_21500.md)
- 연관 토픽: [SLA](./006_sla.md), [ISO/IEC 38500](./002_iso_iec_38500.md), [IT 아웃소싱](./033_it_outsourcing.md)
- 다음 토픽: [MECE](./045_mece.md)
