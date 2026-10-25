---
title: "CoAP(Constrained Application Protocol)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- CoAP(Constrained Application Protocol), REST(Representational State Transfer), UDP(User Datagram Protocol), DTLS(Datagram Transport Layer Security)
- CON(Confirmable), NON(Non-confirmable), ACK, RST, Observe(RFC 7641), Blockwise Transfer(RFC 7959)
- OSCORE(RFC 8613), Message ID, 토큰(Token), MQTT(Message Queuing Telemetry Transport)

## Ⅰ. CoAP의 개요

- 핵심 요약 : 웹의 REST 모델을 UDP 위의 4바이트 헤더로 옮겨 제약 환경 단말에 적용한 경량 응용 프로토콜.
- 개념 : IETF(Internet Engineering Task Force)의 CoRE(Constrained RESTful Environments) 워킹그룹이 RFC 7252로 표준화한 제약 노드용 **경량 응용 프로토콜** (CoAP, Constrained Application Protocol).
- 배경 및 필요성 : HTTP(Hypertext Transfer Protocol)와 TCP(Transmission Control Protocol) 스택은 연결 설정과 텍스트 헤더, 연결 유지 비용이 커서 배터리 동작 소형 센서의 전력 예산을 초과. 웹과 같은 설계 모델을 유지하면서 전송 비용만 줄이는 수단이 필요.
- 주요 목적 : REST 인터페이스의 재사용, 최소 전력 송신, 웹 서비스와의 게이트웨이 연동.

## Ⅱ. CoAP의 특징 및 장점

- 핵심 요약 : REST 모델 계승과 UDP 기반 경량 전송, 선택적 신뢰성이 전력 절감과 웹 연동 효율로 이어지는 구조.

1. REST 모델 계승 : URI(Uniform Resource Identifier) 자원에 GET·POST·PUT·DELETE를 적용하는 **REST** (Representational State Transfer, 자원과 메서드 중심의 웹 아키텍처 스타일) 구조 → HTTP와의 변환·연동이 단순.
2. 경량 전송 : 4바이트 고정 헤더와 **UDP** (User Datagram Protocol, 비연결형 전송 프로토콜) 사용 → 연결 설정 없이 짧은 패킷의 저전력 송신.
3. 선택적 신뢰성 : **확인형 메시지** (CON, Confirmable)는 수신 확인 응답을 받을 때까지 재전송하고 **비확인형 메시지** (NON, Non-confirmable)는 유실을 허용 → 명령·측정치의 중요도별 전송 구분.
4. 자원 관찰 : **Observe 옵션** (RFC 7641, 자원 상태 변경 시 구독자에게 알리는 확장) → 주기적 폴링 축소로 트래픽·전력 절감.
5. 대용량 분할 : **블록 전송** (Blockwise Transfer, RFC 7959, 큰 데이터를 블록 단위로 나누는 확장) → 펌웨어 배포 같은 대용량 데이터의 안정적 전달.

## Ⅲ. CoAP의 구조 (흐름)

- 핵심 요약 : 메시지 계층이 신뢰성을, 요청/응답 계층이 REST 의미를 담당하는 2개 하위 계층 구조.
- 메시지 유형 :
  1. CON : 수신 확인을 요구하며 지수 백오프로 재전송하는 메시지.
  2. NON : 확인 없이 1회 전송으로 끝내는 메시지.
  3. ACK(Acknowledgement) : CON 수신을 확인하며 응답 데이터를 함께 실을 수 있는 메시지.
  4. RST(Reset) : 파싱 실패·상태 유실을 통보하는 재설정 메시지.
- 요청/응답 계층 : 토큰(Token)으로 요청과 응답을 짝짓고 메서드·응답 코드를 처리.
- 자원 탐색 : /.well-known/core 요청으로 서버 보유 자원 목록의 자동 발견.

```text
[ CoAP 프로토콜 계층 구조 ]

응용 : REST 자원 (URI, 메서드)
   ↓
요청/응답 : 토큰 매칭, 응답 코드
   ↓
메시지 : CON / NON / ACK / RST
   ↓
전송 : UDP 5683 / DTLS 5684
```

```text
[ CON 메시지의 응답 유형 ]

클라이언트 → 서버 : CON 요청
   ↓ 응답이 즉시 준비되면
Piggybacked : ACK + 응답 동시 전달
   ↓ 응답이 늦으면
Separate : 빈 ACK 후 CON 응답 별도 전달
```

- 기본 헤더 필드 : Ver(버전), T(메시지 유형), TKL(토큰 길이), Code(메서드·응답 코드), Message ID(중복 제거·재전송 판별 식별자).

## Ⅳ. CoAP와 MQTT의 비교

- 핵심 요약 : 자원의 직접 제어·조회에는 CoAP, 다수 구독자를 향한 데이터 수집에는 MQTT(Message Queuing Telemetry Transport)가 적합한 역할 분담.

| 비교 축 | CoAP | MQTT |
| --- | --- | --- |
| 통신 모델 | 1:1 요청·응답 (클라이언트-서버) | 1:N 발행·구독 (중앙 브로커) |
| 전송 계층 | UDP 5683, DTLS 5684 | TCP 1883, TLS(Transport Layer Security) 8883 |
| 헤더 크기 | 4바이트 고정 | 최소 2바이트 고정 |
| 구독 방식 | Observe 옵션 | 토픽 구독 |
| 적합 용도 | 센서·액추에이터 직접 제어, 자원 조회 | 대량 데이터 수집, 다수 수신자 전달 |

- 선택 기준 :
  1. 단말 자원을 직접 읽고 쓰는 제어 계열 서비스는 CoAP 우선.
  2. 다수 장치의 데이터를 여러 시스템이 나눠 받는 수집 계열은 MQTT 우선.
  3. 게이트웨이에서 두 프로토콜의 변환 계층을 두어 역할을 분리 운영.

## Ⅴ. CoAP의 한계와 방안

- 핵심 요약 : NAT 매핑 소실, DTLS 핸드셰이크 부담, 멀티캐스트 혼잡 제어 부재를 보완 설계로 관리.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| NAT(Network Address Translation) 매핑 소실 | 무활동 UDP 세션의 주소 매핑이 짧은 주기로 삭제 → 외부 접속 불가 | 단말의 주기적 Keep-Alive 신호, 프록시(Proxy) 경유 구조 | 매핑 유지 성공률, 접속 실패 건수 |
| DTLS 핸드셰이크 부담 | 인증서 교환으로 패킷 팽창과 단편화 → 소형 단말 메모리 부족 | 응용 계층 종단 간 암호화인 **OSCORE** (Object Security for Constrained RESTful Environments, RFC 8613) 적용 | 핸드셰이크 실패율, 메모리 사용량 |
| 멀티캐스트 혼잡 제어 부재 | 비확인형 다수 전송 시 응답 폭주 가능 | RFC 7390 그룹 통신 프로파일과 전송률 제한 적용 | 응답 폭주 발생 건수 |

## Ⅵ. CoAP에 대한 기술사적 제언

- 핵심 요약 : 스마트홈 표준 연계, 단말 관리 표준 채택, 변환 게이트웨이 표준화로 생태계 확대 제안.

1. 단말 제조사는 Thread 기반 무선 메시 위에서 동작하는 Matter 생태계의 연동 규격을 준수하여 스마트홈 기기 간 상호운용 비용을 낮춰야 한다.
2. 플랫폼 운영기관은 OMA(Open Mobile Alliance)의 경량 단말 관리 표준인 **LwM2M** (Lightweight M2M)을 채택하여 CoAP 기반의 펌웨어 업데이트·원격 관리를 표준 절차로 운영해야 한다.
3. 통신사는 HTTP와 CoAP 사이의 교차 프록시 동작을 RFC 8075 규격에 맞춰 게이트웨이로 표준화하여 웹 개발 자산의 재사용을 확보해야 한다.

## Ⅶ. 결론

- 핵심 요약 : CoAP는 웹의 REST 모델을 제약 환경의 UDP 전송 위에 구현한 경량 IoT(Internet of Things) 응용 프로토콜.
- 제어·조회는 CoAP, 수집·전파는 MQTT로 나누는 역할 분담이 IoT 설계의 기본 원칙이 됨.
