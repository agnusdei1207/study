---
title: "서브네팅·슈퍼네팅(CIDR·VLSM)"
author: "OpenAI Codex"
date: "2026-09-20T21:28:00+09:00"
tags:
  - "notes-network"
sidebar: { badge: { text: "A" } }
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"

---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 21:28 KST</p>

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
| **경로 집계** | 연속·정렬된 prefix를 짧은 prefix로 광고 | RIB/FIB·광고량 절감 | 구멍 난 주소와 비연속 블록은 집계 제한 |
| **정책 연계** | subnet/VLAN/VRF/ACL 경계 일치 | 보안·운영 단순화 | 주소 구조만으로 보안을 보장하지 않음 |

#### 한줄 요약

- 좋은 주소 설계는 남는 주소가 적은 설계가 아니라 분할·확장·경로 요약이 예측 가능한 설계임

## Ⅲ. Network prefix와 host 영역으로 이루어진 주소 구조

```text
IPv4 32 bit
┌──────────────────────────────┬──────────────────┐
│ Network/Subnet Prefix        │ Host bits        │
│ 왼쪽부터 p bit               │ 32-p bit         │
└──────────────────────────────┴──────────────────┘
              /p

예: 192.0.2.0/24를 /26으로 분할
192.0.2.0/26   192.0.2.64/26   192.0.2.128/26   192.0.2.192/26
     64주소          64주소           64주소            64주소
```

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

```text
① 요구 host·망 수·성장률 조사
          ↓
② host 요구량을 큰 순서로 정렬
          ↓
③ 2^h-2 ≥ 요구량인 최소 h 선택
          ↓
④ prefix = 32-h, block = 2^h 계산
          ↓
⑤ 상위 블록 시작점부터 경계 정렬·순차 배치
          ↓
⑥ network/usable/broadcast·gateway·예비 범위 기록
          ↓
⑦ 중복·누락·요약경로·ACL/DHCP 연계 검증
```

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
| **대표 산출물** | IPAM 주소 계획, subnet/VLAN 표 | 요약경로와 예외경로 |
| **위험** | 단편화·중복 할당 | 과도한 요약에 따른 blackhole |

#### 한줄 요약

- VLSM은 내부 자원을 촘촘히 배분하고, 슈퍼네팅은 외부에 보이는 경로를 단순화함

## Ⅵ. 중복·단편화·오광고를 막는 실무 고려사항

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **주소 중복** | 수기 문서와 실제 DHCP·라우터 상태 불일치 | IPAM을 기준정보로 두고 할당 전 중복 검사 | 충돌·우회 경로 예방 |
| **확장 불가** | 현재 host 수에만 맞춘 최소 블록 배정 | 성장률·HA·관리 주소를 포함한 예비 블록 인접 배치 | renumbering 감소 |
| **경로 단편화** | 조직별 비연속 주소 배정 | 지역·서비스 계층별 연속 prefix 위임 | 요약경로 유지 |
| **요약 blackhole** | 하위 경로 장애에도 상위 요약을 계속 광고 | discard 경로·하위 가용성 추적·정책 검증 | 잘못된 전달 범위 제한 |
| **IPv4 관성의 IPv6 적용** | IPv6를 IPv4처럼 host 수 최소화 중심으로 분할 | IPv6 주소정책과 SLAAC·운영 경계를 기준으로 /64 subnet 검토 | 표준 기능·운영 일관성 확보 |

#### 한줄 요약

- 주소 설계는 계산표 작성으로 끝나지 않고 IPAM·라우팅·VLAN·ACL·DHCP와 같은 기준정보로 운영되어야 함

## Ⅶ. 주소-경로-정책 추적성으로 완성하는 결론

- **[prefix를 운영 기준선으로 관리]**: 주소만 분할하고 라우팅·보안 정책이 따로 움직이면 장애 분석과 변경 통제가 어려우므로 prefix별 소유자, 용도, 위치, VLAN/VRF, gateway, DHCP, ACL, 요약경로를 연결
- 나라면: 변경 전 IPAM에서 중복·경계·요약 가능성을 검사하고, 배포 후 RIB/FIB·DHCP lease·ACL hit·도달성 결과를 대조하여 계획과 실제 상태의 일치 여부 확인

#### 한줄 요약

- 좋은 서브네팅은 빈 주소를 줄이는 계산이 아니라 주소·경로·정책의 일관성을 지속 검증하는 운영 설계임

## 1교시 10점 답안 발췌

### 1. 정의와 관계

```text
CIDR prefix
 ├─ 길게: 서브네팅/VLSM = 요구량별 분할
 └─ 짧게: 슈퍼네팅     = 연속 경로 집계
```

### 2. VLSM 절차

| 순서 | 핵심 |
|---:|---|
| 1 | host 요구량 내림차순 정렬 |
| 2 | `2^h-2` 기준 최소 h와 `/32-h` 선택 |
| 3 | block 경계에 맞춰 순차 배치 |
| 4 | network·usable·broadcast·잔여 범위 검증 |

### 3. 차별화 제언

- Classful 주소는 역사적 배경으로만 설명하고 실제 설계는 CIDR/VLSM·IPv6 prefix로 수행
- IPAM을 기준으로 주소·VLAN/VRF·DHCP·ACL·요약경로를 추적하여 중복과 blackhole 방지

## 출제 이력과 검증 출처

- 제139회: 공식 문제지 맵에 VLSM 서브네팅 계산형 출제 이력 확인
- 제130회: KPC 컴시응 대응 이력
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
