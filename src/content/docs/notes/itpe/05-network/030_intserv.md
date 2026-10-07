---
title: "IntServ"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. IntServ의 개요

- 개념 : 실시간 음성, 비디오 등 지연에 민감한 멀티미디어 서비스를 위해 개별 응용 프로그램의 **마이크로 플로우(Micro-flow)** 단위로 송수신 경로 상의 모든 라우터에 자원 예약 프로토콜(RSVP, Resource Reservation Protocol)을 사용하여 필요한 대역폭과 버퍼를 명시적으로 예약하는 **통합 서비스(Integrated Services)** QoS(Quality of Service) 모델.
- 배경 및 필요성 : 인터넷의 기본 패킷 전달 방식인 **최선형(Best-Effort)** 전송은 혼잡 시 무차별 패킷 드롭과 가변 지연을 유발하므로, 기존 전화망(PSTN)의 전용 회선과 같은 결정론적 품질(QoS) 보장을 IP(Internet Protocol) 패킷망에서 실현하기 위해 IETF(RFC(Request for Comments) 1633)가 제정함.
- 핵심 목적 : 플로우별 절대적 대역폭 예약 및 **엄격한 지연 상한(Bound)** 보장, 네트워크 패킷 손실 제로화, 수락 제어(Admission Control)를 통한 네트워크 과부하 원천 차단.

## Ⅱ. IntServ의 핵심 아키텍처 및 동작 메커니즘

IntServ는 **RSVP** 시그널링을 통해 송수신 경로의 모든 라우터에 플로우 상태(Soft-state)를 생성하고, 수락 제어를 통과한 패킷에 대해 패킷 분류기와 스케줄러를 통해 예약된 자원을 독점 할당함.

```text
[ IntServ / RSVP 자원 예약 메커니즘 및 라우터 내부 구조 ]

1. RSVP 자원 예약 시그널링 절차
송신 호스트                      중간 라우터들                    수신 호스트
    │                                │                                │
    │─── RSVP PATH 메시지 ──────────>│─── RSVP PATH 메시지 ──────────>│
    │    (트래픽 특성 Tspec 전달)     │    (역방향 경로 정보 저장)     │ (트래픽 요구 수신)
    │                                │                                │
    │<── RSVP RESV 메시지 ──────────│<── RSVP RESV 메시지 ──────────│
    │    (수락제어 통과 시 자원 예약) │    (Rspec: 대역폭/버퍼 예약)  │ (예약 요청: Rspec)
    │                                │                                │
    │==== 보장된 QoS 데이터 전송 ===>│==== 엄격한 스케줄링 전송 ====>│

2. IntServ 라우터 내부 핵심 구성 요소
+-----------------------------------------------------------------+
| 패킷 인입 ──► [ 패킷 분류기 ] ──► [ 패킷 스케줄러 (WFQ) ] ──► 출력 |
|                     ▲                     ▲                     |
|                     │                     │                     |
|           [ 수락 제어 (Admission) ] [ RSVP 데몬 (Soft-State) ]   |
+-----------------------------------------------------------------+
```

- **RSVP(Resource Reservation Protocol)** : 송신단의 PATH 메시지로 경로를 탐색하고 수신단의 RESV 메시지로 역방향 경로 상의 모든 라우터에 자원을 명시적으로 예약하는 시그널링 프로토콜.
- **보장형 서비스(Guaranteed Service)** : 큐잉 지연이 전혀 발생하지 않도록 수학적으로 증명 가능한 엄격한 지연 한계(Delay Bound)와 대역폭을 엄격히 보장하는 무손실 서비스.
- **통제된 부하 서비스(Controlled-Load Service)** : 네트워크에 부하가 전혀 없는 한산한 상태(Unloaded Network)에서 제공되는 수준의 지연과 패킷 전달율을 제공하는 서비스.
- **수락 제어(Admission Control)** : 라우터에 잔여 자원이 부족할 경우 신규 플로우의 자원 예약 요청을 단호히 거절하여 기존에 수락된 플로우의 서비스 품질 붕괴 방지.
- **소프트 상태(Soft-State)** : 라우터의 예약 상태는 영구적이지 않으며, 주기적인 갱신(Refresh) 메시지가 도착하지 않으면 자동으로 타임아웃되어 자원 회수.

## Ⅲ. IntServ의 세부 구성 요소 및 비교 분석

| 비교 항목 | IntServ (통합 서비스 모델) | DiffServ (차등 서비스 모델) |
|---|---|---|
| 제어 단위 | 개별 마이크로 플로우 단위 (Micro-flow) | 클래스/그룹 단위 집약 (Class-based) |
| QoS 보증 형태 | 결정론적 절대 보장 (Deterministic) | 통계적 상대 보장 (Statistical) |
| 라우터 상태 정보 | 모든 라우터가 플로우별 상태 저장 (Stateful) | 코어 라우터는 상태를 저장하지 않음 (Stateless)|
| 시그널링 오버헤드 | RSVP 주기적 갱신으로 대역폭/CPU(Central Processing Unit) 소모 극심 | 시그널링 불필요 (DSCP 헤더 마킹만 수행) |
| 핵심 한계점 | 대규모 백본망에서 확장성 완전 붕괴 | 엄격한 개별 대역폭/지연 보장 불가 |
| 적합한 네트워크 | 소규모 인트라넷, 특수 군용망, 방송망 | 대규모 ISP(Internet Service Provider) 백본, 엔터프라이즈 WAN(Wide Area Network) |

- IntServ는 기술적으로 완벽한 품질 보증을 제공하지만 코어망의 확장성 한계로 인해 단독 사용이 좌절되었으며, 현대에는 대규모 백본의 DiffServ와 경계의 IntServ를 결합하는 형태로 응용됨.

## Ⅳ. IntServ의 주요 한계점 및 해결 방안

- 코어 라우터의 플로우 상태 정보(State) 폭증에 따른 확장성(Scalability) 한계 :
  - 한계점 : 수십만~수백만 개 플로우가 통과하는 백본 라우터에서 플로우별 버퍼와 타이머 유지가 물리적으로 불가능하여 시스템 붕괴.
  - 해결 방안 : 코어 네트워크는 확장성이 뛰어난 DiffServ로 구축하고 액세스 경계에서만 IntServ를 적용하는 하이브리드 IntServ-over-DiffServ 모델 채택.
- 주기적 RSVP 리프레시 메시지로 인한 제어 평면 트래픽 폭증 :
  - 한계점 : 수천 개의 예약 세션이 매 30초마다 PATH/RESV 메시지를 교환하여 CPU 점유율 및 제어 대역폭 낭비.
  - 해결 방안 : RFC 2961 RSVP Refresh Overhead Reduction 확장(번들 메시지, 요약 리프레시) 적용.
- 비대칭 라우팅(Asymmetric Routing) 환경에서의 예약 경로 불일치 :
  - 한계점 : 송신 경로와 수신 경로가 서로 다른 인터넷 라우팅 특성상 단방향 예약이 실패하거나 우회되는 현상 발생.
  - 해결 방안 : MPLS(Multiprotocol Label Switching) 트래픽 엔지니어링(MPLS RSVP-TE(Traffic Engineering))을 결합하여 고정된 양방향 명시적 터널 경로 확립.

## Ⅴ. IntServ 적용 및 발전을 위한 기술사적 제언

- 특수 미션 크리티컬 폐쇄망(군 전술망, 항공 관제망, 원전 제어망) 한정 적용 : 공용 인터넷이 아닌 노드 수가 제한되고 절대적 무손실 전송이 필수적인 특수 통신망에 IntServ/RSVP 아키텍처 적극 도입 권장.
- MPLS RSVP-TE 기반 코어 백본 대역폭 예약 인프라 운영 : ISP 백본 간 트래픽 엔지니어링 시 회선 장애 대비 사전 우회 경로(FRR: Fast Reroute)를 위한 RSVP-TE 터널링 최적화.
- 차세대 결정론적 네트워킹(TSN & DetNet) 표준으로의 기술적 계승 : IntServ의 절대 지연 보장 철학을 계승하여 L2 IEEE(Institute of Electrical and Electronics Engineers) 802.1 TSN(Time-Sensitive Networking) 및 L3 IETF DetNet(Deterministic Networking) 표준 설계에 반영.
