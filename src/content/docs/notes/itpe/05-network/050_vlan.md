---
title: "VLAN(Virtual Local Area Network)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  question_no: "050"
  keyword_grade: "응용"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- VLAN(Virtual Local Area Network), IEEE 802.1Q, 브로드캐스트 도메인
- 액세스 포트, 트렁크 포트, 인터 VLAN 라우팅, 사설 VLAN(PVLAN)
- VXLAN, 802.1X 인증, 마이크로 세그멘테이션

## Ⅰ. VLAN의 개요

- 핵심 요약 : 물리 배선과 무관하게 하나의 스위칭 영역을 논리 방 단위로 나누는 L2 격리 기술.
- 개념 : 스위치의 포트와 프레임 태그를 기준으로 **브로드캐스트 도메인** (Broadcast Domain)을 논리적으로 분할하는 가상 근거리 통신망(**VLAN**, Virtual Local Area Network)이며, 프레임 형식 표준은 IEEE(Institute of Electrical and Electronics Engineers) 802.1Q다.
- 배경 및 필요성 : 단일 L2 영역에서 ARP(Address Resolution Protocol) 같은 브로드캐스트 프레임이 전 단말로 확산되어 대역폭을 소모하고, 부서·보안 등급별 분리가 물리 배치에 종속되는 문제가 있었음.
- 주요 목적 : 브로드캐스트 영역 격리를 통한 성능 확보, 배선 변경 없는 조직 단위 재구성, 보안 구역의 논리 분리.

## Ⅱ. VLAN의 특징 및 장점

- 핵심 요약 : 프레임 태그와 포트 역할의 조합이 하나의 물리 링크로 여러 논리 망을 나르는 구조와 운영 효율을 만드는 방식.

1. 태그 기반 식별 : 이더넷 프레임에 4바이트 **802.1Q 태그** (VLAN 소속 식별 정보)를 삽입 → 하나의 링크로 다중 VLAN 운반이 가능한 다중화 효과.
2. 포트 역할 분리 : 단말 접속용 **액세스 포트** (Access Port)는 단일 VLAN으로 태그를 부착·제거하고, 스위치 간 **트렁크 포트** (Trunk Port)는 여러 VLAN 태그를 그대로 운반 → 단말이 VLAN을 의식하지 않는 운영 효율.
3. 논리 격리 : VLAN 식별자가 다르면 L2 포워딩이 차단 → 브로드캐스트 폭풍과 장애의 확산 방지 효과.
4. 정책 단위 제공 : VLAN 단위 필터링·품질 정책 적용 → 보안 경계와 서비스 기준의 관리 단위 확보 효과.

## Ⅲ. VLAN의 구조 (흐름)

- 핵심 요약 : 동일 VLAN 통신은 스위치가 태그로 완결하고, VLAN 간 통신은 L3 라우팅을 거치는 이중 구조.

```text
[ 동일 VLAN 통신 ]

단말 A (VLAN 10)
   ↓ 액세스 포트에서 태그 판별
스위치 포워딩 (동일 VLAN)
   ↓ 액세스 포트로 태그 제거 출력
단말 B (VLAN 10)
```

```text
[ VLAN 간 통신 ]

단말 A (VLAN 10)
   ↓ 트렁크 링크 경유
L3 스위치 SVI 라우팅
   ↓ VLAN 20으로 재전송
단말 B (VLAN 20)
```

- VLAN 간 전달 : 논리 분할로 직접 통신이 막힌 VLAN 사이를 잇는 **인터 VLAN 라우팅** (Inter-VLAN Routing)은 L3 스위치의 SVI(Switch Virtual Interface)나 라우터 서브인터페이스가 수행하는 구조.

## Ⅳ. VLAN 구성 방식의 비교

- 핵심 요약 : 할당 기준이 포트에서 단말·서브넷·포트 역할로 이동할수록 유연성은 커지고 설정 복잡도도 함께 커지는 구조.

| 비교 축 | 포트 기반 | MAC 주소 기반 | 서브넷 기반 | 사설 VLAN |
| --- | --- | --- | --- | --- |
| 할당 기준 | 스위치 물리 포트 | 단말 MAC 주소 | 단말 IP 서브넷 | 동일 VLAN 내 포트 역할 |
| 단말 이동 | 포트 재설정 필요 | 단말을 따라 유지 | IP에 따라 자동 | 역할에 따라 고정 |
| 운영 부담 | 가장 단순 | MAC 사전 등록 | L3 검사 부담 | Primary·Secondary 매핑 |
| 보안 특성 | 포트 탈취에 취약 | MAC 위조 위험 | IP 변조 위험 | 동일 VLAN 내 차단 |

- **사설 VLAN** (PVLAN, Private VLAN) : 하나의 VLAN 안에서 포트 역할로 통신을 한 번 더 제한하는 보조 구조.
  1. Promiscuous 포트 : 게이트웨이처럼 모든 포트와 통신하는 상위 포트.
  2. Isolated 포트 : 상위 포트하고만 통신하고 동급 포트와는 차단.
  3. Community 포트 : 같은 커뮤니티 내에서만 상호 통신을 허용.
- 선택 기준 : 관리 단순성이 우선이면 포트 기반, 단말 이동이 잦으면 MAC 주소 기반, 동일 서브넷 내 단말 간 차단이 필요하면 사설 VLAN을 택함.

## Ⅴ. VLAN의 한계와 방안

- 핵심 요약 : 식별자 공간 한계와 루프 차단의 대역 낭비, 무단 접속을 오버레이·인증 연계로 보완.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 식별자 공간 한계 | VLAN ID가 12비트라 사용 가능 개수가 4,094개로 제한 → 대규모 테넌트 격리 불가 | 24비트 VNI(VXLAN Network Identifier)의 **VXLAN** (Virtual eXtensible LAN) 오버레이 전환 | 세그먼트 사용률 |
| 루프 차단의 대역 낭비 | 이중화 링크가 STP(Spanning Tree Protocol)에 의해 차단 → 링크 활용률 저하 | MC-LAG(Multi-chassis Link Aggregation) 또는 L3 패브릭 구조 | 링크 활용률 |
| 무단 접속과 위조 | 포트 접속만으로 VLAN 배정 → 미인가 단말의 내부 자원 접근 | 802.1X 인증과 NAC(Network Access Control) 연동 동적 배정 | 인증 실패율, 차단 건수 |

## Ⅵ. VLAN에 대한 기술사적 제언

- 핵심 요약 : VLAN 격리를 보안 경계의 끝이 아니라 정책 세분화와 클라우드 연계, 설정 거버넌스의 출발점으로 삼는 방향.

1. 보안 아키텍처 조직은 호스트·워크로드 단위의 **마이크로 세그멘테이션** (Micro-Segmentation)을 단계 도입해 VLAN의 거친 분리를 보완.
2. 네트워크 운영 조직은 온프레미스 VLAN과 클라우드 VPC(Virtual Private Cloud) 구간을 전용선·IPsec(Internet Protocol Security) VPN으로 연결해 정책을 한 체계로 관리.
3. 운영 거버넌스 조직은 VLAN 설정 변경을 자동화 도구와 설정 감사 절차로 통제해 설정 불일치를 방지.

## Ⅶ. 결론

- 핵심 요약 : VLAN은 물리망 위에서 방 단위 논리 격리를 제공하는 네트워크 설계의 기본 단위.
- 물리 배치와 무관한 논리 설계라는 특성이 조직 변화에 유연한 네트워크 운영의 기반이 되는 점이 함의.
