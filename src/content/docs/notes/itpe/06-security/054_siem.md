---
title: "SIEM(Security Information and Event Management)"
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

## Ⅰ. SIEM(통합 보안관제 및 이벤트 관리)의 개요

- 개념 : 엔터프라이즈 전역의 이기종 IT(Information Technology) 인프라(서버, 네트워크, 보안 장비, 클라우드, 데이터베이스 등)로부터 대용량 로그와 보안 이벤트를 실시간으로 수집·정규화하고, 상관분석(Correlation) 룰과 머신러닝을 통해 위협을 조기 탐지·경보하는 중앙 집중형 보안 빅데이터 플랫폼.
- 배경 및 필요성 : 방화벽, IPS(Intrusion Prevention System), WAF(Web Application Firewall) 등 개별 보안 솔루션이 쏟아내는 수억 건의 파편화된 로그로 인해 전체 **침해 공격 경로** (Cyber Kill Chain)를 조망하지 못하는 관제 사각지대를 해소하기 위해 출현.
- 핵심 목적 : **전사 보안 가시성** (Visibility) 일원화, **지능형 지속 위협** (APT, Advanced Persistent Threat) 상관분석 탐지, 법적 로그 보관 컴플라이언스 준수 및 침해 조사 효율화.

## Ⅱ. SIEM(통합 보안관제 및 이벤트 관리)의 핵심 아키텍처 및 동작 메커니즘

SIEM(Security Information and Event Management)은 데이터 수집 -> 정규화/파싱 -> 상관분석(Rule & ML) -> 경보 및 인시던트 생성 -> 대시보드 및 보고서 출력의 수명주기로 작동함.

```text
[ SIEM의 핵심 데이터 파이프라인 및 상관분석 아키텍처 ]

  [ 분산 로그 소스 (방화벽, AD 이벤트, EDR, 클라우드 감사로그) ]
                               │
                               ▼ 1. 대용량 실시간 수집 (Syslog, Kafka, API)
  +-------------------------------------------------------------+
  | 수집 및 정규화 계층 (Log Parser & Normalization)            |
  |  - 이기종 로그 포맷을 공통 스키마(ECS, OCSF 등)로 매핑      |
  |  - IP, 사용자명, 타임스탬프, 이벤트 코드 표준화             |
  +------------------------------┬------------------------------+
                                 │ 2. 실시간 스트리밍 인덱싱
                                 ▼
  +-------------------------------------------------------------+
  | 상관분석 및 위협 탐지 엔진 (Correlation Engine & UEBA)       |
  |  - 단일 이벤트가 아닌 '복합 시나리오 룰' 매칭               |
  |  - 예: [외부 스캔] -> [로그인 5회 실패] -> [비인가 관리자   |
  |        권한 상승] -> [대량 파일 전송] 시퀀스 탐지!          |
  +------------------------------┬------------------------------+
                                 │ 3. 고신뢰 인시던트 경보
                                 ▼
  [ 관제 대시보드 / SOC 분석가 ] ──> [ SOAR 연동 자동 차단 ]
```

- **대용량 로그 수집 및 저장** : Syslog, Agent, API(Application Programming Interface)를 통해 대량의 **EPS** (Events Per Second) 트래픽을 유실 없이 분산 저장(Elasticsearch, Splunk).
- **로그 정규화** (Normalization) : 제조사마다 제각각인 로그 형식을 단일 공통 데이터 모델(예: OCSF, CEF)로 변환하여 통합 질의 가능.
- **상관분석** (Correlation Analysis) : 서로 다른 장비에서 발생한 이벤트들을 시간, IP(Internet Protocol), 사용자 계정 축으로 결합하여 단일 로그로는 알 수 없는 공격 흐름 추적.
- **위협 인텔리전스** (CTI, Cyber Threat Intelligence) 연동 : 수집된 IP, 해시값이 **악성 평판** (IoC)과 일치하는지 실시간 대조하여 경보 우선순위 자동 조정.

## Ⅲ. SIEM(통합 보안관제 및 이벤트 관리)의 세부 구성 요소 및 비교 분석

| 비교 항목 | 전통적 온프레미스 SIEM | 클라우드 네이티브 SIEM | 차세대 SIEM + UEBA(User and Entity Behavior Analytics) |
| --- | --- | --- | --- |
| 인프라 아키텍처 | 전용 어플라이언스 / 물리 스토리지 | 클라우드 SaaS (Sentinel, Chronicle) | 빅데이터 분산 레이크하우스 |
| 확장성(Scalability) | 스토리지 증설 시 고비용 하드웨어 추가 | 클라우드 오토스케일링 무제한 확장 | 페타바이트급 분산 스트리밍 처리 |
| 분석 메커니즘 | 단순 조건문(if-else) 기반 정적 룰 | 클라우드 탄력 쿼리 + 위협 헌팅 | 정적 룰 + 비지도 머신러닝 행위 분석 |
| 비용 모델 | EPS(초당 이벤트) 기반 라이선스 과금 | 수집 데이터 기가바이트(GB)당 과금 | 엔드포인트 사용자 수 또는 노드 기반 |
| 주요 한계점 | 경보 피로(Alert Fatigue), 클라우드 로그 수집 병목 | 클라우드 데이터 송출(Egress) 비용 | 머신러닝 모델 학습을 위한 초기 기준선 필요 |

- SIEM은 기존의 정적 룰 기반 알람 방식에서 벗어나, **사용자 및 엔티티 행위 분석** (UEBA)과 클라우드 네이티브 빅데이터 분석 엔진을 결합한 차세대 SecOps의 두뇌로 진화함.

## Ⅳ. SIEM(통합 보안관제 및 이벤트 관리)의 주요 한계점 및 해결 방안

- 오탐(False Positive) 알람 폭증으로 인한 관제 요원의 **경보 피로** :
  - 한계점 : 하루에도 수만 건의 무의미한 경보가 발생하여 실제 치명적인 침해 신호가 묻히고 분석가가 탈진하는 현상.
  - 해결 방안 : 머신러닝 기반 경보 중복 제거 및 **위험 점수화** (Risk-based Alerting), SOAR(Security Orchestration, Automation and Response) 연동을 통한 L1 단순 알람 무인 자동 처리.
- 클라우드 전환에 따른 **로그 수집 비용 폭증** (Data Egress Cost) :
  - 한계점 : 멀티 클라우드 환경에서 모든 VPC(Virtual Private Cloud) 및 컨테이너 로그를 온프레미스 SIEM으로 중앙 집결할 때 천문학적인 네트워크 비용 발생.
  - 해결 방안 : **엣지 전처리 필터** (Logstash, Cribl)를 배치하여 불필요한 디버그 로그를 엣지에서 제거하고 중요 보안 이벤트만 압축 선별 전송.
- **암호화 트래픽** (TLS(Transport Layer Security) 1.3) 증가에 따른 페이로드 가시성 상실 :
  - 한계점 : 대부분의 네트워크 트래픽이 종단간 암호화되어 패킷 페이로드를 검사하지 못하고 단순 메타데이터(IP/Port)만 분석하는 한계.
  - 해결 방안 : 엔드포인트 EDR(Endpoint Detection and Response) 텔레메트리(복호화 이전의 시스템 콜)와 DNS(Domain Name System) 쿼리 로그, **TLS 지문** (JA3/JA4) 기반 행동 프로파일링 결합.

## Ⅴ. SIEM(통합 보안관제 및 이벤트 관리) 적용 및 발전을 위한 기술사적 제언

- 공통 보안 스키마 **OCSF** (Open Cybersecurity Schema Framework) 채택 : 벤더 종속적인 로그 형식을 탈피하여 전사 로그를 OCSF 오픈 표준으로 일원화.
- **보안 데이터 레이크** (Security Data Lake) 아키텍처 전환 : 고비용 SIEM 스토리지에는 최근 30일 핫(Hot) 데이터만 보관하고, 장기 보존 로그는 저비용 오브젝트 스토리지(S3 Iceberg)로 계층화.
- **위협 헌팅** (Threat Hunting) 전담 분석 체계 수립 : 알람을 기다리지 않고 MITRE ATT&CK 기법을 기반으로 SIEM 데이터를 능동적으로 뒤져 잠복된 공격자를 색출하는 선제적 관제 수행.
