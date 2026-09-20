---
title: "데이터 품질관리"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 관리에서 데이터 거버넌스와 품질로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 거버넌스·품질</span>
  <strong>데이터 품질관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 데이터가 비즈니스 목적에 부합하도록 정책·조직·프로세스·기술 도구를 결합하여 데이터 생명주기 전반의 품질을 계획·진단·개선·통제하는 지속적 프레임워크
- 프레임워크: 조직(Owner/Steward), 프로세스(예방/진단/개선), 정책·표준(규칙/도메인), 도구(프로파일링/모니터링)
- 6대 차원: 정확성, 완전성, 일관성, 유효성, 적시성, 유일성

<div class="itpe-flow-map" role="img" aria-label="데이터 품질관리 프레임워크 순환 체계">
  <div class="itpe-flow-node"><strong>품질 정책 및 기준 수립</strong><small>Critical Data Element(CDE) · 품질 규칙 정의</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>품질 진단 및 프로파일링</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>값 진단</strong><span>Null · 도메인 범위 · 패턴 · 중복 검증</span></div>
      <div class="itpe-flow-branch"><strong>구조 진단</strong><span>참조 무결성 · 카디널리티 · 식별자 관계</span></div>
      <div class="itpe-flow-branch"><strong>업무규칙</strong><span>교차 테이블 정합성 · 프로세스 제약 준수</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>품질 개선 및 원천 통제</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>사후 정제</strong><span>Cleansing · 마스터 동기화</span></div>
      <div class="itpe-flow-branch"><strong>원천 예방</strong><span>Data Contract · 입력 유효성 검증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>지속적 모니터링 & Feedback</strong></div>
</div>

## 예상문제

> 전사 데이터 자산의 신뢰성 확보 및 AI 모델 왜곡 방지를 위한 데이터 품질관리(DQM) 프레임워크 구성요소(조직, 프로세스, 표준, 도구)와 데이터 품질 진단 6대 차원을 제시하고, 사후 정제 한계를 극복하기 위한 원천 예방 통제 전략을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **데이터 품질관리 프레임워크(DQM Framework)** | K-DATA DQC(M/V) 기반 조직, 프로세스, 표준, 기술 도구 4대 영역 통합 아키텍처 | Ⅲ 구조·체계 |
| **데이터 품질 진단 6대 차원** | 정확성, 완전성, 일관성, 유효성, 적시성, 유일성 기반 품질 측정 지표 | Ⅳ 절차·지표 |

## Ⅰ. 데이터 오류 전파를 차단하는 방어선, 데이터 품질관리(DQM)의 개요

> **한줄 요약:** DQM은 비즈니스 적합성(Fitness for Use)을 충족하기 위해 전 생명주기에서 품질을 계획·진단·개선·통제하는 공학적 체계임.

- 정의: 데이터의 정확성, 완전성, 최신성을 유지하여 사용자가 요구하는 품질 수준을 달성하도록 정책, 프로세스, 조직, 도구를 체계화한 활동
- 배경: Garbage In, Garbage Out(GIGO) 원리에 따라 원천 데이터 오류가 ERP, DW, AI 모델로 전파되어 비즈니스 의사결정 파행 및 금융·보안 사고 유발
- 목표: 사후 땜질식 데이터 정제(Cleansing) 관행을 탈피하여, 데이터 생성 및 유입 단계에서 오류를 원천 차단하는 예방적 품질 통제 체계 정착

## Ⅱ. 데이터 품질관리의 핵심 원칙 및 특징

> **한줄 요약:** 일회성 정제 사업이 아닌 지속적 폐루프(Closed Loop) 관리와 업무 영향도 기반 예방 중심 통제를 지향함.

| 특징 | 세부 원리 | 실무적 기여 |
|---|---|---|
| **업무 목적성(Fitness for Use)** | 데이터의 절대적 무결성보다 업무 프로세스가 요구하는 기준 충족 우선 | 비즈니스 중요도(CDE) 기반 품질 예산 집중 |
| **전 생명주기 관리** | 생성, 수집, 변환, 저장, 연계, 활용, 폐기 전 단계 통제 | 데이터 레이크 및 DW 적재 전 단계에서 오염 차단 |
| **원천 예방 중심(Prevention)** | 시스템 인터페이스 및 UI 입력단 제약, Data Contract 적용 | 사후 정제 대비 오류 수정 비용 대폭 절감 |
| **측정 및 지속 개선(PDCA)** | 산식화된 DQI(Data Quality Index) 및 임계치(Threshold) 운영 | 측정 $\rightarrow$ 원인분석 $\rightarrow$ 개선 $\rightarrow$ 모니터링 폐루프 완결 |

## Ⅲ. 데이터 품질관리 프레임워크(DQM Framework) 구성요소

> **한줄 요약:** 조직, 프로세스, 정책·표준, 지원도구 4대 축이 유기적으로 결합되어 전사 품질을 담보함.

<div class="itpe-pipeline" role="img" aria-label="데이터 품질관리 프레임워크 4대 구성요소">
  <div class="itpe-pipeline-node"><strong>조직·거버넌스</strong><small>Owner · Steward</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>정책·표준</strong><small>표준사전 · 품질규칙</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>프로세스</strong><small>측정 · 정제 · 개선</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>지원도구</strong><small>Profiling · 모니터링</small></div>
</div>

| 구성요소 | 핵심 역할 및 책임 | 주요 산출물 및 통제 도구 |
|---|---|---|
| **조직·거버넌스** | 전사 품질 의사결정 협의체, 데이터 도메인별 Owner 및 Steward R&R 지정 | 품질 거버넌스 규정, RACI 매트릭스 |
| **정책·표준** | 전사 공통 단어·용어·도메인·코드 표준 수립, 업무규칙(BR) 정의 | 데이터 표준사전, 테이블 정의서, 품질 규칙집 |
| **프로세스** | 품질 목표 수립 $\rightarrow$ 프로파일링 $\rightarrow$ 원인분석 $\rightarrow$ 정제 $\rightarrow$ 변경통제 | 품질 진단보고서, 오류 개선 계획서, 이슈 대장 |
| **지원도구** | 자동화된 프로파일링 엔진, 실시간 이상치 탐지, 품질 대시보드 | DQM 솔루션, 메타데이터 관리 시스템 |

## Ⅳ. 데이터 품질 진단 6대 차원 및 측정 지표

> **한줄 요약:** 정확성, 완전성, 일관성, 유효성, 적시성, 유일성 6대 지표로 데이터의 건강성을 객관적 수치화함.

| 품질 차원 | 개념 및 판정 질문 | 구체적 측정 산식 및 검증 관점 |
|---|---|---|
| **정확성(Accuracy)** | 데이터가 실제 현실 세계의 참값(Real World)과 일치하는가? | 기준 원천(Golden Record) 대조 오류율 |
| **완전성(Completeness)** | 필수적으로 입력되어야 할 속성이나 레코드가 누락되지 않았는가? | 필수 속성 Not-Null 제약 위반률, 레코드 누락률 |
| **일관성(Consistency)** | 시스템 간, 또는 연계 테이블 간 상호 모순 없이 정합한가? | 원천-타깃 시스템 간 데이터 불일치율, 참조 무결성 오류율 |
| **유효성(Validity)** | 정의된 도메인 범위, 데이터 타입, 포맷 규칙을 준수하는가? | 정규식 패턴 위반률, 유효 코드값 범위 초과율 |
| **적시성(Timeliness)** | 비즈니스 요구 시점까지 최신 데이터가 반영되어 있는가? | 배치 처리 지연 시간, 데이터 갱신 SLA 준수율 |
| **유일성(Uniqueness)** | 동일한 비즈니스 엔티티가 중복 레코드로 존재하지 않는가? | 주 식별자(PK) 중복률, 마스터 데이터 중복 엔티티율 |

## Ⅴ. 데이터 거버넌스 vs 데이터 표준화 vs DQM 비교

> **한줄 요약:** 거버넌스는 권한과 정책, 표준화는 규격과 기준, DQM은 규격 준수와 오류 개선의 실행 통제임.

| 구분 | 데이터 거버넌스 | 데이터 표준화 | 데이터 품질관리(DQM) |
|---|---|---|---|
| **목적** | 데이터 관리 원칙 확립 및 전사적 의사결정 체계화 | 데이터 명칭·형식의 통일성 확보 | 데이터 오류 제거 및 비즈니스 신뢰도 보증 |
| **핵심 활동** | 데이터 정책 수립, Data Owner 지정, 위원회 운영 | 표준 단어·용어·도메인·코드 정의 및 등록 | 프로파일링, 품질 진단, 데이터 정제, 모니터링 |
| **산출물** | 거버넌스 프레임워크, 정책서, R&R 정의서 | 데이터 표준사전, 메타데이터 정의서 | 품질 진단 지표, 오류 목록, 정제 가이드 |
| **상호 관계** | 품질관리와 표준화의 상위 지휘·감독 통제 | DQM의 유효성 검증을 위한 판단 기준선 | 거버넌스와 표준이 현장에서 지켜지는지 검증·환류 |

## Ⅵ. 실무 고려사항 및 장애 대책

> **한줄 요약:** 단순 스크립트 정제 한계를 Data Contract와 CI/CD 기반 입력 통제로 원천 봉쇄함.

- 적용 상황: 차세대 코어뱅킹 데이터 마이그레이션 및 실시간 FDS 파이프라인 품질 관리

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **정제 후 동일 오류 반복 발생** | 데이터베이스 값만 수정하고 화면 UI 및 배치 프로그램 버그 방치 | 원인 분석 기법(5-Why) 적용, 입력단 정규식 검증 로직 강제 | 오류 재발 방지 및 원천 품질 확보 |
| **파이프라인 배포 시 스키마 파손** | 상류(Upstream) 시스템의 일방적 스키마 변경 | Data Contract 체계 도입, CI/CD에 스키마 호환성 테스트 통합 | 다운스트림 분석 파이프라인 무중단 운영 |
| **전수 검사 불가능에 따른 비용 폭증** | 테라바이트급 비정형 데이터 무차별 검사 | 업무 영향도가 높은 핵심 데이터(CDE) 중심 샘플링 및 계층화 검사 | 검사 비용 최적화 및 고위험 영역 집중 통제 |

## Ⅶ. 결론 및 기술사적 제언

> **한줄 요약:** 데이터 품질은 일회성 프로젝트가 아니라 Data Product의 신뢰도를 보증하는 운영 SLA로 내재화되어야 함.

- [핵심 통찰]: 데이터 품질을 IT 부서의 전유물로 보거나 일회성 데이터 정제 사업으로 끝내는 조직은 필연적으로 수개월 내 품질 퇴행을 겪음. 데이터 품질은 데이터 생산 조직(Business Unit)이 책임을 지는 도메인 중심 책임주의(Domain Ownership)가 정착되어야 함.
- 나라면: 데이터 메타데이터 카탈로그와 Data Observability 도구를 연계하여, 데이터 파이프라인 상에서 정확성·완전성·적시성 지표를 실시간 측정하는 Data SLO를 수립하고, SLO 위반 시 배포 파이프라인을 자동 중단(Circuit Breaker)시키는 무결성 게이트를 구축하겠음.

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 데이터 품질관리(DQM)는 데이터의 비즈니스 적합성을 보장하기 위해 정책·조직·프로세스·도구를 기반으로 데이터 전 생명주기에서 품질을 측정·진단·개선·통제하는 공학적 체계임.

### 2. 핵심 메커니즘 / 체계
```text
[조직] Owner/Steward ── [표준] 표준사전/업무규칙
           │                        │
           ▼                        ▼
[프로세스] 진단(Profiling) ──▶ 개선(Cleansing) ──▶ 예방(Data Contract)
           ▲                        ▲
           └──────── [도구] DQM 모니터링 ─────┘
```
- 정확성·완전성·일관성·유효성·적시성·유일성 6대 차원으로 수치화함.

### 3. 차별화 제언
- 사후 정제에서 탈피하여 CDE(Critical Data Element) 기반 Data Contract 및 배포 파이프라인 자동 검증으로 원천 예방 통제를 실현해야 함.

## 출제 이력과 검증 출처

- 출제 이력: 제131회·129회·123회 KPC 모의고사, 제87·83회 기출
- 검증 출처: 한국데이터산업진흥원(K-DATA) DQC-M/V 가이드라인, DAMA DMBOK 2.0

## 학습 체크

- [ ] 데이터 품질관리 프레임워크 4대 구성요소(조직, 프로세스, 표준, 도구)를 설명할 수 있는가?
- [ ] 데이터 품질 진단 6대 차원과 세부 측정 지표를 제시할 수 있는가?
- [ ] 사후 정제의 한계와 Data Contract 기반 원천 예방 전략을 논할 수 있는가?

## 연결 토픽

- 이전 토픽: [데이터 가치평가·데이터 자산화](./002_data_valuation.md)
- 연관 토픽: [데이터 거버넌스](./006_data_governance.md), [데이터 표준화](./008_data_standardization.md), [데이터 프로파일링](./105_data_profiling.md)
- 다음 토픽: [다중공선성(등분산성 포함)](./004_multicollinearity.md)
