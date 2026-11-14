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
- 주요 목적: 클라우드 데이터 기밀성 유지, 안전한 워크로드 운영, 공공과 기업의 규제 준수를 위한 **CSAP** (Cloud Security Assurance Program, 클라우드 보안인증제) 및 ISO/IEC 27017 대응.

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

## Ⅳ. 온프레미스 보안과 클라우드 보안의 비교

- 핵심 요약 : 경계 중심의 온프레미스 보안과 신원·설정 중심의 클라우드 보안은 통제 대상과 책임 구조가 다름.

| 비교 항목 | 온프레미스 보안 | 클라우드 보안 (IaaS·PaaS) |
| --- | --- | --- |
| 보안 경계 | 전산실 물리 경계, 외곽 방화벽 | 가상 네트워크(VPC), IAM 신원 |
| 주요 위협 | 외부 침투, 물리적 장비 도난 | 설정 오류, IAM 키 유출 |
| 자산 가시성 | 정적 하드웨어 인벤토리 | 동적 컨테이너·서버리스 자산 |
| 컴플라이언스 | ISMS, ISO/IEC 27001 | CSAP, ISO/IEC 27017, FedRAMP |
| 대응 주체 | 사내 인프라·보안팀 단독 | 고객과 CSP의 책임 분계 협업 |

- 클라우드 사고는 CSP 인프라 결함보다 고객 측 설정 실수와 자격증명 관리 실패에서 빈번하게 발생하므로, 설정 자동 점검이 우선 과제.

## Ⅴ. 클라우드 보안(CSAP·ISO/IEC 27017)의 한계와 방안

- 핵심 요약 : 설정 오류, 자격증명 유출, 멀티 클라우드 파편화를 배포 단계 검증, 임시 자격증명, 통합 관리로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 설정 오류(Misconfiguration) | 공개 버킷·과도한 권한 설정 → 데이터 노출 | CSPM과 IaC 보안 검사로 배포 전 차단 | 설정 오류 탐지 건수 |
| 장기 자격증명 유출 | 정적 키 노출·재사용 → 인프라 장악 위험 | OIDC·STS 기반 임시 자격증명, 시크릿 스캔 | 장기 키 보유 계정 수 |
| CSP 락인(Vendor Lock-in) | 정책·API 차이 → 통합 모니터링 사각지대 | CNAPP 도입과 공통 보안 정책 정의 | 정책 일관성 점검 결과 |

## Ⅵ. 클라우드 보안(CSAP·ISO/IEC 27017)에 대한 제언

- 핵심 요약 : 인증 대응, 탐지 체계, 개발 보안 거버넌스를 상시 운영 역량으로 내재화.
- 인증·거버넌스 : 시스템 중요도별 CSAP 등급 요건과 책임 분계표를 사전 정의·주기 갱신.
- 탐지·대응 : 제어 평면 로그와 런타임 이상 징후를 결합한 CDR 체계 운영.
- 개발 보안 : IaC 검사, 컨테이너 취약점 점검, SBOM을 배포 승인 조건으로 두는 Shift-Left 정착.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 보안은 책임 경계와 설정 상태를 지속적으로 통제하는 운영 체계의 문제.
- 시사점 : 설정 코드 검증, 임시 자격증명 전환, 책임 분계 문서화가 클라우드 보안의 기본 전제.
