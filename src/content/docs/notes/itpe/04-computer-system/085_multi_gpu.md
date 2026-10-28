---
title: "멀티 GPU (GPU: Graphics Processing Unit)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "085"
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- 멀티 GPU(Multi-GPU), GPU(Graphics Processing Unit), 상호연결(Interconnect), 토폴로지(Topology)
- PCIe(Peripheral Component Interconnect Express), NVLink, NVSwitch, P2P(Peer-to-Peer)
- HGX, 집합 메모리(Aggregate Memory), 확장 효율(Scaling Efficiency), 직접 액체 냉각(DLC, Direct Liquid Cooling)
- MIG(Multi-Instance GPU), vGPU(Virtual GPU)

## Ⅰ. 멀티 GPU의 개요

- 핵심 요약 : 한 노드에 여러 GPU를 장착하고 고속 상호연결로 묶어 메모리와 연산 한계를 넘는 하드웨어 구성.
- 개념 : 노드에 둘 이상의 **GPU** (Graphics Processing Unit)를 장착하고 노드 내 **상호연결** (Interconnect)로 결합해 하나처럼 운용하는 **멀티 GPU** (Multi-GPU) 구성.
- 배경 및 필요성 : 대규모 모델은 가중치만으로 단일 GPU의 비디오 메모리 용량을 초과하고 연산량도 단일 장치 대역을 넘음. 고성능 컴퓨팅(HPC, High-Performance Computing)과 AI 인프라에서 다수 GPU의 결합이 불가피해짐.
- 주요 목적 : **집합 메모리** (Aggregate Memory, 여러 GPU의 메모리를 합쳐 활용하는 용량) 확보, GPU 간 데이터 교환 지연 최소화, 노드 내 연산 밀도 제고.

## Ⅱ. 멀티 GPU의 특징 및 장점

- 핵심 요약 : P2P 직접 경로와 스위치 기반 완전 결합이 호스트 경유 복사를 없애 통신 지연과 대역폭 불균형을 낮춤.

1. **P2P** (Peer-to-Peer, 장치 간 직접 접근) 전송 : 호스트 메모리를 거치지 않고 **NVLink** 또는 **PCIe** (Peripheral Component Interconnect Express) 경로로 상대 GPU 메모리에 직접 읽기·쓰기 → 복사 단계 감소에 따른 지연 절감.
2. **NVSwitch** 완전 결합 : 스위치 칩이 노드 내 전체 GPU를 상호 연결하는 완전 결합 **토폴로지** (Topology, 장치 간 연결 형태)를 구성 → 임의 GPU 쌍이 동일 대역폭으로 통신해 통신 패턴에 따른 성능 편차 제거.
3. 기판 통합 설계 : **HGX** (GPU와 스위치를 한 기판에 통합하는 AI 서버 기판 규격) 기반 베이스보드로 장치를 집적 → 배선 거리 단축과 안정적인 고대역폭 유지.

## Ⅲ. 멀티 GPU의 구조 (흐름)

- 핵심 요약 : 제어·입출력 경로와 GPU 간 데이터 경로가 계층을 이루며, 토폴로지에 따라 통신 거리와 홉 수가 결정됨.
- 호스트 CPU(Central Processing Unit)와 PCIe 스위치가 장치 제어·입출력을 담당하고, NVLink와 NVSwitch 패브릭이 GPU 간 대량 데이터 교환을 담당함.

```text
[ 노드 내 인터커넥트 계층 ]

호스트 CPU (제어·입출력)
      ↓ PCIe 스위치
GPU 0 ~ GPU 7 (연산·메모리)
      ↓ NVLink
NVSwitch 패브릭 (전 GPU 상호연결)
```

```text
[ GPU 간 P2P 전송 경로 ]

GPU A의 메모리
      ↓ NVLink 또는 PCIe 직접 경로
GPU B의 메모리
      ↓
호스트 메모리 경유 없음
```

## Ⅳ. 멀티 GPU 상호연결 방식의 비교

- 핵심 요약 : 버스 기반 연결은 범용성, 링 결합은 중간 규모, 스위치 완전 결합은 대규모 병렬 워크로드에 적합함.
- 비교 대상은 PCIe 연결, 링 방식 NVLink, NVSwitch 완전 결합이며, 통신 경로와 대역폭, 구축 비용이 선택 축임.

| 비교 축 | PCIe 버스 연결 | 링 방식 NVLink | NVSwitch 완전 결합 |
| :--- | :--- | :--- | :--- |
| 통신 경로 | PCIe 스위치·호스트 경유 | 인접 GPU 간 링 연결 | 전용 스위치 패브릭 |
| GPU당 양방향 대역폭 | PCIe 5.0 x16 기준 128GB/s | 링 구성에 따라 상이 | NVLink 4 기준 900GB/s, NVLink 5 기준 1.8TB/s |
| 통신 균등성 | 경로 경합 발생 | 홉 수에 따라 편차 | 임의 쌍 간 균등 |
| 구축 비용 | 범용 서버로 낮음 | 중간 | 전용 베이스보드로 높음 |
| 적합 워크로드 | 경량 추론·렌더링 | 중규모 학습·시뮬레이션 | 대규모 분산 학습 |

- 선택 기준 : 워크로드의 통신 밀도와 예산을 기준으로 삼되 GPU 간 교환량이 큰 학습일수록 높은 등급의 상호연결을 선택함.

## Ⅴ. 멀티 GPU의 한계와 방안

- 핵심 요약 : 통신 병목, 전력·열, 장치 장애를 토폴로지 설계, 액체 냉각, 장애 격리로 일대일 대응함.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| 상호연결 병목에 따른 **확장 효율** (Scaling Efficiency, GPU 수 대비 성능 증가율) 저하 | 저대역 경로에 통신이 몰리면 장치를 늘려도 성능이 비례하지 않음 | 토폴로지 인식 배치, P2P 경로 활성화, 고등급 패브릭 채택 | GPU 수 대비 처리량 증가율 |
| 고밀도 집적에 따른 전력·열 한계 | 섀시당 발열이 공랭 한계를 넘어 클록 저하 발생 | **직접 액체 냉각** (DLC, Direct Liquid Cooling) 도입, 전원 분배 설계 | 장치 온도, 스로틀링 발생률 |
| 단일 장치 장애의 전파 | 밀결합 구성에서 한 장치의 오류가 작업 전체 중단으로 확대 | **ECC** (Error-Correcting Code, 오류를 검출·정정하는 코드) 모니터링, 장치 격리와 예비 자원 전환 | 장애 복구 소요 시간 |

## Ⅵ. 멀티 GPU에 대한 기술사적 제언

- 핵심 요약 : 상호연결을 연산 장치와 같은 설계 우선순위에 두고, 자원 분할과 입출력 경로를 표준화하는 운영 방향.
- 인프라 설계 부서는 장비 예산 수립 시 GPU 수와 상호연결 등급을 같은 기준으로 검토해 통신 계층이 병목이 되지 않는 균형 설계를 해야 함.
- 운영 조직은 **MIG** (Multi-Instance GPU, 하나의 GPU를 물리적으로 분할해 제공하는 기능)와 **vGPU** (Virtual GPU, 가상화로 GPU를 여러 사용자에 할당하는 기술)를 용도별로 배분해 개발·테스트 자원의 활용률을 높여야 함.
- 플랫폼 부서는 저장장치에서 GPU로 가는 직접 전송 경로와 노드 간 고속 네트워크를 표준 아키텍처로 정해 입출력 병목이 상호연결 투자를 상쇄하지 않게 관리해야 함.

## Ⅶ. 결론

- 핵심 요약 : 멀티 GPU는 고속 상호연결로 다수 장치를 결합해 단일 장치 한계를 넘는 하드웨어 구성 기술.
- 토폴로지·냉각·장애 격리가 함께 설계될 때 노드 내 연산 밀도의 가치가 실현됨.
