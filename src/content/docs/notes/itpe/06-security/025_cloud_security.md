---
title: "클라우드 보안(CSAP·ISO/IEC 27017·CSP 리스크)"
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

## Ⅰ. 클라우드 보안(CSAP·ISO/IEC 27017·CSP 리스크)의 개요

- 개념 : IaaS, PaaS, SaaS 등 클라우드 서비스 환경에서 발생하는 멀티테넌시 데이터 유출, 설정 오류, API(Application Programming Interface) 침해를 방어하고, 국내외 컴플라이언스(CSAP(Cloud Security Assurance Program), ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission) 27017) 및 책임 공유 모델(Shared Responsibility Model)에 입각하여 안전성을 확보하는 포괄적 보안 체계.
- 배경 및 필요성 : 온프레미스에서 클라우드로의 전면 전환에 따라 전통적인 물리 경계가 소멸하고, **CSP** (Cloud Service Provider)의 인프라 장애나 고객의 클라우드 설정 오류(Misconfiguration)로 인한 초대형 사고 빈발.
- 핵심 목적 : 클라우드 데이터 기밀성 유지, 안전한 워크로드 운영, 국내외 보안 인증 획득을 통한 공공·엔터프라이즈 규제 준수 달성.

## Ⅱ. 클라우드 보안(CSAP·ISO/IEC 27017·CSP 리스크)의 핵심 아키텍처 및 동작 메커니즘

클라우드 보안은 서비스 모델(IaaS, PaaS, SaaS)에 따라 CSP와 고객 간의 책임 경계가 완전히 달라지는 '책임 공유 모델'을 근간으로 통제가 설계됨.

```text
[ 클라우드 서비스 모델별 책임 공유 모델 (Shared Responsibility) ]

   [ 서비스 계층 ]            [ IaaS ]          [ PaaS ]          [ SaaS ]
   +-----------------------+-----------------+-----------------+-----------------+
   | 데이터 및 접근 관리   |    고객 책임    |    고객 책임    |    고객 책임    |
   +-----------------------+-----------------+-----------------+-----------------+
   | 애플리케이션          |    고객 책임    |    고객 책임    |    CSP 책임     |
   +-----------------------+-----------------+-----------------+-----------------+
   | 런타임 및 미들웨어    |    고객 책임    |    CSP 책임     |    CSP 책임     |
   +-----------------------+-----------------+-----------------+-----------------+
   | 운영체제 (OS)         |    고객 책임    |    CSP 책임     |    CSP 책임     |
   +-----------------------+-----------------+-----------------+-----------------+
   | 가상화 계층           |    CSP 책임     |    CSP 책임     |    CSP 책임     |
   +-----------------------+-----------------+-----------------+-----------------+
   | 물리 서버 및 네트워크 |    CSP 책임     |    CSP 책임     |    CSP 책임     |
   +-----------------------+-----------------+-----------------+-----------------+
```

- **책임 공유 모델** (Shared Responsibility Model) : 물리 인프라와 하이퍼바이저는 CSP가 보호하되, 클라우드 내에 저장된 데이터, IAM(Identity and Access Management) 계정 설정, OS(Operating System) 패치는 전적으로 고객 책임.
- **CSAP** (클라우드 보안인증제) : 공공기관에 민간 클라우드를 공급하기 위해 과학기술정보통신부·KISA(Korea Internet & Security Agency)가 주관하는 제도(상·중·하 등급제 개편).
- **ISO/IEC 27017** : ISO 27001을 기반으로 클라우드 환경에 특화된 7개 추가 통제(가상머신 격리, 자산 반환 및 삭제 등)를 규정한 국제 표준.
- **CSPM(Cloud Security Posture Management) / CWPP(Cloud Workload Protection Platform) / CNAPP** : 클라우드 인프라 설정 오류를 탐지하는 CSPM, 컨테이너/VM(Virtual Machine) 워크로드를 보호하는 CWPP를 통합한 CNAPP 플랫폼 운용.

## Ⅲ. 클라우드 보안(CSAP·ISO/IEC 27017·CSP 리스크)의 세부 구성 요소 및 비교 분석

| 비교 항목 | 온프레미스 보안 | 클라우드 보안 (IaaS/PaaS) | 주요 통제 기술 |
| --- | --- | --- | --- |
| 보안 경계 | 전산실 물리 경계, 외곽 L3/L4 방화벽 | 소프트웨어 정의 네트워크(VPC, Virtual Private Cloud), IAM 신원 | ZTNA(Zero Trust Network Access), 클라우드 IAM, Security Group |
| 보안 위협 1순위 | 외부 네트워크 침투, 물리적 장비 도난 | 클라우드 설정 오류(Misconfiguration), IAM 키 유출 | CSPM (Cloud Security Posture Management) |
| 자산 가시성 | 정적 하드웨어 인벤토리 실사 | 동적 생성/소멸되는 컨테이너 및 서버리스 | eBPF 텔레메트리, CSPM 자산 스캔 |
| 컴플라이언스 | ISMS(Information Security Management System), PIMS(Personal Information Management System), ISO 27001 | CSAP (상/중/하), ISO 27017, FedRAMP | Compliance-as-Code 자동 감사 도구 |
| 대응 주체 | 사내 인프라/보안팀 단독 | 고객 보안팀과 CSP 간의 협업(책임 분계점) | CSP 감사 로그 (CloudTrail) + SIEM(Security Information and Event Management) 연계 |

- 클라우드 보안 사고의 대부분은 CSP 인프라 결함이 아닌 고객의 S3(Simple Storage Service) 버킷 공개, IAM 권한 과다 부여 등 '설정 오류'에서 발생하므로 설정 자동화 감사가 최우선임.

## Ⅳ. 클라우드 보안(CSAP·ISO/IEC 27017·CSP 리스크)의 주요 한계점 및 해결 방안

- **클라우드 자원 설정 오류** (Misconfiguration) 및 섀도우 인프라 폭증 :
  - 한계점 : 개발자가 테스트 목적으로 개방한 공용 S3 버킷이나 0.0.0.0/0 개방 보안 그룹으로 인해 기밀 데이터가 인터넷에 무단 노출.
  - 해결 방안 : CSPM 도구를 파이프라인에 통합하고 **IaC** (Terraform, CloudFormation) 템플릿 검사(Checkov, tfsec)를 통해 설정 오류 배포를 원천 차단.
- IAM 장기 자격증명(Access Key) 소스코드 유출에 따른 전사 침해 :
  - 한계점 : 개발자가 AWS(Amazon Web Services) Access Key를 GitHub 공개 저장소에 실수로 커밋하여 수 분 내에 암호화폐 채굴 봇넷에 인프라 전량 장악.
  - 해결 방안 : 장기 정적 키 사용을 전면 금지하고, **OIDC**(OpenID Connect) 및 **임시 세션 토큰** (STS, IAM Role) 기반 인증 강제 및 **Secret Scanning** 자동 차단.
- **CSP 락인** (Vendor Lock-in) 및 멀티 클라우드 간 보안 정책 파편화 :
  - 한계점 : AWS, Azure, GCP(Google Cloud Platform)의 보안 정책 용어와 API가 상이하여 전사 통합 모니터링이 불가능하고 관리 사각지대 발생.
  - 해결 방안 : 멀티 클라우드를 단일 대시보드로 통합 관리하는 CNAPP(Cloud-Native Application Protection Platform) 도입 및 공통 보안 오케스트레이션 수립.

## Ⅴ. 클라우드 보안(CSAP·ISO/IEC 27017·CSP 리스크) 적용 및 발전을 위한 기술사적 제언

- 공공 클라우드 진입을 위한 CSAP 등급제 맞춤형 설계 : 시스템 중요도에 따라 상(국가 안보), 중(개인정보), 하(대민 공개) 등급 요건을 분석하여 논리적 망분리 허용 여부 선제 검토.
- **클라우드 탐지 및 대응** (CDR, Cloud Detection and Response) 체계 수립 : 단순 로그 수집을 넘어 클라우드 제어 평면(API 호출)과 데이터 평면(런타임 컨테이너)의 이상 징후를 실시간 상호분석.
- DevSecOps 파이프라인을 통한 **Shift-Left** 강제 : 컨테이너 이미지 취약점 스캔, SBOM(Software Bill of Materials) 생성, IaC 보안 검사를 통과해야만 클라우드 K8s 클러스터 배포를 허용하는 **Admission Controller** 연동.
