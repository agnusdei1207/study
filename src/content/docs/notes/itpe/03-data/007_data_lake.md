---
title: "데이터 레이크(데이터 늪 포함)"
category: "03-data"
tags:
  - "데이터레이크"
  - "DataLake"
  - "데이터늪"
  - "DataSwamp"
  - "SchemaOnRead"
  - "메달리온"
  - "Lakehouse"
date: "2026-09-20T23:50:43+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 플랫폼에서 대규모 분석 저장소 및 데이터 레이크로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 저장·플랫폼</span>
  <strong>데이터 레이크(데이터 늪 포함)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 다양한 원천의 정형·반정형·비정형 데이터를 가공 없이 원형(Raw) 그대로 대규모 객체 스토리지에 유연하게 적재하고, 분석 시점에 스키마를 정의(Schema-on-Read)하는 분산 빅데이터 저장·분석 플랫폼
- 메커니즘: 멀티소스 수집 $\rightarrow$ Bronze(Raw 원본 보존) $\rightarrow$ Silver(정제·표준화) $\rightarrow$ Gold(비즈니스 가공) 메달리온 정제 $\rightarrow$ 카탈로그·계보 통제 $\rightarrow$ 레이크하우스 서빙
- 산출물: 메달리온 계층 데이터셋(Parquet/Iceberg) · 메타데이터 카탈로그 · OpenLineage 계보 지도 · 스토리지 수명주기(TTL) 규칙서

<div class="itpe-flow-map" role="img" aria-label="데이터 레이크 메달리온 파이프라인 및 데이터 늪 방지 판정 체계">
  <div class="itpe-flow-node">
    <strong>1단계: 대규모 이종 원천 데이터 수집 (Bronze)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>보존</strong><span>RDBMS, 웹로그, IoT 센서, 이미지 데이터를 원형 그대로 불변 적재 (Schema-on-Read)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 결측치 정제 및 표준화 변환 (Silver)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>정제</strong><span>오류 정제, 중복 제거, 컬럼 표준화 및 Parquet/ORC 압축 컬럼 포맷 변환</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 비즈니스 도메인 집계 및 제품화 (Gold)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>모델링</strong><span>도메인별 스타 스키마 구축, 차원 모델링 및 Data Product 패키징</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 메타데이터 및 거버넌스 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>카탈로그에 메타데이터가 등록되고 Data Owner가 지정되어 '데이터 늪' 위험이 없는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (공식 서비스 승격)</strong>
      <span>전사 Data Catalog 등록 $\rightarrow$ AI/ML 피처 스토어 및 셀프서비스 BI 대시보드 쿼리 오픈</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (데이터 늪 / 다크 데이터)</strong>
      <span>승격 차단 및 격리 $\rightarrow$ 자동 크롤러 메타데이터 태깅 및 스토리지 수명주기(TTL) 강제 적용</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Schema-on-Read`: 데이터를 저장할 때는 스키마를 강제하지 않고 원본 그대로 적재한 뒤, 데이터를 읽어 쿼리하는 시점에 스키마를 동적으로 부여하는 방식
- `Medallion Architecture`: 데이터 레이크 내부를 Bronze(원시 데이터) $\rightarrow$ Silver(정제 데이터) $\rightarrow$ Gold(비즈니스 가공 데이터)로 계층화하여 데이터 품질을 단계적으로 승격시키는 파이프라인
- `Data Swamp(데이터 늪)`: 메타데이터 관리 부재, 계보 추적 불가, 소유자 부재로 인해 데이터의 가치를 잃어버리고 방치된 쓰레기통 상태의 데이터 레이크
- `Data Lineage`: 데이터가 생성된 원천부터 수집, 가공, 변환되어 최종 분석 리포트에 도달하기까지의 전 과정을 시각적으로 추적하는 계보
- `Data Lakehouse`: 데이터 레이크의 저비용 확장성과 데이터 웨어하우스의 ACID 트랜잭션 및 고성능 SQL 엔진을 융합한 차세대 아키텍처

</details>

## 예상문제

> 대용량 이기종 데이터 수용을 위한 데이터 레이크(Data Lake)의 개념, 메달리온 아키텍처(Bronze/Silver/Gold) 및 Schema-on-Read 메커니즘을 설명하고, 메타데이터 부재로 인한 '데이터 늪(Data Swamp)' 발생 원인과 거버넌스 기반 방지 대책을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **메달리온 아키텍처** | Bronze(Raw), Silver(Cleansed), Gold(Curated), Parquet, Iceberg | Ⅲ 아키텍처 |
| **데이터 늪(Data Swamp)** | 다크 데이터, 메타데이터 카탈로그 부재, Data Ownership 결여 | Ⅴ·Ⅵ |
| **데이터 레이크하우스** | 스토리지/컴퓨팅 분리, ACID 트랜잭션, 타임 트래블(Time Travel) | Ⅳ·Ⅶ |

## Ⅰ. 대규모 이종 데이터 수용소, 데이터 레이크(Data Lake)의 개요

> 데이터 레이크는 정형·비정형 원시 데이터를 원형 그대로 보존하고 분석 시 구조를 정의하는 유연한 저장 플랫폼임.

- 정의: 정형 RDBMS 데이터뿐 아니라 로그, JSON, 오디오, 비디오 등 반정형·비정형 데이터를 확장 가능한 객체 스토리지(S3, HDFS 등)에 원본 그대로 저장하는 중앙 집중식 저장소
- 등장 배경: 전통적 DW의 사전 스키마 정의(Schema-on-Write) 방식은 고비용 ETL과 비정형 데이터 수용 불가로 인해 AI/ML 및 빅데이터 분석 요구 지원에 한계 노출
- 핵심 가치: 원본 데이터 영구 보존을 통한 재생산성 확보, 컴퓨팅과 스토리지의 독립적 분리(Decoupling), 다양한 분석 엔진(Spark, Presto, Flink)의 공통 스토리지 공유

## Ⅱ. Schema-on-Write(DW) vs Schema-on-Read(Data Lake) 비교

> 데이터에 스키마 구조를 부여하는 시점의 차이가 분석 민첩성과 데이터 유연성을 결정함.

<svg viewBox="0 0 520 185" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="Schema-on-Write와 Schema-on-Read의 처리 흐름 비교" role="img">
  <defs>
    <marker id="arrow-write" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f0883e"/>
    </marker>
    <marker id="arrow-read" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <!-- Schema on Write -->
  <g transform="translate(10, 15)">
    <rect width="500" height="70" rx="6" fill="rgba(240,136,62,0.06)" stroke="#f0883e" stroke-width="1"/>
    <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#f0883e">Schema-on-Write (전통적 DW)</text>
    <rect x="15" y="30" width="80" height="28" rx="4" fill="#21262d" stroke="#30363d"/>
    <text x="55" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">정형 원천</text>
    <path d="M 95 44 L 140 44" stroke="#f0883e" stroke-width="1.5" marker-end="url(#arrow-write)"/>
    <text x="117" y="38" font-family="system-ui, sans-serif" font-size="9" fill="#f0883e" text-anchor="middle">고비용 ETL</text>
    <rect x="145" y="30" width="105" height="28" rx="4" fill="#21262d" stroke="#f0883e"/>
    <text x="197" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#f0883e" text-anchor="middle">고정 스키마 DB</text>
    <path d="M 250 44 L 320 44" stroke="#8b949e" stroke-width="1.5" marker-end="url(#arrow-write)"/>
    <rect x="325" y="30" width="160" height="28" rx="4" fill="#21262d" stroke="#30363d"/>
    <text x="405" y="48" font-family="system-ui, sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">정형 SQL / 리포팅</text>
  </g>
  <!-- Schema on Read -->
  <g transform="translate(10, 95)">
    <rect width="500" height="75" rx="6" fill="rgba(88,166,255,0.06)" stroke="#58a6ff" stroke-width="1"/>
    <text x="15" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#58a6ff">Schema-on-Read (데이터 레이크)</text>
    <rect x="15" y="32" width="95" height="28" rx="4" fill="#21262d" stroke="#30363d"/>
    <text x="62" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">정형/반정형/비정형</text>
    <path d="M 110 46 L 155 46" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#arrow-read)"/>
    <text x="132" y="40" font-family="system-ui, sans-serif" font-size="9" fill="#58a6ff" text-anchor="middle">저비용 적재</text>
    <rect x="160" y="32" width="115" height="28" rx="4" fill="#21262d" stroke="#58a6ff"/>
    <text x="217" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#58a6ff" text-anchor="middle">객체 스토리지(Raw)</text>
    <path d="M 275 46 L 335 46" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#arrow-read)"/>
    <text x="305" y="40" font-family="system-ui, sans-serif" font-size="9" fill="#58a6ff" text-anchor="middle">읽기 시 스키마</text>
    <rect x="340" y="32" width="145" height="28" rx="4" fill="#21262d" stroke="#30363d"/>
    <text x="412" y="50" font-family="system-ui, sans-serif" font-size="10" fill="#c9d1d9" text-anchor="middle">AI/ML · EDA · Ad-hoc</text>
  </g>
</svg>

| 비교 항목 | Schema-on-Write (전통 DW) | Schema-on-Read (데이터 레이크) |
|---|---|---|
| **스키마 적용 시점** | 데이터베이스 적재(Write) 시점에 스키마 강제 | 데이터를 조회 및 분석(Read)하는 시점에 스키마 정의 |
| **수집 데이터 형태** | 사전에 정제된 정형(Structured) 데이터 위주 | 정형, 반정형(JSON, XML), 비정형(이미지, 로그) 모두 수용 |
| **초기 적재 비용** | 고비용의 사전 모델링 및 무거운 ETL 파이프라인 필수 | 저비용의 신속한 원천 데이터 ELT/직접 적재 |
| **데이터 정합성** | 매우 높음 (DBMS의 엄격한 무결성 제약조건 보장) | 원본 상태로 보존되어 데이터 품질 편차 존재 |
| **활용 유연성** | 정해진 비즈니스 리포트 및 BI 분석에 한정 | 머신러닝/딥러닝, 데이터 과학, 탐색적 데이터 분석(EDA) 최적 |

## Ⅲ. 메달리온(Medallion) 정제 구조 예시

> Bronze·Silver·Gold는 원시→정제→활용 데이터를 나누는 통용 설계 패턴이며, 제품·조직의 품질 기준에 맞게 계층을 조정함.

<svg viewBox="0 0 520 180" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="메달리온 아키텍처 정제 파이프라인" role="img">
  <defs>
    <marker id="arrow-gold" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#d29922"/>
    </marker>
  </defs>
  <!-- Bronze -->
  <g transform="translate(15, 20)">
    <rect width="140" height="95" rx="6" fill="#21262d" stroke="#cd7f32" stroke-width="1.5"/>
    <rect x="0" y="0" width="140" height="24" rx="6" fill="rgba(205,127,50,0.2)"/>
    <text x="70" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#f0883e" text-anchor="middle">Bronze (Raw Zone)</text>
    <text x="12" y="44" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9">• 원천 원본 불변 보존</text>
    <text x="12" y="62" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9">• Append-only 수집</text>
    <text x="12" y="80" font-family="system-ui, sans-serif" font-size="9" fill="#8b949e">• 재처리(Replay) 보장</text>
  </g>
  <!-- Arrow 1 -->
  <path d="M 158 68 L 187 68" stroke="#cd7f32" stroke-width="2" marker-end="url(#arrow-gold)"/>
  <text x="172" y="60" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e" text-anchor="middle">정제</text>

  <!-- Silver -->
  <g transform="translate(190, 20)">
    <rect width="140" height="95" rx="6" fill="#21262d" stroke="#8b949e" stroke-width="1.5"/>
    <rect x="0" y="0" width="140" height="24" rx="6" fill="rgba(139,148,158,0.2)"/>
    <text x="70" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#c9d1d9" text-anchor="middle">Silver (Refined Zone)</text>
    <text x="12" y="44" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9">• 결측/중복 제거 정제</text>
    <text x="12" y="62" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9">• Parquet/ORC 압축</text>
    <text x="12" y="80" font-family="system-ui, sans-serif" font-size="9" fill="#8b949e">• 전사 공통 참조 뷰</text>
  </g>
  <!-- Arrow 2 -->
  <path d="M 333 68 L 362 68" stroke="#d29922" stroke-width="2" marker-end="url(#arrow-gold)"/>
  <text x="347" y="60" font-family="system-ui, sans-serif" font-size="8" fill="#d29922" text-anchor="middle">집계</text>

  <!-- Gold -->
  <g transform="translate(365, 20)">
    <rect width="140" height="95" rx="6" fill="#21262d" stroke="#d29922" stroke-width="1.5"/>
    <rect x="0" y="0" width="140" height="24" rx="6" fill="rgba(210,153,34,0.2)"/>
    <text x="70" y="16" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#e3b341" text-anchor="middle">Gold (Curated Zone)</text>
    <text x="12" y="44" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9">• 비즈니스 스타 스키마</text>
    <text x="12" y="62" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9">• Data Product 패키징</text>
    <text x="12" y="80" font-family="system-ui, sans-serif" font-size="9" fill="#8b949e">• BI / ML 서빙 피처</text>
  </g>

  <!-- Governance Base Bar -->
  <g transform="translate(15, 128)">
    <rect width="490" height="38" rx="4" fill="rgba(56,189,248,0.08)" stroke="rgba(56,189,248,0.3)"/>
    <text x="245" y="22" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#58a6ff" text-anchor="middle">공통 거버넌스 레이어: 메타데이터 카탈로그 (Glue/Atlas) · 데이터 계보 (Lineage) · 보안/권한 통제</text>
  </g>
</svg>

1. **Bronze 계층 (Raw Zone)**:
   - 원천 시스템에서 수집된 변경되지 않은 원시 데이터를 시간순으로 누적 보존 (Append-only)
   - 스키마 변경 시에도 원본이 유지되므로 언제든지 하류 데이터를 재처리(Reprocessing) 가능
2. **Silver 계층 (Refined Zone)**:
   - 결측치 처리, 데이터 유형 표준화, 암호화 처리 및 컬럼 지향 포맷(Parquet, ORC)으로 변환
   - 부서 간 공통으로 참조할 수 있는 엔터프라이즈 통합 데이터 뷰 제공
3. **Gold 계층 (Curated / Aggregated Zone)**:
   - 특정 비즈니스 도메인(재무, 마케팅)에 최적화된 집계 테이블 및 피처 스토어(Feature Store) 구축
   - 셀프서비스 BI 보고서 및 최종 머신러닝 추론 서빙

## Ⅳ. 데이터 웨어하우스 vs 데이터 레이크 vs 데이터 레이크하우스

> 세 저장소 아키텍처의 핵심 특성을 대비함.

| 비교 기준 | 데이터 웨어하우스 (DW) | 데이터 레이크 (Data Lake) | 데이터 레이크하우스 (Lakehouse) |
|---|---|---|---|
| **저장 데이터** | 정형 데이터 위주 | 모든 형태 (정형, 반정형, 비정형) | 모든 형태 (정형, 비정형 통합) |
| **스토리지 비용** | 고비용 (고성능 전용 스토리지) | 초저비용 (클라우드 객체 스토리지) | 초저비용 (오픈 테이블 포맷 기반 객체 스토리지) |
| **ACID 트랜잭션** | 완벽 지원 | 미지원 (단순 파일 저장소) | 완벽 지원 (Delta Lake, Apache Iceberg) |
| **스토리지/연산** | 밀결합 (Scale-Up 위주) | 완전 분리 (독립적 Scale-Out) | 완전 분리 (다양한 쿼리 엔진 연계) |
| **최적 활용 영역** | 전통 기업 경영 분석, BI 대시보드 | 빅데이터 수집, 데이터 과학, AI 연구 | BI 대시보드 + AI/ML 통합 플랫폼 |

## Ⅴ. 데이터 늪(Data Swamp) 발생 원인 및 위험성

> 거버넌스가 결여된 데이터 레이크는 거대한 데이터 쓰레기장으로 전락함.

<svg viewBox="0 0 520 140" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="데이터 늪 발생 악순환 메커니즘" role="img">
  <defs>
    <marker id="arrow-swamp" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#f85149"/>
    </marker>
  </defs>
  <!-- Step 1 -->
  <g transform="translate(15, 20)">
    <rect width="105" height="55" rx="5" fill="#21262d" stroke="#30363d"/>
    <text x="52" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#c9d1d9" text-anchor="middle">무차별 적재</text>
    <text x="52" y="42" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e" text-anchor="middle">검증 없는 Dump</text>
  </g>
  <path d="M 122 47 L 142 47" stroke="#f85149" stroke-width="1.5" marker-end="url(#arrow-swamp)"/>

  <!-- Step 2 -->
  <g transform="translate(145, 20)">
    <rect width="105" height="55" rx="5" fill="#21262d" stroke="#f85149" stroke-width="1"/>
    <text x="52" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#f85149" text-anchor="middle">메타데이터 누락</text>
    <text x="52" y="42" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e" text-anchor="middle">소유자·스키마 부재</text>
  </g>
  <path d="M 252 47 L 272 47" stroke="#f85149" stroke-width="1.5" marker-end="url(#arrow-swamp)"/>

  <!-- Step 3 -->
  <g transform="translate(275, 20)">
    <rect width="105" height="55" rx="5" fill="#21262d" stroke="#f85149" stroke-width="1"/>
    <text x="52" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#f85149" text-anchor="middle">내용 파악 불가</text>
    <text x="52" y="42" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e" text-anchor="middle">다크 데이터화</text>
  </g>
  <path d="M 382 47 L 402 47" stroke="#f85149" stroke-width="1.5" marker-end="url(#arrow-swamp)"/>

  <!-- Step 4 -->
  <g transform="translate(405, 20)">
    <rect width="100" height="55" rx="5" fill="rgba(248,81,73,0.15)" stroke="#f85149" stroke-width="1.5"/>
    <text x="50" y="24" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#ff7b72" text-anchor="middle">데이터 늪 전락</text>
    <text x="50" y="42" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9" text-anchor="middle">비용↑ 신뢰도 0</text>
  </g>

  <!-- Bottom Result Bar -->
  <g transform="translate(15, 90)">
    <rect width="490" height="34" rx="4" fill="#161b22" stroke="#30363d"/>
    <text x="245" y="21" font-family="system-ui, sans-serif" font-size="9.5" fill="#ff7b72" text-anchor="middle">치명적 리스크: 클라우드 스토리지 비용 폭증 · 컴플라이언스(개인정보) 위반 · 분석 신뢰 붕괴</text>
  </g>
</svg>

- **메타데이터 부재**: 파일의 생성자, 비즈니스 의미, 스키마 이력이 카탈로그에 기록되지 않아 검색 불가
- **Data Ownership 부재**: 데이터 적재 후 품질 모니터링과 수명주기 폐기를 책임지는 도메인 오너 부재
- **다크 데이터(Dark Data) 누적**: 분석 가치가 없거나 중복된 임시 파일이 삭제되지 않고 방치되어 스토리지 비용 폭증
- **보안 및 규제 위반**: 개인정보(PII) 포함 여부와 접근 통제(RBAC)가 적용되지 않아 법적 과징금 리스크 노출

## Ⅵ. 데이터 레이크 문제점·대응책

> 카탈로그·계보·수명주기·데이터 계약을 결합하여 검색 불가·품질 저하·다크 데이터 위험을 줄임.

| 통제 영역 | 구체적 실행 대책 | 실무적 통제 효과 |
|---|---|---|
| **메타데이터 카탈로그** | AWS Glue, Apache Atlas 연계 자동 크롤링 및 비즈니스 태깅 | 전사 검색 가능한 데이터 자산 사전 구축 |
| **데이터 계보 (Lineage)** | OpenLineage 및 dbt 기반 데이터 흐름 추적 파이프라인 구성 | 원천 변경에 따른 영향도 분석 및 감사 추적 |
| **수명주기 정책 (FinOps)** | 객체 스토리지 Lifecycle(Hot $\to$ Cold $\to$ Glacier $\to$ 삭제) 수립 | 다크 데이터 자동 소멸 및 클라우드 비용 절감 |
| **데이터 계약 (Data Contract)** | 상류·하류 간 스키마·품질 기준 합의 | 호환되지 않는 변경·저품질 유입 감소 |

## Ⅶ. 기술사적 제언: 레이크하우스로의 진화와 개방형 테이블 포맷

> "데이터 레이크의 가치는 단순히 쌓아둔 테라바이트가 아니라, 신뢰할 수 있는 거버넌스 하에서 즉시 쿼리할 수 있는 가용성에 있다."

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 수집량이 아니라 발견 가능성·신뢰성·소유권이 레이크의 가치를 결정한다. 소비 목적 없는 원본 축적은 필연적으로 데이터 늪(Data Swamp)을 양산한다.
>
> **[나라면 이렇게 쓴다]**
> 수집 단계부터 Data Contract와 도메인 Owner를 강제 바인딩하고, Silver 승격 파이프라인에 스키마 적합성·품질 검증·PII 비식별화 Gate를 통과시켜 무결한 Data Product로 서빙하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 카탈로그 검색 가능성, OpenLineage 계보 추적성, 품질 SLA 준수 여부가 100% 입증된 데이터셋만 상위 계층(Silver/Gold)으로 승격
- **대응 방안**: Apache Iceberg / Delta Lake 기반 오픈 테이블 포맷 도입 $\rightarrow$ 객체 스토리지 상의 ACID 트랜잭션, 스키마 진화 및 타임 트래블(Time Travel) 구현
- **검증 체계**: 메타데이터 카탈로그 등록률 100%, 90일 이상 미사용 다크 데이터 비율 10% 미만 통제
- **기대 효과**: 데이터 늪 전락을 원천 차단하고, BI 분석가와 AI/ML 엔지니어가 단일 스토리지를 신뢰성 있게 공유하는 통합 레이크하우스 완성

<div class="itpe-flow-map" role="img" aria-label="데이터 레이크 품질 고도화 실행 로드맵">
  <div class="itpe-flow-node">
    <strong>1단계: 현행 한계 인식</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-fail"><strong>문제</strong><span>거버넌스 없는 무차별 적재로 인한 데이터 늪화 및 다크 데이터 스토리지 비용 폭증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 아키텍처 개선 방안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>기술 적용</strong><span>Bronze-Silver-Gold 메달리온 파이프라인 + Apache Iceberg 테이블 포맷 + FinOps TTL 정책</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 정량 검증 기준</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>KPI 지표</strong><span>메타데이터 카탈로그 등록률 100%, 비활성 다크 데이터 10% 미만 유지</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 궁극적 실행 효과</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>가치 창출</strong><span>객체 스토리지 상 ACID 트랜잭션 보장 및 스토리지 TCO 40% 이상 절감 달성</span></div>
    </div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 데이터 레이크(Data Lake) 및 데이터 늪(Data Swamp)의 개념

- **데이터 레이크**: 대규모 이종(정형·반정형·비정형) 데이터를 가공 없이 원형(Raw) 그대로 객체 스토리지에 적재하고, 분석 시점에 스키마를 부여(Schema-on-Read)하는 빅데이터 저장 플랫폼
- **데이터 늪**: 메타데이터 카탈로그 및 소유권 거버넌스 부재로 데이터 출처·내용 파악이 불가능하여 가치를 상실한 쓰레기장 상태의 레이크

### 2. 메달리온 정제 아키텍처 및 늪 방지 4대 대책

| 계층/영역 | 핵심 메커니즘 | 실무 통제 방안 |
|---|---|---|
| **Bronze 계층** | Raw Zone (원시 데이터 보존) | 원천 변경 대비 Append-only 불변 적재 |
| **Silver 계층** | Refined Zone (정제·표준화) | 결측치 정제 및 Parquet/ORC 압축 컬럼화 |
| **Gold 계층** | Curated Zone (비즈니스 서빙) | 도메인별 스타 스키마 구축 및 Data Product화 |
| **늪 방지 거버넌스** | 카탈로그·계보·계약·수명주기 | Glue/Atlas 메타 등록, OpenLineage 추적, FinOps TTL 자동 삭제 |

### 3. 기술사적 제언: 레이크하우스(Lakehouse)로의 진화

- Apache Iceberg / Delta Lake 오픈 테이블 포맷을 도입하여 저비용 객체 스토리지 위에서 완벽한 ACID 트랜잭션과 고성능 SQL 엔진을 연계함으로써 데이터 늪 방지와 분석 민첩성을 동시 확보해야 함.

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제137·139회 확인 · 제119회는 KPC 보조자료이며 공식 원문 미확보
- **표준 및 레퍼런스**: [AWS Data Lake Architecture Guide](https://aws.amazon.com/what-is/data-lake/), Databricks Medallion Architecture Whitepaper, Apache Iceberg Documentation

## 학습 체크

- [ ] [Ⅰ 개요]: Schema-on-Read 관점의 데이터 레이크 정의와 등장 배경을 기술하였는가?
- [ ] [Ⅱ 비교]: Schema-on-Write(DW)와 Schema-on-Read(Lake)의 차이를 비교하였는가?
- [ ] [Ⅲ 아키텍처]: Bronze, Silver, Gold 메달리온 3계층의 정제 파이프라인을 제시하였는가?
- [ ] [Ⅴ·Ⅵ 통제]: 데이터 늪의 4대 원인과 메타데이터/Lineage/TTL 기반 방지 대책을 기술하였는가?

## 연결 토픽

- [데이터 거버넌스](./006_data_governance.md) · [로지컬 데이터웨어하우스(LDW)](./132_logical_data_warehouse.md) · [빅데이터 플랫폼 아키텍처](./135_big_data_platform_architecture.md) · [데이터 표준화](./008_data_standardization.md)
