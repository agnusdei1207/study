---
title: "산업제어시스템(ICS)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 산업제어시스템(ICS) 보안의 개요

- 개념 : 원자력 발전소, 전력망, 상수도, 석유화학 플랜트 등 국가 핵심 기반시설의 물리적 공정을 감시하고 제어하는 SCADA(Supervisory Control and Data Acquisition), DCS, PLC(Programmable Logic Controller), RTU 시스템에 대한 사이버 위협을 방어하고 공정의 안전성(Safety)과 연속성을 보장하는 보안 체계.
- 배경 및 필요성 : 과거 폐쇄망으로 운영되던 공정 제어망이 스마트화, 디지털 트윈, 원격 유지보수를 위해 IT(Information Technology)망 및 인터넷과 연결되면서 Stuxnet, Industroyer, Colonial Pipeline 랜섬웨어 등 물리적 파괴를 초래하는 사이버 테러 공격 노출.
- 핵심 목적 : 국가 중요 기반시설의 **가용성** (Availability) 및 **안전성** (Safety) 최우선 보장, 제어 명령 위변조 차단, IT/OT(Operational Technology) 융합 경계의 엄격한 격리.

## Ⅱ. 산업제어시스템(ICS) 보안의 핵심 아키텍처 및 동작 메커니즘

ICS 보안은 ISA(International Society of Automation)/IEC(International Electrotechnical Commission) 62443 표준 및 퍼듀(Purdue) 엔터프라이즈 참조 모델에 기반하여 계층별(Level 0~5) 영역 분리와 산업용 심층 패킷 검사(DPI, Deep Packet Inspection)를 통해 제어 트래픽을 통제함.

```text
[ Purdue 모델 기반 산업제어시스템(ICS) 5계층 구조 ]

  [ IT 영역 ]
  Level 5 : 기업 비즈니스망 (ERP, 이메일, 인터넷)
  Level 4 : 기업 전산망 (IT 인프라, 비즈니스 서버)
  ======================[ 산업용 DMZ (IT/OT 경계) ]======================
  [ OT 영역 ]
  Level 3 : 공정 운영 관리망 (HMI, SCADA 서버, 제어 엔지니어링 워크스테이션)
  Level 2 : 단위 제어망 (운전 콘솔, SCADA Supervisory)
  Level 1 : 로컬 제어망 (PLC, RTU, IED 제어기기)
  Level 0 : 물리 공정 계층 (센서, 밸브, 모터, 액추에이터)

  * 보안 장비 배치:
    - IT/OT 경계: 단방향 데이터 전송장치(Data Diode), 산업용 차세대 방화벽
    - Level 1~3: 산업용 프로토콜 DPI (Modbus, DNP3, OPC-UA 제어명령 검증)
```

- **Purdue 모델 기반 계층 분격** : IT 비즈니스망(L4/5)과 OT 공정 제어망(L0~3) 사이에 **산업용 DMZ**(Demilitarized Zone) (L3.5)를 구축하여 직접 통신을 완전 차단.
- **단방향 데이터 전송장치** (Data Diode) : 물리적으로 수신선(Rx)을 절단하고 송신(Tx) 광케이블만 연결하여 공정 데이터를 IT망으로 반출하되 역유입은 물리적으로 원천 봉쇄.
- **산업용 프로토콜 심층 검사** (DPI) : Modbus, DNP3, Ethernet/IP(Internet Protocol) 등 평문 레거시 프로토콜의 패킷을 7계층까지 파싱하여 허용되지 않은 쓰기(Write) 명령이나 펌웨어 업데이트 패킷 차단.
- 가용성(Availability)과 안전성(Safety) 중심의 통제 : 기밀성을 우선하는 IT 보안과 달리, 1초의 지연도 용납되지 않는 공정 중단 방지와 인명 안전을 최우선 목표로 운영.

## Ⅲ. 산업제어시스템(ICS) 보안의 세부 구성 요소 및 비교 분석

| 비교 항목 | 전통적 IT 정보보안 | 산업제어시스템(OT/ICS) 보안 | 적용 보안 기술 |
| --- | --- | --- | --- |
| 최우선 가치 (CIA) | 기밀성(C) > 완전성(I) > 가용성(A) | 가용성(A) > 완전성(I) > 기밀성(C) | 무중단 Fail-Safe 아키텍처 |
| 보안 목표 | 데이터 유출 및 지적재산권 보호 | 인명 안전(Safety), 물리 설비 파괴 방지 | IEC 62443, 단방향 보안 게이트웨이 |
| 운영 환경 수명 | 장비 교체 주기 3~5년 (빠른 패치) | 설비 수명 15~30년 (패치 극도로 난항) | 가상 패칭(Virtual Patching) |
| 실시간성 요건 | 지연(Latency) 허용 (초 단위 가능) | 결정론적 초저지연 필수 (밀리초 단위) | 인라인 차단 대신 미러링 모니터링 |
| 프로토콜 특성 | 표준 암호화 적용 (TLS, IPsec) | 무인증, 무암호화 레거시 (Modbus, DNP3) | 산업용 침입탐지(IDS, Intrusion Detection System), 프로토콜 DPI |

- ICS 환경에서는 백신 업데이트나 보안 패치 리부팅 한 번으로 공장 전체가 멈추거나 화학 폭발이 일어날 수 있으므로, 인라인 차단보다는 패시브 미러링 기반 이상 탐지가 주를 이룸.

## Ⅳ. 산업제어시스템(ICS) 보안의 주요 한계점 및 해결 방안

- 레거시 산업용 프로토콜의 인증 및 암호화 부재 :
  - 한계점 : Modbus, DNP3 등 수십 년 전 설계된 필드버스 통신은 패킷 내 암호화 및 송신처 인증이 전무하여 스푸핑 및 재생 공격에 무방비.
  - 해결 방안 : 신규 증설 설비는 보안이 내재된 **OPC(Open Platform Communications)-UA** (TLS(Transport Layer Security) 지원) 및 DNP3 Secure로 전환하고, 기존 설비 전면에는 범용 IPsec(Internet Protocol Security) 암호화 래퍼 게이트웨이 배치.
- **PLC 펌웨어 변조** 및 무중단 공정으로 인한 보안 패치 불가 :
  - 한계점 : 24시간 365일 가동되는 연속 공정 특성상 취약점이 발견되어도 재부팅이 수반되는 펌웨어 패치를 1년에 한 번 있는 오버홀(정기보수) 전까지 적용 불가.
  - 해결 방안 : **산업용 차세대 침입방지시스템** (IPS, Intrusion Prevention System)을 통해 네트워크 단에서 취약점 악용 패킷을 사전에 걸러내는 **가상 패칭** (Virtual Patching) 구현.
- 유지보수 업체의 비인가 원격 접속 및 휴대용 USB(Universal Serial Bus) 악성코드 반입 :
  - 한계점 : 공정 설비 유지보수를 위해 원격 벤더가 백도어를 열어두거나 엔지니어의 감염된 노트북/USB를 제어망에 직접 연결하여 감염 전파.
  - 해결 방안 : 공정망 반입 PC(Personal Computer)/USB에 대한 물리적 검사 키오스크 의무화, 원격 유지보수 시 전용 ZTNA(Zero Trust Network Access) 바스티온 호스트 경유 및 세션 무조건 녹화.

## Ⅴ. 산업제어시스템(ICS) 보안 적용 및 발전을 위한 기술사적 제언

- 국제 표준 **ISA/IEC 62443** 기반 보안 거버넌스 수립 : 제어시스템 보안 요구사항을 컴포넌트(Part 4-2)부터 시스템(Part 3-3), 조직 프로세스(Part 2-1)까지 단계별 인증 획득.
- 공정 센서 텔레메트리 기반 **물리 이상 징후 탐지** (Process Anomaly Detection) : 네트워크 패킷뿐 아니라 화학 반응 압력, 모터 회전수, 온도 데이터의 이상 패턴을 학습하는 물리 AI(Artificial Intelligence) 탐지 모델 도입.
- **주요정보통신기반시설** 취약점 분석·평가 정례화 : 정보통신기반 보호법에 의거하여 매년 전력, 가스, 수자원 제어망에 대한 기술적·관리적 취약점 전수 진단 및 재해복구 모의훈련 수행.
