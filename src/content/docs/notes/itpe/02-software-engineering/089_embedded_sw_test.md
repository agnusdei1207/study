---
title: "임베디드 소프트웨어 테스트 및 X-in-the-Loop(MIL·SIL·PIL·HIL) (MIL: Model-in-the-Loop; SIL: Software-in-the-Loop; PIL: Processor-in-the-Loop; HIL: Hardware-in-the-Loop)"
description: "MBD·XiL 단계별 검증, MIL→SIL→PIL→HIL, 고장 주입·vECU·ISO 26262·MC/DC, 비용·타이밍·추적성 한계와 방안"
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

- X-in-the-Loop(XiL), MIL(Model-in-the-Loop), SIL(Software-in-the-Loop), PIL(Processor-in-the-Loop), HIL(Hardware-in-the-Loop)
- 임베디드 시스템 테스트, MBD(Model-Based Development), ECU(Electronic Control Unit), ISO(International Organization for Standardization) 26262, 고장 주입(Fault Injection), vECU(Virtual ECU)

## Ⅰ. 임베디드 SW 테스트 및 X-in-the-Loop의 개요

- 핵심 요약 : 실물 하드웨어가 완성되기 전부터 가상 모델과 시뮬레이션으로 임베디드 SW의 안전성을 단계적으로 검증하는 체계.
- 개념 : 임베디드 시스템 테스트는 하드웨어와 결합된 실시간 제어 시스템(자동차 전장, 항공우주, 철도, 국방 등)에서, 실물 완성 전부터 가상화된 모델과 시뮬레이션을 활용해 단계별로 기능과 안전성을 검증하는 **X-in-the-Loop** (XiL) 테스팅 체계.
- 배경 및 필요성 : 차량 제어기 **ECU** (Electronic Control Unit)의 결함을 실차와 하드웨어 제작 후 발견하면 리콜 비용과 인명 사고 위험이 커지므로, 모델 기반 개발 **MBD** (Model-Based Development) 단계부터 시프트 레프트(Shift-Left) 검증이 필요함.
- 표준 근거 : 자동차 기능안전 표준 ISO(International Organization for Standardization) 26262, 항공 소프트웨어 표준 DO-178C.

## Ⅱ. X-in-the-Loop의 특징 및 장점

- 핵심 요약 : 모델에서 코드, 프로세서, 하드웨어로 검증 대상을 단계적으로 실물화하는 시프트 레프트 검증 체계.

1. **MIL** (Model-in-the-Loop) : MATLAB/Simulink 제어 모델과 가상 플랜트(차량 물리 모델)를 연결해 알고리즘 수준의 동작을 시험 → 설계 오류의 초기 차단.
2. **SIL** (Software-in-the-Loop) : 모델 기반으로 자동 생성한 C/C++ 코드를 호스트 PC(Personal Computer) 시뮬레이터에서 실행해 코드 수준의 기능 검증 → 생성 코드의 정확성 확인.
3. **PIL** (Processor-in-the-Loop) : 타깃 프로세서에 바이너리를 적재해 컴파일러 최적화 오류, 레지스터, 실행 타이밍을 검증 → 대상 아키텍처 종속 결함 발견.
4. **HIL** (Hardware-in-the-Loop) : 실제 ECU에 전원, CAN(Controller Area Network)과 LIN(Local Interconnect Network) 신호, 가상 센서 신호를 연결하여 극한 환경을 재현 → 실차 이전에 안전성 확인. 이때 **고장 주입** (Fault Injection) 시험을 함께 수행.
5. 시뮬레이션 통과와 형식적 증명의 구분 : 시뮬레이션은 시험한 입력에 대한 결과일 뿐, 모든 입력에 대한 수학적 입증은 별도 검증 과제 → 검증 범위의 과신 방지.

## Ⅲ. X-in-the-Loop의 구조 (흐름)

- 핵심 요약 : MIL부터 HIL까지 검증 대상이 수학 모델에서 실물 하드웨어로 점진적으로 이동하며, 결함 발견 비용이 함께 증가하는 구조.

```text
[ 요구사항 · 제어 알고리즘 ]
   ↓
[ 1. MIL : 수학 모델 시뮬레이션 ]
   ↓ 코드 자동 생성
[ 2. SIL : 생성 코드의 PC 검증 ]
   ↓ 타깃 빌드·플래싱
[ 3. PIL : 타깃 프로세서 타이밍 검증 ]
   ↓ 실물 ECU 통합
[ 4. HIL : 실물 ECU와 실시간 시뮬레이터 ]
```

- MIL 단계에서 제어 로직의 타당성을 확보하면 이후 코드와 하드웨어 단계의 결함을 근원에서 줄일 수 있음.

## Ⅳ. X-in-the-Loop 테스팅 단계별 비교

- 핵심 요약 : 검증 대상의 실물화 정도에 따라 실행 환경, 검증 목적, 결함 발견 비용이 단계별로 달라지는 구조.

```text
[ 모델 ]            MIL
   ↓ 코드 생성
[ 생성 코드 ]       SIL
   ↓ 타깃 빌드
[ 타깃 바이너리 ]   PIL
   ↓ 실물 통합
[ 실물 ECU ]        HIL
```

| 단계 | 실행 대상 (Target) | 테스트 환경 | 주 검증 목적 | 결함 발견 시 비용 |
| --- | --- | --- | --- | --- |
| MIL | 제어 알고리즘 모델 | 호스트 PC의 Simulink 환경 | 제어 이론과 수학적 로직의 타당성 | 가장 낮음 (초기 발견) |
| SIL | 모델 기반 자동 생성 코드 | 호스트 PC의 가상 런타임 | 코드 정밀도와 입출력 데이터 정합성 | 낮음 |
| PIL | 실제 타깃 MCU(Microcontroller Unit) 보드 | 타깃 보드와 가상 플랜트 | 타깃 아키텍처 종속성과 클록 타이밍 | 중간 |
| HIL | 최종 제작된 ECU 장치 | HIL 시뮬레이터 장비 | 전기적 특성, 네트워크 통신, 극한 장애 안전성 | 높음 (전용 장비 필요) |

## Ⅴ. 임베디드 SW 테스트의 한계와 방안

- 핵심 요약 : 하드웨어 병목 해소와 조기 결함 차단의 장점 아래, 장비 비용, 실시간 재현 난도, 표준 산출물 부담이라는 한계가 존재.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| HIL 장비 구축 비용과 하드웨어 가용성 병목 | 고가의 시뮬레이터 리그가 필요하고, 칩셋 공급이 지연되면 테스트 전체가 막힘 | 시뮬레이션 선행(Shift-Left) 전략, vECU(Virtual ECU) 기반 SIL과 가상 검증 환경의 조기 구축 | 장비 가동률, HIL 대기 시간 |
| 실시간성 제약과 타이밍 결함 재현 난도 | 마이크로초 단위 인터럽트, 태스크 선점, 지터로 생기는 간헐적 레이스 결함의 재현과 원인 규명이 어려움 | 비침습적 하드웨어 트레이서와 로직 분석기 활용, 타이밍 분석 도구를 연계한 WCET(Worst-Case Execution Time) 검증 | 결함 재현 성공률, WCET 여유율 |
| 기능안전 표준 준수 산출물 부담 | ISO 26262의 ASIL(Automotive Safety Integrity Level) 등급에 따라 요구사항, 코드, 테스트 간 양방향 추적성과 MC/DC(Modified Condition/Decision Coverage)를 수작업으로 입증해야 함 | ALM(Application Lifecycle Management) 도구와 VectorCAST, LDRA 연동으로 추적성 매트릭스와 인증 리포트 자동 생성 | 추적성 누락 건수, 인증 준비 공수 |

## Ⅵ. 자동차 기능안전 관점의 기술사적 제언

- 핵심 요약 : 고장 주입 기반의 Fail-Safe 검증과 가상 ECU 기반 클라우드 CI 확장을 병행하는 방향.
- 실차에서 위험하여 인위적으로 재현하기 어려운 센서 단선, 접지 쇼트, 전압 급강하 같은 고장은 HIL 환경에서 모의 주입하고, ECU가 규정된 안전 상태(Safe State)로 정상 전이하는지 검증하는 절차를 필수로 두어야 한다.
- 가상 ECU(vECU, Virtual ECU)를 컨테이너화하여 클라우드 CI(Continuous Integration) 파이프라인에서 수많은 시나리오를 병렬로 자동 실행하면 물리 HIL 장비의 병목을 완화할 수 있으므로, AUTOSAR(AUTomotive Open System ARchitecture) 기반 vECU의 조기 도입을 검토할 필요가 있다.

## Ⅶ. 결론

- 핵심 요약 : XiL은 가상 모델부터 실물 하드웨어까지 단계적으로 검증하여 임베디드 SW의 안전성을 확보하는 체계.
- 시사점 : vECU 가상화와 테스트 자동화의 연동, 고장 주입 시험의 내재화가 하드웨어 병목과 표준 산출물 부담을 줄이는 핵심 조건.