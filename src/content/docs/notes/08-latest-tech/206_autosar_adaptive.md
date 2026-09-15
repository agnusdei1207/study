---
sidebar:
  order: 206
  label: "206. AUTOSAR Adaptive Platform"
  badge:
    text: "기출 · 70%"
    variant: note
title: "AUTOSAR Adaptive Platform"
date: "2026-09-15T11:50:00+09:00"
tags:
  - "notes-latest_tech"
weight: 206
extra:
  question_no: "206"
  source_status: "기출"
  source_history: "138회"
  priority: 70
  priority_note: "AUTOSAR Adaptive 서비스 구조가 최근 출제됨"
---

## Ⅰ. 개요

- **정의**: 고성능 차량용 컴퓨팅(HPC) 환경에서 멀티코어 프로세서와 POSIX 운영체제를 기반으로 C++14 언어와 서비스 지향 아키텍처(SOA)를 통해 애플리케이션을 동적 프로세스로 실행·관리하는 개방형 전장 소프트웨어 표준 플랫폼
- **배경 및 필요성**: 정적 컴파일 및 마이크로컨트롤러(MCU) 중심의 기존 AUTOSAR Classic Platform은 자율주행, 커넥티드 서비스, 고성능 인포테인먼트가 요구하는 대규모 멀티코어 연산, 런타임 동적 프로세스 스케줄링, 기가비트 이더넷 통신 및 무선 소프트웨어 업데이트(OTA)를 수용할 수 없음에 따라, 고성능 프로세서와 동적 서비스 확장을 지원하기 위해 도입

## Ⅱ. 특징

- **POSIX 기반 프로세스 격리**: POSIX PSE51 준수 OS 위에서 독립된 가상 주소 공간을 갖는 멀티프로세스로 구동되어 단일 앱 결함의 시스템 전파를 원천 차단
- **서비스 지향 통신 (SOA)**: `ara::com` 미들웨어를 통해 컴파일 시점의 정적 결합을 탈피하고 런타임 서비스 탐색(SOME/IP, DDS) 및 동적 바인딩 지원
- **플랫폼 수명주기 및 헬스 관리**: `ara::exec`를 통한 상태 머신 기반 실행 관리, `ara::phm`을 통한 논리적/시간적 헬스체크, `ara::ucm`을 통한 개별 앱 단위 무중단 OTA 배포 지원

## Ⅲ. 구조 및 구성요소

```text
[AUTOSAR Adaptive Platform 레이어드 아키텍처]
├── [Adaptive Applications 계층]
│   ├── [자율주행 인지·판단 앱] (Deep Learning, 센서 퓨전)
│   └── [커넥티드/클라우드 앱] (V2X 통신, 차량 텔레메틱스)
├── [ARA (AUTOSAR Runtime for Adaptive Applications)]
│   ├── [ara::com (통신 관리)] (SOME/IP, DDS 기반 서비스 지향 통신)
│   ├── [ara::exec (실행 관리)] (매니페스트 기반 프로세스 생명주기 관리)
│   ├── [ara::phm (플랫폼 건강 관리)] (워치독, 데드라인, 논리적 실행 순서 감시)
│   ├── [ara::ucm (업데이트 및 구성 관리)] (OTA 패키지 검증, 설치 및 롤백)
│   ├── [ara::crypto (암호화 관리)] (X.509 인증서, SecOC, 키 저장소 연동)
│   └── [ara::per (영속성 관리)] (비휘발성 플래시 데이터 안전 저장)
└── [기반 시스템 계층 (Operating System)]
    ├── [POSIX PSE51 규격 OS] (Linux, QNX, PikeOS 등 독립 가상 주소 공간)
    └── [고성능 멀티코어 SoC/HPC] (ARM Cortex-A, x86_64 멀티코어, NPU/GPU)
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 계층/구성요소 | 세부 구성요소 | 핵심 역할 |
|:---|:---|:---|
| 애플리케이션 계층 | Adaptive Applications (C++14/17) | 자율주행 궤적 계획, 영상 객체 인식, V2X 협력 주행 등 비즈니스 로직 수행 |
| ara::com | SOME/IP, DDS, IPC | 분산 네트워크 간 서비스 인스턴스 검색(FindService), 이벤트 구독 및 원격 메서드 호출 |
| ara::exec | Execution Management, State Management | 머신 상태/기능 그룹 상태에 따른 프로세스 생성(fork/exec), 리소스 제한(cgroups) 통제 |
| ara::phm | Platform Health Management | 슈퍼바이저 워치독, 실행 데드라인 시간 감시, 논리적 체크포인트 순서 검증 |
| ara::ucm | Update and Configuration Management | 개별 Adaptive 애플리케이션 패키지 무결성 검증, A/B 파티션 업데이트 및 롤백 |
| 기반 OS 및 HW | POSIX OS (QNX, Linux), Multi-core SoC | 하이퍼바이저 가상화, 프로세스 메모리 보호(MMU), 하드웨어 가속기(NPU) 자원 제공 |

## Ⅳ. 흐름도

```text
[UCM 패키지 수신 및 서명 검증] (① ara::ucm이 OTA 패키지를 수신하여 ara::crypto로 전자서명 검증)
│
▼
[매니페스트 파싱 및 비활성 슬롯 설치] (② Execution Manifest를 파싱하고 신규 애플리케이션 바이너리를 타깃 영역에 기록)
│
▼
[ara::exec 실행 관리자 기동] (③ 실행 상태 머신(Machine State) 전환에 따라 프로세스를 포크(fork)하여 독립 가상 메모리에 적재)
│
▼
[ara::com 서비스 탐색 및 바인딩] (④ 애플리케이션이 FindService로 인스턴스를 탐색하고 SOME/IP 프록시-스켈레톤 바인딩 체결)
│
▼
[서비스 통신 및 ara::phm 헬스체크 보고] (⑤ 이벤트/메서드 기반 통신을 수행하며 PHM에 주기적 체크포인트 생존 신호 보고)
│
▼
[이상 감지 및 복구/안전 상태 전환] (⑥ 데드라인 초과 또는 메모리 크래시 감지 시 프로세스 재시작 또는 차량 안전 정지(Safe-State) 발동)
```

- 분기 결과: 정상 서비스 운용 시 연속 통신 및 헬스 핑 유지, 프로세스 크래시 시 재시작(3회) 시도 후 지속 실패 시 안전 축퇴 모드 전환

## Ⅴ. 종류 및 비교

| 구분 | AUTOSAR Classic Platform | AUTOSAR Adaptive Platform | 혼합(Hybrid) E/E 아키텍처 |
|:---|:---|:---|:---|
| 실행 타깃 하드웨어 | 마이크로컨트롤러 (MCU, 16/32비트) | 고성능 마이크로프로세서 (MPU/HPC, 64비트) | 중앙 HPC (Adaptive) + 조널 제어기 (Classic) |
| 운영체제 규격 | OSEK/VDX 정적 스케줄링 RTOS | POSIX PSE51 준수 OS (QNX, Embedded Linux) | 도메인별 RTOS 및 POSIX OS 가상화 병행 |
| 통신 패러다임 | 신호(Signal) 기반 CAN/LIN 주기 통신 | 서비스(Service) 기반 SOME/IP, DDS 통신 | 이더넷 백본(SOME/IP)과 CAN-FD 게이트웨이 연계 |
| 메모리 아키텍처 | 단일 평면 물리 주소 공간 (공유 메모리) | 가상 주소 공간 분리 (MMU 기반 메모리 격리) | 존 제어기는 물리 주소, 중앙 HPC는 MMU 보호 |
| 실시간성 특성 | 수 마이크로초 ($\mu$s) 확정적 하드 실시간 | 밀리초 (ms) 단위 소프트/펌 실시간성 | 제어 루프는 하드 실시간, 인지는 소프트 실시간 |
| 주 활용 분야 | 엔진/모터 제어, 에어백, 브레이크, 섀시 | 자율주행(AD), 디지털 콕핏, 텔레매틱스 게이트웨이 | 완성형 SDV (차세대 프리미엄 전기차/자율차) |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 효과 |
|:---|:---|:---|
| 비결정론적 POSIX OS 스케줄링으로 인한 자율주행 제어 루프 데드라인 위반 | SCHED_FIFO 우선순위 스케줄링 및 코어 격리(CPU Pinning/Isolcpus) 적용 | 실시간성 보장 및 최대 지연 시간(Worst-Case Latency) 바운딩 |
| 런타임 서비스 탐색 지연으로 인한 초기 시동(Cold Boot) 시 통신 먹통 | 서비스 사전 정의(Static Service Matching) 및 SOME/IP 로컬 캐싱 구성 | 시동 후 통신 수립 시간 수백 밀리초 이내 단축 |
| 이종 벤더 간 Adaptive 플랫폼 스택 구현 차이로 인한 상호운용성 결함 | 표준 AUTOSAR XML(ARXML) 매니페스트 준수 및 사전 적합성(Conformance) 테스트 수행 | 멀티 티어 소프트웨어 컴포넌트 통합 비용 최소화 |

## Ⅶ. 결론

- **기술 위상/발전**: SDV의 중앙 집중형 E/E 아키텍처를 지탱하는 핵심 개방형 플랫폼이며, 최근에는 ROS2 자율주행 스택, SOAFEE 클라우드 네이티브 컨테이너 가상화와 융합하여 차량-클라우드 연속성을 제공하는 플랫폼으로 진화 중
- **실무 적용/통제**: 마이크로초 단위 하드 실시간 제어는 Classic에 유지하고 인지·판단·OTA는 Adaptive로 분리하는 하이브리드 아키텍처를 구성하되, SOME/IP 게이트웨이 정합성과 ISO 26262 ASIL-D 기능안전 분리를 필수 수립할 필요
