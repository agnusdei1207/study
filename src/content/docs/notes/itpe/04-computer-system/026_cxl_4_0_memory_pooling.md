---
title: "CXL 4.0 / 메모리 풀링 (CXL: Compute Express Link)"
author: "agnusdei1207"
date: "2026-10-24T22:24:38+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- CXL(Compute Express Link), CXL 4.0, PCIe, 캐시 일관성(Cache Coherency)
- 메모리 풀링(Memory Pooling), 메모리 공유(Memory Sharing), 패브릭 스위치(Fabric Switch), 멀티헤드 장치(Multi-Head Device)
- 분해형 아키텍처(Disaggregated Architecture), 스트랜디드 메모리(Stranded Memory), KV 캐시(Key-Value Cache)
- CXL-IDE, 계층형 메모리(Tiered Memory), 제로 카피(Zero-Copy)

## Ⅰ. CXL 4.0 / 메모리 풀링의 개요

- 핵심 요약 : **CXL** (Compute Express Link)은 PCIe 기반으로 메모리를 서버 간에 풀링·공유하여 TCO를 낮추는 분해형 인터커넥트 기술.
- 개념 : PCIe(Peripheral Component Interconnect Express) 물리 계층 위에서 CPU, GPU, 가속기와 메모리 확장 장치 사이의 **캐시 일관성** (Cache Coherency)과 바이트 단위 직접 접근을 보장하고, 여러 서버의 메모리를 하나의 풀로 묶어 동적으로 할당하는 **분해형 아키텍처** (Disaggregated Architecture) 기술.
- 배경 및 필요성 : LLM(Large Language Model)과 생성형 AI(Artificial Intelligence)로 메모리 요구량이 급증했으나, CPU(Central Processing Unit) 소켓당 DRAM(Dynamic Random-Access Memory) 채널 수에는 물리적 한계가 있고, 서버마다 쓰이지 않고 묶인 **스트랜디드 메모리** (Stranded Memory)가 낭비되므로 메모리를 서버 밖으로 풀어 공유할 체계가 필요해짐.
- 주요 목적 : 서버 간 메모리 경계 제거, **메모리 풀링**을 통한 TCO(Total Cost of Ownership) 절감, 이종 가속기 사이의 **제로 카피** (Zero-Copy) 데이터 공유 실현.

## Ⅱ. CXL 4.0 / 메모리 풀링의 특징 및 장점

- 핵심 요약 : CXL.io, CXL.cache, CXL.mem 세 프로토콜과 패브릭 기반 풀링이 결합되어 메모리 활용률과 데이터 이동 효율을 높이는 구조.

1. **CXL.io** : PCIe 기반 입출력 프로토콜로 장치 검색, 구성, DMA(Direct Memory Access), 인터럽트를 담당 → 기존 PCIe 소프트웨어 생태계를 그대로 활용.
2. **CXL.cache** : 가속기가 호스트 CPU의 메인 메모리를 캐시로 가져다 쓰도록 지원 → 가속기와 호스트 사이 데이터 복사 감소.
3. **CXL.mem** : 호스트가 가속기나 확장 카드의 메모리에 일반 로드·스토어 명령으로 접근 → 메모리 확장을 응용 코드 변경 없이 활용 가능.
4. 메모리 풀링 (Memory Pooling) : CXL 스위치 계층을 거쳐 물리 메모리를 여러 서버가 필요한 만큼 나눠 쓰는 구조 → 서버별 과다 탑재 감소와 유휴 메모리 회수.
5. **메모리 공유** (Memory Sharing) : 여러 서버가 같은 물리 메모리 영역을 캐시 일관성을 유지한 채 읽고 쓰는 방식 → 서버 간 데이터 복사 오버헤드 제거.

## Ⅲ. CXL 4.0 / 메모리 풀링의 구조 및 동작 메커니즘

- 핵심 요약 : 스위치 계층과 다중 포트 장치를 통해 여러 호스트가 하나의 메모리 풀에 연결되는 계층 구조.
- **패브릭 스위치** (Fabric Switch) : 여러 호스트 포트와 장치 포트를 연결하여 메모리 자원을 호스트별로 배분하는 CXL 네트워크 요소.
- **멀티헤드 장치** (Multi-Head Device) : 하나의 메모리 장치가 여러 호스트 포트를 가져 공유 영역을 제공하는 장치 형태.

```text
[ 메모리 풀링 구조 ]

서버 노드 A (Host CPU)
서버 노드 B (Host CPU)
        ↓ (CXL 링크)
패브릭 스위치 (Fabric Switch)
        ↓
멀티헤드 메모리 장치 (Memory Pool)
        ↓
DRAM 블록을 호스트별로 논리 할당
```

```text
[ 제로 카피 메모리 공유 흐름 ]

서버 A가 풀 영역에 데이터 기록 (Store)
        ↓
하드웨어 캐시 일관성 유지
        ↓
서버 B가 같은 주소를 읽기 (Load)
        ↓
데이터 복사 없이 즉시 사용
```

## Ⅳ. CXL 4.0 / 메모리 풀링의 비교

- 핵심 요약 : CXL 2.0, CXL 3.0, CXL 4.0은 물리 계층 속도, 연결 범위, 공유 방식이 세대별로 확장된 관계.

| 비교 항목 | CXL 1.1 / 2.0 | CXL 3.0 | CXL 4.0 |
| --- | --- | --- | --- |
| 물리 계층 | PCIe 5.0 기반 | PCIe 6.0 기반 (PAM4(4-level Pulse Amplitude Modulation) 신호) | PCIe 7.0 PHY 기반 (128 GT/s) |
| 토폴로지 | 1.1은 직접 연결, 2.0은 스위치 기반 풀링 | 다단 스위치, 멀티헤드 장치 | 다중 랙 규모로 풀 범위 확장, 번들 포트와 리타이머 지원 |
| 메모리 공유 | 주로 메모리 할당(분할) 중심 | 여러 호스트 간 캐시 일관성 공유 | 공유 범위 확장, 오류 보고와 메모리 스페어링 강화 |
| 주요 적용 분야 | 서버 메모리 용량 확장, 서버 간 풀링 | 랙 단위 동적 메모리 풀링 | 다중 랙 AI 서버를 잇는 메모리 패브릭 |

- 선택 기준 : 단일 서버의 용량 확장이면 CXL 1.1 또는 2.0 장치로 충분하고, 여러 호스트의 공유 일관성과 랙 단위 풀링이 필요하면 CXL 3.0 이후 세대를 검토하는 것이 적절함.

## Ⅴ. CXL 4.0 / 메모리 풀링의 한계와 방안

- 핵심 요약 : 추가 지연, 공유 보안, 소프트웨어 미성숙을 계층형 메모리, CXL-IDE, 인지형 할당 체계로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 추가 메모리 지연 | PCIe 링크와 스위치를 거쳐 로컬 DRAM보다 접근 지연이 길어짐 → 메모리 집약 워크로드 성능 저하 | **계층형 메모리** (Tiered Memory) 구성, **DAMON** (Data Access MONitor)으로 핫·콜드 데이터를 식별해 자동 이동 | 메모리 접근 지연, 계층 간 이동 빈도 |
| 공유 메모리 보안과 테넌트 격리 | 여러 호스트나 VM이 같은 풀을 쓰면서 데이터 오염과 사이드 채널 노출 위험 | **CXL-IDE** (Integrity and Data Encryption) 적용, 하드웨어 수준 접근 제어 정책 | 접근 위반 탐지 건수 |
| 소프트웨어 및 OS 지원 미성숙 | 기존 애플리케이션이 단일 **NUMA** (Non-Uniform Memory Access) 구조를 가정해 동적 풀 할당을 인식하지 못함 | CXL 인지형 메모리 할당 라이브러리(예: Memkind) 도입, 리눅스 커널의 CXL 메모리 서브시스템 개선 추적 | 애플리케이션 적용률, 할당 실패율 |

## Ⅵ. CXL 4.0 / 메모리 풀링에 대한 기술사적 제언

- 핵심 요약 : 워크로드 설계, 자원 회수, 차세대 패브릭 검증을 단계적으로 묶어 메모리 풀링을 데이터센터 운영 모델로 정착.

1. LLM 추론 서비스를 운영하는 AI 인프라팀은 **KV 캐시** (Key-Value Cache)를 CXL 공유 메모리 풀에 상주시켜, 여러 추론 인스턴스가 같은 캐시를 복사 없이 참조하도록 설계한다.
2. 데이터센터 운영팀은 서버별로 과다 탑재된 DRAM을 풀로 옮기고 유휴 메모리 회수율을 지표로 관리하여, 설비 투자(CAPEX, Capital Expenditure) 증가를 줄이는 방향으로 자원 계획을 세운다.
3. 네트워크·하드웨어 조직은 광 연결 기술의 도입 동향을 추적하면서 랙 간 패브릭 시험 환경을 미리 구축하여, 표준 세대가 바뀔 때 전환 비용을 낮춘다.

## Ⅶ. 결론

- 핵심 요약 : CXL은 PCIe 기반의 캐시 일관성 메모리 풀링으로 분해형 아키텍처를 실현하는 기술.
- 시사점 : 메모리를 서버 내부 자원이 아닌 공유 자원으로 다루는 전환이 진행되므로, 지연과 보안, 소프트웨어 지원을 함께 관리하는 것이 도입의 전제 조건이 됨.
