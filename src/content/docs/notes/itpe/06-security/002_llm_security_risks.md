---
title: "LLM(Large Language Model) 보안 위험"
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

## Ⅰ. LLM(Large Language Model) 보안 위험의 개요

- 개념 : **대규모 언어 모델** (LLM, Large Language Model) 및 **생성형 AI**(Artificial Intelligence) 애플리케이션의 학습, 파인튜닝, 추론, 에이전트 도구 실행 전주기에서 발생하는 적대적 공격, 데이터 침해, 모델 탈취, 비결정론적 이상 출력으로 인한 총체적 보안 위협.
- 배경 및 필요성 : 기업 및 서비스 전반에 LLM 기반 **RAG** (Retrieval-Augmented Generation, 검색 증강 생성) 및 자율 에이전트 도입이 급증하면서 전통적인 소프트웨어 보안 통제(방화벽, WAF(Web Application Firewall), 정적 분석)로는 방어가 불가능한 새로운 **공격 표면** (Attack Surface) 발생.
- 핵심 목적 : **OWASP(Open Worldwide Application Security Project) Top 10 for LLM** 및 **MITRE ATLAS** 프레임워크 기반 취약점 식별, 비신뢰 입력 격리, 민감 정보 유출 방지 및 안전한 에이전트 실행 환경 구축.

## Ⅱ. LLM(Large Language Model) 보안 위험의 핵심 아키텍처 및 동작 메커니즘

LLM 보안 위험은 공격자가 비신뢰 프롬프트를 주입하거나 학습 데이터를 오염시켜 모델의 안전 지침(System Prompt)을 무력화하고, 연결된 백엔드 API(Application Programming Interface) 및 시스템 명령을 부당하게 호출하는 혼동된 대리인(Confused Deputy) 공격으로 구체화됨.

```text
[ LLM 공격 경로 및 위험 전이 메커니즘 ]

   [ 공격자 (비인가 사용자 / 악성 데이터 게시자) ]
                     │
         ┌───────────┴────────────────────────┐
         │ 1. 직접/간접 프롬프트 주입           │ 2. 데이터 오염 (Poisoning)
         ▼                                    ▼
   +-------------------------------------------------------------+
   |              LLM 애플리케이션 프레임워크 (RAG / Agent)       |
   |  - System Prompt 탈취 / 탈옥(Jailbreak) 발생                |
   |  - 모델 내부 정렬(Alignment) 우회 및 악성 명령 생성         |
   +------------------------------┬------------------------------+
                                  │
                                  ▼ 3. 도구 실행 권한 오용
   +-------------------------------------------------------------+
   | 백엔드 인프라 / API / 데이터베이스 (Confused Deputy 침해)   |
   |  - 내부 DB 비인가 쿼리 실행 / 원격 코드 실행(RCE) / 토큰 유출|
   +-------------------------------------------------------------+
```

- **프롬프트 주입 및 탈옥** (Prompt Injection & Jailbreak) : 입력 텍스트 내에 숨겨진 악성 메타 명령어로 모델의 안전 지침을 우회하고 시스템 프롬프트나 내부 파라미터 탈취.
- **훈련 데이터 오염** (Data Poisoning) : 사전 학습 또는 파인튜닝 데이터셋에 백도어 트리거를 심어 특정 키워드 입력 시 오동작이나 악성 페이로드 출력을 유발.
- **민감 정보 노출** (Sensitive Information Disclosure) : 모델 가중치 내에 암기된 개인정보, API 키, 기업 기밀이 적대적 프롬프트(Model Inversion)를 통해 유출.
- **과도한 대리 실행** (Excessive Agency) : LLM 에이전트에게 파일 삭제, 이메일 발송, DB(Database) 변경 등 광범위한 시스템 권한이 부여되어 비인가 파괴 행위 발생.

## Ⅲ. LLM(Large Language Model) 보안 위험의 세부 구성 요소 및 비교 분석

| 비교 항목 | 전통적 웹 보안 위협 (OWASP Web) | LLM 보안 위협 (OWASP LLM) | 대응 엔지니어링 기술 |
| --- | --- | --- | --- |
| 공격 입력 형식 | 정형화된 SQL(Structured Query Language)문, 스크립트 코드 (XSS(Cross-Site Scripting), SQLi(SQL Injection)) | 비정형 자연어 프롬프트, 인코딩 텍스트 | 의미론적 가드레일 (NeMo, Llama Guard) |
| 실행 환경 결정성 | 결정론적 (Deterministic) 파싱 및 실행 | 확률론적 (Stochastic) 토큰 생성 및 추론 | 입출력 듀얼 필터링, 프롬프트 격리 |
| 핵심 침해 지점 | 입력값 검증 미비로 인한 인터프리터 오작동 | 자연어 명령과 데이터의 신뢰 경계 모호성 | 데이터-컨텍스트 태깅(XML(Extensible Markup Language) 래핑), 마이크로 샌드박스 |
| 신뢰 경계 | 클라이언트(Untrusted) vs 서버(Trusted) | 프롬프트, RAG 검색문서, 플러그인 모두 잠재 위협 | 제로트러스트 기반 도구 실행 승인 (HITL, Human in the Loop) |
| 영향도 | 데이터 탈취, 웹 세션 하이재킹 | 자율 에이전트 폭주, 전사 인프라 명령 오용 | 최소 권한 실행 환경, Wasm 샌드박싱 |

- LLM 보안 위협은 전통적인 결정론적 구문 분석기(Parser) 대신 확률론적 토큰 생성기를 공격 대상으로 삼으므로, 자연어와 시스템 제어 명령의 엄격한 분리 설계가 필수적임.

## Ⅳ. LLM(Large Language Model) 보안 위험의 주요 한계점 및 해결 방안

- 자연어와 시스템 명령어의 물리적 분리 불가로 인한 완전 방어의 이론적 한계 :
  - 한계점 : 자연어 기반 프롬프트 환경에서는 제어 명령(Control Flow)과 데이터(Data Flow)가 동일한 텍스트 스트림에 혼재되어 있어 블랙리스트 기반 정규식 필터링 무력화.
  - 해결 방안 : 입력 데이터에 대해 구조화된 XML/JSON(JavaScript Object Notation) 태깅을 강제하고, **경량 보안 분류 모델** (Guardrail LLM)을 전면에 배치하여 2단계 **심층 방어** (Defense-in-Depth) 구축.
- RAG(검색 증강 생성) 파이프라인을 통한 **간접 프롬프트 주입** (Indirect Prompt Injection) :
  - 한계점 : 외부 비신뢰 웹 문서, PDF(Portable Document Format), 이메일 본문에 은닉된 악성 프롬프트가 RAG 검색을 통해 컨텍스트 윈도우로 유입되어 모델을 오염시키는 취약점 노출.
  - 해결 방안 : RAG 벡터 DB 인덱싱 단계에서 광학문자인식(OCR, Optical Character Recognition) 검증 및 악성 지침 시그니처 검사를 수행하고, 문서 컨텍스트를 비실행 읽기 전용 블록으로 엄격 분리.
- 에이전트 도구(Tool) 호출 시 과도한 자율성으로 인한 **혼동된 대리인** (Confused Deputy) 리스크 :
  - 한계점 : LLM이 OS(Operating System) 커널 셸 명령, 클라우드 API, DB DDL(Data Definition Language) 쿼리 권한을 보유한 경우 공격자의 교묘한 요청에 의해 파괴적인 시스템 명령을 대리 실행.
  - 해결 방안 : 도구 실행 시 **Human-in-the-Loop** (HITL) 다단계 관리자 승인 체계를 필수화하고, 실행 권한을 최소화된 **임시 토큰** (Just-In-Time)으로 제한.

## Ⅴ. LLM(Large Language Model) 보안 위험 적용 및 발전을 위한 기술사적 제언

- **AI TRiSM** (신뢰·위험·보안 관리) 프레임워크 전면 적용 : 모델 개발부터 서빙, 에이전트 실행까지 모니터링, 데이터 무결성 검증, 이상 탐지 거버넌스를 내재화해야 함.
- **레드팀** (AI Red Teaming) 자동화 및 적대적 모의 공격 정례화 : 새로운 탈옥 프롬프트 기법(JailbreakBench 등)을 지속 수집하여 가드레일 정책을 동적으로 갱신해야 함.
- Wasm/컨테이너 기반 마이크로 샌드박싱 환경 강제 : 모델이 호출하는 모든 외부 도구 및 코드 실행기를 완벽히 격리된 메모리/파일시스템 샌드박스 내에서만 구동하도록 격리해야 함.
