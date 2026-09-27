---
title: "LDAP(Lightweight Directory Access Protocol)"
author: "Codex"
date: "2026-09-27T17:15:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "139. LDAP(Lightweight Directory Access Protocol)"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

정보보안 → 디렉터리·접근통제 → LDAP(Lightweight Directory Access Protocol)

## 30초 인출

- 본질: LDAP은 계층형 디렉터리의 엔트리를 조회·변경하고 바인드를 수행하는 프로토콜
- 메커니즘: TLS로 서버 인증·전송 보호 → DN·필터로 엔트리 검색 → 바인드 결과와 별개로 앱 권한 결정

<details><summary>핵심 용어</summary>

- **DIT:** 디렉터리 엔트리의 계층 구조.
- **DN:** ** 계층 안에서 엔트리를 식별하는 이름.

</details>

---

## 1교시 예상문제 (10점)

> LDAP의 개념과 DIT·DN·바인드의 역할을 설명하시오. (예상·10점)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 계층형 디렉터리 엔트리의 조회·변경과 바인드를 위한 표준 프로토콜 |
| 목적 | 사용자·조직 정보의 중앙 조회 및 인증 바인드 지원 |

- **정의:** ** 디렉터리 엔트리를 검색·갱신하고 인증 바인드를 수행하는 TCP/IP 기반 표준 프로토콜.
- **구조:** ** DIT는 엔트리의 계층, DN은 엔트리의 고유 식별 경로, 속성은 계정·조직 정보 표현.
- **보안:** ** 단순 바인드의 비밀번호는 TLS 보호 채널에서 전송하고 검색 필터 입력을 문맥별 이스케이프.

---

## 2~4교시 예상문제 (25점)

> LDAP 인증 흐름과 접근제어 연계 및 주입·평문 전송 대응을 설명하시오. (예상·25점)

---

## 2~4교시 25점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 계층형 디렉터리 엔트리의 조회·변경과 바인드를 위한 표준 프로토콜 |
| 목적 | 사용자·조직 정보의 중앙 조회 및 인증 바인드 지원 |

### Ⅱ. 역할
- LDAP은 디렉터리 접근·바인드의 프로토콜. 애플리케이션의 SSO·권한 부여 체계와 구분.
### Ⅲ. 처리 흐름
- 연결 → 서버 인증과 TLS 수립 → 서비스 또는 사용자 바인드 → 필요한 엔트리 검색 → 결과 검증·업무 권한 결정 → 연결 종료.
### Ⅳ. 구조
- DIT의 상위·하위 엔트리, DN·RDN 및 속성, 검색 기반 DN·범위·필터의 관계.
### Ⅴ. 통제
- TLS 없는 비밀번호 전송 금지, 서버 인증서 검사, 검색 필터 이스케이프, 최소 권한·반환 속성 제한과 로그 감사.

### 기술사적 제언

- TLS와 서버 인증을 강제하고 디렉터리 검색 결과를 애플리케이션 권한으로 자동 간주하지 않는다.

## 출제 이력과 검증 출처

- 기존 출제 기록은 공식 원문을 확보하지 못해 회차·문구 미검증. 아래 문항은 예상문제.
- [RFC 4511, LDAP Protocol](https://www.rfc-editor.org/rfc/rfc4511): DIT·검색·바인드와 StartTLS
- [RFC 4513, LDAP Authentication Methods](https://www.rfc-editor.org/rfc/rfc4513): TLS와 단순 바인드 보안 조건
- [OWASP LDAP Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html): 검색 필터 입력 이스케이프
