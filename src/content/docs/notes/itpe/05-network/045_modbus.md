---
title: "MODBUS"
author: "agnusdei1207"
date: "2026-10-24T22:49:07+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- MODBUS, PLC(Programmable Logic Controller), 마스터-슬레이브(Master-Slave), 기능 코드(Function Code)
- 레지스터 맵, Modbus RTU, Modbus ASCII, Modbus TCP, MBAP 헤더
- CRC-16, LRC, Modbus TCP Security, OPC UA, MQTT
- 데이터 다이오드, 제로 트러스트(Zero Trust), IEC 62443

## Ⅰ. MODBUS의 개요

- 핵심 요약 : 제어기와 현장 장비를 벤더와 무관하게 연결하기 위해 만들어진 산업용 응용 계층 통신 프로토콜.
- 개념 : 1979년 Modicon(현 Schneider Electric)이 **PLC** (Programmable Logic Controller) 간 통신을 위해 개발한 **마스터-슬레이브** (Master-Slave) 구조의 산업용 응용 계층 프로토콜.
- 배경 및 필요성 : 스마트 공장과 플랜트에는 센서, 구동기, 계측기, PLC가 서로 다른 벤더 제품으로 섞여 있어, 벤더에 종속되지 않고 데이터를 읽고 제어할 공통 규약이 필요함.
- 주요 목적 :
  1. 구조가 단순하고 구현이 쉬운 장비 제어 인터페이스 제공
  2. 시리얼(RS-232, RS-485) 및 산업용 이더넷 환경에서 같은 데이터 모델 사용
  3. 개방형 표준으로 장비 간 데이터 교환 보장

## Ⅱ. MODBUS의 특징 및 장점

- 핵심 요약 : 단순한 질의-응답 구조와 표준화된 레지스터 모델이 구현 비용을 낮추고 장비 호환성을 높이는 방식.

1. 마스터-슬레이브 질의 응답 : 마스터만 요청을 시작하고 슬레이브는 응답만 반환 → 통신 충돌이 적고 장비 측 구현이 단순함.
2. **레지스터 모델** : 이산 입력, 코일, 입력 레지스터, 유지 레지스터의 4가지 메모리 영역으로 데이터를 주소 단위로 접근 → 장비별 데이터 구조를 같은 방식으로 다룸.
3. **표준 기능 코드** : 01(Read Coils), 03(Read Holding Registers), 05, 06, 16 등 표준 코드 사용 → 벤더가 달라도 읽기와 쓰기 명령을 공통으로 처리.
4. 이중 전송 방식 : 시리얼 기반 RTU와 이더넷 기반 TCP를 같은 데이터 모델로 지원 → 기존 장비와 신규 이더넷 장비의 공존.

## Ⅲ. MODBUS의 구조 (흐름)

- 핵심 요약 : 기능 코드와 데이터를 공통 프로토콜 데이터 단위(PDU, Protocol Data Unit)로 두고, 전송 방식에 따라 주소, 오류 검출, 헤더를 덧붙이는 프레임 구조.

```text
[ MODBUS RTU 프레임 ]

슬레이브 주소 (1B)
        ↓
기능 코드 (1B)
        ↓
데이터 (NB)
        ↓
CRC-16 (2B)
```

```text
[ MODBUS TCP 프레임 ]

MBAP 헤더 (7B)
트랜잭션 ID·프로토콜 ID·길이·유닛 ID
        ↓
기능 코드 (1B)
        ↓
데이터 (NB)
```

- **CRC** (Cyclic Redundancy Check) : RTU 프레임 끝에 붙여 전송 중 비트 오류를 검출하는 16비트 값.
- **MBAP 헤더** (Modbus Application Protocol Header) : TCP 프레임 앞에 붙는 7바이트 헤더로, 트랜잭션 식별자와 길이 정보를 담아 요청과 응답을 짝지음.
- 마스터가 요청하면 주소가 지정된 슬레이브가 기능 코드를 수행하고 응답을 돌려주는 단방향 질의-응답 구조.

## Ⅳ. MODBUS 전송 모드의 비교

- 핵심 요약 : 시리얼 모드는 프레임 구분과 오류 검출 방식이 다르고, TCP 모드는 이더넷 계층의 오류 검출과 세션 관리에 기댐.

| 비교 항목 | MODBUS RTU | MODBUS ASCII | MODBUS TCP |
| --- | --- | --- | --- |
| 물리 계층 | RS-485, RS-232 | RS-485, RS-232 | 이더넷 (IEEE(Institute of Electrical and Electronics Engineers) 802.3) |
| 전송 계층 | 시리얼 직접 | 시리얼 직접 | TCP/IP (Transmission Control Protocol/Internet Protocol), 포트 502 |
| 데이터 인코딩 | 8비트 이진 | 2바이트 ASCII 문자 | 8비트 이진 |
| 오류 검출 | CRC-16 | LRC (Longitudinal Redundancy Check) | TCP 체크섬과 이더넷 프레임 검사 |
| 프레임 구분 | 3.5 문자 시간의 무음 구간 | 시작 콜론과 종료 CR/LF | MBAP 헤더의 길이 필드 |
| 전송 효율 | 높음 | 낮음 (데이터량 약 2배) | 매우 높음 |

- 선택 기준 : 기존 시리얼 장비는 RTU가 표준이고, 디버깅이 중요한 저속 구간에는 ASCII가 쓰이며, 신규 이더넷 구간은 TCP를 사용.

## Ⅴ. MODBUS의 한계와 방안

- 핵심 요약 : 인증과 암호화가 없는 평문 구조가 가장 큰 한계이며, 보안 전송 계층과 산업용 침입 탐지로 통제하고, 폴링 한계는 이벤트 기반 프로토콜로 보완.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 인증·암호화 부재 | 평문 전송과 접근 제어 부재로 도청, 레지스터 변조, 리플레이 공격에 노출 | TLS(Transport Layer Security)와 상호 인증을 결합한 Modbus/TCP Security(포트 802) 적용, 산업용 방화벽의 심층 패킷 검사(DPI, Deep Packet Inspection) | 비인가 쓰기 명령 탐지 건수 |
| 폴링 방식의 이벤트 지연 | 마스터가 물어보기 전에는 슬레이브가 알람을 전달할 수 없어 긴급 상황 인지가 늦음 | MQTT(Message Queuing Telemetry Transport), OPC UA(Open Platform Communications Unified Architecture), CoAP(Constrained Application Protocol) 기반 게이트웨이 연계 | 알람 전달 지연 시간 |

## Ⅵ. MODBUS에 대한 기술사적 제언

- 핵심 요약 : 현장 장비는 Modbus를 유지하고 상위 계층은 보안과 의미 모델이 있는 표준으로 옮기되, 레거시 구간은 제로 트러스트 관점으로 격리하는 방향.

1. 레거시 구간의 격리 : 교체가 어려운 Modbus RTU와 TCP 장비가 많은 운영 기술(OT, Operational Technology) 구간에 제로 트러스트 원칙을 적용해 마이크로 세그멘테이션을 두고, 외부 방향으로는 데이터 다이오드를 배치할 필요가 있음.
2. 상위 계층 표준 전환 : 현장 I/O는 Modbus를 그대로 두고, MES(Manufacturing Execution System), SCADA(Supervisory Control and Data Acquisition), 클라우드 연동 구간은 OPC UA로 변환하는 구조를 설계해야 함.
3. 산업 보안 기준 준수 : IEC(International Electrotechnical Commission) 62443 기준으로 Modbus 통신 구간의 위험 평가를 수행하고, 목표 보안 수준에 맞춰 IPsec(Internet Protocol Security)이나 MACsec(Media Access Control Security) 같은 암호화 터널을 적용할 필요가 있음.

## Ⅶ. 결론

- 핵심 요약 : MODBUS는 단순하고 널리 보급된 현장 제어 프로토콜이지만, 보안 설계가 없어 망 구조에서 보완해야 하는 프로토콜.
- 시사점 : 현장 장비의 수명과 보안 요구를 함께 고려해 격리와 표준 전환을 병행하는 것이 산업 제어망 운영의 현실적 방향.
