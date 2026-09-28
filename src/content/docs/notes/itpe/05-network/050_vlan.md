---
title: "VLAN(Virtual LAN)"
author: "Antigravity"
date: "2026-09-24T21:25:00+09:00"
tags:
  - "notes-network"
sidebar:
  label: "050. VLAN(Virtual LAN)"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 데이터 통신 → **VLAN(Virtual LAN)**

## 30초 인출

- 본질: **VLAN (Virtual Local Area Network)** : 단일 물리적 L2 스위치 인프라를 논리적 브로드캐스트 도메인(Broadcast Domain)으로 격리하는 네트워크 가상화 기술
- 메커니즘: Access Port(단일 VLAN untagged)와 Trunk Port(다중 VLAN IEEE 802.1Q 태깅)로 트래픽을 분리하며, VLAN 간 통신은 Router-on-a-Stick 또는 L3 SVI(Switch Virtual Interface)를 통해 Inter-VLAN 라우팅 수행
- 통찰: 단순 논리 분할에 그치지 않고 DTP 협상 비활성화, Native VLAN 격리, Dynamic ARP Inspection(DAI) 등 L2 보안 제어와 결합해야 VLAN Hopping 및 MAC 플러딩을 원천 차단함.

<details>
<summary>핵심 용어</summary>

- **IEEE 802.1Q** : 이더넷 프레임의 헤더에 4바이트 VLAN 태그(TPID 16비트, TCI 16비트)를 삽입하는 국제 표준 트렁킹 프로토콜
- **Access Port** : 최종 단말(PC, 서버 등)과 연결되며 태그 없는(Untagged) 프레임만을 송수신하는 포트
- **Trunk Port** : 스위치 간 또는 스위치-라우터 간 다중 VLAN 트래픽을 전달하기 위해 802.1Q 태그를 부착하는 포트
- **Inter-VLAN Routing** : 서로 다른 VLAN(L2 도메인) 간의 패킷 전달을 위해 L3 라우팅을 수행하는 기법 (Router-on-a-Stick 또는 SVI)
- **VLAN Hopping** : 공격자가 허용되지 않은 다른 VLAN의 패킷에 무단 접근하기 위해 트렁크 협상을 사칭하거나 이중 태그를 주입하는 L2 보안 공격

</details>

---

## 2~4교시 예상문제 (25점)

> VLAN의 논리 분할 원리와 IEEE 802.1Q 트렁크 프레임 구조를 설명하고, L2 VLAN과 L3 IP 서브넷의 매핑 관계 및 운영 시 보안·성능 한계와 대응 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. VLAN의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 단일 물리적 L2 스위칭 인프라 내에서 포트, MAC, 프로토콜 기반으로 논리적 브로드캐스트 도메인을 분할하는 네트워크 가상화 기술 |
| 목적 | 브로드캐스트 트래픽 격리를 통한 대역폭 절약, 부서 간 보안 격리, 물리적 배선 변경 없는 유연한 망 구성 지원 |

## Ⅱ. VLAN의 특징 및 핵심 유형

| 분류 기준 | 특징 및 동작 방식 | 장단점 및 적용 환경 |
|---|---|---|
| **포트 기반 (Port-based)** | 스위치의 물리 포트 번호에 특정 VLAN ID를 정적으로 할당 | 설정 직관적, 가장 대중적 / 단말 이동 시 관리자가 포트 재설정 필요 |
| **MAC 기반 (MAC-based)** | 단말의 NIC MAC 주소를 인식하여 해당 VLAN 동적 매핑 | 단말이 다른 포트로 이동해도 VLAN 유지 / 초기 MAC 등록 및 관리 부하 |
| **프로토콜 기반 (Protocol-based)** | L3 프로토콜(IPv4, IPv6 등) 헤더 값 기반으로 VLAN 매핑 | 복기종 프로토콜 환경에 적합 / 스위치 프레임 분석 오버헤드 발생 |
| **서브넷 기반 (Subnet-based)** | 단말의 L3 IP 서브넷 주소를 기반으로 VLAN 자동 매핑 | IP 이동성 제공 / L3 정보 파싱에 따른 처리 지연 발생 |

## Ⅲ. VLAN 아키텍처 및 IEEE 802.1Q 프레임 구조

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ VLAN 아키텍처 및 트렁킹 ]                      │
│                                                                        │
│   [ VLAN 10 (인사팀) ]                        [ VLAN 20 (개발팀) ]     │
│          │ Access Port                               │ Access Port     │
│   ┌──────┴───────────────────────────────────────────┴──────┐          │
│   │                      Switch A                           │          │
│   │  (PVID: 10)                                 (PVID: 20)  │          │
│   └──────────────────────────┬──────────────────────────────┘          │
│                              │ Trunk Link (IEEE 802.1Q Tagged)         │
│                              │ [DA | SA | 802.1Q | EtherType | Data]   │
│   ┌──────────────────────────┴──────────────────────────────┐          │
│   │                      Switch B                           │          │
│   │  (PVID: 10)                                 (PVID: 20)  │          │
│   └──────┬───────────────────────────────────────────┬──────┘          │
│          │ Access Port                               │ Access Port     │
│   [ VLAN 10 (인사팀) ]                        [ VLAN 20 (개발팀) ]     │
└────────────────────────────────────────────────────────────────────────┘
```

| 필드 | 크기 | 상세 규격 및 역할 |
|---|---|---|
| **TPID (Tag Protocol Identifier)** | 16 bits | 802.1Q 프레임 식별자 (표준 고정값 `0x8100`) |
| **PCP (Priority Code Point)** | 3 bits | QoS 트래픽 우선순위 지정 (IEEE 802.1p, 8단계 CoS: 0~7) |
| **DEI (Drop Eligible Indicator)** | 1 bit | 네트워크 혼잡 발생 시 우선 폐기 가능 여부 표시 (구 CFI) |
| **VID (VLAN Identifier)** | 12 bits | 논리적 VLAN 식별자 (0 및 4095는 예약, 1~4094 가용) |

## Ⅳ. L2 VLAN vs L3 IP 서브넷(Subnet) 비교

| 비교 항목 | L2 VLAN (Virtual Local Area Network) | L3 IP 서브넷 (IP Subnetting) |
|---|---|---|
| **동작 계층** | 데이터링크 계층 (OSI Layer 2) | 네트워크 계층 (OSI Layer 3) |
| **식별 기준** | 12비트 VLAN ID (802.1Q 태그: 1 ~ 4094) | 32비트 IPv4 / 128비트 IPv6 네트워크 프리픽스 |
| **도메인 범위** | 물리 스위치 패브릭 내 논리 브로드캐스트 도메인 | 논리적 IP 주소 할당 및 전역 라우팅 도메인 |
| **포워딩 장비** | L2 이더넷 스위치 (MAC 테이블 기반 스위칭) | L3 라우터 / L3 스위치 (FIB 라우팅 테이블 기반) |
| **상호 매핑 관계** | 통상 1개 VLAN = 1개 IP 서브넷으로 1:1 권장 설계 | 서브넷 간 통신은 L3 라우팅 정책(ACL, 방화벽) 필수 경유 |

## Ⅴ. VLAN 운영 시의 한계와 방안

| 한계 | 방안 |
|---|---|
| 공격자가 DTP 협상 패킷을 사칭 발송하여 스위치 포트를 트렁크로 유도 후 전 VLAN 트래픽을 도청하는 Switch Spoofing 공격 취약 | 사용자 접속 포트는 `switchport mode access`로 고정하고, 트렁크 포트는 `switchport nonegotiate`를 설정하여 동적 트렁크 협상 원천 차단 |
| 공격자가 Native VLAN 태그를 외부에, 피해자 VLAN 태그를 내부에 이중 삽입하여 경계를 우회하는 Double Tagging 공격 발생 | 기본 VLAN 1을 사용하지 않고 비인가 전용 미사용 VLAN을 Native VLAN으로 격리하며, `vlan dot1q tag native` 명령으로 Native VLAN 태그 강제 집행 |
| PVST+ 구동 시 VLAN 개수만큼 Spanning-Tree 인스턴스 BPDU가 폭증하여 스위치 CPU 점유율 100% 도달 및 제어평면 마비 발생 | 다중 VLAN을 소수의 인스턴스로 그룹화하여 BPDU 오버헤드를 최소화하는 MSTP(IEEE 802.1s) 표준 프로토콜로 마이그레이션 수행 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
전사 VLAN 설계 시 업무별 브로드캐스트 도메인을 최소화하고, 모든 트렁크 포트에서 기본 전체 허용(`allow all`) 설정을 즉각 해제하여 실제 경유할 필수 VLAN ID만 화이트리스트(`switchport trunk allowed vlan`)로 명시 등록하며, L2 보안 엔진(DHCP Snooping, Dynamic ARP Inspection)을 연계 활성화함.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ Inter-VLAN 라우팅 구현 방식 비교 ]                  │
│                                                                        │
│   [방식 1: Router-on-a-Stick]         [방식 2: L3 SVI 하드웨어 라우팅]  │
│                                                                        │
│        ┌──────────────┐                       ┌──────────────┐         │
│        │ L3 라우터    │                       │  L3 스위치   │         │
│        └──────┬───────┘                       │  ┌────────┐  │         │
│          Trunk│ (단일 병목)                    │  │SVI 10  │  │         │
│        ┌──────┴───────┐                       │  │SVI 20  │  │         │
│        │  L2 스위치   │                       │  └────────┘  │         │
│        └──┬────────┬──┘                       │ ASIC 라우팅  │         │
│           │        │                          └──┬────────┬──┘         │
│        VLAN 10  VLAN 20                       VLAN 10  VLAN 20         │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 구분 | Router-on-a-Stick | L3 스위치 (SVI 기반 라우팅) | VXLAN 기반 오버레이 (L3 패브릭) |
|---|---|---|---|
| **처리 방식** | 외장 라우터 서브인터페이스 경유 | 백플레인 ASIC 하드웨어 라우팅 | L3 UDP 캡슐화 기반 가상화 (EVPN 제어) |
| **포워딩 성능** | 트렁크 대역폭 이중 소모, 병목 | 와이어 스피드(Wire-speed) 지원 | 데이터센터 대규모 분산 스케일아웃 |
| **VLAN 확장 한계** | 12비트 VID (최대 4,094개) | 12비트 VID (최대 4,094개) | 24비트 VNI (최대 1,600만 개 테넌트) |
| **적용 영역** | 소규모 지사 및 단순 망 | 대규모 캠퍼스 및 엔터프라이즈 백본 | 초대형 클라우드 및 멀티테넌트 데이터센터 |

## 출제 이력과 검증 출처

- 정보관리기술사 120회 1교시: VLAN 개념 및 트렁크 프로토콜
- 컴퓨터시스템응용기술사 114회 2교시: Inter-VLAN 라우팅 및 802.1Q 구조
- IEEE Std 802.1Q-2022: Bridges and Bridged Networks

## 연결 토픽

- 상위 토픽: [017 OSI 7 계층](./017_osi_7_layer.md)
- 연관 토픽: [039 SDN](./039_sdn.md), [048 통신 프로토콜 기본 요소](./048_protocol_elements.md)
