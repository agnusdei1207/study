---
title: "스택(Stack) 자료구조"
author: "OpenAI Codex"
date: "2026-09-20T00:25:00+09:00"
tags: ["notes-software-engineering"]
sidebar:
  badge:
    text: "A"
extra:
  model: "OpenAI Codex"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="자료구조에서 스택까지의 지식 경로"><span>SW 공학·자료구조</span><span>선형 자료구조</span><strong>스택(Stack)</strong></div>

## 큰 그림과 30초 인출

```text
 Push(D) ↓       Pop() ↑
       ┌───┐
 Top → │ D │  후입선출 LIFO
       ├───┤
       │ C │  배열: top index / 연결: head pointer
       ├───┤
       │ B │
       └───┘
```

## 예상문제

> 스택의 개념·구조와 연산을 설명하고 큐·덱과 비교한 후 호출 스택 등 활용 및 오류 대응을 제시하시오.

## Ⅰ. 개요 ───── 최근 상태를 먼저 복원하는 LIFO

스택은 한쪽 끝 Top에서 삽입과 삭제를 수행하는 후입선출 자료구조다. 함수 호출·수식 처리·탐색 되돌리기처럼 최근 상태를 먼저 복원하는 문제에 적합하다.

## Ⅱ. 특징 ───── 제한 접근과 일정 시간 연산

| 특징 | 내용 |
|---|---|
| LIFO | 마지막 입력을 먼저 출력 |
| 단일 접근점 | Top에서 Push·Pop·Peek |
| 시간복잡도 | 정상 구현의 Push·Pop은 O(1) |
| 구현 | 배열 기반 또는 연결 구조 |
| 오류 | 빈 스택 Pop은 Underflow, 용량 초과는 Overflow |

## Ⅲ. 구조 ───── 배열·연결 구현

```text
Array Stack                    Linked Stack
data[0..capacity-1]            top→[D]→[C]→[B]→null
top = 마지막 원소 index         Push: head 삽입
Push: ++top 후 저장             Pop : head 제거
```

## Ⅳ. 동작 ───── Push·Pop·Peek

```text
Push(x): 용량확인 → top 증가 → data[top]=x
Pop()  : 공백확인 → value=data[top] → top 감소 → value
Peek() : 공백확인 → data[top] 반환, 제거 없음
```

불변식은 Top이 항상 마지막 유효 원소를 가리키며 원소 수와 경계를 벗어나지 않는 것이다.

## Ⅴ. 비교 ───── 스택·큐·덱

| 기준 | 스택 | 큐 | 덱 |
|---|---|---|---|
| 원리 | LIFO | FIFO | 양 끝 입출력 |
| 삽입/삭제 | Top/Top | Rear/Front | Front·Rear |
| 활용 | 호출·Undo·DFS | 요청·BFS·Buffer | Sliding Window |
| 핵심 오류 | 깊이·용량 초과 | 포화·기아 | 경계 관리 |

## Ⅵ. 고려 ───── 호출 스택과 안전성

| 문제 | 원인 | 대응 | 확인 |
|---|---|---|---|
| Stack Overflow | 무한 재귀·깊은 호출 | 종료조건, 반복·명시 스택 전환 | 최대 깊이 |
| Underflow | 빈 상태 Pop | 사전조건·예외 처리 | 빈 입력 시험 |
| 고정 배열 초과 | 용량 추정 실패 | 동적 확장·연결 구현 | 최대 원소 수 |
| 메모리 잔존 | Pop 후 참조 유지 | 참조 해제 | 누수 검사 |
| 동시 접근 | 비원자 Top 갱신 | 소유권·동기화·동시 스택 | 경쟁 시험 |

## Ⅶ. 결론 ───── LIFO 불변식과 경계조건 검증

스택은 단순하지만 호출과 상태 복원의 기반이다. 구현 방식보다 LIFO·Top 불변식, Overflow·Underflow와 재귀 깊이를 명시하고 입력 규모와 동시성 조건에 맞게 선택해야 한다.

## 1교시 10점 발췌

```text
Stack = Top 한쪽에서 Push·Pop하는 LIFO 선형 자료구조
연산: Push·Pop·Peek O(1), 오류: Overflow·Underflow
구현: Array(top index) / Linked(top pointer)
활용: Call Stack·Undo·괄호검사·DFS·수식변환
```

## 공식 근거

- [NIST Dictionary of Algorithms and Data Structures — Stack](https://xlinux.nist.gov/dads/HTML/stack.html)
- Q-Net 제132회 2교시 6번, 제138회 3교시 3번

## 체크

- [ ] Top과 Push·Pop을 손그림으로 표현했는가
- [ ] 배열·연결 구현과 경계조건을 썼는가
- [ ] 큐·덱을 동일 기준으로 비교했는가

## 연결 토픽

- [선형 자료구조](./053_linear_structure/)
- [비선형 자료구조](./052_non_linear_structure/)
- [힙](./092_heap/)
