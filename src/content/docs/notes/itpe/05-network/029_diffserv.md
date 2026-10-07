---
title: "DiffServ"
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

## Ⅰ. DiffServ의 개요

- 개념 : IP(Internet Protocol) 패킷 헤더의 DS(Differentiated Services) 필드(IPv4 ToS, IPv6 Traffic Class)에 6비트 **DSCP** 값을 마킹하고, 네트워크 경계 라우터에서 트래픽을 분류/감시한 후 코어 라우터에서는 개별 플로우 상태 유지 없이 클래스 기반의 단순한 홉별 동작(PHB)을 적용하는 확장성 높은 **QoS(Quality of Service) 보장** 모델.
- 배경 및 필요성 : 모든 라우터가 플로우별 상태를 저장해야 했던 기존 **IntServ(통합 서비스)** 방식의 치명적인 확장성(Scalability) 한계를 극복하고, 대규모 인터넷 백본 및 기업망에서 복잡한 시그널링 없이 차등화된 서비스 품질을 제공하기 위해 IETF(Internet Engineering Task Force)에서 제정함.
- 핵심 목적 : 대규모 네트워크 백본에서의 무제한적 QoS 확장성(Scalability) 확보, 트래픽 특성별(음성, 화상, 데이터) 차등 서비스 제공, 코어 라우터의 고속 포워딩 성능 유지.

## Ⅱ. DiffServ의 핵심 아키텍처 및 동작 메커니즘

DiffServ는 도메인 경계 라우터(Edge)에서 패킷을 분류(Classify), 마킹(Mark), 셰이핑(Shape)하고, 내부 코어 라우터(Core)는 오직 헤더의 DSCP 값에 따라 정의된 PHB 규칙으로 단순 고속 처리함.

```text
[ DiffServ 아키텍처 및 에지-코어 처리 메커니즘 ]

[ DiffServ 도메인 인입 트래픽 ]
              │
              ▼
+-----------------------------------------------------------------+
| 경계 라우터 (Edge Router): 트래픽 프로파일링 및 컨디셔닝         |
|  1. 분류기 (Classifier): 5-Tuple 기반 패킷 분류                 |
|  2. 마커 (Marker): DS 필드에 DSCP 값 기록 (EF, AF, BE)          |
|  3. 미터 (Meter) & 폴리서/셰이퍼 (Policer/Shaper): 속도 초과 제어|
+---------------------------------│────────────────---------------+
                                  │ (DSCP 마킹된 패킷 송출)
                                  ▼
+-----------------------------------------------------------------+
| 코어 라우터 (Core Router): 플로우 상태 비보유 (Stateless 고속)  |
|  - 헤더의 6비트 DSCP만 판독하여 사전에 약속된 PHB 실행:        |
|    * EF (Expedited Forwarding: DSCP 46) -> LLQ 최우선 큐잉      |
|    * AF (Assured Forwarding: AF11~43)   -> WRED 차등 드롭       |
|    * BE (Best Effort: DSCP 0)           -> FIFO 일반 큐잉       |
+-----------------------------------------------------------------+
```

- **DS 필드 및 DSCP(DS Codepoint)** : IP 헤더의 8비트 공간 중 상위 6비트를 사용하여 총 64개의 서비스 클래스를 정의(하위 2비트는 ECN(Explicit Congestion Notification) 혼잡 통지로 활용).
- **에지 트래픽 컨디셔너(Traffic Conditioner)** : 경계 라우터에서 패킷을 분류하고 SLA(Service Level Agreement) 계약을 초과한 트래픽에 대해 마킹 강등(Remarking), 지연 버퍼링(Shaping), 또는 즉시 폐기(Policing) 수행.
- **EF(Expedited Forwarding) PHB** : DSCP 값 46(101110)을 사용하며, 전용 대역폭 보장, 극저지연, 최소 손실을 제공하여 가상 전용선(Leased-line) 품질 구현(VoIP(Voice over Internet Protocol) 음성 전용).
- **AF(Assured Forwarding) PHB** : 4개의 독립 클래스와 클래스별 3단계 드롭 우선순위(Drop Precedence)를 조합하여 총 12개 등급으로 세분화된 대역폭 보장(WRED 결합).
- **BE(Best Effort) PHB** : DSCP 값 0으로 일반적인 인터넷 기본 트래픽 처리.

## Ⅲ. DiffServ의 세부 구성 요소 및 비교 분석

| 비교 항목 | DiffServ (차등 서비스) | IntServ (통합 서비스) | Best-Effort (일반 인터넷) |
|---|---|---|---|
| 기본 철학 | 클래스 기반 차등 처리 (Class-based) | 마이크로 플로우 단위 예약 (Flow-based) | 모든 패킷을 차별 없이 동등 처리 |
| QoS 보장 수준 | 상대적/통계적 품질 차등 보장 | 수학적으로 엄격한 절대적 대역 보장 | QoS 보장 전혀 없음 |
| 상태 유지 (State) | 코어 라우터 상태 비유지 (Stateless) | 모든 라우터가 플로우 상태 저장 | 상태 유지 없음 |
| 시그널링 프로토콜 | 사전 시그널링 불필요 | RSVP(Resource Reservation Protocol) 프로토콜 사전 예약 필수 | 없음 |
| 네트워크 확장성 | 매우 뛰어남 (백본망 적합) | 극히 취약 (대규모 망 적용 불가) | 무한 확장 가능 |
| 주요 적용 영역 | 대규모 엔터프라이즈, ISP(Internet Service Provider) 백본 | 특수 폐쇄망, 실시간 방송망 | 공용 인터넷 기본 동작 |

- DiffServ는 엄격한 종단 간 절대 보장을 일부 양보하는 대신, 코어 라우터의 상태 유지 오버헤드를 제로화하여 대규모 인터넷 및 엔터프라이즈 인프라의 표준 QoS 모델로 자리잡음.

## Ⅳ. DiffServ의 주요 한계점 및 해결 방안

- 엔드-투-엔드(End-to-End) 절대적 자원 예약 불가에 따른 통계적 다중화 한계 :
  - 한계점 : 전체 망에 트래픽이 동시 폭증할 경우 AF 클래스조차 지연시간과 패킷 드롭을 완전히 방어하지 못함.
  - 해결 방안 : DiffServ와 트래픽 엔지니어링(MPLS(Multiprotocol Label Switching)-TE(Traffic Engineering) 또는 SR-TE)을 결합하여 명시적 경로 대역폭 사전 예약 병행.
- 이종 도메인(ISP 간) 통과 시 DSCP 값 재설정(Bleaching/Remarking) :
  - 한계점 : 타 통신사망을 경유할 때 경계 라우터가 임의로 DSCP 값을 0(Best Effort)으로 덮어써 E2E(End-to-End) QoS 단절.
  - 해결 방안 : 사업자 간 상호 연동 SLA 협약 체결 및 이더넷 802.1p CoS / MPLS EXP 필드와의 표준 매핑 테이블 준수.
- 암호화 트래픽(HTTPS(Hypertext Transfer Protocol Secure)/QUIC) 증가에 따른 L7 심층 패킷 분류(DPI, Deep Packet Inspection) 무력화 :
  - 한계점 : 페이로드가 암호화되어 경계 라우터가 애플리케이션 유형을 식별하여 정확한 DSCP를 부여하기 어려움.
  - 해결 방안 : 애플리케이션 엔드포인트 자체 마킹 강제 및 AI(Artificial Intelligence)/ML(Machine Learning) 기반 패킷 통계적 행동 분석(Flow Analysis) 적용.

## Ⅴ. DiffServ 적용 및 발전을 위한 기술사적 제언

- 엔터프라이즈 SD-WAN(Software-Defined Wide Area Network) 오버레이와의 결합을 통한 애플리케이션 인지 QoS 수립 : SaaS, VoIP, ERP(Enterprise Resource Planning) 트래픽을 지능적으로 분류하여 회선 품질(회선 지연, 패킷 손실)에 따라 최적의 MPLS/인터넷 터널로 자동 조향.
- 데이터센터 Clos 패브릭 내 RoCE(Remote Direct Memory Access over Converged Ethernet) v2 무손실 DSCP(DSCP 24/26) 매핑 표준화 : AI 분산 학습 클러스터의 패킷 드롭 방지를 위해 RoCE v2 트래픽에 DSCP를 부여하고 스위치 PFC(Priority Flow Control) 큐와 1:1 매핑 권장.
- 코어 백본 WRED(Weighted Random Early Detection) 프로파일 최적화 : AF 드롭 우선순위별로 최소/최대 임계치를 정교하게 차등 설정하여 TCP(Transmission Control Protocol) 전역 동기화(Global Synchronization) 방지.
