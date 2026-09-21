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
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
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
      <strong>통과 (성능 검수 승인)</strong>
      <span>배포 기준선 통과 $\rightarrow$ 프로덕션 오픈 승인 및 모니터링 임계치 알림 연동</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (응답 지연 / 메모리 릭)</strong>
      <span>배포 보류 $\rightarrow$ APM 트레이싱 기반 슬로우 쿼리 인덱싱 및 힙 덤프 튜닝</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **리틀의 법칙(Little's Law)**: 안정된 대기행렬 시스템에서 평균 동시 접속자 수($N$)는 시스템 처리량($X$, TPS)과 평균 체류 시간($R$, 응답시간+ThinkTime)의 곱과 같다는 공식 ($N = X \times R$)
- **부하 테스트(Load Test)**: 일상적 또는 예상되는 피크 트래픽 수준에서 시스템이 계약된 SLA 성능을 안정적으로 유지하는지 검증하는 테스트
- **스트레스 테스트(Stress Test)**: 시스템의 한계 용량을 초과하는 극한의 부하를 단계적으로 인가하여 시스템이 붕괴되는 파괴 임계점(Breakpoint)과 자가 복구력을 확인하는 테스트
- **내구성 테스트(Soak/Endurance Test)**: 장시간(24시간~72시간) 동안 지속적인 부하를 가하여 메모리 누수(Memory Leak), 커넥션 풀 고갈, 디스크 풀 장애를 탐지하는 테스트
</details>

## 1. 개요 및 필요성

### 기능 검증의 맹점과 트래픽 급증 시의 파멸

단위 테스트와 통합 테스트를 100% 통과하여 기능적으로 완벽한 시스템이라도, 대규모 동시 접속자가 몰리는 순간 데이터베이스 커넥션 풀이 고갈되고 CPU 사용률이 100%를 치솟으며 서비스가 멈춰 선다.

성능 테스트는 시스템을 프로덕션에 투입하기 전, **실제 운영 환경과 동일한 부하 프로파일을 시뮬레이션하여 잠재된 자원 병목, 병목 쿼리, 락 경합(Lock Contention)을 사전에 발굴하고 해결**하는 필수 엔지니어링 공정이다.

### 성능 테스트 핵심 4대 지표

| 지표 | 단위 | 개념 및 측정 목적 |
|---|---|---|
| **처리량 (Throughput / TPS)** | Transactions Per Sec | 단위 시간(1초)당 시스템이 성공적으로 처리한 비즈니스 트랜잭션 건수 |
| **응답 시간 (Response Time)** | ms, 초 | 클라이언트가 요청을 보낸 시점부터 응답의 마지막 바이트를 수신할 때까지의 경과 시간 |
| **동시 사용자 수 (Concurrency)** | VUser (가상 사용자) | 시스템 내부에 동시에 연결되어 요청을 생성하거나 대기 중인 활성 세션 수 |
| **자원 사용률 (Resource)** | % | CPU, 메모리 힙, 디스크 I/O 대기율, 네트워크 대역폭, DB 커넥션 점유율 |

## 2. 아키텍처 및 핵심 메커니즘

### 4대 성능 테스트 유형 및 트래픽 인가 패턴

성능 테스트는 목적에 따라 부하 인가 패턴을 완전히 다르게 설계한다.

<div class="itpe-diagram-container" role="img" aria-label="부하, 스트레스, 스파이크, 내구성 4대 성능 테스트 부하 인가 곡선 비교">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: var(--color-surface, #1e293b); }
      .box { fill: var(--color-surface-card, #334155); stroke: var(--color-border, #475569); stroke-width: 1.2; rx: 5; }
      .box-active { fill: var(--color-primary-subtle, rgba(56,189,248,0.12)); stroke: var(--color-primary, #38bdf8); stroke-width: 1.5; rx: 5; }
      .title { fill: var(--color-text-strong, #f8fafc); font-family: system-ui, sans-serif; font-size: 9.5px; font-weight: 700; }
      .h-text { fill: var(--color-primary, #38bdf8); font-family: system-ui, sans-serif; font-size: 8px; font-weight: 700; }
      .text { fill: var(--color-text, #e2e8f0); font-family: system-ui, sans-serif; font-size: 7px; }
      .muted { fill: var(--color-text-muted, #94a3b8); font-family: system-ui, sans-serif; font-size: 6.2px; }
      .line-curve { stroke: #38bdf8; stroke-width: 1.8; fill: none; }
      .line-red { stroke: #ef4444; stroke-width: 1.8; fill: none; }
    </style>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">성능 테스트 4대 유형별 부하 인가 패턴 및 검증 목적</text>

  <!-- 1. Load Test -->
  <rect x="14" y="34" width="115" height="172" class="box"/>
  <text x="22" y="48" class="h-text">1. 부하 테스트 (Load)</text>
  <!-- 사다리꼴 곡선 -->
  <polyline points="24,100 45,70 95,70 115,100" class="line-curve"/>
  <text x="22" y="118" class="text">목표 SLA 용량 검증</text>
  <text x="22" y="130" class="muted">• 피크 트래픽 인가</text>
  <text x="22" y="142" class="muted">• 응답시간 SLA 준수</text>
  <text x="22" y="154" class="muted">• 병목 쿼리 조기 도출</text>
  <text x="22" y="174" class="muted">평상시 2~4시간 유지</text>

  <!-- 2. Stress Test -->
  <rect x="139" y="34" width="115" height="172" class="box-active"/>
  <text x="147" y="48" class="h-text">2. 스트레스 (Stress)</text>
  <!-- 계단식 상승 후 절벽 -->
  <polyline points="149,100 170,82 190,82 210,64 230,64 245,100" class="line-red"/>
  <text x="147" y="118" class="text">한계 임계점(Breakpoint)</text>
  <text x="147" y="130" class="muted">• 시스템 파괴점 탐색</text>
  <text x="147" y="142" class="muted">• 장애 격리 여부 확인</text>
  <text x="147" y="154" class="muted">• 부하 제거 후 자가회복</text>
  <text x="147" y="174" class="muted">최대 수용력 한계 측정</text>

  <!-- 3. Spike Test -->
  <rect x="264" y="34" width="115" height="172" class="box"/>
  <text x="272" y="48" class="h-text">3. 스파이크 (Spike)</text>
  <!-- 급격한 첨두 파형 -->
  <polyline points="274,100 310,100 320,55 330,100 370,100" class="line-curve"/>
  <text x="272" y="118" class="text">돌발 트래픽 폭증 검증</text>
  <text x="272" y="130" class="muted">• 티켓팅/선착순 이벤트</text>
  <text x="272" y="142" class="muted">• 오토스케일링 지연</text>
  <text x="272" y="154" class="muted">• 서킷브레이커 작동</text>
  <text x="272" y="174" class="muted">순간 10배 폭증 대응</text>

  <!-- 4. Soak Test -->
  <rect x="389" y="34" width="117" height="172" class="box"/>
  <text x="397" y="48" class="h-text">4. 내구성 (Soak)</text>
  <!-- 장기 평탄선 -->
  <polyline points="399,75 495,75" class="line-curve"/>
  <text x="397" y="118" class="text">장시간 누수(Leak) 검증</text>
  <text x="397" y="130" class="muted">• 메모리 릭 탐지</text>
  <text x="397" y="142" class="muted">• 커넥션 풀 고갈 추적</text>
  <text x="397" y="154" class="muted">• 디스크 로그 적재</text>
  <text x="397" y="174" class="muted">24~72시간 연속 인가</text>
</svg>
</div>

### 리틀의 법칙(Little's Law) 기반 가상 사용자 모델링

성능 테스트의 가상 사용자(VUser) 규모는 단순 추정이 아니라 리틀의 대기행렬 수식을 기반으로 산출한다.

<div class="itpe-diagram-container" role="img" aria-label="리틀의 법칙 공식 및 가상 사용자 산정 파이프라인 아키텍처">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto">
  <defs>
    <style>
      .bg { fill: var(--color-surface, #1e293b); }
      .box { fill: var(--color-surface-card, #334155); stroke: var(--color-border, #475569); stroke-width: 1.2; rx: 5; }
      .box-active { fill: var(--color-primary-subtle, rgba(56,189,248,0.12)); stroke: var(--color-primary, #38bdf8); stroke-width: 1.5; rx: 5; }
      .title { fill: var(--color-text-strong, #f8fafc); font-family: system-ui, sans-serif; font-size: 9.5px; font-weight: 700; }
      .h-text { fill: var(--color-primary, #38bdf8); font-family: system-ui, sans-serif; font-size: 8px; font-weight: 700; }
      .text { fill: var(--color-text, #e2e8f0); font-family: system-ui, sans-serif; font-size: 7px; }
      .muted { fill: var(--color-text-muted, #94a3b8); font-family: system-ui, sans-serif; font-size: 6.2px; }
    </style>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">리틀의 법칙(Little's Law)과 부하 모델링 수학적 아키텍처</text>

  <!-- 공식 상자 -->
  <rect x="16" y="34" width="488" height="52" class="box-active"/>
  <text x="26" y="52" fill="#38bdf8" font-size="10px" font-weight="bold">리틀의 법칙 공식 : N = X × (Response Time + Think Time)</text>
  <text x="26" y="68" class="text">• N (VUser: 동시 사용자 수)  |  X (Throughput: 목표 초당 트랜잭션 건수 TPS)</text>
  <text x="26" y="78" class="muted">• Response Time: 시스템 처리 응답시간  |  Think Time: 사용자가 화면을 읽고 다음 클릭까지 머무는 대기시간</text>

  <!-- 하단 3개 분석 카드 -->
  <rect x="16" y="96" width="155" height="110" class="box"/>
  <text x="24" y="112" class="h-text">1. Think Time 누락의 오류</text>
  <text x="24" y="126" class="text">사용자 체류시간을 0으로 두면</text>
  <text x="24" y="138" class="muted">VUser가 봇처럼 난사하여</text>
  <text x="24" y="150" class="muted">운영 현실과 괴리된 비정상 부하</text>
  <text x="24" y="162" class="muted">초래 ➔ 정확한 프로파일링 실패</text>
  <text x="24" y="184" class="h-text">▶ 평균 Think Time 반영 필수</text>

  <rect x="181" y="96" width="158" height="110" class="box-active"/>
  <text x="189" y="112" class="h-text">2. 성능 포화(Saturation) 구간</text>
  <text x="189" y="126" class="text">부하 증가 시 TPS 증가가 멈추고</text>
  <text x="189" y="138" class="muted">응답시간만 급격히 치솟는 지점</text>
  <text x="189" y="150" class="muted">➔ CPU/DB Lock 병목 발생</text>
  <text x="189" y="162" class="muted">➔ 시스템 최대 한계 도달</text>
  <text x="189" y="184" class="h-text">▶ 튜닝 및 스케일아웃 기준점</text>

  <rect x="349" y="96" width="155" height="110" class="box"/>
  <text x="357" y="112" class="h-text">3. 테일 레이턴시 (p99) 관리</text>
  <text x="357" y="126" class="text">단순 평균(Mean)의 왜곡 극복</text>
  <text x="357" y="138" class="muted">99%의 사용자가 겪는 지연 측정</text>
  <text x="357" y="150" class="muted">JVM Full GC, I/O 스파이크 등</text>
  <text x="357" y="162" class="muted">숨겨진 악성 지연 100% 포착</text>
  <text x="357" y="184" class="h-text">▶ SLA p95/p99 기준선 관리</text>
</svg>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 사용자 대기시간(Think Time)을 0으로 설정하여 비현실적인 기계적 트래픽으로 WAS 즉시 폭사 | 로그 분석을 통해 실제 사용자의 페이지 체류 시간(Think Time: 보통 2~5초)을 시나리오에 반영 | 현실 부하 반영률 95% 이상 및 정확한 용량 산정 |
| 단일 부하 발생기(Load Generator)의 로컬 포트 고갈(Ephemeral Port)로 인한 클라이언트 병목 | 분산 부하 분산 도구(k6 클러스터, JMeter 분산 모드)를 멀티 인스턴스로 분산 기동 | 클라이언트 측 병목 왜곡 100% 제거 |
| 단순 평균(Average) 응답시간만 측정하여 1%의 극단적 장애(p99 테일 레이턴시)를 간과 | 백분위수 지표(p95, p99)를 핵심 품질 게이트로 채택하고 APM 분산 추적 연계 | 극단적 이상치 장애 사전 적발 및 제거 |

## 4. 기술사 답안 차별화 포인트

### 지속적 성능 테스트(Continuous Performance Testing)와 Shift-Left

과거 성능 테스트는 프로젝트 오픈 2주 전에야 거행되는 '빅뱅 BMT'였다. 이 시점에 심각한 아키텍처 병목이 발견되면 설계를 뜯어고칠 시간이 없어 대형 사고로 이어졌다. 기술사 답안에서는 **GitLab CI/CD 파이프라인에 k6 코드를 통합하여 매 PR(Pull Request)마다 자동으로 마이크로 벤치마크를 수행하고, 성능이 10% 이상 저하되면 빌드를 실패시키는 Shift-Left 성능 엔지니어링**을 제시한다.

### 카오스 엔지니어링(Chaos Engineering)과의 융합

단순히 트래픽만 쏟아붓는 것은 반쪽짜리 테스트다. 실제 운영 환경에서는 트래픽이 폭증하는 와중에 데이터베이스 노드가 죽거나 네트워크 패킷 손실이 발생한다. **최대 부하(Stress) 상태에서 의도적으로 Pod를 다운시키거나 레이턴시를 주입하는 '카오스 주입 성능 테스트'**를 통해 시스템의 복원력(Resilience)을 함께 검증하는 최신 SRE 기법을 결론으로 제언한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 성능 테스트에서 가장 치명적인 실수는 '평균 응답시간의 함정'이다. 평균 1초라 해도 99%는 0.1초인데 1%가 90초 걸려서 타임아웃이 터지는 경우가 다반사다. 그래서 p95, p99 테일 레이턴시와 리틀의 법칙 기반 부하 모델링이 필수다.
- [나라면]: 1교시형 단답 시 4대 유형(Load, Stress, Spike, Soak)의 부하 패턴 곡선을 깔끔하게 그리고 리틀의 법칙($N = X \times R$)을 제시하겠다. 2교시형 출제 시에는 오픈 전 빅뱅 BMT의 한계를 지적하고, CI/CD 파이프라인에 k6를 탑재하는 Shift-Left 지속적 성능 테스트와 카오스 엔지니어링 융합 전략을 기술사적 해법으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 피크 부하 시 TPS 목표치 100% 유지, 99th 백분위 응답시간 p99 2초 이하 및 24시간 Soak 테스트 간 힙 메모리 누수 0건
- **대응 방안**: 리틀의 법칙에 기반한 현실적 부하 모델을 수립하고, CI/CD에 통합된 k6 성능 게이트와 APM 분산 추적 체계 구축
- **검증 체계**: 부하 테스트(Load) ➔ 한계 스트레스(Stress) ➔ 돌발 스파이크(Spike) ➔ 내구성(Soak) ➔ p99 테일 레이턴시 심사
- **기대 효과**: 프로덕션 오픈 후 트래픽 폭증 장애 제로화, 인프라 과다 증설 방지를 통한 클라우드 비용 30% 최적화

<div class="itpe-pipeline-container" role="img" aria-label="성능 테스트 엔지니어링 파이프라인">
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">01</div>
    <div class="itpe-pipeline-step-content">
      <strong>부하 모델링</strong>
      <span>SLA 목표 및 리틀의 법칙 기반 VUser/ThinkTime 산정</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">02</div>
    <div class="itpe-pipeline-step-content">
      <strong>시나리오 스크립팅</strong>
      <span>k6 분산 스크립트 작성 및 테스트 데이터 프로비저닝</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">03</div>
    <div class="itpe-pipeline-step-content">
      <strong>4대 유형 부하 주입</strong>
      <span>Load/Stress/Spike/Soak 인가 및 APM 풀스택 계측</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">04</div>
    <div class="itpe-pipeline-step-content">
      <strong>p99 품질 게이트</strong>
      <span>테일 레이턴시 및 메모리 릭 검증 후 릴리스 승인</span>
    </div>
  </div>
</div>

## 5. 참고 및 연계 학습

- [웹 성능 최적화](./164_web_performance_optimization.md)
- [카오스 테스트(Chaos Engineering)](./176_chaos_test.md)
- [성능 요구사항(SEI 시나리오)](./149_performance_requirement.md)
- [통합 테스트(Integration Test)](./179_integration_test.md)
