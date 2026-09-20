---
title: "클라우드 전환사업 감리"
author: "Codex"
date: "2026-09-20T19:33:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 IT 감리 및 클라우드 거버넌스를 거쳐 클라우드 전환사업 감리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>IT 감리·클라우드 거버넌스</span>
  <strong>클라우드 전환사업 감리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 온프레미스 시스템의 클라우드 이설 시 발생하는 아키텍처 결함, 보안 취약점, 비용 폭증을 방지하기 위한 전 생애주기 품질 검증
- 메커니즘: **6R 전략** 타당성 검토 → 멀티 AZ/IAM 최소 권한 설계 → **CDC(Change Data Capture)** 무중단 이행 → **FinOps** 비용·탄력성 실측
- 산출: 6R 전환 적합성 검토서 · IaC 정적 보안 점검표 · 데이터 이행 검증 대사표 · FinOps 운영 지침서

<div class="itpe-flow-map" role="img" aria-label="클라우드 전환사업 감리의 기획, 설계, 이행, 운영 4단계 감리 프레임워크">
  <div class="itpe-flow-node">
    <strong>기획·분석 감리</strong>
    <small><span class="itpe-keyword"><strong>6R 전환 전략</strong></span> 타당성 · CSAP 보안 인증 등급제 검토</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>설계 검증</small></div>
  <div class="itpe-flow-node">
    <strong>구조·설계 감리</strong>
    <small>멀티 AZ 고가용성(HA) · IAM 최소 권한 · VPC 망분리</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>이행 안전성</small></div>
  <div class="itpe-flow-node is-current">
    <strong>전환·이행 감리</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>데이터</strong><span><span class="itpe-keyword"><strong>CDC</strong></span> 기반 무중단 실시간 동기화</span></div>
      <div class="itpe-flow-branch"><strong>인프라</strong><span><span class="itpe-keyword"><strong>IaC(코드형 인프라)</strong></span> 정적 보안 취약점 검증</span></div>
      <div class="itpe-flow-branch"><strong>리허설</strong><span>모의전환(Dry-Run) 실측 및 컷오버 롤백 경로</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>운영 안정성</small></div>
  <div class="itpe-flow-node">
    <strong>시험·운영 감리</strong>
    <small>오토스케일링 탄력성 실측 + <span class="itpe-keyword"><strong>FinOps</strong></span> 비용 최적화 대시보드</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **6R 마이그레이션 전략**: AWS/Gartner가 정립한 6가지 클라우드 전환 경로(Rehost, Replatform, Refactor, Repurchase, Retain, Retire)
- **CSAP(Cloud Security Assurance Program)**: 국가·공공기관에 안전한 민간 클라우드를 공급하기 위해 보안 적합성을 인증하는 등급제(상·중·하)
- **공유 책임 모델(Shared Responsibility Model)**: 클라우드 서비스 제공자(CSP)와 이용 기관 간에 보안 및 운영 책임을 명확히 구분하는 원칙
- **IaC(Infrastructure as Code)**: Terraform, CloudFormation 등 코드로 인프라를 정의하고 배포하는 자동화 기술
- **CDC(Change Data Capture)**: 소스 데이터베이스의 변경 로그를 실시간 감지하여 목표 클라우드 DB로 지연 없이 복제하는 무중단 이행 기법
- **FinOps(Financial Operations)**: 클라우드 비용을 실시간 모니터링하고 인스턴스 라이트사이징(Rightsizing)을 통해 비용을 최적화하는 거버넌스

</details>

## 예상문제

> 공공 및 금융 기관의 대규모 클라우드 마이그레이션 사업에서 발생할 수 있는 주요 장애 및 리스크를 예방하기 위한 '클라우드 전환사업 감리'의 필요성, 4단계별 핵심 감리 방법 및 점검 항목, 실무적 보안 및 비용 통제 방안을 설명하시오. (25점)

## Ⅰ. 성공적 클라우드 네이티브 안착의 감시탑, 클라우드 전환 감리의 개요

> 레거시 단순 이전을 탈피하여 **6R 전략**의 적합성, **공유 책임 모델(SRM)** 기반 보안, **FinOps 비용 거버넌스**를 전 생애주기 동안 독립 검증함.

- 정의: 온프레미스 레거시 시스템을 클라우드 환경으로 이전하는 사업에서 전환 계획, 아키텍처 설계, 데이터 이행, 운영 안정성을 전 생애주기에 걸쳐 독립 점검하는 **전문 IT 품질 보증 활동**
- 목적: 리프트앤시프트(Rehost)로 인한 비용 폭증 차단, **CSAP(Cloud Security Assurance Program)** 규제 준수 및 무중단 **데이터 무결성** 확보

## Ⅱ. 클라우드 전환사업 4단계 감리 프레임워크 및 방법론

> 기획부터 설계, 이행, 운영 시험에 이르기까지 클라우드 특화 위험 요인을 차단하는 단계별 감리 파이프라인을 운영함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="클라우드 전환사업 4단계 감리 방법론 및 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 기획·분석 감리 (전환 전략 및 규제 검증)</strong></span>
    <small>업무별 6R 전략 타당성, CSAP 보안인증 등급(상/중/하), TCO/ROI 분석<br />→ 전환 마스터플랜 · TCO 타당성 분석서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 구조·설계 감리 (클라우드 아키텍처 검증)</strong></span>
    <small>멀티 AZ 고가용성(HA), IAM 최소 권한(Least Privilege), VPC 격리<br />→ 클라우드 아키텍처 설계서 · IAM 권한 매트릭스</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 전환·이행 감리 (데이터 무결성 및 인프라 감사)</strong></span>
    <small>CDC 기반 실시간 무중단 복제, IaC 정적 분석(Tfsec), 모의전환 실측<br />→ 데이터 이행 정합성 대사표 · 컷오버 롤백 매뉴얼</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 시험·운영 감리 (탄력성 실측 및 비용 거버넌스)</strong></span>
    <small>오토스케일링 부하 실측, CSP 공유 책임 모델 SLA, FinOps 대시보드<br />→ 성능 시험 성적서 · FinOps 최적화 보고서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>품질 정합성</strong></span> · 6R 타당성 ↔ 멀티 AZ 설계 ↔ CDC 무중단 이행 ↔ FinOps 비용 통제 100% 매핑</div>

## Ⅲ. 클라우드 마이그레이션 6R 전략 점검 기준

> 업무의 복잡도와 트래픽 특성에 따라 최적의 6R 전환 경로가 수립되었는지 심의함.

| 6R 전략 | 핵심 개념 | 감리 중점 점검 포인트 | 추천 적용 대상 업무 |
|---|---|---|---|
| **Rehost** (Lift-and-Shift) | 기존 가상머신을 클라우드 VM(IaaS)으로 단순 복제 이전 | 온프레미스 비효율의 단순 이전 여부, OS/DB 버전 호환성 | 단순 업무, 빠른 이전 필요 시스템 |
| **Replatform** (Lift-Tinker-Shift) | 코어 로직 유지하며 관리형 DB(PaaS) 등으로 부분 교체 | 관리형 서비스 호환성, 백업/패치 자동화 설정 검증 | 웹 애플리케이션, 오픈소스 DB 시스템 |
| **Refactor / Rearchitect** | 컨테이너, MSA, 서버리스 등 클라우드 네이티브 전면 재개발 | 서비스 간 네트워크 지연(Latency), 분산 트랜잭션 정합성 | 트래픽 변동 큰 핵심 코어 비즈니스 |
| **Repurchase** (Drop-and-Shop) | 기존 구축형 소프트웨어를 상용 클라우드 SaaS로 전면 대체 | 레거시 데이터 마이그레이션 API 지원, 커스터마이징 제약 | 이메일, 그룹웨어, 범용 ERP/CRM |
| **Retire** (폐기) | 중복되거나 활용도가 극히 낮은 불필요 시스템 종료 | 타 시스템 연계 의존성 분석, 법적 의무 보존 데이터 아카이빙 | 6개월 이상 비사용 레거시 시스템 |
| **Retain** (잔류·유지) | 이전 비용이 과다하거나 규제상 이전 불가능한 시스템 온프레미스 유지 | 하이브리드 전용선(DirectConnect/VPN) 대역폭 및 보안 | 메인프레임, 특수 하드웨어 종속 시스템 |

## Ⅳ. 전통 온프레미스 감리 vs 클라우드 전환 감리 비교

> 하드웨어 납품 실사에서 벗어나 가상 자원 아키텍처, IAM 권한, 탄력성, FinOps 중심으로 전환됨.

| 비교 항목 | 전통 온프레미스 감리 | 클라우드 전환 감리 |
|---|---|---|
| **인프라 검증 대상** | 물리 서버, 스토리지 납품 실사, 데이터센터 랙 실사 | 가상 자원(VPC, 서브넷, 컨테이너), **IaC(Terraform) 코드** |
| **보안 점검 관점** | 경계 기반 하드웨어 방화벽, 물리적 출입 통제 | Zero Trust, **IAM 최소 권한**, KMS 암호화 키 관리 |
| **가용성 보장 방식** | 장비 이중화(Active-Standby), 물리적 DR 센터 구축 | 멀티 AZ 분산, **오토스케일링**, 글로벌 리전 복제 |
| **비용 통제 점검** | 하드웨어 도입 일시불(CAPEX) 감가상각 검토 | 종량제(OPEX) 최적화, **FinOps 라이트사이징** 점검 |
| **장애 책임 분계** | 시스템 구축 사업자(SI) 및 하드웨어 벤더 책임 | CSP와 이용 기관 간의 **공유 책임 모델(SRM)** 적용 |

## Ⅴ. 성공적 클라우드 전환 감리를 위한 기술사적 제언

> 단순 리프트앤시프트(Rehost)를 지양하고 DevSecOps 자동화 감사와 FinOps 검증을 의무화해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 클라우드 마이그레이션은 '서버의 물리적 주소 이전'이 아니라 소프트웨어 아키텍처의 혁신임. 감리원이 온프레미스 시절의 하드웨어 납품 체크리스트로 클라우드를 점검하면, 클라우드의 본질인 탄력성과 복원력을 놓치고 막대한 비용 낭비만 초래함.
- 나라면: 전환 감리 착수 시 Rehost 비율을 전체의 30% 이내로 엄격히 제한하고, 인프라 배포 파이프라인에 [IaC 정적 보안 스캐너(Tfsec/Checkov)]를 감리 도구로 의무 연동하여 설정 오류(Misconfiguration)를 사전 차단하며, [FinOps 인스턴스 라이트사이징 보고서]를 준공 승인의 필수 감리 산출물로 지정하겠음.

### 실전 답안용 기술사적 제언

- 판정: 물리 하드웨어 검수 위주에서 IaC 코드 보안 및 FinOps 비용 거버넌스 검증으로 전환
- 대안: **IaC 정적 보안 분석 자동화** 및 **FinOps 라이트사이징 감리 의무화**
- 검증: CSAP 보안 기준 100% 충족 · IaC 보안 취약점 0건 · FinOps 유휴 자원 회수율 100%
- 효과: 클라우드 비용 폭증 사전 방지 · 침해사고 예방 및 클라우드 네이티브 안정 가동

<div class="itpe-pipeline is-vertical" role="img" aria-label="클라우드 전환 감리 고도화를 위한 기술사적 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>물리 서버 납품식 체크리스트 · Rehost 위주로 인한 클라우드 비용 폭증</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>IaC 정적 분석 기반 보안 감사 + FinOps 라이트사이징 감리 제도화</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>IAM 최소 권한 원칙 점검 · CDC 무중단 데이터 대사 일치율 100%</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>인프라 운영 비용 30% 절감 · 클라우드 네이티브 고가용성(HA) 확보</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 레거시 정보시스템의 클라우드 이설 시 발생하는 아키텍처 비효율, 보안 결함, 비용 초과를 방지하기 위해 전 생애주기적 품질을 독립 검증하는 **클라우드 전문 IT 감리 활동**
- 목적: **6R 전환 전략** 최적화, **공유 책임 모델(SRM)** 기반 보안 준수 및 **FinOps** 비용 최적화 실현

### 2. 구성체계 및 4단계 감리

<div class="itpe-pipeline is-vertical" role="img" aria-label="클라우드 전환 감리 4단계 구성 요약">
  <div class="itpe-pipeline-node"><strong>기획 감리</strong><small>6R 마이그레이션 전략 · CSAP 인증 등급</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>설계 감리</strong><small>멀티 AZ 고가용성 · IAM 최소 권한 · VPC</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>이행 감리</strong><small>CDC 무중단 데이터 복제 · IaC 정적 분석</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>운영 감리</strong><small>오토스케일링 실측 · FinOps 비용 최적화</small></div>
</div>

### 3. 핵심 통제

- **6R 적합성 심의**: Rehost 지양 및 관리형 서비스(Replatform/Refactor) 중심 전환 유도
- **비용 통제**: 인스턴스 과다 프로비저닝 방지를 위한 FinOps 라이트사이징 검증

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 4교시: 클라우드 컴퓨팅 서비스 전환 시 단계별 감리 점검 방안
- [한국지능정보사회진흥원(NIA), 공공기관 클라우드 전환 사업 감리 가이드라인](https://www.nia.or.kr)
- [과학기술정보통신부·KISA, 클라우드 보안인증제(CSAP) 업무 기준](https://isms.kisa.or.kr)

## 학습 체크

- [ ] 클라우드 마이그레이션 6R 전략의 6가지 유형과 감리 점검 기준을 설명할 수 있는가?
- [ ] 공유 책임 모델(Shared Responsibility Model)에 따른 IaaS/PaaS/SaaS 감리 영역을 구분할 수 있는가?
- [ ] FinOps 및 IAM 최소 권한 원칙을 클라우드 감리 실무에 어떻게 적용할 것인지 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [차세대 시스템 오픈 리스크](./103_next_generation_system_open_risk.md)
- 연관 토픽: [지능정보기술 감리 실무 가이드](./102_intelligent_information_technology_audit_guide.md), [FinOps](./012_finops.md)
- 다음 토픽: [품질비용(Cost of Quality)](./106_cost_of_quality_coq.md)
