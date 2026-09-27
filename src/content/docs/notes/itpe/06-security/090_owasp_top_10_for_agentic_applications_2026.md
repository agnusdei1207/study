---
title: "OWASP Top 10 for Agentic Applications 2026"
author: "Codex"
date: "2026-09-27T17:11:00+09:00"
tags:
  - "notes-security"
sidebar:
  order: 90
  label: "090. OWASP Top 10 for Agentic Applications 2026"
  badge:
    text: "서브"
    variant: note
extra:
  keyword_grade: "서브"
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

AI 보안 → 에이전트 실행 위험 → OWASP Agentic Top 10 2026

## 30초 인출

- 본질: 에이전틱 AI 애플리케이션에서 목표·도구·권한·에이전트 간 통신이 만드는 보안 위험의 분류
- 메커니즘: 불신 입력의 지시 승격 → 계획·도구 호출 오염 → 외부 시스템에 영향; 업무 목표 검증·최소 권한·고영향 작업 승인으로 통제

---

<details><summary>핵심 용어</summary>

- 목표 탈취: 불신 입력으로 에이전트의 작업 목표를 바꾸는 공격.
- 연쇄 실패: 한 에이전트의 오류가 다른 구성요소로 전달되어 피해가 커지는 현상.

</details>

## 1교시 예상문제 (10점)

> OWASP Agentic AI Top 10의 목적과 주요 위험을 설명하시오. (예상·10점)

---

## 1교시 10점 답안

**공통 개요**

| 구분 | 핵심 |
|---|---|
| 정의 | OWASP Agentic Top 10 2026은 에이전트의 목표·도구·신원·협업 과정에서 발생하는 열 가지 보안 위험의 분류 |
| 목적 | 외부 상태를 바꾸는 에이전트의 실행 권한과 연쇄 피해 통제 |

OWASP Top 10 for Agentic Applications 2026은 자율적으로 계획·도구 호출·협업하는 AI 에이전트의 주요 보안 위험을 정리한 OWASP 가이드. 목표 탈취, 도구 오용, 권한 남용, 공급망, 예상치 못한 코드 실행, 기억·문맥 오염, 에이전트 간 통신, 연쇄 실패, 인간의 과신, 악성 에이전트를 포함. 불신 입력과 지시의 분리, 도구별 최소 권한, 위험 행위 승인, 실행 격리, 호출 기록과 모니터링으로 대응.

---

## 2~4교시 예상문제 (25점)

> OWASP Agentic AI Top 10의 위험 분류와 에이전트의 목표·도구·권한 통제 방안을 설명하시오. (예상·25점)

---

## 2~4교시 25점 답안

**공통 개요**

| 구분 | 핵심 |
|---|---|
| 정의 | OWASP Agentic Top 10 2026은 에이전트의 목표·도구·신원·협업 과정에서 발생하는 열 가지 보안 위험의 분류 |
| 목적 | 외부 상태를 바꾸는 에이전트의 실행 권한과 연쇄 피해 통제 |

### Ⅰ. 특징과 공식 분류
일반 LLM 출력 위험에 더해 도구 실행과 에이전트 간 위임이 외부 상태를 바꿀 수 있는 위험. OWASP 분류는 다음과 같음.

| 영역 | 공식 항목 |
|---|---|
| 목표·도구·권한 | ASI01 Agent Goal Hijack, ASI02 Tool Misuse and Exploitation, ASI03 Identity and Privilege Abuse |
| 공급망·실행·문맥 | ASI04 Agentic Supply Chain Vulnerabilities, ASI05 Unexpected Code Execution, ASI06 Memory and Context Poisoning |
| 협업·운영 | ASI07 Insecure Inter-Agent Communication, ASI08 Cascading Failures, ASI09 Human-Agent Trust Exploitation, ASI10 Rogue Agents |

### Ⅱ. 위협 흐름
```text
불신 콘텐츠 유입 → 목표·문맥 오염 → 도구 호출 또는 권한 오용
→ 다른 에이전트로 전파·연쇄 실패 → 데이터·시스템 영향
```
이는 가능한 시나리오이며 모든 항목이 한 번에 발생하는 필수 공격 순서는 아님.

### Ⅲ. 통제 설계
| 통제 지점 | 확인 항목 |
|---|---|
| 입력·계획 | 외부 데이터의 지시 승격 차단, 업무 목표 검증 |
| 신원·도구 | 호출 주체 확인, 도구별 권한·입력 제약, 고영향 작업 승인 |
| 실행·협업 | 격리, 예산·반복 제한, 에이전트 간 출처와 전달 내용 확인 |
| 운영 | 호출·승인·결과 로그, 이상 행위 탐지와 복구 절차 |

## 기술사적 제언

업무 목표와 도구 권한을 분리하고 외부 상태를 바꾸는 호출은 정책 검사·승인을 통과하게 한다.

## 출제 이력과 검증 출처

- 확인한 제132~140회 공식 문제지에서 이 표제어의 직접 출제를 확인하지 못함. 그 밖의 회차는 원문 미대조.

- [OWASP Top 10 for Agentic Applications for 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
