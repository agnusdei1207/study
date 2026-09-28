---
title: "ELK 스택"
category: "03-data"
tags:
  - "notes-data"
date: "2026-09-28T22:36:00+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
sidebar:
  badge:
    text: "기초"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>빅데이터 플랫폼·검색엔진</span><strong>ELK 스택</strong></div>

## 30초 인출



- 본질: **Elastic Stack은 로그·이벤트를 수집·변환·색인·검색·시각화해 운영 상태를 분석하는 데이터 플랫폼**
- 메커니즘: 로그 수집·변환 → Elasticsearch의 색인·검색 → Kibana의 탐색·시각화로 운영 데이터를 분석
- 통찰: 대규모 분산 로그 수집·저장·시각화를 위해 Beats-Logstash 수집 파이프라인, Elasticsearch 역색인 검색, Kibana 대시보드의 유기적 연계 및 ILM 수명주기 관리 필수
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

계층 사용 여부와 이동 시점은 고정값이 아니며, 배포 환경·라이선스·조회 요구에 따라 결정.

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 로그 증가와 색인 분할은 자원·검색 비용을 키움 | 검색·보존 목표에 맞춰 샤드·수명주기 정책을 부하 시험 뒤 설정 |
| 유입 급증이 색인 처리량을 넘어 로그 지연·누락 위험 | 버퍼·역압·재시도와 입력·색인 적체 지표를 함께 관리 |
| 파싱 규칙 변경으로 검색 필드의 의미가 달라짐 | 필드 정의·매핑 버전을 관리하고 대표 로그로 검색 회귀 검증 |

## Ⅵ. 제언

로그 급증 시 버퍼링을 위한 Kafka를 전진 배치하고 인덱스 생명주기 관리(ILM: Hot-Warm-Cold)를 적용하여 스토리지 비용 절감과 실시간 검색 성능 보장.

### ELK 스택 엔터프라이즈 로깅 파이프라인

```text
[서버/앱 로그] ──► [Filebeat 경량 수집] ──► [Kafka 버퍼링]
                                                     │
                                                     ▼
[Logstash: 필터링/파싱(Grok/JSON)] ──► [Elasticsearch: 분산 역색인 저장]
                                                     │
                                                     ▼
                                     [Kibana: 실시간 시각화 / 알람]
```

### 선택 근거: 제언: ELK 기반 통합 옵저버빌리티

| 구분 | 단순 파일 로그 적재 | 제언: ELK 기반 통합 옵저버빌리티 |
|---|---|---|
| 검색 성능 | Grep 기반 느린 순차 탐색 | 역색인(Inverted Index) 기반 밀리초 실시간 검색 |
| 분석 확장성 | 서버별 로그 사일로화 | 전사 분산 클러스터 통합 및 샤딩 수평 확장 |
| 수명주기 관리 | 수동 압축/삭제 운영 | ILM 기반 Hot-Warm-Cold 자동 티어링 |

---

## 출제 이력과 검증 출처

- 정보관리기술사 116회 1교시: ELK(Elasticsearch, Logstash, Kibana) 스택의 구성요소와 특징
- 정보관리기술사 126회 2교시: 클라우드 네이티브 환경에서 중앙 집중형 로그 관리 아키텍처
- Elasticsearch: The Definitive Guide

## 연결 토픽

- [인덱스](./047_index.md)
- [데이터 옵저버빌리티](./054_data_observability.md)
- [데이터 시각화](./016_data_visualization.md)
