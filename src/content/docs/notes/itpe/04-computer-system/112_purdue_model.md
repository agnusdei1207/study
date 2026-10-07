---
title: "퍼듀 모델(Purdue Model)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 퍼듀 모델(Purdue Model)의 개요

- 개념 : 공장 자동화, 발전소, 정유 플랜트 등 **산업제어시스템** (ICS, Industrial Control System/SCADA, Supervisory Control and Data Acquisition) 및 **운영기술** (OT: Operational Technology) 환경을 물리적 현장 센서부터 상위 기업 경영 정보시스템(IT, Information Technology)까지 6개의 계층(Level 0 ~ Level 5)으로 구조화하고 계층 간 통신 경계를 정의한 글로벌 표준 산업 참조 모델(ISA(International Society of Automation)-95 및 IEC(International Electrotechnical Commission) 62443 기반).
- 배경 및 필요성 : 과거 폐쇄망으로 운영되던 공장 OT(Operational Technology) 설비들이 스마트 팩토리, 산업용 사물인터넷(IIoT, Industrial Internet of Things), 클라우드 AI(Artificial Intelligence) 분석과 결합하면서 외부 인터넷과 연결됨에 따라 발생한 **랜섬웨어** 및 사이버 테러 위협을 체계적으로 방어하기 위해 필수화됨.
- 핵심 목적 : OT 계층과 IT 계층 간의 명확한 보안 경계 수립, 산업용 DMZ(Demilitarized Zone, IDMZ: Industrial Demilitarized Zone, Level 3.5)를 통한 위험 격리, 실시간 제어 무결성 및 공정 가용성(Availability) 보장.

## Ⅱ. 퍼듀 모델의 6계층 구조 및 산업용 DMZ(IDMZ) 아키텍처

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 퍼듀 모델 (Purdue Enterprise Reference Architecture) 6대 계층 ]     │
│                                                                        │
│   [ IT 계층 ]                                                          │
│   Level 5: 엔터프라이즈 비즈니스 네트워크 (ERP, SCM, 클라우드 AI 분석) │
│   Level 4: 비즈니스 기획 및 물류 (사내 업무망, 데이터센터, 이메일)      │
│   ========================= [ Level 3.5: 산업용 DMZ (IDMZ) ] ==========│
│    * IT/OT 트래픽 직접 통신 절대 금지! 방화벽 기반 프록시 및 데이터 중계│
│    - 패치 관리 (WSUS), 점프 호스트(Bastion), Historian 데이터 복제 서버 │
│   =====================================================================│
│   [ OT 계층 (제조 운영 및 제어 영역) ]                                 │
│   Level 3: 사이트 제조 운영 관리 (MES, 현장 Historian, HMI 중앙 서버)  │
│   Level 2: 구역 제어 (SCADA HMI, 엔지니어링 워크스테이션)              │
│   Level 1: 기본 제어 (PLC, DCS, RTU, 세이프티 SIS 제어기)              │
│   Level 0: 물리적 공정 (센서, 밸브, 모터, 계측기, 액추에이터)          │
└────────────────────────────────────────────────────────────────────────┘
```

- **산업용 DMZ** (IDMZ: Level 3.5) : Level 4(IT망)와 Level 3(OT망) 사이에 위치하는 완충 지대로, 어떠한 IT 트래픽도 제어망(Level 0~3)으로 직접 인입되지 못하도록 양방향 차단 방화벽과 역방향 프록시를 배치.
- **신뢰 경계선** (Conduit & Zone) : **IEC 62443** 표준에 따라 공정 기능별로 독립된 구역(Zone)을 분할하고, 구역 간 통신은 사전 정의된 채널(Conduit)만을 통해서만 통제.

## Ⅲ. 퍼듀 모델 계층별 역할 및 주요 프로토콜 비교 분석

| 계층 구분 | 명칭 및 핵심 역할 | 대표 설비 및 소프트웨어 | 사용 프로토콜 |
| :--- | :--- | :--- | :--- |
| **Level 5 / 4** | 기업 비즈니스 관리 (IT) | SAP ERP(Enterprise Resource Planning), 메일 서버, 클라우드 DW(Data Warehouse) | 표준 TCP(Transmission Control Protocol)/IP(Internet Protocol), HTTPS(Hypertext Transfer Protocol Secure), REST(Representational State Transfer) API(Application Programming Interface) |
| **Level 3.5** | 산업용 완충 지대 (IDMZ) | 점프 호스트, 이중화 Historian 서버| 암호화 SSH(Secure Shell), RDP(Remote Desktop Protocol), 복제 전용 포트|
| **Level 3** | 제조 운영 관리 (MOM, Manufacturing Operations Management/MES, Manufacturing Execution System)| MES, 전사 SCADA 서버, 도면 관리 | OPC(Open Platform Communications)-UA(Unified Architecture), SQL(Structured Query Language) Net, Modbus-TCP |
| **Level 2** | 감독 및 모니터링 제어 | 로컬 터치 HMI, 엔지니어링 랩톱 | OPC-DA, Modbus, Ethernet/IP |
| **Level 1** | **실시간 제어** (Controller) | PLC (Siemens, Rockwell), DCS | PROFINET, Modbus RTU, EtherCAT|
| **Level 0** | 물리적 공정 (Field Device)| 유량계, 압력 센서, 공압 밸브 | 4-20mA 아날로그 신호, HART, IO-Link|

## Ⅳ. 현대 스마트 팩토리 환경에서 퍼듀 모델의 주요 한계점 및 해결 방안

- IIoT 엣지 디바이스의 클라우드 직결에 따른 계층 파괴 :
  - 한계점 : Level 0/1의 스마트 센서가 5G/Wi-Fi를 통해 AWS(Amazon Web Services)/Azure 클라우드로 데이터를 직접 전송하면서 전통적인 IDMZ 방어선 무력화.
  - 해결 방안 : 제로 트러스트(Zero Trust) 및 마이크로 세그멘테이션(Micro-segmentation) 도입, 엣지 게이트웨이 상에서 mTLS 및 일방향 통신(Data Diode) 강제.
- OT 프로토콜(Modbus 등)의 내재적 보안 취약점 :
  - 한계점 : Level 1/2에서 사용되는 전통 산업용 프로토콜이 평문 통신 및 인증 부재로 패킷 스니핑과 제어 명령 위변조에 무방비.
  - 해결 방안 : 암호화 및 디지털 서명을 지원하는 최신 보안 프로토콜(OPC-UA with Security, CIP Security)로 단계적 전면 교체.
- 원격 유지보수 접근(Remote Access)에 따른 랜섬웨어 유입 :
  - 한계점 : 외주 협력사가 TeamViewer 등 비인가 원격 도구를 사용하여 제어망에 접속하다가 IT망의 랜섬웨어가 공장 전체로 횡적 이동(Lateral Movement).
  - 해결 방안 : 제어망 원격 접속 시 전용 IDMZ 내 MFA(Multi-Factor Authentication) 적용 배스천 호스트(Bastion) 경유 의무화, 세션 녹화 및 일회용 비밀번호(OTP, One-Time Password) 강제.

## Ⅴ. 성공적인 OT/IT 융합 보안을 위한 기술사적 제언

- 물리적 일방향 데이터 전송 장치(Data Diode) 도입 : Level 3의 생산 공정 데이터 및 Historian 로그를 Level 4/5 비즈니스 및 클라우드로 전송할 때, 물리적으로 역방향 광신호를 송출할 수 없는 하드웨어 기반 데이터 다이오드(Data Diode)를 구축하여 외부 침입 경로를 100% 원천 차단해야 함.
- OT 전용 침입 탐지 시스템(OT-IDS(Intrusion Detection System)) 및 가용성 중심 관제 수립 : 제어망 패킷은 변동이 거의 없는 결정론적 특성을 가지므로, PLC 로더 명령 및 비정상 쓰기 명령을 AI로 탐지하는 OT 전용 네트워크 이상 감지(Nozomi, Claroty) 솔루션을 인라인 차단이 아닌 미러링(TAP) 방식으로 안전하게 구축할 것을 제언함.
