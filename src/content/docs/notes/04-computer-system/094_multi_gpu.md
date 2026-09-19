---
title: "멀티 GPU"
author: "Gemini 3.8 Flash"
date: "2026-09-20T01:11:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기출 · 70%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "134회"
  priority: 70
  priority_note: "[출제:134]"
---

## 답안 골격
```text
[멀티 GPU] ◀━━ 머리: Ⅶ 내 의견 (NVLink·NVSwitch 패브릭과 RoCEv2 네트워크를 결합한 스케일업-스케일아웃 하이브리드 가속 인프라 구축)
 ┃
 ┣━ Ⅰ 개요 ───── 단일 GPU 메모리 용량 및 단일 칩 연산 한계 봉착 → 복수의 GPU를 초고속 인터커넥트로 결합하여 단일 가상 연산 풀로 통합
 ┣━ Ⅱ 특징 ───── 테라바이트급 초고속 대역폭(NVLink) · 이종 노드 간 RDMA 무복사 통신 · 토폴로지 인식 스케줄링 · 집단 통신(NCCL) 최적화
 ┣━ Ⅲ 구조 ───── 호스트 CPU + 복수 GPU 가속기 + 고속 인터커넥트(NVLink/PCIe Gen5) + 스위치 패브릭(NVSwitch) + RoCEv2/InfiniBand HCA
 ┣━ Ⅳ 흐름 ───── ① GPU 메모리 텐서 적재 → ② 커널 병렬 연산 실행 → ③ NVLink/GPUDirect 통한 노드 내/외 동기화 → ④ 결과 집계
 ┣━ Ⅴ 비교 ───── PCIe 버스 연결 vs NVLink 연결 vs InfiniBand 클러스터 네트워크 연결
 ┗━ Ⅵ 실무 ───── GPU 간 통신 병목(Communication Overhead) / 토폴로지 불일치로 인한 성능 저하 / 전력 밀도 및 발열 제어
```
- 필수 키워드: 멀티 GPU · NVLink · NVSwitch · GPUDirect RDMA · NCCL · 인터커넥트 · 토폴로지
- 배점 전략: 10점 = Ⅰ 개요 → Ⅲ 8-GPU NVLink 풀메시/스위치 구조도 → Ⅴ PCIe vs NVLink 비교표 / 25점 = Ⅰ~Ⅶ 전개, Ⅳ GPUDirect P2P 통신 흐름과 Ⅵ 랙스케일 전력·냉각 인프라 설계
- 기출: 134회 4교시 2번 `딥러닝에서 대규모 신경망을 효율적으로 훈련하기 위한 멀티 GPU 기술에 대하여 설명하시오.` 서술형 출제

## 한 줄 본질
- 수백억 파라미터의 AI 모델은 단일 GPU VRAM에 적재조차 불가능함 → 여러 대의 GPU를 PCIe 버스를 우회하는 전용 고속 링크(NVLink)와 스위치(NVSwitch)로 상호 연결하여 단일 대형 GPU처럼 동작 → 대규모 AI 연산 선형 확장 / GPU 간 동기화 통신 오버헤드 및 막대한 인프라 전력 소모

## 핵심 그림
```text
[ 단일 서버 내 8-GPU NVSwitch 패브릭 상호연결 아키텍처 ]

+─────────────────────────────────────────────────────────────+
| 호스트 CPU 및 시스템 메모리 (Host Control Plane)            |
+──────────────────────────────┬──────────────────────────────+
                               │ PCIe Gen5 버스
+──────────────────────────────v──────────────────────────────+
| NVSwitch 베이스보드 (양방향 900GB/s ~ 1.8TB/s 올투올 패브릭)  |
|  [ NVSwitch 1 ]    [ NVSwitch 2 ]    [ NVSwitch 3 ]   ...   |
+───┬────────┬───────────┬───────────┬───────────┬────────┬───+
    │NVLink  │NVLink     │NVLink     │NVLink     │NVLink  │NVLink
+───v───+ +──v───+   +───v───+   +───v───+   +───v───+ +──v───+
| GPU 0 | | GPU 1 |   | GPU 2 |   | GPU 3 |   | GPU 4 | | GPU 7 |
| (H100)| | (H100)|   | (H100)|   | (H100)|   | (H100)| | (H100)|
+───────+ +──────+   +───────+   +───────+   +───────+ +──────+
    │         │           │           │           │         │
    └─────────┴───────────┴─────┬─────┴───────────┴─────────┘
                                │ GPUDirect RDMA
+───────────────────────────────v─────────────────────────────+
| 초고속 네트워크 HCA (ConnectX-7 / InfiniBand / 400Gbps RoCEv2)|
+─────────────────────────────────────────────────────────────+
```

## 핵심 용어
- NVLink: PCIe의 대역폭 한계(최대 128GB/s)를 돌파하여 GPU 간 최대 900GB/s(NVLink 4) 이상의 초고속 직접 데이터 교환을 지원하는 엔비디아의 독자 버스 기술
- GPUDirect RDMA: 호스트 CPU와 시스템 RAM을 경유하지 않고, 네트워크 카드(NIC)가 원격 노드의 GPU VRAM에 직접 DMA 읽기/쓰기를 수행하는 무복사(Zero-Copy) 기술
- NCCL(NVIDIA Collective Communications Library): All-Reduce, All-Gather, Broadcast 등 멀티 GPU 간의 데이터 교환을 토폴로지(NVLink 링/트리)에 맞춰 하드웨어 최적화한 집단 통신 라이브러리

## 핵심 통찰
- 멀티 GPU의 성패는 연산기가 아니라 '인터커넥트 대역폭'이 결정함 → GPU 코어의 연산 속도가 아무리 빨라도 가중치와 그래디언트를 주고받는 통신 링크가 느리면 GPU는 대부분의 시간을 통신 대기(Idle)로 낭비함
- 스케일업(Scale-Up)과 스케일아웃(Scale-Out)의 분계선이 명확함 → 1개 노드 내부(8개 GPU)는 NVLink/NVSwitch로 묶는 스케일업을 적용하고, 노드와 노드 사이는 InfiniBand/RoCEv2 네트워크로 묶는 스케일아웃 구조가 글로벌 표준 아키텍처임
- NUMA 토폴로지 인식이 누락되면 성능이 반토막 남 → CPU 소켓 0번에 연결된 GPU가 소켓 1번에 연결된 NIC와 통신할 때 QPI/UPI 링크 병목을 거치므로, GPU와 PCIe 스위치, NIC 간의 1:1 친화도(Affinity) 바인딩이 필수적임

## 이웃 토픽과 구분
- 멀티 GPU vs GPGPU: GPGPU = 단일 그래픽 칩셋을 범용 병렬 연산에 활용하는 하드웨어 기술 / 멀티 GPU = 복수의 가속기를 고속 인터커넥트로 결합하여 단일 대형 워크로드를 분산 처리하는 시스템 아키텍처

## 문제·원인·대책
- 사례: 134회 기출 및 8-GPU 서버에서 대규모 언어모델 학습 중 GPU 활용률(GPU Utilization)이 35%로 급락한 병목 사고
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 노드 간 통신 시 CPU 사용률이 100%로 치솟고 GPU 연산 지연 발생 | TCP/IP 스택 경유 및 시스템 메모리 중복 복사(Buffer Copy) 발생 | GPUDirect RDMA 및 RoCEv2 커널 바이패스 네트워크 적용 | CPU 오버헤드 제로화 및 노드 간 GPU 메모리 직접 통신 달성 |
| 특정 GPU 쌍 간의 All-Reduce 통신 속도가 다른 쌍보다 4배 느림 | 서버 내부 NVLink 토폴로지 미고려 및 PCIe 브릿지 경유 통신 발생 | NCCL 환경 변수(`NCCL_TOPO_DUMP`) 점검 및 토폴로지 인식 매핑 | 모든 GPU 간 균등한 최고 대역폭 보장으로 학습 속도 2.8배 향상 |

## 이렇게 출제된다
- 제134회 4교시 2번: "딥러닝에서 대규모 신경망을 효율적으로 훈련하기 위한 멀티 GPU 기술에 대하여 설명하시오." → 요구 포인트: Ⅰ 멀티 GPU 도입 배경 + Ⅲ 하드웨어 인터커넥트(NVLink, NVSwitch, RDMA) + Ⅵ 토폴로지 및 병목 해결 방안

## 내 의견
- [RoCEv2 기반 이더넷 표준화와 랙스케일 액체냉각 멀티 GPU 인프라 구축] 값비싼 InfiniBand 독점 생태계는 인프라 TCO를 극단적으로 상승시킴 → 나라면: 스케일아웃 패브릭에 400Gbps Ultra Ethernet/RoCEv2를 채택하여 표준 네트워크 기반 고성능 클러스터를 구성하고, 8-GPU 고밀도 서버의 40kW 이상 열부하를 해소하기 위해 D2C(Direct-to-Chip) 액체냉각을 기본 설계로 채택

## 찾아볼 것
- Ultra Ethernet Consortium(UEC)의 AI 특화 전송 계층 프로토콜 사양
