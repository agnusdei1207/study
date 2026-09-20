---
sidebar:
  order: 98
  label: "098. 정적 SQL vs 동적 SQL"
  badge:
    text: "B"
    variant: note
title: "정적 SQL(Static SQL)과 동적 SQL(Dynamic SQL)의 비교 및 실행 메커니즘"
author: "OpenAI Codex"
date: "2026-09-20T18:40:00+09:00"
tags:
  - "notes-data"
weight: 98
extra:
  model: "GPT-5"
  keyword_grade: "B"
  question_no: "098"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>SQL·데이터베이스 개발</span><strong>정적 SQL vs 동적 SQL</strong></div>

## 큰 그림과 30초 인출

```text
[정적 SQL과 동적 SQL의 라이프사이클 및 라이브러리 캐시 동작 비교]

 [1. 정적 SQL (Static SQL): 컴파일 시점 구문 확정 및 캐시 재사용]
  [소스 작성] ──► [Pre-compiler] ──► [바인드 변수] ──► [Library Cache 히트] ──► [즉시 실행]
   EXEC SQL       문법/권한 사전검증    PreparedStatement   (Soft Parsing 달성)       (초저지연)
   SELECT ...

 [2. 동적 SQL (Dynamic SQL): 런타임 문자열 조합 및 파싱 분기]
  [사용자 입력] ──► [런타임 조립] ──► [파라미터 전달 방식에 따른 분기]
   카테고리/가격     QueryDSL/MyBatis   │
                                        ├─► [바인드 변수 (?)]: Soft Parsing 재사용, SQLi 차단
                                        └─► [문자열 결합 (+)]: Hard Parsing 폭증, SQLi 노출
```

- 본질: **개발 및 컴파일 시점에 SQL 구조가 완전히 고정되어 문법 검증과 사전 최적화가 이루어지는 정적 SQL(Static SQL)과, 프로그램 실행 런타임(Runtime)에 사용자의 검색 조건 및 비즈니스 분기에 따라 문자열을 동적으로 조립·생성하는 동적 SQL(Dynamic SQL)의 성능·보안·유연성 간 트레이드오프 관계**
- 암기: `정-컴-소-안` (정적 SQL: 컴파일 시점 확정, 소프트 파싱, 안전한 보안) / `동-런-유-하` (동적 SQL: 런타임 조립, 조건 유연성, 하드 파싱 위험) / `바-인-프` (바인드 변수, 인젝션 방어, PreparedStatement)
- 판단축:
  - **정적 SQL**: 코어 트랜잭션, 계좌 이체, 배치 적재 등 쿼리 패턴이 고정적이고 초당 수만 건의 고성능 OLTP가 요구되는 영역
  - **동적 SQL**: 쇼핑몰 다차원 상세 검색, 백오피스 통계 리포트 등 수십 가지 조건의 조합이 가변적인 영역
- 주의: 동적 SQL 작성 시 문자열 단순 결합(`String +`) 방식을 사용할 경우 매번 다른 해시값이 생성되어 **하드 파싱(Hard Parsing)으로 인한 DBMS CPU 고갈**과 **치명적인 SQL Injection 공격**에 직면하므로 반드시 PreparedStatement 바인드 변수를 결합해야 함

## 예상문제

> 데이터베이스 응용 개발에서 사용되는 정적 SQL(Static SQL)과 동적 SQL(Dynamic SQL)의 개념과 실행 메커니즘을 비교하고, 동적 SQL의 성능 저하 원인인 하드 파싱(Hard Parsing)의 문제점 및 SQL Injection 보안 취약점 극복 방안을 설명하시오. (25점)

## Ⅰ. SQL 실행 방식의 양대 축: 정적 SQL vs 동적 SQL 개요

#### 한줄 요약: 컴파일 시점에 구조가 확정되는 고성능 정적 쿼리와 런타임에 유연하게 조합되는 가변형 동적 쿼리의 공학적 대조

- **배경**: 복합 검색 필터가 존재하는 현대 웹 애플리케이션에서 모든 조건별 정적 SQL을 개별 작성하면 코드 중복과 유지보수 비용이 폭증하는 반면, 무분별한 동적 SQL 남발은 DB 서버의 과부하와 보안 사고를 유발함
- **정의**:
  - **정적 SQL (Static SQL)**: 프로그램 작성 시점에 쿼리 문맥이 완성되어 컴파일 단계에서 문법과 권한이 사전 검증되는 SQL
  - **동적 SQL (Dynamic SQL)**: 애플리케이션 실행 도중 런타임 변수나 조건식 분기 로직에 따라 문자열을 조합하여 DBMS로 전송하는 SQL

## Ⅱ. 정적 SQL과 동적 SQL의 5대 핵심 항목 비교

#### 한줄 요약: 개발 생산성과 성능·보안 간의 명확한 상충 관계(Trade-off)

| 비교 항목 | 정적 SQL (Static SQL) | 동적 SQL (Dynamic SQL) |
|:---|:---|:---|
| **문맥 결정 시점** | **컴파일 타임 (Compile-time)** | **런타임 (Run-time)** |
| **파싱 메커니즘** | 사전 컴파일 및 **소프트 파싱(Soft Parsing)** 극대화 | 부적절 구현 시 **하드 파싱(Hard Parsing)** 반복 발생 |
| **SQL Injection 취약성** | **구조적 원천 면역** (쿼리 구조 불변) | 문자열 단순 결합 시 **극도로 취약** (바인드 필수) |
| **조건절 유연성** | 매우 낮음 (고정된 WHERE 조건문만 실행) | 극도로 우수 (다양한 필터 조건 동적 추가/제거) |
| **개발 구현 방식** | Pro*C, Embedded SQL, 고정형 JPA `@Query` | MyBatis `<if>`, QueryDSL `BooleanBuilder`, JDBC |
| **적용 권장 영역** | 초당 트랜잭션이 많은 코어 OLTP, 대량 배치 | 다차원 동적 검색 화면, 조건별 통합 조회 API |

## Ⅲ. 데이터베이스 내부 처리 흐름 및 라이브러리 캐시 메커니즘

#### 한줄 요약: 라이브러리 캐시(Library Cache) 적중 여부가 DBMS 전체 처리 성능을 결정

```text
 [사용자 SQL 요청]
        │
        ▼ [SQL 텍스트 해시값 생성: SHA-1 / MD5]
        │
   ┌────┴───────────────────────────┐
   ▼ (Cache Hit)                    ▼ (Cache Miss)
 [소프트 파싱 (Soft Parsing)]     [하드 파싱 (Hard Parsing)]
 - 문법 검증/최적화 생략          - Syntax Check -> Semantic Check
 - 캐시된 실행 계획 즉시 재사용   - Query Optimizer 비용 산정 -> 플랜 생성
 - CPU 점유율: 0.1% 미만          - 래치(Latch) 경합 발생, CPU 점유율 폭증
```

- **정적 SQL**: 쿼리 텍스트가 대소문자·공백까지 완벽히 일치하여 해시값이 동일하므로 99.9% 소프트 파싱 수행
- **리터럴 동적 SQL (`WHERE id = 'user1'`, `WHERE id = 'user2'`)**: 매번 다른 텍스트로 인식되어 해시값이 변경됨 $\rightarrow$ 매 요청마다 하드 파싱 수행으로 공유 풀(Shared Pool) 메모리 단편화 및 Latch 경합으로 DB 다운 유발

## Ⅳ. 동적 SQL의 양대 보안·성능 위험 및 발생 메커니즘

#### 한줄 요약: 문자열 결합이 초래하는 SQL Injection 침투 경로와 하드 파싱 병목의 구조적 원인

### 1. SQL Injection (보안 위협)
- **취약 코드**: `String sql = "SELECT * FROM TB_USER WHERE ID = '" + inputId + "'";`
- **공격 입력**: `admin' --` 또는 `' OR '1'='1`
- **결과**: `WHERE ID = 'admin' --'`로 변조되어 인증 로직이 무력화되고 전체 개인정보 유출 발생

### 2. 하드 파싱(Hard Parsing) 부하 (성능 위협)
- 동적 SQL에서 파라미터를 리터럴 상수로 인라인 결합하면 옵티마이저가 매번 질의 변환, 접근 경로 탐색, 비용 계산을 반복
- 수천 명의 동시 사용자가 접속 시 `Library Cache Lock` 및 `Library Cache Pin` 대기가 발생하여 시스템 전면 행(Hang) 상태 유발

## Ⅴ. 실무 해결 프레임워크: 안전하고 효율적인 동적 SQL 구축 전략

#### 한줄 요약: PreparedStatement 바인드 변수, ORM 빌더, 그리고 쿼리 분기 설계를 통한 최적화

```text
 [안전한 동적 SQL 아키텍처: QueryDSL / MyBatis]
  사용자 입력 ──► [QueryDSL BooleanExpression] ──► [PreparedStatement (?) 매핑]
                       - 컴파일 타임 문법 검증         - 파라미터 리터럴 분리
                       - 안전한 동적 조건 조립        - Soft Parsing 100% 보장
```

| 해결 방안 | 기술적 메커니즘 | 달성 효과 |
|:---|:---|:---|
| **PreparedStatement / 바인드 변수** | SQL 문장의 구조와 사용자 데이터를 완전히 분리하여 `?` 또는 `:var`로 처리 | 사용자 입력이 쿼리 구조를 바꾸지 못해 **SQL Injection 차단**, 해시값 고정으로 **소프트 파싱 100%** |
| **MyBatis 동적 태그 활용** | `<where>`, `<if test="...">`, `<foreach>` 태그를 사용하여 바인드 변수(`#{...}`) 자동 생성 | 가변 조건 조합의 유지보수 생산성 극대화 및 안전성 확보 |
| **타입 세이프 쿼리 빌더 (QueryDSL)** | Java 코드로 동적 쿼리를 조립하며 `BooleanExpression`을 반환 | 컴파일 타임에 오타 검증 가능, 런타임 쿼리 조립 오류 사전 제거 |

## Ⅵ. 실무 안티패턴과 트러블슈팅

#### 한줄 요약: `NVL` 만능 쿼리 안티패턴과 바인드 피킹(Bind Peeking) 왜곡 대응

| 안티패턴 / 문제 | 발생 원인 | 올바른 실무 해결책 |
|:---|:---|:---|
| **정적 SQL의 무리한 통합 (`NVL` / `LIKE`)** | 조건 분기를 피하려고 `WHERE COL = NVL(:in, COL)`로 작성하여 인덱스 스캔 실패 | 조건 분기별로 동적 SQL을 생성하거나 `UNION ALL`을 통해 쿼리를 명시적으로 분리 |
| **바인드 변수 피킹에 의한 플랜 왜곡** | 데이터가 특정 값에 99% 몰려 있을 때 최초 입력된 드문 값(1%)에 맞춰 인덱스 플랜이 고착 | 편향이 극심한 컬럼은 예외적으로 리터럴 쿼리로 분기하거나 Adaptive Cursor Sharing 적용 |
| **MyBatis `${}` 오용** | 바인드 변수 `#{}` 대신 문자열 치환 연산자인 `${}`를 무분별하게 컬럼/조건에 사용 | 컬럼명이나 정렬 기준(`ORDER BY`) 외에는 무조건 `#{}`를 사용하여 인젝션 원천 방어 |

## Ⅶ. 기술사적 제언: 정적·동적 SQL의 현대적 공존 아키텍처

#### 한줄 요약: 고빈도 코어 트랜잭션의 정적 SQL 최적화와 복합 검색 영역의 타입 세이프 동적 SQL 계층 분리

- **아키텍처 분리 원칙**:
  1. **Core OLTP (쓰기/단건 조회)**: 정적 SQL 및 Spring Data JPA 표준 메서드 적용 $\rightarrow$ 실행 계획 사전 검증, 최소 지연 보장
  2. **Search / Analytics (다차원 조회)**: QueryDSL 기반의 동적 쿼리 계층 구축 $\rightarrow$ 파라미터 바인딩 강제 및 페이징 최적화
  3. **초대용량 로그/검색**: RDBMS의 동적 SQL로 무리하게 풀스캔하지 않고, Elasticsearch/OpenSearch로 읽기 파이프라인을 분리하는 CQRS(명령-조회 책임 분리) 패턴 적용

---

## 1교시 10점 답안 발췌

```text
1. 정적 SQL과 동적 SQL의 정의
  - 정적 SQL: 컴파일 시점에 쿼리 구조가 확정되어 사전 검증 및 소프트 파싱이 보장되는 고정 쿼리.
  - 동적 SQL: 런타임에 사용자 조건에 따라 문자열을 조합하여 생성하는 가변형 쿼리.

2. 양자 간 특성 비교 및 실행 메커니즘
  가. 비교:
    - 결정시점: 컴파일 시점 vs 런타임.
    - 성능/파싱: 소프트 파싱 재사용(우수) vs 하드 파싱 유발 위험(가변 시).
    - 보안: Injection 원천 면역 vs 문자열 결합 시 취약.
  나. 실행 메커니즘:
    - 동일 해시값 유지 여부에 따라 Library Cache 적중(소프트 파싱) 또는 재최적화(하드 파싱) 분기.

3. 동적 SQL 최적화 및 보안 방안
  - PreparedStatement 바인드 변수(#{파라미터}) 사용으로 SQL Injection 차단 및 소프트 파싱 보장.
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제134회 정보관리 1교시: 정적 SQL(Static SQL)과 동적 SQL(Dynamic SQL) 비교
  - 제117회, 제108회 기출
- **검증 출처**:
  - Oracle Database SQL Tuning Guide, "Dynamic SQL and Shared Pool"
  - OWASP Top 10, "A03:2021-Injection"

---

## 학습 체크

- [ ] 정적 SQL과 동적 SQL의 5대 핵심 차이점을 즉시 비교 표로 작성할 수 있는가?
- [ ] 하드 파싱(Hard Parsing)과 소프트 파싱(Soft Parsing)의 라이브러리 캐시 동작 원리를 설명할 수 있는가?
- [ ] 동적 SQL에서 SQL Injection이 발생하는 원리와 바인드 변수를 통한 방어 원리를 서술할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-088 데이터베이스 튜닝](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/088_database_tuning.md)
- 연관 토픽: [03-091 옵티마이저(RBO·CBO)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/091_optimizer.md), [03-094 TEXT2SQL](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/094_text2sql.md)
