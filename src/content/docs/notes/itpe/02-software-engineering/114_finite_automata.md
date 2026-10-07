---
title: "유한 오토마타(Finite Automata)"
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

## Ⅰ. 유한 오토마타의 개요

- 개념 : **유한 오토마타** (Finite Automata) 란 유한한 개수의 상태(States)를 가지며, 외부에서 입력 기호(Symbol)가 주어질 때마다 정의된 **전이 함수** (Transition Function)에 따라 현재 상태에서 다음 상태로 전이하고 특정 **수락 상태** (Accepting State)에 도달하는지 여부를 판별하는 계산 이론 상의 추상 수학 기계.
- 배경 및 필요성 : 컴파일러의 어휘 분석기(Lexer), 정규 표현식(Regular Expression) 매칭 엔진, 네트워크 프로토콜 상태 제어기, 하드웨어 순차 회로를 수학적으로 정형화하고 효율적으로 구현하기 위해 필수.
- 2대 분류 : **결정적 유한 오토마타** (DFA)와 **비결정적 유한 오토마타** (NFA)

## Ⅱ. DFA와 NFA의 구조 및 톰슨(Thompson) 구성 알고리즘

```text
   [ 정규 표현식 (Regex: (a|b)*c) ]
                 │
                 ▼ (톰슨 구성법: Thompson's Construction)
   [ 비결정적 유한 오토마타 (NFA) ] ── 입실론(ε) 전이 허용, 단일 입력에 다중 상태 전이 가능
                 │
                 ▼ (부분집합 구성법: Subset Construction)
   [ 결정적 유한 오토마타 (DFA) ] ──── 각 상태에서 특정 입력 기호당 정확히 하나의 전이만 존재
                 │
                 ▼ (홉크로프트 알고리즘: Hopcroft's Algorithm)
   [ 최소화된 DFA (Minimized DFA) ] ── 상태 수를 최소화하여 고속 메모리 룩업 테이블 구현
```

- **DFA 5-튜플 정의** : $M = (Q, \Sigma, \delta, q_0, F)$
  - $Q$ : 유한한 상태들의 집합.
  - $\Sigma$ : 유한한 입력 알파벳 집합.
  - $\delta$ : 상태 전이 함수 ($Q \times \Sigma \to Q$).
  - $q_0$ : 초기 시작 상태 ($q_0 \in Q$).
  - $F$ : 최종 수락 상태들의 집합 ($F \subseteq Q$).

## Ⅲ. DFA와 NFA의 특성 비교

| 비교 항목 | 결정적 유한 오토마타 (DFA) | 비결정적 유한 오토마타 (NFA) |
|---|---|---|
| 상태 전이의 유일성 | 현재 상태와 입력에 대해 다음 상태가 유일하게 결정 | 단일 입력에 대해 복수의 다음 상태로 분기 가능 |
| 입실론($\epsilon$) 전이 | 허용하지 않음 (반드시 입력 기호 소비 필요) | 입력 기호 소비 없이도 상태 전이 허용 ($\epsilon$-전이) |
| 문자열 매칭 시간 | 매우 빠름: $O(N)$ (문자열 길이 $N$에 비례) | 느림: $O(|S| \cdot N)$ (상태 집합 추적 오버헤드) |
| 공간 메모리 크기 | $O(2^{|S|})$ (NFA를 DFA로 변환 시 상태 수 폭증 가능) | $O(|S|)$ (정규식 길이에 비례하는 작은 크기) |
| 주 활용 분야 | 고속 어휘 분석기(Lex/Flex), 프로토콜 파서 | 정규 표현식 컴파일 초기 모델, 복합 패턴 매칭 |

## Ⅳ. 유한 오토마타(Finite Automata)의 주요 한계점 및 해결 방안

- NFA에서 DFA 변환 시 **상태 폭발** (State Explosion) :
  - 한계점 : 복잡한 패턴을 표현하는 NFA(비결정적 유한 오토마타)를 DFA(결정적 유한 오토마타)로 변환(부분집합 구성법)할 때 상태 수가 최대 $2^n$으로 지수적 증가하여 메모리 고갈.
  - 해결 방안 : **홉크로프트** (Hopcroft) 알고리즘을 활용한 DFA 상태 최소화(Minimization) 적용, 런타임 온더플라이(On-the-Fly) 결정화 기법 도입.
- 문맥 자유 문법(CFG) 및 중첩 구조 표현 불가 :
  - 한계점 : 유한한 메모리(상태)만을 가지므로 괄호 매칭, XML(Extensible Markup Language)/JSON(JavaScript Object Notation) 중첩 태그 등 임의의 깊이를 갖는 문맥 자유 언어를 파싱할 수 없는 태생적 한계.
  - 해결 방안 : 오토마타 모델에 스택 메모리를 추가한 **푸시다운 오토마타** (PDA)로 확장, ANTLR/Bison 등 LALR 파서 제너레이터 활용.
- 정규식 **치명적 백트래킹** (ReDoS) 보안 취약점 :
  - 한계점 : 비효율적인 NFA 백트래킹 엔진을 사용하는 언어 런타임에서 특정 악의적 패턴 매칭 시 CPU(Central Processing Unit) 점유율 100% 지속 및 DoS(Denial of Service) 장애 발생.
  - 해결 방안 : 안전한 선형 시간 보장 정규식 엔진(Google RE2, Rust regex) 채택, 정적 코드 분석을 통한 취약한 정규 표현식 사전 감사.

## Ⅴ. 언어 처리 및 시스템 엔지니어링 관점의 기술사적 제언

- ReDoS(정규식 서비스 거부 공격) 방어 아키텍처 수립 : 악의적인 입력 문자열에 대해 NFA 백트래킹(Backtracking)이 지수함수적 시간($O(2^N)$)을 소비하여 CPU를 고갈시키는 ReDoS 공격을 막기 위해, 선형 시간($O(N)$)을 보장하는 DFA 기반의 정규식 엔진(Google RE2, Rust Regex)을 시스템 표준으로 채택 필수.
- **상태 전이 테이블** (State Transition Table)의 고속 압축 구현 : 컴파일러나 임베디드 통신 제어기 구현 시 2차원 배열 형태의 상태 전이 테이블이 메모리를 과도하게 차지하지 않도록, 행 변위(Row Displacement) 기법을 적용하여 희소 행렬을 1차원 배열로 압축하는 메모리 최적화 기법 적용 권장.
