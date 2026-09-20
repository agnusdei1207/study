---
sidebar:
  order: 7
  label: "007. 데이터 레이크"
  badge:
    text: "A"
    variant: note
title: "데이터 레이크 (Data Lake)"
author: "OpenAI Codex"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-data"
weight: 7
extra:
  model: "GPT-5"
  keyword_grade: "A"
  question_no: "007"

---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 플랫폼</span><span>분석 저장소</span><strong>데이터 레이크</strong></div>

## 큰 그림과 30초 인출

```text
[DB·파일·로그·IoT·미디어]
          │ Batch·Stream·CDC
          ▼
[Landing] → [Raw] → [Cleansed] → [Curated/Serving] → BI·SQL·AI
 원본수신    불변원본    품질·표준화      업무제품
          └──────── Governance Plane ─────────────┘
             Catalog·Lineage·Quality·Security·Cost
```

- 본질: **다양한 원천 데이터를 원형에 가깝게 대규모 저장하고 여러 분석 목적에 따라 읽기·가공하는 공유 데이터 기반**
- 암기: `랜-로-클-서` = Landing → Raw → Cleansed → Serving
- 위험: 메타데이터·품질·소유자·접근통제가 없으면 데이터 늪(Data Swamp)으로 전락

## 예상문제

> 데이터 레이크의 개념과 참조 아키텍처, 데이터 처리절차를 설명하고 DW·데이터 레이크·레이크하우스를 비교하여 데이터 늪 방지방안을 논하시오. (25점)

## Ⅰ. 다양한 원천을 보존하는 분석 데이터 기반, 데이터 레이크 개요

- 정의: 데이터 레이크는 정형·반정형·비정형 데이터를 대규모 분산 저장소에 원형 또는 저가공 형태로 보존하고 목적별 처리·분석을 지원하는 플랫폼
- 목적: 원본 재처리, 탐색적 분석, AI 학습, 대규모 배치·스트림 처리를 위한 공통 기반 확보
- 필요성: 사전 모델링된 정형 데이터만 수용하는 DW만으로는 로그·문서·센서·미디어와 새로운 분석요구에 민첩하게 대응하기 어려움

## Ⅱ. 유연성과 재사용성을 제공하는 데이터 레이크 특징

| 특징 | 핵심 내용 | 통제할 위험 |
|---|---|---|
| 다양한 형식 | 정형·반정형·비정형 수용 | 포맷·스키마 난립 |
| 원본 보존 | 재처리·감사·새로운 Feature 생성 | 개인정보·보존비용 |
| Schema-on-Read | 소비 시점에 목적별 구조 적용 | 의미 불일치·품질 지연 |
| 저장-연산 분리 | 독립 확장·다중 엔진 공유 | 작은 파일·메타데이터 병목 |
| Batch+Stream | 과거·실시간 데이터 통합 | 중복·순서·정합성 문제 |

#### 한줄 요약

- 저장 유연성을 얻는 대신 발견·품질·보안·비용 통제 책임이 플랫폼 운영에 집중됨

## Ⅲ. Zone과 거버넌스 평면의 참조 아키텍처

| 계층 | 역할 | 핵심 통제 |
|---|---|---|
| Source/Ingestion | DB·API·파일·이벤트 수집 | 재시도·중복제거·스키마 변경 |
| Landing | 수신 데이터 임시 격리 | 악성파일·형식·반입 검증 |
| Raw | 불변 원본과 이력 보존 | 암호화·보존·개인정보 분리 |
| Cleansed | 정제·표준화·품질 검증 | 규칙·계보·재처리 가능성 |
| Curated/Serving | 업무별 데이터 제품 제공 | SLO·접근권한·의미계층 |
| Governance Plane | 전 계층의 메타·품질·보안·비용 | Catalog·Lineage·Policy·FinOps |

```text
Control Plane: Catalog / IAM·Policy / Lineage / DQ / Orchestration / Cost
Data Plane:    Object Storage / Table Format / Query·Processing Engines
```

## Ⅳ. 수집부터 서비스까지의 처리절차

```text
① 원천·계약 등록 → ② Batch/Stream/CDC 수집 → ③ 원본 불변 적재
 → ④ Catalog·스키마·계보 등록 → ⑤ 정제·품질·비식별
 → ⑥ 업무 데이터 제품 발행 → ⑦ 사용·비용·품질 모니터링
```

| 단계 | 판정 질문 | 증적 |
|---|---|---|
| 반입 | 누가 어떤 근거·SLA로 제공하는가 | Data Contract·Owner |
| 저장 | 원본·변경·삭제를 재현할 수 있는가 | 버전·보존정책·계보 |
| 가공 | 규칙과 입력·출력이 추적되는가 | Pipeline·DQ 결과 |
| 제공 | 의미·품질·권한·사용예가 명확한가 | Catalog·SLO·접근기록 |
| 운영 | 비용·사용·품질 저하를 감시하는가 | 대시보드·경보·폐기기록 |

## Ⅴ. DW·데이터 레이크·레이크하우스 비교

| 구분 | DW | 데이터 레이크 | 레이크하우스 |
|---|---|---|---|
| 주 데이터 | 정형·정제 | 모든 형식·원본 중심 | 레이크 저장+관리형 테이블 |
| 스키마 | Schema-on-Write | Schema-on-Read 중심 | Write/Read 혼합·Schema Evolution |
| 주 용도 | 정형 BI·보고 | 탐색·대규모 처리·AI | BI와 AI 통합 |
| 강점 | 일관된 성능·의미 | 유연성·원본 재사용 | ACID·버전·다중엔진 상호운용 |
| 위험 | 신규 요구 반영 비용 | 데이터 늪·거버넌스 | 운영 복잡성·엔진 호환성 |
| 선택 | 안정된 정형 지표 | 다양한 원천·탐색 | 공용 오브젝트 저장에서 신뢰 테이블 필요 |

## Ⅵ. 데이터 늪을 막는 실무 고려사항

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 데이터를 찾거나 믿지 못함 | Catalog·Owner·품질·계보 부재 | 반입 시 메타데이터 계약, 자동 계보·DQ·소유자 등록 | 발견·신뢰성 확보 |
| 작은 파일로 성능 저하 | 과도한 스트림 파티션·미병합 | Compaction, 파티션·파일크기 기준, 사용 패턴 튜닝 | 메타·I/O 부하 감소 |
| 개인정보 무기한 축적 | 원본 보존과 최소보유 원칙 충돌 | 분류·마스킹·보존·삭제·법적보존 정책 자동화 | 권리·규제 위험 감소 |
| 중복 데이터·비용 증가 | 저장이 싸다는 이유로 무제한 복제 | 소유자·사용량·수명주기·비용 배부·폐기 기준 | FinOps와 자산 정리 |
| 다중 엔진 결과 불일치 | 스키마·Snapshot·Catalog 기준 상이 | 개방형 테이블 포맷과 단일 Catalog·동시성 정책 | 일관된 읽기·쓰기 |

## Ⅶ. 저장소가 아닌 신뢰 가능한 데이터 제품 기반으로 전환

- **[반입계약-Catalog-SLO-수명주기의 폐루프]**: 원본을 많이 모으는 것만으로 가치는 생기지 않고 소유·품질·사용·폐기가 추적되지 않으면 늪이 됨
- 나라면: 모든 데이터 반입을 Contract와 Owner 등록으로 시작하고, Curated Zone만 공식 데이터 제품으로 발행하며 품질·사용량·비용·보존기간을 함께 운영

#### 한줄 요약

- 데이터 레이크의 성공은 저장량이 아니라 신뢰 가능한 데이터 제품의 재사용률과 재현 가능성으로 판단함

## 1교시 10점 답안 발췌

```text
Source → Landing → Raw → Cleansed → Curated → BI·AI
              Catalog·Lineage·DQ·Security·Cost
```

| 비교 | DW | Lake | Lakehouse |
|---|---|---|---|
| 스키마 | Write | Read 중심 | 혼합·진화 |
| 목적 | 정형 BI | 탐색·AI | BI+AI |
| 핵심위험 | 경직성 | 데이터 늪 | 운영 복잡성 |

- 차별화: 반입 시 Contract·Owner·Catalog를 의무화하고 사용·품질·비용·보존을 SLO로 운영

## 출제 이력과 검증 출처

- 제137·139회 공식 문제지: 데이터 늪과 데이터 레이크 기반 플랫폼 관련 출제
- [Apache Iceberg Documentation](https://iceberg.apache.org/docs/latest/)
- [Q-Net 기술사 자료실](https://www.q-net.or.kr/man001.do?gSite=Q)

## 학습 체크

- [ ] Landing·Raw·Cleansed·Serving Zone을 그림
- [ ] Governance Plane을 모든 Zone에 걸쳐 표시함
- [ ] DW·Lake·Lakehouse를 동일 축으로 비교함
- [ ] 데이터 늪의 원인과 Catalog·Owner·SLO 대책을 연결함

## 연결 토픽

- [데이터 늪](./022_data_swamp/) · [빅데이터 플랫폼](./135_big_data_platform_architecture/) · [데이터 거버넌스](./006_data_governance/) · [데이터 관측가능성](./054_data_observability/)
