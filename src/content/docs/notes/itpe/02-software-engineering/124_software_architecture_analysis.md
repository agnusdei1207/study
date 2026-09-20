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
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 아키텍처 설계 및 평가를 거쳐 아키텍처 분석으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>아키텍처 설계·평가</span>
  <strong>소프트웨어 아키텍처 분석(정방향/역방향)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 소프트웨어 개발 및 유지보수 과정에서 설계 문서와 실제 구현 코드 간의 간극이 벌어지는 아키텍처 침식(Erosion)을 방지하기 위해, 요구사항으로부터 최적 구조를 도출·평가하는 정방향(Forward) 분석과 소스코드로부터 실제 구조를 역추출하여 설계 일치성을 검증하는 역방향(Reverse) 분석을 통합 적용하는 무결성 보증 기법
- 메커니즘: 정방향(품질 속성 시나리오 도출 → 스타일 선정 → ATAM/CBAM 평가) ↔ 역방향(코드 파싱 → 의존성 행렬 DSM 추출 → 의도된 설계 대비 갭 분석 및 아키텍처 규칙 검증)
- 산출물: 소프트웨어 아키텍처 기술서(SAD) · ATAM 평가 보고서 · 복원된 아키텍처 모델 · 의존성 구조 매트릭스(DSM) 갭 분석서

<div class="itpe-flow-map" role="img" aria-label="소프트웨어 아키텍처 정방향 및 역방향 분석 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 정방향 분석 (Forward Analysis)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>흐름</strong><span>비즈니스 목표/품질 속성 요구사항 → 아키텍처 스타일 선정 → ATAM/CBAM 평가</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓ (구현 Implementation)</div>
  <div class="itpe-flow-node">
    <strong>2단계: 소스코드 및 바이너리 자산</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>현실</strong><span>일정 압박 및 편의적 코딩으로 인한 불법 참조 및 기술 부채 누적</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓ (역공학 Reverse Engineering)</div>
  <div class="itpe-flow-node">
    <strong>3단계: 역방향 분석 (Reverse Analysis)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>추출</strong><span>코드 AST 파싱 → 컴포넌트 호출 관계 복원 → DSM(Design Structure Matrix) 도출</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: Gap 분석 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>복원된 구조가 의도된 아키텍처 계층과 규칙을 완벽히 준수하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Pass)</strong>
      <span>아키텍처 일치 입증 → CI/CD 메인 브랜치 머지 승인</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (Fail)</strong>
      <span>아키텍처 침식/순환 참조 식별 → DIP 리팩토링 강제</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **정방향 아키텍처 분석(Forward Analysis)**: 비즈니스 요구사항과 품질 속성(성능, 가용성, 보안 등)을 바탕으로 상위 아키텍처 스타일을 결정하고 구조적 타당성을 연역적으로 평가하는 기법
- **역방향 아키텍처 분석(Reverse Analysis)**: 실제 구현된 소스코드와 바이너리를 정적 분석하여 시스템의 실제 구조, 패키지 간 의존 관계, 호출 경로를 귀납적으로 복원하는 기법
- **아키텍처 침식(Architectural Erosion)**: 개발자가 편의를 위해 계층 원칙을 어기고 하위 레이어를 건너뛰거나 순환 참조를 만들어 시스템 구조가 점진적으로 붕괴되는 현상
- **DSM(Design Structure Matrix)**: 모듈 간의 결합과 의존성을 N x N 정방형 매트릭스로 표현하여 순환 참조와 비정상 계층 침범을 가시화하는 분석 도구
</details>

## 1. 개요 및 필요성

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

## 2. 아키텍처 및 핵심 메커니즘

### 정방향-역방향 통합 아키텍처 거버넌스 프레임워크

```text
+-------------------------------------------------------------------------+
|                  아키텍처 정방향-역방향 닫힌 루프(Closed-Loop)          |
+-------------------------------------------------------------------------+
|      [ 정방향: 비즈니스 요구사항 ]                                      |
|                 │                                                       |
|                 │ 1. ATAM 품질 속성 시나리오 평가                        |
|                 v                                                       |
|      [ 의도된 아키텍처 (As-Designed) ]                                  |
|                 │                                                       |
|                 │ 2. 개발 구현 (Coding)                                 |
|                 v                                                       |
|      [ 실제 구현 코드 (As-Implemented) ]                                |
|                 │                                                       |
|                 │ 3. AST 파싱 및 DSM 의존성 추출                         |
|                 v                                                       |
|      [ 복원된 아키텍처 (As-Recovered) ]                                 |
|                 │                                                       |
|                 v                                                       |
|      +─────────────────────────────────────────────────────────────+    |
|      |  4. 아키텍처 일치성 검증 (Architecture Conformance Checking) |    |
|      |     - 합법적 의존성(Convergence), 불법 침식(Absence/Divergence)|  |
|      +─────────────────────────────────────────────────────────────+    |
+-------------------------------------------------------------------------+
```

### 역방향 분석 4대 핵심 절차

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

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 컨트롤러 계층에서 리포지토리 계층을 직접 참조하여 비즈니스 규칙이 우회되는 아키텍처 침식 | Java의 ArchUnit 등 아키텍처 검증 라이브러리를 빌드 파이프라인에 탑재하여 계층 위반 시 빌드 자동 실패 처리 | 계층형 아키텍처 원칙 100% 강제 및 유지보수성 보호 |
| 서비스 간 A $\rightarrow$ B $\rightarrow$ C $\rightarrow$ A 순환 참조로 인해 독립 배포 및 단위 테스트 불가 | DSM(Design Structure Matrix) 정적 분석으로 순환 결합점을 탐지하고 인터페이스 분리 및 이벤트(Kafka) 기반 디커플링 | 순환 의존성 원천 제거 및 서비스 독립 배포성 확보 |
| 초기 아키텍처 문서(SAD)가 코드와 동기화되지 않고 사문화되어 설계 지침 무력화 | 아키텍처 규칙을 코드(Architecture as Code)로 저장소에 보관하고 다이어그램을 소스코드로부터 자동 역생성 | 문서와 코드 간의 1:1 일치성 상시 유지 |

## 4. 기술사 답안 차별화 포인트

### ArchUnit을 활용한 "Architecture as Code" 실현

아키텍처 분석이 연 1회 형식적인 감사업무로 전락하지 않으려면 **CI/CD 파이프라인과의 실시간 통합**이 핵심이다. 답안에 Java 환경의 `ArchUnit` 실무 코드 패턴(`classes().that().resideInAPackage("..controller..").should().onlyDependOnClassesThat().resideInAnyPackage("..service..")`)을 예시로 제시하고, 개발자가 PR을 올릴 때마다 아키텍처 규칙 위반 여부를 단위 테스트처럼 자동 검증하는 DevSecOps 아키텍처 가드레일을 설명하면 실무 역량을 강하게 어필할 수 있다.

### 소프트웨어 현대화(Modernization) 시 역방향 분석의 전략적 가치

수백만 라인의 레거시 모놀리스를 마이크로서비스(MSA)로 전환할 때 가장 큰 장애물은 "문서가 없고 코드가 너무 꼬여 있어 어디를 잘라야 할지 모른다"는 점이다. 이때 역방향 분석 도구(DSM)를 적용하여 데이터베이스 테이블 공유 관계와 도메인 간 결합도를 먼저 시각화하고, **도메인 주도 설계(DDD)의 Bounded Context 경계를 도출하는 마이그레이션 전략**을 3단락 또는 결론으로 제시한다.

## 5. 참고 및 연계 학습

- [ATAM(Architecture Tradeoff Analysis Method)](./014_atam.md)
- [CBAM(Cost Benefit Analysis Method)](./076_cbam.md)
- [소프트웨어 아키텍처 스타일](./057_architecture_style.md)
- [리팩토링(Refactoring) 및 코드 냄새](./006_refactoring.md)
