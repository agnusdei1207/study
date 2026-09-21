---
title: "통합 테스트(Integration Test)"
category: "02-software-engineering"
tags:
  - "통합테스트"
  - "하향식통합"
  - "상향식통합"
  - "빅뱅통합"
  - "샌드위치통합"
  - "테스트스텁"
  - "테스트드라이버"
  - "Pact"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 테스팅과 품질 보증을 거쳐 통합 테스트로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 테스팅·품질 보증</span>
  <strong>통합 테스트(Integration Test)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 단위 테스트를 통과한 개별 모듈들이 상호 결합할 때 발생하는 데이터 타입 불일치, 인터페이스 프로토콜 오류, 예외 처리 누락을 검증하기 위해, 모듈 간의 상호작용과 데이터 통신 흐름의 정합성을 체계적으로 검증하는 V-모델 상세설계 기반 테스트 레벨
- 메커니즘: 단위 모듈 수집 $\rightarrow$ 점진적 통합 전략(하향식/상향식/샌드위치) 수립 $\rightarrow$ 테스트 하네스(드라이버/스텁) 배치 $\rightarrow$ 인터페이스 결합 시험 $\rightarrow$ 결함 격리 및 정합성 검증
- 산출물: 통합 테스트 계획서 · 인터페이스 테스트 케이스 명세서 · 테스트 하네스 스크립트 · 결함 원인 분석 보고서

<div class="itpe-flow-map" role="img" aria-label="소프트웨어 통합 테스트 절차 및 인터페이스 검증 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 단위 모듈 수집 및 인터페이스 분석</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>단위 테스트 합격 모듈 간 호출 관계 및 파라미터/반환값 명세 확인</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 통합 전략 및 테스트 하네스 준비</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>배치</strong><span>하향식(스텁 Stub) 또는 상향식(드라이버 Driver) 가상 환경 구축</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 점진적 결합 및 인터페이스 통신 시험</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>결합</strong><span>모듈을 단계별로 결합하며 데이터 교환 및 예외 전파 메커니즘 검증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 인터페이스 무결성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>모든 모듈 간 데이터 직렬화와 통신 계약(Contract)이 오류 없이 완결되는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (인터페이스 무결성 확정)</strong>
      <span>통합 승인 $\rightarrow$ 상위 시스템 테스트(System Test) 단계 진입</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (인터페이스 충돌 / 타임아웃)</strong>
      <span>결함 모듈 격리 $\rightarrow$ API 규격 재조정 및 DTO 파라미터 매핑 보완</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **테스트 드라이버(Test Driver)**: 상향식 통합 테스트에서 아직 개발되지 않은 상위 모듈을 대신하여, 하위 모듈에 테스트 데이터를 전달하고 결과를 수신하는 가상 호출 프로그램
- **테스트 스텁(Test Stub)**: 하향식 통합 테스트에서 아직 개발되지 않은 하위 모듈을 대신하여, 상위 모듈의 호출에 미리 정해진 가상의 결과값만 반환하는 임시 더미 루틴
- **빅뱅 통합(Big-Bang Integration)**: 모든 단위 모듈이 완성될 때까지 기다렸다가 일괄 결합하여 테스트하는 비점진적 방식으로, 결함 원인 격리가 극도로 어려움
- **소비자 주도 계약 테스팅(Pact CDC)**: 마이크로서비스 환경에서 API 소비자가 기대하는 인터페이스 계약서를 기준으로 제공자의 호환성을 검증하는 최신 기법
</details>

## 1. 개요 및 필요성

### 단위 테스트의 한계와 인터페이스 결합 병목

아무리 개별 클래스나 함수가 단위 테스트에서 100% 커버리지를 달성했더라도, 서로 다른 개발자가 만든 모듈을 결합하는 순간 시스템은 멈춰 선다. 날짜 포맷(`YYYY-MM-DD` vs `Timestamp`) 불일치, 널(Null) 포인터 예외 전파, 비동기 호출 타임아웃 등 대부분의 치명적 결함은 **모듈 간의 접점인 "인터페이스"**에서 발생한다.

통합 테스트는 소프트웨어 아키텍처 상세설계 단계에서 정의된 인터페이스 규격과 데이터 교환 흐름이 실제 런타임 환경에서 완벽하게 작동하는지 검증하는 필수 공정이다.

### 점진적 통합 vs 비점진적 통합 비교

| 구분 | 비점진적 통합 (Non-Incremental) | 점진적 통합 (Incremental) |
|---|---|---|
| **대표 방식** | **빅뱅 통합 (Big-Bang)** | **하향식(Top-Down), 상향식(Bottom-Up), 샌드위치(Sandwich)** |
| **결합 전략** | 모든 모듈을 한 번에 일괄 결합 | 모듈을 하나씩 또는 클러스터 단위로 단계별 결합 |
| **결함 격리** | **결함 발생 시 원인 추적 극도로 곤란** | **방금 결합된 모듈 또는 인터페이스로 결함 즉시 격리** |
| **하네스 비용** | 드라이버/스텁 작성 불필요 (비용 0) | 드라이버 또는 스텁 개발 공수 필요 |
| **적용 권장** | 초소형 단기 토이 프로젝트 | **엔터프라이즈 및 미션 크리티컬 중대형 시스템** |

## 2. 아키텍처 및 핵심 메커니즘

### 4대 통합 테스트 전략 아키텍처

통합 테스트는 시스템의 제어 흐름과 데이터 종속성에 따라 4가지 전략으로 구분된다.

<div class="itpe-diagram-container" role="img" aria-label="하향식, 상향식, 샌드위치, 빅뱅 4대 통합 테스트 전략 비교 아키텍처">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-head); }
    </style>
    <marker id="arrow-head" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">소프트웨어 4대 통합 테스트 전략 및 테스트 하네스 구조</text>

  <!-- 하향식 Top-Down -->
  <rect x="14" y="32" width="115" height="174" class="box"/>
  <text x="22" y="48" class="h-text">1. 하향식 (Top-Down)</text>
  <rect x="22" y="56" width="99" height="28" class="box-active"/>
  <text x="28" y="69" class="text">메인 제어 모듈 (실제)</text>
  <text x="28" y="78" class="muted">상위 제어 로직 조기 검증</text>
  <line x1="71" y1="84" x2="71" y2="98" class="arrow"/>
  <rect x="22" y="98" width="99" height="30" class="box"/>
  <text x="28" y="111" class="text">가상 스텁 (Stub 1/2)</text>
  <text x="28" y="121" class="muted">하위 더미 응답 데이터 반환</text>
  <text x="22" y="148" class="muted">• 장점: UI·골격 조기 시연</text>
  <text x="22" y="162" class="muted">• 단점: 다수 스텁 제작 공수</text>
  <text x="22" y="176" class="muted">• 깊이/너비 우선 통합 전개</text>

  <!-- 상향식 Bottom-Up -->
  <rect x="139" y="32" width="115" height="174" class="box"/>
  <text x="147" y="48" class="h-text">2. 상향식 (Bottom-Up)</text>
  <rect x="147" y="56" width="99" height="28" class="box"/>
  <text x="153" y="69" class="text">가상 드라이버 (Driver)</text>
  <text x="153" y="78" class="muted">상위 호출 및 테스트 데이터 주입</text>
  <line x1="196" y1="84" x2="196" y2="98" class="arrow"/>
  <rect x="147" y="98" width="99" height="30" class="box-active"/>
  <text x="153" y="111" class="text">원자 모듈 클러스터</text>
  <text x="153" y="121" class="muted">DB·알고리즘 실제 모듈 결합</text>
  <text x="147" y="148" class="muted">• 장점: 핵심 로직 조기 검증</text>
  <text x="147" y="162" class="muted">• 단점: 상위 골격 완성 지연</text>
  <text x="147" y="176" class="muted">• 드라이버로 클러스터 시험</text>

  <!-- 샌드위치 Sandwich -->
  <rect x="264" y="32" width="115" height="174" class="box"/>
  <text x="272" y="48" class="h-text">3. 샌드위치 (Sandwich)</text>
  <rect x="272" y="56" width="99" height="28" class="box"/>
  <text x="278" y="72" class="text">상위 계층: 하향식(스텁)</text>
  <line x1="321" y1="84" x2="321" y2="98" class="arrow"/>
  <rect x="272" y="98" width="99" height="30" class="box-active"/>
  <text x="278" y="112" class="text">중간 계층: 핵심 인터페이스</text>
  <text x="278" y="122" class="muted">양방향 통합 목표 결합점</text>
  <text x="272" y="148" class="muted">• 하위 계층: 상향식(드라이버)</text>
  <text x="272" y="162" class="muted">• 대규모 분산 환경 최적</text>
  <text x="272" y="176" class="muted">• 설계 복잡도 및 비용 증가</text>

  <!-- 빅뱅 Big-Bang -->
  <rect x="389" y="32" width="117" height="174" class="box"/>
  <text x="397" y="48" class="h-text">4. 빅뱅 (Big-Bang)</text>
  <rect x="397" y="56" width="101" height="42" class="box"/>
  <text x="403" y="73" class="text">모든 모듈 일괄 조립</text>
  <text x="403" y="86" class="muted">단위 테스트 완료 후 동시 결합</text>
  <line x1="447" y1="98" x2="447" y2="112" class="arrow"/>
  <rect x="397" y="112" width="101" height="38" class="box-active"/>
  <text x="403" y="127" class="text">결함 원인 추적 불능</text>
  <text x="403" y="139" class="muted">엔터프라이즈 환경 금기</text>
  <text x="397" y="168" class="muted">• 하네스 작성 비용 없음</text>
  <text x="397" y="182" class="muted">• 일정 지연 리스크 극대화</text>
</svg>
</div>

### 통합 방식별 상세 특징 및 테스트 하네스

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 하향식 통합 (Top-Down)</strong></span>
      <span class="itpe-badge">스텁(Stub) 활용</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>시스템 제어 구조의 상위 모듈부터 아래로 결합해 내려가는 방식</li>
        <li>초기 시스템 골격 시연 가능하나 하위 스텁 제작 공수가 큼</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 상향식 통합 (Bottom-Up)</strong></span>
      <span class="itpe-badge">드라이버(Driver) 활용</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>최하위 모듈을 클러스터로 묶어 가상 드라이버로 테스트 후 상위로 이동</li>
        <li>스텁이 불필요하고 고부하 모듈을 조기 검증하나 상위 골격 완성이 늦음</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 샌드위치 통합 (Sandwich)</strong></span>
      <span class="itpe-badge">하이브리드 절충</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>상위 제어는 하향식, 하위 데이터는 상향식으로 동시 진행하여 중간에서 합류</li>
        <li>대규모 복잡한 프로젝트에 적합하나 테스트 설계 난이도가 높음</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 빅뱅 통합 (Big-Bang)</strong></span>
      <span class="itpe-badge">비점진적 일괄</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>모든 모듈이 끝날 때까지 대기 후 일괄 조립하여 한 번에 시험</li>
        <li>결함 원인 규명이 거의 불가능하여 엔터프라이즈 환경에서는 절대 금기</li>
      </ul>
    </div>
  </div>
</div>

### 모던 MSA 통합 검증: Pact CDC 및 Testcontainers 아키텍처

클라우드 및 마이크로서비스 환경에서는 모든 서비스를 직접 기동하지 않고도 인터페이스 계약을 검증하는 모던 테스팅 파이프라인이 필수적이다.

<div class="itpe-diagram-container" role="img" aria-label="Pact 소비자 주도 계약 테스팅 및 Testcontainers 런타임 통합 파이프라인">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-head2); }
    </style>
    <marker id="arrow-head2" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">모던 클라우드 마이크로서비스 통합 검증 아키텍처 (Pact + Testcontainers)</text>

  <!-- 1. Consumer -->
  <rect x="16" y="36" width="145" height="74" class="box"/>
  <text x="24" y="52" class="h-text">1. 소비자(Consumer) 서비스</text>
  <text x="24" y="67" class="text">API 요구사항 단위 테스트 수행</text>
  <text x="24" y="80" class="muted">기대 응답 명세(Pact JSON) 자동 발행</text>
  <text x="24" y="94" class="muted">Mock 서버 기반 인터페이스 확정</text>

  <!-- 화살표 1->2 -->
  <line x1="161" y1="73" x2="183" y2="73" class="arrow"/>

  <!-- 2. Pact Broker -->
  <rect x="187" y="36" width="146" height="74" class="box-active"/>
  <text x="195" y="52" class="h-text">2. Pact Broker (계약 중앙 저장소)</text>
  <text x="195" y="67" class="text">인터페이스 계약 버전 관리</text>
  <text x="195" y="80" class="muted">소비자-제공자 상호 호환성 매트릭스</text>
  <text x="195" y="94" class="muted">can-i-deploy CLI 배포 승인 통제</text>

  <!-- 화살표 2->3 -->
  <line x1="333" y1="73" x2="355" y2="73" class="arrow"/>

  <!-- 3. Provider -->
  <rect x="359" y="36" width="145" height="74" class="box"/>
  <text x="367" y="52" class="h-text">3. 제공자(Provider) 검증</text>
  <text x="367" y="67" class="text">실제 API 구현체에 계약 재생</text>
  <text x="367" y="80" class="muted">요청 주입 및 실제 응답 스키마 대조</text>
  <text x="367" y="94" class="muted">검증 성공 시 결과 Broker 등록</text>

  <!-- 하단: Testcontainers -->
  <rect x="16" y="126" width="488" height="80" class="box-active"/>
  <text x="26" y="143" class="h-text">4. Testcontainers 기반 실제 런타임 환경 자동화 통합 테스팅</text>
  <text x="26" y="159" class="text">인메모리 H2 가짜 Mock 탈피 ──> 실제 PostgreSQL, Redis, Kafka 컨테이너 동적 생성 및 파기</text>
  <text x="26" y="174" class="muted">• 실제 DBMS 방언(Dialect), 트랜잭션 격리수준, 브로커 메시지 라우팅 100% 동일 검증</text>
  <text x="26" y="189" class="muted">• CI/CD 러너에서 Docker Daemon 자동 제어로 프로덕션 불일치 장애 원천 배제</text>
</svg>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 오픈 2주 전 빅뱅 통합을 시도하다가 수천 개의 런타임 오류가 터져 프로젝트 일정 파탄 | 모듈 완성 즉시 클러스터 단위로 결합하는 점진적 상향식 통합(Bottom-Up) 전략 강제 | 결함 모듈 즉시 격리 및 디버깅 공수 70% 절감 |
| 마이크로서비스 간 DTO 필드명 오타 및 API 변경 사항 미공유로 배포 후 서비스 다운 | 소비자 주도 계약 테스팅(Pact CDC)을 CI 파이프라인에 연동하여 API 호환성 자동 검증 | 인터페이스 스펙 불일치 오류 빌드 시점 100% 차단 |
| 가짜 Mock 객체로만 통합 테스트를 통과시킨 후 운영 DB와 실제 연동 시 SQL 문법 에러 발생 | Testcontainers를 도입하여 실제 PostgreSQL, Redis 컨테이너를 동적으로 띄워 통합 검증 | 프로덕션 환경과의 불일치 결함 완벽 제거 |

## 4. 기술사 답안 차별화 포인트

### MSA 시대의 소비자 주도 계약 테스트(Pact CDC)

수백 개의 마이크로서비스가 얽힌 환경에서는 모든 서비스를 로컬에 다 띄우고 하향식/상향식 테스트를 수행하는 것이 불가능하다. 최신 아키텍처에서는 **Pact 기반의 소비자 주도 계약 테스팅(Consumer-Driven Contract Testing)**을 수행한다. API 소비자가 기대하는 요청/응답 명세(Pact 파일)를 생성하고, 제공자 측 파이프라인에서 이를 실행하여 실제 호환성을 검증하는 모던 통합 테스트 표준을 제시한다.

### Testcontainers 기반의 프로덕션 근접 통합 테스트

과거에는 인메모리 DB(H2)나 가짜 Mock을 사용하다가 실제 Oracle/PostgreSQL의 방언(Dialect) 차이로 장애가 났다. 현대 통합 테스트는 **Testcontainers 라이브러리**를 사용하여 Docker 컨테이너로 실제 DBMS, Kafka, Redis를 테스트 시점에 자동 프로비저닝하고 테스트 후 폐기하는 실무적 테스트 엔지니어링 역량을 강조한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 단위 테스트가 '모듈이 자기 할 일을 제대로 하는가'를 증명한다면, 통합 테스트는 '모듈들이 말을 서로 알아듣는가'를 검증하는 공정이다. 빅뱅 방식의 파멸을 막기 위해 전통적으로는 스텁과 드라이버를 활용한 점진적 통합을 썼고, 클라우드 MSA로 넘어가면서는 Pact와 Testcontainers가 이를 완전히 계승·대체했다.
- [나라면]: 2교시형 문제 출제 시, V-모델 상세설계와 통합 테스트의 관계를 1단락에 도식화하고, 2단락에서 하향식/상향식/샌드위치/빅뱅을 스텁과 드라이버 비용 측면에서 비교하겠다. 3단락에서는 MSA 전환 시 모든 서버를 로컬에 기동할 수 없는 한계를 지적하며, 'Pact CDC 계약 검증 + Testcontainers' 파이프라인을 실무 아키텍처로 제시하여 최고 득점을 확보하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 모듈 간 API 직렬화 스키마 호환성 100% 만족 및 통합 테스트 시 Mock 대체율 30% 이하(실제 컨테이너 기반 검증 비율 70% 이상) 달성 여부
- **대응 방안**: 상위 기획 단계부터 OpenAPI/Proto 명세를 단일 진실 공급원(SSOT)으로 정의하고, Pact Broker 기반 계약 검증과 Testcontainers 런타임 검증을 CI/CD 품질 게이트로 의무화
- **검증 체계**: PR 생성 시 Pact CDC 파이프라인 자동 구동 $\rightarrow$ 하위 호환성 위반 시 빌드 Fail 처리 $\rightarrow$ Testcontainers 통합 시험 통과 시 스테이징 배포 승인
- **기대 효과**: 배포 후 인터페이스 불일치 장애 제로화 및 E2E 테스트 대기 시간 80% 단축으로 일일 다회 무중단 배포 실현

<div class="itpe-pipeline-container" role="img" aria-label="통합 테스트 실전 엔지니어링 파이프라인">
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">01</div>
    <div class="itpe-pipeline-step-content">
      <strong>인터페이스 계약 정의</strong>
      <span>소비자 요구 기반 Pact 명세 작성 및 단위 테스트</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">02</div>
    <div class="itpe-pipeline-step-content">
      <strong>계약 중앙 검증</strong>
      <span>Pact Broker 등록 및 제공자 호환성 자동 검증</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">03</div>
    <div class="itpe-pipeline-step-content">
      <strong>실환경 컨테이너 통합</strong>
      <span>Testcontainers로 실제 DB/MQ 격리 연동 시험</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">04</div>
    <div class="itpe-pipeline-step-content">
      <strong>품질 게이트 승인</strong>
      <span>can-i-deploy 합격 판정 후 프로덕션 배포 이관</span>
    </div>
  </div>
</div>

## 5. 참고 및 연계 학습

- [소프트웨어 테스트 유형 및 레벨](./003_sw_test_types_and_levels.md)
- [블랙박스 테스트(Black-box Test)](./008_black_box_test.md)
- [화이트박스 테스트(White-box Test)](./013_white_box_test.md)
- [회귀 테스트(Regression Test)](./061_regression_test.md)
