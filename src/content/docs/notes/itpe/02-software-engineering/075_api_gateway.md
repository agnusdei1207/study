---
title: "API Gateway (API: Application Programming Interface)"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- API Gateway, 마이크로서비스 아키텍처(MSA, Microservice Architecture), 단일 진입점(Single Point of Entry), 리버스 프록시(Reverse Proxy)
- 동적 라우팅, BFF(Backend For Frontend), Rate Limiting, 서킷 브레이커(Circuit Breaker), SPOF(Single Point of Failure), JWT(JSON Web Token)

## Ⅰ. API Gateway의 개요

- 핵심 요약 : 모든 외부 요청을 단일 진입점으로 수용하여 라우팅과 공통 횡단 관심사를 일괄 처리하는 리버스 프록시 기반 미들웨어.
- 개념 : 마이크로서비스 아키텍처(MSA, Microservice Architecture) 및 분산 클라우드 환경에서 모든 외부 클라이언트(Web, Mobile, 3rd Party)의 요청을 단일 진입점(Single Point of Entry)으로 수용하여, 적절한 내부 백엔드 마이크로서비스로 라우팅하고 공통 횡단 관심사를 일괄 처리하는 리버스 프록시(Reverse Proxy) 기반 미들웨어(API, Application Programming Interface).
- 배경 및 필요성 : 수십~수백 개의 마이크로서비스 엔드포인트를 클라이언트가 직접 호출할 때 발생하는 네트워크 오버헤드, 복잡한 인증/보안 처리, 프로토콜 불일치, 엔드포인트 노출 리스크의 원천 해결.
- 대표 솔루션 : Spring Cloud Gateway, Kong, Apigee, AWS(Amazon Web Services) API Gateway, Envoy.

## Ⅱ. API Gateway의 특징

- 핵심 요약 : 인증, 트래픽 제어, 장애 격리, 동적 라우팅, 프로토콜 변환 등 인프라 횡단 관심사의 일원화.

1. 인증 및 인가 : JWT(JSON Web Token) 검증, OAuth 2.0 기반 토큰 처리의 일원화.
2. 트래픽 제어 : Rate Limiting 및 Throttling을 통한 백엔드 서비스 보호.
3. 장애 격리 : 서킷 브레이커(Circuit Breaker, Resilience4j) 기반 연쇄 장애 차단.
4. 동적 라우팅 및 로드밸런싱 : Eureka, Consul, K8s(Kubernetes) DNS(Domain Name System) 연동을 통한 백엔드 파드 인스턴스 IP(Internet Protocol) 동적 감지 및 트래픽 분산.
5. 프로토콜 변환 및 캐싱 : REST(Representational State Transfer)와 gRPC 간 변환, 응답 캐싱.
6. BFF(Backend For Frontend) 패턴 구현 : 웹 전용, 모바일 전용 등 클라이언트 특성에 최적화된 게이트웨이 다변화 및 필요 데이터 조합(Aggregation) 제공.

## Ⅲ. API Gateway의 구조 (흐름)

- 핵심 요약 : 클라이언트의 모든 요청이 게이트웨이의 공통 기능 계층을 통과한 뒤 사설 네트워크의 백엔드 서비스로 분기.
- 단일 진입점 기반 요청 처리 흐름.

```text
[ 클라이언트 (Web / Mobile App) ]
   │
   ▼
[ API Gateway : 단일 진입점 ]
 - 인증 및 인가 (JWT 검증, OAuth 2.0)
 - 트래픽 제어 (Rate Limiting, Throttling)
 - 장애 격리 (Circuit Breaker: Resilience4j)
 - 동적 라우팅 (서비스 디스커버리 연동)
 - 프로토콜 변환 (REST <-> gRPC), 응답 캐싱
   │
   ├─────── 사설 네트워크 라우팅 ───────┐
   ▼                                   ▼
[ Order Service ]          [ Payment Service ]
```

## Ⅳ. 주요 오픈소스 API Gateway 솔루션의 비교

- 핵심 요약 : 기반 기술과 성능·확장성·적합 환경이 상이한 Spring Cloud Gateway, Kong, AWS API Gateway의 선택 기준.

| 비교 항목 | Spring Cloud Gateway | Kong Gateway | AWS API Gateway |
|---|---|---|---|
| 기반 기술 | Java / Netty (Non-blocking 리액티브) | Nginx / Lua (OpenResty) | AWS 완전 관리형 서버리스 |
| 처리 성능 | 우수 (리액티브 비동기 이벤트 루프) | 최고 (C/Nginx 기반 초저지연) | 클라우드 인프라의 자동 오토스케일링 |
| 확장성 | Java 코딩 기반 커스텀 필터 구현 용이 | 다양한 플러그인 생태계 (Lua, Go) | Lambda 연동, 콘솔 기반 구성 |
| 적합 환경 | Spring 생태계 기반 엔터프라이즈 MSA | 대규모 고성능 트래픽, 폴리글랏 환경 | 클라우드 네이티브 서버리스 아키텍처 |

## Ⅴ. API Gateway의 장점과 한계

- 핵심 요약 : 엔드포인트 은닉과 공통 정책 일원화의 이점, 단일 장애점과 Fat Gateway 변질의 한계.
- 장점

  1. 백엔드 엔드포인트 은닉을 통한 공격 표면 축소 및 클라이언트 로직 단순화.
  2. 인증, 트래픽 제어, 로깅 등 공통 정책의 단일 지점 일관 적용.
  3. 프로토콜 불일치 흡수와 클라이언트별 응답 최적화(BFF) 동시 달성.
- 한계점 1 : 단일 장애점(SPOF, Single Point of Failure) 위험 및 네트워크 홉(Hop) 추가에 따른 레이턴시
  - 한계점 : 모든 인바운드 트래픽의 게이트웨이 집중으로 장애 시 전사 서비스 중단 및 추가 프록시 계층에 따른 응답 지연 발생.
  - 해결 방안 : 다중 가용영역(Multi-AZ) 액티브-액티브 클러스터링 및 DNS 기반 GSLB(Global Server Load Balancing) 구성, eBPF 및 Envoy 기반 고성능 비동기 Non-blocking I/O 엔진 채택.
- 한계점 2 : 게이트웨이 내 비즈니스 로직 침투로 인한 'Fat Gateway' 변질
  - 한계점 : 인증, 라우팅을 넘어선 비즈니스 데이터 결합·변환 로직의 과다 구현으로 유지보수성과 배포 민첩성 저하.
  - 해결 방안 : 게이트웨이의 인프라 횡단 관심사(TLS(Transport Layer Security), Rate Limit, Auth) 집중, 클라이언트별 화면 조합 로직의 BFF 패턴 분리.
- 한계점 3 : 분산 환경에서의 인증 토큰 검증 병목
  - 한계점 : 대규모 초당 요청(TPS, Transactions Per Second) 발생 시 중앙 인증 서버 동기 검증에 따른 인증 서버 부하 및 병목 유발.
  - 해결 방안 : 비대칭키 기반 자기 완비형 JWT(JSON Web Token) 도입을 통한 게이트웨이 로컬 공개키 캐싱 검증, Redis 기반 세션 블랙리스트 초고속 비동기 조회 체계 결합.

## Ⅵ. 고가용성 API 게이트웨이 구축을 위한 기술사적 제언

- 핵심 요약 : 다중 가용영역 이중화와 분산 서킷 브레이커 격리 설계의 병행.
- 단일 장애점(SPOF) 방지를 위한 L4/L7 이중화 구성.

```text
[ 클라이언트 ]
      │
      ▼
[ GSLB / DNS 라우팅 ]
      │
      ▼
[ L4/L7 로드밸런서 (AWS ALB 등) ]
      │
 ┌────┴─────┐
 ▼          ▼
[ GW AZ-1 ] [ GW AZ-2 ]
(액티브-액티브, 오토스케일링 그룹)
 └────┬─────┘
      ▼
[ 백엔드 마이크로서비스 + Circuit Breaker ]
```

- 단일 장애점(SPOF) 방지를 위한 인프라 이중화 : API Gateway 다운 시 전체 비즈니스 마비 가능성에 대비하여 게이트웨이 인스턴스 전면의 로드밸런서 배치 및 멀티 AZ 오토스케일링 그룹 구성 필수.
- 분산 서킷 브레이커(Circuit Breaker)를 통한 연쇄 장애(Cascading Failure) 차단 : 특정 하위 서비스 장애 시 게이트웨이 스레드 고갈 방지를 위한 호출 타임아웃의 1~2초 이내 엄격 설정 및 즉각적 폴백(Fallback) 캐시 응답 반환 격리 설계 수립.

## Ⅶ. 결론

- 핵심 요약 : API Gateway는 MSA의 진입점 표준이자 공통 인프라 정책의 집행 지점.
- 요약 : 단일 진입점을 통한 라우팅, 보안, 트래픽 제어의 일원화로 분산 시스템 복잡도를 클라이언트로부터 은닉하는 구조.
- 시사점 : 이중화 기반 고가용성 확보, Fat Gateway 방지 역할 경계 유지, 토큰 검증 병목 최적화가 성공적 운영의 3대 조건.
