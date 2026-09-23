---
sidebar:
  order: 92
  label: "092. 파티셔닝 (Partitioning)"
  badge:
    text: "A"
    variant: note
title: "데이터베이스 파티셔닝(Partitioning) 전략과 데이터 분할 아키텍처"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 92
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "092"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터베이스 설계·물리모델</span><strong>파티셔닝 (Partitioning)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 230" width="100%" height="auto" role="img" aria-label="데이터베이스 파티셔닝 구조 및 파티션 프루닝 메커니즘">
  <defs>
    <marker id="partArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="230" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Top Logical Table Box -->
  <rect x="25" y="15" width="470" height="42" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="1.5"/>
  <text x="40" y="32" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">[논리적 단일 테이블] 주문 (Orders)</text>
  <text x="40" y="48" font-size="10" fill="var(--sl-color-text, #334155)">질의: WHERE 주문일자 BETWEEN '2026-03-01' AND '2026-03-31'</text>

  <!-- Pruning Indicator -->
  <path d="M 260 57 L 260 82" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="2" marker-end="url(#partArr)"/>
  <rect x="180" y="65" width="160" height="18" rx="4" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #bfdbfe)"/>
  <text x="260" y="78" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">옵티마이저 파티션 프루닝 (Pruning)</text>

  <!-- Bottom Partitions -->
  <!-- Partition 1 -->
  <g transform="translate(25, 90)">
    <rect width="145" height="75" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)" stroke-dasharray="3 3"/>
    <text x="72" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-gray-3, #94a3b8)">Part 1 (2026-01)</text>
    <text x="72" y="44" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3, #94a3b8)">세그먼트 A</text>
    <rect x="15" y="52" width="115" height="16" rx="3" fill="#f1f5f9"/>
    <text x="72" y="64" text-anchor="middle" font-size="8.5" font-weight="600" fill="#dc2626">스캔 배제 (I/O 0%)</text>
    <!-- Local Index 1 -->
    <rect y="82" width="145" height="32" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <text x="72" y="102" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2, #64748b)">Local Index 1 (1:1)</text>
  </g>

  <!-- Partition 2 -->
  <g transform="translate(187, 90)">
    <rect width="145" height="75" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)" stroke-dasharray="3 3"/>
    <text x="72" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-gray-3, #94a3b8)">Part 2 (2026-02)</text>
    <text x="72" y="44" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3, #94a3b8)">세그먼트 B</text>
    <rect x="15" y="52" width="115" height="16" rx="3" fill="#f1f5f9"/>
    <text x="72" y="64" text-anchor="middle" font-size="8.5" font-weight="600" fill="#dc2626">스캔 배제 (I/O 0%)</text>
    <!-- Local Index 2 -->
    <rect y="82" width="145" height="32" rx="4" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <text x="72" y="102" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2, #64748b)">Local Index 2 (1:1)</text>
  </g>

  <!-- Partition 3 (Target) -->
  <g transform="translate(350, 90)">
    <rect width="145" height="75" rx="6" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.8"/>
    <text x="72" y="24" text-anchor="middle" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">Part 3 (2026-03)</text>
    <text x="72" y="44" text-anchor="middle" font-size="9" fill="var(--sl-color-text, #1e293b)">세그먼트 C</text>
    <rect x="15" y="52" width="115" height="16" rx="3" fill="var(--sl-color-accent, #dbeafe)"/>
    <text x="72" y="64" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-accent, #1e40af)">물리적 I/O 집중 스캔</text>
    <!-- Local Index 3 -->
    <rect y="82" width="145" height="32" rx="4" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #3b82f6)"/>
    <text x="72" y="102" text-anchor="middle" font-size="9" font-weight="600" fill="var(--sl-color-accent, #1d4ed8)">Local Index 3 (1:1)</text>
  </g>
</svg>
</div>

- 본질: **수억 건 규모의 대용량 테이블이나 인덱스를 애플리케이션 관점에서는 논리적으로 단일 객체로 유지하면서, 물리적으로는 독립된 세그먼트(Segment) 단위로 분할하여 I/O 부하 분산, 파티션 프루닝(Pruning)을 통한 성능 향상 및 무중단 데이터 라이프사이클 관리를 구현하는 기술**
- 암기: `범-목-해-복` (4대 분할 방식: Range, List, Hash, Composite) / `프-가-관-성` (기대효과: 프루닝, 가용성, 관리성, 성능)
- 판단축:
  - **Range(범위)**: 시계열·이력 데이터 보관주기 관리에 최적 (DROP PARTITION으로 즉시 삭제)
  - **List(목록)**: 지역코드, 사업부코드 등 불연속 카테고리 데이터 분할에 적합
  - **Hash(해시)**: 균등 분산으로 I/O 경합(Hot Spot) 해소, 범위 검색에는 부적합
  - **Composite(복합)**: Range+Hash 또는 Range+List로 다차원 대용량 최적화
- 주의: 글로벌 인덱스(Global Index)가 걸린 파티션을 DROP할 경우 전체 인덱스가 `UNUSABLE` 상태에 빠져 전사 장애를 유발하므로 반드시 `UPDATE GLOBAL INDEXES` 옵션을 부여하거나 로컬 파티션 인덱스를 설계해야 함
---

## 1교시 예상문제 (10점)

> 데이터베이스 파티셔닝(Partitioning) 전략과 데이터 분할 아키텍처의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### [문제] 파티셔닝 (Partitioning)

#### 1. 파티셔닝(Partitioning)의 개념
- 대용량 테이블을 논리적으로 단일 객체로 유지하며, 물리적으로 독립된 세그먼트로 분할하여 I/O 부하 분산 및 파티션 프루닝(Pruning)을 달성하는 물리 모델링 기술

#### 2. 파티셔닝 4대 분할 방식 및 인덱스 구조

| 분할 방식 | 핵심 메커니즘 | 최적 적용 업무 |
|:---|:---|:---|
| **Range (범위)** | 연속적인 날짜나 숫자 범위 기준 | 주문 이력, 로그 등 시계열 데이터 |
| **List (목록)** | 고정된 불연속 코드 목록 기준 | 지역코드, 사업부별 데이터 |
| **Hash (해시)** | 해시 알고리즘 균등 분산 | 고객 마스터, I/O 핫스팟 해소 |
| **Composite (복합)** | Range + Hash/List 계층적 결합 | 초대용량 멀티차원 트랜잭션 |

- **파티션 인덱스 구분**:
  - **로컬 인덱스(Local Index)**: 테이블 파티션과 1:1 매핑, 파티션 DROP 시 타 세그먼트 영향 전무(장애 격리 최상)
  - **글로벌 인덱스(Global Index)**: 테이블 파티션과 독립적 구조, 파티션 DROP 시 `UPDATE GLOBAL INDEXES` 누락 시 UNUSABLE 장애 발생

#### 3. 파티션 프루닝(Partition Pruning)의 효과
- 조건절 분석을 통해 불필요한 물리 파티션 스캔을 원천 배제하여 대용량 풀스캔 I/O 병목 해소
---

### 핵심 관계

| 분할 방식 | 분할 기준 및 메커니즘 | 주요 적용 사례 | 장점 및 고려사항 |
|:---|:---|:---|:---|
| **Range (범위)** | 날짜, 일련번호 등 연속적인 값의 범위를 기준으로 분할 (`VALUES LESS THAN`) | 주문 이력, 거래 내역, 접속 로그, 결제 데이터 | 시계열 데이터 관리에 최적, 주기적 파티션 추가 및 일괄 삭제 용이 |
| **List (목록)** | 국가코드, 부서코드, 결제수단 등 불연속적인 고정 코드 목록 기준 | 지역별 매장 테이블, 통신사 가입자 유형 | 특정 코드별 데이터 독립 관리, 예측 불가능한 값 입력 시 에러(Default 파티션 필요) |
| **Hash (해시)** | 파티션 키에 해시 함수를 적용하여 지정된 개수의 파티션에 균등 분할 | 고객 마스터, 계좌 테이블, 장비 센서 데이터 | 데이터 분포의 균일성 보장, I/O 핫스팟 제거, 범위 검색(Range Scan) 불가능 |
| **Composite (복합)** | 주 파티션(Range)과 서브 파티션(Hash 또는 List)의 2단계 계층적 분할 | 일자별 대용량 거래 테이블의 고객 ID별 분산 | 초대용량 테이블의 관리성과 검색 성능 동시 만족, 관리 복잡도 증가 |

---

## 2~4교시 예상문제 (25점)

> 대용량 데이터베이스의 성능 최적화와 가용성 확보를 위한 파티셔닝(Partitioning)의 개념과 4대 분할 방식을 비교하고, 파티션 프루닝(Partition Pruning)의 동작 메커니즘 및 로컬 인덱스와 글로벌 인덱스의 구조적 차이점을 설명하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 대용량 데이터의 한계를 극복하는 파티셔닝(Partitioning) 개요

#### 한줄 요약: 대규모 단일 테이블을 복수의 물리적 세그먼트로 나누어 스캔 비용을 줄이고 데이터 삭제/백업을 고속화하는 물리 모델링 기법

- **배경**: 단일 테이블 데이터가 수억 건을 초과하면 B-Tree 인덱스 높이(Depth) 증가, Full Table Scan 시 I/O 병목 발생, `DELETE` 시 대량의 Undo/Redo 로깅으로 DBMS 락(Lock) 경합 발생
- **정의**: 논리적으로는 하나의 테이블이지만 물리적으로는 지정된 파티션 키(Partition Key)에 따라 여러 개의 데이터 파일 및 세그먼트로 분할 저장하는 기법
- **핵심 목표**: 파티션 프루닝(불필요한 파티션 배제), 가용성 격리(특정 파티션 장애가 타 파티션에 미치는 영향 차단), 유지보수 생산성 극대화

### Ⅱ. 파티셔닝의 4대 분할 방식 비교

#### 한줄 요약: 데이터의 특성과 쿼리 패턴에 따라 Range, List, Hash, Composite 방식을 전략적으로 선택

| 분할 방식 | 분할 기준 및 메커니즘 | 주요 적용 사례 | 장점 및 고려사항 |
|:---|:---|:---|:---|
| **Range (범위)** | 날짜, 일련번호 등 연속적인 값의 범위를 기준으로 분할 (`VALUES LESS THAN`) | 주문 이력, 거래 내역, 접속 로그, 결제 데이터 | 시계열 데이터 관리에 최적, 주기적 파티션 추가 및 일괄 삭제 용이 |
| **List (목록)** | 국가코드, 부서코드, 결제수단 등 불연속적인 고정 코드 목록 기준 | 지역별 매장 테이블, 통신사 가입자 유형 | 특정 코드별 데이터 독립 관리, 예측 불가능한 값 입력 시 에러(Default 파티션 필요) |
| **Hash (해시)** | 파티션 키에 해시 함수를 적용하여 지정된 개수의 파티션에 균등 분할 | 고객 마스터, 계좌 테이블, 장비 센서 데이터 | 데이터 분포의 균일성 보장, I/O 핫스팟 제거, 범위 검색(Range Scan) 불가능 |
| **Composite (복합)** | 주 파티션(Range)과 서브 파티션(Hash 또는 List)의 2단계 계층적 분할 | 일자별 대용량 거래 테이블의 고객 ID별 분산 | 초대용량 테이블의 관리성과 검색 성능 동시 만족, 관리 복잡도 증가 |

### Ⅲ. 파티션 프루닝(Partition Pruning) 메커니즘

#### 한줄 요약: 옵티마이저가 질의 조건절을 분석하여 쿼리 대상이 아닌 물리 파티션을 디스크 I/O 대상에서 원천 배제하는 고속화 기술

- **동작 원리**:
  1. 쿼리 파서 및 옵티마이저가 `WHERE` 조건절의 파티션 키 컬럼 조건 탐색
  2. 메타데이터 딕셔너리의 파티션 바운더리(경계값)와 비교
  3. 조건에 부합하지 않는 파티션 세그먼트는 디스크 I/O 읽기 목록에서 원천 배제
- **프루닝 유형**:
  - **정적 프루닝 (Static Pruning)**: 상수 조건으로 하드코딩되어 컴파일 타임에 접근 파티션 결정 (`Pstart = Pstop = 3`)
    - 예: `WHERE 주문일자 = '20260315'` $\rightarrow$ 컴파일 시점에 'Part 3' 세그먼트만 스캔하도록 플랜 확정
  - **동적 프루닝 (Dynamic Pruning)**: 바인드 변수나 서브쿼리 결과에 의해 실행 런타임에 대상 파티션 동적 필터링 (`KEY(AP)` 표시)
    - 예: `WHERE 주문일자 = :bind_date` $\rightarrow$ 런타임 변수 평가 후 해당 세그먼트만 선택적 I/O

### Ⅳ. 파티션 인덱스 아키텍처: 로컬 인덱스 vs 글로벌 인덱스

#### 한줄 요약: 테이블 파티션과 1:1로 동일하게 분할되는 로컬 인덱스와 독립적인 키 체계를 갖는 글로벌 인덱스의 대조

| 구분 | 로컬 파티션 인덱스 (Local Index) | 글로벌 파티션 인덱스 (Global Index) | 비파티션 글로벌 인덱스 |
|:---|:---|:---|:---|
| **구조적 관계** | 테이블 파티션과 인덱스 파티션이 **1:1 완벽 대응** | 테이블 파티션과 무관하게 독자적인 키 기준으로 분할 | 단일 B-Tree 구조로 전체 테이블 행을 인덱싱 |
| **파티션 키** | 기본적으로 테이블의 파티션 키를 포함 | 테이블의 파티션 키와 완전히 다른 컬럼 가능 | 파티션 개념 없음 |
| **관리 편의성** | 극도로 우수 (특정 파티션 DROP/TRUNCATE 시 해당 인덱스만 삭제) | 낮음 (파티션 DROP 시 글로벌 인덱스 재구축 필요) | 최하 (파티션 변경 시 인덱스 전체가 UNUSABLE) |
| **장애 격리** | 특정 인덱스 파티션 파손 시 타 파티션 정상 서비스 | 인덱스 파티션 손상 시 다중 테이블 파티션 영향 | 인덱스 파손 시 전사 쿼리 중단 |
| **조회 성능** | 조건절에 파티션 키 포함 시 초고속 (미포함 시 전체 인덱스 탐색) | 파티션 키 없는 조건 검색에서도 단일 글로벌 인덱스로 고속 탐색 | 파티션 키와 무관한 유니크 제약(PK) 보장에 필수 |

### Ⅴ. 파티셔닝과 샤딩(Sharding)의 차이점

#### 한줄 요약: 단일 DBMS 인스턴스 내부의 물리 분할(Scale-Up)과 복수 노드 간 네트워크 분산(Scale-Out)의 구조적 차이

| 비교 항목 | 데이터베이스 파티셔닝 (Partitioning) | 데이터베이스 샤딩 (Sharding) |
|:---|:---|:---|
| **물리적 위치** | 단일 DBMS 서버 또는 단일 스토리지 내 복수 세그먼트 | 여러 대의 물리/가상 서버(노드)에 데이터 분산 저장 |
| **확장 방식** | 수직 확장 (Scale-Up 중심) | 수평 확장 (Scale-Out 중심) |
| **트랜잭션 관리** | 단일 DBMS 엔진이 ACID 완전 보장 (로컬 트랜잭션) | 2PC(Two-Phase Commit) 필요, 결과적 일관성(Eventual Consistency) 채택 |
| **조인(Join) 처리** | 파티션 간 조인 연산이 DBMS 내부 메모리에서 즉시 수행 | 샤드 간 조인(Cross-Shard Join)이 극도로 어렵거나 불가 |
| **관리 복잡도** | RDBMS 자체 내장 기능(DDL)으로 비교적 단순 | 애플리케이션 레벨 샤드 라우팅 및 리샤딩(Re-sharding) 복잡성 극심 |

### Ⅵ. 실무 운영 이슈 및 트러블슈팅 지침

#### 한줄 요약: 파티션 프루닝 누락, 글로벌 인덱스 언유저블(UNUSABLE), 롤링 파티션 락을 방지하는 실무 체크리스트

| 장애 상황 | 근본 원인 | 실무 해결 및 예방 조치 |
|:---|:---|:---|
| **파티션 프루닝 미동작** | 쿼리 `WHERE` 조건절에서 파티션 키 컬럼을 가공(`TO_CHAR(주문일자, 'YYYY') = '2026'`)하여 인덱스/파티션 무력화 | 컬럼 변형 금지, `주문일자 >= '20260101' AND 주문일자 < '20260201'`로 작성 |
| **Index Unusable 전사 장애** | 보관주기 만료로 `ALTER TABLE DROP PARTITION` 수행 시 글로벌 인덱스가 깨짐 | DDL 수행 시 `ALTER TABLE DROP PARTITION p_old UPDATE GLOBAL INDEXES;` 구문 필수 적용 |
| **데이터 쏠림(Skew) 현상** | 특정 Range 파티션 또는 Hash 키 편향으로 1개 세그먼트만 기가바이트 단위 비대화 | Composite 파티셔닝(Range + Hash) 도입, 비즈니스 특성에 맞는 파티션 키 재선정 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 파티셔닝의 가장 위대한 실무적 가치는 조회 성능(파티션 프루닝)보다 '데이터 라이프사이클 관리(ILM)'에 있다. 1억 건 테이블에서 1년 지난 데이터를 `DELETE`로 지우려면 수 시간이 소요되고 Undo/Redo 폭증으로 데이터베이스가 정지되지만, Range 파티션으로 설계되어 있다면 `ALTER TABLE DROP PARTITION` 명령 단 0.1초 만에 메타데이터 포인터 삭제로 완료된다. 단, 글로벌 인덱스가 존재할 경우 `UPDATE GLOBAL INDEXES`를 누락하면 서비스 장애가 발생하므로, 인덱스는 가급적 로컬 파티션 인덱스로 설계해야 한다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 파티션 프루닝 다이어그램과 4대 분할 방식(범-목-해-복) 비교표를 일목요연하게 제시하겠다. 2교시 25점형이라면 로컬 인덱스와 글로벌 인덱스의 구조적 차이와 `UNUSABLE` 장애 메커니즘을 상세히 분석하고, 핫/웜/콜드 데이터 수명주기(ILM)를 고려하여 최근 3개월은 SSD 파티션, 1년 경과는 SAS, 영구 보관은 `EXCHANGE PARTITION`을 통해 클라우드 오브젝트 스토리지(Parquet)로 내보내는 하이브리드 티어링 아키텍처를 제언하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 대용량 이력 테이블에 보관 주기 만료 데이터를 단순 `DELETE`로 삭제 시 락 경합 및 트랜잭션 로그 급증으로 서비스 다운타임 발생. 또한 비파티션 글로벌 인덱스 환경에서 파티션 관리 작업 시 전사 인덱스 비활성화 위험 상존.
- **대응 (개선 방안)**: 시계열 Range 파티셔닝과 로컬 파티션 인덱스를 기본 원칙으로 수립하고, 데이터 적재 및 폐기 시 `EXCHANGE PARTITION`을 활용하여 메타데이터 포인터 스왑 방식으로 시스템 락 시간을 밀리초 단위로 최소화.
- **검증 (검증 기준)**: 일별 파티션 프루닝 적용률 100%, 글로벌 인덱스 종속성 0건 유지(필수 PK는 파티션 키 포함 복합 PK 설계), 파티션 DROP 시 DDL 수행 시간 1초 미만 검증.
- **효과 (실행 효과)**: 배치 삭제 소요 시간 99% 단축(수 시간 $\rightarrow$ 0.1초), Undo/Redo I/O 95% 절감, 24x365 무중단 데이터 보관주기 라이프사이클 완성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">대량 DELETE로 인한 락 경합, 글로벌 인덱스 파손으로 인덱스 무효화</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">Range 파티션 + 로컬 인덱스 표준화, Exchange Partition 무중단 전환</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">파티션 프루닝 100%, 글로벌 인덱스 0건, DDL 수행 시간 1초 이내</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">배치 삭제 0.1초 완료, Undo I/O 95% 절감, 365일 무중단 ILM 체계 구현</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제127회 정보관리 2교시: 대용량 데이터베이스의 파티셔닝 개념, 분할 방식 4가지 및 인덱스 파티션(로컬/글로벌)
  - 제138회, 제102회 기출
- **검증 출처**:
  - Oracle Database VLDB and Partitioning Guide (19c/23ai)
  - PostgreSQL Documentation Chapter 5.11 Table Partitioning
---

## 연결 토픽

- 상위 토픽: [021. DB 파티셔닝과 샤딩 (DB Partitioning & Sharding)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/021_db_partitioning_sharding.md)
- 연관 토픽: [045. 샤딩 (Sharding)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/045_sharding.md), [047. 인덱스 (Index)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index.md)
