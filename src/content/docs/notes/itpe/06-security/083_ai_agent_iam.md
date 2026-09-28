---
title: "AI 에이전트 IAM"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  order: 83
  label: "083. AI 에이전트 IAM"
  badge:
    text: "서브"
    variant: note
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"

---

## 지식 로드맵 내 현재 위치

신원·접근 관리 → 비인간 신원(NHI) → AI 에이전트 IAM

## 30초 인출

- **본질:** 사용자를 대리하여 자율적으로 외부 도구, 데이터베이스, API를 호출하는 AI 에이전트의 머신 신원(Non-Human Identity)을 식별하고 권한 위임 및 접근 통제를 수행하는 IAM 체계.
- **메커니즘:** 사용자 인증 및 작업 위임 → OAuth 2.0 Token Exchange(RFC 8693) 기반 단기 다운스코프 토큰 발급 → 도구 호출 시 파라미터 유효성 검증 → 원 사용자와 에이전트 신원 동시 감사 기록.
- 통찰: 에이전트에 영구 고권한 마스터 키 부여 시 프롬프트 인젝션을 통한 인프라 장악이 발생하므로, Just-In-Time(JIT) 최소 권한 인가와 정책 집행점(PEP) 통제 구축 필수.

<details><summary>핵심 용어</summary>

- **AI 에이전트 IAM**: 자율 에이전트의 고유 신원 증명, 권한 범위 위임, 컨텍스트 기반 동적 인가를 관리하는 머신 신원 보안 거버넌스.
- **RFC 8693(OAuth 2.0 Token Exchange)**: 보안 토큰을 다른 보안 토큰으로 교환하여 사용자의 권한을 대리 실행자(에이전트)에게 안전하게 위임하는 표준 규격.
- **과도한 대행(Excessive Agency, OWASP LLM06)**: 에이전트에 과도한 도구 실행 권한이나 지나치게 넓은 리소스 접근 권한이 부여되어 발생하는 보안 취약점.
- **Confused Deputy 문제**: 낮은 권한의 공격자가 고권한을 가진 대리인(에이전트)을 속여 자신이 접근할 수 없는 리소스에 접근하도록 유도하는 보안 취약점.
- **Just-In-Time(JIT) 인가**: 영구적 권한을 배제하고 특정 작업(Task) 수행 시점에만 필요한 최소 권한을 동적으로 발급 후 즉시 회수하는 메커니즘.
</details>

---

## 2~4교시 예상문제 (25점)

> 자율형 AI 에이전트의 확산에 따른 신원 인증 및 권한 위임의 기술적 위험을 분석하고, RFC 8693(Token Exchange) 기반의 AI 에이전트 IAM 아키텍처와 Confused Deputy 방지를 위한 엔지니어링 방안을 설명하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 인간 사용자를 대리하여 복합 태스크를 수행하는 AI 에이전트에 대해 머신 고유 신원을 부여하고, 세분화된 단기 위임 권한을 동적으로 제어·감사하는 신원 및 접근 통제 체계 |
| 목적 | 에이전트의 권한 오남용(Excessive Agency) 및 대리인 공격(Confused Deputy) 방지, 비인가 리소스 조작 차단, 종단 간(End-to-End) 책임 추적성 확보 |

## Ⅱ. AI 에이전트 IAM의 주요 특징

| 특징 | 세부 내용 | 보안 엔지니어링 구현 |
|---|---|---|
| 3자 주체 분리 | 원 사용자(User), 실행 에이전트(Agent), 목적지 리소스(Resource) 신원을 엄격히 구분 | 클레임 내 `sub`(사용자)와 `act`(에이전트) 분리 표기 |
| 동적 다운스코핑 | 사용자가 가진 전체 권한 중 해당 에이전트 태스크 수행에 필수적인 최소 스코프만 추출 | RFC 8693 Token Exchange, Scope 축소 |
| 단기 유효 기간 | 고정된 장기 API 키를 배제하고 태스크 완료 즉시 만료되는 초단기 임시 토큰(STS) 사용 | 수 분(5~15분) 유효 기간의 임시 세션 토큰 강제 |
| 정책 기반 동적 인가 | 에이전트의 도구 호출 시점 파라미터(SQL 문, 금액 한도, 대상 테이블)를 실시간 평가 | OPA(Open Policy Agent) 기반 세부 속성 인가(ABAC) |
| 양방향 감사 증적 | 작업 실행 로그에 원 사용자의 신원과 이를 대리 실행한 에이전트 인스턴스 ID 동시 기록 | OpenTelemetry 기반 분산 추적 태그 연동 |

## Ⅲ. AI 에이전트 신원 인증 및 토큰 교환 아키텍처

```text
[ 사용자 (User) ]
       │ 1. 사용자 인증 및 에이전트 태스크 위임 (User Access Token 전달)
       ▼
[ AI 에이전트 (Autonomous Agent) ]
       │ 2. RFC 8693 Token Exchange 요청 (Subject Token + Agent Client Credentials)
       ▼
[ IAM / 권한 부여 서버 (Authorization Server) ]
       │ 3. 에이전트 신원 검증 및 스코프 다운스코핑 (최소 권한의 대리 토큰 발급)
       ▼
[ AI 에이전트 ] ── 4. 단기 대리 실행 토큰 수신 (Actor Claim: Agent, Subject Claim: User)
       │
       │ 5. Tool Calling 요청 (API + Parameter)
       ▼
[ 정책 집행점 (PEP / Guardrail Gateway) ]
       │ 6. 파라미터 검증 (금액 한도, 대상 자산, 비정상 SQL 차단)
       ▼
[ 대상 리소스 서버 (Target Resource Server / Database) ]
       │ 7. 유효성 검증 성공 시 작업 실행
       ▼
[ SIEM / 감사 로깅 (Audit Log) ] <── [User Identity + Agent Instance ID 기록]
```

| 구성 요소 | 기술적 역할 | 핵심 프로토콜 및 표준 |
|---|---|---|
| Token Exchange 서버 | 사용자의 원본 토큰과 에이전트의 머신 자격증명을 검증하고 단기 위임 토큰 발행 | RFC 8693 OAuth 2.0 Token Exchange |
| 에이전트 자격증명 | 에이전트 런타임 자체의 안전한 신원 증명(비밀키 탈취 방지) | mTLS, SPIFFE/SPIRE 워크로드 신원 증명 |
| 정책 집행점(PEP) | 에이전트가 생성한 도구 파라미터의 구문 및 업무 규칙 적합성 실시간 인라인 검사 | Envoy Proxy, OPA(Open Policy Agent) |
| Actor Token 구조 | JWT 페이로드에 위임자(`sub`)와 대리 실행자(`act`) 정보를 중첩하여 명시 | RFC 8693 Section 4.1 Token Structure |
| 감사 로깅 인프라 | 에이전트의 자율적 판단 근거(추론 로그)와 실제 실행된 API 호출 이력을 상관 연계 | Elastic, OpenTelemetry W3C TraceContext |

## Ⅳ. 전통적 사용자 IAM vs AI 에이전트 IAM 비교

| 비교 항목 | 전통적 사용자 IAM (Human IAM) | AI 에이전트 IAM (Agent IAM) |
|---|---|---|
| 인증 주체 | 인간 사용자 (임직원, 고객) | LLM 런타임, 마이크로서비스 에이전트 |
| 인증 수단 | ID/패스워드, FIDO2 패스키, SMS/OTP MFA | mTLS, 클라우드 워크로드 자격증명(IAM Role), SPIFFE |
| 인가 모델 | 역할 기반 접근 제어(RBAC), 정적 권한 그룹 | 속성 기반(ABAC), 태스크별 Just-In-Time(JIT) 동적 위임 |
| 권한 수명 | 수 시간 ~ 수 주일 세션 유지 | 수 분 단위 단기 토큰(Single-Task Ephemeral Token) |
| 위협 벡터 | 피싱, 자격증명 스터핑, 세션 하이재킹 | 프롬프트 인젝션, Confused Deputy, 과도한 권한 대행 |
| 의사결정 속도 | 인간의 클릭 및 인터랙션 기준 (초~분) | 머신 간 자율 연속 호출 (초당 수십~수백 건) |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 다단계 에이전트 체인(Multi-Agent Chain) 호출 시 중간 에이전트에서 원 사용자 신원(sub) 정보 누락 | RFC 8693 표준의 중첩된 Actor Claim(`act: {sub: "Agent-B", act: {sub: "Agent-A"}}`) 체인을 강제하여 종단 리소스까지 원 사용자 식별자 보존 |
| 간접 프롬프트 인젝션으로 인해 에이전트가 위임받은 정상 권한을 악용하여 민감 데이터를 유출하는 Confused Deputy 취약점 | API 게이트웨이 레벨에서 에이전트의 Egress 전송 목적지 도메인을 엄격히 화이트리스팅하고, 중요 데이터 다운로드 시 사용자 직접 재인증(Step-Up Re-auth) 강제 |
| 에이전트 환경에 장기 API Secret이 하드코딩되거나 메모리에 노출되어 컨테이너 탈취 시 전사 침해로 확산 | HashiCorp Vault와 연동하여 1회용 동적 시크릿을 주입하고, 클라우드 환경에서는 IAM Instance Role 및 OIDC 연동을 통한 무키(Keyless) 인증 적용 |
| 대규모 멀티 에이전트 구동 시 잦은 토큰 교환 및 OPA 정책 검증으로 인한 API 레이턴시 병목 현상 | PEP 계층에 로컬 인메모리 정책 캐시를 적용하고, JWT 서명 검증을 분산 게이트웨이 노드에서 비동기 가속 처리 |

## Ⅵ. 제언

```text
[ AI 에이전트 IAM 구현 3대 핵심 거버넌스 ]

+-------------------------+      +-------------------------+      +-------------------------+
|     무키(Keyless) 신원  | ---> |   미세단위 동적 인가    | ---> |     종단 간 책임 추적   |
| (SPIFFE/mTLS 기반 증명) |      | (RFC 8693 + OPA ABAC)   |      | (원사용자-에이전트 감사)|
+-------------------------+      +-------------------------+      +-------------------------+
```

| 영역 | 엔지니어링 실무 구현 과제 | 비즈니스 기대 가치 |
|---|---|---|
| 신원 인프라 | 에이전트 컨테이너마다 SPIFFE ID 발급 및 단기 X.509 인증서 기반 mTLS 상호 인증 | 고정 자격증명 누출 위험 원천 제거 |
| 인가 거버넌스 | 도구(Tool) 호출 시마다 OPA 정책 엔진을 통한 파라미터 유효성 검사 및 JIT 스코핑 | 프롬프트 인젝션 침해 시에도 파괴적 조치 원천 차단 |
| 규제 및 감사 | EU AI Act 및 전자금융감독규정에 부합하는 원 사용자-에이전트 이중 감사 증적 확보 | AI 자율 거래 및 판단에 대한 법적 부인방지 달성 |

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 (비인간 신원 보안 및 AI 에이전트 거버넌스)
- IETF RFC 8693, OAuth 2.0 Token Exchange
- OWASP Top 10 for LLM Applications (LLM06: Excessive Agency)
- SPIFFE/SPIRE Workload Identity Standards

## 연결 토픽

- 비인간 신원(NHI)
- 제로 트러스트(Zero Trust)
- AI SOC 에이전트
- AI 레드티밍
