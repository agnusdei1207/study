---
title: "ITSM"
author: "Antigravity"
date: "2026-09-20T19:38:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 IT 서비스 운영과 거버넌스를 거쳐 ITSM으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>IT 서비스 운영·거버넌스</span>
  <strong>ITSM</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **ITSM(IT Service Management)**은 기술 인프라 중심의 관리를 탈피하여 사전 합의된 **SLA(Service Level Agreement)** 기반으로 비즈니스 가치를 지속 인도·개선하는 운영 관리 체계
- 메커니즘: 서비스 데스크(SPOC) 접수 → 인시던트 관리(우회책 신속 복구) ↔ 문제 관리(근본 원인 규명 및 **KEDB**) → 변경 관리(**CAB** 심의) → 릴리즈 배포 및 **CMDB** 동기화
- 산출: 서비스 카탈로그 · **SLA/OLA** 협약서 · 인시던트 티켓 · **KEDB(Known Error Database)** · 변경 승인서(RFC) · **CMDB** 형상 정보

<div class="itpe-flow-map" role="img" aria-label="ITSM 핵심 프로세스 연계 및 지속적 서비스 개선 흐름">
  <div class="itpe-flow-node">
    <strong>사용자 요청 및 인시던트 접수</strong>
    <small>서비스 데스크(SPOC) · 단일 접점 티켓 발행</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>ITSM 코어 프로세스 루프</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>인시던트</strong><span>신속 복구 및 우회책(Workaround) 적용</span></div>
      <div class="itpe-flow-branch"><strong>문제 관리</strong><span>5-Why 원인 분석 및 <span class="itpe-keyword"><strong>KEDB</strong></span> 등록</span></div>
      <div class="itpe-flow-branch"><strong>변경·릴리즈</strong><span><span class="itpe-keyword"><strong>CAB</strong></span> 심의 · <span class="itpe-keyword"><strong>CMDB</strong></span> 갱신 및 무중단 배포</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>지속적 서비스 개선 (CSI)</strong>
    <small>SLA 달성도 분석 · XLA 체감 품질 향상</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **ITSM(IT Service Management)**: IT 서비스를 고객 관점에서 정의하고 프로세스 기반으로 기획·구축·운영·개선하는 총체적 관리 프레임워크
- **ITIL(Information Technology Infrastructure Library)**: IT 서비스 관리 모범 실천법(Best Practice)을 집대성한 사실상 표준(de facto)
- **ISO/IEC 20000**: ITSM 체계의 적격성을 검증하고 심사하는 제3자 인증 국제표준
- **SLA(Service Level Agreement)**: 서비스 제공자와 고객 간에 서비스 가용성, 복구 시간 등 목표 수준을 명시한 정량적 협약
- **SPOC(Single Point of Contact)**: 모든 사용자 문의, 요청, 장애 접수를 일원화하는 단일 접점 창구
- **KEDB(Known Error Database)**: 문제 관리에서 규명한 근본 원인과 공식 우회책(Workaround)을 저장한 지식 베이스
- **CAB(Change Advisory Board)**: 변경 요청(RFC)의 기술적 영향도, 비즈니스 리스크, 작업 일정을 사전 심의하는 자문 협의체
- **CMDB(Configuration Management Database)**: IT 서비스와 인프라 구성요소(CI) 간의 의존 관계를 저장·관리하는 형상 데이터베이스
- **XLA(Experience Level Agreement)**: 시스템 가동률 중심의 기술 SLA 한계를 극복하기 위해 사용자 체감 만족도를 측정하는 협약

</details>

## 예상문제

> ISO/IEC 20000 및 ITIL 4 기반의 정보기술 서비스 관리체계(ITSM)의 개념을 설명하고, 인시던트·문제·변경 관리의 상호 연계 프로세스와 참조 아키텍처, 수박 효과(Watermelon Effect) 극복을 위한 XLA 도입 방안을 논하시오. (25점)

## Ⅰ. 고객 가치 중심의 IT 운영 체계, ITSM의 개요

> ITSM은 단순 장비 가동률 점검이 아니라 고객과 합의된 **SLA**를 준수하여 비즈니스 가치를 보호하는 체계이며, 성패는 **KEDB** 기반의 원인 제거와 무장애 **변경 관리**로 판정함.

- 정의: 고객에게 합의된 품질의 IT 서비스를 제공하기 위해 **ITIL** 및 **ISO/IEC 20000** 기반으로 서비스 수명주기 전반을 프로세스로 체계화한 **IT 서비스 관리체계(ITSM)**
- 목적: 정량적 **SLA(Service Level Agreement)** 달성 통한 IT 서비스 안정성 확보, 인프라 운영 비용 최적화 및 **비즈니스 가치 창출**

## Ⅱ. ITSM 핵심 4대 운영 프로세스 및 연계 방법론

> 인시던트로 신속히 서비스를 복구하고, 문제 관리로 재발을 방지하며, 변경 관리로 시스템 무결성을 통제함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="ITSM 핵심 4대 프로세스 연계 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 인시던트 관리 (Incident Management)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>SPOC 단일 접수, 장애 증상 분류, 우회책(Workaround) 적용</span></div>
    <div class="itpe-step-detail"><strong>목표·산출물</strong><span>서비스 최단 시간 정상 복구, 인시던트 처리 티켓</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 문제 관리 (Problem Management)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>5-Why 근본 원인(Root Cause) 규명, 장애 재발 방지 대책 수립</span></div>
    <div class="itpe-step-detail"><strong>목표·산출물</strong><span>KEDB(Known Error DB) 등록, 변경 요청서(RFC) 발행</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 변경 관리 (Change Management)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>변경자문위원회(CAB) 영향도 심의, 다운타임 충돌 검증</span></div>
    <div class="itpe-step-detail"><strong>목표·산출물</strong><span>변경 승인(RFC Approve), 롤백 비상계획서 확정</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 릴리즈 및 배포 (Release & Deployment)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>스테이징 사전 검증, 무중단 카나리 배포, 형상 실시간 갱신</span></div>
    <div class="itpe-step-detail"><strong>목표·산출물</strong><span>배포 완료 보고서, CMDB 형상 정보 및 서비스 카탈로그 갱신</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>지속적 개선(CSI)</strong></span> · 운영 데이터 분석 기반 SLA 지표 갱신 및 서비스 품질 고도화 선순환 환류</div>

## Ⅲ. ITSM 참조 아키텍처 및 핵심 통제 요소

> 서비스 데스크를 단일 창구로 두고 KEDB와 CMDB를 데이터 허브로 삼아 프로세스 간 단절 없는 추적성을 보장함.

| 구성요소 | 핵심 역할 및 기능 | 통제 메커니즘 | 핵심 산출물 |
|---|---|---|---|
| **서비스 데스크** | 사용자 접점 일원화(**SPOC**), 1차 해결 및 에스컬레이션 | 티켓팅 시스템 기반 SLA 복구 시간 모니터링 | 인시던트 접수증, 처리 로그 |
| **KEDB** | 기지 오류 및 공식 우회책(Workaround) 저장소 | 인시던트 발생 시 검색 연동을 통한 초동 해결 시간 단축 | 알려진 오류 명세서, 해결 가이드 |
| **CAB** | 비즈니스 영향도, 다운타임 위험, 변경 충돌 심의 협의체 | 긴급·일반·표준 변경의 3등급 차등화 심의 | 변경 승인서, 배포 승인 일정표 |
| **CMDB** | IT 서비스, 서버, 네트워크, DB 간 논리적 연관 관계 관리 | CI(Configuration Item) 의존성 시각화로 영향도 분석 지원 | 형상 베이스라인, 변경 이력 로그 |

## Ⅳ. ISO/IEC 20000 기반 수명주기 4단계 프로세스

> 서비스 기획부터 설계, 전환, 운영, 지속적 개선까지의 선순환 수명주기를 표준화함.

| 수명주기 단계 | 주요 활동 내용 | 핵심 통제 기준 및 산출물 |
|---|---|---|
| **1. 서비스 전략 및 기획** | 고객 비즈니스 요구사항 분석, IT 서비스 포트폴리오 정의, 투자 타당성 검토 | 서비스 포트폴리오 정의서, ROI 분석서 |
| **2. 서비스 설계 및 구축** | 서비스 카탈로그 작성, **SLA/OLA/UC** 연계 설계, 가용성·보안·연속성 계획 수립 | 서비스 카탈로그, SLA 계약서, BCP 계획 |
| **3. 서비스 전환 및 릴리즈** | 인수 테스트(UAT), 사용자 교육, 전환 롤백 계획 수립, 파일럿 무중단 릴리즈 | 전환 계획서, 릴리즈 패키지 검증서 |
| **4. 서비스 운영 및 개선** | 서비스 데스크 가동, 인시던트/문제 해결, **CSI(지속적 서비스 개선)** 환류 | 월간 SLA 평가 보고서, CSI 개선 과제철 |

## Ⅴ. 전통적 IT 관리 vs ITSM vs DevOps/SRE 비교

> 안정성 확보를 위한 프로세스 중심의 통제(ITSM)와 빠른 출시를 위한 자동화 엔지니어링(SRE)의 균형이 요구됨.

| 비교 항목 | 전통적 IT 관리 | ITSM (ITIL 기반) | DevOps / SRE |
|---|---|---|---|
| **초점 영역** | H/W, 서버, 네트워크 기술 | 고객 관점의 비즈니스 서비스 | 개발-운영 통합 및 소프트웨어 신뢰성 |
| **관리 방식** | 사후 장애 처리, 엔지니어 직관 | 프로세스 준수, **SLA 계약**, CAB 심의 | CI/CD 자동화 파이프라인, **에러 예산(Error Budget)** |
| **주요 지표** | 서버 가동률, 리소스 점유율 | **SLA 달성률**, MTTR, 인시던트 해결률 | 배포 빈도, 변경 실패율, 복구 시간(MTTR), **SLO** |
| **한계 및 약점** | 비즈니스와 단절, 잦은 장애 | 문서화·심의 오버헤드로 인한 배포 지연 | 거버넌스 부재 시 대외 규제 컴플라이언스 위험 |

## Ⅵ. 실무 운영 실패 요인과 공학적 통제 방안

> 지표 왜곡 현상(수박 효과)을 방지하고 수작업 승인 병목을 해소하기 위한 기술적 개선이 필수적임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **수박 효과(Watermelon)** | 기술 SLA 외에 사용자 체감 지표인 **XLA(Experience Level)** 결합 | 실질적 서비스 만족도 향상 |
| **CAB 심의 병목** | 변경 등급화: 저위험 **표준 변경**은 CI/CD 무심의 자동 배포 | 리드타임 단축 및 배포 민첩성 확보 |
| **인시던트-문제 혼재** | 담당자 역할 분리 및 **동일 장애 3회 누적 시 문제 티켓 자동 승격** | 고질적 반복 장애 원천 차단 |
| **CMDB 형상 노후화** | **Cloud Discovery 도구** 및 IaC 파이프라인 연동 실시간 동기화 | 변경 영향도 분석 정확도 100% 확보 |

## Ⅶ. SRE 에러 예산 결합 중심의 기술사적 제언

> 전통적 ITSM의 거버넌스 통제력 위에 SRE의 자동화 실천법을 결합하여 '안정성'과 '민첩성'의 이율배반을 극복해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: ITSM의 본질은 IT 부서의 무사안일한 가동률 자랑이 아니라 비즈니스 사용자가 체감하는 가치와 경험(XLA)을 수호하는 데 있음. 무거운 CAB 심의가 개발의 속도를 가로막지 않도록 위험도 기반의 자동화 파이프라인을 구축해야 함.
- 나라면: 전사 거버넌스 구축 시 `SLI/SLO/SLA 3계층 서비스 지표 체계 정립 → 에러 예산(Error Budget)이 소진된 위험 시점에만 긴급 CAB 승인을 요구하는 정책 수립 → 클라우드 Discovery 도구 기반 CMDB 실시간 자동 갱신`을 운영 계약에 명문화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 프로세스 관료주의(Bureaucracy)를 탈피한 서비스 신뢰성 공학(SRE)과의 결합
- 대안: **ITSM 거버넌스 + SRE 에러 예산 연동** 및 **XLA 기반 체감 품질 평가**
- 검증: **XLA 만족도 지수** 달성률 · 표준 변경의 자동 배포 비율 80% 이상 확보
- 효과: 배포 속도 향상과 서비스 가용성 유지를 동시에 달성하여 비즈니스 경쟁력 극대화

<div class="itpe-pipeline is-vertical" role="img" aria-label="ITSM과 SRE 결합을 통한 실효적 서비스 운영 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제점</strong><span>수박 효과(기술 달성 vs 고객 불만), CAB 승인 지연, 수작업 CMDB 불일치</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>추진 전략</strong><span>XLA 지표 도입, SRE 에러 예산 연계 무심의 배포, Cloud Discovery 자동화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>관리 지표</strong><span>사용자 여정 체감 응답시간, SLO 위반율 모니터링, 형상 데이터 일치율</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>최종 효과</strong><span>릴리즈 리드타임 획기적 단축, 반복 장애 근절 및 비즈니스 가치 실현</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **ITSM(IT Service Management)**은 IT 운영을 고객 및 비즈니스 관점에서 정의하고 사전에 합의된 **SLA(Service Level Agreement)**에 따라 전 수명주기를 프로세스로 관리하는 체계
- 목적: IT 서비스 품질 표준화, 안정적 서비스 제공 통한 **비즈니스 가치 창출**

### 2. 구성체계 및 핵심 프로세스 루프

<div class="itpe-pipeline is-vertical" role="img" aria-label="ITSM 핵심 운영 프로세스 요약">
  <div class="itpe-pipeline-node">
    <strong>서비스 데스크</strong>
    <div class="itpe-step-detail"><strong>접점 일원화</strong><span>단일 접점(SPOC) 티켓 접수 및 1차 조치</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>인시던트 관리</strong>
    <div class="itpe-step-detail"><strong>신속 복구</strong><span>우회책(Workaround) 활용 최단 시간 복구</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>문제 관리</strong>
    <div class="itpe-step-detail"><strong>원인 규명</strong><span>5-Why 근본 원인 분석 및 KEDB 지식 자산화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>변경 및 릴리즈</strong>
    <div class="itpe-step-detail"><strong>통제 배포</strong><span>CAB 심의 후 CMDB 갱신 및 무중단 배포</span></div>
  </div>
</div>

### 3. 핵심 통제

- **KEDB(Known Error Database)**: 알려진 오류 및 우회책 데이터베이스화를 통한 초동 조치 가속화
- **수박 효과 극복**: 단순 인프라 SLA를 넘어 사용자 경험 지표인 **XLA(Experience Level Agreement)** 결합

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 3교시: ISO/IEC 20000 기준 ITSM 개념 및 서비스 설계/구축, 전환 활동
- [ISO/IEC 20000-1:2018, Information technology — Service management](https://www.iso.org)
- [AXELOS, ITIL 4 Foundation: ITIL 4 Edition](https://www.axelos.com)

## 학습 체크

- [ ] 인시던트 관리와 문제 관리의 차이점 및 상호 연계 프로세스를 도식화할 수 있는가?
- [ ] ISO/IEC 20000 수명주기 4단계(전략, 설계, 전환, 운영)의 주요 활동을 서술할 수 있는가?
- [ ] CMDB의 역할과 변경 관리(CAB)와의 상호작용 메커니즘을 설명할 수 있는가?
- [ ] 수박 효과(Watermelon Effect)의 원인과 이를 극복하기 위한 XLA 도입 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [ISO 21500](./043_iso_21500.md)
- 연관 토픽: [SLA](./006_sla.md), [ISO/IEC 38500](./002_iso_iec_38500.md), [IT 아웃소싱](./033_it_outsourcing.md)
- 다음 토픽: [MECE](./045_mece.md)
