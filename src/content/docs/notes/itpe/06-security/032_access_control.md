---
title: "접근통제(Access Control)"
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

## Ⅰ. 접근통제(Access Control)의 개요

- 개념 : 정보 자산에 대한 비인가자의 접근을 차단하고, 인가된 주체(사용자, 프로세스)만이 허가된 권한 범위 내에서 안전하게 자원을 활용할 수 있도록 보장하는 정보보호의 가장 근본적인 예방적 보안 메커니즘.
- 배경 및 필요성 : 네트워크 및 시스템의 복잡성이 증대됨에 따라 자격증명 탈취, 내부자 횡령, 권한 오남용으로 인한 중요 기밀 유출 사고가 지속 발생하여 신원 확인부터 행위 추적까지의 체계적 통제 절차 필수화.
- 핵심 목적 : 식별(Identification), 인증(Authentication), 인가(Authorization), 책임추적성(Accountability)의 4대 보안 통제 단계 실현 및 **최소 권한 원칙** (Least Privilege) 구현.

## Ⅱ. 접근통제(Access Control)의 핵심 아키텍처 및 동작 메커니즘

접근통제는 식별 -> 인증 -> 인가 -> 책임추적성의 'I-A-A-A' 4단계 생명주기를 거치며, 직무 분리와 최소 권한의 기본 원칙을 바탕으로 시스템 자원을 통제함.

```text
[ 접근통제의 4단계 핵심 메커니즘 (I-A-A-A) ]

   [ 접근 요청 주체 (User / Process) ]
                  │
                  ▼
   +-------------------------------------------------------------+
   | 1. 식별 (Identification)    : "당신은 누구인가?"            |
   |    - 사용자 ID, 사번, 이메일, 공개키 식별자 제시            |
   +------------------------------┬------------------------------+
                                  │
                                  ▼
   +-------------------------------------------------------------+
   | 2. 인증 (Authentication)    : "당신이 주장하는 본인이 맞는가?"|
   |    - 지식(비밀번호), 소유(OTP/스마트카드), 생체(지문/홍채)   |
   +------------------------------┬------------------------------+
                                  │
                                  ▼
   +-------------------------------------------------------------+
   | 3. 인가 (Authorization)     : "무엇을 할 수 있는 권한이 있는가?"|
   |    - 접근 권한 부여 (DAC, MAC, RBAC, ABAC 정책 평가)        |
   +------------------------------┬------------------------------+
                                  │
                                  ▼
   +-------------------------------------------------------------+
   | 4. 책임추적성 (Accountability) : "언제, 어떤 행위를 수행했는가?" |
   |    - 감사 로그(Audit Log), SIEM 전송, 부인 방지(전자서명)   |
   +-------------------------------------------------------------+
```

- **식별** (Identification) : 시스템에 접근하고자 하는 주체가 자신이 누구인지를 알리는 단계(ID 입력).
- **인증** (Authentication) : 주체가 주장하는 신원이 진실임을 **다요소 인증** (MFA, Multi-Factor Authentication)을 통해 암호학적 또는 물리적으로 검증하는 단계.
- **인가** (Authorization) : 인증된 주체에게 직무와 정책에 따라 특정 파일/기능에 대한 작업 권한(읽기/쓰기/실행)을 허용하는 단계.
- **책임추적성** (Accountability) : 인가된 주체가 수행한 모든 명령어, 조회, 수정 이력을 타임스탬프와 함께 변경 불가능한 로그로 기록하는 단계.
- 3대 기본 원칙 : **최소 권한의 원칙** (필요한 최소한만 부여), **직무 분리의 원칙** (단독 승인 방지), **알 필요성의 원칙** (Need-to-Know).

## Ⅲ. 접근통제(Access Control)의 세부 구성 요소 및 비교 분석

| 단계 | 핵심 질문 | 주요 구현 기술 | 취약점 및 공격 위협 |
| --- | --- | --- | --- |
| 1. 식별 | Who are you? | 사용자 계정명, 사번, API(Application Programming Interface) 클라이언트 ID | 계정 열거(Account Enumeration) |
| 2. 인증 | Prove it! | 비밀번호, FIDO2, OTP(One-Time Password), PKI(Public Key Infrastructure) 인증서 | 브루트포스, 크리덴셜 스터핑, 피싱 |
| 3. 인가 | What can you do? | ACL(Access Control List), RBAC(Role-Based Access Control) 역할, ABAC(Attribute-Based Access Control) XACML 정책 | 권한 상승(Privilege Escalation), IDOR |
| 4. 책임추적성 | What did you do? | Syslog, 감사 데몬(auditd), SIEM(Security Information and Event Management) | 로그 삭제, 감사 기능 비활성화, 타임스탬프 |

- 어느 한 단계라도 결함이 존재하면 전체 접근통제 체인이 붕괴되므로(예: 인증은 성공했으나 권한 인가 체크 누락 시 타인 데이터 무단 조회 발생), 4개 단계가 유기적인 체인으로 결합되어야 함.

## Ⅳ. 접근통제(Access Control)의 주요 한계점 및 해결 방안

- 단일 인증 단계 통과 후 세션 유지 시간 동안의 권한 남용 :
  - 한계점 : 로그인 시점에 1회 인증된 이후 세션이 만료될 때까지 사용자의 환경 변화나 탈취 행위를 감지하지 못하는 정적 검증 한계.
  - 해결 방안 : 지속적 **적응형 위험 및 신뢰 평가** (CARTA) 도입으로 IP(Internet Protocol) 급변, 비정상 API 호출 시 **단계별 재인증** (Step-up MFA) 강제.
- **특권 계정** (Root/Admin)의 권한 독점 및 감사 로그 무력화 :
  - 한계점 : 최고 관리자 계정을 탈취한 공격자가 접근통제 정책을 임의 변경하고 자신의 침해 흔적이 담긴 감사 로그를 영구 삭제.
  - 해결 방안 : **특권 권한 관리** (PAM, Privileged Access Management) 솔루션 도입으로 루트 비밀번호를 난수화 격리하고, 감사 로그는 실시간 WORM(Write Once Read Many) 불변 스토리지로 전송.
- 조직 이동 및 퇴사자의 **잔존 휴면 계정** (Orphan Account) :
  - 한계점 : 인사 발령이나 퇴사 시 IT(Information Technology) 시스템에서 계정 권한이 즉시 회수되지 않아 전 직원에 의한 비인가 원격 접속 위험 잔존.
  - 해결 방안 : 인사 DB(Database)와 전사 IAM(Identity and Access Management)/IdP(Identity Provider)를 API로 실시간 동기화하여 퇴사 처리 시 1분 이내 전 시스템 계정 비활성화 자동화.

## Ⅴ. 접근통제(Access Control) 적용 및 발전을 위한 기술사적 제언

- '**신원 중심 접근통제** (Identity-First Security)' 확립 : 네트워크 방화벽 IP 통제에서 벗어나 중앙화된 단일 IdP(Entra ID, Okta) 기반의 신원 통제 표준화.
- 정기적인 **권한 재인증** (Access Recertification) 캠페인 의무화 : 매 반기마다 부서장이 팀원의 접근 권한 목록을 검토하고 불필요한 권한을 회수하는 거버넌스 수립.
- **패스워드리스** (Passwordless) 인증 전환 : 비밀번호를 아예 없애고 FIDO2 패스키(Passkey) 및 생체인증을 도입하여 크리덴셜 스터핑 공격 원천 무력화.
