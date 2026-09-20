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
      <span>배포 승인 $\rightarrow$ 기존 기능 정상성 보장 및 무결점 프로덕션 릴리스</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (불일치 / Flaky 실패)</strong>
      <span>배포 차단 $\rightarrow$ DOM 셀렉터 깨짐 확인(Self-Healing) 및 회귀 버그 수정</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Capture & Replay(캡처 및 재생)**: 사용자의 수작업 조작이나 실환경 트래픽을 가로채어 파일로 기록하고, 소프트웨어적으로 이를 동일하게 재생하여 검증하는 테스트 방식
- **Test Oracle(테스트 오라클)**: 테스트 실행 결과의 참/거짓을 판별하기 위해 사전에 확립해 둔 판정 기준 또는 기준 정답 데이터(Golden Master)
- **Flaky Test(불안정한 테스트)**: 실제 소스코드 결함이 없음에도 불구하고 네트워크 지연, 비동기 렌더링 타이밍, 일시적 DOM ID 변경으로 인해 간헐적으로 실패하는 테스트
- **Traffic Shadowing (트래픽 미러링)**: 운영 환경에 인입되는 실제 사용자 HTTP/gRPC 트래픽을 백그라운드에서 복제(Record)하여 신규 개발 서버로 실시간 전달(Replay)해 검증하는 기술 (예: GoReplay)
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

```text
+-------------------------------------------------------------------------+
|                  Record and Replay 테스트 시스템 아키텍처               |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 1. Record 단계 ]                                                     |
|    사용자/테스터의 실제 조작 ──> [ 이벤트 캡처 엔진 ]                   |
|                                       │                                 |
|                                       v                                 |
|                              [ 테스트 스크립트 저장소 ]                 |
|                              (DOM 셀렉터, 입력 데이터, 기대 결과)       |
|                                       │                                 |
|  [ 2. Replay 단계 ]                   v                                 |
|    신규 빌드 배포 ──> [ 가상 재생 엔진 ] <── 스크립트 로딩               |
|                              │                                          |
|                              v (가상 이벤트 주입)                       |
|                       [ 테스트 대상 애플리케이션 ]                       |
|                              │                                          |
|                              v 실제 출력값                              |
|                       [ 테스트 오라클 (비교) ] ──> 일치 시 PASS / 불일치 결함 |
+-------------------------------------------------------------------------+
```

### 핵심 2대 단계 및 메커니즘

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 레코드(Record) 메커니즘</strong></span>
      <span class="itpe-badge">이벤트 캡처</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>브라우저 DOM 이벤트 리스너를 가로채어 클릭, 키 입력 수집</li>
        <li>네트워크 레벨에서는 실제 HTTP 패킷을 패킷 스니퍼로 복제</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 리플레이(Replay) 메커니즘</strong></span>
      <span class="itpe-badge">결과 검증</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>저장된 순서와 시간 간격에 맞춰 대리 실행 엔진이 이벤트 주입</li>
        <li>화면 최종 상태 및 API 응답 코드를 기대값과 $1:1$ 자동 대조</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 화면 UI 개편이나 버튼 클래스명 변경으로 녹화된 수백 개 테스트 스크립트 전면 실패 | `data-testid` 의미론적 불변 속성 강제화 및 AI 기반 셀프 힐링(Self-Healing) 셀렉터 도입 | UI 변경 시 스크립트 깨짐 80% 감소 |
| 비동기 AJAX 지연으로 화면 렌더링 전 이벤트가 주입되어 요소 탐색 실패(Flaky Test) | 고정 슬립(`sleep`) 대신 특정 DOM이 나타날 때까지 기다리는 스마트 명시적 대기(Smart Wait) 적용 | 테스트 신뢰도 99% 달성 |
| 데이터베이스 상태 변경으로 인해 동일 요청 리플레이 시 중복 키 에러 및 트랜잭션 충돌 | Testcontainers를 도입하여 테스트 실행 전 도커 DB 샌드박스를 격리 프로비저닝 | DB 데이터 오염 없는 반복 시험 보장 |

## 4. 기술사 답안 차별화 포인트

### GUI를 넘어선 백엔드 운영 트래픽 섀도잉(GoReplay)

현대 엔지니어링에서 Record and Replay는 단순한 GUI 화면 녹화에 머물지 않는다. **GoReplay나 Envoy 트래픽 미러링**을 활용하여 실제 운영 중인 마이크로서비스로 들어오는 수백만 건의 사용자 HTTP 요청을 복제(Record)하고, 이를 차세대 신규 서버로 실시간 전달(Replay)하는 **"트래픽 섀도잉(Traffic Shadowing)"** 기법을 제시한다. 실제 운영 트래픽으로 신규 시스템의 부하와 정합성을 100% 무중단 검증하는 모던 아키텍처 역량을 피력한다.

### Page Object Model(POM)과의 하이브리드 결합

전통적 레코드 도구의 치명적 약점은 유지보수 불능(Maintenance Nightmare)이다. 따라서 실무에서는 레코드 도구(Playwright Codegen)로 초기 뼈대 코드만 고속 추출한 뒤, 즉시 엔지니어가 **Page Object Model(화면 객체와 비즈니스 로직 분리)** 패턴으로 리팩토링하는 하이브리드 운영 전략을 결론으로 제언한다.

## 5. 참고 및 연계 학습

- [회귀 테스트(Regression Test)](./061_regression_test.md)
- [테스트 자동화(Test Automation)](./091_test_automation.md)
- [통합 테스트(Integration Test)](./179_integration_test.md)
- [성능 테스트(Performance Test)](./191_performance_test.md)
