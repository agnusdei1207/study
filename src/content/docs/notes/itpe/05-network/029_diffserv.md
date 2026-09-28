---
sidebar:
  order: 29
  label: "029. DiffServ"
  badge:
    text: "서브"
    variant: note
title: "DiffServ"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 29
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "서브"
  question_no: "029"
---

## 지식 로드맵 내 현재 위치

지식 위치: 네트워크 → 서비스 품질 제어 → **DiffServ**

## 30초 인출

- 본질: **DiffServ(Differentiated Services)** : 트래픽 집합에 차등 전달 동작을 적용하는 IP QoS 구조
- 메커니즘: 경계에서 트래픽 분류·표시·조절 → DSCP로 PHB 선택 → 도메인 내부에서 집합 단위로 전달
- 통찰: IntServ의 플로우별 상태 유지에 따른 확장성 붕괴를 극복하기 위해 패킷 헤더의 DSCP(6비트) 필드로 트래픽을 소수의 서비스 클래스로 집약 분류하고 코어 라우터는 단순 홉별 동작(PHB)만 수행하는 확장형 QoS 프레임워크임.

<details>
<summary>핵심 용어</summary>

- **DiffServ(Differentiated Services)** : 집합 단위 차등 서비스 제공을 위한 IP 네트워크 구조
- **DSCP(Differentiated Services Code Point)** : IPv4·IPv6 DS 필드의 6비트 코드점으로 PHB 선택
- **PHB(Per-Hop Behavior)** : 노드가 특정 트래픽 집합에 제공하는 외부 관측 가능한 홉 단위 전달 동작
- **DS 도메인(Differentiated Services Domain)** : 공통 서비스 정책·PHB를 운영하는 관리 범위
- **트래픽 조절(Traffic Conditioning)** : 트래픽 프로파일에 따른 측정·마킹·폴리싱·셰이핑 기능
- **EF(Expedited Forwarding)** : 낮은 손실·지연·지터 서비스의 구성 요소가 되는 PHB
- **AF(Assured Forwarding)** : 트래픽 클래스와 폐기 우선순위를 구분하는 PHB 그룹
- **BE(Best Effort)** : 별도 차등 서비스 처리가 선택되지 않은 트래픽의 기본 전달 동작
- **ECN(Explicit Congestion Notification)** : IP DS 필드의 하위 2비트로 혼잡을 알리는 방식

</details>

---

## 2~4교시 예상문제 (25점)

> IP 네트워크 QoS 보장 기술인 DiffServ(Differentiated Services)의 개념, 네트워크 구조(경계 라우터 vs 코어 라우터), DSCP 필드 구조, 주요 PHB(Per-Hop Behavior) 유형 및 IntServ와의 장단점을 비교 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. DiffServ의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | IP 패킷 헤더의 DS 필드(IPv4 ToS, IPv6 Traffic Class) 내 6비트 DSCP 값을 기반으로 트래픽을 서비스 등급별로 분류(Class-based)하고 라우터마다 정의된 홉별 동작(PHB)을 적용하는 확장형 QoS 아키텍처 |
| 목적 | 개별 플로우 상태 유지 없이 백본 라우터의 포워딩 속도 보존, 대규모 엔터프라이즈 및 인터넷 백본망의 차등화된 서비스 품질 제공 |

## Ⅱ. DiffServ의 특징

| 특징 | 상세 내용 |
|---|---|
| 상태 비보존(Stateless)| 코어 라우터가 수백만 개 개별 플로우의 연결 상태를 기억하지 않아 무제한에 가까운 확장성 제공 |
| 역할 분담 구조 | 경계 라우터(Edge)는 트래픽 분류/마킹/폴리싱을 수행하고, 코어 라우터(Core)는 단순 큐잉/스케줄링만 수행 |
| 6비트 DSCP 매핑 | 기존 8비트 ToS 필드 중 상위 6비트를 DSCP로 재정의하여 총 64개(2^6)의 세부 서비스 클래스 정의 |
| 집약 기반 서비스 | 음성, 영상, 업무 데이터 등 다양한 트래픽을 EF, AF, BE 등 소수의 대표 클래스로 번들링 처리 |

## Ⅲ. DiffServ의 체계·프로세스

**DiffServ 도메인 구조 및 패킷 처리 파이프라인**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ DiffServ 도메인 아키텍처 ]                    │
│                                                                        │
│ Ingress Packet ──► [ DiffServ 경계 라우터 (Edge Router) ]              │
│                           │                                            │
│            ┌──────────────┴──────────────┐                             │
│            ▼                             ▼                             │
│   [ 1. Classifier (분류기) ] ──► [ 2. Meter (트래픽 측정) ]            │
│   (5-Tuple 기반 패킷 검사)      (토큰 버킷 기반 계약 대역폭 준수 확인)│
│                                          │                             │
│            ┌─────────────────────────────┴────────┐                    │
│            ▼                                      ▼                    │
│   [ 3. Marker (마킹기) ]                 [ 4. Dropper / Shaper ]       │
│   (DSCP 비트 세팅: EF, AF, BE)          (계약 초과 패킷 폐기 또는 지연)│
│            │                                                           │
│            ▼ (DSCP가 마킹된 패킷 진입)                                 │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ [ DiffServ 코어 라우터 (Core Router) ]                         │   │
│   │   - 플로우별 상태 없음 (No Per-flow State)                      │   │
│   │   - 오직 DSCP 값만 읽고 해당 큐로 전달 (PHB 스케줄링)           │   │
│   │   - EF (Strict PQ), AF (CBWFQ), BE (FIFO/WRED)                 │   │
│   └────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

| 구성요소 | 핵심 역할 | 주요 동작 내용 |
|---|---|---|
| **Classifier (분류기)** | 트래픽 세분화 | BA(Behavior Aggregate, DSCP값만 확인) 또는 MF(Multi-Field, 5-Tuple 확인) 분류 |
| **Meter (측정기)** | 대역폭 준수 평가 | 수신 트래픽을 srTCM/trTCM(Two Rate Three Color Marker) 알고리즘으로 측정 |
| **Marker (마커)** | 패킷 헤더 갱신 | 측정 결과에 따라 IP 헤더의 DS 필드에 해당 DSCP 값을 기록 |
| **Shaper / Dropper**| 트래픽 정형/폐기 | SLA 계약 프로파일을 초과한 트래픽을 버퍼링(Shaping)하거나 즉각 드롭(Policing) |

## Ⅳ. DiffServ의 종류·비교

| 비교 항목 | IntServ (통합 서비스) | DiffServ (차등 서비스) |
|---|---|---|
| **서비스 제어 단위** | 개별 마이크로 플로우 단위 (Flow-based) | 클래스 집약 단위 (Class-based) |
| **자원 예약 프로토콜**| RSVP 명시적 시그널링 필수 | 사전 SLA 계약 및 DSCP 태깅 (시그널링 없음) |
| **라우터 상태 유지** | 전 경로 라우터가 플로우 상태 유지 (Stateful)| 코어 라우터 상태 유지 없음 (Stateless) |
| **네트워크 확장성** | 매우 낮음 (코어망 상태 폭증) | **매우 높음 (글로벌 백본망 적용 표준)** |
| **QoS 보장 수준** | 절대적 경성(Hard) QoS 보장 | 상대적 연성(Soft) QoS (혼잡 시 품질 저하 가능)|
| **주요 적용 위치** | 소규모 엔터프라이즈, 가입자 액세스망 | 글로벌 통신사 백본망, 대규모 멀티캠퍼스 |

## Ⅴ. DiffServ의 한계와 방안

| 한계 | 방안 |
|---|---|
| 사전 대역폭 예약이 없어 네트워크 전체가 심각한 과부하에 도달할 경우 최상위 EF 클래스조차 지터 및 패킷 손실 발생 | 경계 라우터에서 토큰 버킷 기반의 엄격한 인그레스 수락 제어(Admission Control) 및 WRED 임계치 연동 |
| 단일 ISP 도메인을 벗어나 타 통신사 망으로 전달될 때 이종 사업자 간 DSCP 매핑 불일치로 Best Effort로 초기화(DSCP Bleaching) | 통신사 간 NNI(Network-to-Network Interface) 연동 시 SLA 기반 DSCP 상호 매핑 표준 협약 및 MPLS VPN 연계 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
엔터프라이즈 IP 텔레포니(VoIP) 및 화상회의 연동 시, 음성 페이로드는 최고 우선순위인 `EF (DSCP 46, 101110b)`를 부여하고, 음성 호 제어 시그널링(SIP)은 `CS3 (DSCP 24)` 또는 `AF31 (DSCP 26)`로 분리 마킹하여 음성 끊김 현상을 완벽 방지.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ DiffServ DS 필드(6비트 DSCP + 2비트 ECN) 상세 비트 구조 ]           │
│                                                                        │
│   0     1     2     3     4     5     6     7                          │
│  ┌───────────────────────────────┬─────────┐                           │
│  │ DSCP (Differentiated Services)│ ECN     │                           │
│  │ Class Selector / Drop Precedence│ ECT, CE │                         │
│  └───────────────────────────────┴─────────┘                           │
│                                                                        │
│   [ AF(Assured Forwarding) 클래스 세부 십진수 값 매핑 ]                 │
│   Class 1 (Bulk)   : AF11 (28), AF12 (36), AF13 (44)                   │
│   Class 2 (Trans)  : AF21 (48), AF22 (56), AF23 (64)                   │
│   Class 3 (CallSig): AF31 (72), AF32 (80), AF33 (88)                   │
│   Class 4 (Video)  : AF41 (96), AF42 (104), AF43 (112)                 │
│   * 뒤자리 숫자가 클수록 혼잡 시 드롭 확률(Drop Precedence)이 높음     │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| PHB 유형 | 이진 코드 | 권장 스케줄러 | 보장 서비스 수준 | 대표 트래픽 |
|---|---|---|---|---|
| **EF (Expedited Forwarding)** | 101110 (46) | Strict Priority (PQ) | 최소 지연, 최소 지터, 무손실 보장 | 실시간 음성(VoIP) |
| **AF (Assured Forwarding)** | 12개 가변 코드 | CBWFQ + WRED | 클래스별 대역폭 및 드롭 차등화 | 화상회의, ERP 데이터 |
| **CS (Class Selector)** | xxx000 (ToS 호환) | 일반 큐잉 | 레거시 IP ToS 우선순위와 1:1 호환 | 네트워크 제어(OSPF, BGP) |
| **BE (Best Effort)** | 000000 (0) | FIFO | 어떠한 보장도 없는 최선형 전송 | 일반 웹 서핑, 파일 다운로드 |

## 출제 이력과 검증 출처

- IETF RFC 2474: Definition of the Differentiated Services Field (DS Field) in the IPv4 and IPv6 Headers
- IETF RFC 2475: An Architecture for Differentiated Services
- IETF RFC 2597: Assured Forwarding PHB Group

## 연결 토픽

- 상위 토픽: [032 QoS](./032_qos.md)
- 연관 토픽: [030 IntServ](./030_intserv.md), [008 WFQ](./008_wfq.md)
