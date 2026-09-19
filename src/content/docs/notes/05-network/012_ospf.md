---
title: "OSPF(Open Shortest Path First)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기출 · 86%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "124회, 134회"
  priority: 86
  priority_note: "[출제:134] · [출제(KPC):124]"
---

## 답안 골격
```text
[OSPF] ◀━━ 머리: Ⅶ 내 의견 (Area 계층 분할 및 BFD 결합 서브세컨드 고속 수렴망 구현)
 ┃
 ┣━ Ⅰ 개요 ───── 거리벡터(RIP)의 홉수 한계(15홉)·느린 수렴 → 링크 상태(Link State) 개방형 표준
 ┣━ Ⅱ 특징 ───── 다익스트라(SPF) 최단경로, 빠른 수렴, 루프 프리, 계층적 Area 구조, VLSM/CIDR
 ┣━ Ⅲ 구조 ───── Area 0(백본) + 일반 Area + 라우터 역할(DR/BDR, ABR, ASBR) + LSDB
 ┣━ Ⅳ 흐름 ───── ① Hello 패킷 네이버 수립 → ② LSA 플러딩으로 LSDB 동기화 → ③ SPF 알고리즘 경로 산출
 ┣━ Ⅴ 비교 ───── RIP vs OSPF (거리벡터 vs 링크상태, 홉수 vs 대역폭 비용, 브로드캐스트 vs 멀티캐스트)
 ┗━ Ⅵ 실무 ───── 링크 플래핑 시 SPF 연산 폭증 / 대규모 단일 Area 메모리 고갈 / 가상 링크 구성
```
- 필수 키워드: 링크 상태(Link State) · 다익스트라 SPF · Area 0(백본) · DR/BDR · ABR · ASBR · LSA
- 배점 전략: 10점 = Ⅰ → Ⅲ 계층적 Area 아키텍처 도식 → Ⅴ RIP vs OSPF 비교표 / 25점 = Ⅰ~Ⅶ, LSA 패킷 유형(1~5)과 134회 비교 문제 상세 전개
- 기출: 124회 `OSPF 동작 원리 및 Area 구조` → Ⅲ·Ⅳ, 134회 1교시 8번 `RIP와 OSPF 비교` → Ⅴ

## 한 줄 본질
- 거리벡터 방식(RIP)의 홉 수 제한(최대 15)과 느린 수렴으로 인한 라우팅 루프 발생 → 라우터가 링크 상태를 공유해 전체 네트워크 지도를 그리고 다익스트라(SPF) 알고리즘으로 최단 경로를 직접 계산 → 즉각적인 수렴과 최적 경로 보장 / 전체 토폴로지 데이터베이스(LSDB) 유지에 따른 라우터 연산 부하 발생

## 핵심 그림
```text
[ OSPF 계층적 Area 구조 및 라우터 역할 ]

       +------------------ External AS (BGP/RIP) ------------------+
                                  |
                                [ASBR] (AS 경계 라우터)
                                  |
      +------------------------ Area 0 (Backbone) ---------------------+
      |   [Internal Router] <--- DR / BDR 선출 (멀티캐스트 224.0.0.5/6) |
      +-------------------+--------------------+-----------------------+
                          |                    |
                        [ABR]                [ABR] (Area 경계 라우터)
                          |                    |
        +-----------------+---+            +---+-----------------+
        |       Area 1        |            |       Area 2        |
        |  [Internal Router]  |            |  [Internal Router]  |
        +---------------------+            +---------------------+
```

## 핵심 용어
- DR/BDR(Designated Router / Backup DR): 브로드캐스트 네트워크에서 라우터 간 LSA 교환 연결 수($N(N-1)/2$)를 줄이기 위해 선출되는 대표 및 예비 라우터
- ABR(Area Border Router): 백본 Area 0과 하나 이상의 일반 Area 사이에 걸쳐 있어 Area 간 라우팅 정보를 요약 전달하는 라우터
- ASBR(Autonomous System Boundary Router): OSPF 영역 바깥의 다른 라우팅 프로토콜(BGP, EIGRP, RIP)이나 정적 경로를 OSPF 내부로 재분배(Redistribute)하는 라우터

## 핵심 통찰
- OSPF는 "이웃 라우터의 주장(거리)"을 믿고 표를 갱신하는 것이 아니라, 모든 라우터가 "전체 지도(LSDB)"를 똑같이 공유한 뒤 각자 독립적으로 길을 찾음 → 원리상 라우팅 루프가 원천 차단
- 비용(Cost) 기준이 단순 홉 수가 아니라 인터페이스 대역폭($10^8/\text{대역폭}$)이므로, 100Mbps 1홉보다 1Gbps 2홉 경로를 더 빠른 최단 경로로 올바르게 선택
- 단일 망에 라우터가 수백 대 이상 늘어나면 한 링크만 흔들려도(Flapping) 전 라우터가 일제히 SPF 연산을 재수행하여 CPU 폭주 → 반드시 Area를 분할해 LSA 전파 범위를 격리

## 이웃 토픽과 구분
- RIP vs OSPF: RIP는 홉 수만 따지는 단순 거리벡터(최대 15홉, 주기적 전체 전송) / OSPF는 대역폭을 고려하는 링크상태(홉 제한 없음, 상태 변화 시 증분 LSA 전파)

## 문제·원인·대책
- 적용 상황: 대규모 엔터프라이즈 백본망에서 인터페이스 순시 장애 시 라우터 CPU 100% 포화
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 특정 케이블 접촉 불량 시 전 라우터 SPF 연산 반복 | 단일 Flat Area 구성으로 LSA 플래핑이 전사 라우터로 전파 | Area 계층 분할 및 Stub/Totally Stubby Area 적용 | LSA 전파를 Area 내로 차단하고 외부 경로는 기본 경로(0.0.0.0)로 대체 |
| 라우터 장애 감지 및 페일오버 지연(최대 수십 초) | OSPF Hello 타이머(기본 10초) 및 Dead 타이머(40초) 대기 | BFD(Bidirectional Forwarding Detection) 연동 | 50ms 미만의 하드웨어 기반 장애 감지 및 즉시 경로 재수렴 |

## 이렇게 출제된다
- 제124회 2교시: "OSPF의 기본 개념, Area 구조의 필요성, 라우터 유형 및 LSA 패킷 종류를 설명하시오." → 요구 포인트: Ⅲ 계층 다이어그램 + LSA Type 1~5 표
- 제134회 1교시 8번: "RIP(Routing Information Protocol)와 OSPF(Open Shortest Path First) 비교" → 요구 포인트: 알고리즘, 메트릭, 수렴속도, 확장성, 패킷 전달 방식 비교표

## 내 의견
- [Area 0 백본 비연속성 위험] 무분별한 네트워크 증설로 인해 물리적으로 Area 0에 직접 닿지 못하는 고립 Area 발생 시 라우팅 단절 사고 빈발 → 나라면: 초기 설계 단계에서 모든 일반 Area가 물리적으로 Area 0과 2개 이상의 ABR로 이중화되도록 토폴로지 규칙을 강제하고, 불가피한 임시 확장 구간에는 Virtual-Link 설정을 제한적으로 사용하며 조기 물리 회선 직결 추진

## 찾아볼 것
- OSPFv3(IPv6 지원)의 LSA 변경점과 LDP/SR(세그먼트 라우팅)과의 확장 연동 규격
