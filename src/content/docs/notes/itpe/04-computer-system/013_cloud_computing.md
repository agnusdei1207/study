---
title: "클라우드 컴퓨팅(Cloud Computing)"
author: "agnusdei1207"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 클라우드 컴퓨팅(Cloud Computing)의 개요

- 핵심 요약 : **클라우드 컴퓨팅**은 IT 자원을 인터넷으로 주문형 제공받아 사용량 기반 과금하는 분산 컴퓨팅 패러다임.
- 개념 : 컴퓨팅 파워, 스토리지, 데이터베이스, 네트워킹, 소프트웨어 등 정보기술(IT, Information Technology) 인프라 자원을 사용자가 직접 소유하지 않고, 인터넷 네트워크를 통해 **주문형** (On-Demand)으로 제공받아 사용량에 따라 비용을 지불(Pay-as-you-go)하는 유연한 분산 컴퓨팅 패러다임.
- 배경 및 필요성 : 전통적 온프레미스 인프라의 막대한 초기 자본 지출(CAPEX, Capital Expenditure), 긴 조달 주기(수 주~수 개월), 그리고 피크 트래픽 대비 유휴 자원의 낭비를 극복하고 디지털 트랜스포메이션의 민첩성을 확보하기 위해 탄생함.
- 핵심 목적 : IT 자원의 신속한 **탄력적(Elastic)** 프로비저닝, **운영 비용(OPEX, Operating Expenditure)** 모델 전환을 통한 재무 최적화, 글로벌 비즈니스 즉시 배포 역량 확보.

## Ⅱ. 클라우드 컴퓨팅(Cloud Computing)의 특징 및 장점

- 핵심 요약 : **NIST 5대 필수 특성**과 **SPI 서비스 모델**로 탄력적 자원 제공.
1. **주문형 셀프서비스** : 인적 개입 없이 웹 콘솔/API로 실시간 프로비저닝.
2. **광대역 네트워크 접근** : 다양한 클라이언트에서 네트워크 접근.
3. **리소스 풀링** : 멀티테넌트 환경에서 물리 하드웨어 추상화·동적 재할당.
4. **신속한 탄력성** : 워크로드 변동에 초~분 단위 스케일아웃/인.
5. **측정 가능한 서비스** : vCPU/IO/네트워크 정밀 측정 및 종량제 과금.

## Ⅲ. 클라우드 컴퓨팅(Cloud Computing)의 구조 및 동작 메커니즘

- 핵심 요약 : **NIST 5대 특성 → SPI 서비스 모델 → 4대 배포 모델**.
- 클라우드 컴퓨팅은 **NIST** (National Institute of Standards and Technology, 미국 국립표준기술원)가 정의한 5대 필수 특성, 3대 서비스 모델(SPI), 4대 배포 모델을 핵심 아키텍처 축으로 구성됨.

```text
[ NIST 클라우드 컴퓨팅 참조 아키텍처 모델 ]

+---------------------------------------------------------------+
| 5대 필수 특성 (Essential Characteristics)                     |
|  - 주문형 셀프서비스 (On-Demand Self-Service)                 |
|  - 광대역 네트워크 접근 (Broad Network Access)                |
|  - 리소스 풀링 (Resource Pooling: 멀티테넌시 기반 격리)       |
|  - 신속한 탄력성 (Rapid Elasticity: 오토스케일링)             |
|  - 측정 가능한 서비스 (Measured Service: 종량 과금)           |
+---------------------------------------------------------------+
                                │
                                ▼
+---------------------------------------------------------------+
| 3대 서비스 모델 (Service Models)                              |
|                                                               |
|  [SaaS] Software as a Service (완제품 SW, 웹 접속)            |
|    - Salesforce, Microsoft 365, Google Workspace             |
|  [PaaS] Platform as a Service (개발 런타임, DB 환경)          |
|    - AWS Elastic Beanstalk, Red Hat OpenShift                 |
|  [IaaS] Infrastructure as a Service (가상서버, 스토리지, 망)   |
|    - AWS EC2, Azure VM, GCP Compute Engine                   |
+---------------------------------------------------------------+
                                │
                                ▼
+---------------------------------------------------------------+
| 4대 배포 모델 (Deployment Models)                             |
|  - 퍼블릭 (Public)  - 프라이빗 (Private)                     |
|  - 하이브리드 (Hybrid)  - 커뮤니티 (Community)                |
+---------------------------------------------------------------+
```

## Ⅳ. 클라우드 컴퓨팅(Cloud Computing)의 비교

- 핵심 요약 : **IaaS/PaaS/SaaS/Serverless** 관리 범위 비교.

| 서비스 계층 | 고객 관리 범위 (Customer Managed) | CSP 관리 범위 (Provider Managed) | 대표 서비스 예시 |
|---|---|---|---|
| IaaS | 애플리케이션, 데이터, 런타임, 미들웨어, OS | 가상화, 서버 하드웨어, 스토리지, 데이터센터 망 | AWS EC2, Azure VM |
| PaaS | 애플리케이션 코드, 비즈니스 데이터 | 런타임 환경, OS 패치, 미들웨어, 서버 하드웨어 | Heroku, Cloud Run |
| SaaS | 사용자 계정 접근 제어, 데이터 입력/설정 | 애플리케이션 전체, 플랫폼, 인프라, 백업 전반 | Google Workspace, Slack |
| Serverless (FaaS) | 개별 함수 코드, 트리거 이벤트 매핑 | 마이크로VM 인스턴스, 스케일링, 서버 전반 | AWS Lambda, Cloud Functions |

- 클라우드 서비스 모델은 상위 계층으로 갈수록 관리 편의성과 민첩성이 증가하지만, 시스템 내부 통제권과 커스터마이징 유연성은 반비례하여 감소함.

## Ⅴ. 클라우드 컴퓨팅(Cloud Computing)의 한계와 방안

- 핵심 요약 : **비용 폭증·책임 공유 오인·벤더 종속**을 FinOps·CSPM·오픈 표준으로 대응.

- 예측 불가능한 **클라우드 비용 폭증(Cloud Bill Shock)** :
  - 한계점 : 자원 프로비저닝의 용이성으로 인해 미사용 리소스 방치, 과도한 인스턴스 스펙 선정 시 온프레미스 대비 비용 대폭 초과.
  - 해결 방안 : FinOps 프레임워크 구축, 태깅(Tagging) 의무화, 예약 인스턴스(RI)/Savings Plans 약정 할인 및 스팟 인스턴스 결합.
- 클라우드 책임 **공유 모델(Shared Responsibility)** 오인에 따른 보안 사고 :
  - 한계점 : IaaS/PaaS 도입 시 CSP가 모든 보안을 책임진다고 착각하여 S3(Simple Storage Service) 버킷 공개, 미흡한 IAM(Identity and Access Management) 권한으로 데이터 유출 빈발.
  - 해결 방안 : CSPM(Cloud Security Posture Management, 클라우드 보안 태세 관리) 솔루션 도입, IAM 최소 권한 원칙(PoLP, Principle of Least Privilege) 적용, CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인 내 코드 보안 검사 자동화.
- 특정 **글로벌 CSP 종속(Vendor Lock-in)** 및 데이터 주권 이슈 :
  - 한계점 : 특화 독점 API 및 데이터베이스 사용으로 타 클라우드로의 전환 불가 및 국가 핵심 규제 요건 위반 리스크.
  - 해결 방안 : 오픈 표준 컨테이너(Docker/K8s) 기반 워크로드 패키징, 소버린 클라우드 아키텍처 및 멀티클라우드 전략 채택.

## Ⅵ. 클라우드 컴퓨팅(Cloud Computing) 적용 제언

- 핵심 요약 : **네이티브 현대화·FinOps·Multi-AZ DR**.
- 클라우드 네이티브 현대화 : Lift-and-Shift 지양, 마이크로서비스/컨테이너/CI/CD 리팩토링.
- FinOps 거버넌스 전사 내재화 : 단위 경제학(Unit Economics) 기반 비용 최적화 KPI.
- Multi-AZ/Multi-Region DR : 미션 크리티컬 워크로드 Active-Active.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 컴퓨팅은 **주문형 탄력적 자원 제공**으로 민첩성·재무 최적화를 실현하나 비용·보안·종속 리스크 관리가 필수.
- 클라우드 컴퓨팅은 NIST 5대 특성과 SPI 서비스 모델로 IT 자원을 주문형·탄력적으로 제공하여 CAPEX→OPEX 전환과 민첩성을 실현하지만, 비용 폭증·책임 공유 오인·벤더 종속 리스크를 FinOps·CSPM·오픈 표준으로 관리해야 함.
- 답안에는 5대 특성, SPI 비교, 한계·대응, 네이티브 현대화 제언을 연결.