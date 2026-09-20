---
sidebar:
  order: 13
  label: "013. 무결성 제약"
  badge: { text: "A", variant: note }
title: "무결성 제약 (Integrity Constraint)"
author: "OpenAI Codex"
date: "2026-09-20T00:25:00+09:00"
tags: ["notes-data"]
weight: 13
extra: { model: "GPT-5", keyword_grade: "A", question_no: "013" }
---

## 지식 로드맵 내 현재 위치
```text
데이터 관리 → 관계형 데이터 모델 → 무결성 제약
```

## 큰 그림과 30초 인출
```text
[도메인] 값 범위  [키] 유일성  [개체] PK NULL 금지  [참조] FK 일치
      └────────────── DBMS 선언적 제약 ───────────────┘
                  입력·수정·삭제 시 즉시 검증
```
- 본질: **데이터가 업무규칙과 릴레이션 관계를 항상 만족하도록 DBMS가 강제하는 조건**
- 암기: `도-키-개-참` = 도메인·키·개체·참조 무결성

## 예상문제
> 릴레이션 무결성 제약의 유형과 구현 방법을 설명하고 참조 무결성의 변경·삭제 정책을 논하시오. (25점)

## Ⅰ. 데이터 신뢰성의 최소 규칙, 무결성 제약 개요
- 정의: 저장·변경되는 데이터가 정의된 값 범위, 식별성, 관계 규칙을 위반하지 않도록 하는 선언적 조건
- 목적: 오류를 응용마다 사후 보정하지 않고 데이터 계층에서 일관되게 차단
- 구현: 데이터 타입·NOT NULL·CHECK·UNIQUE·PRIMARY KEY·FOREIGN KEY

## Ⅱ. 무결성 제약의 원칙과 계층
| 원칙 | 내용 | 효과 |
|---|---|---|
| 선언성 | 규칙을 스키마에 명시 | 응용 간 동일 규칙 |
| 원자성 | 위반 문장을 거부·롤백 | 부분 반영 방지 |
| 최소성 | 핵심 불변조건은 DB, 복잡 절차는 서비스 | 책임 명확화 |
| 추적성 | 논리 모델 규칙과 DDL 연결 | 변경 영향 분석 |

## Ⅲ. 4대 무결성 제약
| 유형 | 규칙 | 구현 예 |
|---|---|---|
| **도메인** | 속성값은 타입·범위·형식 만족 | TYPE, CHECK, NOT NULL |
| **키** | 후보키 값은 유일 | UNIQUE |
| **개체** | 기본키는 유일하고 NULL 불가 | PRIMARY KEY |
| **참조** | 외래키는 부모키 또는 NULL | FOREIGN KEY |

```sql
CREATE TABLE orders (
  order_id BIGINT PRIMARY KEY,
  customer_id BIGINT NOT NULL REFERENCES customer(customer_id),
  amount NUMERIC CHECK (amount >= 0),
  status VARCHAR(10) CHECK (status IN ('NEW','PAID','DONE'))
);
```

## Ⅳ. 제약 설계·적용 절차
```text
업무규칙 식별 → 엔터티·속성·관계 모델링 → 제약 유형 매핑
 → 기존 데이터 정제 → DDL 적용 → 위반·동시성·성능 시험 → 변경관리
```
- 기존 데이터가 규칙을 위반하면 정제·격리 후 제약을 활성화
- 제약명과 오류 메시지를 표준화해 운영 원인 추적성 확보

## Ⅴ. 참조 동작 정책 비교
| 정책 | 부모 변경·삭제 시 동작 | 적용 판단 |
|---|---|---|
| RESTRICT/NO ACTION | 참조가 있으면 거부 | 원장·핵심 마스터 |
| CASCADE | 자식도 연쇄 변경·삭제 | 강한 생명주기 종속 |
| SET NULL | 외래키를 NULL로 | 선택 관계·이력 보존 |
| SET DEFAULT | 기본값으로 변경 | 명시적 미분류 값 존재 시 |

## Ⅵ. 실무 고려사항
| 문제 | 원인 | 대책 |
|---|---|---|
| 고아 데이터 | FK 미정의·우회 적재 | FK와 적재 순서·격리영역 |
| 연쇄삭제 피해 | CASCADE 범위 미검토 | 영향 건수 확인·Soft Delete |
| 응용-DB 규칙 불일치 | 검증 로직 중복 | 불변조건은 DB를 기준선으로 관리 |
| 대량적재 지연 | 행별 제약·색인 비용 | Stage 적재 후 검증, 배치 전략 |

## Ⅶ. 모델의 불변조건을 데이터 계층에 고정하는 결론
- 핵심 무결성은 문서가 아니라 실행 가능한 스키마 제약으로 구현해야 함
- 참조 정책은 편의보다 데이터 생명주기·감사·복구 요구로 선택

## 1교시 10점 답안 발췌
```text
도메인 → 값 범위 / 키 → 유일성 / 개체 → PK NOT NULL / 참조 → FK 일치
업무규칙 → 모델 → DDL → 정제·적용 → 위반·성능 검증
```

## 출제 이력과 검증 출처
- 제135회 공식 문제지: 릴레이션 무결성 제약의 유형·사례·구현 관련 출제
- 제138회 공식 문제지: 정보모델링의 참조 무결성 관련 출제
- [PostgreSQL Documentation, Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
- [Q-Net 기술사 자료실](https://www.q-net.or.kr/man001.do?gSite=Q)

## 학습 체크
- [ ] 도메인·키·개체·참조 무결성을 구분함
- [ ] PK·FK·CHECK DDL 예시를 씀
- [ ] 참조 동작 4종을 비교함
- [ ] 기존 데이터 정제와 성능을 언급함

## 연결 토픽
- [정규화](./019_normalization/) · [반정규화](./017_denormalization/) · [트랜잭션 격리 수준](./020_isolation_level/)
