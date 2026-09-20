---
title: "무중단 배포·배포 전략"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 빌드·배포·DevOps를 거쳐 무중단 배포로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>빌드·배포·DevOps</span>
  <strong>무중단 배포·배포 전략</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **무중단 배포(Zero-Downtime Deployment)**는 서비스 운영 중단(Downtime) 없이 신규 버전을 프로덕션에 배포하고 즉각 롤백을 지원하는 아키텍처 전략
- 메커니즘: **Rolling**(점진 교체) · **Blue/Green**(이중 환경 스위칭) · **Canary**(소규모 카나리 트래픽 검증 후 전면 전환)
- 산출/효과: 가용성(High Availability) 99.999% 유지 · 배포 위험 최소화 · 무중단 사용자 경험 보장

<div class="itpe-flow-map" role="img" aria-label="무중단 배포 전략 흐름도">
  <div class="itpe-flow-node"><strong>로드밸런서(LB)</strong><small>트래픽 라우팅 제어</small></div>
  <div class="itpe-flow-arrow">→ 배포 전략 선택 →</div>
  <div class="itpe-flow-node is-current">
    <strong>무중단 배포 방식</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Rolling</strong><span>인스턴스 순차 갱신 (자원 절약)</span></div>
      <div class="itpe-flow-branch"><strong>Blue/Green</strong><span><span class="itpe-keyword"><strong>환경 전체 스위칭</strong></span> (즉시 롤백)</span></div>
      <div class="itpe-flow-branch"><strong>Canary</strong><span><span class="itpe-keyword"><strong>가중치 기반 점진 노출</strong></span> (위험 격리)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 검증 및 전환 →</div>
  <div class="itpe-flow-node"><strong>프로덕션 서비스</strong><small>Downtime Zero 운영</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Zero-Downtime Deployment**: 사용자가 서비스 중단을 체감하지 못하도록 트래픽을 제어하며 새 버전을 반영하는 배포 기법
- **Blue/Green Deployment**: 동일한 구성을 가진 Blue(현재 버전)와 Green(신규 버전) 환경을 구축하고 라우터를 통해 트래픽을 한 번에 전환하는 방식
- **Canary Deployment**: 위험을 조기 감지하기 위해 극소수(예: 1~5%)의 사용자 트래픽만 신규 버전에 흘려보내 검증 후 점진 확대하는 방식
- **Rolling Deployment**: 실행 중인 인스턴스를 하나씩 순차적으로 내리고 새 버전으로 교체하여 점진 배포하는 방식
- **Expand/Contract Pattern**: 무중단 배포 시 DB 스키마 호환성을 유지하기 위해 확장(Expand) 후 이전(Transition) 및 축소(Contract)하는 3단계 기법

</details>

## 예상문제

> 클라우드 네이티브 환경에서 무중단 배포(Zero-Downtime Deployment)의 필요성을 설명하고, 3대 배포 전략(Rolling, Blue/Green, Canary)의 장단점 및 데이터베이스 스키마 변경 시 호환성 확보 방안을 제시하시오. (25점)

## Ⅰ. 24/7 무중단 서비스의 필수 요건, 무중단 배포의 개요

> 무중단 배포는 서비스 점검 시간(Maintenance Window)을 없애고, 배포 실패 시 복구 지연을 원천 차단하는 엔지니어링 역량이다.

- 정의: 애플리케이션 업데이트 중에도 시스템 중단 없이 지속적으로 사용자 요청을 처리하도록 트래픽을 동적으로 제어하는 배포 기술
- 목적: 비즈니스 가용성(24/7/365) 확보, 릴리스 주기 가속화, 배포 실패 시 **MTTR(복구 시간)** 제로화

## Ⅱ. 3대 무중단 배포 전략의 메커니즘 및 비교

> 인프라 자원 여력, 롤백 속도, 검증 정밀도에 따라 최적의 배포 전략을 선택해야 한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="3대 무중단 배포 전략 구조">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① Rolling 배포</strong></span>
    <small>인스턴스를 n개씩 순차 교체 · 추가 자원 최소화<br />→ 배포 중 구버전/신버전 혼재 발생</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② Blue/Green 배포</strong></span>
    <small>신규 Green 환경 사전 완벽 검증 후 로드밸런서 스위칭<br />→ 인프라 2배 필요, 스위칭 즉시 롤백 가능</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ Canary 배포</strong></span>
    <small>카나리아 광부 메타포 · 1% → 10% → 100% 트래픽 점진 확대<br />→ 실 사용자 기반 오류율·지연 모니터링 후 자동 롤백</small>
  </div>
</div>

| 비교 기준 | Rolling Update | Blue/Green | Canary |
|---|---|---|---|
| **인프라 비용** | 기존 인프라 활용 (낮음) | 2배 인프라 필요 (높음) | 기존 또는 최소 증설 (중간) |
| **배포 위험도** | 중간 (일부 사용자 영향) | 낮음 (사전 검증 완료) | **매우 낮음** (극소수 사용자 격리) |
| **롤백 속도** | 역순 롤링 필요 (느림) | **즉각 롤백 (LB 재스위칭)** | 카나리 트래픽 즉각 차단 (빠름) |
| **버전 공존 여부** | 배포 중 공존 | 순간적 전환 (공존 없음) | 의도적 장시간 공존 |
| **적합한 상황** | 자원 제약이 있는 환경 | 중요 금융·결제 시스템 전면 교체 | 대규모 B2C 서비스, A/B 테스팅 연계 |

## Ⅲ. 무중단 배포의 핵심 난제: 데이터베이스 호환성 통제

> 애플리케이션 코드는 무중단 배포가 가능하지만, DB 스키마가 하위 호환성을 깨뜨리면 전체 시스템 장애로 이어진다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="Expand-Contract DB 스키마 변경 패턴">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>Phase 1: Expand (확장)</strong></span>
    <small>기존 컬럼 유지 + 신규 컬럼 추가 (구버전 앱 정상 동작 보장)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>Phase 2: Transition (이행 및 양방향 쓰기)</strong></span>
    <small>신버전 앱 배포 · 신규 컬럼 읽기/쓰기 및 백그라운드 데이터 마이그레이션</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>Phase 3: Contract (축소 및 정리)</strong></span>
    <small>모든 인스턴스 신버전 전환 확인 후 구버전 컬럼 삭제</small>
  </div>
</div>

## Ⅳ. 무중단 배포 운영 시 기술적 고려사항

> 애플리케이션의 세션 유지와 커넥션 드레이닝이 보장되지 않으면 배포 중 사용자의 연결이 끊어진다.

| 위험 요소 | 기술적 원인 | 실무 대응 통제책 |
|---|---|---|
| **세션 끊김** | 인스턴스 인메모리 세션 소멸 | Redis 기반 외장형 분산 세션 스토어(Sticky Session 지양) |
| **진행 중 요청 유실** | 인스턴스 강제 종료 (SIGKILL) | **Graceful Shutdown** 및 **Connection Draining**(30초 유예) |
| **헬스체크 실패 오판** | 기동 초기 트래픽 급유입 | Kubernetes `readinessProbe` 및 `livenessProbe` 정밀 구성 |

## Ⅴ. 고가용 무중단 아키텍처를 위한 기술사적 제언

> 배포는 단순 스크립트 실행이 아니며, 인프라 라우팅, 관측성, 데이터 호환성이 삼위일체로 작동해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 많은 기업이 쿠버네티스를 도입하면 무중단 배포가 저절로 된다고 착각하지만, 실제 장애의 80%는 DB 스키마 변경 불일치와 우아한 종료(Graceful Shutdown) 부재에서 발생함. 앱 배포 주기와 DB 마이그레이션 주기를 반드시 분리해야 함.
- 나라면: 서비스 메시(Istio)와 Argo Rollouts를 결합하여 메트릭 기반 자동 카나리 분석(Automated Canary Analysis)을 구축하고, 오류율 1% 초과 시 사람 개입 없이 즉시 자동 롤백되도록 구성하겠음.

### 실전 답안용 기술사적 제언

- 판정: 서비스 중요도에 따른 배포 전략 차등화 (핵심 코어: Blue/Green, 대고객: Canary)
- 대안: **GitOps(ArgoCD)** 기반 선언적 배포 및 **Expand/Contract** DB 패턴 표준화
- 검증: 배포 중 5xx 에러율 제로 검증 · 롤백 시간 10초 이내 검증
- 효과: 배포 스트레스 제거 · 주간 업무시간 상시 배포 실현 및 고객 신뢰 제고

<div class="itpe-pipeline is-vertical" role="img" aria-label="무중단 배포 아키텍처 개선 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>야간 배포 의존 · DB 스키마 불일치로 인한 롤백 불가</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>Canary 자동화 파이프라인 및 Expand/Contract DB 분리</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>SLO 위반 에러율 0% · Connection Draining 및 자동 롤백</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>주간 상시 무중단 배포 달성 · 릴리스 리스크 완벽 제거</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **무중단 배포**는 구버전에서 신버전으로 전환하는 과정에서 서비스 중단 없이 트래픽을 안전하게 승계하는 배포 전략
- 목적: 24/7 서비스 고가용성 유지 및 장애 시 즉각적 롤백 환경 제공

### 2. 3대 배포 전략 요약

<div class="itpe-pipeline is-vertical" role="img" aria-label="무중단 배포 3대 전략 요약">
  <div class="itpe-pipeline-node"><strong>Rolling</strong><small>인스턴스 점진 교체 · 자원 효율</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Blue/Green</strong><small>전체 환경 일괄 스위칭 · 즉시 롤백</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Canary</strong><small>일부 트래픽 선 검증 · 점진적 확대</small></div>
</div>

### 3. 핵심 통제

- **DB 무중단**: Expand/Contract 패턴으로 하위 호환성 유지 후 구버전 컬럼 제거
- **연결 보장**: Graceful Shutdown 및 Connection Draining으로 인플라이트 요청 보존

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 1교시: 무중단 배포 전략
- 제139회 정보관리기술사 2교시: 클라우드 네이티브 배포 전략(Rolling, Blue/Green, Canary) 비교
- Sam Newman, Building Microservices (2nd Edition), Deployment Strategies

## 학습 체크

- [ ] Rolling, Blue/Green, Canary 배포 전략의 장단점을 자원과 롤백 관점에서 비교할 수 있는가?
- [ ] Expand/Contract 패턴의 3단계 수행 절차를 설명할 수 있는가?
- [ ] Graceful Shutdown과 Connection Draining이 무중단 배포에서 필수적인 이유를 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [리팩토링](./006_refactoring.md)
- 연관 토픽: [DevOps](./002_devops.md), [CI/CD](./095_ci_cd.md)
- 다음 토픽: [블랙박스 테스트](./008_black_box_test.md)
