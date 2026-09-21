---
title: "공공부문 클라우드 네이티브 전환"
author: "Antigravity"
date: "2026-09-21T15:30:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 디지털 혁신을 거쳐 공공부문 클라우드 네이티브 전환으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 디지털 혁신</span>
  <strong>공공부문 클라우드 네이티브 전환</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **공공부문 클라우드 네이티브 전환**은 서버 위치만 옮기는 단순 IaaS 이전(Lift & Shift)이 아니라 애플리케이션·데이터·운영을 클라우드 특성에 맞게 전면 현대화하는 전략
- 메커니즘: 진단(6R) → 플랫폼(랜딩존) → 점진 현대화(Strangler Fig) → 무중단 배포(Canary) → 운영 검증(SRE)
- 산출물: 서비스 중요도·보안등급별 6R 전략서 · 마이크로서비스 API 명세서 · SLO 기반 관측성 대시보드

<div class="itpe-flow-map" role="img" aria-label="공공부문 클라우드 네이티브 전환 및 4대 기술 체계">
  <div class="itpe-flow-node">
    <strong>공공 레거시 모놀리식 시스템 한계</strong>
    <small>특정 모듈 장애 시 전산망 전체 다운 · 트래픽 폭증 시 확장 불가</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>클라우드 네이티브 대표 구현요소</strong>
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
- **CSAP(Cloud Security Assurance Program)**: 클라우드서비스의 정보보호 기준 준수 여부를 평가·인증하는 제도
- **SRE(Site Reliability Engineering)**: 소프트웨어 공학 기법을 인프라 운영에 적용하여 SLO 기반 가용성을 보증하는 운영 체계

</details>

## 예상문제

> 공공부문 클라우드 네이티브 전환의 개념과 핵심 요소를 설명하고, 단순 이전과의 차이 및 전환상 문제점·대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 대국민 서비스 안정성과 민첩성을 확보하는 공공 클라우드 네이티브의 개요

> 공공 클라우드 네이티브 전환은 단순 IaaS 서버 이전을 넘어 **애플리케이션과 운영 체계의 전면 현대화**이며, 성패는 공공서비스의 **탄력적 가용성과 무중단 배포 역량**으로 판정함.

- 정의: 공공 정보시스템의 애플리케이션·데이터·운영을 클라우드의 탄력성·회복성·자동화에 맞게 현대화하는 전략
- 목적: 변화 대응력 향상 · 장애영향 축소 · 운영 자동화

## Ⅱ. 공공 클라우드 네이티브의 대표 전환 흐름

> 다음은 진단부터 상시 운영까지를 압축한 대표 흐름이며, 모든 사업에 동일한 공식 5단계를 강제하지 않음.

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

## Ⅲ. 클라우드 네이티브 4대 핵심 구현요소

> 4대 요소 **MSA**·**Container(K8s)**·**CI/CD**·**DevOps/관측성**이 유기적으로 결합되어야 장애 격리, 탄력적 오토스케일링, 무중단 배포가 공공 행정 시스템에서 실현됨.

<div class="itpe-svg-map">
<svg viewBox="0 0 520 330" role="img" aria-label="클라우드 네이티브 4대 구현요소를 MSA, 컨테이너, CI/CD, DevOps 및 관측성으로 분기하고 각 역할과 효과를 표시한 트리">
  <rect class="itpe-svg-node is-current" x="110" y="8" width="300" height="46" rx="12" />
  <text class="itpe-svg-title" x="260" y="31">클라우드 네이티브 4대 요소</text>
  <path class="itpe-svg-link" d="M260 54 V68 H40 V288 M40 102 H70 M40 164 H70 M40 226 H70 M40 288 H70" />
  <rect class="itpe-svg-node" x="70" y="74" width="440" height="56" rx="10" />
  <text class="itpe-svg-sub" x="290" y="94">구조 · MSA(Microservices Architecture)</text>
  <text class="itpe-svg-label" x="290" y="114">도메인 주도 분할 · 결합도 제거 · 장애 격리</text>
  <rect class="itpe-svg-node" x="70" y="136" width="440" height="56" rx="10" />
  <text class="itpe-svg-sub" x="290" y="156">실행 · Container & Kubernetes(K8s)</text>
  <text class="itpe-svg-label" x="290" y="176">표준 패키징 · 수평 확장(HPA) · 자가 치유</text>
  <rect class="itpe-svg-node" x="70" y="198" width="440" height="56" rx="10" />
  <text class="itpe-svg-sub" x="290" y="218">배포 · CI/CD 자동화 파이프라인</text>
  <text class="itpe-svg-label" x="290" y="238">빌드·시험 자동화 · 카나리/블루그린 무중단 릴리즈</text>
  <rect class="itpe-svg-node" x="70" y="260" width="440" height="56" rx="10" />
  <text class="itpe-svg-sub" x="290" y="280">운영 · DevOps & Observability(관측성)</text>
  <text class="itpe-svg-label" x="290" y="300">OpenTelemetry 분산 추적 · SRE 기반 SLO 보증</text>
</svg>
</div>

| 요소 | 역할 | 효과 |
|---|---|---|
| **MSA(Microservices Architecture)** | 업무 경계별 독립 배포 | 변경·장애 범위 축소 |
| **Container·Kubernetes** | 실행환경 표준화·오케스트레이션 | 이식성·탄력성 |
| **CI/CD(Continuous Integration/Continuous Delivery)** | 빌드·시험·배포 자동화 | 변경 리드타임 단축 |
| **DevOps·Observability** | 개발·운영 협업과 신호 통합 | 운영 피드백 단축 |

## Ⅳ. 단순 클라우드 이전(Lift & Shift) vs 클라우드 네이티브 전환 비교

> **Lift & Shift(Rehost)**가 하드웨어 장소만 바꾼 인프라 이전이라면, **클라우드 네이티브(Cloud Native)**는 소프트웨어 아키텍처와 배포·운영 문화를 전면 혁신하는 것임.

| 기준 | Lift & Shift | Cloud Native |
|---|---|---|
| **변화 범위** | 인프라 이전 (IaaS 중심) | 애플리케이션·데이터·운영 현대화 |
| **확장 방식** | 기존 Scale-Up 위주 유지 | 자동화된 수평 확장(Scale-Out/HPA) |
| **변경 방식** | 기존 수작업 정기 배포 유지 | **CI/CD** 기반 무중단 점진 릴리즈 |
| **적용 판단** | 신속 단순 이전·코드 수정 제약 | 대민 트래픽 폭증 대응·지속 혁신 요구 |

## Ⅴ. 공공부문 전환의 문제점·대응책

> 모놀리식 데이터베이스의 강결합과 단일 턴키 발주 관행을 극복하기 위해 **Strangler Fig 패턴**과 단계적 분할 발주 거버넌스를 적용해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **데이터베이스 강결합** | 바운디드 컨텍스트 도출 · **CDC(Change Data Capture)** 기반 동기화 검증 | 정합성을 확인하며 점진 분리 |
| **일괄 발주와 점진 전환 충돌** | 플랫폼·업무서비스의 책임·인터페이스·통합검증 기준 명시 | 단계별 분할 발주 및 검수 가능 |
| **상용 COTS 패키지 전환 불가** | 패키지 시스템은 Replatform/Rehost로 존치하고 래퍼 API로 **MSA** 연계 | 레거시 인터페이스 무결성 유지 및 연계 지연 차단 |

## Ⅵ. 결론 — Strangler Fig 패턴 중심의 점진 전환

> 공공부문 클라우드 네이티브 전환의 성패는 수천억 원짜리 전면 재구축(Big-Bang)이 아니라 검증된 작은 단위부터 떼어내는 **점진적 전환(Strangler Fig) 거버넌스**에 있음.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 클라우드 네이티브의 본질적 가치는 컨테이너 기술 도입 자체가 아니라 서비스 경계·데이터 소유권·배포 책임이 실제로 분리되는 데 있다.
- `나라면`: 전면 빅뱅 재구축 대신 변경 빈도와 장애 영향도가 큰 서비스부터 Strangler Fig 패턴으로 분리하고, 매 단계마다 데이터 정합성·부하 확장성·복구 탄력성을 실측 검증하겠다.

### 실전 답안용 기술사적 제언

- 판정: 빅뱅 일괄 전환 위험을 회피하고 서비스 단위 점진 분리 및 인터페이스 계약 책임을 명시하였는가
- 대안: 대민 파급력이 큰 핵심 모듈부터 **Strangler Fig 패턴** 적용 → 단계적 API 분리
- 검증: **CDC(Change Data Capture)** 기반 데이터 정합성 실측 · 카나리 배포 트래픽 롤백 검증
- 효과: 장애 전파 원천 차단 · 대민 행정서비스 24/365 무중단 가용성 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 클라우드 네이티브 점진 전환 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail">
      <strong>문제</strong><span>빅뱅 전환 위험 · DB 강결합 · 책임 경계 불명확</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail">
      <strong>대안</strong><span>서비스 단위 점진 분리 · 계약·인터페이스 책임 명시</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail">
      <strong>판정</strong><span>데이터 정합성 · 부하시 확장 · 장애시 복구 실측</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail">
      <strong>효과</strong><span>장애영향 축소 · 변경 대응력 향상</span>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 공공 정보시스템의 애플리케이션·데이터·운영을 클라우드의 탄력성·회복성·자동화에 맞게 현대화하는 전략
- 목적: 변화 대응력 향상 · 장애영향 축소 · 운영 자동화

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

- **대표 구현요소**: MSA(서비스 분리), Container·K8s(오케스트레이션), CI/CD(배포 자동화), DevOps·관측성(운영 피드백)
- Strangler Fig 점진 전환: 빅뱅 일괄 전환 대신 가치 중심 단위 모듈부터 순차적으로 분리하여 전환 리스크 최소화

## 출제 이력과 검증 출처

- [국가법령정보센터: 클라우드컴퓨팅법 제20조](https://www.law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1033532191)
- [KISA: 클라우드서비스 보안인증(CSAP)](https://www.kisa.or.kr/1050603)

## 학습 체크

- [ ] Ⅰ 개요: 공공 클라우드 네이티브 전환을 애플리케이션·운영 현대화로 정의할 수 있는가?
- [ ] Ⅱ 전환 흐름: 진단부터 관측성 운영까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ 기술 요소: MSA·컨테이너·CI/CD·DevOps의 역할을 연결할 수 있는가?
- [ ] Ⅳ 비교: Lift & Shift와 클라우드 네이티브의 변화범위·확장·배포 차이를 비교할 수 있는가?
- [ ] Ⅴ 문제점·대응책: DB 강결합·발주 제약·COTS 제약의 위험·대책·효과를 연결할 수 있는가?
- [ ] Ⅵ 결론: 점진 전환의 판정·대안·검증·효과를 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [디지털 트랜스포메이션(DX)](./020_digital_transformation.md)
- 연관 토픽: [FinOps](./012_finops.md), [RTO·RPO](./018_rpo.md)
- 다음 토픽: [국가정보자원관리원 화재 분석](./023_national_information_resources_service_fire.md)
