---
sidebar:
  order: 116
  label: "116. ELK 스택"
  badge:
    text: "기초"
    variant: note
title: "ELK(Elasticsearch·Logstash·Kibana) 스택 기반 분산 로그 분석 및 관측성 플랫폼"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 116
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "116"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>빅데이터 플랫폼·검색엔진</span><strong>ELK 스택</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" role="img" aria-label="엔터프라이즈 ELK 및 Kafka 분산 로그 파이프라인 아키텍처">
  <defs>
    <marker id="elkArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="220" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Step 1: Filebeat -->
  <g transform="translate(15, 20)">
    <rect width="88" height="175" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="88" height="28" rx="6" fill="#f8fafc"/>
    <text x="44" y="19" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">1. Filebeat</text>
    <text x="44" y="55" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-text, #1e293b)">경량 Go 에이전트</text>
    <text x="44" y="75" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">서버/컨테이너</text>
    <text x="44" y="90" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">로그 실시간 감지</text>
    <text x="44" y="115" text-anchor="middle" font-size="8" fill="var(--sl-color-accent, #2563eb)">자원 최소화</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <path d="M 103 107 L 112 107" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#elkArr)"/>

  <!-- Step 2: Kafka Buffer -->
  <g transform="translate(115, 20)">
    <rect width="88" height="175" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="88" height="28" rx="6" fill="#f8fafc"/>
    <text x="44" y="19" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">2. Kafka</text>
    <text x="44" y="55" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-text, #1e293b)">메시지 큐 버퍼</text>
    <text x="44" y="75" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">피크 트래픽 흡수</text>
    <text x="44" y="90" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">데이터 유실 차단</text>
    <text x="44" y="115" text-anchor="middle" font-size="8" fill="var(--sl-color-accent, #2563eb)">디커플링 완충</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <path d="M 203 107 L 212 107" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#elkArr)"/>

  <!-- Step 3: Logstash -->
  <g transform="translate(215, 20)">
    <rect width="88" height="175" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="88" height="28" rx="6" fill="#f8fafc"/>
    <text x="44" y="19" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">3. Logstash</text>
    <text x="44" y="55" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-text, #1e293b)">전처리 파이프라인</text>
    <text x="44" y="75" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">Grok 정규화 파싱</text>
    <text x="44" y="90" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">JSON 구조화 변환</text>
    <text x="44" y="115" text-anchor="middle" font-size="8" fill="var(--sl-color-accent, #2563eb)">GeoIP 위치 보정</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <path d="M 303 107 L 312 107" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#elkArr)"/>

  <!-- Step 4: Elasticsearch -->
  <g transform="translate(315, 20)">
    <rect width="98" height="175" rx="6" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
    <rect width="98" height="28" rx="6" fill="var(--sl-color-accent, #dbeafe)"/>
    <text x="49" y="19" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">4. Elasticsearch</text>
    <text x="49" y="55" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">Lucene 역색인</text>
    <text x="49" y="75" text-anchor="middle" font-size="8" fill="var(--sl-color-text, #334155)">Inverted Index</text>
    <text x="49" y="90" text-anchor="middle" font-size="8" fill="var(--sl-color-text, #334155)">Primary/Replica</text>
    <text x="49" y="115" text-anchor="middle" font-size="8" font-weight="600" fill="var(--sl-color-accent, #1e40af)">ILM 수명주기</text>
  </g>

  <!-- Arrow 4 -> 5 -->
  <path d="M 413 107 L 422 107" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5" marker-end="url(#elkArr)"/>

  <!-- Step 5: Kibana -->
  <g transform="translate(425, 20)">
    <rect width="80" height="175" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="80" height="28" rx="6" fill="#f8fafc"/>
    <text x="40" y="19" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">5. Kibana</text>
    <text x="40" y="55" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-text, #1e293b)">시각화 대시보드</text>
    <text x="40" y="75" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">실시간 검색(KQL)</text>
    <text x="40" y="90" text-anchor="middle" font-size="8" fill="var(--sl-color-gray-2, #64748b)">이상 탐지 알람</text>
    <text x="40" y="115" text-anchor="middle" font-size="8" fill="var(--sl-color-accent, #2563eb)">통합 관측성</text>
  </g>
</svg>
</div>

- 본질: **분산 MSA 환경에서 발생하는 테라바이트급 비정형 로그 및 이벤트를 경량 에이전트(Beats)로 수집하고, 파이프라인 엔진(Logstash)으로 전처리·정제하여, Lucene 기반 역색인 분산 검색엔진(Elasticsearch)에 실시간 색인·저장한 후, 대시보드(Kibana)를 통해 시각화 및 관측성(Observability)을 제공하는 엔드투엔드 데이터 플랫폼**
- 암기: `비-로그-엘-키` (Beats, Logstash, Elasticsearch, Kibana) / `인-샤-레-역` (인덱스, 샤드, 레플리카, 역색인) / `핫-웜-콜-프` (ILM: Hot, Warm, Cold, Frozen)
- 판단축:
  - **Beats vs Logstash**: 각 서버에는 CPU/메모리 오버헤드가 적은 경량 Go 에이전트(Filebeat)를 배포하고, 무거운 JVM 기반 Logstash는 중앙 집중 클러스터로 격리
  - **로그 버퍼링 (Kafka 연계)**: 피크 시간대 대량 로그 유입 시 ES 클러스터의 OOM 장애를 차단하기 위해 Kafka 메시지 큐를 중간 버퍼로 배치
- 주의: 인덱스를 과도하게 세분화하여 **샤드(Shard) 수가 수천 개로 폭증**할 경우 노드 간 마스터 상태 동기화 병목 및 JVM 힙 메모리 고갈(OOM)이 발생하므로 ILM(Index Lifecycle Management) 정책 수립이 필수적임
---

## 1교시 예상문제 (10점)

> ELK(Elasticsearch·Logstash·Kibana) 스택 기반 분산 로그 분석 및 관측성 플랫폼의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### [문제] ELK 스택 (Elasticsearch·Logstash·Kibana)

#### 1. ELK 스택의 정의
- Beats(경량수집), Logstash(전처리/정제), Elasticsearch(Lucene 역색인 분산검색), Kibana(시각화)로 구성된 분산 로그 분석 및 관측성 플랫폼

#### 2. Elasticsearch 역색인(Inverted Index) 및 데이터 파이프라인

| 파이프라인 계층 | 핵심 역할 | 적용 솔루션/기법 |
|:---|:---|:---|
| **1. Edge 수집** | 단말 서버 자원 최소화 로그 수집 | Filebeat, Metricbeat |
| **2. 완충 버퍼** | 피크 트래픽 흡수 및 유실 차단 | Apache Kafka |
| **3. 정제·변환** | 비정형 문자열을 JSON 구조화 파싱 | Logstash (Grok, Dissect) |
| **4. 색인·저장** | 단어별 문서 매핑 $O(1)$ 역색인 | Elasticsearch (Lucene) |
| **5. 시각화** | 실시간 KQL 쿼리 및 대시보드 | Kibana |

- **역색인(Inverted Index)**: 문서 전체 스캔 대신 단어(Term)를 키로 문서 ID 포스팅 리스트를 매핑하여 초고속 전문 검색 실현

#### 3. 대용량 운영을 위한 인덱스 수명주기 관리(ILM)
- Hot(NVMe, 활발한 쓰기) $\rightarrow$ Warm(읽기전용, 세그먼트 병합) $\rightarrow$ Cold(스냅샷 마운트) $\rightarrow$ Delete(보관주기 만료 삭제)
---

### 핵심 관계

| 구성요소 | 핵심 역할 | 주요 동작 메커니즘 및 특징 |
|:---|:---|:---|
| **Beats** | 경량 데이터 수집기 | 각 단말 노드에 데몬으로 상주, 최소의 CPU/RAM 자원으로 로그(Filebeat), 메트릭(Metricbeat) 수집 |
| **Logstash** | 데이터 전처리 파이프라인 | Input $\rightarrow$ Filter $\rightarrow$ Output 3단계 처리, Grok 플러그인 기반 정규표현식 파싱, GeoIP 위치 추가 |
| **Elasticsearch** | 분산 검색·분석 엔진 | Apache Lucene 기반, RESTful JSON API 지원, Primary/Replica 샤딩으로 수평 확장 및 무정지 서비스 |
| **Kibana** | 데이터 탐색 및 시각화 | Elasticsearch 데이터를 실시간 차트·대시보드로 렌더링, KQL(Kibana Query Language) 지원, 알람 발송 |

---

## 2~4교시 예상문제 (25점)

> 마이크로서비스 아키텍처(MSA) 및 클라우드 환경에서 시스템 통합 모니터링을 위한 ELK(Elasticsearch, Logstash, Kibana) 스택의 개념과 아키텍처를 제시하고, Elasticsearch의 역색인(Inverted Index) 구조 및 대규모 로그 운영을 위한 인덱스 수명주기 관리(ILM) 방안을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 분산 시스템의 가시성을 확보하는 ELK 스택 개요

#### 한줄 요약: 분산 환경 전반의 로그를 실시간 수집, 정제, 역색인 분산 검색, 시각화하는 오픈소스 기반 관측성 플랫폼

- **배경**: 모놀리식에서 수백 개의 컨테이너 및 마이크로서비스(MSA)로 전환되면서, 서버별로 분산된 텍스트 로그를 개별 SSH 접속으로 추적하는 것이 불가능해짐
- **정의**: 데이터를 수집하는 **Logstash/Beats**, 대규모 데이터를 역색인 구조로 저장·검색하는 **Elasticsearch**, 데이터를 탐색하고 시각화하는 **Kibana**로 구성된 통합 로그 분석 스택
- **확장성**: 최근에는 단순 로그 분석을 넘어 APM(애플리케이션 성능 모니터링), SIEM(보안 정보 및 이벤트 관리)을 포괄하는 **통합 관측성(Observability) 플랫폼**으로 확장

### Ⅱ. ELK 스택의 4대 핵심 구성요소 및 역할

#### 한줄 요약: Beats의 경량 수집부터 Logstash 파이프라인, ES 분산 색인, Kibana 대시보드의 유기적 결합

| 구성요소 | 핵심 역할 | 주요 동작 메커니즘 및 특징 |
|:---|:---|:---|
| **Beats** | 경량 데이터 수집기 | 각 단말 노드에 데몬으로 상주, 최소의 CPU/RAM 자원으로 로그(Filebeat), 메트릭(Metricbeat) 수집 |
| **Logstash** | 데이터 전처리 파이프라인 | Input $\rightarrow$ Filter $\rightarrow$ Output 3단계 처리, Grok 플러그인 기반 정규표현식 파싱, GeoIP 위치 추가 |
| **Elasticsearch** | 분산 검색·분석 엔진 | Apache Lucene 기반, RESTful JSON API 지원, Primary/Replica 샤딩으로 수평 확장 및 무정지 서비스 |
| **Kibana** | 데이터 탐색 및 시각화 | Elasticsearch 데이터를 실시간 차트·대시보드로 렌더링, KQL(Kibana Query Language) 지원, 알람 발송 |

### Ⅲ. Elasticsearch의 핵심: 역색인(Inverted Index) 구조와 샤딩

#### 한줄 요약: 단어(Term)를 기준으로 해당 단어가 등장하는 문서 ID 목록을 매핑하여 $O(1)$ 전문 검색 속도 실현

- **원천 문서 vs 역색인 테이블 대조**:
  - Doc 1: `"Spring Cloud Gateway Log"`
  - Doc 2: `"Spring Boot Microservice"`

| 단어 (Term) | 문서 빈도 (DF) | 포스팅 목록 (Posting List: Doc ID) |
|:---|:---:|:---|
| **Boot** | 1 | [Doc 2] |
| **Cloud** | 1 | [Doc 1] |
| **Gateway** | 1 | [Doc 1] |
| **Log** | 1 | [Doc 1] |
| **Microservice** | 1 | [Doc 2] |
| **Spring** | 2 | [Doc 1, Doc 2] |

- **전문 검색(Full-text Search) 원리**: 문서 전체를 순차 스캔하지 않고, B-Tree 계열의 사전(Term Dictionary)과 압축된 포스팅 리스트를 통해 "Spring" 검색 시 즉시 `[Doc 1, Doc 2]` 반환
- **샤딩(Sharding) 및 고가용성**:
  - **Primary Shard**: 데이터 쓰기가 수행되는 원본 조각
  - **Replica Shard**: 장애 시 즉시 승격되는 복제본으로, 읽기 쿼리 부하 분산 지원

### Ⅳ. ELK 스택의 엔드투엔드 데이터 처리 파이프라인

#### 한줄 요약: Input 수신 $\rightarrow$ Filter 구조화 $\rightarrow$ Output 색인 $\rightarrow$ Visual 표출의 4단계 라이프사이클

1. **로그 수집 (Edge)**: 각 마이크로서비스 컨테이너의 stdout 로그를 `Filebeat`가 실시간 감지하여 Kafka 토픽으로 전송
2. **버퍼링 및 디커플링 (Kafka)**: 갑작스러운 이벤트 트래픽 폭증 시 ES 클러스터 보호를 위한 완충 지대 역할
3. **정제 및 정규화 (Logstash)**: Grok 필터로 비정형 로그 문자열을 JSON 키-값 구조로 파싱하고 타임스탬프 표준화
4. **분산 색인 (Elasticsearch)**: 분산 노드의 메모리 인덱싱 버퍼에 적재 후 디스크 세그먼트로 Flush하여 불변 세그먼트 생성
5. **표출 및 대응 (Kibana)**: 에러율 임계치 초과 시 Slack/이메일 Webhook 알림 자동 발송

### Ⅴ. 대규모 엔터프라이즈 운영: 인덱스 수명주기 관리(ILM)

#### 한줄 요약: 로그의 경과 시간에 따라 Hot-Warm-Cold-Delete 4단계로 인프라 비용과 성능을 최적화

| ILM 단계 | 데이터 상태 | 하드웨어 사양 | 최적화 작업 |
|:---|:---|:---|:---|
| **Hot** | 활발한 실시간 색인 및 빈번한 조회 | 초고속 NVMe SSD, 고성능 CPU | 샤드 쓰기 성능 극대화 |
| **Warm** | 쓰기 완료, 빈번한 검색 조회 | 표준 SSD, 대용량 메모리 | `ReadOnly` 전환, `Force Merge`(단일 세그먼트 병합) |
| **Cold** | 거의 조회되지 않는 감사/추적용 로그 | 저비용 HDD, 클라우드 S3/GCS | 검색 가능 스냅샷(Searchable Snapshot) 마운트 |
| **Delete** | 보관 주기(예: 30일, 90일) 만료 | 해당 없음 | 인덱스 메타데이터 및 디스크 파일 일괄 삭제 |

### Ⅵ. 실무 장애 시나리오 및 트러블슈팅 (Troubleshooting)

#### 한줄 요약: 샤드 폭증으로 인한 클러스터 OOM, Logstash 과부하, 슬로우 쿼리를 방어하는 실전 지침

| 장애 시나리오 | 발생 원인 | 엔지니어링 해결 대책 |
|:---|:---|:---|
| **클러스터 상태 Red & OOM** | 일자별 인덱스 남발로 노드당 수천 개의 샤드가 생성되어 마스터 힙 메모리 소진 | 샤드 크기를 20GB~50GB 단위로 통합 관리, 노드당 힙 1GB당 샤드 20개 이하로 제한 |
| **Logstash 백프레셔(Backpressure)** | 정규표현식 Grok 필터가 너무 복잡하여 CPU 100% 점유 및 데이터 지연 발생 | Dissect 필터(단순 구분자 분리) 우선 사용, Kafka를 전면에 배치하여 버퍼링 |
| **무제한 와일드카드 검색 쿼리** | 사용자가 `*error*` 형태의 선행 와일드카드 쿼리를 날려 수억 개 역색인 풀스캔 | N-gram 인덱스 사전 구축, Kibana 쿼리 타임아웃 및 조회 기간 제한(최대 7일) 설정 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> ELK 클러스터를 운영할 때 가장 흔한 장애는 '샤드(Shard) 폭증으로 인한 마스터 노드 OOM'이다. 하루에 수십 개씩 인덱스를 만들고 방치하면 몇 달 만에 클러스터 전체 샤드가 1만 개를 넘어서며, 마스터 노드가 샤드 상태(Cluster State)를 브로드캐스팅하다 메모리 고갈로 뻗어버린다. 샤드는 노드당 힙 메모리 1GB당 최대 20개 이하로 통제되어야 하며, 단일 샤드 크기는 30~50GB 수준으로 유지되어야 한다. 이를 위해 ILM(Index Lifecycle Management) 정책을 통해 Rollover와 Shrink, Force Merge를 자동화하는 것이 운영의 핵심이다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 Filebeat-Kafka-Logstash-ES-Kibana의 5단 파이프라인 다이어그램과 역색인(Inverted Index) 구조 표를 컴팩트하게 작성하겠다. 2교시 25점형이라면 Hot-Warm-Cold-Delete 4단계 ILM 매트릭스를 상세히 도식화하고, Elastic 라이선스 분기(SSPL)에 따른 AWS OpenSearch 전환 고려사항 및 분산 트레이싱(OpenTelemetry)과 연계한 로그-메트릭-트레이스 통합 3대 관측성(Observability) 체계를 제언에 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 로그 수집 시 샤드 수 무제한 증가로 인한 ES 마스터 노드 OOM 장애 빈발, 복잡한 Grok 필터 연산으로 Logstash CPU 병목 및 피크 트래픽 유실 위험 상존.
- **대응 (개선 방안)**: 전면에 Kafka 완충 큐를 배치하여 피크 트래픽을 흡수하고, 인덱스 크기(50GB) 기반의 Rollover 및 Hot-Warm-Cold ILM 정책 자동화, Trace ID 주입을 통한 OpenTelemetry 분산 추적 연계.
- **검증 (검증 기준)**: 노드당 힙 1GB당 샤드 수 20개 이하 준수, 피크 시간대 로그 유실율 0%, 30일 경과 콜드 인덱스 S3 티어링을 통한 스토리지 비용 60% 절감 검증.
- **효과 (실행 효과)**: 대규모 장애 원인 분석 리드타임 90% 단축(수 시간 $\rightarrow$ 수 분), 클러스터 장애 발생 빈도 제로화, 시스템 가시성 100% 확보.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">샤드 폭증으로 마스터 노드 OOM 및 피크 시 Logstash 병목·로그 유실</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">Kafka 완충 버퍼 도입 + Hot-Warm-Cold ILM 자동화 및 OTel 연계</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">샤드/힙 20개 이하 유지, 로그 유실 0%, 검색 레이턴시 1초 이내</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">장애 분석 리드타임 90% 단축, OOM 재발 방지, 스토리지 비용 60% 절감</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제132회 정보관리 1교시: ELK(Elasticsearch/Logstash/Kibana) 스택
- **검증 출처**:
  - Elastic Official Documentation, "Elasticsearch Guide & Index Lifecycle Management"
  - Clinton Gormley & Zachary Tong, "Elasticsearch: The Definitive Guide", O'Reilly
---

## 연결 토픽

- 상위 토픽: [015. 텍스트 마이닝 (Text Mining)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/015_text_mining.md)
- 연관 토픽: [054. 데이터 관측가능성 (Data Observability)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/054_data_observability.md), [045. 샤딩 (Sharding)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/045_sharding.md)
