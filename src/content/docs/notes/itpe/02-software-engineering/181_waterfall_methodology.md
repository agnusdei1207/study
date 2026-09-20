---
title: "폭포수 개발 방법론(Waterfall)"
category: "02-software-engineering"
tags:
  - "폭포수방법론"
  - "Waterfall"
  - "선형순차모델"
  - "베이스라인"
  - "V모델"
  - "보엠의곡선"
  - "워터스크럼폴"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 개발 방법론과 공학 프로세스를 거쳐 폭포수 개발 방법론으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>개발 방법론·공학 프로세스</span>
  <strong>폭포수 개발 방법론(Waterfall)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 소프트웨어 생명주기(SDLC)를 요구분석, 설계, 구현, 시험, 유지보수의 순차적 단계로 명확히 구분하고, 각 단계의 산출물을 공식 검토하여 베이스라인(Baseline)으로 동결한 후 다음 단계로 진행하는 전통적인 계획 주도형 선형 순차 소프트웨어 공학 방법론
- 메커니즘: 요구사항 분석 및 SRS 확정 $\rightarrow$ 아키텍처 및 상세설계(SDD) $\rightarrow$ 소스코드 구현 및 단위 검증 $\rightarrow$ 통합 및 시스템 시험 $\rightarrow$ 고객 검수 및 품질 게이트 통과
- 산출물: 요구사항 명세서(SRS) · 시스템 설계서(SDD) · 소스코드 및 형상물 · 시험 결과 보고서 · 운영 이관 계획서

<div class="itpe-flow-map" role="img" aria-label="폭포수 개발 방법론 단계별 생명주기 및 품질 게이트 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 요구사항 분석 및 정의 (Analysis)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>동결</strong><span>요구사항 명세서(SRS) 작성 및 고객 승인을 통한 기능 베이스라인 확정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 시스템 아키텍처 및 상세 설계 (Design)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>명세</strong><span>시스템 설계서(SDD), 데이터베이스 ERD 및 인터페이스 규격서 확정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 코딩 및 단위 구현 (Implementation)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>구현</strong><span>프로그래밍 언어 기반 모듈 코딩, 정적 코드 분석 및 단위 테스트 수행</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 통합 시험 및 최종 인수 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>요구사항 추적표(RTM)의 모든 기능이 100% 검증되고 잔여 결함이 허용 기준 이내인가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (납품 및 검수 승인)</strong>
      <span>운영 환경 배포 $\rightarrow$ 고객 최종 검수 서명 및 유지보수 단계 공식 이관</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (인수 거부 / 결함 다수)</strong>
      <span>배포 보류 $\rightarrow$ 변경 통제 위원회(CCB) 심의를 통한 설계/구현 재작업</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **선형 순차 모델(Linear Sequential Model)**: 이전 단계의 산출물이 완전히 승인되어야만 다음 단계가 시작되는 비중첩 직렬 진행 아키텍처 모델
- **베이스라인(Baseline)**: 공식적으로 검토·합의되어 향후 개발의 기준점이 되는 특정 시점의 산출물 집합으로, 변경 통제 위원회(CCB) 승인 없이 임의 수정 불가
- **보엠의 변경 비용 곡선(Boehm's Curve)**: 요구분석 단계에서 결함을 수정하는 비용을 1로 볼 때, 테스트 및 운영 단계에서 수정하는 비용은 50~100배 지수 폭증한다는 법칙
- **워터-스크럼-폴(Water-Scrum-Fall)**: 상위 계획/예산 및 최종 검수/배포는 폭포수로 통제하되, 중간 구현 및 테스트는 애자일 스프린트로 반복하는 현대적 절충 모델
</details>

## 1. 개요 및 필요성

### 계획 주도 개발의 가치와 태생적 한계

국방 무기 체계, 원자력 제어, 대형 공공 인프라, 차세대 금융 계정계처럼 실패가 인명 피해나 천문학적 금융 손실로 직결되는 도메인은 요구사항의 추적성과 문서화가 엄격히 요구된다. 폭포수 모델은 프로젝트 전 과정을 정형화된 단계로 통제하여 높은 예측 가능성을 제공한다.

그러나 프로젝트 극후반부에 이르러서야 실제 동작하는 소프트웨어가 완성되므로, 비즈니스 환경이 급변하거나 고객이 실물을 본 후 요구사항을 뒤엎을 경우 천문학적인 재작업 비용이 발생하는 "빅뱅 리스크"를 안고 있다.

### 폭포수 vs 나선형 vs 애자일 모델 비교

| 구분 | 폭포수 방법론 (Waterfall) | 나선형 모델 (Spiral) | 애자일 방법론 (Agile) |
|---|---|---|---|
| **개발 철학** | **계획 주도 (선형 순차적)** | **위험 분석 주도 (점진적 반복)** | **가치 주도 (유연한 반복과 적응)** |
| **요구사항 고정** | **초기 분석 단계 동결 원칙** | 반복 주기(Spiral)마다 재평가 | 상시 변경 수용 (스프린트 백로그 관리) |
| **동작 SW 출시** | **프로젝트 극후반부 (빅뱅 릴리스)** | 각 주기별 위험 제거 프로토타입 | **1~4주 단위 동작하는 기능 지속 배포** |
| **고객 참여** | 프로젝트 착수 및 최종 검수 시점 집중 | 각 사이클 검토 시점 참여 | **전 개발 스프린트에 걸쳐 상시 참여** |
| **적합한 분야** | **요구사항이 명확한 공공/국방/금융 코어** | 고위험·대규모 R&D 연구 개발 | 시장 변화가 빠른 모바일/웹/SaaS |

## 2. 아키텍처 및 핵심 메커니즘

### 폭포수 방법론 5단계 생명주기 및 베이스라인 체계

```text
+-------------------------------------------------------------------------+
|                  폭포수 방법론 5단계 생명주기 및 베이스라인 체계        |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ 1. 요구분석 (Analysis) ]                                              |
|    - 기능/비기능 요구 도출 ──> [ 기능 베이스라인: SRS ]                 |
|                                       │                                 |
|                                       v                                 |
|  [ 2. 아키텍처 및 설계 (Design) ]                                       |
|    - HLD / LLD, ERD, 인터페이스 ──> [ 분배 베이스라인: SDD ]            |
|                                       │                                 |
|                                       v                                 |
|  [ 3. 코딩 및 구현 (Implementation) ]                                   |
|    - 컴포넌트 단위 구현 ──> [ 개발 베이스라인: 소스코드 ]               |
|                                       │                                 |
|                                       v                                 |
|  [ 4. 통합 및 시스템 시험 (Testing) ]                                   |
|    - 단위 ──> 통합 ──> 시스템 시험 ──> [ 제품 베이스라인: 검수보고서 ]  |
|                                       │                                 |
|                                       v                                 |
|  [ 5. 운영 및 유지보수 (Maintenance) ]                                  |
|    - 결함 수정, 적응/완전 유지보수 ──> [ 운영 베이스라인 ]              |
+-------------------------------------------------------------------------+
```

### 단계별 주요 태스크 및 핵심 산출물

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 요구분석 단계</strong></span>
      <span class="itpe-badge">요구사항 명세</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>이해관계자 인터뷰, 기능 분할, 요구사항 추적 매트릭스(RTM) 구성</li>
        <li>요구사항 명세서(SRS), 사용자 요구사항 정의서</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 설계 단계</strong></span>
      <span class="itpe-badge">구조 설계</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>기본설계(아키텍처, 네트워크, DB) 및 상세설계(클래스, API 규격)</li>
        <li>시스템 아키텍처 설계서(SAD), 데이터베이스 설계서(ERD)</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 구현 단계</strong></span>
      <span class="itpe-badge">소스 개발</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>시큐어 코딩 규칙 준수 프로그래밍 및 정적 코드 검사(SonarQube)</li>
        <li>소스코드, 단위 테스트 케이스 및 결과서</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 시험 단계</strong></span>
      <span class="itpe-badge">품질 검증</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>통합 테스트, 성능 부하 시험(BMT), 사용자 인수 시험(UAT)</li>
        <li>통합 테스트 결과서, 결함 조치 리포트, 인수 확인서</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 프로젝트 후반부에야 실물 동작을 확인한 발주처의 대규모 요구 변경으로 납기 파행 | 요구분석 단계에서 피그마(Figma) 와이어프레임 및 프로토타이핑(Prototyping) 병행 도입 | 요구사항 오해 100% 해소 및 후반부 변경 요청 60% 감소 |
| 코딩 완료 후 통합 시험 단계에서 인터페이스 불일치 및 잠재 결함이 대량 분출 | 단계별 Fagan 인스펙션(동료 검토) 의무화 및 CI 파이프라인 조기 연동 | 결함 유출 80% 사전 차단 및 재작업 공수 절감 |
| 형식적인 방대한 산출물 작성에 개발 공수의 40% 이상이 매몰되어 실무 생산성 저하 | 모델 기반 시스템 공학(MBSE) 도구 도입 및 경량화 문서 템플릿 표준화 | 서류 작업 공수 50% 절감 및 실무 코딩 집중 |

## 4. 기술사 답안 차별화 포인트

### 하이브리드 거버넌스: 워터-스크럼-폴(Water-Scrum-Fall)

실제 엔터프라이즈 환경에서는 순수 애자일만으로 사업 예산과 계약 일정을 관리하기 어렵다. 기술사 답안에서는 **워터-스크럼-폴(Water-Scrum-Fall)** 모델을 제시한다. 상위 RFP 조달, 요구분석, 전체 아키텍처 수립은 폭포수(Water)로 엄격히 관리하고, 세부 기능 개발과 단위 시험은 2주 단위의 스크럼(Scrum) 스프린트로 빠르게 반복하며, 최종 릴리스 및 감리 검수는 다시 폭포수(Fall) 베이스라인으로 완결 짓는 **현실적 하이브리드 거버넌스**를 답안의 차별화로 제시한다.

### 변경 통제 위원회(CCB)와 영향도 분석 자동화

폭포수 모델의 성패는 변경을 무조건 막는 것이 아니라, "변경을 어떻게 통제하는가"에 달려있다. 요구사항 변경 요청(CR) 접수 시 **형상 관리 도구(Jira/GitLab)와 요구추적표(RTM)를 연동하여 소스코드 및 테스트 케이스에 미치는 변경 영향도(Impact Analysis)**를 자동 산출하는 성숙한 CCB 체계를 결론으로 강조한다.

## 5. 참고 및 연계 학습

- [애자일 방법론(Agile)](./119_agile_methodology.md)
- [SW 개발 방법론 비교](./139_sw_development_methodologies.md)
- [요구공학(Requirements Engineering)](./040_requirements_engineering.md)
- [형상 관리(Configuration Management)](./011_configuration_management.md)
