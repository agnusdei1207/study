---
title: "Text2SQL"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 자연어 기반 데이터 질의의 혁신, Text2SQL 개요

### 가. Text2SQL의 정의
- **Text2SQL** : 사용자가 일상적인 **자연어** (Natural Language)로 입력한 비즈니스 질문을 데이터베이스가 이해하고 실행할 수 있는 정형화된 **SQL** (Structured Query Language) 쿼리로 자동 변환하는 인공지능 기술.
- 복잡한 SQL 문법과 데이터베이스 스키마 구조를 모르는 비전문가도 데이터에 직접 접근하여 분석할 수 있도록 지원하는 **데이터 민주화** (Data Democratization)의 핵심 엔진.

---

## Ⅱ. Text2SQL 시스템의 핵심 아키텍처 및 파이프라인

### 가. 엔드투엔드 Text2SQL 변환 흐름

```text
[ Text2SQL 파이프라인 아키텍처 ]
[사용자 자연어 질문] ---> [스키마 링킹 (Schema Linking)]
                                  | (관련 테이블/컬럼/외래키 추출)
                                  v
                        [프롬프트 구성 (Prompt Builder)]
                        - DDL 스키마 + Few-Shot 예시 + 도메인 규칙
                                  |
                                  v
                        [거대언어모델 (LLM Inference)]
                                  |
                                  v (SQL 생성)
                        [SQL 검증 및 자가 교정 (Self-Correction)]
                        - SQL 구문 검사(Parser) -> Dry-Run 실행
                                  |
                                  v (정상 검증 완료)
                        [DBMS 실행 및 결과 시각화 반환]
```

### 나. 핵심 기술 요소별 메커니즘

| 구성 요소 | 기술적 메커니즘 | 해결하는 과제 |
| :--- | :--- | :--- |
| **스키마 링킹 (Schema Linking)** | 자연어 질의 속 단어들을 DB 카탈로그의 실제 테이블명, 컬럼명, 코드값과 의미론적으로 매핑 | "지난달 VIP 매출" $\rightarrow$ `ORDERS.TOTAL_PRICE`, `CUST.GRADE='VIP'` 매핑 |
| **Few-Shot RAG** | 질의와 가장 유사한 과거 (자연어 질문, 정답 SQL) 쌍을 벡터 검색하여 프롬프트 컨텍스트에 주입 | 고난도 복합 조인 및 사내 특수 비즈니스 계산 로직 가이드 |
| **구문 검증 및 파싱** | `sqlglot`, ANTLR 등 SQL 파서를 통해 생성된 SQL의 문법적 오류 및 예약어 충돌 사전 차단 | 컴파일 에러 없는 완전한 SQL 문장 보장 |
| **자가 교정 (Self-Correction)** | DBMS에 `EXPLAIN`을 돌려 런타임 에러(컬럼 부재, 타입 불일치) 발생 시 에러 메시지를 LLM에 재주입하여 자동 수정 | 1회성 실패를 모델 스스로 재시도하여 성공률(Execution Accuracy) 극대화 |

---

## Ⅲ. Text2SQL 상용화의 한계점·문제점 및 해결 방안

### 가. 방대한 DB 스키마와 컨텍스트 창(Context Window) 한계
- 전사 수천 개 테이블 스키마를 프롬프트에 모두 담을 수 없음 $\rightarrow$ **도메인별 스키마 서브셋 검색** (Schema Pruning)을 통해 질문과 관련된 상위 5~10개 테이블 DDL만 동적 추출.

### 나. 데이터 보안 및 쿼리 파괴 리스크
- 자연어 입력을 통한 악의적 DDL(`DROP TABLE`), CUD 연산 또는 **SQL Injection** 위험.
- 해법 : Text2SQL 전용 DB 계정에 대해 엄격한 읽기 전용(`SELECT` Only) 권한만 부여 하고, 생성된 SQL의 **AST** (추상구문트리)를 검사하여 DDL/DML 키워드를 원천 차단.

---

## Ⅳ. 엔터프라이즈 Text2SQL 구축을 위한 실무 제언

- **시맨틱 데이터 레이어** (Semantic Layer)의 선행 구축 : LLM이 DB의 축약된 영문 컬럼명(`CUST_TP_CD`, `SL_AM`)을 오인하지 않도록, dbt 시맨틱 레이어 또는 Cube.js 등을 도입하여 각 컬럼의 한글 비즈니스 명칭, 계산 공식, 동의어 사전을 메타데이터로 사전 표준화해야 함.
- 비용 폭탄 방지를 위한 실행 **자원 상한선** (Guardrail) 설정 : 잘못 생성된 SQL이 수억 건 테이블의 카테시안 곱(Cartesian Product)을 유발하여 DB CPU를 고갈시키는 사태를 방지하기 위해, 모든 생성 쿼리에 `LIMIT 1000`을 강제 주입하고 쿼리 실행 타임아웃을 5초 이내로 엄격히 제한할 것을 제언함.
