---
sidebar:
  order: 202
  label: "202. OPC UA 산업 표준 통신 (OPC Unified Architecture)"
  badge:
    text: "기출 · 70%"
    variant: note
title: "OPC UA 산업 표준 통신 (OPC Unified Architecture)"
date: "2026-09-15T11:50:00+09:00"
tags:
  - "notes-latest_tech"
weight: 202
extra:
  question_no: "202"
  source_status: "기출"
  source_history: "137회"
  priority: 70
  priority_note: "OPC UA 정보 모델•보안 통신이 최근 출제됨"
---

## Ⅰ. 개요

- **정의**: 제조 및 산업 자동화 환경에서 이종 설비·시스템 간 데이터의 구문론적(Syntax) 교환을 넘어 객체 지향적 의미론(Semantics), 플랫폼 독립적 통신, 종단 간 다계층 보안을 통합 제공하는 개방형 산업 통신 표준 (IEC 62541)
- **배경 및 필요성**: 다양한 제조사(Siemens, Rockwell, Mitsubishi 등)의 이기종 제어기가 제각기 독점 프로토콜을 사용함에 따른 데이터 사일로와 문맥 상실, DCOM 기반 레거시 OPC의 윈도우 OS 종속성 및 보안 취약점을 극복하고, 현장 센서부터 클라우드 엔터프라이즈까지 단일 의미 체계로 안전하게 직결할 필요

## Ⅱ. 특징

- **시맨틱 정보 모델**: 주소 공간(AddressSpace) 내에 노드·속성·참조를 정의하여 단순 태그 값을 넘어 엔지니어링 단위, 데이터 타입, 장비 계층 관계 등 의미론적 메타데이터를 함께 전달
- **복수 통신 모델 지원**: 일대일 질의응답 및 원격 제어를 위한 세션 기반 Client-Server 모델과 초저지연·다자간 실시간 배포를 위한 PubSub over TSN 모델을 동시 지원
- **플랫폼 독립 및 내재 보안**: 임베디드 OS부터 리눅스, 윈도우, 클라우드까지 범용 실행 가능하며, X.509 인증서 기반 암호화·전자서명·사용자 인가를 프로토콜 자체에 내장

## Ⅲ. 구조 및 구성요소

```text
[OPC UA IEC 62541 통합 아키텍처]
├── [정보 모델 계층 (Information Model Layer)]
│   ├── [주소 공간 (AddressSpace)] (노드, 속성, 참조 관계로 구조화)
│   ├── [노드 클래스 (NodeClasses)] (Object, Variable, Method, DataType)
│   └── [동반 명세 (Companion Specs)] (Euromap, PackML, Robotics 표준 모델)
├── [통신 프로토콜 계층 (Communication Layer)]
│   ├── [Client-Server 세션 모델] (TCP/Binary, HTTPS, WebSockets 기반 요청-응답)
│   └── [PubSub 브로커/브로커리스] (UDP Multicast/TSN 결정론적 전송, MQTT 연계)
└── [보안 아키텍처 계층 (Security Architecture)]
    ├── [보안 채널 (Secure Channel)] (TLS/X.509 인증서 기반 서명 및 암호화)
    └── [사용자 인증/인가] (Anonymous, ID/PW, X.509, JSON Web Token)
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 계층/구성요소 | 세부 구성요소 | 핵심 역할 |
|:---|:---|:---|
| 정보 모델 계층 | AddressSpace, Node, Reference | 물리 설비와 공정을 노드와 객체 지향 링크로 추상화하여 시맨틱 표현 제공 |
| 산업 표준 명세 | Companion Specifications | 반도체, 사출성형(Euromap), 포장(PackML) 등 도메인별 표준 객체 모델 정의 |
| Client-Server 통신 | 세션 관리자, OPC UA TCP/Binary | 점대점 요청-응답, 메소드 원격 호출, 상태 변경 통지(MonitoredItems) 처리 |
| PubSub 통신 | DataSetWriter, DataSetReader, TSN | 브로커리스 UDP 멀티캐스트 또는 MQTT 브로커를 통한 대규모 고속 배포 |
| 보안 인프라 | GDS (Global Discovery Server), PKI | X.509 인증서 발급·폐기·신뢰 목록 배포 및 메시지 암호화/무결성 서명 |

## Ⅳ. 흐름도

```text
[엔드포인트 탐색 요청] (① 클라이언트가 OPC UA 서버의 디스커버리 엔드포인트(/discovery)로 보안 정책 목록 질의)
│
▼
[보안 채널 협상 및 인증서 교환] (② 클라이언트와 서버가 X.509 인증서를 교환하고 암호화 스위트(Basic256Sha256) 협상)
│
▼
[보안 채널 및 세션 수립] (③ 서명/암호화 채널을 개설하고 사용자 자격증명(JWT/인증서)으로 인증 세션 생성)
│
▼
[AddressSpace 노드 탐색 및 구독 요청] (④ Browse 서비스로 객체 트리를 탐색하고 관심 센서 변수에 대해 CreateSubscription 요청)
│
▼
[데이터 샘플링 및 큐잉] (⑤ 서버가 지정된 샘플링 주기(예: 10ms)로 PLC 하드웨어 태그 값을 읽어 모니터링 큐에 적재)
│
▼
[PublishResponse 변경 통지 전송] (⑥ 데이터 변경(DataChange) 또는 이벤트 발생 시 게시 응답 메시지로 클라이언트에 전송)
```

- 분기 결과: 정상 통신 시 실시간 변경 텔레메트리 스트리밍 수신, 세션 만료 또는 서명 불일치 시 보안 연결 즉시 해제 및 재인증 요구

## Ⅴ. 종류 및 비교

| 구분 | OPC UA Client-Server | OPC UA PubSub over TSN | 레거시 Modbus/TCP |
|:---|:---|:---|:---|
| 통신 패러다임 | 점대점 세션 기반 요청-응답 | 발행-구독 (1:N 브로커리스 멀티캐스트) | 마스터-슬레이브 폴링 |
| 실시간성/지연 | 수십 밀리초 (ms) 수준 | 마이크로초 ($\mu$s) 단위 확정적 지연 | 네트워크 부하에 따라 지연 가변 |
| 데이터 표현력 | 완전한 객체 지향 시맨틱 정보 모델 | 인코딩된 바이너리/JSON 데이터셋 | 단순 16비트 레지스터 번호 나열 |
| 보안 메커니즘 | X.509 인증서, 세션 암호화 내장 | 대칭키 기반 보안 그룹 키(SKS) 관리 | 보안 기능 없음 (평문 전송) |
| 주 활용 분야 | SCADA-MES-ERP 상위 계층 연계 | 컨트롤러 간(C2C), 모션 제어 필드버스 | 단순 레거시 계측기 및 센서 연결 |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 효과 |
|:---|:---|:---|
| 설비 제조사별 네임스페이스(Namespace) 및 태그 모델링 불일치 | 산업 도메인별 표준 Companion Specification 채택 및 전사 매핑 사전 구축 | 시맨틱 상호운용성 보장 및 상위 시스템 연동 시간 대폭 단축 |
| 수천 대 설비의 X.509 인증서 만료 및 폐기 미흡으로 통신 단절 리스크 | GDS(Global Discovery Server) 기반 인증서 자동 발급·갱신(Push/Pull) 체계 구축 | 인증서 수작업 갱신 오류 제거 및 무중단 보안 가용성 확보 |
| 클라이언트-서버 폴링 과다로 인한 임베디드 PLC의 CPU 오버헤드 급증 | 상태 변경 통지(MonitoredItems/Publish) 전환 및 고주파 데이터는 PubSub 분리 | 제어기 연산 부하 80% 이상 절감 및 실시간 제어 무결성 유지 |

## Ⅶ. 결론

- **기술 위상/발전**: Industry 4.0 및 스마트 팩토리의 상호운용성을 지탱하는 사실상의 국제 표준 산업 통신 백본이며, 최근에는 TSN(Time-Sensitive Networking) 및 클라우드 MQTT 연계와 결합하여 IT/OT 통합 백본으로 확장 중
- **실무 적용/통제**: 장비 도입 시 도메인별 Companion Specification 준수 여부를 필수 검증하고, 제어 트래픽과 모니터링 트래픽의 전송 모드를 분리하되, GDS를 통한 인증서 수명주기 자동화 거버넌스를 갖출 필요
