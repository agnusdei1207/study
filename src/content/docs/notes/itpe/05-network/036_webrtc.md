---
title: "WebRTC(Web Real-Time Communication)"
author: "agnusdei1207"
date: "2026-10-24T22:46:23+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- WebRTC(Web Real-Time Communication), 시그널링, SDP, ICE, STUN, TURN
- SRTP, DTLS, RTCDataChannel, SFU, MCU, E2EE, Simulcast, SVC

## Ⅰ. WebRTC(Web Real-Time Communication)의 개요

- 핵심 요약 : 플러그인 없이 브라우저끼리 음성, 영상, 데이터를 실시간으로 직접 교환하는 개방형 웹 표준.
- 개념 : 별도의 플러그인이나 외부 소프트웨어 없이 W3C의 자바스크립트 API와 IETF의 실시간 통신 프로토콜을 기반으로, 오디오·비디오·임의의 데이터를 피어 간에 직접 교환하는 **WebRTC** (Web Real-Time Communication) 오픈 웹 표준.
- 배경 및 필요성 : 과거 웹 화상 통신은 Flash와 전용 플러그인에 의존하여 보안 취약점과 호환성 문제가 컸고, HTTP(Hypertext Transfer Protocol) 기반 스트리밍(HLS, MPEG-DASH)은 수 초 이상의 지연이 있어 실시간 상호작용을 구현하기 어려웠음.
- 주요 목적 : 초저지연 양방향 미디어 통신, 브라우저 간 P2P(Peer-to-Peer) 연결로 서버 대역폭 비용 절감, 전 구간 암호화를 통한 통신 보안 확보.

## Ⅱ. WebRTC(Web Real-Time Communication)의 특징 및 장점

- 핵심 요약 : 브라우저 내장, P2P 직접 연결, 기본 암호화가 설치 장벽 제거와 저지연, 보안성으로 이어지는 구조.

1. 브라우저 내장 : 표준 브라우저와 모바일 앱에 기본 탑재되어 별도 설치가 필요 없음 → 사용 장벽 제거와 호환성 확보.
2. P2P 직접 연결 : 경로 탐색으로 찾은 최적 경로로 미디어를 피어 간에 직접 전송 → 중계 지연 없이 실시간 상호작용과 서버 대역폭 절감.
3. 기본 암호화 강제 : 음성·영상은 **SRTP** (Secure Real-time Transport Protocol)로, 키 교환과 데이터 채널은 **DTLS** (Datagram Transport Layer Security)로 보호 → 평문 전송 경로가 없어 보안 신뢰도 향상.

## Ⅲ. WebRTC(Web Real-Time Communication)의 구조 (흐름)

- 핵심 요약 : 시그널링으로 연결 정보를 맞춘 뒤 ICE가 경로를 찾고, 직접 연결이 막히면 TURN 릴레이로 바꾸는 이중 경로 구조.
- **시그널링** (Signaling) : 피어 간 미디어 코덱, 해상도, 암호화 정보를 담은 **SDP** (Session Description Protocol)와 네트워크 주소를 교환하는 절차로, WebRTC 표준 외 영역이며 WebSocket 등으로 구현함.
- **ICE** (Interactive Connectivity Establishment) : 복잡한 NAT와 방화벽 환경에서 최적 통신 경로를 찾아내는 프레임워크로, STUN과 TURN을 통합하여 제어함.
- **STUN** (Session Traversal Utilities for NAT) : 단말이 자신의 공인 IP와 포트를 파악하여 직접 P2P 연결을 시도하도록 돕는 경량 프로토콜.
- **TURN** (Traversal Using Relays around NAT) : Symmetric NAT 등으로 직접 연결이 불가능할 때 트래픽을 중계하는 폴백 릴레이 서버.

```text
[ 브라우저 A ] Offer SDP 전송
      ↓ 시그널링 서버 경유
[ 브라우저 B ] Answer SDP 회신
      ↓
[ ICE 후보 교환 (STUN/TURN 조회) ]
      ↓
[ P2P 직접 연결 성공 ]
      ↓ 직접 연결 실패 시
[ TURN 릴레이 경유 ]
```

```text
[ 음성·영상 ] RTP → SRTP 암호화
[ RTCDataChannel ] SCTP over DTLS
[ 전송 기반 ] UDP
```

## Ⅳ. WebRTC(Web Real-Time Communication)의 비교

- 핵심 요약 : WebRTC는 양방향 상호작용에 특화된 저지연 방식이고, HLS와 MPEG-DASH는 대규모 단방향 배포에 강점을 가져 용도가 나뉨.

| 비교 항목 | WebRTC | HLS / MPEG-DASH (HTTP 스트리밍) | RTMP(Real-Time Messaging Protocol) |
| --- | --- | --- | --- |
| 통신 지연 | 실시간 대화가 가능한 초저지연 | 수 초 이상의 청크 단위 지연 | 수 초 내외 |
| 전송 프로토콜 | UDP 기반 (SRTP, SCTP) | TCP 기반 HTTP/HTTPS(Hypertext Transfer Protocol Secure) | TCP 기반 독자 바이너리 프로토콜 |
| 클라이언트 요구 | 표준 브라우저 내장, 설치 불필요 | 표준 브라우저의 HTML5 비디오 | 전용 플레이어 또는 클라이언트 |
| 통신 모델 | P2P 또는 SFU(Selective Forwarding Unit)/MCU(Multipoint Control Unit) 미디어 서버 | 서버-클라이언트, CDN(Content Delivery Network) 캐싱 | 서버-클라이언트 |
| CDN 활용 | 일반 CDN 캐싱 활용이 어려움 | 범용 CDN 완전 지원 | 미디어 전용 서버 필요 |
| 주요 적용처 | 화상회의, 원격의료 | 대규모 생중계, 주문형 스트리밍 | 레거시 방송 송출, 라이브 커머스 |

- 선택 기준 : 참여자가 서로 대화해야 하는 서비스는 WebRTC를, 많은 시청자에게 단방향으로 배포하는 서비스는 HLS나 MPEG-DASH를 검토함.

## Ⅴ. WebRTC(Web Real-Time Communication)의 한계와 방안

- 핵심 요약 : 방화벽에 막힌 P2P, 다자간 업로드 폭증, 무선망 손실을 릴레이 확장, SFU 구조, 혼잡 제어와 계층 부호화로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| Symmetric NAT와 엄격한 기업 방화벽의 P2P 연결 실패 | 포트가 바뀌는 내부망에서 STUN 직접 연결이 차단되어 통화 불가 | 글로벌 분산 TURN 릴레이 클러스터 구축, 표준 TURN 포트 443(TLS, Transport Layer Security) 폴백 지원 | 릴레이 전환 비율 |
| 다자간 Full Mesh 연결의 업로드 폭증 | 참여자 수 N에 대해 연결이 N×(N-1)로 늘어나 단말이 모든 참가자에게 개별 업로드하며 CPU와 대역폭 과부하 | 미디어를 받아 참가자에게 선택적으로 복제 전달하는 SFU 미디어 서버 아키텍처 채택 | 단말 업로드 대역폭 |
| 무선망 손실과 대역폭 변동 | LTE(Long-Term Evolution)나 Wi-Fi의 일시 혼잡 시 프레임 드롭과 화질 열화 | Google Congestion Control(GCC) 적용, SVC(Scalable Video Coding) 또는 Simulcast로 다중 해상도 계층 전송 | 프레임 드롭률, 화질 전환 횟수 |

## Ⅵ. WebRTC(Web Real-Time Communication)에 대한 기술사적 제언

- 핵심 요약 : 대규모 회의는 SFU 중심으로 설계하고, 보안은 서버 신뢰에 의존하지 않는 종단 간 암호화로 보강하는 것이 원칙.
- 대규모 엔터프라이즈 화상회의는 단말 부하를 줄이기 위해 SFU 미디어 서버를 분산 클러스터로 구성하고, 부하에 따라 노드를 오케스트레이션하는 것이 필수적임.
- SFU를 거치더라도 서버 관리자가 미디어 내용을 볼 수 없도록 Insertable Streams 계열 API로 E2EE(End-to-End Encryption) 계층을 추가하고, 키 배포와 교체 절차를 함께 정의해야 함.
- W3C에서 표준화가 진행 중인 WebTransport와 WebCodecs를 점진적으로 결합하면, 저지연 데이터 전송과 미디어 커스텀 처리를 웹 플랫폼 안에서 확장할 수 있음.

## Ⅶ. 결론

- 핵심 요약 : WebRTC는 설치 없이 브라우저끼리 저지연 미디어와 데이터를 주고받는 실시간 양방향 통신의 표준 기반임.
- 시사점 : 상호작용형 서비스에서는 WebRTC가 사실상 기본 선택지이며, 그 가치는 NAT 우회와 암호화를 얼마나 안정적으로 운영하느냐에 달려 있음.
