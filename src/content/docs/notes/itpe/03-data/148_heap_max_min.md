---
title: "힙(최대·최소 힙)"
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

**힙(Heap)**, **완전 이진 트리**, **최대/최소 힙**, **Heapify**, **우선순위 큐(Priority Queue)**, **힙 정렬(Heap Sort)**

## Ⅰ. 개요

- 핵심 요약 : **힙**은 완전 이진 트리 기반으로 최대/최솟값을 O(1)로 조회하는 자료구조.
- 목적 : 우선순위 큐, 힙 정렬, Top-K 탐색.
- 배경 : 최대/최솟값 빈번 조회·삽입/삭제 필요.
- 특징 : 형태 속성(완전 이진 트리), 힙 속성(부모-자식 대소 관계).

## Ⅱ. 특징 및 장점

- 핵심 요약 : **O(1) 최값 조회·O(log n) 삽입/삭제·O(n) 빌드**로 효율적.
- **형태 속성** : 완전 이진 트리 (마지막 레벨 좌측 채움).
- **힙 속성** : 최대 힙(부모≥자식), 최소 힙(부모≤자식).
- **배열 매핑** : 인덱스 산술로 O(1) 부모/자식 이동.
- **Heapify-Up/Down** : 삽입/삭제 시 O(log n) 복원.
- **Build Heap** : O(n) 일괄 구성.

## Ⅲ. 배열 매핑·연산 흐름

- 핵심 요약 : **1차원 배열 + 인덱스 산술**로 트리 표현.
- Parent(i)=floor(i/2), Left=2i, Right=2i+1 (1-based).

```text
[ 배열 인덱스 기반 힙 (1-based) ]

        [1] Root
       /        \
    [2]          [3]
   /   \        /   \
 [4]   [5]    [6]   [7]

Parent(i)=floor(i/2)
Left(i)=2i, Right(i)=2i+1
```

```text
[ 핵심 연산 ]

삽입 : 맨 끝 추가 -> Heapify-Up (O(log n))
삭제 : 루트 추출 -> 마지막을 루트 -> Heapify-Down (O(log n))
빌드 : 바닥부터 Heapify (O(n))
```

## Ⅳ. 연산 비교

- 핵심 요약 : **조회·삽입·삭제·빌드·검색** 복잡도 비교.

| 연산 | 시간 복잡도 | 비고 |
|---|---|---|
| 최값 조회 | O(1) | 루트 |
| 삽입 | O(log n) | Heapify-Up |
| 삭제 | O(log n) | Heapify-Down |
| 빌드 | O(n) | 바닥부터 |
| 임의 검색 | O(n) | 선형 탐색 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **임의 검색·캐시 비친화·락 병목**을 색인 힙·d-ary·락프리로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 임의 검색/삭제 O(n) | 중간 원소 선형 탐색 | 색인 힙(Hash Map 결합), Fibonacci Heap | 검색 시간 |
| 캐시 비친화 | 깊은 트리에서 캐시 미스 | d-ary 힙 (4/8자식), 캐시 인지 힙 | 캐시 미스율 |
| 멀티스레드 락 병목 | 단일 뮤텍스 경합 | 락프리 Skip List, Work-Stealing | 처리량 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **0-based 인덱스·사전 할당·K-way Merge**.
- 0-based 매핑 : Left=2i+1, Right=2i+2, Parent=(i-1)/2 (비트 시프트).
- 사전 할당 메모리 풀로 재할당 지연 방지.
- K-way Merge·Top-K 탐색 응용.

## Ⅶ. 결론

- 핵심 요약 : 힙은 **우선순위 큐·힙 정렬·Top-K**의 기본 자료구조.
- 답안에는 형태/힙 속성, 배열 매핑, 연산 복잡도, 한계·대응을 연결.
- 참고 : [Heap (Wikipedia)](https://en.wikipedia.org/wiki/Heap_(data_structure)).