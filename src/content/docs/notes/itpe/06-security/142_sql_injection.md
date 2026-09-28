---
title: "SQL Injection"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "142. SQL Injection"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 정보보안 → 입력 검증·애플리케이션 보안 → **SQL Injection**

## 30초 인출

- **본질:** 사용자 입력값이 데이터베이스 쿼리 생성 시 검증 없이 문자열로 결합되어, 공격자가 주입한 악의적인 SQL 구문이 쿼리 구조로 해석·실행되는 웹 애플리케이션 취약점
- **메커니즘:** 입력값 미검증 동적 결합 $\rightarrow$ DBMS 쿼리 파서가 코드와 데이터 경계 붕괴 인지 $\rightarrow$ 비인가 데이터 조회·변조 및 OS 명령어(xp_cmdshell) 실행
- **통찰:** 단순 WAF 문자열 차단은 난독화로 우회되므로 PreparedStatement 매개변수화와 동적 식별자 화이트리스트 맵핑 및 RASP 문법 트리 분석 필수

<details>
<summary>핵심 용어</summary>

- **SQL Injection** : 외부 입력 데이터를 SQL 구문으로 오인 해석하게 만들어 DB를 조작하는 공격.
- **PreparedStatement** : 쿼리 컴파일과 데이터 바인딩을 분리하여 입력값을 순수 리터럴로만 취급하는 기법.
- **Blind SQLi** : 에러나 결과 화면이 출력되지 않을 때 참/거짓 응답 또는 지연 시간(Sleep)을 측정해 데이터를 추출하는 기법.
- **Second-Order SQLi** : 1차 입력 시 안전하게 저장된 데이터가 다른 기능에서 동적 쿼리로 재실행될 때 발현되는 공격.

</details>

## 2~4교시 예상문제 (25점)

> 웹 애플리케이션의 SQL Injection 취약점 발생 원리(코드와 데이터의 경계 붕괴), 공격 유형(In-band, Blind, Out-of-band)을 설명하고, PreparedStatement의 내부 동작 원리 및 엔지니어링 다층 방어 방안을 제시하시오. (예상·25점)

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 클라이언트의 신뢰할 수 없는 입력값을 검증 및 이스케이프 없이 동적 SQL 쿼리에 그대로 결합할 때, 데이터 영역이 실행 가능한 명령 코드(Code)로 해석되어 비인가 질의가 실행되는 주입 취약점 |
| 목적 | 사용자 인증 우회, 데이터베이스 내 기밀 정보(고객 개인정보, 비밀번호 해시) 대량 탈취, 테이블 변조·삭제, 데이터베이스 서버 권한 탈취 및 내부망 침투 |

- OWASP Top 10의 'Injection' 항목에 지속적으로 등재된 고위험 취약점으로, 근본 원인은 쿼리 문법 구조(Structure)와 데이터(Literal)의 경계 붕괴에서 비롯됨

## Ⅱ. SQL Injection의 핵심 기술적 특성

| 특성 항목 | 세부 내용 및 기술적 의미 | 엔지니어링 구현 가치 |
|---|---|---|
| 코드-데이터 경계 붕괴 | 문자열 결합 시 입력된 따옴표(`'`)나 주석(`--`)이 SQL 파서에 의해 연산자 및 키워드로 해석 | 입력 데이터가 실행 코드로 변질되는 구조적 결함 |
| 채널 독립적 위협 경로 | 에러 메시지가 출력되지 않는 폐쇄형 환경에서도 시간 지연(Sleep)을 통해 비트 단위 데이터 추출 가능 | 화면 UI 응답 여부와 무관한 데이터 유출 가능성 |
| 다단계 파급 효과 (2차 침투) | DB 내 저장 프로시저(xp_cmdshell) 및 UDF(User Defined Function) 악용 시 OS 명령 실행 | 웹 서버 침해를 넘어 데이터베이스 호스트 장악 |
| 정적 파라미터화로 완전 예방 | PreparedStatement 적용 시 쿼리 파싱 트리가 먼저 고정되어 100% 원천 방어 가능 | 개발 단계의 안전한 코딩 표준 정립으로 해결 가능 |

- 단순한 데이터베이스 조작을 넘어 클라우드 메타데이터 조회(SSRF 연계) 및 Active Directory 권한 장악으로 이어질 수 있는 고위험 특성 보유

## Ⅲ. PreparedStatement 매개변수화 원리 및 공격 방어 프로세스

```text
[취약한 동적 SQL vs PreparedStatement 매개변수화 처리 비교]

 1. 취약한 동적 SQL (String Concatenation):
    사용자 입력: admin' OR '1'='1
    생성 쿼리: SELECT * FROM users WHERE id = 'admin' OR '1'='1'
    결과: 파서가 OR '1'='1'을 조건식(Code)으로 해석하여 전수 참(True) 판정 -> 인증 우회!

 2. 안전한 PreparedStatement 매개변수화:
    [애플리케이션]                           [데이터베이스 엔진 (DBMS)]
          │                                             │
          │ 1. 쿼리 템플릿 사전 컴파일                    │
          │    PREPARE stmt FROM                        │
          │    "SELECT * FROM users WHERE id = ?"       │
          ├────────────────────────────────────────────>│ 2. 구문 분석 및 실행 계획(AST) 고정
          │                                             │    (입력 자리 ?는 순수 값으로 고정)
          │                                             │
          │ 3. 런타임 값만 바인딩 (EXECUTE)              │
          │    EXECUTE stmt USING "admin' OR '1'='1"    │
          ├────────────────────────────────────────────>│ 4. "admin' OR '1'='1" 전체를
          │                                             │    단순한 하나의 문자열 리터럴로 대조
          │                                             │    ==> 주입 공격 완벽 무력화!
```

| 처리 단계 | 핵심 엔지니어링 동작 | 보안 통제 결과 |
|---|---|---|
| 1. 문법 분석 (Parse) | DBMS가 SQL 템플릿(`SELECT ... WHERE id = ?`)을 먼저 파싱하여 추상 구문 트리(AST) 생성 | 쿼리의 논리적 실행 구조 영구 확정 |
| 2. 실행 계획 수립 | 인덱스 스캔, 조인 순서 등 최적화된 실행 계획을 메모리(Plan Cache)에 캐싱 | 성능 향상 및 구문 재해석 차단 |
| 3. 파라미터 바인딩 | 외부에서 전달된 매개변수 값을 플레이스홀더(`?`) 위치에 순수 데이터 리터럴로 결합 | 따옴표나 SQL 키워드가 포함되어도 값으로 취급 |
| 4. 안전한 쿼리 실행 | 고정된 실행 계획에 데이터 값만 전달하여 연산 수행 | 악의적 SQL 구문 주입 원천 무력화 |

## Ⅳ. SQL Injection 주요 공격 유형 비교

| 공격 유형 | 세부 기법 | 데이터 추출 메커니즘 | 공격 탐지 및 대응 난이도 |
|---|---|---|---|
| In-Band SQLi (동일 채널) | Error-based | DB 에러 메시지(`conversion failed...`)에 쿼리 결과를 포함시켜 출력 유도 | 낮음 (DBMS 상세 에러 페이지 차단으로 방어) |
| In-Band SQLi (동일 채널) | Union-based | `UNION SELECT` 구문을 결합하여 다른 테이블의 데이터를 웹 응답에 병합 | 낮음 (결과 컬럼 수 및 데이터 타입 매칭 필요) |
| Inferential / Blind SQLi | Boolean-based | 참/거짓 조건(`AND 1=1`)에 따른 웹 페이지의 미세한 응답 변화(길이, 텍스트) 관찰 | 보통 (반복 질의 필요, 바이너리 서치 활용) |
| Inferential / Blind SQLi | Time-based | `WAITFOR DELAY '0:0:5'` 또는 `pg_sleep(5)`으로 응답 지연 시간을 유발해 비트 추출 | 높음 (서버 응답 시간 통계 분석 필요) |
| Out-of-Band SQLi | DNS / HTTP 유출 | DB의 네트워크 함수(`xp_dirtree`, `UTL_HTTP`)를 악용해 외부 공격자 서버로 DNS 질의 | 높음 (방화벽의 DB 아웃바운드 차단 필수) |

## Ⅴ. SQL Injection 방어 시 엔지니어링 한계와 해결 방안

| 한계 | 방안 |
|---|---|
| `ORDER BY` 절, 동적 테이블명, 컬럼명은 SQL 문법상 PreparedStatement의 플레이스홀더(`?`) 파라미터 바인딩이 불가능하여 여전히 문자열 결합 사용 | 식별자 파라미터에 대한 엄격한 서버 측 화이트리스트 맵핑(예: `Map<String, String>`에 허용된 컬럼명만 등록)을 강제하고, MyBatis에서 `${}` 사용을 금지하며 `#{}` 및 QueryDSL 안전 빌더 적용 |
| WAF(웹 방화벽)의 정규표현식 기반 차단 룰에만 의존할 경우, 다중 URL 인코딩, 유니코드 변환, 공백 대체 주석(`/**/`)을 통한 시그니처 우회 침투 | WAF는 보조 방어선으로만 유지하고, JVM/Node.js 런타임 레벨에서 RASP(Runtime Application Self-Protection) 에이전트를 가동하여 실제 DB로 전송되는 SQL 구문의 문법 트리(AST) 변형을 실시간 차단 |
| 1차 입력 시점에는 특수문자를 검증하여 안전하게 DB에 저장되었으나, 다른 관리자 화면이나 배치 작업에서 해당 데이터를 재조회하여 동적 쿼리로 재실행하는 2차 주입(Second-Order SQLi) 위협 | 입력 시점의 단순 문자열 치환(Blacklist Sanitization)에 의존하지 않고, 데이터를 조회하여 2차 재질의를 수행하는 모든 애플리케이션 계층에서도 예외 없이 PreparedStatement 매개변수화 원칙 관철 |
| 취약점이 발생했을 때 데이터베이스 관리자 계정(sa, root, DBA)으로 구동 중인 경우 단 한 번의 공격으로 DB 전체 탈취 및 OS 쉘 장악 | 데이터베이스 연결 풀(Connection Pool) 계정에 대해 DDL(DROP, ALTER) 권한을 박탈하고 해당 앱이 사용하는 특정 테이블에 대한 DML(SELECT, INSERT, UPDATE, DELETE) 최소 권한만 부여하며 `xp_cmdshell` 프로시저 영구 비활성화 |

## Ⅵ. 시큐어 코딩 및 애플리케이션 다계층 방어 체계 제언

```text
[SQL Injection 원천 차단을 위한 3대 계층 심층 방어 아키텍처]

 ┌─────────────────────────────────────────────────────────────┐
 │                 1. 개발 및 빌드 계층 (DevSecOps)            │
 │   - SAST (정적 코드 분석: SonarQube) 취약 동적 SQL 탐지    │
 │   - MyBatis `${}` 사용 금지 린트 룰(Checkstyle) 강제 적용   │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────┴──────────────────────────────┐
 │              2. 애플리케이션 런타임 계층 (Application Core)   │
 │   - PreparedStatement 및 ORM (JPA / QueryDSL) 전면 적용     │
 │   - ORDER BY / 동적 컬럼 화이트리스트 Enum 매핑             │
 │   - RASP 에이전트 연동 AST 비정상 변형 실시간 차단          │
 └──────────────────────────────┬──────────────────────────────┘
                                │
 ┌──────────────────────────────┴──────────────────────────────┐
 │                 3. 데이터베이스 인프라 계층 (DB Hardening)   │
 │   - 최소 권한 DB 유저 분리 (DDL 권한 박탈)                   │
 │   - OS 명령 실행 프로시저(xp_cmdshell) 영구 제거            │
 │   - DB 서버 아웃바운드 인터넷(DNS, HTTP) 전면 차단 (OOB 방어)│
 └─────────────────────────────────────────────────────────────┘
```

| 관리 영역 | 핵심 엔지니어링 세부 과제 | 통제 목표치 |
|---|---|---|
| 소스코드 검증 | CI/CD 파이프라인 내 SAST 기반 미바인딩 동적 SQL 검출 | 소스코드 내 취약 동적 SQL 0건 |
| DB 권한 관리 | 웹 애플리케이션 전용 계정의 DDL 권한 및 시스템 프로시저 제거 | 관리자(DBA) 전용 권한 부여율 0% |
| 아웃바운드 통제 | DB 서버에서 외부 인터넷(포트 53, 80, 443) 아웃바운드 차단 | Out-of-band 유출 경로 완전 차단 (차단율 100%) |

## 출제 이력과 검증 출처

- 제121회 정보관리기술사 예상 연계 주제: 웹 애플리케이션 보안 및 SQL Injection 대응
- OWASP Top 10:2021 - A03:2021 Injection
- OWASP Cheat Sheet Series: SQL Injection Prevention Cheat Sheet
- NIST SP 800-64 Rev. 2: Security Considerations in the System Development Life Cycle
- Microsoft Security: Protecting Against SQL Injection in T-SQL
