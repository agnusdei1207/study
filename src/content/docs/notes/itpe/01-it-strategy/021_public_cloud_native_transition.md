---
title: "공공부문 클라우드 네이티브 전환"
author: "Antigravity"
date: "2026-09-20T21:00:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash (High)"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 디지털 혁신을 거쳐 공공부문 클라우드 네이티브 전환으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 디지털 혁신</span>
  <strong>공공부문 클라우드 네이티브 전환</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 공공 정보시스템을 단순 인프라 이전(Lift & Shift)에서 탈피하여 클라우드의 탄력성·회복성·자동화 능력을 활용하도록 애플리케이션, 데이터, 운영방식을 전면 현대화하는 전략
- 메커니즘: **4대 핵심 기술(MSA, Container, CI/CD, DevOps)** 및 **6R 프레임워크** 기반 진단 → 플랫폼 구축 → **Strangler Fig** 점진 전환
- 산출: 트래픽 폭증 시 오토스케일링(HPA), 대국민 24/365 무중단 배포(Blue/Green, Canary) 및 **CSAP** 보안인증 준수

<div class="itpe-flow-map" role="img" aria-label="공공부문 클라우드 네이티브 전환 및 4대 기술 체계">
  <div class="itpe-flow-node">
    <strong>공공 레거시 모놀리식 시스템 한계</strong>
    <small>특정 모듈 장애 시 전산망 전체 다운 · 트래픽 폭증 시 확장 불가</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>클라우드 네이티브 4대 핵심 기둥</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>구조</strong><span><span class="itpe-keyword"><strong>MSA(Microservices Architecture)</strong></span> · 장애 격리 및 독립 배포</span></div>
      <div class="itpe-flow-branch"><strong>가상화</strong><span><span class="itpe-keyword"><strong>Container(K8s)</strong></span> · 오토스케일링 및 자가 치유(Self-healing)</span></div>
      <div class="itpe-flow-branch"><strong>배포</strong><span><span class="itpe-keyword"><strong>CI/CD 자동화</strong></span> · 카나리/블루그린 무중단 배포</span></div>
      <div class="itpe-flow-branch"><strong>운영</strong><span><span class="itpe-keyword"><strong>DevOps/관측성</strong></span> · OpenTelemetry 분산 추적 · SRE 운영</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>고신뢰 대국민 행정 서비스 달성</strong>
    <small>24/365 무중단 서비스 · 변경 리드타임 단축 · 장애 전파 차단</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Cloud Native(클라우드 네이티브)**: 클라우드의 탄력성과 복원력을 극대화하여 신속한 변경과 안정성을 달성하는 현대화 접근법
- **Lift & Shift(Rehost)**: 기존 온프레미스 VM을 아키텍처나 코드 수정 없이 클라우드 IaaS로 그대로 단순 복사 이전하는 방식
- **MSA(Microservices Architecture)**: 거대 단일 시스템을 비즈니스 도메인 단위로 분할하여 독립적 배포와 확장을 지원하는 구조
- **Container**: 애플리케이션과 실행 라이브러리를 가볍게 패키징하여 환경 격리와 신속한 구동을 보장하는 경량 가상화 기술
- **Kubernetes(쿠버네티스/K8s)**: 컨테이너의 자동 배치, 수평 확장(HPA), 롤링 업데이트 및 헬스체크를 수행하는 표준 오케스트레이션 엔진
- **CI/CD**: 코드 커밋부터 빌드, 자동화 테스트, 프로덕션 배포까지의 전 과정을 자동화하는 파이프라인
- **6R**: Rehost, Replatform, Repurchase, Refactor, Retain, Retire로 구성된 클라우드 마이그레이션 6대 전략 프레임워크
- **Strangler Fig 패턴**: 기존 모놀리식 레거시 시스템을 일괄 교체하지 않고 점진적으로 마이크로서비스로 대체하는 전환 패턴
- **CSAP(Cloud Security Assurance Program)**: 공공기관에 공급되는 민간 클라우드의 보안 신뢰성을 KISA가 검증하는 인증 제도
- **SRE(Site Reliability Engineering)**: 소프트웨어 공학 기법을 인프라 운영에 적용하여 SLO 기반 가용성을 보증하는 운영 체계

</details>

## 예상문제

> 정부의 '공공부문 클라우드 네이티브 전환 로드맵'에 따른 클라우드 네이티브의 개념과 4대 핵심 기술 요소(MSA, Container, CI/CD, DevOps)를 설명하고, 단순 이전(Lift & Shift)과의 차이점 및 전환 시 직면하는 기술적·제도적 장애요인과 해결 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **클라우드 네이티브 4대 핵심 요소** | 마이크로서비스(MSA), 컨테이너(K8s), CI/CD 자동화, 데브옵스/관측성 | Ⅱ 절, Ⅲ 절 |
| **Lift & Shift vs 클라우드 네이티브** | 단순 VM 이전(Rehost)과 애플리케이션 전면 현대화(Refactor) 비교 | Ⅳ 절 |
| **6R 전환 전략 및 Strangler 패턴** | 6가지 이전 유형 및 점진적 마이그레이션을 위한 스트랭글러 아키텍처 | Ⅱ 절, Ⅵ 절 |
| **CSAP 및 공공 거버넌스** | 공공 클라우드 보안인증(CSAP) 및 기능 분할 발주 제도 대응 | Ⅲ 절, Ⅴ 절 |

## Ⅰ. 대국민 서비스 안정성과 민첩성을 확보하는 공공 클라우드 네이티브의 개요

> 공공 클라우드 네이티브 전환은 단순 IaaS 서버 이전을 넘어 **애플리케이션과 운영 체계의 전면 현대화**이며, 성패는 공공서비스의 **탄력적 가용성과 무중단 배포 역량**으로 판정함.

- 정의: 공공 정보시스템에 클라우드의 탄력성, 회복성, 자동화를 온전히 내재화하기 위해 **마이크로서비스(MSA)**, **컨테이너(Container)**, **CI/CD**, **데브옵스(DevOps)** 기반으로 전면 재설계·운영하는 현대화 전략
- 목적: 행정전산망 단일장애점(SPOF) 차단 및 24/365 대국민 무중단 서비스 확보

## Ⅱ. 공공 클라우드 네이티브 5단계 전환 방법론 및 추진 파이프라인

> 진단 및 6R 전략 수립에서 출발하여 랜딩존 구축, 스트랭글러 기반 점진 전환, SRE 기반 상시 운영으로 연결되어야 시스템 중단 없이 안착함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 클라우드 네이티브 5단계 전환 방법론">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 진단 및 6R 전략 수립 (Assessment & Strategy)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>정보자원 등급 진단 · BIA 분석 · 6R(Refactor, Replatform 등) 분류</span>
      <strong>산출</strong><span>클라우드 전환 타당성 분석서 · 이행 우선순위표</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 랜딩존 및 표준 플랫폼 구축 (Landing Zone & Platform)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>보안 망분리 · CSAP 인증 공공존 확보 · K8s 클러스터 · 표준 배포 파이프라인</span>
      <strong>산출</strong><span>클라우드 플랫폼 표준 명세서 · IAM 정책서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 점진적 애플리케이션 현대화 (Modernization & Strangler)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>도메인 주도 설계(DDD) 기반 MSA 분할 · Strangler Fig 적용 · DB 분리</span>
      <strong>산출</strong><span>MSA 아키텍처 설계서 · 마이크로서비스 API 명세서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 무중단 배포 및 전환 (Zero-Downtime Deployment)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>카나리(Canary)/블루그린 배포 · 트래픽 점진적 롤아웃 · 데이터 정합성 검증</span>
      <strong>산출</strong><span>전환 검수 보고서 · 롤백 시나리오</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 관측성 및 상시 운영 (Observability & SRE)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>OpenTelemetry 분산 추적 · SLO 기반 SRE 운영 · FinOps 비용 최적화</span>
      <strong>산출</strong><span>공공 서비스 가용성 리포트 · 장애 조기 경보 대시보드</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · 공공 정보등급 ↔ 6R 현대화 ↔ 무중단 CI/CD 배포 ↔ SRE 가용성 전주기 추적</div>

## Ⅲ. 클라우드 네이티브 4대 핵심 기술 요소

> 4대 요소가 결합되어야 장애 격리, 탄력적 오토스케일링, 신속한 기능 릴리즈가 공공 행정 시스템에서 실현됨.

| 핵심 요소 | 핵심 역할 및 원리 | 공공 정보시스템 적용 가치 | 대표 표준 및 기술 |
|---|---|---|---|
| **마이크로서비스 (MSA)** | 단일 거대 모놀리스를 업무 도메인 단위로 분할하여 독립 배포 | 특정 기능(인증/조회) 장애가 전산망 전체 다운으로 전파되는 현상 차단 | Spring Cloud, 전자정부 표준 MSA |
| **컨테이너 (Container)** | OS 레벨 가상화로 인프라 환경 종속성을 제거하고 수초 만에 인스턴스 기동 | 트래픽 폭증 시 오토스케일링(HPA) 및 장애 Pod 자동 자가 복구 | Docker, Kubernetes(K8s), CRI-O |
| **지속적 통합/배포 (CI/CD)** | 코드 커밋부터 검증, 컨테이너 빌드, 배포까지 전 과정 자동화 | 야간·주말 서비스 중단 없는 대국민 무중단 배포(Blue/Green, Canary) | ArgoCD, GitLab CI, Jenkins |
| **데브옵스/관측성 (DevOps)** | 개발과 운영 조직 융합 및 메트릭·로그·트레이스 3대 텔레메트리 통합 | 복잡한 분산 환경에서 트랜잭션 병목 및 장애 원인을 즉시 식별 | OpenTelemetry, Prometheus, Grafana |

## Ⅳ. 단순 클라우드 이전(Lift & Shift) vs 클라우드 네이티브 전환 비교

> Lift & Shift가 하드웨어 장소만 바꾼 이전이라면, 클라우드 네이티브는 소프트웨어 구조와 배포 문화를 전면 혁신하는 것임.

| 비교 항목 | 단순 클라우드 이전 (Lift & Shift) | 클라우드 네이티브 전환 (Cloud Native) |
|---|---|---|
| **변화 범위** | 인프라 계층(IaaS VM) 단순 이전 | 애플리케이션 아키텍처, 데이터, 배포·운영 전반 |
| **아키텍처 구조** | 기존 모놀리식(Monolithic) 구조 유지 | 도메인 주도 설계 기반 **마이크로서비스(MSA)** |
| **확장성 (Scalability)** | 서버 사양을 높이는 수직 확장(Scale-up) 중심 | Pod 단위 자동 확장인 수평 확장(Scale-out, HPA) |
| **배포 및 변경** | 정기 점검 시 수작업 일괄 배포 및 다운타임 발생 | CI/CD 파이프라인 기반 상시 무중단 배포 |
| **장애 격리성** | 단일 모듈 오류 시 전체 시스템 동반 마비 (SPOF) | 서비스 단위 격리로 타 업무 영향도 원천 차단 |
| **적합한 상황** | 단기 데이터센터 계약 만료, 레거시 COTS 패키지 | 지속적 변경 요구, 대규모 변동 트래픽 공공 서비스 |

## Ⅴ. 공공부문 전환 제약 및 실무 통제 대책

> 데이터베이스 강결합과 단일 턴키 발주 관행을 극복하기 위해 분할 발주와 스트랭글러 패턴을 적용해야 함.

| 위험 | 원인 | 통제 | 검증 |
|---|---|---|---|
| **데이터베이스 강결합 분할 난항** | 수십 년간 축적된 레거시 공공 DB의 복잡한 외래키(FK) 및 프로시저 락 | 도메인 주도 설계(DDD) 기반 바운디드 컨텍스트 도출 및 CDC 기반 데이터 동기화 | 트랜잭션 정합성 100% 검증 |
| **단일 턴키 발주 관행 충돌** | 전체를 한 번에 묶어 발주하는 공공 계약 관행으로 인한 대형 SI 종속 | 인프라/플랫폼 구축과 업무 모듈 현대화를 분리하는 '기능 단위 분할 발주' 적용 | 분할 발주 계약 적격성 충족 |
| **상용 COTS 패키지 전환 불가** | 외산 상용 패키지 소스코드 수정 불가 및 컨테이너 미지원 | 패키지 시스템은 Replatform/Rehost로 존치하고 래퍼 API로 MSA 연계 | 레거시 인터페이스 무결성 유지 |

## Ⅵ. 점진적 Strangler 패턴 및 분할 발주 중심의 기술사적 제언

> 공공부문 클라우드 네이티브 전환의 성패는 수천억 원짜리 전면 재구축이 아니라 검증된 작은 단위부터 떼어내는 점진적 전환 거버넌스에 있음.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 공공 행정전산망 마비 사태의 본질은 서버 가상화만 해두고 거대 모놀리식 소프트웨어를 방치하여 한 모듈의 장애가 전산망 전체로 번진 데 있음. 클라우드 네이티브 전환은 기술 도입보다 '데이터베이스를 쪼갤 수 있는가'와 '공공 조달 체계가 분할 계약을 지원하는가'가 결정함.
- 나라면: 일괄 빅뱅 전환의 리스크를 방어하기 위해 행정안전부 클라우드 네이티브 시범 가이드라인을 준용하여 트래픽 집중도가 높은 대민 인증·조회 서비스부터 Strangler Fig 패턴으로 우선 분리하고, 조달청 분할 발주 제도를 활용하여 MSA 단위 플랫폼 전문 기업의 참여를 보장하겠음.

### 실전 답안용 기술사적 제언

- 판정: 전면 빅뱅 일괄 재구축을 지양하고 점진적 스트랭글러(Strangler Fig) 전환 확립
- 대안: **Strangler Fig 패턴 기반 점진 분리** 및 **공공 소프트웨어 분할 발주 제도** 적용
- 검증: 핵심 모듈 분리 후 성능 부하 시험(HPA 오토스케일링) 통과 · 카나리 배포 무중단 확인
- 효과: 행정망 단일 장애점(SPOF) 제거 및 트래픽 폭증 시 대국민 공공서비스 가용성 100% 보증

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 클라우드 네이티브 점진 전환 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail">
      <strong>문제</strong><span>빅뱅 전면 전환의 고위험 · 단일 턴키 계약 · DB 강결합으로 전환 실패</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail">
      <strong>대안</strong><span>대민 접점 모듈부터 Strangler Fig 점진 분리 + 기능 단위 분할 발주</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail">
      <strong>판정</strong><span>CDC 기반 데이터 동기화 정합성 · 트래픽 폭증 시 컨테이너 Pod HPA 확장 실측</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail">
      <strong>효과</strong><span>행정전산망 전면 마비 차단 · 24/365 대국민 무중단 서비스 실현 · 공공 IT 민첩성 극대화</span>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **공공부문 클라우드 네이티브 전환**은 공공 시스템의 탄력성과 회복성을 확보하기 위해 **MSA(마이크로서비스)**, **컨테이너(Container)**, **CI/CD**, **데브옵스(DevOps)** 기반으로 애플리케이션과 운영을 전면 현대화하는 전략
- 목적: 행정전산망 단일장애점(SPOF) 차단 및 24/365 대국민 무중단 서비스 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 클라우드 네이티브 전환 5단계 요약">
  <div class="itpe-pipeline-node">
    <strong>① 진단·6R</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>정보자원 등급 · BIA</span>
      <strong>산출</strong><span>6R 전환전략서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>② 플랫폼구축</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>CSAP 공공존 · K8s</span>
      <strong>산출</strong><span>랜딩존 명세서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>③ 점진현대화</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>DDD 도메인 분할</span>
      <strong>산출</strong><span>Strangler 아키텍처</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>④ 무중단배포</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>카나리/블루그린 전환</span>
      <strong>산출</strong><span>롤백 시나리오</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>⑤ 관측성운영</strong>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>OpenTelemetry · SRE</span>
      <strong>산출</strong><span>가용성 모니터링</span>
    </div>
  </div>
</div>

### 3. 핵심 통제

- **4대 기술 기둥**: MSA(도메인 분할), Container/K8s(오토스케일링), CI/CD(무중단 배포), DevOps(관측성)
- Strangler Fig 점진 전환: 빅뱅 일괄 전환 대신 가치 중심 단위 모듈부터 순차적으로 분리하여 전환 리스크 최소화

## 출제 이력과 검증 출처

- 미출제. 출제 예상: 정부의 공공부문 클라우드 네이티브 전환 로드맵에 따른 4대 핵심 기술 요소와 전환 전략 (25점)
- [행정안전부·한국지능정보사회진흥원(NIA) 공공부문 클라우드 네이티브 도입 가이드라인](https://nia.or.kr)
- [클라우드컴퓨팅 발전 및 이용자 보호에 관한 법률 제20조(국가기관등의 클라우드컴퓨팅 도입 촉진)](https://www.law.go.kr)

## 학습 체크

- [ ] 단순 클라우드 이전(Lift & Shift)과 클라우드 네이티브 전환의 차이를 비교할 수 있는가?
- [ ] 클라우드 네이티브 4대 핵심 요소(MSA, 컨테이너, CI/CD, 데브옵스)의 상호 연계 구조를 설명할 수 있는가?
- [ ] 레거시 모놀리스의 점진적 전환을 위한 Strangler Fig 패턴의 개념과 적용 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [디지털 트랜스포메이션(DX)](./020_digital_transformation.md)
- 연관 토픽: [FinOps](./012_finops.md), [RTO·RPO](./018_rpo.md)
- 다음 토픽: [국가정보자원관리원 화재 분석](./023_national_information_resources_service_fire.md)
