---
title: "동적 테스트(Dynamic Testing)"
author: "Antigravity"
date: "2026-09-20T21:40:00+09:00"
tags:
  - "소프트웨어공학"
  - "동적테스트"
  - "화이트박스"
  - "블랙박스"
  - "테스트오라클"
  - "테스트자동화"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "Gemini 3.8 Flash"
---

> **로드맵 경로**: 소프트웨어공학 > 소프트웨어 테스트 및 품질 > 소프트웨어 테스팅 > 동적 테스트(Dynamic Testing)

---

## 큰 그림과 30초 인출

```text
[동적 테스트(Dynamic Testing)]
 ├── 본질: 실제 런타임 환경에서 코드를 직접 실행(Execution)하여 결함 및 비기능 거동 검증
 ├── 3대 분류: 화이트박스(구조/코드 커버리지) + 블랙박스(명세/동등분할) + 경험기반(탐색적)
 ├── 필수 요소: 테스트 데이터 + 4대 테스트 오라클(참, 샘플링, 휴리스틱, 일관성)
 ├── 정적 vs 동적: 정적(결함 원인/싸게 조기 차단) vs 동적(런타임 고장 입증/실행 필수)
 └── 거버넌스: SonarQube(정적) → JUnit/Testcontainers(동적 단위·통합) → k6/DAST(동적 성능·보안)
```

- **30초 인출 구호**: "실행 기반 런타임 고장 검출! 구조(화이트)와 명세(블랙), 4대 테스트 오라클, 정적-동적 연속 파이프라인!"

---

## 핵심 용어 (5개 내외)

| 핵심 용어 | 영문 표기 | 핵심 정의 및 특징 |
|---|---|---|
| **동적 테스트** | Dynamic Testing | 소프트웨어를 실제 구동 환경에서 실행하며 입력 대비 실제 출력과 기대값을 비교하는 테스트 |
| **테스트 오라클** | Test Oracle | 테스트 실행 결과의 성공/실패 여부를 판단하기 위해 사전에 정의된 참값 및 판별 메커니즘 |
| **화이트박스 테스팅** | White-box Testing | 소프트웨어 내부 소스코드의 제어 흐름과 데이터 경로를 직접 분석하여 검증하는 구조 기반 기법 |
| **블랙박스 테스팅** | Black-box Testing | 내부 구현 코드를 보지 않고 요구사항 명세서 기반으로 입출력의 유효성을 검증하는 명세 기반 기법 |
| **테스트컨테이너** | Testcontainers | 임시 데이터베이스 및 메시지 브로커를 컨테이너로 띄워 동적 테스트의 환경 독립성과 멱등성을 보장하는 기술 |

---

## 25점형 답안 프레임워크

### [예상 문제]
> "소프트웨어 동적 테스트(Dynamic Testing)의 개념과 정적 테스트(Static Testing)와의 차이점을 비교하고, 동적 테스트의 3대 분류 체계(화이트박스, 블랙박스, 경험기반) 및 4대 테스트 오라클의 유형과 CI/CD 파이프라인 내 컨테이너 기반 동적 테스트 자동화 전략을 제시하시오."

---

### Ⅰ. 실제 실행 기반의 런타임 품질 검증, 동적 테스트의 개요

#### 1. 동적 테스트의 정의
- 소프트웨어를 **실제 컴퓨터 환경에서 실행(Execution)하면서 입력값에 따른 실제 출력값과 기대 결과를 비교하여 결함을 검출하고 비기능 품질 속성을 평가하는 테스트 기법**.

#### 2. 동적 테스트의 공학적 필요성
- **런타임 고장(Failure) 검출**: 정적 분석만으로는 식별할 수 없는 동시성 교착상태(Deadlock), 메모리 누수, 응답 지연 등 동적 거동 검증.
- **실행 인프라 정합성 확인**: OS, DB, 네트워크 등 실제 운영 런타임 환경과의 상호작용 검증.

---

### Ⅱ. 정적 테스트 vs 동적 테스트 심층 비교

| 비교 항목 | 정적 테스트 (Static Testing) | 동적 테스트 (Dynamic Testing) |
|---|---|---|
| **실행 여부** | **소프트웨어를 실행하지 않음** (Non-Execution) | **소프트웨어를 직접 실행함** (Execution) |
| **대상 산출물** | 요구사항 명세서, 아키텍처 설계서, 소스코드 텍스트 | 컴파일된 바이너리, 실행 모듈, 컨테이너 인스턴스 |
| **수행 기법** | 워크스루, 인스펙션, 동료검토, SAST 정적 린트 | 화이트박스/블랙박스 테스트, DAST, 성능 부하 테스트 |
| **검출 결함** | 코딩 표준 위반, 문법 오류, 논리적 결함, 설계 누락 | 런타임 메모리 누수, 무한 루프, 동시성 경합, 성능 병목 |
| **결함 수정 비용** | **매우 저렴 (개발 초기 즉시 수정, Shift-Left)** | 상대적으로 고비용 (환경 구축 및 런타임 디버깅 필요) |
| **테스트 오라클** | 불필요 (사전 정의된 체크리스트 대조) | **필수 (기대 결과와 실제 출력값의 비교 기준)** |

---

### Ⅲ. 동적 테스트의 3대 분류 체계 및 4대 테스트 오라클

#### 1. 동적 테스트 3대 분류 체계 및 핵심 기법

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" style="max-width: 520px;">
  <!-- 전체 배경 -->
  <rect x="0" y="0" width="520" height="220" fill="var(--sl-color-bg-page, #ffffff)" rx="8"/>
  
  <!-- 상단: 동적 테스트 본질 -->
  <g transform="translate(15, 12)">
    <rect x="0" y="0" width="490" height="42" rx="5" fill="var(--sl-color-bg-inline-code, #f8fafc)" stroke="var(--sl-color-hairline, #cbd5e1)" stroke-width="1"/>
    <text x="245" y="26" font-size="11" font-weight="700" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">동적 테스트(Dynamic Testing): 코드 직접 실행(Execution) 기반 품질 검증</text>
  </g>

  <!-- 분류 1: 화이트박스 (구조 기반) -->
  <g transform="translate(15, 64)">
    <rect x="0" y="0" width="155" height="142" rx="6" fill="var(--sl-color-primary-subtle, #eff6ff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1.5"/>
    <rect x="0" y="0" width="155" height="28" rx="6" fill="var(--sl-color-primary, #3b82f6)"/>
    <text x="77" y="19" font-size="10.5" font-weight="700" text-anchor="middle" fill="#ffffff">화이트박스 (구조)</text>

    <text x="77" y="48" font-size="9" font-weight="700" text-anchor="middle" fill="var(--sl-color-primary, #1d4ed8)">내부 로직·경로 검증</text>
    <text x="77" y="66" font-size="8" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">구문 / 분기 / 조건</text>
    <text x="77" y="80" font-size="8" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">MC/DC 커버리지</text>
    <text x="77" y="94" font-size="8" text-anchor="middle" fill="var(--sl-color-text-accent, #64748b)">기본 경로 테스팅</text>

    <rect x="15" y="108" width="125" height="22" rx="4" fill="#ffffff" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1"/>
    <text x="77" y="123" font-size="8" font-weight="700" text-anchor="middle" fill="var(--sl-color-primary, #1d4ed8)">단위 테스트 (JUnit)</text>
  </g>

  <!-- 분류 2: 블랙박스 (명세 기반) -->
  <g transform="translate(182, 64)">
    <rect x="0" y="0" width="155" height="142" rx="6" fill="var(--sl-color-success-subtle, #f0fdf4)" stroke="var(--sl-color-success, #22c55e)" stroke-width="1.5"/>
    <rect x="0" y="0" width="155" height="28" rx="6" fill="var(--sl-color-success, #22c55e)"/>
    <text x="77" y="19" font-size="10.5" font-weight="700" text-anchor="middle" fill="#ffffff">블랙박스 (명세)</text>

    <text x="77" y="48" font-size="9" font-weight="700" text-anchor="middle" fill="var(--sl-color-success, #15803d)">입·출력 요구사항 검증</text>
    <text x="77" y="66" font-size="8" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">동등 분할 (EP)</text>
    <text x="77" y="80" font-size="8" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">경계값 분석 (BVA)</text>
    <text x="77" y="94" font-size="8" text-anchor="middle" fill="var(--sl-color-text-accent, #64748b)">상태 전이 / 페어와이즈</text>

    <rect x="15" y="108" width="125" height="22" rx="4" fill="#ffffff" stroke="var(--sl-color-success, #22c55e)" stroke-width="1"/>
    <text x="77" y="123" font-size="8" font-weight="700" text-anchor="middle" fill="var(--sl-color-success, #15803d)">통합/시스템 테스트</text>
  </g>

  <!-- 분류 3: 경험 기반 (직관 기반) -->
  <g transform="translate(350, 64)">
    <rect x="0" y="0" width="155" height="142" rx="6" fill="var(--sl-color-bg-page, #ffffff)" stroke="var(--sl-color-hairline, #94a3b8)" stroke-width="1.5"/>
    <rect x="0" y="0" width="155" height="28" rx="6" fill="var(--sl-color-bg-inline-code, #f8fafc)"/>
    <text x="77" y="19" font-size="10.5" font-weight="700" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">경험 기반 (직관)</text>

    <text x="77" y="48" font-size="9" font-weight="700" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">테스터 노하우·휴리스틱</text>
    <text x="77" y="66" font-size="8" text-anchor="middle" fill="var(--sl-color-text-accent, #64748b)">오류 추정 (Error Guess)</text>
    <text x="77" y="80" font-size="8" text-anchor="middle" fill="var(--sl-color-text-accent, #64748b)">탐색적 테스팅 (ET)</text>
    <text x="77" y="94" font-size="8" text-anchor="middle" fill="var(--sl-color-text-accent, #64748b)">체크리스트 기반 테스팅</text>

    <rect x="15" y="108" width="125" height="22" rx="4" fill="var(--sl-color-bg-inline-code, #f1f5f9)"/>
    <text x="77" y="123" font-size="8" text-anchor="middle" fill="var(--sl-color-text, #0f172a)">인수 테스트 / 버그바운티</text>
  </g>
</svg>
</div>

| 분류 | 검증 대상 | 핵심 기법 | 주요 적용 단계 |
|---|---|---|---|
| **화이트박스 (구조 기반)** | 내부 소스코드 및 제어 흐름 경로 | 구문, 분기, 조건, MC/DC 커버리지 | 단위 테스트 (Unit Test) |
| **블랙박스 (명세 기반)** | 기능 요구사항 명세서의 입출력 관계 | 동등 분할(EP), 경계값 분석(BVA), 페어와이즈 | 통합 및 시스템 테스트 |
| **경험 기반 (직관 기반)** | 명세화되지 않은 엣지 케이스 및 휴리스틱 | 오류 추정(Error Guessing), 탐색적 테스팅 | 인수 테스트, 버그 바운티 |

#### 2. 4대 테스트 오라클(Test Oracle)의 유형
- **참 오라클 (True Oracle)**: 모든 입력에 대해 완벽한 기대 결과를 제공하는 전수 검증 오라클 (미션 크리티컬 항공/원전 시스템).
- **샘플링 오라클 (Sampling Oracle)**: 무한한 입력 중 주요 표본값에 대해서만 사전에 기대 결과를 도출해 검증하는 오라클.
- **휴리스틱 오라클 (Heuristic Oracle)**: 특정 입력값에 대한 근사치나 휴리스틱 알고리즘을 활용해 결과의 유효성을 확률적으로 판단.
- **일관성 오라클 (Consistent Oracle)**: 이전 버전의 실행 결과 또는 경쟁 시스템의 결과와 현재 시스템의 출력을 상호 비교 (회귀 테스트).

---

### Ⅳ. 동적 테스트 운용 시 발생 위험 및 대응 전략

| 위험 | 대책 | 효과 |
|---|---|---|
| **정적 분석 100% 통과 후 실운영 환경에서 OOM 및 자원 고갈 다운** | k6 부하 생성기와 APM 프로파일러를 연동한 24시간 내구 동적 테스트(Soak Test) 수행 | 런타임 메모리 누수 배포 전 100% 사전 색출 |
| **외부 연계망 통신 두절로 인한 동적 통합 테스트 파이프라인 중단** | WireMock 및 Testcontainers 기반 독립적 격리 모킹(Mocking) 환경 구축 | 외부 환경 종속 없는 동적 테스트 멱등성 100% 확보 |
| **GUI 수동 동적 테스트 의존으로 인한 배포 리드타임 수 주 지연** | 테스트 피라미드 재편(단위 동적 테스트 70%, API 20%, E2E 10% 자동화) | 회귀 동적 검증 소요 시간 수 주에서 15분으로 단축 |
| **테스트 기대 결과 산출 불가로 인한 테스트 오라클 부재 문제** | 메타모픽 테스팅(Metamorphic Testing) 및 변이 테스트 연계 검증 | 복잡 알고리즘 및 AI 모델의 동적 검증 가능성 확보 |

---

### Ⅴ. 기술사적 제언: 정적-동적 연속 품질 파이프라인 및 Testcontainers 거버넌스

### 학습자 통찰 메모 — 답안 밖
```text
[핵심 통찰]
정적 테스트와 동적 테스트는 양자택일이 아닌 상호보완적 2중 방어선이다.
정적 테스트는 '결함 원인(Fault)'을 초기에 싼값으로 거르고,
동적 테스트는 실제 메모리 누수·교착상태·응답지연 등 '런타임 고장(Failure)'을 실증한다.
동적 테스트의 최대 걸림돌인 '환경 불일치'와 '테스트 데이터 오염'은
최신 Testcontainers 기술로 임시 인프라를 동적 프로비저닝하고 폐기함으로써 완벽히 해결할 수 있다.

[나라면]
실전 답안에서 정적 vs 동적의 6대 비교축(실행여부, 대상, 결함종류, 비용, 오라클 등)을 선명한 표로 제시하겠다.
그리고 2단락에서 화이트/블랙/경험의 3대 축과 4대 오라클을 다이어그램으로 완결한 후,
3단락에서 Testcontainers를 결합한 CI/CD 연속 품질 게이트를 기술사적 실무 해법으로 강조하겠다.
```

### 실전 답안용 기술사적 제언
- **판정 기준**: 정적 분석(SonarQube 품질 게이트 통과), 동적 커버리지(단위 테스트 분기 커버리지 80% 이상), 테스트 오라클 판정 결과(참/샘플링 검증 합격률 100%)를 기준으로 배포 가능 여부를 자동 판정함.
- **대응 방안**: 단위 레벨 화이트박스(JaCoCo)와 API 레벨 블랙박스(RestAssured)를 선행하고, Testcontainers를 통해 외부 DB/Kafka 환경을 독립 격리하여 동적 테스트의 멱등성을 확보함.
- **검증 체계**: 메타모픽 관계(Metamorphic Relation)를 수립하여 복잡 계산 및 AI 영역의 테스트 오라클 부재 문제를 해결하고, k6 기반 런타임 성능 부하 검증을 필수화함.
- **기대 효과**: 환경 불일치로 인한 Flaky Test를 95% 제거하고, 런타임 동시성 장애 및 OOM 결함을 사전에 100% 차단함.

```text
[정적 분석: SonarQube] ──> [격리 동적 검증: Testcontainers] ──> [비기능 동적 부하: k6] ──> [프로덕션 무중단 배포]
(결함 원인 조기 차단)       (단위·통합 멱등성 보장)              (동시성 및 메모리 검증)
```

---

## 1교시 10점형 답안 발췌 (핵심 서술형)

- **동적 테스트(Dynamic Testing)**는 소프트웨어를 실제 런타임 환경에서 실행(Execution)하면서 입력 대비 출력값을 기대 결과(Test Oracle)와 비교하여 기능 및 비기능 결함을 검출하는 활동이다.
- 코드를 실행하지 않는 **정적 테스트(인스펙션, SAST)**와 달리 메모리 누수, 교착상태 등 실제 런타임 거동을 검증하며, 구조 기반의 **화이트박스**, 명세 기반의 **블랙박스**, 직관 기반의 **경험기반 테스트**로 분류된다. 최근에는 Testcontainers 기술을 결합하여 격리된 컨테이너 환경에서 동적 테스트를 100% 자동화하는 추세이다.

---

## 출제 이력 및 기출 분석

- **정보관리기술사**: 86회, 101회, 117회, 137회 (정적 테스트와 동적 테스트의 비교, 화이트박스 커버리지, 동적 테스트 기법 융합)
- **컴퓨터시스템응용기술사**: 97회, 115회, 129회 (동적 테스팅 분류 체계, 테스트 오라클의 4대 유형, 성능/부하 테스트)
- **출제 경향성**: 137회 2교시 기출과 같이 정적/동적 테스트의 단순 대비를 넘어, SDLC 각 단계별 최적 매핑 전략 및 런타임 동적 테스트를 위한 테스트 오라클 해결 방안, CI/CD 자동화 도구 연계 모델을 제시할 때 최고 득점으로 연결됨.

---

## 실전 작성 팁 & 감점 방지

- **정적-동적 테스트 대비표 필수**: 1단락 또는 2단락에서 실행 여부, 대상, 검출 결함, 수정 비용 등 6개 이상의 비교축을 가진 표를 반드시 제시할 것.
- **4대 테스트 오라클 언급**: 참, 샘플링, 휴리스틱, 일관성 오라클의 개념을 명확히 구분하여 작성할 것.
- **현대적 도구 명시**: 화이트박스 커버리지 도구(JaCoCo), 컨테이너 격리 도구(Testcontainers), 부하 도구(k6) 등 구체적인 툴셋을 명시할 것.

---

## 연결 토픽

- [인스펙션(Inspection)](./058_inspection.md) : 소프트웨어를 실행하지 않는 대표적 정형 정적 테스트
- [회귀테스트](./061_regression_test.md) : 변경 후 동적 회귀 결함을 차단하는 자동화 테스트 기법
- [소프트웨어 테스트 원리](./070_software_testing_principles.md) : ISTQB 7대 기본 공리와 결함 집중의 원리
- [메타모픽 테스팅](./030_metamorphic_test.md) : 테스트 오라클 부재 문제를 극복하는 특수 동적 테스팅 기법

