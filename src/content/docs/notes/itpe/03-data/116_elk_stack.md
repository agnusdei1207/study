---
sidebar:
  order: 116
  label: "116. ELK 스택"
  badge:
    text: "서브"
    variant: note
title: "ELK(Elasticsearch·Logstash·Kibana) 스택 기반 분산 로그 분석 및 관측성 플랫폼"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 116
extra:
  model: "GPT-6"
  keyword_grade: "서브"
  question_no: "116"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>빅데이터 플랫폼·검색엔진</span><strong>ELK 스택</strong></div>

## 30초 인출



- 본질: **Elastic Stack은 로그·이벤트를 수집·변환·색인·검색·시각화해 운영 상태를 분석하는 데이터 플랫폼**
- 메커니즘: 로그 수집·변환 → Elasticsearch의 색인·검색 → Kibana의 탐색·시각화로 운영 데이터를 분석
- 통찰: 한계: 로그 증가와 색인 분할은 자원·검색 비용을 키움 → 방안: 검색·보존 목표에 맞춰 샤드·수명주기 정책을 부하 시험 뒤 설정
<details><summary>핵심 용어</summary>

- **Elastic Stack** : 로그·이벤트의 수집, 변환, 검색·분석, 시각화를 지원하는 구성요소 묶음.
- **Beats** : 서버에서 로그·메트릭 등을 수집해 전송하는 경량 데이터 수집기 계열.
- **Logstash** : 입력 데이터를 필터로 변환한 뒤 출력 대상으로 전달하는 데이터 처리 파이프라인.
- **Elasticsearch** : 분산 색인과 검색·분석을 제공하는 엔진.
- **Kibana** : Elasticsearch 데이터를 탐색하고 시각화하는 인터페이스.
- **역색인 (Inverted Index)** : 용어에서 해당 용어를 포함한 문서 식별자 목록으로 연결하는 검색 자료구조.
- **ILM (Index Lifecycle Management)** : 인덱스의 생성 이후 단계별 보존·이동·삭제 정책을 관리하는 기능.

</details>

---

## 2~4교시 예상문제 (25점)

> 마이크로서비스 아키텍처(MSA) 및 클라우드 환경에서 시스템 통합 모니터링을 위한 ELK(Elasticsearch, Logstash, Kibana) 스택의 개념과 아키텍처를 제시하고, Elasticsearch의 역색인(Inverted Index) 구조 및 대규모 로그 운영을 위한 인덱스 수명주기 관리(ILM) 방안을 설명하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|:---|:---|
| 정의 | Elastic Stack은 데이터를 수집·변환·색인·검색·시각화하는 구성요소의 조합 |
| 목적 | 로그·이벤트를 검색 가능한 형태로 분석해 운영 현황과 문제 진단을 지원 |

## Ⅱ. 수집·변환·검색·시각화의 특징


| 구성요소 | 핵심 역할 | 주요 동작 메커니즘 및 특징 |
|:---|:---|:---|
| **Beats** | 경량 데이터 수집기 | 각 단말 노드에 데몬으로 상주, 최소의 CPU/RAM 자원으로 로그(Filebeat), 메트릭(Metricbeat) 수집 |
| **Logstash** | 데이터 전처리 파이프라인 | Input $\rightarrow$ Filter $\rightarrow$ Output 3단계 처리, Grok 플러그인 기반 정규표현식 파싱, GeoIP 위치 추가 |
| **Elasticsearch** | 분산 검색·분석 엔진 | Lucene 기반 색인과 Primary·Replica 샤드로 검색·분석; 가용성은 클러스터 구성에 좌우 |
| **Kibana** | 데이터 탐색 및 시각화 | Elasticsearch 데이터를 차트·대시보드로 탐색하고 필요 시 경보 규칙 구성 |

## Ⅲ. 로그 수집·역색인·검색 응답 체계

```text
서비스 로그 → Beats 수집 → 필요 시 버퍼 → Logstash 파싱·필드 정규화
                                              ↓
                     Elasticsearch 샤드에 문서·역색인 저장
                                              ↓
검색어 → 용어 사전 → 문서 ID 목록 → 검색 결과 → Kibana 탐색
```

### 용어에서 문서로 이어지는 역색인

```text
Doc1: "Spring Cloud"     Doc2: "Spring Boot"
             ↓ 토큰화·색인
Spring → [Doc1, Doc2] / Cloud → [Doc1] / Boot → [Doc2]
검색 "Spring" → 해당 문서 ID 목록을 찾아 결과 구성
```

## Ⅳ. Hot·Warm·Cold·Delete 보존 단계 비교

### 대규모 엔터프라이즈 운영: 인덱스 수명주기 관리(ILM)

| ILM 단계 | 일반적 상태 | 정책 판단 |
|:---|:---|:---|
| **Hot** | 새 로그 색인·빈번한 조회 | 쓰기·검색 부하에 필요한 자원 배치 |
| **Warm** | 쓰기 완료·조회 감소 | 읽기 전환·병합 등 작업을 필요에 따라 선택 |
| **Cold** | 드문 조회 | 검색 허용 시간·보존 비용에 맞는 저장 방식 선택 |
| **Delete** | 보존 기간 만료 | 법정·업무 보존 요구 확인 뒤 삭제 |

계층 사용 여부와 이동 시점은 고정값이 아니며, 배포 환경·라이선스·조회 요구에 따라 정한다.

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 로그 증가와 색인 분할은 자원·검색 비용을 키움 | 검색·보존 목표에 맞춰 샤드·수명주기 정책을 부하 시험 뒤 설정 |
| 유입 급증이 색인 처리량을 넘어 로그 지연·누락 위험 | 버퍼·역압·재시도와 입력·색인 적체 지표를 함께 관리 |
| 파싱 규칙 변경으로 검색 필드의 의미가 달라짐 | 필드 정의·매핑 버전을 관리하고 대표 로그로 검색 회귀 검증 |

## Ⅵ. 제언

로그 증가로 검색 지연과 저장 비용이 커지는 인덱스부터 대표 색인·검색 부하를 재현하고 샤드 수와 수명주기 정책을 조정한다.

## 출제 이력과 검증 출처

- **기출 이력** :
  - 제132회 정보관리 1교시: ELK(Elasticsearch/Logstash/Kibana) 스택
- **검증 출처** :
  - [Elastic, How many shards should I have in my Elasticsearch cluster?](https://www.elastic.co/blog/how-many-shards-should-i-have-in-my-elasticsearch-cluster)
  - [Elastic, Index lifecycle management](https://www.elastic.co/guide/en/elasticsearch/reference/current/index-lifecycle-management.html)
  - Clinton Gormley & Zachary Tong, "Elasticsearch: The Definitive Guide", O'Reilly
---

## 연결 토픽

- 상위 토픽: [015. 텍스트 마이닝 (Text Mining)](./015_text_mining.md)
- 연관 토픽: [054. 데이터 관측가능성 (Data Observability)](./054_data_observability.md), [045. 샤딩 (Sharding)](./045_sharding.md)
