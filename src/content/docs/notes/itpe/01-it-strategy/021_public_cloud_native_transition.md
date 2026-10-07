---
title: "공공부문 클라우드 네이티브 전환"
author: "Antigravity"
date: "2026-10-01T22:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "Gemini 3.8 Flash"
---

## Ⅰ. 공공부문 클라우드 네이티브 전환의 개요

- 개념 : 공공 정보시스템을 **단순 인프라 이전** (Lift & Shift) 방식이 아닌, 설계 단계부터 클라우드의 장점을 극대화할 수 있도록 **마이크로서비스 아키텍처** (MSA, Microservice Architecture), 컨테이너, CI(Continuous Integration)/CD(Continuous Delivery), 데브옵스를 적용하여 전환하는 **행정 혁신 전략**
- 배경 및 필요성 : 대국민 서비스 장애(행정망 먹통 사태 등) 재발 방지, 트래픽 폭증 시 신속한 자동 확장(오토스케일링) 필요성, 레거시 모놀리식 시스템의 노후화 및 유지보수 한계 극복.
- 주요 목적 : 무중단 대국민 서비스 구현, 개발·배포 주기 획기적 단축, 장애 격리 및 시스템 복원력 확보, 클라우드 자원 활용 효율화.

## Ⅱ. 클라우드 네이티브의 4대 핵심 기술 요소

```text
       ┌──────────────────────── 클라우드 네이티브 ────────────────────────┐
       │                                                                  │
   [Microservices (MSA)]       ── 독립적 배포와 확장이 가능한 작은 단위 서비스 분할
       │
   [Containers & K8s(Kubernetes)]          ── 환경 일관성 및 경량 가상화를 위한 컨테이너 오케스트레이션
       │
   [CI/CD & DevOps]            ── 지속적 통합·배포 자동화 파이프라인 및 개발-운영 협업
       │
   [Declarative APIs & GitOps] ── 코드로 관리하는 인프라(IaC, Infrastructure as Code) 및 선언적 상태 동기화
       └──────────────────────────────────────────────────────────────────┘
```

## Ⅲ. 단순 클라우드 이전(Lift & Shift)과 클라우드 네이티브의 비교

| 비교 항목 | 단순 이전 (Lift & Shift, IaaS, Infrastructure as a Service) | 클라우드 네이티브 (Cloud Native, PaaS, Platform as a Service / CaaS, Containers as a Service) |
|---|---|---|
| **시스템 아키텍처** | 단일 모놀리식(Monolithic) 구조 유지 | 도메인 주도 설계(DDD, Domain-Driven Design) 기반 마이크로서비스(MSA) |
| **배포 및 확장** | VM(Virtual Machine) 단위 수동/느린 확장, 정기 배포 시 서비스 중단 | 파드(Pod) 단위 초 단위 오토스케일링, 무중단 카나리 배포 |
| **장애 영향도** | 한 모듈 장애 시 전체 시스템 다운 | 장애 격리(Fault Isolation), 서킷 브레이커 적용 |
| **데이터베이스** | 단일 통합 대용량 RDBMS (SPOF(Single Point of Failure) 존재) | 서비스별 독립 DB (Database per Service), 분산 트랜잭션 |
| **공공 조달 체계** | 기존 서버/스토리지 구매 규격 적용 | PaaS 기반 클라우드 서비스 이용료 계약 및 사용량 과금 |

## Ⅳ. 공공 클라우드 네이티브 전환 시 주요 한계점 및 해결 방안

- 망분리 규제 및 공공 보안 컴플라이언스 제약 :
  - 한계점 : 기존의 획일적 물리적 망분리 규제로 인해 최신 퍼블릭 SaaS 및 클라우드 PaaS 서비스 활용 불가.
  - 해결 방안 : 데이터 중요도에 따른 다층보안체계(MLS, Multi-Level Security) 전환, 제로 트러스트(Zero Trust) 기반 논리적 망분리 실증.
- 단순 Lift-and-Shift 이관으로 인한 비용 및 성능 비효율 :
  - 한계점 : 아키텍처 재설계 없이 기존 VM을 클라우드로 단순 복사하여 클라우드 네이티브의 탄력성 미활용 및 비용 폭증.
  - 해결 방안 : 컨테이너화(Docker/K8s), MSA(마이크로서비스), 서버리스 아키텍처 기반의 전면적 애플리케이션 리팩토링(Refactoring) 지원.
- 공공 IT(Information Technology) 담당자의 클라우드 엔지니어링 역량 부족 및 벤더 종속 :
  - 한계점 : 발주 기관의 데브옵스·클라우드 운영 노하우 부재로 특정 CSP(Cloud Service Provider, 클라우드 서비스 제공사) 종속 및 운영 관리 마비.
  - 해결 방안 : CNCF(Cloud Native Computing Foundation) 공인 표준 오픈소스 기술 스택 채택, 공공 전문 CSP/MSP(Managed Service Provider) 거버넌스 체계 수립 및 공공 IT 인력 역량 개발 의무화.

## Ⅴ. 공공 클라우드 네이티브 전환을 위한 기술사적 제언

- 점진적 전환 전략(Strangler Fig 패턴) 적용 : 대규모 공공시스템의 빅뱅 전환 위험을 방지하기 위해 대국민 접점 및 트래픽 변동이 심한 서비스부터 순차적으로 분리 전환.
- 분산 데이터 정합성 보장 방안 수립 : MSA 전환에 따라 분리된 DB 간 정합성을 위해 2단계 커밋(2PC, Two-Phase Commit) 대신 사가 패턴(Saga Pattern) 및 이벤트 기반 아키텍처(Kafka 등) 도입.
- 보안 및 규제 기준의 합리적 정비 : 클라우드 보안인증제(CSAP, Cloud Security Assurance Program) 등급제 세분화에 맞추어 국가 중요 데이터의 망분리 규제를 완화하고, 제로 트러스트(Zero Trust) 및 서비스 메시(mTLS) 기반 보안 아키텍처 적용.
