---
title: "Six Sigma DMAIC"
author: "Claude Code"
date: "2026-09-28T16:00:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Opus 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → 품질경영·프로세스 개선 → **Six Sigma DMAIC**

## 30초 인출

- 본질: Six Sigma DMAIC는 기존 프로세스의 결함과 변동을 데이터로 원인을 검증해 줄이고 그 수준을 유지하는 5단계 개선 방법
- 메커니즘: 고객 요구를 CTQ로 정의(Define)하고 현 수준을 측정(Measure)한 뒤, 원인을 검증(Analyze)해 개선안을 시험(Improve)하고 관리도로 유지(Control)
- 통찰: 유지 책임이 없으면 개선 효과가 되돌아가므로 관리계획의 책임자 이관과 관리도 기반 유지 확인

<details>
<summary>핵심 용어</summary>

- **Six Sigma DMAIC** : 기존 프로세스의 결함·변동 원인을 데이터로 검증해 개선하고 유지하는 식스 시그마의 5단계 개선 방법
- **DMAIC(Define, Measure, Analyze, Improve, Control)** : 정의·측정·분석·개선·관리로 이어지는 기존 프로세스 개선 절차
- **DMADV(Define, Measure, Analyze, Design, Verify)** : 기존 프로세스로 목표를 달성할 수 없을 때 새 프로세스·제품을 설계·검증하는 식스 시그마 설계(DFSS) 절차. ASQ 블랙벨트 지식체계는 마지막 단계를 Validate로도 표기
- **VOC(Voice of Customer)** : 설문·인터뷰·불만 등으로 수집한 고객의 요구
- **CTQ(Critical to Quality)** : VOC에서 도출한, 측정 가능한 핵심 품질 특성과 허용 기준
- **DPMO(Defects Per Million Opportunities)** : 결함 발생 기회 100만 건당 결함 수. 식스 시그마 수준은 장기 3.4 DPMO가 관례
- **MSA(Measurement System Analysis)** : 측정값의 반복성·재현성 등 측정체계 오차를 검증하는 분석
- **SPC(Statistical Process Control)** : 관리도로 프로세스의 비정상 변동을 감시하는 통계적 공정관리
- **Control Plan(관리계획)** : 개선된 프로세스의 감시 지표·측정 주기·책임자·이탈 시 대응을 정한 문서

</details>

---

## 2~4교시 예상문제 (25점)

> Six Sigma DMAIC의 개념과 단계별 절차를 설명하고, 적용 시 한계와 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. Six Sigma DMAIC의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Six Sigma DMAIC** 는 기존 프로세스의 결함·변동 원인을 데이터로 검증해 개선하고 그 수준을 유지하는 5단계 개선 방법 |
| 목적 | 고객 핵심 품질 요구(CTQ)의 충족과 결함·변동 감소 |

## Ⅱ. 경험 기반 개선과 구별되는 DMAIC의 특징

| 특징 | 의미 |
|---|---|
| 고객 기준 출발 | **VOC** 를 측정 가능한 **CTQ** 로 바꾼 개선 목표 설정 |
| 측정 신뢰성 선확인 | **MSA** 로 측정체계를 확인한 뒤 현 수준 확정 |
| 원인 검증 후 개선 | 가설검정·실험으로 확인한 핵심 원인만 개선 대상 |
| 유지 단계 포함 | 개선 후 **SPC** 관리도 감시까지 과제 범위에 포함 |
| 통계적 목표 수준 | **DPMO** 로 결함 수준 비교. 3.4 DPMO는 1.5σ 평균 이동을 가정한 장기 관례 |

## Ⅲ. DMAIC 5단계 절차와 Analyze의 원인 검증

### DMAIC 5단계 절차

```text
Define ── 문제·CTQ·범위·목표 정의
    ↓
Measure ── 측정체계 검증(MSA)·현 수준 측정
    ↓
Analyze ── 원인 가설 수립·데이터로 검증
    ↓
Improve ── 개선안 설계·시범 적용·효과 확인
    ↓
Control ── 표준화·관리도 감시·이탈 대응
```

### Analyze 확대: 핵심 원인 검증 절차

```text
잠재 원인 도출 (특성요인도·파레토 분석)
    ↓
원인별 가설과 데이터 수집
    ↓
가설검정·회귀·실험으로 영향 확인
    ├─ 영향 확인 → 핵심 원인(Vital Few) 확정
    └─ 영향 없음 → 다음 원인 가설 검증
```

## Ⅳ. DMAIC·DMADV·Lean의 비교

| 구분 | DMAIC | **DMADV** | Lean |
|---|---|---|---|
| 대상 | 기존 프로세스 | 새 프로세스·제품 | 기존 프로세스의 흐름 |
| 적용 조건 | 결함·변동 원인이 불명확 | 기존 프로세스로 CTQ 달성 불가 | 대기·재작업 등 낭비가 뚜렷 |
| 마지막 단계 | Control: 개선 수준 유지 | Verify: 새 설계 검증 | 흐름 개선의 표준화 |
| 핵심 도구 | 가설검정·실험계획·SPC | 품질기능전개·설계 검증 | 가치흐름도·Kanban |

## Ⅴ. DMAIC 적용의 한계와 방안

| 한계 | 방안 |
|---|---|
| 원인 확인 없는 경험적 해결책 적용으로 결함 재발 | Analyze의 가설검정으로 원인을 확인한 뒤 개선안 선택 |
| 측정 오차로 현 수준과 개선 효과 왜곡 | MSA로 측정체계를 검증한 뒤 기준선 확정 |
| 기존 프로세스 개선만으로 CTQ 달성 불가 | 해당 과제의 DMAIC 대신 DMADV 재설계 선택 |
| 원인이 분명한 대기·낭비 문제의 과도한 통계 분석 | 흐름 문제에는 Lean 기법 우선 선택 |
| 과제팀 해산 후 관리 중단으로 원래 수준 회귀 | Control Plan에 책임자·관리도·이탈 대응 명시 |

## Ⅵ. 제언

과제 종료 전 관리계획을 프로세스 책임자에게 이관하고, 관리도로 개선 수준의 유지를 확인한 뒤 과제 종료

### 개선 유지 책임 구조

```text
개선 유지 책임
    │
    ├─ 과제 리더 ── 관리계획 작성·이관
    │
    ├─ 프로세스 책임자 ── 관리도 감시·이탈 대응
    │
    └─ 경영 후원자 ── 유지 확인 후 과제 종료 승인
```

### 프로세스 책임자 역할 확대: 관리도 이탈 대응

```text
관리도에 CTQ 측정값 기록
    ↓
관리 한계선 이탈·비정상 패턴 여부 확인
    ├─ 관리 상태 → 표준 절차 유지
    └─ 이탈 → 원인 조사·조치 후 관리계획 갱신
```

### 선택 근거: 개선 적용 즉시 종료와의 비교

| 구분 | 개선 적용 즉시 종료 | 제언: 유지 확인 후 종료 |
|---|---|---|
| 종료 기준 | 개선안 적용 완료 | 관리도로 개선 수준 유지 확인 |
| 유지 책임 | 과제팀 해산 후 불명확 | 프로세스 책임자 |
| 이탈 시 대응 | 재발 후 신규 과제 착수 | 관리계획의 사전 대응 기준 |

## 출제 이력과 검증 출처

- 제132~140회 공식 문제지에 Six Sigma DMAIC 단독 문항 없음
- [ASQ, DMAIC Process: Define, Measure, Analyze, Improve, Control](https://asq.org/quality-resources/dmaic): 기존 프로세스 개선용 5단계, Measure의 측정체계 검증·기준선 확정, Control의 관리계획·통계적 공정관리
- [ASQ, What Is Six Sigma?](https://asq.org/quality-resources/six-sigma)
- [ASQ, Certified Six Sigma Green Belt Body of Knowledge, 2022](https://www.asq.org/cert/resource/pdf/certification/2022-SSGB-BoK.pdf): DFSS 로드맵으로서 DMADV(define, measure, analyze, design, verify)와 DMAIC의 대응
- [ASQ, Certified Six Sigma Black Belt Body of Knowledge, 2022](https://www.asq.org/cert/resource/pdf/certification/2022-SSBB-BoK.pdf): DMADV의 마지막 단계를 validate로 표기
- [ASQ, What Is 3.4 per Million?](https://asq.org/quality-progress/articles/what-is-34-per-million?id=d3d31b31c1da4f60b281025df9ccd057)

## 연결 토픽

- 이전 토픽: [Programmable Money·AI Agent 결제](./110_programmable_money_ai_agents.md)
- 연관 토픽: [품질비용(COQ)](./106_cost_of_quality_coq.md), [BPR](./010_bpr.md)
- 다음 토픽: [CCPM·TOC](./112_critical_chain_toc.md)
