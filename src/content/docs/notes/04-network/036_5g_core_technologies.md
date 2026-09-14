---
sidebar:
  order: 36
  label: "036. 5G 3대 서비스"
  badge:
    text: "기출 · 30%"
    variant: note
title: "5G 3대 서비스 시나리오 : eMBB•URLLC•mMTC (5G Services)"
date: "2026-09-07T14:00:00+09:00"
tags:
  - "notes-network"
weight: 36
extra:
  question_no: "36"
  source_status: "기출"
  source_history: "128회"
  priority: 30
  priority_note: "ITU-R 5G 3대 서비스 시나리오 및 네트워크 슬라이싱 연계"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **eMBB (Enhanced Mobile Broadband)**: 최대 20Gbps 다운링크와 광대역 주파수를 통해 대용량 멀티미디어를 전송하는 초고속 서비스.
- **URLLC (Ultra-Reliable Low Latency)**: 무선 구간 1ms 이하 지연과 99.999% 무결성 신뢰도를 보장하는 초고신뢰 저지연 서비스.
- **mMTC (Massive Machine Type)**: $1\text{km}^2$ 당 100만 개 이상의 저전력 센서 단말을 수용하는 대규모 사물 통신 서비스.

</details>

- 정의/개념: ITU-R(IMT-2020)이 정의한 5G 3대 서비스로 **초고속(eMBB), 초저지연·초고신뢰(URLLC), 대규모 접속(mMTC)을 단일 망에 분할 수용하는 통신 체계**
- 배경/필요성: 스마트폰 데이터 통신 중심의 4G LTE 단일 모바일 광대역(MBB) 아키텍처로는 최대 20Gbps 다운링크의 초고용량 실감 미디어, 1ms 이하 지연과 99.999% 무결성을 요구하는 자율주행(V2X)/스마트팩토리 제어, $1\text{km}^2$ 당 100만 개 이상의 저전력 센서 단말이 결합하는 대규모 IoT 인프라 요구를 단일 물리망에서 동시에 충족할 수 없는 한계를 극복하기 위해, 서비스별 요구 특성에 맞추어 초고속(eMBB), 초저지연·초고신뢰(URLLC), 대규모 사물 통신(mMTC)으로 역할을 분화하고 End-to-End 네트워크 슬라이싱(Network Slicing) 및 MEC로 격리 수용하는 ITU-R 5G 3대 서비스 프레임워크를 도입하여 **단일 물리 인프라 상에서의 이종 산업 워크로드별 맞춤형 QoS 보증 및 무선 스펙트럼 효율 향상**을 달성할 필요

#### 한줄 요약
- eMBB(초고속), URLLC(초저지연/고신뢰), mMTC(초연결)를 네트워크 슬라이싱으로 단일 인프라에 통합해야 한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **Network Slicing**: 단일 물리 5G 네트워크를 가상화(NFV/SDN)하여 eMBB, URLLC, mMTC 전용의 독립 가상망으로 격리 제공하는 기술.
- **5QI (5G QoS Identifier)**: 5G 서비스별 지연 허용 한도, 패킷 손실률, 우선순위를 정의하는 QoS 식별자.

</details>

- **eMBB**: 밀리미터파(mmWave), Massive MIMO, 빔포밍을 통한 **최대 20Gbps 고속 대역폭 제공**
- **URLLC**: 가변 부반송파(SCS), Mini-slot 선점형 스케줄링 및 MEC 전진 배치를 통한 **1ms 저지연 달성**
- **mMTC**: 협대역(NB-IoT), 저전력 수면 모드(PSM/eDRX)를 통한 **100만 개/$\text{km}^2$ 단말 수용**

#### 한줄 요약
- eMBB는 대역폭, URLLC는 저지연과 고신뢰성, mMTC는 저전력 대규모 접속 요구사항을 만족해야 한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **UPF (User Plane Function)**: 5G 코어에서 실제 사용자 데이터 트래픽의 고속 라우팅 및 QoS 집행을 전담하는 데이터 플레인 노드.
- **MEC (Mobile Edge Computing)**: 지연 시간을 단축하기 위해 기지국(gNB) 인접 위치에 컴퓨팅 자원과 로컬 UPF를 배치하는 아키텍처.

</details>

```text
[5G 3대 서비스 아키텍처]
  │
  ├─ [무선 접속망 영역] ── 5G RAN (gNodeB)
  │     ├─ [가변 뉴머롤로지] (SCS 15~120kHz 동적 분할)
  │     ├─ [Massive MIMO] (eMBB 대용량 빔포밍)
  │     └─ [Mini-slot 선점] (URLLC 저지연 스케줄링)
  │
  ├─ [네트워크 슬라이스] ── Network Slices
  │     ├─ [eMBB 슬라이스] (광대역 멀티미디어 전송)
  │     ├─ [URLLC 슬라이스] (고신뢰 1ms 지연 보장)
  │     └─ [mMTC 슬라이스] (대규모 저전력 센서 수용)
  │
  └─ [코어망 분기 처리] ── 5G Core & Edge
        ├─ [중앙 집중형 UPF] (대용량 인터넷 백본 연동)
        ├─ [로컬 MEC & UPF] (기지국 인접 LBO, 저지연)
        └─ [경량화 제어평면] (AMF/SMF 대규모 시그널링)
```

- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| gNB 가변 뉴머롤로지 | 부반송파 간격(SCS 15~120kHz)과 슬롯의 **서비스별 동적 최적화** |
| 로컬 UPF / MEC | 기지국 인접 로컬 트래픽 브레이크아웃(LBO)으로 **왕복 지연 1ms 보장** |
| 중앙 집중형 UPF | 인터넷 백본 연동 기반 **대용량 트래픽 고속 기가비트 라우팅** |
| 경량 제어 평면 (AMF/SMF) | 대규모 센서 단말 시그널링의 **경량화 흡수 및 절전 관리** |

#### 한줄 요약
- 서비스 요구사항에 따라 UPF를 중앙 또는 엣지 MEC로 분산 배치하여 최적의 전송 경로를 제공해야 한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **Mini-slot (비슬롯 기반 스케줄링)**: 표준 14개 심볼 슬롯을 기다리지 않고 2~7개 심볼 단위로 즉시 무선 자원을 선점하는 URLLC 전용 스케줄링.

</details>

```text
[5G 서비스 분기·슬라이스 처리 흐름] (진행 ①→③, ② 서비스 유형별 경로 분기)
  │
  ├─ [단말 접속 식별기] (① S-NSSAI·5QI 기반 서비스 요구 분류)
  │
  ├─ [eMBB 경로] (② mmWave·Massive MIMO 후 중앙 UPF 라우팅으로 대역폭 확보)
  │
  ├─ [URLLC 경로] (② Mini-slot 선점 및 로컬 MEC UPF 직결로 1ms 저지연 확보)
  │
  ├─ [mMTC 경로] (② NB-IoT 협대역 채널과 PSM/eDRX 절전 구성으로 배터리 확보)
  │
  └─ [E2E SLA 관리기] (③ 슬라이스별 SLA 계측 및 보장 후 데이터 전송 완료)
```

분기 결과: **S-NSSAI 및 5QI**를 식별하는 ①단계를 거쳐 ②단계에서 서비스 요구 특성에 따라 대역폭 중심의 eMBB, 로컬 MEC 직결 기반 저지연 중심의 URLLC, 경량 제어평면 기반 저전력 중심의 mMTC 경로로 분기되어 각각의 독립적 SLA를 보장하는 경로로 귀결된다.

#### 한줄 요약
- 단말 요구 특성에 따라 슬라이스를 분기하고 로컬 MEC 및 무선 스케줄링을 차등 적용하여 SLA를 보장해야 한다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **PSM (Power Saving Mode)**: 단말이 데이터 송수신 후 수신 회로를 끄고 깊은 수면 상태로 진입하여 배터리를 수년간 유지하는 기술.

</details>

| 비교 항목 | 초고속 통신 (eMBB) | 초저지연 통신 (URLLC) | 대규모 사물 통신 (mMTC) |
|:---|:---|:---|:---|
| **핵심 성능 목표** | **최대 20Gbps (체감 100Mbps)** | **무선 1ms (E2E 5ms 이하), 99.999%** | **$10^6 \text{ devices}/\text{km}^2$, 배터리 10년** |
| **주요 무선 기술** | **mmWave (28GHz), Massive MIMO** | **Mini-slot, Preemption, 가변 SCS** | **NB-IoT, eMTC, PSM, eDRX** |
| **코어망 아키텍처**| 대용량 패킷 스위칭 (중앙 UPF) | **MEC (모바일 엣지 컴퓨팅) 전진 배치**| 제어 평면 시그널링 최적화 코어 |
| **주요 적용 분야** | 4K/8K 실시간 중계, AR/VR, 홀로그램 | **자율주행(V2X), 원격 수술, 스마트팩토리**| 원격 검침, 환경 센서, 스마트 물류 |

#### 한줄 요약
- eMBB는 대역폭(20Gbps), URLLC는 1ms 저지연과 신뢰성, mMTC는 대규모 연결($10^6/\text{km}^2$)을 목표로 한다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **Preemption (선점형 스케줄링)**: URLLC 긴급 패킷 발생 시 이미 진행 중인 eMBB 전송 자원을 즉시 중단하고 URLLC 패킷을 최우선 전송하는 기술.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 대용량 eMBB 트래픽 버스트로 인한 URLLC 트래픽 지연 및 간섭 | **`선점형 스케줄링(Preemption)` 및 무선 하드 슬라이싱(Hard Slicing)** | eMBB 간섭 차단 및 URLLC 1ms 지연 시간 SLA 보증 |
| 코어망 원거리 전송 지연으로 인한 URLLC 종단 지연(5ms) 초과 | 기지국 인접 **`MEC(Mobile Edge Computing) 및 분산 로컬 UPF` 구축** | 물리적 전송 거리 단축 및 E2E 저지연 달성 |
| 수백만 mMTC 단말의 동시 재접속 시 제어 평면(AMF/SMF) 시그널링 폭증 | **접속 시도 `백오프(Back-off) 제어` 및 비접속(Connectionless) 전송** | 제어 평면 과부하 방지 및 코어망 안정성 유지 |
| 28GHz 밀리미터파(mmWave) 대역의 높은 경로 손실 및 장애물 차단 | **`빔포밍(Beamforming)` 및 소형 기지국(Small Cell) 고밀도 구축** | 전파 도달 거리 극복 및 음영 지역 해소 |

#### 한줄 요약
- 선점형 스케줄링, MEC 로컬 UPF, 백오프 접속 제어, 빔포밍 스몰셀을 통해 서비스별 간섭을 방지하고 품질을 보장해야 한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **Small Cell (소형 기지국)**: 수십 미터~수백 미터 반경을 커버하여 고주파수 감쇄를 극복하고 용량을 증대시키는 저전력 무선 기지국.

</details>

- 단순한 모바일 통신을 넘어 스마트 시티, 커넥티드 카, 스마트 팩토리, 원격 의료 등 전 산업의 디지털 전환을 지원하는 **5G/5G-Advanced 및 6G의 핵심적인 서비스 분류 및 망 설계 표준 체계**로 확립.
- 실무 무선 통신망 구축 시에는 **eMBB 버스트로부터 URLLC 품질을 보호하는 선점형 스케줄링(Preemption)**, **종단 지연 단축을 위한 기지국 인접 로컬 UPF/MEC 전진 배치**, **수백만 센서의 시그널링 폭증을 방어하는 C-Plane 백오프 제어**를 결합하여 엄격한 서비스 SLA를 완성.

#### 한줄 요약
- 5G 3대 서비스는 eMBB, URLLC, mMTC의 차별화된 요구를 네트워크 슬라이싱과 MEC를 통해 단일 망에서 실현하는 핵심 서비스 체계로 구축해야 한다.
