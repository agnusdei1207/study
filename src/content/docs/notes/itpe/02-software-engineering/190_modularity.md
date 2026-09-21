---
title: "모듈성(결합도·응집도)"
category: "02-software-engineering"
tags:
  - "모듈성"
  - "결합도"
  - "응집도"
  - "Coupling"
  - "Cohesion"
  - "LCOM"
  - "마이어5대기준"
  - "FanInFanOut"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 설계 원칙과 아키텍처 품질을 거쳐 모듈성으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 설계 원칙·아키텍처 품질</span>
  <strong>모듈성(결합도·응집도)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 대규모 소프트웨어의 복잡성을 통제하고 분할 정복(Divide & Conquer)을 실현하기 위해, 소프트웨어를 자율적이고 독립적인 모듈 단위로 분해하고, 모듈 간 상호 의존성을 최소화(저결합도: Loose Coupling)하며 모듈 내부의 책임 집중도를 극대화(고응집도: High Cohesion)하여 변경 파급효과를 완벽히 격리하는 핵심 소프트웨어 공학 설계 원리
- 메커니즘: 도메인 요구 분석 $\rightarrow$ 단일 책임(SRP) 기반 모듈 분할 $\rightarrow$ 인터페이스 추상화 및 최소 데이터 전달 $\rightarrow$ 정량 메트릭(LCOM, Fan-in/out) 측정 $\rightarrow$ 고응집·저결합 모듈성 확정
- 산출물: 모듈 아키텍처 구조도 · 결합도/응집도 분석 보고서 · LCOM 정적 분석 리포트 · 모듈 인터페이스 정의서

<div class="itpe-flow-map" role="img" aria-label="모듈성 설계 및 정량적 품질 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 도메인 책임 분할 (고응집화)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분할</strong><span>단일 책임 원칙(SRP)에 따라 하나의 모듈이 오직 하나의 비즈니스 기능만 수행하도록 설계</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 인터페이스 캡슐화 (저결합화)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>격리</strong><span>정보 은닉을 적용하고 모듈 간에는 최소한의 원시 데이터(자료 결합도)만 전달</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 정량적 복잡도 계측</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>측정</strong><span>LCOM(응집도 결여) 및 Fan-in(호출 유입), Fan-out(호출 유출) 메트릭 산출</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 모듈성 품질 적합성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>LCOM 수치가 낮고 결합도가 자료/스탬프 수준이며 Fan-out이 4 이하로 통제되었는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (이상적 모듈성 달성)</strong>
      <span>아키텍처 승인 $\rightarrow$ 변경 파급효과 차단 및 독립적 단위 테스트 착수</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (스파게티 결합 / 응집 결여)</strong>
      <span>리팩토링 발동 $\rightarrow$ 모듈 분할 및 의존성 역전(DIP) 인터페이스 추출</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **결합도(Coupling)**: 모듈과 모듈 간의 상호 의존성의 정도를 나타내며, 낮을수록(Loose Coupling) 모듈의 독립성이 높아 변경에 안전함
- **응집도(Cohesion)**: 모듈 내부의 구성 요소들이 단일한 목적을 달성하기 위해 얼마나 긴밀하게 집중되어 있는지를 나타내며, 높을수록(High Cohesion) 유지보수성이 뛰어남
- **LCOM(Lack of Cohesion in Methods)**: 클래스 내 메서드들이 인스턴스 필드를 공유하지 않는 정도를 수학적으로 계측하여 응집도의 결여를 판정하는 객체지향 메트릭
- **Fan-In / Fan-Out**: 특정 모듈을 호출하는 상위 모듈의 수(Fan-In)와, 특정 모듈이 호출하는 하위 모듈의 수(Fan-Out)로, 높은 Fan-In과 낮은 Fan-Out이 이상적 아키텍처임
</details>

## 1. 개요 및 필요성

### 거대 소프트웨어의 복잡성 폭발과 모듈화

소프트웨어 규모가 커짐에 따라 코드 라인 수의 증가는 버그 발생 가능성을 지수 함수적으로 폭증시킨다. 하나의 함수나 모듈이 수만 줄에 달하고 전역 변수를 사방에서 참조하는 모놀리스 시스템은 사소한 버그 하나를 고치려다 시스템 전체가 다운되는 파멸을 낳는다.

모듈성(Modularity)은 "문제를 잘게 쪼개어 독립적으로 해결한다"는 분할 정복(Divide and Conquer)과 정보 은닉(Information Hiding)을 구현하는 공학적 뼈대이다. **결합도를 최소화(자료 결합도)하고 응집도를 극대화(기능적 응집도)**함으로써 시스템의 수정성, 재사용성, 테스트 용이성을 극대화한다.

### 결합도와 응집도의 상반 관계 매트릭스

| 품질 속성 | 나쁜 상태 (Worst) | 이상적인 상태 (Best) | 공학적 달성 원칙 |
|---|---|---|---|
| **결합도 (Coupling)** | **내용 결합도 (Content)**: 타 모듈 내부 변수 직접 수정 | **자료 결합도 (Data)**: 파라미터 값만 전달 | **정보 은닉, 인터페이스 캡슐화, DIP** |
| **응집도 (Cohesion)** | **우연적 응집도 (Coincidental)**: 아무 연관 없는 함수 집합 | **기능적 응집도 (Functional)**: 오직 1개 단일 작업 전담 | **단일 책임 원칙(SRP), 고순도 도메인 모델** |
| **변경 파급력** | 나비효과 (1줄 수정으로 전사 장애) | **완벽한 변경 격리 (Local Change)** | 모듈 내부 수정이 외부 인터페이스에 무영향 |
| **단위 테스트** | 테스트 불가능 (전체 시스템 기동 필수) | **완전한 격리 테스트 가능 (Mock 불필요)** | 모듈 단위 독립적 TDD 구축 가능 |

## 2. 아키텍처 및 핵심 메커니즘

### 결합도 6단계 및 응집도 7단계 스펙트럼

결합도는 낮을수록, 응집도는 높을수록 우수한 소프트웨어 아키텍처이다.

<div class="itpe-diagram-container" role="img" aria-label="결합도 6단계와 응집도 7단계 품질 스펙트럼 비교도">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-mod); }
    </style>
    <marker id="arrow-mod" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">모듈성 스펙트럼: 결합도(Coupling) 6단계 vs 응집도(Cohesion) 7단계</text>

  <!-- 왼쪽: 결합도 (낮을수록 우수) -->
  <rect x="16" y="34" width="236" height="172" class="box"/>
  <text x="24" y="50" class="h-text">결합도 (Coupling) : 낮을수록 우수 (약한 결합)</text>

  <rect x="24" y="58" width="220" height="18" class="box-active"/>
  <text x="30" y="70" class="h-text">1. 자료 결합도 (Data) - Best : 순수 값 파라미터 전달</text>

  <rect x="24" y="79" width="220" height="18" class="box"/>
  <text x="30" y="91" class="text">2. 스탬프 결합도 (Stamp) : 구조체/DTO 전달</text>

  <rect x="24" y="100" width="220" height="18" class="box"/>
  <text x="30" y="112" class="text">3. 제어 결합도 (Control) : 플래그로 타 모듈 흐름 통제</text>

  <rect x="24" y="121" width="220" height="18" class="box"/>
  <text x="30" y="133" class="text">4. 외부 결합도 (External) : 외부 통신/프로토콜 공유</text>

  <rect x="24" y="142" width="220" height="18" class="box"/>
  <text x="30" y="154" class="text">5. 공통 결합도 (Common) : 전역 변수(Global) 공유</text>

  <rect x="24" y="163" width="220" height="18" style="fill:rgba(239,68,68,0.18); stroke:#ef4444; stroke-width:1; rx:3;"/>
  <text x="30" y="175" fill="#ef4444" font-size="6.8px" font-weight="bold">6. 내용 결합도 (Content) - Worst : 내부 변수 직접 수정</text>

  <text x="24" y="198" class="muted">▶ 암기: 자 - 스 - 제 - 외 - 공 - 내 (약함 ➔ 강함)</text>

  <!-- 오른쪽: 응집도 (높을수록 우수) -->
  <rect x="268" y="34" width="236" height="172" class="box-active"/>
  <text x="276" y="50" class="h-text">응집도 (Cohesion) : 높을수록 우수 (단일 집중)</text>

  <rect x="276" y="58" width="220" height="18" class="box-active"/>
  <text x="282" y="70" class="h-text">1. 기능적 응집도 (Functional) - Best : 단일 목적 전담</text>

  <rect x="276" y="79" width="220" height="18" class="box"/>
  <text x="282" y="91" class="text">2. 순차적 응집도 (Sequential) : A 출력이 B 입력</text>

  <rect x="276" y="100" width="220" height="18" class="box"/>
  <text x="282" y="112" class="text">3. 통신적 응집도 (Communicational) : 동일 입력 기반</text>

  <rect x="276" y="121" width="220" height="18" class="box"/>
  <text x="282" y="133" class="text">4. 절차적 응집도 (Procedural) : 순차적 흐름 실행</text>

  <rect x="276" y="142" width="220" height="18" class="box"/>
  <text x="282" y="154" class="text">5. 시간적 응집도 (Temporal) : 동시 시점 실행(초기화)</text>

  <rect x="276" y="163" width="220" height="18" style="fill:rgba(239,68,68,0.18); stroke:#ef4444; stroke-width:1; rx:3;"/>
  <text x="282" y="175" fill="#ef4444" font-size="6.8px" font-weight="bold">6. 논리적 / 7. 우연적 (Coincidental) - Worst : 연관 없음</text>

  <text x="276" y="198" class="muted">▶ 암기: 기 - 순 - 교(통) - 절 - 시 - 논 - 우 (강함 ➔ 약함)</text>
</svg>
</div>

### 모듈성 평가 지표 및 구조적 규칙

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① LCOM (응집도 결여)</strong></span>
      <span class="itpe-badge">객체지향 메트릭</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>클래스 내 메서드들이 공유하는 인스턴스 필드 수의 차이로 계산</li>
        <li>LCOM 값이 0에 가까울수록 고응집도 클래스, 높을수록 클래스 분할 필요</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② Fan-In & Fan-Out</strong></span>
      <span class="itpe-badge">호출 관계도</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>Fan-In(호출받는 수)이 높을수록 모듈 재사용성이 우수함</li>
        <li>Fan-Out(호출하는 수)이 높을수록 타 모듈 변경에 취약하므로 3~4 이하 유지</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 버트란드 마이어 5대 기준</strong></span>
      <span class="itpe-badge">설계 품질</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>모듈 분해성, 모듈 조합성, 모듈 이해성, 모듈 연속성, 모듈 보호성</li>
        <li>오류가 모듈 경계를 넘어 연쇄 파급되지 않는 보호성(Protection) 필수</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 정보 은닉 (Information Hiding)</strong></span>
      <span class="itpe-badge">캡슐화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>데이비드 파나스(Parnas)가 제창한 모듈화의 제1원리</li>
        <li>변경 가능성이 높은 내부 자료구조와 알고리즘은 private 은닉</li>
      </ul>
    </div>
  </div>
</div>

### 이상적 아키텍처: 높은 Fan-In과 낮은 Fan-Out 구조

모듈의 재사용성과 안정성을 보장하는 아키텍처 호출 토폴로지이다.

<div class="itpe-diagram-container" role="img" aria-label="모듈 간 Fan-In과 Fan-Out 이상적 계층 구조도">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-fi); }
    </style>
    <marker id="arrow-fi" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">이상적인 모듈 복잡도 통제: 높은 Fan-In과 낮은 Fan-Out 아키텍처</text>

  <!-- 상위 모듈들 (호출자) -->
  <rect x="24" y="38" width="95" height="34" class="box"/>
  <text x="32" y="53" class="text">주문 서비스 (A)</text>
  <text x="32" y="63" class="muted">비즈니스 모듈</text>

  <rect x="144" y="38" width="95" height="34" class="box"/>
  <text x="152" y="53" class="text">결제 서비스 (B)</text>
  <text x="152" y="63" class="muted">비즈니스 모듈</text>

  <rect x="264" y="38" width="95" height="34" class="box"/>
  <text x="272" y="53" class="text">배송 서비스 (C)</text>
  <text x="272" y="63" class="muted">비즈니스 모듈</text>

  <!-- 중앙 공통 핵심 모듈 (높은 Fan-In) -->
  <rect x="114" y="112" width="155" height="46" class="box-active"/>
  <text x="122" y="129" class="h-text">공통 인증/로깅 모듈 (Target)</text>
  <text x="122" y="142" class="text">Fan-In = 3 (다수 상위 모듈이 재사용)</text>
  <text x="122" y="152" class="muted">높은 재사용성 ➔ 검증 집중 필요</text>

  <!-- 상위 -> 중앙 화살표들 (Fan-In) -->
  <line x1="71" y1="72" x2="135" y2="112" class="arrow"/>
  <line x1="191" y1="72" x2="191" y2="112" class="arrow"/>
  <line x1="311" y1="72" x2="247" y2="112" class="arrow"/>

  <!-- 하위 의존 모듈 (낮은 Fan-Out) -->
  <rect x="144" y="180" width="95" height="30" class="box"/>
  <text x="154" y="195" class="text">보안 라이브러리</text>
  <text x="154" y="204" class="muted">단일 원자 의존성</text>

  <!-- 중앙 -> 하위 화살표 (Fan-Out = 1) -->
  <line x1="191" y1="158" x2="191" y2="180" class="arrow"/>
  <text x="198" y="172" fill="#38bdf8" font-size="6.5px">Fan-Out = 1</text>

  <!-- 우측 설명 카드 -->
  <rect x="380" y="38" width="124" height="168" class="box-active"/>
  <text x="388" y="56" class="h-text">모듈 복잡도 통제 원칙</text>
  
  <text x="388" y="74" class="text">• Fan-In이 높다:</text>
  <text x="388" y="86" class="muted">여러 모듈이 공유함</text>
  <text x="388" y="96" class="muted">➔ 높은 재사용성 증명</text>
  <text x="388" y="106" class="muted">➔ 철저한 단위테스트 필수</text>

  <text x="388" y="126" class="text">• Fan-Out이 낮다:</text>
  <text x="388" y="138" class="muted">타 모듈을 적게 호출함</text>
  <text x="388" y="148" class="muted">➔ 독립성 극대화</text>
  <text x="388" y="158" class="muted">➔ Fan-Out &gt; 5는 위험</text>

  <text x="388" y="184" fill="#38bdf8" font-size="6.5px" font-weight="bold">이상형: High Fan-In,</text>
  <text x="388" y="194" fill="#38bdf8" font-size="6.5px" font-weight="bold">Low Fan-Out (다이아몬드)</text>
</svg>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 싱글톤 전역 객체(Global State) 남용으로 인해 스레드 세이프티 파탄 및 공통 결합도(Common) 발생 | 의존성 주입(DI: Dependency Injection) 프레임워크를 도입하여 인스턴스 생명주기를 IoC 컨테이너로 격리 | 동시성 결함 100% 제거 및 단위 테스트 모킹 용이성 확보 |
| 특정 비즈니스 로직을 변경했을 때 전혀 무관한 15개 파일이 연쇄 컴파일 에러를 일으키는 변경 전파 | 구체 클래스 직접 참조를 제거하고 인터페이스 분리 원칙(ISP) 및 의존성 역전(DIP) 적용 | 변경 파급 범위 단일 모듈로 완벽 격리 |
| 만능 클래스(God Object)에 수십 개 업무 메서드가 뒤섞여 LCOM 수치 폭증 및 가독성 마비 | 단일 책임 원칙(SRP) 기반으로 클래스를 3~4개의 고응집 기능별 서비스 클래스로 세분화 리팩토링 | 클래스당 라인 수 80% 감축 및 유지보수 생산성 3배 증대 |

## 4. 기술사 답안 차별화 포인트

### 객체지향 응집도 결여(LCOM) 메트릭의 수학적 분석

많은 수험생이 응집도를 정성적 개념으로만 서술한다. 기술사 답안에서는 치담버와 케머러(Chidamber & Kemerer)의 **LCOM(Lack of Cohesion in Methods) 수식**을 제시한다. 클래스 내 임의의 두 메서드 쌍 $(M_i, M_j)$에 대해 공통 인스턴스 변수를 전혀 공유하지 않는 쌍의 집합 크기 $P$와, 공유하는 쌍의 집합 크기 $Q$에 대하여 $LCOM = \max(0, P - Q)$로 정의됨을 서술하고, LCOM 값이 클수록 클래스를 분할해야 한다는 **정량적 엔지니어링 메트릭**을 강조한다.

### 마이크로서비스(MSA)의 도메인 경계와 모듈성의 진화

전통적 모듈성이 단일 JVM 메모리 내 클래스/패키지 분할을 의미했다면, 현대 분산 환경에서는 **DDD(도메인 주도 설계)의 바운디드 컨텍스트(Bounded Context)와 마이크로서비스**가 모듈성의 새로운 단위이다. 서비스 간에는 REST/Kafka를 통한 자료 결합도를 유지하고, 서비스 내부 도메인은 고응집 Aggregate로 묶는 **분산 아키텍처 수준의 모듈성 확장**을 결론으로 제시한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 결합도와 응집도는 소프트웨어 공학의 알파이자 오메가다. 스프링의 DI/IoC, 객체지향의 SOLID 원칙, DDD의 바운디드 컨텍스트, MSA까지... 소프트웨어 공학 역사의 모든 진보는 결국 "어떻게 하면 결합도를 낮추고 응집도를 올릴 것인가"라는 질문에 대한 대답이었다.
- [나라면]: 1교시형 단답 시 결합도 6단계(자-스-제-외-공-내)와 응집도 7단계(기-순-교-절-시-논-우)를 완벽히 암기하여 위상 스펙트럼으로 제시하겠다. 2교시형 출제 시에는 Fan-In/Fan-Out 다이아몬드 구조와 LCOM 수식을 정량 지표로 제시하고, 모듈성 원리가 현대 MSA 및 헥사고날 아키텍처로 어떻게 확장되었는지를 연결하여 득점 포인트를 극대화하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 모듈 간 결합도가 자료/스탬프 결합도 수준으로 통제되고, 클래스별 LCOM=0(완전 응집) 및 모듈 Fan-Out 4 이하 달성 여부
- **대응 방안**: 단일 책임 원칙(SRP) 기반 도메인 분할 및 인터페이스 기반 의존성 역전(DIP)을 전사 코딩 컨벤션으로 강제화
- **검증 체계**: SonarQube 정적 분석 기반 LCOM/순환 참조 측정 ➔ ArchUnit 아키텍처 규칙 단위 테스트 ➔ PR 리뷰 게이트
- **기대 효과**: 변경 파급효과 원천 격리, 신규 기능 추가 시 회귀 결함 발생률 70% 감소 및 분산 MSA 전환 비용 최소화

<div class="itpe-pipeline-container" role="img" aria-label="모듈성 아키텍처 엔지니어링 파이프라인">
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">01</div>
    <div class="itpe-pipeline-step-content">
      <strong>도메인 책임 분할</strong>
      <span>단일 책임 원칙(SRP) 기반 기능적 고응집 모듈 분리</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">02</div>
    <div class="itpe-pipeline-step-content">
      <strong>인터페이스 캡슐화</strong>
      <span>정보 은닉 적용 및 파라미터 기반 자료 결합도 설계</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">03</div>
    <div class="itpe-pipeline-step-content">
      <strong>정량적 메트릭 계측</strong>
      <span>LCOM 측정 및 Fan-In/Fan-Out 구조 복잡도 검증</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">04</div>
    <div class="itpe-pipeline-step-content">
      <strong>ArchUnit 자동 검증</strong>
      <span>CI 파이프라인에서 레이어 간 불법 참조 빌드 차단</span>
    </div>
  </div>
</div>

## 5. 참고 및 연계 학습

- [객체지향 설계 5대 원칙(SOLID)](./047_solid_principles.md)
- [추상 클래스와 인터페이스](./205_abstract_class_and_interface.md)
- [마이크로서비스 아키텍처(MSA)](./035_msa.md)
- [소프트웨어 아키텍처 기술서(SAD)](./202_sad.md)
