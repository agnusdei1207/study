---
title: "WebRTC(Web Real-Time Communication)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. WebRTC(Web Real-Time Communication)의 개요

- **개념** : 웹 브라우저 및 모바일 애플리케이션 간에 별도의 플러그인, 액티브X, 또는 외부 소프트웨어 설치 없이 W3C 자바스크립트 표준 API와 IETF 실시간 통신 프로토콜을 기반으로 오디오, 비디오 및 임의의 데이터(P2P Data Channel)를 실시간 직접 교환하는 오픈소스 웹 표준 기술.
- **배경 및 필요성** : 과거 웹 기반 화상 통신은 Flash나 전용 플러그인 설치가 필수적이어서 보안 취약점과 호환성 문제가 극심했으며, HTTP 기반 스트리밍(HLS, DASH)은 수 초~수십 초의 지연시간이 발생하여 진정한 실시간 상호작용(Sub-second Latency)을 구현하기 어려웠음.
- **핵심 목적** : 500ms 미만의 극초저지연 실시간 양방향 미디어 통신, 브라우저 네이티브 P2P 연결을 통한 서버 대역폭 비용 절감, 전 구간 암호화(DTLS/SRTP)를 통한 강력한 통신 보안성 보장.

## Ⅱ. WebRTC(Web Real-Time Communication)의 핵심 아키텍처 및 동작 메커니즘

WebRTC는 시그널링(SDP 교환), NAT 트래버스(ICE/STUN/TURN), 미디어 스트리밍(SRTP), 데이터 전송(SCTP over DTLS)의 유기적 결합으로 브라우저 간 종단 간 통신을 수립함.

```text
[ WebRTC 종단 간 연결 수립 및 미디어 전송 아키텍처 ]

브라우저 A (Caller)              시그널링 서버 (WebSocket)          브라우저 B (Callee)
      │                                │                                │
      │─── 1. Offer SDP 전송 ─────────>│─── 1. Offer SDP 전달 ─────────>│
      │<── 2. Answer SDP 전달 ─────────│<── 2. Answer SDP 전송 ─────────│
      │                                │                                │
      │ (ICE Candidate 수집: STUN/TURN 서버 조회)                       │
      │─── 3. ICE 후보 교환 ──────────>│─── 3. ICE 후보 교환 ──────────>│
      │                                │                                │
      ▼                                                                 ▼
+-------------------------------------------------------------------------------+
|                    4. P2P 직접 미디어 및 데이터 채널 수립                      |
|                                                                               |
|  [ 브라우저 A ] <===== 직접 P2P (또는 방화벽 시 TURN 릴레이) =====> [ 브라우저 B ]  |
|                                                                               |
|  - 음성/영상 미디어: RTP / SRTP (AES 암호화 미디어 스트림)                    |
|  - 데이터 채널 (RTCDataChannel): SCTP over DTLS (신뢰성/비신뢰성 데이터 전송) |
+-------------------------------------------------------------------------------+
```

- **시그널링(Signaling)** : 통신할 피어 간에 미디어 코덱, 해상도, 암호화 키 정보를 담은 SDP(Session Description Protocol)와 네트워크 주소를 교환하는 절차(WebSocket/SIP 활용, WebRTC 표준 외 영역).
- **ICE(Interactive Connectivity Establishment)** : 복잡한 NAT 및 방화벽 환경에서 피어 간 최적의 통신 경로를 찾아내는 프레임워크로, STUN과 TURN을 통합 제어.
- **STUN(Session Traversal Utilities for NAT)** : 단말이 자신의 공인 IP와 포트 번호를 파악하여 직접 P2P 연결을 시도할 수 있도록 지원하는 경량 프로토콜.
- **TURN(Traversal Using Relays around NAT)** : Symmetric NAT 등 직접 P2P가 원천 불가능한 폐쇄망 환경에서 트래픽을 중계해 주는 폴백(Fallback) 릴레이 서버.
- **SRTP & DTLS 보안** : 모든 음성/영상 미디어는 SRTP로 실시간 암호화되며, 키 교환과 데이터 채널은 DTLS(Datagram TLS)를 통해 보호(보안 암호화 강제 표준).

## Ⅲ. WebRTC(Web Real-Time Communication)의 세부 구성 요소 및 비교 분석

| 비교 항목 | WebRTC (웹 실시간 통신) | HLS / MPEG-DASH (HTTP 스트리밍) | RTMP (레거시 플래시 스트리밍) |
|---|---|---|---|
| **통신 지연 (Latency)**| 200 ~ 500 ms 미만 (초저지연) | 2 ~ 10초 내외 (청크 지연) | 1 ~ 3초 내외 |
| **전송 프로토콜** | UDP 기반 (SRTP, SCTP) | TCP 기반 (HTTP / HTTPS) | TCP 기반 (독자 바이너리) |
| **클라이언트 요구** | 표준 브라우저 내장 (무설치) | 표준 브라우저 HTML5 비디오 | 전용 플러그인 또는 클라이언트 |
| **통신 모델** | P2P 및 미디어 서버 (SFU/MCU) | 서버-클라이언트 (CDN 캐싱) | 서버-클라이언트 |
| **CDN 호환성** | 전통 CDN 캐싱 불가 | 글로벌 범용 CDN 완벽 지원 | 미디어 전용 CDN 필요 |
| **주요 적용처** | 화상회의(Zoom, Meet), 원격의료 | 대규모 스포츠 생중계, 넷플릭스 | 레거시 방송 송출, 라이브 커머스 |

- WebRTC는 대규모 단방향 방송보다는 양방향 상호작용이 생명인 화상회의, 메타버스, 클라우드 게이밍의 초저지연을 보장하는 현대 웹 통신의 독보적 표준임.

## Ⅳ. WebRTC(Web Real-Time Communication)의 주요 한계점 및 해결 방안

- **Symmetric NAT 및 엄격한 기업 방화벽 환경에서의 P2P 연결 실패** :
  - **한계점** : 포트가 지속 변경되는 기업 내부망에서 STUN 직접 연결이 100% 차단되는 현상 발생.
  - **해결 방안** : 글로벌 분산 고대역 TURN 릴레이 클러스터를 구축하고 표준 TURN 포트 443(TLS) 폴백 지원.
- **다자간 화상회의(Full Mesh P2P) 시 단말 업로드 대역폭 폭증 ($N \times (N-1)$ 문제)** :
  - **한계점** : 참여자가 4~5명을 넘어가면 단말이 모든 참가자에게 영상을 개별 업로드하여 네트워크 및 CPU 과부하.
  - **해결 방안** : 미디어 패킷을 받아서 참가자들에게 지능적으로 단순 복제 전달하는 SFU(Selective Forwarding Unit) 미디어 서버 아키텍처 채택.
- **무선망 패킷 손실 및 대역폭 변동 시 영상 끊김과 화질 열화** :
  - **한계점** : 모바일 LTE/Wi-Fi 환경의 일시적 혼잡 시 프레임 드롭 및 모자이크 왜곡 발생.
  - **해결 방안** : 구글 혼잡제어(GCC: Google Congestion Control) 적용 및 단일 스트림 내 다중 해상도 계층을 전송하는 SVC(Scalable Video Coding) / Simulcast 기법 적용.

## Ⅴ. WebRTC(Web Real-Time Communication) 적용 및 발전을 위한 기술사적 제언

- **대규모 엔터프라이즈 화상 회의 구축 시 SFU 미디어 서버 클러스터링 설계** : 단말 부하를 최소화하고 100명 이상의 대규모 세미나를 지원하기 위해 분산 SFU(Selective Forwarding Unit) 노드 오케스트레이션 필수.
- **종단 간 암호화(E2EE: End-to-End Encryption) 키 관리 체계 수립** : SFU 미디어 서버를 거치는 환경에서도 서버 관리자가 도청할 수 없도록 WebRTC Insertable Streams(WebCodecs) 기반 E2EE 미디어 암호화 계층 결합 권장.
- **차세대 웹 표준 WebTransport 및 WebCodecs와의 기술 융합 추진** : 극초저지연 데이터 통신과 미디어 커스텀 인코딩/디코딩 제어를 위해 W3C의 WebTransport 기술을 점진적 결합하여 미래형 웹 미디어 플랫폼 구현.
