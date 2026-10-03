---
title: "LDAP(Lightweight Directory Access Protocol)"
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

## Ⅰ. LDAP(Lightweight Directory Access Protocol)의 개요

- 개념 : 네트워크 상에 분산된 사용자, 그룹, 컴퓨터 자원, 조직 구조 등의 디렉터리 정보를 **계층형 트리 구조** (DIT)로 저장하고, TCP/IP 상에서 경량화된 방식으로 초고속 검색, 조회 및 중앙 집중 인증을 제공하는 개방형 표준 프로토콜(RFC 4510).
- 배경 및 필요성 : 초기 OSI 7계층의 **X.500 DAP** (Directory Access Protocol)는 프로토콜 스택이 너무 무겁고 복잡하여 범용 유닉스 및 윈도우 네트워크 환경에서 작동하기 어려웠으며, 이를 TCP/IP 상에서 가볍게 구현할 프로토콜이 요구됨.
- 핵심 목적 : 엔터프라이즈 전반의 사원 정보, 권한, 시스템 계정을 단일 디렉터리에 통합 관리하여 **싱글 사인온** (SSO)과 중앙 집중 접근 통제를 실현.

## Ⅱ. LDAP(Lightweight Directory Access Protocol)의 핵심 아키텍처 및 동작 메커니즘

LDAP은 계층형 디렉터리 정보 트리(DIT: Directory Information Tree), 고유 식별 명칭인 DN(Distinguished Name), **객체 클래스** (objectClass), **속성** (Attribute) 모델로 구성되며, 클라이언트-서버 모델로 동작함.

```text
[ LDAP 디렉터리 정보 트리(DIT) 구조 및 바인드(인증) 메커니즘 ]

 [ 루트(dc) ] --------------> dc=example, dc=com
                                   |
         +-------------------------+-------------------------+
         |                                                   |
 [ 조직단위(ou) ]                                     [ 조직단위(ou) ]
 ou=people (임직원 계정)                               ou=groups (보안 그룹)
         |                                                   |
         +-----------------------+                           +-------------------+
         |                       |                           |                   |
 [ 엔트리(uid) ]          [ 엔트리(uid) ]              [ 엔트리(cn) ]       [ 엔트리(cn) ]
 uid=alice                uid=bob                     cn=developers        cn=admins
 - mail: alice@corp.com   - mail: bob@corp.com        - member: alice      - member: bob
 - userPassword: {SSHA}...- userPassword: ...

 * Alice의 고유 명칭(DN): "uid=alice, ou=people, dc=example, dc=com"

 [ 클라이언트 바인드(Bind) 인증 흐름 ]
  [사용자 클라이언트] ---- (1) ID/PW 입력 ----> [ 사내 애플리케이션 (VPN, ERP) ]
                                                       |
                                                       | (2) LDAP 바인드 요청 (LDAPS 636)
                                                       v
                                            [ 중앙 LDAP / Active Directory ]
                                            * DN 검색: (&(uid=alice)(mail=...))
                                            * 비밀번호 해시 대조 검증
                                                       |
                                                       v
  [사용자 로그인 승인] <--- (3) Auth Success <--------+
```

- **디렉터리 정보 트리(DIT: Directory Information Tree)** : 국가(c), 조직(o), 조직단위(ou), 공통이름(cn), 사용자ID(uid) 등 현실 조직 구조를 반영한 계층적 트리 구조로 엔트리를 체계적 배치.
- **식별 명칭(DN: Distinguished Name)** : 트리 상에서 엔트리의 절대적 위치를 나타내는 유일한 고유 키로, 상대 식별 명칭(RDN: Relative DN)들의 연속적 결합으로 표기.
- **읽기 중심(Read-heavy) 아키텍처** : 쓰기(트랜잭션) 성능에 최적화된 RDBMS와 달리, 대부분이 검색 및 조회인 환경에 맞춰 고속 인덱싱과 캐싱을 제공.
- **보안 바인드(Bind)와 LDAPS** : 익명 바인드, 단순 바인드(평문), SASL 기반 보안 바인드를 지원하며, 네트워크 도청 방지를 위해 TLS 암호화 채널(LDAPS 포트 636)이 필수적임.

## Ⅲ. LDAP(Lightweight Directory Access Protocol)의 세부 구성 요소 및 비교 분석

| 비교 항목 | **LDAP** (디렉터리 서비스) | **관계형 데이터베이스** (RDBMS) | **Active Directory** (AD) |
| --- | --- | --- | --- |
| 데이터 모델 | 계층형 트리 구조 (DIT) | 2차원 테이블 및 관계 (Relational) | 계층형 트리 (LDAP 표준 준수 구현체) |
| 최적화 영역 | 읽기(Read/Search) 극대화, 쓰기 느림 | 트랜잭션 ACID, 빈번한 쓰기/수정 | Windows 도메인 인증, 정책(GPO) 배포 |
| 조회 언어 | LDAP 필터 구문: (&(ou=it)(title=mgr)) | 정형 질의 언어 (SQL: SELECT ...) | LDAP 프로토콜 및 Kerberos v5 결합 |
| 표준 여부 | IETF 오픈 표준 프로토콜 (OpenLDAP 등) | ANSI SQL 표준 및 벤더 독자 구현 | Microsoft 독자 엔터프라이즈 솔루션 |
| 주요 용도 | 전사 주소록, SSO 인증 백엔드, 계정 통합 | ERP 원장, 전자상거래 주문/결제 데이터 | 기업 윈도우 PC 중앙 제어, 그룹 정책 관리 |

- LDAP은 전사 자원의 단일 계정 저장소 역할을 수행하므로, 침해 시 전사 인프라 장악으로 직결되는 바 LDAPS와 인젝션 방어가 최우선 과제임.

## Ⅳ. LDAP(Lightweight Directory Access Protocol)의 주요 한계점 및 해결 방안

- LDAP Injection을 통한 인증 우회 및 디렉터리 탈취 :
  - 한계점 : 사용자 입력값을 검증 없이 LDAP 검색 필터 문자열에 직접 연결할 경우, 공격자가 특수문자(')(*)(|)(&)를 주입하여 비밀번호 없이 관리자 바인드 성공.
  - 해결 방안 : 모든 사용자 입력값에 대해 LDAP 특수문자 이스케이프 함수를 적용하고, 프레임워크 수준의 매개변수화 바인딩 쿼리 강제화.
- 기본 평문(389번 포트) 통신에 따른 자격증명 도청 위험 :
  - 한계점 : 레거시 시스템이 표준 LDAP 389번 포트를 사용할 경우 네트워크 스니핑을 통해 사용자 ID와 패스워드가 평문으로 쉽게 노출.
  - 해결 방안 : 389번 포트를 방화벽에서 전면 차단하고, TLS 1.3 기반의 LDAPS(636 포트) 또는 StartTLS 프로토콜 전환 의무화.
- 클라우드 SaaS 애플리케이션과의 프로토콜 연동 한계 :
  - 한계점 : 방화벽 외부의 현대적 SaaS(M365, Salesforce)는 사내 폐쇄망 LDAP 프로토콜을 직접 호출하기 어려움.
  - 해결 방안 : SCIM(System for Cross-domain Identity Management) 및 SAML/OIDC 기반 ID 공급자(IdP)를 구축하여 클라우드 계정 자동 프로비저닝 연계.

## Ⅴ. LDAP(Lightweight Directory Access Protocol) 적용 및 발전을 위한 기술사적 제언

- 현대적 IdP(Okta, Keycloak, Entra ID)로의 계정 브릿징 아키텍처 수립 : 온프레미스 레거시 LDAP을 직접 노출하지 않고 현대적 신원 연합 IdP를 전면에 두어 RESTful API 및 다중 인증(MFA) 결합.
- Active Directory Kerberos 인증과의 보안 연계 하드닝 : LDAP 단순 바인드 사용을 금지하고 티켓 기반의 강력한 Kerberos SASL 상호 인증을 적용하여 릴레이 공격 방어.
- 디렉터리 접근 권한의 최소 권한(Least Privilege) ACL 적용 : 익명 읽기 권한을 기본 비활성화하고, 부서별/조직별 엔트리에 세분화된 접근 제어 목록(ACL)을 적용하여 기밀 속성(비밀번호 해시, 주민번호) 은닉.
