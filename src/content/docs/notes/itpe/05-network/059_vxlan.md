---
title: "VXLAN(Virtual Extensible Local Area Network) (VXLAN: Virtual Extensible LAN)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- VXLAN(Virtual eXtensible Local Area Network), 오버레이(Overlay), 언더레이(Underlay)
- VTEP(VXLAN Tunnel End Point), VNI(VXLAN Network Identifier), MAC-in-UDP 캡슐화
- UDP(User Datagram Protocol) 4789 포트, BGP EVPN(Ethernet VPN), 인그레스 복제(Ingress Replication)
- BUM 트래픽, 분산 애니캐스트 게이트웨이(Distributed Anycast Gateway), 리프-스파인(Leaf-Spine)

## Ⅰ. VXLAN의 개요

- 핵심 요약 : L3 IP망 위에서 UDP 캡슐화로 논리 L2 구간을 만들어 대규모 멀티테넌트 네트워크를 구현하는 오버레이 표준.
- 개념 : 이더넷 프레임을 UDP(User Datagram Protocol) 패킷으로 감싸 L3 IP망 위에 논리 L2 구간을 형성하는 **VXLAN**(Virtual eXtensible Local Area Network, RFC 7348) 프로토콜이며, 논리망이 물리망 위에 겹쳐지는 **오버레이**(Overlay) 구조가 핵심.
- 배경 및 필요성 : 클라우드 데이터센터에서 가상머신(VM, Virtual Machine) 수와 테넌트 수가 기존 세그먼트 식별 체계의 용량을 초과했고, 루프 방지를 위한 링크 차단 구조와 가상머신 이동 시의 논리 L2 연속성 요구가 겹치면서 물리망과 독립된 논리망 기술이 필요해짐.
- 주요 목적 : 24비트 식별자로 테넌트 세그먼트를 대규모로 분리하고, 표준 IP 라우팅망을 그대로 활용하며, 데이터센터 전역의 논리 L2 연결성 보장.

## Ⅱ. VXLAN의 특징 및 장점

- 핵심 요약 : 캡슐화로 논리망과 물리망을 분리하고 24비트 식별과 컨트롤 플레인 제어로 확장성과 안정성을 함께 확보.

1. MAC-in-UDP 캡슐화 : **VTEP**(캡슐화·역캡슐화를 수행하는 터널 종단점, VXLAN Tunnel End Point)이 원본 프레임을 외부 IP·UDP 헤더로 감싸고 수신 VTEP에서 복원 → 표준 IP 라우팅망 위에서 L2 연결성 제공.
2. 24비트 세그먼트 식별 : **VNI**(VXLAN 세그먼트 식별자, VXLAN Network Identifier)가 약 1,677만 개의 논리 세그먼트를 구분 → 대규모 멀티테넌트 격리 확보.
3. 해시 기반 경로 분산 : 내부 프레임 해시값을 외부 UDP 소스 포트에 반영 → 언더레이 라우터의 ECMP(Equal-Cost Multi-Path)로 전 경로 동시 활용.
4. 컨트롤 플레인 제어 : **BGP EVPN**(경로 배포 기반 이더넷 VPN 제어, Ethernet VPN)이 VTEP 간 MAC·IP 도달 정보를 사전 배포 → 불필요한 플러딩 제거와 안정적 수렴.

## Ⅲ. VXLAN의 구조 (흐름)

- 핵심 요약 : 원본 프레임이 VTEP에서 캡슐화되어 IP망을 건너고 수신 VTEP에서 복원되는 터널 구조.
- VTEP 배치 : 하이퍼바이저의 가상 스위치 또는 리프 스위치가 VTEP 역할을 수행하는 형태가 일반적.
- 오버헤드 : 외부 이더넷·IP·UDP 헤더와 VXLAN 헤더를 합쳐 약 50바이트가 추가되어 MTU(Maximum Transmission Unit) 설계와 연동.

```text
[ 캡슐화된 프레임 구조 ]

외부 이더넷 헤더
    ↓
외부 IP 헤더 (VTEP 간 주소)
    ↓
UDP 헤더 (4789 포트)
    ↓
VXLAN 헤더 (VNI 24비트)
    ↓
원본 이더넷 프레임
```

```text
[ 오버레이 터널 흐름 ]

VM → 리프 스위치 (VTEP)
    ↓ 캡슐화
스파인 계층 (IP 라우팅)
    ↓ ECMP 경로 분산
리프 스위치 (VTEP)
    ↓ 역캡슐화
목적지 VM으로 원본 프레임 전달
```

## Ⅳ. VXLAN 컨트롤 플레인 방식의 비교

- 핵심 요약 : 데이터 평면 학습 방식은 멀티캐스트에 의존하는 반면, BGP EVPN 방식은 경로 사전 배포로 예측 가능한 운영을 제공.

| 비교 축 | 플러드 앤 러닝 (멀티캐스트 기반) | BGP EVPN (컨트롤 플레인 기반) |
| --- | --- | --- |
| 도달 정보 습득 | 데이터 평면에서 실시간 학습 | MAC·IP 경로의 사전 배포 |
| **BUM 트래픽**(브로드캐스트·미지 유니캐스트·멀티캐스트) 처리 | 언더레이 멀티캐스트 라우팅 의존 | 인그레스 복제(Ingress Replication) 유니캐스트 |
| ARP(Address Resolution Protocol) 처리 | 전 구간 플러딩 | 경로 기반 응답으로 플러딩 억제 |
| 언더레이 요건 | 멀티캐스트 라우팅 설계 필요 | 순수 유니캐스트 라우팅만 요구 |
| 확장성 | 그룹 수 증가 시 복잡도 상승 | 경로 수 기반의 예측 가능한 확장 |

- 선택 기준 : 소규모 구성과 멀티캐스트 운영 역량이 있는 환경은 플러드 앤 러닝도 가능하나, 대규모 멀티테넌트 데이터센터는 BGP EVPN 표준 구성이 원칙.
- 게이트웨이 선택 : 서브넷 간 통신이 잦은 환경은 VTEP마다 게이트웨이를 두는 분산 애니캐스트 게이트웨이(Distributed Anycast Gateway) 구성이 유리.

## Ⅴ. VXLAN 운영의 한계와 방안

- 핵심 요약 : 캡슐화 오버헤드, 문제 분석 가시성 저하, 제어 경로 불일치가 운영 한계이며 설계·도구·검증으로 일대일 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 오버헤드로 인한 단편화 | 약 50바이트 추가로 표준 MTU 환경에서 단편화와 처리 부하 증가 | 언더레이 전 구간의 점보 프레임 허용과 MTU 일관성 점검 | 단편화 패킷 수, MTU 불일치 건수 |
| 문제 분석 가시성 저하 | 캡슐화로 내부 헤더와 경로 확인이 어려워 장애 원인 규명 지연 | 내부 헤더를 보존하는 패킷 분석 도구와 흐름 텔레메트리 도입 | 장애 평균 복구 시간, 가시성 커버리지 |
| 제어 경로 불일치 | VTEP 간 EVPN 경로 상이 시 트래픽 블랙홀과 학습 오류 발생 | 구성 검증 자동화와 경로 일관성 점검 절차 운영 | 경로 불일치 검출 건수, 수렴 시간 |

## Ⅵ. VXLAN 적용 확산을 위한 기술사적 제언

- 핵심 요약 : 하드웨어 오프로딩, 표준 패브릭 구성의 정착, 데이터센터 간 연장 설계로 운영 체계를 갖추는 것.

1. 대규모 데이터센터 운영자는 리프 스위치의 전용 칩(ASIC, Application-Specific Integrated Circuit)을 VTEP으로 쓰는 하드웨어 오프로딩을 기본 설계에 반영해, 서버 CPU의 캡슐화 부담을 제거해야 한다.
2. 네트워크 조직은 리프-스파인 패브릭과 BGP EVPN을 표준 구성으로 정착시켜, 장비 추가 시에도 제어 평면이 자동 확장되는 운영 체계를 마련해야 한다.
3. 재해 복구 요건이 있는 기관은 데이터센터 간 상호 연결(DCI, Data Center Interconnect) 구간에 VXLAN 터널을 연장하는 설계를 사전에 확정해, IP 변경 없는 서비스 절체 능력을 확보해야 한다.

## Ⅶ. 결론

- 핵심 요약 : VXLAN은 IP망 위에 논리 L2 구간을 겹쳐 멀티테넌트 확장과 가상머신 이동성을 함께 해결하는 오버레이 표준.
- 확장성은 EVPN 컨트롤 플레인과 리프-스파인 패브릭이, 성능은 MTU 설계와 하드웨어 오프로딩이 좌우한다.
