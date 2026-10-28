---
title: "접근통제(Access Control)"
author: "agnusdei1207"
date: "2026-10-24T22:55:16+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "032"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 접근통제(Access Control), 식별(Identification), 인증(Authentication), 인가(Authorization), 책임추적성(Accountability)
- 최소 권한 원칙(Least Privilege), 직무 분리(Separation of Duties), 알 필요성 원칙(Need-to-Know)
- DAC, MAC, RBAC, ABAC, 다요소 인증(MFA), 지속적 신뢰 평가(CARTA), 특권 접근 관리(PAM), WORM

## Ⅰ. 접근통제(Access Control)의 개요

- 핵심 요약 : 인가되지 않은 접근을 사전에 차단하고, 인가된 주체만 허용된 범위에서 자원을 쓰게 하는 예방적 보안 통제.
- 개념 : 정보 자산에 대한 비인가 접근을 차단하고 인가된 주체(사용자, 프로세스)만 허가된 권한 범위에서 자원을 사용하도록 보장하는 정보보호 통제인 **접근통제** (Access Control).
- 배경 및 필요성 : 시스템이 복잡해지면서 자격증명 탈취와 내부자 권한 오남용으로 기밀이 유출되는 사고가 반복되어, 신원 확인부터 행위 추적까지 이어지는 체계적 통제가 필요해짐.
- 주요 목적 : 인가된 주체만 허용 범위에서 자원을 쓰게 하고, 모든 행위를 사후에 추적할 수 있도록 하는 것.

## Ⅱ. 접근통제(Access Control)의 특징 및 장점

- 핵심 요약 : 4단계 검증 체인과 기본 원칙이 결합되어, 사전 차단과 사후 추적을 함께 보장하는 구조.

1. **식별** (Identification) : 주체가 계정, 사번 등으로 자신을 밝힘 → 인증 대상을 확정.
2. **인증** (Authentication) : 지식, 소유, 생체 요소로 주장하는 신원을 검증 → 도용된 계정의 진입 차단.
3. **인가** (Authorization) : 직무와 정책에 따라 자원별 읽기, 쓰기, 실행 권한을 판단 → 권한 과다 부여 방지.
4. **책임추적성** (Accountability) : 행위를 시각과 함께 변조 방지 로그로 기록 → 사고 원인 규명과 부인 방지.
5. **최소 권한 원칙** (Least Privilege) : 업무에 필요한 권한만 부여 → 오남용 시 피해 범위 축소.
6. **직무 분리** (Separation of Duties) : 요청과 승인을 서로 다른 주체가 수행 → 단독 부정 행위 억제.
7. **알 필요성 원칙** (Need-to-Know) : 업무상 알아야 할 정보에만 접근 허용 → 기밀 노출면 축소.

## Ⅲ. 접근통제(Access Control)의 구조 (흐름)

- 핵심 요약 : 식별, 인증, 인가, 책임추적성이 하나의 체인으로 결합되어 한 단계의 결함이 전체 통제를 무너뜨리는 구조.

```text
[ 접근통제 4단계 체인 ]

접근 요청 주체 (사용자, 프로세스)
          ↓
1. 식별 : 누구인가
          ↓
2. 인증 : 주장하는 본인이 맞는가
          ↓
3. 인가 : 무엇을 할 수 있는가
          ↓
4. 책임추적성 : 언제 무엇을 했는가
```

```text
[ 단계별 결함의 전파 ]

인증 성공
   ↓
인가 검사 누락
   ↓
타인 데이터 무단 조회
   ↓
감사 로그 부재로 사후 추적 불가
```

| 단계 | 핵심 질문 | 주요 구현 기술 | 주요 공격 위협 |
| --- | --- | --- | --- |
| 식별 | Who are you? | 계정명, 사번, API(Application Programming Interface) 클라이언트 ID | 계정 열거 |
| 인증 | Prove it! | 비밀번호, OTP(One-Time Password), FIDO2, PKI(Public Key Infrastructure) 인증서 | 무차별 대입, 크리덴셜 스터핑, 피싱 |
| 인가 | What can you do? | ACL(Access Control List), 역할 기반 정책 | 권한 상승, IDOR(Insecure Direct Object Reference) |
| 책임추적성 | What did you do? | 감사 로그, SIEM(Security Information and Event Management) | 로그 삭제, 감사 기능 비활성화 |

## Ⅳ. 접근통제(Access Control)의 비교

- 핵심 요약 : 권한을 누가 결정하느냐에 따라 임의적, 강제적, 역할 기반, 속성 기반 모델로 나뉘며, 운영 경직성과 세밀함이 서로 상충함.

| 모델 | 권한 결정 기준 | 장점 | 한계 |
| --- | --- | --- | --- |
| DAC(Discretionary Access Control, 임의적 접근 통제) | 자원 소유자의 재량 | 운영이 유연함 | 권한이 임의로 확산될 위험 |
| MAC(Mandatory Access Control, 강제적 접근 통제) | 중앙의 보안 등급 정책 | 강제력이 높음 | 운영이 경직됨 |
| RBAC(Role-Based Access Control, 역할 기반 접근 통제) | 직무별 역할 | 권한 관리가 단순함 | 역할 설계가 부정확하면 권한 과다 |
| ABAC(Attribute-Based Access Control, 속성 기반 접근 통제) | 주체, 자원, 환경의 속성 조건 | 시간, 위치 등 세밀한 통제 | 정책 설계와 평가 비용 증가 |

## Ⅴ. 접근통제(Access Control)의 한계와 방안

- 핵심 요약 : 로그인 시점의 정적 검증, 특권 계정, 잔존 계정이 주요 한계이며 지속 검증과 자동 회수로 대응해야 함.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 세션 중 권한 남용 | 1회 인증 이후 환경 변화를 감지하지 못해 세션 탈취 시 무단 사용 | 지속적 신뢰 평가(CARTA, Continuous Adaptive Risk and Trust Assessment) 도입, 위험 신호 시 단계별 재인증(Step-up MFA) 강제 | 재인증 발생 건수 |
| 특권 계정 독점과 감사 로그 무력화 | 관리자 계정 탈취 시 정책 변경과 로그 삭제 | 특권 접근 관리(PAM, Privileged Access Management) 도입, 감사 로그를 WORM(Write Once Read Many) 저장소에 전송 | 특권 세션 승인 건수 |
| 퇴사, 이동 후 잔존 계정 | 인사 변경이 IAM(Identity and Access Management)에 즉시 반영되지 않아 비인가 접속 위험 잔존 | 인사 DB와 IdP(Identity Provider)를 연동해 퇴사 처리 시 계정 자동 비활성화 | 미회수 계정 수 |

## Ⅵ. 접근통제(Access Control)에 대한 기술사적 제언

- 핵심 요약 : 통제 기준을 네트워크 위치에서 신원으로 옮기고, 권한을 주기적으로 재검증하는 운영 체계로 전환.
- 방화벽의 IP 기준 통제에 의존하던 구조는 중앙 IdP를 기준으로 한 신원 중심 통제로 재편하는 것이 바람직하다.
- 권한은 한 번 부여하고 끝내지 않고, 정기적인 재인증 캠페인으로 현업 책임자가 권한 목록을 검토하는 거버넌스를 정착시킬 필요가 있다.
- 장기적으로는 비밀번호 의존도를 낮추고 패스키(Passkey) 기반 패스워드리스 인증으로 전환하여 크리덴셜 공격 노출면을 줄이는 방향을 검토해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 접근통제는 권한을 나누는 기술이 아니라 신원, 권한, 행위를 하나로 묶어 검증하는 신뢰 체계임.
- 단계별 검증이 끊기지 않을 때 접근통제는 사고를 예방하고 사후에도 책임을 가릴 수 있는 기반이 됨.
