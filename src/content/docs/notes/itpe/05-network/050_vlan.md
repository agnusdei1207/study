---
title: "VLAN(Virtual Local Area Network)"
author: "agnusdei1207"
date: "2026-10-24T22:48:45+09:00"
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

- VLAN, IEEE 802.1Q, 브로드캐스트 도메인, 액세스 포트, 트렁크 포트
- 인터 VLAN 라우팅, 사설 VLAN(PVLAN), Isolated·Community·Promiscuous 포트
- VXLAN, Geneve, STP, MC-LAG, 802.1X, NAC

## Ⅰ. VLAN의 개요

- 핵심 요약 : 물리 배선과 무관하게 스위치 안에서 브로드캐스트 도메인을 논리적으로 나누는 격리 기술.
- 개념 : 물리적 토폴로지와 무관하게 스위치의 포트나 트래픽 특성을 기준으로 브로드캐스트 도메인을 논리적으로 분할·격리하는 **VLAN** (Virtual Local Area Network, 가상 근거리 통신망)이며, 표준은 IEEE(Institute of Electrical and Electronics Engineers) 802.1Q다.
- 배경 및 필요성 : 하나의 L2 스위칭 영역에서 ARP(Address Resolution Protocol), DHCP(Dynamic Host Configuration Protocol) 같은 **브로드캐스트** 트래픽이 모든 노드로 전파되어 대역폭을 낭비하고, 부서나 보안 등급별 접근 통제도 어려워짐.
- 주요 목적 : 브로드캐스트 도메인 격리로 성능 향상, 배선 변경 없는 유연한 재구성, **접근 제어 목록** (ACL, Access Control List) 연계로 보안 강화.

## Ⅱ. VLAN의 특징 및 장점

- 핵심 요약 : 프레임에 소속 태그를 붙여 하나의 물리 링크로 여러 논리 망을 나르고, 포트 역할에 따라 태그를 붙이거나 떼는 구조.

1. 태그 기반 다중화 : 이더넷 프레임에 4바이트 **802.1Q 태그** (TPID(Tag Protocol Identifier)와 TCI(Tag Control Information)로 구성)를 삽입 → 하나의 링크로 여러 VLAN 트래픽을 전달해 배선 수 절감.
2. 포트 역할 분리 : 액세스 포트는 단일 VLAN에 속하고 단말 쪽 프레임은 태그가 없으며, 트렁크 포트는 여러 VLAN 태그를 유지 → 단말은 VLAN을 의식하지 않고 스위치가 분류.
3. 논리적 격리 : 브로드캐스트 도메인이 나뉘어 한 망의 폭풍이 다른 망으로 번지지 않음 → 성능 저하와 장애의 확산을 함께 차단.

```text
[ 802.1Q 태그 삽입 ]

DMAC · SMAC · Type · Data · FCS
              ↓ SMAC 뒤 4바이트 삽입
DMAC · SMAC · TPID · TCI
· Type · Data · FCS
```

```text
[ TCI 2바이트 구성 ]

PCP 3비트  : QoS 우선순위
DEI 1비트  : 폐기 적격 표시
VID 12비트 : VLAN ID (0~4095)
```

## Ⅲ. VLAN의 구조 (흐름)

- 핵심 요약 : 같은 VLAN 안의 통신은 스위치가 처리하고, 서로 다른 VLAN 간 통신은 L3(네트워크 계층) 중계를 거치는 구조.
- **인터 VLAN 라우팅** (Inter-VLAN Routing) : 논리적으로 분할된 VLAN 사이의 통신은 L2 스위치만으로 불가능하므로, L3 스위치의 SVI(Switch Virtual Interface)나 라우터(Router-on-a-Stick)에서 포워딩.

```text
[ VLAN 10 → VLAN 20 통신 ]

단말 A (VLAN 10)
      ↓ 액세스 포트 (태그 부착)
L2 스위치 → 트렁크 링크
      ↓
L3 스위치 (SVI 라우팅)
      ↓ 대상 VLAN 20으로 전달
단말 B (VLAN 20)
```

## Ⅳ. VLAN 구성 방식의 비교

- 핵심 요약 : 할당 기준이 물리 포트에서 단말 식별자, IP 대역으로 옮겨갈수록 이동성은 좋아지고 위조 위험은 커지는 구조.

| 구분 | 포트 기반 VLAN | MAC 기반 VLAN | 서브넷 기반 VLAN | 사설 VLAN (PVLAN) |
| --- | --- | --- | --- | --- |
| 할당 기준 | 스위치의 물리 포트 번호 | 접속 단말의 MAC 주소 | 패킷의 L3 IP 서브넷 대역 | 동일 VLAN 내 포트 역할 |
| 단말 이동 | 포트를 옮기면 재설정 필요 | 단말을 따라 VLAN 유지 | 단말 IP에 따라 자동 매핑 | 포트 역할에 따라 고정 |
| 운영 복잡도 | 가장 단순, 널리 사용 | 단말 MAC 사전 등록 부담 | L3 헤더 검사로 오버헤드 | Primary·Secondary 매핑 필요 |
| 보안성 | 물리 포트 탈취 시 취약 | MAC 스푸핑 위험 | IP 변조 위험 | 같은 VLAN 안에서도 통신 제한 |

- **사설 VLAN** (PVLAN, Private VLAN) : 하나의 VLAN 안에서 포트 간 통신을 한 번 더 격리하는 방식.
  - Isolated 포트 : Promiscuous 포트(게이트웨이)하고만 통신하고, 다른 Isolated 포트와는 차단.
  - Community 포트 : 같은 커뮤니티끼리만 통신하고, 다른 커뮤니티와는 차단.
  - Promiscuous 포트 : 모든 Isolated·Community 포트와 통신하는 상위 포트.
- 선택 기준 : 관리 단순성이 우선이면 포트 기반, 단말 이동이 잦으면 MAC 기반, 같은 서브넷 내 단말 간 차단이 필요하면 사설 VLAN을 택함.

## Ⅴ. VLAN의 한계와 방안

- 핵심 요약 : VLAN ID 공간의 한계, 루프와 대역 낭비, 포트 기반 인증의 취약점을 오버레이와 인증 연계로 보완.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| VLAN ID 공간 부족 | VLAN ID가 12비트라 4,096개 중 0과 4095를 뺀 4,094개만 사용 가능 → 대규모 테넌트 격리 불가 | 24비트 VNI(VXLAN Network Identifier) 기반 **VXLAN** (Virtual eXtensible LAN) 또는 Geneve로 L3 위에 L2 오버레이 구성 | 테넌트 수 대비 세그먼트 사용률 |
| STP 루프와 대역 낭비 | 트렁크 확장 시 STP(Spanning Tree Protocol)가 중복 링크를 블로킹 → 다중 링크 대역 사용 저하 | MC-LAG(Multi-Chassis Link Aggregation) 또는 L3 기반 리프-스파인 구조 | 블로킹 포트 수, 링크 활용률 |
| 포트 기반 인증 부재 | 물리 포트에 접속하면 신원 확인 없이 VLAN이 배정되어 무단 접속 위험 | 802.1X 인증과 NAC(Network Access Control) 연동 | 인증 실패율, 미인가 단말 차단 건수 |

## Ⅵ. VLAN에 대한 기술사적 제언

- 핵심 요약 : VLAN을 보안 경계의 전부로 보지 않고, 인증 기반 정책과 워크로드 단위 격리로 확장하는 방향.

VLAN은 서브넷 단위의 거친 분리에 그치므로, 호스트 방화벽과 워크로드 단위 정책을 결합한 마이크로 세그멘테이션으로 점차 옮겨 가는 것이 바람직하다. 온프레미스 VLAN과 퍼블릭 클라우드의 VPC(Virtual Private Cloud)는 전용 회선이나 IPsec(Internet Protocol Security) VPN으로 연결하고, 두 환경의 보안 정책을 한 체계에서 관리하는 것이 필요하다. 포트 인증 결과에 따라 VLAN을 동적으로 배정하는 구조는 배선 변경 없이 사용자 권한과 단말 상태를 반영하는 기반이 된다.

## Ⅶ. 결론

- 핵심 요약 : VLAN은 물리망 위에서 브로드캐스트 도메인과 접근 정책을 논리적으로 나누는 기본 격리 수단.
- 시사점 : 규모가 커지면 VLAN ID 한계와 STP 문제가 드러나므로, 오버레이 기술과 인증 기반 정책으로 점진적으로 확장하는 것이 현실적이다.
