---
sidebar:
  order: 6
  label: "006. 모델 컨텍스트 프로토콜 (Model Context Protocol, MCP)"
  badge:
    text: "기출 · 70%"
    variant: note
title: "모델 컨텍스트 프로토콜 (Model Context Protocol, MCP)"
date: "2026-09-15T09:55:00+09:00"
tags:
  - "notes-latest_tech"
weight: 6
extra:
  question_no: "006"
  source_status: "기출"
  source_history: "138회"
  priority: 70
  priority_note: "표준형 AI 도구 연계가 최신 출제축"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **모델 컨텍스트 프로토콜(Model Context Protocol, MCP)**: AI 호스트와 외부 서버 간 도구·리소스·프롬프트 발견 및 교환을 표준화한 연결 프로토콜. 시스템의 자율적 기능 발견과 일관된 상호작용을 매개하는 핵심 아키텍처.

</details>

- 개념: AI 호스트와 서버가 기능을 교환하는 **JSON-RPC 프로토콜**
- 배경/필요성: 다양한 AI 애플리케이션(Claude Desktop, IDE, 챗봇 등)과 외부 데이터 소스 및 도구(DB, GitHub, 로컬 파일 등) 간의 연동이 파편화된 개별 API로 구현됨에 따라, 클라이언트와 서버의 추가마다 연동 복잡도가 $M \times N$으로 기하급수적으로 폭증하고 유지보수가 불가능해지는 생태계 고립 문제가 발생함에 따라, 앤트로픽(Anthropic)이 주도하여 AI 모델과 외부 시스템 간의 표준 개방형 연결 규격인 모델 컨텍스트 프로토콜(MCP: Model Context Protocol)을 정립하여 **JSON-RPC 2.0 기반의 도구(Tools)·리소스(Resources)·프롬프트(Prompts) 표준 인터페이스 확립, $M+N$ 복잡도의 개방형 AI 확장 생태계 구축 및 로컬(stdio)·원격(SSE/Streamable HTTP) 전송 계층 통일**을 달성할 필요

#### 한줄 요약
- **MCP**는 조합별 최적화 여지를 포기하는 대신 호스트와 서버가 서로를 모른 채 붙게 하여, 연동 비용을 조합 수가 아니라 참여자 수에 비례시킨다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **요청 자기기술성(Self-Descriptive Request)**: 요청이 프로토콜 버전·클라이언트 식별·기능 메타데이터를 자체적으로 전달하는 성질.
- **서버 발견(Server Discovery)**: 클라이언트가 호출 전 서버 기능을 선택적으로 조회하는 원격 프로시저 호출 절차.
- **JSON-RPC**: 요청·응답·알림·오류를 JSON 객체로 표현하는 메시지 표준 형식.
- **메시지 축(Message Axis)**: JSON-RPC 기반 도구·리소스·프롬프트를 교환하는 메시지 데이터 교환 영역.
- **책임 축(Responsibility Axis)**: 호스트·클라이언트·서버 간 정책·연결·기능 책임을 명확히 구분하는 아키텍처 영역.

</details>

- **협상 축**: 초기화로 버전·기능·식별 정보 교환
- **메시지 축**: JSON-RPC로 도구•리소스•프롬프트 교환
- **책임 축**: 호스트•클라이언트•서버 책임 분리

#### 한줄 요약
- **요청 자기기술성•서버 발견** 기반 연동 방식 통일

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **모델 컨텍스트 프로토콜 호스트(Model Context Protocol Host, MCP Host)**: 사용자 동의•보안 정책과 여러 MCP 클라이언트 연결을 관리하는 인공지능 애플리케이션.
- **MCP 클라이언트(MCP Client)**: 서버별 연결과 프로토콜 메시지 교환을 관리하는 호스트 내부 구성요소를 뜻하며, 복잡한 문제 해결과 동적 환경 적응에 필수적인 역할을 수행한다.
- **MCP 서버(MCP Server)**: 도구•리소스•프롬프트 기능을 표준 메시지로 제공하는 외부 구성요소.
- **표준 입출력(Standard Input/Output, stdio)**: 로컬 MCP 프로세스가 표준 입력•출력 스트림으로 메시지를 교환하는 전송 방식을 지칭한다.
- **스트리밍 가능 하이퍼텍스트 전송 프로토콜(Streamable Hypertext Transfer Protocol, Streamable HTTP)**: HTTP POST와 요청 라우팅 헤더로 원격 MCP 메시지를 교환하는 방식.

</details>

```text
[Model Context Protocol 체계] ── [개방형 AI 도구 연결 표준]
├── [MCP 호스트 계층 (Application)]
│   ├── AI 애플리케이션 (Claude/IDE)
│   └── 사용자 동의 및 보안 정책 통제
├── [MCP 클라이언트 계층 (Client)]
│   ├── 세션 수명주기 및 초기화 관리
│   └── 1:N 서버 연결 및 라우팅
├── [프로토콜 및 전송 계층 (Transport)]
│   ├── JSON-RPC 2.0 프로토콜 규격
│   └── stdio (로컬) / Streamable HTTP (원격)
└── [MCP 서버 계층 (Primitives)]
    ├── Tools (실행 가능한 도구/함수)
    ├── Resources (컨텍스트 데이터/파일)
    └── Prompts (재사용 프롬프트 템플릿)
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 MCP 프로토콜 아키텍처 계층과 세부 요소 간의 계층적 포함 관계를 나타냄

| 구성요소 | 책임 |
|:---|:---|
| MCP 호스트 | AI 모델 실행 환경, 사용자 동의 및 서버 연결 정책 통제 |
| MCP 클라이언트 | 세션 라이프사이클 관리 및 1:N 서버 메시지 라우팅 중개 |
| MCP 서버 | Tools, Resources, Prompts 원시 기능을 표준 규격으로 제공 |
| JSON-RPC·전송 계층 | stdio 및 Streamable HTTP 기반 메시지 직렬화 및 양방향 전송 |

#### 한줄 요약
- **MCP Host** 서버별 연결•보안 경계 관리

## Ⅳ. 흐름도

```text
[초기화 단계] (① MCP 클라이언트가 initialize 요청으로 프로토콜 버전 및 기능 협상)
       │
       ▼
[준비 완료 통지] (② MCP 서버의 응답 수신 후 initialized 알림 전송으로 세션 확립)
       │
       ▼
[도구/자원 탐색] (③ tools/list 및 resources/list 요청을 통한 서버 제공 기능 목록 동적 조회)
       │
       ▼
[도구 호출 실행] (④ LLM 추론에 따라 tools/call 요청 전송 및 인자 스키마 전달)
       │
       ▼
[결과 수신/반환] (⑤ 도구 실행 결과 또는 에러 객체를 JSON-RPC 응답으로 수신하여 모델 전달)
```

- 분기 결과: 도구 호출 성공 시 결과 데이터 컨텍스트 주입, 실행 실패 또는 스키마 오류 시 에러 코드 반환

#### 한줄 요약
- 초기화와 기능 목록 조회 후 선택한 도구를 호출한다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **개방형 응용 프로그래밍 인터페이스 명세(OpenAPI Specification, OpenAPI)**: 고정된 하이퍼텍스트 전송 프로토콜(Hypertext Transfer Protocol, HTTP) API 계약을 기술하는 명세를 뜻하며, 복잡한 문제 해결과 동적 환경 적응에 필수적인 역할을 수행한다.

</details>

| 구분 | MCP | OpenAPI | 맞춤형 API |
|:---|:---|:---|:---|
| 적용 기준 | 모델 도구 및 컨텍스트 동적 연계 | 정적 HTTP RESTful API 계약 | 단일 시스템 간 일대일 직접 연동 |
| 핵심 특징 | 기능 목록 탐색·호출 및 컨텍스트 교환 | 엔드포인트 및 HTTP 규격 명세 | 시스템별 독자 규격 직접 구현 |
| 한계 | 호스트-서버 간 보안 신뢰 경계 필수 | 동적 런타임 기능 발견 메커니즘 부재 | 시스템 확장 시 $M \times N$ 복잡도 폭증 |

#### 한줄 요약
- 기능 목록 기반 연계는 **MCP**, 고정 HTTP 계약은 **OpenAPI**

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **신뢰 경계(Trust Boundary)**: 호스트•클라이언트•서버 사이에서 인증•권한•입력 검증 책임이 달라지는 보안 경계.
- **전송 계층 보안(Transport Layer Security, TLS)**: 원격 전송 메시지의 기밀성•무결성과 서버 인증을 제공하는 보안 프로토콜.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 과도한 기능 공개와 권한 확산 | 경계별 허용 도구 목록 지정 및 최소 권한 원칙 적용 | 서버 보안 경계 및 불필요한 침해 차단 |
| 원격 전송 시 토큰 탈취·오용 | TLS 암호화 및 OAuth 2.0 기반 토큰 스코프 검증 | 전송 중 비인가 변조 및 도청 방지 |
| 도구 호출에 따른 비가역 부작용 | 상태 변경 도구 대상 사용자 명시적 승인(HITL) 의무화 | 비가역적 데이터 훼손 및 사고 사전 예방 |

#### 한줄 요약
- 서버별 **신뢰 경계•최소 권한** 기반 기능 공개 제한

## Ⅶ. 결론

- **기술 위상/발전**: MCP는 AI 애플리케이션과 외부 도구·데이터를 표준화된 인터페이스로 연결하는 **개방형 AI 에이전트 생태계의 사실상 표준**
- **실무 적용/통제**: 동적 기능 탐색(tools/list) 구현, **Resource(읽기)와 Tool(쓰기) 권한 분리**, stdio 및 보안 전송(Streamable HTTP/TLS) 환경 최적화 필수

#### 한줄 요약
- **기능 발견 필요성•계약 고정성** 대상 따라 프로토콜 결정

