---
title: "소프트웨어 아키텍처 분석(정방향/역방향)"
category: "02-software-engineering"
tags:
  - "소프트웨어아키텍처"
  - "아키텍처분석"
  - "정방향분석"
  - "역방향분석"
  - "ATAM"
  - "DSM"
  - "아키텍처침식"
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
sidebar:
  badge:
    text: "서브"
extra:
  model: "GPT-6"
  keyword_grade: "서브"
---

## 지식 위치

소프트웨어공학 > 아키텍처 설계·평가 > 정방향·역방향 분석

## 큰 그림과 30초 인출

- 본질: 소프트웨어 아키텍처 분석은 요구·설계에서 구조를 평가하고 구현 코드에서 실제 구조를 복원해 비교하는 활동
- 메커니즘: 정방향 품질 요구 분석 ↔ 역방향 코드 구조 복원 → 설계와 구현의 차이·위반 확인
- 산출물: 소프트웨어 아키텍처 기술서(SAD) · ATAM 평가 보고서 · 복원된 아키텍처 모델 · 의존성 구조 매트릭스(DSM) 갭 분석서

<details>
<summary>핵심 용어</summary>

- **정방향 아키텍처 분석(Forward Analysis)**: 비즈니스 요구사항과 품질 속성(성능, 가용성, 보안 등)을 바탕으로 상위 아키텍처 스타일을 결정하고 구조적 타당성을 연역적으로 평가하는 기법
- **역방향 아키텍처 분석(Reverse Analysis)**: 실제 구현된 소스코드와 바이너리를 정적 분석하여 시스템의 실제 구조, 패키지 간 의존 관계, 호출 경로를 귀납적으로 복원하는 기법
- **아키텍처 침식(Architectural Erosion)**: 개발자가 편의를 위해 계층 원칙을 어기고 하위 레이어를 건너뛰거나 순환 참조를 만들어 시스템 구조가 점진적으로 붕괴되는 현상
- **DSM(Design Structure Matrix)**: 모듈 간의 결합과 의존성을 N x N 정방형 매트릭스로 표현하여 순환 참조와 비정상 계층 침범을 가시화하는 분석 도구
</details>

---

## 1교시 예상문제 (10점)

> 소프트웨어 아키텍처 분석(정방향/역방향)의 정의와 목적, 핵심 메커니즘을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 소프트웨어 아키텍처 분석은 요구·설계에서 구조를 평가하고 구현 코드에서 실제 구조를 복원해 비교하는 활동 |
| 목적 | 품질 요구에 맞는 설계 선택과 구현의 구조적 이탈을 확인 |

### 2. 핵심 관계

```text
설계 아키텍처 ─ 기대 의존 관계
구현 소스코드 ─ 실제 의존 관계
    ↓ 코드에서 구조 복원
설계·구현 관계 대조
    ↓
차이·위반 의존성 분석
```

- 제언: 품질속성 시나리오와 구조를 연결해 절충점을 검토하고 설계 결정 근거를 기록
---

## 2~4교시 예상문제 (25점)

> 소프트웨어 아키텍처 분석(정방향/역방향)의 개념과 목적을 설명하고, 핵심 메커니즘과 구성요소·절차, 적용 시 문제점과 대응 방안을 제시하시오. (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 개요 및 필요성

| 구분 | 핵심 |
|---|---|
| 정의 | 소프트웨어 아키텍처 분석은 요구·설계에서 구조를 평가하고 구현 코드에서 실제 구조를 복원해 비교하는 활동 |
| 목적 | 품질 요구에 맞는 설계 선택과 구현의 구조적 이탈을 확인 |

### 의도된 아키텍처와 구현된 아키텍처의 괴리

프로젝트 초기에는 소프트웨어 아키텍트가 정교한 3계층 아키텍처(Presentation - Business - Data)나 헥사고날 아키텍처를 설계한다. 그러나 실제 개발이 진행되고 유지보수가 지속되면서, 개발자들은 빠른 납기를 위해 비즈니스 로직을 건너뛰고 컨트롤러에서 DB를 직접 쿼리하거나, 서비스 간에 양방향 순환 참조를 만드는 등 **설계 원칙을 위반(아키텍처 침식)**하게 된다.

이로 인해 시스템은 점차 스파게티 구조로 전락하여 모듈 분리가 불가능해지고 작은 수정에도 시스템 전체가 마비된다. 따라서 **요구사항으로부터 최적 설계를 도출하는 정방향 분석**과 **구현 코드가 설계를 지키고 있는지 감시하는 역방향 분석**을 상호 연계하는 종합 아키텍처 통제가 필수적이다.

### 정방향 분석 vs 역방향 분석 핵심 비교

| 구분 | 정방향 아키텍처 분석 (Forward) | 역방향 아키텍처 분석 (Reverse) |
|---|---|---|
| **분석 출발점** | 비즈니스 목표, 품질 속성 요구사항 | 실제 소스코드, 설정 파일, 바이너리 |
| **추론 방식** | 연역적 (Top-Down: 요구사항 $\rightarrow$ 설계) | 귀납적 (Bottom-Up: 코드 $\rightarrow$ 아키텍처 복원) |
| **핵심 목적** | 아키텍처 스타일 선정 및 품질 트레이드오프 평가 | 아키텍처 침식 탐지 및 설계-구현 갭(Gap) 검증 |
| **적용 시점** | 아키텍처 수립 및 상세 설계 초기 단계 | 개발 진행 중(CI 연계) 및 레거시 유지보수 단계 |
| **대표 도구** | ATAM, CBAM, ADD(Attribute-Driven Design) | ArchUnit, SonarQube, Structure101, Lattix(DSM) |

### Ⅱ. 아키텍처 및 핵심 메커니즘

### 정방향-역방향 통합 아키텍처 거버넌스 프레임워크

```text
설계 아키텍처 ─ 기대 의존 관계
구현 소스코드 ─ 실제 의존 관계
    ↓ 코드에서 구조 복원
설계·구현 관계 대조
    ↓
차이·위반 의존성 분석
```

### 역방향 분석 4대 핵심 절차

```text
코드·패키지 의존 관계 추출
    ↓
DSM 등으로 결합 관계 표시
    ↓
설계 제약과 차이 분석
    ↓
아키텍처 규칙을 자동 검사에 반영
```

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 소스코드 파싱 (Parsing)</strong></span>
      <span class="itpe-badge">데이터 추출</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>구문 분석기를 통해 소스코드를 추상 구문 트리(AST)로 변환</li>
        <li>클래스 간 import, 상속, 호출, 객체 생성 관계 추출</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 의존성 모델링 (DSM)</strong></span>
      <span class="itpe-badge">구조 가시화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>모듈 간 의존 관계를 N x N 매트릭스(Design Structure Matrix)로 변환</li>
        <li>대각선 상단의 0이 아닌 값을 통해 순환 참조(Circular Dependency) 즉시 식별</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 갭 분석 (Gap Analysis)</strong></span>
      <span class="itpe-badge">침식 판정</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>설계와 일치하는 수렴(Convergence), 누락된 결여(Absence) 판정</li>
        <li>설계 규칙을 위반하여 발생한 불법 발산(Divergence) 라인 적발</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 리팩토링 및 규칙 코드화</strong></span>
      <span class="itpe-badge">재발 방지</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>의존관계 역전 원칙(DIP)을 적용하여 불법 순환 결합 해소</li>
        <li>ArchUnit 단위 테스트 코드로 아키텍처 규칙을 작성하여 CI에 등록</li>
      </ul>
    </div>
  </div>
</div>

### Ⅲ. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 컨트롤러 계층에서 리포지토리 계층을 직접 참조하여 비즈니스 규칙이 우회되는 아키텍처 침식 | ArchUnit 등 아키텍처 검증 도구를 빌드 파이프라인에 연결해 계층 위반을 확인 | 계층 의존 규칙의 반복 검증 |
| 서비스 간 A $\rightarrow$ B $\rightarrow$ C $\rightarrow$ A 순환 참조로 인해 독립 배포 및 단위 테스트 불가 | DSM(Design Structure Matrix) 정적 분석으로 순환 결합점을 탐지하고 인터페이스 분리 및 이벤트(Kafka) 기반 디커플링 | 순환 의존성 원천 제거 및 서비스 독립 배포성 확보 |
| 초기 아키텍처 문서(SAD)가 코드와 동기화되지 않고 사문화되어 설계 지침 무력화 | 아키텍처 규칙을 코드로 관리하고 변경 때 설계와 구현의 차이를 검토 | 문서와 구현 사이의 차이 조기 확인 |

### Ⅳ. 점검 기준

### 아키텍처 무결성 판정 체크리스트

| 점검 영역 | 상세 검증 항목 | 합격 기준 |
|---|---|---|
| **계층 준수** | ArchUnit 기반 단방향 의존 규칙 | 승인되지 않은 위반의 원인·조치 기록 |
| **순환 참조** | DSM 분석을 통한 패키지·서비스 간 순환 결합 여부 | 순환 참조의 영향 범위와 제거 계획 확인 |
| **품질 속성** | ATAM 시나리오에 따른 핵심 응답시간·처리량 검토 | 사업별 목표와 측정 결과의 비교 |
| **설계 일치** | As-Designed 대비 As-Recovered 구성 차이 | 차이의 위험도·승인 여부 기록 |

### Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 예외가 필요한 설계 변경까지 일률 차단하면 팀이 규칙을 우회하거나 승인 절차가 지연될 수 있음 | 아키텍처 경계별 필수 규칙과 예외 가능 항목을 구분하고, 예외에는 근거·책임자·재검토 시점을 기록 |

### 참고 및 연계 학습

- [ATAM(Architecture Tradeoff Analysis Method)](./014_atam.md)
- [CBAM(Cost Benefit Analysis Method)](./076_cbam.md)
- [소프트웨어 아키텍처 스타일](./057_architecture_style.md)
- [리팩토링(Refactoring) 및 코드 냄새](./006_refactoring.md)
---
