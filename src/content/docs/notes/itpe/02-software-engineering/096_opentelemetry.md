---
title: "OpenTelemetry(관측성 표준)"
author: "Antigravity"
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

## Ⅰ. OpenTelemetry의 개요

- **개념** : 클라우드 네이티브 컴퓨팅 재단(CNCF)에서 OpenTracing과 OpenCensus 프로젝트를 통합하여 표준화한 벤더 중립적 오픈소스 원격 측정(Telemetry) 프레임워크로, 분산 클라우드 환경에서 트레이스(Traces), 메트릭(Metrics), 로그(Logs)를 생성, 수집, 처리, 내보내기(Export)하기 위한 표준 API, SDK 및 도구 체계.
- **배경 및 필요성** : 복잡한 마이크로서비스 및 분산 서버 환경에서 상용 APM(Datadog, New Relic) 도구마다 서로 다른 전용 에이전트와 수집 포맷을 사용하여 발생하는 벤더 락인과 유지보수 오버헤드를 극복하기 위해 제정.
- **관측성의 3대 기둥 (MELT)** : 메트릭(Metrics), 이벤트(Events), 로그(Logs), 트레이스(Traces).

## Ⅱ. OpenTelemetry 아키텍처 및 원격 측정 수집 흐름

```text
   [ 마이크로서비스 A ] ──────── (W3C Trace Context 전파) ────────> [ 마이크로서비스 B ]
     (OTel SDK 계측)                                                   (OTel SDK 계측)
          │ (OTLP 프로토콜 전송)                                            │
          ▼                                                                 ▼
   ┌────────────────────────────────────────────────────────────────────────────────┐
   │ [ OpenTelemetry Collector ]                                                    │
   │  ┌──────────────────┐       ┌──────────────────┐       ┌──────────────────┐    │
   │  │ 1. Receivers     │ ────> │ 2. Processors    │ ────> │ 3. Exporters     │    │
   │  │ (OTLP, Jaeger)   │       │ (배치, 마스킹)   │       │ (OTLP, 백엔드변환) │    │
   │  └──────────────────┘       └──────────────────┘       └──────────────────┘    │
   └───────────────────────────────────────┬────────────────────────────────────────┘
                                           │
                                           ▼
   ┌────────────────────────────────────────────────────────────────────────────────┐
   │ [ 스토리지 및 시각화 백엔드 ]                                                  │
   │  - 트레이스: Jaeger, Tempo / 메트릭: Prometheus / 로그: Loki, Elasticsearch    │
   └────────────────────────────────────────────────────────────────────────────────┘
```

- **API와 SDK의 분리** : 비즈니스 코드는 벤더 중립적인 OTel API만을 호출하여 계측(Instrumentation)하고, 실제 데이터 전송 구현은 런타임에 주입되는 OTel SDK가 담당.
- **OTel Collector (수집기)** : 데이터를 수신(Receiver)하여, 민감정보 마스킹 및 배치 처리(Processor)를 거친 후, 원하는 모니터링 백엔드로 전송(Exporter)하는 프록시 서비스.
- **컨텍스트 전파 (Context Propagation)** : W3C Trace Context 표준 HTTP 헤더(traceparent)를 서비스 간에 전달하여 단일 비즈니스 트랜잭션의 분산 호출 경로 추적.

## Ⅲ. 관측성 3대 핵심 데이터(Traces, Metrics, Logs) 비교

| 데이터 유형 | 정의 및 특징 | 주 검증 목적 및 장점 | 대표 시각화 도구 |
|---|---|---|---|
| 트레이스 (Traces) | 요청이 여러 서비스를 거쳐 처리되는 엔드투엔드 분산 호출 경로 | 병목 서비스 식별, 네트워크 지연 원인 파악, 서비스 간 의존성 파악 | Jaeger, Grafana Tempo, Zipkin |
| 메트릭 (Metrics) | 시스템의 상태를 시간 경과에 따라 수치로 집계한 시계열 데이터 | 시스템 이상 징후 알람, CPU/메모리/TPS 추세 분석 | Prometheus, Datadog, InfluxDB |
| 로그 (Logs) | 특정 시점에 발생한 사건에 대한 텍스트 기반의 상세 기록 | 장애 발생 시의 근본 원인(Root Cause) 상세 디버깅 | Elasticsearch, Grafana Loki, Fluentd |

## Ⅳ. 엔터프라이즈 관측성(Observability) 구축을 위한 기술사적 제언

- **자동 계측(Auto-Instrumentation)과 수동 계측의 조화** : Java Agent 등을 활용하여 프레임워크 수준의 HTTP/DB 호출은 코드 수정 없이 자동 계측하되, 비즈니스 핵심 도메인 트랜잭션(주문 ID, 결제 금액 등)은 OTel 수동 API를 통해 스팬 태그(Attribute)로 명시하여 비즈니스 가시성 확보.
- **샘플링(Sampling) 전략을 통한 네트워크 및 스토리지 비용 최적화** : 초당 수십만 건의 대규모 트래픽 환경에서 모든 트레이스를 100% 수집하면 막대한 네트워크 및 스토리지 비용이 발생하므로, 정상 응답은 1%만 샘플링하고 에러(HTTP 5xx)나 지연(Latency > 2초) 트랜잭션은 100% 수집하는 테일 기반 샘플링(Tail-based Sampling)을 OTel Collector에 필수 구성.
