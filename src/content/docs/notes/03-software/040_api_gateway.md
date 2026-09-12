---
sidebar:
  order: 40
  label: "040. API 게이트웨이"
  badge:
    text: "기출 · 50%"
    variant: note
title: "API 게이트웨이 (API Gateway)"
date: "2026-09-07T10:00:00+09:00"
tags:
  - "notes-software"
weight: 40
extra:
  question_no: "040"
  source_status: "기출"
  source_history: "120회"
  priority: 50
  priority_note: "120회 기출, API 진입점•정책 집중 구조"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **API 게이트웨이(API Gateway)**: 클라이언트와 마이크로서비스들 사이에 위치하여 인증/인가, L7 라우팅, 로드밸런싱, 트래픽 제한을 단일 지점에서 전담하는 리버스 프록시.
- **횡단 관심사(Cross-Cutting Concerns)**: 인증, 로깅, 모니터링, SSL 종료, Rate Limiting 등 모든 서비스에 공통으로 필요한 기능.

</details>

- 정의/개념: 외부 클라이언트와 마이크로서비스 간 경계에서 **L7 동적 라우팅, 인증/인가(JWT), 트래픽 제어(Rate Limiting)** 를 일원화하는 단일 진입점 프록시
- 배경/필요성: 외부 클라이언트의 분산 서비스 직접 호출 시 발생하는 **내부 토폴로지 노출 및 횡단 관심사 중복 구현 비효율 한계**

#### 한줄 요약
- MSA 외부 요청의 단일 진입점으로 인증, 라우팅, 보안 및 트래픽 제어를 집중 처리한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **Rate Limiting(속도 제한)**: 토큰 버킷(Token Bucket) 등의 알고리즘으로 클라이언트별 초당 요청 수를 제한하여 백엔드 과부하를 방어하는 기제.
- **BFF(Backend For Frontend)**: 모바일 앱, 웹 브라우저 등 클라이언트 플랫폼별로 최적화된 API 게이트웨이를 분리 구축하는 패턴.

</details>

- 내부 마이크로서비스의 위치를 은닉하는 **단일 진입점(Single Entry Point)** 제공
- **인증(JWT 검증)·트래픽 제어(Rate Limiting)·SSL 종단(Termination)** 등 횡단 관심사 중앙화
- 플랫폼별(Web, iOS, Android) 데이터 애그리게이션을 지원하는 **BFF 패턴(Backend For Frontend)** 지원

#### 한줄 요약
- 단일 진입점은 횡단 관심사를 한 곳에 모으는 대신 모든 트래픽이 한 지점을 지나게 하므로, 중앙화의 이득과 병목 위험이 같은 성질에서 나온다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **필터 체인(Filter Chain)**: 요청이 인입되어 라우팅되기 전후에 Pre-Filter(인증/로깅), Routing-Filter, Post-Filter(응답 가공)를 거치는 파이프라인.

</details>

```text
[API 게이트웨이 파이프라인]
  │
  ├─ [SSL 종단기] (HTTPS 복호화·CPU 부하 절감)
  │
  ├─ [인증/인가 엔진] (JWT/OAuth 검증·엣지 차단)
  │
  ├─ [트래픽 제어기] (Token Bucket·Rate Limiting)
  │
  └─ [동적 라우터] (URI 매핑·백엔드 디스패치)
```
- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| SSL 종단기 | HTTPS 암호화를 게이트웨이에서 해제하여 내부 백엔드 CPU 부하 절감 |
| 인증/인가 엔진 | OAuth 2.0 / JWT 서명을 검증하고 미인증 요청을 **엣지(Edge)에서 즉시 차단** |
| 트래픽 제어기 | **Token Bucket / Leaky Bucket** 기반 클라이언트별 Rate Limiting 강제 |
| 동적 라우터 | URI 패스(`/api/orders/**`) 및 서비스 레지스트리를 조회하여 백엔드로 디스패치 |

#### 한줄 요약
- 필터 파이프라인이 순서를 가진 계층이므로, 인증·트래픽 제어·라우팅의 배치 순서가 곧 게이트웨이의 보호 강도와 처리 비용을 정한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **토큰 버킷(Token Bucket)**: 고정된 용량의 버킷에 일정 주기로 토큰을 채우고 요청 시 토큰을 소모하여 버킷이 비면 429 Too Many Requests를 반환하는 알고리즘.

</details>

```text
[API 게이트웨이 요청 처리 흐름] (진행 ①→⑤, 인증·속도 제한 실패 시 백엔드 도달 전 엣지 차단)
  │
  ├─ [요청 인입] (① 클라이언트 HTTPS 호출(GET /api/v1/orders/10 등), SSL/TLS 종단 및 HTTP 복호화)
  │
  ├─ [인증 검증] (② JWT 토큰 서명 유효성·만료 검증, 실패 시 401 Unauthorized 반환)
  │
  ├─ [속도 제한] (③ 토큰 버킷 기반 Rate Limiting 검사, 초과 시 429 Too Many Requests 반환)
  │
  ├─ [라우팅] (④ 서비스 디스커버리 조회로 인스턴스 IP/Port 확인 후 로드밸런싱 적용해 대상 마이크로서비스로 전달)
  │
  └─ [응답 처리] (⑤ 백엔드 응답 수신 후 사후 필터(CORS 헤더 추가 등) 처리해 클라이언트 반환)
```

분기 결과: 차단 갈래는 ②③에서 401·429를 즉시 반환하므로 유효성 검증 비용만 치르고 백엔드 보호를 얻고, 통과 갈래는 **토큰 버킷**의 토큰을 하나 더 소모해 실제 트랜잭션 처리 비용까지 지불하므로, 필터 순서가 인증·속도 제한보다 라우팅에 뒤처지면 비정상 요청이 백엔드에 닿은 뒤에야 걸러져 막아내는 부하가 달라진다

#### 한줄 요약
- 인증과 Rate Limiting이 라우팅보다 앞에 놓여야 비정상 요청이 백엔드에 닿기 전에 걸러지므로, 필터 순서가 곧 게이트웨이가 막아내는 부하의 크기가 된다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **Spring Cloud Gateway vs Kong vs AWS API Gateway**: Spring 생태계 전용 Netty 게이트웨이, C/Lua 기반 초고성능 Kong, 완전 관리형 클라우드 서비스 AWS API Gateway.

</details>

| 구현 솔루션 | 기반 기술 스택 | 핵심 특징 | 주 적용 환경 |
|:---|:---|:---|:---|
| Spring Cloud Gateway | Java / Spring WebFlux (Netty) | Spring 생태계 완벽 통합, 비동기 논블로킹 | Java/Spring 백엔드 엔터프라이즈 |
| Kong Gateway | Nginx / OpenResty / Lua | **초저지연, 수만 RPS 초고성능**, 풍부한 플러그인 | 폴리글랏 환경, 대규모 글로벌 트래픽 |
| AWS API Gateway | AWS 완전 관리형 클라우드 | 서버리스 연동(Lambda), 인프라 관리 0화 | AWS 클라우드 네이티브 서버리스 |
| Envoy Proxy | C++ | 초경량 고성능, Service Mesh 사이드카 표준 | Kubernetes 이스티오(Istio) 인프라 |

#### 한줄 요약
- Java 환경은 Spring Cloud Gateway, 고성능 폴리글랏은 Kong, 서버리스는 AWS API Gateway를 채택한다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **SPOF(Single Point of Failure)**: 단일 API 게이트웨이 인스턴스가 다운되면 전체 시스템 접근이 전면 차단되는 단일 장애점 위험.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 단일 게이트웨이 장애 시 전사 서비스 마비(**SPOF**) | 앞단에 **L4 로드밸런서(ALB) 및 게이트웨이 Multi-AZ 오토스케일링** | 단일 인스턴스 무관 99.99% 고가용성 보장 |
| 게이트웨이에 비즈니스 로직 구현으로 성능 병목(Fat Gateway) | 비즈니스 로직 금지 및 **순수 횡단 관심사(인증/라우팅)** 만 격리 | 게이트웨이 경량화 및 5ms 이내 처리 지연 유지 |
| 악의적 크롤러/DDoS 공격으로 백엔드 리소스 고갈 | **Redis 기반 분산 Rate Limiting + IP 블랙리스트 WAF 연동** | 비정상 트래픽 엣지 차단 및 백엔드 보호 |
| 다중 서비스 응답 조합 시 네트워크 오버헤드 | 플랫폼별 전용 게이트웨이를 분리하는 **BFF(Backend For Frontend) 패턴** | 모바일 맞춤형 응답 압축 및 레이턴시 단축 |

#### 한줄 요약
- 게이트웨이는 횡단 관심사를 한 곳에 모으는 대신 단일 관문을 병목이자 실패점으로 만들므로, L4 다중화로 가용성을 되사고 비즈니스 로직은 올리지 않아 관문이 비대해지지 않게 한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **쿠버네티스 게이트웨이 API(Kubernetes Gateway API)**: 기존 Ingress의 표현력 한계를 극복하고 인프라 관리자, 클러스터 운영자, 개발자 간의 역할을 분리하여 L4/L7 라우팅을 선언적으로 제어하는 차세대 표준 규격.
- **웹 애플리케이션 방화벽(Web Application Firewall, WAF)**: SQL Injection, XSS 등 애플리케이션 계층의 웹 취약점 공격과 비정상 트래픽을 엣지에서 실시간 탐지·차단하는 보안 솔루션.
- **다중 가용 영역(Multi-Availability Zone, Multi-AZ)**: 단일 데이터센터 장애에 대비하여 지리적으로 분리된 둘 이상의 독립 가용 영역에 인스턴스를 분산 배치하는 고가용성 인프라 구성.

</details>

- **차세대 발전 전망**: 클라우드 네이티브 환경에서 **쿠버네티스 게이트웨이 API** 표준 채택과 함께, **웹 애플리케이션 방화벽(WAF)** 및 서비스 메시 인그레스 프록시와 통합된 지능형 엣지 보안 게이트웨이로 진화 추세.
- **실무 공학적 통찰**: **단일 장애점(SPOF)** 리스크를 해소하기 위해 **다중 가용 영역(Multi-AZ)** 기반 분산 배치를 강제하고, 비즈니스 로직이 침투하는 비대 게이트웨이(Fat Gateway)를 방지하여 순수 횡단 관심사만 격리하는 엄격한 아키텍처 거버넌스 확립 필요.

#### 한줄 요약
- API 게이트웨이는 쿠버네티스 Gateway API 및 WAF 통합 엣지 보안으로 진화하되, Multi-AZ 다중화와 Fat Gateway 방지를 위한 횡단 관심사 격리가 신뢰성의 핵심이다.
