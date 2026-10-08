---
title: "VLAN(Virtual Local Area Network)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. VLAN(Virtual LAN)의 개요

- 개념 : 물리적인 네트워크 토폴로지와 무관하게 스위치 장비 내부에서 포트나 트래픽 특성을 기준으로 브로드캐스트 도메인을 논리적으로 분할 및 격리하는 **가상 근거리 통신망** 기술 (IEEE(Institute of Electrical and Electronics Engineers) 802.1Q).
- 배경 및 필요성 : 동일 L2 스위칭 환경에서 전체 노드로 전파되는 ARP(Address Resolution Protocol), DHCP(Dynamic Host Configuration Protocol) 등 브로드캐스트 트래픽 폭증으로 인한 대역폭 낭비 억제 및 부서·보안 등급별 네트워크 접근 통제 필요성 증대.
- 핵심 목적 : 브로드캐스트 도메인 격리를 통한 네트워크 성능 향상, 물리적 배선 변경 없는 유연한 네트워크 재구성, **접근 제어 목록(ACL, Access Control List)** 연계를 통한 보안성 강화.

## Ⅱ. VLAN의 핵심 아키텍처 및 동작 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   [ IEEE 802.1Q 태그 프레임 구조 ]                     │
│                                                                        │
│   표준 이더넷 프레임                                                   │
│   ┌────────┬────────┬─────────────────────────┬────────┬───────┐       │
│   │ DMAC   │ SMAC   │      Type / Length      │ Data   │ FCS   │       │
│   │ 6 Byte │ 6 Byte │         2 Byte          │        │ 4 Byte│       │
│   └────────┴────────┴─────────────────────────┴────────┴───────┘       │
│                                   │                                    │
│   ▼ 802.1Q 태그 4바이트 삽입       │                                    │
│   ┌────────┬────────┬─────────────────────────┬────────┬───────┬───────┐│
│   │ DMAC   │ SMAC   │ TPID (0x8100) │ TCI     │ Type   │ Data  │ FCS   ││
│   │ 6 Byte │ 6 Byte │    2 Byte     │ 2 Byte  │ 2 Byte │       │ 4 Byte││
│   └────────┴────────┴───────────────┴─────────┴────────┴───────┴───────┘│
│                                           │                            │
│                         ┌─────────────────┴─────────────────┐          │
│                         │ PCP (3bit) │ DEI (1bit) │ VID (12bit)     │  │
│                         │ QoS 우선순위│ 드롭 적격  │ VLAN ID (0~4095)│  │
│                         └───────────────────────────────────┘          │
└────────────────────────────────────────────────────────────────────────┘
```

- **IEEE 802.1Q 프레임 태깅** : 이더넷 헤더의 송신 MAC(Media Access Control) 주소 뒤에 4바이트 태그를 삽입. TPID(Tag Protocol Identifier: `0x8100`)와 TCI(Tag Control Information)로 구성.
- 포트 분류 메커니즘 :
  - **액세스 포트 (Access Port)** : 단일 VLAN(Virtual Local Area Network)에만 속하는 포트로 일반 PC(Personal Computer)/서버와 연결되며, 스위치 유입 시 태그를 붙이고 단말로 나갈 때 태그를 제거(Untagged).
  - **트렁크 포트 (Trunk Port)** : 여러 VLAN 트래픽을 단일 물리 링크로 동시 다중화 전송하며 프레임에 802.1Q 태그를 그대로 유지(Tagged).
- **인터 VLAN 라우팅 (Inter-VLAN Routing)** : 논리적으로 분할된 서로 다른 VLAN 간 통신은 L2 스위치 자체로는 불가하며, L3 스위치의 가상 라우팅 인터페이스(SVI, Switch Virtual Interface)나 라우터(Router-on-a-Stick)를 통해 L3 포워딩 수행.

## Ⅲ. VLAN 구성 방식 및 확장 기술 비교 분석

| 구분 | 포트 기반 VLAN | MAC 기반 VLAN | 서브넷 기반 VLAN | 사설 VLAN (PVLAN) |
|---|---|---|---|---|
| 할당 기준 | 스위치의 물리 포트 번호 | 접속 단말의 MAC 주소 | 패킷의 L3 IP(Internet Protocol) 서브넷 대역 | 동일 VLAN 내 포트 격리 |
| 동적 이동성 | 포트 이동 시 재설정 필요 | 단말 이동 시 자동 VLAN 유지 | 단말 IP 기준 자동 매핑 | 엄격한 다운스트림 격리 |
| 운영 복잡도 | 매우 단순, 가장 널리 사용 | 단말 MAC 사전 등록 부담 | L3 헤더 검사로 오버헤드 | Primary/Secondary 매핑 |
| 보안성 | 물리 포트 탈취 시 취약 | MAC 스푸핑 위험 | IP 변조 가능 | 동일 서브넷 간 통신 차단 |

- **사설 VLAN (Private VLAN: PVLAN)** : 동일한 서브넷/VLAN 내부에서 포트 간 통신을 추가 격리.
  - **Isolated Port** : 오직 Promiscuous 포트(게이트웨이)와만 통신 가능, 동일 Isolated 포트 간 차단.
  - **Community Port** : 동일 커뮤니티 그룹 간에는 상호 통신 가능, 타 커뮤니티는 차단.
  - **Promiscuous Port** : 모든 포트(Isolated, Community)와 자유롭게 통신 가능한 마스터 포트.

## Ⅳ. VLAN의 주요 한계점 및 해결 방안

- 12비트 VID 공간 한계로 인한 초대규모 멀티테넌시 수용 불가 :
  - 한계점 : VLAN ID가 12비트($2^{12} = 4,096$개, 실제 가용 4,094개)로 제한되어 클라우드 데이터센터의 수만 개 가상 머신(VM, Virtual Machine) 및 테넌트 격리 불가능.
  - 해결 방안 : 24비트 VNI(VXLAN Network Identifier, $1,600만$개 세그먼트)를 제공하고 L3 언더레이 위에 L2 오버레이를 구성하는 VXLAN(Virtual eXtensible LAN) 및 Geneve 기술로 전환.
- L2 도메인 확장에 따른 STP(Spanning Tree Protocol) 루프 및 대역폭 낭비 :
  - 한계점 : VLAN 트렁크 링크 확장에 따라 스패닝 트리 프로토콜(STP)이 블로킹 포트를 생성하여 다중 물리 링크 대역폭의 상당 부분 사장.
  - 해결 방안 : MC-LAG(Multi-Chassis Link Aggregation) 또는 L3 기반 리프-스파인(Leaf-Spine) 아키텍처 위에 오버레이 터널링 구축.

## Ⅴ. VLAN 적용 및 발전을 위한 기술사적 제언

- 제로 트러스트(Zero Trust) 마이크로 세그멘테이션으로의 진화 : 단순 서브넷 기반 VLAN 분리에 머물지 않고, 호스트 방화벽과 eBPF 기반 소프트웨어 정의 경계(SDP, Software-Defined Perimeter)를 연동하여 워크로드 단위 극소 격리 달성.
- Dynamic VLAN과 802.1X NAC(Network Access Control) 연동 : 사용자가 포트에 접속할 때 RADIUS(Remote Authentication Dial-In User Service) 인증을 거쳐 사용자의 권한과 디바이스 무결성에 따라 스위치가 동적으로 VLAN을 할당하는 자동화 인프라 구성.
- 클라우드 VPC(Virtual Private Cloud)와의 하이브리드 연계 설계 : 온프레미스 VLAN 네트워크와 퍼블릭 클라우드의 가상 사설망(VPC)을 Direct Connect / IPsec(Internet Protocol Security) VPN(Virtual Private Network)을 통해 일관된 보안 서브넷 정책으로 통합 관리.
