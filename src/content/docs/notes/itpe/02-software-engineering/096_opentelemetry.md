---
title: "OpenTelemetry(관측성 표준)"
tags:
  - "notes-software-engineering"
---

| 세부 토픽 키워드 | 핵심 다이어그램 / 개념 매핑 |
|---|---|
| OpenTelemetry (OTel) | CNCF 주도 오픈소스 벤더 중립적 관측성(Observability) 계측 표준 |
| 3대 텔레메트리 (MELT) | Traces(분산 추적), Metrics(시계열 수치), Logs(이벤트 기록) 통합 |
| OTel 4대 핵심 구조 | API(명세) ➔ SDK(구현체) ➔ Collector(수집/가공/전송) ➔ OTLP(전송 프로토콜) |
| W3C Trace Context & 샘플링 | HTTP 헤더 전파(traceparent) 및 비용 최적화 Tail-based 샘플링 |

## 답안 골격 (세로 피시본)

```text
[OpenTelemetry] ◀━━ 머리: Ⅶ 내 의견 (벤더 중립적 표준 계측 체계와 Tail-based 샘플링 기반 비용 효율적 관측성 확립)
 ┃
 ┣━ Ⅰ 개요 ───── 모니터링 벤더별 상이한 독점 SDK와 에이전트 종속 ↔ CNCF 통합 표준 관측성 프레임워크
 ┣━ Ⅱ 특성 ───── 벤더 중립성 · 3대 텔레메트리(MELT) 단일화 · OTLP 표준 프로토콜 · 무중단 백엔드 교체
 ┣━ Ⅲ 구조 ───── 계측 계층(API/SDK) ➔ 수집 계층(Collector: Receiver, Processor, Exporter) ➔ 분석 백엔드
 ┣━ Ⅳ 메커니즘 ─ W3C Trace Context 전파(Span ID/Trace ID 주입·추출) ➔ OTLP 전송 ➔ Tail 샘플링/가공
 ┣━ Ⅴ 비교 ───── OpenTelemetry vs OpenTracing vs OpenCensus / 모니터링 vs 관측성
 ┗━ Ⅵ 실무 ───── 고트래픽 트레이싱 수집 비용 폭증 · 민감정보 노출(PII) · 자동 vs 수동 계측 하이브리드
```

- 필수 키워드: OpenTelemetry, 관측성(Observability), MELT(Traces/Metrics/Logs), OTel Collector, OTLP(OpenTelemetry Protocol), W3C Trace Context, Span/Trace ID, Tail-based Sampling
- 기출 이력: 시사·트렌드 미출제 (클라우드 네이티브 MSA 핵심 인프라 1순위 예상 토픽)

## 핵심 그림 (30초 인출용)

```text
+-------------------------------------------------------------------------+
|                  OpenTelemetry 수집 및 전송 아키텍처                    |
+-------------------------------------------------------------------------+
|  [ Microservice A ]          [ Microservice B ]                         |
|  OTel SDK (Auto/Manual)      OTel SDK (Auto/Manual)                     |
|           \                      /                                      |
|            \ (OTLP / gRPC)      / (OTLP / HTTP)                         |
|             v                  v                                        |
|  +-------------------------------------------------------------------+  |
|  |                    OpenTelemetry Collector                        |  |
|  |  [ Receiver ]    -->    [ Processor ]    -->    [ Exporter ]      |  |
|  |  (OTLP, Zipkin,         (배치 압축,             (Prometheus,      |  |
|  |   Jaeger 수신)           Tail 샘플링, PII 마스킹) Jaeger, Datadog) |  |
|  +-------------------------------------------------------------------+  |
|                                │                                        |
|              ┌─────────────────┴─────────────────┐                      |
|              v                                   v                      |
|     [ Prometheus / Grafana ]             [ Jaeger / OpenSearch ]        |
|     (Metrics 분석 및 대시보드)           (분산 Traces 및 Logs 분석)     |
+-------------------------------------------------------------------------+
|                 W3C Trace Context 분산 서비스 간 전파 메커니즘           |
|                                                                         |
| Client ──> [Service A] ── HTTP traceparent 헤더 ──> [Service B]         |
|            Trace ID: 4bf92f35...                    Trace ID: 동일      |
|            Span ID : 00f067aa...                    Span ID : 5c341b8a..|
+-------------------------------------------------------------------------+
```

## 비교·연결 (유사 개념 간 차이점)

### 전통적 모니터링 vs 현대적 관측성(Observability)

| 비교 항목 | 전통적 모니터링 (Monitoring) | 현대적 관측성 (Observability) |
|---|---|---|
| **핵심 질문** | **"시스템이 지금 정상인가? (Is it broken?)"** | **"시스템 내부에서 왜 문제가 발생했는가? (Why?)"** |
| **대상 문제** | 사전에 정의된 알고 있는 문제(Known-Unknowns) | **예측 불가능한 미지의 복합 장애(Unknown-Unknowns)** |
| **데이터 수집** | 단편적 메트릭(CPU, 메모리) 및 시스템 로그 | **Traces + Metrics + Logs(MELT)의 맥락적 결합** |
| **시스템 구조** | 단일 모놀리식 서버 중심 | 수백 개 서비스가 비동기 통신하는 분산 MSA |

### 관측성 3대 텔레메트리 데이터 (MELT) 비교

| 데이터 유형 | 정의 및 특성 | 장점 | 한계 및 비용 |
|---|---|---|---|
| **Traces (추적)** | 단일 요청이 분산 서비스를 거쳐가는 전 구간 경로 기록 | **서비스 간 병목 구간 및 장애 발생 지점 즉시 특정** | 데이터 볼륨이 커서 샘플링(Sampling) 필수 |
| **Metrics (지표)** | 특정 시간 간격으로 집계된 수치 데이터 (카운터, 게이지) | 용량이 매우 작고 실시간 알림/대시보드에 최적 | 개별 요청 수준의 상세 원인 파악 불가 |
| **Logs (로그)** | 특정 시점에 발생한 사건의 상세 텍스트 기록 | 풍부한 디버깅 세부 컨텍스트 제공 | 구조화되지 않으면 검색 비용과 스토리지 폭증 |

## 실무 적용과 트레이드오프

- 적용 상황: 수백 개 마이크로서비스가 운영되는 엔터프라이즈 금융 클라우드 플랫폼

| 실패 증상 (위험) | 근본 원인 | 엔지니어링 대책 | 기대 효과 |
|---|---|---|---|
| **상용 APM 벤더 교체 시 전사 서비스 소스코드 및 도커 이미지 전면 재작성** | 특정 APM 벤더의 독점 SDK와 소스코드가 강하게 결합된 종속성 | 코드 레벨 계측을 OpenTelemetry 표준 API로 통일하고 Collector Exporter만 교체 | 벤더 전환 비용 90% 절감 및 다중 백엔드 동시 전송 실현 |
| **모든 트레이스 무차별 수집으로 APM 라이선스 비용 및 네트워크 폭증** | 분산 트레이싱 전수 수집(Head-based 100%) 정책 적용 | OTel Collector에 Tail-based Sampling 적용 (정상 1%, 오류 및 P99 지연 100%) | 데이터 전송량 80% 감축 및 중요 장애 트레이스 100% 보존 |
| **분산 로그 및 트레이스에 고객 주민번호, 계좌번호 등 개인정보(PII) 노출** | 애플리케이션 계측 단계에서 민감정보 마스킹 누락 | OTel Collector의 Transform Processor를 활용한 정규식 기반 PII 자동 마스킹 | 개인정보보호법 컴플라이언스 준수 및 데이터 유출 방지 |

## 기술사의 눈 (주체적 차별화 제언)

- **[단순 자동 계측에 만족하는 형식적 관측성 도입의 한계]**: 다수 프로젝트가 라이브러리 자동 주입(Auto-Instrumentation)만 켜두어 단순 HTTP 상태코드(200, 500)만 수집함. 정작 실제 장애 상황에서는 '어떤 고객 세그먼트의 어떤 주문 건인지' 비즈니스 컨텍스트가 결여되어 근본 원인을 찾지 못함.
- **[나라면: 2계층 수집 파이프라인과 비즈니스 도메인 계측 표준 수립]**:
  1. **계측 계층**: 프레임워크 레벨 자동 계측을 기본 인프라로 적용하되, 결제·주문 등 핵심 비즈니스 로직에는 수동 계측(Manual SDK)을 의무화하여 `order_id`, `user_tier`, 결제 수단 등 도메인 속성(Span Attributes)을 주입.
  2. **수집 계층 (Agent-Gateway 2단 구성)**: 각 노드에는 경량화된 OTel Collector DaemonSet을 배치해 로컬 수집을 담당하게 하고, 중앙에는 다중 인스턴스로 스케일아웃되는 Collector Gateway 클러스터를 구성하여 배치 압축, PII 마스킹, Tail-based 샘플링을 전담 처리.
  3. **비용 효율적 분석 백엔드 분리**: 고가의 상용 APM(Datadog 등)에는 이상 징후 트레이스(오류, P99)만 선별 전송하고, 장기 보관 및 감사용 로그는 오픈소스 OpenSearch 및 S3 오브젝트 스토리지로 이원화 라우팅하여 관측성 비용을 60% 이상 절감하겠음.
