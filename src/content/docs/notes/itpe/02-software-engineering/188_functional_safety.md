---
title: "기능안전(Functional Safety)"
author: "agnusdei1207"
date: "2026-10-25T00:07:34+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 기능안전(Functional Safety), IEC(International Electrotechnical Commission) 61508, ISO(International Organization for Standardization) 26262, HARA(Hazard Analysis and Risk Assessment)
- ASIL(Automotive Safety Integrity Level), SIL(Safety Integrity Level), SOTIF(Safety of the Intended Functionality), 페일 오퍼레이셔널(Fail-Operational), Automotive SPICE

## Ⅰ. 기능안전의 개요

- 핵심 요약 : 제어 시스템의 오작동과 결함에도 안전 상태로 전이하고 잔존 위험을 허용 수준 이하로 억제하는 안전 공학 체계.
- 개념 : **기능안전** (Functional Safety)은 전기·전자·소프트웨어 기반 제어 시스템에서 오작동이나 부품 결함, 환경 장애가 생겨도 시스템이 이를 감지해 안전 상태(Safe State)로 전이하거나 위험을 허용 가능한 잔존 위험(Tolerable Risk) 이하로 억제하도록 보장하는 안전 공학 체계.
- 배경 및 필요성 : 자율주행차, 원자력 발전소, 항공기 비행제어, 의료 로봇처럼 소프트웨어 오류가 인명 피해로 직결되는 임베디드 제어 시스템에서 사고를 사전에 막을 체계가 필요함.
- 모태 및 도메인 표준 : 모태 표준은 **IEC 61508** (International Electrotechnical Commission 61508, 전기·전자·프로그래밍 가능 전자 시스템의 기능안전)이며, 자동차 분야는 ISO(International Organization for Standardization) 26262, 철도 분야는 EN 50128, 항공 분야는 DO-178C 등 도메인별 표준으로 파생됨.

## Ⅱ. 기능안전의 특징 및 장점

- 핵심 요약 : 위험 분석에 기반한 등급화와 안전 상태 전이를 결합해 고장 유형별로 차별 대응하는 체계.

1. 안전 상태 전이 : 결함을 감지하면 안전 상태로 전이 → 사고 확대를 차단.
2. 잔존 위험 통제 : 위험을 허용 가능한 수준 이하로 억제 → 기준 대비 안전 수준을 정량적으로 입증.
3. 위험원 분석 : **HARA** (Hazard Analysis and Risk Assessment, 위험원 분석 및 위험도 평가)로 위험을 먼저 식별 → 안전 요구의 근거 확보.
4. 등급 기반 요구 : **SIL** (Safety Integrity Level)과 **ASIL** (Automotive Safety Integrity Level) 등급으로 안전 요구의 강도를 구분 → 개발 자원을 위험도에 비례하게 배분.
5. 고장 유형별 대응 : 무작위 하드웨어 고장과 체계적 소프트웨어 결함을 나누어 대응 → 검증 수단의 낭비 감소.
6. 표준 체계 : 모태 표준과 도메인 파생 표준을 연계 → 산업 간 안전 요구 소통 비용 절감.

## Ⅲ. 기능안전의 구조 (흐름)

- 핵심 요약 : 위험원 분석 후 심각도·노출 빈도·통제 가능성의 조합으로 안전 무결성 등급을 정하는 흐름.

```text
[ 위험원 분석 (HARA) ]
          ↓
[ 심각도 S0 ~ S3 ]
[ 노출 빈도 E1 ~ E4 ]
[ 통제 가능성 C1 ~ C3 ]
          ↓ 매트릭스 조합
[ ASIL 등급 : QM, A, B, C, D ]
```

- **SIL** (Safety Integrity Level, IEC 61508) : 1단계부터 4단계까지 정의하며, 최상위인 SIL 4는 고요구 모드에서 시간당 위험 측 고장 확률을 10^-9 이상 10^-8 미만으로 제한.
- **ASIL** (Automotive Safety Integrity Level, ISO 26262) : 심각도(S), 노출 빈도(E), 운전자 통제 가능성(C)의 조합으로 QM(Quality Management)부터 ASIL A, B, C, D까지 등급을 부여하며 ASIL D가 가장 엄격함.

```text
[ 고장 원인 ]
          ↓
[ 무작위 하드웨어 고장 ] → 확률로 예측 → 하드웨어 이중화
[ 체계적 소프트웨어 결함 ] → 입력 조건에 재현 → 프로세스 준수
```

## Ⅳ. 무작위 하드웨어 고장과 체계적 소프트웨어 결함의 비교

- 핵심 요약 : 통계적으로 예측 가능한 하드웨어 고장은 이중화로, 재현되는 소프트웨어 결함은 개발 프로세스로 대응하는 구분.

| 비교 항목 | 무작위 하드웨어 고장 (Random Hardware Failure) | 체계적 소프트웨어 결함 (Systematic Failure) |
| --- | --- | --- |
| 발생 원인 | 마모, 열화, 방사선에 의한 비트 플립(Bit-Flip) | 요구사항 오해, 설계 및 코딩 논리 오류 |
| 예측 가능성 | 고장률 분포로 정량 예측 (FIT(Failures In Time), MTBF(Mean Time Between Failures)) | 동일 조건에서 같은 결함이 재현되므로 확률 모델로 다루기 어려움 |
| 대응 방안 | 듀얼 코어 락스텝, ECC(Error-Correcting Code) 메모리, 워치독 | V-모델 준수, MISRA-C 정적 분석, MC/DC(Modified Condition/Decision Coverage) 검증 |
| 안전 메트릭 | SPFM(Single-Point Fault Metric), LFM(Latent Fault Metric) | 결함 밀도, 테스트 커버리지, 프로세스 성숙도 |

- 선택 기준 : 고장 원인이 물리적 열화인지 설계 결함인지 먼저 구분한 뒤 하드웨어 대책과 프로세스 대책의 비중을 정함.

## Ⅴ. 기능안전의 한계와 방안

- 핵심 요약 : 엄격한 표준 준수의 개발 공수, AI 등 비결정론 기술의 검증, 하드웨어 이중화 원가가 주요 한계이며 도구화·표준 융합·하이브리드 설계로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 표준 준수 개발 공수 증가 | 정형 기법, MC/DC 커버리지, 안전 산출물 관리로 일정 비중 확대 | 모델 기반 개발 (MBD, Model-Based Development)과 인증된 자동 코드 생성 도구 활용 | 안전 산출물 완결률, 결함 발견 시점 |
| 비결정론 AI 시스템의 검증 한계 | 고장이 없어도 환경 인지 실패로 사고 발생, 전통적 고장 중심 분석으로 포착 불가 | **의도된 기능의 안전성** (SOTIF, Safety of the Intended Functionality, ISO 21448) 적용, 시나리오 기반 시뮬레이션과 섀도 모드 데이터 검증 | 미탐지 시나리오 수, 인지 실패율 |
| 하드웨어 이중화 원가 | 듀얼 코어 락스텝, TMR(Triple Modular Redundancy) 등 중복 구성으로 제품 원가 상승 | 소프트웨어 자가 시험 라이브러리, ECC, 워치독을 조합한 하이브리드 장애 허용 구조 | 부품 원가, 진단 커버리지 |

## Ⅵ. 고신뢰성 제어 소프트웨어 구축을 위한 기술사적 제언

- 핵심 요약 : 페일 세이프에서 페일 오퍼레이셔널 구조로 아키텍처를 진화시키고, 프로세스 성숙도를 전사 개발 체계에 내재화하는 방향.

1. 아키텍처 진화 : 자율주행 시스템은 제어기 고장 시 전원을 끊는 페일 세이프(Fail-Safe) 방식만으로는 부족하므로, 보조 제어기가 **페일 오퍼레이셔널** (Fail-Operational) 방식으로 필수 기능을 유지하고 안전하게 정차하는 구조를 갖추는 것이 바람직하다.
2. 프로세스 내재화 : 정보시스템 부서와 품질 조직은 **Automotive SPICE** (Automotive Software Process Improvement and Capability Determination) 기준으로 요구사항 추적성과 변경 영향도 분석을 개발 표준에 포함해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 정량 등급에 근거한 안전 설계가 기능안전의 출발점이며, 비결정론 기술은 표준 융합으로 보완해야 함.
- 시사점 : 위험 분석과 등급화 위에 SOTIF 융합과 페일 오퍼레이셔널 구조를 더하는 것이 현재 기능안전의 진화 방향임.
