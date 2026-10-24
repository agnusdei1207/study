---
title: "IntServ(Integrated Services)"
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

- IntServ(Integrated Services), RSVP(Resource Reservation Protocol), 마이크로 플로우(Micro-flow), 소프트 상태(Soft-State), 수락 제어(Admission Control)
- 보장형 서비스(Guaranteed Service), 통제된 부하 서비스(Controlled-Load Service), DiffServ, MPLS RSVP-TE, TSN(Time-Sensitive Networking), DetNet(Deterministic Networking)

## Ⅰ. IntServ의 개요

- 핵심 요약 : 플로우마다 경로 전체에 자원을 미리 예약하여 절대적 품질을 보장하는 QoS 모델.
- 개념 : 음성과 영상처럼 지연에 민감한 실시간 서비스의 **마이크로 플로우**(Micro-flow)별로 **RSVP**(Resource Reservation Protocol)를 써서 경로 상 모든 라우터에 대역폭과 버퍼를 명시적으로 예약하는 **통합 서비스**(IntServ, Integrated Services) QoS 모델.
- 배경 및 필요성 : 인터넷의 최선형(Best-Effort) 전송은 혼잡 시 패킷을 무차별 폐기하고 지연 변동을 일으켜, 전화망 전용 회선과 같은 결정론적 품질을 보장하기 어려움. 이를 IP 패킷망에서 실현하기 위해 IETF(Internet Engineering Task Force)가 IntServ 구조(RFC 1633)를 정립함.
- 주요 목적 : 플로우별 대역폭 예약과 엄격한 지연 상한 보장, 수락 제어를 통한 과부하 차단, 실시간 품질의 안정적 확보.

## Ⅱ. IntServ의 특징 및 장점

- 핵심 요약 : 예약 시그널링, 수락 제어, 패킷 스케줄링이 결합해 플로우 단위의 보장을 만드는 구조.

1. RSVP 자원 예약 : PATH 메시지로 경로를 파악하고 RESV 메시지로 역방향 경로에 자원을 예약 → 전송 시작 전에 경로 전체의 자원 확보.
2. 보장형 서비스 : 지연 상한과 대역을 수학적으로 보장 → 실시간 음성과 제어 신호의 엄격한 품질 확보.
3. 통제된 부하 서비스 : 한산한 망과 비슷한 수준의 품질을 제공 → 과부하 구간에서도 기본 품질 유지.
4. 수락 제어 : 잔여 자원이 부족하면 신규 예약을 거절 → 기존 플로우의 품질 붕괴 방지.
5. 소프트 상태(Soft-State) : 주기적 갱신이 없으면 예약을 자동 해제 → 중단된 세션의 자원을 신속히 회수.

## Ⅲ. IntServ의 구조 (흐름)

- 핵심 요약 : RSVP 예약 절차로 경로 상태를 세우고, 라우터 내부의 분류기, 스케줄러, 수락 제어가 예약된 자원을 독점 할당하는 구조.

```text
[ RSVP 예약 절차 ]

1. 송신: PATH 메시지 (Tspec 전달)
      ↓ 경로 상 라우터가 상태 저장
2. 수신: RESV 메시지 (Rspec 요청)
      ↑ 역방향 경로를 따라 복귀
3. 라우터: 수락 제어 후 자원 예약
      ↓
4. 송신: 보장된 데이터 전송
```

```text
[ IntServ 라우터 내부 구성 ]

패킷 인입
      ↓
패킷 분류기 (플로우 식별)
      ↓
패킷 스케줄러 (예: 가중 공정 큐잉)
      ↓
출력
  ※ 수락 제어와 RSVP 데몬이 예약 상태 관리
```

- 패킷 스케줄러는 가중 공정 큐잉(WFQ, Weighted Fair Queuing) 같은 방식으로 플로우별 예약 대역을 보장함.

## Ⅳ. IntServ와 DiffServ의 비교

- 핵심 요약 : IntServ는 플로우 단위 절대 보장과 상태 보유를, DiffServ는 클래스 단위 상대 보장과 상태 비보유를 택한 대비 구조.
- 선택 기준 : 노드 수가 적고 절대 보장이 필수인 폐쇄망이면 IntServ, 노드가 많은 공용 백본이면 DiffServ가 적합.

| 비교 축 | IntServ (통합 서비스) | DiffServ (차등 서비스) |
| --- | --- | --- |
| 제어 단위 | 개별 마이크로 플로우 | 클래스 단위 집약 |
| QoS 보증 형태 | 결정론적 절대 보장 | 통계적 상대 보장 |
| 라우터 상태 | 모든 라우터가 플로우별 상태 보유 | 코어 라우터는 상태 비보유 |
| 시그널링 오버헤드 | RSVP 주기 갱신으로 대역폭과 CPU 소모 | 시그널링 없이 헤더 표시만 수행 |
| 핵심 한계 | 대규모 백본에서 확장성 붕괴 | 개별 대역과 지연의 엄격한 보장 불가 |
| 적합한 네트워크 | 소규모 인트라넷, 특수 군용망, 방송망 | 대규모 ISP(Internet Service Provider) 백본, 엔터프라이즈 WAN |

## Ⅴ. IntServ의 한계와 방안

- 핵심 요약 : 상태 폭증, 갱신 메시지 부하, 비대칭 경로의 세 한계를 계층 분리, 갱신 축소, 명시적 터널로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 코어 상태 폭증 | 백본을 통과하는 수많은 플로우마다 버퍼와 타이머를 유지할 수 없어 시스템 과부하 | 코어는 DiffServ로 구축하고 액세스 경계에서만 IntServ를 적용하는 IntServ-over-DiffServ 모델 | 라우터당 플로우 상태 수 |
| 주기 갱신 메시지 부하 | 예약 세션이 많을수록 PATH와 RESV 교환이 늘어 CPU와 제어 대역폭 낭비 | RFC 2961 RSVP 갱신 부하 감소 확장(메시지 묶음, 요약 갱신) 적용 | 제어 메시지 비율, CPU 점유율 |
| 비대칭 라우팅 | 송신과 수신 경로가 달라 한쪽 방향의 예약이 실패하거나 우회됨 | MPLS RSVP-TE로 고정된 양방향 명시적 터널 경로 설정 | 예약 실패율 |

## Ⅵ. IntServ에 대한 기술사적 제언

- 핵심 요약 : 절대 보장이 필수인 폐쇄망에는 IntServ 방식을 한정 적용하고, 공용 백본에는 예약 기반 트래픽 엔지니어링을 결합하는 역할 분담.
- 군 전술망, 항공 관제망, 원전 제어망처럼 노드 수가 제한되고 무손실 전송이 필수인 폐쇄망에는 IntServ와 RSVP의 절대 보장 방식을 적용하는 것이 타당하다.
- ISP 백본에서는 MPLS RSVP-TE로 대역 예약과 고속 우회 경로(FRR, Fast Reroute)를 함께 구성하여 회선 장애 시에도 보장 품질이 유지되도록 설계할 필요가 있다.
- 산업용 실시간 네트워크에서는 시간 민감 네트워킹(TSN, Time-Sensitive Networking)과 결정론적 네트워킹(DetNet, Deterministic Networking) 표준을 우선 검토하여, 지연 보장이 필요한 구간에 표준 기반 설계를 적용하는 것이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : IntServ는 플로우별 절대 보장이라는 기술적 완성도가 높으나, 확장성 한계로 코어 단독 적용은 제한된 모델.
- 시사점 : 현재는 DiffServ 코어, IntServ 경계, 결정론적 표준을 용도에 맞게 조합하는 방식으로 활용되는 것이 현실적.
