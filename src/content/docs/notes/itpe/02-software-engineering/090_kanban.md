---
title: "칸반(Kanban)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "Gemini 3.8 Flash (High)"
author: "Antigravity"
lastModified: "2026-03-30T10:00:00+09:00"
---

## 큰 그림과 30초 인출

- **본질**: 업무 단계를 보드에 시각화하고 동시에 진행 가능한 작업량(WIP)을 강제로 제한하여, 멀티태스킹 병목을 제거하고 작업 완료(Lead Time)를 앞당기는 린(Lean) 기반 지속 흐름 관리 기법이다.
- **메커니즘**: 백로그 $\rightarrow$ 분석 $\rightarrow$ 개발 $\rightarrow$ 테스트 $\rightarrow$ 완료 흐름에서 칼럼별 최대 허용 개수(WIP Limit)를 설정하고, 병목 발생 시 신규 착수를 중단(Stop Starting)하고 기존 작업을 완료(Start Finishing)하는 풀(Pull) 방식으로 운영한다.
- **산출물**: 칸반 보드(Kanban Board), 누적 흐름 다이어그램(CFD), 리드 타임/사이클 타임 분포도, 완료의 정의(DoD) 정책 문서.

<div class="itpe-flow">
  <div class="itpe-flow-steps">
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>1. 백로그 시각화</strong></span>
      <div class="itpe-step-detail">전체 작업 카드 가시화 및 우선순위 정렬</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>2. WIP 제한 통제</strong></span>
      <div class="itpe-step-detail">칼럼별 동시 처리 상한선(WIP Limit) 강제 설정</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>3. 풀(Pull) 기반 실행</strong></span>
      <div class="itpe-step-detail">후속 단계 여유 발생 시에만 작업을 당겨와 착수</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node is-current">
      <span class="itpe-keyword"><strong>Quality Gate</strong></span>
      <div class="itpe-step-detail"><strong>판정 질문</strong><span>목표 단계 WIP에 여유가 있고 선행 완료 조건(DoD)을 충족하는가?</span></div>
      <div class="itpe-flow-branches">
        <div class="itpe-flow-branch"><strong>통과</strong><span>다음 단계로 카드 이동 및 지속 흐름 유지</span></div>
        <div class="itpe-flow-branch"><strong>미통과</strong><span>신규 착수 차단 및 병목 구간 전원 협업(Swarming)</span></div>
      </div>
    </div>
  </div>
</div>

---

## 핵심 메커니즘

### (1) 칸반의 4대 핵심 실천 원칙 (David J. Anderson)
1. **업무 흐름의 시각화 (Visualize the Flow)**: 백로그부터 완료까지 모든 작업 카드를 보드에 가시화하여 정체 지점을 즉각 식별한다.
2. **진행 중 작업 제한 (Limit WIP)**: 각 칼럼(단계)마다 동시에 처리할 수 있는 최대 작업 수 상한선을 설정하여 컨텍스트 스위칭 낭비를 제거한다.
3. **흐름 관리 및 측정 (Manage Flow)**: 누적 흐름 다이어그램(CFD)과 리드 타임을 모니터링하여 흐름의 정체를 선제적으로 해소한다.
4. **프로세스 정책의 명시화 (Make Policies Explicit)**: 각 단계의 진입 및 완료 기준(Definition of Done), 긴급 장애 처리 우선순위 정책을 명문화한다.

### (2) 리틀의 법칙(Little's Law)과 공학적 의미
- 대기행렬 이론(Queueing Theory)에 기반하며, 시스템 내 평균 체류 작업 수(WIP)는 평균 처리율(Throughput, $\lambda$)과 체류 시간(Lead Time, $W$)의 곱과 같다:
  $$\text{WIP} = \text{Throughput} \times \text{Lead Time} \quad \Longleftrightarrow \quad \text{Lead Time} = \frac{\text{WIP}}{\text{Throughput}}$$
- **공학적 통찰**: 처리율(Throughput)이 일정한 조직에서 리드 타임을 절반으로 단축하려면, 인력을 2배 늘리기보다 **현재 진행 중인 작업(WIP)의 상한선을 절반으로 축소하는 것이 가장 경제적이고 확실한 해법**이다.

### (3) 칸반(Kanban) vs 스크럼(Scrum) 상세 비교

| 비교 항목 | 칸반 (Kanban) | 스크럼 (Scrum) |
|---|---|---|
| **반복 주기** | **주기 없음 (지속적 흐름, Continuous Flow)** | **고정 타임박스 (1~4주 스프린트)** |
| **작업 인도 방식** | 기능 완료 즉시 수시 배포 (On-Demand) | 스프린트 종료 시점 일괄 데모 및 릴리스 |
| **역할 정의** | 별도 역할 규정 없음 (기존 팀 구조 유지) | 스크럼 마스터, 제품 책임자(PO), 개발팀 |
| **주요 통제 메커니즘**| **WIP (진행 중 작업) 상한선 제한** | **스프린트 타임박스 및 계획된 백로그** |
| **신규 요구 수용** | WIP 슬롯에 여유가 생기면 언제든 즉시 풀(Pull) | 스프린트 진행 도중 신규 요구 원칙적 변경 금지 |
| **주요 측정 지표** | 사이클 타임, 리드 타임, CFD 누적 흐름도 | 스프린트 속도(Velocity), 번다운 차트(Burndown) |
| **적합한 도메인** | **운영 유지보수, 핫픽스 대응, 지속 배포 DevOps** | **신규 제품 개발, 목표 범위가 명확한 프로젝트** |

---

## 실무 적용 및 도입 체크리스트

1. **칼럼별 합리적 WIP 설정**: 엔지니어 수와 병목 특성을 고려하여 1인당 1~1.5개 수준으로 WIP Limit를 설정하였는가?
2. **명확한 완료 기준(DoD)**: 단순 개발 종료가 아닌 단위 테스트 통과, 코드 리뷰 완료, 배포 검증 기준이 보드 상단에 명시되어 있는가?
3. **스워밍(Swarming) 문화 장려**: 특정 칼럼의 카드가 WIP 상한에 도달했을 때 다른 개발자가 자기 일만 하지 않고 병목 지점을 지원하는 규칙이 정착되어 있는가?
4. **누적 흐름 다이어그램(CFD) 분석 주기**: 주간 단위로 CFD 밴드 폭(WIP 크기)과 기울기(처리 속도)를 분석하여 프로세스 병목을 개선하고 있는가?

---

## 실패 시나리오 및 트러블슈팅

| 위험 | 대책 | 효과 |
|---|---|---|
| **WIP 제한 미준수로 멀티태스킹 병목 및 납기 지연** | 개발자 1인당 WIP 1개 강제 상한선 설정 및 'Start Finishing' 원칙 적용 | 티켓 평균 사이클 타임 25일에서 4일로 단축 |
| **검수 칼럼 적체로 개발된 코드가 배포 대기** | 검수 칼럼 WIP 초과 시 신규 개발 착수 차단 및 전원 검수 협업(Swarming) | 검수 대기 시간 80% 감축 및 릴리스 병목 해소 |
| **WIP 상한 없는 형식적 칸반 보드 운영** | 칸반 도구(Jira 등)에 칼럼별 Max WIP 하드 리밋 설정 및 초과 시 경고 발령 | 작업 정체율 70% 개선 및 실제 납기 예측도 향상 |

---

## 차세대 확장 및 융합

- **스크럼반(Scrumban) 하이브리드 거버넌스**: 전체 비즈니스 로드맵과 대규모 릴리스는 스크럼의 타임박스 스프린트로 기획하고, 일상적인 결함 수정·인프라 변경·운영 티켓은 칸반의 지속적 풀(Pull) 방식으로 처리하는 융합 체계가 주류로 자리 잡았다.
- **가치 스트림 관리(VSM) 및 DORA 지표 연계**: 단순 티켓 이동을 넘어 배포 빈도(Deployment Frequency), 변경 리드 타임(Lead Time for Changes) 등 DORA 메트릭스와 칸반 리드 타임을 연동하여 엔드투엔드 개발 파이프라인의 낭비를 제거한다.

---

## 25점형 실전 답안 프레임워크

### 1단락: 칸반의 대두 배경 및 개념
- **배경**: 스프린트 타임박스로 수용하기 어려운 긴급 운영 이슈 대응 및 멀티태스킹으로 인한 납기 지연을 타파하기 위해 린(Lean) JIT 사상을 차용함.
- **정의**: 업무 흐름 시각화와 진행 중 작업(WIP) 제한을 통해 낭비를 줄이고 지속적인 가치 흐름을 창출하는 애자일 관리 체계.

### 2단락: 칸반의 핵심 원리 및 공학 메커니즘
- **칸반 보드 구성도 및 풀(Pull) 시스템 구조**: Backlog $\rightarrow$ Dev(WIP: 3) $\rightarrow$ Test(WIP: 2) $\rightarrow$ Done.
- **리틀의 법칙(Little's Law) 수학적 도해**:
  - 수식: $\text{Lead Time} = \frac{\text{WIP}}{\text{Throughput}}$.
  - 인력 추가 없이 WIP 제한만으로 리드 타임을 획기적으로 감축하는 공학 메커니즘 제시.

### 3단락: 칸반(Kanban)과 스크럼(Scrum)의 비교 및 상호 보완 (스크럼반)
- **비교 분석**: 반복 주기(연속 vs 스프린트), 작업 진입(WIP 여유 시 vs 스프린트 계획 시), 역할(유연 vs 엄격).
- **스크럼반(Scrumban) 융합 전략**: 아키텍처/신규 기능은 스크럼, 유지보수/운영/DevOps는 칸반 적용.

### 4단락: 성공적인 칸반 정착을 위한 기술사적 거버넌스 제언
- **문화적 전환(Stop Starting, Start Finishing)**: 신규 작업 착수를 영웅시하던 문화에서 기존 작업의 완료를 최우선시하는 문화로 전환.
- **CFD 기반 데이터 중심 회고**: 직관에 의존하지 않고 누적 흐름도의 밴드 폭과 경사도를 분석하여 과학적으로 프로세스를 지속 개선할 것을 제언함.

---

## 10점형 핵심 요약

1. **정의**: 전체 작업 흐름을 시각화하고 칼럼별 동시 진행 작업 수(WIP)를 엄격히 제한하여 리드 타임을 단축하는 린(Lean) 애자일 기법.
2. **핵심 요소**:
   - **WIP 제한**: 멀티태스킹 방지, 리틀의 법칙($\text{Lead Time} = \text{WIP} / \text{Throughput}$) 적용.
   - **지속적 흐름**: 타임박스 없이 작업이 완료되면 즉시 배포하는 풀(Pull) 방식.
3. **실무 핵심**: 운영성 업무 및 DevOps 환경에 최적이며, 대규모 신규 개발에서는 스크럼과 결합한 스크럼반(Scrumban) 형태로 발전함.
