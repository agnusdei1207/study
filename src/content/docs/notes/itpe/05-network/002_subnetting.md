---
title: "서브네팅·슈퍼네팅(CIDR·VLSM)"
author: "OpenAI Codex"
date: "2026-09-20T20:08:10+09:00"
tags:
  - "notes-network"
sidebar: { badge: { text: "A" } }
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"

---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 20:08 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>IP 네트워크</span><span>주소·경로 집계</span><strong>서브네팅·슈퍼네팅</strong></div>

## 큰 그림과 30초 인출

- 본질: IPv4 클래스를 쓰는 기술이 아니라 **prefix 길이**로 주소 경계와 경로 집계를 설계하는 기술
- 메커니즘: 큰 요구부터 경계에 맞춰 분할하고 연속·정렬 Prefix만 다시 집계함
- 산출: 주소 낭비·라우팅 상태를 줄이면서 장애·보안 영역을 계층화함

<div class="itpe-flow itpe-flow--vertical" aria-label="주소 분할과 경로 집계">
  <div class="itpe-flow__node"><strong>IP Prefix</strong><small><b>입력:</b> 주소 블록 · Host 요구량</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>VLSM 분할</strong></span><small><b>활동:</b> 큰 요구부터 Block 경계 정렬</small><small><b>산출:</b> 크기가 다른 Subnet</small></div><div class="itpe-flow__arrow">↓</div>
  <div class="itpe-flow__node"><span class="itpe-keyword"><strong>CIDR 집계</strong></span><small><b>판정:</b> 연속성 · 정렬 · 동일 정책</small><small><b>산출:</b> 요약 경로</small></div>
</div>

<details><summary>핵심 용어</summary>

- `CIDR(Classless Inter-Domain Routing)`: 클래스 경계 대신 Prefix 길이로 주소와 경로를 표현함
- `VLSM(Variable Length Subnet Mask)`: 요구량별로 서로 다른 Prefix 길이를 배정함
- `LPM(Longest Prefix Match)`: 목적지와 가장 길게 일치하는 경로를 선택함
</details>

## 예상문제

> CIDR 기반 서브네팅과 VLSM의 개념 및 설계 절차를 설명하고, 슈퍼네팅과의 차이 및 IPv4·IPv6 주소 설계 시 고려사항을 논하시오. (25점)

## Ⅰ. Prefix로 주소 공간을 설계하는 서브네팅 개요

- 정의: **서브네팅**은 하나의 IP prefix를 더 긴 prefix의 여러 논리 네트워크로 분할하는 기법이며, **VLSM**은 각 네트워크의 요구량에 따라 서로 다른 prefix 길이를 적용하는 기법
- 목적: 주소 공간을 요구량에 맞게 배분하고, broadcast·보안·장애·관리 영역을 분리
- 필요성: Class A/B/C의 고정 경계는 실제 규모와 맞지 않아 주소 낭비와 경로 확장 문제를 유발하므로 CIDR의 classless prefix를 기준으로 설계

#### 한줄 요약

- 서브네팅은 prefix를 늘려 망을 나누고, 슈퍼네팅은 prefix를 줄여 경로를 묶는 주소 계층화 기술임

## Ⅱ. 유연성·계층성·집계성을 제공하는 CIDR/VLSM 특징

| 특징 | 구현 원리 | 효과 | 주의점 |
|---|---|---|---|
| **Classless** | `주소/prefix-length`로 경계 명시 | 요구량별 블록 선택 | 클래스 명칭을 현재 설계 기준으로 사용하지 않음 |
| **가변 길이** | subnet마다 다른 prefix 적용 | 주소 낭비 축소 | 큰 요구부터 정렬·배치 |
| **계층 주소** | 조직·지역·서비스별 상위 prefix 위임 | 책임과 장애영역 분리 | 향후 성장분과 예비 블록 확보 |
| **경로 집계** | 연속·정렬된 prefix를 짧은 prefix로 광고 | RIB(Routing Information Base)·FIB(Forwarding Information Base)·광고량 절감 | 구멍 난 주소와 비연속 블록은 집계 제한 |
| **정책 연계** | Subnet·VLAN(Virtual LAN)·VRF(Virtual Routing and Forwarding)·ACL(Access Control List) 경계 일치 | 보안·운영 단순화 | 주소 구조만으로 보안을 보장하지 않음 |

#### 한줄 요약

- 좋은 주소 설계는 남는 주소가 적은 설계가 아니라 분할·확장·경로 요약이 예측 가능한 설계임

## Ⅲ. Network prefix와 host 영역으로 이루어진 주소 구조

<div class="itpe-flow itpe-flow--vertical" aria-label="IPv4 Prefix 구조"><div class="itpe-flow__node"><strong>IPv4 32 bit</strong><small><b>구성:</b> Network Prefix p bit · Host 32-p bit</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>/26 분할</strong><small><b>산출:</b> 0 · 64 · 128 · 192 경계의 64주소 블록</small></div></div>

| 항목 | 산식·판정 | 의미 |
|---|---|---|
| **총 주소 수** | `2^(32-p)` | prefix `/p`가 포함하는 IPv4 주소 수 |
| **일반 subnet host 수** | `2^h - 2` | network·broadcast 제외, `/31·/32`는 용도별 예외 |
| **block size** | `2^h` | 다음 subnet 경계를 구하는 증가폭 |
| **network 주소** | host bit 전체 0 | subnet 식별 |
| **broadcast 주소** | host bit 전체 1 | IPv4 subnet broadcast |
| **요약 가능 조건** | 연속 블록 + 동일 길이 + 상위 경계 정렬 | 상위 공통 prefix로 집계 가능 |

#### 한줄 요약

- prefix 길이는 주소 경계와 블록 크기를 동시에 결정하며, 이 경계를 라우팅·보안·운영 영역과 맞춰야 함

## Ⅳ. 큰 요구부터 경계에 맞춰 배치하는 VLSM 설계 절차

<div class="itpe-flow itpe-flow--vertical" aria-label="VLSM 설계 절차"><div class="itpe-flow__node"><strong>요구량 정렬</strong><small><b>활동:</b> Host·성장량을 큰 순서로 배열</small><small><b>산출:</b> 배치 우선순위</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>Prefix 계산</strong><small><b>활동:</b> 최소 h와 32-h 선택</small><small><b>산출:</b> Block 크기</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>경계 배치</strong><small><b>활동:</b> 시작점부터 순차 할당</small><small><b>산출:</b> Network·Usable·Broadcast</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>연계 검증</strong><small><b>판정:</b> 중복·누락·요약·정책 일치</small><small><b>산출:</b> 승인된 주소계획</small></div></div>

### 계산 예시: `192.0.2.0/24`, 요구량 100·50·20·10 host

| 배치 | 요구 host | 선택 prefix | 할당 범위 | 사용 가능 범위 | broadcast |
|---:|---:|---:|---|---|---|
| 1 | 100 | `/25` | 192.0.2.0~127 | 192.0.2.1~126 | 192.0.2.127 |
| 2 | 50 | `/26` | 192.0.2.128~191 | 192.0.2.129~190 | 192.0.2.191 |
| 3 | 20 | `/27` | 192.0.2.192~223 | 192.0.2.193~222 | 192.0.2.223 |
| 4 | 10 | `/28` | 192.0.2.224~239 | 192.0.2.225~238 | 192.0.2.239 |

- 잔여: `192.0.2.240/28`, 향후 확장·인프라용으로 예약 가능
- 계산 검증: 모든 시작 주소가 해당 block size 경계에 정렬되고 할당 범위가 겹치지 않아야 함

#### 한줄 요약

- VLSM 계산은 공식 암기보다 큰 요구 우선·경계 정렬·범위 중복 검증의 세 원칙이 핵심임

## Ⅴ. 분할과 집계를 가르는 서브네팅·슈퍼네팅 비교

| 구분 | 서브네팅/VLSM | 슈퍼네팅/Route Aggregation |
|---|---|---|
| **방향** | 큰 prefix → 작은 subnet들 | 작은 prefix들 → 큰 요약 prefix |
| **prefix 변화** | 길어짐 | 짧아짐 |
| **주요 목적** | 주소 배분·broadcast/정책 영역 분리 | 라우팅 정보·광고량 축소 |
| **핵심 조건** | 요구량과 block 경계 | 연속성·동일 크기·정렬 |
| **대표 산출물** | IPAM(IP Address Management) 주소 계획, Subnet·VLAN 표 | 요약경로와 예외경로 |
| **위험** | 단편화·중복 할당 | 과도한 요약에 따른 blackhole |

#### 한줄 요약

- VLSM은 내부 자원을 촘촘히 배분하고, 슈퍼네팅은 외부에 보이는 경로를 단순화함

## Ⅵ. 중복·단편화·오광고를 막는 실무 고려사항

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **주소 중복** | 수기 문서와 실제 DHCP(Dynamic Host Configuration Protocol)·라우터 상태 불일치 | IPAM을 기준정보로 두고 할당 전 중복 검사 | 충돌·우회 경로 예방 |
| **확장 불가** | 현재 host 수에만 맞춘 최소 블록 배정 | 성장률·HA(High Availability)·관리 주소를 포함한 예비 블록 인접 배치 | renumbering 감소 |
| **경로 단편화** | 조직별 비연속 주소 배정 | 지역·서비스 계층별 연속 prefix 위임 | 요약경로 유지 |
| **요약 blackhole** | 하위 경로 장애에도 상위 요약을 계속 광고 | discard 경로·하위 가용성 추적·정책 검증 | 잘못된 전달 범위 제한 |
| **IPv4 관성의 IPv6 적용** | IPv6를 IPv4처럼 host 수 최소화 중심으로 분할 | IPv6 주소정책과 SLAAC(Stateless Address Autoconfiguration)·운영 경계를 기준으로 /64 Subnet 검토 | 표준 기능·운영 일관성 확보 |

#### 한줄 요약

- 주소 설계는 계산표 작성으로 끝나지 않고 IPAM·라우팅·VLAN·ACL·DHCP와 같은 기준정보로 운영되어야 함

## Ⅶ. 주소-경로-정책 추적성으로 완성하는 결론

> 좋은 주소 설계는 빈 주소 수가 아니라 Prefix·경로·정책의 실제 상태가 동일한 Baseline으로 유지되는지로 판정함.

### 학습자 통찰 메모 — 답안 밖
- `[핵심 통찰]`: 주소를 촘촘히 쓰는 것보다 연속성과 성장 여지를 보존해야 경로 집계와 변경 통제가 쉬워진다.
- `나라면`: 변경 전 IPAM에서 경계·중복·요약을 검사하고 배포 후 제어 평면과 전달 평면을 대조하겠다.

### 실전 답안용 기술사적 제언
- 판정: 계획 Prefix와 실제 주소·경로·정책의 일치
- 대안: IPAM을 Baseline으로 주소·VLAN·VRF·DHCP·ACL 연결
- 검증: RIB·FIB·Lease·ACL Hit·도달성 교차 확인
- 효과: 주소 충돌·요약 Blackhole·정책 누락 예방
<div class="itpe-flow itpe-flow--vertical" aria-label="주소 설계 개선"><div class="itpe-flow__node"><strong>분산 관리</strong><small><b>문제:</b> 주소·경로·정책 불일치</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>IPAM Baseline</strong><small><b>대안:</b> Prefix와 운영 객체 연결</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>배포 대조</strong><small><b>판정:</b> 계획·RIB·FIB·정책 일치</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>일관성 확보</strong><small><b>효과:</b> 충돌·Blackhole 예방</small></div></div>

## 1교시 10점 답안 발췌

- 정의: **CIDR(Classless Inter-Domain Routing)** 기반 서브네팅은 Prefix를 늘려 주소 블록을 분할하고, **VLSM(Variable Length Subnet Mask)**은 요구량별 길이를 달리하는 설계임
- 목적: 주소 효율과 장애·보안 영역 분리 → 확장 가능한 계층 주소 확보
<div class="itpe-flow itpe-flow--vertical" aria-label="서브네팅 1교시 그림"><div class="itpe-flow__node"><strong>요구량</strong><small><b>입력:</b> Host·성장량</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>VLSM 분할</strong><small><b>활동:</b> 큰 요구부터 경계 배치</small><small><b>산출:</b> Subnet Prefix</small></div><div class="itpe-flow__arrow">↓</div><div class="itpe-flow__node"><strong>CIDR 집계</strong><small><b>판정:</b> 연속·정렬·동일 정책</small><small><b>산출:</b> 요약 경로</small></div></div>
| 축 | 서브네팅·VLSM | 슈퍼네팅 |
|---|---|---|
| 방향 | Prefix 증가·분할 | Prefix 감소·집계 |
| 목적 | 주소·영역 배정 | 경로 상태 축소 |
| 위험 | 단편화·중복 | Blackhole·과잉 광고 |
- 결론: IPAM Baseline과 RIB·FIB·정책 대조로 주소 계산을 운영 일관성까지 닫음

## 출제 이력과 검증 출처

- 제139회: 공식 문제지 맵에 VLSM 서브네팅 계산형 출제 이력 확인
- [RFC 4632, Classless Inter-domain Routing Address Assignment and Aggregation Plan](https://www.rfc-editor.org/info/rfc4632/)
- [RFC 950, Internet Standard Subnetting Procedure](https://www.rfc-editor.org/info/rfc950/)
- [RFC 4291, IPv6 Addressing Architecture](https://www.rfc-editor.org/info/rfc4291/)
- [RFC 5375, IPv6 Unicast Address Assignment Considerations](https://www.rfc-editor.org/info/rfc5375/)

## 학습 체크

- [ ] `prefix-분할-집계` 큰 그림을 30초 안에 그림
- [ ] 큰 요구부터 prefix와 block size를 계산함
- [ ] network·usable·broadcast·잔여 범위를 표로 검증함
- [ ] VLSM과 슈퍼네팅을 방향·목적·조건으로 비교함
- [ ] Classful 표현을 현재 주소 설계 기준으로 사용하지 않음

## 연결 토픽

- [VLSM](./022_vlsm/) · [슈퍼네팅](./037_supernetting/) · [라우팅 테이블 탐색](./023_routing_table_lookup/) · [NAT](./071_nat/)
