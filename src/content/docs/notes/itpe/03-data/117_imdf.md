---
sidebar:
  order: 117
  label: "117. IMDF"
  badge:
    text: "응용"
    variant: note
author: "Codex"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 117
title: "IMDF(Indoor Mapping Data Format) 실내 지도 데이터 표준"
extra:
  model: "GPT-6"
  keyword_grade: "응용"
  question_no: "117"
---

## 지식 로드맵 내 현재 위치

데이터베이스 → 공간정보·데이터 표준 → IMDF

## 30초 인출

- 본질: **IMDF는 실내 공간의 위치·형태·명칭·연결 정보를 교환하기 위한 GeoJSON 기반 데이터 표준**
- 메커니즘: 공간 객체를 정해진 Feature와 속성으로 표현하고, 식별자와 참조로 공간 간 관계를 전달
- 통찰: 한계: 생산자별 속성·참조 오류가 있으면 실내 지도의 연결·검색 결과가 깨짐 → 방안: 스키마·참조 무결성 검사를 배포 과정에 넣고 실제 지도 시나리오로 확인

<details><summary>핵심 용어</summary>

- **IMDF (Indoor Mapping Data Format)** : 실내 지도 객체와 속성을 GeoJSON 등으로 인코딩하는 OGC 커뮤니티 표준
- **Feature** : 실내의 공간·시설·표지 등 하나의 물리적 또는 개념적 요소를 나타내는 GeoJSON 객체
- **Level** : 건물 안팎의 층 정보를 담는 Feature로, 관련 Unit·Opening 등의 위치 해석에 쓰이는 요소
- **Relationship** : 서로 다른 Feature 사이의 의미 관계를 표현하는 요소

</details>

---

## 2~4교시 예상문제 (25점)

> IMDF의 개념과 데이터 모델을 설명하고, 주요 Feature의 역할 및 실내 정보시스템 적용 시 고려사항을 기술하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | IMDF는 실내 공간 정보를 GeoJSON 기반 Feature로 표현하는 데이터 표준 |
| 목적 | 실내 지도의 제작·교환·해석을 위한 공통 데이터 모델 제공 |

## Ⅱ. GeoJSON Feature와 참조 식별자의 특징

IMDF 전달물은 Manifest와 유형별 GeoJSON FeatureCollection으로 구성되며, 각 Feature는 유형·식별자·속성을 보유

| 구조 | 역할 |
|---|---|
| Manifest | 전달물의 표준 버전·언어 등 메타정보 |
| FeatureCollection | 같은 Feature 유형의 객체 묶음 |
| Feature | GeoJSON 형상·유형·속성 및 식별자 |

## Ⅲ. 전달 파일·Feature 참조·지도 검증 체계

```text
IMDF ZIP 전달물
  ├─ manifest.json: 버전·언어 등 메타정보
  └─ 유형별 .geojson: 동종 FeatureCollection
         ↓ 각 Feature의 id·feature_type·geometry·properties 확인
Level ─ 참조 ─→ Unit·Opening 등 공간 객체
Relationship ─ 참조 ─→ 관련 Feature의 의미 연결
         ↓ 참조 대상·형상·층 맥락 검사
지도 표시·검색·길찾기 시나리오 검증
```

**Feature 참조의 단계별 검증**

```text
참조 필드의 Feature ID·유형
       ↓ 대상 파일에서 동일 ID·유형 존재 확인
대상 Feature의 형상·속성
       ↓ Level 소속·Opening/Unit 공간 관계 확인
층 이동·통로 연결이 실제 경로와 일치하는지 검증
```

## Ⅳ. 장소·공간·시설·관계 Feature 비교

| 범주 | 대표 Feature | 정보 역할 |
|---|---|---|
| 장소 맥락 | Venue, Building, Level | 장소·건물·층의 맥락 설정 |
| 공간·출입 | Unit, Footprint, Opening | 구역과 외곽·통로 정보 표현 |
| 시설·위치 | Amenity, Anchor, Detail | 편의시설·기준점·선형 요소 표시 |
| 의미 연결 | Relationship | 객체 사이의 관계 표현 |

Feature의 참조는 대상 식별자와 유형을 함께 가리키므로, 공간 계층과 의미 관계를 같은 계층 구조로 혼동하지 않는 것이 핵심

### 적용과 품질관리

| 점검 축 | 확인 내용 |
|---|---|
| 구조 적합성 | 필수 전달 파일, Feature 유형·속성 형식의 표준 준수 |
| 참조 무결성 | 관계가 가리키는 Feature 식별자·유형의 유효성 |
| 공간 품질 | 형상·좌표계·층 맥락의 일관성 |
| 활용 연계 | 지도 표시·검색·길찾기 애플리케이션 요구와 데이터 범위의 부합 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 생산자별 속성·참조 오류가 있으면 실내 지도의 연결·검색 결과가 깨짐 | 스키마·참조 무결성 검사를 배포 과정에 넣고 실제 지도 시나리오로 확인 |
| Feature 식별자를 재발행해 갱신 전후 참조가 끊김 | 객체 생애 동안 ID를 유지하고 전달물 간 참조 차이 검사 |
| 형상·층 맥락이 실제 이동 경로와 다름 | 공간 검증과 실제 길찾기 시나리오로 통로·층 전환 확인 |

## Ⅵ. 제언

Feature 참조나 층·통로 관계가 틀리면 길찾기가 끊기므로 배포 전 ID·유형·공간 관계를 자동 검사하고 실제 경로 탐색으로 확인한다.

## 출제 이력과 검증 출처

- 출제 이력: IMDF의 표준 구조와 실내 공간정보 활용에 관한 기본 예상문제
- 검증 출처: [OGC IMDF 표준 안내](https://www.ogc.org/standards/indoor-mapping-data-format/), [OGC IMDF 1.0.0 Reference](https://docs.ogc.org/cs/20-094/Reference/index.html)

## 연결 토픽

- 실내 공간정보의 모델링 및 공간정보 표준
