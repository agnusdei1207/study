---
sidebar:
  order: 36
  label: "036. WebRTC"
  badge:
    text: "서브"
    variant: note
title: "WebRTC(Web Real-Time Communication)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-network"
weight: 36
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "서브"
  question_no: "036"
---

## 지식 로드맵 내 현재 위치

지식 위치: 네트워크 → 실시간 브라우저 통신 → **WebRTC**

## 30초 인출

- 본질: **WebRTC(Web Real-Time Communication)** : 브라우저·응용에서 실시간 오디오·영상·데이터 통신을 지원하는 웹 API와 프로토콜 체계
- 메커니즘: 응용의 signaling으로 SDP 교환 → ICE로 통신 경로 확인 → DTLS-SRTP 미디어·SCTP 데이터 통신
- 통찰: 별도의 플러그인 설치 없이 웹 브라우저 간에 오디오, 비디오 및 임의의 데이터 청크를 P2P로 직접 실시간 교환할 수 있도록 W3C 표준 자바스크립트 API와 IETF 통신 프로토콜을 결합한 개방형 웹 실시간 통신 기술임.

<details>
<summary>핵심 용어</summary>

- **WebRTC(Web Real-Time Communication)** : 실시간 미디어·데이터 연결을 위한 웹 API와 관련 통신 체계
- **Signaling(시그널링)** : 세션 설명과 ICE 후보를 교환하는 응용 경로; WebRTC 표준이 특정 signaling 전송 프로토콜을 정하지 않음
- **SDP(Session Description Protocol)** : 세션·미디어 속성을 표현하는 형식; 자체적으로 미디어를 전달하지 않음
- **ICE(Interactive Connectivity Establishment)** : 후보 주소·포트를 시험해 통신 경로를 찾는 NAT 통과 프레임워크
- **STUN(Session Traversal Utilities for NAT)** : NAT 환경의 주소 정보를 파악하고 연결성 검사를 지원하는 프로토콜
- **TURN(Traversal Using Relays around NAT)** : 직접 연결이 어려울 때 미디어·데이터를 중계하는 릴레이 프로토콜
- **DTLS-SRTP(Datagram Transport Layer Security–Secure Real-time Transport Protocol)** : WebRTC 미디어 전송 보안에 쓰이는 키 교환·보호 구조
- **SCTP(Stream Control Transmission Protocol)** : WebRTC 데이터 채널의 신뢰성 있는 메시지 전달에 사용되는 전송 프로토콜
- **SFU(Selective Forwarding Unit)** : 참가자 미디어를 선택·전달하는 다자 통화 서버 구조

</details>

---

## 2~4교시 예상문제 (25점)

> 웹 기반 실시간 멀티미디어 통신 기술인 WebRTC(Web Real-Time Communication)의 개념, 핵심 3대 JS API, NAT 통과 메커니즘(ICE, STUN, TURN) 및 다자간 통신 아키텍처(Mesh, MCU, SFU)를 비교 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. WebRTC(Web Real-Time Communication)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 웹 브라우저 간에 별도의 추가 플러그인이나 외부 소프트웨어 설치 없이 실시간으로 음성, 영상 미디어 스트림 및 양방향 데이터를 P2P(Peer-to-Peer)로 전송하는 오픈소스 웹 표준 기술 |
| 목적 | 액티브X 및 전용 플러그인 종속 탈피, 초저지연(500ms 미만) 화상회의, 원격 교육, 클라우드 게임 및 브라우저 간 실시간 데이터 공유 |

## Ⅱ. WebRTC(Web Real-Time Communication)의 특징

| 특징 | 상세 내용 |
|---|---|
| 플러그인 프리 | 크롬, 사파리, 엣지 등 모든 최신 표준 브라우저에 기본 내장되어 즉각적인 브라우저 통신 가능 |
| P2P 직접 미디어 전송 | 중앙 미디어 서버 경유 없이 단말 간 직접 암호화 전송하여 서버 대역폭 비용 절감 및 지연 극소화 |
| 강력한 보안 내장 | 시그널링과 미디어 전송 전 구간에 DTLS(데이터그램 TLS) 및 SRTP(보안 실시간 전송) 암호화 강제 |
| 유연한 다자간 확장 | P2P 메시(Mesh) 외에도 미디어 서버 기반의 SFU(Selective Forwarding Unit) 아키텍처 연계 지원 |

## Ⅲ. WebRTC(Web Real-Time Communication)의 체계·프로세스

**WebRTC P2P 연결 수립 절차 및 NAT 통과 아키텍처**

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        [ WebRTC 연결 수립 및 ICE 프레임워크 ]          │
│                                                                        │
│   [ 브라우저 A ]             [ 시그널링 서버 (WebSocket) ]   [ 브라우저 B ] │
│         │                               │                     │        │
│         ├─── 1. SDP Offer 전송 ────────►│                     │        │
│         │    (코덱, 해상도 사양)        ├──── 2. SDP Offer ──►│        │
│         │                               │                     │        │
│         │                               │◄─── 3. SDP Answer ──┤        │
│         │◄── 4. SDP Answer 수신 ────────┤    (수락 코덱 사양) │        │
│         │                               │                     │        │
│         ▼ [ 5. ICE Candidate 수집 (STUN / TURN 서버 질의) ]   ▼        │
│         │                               │                     │        │
│         ├─── 6. 공인 IP/Port 후보 교환 ─►│                     │        │
│         │                               ├──── 7. 후보 교환 ──►│        │
│         │                                                     │        │
│         ▼                                                     ▼        │
│   ══════════ P2P DTLS-SRTP 직접 미디어 스트림 암호화 전송 ══════════════   │
│   (P2P 직접 연결 실패 시 클라우드 TURN 릴레이 서버를 통해 중계 전송)    │
└────────────────────────────────────────────────────────────────────────┘
```

| 3대 핵심 JavaScript API | W3C 표준 명칭 | 핵심 기능 및 역할 |
|---|---|---|
| **미디어 캡처** | `getUserMedia()` | 사용자 단말의 카메라, 마이크 하드웨어에 접근하여 로컬 오디오/비디오 스트림 획득 |
| **피어 연결** | `RTCPeerConnection` | SDP 협상, NAT 통과(ICE), 코덱 인코딩/디코딩, 패킷 손실 복구 등 E2E 연결 관리 |
| **양방향 데이터** | `RTCDataChannel` | 브라우저 간 임의의 텍스트, 바이너리 데이터를 SCTP 기반으로 초저지연 양방향 직접 전송 |

## Ⅳ. WebRTC(Web Real-Time Communication)의 종류·비교

| 비교 항목 | 메시 (Mesh / P2P) | MCU (Multipoint Control Unit) | SFU (Selective Forwarding Unit) |
|---|---|---|---|
| **동작 방식** | 각 단말이 모든 참가자와 1:1 연결 | 서버가 모든 영상을 단일 화면으로 믹싱 | 서버가 영상을 믹싱 없이 선별 라우팅 |
| **서버 부하** | 서버 불필요 (시그널링만 수행) | **극심 (비디오 디코딩/인코딩 CPU 부하)**| **낮음 (단순 패킷 복제 및 포워딩)** |
| **단말 업링크 대역폭**| N-1개 업로드 필요 (부하 극심) | 단 1개 스트림만 업로드 | **단 1개 스트림만 업로드 (최적)** |
| **단말 다운링크 대역폭**| N-1개 다운로드 | **단 1개 믹싱 스트림 다운로드** | N-1개 다운로드 (Simulcast 최적화) |
| **지연 시간** | 최저 (P2P 직접 전송) | 높음 (서버 트랜스코딩 지연 발생) | **매우 낮음 (즉각 패킷 포워딩)** |
| **주 적용 분야** | 1:1 통화, 3~4인 소규모 통화 | 레거시 화상회의 시스템, 저사양 단말 | **대규모 다자간 화상회의 (Zoom, Meet)**|

## Ⅴ. WebRTC(Web Real-Time Communication)의 한계와 방안

| 한계 | 방안 |
|---|---|
| 기업 내부 대칭형 NAT(Symmetric NAT) 및 엄격한 아웃바운드 방화벽 환경에서 P2P 직접 연결(Direct Media) 실패율 급증 | 글로벌 분산 TURN(Traversal Using Relays around NAT) 릴레이 서버 팜 구축 및 클라우드 지리적 최적 라우팅 |
| 1:N 또는 N:M 다자간 영상회의 시 메시(Mesh) 구조 연결 시 단말의 업링크 대역폭과 인코딩 CPU 부하가 O(N)으로 폭증하여 단말 다운 | 클라우드 미디어 서버 기반 SFU(Selective Forwarding Unit) 아키텍처 도입으로 단말 업링크 1회 전송 및 동적 Simulcast 적응형 해상도 분배 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
엔터프라이즈 화상회의 플랫폼 구축 시, 네트워크 대역폭 변동에 적응하기 위해 송신측에서 단일 영상을 고·중·저 3가지 해상도로 동시 인코딩 송출하는 사이멀캐스트(Simulcast)를 적용하고, SFU 서버가 수신측 단말의 네트워크 상태에 따라 최적 해상도를 동적 스위칭하도록 구성.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ SFU 기반 대규모 화상회의 사이멀캐스트 (Simulcast) 스트리밍 구조 ]   │
│                                                                        │
│   [ 발표자 단말 ]                                                      │
│     ├─── High (1080p, 2.5Mbps) ──┐                                     │
│     ├─── Medium (720p, 1.0Mbps) ─┼──► [ SFU 미디어 서버 ]              │
│     └─── Low (360p, 0.3Mbps) ────┘           │                         │
│                                              ├─► [ 단말 A (초고속 광랜) ]│
│                                              │   - High 스트림 수신    │
│                                              ├─► [ 단말 B (무선 Wi-Fi) ]│
│                                              │   - Medium 스트림 수신  │
│                                              └─► [ 단말 C (불안정 모바일)│
│                                                  - Low 스트림 수신     │
│   (서버 재인코딩 부하 없이 각 수신자 대역폭 맞춤형 최적 품질 보장 성공) │
└────────────────────────────────────────────────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| NAT 통과 기술 | 핵심 메커니즘 | 통과 성공률 | 서버 비용 발생 |
|---|---|---|---|
| **STUN (RFC 5389)** | 단말의 공인 IP와 Port 번호를 반환 | 약 80% (대칭형 NAT 통과 불가) | 극소 (단순 UDP 반사) |
| **TURN (RFC 5766)** | 통과 불가 시 클라우드 릴레이 서버가 패킷 중계 | **100% 완벽 통과 보장** | **높음 (모든 미디어 트래픽 대역폭)**|
| **ICE (RFC 8445)** | STUN과 TURN을 우선순위별로 자동 조합 시도 | 최적 경로 자동 선출 | STUN 실패 시에만 TURN 과금 |

## 출제 이력과 검증 출처

- W3C Recommendation: WebRTC 1.0: Real-Time Communication Between Browsers
- IETF RFC 8825: Overview: Real-Time Communication in World-Wide-Web Browsers
- IETF RFC 8445: Interactive Connectivity Establishment (ICE)

## 연결 토픽

- 상위 토픽: [017 OSI 7 계층](./017_osi_7_layer.md)
- 연관 토픽: [034 SCTP](./034_sctp.md), [007 TCP 혼잡 제어](./007_tcp_congestion_control.md)
