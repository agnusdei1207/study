---
title: "실내 매핑 데이터 포맷(IMDF)"
author: "Claude Code"
date: "2026-09-30T15:22:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

자료처리·데이터 → 공간 데이터 → **실내 매핑 데이터 포맷(IMDF)**

## 30초 인출

- 본질: IMDF는 실내 공간 정보를 GeoJSON 기반의 Feature로 표현하는 데이터 표준
- 메커니즘: ZIP 전달물이 manifest.json(버전·언어 등)과 유형별 GeoJSON FeatureCollection으로 구성되고, 각 Feature는 id·feature_type·geometry·properties를 가지며 Level·Unit·Opening·Relationship 등이 식별자로 서로를 참조
- 통찰: 참조 대상의 ID·유형이 어긋나면 실내 지도의 연결·검색이 깨지므로 스키마와 참조 무결성 검사를 배포 과정에 넣고, 실제 길찾기 시나리오로 층 전환과 통로 연결을 검증

<details>
<summary>핵심 용어</summary>

- **IMDF(Indoor Mapping Data Format)** : 실내 지도를 GeoJSON Feature로 표현하는 데이터 포맷
- **Manifest** : 전달물의 버전·언어 등 메타정보 파일
- **FeatureCollection·Feature** : 같은 유형의 객체 묶음 / 형상·유형·속성·식별자를 가진 객체
- **Venue·Building·Level** : 장소·건물·층
- **Unit·Opening** : 구역·출입구(통로)
- **Relationship** : Feature 사이의 의미 관계
- **GeoJSON** : JSON으로 공간 형상을 표현하는 형식

</details>

---

## 2~4교시 예상문제 (25점)

> 실내 매핑 데이터 포맷(IMDF)의 구조와 Feature 유형, 품질관리 방법을 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. IMDF의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **IMDF** 는 실내 공간 정보를 GeoJSON 기반 Feature로 표현하는 데이터 표준 |
| 목적 | 실내 지도의 제작·교환·해석을 위한 공통 데이터 모델 제공 |

## Ⅱ. 특징과 전달물 구조

| 구조 | 역할 |
|---|---|
| Manifest | 표준 버전·언어 등 메타정보 |
| FeatureCollection | 같은 유형의 Feature 묶음 |
| Feature | GeoJSON 형상·유형·속성·식별자 |

## Ⅲ. 참조 구조와 검증

```text
IMDF ZIP
 ├ manifest.json: 버전·언어 등
 └ 유형별 .geojson: 동종 FeatureCollection
      ↓ 각 Feature의 id·feature_type·geometry·properties 확인
Level ─ 참조 → Unit·Opening 등 / Relationship ─ 참조 → 관련 Feature
      ↓ 참조 대상 ID·유형 존재, 형상·층 맥락 검사
지도 표시·검색·길찾기 시나리오 검증
```

## Ⅳ. Feature 유형과 품질관리

| 범주 | 대표 Feature | 역할 |
|---|---|---|
| 장소 맥락 | Venue, Building, Level | 장소·건물·층의 맥락 |
| 공간·출입 | Unit, Footprint, Opening | 구역과 외곽·통로 |
| 시설·위치 | Amenity, Anchor, Detail | 편의시설·기준점·선형 요소 |
| 의미 연결 | Relationship | 객체 간 관계 |

참조는 대상의 식별자와 유형을 함께 가리키며, 공간 계층과 의미 관계를 같은 계층으로 혼동하지 않는 것이 핵심.

| 점검 축 | 확인 내용 |
|---|---|
| 구조 적합성 | 필수 파일, Feature 유형·속성 형식 |
| 참조 무결성 | 관계가 가리키는 Feature ID·유형의 유효성 |
| 공간 품질 | 형상·좌표계·층 맥락의 일관성 |
| 활용 연계 | 지도 표시·검색·길찾기 요구와 데이터 범위 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 생산자별 속성·참조 오류로 연결·검색 결과 손상 | 스키마·참조 무결성 검사를 배포 과정에 포함, 실제 지도 시나리오로 확인 |
| Feature ID 재발행으로 갱신 전후 참조 단절 | 객체 생애 동안 ID 유지, 전달물 간 참조 차이 검사 |
| 형상·층 맥락이 실제 이동 경로와 다름 | 공간 검증과 길찾기 시나리오로 통로·층 전환 확인 |

## Ⅵ. 제언

전달물 배포 전에 스키마·참조·공간 검증을 자동화하고 길찾기 시나리오로 최종 확인

```text
제작 → 스키마 검사 → 참조 무결성 검사 → 공간 검증 → 길찾기 시나리오 → 배포
```

| 구분 | 육안 검토 | 제언: 자동 검증 |
|---|---|---|
| 참조 오류 | 누락 | 배포 전 차단 |
| 갱신 | ID 단절 위험 | ID 유지·차이 검사 |

## 출제 이력과 검증 출처

- Q-net 기출 원문에서 직접 묻는 문항 없음
- Apple, Indoor Mapping Data Format 명세

## 연결 토픽

- 연관 토픽: [공간 연산자](./119_spatial_operator.md), [다차원 인덱스 구조](./052_multidimensional_index_structure.md), [참조 무결성](./070_referential_integrity.md)
