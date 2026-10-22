---
title: "공간 연산자"
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

**공간 연산자(Spatial Operator)**, **OGC**, **DE-9IM**, **R-Tree**, **2단계 질의**, **Geometry/Geography**, **SRID**

## Ⅰ. 개요

- 핵심 요약 : **공간 연산자**는 기하 객체 간 위상·기하·방향 관계를 판별·조작하는 OGC 표준 함수.
- 목적 : 공간 데이터베이스에서 공간 질의 고속 처리.
- 배경 : 단순 수치 비교로는 공간 관계 표현 불가 → 전용 연산자 필요.
- 특징 : OGC 표준, DE-9IM 모델, R-Tree 인덱스 결합.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **위상 관계 판별·기하 조작·인덱스 결합**으로 공간 질의 고속화.
- **공간 관계** : Contains, Intersects, Touches, Disjoint 등.
- **공간 분석** : Buffer, Distance, Intersection, Union.
- **공간 변환** : 좌표계 변환, 단순화, 포맷 변환.
- **인덱스 결합** : R-Tree/GiST로 고속 필터링.
- **2단계 질의** : MBR 필터링 → 정밀 검사.

## Ⅲ. 2단계 질의 흐름

- 핵심 요약 : **MBR 필터링 → 정밀 기하 검사** 2단계 처리.
- DE-9IM : 3×3 행렬로 위상 관계 수학적 정의.

```text
[ 공간 연산자 3대 분류 ]

1. 공간 관계 (Relationship) : Contains, Intersects, Touches, Disjoint
2. 공간 분석 (Analysis)     : Buffer, Distance, Intersection, Union
3. 공간 변환 (Transform)    : Proj, Simplify, GeoJSON/WKT
```

```text
[ 2단계 공간 질의 파이프라인 ]

[공간 쿼리] ---> [1단계: MBR 필터링 (R-Tree)]
                      후보군 대폭 압축
                          |
                          v
                  [2단계: 정밀 검사 (DE-9IM)]
                      실제 기하 엄격 계산
```

## Ⅳ. 공간 관계 함수 비교

- 핵심 요약 : **위상 관계·DE-9IM 패턴·활용 사례** 비교.

| 함수 | 위상적 의미 | DE-9IM 패턴 | 활용 사례 |
|---|---|---|---|
| ST_Contains(A,B) | A가 B를 완전 포함 | T*****FF* | 행정구역 내 상점 검색 |
| ST_Intersects(A,B) | 공간 공유 | T******** | 도로-하천 교차 지점 |
| ST_Touches(A,B) | 경계만 접촉 | FT******* | 인접 지자체 검색 |
| ST_Disjoint(A,B) | 완전 분리 | FF*FF**** | 침수 구역 밖 대피소 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **조인 복잡도·SRID 불일치·인덱스 재구성**을 2단계 처리·표준화·그리드로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 조인 복잡도 | 고차원 폴리곤 DE-9IM 연산 비용 급증 | 2단계 질의, ST_Simplify | 쿼리 응답 시간 |
| SRID 불일치 | 좌표계 혼재로 변환 오버헤드·왜곡 | 적재 시 표준 투영 변환, SRID 일치 | 변환 오류 수 |
| 인덱스 재구성 | 고빈도 삽입 시 R-Tree Split·MBR 재계산 | Geohash/H3/S2 그리드, Bulk Loading | 쓰기 레이턴시 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **Geometry/Geography 구분·바운딩 박스 연산자**로 성능 최적화.
- Geometry (평면) : 도시 단위 배달 반경, 고속 연산.
- Geography (구면) : 국가/대륙 간 정확 거리.
- `&&` 바운딩 박스 연산자 선행 강제로 인덱스 스캔 유도.

## Ⅶ. 결론

- 핵심 요약 : 공간 연산자는 **OGC 표준·DE-9IM·R-Tree**로 공간 질의 고속화.
- 답안에는 3대 분류, DE-9IM, 2단계 질의, 한계·대응을 연결.
- 참고 : [PostGIS](https://postgis.net/).