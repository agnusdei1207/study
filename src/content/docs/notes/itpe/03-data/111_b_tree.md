---
title: "B-Tree·B+Tree"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 데이터베이스 스토리지 엔진의 절대 표준, B-Tree와 B+Tree 개요

### 가. B-Tree·B+Tree의 정의
- **B-Tree (Balanced Tree)** : 디스크 블록(Block / Page) I/O 횟수를 최소화하기 위해 하나의 노드가 여러 개의 키와 자식 포인터를 가질 수 있도록 **다원화** (Multi-way)된 자가 균형 탐색 트리.
- **B+Tree** : B-Tree를 개량하여 모든 실제 데이터 포인터를 **리프 노드** (Leaf Node)에만 저장 하고, 리프 노드들을 **양방향 연결 리스트** 로 연결하여 범위 검색(Range Scan) 성능을 극대화한 현대 관계형 DBMS 인덱스의 표준 자료구조.

### 나. 이진 탐색 트리(BST) 대비 B-Tree의 우수성
- 메모리 참조는 $O(\log_2 n)$ 높이여도 상관없으나, 디스크 I/O는 1회 접근당 수 밀리초가 소요됨.
- B-Tree는 노드 크기를 OS 디스크 블록 크기(4KB~16KB)와 일치시켜 **차수** (M)를 수백 개로 확장함으로써, 수천만 건의 데이터도 트리 높이(Height)를 3~4 이내로 유지($O(\log_M n)$) 하여 디스크 I/O를 극소화함.

---

## Ⅱ. B-Tree vs B+Tree 심층 비교 분석

### 가. 두 자료구조의 내부 아키텍처 비교

```text
[ B-Tree vs B+Tree 구조 비교 ]
(A) B-Tree
    [Root Node (Key 10, DataPtr) (Key 20, DataPtr)]
               /                     \
    [Leaf: Key 5, DataPtr]     [Leaf: Key 15, DataPtr]
    * 루트와 브랜치 노드에도 키와 함께 실제 데이터 레코드 포인터가 저장됨

(B) B+Tree (현대 DBMS 표준)
    [Root Node (Key 10) (Key 20)]  <--- 내부 노드는 오직 라우팅 키(인덱스)만 저장!
               /                     \
    [Leaf: Key 5, DataPtr] <===> [Leaf: Key 15, DataPtr] <===> [Leaf: Key 25, DataPtr]
    * 모든 데이터 포인터는 리프 노드에만 존재하며, 리프 간 양방향 순차 링크(Linked List)로 연결됨
```

### 나. B-Tree vs B+Tree 핵심 기술 비교

| 비교 항목 | B-Tree | B+Tree |
| :--- | :--- | :--- |
| **데이터 포인터 저장 위치** | 모든 노드(루트, 브랜치, 리프)에 키와 데이터 포인터 분산 저장 | 오직 최하위 리프 노드(Leaf Node)에만 데이터 포인터 저장 |
| **내부 노드(Branch) 용량** | 데이터 포인터로 인해 하나의 노드에 담을 수 있는 키 개수가 적음 | 오직 키만 저장하므로 한 페이지에 훨씬 더 많은 키를 수용 (차수 M 극대화) |
| **트리 높이 (Height)** | 상대적으로 약간 높음 | 트리 높이가 더 낮아짐 (디스크 I/O 횟수 감소) |
| **범위 검색 (Range Scan)** | 범위 탐색 시 매번 중위 순회(In-order Traversal)로 부모 노드를 재방문 | 리프 노드의 연결 리스트를 순차 선형 스캔 하므로 압도적 고속 |
| **단건 검색 속도 (Point)** | 루트나 브랜치에서 일치하는 키를 바로 찾으면 리프까지 안 가고 즉시 종료 | 무조건 최하위 리프 노드까지 도달해야 검색 완료 (균일한 응답 시간) |

---

## Ⅲ. B+Tree의 노드 분할(Split) 및 병합(Merge) 알고리즘

### 가. 노드 분할 (Node Split - 상향식 확장)
- 리프 노드가 허용된 최대 키 개수($M-1$)를 초과하여 가득 차면, **중간값** (Median Key)을 부모 노드로 **승격** (Promote) 시키고 노드를 좌우 2개로 분할.
- 루트 노드가 분할될 때만 트리의 높이가 1 증가하므로, 트리는 항상 완벽한 균형(Balanced)을 유지함.

### 나. 노드 병합 (Node Merge - 하향식 축소)
- 삭제 연산으로 인해 노드의 키 개수가 최소 기준($\lceil M/2 \rceil - 1$) 미만으로 떨어지면, 인접 형제 노드로부터 키를 **빌려오거나** (Borrow) 형제 노드와 단일 노드로 병합.

---

## Ⅳ. B-Tree·B+Tree 인덱스의 주요 한계점 및 해결 방안

- **랜덤 쓰기** (Random Write) 집중에 따른 디스크 I/O 증폭 및 페이지 분할 :
  - 한계점 : 순차적이지 않은 무작위 키(UUID 등) 삽입 시 빈번한 노드 분할(Page Split)과 재균형 연산이 발생하여 내부 단편화 및 쓰기 성능 급락.
  - 해결 방안 : **단조 증가 키** (Auto Increment, TSID, ULID) 설계 채택, 쓰기 집약적 워크로드에는 **LSM-Tree** (RocksDB 등) 스토리지 엔진 검토.
- 고동시성 멀티스레드 환경에서 루트 노드 및 상위 인덱스 페이지의 래치 경합 :
  - 한계점 : 모든 인덱스 탐색이 루트 노드를 거치므로 다수 트랜잭션이 동시 진입 시 페이지 래치(Page Latch) 락 경합으로 인한 CPU 스핀락(Spinlock) 오버헤드 폭증.
  - 해결 방안 : 락 프리(Lock-free) 기법(B-link Tree 아키텍처, OLFIT: Optimistic Lock-Free Indexing), 캐시 라인 친화적 하드웨어 최적화 인덱스 적용.
- 인덱스 비대화에 따른 **버퍼 풀** 메모리 점유율 과다 및 캐시 미스 :
  - 한계점 : 테이블 크기 증가와 함께 B+Tree의 깊이(Height)와 리프 노드 수가 비대해져 버퍼 캐시 적중률(Hit Ratio)이 저하되고 물리적 디스크 읽기 증가.
  - 해결 방안 : 접두사 압축(Prefix Compression), 부분 인덱스(Partial/Filtered Index) 생성, 불필요한 보조 인덱스 정기 정리.

## Ⅴ. 고성능 인덱스 운용을 위한 실무 제언

- 순차 **증가 기본키** (Auto-Increment) 사용의 우월성 : B+Tree 인덱스는 정렬 상태를 유지하므로, UUID 등 무작위 난수 키를 PK로 사용하면 데이터가 리프 노드의 중간에 무작위로 끼어들어 빈번한 **페이지 분할** (Page Split)과 I/O 병목이 발생함. 따라서 대용량 OLTP 테이블은 반드시 순차 증가 시퀀스나 타임스탬프 기반 키(TSID, ULID)를 PK로 채택해야 함.
- 인덱스 **클러스터링 팩터** (Clustering Factor) 관리 : 보조 인덱스의 성능은 물리적 데이터 페이지가 인덱스 정렬 순서와 얼마나 일치하는지를 나타내는 클러스터링 팩터에 의해 결정되므로, 대규모 갱신 후 파편화가 심한 테이블은 정기적으로 테이블 및 인덱스 재빌드(`REORGANIZE / REBUILD`)를 수행할 것을 제언함.
