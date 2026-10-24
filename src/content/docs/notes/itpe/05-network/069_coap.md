---
title: "CoAP(Constrained Application Protocol)"
author: "agnusdei1207"
date: "2026-10-24T22:50:25+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- CoAP(Constrained Application Protocol), RESTful, UDP(User Datagram Protocol), DTLS(Datagram Transport Layer Security)
- CON, NON, ACK, RST, Observe(RFC 7641), Blockwise Transfer(RFC 7959), OSCORE(RFC 8613)
- MQTT(Message Queuing Telemetry Transport), 제약 노드(Constrained Node), Matter, NB-IoT
- 4바이트 헤더, Message ID, 토큰(Token), 프록시(Proxy)

## Ⅰ. CoAP의 개요

- 핵심 요약 : 웹의 REST 모델을 UDP 위에서 4바이트 헤더로 가볍게 옮긴 IoT용 경량 웹 전송 프로토콜.
- 개념 : 8비트 마이크로컨트롤러와 수 킬로바이트 수준의 메모리, 높은 패킷 손실률을 가진 **제약 노드와 제약 네트워크** (Constrained Nodes and Networks)으로 이루어진 IoT (Internet of Things) 환경을 위해 IETF(Internet Engineering Task Force)의 CoRE 워킹그룹이 정한 **경량 응용 프로토콜** (CoAP, Constrained Application Protocol, RFC 7252).
- 배경 및 필요성 : HTTP (Hypertext Transfer Protocol)와 TCP (Transmission Control Protocol) 스택은 연결 설정 과정과 텍스트 헤더, 연결 유지 비용이 커서, 배터리로 동작하는 소형 센서에서는 전력 소모가 감당하기 어렵다. 웹 서버와 같은 설계 모델을 유지하면서 전송 비용만 줄이는 방식이 필요해졌다.
- 주요 목적 : HTTP의 REST 모델(GET, POST, PUT, DELETE)을 그대로 쓰면서 전송 비용을 줄이고, 게이트웨이를 통해 웹 서비스와 원활히 연동.

## Ⅱ. CoAP의 특징 및 장점

- 핵심 요약 : REST 모델의 친숙함과 UDP 기반의 가벼운 전송이 결합되어 배터리 소모와 웹 연동 비용을 함께 낮추는 구조.

1. REST (Representational State Transfer) 모델 계승 : URI 자원에 GET, POST, PUT, DELETE를 적용 → 웹 개발 경험을 그대로 활용하고 HTTP와 1:1 변환이 쉬움.
2. 경량 헤더와 비연결 전송 : 4바이트 고정 헤더와 UDP (User Datagram Protocol) 사용 → 연결 설정이 없어 짧은 패킷을 적은 전력으로 송신.
3. 선택적 신뢰성 : **확인형 메시지** (CON, Confirmable)는 ACK를 받을 때까지 재전송하고, **비확인형 메시지** (NON, Non-Confirmable)는 유실을 허용 → 중요 명령과 주기 측정치를 구분.
4. 자원 관찰 : **Observe 옵션** (RFC 7641, 자원 상태 변경 시 알림을 받는 구독 방식) → 주기적 폴링이 줄어 트래픽과 전력 절감.
5. 블록 단위 전송 : **블록 전송** (Blockwise Transfer, RFC 7959, 큰 데이터를 번호 단위로 나누는 방식) → 펌웨어 같은 대용량 데이터를 작은 패킷으로 나누어 전송.

```text
[ CoAP 계층 구조 ]

응용 : RESTful 자원 (URI, GET/POST)
   ↓
요청/응답 계층 : 메서드 코드, 응답 코드
   ↓
메시지 계층 : CON, NON, ACK, RST
   ↓
전송 계층 : UDP 5683 / DTLS 5684
```

## Ⅲ. CoAP의 구조 (흐름)

- 핵심 요약 : 메시지 계층이 신뢰성을 맡고, 요청과 응답 계층이 REST 의미를 맡는 두 서브 계층 구조.
- **메시지 계층** (Messages Layer) : UDP 위에서 재전송과 중복 제거를 수행하여 신뢰성을 선택적으로 부여한다.
- **요청/응답 계층** (Request/Response Layer) : 토큰(Token)으로 요청과 응답을 짝지어 REST 메서드와 상태 코드를 처리한다.
- 메시지 유형 : CON은 응답을 받을 때까지 지수 백오프로 재전송하고, ACK는 CON 수신을 확인하며 응답 데이터를 함께 실을 수 있고, RST는 파싱 실패나 상태 유실을 알린다.

```text
[ 4바이트 기본 헤더 ]

Ver(2) | T(2) | TKL(4)
| Code(8) | Message ID(16)
   ↓ 각 필드의 의미
Ver : 프로토콜 버전
T : 메시지 유형 (CON, NON, ACK, RST)
TKL : 토큰 길이 / Code : 메서드 또는 응답 코드
```

## Ⅳ. CoAP와 MQTT의 비교

- 핵심 요약 : CoAP는 1:1 요청과 응답에, MQTT는 중앙 브로커를 통한 1:N 발행과 구독에 적합하며, 두 방식은 용도에 따라 선택된다.

| 비교 항목 | CoAP (Constrained Application Protocol) | MQTT (Message Queuing Telemetry Transport) |
| --- | --- | --- |
| 표준화 기구 | IETF, RFC 7252 | OASIS, ISO/IEC 20922 |
| 통신 모델 | 1:1 요청과 응답 (클라이언트-서버) | 1:N 발행과 구독 (중앙 브로커) |
| 전송 프로토콜 | UDP (포트 5683), DTLS (Datagram Transport Layer Security, 포트 5684) | TCP (포트 1883), TLS (Transport Layer Security) |
| 헤더 크기 | 4바이트 고정 헤더 | 2바이트 고정 헤더 |
| 자원 탐색 | /.well-known/core로 자원 자동 발견 | 브로커 안의 토픽 설계에 의존 |
| 구독 방식 | Observe 옵션 | 토픽 구독 기능 |
| 적합 환경 | 센서와 액추에이터의 직접 제어, 극소 전력 단말 | 데이터 수집, 다수 구독자 대상 메시지 전달 |

- 선택 기준 : 한 장치를 직접 제어하거나 자원 상태를 조회하는 경우에는 CoAP를, 다수의 장치가 데이터를 발행하고 여러 시스템이 구독하는 경우에는 MQTT를 고른다.

## Ⅴ. CoAP의 한계와 방안

- 핵심 요약 : UDP 특성상 NAT 매핑 소실과 DTLS 부담이 주요 한계이며, 주기적 신호와 응용 계층 암호화로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| NAT (Network Address Translation) 매핑 소실 | 공유기와 셀룰러 NAT가 비활성 UDP 매핑을 짧은 시간에 지워 외부에서 단말로 접속 불가 | 단말이 주기적으로 경량 Keep-Alive 패킷을 보내고, 중계 역할의 CoAP 프록시 배치 | 매핑 유지 성공률, 접속 실패 건수 |
| DTLS 핸드셰이크 부담 | 인증서 교환으로 패킷이 커져 단편화가 생기고, 마이크로컨트롤러 메모리가 부족해짐 | 전송 계층 대신 응용 계층 페이로드만 종단 간 암호화하는 OSCORE (Object Security for Constrained RESTful Environments, RFC 8613) 적용 | 핸드셰이크 실패율, 메모리 사용량 |

## Ⅵ. CoAP 적용 및 발전을 위한 기술사적 제언

- 핵심 요약 : Matter 연동, HTTP 게이트웨이 표준화, 셀룰러 IoT 압축으로 CoAP 생태계를 넓히는 방향.

1. 스마트홈 표준인 Matter의 응용 계층 통신 기반으로 CoAP 생태계를 넓혀 나가는 것이 바람직하다. 스레드(Thread) 기반 무선 메시 네트워크 위에서 단말 간 통신 규격을 통일하면 제조사 간 연동 비용이 줄어든다.
2. 기존 클라우드 REST API와 현장 센서 사이에는 HTTP 메서드와 상태 코드를 대응시키는 고성능 게이트웨이를 두어야 한다. 변환 계층을 표준화하면 웹 개발 인력이 IoT 서비스를 함께 운영할 수 있다.
3. NB-IoT (Narrowband IoT) 같은 셀룰러 IoT 망에서는 CoAP 메시지를 바이너리로 압축하여 전송하는 방식을 검토하는 것이 바람직하다. 원격 검침처럼 주기 전송이 많은 서비스에서는 단말 배터리 수명 연장 효과가 크다.

## Ⅶ. 결론

- 핵심 요약 : CoAP는 웹의 REST 모델을 제약 환경의 UDP 전송으로 옮긴 경량 IoT 응용 프로토콜.
- 시사점 : 직접 제어와 자원 관찰은 CoAP가, 대량 수집과 브로드캐스트는 MQTT가 맡는 역할 분담이 IoT 설계의 기본 원칙이 된다.
