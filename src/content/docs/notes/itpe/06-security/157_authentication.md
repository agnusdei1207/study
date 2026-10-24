---
title: "인증(Authentication)"
author: "agnusdei1207"
date: "2026-10-24T23:11:12+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 인증(Authentication), 주체 인증, 메시지 인증, 연합 신원(Federated Identity), 제로 트러스트
- AAA, 인가(Authorization), 감사(Accounting), SSO, SAML, OpenID Connect, OAuth 2.0
- FIDO2, 패스키(Passkey), 세션 하이재킹, 크리덴셜 스터핑, CAEP, SPOF

## Ⅰ. 인증(Authentication)의 개요

- 핵심 요약 : 접근 주체의 신원과 메시지 출처를 신뢰할 수 있는 수단으로 확인하는 보안의 근간 메커니즘.
- 개념 : 시스템이나 네트워크에서 자원에 접근하려는 **주체** (사용자, 프로세스, 시스템, 디바이스)의 신원이 주장과 일치하는지 확인하고, 메시지의 출처와 진본성을 입증하는 메커니즘.
- 배경 및 필요성 : 로컬 비밀번호 입력을 넘어 클라우드, 마이크로서비스, API(Application Programming Interface) 생태계로 인프라가 확장되면서, 이종 도메인 간에 안전하게 신원을 넘기는 **연합 신원** (Federated Identity)과 **제로 트러스트** 검증이 필요해졌다.
- 주요 목적 : 비인가자의 자원 접근과 신원 사칭을 막고, 인가와 감사가 정확히 작동하도록 하는 신뢰 기반을 제공하는 것.

## Ⅱ. 인증(Authentication)의 특징 및 장점

- 핵심 요약 : 주체와 메시지를 나눠 검증하고 연합 인증과 지속 검증을 결합해, 신뢰 기반을 여러 서비스에 걸쳐 일관되게 유지하는 특징.

1. 주체 인증과 메시지 인증의 분리 : 사용자·기기의 신원과 전송 데이터의 출처를 각각 검증 → 접근 주체와 데이터 양쪽의 신뢰 확보.
2. 연합 인증 : SAML(Security Assertion Markup Language), OAuth 2.0(Open Authorization 2.0)/OpenID Connect 기반 위임으로 한 번의 로그인을 여러 서비스에 재사용 → 계정 분산과 비밀번호 재사용 감소.
3. 지속 검증 : 세션 유지 중에도 기기 상태와 행위를 평가 → 탈취된 세션을 중간에 차단.
4. AAA(Authentication, Authorization, Accounting) 연계 : 인증, 인가, 감사를 한 흐름으로 묶음 → 누가 무엇을 했는지 추적 가능.

## Ⅲ. 인증(Authentication)의 구조 (흐름)

- 핵심 요약 : 서비스 제공자가 인증을 신원 제공자에게 위임하고, 신원 제공자가 서명된 토큰으로 결과를 전달하는 연합 인증 구조.
- 용어 : 서비스 제공자(SP, Service Provider)는 자원을 제공하는 쪽이고, 신원 제공자(IdP, Identity Provider)는 신원을 확인하는 쪽이다. ID 토큰은 JWT(JSON Web Token) 형식이며, 서명 검증에 쓰는 공개키 목록은 JWKS(JSON Web Key Set)로 배포된다.

```text
[ 연합 인증(SSO) 흐름 ]

(1) 사용자가 SP에 접속
          ↓
(2) SP가 IdP로 인증 위임 (리다이렉트)
          ↓
(3) IdP가 다중 요인 인증과 위험 평가 수행
          ↓
(4) IdP가 서명된 ID 토큰(JWT) 발급
          ↓
(5) SP가 JWKS 공개키로 서명 검증 후 로그인
```

```text
[ AAA 보안 프레임워크 ]

Authentication (인증) : 누구인가
          ↓
Authorization (인가) : 무엇을 할 수 있는가
          ↓
Accounting (감사) : 무엇을 했는가
```

- **주체 인증 vs 메시지 출처 인증** : 로그인을 시도하는 사람이나 기기를 확인하는 주체 인증과, 전송된 데이터가 진짜 송신자로부터 위변조 없이 왔음을 증명하는 메시지 인증(HMAC(Hash-based Message Authentication Code), 디지털 서명)으로 나뉜다.
- 연합 신원 관리(Federated Identity Management) : 조직 간이나 클라우드 서비스 간에 계정을 통합해, 단 한 번의 로그인으로 여러 서비스를 이용하게 하는 체계. 대표 방식이 **SSO** (Single Sign-On, 싱글 사인온)이다.
- **AAA** (Authentication, Authorization, Accounting) : 인증, 인가(권한 부여), 계정 관리와 감사(행위 로그 기록)를 결합한 보안 프레임워크.
- **지속적 적응형 인증** (Continuous Adaptive Authentication) : 로그인 시점의 1회성 검증에 그치지 않고 세션 중에도 기기 상태와 행위 프로파일을 평가하여, 위험이 감지되면 세션을 즉시 만료시키는 방식.

## Ⅳ. 인증과 인접 통제의 비교

- 핵심 요약 : 인증은 "누구인가", 인가는 "무엇을 할 수 있는가", 계정 관리는 "무엇을 했는가"에 답하며 순서대로 작동하는 관계.

| 비교 항목 | 인증 (Authentication) | 인가 (Authorization) | 계정 관리 (Accounting) |
| --- | --- | --- | --- |
| 핵심 질문 | 당신은 누구인가 (신원 증명) | 무엇을 할 수 있는가 (접근 허용) | 무엇을 하였는가 (활동 추적) |
| 수행 시점 | 접속과 세션 수립의 최초 단계 | 인증 완료 후 개별 자원이나 API 호출 시 | 자원 사용 중과 종료 후 상시 기록 |
| 대표 기술 | 비밀번호, FIDO2, 생체인증, PKI(Public Key Infrastructure), OTP(One-Time Password) | RBAC(Role-Based Access Control), ABAC(Attribute-Based Access Control), OAuth | Syslog, SIEM(Security Information and Event Management), 감사 로그 DB |
| 실패 시 결과 | 로그인 거부 (401 Unauthorized) | 접근 권한 거부 (403 Forbidden) | 감사 불가, 부인 방지 상실, 규제 위반 |
| 프로토콜 예시 | OpenID Connect, SAML, Kerberos | OAuth 2.0 스코프, XACML(eXtensible Access Control Markup Language), IAM 정책 | RADIUS 계정 기록, TACACS+, CloudTrail |

- 선택 기준 : 자원 접근의 세부 권한이 필요하면 인가 정책을, 사후 책임 추적이 필요하면 계정 관리 로그를 우선 설계.

## Ⅴ. 인증의 한계와 방안

- 핵심 요약 : 세션 탈취, 자동화된 ID·PW 대입, 중앙 신원 제공자 장애를 토큰 바인딩, 속도 제어, 이중화로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 세션 하이재킹 | 발급된 세션 쿠키나 토큰이 XSS(Cross-Site Scripting)나 스니핑으로 탈취되면, 강력한 인증을 거쳤어도 우회됨 | 쿠키에 HttpOnly, Secure, SameSite 속성 적용, mTLS(Mutual TLS) 또는 DPoP(Demonstrating Proof of Possession)로 토큰을 주체에 바인딩 | 세션 탈취 탐지 건수 |
| 크리덴셜 스터핑 | 타 사이트에서 유출된 ID·PW 쌍을 봇으로 대입해 무차별 로그인에 성공 | CAPTCHA(reCAPTCHA v3) 적용, 요청 속도 제한, MFA(Multi-Factor Authentication) 강제 | 비정상 로그인 시도율 |
| 신원 제공자의 단일 실패점 | 중앙 IdP 장애나 침해 시 연동된 다수의 클라우드 서비스와 내부 시스템 로그인이 동시에 중단되는 SPOF(Single Point of Failure) | 멀티 리전 이중화, 비상 시에만 쓰는 Break-glass 계정의 엄격한 관리 | 신원 제공자 가용률 |

## Ⅵ. 인증에 대한 기술사적 제언

- 핵심 요약 : 비밀번호 의존의 축소, 보안 상태의 표준 기반 재평가, 위험 기반 동적 인증을 결합해 인증을 상시 운영 체계로 정착.

1. 인증 체계 조직은 취약한 비밀번호 정책을 단계적으로 줄이고 FIDO2 패스키 기반의 무암호 인증으로 옮겨, 피싱에 강한 인증을 기본값으로 삼아야 한다.
2. 플랫폼 조직은 신원 제공자와 서비스 제공자 사이에 보안 상태 변경 이벤트를 공유하는 CAEP(Continuous Access Evaluation Profile) 같은 표준 프로파일을 연동하여, 세션 재평가가 여러 서비스에 일관되게 적용되도록 하는 것이 바람직하다.
3. 보안 조직은 사용자 신원에 기기 무결성, 접속 위치, 시간대, IP 평판을 더해 위험을 실시간으로 점수화하고, 고위험 상황에서만 추가 인증을 요구하는 제로 트러스트 기반 동적 인증 구조를 구축해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 인증은 모든 접근 통제의 출발점이며, 정적 단일 요인 인증을 벗어난 지속 검증 체계가 전제.
- 시사점 : 인증이 강화되어도 세션과 신원 제공자가 함께 보호되어야 신뢰 기반이 유지되므로, 인증을 세션 전체의 수명 주기로 관리해야 한다.
