---
title: "클라우드 보안(CSAP·ISO/IEC 27017·CSP 리스크) (ISO: International Organization for Standardization; IEC: International Electrotechnical Commission; CSAP: Cloud Security Assurance Program; CSP: Cloud Service Provider)"
author: "agnusdei1207"
date: "2026-10-24T22:55:10+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "025"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 클라우드 보안, CSAP, ISO/IEC 27017, CSP, 책임 공유 모델
- CSPM, CWPP, CNAPP, CDR, IaC, Shift-Left, SBOM
- 설정 오류, 장기 자격증명, CSP 락인

## Ⅰ. 클라우드 보안(CSAP·ISO/IEC 27017)의 개요

- 핵심 요약 : 클라우드 환경의 설정 오류와 자격증명 유출을 막고 국내외 인증 기준을 충족하도록 책임을 나누어 관리하는 보안 체계.
- 개념 : IaaS(Infrastructure as a Service), PaaS(Platform as a Service), SaaS(Software as a Service) 등 클라우드 서비스에서 발생하는 데이터 유출, 설정 오류, API(Application Programming Interface) 침해를 방어하기 위해 **책임 공유 모델** (Shared Responsibility Model)에 따라 보안 책임을 나누는 체계.
- 배경 및 필요성 : 온프레미스에서 클라우드로 전환하면서 물리적 경계가 사라지고, **CSP** (Cloud Service Provider, 클라우드 서비스 제공자)의 인프라 장애와 고객의 설정 오류가 모두 사고 원인이 되므로, 두 주체의 책임을 명확히 할 필요가 생김.
- 주요 목적 : 클라우드 데이터 기밀성 유지, 안전한 워크로드 운영, 공공과 기업의 규제 준수를 위한 **CSAP** (Cloud Security Assurance Program, 클라우드 보안인증제) 및 ISO/IEC 27017 대응.

## Ⅱ. 클라우드 보안(CSAP·ISO/IEC 27017)의 특징 및 장점

- 핵심 요약 : 책임 경계의 명시, 설정 상태의 상시 점검, 워크로드 런타임 보호가 결합되어 클라우드 설정 오류를 조기에 찾고 관리 범위를 단일화하는 구조.

1. **책임 공유 모델** (Shared Responsibility Model, 인프라는 CSP가, 데이터와 설정은 고객이 맡는 책임 분담 원칙) : 책임 분계점이 서비스 모델별로 정해져 보안 책임 누락을 줄임.
2. **CSPM** (Cloud Security Posture Management, 클라우드 설정 상태 점검 관리) : 클라우드 API로 자산 설정을 주기적으로 점검 → 공개 설정과 과다 권한의 조기 탐지.
3. **CWPP** (Cloud Workload Protection Platform, 클라우드 워크로드 보호 플랫폼) : 컨테이너와 VM(Virtual Machine) 등 실행 중인 워크로드를 보호 → 런타임 위협의 즉시 차단.
4. **CNAPP** (Cloud-Native Application Protection Platform, 클라우드 네이티브 애플리케이션 보호 플랫폼) : CSPM과 CWPP 등 기능을 통합 → 멀티 클라우드를 단일 화면에서 관리.

## Ⅲ. 클라우드 보안(CSAP·ISO/IEC 27017)의 구조 (흐름)

- 핵심 요약 : 서비스 모델에 따라 책임 분계점이 이동하고, 설정 점검과 배포 게이트가 사고를 앞단에서 막는 구조.

```text
[ 책임 공유 모델 (IaaS 기준) ]

고객 책임 영역
  데이터, 애플리케이션, OS, IAM 설정
   ↓ 책임 분계점
CSP 책임 영역
  가상화 계층, 물리 서버, 네트워크
```

```text
[ IaC 배포 전 차단 흐름 ]

IaC 템플릿 작성
   ↓
보안 검사 (Checkov, tfsec)
   ↓ 위험 설정 발견
배포 차단 후 수정
   ↓ 검사 통과
클라우드 배포
```

```text
[ 클라우드 보안 통합 흐름 ]

클라우드 자산 (IaaS, PaaS, SaaS)
   ↓ 설정 상태 점검
CSPM (설정 오류 탐지)
   ↓ 실행 중 보호
CWPP (컨테이너·VM 보호)
   ↓ 통합 관리
CNAPP (멀티 클라우드 관리)
```

- **CSAP** (Cloud Security Assurance Program, 클라우드 보안인증제) : 공공기관에 민간 클라우드를 공급하기 위해 과학기술정보통신부와 KISA(Korea Internet & Security Agency, 한국인터넷진흥원)가 주관하는 인증 제도로, 시스템 중요도에 따른 상·중·하 등급으로 운영.
- **ISO/IEC 27017** (클라우드 서비스 정보보호 국제 표준) : ISO/IEC 27002를 바탕으로 클라우드 환경에 특화된 추가 통제 7개를 규정한 국제 표준.

| 비교 항목 | 온프레미스 보안 | 클라우드 보안 (IaaS·PaaS) | 주요 통제 기술 |
| --- | --- | --- | --- |
| 보안 경계 | 전산실 물리 경계, 외곽 방화벽 | 가상 네트워크 (VPC, Virtual Private Cloud), IAM 신원 | 제로트러스트 접근 (ZTNA, Zero Trust Network Access), 보안 그룹 |
| 주요 위협 | 외부 침투, 물리적 장비 도난 | 설정 오류, IAM 키 유출 | CSPM |
| 자산 가시성 | 정적 하드웨어 인벤토리 점검 | 동적으로 생성·소멸되는 컨테이너와 서버리스 | eBPF (extended Berkeley Packet Filter) 기반 텔레메트리 |
| 컴플라이언스 | ISMS (Information Security Management System), ISO/IEC 27001 | CSAP, ISO/IEC 27017, FedRAMP (Federal Risk and Authorization Management Program) | 컴플라이언스 자동 감사 도구 |
| 대응 주체 | 사내 인프라·보안팀 단독 | 고객 보안팀과 CSP의 책임 분계점 기반 협업 | 클라우드 감사 로그와 SIEM (Security Information and Event Management) 연계 |

- 클라우드 사고는 CSP 인프라 결함보다 고객 측 설정 실수와 자격증명 관리 실패에서 빈번하게 발생하므로, 설정 자동 점검이 우선 과제가 됨.

## Ⅳ. 클라우드 보안(CSAP·ISO/IEC 27017)의 한계와 방안

- 핵심 요약 : 설정 오류, 자격증명 유출, 멀티 클라우드 파편화를 배포 단계 검증, 임시 자격증명, 통합 관리로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| **설정 오류** (Misconfiguration) | 테스트용으로 개방한 공용 버킷과 전체 개방 보안 그룹으로 기밀 데이터가 인터넷에 노출 | CSPM을 배포 파이프라인에 통합하고, **IaC** (Infrastructure as Code, 인프라를 코드로 정의하는 방식) 템플릿을 검사해 위험 설정의 배포를 차단 | 설정 오류 탐지 건수, 공개 자원 수 |
| **장기 자격증명** (Long-lived Credential) 유출 | 액세스 키를 공개 저장소에 실수로 커밋하면 외부에서 인프라를 장악할 수 있음 | 장기 정적 키 사용을 줄이고, **OIDC** (OpenID Connect) 연동과 **STS** (Security Token Service, 임시 보안 자격증명) 기반 세션 발급, Secret Scanning으로 커밋 단계 차단 | 장기 키 보유 계정 수, 커밋 차단 건수 |
| **CSP 락인** (Vendor Lock-in) | 클라우드마다 보안 정책 용어와 API가 달라 통합 모니터링에 사각지대 발생 | 멀티 클라우드를 한 화면에서 관리하는 CNAPP 도입과 공통 보안 정책 정의 | 클라우드별 정책 일관성 점검 결과 |

## Ⅴ. 클라우드 보안(CSAP·ISO/IEC 27017)에 대한 기술사적 제언

- 핵심 요약 : 인증 대응을 시스템 중요도 기준으로 미리 설계하고, 탐지 체계와 개발 보안 거버넌스를 함께 운영하여 클라우드 보안을 상시 관리 역량으로 내재화.

1. 등급별 인증 전략 : 공공 분야 클라우드 도입 전에 시스템 중요도별 CSAP 등급 요건을 미리 분석하고, 망분리 적용 범위를 사전에 검토하여 도입 지연을 줄이는 것이 필요.
2. 탐지 대응 체계 : 보안관제 조직이 클라우드 제어 평면의 API 호출 기록과 워크로드 런타임의 이상 징후를 함께 분석하는 **CDR** (Cloud Detection and Response, 클라우드 탐지 및 대응) 체계를 운영하는 것이 필요.
3. 개발 보안 거버넌스 : 개발 조직과 보안 조직이 배포 보안 게이트의 기준과 예외 승인 절차를 공동으로 정하고, 컨테이너 이미지 취약점과 SBOM(Software Bill of Materials, 소프트웨어 구성 명세서)을 배포 승인 조건으로 두는 **Shift-Left** (보안 점검을 개발 초기 단계로 앞당기는 방식) 문화 정착이 필요.

## Ⅵ. 클라우드 보안(CSAP·ISO/IEC 27017)의 기술사적 제언

- 핵심 요약 : 클라우드 보안을 도입 프로젝트가 아닌 설정 검증과 책임 분계를 상시 운영하는 거버넌스 문제로 다루는 것이 필요.
- 책임 분계 문서화 : 보안 부서와 사업 부서가 서비스별 책임 분계표를 만들고 분기마다 갱신하여, 설정 변경 시 책임 주체가 모호해지는 상황을 막아야 함.
- 자격증명 정책 : 장기 키 발급을 승인 절차로 묶고, 임시 자격증명 전환 현황을 경영진 보고 지표로 관리하는 것이 필요.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 보안은 기술 도입보다 책임 경계와 설정 상태를 지속적으로 통제하는 운영 체계의 문제임.
- 시사점 : 설정을 코드로 검증하고 책임 분계를 문서로 관리하는 방식이 클라우드 보안의 기본 전제로 자리 잡는 흐름.
