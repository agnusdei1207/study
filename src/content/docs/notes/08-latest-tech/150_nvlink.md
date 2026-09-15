---
sidebar:
  order: 150
  label: "150. NVLink"
  badge:
    text: "기출 · 50%"
    variant: note
title: "NVLink"
date: "2026-09-15T11:20:00+09:00"
tags:
  - "notes-latest_tech"
weight: 150
extra:
  question_no: "150"
  source_status: "기출"
  source_history: "138회"
  priority: 50
  priority_note: "NVLink GPU 간 대역폭 설계가 138회 출제됨"
---

## Ⅰ. 개요

- **정의**: 기존 PCIe 버스의 대역폭 한계와 지연시간을 극복하기 위해 다중 GPU 간 또는 GPU-CPU 간에 초당 수백 기가바이트에서 테라바이트급 양방향 대역폭과 메모리 의미론(Load/Store)을 제공하는 엔비디아의 독자적 초고속 인터커넥트 기술
- **배경 및 필요성**: 수천억 파라미터 기반 LLM 모델의 분산 학습 시 텐서 병렬화(TP) 및 All-Reduce 집합 통신은 매 레이어마다 대규모 그래디언트와 활성화 텐서를 교환해야 하나, 표준 PCIe Gen5 버스는 대역폭(양방향 128GB/s) 한계와 호스트 CPU 루트 복합체 경유 지연으로 심각한 통신 병목을 초래함에 따라, GPU 간 직접 점대점(P2P) 및 NVSwitch 기반 풀메시 패브릭을 구성하여 단일 노드 내 수십 개 GPU를 거대한 단일 공유 메모리 공간으로 통합할 필요성 대두

## Ⅱ. 특징

- GPU당 양방향 최대 1.8TB/s(NVLink 5 기준)에 달하는 초고대역폭 및 나노초 단위 초저지연 전송
- NVSwitch ASIC 기반의 풀메시(Full-Mesh) 토폴로지 구축으로 노드 내 임의 GPU 간 비차단 통신
- NVSwitch 내부 하드웨어 수준에서 리덕션을 직접 수행하는 인네트워크 컴퓨팅(SHARP) 가속

## Ⅲ. 구조 및 구성요소

```text
[NVLink 인터커넥트 아키텍처]
├── [GPU 인터페이스 및 프로토콜 계층]
│   ├── [NVLink 엔드포인트 포트 (NVLink Port/PHY)]
│   └── [메모리 변환 엔진 (NVLink Memory Management)]
├── [스위칭 패브릭 계층]
│   ├── [NVSwitch 패브릭 ASIC (Crossbar Non-blocking Switch)]
│   └── [인네트워크 리덕션 엔진 (SHARP Hardware Engine)]
└── [토폴로지 및 소프트웨어 계층]
    ├── [단일 공유 메모리 주소 공간 (Unified Memory Space)]
    └── [통신 최적화 라이브러리 (NCCL - Collective Communications)]
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 구분 | 구성요소 | 기능 설명 |
|:---|:---|:---|
| 물리 인터페이스 | NVLink PHY | 고속 차동 시리얼라이저(SerDes) 기반으로 레인당 고속 PAM4 신호 송수신 |
| 통신 프로토콜 | 트랜잭션 엔진 | PCIe 변환 없이 GPU VRAM 간 P2P 직접 읽기/쓰기 및 캐시 일관성 트랜잭션 처리 |
| 스위칭 패브릭 | NVSwitch | 다중 GPU의 NVLink 포트를 집선하여 완전 메시(Full-mesh) 비차단 패킷 스위칭 제공 |
| 하드웨어 가속 | SHARP 엔진 | All-Reduce 집합 통신 시 스위치 내부에서 부동소수점 합산 연산을 직접 처리하여 트래픽 반감 |
| 소프트웨어 스택 | NCCL 라이브러리 | NVLink 토폴로지를 자동 감지하여 링(Ring) 또는 트리(Tree) 알고리즘으로 최적 집합 통신 수행 |

## Ⅳ. 흐름도

```text
[송신 GPU 코어] (① 텐서 병렬화 연산 후 인접 GPU로 전송할 그래디언트 텐서 버퍼 지정)
│
▼
[NVLink 엔드포인트] (② PCIe 버스를 우회하여 고속 NVLink 패킷으로 직렬화 송출)
│
▼
[NVSwitch 패브릭] (③ 크로스바 스위치를 통해 목적지 GPU 포트로 무손실 초저지연 라우팅)
│
▼
[SHARP 인네트워크] (④ NVSwitch 내부에서 다중 GPU 데이터의 합산(All-Reduce) 동시 연산)
│
▼
[수신 GPU VRAM] (⑤ 중간 복사 없이 타깃 GPU의 VRAM 주소로 직접 DMA 기록 완료)
```

- 분기 결과: 노드 내 GPU 간 통신은 NVSwitch 전용 도메인으로 초고속 완료되며, 노드 간 경계 통신 발생 시 InfiniBand/RoCE 네트워크 카드로 자동 분기

## Ⅴ. 종류 및 비교

| 비교 항목 | NVLink / NVSwitch | 표준 PCIe Gen5 | InfiniBand (NDR/XDR) |
|:---|:---|:---|:---|
| 주요 적용 범위 | 단일 노드 또는 랙(NVL72) 내부 | 서버 메인보드 내부 기성 슬롯 | 노드 간 클러스터 스케일아웃 |
| 양방향 최대 대역폭 | GPU당 900GB/s ~ 1.8TB/s | x16 슬롯 기준 128GB/s | 포트당 400Gbps ~ 800Gbps (50~100GB/s) |
| 통신 방식 | P2P 메모리 Load/Store 직접 매핑 | 호스트 루트 복합체 경유 DMA | 네트워크 패킷 기반 RDMA 전송 |
| 집합 연산 가속 | 스위치 내장 SHARP 하드웨어 가속 | 없음 (CPU 또는 GPU 코어 연산) | 인피니밴드 스위치 내 SHARP 가속 |
| 생태계 종속성 | NVIDIA 전용 하드웨어 독점 규격 | 개방형 PCI-SIG 산업 표준 | 개방형 IBTA 표준 (Mellanox 중심) |

## Ⅵ. 실무 고려사항 및 대책

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| NVSwitch 도메인 외부 노드 간 통신 시 대역폭 불일치(병목 현상) | 노드 내부는 텐서/파이프라인 병렬화에 집중하고 노드 간은 데이터 병렬화 계층 배치 | 계층형 All-Reduce를 통한 노드 간 트래픽 격리 및 전체 처리량 극대화 |
| 특정 NVLink 레인 물리적 단선 또는 신호 감쇠 시 클러스터 중단 | 링크 레벨 FEC(순방향 오류 정정) 활성화 및 불량 레인 자가 디그레이드 회피 라우팅 | 일시적 신호 오류 복구 및 분산 학습 중단 방지 |
| 대규모 랙 스케일(NVL72) 확장 시 고밀도 구리 케이블링 및 발열 급증 | 카트리지형 백플레인 직접 체결 및 액체 냉각(Direct Liquid Cooling) 전면 도입 | 신호 무결성 유지 및 랙 단위 초고밀도 GPU 집적 완성 |

## Ⅶ. 결론

- **기술 위상/발전**: 초대형 AI 슈퍼컴퓨팅의 핵심 병목인 GPU 간 통신 대역폭을 획기적으로 확장한 사실상의 글로벌 표준 인터커넥트로서, 단일 서버 내 8개 GPU 연결에서 출발하여 GB200 NVL72 랙 스케일 전체를 72개 GPU 단일 NVLink 도메인으로 묶는 혁신적 아키텍처로 진화
- **실무 적용/통제**: 초거대 트랜스포머 분산 학습 인프라 사이징 시 텐서 병렬화(TP) 크기는 반드시 단일 NVLink 도메인 내부로 한정 배치하고, 노드 간 통신은 800G InfiniBand와 1:1 레일 최적화(Rail-optimized) 토폴로지로 계층화 연계할 것 권장
