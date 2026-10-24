---
title: "프레임릴레이(Frame Relay)"
author: "agnusdei1207"
date: "2026-10-24T22:50:25+09:00"
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

- 프레임릴레이(Frame Relay), X.25, MPLS(Multiprotocol Label Switching), SD-WAN(Software-Defined WAN)
- DLCI(Data Link Connection Identifier), 가상 회선(Virtual Circuit), CIR(Committed Information Rate), EIR(Excess Information Rate)
- FECN, BECN, DE(Discard Eligibility), LMI(Local Management Interface)
- 홉 바이 홉(Hop-by-Hop), 엔드투엔드 원칙(End-to-End Argument), 혼잡 제어

## Ⅰ. 프레임릴레이의 개요

- 핵심 요약 : 종단 중심의 오류 제어로 오버헤드를 줄인 L2 기반 고속 패킷 WAN 프로토콜.
- 개념 : 기존 X.25의 무거운 오류 제어와 흐름 제어를 줄여, 신뢰성 높은 디지털 회선 위에서 패킷을 빠르게 교환하는 데이터 링크 계층 기반 **광역 통신망** (WAN, Wide Area Network) 프로토콜이다. 표준은 ITU(International Telecommunication Union)-T의 I.122와 Q.922에 정의된다.
- 배경 및 필요성 : X.25는 잡음이 많던 아날로그 회선을 전제로 노드마다 **홉 바이 홉** (Hop-by-Hop, 구간마다 오류를 확인하고 재전송하는 방식) 검사를 수행했다. 이 검사가 노드마다 지연을 쌓아 전송 속도를 떨어뜨렸으므로, 전송 매체 품질이 좋아진 1990년대 이후에는 검사 기능을 종단으로 넘기는 방식이 요구되었다.
- 주요 목적 : WAN 데이터 전송의 오버헤드 최소화, 단일 물리 회선에 여러 **가상 회선** (Virtual Circuit) 다중화, 지사 간 저비용 메시 망 구축.

## Ⅱ. 프레임릴레이의 특징 및 장점

- 핵심 요약 : 헤더 기반 가상 회선 다중화와 명시적 혼잡 통보가 회선 절감과 핵심 트래픽 보호로 이어지는 구조.

1. 가상 회선 다중화 : **DLCI** (Data Link Connection Identifier, 10비트 가상 회선 식별자)로 한 인터페이스에 여러 PVC(Permanent Virtual Circuit) 또는 SVC(Switched Virtual Circuit)를 수용 → 지점별 물리 회선 수 절감.
2. 종단 오류 제어 : 손상된 프레임은 스위치가 즉시 폐기하고, 복구와 흐름 제어는 종단의 TCP(Transmission Control Protocol)가 담당 → 노드 처리 지연 감소.
3. 명시적 혼잡 통보 : **FECN** (Forward Explicit Congestion Notification, 수신 방향 혼잡 통보), **BECN** (Backward Explicit Congestion Notification, 송신 방향 혼잡 통보) 비트로 혼잡을 알림 → 송신측이 전송률을 낮출 근거 확보.
4. 대역 보장과 초과 허용 : **CIR** (Committed Information Rate, 평상시 보장 대역)과 **EIR** (Excess Information Rate, 여유 있을 때 초과 전송 가능한 대역)으로 나눔 → 보장 대역 기준의 비용 예측 가능.

```text
[ 프레임 구조 ]

Flag | 헤더 2B | 사용자 데이터 | FCS 2B | Flag
   ↓ 헤더 내부
DLCI 상위 6비트 | C/R | EA
DLCI 하위 4비트 | FECN | BECN | DE | EA
```

## Ⅲ. 프레임릴레이의 구조 (흐름)

- 핵심 요약 : 프레임 헤더의 DLCI로 경로를 정하고, 혼잡 비트가 종단으로 전파되어 송신을 조절하는 흐름.
- **관리 인터페이스** (LMI, Local Management Interface) : 라우터(DTE)와 프레임릴레이 스위치(DCE) 사이에서 PVC의 상태(Active, Inactive, Deleted)를 동기화하고 Keepalive를 유지하는 관리 규격.
- DE 비트 : 혼잡 시 스위치가 우선 폐기할 수 있는 프레임임을 표시하며, EIR 구간 초과 트래픽에 DE=1을 설정한다.

```text
[ 혼잡 통보 흐름 ]

스위치에서 혼잡 감지
   ↓ FECN 설정 (순방향 프레임)
수신측이 상위 계층에 혼잡 통보
   ↓ BECN 설정 (역방향 프레임)
송신측이 전송률 감축
```

```text
[ 혼잡 시 폐기 순서 ]

1. DE=1 프레임 (EIR 초과 트래픽) 우선 폐기
   ↓ 여전히 혼잡하면
2. 일반 프레임 폐기 → 종단 TCP가 재전송
```

## Ⅳ. X.25, 프레임릴레이, MPLS 비교

- 핵심 요약 : 세 기술은 오류 제어 위치와 식별자 방식이 달라, 프레임릴레이는 X.25와 MPLS의 중간 단계에 해당한다.

| 비교 항목 | X.25 | 프레임릴레이 | MPLS (Multiprotocol Label Switching) |
| --- | --- | --- | --- |
| 동작 계층 | L3 (네트워크 계층) | L2 (데이터 링크 계층) | L2.5 (레이블 스위칭) |
| 오류 제어 | 노드 간 홉 단위 검사 | 오류 프레임 폐기, 복구는 종단 담당 | 하드웨어 기반 빠른 포워딩 |
| 혼잡 제어 | 홉 단위 윈도우 흐름 제어 | FECN, BECN 명시적 통보 | RSVP-TE (Traffic Engineering) 경로 설계, QoS |
| 주요 식별자 | LCN (Logical Channel Number) | DLCI (10비트) | 20비트 MPLS 레이블 |
| 최대 속도 | 저속 회선 중심 | E1·T1급에서 T3급 수준 | 초고속 백본급 |
| 현재 위상 | 사실상 퇴역 | MPLS 및 SD-WAN으로 대체 | 통신사 백본의 주요 기술 |

- 선택 기준 : 과거 레거시 회선 유지보수가 필요한지, 신규 망을 짓는지에 따라 기술을 구분하며, 신규 구축에는 MPLS 또는 SD-WAN을 검토한다.

## Ⅴ. 프레임릴레이의 한계와 방안

- 핵심 요약 : 혼잡 시 실시간 트래픽 품질 보장 불가와 전용선 비용 과다가 퇴출의 핵심 원인이며, 품질 보장 기술과 SD-WAN 전환으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| EIR 구간의 폐기와 지터 불안정 | 망 혼잡 시 DE=1 트래픽이 폐기되어 VoIP(Voice over Internet Protocol) 음성 끊김 발생 | 대역 보장과 우선순위 큐잉을 지원하는 ATM(Asynchronous Transfer Mode) 또는 DiffServ 기반 IP-VPN(Virtual Private Network)으로 전환 | 패킷 손실률, 지터 |
| 전용선 중심의 높은 회선 비용 | 전용 회선 계약 구조로 인터넷 회선 대비 대역폭당 비용 과다 | 저가 인터넷 회선을 묶어 암호화 오버레이를 구성하는 SD-WAN(Software-Defined WAN) 도입 | 대역폭당 월 비용, 회선 가용률 |

## Ⅵ. 프레임릴레이 적용 및 발전을 위한 기술사적 제언

- 핵심 요약 : 레거시 회선은 SD-WAN으로 옮기고, 보장 대역 사상은 클라우드 설계에 반영하는 방향.

1. 레거시 회선의 SD-WAN 전환을 단계적으로 추진한다. 공공·금융 및 해외 지사에 남은 프레임릴레이와 구형 전용회선은 제로터치 프로비저닝(ZTP, Zero-Touch Provisioning)과 IPsec(Internet Protocol Security) 터널을 지원하는 패브릭으로 옮겨야 한다.
2. 클라우드 네트워크 설계에 CIR과 EIR의 사상을 적용한다. 보장 대역과 버스트 대역을 나누는 방식을 클라우드 전용 연결의 대역폭 제어와 버스트 정책 설계에 반영하는 것이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : 프레임릴레이는 신뢰성 높은 회선에서 하위 계층 제어를 줄이는 방식이 성능을 높인다는 엔드투엔드 원칙을 보여준 기술.
- 시사점 : 보장 대역과 혼잡 통보의 설계 사상은 이후 MPLS와 SD-WAN의 품질 제어로 이어졌으며, 현재는 레거시 회선을 정리하는 단계에 있다.
