---
title: "기능안전(Functional Safety)"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- 기능안전(Functional Safety), IEC(International Electrotechnical Commission) 61508, ISO(International Organization for Standardization) 26262, HARA(Hazard Analysis and Risk Assessment)
- ASIL(Automotive Safety Integrity Level), SIL(Safety Integrity Level), SOTIF(Safety of the Intended Functionality), 페일 오퍼레이셔널(Fail-Operational), Automotive SPICE

## Ⅰ. 기능안전(Functional Safety)의 개요

- 핵심 요약 : 제어 시스템의 오작동·결함·환경 장애 시 안전 상태 전이와 잔존 위험 억제를 보장하는 안전 공학 체계.
- 개념 : 전기·전자·소프트웨어 기반 제어 시스템의 오작동, 내부 부품 결함 또는 예기치 못한 환경적 장애 발생 시에도, 시스템이 이를 감지하여 안전 상태(Safe State)로 전이하거나 위험을 허용 가능한 잔존 위험(Tolerable Risk) 수준 이하로 억제하도록 보장하는 안전 공학 체계.
- 배경 및 필요성 : 자율주행차, 원자력 발전소, 항공기 비행제어, 의료 로봇 등 복잡한 임베디드 제어 시스템의 소프트웨어 오류 직결 대형 인명 피해(사망, 상해) 참사 방지 필요.
- 모태 및 도메인 표준 : 모태 표준 IEC(International Electrotechnical Commission) 61508(전기/전자/프로그래밍 가능 전자 시스템의 기능안전), 자동차 ISO(International Organization for Standardization) 26262, 철도 EN 50128, 항공 DO-178C.

## Ⅱ. 기능안전의 특징

- 핵심 요약 : 위험 분석 기반 등급화와 안전 상태 전이, 고장 유형별 차별 대응의 체계.

1. 오작동·결함·환경 장애 감지 시 안전 상태(Safe State) 전이.
2. 위험의 잔존 위험(Tolerable Risk) 수준 이하 억제.
3. HARA(Hazard Analysis and Risk Assessment) 기반 위험원 분석 및 위험도 평가.
4. SIL(Safety Integrity Level)·ASIL(Automotive Safety Integrity Level) 등급 체계의 정량적 안전 요구.
5. 무작위 하드웨어 고장과 체계적 소프트웨어 결함의 구분 대응.
6. 모태 표준 IEC 61508과 도메인별 파생 표준(ISO 26262, EN 50128, DO-178C) 체계.

## Ⅲ. 기능안전의 구조 (흐름)

- 핵심 요약 : 심각도·노출·통제 가능성의 매트릭스 조합으로 ASIL 등급을 확정하는 흐름.
- 위험도 분석 및 안전 무결성 등급 결정 메커니즘.

```text
[ 위험원 분석 및 위험도 평가 (HARA) ]
[ 심각도 (Severity, S) ]
 - S0: 무상해 / S1: 경상/중상
 - S2: 중상/생명 위협 / S3: 치명적 사망
[ 노출 확률 (Exposure, E) ]
 - E1: 극히 희박 / E2: 낮은 빈도
 - E3: 중간 빈도 / E4: 상시 주행
[ 통제 가능성 (Controllability, C) ]
 - C1: 통제 용이 (99% 운전자 대처)
 - C2: 보통 통제 (90% 대처)
 - C3: 통제 극난 (사고 회피 불가)
[ ASIL 등급 확정 = S x E x C ]
 - QM → ASIL A → B → C → D
   (ASIL D: 최고 안전 요구)
```

- SIL(Safety Integrity Level, IEC 61508) : 1단계부터 4단계까지 정의, SIL 4는 시간당 고장 확률 $10^{-9}$ 이하의 최고 안전 무결성 요구.
- ASIL(Automotive Safety Integrity Level, ISO 26262) : 심각도(S0~S3), 노출 빈도(E1~E4), 운전자 통제 가능성(C1~C3)의 매트릭스 조합, QM(Quality Management)부터 ASIL A, B, C, D까지 5단계 등급 부여.

## Ⅳ. 무작위 하드웨어 고장과 체계적 소프트웨어 결함의 비교

- 핵심 요약 : 통계적 예측 가능 고장의 이중화 대응과 확률적 예측 불가 결함의 프로세스 대응 구분.
- 고장 유형별 대응 체계 대조.

```text
[ 무작위 하드웨어 고장 ]              [ 체계적 소프트웨어 결함 ]
  통계적 확률로 정량 예측 가능          동일 조건 입력 시 100% 재현
        │                                   │
  듀얼 코어 락스텝·ECC·워치독           V-모델·MISRA-C 정적 분석·MC/DC
 (메트릭 : SPFM, LFM)                (커버리지·프로세스 성숙도)
```

| 비교 항목 | 무작위 하드웨어 고장(Random Hardware Failure) | 체계적 소프트웨어 결함(Systematic Failure) |
|---|---|---|
| 발생 원인 | 물리적 마모, 열화, 방사선에 의한 비트 플립(Bit-Flip) | 요구사항 명세 오해, 코딩 논리 오류, 설계 결함 |
| 예측 가능성 | 통계적 확률 분포(FIT(Failures In Time), MTBF(Mean Time Between Failures))로 고장률 정량 예측 가능 | 확률적 예측 불가(동일 조건 입력 시 100% 동일 결함 재현) |
| 대응 방안 | 하드웨어 이중화(듀얼 코어 락스텝), ECC(Error-Correcting Code) 메모리, 워치독 | 엄격한 프로세스 준수(V-모델), MISRA-C 정적 분석, MC/DC 검증 |
| 안전 메트릭 | SPFM(Single-Point Fault Metric, 단일점 결함 메트릭), LFM(Latent Fault Metric, 잠재 결함 메트릭) | 결함 밀도, 테스트 커버리지, 프로세스 성숙도(Automotive SPICE) |

## Ⅴ. 기능안전의 장점과 한계

- 핵심 요약 : 인명 참사 방지·정량 등급화의 장점, 개발 공수·AI 검증·이중화 비용의 한계.
- 장점
  1. 소프트웨어 오류 직결 대형 인명 사고의 사전 방지.
  2. SIL/ASIL 등급 기반의 명확한 안전 요구 소통.
  3. 하드웨어·소프트웨어 고장 유형별 체계적 검증.
- 한계점 1 : 엄격한 기능안전 표준(ISO 26262, IEC 61508) 준수에 따른 개발 공수 폭증
  - 한계점 : ASIL/SIL 등급 달성 요건인 정형 기법, MC/DC 테스트 커버리지, 안전 산출물 관리의 개발 일정 비중 확대.
  - 해결 방안 : 모델 기반 개발 MBD(Model-Based Development; Simulink 활용) 및 자동 코드 생성 도구(Qualified Code Generator) 도입을 통한 인적 코딩 오류·검증 공수 대폭 절감.
- 한계점 2 : 자율주행·AI(Artificial Intelligence) 등 비결정론적 기술의 안전 무결성 입증 한계
  - 한계점 : 고장(Fault) 방지 중심의 전통적 기능안전으로는 하드웨어/SW(Software) 결함 부재 환경에서도 환경 인지 한계로 발생하는 AI 시스템 사고 검증 불가.
  - 해결 방안 : 의도된 기능의 안전성 SOTIF(Safety of the Intended Functionality; ISO 21448) 표준 융합, 섀도 모드(Shadow Mode) 주행 데이터 기반 시나리오 시뮬레이션 및 안전 방어선(Safety Barrier) 다중화.
- 한계점 3 : 하드웨어 무작위 결함 대응 이중화의 원가 부담
  - 한계점 : 안전 목표 달성을 위한 듀얼 코어 록스텝(Lockstep), TMR(Triple Modular Redundancy) 등 하드웨어 중복 구성으로 인한 제품 원가 상승.
  - 해결 방안 : 소프트웨어 기반 결함 탐지(Self-Test Library) 및 에러 정정 코드(ECC), 워치독 타이머 활용 하이브리드 장애 허용(Fault-Tolerant) 아키텍처 구축.

## Ⅵ. 고신뢰성 제어 소프트웨어 구축을 위한 기술사적 제언

- 핵심 요약 : 페일 세이프에서 페일 오퍼레이셔널로의 아키텍처 진화와 A-SPICE 레벨 3 프로세스 내재화.
- 페일 세이프(Fail-Safe)에서 페일 오퍼레이셔널(Fail-Operational)로의 아키텍처 진화 : 레벨 3 이상 자율주행 시스템의 제어기 고장 시 단순 전원 차단(Fail-Safe) 한계 보완, 보조(Secondary) 제어기의 최소 10초 이상 조향·제동 유지와 갓길 안전 정차 아키텍처 필수 구축.
- 소프트웨어 안전 수명주기 전반의 A-SPICE 레벨 3 연계 인증 : 프로세스 결함의 소프트웨어 결함 직결 방지, Automotive SPICE 레벨 3 인증 기반 요구사항 추적성, 양방향 아키텍처 검증, 변경 영향도 분석 체계의 전사 프로세스 의무 내재화 필요.

## Ⅶ. 결론

- 핵심 요약 : 정량 등급 기반 안전 설계와 비결정론적 기술·비용 과제의 표준 융합 대응 필요.
- 요약 : 위험 분석·등급화·안전 상태 전이로 인명 피해를 억제하는 안전 공학 체계.
- 시사점 : SOTIF 융합, 페일 오퍼레이셔널 아키텍처, Automotive SPICE 기반 프로세스 내재화의 병행 필요.
