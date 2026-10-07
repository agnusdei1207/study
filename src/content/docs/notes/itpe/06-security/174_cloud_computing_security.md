---
title: "클라우드 컴퓨팅 보안(Cloud Security)"
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

## Ⅰ. 클라우드 컴퓨팅 보안(Cloud Security)의 개요

- 개념 : **클라우드 컴퓨팅 환경** (IaaS, PaaS, SaaS, 하이브리드/멀티 클라우드)에서 가상화 인프라, 컨테이너, 서버리스 워크로드, 마이크로서비스 및 데이터를 내외부 사이버 위협으로부터 보호하기 위해 수립하는 종합적인 보안 아키텍처, 거버넌스 및 자동화 통제 체계.
- 배경 및 필요성 : 온프레미스 인프라가 멀티 클라우드로 급격히 전환되면서 네트워크 경계가 사라지고, **코드형 인프라** (IaC, Infrastructure as Code) 배포 오류, 과도한 IAM(Identity and Access Management) 권한, **섀도우 클라우드** 자산의 노출로 인한 대규모 데이터 침해가 빈발함.
- 핵심 목적 : 클라우드의 민첩성과 확장성을 저해하지 않으면서도, 멀티 테넌트 환경의 완벽한 자원 격리, 컴플라이언스 준수, **코드형 보안** (Security as Code)을 통한 **제로 트러스트** 달성.

## Ⅱ. 클라우드 컴퓨팅 보안(Cloud Security)의 핵심 아키텍처 및 동작 메커니즘

현대 클라우드 보안 아키텍처는 클라우드 네이티브 애플리케이션 보호 플랫폼(CNAPP)을 중심으로 CSPM(Cloud Security Posture Management), CWPP(Cloud Workload Protection Platform), CIEM(Cloud Infrastructure Entitlement Management)이 통합된 단일 파이프라인으로 동작함.

```text
[ 통합 클라우드 보안 플랫폼 (CNAPP: Cloud Native Application Protection Platform) ]

 +--------------------------------------------------------------------------+
 |                      CNAPP (통합 클라우드 네이티브 보안 플랫폼)          |
 |                                                                          |
 |  [ 1. CSPM : 자세 관리 ]     | [ 2. CIEM : 권한 관리 ]                    |
 |  * 멀티클라우드 설정오류 탐지 | * IAM 과잉 권한 머신러닝 분석             |
 |  * S3 퍼블릭 오픈 자동 치유   | * 미사용 권한 제거, 최소 권한 자동화       |
 |  * CIS 벤치마크 컴플라이언스 | * 권한 상승(Privilege Escalation) 차단     |
 | -----------------------------+------------------------------------------ |
 |  [ 3. CWPP : 워크로드 보호 ] | [ 4. Shift-Left : 코드형 보안 (DevSecOps) ]|
 |  * VM, Docker, K8s 런타임보호| * Terraform / K8s 매니페스트 사전 정적 스캔|
 |  * 컨테이너 이미지 취약점검사| * Git 프리커밋 훅 시크릿(API Key) 유출 차단|
 |  * eBPF 기반 비정상 행위 차단| * SBOM(소프트웨어 자재명세서) 무결성 검증  |
 +----------------------------------+---------------------------------------+
                                    |
                                    v
 [ 클라우드 전주기 런타임 환경 (AWS, Azure, GCP, K8s 클러스터) ]
  * 통합 가시성 대시보드 제공
  * 공격 경로 분석 (Attack Path Analysis) -> 복합 위협 우선순위화!
```

- **CNAPP (Cloud Native Application Protection Platform)** : 파편화되어 있던 CSPM, CWPP, CIEM, IaC 스캐닝 도구를 단일 플랫폼으로 통합하여 개발부터 배포, 런타임까지 전주기 보안 제공.
- **CSPM (Cloud Security Posture Management)** : 클라우드 서비스 설정 상태를 API(Application Programming Interface)로 상시 감사하여 잘못된 네트워크 보안 그룹, 비암호화 스토리지 등 설정 오류(Misconfiguration)를 탐지·자동 복구.
- **CWPP (Cloud Workload Protection Platform)** : 가상머신, 컨테이너, 서버리스 등 실행 중인 워크로드 내부의 시스템 콜과 파일 무결성을 모니터링하여 익스플로잇 및 랜섬웨어 공격 방어.
- **CIEM (Cloud Infrastructure Entitlement Management)** : 클라우드 IAM의 과도하게 부여된 권한(Excessive Entitlements)을 지속적으로 식별하고 최소 권한 원칙에 따라 동적으로 회수.

## Ⅲ. 클라우드 컴퓨팅 보안(Cloud Security)의 세부 구성 요소 및 비교 분석

| 비교 항목 | **CSPM** (자세 관리) | **CWPP** (워크로드 보호) | **CIEM** (권한 관리) | **CASB** (Cloud Access Security Broker, 접근 중개) |
| --- | --- | --- | --- | --- |
| 통제 계층 | 클라우드 제어 평면 (Control Plane) | 실행 중인 워크로드 (Data Plane) | 신원 및 권한 계층 (IAM) | 사용자와 SaaS 간 네트워크 에지 |
| 수집 방식 | CSP(Cloud Service Provider) 제공 API 기반 (Agentless) | OS(Operating System)/컨테이너 내부 에이전트/eBPF | 클라우드 IAM 정책 로그 분석 | 프록시(인라인) 및 API 연동 |
| 핵심 목적 | 인프라 설정 오류 및 규제 감사 | 런타임 악성코드 및 침입 차단 | 과잉 권한 회수, 권한 탈취 방어 | SaaS 데이터 유출(DLP, Data Loss Prevention) 및 접근 통제 |
| 주요 대상 | S3(Simple Storage Service) 버킷, 보안그룹, VPC(Virtual Private Cloud), IAM 설정 | EC2, Docker 컨테이너, Pod, Lambda | AWS(Amazon Web Services) IAM Role, Azure AD(Active Directory), 서비스계정 | M365, Google Workspace, Salesforce |

- 클라우드 보안 사고의 대부분은 클라우드 자체의 취약점이 아닌 고객의 설정 오류와 부실한 IAM에서 발생하므로, 코드형 보안(Shift-Left)과 CNAPP의 조기 정착이 필수적임.

## Ⅳ. 클라우드 컴퓨팅 보안(Cloud Security)의 주요 한계점 및 해결 방안

- 클라우드 설정 오류(Misconfiguration)의 자동화된 공격 표면 노출 :
  - 한계점 : S3 버킷을 실수로 퍼블릭 개방할 경우 공격자의 전 세계 포트 스캐닝 봇에 의해 수 분 내에 탐지되어 기밀 데이터 유출.
  - 해결 방안 : IaC 파이프라인에서 프리커밋 정적 분석(Checkov)을 강제하고 CSPM 자동 복구(Auto-Remediation) 규칙 가동.
- 멀티 클라우드 확산에 따른 보안 정책 파편화 및 사각지대 :
  - 한계점 : AWS, GCP(Google Cloud Platform), Azure마다 서로 다른 보안 용어, 대시보드, IAM 구조를 가지고 있어 일관된 전사 보안 거버넌스 유지 곤란.
  - 해결 방안 : 이종 클라우드 API를 단일 쿼리 언어로 통합 감사할 수 있는 멀티 클라우드 전용 CNAPP 플랫폼 구축.
- 하이퍼바이저 및 컨테이너 샌드박스 탈출(Escape) 제로데이 :
  - 한계점 : 공동 테넌트 환경에서 악성 컨테이너가 리눅스 커널 취약점을 악용해 호스트 노드를 장악하고 타 테넌트의 메모리 데이터 침범 위험.
  - 해결 방안 : gVisor, Kata Containers 등 격리형 마이크로VM(Virtual Machine) 런타임 도입 및 호스트 커널 시스템 콜 seccomp/AppArmor 강제 프로파일링.

## Ⅴ. 클라우드 컴퓨팅 보안(Cloud Security) 적용 및 발전을 위한 기술사적 제언

- 시프트 레프트(Shift-Left) 기반 데브섹옵스(DevSecOps) 내재화 : 배포 후 사후 점검 대신 개발자가 작성한 Terraform 코드와 Dockerfile을 빌드 파이프라인에서 자동 검사하여 결함 조기 치유.
- 제로 트러스트 기반 단기 임시 자격증명(STS) 및 IAM 역할 사용 : 소스코드나 서버에 고정된 영구 API Access Key 하드코딩을 전면 금지하고, 1시간 만료되는 IAM Role 임시 토큰만 사용.
- 기밀 컴퓨팅(Confidential Computing) 기술을 통한 사용 중(In-Use) 데이터 보호 : 클라우드 메모리 상에서 데이터가 처리되는 동안에도 하드웨어 TEE(Intel SGX, AMD SEV)로 메모리를 실시간 암호화하여 CSP 내부자 도청 차단.
