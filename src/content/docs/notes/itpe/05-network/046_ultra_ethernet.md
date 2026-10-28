---
title: "Ultra Ethernet (UEC) (UEC: Ultra Ethernet Consortium)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "046"
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- Ultra Ethernet, UEC(Ultra Ethernet Consortium), UET(Ultra Ethernet Transport)
- 패킷 스프레잉(Packet Spraying), 패킷 트림(Packet Trimming), 수신자 주도 크레딧 흐름 제어
- 인캐스트(Incast), 올투올(All-to-All), 이스트-웨스트 트래픽, LL-FEC
- InfiniBand, RoCEv2, ECMP, 공동 패키지 광학(CPO), NCCL

## Ⅰ. Ultra Ethernet의 개요

- 핵심 요약 : AI 학습과 고성능 컴퓨팅 클러스터의 통신 부하를 개방형 이더넷으로 처리하기 위한 차세대 고성능 이더넷 규격.
- 개념 : 리눅스 재단 산하 개방형 컨소시엄인 **Ultra Ethernet Consortium** (UEC)이 정의하는 고성능 이더넷 전송 규격, 2025년 표준 1.0 공개.
- 배경 및 필요성 : 대규모 언어 모델(LLM, Large Language Model) 학습에서는 수만 개의 GPU(Graphics Processing Unit)가 **올투올**(All-to-All, 모든 노드가 서로 통신하는 패턴) 통신을 수행하고 데이터센터 내부의 **이스트-웨스트 트래픽**(East-West Traffic, 서버·가속기 간 수평 방향 트래픽)이 폭증, 단일 생태계 의존의 InfiniBand는 비용 부담, RoCEv2(RDMA over Converged Ethernet v2)는 혼잡 제어·무손실 설정의 한계.
- 주요 목적 :
  1. 개방형 이더넷 기반의 초고대역폭·초저지연 전송
  2. **인캐스트**(Incast, 다수 송신자가 한 수신자로 몰리는 현상) 혼잡 붕괴 방지
  3. 패킷 단위 분산 전송으로 경로 활용률 향상

## Ⅱ. Ultra Ethernet의 특징 및 장점

- 핵심 요약 : 패킷을 여러 경로로 흩어 보내고 수신 측이 순서와 전송량을 통제하는 구조가 혼잡 제어와 경로 활용을 함께 높이는 방식.

1. **패킷 스프레잉** (Packet Spraying) : 하나의 플로우를 패킷 단위로 나눠 ECMP(Equal-Cost Multi-Path) 경로에 분산 → 특정 링크 쏠림과 혼잡 감소.
2. 비순서 전달과 수신단 재정렬 : 패킷이 서로 다른 경로로 도착해도 수신 NIC(Network Interface Card)가 순서를 복원 → 스위치는 단순 전달만 수행.
3. **패킷 트림** (Packet Trimming) : 혼잡 시 패킷 전체 폐기 대신 페이로드를 잘라 헤더만 송신단에 통보 → 빠른 혼잡 신호 확보와 재전송 절약.
4. **수신자 주도 크레딧 흐름 제어** (Receiver-Driven Credit Flow Control) : 수신 측이 버퍼 여유만큼 송신 권한 부여 → 인캐스트 버퍼 과부하 방지.
5. 저지연 전방 오류정정 (LL-FEC, Low-Latency Forward Error Correction) : 물리 계층 오류를 수신 측에서 즉시 정정 → 재전송 지연 회피.
6. 이더넷 운영 모델 계승 : 기존 이더넷의 관리·진단 도구와 호환 유지 → 운영 조직의 재학습 부담 감소.

## Ⅲ. Ultra Ethernet의 구조 (흐름)

- 핵심 요약 : 응용 라이브러리가 UET 전송 계층의 분산·혼잡 제어를 호출하고 이더넷 계층이 운반하는 계층 구조.
- **UET**(Ultra Ethernet Transport) : 패킷 스프레잉·크레딧·혼잡 제어를 담당하는 UEC의 전송 계층 기능.
- 응용 연계 : PyTorch 같은 학습 프레임워크와 MPI(Message Passing Interface) 등 병렬 런타임이 응용 프로그래밍 인터페이스(API, Application Programming Interface)를 통해 UET를 호출.

```text
[ UEC 프로토콜 스택 ]

AI·HPC 응용 (프레임워크·병렬 런타임)
   ↓
응용 인터페이스 (libfabric 계열)
   ↓
UET 전송 계층 : 스프레잉·트림·크레딧
   ↓
이더넷 링크·물리 계층 (LL-FEC)
```

```text
[ 패킷 스프레잉과 재정렬 ]

하나의 플로우
   ↓ 패킷 단위 분할
ECMP 경로 A · B · C 분산 전송
   ↓ 도착 순서 뒤섞임
수신 NIC 재정렬 버퍼에서 복원
```

## Ⅳ. InfiniBand·RoCEv2와의 비교

- 핵심 요약 : 무손실 전용 패브릭의 InfiniBand와 해시 고정 경로의 RoCEv2에 비해 UEC는 패킷 단위 분산과 수신 측 제어로 개방성과 확장성을 함께 추구.

| 비교 항목 | InfiniBand | RoCEv2 | Ultra Ethernet (UEC) |
| --- | --- | --- | --- |
| 표준화 주체 | IBTA(InfiniBand Trade Association) | IBTA·IEEE 확장 | 리눅스 재단 산하 UEC |
| 무손실 방식 | 크레딧 기반 하드웨어 무손실 | PFC(Priority Flow Control)·ECN(Explicit Congestion Notification) | 손실 허용 전송과 빠른 혼잡 회복 |
| 경로 방식 | 정적·적응형 경로 | 해시 기반 단일 경로 고정 | 패킷 단위 멀티패스 스프레잉 |
| 혼잡 제어 | 크레딧 흐름 제어 | PFC 데드록·인캐스트 위험 | 패킷 트림·원격 계측·수신자 크레딧 |
| 인프라 | 전용 스위치 필요 | 일반 이더넷 스위치 | 일반 고속 이더넷과 UEC NIC |

- 선택 기준 : 기존 InfiniBand 자산과 단일 벤더 최적화를 중시하면 InfiniBand, 이더넷 운영 경험과 공급망 다변화를 중시하면 RoCEv2 또는 UEC를 검토.

## Ⅴ. Ultra Ethernet의 한계와 방안

- 핵심 요약 : 수신단 재정렬 부담과 생태계 초기 미성숙·교체 비용을 하드웨어 재정렬과 호환·단계 전략으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 수신단 재정렬 오버헤드 | 경로 간 지연 편차 확대 → 재정렬 버퍼 고갈과 메모리 병목 | NIC 내 하드웨어 재정렬 엔진, 경로 편차 기반 스프레잉 비율 조정 | 재정렬 버퍼 점유율 |
| 생태계 초기 미성숙 | 표준 초기 단계의 검증 레퍼런스·장비 선택지 부족 | RoCEv2 호환 구성과 병행 검증, 오픈소스 스택 벤치마크 | 검증 완료 구성 수 |
| 패브릭 교체 비용 | UEC 대응 NIC·스위치의 신규 도입 필요 | 영향이 제한된 구역부터의 단계 도입과 기존 패브릭 공존 설계 | 단위 대역폭당 도입 비용 |

## Ⅵ. Ultra Ethernet에 대한 기술사적 제언

- 핵심 요약 : AI 인프라 설계 조직이 개방형 패브릭·광 인터커넥트·집합 통신 최적화를 하나의 로드맵으로 묶는 방향.

1. 인프라 설계 조직 : InfiniBand 일변도 의존을 낮추도록 NPU(Neural Processing Unit) 등 이기종 가속기를 수용하는 개방형 패브릭 기준 선정.
2. 플랫폼 엔지니어링 조직 : 고속화에 따른 구리 배선 거리 한계에 대비해 공동 패키지 광학(CPO, Co-Packaged Optics)을 스위치 로드맵에 반영.
3. 학습 플랫폼 조직 : All-Reduce·All-to-All 같은 집합 통신 연산과 UET 스프레잉 동작의 정합성을 NCCL(NVIDIA Collective Communications Library) 등 라이브러리 조정으로 검증.

## Ⅶ. 결론

- 핵심 요약 : Ultra Ethernet은 AI 클러스터의 통신을 개방형 이더넷 위에서 해결하려는 차세대 고성능 전송 규격.
- 패브릭의 개방성과 혼잡 제어 설계가 AI 인프라의 확장 비용과 공급망 선택권을 결정하는 요소.
