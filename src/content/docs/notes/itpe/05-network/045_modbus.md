---
title: "MODBUS"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "045"
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- MODBUS, PLC(Programmable Logic Controller), 마스터-슬레이브(Master-Slave), 기능 코드(Function Code)
- 코일, 유지 레지스터, PDU(Protocol Data Unit), ADU, CRC-16, MBAP 헤더
- Modbus RTU, Modbus ASCII, Modbus TCP, 포트 502
- Modbus/TCP Security, OPC UA, IEC 62443, 단방향 게이트웨이

## Ⅰ. MODBUS의 개요

- 핵심 요약 : 제어기와 현장 장비를 벤더와 무관하게 연결하기 위해 만들어진 산업용 응용 계층 통신 프로토콜.
- 개념 : 1979년 Modicon(현 Schneider Electric)이 **PLC**(Programmable Logic Controller) 간 통신용으로 개발한 **마스터-슬레이브**(Master-Slave) 구조의 응용 계층 프로토콜.
- 배경 및 필요성 : 플랜트와 스마트 팩토리에 센서·구동기·계측기·PLC가 벤더별로 혼재, 벤더 종속 없이 데이터를 읽고 쓰는 공통 규약의 필요.
- 주요 목적 :
  1. 단순 구조의 장비 제어 인터페이스 제공
  2. 시리얼(RS-232·RS-485)과 이더넷에서의 동일 데이터 모델 사용
  3. 개방형 규격으로 이기종 장비 간 상호 접속 보장

## Ⅱ. MODBUS의 특징 및 장점

- 핵심 요약 : 질의-응답 구조와 표준화된 데이터 모델·기능 코드가 구현 비용을 낮추고 이기종 장비 호환성을 높이는 방식.

1. 마스터-슬레이브 질의-응답 : 마스터만 요청을 시작하고 슬레이브는 응답만 반환 → 통신 충돌 방지와 장비 측 구현의 단순화.
2. 표준 데이터 모델 : 코일, 이산 입력, 입력 레지스터, 유지 레지스터의 4종 메모리 영역을 주소 단위 접근 → 장비별 구조 차이의 흡수.
3. 표준 기능 코드 : 읽기(01·03)와 쓰기(05·06·16) 등 공통 코드 사용 → 벤더가 달라도 동일 명령 처리.
4. 다중 전송 모드 : 시리얼 기반 RTU(Remote Terminal Unit)·ASCII(American Standard Code for Information Interchange) 모드와 이더넷 기반 TCP(Transmission Control Protocol) 모드가 동일 데이터 구조 공유 → 기존 장비와 신규 장비의 공존.

## Ⅲ. MODBUS의 구조 (흐름)

- 핵심 요약 : 기능 코드와 데이터를 공통 PDU로 정의하고, 전송 모드에 따라 주소·오류 검출·헤더를 덧붙인 ADU로 운반하는 구조.
- **PDU**(Protocol Data Unit) : 기능 코드와 데이터로 구성되는 전송 모드 독립 부분.
- **ADU**(Application Data Unit) : 주소와 오류 검출 필드 등을 덧붙인 전송 모드 종속 프레임.

```text
[ MODBUS RTU 프레임 (ADU) ]

슬레이브 주소 (1바이트)
   ↓
PDU : 기능 코드 + 데이터
   ↓
CRC-16 (2바이트)
```

```text
[ MODBUS TCP 프레임 ]

MBAP 헤더 (7바이트)
   ↓
PDU : 기능 코드 + 데이터
   ↓
TCP 포트 502 전송
```

- **MBAP 헤더**(Modbus Application Protocol Header) : 트랜잭션 식별자·프로토콜 식별자·길이·유닛 식별자를 담아 요청과 응답을 짝짓는 헤더.
- **CRC**(Cyclic Redundancy Check) : RTU 프레임 끝에 붙는 16비트 오류 검출 값.

## Ⅳ. MODBUS 전송 모드의 비교

- 핵심 요약 : 시리얼 모드는 오류 검출·프레임 구분 방식이 다르고, TCP 모드는 이더넷·TCP 계층의 검증에 기대는 차이.

| 비교 항목 | Modbus RTU | Modbus ASCII | Modbus TCP |
| --- | --- | --- | --- |
| 물리 계층 | RS-485·RS-232 | RS-485·RS-232 | 이더넷 |
| 데이터 인코딩 | 8비트 이진 | ASCII 문자 2바이트 | 8비트 이진 |
| 오류 검출 | CRC-16 | LRC(Longitudinal Redundancy Check) | TCP 체크섬 |
| 프레임 구분 | 3.5 문자 시간의 무음 구간 | 시작 콜론·종료 CR/LF | MBAP 헤더의 길이 필드 |
| 전송 효율 | 높음 | 낮음 (데이터량 증가) | 가장 높음 |

- 선택 기준 : 기존 시리얼 장비 연동은 RTU, 저속 구간의 디버깅 편의가 필요하면 ASCII, 신규 이더넷 구간은 TCP 사용.

## Ⅴ. MODBUS의 한계와 방안

- 핵심 요약 : 인증·암호화 부재의 평문 구조와 폴링 방식의 이벤트 지연이 핵심 한계이며 보안 전송·게이트웨이 연계로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 인증·암호화 부재 | 평문 전송과 접근 제어 부재 → 도청·레지스터 변조·리플레이 공격에 노출 | 상호 인증 TLS(Transport Layer Security)를 결합한 Modbus/TCP Security(포트 802), 산업용 방화벽의 심층 패킷 검사 | 비인가 쓰기 명령 탐지 건수 |
| 폴링 방식의 이벤트 지연 | 마스터 질의 전에는 슬레이브의 알람 전달 불가 → 긴급 상황 인지 지연 | OPC UA(Open Platform Communications Unified Architecture)·MQTT(Message Queuing Telemetry Transport) 게이트웨이의 이벤트 중계 | 알람 전달 지연 시간 |

## Ⅵ. MODBUS에 대한 기술사적 제언

- 핵심 요약 : 현장 계층은 Modbus를 유지하되 상위 계층 전환·구간 보안·격리를 제도화하는 방향.

1. OT 보안 담당 조직 : IEC(International Electrotechnical Commission) 62443 기준의 위험 평가를 Modbus 통신 구간에 수행하고 목표 보안 수준에 맞춘 통제 설계.
2. 시스템 설계 조직 : 현장 입출력은 Modbus를 유지하고 MES(Manufacturing Execution System)·SCADA(Supervisory Control and Data Acquisition)·클라우드 연동 구간은 OPC UA 변환 계층을 두는 이중 구조 설계.
3. 네트워크 운영 조직 : 레거시 RTU·TCP 구간의 세그먼트 분리와 단방향 게이트웨이 배치로 외부 유출 경로 차단.

## Ⅶ. 결론

- 핵심 요약 : MODBUS는 단순성과 보급률이 강점인 현장 제어 프로토콜이면서 보안 설계가 결핍된 레거시 규격.
- 현장 장비의 수명 특성을 고려한 격리와 상위 계층 전환의 병행이 산업 제어망 운영의 현실적 방향.
