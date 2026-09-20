---
title: "테스트 커버리지(Test Coverage)"
category: "02-software-engineering"
tags:
  - "테스트커버리지"
  - "코드커버리지"
  - "기능커버리지"
  - "RTM"
  - "ExitCriteria"
  - "QualityGate"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 테스팅 및 품질 관리를 거쳐 테스트 커버리지로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>테스팅·품질 관리</span>
  <strong>테스트 커버리지(Test Coverage)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: "테스트를 충분히 수행했는가"와 "언제 테스트를 종료할 것인가"를 정량적으로 증명하기 위해, 시스템의 요구사항 명세(기능)와 소스코드 내부 구조(구문·분기) 대비 테스트 케이스가 실제로 통과한 검증 비율을 백분율(%)로 계측하는 품질 완료 판정 지표
- 메커니즘: 검증 기준 수립 → 테스트 케이스 실행 및 동적 계측(Instrumentation) → 기능·구조 다차원 커버리지 수집 → 미달 구간 보완 → 테스트 완료 기준(Exit Criteria) 및 Quality Gate 판정
- 산출물: 요구사항 추적 매트릭스(RTM) 커버리지 표 · 코드 커버리지 계측 보고서(JaCoCo, Coverage.py) · 테스트 완료 보고서 · 품질 게이트 승인 기록

<div class="itpe-flow-map" role="img" aria-label="테스트 커버리지 측정 파이프라인 및 Quality Gate 판정 흐름">
  <div class="itpe-flow-node">
    <strong>1단계: 커버리지 목표 및 기준 수립</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설정</strong><span>기능 요구사항 100% (RTM) · 핵심 모듈 분기 80% 이상</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 테스트 실행 및 동적 계측</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>도구</strong><span>동적 바이트코드 계측(JaCoCo) · 명세 기반 RTM 매핑 실행</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: Quality Gate (종료 기준 판정)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>기능 100% 및 목표 코드 커버리지를 모두 충족하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Pass)</strong>
      <span>테스트 공식 종료(Exit Criteria) → 운영 배포 승인</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (Fail)</strong>
      <span>미달 영역 식별 → 보완 테스트 케이스 추가 작성</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **테스트 커버리지(Test Coverage)**: 시스템의 전체 검증 대상(요구사항, 소스코드, 인터페이스 등) 중 작성된 테스트 케이스를 통해 실제로 테스트가 수행된 영역의 비율
- **기능 커버리지(Functional Coverage)**: 사용자의 업무 요구사항 명세서 및 유스케이스 대비 테스트 케이스가 누락 없이 매핑되어 실행되었는지를 나타내는 블랙박스 관점의 지표
- **구조적 코드 커버리지(Code Coverage)**: 프로그램 소스코드의 구문(Statement), 분기(Branch), 조건(Condition), MC/DC 중 테스트 실행 시 실제로 거쳐 간 코드 라인의 비율
- **테스트 완료 기준(Exit Criteria)**: 사전에 정의된 품질 및 일정 목표로, 특정 커버리지 임계치와 잔존 결함 기준을 만족해야 테스트 단계를 종료할 수 있도록 규정한 정책
</details>

## 1. 개요 및 필요성

### 테스트 종료 시점의 불확실성과 커버리지의 역할

소프트웨어 개발 프로젝트에서 가장 빈번하게 발생하는 딜레마는 **"과연 테스트를 어디까지 해야 충분하며, 언제 배포를 승인할 것인가?"**이다. 주관적인 판단이나 단순한 테스트 수행 횟수(건수)에 의존할 경우, 중요 비즈니스 로직이 전혀 검증되지 않은 상태에서 납기 압박으로 인해 결함이 운영 환경으로 유출된다.

테스트 커버리지는 시스템의 명세와 소스코드를 분모로 두고 테스트가 실행된 영역을 분자로 계산하여, **테스트 활동의 충분성을 객관적·정량적 수치로 가시화**한다. 이를 통해 테스트 공백을 방지하고 배포 안정성을 보장하는 Quality Gate 통과 기준으로 활용된다.

### 기능 커버리지 vs 구조적 코드 커버리지 비교

| 구분 | 기능 커버리지 (Functional Coverage) | 구조적 코드 커버리지 (Code Coverage) |
|---|---|---|
| **측정 기준** | 요구사항 명세서, 유스케이스, 화면 정의서 | 소스코드 텍스트, AST, 바이트코드 구조 |
| **테스트 관점** | 블랙박스 테스팅 (명세 기반) | 화이트박스 테스팅 (구현 기반) |
| **측정 대상** | 요구사항 항목, 사용자 시나리오 흐름 | 구문(Statement), 분기(Branch), 조건, MC/DC |
| **누락 탐지력** | 구현 누락(Omission 결함) 탐지 가능 | **요구사항이 미구현된 코드는 계측 불가** |
| **핵심 도구** | Jira, ALM, 요구사항 추적표(RTM) | JaCoCo, Cobertura, Coverage.py, SonarQube |

## 2. 아키텍처 및 핵심 메커니즘

### 다차원 테스트 커버리지 모델

테스트 커버리지는 소스코드 한 영역에 국한되지 않고 시스템 전체를 다차원으로 포괄해야 한다.

```text
+-------------------------------------------------------------------------+
|                  다차원 테스트 커버리지(Test Coverage) 모델             |
+-------------------------------------------------------------------------+
|                                                                         |
|      [ 요구사항 / 기능 관점 ]             [ 아키텍처 / 인터페이스 관점 ] |
|      - 요구사항 추적성(RTM) 100%          - REST API 엔드포인트 호출률   |
|      - 유스케이스 시나리오 실행률         - 메시지 큐 이벤트 커버리지    |
|                     │                                   │               |
|                     └─────────────────┬─────────────────┘               |
|                                       │                                 |
|                                       v                                 |
|                     [ 종합 테스트 완료 판정 게이트 ]                    |
|                        (Release Exit Criteria)                          |
|                                       ▲                                 |
|                     ┌─────────────────┴─────────────────┐               |
|                     │                                   │               |
|      [ 소스코드 / 구조 관점 ]             [ 운영 / 비기능 관점 ]          |
|      - 구문(Line) / 분기(Branch)          - OS / 브라우저 호환 매트릭스  |
|      - 고안전 도메인 MC/DC                - 부하 및 장애 복구 시나리오   |
|                                                                         |
+-------------------------------------------------------------------------+
```

### 구조적 코드 커버리지 4대 단계 상세

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 구문 커버리지 (Statement, C0)</strong></span>
      <span class="itpe-badge">기본 수준</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>전체 실행 가능한 소스코드 라인 중 1회 이상 실행된 라인의 비율</li>
        <li>if 조건문의 false 분기나 예외 처리 블록 누락 가능성 존재</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 분기 커버리지 (Branch, C1)</strong></span>
      <span class="itpe-badge">실무 표준</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>전체 조건문의 참(True)과 거짓(False) 결과 분기가 1회 이상 실행된 비율</li>
        <li>결정 커버리지(Decision Coverage)와 동일하며 일반 엔터프라이즈의 표준 기준</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 조건 커버리지 (Condition, C2)</strong></span>
      <span class="itpe-badge">개별 조건</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>복합 조건문 내부의 개별 개별 조건식(Sub-condition)이 참/거짓을 만족한 비율</li>
        <li>전체 조건문의 결과는 참/거짓을 모두 만족하지 못할 수 있는 한계 보유</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ MC/DC (수정 조건/결정 커버리지)</strong></span>
      <span class="itpe-badge">안전 필수</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>각 개별 조건식이 다른 조건식과 무관하게 전체 결정문의 결과에 독립적 영향 입증</li>
        <li>항공(DO-178C), 자동차(ISO 26262 ASIL-D) 고안전 제어 소프트웨어 필수 적용</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 단위 테스트 코드 커버리지가 85%를 달성했으나 오픈 첫날 미구현 요구사항 발생 | 소스코드 계측과 별개로 요구사항 추적표(RTM) 기반 기능 커버리지 100% 매핑을 인수 조건으로 강제 | 요구사항 누락(Omission 결함) 및 미개발 기능 조기 탐지 |
| 마감 일정 압박으로 커버리지 100% 달성에 집착하다가 단순 getter/setter 테스트만 양산 | 리스크 기반 테스팅(RBT)을 연계하여 결제·인증 핵심 모듈은 분기 90%, 단순 모듈은 50%로 차등화 | 테스트 자원 낭비 방지 및 고위험 결함 집중 방어 |
| 테스트 커버리지 수치만 높고 실제 비즈니스 예외 상황에 대한 어서션(Assertion) 부재 | SonarQube 커버리지 검증과 함께 돌연변이 테스트(Mutation Testing) 점수 연동 검증 | 무의미한 테스트 코드 제거 및 실질적 결함 검출력 확보 |

## 4. 기술사 답안 차별화 포인트

### 100% 코드 커버리지의 함정과 실질적 품질 지표

답안 서술 시 "코드 커버리지 100% = 결함 0%"라는 환상을 비판적으로 지적해야 한다. 코드가 아무리 100% 실행되었더라도 요구사항 자체가 누락된 결함은 코드 계측 도구로 감지할 수 없으며, Assertion이 없는 엉터리 테스트도 커버리지는 100%로 집계된다. 따라서 **"기능 커버리지(RTM) 100% + 리스크 기반 코드 커버리지(차등화) + 돌연변이 테스트 점수(Mutation Score)"를 결합한 3차원 품질 보증 체계**를 기술사적 시각으로 제시한다.

### CI/CD Quality Gate와의 완전 자동화 연계

현대 DevSecOps 파이프라인에서 테스트 커버리지는 단순한 사후 보고서가 아니다. GitHub Actions, GitLab CI 등에서 SonarQube의 Quality Gate 기준(신규 코드 기준 분기 커버리지 80% 이상 미달 시 빌드 차단)을 자동화하여, **커버리지 기준을 통과하지 못한 코드는 결코 메인 브랜치에 머지되거나 운영 배포되지 못하도록 강제하는 아키텍처**를 3단락 또는 전문가 제언으로 제시한다.

## 5. 참고 및 연계 학습

- [요구사항 추적표(RTM)](./102_requirement_traceability_matrix.md)
- [화이트박스 테스트 기법](./013_white_box_test.md)
- [돌연변이 테스팅(Mutation Test)](./084_mutation_test.md)
- [CI/CD 지속적 통합 및 배포](./095_ci_cd.md)
