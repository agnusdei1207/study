---
title: "CI/CD(Continuous Integration/Continuous Delivery)"
author: "Claude Code"
date: "2026-09-29T19:18:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 빌드·배포·DevOps → **CI/CD(Continuous Integration/Continuous Delivery)**

## 30초 인출

- 본질: CI/CD는 코드 변경을 자주 통합해 빌드·시험하고(CI) 배포 가능한 상태로 유지하며 운영에 전달(CD)하는 자동화 파이프라인
- 메커니즘: 커밋이 빌드·정적 분석·단위 시험·통합 시험을 거쳐 품질 게이트를 통과하면 배포 가능한 산출물이 되고 승인 또는 자동으로 운영에 반영
- 통찰: 배포 직전에 보안 점검을 하면 병목과 늦은 수정이 생기므로 파이프라인 각 단계에 보안 점검(DevSecOps)을 자동으로 넣어 취약점을 앞 단계에서 차단

<details>
<summary>핵심 용어</summary>

- **지속적 통합(CI, Continuous Integration)** : 변경을 자주 공유 저장소에 통합하고 자동으로 빌드·시험하는 방식
- **지속적 제공(Continuous Delivery)** : 통합된 코드를 언제든 운영에 배포할 수 있는 상태로 유지하는 방식
- **지속적 배포(Continuous Deployment)** : 시험을 통과한 변경을 사람 개입 없이 운영에 자동 배포하는 방식
- **품질 게이트(Quality Gate)** : 다음 단계로 넘어가기 위한 품질·보안 기준
- **DevSecOps** : 파이프라인 각 단계에 보안 활동을 통합한 DevOps
- **SAST·DAST·SCA** : 소스 코드 정적 분석, 실행 중 동적 분석, 오픈소스 구성요소 분석

</details>

---

## 2~4교시 예상문제 (25점)

> CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. CI/CD의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **CI/CD** 는 코드 변경을 자동으로 빌드·시험하고 운영까지 전달하는 파이프라인 |
| 목적 | 변경 전달의 속도·안정성 확보와 수동 작업 감소 |

## Ⅱ. 수동 배포와 구별되는 특징

| 특징 | 의미 |
|---|---|
| 자동화 | 빌드·시험·배포 자동 수행 |
| 잦은 통합 | 작은 변경의 빠른 통합 |
| 게이트 기반 | 품질 기준 통과 후 진행 |

## Ⅲ. 파이프라인 구조와 DevSecOps 통합

### CI/CD 파이프라인

```text
커밋 → 빌드 → 단위 시험 → 통합 시험 → 스테이징 배포 → 운영 배포
```

### 확대: 단계별 보안 점검(DevSecOps)

```text
커밋 ── 비밀정보 노출 검사
빌드 ── SCA(오픈소스 취약점·라이선스), SAST(정적 분석)
시험·스테이징 ── DAST(동적 분석)
배포 ── 이미지 취약점 검사·서명, 배포 승인 정책
운영 ── 모니터링·취약점 대응
```

## Ⅳ. 지속적 제공과 배포의 비교, 보안 점검 방식

### 지속적 제공과 지속적 배포

| 구분 | 지속적 제공(Delivery) | 지속적 배포(Deployment) |
|---|---|---|
| 운영 반영 | 승인 후 수동 반영 | 자동 반영 |
| 적합 조건 | 규제·승인 필요 | 높은 자동 시험 신뢰도 |

### 보안 점검 방식

| 점검 | 시점 | 대상 |
|---|---|---|
| SAST | 빌드 | 소스 코드 |
| SCA | 빌드 | 오픈소스 구성요소·라이선스 |
| DAST | 시험·스테이징 | 실행 중인 애플리케이션 |
| 이미지 스캔 | 배포 전 | 컨테이너 이미지 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 배포 직전 보안 점검으로 일정 지연 | 초기 단계부터 자동 보안 점검(Shift-Left) |
| 보안 점검 오탐으로 파이프라인 지연 | 위험도 기준의 차단 정책과 예외 관리 |
| 파이프라인 자체의 자격 증명 유출 | 비밀 정보의 저장소 분리와 최소 권한 |

## Ⅵ. 제언

파이프라인 각 단계에 자동 보안 점검을 넣고, 위험도 기준을 넘는 결과는 다음 단계로 진행하지 않도록 품질 게이트로 차단

### 게이트 기반 보안 통제

```text
단계별 보안 점검 실행
    ↓
결과 판정
    ├─ 기준 초과(높은 위험도) → 파이프라인 중단·수정
    └─ 기준 이내 → 다음 단계
```

### 선택 근거: 배포 직전 점검과의 비교

| 구분 | 배포 직전 점검 | 제언: 단계별 자동 점검 |
|---|---|---|
| 취약점 발견 시점 | 후반 | 초기 |
| 수정 비용 | 큼 | 작음 |
| 배포 지연 | 큼 | 완화 |

## 출제 이력과 검증 출처

- 제135회 2교시 2번: CI/CD 파이프라인에서 DevSecOps 적용방안
- NIST SP 800-218 Secure Software Development Framework (SSDF)

## 연결 토픽

- 이전 토픽: [Apache Iceberg](./094_apache_iceberg_open_table_format.md)
- 연관 토픽: [DevOps](./002_devops.md), [무중단 배포](./007_zero_downtime_deployment.md), [플랫폼 엔지니어링](./033_platform_engineering.md)
- 다음 토픽: [OpenTelemetry](./096_opentelemetry.md)
