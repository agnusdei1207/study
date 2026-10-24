---
title: "TA와 AA 역할 비교 및 협업 (TA: Technical Architect; AA: Application Architect)"
author: "agnusdei1207"
date: "2026-10-24T23:57:08+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 테크니컬 아키텍트(TA, Technical Architect), 애플리케이션 아키텍트(AA, Application Architect), 비기능 요구사항(NFR, Non-Functional Requirement)
- RACI 매트릭스, ARB(Architecture Review Board), ADR(Architecture Decision Record), ATAM(Architecture Tradeoff Analysis Method), 플랫폼 엔지니어링

## Ⅰ. TA와 AA의 개요

- 핵심 요약 : 인프라와 플랫폼을 총괄하는 **테크니컬 아키텍트**(TA, Technical Architect)와 업무 애플리케이션 구조를 총괄하는 **애플리케이션 아키텍트**(AA, Application Architect)가 역할을 나눠 맡는 체계.
- 개념 : 대규모 엔터프라이즈 프로젝트에서 인프라, 미들웨어, 플랫폼 아키텍처를 맡는 TA와 도메인 및 애플리케이션 아키텍처를 맡는 AA를 분리해 두는 전문 아키텍트 역할 체계다.
- 배경 및 필요성 : 업무 로직이 복잡해지고 클라우드와 컨테이너 같은 하부 기술이 고도화되면서, 한 명의 아키텍트가 두 영역을 모두 통제하기 어려워졌다. 책임과 전문성을 구조적으로 나눌 필요가 생긴 것이다.
- 주요 목적 : 업무 요건을 정밀하게 구현하는 AA의 설계와, 성능과 가용성과 보안을 충족하는 TA의 실행 기반이 맞물리도록 하는 것.

## Ⅱ. TA와 AA의 특징 및 장점

- 핵심 요약 : AA는 기능적 구조, TA는 실행 환경과 비기능 품질을 맡고, 두 영역이 만나는 접점에서 협업하는 구조.

1. AA의 주안점 : 업무 로직과 기능 요구(FR, Functional Requirement) 중심의 애플리케이션 설계 → 도메인 구현의 정밀성 확보.
2. TA의 주안점 : 실행 환경과 비기능 요구(NFR, Non-Functional Requirement) 중심의 인프라·미들웨어·플랫폼 설계 → 운영 안정성 확보.
3. 협업 접점 : 트랜잭션 격리수준, 분산 락, 캐싱 전략, 처리량·지연 목표(TPS, Transactions Per Second, Latency), REST와 gRPC 메시지 규격, API(Application Programming Interface) 게이트웨이 라우팅을 두 영역이 함께 정함 → 기능과 성능의 동시 충족.
4. 전문성 분리 효과 : 역할을 나눠 맡으므로 각 영역의 깊이를 확보하고, 접점 협의로 전체 정합성을 유지.

## Ⅲ. TA와 AA의 구조 (흐름)

- 핵심 요약 : AA의 애플리케이션 영역과 TA의 인프라 영역이 협업 접점을 사이에 두고 연결되는 계층 구조.

```text
[ AA 영역 : 애플리케이션 ]
  도메인 모델링, 서비스 인터페이스
        ↓
[ 협업 접점 : 비기능 요구 ]
  격리수준, 캐싱, 목표 지연 시간
        ↓
[ TA 영역 : 인프라와 플랫폼 ]
  클라우드, 네트워크, 보안, 고가용성
```

```text
[ 협업 거버넌스 흐름 ]

비즈니스 요건 정의 (AA)
        ↔ NFR 목표 정의 (TA)
        ↓ 공동 품질속성 워크숍
ARB 검토 (아키텍처 검토 위원회)
        ↓
ADR 기록 (아키텍처 결정 기록)
        ↓
설계·구현 후 ATAM으로 트레이드오프 평가
```

- 약어 풀이 : WAF(Web Application Firewall), IAM(Identity and Access Management), APM(Application Performance Monitoring), CI/CD(Continuous Integration/Delivery)는 TA 영역의 보안과 관측성, 배포 자동화를 가리킨다.

## Ⅳ. TA와 AA의 비교

- 핵심 요약 : 주안점, 관리 대상, 산출물, 기술 스택, 성과 지표가 서로 대비되는 상호 보완적 역할.

| 비교 항목 | 테크니컬 아키텍트(TA) | 애플리케이션 아키텍트(AA) |
| --- | --- | --- |
| 주안점 | 실행 환경과 비기능 품질(NFR) | 업무 로직과 기능 구조(FR) |
| 관리 대상 | 서버, OS(Operating System), 네트워크, K8s(Kubernetes), WAS(Web Application Server), DB(Database), 클라우드 자원 | 도메인 엔티티, 유스케이스, API 명세, 공통 프레임워크 |
| 핵심 산출물 | 시스템 구성도, 네트워크 구성도, 용량 산정서, DR(Disaster Recovery) 계획서 | 애플리케이션 아키텍처 설계서(SAD, Software Architecture Description), 공통 컴포넌트 명세서 |
| 기술 스택 예 | AWS(Amazon Web Services), Docker, Linux, Kafka, Terraform | Java와 Spring, JPA(Java Persistence API), DDD(Domain-Driven Design) |
| 성과 지표 | 가용성 목표 달성률, 응답 지연, 보안 점검 결과 | 업무 요구 충족률, 코드 재사용률, 결합도와 응집도 |

## Ⅴ. TA와 AA 협업의 한계와 방안

- 핵심 요약 : 접점 영역의 책임 모호, 관점 충돌, 클라우드 환경의 역할 재편이라는 한계를 RACI, ARB와 ADR, 플랫폼 엔지니어링으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 접점 영역의 R&R 모호 | 커넥션 풀, 분산 트랜잭션, 메시지 큐 연동이 인프라와 애플리케이션 양쪽에 걸쳐 장애 시 책임 회피 발생 | **RACI** 매트릭스로 캐시·배치·메시징·성능의 오너십을 정하고 정례 기술 협의체 운영 | 장애 책임 불명확 건수 |
| 기능 유연성과 인프라 제약의 충돌 | AA는 잦은 업무 변경에 대응하려 계층을 늘리고, TA는 자원과 지연 제약을 이유로 이를 제한 | **ARB**(Architecture Review Board, 아키텍처 검토 위원회)를 상설 운영하고, 결정 내용을 **ADR**(Architecture Decision Record)로 남겨 트레이드오프를 합의 | 미합의 결정 건수 |
| 클라우드 네이티브에서의 역할 혼선 | 인프라가 코드(IaC, Infrastructure as Code)로 추상화되어 TA의 물리 인프라 업무가 줄고 개발 영역과 겹침 | TA는 내부 개발자 플랫폼(IDP, Internal Developer Platform)을 만드는 **플랫폼 엔지니어링**으로 전환, AA는 DDD 기반으로 서비스 경계 정의에 집중 | 역할 재정의 문서 반영 여부 |

## Ⅵ. 성공적인 프로젝트 수행을 위한 기술사적 제언

- 핵심 요약 : 프로젝트 초기에 NFR을 함께 확정하는 워크숍을 정례화하고, 데이터·보안 아키텍트까지 포함한 협력 체계를 세울 것.

1. 프로젝트 초기의 NFR 공동 워크숍 : 처리량, 복구 목표(RTO(Recovery Time Objective), RPO(Recovery Point Objective)), 동시성 제어 요건은 인프라와 로직이 함께 타협해야 하므로, 초기 단계에 ATAM(Architecture Tradeoff Analysis Method) 기반의 품질속성 워크숍을 열고 그 결과를 ADR로 먼저 남긴다.
2. 4자 협력 체계 : 데이터 아키텍트(DA, Data Architect)와 보안 아키텍트(SA, Security Architect)가 TA, AA와 분리되어 움직이면 쿼리 성능 병목과 보안 취약점이 생기므로, 정기 ARB 회의에 네 역할이 함께 참여해 구조적 정합성을 점검한다.

## Ⅶ. 결론

- 핵심 요약 : TA와 AA는 실행 기반과 업무 구조를 나눠 맡는 상호 보완적 역할 체계.
- 시사점 : 클라우드 네이티브 전환에 따라 접점의 책임을 명문화하고, 플랫폼 엔지니어링과 DDD 중심으로 역할을 다시 짜는 것이 필요하다.
