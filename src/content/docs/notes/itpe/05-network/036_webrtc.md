---
title: "WebRTC(Web Real-Time Communication)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- WebRTC(Web Real-Time Communication), 시그널링, SDP(Session Description Protocol)
- ICE, STUN, TURN, SRTP, DTLS, RTCDataChannel
- SFU, MCU, Simulcast, SVC, GCC

## Ⅰ. WebRTC의 개요

- 핵심 요약 : 플러그인 없이 브라우저끼리 음성·영상·데이터를 직접 교환하는 개방형 실시간 통신 표준.
- 개념 : W3C(World Wide Web Consortium)의 자바스크립트 API와 IETF(Internet Engineering Task Force)의 전송 프로토콜을 결합해, 별도 설치 없이 브라우저·앱 간에 실시간 미디어와 데이터를 주고받는 **WebRTC** (Web Real-Time Communication) 기술.
- 배경 및 필요성 : 과거 웹 화상 통신은 전용 플러그인에 의존해 보안 취약점과 호환성 문제가 컸고, HTTP(Hypertext Transfer Protocol) 스트리밍 방식의 수 초 지연으로 양방향 상호작용 구현이 어려웠음.
- 주요 목적 : 초저지연 양방향 통신의 구현과, 전 구간 암호화에 기반한 통신 보안 확보.

## Ⅱ. WebRTC의 특징 및 장점

- 핵심 요약 : 브라우저 내장, 직접 연결, 필수 암호화가 접근성·저지연·보안이라는 장점으로 이어지는 구조.

1. 브라우저 내장 : 표준 API가 브라우저와 모바일 플랫폼에 기본 탑재 → 별도 설치 없는 서비스 접근성 확보.
2. P2P(Peer-to-Peer) 직접 전송 : NAT(Network Address Translation) 우회 경로 탐색으로 피어 간 직접 연결을 수립 → 중계 지연 제거와 서버 대역폭 비용 절감.
3. 전송 계층 암호화 필수 : 음성·영상은 RTP(Real-time Transport Protocol)를 **SRTP** (Secure Real-time Transport Protocol)로 감싸고, 키 교환은 **DTLS** (Datagram Transport Layer Security)로 수행 → 평문 경로 없는 기본 보안.
4. 미디어·데이터의 통합 : 통화용 미디어와 범용 데이터를 하나의 연결 위에서 처리하는 **RTCDataChannel** 제공 → 채팅·파일 전송 같은 부가 기능의 단일 구현.

## Ⅲ. WebRTC의 구조 (흐름)

- 핵심 요약 : 연결 정보의 교환과 경로 탐색 절차를 거쳐 직접 연결을 수립하고, 실패 시 중계 전환으로 이어지는 구조.
- **시그널링** (Signaling) : 코덱·암호화·네트워크 정보를 담은 **SDP** (Session Description Protocol)의 Offer·Answer를 피어 사이에서 교환하는 절차로, WebRTC 표준 밖 영역이라 WebSocket 등으로 별도 구현함.
- **ICE** (Interactive Connectivity Establishment) : 후보 주소(host, srflx, relay)를 수집·검사해 연결 가능한 최적 경로를 고르는 프레임워크.
- **STUN** (Session Traversal Utilities for NAT) : 단말이 자신의 공인 주소를 확인해 직접 연결을 시도하게 돕는 경량 서버 기능.
- **TURN** (Traversal Using Relays around NAT) : 대칭형 NAT 등으로 직접 연결이 불가할 때 트래픽을 중계하는 폴백 서버.
- 데이터 채널 : RTCDataChannel은 SCTP(Stream Control Transmission Protocol) 위에 DTLS를 결합한 신뢰성 있는 메시지 채널임.

```text
[ 연결 수립 흐름 ]

브라우저 A의 Offer SDP 전송
    ↓ 시그널링 서버 경유
브라우저 B의 Answer SDP 회신
    ↓
ICE 후보 교환과 경로 검사
    ↓
P2P 직접 연결 성립
    ↓ 직접 연결 실패 시
TURN 릴레이 경유 연결
```

```text
[ 미디어 송수신 흐름 ]

카메라·마이크 입력 수집
    ↓ 코덱 부호화
RTP 패킷화 후 SRTP 암호화
    ↓ ICE 경로로 전송
수신 측 복호화·재생
```

## Ⅳ. WebRTC와 HTTP 스트리밍·RTMP의 비교

- 핵심 요약 : WebRTC는 양방향 상호작용의 초저지연 방식이고, HLS(HTTP Live Streaming)·MPEG-DASH(Dynamic Adaptive Streaming over HTTP)는 대규모 단방향 배포에 강점을 가진 방식.

| 비교 항목 | WebRTC | HLS·MPEG-DASH | RTMP(Real-Time Messaging Protocol) |
| --- | --- | --- | --- |
| 지연 수준 | 실시간 대화가 가능한 수준 | 청크 단위의 수 초 지연 | 수 초 내외 |
| 전송 기반 | UDP(User Datagram Protocol) 기반 | TCP 기반 HTTP | TCP 기반 독자 프로토콜 |
| 클라이언트 | 브라우저 내장 | HTML5 비디오 태그 | 전용 플레이어 |
| 통신 모델 | P2P 또는 SFU·MCU(Multipoint Control Unit) 미디어 서버 | 서버-클라이언트·CDN(Content Delivery Network) | 서버-클라이언트 |
| CDN 호환 | 범용 캐싱 부적합 | 완전 지원 | 전용 서버 필요 |
| 적용 서비스 | 화상회의·원격의료 | 생중계·주문형 스트리밍 | 방송 송출·라이브 커머스 |

- 선택 기준 : 참여자 간 대화가 필요한 서비스는 WebRTC를, 다수 시청자 대상 단방향 배포는 HLS·MPEG-DASH를 적용함.

## Ⅴ. WebRTC의 한계와 방안

- 핵심 요약 : NAT 환경의 연결 실패, 다자간 확장 시 부하 폭증, 무선망 손실을 릴레이 확충과 SFU 구조, 적응형 전송으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 엄격한 NAT·방화벽에서 연결 실패 | 대칭형 NAT나 정책 방화벽이 직접 경로를 차단해 통화 불가 | 분산 TURN 클러스터 구축과 443 포트 기반 폴백 지원 | TURN 전환 비율 |
| 다자간 메시 연결의 부하 폭증 | 참여자 수가 늘수록 업로드 연결이 제곱으로 증가 | 미디어를 수신 후 선택 전달하는 **SFU** (Selective Forwarding Unit) 서버 구조 채택 | 단말 업로드 대역폭 |
| 무선망 손실·대역폭 변동 | 혼잡 구간에서 프레임 드롭과 화질 열화 발생 | GCC(Google Congestion Control) 기반 전송률 조절과 SVC(Scalable Video Coding)·Simulcast 계층 전송 | 프레임 드롭률 |

## Ⅵ. WebRTC에 대한 기술사적 제언

- 핵심 요약 : 확장형 미디어 운영 체계와 서버 의존 없는 종단 간 암호화, 차세대 웹 기술 결합으로 완성도를 높이는 방향.

1. 엔터프라이즈 서비스 조직은 대규모 회의 트래픽을 미디어 서버의 분산 클러스터로 처리하고, 수요 기반 자동 확장과 장애 노드 격리를 수행하는 운영 체계를 구축할 필요가 있음.
2. 보안 담당 조직은 Insertable Streams 계열 API로 E2EE(End-to-End Encryption) 계층을 추가해 SFU 운영자도 미디어 내용을 볼 수 없는 구조를 설계하고, 키 배포·교체 절차를 함께 정의해야 함.
3. 플랫폼 개발 조직은 WebTransport·WebCodecs 같은 신규 웹 표준과의 결합을 검토해 저지연 데이터 전송과 미디어 처리 확장성을 확보해야 함.

## Ⅶ. 결론

- 핵심 요약 : WebRTC는 설치 없이 브라우저 간 저지연 미디어·데이터 교환을 가능하게 한 실시간 통신의 표준 기반임.
- 시사점 : 상호작용형 서비스의 사실상 기본 선택지로서, NAT 우회와 암호화 운영의 안정성이 서비스 품질을 결정함.
