---
title: "Mirai 봇넷"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. Mirai 봇넷의 개요

- 개념 : 2016년 오리지널 Mirai 악성코드의 소스코드가 공개된 이후, 전 세계 사이버 범죄자 및 위협 행위자들에 의해 다양한 CPU(Central Processing Unit) 아키텍처 지원, 신규 **원격 코드 실행** (RCE, Remote Code Execution) 제로데이 취약점 통합, **P2P(Peer-to-Peer) 기반 분산 C2**(Command and Control) 체계로 급격히 진화한 악성 IoT(Internet of Things) 봇넷 생태계 및 파생 변종군.
- 배경 및 필요성 : 원작자의 깃허브 소스코드 유출로 진입 장벽이 낮아졌으며, 공격자들은 단순 Telnet 기본 계정 대입의 한계를 극복하기 위해 엔터프라이즈 라우터, IP(Internet Protocol) 카메라, NAS(Network-Attached Storage)의 최신 웹 취약점을 결합하여 감염 속도와 지속성을 비약적으로 향상시킴.
- 핵심 목적 : **중앙 C2 서버 차단** (Sinkholing)을 회피하고 엔터프라이즈 네트워킹 장비까지 공격 표면을 확장하여, 테라비트(Tbps) 급의 초강력 **분산 서비스 거부** (DDoS, Distributed Denial of Service) 및 랜섬웨어 유포 인프라를 구축.

## Ⅱ. Mirai 봇넷의 핵심 아키텍처 및 동작 메커니즘

Mirai 변종들은 Satori, Okiru, Echobot, Mozi 등으로 분화 발전하였으며, 중앙 집중형 C2 구조에서 탈중앙 분산 해시 테이블(DHT) 기반 P2P 봇넷으로 구조적 진화를 달성함.

```text
[ Mirai 봇넷의 진화 계보 및 P2P(Mozi) 아키텍처 전환 ]

 [ 1세대: 오리지널 Mirai (2016) ]
  * 침투: Telnet (포트 23/2323) 기본 패스워드 사전 대입
  * 구조: 중앙 집중식 C2 서버 (IP/도메인 차단 시 무력화)
               |
               v (소스코드 공개 및 진화)
 [ 2세대: 복합 취약점 결합 변종 (2017~2019) ]
  * Satori : UPnP 제로데이(CVE-2017-17215) 결합, 자율 웜(Worm) 전파
  * Okiru  : ARC 임베디드 프로세서 최초 감염 지원
  * Echobot: 50개 이상의 다양한 엔터프라이즈 RCE 취약점 동시 탑재
               |
               v (탈중앙화 및 탐지 회피)
 [ 3세대: Mozi 및 현대 P2P 봇넷 (2020~현재) ]
  * 침투: 최신 IoT/방화벽 웹 RCE + 약한 계정 복합 익스플로잇
  * C2 체계: 중앙 서버 없음! BitTorrent DHT(분산해시테이블) 기반 P2P
  
  [ P2P 봇 노드 A ] <====== (DHT 통신) ======> [ P2P 봇 노드 B ]
         \                                             /
          +================ (DHT 통신) ===============+
                                   |
                                   v
             [ 암호학적 ECDSA 서명 검증을 통한 공격 명령 동기화 ]
             * 중앙 서버가 없어 싱크홀링(Sinkholing) 원천 불가능!
```

- **Satori(Okiku) 변종** : Huawei 라우터의 제로데이 취약점(UPnP SOAP 버그)을 통합하여 사전 대입 없이도 수 시간 만에 수십만 대를 자율 감염시키는 웜(Worm) 전파 능력 탑재.
- **Echobot 변종** : 오라클 웹로직, 스프링 프레임워크, 감시 카메라 등 50여 개 이상의 방대한 멀티 플랫폼 취약점을 모듈식으로 결합하여 기업 내부망까지 침투.
- **Mozi 봇넷 (P2P 혁신)** : 중앙 C2 서버를 전면 제거하고 BitTorrent의 분산 해시 테이블(DHT) 프로토콜을 통신망으로 사용하여 C2 도메인 차단 방어를 완벽히 무력화.
- 암호학적 명령 검증 : P2P 네트워크에서 타 해커가 C2를 가로채지 못하도록 봇마스터의 개인키로 서명된 **ECDSA**(Elliptic Curve Digital Signature Algorithm) 서명이 포함된 명령만 실행하도록 하드닝.

## Ⅲ. Mirai 봇넷의 세부 구성 요소 및 비교 분석

| 비교 항목 | **오리지널 Mirai** | **Satori 변종** | **Mozi 봇넷** |
| --- | --- | --- | --- |
| 등장 시기 | 2016년 | 2017년 | 2019년~현재 |
| 주요 침투 수단 | Telnet 하드코딩 기본 계정 대입 | 라우터 UPnP 제로데이 RCE 취약점 | 다중 웹 RCE 취약점 + DHT P2P 전파 |
| C2 아키텍처 | 중앙 집중형 C2 서버 | 중앙 집중형 C2 서버 | 완전 탈중앙 BitTorrent DHT P2P |
| 차단 난이도 | 쉬움 (C2 도메인 싱크홀링) | 중간 (C2 IP 차단) | 극도로 어려움 (P2P 노드 전수 차단 필요) |
| 타깃 기종 | DVR, CCTV(Closed-Circuit Television), 단순 공유기 | 가정용 고속 라우터 | 기업용 게이트웨이, 라우터, NAS, IoT 전반 |

- Mirai 변종들은 단순 스크립트 키디 수준을 넘어 국가급 위협 행위자들의 사이버 무기로 활용되고 있으며, P2P 아키텍처 도입으로 네트워크 수준의 단일 차단이 불가능해짐.

## Ⅳ. Mirai 봇넷의 주요 한계점 및 해결 방안

- P2P DHT 기반 C2 통신의 중앙 차단(Sinkholing) 불가 :
  - 한계점 : 단일 C2 IP나 도메인이 존재하지 않고 수만 대의 감염 봇이 상호 C2 역할을 분담하므로 DNS(Domain Name System) 싱크홀링이나 방화벽 IP 차단 무력화.
  - 해결 방안 : DHT 트래픽 패턴 분석을 통한 악성 노드 식별, P2P 네트워크에 위조 노드를 투입하여 라우팅 테이블을 오염시키는 Sybil 방어 기법 연구.
- 엔터프라이즈 네트워킹 장비의 펌웨어 제로데이 악용 확산 :
  - 한계점 : 저가 IoT뿐만 아니라 기업용 방화벽, VPN(Virtual Private Network) 게이트웨이의 취약점을 결합하여 기업 내부망 침투 거점(Footprint)으로 악용.
  - 해결 방안 : 공격 표면 관리(ASM)를 통한 외곽 노출 장비 전수 점검 및 벤더 보안 권고안 발표 즉시 긴급 패치 적용.
- 광범위한 이종 프로세서 지원으로 분석 난이도 급증 :
  - 한계점 : MIPS, ARM, SuperH, ARC 등 리버스 엔지니어링 도구가 취약한 이종 아키텍처 바이너리로 컴파일되어 신속한 악성코드 디스어셈블리 지연.
  - 해결 방안 : 멀티 아키텍처를 에뮬레이션(QEMU) 지원하는 자동화된 클라우드 샌드박스 동적 분석 파이프라인 가동.

## Ⅴ. Mirai 봇넷 적용 및 발전을 위한 기술사적 제언

- ISP(Internet Service Provider) 수준의 BGP(Border Gateway Protocol) Flowspec 기반 대규모 트래픽 차단 공조 : 초대형 볼륨 공격 발생 시 통신 사업자 백본망에서 악성 패킷의 특성을 정의한 BGP Flowspec 룰을 즉각 전파하여 경계선에서 공격 트래픽 흡수.
- IoT 기기 펌웨어 보안 인증제도(KISA(Korea Internet & Security Agency) IoT 보안인증) 강화 : 공장 출하 단계부터 기본 패스워드 제거, Secure Boot, 서명된 펌웨어 업데이트가 검증된 제품만 국내 유통을 허용하는 제도적 통제.
- P2P 통신 프로토콜에 대한 통계적 이상 트래픽 탐지(NDR, Network Detection and Response) 구축 : 사내 업무망 및 IDC(Internet Data Center) 내에서 BitTorrent DHT 트래픽이 비정상적으로 발생하는 단말을 실시간 탐지하여 즉시 네트워크 격리.
