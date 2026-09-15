---
sidebar:
  order: 170
  label: "170. OpenTelemetry"
  badge:
    text: "미출 · 60%"
    variant: note
title: "OpenTelemetry"
date: "2026-09-07T16:00:00+09:00"
tags: ["notes-latest_tech"]
weight: 170
extra:
  question_no: "170"
  source_status: "미출"
  source_history: ""
  priority: 60
  priority_note: "OpenTelemetry 구성과 수집 파이프라인이 유력"
---

## Ⅰ. 개요

- **정의**: 공급자 중립 텔레메트리(Metrics, Traces, Logs) 생성·처리·전송을 위한 CNCF 표준 관찰 가능성(Observability) 오픈소스 프레임워크
- **배경 및 필요성**: 다양한 상용 및 오픈소스 모니터링 벤더(Datadog, Prometheus, Jaeger 등) 고유 에이전트와 비표준 SDK로 인한 벤더 락인 및 코드 파편화를 해결하기 위해, OpenTracing과 OpenCensus를 통합하여 단일화된 벤더 중립적 API/SDK, OTLP 전송 프로토콜, Collector 파이프라인 표준 프레임워크 도입 필요

## Ⅱ. 특징

- 계측 생성 계약과 처리 정책을 분리하는 API·SDK 아키텍처 분리
- W3C Trace Context 및 시맨틱 규약 기반 맥락·속성 명명 표준화
- OTLP 프로토콜 및 OTel Collector 기반 공급자 중립 전송 파이프라인
- 자동 계측(Auto-instrumentation) 및 수동 계측(Manual instrumentation) 동시 지원

## Ⅲ. 구조 및 구성요소

```text
[OpenTelemetry 프레임워크]
├── 표준 규약 계층 ── W3C Context 전파 및 Semantic Conventions 정의
├── 계측 계층 ── 벤더 중립 API(생성 계약) 및 SDK(샘플링/가공 구현)
└── 파이프라인 계층 ── OTLP 프로토콜 및 OTel Collector(수신/처리/전송)
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 계층 | 핵심 구성요소 | 주요 역할 및 책임 |
|:---|:---|:---|
| 표준 규약 계층 | Semantic Conventions | 서비스, HTTP, DB 등 공통 자원 및 속성 명명 표준 규약 정의 |
| 표준 규약 계층 | Context Propagation | 분산 트레이스 식별자(Trace ID, Span ID)의 서비스 경계 전파 계약 |
| 계측 계층 | API | 텔레메트리 데이터 생성 인터페이스 제공 및 종속성 격리 |
| 계측 계층 | SDK | 샘플링 정책 실행, 자원 결합, 메모리 버퍼링 및 내보내기 구현체 |
| 파이프라인 계층 | OTLP | gRPC/HTTP 기반 바이너리 프로토콜로 네트워크 전송 효율 극대화 |
| 파이프라인 계층 | OTel Collector | Receiver(수신), Processor(변환/마스킹), Exporter(백엔드 라우팅) 파이프라인 |

## Ⅳ. 흐름도

```text
[애플리케이션 계측] (① OTel API 및 시맨틱 규약 기반 텔레메트리 신호 생성)
│
▼
[SDK 처리 엔진] (② 자원 결합, 샘플링 필터링, 메모리 버퍼 일괄 배치 처리)
│
▼
[OTLP 전송] (③ gRPC/HTTP 기반 표준 OTLP 프로토콜 네트워크 전송)
│
▼
[OTel Collector] (④ Receiver 수신, Processor 변환/마스킹, Exporter 백엔드 라우팅)
│
▼
[다중 백엔드 저장소] (⑤ Prometheus, Jaeger, Datadog 등 다중 APM 저장 및 시각화)
```

- 분기 결과: Head-based 샘플링 통과 데이터는 OTLP를 통해 Collector로 실시간 전송되며, 필터링 및 배치 가공 후 등록된 다중 백엔드 스토리지로 무손실 라우팅 전달됨

## Ⅴ. 종류 및 비교

| 구분 | API | SDK | Collector |
|:---|:---|:---|:---|
| 적용 기준 | 애플리케이션 계측 인터페이스 | 애플리케이션 런타임 구현체 | 중앙 또는 에이전트형 수집 프록시 |
| 핵심 특징 | 공급자 중립 신호 생성 계약 정의 | 샘플링, 버퍼링, 배치 처리 실행 | 수신기, 처리기, 내보내기 3단계 파이프라인 |
| 변경 영향도 | 인터페이스 고정으로 코드 수정 최소화 | 런타임 라이브러리 업데이트 필요 | 인프라 설정 변경만으로 백엔드 전환 가능 |
| 한계점 | 신호 처리 및 전송 불가능 | 애플리케이션 CPU 및 메모리 점유 | 과부하 발생 시 버퍼 오버플로우 위험 |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 효과 |
|:---|:---|:---|
| 맥락 전파 단절로 인한 호출 경로 추적 실패 | W3C Trace Context 규약 통일 및 메시지 큐 헤더 주입/추출 표준화 | 분산 마이크로서비스 전 구간 추적 연속성 확보 |
| 과도한 메트릭 카디널리티로 백엔드 비용 폭증 | Collector Processor에서 고유 ID 제거 및 카디널리티 한도 정책 적용 | APM 인덱싱 비용 절감 및 쿼리 응답 성능 안정화 |
| Collector 과부하로 인한 텔레메트리 유실 위험 | 노드별 DaemonSet 에이전트 및 중앙 Gateway Collector 2계층 구성, 영속 디스크 큐 적용 | 트래픽 폭증 시 데이터 손실 방지 및 고가용성 보장 |

## Ⅶ. 결론

- **기술 위상/발전**: CNCF 졸업 프로젝트이자 클라우드 네이티브 관찰 가능성 생태계의 단일 글로벌 표준으로 메트릭·로그·트레이스를 넘어 지속적 프로파일링까지 단일 파이프라인으로 통합 확장
- **실무 적용/통제**: 데몬셋 기반 에이전트와 중앙 게이트웨이 2계층 Collector 파이프라인 구성, 테일 기반 샘플링 및 배치 프로세서 튜닝을 통한 네트워크 부하 제어 및 수집 비용 최적화
