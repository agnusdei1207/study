---
title: "MOLAP (Multidimensional OLAP) (MOLAP: Multidimensional Online Analytical Processing)"
author: "agnusdei1207"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Antigravity Professional Engine"
---

## 연관 키워드

**MOLAP**, **다차원 큐브(Cube)**, **사전 집계(Pre-aggregation)**, **큐브 폭발(Cube Explosion)**, **희소성(Sparsity)**, **ROLAP/HOLAP**

## Ⅰ. 개요

- 핵심 요약 : **MOLAP**은 다차원 배열 큐브에 데이터를 저장하고 사전 집계하여 초고속 분석을 제공하는 OLAP 기술.
- 목적 : 다차원 분석의 O(1) 조회.
- 배경 : ROLAP의 런타임 집계 지연 → 사전 집계 필요.
- 특징 : MDDB, Hypercube, 사전 집계, 큐브 폭발.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **다차원 배열·사전 집계·O(1) 조회**로 초고속 분석.
- **다차원 배열** : Array[시간][지역][상품] 직접 접근.
- **사전 집계** : 배치 적재 시 모든 차원 조합 집계.
- **JOIN 배제** : 배열 오프셋 계산으로 즉시 조회.
- **희소성 압축** : CSR/CSC로 빈 셀 제거.
- **HOLAP** : 인메모리 MOLAP + ROLAP 페더레이션.

## Ⅲ. 큐브 구조 흐름

- 핵심 요약 : **다차원 큐브 + 사전 집계 + 희소 압축**.
- 큐브 폭발 : $\prod C_i$ 기하급수 증가.

```text
[ MOLAP vs ROLAP ]

MOLAP : MDDB 큐브, 사전 집계, O(1) 조회, 큐브 폭발 한계
ROLAP : RDBMS 스타 스키마, 런타임 SQL, 무제한 확장, 지연 가변
```

```text
[ 큐브 폭발 ]

Total Cells = C1 x C2 x ... x CD
10차원 x 100항목 = 100^10 = 10^20 셀
```

## Ⅳ. MOLAP vs ROLAP 비교

- 핵심 요약 : **저장 엔진·집계 시점·속도·확장성·상세 추적** 비교.

| 항목 | MOLAP | ROLAP |
|---|---|---|
| 저장 엔진 | MDDB 큐브 | RDBMS 스타 스키마 |
| 집계 시점 | 배치 사전 집계 | 런타임 SQL |
| 조회 속도 | O(1) 배열 접근 | 가변 (조인 복잡도) |
| 확장성 | 큐브 폭발로 수십 GB 한계 | PB급 무제한 |
| 상세 추적 | 제약 | 로우 레벨까지 드릴다운 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **큐브 폭발·희소성·확장 한계**를 압축·HOLAP·휴리스틱으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 큐브 폭발 | 차원×카디널리티 기하급수 증가 | 희소 압축(CSR/CSC), HOLAP | 큐브 크기 |
| 희소성 | 빈 셀이 대부분 차지 | 빈 셀 제거, 좌표만 저장 | 압축률 |
| 확장성 한계 | 수십 GB 내외 | ROLAP 페더레이션, 인메모리 큐브 | 처리량 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **HOLAP·인메모리 큐브·휴리스틱 사전 집계**.
- 인메모리 MOLAP (VertiPaq) + ROLAP 페더레이션.
- 쿼리 로그 기반 핵심 차원 조합만 사전 집계 (파레토).
- 사전 집계 범위 휴리스틱 최적화.

## Ⅶ. 결론

- 핵심 요약 : MOLAP은 **다차원 배열 사전 집계**로 초고속 분석, 큐브 폭발이 핵심 과제.
- 답안에는 큐브 구조, MOLAP/ROLAP 비교, 한계·대응을 연결.
- 참고 : [Microsoft Analysis Services](https://learn.microsoft.com/analysis-services/).