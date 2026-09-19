---
title: "DiffServ"
date: "2026-09-20T00:30:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기출 · 76%"
extra:
  source_status: "기출"
  source_history: "125회"
  priority: 76
  priority_note: "[출제(KPC):125]"
---

## 답안 골격
```text
[DiffServ] ◀━━ 머리: Ⅶ 내 의견 (엣지 DSCP 마킹 표준화와 코어망 단순 PHB 전달의 결합 아키텍처)
 ┃
 ┣━ Ⅰ 개요 ───── IntServ의 코어 라우터 상태 저장 한계(확장성 결여) → 클래스 기반 차등 QoS
 ┣━ Ⅱ 특징 ───── 확장성(Scalability), 클래스 집합 처리, 상태 비저장(Stateless Core), SLA 기반
 ┣━ Ⅲ 구조 ───── 경계 라우터(분류기·미터·마커·셰이퍼) + 코어 라우터(PHB 처리) + DS 필드(DSCP 6비트)
 ┣━ Ⅳ 흐름 ───── ① 경계 트래픽 분류 및 DSCP 마킹 → ② 코어 라우터 유입 → ③ DSCP 매핑 큐 스케줄링(PHB)
 ┣━ Ⅴ 비교 ───── IntServ vs DiffServ (플로우 단위 vs 클래스 단위, RSVP 상태 보관 vs 상태 없음)
 ┗━ Ⅵ 실무 ───── 종단 간(E2E) 절대적 대역폭 보장 불가(Soft QoS) / 도메인 간 SLA 협약 복잡성
```
- 필수 키워드: 차등화 서비스 · DSCP(6비트) · PHB(EF/AF/BE) · 경계 라우터(Edge) · 코어 라우터(Core) · 상태 비저장
- 배점 전략: 10점 = Ⅰ → Ⅲ DiffServ 도메인 구성도(엣지 분류 vs 코어 PHB) → Ⅴ IntServ vs DiffServ 비교표 / 25점 = 125회 기출 종합 QoS 모델 비교 상세
- 기출: 125회 1교시: "인터넷 QoS 보장 기법 중 IntServ와 DiffServ의 차이점을 설명하시오." → Ⅰ~Ⅴ

## 한 줄 본질
- 수백만 개 개별 통신 플로우마다 라우터가 자원을 예약하고 상태를 기억해야 했던 IntServ의 확장성 붕괴 → 망 입구(Edge)에서 패킷의 중요도를 몇 개의 등급(DSCP)으로 도장 찍고 망 내부(Core)는 상태 기억 없이 단순 등급별 차등(PHB) 처리 → 대규모 인터넷 백본망의 무제한 확장성 획득 / 개별 세션에 대한 수학적 절대 대역폭 보증(Hard QoS) 불가

## 핵심 그림
```text
[ DiffServ 도메인 구조 및 동작 흐름 ]

   (사용자 패킷 유입)
          |
          v
 [ 1. 경계 라우터 (Edge Router / Boundary) ]
 +---------------------------------------------------------+
 | 분류기(Classifier) -> 미터(Meter) -> 마커(DSCP 부여)   |
 | -> 폴리서/셰이퍼(Policer/Shaper: 초과 트래픽 드롭/지연)  |
 +---------------------------------------------------------+
          | (IP 헤더 DSCP 6비트 마킹 패킷)
          v
 [ 2. 코어 라우터 (Core Router / Interior) ]
 +---------------------------------------------------------+
 | 상태 보관 없음 (Stateless!)                            |
 | 오직 DSCP 값만 보고 미리 정의된 PHB(홉 단위 동작) 수행: |
 |  - EF (Expedited Forwarding) : 음성/VoIP 우선 전송      |
 |  - AF (Assured Forwarding)   : 중요 업무 차등 대역폭    |
 |  - BE (Best Effort)          : 일반 인터넷 패킷         |
 +---------------------------------------------------------+
```

## 핵심 용어
- DSCP(Differentiated Services Code Point): IPv4의 ToS 필드나 IPv6의 Traffic Class 필드 상위 6비트를 사용하여 64가지 서비스 클래스를 정의하는 코드
- PHB(Per-Hop Behavior): 코어 라우터가 특정 DSCP 값을 가진 패킷을 만났을 때 큐잉 스케줄링(WFQ, PQ)과 패킷 폐기(WRED)를 적용하는 홉 단위 전달 규칙
- EF(Expedited Forwarding): 지연과 손실에 극도로 민감한 트래픽(VoIP)을 위해 엄격한 대역폭 보장과 최우선 순위를 부여하는 가상 전용회선(Leased Line)급 PHB

## 핵심 통찰
- 복잡한 작업(패킷 검사, 분류, 대역폭 측정, 마킹)은 트래픽 양이 적은 망 외곽의 "경계 라우터"로 밀어내고, 초당 수억 패킷이 지나는 "코어 라우터"는 헤더의 도장(DSCP)만 보고 단순 전달만 하도록 역할을 완벽히 분리
- 개별 세션의 대역폭을 예약하지 않으므로 사용자가 갑자기 폭증하면 AF 클래스 패킷이라도 지연이 발생할 수 있는 "상대적 우선순위(Soft QoS)" 모델
- 서로 다른 통신사 망을 건너갈 때(Inter-domain) DSCP 매핑 정책이 깨질 수 있으므로, 사업자 간 트래픽 교환 계약(SLA) 시 DSCP 재분류 룰 정합 필수

## 이웃 토픽과 구분
- IntServ vs DiffServ: IntServ는 RSVP 프로토콜로 출발지부터 목적지까지 모든 라우터에 자원을 예약(상태 저장) / DiffServ는 패킷 헤더에 클래스를 적고 코어 라우터는 상태 없이 차등 처리(상태 비저장)

## 문제·원인·대책
- 적용 상황: 기업 클라우드 연동망에서 대용량 트래픽 유입 시 음성 통화 끊김
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 음성 트래픽이 일반 데이터 패킷과 뒤섞여 지연 발생 | DSCP 마킹 누락으로 전 트래픽이 Best Effort로 일괄 처리 | 음성 패킷에 EF(DSCP 46) 마킹 및 코어 라우터 LLQ(저지연 큐) 적용 | 음성 지연 시간을 20ms 이내로 보장 |
| 계약 대역폭을 초과한 비인가 트래픽의 망 유입 | 경계 라우터의 트래픽 조절(Conditioning) 기능 부재 | 토큰 버킷 기반 트래픽 폴리싱(Policing) 및 셰이핑(Shaping) 적용 | 초과 패킷 폐기 또는 지연을 통해 코어 백본망 포화 방지 |

## 이렇게 출제된다
- 제125회 1교시: "QoS 보장 기술인 IntServ와 DiffServ를 비교하여 설명하시오." → 요구 포인트: 아키텍처 차이(Stateful vs Stateless), DSCP 필드 구조, PHB 3종(EF, AF, BE), 확장성 비교

## 내 의견
- [SD-WAN 환경과의 DiffServ 오버레이 결합] 물리 언더레이 회선이 여러 사업자로 나뉘어 있을 때 DSCP 값이 초기화되거나 무시되는 문제 발생 → 나라면: 기업 지사와 데이터센터 구간에 SD-WAN 오버레이 터널을 뚫고, 터널 내부 헤더뿐만 아니라 외부 IPsec 헤더에도 DSCP 값을 복제(TOS Copy)하여 통신사 회선 구간에서도 의도한 QoS 우선순위가 유지되도록 설계

## 찾아볼 것
- RFC 2597의 AF(Assured Forwarding) 클래스 4개 그룹과 3단계 드롭 우선순위(Drop Precedence)
