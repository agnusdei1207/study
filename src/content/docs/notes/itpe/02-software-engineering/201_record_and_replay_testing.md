---
title: "Record and Replay 테스트 기법"
category: "02-software-engineering"
tags:
  - "RecordAndReplay"
  - "테스트자동화"
  - "회귀테스트"
  - "FlakyTest"
  - "GoReplay"
  - "트래픽섀도잉"
  - "PageObjectModel"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 테스팅과 테스트 자동화를 거쳐 Record and Replay 테스트 기법으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 테스팅·테스트 자동화</span>
  <strong>Record and Replay 테스트 기법</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 사용자의 GUI 마우스/키보드 입력 행위나 실제 운영 환경의 네트워크 패킷을 실시간 가로채어 기록(Record)한 뒤, 소스코드 수정 및 신규 배포 시 동일하게 재생(Replay)하여 이전과 똑같이 정상 동작하는지 검증하고 회귀 결함을 조기 발견하는 테스트 자동화 기법
- 메커니즘: 사용자 인터랙션 캡처 $\rightarrow$ 테스트 스크립트 및 기대값(Golden Master) 저장 $\rightarrow$ 신규 빌드 대상 가상 이벤트 주입 재생 $\rightarrow$ 테스트 오라클(Oracle) 비교 검증 $\rightarrow$ 회귀 결함 판정
- 산출물: 캡처된 테스트 스크립트 파일 · 기대 결과 데이터셋 · 회귀 시험 성적서 · 트래픽 리플레이 로그

<div class="itpe-flow-map" role="img" aria-label="Record and Replay 테스트 수행 및 회귀 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 사용자 조작 캡처 및 레코딩 (Record)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>기록</strong><span>마우스 클릭, 텍스트 입력, API 요청 패킷을 이벤트 단위로 가로채어 저장</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 테스트 스크립트 및 오라클 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>명세</strong><span>DOM 셀렉터, 파라미터 및 기준 기대값(Golden Master) 자동 생성</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 신규 시스템 대상 자동 재생 (Replay)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>재생</strong><span>신규 배포된 앱에 가상 이벤트를 자동 주입하여 실제 실행 결과 도출</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 회귀 결함 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>재생 결과가 기대 오라클과 100% 일치하며 회귀 결함이나 Flaky 에러가 없는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (회귀 검증 합격)</strong>
      <span>신규 버전 릴리스 승인 $\rightarrow$ 프로덕션 배포 파이프라인 통과</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (화면 깨짐 / 불일치)</strong>
      <span>배포 보류 $\rightarrow$ UI 변경 여부 확인 후 스크립트 갱신 또는 결함 티켓 발행</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **테스트 오라클(Test Oracle)**: 테스트 수행 결과가 참인지 거짓인지를 판단하기 위해 사전에 정의된 참값(기대 결과값)을 제공하는 기준 메커니즘
- **Flaky Test (간헐적 실패 테스트)**: 소스코드에 아무런 변경이 없음에도 타이밍, 네트워크 지연, 비동기 렌더링 속도 차이로 인해 성공과 실패를 무작위로 오가는 불안정한 테스트
- **골든 마스터(Golden Master)**: 레코딩 시점에 정상적으로 생성된 시스템의 스크린샷, 응답 JSON, DB 스냅샷을 기준 원본으로 삼아 변경분을 대조하는 회귀 기법
- **트래픽 섀도잉(Traffic Shadowing)**: 운영 환경의 실제 인입 HTTP 패킷을 백그라운드에서 복제(GoReplay 등)하여 스테이징 신규 버전 서버로 무해하게 실시간 리플레이하는 기법
</details>

## 1. 개요 및 필요성

### 수작업 회귀 테스트의 한계와 자동화의 진입 장벽

소프트웨어 기능이 추가될 때마다 기존에 잘 돌아가던 기능이 깨지지 않았는지 확인하는 "회귀 테스트(Regression Test)" 공수는 기하급수적으로 폭증한다. 그러나 코딩 기반의 E2E 테스트(Selenium, Playwright)를 일일이 작성하는 것은 높은 숙련도와 많은 시간이 소요된다.

Record and Replay 기법은 **비전문가도 실제 화면을 조작하는 것만으로 신속하게 테스트 스크립트를 생성**할 수 있도록 지원하여, 테스트 자동화의 초기 구축 속도를 극대화하는 실용적 테스팅 기법이다.

### 레코드 & 리플레이 vs 코드 기반 E2E vs 키워드 주도 테스트 비교

| 구분 | 레코드 & 리플레이 (Record & Replay) | 코드 기반 E2E 테스트 (Playwright 등) | 키워드 주도 테스트 (Robot Framework) |
|---|---|---|---|
| **스크립트 생성**| **사용자 조작을 화면 녹화하듯 자동 생성** | **개발자/QA가 직접 프로그래밍 코딩** | 스프레드시트에 정의된 키워드 조합 |
| **작성 난이도** | **매우 낮음 (비개발자도 즉시 가능)** | 높음 (테스트 프레임워크 지식 필요) | 보통 (테이블 정의 수준) |
| **유지보수성** | **취약 (UI 변경 시 스크립트 깨짐 빈번)** | **우수 (Page Object Model 모듈화)** | 우수 (키워드 매핑 테이블만 수정) |
| **실행 신뢰도** | 낮음 (Flaky Test 발생 위험) | **높음 (스마트 대기 및 예외 처리 견고)** | 높음 |
| **대표 도구** | Selenium IDE, Cypress Studio, GoReplay | Playwright, Selenium WebDriver | Robot Framework |

## 2. 아키텍처 및 핵심 메커니즘

### Record and Replay 테스트 시스템 아키텍처

레코드 단계와 리플레이 단계의 유기적 상호작용 아키텍처이다.

<div class="itpe-diagram-container" role="img" aria-label="Record 단계 캡처 및 Replay 단계 오라클 대조 아키텍처">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-rr); }
    </style>
    <marker id="arrow-rr" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">Record and Replay 테스트 2단계 시스템 아키텍처</text>

  <!-- 상단: 1. Record 단계 -->
  <rect x="16" y="34" width="488" height="74" class="box"/>
  <text x="24" y="48" class="h-text">[1. Record 단계: 실사용자 인터랙션 캡처]</text>

  <rect x="24" y="56" width="120" height="42" class="box-active"/>
  <text x="30" y="70" class="text">사용자/테스터 조작</text>
  <text x="30" y="82" class="muted">마우스 클릭, 키보드 입력</text>
  <line x1="144" y1="77" x2="168" y2="77" class="arrow"/>

  <rect x="170" y="56" width="140" height="42" class="box"/>
  <text x="176" y="70" class="h-text">이벤트 캡처 엔진</text>
  <text x="176" y="82" class="muted">DOM 이벤트 및 HTTP 패킷</text>
  <line x1="310" y1="77" x2="334" y2="77" class="arrow"/>

  <rect x="336" y="56" width="158" height="42" class="box-active"/>
  <text x="342" y="70" class="h-text">골든 마스터 (Golden Master)</text>
  <text x="342" y="82" class="muted">스크립트 파일 및 기대값 DB 저장</text>

  <!-- 하단: 2. Replay 단계 -->
  <rect x="16" y="118" width="488" height="88" class="box-active"/>
  <text x="24" y="132" class="h-text">[2. Replay 단계: 신규 빌드 대상 자동 재생 및 회귀 검증]</text>

  <rect x="24" y="140" width="120" height="48" class="box"/>
  <text x="30" y="154" class="text">신규 배포 시스템</text>
  <text x="30" y="166" class="muted">수정된 신규 빌드</text>
  <line x1="144" y1="164" x2="168" y2="164" class="arrow"/>

  <rect x="170" y="140" width="140" height="48" class="box-active"/>
  <text x="176" y="154" class="h-text">가상 재생 엔진 (Replay)</text>
  <text x="176" y="166" class="muted">스크립트 로딩 ➔ 이벤트 주입</text>
  <line x1="310" y1="164" x2="334" y2="164" class="arrow"/>

  <rect x="336" y="140" width="158" height="48" class="box"/>
  <text x="342" y="154" class="h-text">테스트 오라클 판정</text>
  <text x="342" y="166" class="muted">실제 결과값 vs 골든 마스터 비교</text>
  <text x="342" y="178" fill="#10b981" font-size="6.8px" font-weight="bold">일치 시 PASS / 불일치 시 회귀 결함</text>
</svg>
</div>

### 모던 백엔드 진화: GoReplay 기반 프로덕션 트래픽 섀도잉

GUI 캡처의 취약점을 극복하고 백엔드 서버의 실제 운영 트래픽을 복제하여 검증하는 모던 테스팅 아키텍처이다.

<div class="itpe-diagram-container" role="img" aria-label="GoReplay 기반 프로덕션 트래픽 미러링 및 스테이징 섀도우 검증 아키텍처">
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
      .arrow { stroke: var(--color-border-strong, #64748b); stroke-width: 1.2; marker-end: url(#arrow-gor); }
    </style>
    <marker id="arrow-gor" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="4" markerHeight="4" orient="auto">
      <path d="M 0 0 L 6 3 L 0 6 z" fill="var(--color-border-strong, #64748b)"/>
    </marker>
  </defs>
  <rect width="520" height="220" class="bg" rx="8"/>
  <text x="16" y="20" class="title">모던 트래픽 섀도잉: GoReplay 패킷 미러링 및 비침해적 검증 아키텍처</text>

  <!-- 실사용자 -->
  <rect x="16" y="45" width="95" height="50" class="box"/>
  <text x="24" y="65" class="h-text">실제 실사용자</text>
  <text x="24" y="78" class="muted">운영 HTTP 요청</text>
  <line x1="111" y1="70" x2="140" y2="70" class="arrow"/>

  <!-- 운영 서버 (Prod) -->
  <rect x="140" y="40" width="150" height="60" class="box-active"/>
  <text x="148" y="58" class="h-text">프로덕션 웹 서버 (Prod)</text>
  <text x="148" y="72" class="text">정상 비즈니스 처리 및 응답 반환</text>
  <text x="148" y="86" class="muted">[GoReplay Agent]: 네트워크 패킷 캡처</text>

  <!-- 패킷 미러링 화살표 -->
  <line x1="215" y1="100" x2="215" y2="135" class="arrow"/>
  <text x="220" y="120" fill="#38bdf8" font-size="6.8px">비침해적 패킷 복제 (Shadowing)</text>

  <!-- 스테이징 신규 버전 서버 -->
  <rect x="140" y="135" width="364" height="65" class="box-active"/>
  <text x="148" y="152" class="h-text">신규 릴리스 검증 서버 (Shadow Staging: 새 버전 코드)</text>
  <text x="148" y="167" class="text">실제 운영 트래픽을 100% 동일하게 재생(Replay)하여 응답 정합성 검증</text>
  <text x="148" y="180" class="muted">• 쓰기(Write) 요청은 Mock 처리하여 실제 운영 DB 오염 완벽 방지</text>
  <text x="148" y="191" class="muted">• 가짜 데이터가 아닌 100% 실제 유저 트래픽으로 극한의 엣지 케이스 사전 적발</text>
</svg>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 프론트엔드 버튼 위치나 HTML id가 바뀌어 재생 시 요소를 못 찾아 스크립트가 깨짐 | 절대 좌표나 자동 생성 id 대신, 비즈니스 의미를 담은 `data-testid` 속성 기반 셀렉터 지정 | UI 변경 시 테스트 스크립트 파손율 80% 감축 |
| 네트워크 비동기 지연으로 요소가 미처 뜨기 전에 클릭하여 테스트가 실패하는 Flaky 현상 | 하드코딩된 `sleep()`을 금지하고, DOM 요소가 나타날 때까지 스마트 대기하는 `waitForSelector` 적용 | 간헐적 Flaky Test 실패율 95% 제거 |
| 운영 트래픽 섀도잉(GoReplay) 중 결제 승인 등 CUD 요청이 실제 외부 결제망으로 재전송 | 결제, 이메일 등 외부 부수효과(Side-Effect)를 유발하는 API 엔드포인트는 리플레이 필터링 또는 가상 Mock 격리 | 운영 데이터베이스 오염 및 금전 사고 원천 차단 |

## 4. 기술사 답안 차별화 포인트

### Page Object Model(POM)과의 결합을 통한 유지보수성 혁신

순수 Record and Replay 도구는 UI가 조금만 바뀌어도 수백 개의 스크립트를 다시 녹화해야 하는 '유지보수의 지옥'을 초래한다. 기술사 답안에서는 녹화된 스크립트를 그대로 쓰지 않고, **화면의 요소를 객체화하여 분리하는 Page Object Model(POM)** 구조로 변환하여 관리하는 실무적 프레임워크를 제시한다. UI가 변경되더라도 Page 클래스의 셀렉터 한 줄만 수정하면 모든 테스트가 유지되는 성숙한 엔지니어링을 강조한다.

### 카나리 배포(Canary)와 트래픽 미러링(Traffic Shadowing)의 결합

최신 클라우드 네이티브 환경에서는 GUI 녹화 대신 **네트워크 수준의 Record & Replay(GoReplay, Istio Traffic Mirroring)**가 대세이다. 실제 사용자에게 영향을 주지 않고 운영 트래픽을 그대로 복제하여 신규 컨테이너로 흘려보냄으로써, 수천 가지의 예측 불가능한 사용자 입력 패턴을 사전에 100% 검증하는 **무결점 카나리 릴리스 파이프라인**을 결론으로 제언한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: Record and Replay는 '양날의 검'이다. 처음 만들 때는 5분 만에 끝나서 감탄하지만, UI가 바뀌는 순간 모든 스크립트가 쓰레기가 된다. 그래서 실무에서는 순수 녹화에만 의존하지 않고 `data-testid` 기반 POM으로 감싸거나, 네트워크 수준의 GoReplay 섀도잉으로 전환하는 것이 정답이다.
- [나라면]: 1교시형 단답 시 Record ➔ Script/Oracle ➔ Replay의 3단계를 도식화하고 Flaky Test 해결 방안을 명시하겠다. 2교시형 출제 시에는 GUI 레코드의 한계(유지보수 취약)를 지적하고, 이를 극복한 POM(Page Object Model) 리팩토링과 백엔드 트래픽 미러링(GoReplay/Istio) 실무 파이프라인을 기술사적 해법으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 회귀 테스트 수행 시 스크립트 자가 복원율 90% 이상 및 Flaky Test 발생률 2% 이하 통제 여부
- **대응 방안**: 레코드 도구 도입 시 data-testid 표준 명명 규칙을 적용하고, 백엔드는 GoReplay 트래픽 섀도잉을 CI/CD 품질 게이트로 연동
- **검증 체계**: 신규 배포 빌드 ➔ 가상 이벤트 주입 ➔ 골든 마스터 오라클 대조 ➔ 결함 자동 리포팅
- **기대 효과**: 회귀 테스트 작성 공수 70% 단축, 배포 전 잠재적 런타임 결함 조기 적발 및 무중단 배포 신뢰성 확보

<div class="itpe-pipeline-container" role="img" aria-label="Record and Replay 자동화 엔지니어링 파이프라인">
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">01</div>
    <div class="itpe-pipeline-step-content">
      <strong>인터랙션/패킷 캡처</strong>
      <span>UI 사용자 조작 및 운영 네트워크 패킷 레코딩</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">02</div>
    <div class="itpe-pipeline-step-content">
      <strong>골든 마스터 정제</strong>
      <span>data-testid 기반 POM 변환 및 기대 오라클 확정</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">03</div>
    <div class="itpe-pipeline-step-content">
      <strong>스마트 리플레이</strong>
      <span>신규 빌드 대상 이벤트 주입 및 비동기 대기 동기화</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">➔</div>
  <div class="itpe-pipeline-step">
    <div class="itpe-pipeline-step-num">04</div>
    <div class="itpe-pipeline-step-content">
      <strong>회귀 결함 게이트</strong>
      <span>오라클 불일치 시 배포 자동 차단 및 결함 격리</span>
    </div>
  </div>
</div>

## 5. 참고 및 연계 학습

- [통합 테스트(Integration Test)](./179_integration_test.md)
- [회귀 테스트(Regression Test)](./061_regression_test.md)
- [성능 테스트(Performance Test)](./191_performance_test.md)
- [카오스 테스트(Chaos Engineering)](./176_chaos_test.md)
