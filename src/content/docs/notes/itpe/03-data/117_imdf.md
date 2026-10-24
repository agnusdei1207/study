---
title: "실내 매핑 데이터 포맷(IMDF, Indoor Mapping Data Format)"
author: "agnusdei1207"
date: "2026-10-25T00:16:31+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

IMDF, OGC, GeoJSON, 실내 공간정보, IPS, 디지털 트윈, BIM, 객체 계층, 피처 유형

## Ⅰ. 실내 매핑 데이터 포맷의 개요

- 핵심 요약 : 실내 공간을 **GeoJSON** (지리 데이터를 JSON으로 표현하는 형식) 기반으로 모델링하는 표준 포맷.
- 개념 : 공항, 쇼핑몰, 병원 같은 건물 내부의 공간과 시설을 피처 단위로 표현하는 실내 공간정보 포맷 (**IMDF**, Indoor Mapping Data Format).
- 배경 및 필요성 : 실외에서는 위성 측위(GPS, Global Positioning System)로 위치를 알 수 있지만 실내에서는 신호가 약해 쓸 수 없으므로, 건물마다 다른 도면을 공통 포맷으로 맞춰야 실내 공간정보를 여러 서비스가 함께 쓸 수 있음.
- 주요 목적 : 실내 지도의 상호 운용성 확보와 실내 위치 기반 서비스의 기준 데이터 마련.
- 특징 : 계층형 피처 모델과 GeoJSON 기반 표준 구조.

## Ⅱ. IMDF의 특징 및 장점

- 핵심 요약 : 계층 모델과 표준 기반 상호 운용이 실내 측위와 디지털 트윈 연계의 바탕이 되는 구조.

1. **계층 모델** (Venue → Building → Level → Unit) : 건물을 상위에서 하위로 포함 관계로 나눔 → 층별, 공간별 검색과 갱신 단위가 명확해짐.
2. **OGC** (Open Geospatial Consortium) 표준 : GeoJSON 기반 구조를 공통 규약으로 따름 → 서로 다른 시스템 간 데이터 교환 호환성 확보.
3. **IPS** (Indoor Positioning System, 실내 측위 시스템) 연동 : BLE나 Wi-Fi 비콘의 신호로 위치를 추정하고 그 결과를 IMDF 도면 위에 표시 → 실내 위치 서비스의 기준 지도 역할.
4. **디지털 트윈** (Digital Twin) 연계 : **BIM** (Building Information Modeling) 모델을 경량화해 IoT (Internet of Things) 센서 값을 겹쳐 보여줌 → 건물 상태를 공간 단위로 모니터링.
5. 경량 렌더링 : 설계 원본 대신 GeoJSON 기반 경량 데이터를 쓰므로 웹과 모바일에서 빠르게 그릴 수 있음.

## Ⅲ. 객체 계층 흐름

- 핵심 요약 : Venue에서 Level로 내려가며 Unit, Opening, Anchor가 층 안에 배치되는 포함 관계 구조.
- 피처 유형 : Venue, Building, Footprint, Level, Unit, Opening, Amenity, Anchor, Relationship 등으로 역할을 분리.

```text
[ IMDF 객체 계층 ]

Venue (부지 경계)
      ↓
Building (건물, Footprint 외곽)
      ↓
Level (층)
      ↓
Unit (방·복도)
Opening (출입구)
Amenity (편의시설)
Anchor (POI 기준점)
```

- 구축 흐름 : 설계 원본인 BIM을 IMDF로 변환하고 검증을 거친 뒤 서비스에 배포함.

```text
[ IMDF 구축 흐름 ]

BIM 설계 원본
      ↓
IMDF 자동 변환 (피처 추출)
      ↓
OGC 위상 검증
      ↓
서비스 배포 (IPS·디지털 트윈)
```

## Ⅳ. 피처 유형 비교

- 핵심 요약 : 기하 형태와 역할로 피처 유형을 구분해 데이터 종류에 맞는 표현을 고름.

| 피처 | 기하 형태 | 역할 |
| --- | --- | --- |
| Venue | Polygon | 전체 부지 경계 |
| Building | Polygon | 건물 외곽 |
| Level | 층 단위 묶음 | 층 서열(ordinal)과 층 이름(short_name) |
| Unit | Polygon | 방, 복도, 엘리베이터 홀 |
| Opening | LineString | 문과 개방 구간 |
| Anchor | Point | POI 기준점 |
| Relationship | ID 참조 | 포함과 소속 관계 |

- 선택 기준 : 면적이 있는 공간은 Polygon, 통로와 문은 LineString, 지점 정보는 Point로 나누어 데이터 종류에 맞춤.

## Ⅴ. 한계와 방안

- 핵심 요약 : 수직 연결 위상 오류, 좌표 정합 오차, 현행화 지연을 BIM 변환과 검증, 위치 보정, 연계 저작 도구로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 수직 연결성 모델링 | 복층, 메자닌 등 비정형 구조에서 층 간 위상 오류 발생 | BIM 자동 변환 후 OGC 위상 검증 | 위상 오류 건수 |
| 좌표 정합 오차 | WGS84 (World Geodetic System 1984)와 건물 로컬 좌표계의 변환 오차로 위치가 어긋남 | 앵커 포인트 기준 보정, 칼만 필터와 PDR(Pedestrian Dead Reckoning) 융합 | 위치 정확도 |
| 데이터 현행화 지연 | 입주 테넌트 변경을 수작업으로 반영해 갱신이 늦어짐 | FMS(Facility Management System) 연계 웹 저작 도구 사용 | 갱신 소요 기간 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : 실내 공간정보를 일회성 구축이 아닌 상시 관리 데이터로 다루는 거버넌스와 공통 기반이 필요함.

1. 데이터 거버넌스 : 건물 공간정보의 구축 주체와 갱신 책임을 명확히 정하고, 신규 건물에는 IMDF 납품 절차를 기본 요건으로 두는 방안을 검토할 만함.
2. 공통 기반 공유 : 건물 단위의 실내 데이터를 여러 서비스가 함께 재사용하도록 공유 저장소를 두면, 같은 도면을 서비스마다 다시 만드는 중복 구축을 줄일 수 있음.
3. 디지털 트윈 확장 : 실내 지도를 IoT 센서 데이터와 묶어 시설 관리 용도로 넓히면, 위치 서비스에 머물던 데이터의 활용 범위가 커짐.

## Ⅶ. 결론

- 핵심 요약 : IMDF는 실내 공간정보를 GeoJSON 기반 표준으로 묶어 위치 서비스와 디지털 트윈의 공통 기준선이 되는 포맷임.
- 시사점 : 데이터 품질은 BIM 변환과 검증 체계 위에서 유지되므로, 표준 포맷 도입과 함께 현행화 절차를 갖춰야 활용 가치가 커짐.

참고 : [OGC IMDF](https://www.ogc.org/standards/imdf/)
