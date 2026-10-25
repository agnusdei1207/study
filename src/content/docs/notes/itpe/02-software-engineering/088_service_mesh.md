---
title: "서비스 메시(Service Mesh)"
description: "사이드카·데이터/컨트롤 플레인·mTLS·East-West, API Gateway 비교, 오버헤드·복잡성·조기 도입 한계와 방안"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드

- 서비스 메시(Service Mesh), 사이드카 패턴(Sidecar Pattern), mTLS(mutual Transport Layer Security), East-West 트래픽, Istio, Envoy
- 데이터 플레인(Data Plane), 컨트롤 플레인(Control Plane), API Gateway, 제로 트러스트(Zero Trust), 사이드카리스(Sidecarless)

## Ⅰ. 서비스 메시의 개요

- 핵심 요약 : 애플리케이션 코드를 고치지 않고 MSA 서비스 간 통신의 보안과 관측성을 인프라 계층에서 처리하는 전용 통신 계층.
- 개념 : 마이크로서비스 아키텍처(MSA, Microservice Architecture)에서 서비스 간 통신(East-West 트래픽)을 안전하게 중계하기 위해, 비즈니스 코드 수정 없이 인프라 계층에서 서비스 디스커버리, 로드밸런싱, 암호화, 트래픽 라우팅, 관측성을 제공하는 **서비스 메시** (Service Mesh).
- 배경 및 필요성 : 서비스가 수백 개로 늘면 Netflix Eureka, Ribbon, Hystrix 같은 통신 라이브러리를 서비스마다 내장해야 해, 다중 언어(Polyglot) 환경에서 언어 종속성과 프레임워크 유지보수 부담이 커짐.
- 핵심 패턴 : **사이드카 패턴** (Sidecar Pattern)과 **데이터 플레인** (Data Plane)·**컨트롤 플레인** (Control Plane)의 분리.

## Ⅱ. 서비스 메시의 특징 및 장점

- 핵심 요약 : 코드 비침습성, 플레인 분리, mTLS 보안, 정교한 트래픽 제어와 관측성이 결합된 인프라 기능 묶음.

1. 코드 비침습성 : 애플리케이션 수정 없이 통신 기능을 부여 → 도입 비용과 변경 부담 감소.
2. 사이드카 주입 : 각 파드에 **Envoy** 프록시를 붙여 서비스 간 트래픽을 가로챔 → 모든 서비스에 같은 통신 정책 적용.
3. 플레인 분리 : 데이터 플레인과 컨트롤 플레인이 역할을 나누고, xDS(x Discovery Service) API로 설정을 동기화 → 중앙 정책의 일관된 배포.
4. **mTLS** (mutual Transport Layer Security) 인증 : 양방향 인증서로 서비스 신원을 확인하고 인가 정책(AuthorizationPolicy)으로 접근을 제어 → 내부 통신 보안 강화.
5. 트래픽 셰이핑 : 카나리 라우팅, 서킷 브레이킹 등으로 트래픽을 세밀히 분배 → 장애 전파 억제와 안전한 배포.
6. 관측성(Observability) 내장 : 메트릭과 트레이스를 자동 수집 → 장애 원인 추적 시간 단축.

## Ⅲ. 서비스 메시의 구조 (흐름)

- 핵심 요약 : 컨트롤 플레인의 정책 배포와 사이드카 프록시 사이의 mTLS 데이터 전송이 이루는 이중 구조.

```text
[ 컨트롤 플레인 (Istiod) ]
   ↓ xDS로 정책·인증서 배포
[ 파드 A : 앱 + Envoy 사이드카 ]
   ↓ mTLS 암호화 통신 (데이터 플레인)
[ 파드 B : 앱 + Envoy 사이드카 ]
```

- 데이터 플레인은 사이드카 프록시가 인·아웃바운드 패킷을 가로채 암호화, 서킷 브레이킹, 메트릭 수집을 수행하는 영역.
- 컨트롤 플레인은 Istiod가 라우팅 규칙과 인증서를 중앙에서 관리하고 xDS로 프록시와 동기화하는 영역.

## Ⅳ. API Gateway와 서비스 메시의 비교

- 핵심 요약 : 외부 진입(North-South) 제어와 내부 서비스 간(East-West) 제어를 나누어 맡는 역할 분담 구조.
- 구분 : 외부 진입을 담당하는 **API Gateway** (API(Application Programming Interface) 관문)와 내부 통신을 담당하는 서비스 메시는 트래픽 방향과 배치 위치가 다름.

```text
[ 외부 클라이언트 ]
   ↓ North-South 트래픽
[ API Gateway ]
   ↓ 내부 진입
[ 서비스 A ] ⇄ [ 서비스 B ]
   East-West 트래픽 (서비스 메시)
```

| 비교 항목 | API Gateway | Service Mesh |
| --- | --- | --- |
| 주요 트래픽 방향 | North-South (외부 클라이언트에서 내부 백엔드) | East-West (내부 마이크로서비스 간) |
| 핵심 책임 | 인증·인가(OAuth 2.0(Open Authorization 2.0), JWT(JSON Web Token)), Rate Limiting, API 관리 | 서비스 간 보안(mTLS), 트래픽 셰이핑, 카나리 라우팅, 관측성 |
| 배포 위치 | 시스템 외곽 경계 | 각 애플리케이션 파드 내부(사이드카) |
| 대상 클라이언트 | 웹 브라우저, 모바일 앱, 외부 제휴 시스템 | 같은 클러스터 안의 다른 마이크로서비스 |
| 대표 솔루션 | Kong, Spring Cloud Gateway, Apigee | Istio, Linkerd, Consul Connect, Cilium |

## Ⅴ. 서비스 메시의 한계와 방안

- 핵심 요약 : 코드 무수정 보안과 관측성의 장점 아래, 리소스 오버헤드, 설정 복잡성, 조기 도입의 부담이라는 한계가 존재.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 사이드카 오버헤드 | 파드마다 프록시가 추가되어 CPU·메모리 소모가 늘고 네트워크 홉과 핸드셰이크로 지연 증가 | **사이드카리스** (Sidecarless) 아키텍처(Istio Ambient Mesh, Cilium Service Mesh) 검토, eBPF(extended Berkeley Packet Filter) 기반 커널 가속 | 파드당 리소스 사용량, 요청 지연 시간 |
| 설정 복잡성 | VirtualService, DestinationRule 등 구성 리소스가 늘고 설정 충돌과 분산 디버깅 난도 급상승 | GitOps 기반 설정 버전 관리, Istio Analyze와 Kiali 토폴로지 시각화, 사전 검증 CI 강제 | 설정 충돌 건수, 배포 실패율 |
| 조기 도입과 역량 부족 | 서비스 수와 트래픽 복잡도 기준의 도입 타당성 체크리스트, 점진적 전환 | 운영 공수 대비 효과 평가 | 운영 공수 대비 효과 평가 |

## Ⅵ. 엔터프라이즈 도입을 위한 기술사적 제언

- 핵심 요약 : 사이드카 오버헤드를 선별 적용으로 통제하고, 제로 트러스트 보안 원칙을 전면 적용하는 방향.
- 모든 파드에 프록시를 두기보다 트래픽이 많거나 보안 요구가 높은 서비스부터 선별 적용하고, eBPF 기반 사이드카리스 구조의 도입 가능성을 주기적으로 검토하는 것이 바람직하다.
- 내부 사설망을 신뢰하지 않는 **제로 트러스트** (Zero Trust) 원칙에 따라 mTLS 인증서 자동 교환과 인가 정책을 전 서비스에 적용하여, 내부 횡적 이동(Lateral Movement) 공격을 차단할 필요가 있다.

## Ⅶ. 결론

- 핵심 요약 : 서비스 메시는 MSA 내부 통신의 보안·신뢰성·관측성을 담당하는 인프라 계층.
- 시사점 : API Gateway의 North-South 제어와 서비스 메시의 East-West 제어가 상호 보완하며, 도입 타당성 평가와 점진적 전환이 성공의 전제 조건.