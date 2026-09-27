---
title: "파이썬(Python)"
category: "02-software-engineering"
tags:
  - "Python"
  - "파이썬"
  - "CPython"
  - "GIL"
  - "동적타이핑"
  - "프로그래밍언어"
date: "2026-09-27T00:24:59+09:00"
author: "Codex"
sidebar:
  badge:
    text: "응용"
extra:
  model: "GPT-6"
  keyword_grade: "응용"
---


## 지식 로드맵 내 현재 위치

소프트웨어 공학 → 소프트웨어 개발·운영 → 파이썬(Python)

## 지식 위치

소프트웨어공학 > 프로그래밍 언어·런타임 > 파이썬

## 30초 인출

- 본질: 파이썬은 동적 객체 모델과 간결한 문법을 갖춘 고급 범용 프로그래밍 언어
- 메커니즘: 소스 코드 → 구현체의 실행 모델에 따른 해석·실행 → 객체 메모리 관리와 라이브러리 활용
- 통찰: 한계: 동적 타입과 패키지 설치 자유도는 실행 전 오류·환경 차이를 남길 수 있음 → 방안: 타입 검사·자동 시험과 의존성 격리를 함께 적용

<details>
<summary>핵심 용어</summary>

- **CPython** : C 언어로 구현된 Python의 대표 구현체로, 소스 코드를 바이트코드로 컴파일한 뒤 인터프리터에서 실행
- **PVM(Python Virtual Machine)** : 바이트코드를 명령어 단위로 해석 실행하는 스택 기반 가상머신
- **GIL(Global Interpreter Lock)** : GIL이 활성화된 CPython 빌드에서 Python 객체 접근을 조정하는 전역 잠금. 기본 빌드는 한 번에 하나의 스레드만 Python 코드를 실행하며, 선택 가능한 free-threaded 빌드는 GIL을 비활성화
- **동적 타이핑(Dynamic Typing)** : 변수의 데이터 타입을 코드 작성 시 선언하지 않고, 프로그램 런타임에 변수에 할당되는 객체의 타입에 따라 동적으로 결정되는 방식
- **참조 카운팅(Reference Counting)** : 객체를 가리키는 포인터 수를 실시간 카운트하여 0이 되는 즉시 메모리를 즉시 해제하는 CPython의 기본 가비지 컬렉션 기법
</details>

---

## 2~4교시 예상문제 (25점)

> 파이썬(Python)의 개념과 목적을 설명하고, 핵심 메커니즘과 구성요소·절차, 적용 시 문제점과 대응 방안을 제시하시오. (25점, 예상)

---

## 2~4교시 25점 답안

## Ⅰ. 파이썬의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 파이썬은 동적 객체 모델과 간결한 문법을 갖춘 고급 범용 프로그래밍 언어 |
| 목적 | 범용 소프트웨어와 자동화 도구의 신속한 개발을 지원 |

## Ⅱ. 파이썬의 특징

| 특징 | 설계·운영상 의미 |
|---|---|
| 동적 객체·타입 모델 | 빠른 표현이 가능하지만 타입 오류가 런타임에 드러날 수 있음 |
| 모듈·패키지 생태계 | 기능 재사용과 의존성 격리를 함께 관리 |
| 구현체별 실행 차이 | CPython의 GIL·free-threaded 빌드 등 환경 조건 확인 |

## Ⅲ. CPython 실행 체계와 코드 실행 프로세스

### CPython 실행 구조와 GIL

```text
Python 소스(.py)
    ↓ 컴파일
바이트코드
    ↓ 실행
CPython 런타임
    ├─ 일반 빌드: GIL 동작
    └─ free-threaded 빌드: GIL 비활성화
```

## Ⅳ. 언어·구현 특징과 Java·C++ 비교

| 구분 | Python | Java | C++ |
|---|---|---|---|
| 타입 | 동적 타입·타입 힌트 | 정적 타입 | 정적 타입 |
| 실행 예 | CPython 바이트코드 | JVM 바이트코드·JIT | 빌드된 기계어 |
| 병렬 처리 | 일반 CPython의 GIL, 별도 free-threaded 빌드 | JVM 스레드 모델 | 언어·라이브러리 동시성 모델 |

### 언어와 대표 구현의 주요 특성

| 구성요소 | 핵심 판단 |
|---|---|
| 객체 모델 | 함수·클래스를 포함한 값이 객체이며, 함수도 인자로 전달 가능 |
| 모듈 | 기능을 파일·패키지 단위로 구성하고 import로 재사용 |
| CPython 실행 | 소스를 바이트코드로 컴파일해 실행, 일반 빌드에서는 GIL 사용 |
| 타입 힌트 | 정적 분석·편집 도구에 타입 정보를 제공, 기본적으로 런타임 타입 강제 없음 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 동적 타입과 패키지 설치 자유도는 실행 전 오류·환경 차이를 남길 수 있음 | 타입 검사·자동 시험과 의존성 격리를 함께 적용 |
| GIL 활성 CPython의 CPU 작업 병렬성 제약 | 프로세스·네이티브 확장·free-threaded 빌드를 검토하고 대상 환경에서 측정 |
| 패키지 버전 충돌·재현 어려움 | 프로젝트 가상환경·잠금 파일로 설치와 실행 재현성 확인 |

## Ⅵ. 제언

대상 업무의 CPU·I/O 병목을 먼저 측정하고 해당 CPython 빌드의 GIL 조건과 타입·의존성 검증 결과를 바탕으로 실행 방식을 선택한다.

---

## 연결 토픽

- [객체지향 프로그래밍(OOP) 4대 특징](./083_oop.md)
- [SOLID 원칙](./082_solid.md)
- [CI/CD 지속적 통합 및 배포](./095_ci_cd.md)
- [알고리즘 복잡도 Big-O](./125_algorithm_complexity_big_o.md)
- [Python 3.14 Thread States and the Global Interpreter Lock](https://docs.python.org/3.14/c-api/threads.html)
- [What's New in Python 3.14: Free-threaded Python](https://docs.python.org/3/whatsnew/3.14.html#free-threaded-python-is-officially-supported)
---

## 출제 이력과 검증 출처

- **출제 상태:** 예상문제는 학습용 문항이며, 공식 기출 원문과 동일하다고 단정하지 않는다.
- [검증 자료 1](https://docs.python.org/3.14/c-api/threads.html)
- [검증 자료 2](https://docs.python.org/3/whatsnew/3.14.html#free-threaded-python-is-officially-supported)
