---
title: "VXLAN(Virtual eXtensible LAN)"
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

네트워크 → 데이터센터 오버레이 → VXLAN

## 30초 인출

- 본질: **VXLAN(Virtual eXtensible LAN)** 은 L3 네트워크 위에 가상 L2 세그먼트를 제공하는 캡슐화 방식
- 메커니즘: VTEP가 내부 Ethernet 프레임을 VNI가 든 VXLAN 헤더와 UDP/IP로 캡슐화하고, 상대 VTEP가 이를 풀어 내부 프레임을 전달

<details>
<summary>핵심 용어</summary>

- **VXLAN(Virtual eXtensible LAN):** L2 프레임을 UDP/IP로 캡슐화해 L3 네트워크 위에 가상 L2 세그먼트를 만드는 방식
- **VTEP(VXLAN Tunnel Endpoint):** VXLAN 프레임을 캡슐화·역캡슐화하는 터널 종단
- **VNI(VXLAN Network Identifier):** VXLAN 오버레이 세그먼트를 구분하는 24비트 식별자
- **EVPN(Ethernet VPN):** BGP 제어 평면으로 MAC·IP 도달 정보를 교환하는 Ethernet VPN 기술
- **MTU(Maximum Transmission Unit):** 한 링크에서 전달 가능한 최대 패킷 크기
- **BGP(Border Gateway Protocol):** 경로 정보를 교환하며 EVPN에서는 MAC·IP 도달 정보를 전달하는 프로토콜
- **VLAN(Virtual Local Area Network):** 물리 LAN을 논리적 브로드캐스트 도메인으로 분리하는 기술

</details>

---

## 1교시 예상문제 (10점)

> VXLAN의 개념과 캡슐화 동작을 설명하시오. (예상)

---

## 1교시 10점 답안

## Ⅰ. VXLAN 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **VXLAN(Virtual eXtensible LAN):** 내부 L2 프레임을 UDP/IP로 캡슐화해 L3 위에 가상 L2 세그먼트를 제공하는 방식 |
| 목적 | 데이터센터 L2 세그먼트의 확장과 테넌트별 논리적 분리 |

## Ⅱ. 캡슐화 구조

```text
송신 VM의 내부 Ethernet 프레임
              ↓
       송신 VTEP
              ↓ VNI·VXLAN·UDP/IP 캡슐화
        L3 언더레이
              ↓
       수신 VTEP
              ↓ 역캡슐화
       수신 VM 포트
```

| 필드 | 기능 |
|---|---|
| 내부 Ethernet 프레임 | 테넌트의 원래 L2 데이터 |
| VXLAN 헤더의 VNI | 오버레이 세그먼트 식별 |
| 외부 UDP/IP | 언더레이가 VTEP 간 패킷을 전달할 주소·전송 정보 |

제언: 오버레이 VNI와 언더레이 VTEP 주소·경로를 분리해 관리

---

## 2~4교시 예상문제 (25점)

> VXLAN의 구조와 제어·데이터 평면 동작을 설명하고, 기존 VLAN과 비교하여 구축 시 고려사항을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. VXLAN 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **VXLAN(Virtual eXtensible LAN):** 내부 L2 프레임을 UDP/IP로 캡슐화해 L3 위에 가상 L2 세그먼트를 제공하는 방식 |
| 목적 | 데이터센터 L2 세그먼트의 확장과 테넌트별 논리적 분리 |

## Ⅱ. VTEP 간 캡슐화 동작

```text
테넌트 프레임
    ↓ ingress VTEP
내부 프레임 + VXLAN 헤더(VNI)
    ↓ 외부 UDP/IP 헤더 추가
IP 언더레이 라우팅
    ↓ egress VTEP
외부 헤더 제거·VNI 확인
    ↓ 내부 프레임 전달
대상 테넌트 포트
```

| 추가 헤더 | 역할 | 크기·설계 영향 |
|---|---|---|
| VXLAN | VNI 등 오버레이 정보 | VXLAN 헤더 8 octets |
| UDP/IP | VTEP 주소 사이의 언더레이 전달 | IP 버전·옵션에 따라 크기 상이 |
| 외부 Ethernet | 인접 언더레이 홉 전달 | 실제 L2 구간·태그 구성에 따라 추가 |

기본 VXLAN 헤더는 8 octets이며 전체 캡슐화 오버헤드는 IP 버전·외부 링크 구성에 따라 달라짐. 언더레이 MTU는 실제 패킷 경로의 캡슐화 크기를 수용해야 함

## Ⅲ. VLAN 및 제어 평면 비교

| 구분 | VLAN(802.1Q) | VXLAN 기본 동작 | EVPN 연계 VXLAN |
|---|---|---|---|
| 식별 | 12-bit VLAN ID | 24-bit VNI | VNI와 EVPN 서비스 매핑 |
| 세그먼트 범위 | L2 도메인 | L3 언더레이 위 오버레이 | BGP 제어 평면과 오버레이 |
| 주소 학습 | 브리지 학습 | 기본적으로 데이터 평면 학습·BUM 처리 | MAC/IP 도달 정보를 BGP EVPN으로 배포 |
| 확장 고려 | VLAN·브리지 도메인 운영 | VTEP·언더레이 도달성 | EVPN 정책·경로·멀티호밍 설계 |

EVPN 제어 평면을 쓰더라도 브로드캐스트·unknown unicast·multicast(BUM) 전달 방식은 구성에 따라 별도 설계 대상

## Ⅳ. 구축 고려사항과 통제

| 한계 | 대응 |
|---|---|
| 캡슐화 오버헤드로 경로 MTU 초과 | 종단부터 경로 전체의 MTU·PMTUD 동작 확인 |
| VTEP 주소·VNI 매핑 불일치 | 중앙 할당·구성 검증과 중복 식별자 점검 |
| MAC/IP 학습·BUM 확산 부하 | 토폴로지에 맞춰 flood-and-learn 또는 EVPN 제어 평면과 복제 방식을 설계 |
| 테넌트 경계 설정 오류 | VNI·VRF·정책의 매핑과 교차 테넌트 차단 시험 |

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 세그먼트 수만 늘리면 MTU 불일치와 VNI·경로 정책 오류가 함께 늘어날 수 있음 | VTEP 주소·VNI·VRF 관계를 기준 모델로 관리하고, 파일럿 트래픽으로 경로 MTU와 테넌트 격리를 확인한 뒤 세그먼트 단위로 확장 |

## 출제 이력과 검증 출처

- 제130회 1교시 8번: `VXLAN(Virtual eXtensible LAN)`
- [RFC 7348 — Virtual eXtensible LAN](https://www.rfc-editor.org/rfc/rfc7348)
- [RFC 8365 — A Network Virtualization Overlay Solution Using EVPN](https://www.rfc-editor.org/rfc/rfc8365)
- [RFC 7432 — BGP MPLS-Based Ethernet VPN](https://www.rfc-editor.org/rfc/rfc7432)
- [IANA Service Name and Transport Protocol Port Number Registry — vxlan 4789/udp](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 연결 토픽

- [VLAN](./050_vlan/) · [SDN](./035_sdn/) · [NFV](./001_nfv/)
