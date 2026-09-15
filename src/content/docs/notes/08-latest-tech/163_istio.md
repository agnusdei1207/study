---
sidebar:
  order: 163
  label: "163. 이스티오 (Istio)"
  badge:
    text: "기출 · 50%"
    variant: note
title: "이스티오 (Istio)"
date: "2026-09-15T11:20:00+09:00"
tags:
  - "notes-latest_tech"
weight: 163
extra:
  question_no: "163"
  source_status: "기출"
  source_history: "138회"
  priority: 50
  priority_note: "Istio 제어•데이터 평면 구조가 출제됨"
---

## Ⅰ. 개요

- **정의**: 쿠버네티스 환경에서 마이크로서비스 간의 트래픽 라우팅, 보안(mTLS), 복원력 및 전방위 관측성을 제공하는 CNCF 졸업 오픈소스 서비스 메시 플랫폼
- **배경 및 필요성**: 대규모 분산 파드 간 통신에서 수동 네트워크 설정은 mTLS 인증서 갱신 누락, 카나리 배포 설정 오류, 서비스 간 장애 연쇄 전파를 초래하므로, 중앙 제어면(Istiod)에서 정책을 일괄 계산하고 고성능 데이터면(Envoy Proxy/Ambient Mesh)으로 동적 배포하는 표준화된 관리 체계의 필요성 대두

## Ⅱ. 특징

- **단일 통합 제어면(Istiod)**: 과거 분산되어 있던 Pilot, Citadel, Galley를 단일 데몬인 Istiod로 통합하여 운영 복잡도 대폭 완화
- **동적 xDS 프로토콜**: Envoy 프록시와 gRPC 기반 xDS(LDS, RDS, CDS, EDS) 표준 API로 통신하여 무중단 동적 구성 갱신
- **제로 트러스트 보안 인프라**: 워크로드 단위 SPIFFE ID 부여 및 자동 인증서 발급/순환을 통해 무중단 STRICT mTLS 암호화 구현
- **유연한 데이터면 아키텍처**: 전통적인 파드별 사이드카(Sidecar) 방식과 노드 공유 기반의 사이드카리스(Ambient Mesh) 모드 동시 지원

## Ⅲ. 구조 및 구성요소

```text
[Istio 서비스 메시 아키텍처]
├── [Control Plane (Istiod)] ── Pilot (xDS 변환), Citadel (인증서 발급), Galley (설정 검증)
├── [Data Plane (Envoy)] ────── Sidecar 프록시 (파드 격리 L4/L7 집행)
├── [Data Plane (Ambient)] ──── ztunnel (노드 공유 L4 mTLS), Waypoint (서비스 단위 L7 프록시)
└── [트래픽 선언 CRD] ──────── VirtualService, DestinationRule, Gateway, PeerAuthentication
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 구성요소 | 설명 | 주요 역할 |
|:---|:---|:---|
| Istiod | 중앙 집중형 제어면 단일 프로세스 | K8s 리소스를 xDS 구성으로 변환(Pilot), CA 인증서 발급(Citadel), 설정 유효성 검증(Galley) |
| Sidecar Envoy | 파드마다 주입되는 고성능 C++ 프록시 | 파드 인바운드/아웃바운드 트래픽을 가로채어 L4/L7 정책, 서킷 브레이커, mTLS 집행 |
| Ambient ztunnel | 노드당 1개 실행되는 공유 L4 프록시 | HBONE(HTTP-based Overlay) 프로토콜을 이용해 노드 간 제로 트러스트 L4 mTLS 터널 구축 |
| Ambient Waypoint | 특정 네임스페이스/서비스 전용 L7 프록시 | HTTP 헤더 조작, 세분화된 L7 인가, 카나리 라우팅이 필요한 경우에만 선택적으로 경유 |
| 선언적 CRD | 사용자가 정의하는 Istio 사용자 정의 리소스 | VirtualService(라우팅 규칙), DestinationRule(로드밸런싱/서킷브레이크), PeerAuthentication(mTLS 모드) |

## Ⅳ. 흐름도

```text
[CRD 정책 정의 및 적용] (① VirtualService, DestinationRule 선언 매니페스트 제출)
│
▼
[Istiod xDS 동적 변환] (② Istiod가 쿠버네티스 엔드포인트와 정책을 취합하여 xDS 구성 생성)
│
▼
[데이터면 구성 동기화] (③ Envoy 프록시 또는 ztunnel/Waypoint로 xDS 구성 및 SPIFFE 인증서 배포)
│
▼
[인바운드/아웃바운드 가로챔] (④ iptables 또는 eBPF 규칙을 통해 워크로드 네트워크 트래픽 가로챔)
│
▼
[L4 mTLS 및 L7 정책 집행] (⑤ 프록시 간 mTLS 상호 인증, 가중치 라우팅 및 서킷브레이크 적용)
│
▼
[원격 텔레메트리 전송] (⑥ 지연시간, 에러율 메트릭(Prometheus) 및 분산 추적 스팬(Jaeger) 전송)
```

- 분기 결과: mTLS 검증 실패 또는 서킷 브레이커 임계치 초과 시 연결 즉시 차단, 정상 통과 시 대상 워크로드 파드로 무중단 트래픽 전달

## Ⅴ. 종류 및 비교

| 구분 | Sidecar 모드 | Ambient ztunnel 모드 | Ambient ztunnel + Waypoint |
|:---|:---|:---|:---|
| 배포 방식 | 모든 파드마다 Envoy 프록시 주입 | 노드당 1개의 DaemonSet ztunnel 배포 | ztunnel + 네임스페이스당 Waypoint 프록시 |
| 지원 프로토콜 계층 | L4 전송 계층 + L7 응용 계층 전체 | L4 전송 계층 (mTLS 암호화 및 L4 인가) | L4 mTLS 터널 + L7 완전한 애플리케이션 정책 |
| 메모리/CPU 오버헤드 | 파드 수에 비례하여 선형적 증가 (큼) | 노드당 고정 오버헤드로 극소화 (매우 낮음) | L7 검사가 필요한 서비스에만 국소적 비용 부과 |
| 애플리케이션 침투성 | 파드 재기동 필요 (사이드카 주입) | 애플리케이션 파드 수정 및 재기동 완전 불필요 | 파드 재기동 없이 라벨 지정만으로 동적 연결 |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 효과 |
|:---|:---|:---|
| 대규모 클러스터에서 Istiod 메모리 고갈 및 xDS 지연 | Sidecar CRD 도입을 통한 네임스페이스별 설정 범위 제한(exportTo) | 불필요한 엔드포인트 전파 차단 및 제어면 CPU/메모리 70% 절감 |
| 수천 개 파드에 사이드카 주입 시 클러스터 리소스 낭비 | Ambient Mesh 도입을 통해 L4 기본망과 L7 정책 계층 분리 | 파드당 사이드카 메모리 오버헤드 원천 제거 |
| 잘못된 가중치 라우팅 설정 시 전면 장애 확산 | istioctl analyze 사전 정적 분석 및 카나리 점진적 배포 적용 | 매니페스트 문법 오류 사전 차단 및 안정적 트래픽 전환 |

## Ⅶ. 결론

- **기술 위상/발전**: 쿠버네티스 기반 클라우드 네이티브 서비스 메시의 절대적 사실상 표준으로 자리 잡았으며 최근에는 사이드카 오버헤드를 근본적으로 해소하는 Ambient Mesh 아키텍처로의 전환이 가속화되는 추세
- **실무 적용/통제**: L4 전송 암호화는 Ambient ztunnel로 표준화하고 정교한 HTTP L7 조작이 요구되는 도메인에만 Waypoint 프록시를 결합하며, Sidecar CRD 기반의 xDS 범위 통제를 적용한 고효율 운영 아키텍처 수립 필수
