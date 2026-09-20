---
sidebar:
  order: 114
  label: "114. DB 복제 유형"
title: "DB 복제 유형"
author: "Gemini 3.8 Flash"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-data"
weight: 114
extra:
  model: "Gemini 3.8 Flash"
  question_no: "114"

---

## 답안 골격
```text
[DB 복제 유형 (Replication Types)] ◀━━ 머리: Ⅶ 내 의견 (반동기 복제 기반 RPO 0 달성과 읽기 트래픽의 Read Replica 분산)
 ┃
 ┣━ Ⅰ 개요 ───── 데이터베이스의 고가용성(HA), 부하 분산, 재해 복구를 위해 둘 이상의 DB 노드 간에 데이터를 동기화하는 복제 기술
 ┣━ Ⅱ 특징 ───── 쓰기/읽기 트래픽 분리 · 노드 장애 시 무중단 자동 장애조치(Failover) · 동기화 시점에 따른 성능-정합성 트레이드오프
 ┣━ Ⅲ 구조 ───── 동기화 시점: 동기(Sync) / 비동기(Async) / 반동기(Semi-Sync) ┃ 토폴로지: Master-Slave(Active-Standby) / Multi-Master(Active-Active)
 ┣━ Ⅳ 흐름 ───── ① Primary 노드 트랜잭션 쓰기 및 WAL(Redo Log) 기록 → ② 복제 프로세스가 네트워크로 로그 전송 → ③ Secondary 노드 릴레이 로그 적용 → ④ 동기 방식에 따른 ACK 응답 및 커밋
 ┣━ Ⅴ 비교 ───── 동기 복제 vs 비동기 복제 vs 반동기 복제 (RPO 0/지연 높음 vs 지연 낮음/데이터 유실 위험 vs 최소 1개 노드 복제 보장 절충)
 ┗━ Ⅵ 실무 ───── 비동기 복제 지연(Replication Lag)으로 사용자가 방금 쓴 글을 조회하지 못하는 읽기 일관성 불일치
```
- 필수 키워드: DB 복제 · 동기 복제(Synchronous) · 비동기 복제(Asynchronous) · 반동기 복제(Semi-Sync) · Master-Slave · Multi-Master · 복제 지연(Replication Lag) · Failover
- 기출: 120회 `데이터베이스 복제(Replication)의 동기화 방식(동기, 비동기, 반동기)과 토폴로지 구조를 비교 설명하시오.` → Ⅰ 정의 + Ⅲ 복제 방식 및 토폴로지 + Ⅴ 상세 비교 + Ⅵ 운영 이슈

## 한 줄 본질
- 단일 DB 장애 시 전체 서비스 중단 및 데이터 유실 위험 → 트랜잭션 로그(WAL/바이너리 로그)를 네트워크를 통해 복제 노드에 동기/비동기 전달 → 무중단 가용성과 읽기 확장성 달성 / 복제 지연에 따른 일관성 불일치 발생

## 핵심 그림
```text
[DB 복제 동기화 3대 메커니즘 시퀀스 비교]

  [1. 동기 복제 (Sync)]           [2. 비동기 복제 (Async)]        [3. 반동기 복제 (Semi-Sync)]
  (데이터 유실 0 / 지연 큼)       (빠른 응답 / 장애 시 유실)      (최소 1개 복제 보장 절충)

  Primary       Secondary         Primary       Secondary         Primary       Secondary
     │              │                │              │                │              │
     ├─ 트랜잭션    │                ├─ 트랜잭션    │                ├─ 트랜잭션    │
     ├─ 로그 전송 ─►│                ├─ 커밋 완료!  │                ├─ 로그 전송 ─►│
     │              ├─ 로그 기록     ├─ 로그 전송 ─►│                │              ├─ 릴레이 기록
     │◄── ACK 응답 ─┤                │              ├─ 로그 기록     │◄── ACK 응답 ─┤
     ├─ 최종 커밋   │                │              │                ├─ 최종 커밋   │
     ▼              ▼                ▼              ▼                ▼              ▼
```

## 핵심 용어
- 복제 지연(Replication Lag): Primary에 반영된 트랜잭션이 네트워크 전송 지연 및 Secondary 적용 병목으로 인해 복제본에 뒤늦게 반영되는 시간 차이
- WAL(Write-Ahead Logging): 데이터 파일에 실제 쓰기를 수행하기 전에 변경 이력을 로그 파일에 먼저 영속화하는 데이터베이스의 기본 원리

## 핵심 통찰
- 비동기 복제 환경에서 Primary 노드가 하드웨어 고장으로 급사하면, 복제본으로 넘어가지 못한 최신 데이터는 영원히 유실됨(RPO > 0) → 금융 결제 시스템에서는 비동기 복제를 절대 쓸 수 없음
- 동기 복제를 리전 간(Cross-Region) 장거리 네트워크에 걸면, 네트워크 RTT(왕복 지연)만큼 트랜잭션 커밋이 멈춰 초당 트랜잭션 처리량(TPS)이 1/10 수준으로 곤두박질침
- '반동기 복제(Semi-Sync)'는 여러 복제 노드 중 최소 1개 노드의 메모리/릴레이 로그에 쓰여졌다는 응답만 오면 Primary가 즉시 커밋하므로, 성능 저하를 최소화하면서 RPO=0을 달성하는 현실적 최적해임

## 이웃 토픽과 구분
- DB 복제 vs DB 클러스터링(공유 디스크): 복제 = 각 노드가 독립적인 스토리지(Shared Nothing)를 갖고 로그를 주고받아 동기화 / 공유 디스크 클러스터링(Oracle RAC) = 여러 DB 엔진이 단일 스토리지(SAN)를 물리적으로 공유하여 락을 조율

## 문제·원인·대책
- 적용 상황: 대규모 SNS 커뮤니티의 Master-Slave 읽기 분산 아키텍처
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 사용자가 게시글을 등록하자마자 새로고침하면 글이 보이지 않는 현상 | Primary 쓰기 후 복제본(Slave) 반영 전 읽기 요청이 Slave로 인입(Replication Lag) | 본인이 방금 작성한 쓰기 직후 세션은 5초간 Primary에서 직접 읽도록 라우팅 | 사용자 체감 일관성(Read-your-writes) 100% 보장 |
| 마스터 장애 시 복제 노드로 승격(Failover)하는 과정에서 두 노드가 모두 마스터가 되는 스플릿 브레인(Split-Brain) | 네트워크 단절로 서로를 장애로 오인하여 양쪽 모두 쓰기 수용 | 과반수 투표 기반 합의(Raft/Quorum) 오케스트레이터(Orchestrator) 도입 | 단일 Primary 보장 및 데이터 충돌 방지 |

## 이렇게 출제된다
- 제120회: "고가용성 확보를 위한 데이터베이스 복제(Replication)의 동기화 방식(동기, 비동기, 반동기)을 비교하고, 읽기/쓰기 분리 아키텍처에서 발생하는 복제 지연(Replication Lag)의 해결 방안을 기술하시오." → 요구 포인트: 3대 복제 방식 시퀀스 도식 + 토폴로지 구조 + 지연 문제 원인과 라우팅 대책

## 내 의견
- [수작업 Failover의 다운타임 부채] 마스터 DB가 죽었을 때 당직 엔지니어가 전화를 받고 접속해 수동으로 DNS를 바꾸고 Slave를 승격시키는 체계는 목표 RTO(5분 이내) 달성 불가능 → 나라면: MHA(Master High Availability)나 AWS Aurora Global Database의 자동 장애조치를 구축하고, 평상각 카오스 엔지니어링(Chaos Engineering)을 통해 주기적으로 강제 다운 훈련을 수행하여 무인 자동 절체 신뢰성 확보

## 찾아볼 것
- MySQL의 Group Replication 및 PostgreSQL의 스트리밍 복제에서 지원하는 정족수 기반 Paxos 동기화 기제
