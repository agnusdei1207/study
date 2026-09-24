---
sidebar:
  order: 117
  label: "117. IMDF"
  badge:
    text: "기초"
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
  keyword_grade: "기초"
  question_no: "117"
---

## 지식 로드맵 내 현재 위치

데이터베이스 → 공간정보·데이터 표준 → IMDF

## 30초 인출

- 본질: **IMDF는 실내 공간의 위치·형태·명칭·연결 정보를 교환하기 위한 GeoJSON 기반 데이터 표준**
- 메커니즘: 공간 객체를 정해진 Feature와 속성으로 표현하고, 식별자와 참조로 공간 간 관계를 전달

<details><summary>핵심 용어</summary>

- **IMDF (Indoor Mapping Data Format)** : 실내 지도 객체와 속성을 GeoJSON 등으로 인코딩하는 OGC 커뮤니티 표준
- **Feature** : 실내의 공간·시설·표지 등 하나의 물리적 또는 개념적 요소를 나타내는 GeoJSON 객체
- **Level** : 건물 안팎의 층 정보를 담는 Feature로, 관련 Unit·Opening 등의 위치 해석에 쓰이는 요소
- **Relationship** : 서로 다른 Feature 사이의 의미 관계를 표현하는 요소

</details>

---

## 1교시 예상문제 (10점)

> IMDF의 개념과 주요 구성요소 및 활용 목적을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. IMDF 개요

| 구분 | 핵심 |
|---|---|
| 정의 | IMDF는 실내 공간 정보를 GeoJSON 기반 Feature로 표현하는 데이터 표준 |
| 목적 | 실내 지도의 제작·교환·해석을 위한 공통 데이터 모델 제공 |

### Ⅱ. 구성요소

| Feature | 표현 대상 |
|---|---|
| Venue·Building·Level | 장소·건물·층의 공간 맥락 |
| Unit·Opening·Footprint | 공간 단위와 출입·외곽 형상 |
| Amenity·Anchor·Detail | 시설·위치 기준점·선형 세부정보 |
| Relationship | Feature 사이의 의미 관계 |

**제언:** 공간 객체의 식별자와 참조 관계를 검증하는 적합성 점검 절차의 마련

---

## 2~4교시 예상문제 (25점)

> IMDF의 개념과 데이터 모델을 설명하고, 주요 Feature의 역할 및 실내 정보시스템 적용 시 고려사항을 기술하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. IMDF 개요

| 구분 | 핵심 |
|---|---|
| 정의 | IMDF는 실내 공간 정보를 GeoJSON 기반 Feature로 표현하는 데이터 표준 |
| 목적 | 실내 지도의 제작·교환·해석을 위한 공통 데이터 모델 제공 |

## Ⅱ. 데이터 구조와 인코딩

IMDF 전달물은 Manifest와 유형별 GeoJSON FeatureCollection으로 구성되며, 각 Feature는 유형·식별자·속성을 보유

| 구조 | 역할 |
|---|---|
| Manifest | 전달물의 표준 버전·언어 등 메타정보 |
| FeatureCollection | 같은 Feature 유형의 객체 묶음 |
| Feature | GeoJSON 형상·유형·속성 및 식별자 |

## Ⅲ. 공간·의미 Feature

| 범주 | 대표 Feature | 정보 역할 |
|---|---|---|
| 장소 맥락 | Venue, Building, Level | 장소·건물·층의 맥락 설정 |
| 공간·출입 | Unit, Footprint, Opening | 구역과 외곽·통로 정보 표현 |
| 시설·위치 | Amenity, Anchor, Detail | 편의시설·기준점·선형 요소 표시 |
| 의미 연결 | Relationship | 객체 사이의 관계 표현 |

Feature의 참조는 대상 식별자와 유형을 함께 가리키므로, 공간 계층과 의미 관계를 같은 계층 구조로 혼동하지 않는 것이 핵심

## Ⅳ. 적용과 품질관리

| 점검 축 | 확인 내용 |
|---|---|
| 구조 적합성 | 필수 전달 파일, Feature 유형·속성 형식의 표준 준수 |
| 참조 무결성 | 관계가 가리키는 Feature 식별자·유형의 유효성 |
| 공간 품질 | 형상·좌표계·층 맥락의 일관성 |
| 활용 연계 | 지도 표시·검색·길찾기 애플리케이션 요구와 데이터 범위의 부합 |

## Ⅴ. 기술사적 제언

| 문제 | 해결 방안 |
|---|---|
| 데이터 생산자별 속성·참조 오류가 실내 지도 품질 저하로 이어질 가능성 | 표준 스키마 검증과 참조 무결성 검사를 배포 파이프라인에 포함하고, 실제 지도 활용 시나리오로 검증 |

---

## 출제 이력과 검증 출처

- 출제 이력: IMDF의 표준 구조와 실내 공간정보 활용에 관한 기본 예상문제
- 검증 출처: [OGC IMDF 표준 안내](https://www.ogc.org/standards/indoor-mapping-data-format/), [OGC IMDF 1.0.0 Reference](https://docs.ogc.org/cs/20-094/Reference/index.html)

## 연결 토픽

- 실내 공간정보의 모델링 및 공간정보 표준
