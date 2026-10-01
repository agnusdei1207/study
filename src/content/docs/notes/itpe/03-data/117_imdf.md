---
title: "실내 매핑 데이터 포맷(IMDF)"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 스마트 실내 공간 정보의 표준, IMDF의 개요

### 가. IMDF(Indoor Mapping Data Format)의 정의
- 공항, 쇼핑몰, 병원, 대형 전시장 등 복잡한 실내 공간의 구조(층, 방, 통로, 출입구, 편의시설 등)를 디지털 지도로 모델링하고 모바일 및 웹 애플리케이션에서 상호 운용할 수 있도록 OGC(Open Geospatial Consortium)에서 커뮤니티 표준으로 제정한 GeoJSON 기반의 데이터 교환 포맷.
- 애플(Apple)에 의해 초기 개발되어 실내 위치 추적(Indoor Positioning) 및 내비게이션의 산업 표준으로 안착함.

### 나. 실외 GIS(GPS)와 실내 매핑(IMDF)의 핵심 차이
- **실외 GIS** : 위도/경도 중심의 2D 평면 공간 모델링, GPS 위성 신호 직접 수신 기반.
- **실내 IMDF** : 3차원 수직 층(Level/Floor), 출입 가능 여부(Pedestrian Walkway), 비콘(Beacon)/Wi-Fi 실내 측위 인프라 연계를 포함한 다층 계층형 모델링.

---

## Ⅱ. IMDF의 데이터 모델 및 핵심 객체 계층 구조

### 가. IMDF의 계층적 피처(Feature) 모델

```text
[ IMDF 객체 계층도 ]
[Venue (장소/경기장)]
        |
        v
    [Building (개별 건물)]
        |
        v
    [Footprint (건물 바닥 외곽선)]
        |
        v
    [Level (층 단위 슬라이스: 1F, B1F)]
        |
        +---> [Unit (개별 방, 매장, 화장실 공간 폴리곤)]
        +---> [Opening (출입문, 창문 등 경계)]
        +---> [Anchor (POI 레이블 표시 중심점)]
        +---> [Kiosk, Amenity, Occupant (편의시설, 입주자)]
```

### 나. 핵심 피처 타입 상세 설명

| 피처 유형 | 기하학적 형태 | 주요 역할 및 속성 |
| :--- | :--- | :--- |
| **Venue** | Polygon / MultiPolygon | 지리적으로 정의된 전체 사업장 또는 부지 경계 |
| **Building** | Polygon | 단일 물리적 건축물의 외곽 구조 |
| **Level** | (논리적 층 컨테이너) | `ordinal`(서열 정수), `short_name`("2F"), 고도 정보 포함 |
| **Unit** | Polygon | 벽으로 둘러싸인 물리적 방, 복도, 엘리베이터 홀 등 최소 단위 공간 |
| **Opening** | LineString | Unit 사이 또는 내외부를 연결하는 문(Door) 및 개방 구간 |
| **Amenity** | Point | 소화기, AED, ATM, 장애인 경사로 등 편의·안전 시설 POI |
| **Relationship** | 속성 참조 (JSON ID) | 층-방, 방-입주자 간의 포함 및 소속 관계를 명시적 ID 참조로 구성 |

---

## Ⅲ. IMDF와 실내 측위 기술(IPS) 및 디지털 트윈의 융합

### 가. Wi-Fi RTT 및 BLE 비콘 연동
- IMDF 지도 위에 BLE(Bluetooth Low Energy) 비콘 및 Wi-Fi AP의 물리적 설치 좌표를 Anchor 객체로 등록 $\rightarrow$ 스마트폰 센서와 핑거프린팅(Fingerprinting) 알고리즘을 결합하여 오차 1~2m 이내의 실내 길안내 구현.

### 나. 스마트 빌딩 디지털 트윈(Digital Twin)의 기초 레이어
- BIM(Building Information Modeling)의 복잡한 3D CAD 데이터를 경량화하여 웹 및 모바일에서 수 밀리초 만에 렌더링 가능한 IMDF 포맷으로 변환 후, IoT 온도·재실 센서 데이터를 실시간 오버레이.

---

## Ⅳ. 공공 및 엔터프라이즈 실내 공간정보 구축 실무 제언

- **BIM $\rightarrow$ IMDF 자동 변환 ETL 파이프라인 구축** : Revit이나 IFC 파일 등 건축 설계 도면을 수작업으로 다시 그리는 것은 막대한 공수가 소요되므로, FME(Feature Manipulation Engine) 등을 활용하여 BIM 파일에서 벽체와 룸 경계를 추출하여 IMDF GeoJSON으로 자동 정제·변환하는 파이프라인을 구축해야 함.
- **OGC 표준 준수 및 유효성 검증(Validator) 의무화** : 모바일 OS(iOS/Android)의 지도 렌더러가 비정상 종료되는 것을 방지하기 위해, Unit 폴리곤 간의 비정상적인 겹침(Overlap)이나 Level 서열 누락을 사전에 스캔하는 자동화 검증 도구를 배포 프로세스에 필수 연계할 것을 제언함.
