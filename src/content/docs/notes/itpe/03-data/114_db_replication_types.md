---
title: "데이터베이스 복제 유형"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 무중단 가용성과 부하 분산을 위한 데이터베이스 복제 개요

### 가. 데이터베이스 복제(Replication)의 정의
- **데이터베이스 복제** : 하나의 데이터베이스 서버(Primary / Master / Leader)에 저장된 데이터를 네트워크를 통해 연결된 다른 데이터베이스 서버(Secondary / Slave / Follower)로 지속적으로 복사하여 동기화된 사본을 유지하는 기술.
- 데이터 유실 방지(재해 복구), 읽기 전용 트래픽 분산(Scale-Out), 그리고 지리적 분산을 통한 지연 시간 단축을 달성함.

---

## Ⅱ. 데이터베이스 복제의 3대 핵심 분류 체계

### 가. 동기화 시점에 따른 분류: 동기식 vs 비동기식 vs 반동기식

```text
[ 복제 동기화 메커니즘 비교 ]
(A) 동기식 복제 (Synchronous)
    [Primary] ---Write---> [Standby] (ACK 대기) ---> [Client Commit 완료]
    * RPO = 0 (완벽한 데이터 무결성 보장) / 네트워크 지연 시간만큼 쓰기 트랜잭션 대기

(B) 비동기식 복제 (Asynchronous)
    [Primary] ---Write---> [Client Commit 완료]
        | (백그라운드 비동기 복제)
        v
    [Standby]
    * 빠른 응답 시간 / Primary 장애 시 미전송된 데이터 유실 위험 (RPO > 0)

(C) 반동기식 복제 (Semi-Synchronous)
    * N개의 복제본 중 최소 1개 노드로부터 복제 수신(Relay Log 기록) ACK를 받으면 즉시 커밋
```

### 나. 노드 토폴로지 및 권한에 따른 분류

| 복제 토폴로지 | 구조 및 동작 메커니즘 | 장점 | 트레이드오프 및 주의사항 |
| :--- | :--- | :--- | :--- |
| **단일 리더 (Single-Leader / Master-Slave)** | 오직 1개의 마스터 노드만 쓰기(Write)를 전담하고, 슬레이브 노드들은 읽기 전용(Read-Only) 복제본으로 동작 | 충돌(Conflict)이 원천 배제됨, 구현 직관적 | 마스터 노드 장애 시 페일오버 시간(RTO) 소요, 쓰기 스케일아웃 불가 |
| **다중 리더 (Multi-Leader / Active-Active)** | 지리적으로 분산된 복수의 노드가 모두 읽기 및 쓰기를 동시에 처리하며 상호 복제 | 원격 데이터센터 간 쓰기 지연 단축, 마스터 장애 무영향 | 동일 레코드 동시 수정 시 쓰기 충돌(Write Conflict) 해결 필수 |
| **리더리스 (Leaderless / Dynamo 스타일)** | 특정 리더 노드 없이 클라이언트가 여러 복제 노드에 직접 병렬 읽기/쓰기 요청 (Quorum) | 노드 장애에 극도로 강건함, 단일 장애점(SPOF) 부재 | 일관성 수준($W+R > N$) 엄격 관리 필요, 정합성 검증 오버헤드 |

---

## Ⅲ. 복제 데이터 전송 계층에 따른 기술적 구현 방식

### 가. 구문 기반 복제(Statement-Based) vs 행 기반 복제(Row-Based)
- **Statement-Based Replication (SBR)** : Primary에서 실행된 SQL 문장 자체를 바이너리 로그로 전송 $\rightarrow$ 네트워크 대역폭 절감, 단 `NOW()`, `UUID()` 등 비결정론적 함수 실행 시 양 노드 간 데이터 불일치 발생.
- **Row-Based Replication (RBR)** : 실제 디스크에서 변경된 행(Row)의 비트 변화 자체를 전송 $\rightarrow$ 완벽한 데이터 일관성 보장, 대량 갱신(`UPDATE 100만건`) 시 로그 크기 급증.
- **Mixed Replication** : 평상시에는 SBR을 쓰다가 비결정적 함수 사용 시 RBR로 동적 전환.

---

## Ⅳ. 데이터베이스 복제 유형별 주요 한계점 및 해결 방안

- 동기 복제(Synchronous Replication)의 트랜잭션 지연 및 가용성 저하 :
  - 한계점 : 모든 복제본의 쓰기 완료 응답을 대기해야 하므로 네트워크 지연이나 슬레이브 노드 지연 시 마스터 노드의 트랜잭션 처리량 급감 및 행(Hang) 발생.
  - 해결 방안 : 반동기 복제(Semi-synchronous Replication: 최소 1개 노드 ACK 후 커밋) 도입, 정족수(Quorum) 기반 합의 알고리즘(Raft, Paxos) 적용.
- **비동기 복제(Asynchronous Replication)** 시 마스터 장애에 따른 데이터 유실 :
  - 한계점 : 마스터 커밋 후 복제본으로 바이너리 로그가 전송되기 전에 마스터 다운 시 페일오버 과정에서 최신 트랜잭션 유실(RPO > 0).
  - 해결 방안 : 무손실 반동기 복제(Lossless Semi-sync) 활성화, 스토리지 수준의 동기 미러링 또는 클라우드 공유 스토리지(Aurora Storage Engine) 아키텍처 활용.
- 다중 **마스터(Multi-Master)** 복제 환경의 쓰기 충돌 및 스플릿 브레인 :
  - 한계점 : 여러 노드에서 동일 레코드가 동시 갱신될 경우 정합성 충돌 발생, 네트워크 단절 시 양쪽 마스터가 독립 승격되어 데이터 분기 오류 초래.
  - 해결 방안 : 충돌 없는 복제 데이터 타입(CRDT) 적용, 펜싱(Fencing/STONITH) 메커니즘을 통한 과반수 쿼럼 미달 노드의 쓰기 차단.

## Ⅴ. 고신뢰 복제 시스템 운영을 위한 실무 제언

- 복제 지연(**Replication** Lag)에 따른 stale read 방어 : 비동기 복제 환경에서 사용자가 게시글을 작성하고 즉시 조회할 때 복제본 노드로 라우팅되면 방금 쓴 글이 보이지 않는 현상(Read-after-write 위반)이 발생하므로, "자신이 작성한 변경 직후 5초간은 Primary 노드에서 직접 읽도록" 라우터를 제어해야 함.
- **스플릿 브레인(Split-Brain)** 방지를 위한 합의 프로토콜 도입 : 마스터 노드 헬스체크 단절 시 슬레이브가 독자적으로 마스터로 승격하여 2개의 마스터가 쓰기를 받는 대재앙을 방지하기 위해, Raft 또는 Paxos 합의 알고리즘 기반의 오케스트레이터(Orchestrator, Patroni)를 연동할 것을 제언함.
