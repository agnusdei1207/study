---
title: "선형 구조(Linear Structure)"
author: "Antigravity"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 선형 구조의 개요

- **개념** : 데이터 원소들이 논리적으로 하나의 연속된 순서를 가지며, 각 원소의 앞(이전)과 뒤(이후)에 1:1 관계를 유지하는 1차원적 형태의 기본 자료구조.
- **배경 및 필요성** : 프로그램 실행 시 연속된 데이터의 순차적 저장, 임의 접근, 버퍼링, LIFO/FIFO 처리 등 알고리즘 구현의 기초 빌딩 블록으로 활용.
- **대표적 종류** : 배열(Array), 연결 리스트(Linked List), 스택(Stack), 큐(Queue), 덱(Deque).

## Ⅱ. 선형 자료구조의 메모리 배치 및 동작 메커니즘

```text
   [ 배열 (Array) ] ────────── 물리적 메모리 연속 할당
     [ Index 0 ] [ Index 1 ] [ Index 2 ] [ Index 3 ] -> 인덱스 즉각 접근 O(1)
          │
   [ 연결 리스트 (Linked List) ] ─ 물리적 메모리 불연속, 포인터 연결
     [ Data|Next ] ──> [ Data|Next ] ──> [ Data|Next ] -> 삽입/삭제 O(1)
          │
   [ 스택 (Stack) ] ────────── LIFO (Last In First Out)
     Top -> [ D ] -> [ C ] -> [ B ] -> [ A ] (Bottom)
          │
   [ 큐 (Queue) ] ──────────── FIFO (First In First Out)
     Rear(Enqueue) -> [ D ] [ C ] [ B ] [ A ] -> Front(Dequeue)
```

- **배열 (Array)** : 연속된 메모리 공간에 동일한 타입의 데이터를 순서대로 배치하여 인덱스를 통한 직접 접근(Random Access)이 $O(1)$로 매우 빠름.
- **연결 리스트 (Linked List)** : 각 노드가 데이터와 다음 노드를 가리키는 포인터를 보유하여 동적 크기 할당 및 중간 삽입/삭제가 용이하나, 임의 접근 시 $O(N)$ 소요.
- **큐 (Queue) & 덱 (Deque)** : 큐는 한쪽(Rear)에서 삽입, 반대쪽(Front)에서 삭제가 일어나는 선입선출(FIFO) 구조이며, 덱(Double-Ended Queue)은 양쪽 끝 모두에서 삽입과 삭제가 가능한 유연한 구조.

## Ⅲ. 주요 선형 자료구조의 시간복잡도 비교

| 자료구조 | 접근(Access) | 탐색(Search) | 삽입(Insertion) | 삭제(Deletion) | 메모리 오버헤드 |
|---|---|---|---|---|---|
| 배열 (Array) | $O(1)$ | $O(N)$ | $O(N)$ (밀어내기) | $O(N)$ (당기기) | 없음 (순수 데이터만 저장) |
| 연결 리스트 (Linked List) | $O(N)$ | $O(N)$ | $O(1)$ (해당 위치) | $O(1)$ (해당 위치) | 포인터 저장 메모리 발생 |
| 스택 (Stack) | $O(N)$ (Top 외 불가) | $O(N)$ | $O(1)$ (Push) | $O(1)$ (Pop) | 최소 (구현 방식에 의존) |
| 큐 (Queue) | $O(N)$ (Front 외 불가) | $O(N)$ | $O(1)$ (Enqueue) | $O(1)$ (Dequeue) | 원형 큐 관리 또는 포인터 |
| 덱 (Deque) | $O(1)$ (양단) | $O(N)$ | $O(1)$ (양단) | $O(1)$ (양단) | 양방향 포인터 또는 환형 배열 |

## Ⅳ. 고성능 컴퓨팅 환경에서의 기술사적 제언

- **CPU 캐시 지역성(Spatial/Temporal Locality)에 기반한 배열 선호** : 이론적으로 연결 리스트의 삽입/삭제 복잡도가 $O(1)$이지만, 현대 CPU 아키텍처에서는 메모리가 불연속 분산된 연결 리스트 노드 순회 시 L1/L2 캐시 미스가 빈번하여, 실제로는 연속 메모리를 사용하는 동적 배열(Vector, ArrayList)이 훨씬 높은 성능을 발휘함을 인지해야 함.
- **대규모 버퍼링 시스템에서의 원형 큐(Circular Queue) 및 링 버퍼(Ring Buffer) 채택** : 큐의 선형 배열 구현 시 발생하는 메모리 낭비와 데이터 이동 오버헤드를 제거하기 위해 모듈로($\%$) 연산을 활용한 원형 큐 또는 LMAX Disruptor 같은 락프리 링 버퍼를 적용하여 초고속 트랜잭션 버퍼 구축 권장.
