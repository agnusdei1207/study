---
title: "DevSecOps"
author: "OpenAI"
date: "2026-09-24T22:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

안전한 소프트웨어 개발 → 개발·보안·운영 통합 → CI/CD 보안

## 30초 인출

- **본질**: DevSecOps는 보안을 개발·운영 생애주기에 포함하고 팀이 함께 책임지는 소프트웨어 제공 방식.
- **메커니즘**: 변경 → 자동 점검·위험 판정 → 수정 피드백 → 승인된 배포 → 운영 결과를 다음 변경에 반영.
- **핵심**: 도구 설치보다 위험기반 기준, 실행 가능한 피드백, 예외 추적이 중요.

<details><summary>핵심 용어</summary>

- **DevSecOps**: Development, Security, and Operations를 결합해 보안을 개발·배포·운영에 통합하는 방식.
- **CI/CD(Continuous Integration/Continuous Delivery or Deployment)**: 코드 변경의 통합·검증과 전달 또는 배포를 자동화하는 개발 흐름.
- **SAST(Static Application Security Testing)**: 프로그램을 실행하지 않고 소스·바이트코드를 분석하는 보안 시험.
- **SCA(Software Composition Analysis)**: 소프트웨어 의존성의 구성·취약점·라이선스 위험을 분석하는 활동.
- **DAST(Dynamic Application Security Testing)**: 실행 중인 애플리케이션에 요청을 보내 외부에서 드러나는 취약점을 시험하는 방식.
- **IaC(Infrastructure as Code)**: 인프라 구성을 코드와 선언형 설정으로 관리하는 방식.
- **SSDF(Secure Software Development Framework)**: NIST가 SDLC에 통합할 보안 개발 실천을 제시한 프레임워크.
- **SBOM(Software Bill of Materials)**: 소프트웨어에 포함된 구성요소와 관계를 기록한 목록.
</details>

---

## 1교시 예상문제 (10점)

---

> DevSecOps의 개념과 CI/CD에서 보안을 통합하는 기본 흐름을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **DevSecOps**는 보안을 개발·운영 생애주기에 포함하고 팀이 함께 책임지는 소프트웨어 제공 방식. |
| 목적 | 변경 속도를 유지하면서 취약점을 조기에 발견·수정하고 안전한 배포 근거를 확보. |

### Ⅱ. CI/CD 보안 통합 흐름

```text
요구·코드 변경
      ↓
자동 빌드·시험 ── SAST·SCA·시크릿 검사
      ↓ 결과·위험 확인
수정 피드백 또는 승인 게이트
      ↓
배포·운영 모니터링
      └──────── 발견사항을 다음 변경에 반영
```

점검 결과는 위험도와 서비스 중요도에 따라 배포 차단·예외 승인·추적을 구분하고 수정 뒤 재시험.

제언: 오탐과 수정경로를 함께 관리하는 위험기반 게이트부터 적용해 팀별 보안 피드백을 정착.

---

## 2~4교시 예상문제 (25점)

---

> CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오. (제135회 2교시 2번)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **DevSecOps**는 보안을 개발·운영 생애주기에 포함하고 팀이 함께 책임지는 소프트웨어 제공 방식. |
| 목적 | 변경 속도를 유지하면서 취약점을 조기에 발견·수정하고 안전한 배포 근거를 확보. |

## Ⅱ. 파이프라인 통합 원리

```text
계획·요구사항 → 코드 변경 → 빌드·시험 → 승인·배포 → 운영
      ↑              │            │            │          │
위협모델 갱신   코드·시크릿 검사 SAST·SCA·시험  정책검사  로그·취약점 감시
      └────────── 결함·사고 피드백과 재검증 ─────────────┘
```

NIST SSDF는 기존 개발수명주기에 통합할 보안 실천을 제시하며, 특정 제품이나 파이프라인 도구를 강제하지 않음.

## Ⅲ. 단계별 통제와 증거

| 단계 | 통제 | 추적 근거 |
|---|---|---|
| 계획 | 보안 요구·위협모델·위험 기준 | 승인된 요구와 위협 시나리오 |
| 코드·빌드 | 시크릿 검사, SAST, SCA, 빌드 무결성 | 커밋·빌드 식별자, 검사 결과, SBOM |
| 시험 | DAST·통합 보안시험·수정 재검증 | 재현 정보, 결함 연결, 재시험 결과 |
| 배포 | IaC·이미지·서명·설정 정책 확인 | 산출물 버전, 승인, 배포 이력 |
| 운영 | 취약점·로그·런타임 징후 대응 | 탐지·조치 기록, 개선 작업 |

SAST는 실제 실행 경로를 모두 확인하지 못하고 DAST는 시험한 구성·경로에 제한되므로 상호 보완과 수동 검토가 필요.

## Ⅳ. 게이트와 협업 운영

| 운영 요소 | 적용 방식 |
|---|---|
| 배포 기준 | 자산 중요도·노출도·악용 가능성에 따라 심각도와 조치기준 설정 |
| 예외 | 사유·책임자·만료일·보완통제를 기록하고 재검토 |
| 피드백 | 재현 가능한 근거와 수정 위치를 개발팀에 전달 |
| 지표 | 처리시간·재발·오탐·예외 만료로 규칙과 절차 개선 |

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 초기부터 모든 경보를 일괄 차단하면 오탐·지연으로 우회 가능성이 커질 수 있음. | 서비스 위험에 맞는 게이트를 우선 적용하고 오탐·예외·수정 시간을 측정해 규칙을 단계적으로 조정하는 방안. |

## 출제 이력과 검증 출처

- 제135회 2교시 2번 원문: “CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오.”
- [NIST SP 800-218: Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — SSDF 1.1 최종본.
- [NIST SSDF publications](https://csrc.nist.gov/projects/ssdf/publications) — SSDF 1.2 초안과 관련 자료의 최신 상태.
- [NIST SP 800-218A](https://csrc.nist.gov/pubs/sp/800/218/a/final) — 생성형 AI·기반모델 개발을 위한 SSDF 프로파일.
