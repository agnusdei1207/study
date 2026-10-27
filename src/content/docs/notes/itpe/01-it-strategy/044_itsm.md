---
title: "ITSM(IT Service Management)"
author: "Claude Code"
date: "2026-10-24T23:46:02+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "044"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- ITSM (IT Service Management), IT 서비스 관리
- ITIL 4, SVS (Service Value System), SVC (Service Value Chain)
- AIOps, CMDB (Configuration Management Database), SLA (Service Level Agreement), XLA (Experience Level Agreement)

## Ⅰ. ITSM의 개요

- 핵심 요약 : IT 조직이 비즈니스 요구에 맞는 고품질 IT 서비스를 제공·관리하기 위한 서비스 중심 IT 관리 체계.
- 개념 : IT (Information Technology) 조직이 사람·프로세스·정보기술을 최적화해 비즈니스 요구에 부합하는 고품질 IT 서비스를 제공·관리하는 서비스 중심 체계 **ITSM** (IT Service Management). 대표 프레임워크는 **ITIL** (IT Infrastructure Library)이며, 이후 절은 최신판인 ITIL 4를 기준으로 서술함.
- 배경 및 필요성 : 하드웨어·인프라 중심의 기술 지향 관리로는 서비스 품질과 사용자 만족을 보장하기 어려워, 비즈니스 가치를 지향하는 고객 중심의 서비스 관리로 전환할 필요가 있음.
- 주요 목적 : IT 서비스 품질 향상, **TCO** (Total Cost of Ownership, 총소유비용) 절감, SLA 준수를 통한 고객 만족도 제고, 비즈니스와 IT의 전략적 정렬.

## Ⅱ. ITIL 4의 특징 및 장점

- 핵심 요약 : SVS 운용 모델, SVC 6개 활동, 7대 기본 원칙, 34개 실천 관행으로 구성된 고객 중심 서비스 관리 체계.

1. **서비스 가치 시스템** (SVS, Service Value System) : 수요와 기회를 가치로 연결하는 운용 모델 → IT 운영의 목적을 고객 성과에 맞춤.
2. **서비스 가치 사슬** (SVC, Service Value Chain) : 계획·개선·참여·설계/전환·획득/구축·제공/지원의 6개 활동으로 서비스 활동을 연결 → 수요에서 가치까지의 흐름 명확화.
3. 4차원 관점 : 조직·사람, 정보·기술, 파트너·공급자, 가치 흐름·프로세스를 함께 살핌 → 한 영역만 최적화하는 오류 감소.
4. **실천 관행** (Practices) : 인시던트·문제·변경 등의 실행 기준을 제공 → 운영의 일관성 향상.
5. 지속적 개선 : 고객 경험과 운영 지표를 반복 점검 → 서비스 품질의 점진적 향상.

## Ⅲ. ITSM의 구조 (흐름)

- 핵심 요약 : SVS 안에서 수요를 가치로 전환하는 SVC 6개 활동이 흐르고, 계획과 개선이 전 활동에 걸쳐 작동하는 구조.

```text
[ 서비스 가치 시스템 (SVS) ]

기회 · 수요 (Opportunity, Demand)
       ↓
[ 서비스 가치 사슬 (SVC) ]
       ↓
가치 (Value)

※ 전 과정에 거버넌스·실천 관행·개선 적용
```

```text
[ SVC 6개 활동 흐름 ]

참여 (Engage) ── 요구 수집·수요 대응
       ↓
설계/전환 (Design & Transition)
       ↓
획득/구축 (Obtain/Build)
       ↓
제공/지원 (Deliver & Support)
       ↓
가치 (Value)
※ 계획 (Plan), 개선 (Improve)은 전 활동에 상시 적용
```

- 참여 : 이해관계자의 요구를 수집하고 수요에 대응하는 진입점.
- 설계/전환 : 품질·비용·출시 시점의 요구를 충족하도록 서비스를 설계하고 운영으로 전환.
- 획득/구축 : 합의된 사양에 맞게 서비스 구성요소를 조달·구축.
- 제공/지원 : 합의된 수준에 따라 서비스를 제공하고 지원.
- 위 흐름은 대표 경로를 단순화한 것이며, 실제 활동은 서로 다중으로 연계됨.

## Ⅳ. ITSM 핵심 운영 프로세스의 비교

- 핵심 요약 : 서비스 데스크·인시던트·문제·변경·서비스 수준 관리의 목적과 활동이 장애 대응에서 재발 방지, 변경 통제로 이어지는 구조.

```text
[ 인시던트 → 문제 관리 흐름 ]

인시던트 발생
       ↓
임시 조치 (Workaround) → 서비스 복구
       ↓
근본 원인 분석
       ↓
문제 등록 → 재발 방지 → 변경 요청
```

| 운영 프로세스 | 핵심 목적 | 주요 활동 및 특징 |
|---|---|---|
| **서비스 데스크** (Service Desk) | 사용자와 IT 간의 단일 접점 (SPOC, Single Point of Contact) 운영 | 문의·인시던트·서비스 요청 접수, 에스컬레이션 (Escalation) |
| **인시던트 관리** (Incident Management) | 서비스 중단 시 최단 시간 내 정상 서비스로 복구 | 임시 조치 (Workaround), 우선순위 분류, 긴급 복구 |
| **문제 관리** (Problem Management) | 인시던트의 근본 원인을 분석해 재발 방지 | 근본 원인 분석 (RCA, Root Cause Analysis), 알려진 오류 데이터베이스 (KEDB, Known Error Database) 등록 |
| **변경 관리** (Change Management) | 서비스 중단 위험을 줄이며 안전하게 변경 수행 | 변경 자문 위원회 (CAB, Change Advisory Board) 심의, 영향도 평가, 롤백 (Rollback) 계획 수립 |
| **서비스 수준 관리** (SLM, Service Level Management) | 고객과 합의한 서비스 품질 협약과 모니터링 | SLA·OLA (Operational Level Agreement) 체결, 서비스 달성도 측정, 개선 계획 수립 |

- ITIL 4에서는 프로세스 개념을 실천 관행으로 통칭하며, 인시던트·문제·변경 관리도 모두 실천 관행에 포함됨.

## Ⅴ. ITSM의 한계와 방안

- 핵심 요약 : 절차 과중, 도구 중심 운영, CMDB 노후화를 자동화와 단계적 정착으로 줄임.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 모든 변경에 같은 승인 절차 적용 | 저위험 변경까지 승인을 거쳐 배포 지연 | 저위험 반복 작업은 표준 변경으로 사전 승인하고 자동 증거를 연계 | 변경 리드타임 |
| 도구 중심 도입 | 도구만 들여오면 현장 활용도가 낮아짐 | 핵심 관행부터 적용하고 사용자 피드백으로 절차 개선 | 도구 활용률 |
| 동적 클라우드 자원 | 자원 변화가 빨라 **CMDB** (Configuration Management Database) 정확도 저하 | 자동 발견과 프로비저닝 이벤트로 구성 항목 갱신 | CMDB 정확도 |

## Ⅵ. ITSM에 대한 기술사적 제언

- 핵심 요약 : AI 기반 운영 자동화, DevOps 파이프라인과 변경 관리의 통합, 경험 중심 지표 고도화가 필요함.

1. **AIOps** (Artificial Intelligence for IT Operations) 기반 장애 예측 : 인프라와 애플리케이션 로그를 머신러닝으로 실시간 분석해 장애 징후를 미리 감지하고, 반복되는 인시던트는 자동 처리하는 체계를 두는 것이 바람직하다.
2. DevOps (Development and Operations) 파이프라인과 변경 관리의 통합 : 자동화 테스트를 통과한 표준 변경은 승인 대기 없이 파이프라인에서 배포하도록 절차를 단순화해야 승인 대기로 인한 릴리스 지연을 줄일 수 있다.
3. **XLA** (Experience Level Agreement, 경험 수준 협약) 중심 지표 고도화 : 가용률 같은 기술 지표 달성에 머물지 않고, 사용자가 체감하는 만족도와 업무 생산성을 측정 지표로 확대하는 것이 필요하다.

## Ⅶ. 결론

- 핵심 요약 : ITSM은 ITIL 4의 SVS·SVC를 바탕으로 IT 서비스를 가치로 전환하는 고객 중심 관리 체계이며, AIOps·DevOps·XLA 방향으로 진화.
- 시사점 : 프로세스 관료주의와 CMDB 데이터 노후화를 자동화와 파이프라인 통합으로 보완하고, XLA 중심의 사용자 체감 지표로 고도화해야 함.
