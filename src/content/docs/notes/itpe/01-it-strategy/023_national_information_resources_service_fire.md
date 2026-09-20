---
title: "국가정보자원관리원 화재와 공공 디지털서비스 회복탄력성"
author: "Codex"
date: "2026-09-21T12:30:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 재해복구·서비스 연속성을 거쳐 국가정보자원관리원 화재와 공공 디지털서비스 회복탄력성으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>재해복구·서비스 연속성</span>
  <strong>국가정보자원관리원 화재와 공공 디지털서비스 회복탄력성</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 2025년 국정자원 대전센터 화재가 공공 디지털서비스의 센터 집중·DR 미비 위험을 드러낸 사건
- 메커니즘: 시스템 중요도 분류 → 이중운영·대기형 DR 선택 → 데이터 이중화 → 전환훈련
- 후속: 대전센터 시스템 재배치 ISP와 13개 시스템 Active-Active DR 설계 추진

<div class="itpe-flow-map" role="img" aria-label="물리 재난에서 다중 거점 서비스 연속성으로 이어지는 회복탄력성 흐름">
  <div class="itpe-flow-node">
    <strong>물리 설비 재난</strong>
    <small>2025년 대전센터 화재 · 행정정보시스템 장애</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>장애 전파 차단</strong>
    <small>방화구획 물리 격리 · 전력·통신 인입 관로 이원화</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>다중 거점 회복탄력성 체계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>접속</strong><span><span class="itpe-keyword"><strong>GSLB</strong></span> 기반 트래픽 자동 우회</span></div>
      <div class="itpe-flow-branch"><strong>애플리케이션</strong><span>무상태(Stateless) 컨테이너 분산</span></div>
      <div class="itpe-flow-branch"><strong>데이터</strong><span>업무등급별 동기·비동기 복제 및 격리 백업</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>검증 가능한 행정서비스 연속성</strong>
    <small>서비스별 <span class="itpe-keyword"><strong>RTO·RPO</strong></span> 실측 · 전환·복귀 검증</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **SPOF(Single Point of Failure)**: 단일 구성요소 고장이 시스템 전체 마비로 파급되는 단일 실패점
- **공통원인 장애(Common Cause Failure)**: 하나의 물리적 사건(화재·정전)이 공유 인프라를 통해 다수 서비스로 전파되는 장애
- **GSLB(Global Server Load Balancing)**: DNS 기반 헬스체크를 통해 장애 센터를 배제하고 정상 거점으로 트래픽을 자동 분산
- **Active-Active DR(이중운영체계)**: 복수 거점이 서비스를 운영하여 대기형 DR보다 전환시간을 줄이는 구성
- **RTO(Recovery Time Objective)**: 재해 발생 시 서비스가 정상 수준으로 복구되기까지 허용되는 최대 시간
- **RPO(Recovery Point Objective)**: 재해 발생 시 유실을 허용할 수 있는 최대 데이터 시점 간격
- **에어갭(Air-Gap)**: 백업 저장소를 네트워크와 물리적으로 단절시켜 악성코드 감염 및 물리 재난으로부터 데이터를 보존
- **Split-Brain**: 네트워크 단절 시 양 센터가 상호 다운으로 오판하여 독자 쓰기를 수행하며 발생하는 데이터 불일치 현상

</details>

## 예상문제

> 국가정보자원관리원 화재로 드러난 공공 디지털서비스의 연속성 문제를 분석하고, 시스템 등급별 재해복구체계와 검증 방안을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 물리적 설비 방호에서 디지털 회복탄력성으로의 전환 개요

> 데이터센터 물리 재난 시 핵심 서비스의 무중단 제공 능력을 확보하며, 성패는 단순 설비 내구성이 아닌 **다중 거점 서비스 다중화**와 **RTO·RPO 단축**으로 판정함.

- 정의: 재난에도 핵심 서비스를 허용 수준으로 유지하고 정해진 목표 안에 복구하는 **회복탄력성(Resilience)** 역량
- 목적: 장애영향 축소 · 행정서비스 연속성 확보 · 복구능력 검증

## Ⅱ. 장애 전파 차단·회복탄력성의 대표 흐름

> 화재 전파 경로를 계층별로 차단하고 `물리격리 → 가상화망 → 공통분산 → 동기복제 → 자동절체` 파이프라인으로 연결해야 서비스가 지속됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="회복탄력성 5단계 구성체계 및 단계별 활동과 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 물리 설비 격리</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>배터리실 방화구획 분리 · 전원·통신 인입 관로 이원화</span>
      <strong>산출</strong><span>물리 격리 설계서 · 관로 이원화 도면</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 인프라 가상화 및 망 분산</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>다중 거점 클라우드 배치 · 전용 백본망 이중화</span>
      <strong>산출</strong><span>멀티 리전 인프라 구성도 · 대역폭 용량계획서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 플랫폼 및 공통 서비스 분산</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>공통 인증·행정연계 게이트웨이 거점별 독립 배포</span>
      <strong>산출</strong><span>분산 게이트웨이 아키텍처 · 무상태 컨테이너 매니페스트</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 데이터 동기 복제 및 에어갭</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>업무등급별 데이터 이중화 · 원격지 격리 백업</span>
      <strong>산출</strong><span>복제 정책서 · 복구 백업 대장</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 자동 장애 감지 및 절체</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>장애 감지 · 서비스 전환 · 데이터 정합성 확인 · 복귀</span>
      <strong>산출</strong><span>Failover 절차서 · 전환훈련 결과서</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · 물리 재난 감지 ↔ GSLB 트래픽 우회 ↔ 스토리지 정합성 ↔ 서비스 무중단 검증</div>

## Ⅲ. 단순 설비 이중화 vs 분산 서비스 다중화 비교

> 단순 설비 이중화는 상면 전소 시 무력화되므로, 센터를 초월한 **서비스 다중화**로 패러다임을 전환해야 함.

| 기준 | 단일센터 설비 이중화 | 다중거점 서비스 연속성 |
|---|---|---|
| **보호 범위** | 장비·설비 장애 | 센터 상실·광역 재난 |
| **서비스 배치** | 단일 거점 집중 | 이중운영 또는 대기형 DR |
| **데이터 보호** | 센터 내부 이중화 | 원격 복제·격리 백업 |
| **검증** | 부품·설비 시험 | 서비스 전환·복귀 훈련 |

## Ⅳ. 계층별 회복탄력성 아키텍처 및 핵심 통제

> 물리·네트워크·플랫폼·데이터의 공유 의존성을 분리해야 공통원인 장애의 전파 범위를 줄일 수 있음.

| 계층 | 대책 | 검증 |
|---|---|---|
| **시설** | 방화구획 · 전력·통신 경로 분리 | 설비 점검·재난 시나리오 |
| **서비스** | 중요도별 이중운영·대기형 DR | 전환 후 핵심기능 확인 |
| **데이터** | 원격 복제 · 격리 백업 | 정합성·복원 시험 |
| **운영** | 전환·복귀 절차와 책임 명시 | RTO·RPO 실측 |

## Ⅴ. 다중거점 전환의 문제점·대응책

> 다중 거점 분산 환경에서는 동기 복제 지연과 **Split-Brain** 방지가 아키텍처의 최대 공학적 난제임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **Split-Brain 발생** | 독립 Quorum Witness · 펜싱 통제 | 동시 쓰기·데이터 충돌 위험 완화 |
| **원격 동기 복제 지연** | 핵심 DB 동기 복제, 비정형 데이터 비동기 파이프라인 분리 | 주 센터 트랜잭션 성능 저하 억제 및 가용성 유지 |
| **공통 연계망 단절** | 행정연계 게이트웨이의 Active-Active 다중 거점화 | 타 부처 및 대국민 연계 서비스 연속성 보증 |
| **비상 절체(Failover) 실패** | IaC 기반 복구 자동화 · 전환훈련 | 목표 RTO 달성 가능성 확인 |

## Ⅵ. 결론 — 무상태 분산·전환훈련 기반 회복탄력성

> 완벽한 건물이 아닌 언제든 한쪽 센터를 즉시 버릴 수 있는 **무상태(Stateless) 분산 구조**와 **실전 불시 절체 검증**이 회복탄력성의 본질임.

`[핵심 통찰]` 시설 이중화만으로는 센터 단위 재난을 견딜 수 없으며, 서비스·데이터·운영절차가 다른 거점에서 실제 작동해야 회복탄력성이 성립함.

`나라면` 모든 시스템에 고비용 Active-Active를 강제하지 않고, 업무등급별로 이중운영·대기형 DR을 선택한 뒤 전환훈련의 실측 RTO·RPO로 투자 적정성을 검증하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="다중 거점 회복탄력성 구축 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail">
      <strong>문제</strong><span>단일 센터 설비 이중화 · 공통 연계망 중앙 집중 의존</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail">
      <strong>대안</strong><span>업무등급별 이중운영·대기형 DR · 원격 백업</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail">
      <strong>판정</strong><span>전환·복귀 성공 · RTO·RPO 실측 · 데이터 정합성</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail">
      <strong>효과</strong><span>센터 상실 영향 축소 · 복구능력 증명</span>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 재난에도 핵심 서비스를 허용 수준으로 유지하고 정해진 목표 안에 복구하는 **회복탄력성(Resilience)** 역량
- 목적: 장애영향 축소 · 행정서비스 연속성 확보 · 복구능력 검증

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="1교시 10점용 회복탄력성 메커니즘 요약">
  <div class="itpe-pipeline-node">
    <strong>① 물리격리</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>배터리실 방화구획 분리</span>
      <strong>산출</strong><span>관로 이원화 도면</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>② 트래픽우회</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>GSLB 자동 헬스체크</span>
      <strong>산출</strong><span>Failover 경로</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>③ 데이터동기</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>Active-Active 스토리지 미러링</span>
      <strong>산출</strong><span>동기 복제 정책서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>④ 불변보존</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>제3 거점 에어갭 WORM 백업</span>
      <strong>산출</strong><span>불변 백업 대장</span>
    </div>
  </div>
</div>

### 3. 핵심 통제

- **이중운영(Active-Active DR)**: 복수 거점이 서비스를 운영하여 전환시간을 줄이는 방식
- **대기형(Active-Standby DR)**: 주 시스템 장애 시 보조 시스템으로 전환하는 방식
- **전환훈련**: 서비스·데이터·연계 기능을 전환하고 복귀하여 RTO·RPO를 실측

## 출제 이력과 검증 출처

- [행정안전부: 국정자원 혁신 ISP 착수](https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=126568)
- [행정안전부: 국정자원 DR 구축 ISP 착수](https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do%3Bjsessionid%3DFAiZ7-yPmlD1qtA3xJmCFCFZXV3liaV5TYPLvJZv.node10?bbsId=BBSMSTR_000000000008&nttId=126963)

## 학습 체크

- [ ] Ⅰ 개요: 공통원인 장애와 서비스 회복탄력성의 관계를 설명할 수 있는가?
- [ ] Ⅱ 흐름: 물리격리부터 자동 절체까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ 비교: 설비 이중화와 다중거점 서비스 다중화의 보호대상·범위를 비교할 수 있는가?
- [ ] Ⅳ 계층 통제: 시설·네트워크·플랫폼·데이터별 취약점과 통제를 연결할 수 있는가?
- [ ] Ⅴ 문제점·대응책: Split-Brain·복제 지연·연계망 단절·절체 실패의 위험·대책·효과를 연결할 수 있는가?
- [ ] Ⅵ 결론: 전환훈련 중심의 판정·대안·검증·효과를 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [공공부문 클라우드 네이티브 전환](./021_public_cloud_native_transition.md)
- 연관 토픽: [액티브-액티브 스토리지 DR](./027_active_active_storage_dr.md), [RTO·RPO](./018_rpo.md), [DRS](./042_drs.md)
- 다음 토픽: [국가 AI 전략](./024_korea_ai_action_plan.md)
