---
title: "OpenTelemetry(관측성 표준)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
date: "2026-09-22T07:25:00+09:00"
extra:
  model: "GLM-5.3-Flash"
author: "Antigravity"
lastModified: "2026-03-30T10:00:00+09:00"
---

## 큰 그림과 30초 인출

- **본질**: 특정 모니터링 상용 벤더(APM)에 코드가 종속되는 것을 방지하고, 분산 시스템의 3대 텔레메트리(Traces, Metrics, Logs)를 단일한 표준 방식으로 계측·수집·가공·전송하는 CNCF 오픈소스 관측성 표준이다.
- **메커니즘**: 애플리케이션 계측(API/SDK) $\rightarrow$ W3C Trace Context 헤더 분산 전파 $\rightarrow$ OTLP 프로토콜 전송 $\rightarrow$ Collector의 Receiver/Processor/Exporter 파이프라인 가공 $\rightarrow$ 다중 백엔드 라우팅 순으로 동작한다.
- **산출물**: OTLP 텔레메트리 데이터 스트림, 분산 서비스 호출 맵(Trace Dependency), OTel Collector 파이프라인 설정 파일, Tail-based 샘플링 정책서.

---

## 핵심 메커니즘과 수집·가공 아키텍처

```mermaid
flowchart LR
    subgraph C["OTel Collector"]
        direction LR
        R["Receiver"] --> P["Processor"] --> E["Exporter"]
    end
    A["애플리케이션 계측"] -->|OTLP| R
    E --> B["다중 백엔드"]
```

### (1) 모니터링(Monitoring) vs 관측성(Observability)

| 비교 항목 | 전통적 모니터링 (Monitoring) | 현대적 관측성 (Observability) |
|---|---|---|
| **핵심 질문** | **"시스템이 지금 정상인가? (Is it broken?)"** | **"시스템 내부에서 왜 이런 문제가 발생했는가? (Why?)"** |
| **대상 문제** | 사전에 예측 가능한 기지의 문제(Known-Unknowns) | **예측 불가능한 미지의 복합 장애(Unknown-Unknowns)** |
| **수집 데이터** | 단편적인 서버 메트릭(CPU/메모리) 및 단순 텍스트 로그 | **Traces + Metrics + Logs(MELT)의 유기적 결합** |
| **시스템 구조** | 단일 모놀리식 서버 중심 | 수백 개 마이크로서비스가 비동기 통신하는 분산 환경 |

### (2) OpenTelemetry 4대 핵심 아키텍처 구성 요소
1. **API**: 소스코드에 텔레메트리 계측을 선언하는 인터페이스(구현체 없음). 소스코드가 특정 벤더 라이브러리에 오염되지 않도록 격리.
2. **SDK**: API의 실제 구현체로, 메모리 버퍼링, 배치 처리, 프로세서 파이프라인, 전송 메커니즘을 구동.
3. **Collector**: 수집된 텔레메트리를 프록시 형태로 중계하는 독립 데몬.
   - **Receiver**: OTLP, Jaeger, Zipkin, Prometheus 등 다양한 포맷으로 데이터 수신.
   - **Processor**: 데이터 배치 압축, 민감정보(PII) 마스킹, Tail-based 샘플링 수행.
   - **Exporter**: 가공된 데이터를 원하는 다중 백엔드(Prometheus, Datadog, OpenSearch 등)로 변환 전송.
4. **OTLP (OpenTelemetry Protocol)**: gRPC 및 HTTP/Protobuf 기반의 고성능 표준 직렬화 전송 프로토콜.

### (3) W3C Trace Context 분산 전파 메커니즘
- 분산 서비스 A에서 서비스 B로 HTTP 요청 시 헤더에 `traceparent` 필드를 주입(Inject)하고 추출(Extract)하여 동일한 `Trace ID`를 유지함으로써 마이크로서비스 전 구간을 하나의 단일 트랜잭션으로 연결함:
  - `traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01`
  - 버전(00) - Trace ID(32자 Hex) - Parent Span ID(16자 Hex) - Trace Flags(샘플링 여부).

---

## 실무 적용 및 도입 체크리스트

1. **하이브리드 계측 표준 수립**: HTTP 라우팅, DB 쿼리 등 범용 구간은 OTel Auto-Instrumentation을 적용하고, 결제·주문 등 핵심 비즈니스 로직에는 Manual SDK로 도메인 속성(`order_id`, `user_tier`)을 추가하였는가?
2. **Tail-based 샘플링 파이프라인**: 정상 트래픽은 1%만 수집하고, 오류(5xx) 및 지연(P99) 트랜잭션은 100% 수집하도록 Collector에 Tail-based Sampling을 구성하였는가?
3. **개인정보(PII) 마스킹 자동화**: 계측 데이터 내 주민등록번호, 카드번호, 비밀번호 등이 노출되지 않도록 Collector의 Transform Processor에 정규식 마스킹을 적용하였는가?
4. **Agent-Gateway 2단 구성**: 쿠버네티스 노드별 경량화된 DaemonSet(Agent)과 중앙 스케일아웃 Gateway 클러스터로 분리하여 노드 부하를 최소화하였는가?

---

## 실패 시나리오 및 트러블슈팅

| 위험 | 대책 | 효과 |
|---|---|---|
| **상용 APM 교체 시 전사 소스코드 재작성 병목** | 코드 레벨 계측을 OTel 표준 API로 통일하고 Collector Exporter만 교체 | 벤더 전환 비용 90% 절감 및 멀티 백엔드 동시 라우팅 실현 |
| **트레이스 무차별 수집으로 APM 비용 폭증** | OTel Collector에 Tail-based Sampling 적용 (정상 1%, 장애 100%) | 데이터 전송량 80% 감축 및 중요 장애 트레이스 100% 보존 |
| **분산 로그 및 트레이스에 개인정보(PII) 유출** | OTel Collector의 Transform Processor 기반 정규식 마스킹 강제 | 개인정보보호법 컴플라이언스 완벽 준수 및 보안 사고 예방 |

---

## 차세대 확장 및 융합

- **지속적 프로파일링(Continuous Profiling)의 4대 요소 편입**: 기존 Traces, Metrics, Logs(MELT)에 이어 CPU/메모리 함수 호출 스택을 나노초 단위로 계측하는 eBPF 기반 프로파일링(Profiles)이 OTel 표준의 4번째 핵심 기둥으로 통합되고 있다.
- **AI/LLM 관측성(LLMOps) 연계**: LLM 호출 시 토큰 수, 레이턴시, 프롬프트 및 응답 임베딩 비용을 추적하는 OpenTelemetry GenAI 시맨틱 컨벤션(Semantic Conventions) 표준이 제정되어 빠르게 확산되고 있다.

---

## 실전 합격 전략 및 기술사적 제언

### 학습자 통찰 메모 — 답안 밖
- **[핵심 통찰]**: OTel 도입의 결정적 가치는 '벤더 종속 탈피(Vendor Neutrality)'와 '비용 통제(Cost Governance)'이다. 소스코드에는 오직 OTel API만 남기고, 데이터 수집 파이프라인의 Collector에서 Tail-based Sampling을 걸어 고비용 상용 SaaS APM과 저비용 오픈소스 스토리지로 트래픽을 분기하는 것이 엔터프라이즈의 정석이다.
- **나라면**: 답안 2단락에 Receiver-Processor-Exporter 3단 구조를 명확히 제시하고 W3C 헤더 구조(`traceparent`)를 서술하겠다. 4단락에서는 Agent-Gateway 2단계 토폴로지와 eBPF 프로파일링 통합을 통한 무간섭 관측성 고도화 방안을 강조하겠다.

### 실전 답안용 기술사적 제언
- **판정 기준**: 마이크로서비스 전 구간에서 Trace Context 누락율 0% 및 관측성 데이터 수집으로 인한 애플리케이션 CPU 오버헤드 3% 미만 준수.
- **대응 방안**: K8s 노드별 DaemonSet 수집기(Agent)와 중앙 Gateway 클러스터의 2단 토폴로지를 구축하고, Collector Processor에서 민감정보(PII) 정규식 마스킹과 Tail-based 샘플링 동시 적용.
- **검증 체계**: 분산 서비스 간 지연 이상 징후(P99 > 500ms) 및 HTTP 5xx 에러 트레이스 100% 보존 여부를 모니터링하는 E2E 합성 트랜잭션 검증.
- **기대 효과**: APM 상용 벤더 종속 완전 탈피, 네트워크 수집 전송량 80% 절감 및 분산 트랜잭션 장애 원인 규명 시간(MTTR) 70% 단축.
