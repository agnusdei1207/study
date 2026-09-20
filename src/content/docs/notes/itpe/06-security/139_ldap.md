---
title: "LDAP(Lightweight Directory Access Protocol)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T01:00:00+09:00"
tags:
  - "notes-security"
extra:
  model: "Gemini 3.8 Flash"

---

## 답안 골격
```text
[경량 디렉토리 액세스 프로토콜(LDAP)] ◀━━ 머리: Ⅶ 내 의견 (평문 단순 바인드 취약점 제거 → LDAPS(TCP 636) 암호화와 LDAP 인젝션 방어 입력값 검증 강제)
 ┃
 ┣━ Ⅰ 개요 ───── 복잡하고 무거운 X.500 DAP 프로토콜을 TCP/IP 기반으로 경량화하여, 엔터프라이즈 네트워크 상의 사용자 계정, 조직도, 권한 자원 정보를 계층형 디렉토리 트리(DIT)로 중앙 집중 관리하고 고속 조회·인증을 제공하는 표준 프로토콜
 ┣━ Ⅱ 특징 ───── 읽기(조회/검색) 연산에 극도로 최적화 · 계층적 트리 구조(DIT, Directory Information Tree) · 싱글 사인온(SSO) 및 통합 계정 관리(IAM)의 기반 프로토콜 · 바인드(Bind) 기반 인증
 ┣━ Ⅲ 구조 ───── 식별명(DN: Distinguished Name) 체계: dc(도메인) + ou(조직단위) + cn(공통이름) + uid(사용자ID) + DIT 계층 구조
 ┣━ Ⅳ 흐름 ───── 클라이언트 TCP 연결 → 바인드 요청(Bind Request: DN, Password) → 디렉토리 DB 대조 및 인증 성공 응답 → 검색 요청(Search: 필터) → 엔트리 반환 → 연결 해제(Unbind)
 ┣━ Ⅴ 비교 ───── RDBMS(복잡한 트랜잭션, 쓰기/갱신 빈번, 테이블 정규화) vs LDAP(계층 트리 구조, 읽기/검색 위주, 갱신 드묾, 고속 조회 최적화)
 ┗━ Ⅵ 실무 ───── 단순 바인드(Simple Bind) 사용 시 비밀번호 평문 노출 / 특수문자 조작을 통한 LDAP Injection 공격 / 중앙 서버 단일 실패점(SPOF)
```
- 필수 키워드: LDAP · X.500 경량화 · DIT(Directory Information Tree) · DN(Distinguished Name) · 바인드(Bind) 인증 흐름 · LDAPS(TCP 636) · LDAP 인젝션
- 기출: 제129회 2교시 2번: "접근 제어(Access Control)의 통제정책과 경량 디렉토리 액세스 프로토콜 (LDAP: Lightweight Directory Access Protocol)의 인증 흐름(Flow)"

## 한 줄 본질
- 수백 대의 사내 서버와 애플리케이션마다 계정을 개별 생성하느라 발생하는 계정 파편화와 로그인 인증 지연 병목 → X.500을 경량화한 계층형 트리(DIT)에 사용자 정보를 중앙 집중화하고 읽기 최적화 검색을 제공 → 전사 통합 계정 관리(SSO) 확보 / 평문 전송 시 비밀번호 도청 및 주입 공격 위험

## 핵심 그림
```text
[LDAP 디렉토리 정보 트리(DIT) 계층 구조 및 클라이언트 인증 시퀀스 흐름]

[1. DIT 계층 트리 구조]
          [dc=company, dc=com] (루트 도메인)
                   │
       ┌───────────┴───────────┐
       ▼                       ▼
  [ou=Engineering]        [ou=Sales] (조직 단위)
       │
  [cn=Gildong Hong] ──> 전체 식별명 (DN): `cn=Gildong Hong,ou=Engineering,dc=company,dc=com`

[2. LDAP 인증 흐름 (Authentication Flow)]
  [클라이언트 (사용자)]                                     [LDAP 디렉토리 서버]
          │                                                          │
          │ ─── 1. TCP 연결 수립 (기본 389, LDAPS 636) ────────────> │
          │                                                          │
          │ ─── 2. Bind Request (사용자 DN, 패스워드 전송) ─────────> │ (자격증명 대조)
          │ <── 3. Bind Response (성공: Success / 실패: Invalid) ─── │
          │                                                          │
          │ ─── 4. Search Request (검색 기본 DN, 필터: `(uid=user)`) ─> │ (속성 조회)
          │ <── 5. Search Result (사용자 이메일, 직급, 그룹 권한) ─── │
          │                                                          │
          │ ─── 6. Unbind Request (세션 종료) ─────────────────────> │ (연결 해제)
```

## 핵심 용어
- DN (Distinguished Name): LDAP 디렉토리 트리 내에서 특정 객체(엔트리)를 고유하게 가리키는 완전한 경로 이름으로, 파일 시스템의 절대 경로와 유사함 (예: `cn=admin,ou=IT,dc=org`)
- 바인드 (Bind): 클라이언트가 LDAP 서버에 대해 자신을 인증하고 세션의 권한 수준을 확립하는 초기 작업으로, 평문 전송인 단순 바인드(Simple Bind)와 암호화된 SASL/TLS 바인드가 있음

## 핵심 통찰
- 관계형 데이터베이스(RDB)로 계정을 관리하면 사원 1만 명이 동시 로그인할 때 테이블 조인 락(Lock)으로 성능이 저하됨 → LDAP은 "쓰기는 거의 없고, 조회가 99%인 환경"에 특화되어 설계되었으므로 RDB보다 수배 이상 빠른 검색 성능을 냄
- LDAP 통신은 기본 포트 389번을 쓸 때 모든 패킷(비밀번호 포함)이 평문으로 날아감 → Wireshark로 네트워크를 캡처하면 관리자 비밀번호가 즉각 노출되므로 반드시 TLS로 래핑된 LDAPS(포트 636)를 강제해야 함
- 웹 입력창에 `*`나 `)(&)`를 넣는 'LDAP 인젝션' 공격이 발생하면 비밀번호 없이도 관리자 바인드를 뚫고 전사 조직도 전체를 덤프해 감

## 이웃 토픽과 구분
- LDAP vs Active Directory(AD): LDAP = 디렉토리에 접근하기 위한 "표준 통신 프로토콜" / Active Directory = 마이크로소프트가 LDAP, Kerberos, DNS를 결합해 만든 윈도우용 "디렉토리 서비스 제품"

## 문제·원인·대책
- 사례: 사내 그룹웨어 로그인 페이지에서 입력값 검증 부재로 LDAP 인젝션 공격이 발생해 전사 임직원 주민번호가 유출된 사고
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 특수문자 조작을 통한 LDAP 쿼리 구조 왜곡 (LDAP Injection) | 사용자 입력값을 필터링 없이 동적 LDAP 검색 필터에 문자열 결합 | 준비된 질의(Prepared Statements) 및 특수문자(`*`, `(`, `)`, `&`, `|`) 이스케이프 강제 | 비인가 쿼리 구조 조작 원천 방지 |
| 네트워크 패킷 스니핑을 통한 사내 계정 비밀번호 유출 | 비암호화 기본 포트(TCP 389)를 사용하는 단순 바인드 운영 | LDAPS(TCP 636, TLS 1.3) 전면 전환 및 StartTLS 강제 | 전송 구간 도청 시에도 계정 자격증명 완전 암호화 보호 |

## 이렇게 출제된다
- 제129회 2교시 2번: "접근 제어(Access Control)의 통제정책과 경량 디렉토리 액세스 프로토콜 (LDAP: Lightweight Directory Access Protocol)의 인증 흐름(Flow)" → 요구 포인트: Ⅰ 접근제어 정책(DAC/MAC/RBAC) + Ⅲ LDAP DIT 구조 및 Bind 인증 6단계 시퀀스 도식 + Ⅵ LDAPS 보안 강화 방안

## 내 의견
- [클라우드 IdP(사스 기반)와 연동 시 LDAP 프록시 격리 아키텍처 수립] 온프레미스 레거시 시스템들은 여전히 LDAP 인터페이스만 지원하는데, 사내 계정을 Okta나 Entra ID(클라우드)로 이전하면서 클라우드-온프레미스 간 포트 개방 위험 발생 → 나라면: 공인 인터넷에 사내 LDAP 포트를 절대 개방하지 않고, 온프레미스 내부에 '클라우드 연동 LDAP 브로커 에이전트'를 두어 아웃바운드 443 암호화 터널로만 인증 요청을 중계하도록 네트워크 경계를 분리

## 찾아볼 것
- RFC 4511 (LDAP: The Protocol) 및 OWASP LDAP Injection Prevention Cheat Sheet
