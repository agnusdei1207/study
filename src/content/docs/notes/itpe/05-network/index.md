---
sidebar:
  order: 0
title: "정보통신"
description: "네트워크 기본에서 지능형·융합 네트워크까지 이어지는 학습 로드맵"
weight: 5
---

## 8과목 전체 로드맵과 현재 위치

```text
                    [01 IT 경영전략]
               전략·거버넌스·투자·서비스
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
[02 SW 공학]        [03 데이터]       [04 컴퓨터시스템]
개발·품질·PM        DB·분석·AI         CA·OS·알고리즘
       │                 │                 │
       └────────────┬────┴────┬────────────┘
                    ▼         ▼
          [05 네트워크 ◀ 현재 과목] ─── [06 보안]
          연결·전송·이동·제어           보호·복원·신뢰
                    │                    │
                    └─────────┬──────────┘
                              ▼
                    [07 디지털 융합]
                  신기술·플랫폼·서비스
                              │
                              ▼
                    [08 법률·정책·윤리]
                  규제·표준·책임·준거성
```

- 현재 과목 역할: 컴퓨팅·데이터·SW(Software) 서비스를 서로 연결하고, 보안 통제를 적용할 전송·제어 기반을 제공
- 연계 축: `03 데이터의 분산 처리 ↔ 05 네트워크의 지연·대역폭 ↔ 06 보안의 경계·암호·가용성`

## 05 정보통신 확대 지도

```text
                            [네트워크 기본]
                  OSI/TCP-IP · 프로토콜 · 오류/흐름/혼잡제어
                                │
              ┌─────────────────┴─────────────────┐
              ▼                                   ▼
       [유선 네트워크]                       [무선 네트워크]
  Ethernet · VLAN/VXLAN              Wi-Fi · 5G/6G · 위성/NTN
  CIDR/VLSM · 라우팅/QoS             다중접속 · 이동성 · V2X
              │                                   │
              └─────────────────┬─────────────────┘
                                ▼
                    [제어·가상화 기반 서비스화]
                   SDN/OpenFlow · NFV/CNF · IBN
                                │
                                ▼
                       [지능·융합 네트워크]
               AI-RAN · AI Native · SATIN · IoT/Edge
                                │
                                ▼
               가용성 · 지연 · 처리량 · 보안 · 운영자동화
```

선의 의미: 물리·논리 전송 기반 위에 유선·무선 접속망을 구성하고, 제어와 기능을 소프트웨어화하여 지능형 서비스로 확장하는 계층 관계

### 30초 인출

```text
기본 → 유선/무선 → 제어·가상화 → 지능·융합

기본: 계층·프로토콜·오류/흐름/혼잡
유선: CIDR/VLSM·라우팅·QoS·Overlay
무선: Wi-Fi·5G/6G·NTN·다중접속
진화: SDN/NFV → IBN/AI Native
```

- 설계 기준: 주소·경로·대역폭·지연·손실·가용성·보안·관측 가능성을 함께 판단
- 현대화 기준: Classful IPv4(Internet Protocol version 4)는 역사적 한계 설명에만 사용하고, 주소 설계는 **CIDR(Classless Inter-Domain Routing)/VLSM(Variable Length Subnet Mask)·IPv6**(Internet Protocol version 6)를 기준으로 기술

## 영역별 로드맵

| 영역 | 핵심 관계 | 대표 토픽 | 주요 시각화 |
|---|---|---|---|
| **기본 원리** | 계층 간 캡슐화·전달 | OSI(Open Systems Interconnection) 7계층, 프로토콜 요소, 오류·흐름·혼잡제어 | 계층도, 프레임/패킷 흐름 |
| **주소·경로** | 주소 기반 목적지 전달·경로 선택 | CIDR/VLSM, IPv6, 라우팅, NAT(Network Address Translation) | prefix 분할, RIB/FIB 흐름 |
| **품질·운영** | 혼잡·장애에 따른 품질 제어 | QoS(Quality of Service), WFQ, TCP(Transmission Control Protocol) 혼잡제어, CDN(Content Delivery Network) | 큐·윈도우·피드백 루프 |
| **무선·이동** | 공유 매체 접근·이동성 제어 | CSMA/CA, Wi-Fi 7/8, 5G/6G, NTN(Non-Terrestrial Network) | 무선 접속 절차, 다중 링크 |
| **제어·가상화** | 제어 기능 분리·자동화 | SDN(Software-Defined Networking)/OpenFlow, NFV(Network Functions Virtualisation)/CNF, IBN | 제어/데이터 평면, MANO |
| **지능·융합** | AI(Artificial Intelligence)·위성·지상망 폐루프 연계 | AI-RAN(Radio Access Network), AI Native, SATIN, IoT(Internet of Things) | 의도-분석-정책-검증 루프 |

## 전체 키워드 보존과 누적 회독

| 단계 | 의미 | 누적 회독 |
|---|---|---|
| **기초** | 핵심 코어의 기본 개념 | 기초 |
| **서브** | 코어와 함께 이해할 주요 주변 요소 | 기초+서브 |
| **응용** | 코어를 전제로 한 파생·적용 요소 | 기초+서브+응용 |

전체 키워드를 보존하고 회독 범위만 누적 확장한다.

### 대표 토픽 링크

| 번호 | 토픽 | 링크 |
|---:|---|:---:|
| 1 | 위성·공중·지상 통합망 | [보기](./004_satin/) |
| 2 | 라우팅 프로토콜 | [보기](./012_ospf/) |
| 3 | NFV | [보기](./001_nfv/) |
| 4 | 서브네팅·VLSM | [보기](./002_subnetting/) |
| 5 | 오류제어 | [보기](./003_error_control/) |
| 6 | Wi-Fi 7 | [보기](./005_wifi_7/) |
| 7 | WFQ | [보기](./008_wfq/) |
| 8 | TCP 혼잡제어 | [보기](./007_tcp_congestion_control/) |
| 9 | 6G 이동통신 | [보기](./027_6g_mobile_communication/) |
| 10 | 5G 특화망 | [보기](./009_5g_private_network/) |
| 11 | AI-RAN | [보기](./010_ai_ran/) |
| 12 | CSMA/CA | [보기](./011_csma_ca/) |
| 13 | 슬라이딩 윈도우 | [보기](./018_sliding_window/) |
| 14 | SCTP(Stream Control Transmission Protocol) | [보기](./034_sctp/) |
| 15 | Wi-Fi 8 | [보기](./043_ieee_802_11bn/) |

## 일반 학습 원칙

- 패킷과 신호가 계층·상태·테이블·피드백을 거쳐 전달되는 과정을 그림으로 연결한다.
- 최고속도 하나보다 지연, 손실, 가용성, 상호운용성과 운용 조건을 함께 비교한다.
- 표준 번호와 성능 정보는 IEEE(Institute of Electrical and Electronics Engineers)·IETF(Internet Engineering Task Force)·3GPP·ETSI 등 1차 출처로 확인한다.
