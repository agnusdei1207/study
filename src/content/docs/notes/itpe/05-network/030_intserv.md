---
sidebar:
  order: 30
  label: "030. IntServ"
  badge:
    text: "서브"
    variant: note
title: "IntServ"
author: "Codex"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 30
extra:
  model: "GPT-6"
  keyword_grade: "서브"
  question_no: "030"
---

## 지식 로드맵 내 현재 위치

지식 위치: 네트워크 → 서비스 품질 제어 → **IntServ**

## 30초 인출

- 본질: **IntServ(Integrated Services)** : 흐름별 자원 요청과 상태를 이용해 IP 네트워크에서 통합 서비스를 제공하는 QoS 모델
- 메커니즘: 송신자 **PATH** 전달 → 수신자 **RESV** 자원 요청 → 각 라우터가 수락 제어·상태 관리 → 예약된 흐름에 서비스 적용

<details>
<summary>핵심 용어</summary>

- **IntServ(Integrated Services)** : IP 네트워크에서 흐름별 자원 상태와 서비스 모델을 관리하는 QoS 구조
- **RSVP(Resource ReSerVation Protocol)** : 수신자가 자원 예약을 요청하고 라우터가 경로별 상태를 관리하도록 돕는 시그널링 프로토콜
- **PATH 메시지(PATH Message)** : 송신자가 트래픽 특성과 경로 상태 정보를 수신자 방향으로 전달하는 RSVP 메시지
- **RESV 메시지(RESV Message)** : 수신자가 선택한 서비스·자원 요청을 송신자 방향으로 전달하는 RSVP 메시지
- **수락 제어(Admission Control)** : 새 요청이 정책·자원 조건에 맞게 수용 가능한지 판단하는 기능
- **소프트 상태(Soft State)** : 주기적 갱신이 없으면 상태가 만료·해제되는 관리 방식
- **Guaranteed Service(보장 서비스)** : 규격된 트래픽과 자원 관리 조건에서 지연 상한 등 서비스 특성을 제공하는 모델
- **Controlled-Load Service(제어 부하 서비스)** : 혼잡이 적은 네트워크에 가까운 서비스 특성을 목표로 하는 모델

</details>

---

## 1교시 예상문제 (10점)

> IntServ의 개념과 RSVP 자원 예약 절차를 설명하시오. (예상·10점)

---

## 1교시 10점 답안

### Ⅰ. IntServ의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **IntServ** : IP 네트워크에서 흐름별 자원 상태와 서비스 모델을 관리하는 QoS 구조 |
| 목적 | 흐름별 요구에 따라 네트워크 자원·서비스 수락을 관리 |

### Ⅱ. RSVP 예약 절차

```text
송신자
  ↓ PATH·트래픽 특성
경로상 라우터 (경로 기록)
  ↓ PATH 전달
수신자
  ↑ RESV·자원 요청
경로상 라우터 (수락 제어·상태 설정)
  ↑ RESV 전달
송신자
```

- 제언: 트래픽 특성·요청 서비스·경로 자원을 함께 검토하는 흐름별 QoS 설계.

---

## 2~4교시 예상문제 (25점)

> IntServ의 RSVP 예약 구조와 서비스 모델을 설명하고, 흐름별 상태 관리의 한계 및 적용 방안을 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

### Ⅰ. IntServ의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **IntServ** : IP 네트워크에서 흐름별 자원 상태와 서비스 모델을 관리하는 QoS 구조 |
| 목적 | 흐름별 요구에 따라 네트워크 자원·서비스 수락을 관리 |

### Ⅱ. RSVP 예약 절차

```text
송신자
  ↓ PATH·트래픽 특성
경로상 라우터 (경로 기록)
  ↓ PATH 전달
수신자
  ↑ RESV·자원 요청
경로상 라우터 (수락 제어·상태 설정)
  ↑ RESV 전달
송신자
```

라우터는 RESV 요청을 처리하며 서비스·자원 정책에 따라 수락하거나 거절. 상태는 주기적 RSVP 갱신을 통해 유지되며 갱신이 사라지면 만료 가능.

### Ⅲ. 주요 기능

| 기능 | 역할 |
|---|---|
| 자원 요청 | 트래픽 특성과 원하는 서비스 요구 전달 |
| 수락 제어 | 정책·자원 가용성을 기준으로 새 흐름 판단 |
| 분류·스케줄링 | 흐름별 패킷을 구분하고 요청 서비스에 맞게 처리 |
| 소프트 상태 | 갱신에 따라 상태를 유지하고 만료 시 정리 |

### Ⅳ. 서비스 모델

| 서비스 | 목표 특성 | 조건·해석 |
|---|---|---|
| Guaranteed Service | 트래픽·자원 조건 아래 지연 상한 등 서비스 제공 | 트래픽 명세와 네트워크 자원 관리 필요 |
| Controlled-Load Service | 혼잡하지 않은 환경에 가까운 서비스 | 절대적 무손실·무지연 보장과 다름 |

### Ⅴ. IntServ와 DiffServ 비교

| 관점 | IntServ | DiffServ |
|---|---|---|
| 처리 단위 | 흐름별 상태·요청 | 트래픽 집합·클래스 |
| 주요 방식 | RSVP 시그널링과 수락 제어 | DSCP와 PHB 기반 전달 |
| 자원 관리 | 경로의 노드별 상태와 정책 | 도메인 경계 조절·홉별 자원 배분 |
| 고려점 | 흐름 수 증가에 따른 상태·신호 부하 | 클래스별 품질이 자원 구성·정책에 의존 |

### Ⅵ. 한계와 대응

| 한계 | 대응 |
|---|---|
| 흐름 수 증가에 따른 상태·갱신 메시지 부담 | 적용 도메인의 규모·경로 자원·상태 처리 능력 평가 |
| 경로 변경·라우터 미지원 시 예약 연속성 저하 | RSVP 지원·경로 변화·대체 경로 동작 시험 |
| 자원 요청을 서비스 보장으로 과대 해석 | 트래픽 명세·수락 제어·스케줄러·경로 전체의 조건 점검 |

### Ⅶ. 기술사적 제언

| 우선 적용 | 적용 기준 |
|---|---|
| 흐름별 자원 제어가 필요한 관리 도메인에 한정해 IntServ 검토 | 노드 지원·예약 규모·장애 시 동작을 검증하고 다른 구간과의 DiffServ 연계를 설계 |

---

## 출제 이력과 검증 출처

- 제125회 1교시: “인터넷 QoS 보장 기술인 IntServ와 DiffServ를 비교 설명하시오.”
- [RFC 2205: Resource ReSerVation Protocol (RSVP)](https://www.rfc-editor.org/rfc/rfc2205)
- [RFC 2212: Specification of Guaranteed Quality of Service](https://www.rfc-editor.org/rfc/rfc2212)
- [RFC 2211: Specification of the Controlled-Load Network Element Service](https://www.rfc-editor.org/rfc/rfc2211)
- [RFC 2210: RSVP with Integrated Services](https://www.rfc-editor.org/rfc/rfc2210)

## 연결 토픽

- 연관 토픽: [DiffServ](./029_diffserv.md), [QoS](./032_qos.md)
