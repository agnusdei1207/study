---
title: "SCTP(Stream Control Transmission Protocol)"
author: "agnusdei1207"
date: "2026-10-24T22:46:23+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- SCTP, 결합(Association), 멀티호밍, 멀티스트리밍, 헤드오브라인 블로킹, 청크
- 상태 쿠키, SYN 플러딩, PR-SCTP, SIGTRAN, WebRTC

## Ⅰ. SCTP(Stream Control Transmission Protocol)의 개요

- 핵심 요약 : 신뢰성과 메시지 경계를 함께 갖추고 다중 경로와 다중 스트림을 지원하는 전송 계층 프로토콜.
- 개념 : TCP의 신뢰성 있는 연결 지향 전송과 UDP의 메시지 경계 보존 특성을 결합하고, 멀티호밍과 멀티스트리밍을 지원하는 **전송 계층**(L4) 프로토콜인 **SCTP** (Stream Control Transmission Protocol, RFC 4960).
- 배경 및 필요성 : 통신 사업자망의 SS7(Signaling System No. 7) 신호를 IP 망 위에서 무손실·무중단으로 전송하는 SIGTRAN(Signaling Transport) 요구에서 출발함. 단일 IP 연결에 의존하는 TCP의 회선 단절 취약성과 단일 큐 블로킹 한계를 넘기 위해 제정됨.
- 주요 목적 : 회선 장애 시 무중단 페일오버, 스트림 분리를 통한 블로킹 제거, 연결 설정 단계에서 SYN 플러딩 공격에 대한 방어.

## Ⅱ. SCTP(Stream Control Transmission Protocol)의 특징 및 장점

- 핵심 요약 : 다중 경로, 독립 스트림, 상태 쿠키 기반 연결 설정이 장애 시 세션 유지와 공격 저항성으로 이어지는 구조.

1. **멀티호밍** (Multi-Homing) : 한 호스트의 여러 IP 주소를 단일 결합에 묶고 하트비트로 경로 상태를 점검 → 주 경로 장애 시 백업 경로로 무손실 전환.
2. **멀티스트리밍** (Multi-Streaming) : 하나의 결합 안에 독립된 스트림 ID를 두어 순서를 스트림별로만 보장 → 한 스트림의 손실이 다른 스트림을 막지 않음.
3. 메시지 경계 보존 : 응용 계층의 메시지 단위를 그대로 유지 → 수신 측에서 별도의 프레이밍 처리가 필요 없음.
4. **상태 쿠키** (State Cookie) : 4-Way 핸드셰이크에서 서버가 연결 상태를 미리 저장하지 않고 서명된 쿠키를 반환 → 클라이언트 검증 후에만 자원을 할당하여 SYN 플러딩 공격을 무력화.

## Ⅲ. SCTP(Stream Control Transmission Protocol)의 구조 (흐름)

- 핵심 요약 : 공통 헤더 아래 여러 청크를 묶는 패킷 구조 위에서, 결합 단위로 다중 경로와 다중 스트림이 동작하는 이중 계층 구조.
- **결합** (Association) : 양단 호스트의 IP 주소 집합 사이에 맺어지는 포괄적 전송 세션으로, 물리 링크가 끊겨도 세션이 유지됨.
- **청크** (Chunk) : 제어 정보와 데이터를 나누어 담는 단위로, 하나의 패킷에 여러 청크를 다중화하여 실음.

```text
[ SCTP 패킷 ]
[ 공통 헤더 ] 포트 · 검증 태그 · CRC-32c
      ↓
[ 제어 청크 ] INIT · SACK · HEARTBEAT 등
      ↓
[ 데이터 청크 ] Stream ID · 순서 번호 · 페이로드
```

```text
[ 호스트 A ]              [ 호스트 B ]
  IP A1 (주 경로) ======== IP B1
      ↓ 주 경로 단절 시
  IP A2 (백업 경로) ====== IP B2
```

```text
[ Stream 0 ] Msg 1 → Msg 2(손실) → 대기
[ Stream 1 ] Msg A → Msg B → Msg C
             Stream 1은 지연 없이 수신
```

- **헤드오브라인 블로킹** (HoL Blocking, Head-of-Line Blocking) : 앞선 패킷 하나의 손실이 뒤따르는 모든 데이터를 막는 현상으로, 멀티스트리밍 구조가 이 문제를 스트림 단위로 제한함.

## Ⅳ. SCTP(Stream Control Transmission Protocol)의 비교

- 핵심 요약 : TCP의 신뢰성과 UDP의 메시지 단위를 함께 갖추되, 연결 설정 방식과 블로킹 처리에서 차별화됨.

| 비교 항목 | TCP (전송 제어 프로토콜) | UDP (사용자 데이터그램 프로토콜) | SCTP (스트림 제어 전송 프로토콜) |
| --- | --- | --- | --- |
| 신뢰성 | ACK(Acknowledgment)와 재전송으로 완전 보장 | 미보장 (Best-Effort) | 완전 보장, 선택적 비신뢰 전송인 PR-SCTP(Partially Reliable SCTP)도 지원 |
| 전송 단위 | 연속된 바이트 스트림 | 독립된 데이터그램 | 메시지 경계를 보존하는 청크 |
| 연결 모델 | 1:1 단일 IP 쌍 | 비연결형 | 복수 IP를 가진 결합 (멀티호밍) |
| 헤드오브라인 블로킹 | 심각 (한 패킷 손실이 전체 대기) | 없음 | 없음 (스트림별 독립 큐) |
| 연결 수립 | 3-Way 핸드셰이크 (SYN 공격에 취약) | 핸드셰이크 없음 | 4-Way 핸드셰이크와 상태 쿠키 |
| 오류 검출 | 16비트 체크섬 | 16비트 체크섬(선택적) | 32비트 CRC(Cyclic Redundancy Check)-32c |

- 선택 기준 : 범용 바이트 스트림은 TCP, 지연에 민감한 단발 메시지는 UDP, 다중 경로 신뢰 전송이 필요한 신호·실시간 데이터는 SCTP를 검토함.

## Ⅴ. SCTP(Stream Control Transmission Protocol)의 한계와 방안

- 핵심 요약 : 중간 장비의 차단, OS 지원 부족, QUIC과의 기능 경쟁을 캡슐화, 사용자 공간 라이브러리, 적용 영역 집중으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| NAT(Network Address Translation) 장비와 방화벽의 차단 | 다수의 공유기와 방화벽이 TCP/UDP만 해석하고 IP 프로토콜 번호 132를 막아 종단 간 연결 실패 | 표준 RFC 6951의 UDP 캡슐화(SCTP-over-UDP, 포트 9899) 적용 | 연결 수립 성공률 |
| OS 커널의 SCTP 지원 부족 | 윈도우, 임베디드 OS 등에서 커널 수준 스택이 없어 애플리케이션 개발 난항 | usrsctp 같은 사용자 공간(User-space) 오픈소스 라이브러리 채택 | 플랫폼별 호환 여부 |
| QUIC과의 기능 경쟁 | 멀티스트리밍과 연결 이동을 갖춘 QUIC이 웹 전송 영역을 선점 | 범용 웹은 QUIC에 맡기고, SCTP는 5G 코어 시그널링과 WebRTC 데이터 채널에 집중 | 영역별 채택 현황 |

## Ⅵ. SCTP(Stream Control Transmission Protocol)에 대한 기술사적 제언

- 핵심 요약 : 무중단이 요구되는 시그널링과 실시간 P2P 전송에 SCTP를 선택적으로 배치하는 것이 실효성이 높음.
- 5G 코어망에서는 기지국(gNB, next generation NodeB)과 AMF(Access and Mobility Management Function) 사이의 시그널링 링크, 즉 NGAP(NG Application Protocol) 전송 경로에 SCTP 멀티호밍을 기본 구성으로 두어야 무중단 운영이 가능함.
- WebRTC의 데이터 채널은 DTLS(Datagram Transport Layer Security) 위에서 SCTP(RFC 8831)를 사용하므로, 브라우저 간 대용량 P2P 전송에서는 SCTP 파라미터를 튜닝해 처리 효율을 높이는 것이 바람직함.
- 증권 체결 같은 금융 시스템에서 전용선 장애 시 자동 우회를 얻기 위해 SCTP 도입을 검토하되, 사전에 방화벽 정책과 소켓 지원 여부를 검증하는 절차를 전제로 삼아야 함.

## Ⅶ. 결론

- 핵심 요약 : SCTP는 멀티호밍과 멀티스트리밍, 상태 쿠키를 갖춘 통신 캐리어급 신뢰 전송 프로토콜임.
- 시사점 : 범용 웹 전송은 QUIC이 맡고 SCTP는 시그널링과 실시간 P2P라는 특정 영역에서 가치를 가지므로, 적용 범위를 명확히 정의하는 것이 운영 위험을 줄이는 길임.
