---
title: "VLAN(Virtual LAN)"
author: "GPT-6"
date: "2026-09-24T21:25:00+09:00"
tags:
  - "notes-network"
extra:
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 핵심 개념 → VLAN

## 30초 인출

- 본질: **VLAN (Virtual Local Area Network)** 은 하나의 브리지 네트워크를 논리적 브로드캐스트 도메인으로 나누는 기능
- 메커니즘: 포트 소속을 VLAN별로 나누고, 트렁크에서는 VLAN 태그로 프레임 소속을 식별

<details>
<summary>핵심 용어</summary>

- **VLAN (Virtual Local Area Network)**: 브리지 네트워크를 논리적 브로드캐스트 도메인으로 나누는 기능
- **Access port**: 단말 트래픽을 하나의 VLAN에 연결하는 스위치 포트
- **Trunk port**: 여러 VLAN 프레임을 하나의 링크로 전달하며 VLAN 식별 정보를 유지하는 포트
- **IEEE 802.1Q**: 브리지 네트워크에서 VLAN 식별을 포함한 태그 프레임 처리를 규정하는 표준
- **Inter-VLAN routing**: 서로 다른 IP 서브넷/VLAN 사이의 패킷을 라우터나 L3 스위치가 전달하는 기능

</details>

---

## 1교시 예상문제 (10점)

> VLAN의 개념과 핵심 구조 또는 동작을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 정의·목적

| 구분 | 핵심 |
|---|---|
| 정의 | **VLAN (Virtual Local Area Network)** 은 브리지 네트워크를 논리적 브로드캐스트 도메인으로 나누는 기능 |
| 목적 | 물리 배선과 별도로 단말의 L2 네트워크 소속을 구성 |

### Ⅱ. 핵심 구조와 작동

```text
VLAN 10                         VLAN 10
   │                               │
 access                           access
   │                               │
Switch A ═══════ 802.1Q trunk ═══ Switch B
   │                               │
 access                           access
   │                               │
VLAN 20                         VLAN 20
```

제언: VLAN 구획과 실제 접근 권한을 분리 설계하고 L3 정책까지 함께 검증

트렁크에서 VLAN별 프레임을 구분하는 태그 필드는 다음과 같이 구성.

| 필드 | 크기 | 역할 |
|---|---:|---|
| TPID | 16비트 | 802.1Q 태그임을 식별 |
| TCI | 16비트 | 우선순위·DEI·12비트 VID 포함 |

---

## 2~4교시 예상문제 (25점)

> VLAN의 구조와 동작을 설명하고, 주요 비교 또는 적용 시 문제와 대응책을 제시하시오. (예상)

---

## 2~4교시 25점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **VLAN (Virtual Local Area Network)** 은 브리지 네트워크를 논리적 브로드캐스트 도메인으로 나누는 기능 |
| 목적 | 물리 배선과 별도로 단말의 L2 네트워크 소속을 구성 |

### Ⅱ. 논리 분할과 트렁크

```text
VLAN 10                         VLAN 10
   │                               │
 access                           access
   │                               │
Switch A ═══════ 802.1Q trunk ═══ Switch B
   │                               │
 access                           access
   │                               │
VLAN 20                         VLAN 20
```

VLAN별 프레임 식별을 위해 트렁크 링크에서 VID를 포함한 태그 사용.

### Ⅲ. VLAN 구조와 식별

| 구분 | 핵심 |
|---|---|
| L2 범위 | 브로드캐스트 도메인은 VLAN 단위로 분리되며, 서로 다른 VLAN 간 통신에는 L3 전달 필요 |
| 태그 | 802.1Q 태그는 TPID 16비트와 TCI 16비트로 구성; TCI 안에 12비트 VID |
| VLAN ID | VID 0과 4095는 예약 값이며, 일반 VLAN 식별자 범위는 1–4094 |

### Ⅳ. 계층별 역할

| 구분 | VLAN | IP 서브넷 |
|---|---|---|
| 계층 | L2 브리지 도메인 | L3 주소·라우팅 도메인 |
| 기준 | 브리지 VLAN 소속 | IP prefix |
| 관계 | 설계 시 자주 대응시키지만 표준이 1:1 매핑을 강제하지 않음 | VLAN 경계를 넘는 통신은 L3 라우팅 정책에 따름 |

### Ⅴ. 구성 한계와 대응

| 한계 | 대응 |
|---|---|
| VLAN 분리는 자체적으로 단말 인증이나 L3 접근 통제를 보장하지 않음 | 포트 역할을 명시하고 불필요한 트렁크 협상을 끄며, VLAN 간 방화벽·라우팅 정책 적용 |
| 태그·native VLAN 설정 불일치로 우회·도청 위험 | trunk allowed VLAN과 native VLAN을 양 끝에서 일치시키고, 비사용 포트를 비활성화 |

### Ⅵ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 논리 분할만으로 보안 경계가 완성되지는 않음 | VLAN은 L2 구획에 사용하고, 신뢰 경계·사용자 인증·세분화 정책은 별도 L3/L4 통제로 구성 |

## 출제 이력과 검증 출처

- 제120회 1교시: “VLAN(Virtual LAN)의 개념, 필요성, 분류 방식 및 IEEE 802.1Q 프레임 태깅 구조를 설명하시오.”
- [IEEE 802.1Q-2022, Bridges and Bridged Networks](https://standards.ieee.org/ieee/802.1Q/10323/)
