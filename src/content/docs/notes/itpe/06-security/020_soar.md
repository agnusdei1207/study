---
title: "SOAR(Security Orchestration, Automation and Response)"
author: "agnusdei1207"
date: "2026-10-24T22:57:27+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- SOAR(Security Orchestration, Automation and Response), 보안 오케스트레이션(Security Orchestration)
- 플레이북(Playbook), 자동 대응(Automated Response), 케이스 관리(Case Management)
- SIEM, EDR, CTI, 위협 지표(IoC), 표준운영절차(SOP)
- MTTR, MTTD, HITL, STIX/TAXII, NIST SP 800-61, ASM

## Ⅰ. SOAR(보안 오케스트레이션·자동화·대응)의 개요

- 핵심 요약 : 이기종 보안 도구의 경보를 하나의 워크플로우로 묶어 침해사고 대응을 자동화하는 보안 관제 플랫폼.
- 개념 : SIEM(Security Information and Event Management), EDR(Endpoint Detection and Response), 방화벽, CTI(Cyber Threat Intelligence) 등 이기종 보안 솔루션을 하나의 흐름으로 잇는 **보안 오케스트레이션** (Security Orchestration)과, 사전에 정의된 **플레이북** (Playbook)에 따라 사고를 분석·차단·대응하는 **자동 대응** (Automated Response)을 결합한 관제 플랫폼.
- 배경 및 필요성 : 하루 대량의 보안 경보로 인한 보안관제센터(SOC, Security Operations Center)의 경보 피로, 보안 인력 부족, 수작업 대응 지연이 겹쳐 평균 탐지 시간(MTTD, Mean Time to Detect)과 평균 복구 시간(MTTR, Mean Time to Repair)이 길어지므로 도입이 요구됨.
- 주요 목적 : 보안 운영 효율을 높이고, 탐지부터 격리까지 걸리는 시간을 줄이며, 관제 업무를 표준화해 대응 품질을 일정하게 유지하는 것.

## Ⅱ. SOAR(보안 오케스트레이션·자동화·대응)의 특징 및 장점

- 핵심 요약 : 연계, 표준화, 자동 차단, 증적 집중이 결합되어 반복 관제 업무의 처리 속도와 일관성을 높이는 구조.

1. 도구 연계 : API(Application Programming Interface), 웹훅, CLI(Command-Line Interface)로 방화벽, 메일 서버, EDR, 액티브 디렉터리를 하나의 파이프라인으로 연결 → 도구 간 수작업 전달 제거.
2. 절차 표준화 : 피싱 메일, 악성코드 감염, 랜섬웨어 확산 등 사고 유형별 **표준운영절차** (SOP, Standard Operating Procedure)를 워크플로우로 구현 → 담당자에 따른 대응 편차 감소.
3. 자동 차단 : **위협 지표** (IoC, Indicator of Compromise)의 평판이 임계치를 넘으면 사람의 개입 없이 방화벽 정책을 추가하고 감염 단말을 격리 → 확산 전 초기 차단.
4. **케이스 관리** (Case Management) : 수집 증적, 대응 이력, 담당자 메모를 단일 케이스에 모아 법적 증적과 감사 이력을 보존 → 사후 분석 근거 확보.

## Ⅲ. SOAR(보안 오케스트레이션·자동화·대응)의 구조 (흐름)

- 핵심 요약 : 경보 정규화와 평판 검증을 거쳐 플레이북이 단계별로 대응을 실행하는 파이프라인 구조.

```text
[ SOAR 대응 라이프사이클 ]

이종 보안 로그 (SIEM, EDR, 방화벽)
        ↓ 인입 및 정규화
오케스트레이션 엔진
  CTI 평판 조회, 경보 중복 제거
        ↓ 플레이북 매핑
플레이북 엔진 (자동 대응)
        ↓ 휴먼 승인
티켓 생성·종결 (IT 서비스 관리 연동)
```

```text
[ 플레이북 단계별 자동화 수준 ]

1단계: 악성 주소·도메인 차단 (방화벽)
        ↓
2단계: 감염 단말 격리, 메모리 수집 (EDR)
        ↓
3단계: 계정 비밀번호 재설정, 악성 메일 삭제
```

- 1단계와 2단계는 자동 실행하고, 계정 변경처럼 업무 영향이 큰 3단계는 승인 분기를 거치도록 구성하는 것이 일반적인 설계 방향이다.

## Ⅳ. SOAR(보안 오케스트레이션·자동화·대응)와 SIEM·CTI의 비교

- 핵심 요약 : SIEM은 경보를, CTI는 위협 정보를 제공하고, SOAR는 이를 결합해 대응을 실행하는 역할 분담.

| 비교 항목 | SIEM (Security Information and Event Management) | CTI (Cyber Threat Intelligence) | SOAR |
| --- | --- | --- | --- |
| 주요 역할 | 전사 로그 수집과 상관분석 탐지 | 외부 위협 정보, 공격자의 전술과 기법 제공 | 경보 분석, 도구 연계, 대응 실행 |
| 핵심 산출물 | 상관분석 경보, 보안 대시보드 | 위협 지표 피드 (표준 교환 규격 사용) | 자동 차단 정책 실행, 인시던트 티켓 종결 |
| 대응 자동화 | 제한적 (경보 발송, 단순 스크립트) | 없음 (정보 제공에 집중) | 플레이북 기반 전 주기 자동 차단 |
| 인력 의존도 | 분석가의 수작업 분석 필요 | 위협 사냥 인력 필요 | 반복적인 1·2차 관제 업무 자동화 |
| 상호 관계 | SOAR에 경보를 제공하는 입력 소스 | SOAR 플레이북의 판단 기준 데이터 | SIEM 경보와 CTI를 결합해 최종 대응 |

- SIEM은 상황을 알리는 눈, CTI는 적을 설명하는 지식, SOAR는 이를 종합해 실제로 조치하는 손에 해당함.

## Ⅴ. SOAR(보안 오케스트레이션·자동화·대응)의 한계와 방안

- 핵심 요약 : 오탐에 의한 과잉 차단, 연동 API 변경, 표준 절차 부재를 승인 분기, 표준 규격, 절차 표준화로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 오탐에 따른 과잉 자동 차단 | 정상 결제 게이트웨이나 협력사 IP가 오탐으로 차단되어 서비스 장애 유발 | 핵심 인프라를 화이트리스트에 등록하고, 차단 전 **HITL** (Human in the Loop) 분석가 승인 단계를 플레이북 분기로 구성 | 오탐 차단 건수, 승인 대기 시간 |
| 연동 API 변경 | 상용 방화벽과 EDR 업그레이드로 API 스펙이 바뀌면 플레이북 커넥터가 중단됨 | **STIX** (Structured Threat Information eXpression)·**TAXII** (Trusted Automated eXchange of Intelligence Information) 등 표준 규격을 채택하고 커넥터를 모듈화 | 커넥터 장애 건수, 플레이북 중단 시간 |
| 표준 절차 부재 | 사고 대응 절차가 문서화되지 않거나 담당자마다 달라 코드로 옮기지 못하고 프로젝트가 중단됨 | NIST(National Institute of Standards and Technology)의 **SP 800-61** 침해사고 대응 가이드를 기준으로 전사 SOP를 표준화하고, 반복이 많은 피싱 메일 분석부터 자동화 범위 확대 | 플레이북 적용 사고 유형 수, 수작업 비율 |

## Ⅵ. SOAR(보안 오케스트레이션·자동화·대응)에 대한 기술사적 제언

- 핵심 요약 : 생성형 AI 보조, 대응 지표 관리, 노출 자산 연동을 SOAR 고도화의 방향으로 제시.

1. 생성형 AI 보조 도입 : 경보 분석 때 LLM(Large Language Model) 에이전트가 공격 요약과 플레이북 초안을 만들고 분석가가 검증하는 방식으로 도입하는 것이 바람직하다.
2. 대응 지표 관리 : 탐지부터 격리까지의 MTTR 감소와 단순 경보의 무인 처리 비율을 핵심 **KPI** (Key Performance Indicator, 핵심 성과 지표)로 관리하는 것이 필요하다.
3. 노출 자산 연동 : **ASM** (Attack Surface Management, 공격표면 관리)에서 발견된 외부 노출 취약점을 플레이북이 받아 임시 방화벽 정책을 적용하고, 가상 패치 배포까지 잇는 폐루프 체계를 구축하는 것이 좋다.

## Ⅶ. 결론

- 핵심 요약 : SOAR는 SIEM의 경보와 CTI의 지식을 플레이북으로 묶어 반복 대응을 자동화하는 보안 관제 플랫폼.
- 시사점 : 자동화 범위는 오탐 통제와 승인 체계를 전제로 단계적으로 넓혀야 대응 속도와 안정성을 함께 얻을 수 있다.
