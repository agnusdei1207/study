---
title: "워크플로 스케줄링·백필"
author: "agnusdei1207"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 워크플로 스케줄링·백필의 개요

- 핵심 요약 : **워크플로 스케줄링·백필**은 DAG 기반 태스크 의존성 관리와 과거 데이터 소급 재처리를 자동화하는 데이터 엔지니어링 기술.
- 개념 : 데이터 파이프라인 및 대규모 배치 처리 환경에서 작업 간의 선후 의존 관계를 **방향성 비순환 그래프** (DAG: Directed Acyclic Graph)로 정의하여 자동 실행하는 **워크플로 스케줄링** (Workflow Scheduling) 과, 파이프라인 결함 수정이나 지연 도착 데이터(Late Data) 처리를 위해 과거 특정 기간의 데이터를 소급 재실행하는 **백필** (Backfill) 오케스트레이션 엔지니어링 기술.
- 배경 및 필요성 : 단순 **cron** 기반 스케줄링은 태스크 간 의존성 관리 불가, 장애 발생 시 부분 재실행 곤란, 과거 데이터 재생성 시 극심한 수작업 오류를 유발하므로 대규모 엔터프라이즈 데이터 플랫폼에서 통합 워크플로 엔진이 필수화됨.
- 핵심 목적 : 태스크 의존성(Dependency) 및 병렬성 최적화, 과거 특정 구간의 안전한 자동 백필, 파이프라인의 **멱등성** (Idempotency) 및 정합성 보장.

## Ⅱ. 워크플로 스케줄링·백필의 특징 및 장점

- 핵심 요약 : **DAG 스케줄링·논리적 실행 시점·파티션 원자적 교체**.
1. **논리적 실행 시점** (Logical Date / Execution Date) : 작업이 실제 실행되는 현재 물리적 시각이 아니라, 처리 대상 데이터가 속한 논리적 시간 윈도우(`data_interval_start`, `data_interval_end`)를 파라미터로 전달받아 실행.
2. **파티션 원자적 교체** : 백필 도중 조회자가 불완전한 데이터를 읽지 않도록 임시 디렉터리에 데이터를 모두 쓴 뒤 메타스토어 포인터를 원자적(Atomic)으로 스왑.

## Ⅲ. 워크플로 스케줄링·백필의 구조 및 동작 메커니즘

- 핵심 요약 : **DAG 정의 → 스케줄러/Executor → 워커 분배 → 파티션 원자적 교체**.
- 워크플로 DAG 스케줄링 및 백필은 Airflow Scheduler/Executor가 DAG Run 인스턴스를 생성하고 워커 노드에 분배하여 파티션 원자적 교체로 수행함.

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 워크플로 DAG (Apache Airflow) 스케줄링 및 백필 실행 구조 ]           │
│                                                                        │
│   [ 워크플로 DAG 정의 ]                                                │
│    (Task A: 데이터 추출) ──> (Task B: 정제 및 변환) ──> (Task C: 마트 적재)│
│                                                                        │
│   ─── [ 백필(Backfill) 명령 실행: 2026-01-01 ~ 2026-01-05 ] ────────── │
│                                                                        │
│   [ Airflow Scheduler & Executor ]                                     │
│    - DAG Run 인스턴스 5개 동시 생성 (logical_date 기준)                 │
│    - 동시성 제어: max_active_runs=2, max_active_tasks_per_dag=4        │
│                     │                                                  │
│                     ▼ Task Instance 분배                               │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ [ 워커 노드 풀 (Celery / Kubernetes Workers) ]                 │   │
│   │  [Worker 1] 2026-01-01 Run -> Task A -> Task B -> Task C       │   │
│   │  [Worker 2] 2026-01-02 Run -> Task A -> Task B -> Task C       │   │
│   └───────────────────────────────┬────────────────────────────────┘   │
│                                   │ 원자적 파티션 덮어쓰기             │
│                                   ▼                                    │
│   ┌────────────────────────────────────────────────────────────────┐   │
│   │ [ 타깃 데이터 스토리지 (Lakehouse / Data Warehouse) ]          │   │
│   │  - PARTITION (date = '2026-01-01') ATOMIC OVERWRITE!           │   │
│   │  - 타 날짜 데이터 간섭 없이 해당 파티션만 멱등하게 갱신       │   │
│   └────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```

## Ⅳ. 워크플로 스케줄링·백필의 비교

- 핵심 요약 : **Airflow·Dagster·Prefect** 패러다임·백필·상태저장소·데이터 전달·성숙도·한계 비교.

| 비교 항목 | Apache Airflow | Dagster | Prefect |
| :--- | :--- | :--- | :--- |
| 핵심 패러다임 | 태스크 중심 (Task-Centric DAG) | 자산 중심 (Software-Defined Assets) | 코드 중심 (Pythonic Functions) |
| 백필 지원성 | CLI(Command-Line Interface) 명령어(`airflow dags backfill`) 강력 지원 | 자산 파티셔닝 기반 정밀 백필 네이티브 지원 | 파라미터 기반 플로우 재실행 지원 |
| 상태 저장소 | RDBMS(Relational Database Management System) 필수 (PostgreSQL, MySQL) | RDBMS 지원 (PostgreSQL, SQLite) | 클라우드 서비스(SaaS) 또는 백엔드 DB(Database) |
| 데이터 전달 방식 | XCom 기반 (소용량 메타데이터 전용) | 네이티브 I/O 매니저 기반 데이터 전달 | 결과 핸들러(Result Handlers) 기반 |
| 생태계 성숙도 | 업계 사실상 표준 (De-facto Standard) | 빠르게 성장 중인 모던 데이터 스택 | 파이썬 친화적 경량 워크플로 중심 |
| 단점 및 한계점 | 스케줄러 루프 지연, 로컬 테스트 난이도 | 기존 Airflow 대비 학습 곡선 존재 | 대규모 엔터프라이즈 레거시 연동성 |

## Ⅴ. 워크플로 스케줄링·백필의 한계와 방안

- 핵심 요약 : **원천 시스템 과부하·비멱등성 중복 적재·Execution Date 혼선**을 동시성 제어·Upsert·data_interval로 대응.

- 원천 시스템(소스 DB/API(Application Programming Interface)) 과부하로 인한 장애 유발 :
  - 한계점 : 수개월 치 데이터를 백필할 때 수십 개의 DAG(Directed Acyclic Graph) 인스턴스가 동시 기동하여 원천 OLTP(Online Transaction Processing) 데이터베이스 커넥션 고갈 및 슬로우 쿼리 유발.
  - 해결 방안 : Airflow 풀(Pool) 기능을 활용한 동시 쿼리 수 제한, `max_active_runs` 파라미터 조절 및 주말/야간 유휴 시간 대역 한정 실행.
- 태스크 비멱등성(Non-Idempotency)에 따른 데이터 중복 적재 :
  - 한계점 : 단순 `INSERT INTO`로 작성된 파이프라인을 백필할 경우 동일 날짜의 데이터가 두 배, 세 배로 중복되어 매출 집계 왜곡.
  - 해결 방안 : 타깃 테이블의 `INSERT OVERWRITE` 또는 `MERGE INTO` (Upsert) 쿼리 강제, 파이프라인 코드 리뷰 시 멱등성 검증 체크리스트 의무화.
- 시간 윈도우 파라미터 혼선(Execution Date Confusion) :
  - 한계점 : Airflow의 전통적인 `execution_date`는 주기 시작 시점을 가리켜 실제 배치 실행 시점(주기 종료 시점)과 시차가 있어 개발자 실수 빈번.
  - 해결 방안 : Airflow 2.2+의 `data_interval_start` 및 `data_interval_end` 표준 시간 윈도우 템플릿 변수로 전면 리팩토링.

## Ⅵ. 워크플로 스케줄링·백필 적용 제언

- 핵심 요약 : **자산 중심 아키텍처·CI/CD 백필 테스트베드**.
- 선언적 데이터 자산(Data Asset) 중심 아키텍처로의 전환 : Task-Driven → Asset-Driven (Dagster, dbt), 백필 시 상위/하위 의존 자산 역추적.
- CI/CD 파이프라인과 통합된 백필 검증 테스트베드 구축 : 스테이징에서 최근 7일 가상 백필 자동 수행, 데이터 차이(Data Diff) 리포팅.

## Ⅶ. 결론

- 핵심 요약 : 워크플로 스케줄링·백필은 **DAG 의존성 관리와 소급 재처리**를 자동화하나 원천 시스템 과부하·비멱등성·시간 윈도우 혼선 리스크 관리가 필수.
- 워크플로 스케줄링·백필은 DAG 의존성 관리와 소급 재처리를 자동화하지만, 원천 시스템 과부하·비멱등성 중복 적재·시간 윈도우 혼선 리스크를 동시성 제어·Upsert·data_interval로 관리해야 함.
- 답안에는 DAG 스케줄링, Airflow/Dagster/Prefect 비교, 백필 메커니즘, 한계·대응, 자산 중심·CI/CD 테스트베드 제언을 연결. (Directed Acyclic Graph, DAG) (Logical Date / Execution Date) (data_interval_start, data_interval_end) (Atomic Overwrite) (Idempotency, Idempotent) (INSERT OVERWRITE, MERGE INTO, Upsert) (max_active_runs, max_active_tasks_per_dag) (Pool) (XCom) (Software-Defined Assets) (Pythonic Functions) (Result Handlers) (CLI, Command-Line Interface) (RDBMS, Relational Database Management System) (PostgreSQL, MySQL, SQLite) (SaaS, Software as a Service) (De-facto Standard) (modular data stack) (OLTP, Online Transaction Processing) (API, Application Programming Interface) (dbt, data build tool) (Data Diff) (CI, Continuous Integration) (CD, Continuous Delivery) (DAG, Directed Acyclic Graph) (Logical Date / Execution Date) (data_interval_start, data_interval_end) (Atomic Overwrite) (Idempotency, Idempotent) (INSERT OVERWRITE, MERGE INTO, Upsert) (max_active_runs, max_active_tasks_per_dag) (Pool) (XCom) (Software-Defined Assets) (Pythonic Functions) (Result Handlers) (CLI, Command-Line Interface) (RDBMS, Relational Database Management System) (PostgreSQL, MySQL, SQLite) (SaaS, Software as a Service) (De-facto Standard) (modular data stack) (OLTP, Online Transaction Processing) (API, Application Programming Interface) (dbt, data build tool) (Data Diff) (CI, Continuous Integration) (CD, Continuous Delivery)