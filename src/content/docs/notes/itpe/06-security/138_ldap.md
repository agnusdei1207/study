---
title: "LDAP(Lightweight Directory Access Protocol)"
author: "agnusdei1207"
date: "2026-10-24T23:10:07+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "응용"
extra:
  question_no: "138"
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- LDAP(Lightweight Directory Access Protocol), DIT, DN, 바인드(Bind), LDAPS, LDAP 인젝션
- SSO, Active Directory, SCIM, ACL, 객체 클래스(objectClass), 속성(Attribute)

## Ⅰ. LDAP의 개요

- 핵심 요약 : 사용자·그룹·자원 정보를 계층형 디렉터리에 모아 조회와 중앙 집중 인증을 제공하는 개방형 프로토콜.
- 개념 : 네트워크에 분산된 사용자, 그룹, 컴퓨터 자원, 조직 구조 등의 디렉터리 정보를 계층형 트리로 저장하고, TCP(Transmission Control Protocol)/IP(Internet Protocol) 위에서 검색·조회와 인증을 제공하는 **경량 디렉터리 접근 프로토콜** (LDAP, Lightweight Directory Access Protocol)로, RFC(Request for Comments) 4510에 정의된 개방형 표준.
- 배경 및 필요성 : OSI(Open Systems Interconnection) 7계층 기반의 X.500 DAP(Directory Access Protocol)는 프로토콜 스택이 무거워 일반 유닉스와 윈도우 네트워크에서 운용하기 어려웠으므로, TCP/IP 위에서 가볍게 구현할 프로토콜이 요구됨.
- 주요 목적 : 사원 정보, 권한, 시스템 계정을 단일 디렉터리에 통합하여 **싱글 사인온** (SSO, Single Sign-On)과 중앙 집중 접근 통제를 실현.

## Ⅱ. LDAP의 특징 및 장점

- 핵심 요약 : 계층형 트리와 조회 최적화 구조가 대량 검색과 중앙 인증으로 이어지는 방식.

1. **디렉터리 정보 트리** (DIT, Directory Information Tree) : 조직 구조를 계층으로 그대로 반영 → 부서 단위 위임 관리와 검색 범위 지정이 용이.
2. 조회 중심 최적화 : 대부분이 검색인 환경에 맞춰 고속 인덱싱과 캐싱을 제공 → 대량 조회 응답 속도 향상, 쓰기 성능은 상대적으로 낮음.
3. **바인드** (Bind) 기반 인증 : 단순 바인드와 SASL(Simple Authentication and Security Layer) 기반 보안 바인드를 지원 → 인증 절차를 디렉터리 한곳에서 처리.
4. 암호화 채널 지원 : TLS(Transport Layer Security) 위의 LDAPS(LDAP over TLS, 636번 포트) 사용 → 네트워크 도청으로부터 자격 증명 보호.
5. 단일 계정 저장소 : 사원·권한·시스템 계정을 한곳에서 관리 → 입사·퇴사 시 계정 생명주기를 일관되게 반영.

```text
[ DIT 구조 예시 ]

dc=example, dc=com (루트)
    ↓
ou=people (임직원 계정)
    ↓
uid=alice (사용자 엔트리)
```

## Ⅲ. LDAP의 구조 (흐름)

- 핵심 요약 : 루트에서 조직단위를 거쳐 엔트리로 내려가는 트리 구조를 고유 위치 키로 찾고, 바인드로 인증하는 구조.
- **객체 클래스** (objectClass) : 엔트리가 따르는 스키마 유형으로, 엔트리가 가질 수 있는 속성 집합을 정함.
- **속성** (Attribute) : 엔트리가 가지는 값으로, mail, userPassword 같은 항목이 해당함.
- **식별 명칭** (DN, Distinguished Name) : 트리에서 엔트리의 절대 위치를 나타내는 유일한 키이며, 상대 식별 명칭(RDN, Relative Distinguished Name)의 연속 결합으로 표기됨.

```text
[ 바인드(Bind) 인증 흐름 ]

사용자 → 사내 애플리케이션 (VPN, ERP)
    ↓ (ID·PW 입력)
애플리케이션 → LDAP 서버 (LDAPS 636)
    ↓ (DN 검색 후 비밀번호 해시 대조)
LDAP 서버 → 인증 결과 반환
    ↓
로그인 승인 또는 거부
```

## Ⅳ. LDAP의 비교 분석

- 핵심 요약 : 읽기 중심의 LDAP, 쓰기 중심의 관계형 모델, Windows 도메인 특화 디렉터리가 용도 축에서 구분되는 구조.

비교 대상은 **관계형 데이터베이스** (RDBMS, Relational Database Management System)와 **Active Directory** (AD)다.

| 비교 축 | LDAP | RDBMS | Active Directory |
| --- | --- | --- | --- |
| 데이터 모델 | 계층형 트리 (DIT) | 2차원 테이블과 관계 | LDAP 호환 계층형 트리 |
| 최적화 영역 | 읽기·검색 중심, 쓰기는 상대적으로 느림 | 트랜잭션(ACID)과 잦은 쓰기·수정 | Windows 도메인 인증, 그룹 정책 배포 |
| 질의 방식 | LDAP 필터 구문 (&(ou=it)(title=mgr)) | SQL(Structured Query Language) SELECT | LDAP 프로토콜과 Kerberos 결합 |
| 표준 여부 | IETF(Internet Engineering Task Force) 개방형 표준 | 표준 SQL과 벤더별 구현 | Microsoft 독자 구현 (LDAP 호환) |
| 주요 용도 | 주소록, SSO 인증 백엔드, 계정 통합 | ERP(Enterprise Resource Planning) 원장, 주문·결제 | 기업 PC 중앙 제어, 그룹 정책 |

- 선택 기준 : 읽기 위주의 인증과 주소록에는 LDAP이, 빈번한 트랜잭션에는 RDBMS가, Windows 중심 환경의 정책 관리에는 Active Directory가 적합함.

## Ⅴ. LDAP의 한계와 방안

- 핵심 요약 : 필터 인젝션, 평문 통신, 클라우드 연동 한계를 입력 이스케이프, 암호화 채널, 현대 ID 공급자 연계로 보완.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| **LDAP 인젝션** (LDAP Injection) | 사용자 입력을 검색 필터에 검증 없이 연결하여, 특수문자 주입으로 비밀번호 없이 인증 우회 | 모든 입력값에 LDAP 특수문자 이스케이프 적용, 매개변수화된 필터 API 강제 | 필터 입력 검증 실패 건수 |
| 평문 통신에 따른 자격 증명 노출 | 389번 포트의 평문 바인드를 스니핑하면 ID와 비밀번호가 그대로 노출 | 389번 포트를 외부 구간에서 차단하고 LDAPS(636번 포트)나 StartTLS 전환 의무화 | 평문 바인드 시도 건수 |
| 클라우드 SaaS 연동 한계 | 폐쇄망 LDAP을 외부 SaaS가 직접 호출하기 어려움 | **SCIM** (System for Cross-domain Identity Management)과 **SAML** (Security Assertion Markup Language), OIDC(OpenID Connect) 기반 ID 공급자(IdP, Identity Provider)로 계정 자동 프로비저닝 연계 | 자동 프로비저닝 성공률 |

## Ⅵ. LDAP의 기술사적 제언

- 핵심 요약 : 레거시 디렉터리를 직접 노출하지 않고 현대적 신원 연합과 강력한 인증을 앞단에 두는 구조로 전환하는 방향.

1. 온프레미스 레거시 LDAP을 외부에 직접 노출하지 않고, Okta, Keycloak, Entra ID 같은 신원 연합 플랫폼을 전면에 두어 다중 인증(MFA, Multi-Factor Authentication)과 결합하는 계정 브리지 구조를 세우는 것이 바람직하다.
2. Active Directory 환경이라면 LDAP 단순 바인드를 금지하고 LDAP 서명(LDAP signing)과 채널 바인딩(channel binding)을 강제하여, 인증 중계(릴레이) 공격을 구조적으로 막는 정책을 둘 필요가 있다.
3. 디렉터리 접근 권한은 최소 권한(Least Privilege) 원칙으로 설계하여 익명 읽기를 기본 비활성화하고, 비밀번호 해시나 주민번호 같은 기밀 속성은 **ACL** (Access Control List, 접근 제어 목록)으로 은닉하는 운영 기준을 세워야 한다.

## Ⅶ. 결론

- 핵심 요약 : LDAP은 전사 신원을 한곳에 모으는 디렉터리 표준이며, 보안의 핵심은 저장보다 노출 통제에 있음.
- 시사점 : 단일 계정 저장소가 침해되면 인프라 전체가 위험해지므로, 암호화 채널과 입력 검증, ID 공급자 연계를 전제로 운영해야 함.
