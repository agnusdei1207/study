---
title: "FIDO 인증과 FIDO2"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "129. FIDO 인증과 FIDO2"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 신원·인증 → 공개키 기반 사용자 인증 → **FIDO2**

## 30초 인출

- **본질:** 공유 비밀(비밀번호)을 서버에 전송하지 않고, 단말의 보안 영역(TPM/Secure Enclave)에서 비대칭 키쌍을 생성·서명하여 오리진 바인딩 기반 피싱 저항성을 제공하는 개방형 인증 표준
- **메커니즘:** 서버 난수 도전값(Challenge) 발송 → 로컬 생체 인증(지문/Face ID) → 개인키로 Challenge + ClientDataJSON(오리진) 서명 → 서버 공개키 검증
- **통찰:** 클라우드 동기화형 패스키의 공급자 계정 침해 위험은 고위험 트랜잭션 시 기기 바운드 하드웨어 키 강제로 보완하고 세션 토큰 탈취는 DPoP 결속으로 방어 필수

<details>
<summary>핵심 용어</summary>

- **FIDO2** : 웹 표준 API(WebAuthn)와 외부 인증기 통신 프로토콜(CTAP)을 통합한 차세대 무암호 인증 표준.
- **WebAuthn** : 웹 브라우저가 자바스크립트를 통해 공개키 자격증명을 생성·검증할 수 있도록 지원하는 W3C 권고안.
- **CTAP (CTAP1/CTAP2)** : 클라이언트(OS/브라우저)와 외부 보안키(USB, BLE, NFC 토큰) 간의 통신 프로토콜.
- **Passkey (패스키)** : FIDO 자격증명을 클라우드 키체인 간 종단간 암호화(E2EE)로 동기화하여 멀티 디바이스 사용성을 극대화한 FIDO2 자격증명.

</details>

## 2~4교시 예상문제 (25점)

> FIDO 1.0(UAF, U2F)과 FIDO2의 아키텍처 차이점을 비교하고, WebAuthn 기반의 등록 및 인증 프로세스, 피싱 저항성(Phishing-resistant) 원리와 엔터프라이즈 환경 도입 시 보안 한계 및 극복 방안을 설명하시오. (예상·25점)

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 서버에 공유 비밀번호를 보관하지 않고, 사용자 기기 내부 보안 칩에서 생성된 공개키 암호화(Public Key Cryptography)와 로컬 생체 인식을 결합한 피싱 저항성 차세대 사용자 인증 표준 |
| 목적 | 대규모 비밀번호 유출(Credential Stuffing), 키로깅, 중간자 피싱 공격(AitM)을 원천 차단하고 완전한 패스워드리스(Passwordless) 환경 실현 |

- W3C의 WebAuthn과 FIDO Alliance의 CTAP 프로토콜 결합으로 플러그인(ActiveX, exe) 없이 모든 최신 웹 브라우저와 모바일 OS에서 네이티브로 동작

## Ⅱ. FIDO2의 핵심 기술적 특성

| 특성 항목 | 세부 내용 및 기술적 의미 | 엔지니어링 구현 가치 |
|---|---|---|
| 피싱 저항성 (Phishing Resistance) | 브라우저가 접속한 웹사이트 도메인(RP ID/Origin)을 서명 데이터에 암호학적으로 강제 결속 | 피싱 사칭 사이트에서 정당한 인증 토큰 생성 원천 불가 |
| 개인정보 보호 (Privacy by Design) | 사용자 생체 정보(지문, 홍채)는 단말 Secure Enclave 내부에서만 처리되고 서버로 미전송 | 생체 템플릿의 중앙 서버 유출 및 대량 도난 위험 배제 |
| 서비스별 키쌍 분리 | 등록하는 웹 서비스(RP)마다 서로 다른 독립된 공개키/개인키 쌍을 생성하여 매핑 | 특정 사이트의 공개키 DB가 유출되어도 타 서비스 추적 불가 |
| 플랫폼 인증기 네이티브 지원 | 스마트폰, 노트북에 내장된 생체 인식(Windows Hello, Touch ID)을 기본 인증기로 활용 | 외장 하드웨어 토큰 구매 비용 절감 및 뛰어난 사용자 경험 |

- 기기 소유(Possession)와 생체 특성(Inherence)을 로컬에서 융합하는 강력한 다요소 인증(MFA) 특성 보유

## Ⅲ. WebAuthn 등록 및 인증 엔지니어링 프로세스

```text
[WebAuthn 기반 FIDO2 등록(Registration) 및 인증(Authentication) 흐름]

  [Web Browser / OS]               [Relying Party (RP) Server]          [Authenticator (TPM/SE)]
          │                                      │                                  │
          │ 1. 등록/인증 옵션 요청 (GET)           │                                  │
          ├─────────────────────────────────────>│                                  │
          │ 2. Challenge + RP ID 반환            │                                  │
          │<─────────────────────────────────────┤                                  │
          │                                      │                                  │
          │ 3. navigator.credentials.create() / get()                               │
          ├────────────────────────────────────────────────────────────────────────>│
          │                                      │                                  │ 사용자 생체인증 확인
          │                                      │                                  │ (지문/얼굴 인식 성공)
          │                                      │                                  │ 개인키로 Challenge 서명
          │ 4. 서명된 Attestation / Assertion 객체 반환                             │
          │<────────────────────────────────────────────────────────────────────────┤
          │                                      │                                  │
          │ 5. 검증 요청 (POST ClientDataJSON + Signature)                          │
          ├─────────────────────────────────────>│                                  │
          │                                      │ 6. Challenge 신선도 검증          │
          │                                      │    Origin/RP ID 일치 검증         │
          │                                      │    공개키로 전자서명 검증 완료   │
          │ 7. 최종 로그인 세션 발급             │                                  │
          │<─────────────────────────────────────┤                                  │
```

| 프로세스 단계 | 핵심 세부 동작 메커니즘 | 위협 통제 포인트 |
|---|---|---|
| 1. 챌린지 생성 | RP 서버가 암호학적으로 안전한 의사 난수 챌린지(Minimum 16B)와 RP ID를 클라이언트로 전송 | 재생 공격(Replay Attack) 방어 |
| 2. 사용자 확인 (UV) | 클라이언트 OS가 인증기를 호출하여 생체 인식(지문/안면) 또는 로컬 PIN 번호 확인 | 단말 도난 시 비인가자 서명 생성 차단 |
| 3. 오리진 바인딩 서명 | 브라우저가 현재 주소창의 완전한 도메인(Origin)을 `ClientDataJSON`에 포함 후 개인키 서명 | 중간자 피싱 도메인 사칭 무력화 |
| 4. 서버 검증 및 인가 | RP 서버가 등록된 공개키로 서명을 검증하고, 챌린지 일치 및 카운터(Sign Count) 증가 확인 | 복제된 인증기 탐지 및 최종 인증 승인 |

## Ⅳ. FIDO 표준군 발전 단계 비교

| 비교 항목 | FIDO 1.0 UAF (Universal Auth) | FIDO 1.0 U2F (2nd Factor) | FIDO2 (WebAuthn + CTAP) | 패스키 (Synced Passkey) |
|---|---|---|---|---|
| 주요 목적 | 비밀번호 없는 인증 (모바일 앱) | 기존 패스워드 대체 2차 인증 | 완전 무암호 웹/앱 표준 인증 | 다중 기기 자동 동기화 무암호 |
| 브라우저 지원 | 미지원 (전용 모바일 SDK 필수) | Chrome 등 일부 브라우저 지원 | W3C 웹 표준 (전 브라우저 내장) | iOS, Android, Windows 내장 |
| 사용 하드웨어 | 스마트폰 지문인식 전용 | USB/NFC 외장 전용 보안 토큰 | 내장(Hello/TouchID) + 외장키 | 클라우드 키체인 동기화 단말 |
| 통신 프로토콜 | UAF 전용 프로토콜 | U2F Raw Message Format | WebAuthn JS API + CTAP2 | WebAuthn + FIDO Credential Sync |
| 백업 및 복구 | 단말 변경 시 서비스별 재등록 | 분실 시 백업 보안키 필요 | 서비스별 수동 재등록 필요 | 클라우드 백업으로 자동 복구 |

## Ⅴ. FIDO2 도입 시 보안 한계와 엔지니어링 해결 방안

| 한계 | 방안 |
|---|---|
| 동기화형 패스키(Synced Passkey)가 Apple/Google 계정에 백업됨에 따라 빅테크 계정(ID/PW) 침해 시 전사 패스키 일괄 유출 위험 | 엔터프라이즈 환경에서는 기기 귀속형(Device-bound FIDO2 토큰)을 강제하고, WebAuthn 등록 시 Attestation Statement(FIPS 140-3 검증 증적)를 평가하여 비인가 클라우드 동기화 차단 |
| 로그인 단계가 강력한 피싱 저항성을 제공하더라도, 최초 FIDO2 등록(Enrollment)이나 단말 분실 후 복구 단계에서 취약한 SMS OTP 제공으로 우회 침해 | 계정 복구 및 신규 기기 등록 시 모바일 신분증, 신분증 OCR + 라이브니스(Liveness) 안면 검증 등 강화된 디지털 신원 확인(Identity Proofing) 프로세스 의무화 |
| FIDO2 인증 성공 후 발행된 세션 쿠키 또는 Bearer 토큰이 정보탈취형 악성코드(Infostealer)에 의해 메모리 덤프 탈취(Pass-the-Cookie) | RFC 9449 DPoP(Demonstrating Proof-of-Possession) 및 애플리케이션 레벨 토큰 바인딩(Token Binding)을 적용하여 세션 토큰을 클라이언트 비대칭키와 암호학적으로 결속 |
| 사내 폐쇄망 및 에어갭(Air-gapped) 환경에서 외부 FIDO MDS(Metadata Service) 서버 조회가 불가능하여 기기 인증서 유효성 검증 실패 | 사내 프라이빗 FIDO MDS 캐시 서버를 온프레미스에 구축하고 엔터프라이즈 전용 루트 CA 기반 기기 인증서(Attestation Root Certificate) 화이트리스트 운영 |

## Ⅵ. 피싱 저항성 제로 트러스트 인증 아키텍처 제언

```text
[FIDO2 패스키 기반 엔터프라이즈 제로 트러스트 인증 아키텍처]

  ┌─────────────────────────────────────────────────────────────┐
  │                 1. 인증기 계층 (Multi-Authenticator)        │
  │   - 일반 임직원: OS 내장 패스키 (Windows Hello / Touch ID)  │
  │   - 특권 관리자: FIPS 140-3 Level 3 외장 하드웨어 보안키    │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
  ┌──────────────────────────────┴──────────────────────────────┐
  │              2. 접근 제어 계층 (Conditional Access PDP)      │
  │   - Device Attestation (TPM PCR 무결성 상태 확인)           │
  │   - 위치, 시간, EDR 단말 보안 점수를 FIDO 서명과 결합 평가 │
  └──────────────────────────────┬──────────────────────────────┘
                                 │
  ┌──────────────────────────────┴──────────────────────────────┐
  │              3. 세션 보호 계층 (Cryptographic Binding)      │
  │   - DPoP 기반 비대칭키 증명 토큰 발급 (세션 탈취 무력화)   │
  │   - 지속적 세션 평가(CAEP)로 비정상 행위 감지 시 즉시 파기  │
  └─────────────────────────────────────────────────────────────┘
```

| 구축 영역 | 엔지니어링 세부 과제 | 관리 지표 |
|---|---|---|
| 인증 방식 전환 | 사내 포털 및 SaaS(M365 등) 대상 FIDO2 무암호 로그인 전면 적용 | 패스워드 기반 인증 비율 0%, 피싱 공격 성공률 0% |
| 토큰 보호 | API 게이트웨이 전 구간 DPoP(RFC 9449) 프로토콜 적용 | 세션 하이재킹 및 쿠키 탈취 악용 차단율 100% |
| 관리자 통제 | 코어 시스템 관리자에 대한 하드웨어 바운드 보안키 의무화 | 특권 계정 하드웨어 보안키 보급률 100% |

## 출제 이력과 검증 출처

- 제107·116·118회 정보관리기술사 기출 및 빈출: FIDO 인증 기술 및 WebAuthn 표준
- FIDO Alliance: FIDO2: Key Specifications and How They Intersect
- W3C Recommendation: Web Authentication: An API for accessing Public Key Credentials (WebAuthn Level 3)
- CISA: Implementing Phishing-Resistant MFA (Cybersecurity Advisory)
- IETF RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)
