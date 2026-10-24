---
title: "네트워크 스캐닝(Network Scanning)"
author: "agnusdei1207"
date: "2026-10-24T23:10:07+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 네트워크 스캐닝(Network Scanning), 포트 스캐닝(Port Scanning), SYN 스캔, TCP Connect 스캔, 스텔스 스캔(Stealth Scan)
- OS 핑거프린팅(OS Fingerprinting), 배너 그래빙(Banner Grabbing), 공격 표면 관리(ASM), EASM, 포트 노킹(Port Knocking), 허니팟(Honeypot)

## Ⅰ. 네트워크 스캐닝의 개요

- 핵심 요약 : 대상 호스트의 패킷 응답을 분석해 활성 호스트, 열린 포트, 서비스, 운영체제를 식별하는 정찰 기법.
- 개념 : 대상 네트워크와 호스트에 TCP(Transmission Control Protocol), UDP(User Datagram Protocol), ICMP(Internet Control Message Protocol) 패킷을 보내 응답의 유형과 상태를 분석하여, 활성 호스트, 개방 포트, 구동 서비스, 운영체제와 알려진 취약점을 식별하는 **정찰** (Reconnaissance) 기법.
- 배경 및 필요성 : 사이버 킬 체인의 초기 단계인 정찰에서 공격자는 침투 접점을 찾아야 하며, 방어자도 자산 식별과 공격 표면 관리(ASM, Attack Surface Management)를 위해 같은 기술을 사용함.
- 주요 목적 : 네트워크 공격 표면을 전수 식별하고, 불필요하게 외부에 열린 포트와 취약한 서비스 버전을 찾아 차단과 하드닝을 수행하는 것.

## Ⅱ. 네트워크 스캐닝의 특징 및 장점

- 핵심 요약 : 호스트 탐색, 포트 스캐닝, 배너 확인, OS 판별이 단계적으로 이어지는 파이프라인 구조.

1. **호스트 탐색** (Host Discovery, Ping Scan) : ICMP 등으로 응답하는 호스트를 식별 → 스캔 대상을 줄여 점검 시간 단축.
2. **포트 스캐닝** (Port Scanning) : TCP Connect, SYN, FIN·NULL·Xmas 등 방식으로 열린 포트를 판별 → 노출 서비스 목록 확보.
3. **배너 그래빙** (Banner Grabbing) : 열린 포트에 접속해 서비스 종류와 버전 문자열을 수집 → 알려진 취약점과 대조.
4. **OS 핑거프린팅** (OS Fingerprinting) : 초기 시퀀스 번호(ISN, Initial Sequence Number) 생성 방식, TTL(Time to Live), TCP 윈도우 크기, 옵션 값의 차이로 운영체제를 추정 → 공격 대상의 환경 파악.

```text
[ TCP Connect 스캔 (완전 연결) ]

스캐너 → 대상 : SYN
대상 → 스캐너 : SYN/ACK (포트 열림)
스캐너 → 대상 : ACK (연결 완료)
스캐너 → 대상 : RST (종료, 로그 남음)
```

```text
[ TCP SYN 스캔 (반개방) ]

스캐너 → 대상 : SYN
대상 → 스캐너 : SYN/ACK (포트 열림)
스캐너 → 대상 : RST (연결 수립 전 중단)
→ 애플리케이션 로그에 기록되지 않는 경우가 많음
```

## Ⅲ. 네트워크 스캐닝의 구조 (흐름)

- 핵심 요약 : 정상 연결 절차를 따르지 않는 비정상 플래그 기법들이 응답 유무의 차이로 포트 상태를 추정하는 구조.
- **스텔스 스캔** (Stealth Scan) : 연결 수립 절차를 완료하지 않아 애플리케이션 계층의 기록을 줄이는 방식의 총칭.
- **FIN·NULL·Xmas 스캔** : RFC(Request for Comments) 793의 응답 규칙을 이용하는 역발상 스캔으로, 닫힌 포트는 RST로 응답하고 열린 포트는 무응답으로 처리함. 다만 Windows 계열 구현은 열림과 닫힘 모두 RST로 응답하여 판별이 어려움.

```text
[ FIN·NULL·Xmas 스캔 흐름 ]

스캐너 → 대상 : 비정상 플래그 패킷
    ↓
열린 포트 : 무응답 (Silent Drop)
닫힌 포트 : RST/ACK 응답
    ↓
Windows 계열은 열림·닫힘 모두 RST 응답
```

## Ⅳ. 네트워크 스캐닝의 비교 분석

- 핵심 요약 : 연결 수립 방식, 로그 흔적, 권한 요건, 방화벽 통과 특성에 따라 스캔 기법의 성격이 구분되는 구조.

비교 대상은 **TCP Connect 스캔** (Open Scan)과 **TCP SYN 스캔** (Half-Open Scan)이며, 나머지 비정상 플래그 기법과 UDP 스캔을 함께 비교한다.

| 비교 축 | TCP Connect | TCP SYN | FIN·NULL·Xmas | UDP |
| --- | --- | --- | --- | --- |
| 연결 수립 | 3-Way Handshake 완료 | 반개방, RST로 종료 | 연결 없음 (비정상 플래그) | 비연결형 (UDP 전송) |
| 서버 로그 | 애플리케이션 로그에 기록 | 대부분 남지 않음 | 남지 않음 | 남지 않음 |
| 실행 권한 | 일반 사용자 가능 | 관리자 권한 필요 (Raw Socket) | 관리자 권한 필요 | 관리자 권한 권장 |
| 방화벽 우회 | 쉽게 탐지되고 차단됨 | 단순 패킷 필터링 일부 우회 | 상태 비저장 방화벽 우회 가능 | 방화벽 통과가 어려움 |
| 스캔 속도 | 상대적으로 느림 | 빠름 | 중간 | 매우 느림 (ICMP 응답 제한) |

- 선택 기준 : 기법마다 로그 흔적과 방화벽 통과 특성이 다르므로, 방어 측은 각 기법이 어떤 로그와 탐지 규칙에 남는지 기준선을 확인해 두는 것이 필요함.

## Ⅴ. 네트워크 스캐닝의 한계와 방안

- 핵심 요약 : 임계치 기반 자동 차단, UDP 응답 제한, 클라우드 사전 승인 요건이 점검의 한계를 만들므로, 점검 설계와 정책 준수로 대응하는 구조.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| **상태 추적 방화벽** (Stateful Inspection)과 IPS(Intrusion Prevention System)의 즉각 차단 | 차세대 방화벽(NGFW, Next-Generation Firewall)이 스캔 임계치를 감지해 출발지 IP를 자동 차단 → 정밀 점검이 중단됨 | 점검 일정과 출발지를 사전에 등록하여 보안 장비의 예외 정책으로 관리하고, 스캔 로그를 점검 기록과 대조 | 점검 중 차단 건수 |
| UDP 스캔의 속도 저하와 신뢰성 한계 | 닫힌 포트에서만 ICMP Port Unreachable이 돌아오고, OS가 ICMP 응답 속도를 제한하여 결과가 불확실함 | DNS(Domain Name System) 53, SNMP(Simple Network Management Protocol) 161, NTP(Network Time Protocol) 123 등 핵심 포트로 대상을 좁히고 서비스별 프로토콜 질의 사용 | 스캔 소요 시간, 응답 누락률 |
| 클라우드 사전 승인 없는 스캔 | CSP(Cloud Service Provider) 인프라에서 승인 없이 스캔하면 공격으로 간주되어 계정이 제한될 위험 | CSP의 모의 진단 정책을 사전에 확인·준수하고, AWS Inspector 같은 클라우드 네이티브 점검 도구로 에이전트 기반 점검 수행 | 승인 절차 준수율 |

## Ⅵ. 네트워크 스캐닝의 기술사적 제언

- 핵심 요약 : 외부 노출 자산을 상시 발견하고, 관리 포트를 은닉하며, 스캔 행위를 조기에 탐지하는 능동 방어 체계로 운영하는 방향.

1. 기업의 외부 노출 자산(도메인, 서브도메인, 공인 IP)을 주기적으로 자동 탐색하는 **EASM** (External Attack Surface Management) 체계를 도입하여, 섀도 IT(Shadow IT)와 승인되지 않은 공개 포트를 정기적으로 찾아내는 것이 바람직하다.
2. SSH(Secure Shell)나 RDP(Remote Desktop Protocol) 같은 관리 포트는 평상시 외부에서 닫아 두고, 사전에 인증된 단일 패킷을 받았을 때만 특정 출발지에 일시적으로 여는 **SPA** (Single Packet Authorization) 방식이나 포트 노킹(Port Knocking)을 검토할 필요가 있다.
3. 사용하지 않는 IP 대역과 포트에 **허니팟** (Honeypot)을 배치하여 스캔 행위를 조기에 감지하고, 공격 원천 IP를 관제 체계에 자동 공유하여 대응 시간을 줄여야 한다.

## Ⅶ. 결론

- 핵심 요약 : 네트워크 스캐닝은 공격자에게는 정찰 수단이고 방어자에게는 노출 자산을 식별하는 점검 수단인 양면적 기술.
- 시사점 : 공격 표면을 상시 관리하는 ASM 체계의 기반으로 스캐닝을 운영하되, 승인된 범위 안에서 정기적으로 수행하는 것이 전제가 되어야 함.
