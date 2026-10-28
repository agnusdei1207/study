---
title: "NIST CSF 2.0 (Govern 기능) (NIST: National Institute of Standards and Technology; CSF: Cybersecurity Framework)"
author: "agnusdei1207"
date: "2026-10-24T22:55:16+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "039"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- NIST CSF 2.0, 거버넌스(GV, Govern), 위험 선호도(Risk Appetite), 이사회 감독, 사이버 회복탄력성(Cyber Resilience)
- 공급망 위험 관리(C-SCRM), SBOM, 서드파티 위험 관리(TPRM), 위험 정량화(FAIR)
- 비즈니스 연속성 계획(BCP), 평균 복구 시간(MTTR), 복구 시점 목표(RPO), CISO

## Ⅰ. NIST CSF 2.0 및 거버넌스(Govern) 기능의 개요

- 핵심 요약 : 기존 5대 기능 위에 전사 의사결정과 정책을 총괄하는 거버넌스 기능을 최상위 축으로 추가한 사이버 위험 관리 표준.
- 개념 : 미국 **국립표준기술원** (NIST, National Institute of Standards and Technology)이 제정한 **사이버보안 프레임워크** (CSF, Cybersecurity Framework)의 2.0 버전으로, 기존 5대 기능에 **거버넌스** (Govern, GV) 기능을 최상위 축으로 신설한 개정 체계.
- 배경 및 필요성 : 보안이 IT(Information Technology) 실무의 기술적 방어에 머무르면 경영진의 의사결정 및 비즈니스 리스크와 괴리되므로, 공급망 위험과 이사회 수준의 책임을 체계에 반영할 필요가 생김.
- 주요 목적 : 비즈니스 전략과 사이버 위험 관리를 일체화하고, 이사회와 경영진 수준의 거버넌스를 확립하며, 6대 기능으로 **사이버 회복탄력성** (Cyber Resilience)을 구축.

## Ⅱ. NIST CSF 2.0 및 거버넌스(Govern) 기능의 특징 및 장점

- 핵심 요약 : 거버넌스를 최상위에 둔 6대 기능 구조로, 기술 대응을 경영 판단과 예산에 연결하는 것이 핵심 특징.

1. 거버넌스 (GV, Govern) : 조직 맥락과 위험 선호도(Risk Appetite)를 정하고 역할, 정책, 공급망 위험을 관리 → 기술 기능의 방향과 예산을 통제.
2. 식별 (ID, Identify) : 자산, 공급망 파트너, 위험과 취약점을 전사 차원에서 가시화 → 보호 대상의 범위 확정.
3. 보호 (PR, Protect) : **신원 및 접근 관리** (IAM, Identity and Access Management)와 데이터 보안으로 공격 표면 축소.
4. 탐지 (DE, Detect) : **보안 정보 및 이벤트 관리** (SIEM, Security Information and Event Management)과 EDR(Endpoint Detection and Response)로 비인가 접근을 실시간 감지.
5. 대응 (RS, Respond) : 침해 시 통제된 절차에 따라 시스템을 격리하고 피해 확산을 차단하며 이해관계자와 소통.
6. 복구 (RC, Recover) : **비즈니스 연속성 계획** (BCP, Business Continuity Plan)에 따라 정상 상태로 회복하고 교훈을 반영.

## Ⅲ. NIST CSF 2.0 및 거버넌스(Govern) 기능의 구조 (흐름)

- 핵심 요약 : 거버넌스가 나머지 5대 기능의 방향을 정하고, 사고의 교훈이 다시 거버넌스로 환류되는 순환 구조.

```text
[ CSF 2.0 6대 기능의 흐름 ]

GV 거버넌스 (Govern)
          ↓ 정책과 위험 지침 하달
ID 식별 (Identify)
          ↓
PR 보호 (Protect)
          ↓
DE 탐지 (Detect)
          ↓
RS 대응 (Respond)
          ↓
RC 복구 (Recover)
          ↑ 교훈 환류
GV 거버넌스 (재평가)
```

```text
[ 거버넌스의 통제 관계 ]

GV 거버넌스 (Govern)
          ↓ 전략, 정책, 위험 선호도 하달
ID, PR, DE, RS, RC 5대 기능
          ↓ 결과와 사고 교훈 보고
GV 거버넌스 (재평가)
```

## Ⅳ. NIST CSF 2.0 및 거버넌스(Govern) 기능의 비교

- 핵심 요약 : CSF 2.0은 적용 대상을 넓히고 공급망과 경영진 책임을 독립 항목으로 격상하여, 1.1 대비 보안의 무게 중심을 경영 쪽으로 옮김.

| 비교 항목 | NIST CSF 1.1 | NIST CSF 2.0 |
| --- | --- | --- |
| 기본 구조 | 5대 기능 (ID, PR, DE, RS, RC) | 6대 기능 (GV 추가) |
| 적용 대상 | 주로 중요 기반시설 중심 | 규모와 산업에 관계없이 쓰는 범용 프레임워크 |
| 공급망 위험 | 식별 기능의 하위 범주 | 거버넌스의 독립 범주로 격상 |
| 경영진 책임 | 실무 조직 중심 서술 | 경영진과 이사회의 감독 책임 강조 |
| 프로파일 | 현재와 목표 프로파일 | 조직 프로파일과 커뮤니티 프로파일 |

- CSF 2.0은 보안을 기술 엔지니어링에서 경영 거버넌스의 영역으로 끌어올린 개정으로, 경영진의 의사결정과 예산 배분이 뒷받침되지 않으면 5대 기술 기능이 실효성을 갖기 어려움을 전제함.

## Ⅴ. NIST CSF 2.0 및 거버넌스(Govern) 기능의 한계와 방안

- 핵심 요약 : 중소기업의 거버넌스 역량 부족, 기술 지표와 경영 언어의 단절, 공급망 통제의 강제력 한계가 주요 과제이며 단계적 내재화와 위험의 금액 환산으로 대응해야 함.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 중소기업의 거버넌스 자원 부족 | 전담 CISO(Chief Information Security Officer)나 보안위원회를 두기 어려워 거버넌스 요건이 실행되지 않음 | 규모에 맞춘 최소 거버넌스 체계를 세우고, 외부 가상 CISO(vCISO, virtual CISO)와 협력해 단계적으로 내재화 | 거버넌스 정책 문서 보유율 |
| 기술 지표와 경영 언어의 단절 | CVSS(Common Vulnerability Scoring System) 점수를 경영진이 손실 금액으로 이해하지 못해 예산 확보가 어려움 | 위험 정량 분석 모델(FAIR, Factor Analysis of Information Risk)을 연계해 위험을 예상 손실액으로 환산하여 보고 | 금액으로 환산된 위험 항목 수 |
| 공급망 통제의 강제력 한계 | 협력사와 해외 SaaS(Software as a Service) 공급자를 감사하거나 준수를 강제할 권한이 부족 | 계약서에 보안 평가 기준과 SBOM(Software Bill of Materials) 제출을 명시하고, 서드파티 위험 관리(TPRM, Third-Party Risk Management) 플랫폼으로 지속 평가 | 보안 평가 완료 공급사 비율 |

## Ⅵ. NIST CSF 2.0 및 거버넌스(Govern) 기능에 대한 기술사적 제언

- 핵심 요약 : 보안 기준을 경영 계획과 예산 체계에 묶고, 공급망과 복원력을 이사회 지표로 관리하는 방향.
- 국내 ISMS(Information Security Management System) 인증 체계를 준비할 때 CSF 2.0의 거버넌스 항목을 함께 매핑하면, 국내 인증과 국제 프레임워크를 하나의 관리 체계로 운영할 수 있다.
- 조달과 구매 과정에 보안 검증을 의무로 넣고, 협력사 소프트웨어를 납품할 때 SBOM 제출을 조건으로 두는 공급망 거버넌스가 필요하다.
- 방어율 중심의 지표에서 벗어나, 사고 후 정상 업무로 돌아가는 데 걸리는 평균 복구 시간(MTTR, Mean Time to Recovery)과 복구 시점 목표(RPO, Recovery Point Objective)를 이사회 핵심 지표로 관리하는 전환이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : CSF 2.0의 핵심은 보안을 기술 실무에서 경영 거버넌스의 과제로 끌어올린 것임.
- 거버넌스가 예산과 책임을 확보할 때 5대 기술 기능이 실효성을 가짐.
