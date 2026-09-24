---
sidebar:
  order: 123
  label: "123. 대기행렬이론 (Queuing Theory)"
  badge:
    text: "기초"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 123
title: "대기행렬이론(Queuing Theory) 구조와 켄달 표기법 및 리틀의 법칙 기반 시스템 사이징"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "123"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>통계·데이터 분석</span><strong>대기행렬이론</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 260" width="100%" height="260" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Arrival Process -->
  <rect x="15" y="40" width="110" height="90" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="70" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">도착 과정 (A)</text>
  <text x="70" y="88" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">포아송 도착</text>
  <text x="70" y="108" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">도착률 λ</text>

  <path d="M 125 85 L 165 85" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow123)"/>

  <!-- Queue Buffer -->
  <rect x="165" y="40" width="150" height="90" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="240" y="65" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">대기열 (Queue)</text>
  <!-- Queue Slots -->
  <g fill="#ffffff" stroke="#f59e0b" stroke-width="1">
    <rect x="180" y="78" width="22" height="35" rx="3"/>
    <rect x="206" y="78" width="22" height="35" rx="3"/>
    <rect x="232" y="78" width="22" height="35" rx="3"/>
    <rect x="258" y="78" width="22" height="35" rx="3"/>
    <rect x="284" y="78" width="22" height="35" rx="3"/>
  </g>
  <text x="240" y="122" text-anchor="middle" font-size="9" fill="#78350f">용량 K / 서비스 규율 Z(FIFO)</text>

  <path d="M 315 85 L 355 85" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow123)"/>

  <!-- Service Facility -->
  <rect x="355" y="25" width="150" height="120" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="430" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">서비스 창구 (B, c)</text>
  <rect x="375" y="58" width="110" height="30" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1"/>
  <text x="430" y="78" text-anchor="middle" font-size="11" fill="#065f46">서버 1 (처리율 μ)</text>
  <rect x="375" y="98" width="110" height="30" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1"/>
  <text x="430" y="118" text-anchor="middle" font-size="11" fill="#065f46">서버 c (처리율 μ)</text>

  <!-- Bottom Kendall & Little Summary -->
  <rect x="15" y="165" width="490" height="80" rx="6" fill="#f8fafc" stroke="#94a3b8" stroke-width="1"/>
  <text x="30" y="190" font-size="11" font-weight="bold" fill="#1e293b">켄달 표기법: [ A / B / c / K / m / Z ] (예: M / M / 1 / ∞ / ∞ / FIFO)</text>
  <text x="30" y="210" font-size="11" fill="#334155">리틀의 법칙(Little's Law): L = λW, Lq = λWq (안정 상태 ρ = λ/cμ &lt; 1 필수)</text>
  <text x="30" y="230" font-size="10" fill="#dc2626">주의: 이용률 ρ &gt; 80% 초과 시 대기시간 Wq가 1/(1-ρ)에 의해 기하급수적으로 폭증</text>

  <defs>
    <marker id="arrow123" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **불규칙하게 유입되는 서비스 요청의 도착 과정(Arrival), 대기열(Queue), 서버의 처리 용량(Service)을 확률 모형으로 정량화하여 시스템의 평균 대기시간, 큐 적체량, 적정 서버 용량(Sizing)을 수학적으로 산출하는 대기 네트워크 이론**
- 암기: `도-대-서-규` (대기행렬 4대 요소: 도착 과정, 대기열, 서비스 창구, 서비스 규율) / `에-비-씨-케이-엠-지` (켄달 표기법: A/B/c/K/m/Z) / `엘-람-더블유` (리틀의 법칙: $L = \lambda W$)
- 판단축:
  - **M/M/1**: 단일 서버 지수형 모델, 연산 공식이 가장 단순하여 개략적 사이징에 활용
  - **M/M/c**: 다중 병렬 서버 모델, 스케일아웃 및 로드밸런서 환경의 표준 분석 모형
  - **M/G/1**: 임의의 일반 서비스 시간 분포(분산 $\sigma^2$ 반영, Pollaczek-Khinchine 공식)
- 주의: 이용률($\rho$)이 1에 가까워지면 대기시간이 급격히 늘 수 있으나, 적정 이용률은 도착 변동성·서비스시간 분포·서비스 목표·증설 비용을 함께 고려해 산정
---

## 1교시 예상문제 (10점)

> 대기행렬이론(Queuing Theory) 구조와 켄달 표기법 및 리틀의 법칙 기반 시스템 사이징의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 서비스 요청의 도착률($\lambda$)과 처리율($\mu$)의 확률적 관계를 수학적으로 모델링하여 평균 대기시간 및 적정 서버 용량을 산정하는 이론 |
| **2. 켄달 표기법** | $[A / B / c / K / m / Z]$ (도착 분포 / 서비스 시간 분포 / 병렬 서버 수 / 시스템 용량 / 모집단 / 서비스 규율) |
| **3. 리틀의 법칙** | - 수식: $L = \lambda W, \quad L_q = \lambda W_q$<br/>- 의미: 시스템 내 평균 고객 수는 도착률과 평균 체류 시간의 곱과 항상 일치 |
| **4. 시스템 사이징** | 이용률이 1에 가까워질수록 대기시간이 민감하게 증가하므로 부하 변동과 서비스 목표를 반영해 용량 검토 |
---

### 핵심 관계

| 구성요소 | 핵심 특성 | IT 시스템 매핑 예시 |
|:---|:---|:---|
| **1. 도착 과정 (Arrival)** | 단위 시간당 평균 도착률 $\lambda$ (포아송 과정, 도착 간격은 지수분포) | 웹 클라이언트의 초당 HTTP API 요청 수(RPS) |
| **2. 대기열 (Queue)** | 서비스 대기 공간의 최대 수용 용량($K$) 및 유한/무한 여부 | 톰캣의 acceptCount, 운영체제의 TCP 백로그 큐 |
| **3. 서비스 창구 (Service)** | 서비스 처리율 $\mu$ (평균 서비스 시간 $1/\mu$) 및 병렬 서버 수($c$) | 웹 애플리케이션 서버(WAS)의 워커 스레드 풀, 컨테이너 Pod 수 |
| **4. 서비스 규율 (Discipline)** | 큐에 대기 중인 요청을 처리하는 우선순위 규칙 | FIFO(선입선출), LIFO, 우선순위 큐(Priority), 라운드로빈 |

---

## 2~4교시 예상문제 (25점)

> 대기행렬이론(Queuing Theory)의 기본 구조와 켄달의 표기법(Kendall's Notation)을 기술하고, 리틀의 법칙(Little's Law)의 수식 및 IT 시스템 성능 용량 산정(Capacity Sizing)에서의 활용 방안을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. IT 시스템의 병목을 수학적으로 예측하는 대기행렬이론 개요

#### 한줄 요약: 서비스 요청의 유입률과 처리율의 확률적 불일치로 발생하는 대기 지연을 수학적으로 모델링하여 최적 자원 용량을 설계하는 이론

- **배경**:
  - 아무리 평균 서버 처리 속도가 고객 도착 속도보다 빠르더라도, 트래픽 유입의 확률적 요동(Burstiness) 때문에 일시적 대기열 적체와 지연 발생
  - 무작정 서버를 과다 증설하면 비용이 낭비되고, 축소하면 큐가 폭발하여 타임아웃 장애가 발생하는 딜레마 직면
- **정의**: 무작위로 도착하는 고객(요청)과 이들을 처리하는 서비스 시설 간의 대기 현상을 마르코프 연쇄(Markov Chain)와 확률 과정으로 분석하는 수리통계학 이론
- **목적**: 이용률($\rho$), 평균 대기시간($W_q$), 평균 큐 길이($L_q$)를 추정해 목표 응답시간과 부하 조건에 맞는 용량 검토

### Ⅱ. 대기행렬 시스템의 4대 핵심 구성요소

#### 한줄 요약: 도착 과정, 대기 공간, 서비스 창구, 서비스 규율의 상호작용 체계

| 구성요소 | 핵심 특성 | IT 시스템 매핑 예시 |
|:---|:---|:---|
| **1. 도착 과정 (Arrival)** | 단위 시간당 평균 도착률 $\lambda$ (포아송 과정, 도착 간격은 지수분포) | 웹 클라이언트의 초당 HTTP API 요청 수(RPS) |
| **2. 대기열 (Queue)** | 서비스 대기 공간의 최대 수용 용량($K$) 및 유한/무한 여부 | 톰캣의 acceptCount, 운영체제의 TCP 백로그 큐 |
| **3. 서비스 창구 (Service)** | 서비스 처리율 $\mu$ (평균 서비스 시간 $1/\mu$) 및 병렬 서버 수($c$) | 웹 애플리케이션 서버(WAS)의 워커 스레드 풀, 컨테이너 Pod 수 |
| **4. 서비스 규율 (Discipline)** | 큐에 대기 중인 요청을 처리하는 우선순위 규칙 | FIFO(선입선출), LIFO, 우선순위 큐(Priority), 라운드로빈 |

### Ⅲ. 켄달의 표기법 (Kendall's Notation)

#### 한줄 요약: 대기행렬 모형의 특성을 6개의 표준 기호 $[A / B / c / K / m / Z]$로 규격화한 표기법

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 120" width="100%" height="120" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Six Slots -->
  <g fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5">
    <rect x="20" y="30" width="70" height="60" rx="6"/>
    <rect x="100" y="30" width="70" height="60" rx="6"/>
    <rect x="180" y="30" width="70" height="60" rx="6"/>
    <rect x="260" y="30" width="70" height="60" rx="6"/>
    <rect x="340" y="30" width="70" height="60" rx="6"/>
    <rect x="420" y="30" width="70" height="60" rx="6"/>
  </g>
  <text x="55" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">A</text>
  <text x="55" y="75" text-anchor="middle" font-size="9" fill="#334155">도착 분포</text>

  <text x="135" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">B</text>
  <text x="135" y="75" text-anchor="middle" font-size="9" fill="#334155">서비스 분포</text>

  <text x="215" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">c</text>
  <text x="215" y="75" text-anchor="middle" font-size="9" fill="#334155">서버 개수</text>

  <text x="295" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">K</text>
  <text x="295" y="75" text-anchor="middle" font-size="9" fill="#334155">시스템 용량</text>

  <text x="375" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">m</text>
  <text x="375" y="75" text-anchor="middle" font-size="9" fill="#334155">모집단 크기</text>

  <text x="455" y="55" text-anchor="middle" font-size="14" font-weight="bold" fill="#1d4ed8">Z</text>
  <text x="455" y="75" text-anchor="middle" font-size="9" fill="#334155">서비스 규율</text>
</svg>
</div>

1. **A (도착 분포)**: $M$(Markovian, 포아송 도착), $D$(Deterministic, 고정 주기), $G$(General, 일반 분포)
2. **B (서비스 시간 분포)**: $M$(지수분포), $D$(고정 시간), $G$(일반 분포)
3. **c (병렬 서버 수)**: $1, 2, \dots, c$ (처리 창구의 개수)
4. **K (시스템 수용 용량)**: 대기열과 서버를 포함한 최대 수용량 (생략 시 $\infty$)
5. **m (모집단 크기)**: 잠재 고객의 총원 (생략 시 $\infty$)
6. **Z (서비스 규율)**: FIFO(선입선출), LIFO, PRI(우선순위), SIRO(무작위) (생략 시 FIFO)

### Ⅳ. 리틀의 법칙 (Little's Law) 및 M/M/1 핵심 공식

#### 한줄 요약: 시스템 체류 수($L$)는 도착률($\lambda$)과 체류 시간($W$)의 곱과 같으며, 이용률($\rho$)이 1에 근접하면 대기시간이 폭발함

1. **리틀의 법칙 (Little's Law)**:
   - 시스템이 장기적으로 안정된 조건에서 평균 개체 수와 평균 체류 시간, 유효 도착률의 관계를 나타내는 법칙

$$L = \lambda W, \quad L_q = \lambda W_q$$

   - $L$: 시스템 내 평균 총 고객 수 (대기열 + 서비스 중)
   - $L_q$: 대기열(Queue)에서 순수하게 기다리는 평균 고객 수
   - $W$: 고객이 시스템에 머무는 평균 총 체류 시간 ($W = W_q + 1/\mu$)
   - $W_q$: 대기열에서 순수하게 기다리는 평균 대기시간
2. **M/M/1 기본 모형의 주요 성능 지표**:
   - 시스템 이용률 ($\rho$, Server Utilization):

$$\rho = \frac{\lambda}{\mu} \quad (\text{안정 상태 조건: } \rho < 1)$$

   - 평균 시스템 체류 고객 수: $L = \frac{\rho}{1 - \rho} = \frac{\lambda}{\mu - \lambda}$
   - 평균 대기열 고객 수: $L_q = \frac{\rho^2}{1 - \rho}$
   - 평균 대기시간: $W_q = \frac{L_q}{\lambda} = \frac{\rho}{\mu(1 - \rho)}$
   - 평균 시스템 체류시간: $W = \frac{L}{\lambda} = \frac{1}{\mu(1 - \rho)}$

### Ⅴ. M/M/1 vs M/M/c vs M/G/1 3대 대기 모형 비교

#### 한줄 요약: 단일 서버의 기본형 M/M/1, 병렬 분산의 M/M/c, 서비스 편차를 반영한 M/G/1

| 비교 항목 | M/M/1 | M/M/c | M/G/1 |
|:---|:---|:---|:---|
| **서버 구조** | 단일 서버 ($c=1$) | **다중 병렬 서버 ($c > 1$)** | 단일 서버 ($c=1$) |
| **서비스 시간** | 지수분포 (메모리리스) | 지수분포 (동일한 $\mu$) | **일반 임의 분포 (평균 $1/\mu$, 분산 $\sigma^2$)** |
| **이용률 정의** | $\rho = \lambda / \mu$ | $\rho = \lambda / (c \mu)$ | $\rho = \lambda / \mu$ |
| **특징 및 한계** | 수식이 가장 단순함 | 단일 대기열을 공유하는 은행 창구 모형 | 서비스 시간 편차가 대기시간에 미치는 영향 분석 |
| **핵심 공식** | $L_q = \frac{\rho^2}{1-\rho}$ | Erlang-C 공식을 통한 대기 확률 산출 | **P-K 공식**: $L_q = \frac{\lambda^2 \sigma^2 + \rho^2}{2(1-\rho)}$ |
| **실무 적용** | 단일 DB 인스턴스 질의 처리 | **로드밸런서 뒷단의 웹 서버/WAS 클러스터** | 페이로드 크기에 따라 처리시간이 요동치는 API |

### Ⅵ. 실무 인프라 사이징 및 트러블슈팅

#### 한줄 요약: 이용률 $\rho > 80\%$ 초과 방지, 카프카 컨슈머 랙(Lag) 제어, 오토스케일링 임계치 설정

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **CPU 85% 도달 시 급작스러운 504 타임아웃** | 이용률 $\rho$가 1에 근접하면서 대기시간 $W_q$가 분모 $(1-\rho)$로 인해 지수함수 폭증 | 오토스케일링 목표 CPU를 **70%**로 낮추고, 큐 깊이(Queue Depth) 지표를 복합 메트릭으로 설정 |
| **메시지 브로커 컨슈머 랙(Lag) 누적** | 생산자 발행률($\lambda$)이 단일 컨슈머 처리율($\mu$)을 초과하여 $\rho > 1$ 발산 | 파티션 개수와 컨슈머 Pod 수를 $c$개로 동시 확장하여 $\rho = \lambda / (c\mu) \le 0.6$ 유지 |
| **스레드 풀 고갈 및 Connection Drop** | 순간 트래픽 버스트로 인해 M/M/1/K 시스템의 큐 용량 $K$ 초과 | 서킷 브레이커(Resilience4j)를 연계하여 큐 초과 시 즉각적인 Fail-fast 및 대체 응답(Fallback) 반환 |

### Ⅶ. 기술사적 제언

### 실전 답안용 기술사적 제언

- **판정**: 대규모 트랜잭션 시스템에서 SLA 응답 지연을 방지하고 인프라 비용을 최적화하기 위해 대기행렬이론 기반 용량 산정이 필수적임.
- **대응**:
  1. **골디락스 이용률 준수**: 상시 시스템 이용률($\rho$)을 70% 이하로 통제하여 버스트 트래픽에 대한 쿠션 확보.
  2. **M/M/c 병렬 확장 설계**: 쿠버네티스 Pod 및 메시지 컨슈머를 다중 채널($c$)로 구성하여 전체 처리율 증대.
  3. **리틀의 법칙 기반 HPA**: Pod 오토스케일링 메트릭으로 단순 CPU 대신 $L_q$(대기열 적체 수) 지표를 연동.
- **검증**: 성능 부하 테스트(nGrinder/k6) 시 P99 응답시간 200ms 이내 및 큐 적체 제로 확인.
- **효과**: 피크 트래픽 타임아웃 장애 원천 차단 및 인프라 오버프로비저닝 비용 30% 절감.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">서버 이용률 90% 초과 시 대기시간 지수 폭발 및 504 타임아웃</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">대기행렬 수식 기반 사이징, 이용률 70% 상한, M/M/c 확장</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">리틀의 법칙 L = λW 검증, 피크 부하 시 이용률 ρ &lt; 0.8 유지</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">SLA 응답속도 준수 및 무장애 고가용성 서비스 환경 실현</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제120회 정보관리 2교시: 대기행렬이론(Queuing Theory)의 기본 구조, 켄달의 표기법(Kendall's Notation), 리틀의 법칙(Little's Law)
- **검증 출처**:
  - Leonard Kleinrock, "Queueing Systems: Volume I - Theory", Wiley-Interscience
  - John D. C. Little, "A Proof for the Queuing Formula: L = λW", Operations Research
---

## 연결 토픽

- 상위 토픽: [03-036 기술통계](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/036_descriptive_statistics.md)
- 연관 토픽: [03-109 신뢰도 분석](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/109_reliability.md), [05-001 이동통신 및 무선 네트워크](file:///C:/workspace/study/src/content/docs/notes/itpe/05-network/001_mobile_communication.md)
