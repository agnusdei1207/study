---
title: "시스템 운영 감리"
author: "Antigravity"
date: "2026-09-20T19:48:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 정보시스템 감리 및 품질 보증을 거쳐 시스템 운영 감리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>정보시스템 감리·품질 보증</span>
  <strong>시스템 운영 감리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **시스템 운영 감리**는 정보시스템 가동 후 서비스 가용성, 인프라 용량, 재해복구 체계 등 운영 안정성을 진단하는 '운영 감리'와, 응용 소프트웨어 결함 수정 및 과업 변경 적정성을 진단하는 '유지보수 감리'의 독립적 종합 품질 보증 활동
- 메커니즘: `서비스 수준(SLA) + 용량·성능 + BCP/DR + 백업·복원 + 보안`의 5대 운영 영역과, `과업 범위 + 서비스 요청(SR) + 결함 품질 + 형상 관리`의 4대 유지보수 영역을 교차 실사
- 산출: 운영 감리 점검표 · **SLA(Service Level Agreement)** 달성도 분석서 · 백업 무작위 복원 실사실적서 · 과업 변경 이행 검토서 · 시정조치 확인보고서

<div class="itpe-flow-map" role="img" aria-label="시스템 운영 및 유지보수 감리 점검 흐름도">
  <div class="itpe-flow-node">
    <strong>시스템 가동 및 운영 계약 체결</strong>
    <small>가동 후 장애 방지 · 유지관리 계약 및 SLA 기준선 설정</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>운영 감리 및 유지보수 감리 종합 실사</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>운영 5대</strong><span><span class="itpe-keyword"><strong>ITSM/SLA</strong></span> · 용량 관리 · <span class="itpe-keyword"><strong>BCP/DR</strong></span> · 백업 복원 · 정보보안</span></div>
      <div class="itpe-flow-branch"><strong>유지보수 4대</strong><span>계약·과업 이행 · <span class="itpe-keyword"><strong>SR 변경</strong></span> · 결함 품질 · 형상 무결성</span></div>
      <div class="itpe-flow-branch"><strong>동적 실증</strong><span>단순 서류 탈피 · 백업 미디어 실복원 · 카오스 장애 주입</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>상시 서비스 연속성 보증 및 무상 과업 추가 차단</strong>
    <small>RTO/RPO 실측 검증 · 투입 공수 투명성 확보 및 SW 제값주기 실현</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **ITSM(IT Service Management)**: IT 서비스를 고객 관점에서 계획, 설계, 전달, 운영 및 개선하는 관리 프레임워크
- **SLA(Service Level Agreement)**: 서비스 제공자와 수혜자 간에 합의된 서비스 가동률, 응답 시간 등 정량적 성과 지표 협약
- **BCP(Business Continuity Planning)**: 재해나 비상사태 발생 시 조직의 핵심 비즈니스 기능을 중단 없이 지속하기 위한 연속성 계획
- **DR(Disaster Recovery)**: 재해로 인한 주 전산센터 마비 시 백업 센터를 통해 시스템을 신속히 복원·재개하는 공학적 복구 체계
- **RTO(Recovery Time Objective)**: 재해 발생 시점부터 서비스가 정상 복구되어 재개될 때까지 허용되는 최대 목표 복구 시간
- **RPO(Recovery Point Objective)**: 재해 발생 시 데이터 손실을 감내할 수 있는 과거 시점까지의 최대 허용 데이터 손실 기준
- **SR(Service Request)**: 운영 중 사용자나 관리자로부터 발생하는 오류 수정, 기능 개선 등의 공식 서비스 요청
- **APM(Application Performance Monitoring)**: 응용 소프트웨어 및 인프라의 트랜잭션, 응답속도, 자원 점유율을 실시간 계측·분석하는 모니터링 도구

</details>

## 딸려 나오는 하위 토픽

| 키워드 | 등급 | 학습 역할 및 연결 이유 | 핵심 질문/키워드 |
|---|---|---|---|
| **유지보수 감리** | B | 시스템 운영 감리와 함께 가동 후 단계에서 응용 SW 결함 개선 및 계약 이행을 검증하는 필수 하위 영역 | 과업 범위 준수, 부당한 무상 과업 추가 방지, 형상 관리 무결성 |

## 예상문제

> 정보시스템 감리 기준에 따른 '시스템 운영 감리'와 '유지보수 감리'의 개념을 비교하고, 시스템 운영 감리의 5대 점검분야와 유지보수 감리의 4대 점검분야, 형식적 서류 감리를 극복하기 위한 실무 동적 검증 방안을 설명하시오. (25점)

## Ⅰ. 가동 후 서비스 안정성과 계약 이행을 보증하는 감리의 개요

> 시스템 운영 감리는 인프라 가용성과 BCP 체계를, 유지보수 감리는 응용 SW 품질과 과업 변경을 검증하며, 성패는 **무작위 백업 복원 실사**와 **비공식 과업 추가 차단**으로 판정함.

- 정의: 정보시스템 가동 후 서비스 가용성, 인프라 성능, 재난복구 체계를 점검하는 **시스템 운영 감리**와, 응용 SW 하자보수 및 계약 과업 범위를 점검하는 **유지보수 감리**의 독립적 종합 품질 검증 활동
- 목적: 시스템 상시 가용성 보증, **BCP/DR** 실효성 검증 및 비공식 과업 추가 통제

## Ⅱ. 시스템 운영 감리 vs 유지보수 감리 비교

> 운영 감리는 인프라의 상시 가용성을 보장하는 데 집중하고, 유지보수 감리는 계약된 범위 내에서 소프트웨어 품질이 개선되는지 통제함.

| 비교 항목 | 시스템 운영 감리 (Operation Audit) | 유지보수 감리 (Maintenance Audit) |
|---|---|---|
| **핵심 점검 대상** | 서버, 네트워크, DBMS, 클라우드 인프라, **SLA(Service Level Agreement)** | 응용 소프트웨어 소스코드, **SR(Service Request)**, 유지관리 인력 |
| **품질 검증 초점** | 시스템 가용성(Availability), 비즈니스 연속성(Resilience) | 계약 이행 완결성, 결함 개선율, 형상 베이스라인 무결성 |
| **주요 평가 기준** | SLA 목표치 달성률, **RTO/RPO** 지표 준수, 백업 주기 | 제안요청서 과업 범위, 과업심의위원회 의결서, 기술자 투입 공수 |
| **점검 기법** | 모니터링 로그 분석, 부하 시험 계측, **백업 실복원 실사** | 기능점수(FP) 산정 검토, 소스코드 정적 분석, 형상 감사 |
| **수행 시점** | 시스템 오픈 후 정기적(연 1회) 또는 대규모 인프라 개편 시 | 정기 유지보수 사업 종료 전 또는 계약 갱신 시점 |

## Ⅲ. 시스템 운영 감리 5대 분야 및 유지보수 감리 4대 분야 체계

> 운영과 유지보수는 독립적이면서도 긴밀히 상호작용하므로 두 영역의 점검 체계가 단절 없이 결합되어야 함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="운영 감리 5대 분야 및 유지보수 감리 4대 분야 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>[운영 감리] ① 서비스 관리 및 ITSM</strong></span>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>SLA 지표 설정 현실성, MTTR 로그 및 ITSM 티켓 검증</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>[운영 감리] ② 성능 및 용량 관리</strong></span>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>피크 타임 자원 병목 식별, 3개년 증설 계획 및 APM 추이 실사</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>[운영 감리] ③ BCP 및 재해복구(DR)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>RTO/RPO 부합성, 데이터 동기화 지연 계측 및 모의훈련 실효성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>[운영 감리] ④ 백업 및 무작위 복원 실사</strong></span>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>풀/증분 및 원격 소산 정책, 실제 데이터 복원 시간 실측</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>[유지보수] ⑤ 계약 이행, SR 변경 및 형상 통제</strong></span>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>과업 범위 준수, 구두 요구 차단, 과업심의 의결서 및 형상 무결성</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability & Continuity</strong></span> · SLA 지표 ↔ 인프라 용량 ↔ 재해복구(DR) ↔ 소스 형상 ↔ 과업 계약 완결</div>

## Ⅳ. 신규 구축 감리 vs 시스템 운영 감리 vs 유지보수 감리 3자 비교

> 사업 단계별 라이프사이클에 따라 감리 목적과 중점 점검 기법이 명확히 구별됨.

| 비교 항목 | 신규 구축(개발) 감리 | 시스템 운영 감리 | 유지보수 감리 |
|---|---|---|---|
| **주요 목적** | 요구사항의 설계도서 반영 및 기능 구현 검증 | 상시 가용성 보장 및 **BCP/DR** 연속성 보증 | SW 하자 개선 및 계약 과업 이행 정당성 검증 |
| **감리 시점** | 요구정의, 설계, 종료 단계 (3단계 감리) | 가동 후 정기적 수행 (연 1회 이상) | 유지보수 사업 기간 중 또는 연간 계약 종료 시 |
| **핵심 산출물** | 단계별 감리보고서 (적합/부적합/개선권고) | 운영 감리 결과보고서 · 가용성 진단서 | 과업 이행 평가서 · 결함 조치율 분석서 |
| **핵심 기법** | CBD 방법론, 기능점수, 테스트 커버리지 | **APM 계측**, 백업 실복원, 모의 장애 주입 | 정적 소스코드 분석, 형상 감사, 과업 심의 |
| **법적 통제** | 전자정부법상 10억 이상 의무 감리 | 국가정보화기본법 및 감리기준 고시 | 공공 SW사업 계약 기준 및 과업심의 연계 |

## Ⅴ. 실무 감리 시 위험 요인 및 기술사적 대책

> 단순 매뉴얼과 로그 화면 육안 확인에 의존하는 형식적 서류 감리는 실제 재해 발생 시 대형 장애로 직결됨.

| 위험 | 대책 | 효과 |
|---|---|---|
| **서류 중심 형식적 백업 검증** | 감리 현장에서 무작위 백업 미디어 추출 후 **테스트 서버 실복원 실사** | 백업 데이터 무결성 100% 확보 및 목표 RTO 이내 복원 완료 |
| **운영 중 부하 테스트 한계** | 스테이징 환경 대상 **트래픽 미러링(Shadowing)** 기법 및 심야 계측 | 상용 서비스 영향도 제로화 및 피크 부하 임계치 식별 |
| **부당한 무상 과업 추가 묵인** | SR 접수 대장과 실제 Git 커밋 로그 교차 감사 및 **과업심의위 회부** | 계약 외 과업 적발률 제고 및 정당한 대가 지급 체계 확립 |
| **SLA 지표의 왜곡 보고** | **APM 및 불변 감사 로그(Immutable Audit Log)** 기반 지표 교차 검증 | 허위 가동률 보정 및 객관적 MTBF/MTTR 산출 |

## Ⅵ. 카오스 엔지니어링 기반 실전형 감리 중심의 결론

> 시스템 운영 감리는 정적 서류 대조를 탈피하여, 실제 인위적 장애 상황에서 목표 복구 시간 내에 서비스가 정상 절체되는지 검증하는 **동적 실증 감리**로 진화해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 백업 로그가 '성공(Success)'으로 찍혀 있어도 실제 스토리지 블록이 깨져 복원이 실패하는 사례가 빈번함. 감리원이 현장에서 임의의 과거 백업본을 골라 테스트 장비에 직접 마운트해 보는 물리적 복원 실사가 가용성 보증의 유일한 해법임.
- 나라면: 1등급 공공 핵심 인프라 운영 감리 시 카오스 엔지니어링 도구(Chaos Mesh 등)를 이용해 컨테이너 강제 종료나 네트워크 지연을 인위적으로 주입하고, 액티브-액티브 스토리지 DR이 무중단 자동 절체되는지 실시간 참관하여 감리보고서에 증적을 남기겠음.

### 실전 답안용 기술사적 제언

- 판정: 점검표 체크박스 확인보다 실제 장애 복원 실증 여부로 감리 품질 판정
- 대안: **무작위 백업 실복원 실사 의무화** + **카오스 엔지니어링 기반 DR 모의 절체**
- 검증: 목표 RTO/RPO 지표 충족 여부 실측 · 과업 변경 이력 교차 감사
- 효과: 대형 전산 마비 사고 원천 차단 · 유지보수 사업자 부당 노동 방지 및 상호 신뢰 제고

<div class="itpe-pipeline is-vertical" role="img" aria-label="시스템 운영 감리 실전형 진화 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>취약점</strong><span>로그 화면 단순 대조, 백업 미복원 위험 방치, 구두 과업 추가 묵인</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>동적 검증</strong><span>무작위 백업 실복원 실사 및 카오스 엔지니어링 기반 장애 주입 검증</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>목표 지표</strong><span>목표 RTO/RPO 실측치 부합, 소스 형상과 SR 일치율 100% 달성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>가치 창출</strong><span>재난 시 무중단 복구 능력 확보, SW 제값주기 및 서비스 연속성 완성</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **시스템 운영 감리**는 정보시스템 가동 후 가용성, 인프라 용량, 재해복구 체계를 점검하는 '운영 감리'와, 응용 SW 결함 수정 및 과업 범위를 점검하는 '유지보수 감리'의 독립적 종합 품질 검증 활동
- 목적: 시스템 상시 가용성 보증, BCP/DR 실효성 검증 및 비공식 과업 추가 통제

### 2. 운영 감리 및 유지보수 감리 핵심 점검 분야

<div class="itpe-pipeline is-vertical" role="img" aria-label="운영 및 유지보수 감리 핵심 점검 분야 요약">
  <div class="itpe-pipeline-node">
    <strong>운영: ITSM / SLA</strong>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>가동률 지표 적정성 및 인시던트 처리 검증</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>운영: 성능·용량 & DR</strong>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>피크 병목 식별 및 RTO/RPO 충족 여부 실사</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>운영: 백업 복원 실사</strong>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>무작위 백업본 추출 및 실제 복구 계측</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>유지보수: 과업 & 형상</strong>
    <div class="itpe-step-detail"><strong>핵심 점검</strong><span>계약 범위 준수, SR 변경 통제 및 형상 무결성</span></div>
  </div>
</div>

### 3. 핵심 통제

- **무작위 백업 실복원 실사**: 백업 성공 로그 육안 확인을 배제하고, 현장에서 무작위 샘플 데이터를 테스트 서버에 직접 복원하여 무결성과 RTO 실측
- **과업 변경 및 형상 감사**: 사용자 서비스 요청(SR) 대장과 소스코드 커밋 로그를 교차 대조하여 발주자의 비공식 무상 요구 차단 및 소프트웨어 제값주기 실현

## 출제 이력과 검증 출처

- 제137회 정보관리기술사 4교시 2번: 시스템 운영 및 유지보수 감리의 개념, 운영 감리 점검분야, 유지보수 감리 점검분야
- 제130회 정보관리기술사 2교시: 공공 정보시스템 감리 프레임워크 및 단계별 점검 기준
- 행정안전부, '정보시스템 감리 기준 (행정안전부 고시 제2023-3호)'
- 한국지능정보사회진흥원(NIA), '정보시스템 운영 감리 실무 가이드라인'

## 학습 체크

- [ ] 시스템 운영 감리와 유지보수 감리의 목적, 대상, 평가 기준의 차이를 설명할 수 있는가?
- [ ] 시스템 운영 감리의 5대 점검 분야(SLA, 용량, BCP/DR, 백업, 보안)를 기술할 수 있는가?
- [ ] 유지보수 감리에서 과업 변경 심의 및 무상 과업 추가 차단의 중요성을 논술할 수 있는가?
- [ ] 서류 중심 감리를 탈피한 '무작위 백업 실복원 실사'의 수행 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [기술 주권](./058_technology_sovereignty.md)
- 연관 토픽: [정보시스템 감리](./008_it_audit.md), [액티브-액티브 스토리지 DR](./027_active_active_storage_dr.md), [SLA](./006_sla.md)
- 다음 토픽: [AI 에너지 인프라](./060_ai_energy_infrastructure.md)
