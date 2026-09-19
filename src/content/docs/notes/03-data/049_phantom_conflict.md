---
sidebar:
  order: 49
  label: "049. 팬텀 충돌 (Phantom Conflict)"
  badge:
    text: "기출 · 81%"
    variant: note
title: "팬텀 충돌 (Phantom Conflict)"
date: "2026-09-20T00:40:00+09:00"
tags:
  - "notes-data"
weight: 49
extra:
  question_no: "049"
  source_status: "기출"
  source_history: "135회, 98회"
  priority: 81
  priority_note: "[출제:135] · 이전(KPC):98"
---

## 답안 골격
```text
[팬텀 충돌] ◀━━ 머리: Ⅶ 내 의견 (갭 락(Gap Lock)과 Next-Key Lock 적용으로 범위 직렬성 보장 및 락 경합 완화)
 ┃
 ┣━ Ⅰ 개요 ───── 트랜잭션이 범위 검색(Range Scan) 후 다른 트랜잭션의 신규 INSERT로 인해 없던 레코드가 나타나는 동시성 충돌
 ┣━ Ⅱ 특징 ───── 행 락(Row Lock) 한계 노출 · 동적 집합 충돌 · 팬텀 리드(Phantom Read) 유발 · 직렬화 격리 요구
 ┣━ Ⅲ 구조 ───── 검색 조건(Predicates) / 기존 레코드 / 인접 간격(Gap) / 신규 삽입 튜플(Phantom Tuple)
 ┣━ Ⅳ 흐름 ───── ① T1이 조건 범위 레코드 조회(S-Lock) → ② T2가 해당 범위에 신규 튜플 INSERT 커밋 → ③ T1이 동일 조건 재조회 시 새 레코드 출현(충돌)
 ┣━ Ⅴ 비교 ───── Non-Repeatable Read vs Phantom Conflict (기존 행의 값 변경 vs 신규 행의 삽입/삭제)
 ┗━ Ⅵ 실무 ───── 수강 인원 제한(최대 30명) 초과 삽입 / 중복 예약 발생 / 일일 정산 합계 불일치
```
- 필수 키워드: 팬텀 리드(Phantom Read) · 갭 락(Gap Lock) · Next-Key Lock · 서술어 락(Predicate Lock) · Repeatable Read · 직렬성(Serializability)
- 배점 전략: 10점 = Ⅰ → Ⅳ 시간축 충돌 흐름도 → Ⅵ 해결 기법(갭 락, 인덱스 락) / 25점 = Ⅰ~Ⅶ, Ⅲ 충돌 메커니즘 및 Ⅴ 이상현상 비교
- 기출: 135회 1교시 11번 `팬텀충돌(Phantom Conflict)` → Ⅰ 개념 + Ⅳ 발생 메커니즘 + 해결방안

## 한 줄 본질
- 개별 행 락(Row-level Lock)은 아직 존재하지 않는 가상의 데이터 공간을 보호하지 못함 → 트랜잭션 도중 조건 범위 내 신규 데이터 삽입 발생 → 갭 락(Gap Lock) 또는 서술어 락으로 인접 빈 공간까지 잠가 방지 / 동시성 저하

## 핵심 그림
```text
[팬텀 충돌(Phantom Conflict) 발생 타임라인]

      트랜잭션 1 (T1)                      트랜잭션 2 (T2)
 ─────────────────────────            ─────────────────────────
 ① SELECT * FROM 계좌
    WHERE 잔액 >= 1000;
    (결과: A(1000), B(1500))
    * 개별 행 A, B에 S-Lock 획득
                                   ② INSERT INTO 계좌 VALUES (C, 1200);
                                      * C는 기존에 없던 행이므로
                                        T1의 행 락을 우회하여 성공!
                                   ③ COMMIT;
 ④ SELECT * FROM 계좌
    WHERE 잔액 >= 1000;
    (결과: A, B, C 출현! ───> [팬텀 충돌 발생: 유령 행 C 등장])
```

## 핵심 용어
- 갭 락(Gap Lock): 실제 레코드가 아닌 인덱스 레코드 사이의 빈 공간(Gap)에 거는 락으로, 타 트랜잭션의 신규 INSERT를 방지
- 넥스트 키 락(Next-Key Lock): 레코드 락(Record Lock)과 갭 락(Gap Lock)을 결합하여 현재 레코드와 바로 앞의 갭을 동시에 잠그는 InnoDB의 기본 락 방식

## 핵심 통찰
- 일반적인 2단계 락킹(2PL)에서 행(Row)만 잠그면 '아직 존재하지 않는 미래의 레코드'를 막을 수 없음 → 이것이 팬텀 충돌의 본질
- 서술어 락(Predicate Lock)은 이론적으로 완벽하지만 조건식 평가 비용이 너무 큼 → 실무 RDBMS(MySQL InnoDB 등)는 인덱스의 정렬 순서를 이용한 Next-Key Lock으로 실용적 해결
- 단순 MVCC(다중 버전 동시성 제어) 환경에서 스냅샷 읽기는 팬텀 리드를 막지만, `SELECT ... FOR UPDATE` 같은 락 기반 읽기나 직접 UPDATE 수행 시 여전히 팬텀 충돌이 발현될 수 있음

## 딸려 나오는 하위 토픽
| 하위 토픽 | 상위 구조 속 위치 | 한 줄 |
|---|---|---|
| 서술어 락(Predicate Lock) | 팬텀 충돌의 이론적 완벽 해결책 | WHERE 절의 검색 조건 자체를 잠가 해당 조건에 부합하는 모든 삽입·수정을 원천 차단 |
| 스냅샷 격리(Snapshot Isolation) | MVCC 기반 팬텀 완화 | 트랜잭션 시작 시점의 스냅샷 버전만 읽음으로써 일반 SELECT 시 팬텀 리드를 자동 은폐 |

## 이웃 토픽과 구분
- Non-Repeatable Read vs Phantom Conflict: Non-Repeatable Read = 이미 읽었던 기존 레코드의 값이 변경됨(행 락으로 방지 가능) / Phantom Conflict = 범위 조건 내에 없던 새로운 레코드가 불쑥 나타남(행 락으로 방지 불능, 갭 락 필요)

## 문제·원인·대책
- 적용 상황: 수강신청 시스템의 정원(30명) 통제
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 29명 신청 상태에서 두 사용자가 동시 신청 시 둘 다 성공하여 정원 초과(31명) | COUNT(*) 조회 시 기존 행 락만 걸려 새 신청 건의 동시 INSERT 방지 실패 | SELECT ... FOR UPDATE에 의한 Next-Key Lock 적용 또는 테이블 집계 행 배타적 락 | 정원 초과 원천 방지 |
| 대량 배치 INSERT 중 웹 애플리케이션의 단건 조회가 락 대기로 타임아웃 | Next-Key Lock이 필요 이상으로 넓은 인덱스 갭을 잠금 | 격리 수준을 Read Committed로 낮추고 MVCC 적극 활용 | 락 경합 완화 및 처리량 증대 |

## 이렇게 출제된다
- 제135회 1교시 11번: "팬텀충돌(Phantom Conflict)" → 요구 포인트: 개념 정의 + 타임라인 기반 발생 메커니즘 + 방지 기법(서술어 락, Next-Key Lock, 격리 수준)

## 내 의견
- [격리 수준에 대한 맹신과 동시성 버그] 개발자가 MySQL의 Repeatable Read 격리 수준만 믿고 락 없는 비즈니스 검증 로직을 구현하여 팬텀 충돌 기반 정원 초과 버그 양산 → 나라면: 정원·재고처럼 엄격한 카디널리티 제약이 필요한 구간은 낙관적 락(버전)이나 Redis 원자적 분산 락(Redlock)을 애플리케이션 진입점에 전진 배치

## 찾아볼 것
- MySQL InnoDB의 `innodb_locks_unsafe_for_binlog` 옵션과 갭 락 비활성화 시의 부작용
