---
title: "NIST AI RMF"
author: "Claude Code"
date: "2026-09-29T13:36:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → AI 거버넌스·신뢰성 → **NIST AI RMF**

## 30초 인출

- 본질: NIST AI RMF(AI Risk Management Framework)는 AI 시스템의 위험을 관리하고 신뢰할 수 있는 AI의 개발·사용을 돕는 미국 NIST의 자율 적용 프레임워크
- 메커니즘: GOVERN이 조직 전반을 관통하며 MAP(맥락·위험 식별) → MEASURE(분석·평가) → MANAGE(우선순위·대응)를 반복하고, 7가지 신뢰 가능한 특성으로 목표 수준을 판단
- 통찰: 특성 간 상충이 있고 사용 맥락마다 중요도가 달라 전 항목 일괄 적용이 어려우므로 Current Profile과 Target Profile의 격차 순서로 MANAGE 대응 우선순위 결정

<details>
<summary>핵심 용어</summary>

- **AI RMF(AI Risk Management Framework)** : NIST가 AI 시스템의 설계·개발·배포·사용 조직에 제공하는 자율 적용 위험관리 프레임워크. 2023년 1월 AI RMF 1.0(NIST AI 100-1) 발행
- **NIST(National Institute of Standards and Technology)** : AI RMF를 발행한 미국 국립표준기술연구소
- **AI actor** : AI 시스템 생애주기에서 AI를 배포·운영하는 조직과 개인을 포함해 능동적 역할을 하는 주체(OECD 정의 인용)
- **Core** : GOVERN·MAP·MEASURE·MANAGE 네 기능과 그 아래 범주·하위 범주로 구성된 위험관리 결과·행동의 집합
- **GOVERN** : 위험관리 문화와 정책·역할을 세우고 나머지 세 기능에 관통되는 기능
- **MAP** : AI 시스템의 위험을 판단할 맥락을 세우는 기능
- **MEASURE** : 정량·정성 도구로 AI 위험과 영향을 분석·평가·모니터링하는 기능
- **MANAGE** : 식별·측정된 위험에 자원을 배분하고 대응·복구·소통 계획을 실행하는 기능
- **Trustworthy AI 특성** : Valid and Reliable, Safe, Secure and Resilient, Accountable and Transparent, Explainable and Interpretable, Privacy-Enhanced, Fair with Harmful Bias Managed의 7가지
- **Profile** : 특정 환경·용도에서 조직의 요구사항·위험 허용 수준·자원에 맞춰 Core를 구체화한 것. 현재 상태를 Current Profile, 목표 상태를 Target Profile로 기술
- **Playbook** : AI RMF 결과를 달성하기 위한 실행 제안을 담은 NIST의 온라인 동반 자료
- **Generative AI Profile(NIST AI 600-1)** : 생성형 AI의 위험을 AI RMF Core에 대응시킨 교차 산업 프로파일

</details>

---

## 2~4교시 예상문제 (25점)

> NIST AI RMF(AI Risk Management Framework)의 개념과 핵심구조(Core), 신뢰 가능한 AI의 특성을 설명하고, 적용 시 한계와 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. NIST AI RMF의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **NIST AI RMF(AI Risk Management Framework)** 는 AI 시스템의 설계·개발·배포·사용 단계에서 위험을 관리하는 미국 NIST의 자율 적용 프레임워크 |
| 목적 | 신뢰할 수 있는 AI의 책임 있는 개발·사용 촉진 |

## Ⅱ. 조직 규모와 산업을 가리지 않는 AI RMF의 특징

| 특징 | 의미 |
|---|---|
| 자율 적용(voluntary) | 법적 의무가 아닌 조직의 선택 적용 |
| 산업·용도 중립 | 특정 산업이나 사용 사례에 한정하지 않는 non-sector-specific, use-case agnostic |
| 생애주기 전반 | 위험관리를 AI 시스템 생애주기 전반에 걸쳐 지속·적시 수행 |
| 위험의 정의 | 사건의 발생 확률과 결과 크기를 합친 복합 척도. 영향은 기회와 위협 모두 가능 |
| 체크리스트 아님 | 행동은 정해진 순서의 단계가 아님. 조직이 범주·하위 범주를 선택 적용 |

## Ⅲ. AI RMF의 구조와 신뢰 가능한 AI의 특성

### AI RMF Core의 4가지 기능

```text
GOVERN ── 위험관리 문화·정책·역할 (MAP·MEASURE·MANAGE에 관통)
   │
   ├─ MAP ───────→ MEASURE ───────→ MANAGE
   │  맥락 설정·      분석·평가·        우선순위·대응·
   │  위험 식별       모니터링          복구·소통
   │
   └─ 실행 순서는 고정이 아니며 반복하며 서로 참조
```

### 신뢰 가능한 AI의 7가지 특성 확대

```text
Accountable and Transparent  ← 다른 모든 특성과 관련
────────────────────────────────────────────
Safe │ Secure and Resilient │ Explainable and Interpretable
Privacy-Enhanced │ Fair with Harmful Bias Managed
────────────────────────────────────────────
Valid and Reliable  ← 신뢰성의 필요 조건, 기반
```

## Ⅳ. Core·Profile·Playbook의 층위 비교

| 구분 | 무엇을 정함 | 사용 방식 |
|---|---|---|
| Core | GOVERN 6·MAP 5·MEASURE 4·MANAGE 4개 범주와 하위 범주의 결과·행동 | 조직이 필요한 범주·하위 범주 선택 |
| Profile | 특정 환경·용도에 맞춘 Core 구현. Current·Target로 상태 구분 | 두 상태의 격차 파악 |
| Playbook | Core 결과 달성을 위한 실행 제안 | 조직 맥락에 맞춰 골라 활용 |
| Generative AI Profile(NIST AI 600-1) | 생성형 AI 고유·악화 위험 12개 범주와 Core 대응 행동 | 교차 산업 프로파일로 LLM 활용 등에 적용 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 7가지 특성이 서로 상충(예: 해석 가능성과 프라이버시)해 모두 최대화 불가 | 조직의 위험 허용 수준으로 필요한 위험관리 수준 결정(GOVERN 1.3), 임계값은 사용 맥락의 판단으로 확정 |
| 측정하기 어려운 위험이 낮은 위험으로 오인 | 측정하지 않거나 못 하는 위험·특성의 문서화(MEASURE 1.1) |
| 자율 적용이라 어느 항목부터 적용할지 기준 부재 | Current Profile과 Target Profile의 격차를 대응 우선순위 기준으로 사용 |
| 범용 프레임워크라 생성형 AI 고유 위험의 누락 | 생성형 AI 시스템에 Generative AI Profile의 위험 범주 병행 적용 |

## Ⅵ. 제언

특성별 목표 수준을 담은 Target Profile을 GOVERN에서 정하고, Current Profile과의 격차 순서로 MANAGE 대응을 실행

### Profile 격차 기반 실행 구조

```text
GOVERN: 위험 허용 수준 → 특성별 Target Profile
    ↓
MAP·MEASURE: 현재 위험·측정 결과 → Current Profile
    ↓
두 Profile의 격차 식별
    ↓
MANAGE: 격차 큰 위험 순으로 대응·잔여 위험 문서화
```

### MANAGE 확대: 우선순위 위험의 대응 선택

```text
우선순위 위험 (영향·발생 가능성·가용 자원 기준, MANAGE 1.2)
    ├─ 완화(mitigating)
    ├─ 전가(transferring)
    ├─ 회피(avoiding)
    └─ 수용(accepting)
    ↓
잔여 위험을 인수 조직·최종 사용자 기준으로 문서화(MANAGE 1.4)
```

### 선택 근거: 전 항목 일괄 적용과의 비교

| 구분 | 전 범주 일괄 적용 | 제언: 격차 기반 적용 |
|---|---|---|
| 적용 기준 | 프레임워크 항목 전체 | 특성별 Target과 현재 상태의 차이 |
| 특성 상충 처리 | 특성별 개별 최적화 | 맥락별 목표 수준 사전 결정 |
| 미측정 위험 | 누락 가능 | 문서화 후 대응 판단 |

## 출제 이력과 검증 출처

- 제138회 1교시 1번: AI RMF의 개념과 4가지 핵심구조, 7가지 신뢰 가능한 특성
- NIST AI 100-1, Artificial Intelligence Risk Management Framework (AI RMF 1.0), 2023.1
- NIST AI 600-1, Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, 2024.7

## 연결 토픽

- 이전 토픽: [IT 전략·관리 개요](./index.md)
- 연관 토픽: [AI 거버넌스 플랫폼](./050_ai_governance_platform.md), [AI 프라이버시 리스크 관리 모델](./054_ai_privacy_risk_management_model.md), [ISO 31000](./069_iso_31000.md)
- 다음 토픽: [부정적 위험 대응 전략](./040_negative_risk_response_strategy.md)
