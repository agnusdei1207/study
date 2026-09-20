---
title: "액티브-액티브 이중화와 스토리지 DR"
author: "Codex"
date: "2026-09-20T22:22:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 재해복구·서비스 연속성을 거쳐 액티브-액티브 이중화와 스토리지 DR로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>재해복구·서비스 연속성</span>
  <strong>액티브-액티브 이중화와 스토리지 DR</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **액티브-액티브(Active-Active) 이중화**와 **스토리지 DR(Disaster Recovery)**은 2개 이상의 독립 데이터센터가 워크로드를 동시 분산 처리하며 한 거점 소실 시에도 **RTO≈0**, **RPO=0**을 보장하는 고가용 재해복구 아키텍처
- 메커니즘: **GSLB(Global Server Load Balancing)** 트래픽 분산 → 스토리지 블록 단위 동기 미러링 → 제3 거점 **Quorum Witness** 스플릿 브레인 방지 → 무중단 자동 절체
- 산출: 다중 거점 무중단 인프라 · 실시간 정합성 보증 가상 볼륨 · **N-1** 용량 보장 체계

<div class="itpe-flow-map" role="img" aria-label="트래픽 분산에서 스토리지 동기 복제 및 쿼럼 중재로 이어지는 액티브-액티브 흐름">
  <div class="itpe-flow-node">
    <strong>글로벌 트래픽 유입</strong>
    <small>대국민 서비스 · 대규모 금융 결제 트랜잭션</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>GSLB 트래픽 분산</strong>
    <small><span class="itpe-keyword"><strong>GSLB</strong></span> 헬스체크 및 RTT 기반 근접 라우팅</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>액티브-액티브 다중 거점</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>제1 센터</strong><span>서버 가동 및 스토리지 Primary 볼륨</span></div>
      <div class="itpe-flow-branch"><strong>제2 센터</strong><span>서버 동시 가동 및 스토리지 Active 볼륨</span></div>
      <div class="itpe-flow-branch"><strong>동기 복제</strong><span>양방향 광채널 ISL 기반 무손실 미러링</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>제3 거점 Quorum 중재</strong>
    <small><span class="itpe-keyword"><strong>Split-Brain</strong></span> 방지 · 다수결 기반 I/O 펜싱 통제</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Active-Active**: 복수 센터의 서버와 스토리지가 동시에 실제 트래픽을 분산 처리하는 상시 가동 구성
- **스토리지 DR(Disaster Recovery)**: 재해 발생 시 데이터 유실 없이 서비스를 지속하기 위해 원격지에 스토리지를 복제·대체 운용하는 체계
- **GSLB(Global Server Load Balancing)**: DNS 쿼리 단계에서 서버 헬스체크 및 지연시간을 측정하여 최적 거점으로 트래픽을 분산
- **동기 복제(Synchronous Replication)**: 로컬과 원격 스토리지 모두에 쓰기 완료를 확인한 후 호스트에 응답하여 RPO=0을 달성하는 기법
- **비동기 복제(Asynchronous Replication)**: 로컬 스토리지 완료 즉시 응답 후 원격지로 백그라운드 전송하여 원거리 지연을 방어하는 기법
- **Split-Brain**: 센터 간 네트워크 단절 시 양 센터가 상호 다운으로 오판하여 독자 쓰기를 수행하며 데이터가 분열되는 현상
- **Quorum Witness**: 네트워크 단절 시 양 센터 중 어느 센터가 쓰기를 지속할지 판정하는 제3 거점 독립 중재자
- **N-1 용량 설계**: 한 센터 상실 시 잔여 센터 하나가 전체 트래픽을 감당할 수 있도록 평시 부하를 50% 이하로 통제하는 설계 원칙

</details>

## 예상문제

> 국가 행정망 장애 및 데이터센터 화재를 계기로 부각된 다중 거점 기반 액티브-액티브(Active-Active) 데이터센터 및 스토리지 DR의 구성 메커니즘을 설명하고, 동기/비동기 복제 방식의 특징과 스플릿 브레인(Split-Brain) 방지 대책을 논하시오. (25점)

## Ⅰ. 무중단 서비스 연속성을 위한 액티브-액티브 스토리지 DR의 개요

> 기존 Active-Standby의 기동 지연과 유휴 낭비를 극복하며, 성패는 단순 장비 증설이 아닌 **동기 복제 레이턴시 제어**와 **Quorum 무결성**으로 판정함.

- 정의: 2개 이상의 독립 데이터센터에 서버와 스토리지를 상시 가동하여 트래픽을 동시 분산 처리하고, 재해 시 즉시 워크로드를 승계하는 **무중단 재해복구(DR) 아키텍처**
- 목적: 서비스 중단 시간을 최소화하는 **RTO≈0** 및 데이터 유실 없는 **RPO=0** 동시 달성 → 비즈니스 연속성 보장

## Ⅱ. 액티브-액티브 스토리지 DR 구성체계 및 복제 메커니즘

> 트래픽 제어부터 스토리지 블록 미러링과 쿼럼 중재까지 계층별 파이프라인으로 연결해야 무손실 자동 절체가 완성됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="액티브-액티브 스토리지 DR 구성체계 및 단계별 활동과 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 트래픽 감지 및 분산</strong></span>
    <small>GSLB 헬스체크 · Anycast 라우팅 기반 다중 거점 부하분산<br />→ DNS 트래픽 분산 정책서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 애플리케이션 무상태 처리</strong></span>
    <small>분산 세션 클러스터링 및 MSA 컨테이너 분산 가동<br />→ 무상태(Stateless) 아키텍처 설계서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 스토리지 블록 동기 미러링</strong></span>
    <small>전용 광채널(ISL) 기반 양방향 쓰기 복제 및 캐시 동기화<br />→ 스토리지 동기 복제 구성도</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 제3 거점 쿼럼 상태 감시</strong></span>
    <small>하트비트 신호 모니터링 및 센터 간 네트워크 단절 감지<br />→ Quorum Witness 감시 로그</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 장애 판정 및 I/O 펜싱</strong></span>
    <small>단절 센터 쓰기 즉시 차단 및 정상 센터 단독 마스터 승격<br />→ 자동 절체(Failover) 결과서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · GSLB 헬스체크 ↔ 스토리지 동기 복제 ↔ Quorum 중재 ↔ 무중단 서비스 양방향 연계</div>

## Ⅲ. 스토리지 복제 방식(동기식 vs 비동기식) 비교

> 근거리는 동기 복제로 RPO=0을 달성하고, 장거리는 비동기 복제로 트랜잭션 지연을 방어해야 함.

| 비교 기준 | 동기식 복제 (Synchronous) | 비동기식 복제 (Asynchronous) |
|---|---|---|
| **동작 메커니즘** | 양쪽 스토리지에 모두 쓰기가 완료된 후 호스트에 응답 | 로컬 스토리지에 쓴 뒤 즉시 응답하고 원격지 백그라운드 전송 |
| **데이터 손실** | **RPO = 0** (완전 무손실 보장) | **RPO > 0** (전송 지연 버퍼만큼 미세 유실 가능) |
| **거리 한계** | 광케이블 지연(RTT)으로 인해 **통상 수십 km 이내** 권장 | 거리 제약 없음 (광역 및 대륙 간 DR 구축 가능) |
| **트랜잭션 영향** | 네트워크 왕복 시간(RTT)이 호스트 응답시간에 직접 누적 | 호스트 애플리케이션 쓰기 성능에 영향 없음 |
| **주 적용 분야** | 계정계 금융 거래, 핵심 결제, 최상위 1등급 행정 | 정보계 분석, 빅데이터 저장소, 원거리 재해복구 백업 |

## Ⅳ. 액티브-액티브(Active-Active) vs 액티브-스탠바이(Active-Standby) 비교

> Active-Active는 높은 복잡도와 구축 비용을 감수하고 절대적인 무중단(RTO≈0)을 실현하는 구조임.

| 비교 기준 | 액티브-액티브 (Active-Active) | 액티브-스탠바이 (Active-Standby) |
|---|---|---|
| **평시 운영 상태** | 양 센터 모두 실제 워크로드 동시 분산 처리 | 주 센터만 운영, 대기 센터는 유휴 상태 대기 |
| **목표 복구 시간** | **RTO ≈ 0** (트래픽 재라우팅만으로 수 초 내 전환) | **RTO 수십 분 ~ 수 시간** (대기계 기동 및 DB 승격 필요) |
| **목표 복구 시점** | **RPO = 0** (동기 복제 기반 무손실 달성) | **RPO 수 분 ~ 수 시간** (비동기 복제 및 백업 주기에 의존) |
| **자원 활용률** | 투자된 인프라 자원을 100% 상시 활용 | 대기 센터 자원이 유휴화되어 TCO 효율 저하 |
| **기술 복잡도** | **Split-Brain**, 세션 동기화, 분산 락 고도화 필요 | 단순 단방향 복제로 아키텍처가 상대적으로 단순함 |
| **전환 리스크** | 자동 절체로 인적 개입 최소화 및 신속 대응 | 수동 절체 매뉴얼 오류, DB 기동 실패 위험 존재 |

## Ⅴ. 실무 아키텍처 실패 모드와 공학적 해결 방안

> 분산 환경에서 발생하는 네트워크 단절과 용량 초과는 연쇄 장애의 주원인이므로 사전 통제가 필수적임.

| 실패 모드 | 발생 원인 | 공학적 해결 대책 | 기대 효과 |
|---|---|---|---|
| **스플릿 브레인(Split-Brain)** | 센터 간 네트워크 단절 시 양 센터가 독립 마스터로 승격 | 제3 거점 독립 **Quorum Witness** 배치 및 다수결 I/O 펜싱 | 양방향 동시 쓰기로 인한 데이터 오염 원천 차단 |
| **N-1 용량 초과 장애** | 한 센터 상실 시 단일 센터 자원이 전체 트래픽 감당 불가 | 평시 센터당 최대 사용률을 50% 이하로 통제(**N-1 설계**) | 장애 센터 절체 시 잔여 센터 연쇄 붕괴 방지 |
| **복제 지연 누적** | 피크 타임 I/O 급증 및 장거리 선로 레이턴시 누적 | DWDM 고속 전용선 대역폭 확보 및 스토리지 캐시 버퍼 최적화 | 애플리케이션 응답 속도 지연(Latency) 방어 |
| **논리적 오염 동시 전파** | 소프트웨어 버그나 악의적 SQL이 양 센터에 실시간 복제 | 제3 거점에 스냅샷 기반 격리 불변(**WORM**) 백업 병행 | 논리적 데이터 손상 시 시점 복구(PITR) 보장 |

## Ⅵ. 정합성 및 실전 절체 중심의 기술사적 제언

> 인프라 스펙 도입에 머물지 않고 센터 간 네트워크 **RTT 지연 통제**와 **정기적 불시 절체 실증**이 액티브-액티브의 성패를 가름.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 액티브-액티브 데이터센터의 치명적 함정은 양 센터가 상시 가동 중이라는 이유로 평시 모의훈련을 게을리하는 것임. 실제로 한쪽 센터가 불시에 단절되었을 때 잔여 센터의 CPU·메모리가 전체 트래픽을 감당하지 못해 연쇄 붕괴(Cascading Failure)하거나, 스플릿 브레인으로 데이터가 꼬이는 사고가 빈번함.
- 나라면: 센터 간 RTT 지연 5ms 이내 광전용선을 확보하고, 평시 각 센터의 자원 점유율을 50% 이하로 통제하는 'N-1 용량 기준'을 감리 기준에 필수 명시하며, 제3 거점 클라우드 쿼럼을 통한 I/O 펜싱을 자동화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 장비 이중화 도입을 넘어선 N-1 용량 통제 및 스플릿 브레인 차단
- 대안: **제3 거점 Quorum Witness** 구축 및 **N-1 용량 한계선(50% 상한)** 엄수
- 검증: 센터 간 RTT 5ms 이내 유지 · 분기별 불시 단절 모의절체 RTO 실증
- 효과: 단일 센터 전소 시에도 서비스 무중단 지속 및 데이터 무결성 보장

<div class="itpe-pipeline is-vertical" role="img" aria-label="액티브-액티브 스토리지 DR 신뢰성 확보 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>Active-Standby 기동 지연 · 유휴 인프라 비용 과다 및 전환 실패</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>Active-Active 다중 거점 분산 · 제3 거점 Quorum Witness 중재</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>센터 간 RTT 5ms 이내 유지 · N-1 부하 50% 이하 엄격 통제</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>RTO≈0 · RPO=0 달성 · 국가 핵심 디지털 행정 무중단 연속성 보장</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 2개 이상의 독립된 데이터센터에 서버와 스토리지를 상시 가동하여 부하를 분산하고 재해 시 무중단 승계하는 **액티브-액티브 재해복구(DR) 아키텍처**
- 목적: 단일 실패점(**SPOF**) 극복 및 **RTO(Recovery Time Objective)≈0**, **RPO(Recovery Point Objective)=0** 동시 달성

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="1교시 10점용 액티브-액티브 스토리지 DR 구조 요약">
  <div class="itpe-pipeline-node"><strong>GSLB 트래픽 제어</strong><small>헬스체크 및 RTT 기반 분산</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Active-Active 센터</strong><small>제1센터 Active ↔ 제2센터 Active</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>스토리지 동기 복제</strong><small>광채널 ISL 기반 실시간 미러링</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Quorum 중재</strong><small>제3 거점 Witness 기반 I/O 펜싱</small></div>
</div>

### 3. 핵심 통제

- **동기식 복제**: 통상 50km 이내 전용선 환경에서 데이터 유실 0건(**RPO=0**) 보장
- **Quorum Witness**: 센터 간 통신 장애 시 **Split-Brain** 방지 및 단독 마스터 승격 판정
- **N-1 용량 통제**: 단일 센터 상실에 대비하여 평시 센터별 자원 가동률 50% 이하 엄수

## 출제 이력과 검증 출처

- 시사·트렌드 집중 토픽 (국가 행정망 장애 및 데이터센터 화재 대응 핵심 아키텍처)
- 제133회 정보관리기술사 1교시: DRS 유형 (Mirror Site, Hot Site 등)
- 제140회 정보관리기술사 2교시: 공공 정보시스템 다중화 및 무중단 재해복구 전략
- 행정안전부, [행정기관 및 공공기관 정보자원 통합기준 고시](https://www.law.go.kr)
- NIST SP 800-34 Rev.1, [Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov)

## 학습 체크

- [ ] Active-Active와 Active-Standby의 구조적 차이점과 RTO/RPO 달성 수준을 비교할 수 있는가?
- [ ] 스토리지 동기 복제와 비동기 복제의 트레이드오프(지연시간 vs RPO)를 설명할 수 있는가?
- [ ] 스플릿 브레인 현상의 발생 원인과 Quorum Witness를 이용한 해결 메커니즘을 도식화할 수 있는가?
- [ ] N-1 용량 설계의 개념과 단일 센터 상실 시 연쇄 장애 방지 대책을 서술할 수 있는가?

## 연결 토픽

- 이전 토픽: [소프트웨어 사업 대가산정](./026_software_cost_estimation.md)
- 연관 토픽: [국가정보자원관리원 화재](./023_national_information_resources_service_fire.md), [RTO·RPO](./018_rpo.md), [DRS](./042_drs.md), [BCP](./030_bcp.md)
- 다음 토픽: [터크만 팀 발달 모델](./028_tuckman_team_development_model.md)
