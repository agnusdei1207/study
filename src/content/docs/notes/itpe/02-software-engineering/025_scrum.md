---
title: "스크럼(Scrum)"
description: "3-5-3 체계, 스프린트 흐름, DEEP·INVEST·DoD, 지표 오용·PO 병목·행사 형식화 한계와 방안"
tags:
  - "notes-software-engineering"
  - "notes-itpe"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
---

## 연관 키워드
- Scrum, Product Owner, Scrum Master, Developers, Sprint, Product Backlog, Increment, Definition of Done

## Ⅰ. Scrum의 개요
- 핵심 요약 : Scrum은 복잡한 제품 개발을 짧은 Sprint와 경험적 통제로 수행하는 경량 프레임워크.
- 개념 : 투명성·점검·적응의 경험주의와 용기·집중·헌신·존중·개방성의 가치를 바탕으로 제품가치를 반복 전달.
- 필요성 : 요구·기술 불확실성이 큰 상황에서 장기 계획만으로 결과를 예측하기 어려움.
- 목적 : 작동 가능한 Increment를 자주 확인해 제품 목표와 계획을 적응적으로 관리.

## Ⅱ. Scrum의 특징 및 장점
- 핵심 요약 : 세 가지 accountabilities, 다섯 이벤트, 세 산출물과 산출물별 약속이 피드백 구조를 형성.
1. 경험적 통제 : 투명성·점검·적응 → 변화·위험 조기 발견.
2. 자기관리 팀 : Product Owner·Scrum Master·Developers가 책임을 분담 → 의사결정 지연 완화.
3. 고정 길이 Sprint : 매 Sprint에서 Done Increment 생성 → 점진적 검증과 예측 가능성 향상.
- 주의 : DEEP는 Product Backlog 관리 특성의 실무 가이드, INVEST는 사용자 스토리 품질 점검 휴리스틱으로 Scrum Guide의 필수 산출물·규칙과 구분.

## Ⅲ. Scrum의 운영 흐름
- 핵심 요약 : Sprint Planning에서 목표와 작업을 정하고 Daily Scrum·실행을 거쳐 Review와 Retrospective로 적응.
```text
Product Goal → Product Backlog → Sprint Planning
       → Sprint(Developers 작업·Daily Scrum)
       → Done Increment → Sprint Review → Retrospective → 다음 Sprint
```
```text
산출물             약속
Product Backlog → Product Goal
Sprint Backlog  → Sprint Goal
Increment       → Definition of Done
```
- 이벤트 : Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.

## Ⅳ. Scrum과 Kanban 비교
- 핵심 요약 : Scrum은 고정 길이 Sprint·역할·산출물 약속, Kanban은 흐름·진행작업 제한·지속적 전달을 중심으로 운영.
| 기준 | Scrum | Kanban |
|---|---|---|
| 작업주기 | 고정된 Sprint | 연속 흐름, 필요시 전달 |
| 관리 초점 | Sprint Goal·Increment·이벤트 | 작업 시각화·WIP 제한·흐름 최적화 |
| 역할·책임 | 정의된 세 accountabilities | 특정 역할을 필수 규정하지 않음 |
| 적합 상황 | 정기 점검·제품목표 기반 반복개발 | 운영·지원의 변동 작업흐름 |

## Ⅴ. Scrum의 한계와 대응
- 핵심 요약 : 이벤트 형식화·PO 병목·속도지표 오용은 경험주의를 훼손하므로 제품권한과 팀 학습을 강화.
| 한계 | 영향 | 대응 |
|---|---|---|
| 행사만 준수 | 점검·적응 없는 의례화 | 이벤트별 목적·결정·후속조치 확인 |
| PO 의사결정 병목 | 백로그 우선순위·피드백 지연 | 제품목표·권한·대리의사결정 원칙 명확화 |
| Velocity 비교·목표화 | 추정치 게임과 품질 저하 | 팀 내부 계획 보조로만 사용, 가치·품질 측정 |

## Ⅵ. Scrum 도입 제언
- 핵심 요약 : 제품 책임자는 Product Goal과 권한을 보장하고 팀은 Done 기준·품질과 사용자 결과를 함께 관리.
1. 경영진은 제품팀의 우선순위·사용자 접근·배포권한을 보호하고 외부 의존성을 제거.
2. Scrum Master는 이벤트가 학습·장애물 제거로 이어지는지 점검하고 팀 자율성을 촉진.
3. Product Owner는 백로그를 가치·위험·학습 순으로 정렬하고 이해관계자와 결과를 검증.

## Ⅶ. 결론
- 핵심 요약 : Scrum은 복잡한 제품 문제를 짧은 주기로 검증·적응하는 프레임워크.
- 시사점 : 프레임워크의 효과는 역할·이벤트 준수보다 Done 결과와 실제 제품가치에 달림.
