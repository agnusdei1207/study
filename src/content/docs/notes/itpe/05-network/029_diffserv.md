---
title: "DiffServ(Differentiated Services)"
author: "agnusdei1207"
date: "2026-10-24T22:43:45+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- DiffServ(Differentiated Services), DSCP(Differentiated Services Code Point), PHB(Per-Hop Behavior), EF(Expedited Forwarding), AF(Assured Forwarding), BE(Best Effort)
- QoS(Quality of Service), IntServ(Integrated Services), 경계 라우터, 코어 라우터, WRED(Weighted Random Early Detection), 트래픽 조절

## Ⅰ. DiffServ의 개요

- 핵심 요약 : 경계에서 트래픽에 표시를 붙이고 코어는 표시만 보고 처리하는 클래스 기반의 확장형 QoS 모델.
- 개념 : IP 헤더의 **DS 필드**(Differentiated Services Field)에 **DSCP**(Differentiated Services Code Point) 값을 기록하고, 경계에서 분류한 트래픽을 클래스 단위로 처리하는 **차등 서비스**(DiffServ, Differentiated Services) 기반 QoS(Quality of Service) 보장 모델.
- 배경 및 필요성 : 모든 라우터가 플로우마다 상태를 저장해야 하는 통합 서비스(IntServ, Integrated Services) 방식은 대규모 망에서 확장성이 부족하므로, 상태를 저장하지 않는 클래스 기반 처리가 필요해져 IETF(Internet Engineering Task Force)가 표준화함.
- 주요 목적 : 대규모 백본에서도 확장 가능한 QoS 제공, 음성·영상·데이터의 차등 처리, 코어 라우터의 고속 포워딩 유지.

## Ⅱ. DiffServ의 특징 및 장점

- 핵심 요약 : 경계 분류와 코어의 단순 처리로 역할을 나누어, 상태 부담 없이 확장되는 차등 품질 구조.

1. 에지 분류와 표시 : 5-튜플 기준으로 패킷을 분류한 뒤 DSCP를 기록 → 이후 노드는 헤더만 보고 처리하여 판단 비용 절감.
2. 코어 상태 비보유 : 플로우 정보 없이 DSCP만 판독 → 코어 라우터의 부하가 플로우 수와 무관하여 백본 확장이 용이.
3. 홉별 행위(PHB, Per-Hop Behavior) : EF(Expedited Forwarding)는 저지연 큐(LLQ, Low Latency Queuing)에, AF(Assured Forwarding)는 가중 무작위 조기 폐기(WRED, Weighted Random Early Detection)로 드롭 우선순위를 나눔 → 음성 지연 최소화와 일반 데이터의 공정한 처리.
4. 계약 기반 트래픽 조절 : 미터와 셰이퍼가 서비스 수준 협약(SLA, Service Level Agreement)을 넘는 트래픽을 강등, 지연, 폐기 중 하나로 처리 → 계약한 품질의 준수 근거 확보.

## Ⅲ. DiffServ의 구조 (흐름)

- 핵심 요약 : 경계 라우터에서 분류, 표시, 조절을 마친 패킷만 코어로 보내고, 코어는 표시에 따른 큐잉만 수행하는 두 단계 구조.

```text
[ 에지 → 코어 처리 흐름 ]

인입 패킷
      ↓
경계 라우터 (분류·표시·조절)
      ↓ DSCP 표시
코어 라우터 (DSCP만 판독)
      ↓
클래스별 PHB 실행
      ↓
목적지
```

```text
[ DSCP 클래스와 PHB ]

EF (DSCP 46) → 전용 우선 큐
AF (AF11~AF43) → 3단계 폐기 우선순위
BE (Best Effort, DSCP 0) → 일반 FIFO 큐
```

- DSCP는 IP 헤더의 8비트 중 상위 6비트를 쓰므로 64개의 클래스를 표현하며, 하위 2비트는 혼잡 통지(ECN, Explicit Congestion Notification)에 쓰임.

## Ⅳ. DiffServ, IntServ, Best-Effort의 비교

- 핵심 요약 : DiffServ는 클래스 단위의 상대적 보장을 상태 비보유로 제공하고, IntServ는 플로우 단위의 절대 보장을 상태 보유로 제공하는 대비 구조.

| 비교 축 | DiffServ (차등 서비스) | IntServ (통합 서비스) | Best-Effort (일반 인터넷) |
| --- | --- | --- | --- |
| 제어 단위 | 클래스 단위 집약 | 개별 마이크로 플로우 | 구분 없음 |
| QoS 보장 수준 | 상대적·통계적 차등 보장 | 결정론적 절대 보장 | 보장 없음 |
| 라우터 상태 | 코어는 상태 비보유 | 모든 라우터가 플로우 상태 보유 | 상태 없음 |
| 시그널링 | 사전 시그널링 불필요 | RSVP(Resource Reservation Protocol) 예약 필요 | 없음 |
| 확장성 | 대규모 백본에 적합 | 대규모 망에서 한계 | 제한 없음 |
| 주요 적용 영역 | 엔터프라이즈 망, ISP(Internet Service Provider) 백본 | 폐쇄망, 실시간 방송망 | 공용 인터넷 기본 동작 |

- 선택 기준 : 대규모 망에서 등급별 차등이면 DiffServ, 소규모 폐쇄망에서 절대 보장이 필수이면 IntServ, 품질 보장이 없어도 되면 Best-Effort를 적용.

## Ⅴ. DiffServ의 한계와 방안

- 핵심 요약 : 절대 보장 불가, 도메인 간 표시 소실, 암호화 트래픽의 식별 한계를 경로 예약, 사업자 간 계약, 응용 단 표시로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 절대 보장 불가 | 전체 트래픽이 동시에 몰리면 AF 클래스도 지연과 손실을 막지 못함 | MPLS 트래픽 엔지니어링(MPLS-TE, Multiprotocol Label Switching Traffic Engineering)과 결합해 경로별 대역 사전 예약 | 클래스별 지연, 손실률 |
| 도메인 간 표시 소실 | 타 사업자 경계에서 DSCP가 0으로 재표시되어 종단 간 품질 단절 | 사업자 간 SLA 협약과 이더넷 802.1p CoS, MPLS EXP 필드의 표준 매핑 준수 | 경계별 DSCP 재표시율 |
| 암호화 트래픽 식별 불가 | HTTPS(Hypertext Transfer Protocol Secure) 확산으로 심층 패킷 검사(DPI, Deep Packet Inspection)가 응용을 식별하기 어려움 | 응용 단에서 직접 DSCP를 표시하고, 흐름 통계 기반의 분류 적용 | 미분류 트래픽 비율 |

## Ⅵ. DiffServ에 대한 기술사적 제언

- 핵심 요약 : 무손실이 필요한 데이터센터 트래픽, 기업 WAN, 코어 혼잡 제어를 각각 분리된 설계 원칙으로 운영하는 방향.
- AI 분산 학습처럼 손실에 민감한 데이터센터 트래픽에는 RoCE(RDMA over Converged Ethernet) 전용 DSCP 클래스를 두고 PFC(Priority Flow Control) 우선순위와 일대일로 대응시키는 설계가 필요하다.
- 코어 백본의 WRED 임계치는 드롭 우선순위별로 차등 설정하여 TCP(Transmission Control Protocol)의 전역 동기화를 막는 방향으로 튜닝할 필요가 있다.
- 기업 WAN에서는 소프트웨어 정의 광역 네트워크(SD-WAN, Software-Defined Wide Area Network) 오버레이가 애플리케이션을 식별해 DSCP를 부여하고 회선 품질에 따라 경로를 고르도록 도입을 검토하는 것이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : DiffServ는 상태 비보유 코어와 클래스 기반 표시로 QoS를 확장 가능하게 만든 표준 모델.
- 시사점 : 절대 보장은 어려우므로, 계약과 경로 설계를 함께 운영해야 체감 품질이 유지됨.
