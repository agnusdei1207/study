---
title: "위성·공중·지상 통합망(SATIN, Satellite-Air-Terrestrial Integrated Network)"
author: "agnusdei1207"
date: "2026-10-24T22:42:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- SATIN(Satellite-Air-Terrestrial Integrated Network), NTN(Non-Terrestrial Network), LEO(Low Earth Orbit), GEO(Geostationary Earth Orbit)
- HAPS(High Altitude Platform Station), UAV(Unmanned Aerial Vehicle), ISL(Inter-Satellite Link), 수직 핸드오버(Vertical Handover)
- 조건부 핸드오버(CHO), 도플러 천이(Doppler Shift), 동적 스펙트럼 공유(DSS), 통신 복원력(Resilience)

## Ⅰ. 위성·공중·지상 통합망(SATIN)의 개요

- 핵심 요약 : 위성, 성층권 플랫폼, 무인기, 지상망을 하나의 3차원 구조로 묶어 지구 전역의 연결성을 제공하는 통합 통신망.
- 개념 : 저궤도(LEO, Low Earth Orbit), 중궤도(MEO, Medium Earth Orbit), 정지궤도(GEO, Geostationary Earth Orbit) 위성, 성층권 플랫폼(HAPS, High Altitude Platform Station), 무인기(UAV, Unmanned Aerial Vehicle)와 지상 이동통신망을 하나의 구조로 통합한 **위성·공중·지상 통합망** (SATIN, Satellite-Air-Terrestrial Integrated Network).
- 배경 및 필요성 : 사막, 해양, 산악, 극지처럼 지상망이 닿지 않는 지역이 남아 있고, 도심항공교통(UAM, Urban Air Mobility)과 재난 대응을 위해 공중 공간까지 연결성을 보장해야 할 필요가 커짐.
- 주요 목적 : 지구 전역의 커버리지 확보, 시공간 제약 없는 연결성 제공, 지상망이 손상되어도 유지되는 **통신 복원력** (Resilience) 확보.

## Ⅱ. 위성·공중·지상 통합망(SATIN)의 특징 및 장점

- 핵심 요약 : 세 계층의 이종 링크를 하나의 프로토콜 체계로 묶어 커버리지, 복원력, 연결 지속성의 장점을 얻는 구조.

1. 3차원 계층 결합 : 우주, 공중, 지상 계층이 링크로 이어짐 → 지상망 공백을 메우는 전 지구 커버리지.
2. 위성 간 링크 : 저궤도 위성끼리 레이저 링크(ISL, Inter-Satellite Link)로 메시를 구성 → 지상 기지국을 거치지 않는 우주 백본 라우팅 가능.
3. 공중 계층 보조 : HAPS와 UAV가 중계와 에지 컴퓨팅(MEC, Multi-access Edge Computing) 노드 역할 → 트래픽이 몰리는 구역에 빠른 보조 커버리지 제공.
4. 통합 이동성 제어 : 위성과 단말 간 도플러 천이와 전파 지연을 보상하며 계층 사이를 옮겨 다니는 핸드오버 지원 → 끊김 없는 연결 유지.

## Ⅲ. 위성·공중·지상 통합망(SATIN)의 구조 (흐름)

- 핵심 요약 : 우주, 공중, 지상 계층이 인터링크와 **비지상 네트워크** (NTN, Non-Terrestrial Network) 프로토콜을 공유하며 하나의 제어 평면으로 묶이는 구조.

```text
[ 우주 계층 : LEO·MEO·GEO 위성 ]
   ↓ 위성-공중 링크
[ 공중 계층 : HAPS·UAV ]
   ↓ 피더·액세스 링크
[ 지상 계층 : 기지국·위성 게이트웨이 ]
   ↓
통합 5G/6G 코어망
```

- 우주 계층 : 여러 궤도의 위성이 ISL로 메시를 이루어 지상 경유 없이 트래픽을 전달.
- 공중 계층 : 성층권 HAPS와 UAV가 셀룰러 기지국을 보조하고 공중에서 에지 노드 역할 수행.
- 지상 계층과 코어 : 지상 기지국과 게이트웨이가 통합 코어에 접속하며, 코어의 접근·이동성 관리 기능(AMF, Access and Mobility Management Function), 세션 관리 기능(SMF, Session Management Function), 사용자 평면 기능(UPF, User Plane Function)이 세 계층의 세션을 관리.

```text
[ 통합 이동성 제어 흐름 ]

단말 위치 측정 (위성 항법 기반)
   ↓
도플러·지연 사전 보상
   ↓
계층 간 조건부 핸드오버
   ↓
끊김 없는 연결 유지
```

## Ⅳ. 위성·공중·지상 통합망(SATIN)의 비교

- 핵심 요약 : SATIN은 지상 셀룰러의 용량과 저지연, 정지궤도 위성의 광역성을 함께 취하는 중간 지점의 구조.

| 비교 축 | SATIN | 지상 셀룰러망 (5G TN, Terrestrial Network) | 독립 정지궤도 위성망 (GEO) |
| --- | --- | --- | --- |
| 통신 커버리지 | 지상·해상·공중을 포함한 전 지구 | 인구 밀집 지역 중심 | 광역이나 고위도 음영 발생 |
| 전파 지연 | 낮음 (LEO와 공중망 활용) | 가장 짧음 | 정지궤도 특성상 지연이 큼 |
| 단말 형태 | 일반 스마트폰(직접 연결)과 UAM 단말 | 일반 스마트폰, IoT 센서 | 전용 위성 안테나와 단말기 |
| 토폴로지 | 시간에 따라 바뀌는 3차원 동적 메시 | 고정 기지국 중심의 2차원 셀룰러 | 단일 홉 스타(Star) 구조 |
| 인프라 복원력 | 재해 시에도 공중·우주 링크 유지 | 지진·홍수 시 기지국 단절 | 지상 게이트웨이 손상에 취약 |

- 선택 기준 : 커버리지 공백과 재난 복원력이 중요하면 SATIN을, 도심의 대용량 트래픽이 중요하면 지상망을 우선 검토함.

## Ⅴ. 위성·공중·지상 통합망(SATIN)의 한계와 방안

- 핵심 요약 : 빈번한 핸드오버, 계층 간 주파수 간섭, 우주 방사선이 주요 한계이며, 사전 보상, 빔 제어, 내방사선 설계로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 잦은 핸드오버와 도플러 천이 | 저궤도 위성이 초고속으로 이동하여 단말의 핸드오버가 수 분 단위로 발생하고 주파수 편이가 큼 | GNSS(Global Navigation Satellite System) 위치 기반 도플러 사전 보상, 조건부 핸드오버(CHO, Conditional Handover) 도입 | 핸드오버 실패율, 주파수 오차 |
| 지상·위성 간 주파수 간섭 | 같은 주파수를 나눠 쓰면 상호 간섭으로 신호 대 잡음비(SINR, Signal-to-Interference-plus-Noise Ratio)가 급락 | 공간 분할 기반 3차원 빔포밍, 인지 무선 기반 동적 스펙트럼 공유(DSS, Dynamic Spectrum Sharing) | SINR, 간섭 발생 빈도 |
| 우주 방사선에 의한 탑재체 오류 | 기지국 기능을 위성에 직접 탑재하면 방사선으로 단일 사건 업셋(SEU, Single Event Upset)이 발생 | 내방사선 반도체 채택, 삼중 모듈 이중화(TMR, Triple Modular Redundancy), 지상 코어 중심의 기능 분할 | 비트 오류 발생 횟수 |

## Ⅵ. 위성·공중·지상 통합망(SATIN)의 기술사적 제언

- 핵심 요약 : 표준 주도권, 독자 백본, 항공 실증을 함께 추진하여 연결성 공백과 통신 종속을 동시에 줄이는 방향.

1. 국내 연구 조직은 3GPP NTN 표준의 후속 릴리스 논의에 참여하여 기고와 표준 주도권을 확보하고, 직접 단말 통신과 6G 위성 규격을 독자 군집위성 개발 계획과 함께 맞춰 나가야 한다.
2. 정부와 통신 사업자는 해저 케이블 단절이나 전시 재난에 대비하여 독자 저궤도 위성군과 지상국을 잇는 백본을 확보하고, 국가 통신 주권을 지킬 수 있는 인프라 정책을 마련해야 한다.
3. 항공 모빌리티 분야에서는 도심 공역에 5G 특화망, HAPS, 저궤도 위성을 융합한 실증 회랑을 먼저 조성하여 안전 운항 기준을 검증해야 한다.

## Ⅶ. 결론

- 핵심 요약 : SATIN은 지상망의 용량과 저지연 장점에 비지상망의 광역 커버리지와 복원력을 결합한 3차원 통신 패러다임임.
- 시사점 : 표준 주도권과 독자 인프라를 함께 확보해야 연결성 공백과 통신 종속을 동시에 줄일 수 있음.
