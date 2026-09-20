---
title: "스레드(Thread)"
author: "Codex"
date: "2026-09-20T20:09:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"

---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 20:09 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>운영체제</span><span>실행 단위</span><strong>스레드</strong></div>

## 큰 그림과 30초 인출

```text
┌────────────── Process Address Space ──────────────┐
│ 공유: Code │ Data │ Heap │ Open Files            │
│                                                  │
│ Thread A      Thread B       Thread C             │
│ TID·PC·Reg    TID·PC·Reg     TID·PC·Reg          │
│ Stack·TLS     Stack·TLS      Stack·TLS           │
└──────────────────────┬────────────────────────────┘
                       ▼
             Scheduler / Kernel Threads
```

```text
Thread = 프로세스 안의 단일 제어 흐름
공유 = Code·Data·Heap·File / 독립 = ID·PC·Register·Stack·TLS
장점 = 낮은 통신 비용·병렬성 / 위험 = Race·Deadlock·격리 약화
통제 = Mutex·Semaphore·Condition·Atomic·Thread Pool
```

## 예상문제

> 스레드의 개념과 메모리 구조 및 상태 전이를 설명하고 프로세스와 비교한 후, 멀티스레드 구현의 고려사항을 제시하시오.

## Ⅰ. 개요 ───── 정의·필요성

스레드는 POSIX 관점에서 **프로세스 내부의 단일 제어 흐름**이며, 같은 프로세스의 다른 스레드와 주소 가능한 메모리를 공유하면서 독립적인 실행 문맥을 갖는다.

| 필요성 | 효과 | 위험 |
|---|---|---|
| 동시 요청 처리 | 응답성·처리량 향상 가능 | 공유 상태 경합 |
| 멀티코어 활용 | 병렬 실행 가능 | 동기화·스케줄 비용 |
| 주소 공간 공유 | 통신·복사 감소 | 장애 격리 약화 |

## Ⅱ. 특징 ───── 공유 자원과 독립 문맥

| 구분 | 스레드 간 공유 | 스레드별 독립 |
|---|---|---|
| 메모리·자원 | Code, Global/Data, Heap, Open File | Stack, TLS |
| 실행 문맥 | 프로세스 자원 한계·주소 공간 | Thread ID, PC, Register, Scheduling 속성 |
| 결과 | 빠른 데이터 교환 | 독립 호출 흐름·재진입 |

공유 여부의 상세 범위는 OS와 런타임 구현에 좌우되므로 TCB 필드나 스택 크기를 보편적 고정값으로 단정하지 않는다.

## Ⅲ. 구조 ───── 사용자·커널 매핑과 TCB

```text
User Threads       Runtime/Library       Kernel Threads       CPU
 U1 ─┐                                  K1 ────────────────> Core0
 U2 ─┼── 1:1 / M:N Mapping ──────────── K2 ────────────────> Core1
 U3 ─┘                                  K3 ────────────────> Run Queue

TCB: TID·State·PC·Registers·Stack Pointer·Scheduling Info·TLS Reference
```

| 모델 | 구조 | 장점 | 제약 |
|---|---|---|---|
| 사용자 수준 | 라이브러리가 스케줄 | 빠른 사용자 전환 가능 | 블로킹·코어 활용 제약 가능 |
| 커널 수준 | 커널이 개별 스케줄 | 멀티코어·블로킹 처리 | 커널 전환·관리 비용 |
| 혼합 M:N | 다수 사용자를 다수 커널에 매핑 | 유연한 병렬성 | 런타임 복잡성 |

## Ⅳ. 동작 ───── 생명주기·문맥 교환

```text
             preempt/yield
 [Running] ───────────────> [Ready]
     │                         ▲
 I/O │wait                     │ dispatch
     ▼                         │
 [Blocked] ─── event/signal ───┘
     │
     └── exit/cancel ──> [Terminated]
```

문맥 교환 시 현재 스레드의 실행 문맥을 저장하고 다음 스레드의 문맥을 복원한다. 같은 프로세스라고 해서 캐시·TLB 비용이 항상 사라지는 것은 아니다.

## Ⅴ. 비교 ───── 프로세스·스레드

| 구분 | 프로세스 | 스레드 |
|---|---|---|
| 주소 공간 | 원칙적으로 분리 | 프로세스 내 공유 |
| 통신 | IPC 필요 | 공유 메모리 직접 접근 |
| 생성·전환 | 상대적으로 큰 자원 문맥 | 상대적으로 작은 실행 문맥 |
| 장애 영향 | 격리 경계가 큼 | 프로세스 전체에 전파 가능 |
| 동기화 | IPC·공유 메모리 통제 | Race·Visibility 통제 필수 |
| 선택 | 격리·보안·독립 배포 | 밀결합 동시 작업 |

## Ⅵ. 고려 ───── 안전성·성능·운영 검증

| 문제 | 원인 | 대응 | 검증 |
|---|---|---|---|
| Race Condition | 무동기 공유 쓰기 | Mutex·Atomic·불변 데이터 | 경쟁 탐지·부하 시험 |
| Deadlock | 순환 대기·잠금 순서 불일치 | 잠금 순서, Timeout, 구조 축소 | 교착 탐지·덤프 |
| 가시성 오류 | 캐시·컴파일러 재배치 | 언어 메모리 모델·동기화 준수 | 반복·약한 메모리 시험 |
| 과다 스레드 | 요청당 생성·블로킹 | Pool, Queue, Backpressure | Queue·문맥 교환·지연 |
| False Sharing | 동일 캐시라인 갱신 | 데이터 배치·패딩 검토 | 캐시 미스·확장성 |
| 안전하지 않은 종료 | 취소 중 잠금·자원 보유 | 협력적 취소, Cleanup, Join | 누수·일관성 시험 |

## Ⅶ. 결론 ───── 공유 최소화와 구조적 동시성

스레드는 낮은 통신 비용으로 멀티코어를 활용하지만 공유 주소 공간이 곧 위험 경계다. **공유 상태 최소화, 명시적 소유권, 제한된 동시성, 취소·종료까지 포함한 생명주기 관리**가 성능보다 먼저 설계돼야 한다.

## 1교시 10점 발췌

```text
스레드는 프로세스 내부의 단일 제어 흐름이다.
공유: Code·Data·Heap·Open File
독립: TID·PC·Register·Stack·TLS

상태: Ready ⇄ Running ⇄ Blocked → Terminated
통제: Mutex·Atomic·Condition·Pool·Backpressure·Join
```

## 공식 검증 출처

- [The Open Group POSIX Definitions — Thread·Thread-Safe](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap03.html)
- [The Open Group pthread.h](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/pthread.h.html)

## 답안 체크

- [ ] 공유 영역과 독립 영역을 한 그림에 배치했는가
- [ ] 상태 전이와 문맥 교환을 구분했는가
- [ ] Race·Deadlock·가시성·과다 스레드 대응을 썼는가
- [ ] 확인되지 않은 140회 기출 표기를 제거했는가

## 연결 토픽

- [컴퓨터 시스템 과목 지도](./)
- [가상화](./008_virtualization/)
- [NPU](./007_npu/)
