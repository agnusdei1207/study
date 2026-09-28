---
title: "프로세스 동기화 기법(뮤텍스·세마포어·모니터)"
author: "Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  label: "122. 프로세스 동기화 기법(뮤텍스·세마포어·모니터)"
  order: 122
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

운영체제 → 동시성 제어 → 프로세스 동기화

## 30초 인출

- 본질: 프로세스 동기화는 공유 상태의 동시 변경과 실행 순서를 통제하는 기법
- 메커니즘: 공유 불변식을 기준으로 뮤텍스·세마포어·모니터가 진입과 조건 대기를 원자적으로 조정
- 통찰: 한계: 잠금만 추가하면 교착·기아·조건 오류가 남음 → 방안: 전역 획득 순서와 조건 재검사·예외 반환을 함께 설계한다.

<details>
<summary>핵심 용어</summary>

- **프로세스 동기화(Process Synchronization):** 공유 상태 접근과 실행 순서를 조정해 데이터 불변식을 지키는 기법
- **뮤텍스(Mutex, Mutual Exclusion):** 소유권을 가진 실행 흐름만 해제하는 상호배제 잠금
- **세마포어(Semaphore):** 원자적 wait/signal 연산으로 허가증 수와 대기자를 관리하는 동기화 객체
- **모니터(Monitor):** 공유 데이터와 연산을 캡슐화하고 한 번에 하나의 실행 흐름만 진입하게 하는 동기화 구조
- **조건 변수(Condition Variable):** 조건이 성립할 때까지 잠금을 놓고 대기한 뒤 상태를 다시 확인하도록 돕는 객체
- **경쟁 상태(Race Condition):** 실행 순서에 따라 공유 상태의 결과가 달라지는 오류

</details>

---

## 2~4교시 예상문제 (25점)

> 프로세스 동기화의 목적과 동작 원리를 설명하고, 뮤텍스·세마포어·모니터를 비교하여 동기화 오류 통제방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

### Ⅰ. 프로세스 동기화의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **프로세스 동기화(Process Synchronization):** 공유 상태의 동시 접근과 조건 대기를 조정하는 기법 |
| 목적 | 경쟁 상태를 막고 공유 데이터의 불변식을 보존 |

### Ⅱ. 프로세스 동기화의 특징

| 특징 | 의미 |
|---|---|
| 공유 불변식 보호 | 동시에 변경되면 안 되는 상태의 조건을 유지 |
| 원자적 진입·해제 | 임계구역 접근 권한을 경쟁 없이 획득·반환 |
| 조건 대기 | 자원 수·상태 조건이 충족될 때까지 안전하게 대기 |

### Ⅲ. 임계구역 체계·동작 프로세스

**핵심 동기화 프레임**

```text
동시 실행 흐름 → 공유 불변식·임계구역 식별
               → 진입 제어(뮤텍스/세마포어/모니터)
               → 공유 상태 읽기·변경 → 조건 통지·권한 반환
               → 대기 흐름의 재진입·조건 재검사
```

**하위 메커니즘: 모니터 조건 대기**

```text
잠금 획득 → while 조건 미충족: 잠금 해제하며 대기
          → 신호 수신 후 잠금 재획득 → 조건 다시 확인
          → 상태 변경 → 신호 통지 → 잠금 해제
```

### Ⅳ. 동기화 객체 비교

| 객체 | 핵심 동작 | 적합한 상황 |
|---|---|---|
| 뮤텍스 | 소유 잠금 획득·해제 | 단일 공유 상태의 상호배제 |
| 세마포어 | wait/signal로 허가증 수 관리 | N개 자원 수량·신호 조정 |
| 모니터 | 상태·연산·조건 대기 캡슐화 | 복합 불변식과 조건 대기 |

### Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 잠금 획득 순서가 달라 교착 발생 | 전역 순서·시간 제한·잠금 수 축소 |
| 예외 경로에서 허가증·잠금 반환 누락 | 구조적 반환과 모든 종료 경로 점검 |
| 대기자가 오래 밀려 기아 발생 | 공정성 정책과 대기 시간 관측 |
| 깨어난 뒤 조건이 바뀌어 잘못 실행 | 잠금 안에서 while 조건 재검사 |

### Ⅵ. 제언

저수준 잠금 호출을 여러 코드 경로에 흩어 놓으면 획득 순서와 예외 반환을 검증하기 어렵다. **공유 불변식을 먼저 정의하고 이를 캡슐화하는 동기화 객체를 선택**하며, 전역 획득 순서·조건 재검사·구조적 반환을 코드 검토 기준으로 삼아야 한다.

## 출제 이력과 검증 출처

- 제139회 정보관리기술사 4교시 2번: `운영체제의 프로세스 동기화 기법 중 뮤텍스(Mutex), 세마포어(Semaphore), 모니터(Monitor)에 대하여 설명하시오.`
- [The Open Group Base Specifications Issue 8 — pthread_mutex_lock](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_mutex_lock.html)
- [The Open Group Base Specifications Issue 8 — pthread_cond_wait](https://pubs.opengroup.org/onlinepubs/9799919799/functions/pthread_cond_wait.html)
- [The Open Group Base Specifications Issue 8 — sem_wait](https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_wait.html)
- [The Open Group Base Specifications Issue 8 — sem_post](https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_post.html)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 연결 토픽

- [교착상태](./038_deadlock/) · [우선순위 역전](./059_priority_inversion/) · [경쟁 상태](./091_race_condition/) · [IPC](./034_ipc/)
