---
title: "클라우드 서비스 보안"
author: "agnusdei1207"
date: "2026-10-24T23:07:38+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "126"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 클라우드 서비스 보안(Cloud Service Security), IaaS(Infrastructure as a Service), PaaS(Platform as a Service), SaaS(Software as a Service)
- 책임 공유 모델(Shared Responsibility Model), CSP(Cloud Service Provider), CSC(Cloud Service Customer), CSPM(Cloud Security Posture Management)
- CWPP(Cloud Workload Protection Platform), CIEM(Cloud Infrastructure Entitlement Management), CNAPP(Cloud Native Application Protection Platform), CASB(Cloud Access Security Broker)
- 설정 오류(Misconfiguration), 멀티 테넌시(Multi-tenancy), IaC(Infrastructure as Code)

## Ⅰ. 클라우드 서비스 보안의 개요

- 핵심 요약 : 클라우드 서비스 제공자와 이용자가 보안 책임을 나누어 맡는 전제 위에서, 데이터와 인프라를 보호하는 통합 정보보호 체계.
- 개념 : IaaS(Infrastructure as a Service), PaaS(Platform as a Service), SaaS(Software as a Service) 도입과 운영에서 데이터, 애플리케이션, 인프라를 위협과 규제 위반으로부터 보호하기 위해, **클라우드 서비스 제공자** (CSP, Cloud Service Provider)와 이용자(CSC, Cloud Service Customer)가 책임을 나누는 **책임 공유 모델** (Shared Responsibility Model)에 기반하여 수립하는 보안 체계.
- 배경 및 필요성 : 기업의 디지털 전환(DX, Digital Transformation)으로 워크로드가 멀티·하이브리드 클라우드로 옮겨갔으나, 설정 오류와 계정 권한 남용에 따른 데이터 침해가 빈발함.
- 주요 목적 : 클라우드의 탄력성을 유지하면서 데이터 주권을 확보하고, 멀티 테넌시 환경의 데이터 격리와 CSAP(Cloud Security Assurance Program), FedRAMP(Federal Risk and Authorization Management Program), ISMS-P(정보보호 및 개인정보보호 관리체계) 같은 규제 준수를 충족하는 것.

## Ⅱ. 클라우드 서비스 보안의 특징 및 장점

- 핵심 요약 : 책임 경계를 명확히 나누고 설정과 권한을 상시 점검하는 도구가 결합되어, 클라우드 확장성과 보안 통제를 동시에 얻는 구조.

1. 책임 공유 : 물리 인프라와 하이퍼바이저는 CSP가, 데이터와 운영체제(OS, Operating System) 패치, 접근 권한은 CSC가 맡음 → 책임 공백에 따른 방치를 줄임.
2. **CSPM** (Cloud Security Posture Management, 클라우드 설정 상태 상시 점검) : 공개 저장소와 보안 그룹 설정 오류를 자동 탐지하고 치료 → 설정 오류에 따른 침해 가능성 축소.
3. **CWPP** (Cloud Workload Protection Platform, 가상 머신(VM, Virtual Machine)·컨테이너·서버리스 보호) : 실행 중 워크로드의 이상 행위와 취약점을 점검 → 런타임 공격의 조기 탐지.
4. **CIEM** (Cloud Infrastructure Entitlement Management, 클라우드 권한 관리) : 과잉 권한과 비활성 계정을 분석해 최소 권한을 적용 → 권한 상승 경로 차단.

## Ⅲ. 클라우드 서비스 보안의 구조 (흐름)

- 핵심 요약 : 서비스 모델에 따라 이용자의 관리 범위가 달라지며, 데이터와 신원은 모든 모델에서 이용자 책임으로 남는 구조.

```text
[ 책임 공유 범위 (요약) ]

구분           IaaS    PaaS    SaaS
데이터·신원     이용자  이용자  이용자
애플리케이션    이용자  이용자  제공자
런타임·OS      이용자  제공자  제공자
가상화·물리층   제공자  제공자  제공자
```

```text
[ 보안 도구의 적용 계층 ]

설정 상태 (클라우드 자원)
   ↓ CSPM
워크로드 실행 (VM·컨테이너·서버리스)
   ↓ CWPP
신원과 권한 (IAM 계정)
   ↓ CIEM
```

## Ⅳ. 클라우드 서비스 모델별 보안의 비교

- 핵심 요약 : IaaS는 제어 범위가 넓은 만큼 책임도 크고, SaaS는 제어가 좁아 계정 관리와 제공자 인증 검토가 핵심이 되는 구조.

| 비교 항목 | IaaS 보안 | PaaS 보안 | SaaS 보안 |
| --- | --- | --- | --- |
| 이용자 관리 범위 | OS, 네트워크 서브넷, 보안 그룹, 데이터 | 애플리케이션 코드, API(Application Programming Interface) 키, 데이터 | 사용자 계정, 권한, 데이터 |
| 핵심 보안 기술 | 가상 방화벽, 호스트 침입 탐지(HIDS, Host-based Intrusion Detection System), EDR(Endpoint Detection and Response) | 시큐어 코딩, API 게이트웨이, WAF(Web Application Firewall) | CASB(Cloud Access Security Broker), 데이터 유출 방지(DLP, Data Loss Prevention) |
| 주요 위협 | OS 미패치, 보안 그룹 설정 오류 | 의존 라이브러리 취약점, API 취약점 | 계정 탈취, 섀도우 IT, 데이터 비인가 반출 |
| 가시성 | 패킷과 OS 커널 수준 제어 가능 | 런타임 로그와 메트릭 수준 | 제공자가 주는 감사 로그만 열람 |
| 컴플라이언스 | 인프라 전반의 직접 인증 필요 | 배포 소프트웨어의 보안성 평가 | 제공자의 SOC 2, CSAP 인증서 검토 |

- 선택 기준 : 통제 범위가 넓어야 하는 업무는 IaaS, 개발 속도가 중요하면 PaaS, 빠른 도입이 중요하면 SaaS가 적합하며, 각 모델의 책임 범위를 먼저 확인해야 한다.

## Ⅴ. 클라우드 서비스 보안의 한계와 방안

- 핵심 요약 : 멀티 클라우드의 가시성 파편화, 비밀키 노출, 멀티 테넌트 격리 위협을 통합 관리, 비밀 관리 체계, 전용 배치로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 멀티 클라우드 가시성 파편화 | CSP마다 대시보드와 IAM(Identity and Access Management) 정책 형식이 달라 전사 통합 모니터링이 어려움 | 단일 콘솔에서 자산을 통합 관리하고 정책을 자동 배포하는 멀티 클라우드 CNAPP(Cloud Native Application Protection Platform) 도입 | 통합 자산 비율 |
| API 키와 토큰의 소스 코드 유출 | 관리자 키가 저장소나 CI/CD(Continuous Integration/Continuous Delivery) 파이프라인에 평문으로 커밋되어 외부에서 악용됨 | 비밀 관리 시스템 연동, 커밋 전 비밀값 탐지 훅 적용 | 평문 비밀값 탐지 건수 |
| 하이퍼바이저 탈출 등 멀티 테넌트 위협 | 같은 물리 서버의 악성 VM이 하이퍼바이저 취약점으로 이웃 테넌트를 침범할 잠재 위험 | 핵심 워크로드에 전용 호스트 배치, 하드웨어 기반 기밀 VM 적용 | 전용 배치 워크로드 비율 |

## Ⅵ. 클라우드 서비스 보안에 대한 기술사적 제언

- 핵심 요약 : 인프라 코드의 사전 점검, 신원 중심 접근 통제, 인증 체계와의 상시 정렬을 함께 추진해야 클라우드 보안의 실효성이 확보된다.
- 코드형 인프라(IaC, Infrastructure as Code)는 배포 전에 정적 분석 도구를 파이프라인에 넣어 설정 오류를 사전에 차단하는 방식으로 개발 단계에서부터 보안을 내재화하는 것이 바람직하다.
- 물리 IP 주소 기반 방화벽 정책에서 벗어나, 신원 제공자와 연계한 조건부 접근과 단기 임시 자격증명을 중심으로 경계를 설계하는 것이 제로 트러스트의 방향이다.
- 공공 클라우드 이전에는 CSAP 등급별 요구사항을 충족하고, ISMS-P 체계 안에서 정기적으로 클라우드 전용 모의 침투를 수행하여 인증과 실제 보안 수준을 함께 유지해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 보안 사고의 상당수는 플랫폼 결함보다 이용자의 설정 오류와 계정 관리 미흡에서 비롯되는 책임 영역의 문제.
- 시사점 : 책임 경계를 이해하고 설정을 코드로 관리하는 체계가 클라우드 보안의 전제 조건이다.
