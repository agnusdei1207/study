---
title: "아두이노(Arduino)"
author: "agnusdei1207"
date: "2026-10-24T22:40:52+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 아두이노(Arduino), 피지컬 컴퓨팅(Physical Computing), 마이크로컨트롤러(MCU)
- 부트로더(Bootloader), 베어메탈(Bare-Metal), setup(), loop()
- GPIO, PWM, ADC, ISP(In-System Programming), USB
- 비차단 상태 머신, 포토커플러, PLC, TinyML, FreeRTOS

## Ⅰ. 아두이노의 개요

- 핵심 요약 : 마이크로컨트롤러 보드와 간단한 개발 환경으로 센서와 액추에이터 제어의 진입 장벽을 낮춘 피지컬 컴퓨팅 플랫폼.
- 개념 : 마이크로컨트롤러(MCU, Microcontroller Unit) 칩을 탑재한 오픈소스 하드웨어 보드와, 통합 개발 환경(IDE, Integrated Development Environment)과 C/C++ 기반 라이브러리로 구성된 **아두이노** (Arduino) 플랫폼. 실제 세계의 센서 입력과 장치 출력을 다루는 **피지컬 컴퓨팅** (Physical Computing)의 대표 프로토타이핑 도구임.
- 배경 및 필요성 : 과거에는 어셈블리 코딩과 고가의 **ISP** (In-System Programming) 장비, 레지스터 직접 제어가 필요해 전문가만 다룰 수 있었음.
- 주요 목적 : 오픈소스 하드웨어 생태계 확보, **사물인터넷** (IoT, Internet of Things)과 임베디드 시제품의 신속한 검증, 표준 핀헤더와 쉴드를 통한 기능 확장.

## Ⅱ. 아두이노의 특징 및 장점

- 핵심 요약 : USB 부트로더와 setup-loop 실행 모델이 별도 장비 없이 빠른 시제품 개발을 가능하게 하는 구조.

1. **부트로더** (Bootloader) : 칩 플래시 최상단에 상주한 소형 부트로더가 USB(Universal Serial Bus) 시리얼을 통해 새 펌웨어를 기록 → 전용 프로그래머 없이 USB 연결만으로 펌웨어 교체.
2. **베어메탈** (Bare-Metal) 실행 : 운영체제 없이 `setup()`에서 핀과 주변장치를 한 번 초기화한 뒤 `loop()`를 무한 반복 실행 → 구조가 단순하고 응답 시간을 예측하기 쉬움.
3. 표준 핀 확장 : 표준 핀헤더와 쉴드로 센서와 모터 모듈을 결합 → 하드웨어 연결과 검증 시간 단축.

## Ⅲ. 아두이노의 구조 (흐름)

- 핵심 요약 : 개발 PC에서 컴파일한 펌웨어가 USB 시리얼 칩과 부트로더를 거쳐 MCU 플래시에 올라가고, 이후 setup과 loop 구조로 실행되는 흐름.

```text
[ 펌웨어 업로드 흐름 ]

PC (Arduino IDE)
  스케치 컴파일 → .hex 생성
     ↓ USB 시리얼
USB-시리얼 칩 (ATmega16U2)
     ↓ DTR(Data Terminal Ready) 자동 리셋
MCU (ATmega328P)
  부트로더가 새 .hex를 플래시에 기록
```

```text
[ 실행 루프 구조 ]

전원 인가 또는 리셋
     ↓
setup() (1회 초기화)
     ↓
loop() (무한 반복)
  센서 읽기 → 판단 → 액추에이터 제어
  → loop() 처음으로 복귀
```

- 메모리 구성 (Uno 기준) : 32KB 플래시에 프로그램 코드를, 2KB **SRAM** (Static Random-Access Memory)에 실행 중 변수와 스택을, 1KB **EEPROM** (Electrically Erasable Programmable Read-Only Memory)에 전원 차단 후에도 남을 데이터를 둠.
- 주변장치 : 타이머와 카운터, 10비트 **ADC** (Analog-to-Digital Converter) 6채널, 디지털 **GPIO** (General-Purpose Input/Output) 14핀 중 6핀의 **PWM** (Pulse-Width Modulation), 인터럽트를 제공함.

## Ⅳ. 아두이노와 라즈베리 파이의 비교 분석

- 핵심 요약 : 아두이노는 OS 없이 실시간 제어와 저전력에 강하고, 라즈베리 파이는 Linux 기반으로 대용량 연산과 네트워크 처리에 강함.

| 비교 항목 | 아두이노 (Uno 등) | 라즈베리 파이 (Pi 4·5 등) |
| :--- | :--- | :--- |
| 컴퓨팅 분류 | 마이크로컨트롤러 (MCU) | 싱글보드 컴퓨터 (SBC, Single-Board Computer) |
| 운영체제 | 없음 (베어메탈 펌웨어 단독 실행) | Linux 기반 OS 탑재 |
| 프로세서 | 8비트 AVR 등 저속 단일 코어 중심 | 64비트 쿼드코어 ARM, GHz급 |
| 메모리 | 수 KB 규모의 RAM (Random-Access Memory) | 수 GB 규모의 RAM |
| 전력 소모 | 저전력, 배터리 구동에 유리 | 전용 어댑터 전원이 필요한 수준 |
| 실시간 제어 | 결정론적 제어에 강함 | Linux 스케줄링 특성상 엄격한 실시간 보장에 한계 |
| 적합 분야 | 모터 PWM 제어, 단순 센서 수집, 도어락 | 영상 처리, 웹 서버, AI(Artificial Intelligence) 비전, 복잡한 네트워크 통신 |

- 선택 기준 : 마이크로초 단위의 정확한 제어와 저전력이 우선이면 MCU, 복잡한 소프트웨어 스택과 대용량 데이터가 우선이면 SBC를 고름.

## Ⅴ. 아두이노 플랫폼의 주요 한계와 방안

- 핵심 요약 : 메모리 고갈, 블로킹 함수로 인한 반응성 저하, 산업 현장의 노이즈 취약성이 주요 한계이며 메모리 관리, 비차단 설계, 산업용 장비 전환으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| 극도로 제한된 메모리 | 문자열 처리나 큰 버퍼로 힙과 스택이 충돌해 예측 불가능한 재부팅 발생 | 동적 할당(`malloc`, `String`) 최소화, 정적 문자열은 `F()` 매크로로 플래시에 상주 | 스택 여유 공간, 재부팅 횟수 |
| `delay()` 남발에 따른 반응성 상실 | 대기 중 CPU가 멈춰 센서 인터럽트와 수신 데이터를 놓침 | `millis()` 기반 비차단 상태 머신(FSM, Finite State Machine) 구현 | 입력 처리 지연, 데이터 유실률 |
| 산업 현장의 전기적 노이즈 | 보급형 보드에 서지와 EMI(Electromagnetic Interference) 보호 회로가 없어 모터 노이즈에 즉시 오동작 | 포토커플러 절연 회로 설계, 산업용 보드(Arduino Pro, Portenta) 또는 PLC(Programmable Logic Controller)로 대체 | 오동작 발생 건수, 절연 시험 결과 |

## Ⅵ. 미래 임베디드 IoT 환경을 위한 기술사적 제언

- 핵심 요약 : 아두이노의 쓰임새를 넓히려면 경량 AI를 기기 안에 두고, 다중 작업은 실시간 운영체제로 관리하는 방향으로 진화해야 함.

1. Cortex-M 계열 아두이노 보드에 **TinyML** (초소형 머신러닝, Tiny Machine Learning) 방식의 TensorFlow Lite for Microcontrollers 같은 경량 추론 엔진을 올려, 클라우드 연결 없이 음성 키워드나 진동 이상을 감지하는 엣지 노드를 설계하는 것이 바람직하다.
2. 다중 태스크가 필요한 상용 IoT 기기는 FreeRTOS나 Zephyr 같은 실시간 운영체제를 도입해 태스크 우선순위와 세마포어 동기화를 관리하도록 해야 한다.

## Ⅶ. 결론

- 핵심 요약 : 아두이노는 입문과 시제품의 표준 플랫폼이지만, 규모와 안전성 요구가 커지면 실시간 운영체제와 산업용 장비로 옮겨 가야 함.
- 시사점 : 프로토타입의 속도와 제품의 신뢰성을 구분해 플랫폼을 선택하는 기준이 필요함.
