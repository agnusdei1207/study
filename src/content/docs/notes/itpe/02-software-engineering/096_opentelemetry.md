---
title: "OpenTelemetry(관측성 표준)"
description: "API·SDK·Collector·OTLP·W3C Trace Context, 3대 데이터 비교, 데이터 비용·수집기 복잡도·계측 누락 한계와 방안"
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

- OpenTelemetry; 분산 추적; 메트릭; 로그; 컨텍스트 전파; OTLP; Collector; 시맨틱 규약

## Ⅰ. OpenTelemetry의 개요

- 핵심 요약 : OpenTelemetry는 애플리케이션·인프라의 텔레메트리를 생성·수집·처리·전송하기 위한 벤더 중립 관측성 프레임워크와 규격.
- 개념 : OpenTelemetry는 애플리케이션·인프라의 텔레메트리를 생성·수집·처리·전송하기 위한 벤더 중립 관측성 프레임워크와 규격.
- 배경 및 필요성 : 마이크로서비스·클라우드 환경에서는 단일 로그나 지표만으로 요청의 종단 경로·오류원인을 연결하기 어려움.
- 주요 목적 : 분산 시스템의 상태와 장애원인을 상호운용 가능한 계측 데이터로 파악해 서비스 신뢰성과 운영효율을 높임.

## Ⅱ. OpenTelemetry의 특징 및 장점

- 핵심 요약 : 핵심 요소: 트레이스(Trace)·메트릭(Metrics)·로그(Logs)·SDK·Collector·OTLP. 설계목표는 분산 시스템의 상태와 장애원인을 상호운용 가능한 계측 데이터로 파악해 서비스 신뢰성과 운영효율을 높임.

1. 트레이스(Trace) : 요청을 스팬(Span) 계층으로 표현하고 컨텍스트 전파 → 서비스 간 지연·오류 경로 추적.
2. 메트릭(Metrics) : 시계열 측정값으로 처리량·오류·지연 관찰 → 용량·SLO(Service Level Objective, 서비스 수준 목표) 추세 판단.
3. 로그(Logs) : 시각·문맥·속성을 가진 이벤트 기록 → 개별 사건의 상세 원인 분석.
4. SDK·Collector·OTLP : 계측 API와 SDK가 데이터 생성, Collector가 수신·처리·내보내기 → 백엔드 교체와 공통 파이프라인 지원.

## Ⅲ. OpenTelemetry의 구조 (흐름)

- 핵심 요약 : 계측 API·SDK → Resource·Semantic Attributes 부착 → OTLP 전송 → Collector 수신·필터·배치·샘플링 → 백엔드 내보내기 → 경보·분석.

```text
계측 API·SDK
   ↓
Resource·Semantic Attributes 부착
   ↓
OTLP 전송
   ↓
Collector 수신·필터·배치·샘플링
   ↓
백엔드 내보내기
   ↓
경보·분석
```

```text
애플리케이션 SDK
  ├ traces: span·context
  ├ metrics: measurements
  └ logs: events
         ↓ OTLP
OpenTelemetry Collector
receivers → processors → exporters
```

## Ⅳ. OpenTelemetry의 비교

- 핵심 요약 : 벤더별 APM(Application Performance Monitoring, 애플리케이션 성능 모니터링) 에이전트: 특정 공급자 SDK·백엔드에 결합; OpenTelemetry: 개방 표준·중립 계측 API·SDK·프로토콜.

| 비교 대상 | 핵심 특성 | 적용·판단 기준 |
| --- | --- | --- |
| 벤더별 APM 에이전트 | 특정 공급자 SDK·백엔드에 결합 | 단일 관측도구·전용 기능이 우선 |
| OpenTelemetry | 개방 표준·중립 계측 API·SDK·프로토콜 | 다중 백엔드·이식성·공통 계측 |
| Prometheus | 메트릭 수집·질의 생태계 중심 | 메트릭 우선 관측과 scrape 모델 |

## Ⅴ. OpenTelemetry의 한계와 방안

- 핵심 요약 : 위험 초점: 고카디널리티·민감속성·잘못된 컨텍스트 전파·계측 누락·중복. 권고 대응은 통제·책임을 명확히 해 분산 시스템의 상태와 장애원인을 상호운용 가능한 계측 데이터로 파악해 서비스 신뢰성과 운영효율을 높임.

| 위험 | 원인·영향 | 대응통제 | 지표 예시 |
| --- | --- | --- | --- |
| 고카디널리티·민감속성 | 저장비용·성능부하·개인정보 노출 | 속성 허용목록·마스킹·카디널리티 예산 | 시계열 수, 속성 유출 점검 |
| 잘못된 컨텍스트 전파 | 분산 추적이 끊기거나 서로 다른 요청을 연결 | 전파 규약·비동기 경계·샘플링 검증 | trace 연결률, orphan span |
| 계측 누락·중복 | 서비스별 계측편차가 관측 사각지대 생성 | 공통 semantic convention·자동계측 범위 점검 | 서비스 계측률, 중복 비율 |

## Ⅵ. OpenTelemetry 적용에 대한 기술사적 제언

- 핵심 요약 : 적용 원칙: 분산 시스템의 상태와 장애원인을 상호운용 가능한 계측 데이터로 파악해 서비스 신뢰성과 운영효율을 높임.
- 실행 제언 : 플랫폼팀은 공통 시맨틱 규약·속성정책·Collector 구성을 제공하고, 서비스팀은 사용자 영향을 설명하는 트레이스·메트릭·로그를 함께 설계하되 데이터 최소화와 비용한도를 운영.

## Ⅶ. 결론

- 핵심 요약 : OpenTelemetry는 애플리케이션·인프라의 텔레메트리를 생성·수집·처리·전송하기 위한 벤더 중립 관측성 프레임워크와 규격.
- 시사점 : OpenTelemetry는 관측 데이터를 교환·상관시키는 벤더 중립 계측기반이며, 서비스 문제를 사용자 요청의 전체 경로와 연결해 분석.
