---
title: "LLM(Large Language Model) 보안 위험"
author: "agnusdei1207"
date: "2026-10-24T22:51:45+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "002"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- LLM 보안 위험, LLM(Large Language Model), 생성형 AI(Generative AI), RAG(Retrieval-Augmented Generation)
- 프롬프트 주입(Prompt Injection), 간접 프롬프트 주입(Indirect Prompt Injection), 탈옥(Jailbreak), 데이터 오염(Data Poisoning)
- 과도한 대리 실행(Excessive Agency), 혼동된 대리인(Confused Deputy), HITL(Human-in-the-Loop), 가드레일(Guardrail)
- OWASP Top 10 for LLM, MITRE ATLAS, AI TRiSM, AI 레드팀(AI Red Teaming), 심층 방어(Defense-in-Depth)

## Ⅰ. LLM(Large Language Model) 보안 위험의 개요

- 핵심 요약 : 학습부터 추론, 에이전트 도구 실행까지 이어지는 전 주기에서 생기는 적대적 입력과 비결정적 출력이 만드는 새로운 공격 표면.
- 개념 : **LLM 보안 위험** (대규모 언어 모델과 **생성형 AI** (Generative AI, 입력에 따라 텍스트·코드 등을 만들어 내는 AI) 애플리케이션의 학습·파인튜닝·추론·도구 실행 전 주기에서 발생하는 적대적 공격, 데이터 침해, 모델 탈취, 비결정적 이상 출력의 총칭).
- 배경 및 필요성 : 기업 서비스에 **RAG** (Retrieval-Augmented Generation, 외부 문서를 검색해 답변 근거로 덧붙이는 기법)와 자율 에이전트 도입이 늘면서, 방화벽·WAF(Web Application Firewall)·정적 분석 같은 전통적 통제로는 막기 어려운 새 **공격 표면** (Attack Surface)이 생김.
- 주요 목적 : OWASP(Open Worldwide Application Security Project)의 **OWASP Top 10 for LLM**과 AI 시스템 대상 적대적 위협 지식 체계인 **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems)를 기준으로 취약점을 식별하고, 비신뢰 입력을 격리하며, 민감 정보 유출을 막는 것.

## Ⅱ. LLM(Large Language Model) 보안 위험의 특징 및 장점

- 핵심 요약 : 자연어 명령과 데이터가 같은 입력 채널을 타고 들어오므로, 공격자가 모델의 지침을 우회해 연결된 백엔드를 대신 움직이는 구조.

1. 입력 채널 혼재 : 지시문과 데이터가 같은 텍스트 스트림으로 들어옴 → **프롬프트 주입** (Prompt Injection, 입력문 속 숨은 지침으로 시스템 지침을 덮어쓰는 공격) 한 번으로 안전 지침이 무력화.
2. 확률론적 출력 : 같은 입력에도 출력이 달라져 결정론적 검증이 어려움 → 정규식 기반 차단 규칙이 우회되기 쉬움.
3. 도구 실행 권한 결합 : 에이전트가 API·DB·셸에 연결되면 모델 출력이 곧 실행 명령이 됨 → 권한을 가진 대리자가 공격자의 요청을 대신 수행하는 **혼동된 대리인** (Confused Deputy) 문제 발생.
4. 학습 데이터 신뢰 : 사전 학습이나 파인튜닝 데이터에 백도어 트리거를 심는 **데이터 오염** (Data Poisoning) → 특정 입력에서만 악성 출력이 나타나 탐지가 어려움.

## Ⅲ. LLM(Large Language Model) 보안 위험의 구조 (흐름)

- 핵심 요약 : 위험은 입력 주입, 학습 오염, 정보 노출, 과도한 권한의 네 축이며, 프롬프트 입력에서 시작해 백엔드 인프라까지 전이되는 흐름.
- 직접·간접 프롬프트 주입과 **탈옥** (Jailbreak, 모델의 안전 정렬을 우회해 금지된 출력을 유도하는 기법)으로 시스템 프롬프트와 내부 설정이 노출될 수 있음.
- 민감 정보 노출 (Sensitive Information Disclosure) : 가중치에 암기된 개인정보·API 키·기업 기밀이 적대적 질의로 유출될 수 있음.
- 과도한 대리 실행 (Excessive Agency) : 에이전트에 파일 삭제·메일 발송·DB 변경 권한이 넓게 주어져 비인가 파괴 행위가 발생.

```text
[ LLM 공격 전이 경로 ]

외부 공격자 (직접·간접 입력)
   ↓ 1. 프롬프트 주입
LLM 애플리케이션 (RAG·에이전트)
   ↓ 2. 지침 우회·악성 출력
도구 호출 (API·DB·셸)
   ↓ 3. 권한 오용
백엔드 인프라 (유출·원격 실행)
```

```text
[ 신뢰 경계 ]

신뢰 영역 : 시스템 프롬프트, 서버 정책
────────────────────────────────
비신뢰 영역 : 사용자 입력, RAG 문서,
              플러그인 응답
```

## Ⅳ. LLM(Large Language Model) 보안 위험과 전통 웹 보안의 비교

- 핵심 요약 : 전통 웹 보안은 결정론적 파싱을 방어하고, LLM 보안은 확률론적 생성과 자연어 신뢰 경계를 방어하는 차이.

| 비교 항목 | 전통 웹 보안 위협 (OWASP Web) | LLM 보안 위협 | 대응 엔지니어링 기술 |
| --- | --- | --- | --- |
| 공격 입력 형식 | SQL 구문, 스크립트 코드 (XSS, SQLi) | 비정형 자연어 프롬프트, 인코딩 텍스트 | 의미 기반 가드레일 (NeMo Guardrails, Llama Guard) |
| 실행 결정성 | 결정론적 파싱과 실행 | 확률론적 토큰 생성과 추론 | 입출력 이중 필터링, 프롬프트 격리 |
| 핵심 침해 지점 | 입력값 검증 미비로 인한 인터프리터 오작동 | 자연어 명령과 데이터의 신뢰 경계 모호성 | 데이터·컨텍스트 태깅, 마이크로 샌드박스 |
| 신뢰 경계 | 클라이언트(비신뢰)와 서버(신뢰) | 프롬프트, RAG 검색 문서, 플러그인 모두 잠재 위협 | 도구 실행 시 사람 승인 (HITL) |
| 영향도 | 데이터 탈취, 세션 하이재킹 | 자율 에이전트 오작동, 인프라 명령 오용 | 최소 권한 실행 환경, Wasm 샌드박싱 |

- LLM 보안은 결정론적 구문 분석기 대신 확률론적 토큰 생성기를 공격 대상으로 삼으므로, 자연어와 시스템 제어 명령을 엄격히 분리하는 설계가 필수.

## Ⅴ. LLM(Large Language Model) 보안 위험의 한계와 방안

- 핵심 요약 : 자연어 경계를 완전히 나눌 수 없으므로, 입력 구조화와 간접 주입 차단, 권한 승인 체계를 겹쳐 두는 심층 방어로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 자연어와 시스템 명령의 물리적 분리 불가 | 제어 흐름과 데이터 흐름이 한 텍스트 스트림에 섞여 블랙리스트 정규식이 무력화 | XML(Extensible Markup Language)·JSON(JavaScript Object Notation) 태깅 강제, 경량 보안 분류 모델(Guardrail LLM)을 앞단에 배치한 **심층 방어** (Defense-in-Depth) | 우회 시도 탐지율, 차단 오탐률 |
| **간접 프롬프트 주입** (Indirect Prompt Injection) | RAG로 유입된 웹 문서·PDF·메일 속 은닉 지침이 컨텍스트에 들어가 모델을 오염 | 인덱싱 단계에서 OCR(Optical Character Recognition) 결과를 포함한 악성 지침 검사, 문서 컨텍스트를 비실행 읽기 전용 블록으로 분리 | 악성 지침 탐지 건수, 격리 문서 비율 |
| **혼동된 대리인** (Confused Deputy) | 셸·클라우드 API·DDL(Data Definition Language) 권한을 가진 에이전트가 공격자의 요청을 대신 실행 | HITL(Human-in-the-Loop) 다단계 승인, 임시 권한(Just-In-Time)으로 실행 범위 최소화 | 승인 대기 건수, 상시 권한 부여 비율 |

## Ⅵ. LLM(Large Language Model) 보안 위험에 대한 기술사적 제언

- 핵심 요약 : 모델이 확률론적으로 동작한다는 전제 아래, AI 전용 위험 관리 체계와 실행 격리를 상시 운영하는 방향.

1. 조직은 개발부터 서빙, 에이전트 실행까지 **AI TRiSM** (AI Trust, Risk and Security Management, 신뢰·위험·보안 관리 프레임워크)을 적용해 모델 무결성과 이상 행위를 상시 감시하는 것이 필요.
2. 보안 조직은 **AI 레드팀** (AI Red Teaming, 공격자 관점에서 모델을 시험하는 활동)을 정례화하고, JailbreakBench 같은 탈옥 기법 자료를 주기적으로 수집해 가드레일 정책을 갱신하는 것이 필요.
3. 모델이 호출하는 외부 도구와 코드 실행기는 Wasm(WebAssembly) 또는 컨테이너 샌드박스 안에서만 구동되도록 강제하여, 침해가 메모리와 파일시스템으로 번지지 않게 하는 것이 필요.

## Ⅶ. 결론

- 핵심 요약 : LLM 보안은 자연어 입력을 신뢰할 수 없는 데이터로 간주하고 권한과 실행을 격리하는 설계 문제.
- 시사점 : 모델 성능 개선만으로는 해결되지 않으므로, 권한 최소화와 사람 승인 체계가 기본 통제로 자리 잡아야 함.
