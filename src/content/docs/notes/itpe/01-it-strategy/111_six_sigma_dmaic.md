---
title: "Six Sigma DMAIC (DMAIC: Define, Measure, Analyze, Improve, Control)"
author: "agnusdei1207"
date: "2026-10-24T23:52:29+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "Claude Haiku 5.5"
---

## 연관 키워드

- 식스 시그마(Six Sigma), DMAIC(Define, Measure, Analyze, Improve, Control), DPMO(Defects Per Million Opportunities, 백만 기회당 결함 수)
- CTQ(Critical to Quality, 핵심 품질 특성), SIPOC(Suppliers, Inputs, Process, Outputs, Customers), Gage R&R(Repeatability and Reproducibility, 측정시스템 분석)
- 공정능력지수(Cp, Cpk), 특성요인도(Fishbone), 파레토 차트(Pareto Chart), 가설 검정(Hypothesis Test)
- DOE(Design of Experiments, 실험계획법), FMEA(Failure Mode and Effects Analysis, 고장 모드 영향 분석), SPC(Statistical Process Control, 통계적 공정관리)
- Poka-Yoke(실수방지), DMADV(Define, Measure, Analyze, Design, Verify), DFSS(Design for Six Sigma), 린 식스 시그마(Lean Six Sigma)

## Ⅰ. Six Sigma DMAIC의 개요

- 핵심 요약 : 결함을 백만 기회당 3.4개 이하로 줄이기 위해 데이터와 통계로 문제를 정의·측정·분석·개선·통제하는 5단계 품질 혁신 방법론.
- 개념 : 프로세스의 결함을 **식스 시그마** (Six Sigma)의 목표 수준인 백만 기회당 3.4개(3.4 DPMO, Defects Per Million Opportunities) 이하로 낮추기 위해, 데이터와 통계 기법으로 문제를 정의·측정·분석·개선·통제하는 **DMAIC** (Define, Measure, Analyze, Improve, Control) 5단계 방법론.
- 배경 및 필요성 : 경험과 감에 의존한 품질 관리는 프로세스 변동(Variation)의 원인을 규명하지 못해 결함이 반복되므로, 원인을 통계적으로 찾아 제거하는 체계가 필요해짐.
- 주요 목적 : 공정 변동 축소, 결함률 감축, 고객 만족 향상과 품질 원가 절감.

## Ⅱ. Six Sigma DMAIC의 특징 및 장점

- 핵심 요약 : 5단계 절차, 핵심 품질 특성 중심의 자원 집중, 통계 검증이 결합되어 결함의 재발을 막는 체계.

1. DMAIC 5단계 : 문제 정의부터 통제까지 연결 → 일회성 처방 감소.
2. **CTQ** (Critical to Quality, 고객이 중요하게 여기는 핵심 품질 특성) 중심 : 개선 자원을 품질 특성에 집중 → 투자 효율 향상.
3. Gage R&R(Repeatability and Reproducibility, 측정시스템 분석) : 측정의 반복성과 재현성을 확인 → 잘못된 원인 분석 축소.
4. 통계적 원인 분석 : 파레토 차트와 가설 검정으로 핵심 변동 원인을 구분 → 근거 기반 개선.
5. DPMO 추적 : 개선 전후 결함 수준을 수치로 비교하고 관리도로 재발을 감시 → 효과 입증.

## Ⅲ. Six Sigma DMAIC의 구조 (흐름)

- 핵심 요약 : 정의에서 통제까지 5단계가 순서대로 진행되고, 단계마다 전용 도구가 대응하는 구조.
- SIPOC(Suppliers, Inputs, Process, Outputs, Customers) : 공급자, 입력, 프로세스, 출력, 고객의 범위를 한눈에 보여주는 프로세스 맵.

```text
[1. Define 정의]
  CTQ 선정, 프로젝트 헌장,
  SIPOC 프로세스 맵 작성
          ↓
[2. Measure 측정]
  측정시스템 분석, 데이터 수집,
  공정능력지수 산출
          ↓
[3. Analyze 분석]
  특성요인도, 파레토 차트,
  가설 검정으로 근본 원인 확정
          ↓
[4. Improve 개선]
  실험계획법, 파일럿 검증,
  고장 위험 분석
          ↓
[5. Control 통제]
  표준화, 관리도 감시,
  실수방지 장치 적용
```

- **DOE** (Design of Experiments, 실험계획법) : 여러 요인의 수준 조합을 체계적으로 실험해 개선 효과가 큰 요인을 찾는 기법.
- **SPC** (Statistical Process Control, 통계적 공정관리) : 관리도로 공정 산포를 감시해 이상 신호를 조기에 잡는 Control 단계 도구.
- **Poka-Yoke** (실수방지) : 작업자 실수가 결함으로 이어지지 않도록 공정을 설계하는 장치.
- 공정능력지수(Cp, Cpk, Process Capability Index) : 규격 대비 공정 산포의 여유를 나타내는 지수.
- FMEA(Failure Mode and Effects Analysis, 고장 모드 영향 분석) : 실패 가능성과 영향을 미리 평가해 개선 우선순위를 정하는 위험 분석 기법.

```text
[식스 시그마 성과 측정 체계]
  DPMO 측정
     ↓
  시그마 수준 환산, 공정능력지수 확인
     ↓
  품질 원가 절감액 정량화
```

## Ⅳ. DMAIC와 DMADV(DFSS)의 비교

- 핵심 요약 : 기존 프로세스를 고치는 DMAIC와, 신규 설계 단계에서 결함을 예방하는 DMADV(DFSS, Design for Six Sigma)의 비교.

| 비교 축 | DMAIC | DMADV (DFSS) |
| --- | --- | --- |
| 적용 대상 | 운영 중인 기존 프로세스와 시스템 | 신규 제품·서비스·아키텍처 |
| 단계 | Define, Measure, Analyze, Improve, Control | Define, Measure, Analyze, Design, Verify |
| 초점 | 기존 결함 원인 제거와 변동 축소 | VoC(Voice of the Customer, 고객의 소리)를 반영한 초기 설계 |
| 접근 방식 | 사후 개선 | 사전 예방 설계 |

## Ⅴ. Six Sigma DMAIC 적용의 한계와 방안

- 핵심 요약 : 분석 비용, 측정 대상의 적합성, 형식적 운영을 통제해야 개선 성과가 유지된다.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 분석 과잉 | 과도한 통계 분석이 개선 의사결정을 늦춤 | 문제 규모에 맞는 도구를 선택하고 린(Lean)의 가치 흐름 분석과 결합 | 과제 리드타임 |
| 제조 지표의 소프트웨어 적용 한계 | 비정형 소프트웨어 업무에 제조 공정 지표를 그대로 적용하기 어려움 | 빌드 실패율, 결함률처럼 반복 측정 가능한 공정부터 적용 | 측정 가능 지표 비율 |
| 형식적 운영 | 자격 취득 중심 과제는 고객·원가 성과와 분리되기 쉬움 | CTQ 개선 결과와 비용 절감액을 검증하고 Control 단계 책임자 지정 | 절감액, 관리도 이탈 건수 |

## Ⅵ. 소프트웨어 및 IT 서비스에서의 Six Sigma 적용을 위한 기술사적 제언

- 핵심 요약 : 린과 식스 시그마의 결합, 측정 신뢰도 확보, 애자일 회고와의 융합으로 경량화된 품질 개선 체계 구축.

- 소프트웨어 조직은 **린 식스 시그마** (LSS, Lean Six Sigma)를 검토할 만하다. 식스 시그마의 통계적 엄격성이 속도를 늦추는 경우 린의 낭비 제거를 함께 적용하면 속도와 품질을 동시에 얻을 수 있다.
- 생산성이나 코드 결함처럼 측정자와 도구에 따라 값이 흔들리는 지표는 Gage R&R로 측정 시스템을 먼저 검증하고, 정적 분석 도구로 측정을 자동화하는 것이 바람직하다.
- 수개월 단위의 대형 프로젝트 대신 애자일 회고에 특성요인도와 5-Whys 기법을 넣어 2주 단위로 병목을 해결하는 경량 방식이 실효성이 높다. 조직 차원에서는 이 방식을 표준 개선 루틴으로 정착시키는 것이 중요하다.

## Ⅶ. 결론

- 핵심 요약 : DMAIC는 데이터와 통계로 결함 원인을 제거하는 5단계 품질 방법론이며, 소프트웨어 적용의 관건은 경량화와 측정 신뢰도 확보.
- 결함 수치를 맞추기보다 고객이 체감하는 품질 특성을 측정 가능하게 정의하고 지속 관리하는 체계로 이해할 필요가 있다.
