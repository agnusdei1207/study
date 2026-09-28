---
title: "OpenTelemetry(관측성 표준)"
description: "클라우드 네이티브 분산 시스템에서 추적(Trace), 지표(Metric), 로그(Log)를 수집·가공·전송하기 위한 벤더 중립 오픈소스 표준 프레임워크인 OpenTelemetry의 아키텍처 및 구현 전략"
author: "Antigravity"
date: "2026-09-28T18:35:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
    variant: "note"
extra:
  series: "itpe"
  topic: "02-software-engineering"
  sub_topic: "msa"
  order: 96
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

지식 위치: 소프트웨어공학 → 운영·관측성 → **OpenTelemetry(관측성 표준)**

---

## 30초 인출

- 본질: **OpenTelemetry (OTel)** 는 CNCF 주도하에 OpenTracing과 OpenCensus 프로젝트가 통합된 표준으로, 분산 환경의 3대 관측성 신호(M.E.L.T: Metrics, Events, Logs, Traces)를 계측(Instrument), 수집, 가공, 전송하기 위한 단일 벤더 중립적 API, SDK 및 Collector 프레임워크
- 메커니즘: 애플리케이션 OTel SDK 계측 → W3C TraceContext 기반 HTTP/gRPC 헤더 컨텍스트 전파 → OTLP 프로토콜 전송 → OTel Collector (Receiver $\rightarrow$ Processor $\rightarrow$ Exporter) 파이프라인 가공 → 다양한 APM 백엔드(Jaeger, Prometheus, Datadog)로 다중 내보내기
- 통찰: 특정 APM 상용 솔루션 에이전트에 대한 강결합은 벤더 락인과 마이그레이션 비용을 유발하므로 OTel 표준 계측과 수집기(Collector)의 테일 기반 샘플링(Tail-based Sampling)을 통해 전송 비용을 통제하고 인프라 유연성을 확보할 필요가 있음

<details>
<summary>핵심 용어</summary>

- **관측성 3대 기둥 (Observability Pillars)** : 시스템 내부 상태를 외부 출력으로 유추하기 위한 핵심 3대 신호인 지표(Metric), 분산 추적(Trace), 로그(Log)
- **OTel Collector** : 텔레메트리 데이터를 수신(Receiver), 배치/필터링/마스킹(Processor), 백엔드 전송(Exporter)하는 벤더 독립적 프록시 서버
- **OTLP (OpenTelemetry Protocol)** : Protobuf 기반 gRPC 및 HTTP 상에서 텔레메트리를 가장 효율적으로 직렬화하여 전송하는 고성능 통신 규격
- **컨텍스트 전파 (Context Propagation)** : 마이크로서비스 간 비동기 호출 시 `traceparent` 등의 공통 HTTP 헤더를 통해 트랜잭션 흐름을 중단 없이 이어주는 메커니즘 (W3C 표준)
- **Span & Trace** : Trace는 전체 엔드투엔드 트랜잭션 여정이며, Span은 개별 서비스 내에서 수행된 작업의 단일 실행 시간 단위 블록

</details>

---

## 2~4교시 예상문제 (25점)

> 클라우드 네이티브 마이크로서비스(MSA)의 관측성(Observability) 확보를 위한 OpenTelemetry(OTel)의 개념과 도입 배경을 설명하고, 3대 관측성 신호(M.E.L.T), OTel Collector의 내부 파이프라인(Receiver-Processor-Exporter) 아키텍처 및 W3C 분산 추적 전파 메커니즘을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 분산 시스템에서 발생하는 지표(Metrics), 추적(Traces), 로그(Logs)를 생성·수집·가공하여 분석 백엔드로 전송하는 CNCF 공식 벤더 중립 표준 관측성 프레임워크 |
| 목적 | 상용 APM(Datadog, New Relic) 벤더 락인 방지, 이기종 마이크로서비스 간 계측 표준화, 고성능 저비용의 원격 측정 데이터 통합 관리 |

## Ⅱ. 핵심 특징

OpenTracing(추적)과 OpenCensus(지표)의 장점을 결합하여 완전한 단일 관측성 생태계 구축.

| 핵심 요소 | 공학적 원리 | 실무 기대 효과 |
|---|---|---|
| **벤더 중립성 (Vendor Neutral)** | 표준 OTLP 프로토콜을 사용하여 코드 변경 없이 백엔드(Grafana, Datadog 등) 교체 가능 | 모니터링 솔루션 전환 비용 및 라이선스 비용 절감 |
| **자동/수동 계측 지원 (Instrumentation)** | Bytecode 바이트코드 조작을 통한 무수정 계측(Java Agent)과 명시적 SDK API 지원 | 손쉬운 초기 도입 및 정밀한 도메인 비즈니스 지표 계측 |
| **W3C TraceContext 준수** | 글로벌 웹 표준 헤더(`traceparent`, `tracestate`) 기반 분산 문맥 전파 | 서비스 경계를 넘나드는 100% 끊김 없는 엔드투엔드 추적 |
| **수집 계층의 분리 (Collector)** | 애플리케이션 파드와 분석 스토리지 사이에 전용 Collector 프록시 배치 | 민감정보(PII) 마스킹, 데이터 압축 및 테일 기반 샘플링 실현 |

## Ⅲ. 체계·프로세스

OpenTelemetry의 데이터 수집 파이프라인 및 분산 추적 문맥 전파 아키텍처.

```text
+---------------------------------------------------------------------------------------------------------+
|                                    OpenTelemetry 아키텍처 및 파이프라인 체계                             |
+---------------------------------------------------------------------------------------------------------+
                                                                                                           
  [1] 애플리케이션 계측 (Instrumentation)                                                                   
  +───────────────────────────────────────────────────+                                                    
  |  주문 서비스 (Service A)                          |                                                    
  |  - OTel Java Agent (자동 계측: Traces/Metrics)    |                                                    
  |  - TraceId: 4bf92f3577b34da6a3ce929d0e0e4736      |                                                    
  +─────────────────────────┬─────────────────────────+                                                    
                            │ HTTP POST (Header: traceparent: 00-4bf92f35...-01)                           
                            ▼ (W3C Context Propagation)                                                    
  +───────────────────────────────────────────────────+                                                    
  |  결제 서비스 (Service B)                          |                                                    
  |  - 동일 TraceId 상속, 신규 SpanId 생성            |                                                    
  +─────────────────────────┬─────────────────────────+                                                    
                            │                                                                              
                            │ OTLP Protocol (gRPC : Port 4317)                                             
                            ▼                                                                              
  ─────────────────────────────────────────────────────────────────────────────────────────────────────────
  [2] OpenTelemetry Collector 파이프라인                                                                   
  +─────────────────────────────────────────────────────────────────────────────────────────────────────+  
  |   [ Receiver ]                 [ Processor ]                       [ Exporter ]                     |  
  |   * otlp (gRPC/HTTP)   ───>    * memory_limiter (메모리 제어)  ───>  * otlp (Jaeger 전송)           |  
  |   * prometheus                 * batch (배치 버퍼링)                 * prometheus (메트릭 노출)     |  
  |   * filelog                    * transform (개인정보 마스킹)        * datadog (상용 클라우드 전송) |  
  +───────────────────────────────────────────────────┬─────────────────────────────────────────────────+  
                                                      │                                                    
                                                      ▼                                                    
  [3] 분산 관측성 백엔드 (Observability Backends)                                                          
  +─────────────────────────+   +─────────────────────────+   +─────────────────────────+                  
  |     Jaeger / Tempo      |   |   Prometheus / Mimir    |   |     Grafana Loki        |                  
  |   (분산 추적 Trace 뷰)  |   |   (시스템 지표 Metric)  |   |   (구조화 로그 Log 뷰)  |                  
  +─────────────────────────+   +─────────────────────────+   +─────────────────────────+                  
```

- **OTel 3단계 동작 프로세스**:
  1. **계측 및 문맥 주입(Inject)** : 클라이언트 요청 처리 시 OTel SDK가 루트 Span을 생성하고, 다음 서비스 호출 시 HTTP 요청 헤더에 W3C 표준 `traceparent`를 주입.
  2. **수집 및 파이프라인 처리(Collector)** : Collector의 Receiver가 OTLP 패킷을 수신하고, Processor가 민감한 개인정보(주민번호, 카드번호)를 해시 마스킹한 후 배치 단위로 묶음.
  3. **다중 대상 전송(Export)** : 가공된 추적 데이터는 Jaeger로, 시계열 지표는 Prometheus로, 로그는 Loki로 동시에 라우팅하여 분산 적재.

## Ⅳ. 종류·비교

#### 관측성 3대 기둥(M.E.L.T) 신호 특성 비교

| 신호 (Signal) | 데이터 형식 및 특징 | 주요 목적 | 한계 및 상호 보완 |
|---|---|---|---|
| **지표 (Metrics)** | 타임스탬프와 숫자 값의 쌍, 집계된 시계열 데이터 | 시스템 이상 징후 조기 감지, 알람(Alerting) 발송 | 세부적인 원인 분석(Why) 불가 $\rightarrow$ Trace로 보완 |
| **추적 (Traces)** | 요청의 시작부터 끝까지 서비스 간 호출 경로와 지연시간 | 분산 환경의 병목 구간 및 지연(Latency) 원인 분석 | 개별 요청 경로만 표시, 전체 집계성 분석에는 Metric 필요 |
| **로그 (Logs)** | 타임스탬프와 함께 기록된 구조화/비구조화 텍스트 이벤트 | 특정 에러 발생 당시의 상세 컨텍스트(스택 트레이스) 확인 | 데이터 크기가 방대하여 전체 검색 시 높은 비용 유발 |

#### OTel Collector 배포 모델 비교

| 배포 모델 | 배치 구조 | 장점 | 단점 및 적합한 환경 |
|---|---|---|---|
| **에이전트 (Sidecar/DaemonSet)** | 각 애플리케이션 파드 또는 VM 노드마다 1:1 배치 | 네트워크 지연 최소화, 로컬 호스트 자원 격리 수집 | 파드 증가 시 클러스터 메모리 오버헤드 발생 |
| **게이트웨이 (Standalone Cluster)** | 독립된 쿠버네티스 서비스 클러스터로 원격 집중 배치 | 중앙 집중식 샘플링, 인증, 버퍼링 정책 일괄 관리 | 네트워크 홉 1회 추가로 미세 지연시간 발생 |
| **하이브리드 (Agent + Gateway)** | 노드 에이전트가 수집 후 중앙 게이트웨이로 릴레이 | 대규모 트래픽 완벽 처리, 보안 격리 및 비용 최적화 | 가장 권장되는 엔터프라이즈 프로덕션 아키텍처 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 대규모 트래픽 인입 시 100% 추적 데이터 수집으로 인한 네트워크 대역폭 고갈 및 스토리지 비용 폭증 | Collector 계층에 테일 기반 샘플링(Tail-based Sampling)을 적용하여 에러 발생 트레이스 및 고지연 트레이스만 선별 저장 |
| 비동기 메시지 큐(Kafka, RabbitMQ) 연동 시 컨텍스트 헤더 유실로 인한 분산 추적 체인 단절 | 메시지 프로듀서 발행 시 레코드 헤더에 TraceId를 명시 주입하고 컨슈머 수신 시 컨텍스트 복원(Extract) 표준화 |
| 로그, 지표, 트레이스가 서로 다른 메타데이터 키를 사용하여 상호 연관 분석(Correlation) 곤란 | OTel의 시맨틱 컨벤션(Semantic Conventions)을 강제하여 `service.name`, `host.id` 표준 속성을 전사 통일 |

## Ⅵ. 제언

OpenTelemetry 도입 시 단순 모니터링 도구의 교체가 아닌 클라우드 네이티브 관측성 거버넌스 차원에서 시맨틱 컨벤션을 수립하고, 하이브리드 Collector 구조와 테일 샘플링을 결합한 비용 최적화 설계가 필수적임.

```text
[애플리케이션 계측] ──> [노드 데몬셋 수집기] ──> [중앙 게이트웨이 클러스터] ──> [테일 샘플링 필터] ──> [백엔드 저장]
 (OTel SDK/Agent)         (초고속 로컬 수집)       (전사 로드밸런싱 & 인증)         (정상 1%, 오류 100%)    (비용 80% 절감)
```

| 거버넌스 영역 | 권장 아키텍처 실천법 | 핵심 관리 지표 |
|---|---|---|
| **표준화** | OTel 시맨틱 컨벤션 준수 (`service.name`, `deployment.environment`) | 서비스 식별자 불일치율 0% 달성 |
| **비용 통제** | Tail-based Sampling Processor 가동 (성공 트랜잭션 샘플링 축소) | 텔레메트리 스토리지 인프라 비용 70% 절감 |
| **장애 대응** | Prometheus 지표 알람 발생 시 해당 시점 Trace 링크 자동 연계 | 장애 원인 식별 시간(MTTD) 5분 이내 단축 |

---

## 출제 이력

- 제134회 정보관리기술사 1교시: OpenTelemetry(OTel)의 개념과 구성요소(API, SDK, Collector)
- 제129회 컴퓨터시스템응용기술사 4교시: 마이크로서비스 관측성(Observability)의 3대 요소(M.E.L.T)와 분산 추적 기법
- 제124회 정보관리기술사 2교시: 클라우드 네이티브 분산 추적을 위한 W3C TraceContext 표준 헤더 구조

## 참고 자료

- CNCF OpenTelemetry 공식 문서: opentelemetry.io Architecture and Concepts
- Ted Young, Austin Parker, "Cloud Observability in Action with OpenTelemetry"
- W3C Recommendation: Trace Context Level 2 Specification

## 연결 토픽

- [마이크로서비스 아키텍처(MSA)](./035_msa.md)
- [API Gateway](./075_api_gateway.md)
- [서비스 메시](./088_service_mesh.md)
- [CI/CD 파이프라인](./095_ci_cd.md)
