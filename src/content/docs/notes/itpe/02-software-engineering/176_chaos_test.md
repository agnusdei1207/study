---
title: "카오스 테스트(Chaos Test)"
category: "02-software-engineering"
tags:
  - "카오스테스트"
  - "카오스엔지니어링"
  - "ChaosEngineering"
  - "회복탄력성"
  - "폭발반경"
  - "서킷브레이커"
  - "넷플릭스"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 테스팅과 회복탄력성 엔지니어링을 거쳐 카오스 테스트로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 테스팅·회복탄력성 엔지니어링</span>
  <strong>카오스 테스트(Chaos Test)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 분산 클라우드 환경에서 하드웨어 고장, 네트워크 지연, 인스턴스 크래시 등 불가피한 돌발 결함이 발생했을 때 시스템이 연쇄 장애로 붕괴하지 않고 스스로 복구하는지 검증하기 위해, 운영 및 유사 환경에 제어된 장애를 선제적으로 주입하여 시스템의 회복 탄력성(Resilience)을 실증하는 실험적 테스팅 기법
- 메커니즘: 비즈니스 정상 상태(Steady State) 정의 $\rightarrow$ 장애 내결함 가설 수립 $\rightarrow$ 최소 폭발 반경(Blast Radius) 내 장애 주입 실험 $\rightarrow$ 지표 관측 및 자가 치유 판정 $\rightarrow$ 취약점 개선
- 산출물: 카오스 실험 계획서 · 정상 상태 메트릭 정의서 · 회복력 검증 리포트 · 긴급 중단 롤백 절차서

<div class="itpe-flow-map" role="img" aria-label="카오스 엔지니어링 4단계 실험 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 정상 상태(Steady State) 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>계측</strong><span>초당 주문 성공 건수, p99 응답시간 등 정상 작동 대변 지표 확정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 가설 수립 및 폭발 반경 통제</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설계</strong><span>"결제 파드 1개가 급사해도 전체 결제 성공률은 99.9% 유지된다" 가설</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 통제된 결함 주입 (Fault Injection)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>주입</strong><span>Chaos Mesh/Litmus 기반 파드 강제 종료 및 500ms 네트워크 지연 발생</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 회복 탄력성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>서킷 브레이커와 오토스케일링이 작동하여 정상 상태 메트릭을 유지하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (가설 검증 성공)</strong>
      <span>자가 치유 확인 $\rightarrow$ 회복 탄력성 Baseline 승인 및 정기 자동화 실험 등록</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (연쇄 장애 전파)</strong>
      <span>비상 중단(Rollback) 즉각 발동 $\rightarrow$ 타임아웃/서킷 브레이커 설정 재설계</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Steady State(정상 상태)**: 시스템이 장애 없이 정상적으로 비즈니스를 수행하고 있음을 객관적으로 나타내는 측정 가능한 비즈니스 메트릭(예: 초당 결제 트랜잭션 수)
- **Blast Radius(폭발 반경)**: 카오스 장애 주입 시 실제 사용자나 연계 시스템에 미칠 수 있는 피해의 물리적·논리적 영향 범위
- **Resilience(회복 탄력성)**: 시스템에 예기치 않은 오류, 고장, 부하가 발생하더라도 기능을 정상 유지하거나 스스로 신속하게 원래 상태로 복구하는 능력
- **Simian Army**: 넷플릭스에서 개발한 카오스 도구군으로, Chaos Monkey(서버 강제 종료), Chaos Gorilla(가용 영역 AZ 다운), Chaos Kong(전체 리전 다운) 등으로 구성
</details>

## 1. 개요 및 필요성

### 클라우드 복잡성과 "고장 불가피성(Design for Failure)"

수천 개의 마이크로서비스로 구성된 분산 클라우드 환경에서는 네트워크 단절, 디스크 풀, 써드파티 API 먹통 등 장애가 일상적으로 발생한다. "장애를 100% 예방할 수 있다"는 전통적 관점은 클라우드에서 완전히 붕괴되었다.

카오스 테스트는 **"장애는 반드시 발생한다"**는 전제하에, 새벽에 돌발 장애로 시스템이 터지기 전에 **업무 시간 중에 엔지니어가 모니터링하는 상태에서 고의로 장애를 터뜨려** 아키텍처의 취약점을 선제적으로 도출하는 현대적 신뢰성 공학 기법이다.

### 전통적 장애 테스트 vs 카오스 테스트 비교

| 구분 | 전통적 장애 복구 테스트 (DR Test) | 카오스 테스트 (Chaos Test) |
|---|---|---|
| **수행 환경** | 격리된 테스트베드 / 사전 공지된 모의 훈련 | **실제 운영 환경 (또는 프로덕션 동등 환경)** |
| **장애 주입 방식** | 사전에 약속된 시나리오에 따른 수작업 차단 | **자동화된 도구를 통한 무작위·돌발적 결함 주입** |
| **초점 영역** | 백업 및 수동 페일오버(Failover) 매뉴얼 검증 | **소프트웨어 아키텍처의 자가 치유(Self-Healing) 검증** |
| **수행 주기** | 연 1~2회 대규모 정기 훈련 | **CI/CD 파이프라인 연계 지속적 상시 실험** |
| **핵심 지표** | RTO(목표 복구 시간), RPO(목표 복구 시점) | **정상 상태 메트릭 변동률, 서비스 가용성(SLO)** |

## 2. 아키텍처 및 핵심 메커니즘

### 카오스 엔지니어링 4단계 실험 아키텍처

```text
+-------------------------------------------------------------------------+
|                  카오스 엔지니어링 4단계 실험 파이프라인                 |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 1. 정상 상태 정의 ]                                                  |
|    - 정상 운영을 대변하는 처리량 측정치 선정 (주문 성공률 99.9%, TPS 유지)|
|                   │                                                     |
|                   v                                                     |
|  [ 2. 가설 수립 ]                                                       |
|    - "인증 서비스 파드 3개 중 2개가 다운되어도, 세션 캐시로 정상 인가된다"|
|                   │                                                     |
|                   v                                                     |
|  [ 3. 장애 주입 실험 (최소 폭발 반경 격리) ]                           |
|    - Litmus / Chaos Mesh 도구를 통한 파드 강제 삭제 및 CPU 부하 유발   |
|    - 특정 카나리(Canary) 트래픽 영역으로만 피해 범위 제한               |
|                   │                                                     |
|                   v                                                     |
|  [ 4. 가설 검증 및 자가 치유 관측 ]                                     |
|    - 서킷 브레이커(Resilience4j) 정상 오픈 및 폴백(Fallback) 동작 확인  |
|    - 이상 발생(오류 급증) 시 비상 정지(Dead Man's Switch) 자동 롤백    |
+-------------------------------------------------------------------------+
```

### 카오스 실험 4대 핵심 구성요소

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 정상 상태 메트릭</strong></span>
      <span class="itpe-badge">기준선 정의</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>CPU 등 단순 시스템 지표가 아닌 비즈니스 트랜잭션 지표 중심</li>
        <li>Prometheus/Datadog 메트릭과 연계하여 실시간 편차 감시</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 결함 주입기 (Injector)</strong></span>
      <span class="itpe-badge">실험 유발</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>컴퓨팅 장애: 프로세스 Kill, CPU 스로틀링, 메모리 릭</li>
        <li>네트워크 장애: 패킷 드롭, 지연시간 추가, DNS 확인 실패</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 폭발 반경 제어기</strong></span>
      <span class="itpe-badge">안전 격리</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>전체 시스템이 아닌 단일 네임스페이스나 특정 카나리 파드에 한정</li>
        <li>테스트용 모의 사용자(Synthetic User) 트래픽 대상 실험</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 비상 정지 (Emergency Stop)</strong></span>
      <span class="itpe-badge">자동 원복</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>SLA/SLO 허용 오차를 벗어나는 즉시 장애 주입 프로세스 강제 종료</li>
        <li>원래 정상 상태 인프라 구성으로 자동 복구(Auto-Rollback)</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 캐시 인스턴스 강제 종료 시 백엔드 DB로 대량 조회가 직격하여 쇼핑몰 전체가 마비되는 연쇄 장애 발생 | 서킷 브레이커(Resilience4j) 오픈 및 로컬 메모리 폴백(Fallback) 캐시 자동 반환 사전 구성 | 캐시 급사 시에도 백엔드 DB 장애 전파 100% 차단 |
| 카오스 장애 주입이 통제 범위를 벗어나 실제 VIP 고객들의 결제 요청에 오류 발생 | 카나리 배포 환경 및 모의 트래픽으로 폭발 반경 격리, 임계 에러율 초과 시 자동 중단 스위치 연동 | 프로덕션 비즈니스 피해 제로화 |
| 단위 테스트 및 모니터링 체계가 미흡한 상태에서 운영 카오스 테스트를 강행하다가 대형 참사 발생 | 단계적 카오스 성숙도 모델(스테이징 검증 $\rightarrow$ CI/CD 카오스 게이트 $\rightarrow$ 운영 카오스) 정립 | 시스템 성숙도 기반의 안전한 카오스 도입 |

## 4. 기술사 답안 차별화 포인트

### 쿠버네티스 네이티브 카오스(Litmus, Chaos Mesh)와 GitOps 결합

현대 클라우드 환경에서는 카오스 실험을 수작업으로 돌리지 않는다. **LitmusChaos나 Chaos Mesh**는 카오스 실험을 쿠버네티스 CRD(Custom Resource Definition)로 선언한다. 이를 통해 **"카오스 실험 자체를 코드로 관리(Chaos-as-Code)"**하고, ArgoCD와 연계하여 매주 무작위 시간에 프로덕션 클러스터의 복원력을 지속적으로 검증하는 **GitOps 기반 카오스 자동화 파이프라인**을 답안의 차별화로 제시한다.

### 금융권 DORA(디지털 운영 탄력성) 및 전산사고 규제 대응

금융보안원 및 유럽 DORA(Digital Operational Resilience Act) 규정에 따라, 금융기관의 IT 시스템은 정기적인 위협 기반 침투 시험과 운영 탄력성 입증이 법제화되고 있다. 카오스 엔지니어링은 단순 개발 기법을 넘어 **"금융 IT 거버넌스 규제 준수와 재해 복구(DR) 실효성을 입증하는 핵심 감사 증적"**임을 결론으로 강조한다.

## 5. 참고 및 연계 학습

- [마이크로서비스 아키텍처(MSA)](./035_msa.md)
- [서비스 메시(Service Mesh)](./088_service_mesh.md)
- [성능 요구사항(Performance Requirement)](./149_performance_requirement.md)
- [성능 테스트(Performance Test)](./191_performance_test.md)
