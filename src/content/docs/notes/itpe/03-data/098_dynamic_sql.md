---
title: "동적 SQL"
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

## Ⅰ. 유연한 조건 처리를 위한 동적 SQL(Dynamic SQL)의 개요

### 가. 동적 SQL의 정의
- 애플리케이션의 **런타임** (Runtime) 시점에 사용자의 입력 값, 선택 조건, 비즈니스 분기 로직에 따라 문자열을 조합하여 SQL(Structured Query Language) 문장의 구조(SELECT 절, WHERE 조건절, ORDER BY 절 등)를 동적으로 생성하고 실행하는 SQL 기법.
- 컴파일 시점에 구문과 접근 경로가 완전히 확정되는 **정적 SQL** (Static SQL)과 대조됨.

### 나. 정적 SQL vs 동적 SQL 비교

| 비교 항목 | 정적 SQL (Static SQL) | 동적 SQL (Dynamic SQL) |
| :--- | :--- | :--- |
| **구문 확정 시점** | 애플리케이션 컴파일 / 빌드 시점에 완벽히 확정 | 애플리케이션 런타임 실행 시점에 동적 조립 |
| **SQL 파싱 비용** | 사전 파싱 및 실행 계획 캐싱(소프트 파싱) 극대화 | 구조 변경 시마다 하드 파싱(Hard Parsing) 발생 가능 |
| **보안성** | 바인드 변수 강제로 SQL Injection 원천 면역 | 단순 문자열 결합 시 SQL Injection 공격에 극도로 취약 |
| **개발 유연성** | 조건이 복잡한 다중 검색 화면 구현 시 SQL 중복 급증 | 가변 검색 조건, 다차원 필터링에 최상의 유연성 제공 |

---

## Ⅱ. 동적 SQL의 성능 병목 메커니즘: 하드 파싱 vs 소프트 파싱

### 가. DBMS의 SQL 파싱 처리 흐름

```text
[ SQL 파싱 및 실행 계획 캐시 흐름 ]
[SQL 인입] ---> [SGA 라이브러리 캐시 검색 (해시 매칭)]
                     |
         +-----------+-----------+
         |                       |
   (캐시에 존재 - 완전 일치)   (캐시에 없음 / 신규 SQL)
         v                       v
  [소프트 파싱 (Soft)]      [하드 파싱 (Hard Parsing)]
  - 기존 실행 계획 즉시 재사용  - 문법 검사 + 권한 검사 + 옵티마이저 비용 계산
  - CPU 소모 극소, 초고속    - CPU 폭증, 라이브러리 캐시 래치(Latch) 경합!
```

### 나. 리터럴 SQL(Literal SQL)의 위험성과 바인드 변수(Bind Variable)

```sql
-- [안티패턴: 리터럴 문자열 결합 -> 매번 하드 파싱 발생]
SELECT * FROM EMP WHERE id = ' + input_id + ';  -- id가 1, 2, 3일 때마다 다른 SQL로 인식!

-- [모범패턴: 동적 조건에 바인드 변수 사용 -> 최초 1회만 하드 파싱 후 캐시 재사용]
SELECT * FROM EMP WHERE id = :id;
```

---

## Ⅲ. 현대적 ORM 및 프레임워크에서의 동적 SQL 구현 기술

### 가. MyBatis 동적 태그를 통한 안전한 SQL 조립

```xml
<select id="searchOrders" resultType="Order">
  SELECT * FROM ORDERS
  <where>
    <if test="customerId != null">
      AND customer_id = #{customerId}  <!-- 바인드 변수 처리 (#) -->
    </if>
    <if test="startDate != null and endDate != null">
      AND order_date BETWEEN #{startDate} AND #{endDate}
    </if>
  </where>
</select>
```

### 나. Querydsl 기반 타입 세이프(Type-Safe) 동적 쿼리
- 문자열 조립의 컴파일 타임 오류 검출 불가 한계를 극복하기 위해, Java 코드 기반으로 `BooleanBuilder` 또는 `BooleanExpression`을 체이닝하여 오타 없이 안전한 동적 쿼리 작성.

---

## Ⅳ. 동적 SQL의 주요 한계점 및 해결 방안

- 바인드 변수 미사용으로 인한 **하드 파싱** (Hard Parsing) 및 공유 풀 고갈 :
  - 한계점 : 문자열 단순 결합(String Concatenation) 방식으로 동적 SQL 작성 시 리터럴 SQL이 매번 신규 컴파일되어 CPU(Central Processing Unit) 점유율 급등 및 라이브러리 캐시 래치 경합 발생.
  - 해결 방안 : MyBatis/JPA(Java Persistence API) 등 매퍼 프레임워크에서 바인드 파라미터(`#{param}`) 필수 사용, 동적 조건 분기 시에도 **사전 바인딩 템플릿** (Parameterized Query) 엄격 준수.
- **SQL 인젝션** (SQL Injection) 취약점 노출 및 보안 침해 :
  - 한계점 : ORDER BY 절이나 테이블명, 컬럼명 동적 지정 시 사용자 입력값이 검증 없이 쿼리에 삽입되어 데이터 탈취 및 시스템 침해 위험 노출.
  - 해결 방안 : **화이트리스트** (Whitelist) 기반 파라미터 검증, 안전한 식별자 매핑 클래스 운영, 정적 분석(SAST, Static Application Security Testing) 도구를 통한 취약한 동적 SQL 코드 자동 점검.
- 조건 분기 복잡성에 따른 실행 계획 최적화 난제 및 플랜 불안정성 :
  - 한계점 : 검색 조건 조합에 따라 생성되는 쿼리 패턴이 수십~수백 가지로 분기되어 옵티마이저가 최적의 인덱스를 선택하지 못하고 플랜 변동성 심화.
  - 해결 방안 : 핵심 조회 조건별로 정적 쿼리를 분리 작성(모듈화), 쿼리 힌트를 활용한 강제 인덱스 지정, QueryDSL과 같은 타입 안전 동적 쿼리 빌더 활용.

## Ⅴ. 엔터프라이즈 환경에서의 동적 SQL 운영 실무 제언

- `#`(바인드) vs `$`(리터럴 치환) 문법의 엄격한 통제 : MyBatis 등 SQL 매퍼에서 컬럼값은 무조건 `#{param}` 바인드 변수를 강제하고, 테이블명이나 정렬 방향(`ASC/DESC`) 등 바인드 변수 적용이 불가능한 영역에 한해 `${orderCol}` 치환을 허용하되, 입력값에 대한 엄격한 화이트리스트 검증(Whitelist Validation)을 적용하여 SQL Injection을 원천 차단해야 함.
- **바인드 피킹** (Bind Peeking)과 실행 계획 왜곡 방어 : CBO(Cost-Based Optimizer)가 최초 파싱 시 바인드 변수 값을 훔쳐보고(Peeking) 특정 소수 데이터에 최적화된 실행 계획을 캐싱하여 다른 대다수 요청에서 풀 스캔이 유발되는 사고를 막기 위해, 편향이 극심한 대형 테이블의 핵심 검색 조건은 정적 분기 쿼리로 분리할 것을 제언함.
