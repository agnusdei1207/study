---
title: "OWASP Top 10 for LLM Applications"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. OWASP Top 10 for LLM Applications의 개요

- 개념 : **오픈소스 웹 애플리케이션 보안 프로젝트** (OWASP)가 **대규모 언어 모델** (LLM) 및 생성형 AI 애플리케이션의 개발, 배포, 운영 과정에서 가장 빈번하게 발생하고 영향도가 치명적인 10대 핵심 보안 취약점을 체계화한 글로벌 표준 가이드라인.
- 배경 및 필요성 : 전통적인 웹 취약점(SQLi, XSS) 중심의 OWASP Top 10으로는 자연어를 입력받고 비결정론적으로 동작하는 생성형 AI 애플리케이션의 신종 위험을 방어할 수 없다는 요구에 따라 2023년 최초 제정 및 2025년 개정.
- 핵심 목적 : LLM 아키텍처 상의 고유 보안 약점 가시화, 개발자 및 보안 아키텍트를 위한 실질적 완화 조치 제공, AI 서비스 보안 감사 표준 기준 확립.

## Ⅱ. OWASP Top 10 for LLM Applications의 핵심 아키텍처 및 동작 메커니즘

OWASP Top 10 for LLM은 프롬프트 주입(LLM01)부터 취약한 출력 처리, 공급망 침해, 서비스 거부(DoS)에 이르는 10가지 위협 벡터를 정의함.

```text
[ OWASP Top 10 for LLM 핵심 취약점 분류 및 매핑 ]

  +-------------------------------------------------------------+
  |            사용자 입력 계층 (Input Layer)                   |
  |  ★ LLM01: Prompt Injection (직접/간접 프롬프트 주입, 탈옥)  |
  +------------------------------┬------------------------------+
                                 │
         ┌───────────────────────┴───────────────────────┐
         ▼                                               ▼
  [ 모델 및 파이프라인 계층 ]                     [ 데이터 및 공급망 계층 ]
  - LLM10: Unbounded Consumption (자원 고갈, DoS)   - LLM03: Supply Chain
  - LLM09: Misinformation (환각 맹신)             - LLM04: Data and Model Poisoning
         │                                               │
         └───────────────────────┬───────────────────────┘
                                 │
                                 ▼
  +-------------------------------------------------------------+
  |            모델 출력 및 도구 실행 계층 (Output & Tools)      |
  |  - LLM02: Sensitive Info Disclosure (민감 데이터 유출)      |
  |  - LLM05: Improper Output Handling (출력 무검증 처리)       |
  |  - LLM06: Excessive Agency (과도한 권한 대리 실행)          |
  |  - LLM07: System Prompt Leakage (시스템 프롬프트 노출)       |
  |  - LLM08: Vector and Embedding Weaknesses (RAG 임베딩 오염) |
  +-------------------------------------------------------------+
```

- **LLM01: Prompt Injection** : 직접/간접 프롬프트 조작을 통해 모델의 안전 지침을 우회하고 의도치 않은 악성 행위를 유도하는 최우선 위협.
- **LLM02: Sensitive Information Disclosure** : 독점 알고리즘, 개인정보, API 키가 모델 응답을 통해 비인가자에게 무단 유출.
- **LLM03: Supply Chain Vulnerabilities** : 비신뢰 사전학습 모델, 취약한 파이썬 라이브러리(LangChain 등)를 통한 백도어 감염.
- **LLM04: Data and Model Poisoning** : 학습 데이터셋이나 RAG 검색 풀을 오염시켜 모델의 예측 왜곡 및 특정 백도어 유발.
- **LLM05: Improper Output Handling** : 모델 출력을 검증 없이 웹 브라우저나 DB 백엔드로 넘겨 발생하는 XSS 또는 **원격 코드 실행** (RCE).
- **LLM06: Excessive Agency** : 에이전트에게 지나치게 넓은 권한(파일 삭제, 메일 전송 등)이 부여되어 프롬프트 조작 시 파괴적 실행.

## Ⅲ. OWASP Top 10 for LLM Applications의 세부 구성 요소 및 비교 분석

| 순위 | 취약점 명칭 (2025 기준) | 위협 내용 | 엔지니어링 대응책 |
| --- | --- | --- | --- |
| LLM01 | Prompt Injection | 자연어 명령 주입으로 모델 제어권 탈취 | 입력 샌드박싱, 의미론적 가드레일 (NeMo) |
| LLM02 | Sensitive Info Disclosure | 학습 데이터 내 개인정보/기밀 응답 노출 | 데이터 전처리 가명화, 출력 PII 마스킹 |
| LLM03 | Supply Chain | 취약한 모델 가중치 및 오픈소스 종속성 | 모델 해시 서명 검증, AIBOM(CycloneDX) 관리 |
| LLM04 | Data & Model Poisoning | 학습/RAG 데이터 오염을 통한 백도어 주입 | 데이터셋 출처 검증, 이상 임베딩 탐지 |
| LLM05 | Improper Output Handling | 모델 출력을 신뢰하여 백엔드 해석 시 결함 | 출력값 HTML 인코딩, 파라미터화 쿼리 강제 |
| LLM06 | Excessive Agency | 에이전트의 과도한 자율성 및 고권한 남용 | 최소 권한 원칙, 인간 승인(HITL) 체계 |

- OWASP Top 10 for LLM은 웹 보안의 기술적 접근법과 달리, 확률론적 생성 모델이 갖는 비결정론적 특성과 자율 에이전트의 권한 위임 문제를 집중적으로 조명함.

## Ⅳ. OWASP Top 10 for LLM Applications의 주요 한계점 및 해결 방안

- 기존 **웹 방화벽** (WAF) 장비의 LLM 자연어 공격 페이로드 미탐 :
  - 한계점 : 전통적 WAF는 SQL 특수문자나 스크립트 태그만 검사하므로, 자연어 문장으로 정교하게 작성된 프롬프트 인젝션 탐지 불가.
  - 해결 방안 : LLM 전용 **AI 방화벽** (AI Gateway)을 도입하여 임베딩 기반 유사도 및 분류 전용 소형 모델을 통한 인라인 의미론적 검사 수행.
- 모델 출력 처리 미흡으로 인한 2차 XSS 및 시스템 콜 실행 :
  - 한계점 : LLM이 생성한 마크다운이나 자바스크립트 코드를 웹 프론트엔드에서 `innerHTML`이나 `eval()`로 무검증 렌더링하다가 클라이언트 장악.
  - 해결 방안 : LLM 출력을 비신뢰 사용자 입력과 동일하게 취급하여 엄격한 컨텍스트별 이스케이프(DOMPurify) 적용 및 CSP 정책 강제.
- RAG 파이프라인의 **벡터 임베딩 조작** (Vector Embedding Weakness) :
  - 한계점 : 공격자가 벡터 공간에서 특정 질문과 가장 유사하게 매핑되도록 최적화된 적대적 문서를 RAG DB에 주입하여 오답 생성 유도.
  - 해결 방안 : 문서 인덱싱 시 출처(Provenance) 기반 암호학적 서명 검증 및 검색된 문서 청크의 신뢰 점수(Relevance Threshold) 필터링.

## Ⅴ. OWASP Top 10 for LLM Applications 적용 및 발전을 위한 기술사적 제언

- 사내 LLM 애플리케이션 보안 체크리스트 의무화 : 신규 생성형 AI 서비스 출시 전 OWASP LLM Top 10 기준 전수 진단 및 보안성 검토 회의 통과 의무화.
- **AI 레드팀 모의침투 프레임워크** (Garak, PyRIT) 연동 : 배포 전 자동화된 취약점 스캐너를 구동하여 10대 취약점 악용 가능성을 사전에 계측.
- 플러그인 및 도구 호출의 **최소 권한 인가** 설계 : 에이전트가 호출하는 도구 API에 대해 시한부 세션 토큰과 엄격한 화이트리스트 파라미터 제약 부여.
