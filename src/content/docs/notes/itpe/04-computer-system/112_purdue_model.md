---
title: "퍼듀 모델(Purdue Model)"
author: "agnusdei1207"
date: "2026-10-24T22:41:35+09:00"
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

- 퍼듀 모델(Purdue Model), 산업제어시스템(ICS), SCADA, 운영기술(OT)
- 산업용 DMZ(IDMZ), 신뢰 경계(Zone & Conduit), IEC 62443, ISA-95
- 데이터 다이오드(Data Diode), 제로 트러스트(Zero Trust), 마이크로 세그멘테이션
- 점프 호스트(Bastion), OT 침입 탐지, 산업용 프로토콜(Modbus, OPC UA)

## Ⅰ. 퍼듀 모델(Purdue Model)의 개요

- 핵심 요약 : 현장 센서부터 기업 경영 시스템까지를 여섯 계층으로 나누고 계층 사이의 통신 경계를 정의한 산업 시스템 참조 모델.
- 개념 : 공장 자동화, 발전소, 정유 플랜트 등 **산업제어시스템** (ICS, Industrial Control System)과 **운영기술** (OT, Operational Technology) 환경을 Level 0부터 Level 5까지 여섯 계층으로 구조화하고 계층 간 경계를 정의한 산업 참조 모델로, ISA(International Society of Automation)-95 계열의 기업-제조 통합 체계를 바탕으로 하며, 그 안에 감독 제어 시스템인 SCADA(Supervisory Control and Data Acquisition)가 포함됨.
- 배경 및 필요성 : 폐쇄망으로 운영되던 공장 설비가 스마트 팩토리, 산업용 사물인터넷(IIoT, Industrial Internet of Things), 클라우드 분석과 연결되면서 외부 인터넷에 노출되었고, 이에 따른 **랜섬웨어** 등 사이버 위협을 체계적으로 막기 위해 필요해짐.
- 주요 목적 : OT 계층과 IT(Information Technology) 계층 사이의 명확한 보안 경계 수립, 산업용 DMZ(IDMZ, Industrial Demilitarized Zone)를 통한 위험 격리, 실시간 제어의 무결성과 공정 가용성(Availability) 보장.

## Ⅱ. 퍼듀 모델의 특징 및 장점

- 핵심 요약 : 기능별 계층 분리와 중계 구간 설정이 장애와 침해의 전파 범위를 좁혀 제어 공정의 가용성을 지키는 방식.

1. 계층 분리 : 기능별로 여섯 계층을 나눔 → 장애와 침해의 전파 범위를 계층 단위로 한정하여 하위 제어망의 연쇄 중단 방지.
2. 구역과 통로 : 기능별 구역을 나누고 구역 사이 통신을 정의된 경로로만 허용 → 제어망 내부의 측면 이동 억제.
3. 중계 완충 : IT와 OT 사이에 Level 3.5 산업용 DMZ를 두어 직접 통신을 막음 → 외부 위협이 제어망에 닿기 전에 걸러짐.

## Ⅲ. 퍼듀 모델의 계층 구조

- 핵심 요약 : IT와 OT를 Level 3.5의 산업용 DMZ로 나누고, OT 내부는 제어 기능에 따라 Level 0부터 Level 3까지 깊이 분리하는 구조.

```text
[ 퍼듀 모델 6계층 흐름 ]

Level 5 : 기업 비즈니스 시스템
   ↓
Level 4 : 사내 업무망 (IT)
   ↓
Level 3.5 : 산업용 DMZ (IDMZ)
   ↓
Level 3 : 제조 운영 (MES, 현장 Historian)
   ↓
Level 2 : 감독 제어 (SCADA HMI)
   ↓
Level 1 : 실시간 제어 (PLC, DCS)
   ↓
Level 0 : 물리 공정 (센서, 밸브, 모터)
```

- 산업용 DMZ(IDMZ, Level 3.5)는 IT망과 제어망 사이의 완충 지대로, IT 트래픽이 제어망으로 직접 들어오지 못하도록 방화벽과 역방향 프록시를 배치하는 계층.
- 신뢰 경계(Zone & Conduit)는 IEC(International Electrotechnical Commission) 62443 표준에 따라 기능별로 구역(Zone)을 나누고, 구역 사이의 통신을 사전에 정의된 통로(Conduit)로만 허용하는 원칙.

## Ⅳ. 계층별 역할과 주요 프로토콜 비교

- 핵심 요약 : 상위 계층일수록 표준 IT 프로토콜을, 하위 계층일수록 실시간성이 강한 산업용 프로토콜을 사용하므로, 계층마다 보안 통제 방식이 달라야 함.

약어 풀이는 다음과 같다.

1. ERP(Enterprise Resource Planning), MOM(Manufacturing Operations Management), MES(Manufacturing Execution System)
2. PLC(Programmable Logic Controller), DCS(Distributed Control System), HMI(Human-Machine Interface)
3. TCP/IP(Transmission Control Protocol/Internet Protocol), HTTPS(Hypertext Transfer Protocol Secure), SSH(Secure Shell), RDP(Remote Desktop Protocol), OPC UA(OPC Unified Architecture)

| 계층 구분 | 명칭 및 핵심 역할 | 대표 설비와 소프트웨어 | 사용 프로토콜 |
| :--- | :--- | :--- | :--- |
| Level 5 / 4 | 기업 비즈니스 관리 (IT) | ERP 시스템, 메일 서버, 클라우드 데이터 웨어하우스 | TCP/IP, HTTPS, REST API |
| Level 3.5 | 산업용 완충 지대 (IDMZ) | 점프 호스트, 이중화 Historian 서버 | SSH, RDP, 복제 전용 포트 |
| Level 3 | 제조 운영 관리 (MOM) | MES, 전사 SCADA 서버, 도면 관리 | OPC UA, SQL, Modbus TCP |
| Level 2 | 감독 및 모니터링 제어 | 현장 HMI, 엔지니어링 워크스테이션 | OPC DA, Modbus, EtherNet/IP |
| Level 1 | 실시간 제어 | PLC, DCS | PROFINET, Modbus RTU, EtherCAT |
| Level 0 | 물리적 공정 (필드 장치) | 유량계, 압력 센서, 공압 밸브 | 4-20mA 아날로그 신호, HART, IO-Link |

## Ⅴ. 현대 스마트 팩토리에서 퍼듀 모델의 한계와 방안

- 핵심 요약 : 클라우드 직결, 평문 산업 프로토콜, 원격 유지보수 접속이 계층 경계를 무너뜨리므로, 제로 트러스트와 프로토콜 전환, 중계 접속으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| IIoT 엣지의 클라우드 직결 | Level 0~1 센서가 5G나 Wi-Fi로 클라우드에 직접 연결되어 IDMZ 방어선 우회 | 제로 트러스트 적용, 마이크로 세그멘테이션, 엣지 게이트웨이에서 상호 TLS(mTLS, mutual Transport Layer Security) 적용 | 제어망의 외부 직접 세션 수 |
| 산업 프로토콜의 보안 취약점 | Modbus 등 평문 통신과 인증 부재로 패킷 도청과 제어 명령 위변조에 노출 | 암호화와 인증을 지원하는 OPC UA with Security, CIP Security로 단계적 전환 | 평문 프로토콜 잔존 비율 |
| 외부 원격 유지보수 접속 | 협력사의 비인가 원격 도구를 통해 IT망의 랜섬웨어가 제어망으로 횡적 이동 | IDMZ 내 점프 호스트(Bastion) 경유 의무화, MFA(Multi-Factor Authentication) 적용, 세션 녹화와 OTP(One-Time Password) 강제 | 원격 접속 세션 감사 건수 |

## Ⅵ. OT/IT 융합 보안을 위한 기술사적 제언

- 핵심 요약 : 제어망의 데이터는 단방향으로만 내보내고, 제어망 탐지는 가용성을 해치지 않는 미러링 방식으로 운영하는 방향.

생산 데이터와 Historian 로그를 Level 4 이상 비즈니스 망이나 클라우드로 보낼 때는 데이터 다이오드(Data Diode)처럼 물리적으로 역방향 신호를 보낼 수 없는 장치를 쓰는 것이 바람직하다. 이렇게 하면 외부에서 제어망으로 들어오는 경로를 하드웨어 수준에서 차단할 수 있다. 제어망의 트래픽은 주기가 일정한 결정론적 특성이 있으므로, 제어 명령의 비정상 쓰기나 PLC 프로그램 다운로드 명령을 감시하는 OT 침입 탐지(OT-IDS, Intrusion Detection System)는 트래픽을 미러링하여 관찰하는 방식으로 도입해 실시간 제어를 방해하지 않도록 해야 한다.

```text
[ 제어망 데이터의 단방향 전송 ]

Level 0~3 : 생산 데이터, Historian 로그
   ↓ 데이터 다이오드 (단방향)
Level 3.5 : 산업용 DMZ 중계
   ↓
Level 4~5 : 비즈니스망, 클라우드 분석
```

## Ⅶ. 결론

- 핵심 요약 : 퍼듀 모델은 IT와 OT의 경계를 계층과 산업용 DMZ로 세우는 참조 모델이며, 스마트 팩토리에서는 그 경계를 제로 트러스트와 단방향 전송으로 보강해야 함.
- 시사점 : 제어 공정의 가용성이 최우선인 환경에서는 보안 통제가 실시간 제어를 방해하지 않아야 하므로, 계층별 통제 수단은 가용성 영향을 먼저 검증해야 함.
