---
title: "ITSM(IT Service Management)"
author: "Claude Code"
date: "2026-10-18T15:16:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "GLM-5.3 Flash"
---

## 연관 키워드

- ITSM (IT Service Management), IT 서비스 관리
- ITIL 4, SVS (Service Value System), SVC (Service Value Chain)
- AIOps, CMDB (Configuration Management Database), SLA (Service Level Agreement), XLA (Experience Level Agreement)

## Ⅰ. ITSM의 개요

- 핵심 요약 : IT 조직이 비즈니스 요구에 부합하는 고품질 IT 서비스를 제공·관리하기 위한 서비스 중심 IT 관리 체계.
- 개념 : IT (Information Technology) 조직이 비즈니스 요구에 부합하는 고품질의 IT 서비스를 고객에게 효과적으로 제공하고 관리하기 위해 사람, 프로세스, 정보기술을 최적화하는 서비스 중심의 IT 관리 체계 (**ITSM**, IT Service Management). 대표 프레임워크는 ITIL (IT Infrastructure Library)이며, 이후 절은 최신판인 ITIL 4를 기준으로 설명함.
- 배경 및 필요성 : 하드웨어·인프라 중심의 기술 지향 관리로는 비즈니스 요구에 따른 서비스 품질과 사용자 만족을 보장할 수 없어, 비즈니스 가치 창출을 지향하는 고객 중심의 서비스 관리 패러다임으로의 전환이 필요.
- 주요 목적 : IT 서비스 품질 향상, IT 운영 비용 절감 (TCO, Total Cost of Ownership 감축), SLA (Service Level Agreement) 준수를 통한 고객 만족도 제고, 비즈니스와 IT의 전략적 정렬.

## Ⅱ. ITIL 4의 특징

- 핵심 요약 : SVS 전체 운용 모델과 SVC 6개 활동, 7대 기본 원칙, 34개 실천 관행으로 구성된 고객 중심 서비스 관리.
1. 서비스 가치 시스템 (SVS, Service Value System) : 기회·수요를 가치로 전환하는 ITIL 4의 전체 운용 모델.
2. 7대 기본 원칙 (Guiding Principles) : 가치에 집중, 현재 있는 곳에서 시작, 피드백을 통한 반복적 진행, 협업과 가시성 촉진, 전체적으로 사고하고 일하기, 단순하고 실용적으로 유지, 최적화와 자동화.
3. 거버넌스 (Governance) : 조직의 방향을 설정하고 이행을 감독하는 통제 체계.
4. 서비스 가치 사슬 (SVC, Service Value Chain) : 계획, 개선, 참여, 설계/전환, 획득/구축, 제공/지원의 6개 활동.
5. 실천 관행 (Practices) : 일반 관행 14개, 서비스 관행 17개, 기술 관행 3개 등 34개로 분류됨.
6. 지속적 개선 (Continual Improvement) : SVS 전체에 걸쳐 모든 수준에서 상시 수행되는 개선 활동.
7. 4차원 관점 : 조직과 사람, 정보와 기술, 파트너와 공급자, 가치 흐름과 프로세스.

## Ⅲ. ITSM의 구조 (흐름)

- 핵심 요약 : SVS 내부에서 수요를 가치로 전환하는 SVC 6개 활동의 흐름 구조.
- SVS 구조와 SVC 흐름.

```text
      기회(Opportunity)·수요(Demand)
              │
              ▼
 ------------------------------------
   서비스 가치 시스템 (SVS)
 ------------------------------------
   기본 원칙 · 거버넌스
   실천 관행 · 지속적 개선
 ------------------------------------
   서비스 가치 사슬 (SVC) ← 가치 창출
 ------------------------------------
              │
              ▼
           가치(Value)
```

```text
 기회·수요 (Demand)
       │
       ▼
 참여(Engage)
       │
       ▼
 설계/전환 (Design & Transition)
       │
       ▼
 획득/구축 (Obtain/Build)
       │
       ▼
 제공/지원 (Deliver & Support)
       │
       ▼
   가치(Value)

 ── 전 활동 공통 ──
  계획(Plan)    : 목표와 방향 수립
  개선(Improve) : 전 활동 상시 개선
```

- 참여 : 이해관계자의 요구를 수집하고 수요에 대응하는 진입점.
- 설계/전환 : 품질·비용·출시 시점의 요구를 충족하도록 서비스를 설계하고 운영으로 전환.
- 획득/구축 : 합의된 사양에 맞게 서비스 구성요소를 조달·구축.
- 제공/지원 : 합의된 수준에 따라 서비스를 제공하고 지원.
- 위 흐름은 가치 창출의 대표 경로를 단순화한 것으로, 공식 모델에서는 참여가 설계/전환·획득/구축·제공/지원과 다중 연계되고 계획과 개선이 전 활동과 연결됨.

## Ⅳ. ITSM 핵심 운영 프로세스의 비교

- 핵심 요약 : 서비스 데스크·인시던트·문제·변경·서비스 수준 관리의 목적과 활동 비교.
- 인시던트에서 문제 관리로 이어지는 대표 흐름.

```text
[ 인시던트 → 문제 관리 흐름 ]
인시던트 발생 → 임시 조치(Workaround) → 복구
        ↓ 근본 원인 분석(RCA)
문제 등록(KEDB) → 재발 방지 → 변경 요청
```

| 운영 프로세스 | 핵심 목적 | 주요 활동 및 특징 |
|---|---|---|
| 서비스 데스크 (Service Desk) | 사용자와 IT 간의 단일 접점 (SPOC, Single Point of Contact) 운영 | 문의·인시던트·서비스 요청 접수, 에스컬레이션 (Escalation) |
| 인시던트 관리 (Incident Management) | 서비스 중단 시 최단 시간 내 정상 서비스로 복구 | 임시 조치 (Workaround), 우선순위 분류, 긴급 복구 |
| 문제 관리 (Problem Management) | 인시던트의 근본 원인을 분석하여 재발 방지 | 근본 원인 분석 (RCA, Root Cause Analysis), 알려진 오류 데이터베이스 (KEDB, Known Error Database) 등록 |
| 변경 관리 (Change Management) | 서비스 중단 위험을 최소화하면서 안전하게 변경 수행 | 변경 자문 위원회 (CAB, Change Advisory Board) 심의, 영향도 평가, 롤백 (Rollback) 계획 수립 |
| 서비스 수준 관리 (SLM, Service Level Management) | 고객과 합의된 서비스 품질 협약 및 모니터링 | SLA/OLA (Operational Level Agreement) 체결, 서비스 달성도 측정, 서비스 개선 계획 수립 |

- ITIL 4는 프로세스 개념을 실천 관행으로 통칭하며, 인시던트·문제·변경 관리도 모두 실천 관행에 포함됨.

## Ⅴ. ITSM의 장점과 한계

- 핵심 요약 : 고객 중심 서비스 품질 향상의 장점, 프로세스 관료주의·도구 왜곡·CMDB 데이터 노후화의 한계.
- 장점
  1. IT 서비스 품질 향상과 고객 만족도 제고.
  2. SLA 준수를 통한 비즈니스·IT 정렬.
  3. 운영 비용 (TCO) 감축과 표준화된 프로세스.
- 한계점 1 : 프로세스 관료주의화 및 신속성 저하
  - 한계점 : 엄격한 변경 관리 (CAB 승인)와 절차 준수 요구로 인해 경미한 패치나 배포에도 수일이 소요되어 비즈니스 민첩성 저해.
  - 해결 방안 : 반복적 경미 변경을 표준 변경 (Standard Change)으로 사전 승인하여 자동화하고, 데브옵스 (DevOps) CI (Continuous Integration)/CD (Continuous Delivery) 파이프라인과 ITSM 티켓팅을 API (Application Programming Interface)로 자동 연동.
- 한계점 2 : 도구 (Tool) 도입 중심의 왜곡된 운영
  - 한계점 : 조직 문화와 인력 역량 혁신 없이 고가의 솔루션 (ServiceNow 등) 도입에만 치중하여 메뉴만 복잡해지고 활용도 저하.
  - 해결 방안 : 조직 성숙도에 맞추어 인시던트·문제·변경 등 핵심 프로세스를 단계적으로 도입하고, 지속적 개선 (Continual Improvement) 워크숍을 정례화.
- 한계점 3 : CMDB (Configuration Management Database, 구성관리DB)의 데이터 최신성 상실
  - 한계점 : 클라우드 인프라의 동적 생성·삭제 환경에서 수동 입력 위주 CMDB는 실제 형상과 불일치가 누적됨.
  - 해결 방안 : 자동 검색 (Auto-Discovery) 도구로 구성 항목 (Configuration Item)을 자동 수집하고, 인프라 프로비저닝 (Provisioning) 시 CMDB를 실시간 자동 갱신.

## Ⅵ. ITSM에 대한 기술사적 제언

- 핵심 요약 : AIOps 자동화, DevOps 변경 관리 통합, XLA 중심 지표 고도화.
- AIOps (Artificial Intelligence for IT Operations) 기반의 장애 예방 및 인시던트 자동화 : 인프라·애플리케이션 로그를 머신러닝으로 실시간 분석하여 장애 징후를 사전에 감지하고 자가 치유 (Self-Healing)를 수행.
- DevOps 파이프라인과 변경 관리의 통합 : 승인 대기로 인한 릴리스 지연을 해소하기 위해, 자동화된 테스트를 통과한 표준 변경은 승인 절차 없이 파이프라인에서 즉시 배포하도록 간소화.
- 경험 수준 협약 (XLA, Experience Level Agreement) 중심의 지표 고도화 : 가용률 99.9% 등의 기술 지표 중심 SLA 달성에 안주하지 않고, 사용자가 체감하는 만족도와 비즈니스 생산성을 측정 지표로 확대.

## Ⅶ. 결론

- 핵심 요약 : ITSM은 ITIL 4의 SVS·SVC를 기반으로 IT 서비스를 가치로 전환하는 고객 중심 관리 체계이며 AIOps·DevOps·XLA로 진화.
- 요약 : ITSM은 ITIL 4의 SVS와 SVC를 통해 수요를 가치로 전환하고, 34개 실천 관행으로 서비스를 관리하는 체계.
- 시사점 : 프로세스 관료주의와 CMDB 데이터 노후화를 자동화·통합 파이프라인으로 보완하고, XLA 중심의 사용자 체감 지표로 고도화 필요.
