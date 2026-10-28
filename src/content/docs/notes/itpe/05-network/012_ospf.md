---
title: "OSPF(Open Shortest Path First)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "012"
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- OSPF, 링크 상태, LSA, LSDB, SPF, 다익스트라 알고리즘
- 영역(Area), 백본 영역(Area 0), ABR, ASBR, DR/BDR, Hello 패킷, 수렴
- RIP, BGP, IGP, 거리 벡터, BFD, OSPFv3

## Ⅰ. OSPF의 개요

- 핵심 요약 : 자율 시스템 내부에서 링크 상태를 전파해 동일한 지도를 만들고 최단 경로를 계산하는 대규모 내부망용 라우팅 프로토콜.
- 개념 : 하나의 자율 시스템(AS, Autonomous System) 내에서 링크 상태 정보를 플러딩하고 다익스트라 알고리즘으로 최단 경로를 계산하는 **OSPF** (Open Shortest Path First) 라우팅 프로토콜이며, IETF(Internet Engineering Task Force) 표준의 내부 게이트웨이 프로토콜(IGP, Interior Gateway Protocol)로 RFC 2328에 정의됨.
- 배경 및 필요성 : 거리 벡터(Distance-Vector) 방식의 RIP(Routing Information Protocol)는 최대 15홉 제한, 느린 수렴, 대역폭 무시의 한계로 수백 대 이상의 대형 망을 감당하기 어려움.
- 주요 목적 : 루프 없는 최단 경로 계산, 링크 변화 시의 빠른 재수렴, 영역 분할 기반의 확장성 확보.

## Ⅱ. OSPF의 특징 및 장점

- 핵심 요약 : 동일 토폴로지 동기화, 최단 경로 계산, 영역 계층화, 대표 라우터 선출이 빠른 수렴과 확장성을 함께 만드는 구조.

1. 링크 상태 플러딩 : 각 라우터가 인터페이스·코스트·이웃 정보를 **LSA**(Link-State Advertisement)로 만들어 전파 → 영역 내 모든 라우터가 동일한 **LSDB**(Link-State Database)를 보유하는 루프 없는 계산의 전제.
2. 최단 경로 계산 : 다익스트라 기반의 **SPF**(Shortest Path First) 알고리즘으로 링크 코스트 합이 최소인 경로 트리 생성 → 대역폭을 반영한 경로 선택.
3. 계층적 영역 설계 : 일반 영역을 **백본 영역**(Area 0, 전체 영역을 관통하는 중심 영역)에 직접 연결하고 **ABR**(Area Border Router, 영역 경계 라우터)이 영역 간 경로를 요약 전달 → 라우팅 정보 집약과 연산 범위 축소.
4. 대표 라우터 선출 : 브로드캐스트 구간에서 **DR/BDR**(Designated Router/Backup Designated Router)을 선출해 인접 관계의 폭증 억제 → 수렴 부하 감소.
5. Hello 기반 이웃 관리 : **Hello 패킷**(이웃 발견·유지용 주기 메시지)의 교환으로 이웃 발견과 장애 감지를 수행하고 인증을 결합 → 안정적인 인접 유지.

## Ⅲ. OSPF의 구조 (흐름)

- 핵심 요약 : 백본 중심의 영역 계층과 Hello부터 완전 인접까지의 상태 전이 절차.

```text
[ 계층적 영역 구조 ]

일반 영역 (Area 1·2 ...)
   ↓  ABR의 경로 요약 전달
백본 영역 (Area 0)
   ↓  ASBR 경유의 외부 경로 연동
외부 자율 시스템 (BGP 연동)
```

```text
[ 인접 관계 상태 전이 ]

Down → Init → 2-Way
   ↓  브로드캐스트 구간이면 DR/BDR 선출
ExStart → Exchange → Loading
   ↓  LSDB 동기화 완료
Full (완전 인접)
```

- 수렴 절차 : Hello로 이웃을 발견하고 LSA 교환으로 LSDB를 맞춘 뒤 SPF 계산으로 라우팅 테이블을 구성하는 순서의 수렴 과정.
- **ASBR**(Autonomous System Boundary Router, 외부 경로를 연동하는 경계 라우터) : 외부 자율 시스템의 경로를 OSPF 영역으로 가져오는 구성요소.

## Ⅳ. OSPF와 RIP·BGP의 비교

- 핵심 요약 : 내부 최단 경로는 OSPF, 소규모 단순 망은 RIP, 자율 시스템 간 정책 라우팅은 BGP가 담당하는 역할 분담.
- 비교 대상 : 링크 상태형 IGP인 OSPF, 거리 벡터형 IGP인 RIP, 경로 벡터형 외부 게이트웨이 프로토콜인 **BGP**(Border Gateway Protocol).

| 비교 축 | OSPF | RIP | BGP |
| --- | --- | --- | --- |
| 분류 | 링크 상태형 IGP | 거리 벡터형 IGP | 경로 벡터형 EGP(External Gateway Protocol) |
| 메트릭 | 링크 코스트 (대역폭 기반) | 홉 수 (최대 15홉) | AS-Path 등 복합 속성 |
| 알고리즘 | 다익스트라 SPF | 벨만-포드(Bellman-Ford) | 최적 경로 선택 절차 |
| 수렴 | LSA 전파로 빠른 재수렴 | 주기적 전체 테이블 교환으로 느림 | 정책 중심으로 느린 편 |
| 적용 규모 | 대규모 기업망·데이터센터 | 소규모 망 | 인터넷 백본·AS 간 연동 |

- 선택 기준 : 같은 기관 내부의 경로 결정은 OSPF가 기본이고, 기관 간 연결에는 BGP를 두며 RIP은 규모가 작은 망으로 한정하는 운영이 표준적.

## Ⅴ. OSPF의 한계와 방안

- 핵심 요약 : 재계산 부하, 대표 라우터 전환 지연, 백본 분할을 타이머 통제·감지 연동·논리 연결로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 링크 플래핑 시 재계산 폭증 | 반복 LSA 플러딩 → SPF 재실행과 CPU 부하 | SPF 스로틀 타이머 적용과 영역 분할·경로 요약 | SPF 실행 횟수, CPU 사용률 |
| DR 전환 시의 수렴 지연 | DR 장애 후 BDR 승격 절차에서 대기 발생 | 점대점 모드 전환과 양방향 포워딩 감지(BFD, Bidirectional Forwarding Detection) 연동 | 장애 감지 시간 |
| 백본 영역 분할 위험 | Area 0 분단 시 영역 간 경로 마비 | Virtual-Link 논리 연결과 백본 물리 이중화 | 백본 연결 상태 |

## Ⅵ. OSPF에 대한 기술사적 제언

- 핵심 요약 : 역할 분리 설계, 표준 설정 템플릿, IPv6 전환 대응의 상위 운영 전략 필요.
- 설계 : 데이터센터 네트워크 조직은 Clos 구조의 언더레이에 OSPF를 두고 오버레이 제어는 EVPN(Ethernet VPN) 기반 BGP에 맡기는 역할 분리 권장.
- 운영 : 망 운영 조직은 서비스 등급별 타이머·코스트 값을 표준 템플릿으로 관리해 현장 설정 편차를 제거하는 체계 구축.
- 전환 : IPv6(Internet Protocol version 6) 도입 조직은 OSPFv3의 주소 패밀리(Address Family) 기능으로 IPv4·IPv6 라우팅의 단일 프로세스 운영 검토 권장.

## Ⅶ. 결론

- 핵심 요약 : OSPF는 링크 상태 동기화와 SPF 계산, 영역 계층화로 대규모 내부망의 표준 라우팅을 구현한 프로토콜임.
- 시사점 : 수렴 속도와 확장성의 원천은 토폴로지 설계에 있으므로 영역 구조와 이중화의 품질이 운영 품질을 결정함.
