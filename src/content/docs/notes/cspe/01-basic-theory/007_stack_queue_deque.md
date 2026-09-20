---
title: "스택·큐·덱(Stack Queue Deque)"
date: "2026-09-20T11:00:00+09:00"
tags:
  - "notes-basic-theory"
sidebar:
  badge:
    text: "C · 미출 · 30%"
extra:
  source_status: "미출"
  source_history: ""
  priority: 30
  priority_note: "-"
---

## 답안 골격
```text
[기초 선형 자료구조] ◀━━ 머리: 데이터 입출력 제약에 따른 LIFO(스택), FIFO(큐), 양단(덱)의 구조화
 ┃
 ┣━ Ⅰ 개요 ───── 임의 접근 배열의 관리 복잡성 한계 → 접근 포인트를 끝단으로 제한한 추상 자료형(ADT)
 ┣━ Ⅱ 유형 ───── 스택(LIFO: 후입선출) · 큐(FIFO: 선입선출) · 덱(Deque: 양단 입출력 자유)
 ┣━ Ⅲ 구조 ───── Top 포인터 단일 조작(스택) vs Front/Rear 양방향 조작(큐, 덱)
 ┣━ Ⅳ 메커니즘 ─ 원형 큐(Circular Queue) 모듈러 인덱싱($(\text{rear}+1) \pmod N$)을 통한 메모리 재사용
 ┣━ Ⅴ 비교 ───── 스택 vs 큐 vs 덱 (동작 원리, 주요 연산 $O(1)$, 시스템 활용처)
 ┗━ Ⅵ 실무 ───── 시스템 콜 스택 · OS 작업 스케줄링 · Fork-Join 작업 훔치기(Work-Stealing)
```
- 필수 키워드: LIFO · FIFO · Top/Front/Rear · 원형 큐(Circular Queue) · 덱(Deque) · 작업 훔치기

## 한 줄 본질
- 데이터의 출입 순서를 후입선출(스택), 선입선출(큐), 양방향(덱)의 정형화된 규칙으로 강제 제약하여 연산 복잡도를 $O(1)$로 보장 → 명확한 실행 흐름 통제 / 임의 위치 원소 접근 불가

## 핵심 그림
```text
[스택: LIFO]             [큐: FIFO]                  [덱: Deque 양단 입출력]
   Push | ^ Pop               Enqueue         Dequeue       Push/Pop           Push/Pop
        v |                      |               ^             ^ |                | ^
     +-----+                  +--v---------------+--+         v |                v |
 Top |  C  |           Rear ->| C | B | A |   |  |  |-> Front +--------------------+
     +-----+                  +---------------------+         |  A  |  B  |  C  |  |
     |  B  |                  (선입선출 대기열 버퍼)           +--------------------+
     +-----+                                                  Front                Rear
     |  A  | (후입선출)
     +-----+
```

## 핵심 통찰
- 선형 큐는 앞에서 데이터를 꺼낼 때마다 앞 공간이 비어 있어도 뒤쪽이 차면 오버플로로 오판하는 '거짓 포화' 문제가 발생하므로, 모듈러 연산으로 배열의 양 끝을 둥글게 연결한 원형 큐(Circular Queue)가 필수적임
- 덱(Deque)은 스택과 큐를 포괄하는 상위 호환 자료구조로서, 멀티스레드 스케줄러가 자신의 큐에서는 LIFO(스택)로 캐시 친화적 처리를 하고 다른 스레드에서는 FIFO(큐)로 작업을 훔쳐오는 작업 훔치기(Work-Stealing)의 핵심 뼈대가 됨

## 이웃 토픽과 구분
- 스택 vs 큐 vs 덱:
| 비교 항목 | 스택 (Stack) | 큐 (Queue) | 덱 (Deque) |
|---|---|---|---|
| 입출력 원칙 | LIFO (Last In First Out) | FIFO (First In First Out) | 양단 어디서나 삽입/삭제 가능 |
| 조작 포인터 | Top (1개) | Front, Rear (2개) | Front, Rear (2개) |
| 시스템 대표 활용 | 함수 콜 스택, 실행 취소(Undo) | 프린터 스풀러, 패킷 버퍼, BFS | Fork-Join 프레임워크, 브라우저 방문 기록 |

## 이렇게 출제된다
- 미출 대비: "스택, 큐, 덱의 개념 및 동작 원리, 원형 큐의 필요성과 인덱스 연산식" → 요구 포인트: LIFO/FIFO 차이, 원형 큐 포화/공백 판정($\text{front} == \text{rear}$), 시스템 소프트웨어 응용
