---
title: "클라우드 컴퓨팅 서비스 모델"
author: "agnusdei1207"
date: "2026-10-24T22:41:35+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 클라우드 컴퓨팅 서비스 모델, IaaS, PaaS, SaaS, FaaS
- 서버리스(Serverless), 공유 책임 모델, 관리 책임 분계, NIST SP 800-145
- 벤더 종속(Vendor Lock-in), 리프트 앤드 시프트(Lift-and-Shift), 클라우드 네이티브 리팩토링
- CASB(Cloud Access Security Broker), BYOK(Bring Your Own Key), CSPM(Cloud Security Posture Management)

## Ⅰ. 클라우드 컴퓨팅 서비스 모델의 개요

- 핵심 요약 : 고객이 직접 통제하는 범위와 CSP가 관리하는 범위의 경계에 따라 서비스를 구분하는 클라우드 제공 모델 체계.
- 개념 : 미국 **NIST** (National Institute of Standards and Technology, 미국 국립표준기술연구원)의 SP 800-145가 정의한 클라우드 컴퓨팅 분류 체계로, 고객의 제어 범위와 **CSP** (Cloud Service Provider, 클라우드 서비스 제공자)가 관리하는 추상화 계층에 따라 **IaaS** (Infrastructure as a Service, 서비스형 인프라), **PaaS** (Platform as a Service, 서비스형 플랫폼), **SaaS** (Software as a Service, 서비스형 소프트웨어)의 3대 모델로 구분하며, 최근에는 서버리스(Serverless) 방식의 **FaaS** (Function as a Service, 서비스형 함수)가 함께 쓰임.
- 배경 및 필요성 : 과거에는 서버 하드웨어부터 OS(Operating System), 미들웨어, 애플리케이션까지 기업이 직접 구축하고 유지보수했으나, 핵심 업무 로직에 집중하고 비핵심 인프라 관리를 위임하려는 요구에 따라 서비스 모델이 발전함.
- 주요 목적 : 관리 책임의 선택적 위임, 인프라 민첩성 확보, 초기 구축 비용(CapEx, Capital Expenditure)의 운영 비용(OpEx, Operational Expenditure) 전환.

## Ⅱ. 클라우드 서비스 모델별 특징 및 관리 책임 분계

- 핵심 요약 : 모델이 올라갈수록 고객의 관리 범위가 줄고 CSP의 책임이 커지며, 그만큼 제어 자유도는 낮아지는 반비례 구조.

1. IaaS : 서버, 스토리지, 가상화 계층을 CSP가 제공 → 고객은 OS 설치, 보안 패치, 미들웨어 구동을 맡아 제어 자유도가 가장 높음.
2. PaaS : OS와 개발 런타임, 미들웨어를 CSP가 관리 → 고객은 소스코드와 데이터에만 집중하여 운영 부담이 줄어듦.
3. SaaS : 완성된 애플리케이션을 웹 브라우저나 API(Application Programming Interface)로 즉시 이용 → 고객은 설정과 사용자 권한만 관리하여 유지보수 부담이 가장 작음.

## Ⅲ. 클라우드 서비스 모델의 구조와 책임 위임

- 핵심 요약 : 온프레미스에서 SaaS로 갈수록 CSP의 관리 범위가 넓어지는 단계형 책임 위임 구조.

```text
[ 관리 책임 위임 흐름 ]

온프레미스 : 전 계층 고객 관리
   ↓
IaaS : OS 이상 계층 고객 관리
   ↓
PaaS : 애플리케이션과 데이터만 고객 관리
   ↓
SaaS : 설정과 접근 권한만 고객 관리
```

- 공유 책임 모델(Shared Responsibility Model)에 따라 IaaS에서는 OS 패치와 취약점 관리가 전적으로 고객 책임이며, 이 경계를 문서로 명확히 해야 함.

```text
[ IaaS 기준 책임 경계 ]

고객 책임 : 애플리케이션, 데이터, 런타임, OS
   ↓ 책임 경계선
CSP 책임 : 가상화, 서버 하드웨어, 스토리지, 네트워크
```

## Ⅳ. 클라우드 3대 서비스 모델 비교 분석

- 핵심 요약 : 세 모델은 사용자 대상, 제어 유연성, 유지보수 부담, 벤더 종속성이 서로 반대로 움직이므로 업무 성격에 맞춰 조합.

| 비교 항목 | IaaS (인프라 서비스) | PaaS (플랫폼 서비스) | SaaS (소프트웨어 서비스) |
| :--- | :--- | :--- | :--- |
| 제공 핵심 단위 | 가상 머신(VM, Virtual Machine), 가상 네트워크, 블록 볼륨 | 개발 프레임워크, 관리형 DB(Database), 실행 환경 | 완성된 최종 사용자 애플리케이션 |
| 사용자 대상 | 시스템 엔지니어, 네트워크 관리자 | 애플리케이션 개발자, 데이터 엔지니어 | 일반 사용자, 현업 부서 |
| 제어 유연성 | 최고 (OS 수준 설정 가능) | 중간 (런타임 안의 설정만 가능) | 최저 (제공 기능 설정만 가능) |
| 유지보수 부담 | 높음 (OS 패치, 미들웨어 튜닝 직접 수행) | 낮음 (애플리케이션 품질에 집중) | 최저 (직접 유지보수 없음) |
| 벤더 종속성 | 낮음 (VM 이미지의 이관이 상대적으로 용이) | 높음 (CSP 전용 PaaS API 의존) | 최고 (데이터 추출 외 타 시스템 전환이 어려움) |
| 대표 서비스 | AWS EC2, Azure Virtual Machines, Google Compute Engine | AWS Elastic Beanstalk, Heroku, Google App Engine | Microsoft 365, Salesforce, Google Workspace |

## Ⅴ. 서비스 모델 채택 시 주요 한계와 방안

- 핵심 요약 : 벤더 종속, 데이터 통제 상실, 운영 역량 부족이 모델별로 다른 형태로 나타나므로 모델에 맞는 통제 수단을 병행.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| PaaS의 벤더 종속(Vendor Lock-in) 심화 | CSP 전용 관리형 DB나 고유 API에 맞춘 코드는 타 클라우드로 이전이 어려움 | 쿠버네티스(Kubernetes, K8s) 기반 표준 스택과 클라우드 중립적 프레임워크 사용 | 전용 API 의존 모듈 비율 |
| SaaS의 데이터 주권·통제 상실 | 기밀 데이터가 외부 서버에 저장되어 유출 위험과 감사 증적 확보 곤란 | CASB(Cloud Access Security Broker) 도입, BYOK(Bring Your Own Key) 기반 암호화 적용 | 감사 로그 확보율, 외부 공유 이벤트 건수 |
| IaaS의 운영 역량 부족 | 레거시 VM을 그대로 옮기는 리프트 앤드 시프트(Lift-and-Shift)는 클라우드 장점 없이 비용만 증가 | 클라우드 네이티브 리팩토링, 오토스케일링 적용, 관리형 서비스로 점진 전환 | 월간 인프라 비용, 자동 확장 적용률 |

## Ⅵ. 엔터프라이즈 클라우드 전환을 위한 기술사적 제언

- 핵심 요약 : 범용 업무는 SaaS로 빠르게 도입하고 핵심 업무는 PaaS 위에 두되, IaaS 구간의 보안 책임을 명확히 하는 혼합 전략.

범용 업무인 메일, ERP(Enterprise Resource Planning), CRM(Customer Relationship Management) 같은 영역은 SaaS 도입을 우선 검토하여 개발 부담을 줄이는 것이 합리적이다. 차별화된 핵심 업무 시스템은 컨테이너 기반 PaaS에서 마이크로서비스 구조로 구축하여 확장성을 확보하는 방향이 적절하다. IaaS를 쓰는 구간에는 OS 패치와 취약점 관리가 고객 책임임을 조직 규정으로 명시하고, CSPM(Cloud Security Posture Management) 도구로 설정 오류를 상시 점검하는 체계를 함께 갖출 필요가 있다.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 서비스 모델은 관리 책임의 위임 수준을 고르는 선택이며, IaaS, PaaS, SaaS 중 무엇을 쓰든 남는 책임의 경계를 정의하는 것이 핵심.
- 시사점 : 모델 선택은 비용보다 책임 경계와 벤더 종속 위험을 먼저 따져야 하므로, 도입 전에 관리 책임표를 작성해 보안·운영 조직이 함께 승인해야 함.
