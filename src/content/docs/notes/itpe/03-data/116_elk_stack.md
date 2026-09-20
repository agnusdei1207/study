---
sidebar:
  order: 116
  label: "116. ELK(Elasticsearch/Logstash/Kibana) 스택"
  badge:
    text: "기출 · 70%"
    variant: note
title: "ELK(Elasticsearch/Logstash/Kibana) 스택"
author: "Gemini 3.8 Flash"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-data"
weight: 116
extra:
  model: "Gemini 3.8 Flash"
  question_no: "116"
  source_status: "기출"
  source_history: "132회"
  priority: 70
  priority_note: "[출제:132]"
---

## 답안 골격
```text
[ELK 스택 (Elasticsearch·Logstash·Kibana)] ◀━━ 머리: Ⅶ 내 의견 (경량 Beats 수집 에이전트와 인덱스 수명주기 관리(ILM) 적용)
 ┃
 ┣━ Ⅰ 개요 ───── 분산 환경의 대규모 로그 및 이벤트를 실시간으로 수집(Logstash), 역색인 검색·저장(Elasticsearch), 시각화(Kibana)하는 오픈소스 통합 데이터 분석 플랫폼
 ┣━ Ⅱ 특징 ───── 역색인(Inverted Index) 기반 초고속 전문 검색 · 분산 샤딩 및 고가용성 · 스키마리스 JSON 지원 · 대시보드 실시간 가시성
 ┣━ Ⅲ 구조 ───── Beats(경량 수집) / Logstash(파이프라인 변환) / Elasticsearch(분산 검색·저장 엔진) / Kibana(시각화 대시보드)
 ┣━ Ⅳ 흐름 ───── ① 서버 로그 발생 → ② Beats 수집 및 Logstash 전달 → ③ 필터 플러그인 정제(Grok 파싱) → ④ ES 인덱싱 및 샤드 분산 적재 → ⑤ Kibana 시각화 및 알람
 ┣━ Ⅴ 비교 ───── ELK 스택 vs Splunk vs Prometheus/Grafana
 ┗━ Ⅵ 실무 ───── 샤드(Shard) 과다 생성으로 인한 클러스터 OOM / Logstash JVM 무거움으로 인한 서버 자원 고갈
```
- 필수 키워드: ELK 스택 · Elasticsearch · Logstash · Kibana · Beats · 역색인(Inverted Index) · 샤딩(Sharding) · Grok 필터 · 인덱스 수명주기(ILM)
- 배점 전략: 10점 = Ⅰ → Ⅲ ELK 4대 구성요소 파이프라인 구조도 → Ⅴ Splunk와의 비교 / 25점 = Ⅰ~Ⅶ, Ⅳ 로그 수집-정제-색인-시각화 파이프라인 흐름 및 Ⅵ 대용량 클러스터 운영 최적화(샤드/ILM)
- 기출: 132회 1교시 7번 `ELK(Elasticsearch/Logstash/Kibana) 스택` → Ⅰ 정의 + Ⅲ 핵심 구성요소 + Ⅳ 데이터 흐름 + Ⅵ 실무 운영 방안

## 한 줄 본질
- 수백 대의 분산 서버에서 쏟아지는 비정형 로그를 중앙에서 실시간으로 통합 분석하기 어려움 → Beats/Logstash로 수집·정제하고 Lucene 기반 역색인 엔진(ES)에 분산 저장하여 Kibana로 즉시 표출 → 실시간 가시성 확보 / 인덱스 및 JVM 메모리 폭증 위험

## 핵심 그림
```text
[ELK (Elastic) 스택의 엔드투엔드 데이터 파이프라인]

  ┌──────────────┐     ┌──────────────┐     ┌──────────────────────┐     ┌──────────────┐
  │ 1. 수집      │────►│ 2. 정제·가공 │────►│ 3. 분산 저장·색인    │────►│ 4. 시각화    │
  │ (Beats)      │     │ (Logstash)   │     │ (Elasticsearch)      │     │ (Kibana)     │
  └──────────────┘     └──────────────┘     └──────────────────────┘     └──────────────┘
   - Filebeat (로그)    - Inputs (Kafka 등)  - Master/Data Node 분리      - Discover (검색)
   - Metricbeat (지표)  - Filters (Grok/JSON)- Inverted Index (역색인)    - Dashboard (대시보드)
   - 경량 C/Go 에이전트 - Outputs (ES 전송)  - Primary/Replica 샤딩       - Alerting (알림)
```

## 핵심 용어
- 역색인(Inverted Index): 책 맨 뒤의 색인처럼, 문서 내에 등장하는 단어(Term)를 키로 두고 해당 단어가 포함된 문서 ID 리스트를 매핑하여 $O(1)$ 속도로 검색하는 핵심 자료구조
- Grok 필터: 정규표현식을 기반으로 구조화되지 않은 텍스트 로그(Apache/Nginx 로그 등)를 파싱하여 JSON 형태의 구조화된 필드로 변환하는 Logstash 플러그인

## 핵심 통찰
- Logstash는 무거운 JVM 위에서 돌기 때문에 각 애플리케이션 서버에 직접 깔면 CPU와 메모리를 잡아먹어 본업에 지장을 줌 → 경량 Go 언어 에이전트인 'Filebeat'를 서버마다 심고, 중간에 Kafka 큐를 둔 뒤 중앙 Logstash 클러스터로 모으는 것이 표준 아키텍처
- Elasticsearch 클러스터 장애의 80%는 '샤드(Shard) 남발' 때문임 → 샤드 1개당 Lucene 인스턴스가 뜨고 메모리를 먹으므로, 날짜별로 수백 개의 인덱스를 무작정 쪼개면 힙 메모리가 고갈되어 클러스터가 뻗음
- 핫-웜-콜드(Hot-Warm-Cold) 아키텍처와 인덱스 수명주기 관리(ILM)를 적용해, 7일이 지난 로그는 SSD에서 저비용 HDD 노드로 자동 강등하고 30일 후 닫아야 클라우드 비용을 통제 가능

## 이웃 토픽과 구분
- ELK 스택 vs Prometheus/Grafana: ELK = 대량의 '비정형 텍스트 로그(Log)' 전문 검색 및 이벤트 분석에 최적화 / Prometheus = 시계열 '수치 메트릭(Metric: CPU, 메모리 수치)' 수집 및 실시간 알람에 최적화

## 문제·원인·대책
- 적용 상황: 수백 개 마이크로서비스(MSA) 환경의 통합 분산 로깅 시스템 구축
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 대규모 트래픽 발생 시 로그 유실 및 Logstash 과부하로 인한 지연 폭증 | Logstash 전단 버퍼링 부재로 스파이크 트래픽 흡수 실패 | Beats와 Logstash 사이에 Apache Kafka 메시지 큐 완충 계층 배치 | 로그 유실 제로 달성 및 백프레셔(Backpressure) 해소 |
| Elasticsearch 클러스터 노드들이 잦은 GC Pause로 다운되며 마스터 노드 분리 | 날짜별 과도한 샤드 분할(샤드 크기 1GB 미만)로 인한 힙 메모리 고갈 | 인덱스당 샤드 크기를 30~50GB로 재설계하고 인덱스 수명주기(ILM) 자동화 | 힙 메모리 사용량 60% 절감 및 클러스터 안정화 |

## 이렇게 출제된다
- 제132회 1교시 7번: "ELK(Elasticsearch/Logstash/Kibana) 스택" → 요구 포인트: ELK 스택의 개념 + 각 구성요소(ES, Logstash, Kibana, Beats)의 역할과 상호작용 + 역색인 원리 + 대용량 로그 수집 파이프라인 아키텍처

## 내 의견
- [원시 로그 무차별 수집의 비용 낭비] 무조건 모든 디버그(`DEBUG`) 레벨 로그까지 ES에 적재하여 스토리지 비용이 눈덩이처럼 불어나고 정작 중요한 에러 분석 시 검색 속도가 느려지는 문제 빈발 → 나라면: 수집단 Filebeat에서 `INFO/WARN/ERROR`만 선별 수집하도록 필터링을 걸고, 비즈니스상 필수적인 3대 로그 필드(Timestamp, TraceId, ErrorCode)를 표준 JSON 포맷으로 강제하는 전사 로깅 규약 확립

## 찾아볼 것
- Elasticsearch의 라이선스 정책 변경(SSPL)에 따라 AWS가 주도하여 포크한 완전 오픈소스 검색 엔진 `OpenSearch`와의 기능 및 생태계 차이
