---
title: "OWASP Top 10 for LLM Applications"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "053. OWASP Top 10 for LLM Applications"
  badge:
    text: "기초"
    variant: note
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

AI 보안 → 생성형 AI 애플리케이션 위험 → OWASP LLM Top 10 보안 통제

## 30초 인출

- **본질:** LLM 및 생성형 AI 애플리케이션을 배포·운영할 때 발생하는 핵심 보안 취약점 10가지를 정의하고 아키텍처적 방어 지침을 제시하는 OWASP 보안 프레임워크
- **메커니즘:** 입력 신뢰 경계(인젝션 필터) → 모델 계층(가중치/프롬프트 보호) → 검색 계층(RAG/벡터 무결성) → 도구 계층(최소권한/HITL) → 런타임 자원 제어
- 통찰: 모델 자체의 안전성 정렬에만 의존하지 않고 RAG 검색 문서 및 외부 도구 호출 접점의 입력 검증, 출력 인코딩, 최소 권한 실행 환경이 결합된 애플리케이션 레벨의 제로 트러스트 방어 체계 필수

<details><summary>핵심 용어</summary>

- **OWASP GenAI Security Project:** 대규모 언어 모델(LLM) 생태계의 급격한 변화에 맞추어 2025년 개정된 애플리케이션 보안 가이드라인.
- **LLM01 Prompt Injection:** 직접 탈옥(Jailbreak) 또는 웹문서/RAG를 통한 간접 프롬프트 주입으로 모델의 본래 제약을 우회하는 공격.
- **LLM06 Excessive Agency:** 에이전트에 불필요하게 넓은 쓰기/삭제 권한이나 자율성을 부여하여 발생하는 의도치 않은 시스템 손상 취약점.
- **LLM08 Vector and Embedding Weaknesses:** RAG 검색에 쓰이는 벡터 데이터베이스 오염, 임베딩 역추출, 비인가 청크 접근 취약점.
- **LLM10 Unbounded Consumption:** 대량의 비정상 토큰 요청이나 DoS 공격으로 인해 클라우드 API 과금 폭탄 및 서비스 거부를 유발하는 위험.

</details>

---

## 2~4교시 예상문제 (25점)

> 생성형 AI 및 대규모 언어 모델(LLM) 환경의 대표적 보안 취약점인 'OWASP Top 10 for LLM Applications (2025)'의 핵심 항목을 설명하고, RAG 및 에이전틱 도구 연계 시 발생하는 신뢰 경계 붕괴 극복을 위한 방어 아키텍처를 제시하시오. (기출·제136회 4교시 5번)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 대규모 언어 모델(LLM)을 활용하는 웹, API, 자율 에이전트 애플리케이션에서 가장 빈번하게 발생하는 상위 10대 보안 취약점 및 완화 표준 목록 |
| 목적 | AI 개발자 및 보안 아키텍트에게 위협 모델링 기준을 제공하고, 데이터-모델-도구 연계 전주기에서 내재적 안전성 확보 |

## Ⅱ. OWASP LLM Top 10의 주요 특징

| 특징 | 세부 내용 | 구현 요소 |
|---|---|---|
| 자연어 기반 취약점 | 결정론적 코드가 아닌 확률적 자연어 입력(프롬프트) 자체가 공격 벡터로 작용 | 의미론적 분석기, 가드레일 |
| 신뢰 경계의 모호성 | 사용자 입력과 RAG 검색 문서가 단일 컨텍스트 윈도우에 결합되어 명령어와 데이터 혼재 | 데이터-지시문 분리 파서 |
| 2025년 최신 개정 반영 | 벡터 DB 취약점(LLM08), 시스템 프롬프트 유출(LLM07), 오정보(LLM09) 등 최신 동향 추가 | 에이전트 및 RAG 보안 특화 |
| 공급망 및 자원 관리 | 오픈소스 사전학습 가중치 공급망(LLM03)과 토큰 과소비 DoS(LLM10) 통제 포함 | Safetensors, 토큰 쿼터제 |

## Ⅲ. OWASP Top 10 for LLM (2025) 분류 체계 및 방어 아키텍처

```text
[ 1. 사용자 / 외부 데이터 입력 ]
         │ (사용자 프롬프트 / RAG 벡터 문서)
         ▼
┌────────────────────────────────────────────────────────┐
│ [입력 계층 방어]                                       │
│  - LLM01: Prompt Injection 차단 (NeMo Guardrails)       │
│  - LLM07: System Prompt Leakage 방어 (접근 제어)        │
│  - LLM08: Vector DB 오염 및 비인가 청크 격리          │
└────────────────────────┬───────────────────────────────┘
                         ▼
┌────────────────────────────────────────────────────────┐
│ [모델 및 공급망 계층]                                  │
│  - LLM03: Supply Chain (Safetensors 포맷, 서명 검증)   │
│  - LLM04: Data & Model Poisoning (학습 데이터 무결성)   │
│  - LLM10: Unbounded Consumption (토큰 스로틀링/WAF)     │
└────────────────────────┬───────────────────────────────┘
                         ▼
┌────────────────────────────────────────────────────────┐
│ [출력 및 실행 계층]                                    │
│  - LLM02: Sensitive Info Disclosure (개인정보 마스킹) │
│  - LLM05: Improper Output Handling (출력 인코딩/검증)   │
│  - LLM06: Excessive Agency (PEP 도구 통제 및 HITL 게이트)│
│  - LLM09: Misinformation (환각 탐지 및 신뢰도 검증)   │
└────────────────────────────────────────────────────────┘
```

| 취약점 코드 | 취약점 명칭 (2025) | 공격 메커니즘 및 방어 대책 |
|---|---|---|
| LLM01 | Prompt Injection | 직접 탈옥 및 웹 RAG를 통한 악성 지시 주입 / 듀얼 가드레일 및 구조화된 입력 분리 |
| LLM02 | Sensitive Information Disclosure | 모델 응답을 통한 PII/내부 기밀 유출 / 출력단 정규식 마스킹 및 차분 프라이버시 |
| LLM03 | Supply Chain | 악성 가중치(Pickle RCE) 및 오염된 라이브러리 도입 / AIBOM 검증, Safetensors 전환 |
| LLM04 | Data and Model Poisoning | 파인튜닝/RAG 데이터 오염으로 백도어 주입 / 데이터 출처 검증 및 이상치 필터링 |
| LLM05 | Improper Output Handling | 모델 출력이 검증 없이 SQL/셸 명령어로 직결 / 엄격한 스키마 검증 및 출력 인코딩 |
| LLM06 | Excessive Agency | 에이전트에 과도한 쓰기/삭제 권한 부여 / 독립 PEP 인터셉터 및 고위험 HITL 승인 |
| LLM07 | System Prompt Leakage | 비즈니스 로직이 담긴 시스템 프롬프트 탈취 / 메타 프롬프트 보호 및 프롬프트 난독화 |
| LLM08 | Vector and Embedding Weaknesses | 벡터 DB 오염 및 임베딩 역추출 공격 / 벡터 저장소 RBAC 접근통제 및 서명 검증 |
| LLM09 | Misinformation | 환각(Hallucination)에 의한 오정보 생성 / 사실 검증(Fact-Checking) 모델 및 출처 명시 |
| LLM10 | Unbounded Consumption | 과도한 토큰 소비를 유발하는 DoS 공격 / 사용자별 토큰 쿼터제 및 Rate Limiting |

## Ⅳ. OWASP LLM 2023 버전 대비 2025 버전 주요 변경사항 비교

| 구분 | OWASP LLM Top 10 (2023) | OWASP LLM Top 10 (2025) | 변경 사유 및 의미 |
|---|---|---|---|
| LLM07 | Insecure Plugin Design | System Prompt Leakage | 플러그인 위험을 LLM06으로 통합하고, 프롬프트 지식재산 탈취 위험을 독립 항목 승격 |
| LLM08 | Insecure Output Handling (구 LLM02) | Vector and Embedding Weaknesses | RAG 아키텍처 확산에 따른 벡터 DB 및 임베딩 오염 위협을 신규 최우선 항목 반영 |
| LLM09 | Overreliance (과도한 의존) | Misinformation (오정보) | 사용자 심리적 의존에서 벗어나 모델 자체의 허위 정보 생성 및 환각 피해에 집중 |
| LLM10 | Model Theft (모델 도난) | Unbounded Consumption | 모델 추출보다 클라우드 API 자원 고갈 및 DoS 과금 공격이 실질적 운영 위험으로 대두 |

## Ⅴ. LLM 애플리케이션 보안의 한계와 방안

| 한계 | 방안 |
|---|---|
| 자연어의 본질적 유연성으로 인해 우회 탈옥(DAN, Base64 난독화) 프롬프트 인젝션(LLM01)을 100% 탐지 차단 불가능 | 입력 프롬프트 분석 전용 소형 모델(Llama Guard) 배치와 출력단 인코딩 및 실행 권한 최소화(Least Privilege) 심층 방어 결합 |
| RAG 검색 파이프라인에서 신뢰되지 않은 외부 웹 문서가 벡터 DB에 적재되어 간접 인젝션(LLM08) 유발 | 문서 임베딩 전 파싱 정제 파이프라인 구축 및 벡터 검색 결과에 대한 테넌트 격리 및 사용자 권한(RBAC) 필터링 강제 |
| 에이전틱 도구(Function Calling) 호출 시 과도한 자율성(LLM06)으로 인한 비인가 DB 삭제 및 금융 거래 위험 | 모델과 백엔드 시스템 사이에 독립적인 정책 집행 지점(PEP)을 두고 비가역적 쓰기/삭제 작업에 대해 HITL(인간 승인) 강제 |

## Ⅵ. 제언

```text
[ 단순 프롬프트 엔지니어링 ]           [ OWASP 2025 기반 제로 트러스트 AI ]
모델 내부 지시에 의존 ──┐             ┌── 듀얼 가드레일 (입력/출력) 실시간 검증
권한 분리 없는 실행 ──┼─→ [ 침해 취약 ] ─┼── RAG 벡터 DB 접근 제어 및 서명
사후 대응 불가능 ──────┘             └── 마이크로 샌드박스 격리 및 HITL 게이트
```

| 평가 영역 | 초기 LLM 배포 체계 | OWASP 2025 준수 체계 | 향후 발전 방향 |
|---|---|---|---|
| 프롬프트 방어 | 정적 키워드 필터링 | 의미론적 가드레일 방어 | 강화학습 기반 능동적 레드팀(Red Teaming) |
| 실행 안전성 | 시스템 셸 직접 호출 | 샌드박스 및 PEP 인터셉트 | eBPF 기반 에이전트 런타임 행위 격리 |
| 규제 대응력 | 컴플라이언스 공백 | EU AI Act 요구사항 충족 | AI 거버넌스 자동 감사(AIBOM 연동) |

OWASP Top 10 for LLM Applications (2025)는 생성형 AI가 단순 챗봇에서 자율 에이전트와 RAG 기반 업무 시스템으로 진화함에 따라 필수적으로 준수해야 하는 현대 AI 보안의 표준 아키텍처 나침반.

## 출제 이력과 검증 출처

- 정보관리기술사 제136회 4교시 5번 (생성형 AI 보안 위협 및 OWASP LLM 취약점)
- 정보관리기술사 제134회 2교시 (생성형 AI 서비스 보안 가이드라인)
- OWASP GenAI Security Project: Top 10 for LLM Applications (2025 Edition)
- NIST AI Risk Management Framework: Generative AI Profile (NIST AI 600-1)
- KISA 생성형 AI 서비스 보안 가이드라인
