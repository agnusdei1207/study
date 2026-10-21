---
title: "Six Sigma DMAIC (DMAIC: Define, Measure, Analyze, Improve, Control)"
author: "agnusdei1207"
date: "2026-10-01T22:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "LongCat 2.5 Preview Free"
---

## 연관 키워드

- 식스 시그마(Six Sigma), DMAIC(Define, Measure, Analyze, Improve, Control)
- DPMO(Defects Per Million Opportunities, 백만 기회당 결함 수), 3.4 DPMO
- CTQ(Critical to Quality, 핵심 품질 특성), SIPOC(Suppliers, Inputs, Process, Outputs, Customers)
- Gage R&R(Repeatability and Reproducibility, 측정시스템 분석)
- Cp/Cpk(공정능력지수), 특성요인도(Fishbone), 파레토 차트
- t-test, ANOVA(Analysis of Variance), DOE(Design of Experiments)
- FMEA(Failure Mode and Effects Analysis), SPC(Statistical Process Control)
- Poka-Yoke(실수방지), DMADV(DFSS), 린 식스 시그마(LSS, Lean Six Sigma)

## Ⅰ. Six Sigma DMAIC의 개요

- 핵심 요약 : 프로세스 결함을 100만 기회당 3.4개(3.4 DPMO) 이하로 줄이기 위해 데이터와 통계적 기법으로 문제를 정의·측정·분석·개선·통제하는 DMAIC 5단계 혁신 방법론.
- 개념 : 프로세스에서 발생하는 결함을 100만 기회당 3.4개(3.4 DPMO, Defects Per Million Opportunities) 이하로 줄이기 위해 데이터와 통계적 기법을 기반으로 문제를 과학적으로 정의(D), 측정(M), 분석(A), 개선(I), 통제(C)하는 DMAIC 5단계 혁신 방법론.
- 배경 및 필요성 : 단순한 주관적 경험이나 감에 의한 품질 관리의 한계를 극복하고 프로세스 변동(Variation)의 원인을 통계적으로 규명하여 제품 및 IT(Information Technology) 서비스 품질의 무결점 추구.
- 주요 목적 : 공정 변동성 최소화, 결함률 획기적 감축, 고객 만족度 극대화 및 품질 원가 절감.

## Ⅱ. Six Sigma DMAIC의 특징 및 장점

- 핵심 요약 : 데이터·통계 기반의 5단계 체계와 CTQ 중심 품질 관리, 벨트 자격증 기반 전문가 체계.

1. **DMAIC 5단계** : 문제 정의부터 개선 유지까지 연결하여 일회성 처방을 줄인다.
2. **CTQ 중심** : 고객이 중요하게 여기는 품질 특성에 개선 자원을 집중한다.
3. **측정시스템 검증** : Gage R&R 등으로 데이터 신뢰도를 확인하여 잘못된 원인 분석을 줄인다.
4. **통계적 원인 분석** : 파레토·가설 검정으로 핵심 변동 원인을 구분하여 개선의 근거를 마련한다.
5. **DPMO·관리도 추적** : 개선 전후 결함 수준과 재발 여부를 수치로 확인한다.

## Ⅲ. Six Sigma DMAIC의 구조 (흐름)

- 핵심 요약 : Define부터 Control까지 5단계 진행과 단계별 핵심 도구 체계.
- DMAIC 5단계 로드맵.

```text
[1. Define (정의)]
   핵심 품질 특성(CTQ, Critical to Quality),
   프로젝트 헌장 작성,
   프로세스 맵(SIPOC, Suppliers, Inputs,
   Process, Outputs, Customers)
          ↓
[2. Measure (측정)]
   측정시스템 분석(Gage R&R), 데이터 수집,
   공정능력지수(Cp, Cpk) 산출
          ↓
[3. Analyze (분석)]
   근본 원인 분석, 특성요인도(Fishbone),
   파레토 차트, 가설 검정(t-test, ANOVA,
   Analysis of Variance)
          ↓
[4. Improve (개선)]
   최적 솔루션 도출,
   실험계획법(DOE, Design of Experiments),
   파일럿 검증, 위험 방지(FMEA,
   Failure Mode and Effects Analysis)
          ↓
[5. Control (통제)]
   표준화 및 문서화, 통계적 공정관리(SPC,
   Statistical Process Control) 관리도,
   실수방지(Poka-Yoke)
```

```text
[식스 시그마 성과 측정 체계]
  DPMO 측정 ──→ 공정능력지수(Cp, Cpk)
        │
        ├─ 시그마 수준 산출
        │
        └─ 품질 원가 절감액 정량화
```

- CTQ : Define 단계에서 정의하는 핵심 품질 특성.
- DOE : Improve 단계의 실험계획법.
- SPC : Control 단계의 통계적 공정관리 관리도.
- Poka-Yoke : Control 단계의 실수방지 기법.

## Ⅳ. DMAIC와 DMADV(DFSS)의 비교

- 핵심 요약 : 기존 프로세스 개선(DMAIC)과 신규 무결점 설계(DMADV/DFSS)의 비교.
- DMAIC(기존 프로세스 개선)와 DMADV/DFSS(신규 설계)의 대비.

| 비교 항목 | DMAIC (기존 프로세스 개선) | DMADV / DFSS (신규 설계) |
|---|---|---|
| 적용 대상 | 현재 운영 중인 기존 프로세스 및 시스템 | 신규 개발하려는 제품, 서비스 및 아키텍처 |
| 5단계 절차 | Define - Measure - Analyze - Improve - Control | Define - Measure - Analyze - Design - Verify |
| 핵심 초점 | 기존 결함 원인 제거 및 변동성 축소 | 고객 요구(VoC, Voice of the Customer)를 반영한 무결점 초기 설계 |
| 접근 방식 | 사후 반응적 개선(Reactive) | 선제적 예방 설계(Proactive) |

## Ⅴ. Six Sigma DMAIC 적용의 한계와 방안

- 핵심 요약 : **분석 비용**, 측정 대상 적합성, 형식적 운영을 통제해야 개선 성과가 유지된다.

| 한계 | 방안 |
|---|---|
| 과도한 통계 분석은 **개선 의사결정**을 늦출 수 있음 | 문제 규모에 맞는 분석 도구를 선택하고 린의 가치 흐름 분석과 결합 |
| 비정형 소프트웨어 업무에 **제조 공정 지표**를 그대로 적용하기 어려움 | 결함률·빌드 실패율처럼 반복 측정 가능한 공정부터 적용 |
| 자격 취득 중심 과제는 실제 **고객·원가 성과**와 분리되기 쉬움 | CTQ 개선 결과와 비용 절감액을 검증하고 Control 단계의 책임자를 지정 |

## Ⅵ. 소프트웨어 및 IT 서비스에서의 Six Sigma 적용을 위한 기술사적 제언

- 핵심 요약 : 린·식스 시그마 결합, 측정시스템 분석 철저화, 애자일 회고 융합.

- 린과 식스 시그마의 결합(Lean Six Sigma) : 통계적 엄격성으로 인해 속도가 느려질 수 있는 식스 시그마의 단점을 보완하여 린의 낭비 제거(속도)와 식스 시그마의 결함 제거(품질)를 동시 달성.
- 소프트웨어 메트릭스의 측정시스템 분석(Gage R&R, Repeatability and Reproducibility) 철저화 : 개발 생산성이나 코드 결함 측정 시 도구와 평가자마다 주관적 편차가 발생하지 않도록 정적 분석 도구(SonarQube 등)를 통한 자동 측정 표준화.
- 애자일 회고(Retrospective) 프로세스와의 융합 : 무거운 수개월 단위의 식스 시그마 프로젝트를 지양하고 2주 단위 스프린트 회고에서 특성요인도와 5-Whys 기법을 활용하여 빠르게 병목을 해결하는 경량화 적용.

## Ⅶ. 결론

- 핵심 요약 : DMAIC는 데이터·통계 기반 5단계 품질 혁신 방법론으로 린 결합과 애자일 융합이 소프트웨어 적용의 관건.
- 요약 : DMAIC는 프로세스 결함을 100만 기회당 3.4개 이하로 줄이기 위해 데이터와 통계적 기법으로 문제를 정의·측정·분석·개선·통제하는 5단계 혁신 방법론.
- 시사점 : 린 식스 시그마 결합, 측정시스템 분석 철저화, 애자일 회고 융합을 통해 소프트웨어 환경에서의 실효성 확보 필요.
