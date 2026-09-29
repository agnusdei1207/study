---
title: "ELK 스택"
author: "Claude Code"
date: "2026-09-30T15:18:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

자료처리·데이터 → 로그·검색 분석 → **ELK 스택**

## 30초 인출

- 본질: ELK 스택은 Elasticsearch(검색·분석), Logstash(수집·변환), Kibana(시각화)를 조합해 로그·이벤트를 검색 가능한 형태로 분석하는 스택
- 메커니즘: 수집기(Beats)가 로그를 모아 Logstash가 파싱·정규화하고, Elasticsearch가 샤드에 문서와 역색인으로 저장하면 검색어가 용어 사전에서 문서 ID 목록을 찾아 Kibana로 탐색
- 통찰: 로그가 늘면 색인·검색 비용이 커지므로 인덱스 수명주기(Hot·Warm·Cold·Delete)로 보존 비용을 관리하고, 유입 급증과 파싱 규칙 변경에 따른 지연·필드 의미 변화는 버퍼와 매핑 버전 관리로 통제

<details>
<summary>핵심 용어</summary>

- **ELK 스택(Elastic Stack)** : Elasticsearch·Logstash·Kibana(와 Beats)의 조합
- **Beats** : 각 노드에서 로그·메트릭을 가볍게 수집하는 에이전트
- **Logstash** : 입력 → 필터 → 출력 단계로 데이터를 변환하는 파이프라인
- **Elasticsearch** : Lucene 기반의 분산 검색·분석 엔진
- **역색인(Inverted Index)** : 용어에서 문서 목록을 찾는 색인
- **샤드(Shard)** : 인덱스를 나눈 저장·검색 단위(Primary·Replica)
- **ILM(Index Lifecycle Management)** : 인덱스를 Hot·Warm·Cold·Delete 단계로 관리하는 정책

</details>

---

## 2~4교시 예상문제 (25점)

> ELK 스택의 구성요소와 로그 처리 흐름, 인덱스 수명주기 관리를 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. ELK 스택의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **ELK 스택** 은 데이터를 수집·변환·색인·검색·시각화하는 구성요소의 조합 |
| 목적 | 로그·이벤트를 검색 가능하게 분석해 운영 현황과 문제 진단 지원 |

## Ⅱ. 구성요소와 특징

| 구성요소 | 역할 | 특징 |
|---|---|---|
| Beats | 경량 수집기 | 각 노드에 상주해 로그(Filebeat)·메트릭(Metricbeat) 수집 |
| Logstash | 전처리 파이프라인 | 입력 → 필터 → 출력, Grok 파싱 등 |
| Elasticsearch | 분산 검색·분석 엔진 | Lucene 기반 색인과 Primary·Replica 샤드, 가용성은 클러스터 구성에 좌우 |
| Kibana | 탐색·시각화 | 차트·대시보드, 필요 시 경보 규칙 |

## Ⅲ. 로그 처리와 역색인

```text
서비스 로그 → Beats → (버퍼) → Logstash 파싱·필드 정규화
   → Elasticsearch 샤드에 문서·역색인 저장
검색어 → 용어 사전 → 문서 ID 목록 → 검색 결과 → Kibana 탐색
```

```text
Doc1: "Spring Cloud"   Doc2: "Spring Boot"
   ↓ 토큰화·색인
Spring → [Doc1, Doc2] / Cloud → [Doc1] / Boot → [Doc2]
검색 "Spring" → 문서 ID 목록으로 결과 구성
```

## Ⅳ. 인덱스 수명주기 관리(ILM)

| 단계 | 일반적 상태 | 정책 판단 |
|---|---|---|
| Hot | 새 로그 색인·빈번한 조회 | 쓰기·검색 부하에 필요한 자원 배치 |
| Warm | 쓰기 완료·조회 감소 | 읽기 전환·병합 등 필요에 따라 선택 |
| Cold | 드문 조회 | 검색 허용 시간·비용에 맞는 저장 방식 |
| Delete | 보존 기간 만료 | 법정·업무 보존 요구 확인 후 삭제 |

계층 사용 여부와 이동 시점은 고정값이 아니며 환경·라이선스·조회 요구에 따라 결정.

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 로그 증가와 색인 분할이 자원·검색 비용 증가 | 검색·보존 목표에 맞춰 샤드·수명주기를 부하 시험 후 설정 |
| 유입 급증이 색인 처리량 초과, 지연·누락 위험 | 버퍼·역압·재시도, 입력·색인 적체 지표 관리 |
| 파싱 규칙 변경으로 필드 의미 변화 | 필드 정의·매핑 버전 관리, 대표 로그로 검색 회귀 검증 |

## Ⅵ. 제언

보존 요구와 조회 빈도로 수명주기를 정하고, 유입 급증에 대비해 버퍼와 적체 지표를 운영

```text
수집 → 버퍼 → 파싱 → 색인(Hot) → Warm → Cold → 보존 만료 시 Delete
```

| 구분 | 전 로그 동일 보존 | 제언: 수명주기별 관리 |
|---|---|---|
| 비용 | 증가 | 단계별 절감 |
| 검색 | 전체 부하 | 조회 빈도에 맞춤 |

## 출제 이력과 검증 출처

- 제132회 1교시 7번: ELK(Elasticsearch/Logstash/Kibana) 스택
- Elastic 공식 문서(Elasticsearch·Logstash·Kibana, Index Lifecycle Management)

## 연결 토픽

- 연관 토픽: [데이터 관측가능성](./054_data_observability.md), [빅데이터](./112_big_data.md), [NoSQL](./001_nosql.md)
