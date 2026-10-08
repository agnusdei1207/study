---
title: "CAP·PACELC 정리 (CAP: Consistency, Availability, Partition Tolerance; PACELC: Partition: Availability/Consistency; Else: Latency/Consistency)"
author: "Codex"
date: "2026-10-08T15:46:11+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GPT-6"
---

## Ⅰ. CAP·PACELC의 개요

- **CAP**(Consistency, Availability, Partition Tolerance) 정리는 네트워크 분할이 발생한 분산 시스템에서 강한 일관성과 모든 정상 노드의 요청 가용성을 동시에 보장할 수 없다는 한계.
- **PACELC**(Partition: Availability/Consistency; Else: Latency/Consistency)는 분할 시 가용성·일관성의 선택뿐 아니라 평상시 지연시간·일관성의 절충을 설명하는 분석 틀.
- CAP를 항상 세 속성 중 정확히 두 개를 고르는 규칙으로 해석하지 않도록 구분. 분할이 없는 구간에서는 일관성과 가용성을 함께 제공할 수 있음.

## Ⅱ. 속성의 정확한 의미

| 속성 | 의미 | 실무 해석 |
|---|---|---|
| 일관성(C) | 연산이 단일 최신 복사본에서 원자적으로 실행된 것처럼 보이는 선형화 가능성 | 모든 복제본의 물리적 값이 매순간 같아야 한다는 뜻은 아님 |
| 가용성(A) | 장애가 없는 노드가 받은 요청이 응답으로 완료 | 운영 지표의 가동률과 다른 이론적 정의 |
| 분할 내성(P) | 통신 메시지 손실·단절 상황을 모델에 포함 | 모든 기능을 무조건 정상 제공한다는 뜻은 아님 |

```text
통신 분할 발생 → C 유지: 일부 요청 대기·거부 가능
              → A 유지: 서로 다른 값·오래된 값 허용 가능
분할 없는 평시 → 복제·합의로 얻는 일관성과 지연의 절충
```

## Ⅲ. 제품보다 연산·설정 중심의 분류

| 구성 예시 | 확인할 사항 | 분할 시 영향 |
|---|---|---|
| 합의·쿼럼 기반 쓰기 | 필요한 투표·복제본 수, 커밋 조건 | 쿼럼에 도달하지 못하면 쓰기 진행 제한 |
| 비동기 복제와 로컬 읽기 | 허용 지연, 충돌 해결, 읽기 범위 | 오래된 값 또는 동시 변경 가능 |
| MongoDB 복제 집합 | primary 선출, read concern, write concern | 다수 투표 노드에 도달할 수 없는 측에서는 다수 확인 쓰기 불가 |
| Cassandra | 연산별 consistency level, 복제 계수 | 지정한 응답 수에 도달하지 못하면 연산 실패 가능 |
| DynamoDB | 테이블·인덱스·리전 구성과 읽기 모드 | 글로벌 구성과 일관성 모드에 따라 보장 차이 |

- 특정 데이터베이스를 모든 설정과 연산에서 고정된 AP·CP 또는 PA/EC 제품으로 단정하지 않도록 구분.
- 읽기 쿼럼 $R$과 쓰기 쿼럼 $W$의 교집합 조건 $R+W>N$만으로 동시 쓰기·버전 충돌 등을 포함한 선형화 가능성이 자동 보장되지 않음.
- 참고 : [Gilbert·Lynch의 CAP 증명](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf), [Abadi의 PACELC 논문](https://doi.org/10.1109/MC.2012.33), [MongoDB 복제 집합](https://www.mongodb.com/docs/manual/replication/), [Cassandra 일관성 설정](https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html), [DynamoDB 읽기 일관성](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html).

## Ⅳ. CAP·PACELC 적용의 한계점 및 해결 방안

- 제품 단위의 단순 분류 : 실제 읽기·쓰기 경로와 장애 조건을 나누어 보장 수준 확인.
- 최종 일관성의 업무 오류 : 잔액·재고·중복 결제처럼 정합성이 필요한 연산에는 적절한 직렬화·합의·멱등성 설계.
- 평상시 성능과 장애 시 동작의 차이 : 정상 부하 시험과 네트워크 분할 시험을 함께 수행하고 데이터 복구·충돌 처리도 검증.

## Ⅴ. 분산 데이터 설계를 위한 제언

- 서비스마다 허용 가능한 데이터 지연, 거부 가능한 요청 및 장애 복구 정책을 명시하고 복제·합의 설정에 반영.
- 이론적 분류를 제품 선택의 참고 틀로 활용하고 실제 보장 여부는 설정·연산·장애 시험 결과로 확인.
