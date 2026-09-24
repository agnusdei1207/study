---
sidebar:
  order: 117
  label: "117. IMDF (Indoor Mapping Data Format)"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 117
title: "IMDF(Indoor Mapping Data Format) 실내 공간정보 표준 규격 및 디지털 트윈 응용"
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "117"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>공간 데이터베이스·GIS</span><strong>IMDF</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <rect x="15" y="15" width="490" height="40" rx="6" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="260" y="38" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--sl-color-text, #1e293b)">1. Venue (복합 사이트: 공항, 쇼핑몰, 병원 캠퍼스)</text>

  <path d="M 260 55 L 260 70" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117)"/>
  <text x="275" y="65" font-size="10" fill="#64748b">1 : N</text>

  <rect x="40" y="70" width="440" height="38" rx="6" fill="#0ea5e9" fill-opacity="0.15" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="260" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">2. Building (단일 물리적 건축물 구조체)</text>

  <path d="M 260 108 L 260 123" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117)"/>
  <text x="275" y="118" font-size="10" fill="#64748b">1 : N</text>

  <rect x="65" y="123" width="390" height="38" rx="6" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-width="1.5"/>
  <text x="260" y="146" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">3. Footprint (대지 접지 물리적 바닥 경계 폴리곤)</text>

  <path d="M 260 161 L 260 176" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117)"/>
  <text x="275" y="171" font-size="10" fill="#64748b">1 : N</text>

  <rect x="90" y="176" width="340" height="38" rx="6" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="260" y="199" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">4. Level (수직 층: 지하 1층 B1, 지상 1층 1F 레이어)</text>

  <path d="M 260 214 L 260 229" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117)"/>
  <text x="275" y="224" font-size="10" fill="#64748b">1 : N</text>

  <rect x="115" y="229" width="290" height="38" rx="6" fill="#8b5cf6" fill-opacity="0.15" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="260" y="252" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">5. Unit (매장, 복도, 회의실, 화장실 등 닫힌 다각형)</text>

  <defs>
    <marker id="arrow117" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **공항, 복합쇼핑몰, 스마트 팩토리 등 복잡한 실내 공간의 2차원 및 2.5차원 기하 객체를 웹과 모바일에서 초경량으로 상호운용하기 위해 Apple이 제안하고 OGC(Open Geospatial Consortium)가 국제 커뮤니티 표준으로 채택한 GeoJSON 기반의 실내 공간 데이터 교환 규격**
- 암기: `베-빌-풋-레-유` (5대 공간 계층: Venue, Building, Footprint, Level, Unit) / `오-앵-어-릴` (4대 보조 피처: Opening, Anchor, Amenity, Relationship)
- 판단축:
  - **IMDF (GeoJSON)**: 모바일 앱 렌더링 및 LBS 실내 보행자 내비게이션에 최적화된 초경량 2.5D 표준
  - **IndoorGML (GML/XML)**: 실내 공간 간 위상(Topology) 수학 및 Poincaré 이원성 기반 경로 탐색 특화
  - **CityGML / IFC (BIM)**: 고정밀 3D 솔리드 건축 도면 및 시설물 유지보수용 중량급 규격
- 주의: CAD 도면을 IMDF로 자동 변환 시 계단실 및 엘리베이터의 수직 층간 연결성(`Relationship` 및 `Opening`)이 누락되면 층간 최적 경로 탐색 알고리즘이 단절되는 런타임 오류 발생
---

## 1교시 예상문제 (10점)

> IMDF(Indoor Mapping Data Format) 실내 공간정보 표준 규격 및 디지털 트윈 응용의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 공항, 쇼핑몰 등 복잡한 대형 실내 공간의 지리 객체를 웹/모바일에서 초경량으로 표출하기 위해 Apple이 제안하고 OGC가 표준화한 GeoJSON 기반 2.5D 실내 지도 규격 |
| **2. 5대 공간 계층** | - **Venue**: 전체 복합 단지 부지<br/>- **Building**: 단일 건축물 외벽<br/>- **Footprint**: 접지 바닥 경계<br/>- **Level**: 수직 층 레이어(`ordinal`)<br/>- **Unit**: 방, 매장, 복도 등 독립 다각형 |
| **3. 4대 보조 피처** | - **Opening**: 출입문/통로<br/>- **Anchor**: POI 명칭 표기 중심점<br/>- **Amenity**: 편의시설 아이콘<br/>- **Relationship**: 층간 수직 이동 연결 |
| **4. 표준 비교** | IndoorGML(XML/위상 경로 탐색) 및 CityGML(3D 도시 계획) 대비 모바일 초경량 렌더링에 최적화 |
---

### 핵심 관계

| 공간 계층 | GeoJSON 형태 | 상세 설명 및 모델링 대상 |
|:---|:---:|:---|
| **1. Venue** | Polygon / MultiPolygon | 복합 건축물 전체가 위치한 물리적 사이트 경계 (예: 코엑스 몰, 인천국제공항 부지) |
| **2. Building** | Polygon / MultiPolygon | Venue 내에 위치한 개별 단일 물리 건축물 외벽 경계 |
| **3. Footprint** | Polygon | 건축물이 지표면과 맞닿는 실제 물리적 기초 바닥면 (수직 돌출부 배제) |
| **4. Level** | Polygon | 건축물 내부의 수직 층 (지하 2층, 지상 1층 등). `ordinal`(정수 정렬 순서) 속성 필수 |
| **5. Unit** | Polygon | 벽으로 둘러싸인 실제 사용 공간 단위 (매장, 보행 복도, 화장실, 회의실 등) |

---

## 2~4교시 예상문제 (25점)

> 스마트 시티 및 실내 위치기반서비스(LBS)를 위한 OGC 국제 표준 데이터 포맷인 IMDF(Indoor Mapping Data Format)의 개념과 특징을 설명하고, 5단계 계층적 공간 모델 및 실내 공간 표준(IndoorGML, CityGML)과의 차이점을 비교하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. GPS 음영지역을 해소하는 실내 공간정보 표준: IMDF 개요

#### 한줄 요약: 복합 대형 건축물의 실내 지도를 웹과 모바일 환경에서 초경량으로 렌더링하고 LBS 내비게이션을 지원하는 GeoJSON 기반 OGC 표준

- **배경**:
  - 현대 도시인의 생활 반경이 공항, 대형 복합 쇼핑몰, 지하 환승역 등 거대 실내 공간으로 이동했으나, 위성 기반 실외 GPS는 실내 음영지역에서 작동 불가
  - 기존 실내 도면은 AutoCAD(DWG), Revit(BIM) 등 중량급 바이너리 포맷으로 파편화되어 모바일 단말의 실시간 파싱 및 경량 렌더링 한계 직면
- **정의**: 실내 공간의 폴리곤(Polygon), 라인스트링(LineString), 포인트(Point) 객체와 메타데이터 속성을 GeoJSON 표준을 확장하여 5단계 계층으로 정의한 개방형 데이터 교환 규격
- **표준화 위상**: Apple Maps의 실내 지도 기술로 시작되어 2021년 OGC(Open Geospatial Consortium) 커뮤니티 표준으로 공식 승인

### Ⅱ. IMDF의 4대 핵심 아키텍처 특성

#### 한줄 요약: GeoJSON 경량성, WGS84 절대 좌표계, 엄격한 계층적 외래키 참조, 객체 지향적 시설물 모델링

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="115" height="140" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="72" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. GeoJSON 기반</text>
  <text x="72" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">순수 텍스트 포맷</text>
  <text x="72" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">모바일 브라우저</text>
  <text x="72" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">초고속 렌더링</text>
  <text x="72" y="135" text-anchor="middle" font-size="11" fill="#64748b">XML 대비 80% 절감</text>

  <!-- Box 2 -->
  <rect x="140" y="20" width="115" height="140" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="197" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. WGS84 좌표</text>
  <text x="197" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">전 지구 절대좌표</text>
  <text x="197" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">실외-실내 지도</text>
  <text x="197" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">심리스(Seamless)</text>
  <text x="197" y="135" text-anchor="middle" font-size="11" fill="#64748b">단절 없는 전환</text>

  <!-- Box 3 -->
  <rect x="265" y="20" width="115" height="140" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="322" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. 엄격한 계층</text>
  <text x="322" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Venue to Unit</text>
  <text x="322" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">UUID 외래키 참조</text>
  <text x="322" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">층별(Level) 필터</text>
  <text x="322" y="135" text-anchor="middle" font-size="11" fill="#64748b">트리형 관계망</text>

  <!-- Box 4 -->
  <rect x="390" y="20" width="115" height="140" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="447" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">4. POI/위상 모델</text>
  <text x="447" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">출입문(Opening)</text>
  <text x="447" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">편의시설(Amenity)</text>
  <text x="447" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">층간연결 관계성</text>
  <text x="447" y="135" text-anchor="middle" font-size="11" fill="#64748b">보행 네트워크</text>
</svg>
</div>

1. **GeoJSON 기반의 경량성**: 복잡한 바이너리나 중량급 GML/XML 대신 웹/모바일 친화적인 JSON 포맷을 채택하여 모바일 단말에서 즉각적인 파싱과 GPU 가속 렌더링 지원
2. **WGS84 절대 좌표계 결합**: 건물의 실내 도면을 상대 로컬 픽셀이 아닌 지구 위경도(EPSG:4326) 좌표계로 프로젝션하여 실외 지도에서 건물 실내로 줌인 시 이음새 없는 연속성 보장
3. **엄격한 부모-자식 계층 모델**: 최상위 Venue부터 개별 Unit까지 모든 객체가 UUID 기반 외래키(FK)로 연결되어 층별(`ordinal`) 격리 및 다이나믹 레이어 슬라이싱 지원
4. **객체 지향적 실내 요소 표현**: 단순 벽면 표현을 넘어 문(Opening), 라벨 중심점(Anchor), 엘리베이터/비상구(Amenity) 등을 독립 피처로 분리하여 내비게이션 엔진 탑재 용이

### Ⅲ. IMDF 5대 공간 계층 및 핵심 구성요소

#### 한줄 요약: Venue $\rightarrow$ Building $\rightarrow$ Footprint $\rightarrow$ Level $\rightarrow$ Unit의 계층 구조와 4대 보조 피처

| 공간 계층 | GeoJSON 형태 | 상세 설명 및 모델링 대상 |
|:---|:---:|:---|
| **1. Venue** | Polygon / MultiPolygon | 복합 건축물 전체가 위치한 물리적 사이트 경계 (예: 코엑스 몰, 인천국제공항 부지) |
| **2. Building** | Polygon / MultiPolygon | Venue 내에 위치한 개별 단일 물리 건축물 외벽 경계 |
| **3. Footprint** | Polygon | 건축물이 지표면과 맞닿는 실제 물리적 기초 바닥면 (수직 돌출부 배제) |
| **4. Level** | Polygon | 건축물 내부의 수직 층 (지하 2층, 지상 1층 등). `ordinal`(정수 정렬 순서) 속성 필수 |
| **5. Unit** | Polygon | 벽으로 둘러싸인 실제 사용 공간 단위 (매장, 보행 복도, 화장실, 회의실 등) |

- **주요 연결 및 보조 피처**:
  - **Opening**: 벽이나 경계에 위치한 출입문, 자동문, 개구부 (Unit 간 보행 통로를 연결하는 핵심 노드)
  - **Anchor**: 특정 공간의 중심점(Point)으로 텍스트 라벨 표기 및 POI 검색 기준 좌표 제공
  - **Amenity**: 화장실, 엘리베이터, ATM, 심장충격기(AED) 등 편의시설 아이콘 표시 객체
  - **Relationship**: 계단이나 승강기를 매개로 상하 층간 Unit을 연결하는 수직 보행 네트워크 관계 정의

### Ⅳ. 실내 공간정보 표준 비교: IMDF vs IndoorGML vs CityGML

#### 한줄 요약: 모바일 시각화의 IMDF, 네트워크 위상 경로의 IndoorGML, 3D 도시 모델링의 CityGML

| 비교 항목 | IMDF | IndoorGML | CityGML |
|:---|:---|:---|:---|
| **제정 주체** | Apple 제안 $\rightarrow$ OGC 커뮤니티 표준 | OGC 공식 표준 (한국 주도) | OGC 공식 표준 |
| **기반 포맷** | **GeoJSON (초경량 텍스트)** | **GML / XML (중량급)** | **GML / XML (초중량급)** |
| **차원 및 표현** | **2D / 2.5D (다각형 레이어)** | **위상 네트워크 (Node-Link 그래프)** | **정밀 3D 솔리드/표면 모델** |
| **주요 목적** | **모바일 실내 맵 렌더링 및 LBS** | **실내 보행자/로봇 경로 탐색** | 도시 계획, 일조권/바람길 시뮬레이션 |
| **모바일 적합성** | **극도로 우수** (초경량, 저지연 파싱) | 낮음 (XML 파싱 오버헤드) | 매우 낮음 (렌더링 부하 극심) |
| **경로 탐색** | Opening 기반 위상 추출 필요 | Poincaré 이원성 기반 위상 완벽 지원 | 경로 탐색 엔진 미지원 |

### Ⅴ. IMDF 데이터 제작 및 검증 파이프라인

#### 한줄 요약: CAD/BIM 도면 수집 $\rightarrow$ 좌표 보정 $\rightarrow$ GeoJSON 추출 $\rightarrow$ 스키마 검증 $\rightarrow$ LBS 서빙

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 140" width="100%" height="140" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Step 1 -->
  <rect x="10" y="35" width="88" height="65" rx="5" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="54" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">1. 원천 도면</text>
  <text x="54" y="78" text-anchor="middle" font-size="9" fill="#64748b">AutoCAD/BIM</text>

  <path d="M 98 67 L 112 67" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117_p)"/>

  <!-- Step 2 -->
  <rect x="114" y="35" width="88" height="65" rx="5" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="158" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">2. 지리보정</text>
  <text x="158" y="78" text-anchor="middle" font-size="9" fill="#2563eb">WGS84 투영 매핑</text>

  <path d="M 202 67 L 216 67" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117_p)"/>

  <!-- Step 3 -->
  <rect x="218" y="35" width="88" height="65" rx="5" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5"/>
  <text x="262" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#4338ca">3. 피처 추출</text>
  <text x="262" y="78" text-anchor="middle" font-size="9" fill="#4f46e5">5대 계층 GeoJSON</text>

  <path d="M 306 67 L 320 67" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117_p)"/>

  <!-- Step 4 -->
  <rect x="322" y="35" width="88" height="65" rx="5" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="366" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">4. 스키마 검증</text>
  <text x="366" y="78" text-anchor="middle" font-size="9" fill="#d97706">JSON Schema 린트</text>

  <path d="M 410 67 L 424 67" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow117_p)"/>

  <!-- Step 5 -->
  <rect x="426" y="35" width="84" height="65" rx="5" fill="#dcfce7" stroke="#10b981" stroke-width="1.5"/>
  <text x="468" y="60" text-anchor="middle" font-size="11" font-weight="bold" fill="#047857">5. LBS 서빙</text>
  <text x="468" y="78" text-anchor="middle" font-size="9" fill="#059669">모바일 내비게이션</text>

  <defs>
    <marker id="arrow117_p" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

1. **지리참조(Georeferencing)**: CAD 건축 도면의 픽셀 좌표를 실제 지구 표면의 WGS84 위경도 좌표로 회전, 이동 및 스케일 변환
2. **속성 정제 및 레이어 필터링**: CAD의 배관, 전기 설비 등 불필요한 수백 개 레이어를 제거하고 순수 공간 경계(벽, 문, 구역)만 추출
3. **IMDF 피처셋 생성**: 공간 객체별 고유 UUID를 발급하고 부모-자식 계층 관계를 외래키로 결합한 GeoJSON 데이터셋 구성
4. **유효성 검증(Validation)**: OGC 공식 IMDF JSON Schema Validator를 통해 토폴로지 교차 오류, 폴리곤 자기교차, 고아 객체 검출

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 수직 층간 단절, 측위 인프라(Wi-Fi/BLE) 연계 오차, 매장 리모델링 동기화 지연 해결

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **층간 이동 경로 단절** | 1층과 2층 Unit 간의 엘리베이터/에스컬레이터 Relationship 연결 누락 | FME 변환 시 수직 축 좌표가 일치하는 관통 수직 통로 객체에 Relationship 태그 자동 생성 파이프라인 구축 |
| **실내 측위 오차와 지도 불일치** | Wi-Fi RTT/BLE 비콘 측위 좌표가 벽면을 뚫고 이동하는 텔레포트 현상 | IMDF의 Unit 경계를 보행 가능 영역(Walkable Area)으로 마스킹하는 파티클 필터 기반 맵 매칭(Map Matching) 적용 |
| **매장 리모델링 시 지도 노후화** | 복합몰 입점 매장 변경 시 CAD 도면 갱신 지연으로 안내 정보 왜곡 | 경량 웹 기반 IMDF 에디터를 배포하여 현장 매니저가 브라우저에서 Unit 분할/병합을 직접 수정 후 즉시 배포 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> IMDF는 스마트폰 사용자에게 실내 매장 위치를 보여주는 단순 렌더링 지도에서 시작했지만, 4차 산업혁명 시대의 진정한 가치는 **실내 자율주행 모빌리티(AMR/AGV)와 디지털 트윈의 핵심 지리정보 인프라**로의 진화에 있다.
> CAD 도면은 너무 무겁고 IndoorGML은 시각화 렌더링 파이프라인이 부재한 상황에서, IMDF는 '경량 GeoJSON'이라는 웹 표준성을 무기로 산업 표준의 패권을 쥐었다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 단순 지도 표출을 넘어, "Wi-Fi RTT(802.11mc) / UWB 고정밀 측위 인프라 결합"과 "실내 자율주행 서비스 로봇(배송, 방역, 물류)의 HD-Map으로서의 IMDF 확장"을 제언하겠다. 아울러 건물 화재 등 재난 시 층간 비상 대피 경로를 실시간 계산하는 공공 안전 플랫폼과의 연계를 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 대형 복합 건축물의 증가로 GPS 음영지역 해소가 필수적이나, 기존 CAD/BIM 도면은 모바일 환경에서 실시간 서비스가 불가능하므로 경량 OGC 표준인 IMDF 도입이 필수적임.
- **대응**:
  1. **고정밀 측위 결합**: Wi-Fi RTT(802.11mc) 및 UWB 인프라와 결합하여 오차 1m 이내의 정밀 위치 측정 구현.
  2. **디지털 트윈 연계**: IMDF의 Unit 객체에 IoT 센서(온습도, 유동인구) 메타데이터를 매핑하여 실시간 건물 관제 구현.
- **검증**: OGC IMDF Schema Validator 전수 자동 통과 및 수직 층간 위상 연결성(Relationship) 100% 무결성 검증.
- **효과**: 대국민 실내 길찾기 서비스 편익 증대 및 실내 자율주행 로봇(AMR)의 표준 주행 맵 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">CAD/BIM의 중량성 및 모바일 파싱 불가, 실내 GPS 음영</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">GeoJSON 기반 IMDF 5대 계층 모델링 및 UWB 측위 융합</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">OGC Schema Validator 검증 및 층간 Relationship 위상 연속성</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">초경량 실내 LBS 서비스 및 자율주행 로봇 물류 HD-Map 실현</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제124회 정보관리 2교시: 실내 공간정보 모델링을 위한 IMDF(Indoor Mapping Data Format)의 개념과 구성요소
- **검증 출처**:
  - Open Geospatial Consortium (OGC), "OGC Indoor Mapping Data Format (IMDF) Community Standard"
  - Apple Developer Documentation, "Indoor Mapping Data Format Specification"
---

## 연결 토픽

- 상위 토픽: [03-119 공간 연산자](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/119_spatial_operator.md)
- 연관 토픽: [03-016 데이터 시각화](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/016_data_visualization.md), [05-001 이동통신 및 무선 네트워크](file:///C:/workspace/study/src/content/docs/notes/itpe/05-network/001_mobile_communication.md)
