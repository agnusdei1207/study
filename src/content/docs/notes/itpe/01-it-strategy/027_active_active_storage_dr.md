---
title: "액티브-액티브 이중화와 스토리지 DR"
author: "OpenAI Codex"
date: "2026-09-21T16:25:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 재해복구·서비스 연속성을 거쳐 액티브-액티브 이중화와 스토리지 DR로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>재해복구·서비스 연속성</span>
  <strong>액티브-액티브 이중화와 스토리지 DR</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 복수 거점이 평시에도 서비스를 분담하고 장애 시 정상 거점이 부하를 승계하는 고가용성·DR 구조
- 메커니즘: 트래픽 분산 → 애플리케이션 상태 공유 → 데이터 복제 → Quorum 판정 → 장애 거점 격리
- 통제: RTO·RPO 등급에 맞는 복제방식 · Split-Brain 방지 · 잔여 거점 수용용량 검증

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
      <div class="itpe-flow-branch"><strong>데이터 계층</strong><span>동기 또는 비동기 복제 · 쓰기 충돌 통제</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>제3 거점 Quorum 중재</strong>
    <small><span class="itpe-keyword"><strong>Split-Brain</strong></span> 방지 · 정상 거점 판정 · I/O Fencing</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Active-Active**: 복수 센터의 서버와 스토리지가 동시에 실제 트래픽을 분산 처리하는 상시 가동 구성
- **스토리지 DR(Disaster Recovery)**: 재해 발생 시 데이터 유실 없이 서비스를 지속하기 위해 원격지에 스토리지를 복제·대체 운용하는 체계
- **GSLB(Global Server Load Balancing)**: DNS 쿼리 단계에서 서버 헬스체크 및 지연시간을 측정하여 최적 거점으로 트래픽을 분산
- **동기 복제(Synchronous Replication)**: 로컬과 원격 스토리지의 쓰기 완료를 확인한 후 호스트에 응답하는 복제 기법
- **비동기 복제(Asynchronous Replication)**: 로컬 스토리지 완료 즉시 응답 후 원격지로 백그라운드 전송하여 원거리 지연을 방어하는 기법
- **Split-Brain**: 센터 간 네트워크 단절 시 양 센터가 상호 다운으로 오판하여 독자 쓰기를 수행하며 데이터가 분열되는 현상
- **Quorum Witness**: 네트워크 단절 시 양 센터 중 어느 센터가 쓰기를 지속할지 판정하는 제3 거점 독립 중재자
- **N-1 용량 설계**: 한 거점 상실 후에도 잔여 자원으로 목표 서비스를 운영할 수 있게 수용용량을 확보하는 설계 원칙

</details>

## 예상문제

> 다중 거점 Active-Active 및 스토리지 DR의 구성 메커니즘을 설명하고, 동기·비동기 복제의 특징과 Split-Brain 방지 대책을 논하시오. **(미출제 예상·25점)**

## Ⅰ. 무중단 서비스 연속성을 위한 액티브-액티브 스토리지 DR의 개요

> 서비스 Active-Active와 데이터 동기 복제는 같은 뜻이 아니며, 업무의 RTO·RPO와 정합성 요구에 따라 조합해야 함.

- 정의: 복수 거점의 서비스 자원을 동시에 운영하고 장애 거점의 부하를 정상 거점으로 전환하는 고가용성·재해복구 구조
- 목적: 서비스 중단시간 단축 · 자원 활용 · 업무 연속성 확보

## Ⅱ. 액티브-액티브 스토리지 DR 구성체계 및 복제 메커니즘

> 트래픽 제어부터 스토리지 블록 미러링과 쿼럼 중재까지 계층별 파이프라인으로 연결해야 무손실 자동 절체가 완성됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="액티브-액티브 스토리지 DR 구성체계 및 단계별 활동과 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 트래픽 감지 및 분산</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>GSLB 헬스체크 · Anycast 라우팅 기반 다중 거점 부하분산</span>
      <strong>산출</strong><span>DNS 트래픽 분산 정책서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 애플리케이션 무상태 처리</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>분산 세션 클러스터링 및 MSA 컨테이너 분산 가동</span>
      <strong>산출</strong><span>무상태(Stateless) 아키텍처 설계서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 스토리지 블록 동기 미러링</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>전용 광채널(ISL) 기반 양방향 쓰기 복제 및 캐시 동기화</span>
      <strong>산출</strong><span>스토리지 동기 복제 구성도</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 제3 거점 쿼럼 상태 감시</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>하트비트 신호 모니터링 및 센터 간 네트워크 단절 감지</span>
      <strong>산출</strong><span>Quorum Witness 감시 로그</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 장애 판정 및 I/O 펜싱</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>단절 센터 쓰기 즉시 차단 및 정상 센터 단독 마스터 승격</span>
      <strong>산출</strong><span>자동 절체(Failover) 결과서</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · GSLB 헬스체크 ↔ 스토리지 동기 복제 ↔ Quorum 중재 ↔ 무중단 서비스 양방향 연계</div>

## Ⅲ. 스토리지 복제 방식(동기식 vs 비동기식) 비교

> 동기식은 데이터 정합성을 우선하고, 비동기식은 원거리 전송과 응답지연 완화를 우선함.

| 비교 기준 | 동기식 복제 (Synchronous) | 비동기식 복제 (Asynchronous) |
|---|---|---|
| **동작 메커니즘** | 양쪽 스토리지에 모두 쓰기가 완료된 후 호스트에 응답 | 로컬 스토리지에 쓴 뒤 즉시 응답하고 원격지 백그라운드 전송 |
| **RPO** | 완료 응답된 쓰기의 원격 반영 | 복제 지연 구간의 손실 가능 |
| **거리** | RTT 증가에 민감 | 원거리 구성에 유리 |
| **성능** | 원격 쓰기 확인만큼 지연 증가 | 로컬 쓰기 응답 후 전송 |
| **선택기준** | 데이터 손실 허용 불가 · 지연 수용 | 지연 최소화 · 제한적 손실 수용 |

## Ⅳ. 액티브-액티브(Active-Active) vs 액티브-스탠바이(Active-Standby) 비교

> Active-Active는 복구시간을 줄이지만 동시운영·정합성 통제가 복잡하고, Active-Standby는 단순하지만 전환시간과 대기자원 비용이 발생함.

| 비교 기준 | 액티브-액티브 (Active-Active) | 액티브-스탠바이 (Active-Standby) |
|---|---|---|
| **평시 운영 상태** | 양 센터 모두 실제 워크로드 동시 분산 처리 | 주 센터만 운영, 대기 센터는 유휴 상태 대기 |
| **RTO** | 트래픽 전환 중심 | 대기자원 기동·승격 필요 |
| **RPO** | 선택한 데이터 복제방식에 좌우 | 선택한 데이터 복제방식에 좌우 |
| **자원** | 평시 양쪽 활용 | 대기자원 활용 제한 |
| **복잡도** | 정합성·세션·쓰기 충돌 통제 | 전환절차·구성 동기화 통제 |

## Ⅴ. 실무 아키텍처 실패 모드와 공학적 해결 방안

> 분산 환경에서 발생하는 네트워크 단절과 용량 초과는 연쇄 장애의 주원인이므로 사전 통제가 필수적임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **스플릿 브레인(Split-Brain)** | 제3 거점 독립 **Quorum Witness** 배치 및 다수결 I/O 펜싱 | 양방향 동시 쓰기로 인한 데이터 오염 원천 차단 |
| **잔여 거점 용량 부족** | **N-1 용량 설계**와 부하차단 우선순위 검증 | 연쇄 장애 방지 |
| **복제 지연 누적** | 회선·변경량 모니터링 · 업무별 동기·비동기 분리 | 지연과 RPO 균형 |
| **논리적 오염 전파** | 복제와 분리된 불변 백업·복구점 운영 | 정상 시점 복구 |

## Ⅵ. 정합성 및 실전 절체 중심의 기술사적 제언

> 장비가 이중화되어도 실제 절체와 복구를 검증하지 않으면 DR은 문서상 구성에 머무름.

`[핵심 통찰]` Active-Active의 위험은 장애 거점보다 살아남은 거점의 용량 부족과 잘못된 이중 쓰기이며, 가용성은 장비 수가 아니라 장애 격리 후 서비스·데이터의 일관성으로 판정해야 함.

`나라면` 업무등급별 RTO·RPO로 복제방식을 정하고, 단일 거점 단절훈련에서 Quorum 판정·I/O Fencing·잔여 용량·복구 데이터를 함께 검증하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="액티브-액티브 스토리지 DR 신뢰성 확보 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>미검증 자동절체 · Split-Brain · 잔여 거점 용량 부족</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>Quorum Witness · I/O Fencing · N-1 용량 설계</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>목표 RTO·RPO · 쓰기 정합성 · 잔여 용량 · 복구 가능성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>장애 격리 · 연쇄 장애 방지 · 검증 가능한 서비스 연속성</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 복수 거점의 서비스 자원을 동시에 운영하고 장애 거점의 부하를 정상 거점으로 전환하는 고가용성·재해복구 구조
- 목적: 서비스 중단시간 단축 · 자원 활용 · 업무 연속성 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="1교시 10점용 액티브-액티브 스토리지 DR 구조 요약">
  <div class="itpe-pipeline-node">
    <strong>GSLB 트래픽 제어</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>헬스체크 및 RTT 기반 분산</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Active-Active 센터</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>제1센터 Active ↔ 제2센터 Active</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>스토리지 동기 복제</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>광채널 ISL 기반 실시간 미러링</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Quorum 중재</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>제3 거점 Witness 기반 I/O 펜싱</span></div>
  </div>
</div>

### 3. 핵심 통제

- **동기식 복제**: 원격 쓰기 완료를 확인한 뒤 응답하여 완료된 쓰기의 정합성을 확보
- **Quorum Witness**: 센터 간 통신 장애 시 **Split-Brain** 방지 및 단독 마스터 승격 판정
- **N-1 용량 설계**: 단일 거점 상실 후 잔여 거점의 수용능력과 부하차단 순위를 검증

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [NIST SP 800-34 Rev.1: Contingency Planning Guide for Federal Information Systems](https://csrc.nist.gov/pubs/sp/800/34/r1/final)

## 학습 체크

- [ ] Ⅰ. Active-Active의 정의·목적과 데이터 복제방식이 별도 결정임을 설명할 수 있는가?
- [ ] Ⅱ. 트래픽 분산부터 Quorum·I/O Fencing까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ~Ⅳ. 동기·비동기 복제와 Active-Active·Active-Standby를 구분할 수 있는가?
- [ ] Ⅴ. Split-Brain·용량 부족·복제 지연·논리오염의 대응책을 제시할 수 있는가?
- [ ] Ⅵ. 단절훈련에서 RTO·RPO·정합성·잔여 용량을 검증하는 방안을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [소프트웨어 사업 대가산정](./026_software_cost_estimation.md)
- 연관 토픽: [국가정보자원관리원 화재](./023_national_information_resources_service_fire.md), [RTO·RPO](./018_rpo.md), [DRS](./042_drs.md), [BCP](./030_bcp.md)
- 다음 토픽: [터크만 팀 발달 모델](./028_tuckman_team_development_model.md)
