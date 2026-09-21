---
title: "CMMI(Capability Maturity Model Integration)"
category: "02-software-engineering"
tags:
  - "CMMI"
  - "프로세스성숙도"
  - "통계적공정관리"
  - "단계적표현"
  - "연속적표현"
  - "SPICE"
  - "테일러링"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 품질 보증과 프로세스 평가를 거쳐 CMMI로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 품질 보증·프로세스 평가</span>
  <strong>CMMI(Capability Maturity Model Integration)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 소프트웨어 개발 조직의 품질과 납기 통제를 특정 개인의 영웅적 역량에 의존하지 않고, 조직 차원의 표준 프로세스와 정량적 데이터 기반의 통계적 공정 관리(SPC)를 통해 예측 가능하고 재현 가능한 고품질 소프트웨어를 반복 생산하도록 지원하는 SEI/ISACA 프로세스 통합 성숙도 모델
- 메커니즘: 프로세스 혼돈(Level 1) $\rightarrow$ 프로젝트 차원 관리(Level 2) $\rightarrow$ 전사 표준화 및 테일러링(Level 3) $\rightarrow$ 통계적 정량 관리(Level 4) $\rightarrow$ 지속적 결함 예방 및 공정 최적화(Level 5)
- 산출물: 조직 표준 프로세스 자산(OSSP) · 테일러링 계획서 · 통계적 공정 관리도(Control Chart) · CMMI 심사 결과 보고서

<div class="itpe-flow-map" role="img" aria-label="CMMI 성숙도 레벨 5단계 발전 및 공정 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1~2단계: 프로젝트 차원 관리 (Managed)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>통제</strong><span>개별 프로젝트 단위로 요구사항, 일정, 형상 관리 베이스라인 수립</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 조직 표준 프로세스 확립 (Defined)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>표준화</strong><span>전사 표준 프로세스 자산화(OSSP) 및 프로젝트별 테일러링 수행</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 통계적 정량 관리 (Quantitatively Managed)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>계측</strong><span>관리도(Control Chart) 기반 결함 밀도 및 생산성의 통계적 예측 제어</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>5단계: 지속적 최적화 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>공정 변동이 통계 한계선 내에서 통제되며 근본 원인 분석(CAR) 기반 결함 예방이 작동하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Level 5 Optimizing 달성)</strong>
      <span>자가 혁신 조직 안착 $\rightarrow$ 비즈니스 품질 예측 신뢰성 99% 달성</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (이상 변동 탐지)</strong>
      <span>Level 4 관리 강화 $\rightarrow$ 통계 지표 이상치(Outlier) 근본 원인 재분석</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **단계적 표현(Staged Representation)**: 조직 전체의 프로세스 성숙도를 1단계부터 5단계까지 순차적으로 평가하여 조직 단위 성숙도 레벨(Maturity Level)을 부여하는 방식
- **연속적 표현(Continuous Representation)**: 조직이 필요로 하는 개별 프로세스 영역(PA)을 선별하여 능력 레벨(Capability Level 0~3)을 집중 개선하는 맞춤형 방식
- **통계적 공정 관리(SPC, Statistical Process Control)**: 공정의 변동성을 관리 상한선(UCL)과 관리 하한선(LCL)으로 통제하여 결함 발생률과 개발 생산성을 수학적으로 예측하는 기법
- **테일러링(Tailoring)**: 조직 표준 프로세스(OSSP)를 개별 프로젝트의 특성, 규모, 위험도, 계약 조건에 맞추어 합리적으로 가감 조정하는 표준 활동
</details>

## 1. 개요 및 필요성

### 개인 의존적 개발의 한계와 프로세스 성숙도

소프트웨어 개발 프로젝트가 소수의 천재 개발자(Hero)의 야근과 개인기에만 의존하면, 해당 인력이 이탈하는 순간 프로젝트는 파탄에 직면한다. 제품의 품질이 일정하지 않고 일정과 예산 예측이 불가능한 현상을 "소프트웨어 위기"라 부른다.

CMMI는 **"우수한 프로세스에서 우수한 품질의 제품이 나온다"**는 철학을 바탕으로, 조직의 개발 역량을 체계적인 5단계 성숙도 레벨로 정형화하여 **예측 가능하고 재현 가능한 엔지니어링 프로세스**를 정립한다.

### CMMI vs SPICE vs ISO 9001 비교

| 구분 | CMMI (v2.0 / v3.0) | SPICE (ISO/IEC 33000 / 15504) | ISO 9001 |
|---|---|---|---|
| **주관 기관** | 미국 카네기멜론 SEI / ISACA | ISO / IEC 국제표준화기구 | ISO 국제표준화기구 |
| **적용 영역** | **소프트웨어, 시스템 엔지니어링, R&D** | 소프트웨어 프로세스 평가 및 개선 | 제조 및 전 산업 일반 품질경영시스템 |
| **평가 모델** | **단계적(1~5) 및 연속적(0~3) 병행** | 연속적 모델 중심 (능력 0~5단계) | 요구사항 충족 여부 단일 합격/불합격 |
| **핵심 지향** | **조직의 프로세스 개선 및 비즈니스 성과 연계** | 국제 표준 규격 준수 평가 | 고객 요구 충족 및 품질 보증 체계 |

## 2. 아키텍처 및 핵심 메커니즘

### CMMI 5대 성숙도 레벨 (Staged Model)

CMMI 단계적 모델은 조직의 프로세스 진화 과정을 5단계의 계층 구조로 정의한다.

<div class="itpe-diagram-container" role="img" aria-label="CMMI 5단계 성숙도 레벨 계층 구조도">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-cmmi); }
    </style>
    <marker id="arrow-cmmi" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">CMMI 5대 성숙도 레벨 계층 구조 (Staged Representation)</text>

  <!-- Level 5 -->
  <rect x="16" y="34" width="488" height="32" class="box-active"/>
  <text x="26" y="48" class="h-text">Level 5: 최적화 단계 (Optimizing)</text>
  <text x="26" y="59" class="text">지속적 프로세스 혁신, 원인 분석 및 해결(CAR), 정량적 결함 예방 및 공정 자가 튜닝</text>

  <!-- Level 4 -->
  <rect x="16" y="70" width="488" height="32" class="box"/>
  <text x="26" y="84" class="h-text">Level 4: 정량적 관리 단계 (Quantitatively Managed)</text>
  <text x="26" y="95" class="text">통계적 공정 관리(SPC), 공정 성능 베이스라인(QPM/OPP), 수학적 모델 기반 품질·납기 정밀 예측</text>

  <!-- Level 3 -->
  <rect x="16" y="106" width="488" height="32" class="box-active"/>
  <text x="26" y="120" class="h-text">Level 3: 정의 단계 (Defined)</text>
  <text x="26" y="131" class="text">전사 표준 프로세스 자산화(OSSP), 프로젝트별 테일러링(Tailoring) 가이드라인 준수, 기술 솔루션 확립</text>

  <!-- Level 2 -->
  <rect x="16" y="142" width="488" height="32" class="box"/>
  <text x="26" y="156" class="h-text">Level 2: 관리 단계 (Managed)</text>
  <text x="26" y="167" class="text">개별 프로젝트 수준의 계획, 요구사항 관리, 형상 관리(CM), 측정 및 분석, 협력업체 계약 관리</text>

  <!-- Level 1 -->
  <rect x="16" y="178" width="488" height="32" class="box"/>
  <text x="26" y="192" class="h-text">Level 1: 초기 단계 (Initial)</text>
  <text x="26" y="203" class="text">표준 프로세스 부재, 특정 영웅적 개인 역량에 의존, 일정·비용 초과 다발, 혼돈(Chaos) 상태</text>
</svg>
</div>

### 단계적 표현 vs 연속적 표현 구조

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>단계적 표현 (Staged)</strong></span>
      <span class="itpe-badge">조직 성숙도</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>조직 전체를 1단계부터 5단계까지 레벨(Maturity Level)로 종합 평가</li>
        <li>기업 대외 홍보, 입찰 자격 심사, 공인 인증 획득에 주로 활용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>연속적 표현 (Continuous)</strong></span>
      <span class="itpe-badge">프로세스 영역별 능력</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>조직이 개선하려는 특정 프로세스 영역(PA)을 골라 능력 레벨(0~3) 평가</li>
        <li>조직의 단기 병목 영역(예: 요구사항 관리, 형상 관리) 집중 개선에 최적</li>
      </ul>
    </div>
  </div>
</div>

### Level 4 통계적 공정 관리(SPC)와 결함 통제 메커니즘

CMMI 고성숙도(High Maturity, Level 4/5)의 핵심은 관리도(Control Chart)를 통한 이상치 감지와 근본 원인 해결이다.

<div class="itpe-diagram-container" role="img" aria-label="통계적 공정 관리 관리도 및 근본 원인 분석 피드백 루프">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-spc); }
      .line-ucl { stroke: #ef4444; stroke-width: 1.5; stroke-dasharray: 4,4; }
      .line-cl { stroke: #38bdf8; stroke-width: 1.5; }
      .line-lcl { stroke: #ef4444; stroke-width: 1.5; stroke-dasharray: 4,4; }
    </style>
    <marker id="arrow-spc" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">통계적 공정 관리(SPC) 관리도 및 Level 5 결함 예방(CAR) 피드백 루프</text>

  <!-- 왼쪽: 관리도 차트 -->
  <rect x="16" y="34" width="270" height="170" class="box"/>
  <text x="24" y="50" class="h-text">소프트웨어 공정 성능 관리도 (Control Chart)</text>
  
  <!-- 기준선들 -->
  <line x1="30" y1="72" x2="270" y2="72" class="line-ucl"/>
  <text x="210" y="68" fill="#ef4444" font-size="6.5px" font-weight="bold">UCL (관리상한: +3σ)</text>

  <line x1="30" y1="114" x2="270" y2="114" class="line-cl"/>
  <text x="210" y="110" fill="#38bdf8" font-size="6.5px" font-weight="bold">CL (공정평균: Mean)</text>

  <line x1="30" y1="156" x2="270" y2="156" class="line-lcl"/>
  <text x="210" y="152" fill="#ef4444" font-size="6.5px" font-weight="bold">LCL (관리하한: -3σ)</text>

  <!-- 데이터 포인트 및 이상치 -->
  <circle cx="50" cy="118" r="3" fill="#38bdf8"/>
  <circle cx="85" cy="100" r="3" fill="#38bdf8"/>
  <circle cx="120" cy="125" r="3" fill="#38bdf8"/>
  <circle cx="155" cy="62" r="4.5" fill="#ef4444"/> <!-- 이상치 -->
  <text x="145" y="54" fill="#ef4444" font-size="6.5px" font-weight="bold">이상치(Outlier)</text>
  <circle cx="190" cy="108" r="3" fill="#38bdf8"/>
  <circle cx="225" cy="120" r="3" fill="#38bdf8"/>

  <!-- 연결선 -->
  <polyline points="50,118 85,100 120,125 155,62 190,108 225,120" fill="none" stroke="var(--color-border-strong, #64748b)" stroke-width="1.2"/>
  <text x="24" y="188" class="muted">통계적 공정 상태: 관리 한계선(UCL~LCL) 내 변동은 정상(우연원인)</text>

  <!-- 오른쪽: CAR 피드백 루프 -->
  <rect x="300" y="34" width="204" height="170" class="box-active"/>
  <text x="310" y="50" class="h-text">Level 5 근본 원인 분석 (CAR)</text>
  
  <rect x="310" y="60" width="184" height="34" class="box"/>
  <text x="316" y="74" class="text">1. 이상치 발생 탐지</text>
  <text x="316" y="86" class="muted">UCL 초과 결함 밀도 급증 감지</text>
  <line x1="402" y1="94" x2="402" y2="104" class="arrow"/>

  <rect x="310" y="104" width="184" height="34" class="box"/>
  <text x="316" y="118" class="text">2. 근본 원인 도출 (Fishbone)</text>
  <text x="316" y="130" class="muted">특수원인(인력 교체, 툴 오류) 격리</text>
  <line x1="402" y1="138" x2="402" y2="148" class="arrow"/>

  <rect x="310" y="148" width="184" height="42" class="box-active"/>
  <text x="316" y="162" class="text">3. 표준 프로세스 자산 영구 개정</text>
  <text x="316" y="174" class="muted">동일 결함 재발 원천 차단 (결함 예방)</text>
  <text x="316" y="184" class="muted">▶ 자가 혁신(Self-Optimizing) 조직 안착</text>
</svg>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| CMMI 심사 통과만을 위해 실무와 동떨어진 수천 장의 가짜 산출물을 작성하는 '페이퍼 CMMI' 전락 | Jira, Confluence, Git 등 실제 개발 도구의 API와 CMMI 프로세스 영역을 100% 자동 매핑 | 문서 작성 오버헤드 80% 감축 및 실질적 품질 향상 |
| 소규모 스타트업이나 애자일 조직에 무거운 Level 3 전사 표준 프로세스를 강요하여 개발 속도 마비 | 조직 특성과 규모에 맞게 필수 프로세스만 선별하여 간소화하는 테일러링(Tailoring) 가이드라인 엄격 적용 | 애자일의 속도와 CMMI의 품질 통제력 동시 확보 |
| Level 4 통계적 공정 관리 시 잘못된 표본 추출로 공정 능력 지수($C_p, C_{pk}$)의 신뢰성 상실 | 프로젝트 규모(FP/LOC)와 도메인 복잡도를 정규화한 표준 결함 밀도 지표 수립 | 품질 예측 신뢰성 95% 이상 확보 |

## 4. 기술사 답안 차별화 포인트

### CMMI v2.0/v3.0과 애자일/DevOps의 융합

과거 CMMI v1.3은 무거운 폭포수 모델에 치우쳐 애자일 환경과 대립한다는 비판을 받았다. 그러나 **CMMI v2.0 및 v3.0**은 스크럼(Scrum), 칸반(Kanban), DevOps 파이프라인을 핵심 프랙티스로 정식 통합하였다. 답안에서는 **"지속적 통합/배포(CI/CD) 로그에서 품질 메트릭을 실시간 수집하여 CMMI Level 4 통계적 공정 관리를 자동화하는 모던 CMMI 체계"**를 제시하여 현대적 엔지니어링 감각을 보여준다.

### 공정 성능 모델(PPM) 기반의 비즈니스 ROI 예측

CMMI 고성숙도(High Maturity)는 단순한 인증 마크가 아니라 비즈니스 투자 수익(ROI)을 입증하는 도구이다. **공정 성능 모델(Process Performance Model)**을 활용하여 "코드 리뷰 시간을 20% 늘리면 배포 후 장애율이 45% 감소하고 유지보수 비용이 3억 원 절감된다"는 식의 **정량적 의사결정 시뮬레이션 역량**을 결론으로 강조한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: CMMI의 본질은 '서류 만들기'가 아니라 '데이터로 일하기'다. Level 3까지는 상식적인 프로세스 정리지만, 진짜 차별화는 Level 4의 통계적 관리(SPC)와 Level 5의 결함 예방(CAR)에서 나온다.
- [나라면]: 1교시형 단답 출제 시 5단계 계층과 핵심 단어(혼돈-프로젝트-전사표준-통계-최적화)를 명확히 구조화하고, 단계적 모델과 연속적 모델의 차이를 비교하겠다. 2교시형 출제 시에는 과거 '페이퍼 CMMI'의 폐해를 지적하고, Jira/GitLab 기반 실시간 메트릭 수집을 결합한 'CMMI v3.0 + DevOps' 융합 모델을 기술사적 해법으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 전사 프로젝트 표준 테일러링 준수율 100% 및 결함 밀도 관리도 상한선(UCL) 이내 통제율 98% 달성 여부
- **대응 방안**: CMMI v2.0/v3.0 거버넌스를 기반으로 GitOps CI/CD 파이프라인과 자동 연동되는 정량적 품질 통제 체계 구축
- **검증 체계**: 동료 인스펙션 증적 자동 추출 ➔ 공정 성능 모델(PPM) 분석 ➔ 통계적 공정 관리도 이상치 모니터링 ➔ SCAMPI 심사
- **기대 효과**: 소프트웨어 납기 지연율 0% 수렴, 프로젝트 재작업 비용 40% 절감 및 글로벌 수주 경쟁력 확보

<div class="itpe-pipeline-container" role="img" aria-label="CMMI 프로세스 성숙도 고도화 파이프라인">
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">01</div>
    <div class="itpe-pipeline-step-content">
      <strong>프로젝트 통제</strong>
      <span>요구사항·형상관리 베이스라인 및 산출물 추적 확립</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">02</div>
    <div class="itpe-pipeline-step-content">
      <strong>전사 표준 테일러링</strong>
      <span>조직 표준 프로세스(OSSP) 수립 및 프로젝트별 최적화</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">03</div>
    <div class="itpe-pipeline-step-content">
      <strong>통계적 정량 관리</strong>
      <span>관리도(SPC) 기반 결함 밀도 및 생산성 변동 제어</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">04</div>
    <div class="itpe-pipeline-step-content">
      <strong>원인 분석 및 최적화</strong>
      <span>CAR 결함 예방 루프 가동 및 프로세스 자가 혁신</span>
    </div>
  </div>
</div>

## 5. 참고 및 연계 학습

- [SPICE (ISO/IEC 15504)](./016_spice.md)
- [SW 개발 방법론 비교](./139_sw_development_methodologies.md)
- [형상 관리(Configuration Management)](./011_configuration_management.md)
- [소프트웨어 품질 비용(PAF 모델)](./150_software_quality_cost.md)
