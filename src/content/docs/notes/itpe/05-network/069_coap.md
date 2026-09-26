---
title: "CoAP(Constrained Application Protocol)"
author: "Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-network"]
sidebar:
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

네트워크 → 제약 장치 웹 통신 → CoAP

## 30초 인출

- 본질: **CoAP(Constrained Application Protocol)** 는 제약된 장치에서 웹 자원을 가볍게 요청·응답하는 응용 프로토콜
- 메커니즘: 간결한 이진 메시지에 REST 메서드·자원 경로를 담고, 메시지 유형으로 확인·재전송 동작을 구분

<details>
<summary>핵심 용어</summary>

- **CoAP(Constrained Application Protocol):** 제약된 노드·네트워크에 맞춰 웹 자원 요청·응답을 제공하는 응용 프로토콜
- **CON(Confirmable):** 응답 확인과 재전송 처리가 필요한 CoAP 메시지 유형
- **NON(Non-confirmable):** 확인 응답 없이 전송하는 CoAP 메시지 유형
- **ACK(Acknowledgement):** 수신한 CON 메시지를 확인하는 CoAP 메시지 유형
- **RST(Reset):** 처리할 수 없거나 연결 맥락이 없는 메시지를 알리는 CoAP 메시지 유형
- **Observe:** 자원 상태 변경을 클라이언트에 통지하는 CoAP 확장 옵션
- **Block-wise Transfer:** 큰 본문을 여러 블록으로 나눠 전송하는 CoAP 확장

</details>

---

## 1교시 예상문제 (10점)

> CoAP의 개념과 메시지 구조·유형을 설명하시오. (예상)

---

## 1교시 10점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **CoAP(Constrained Application Protocol)** 는 제약된 환경에서 웹 자원 요청·응답을 제공하는 경량 응용 프로토콜 |
| 목적 | 제한된 처리·전송 자원으로 기기 자원 접근과 상태 교환 지원 |

## Ⅱ. 메시지 구조와 유형

```text
CoAP 메시지
  ├─ 4바이트 고정 헤더: 버전·유형·토큰 길이·코드·메시지 ID
  ├─ 선택 항목: 토큰·옵션
  └─ 선택 항목: 페이로드

유형: CON(확인) · NON(비확인) · ACK(확인 응답) · RST(초기화)
```

| 메시지 유형 | 동작 |
|---|---|
| **CON(Confirmable)** | 확인 응답이 필요한 메시지 |
| **NON(Non-confirmable)** | 확인 없이 보내는 메시지 |
| **ACK(Acknowledgement)** | CON 수신 확인 또는 응답 전달 |
| **RST(Reset)** | 수신 메시지를 처리할 수 없음을 통지 |

제언: 중요한 제어 요청과 주기적 센서 보고를 메시지 확인 요구에 따라 구분

---

## 2~4교시 예상문제 (25점)

> CoAP의 메시지 구조와 요청·응답 및 확인 동작을 설명하고, 제약 장치 적용 시 신뢰성·보안·대용량 전송 고려사항을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **CoAP(Constrained Application Protocol)** 는 제약된 환경에서 웹 자원 요청·응답을 제공하는 경량 응용 프로토콜 |
| 목적 | 제한된 처리·전송 자원으로 기기 자원 접근과 상태 교환 지원 |

## Ⅱ. 계층·메시지 구조

```text
응용 자원·REST 요청/응답
          │ CoAP 코드·옵션·페이로드
CoAP 메시지 전송·확인 유형
          │ 기본 전송 매핑
UDP/IP 네트워크
```

| 필드 | 기능 |
|---|---|
| 고정 헤더 | 버전·유형·토큰 길이·코드·메시지 ID |
| 토큰 | 요청과 응답의 대응 관계 표시 |
| 옵션 | URI 경로·질의·확장 기능 등 추가 정보 |
| 페이로드 | 자원 표현 또는 요청 데이터 |

## Ⅲ. 요청·응답과 확인 동작

```text
클라이언트 ── CON 요청 ──▶ 서버
클라이언트 ◀── ACK + 응답 ── 서버    (즉시 처리: Piggyback)

클라이언트 ── CON 요청 ──▶ 서버
클라이언트 ◀── 빈 ACK ──── 서버
클라이언트 ◀── 별도 응답 ── 서버    (지연 처리: Separate)
```

| 동작 | 의미 |
|---|---|
| Piggyback 응답 | CON 요청의 ACK에 처리 응답을 함께 담음 |
| Separate 응답 | 먼저 빈 ACK로 수신을 확인하고 나중에 별도 응답 전송 |
| NON 메시지 | 확인 교환 없이 전송하므로 중요 동작에는 적절한 응용 수준 처리 필요 |

## Ⅳ. 제약 환경 확장과 운영 고려

| 요구 | CoAP 기능·고려사항 |
|---|---|
| 상태 변경 통지 | Observe 옵션으로 자원 변경 구독과 통지 지원 |
| 큰 본문 전송 | Block-wise Transfer로 본문을 여러 블록으로 분할 |
| 메시지 신뢰성 | CON 재전송과 중복 처리, 타임아웃 정책 점검 |
| 기밀성·인증 | 전송 보안과 단말 자격 증명 등 보호 대책 적용 |

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 무선 품질이 낮은 환경에서 큰 본문·잦은 확인 교환이 전력과 채널 자원을 소모 | 제어 중요도·본문 크기·단말 수면 정책에 맞춰 CON/NON과 블록 전송을 선택하고, 인증·암호화는 장치 자원 한도와 함께 검증 |

## 출제 이력과 검증 출처

- 제108회 1교시 관련 문항은 공식 문제지 원문을 확보하지 못해 회차·문구를 검증하지 못함.
- [RFC 7252 — The Constrained Application Protocol (CoAP)](https://www.rfc-editor.org/rfc/rfc7252)
- [RFC 7641 — Observing Resources in the Constrained Application Protocol](https://www.rfc-editor.org/rfc/rfc7641)
- [RFC 7959 — Block-Wise Transfers in the Constrained Application Protocol](https://www.rfc-editor.org/rfc/rfc7959)
