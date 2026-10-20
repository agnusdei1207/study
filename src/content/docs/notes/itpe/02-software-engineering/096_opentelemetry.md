---
title: "OpenTelemetry(관측성 표준)"
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

- OpenTelemetry(OTel), 관측성(Observability), 텔레메트리(Telemetry), 트레이스(Traces), 메트릭(Metrics), 로그(Logs)
- OTel Collector, OTLP(OpenTelemetry Protocol), 컨텍스트 전파(Context Propagation), W3C Trace Context, 테일 기반 샘플링(Tail-based Sampling)

## Ⅰ. OpenTelemetry의 개요

- 핵심 요약 : 분산 시스템의 텔레메트리 생성·수집·내보내기를 표준화한 벤더 중립 오픈소스 프레임워크.
- 개념 : 클라우드 네이티브 컴퓨팅 재단(CNCF, Cloud Native Computing Foundation)에서 OpenTracing과 OpenCensus 프로젝트를 통합하여 표준화한 벤더 중립적 오픈소스 원격 측정(Telemetry) 프레임워크로, 분산 클라우드 환경의 트레이스(Traces), 메트릭(Metrics), 로그(Logs)의 생성·수집·처리·내보내기(Export)를 위한 표준 API(Application Programming Interface), SDK(Software Development Kit) 및 도구 체계.
- 배경 및 필요성 : 마이크로서비스·분산 서버 환경에서 상용 APM(Application Performance Monitoring) 도구(Datadog, New Relic)별 전용 에이전트·수집 포맷의 파편화, 벤더 락인과 유지보수 오버헤드의 극복 필요.
- 관측성 신호 체계(MELT) : 메트릭(Metrics), 이벤트(Events), 로그(Logs), 트레이스(Traces).

## Ⅱ. OpenTelemetry의 특징

- 핵심 요약 : API와 SDK의 분리, 수집기 파이프라인, 표준 컨텍스트 전파의 3축 구조.

1. 벤더 중립 API 기반 계측(Instrumentation)과 런타임 주입 SDK의 역할 분리.
2. OTel(OpenTelemetry) Collector의 수신(Receiver)·처리(Processor)·전송(Exporter) 파이프라인 구조.
3. W3C(World Wide Web Consortium) Trace Context 표준 헤더(traceparent) 기반 컨텍스트 전파(Context Propagation).
4. 백엔드 독립성 : Jaeger, Prometheus, Loki 등 다양 모니터링 백엔드로의 자유 전송.
5. 단일 비즈니스 트랜잭션의 분산 호출 경로 통합 추적.

## Ⅲ. OpenTelemetry의 구조 (흐름)

- 핵심 요약 : 애플리케이션 계측에서 백엔드 시각화까지 이어지는 텔레메트리 파이프라인 흐름.
- 텔레메트리 수집 흐름.

```text
[ 마이크로서비스 A / B ]
 - OTel SDK 계측, W3C Trace Context 전파
   │ OTLP 프로토콜 전송
   ▼
[ OpenTelemetry Collector ]
   ├─ 1. Receivers  (OTLP, Jaeger)
   ├─ 2. Processors (배치, 마스킹)
   └─ 3. Exporters  (OTLP, 백엔드 변환)
   │
   ▼
[ 스토리지 및 시각화 백엔드 ]
 - 트레이스: Jaeger, Tempo
 - 메트릭: Prometheus
 - 로그: Loki, Elasticsearch
```

- API와 SDK의 분리 : 비즈니스 코드의 벤더 중립 OTel API 단독 호출 계측, 실제 데이터 전송 구현의 런타임 주입 SDK 담당.
- OTel Collector(수집기) : 데이터 수신(Receiver) 후 민감정보 마스킹·배치 처리(Processor)를 거쳐 원하는 모니터링 백엔드로 전송(Exporter)하는 프록시 서비스.
- 컨텍스트 전파(Context Propagation) : W3C Trace Context 표준 HTTP(Hypertext Transfer Protocol) 헤더(traceparent)의 서비스 간 전달, 단일 비즈니스 트랜잭션의 분산 호출 경로 추적.

## Ⅳ. 관측성 3대 핵심 데이터의 비교

- 핵심 요약 : 집계·경로·기록의 상이한 관찰 관점과 상호 보완적 분석 흐름.
- 3대 데이터의 장애 분석 활용 순서.

```text
[ 1단계 ] 메트릭 이상 감지 알람 (Prometheus)
    ↓
[ 2단계 ] 트레이스 병목 구간·지연 서비스 식별 (Jaeger/Tempo)
    ↓
[ 3단계 ] 로그 기반 근본 원인 상세 분석 (Loki/Elasticsearch)
```

| 데이터 유형 | 정의 및 특징 | 주 검증 목적 및 장점 | 대표 시각화 도구 |
|---|---|---|---|
| 트레이스(Traces) | 요청이 여러 서비스를 거쳐 처리되는 엔드투엔드 분산 호출 경로 | 병목 서비스 식별, 네트워크 지연 원인 파악, 서비스 간 의존성 파악 | Jaeger, Grafana Tempo, Zipkin |
| 메트릭(Metrics) | 시스템 상태를 시간 경과에 따라 수치로 집계한 시계열 데이터 | 시스템 이상 징후 알람, CPU(Central Processing Unit)/메모리/TPS(Transactions Per Second) 추세 분석 | Prometheus, Datadog, InfluxDB |
| 로그(Logs) | 특정 시점에 발생한 사건에 대한 텍스트 기반 상세 기록 | 장애 발생 시의 근본 원인(Root Cause) 상세 디버깅 | Elasticsearch, Grafana Loki, Fluentd |

## Ⅴ. OpenTelemetry의 장점과 한계

- 핵심 요약 : 벤더 독립 관측성 표준화의 장점, 데이터 비용·수집기 복잡성·계측 누락의 한계.
- 장점
  1. 단일 표준 계측을 통한 APM 벤더 교체 비용 제거(벤더 락인 방지).
  2. 트레이스·메트릭·로그의 통합 수집과 상호 연관 분석.
  3. 오픈소스 생태계 기반 언어별 자동 계측(Auto-Instrumentation) 지원.
- 한계점 1 : 원격 측정 데이터 대량 수집에 따른 네트워크·스토리지 비용 폭증
  - 한계점 : 모든 트레이스·메트릭·로그 전수 수집 시 네트워크 대역폭 포화, 백엔드(APM, 시계열 DB(Database)) 스토리지 비용의 기하급수적 증가.
  - 해결 방안 : 테일 기반 샘플링(Tail-based Sampling) 도입을 통한 에러·고지연 트레이스 선별 수집, OTel Collector 필터링 프로세서의 노이즈 데이터 사전 정제.
- 한계점 2 : OTel Collector 구성 복잡도 및 장애 시 텔레메트리 유실
  - 한계점 : 수집기의 리시버·프로세서·익스포터 파이프라인 설정 복잡성, 트래픽 스파이크 시 컬렉터 메모리 고갈과 관측 데이터 유실.
  - 해결 방안 : OTel Collector의 데몬셋(DaemonSet)과 게이트웨이 2계층 클러스터링 구성, 메모리 제한기(Memory Limiter) 및 큐 기반 재시도(File Storage Extension) 설정.
- 한계점 3 : 수동 계측(Instrumentation) 오버헤드 및 컨텍스트 전파 누락
  - 한계점 : 비표준 비동기 스레드 풀·레거시 프로토콜 사용 환경의 Trace ID 단절, 트레이스 파편화 발생.
  - 해결 방안 : 자바/Go 등 주요 언어별 자동 계측 에이전트(Auto-Instrumentation) 표준화, 사내 프레임워크 차원의 W3C Trace Context 헤더 자동 주입 보일러플레이트 제공.

## Ⅵ. 엔터프라이즈 관측성 구축을 위한 기술사적 제언

- 핵심 요약 : 자동·수동 계측의 조화와 테일 기반 샘플링 중심의 비용 최적화.
- 자동 계측(Auto-Instrumentation)과 수동 계측의 조화 : Java Agent 활용 프레임워크 수준 HTTP·DB 호출의 코드 무수정 자동 계측, 비즈니스 핵심 도메인 트랜잭션(주문 ID, 결제 금액 등)의 OTel 수동 API 스팬 태그(Attribute) 명시를 통한 비즈니스 가시성 확보.
- 샘플링(Sampling) 전략을 통한 네트워크·스토리지 비용 최적화 : 초당 수십만 건 대규모 트래픽 환경의 정상 응답 일부 샘플링, 에러(HTTP 5xx)·지연(Latency 초과) 트랜잭션 전수 수집의 테일 기반 샘플링(Tail-based Sampling)을 OTel Collector에 필수 구성.

## Ⅶ. 결론

- 핵심 요약 : OpenTelemetry는 벤더 중립 관측성의 사실상 표준 계측 체계.
- 요약 : API/SDK 분리와 Collector 파이프라인, 표준 컨텍스트 전파가 통합 관측성의 골격.
- 시사점 : 샘플링 정책 설계, 수집기 이중화, 자동 계측 표준화가 운영 비용과 가시성 균형의 핵심.
