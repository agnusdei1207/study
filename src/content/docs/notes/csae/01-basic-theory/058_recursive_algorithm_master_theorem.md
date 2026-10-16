---
title: "재귀 알고리즘·마스터 정리(Recursive Algorithm Master Theorem)"
date: "2026-09-20T11:00:00+09:00"
tags:
  - "notes-basic-theory"
sidebar:
  badge:
    text: "C · 미출 · 50%"
extra:
  source_status: "미출"
  source_history: ""
  priority: 50
  priority_note: "-"
---

## 답안 골격
```text
[재귀와 마스터 정리] ◀━━ 머리: 점화식의 분할-결합 연산량과 재귀 리프 비용 비교를 통한 시간 복잡도 즉시 판정
 ┃
 ┣━ Ⅰ 개요 ───── 재귀 점화식 전개 복잡성 한계 → $T(n) = aT(n/b) + f(n)$ 형태의 점근 복잡도를 공식으로 즉시 해결
 ┣━ Ⅱ 수식 ───── 마스터 정리 기본형: $T(n) = a T(n/b) + f(n)$ ($a \ge 1, b > 1, f(n) = \Theta(n^c)$)
 ┣━ Ⅲ 조건 ───── 임계 지수 $\log_b a$와 분할/결합 차수 $c$ 간의 대소 비교를 통한 3대 케이스 판정
 ┣━ Ⅳ 3케이스 ── Case 1($c < \log_b a \to \Theta(n^{\log_b a})$) · Case 2($c = \log_b a \to \Theta(n^c \log n)$) · Case 3($c > \log_b a \to \Theta(f(n))$)
 ┣━ Ⅴ 비교 ───── 치환법(Substitution) vs 재귀 트리(Recursion Tree) vs 마스터 정리(Master Theorem)
 ┗━ Ⅵ 실무 ───── 병합 정렬($O(n \log n)$) · 스트라센 행렬 곱셈($O(n^{2.81})$) · 꼬리 재귀 최적화
```
- 필수 키워드: 점화식 · 마스터 정리(Master Theorem) · 임계 지수($\log_b a$) · 3대 케이스 · 꼬리 재귀(Tail Recursion)

## 한 줄 본질
- 분할 정복 알고리즘의 재귀 점화식을 트리로 일일이 전개하지 않고 하위 문제 분할 수($a$), 크기 감소율($b$), 결합 비용($f(n)$)의 비율만으로 시간 복잡도를 한 번에 판정 → 알고리즘 효율성 즉시 검증 / 비표준 점화식 적용 불가

## 핵심 그림
```text
[마스터 정리 3대 판정 케이스 (기준: log_b(a) vs c)]
  T(n) = a * T(n / b) + Theta(n^c)
  
  임계값: log_b(a)
    ^
    |-- Case 1: log_b(a) > c  ===> T(n) = Theta(n^(log_b a))  [리프 노드 연산 지배]
    |   (예: 스트라센 행렬곱 T(n)=7T(n/2)+O(n^2) -> n^(log_2 7) = O(n^2.81))
    |
    |-- Case 2: log_b(a) == c ===> T(n) = Theta(n^c * log n)  [모든 계층 비용 균등]
    |   (예: 병합 정렬 T(n)=2T(n/2)+O(n) -> log_2(2)=1 == c -> O(n log n))
    |
    +-- Case 3: log_b(a) < c  ===> T(n) = Theta(f(n))         [루트 분할/결합 지배]
```

## 핵심 통찰
- 마스터 정리의 직관적 본질은 "재귀 트리의 바닥(Leaf)에서 일어나는 총 연산량 $n^{\log_b a}$"과 "문제를 쪼개고 합치는 데 드는 오버헤드 $f(n)$" 중 어느 쪽이 수학적으로 지배적인가를 가리는 것임
- 함수 호출 스택의 한계로 인한 재귀 함수의 스택 오버플로를 막기 위해, 컴파일러가 반환 직전의 재귀 호출을 단순 루프로 치환하는 '꼬리 재귀 최적화(Tail Call Optimization)'를 적용함

## 이웃 토픽과 구분
- 점화식 해결 기법 비교: 재귀 트리법(트리 각 레벨의 비용을 직접 그려 합산하는 직관적 방법) vs 마스터 정리(표준 분할 정복 형태 $aT(n/b)+f(n)$에 한해 수식 대입만으로 1초 만에 해를 도출하는 공식)

## 이렇게 출제된다
- 미출 대비: "분할 정복 재귀 알고리즘의 시간 복잡도 분석을 위한 마스터 정리(Master Theorem)의 수식 및 3가지 케이스 판정 기준" → 요구 포인트: $aT(n/b)+f(n)$ 형태, $\log_b a$와 $c$ 비교 3가지 케이스, 병합 정렬 대입 유도
