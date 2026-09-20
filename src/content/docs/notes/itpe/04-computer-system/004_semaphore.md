---
title: "세마포어(Semaphore)"
author: "Codex"
date: "2026-09-20T19:44:16+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 19:44 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>운영체제</span><span>프로세스 동기화</span><strong>세마포어</strong></div>

## 큰 그림과 30초 인출

- 본질: 원자적 카운터와 대기 큐로 공유자원의 동시 사용량과 실행 순서를 통제함
- 메커니즘: **wait(P)**가 허가증을 획득하거나 대기시키고 **signal(V)**가 허가증을 반환하거나 대기자를 깨움
- 산출: Binary는 상호배제·신호, Counting은 동종 자원 N개 제한에 쓰며 대가는 순서 오류·교착·기아 가능성임

<div class="itpe-flow itpe-flow--vertical" aria-label="세마포어 동작 원리">
  <div class="itpe-flow__node"><strong>wait(P)</strong><small><b>입력:</b> 세마포어 S와 자원 요청</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>원자적 획득</strong></span><small><b>판정:</b> 허가증이 있으면 감소·진입, 없으면 대기 큐 이동</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>임계구역·제한 자원</strong><small><b>처리:</b> 허용된 실행 흐름만 공유자원 사용</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>signal(V)</strong><small><b>산출:</b> 허가증 반환 또는 대기자 Wakeup</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- `Semaphore`: 가용 허가증 수와 대기자를 함께 관리하는 동기화 객체 → 소유권보다 수량·신호를 통제
- `wait(P)`: 허가증 획득을 원자적으로 시도 → 부족하면 실행 흐름을 대기 상태로 전환
- `signal(V)`: 허가증을 원자적으로 반환 → 대기자가 있으면 실행 가능 상태로 전환
- `Binary Semaphore`: 값 0·1로 단일 진입 또는 사건 통지 통제
- `Counting Semaphore`: 값 N으로 연결 풀·버퍼 슬롯 같은 동종 자원의 동시 사용량 통제

</details>

## 예상문제

- 세마포어의 개념·구조·동작 원리를 설명하고, 이진·카운팅 세마포어 및 뮤텍스·모니터와 비교한 후 동기화 오류 통제방안을 제시하시오.

## Ⅰ. 원자적 허가증 기반 세마포어 개요

> 세마포어는 단순 정수가 아니라 카운터 변경과 대기·깨움을 분리 불가능하게 묶은 동기화 통제점임.

- 정의: 정수 **카운터**, **대기 큐**, 원자적 **wait(P)·signal(V)** 연산으로 공유자원 접근 수와 실행 순서를 제어하는 동기화 기법
- 목적: **Race Condition(경쟁 상태)** 차단과 한정 자원 동시 사용량 제한 → 공유 상태의 일관성 유지

| 종류 | 값 | 용도 | 주의 |
|---|---:|---|---|
| **Binary** | 0·1 | 상호배제·사건 통지 | 뮤텍스와 달리 소유권 없음 |
| **Counting** | 0 이상 | 풀·슬롯·연결 N개 제한 | 초기값이 가용 자원 수와 일치해야 함 |

## Ⅱ. 카운터·대기 큐와 P/V 동작

> wait와 signal의 원자성이 검사-변경 사이 경쟁을 막고, 대기 정책은 처리량과 공정성의 균형을 결정함.

<div class="itpe-flow itpe-flow--vertical" aria-label="세마포어 처리 절차">
  <div class="itpe-flow__node"><strong>획득 요청</strong><small><b>활동:</b> <span class="itpe-keyword"><strong>wait(P)</strong></span>로 카운터 검사·감소</small><small><b>산출:</b> 진입 허가 또는 Block</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>대기·실행</strong><small><b>활동:</b> 부족 시 대기 큐, 허가 시 임계구역 실행</small><small><b>산출:</b> 제한된 동시 접근</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>반환 요청</strong><small><b>활동:</b> <span class="itpe-keyword"><strong>signal(V)</strong></span>로 카운터 증가 또는 Wakeup</small><small><b>산출:</b> 다음 대기자 실행 가능</small></div>
</div>

- 구현 선택: 대기가 매우 짧으면 Spin, 길면 Block이 유리하므로 임계구역 길이와 Context Switch 비용으로 판단
- 정확성 조건: 카운터 검사·변경, 큐 삽입, Wakeup 결정이 하나의 원자적 연산 의미를 보존해야 함

## Ⅲ. 세마포어·뮤텍스·모니터 비교

> 자원 수 제한은 세마포어, 단일 자원 소유권은 뮤텍스, 복합 공유상태 캡슐화는 모니터가 의도를 가장 잘 드러냄.

| 축 | 세마포어 | 뮤텍스 | 모니터 |
|---|---|---|---|
| 추상화 | 카운터·신호 | 소유권 잠금 | 공유상태·조건변수 캡슐화 |
| 진입 수 | 1 또는 N | 1 | 모니터 진입 1 |
| 소유권 | 없음 | 획득 실행 흐름 | 런타임 통제 |
| 순서 동기화 | 직접 가능 | 조건변수 필요 | 조건변수 내장 |
| 주 용도 | 자원 풀·신호 | 단일 임계구역 | 복합 불변식 |
| 오류 | P/V 순서·누락 | 이중 해제·순서 | 조건 대기 오류 |

## Ⅳ. 교착·기아·우선순위 역전 통제

> 동기화 정확성은 정상 경로보다 예외 경로의 반환, 다중 잠금 순서, 대기자 선택 정책에서 무너짐.

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **교착상태** | 여러 세마포어 획득 순서 불일치 | 전역 순서·Timeout·다중 획득 축소 | 순환대기 차단 |
| 허가증 누수 | 예외 경로의 signal 누락 | Scope Guard·구조적 정리 | 모든 종료 경로 반환 |
| **기아** | 비공정 대기자 선택 | FIFO 큐·대기시간 관측 | 장기 대기 완화 |
| **우선순위 역전** | 저우선순위 보유자의 고우선순위 차단 | 우선순위 상속·상한 | 마감 위반 완화 |
| 과도한 경합 | 큰 임계구역·공유 범위 | Lock 분할·불변 데이터·메시지 전달 | 직렬 구간 축소 |

## Ⅴ. 의도 중심 동기화 설계 결론

> 저수준 P/V를 넓게 노출할수록 검증해야 할 실행 경로가 늘어나므로, 자원 수·소유권·상태 불변식에 맞는 가장 높은 추상화를 선택해야 함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 세마포어의 비소유권은 신호 전달을 가능하게 하지만 잘못된 실행 흐름의 signal도 허용하므로 유연성과 안전성이 맞바뀐다.
- `나라면`: 카운팅 세마포어는 자원 풀 경계 안에 캡슐화하고, 복합 상태는 모니터·채널 등 의도가 드러나는 상위 구조로 전환하겠다.

### 실전 답안용 기술사적 제언

- 판정: 동시 허용량·소유권·복합 상태 중 무엇을 통제하는지로 동기화 원시기법 선택
- 대안: 전역 획득 순서, 구조적 반환, 공정 큐를 동시성 코딩 Baseline으로 적용
- 검증: 부하·예외 주입에서 대기시간, 큐 길이, Timeout, 미반환 허가증을 관측
- 효과: 교착·기아를 줄이고 동기화 의도와 운영 징후를 연결

<div class="itpe-flow itpe-flow--vertical" aria-label="세마포어 사용 개선 흐름">
  <div class="itpe-flow__node"><strong>현행 한계</strong><small><b>문제:</b> P/V 분산과 예외 경로 반환 누락</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>동기화 Baseline</strong><small><b>대안:</b> 획득 순서 · Scope Guard · 공정 큐</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>동시성 검증</strong><small><b>판정:</b> 예외 주입과 장시간 부하에서 교착·기아 부재</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>상위 추상화 전환</strong><small><b>효과:</b> 오류 표면 축소와 유지보수성 향상</small></div>
</div>

## 1교시 10점 답안 발췌

- 정의: 정수 **Semaphore**, **대기 큐**, 원자적 **wait(P)·signal(V)**로 공유자원 접근 수와 실행 순서를 제어하는 동기화 기법
- 목적: **Race Condition** 차단과 동시 사용량 제한 → 공유 상태 일관성 유지

<div class="itpe-flow itpe-flow--vertical" aria-label="세마포어 1교시 동작">
  <div class="itpe-flow__node"><strong>wait(P)</strong><small><b>활동:</b> 허가증 검사·감소</small><small><b>산출:</b> 진입 또는 Block</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>Critical Section</strong><small><b>처리:</b> Binary는 1개, Counting은 N개 진입</small></div>
  <div class="itpe-flow__arrow" aria-hidden="true">↓</div>
  <div class="itpe-flow__node"><strong>signal(V)</strong><small><b>활동:</b> 허가증 반환</small><small><b>산출:</b> 대기자 Wakeup</small></div>
</div>

- 비교: 세마포어는 비소유권·N개 허가증, 뮤텍스는 소유권·단일 잠금, 모니터는 공유상태·조건변수 캡슐화
- 결론: 반환 구조화와 전역 획득 순서로 교착·누수를 통제

## 출제 이력과 검증 출처

- 제139회 정보관리기술사 4교시 2번: 뮤텍스·세마포어·모니터 설명
- [The Open Group Base Specifications Issue 8 — sem_wait](https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_wait.html)
- [The Open Group Base Specifications Issue 8 — sem_post](https://pubs.opengroup.org/onlinepubs/9799919799/functions/sem_post.html)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)

## 학습 체크

- [ ] Ⅰ 개요: 카운터·대기 큐·P/V의 정의와 Binary·Counting의 용도를 구분할 수 있는가?
- [ ] Ⅱ 동작: wait·대기 또는 진입·signal의 활동과 산출을 순서대로 그릴 수 있는가?
- [ ] Ⅲ 비교: 세마포어·뮤텍스·모니터를 추상화·진입 수·소유권·용도로 비교할 수 있는가?
- [ ] Ⅳ 통제: 교착·누수·기아·우선순위 역전의 원인과 대책을 연결할 수 있는가?
- [ ] Ⅴ 제언: 원시기법 선택부터 Baseline·검증·상위 추상화 전환까지 설명할 수 있는가?

## 연결 토픽

- [뮤텍스](./045_mutex/) · [모니터](./015_monitor/) · [교착상태](./038_deadlock/) · [우선순위 역전](./059_priority_inversion/) · [경쟁 상태](./091_race_condition/)
