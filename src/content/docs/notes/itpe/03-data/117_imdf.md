---
sidebar:
  order: 117
  label: "117. IMDF (Indoor Mapping Data Format)"
  badge:
    text: "C"
    variant: note
title: "IMDF(Indoor Mapping Data Format) 실내 공간정보 표준 규격 및 디지털 트윈 응용"
author: "OpenAI Codex"
date: "2026-09-20T19:30:00+09:00"
tags:
  - "notes-data"
weight: 117
extra:
  model: "GPT-5"
  keyword_grade: "C"
  question_no: "117"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>공간 데이터베이스·GIS</span><strong>IMDF</strong></div>

## 큰 그림과 30초 인출

```text
[IMDF 계층적 실내 공간 객체 모델 아키텍처 (OGC 표준)]

  ┌─────────────────────────────────────────────────────────────┐
  │  Venue (전체 복합 단지: 공항, 코엑스 쇼핑몰, 병원 캠퍼스)  │
  └──────────────────────────────┬──────────────────────────────┘
                                 │ 1:N
  ┌──────────────────────────────▼──────────────────────────────┐
  │  Building (단일 건축물 외형)                                │
  └──────────────────────────────┬──────────────────────────────┘
                                 │ 1:N
  ┌──────────────────────────────▼──────────────────────────────┐
  │  Footprint (건물이 대지와 접하는 물리적 바닥 경계 폴리곤)   │
  └──────────────────────────────┬──────────────────────────────┘
                                 │ 1:N
  ┌──────────────────────────────▼──────────────────────────────┐
  │  Level (각 층: 지하 1층 B1, 지상 1층 1F 등 수직 층 레이어)  │
  └──────────────────────────────┬──────────────────────────────┘
                                 │ 1:N
  ┌──────────────────────────────▼──────────────────────────────┐
  │  Unit (개별 매장, 회의실, 복도, 화장실 등 닫힌 다각형 구역) │
  └─────────────────────────────────────────────────────────────┘
     * 연결 및 보조 객체: Opening (출입문/개구부), Anchor (명칭/라벨 중심점)
```

- 본질: **공항, 쇼핑몰, 대형 병원 등 복합 실내 공간의 2차원/2.5차원 지리 객체(GIS)를 웹과 모바일 환경에서 상호운용하기 위해 Apple이 제안하고 OGC(Open Geospatial Consortium)가 국제 표준으로 채택한 경량 GeoJSON 기반의 실내 공간 데이터 교환 포맷**
- 암기: `베-빌-풋-레-유` (5대 공간 계층: Venue, Building, Footprint, Level, Unit) / `오-앵-어-릴` (보조 객체: Opening, Anchor, Amenity, Relationship)
- 판단축:
  - **IMDF (GeoJSON)**: 모바일 앱 렌더링 및 LBS 실내 내비게이션에 최적화된 경량 2.5D 표준
  - **IndoorGML (GML/XML)**: 실내 공간 간의 위상(Topology) 및 보행자 경로 탐색 네트워크에 특화
  - **CityGML / IFC (BIM)**: 고정밀 3D 건축 설계 및 유지보수용 복잡 포맷
- 주의: 고정밀 3D CAD/BIM 도면을 모바일용 IMDF로 변환할 때 계단, 엘리베이터 등 **수직 층간 이동 연결(Relationship/Opening)**이 누락되면 층간 길찾기 알고리즘이 단절되는 결함이 발생함

## 예상문제

> 스마트 시티 및 실내 위치기반서비스(LBS)를 위한 OGC 국제 표준 데이터 포맷인 IMDF(Indoor Mapping Data Format)의 개념과 특징을 설명하고, 5단계 계층적 공간 모델 및 실내 공간 표준(IndoorGML, CityGML)과의 차이점을 비교하시오. (25점)

## Ⅰ. GPS 음영지역을 해소하는 실내 공간정보 표준: IMDF 개요

#### 한줄 요약: 복잡한 대형 건물의 실내 지도를 웹과 모바일에서 초경량으로 렌더링하고 내비게이션을 지원하는 GeoJSON 기반 OGC 표준

- **배경**: 실내 복합 쇼핑몰, 지하철 환승역, 스마트 팩토리 등 현대인의 생활 공간이 실내화되었으나, 실외용 GPS는 건물 내부에서 동작하지 않고 실내 지도는 CAD/이미지로 파편화되어 호환성 부재
- **정의**: 실내 공간의 다각형(Polygon), 선(LineString), 점(Point) 객체와 속성을 GeoJSON 표준을 확장하여 계층적으로 표현한 개방형 데이터 모델
- **표준화**: Apple이 Apple Maps 실내 지도를 위해 개발한 후 2021년 OGC(Open Geospatial Consortium)의 공식 커뮤니티 표준으로 승인

## Ⅱ. IMDF의 핵심 특징

#### 한줄 요약: GeoJSON 경량성, WGS84 좌표계, 모바일 플랫폼 호환성 및 위상적 연결성

```text
  ┌─────────────────────────────────────────────────────────────┐
  │                   IMDF 4대 핵심 기술 특성                   │
  └─────────────────────────────────────────────────────────────┘
          │                      │                      │
  ┌───────▼──────────┐   ┌───────▼──────────┐   ┌───────▼──────────┐
  │ 1. GeoJSON 기반  │   │ 2. WGS84 좌표계  │   │ 3. 계층적 모델   │
  ├──────────────────┤   ├──────────────────┤   ├──────────────────┤
  │ - JSON 텍스트    │   │ - 위도/경도 절대 │   │ - 부모-자식 관계 │
  │ - 경량 모바일 최 │   │   좌표계 준수    │   │   UUID 명시적참조│
  │   적화 렌더링    │   │ - 실외 맵과 연속 │   │ - Venue부터 Unit │
  └──────────────────┘   └──────────────────┘   └──────────────────┘
```

1. **GeoJSON 기반의 경량성**: 복잡한 바이너리나 중량급 XML 대신 웹/모바일 친화적인 JSON 포맷을 채택하여 모바일 단말에서 즉각 파싱 및 렌더링 가능
2. **WGS84 절대 좌표계 결합**: 건물의 실내 도면을 로컬 상대 좌표가 아닌 전 지구적 경위도(WGS84) 좌표계로 변환하여 실외 지도와 실내 지도의 매끄러운(Seamless) 전환 보장
3. **엄격한 공간 계층 구조**: 최상위 Venue부터 최하위 Unit까지 부모-자식 관계가 명확한 외래키(UUID)로 연결되어 층별(Level) 필터링 검색 지원
4. **객체 지향적 실내 요소 표현**: 출입문, 키오스크, 소화전, 와이파이 AP 등 시설물(Amenity)을 포인트 및 앵커로 유연하게 모델링

## Ⅲ. IMDF 5대 공간 계층 및 핵심 구성요소

#### 한줄 요약: Venue $\rightarrow$ Building $\rightarrow$ Footprint $\rightarrow$ Level $\rightarrow$ Unit의 계층 구조와 보조 객체

| 공간 계층 | GeoJSON 형태 | 상세 설명 및 모델링 대상 |
|:---|:---:|:---|
| **1. Venue** | Polygon / MultiPolygon | 복합 건축물 전체가 위치한 물리적 사이트 경계 (예: 인천국제공항 제1터미널 부지) |
| **2. Building** | Polygon / MultiPolygon | Venue 내에 위치한 개별 단일 물리 건축물 외벽 경계 |
| **3. Footprint** | Polygon | 건축물이 지표면과 맞닿는 실제 물리적 기초 바닥면 (수직 돌출부 배제) |
| **4. Level** | Polygon | 건축물 내부의 수직 층 (지하 2층, 지상 1층 등). `ordinal`(정수형 정렬 순서) 속성 보유 |
| **5. Unit** | Polygon | 벽으로 둘러싸인 실제 사용 공간 단위 (식당, 면세점 매장, 보행 복도, 화장실, 계단실) |

- **주요 연결 및 보조 피처**:
  - **Opening**: 벽이나 경계에 뚫려 있는 출입문, 자동문, 개구부 (Unit 간 보행 통로 연결)
  - **Anchor**: 특정 공간의 중심점(Point)으로 텍스트 라벨 표기 및 POI 검색 기준 좌표 제공
  - **Amenity**: 화장실, 엘리베이터, ATM, 응급제세동기(AED) 등 편의시설 아이콘 표시 객체
  - **Relationship**: 층간 계단이나 엘리베이터를 통해 연결되는 수직 이동 경로 관계 정의

## Ⅳ. 실내 공간정보 표준 비교: IMDF vs IndoorGML vs CityGML

#### 한줄 요약: 모바일 시각화의 IMDF, 네트워크 경로 탐색의 IndoorGML, 3D 도시 모델링의 CityGML

| 비교 항목 | IMDF | IndoorGML | CityGML |
|:---|:---|:---|:---|
| **제정 주체** | Apple 제안 $\rightarrow$ OGC 표준 | OGC 공식 표준 (한국 주도) | OGC 공식 표준 |
| **기반 포맷** | **GeoJSON (경량 텍스트)** | **GML / XML (중량급)** | **GML / XML (초중량급)** |
| **차원 및 표현** | **2D / 2.5D (다각형 레이어)** | **위상 네트워크 (Node-Link 그래프)** | **정밀 3D 솔리드/표면 모델** |
| **주요 목적** | **모바일 실내 맵 렌더링 및 LBS** | **실내 보행자/로봇 경로 탐색** | 도시 계획, 일조권/바람길 시뮬레이션 |
| **모바일 적합성** | **극도로 우수** (초경량, 저지연 파싱) | 낮음 (XML 파싱 오버헤드) | 매우 낮음 (렌더링 부하 극심) |
| **경로 탐색** | 노드-링크 별도 추출 필요 | Poincaré 쌍대성 기반 토폴로지 완벽 지원 | 경로 탐색 미지원 |

## Ⅴ. IMDF 데이터 제작 및 검증 파이프라인

#### 한줄 요약: CAD/BIM 도면 수집 $\rightarrow$ 지리보정 $\rightarrow$ GeoJSON 추출 $\rightarrow$ 스키마 검증 $\rightarrow$ LBS 서빙

```text
 [1. 원천 도면 수집] ──► [2. 좌표계 변환] ──► [3. IMDF 피처 추출] ──► [4. 스키마 검증] ──► [5. LBS 서빙]
  - AutoCAD (DWG)        - WGS84 좌표 투영    - FME / Python 스크립트 - OGC JSON Schema     - Apple Maps
  - Revit (BIM/IFC)      - 실외 건물 외곽 일치- Venue/Level/Unit 분해 - 유효성 Lint 검사    - 실내 내비게이션
```

1. **지리참조(Georeferencing)**: CAD 건축 도면의 픽셀 좌표를 실제 지구 표면의 WGS84 위경도 좌표로 회전 및 스케일 매핑
2. **속성 정제 및 레이어 매핑**: CAD의 수백 개 복잡 레이어(배관, 전선)를 제거하고 순수 공간 경계(벽, 문, 방)만 추출
3. **IMDF 피처셋 생성**: 공간 객체별 고유 UUID를 부여하고 계층적 외래키 참조 관계를 구성하여 GeoJSON 파일군으로 저장
4. **유효성 검증(Validation)**: OGC 공식 IMDF JSON Schema Validator를 통과시켜 토폴로지 교차 오류나 고아 객체 검출

## Ⅵ. 실무 적용 시 기술적 한계 및 트러블슈팅

#### 한줄 요약: 수직 층간 단절, 측위 인프라(Wi-Fi/BLE) 연계, 도면 변경 동기화

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **층간 이동 경로 단절** | 1층과 2층 Unit 간의 엘리베이터/에스컬레이터 Relationship 연결 누락 | FME 자동화 변환 시 수직 축 좌표가 일치하는 관통 객체에 Relationship 태그 자동 생성 |
| **실내 측위 오차와 지도 불일치** | Wi-Fi RTT/BLE 비콘 측위 좌표가 벽면을 뚫고 지나가는 텔레포트 현상 | IMDF의 Unit 경계를 보행 가능 영역(Walkable Area)으로 마스킹하는 맵 매칭(Map Matching) 적용 |
| **매장 리모델링 시 지도 노후화** | 쇼핑몰 매장 경계가 수시로 바뀌나 CAD 도면 갱신 지연으로 정보 왜곡 | 경량 웹 기반 IMDF 에디터 도입하여 현장 관리자가 브라우저에서 Unit 분할/병합 즉시 수정 |

## Ⅶ. 기술사적 제언: 실내 디지털 트윈과 자율주행 로봇 물류 연계

#### 한줄 요약: 사람을 위한 내비게이션을 넘어 자율주행 서비스 로봇의 실내 HD-Map으로 확장

```text
 [차세대 실내 공간정보 플랫폼: IMDF 2.0]
  [IMDF 실내 공간 모델] ──► Wi-Fi RTT / UWB 고정밀 측위 인프라 결합
                                   │
              ┌────────────────────┴────────────────────┐
              ▼                                         ▼
   [대국민 실내 LBS 서비스]               [실내 자율주행 로봇 관제]
   - 병원/공항 길찾기 AR 표출             - 서빙/방역/배송 로봇 주행 맵
   - 화재 시 최적 대피 경로 안내          - 스마트 팩토리 AGV/AMR 물류 통제
```

- IMDF는 스마트폰 사용자 화면 표출을 위해 시작되었으나, 향후 빌딩 내 배송 로봇, 청소 로봇 등 **실내 자율주행 모빌리티(AMR)**의 고정밀 실내 지도로 확장되고 있음
- Wi-Fi RTT(802.11mc), UWB(Ultra-Wideband) 고정밀 측위 인프라와 IMDF를 실시간 융합하여 센티미터(cm)급 위치 기반의 실내 디지털 트윈 관제 플랫폼을 구축해야 함

---

## 1교시 10점 답안 발췌

```text
1. IMDF(Indoor Mapping Data Format)의 정의
  - 대형 복합 실내 공간정보를 웹/모바일에서 상호운용하기 위해 Apple이 제안하고 OGC가 표준화한 GeoJSON 기반 경량 실내지도 규격.

2. IMDF 5대 공간 계층 및 보조 객체
  가. 5대 계층:
    - Venue(전체 단지) -> Building(단일 건물) -> Footprint(지표면 바닥면) -> Level(수직 층) -> Unit(실제 방/매장).
  나. 보조 객체:
    - Opening(문/통로), Anchor(라벨 중심점), Amenity(편의시설), Relationship(층간 연결).

3. 타 실내 공간 표준과의 비교
  - IndoorGML은 경로 위상 분석(XML), CityGML은 3D 도시 모델링에 특화된 반면, IMDF는 모바일 초경량 실내 렌더링에 최적화.
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제124회 정보관리 2교시: 실내 공간정보 모델링을 위한 IMDF(Indoor Mapping Data Format)의 개념과 구성요소
- **검증 출처**:
  - Open Geospatial Consortium (OGC), "OGC Indoor Mapping Data Format (IMDF) Community Standard"
  - Apple Developer Documentation, "Indoor Mapping Data Format Specification"

---

## 학습 체크

- [ ] IMDF의 5대 공간 계층(Venue-Building-Footprint-Level-Unit)의 포함 관계를 도식화할 수 있는가?
- [ ] IMDF와 IndoorGML의 설계 목적 및 데이터 포맷(GeoJSON vs GML)의 차이를 비교할 수 있는가?
- [ ] 실내 위치기반서비스(LBS)에서 Wi-Fi/BLE 측위와 IMDF의 맵 매칭 결합 원리를 설명할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-119 공간 연산자](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/119_spatial_operator.md)
- 연관 토픽: [03-016 데이터 시각화](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/016_data_visualization.md), [05-001 이동통신 및 무선 네트워크](file:///C:/workspace/study/src/content/docs/notes/itpe/05-network/001_mobile_communication.md)
