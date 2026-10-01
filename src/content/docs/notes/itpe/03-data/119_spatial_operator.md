---
title: "공간 연산자"
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

## Ⅰ. 지리공간 데이터베이스의 핵심, 공간 연산자의 개요

### 가. 공간 연산자(Spatial Operator)의 정의
- 2차원 또는 3차원 공간 상에 존재하는 기하학적 객체(점, 선, 면) 간의 위상적(Topological), 기하학적(Geometric), 방향적(Directional) 관계를 수학적으로 판별하고 조작하기 위해 OGC(Open Geospatial Consortium) 표준 및 SQL/MM 표준에 정의된 데이터베이스 연산 함수.
- 단순 수치 비교 연산자와 달리 공간 인덱스(R-Tree, GiST)와 결합하여 공간 질의를 초고속으로 필터링함.

---

## Ⅱ. OGC 표준 3대 공간 연산자 분류 및 DE-9IM 모델

### 가. 공간 연산자의 3대 기능적 분류

```text
[ 공간 연산자 3대 분류 체계 ]
1. 공간 관계 연산자 (Spatial Relationship) : 두 공간 객체 간의 위상적 포함/교차/접촉 여부 판별 (True/False)
2. 공간 분석 연산자 (Spatial Analysis)     : 거리 계산, 교집합 면적, 버퍼 생성 등 새로운 공간 기하 생성
3. 공간 변환 연산자 (Spatial Transform)    : 좌표계 변환(Proj), 단순화(Simplify), 포맷 변환(GeoJSON/WKT)
```

### 나. 9-교차 모델 (DE-9IM, Dimensionally Extended 9-Intersection Model)
- 두 기하 객체 $A, B$의 **내부(Interior, $I$), 경계(Boundary, $B$), 외부(Exterior, $E$)** 가 상호 교차할 때 형성되는 교집합 영역의 차원(Dimension: -1=공집합, 0=점, 1=선, 2=면)을 $3 \times 3$ 행렬로 표현하여 모든 위상 관계를 수학적으로 정의.

| 공간 관계 함수 | 위상적 의미 및 조건 | DE-9IM 패턴 | 실제 비즈니스 활용 사례 |
| :--- | :--- | :--- | :--- |
| **ST_Contains(A, B)** | 기하 객체 $A$가 $B$를 내부에 완전히 포함함 | `T*****FF*` | 특정 행정구역(구/동) 폴리곤 내에 위치한 상점 검색 |
| **ST_Intersects(A, B)** | 두 객체 $A, B$가 점, 선, 면 중 어느 하나라도 공간을 공유함 | `T********` | 도로 경로와 하천이 교차하는 교량 지점 탐색 |
| **ST_Touches(A, B)** | 두 객체의 경계선만 접하고 내부는 전혀 겹치지 않음 | `FT*******` | 국경선이나 행정구역 경계를 맞대고 있는 인접 지자체 검색 |
| **ST_Disjoint(A, B)** | 두 객체가 공간적으로 완전히 분리되어 전혀 만나지 않음 | `FF*FF****` | 침수 위험 구역 밖에 안전하게 위치한 대피소 검증 |

---

## Ⅲ. 주요 공간 기하 조작 및 분석 함수

### 가. 공간 연산 및 기하 생성 함수

```text
[ 주요 공간 기하 조작 함수 ]
- ST_Buffer(geom, radius)   : 특정 객체로부터 반경 r 이내의 완충 영역(폴리곤) 생성
- ST_Distance(geomA, geomB) : 두 기하 객체 간의 최단 유클리디안/대권 거리 계산
- ST_Intersection(A, B)     : 두 폴리곤이 겹치는 공통 교집합 기하 추출
- ST_Union(geomA, geomB)    : 복수의 기하 객체를 하나의 단일 폴리곤으로 병합
```

### 나. 2단계 공간 질의 처리(Two-Tier Spatial Query) 메커니즘

```text
[ 2단계 공간 필터링 파이프라인 ]
[사용자 공간 쿼리] ---> [1단계: 필터링 단계 (Filter Step)]
                              - 인덱스(R-Tree)를 사용하여 MBR(경계 사각형) 겹침 스캔
                              - 연산 비용 극소, 후보군(Candidate) 대폭 압축
                              |
                              v
                        [2단계: 정밀 검사 단계 (Refinement Step)]
                              - 실제 정밀 폴리곤 좌표를 대상으로 DE-9IM 엄격 계산
                              - 연산 비용 높으나 대상 수가 적어 고속 처리 완료
```

---

## Ⅳ. 고성능 공간 데이터베이스 구축을 위한 실무 제언

- **구면 좌표계(Geography) vs 평면 좌표계(Geometry)의 구분 사용** :
  - **Geometry (SRID 3857 등 투영좌표계)** : 평면 직교 좌표계로 연산 속도가 극도로 빠르나, 장거리 거리 계산 시 왜곡 발생. 도시 단위 배달 반경 검색에 최적.
  - **Geography (SRID 4326 WGS84 타원체)** : 대권 거리(Great-Circle Distance)를 정확히 계산하나 삼각함수 연산 부하 큼. 국가/대륙 간 항공 경로에 적용.
- **공간 인덱스 바운딩 박스 연산자(`&&`)의 선행 강제** : 복잡한 정밀 함수(`ST_Contains`)를 단독 호출하면 풀 스캔이 발생할 수 있으므로, PostGIS 등에서 항상 MBR 겹침 연산자(`geomA && geomB`)가 옵티마이저에 의해 실행 계획 상 최우선 인덱스 스캔으로 풀리도록 쿼리를 최적화할 것을 제언함.
