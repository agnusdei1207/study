---
title: "WebRTC(Web Real-Time Communication)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:30:00+09:00"
tags:
  - "notes-network"
extra:
  model: "Gemini 3.8 Flash"

---

## 답안 골격
```text
[WebRTC] ◀━━ 머리: Ⅶ 내 의견 (P2P 메쉬 한계 극복을 위한 SFU 미디어 서버 클러스터링 구축)
 ┃
 ┣━ Ⅰ 개요 ───── 플러그인(ActiveX/Flash) 없는 브라우저 간 실시간 멀티미디어 P2P 통신 표준
 ┣━ Ⅱ 특징 ───── 플러그인 프리(Plugin-free), 초저지연(Sub-500ms), UDP 기반, 기본 암호화 강제
 ┣━ Ⅲ 구조 ───── API 계층(GetUserMedia, RTCPeerConnection, RTCDataChannel) + 프로토콜(SRTP, DTLS, SCTP)
 ┣━ Ⅳ 흐름 ───── ① 시그널링 서버 통한 SDP Offer/Answer 교환 → ② ICE/STUN 후보 수집 → ③ P2P 미디어 스트림 직결
 ┣━ Ⅴ 비교 ───── P2P Mesh vs SFU vs MCU (단말 부하, 대역폭 소모, 서버 믹싱 연산 비용)
 ┗━ Ⅵ 실무 ───── 대칭형 NAT(Symmetric NAT) P2P 실패 / 다자간 통화 시 업로드 대역폭 폭증
```
- 필수 키워드: W3C/IETF · SDP · ICE · STUN · TURN · SRTP · DTLS · SFU(Selective Forwarding Unit)
- 기출: 123회 2교시: "WebRTC의 아키텍처, 연결 수립 절차(ICE, STUN, TURN, SDP) 및 다자간 영상회의 구성 방식을 설명하시오." → Ⅰ~Ⅵ

## 한 줄 본질
- 웹 브라우저에서 화상 통신 시 무거운 플러그인 설치 강제와 서버 경유 지연의 한계 → 브라우저에 내장된 표준 API와 ICE/STUN NAT 관통 기술로 단말 간 UDP 암호화 P2P 터널을 직접 형성 → 서브 200ms 초저지연 화상/데이터 통신 구현 / 참가자 수가 늘어날 때 단말의 CPU 및 업로드 대역폭이 기하급수적으로 폭증

## 핵심 그림
```text
[ WebRTC 연결 수립 (Signaling 및 ICE) 및 미디어 전송 흐름 ]

  [ 브라우저 A ]                 [ 시그널링 서버 (WebSocket) ]           [ 브라우저 B ]
        |                                       |                                     |
        |---- 1. SDP Offer (코덱/해상도) ------>|                                     |
        |                                       |---- 1. SDP Offer 전달 ------------->|
        |                                       |<--- 2. SDP Answer ------------------|
        |<--- 2. SDP Answer 전달 ---------------|                                     |
        |                                                                             |
        +======== 3. STUN 서버 질의 (공인 IP/Port 후보 수집: ICE Candidates) ========+
        |                                       |                                     |
        |---- 4. ICE 후보 교환 ---------------->|---- 4. ICE 후보 전달 -------------->|
        |                                       |                                     |
        |================ 5. P2P 직접 미디어 연결 (SRTP / DTLS 암호화) ================|
        |   (단, P2P 실패 시 TURN 중계 서버를 경유하여 미디어 릴레이)                 |
```

## 핵심 용어
- SDP(Session Description Protocol): 내가 지원하는 비디오 코덱(VP8, H.264), 해상도, 오디오 샘플링 레이트 등의 미디어 메타데이터를 텍스트로 표현한 세션 기술서
- ICE(Interactive Connectivity Establishment): STUN과 TURN 프로토콜을 결합하여 다양한 방화벽과 NAT 환경 속에서 단말 간 최적의 통신 경로 후보를 찾아내는 프레임워크
- STUN vs TURN: STUN은 단말에게 자신의 "공인 IP와 포트"를 알려주어 P2P 직결을 돕는 경량 서버 / TURN은 보안이 엄격한 대칭형 NAT 환경에서 P2P가 불가능할 때 트래픽을 대신 중계해 주는 릴레이 서버

## 핵심 통찰
- WebRTC 표준 기구는 "시그널링(누가 누구에게 전화 거는지)" 방식을 일부러 표준화하지 않음 → 개발자가 WebSocket, SIP, REST 등 원하는 방식을 자유롭게 쓰도록 유연성 보장
- 기본 보안(Security by Default) 원칙에 따라, 모든 미디어는 SRTP로, 모든 데이터 채널은 DTLS로 암호화되지 않으면 브라우저가 통신 자체를 차단
- 3인 이상의 다자간 통화에서 순수 P2P(Mesh)는 단말이 $N-1$개의 스트림을 중복 업로드해야 하므로 단말이 과열됨 → 서버가 영상 인코딩 없이 패킷만 라우팅해 주는 SFU(Selective Forwarding Unit) 아키텍처 채택 필수

## 이웃 토픽과 구분
- HLS/DASH vs WebRTC: HLS/DASH는 HTTP 기반 청크 스트리밍으로 지연 시간 2~5초 발생(대규모 1:N 방송용) / WebRTC는 UDP 기반 프레임 즉시 전송으로 지연 0.2초 미만(양방향 화상회의용)

## 문제·원인·대책
- 적용 상황: 기업 방화벽 내부 단말 간 WebRTC 연결 실패
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 엄격한 기업 방화벽(Symmetric NAT)으로 P2P 연결 100% 실패 | 포트 매핑 규칙이 목적지마다 달라 STUN 공인 주소 무효화 | 443번 포트 기반 TURN(Traversal Using Relays around NAT) 릴레이 배치 | P2P 불가 환경에서도 100% 연결 성공률 보장 |
| 5인 이상 다자 회의 시 참가자 PC 발열 및 프레임 드롭 | P2P Mesh 방식의 다중 업로드 대역폭 및 CPU 인코딩 과부하 | 미디어 분배 서버인 SFU(Selective Forwarding Unit) 도입 | 단말은 1개 스트림만 업로드하고 서버가 구독자에게 분배 |

## 이렇게 출제된다
- 제123회 2교시: "WebRTC의 개념, 주요 프로토콜 스택, 세션 연결 절차(SDP, ICE, STUN, TURN) 및 1:N/N:M 통화 구성을 위한 아키텍처(Mesh, MCU, SFU)를 설명하시오." → 요구 포인트: Ⅲ 계층 구조 + Ⅳ 시퀀스 다이어그램 + Ⅴ 미디어 서버 3종 비교표

## 내 의견
- [단말 네트워크 상태에 맞춘 Simulcast/SVC 적응형 송출] 네트워크가 불안정한 모바일 참가자 1명 때문에 전체 방의 해상도가 떨어지는 품질 저하 발생 → 나라면: 송신 단말이 고/중/저 3가지 해상도를 동시 인코딩해 올리는 사이멀캐스트(Simulcast) 또는 계층형 코덱(SVC, Scalable Video Coding)을 SFU 서버와 연동하여, 회선이 좋은 참가자에게는 1080p를 주고 나쁜 참가자에게는 360p를 선별 전송하는 지능형 미디어 파이프라인 구축

## 찾아볼 것
- 차세대 코덱 AV1의 WebRTC 실시간 인코딩 성능 및 브라우저 하드웨어 가속 현황
