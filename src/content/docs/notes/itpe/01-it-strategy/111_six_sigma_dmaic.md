---
title: "Six Sigma DMAIC"
author: "Claude Code"
date: "2026-09-29T22:52:04+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → 사업 품질·독립 점검 → **Six Sigma DMAIC**

## 30초 인출

- 본질: Six Sigma DMAIC는 기준에 못 미치는 기존 프로세스를 정의·측정·분석·개선·관리의 5단계로 데이터에 근거해 개선하는 문제 해결 방식
- 메커니즘: 문제와 목표를 정하고(Define) 실제 프로세스의 기준선을 측정해(Measure) 변동의 근본 원인을 찾은 뒤(Analyze) 해결안을 최적화하고(Improve) 개선 수준을 유지하는 관리 체계를 세움(Control)
- 통찰: 원인 분석과 개선 효과 판단이 모두 측정 단계의 기준선 데이터에 의존하므로, 기준선을 정하기 전에 측정 시스템 분석(MSA)으로 데이터의 신뢰성을 확인

<details>
<summary>핵심 용어</summary>

- **Six Sigma** : 프로세스의 변동과 결함을 줄여 고객 만족을 높이는 체계적 품질 개선 방법이며, 6시그마 수준 프로세스의 수치 목표는 100만 기회당 결함 3.4개
- **DMAIC** : Define·Measure·Analyze·Improve·Control의 5단계로 기존 프로세스를 개선하는 구조화된 문제 해결 방식
- **DMADV** : Define·Measure·Analyze·Design·Verify의 5단계로 신규 제품·서비스를 개발하거나 프로세스를 전면 재설계할 때 쓰는 방식
- **DPMO(Defects Per Million Opportunities)** : 100만 기회당 결함 수이며 시그마 수준의 기준 지표
- **SIPOC(Supplier, Inputs, Process, Output, Customer)** : 공급자·입력·프로세스·출력·고객으로 프로세스의 입출력 관계를 정리하는 모델
- **MSA(Measurement System Analysis)** : 측정 시스템의 반복성·재현성 등 능력을 평가하는 분석이며 GR&R(Gauge Repeatability and Reproducibility)이 대표 기법
- **SPC(Statistical Process Control)** : 관리도로 프로세스 변동을 감시해 이상 원인을 식별하는 통계적 공정 관리
- **프로젝트 헌장(Project charter)** : 프로젝트의 초점·범위·방향과 문제·목표 진술, 지표, 일정을 정한 문서
- **Champion·Black Belt·Green Belt** : 프로젝트 성공과 자원을 책임지는 경영진, 전업으로 프로젝트를 이끄는 리더, 프로젝트 팀원

</details>

---

## 2~4교시 예상문제 (25점)

> Six Sigma의 개념과 DMAIC 단계별 활동을 설명하고, DMAIC 적용 시 한계와 개선 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. Six Sigma DMAIC의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Six Sigma** 의 **DMAIC** 는 기존 프로세스의 변동과 결함을 5단계로 줄이는 데이터 기반 개선 방법 |
| 목적 | 프로세스 변동 감소를 통한 결함 감소와 고객 만족 향상 |

## Ⅱ. 기준선 데이터에 의존하는 DMAIC의 특징

| 특징 | 의미 |
|---|---|
| 데이터 기반 | 사실과 통계 방법에 근거해 고객이 정의한 결함률을 줄임 |
| 결함 예방 중시 | 결함 발견보다 결함 예방을 중시 |
| 수치 목표 | 6시그마 수준 프로세스는 100만 기회당 결함 3.4개 |
| 프로젝트 단위 | Champion·Black Belt·Green Belt로 구성한 팀이 조직 성과에 직결되는 프로젝트 수행 |
| 기존 프로세스 대상 | 성과 기준에 못 미치는 기존 프로세스의 점진적 개선 |

## Ⅲ. DMAIC의 5단계 체계

### 5단계 개선 절차

```text
Define   문제·목표·고객 요구 정의, 프로젝트 헌장, 이해관계자 분석, 입출력 정리(SIPOC), 팀 선정
    ↓
Measure  실제 프로세스 문서화, 측정 시스템 검증, 기준선 성과 설정
    ↓
Analyze  변동과 결함을 일으키는 핵심 입력과 근본 원인 식별
    ↓
Improve  해결안 평가·프로세스 최적화, 통제할 핵심 입력 결정
    ↓
Control  실수 방지·장기 측정·대응 계획, 표준 작업 절차, 프로세스 능력 확립
```

### Measure 확대: 기준선을 세우는 순서

```text
프로세스 맵 작성: 단계별 입력·출력 식별
    ↓
측정 시스템 분석(MSA): 반복성·재현성 평가 (GR&R)
    ↓
데이터 수집 계획에 따른 수집
    ↓
프로세스 능력 산출: 시그마 수준, 단기·장기 능력의 차이(시그마 이동)
    ↓
기준선 성과 확정 → Analyze로 전달
```

## Ⅳ. DMAIC와 DMADV의 비교

| 단계 | DMAIC (기존 프로세스의 점진적 개선) | DMADV (신규 개발·전면 재설계) |
|---|---|---|
| 1 | **Define** : 문제·목표·고객 정의 | **Define** : 신규 제품·서비스의 시장·고객 요구 결정 |
| 2 | **Measure** : 실제 프로세스 측정, 기준선 설정 | **Measure** : 고객의 소리(VOC) 수집, 사양 설정 |
| 3 | **Analyze** : 변동·결함의 근본 원인 식별 | **Analyze** : 요구를 충족하는 최선의 설계 개념 선택 |
| 4 | **Improve** : 해결안 평가와 프로세스 최적화 | **Design** : 상세 설계와 파일럿·시뮬레이션·프로토타입 입증 |
| 5 | **Control** : 실수 방지·장기 측정·대응 계획 | **Verify** : 설계 결과가 요구·사양을 충족하는지 시험·검증 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 검증되지 않은 측정 시스템으로 잡은 기준선 때문에 어긋나는 Analyze의 원인 판단과 Improve의 효과 확인 | Measure 단계에서 측정 시스템 분석(MSA)으로 측정 시스템을 검증한 뒤 기준선 설정 |
| 해결안의 전면 적용에 따른 예상하지 못한 부작용의 운영 반영 | Improve 단계에서 개념 검증(proof of concept)과 파일럿 테스트로 효과를 확인한 뒤 적용 |
| 개선 뒤 원래 수준으로 되돌아가는 성과 | Control 단계에서 관리 계획과 SPC로 개선 수준을 감시하고 표준 작업 절차에 반영 |
| 기존 프로세스의 기준선이 없는 신규 개발·전면 재설계 과제 | DMADV로 과제 성격에 맞는 방식 선택 |

## Ⅵ. 제언

DMAIC 프로젝트에서 기준선을 정하기 전에 측정 시스템 분석으로 데이터 신뢰성을 확인하는 관문 설정

### 기준선 관문

```text
Define: 문제·목표 확정
    ↓
Measure: 프로세스 맵 → 데이터 수집 계획
    ↓
[관문] 측정 시스템 검증
    ↓
기준선 설정
    ↓
Analyze → Improve → Control
```

### 관문 확대: 측정 시스템 판정

```text
반복성·재현성 평가(GR&R) 수행
    ├─ 측정 오차가 커서 결함 판정에 부적합 → 측정 방법 개선 후 재평가
    └─ 사용 가능
         ↓
데이터 수집 → 기준선 성과 확정
```

| 구분 | 측정 후 바로 기준선 설정 | 제언: 측정 시스템 검증 후 설정 |
|---|---|---|
| 기준선의 근거 | 측정값 그대로 | 검증된 측정 시스템의 측정값 |
| 측정 오차의 발견 시점 | Analyze·Improve 결과가 어긋난 뒤 | 기준선 설정 전 |
| 개선 효과 판단 | 측정 변동과 프로세스 변동이 섞임 | 프로세스 변동에 집중 |

## 출제 이력과 검증 출처

- Q-net 제132~140회 문제지에서 Six Sigma DMAIC를 직접 묻는 문항 없음
- ASQ, DMAIC Process: Define, Measure, Analyze, Improve, Control — DMAIC 5단계와 DMAIC·DMADV의 구분
- ASQ, What Is Six Sigma? — Six Sigma의 정의, 3.4 DPMO 수치 목표, 역할
- ASQ, Certified Six Sigma Green Belt Body of Knowledge(2022) — 단계별 주제(SIPOC, MSA, 시그마 이동, SPC, 파일럿 테스트)

## 연결 토픽

- 이전 토픽: [Programmable Money·AI Agent 결제](./110_programmable_money_ai_agents.md)
- 연관 토픽: [품질비용(COQ)](./106_cost_of_quality_coq.md), [PMO](./004_pmo.md)
- 다음 토픽: [CCPM·TOC](./112_critical_chain_toc.md)
