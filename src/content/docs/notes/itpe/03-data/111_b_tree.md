---
sidebar:
  order: 111
  label: "111. B-Tree·B+Tree"
  badge:
    text: "C"
    variant: note
title: "B-Tree와 B+Tree 색인 구조의 동작 메커니즘 및 DBMS 인덱스 최적화"
author: "OpenAI Codex"
date: "2026-09-20T19:20:00+09:00"
tags:
  - "notes-data"
weight: 111
extra:
  model: "GPT-5"
  keyword_grade: "C"
  question_no: "111"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>자료구조·인덱스</span><strong>B-Tree·B+Tree</strong></div>

## 큰 그림과 30초 인출

```text
[B-Tree와 B+Tree의 내부 노드 및 리프 노드 구조 비교]

 [1. B-Tree: 모든 노드가 키와 데이터 포인터 보유]
    [내부 노드] : [ P0 | Key 20, RID | P1 | Key 50, RID | P2 ]
                   - 단건 탐색 시 상위 노드에서 즉시 반환 가능
                   - 블록 내 데이터 포인터(RID) 차지로 Fan-out 감소, 트리 높이 증가
                   - 범위 검색 시 트리를 부모-자식 간에 반복 재탐색(In-order Traversal)

 [2. B+Tree: 내부 노드는 라우팅 키만, 모든 데이터는 리프 노드에 집중]
    [내부 노드] : [ P0 | Key 20 | P1 | Key 50 | P2 ] (Fan-out 극대화, 3~4 레벨 압축)
                       │          │          │
    [리프 노드] : [Key 10,RID] ◄► [Key 20,RID] ◄► [Key 30,RID] ◄► [Key 50,RID]
                   - 모든 리프 노드가 양방향 연결 리스트(Doubly Linked List)로 결합
                   - 범위 검색(BETWEEN) 시 리프 노드 간 수평 순차 스캔으로 I/O 극소화
```

- 본질: **디스크 I/O 횟수를 최소화하기 위해 노드 1개를 디스크 블록(Page) 1개에 매핑하여 높은 팬아웃(Fan-out)을 갖는 다원 균형 탐색 트리(B-Tree)와, 모든 실제 데이터를 최하위 리프 노드에만 배치하고 양방향 연결 리스트로 묶어 범위 검색(Range Scan)을 $O(K + \log N)$에 완결하는 현대 RDBMS 표준 인덱스 구조(B+Tree)**
- 암기: `균-다-블-분` (균형트리, 다원탐색, 디스크블록 매핑, 분할/병합) / `비플-리-연-팬` (B+Tree는 리프집중, 양방향연결, 팬아웃극대화)
- 판단축:
  - **B-Tree**: 단건 동등 검색(`=`) 시 상위 레벨에서 즉시 발견될 수 있으나 범위 검색 시 비효율
  - **B+Tree**: 모든 쿼리가 리프까지 내려가야 하나($O(\log N)$ 고정), 인덱스 레인지 스캔 및 풀 인덱스 스캔 성능이 압도적이어서 Oracle, MySQL(InnoDB), PostgreSQL 표준 채택
- 주의: 무작위(Random) 키 대량 삽입 시 리프 노드가 50% 분할되는 **인덱스 페이지 분할(Page Split)**이 연쇄 발생하여 I/O 경합과 인덱스 단편화가 유발되므로 채번 전략(시퀀스, TSID) 고려가 필수적임

## 예상문제

> 데이터베이스 인덱스의 핵심 자료구조인 B-Tree와 B+Tree의 개념 및 내부 노드·리프 노드 구조를 비교하고, 노드의 삽입(Split)과 삭제(Merge) 메커니즘 및 B+Tree가 현대 RDBMS의 표준 인덱스로 채택된 공학적 이유를 설명하시오. (25점)

## Ⅰ. 디스크 I/O 병목을 해결하는 다원 균형 트리 개요

#### 한줄 요약: 이진 트리의 높이 문제를 극복하기 위해 노드당 다수의 키를 배치하여 트리의 높이를 3~4단계로 낮춘 디스크 친화적 인덱스 구조

- **배경**: 메모리 기반의 이진 탐색 트리(BST, AVL, Red-Black Tree)는 데이터 1,000만 건 적재 시 트리의 높이가 약 24레벨에 달해 디스크 I/O가 24번 발생하여 심각한 지연 발생
- **정의**:
  - **B-Tree**: 차수 $M$을 기준으로 모든 노드가 최대 $M-1$개의 키와 $M$개의 자식 포인터를 가지며, 모든 리프 노드가 동일한 깊이를 유지하는 자가 균형 다원 탐색 트리
  - **B+Tree**: B-Tree를 개량하여 내부 노드는 분기(라우팅) 목적의 키만 보관하고, 모든 실제 데이터(RID)는 리프 노드에만 중복 저장하며 리프 노드들을 포인터로 연결한 구조

## Ⅱ. B-Tree의 구조적 규칙과 수학적 제약조건

#### 한줄 요약: 차수 $M$에 따라 루트, 내부 노드, 리프 노드가 만족해야 하는 최소·최대 키 개수 제약

```text
 [차수 M인 B-Tree 노드의 수학적 불변식 (Invariants)]
  1. 루트 노드: 최소 2개 이상의 자식 노드 보유 (자식이 있는 경우)
  2. 내부/리프 노드: 최소 ⌈M/2⌉개의 자식 보유 (최소 ⌈M/2⌉ - 1개의 키 보유)
  3. 모든 노드: 최대 M개의 자식 보유 (최대 M - 1개의 키 보유)
  4. 모든 리프 노드는 반드시 동일한 레벨(Level)에 위치함 (완벽한 균형)
```

| 노드 구성요소 | B-Tree 구조 | B+Tree 구조 |
|:---|:---|:---|
| **내부 노드 (Non-Leaf)** | 자식 포인터($P$) + 키($Key$) + **데이터 레코드 포인터($RID$)** | 자식 포인터($P$) + **인덱스 분기 키($Key$)만 저장** |
| **리프 노드 (Leaf Node)** | 자식 포인터 없음 + 키($Key$) + 데이터 레코드 포인터($RID$) | 키($Key$) + 데이터 레코드 포인터($RID$) + **Prev/Next 링크** |
| **키의 중복성** | 트리 전체에서 각 키는 **단 1회만 유일하게 등장** | 내부 노드의 키가 리프 노드에 **다시 한 번 중복 등장** |

## Ⅲ. B-Tree vs B+Tree 핵심 특성 비교

#### 한줄 요약: 단건 검색에 유리한 B-Tree와 대규모 범위 검색 및 팬아웃에서 압도적인 B+Tree의 대조

| 비교 항목 | B-Tree | B+Tree |
|:---|:---|:---|
| **실제 데이터 저장 위치** | 루트, 내부 노드, 리프 노드 **모두에 저장** | **오직 최하위 리프 노드에만 저장** |
| **팬아웃 (Fan-out)** | 데이터 포인터로 인해 노드당 키 수 적음 ($\approx 100$) | 데이터가 없어 노드당 수백~수천 개 키 수용 ($\approx 1,000$) |
| **트리 높이 (Depth)** | 상대적으로 높음 (동일 데이터 기준 4~6 레벨) | 극단적으로 낮음 (수억 건 데이터도 **3~4 레벨 유지**) |
| **단건 검색 성능 ($=$)** | 상위 노드 적중 시 $O(1) \sim O(\log N)$ 가변 | 무조건 리프 노드까지 도달해야 하므로 **$O(\log N)$ 균일** |
| **범위 검색 성능 (BETWEEN)** | 매우 느림 (In-order 트리 재순회로 Random I/O 다발) | **초고속** (리프 노드 양방향 링크를 따라 **Sequential I/O**) |
| **인덱스 풀스캔** | 트리 전체를 중위 순회 탐색 | 리프 노드 체인만 수평으로 1차원 순차 읽기 |
| **현대 DBMS 채택** | SQLite 일부, NoSQL 키-값 저장소 | **Oracle, MySQL(InnoDB), PostgreSQL, SQL Server** |

## Ⅳ. B+Tree 인덱스의 동적 갱신: 노드 분할(Split)과 병합(Merge)

#### 한줄 요약: 노드 포화 시 상향 분할하는 Split과, 언더플로우 시 인접 노드와 결합하는 Merge

```text
 [1. 삽입 연산: 노드 분할 (Page Split)]
  Step 1: 탐색을 통해 신규 키가 삽입될 적절한 리프 노드 위치 결정
  Step 2: 리프 노드에 빈 공간이 있으면 키를 정렬 순서에 맞게 삽입
  Step 3: 노드가 가득 찬 상태(M-1개 초과)이면 노드를 50:50으로 둘로 분할
  Step 4: 중간 키(Median Key)를 복사하여 부모 노드로 승격 (B+Tree는 리프에도 키 유지)
  Step 5: 부모 노드도 가득 차면 루트까지 분할이 상향 전파 -> 루트 분할 시 트리 높이 1 증가

 [2. 삭제 연산: 노드 재분배 및 병합 (Merge)]
  Step 1: 리프 노드에서 대상 키 삭제
  Step 2: 노드의 키 개수가 최소 기준(⌈M/2⌉ - 1) 미만으로 떨어지면 언더플로우 발생
  Step 3: 형제(Sibling) 노드에 여유 키가 있으면 키를 하나 빌려옴 (Borrow / Redistribution)
  Step 4: 형제 노드도 여유가 없으면 두 노드를 하나로 합침 (Merge)
  Step 5: 부모 노드의 분기 키를 제거하고, 언더플로우가 상향 전파되어 루트 노드 병합 시 높이 감소
```

## Ⅴ. B+Tree가 현대 RDBMS의 표준이 된 3대 공학적 이유

#### 한줄 요약: 극대화된 팬아웃, 완벽한 범위 스캔 성능, 디스크 프리페치(Prefetch) 친화성

1. **팬아웃(Fan-out) 극대화로 디스크 I/O 최소화**:
   - 16KB 인스턴스 블록에서 8바이트 키와 8바이트 포인터를 사용할 경우, B+Tree 내부 노드는 블록당 약 1,000개의 자식 포인터를 수용 가능
   - 1,000개의 팬아웃을 가지면 **단 3번의 블록 읽기($1,000^3 = 10$억 건)**만으로 10억 개의 행 중 원하는 데이터를 즉시 탐색 완료
2. **범위 검색(Index Range Scan)의 압도적 효율성**:
   - `BETWEEN 20 AND 50` 쿼리 실행 시, 20이 위치한 리프 노드를 $O(\log N)$에 한 번만 찾으면, 이후 50을 만날 때까지 리프 노드의 `Next` 포인터를 따라 수평으로 디스크 블록을 연속 순차 읽기(Multi-block Read) 수행
3. **안정적인 쿼리 응답 시간 보장**:
   - B-Tree는 어떤 키는 루트(1회 I/O)에서 끝나고 어떤 키는 리프(4회 I/O)에서 끝나 응답 속도 편차가 심하지만, B+Tree는 모든 탐색 경로가 정확히 동일한 깊이를 거치므로 예측 가능한 일정한 레이턴시 제공

## Ⅵ. 실무 운영 이슈 및 인덱스 튜닝 (Troubleshooting)

#### 한줄 요약: 무작위 UUID 삽입으로 인한 페이지 분할 폭증과 인덱스 단편화 해소

| 장애 요인 | 근본 원인 | 실무 엔지니어링 극복 방안 |
|:---|:---|:---|
| **랜덤 UUID PK로 인한 Page Split** | `UUID v4`처럼 무작위 해시 문자열을 클러스터드 인덱스 PK로 채택하여 리프 노드 중간 삽입 폭증 | 시계열 정렬이 보장되는 **UUID v7 또는 TSID, Snowflake ID** 채택 |
| **인덱스 단편화(Fragmentation)** | 빈번한 `DELETE/UPDATE`로 인해 인덱스 페이지 내부 공간이 50% 이하로 낭비됨 | 주기적으로 `ALTER INDEX ... REBUILD` 또는 `OPTIMIZE TABLE` 수행 |
| **과도한 인덱스 생성** | 조회 성능만 고려하여 테이블당 10개 이상의 B+Tree 인덱스 생성 시 CUD 쓰기 성능 급락 | 테이블당 필수 인덱스 3~5개 이내로 제한, 복합 결합 인덱스(Composite)로 커버링 |

## Ⅶ. 기술사적 제언: SSD/NVMe 시대 B+Tree의 변형과 LSM-Tree와의 대립

#### 한줄 요약: B+Tree의 쓰기 증폭(Write Amplification) 한계를 극복하는 Bw-Tree 및 LSM-Tree 아키텍처

```text
 [전통적 B+Tree: Random Overwrite] ──► SSD 플래시 메모리의 덮어쓰기 한계 (쓰기 증폭)
                 │
                 ├──► [Bw-Tree / Masstree]: 락 프리(Lock-free) + 메모리 친화적 B+Tree
                 │
                 └──► [LSM-Tree (RocksDB/Cassandra)]: MemTable(메모리) + SSTable(순차 Append)
                      - 쓰기 처리량 10배 극대화 (대용량 쓰기 워크로드 대체)
```

- B+Tree는 읽기 성능이 매우 뛰어나지만, 임의 쓰기(Random Write)가 발생할 때마다 16KB 페이지 전체를 디스크에 다시 써야 하는 **쓰기 증폭(Write Amplification)** 문제를 안고 있음
- 이에 따라 읽기 중심의 정형 RDBMS는 **B+Tree**를 고수하되, 대규모 쓰기가 중심인 NoSQL(Cassandra, RocksDB)은 순차 쓰기 기반의 **LSM-Tree(Log-Structured Merge-Tree)**를 채택하여 상호 보완적인 인덱스 생태계를 형성하고 있음

---

## 1교시 10점 답안 발췌

```text
1. B-Tree와 B+Tree의 정의
  - B-Tree: 보조기억장치 블록 I/O를 최소화하기 위해 노드당 다수의 키를 갖는 자가 균형 다원 탐색 트리.
  - B+Tree: 내부 노드는 라우팅 키만 두고 모든 데이터를 리프에 모아 양방향 연결 리스트로 결합한 인덱스 표준 구조.

2. B-Tree vs B+Tree 구조적 차이점
  가. 데이터 저장: 모든 노드에 RID 저장(B-Tree) vs 최하위 리프 노드에만 중복 저장(B+Tree).
  나. Fan-out 및 높이: B+Tree는 내부 노드에 데이터가 없어 Fan-out 극대화, 트리 높이 3~4로 최소화.
  다. 범위 검색: 트리 재방문 필요(B-Tree) vs 리프 노드 간 수평 순차 스캔으로 초고속 처리(B+Tree).

3. RDBMS 표준 인덱스 채택 사유
  - 높은 Fan-out에 따른 I/O 최소화 및 Index Range Scan(BETWEEN/ORDER BY) 시 압도적 순차 읽기 성능 보장.
```

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제105회 정보관리 2교시: B-Tree의 개념과 특징, 삽입/삭제 연산 과정
  - 제101회, 제98회, 제89회 기출 (합숙·모의 최빈출 11회)
- **검증 출처**:
  - Thomas H. Cormen et al., "Introduction to Algorithms (CLRS 4th Edition)", Chapter 18 B-Trees
  - MySQL 8.0 Reference Manual, "15.6.2.1 Clustered and Secondary Indexes"

---

## 학습 체크

- [ ] B-Tree 차수 $M$에 따른 노드별 최소/최대 자식 수 및 키 개수 조건을 제시할 수 있는가?
- [ ] B+Tree가 B-Tree 대비 범위 검색(Range Scan)에서 성능이 압도적인 이유를 도식화할 수 있는가?
- [ ] B+Tree의 페이지 분할(Page Split)이 발생하는 원인과 랜덤 UUID PK의 문제점을 설명할 수 있는가?

---

## 연결 토픽

- 상위 토픽: [03-047 인덱스(클러스터드·논클러스터드)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/047_index_clustered_nonclustered.md)
- 연관 토픽: [03-027 트리·이진 탐색 트리](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/027_binary_search_tree.md), [03-052 다차원 색인구조](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/052_multidimensional_index_structure.md)
