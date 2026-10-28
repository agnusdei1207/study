---
title: "프레임릴레이(Frame Relay)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  question_no: "064"
  keyword_grade: "응용"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- 프레임릴레이(Frame Relay), X.25, MPLS(Multiprotocol Label Switching), SD-WAN(Software-Defined WAN)
- DLCI(Data Link Connection Identifier), 가상 회선(Virtual Circuit), CIR(Committed Information Rate), EIR(Excess Information Rate)
- FECN, BECN, DE(Discard Eligibility), LMI(Local Management Interface)
- 홉 바이 홉(Hop-by-Hop), 혼잡 제어

## Ⅰ. 프레임릴레이의 개요

- 핵심 요약 : 종단 중심의 오류 제어로 중간 노드의 부담을 줄인 데이터 링크 계층 기반의 고속 패킷 교환 광역망 기술.
- 개념 : 신뢰성 높은 디지털 회선 위에서 프레임 단위로 데이터를 교환하는 **프레임릴레이**(Frame Relay) WAN(Wide Area Network) 프로토콜이며, ITU-T(International Telecommunication Union Telecommunication Standardization Sector)의 I.122와 Q.922 권고에 근거.
- 배경 및 필요성 : 선행 기술 X.25는 잡음이 많던 아날로그 회선을 전제로 노드마다 **홉 바이 홉**(구간마다 오류를 확인하고 재전송하는 방식, Hop-by-Hop) 오류 제어를 수행해 지연이 누적되었고, 디지털 전송 품질이 좋아진 환경에서는 노드별 오류 제어가 과잉 기능이 됨.
- 주요 목적 : 광역 전송의 오버헤드 최소화, 단일 물리 회선에 여러 가상 회선의 다중화, 지사 간 저비용 망 구축.

## Ⅱ. 프레임릴레이의 특징 및 장점

- 핵심 요약 : 헤더 기반 가상 회선 다중화와 명시적 혼잡 통보가 회선 절감과 핵심 트래픽 보호로 이어지는 구조.

1. 가상 회선 다중화 : **DLCI**(10비트 가상 회선 식별자, Data Link Connection Identifier)로 인터페이스당 다수의 **PVC**(영구 가상 회선, Permanent Virtual Circuit)와 **SVC**(교환 가상 회선, Switched Virtual Circuit)를 수용 → 지사별 물리 회선 수 절감.
2. 종단 오류 제어 : 스위치는 손상 프레임의 폐기만 수행하고 복구와 흐름 제어는 종단의 TCP(Transmission Control Protocol)가 담당 → 노드 처리 지연 감소.
3. 명시적 혼잡 통보 : **FECN**(순방향 혼잡 통보 비트, Forward Explicit Congestion Notification)과 **BECN**(역방향 혼잡 통보 비트, Backward Explicit Congestion Notification)으로 혼잡을 알림 → 송신률 조절의 근거 제공.
4. 대역 보장과 초과 허용 : **CIR**(보장 정보율, Committed Information Rate)과 **EIR**(초과 정보율, Excess Information Rate)의 이원화 → 보장 대역 기준의 비용 예측성과 여유 시 버스트 유연성 확보.

## Ⅲ. 프레임릴레이의 구조 (흐름)

- 핵심 요약 : 헤더의 DLCI로 경로를 정하고, 혼잡 비트가 종단으로 전파되어 송신을 조절하는 흐름.
- LMI(Local Management Interface) : 라우터(DTE, Data Terminal Equipment)와 프레임릴레이 스위치(DCE, Data Circuit-terminating Equipment) 사이에서 가상 회선 상태를 동기화하고 Keepalive를 유지하는 관리 규격.
- DE(Discard Eligibility) : 혼잡 시 스위치가 우선 폐기할 수 있는 프레임임을 표시하는 비트로, EIR 구간의 초과 트래픽에 설정.

```text
[ 프레임 구조 ]

Flag
    ↓
헤더 (DLCI · FECN · BECN · DE)
    ↓
사용자 데이터
    ↓
FCS (Frame Check Sequence)
    ↓
Flag
```

```text
[ 혼잡 통보 흐름 ]

스위치의 혼잡 감지
    ↓ FECN 설정 (순방향 프레임)
수신측의 혼잡 인지
    ↓ BECN 설정 (역방향 프레임)
송신측의 전송률 감축
```

## Ⅳ. X.25, 프레임릴레이, MPLS의 비교

- 핵심 요약 : 오류 제어 위치와 식별자 방식의 차이로 세 기술은 발전 단계를 이루며, 프레임릴레이는 X.25와 MPLS의 중간 단계.

| 비교 항목 | X.25 | 프레임릴레이 | MPLS(Multiprotocol Label Switching) |
| --- | --- | --- | --- |
| 동작 계층 | 네트워크 계층(L3) | 데이터 링크 계층(L2) | 레이블 스위칭(L2.5) |
| 오류 제어 | 노드 간 홉 단위 검사 | 오류 프레임 폐기, 복구는 종단 담당 | 하드웨어 기반 빠른 포워딩 |
| 혼잡 제어 | 홉 단위 윈도우 흐름 제어 | FECN·BECN 명시적 통보 | 트래픽 엔지니어링과 QoS |
| 주요 식별자 | 논리 채널 번호(LCN) | DLCI(10비트) | 20비트 MPLS 레이블 |
| 현재 위상 | 사실상 퇴역 | MPLS·SD-WAN으로 대체 | 통신사 백본의 주요 기술 |

- 선택 기준 : 레거시 회선의 유지보수 여부에 따라 X.25·프레임릴레이를 구분하고, 신규 광역망 구축은 MPLS 또는 SD-WAN(Software-Defined WAN)을 검토.
- 전환 판단 : 대역 보장과 품질 구분이 필요하면 MPLS, 비용 효율과 유연성이 우선이면 인터넷 회선 기반 SD-WAN이 유리.

## Ⅴ. 프레임릴레이의 한계와 방안

- 핵심 요약 : 혼잡 시 실시간 트래픽 품질 보장 불가와 전용선 비용 과다가 퇴출의 핵심 원인이며, 품질 보장 기술과 대체망 전환으로 일대일 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 혼잡 구간의 폐기와 품질 불안정 | 망 혼잡 시 DE=1 트래픽 폐기로 음성 등 실시간 서비스 품질 저하 | 대역 보장과 우선순위 큐잉을 지원하는 IP-VPN(Virtual Private Network) 등 품질 보장형 서비스로 전환 | 패킷 손실률, 지터 |
| 전용선 중심의 높은 회선 비용 | 전용 회선 계약 구조로 인터넷 회선 대비 대역폭당 비용 과다 | 저가 인터넷 회선을 묶어 암호화 오버레이를 구성하는 SD-WAN 도입 | 대역폭당 월 비용, 회선 가용률 |

## Ⅵ. 프레임릴레이 자산 정리를 위한 기술사적 제언

- 핵심 요약 : 레거시 회선의 단계적 전환과 보장 대역 설계 사상의 계승으로 기술 전환을 정리하는 것.

1. 공공·금융 기관과 다국적 기업은 남은 프레임릴레이·구형 전용회선을 제로터치 프로비저닝(ZTP, Zero-Touch Provisioning)과 IPsec(Internet Protocol Security) 터널을 지원하는 패브릭으로 단계 전환하는 계획을 수립해야 한다.
2. 네트워크 설계 조직은 보장 대역과 버스트 대역을 나누는 CIR·EIR의 사상을 클라우드 전용 연결의 대역폭 제어와 버스트 정책 설계에 반영하는 방안을 검토해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 프레임릴레이는 신뢰성 높은 회선에서 하위 계층 제어를 줄이는 방식이 성능을 높인다는 원칙을 보여준 기술.
- 보장 대역과 혼잡 통보의 설계 사상은 이후 MPLS와 SD-WAN의 품질 제어로 이어졌으며, 현재는 레거시 자산을 정리하는 단계에 있음.
