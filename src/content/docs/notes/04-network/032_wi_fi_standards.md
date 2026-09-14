---
sidebar:
  order: 32
  label: "032. Wi-Fi 표준"
  badge:
    text: "기출 · 50%"
    variant: note
title: "Wi-Fi 무선 LAN 표준 : 802.11ac•ax•be (Wi-Fi Standards)"
date: "2026-09-07T14:00:00+09:00"
tags:
  - "notes-network"
weight: 32
extra:
  question_no: "32"
  source_status: "기출"
  source_history: "125회, 134회"
  priority: 50
  priority_note: "IEEE 802.11ac, 802.11ax(Wi-Fi 6), 802.11be(Wi-Fi 7) 진화 및 비교"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **IEEE 802.11**: 비면허 주파수 대역에서 무선 LAN의 물리(PHY) 및 MAC 계층을 정의하는 국제 무선 통신 표준.
- **AP (Access Point)**: 유선 이더넷 백본망(DS)과 무선 단말(STA) 간에 프레임 변환 및 전파 송수신을 중계하는 무선 기지국 장비.

</details>

- 정의/개념: 비면허 대역(2.4GHz, 5GHz, 6GHz)에서 **대역폭 확장, 고차 변조(4096-QAM) 및 다중 링크(MLO)를 진화시킨 무선 LAN 표준 규격(IEEE 802.11ac/ax/be)**
- 배경/필요성: 초기 무선 LAN 규격(802.11a/b/g/n)의 단일 링크 대역폭 한계와 CSMA/CA 매체 경합으로 인해 스마트폰, IoT 단말이 밀집된 고밀도(High-Density) 환경에서 심각한 주파수 충돌, 패킷 지연 및 전송 효율 급감이 발생하고, 4K/8K 영상 스트리밍과 AR/VR 메타버스 등 차세대 서비스의 고속·저지연 요구를 수용할 수 없는 한계를 극복하기 위해, 채널 대역폭 확장(최대 320MHz), 고차 변조(4096-QAM), 다중 접속(OFDMA 및 MU-MIMO), 다중 대역 동시 결합(MLO: Multi-Link Operation)으로 진화한 IEEE 802.11ac/ax/be 무선 LAN 표준을 도입하여 **기가비트/수십 기가비트급 무선 전송 용량과 유선 이더넷 수준의 결정론적 저지연 연결성**을 달성할 필요

#### 한줄 요약
- 무선 표준의 발전에 발맞추어 고차 변조와 OFDMA 및 MLO 기술을 적용하여 접속 효율과 전송 속도를 높여야 한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **OFDMA (Orthogonal Frequency Division Multiple Access)**: 단일 채널을 복수의 자원 단위(RU)로 세분화하여 다수 단말이 동시 통신하는 기술.
- **MLO (Multi-Link Operation)**: 2.4GHz, 5GHz, 6GHz 대역의 복수 링크를 단일 단말이 동시 결합하여 대역폭 증대 및 지연을 최소화하는 기술.

</details>

- **세대별 대역 확장**: Wi-Fi 5(5GHz) $\to$ Wi-Fi 6/6E(2.4/5/6GHz) $\to$ Wi-Fi 7(최대 320MHz 초광대역 및 MLO)
- **고차 변조 진화**: 256-QAM(11ac) $\to$ 1024-QAM(11ax) $\to$ **4096-QAM(11be, 4K-QAM)** 심볼당 비트 전송률 향상
- **고밀도 다중 접속 최적화**: BSS Coloring, Target Wake Time(TWT), UL/DL MU-MIMO 다중 단말 수용

#### 한줄 요약
- 4096-QAM 변조, 320MHz 채널 폭, OFDMA 다중 접속, MLO 다중 링크 결합을 체계적으로 구현해야 한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **BSS (Basic Service Set)**: 단일 AP와 이에 결합(Associate)된 무선 단말(STA)들로 구성되는 기본 무선 셀 단위.
- **Distribution System (분배 시스템, DS)**: 복수의 AP(BSS)를 연결하여 로밍 및 유선망 연동을 제공하는 백본 스위치 네트워크.

</details>

```text
[Wi-Fi 무선 LAN 아키텍처]
  │
  ├─ [무선 단말 영역] ── Stations (STA)
  │     ├─ [단말 무선 NIC] (트라이밴드 2.4/5/6GHz 지원)
  │     └─ [MLO 제어기] (다중 주파수 대역 동시 결합)
  │
  ├─ [무선 접속점 영역] ── Access Point (AP)
  │     ├─ [RF 트랜시버] (독립 다중 RF 인터페이스)
  │     ├─ [MAC/PHY 스케줄러] (OFDMA Multi-RU, 4096-QAM)
  │     └─ [BSS 관리 셀] (Basic Service Set 커버리지)
  │
  └─ [유선 분배 백본] ── Distribution System (DS)
        ├─ [유선 스위칭망] (AP 간 802.3 이더넷 연결)
        ├─ [로밍 브리지] (BSS 간 무단절 핸드오버)
        └─ [게이트웨이 연동] (WAN/인터넷 백본 접속)
```

- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| 무선 단말 (STA) | AP와 결합하여 **MLO 다중 대역 동시 결합 송수신** |
| 무선 접근점 (AP) | 802.11/802.3 **프레임 상호 브리지 및 무선 매체 스케줄링** |
| 기본 서비스 세트 (BSS) | 단일 AP 전파 도달 범위 내 **무선 통신 셀 도메인 유지** |
| 분배 시스템 (DS) | 복수 BSS 간 **단말 로밍 및 유선 백본 연결 제공** |

#### 한줄 요약
- AP는 BSS 내부 무선 프레임을 중계하고 유선 DS 백본은 셀 간 무단절 로밍을 지원해야 한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **Wi-Fi 접속 5단계**: 매체 탐색 $\to$ 신원 인증 $\to$ 링크 결합 $\to$ 4-Way Handshake $\to$ 무선 통신 개시.

</details>

```text
[Wi-Fi 단말 접속 수립 흐름] (진행 ①→④, 진입, ④ PTK·GTK 유도 완료 후에만 데이터 개시)
  │
  ├─ [무선 단말 STA] (① 비콘 수신(Passive) 또는 프로브 송출(Active)로 매체 탐색)
  │
  ├─ [AP 인증기] (② WPA3-Personal(SAE) 또는 WPA3-Enterprise(802.1X EAP) 상호 인증)
  │
  ├─ [AP MAC/PHY 스케줄러] (③ MLO 다중 링크·320MHz 채널 폭·MIMO 규격 협상 및 Association 완료)
  │
  └─ [4-Way Handshake 키 유도기] (④ PTK·GTK 생성 후 4096-QAM·OFDMA 데이터 송수신 개시)
```

분기 결과: 매체 탐색 방식에 따라 비콘 기반 수동 탐색 또는 프로브 기반 능동 탐색으로 분기되고, 상호 인증 및 결합을 거쳐 4-Way Handshake 키 유도 완료 후 데이터 통신으로 분기된다.

#### 한줄 요약
- 탐색 방식에 맞추어 접속을 초기화하고 WPA3 인증과 4-Way Handshake 키 유도를 완료해야 한다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **Wi-Fi 5 (802.11ac)** vs **Wi-Fi 6/6E (802.11ax)** vs **Wi-Fi 7 (802.11be)**.

</details>

| 비교 항목 | Wi-Fi 5 (802.11ac) | Wi-Fi 6/6E (802.11ax) | Wi-Fi 7 (802.11be) |
|:---|:---|:---|:---|
| **지원 주파수 대역** | 5 GHz 전용 | 2.4 GHz, 5 GHz, **6 GHz (6E)** | 2.4 GHz, 5 GHz, **6 GHz 전 대역** |
| **최대 채널 대역폭** | 160 MHz | 160 MHz | **320 MHz (초광대역 2배)** |
| **최고 변조 방식** | 256-QAM | 1024-QAM (10-bit) | **4096-QAM (12-bit, 4K-QAM)** |
| **다중 접속 방식** | OFDM | **OFDMA (자원 단위 RU 분할)** | **OFDMA + Multi-RU 복합 할당** |
| **핵심 다중화 기술** | DL MU-MIMO (최대 4x4) | UL/DL MU-MIMO (최대 8x8) | **MLO (다중 링크 동시 결합), 16x16 MIMO** |
| **이론상 최고 전송률**| 약 6.9 Gbps | 약 9.6 Gbps | **약 46 Gbps (4.8배 향상)** |

#### 한줄 요약
- 802.11ac(5GHz 전용), 802.11ax(고밀도 OFDMA), 802.11be(320MHz 및 MLO) 특성에 맞추어 인프라를 업그레이드해야 한다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **BSS Coloring**: 동일 채널을 사용하는 인접 BSS 프레임에 색상 식별 비트를 부여하여 간섭 신호를 무시하고 공간을 재사용(Spatial Reuse)하는 기술.
- **Airtime Fairness**: 저속 구형 단말의 전파 독점을 방지하고 단말별 에어타임 점유 시간을 균등 분배하는 알고리즘.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 동일 채널 인접 AP 간섭으로 인한 처리량 저하 및 무선 지연 | **Wi-Fi 6 `BSS Coloring (공간 재사용)` 및 동적 임계치 적용** | 인접 셀 간 간섭 회피 및 실효 대역폭 3배 향상 |
| WPA2 사전 대입 공격(Dictionary Attack) 및 패킷 스니핑 보안 취약점 | **`WPA3-Personal (SAE 동시 인증)` 및 WPA3-Enterprise 의무화** | 오프라인 사전 공격 차단 및 순방향 비밀성 보장 |
| 레거시 저속 단말(802.11b/g/n)의 전파 독점으로 고속 단말 지연 | **`Airtime Fairness (에어타임 공평성)` 및 5G/6GHz 밴드 스티어링** | 고속 단말 전송 기회 보장 및 트래픽 분산 |
| 6GHz 초고주파수 대역의 벽면 투과 손실 및 전파 도달 거리 축소 | **`Wi-Fi 7 MLO 링크 집성` 및 AP 밀집 배치(High-Density AP)** | 음영 지역 해소 및 무중단 고속 연결 유지 |

#### 한줄 요약
- BSS Coloring 공간 재사용, WPA3 보안 의무화, Airtime Fairness, MLO 결합 설정을 체계적으로 적용해야 한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **Wi-Fi 8 (IEEE 802.11bn UHR)**: 초고속 전송률 경쟁을 넘어 실제 체감 품질(QoE), 결정론적 저지연 및 링크 신뢰성을 극대화하기 위해 개발 중인 차세대 초고신뢰성 무선 LAN 표준.

</details>

- 가정, 엔터프라이즈 오피스, 스마트 팩토리 및 공공 인프라를 아우르는 보편적이고 핵심적인 무선 액세스 네트워크 표준 기술로 확립.
- 최근에는 단순 속도 증대를 넘어 2.4/5/6GHz 대역을 동시 결합하여 저지연 및 고신뢰성을 제공하는 Wi-Fi 7(802.11be) 및 차세대 Wi-Fi 8(UHR)로 진화하고 있으며, 실무 무선망 설계 시에는 WPA3-SAE 보안 의무화, BSS Coloring 공간 재사용 활성화, 멀티기가비트(PoE++/10GbE) 유선 백본 연동을 결합하여 고품질 무선 인프라를 구축.

#### 한줄 요약
- Wi-Fi 표준은 320MHz 대역폭, 4096-QAM, MLO 기술을 통해 진화하며, WPA3와 BSS Coloring을 결합하여 고보안 무선 인프라를 실현해야 한다.
