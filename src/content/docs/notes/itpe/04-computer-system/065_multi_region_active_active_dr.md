---
title: "Multi-Region Active-Active DR"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:40:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기출 · 75%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "137회"
  priority: 75
  priority_note: "[출제:137]"
---

## 답안 골격
```text
[Multi-Region Active-Active DR] ◀━━ 머리: Ⅶ 내 의견 (CRDT 기반 충돌 해소와 글로벌 애니캐스트 라우팅을 결합한 제로 RTO DR 구축)
 ┃
 ┣━ Ⅰ 개요 ───── 단일 리전 재해 시 Active-Standby의 전환 지연 및 유휴 비용 → 복수 리전에서 트래픽을 동시 분산 처리
 ┣━ Ⅱ 특징 ───── RTO ≈ 0, RPO ≈ 0(근접) · 트래픽 부하 분산 · 고비용 인프라 · 데이터 동기화 복잡성
 ┣━ Ⅲ 구조 ───── 글로벌 Anycast DNS/GSLB + 리전별 풀스택 앱 + 분산 데이터베이스(Spanner/CockroachDB)
 ┣━ Ⅳ 흐름 ───── ① 사용자 요청 글로벌 GSLB 인입 → ② 최근접 리전 분기 → ③ 양방향 데이터 복제/합의 → ④ 단일 리전 단절 시 즉각 우회
 ┣━ Ⅴ 비교 ───── Active-Active vs Active-Standby vs Multi-AZ
 ┗━ Ⅵ 실무 ───── 데이터 쓰기 충돌(Conflict) / 빛의 속도 한계(RTT 지연) / Split-Brain 현상
```
- 필수 키워드: Multi-Region · Active-Active · RTO=0 · GSLB · 데이터 동기화 · CRDT · 분산 합의(Paxos/Raft)
- 배점 전략: 10점 = Ⅰ 개요 → Ⅲ 멀티 리전 액티브-액티브 아키텍처 도식 → Ⅴ DR 아키텍처 유형별 비교 / 25점 = Ⅰ~Ⅶ 전개, Ⅳ 트래픽 라우팅 및 데이터 정합성 흐름과 Ⅵ 쓰기 분산(Write Path) 및 네트워크 단절 시 Split-Brain 방지책
- 기출: 137회 3교시 3번 `다중지역 동시 가동방식(Multi-Region Active-Active) 재해복구시스템` 논술형 출제

## 한 줄 본질
- 주 센터와 대기 센터로 나누는 Active-Standby는 재해 시 대기 장비 승격과 DNS 전파에 수십 분이 걸리고 대기 자원이 낭비됨 → 지리적으로 수백 km 떨어진 복수 리전에 상시 가동 시스템을 구축하고 트래픽을 양방향 동시 수용 → 재해 발생 시 전환 시간 없는 제로 RTO 달성 / 리전 간 네트워크 왕복 지연(RTT)과 분산 트랜잭션 동기화 비용 발생

## 핵심 그림
```text
[ Multi-Region Active-Active 라우팅 및 데이터 복제 구조 ]

                         [ 사용자 트래픽 (Global Users) ]
                                        │
                         [ Route 53 / Cloudflare Anycast DNS ]
                          (Latency-based / Geo-Proximity)
                            │                       │
               (50% 트래픽) │                       │ (50% 트래픽)
                            v                       v
     +──────────────────────────────+       +──────────────────────────────+
     | Region A (Seoul)             |       | Region B (Tokyo)             |
     | +──────────────────────────+ |       | +──────────────────────────+ |
     | | Ingress & API Services   | |       | | Ingress & API Services   | |
     | +────────────┬─────────────+ |       | +────────────┬─────────────+ |
     |              ▼               |       |              ▼               |
     | [ Distributed Database A ]  |<─(WAN)─>| [ Distributed Database B ]  |
     +──────────────────────────────+ RTT   +──────────────────────────────+
                                      ~30ms
            (Raft/Paxos 쿼럼 합의 또는 양방향 비동기 복제 + CRDT)
```

## 핵심 용어
- Anycast DNS: 전 세계 여러 데이터센터에 동일한 IP 주소를 광고하고 BGP 라우팅을 통해 사용자와 가장 가까운 리전으로 패킷을 자동 전달하는 기술
- CRDT(Conflict-free Replicated Data Type): 네트워크 단절이나 동시 쓰기 시에도 중앙 잠금 없이 수학적으로 최종 일관성(Eventual Consistency)이 100% 보장되는 특수 분산 자료구조
- Split-Brain(스플릿 브레인): 리전 간 통신망이 단절되었을 때 두 리전이 모두 상대방이 죽었다고 판단하여 각자 마스터로 승격해 데이터 불일치가 회복 불가능하게 찢어지는 현상

## 핵심 통찰
- 완벽한 글로벌 동기(Synchronous) 쓰기는 불가능함 → 빛의 속도 한계로 서울과 도쿄 간 왕복 시간(RTT)은 약 30ms, 미국 동서부는 70ms 이상이 걸리므로, 모든 쓰기에 동기 복제를 걸면 웹 응답 시간이 수백 ms로 치솟아 실서비스가 불가능함
- 따라서 '읽기는 로컬, 쓰기는 분할'하는 전략이 핵심임 → 데이터베이스의 샤드를 지역별로 나누어 한국 사용자 쓰기는 서울 리전 마스터, 일본 사용자 쓰기는 도쿄 리전 마스터가 처리하도록 국소화(Data Locality)해야 함
- 제3의 중립 지역에 쿼럼(Witness) 노드가 필수적임 → 2개 리전만 두면 망 단절 시 50:50이 되어 과반수 투표가 불가능하므로, 미국이나 제3 리전에 가벼운 투표 전용 노드를 두어 Split-Brain을 차단함

## 이웃 토픽과 구분
- Multi-AZ vs Multi-Region: Multi-AZ = 동일 도시 내 수십 km 거리의 데이터센터 간 초저지연(1~2ms) 동기 복제(도시 단위 재해에 취약) / Multi-Region = 수백~수천 km 떨어진 국가/도시 간 재해복구(전쟁, 지진, 광역 전력망 마비 완벽 극복)

## 문제·원인·대책
- 사례: 137회 기출 및 판교 데이터센터 화재로 인한 주요 메신저·금융 서비스 장시간 먹통 사태
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 리전 간 네트워크 단절 시 양쪽 리전에서 동일 데이터 중복 갱신으로 불일치 | 네트워크 분할(Partition) 발생 시 양쪽 리전이 독자적으로 쓰기 수용 | 제3 리전에 Witness 노드 배치 및 Raft 과반수 쿼럼(Quorum) 합의 강제 | 네트워크 고립 리전의 쓰기 자동 차단으로 일관성 보존 |
| 리전 간 동기식 복제로 인한 결제 API 지연 시간 300ms 초과 | WAN 구간 왕복 통신(RTT) 동안 애플리케이션 스레드 대기 | 사용자 ID 기반 리전 샤딩(Data Pinning) 및 비동기 복제 + CRDT 적용 | 로컬 리전 즉시 쓰기(지연 5ms) 및 최종 일관성 자동 수렴 |

## 이렇게 출제된다
- 제137회 3교시 3번: "다중지역 동시 가동방식(Multi-Region Active-Active) 재해복구시스템에 대하여 다음을 설명하시오." → 요구 포인트: Ⅰ Multi-Region Active-Active의 개념 및 필요성 + Ⅲ 트래픽 라우팅 및 분산 DB 구조도 + Ⅵ 데이터 동기화 지연 극복 및 Split-Brain 방지 대책

## 내 의견
- [전체 시스템이 아닌 핵심 티어(Tier 1) 중심의 선별적 Active-Active 구축] 모든 서비스와 배치를 Multi-Region Active-Active로 구축하는 것은 천문학적인 클라우드 트래픽 전송료(Egress 비용)와 복잡도를 초래함 → 나라면: 사용자 인증 및 주문/결제 등 중단 시 치명적인 핵심 20% 도메인만 선별하여 분산 SQL(CockroachDB) 기반 Active-Active로 격상하고, 나머지 80% 업무는 읽기 전용 복제본 기반의 Warm Standby로 구성하는 비용 효율적 하이브리드 DR 표준화

## 찾아볼 것
- 구글 스패너(Spanner)의 TrueTime API(원자시계/GPS 기반)를 이용한 분산 트랜잭션 직렬화 메커니즘
