---
title: "몽키 테스트(Monkey Test)"
category: "02-software-engineering"
tags:
  - "몽키테스트"
  - "MonkeyTest"
  - "무작위테스팅"
  - "스마트몽키"
  - "덤몽키"
  - "복원력"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 동적 테스팅 기법을 거쳐 몽키 테스트로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>동적 테스팅 기법</span>
  <strong>몽키 테스트(Monkey Test)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 테스터가 사전에 정해둔 시나리오 위주의 테스트 케이스로 발견할 수 없는 예측 불가능한 사용자 오작동과 극한의 예외를 찾아내기 위해, 사전 작성된 테스트 케이스 없이 무작위(Random) 입력과 제스처 이벤트를 대량으로 쏟아부어 시스템 비정상 종료(Crash)를 유도하는 블랙박스 테스팅 기법
- 메커니즘: 의사 난수 시드(Seed) 기반 이벤트 스트림 생성 → UI 컴포넌트 및 API 무작위 주입 → 크래시(Crash) 및 무응답(ANR) 감지 → 시드 기반 이벤트 리플레이를 통한 결함 재현 디버깅
- 산출물: 몽키 테스트 실행 로그(Seed 번호 포함) · 크래시/ANR 스택 트레이스 보고서 · 복원력 분석서

<div class="itpe-flow-map" role="img" aria-label="몽키 테스트 실행 파이프라인 및 결함 재현 루프">
  <div class="itpe-flow-node">
    <strong>1단계: 난수 시드(Seed) 생성 및 파라미터 설정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설정</strong><span>시드 번호 부여 (결함 재현용) · 이벤트 발생 빈도/유형 비율 정의</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 무작위 이벤트 스트림 주입</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>유형</strong><span>터치 연타, 화면 회전, 백그라운드 전환, 임의 문자열 주입</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: 시스템 모니터링 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>수십만 회 이벤트 주입 중 크래시나 메모리 누수가 없는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Pass)</strong>
      <span>비정상 종료 무결성 입증 → 릴리스 안정성 게이트 승인</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (Fail)</strong>
      <span>Crash/ANR 발생 → 시드 기반 재현 및 레이스 컨디션 디버깅</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **덤 몽키(Dumb Monkey)**: 대상 시스템의 내부 상태나 UI 구조에 대한 정보 없이 완전히 무작위로 클릭, 터치, 키 입력을 쏟아붓는 가장 단순한 형태의 무작위 테스팅
- **스마트 몽키(Smart Monkey)**: 시스템의 화면 객체 모델(DOM, View 계층)과 현재 상태를 인식하여, 클릭 가능한 유효 영역 위주로 지능적 이벤트를 주입하는 고도화된 테스팅
- **재현성(Reproducibility)**: 무작위 테스트에서 결함이 터졌을 때 동일한 입력 순서를 재현할 수 있는 능력으로, 난수 발생기의 고정 시드(Seed) 관리가 핵심
- **ANR(Application Not Responding)**: 모바일 앱 메인 스레드가 일정 시간(통상 5초) 이상 멈추어 사용자 입력에 응답하지 못하는 프리징 상태
</details>

## 1. 개요 및 필요성

### 정형 테스트 케이스의 사각지대와 몽키 테스트의 가치

전통적인 소프트웨어 테스팅은 요구사항 명세서를 바탕으로 정상 경로(Happy Path)와 예상 가능한 예외 경로 위주로 테스트 케이스를 설계한다. 그러나 실제 운영 환경에서 일반 사용자는 화면을 빠르게 연타하거나, 화면이 회전하는 도중 홈 버튼을 누르고 복귀하는 등 **개발자가 전혀 상상하지 못한 비정형적이고 극단적인 조작**을 수행한다.

몽키 테스트는 사전 정의된 테스트 케이스 없이, 마치 원숭이가 단말기를 마구 두드리는 것처럼 무작위 이벤트를 쏟아부어 **메모리 누수, 멀티스레드 레이스 컨디션, 예상치 못한 널 포인터 참조로 인한 앱 강제 종료(Crash)를 선제적으로 발굴**한다.

### 몽키 테스트 vs 고릴라 테스트 vs 퍼즈 테스팅 비교

| 구분 | 몽키 테스트 (Monkey Test) | 고릴라 테스트 (Gorilla Test) | 퍼즈 테스팅 (Fuzz Testing) |
|---|---|---|---|
| **테스트 대상** | 애플리케이션 시스템 전체 | **특정 단일 모듈/컴포넌트 집중** | 네트워크 프로토콜, 파일 포맷, API 파서 |
| **주입 데이터** | 무작위 UI 터치, 키 입력, 화면 제스처 | 특정 모듈에 대한 반복적 과부하 입력 | 규격에 맞지 않는 기형적 바이트/패킷 데이터 |
| **핵심 목적** | 비정상 사용자 조작 대비 앱 안정성(Crash) 검증 | 특정 핵심 모듈의 한계 성능 및 파괴 시험 | 보안 취약점(버퍼 오버플로우, 원격 코드 실행) 탐지 |
| **대표 도구** | Android UI/Exerciser Monkey | 커스텀 부하/스트레스 테스트 스크립트 | AFL(American Fuzzy Lop), LibFuzzer |

## 2. 아키텍처 및 핵심 메커니즘

### 덤 몽키 vs 스마트 몽키 아키텍처

```text
+-------------------------------------------------------------------------+
|                  몽키 테스트 분류 및 이벤트 주입 구조                   |
+-------------------------------------------------------------------------+
|  [ 덤 몽키 (Dumb Monkey) ]           [ 스마트 몽키 (Smart Monkey) ]     |
|  - 시스템 화면/상태 무인식           - 현재 UI 계층 트리(View Tree) 인식|
|  - 화면 밖 좌표도 무작위 클릭        - 입력창, 버튼 등 유효 컴포넌트 식별|
|  - 구현 간단하나 깊은 탐색 불가      - 로그인 통과 후 비즈니스 계층 탐색 |
|               │                                      │                  |
|               └──────────────────┬───────────────────┘                  |
|                                  v                                      |
|                   [ 의사 난수 기반 이벤트 주입기 ]                      |
|                      (고정 Seed 기반 이벤트 생성)                       |
|                                  │                                      |
|                                  v                                      |
|                   [ 대상 시스템 (Mobile / Web App) ]                    |
|                                  │                                      |
|                                  v                                      |
|                   [ 크래시 감지 및 Stack Trace 기록 ]                   |
+-------------------------------------------------------------------------+
```

### 몽키 테스트 핵심 실행 단계

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 파라미터 및 시드(Seed) 설정</strong></span>
      <span class="itpe-badge">재현성 확보</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>의사 난수 생성기에 특정 정수 Seed 부여 (동일 시드 입력 시 동일 이벤트 재현)</li>
        <li>터치, 모션, 트랙볼, 시스템 키 이벤트 비율(%) 설정</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 연속 이벤트 주입</strong></span>
      <span class="itpe-badge">부하 유발</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>초당 수십~수백 건의 이벤트를 쉬지 않고 애플리케이션에 전달</li>
        <li>화면 전환, 네트워크 끊김, 배터리 부족 이벤트 병행 시뮬레이션</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 이상 징후 실시간 로깅</strong></span>
      <span class="itpe-badge">결함 감지</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>Logcat 등을 통해 Crash, ANR, OutOfMemory 예외 감지</li>
        <li>장애 발생 직전 100개 이벤트 히스토리와 스택 트레이스 보관</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 회귀 검증 및 리플레이</strong></span>
      <span class="itpe-badge">수정 확인</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>크래시를 유발한 Seed 번호로 몽키 테스트를 재실행하여 버그 재현</li>
        <li>코드 패치 후 동일 Seed 재실행으로 정상 종료 여부 검증</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 수십만 회 무작위 터치 중 크래시가 터졌으나 입력 순서를 몰라 버그 재현 불가 | 난수 생성기의 시드(Seed) 값을 실행 로그에 필수 기록하고 Replay 기능 지원 도구 채택 | 버그 100% 결정론적 재현 및 디버깅 소요 시간 80% 단축 |
| 덤 몽키가 로그인 화면의 빈 공간만 난타하다가 실제 서비스 핵심 화면에 진입하지 못함 | 화면 UI 계층을 파싱하여 폼 입력과 버튼 클릭을 지능적으로 수행하는 스마트 몽키(Appium 등 연계) 적용 | 화면 깊숙한 결제 및 비즈니스 로직 계층 탐색 커버리지 확보 |
| 몽키 테스트 실행 중 실제 운영 DB 결제 승인 또는 계정 삭제 등 파괴적 이벤트 실행 | 테스트 전용 샌드박스 환경 격리 및 치명적 버튼(회원탈퇴, 초기화) 영역 블랙리스트 설정 | 운영 데이터 훼손 방지 및 안전한 무작위 테스트 수행 |

## 4. 기술사 답안 차별화 포인트

### 카오스 엔지니어링(Chaos Monkey)으로의 확장 개념 제시

몽키 테스트를 UI 단말 레벨에만 국한하지 않고, 넷플릭스가 제안한 **클라우드 인프라 레벨의 카오스 몽키(Chaos Monkey)**와 연계하여 서술하면 높은 점수를 얻는다. UI 단말에서 무작위 클릭을 주입하듯, 프로덕션 클라우드 환경에서 무작위로 마이크로서비스 컨테이너를 강제 종료시키거나 네트워크 지연을 인젝션하여 시스템의 자가 복원력(Resilience)을 검증하는 카오스 엔지니어링의 철학적 기반임을 강조한다.

### AI/강화학습 기반의 차세대 자율 몽키 테스팅

최근 연구되는 스마트 몽키는 단순 휴리스틱을 넘어 **강화학습(RL) 및 멀티모달 LLM 에이전트**를 결합하여 발전하고 있다. 화면의 스크린샷과 텍스트 문맥을 스스로 해석하고, 보상 함수(미방문 화면 도달, 크래시 유발)를 극대화하도록 자율 학습하여 인간 테스터보다 빠르게 엣지 케이스 버그를 털어내는 차세대 테스팅 아키텍처를 3단락 또는 결론으로 제시한다.

## 5. 참고 및 연계 학습

- [임베디드 소프트웨어 테스트](./089_embedded_sw_test.md)
- [테스트 자동화(Test Automation)](./091_test_automation.md)
- [카오스 테스트(Chaos Engineering)](./176_chaos_test.md)
- [돌연변이 테스팅(Mutation Test)](./084_mutation_test.md)
