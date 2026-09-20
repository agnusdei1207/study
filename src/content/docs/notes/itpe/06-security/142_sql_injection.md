---
title: "SQL Injection"
author: "Gemini 3.8 Flash"
date: "2026-09-20T01:00:00+09:00"
tags:
  - "notes-security"
extra:
  model: "Gemini 3.8 Flash"

---

## 답안 골격
```text
[SQL 인젝션(SQL Injection)] ◀━━ 머리: Ⅶ 내 의견 (단순 특수문자 치환 땜질 탈피 → PreparedStatement 매개변수화 쿼리 강제와 DB 계정 최소 권한화)
 ┃
 ┣━ Ⅰ 개요 ───── 웹 애플리케이션의 사용자 입력값 검증 부재를 악용하여 악의적인 SQL 구문을 주입함으로써, 백엔드 데이터베이스의 쿼리 문법 구조를 왜곡하여 비인가 데이터 조회·변조·삭제 및 관리자 권한을 탈취하는 대표적 웹 취약점 공격
 ┣━ Ⅱ 특징 ───── OWASP Top 10 최상위 위험군 · 코드와 데이터의 미분리에서 발생 · 인증 우회, 데이터베이스 덤프, OS 원격 명령 실행(xp_cmdshell)까지 전이 가능
 ┣━ Ⅲ 구조 ───── 공격 벡터 3대 유형: 인밴드(Error-based, Union-based) + 블라인드(Boolean-based, Time-based) + 아웃오브밴드(DNS 조회 유도)
 ┣━ Ⅳ 흐름 ───── 사용자 입력창에 악의적 구문(`' OR '1'='1`) 입력 → 애플리케이션이 쿼리 문자열에 동적 결합 → DB 컴파일러가 조작된 구문 실행 → 전체 회원 정보 노출
 ┣━ Ⅴ 비교 ───── 단순 문자열 결합 동적 쿼리(데이터가 코드로 해석되어 인젝션 노출) vs Prepared Statement(쿼리 구조 사전 컴파일, 입력값은 단순 상수로만 취급)
 ┗━ Ⅵ 실무 ───── ORM(MyBatis, JPA) 사용 시 동적 정렬 필드(`ORDER BY`) 인젝션 노출 / 2차 인젝션(Second-order SQLi) / WAF 필터링 우회(인코딩 기법)
```
- 필수 키워드: SQL Injection · PreparedStatement(매개변수화 쿼리) · Error-based · Union-based · Blind SQLi · 코드와 데이터 분리 · 최소 권한 원칙
- 기출: 제121회 2교시 6번: "OWASP에서 발표한 보안 위협 인젝션(Injection)의 개념과 대응 방안" (이전: 92회)

## 한 줄 본질
- 개발자가 편의를 위해 사용자 입력값을 SQL 문자열에 그대로 이어 붙여(Concatenate) 명령어로 실행시켜 버리는 코드-데이터 미분리 병목 → 쿼리 문법 구조를 먼저 컴파일하고 입력값은 단순 리터럴 데이터로만 바인딩(PreparedStatement)하여 원천 차단 → 데이터베이스 탈취 방지 / 동적 정렬 등 유연한 쿼리 작성 시 제약

## 핵심 그림
```text
[동적 SQL 문자열 결합 취약점 vs Prepared Statement 안전한 컴파일 비교]

[1. 취약한 동적 SQL: 데이터가 코드로 둔갑]
  - 개발자 코드: `SELECT * FROM users WHERE id = '` + input + `' AND pw = '` + pw + `'`
  - 공격자 입력: `' OR '1'='1' --`
  - DB 파싱 결과: `SELECT * FROM users WHERE id = '' OR '1'='1' -- ...`
                   └── 항상 참(True)으로 평가되어 비밀번호 검증 없이 1등 관리자로 로그인!

[2. 안전한 Prepared Statement: 쿼리 구조 선(先) 컴파일]
  - 1단계 (구조 컴파일): `SELECT * FROM users WHERE id = ? AND pw = ?` (문법 트리 확정)
  - 2단계 (데이터 바인딩): ? 자리에 `' OR '1'='1' --` 전체가 '단순한 문자열 ID 하나'로 입력됨
  - DB 실행 결과: 그런 이상한 아이디를 가진 사용자가 없으므로 즉각 로그인 거부!
```

## 핵심 용어
- 매개변수화된 질의 (Parameterized Query / Prepared Statement): 데이터베이스 엔진이 쿼리의 문법적 구조(SELECT, FROM, WHERE)를 먼저 컴파일하여 파싱 트리를 고정해 둔 후, 물음표(`?`) 파라미터 자리에 사용자 입력을 순수한 데이터 값으로만 안전하게 대입하는 프로그래밍 방식
- 블라인드 SQL 인젝션 (Blind SQL Injection): DB 에러 메시지가 화면에 출력되지 않는 안전해 보이는 사이트에서, 참/거짓 조건에 따른 웹페이지 반응 차이나 `SLEEP(5)` 함수의 응답 지연 시간차를 이용해 1비트씩 데이터를 긁어모으는 지능형 공격

## 핵심 통찰
- SQL 인젝션은 25년 전이나 지금이나 원리가 똑같음 → "명령어(Code)와 데이터(Data)의 경계가 무너졌기 때문"임
- 정규식으로 따옴표(`'`)나 `SELECT`, `UNION` 같은 키워드를 필터링하는 방식(Blacklist)은 100% 뚫림 → URL 인코딩, 대소문자 혼합(`sElEcT`), 공백 우회(`/**/`) 등 수백 가지의 WAF 우회 기법이 존재함
- 유일하고 완벽한 해법은 'PreparedStatement'뿐임 → 아무리 흉악한 SQL 구문이 들어와도 DB 엔진은 이를 코드가 아닌 '단순한 문자열 리터럴'로 취급하므로 쿼리 구조가 1밀리미터도 뒤틀리지 않음

## 이웃 토픽과 구분
- SQL Injection vs XSS(Cross-Site Scripting): SQLi = 공격 대상이 백엔드 "데이터베이스" / XSS = 공격 대상이 웹브라우저를 열고 있는 다른 "클라이언트 사용자"

## 문제·원인·대책
- 사례: 공공기관 웹사이트 게시판 검색창에 SQL 인젝션 공격이 발생해 10만 명의 시민 개인정보 테이블 전체가 유출된 사고
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 사용자 입력값을 SQL 쿼리에 직접 문자열 결합 (`Statement` 사용) | 개발자의 시큐어 코딩 미준수 및 문자열 쿼리 조합 | PreparedStatement 파라미터 바인딩 및 ORM 안전한 바인딩 강제 | 쿼리 구조 왜곡 원천 차단 |
| DB 침해 시 `DROP TABLE` 및 OS 시스템 파일 무단 열람 | 웹 애플리케이션이 DB `sa`(시스템 관리자) 최고 권한 계정으로 접속 | DB 계정 권한 최소화(해당 DB 특정 테이블 SELECT/INSERT만 부여) | 취약점 노출 시에도 데이터 파괴 및 시스템 장악 방지 |

## 이렇게 출제된다
- 제121회 2교시 6번: "OWASP에서 발표한 보안 위협 인젝션(Injection)의 개념과 대응 방안" → 요구 포인트: Ⅰ 인젝션 발생 원리 + Ⅲ 공격 유형(In-band, Blind, OOB) + Ⅵ PreparedStatement 및 시큐어 코딩 대책

## 내 의견
- [MyBatis 프레임워크의 `${}` 사용 전면 금지 및 CI 빌드 차단] MyBatis 매퍼 파일에서 바인딩을 의미하는 `#{}` 대신 문자열 치환인 `${}`를 사용하여 발생하는 SQL 인젝션이 실무 결함의 80%를 차지함 → 나라면: 정적 코드 분석 룰(SonarQube)에 MyBatis XML 내의 `${}` 패턴을 치명적 결함(Blocker)으로 등록하여, 코드에 `${}`가 단 1줄이라도 존재하면 빌드 배포를 원천 중단시키는 강제 파이프라인 수립

## 찾아볼 것
- OWASP Top 10: A03:2021-Injection 및 SQL Injection Prevention Cheat Sheet
