---
title: "메인 메모리 DBMS(MMDBMS, Main Memory Database Management System) (DBMS: Database Management System)"
author: "agnusdei1207"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Antigravity Professional Engine"
---

## 연관 키워드

**MMDBMS(Main Memory DBMS)**, **T-Tree**, **직접 포인터(Direct Pointer)**, **WAL**, **체크포인팅**, **NVRAM**, **Tiered Storage**

## Ⅰ. 개요

- 핵심 요약 : **MMDBMS**는 데이터를 RAM에 상주시켜 디스크 I/O 없이 마이크로초 단위 초고속 처리하는 DBMS.
- 목적 : 디스크 I/O 병목 근원적 극복.
- 배경 : 디스크 기반 DBMS의 버퍼 관리·I/O 오버헤드 한계.
- 특징 : 직접 포인터, T-Tree, WAL, 체크포인팅, NVRAM.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **직접 포인터·T-Tree·WAL**로 I/O 없는 초고속 처리.
- **직접 포인터** : ROWID 변환 없이 64비트 주소 직접 참조 (O(1)).
- **T-Tree** : AVL 균형 + B-Tree 밀집도 결합.
- **WAL** : Redo 로그 디스크 순차 기록.
- **체크포인팅** : 백그라운드 스냅샷.
- **NVRAM** : 정전 시 플래시 백업.

## Ⅲ. 아키텍처 흐름

- 핵심 요약 : **RAM 상주 + WAL/체크포인트 영속성**.
- DRDBMS vs MMDBMS : 버퍼 풀 → 직접 메모리 포인터.

```text
[ DRDBMS vs MMDBMS ]

DRDBMS : App -> Buffer Pool -> (Cache Miss) Disk I/O
MMDBMS : App -> RAM 직접 포인터 접근
         (비동기 WAL + 주기적 체크포인트만 디스크)
```

```text
[ T-Tree 노드 ]

[부모/자식 포인터]
[최소키 | 키1..키N | 최대키]
- AVL 균형 + B-Tree 밀집도
```

## Ⅳ. DRDBMS vs MMDBMS 비교

- 핵심 요약 : **I/O·버퍼·인덱스·영속성** 비교.

| 항목 | DRDBMS | MMDBMS |
|---|---|---|
| 데이터 위치 | 디스크 + 버퍼 풀 | RAM 상주 |
| 인덱스 | ROWID → 디스크 변환 | 직접 메모리 포인터 |
| 버퍼 관리 | 복잡 (이중 페이징) | 불필요 |
| 영속성 | 디스크 직접 | WAL + 체크포인트 + NVRAM |
| 지연 | ms | µs |

## Ⅴ. 한계와 방안

- 핵심 요약 : **휘발성·용량·NUMA**를 NVRAM·티어링·NUMA-aware로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 휘발성 유실 | 정전 시 메모리 소실, 긴 복구 | NVDIMM, CXL 영속 메모리, 체크포인트 최적화 | MTTR |
| 용량·비용 | DRAM 고비용, OOM 크래시 | Tiered Storage (핫/콜드), 압축 | 메모리 사용률 |
| NUMA 병목 | 원격 메모리 접근 레이턴시 | NUMA-aware 할당, 스레드 바인딩, 캐시 인지 자료구조 | 캐시 미스율 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **하이브리드 티어링·캐시 미스 최적화**.
- 핫 데이터 MMDBMS, 콜드 데이터 디스크 RDBMS/Lakehouse.
- 벡터화 실행(SIMD) + 메모리 정렬.

## Ⅶ. 결론

- 핵심 요약 : MMDBMS는 **RAM 상주 + WAL/체크포인트**로 초고속 처리, 휘발성·용량·NUMA가 핵심 과제.
- 답안에는 직접 포인터, T-Tree, 영속성 3기술, 한계·대응을 연결.
- 참고 : [Redis](https://redis.io/).