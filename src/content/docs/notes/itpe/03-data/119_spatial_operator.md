---
sidebar:
  order: 119
  label: "119. 공간 연산자 (Spatial Operator)"
  badge:
    text: "기초"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 119
title: "공간 연산자 (Spatial Operator) 체계 및 공간 인덱스 기반 2단계(Filter & Refine) 처리"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "119"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>공간 데이터베이스·GIS</span><strong>공간 연산자</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Top Query -->
  <rect x="60" y="15" width="400" height="36" rx="6" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="260" y="38" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">공간 질의: ST_Contains(구역Polygon, 위치Point)</text>

  <path d="M 260 51 L 260 75" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow119)"/>

  <!-- Filter Phase -->
  <rect x="30" y="75" width="460" height="65" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="50" y="98" font-size="12" font-weight="bold" fill="#0284c7">1단계: MBR 필터링 단계 (Filter Phase)</text>
  <text x="50" y="118" font-size="11" fill="var(--sl-color-text, #334155)">- R-Tree / GiST 공간 인덱스를 활용하여 최소경계사각(MBR) 교차 검사</text>
  <text x="50" y="132" font-size="10" fill="#64748b">비용 높은 정밀 연산 전 99% 후보군 고속 배제 (Candidate Selection)</text>

  <path d="M 260 140 L 260 165" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow119)"/>
  <text x="275" y="155" font-size="10" fill="#64748b">MBR 포함 후보군만 전달</text>

  <!-- Refine Phase -->
  <rect x="30" y="165" width="460" height="65" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="50" y="188" font-size="12" font-weight="bold" fill="#059669">2단계: 정밀 기하 연산 단계 (Refine Phase)</text>
  <text x="50" y="208" font-size="11" fill="var(--sl-color-text, #334155)">- 실제 폴리곤의 수천 개 정점(Vertex) 좌표에 대해 DE-9IM 위상 행렬 연산</text>
  <text x="50" y="222" font-size="10" fill="#64748b">최종 수학적 포함·교차 여부 검증 후 엄밀한 True/False 레코드 반환</text>

  <defs>
    <marker id="arrow119" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **공간 데이터베이스(Spatial DB)에서 기하 객체(Point, Line, Polygon) 간의 위상적(Topological) 관계, 거리(Metric), 집합적(Set) 변환을 계산하기 위해 OGC 표준(Simple Features for SQL)으로 규격화된 함수 집합이며, 고비용의 기하 계산 부하를 줄이기 위해 MBR 공간 인덱스를 활용하는 2단계(Filter & Refine) 파이프라인으로 동작함**
- 암기: `위-거-변` (3대 연산자: 위상 연산자, 거리 연산자, 공간 변환 연산자) / `콘-인-위-터` (핵심 위상 함수: ST_Contains, ST_Intersects, ST_Within, ST_Touches) / `필-리-엠-디` (Filter & Refine, MBR, DE-9IM)
- 판단축:
  - **위상 연산자 (ST_Intersects, ST_Contains)**: 객체 간의 기하학적 접촉·포함·분리 여부를 수학적으로 판정
  - **거리 연산자 (ST_Distance, ST_DWithin)**: 객체 간 최단 유클리드/구면 거리를 계산하거나 반경 내 존재 여부를 인덱스로 판별
  - **공간 변환 연산자 (ST_Buffer, ST_Union)**: 기존 기하 객체를 기반으로 새로운 영역을 생성하거나 결합
- 주의: 반경 검색 시 `WHERE ST_Distance(a, b) < 3000`을 사용하면 공간 인덱스를 타지 못해 풀 테이블 스캔이 발생하므로, 반드시 공간 인덱스 바운딩 박스를 활용하는 `WHERE ST_DWithin(a, b, 3000)`을 사용해야 함
---

## 1교시 예상문제 (10점)

> 공간 연산자 (Spatial Operator) 체계 및 공간 인덱스 기반 2단계(Filter & Refine) 처리의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 공간 데이터베이스에서 점, 선, 면 기하 객체 간의 위상적·거리적·집합적 관계를 판별하고 변환하기 위한 OGC 표준 함수 규격 |
| **2. 3대 유형** | - **위상 연산자**: ST_Contains, ST_Intersects, ST_Within (DE-9IM 기반 접촉 상태 판정)<br/>- **거리 연산자**: ST_Distance, ST_DWithin (최단거리 계산 및 반경 판별)<br/>- **변환/집합 연산자**: ST_Buffer, ST_Union, ST_Intersection (신규 영역 생성/병합) |
| **3. 2단계 처리 메커니즘** | - **1단계 (Filter)**: R-Tree 인덱스 기반 MBR 바운딩 박스 교차로 99% 후보 고속 탈락<br/>- **2단계 (Refine)**: 통과된 객체의 실제 정점 좌표로 DE-9IM 정밀 기하 연산 수행 |
| **4. 튜닝 핵심** | `ST_Distance() < r` 대신 공간 인덱스를 타는 `ST_DWithin()` 함수를 사용하여 풀스캔 방지 |
---

### 핵심 관계

| 분류 | 주요 함수 | 연산 목적 및 기능 설명 | 반환 타입 |
|:---|:---|:---|:---:|
| **위상 연산자 (Topological)** | `ST_Contains(A, B)`<br/>`ST_Within(A, B)`<br/>`ST_Intersects(A, B)`<br/>`ST_Touches(A, B)` | - A가 B를 완전히 포함하는지 여부 판별<br/>- A가 B의 내부에 완전히 속하는지 여부<br/>- 두 객체가 한 점이라도 공간을 공유하는지 판별<br/>- 경계선에서만 접촉하고 내부는 공유하지 않는지 판별 | Boolean (True/False) |
| **거리 연산자 (Metric)** | `ST_Distance(A, B)`<br/>`ST_DWithin(A, B, dist)`<br/>`ST_Length(Line)` | - 두 객체 간의 최단 유클리드/구면 거리 계산<br/>- 두 객체의 거리가 dist 반경 이내인지 불리언 판정 (인덱스 지원)<br/>- 선형 객체의 총 길이 계산 | Float / Boolean |
| **공간 변환·집합 (Constructive)** | `ST_Buffer(geom, radius)`<br/>`ST_Union(A, B)`<br/>`ST_Intersection(A, B)`<br/>`ST_Difference(A, B)` | - 객체 주위로 지정 반경만큼 확장된 다각형 영역 생성<br/>- 두 공간 객체를 결합하여 단일 기하 객체로 병합<br/>- 두 공간 객체의 공통 교차 영역 다각형 추출<br/>- A 영역에서 B 영역을 차감한 잔여 영역 반환 | Geometry (Polygon 등) |

---

## 2~4교시 예상문제 (25점)

> 공간 데이터베이스(Spatial Database)의 공간 연산자(Spatial Operator)의 개념과 주요 유형(위상 연산자, 거리 연산자, 공간 변환 연산자)을 설명하고, 공간 질의 처리 시의 2단계(Filter & Refine) 처리 메커니즘 및 성능 최적화 방안을 기술하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 공간 데이터베이스와 공간 연산자 개요

#### 한줄 요약: 관계형 연산자로 처리 불가능한 좌표·선·면 기하 객체의 공간적 상호관계를 OGC 표준 함수로 계산하는 특수 연산 체계

- **배경**:
  - 전통적인 관계형 데이터베이스의 동등/대소 비교 연산자(`=, <, >`)는 2차원 이상의 좌표 및 다각형 객체 간의 공간적 관계(포함, 교차, 인접)를 계산 불가
  - LBS, GIS, 배달 및 모빌리티 플랫폼의 폭발적 성장으로 복잡한 지리 객체 간의 관계를 고속으로 판별하는 표준 인터페이스 필요성 대두
- **정의**: 공간 데이터베이스 관리 시스템(SDBMS: PostGIS, Oracle Spatial 등)에서 OGC 'Simple Features for SQL' 표준에 따라 공간 객체 간의 위상, 거리, 기하학적 연산을 수행하는 함수 집합
- **핵심 특징**:
  - **OGC 표준 준수**: `ST_` (Spatial Type) 접두사로 시작하는 표준 함수 규격 제공
  - **차원 확장 9-교차 모델(DE-9IM)** 기반 엄밀한 위상 수학 판정
  - **다차원 공간 인덱스(R-Tree, GiST)** 결합 필수

### Ⅱ. 공간 연산자의 3대 유형 및 주요 함수

#### 한줄 요약: 공간적 접촉을 다루는 위상 연산자, 공간적 간격을 다루는 거리 연산자, 새 형상을 만드는 공간 변환 연산자

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="155" height="140" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="92" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. 위상 연산자</text>
  <text x="92" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Contains (포함)</text>
  <text x="92" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Within (속함)</text>
  <text x="92" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Intersects (교차)</text>
  <text x="92" y="135" text-anchor="middle" font-size="11" fill="#64748b">ST_Touches / Disjoint</text>

  <!-- Box 2 -->
  <rect x="182" y="20" width="155" height="140" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="260" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. 거리 연산자</text>
  <text x="260" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Distance (최단거리)</text>
  <text x="260" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_DWithin (반경판별)</text>
  <text x="260" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Length (선분길이)</text>
  <text x="260" y="135" text-anchor="middle" font-size="11" fill="#64748b">인덱스 스캔 연계 필수</text>

  <!-- Box 3 -->
  <rect x="350" y="20" width="155" height="140" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="427" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. 변환/집합 연산자</text>
  <text x="427" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Buffer (버퍼영역)</text>
  <text x="427" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Union (합집합)</text>
  <text x="427" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">ST_Intersection (교차면)</text>
  <text x="427" y="135" text-anchor="middle" font-size="11" fill="#64748b">ST_Difference (차집합)</text>
</svg>
</div>

| 분류 | 주요 함수 | 연산 목적 및 기능 설명 | 반환 타입 |
|:---|:---|:---|:---:|
| **위상 연산자 (Topological)** | `ST_Contains(A, B)`<br/>`ST_Within(A, B)`<br/>`ST_Intersects(A, B)`<br/>`ST_Touches(A, B)` | - A가 B를 완전히 포함하는지 여부 판별<br/>- A가 B의 내부에 완전히 속하는지 여부<br/>- 두 객체가 한 점이라도 공간을 공유하는지 판별<br/>- 경계선에서만 접촉하고 내부는 공유하지 않는지 판별 | Boolean (True/False) |
| **거리 연산자 (Metric)** | `ST_Distance(A, B)`<br/>`ST_DWithin(A, B, dist)`<br/>`ST_Length(Line)` | - 두 객체 간의 최단 유클리드/구면 거리 계산<br/>- 두 객체의 거리가 dist 반경 이내인지 불리언 판정 (인덱스 지원)<br/>- 선형 객체의 총 길이 계산 | Float / Boolean |
| **공간 변환·집합 (Constructive)** | `ST_Buffer(geom, radius)`<br/>`ST_Union(A, B)`<br/>`ST_Intersection(A, B)`<br/>`ST_Difference(A, B)` | - 객체 주위로 지정 반경만큼 확장된 다각형 영역 생성<br/>- 두 공간 객체를 결합하여 단일 기하 객체로 병합<br/>- 두 공간 객체의 공통 교차 영역 다각형 추출<br/>- A 영역에서 B 영역을 차감한 잔여 영역 반환 | Geometry (Polygon 등) |

### Ⅲ. 공간 질의 처리의 2단계(Filter & Refine) 메커니즘

#### 한줄 요약: MBR 공간 인덱스를 통한 1차 후보군 축약(Filter) 후 정밀 기하 연산(Refine)을 수행하는 최적화 파이프라인

1. **MBR (Minimum Bounding Rectangle, 최소경계사각)**:
   - 복잡한 수천 개 정점의 다각형을 외곽을 감싸는 가장 작은 직사각형(Xmin, Ymin, Xmax, Ymax)으로 단순화
   - R-Tree, R*-Tree, PostGIS GiST 인덱스는 이 MBR을 키로 계층적 B-Tree 형태로 관리
2. **1단계: MBR 필터링 단계 (Filter Phase)**:
   - 질의 대상 영역의 MBR과 데이터 테이블의 공간 인덱스(R-Tree)를 비교하여 MBR이 겹치는 후보 레코드만 고속 추출
   - CPU 비용이 거의 들지 않으며, 전체 데이터셋의 95~99%를 순식간에 탈락시킴
3. **2단계: 정밀 기하 연산 단계 (Refine Phase)**:
   - 1단계를 통과한 극소수 후보 객체들의 실제 정점(Vertex) 좌표를 디스크에서 읽어옴
   - DE-9IM 수학 모델을 기반으로 선분 교차점 및 포함 관계를 엄밀하게 계산하여 최종 질의 조건 만족 여부 결정

### Ⅳ. 핵심 위상 판정 모델: DE-9IM (Dimensionally Extended 9-Intersection Model)

#### 한줄 요약: 두 공간 객체의 내부(Interior), 경계(Boundary), 외부(Exterior)가 만나는 교차 차원을 $3 \times 3$ 행렬로 규격화한 수학적 모델

- **개념**: 두 기하 객체 $A$와 $B$의 세 가지 구성 요소(내부 $I$, 경계 $B$, 외부 $E$)의 교차 집합 차원($-1, 0, 1, 2$)을 $3 \times 3$ 행렬로 정의

$$\begin{pmatrix} \dim(I(A) \cap I(B)) & \dim(I(A) \cap B(B)) & \dim(I(A) \cap E(B)) \\ \dim(B(A) \cap I(B)) & \dim(B(A) \cap B(B)) & \dim(B(A) \cap E(B)) \\ \dim(E(A) \cap I(B)) & \dim(E(A) \cap B(B)) & \dim(E(A) \cap E(B)) \end{pmatrix}$$

- 차원 값 정의:
  - `-1` (또는 `F`): 교차점이 전혀 없음 (공집합)
  - `0`: 점(Point) 형태로 교차
  - `1`: 선(Line) 형태로 교차
  - `2`: 면(Polygon) 형태로 교차
  - `T`: 차원에 관계없이 교차점이 존재함 (0, 1, 2 중 하나)
  - `*`: 어떤 값이든 상관없음 (Don't care)
- **주요 연산자 매핑 예시**:
  - `ST_Intersects`: 교차 행렬의 $I(A) \cap I(B) \neq \emptyset$ 또는 $B(A) \cap B(B) \neq \emptyset$ 등 최소 하나 이상 접촉
  - `ST_Disjoint`: 9개 교차 공간 중 외부($E \cap E$)를 제외한 모든 내부/경계 교차가 `F` (완전 분리)

### Ⅴ. 주요 공간 연산자 기능 비교

#### 한줄 요약: 포함 관계의 주체에 따른 Contains/Within, 교차의 Intersects, 거리 기반 반경의 DWithin

| 연산자 | 질의 구문 예시 | 판정 조건 및 특징 | 인덱스 활용 여부 |
|:---|:---|:---|:---:|
| **ST_Contains** | `ST_Contains(A, B)` | B의 모든 점이 A의 내부에 속하고 외부는 겹치지 않음 (A가 B를 포함) | GiST / R-Tree 인덱스 지원 |
| **ST_Within** | `ST_Within(A, B)` | A가 B의 내부에 완전히 속함 (`ST_Contains(B, A)`와 동치) | GiST / R-Tree 인덱스 지원 |
| **ST_Intersects** | `ST_Intersects(A, B)` | A와 B가 경계선이든 내부든 한 점이라도 접촉하거나 공유함 | GiST / R-Tree 인덱스 지원 |
| **ST_Distance** | `ST_Distance(A, B)` | A와 B 사이의 수학적 최단 거리를 부동소수점 실수로 계산 | **인덱스 미적용 (풀스캔 유발)** |
| **ST_DWithin** | `ST_DWithin(A, B, d)` | A와 B 사이의 거리가 `d` 이내인지 여부를 MBR 확장 박스로 판별 | **GiST 인덱스 완벽 활용 (고속)** |

### Ⅵ. 실무 성능 최적화 및 트러블슈팅

#### 한줄 요약: ST_DWithin 치환, 좌표계(SRID) 통일, 복잡 다각형 단순화(ST_Simplify)

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **반경 검색 쿼리 타임아웃** | `WHERE ST_Distance(loc, rider) < 3000` 사용으로 공간 인덱스를 타지 못하고 테이블 풀스캔 | 인덱스 스캔을 지원하는 `WHERE ST_DWithin(loc, rider, 3000)`으로 함수 전면 교체 |
| **거리 계산 수 킬로미터 오차** | 평면 직교 좌표계(EPSG:5186)와 구면 좌표계(EPSG:4326, WGS84) 간 SRID 불일치 연산 | `ST_Transform(geom, 5186)`을 통해 동일 투영 좌표계로 변환하거나 PostGIS `Geography` 타입 채택 |
| **대규모 폴리곤 연산 시 CPU 100%** | 해안선, 국경선 등 정점이 수만 개인 폴리곤 간의 `ST_Intersects` 조인 연산 | `ST_SimplifyPreserveTopology(geom, tolerance)`를 적용하여 정점 수를 90% 이상 압축 후 연산 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 공간 연산자는 일반적인 B-Tree 인덱스가 작동하지 않는 2차원 이상의 다차원 공간 데이터를 다루기 때문에, RDBMS 질의 중 가장 많은 CPU와 메모리를 소모하는 **초고비용 연산**이다.
> 실무에서 공간 쿼리 성능이 터지는 이유는 대부분 '정밀 기하 연산의 남용'과 '인덱스 미적용 거리 함수(`ST_Distance`) 사용'에 있다.
> 따라서 공간 데이터 아키텍처의 핵심은 "어떻게 하면 1단계 MBR 필터링에서 99%를 걸러내어 2단계 정밀 기하 연산으로 넘어가는 데이터양을 최소화할 것인가"에 집중되어야 한다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "PostgreSQL/PostGIS 환경에서 `Geometry` 타입(평면 유클리드)과 `Geography` 타입(구면 타원체)의 트레이드오프"를 언급하겠다. 전 지구적 거리 왜곡을 피하기 위한 측지학적 모델링 원칙을 제시하고, 공간 조인(Spatial Join) 시 `ST_Subdivide` 기법을 통해 초대형 폴리곤을 작은 조각으로 미리 분할 인덱싱하는 엔지니어링 해법을 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 위치기반 서비스(LBS)의 트래픽 급증 환경에서 단순 기하 연산은 심각한 CPU 병목을 유발하므로, 공간 인덱스와 2단계 처리 파이프라인의 엄격한 최적화가 필수적임.
- **대응**:
  1. **인덱스 친화적 쿼리 강제**: `ST_Distance` 사용을 금지하고 `ST_DWithin` 및 바운딩 박스 연산자(`&&`) 사용을 코딩 표준으로 수립.
  2. **초대형 폴리곤 분할**: 정점이 수천 개 이상인 대형 구역 폴리곤은 `ST_Subdivide`를 통해 256개 정점 단위로 분할 저장하여 R-Tree 인덱스 효율 극대화.
  3. **좌표계(SRID) 표준화**: 글로벌 LBS는 EPSG:4326(WGS84), 국내 정밀 시설물 관제는 EPSG:5186(중부원점)으로 SRID를 일원화하고 저장 단계에서 검증.
- **검증**: `EXPLAIN ANALYZE` 실행 계획을 통해 `Bitmap Index Scan on GiST` 적용 여부 및 쿼리 응답 시간 50ms 미만 검증.
- **효과**: 대규모 동시 접속 환경에서 공간 질의 처리 성능 50배 이상 향상 및 CPU 부하 안정화.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">ST_Distance 풀스캔, 수만 정점 폴리곤으로 CPU 100% 병목</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">ST_DWithin 치환, R-Tree 인덱스 연계, ST_Subdivide 분할</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">GiST 공간 인덱스 스캔 실행 계획 확인, 응답시간 50ms 미만</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">초고속 LBS 반경 검색 실현 및 서버 자원 사용량 80% 절감</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제124회 정보관리 1교시: 공간 데이터베이스의 공간 연산자(Spatial Operator)의 개념과 주요 유형(위상, 거리, 집합 연산)
- **검증 출처**:
  - Open Geospatial Consortium (OGC), "OpenGIS Simple Features Specification for SQL"
  - PostGIS Development Team, "PostGIS 3.4 Manual: Spatial Relationships and Measurements"
---

## 연결 토픽

- 상위 토픽: [03-052 다차원 색인 구조](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/052_multidimensional_index_structure.md)
- 연관 토픽: [03-117 IMDF](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/117_imdf.md), [03-047 인덱스(Index)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index.md)
