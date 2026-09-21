---
sidebar:
  order: 135
  label: "135. 빅데이터 플랫폼 아키텍처"
  badge:
    text: "A"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-20T09:30:00+09:00"
tags:
  - "notes-data"
weight: 135
title: "빅데이터 플랫폼 아키텍처(5계층)와 람다·카파 및 데이터 레이크하우스 진화"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
  question_no: "135"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>빅데이터·분석 아키텍처</span><strong>빅데이터 플랫폼 아키텍처</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- 4 Main Pipeline Stages -->
  <g fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5">
    <rect x="15" y="20" width="115" height="150" rx="6"/>
    <rect x="140" y="20" width="115" height="150" rx="6"/>
    <rect x="265" y="20" width="115" height="150" rx="6"/>
    <rect x="390" y="20" width="115" height="150" rx="6"/>
  </g>

  <!-- Headers -->
  <rect x="15" y="20" width="115" height="32" rx="6" fill="#3b82f6" fill-opacity="0.15"/>
  <text x="72" y="41" text-anchor="middle" font-size="11" font-weight="bold" fill="#1d4ed8">1. 수집 계층</text>
  <text x="72" y="70" text-anchor="middle" font-size="10" fill="#334155">Apache Kafka</text>
  <text x="72" y="90" text-anchor="middle" font-size="10" fill="#334155">Debezium (CDC)</text>
  <text x="72" y="110" text-anchor="middle" font-size="10" fill="#334155">Fluentbit / NiFi</text>
  <text x="72" y="145" text-anchor="middle" font-size="9" fill="#64748b">실시간·배치 유입</text>

  <rect x="140" y="20" width="115" height="32" rx="6" fill="#0ea5e9" fill-opacity="0.15"/>
  <text x="197" y="41" text-anchor="middle" font-size="11" font-weight="bold" fill="#0284c7">2. 저장 계층</text>
  <text x="197" y="70" text-anchor="middle" font-size="10" fill="#334155">AWS S3 / HDFS</text>
  <text x="197" y="90" text-anchor="middle" font-size="10" font-weight="bold" fill="#0284c7">Apache Iceberg</text>
  <text x="197" y="110" text-anchor="middle" font-size="10" fill="#334155">Delta Lake</text>
  <text x="197" y="145" text-anchor="middle" font-size="9" fill="#64748b">오픈 테이블 포맷</text>

  <rect x="265" y="20" width="115" height="32" rx="6" fill="#10b981" fill-opacity="0.15"/>
  <text x="322" y="41" text-anchor="middle" font-size="11" font-weight="bold" fill="#059669">3. 처리 계층</text>
  <text x="322" y="70" text-anchor="middle" font-size="10" fill="#334155">Batch: Spark</text>
  <text x="322" y="90" text-anchor="middle" font-size="10" fill="#334155">Stream: Flink</text>
  <text x="322" y="110" text-anchor="middle" font-size="10" fill="#334155">SQL: DuckDB</text>
  <text x="322" y="145" text-anchor="middle" font-size="9" fill="#64748b">스토리지-컴퓨트 분리</text>

  <rect x="390" y="20" width="115" height="32" rx="6" fill="#f59e0b" fill-opacity="0.15"/>
  <text x="447" y="41" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">4. 서빙 계층</text>
  <text x="447" y="70" text-anchor="middle" font-size="10" fill="#334155">Trino (SQL 엔진)</text>
  <text x="447" y="90" text-anchor="middle" font-size="10" fill="#334155">ClickHouse / Redis</text>
  <text x="447" y="110" text-anchor="middle" font-size="10" fill="#334155">BI: Superset</text>
  <text x="447" y="145" text-anchor="middle" font-size="9" fill="#64748b">초저지연 대시보드</text>

  <!-- Connecting Arrows -->
  <path d="M 130 95 L 140 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <path d="M 255 95 L 265 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <path d="M 380 95 L 390 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>

  <!-- Layer 5: Common Governance Bottom -->
  <rect x="15" y="185" width="490" height="75" rx="6" fill="#f8fafc" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="260" y="208" text-anchor="middle" font-size="11" font-weight="bold" fill="#6d28d9">5. 공통 데이터 거버넌스 및 카탈로그 계층 (Cross-cutting Layer)</text>
  <text x="260" y="228" text-anchor="middle" font-size="10" fill="#334155">메타데이터 카탈로그(DataHub) ┃ 통합 보안·접근 통제(Apache Ranger) ┃ 데이터 품질 검증(Great Expectations)</text>
  <text x="260" y="246" text-anchor="middle" font-size="9" fill="#64748b">람다(이중 코드 부채) ──► 카파(단일 스트림 재처리) ──► 레이크하우스(ACID 테이블 통합)로 진화</text>

  <defs>
    <marker id="arrow135" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **페타바이트급 대용량 정형·비정형 데이터를 실시간 및 배치로 수집, 저장, 처리, 분석, 서빙하기 위해 분산 컴퓨팅 인프라를 5계층(수집-저장-처리-서빙-거버넌스)으로 유기적으로 결합한 엔드투엔드(End-to-End) 전사 데이터 참조 아키텍처**
- 암기: `수-저-처-서-거` (5대 계층: 수집, 저장, 처리, 서빙, 거버넌스) / `람-카-레` (아키텍처 진화: 람다 Lambda, 카파 Kappa, 레이크하우스 Lakehouse) / `브-실-골` (메달리온 아키텍처: Bronze 원천, Silver 정제, Gold 집계)
- 판단축:
  - **람다 아키텍처 (Lambda)**: 배치 레이어(정확성)와 스피드 레이어(실시간성) 병렬 운영, 코드 이원화 부채 발생
  - **카파 아키텍처 (Kappa)**: 배치 레이어를 제거하고 카프카 로그 기반 단일 스트림 엔진(Flink)으로 재처리 일원화
  - **데이터 레이크하우스 (Lakehouse)**: 저비용 오브젝트 스토리지(S3) 위에 오픈 테이블 포맷(Iceberg)을 얹어 배치와 스트리밍 쓰기 모두에 ACID 보장
- 주의: 람다 아키텍처 적용 시 비즈니스 집계 룰이 변경될 때 배치 코드(Spark)와 스트림 코드(Flink)를 동시에 완벽히 수정하지 않으면 배치 결과와 실시간 대시보드 숫자가 불일치하는 심각한 정합성 오류 발생

## 예상문제

> 빅데이터 플랫폼 아키텍처의 5대 계층 구조를 설명하고, 대용량 실시간 처리를 위한 람다(Lambda) 아키텍처와 카파(Kappa) 아키텍처의 동작 원리 및 장단점을 비교한 후, 현대적 데이터 레이크하우스(Data Lakehouse)로의 진화 방향을 기술하시오. (25점)

## Ⅰ. 데이터 가치 창출의 기반 인프라: 빅데이터 플랫폼 개요

#### 한줄 요약: 실시간 이벤트 스트림과 페타바이트 대용량 데이터를 단절 없이 수집·저장·분석하여 데이터 제품으로 서빙하는 통합 인프라

- **배경**:
  - 기업 내 데이터가 로그, 센서 IoT, 모바일 클릭스트림 등 비정형 형태로 폭증하고 초저지연 분석 요구가 증대됨에 따라 기존 RDBMS 중심의 DW 인프라 한계 봉착
  - 분산 환경에서의 고가용성, 탄력적 스케일아웃, 스토리지와 컴퓨팅의 분리(Disaggregation)를 지원하는 표준 참조 아키텍처 필요
- **정의**: 대규모 데이터의 전체 생명주기(수집 $\rightarrow$ 저장 $\rightarrow$ 처리 $\rightarrow$ 서빙 $\rightarrow$ 거버넌스)를 엔지니어링 관점에서 지원하는 분산 소프트웨어 스택의 유기적 결합체

## Ⅱ. 엔드투엔드 5대 계층 구조 및 핵심 기술 스택

#### 한줄 요약: 파이프라인의 흐름에 따른 수집, 저장, 처리, 서빙 및 전 계층을 관통하는 거버넌스 계층

| 아키텍처 계층 | 핵심 기능 및 역할 | 표준 기술 스택 |
|:---|:---|:---|
| **1. 수집 계층 (Ingestion)** | 다양한 이종 소스(RDB CDC, 웹 로그, 센서)로부터 데이터를 무손실 버퍼링 수집 | **Apache Kafka**, Debezium(CDC), Fluentbit, Apache NiFi, AWS Kinesis |
| **2. 저장 계층 (Storage)** | 저비용 무제한 확장 스토리지 및 트랜잭션 보장 테이블 포맷 제공 | **AWS S3 / HDFS**, **Apache Iceberg**, Delta Lake, Apache Hudi |
| **3. 처리 계층 (Processing)** | 분산 컴퓨팅 엔진을 통한 대규모 배치 변환(ETL) 및 실시간 이벤트 스트림 연산 | **Apache Spark** (배치), **Apache Flink** (스트리밍), Apache Beam |
| **4. 서빙 계층 (Serving)** | 분석가와 비즈니스 앱이 즉시 소비할 수 있도록 초고속 쿼리 및 대시보드 제공 | **Trino** (애드혹 SQL), **ClickHouse** (실시간 OLAP), Redis, Superset |
| **5. 거버넌스 계층 (Governance)** | 전사 메타데이터 카탈로그, 데이터 계보(Lineage), 보안/권한 통제 및 품질 모니터링 | **DataHub, Apache Atlas**, Apache Ranger (RBAC), Great Expectations |

## Ⅲ. 실시간·배치 통합 처리 패러다임: 람다(Lambda) vs 카파(Kappa)

#### 한줄 요약: 이원화 병렬 파이프라인의 람다와 단일 스트림 재처리의 카파

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Top Half: Lambda -->
  <text x="25" y="25" font-size="11" font-weight="bold" fill="#1d4ed8">[람다(Lambda) 아키텍처: 이원화 파이프라인]</text>
  <rect x="25" y="40" width="80" height="60" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="65" y="75" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">원천 데이터</text>

  <!-- Speed Layer -->
  <path d="M 105 55 L 150 45" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <rect x="150" y="30" width="190" height="30" rx="4" fill="#fee2e2" stroke="#ef4444" stroke-width="1"/>
  <text x="245" y="50" text-anchor="middle" font-size="10" fill="#b91c1c">스피드 레이어 (Storm/Flink, 실시간 뷰)</text>

  <!-- Batch Layer -->
  <path d="M 105 85 L 150 95" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <rect x="150" y="80" width="190" height="30" rx="4" fill="#dbeafe" stroke="#3b82f6" stroke-width="1"/>
  <text x="245" y="100" text-anchor="middle" font-size="10" fill="#1d4ed8">배치 레이어 (Hadoop/Spark, 배치 뷰)</text>

  <!-- Merge Serving -->
  <path d="M 340 45 L 385 55" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <path d="M 340 95 L 385 85" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <rect x="385" y="45" width="115" height="50" rx="4" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
  <text x="442" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="#b45309">서빙 레이어</text>
  <text x="442" y="84" text-anchor="middle" font-size="9" fill="#78350f">두 뷰 결과 병합</text>

  <!-- Bottom Half: Kappa -->
  <line x1="15" y1="125" x2="505" y2="125" stroke="#e2e8f0" stroke-width="1"/>
  <text x="25" y="145" font-size="11" font-weight="bold" fill="#047857">[카파(Kappa) 아키텍처: 단일 스트림 파이프라인]</text>

  <rect x="25" y="160" width="80" height="45" rx="4" fill="#ffffff" stroke="#94a3b8" stroke-width="1"/>
  <text x="65" y="187" text-anchor="middle" font-size="10" font-weight="bold" fill="#1e293b">원천 데이터</text>

  <path d="M 105 182 L 150 182" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <rect x="150" y="160" width="200" height="45" rx="4" fill="#dcfce7" stroke="#10b981" stroke-width="1"/>
  <text x="250" y="180" text-anchor="middle" font-size="10" font-weight="bold" fill="#047857">Kafka 영구 로그 + Flink 스트림 처리</text>
  <text x="250" y="196" text-anchor="middle" font-size="9" fill="#065f46">실시간 처리 및 과거 데이터 오프셋 Replay</text>

  <path d="M 350 182 L 385 182" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>
  <rect x="385" y="160" width="115" height="45" rx="4" fill="#fef3c7" stroke="#f59e0b" stroke-width="1"/>
  <text x="442" y="180" text-anchor="middle" font-size="10" font-weight="bold" fill="#b45309">서빙 레이어</text>
  <text x="442" y="196" text-anchor="middle" font-size="9" fill="#78350f">단일 실시간 서빙</text>
</svg>
</div>

1. **람다 아키텍처 (Lambda Architecture)**:
   - **배치 레이어**: 불변 원천 데이터 전체를 보관하고, 주기적으로 무거운 분산 배치(Spark)를 돌려 오차 없는 정확한 뷰 생성
   - **스피드 레이어**: 배치 주기 사이에 유입되는 최근 데이터를 실시간 스트림(Flink)으로 처리하여 저지연 뷰 제공
   - **서빙 레이어**: 사용자의 질의 시점에 배치 뷰와 실시간 뷰를 결합하여 최종 응답 반환
   - **치명적 단점**: 동일한 비즈니스 로직을 배치 코드와 스트림 코드로 이중 개발·유지보수해야 하는 극심한 코드 부채 발생
2. **카파 아키텍처 (Kappa Architecture)**:
   - 람다의 이중 코드 문제를 해결하기 위해 배치 레이어를 전면 폐지
   - Kafka에 원천 이벤트를 보관하고, 단일 스트림 처리 엔진(Flink)으로 실시간 처리와 과거 데이터 재처리(Log Replay)를 단일 코드로 일원화

## Ⅳ. 데이터 레이크하우스(Data Lakehouse)와 메달리온 패턴

#### 한줄 요약: 오브젝트 스토리지의 경제성과 데이터 웨어하우스의 ACID 무결성을 결합한 현대적 종착지

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 120" width="100%" height="120" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Bronze -->
  <rect x="25" y="25" width="135" height="70" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="92" y="50" text-anchor="middle" font-size="11" font-weight="bold" fill="#b45309">Bronze (Raw Data)</text>
  <text x="92" y="68" text-anchor="middle" font-size="9" fill="#78350f">원천 변경 없는 원시 적재</text>
  <text x="92" y="82" text-anchor="middle" font-size="8" fill="#64748b">JSON, Kafka 덤프, 로그</text>

  <path d="M 160 60 L 195 60" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>

  <!-- Silver -->
  <rect x="195" y="25" width="135" height="70" rx="6" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
  <text x="262" y="50" text-anchor="middle" font-size="11" font-weight="bold" fill="#334155">Silver (Cleaned Data)</text>
  <text x="262" y="68" text-anchor="middle" font-size="9" fill="#334155">정제, 스키마 강제, 중복제거</text>
  <text x="262" y="82" text-anchor="middle" font-size="8" fill="#64748b">Apache Iceberg 테이블</text>

  <path d="M 330 60 L 365 60" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow135)"/>

  <!-- Gold -->
  <rect x="365" y="25" width="135" height="70" rx="6" fill="#fef9c3" stroke="#eab308" stroke-width="1.5"/>
  <text x="432" y="50" text-anchor="middle" font-size="11" font-weight="bold" fill="#a16207">Gold (Business Data)</text>
  <text x="432" y="68" text-anchor="middle" font-size="9" fill="#a16207">비즈니스 집계 KPI 마트</text>
  <text x="432" y="82" text-anchor="middle" font-size="8" fill="#64748b">BI 리포트 및 AI 특화 피처</text>
</svg>
</div>

- **개념**: S3/HDFS와 같은 저비용 객체 스토리지 위에 **Apache Iceberg / Delta Lake** 오픈 테이블 포맷을 도입하여 스냅샷 격리, ACID 트랜잭션, 타임 트래블(Time Travel), 스키마 진화를 제공
- **메달리온 아키텍처 (Medallion Pattern)**:
  - **Bronze**: 원천에서 유입된 변경 없는 원시 데이터 보관 (Raw Ingestion)
  - **Silver**: 결측치 정제, 개인정보 가명처리, 비즈니스 엔티티 결합 (Enriched & Filtered)
  - **Gold**: 현업 부서별 KPI 집계 및 머신러닝 피처 스토어로 서빙 (Aggregated Business Mart)

## Ⅴ. 람다 vs 카파 vs 데이터 레이크하우스 상세 비교

#### 한줄 요약: 파이프라인 복잡도, 일관성, 운영 비용 관점에서의 비교

| 비교 항목 | 람다 아키텍처 (Lambda) | 카파 아키텍처 (Kappa) | 데이터 레이크하우스 (Lakehouse) |
|:---|:---|:---|:---|
| **처리 파이프라인** | **배치 + 스트림 (이원화 병렬)** | **단일 스트림 파이프라인** | **단일 스토리지 기반 배치/스트림 통합** |
| **코드베이스** | **2벌 작성 (배치용 + 스트림용)** | 1벌 작성 (스트림 처리 엔진) | 1벌 작성 (Iceberg ACID 기반) |
| **대규모 재처리** | 배치 레이어에서 자연스럽게 수행 | Kafka 오프셋 재설정 (리소스 부담 큼) | **테이블 타임 트래블 및 파티션 스왑** |
| **데이터 정합성** | 서빙 뷰 병합 시 불일치 위험 | 단일 스트림으로 정합성 우수 | **ACID 트랜잭션으로 완벽한 일관성** |
| **대표 기술** | Spark + Flink + Cassandra | Kafka + Flink + ClickHouse | **S3 + Apache Iceberg + Spark/Trino** |

## Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 작은 파일 문제(Small File Problem), 스트림 백엔드 OOM, 스토리지-컴퓨팅 분리

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **데이터 레이크에 100만 개 작은 파일 누적으로 쿼리 마비** | 스트리밍 엔진이 초 단위로 소용량 Parquet 파일을 커밋하여 네임노드/메타스토어 병목 | Apache Iceberg의 **Compaction(비동기 파일 압축)** 백그라운드 프로시저 가동 |
| **Flink 스트리밍 장기 가동 시 RocksDB 상태 OOM** | 윈도우 조인 및 긴 상태(State) 데이터가 메모리를 초과하여 파드 강제 종료 | 증분 체크포인트(Incremental Checkpointing) 활성화 및 상태 TTL(유효시간) 강제 설정 |
| **야간 배치 폭증 시 인프라 자원 부족** | 온프레미스 고정 클러스터의 물리적 컴퓨팅 용량 한계 | 클라우드 객체 스토리지와 연산 엔진을 분리하여 배치 시간에만 컨테이너 스케일아웃 |

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 빅데이터 플랫폼의 역사는 "데이터의 실시간성(Latency)"과 "역사적 정확성(Accuracy)" 사이의 끝없는 줄다리기였다.
> 람다 아키텍처는 둘을 모두 취하려다 '코드 중복과 결과 불일치'라는 괴물을 낳았고, 카파 아키텍처는 과거 재처리의 인프라 비용 한계에 부딪혔다.
> 오늘날 이 전쟁을 끝낸 영웅은 바로 **"오픈 테이블 포맷(Apache Iceberg) 기반의 데이터 레이크하우스"**이다.
> 스토리지 수준에서 ACID 트랜잭션과 스냅샷 격리를 보장함으로써, 스트리밍 쓰기와 배치 조회가 단 하나의 테이블에서 안전하게 공존할 수 있게 되었다.
>
> **[나라면 이렇게 쓴다]**
> 결론부에서 "데이터 레이크하우스와 데이터 메시(Data Mesh)의 조직적 융합"을 제언하겠다. 기술적으로는 Apache Iceberg와 Trino 기반의 단일 레이크하우스 인프라를 구축하되, 거버넌스적으로는 각 비즈니스 도메인 팀이 자체 데이터 제품(Data Product)을 책임지고 배포하는 '탈중앙화 데이터 메시 거버넌스'를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 배치-실시간 데이터 불일치를 해소하고 운영 TCO를 절감하기 위해 데이터 레이크하우스 중심의 빅데이터 플랫폼 현대화가 필수적임.
- **대응**:
  1. **오픈 테이블 포맷 표준화**: 벤더 종속을 탈피하고 ACID를 확보하기 위해 전사 스토리지를 Apache Iceberg로 일원화.
  2. **메달리온 아키텍처 파이프라인 구축**: Bronze(원천), Silver(정제), Gold(비즈니스 마트)의 3단계 정제 파이프라인을 dbt로 표준화.
  3. **통합 거버넌스 프레임워크 연계**: DataHub 카탈로그와 Apache Ranger를 결합하여 단일 보안 및 메타데이터 계보 관리.
- **검증**: 실시간-배치 정산 결과 일치율 100%, 쿼리 P95 응답시간 2초 이내 및 컴팩션을 통한 파일 수 90% 감축 검증.
- **효과**: 람다 아키텍처 대비 파이프라인 개발 공수 50% 절감 및 전사 데이터 레이크 쿼리 속도 10배 향상.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">람다의 코드 이원화 부채, 배치-실시간 데이터 불일치, 작은 파일 병목</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">5계층 아키텍처 정립, Apache Iceberg 기반 레이크하우스 단일화</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">ACID 트랜잭션 무결성, 정산 일치율 100%, Compaction 자동화</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">유지보수 비용 50% 절감 및 초고속 실시간 의사결정 체계 완성</div>
  </div>
</div>

---

## 1교시 10점 답안 발췌

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | 대규모 데이터를 수집, 저장, 처리, 서빙, 관리하기 위해 분산 컴퓨팅 기술을 결합한 5계층 엔드투엔드 데이터 플랫폼 |
| **2. 5대 계층** | 수집(Kafka/CDC), 저장(S3/Iceberg), 처리(Spark/Flink), 서빙(Trino/ClickHouse), 거버넌스(DataHub/Ranger) |
| **3. 람다 vs 카파** | - **람다**: 배치와 스피드 레이어 병렬 운영, 코드 이원화 부채 존재<br/>- **카파**: 배치 제거, Kafka 로그 기반 단일 스트림 재처리로 일원화 |
| **4. 레이크하우스 진화** | 저비용 S3 위에 Apache Iceberg 오픈 테이블 포맷을 도입하여 ACID 트랜잭션과 메달리온(Bronze/Silver/Gold) 아키텍처 완성 |

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제126회 정보관리 1교시: 빅데이터 플랫폼 아키텍처의 계층별 구성요소와 람다(Lambda) 및 카파(Kappa) 아키텍처의 비교
- **검증 출처**:
  - Michael Armbrust et al., "Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics", CIDR
  - Nathan Marz & James Warren, "Big Data: Principles and best practices of scalable realtime data systems", Manning

---

## 학습 체크

- [ ] 빅데이터 플랫폼의 5대 계층(수집, 저장, 처리, 서빙, 거버넌스)과 대표 오픈소스 기술을 도식화할 수 있는가?
- [ ] 람다 아키텍처의 배치/스피드 레이어 구조와 이중 코드 문제점, 그리고 카파 아키텍처의 해결 원리를 비교할 수 있는가?
- [ ] Apache Iceberg를 활용한 데이터 레이크하우스와 메달리온(Bronze/Silver/Gold) 아키텍처의 개념을 설명할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-112 빅데이터](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/112_big_data.md)
- 연관 토픽: [03-007 데이터 레이크](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/007_data_lake.md), [03-134 빅데이터 분석도구 선택 원칙](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/134_big_data_analytics_tool_selection_principles.md)
