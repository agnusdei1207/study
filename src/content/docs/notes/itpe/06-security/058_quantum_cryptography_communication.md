---
title: "양자암호통신(Quantum Cryptography Communication)"
author: "OpenAI"
date: "2026-09-24T22:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  model: "GPT-6"
  keyword_grade: "서브"
---

## 지식 로드맵 내 현재 위치

암호기술 → 양자 기술 기반 키 분배 → QKD 통신망과 암호응용

## 30초 인출

- **본질**: 양자암호통신은 QKD로 키를 생성·분배하고 키관리·암호응용과 연결하는 통신 보안 체계.
- **메커니즘**: 양자상태 교환 → 인증된 고전채널로 오류·도청 영향 확인 → 키 정제 → 암호장비에 키 제공.
- **핵심**: QKD는 키 분배 기술이며 데이터 암호화·인증·키관리를 대신하지 않음.

<details><summary>핵심 용어</summary>

- **양자암호통신**: QKD로 공유 키를 만들고 키관리·고전 암호응용과 연결하는 통신 체계.
- **QKD(Quantum Key Distribution)**: 양자상태 측정과 고전 통신 절차로 공유 키를 생성·합의하는 기술.
- **QKDN(Quantum Key Distribution Network)**: QKD 노드와 키 관리기능을 연결해 암호 응용에 키를 제공하는 네트워크.
- **QRNG(Quantum Random Number Generator)**: 양자 현상을 이용해 난수를 생성하는 장치·기능.
- **KMS(Key Management System)**: 암호키의 생성·배포·저장·폐기 정책을 관리하는 시스템.
- **PQC(Post-Quantum Cryptography)**: 양자컴퓨터 공격을 고려해 설계한 고전적 계산 기반 암호기술.
- **ITU-T(International Telecommunication Union Telecommunication Standardization Sector)**: 통신 분야 국제 표준을 개발하는 ITU 표준화 부문.
</details>

---

## 1교시 예상문제 (10점)

---

> 양자암호통신의 개념과 QKD 원리, 키관리·데이터 암호화와의 관계를 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **양자암호통신**은 QKD로 키를 생성·분배하고 키관리·암호응용과 연결하는 통신 보안 체계. |
| 목적 | 도청 영향을 확인하는 키 분배와 기존 데이터 암호화를 결합해 통신 기밀성을 지원. |

### Ⅱ. 키 생성·암호응용 연계

```text
송신 QKD 장비 ── 양자채널 상태 교환 ──→ 수신 QKD 장비
       └──── 인증된 고전채널: 기저·오류 확인 ────┘
                         ↓ 안전한 키 합의
                 키관리시스템(KMS)
                         ↓ 키 제공
              대칭키 암호장비 → 데이터 보호
```

양자채널과 인증된 고전채널은 역할이 다르며, 사용자 데이터는 별도 암호응용에서 처리.

제언: QKD 링크뿐 아니라 고전채널 인증·키관리·암호장비까지 하나의 신뢰경계로 설계.

---

## 2~4교시 예상문제 (25점)

---

> 양자암호통신의 원리와 구성요소, 기존 통신망과의 연동방안 및 보안상 한계를 설명하시오. (KPC 제128회 취지 반영)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **양자암호통신**은 QKD로 키를 생성·분배하고 키관리·암호응용과 연결하는 통신 보안 체계. |
| 목적 | 도청 영향을 확인하는 키 분배와 기존 데이터 암호화를 결합해 통신 기밀성을 지원. |

## Ⅱ. QKD 키 합의 원리

```text
① 양자상태 전송·측정
          ↓
② 인증된 고전채널에서 기저 정보 비교
          ↓
③ 일부 표본으로 오류 수준 추정
       ┌──┴──┐
   기준 초과   기준 충족
   키 폐기      오류 보정
                    ↓
             프라이버시 증폭
                    ↓
               합의된 키
```

보안 분석의 전제와 허용 오류기준을 만족할 때 키 재료를 확정하며, 실제 보안은 장비 구현·채널·인증에 따른 가정에도 좌우.

## Ⅲ. 네트워크 구성과 역할

| 구성요소 | 역할 | 주요 보호점 |
|---|---|---|
| QKD 장비·양자채널 | 양자상태 교환과 키 재료 생성 | 장비 무결성·물리 접근·구현 취약점 |
| 고전 제어채널 | 기저 협의·오류 보정 등 공개 절차 | 메시지 인증·무결성 |
| KMS | 키 수명주기·정책·응용별 공급 | 키 접근권한·감사·폐기 |
| 신뢰노드 | 링크 사이에서 키를 중계 | 노드·운영자 침해와 물리보안 |
| 암호 응용 | 공유 키로 실제 데이터 보호 | 키 인터페이스와 종단 보안 |

## Ⅳ. 기존망 연동과 보안 한계

| 기술·방식 | 키 보안 원리 | 연동 시 검토 |
|---|---|---|
| QKD | 양자상태 교환에 기반한 키 생성·합의 | 전용 장비·인증된 고전채널·신뢰노드 |
| PQC | 양자 공격을 고려한 고전 알고리즘 | 기존 프로토콜·인증서·암호제품의 전환 |
| 하이브리드 | 기존 암호와 PQC 또는 QKD 키를 함께 운용 | 상호운용·키관리·성능·전환·장애 시 정책 |

QKD는 사용자 데이터 암호화나 상대 인증을 자동 제공하지 않으며, NIST는 실제 QKD 구현과 프로토콜의 취약점·운영 조건을 별도로 검토하도록 설명.

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 키 생성만 도입해도 전체 통신이 안전해진다고 오해하기 쉬움. | 데이터 암호화·인증·키 수명주기·단말을 포함한 종단 위협모델을 세우고 제한 구간 실증 후 확대하는 방안. |

## 출제 이력과 검증 출처

- 기존 노트의 KPC 제128회 출제 취지를 보존한 예상 확장문항.
- [ITU-T X.1710: Security Framework for QKD Networks](https://www.itu.int/epublications/en/publication/itu-t-x-1710-2020-10-security-framework-for-quantum-key-distribution-networks/en) — QKDN 보안 프레임워크.
- [ITU-T Y.3800: Overview on Networks Supporting QKD](https://www.itu.int/epublications/publication/itu-t-y-3800-2019-10-overview-on-networks-supporting-quantum-key-distribution) — QKD 지원 네트워크 개요.
- [NIST: What Is Quantum Cryptography?](https://www.nist.gov/cybersecurity-and-privacy/what-quantum-cryptography) — QKD의 역할과 기술적 고려사항.
- [NISTIR 6977: Vulnerabilities in Quantum Key Distribution Protocols](https://www.nist.gov/publications/vulnerabilities-quantum-key-distribution-protocols) — 프로토콜별 공격 가능성 검토.
