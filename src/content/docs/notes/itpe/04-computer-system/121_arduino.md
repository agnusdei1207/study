---
title: "아두이노(Arduino)"
author: "Codex"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  label: "121. 아두이노(Arduino)"
  order: 121
  badge:
    text: "응용"
extra:
  model: "GPT-6"
  keyword_grade: "응용"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 → 임베디드 시스템 → 아두이노

## 30초 인출

- 본질: Arduino는 보드·개발 도구·라이브러리로 센서와 액추에이터를 제어하는 오픈 하드웨어·소프트웨어 플랫폼
- 메커니즘: 보드별 코어로 스케치를 빌드·업로드하고 MCU가 센서 입력을 읽어 제어 출력을 수행
- 통찰: 한계: 빌드 성공이 보드별 전압·핀·부하 호환을 보장하지 않음 → 방안: 공식 핀맵과 실제 회로에서 입출력·보호를 검증한다.

<details>
<summary>핵심 용어</summary>

- **Arduino(아두이노):** 보드와 IDE·코어 라이브러리를 결합해 임베디드 장치를 개발하는 플랫폼
- **MCU(Microcontroller Unit):** CPU·메모리·주변장치를 통합해 장치 제어 프로그램을 실행하는 마이크로컨트롤러
- **GPIO(General-Purpose Input/Output):** 디지털 신호를 입력하거나 출력하는 범용 핀 기능
- **PWM(Pulse-Width Modulation):** 펄스의 듀티비를 조절해 평균 전압·전력을 제어하는 방식
- **Sketch:** Arduino 개발 환경에서 작성하는 보드용 프로그램

</details>

---

## 2~4교시 예상문제 (25점)

> 아두이노 플랫폼의 구조와 동작을 설명하고, 보드 선택 및 실제 적용 시 고려사항을 제시하시오. (예상)

---

## 2~4교시 25점 답안

### Ⅰ. 아두이노의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Arduino(아두이노):** 보드·개발 도구·라이브러리로 임베디드 장치를 개발하는 플랫폼 |
| 목적 | 하드웨어 제어 프로그램의 작성·빌드·업로드를 단순화 |

### Ⅱ. Arduino 플랫폼의 특징

| 특징 | 의미 |
|---|---|
| 보드·도구 통합 | IDE·보드 코어·라이브러리로 개발·업로드 지원 |
| 물리 입출력 | GPIO·ADC·PWM·통신으로 센서와 구동 회로 연결 |
| 보드 다양성 | MCU·전압·핀·메모리·OS 구성이 제품마다 다름 |

### Ⅲ. 개발·제어 체계와 프로세스

**핵심 실행 체계**

```text
스케치 → 보드 코어·도구체인 → 펌웨어 업로드 → MCU
                                           ↓
센서·통신 입력 → GPIO/ADC → 제어 로직 → GPIO/PWM/통신 출력
                                           ↓
                                      구동 회로·액추에이터
```

**하위 메커니즘: 센서 값의 출력 제어**

```text
입력 핀 설정 → 샘플링·ADC 변환 → 임계값/제어 연산
           → 출력 핀·PWM 설정 → 구동 회로 동작 → 입력 재확인
```

### Ⅳ. 보드·입출력 유형 비교

| 비교 대상 | 확인할 차이 | 적용 판단 |
|---|---|---|
| Uno Rev3·R4·Q | MCU/MPU 구성·전압·메모리·OS | 공식 사양과 기존 코드 호환성 확인 |
| 디지털 I/O·ADC | 논리 전압·입력 범위·해상도 | 센서 전기 규격과 일치 여부 |
| PWM·통신 | 지원 핀·주파수·버스 | 액추에이터 구동 회로와 핀 충돌 확인 |

### Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 보드별 핀·전압·주변장치가 달라 코드 이식 오류 발생 | 공식 핀맵·전기 규격을 기준으로 연결 시험 |
| MCU 핀의 허용 전류로 부하를 직접 구동할 수 없음 | 적절한 드라이버·절연·보호 회로 사용 |
| 실험실 동작이 현장 전원·환경을 대표하지 않음 | 전원 변동·센서 이상·재시작 시나리오 시험 |

### Ⅵ. 제언

스케치가 빌드되고 보드에서 실행돼도 실제 부하의 전기적 안전과 복구 능력은 확인되지 않는다. **대상 보드의 핀·전원·구동 회로를 먼저 확정**하고 센서 오류·전원 재투입·출력 고착을 실물에서 검증한 뒤 적용해야 한다.

## 출제 이력과 검증 출처

- 제102회 1교시: `오픈소스 하드웨어(OSHW)의 개념과 아두이노(Arduino)의 구조적 특징을 설명하시오.`
- 제105회 1교시: `아두이노(Arduino)와 라즈베리 파이(Raspberry Pi)의 하드웨어 특성 및 용도를 비교 설명하시오.`
- [Arduino UNO Rev3 — Official Documentation](https://docs.arduino.cc/hardware/uno-rev3/)
- [Arduino UNO R4 Minima — Official Documentation](https://docs.arduino.cc/hardware/uno-r4-minima/)
- [Arduino UNO Q — Official Documentation](https://docs.arduino.cc/hardware/uno-q/)
- [Arduino Language Reference](https://docs.arduino.cc/language-reference/)
- [Q-Net 정보관리기술사 출제문제](https://www.q-net.or.kr/cst006.do?id=cst00601&gSite=Q&gId=)
