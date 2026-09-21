---
sidebar:
  order: 98
  label: "098. 정적 SQL vs 동적 SQL"
  badge:
    text: "A"
    variant: note
title: "정적 SQL(Static SQL)과 동적 SQL(Dynamic SQL)의 비교 및 실행 메커니즘"
author: "Antigravity"
date: "2026-09-20T18:40:00+09:00"
tags:
  - "notes-data"
weight: 98
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
  question_no: "098"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>SQL·데이터베이스 개발</span><strong>정적 SQL vs 동적 SQL</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 230" width="100%" height="auto" role="img" aria-label="정적 SQL과 동적 SQL의 파싱 라이프사이클 비교">
  <defs>
    <marker id="sqlArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
    <marker id="sqlBad" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ef4444"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="230" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Row 1: 정적 SQL -->
  <g transform="translate(20, 20)">
    <rect width="110" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
    <text x="55" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">정적 SQL</text>
    <text x="55" y="38" text-anchor="middle" font-size="8.5" fill="var(--sl-color-gray-2, #64748b)">컴파일 시점 확정</text>

    <path d="M 110 25 L 135 25" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#sqlArr)"/>

    <rect x="140" width="140" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <text x="210" y="22" text-anchor="middle" font-size="10" font-weight="700" fill="var(--sl-color-text, #1e293b)">동일 SQL 해시값</text>
    <text x="210" y="38" text-anchor="middle" font-size="8.5" fill="var(--sl-color-gray-2, #64748b)">바인드 변수 전제</text>

    <path d="M 280 25 L 305 25" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#sqlArr)"/>

    <rect x="310" width="170" height="50" rx="6" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
    <text x="395" y="22" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">소프트 파싱 (100%)</text>
    <text x="395" y="38" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1e293b)">Library Cache 적중 · SQLi 면역</text>
  </g>

  <!-- Row 2: 동적 SQL -->
  <g transform="translate(20, 95)">
    <rect width="110" height="110" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)" stroke-width="1.5"/>
    <text x="55" y="48" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-text, #0f172a)">동적 SQL</text>
    <text x="55" y="65" text-anchor="middle" font-size="8.5" fill="var(--sl-color-gray-2, #64748b)">런타임 문자열 조립</text>
    <text x="55" y="80" text-anchor="middle" font-size="8.5" fill="var(--sl-color-gray-2, #64748b)">다차원 가변 검색</text>

    <!-- Branch Good: 바인드 변수 사용 -->
    <path d="M 110 30 L 135 20" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#sqlArr)"/>
    <rect x="140" y="0" width="160" height="46" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)"/>
    <text x="220" y="18" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">바인드 변수 (?, #{})</text>
    <text x="220" y="34" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #334155)">QueryDSL / PreparedStatement</text>

    <path d="M 300 20 L 325 20" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#sqlArr)"/>
    <rect x="330" y="0" width="150" height="46" rx="5" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)"/>
    <text x="405" y="18" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">소프트 파싱 재사용</text>
    <text x="405" y="34" text-anchor="middle" font-size="8.5" fill="var(--sl-color-accent, #1e40af)">SQL 인젝션 원천 차단</text>

    <!-- Branch Bad: 문자열 리터럴 결합 -->
    <path d="M 110 80 L 135 90" stroke="#ef4444" stroke-width="1.5" marker-end="url(#sqlBad)"/>
    <rect x="140" y="65" width="160" height="46" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="#ef4444"/>
    <text x="220" y="83" text-anchor="middle" font-size="9.5" font-weight="700" fill="#b91c1c">문자열 결합 (+, ${})</text>
    <text x="220" y="99" text-anchor="middle" font-size="8.5" fill="#ef4444">리터럴 상수 인라인 매칭</text>

    <path d="M 300 90 L 325 90" stroke="#ef4444" stroke-width="1.5" marker-end="url(#sqlBad)"/>
    <rect x="330" y="65" width="150" height="46" rx="5" fill="#fee2e2" stroke="#dc2626"/>
    <text x="405" y="83" text-anchor="middle" font-size="9.5" font-weight="700" fill="#991b1b">하드 파싱 폭증 (위험)</text>
    <text x="405" y="99" text-anchor="middle" font-size="8.5" fill="#b91c1c">CPU 100% · SQL Injection 취약</text>
  </g>
</svg>
</div>

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

- **SQL 해시 생성 및 라이브러리 캐시 분기**:
  - 사용자 질의 수신 시 SQL 텍스트 기반 해시값(SHA-1/MD5) 생성
  - **소프트 파싱 (Soft Parsing, Cache Hit)**:
    - 문법 검증 및 비용 계산 생략, 캐시된 실행 계획 즉시 재사용
    - CPU 점유율 0.1% 미만, 수 밀리초 이내 처리 완료
  - **하드 파싱 (Hard Parsing, Cache Miss)**:
    - 문법/의미 분석 $\rightarrow$ 옵티마이저 비용 산정 $\rightarrow$ 실행 계획 신규 생성
    - `Shared Pool Latch` 경합 발생, CPU 사용률 100% 폭증 및 락 경합 유발
- **정적 SQL vs 리터럴 동적 SQL 비교**:
  - 정적 SQL은 텍스트가 불변이므로 99.9% 소프트 파싱 유지
  - 리터럴 동적 SQL(`WHERE id = 'user1'`, `WHERE id = 'user2'`)은 매번 다른 해시값을 생성하여 하드 파싱 폭증

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

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 현업에서 빈번한 실수 중 하나는 개발자가 '모든 조건을 하나의 만능 정적 SQL'로 처리하겠다고 `WHERE (:name IS NULL OR name = :name)` 형태를 남발하는 것이다. 이러한 쿼리는 파싱 비용은 아낄 수 있을지 몰라도 옵티마이저가 인덱스를 타지 못해 무조건 풀 테이블 스캔(Full Table Scan)을 선택하게 만든다. 반대로 문자열 결합 동적 SQL은 하드 파싱과 SQL 인젝션 지옥을 부른다. 따라서 조건 조합이 다양한 업무는 반드시 QueryDSL 같은 타입 세이프 빌더로 바인드 변수를 결합한 동적 SQL을 생성하는 것이 정답이다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 정적 SQL과 동적 SQL의 5대 비교표와 라이브러리 캐시 분기도를 깔끔하게 구성하겠다. 2교시 25점형이라면 하드 파싱 및 SQL 인젝션 공격 메커니즘을 실제 코드 전/후로 대조하고, 코어 트랜잭션(정적 SQL)과 다차원 검색(QueryDSL 동적 SQL), 대용량 검색(CQRS 패턴 기반 Search Engine 분리)으로 이어지는 계층별 공존 아키텍처를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 웹 애플리케이션에서 문자열 단순 연결 형태의 동적 SQL 남발 시 하드 파싱에 따른 CPU 과열 장애 및 SQL Injection 침해 사고가 필연적으로 발생함. 또한 만능 정적 SQL 작성 시 인덱스 무효화 초래.
- **대응 (개선 방안)**: 코어 OLTP 트랜잭션은 정적 SQL(JPA 표준)로 고정하고, 다차원 가변 검색은 QueryDSL 타입 세이프 빌더를 도입하여 바인드 변수(`PreparedStatement`) 매핑을 강제하는 아키텍처 분리 전략 적용.
- **검증 (검증 기준)**: 소프트 파싱률 99% 이상 유지 모니터링, 정적 코드 분석 도구(SonarQube)를 통한 문자열 결합 SQL 검출률 0건 달성, SQL Injection 모의해킹 전수 통과.
- **효과 (실행 효과)**: 하드 파싱에 따른 DB CPU 점유율 70% 절감, 웹 애플리케이션 보안 취약점 원천 제거, 동적 검색 쿼리 응답 시간 80% 단축.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">문자열 결합 동적 SQL로 하드 파싱 폭증 및 SQL Injection 노출</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">코어 OLTP 정적 분리 + 검색 영역 QueryDSL 바인드 변수 강제화</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">소프트 파싱 99% 이상, SonarQube 문자열 결합 0건, 모의해킹 통과</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">DB CPU 70% 절감, SQLi 보안 사고 원천 예방, 검색 성능 80% 향상</div>
  </div>
</div>

---

## 1교시 10점 답안 발췌

### [문제] 정적 SQL vs 동적 SQL

#### 1. 정적 SQL과 동적 SQL의 정의
- **정적 SQL**: 컴파일 시점에 쿼리 구조가 확정되어 사전 검증 및 소프트 파싱이 보장되는 고정 쿼리
- **동적 SQL**: 런타임에 사용자 조건에 따라 문자열을 조합하여 생성하는 가변형 쿼리

#### 2. 양자 간 특성 비교 및 실행 메커니즘

| 비교 항목 | 정적 SQL (Static SQL) | 동적 SQL (Dynamic SQL) |
|:---|:---|:---|
| **문맥 결정 시점** | 컴파일 타임 (Compile-time) | 실행 런타임 (Run-time) |
| **파싱 메커니즘** | 소프트 파싱 (100% 캐시 적중) | 문자열 결합 시 하드 파싱 폭증 위험 |
| **보안 (SQL Injection)** | 구조적 불변으로 원천 면역 | 바인드 변수 미사용 시 극도로 취약 |
| **조건절 유연성** | 낮음 (고정된 쿼리만 실행) | 극도로 우수 (다차원 동적 필터링) |
| **대표 기술** | Pro*C, JPA `@Query` | MyBatis `<if>`, QueryDSL |

- **실행 메커니즘**: SQL 텍스트 해시값 일치 여부에 따라 라이브러리 캐시 적중(소프트 파싱) 또는 재최적화(하드 파싱) 분기

#### 3. 동적 SQL 최적화 및 보안 방안
- `PreparedStatement` 바인드 변수(`#{param}`, `?`) 전면 적용으로 SQL Injection 원천 차단 및 소프트 파싱 보장

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

- 상위 토픽: [088. 데이터베이스 튜닝 (Database Tuning)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/088_database_tuning.md)
- 연관 토픽: [091. 옵티마이저 (Optimizer)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/091_optimizer.md), [094. TEXT2SQL](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/094_text2sql.md)
