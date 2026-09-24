---
title: "AI 보안 플랫폼 (AI Security Platform)"
author: "OpenAI"
date: "2026-09-24T22:25:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "GPT-6"
---

## 지식 로드맵 내 현재 위치

AI 보안 → 조직 보안 아키텍처 → AI 보안 플랫폼

## 30초 인출

- **본질:** **AI 보안 플랫폼**은 조직의 AI 자산과 사용 경로에 보안 통제를 연결하는 솔루션 범주
- **구조:** 자산·구성 상태 관리와 요청·응답의 실행 시점 통제
- **판단:** 기능과 범위는 제품마다 달라 요구사항·연동·성능 기준으로 평가

<details>
<summary>핵심 용어</summary>

- **AI (Artificial Intelligence):** 데이터로부터 패턴을 학습하거나 추론해 과업을 수행하는 인공지능 기술
- **AI 보안 플랫폼:** AI 자산·사용 경로를 파악하고 구성 위험이나 요청 흐름에 보안 통제를 적용하는 솔루션 범주
- **AI-SPM (Artificial Intelligence Security Posture Management):** AI 자산·구성·의존성의 보안 상태와 위험을 점검하는 관리 기능
- **런타임 보호(runtime protection):** AI 요청·응답·도구 실행 중 정책을 검사·집행하는 통제
- **AI 자산명세(AI Bill of Materials):** AI 애플리케이션의 구성요소·데이터·모델 자산을 식별한 목록
- **NIST (National Institute of Standards and Technology):** 미국 국립표준기술연구소
- **AI RMF (Artificial Intelligence Risk Management Framework):** NIST의 자율적 AI 위험관리 프레임워크
- **AI 게이트웨이(AI gateway):** 애플리케이션의 모델 요청을 중계하며 정책·인증·기록을 적용하는 구성요소
- **API (Application Programming Interface):** 애플리케이션 간 기능·데이터 요청을 위한 인터페이스
- **IAM (Identity and Access Management):** 사용자·서비스의 신원과 접근권한 관리
- **DLP (Data Loss Prevention):** 민감정보의 노출·반출을 탐지·통제하는 기능
- **SIEM (Security Information and Event Management):** 보안 이벤트를 수집·상관분석하는 관리 체계
- **오탐(false positive):** 정상 사용이나 콘텐츠를 탐지·차단 대상으로 잘못 분류하는 결과
</details>

---
## 1교시 예상문제 (10점)

> AI 보안 플랫폼의 개념과 자산관리·런타임 보호의 주요 기능을 설명하시오. *(10점 예상문제)*

---
## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **AI 보안 플랫폼**은 조직의 AI 자산과 사용 경로에 보안 통제를 연결하는 솔루션 범주 |
| 목적 | AI 관련 자산·구성 위험과 사용 중 보안 위협의 가시성·통제성 향상 |

### Ⅱ. 관리 기능과 처리 흐름

```text
AI 자산·구성 ──> 목록화·상태 점검 ──> 위험 확인·개선

사용자 요청 ──> AI 게이트웨이 ──> 정책 검사 ──> 모델·도구
                     └── 요청·응답 기록 ──> 모니터링
```

| 기능 | 관리 대상 |
|---|---|
| 자산·구성 관리 | 모델·애플리케이션·데이터·의존성·연결 경로 |
| 런타임 보호 | 프롬프트·응답·도구 요청·민감정보 |
| 가시성·감사 | 정책 결정·사용행위·위험 조치 기록 |

**제언:** 제품 명칭보다 자산 발견 범위와 요청 경로별 통제·기록 기능을 먼저 확인

---
## 2~4교시 예상문제 (25점)

> AI 보안 플랫폼의 자산관리·런타임 통제 구조와 주요 기능을 설명하고, 기존 보안체계와의 연동·단계적 도입방안을 제시하시오. *(25점 예상문제)*

---
## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **AI 보안 플랫폼**은 조직의 AI 자산과 사용 경로에 보안 통제를 연결하는 솔루션 범주 |
| 목적 | AI 관련 자산·구성 위험과 사용 중 보안 위협의 가시성·통제성 향상 |

```text
관리 영역: 코드·클라우드·모델 자산 → 구성·의존성 위험 → 조치·상태 추적

실행 영역: 사용자 요청 → 인증·AI 게이트웨이 → 모델·도구
                                  ├── 정책 검사·필터
                                  └── 사용 기록·경보
```

AI 보안 플랫폼은 단일 표준 제품 구조를 뜻하지 않는 솔루션 범주이며, 관리 영역과 실행 영역의 포함 범위는 구현마다 다름.

## Ⅱ. 핵심 기능

| 기능 영역 | 주요 기능 | 통제 대상 |
|---|---|---|
| 자산·상태 관리 | AI 앱·모델·데이터·에이전트·의존성 식별, 위험 우선순위화 | 미승인 자산·취약 구성·과도한 노출 |
| 실행 시점 통제 | 호출 경로 중계, 인증·정책·입출력 검사 | 비인가 사용·민감정보·악성 지시 |
| 로그·대응 | 요청·정책결정 기록, 경보·사고 분석 | 오용·정책 위반·이상행위 |
| 거버넌스 연계 | 위험·소유자·조치 현황 연결 | 책임 공백·개선 미완료 |

## Ⅲ. 기능 범위 구분

| 기능 | 관리 시점 | 기대 역할 |
|---|---|---|
| AI-SPM (Artificial Intelligence Security Posture Management) | 개발·배포 전후의 자산·구성 점검 | 위험·취약 구성의 식별과 개선 추적 |
| AI 게이트웨이·런타임 보호 | 서비스 요청·응답 처리 중 | 사용정책·민감정보·도구 요청의 검사 |
| AI 자산명세(AI Bill of Materials) | 구성·공급망 식별 | 모델·라이브러리·데이터 자산의 목록화 |

이 기능명은 제품별 범위를 설명하는 용어이며 표준화된 필수 모듈 목록은 아님.

## Ⅳ. 기존 보안체계와 연동

| 연동 대상 | 연동 목적 | 확인 사항 |
|---|---|---|
| IAM (Identity and Access Management) | 사용자·서비스 신원과 권한 적용 | 호출 주체·모델·도구 계정의 권한 분리 |
| DLP (Data Loss Prevention) | 민감정보 탐지·반출 통제 | AI 입력·출력의 검사범위와 예외 |
| SIEM (Security Information and Event Management) | 보안 이벤트 상관분석·대응 | 로그 형식·보관·연계 권한 |
| 애플리케이션·API | 요청경로와 서비스 정책 연결 | 우회 호출·미등록 모델·성능 영향 |

## Ⅴ. 한계와 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 제품마다 AI 자산 발견과 요청중계 범위가 다르면 하나의 도구가 전체 AI 사용을 포괄한다고 오인할 수 있음 | 조직의 모델·애플리케이션·사용경로를 먼저 목록화하고, 미발견 영역을 보완할 연동점과 책임자를 정한 뒤 단계 도입하는 적용안 제안 |
| 게이트웨이를 통하지 않는 API·개발환경 호출은 실행 시점 정책에서 빠질 수 있음 | 자산·호출경로 목록과 게이트웨이 로그를 대조해 우회경로를 찾고, 개발·클라우드 설정 점검과 함께 통제 범위를 보완 |

## 검증 출처

- NIST, [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) — 조직의 AI 위험관리와 자율 프레임워크
- Microsoft Learn, [AI security posture management](https://learn.microsoft.com/en-us/azure/defender-for-cloud/ai-security-posture) — AI 앱 발견, 보안 상태 권고, 위험 경로 분석의 제품 사례
- Google Cloud, [AI Protection overview](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview) — AI 자산 보안상태 가시성·위협 탐지 제품 사례

## 연결 토픽

- [AI 보안 안내서](./034_ai_security_guidelines_msit_kisa/)
- [프롬프트 인젝션](./033_prompt_injection/)
