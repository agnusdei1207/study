---
title: "Ultra Ethernet (UEC) (UEC: Ultra Ethernet Consortium)"
author: "agnusdei1207"
date: "2026-10-24T22:49:07+09:00"
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

- Ultra Ethernet, UEC(Ultra Ethernet Consortium), UET(Ultra Ethernet Transport)
- 패킷 스프레잉(Packet Spraying), 패킷 트림(Packet Trimming), 수신자 주도 크레딧 흐름 제어
- 인캐스트(Incast), 올투올(All-to-All), 이스트-웨스트 트래픽, LL-FEC
- 인피니밴드(InfiniBand), RoCEv2, 공동 패키지 광학(CPO), NCCL

## Ⅰ. Ultra Ethernet (UEC)의 개요

- 핵심 요약 : AI 학습과 고성능 컴퓨팅 클러스터의 통신 부하를 개방형 이더넷으로 처리하기 위한 차세대 고성능 이더넷 규격.
- 개념 : 리눅스 재단 산하의 다수 기업 연합인 **Ultra Ethernet Consortium** (UEC)이 정의하는 고성능 이더넷 전송 규격으로, 대규모 AI와 고성능 컴퓨팅(HPC, High-Performance Computing) 클러스터의 **이스트-웨스트** (East-West) 트래픽을 처리하는 것이 목적.
- 배경 및 필요성 : 대규모 언어 모델(LLM, Large Language Model) 학습에서는 수만 개의 GPU(Graphics Processing Unit)가 **올투올** (All-to-All) 통신을 해야 하는데, 기존 인피니밴드는 단일 생태계 의존으로 비용이 높고, RoCEv2는 혼잡 제어와 무손실 설정에 한계가 있음.
- 주요 목적 :
  1. 개방형 이더넷 기반의 초고대역폭, 초저지연 전송
  2. 인캐스트(Incast) 상황의 혼잡 붕괴 방지
  3. 패킷 단위 분산 전송으로 경로 활용률 향상

## Ⅱ. Ultra Ethernet의 특징 및 장점

- 핵심 요약 : 패킷을 여러 경로로 흩뿌리고 수신 측이 순서와 전송량을 책임지는 구조가 혼잡 제어와 경로 활용을 함께 높이는 방식.

1. **패킷 스프레잉** (Packet Spraying) : 하나의 플로우를 패킷 단위로 나눠 가용한 ECMP(Equal-Cost Multi-Path) 경로에 분산 → 특정 링크의 쏠림과 혼잡 감소.
2. 비순서 전달과 수신단 재정렬 : 패킷이 서로 다른 경로로 도착해도 수신 NIC(Network Interface Card)가 순서를 맞춤 → 스위치는 단순한 전달만 수행.
3. **패킷 트림** (Packet Trimming) : 스위치 버퍼가 찰 때 패킷 전체를 버리지 않고 페이로드를 잘라 헤더만 송신단에 알림 → 빠른 재전송 신호 확보.
4. **수신자 주도 크레딧 흐름 제어** (Receiver-Driven Credit Flow Control) : 수신 측이 버퍼 여유만큼 송신 권한을 허용 → 인캐스트에 따른 버퍼 과부하 방지.
5. 저지연 전방향 오류정정 (LL-FEC, Low-Latency Forward Error Correction) : 물리 계층의 비트 오류를 즉시 정정 → 재전송 지연 회피.

## Ⅲ. Ultra Ethernet의 구조 (흐름)

- 핵심 요약 : 응용 API가 전송 계층의 스프레잉과 크레딧 기능을 호출하고, 이더넷 물리 계층이 그 패킷을 운반하는 계층 구조.

```text
[ UEC 프로토콜 스택 ]

AI·HPC 응용 (PyTorch, MPI 등)
          ↓
libfabric (OFI) API
          ↓
UET 전송 계층 (스프레잉, 트림, 크레딧)
          ↓
이더넷 물리·링크 계층 (LL-FEC)
```

- **UET** (Ultra Ethernet Transport) : UEC의 전송 계층으로, 패킷 스프레잉과 혼잡 제어를 담당.

```text
[ 패킷 스프레잉 흐름 ]

하나의 플로우
      ↓ 패킷 단위 분할
경로 A · 경로 B · 경로 C (ECMP)
      ↓ 도착 순서가 뒤섞임
수신 NIC가 순서 재정렬
```

## Ⅳ. 인피니밴드, RoCEv2와의 비교

- 핵심 요약 : 인피니밴드의 무손실 단일 경로 구조와 RoCEv2의 해시 기반 경로 고정을 넘어, UEC는 패킷 단위 분산과 수신 측 제어로 이더넷 위에서 확장성을 확보하려는 방식.

| 비교 항목 | 인피니밴드 (InfiniBand NDR) | RoCEv2 (RDMA over Converged Ethernet v2) | Ultra Ethernet (UEC) |
| --- | --- | --- | --- |
| 표준화 주체 | IBTA(InfiniBand Trade Association), 단일 생태계 의존도 높음 | IBTA와 IEEE(Institute of Electrical and Electronics Engineers) 확장 | 리눅스 재단 산하 개방형 컨소시엄 |
| 네트워크 특성 | 크레딧 기반 무손실 | PFC(Priority Flow Control)와 ECN(Explicit Congestion Notification) 기반 무손실 추구 | 손실을 허용하는 유연한 전송 |
| 경로 방식 | 정적 경로 또는 적응형 경로 | 해시 기반 단일 경로 고정 | 패킷 단위 멀티패스 스프레잉 |
| 혼잡 제어 | 하드웨어 크레딧 흐름 제어 | PFC 데드록과 인캐스트 위험 | 패킷 트림, 종단 원격 측정, 수신자 크레딧 |
| 스위치 인프라 | 전용 인피니밴드 스위치 필요 | 일반 데이터센터 이더넷 스위치 | 일반 고속 이더넷 스위치와 UEC NIC |
| 확장성 | 대규모 GPU 확장 시 비용 증가 | 대규모에서 성능 저하 가능 | 초대규모 GPU 클러스터 지향 |

- 선택 기준 : 이미 인피니밴드 자산이 있고 단일 벤더 최적화가 중요하면 인피니밴드를, 이더넷 운영 경험을 살리려면 RoCEv2 또는 UEC를 검토.

## Ⅴ. Ultra Ethernet의 한계와 방안

- 핵심 요약 : 비순서 패킷의 재정렬 부담과 생태계 미성숙이 핵심 한계이며, 하드웨어 재정렬과 호환 계층으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 수신단 재정렬 오버헤드 | 경로 간 지연 편차가 크면 재정렬 버퍼가 고갈되어 메모리 병목과 CPU 개입 발생 | NIC 내부 하드웨어 재정렬 엔진 적용, 경로별 지연 편차에 따라 스프레잉 비율 조정 | 재정렬 버퍼 점유율 |
| 신규 하드웨어와 생태계 미성숙 | 표준 초기 단계라 검증 레퍼런스가 부족하고 NIC와 스위치를 교체해야 함 | RoCEv2 지원 스위치와의 소프트웨어 호환 계층 제공, 검증된 오픈소스 스택 보급 | 검증 완료 구성 수, 교체 비용 |

## Ⅵ. Ultra Ethernet에 대한 기술사적 제언

- 핵심 요약 : 특정 벤더 패브릭에 대한 종속을 줄이고, 광 인터커넥트와 집합 통신 라이브러리를 함께 맞추는 방향으로 AI 인프라를 설계.

1. 이기종 가속기 패브릭 검토 : 인피니밴드 일변도에서 벗어나 NPU(Neural Processing Unit)를 포함한 이기종 가속기 클러스터를 수용할 개방형 패브릭을 선제적으로 검토할 필요가 있음.
2. 광 인터커넥트 로드맵 : 800G와 1.6T급 이상으로 속도가 올라가면 구리선 거리 한계가 커지므로, 공동 패키지 광학(CPO, Co-Packaged Optics) 기술을 스위치 로드맵과 함께 준비해야 함.
3. 집합 통신 라이브러리 최적화 : All-Reduce와 All-to-All 같은 집합 통신 연산이 UET의 스프레잉 동작과 맞물리도록 NCCL(NVIDIA Collective Communications Library) 등 라이브러리를 조정할 필요가 있음.

## Ⅶ. 결론

- 핵심 요약 : Ultra Ethernet은 AI 클러스터의 통신을 개방형 이더넷 위에서 처리하려는 차세대 고성능 전송 규격.
- 시사점 : 패브릭의 개방성과 혼잡 제어 방식이 AI 인프라의 확장 비용을 좌우하므로, 표준의 성숙도와 검증 사례를 함께 추적하는 것이 중요함.
