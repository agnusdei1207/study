---
title: "CMMI(Capability Maturity Model Integration)"
category: "02-software-engineering"
tags:
  - "CMMI"
  - "프로세스성숙도"
  - "통계적공정관리"
  - "단계적표현"
  - "연속적표현"
  - "SPICE"
  - "테일러링"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 소프트웨어 품질 보증과 프로세스 평가를 거쳐 CMMI로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>소프트웨어 품질 보증·프로세스 평가</span>
  <strong>CMMI(Capability Maturity Model Integration)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 소프트웨어 개발 조직의 품질과 납기 통제를 특정 개인의 영웅적 역량에 의존하지 않고, 조직 차원의 표준 프로세스와 정량적 데이터 기반의 통계적 공정 관리(SPC)를 통해 예측 가능하고 재현 가능한 고품질 소프트웨어를 반복 생산하도록 지원하는 SEI/ISACA 프로세스 통합 성숙도 모델
- 메커니즘: 프로세스 혼돈(Level 1) $\rightarrow$ 프로젝트 차원 관리(Level 2) $\rightarrow$ 전사 표준화 및 테일러링(Level 3) $\rightarrow$ 통계적 정량 관리(Level 4) $\rightarrow$ 지속적 결함 예방 및 공정 최적화(Level 5)
- 산출물: 조직 표준 프로세스 자산(OSSP) · 테일러링 계획서 · 통계적 공정 관리도(Control Chart) · CMMI 심사 결과 보고서

<div class="itpe-flow-map" role="img" aria-label="CMMI 성숙도 레벨 5단계 발전 및 공정 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1~2단계: 프로젝트 차원 관리 (Managed)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>통제</strong><span>개별 프로젝트 단위로 요구사항, 일정, 형상 관리 베이스라인 수립</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 조직 표준 프로세스 확립 (Defined)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>표준화</strong><span>전사 표준 프로세스 자산화(OSSP) 및 프로젝트별 테일러링 수행</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 통계적 정량 관리 (Quantitatively Managed)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>계측</strong><span>관리도(Control Chart) 기반 결함 밀도 및 생산성의 통계적 예측 제어</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>5단계: 지속적 최적화 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>공정 변동이 통계 한계선 내에서 통제되며 근본 원인 분석(CAR) 기반 결함 예방이 작동하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Level 5 Optimizing 달성)</strong>
      <span>자가 혁신 조직 안착 $\rightarrow$ 비즈니스 품질 예측 신뢰성 99% 달성</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (이상 변동 탐지)</strong>
      <span>Level 4 관리 강화 $\rightarrow$ 통계 지표 이상치(Outlier) 근본 원인 재분석</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **단계적 표현(Staged Representation)**: 조직 전체의 프로세스 성숙도를 1단계부터 5단계까지 순차적으로 평가하여 조직 단위 성숙도 레벨(Maturity Level)을 부여하는 방식
- **연속적 표현(Continuous Representation)**: 조직이 필요로 하는 개별 프로세스 영역(PA)을 선별하여 능력 레벨(Capability Level 0~3)을 집중 개선하는 맞춤형 방식
- **통계적 공정 관리(SPC, Statistical Process Control)**: 공정의 변동성을 관리 상한선(UCL)과 관리 하한선(LCL)으로 통제하여 결함 발생률과 개발 생산성을 수학적으로 예측하는 기법
- **테일러링(Tailoring)**: 조직 표준 프로세스(OSSP)를 개별 프로젝트의 특성, 규모, 위험도, 계약 조건에 맞추어 합리적으로 가감 조정하는 표준 활동
</details>

## 1. 개요 및 필요성

### 개인 의존적 개발의 한계와 프로세스 성숙도

소프트웨어 개발 프로젝트가 소수의 천재 개발자(Hero)의 야근과 개인기에만 의존하면, 해당 인력이 이탈하는 순간 프로젝트는 파탄에 직면한다. 제품의 품질이 일정하지 않고 일정과 예산 예측이 불가능한 현상을 "소프트웨어 위기"라 부른다.

CMMI는 **"우수한 프로세스에서 우수한 품질의 제품이 나온다"**는 철학을 바탕으로, 조직의 개발 역량을 체계적인 5단계 성숙도 레벨로 정형화하여 **예측 가능하고 재현 가능한 엔지니어링 프로세스**를 정립한다.

### CMMI vs SPICE vs ISO 9001 비교

| 구분 | CMMI (v2.0 / v3.0) | SPICE (ISO/IEC 33000 / 15504) | ISO 9001 |
|---|---|---|---|
| **주관 기관** | 미국 카네기멜론 SEI / ISACA | ISO / IEC 국제표준화기구 | ISO 국제표준화기구 |
| **적용 영역** | **소프트웨어, 시스템 엔지니어링, R&D** | 소프트웨어 프로세스 평가 및 개선 | 제조 및 전 산업 일반 품질경영시스템 |
| **평가 모델** | **단계적(1~5) 및 연속적(0~3) 병행** | 연속적 모델 중심 (능력 0~5단계) | 요구사항 충족 여부 단일 합격/불합격 |
| **핵심 지향** | **조직의 프로세스 개선 및 비즈니스 성과 연계** | 국제 표준 규격 준수 평가 | 고객 요구 충족 및 품질 보증 체계 |

## 2. 아키텍처 및 핵심 메커니즘

### CMMI 5대 성숙도 레벨 (Staged Model)

```text
+-------------------------------------------------------------------------+
|                  CMMI 5대 성숙도 레벨 (Maturity Levels)                 |
+-------------------------------------------------------------------------+
|                                                                         |
|  [ Level 5 : Optimizing (최적화) ]                                      |
|    - 지속적 공정 개선, 결함 근본 원인 분석(CAR), 혁신 기술 도입         |
|                                       ▲                                 |
|  [ Level 4 : Quantitatively Managed (정량적 관리) ]                     |
|    - 프로세스 성능 기준선(PPB), 통계적 공정 관리(SPC), 품질 예측 모델   |
|                                       ▲                                 |
|  [ Level 3 : Defined (정의됨) ]                                         |
|    - 전사 표준 프로세스 자산(OSSP) 확립, 프로젝트별 테일러링 수행       |
|                                       ▲                                 |
|  [ Level 2 : Managed (관리됨) ]                                         |
|    - 개별 프로젝트 단위의 요구사항 관리, WBS 일정, 형상 관리 통제       |
|                                       ▲                                 |
|  [ Level 1 : Initial (초기) ]                                           |
|    - 프로세스 부재, 혼돈, 개인의 영웅적 역량에 의존 (재현성 결여)       |
+-------------------------------------------------------------------------+
```

### 5대 성숙도 레벨 핵심 활동

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>Level 2: Managed</strong></span>
      <span class="itpe-badge">프로젝트 통제</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>요구사항 관리, 프로젝트 계획, 형상 관리, 측정 및 분석</li>
        <li>프로젝트가 약속된 일정과 비용 내에서 관리됨</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>Level 3: Defined</strong></span>
      <span class="itpe-badge">조직 표준화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>조직 프로세스 정의(OPD), 조직 교육, 통합 프로젝트 관리</li>
        <li>표준 프로세스를 프로젝트 환경에 맞게 테일러링하여 적용</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>Level 4: Quantitatively Managed</strong></span>
      <span class="itpe-badge">통계적 제어</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>정량적 프로젝트 관리(QPM), 조직 프로세스 성능(OPP)</li>
        <li>결함 밀도와 생산성을 통계 모델(관리도)로 정밀 제어</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>Level 5: Optimizing</strong></span>
      <span class="itpe-badge">자가 혁신</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>인과 분석 및 해결(CAR), 조직 성과 관리(OPM)</li>
        <li>프로세스 결함의 근본 원인을 선제 제거하고 신기술 도입 혁신</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| CMMI 심사 통과만을 목적으로 실제 개발 업무와 동떨어진 가짜 서류를 양산하여 프로세스 사장 | Jira, GitLab, SonarQube 등 실무 도구와 파이프라인을 연동하여 개발 중 메트릭 자동 수집 | 페이퍼워크 80% 제거 및 실질적 프로세스 내재화 |
| 전사 표준 프로세스를 스타트업이나 소규모 프로젝트에 획일 강요하여 릴리스 지연 발생 | 프로젝트 규모, 도메인 위험도에 따른 표준 테일러링(Tailoring) 가이드라인 수립 | 개발 민첩성 유지 및 불필요한 공수 낭비 차단 |
| 정량적 데이터 측정 체계 부재로 Level 4 통계적 공정 관리(SPC) 구축 난항 | CI/CD 파이프라인 기반 빌드 결함률, 테스트 커버리지, 배포 성공률 실시간 통계 관리도화 | 통계적 공정 관리 요건 100% 충족 및 예측력 확보 |

## 4. 기술사 답안 차별화 포인트

### CMMI V2.0/V3.0의 애자일 및 데브옵스(DevOps) 공식 통합

과거 CMMI는 무거운 폭포수 전유물로 비판받았으나, **CMMI V2.0부터는 스크럼(Scrum), 칸반(Kanban), DevOps(DORA 메트릭)를 공식 수용**하였다. 배포 빈도(Deployment Frequency), 변경 실패율(Change Failure Rate), 복구 시간(MTTR)을 Level 4의 정량적 프로세스 성능 지표(PPB)로 설정하는 현대적 애자일-CMMI 융합 모델을 제시한다.

### "Process as Code": 프로세스의 코드화 거버넌스

수백 페이지의 두꺼운 절차서 대신, **GitLab CI/CD 파이프라인 스크립트와 Quality Gate 설정 자체를 프로세스(Process as Code)**로 구현해야 한다. 개발자가 코드를 푸시하면 단위 테스트 커버리지, 정적 보안 점검, 동료 코드 리뷰 승인이 자동으로 강제되는 시스템적 프로세스 보증 체계를 결론으로 강조한다.

## 5. 참고 및 연계 학습

- [품질 보증(Quality Assurance)](./060_quality_assurance.md)
- [SW 품질비용(Cost of Quality)](./150_software_quality_cost.md)
- [테일러링(Methodology Tailoring)](./039_methodology_tailoring.md)
- [소프트웨어 신뢰도 성장 모델(SRGM)](./136_srgm.md)
