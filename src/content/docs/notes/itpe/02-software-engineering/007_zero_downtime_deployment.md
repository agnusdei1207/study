---
title: "무중단 배포·배포 전략"
author: "OpenAI Codex"
date: "2026-09-20T00:25:00+09:00"
tags: ["notes-software-engineering"]
sidebar:
  badge:
    text: "A"
extra:
  model: "OpenAI Codex"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="소프트웨어 전달에서 무중단 배포까지의 지식 경로"><span>SW 공학·DevOps</span><span>릴리스·배포</span><strong>무중단 배포</strong></div>

## 큰 그림과 30초 인출

```text
User → LB/Service → [V1] [V1] [V2] [V2]
                        │ traffic shift │
Build → Test → Deploy → Health/SLO → Promote or Rollback
                        └─ DB: Expand → Migrate → Contract
```

```text
무중단 = 신·구 버전 동시 수용 + 트래픽 제어 + 상태 호환
전략 = Rolling·Blue/Green·Canary
판정 = Readiness + SLO + 오류/지연 + 자동 중단·복원
핵심 = 애플리케이션만이 아니라 DB·메시지·세션 호환성
```

## 예상문제

> 무중단 배포의 개념과 구성, Rolling·Blue/Green·Canary 전략을 비교하고 데이터베이스 변경을 포함한 수행 절차와 고려사항을 설명하시오.

## Ⅰ. 개요 ───── 서비스 연속성을 지키는 버전 전환

무중단 배포는 서비스를 중지하지 않고 신·구 버전을 일정 기간 병행하며 트래픽을 제어해 신규 버전으로 전환하는 배포 방식이다. 핵심은 인스턴스 교체가 아니라 요청·상태·데이터 계약의 연속성이다.

## Ⅱ. 특징 ───── 병행·점진·가역·관측

| 특징 | 의미 | 구현 |
|---|---|---|
| 병행성 | 신·구 버전 동시 실행 | 복수 인스턴스·환경 |
| 점진성 | 일부부터 트래픽 전환 | Weight·Segment |
| 가역성 | 이상 시 이전 버전 복귀 | Immutable Artifact·Rollback |
| 관측성 | 전환 판단의 증거 | 오류·지연·포화·업무 KPI |
| 호환성 | 양 버전이 상태를 함께 사용 | API·Schema 하위 호환 |

## Ⅲ. 구조 ───── 전달·실행·데이터·판정 계층

```text
[CI: Build/Test/Scan] → [Artifact Registry]
                              │
                              ▼
[CD Controller] → [V1 Pool] [V2 Pool] ← [LB/Service Mesh] ← User
                       │        │
                       └── [DB·Cache·Queue] ──┘
                              │
                    [Metric·Log·Trace·SLO]
                              └→ Promote / Abort / Rollback
```

## Ⅳ. 절차 ───── 사전 호환부터 정리까지

```text
① 불변 아티팩트·복원 기준 확정
 → ② DB Expand로 양 버전 호환 스키마 배포
 → ③ V2 배치, Readiness·Smoke Test
 → ④ 전략별 트래픽 전환
 → ⑤ 기술 SLI와 업무 KPI 관찰
 → ⑥ 승격 또는 중단·롤백
 → ⑦ 데이터 이관 후 구 필드·V1 Contract
```

## Ⅴ. 비교 ───── Rolling·Blue/Green·Canary

| 기준 | Rolling | Blue/Green | Canary |
|---|---|---|---|
| 전환 | 인스턴스 순차 교체 | 두 환경 간 일괄 전환 | 일부 사용자·비율부터 확대 |
| 추가 자원 | 비교적 적음 | 두 환경 필요 | 신·구 병행 규모에 따름 |
| 위험 노출 | 교체 중 혼재 | 전환 시 전체 영향 가능 | 제한된 범위 |
| 복원 | 역 Rolling | 라우팅 복귀 | 가중치 0·중단 |
| 적합 | 표준 서비스 갱신 | 빠른 전환·환경 검증 | 위험 높은 변경·실험 |
| 유의 | 버전 혼재 호환 | DB는 공유될 수 있음 | 대표성·통계적 판정 |

## Ⅵ. 고려 ───── 반쪽짜리 무중단 방지

| 문제 | 원인 | 대응 | 검증 |
|---|---|---|---|
| DB 롤백 불가 | 파괴적 DDL 선행 | Expand-Migrate-Contract | 양 버전 CRUD |
| 세션 단절 | 인스턴스 로컬 상태 | 외부화·호환 Serialization | 전환 중 세션 |
| 메시지 오류 | Event Schema 비호환 | Versioning·Tolerant Reader | 소비자 계약 |
| 잘못된 승격 | 단일 평균 지표 | 오류·지연 분포·KPI·Guardrail | 자동 분석 |
| 복원 실패 | 코드만 롤백 | 데이터·설정·Feature Flag 계획 | 정기 Drill |
| 장기 혼재 | 종료 조건 부재 | 소유자·기한·정리 체크 | 구 버전 제거 |

## Ⅶ. 결론 ───── 트래픽보다 계약의 무중단

무중단 배포는 라우팅 기법만으로 달성되지 않는다. 신·구 버전의 API·DB·이벤트·세션 계약을 호환시키고 관측 지표에 따라 승격과 복원을 자동화해야 서비스 연속성과 변경 안전성을 함께 확보할 수 있다.

## 1교시 10점 발췌

```text
무중단 배포 = 신·구 버전을 병행하고 트래픽을 제어해 서비스 중단 없이 전환
전략: Rolling(순차) / Blue-Green(환경 전환) / Canary(점진 노출)
구조: CI→Artifact→CD→V1/V2→LB + DB/Queue + Observability
핵심: Expand-Migrate-Contract, Readiness, SLO, Rollback
```

## 공식 근거

- [Kubernetes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Argo Rollouts Concepts](https://argo-rollouts.readthedocs.io/en/stable/concepts/)
- Q-Net 제139회 정보관리기술사 1교시 5번, 제134회 3교시 1번

## 체크

- [ ] 세 전략을 전환·자원·위험·복원으로 비교했는가
- [ ] DB Expand-Migrate-Contract를 그렸는가
- [ ] 상태·메시지·관측과 롤백을 포함했는가
- [ ] 무중단을 무장애와 동일시하지 않았는가

## 연결 토픽

- [DevOps](./002_devops/)
- [CI/CD](./095_ci_cd/)
- [회귀 테스트](./061_regression_test/)
