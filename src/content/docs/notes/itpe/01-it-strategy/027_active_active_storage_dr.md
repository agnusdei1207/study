---
title: "액티브-액티브 이중화와 스토리지 DR"
author: "Antigravity"
date: "2026-09-21T15:40:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 재해복구·서비스 연속성을 거쳐 액티브-액티브 이중화와 스토리지 DR로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>재해복구·서비스 연속성</span>
  <strong>액티브-액티브 이중화와 스토리지 DR</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **액티브-액티브 이중화와 스토리지 DR**은 복수 데이터센터가 평시 실제 워크로드를 동시 분산 처리(Active-Active)하고, 스토리지 블록 미러링과 제3 거점 Quorum 중재를 통해 단일 센터 전소 시에도 RTO 0·RPO 0에 근접한 무중단 서비스를 보장하는 최고 수준의 재해복구 아키텍처
- 메커니즘: GSLB 트래픽 분산 → 무상태(Stateless) 컨테이너 앱 실행 → 광채널(ISL) 기반 스토리지 동기 복제 → 제3 거점 Quorum Witness 헬스체크 및 I/O Fencing → 장애 센터 격리
- 산출물: 다중 거점 Active-Active 네트워크 구성도 · 스토리지 동기 복제 정책서 · Quorum 중재 규칙서 및 N-1 용량 검증서

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

> **동기식 복제(Synchronous)**는 양쪽 쓰기 완료를 보장하여 데이터 정합성(RPO=0)을 최우선시하고, **비동기식 복제(Asynchronous)**는 로컬 즉시 응답으로 원거리 전송 지연(Latency)을 최소화함.

<div class="itpe-svg-map">
<svg viewBox="0 0 520 330" role="img" aria-label="동기식 복제와 비동기식 복제의 I/O 흐름 및 응답 시점을 비교한 메커니즘 다이어그램">
  <rect class="itpe-svg-node is-current" x="10" y="8" width="500" height="42" rx="10" />
  <text class="itpe-svg-title" x="260" y="30">스토리지 복제 방식 메커니즘 비교</text>
  
  <!-- 동기식 레인 -->
  <rect class="itpe-svg-node" x="10" y="60" width="240" height="250" rx="8" />
  <text class="itpe-svg-sub" x="130" y="85">동기식 복제 (Sync)</text>
  <text class="itpe-svg-label" x="130" y="105">RPO = 0 · 무손실 보장</text>
  <path class="itpe-svg-link" d="M130 115 V280" />
  <circle cx="130" cy="135" r="5" fill="#3b82f6" />
  <text class="itpe-svg-label" x="140" y="140" text-anchor="start">① 호스트 쓰기 요청</text>
  <circle cx="130" cy="175" r="5" fill="#3b82f6" />
  <text class="itpe-svg-label" x="140" y="180" text-anchor="start">② 원격지 동기 복제(ISL)</text>
  <circle cx="130" cy="215" r="5" fill="#3b82f6" />
  <text class="itpe-svg-label" x="140" y="220" text-anchor="start">③ 원격 쓰기 완료 응답</text>
  <circle cx="130" cy="255" r="5" fill="#10b981" />
  <text class="itpe-svg-label" x="140" y="260" text-anchor="start">④ 호스트 최종 응답(ACK)</text>
  <text class="itpe-svg-label" x="130" y="295">거리 한계: RTT 10ms 이내 권장</text>

  <!-- 비동기식 레인 -->
  <rect class="itpe-svg-node" x="270" y="60" width="240" height="250" rx="8" />
  <text class="itpe-svg-sub" x="390" y="85">비동기식 복제 (Async)</text>
  <text class="itpe-svg-label" x="390" y="105">RPO > 0 · 원거리 무제한</text>
  <path class="itpe-svg-link" d="M390 115 V280" />
  <circle cx="390" cy="135" r="5" fill="#3b82f6" />
  <text class="itpe-svg-label" x="400" y="140" text-anchor="start">① 호스트 쓰기 요청</text>
  <circle cx="390" cy="175" r="5" fill="#10b981" />
  <text class="itpe-svg-label" x="400" y="180" text-anchor="start">② 로컬 즉시 응답(ACK)</text>
  <circle cx="390" cy="215" r="5" fill="#f59e0b" />
  <text class="itpe-svg-label" x="400" y="220" text-anchor="start">③ 백그라운드 원격 전송</text>
  <circle cx="390" cy="255" r="5" fill="#f59e0b" />
  <text class="itpe-svg-label" x="400" y="260" text-anchor="start">④ 원격지 버퍼 기록</text>
  <text class="itpe-svg-label" x="390" y="295">적용 대상: 대륙간 원거리 DR</text>
</svg>
</div>

| 비교 기준 | 동기식 복제 (Synchronous) | 비동기식 복제 (Asynchronous) |
|---|---|---|
| **동작 메커니즘** | 양쪽 스토리지에 모두 쓰기가 완료된 후 호스트에 응답 | 로컬 스토리지에 쓴 뒤 즉시 응답하고 원격지 백그라운드 전송 |
| **RPO** | 완료 응답된 쓰기의 원격 반영 (**RPO = 0**) | 복제 지연 구간의 데이터 유실 가능 (**RPO > 0**) |
| **거리 제약** | 광채널 지연(RTT) 민감 (통상 100km 이내) | 거리 제약 없음 (광역 및 글로벌 원거리 가능) |
| **호스트 성능** | 원격지 왕복 지연만큼 I/O Latency 증가 | 로컬 쓰기 즉시 반환으로 애플리케이션 지연 없음 |
| **선택 기준** | 금융 거래, 공공 핵심 행정 등 데이터 무손실 필수 | 대규모 비정형 데이터, 원거리 재난 대피 DR |

## Ⅳ. 액티브-액티브(Active-Active) vs 액티브-스탠바이(Active-Standby) 비교

> **Active-Active**는 평시 자원 활용률을 극대화하고 복구시간(RTO)을 단축하지만 동시 쓰기 정합성 통제가 복잡하며, **Active-Standby**는 구조가 단순하지만 대기 자원의 유휴 비용이 발생함.

| 비교 기준 | 액티브-액티브 (Active-Active) | 액티브-스탠바이 (Active-Standby) |
|---|---|---|
| **평시 운영 상태** | 양 센터 모두 실제 워크로드 동시 분산 처리 | 주 센터만 운영, 대기 센터는 유휴 상태 대기 |
| **RTO** | DNS/GSLB 트래픽 전환 즉시 복구 (**RTO ≈ 0**) | 대기 자원 기동·승격·DB 정합성 확인 시간 소요 |
| **RPO** | 선택한 데이터 복제방식에 좌우 (**동기 시 RPO=0**) | 선택한 데이터 복제방식에 좌우 |
| **자원 활용률** | 100% (양 센터 자원 평시 가동) | 50% 미만 (대기 센터 자원 유휴화) |
| **아키텍처 난이도** | 정합성·분산 세션·쓰기 충돌·스플릿브레인 통제 | 비교적 단순한 Failover 절차 및 복구 시나리오 |

## Ⅴ. 실무 아키텍처 실패 모드와 공학적 해결 방안

> 분산 환경에서 발생하는 네트워크 단절과 잔여 용량 초과는 연쇄 붕괴의 주원인이므로 공학적 통제 장치가 필수적임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **스플릿 브레인(Split-Brain)** | 제3 거점 독립 **Quorum Witness** 배치 및 다수결 **I/O Fencing** | 양방향 동시 쓰기로 인한 데이터 오염 원천 차단 |
| **잔여 거점 용량 부족** | **N-1 용량 설계**와 비핵심 업무 자동 부하차단(Shedding) | 단일 거점 상실 시 연쇄 과부하 다운 차단 |
| **복제 지연 누적** | 회선 대역폭 모니터링 · 중요도별 동기/비동기 분리 적용 | 트랜잭션 병목 해소 및 RPO 균형 확보 |
| **논리적 오염 전파** | 실시간 복제와 분리된 제3 거점 **불변(WORM) 백업** 운영 | 랜섬웨어 및 관리자 실수 발생 시 과거 시점 복원 |

## Ⅵ. 정합성 및 실전 절체 중심의 기술사적 제언

> 아무리 고가의 이중화 장비를 구축했더라도 불시 실전 모의 절체 훈련을 통해 실측 검증하지 않으면 DR은 문서상 계획에 불과함.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: Active-Active 아키텍처의 가장 치명적인 위험은 장애가 발생한 센터가 아니라, 살아남은 단일 센터의 용량 초과와 네트워크 단절 시 발생하는 Split-Brain 데이터 오염이다.
- `나라면`: 모든 인프라에 무리한 전면 Active-Active를 강제하지 않고, 서비스 중요도에 맞추어 Tier 1 업무에만 동기 복제 + Quorum 중재를 적용하고, 평시 50% 부하 상한선(N-1 용량 설계)을 엄격히 통제하겠다.

### 실전 답안용 기술사적 제언

- 판정: 단일 거점 전소 시에도 잔여 센터 단독으로 목표 SLA를 보증할 수 있는 공학적 안전장치를 갖추었는가
- 대안: **Quorum Witness** 기반 I/O Fencing + **N-1 용량 설계** 기반 자동 부하 차단 거버넌스
- 검증: 연 2회 불시 단절 모의훈련 · RTO < 1분, RPO = 0 실측 · 스토리지 데이터 정합성 검증
- 효과: 대민 서비스 24/365 무중단 보증 · 재난 발생 시 데이터 무손실 및 연쇄 장애 방지

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
