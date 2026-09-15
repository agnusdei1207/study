---
sidebar:
  order: 8
  label: "008. MCP Client (모델 컨텍스트 프로토콜 클라이언트)"
  badge:
    text: "기출 · 30%"
    variant: note
title: "MCP Client (모델 컨텍스트 프로토콜 클라이언트)"
date: "2026-09-15T09:55:00+09:00"
tags:
  - "notes-latest_tech"
weight: 8
extra:
  question_no: "008"
  source_status: "기출"
  source_history: "138회"
  priority: 30
  priority_note: "클라이언트 연결은 MCP 하위 구조"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **모델 컨텍스트 프로토콜 클라이언트(Model Context Protocol Client, MCP Client)**: 호스트 내부에서 하나의 MCP 서버 연결과 자기기술적 JSON-RPC 요청을 관리하는 구성요소이다.
- **자바스크립트 객체 표기법 원격 절차 호출(JavaScript Object Notation Remote Procedure Call, JSON-RPC)**: 요청•응답•알림•오류를 JSON 객체로 표현하는 메시지 형식으로 정의된다.
- **모델 컨텍스트 프로토콜 서버(Model Context Protocol Server, MCP Server)**: 도구•리소스•프롬프트 기능을 표준 메시지로 제공하는 외부 구성요소를 지칭한다.

</details>

- 정의: 서버 연결과 JSON-RPC를 관리하는 **MCP Client**이다.
- 배경/필요성: AI 호스트 애플리케이션이 다수의 이종 MCP 서버들과 직접 통신할 경우, 개별 서버의 프로세스 생명주기 관리, 비동기 JSON-RPC 요청-응답 매핑, 통신 오류 및 타임아웃 처리가 애플리케이션 비즈니스 로직과 강하게 결합되어 복잡도가 폭증하는 한계가 발생함에 따라, 각 MCP 서버 연결을 전담하여 1:1 세션 관리, 메시지 디스패칭, 비동기 Request ID 추적 및 기능 명세 변환을 독립적으로 수행하는 MCP Client 계층을 도입하여 **호스트와 서버 간의 느슨한 결합(Loose Coupling) 보장, 서버 장애 시 격리 및 재시도·취소 정책의 일원화된 통제, 다중 서버 기능의 단일 컨텍스트 통합 지원**을 달성할 필요

#### 한줄 요약
- **MCP Client**를 서버마다 하나씩 두면 연결 격리와 보안 경계를 얻지만, 그만큼 호스트가 서버 수에 비례하는 세션 상태를 떠안는다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **요청 식별자(Request Identifier, Request ID)**: 비동기 요청과 그에 대응하는 응답•취소를 연결하는 값으로 정의된다.
- **요청 축(Request Axis)**: 서버별 연결과 요청 메타데이터를 관리하는 기능 영역으로 정의된다.
- **추적 축(Tracking Axis)**: 요청 식별자•알림•취소로 비동기 상태를 추적하는 기능 영역을 뜻하며, 복잡한 문제 해결과 동적 환경 적응에 필수적인 역할을 수행한다.
- **중계 축(Relay Axis)**: 서버 기능 명세•실행 결과를 호스트에 전달하는 기능 영역으로 정의된다.

</details>

- **요청 축**: 서버별 연결과 JSON-RPC 요청 관리
- **추적 축**: Request ID•알림•취소 기반 상태 추적
- **중계 축**: 기능 명세•실행 결과를 호스트에 전달

#### 한줄 요약
- **Request ID·서버별 연결** 기반 결과 중계

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **기능 변환기(Feature Converter)**: 서버가 공개한 도구•리소스•프롬프트 명세를 호스트가 사용할 수 있는 형태로 전달하는 구성요소로 정의된다.
- **표준 입출력(Standard Input/Output, stdio)**: 로컬 클라이언트와 서버가 프로세스 입출력 스트림으로 메시지를 교환하는 전송 방식이다.
- **스트리밍 가능 하이퍼텍스트 전송 프로토콜(Streamable Hypertext Transfer Protocol, Streamable HTTP)**: 원격 요청을 HTTP POST와 메서드•기능 라우팅 헤더로 교환하는 전송 방식.

</details>

```text
[MCP Client 내부 아키텍처] ── [세션 중개 및 메시지 라우팅 코어]
├── [호스트 연동 인터페이스]
│   ├── 호스트 API 어댑터
│   └── 컨텍스트 및 도구 명세 제공
├── [메시지 디스패칭 코어]
│   ├── 메시지 중개기 (Dispatcher)
│   ├── Request ID 매핑 및 비동기 추적
│   └── 취소(Cancellation) 및 타임아웃
├── [기능 변환 계층]
│   ├── Tools/Resources/Prompts 변환
│   └── 결과 정규화 및 오류 래핑
└── [전송 관리 계층 (Transport)]
    ├── stdio 프로세스 관리자
    └── HTTP-SSE 연결 및 재연결 제어
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 MCP Client 아키텍처 계층과 세부 중개 모듈 간의 계층적 포함 관계를 나타냄

| 구성요소 | 책임 |
|:---|:---|
| 요청 메타 관리자 | Request ID 발급 및 요청 수명주기, 취소·타임아웃 상태 관리 |
| 메시지 중개기 | 비동기 JSON-RPC 요청 전송 및 응답 상관관계(Correlation) 매핑 |
| 기능 변환기 | 서버 제공 Tools, Resources 명세를 호스트 규격으로 변환 및 중계 |
| 전송 관리자 | 로컬 stdio 프로세스 파이프 및 원격 Streamable HTTP 연결 수립 |

#### 한줄 요약
- **메시지 디스패처•전송 관리자** 연결 책임 분담

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **호출 식별자(Call Identifier)**: 비동기 JSON-RPC 요청과 나중에 도착한 응답을 정확히 연결하는 값.
- **모델 컨텍스트 프로토콜 호스트(Model Context Protocol Host, MCP Host)**: 사용자 정책과 여러 MCP Client 연결을 관리하는 AI 애플리케이션.
- **Request ID 기반 표준 요청 전송(Standard Request Transmission)**: 선택 기능과 구조화 인자를 식별자와 함께 보내는 단계.
- **서버 결과•오류 반환(Server Result Return)**: 실행 결과•오류를 요청 식별자와 연결해 받는 단계이다.
- **출처가 구분된 결과 전달(Differentiated Result Delivery)**: 서버 경계를 표시한 결과를 호스트에 중계하는 단계를 지칭한다.

</details>

```text
[호출 의도 수신] (① 호스트로부터 도구 선택, 파라미터 및 실행 정책 전달 접수)
       │
       ▼
[메시지 프레임 구성] (② 고유 Request ID 할당 및 JSON-RPC 2.0 규격 요청 메시지 조립)
       │
       ▼
[전송 계층 디스패치] (③ stdio 파이프 또는 Streamable HTTP 연결을 통해 대상 MCP 서버에 전송)
       │
       ▼
[응답 매핑/상관관계] (④ 서버 반환값 수신 후 Request ID 대조 및 취소·타임아웃 여부 판정)
       │
       ▼
[결과 정규화/호스트 반환] (⑤ 서버 출처 네임스페이스를 바인딩하여 호스트 추론 컨텍스트로 전달)
```

- 분기 결과: 정상 응답 시 호스트로 정규화 결과 반환, 타임아웃 또는 연결 단절 시 재시도 백오프 또는 취소 통지

#### 한줄 요약
- **출처가 구분된 결과 전달** 기반 서버 경계 보존

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **스트리밍 가능 하이퍼텍스트 전송 프로토콜 클라이언트(Streamable Hypertext Transfer Protocol Client, Streamable HTTP Client)**: HTTP POST와 라우팅 헤더로 원격 MCP 서버와 통신하는 클라이언트.

</details>

| 구분 | MCP Client | MCP Server |
|:---|:---|:---|
| 적용 기준 | AI 호스트 애플리케이션의 서버별 1:1 연결 | 백엔드 데이터 및 실행 기능의 표준 공개 |
| 핵심 특징 | 세션 생명주기 관리 및 Request ID 메시지 중개 | Tools, Resources, Prompts 원시 기능 제공 |
| 한계 | 다중 서버 연결 시 호스트 세션 상태 관리 부담 | 서버 자체의 인가 검증 및 백엔드 보안 책임 |

#### 한줄 요약
- **MCP Client** 기반 연결 중개, **MCP Server** 기반 기능 제공

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **재요청 정책(Retry Policy)**: 통신 장애 후 백오프•재시도 상한•멱등성으로 중복 실행을 통제하는 규칙.
- **호스트 중계(Host Relay)**: 클라이언트가 서버 기능 명세와 실행 결과를 호스트에 전달하고 최종 사용 여부는 호스트가 결정하게 하는 책임 분리로 정의된다.
</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 복수 서버 결과의 출처 오인 | 연결 및 결과에 서버별 네임스페이스 식별자 부여 | 컨텍스트 혼선 방지 및 권한 경계 보존 |
| 연결 중단과 미완료 요청 잔존 | 지수 백오프 재요청 및 취소·타임아웃 정책 적용 | 요청 유실 및 중복 실행 사전 방지 |
| 기능 변경과 허용 정책 불일치 | 서버 기능 목록 변경 감지 시 호스트 정책 재평가 | 런타임 변경 사항의 안전한 반영 |

#### 한줄 요약
- **재요청 정책•서버별 허용 정책** 기반 기능 범위 통제

## Ⅶ. 결론

- **기술 위상/발전**: MCP Client는 호스트 추론 로직과 외부 분산 MCP 서버들 간의 통신 복잡성을 추상화하는 **세션 중개 및 메시지 라우팅 엔진**
- **실무 적용/통제**: Request ID 기반 비동기 추적, **네임스페이스 충돌 방지 및 출처 추적성 확보**, 서버 장애 대비 **서킷 브레이커 및 헬스체크** 구현 필수

#### 한줄 요약
- **연결 책임•기능 제공 책임** 대상 따라 Client•Server 결정

