---
title: "4-way handshake"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "서브"
extra:
  question_no: "049"
  keyword_grade: "서브"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- TCP 4-Way Handshake, FIN, ACK, 반종료(Half-Close)
- TIME_WAIT, 2MSL, CLOSE_WAIT, LAST_ACK, 반개방(Half-Open)
- 연결 드레이닝, 소켓 누수, 포트 고갈

## Ⅰ. TCP 4-Way Handshake의 개요

- 핵심 요약 : 양방향 연결을 방향별로 차례로 닫아 잔여 데이터를 보존하고 소켓 자원을 반환하는 TCP 연결 해제 절차.
- 개념 : TCP(Transmission Control Protocol) 연결에서 두 종단이 **FIN** (Finish)과 **ACK** (Acknowledgment) 패킷을 네 번 주고받아 각 방향의 데이터 흐름을 닫는 절차(**TCP 4-Way Handshake**).
- 배경 및 필요성 : TCP 연결은 두 방향이 독립인 **전이중** (Full-Duplex) 구조이므로, 한쪽 송신의 종료가 곧 연결 전체의 종료가 아니어서 반대 방향 전달 중 데이터의 보존 장치가 필요.
- 주요 목적 : 두 방향 잔여 데이터의 전달 보장, 새 연결로의 지연 패킷 혼입 차단, 운영체제 소켓 자원의 질서 있는 반환.

## Ⅱ. TCP 4-Way Handshake의 특징 및 장점

- 핵심 요약 : 종료를 방향 단위로 분리하고 종료 후에도 일정 시간 상태를 유지해 데이터 무결성과 자원 안전을 함께 확보하는 구조.

1. 방향별 분리 종료 : 한쪽 FIN 이후에도 반대 방향 전송이 유지되는 **반종료** (Half-Close) 특성 → 응답 전송을 마친 뒤 닫는 무결성 효과.
2. 방향별 2단계 종료 : 각 방향을 FIN과 ACK 한 쌍으로 닫음 → 종료 진행 위치를 상태로 추적 가능한 운영성 효과.
3. 종료 후 대기 : 최종 ACK 전송 후 **TIME_WAIT** 상태에서 **2MSL** (Maximum Segment Lifetime의 두 배) 동안 대기 → 최종 ACK 유실 시 재응답 가능과 지연 패킷 혼입 차단 효과.
4. 상태 기반 추적 : 종료 과정이 FIN_WAIT, CLOSE_WAIT 등 상태 전이로 관리 → 장애 위치 판별과 소켓 누수 진단이 쉬워지는 효과.

## Ⅲ. TCP 4-Way Handshake의 구조 (흐름)

- 핵심 요약 : 능동 종료측은 FIN_WAIT 계열과 TIME_WAIT를, 수동 종료측은 CLOSE_WAIT와 LAST_ACK를 거쳐 CLOSED로 수렴하는 상태 흐름.

```text
[ 4-Way 종료 메시지 흐름 ]

1. A → B : FIN (A 송신 종료 선언)
        ↓
2. B → A : ACK (B는 아직 전송 중)
        ↓
3. B → A : FIN (B 송신 종료 선언)
        ↓
4. A → B : ACK → A는 TIME_WAIT 진입
```

```text
[ 수동 종료측 상태 전이 ]

ESTABLISHED
   ↓ 상대 FIN 수신, ACK 회신
CLOSE_WAIT
   ↓ 잔여 전송 완료 후 FIN 전송
LAST_ACK
   ↓ 최종 ACK 수신
CLOSED
```

- 능동 종료측 : FIN 전송 후 FIN_WAIT_1 → FIN_WAIT_2를 거쳐 최종 ACK 후 TIME_WAIT에 진입하고, 2MSL 경과 후 CLOSED로 이동.
- 수동 종료측 : 상대의 종료 통지를 인지한 뒤에도 애플리케이션이 소켓을 닫지 않으면 CLOSE_WAIT에 잔류하는 구조.

## Ⅳ. TCP 4-Way Handshake와 3-Way Handshake의 비교

- 핵심 요약 : 3-Way는 양단 시퀀스 기준을 맞추는 수립 절차, 4-Way는 방향별로 열린 흐름을 닫는 해제 절차로 대칭 구조가 다름.

| 비교 축 | 3-Way (연결 수립) | 4-Way (연결 해제) |
| --- | --- | --- |
| 교환 패킷 | SYN(Synchronize), SYN+ACK, ACK 3회 | FIN, ACK, FIN, ACK 4회 |
| 결합 여부 | SYN과 ACK를 한 세그먼트로 결합 | 종료 시점이 방향마다 달라 분리 |
| 핵심 목적 | 시퀀스 동기화와 옵션 협상 | 잔여 데이터 보존과 자원 반환 |
| 마지막 단계 | 양단이 동시에 ESTABLISHED | 능동측 TIME_WAIT 대기 후 CLOSED |

- 선택 기준 : 수립과 해제는 대체 관계가 아닌 연결 수명 주기의 앞뒤 단계이며, 종료 시 데이터 무결성이 우선이면 FIN 절차, 즉시 회수나 차단이 우선이면 RST(Reset) 기반 강제 종료를 택함.

## Ⅴ. TCP 4-Way Handshake의 한계와 방안

- 핵심 요약 : 종료 상태의 잔류와 일방 종료 누락이 자원 고갈로 이어지므로 커널 설정과 애플리케이션 종료 보장으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| TIME_WAIT 포트 고갈 | 단발성 연결 급증으로 출발지 포트 소진 → 신규 연결 생성 실패 | 커넥션 풀과 Keep-Alive 재사용, 아웃바운드 한정 `tcp_tw_reuse` 검토 | TIME_WAIT 소켓 수, 포트 사용률 |
| CLOSE_WAIT 소켓 누수 | 예외 경로에서 close 호출 누락 → 파일 디스크립터 고갈 | 종료 보장 코드 표준, 유휴 연결 타임아웃 | CLOSE_WAIT 소켓 수 |
| **반개방** (Half-Open, 일방만 살아 있는 비대칭 상태) 잔류 | 한 종단이 FIN 없이 비정상 종료 → 상대는 ESTABLISHED로 착각한 채 자원 잔류 | TCP KeepAlive 프로브와 애플리케이션 하트비트로 이탈 세션 정리 | 반개방 세션 수 |

## Ⅵ. TCP 4-Way Handshake에 대한 기술사적 제언

- 핵심 요약 : 배포 절차와 개발 표준에 정상 종료를 내재화해 종료 상태가 서비스 장애로 번지지 않게 하는 운영 체계.

1. 애플리케이션 개발 조직은 예외 경로를 포함한 소켓 종료 보장 패턴을 코딩 표준으로 지정하고 정적 분석으로 종료 누락을 점검.
2. 인프라 운영 조직은 무중단 배포 시 로드밸런서의 **연결 드레이닝** (Connection Draining) 기간을 절차에 명시해 구 서버의 정상 종료 완료를 보장.
3. 플랫폼 조직은 서버별 임의 튜닝을 금지하고 TCP 커널 파라미터를 표준 템플릿과 변경 이력으로 통제하는 거버넌스를 운영.

## Ⅶ. 결론

- 핵심 요약 : TCP 4-Way Handshake는 전이중 연결의 양방향 종료를 안전하게 마무리하는 표준 절차.
- 종료 과정이 남기는 TIME_WAIT와 CLOSE_WAIT 상태가 연결 안정성 운영의 관찰 대상이 되는 점이 기술적 함의.
