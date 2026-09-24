---
sidebar:
  order: 118
  label: "118. MongoDB"
  badge:
    text: "기초"
    variant: note
author: "Antigravity"
category: "03-data"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 118
title: "MongoDB 문서 지향(Document-Oriented) NoSQL 아키텍처 및 샤딩·복제 체계"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "118"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>NoSQL·비정형 데이터베이스</span><strong>MongoDB</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Client -->
  <rect x="180" y="12" width="160" height="36" rx="6" fill="#3b82f6" fill-opacity="0.15" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="260" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--sl-color-text, #1e293b)">클라이언트 앱 (BSON 쿼리)</text>

  <path d="M 260 48 L 260 70" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow118)"/>

  <!-- Mongos & Config Server -->
  <rect x="60" y="72" width="180" height="42" rx="6" fill="#0ea5e9" fill-opacity="0.15" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="150" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">Mongos (쿼리 라우터)</text>
  <text x="150" y="107" text-anchor="middle" font-size="10" fill="#64748b">샤드 키 기반 요청 분기</text>

  <path d="M 240 93 L 290 93" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" marker-end="url(#arrow118)" marker-start="url(#arrow118_rev)"/>

  <rect x="290" y="72" width="180" height="42" rx="6" fill="#f59e0b" fill-opacity="0.15" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="380" y="93" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">Config Server (3노드 쿼럼)</text>
  <text x="380" y="107" text-anchor="middle" font-size="10" fill="#64748b">청크 매핑 메타데이터 관리</text>

  <!-- Routing Lines -->
  <path d="M 120 114 L 120 150" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow118)"/>
  <path d="M 180 114 L 380 150" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow118)"/>

  <!-- Shard A -->
  <rect x="25" y="152" width="220" height="115" rx="8" fill="#10b981" fill-opacity="0.08" stroke="#10b981" stroke-width="1.5"/>
  <text x="135" y="172" text-anchor="middle" font-size="12" font-weight="bold" fill="#047857">Shard A (Replica Set)</text>
  <rect x="40" y="182" width="90" height="30" rx="4" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="1"/>
  <text x="85" y="202" text-anchor="middle" font-size="11" font-weight="bold" fill="#065f46">Primary</text>
  <path d="M 130 197 L 150 197" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow118)"/>
  <rect x="150" y="182" width="80" height="30" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1"/>
  <text x="190" y="202" text-anchor="middle" font-size="11" fill="#334155">Secondary</text>
  <text x="135" y="240" text-anchor="middle" font-size="10" fill="#64748b">Oplog 비동기 복제 · 자동 Failover</text>

  <!-- Shard B -->
  <rect x="275" y="152" width="220" height="115" rx="8" fill="#8b5cf6" fill-opacity="0.08" stroke="#8b5cf6" stroke-width="1.5"/>
  <text x="385" y="172" text-anchor="middle" font-size="12" font-weight="bold" fill="#5b21b6">Shard B (Replica Set)</text>
  <rect x="290" y="182" width="90" height="30" rx="4" fill="#8b5cf6" fill-opacity="0.25" stroke="#8b5cf6" stroke-width="1"/>
  <text x="335" y="202" text-anchor="middle" font-size="11" font-weight="bold" fill="#4c1d95">Primary</text>
  <path d="M 380 197 L 400 197" stroke="#64748b" stroke-width="1.5" marker-end="url(#arrow118)"/>
  <rect x="400" y="182" width="80" height="30" rx="4" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1"/>
  <text x="440" y="202" text-anchor="middle" font-size="11" fill="#334155">Secondary</text>
  <text x="385" y="240" text-anchor="middle" font-size="10" fill="#64748b">독립 파티션 보관 · 수평 Scale-out</text>

  <defs>
    <marker id="arrow118" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
    </marker>
    <marker id="arrow118_rev" viewBox="0 0 10 10" refX="4" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 10 0 L 0 5 L 10 10 z" fill="#64748b"/>
    </marker>
  </defs>
</svg>
</div>

- 본질: **MongoDB는 BSON 문서를 컬렉션에 저장하는 문서 데이터베이스로, 문서 모델링·복제·샤딩 기능을 통해 데이터 구조와 확장 요구에 대응**
- 암기: `비-몽-컨-샤` (BSON, Mongos 라우터, Config Server, Shard Replica Set) / `임-참-애-와` (임베딩 vs 참조, 애그리게이션 파이프라인, WiredTiger 스토리지 엔진)
- 판단축:
  - **Embedding (중첩)**: 1:1 또는 유한한 1:N 관계에서 함께 조회되는 데이터, 단 1회의 디스크 I/O로 고속 완결
  - **Referencing (참조)**: 1:N에서 N이 수천 건 이상 무한 증가하거나 M:N 다대다 관계, 독립적인 갱신이 빈번한 경우
- 주의: 단일 BSON 문서의 최대 용량은 **16MB**로 엄격히 제한되므로, 무한히 누적되는 로그나 댓글을 배열로 중첩하면 문서 크기 초과 오류가 발생하므로 버킷 패턴(Bucket Pattern)이나 참조 모델로 분리 필수
---

## 1교시 예상문제 (10점)

> MongoDB 문서 지향(Document-Oriented) NoSQL 아키텍처 및 샤딩·복제 체계의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **1. 개념** | JSON 기반의 BSON 문서를 저장 단위로 사용하여 복잡한 계층 데이터를 테이블 조인 없이 처리하고, 샤딩과 복제셋으로 수평 확장을 지원하는 문서 지향 NoSQL |
| **2. 샤딩 3대 구성요소** | - **Mongos**: 쿼리 라우팅 및 분산 질의 머지 게이트웨이<br/>- **Config Server**: 청크 범위 및 라우팅 메타데이터 보관 (Raft 3노드)<br/>- **Shard Nodes**: 실제 파티션 데이터를 보관하는 독립 Replica Set |
| **3. 모델링 비교** | - **Embedding(중첩)**: 1회 I/O 고속 완결 및 단일 문서 원자성 보장, 16MB 한도 주의<br/>- **Referencing(참조)**: $lookup 조인 필요하나 무제한 용량 및 N:M 관계 수용 |
| **4. 핵심 차별점** | WiredTiger 엔진의 문서 레벨 동시성 제어 및 Snappy 디스크 압축, 최신 Vector Search 내장 |
---

### 핵심 관계

| 구성요소 | 핵심 역할 | 분산 동작 메커니즘 |
|:---|:---|:---|
| **Mongos (Query Router)** | 샤딩 클러스터의 단일 진입 게이트웨이 | 클라이언트의 쿼리를 수신하여 Config Server의 청크 매핑 메타데이터를 캐싱·참조한 후, 해당 데이터가 존재하는 샤드로만 질의를 전송하고 결과를 머지하여 반환 |
| **Config Server** | 클러스터 메타데이터 및 카탈로그 저장소 | 청크 배치 등 샤딩 메타데이터를 저장. 복제셋 기반 구성과 다수결 확인 동작은 버전·구성에 따름 |
| **Shard Nodes** | 실제 파티션 데이터를 영속 저장하는 노드 | 전체 데이터의 분할 서브셋(청크)을 보관. 데이터 유실 방지와 고가용성을 위해 각 샤드 자체를 **독립된 3노드 이상의 Replica Set**으로 구축 |

---

## 2~4교시 예상문제 (25점)

> 대용량 비정형 데이터 처리를 위한 문서 지향(Document-oriented) NoSQL 데이터베이스인 MongoDB의 개념과 핵심 특징을 설명하고, 분산 샤딩(Sharding) 클러스터의 3대 구성요소와 데이터 모델링 기법(Embedding vs Referencing)을 비교하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 유연한 스키마와 수평 확장을 제공하는 MongoDB 개요

#### 한줄 요약: BSON 문서를 컬렉션에 저장하고 문서 구조와 질의·분산 기능을 업무 요구에 맞춰 구성하는 문서 데이터베이스

- **배경**:
  - 애자일 개발 및 마이크로서비스 환경에서 빈번한 스키마 변경 시 RDBMS의 DDL Lock 병목 발생
  - 복잡한 1:N 계층 데이터를 표현하기 위해 수많은 외래키 조인(Join) 연산으로 디스크 I/O 급증 및 성능 저하 직면
- **정의**: BSON 문서를 기본 데이터 단위로 저장하는 문서 데이터베이스. 컬렉션 내 문서 구조는 유연하게 둘 수 있으나 스키마 검증 규칙을 지정할 수도 있음
- **데이터 모델링 매핑 구조**:
  - RDBMS Database $\rightarrow$ MongoDB Database
  - RDBMS Table $\rightarrow$ MongoDB **Collection (컬렉션)**
  - RDBMS Row $\rightarrow$ MongoDB **Document (BSON 문서)**
  - RDBMS Column $\rightarrow$ MongoDB **Field (필드)**

### Ⅱ. MongoDB의 4대 핵심 아키텍처 특성

#### 한줄 요약: BSON 이진 포맷, WiredTiger 스토리지 엔진, 자동 복제셋, 수평 샤딩의 결합

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Box 1 -->
  <rect x="15" y="20" width="115" height="140" rx="6" fill="#3b82f6" fill-opacity="0.1" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="72" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. BSON 포맷</text>
  <text x="72" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">JSON의 이진화</text>
  <text x="72" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">길이 접두사 인덱싱</text>
  <text x="72" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">날짜·바이너리 지원</text>
  <text x="72" y="135" text-anchor="middle" font-size="11" fill="#64748b">초고속 직렬화</text>

  <!-- Box 2 -->
  <rect x="140" y="20" width="115" height="140" rx="6" fill="#0ea5e9" fill-opacity="0.1" stroke="#0ea5e9" stroke-width="1.5"/>
  <text x="197" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">2. WiredTiger</text>
  <text x="197" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">기본 스토리지 엔진</text>
  <text x="197" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">문서 레벨 동시성</text>
  <text x="197" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Snappy 디스크 압축</text>
  <text x="197" y="135" text-anchor="middle" font-size="11" fill="#64748b">체크포인트 영속</text>

  <!-- Box 3 -->
  <rect x="265" y="20" width="115" height="140" rx="6" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="1.5"/>
  <text x="322" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#059669">3. Replica Set</text>
  <text x="322" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">홀수 노드 쿼럼</text>
  <text x="322" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Raft 기반 자동 선출</text>
  <text x="322" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">Oplog 비동기 복제</text>
  <text x="322" y="135" text-anchor="middle" font-size="11" fill="#64748b">2초 내 Failover</text>

  <!-- Box 4 -->
  <rect x="390" y="20" width="115" height="140" rx="6" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="447" y="45" text-anchor="middle" font-size="12" font-weight="bold" fill="#d97706">4. Sharding</text>
  <text x="447" y="75" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">샤드 키 분산</text>
  <text x="447" y="95" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">청크 단위 자동 분할</text>
  <text x="447" y="115" text-anchor="middle" font-size="11" fill="var(--sl-color-text, #334155)">무중단 리밸런싱</text>
  <text x="447" y="135" text-anchor="middle" font-size="11" fill="#64748b">수평 Scale-out</text>
</svg>
</div>

1. **BSON (Binary JSON)**: JSON의 가독성과 텍스트 파싱 오버헤드를 극복하기 위해 길이 접두사(Length Prefix)와 타입 태그를 추가하여 특정 필드로의 O(1) 스킵 검색 및 이진 직렬화 지원
2. **WiredTiger 스토리지 엔진**: 문서 레벨 동시성 제어(Document-level Locking)와 비차단 읽기를 지원하며, Snappy 알고리즘을 통해 디스크 용량을 60~80% 압축
3. **고가용성 복제셋 (Replica Set)**: Primary-Secondary 구조로 동작하며, Heartbeat를 통해 Primary 장애 감지 시 2초 이내에 과반수 투표로 Secondary 중 하나를 새 Primary로 자동 승격
4. **수평적 샤딩 (Sharding)**: 샤드 키에 따라 데이터를 여러 샤드로 분산. 청크 크기·분할·밸런싱 정책은 버전과 설정을 확인

### Ⅲ. 분산 샤딩(Sharding) 클러스터의 3대 핵심 구성요소

#### 한줄 요약: 요청을 라우팅하는 Mongos, 메타데이터를 보관하는 Config Server, 데이터를 담는 Shard 노드

| 구성요소 | 핵심 역할 | 분산 동작 메커니즘 |
|:---|:---|:---|
| **Mongos (Query Router)** | 샤딩 클러스터의 단일 진입 게이트웨이 | 클라이언트의 쿼리를 수신하여 Config Server의 청크 매핑 메타데이터를 캐싱·참조한 후, 해당 데이터가 존재하는 샤드로만 질의를 전송하고 결과를 머지하여 반환 |
| **Config Server** | 클러스터 메타데이터 및 카탈로그 저장소 | 어떤 청크(Chunk)가 어느 샤드 노드에 위치하는지 범위 정보를 저장. 자체 3노드 복제셋으로 엄격한 일관성(CP) 유지 |
| **Shard Nodes** | 실제 파티션 데이터를 영속 저장하는 노드 | 각 샤드가 데이터 일부를 담당하며, 가용성 토폴로지는 배포 요건에 맞춰 복제셋 등으로 구성 |

### Ⅳ. MongoDB 데이터 모델링 전략: Embedding vs Referencing

#### 한줄 요약: 조인을 없애고 단일 I/O로 읽는 중첩(Embedding)과 관계를 분리하여 대용량을 수용하는 참조(Referencing)

<div class="itpe-svg-container" style="margin: 1.5rem 0; overflow-x: auto;">
<svg viewBox="0 0 520 200" width="100%" height="200" xmlns="http://www.w3.org/2000/svg" style="font-family: sans-serif; background: var(--sl-color-bg-inline-code, #f8fafc); border-radius: 8px; border: 1px solid var(--sl-color-gray-5, #e2e8f0);">
  <!-- Embedding Box -->
  <rect x="20" y="20" width="230" height="160" rx="6" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5"/>
  <text x="135" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">1. Embedding (중첩 모델)</text>
  <rect x="35" y="55" width="200" height="85" rx="4" fill="#ffffff" stroke="#93c5fd" stroke-width="1"/>
  <text x="45" y="75" font-size="10" font-family="monospace" fill="#1e293b">{ _id: "user1", name: "홍길동",</text>
  <text x="45" y="93" font-size="10" font-family="monospace" fill="#2563eb">  addresses: [</text>
  <text x="55" y="111" font-size="10" font-family="monospace" fill="#047857">    { city: "서울", zip: "06000" }</text>
  <text x="45" y="129" font-size="10" font-family="monospace" fill="#2563eb">  ] }</text>
  <text x="135" y="162" text-anchor="middle" font-size="10" font-weight="bold" fill="#1d4ed8">단 1회 디스크 I/O 완결 · 원자적 갱신</text>

  <!-- Referencing Box -->
  <rect x="270" y="20" width="230" height="160" rx="6" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
  <text x="385" y="42" text-anchor="middle" font-size="12" font-weight="bold" fill="#b45309">2. Referencing (참조 모델)</text>
  <rect x="285" y="55" width="200" height="85" rx="4" fill="#ffffff" stroke="#fcd34d" stroke-width="1"/>
  <text x="295" y="75" font-size="10" font-family="monospace" fill="#1e293b">User: { _id: "u1", name: "홍길동" }</text>
  <path d="M 385 85 L 385 100" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#arrow118)"/>
  <text x="295" y="115" font-size="10" font-family="monospace" fill="#b45309">Addr: { _id: "a1", userId: "u1",</text>
  <text x="345" y="131" font-size="10" font-family="monospace" fill="#b45309">city: "서울" }</text>
  <text x="385" y="162" text-anchor="middle" font-size="10" font-weight="bold" fill="#b45309">$lookup 조인 수행 · 16MB 제한 극복</text>
</svg>
</div>

| 비교 항목 | 중첩 모델 (Embedding) | 참조 모델 (Referencing) |
|:---|:---|:---|
| **관계 표현** | 단일 BSON 문서 내부에 배열이나 서브 도큐먼트로 포함 | 문서 간에 `_id`를 외래키(FK)처럼 저장하고 분리 컬렉션 관리 |
| **I/O 성능** | **단 1회의 디스크 읽기로 모든 연관 데이터 조회 (초고속)** | 연관 데이터 조회 시 `$lookup` 파이프라인 또는 추가 쿼리 필요 |
| **원자성 (ACID)** | **단일 문서 내 모든 수정은 락 없이 완벽한 원자성 보장** | 다중 문서 트랜잭션 필요 (성능 오버헤드 수반) |
| **문서 크기 제한** | 16MB 한도 초과 위험 존재 (무한 증가 배열 주의) | 16MB 제한으로부터 완전히 자유로움 |
| **적합한 관계** | 1:1 관계, 유한하고 적은 수의 1:N 관계 (댓글 100개 미만) | 1:N에서 N이 수천 건 이상 폭증하거나 N:M 다대다 관계 |

### Ⅴ. RDBMS vs MongoDB vs Redis 3대 데이터베이스 비교

#### 한줄 요약: 엄격한 정규화의 RDBMS, 유연한 문서 저장의 MongoDB, 초고속 인메모리 캐시의 Redis

| 비교 항목 | RDBMS (PostgreSQL) | MongoDB | Redis |
|:---|:---|:---|:---|
| **데이터 모델** | 2차원 관계형 테이블 (행/열) | **문서 지향 (BSON Document)** | 인메모리 키-값 (Key-Value) 및 자료구조 |
| **스키마 특성** | 엄격한 정적 스키마 (Schema-on-Write) | **동적 스키마 (Schema-less)** | 스키마 없음 |
| **트랜잭션 (ACID)** | 전사 다중 테이블 완전 지원 (기본) | 단일 문서 기본, 다중 문서 트랜잭션 지원 | MULTI/EXEC 기반 단위 트랜잭션 |
| **확장 방식** | 수직 확장(Scale-up), 읽기 복제본 | **수평 샤딩(Scale-out) 기본 내장** | 레디스 클러스터 샤딩 |
| **주요 사용 사례** | 금융, 결제, ERP 코어 원장 데이터 | 콘텐츠 관리, 상품 카탈로그, IoT 로그, 모바일 백엔드 | 세션 저장소, 캐싱 계층, 실시간 랭킹보드 |

### Ⅵ. 실무 운영 이슈 및 트러블슈팅

#### 한줄 요약: 샤드 키 단조 증가로 인한 Hotspot, 점보 청크(Jumbo Chunk), 16MB 문서 초과 에러 방지

| 장애 요인 | 발생 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **샤드 핫스팟 (Hotspot)** | `_id`(ObjectId)나 생성일자처럼 단조 증가하는 키를 샤드 키로 설정하여 특정 샤드 1개에만 쓰기 폭증 | 카디널리티가 높은 복합 샤드 키 선정 또는 해시 샤드 키(**Hashed Shard Key**) 적용 |
| **점보 청크 (Jumbo Chunk)** | 샤드 키 값이 동일한 데이터가 64MB 청크 제한을 초과하여 밸런서 분할(Split) 불가 상태 발생 | 세부 식별자를 추가하여 샤드 키를 복합 키(`{ country: 1, userId: 1 }`)로 재설계 및 수동 분할 |
| **16MB 문서 초과 에러** | 사용자의 활동 로그나 대댓글 목록을 단일 문서 내 무한 배열로 누적 | 버킷 패턴(Bucket Pattern)을 적용하여 100건 단위로 문서를 분할 저장하거나 GridFS 활용 |

### Ⅶ. 기술사적 제언

### 실전 답안용 기술사적 제언

- **판정**: 대규모 트래픽 환경에서 잦은 스키마 변경과 수평 확장이 필요한 서비스는 RDBMS만으로 감당할 수 없으므로 MongoDB 기반의 분산 아키텍처 도입이 타당함.
- **대응**:
  1. **샤드 키 최적화**: 단조 증가 키 대신 해시 샤드 키(Hashed Key) 또는 비즈니스 복합 키를 적용하여 쓰기 핫스팟 원천 차단.
  2. **하이브리드 모델링**: 1회 조회 빈도가 높은 핵심 데이터는 Embedding, 무한 증가 이력 데이터는 Bucket Pattern Referencing으로 이원화.
  3. **멀티모달 AI 확장**: Atlas Vector Search를 결합하여 RAG 시스템의 벡터 인덱싱과 메타데이터 필터링을 단일 저장소로 일원화.
- **검증**: 클러스터 내 청크 밸런싱 균등도 모니터링 및 복제 지연(Replication Lag) 1초 미만 유지 검증.
- **효과**: 페타바이트급 데이터 수평 확장성 확보 및 무중단 고가용성(HA) 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">1. 현행 한계</div>
    <div class="itpe-flow-desc">RDBMS의 DDL Lock 병목, 조인 연산 급증, 수평 확장 불가</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">2. 개선 방안</div>
    <div class="itpe-flow-desc">MongoDB BSON 모델링 및 분산 샤딩·Replica Set 구축</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">3. 검증 기준</div>
    <div class="itpe-flow-desc">해시 샤드 키 균등 분산, 16MB 문서 제한 준수, 2초 내 Failover</div>
  </div>
  <div class="itpe-flow-arrow">&#x2192;</div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-title">4. 실행 효과</div>
    <div class="itpe-flow-desc">페타바이트급 수평 Scale-out 및 Vector Search 통합 AI 백엔드 완성</div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제127회 정보관리 2교시: 문서 지향 NoSQL인 MongoDB의 특징과 아키텍처 및 데이터 모델링 기법
- **검증 출처**:
  - Shannon Bradshaw et al., "MongoDB: The Definitive Guide (3rd Edition)", O'Reilly
  - MongoDB Manual, "Sharding Architecture and Data Modeling Concepts"
---

## 연결 토픽

- 상위 토픽: [03-001 NoSQL](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/001_nosql.md)
- 연관 토픽: [03-045 샤딩(Sharding)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/045_sharding.md), [03-113 CAP·PACELC 이론](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/113_cap_pacelc.md)
