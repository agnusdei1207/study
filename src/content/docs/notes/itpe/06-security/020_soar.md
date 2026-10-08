---
title: "SOAR(Security Orchestration, Automation and Response)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. SOAR(보안 오케스트레이션·자동화·대응)의 개요

- 개념 : 다양한 이기종 보안 솔루션(SIEM(Security Information and Event Management), EDR(Endpoint Detection and Response), 방화벽, CTI(Cyber Threat Intelligence) 등)의 경보와 대응 도구를 단일 워크플로우로 **연계** (Orchestration)하고, 사전 정의된 **표준 대응 절차** (Playbook)에 따라 침해사고를 사람의 개입 없이 자동으로 **분석·차단·대응** (Automation & Response)하는 보안 관제 플랫폼.
- 배경 및 필요성 : 하루 대량으로 발생하는 보안 경보로 인한 **보안관제센터** (SOC, Security Operations Center)의 **경보 피로** (Alert Fatigue), 보안 전문 인력 부족, 수작업 대응으로 인한 **평균 침해 대응 시간** (MTTD/MTTR(Mean Time to Repair)) 지연을 극복하기 위해 도입.
- 핵심 목적 : 보안 운영(SecOps) 효율성 극대화, 침해사고 탐지부터 격리까지의 MTTR 단축(분/초 단위), 관제 업무 표준화 및 일관된 대응 품질 확보.

## Ⅱ. SOAR(보안 오케스트레이션·자동화·대응)의 핵심 아키텍처 및 동작 메커니즘

SOAR(Security Orchestration, Automation and Response)는 SIEM 등에서 유입된 경보를 정규화하고, CTI 위협 평판 조회를 거친 뒤 플레이북 엔진을 통해 방화벽 IP(Internet Protocol) 차단, 단말 격리, 티켓 생성을 자동으로 수행함.

```text
[ SOAR 기반 보안 관제 자동화 대응 라이프사이클 ]

  [ 이종 보안 로그 소스 (SIEM, EDR, WAF, 클라우드 감사로그) ]
                               │
                               ▼ 1. 인시던트 인입 및 정규화
  +-------------------------------------------------------------+
  | SOAR 오케스트레이션 엔진 (Security Orchestration Engine)     |
  |  - 위협 인텔리전스(CTI) 평판 조회 (VirusTotal, MISP 자동 연동) |
  |  - 위험 점수 산정 및 경보 중복 제거                         |
  +------------------------------┬------------------------------+
                                 │ 2. 플레이북(Playbook) 매핑
                                 ▼
  +-------------------------------------------------------------+
  | 자동화 워크플로우 실행 (Playbook Engine)                    |
  |  - Level 1: 악성 IP/도메인 방화벽 정책 자동 등록 (차단)       |
  |  - Level 2: EDR을 통한 감염 PC 네트워크 격리 및 메모리 덤프  |
  |  - Level 3: 사용자 악성 메일 계정 패스워드 리셋 및 메일 삭제 |
  +------------------------------┬------------------------------+
                                 │ 3. 휴먼 승인 및 사후 관리
                                 ▼
  [ IT 서비스 관리 연동 (Jira, ServiceNow 티켓 자동 생성 및 종결) ]
```

- **보안 오케스트레이션** (Security Orchestration) : API(Application Programming Interface), 웹훅, CLI(Command-Line Interface)를 통해 방화벽, 메일 서버, EDR, 액티브 디렉터리 등 서로 다른 솔루션을 하나의 파이프라인으로 연결.
- **플레이북** (Playbook) 기반 자동화 : 피싱 메일 대응, 악성코드 감염, 랜섬웨어 확산 등 사고 유형별로 **표준운영절차** (SOP, Standard Operating Procedure)를 그래픽 워크플로우 코드로 구현.
- **자동화된 대응** (Automated Response) : **위협 지표** (IoC)의 평판이 임계치를 초과할 경우 사람의 개입 없이 방화벽 룰 추가 및 감염 단말을 초 단위로 즉시 차단.
- **케이스 관리 및 협업** (Case Management) : 모든 수집 증적, 대응 이력, 담당자 메모를 단일 케이스에 중앙 집중화하여 법적 증적 및 감사 이력 보존.

## Ⅲ. SOAR(보안 오케스트레이션·자동화·대응)의 세부 구성 요소 및 비교 분석

| 비교 항목 | SIEM (Security Information and Event Management) | CTI (Cyber Threat Intelligence) | SOAR (Security Orchestration, Automation and Response) |
| --- | --- | --- | --- |
| 주요 역할 | 전사 대용량 로그 수집 및 상관분석 탐지 | 외부 위협 정보(IoC, 공격자 TTPs) 제공 | 경보 분석, 도구 연계 오케스트레이션 및 대응 |
| 핵심 산출물 | 상관분석 알람, 보안 대시보드 | 위협 지표 피드 (STIX/TAXII, IP/도메인 평판) | 자동 차단 정책 실행, 인시던트 티켓 종결 |
| 대응 자동화 | 제한적 (경보 발송 및 단순 스크립트) | 없음 (정보 제공에 집중) | 고도화된 플레이북 기반 전주기 자동 차단 |
| 인력 의존도 | 보안 분석가의 수작업 분석 필수 | 위협 사냥(Threat Hunting) 인력 필요 | 반복적 L1/L2 관제 업무의 무인 자동화 |
| 상호 관계 | SOAR에 경보(Alert)를 제공하는 입력 소스 | SOAR 플레이북의 판단 기준 데이터 제공 | SIEM 경보와 CTI를 결합하여 최종 대응 수행 |

- SIEM이 '상황을 인지하고 알리는 눈'이고 CTI가 '적의 정보를 알려주는 지식'이라면, SOAR는 이를 종합하여 '즉각 무기를 휘둘러 위협을 격퇴하는 손과 발'에 해당함.

## Ⅳ. SOAR(보안 오케스트레이션·자동화·대응)의 주요 한계점 및 해결 방안

- **오탐** (False Positive)에 기반한 과도한 자동 차단으로 인한 비즈니스 중단 :
  - 한계점 : 정상적인 결제 게이트웨이나 핵심 협력사 IP가 CTI 오탐으로 악성으로 분류되어 방화벽에서 자동 차단될 경우 대규모 서비스 장애 유발.
  - 해결 방안 : 핵심 인프라 및 화이트리스트 사전 등록, 차단 전 **Human-in-the-Loop** (HITL, Human in the Loop) 분석가 승인 단계를 플레이북 조건 분기로 구성.
- 이기종 솔루션 API 변경에 따른 플레이북 오류 및 유지보수 비용 증가 :
  - 한계점 : 연동된 상용 방화벽, EDR 솔루션의 버전 업그레이드로 API 스펙이 변경될 때 플레이북 스크립트가 중단되는 커넥터 의존성 문제.
  - 해결 방안 : OpenDXL, STIX-Shifter 등 보안 오케스트레이션 오픈 표준 프로토콜을 채택하고, 모듈화된 컨테이너 기반 앱 커넥터 아키텍처 적용.
- 조직 내 표준운영절차(SOP) 미비로 인한 플레이북 제작 난항 :
  - 한계점 : 사고 대응 프로세스가 문서화되어 있지 않거나 담당자마다 대응 방식이 상이하여 코드로 자동화하지 못하고 프로젝트 좌초.
  - 해결 방안 : **NIST(National Institute of Standards and Technology) SP 800-61** 침해사고 대응 가이드를 바탕으로 전사 SOP를 표준화하고, 단순 반복 업무(피싱 메일 분석 등)부터 단계적으로 자동화 범위 확장.

## Ⅴ. SOAR(보안 오케스트레이션·자동화·대응) 적용 및 발전을 위한 기술사적 제언

- 생성형 AI(Artificial Intelligence) 기반 플레이북 보조 및 자율 에이전트 연동 : 보안 경보 분석 시 LLM(Large Language Model) 에이전트를 결합하여 공격 요약, 역공학 스크립트 생성, 플레이북 코드 작성을 지원하는 SecOps AI 도입.
- **MTTR** 및 자동화 비율을 핵심 KPI(Key Performance Indicator)로 설정 : 침해 발생부터 격리까지의 시간(MTTR 지속 단축)과 L1 단순 경보의 높은 비율 무인 자동화 처리를 조직 목표로 관리.
- 공격표면관리(ASM) 및 침해모의평가(BAS)와의 폐루프 연동 : 발견된 외부 노출 취약점에 대해 SOAR 플레이북이 즉시 임시 방화벽 룰을 적용하고 가상 패치를 배포하는 선제적 자동화 체계 구축.
