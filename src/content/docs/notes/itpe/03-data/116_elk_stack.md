---
title: "ELK 스택 (ELK: Elasticsearch, Logstash, Kibana)"
author: "agnusdei1207"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## 연관 키워드

**ELK 스택**, **Elasticsearch**, **Logstash**, **Kibana**, **Beats**, **역색인(Inverted Index)**, **ILM(Index Lifecycle Management)**

## Ⅰ. 개요

- 핵심 요약 : **ELK 스택**은 로그 수집·색인·검색·시각화를 통합하는 엔드투엔드 데이터 플랫폼.
- 목적 : 분산 시스템의 대규모 로그와 시계열 데이터 실시간 분석.
- 배경 : 분산 환경 로그 폭증으로 수작업 분석 불가 → 통합 플랫폼 필요.
- 특징 : Elasticsearch(검색), Logstash(수집·가공), Kibana(시각화), Beats(경량 수집).

## Ⅱ. 특징 및 장점

- 핵심 요약 : **역색인·분산 샤딩·실시간 검색**으로 대규모 로그 고속 분석.
- **역색인** : 단어 기반 즉시 탐색, 수억 문서 검색.
- **분산 샤딩** : 자동 분산·복제로 고가용성.
- **실시간 색인** : Near Real-Time 검색.
- **시각화** : Kibana 대시보드·APM·지도.
- **확장성** : 수평 확장으로 볼륨 대응.

## Ⅲ. 파이프라인 흐름

- 핵심 요약 : **Beats → Kafka → Logstash → Elasticsearch → Kibana**.
- 역색인(Inverted Index) : 단어(Term) → 문서 목록(Posting List) 매핑.

```text
[ ELK 데이터 파이프라인 ]

[Web/App Servers]
        |
        v
[Filebeat/Metricbeat] ---> [Kafka] ---> [Logstash (가공/필터링)]
                                              |
                                              v
                                  [Elasticsearch Cluster]
                                  (역색인, 분산 샤딩)
                                              ^
                                              |
                                  [Kibana Dashboard]
```

```text
[ 역색인(Inverted Index) ]

단어 (Term)    | 문서 목록 (Posting List)
---------------+-------------------------
"Database"     | Doc 1, Doc 2
"Tuning"       | Doc 1, Doc 3
"Index"        | Doc 1, Doc 3
```

## Ⅳ. 구성 요소 비교

- 핵심 요약 : **Beats·Logstash·Elasticsearch·Kibana** 역할 분담.

| 구성 요소 | 역할 | 특징 |
|---|---|---|
| Beats | 경량 데이터 수집기 | CPU/메모리 오버헤드 극소 |
| Logstash | 수집·가공·전송 | 플러그인 풍부, JVM 부하 |
| Elasticsearch | 분산 검색·분석 엔진 | 역색인, 자동 샤딩·복제 |
| Kibana | 시각화·대시보드 | 차트, APM, 지도 |

## Ⅴ. 한계와 방안

- 핵심 요약 : **인덱싱 병목·Over-sharding·GC**를 버퍼·ILM·튜닝으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 인덱싱 병목 | 피크 시 Logstash/ES 병목 → 백프레셔 | Kafka 버퍼, Filebeat 직결, Bulk API 튜닝 | 인덱싱 지연 |
| Over-sharding | 샤드 과다로 마스터 메모리 고갈 | ILM, Rollover API, 20~50GB 유지 | 샤드 수 |
| GC 일시 정지 | Full GC로 노드 이탈 | 힙 50%(최대 31GB), G1GC 튜닝 | GC 시간 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **Kafka 버퍼·ILM·튜닝**으로 안정적 대규모 운영.
- Kafka 완충 계층 : 로그 스파이크 시 OOM 방지.
- ILM : Hot→Warm→Cold→Delete 파이프라인으로 비용 절감.
- 힙 크기 제한 및 G1GC 튜닝.

## Ⅶ. 결론

- 핵심 요약 : ELK는 **로그 수집·검색·시각화 통합 플랫폼**으로 역색인·ILM이 핵심.
- 답안에는 파이프라인, 구성 요소, 한계·대응, 실무 제언을 연결.
- 참고 : [Elastic Stack](https://www.elastic.co/elastic-stack).