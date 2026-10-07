---
title: "인젝션(Injection) 공격"
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

## Ⅰ. 인젝션(Injection) 공격의 개요

- 개념 : 신뢰할 수 없는 외부 사용자 입력값이 애플리케이션의 **인터프리터** (Interpreter)나 **파서** (Parser)에 의해 문법적 명령어 또는 쿼리의 일부로 오해되어 그대로 실행됨으로써, 백엔드 데이터베이스를 탈취하거나 시스템 OS(Operating System) 쉘 명령어를 실행하는 모든 취약점 공격군 (OWASP(Open Worldwide Application Security Project) Top 10의 최상위 위협).
- 배경 및 필요성 : 소프트웨어가 사용자의 입력을 '순수한 데이터'로 취급하지 않고 '명령어 문자열 결합'에 그대로 사용함에 따라 문법적 제어 흐름이 공격자의 의도대로 왜곡되는 고전적이면서도 치명적인 결함.
- 핵심 목적 : 인증 우회, 데이터베이스 덤프, 서버 파일 시스템 조작, 나아가 OS 커널 레벨의 **임의 코드 실행** (RCE, Remote Code Execution)을 통해 서버 전체를 완전 장악.

## Ⅱ. 인젝션(Injection) 공격의 핵심 아키텍처 및 동작 메커니즘

인젝션 공격은 인터프리터의 종류에 따라 SQL(Structured Query Language) Injection, OS Command Injection, LDAP(Lightweight Directory Access Protocol) Injection, XPath/XQuery Injection, Server-Side Template Injection(SSTI) 등으로 광범위하게 분류됨.

```text
[ 다양한 인젝션(Injection) 공격 유형 및 파싱 왜곡 아키텍처 ]

                      [ 공격자의 조작된 입력값 ]
                                  |
         +------------------------+------------------------+
         |                        |                        |
         v                        v                        v
 [ SQL Injection ]       [ Command Injection ]     [ SSTI (템플릿 인젝션) ]
 * 입력: ' OR 1=1 --     * 입력: ; rm -rf / ;      * 입력: {{7*7}} -> 49 실행
 * 대상: SQL 인터프리터  * 대상: OS 시스템 쉘(sh) * 대상: Jinja2/Thymeleaf
 * 파싱 왜곡: WHERE 참    * 파싱 왜곡: 다중 명령     * 파싱 왜곡: 파이썬 RCE
         |                        |                        |
         +------------------------+------------------------+
                                  |
                                  v
 [ 취약한 애플리케이션: 데이터와 명령어를 결합하여 실행! ]
  * System("ping " + user_input) -> OS 쉘이 공격자 명령 추가 실행!
                                  |
                                  v
 [ 시스템 침해 결과: 기밀 유출, 랜섬웨어 설치, 원격 쉘 획득 ]
 ================================================================
 [ 근본적 방어 원칙: 데이터와 명령어의 물리적/논리적 분리! ]
  1. 정적 매개변수화 (PreparedStatement / Parameterized API)
  2. 시스템 쉘 실행 금지 (execve 직접 호출, sh/cmd 미경유)
  3. 엄격한 입력값 화이트리스트 정규식 검증
```

- **OS Command Injection** : 웹 애플리케이션이 ping, mail 등 시스템 명령어를 호출할 때 사용자 입력값을 검증 없이 쉘 문자열에 결합하여 공격자가 세미콜론(;)이나 파이프(|)로 추가 임의 명령어를 실행.
- **LDAP Injection** : 사용자 입력을 검증 없이 LDAP 검색 필터에 결합하여 디렉터리 서비스의 인증을 우회하거나 전사 사원 명부 및 비밀번호 해시 탈취.
- **Server-Side Template Injection (SSTI)** : 템플릿 엔진(Jinja2, FreeMarker 등)에 악의적인 템플릿 구문이 직접 전달되어 템플릿 인터프리터 내부에서 객체 리플렉션을 통해 OS 쉘 코드를 탈취 실행.
- 공통 메커니즘: 파서의 문법 오해 : 모든 인젝션의 본질은 파서가 데이터(Data) 영역과 제어 코드(Control Code) 영역을 명확히 구분하지 못하여 데이터가 명령어로 승격되어 실행되는 현상임.

## Ⅲ. 인젝션(Injection) 공격의 세부 구성 요소 및 비교 분석

| 비교 항목 | **OS Command Injection** | **SQL Injection** | **LDAP Injection** | **SSTI** (Template) |
| --- | --- | --- | --- | --- |
| 대상 인터프리터 | OS 시스템 쉘 (/bin/sh, cmd.exe) | 데이터베이스 엔진 (Oracle, MySQL) | 디렉터리 서비스 (OpenLDAP, AD) | 웹 템플릿 엔진 (Jinja2, Velocity) |
| 공격 영향 | 서버 OS 완전 장악 (RCE) | DB(Database) 전수 유출, 원장 변조, 관리자 우회 | 사내 계정 도용, 디렉터리 정보 유출 | 서버 메모리 접근 및 원격 쉘 탈취 |
| 특수 문자 | ;, &, \|, `, $(), > | ', ", --, ;, /* */, UNION | *, (, ), &, \|, !, = | {{, }}, ${, }, <%, %> |
| 위험도 | 극상 (서버 장악 즉각 완료) | 극상 (대규모 데이터 침해) | 상 (계정 인프라 붕괴) | 극상 (웹 프레임워크 샌드박스 탈출) |
| 원천 해결책 | 쉘 호출 금지, execve 배열 전달 | PreparedStatement 바인딩 | 매개변수화 검색 필터 | 템플릿에 사용자 입력 직접 렌더링 금지 |

- 인젝션 공격은 수십 년간 지속된 가장 원초적인 취약점이나, '데이터와 명령어의 분리'라는 단순한 소프트웨어 공학적 원칙을 준수하면 원천 차단이 가능함.

## Ⅳ. 인젝션(Injection) 공격의 주요 한계점 및 해결 방안

- 레거시 시스템의 시스템 쉘(sh/cmd) 호출 관행 잔존 :
  - 한계점 : 개발 편의를 위해 'system()', 'exec()', 'Runtime.getRuntime().exec()'을 무분별하게 호출하여 문자열 인자를 결합하는 레거시 코드 광범위 존재.
  - 해결 방안 : 쉘 인터프리터를 경유하지 않는 구조적 API(ProcessBuilder에 인자를 문자열 배열로 개별 전달) 사용 강제.
- 블랙리스트 기반 필터링의 다양한 인코딩/우회 기법 노출 :
  - 한계점 : 공백, 세미콜론 차단 시 ${IFS}, 줄바꿈(LF), 탭, 16진수 인코딩, 환경변수 슬라이싱 등으로 필터링 정규식을 손쉽게 우회.
  - 해결 방안 : 블랙리스트를 완전히 폐기하고 허용된 문자(영숫자 등)만 통과시키는 엄격한 화이트리스트 검증 라이브러리 전면 적용.
- ORM(Object-Relational Mapping) 및 현대적 프레임워크에서의 부주의한 Raw Query 작성 :
  - 한계점 : JPA(Java Persistence API)나 MyBatis를 사용하면서도 성능 튜닝이나 복잡한 동적 조건 검색을 핑계로 Native Query 및 문자열 결합(${param}) 남용.
  - 해결 방안 : 정적 분석(SAST, Static Application Security Testing) 룰셋에서 Raw Query 문자열 결합 검출 시 빌드 실패(Build-break) 정책 적용.

## Ⅴ. 인젝션(Injection) 공격 적용 및 발전을 위한 기술사적 제언

- 데브섹옵스(DevSecOps) CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인의 SAST/DAST(Dynamic Application Security Testing) 자동화 연동 : 코드 커밋 시마다 SonarQube, Fortify 등 정적 분석 도구로 모든 인젝션 취약점을 전수 검사하여 사전 배포 차단.
- 시스템 쉘 실행 환경의 최소 권한 격리 (Container & Least Privilege) : 웹 애플리케이션 프로세스를 일반 사용자로 구동하고 불필요한 시스템 바이너리(/bin/sh, /usr/bin/curl)가 제거된 초경량 Distroless 컨테이너 이미지 사용.
- 웹 애플리케이션 방화벽(WAF, Web Application Firewall) 및 RASP(Runtime Application Self-Protection)를 통한 심층 다층 방어 : 네트워크 경계에서 인젝션 시그니처를 인라인 차단하는 WAF와, 애플리케이션 런타임에서 비정상 시스템 콜을 감시 차단하는 RASP 결합.
