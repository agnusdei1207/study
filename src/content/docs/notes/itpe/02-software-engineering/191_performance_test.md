---
title: "성능 테스트(Performance Test)"
category: "02-software-engineering"
tags:
  - "성능테스트"
  - "부하테스트"
  - "스트레스테스트"
  - "내구성테스트"
  - "스파이크테스트"
  - "리틀의법칙"
  - "TPS"
  - "APM"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 테스팅과 성능 엔지니어링을 거쳐 성능 테스트로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 테스팅·성능 엔지니어링</span>
  <strong>성능 테스트(Performance Test)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 실제 운영 환경에서 예상되는 다양한 트래픽 조건하에서 시스템의 응답 시간(Response Time), 처리량(TPS), 자원 사용률(CPU, 메모리, I/O)을 정량적으로 계측하여 목표 SLA/SLO 준수 여부를 검증하고, 시스템의 파괴 임계점(Breakpoint)과 인프라 병목을 선제 도출하는 비기능 테스트 엔지니어링
- 메커니즘: SLA 성능 목표 설정 $\rightarrow$ 리틀의 법칙 기반 부하 모델링 $\rightarrow$ 유형별(Load/Stress/Soak/Spike) 부하 주입 및 APM 계측 $\rightarrow$ 병목 프로파일링 및 튜닝 $\rightarrow$ 성능 기준선 확정
- 산출물: 성능 테스트 계획서 · 부하 모델 정의서 · 성능 시험 성적서(BMT Report) · 병목 구간 튜닝 권고서

<div class="itpe-flow-map" role="img" aria-label="성능 테스트 추진 절차 및 성능 게이트 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 성능 목표(SLA) 정의 및 부하 모델링</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>모델링</strong><span>피크 TPS, 목표 응답시간, 동시 사용자(VUser) 규모 수학적 산정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 부하 시나리오 스크립팅</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>스크립트</strong><span>사용자 체류 시간(Think Time)을 반영한 k6/JMeter 테스트 코드 작성</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 유형별 부하 주입 및 APM 심층 계측</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>주입</strong><span>Load, Stress, Soak, Spike 부하 인가 및 DB 락, JVM 힙 메모리 추적</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 성능 기준선 적합성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>최대 부하 시 TPS가 유지되고 95th 백분위 응답시간이 SLA를 만족하며 자원 누수가 없는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (성능 Baseline 충족)</strong>
      <span>운영 환경 배포 승인 $\rightarrow$ 인프라 적정 사이징 확정 및 오픈 준비 완결</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (임계점 초과 / OOM 발생)</strong>
      <span>배포 차단 $\rightarrow$ HikariCP 풀 튜닝, 슬로우 쿼리 인덱싱, 캐시 계층 추가</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **처리량(TPS, Transactions Per Second)**: 시스템이 단위 시간(1초)당 에러 없이 정상적으로 처리해 낸 트랜잭션의 완료 건수
- **임계점(Breakpoint)**: 부하가 증가함에 따라 TPS가 더 이상 증가하지 않고 수평 정체되거나 급감하며, 응답 시간이 기하급수적으로 폭증하기 시작하는 성능 한계점
- **리틀의 법칙(Little's Law)**: 안정적인 시스템에서 체류하는 평균 고객 수($N$)는 고객의 평균 도착률($\lambda$, TPS)과 시스템 내 평균 체류 시간($W$, 응답시간 + Think Time)의 곱과 같다는 이론 ($N = \text{TPS} \times (\text{Response Time} + \text{Think Time})$)
- **가상 사용자(VUser)**: 실제 사용자처럼 로그인, 검색, 주문 등 일련의 시나리오를 반복 수행하며 서버에 트래픽 부하를 생성하는 논리적 스레드 단위
</details>

## 1. 개요 및 필요성

### 기능 검증의 맹점과 프로덕션 대형 장애 방지

단위 및 기능 테스트를 완벽히 통과한 시스템이라도 동시 접속자가 1만 명으로 치솟는 순간 데이터베이스 커넥션 고갈, 쓰레드 락 경합, 메모리 누수로 인해 시스템 전체가 다운된다.

성능 테스트는 시스템이 감당할 수 있는 **최대 용량과 한계 임계점(Breakpoint)**을 사전에 파악하여, 프로덕션 릴리스 전 인프라 사이징을 검증하고 서비스 장애를 원천 예방하는 핵심 신뢰성 엔지니어링이다.

### 성능 테스트 4대 주요 유형 비교

| 구분 | 부하 테스트 (Load Test) | 스트레스 테스트 (Stress Test) | 내구성 테스트 (Soak/Endurance) | 스파이크 테스트 (Spike Test) |
|---|---|---|---|---|
| **부하 수준** | **예상되는 최대 정상 부하 (100%)** | **임계치를 초과하는 극한 부하 (150%~300%)** | 평균 운영 수준 부하 (70%~80%) | **순간적으로 급증하는 초과 부하** |
| **수행 시간** | 1시간 ~ 4시간 | 30분 ~ 1시간 (단기 집중) | **24시간 ~ 수일간 장기 실행** | 수 분 ~ 수십 분 |
| **주요 목적** | 목표 SLA/SLO 달성 여부 검증 | **시스템 파괴 시점(임계점) 및 복원력 측정** | **메모리 누수(OOM), 자원 누수 감지** | 버퍼 오버플로우, 오토스케일링 민첩성 |
| **검증 결함** | 쿼리 병목, 쓰레드 풀 부족 | 서킷 브레이커 미작동, 페일오버 실패 | JVM Full GC 빈도 증가, 세션 미반환 | 인스턴스 패닉 다운, 메시지 큐 지연 |

## 2. 아키텍처 및 핵심 메커니즘

### 4대 성능 테스트 부하 프로파일 (Load Profile)

```text
+-------------------------------------------------------------------------+
|                  성능 테스트 유형별 부하 주입 프로파일 (Load Profile)     |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 1. 부하(Load) ]      [ 2. 스트레스(Stress) ]  [ 3. 내구성(Soak) ]    |
|    트래픽                 트래픽 (임계초과)        트래픽                |
|      ┌────┐                    ▲                    ┌──────────┐        |
|      │    │                  ┌─┘                  ┌─┘          │        |
|    ──┘    └───             ──┘                    │            │        |
|    (정상 최대 부하)         (시스템 한계 측정)      (장시간 메모리 누수) |
|                                                                         |
|  [ 4. 스파이크(Spike) ]                                                 |
|    트래픽 (순간폭증)        * 리틀의 법칙:                               |
|        ┌┐                     VUser = TPS × (응답시간 + Think Time)     |
|        ││                   * 임계점 도출:                               |
|    ────┘└───                  TPS 정체 & 응답시간 급증 지점 포착        |
+-------------------------------------------------------------------------+
```

### 성능 측정 4대 핵심 지표

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 처리량 (TPS)</strong></span>
      <span class="itpe-badge">처리 성능</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>초당 완결된 비즈니스 트랜잭션 건수</li>
        <li>부하 증가에도 TPS가 선형 증가하는지 여부 확인</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 응답 시간 (Latency)</strong></span>
      <span class="itpe-badge">속도 측정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>요청 전송부터 응답 수신 완료까지의 소요 시간</li>
        <li>평균치 대신 p95, p99 백분위수(Percentile) 중심 평가</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 자원 사용률</strong></span>
      <span class="itpe-badge">효율성 계측</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>CPU 점유율, 메모리 사용량, 디스크 I/O 대기율, 네트워크 대역</li>
        <li>피크 부하 시 하드웨어 자원 임계치(70%) 유지 여부 확인</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 에러율 (Error Rate)</strong></span>
      <span class="itpe-badge">안정성 평가</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>HTTP 5xx 에러, 소켓 타임아웃, 커넥션 리셋 발생 비율</li>
        <li>허용 에러율 0.1% 이하 통제 기준 검증</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 부하 증가 시 TPS가 정체되고 504 타임아웃이 속출하여 WAS 전체 대기열 적체 | HikariCP 커넥션 풀 크기 튜닝, 슬로우 쿼리 복합 인덱싱 및 Redis 캐시 계층 도입 | 응답 지연 80% 단축 및 안정적 TPS 유지 |
| 24시간 장기 내구성(Soak) 테스트 중 JVM 힙 메모리 고갈로 인한 OutOfMemoryError 크래시 | Eclipse MAT 기반 힙 덤프 정밀 분석, 미해제 정적 컬렉션 객체 제거 및 캐시 TTL 설정 | 장기 무장애 연속 가동성 100% 보장 |
| 예산 부족으로 테스트 서버 사양이 운영 서버의 1/4에 불과하여 성능 측정 결과 왜곡 | 클라우드 오토스케일링을 활용하여 테스트 시간 동안만 운영 동등 사양 인프라 프로비저닝 | 실제 운영 부하 환경과 100% 일치하는 신뢰성 확보 |

## 4. 기술사 답안 차별화 포인트

### Shift-Left 성능 테스트와 "Performance-as-Code"

프로젝트 종료 직전에야 부하를 걸어보다가 구조적 아키텍처 결함으로 오픈이 연기되는 참사를 방지하기 위해 **'Shift-Left 지속적 성능 테스트'**를 도입해야 한다. **k6나 Locust**를 활용하여 부하 테스트 시나리오를 소스코드와 함께 Git 저장소에 버전 관리(Performance-as-Code)하고, 매 스프린트 또는 PR(Pull Request) 머지 시 주요 API의 응답시간 회귀를 자동 검증하는 **CI/CD 성능 게이트**를 운영 모델로 제시한다.

### 분산 추적(OpenTelemetry) 및 APM과의 심층 결합

단순 부하 생성 도구만으로는 어느 마이크로서비스의 어떤 DB 쿼리가 병목인지 알 수 없다. 부하 테스트 실행 시 **OpenTelemetry 기반 분산 추적(Trace ID 전파)**을 통해 수십 개 마이크로서비스 간의 병목 구간을 나노초 단위로 시각화하고 즉각 격리하는 실무 아키텍트의 성능 엔지니어링 역량을 결론으로 강조한다.

## 5. 참고 및 연계 학습

- [성능 요구사항(Performance Requirement)](./149_performance_requirement.md)
- [웹 성능 최적화](./164_web_performance_optimization.md)
- [카오스 테스트(Chaos Test)](./176_chaos_test.md)
- [통합 테스트(Integration Test)](./179_integration_test.md)
