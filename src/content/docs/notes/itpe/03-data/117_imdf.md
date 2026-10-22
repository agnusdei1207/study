---
title: "실내 매핑 데이터 포맷(IMDF, Indoor Mapping Data Format)"
author: "agnusdei1207"
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

## 연관 키워드

**IMDF(Indoor Mapping Data Format)**, **OGC**, **GeoJSON**, **실내 매핑**, **IPS(Indoor Positioning System)**, **디지털 트윈**, **BIM**

## Ⅰ. 개요

- 핵심 요약 : **IMDF**는 복잡한 실내 공간을 GeoJSON 기반으로 모델링하는 OGC 커뮤니티 표준.
- 목적 : 공항·쇼핑몰·병원 등 실내 지도의 상호 운용성 확보.
- 배경 : 실외 GPS 불가 실내 환경 → 표준화된 실내 지도 포맷 필요.
- 특징 : 계층적 피처 모델, OGC 표준, IPS·디지털 트윈 연동.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **계층 모델·OGC 표준·IPS 연동**으로 실내 공간정보 표준화.
- **계층 모델** : Venue→Building→Level→Unit/Opening/Anchor.
- **OGC 표준** : GeoJSON 기반 상호 운용성.
- **IPS 연동** : BLE/Wi-Fi 비콘으로 1~2m 위치 추적.
- **디지털 트윈** : BIM 경량화 + IoT 센서 오버레이.
- **경량 렌더링** : 웹·모바일 수 밀리초 렌더링.

## Ⅲ. 객체 계층 흐름

- 핵심 요약 : **Venue→Building→Level→Unit/Opening/Anchor** 계층 구조.
- 피처 유형 : Venue, Building, Level, Unit, Opening, Amenity, Relationship.

```text
[ IMDF 객체 계층 ]

[Venue (장소/부지)]
        |
        v
    [Building (건물)]
        |
        v
    [Footprint (외곽선)]
        |
        v
    [Level (층)]
        |
        +---> [Unit (방/매장)]
        +---> [Opening (출입문)]
        +---> [Anchor (POI 중심점)]
        +---> [Amenity (편의시설)]
```

## Ⅳ. 피처 유형 비교

- 핵심 요약 : **기하 형태·역할**로 피처 유형 구분.

| 피처 | 기하 형태 | 역할 |
|---|---|---|
| Venue | Polygon | 전체 부지 경계 |
| Building | Polygon | 건물 외곽 |
| Level | 논리 컨테이너 | 층(ordinal, short_name) |
| Unit | Polygon | 방/복도/엘리베이터 홀 |
| Opening | LineString | 문/개방 구간 |
| Amenity | Point | 편의·안전 시설 POI |
| Relationship | ID 참조 | 포함/소속 관계 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **수직 연결성·좌표 정합·현행화**를 BIM 변환·보정·자동화로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 수직 연결성 모델링 | 복층·메자닌 등 비정형 구조의 위상 오류 | BIM 자동 변환, OGC 위상 검증 | 위상 오류 수 |
| 좌표 정합 오차 | WGS84 vs 로컬 좌표계 변환 오차 | 앵커 포인트 보정, 칼만 필터·PDR | 위치 정확도 |
| 데이터 현행화 지연 | 빈번한 테넌트 변경의 수작업 편집 | FMS 연계 웹 저작 도구, 크라우드소싱 | 갱신 지연 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **BIM→IMDF ETL·Validator·IPS 연동**으로 실내 공간정보 구축.
- FME 기반 BIM→IMDF 자동 변환 파이프라인.
- OGC Validator 의무화 (폴리곤 겹침·Level 서열 검증).
- IPS 좌표 보정 및 센서 퓨전.

## Ⅶ. 결론

- 핵심 요약 : IMDF는 **실내 공간정보 OGC 표준**으로 계층 모델·IPS·디지털 트윈이 핵심.
- 답안에는 객체 계층, 피처 유형, 한계·대응, 실무 제언을 연결.
- 참고 : [OGC IMDF](https://www.ogc.org/standards/imdf/).