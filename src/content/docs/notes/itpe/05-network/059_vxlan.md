---
title: "VXLAN(Virtual Extensible Local Area Network) (VXLAN: Virtual Extensible LAN)"
author: "agnusdei1207"
date: "2026-10-24T22:48:49+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- VXLAN(Virtual eXtensible Local Area Network), VNI(VXLAN Network Identifier), VTEP(VXLAN Tunnel End Point)
- 오버레이 네트워크(Overlay Network), 언더레이 네트워크(Underlay Network), MAC-in-UDP
- VLAN, BGP EVPN(Ethernet VPN), ECMP(Equal-Cost Multi-Path), 인그레스 복제(Ingress Replication)
- 리프-스파인(Leaf-Spine), DCI(Data Center Interconnect), MTU(Maximum Transmission Unit)

## Ⅰ. VXLAN(Virtual eXtensible Local Area Network)의 개요

- 핵심 요약 : L3 IP 네트워크 위에 L2 프레임을 UDP로 감싸 대규모 가상 L2 망을 만드는 네트워크 가상화 표준.
- 개념 : 기존 L3 IP 네트워크(언더레이) 위에 이더넷 프레임을 UDP 패킷으로 캡슐화해 논리적인 L2 오버레이 망을 구축하는 **VXLAN** (Virtual eXtensible Local Area Network, RFC 7348) 프로토콜.
- 배경 및 필요성 : 클라우드 데이터센터에서 VLAN(Virtual Local Area Network) ID(12비트)로 수용할 수 있는 세그먼트가 4,094개로 제한되고, L2 확장 시 STP(Spanning Tree Protocol)로 링크가 차단되며, 가상머신(VM, Virtual Machine)의 무중단 라이브 마이그레이션에는 L2 연결성이 필요해짐.
- 주요 목적 : 24비트 **VNI** (VXLAN Network Identifier)로 세그먼트를 대규모로 분리하고, L3 ECMP(Equal-Cost Multi-Path)로 물리 경로를 모두 활용하며, 데이터센터 전역의 L2 이동성을 보장.

## Ⅱ. VXLAN의 특징 및 장점

- 핵심 요약 : 논리망과 물리망을 캡슐화로 분리하고, 해시 기반 경로 분산과 BGP EVPN 제어로 확장성과 경로 활용을 함께 확보하는 방식.

1. MAC-in-UDP 캡슐화 : **VTEP** (VXLAN Tunnel End Point, 캡슐화·역캡슐화를 수행하는 터널 종단점)이 원본 프레임을 UDP(User Datagram Protocol) 4789 포트로 감쌈 → 기존 IP 라우팅망을 그대로 활용.
2. 24비트 VNI : 2의 24제곱, 약 1,677만 개의 세그먼트를 정의 → 멀티테넌트 간 격리 확보.
3. 해시 기반 ECMP 분산 : 내부 헤더 해시를 외부 UDP 소스 포트에 넣어 중간 라우터가 여러 경로로 트래픽을 나눔 → 링크 활용률 향상과 STP 차단 제거.
4. 분산 게이트웨이 : **BGP EVPN** (Ethernet VPN, 이더넷 VPN 제어 기능)으로 MAC·IP 도달 정보를 미리 배포 → ARP(Address Resolution Protocol) 플러딩 감소.

## Ⅲ. VXLAN의 구조 (흐름)

- 핵심 요약 : VM 프레임이 VTEP에서 감싸져 IP 망을 건너 수신 VTEP에서 풀리는 터널 구조이며, 리프 스위치가 VTEP 역할을 담당하는 것이 일반적인 배치.

```text
[ 원본 이더넷 프레임 ]  VM → VTEP
        ↓ 캡슐화 (약 50바이트 추가)
[ 외부 IP 헤더 ] [ UDP 4789 ]
[ VXLAN 헤더 (VNI 24비트) ]
[ 원본 프레임 ]
        ↓ L3 언더레이 라우팅
수신 VTEP에서 역캡슐화
```

```text
[ 스파인 ]  IP 고속 전달 전담
        ↑↓ ECMP
[ 리프 = VTEP ]  캡슐화·역캡슐화
        ↑↓
[ 서버·VM ]  원본 L2 프레임
```

- 오버헤드 구성 : 외부 이더넷 헤더 14바이트, 외부 IP 헤더 20바이트, UDP 헤더 8바이트, VXLAN 헤더 8바이트를 합쳐 약 50바이트가 추가됨.

## Ⅳ. VXLAN과 전통적 VLAN의 비교

- 핵심 요약 : VLAN은 단일 L2 도메인 안의 분할에 머물지만, VXLAN은 L3 망 위에서 세그먼트 수와 이동 범위를 함께 넓힘.

| 비교 축 | VLAN (IEEE 802.1Q) | VXLAN (RFC 7348) |
| --- | --- | --- |
| 세그먼트 식별자 | 12비트 VID (최대 4,094개) | 24비트 VNI (약 1,677만 개) |
| 캡슐화 방식 | L2 이더넷 태그 삽입 (4바이트) | L3 UDP 오버레이 캡슐화 (약 50바이트) |
| 물리망(언더레이) 요건 | 순수 L2 스위칭망 | 표준 L3 IP 라우팅망 (OSPF(Open Shortest Path First), BGP(Border Gateway Protocol) 기반) |
| 루프 방지와 대역 활용 | STP로 일부 링크 차단 | L3 ECMP로 전 경로 동시 활용 |
| VM 마이그레이션 범위 | 동일 L2 도메인 내로 제한 | L3를 넘어 데이터센터 간 이동 가능 |
| 제어 평면 | 데이터 평면 Flooding과 MAC 학습 | 멀티캐스트 또는 BGP EVPN |

- 제어 평면 연동 : 초기 멀티캐스트 기반 Flood-and-Learn의 비효율을 피하려고, BGP EVPN으로 VTEP 간 MAC·IP 정보를 사전에 배포하고 분산 애니캐스트 게이트웨이(Distributed Anycast Gateway)를 구현.

## Ⅴ. VXLAN의 한계와 방안

- 핵심 요약 : 캡슐화 오버헤드로 인한 단편화와 멀티캐스트 의존이 운영 한계이며, 점보 프레임과 BGP EVPN 기반 유니캐스트 복제로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 캡슐화 오버헤드로 인한 단편화 | 표준 MTU(Maximum Transmission Unit) 1500바이트에 약 50바이트가 더해져 L3 구간에서 단편화와 라우터 부하 증가 | 언더레이 전 구간 MTU를 점보 프레임으로 확장 | 단편화 패킷 수, MTU 불일치 건수 |
| BUM 트래픽을 위한 멀티캐스트 의존 | 브로드캐스트·미지 유니캐스트·멀티캐스트 처리를 위해 PIM(Protocol Independent Multicast) 설정이 강제되어 운영 부담 증가 | BGP EVPN 제어 평면을 도입하고 인그레스 복제(Ingress Replication)로 유니캐스트 전환 | 복제 트래픽량, 제어 평면 수렴 시간 |

## Ⅵ. VXLAN 적용 및 발전을 위한 기술사적 제언

- 핵심 요약 : 리프 스위치 하드웨어 VTEP 오프로딩, 리프-스파인과 BGP EVPN의 표준 구성, DCI 구간 VXLAN 연장으로 운영 체계를 갖추는 것.

1. 대규모 데이터센터 운영자는 리프 스위치의 전용 칩(ASIC, Application-Specific Integrated Circuit)을 VTEP으로 쓰는 하드웨어 오프로딩을 기본 설계에 넣어, 소프트웨어 가상 스위치가 캡슐화 연산에 쓰는 CPU 부담을 덜어야 한다.
2. 네트워크 조직은 리프-스파인 패브릭과 BGP EVPN을 표준 구성으로 정착시켜, 장비 추가 시에도 제어 평면을 자동으로 확장할 수 있는 운영 체계를 갖춰야 한다.
3. 재해 복구 요건이 있는 기관은 리전 간 데이터센터 상호 연결(DCI, Data Center Interconnect) 구간에 VXLAN 터널을 연장하는 구성을 사전에 설계해, IP 변경 없이 서비스를 절체할 수 있도록 해야 한다.

## Ⅶ. 결론

- 핵심 요약 : VXLAN은 IP 망 위에 L2 논리망을 겹쳐 멀티테넌트 확장과 이동성을 함께 해결하는 오버레이 표준.
- 시사점 : 확장성은 리프-스파인과 EVPN 제어 체계가, 성능은 MTU 설계와 하드웨어 가속이 좌우한다.
