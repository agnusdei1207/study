---
title: "지속적 위협 노출 관리(CTEM, Continuous Threat Exposure Management)"
author: "agnusdei1207"
date: "2026-10-24T22:56:33+09:00"
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

- 지속적 위협 노출 관리(CTEM), 공격 표면(Attack Surface), 악용 가능성(Exploitability), 노출 수준
- 공격표면관리(ASM), CAASM(Cyber Asset Attack Surface Management), 침해·공격 시뮬레이션(BAS), 가상 패칭(Virtual Patching)
- EPSS(Exploit Prediction Scoring System), CVSS(Common Vulnerability Scoring System), CSPM(Cloud Security Posture Management), 초크 포인트(Choke Point)

## Ⅰ. 지속적 위협 노출 관리(CTEM)의 개요

- 핵심 요약 : 취약점을 찾는 데서 그치지 않고 실제 악용 가능성과 비즈니스 영향을 검증해 우선순위를 정하고 상시 줄이는 순환형 보안 관리 프레임워크.
- 개념 : 공격 표면 전반의 취약점, 설정 오류, 자격증명 노출 등을 식별하고, 공격자의 실제 **악용 가능성** (Exploitability)과 비즈니스 영향도를 검증하여 우선순위화하고 지속적으로 완화하는 5단계 순환형 프레임워크인 **지속적 위협 노출 관리** (CTEM, Continuous Threat Exposure Management).
- 배경 및 필요성 : 매년 수많은 CVE(Common Vulnerabilities and Exposures) 취약점이 공개되어 모든 결함을 패치할 수 없으므로, 실제로 침투 가능한 경로만 집중 대응해야 한다는 요구에서 등장. 가트너(Gartner)가 핵심 보안 트렌드로 제시함.
- 주요 목적 : 취약점 조치의 우선순위 최적화, 보안 경보 피로(Alert Fatigue) 해소, 공격 노출 수준의 지속적 축소.

## Ⅱ. 지속적 위협 노출 관리(CTEM)의 특징 및 장점

- 핵심 요약 : 발견과 검증을 분리해 실제로 악용 가능한 소수의 경로에 조치를 모으므로, 제한된 자원으로 위험을 더 크게 줄임.

1. 범위 기반 관리 : 모든 자산 대신 비즈니스 가치가 높은 인프라, SaaS(Software as a Service), 공급망 파트너를 관리 범위로 설정 → 관리 부담을 핵심 영역에 집중.
2. 악용 가능성 중심 우선순위 : **EPSS** (Exploit Prediction Scoring System)와 CTI(Cyber Threat Intelligence)를 CVSS(Common Vulnerability Scoring System) 점수와 결합 → 실제 공격이 예상되는 취약점이 먼저 처리됨.
3. 실증 기반 검증 : **침해·공격 시뮬레이션** (BAS, Breach and Attack Simulation)으로 공격 경로가 실제로 뚫리는지 확인 → 추측이 아닌 근거에 따른 조치.
4. 폐루프 반복 : 조치 결과를 다시 발견 단계로 환류 → 노출 수준이 시간에 따라 줄어듦.

```text
[ CTEM 5단계 순환 프레임워크 ]

1. 범위 설정 (Scoping)
        ↓
2. 발견 (Discovery)
        ↓
3. 우선순위화 (Prioritization)
        ↓
4. 유효성 검증 (Validation)
        ↓
5. 조치 동원 (Mobilization)
        ↓ 결과를 다시 1단계로 환류
```

## Ⅲ. 지속적 위협 노출 관리(CTEM)의 구성 요소 및 흐름

- 핵심 요약 : 발견된 노출 자산을 CVSS 심각도, EPSS 악용 확률, 공격 경로 분석으로 걸러내는 우선순위화 흐름이 핵심.

```text
[ 우선순위화 흐름 ]

발견된 취약점 목록
        ↓
CVSS 심각도 점수 확인
        ↓
EPSS 악용 확률·CTI 결합
        ↓
공격 경로 연결 여부 판정
        ↓
실제 침투 가능한 소수 항목 선별
```

- 범위 설정 (Scoping) : 핵심 자산, SaaS, 공급망 파트너를 관리 범위로 정의.
- 발견 (Discovery) : 외부 공격 표면 관리(EASM, External Attack Surface Management), CAASM(Cyber Asset Attack Surface Management), 취약점 스캐너로 미관리 노출 자산을 전수 발굴.
- 우선순위화 (Prioritization) : CVSS 점수에 EPSS와 CTI를 결합해 실제 침해 가능성이 높은 항목을 선별.
- 유효성 검증 (Validation) : BAS와 자동화된 침투 테스트로 공격자가 방어를 실제로 뚫을 수 있는지 실증.
- 조치 동원 (Mobilization) : 보안팀과 IT 개발·운영팀이 패치, 가상 패칭, 세그멘테이션 격리를 함께 실행.

## Ⅳ. 지속적 위협 노출 관리(CTEM)의 비교 분석

- 핵심 요약 : 취약점 목록 중심의 관리에서 검증된 고위험 경로 중심의 관리로 옮겨 가는 것이 CTEM의 차별점.

| 비교 항목 | 전통적 취약점 관리 (VM, Vulnerability Management) | 공격표면관리 (ASM, Attack Surface Management) | 지속적 위협 노출 관리 (CTEM) |
| --- | --- | --- | --- |
| 관리 범위 | 내부 서버와 소프트웨어 취약점 | 인터넷에 노출된 외부 자산과 포트 | 내·외부 자산, SaaS, 클라우드, 계정 권한 |
| 평가 기준 | 심각도 점수 중심 | 외부 노출 여부 | 악용 가능성, 공격 경로, 비즈니스 가치 |
| 검증 방식 | 스캐너 기반 시그니처 매칭 | 외부 프로빙 | BAS 기반 실효성 검증 |
| 수행 주기 | 분기 또는 연간 진단 | 지속적 외부 스캔 | 상시 순환 운영 |
| 최종 산출물 | 취약점 나열 보고서 | 외부 노출 자산 목록 | 검증된 고위험 경로의 완화 조치 |

- 전통적 취약점 관리가 패치할 결함의 목록을 끝없이 제시했다면, CTEM은 지금 공격자가 뚫고 들어올 수 있는 소수의 경로를 검증해 집중 해결하도록 이끎.

## Ⅴ. 지속적 위협 노출 관리(CTEM)의 한계와 방안

- 핵심 요약 : 보안팀과 운영팀의 조치 병목, 공격 경로 연산 부담, 검증 도구의 운영 간섭이 주요 한계이며 업무 도구 연동, 그래프 기반 분석, 안전 모드 검증으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 조치 병목 | 우선순위가 정해져도 운영 안정성 우려와 개발 일정 충돌로 패치가 지연 | 티켓 관리 도구와 API로 연동하고, 미조치 시 경영진 승인 예외 처리 절차 수립 | 우선순위 항목 조치 완료율 |
| 공격 경로 연산 부담 | 멀티 클라우드와 다수 엔드포인트에서 잠재 경로가 급증해 분석 성능 저하 | 그래프 데이터베이스 기반 CSPM(Cloud Security Posture Management)과 초크 포인트 중심의 경로 압축 적용 | 경로 분석 소요 시간 |
| 검증 도구의 운영 간섭 | 자동화 공격 도구가 운영 데이터베이스에 비정상 질의를 보내 장애 위험 | 검증된 BAS 프레임워크 사용, 페이로드를 실행하지 않고 통과 여부만 확인하는 안전 모드 | 검증 중 서비스 장애 건수 |

## Ⅵ. 지속적 위협 노출 관리(CTEM)에 대한 기술사적 제언

- 핵심 요약 : 정적 점수 대신 악용 확률을 기준으로 삼고, 보안과 운영이 함께 조치를 결정하는 거버넌스를 세워야 함.

1. 정적 CVSS 점수 대신 향후 30일 안에 실제 악용될 확률을 추정하는 EPSS를 패치 우선순위의 보조 기준으로 도입하는 것이 바람직함.
2. 보안팀, 클라우드 엔지니어링팀, 인프라 운영팀이 정기적으로 합동 회의를 열어 검증된 상위 노출 위험을 일괄 조치하는 협의체를 구성하는 것이 필요함.
3. 코드 수정과 재배포에 시간이 걸리는 경우에는 WAF(Web Application Firewall), API(Application Programming Interface) 게이트웨이, EDR(Endpoint Detection and Response)에서 가상 패칭 규칙을 먼저 적용하는 절차를 표준화하는 것이 필요함.

## Ⅶ. 결론

- 핵심 요약 : CTEM은 모든 취약점을 막는 대신 실제로 뚫리는 경로를 찾아 상시 줄이는 관리 체계.
- 시사점 : 발견, 우선순위, 검증, 조치가 한 순환으로 연결될 때 보안 투자가 공격 노출 감소로 이어짐.
