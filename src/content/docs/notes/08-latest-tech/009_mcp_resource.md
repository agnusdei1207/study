---
sidebar:
  order: 9
  label: "009. MCP Resource (모델 컨텍스트 프로토콜 리소스)"
  badge:
    text: "기출 · 30%"
    variant: note
title: "MCP Resource (모델 컨텍스트 프로토콜 리소스)"
date: "2026-09-15T09:55:00+09:00"
tags:
  - "notes-latest_tech"
weight: 9
extra:
  question_no: "009"
  source_status: "기출"
  source_history: "138회"
  priority: 30
  priority_note: "리소스 제공은 MCP 세부 구성요소"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **모델 컨텍스트 프로토콜 리소스(Model Context Protocol Resource, MCP Resource)**: 서버가 URI로 식별하여 클라이언트에 읽기 중심의 컨텍스트 데이터를 제공하는 MCP 기능을 뜻하며, 복잡한 문제 해결과 동적 환경 적응에 필수적인 역할을 수행한다.
- **통합 자원 식별자(Uniform Resource Identifier, URI)**: 리소스를 고유하게 가리키는 주소 표기로 정의된다.

</details>

- 정의: URI 기반 읽기 문맥을 제공하는 **MCP Resource**이다.
- 배경/필요성: AI 모델에 최신 비즈니스 문맥(로컬 파일, 로그, DB 레코드, 실시간 문서 등)을 주입할 때, 각 데이터 저장소마다 상이한 접근 프로토콜과 파싱 로직을 구현하면 데이터 소스 확장에 따른 통합 비용이 급증하고 부작용(Side Effect) 없는 읽기 전용 데이터와 상태 변경 도구 간의 보안 경계가 무너지는 결함이 발생함에 따라, 모든 정적·동적 데이터를 고유한 URI 및 URI 템플릿으로 식별하여 안전하게 읽기 전용으로 제공하는 MCP Resource 표준 명세를 도입하여 **표준화된 URI 기반 컨텍스트 데이터 식별 및 MIME 타입 기반 구조화 반환, 애플리케이션 제어 컨텍스트(Application-Controlled Context)를 통한 무단 데이터 유출 방지, 변경 알림 구독(resources/subscribe)을 통한 실시간 컨텍스트 최신성 유지**를 달성할 필요

#### 한줄 요약
- **URI** 기반 자원은 부작용 없는 읽기로 범위를 좁혀 안전성을 얻는 대신 상태 변경을 표현하지 못하므로, 행동은 도구 쪽으로 분리해 맡긴다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **애플리케이션 제어 컨텍스트(Application-Controlled Context)**: 호스트가 리소스를 조회하고 모델 문맥에 포함할지 결정하여 데이터 사용 범위를 통제하는 방식이다.
- **변경 알림 구독(Change Notification Subscription)**: 선택 리소스의 변경 알림을 받는 기능.
- **제어 축(Control Axis)**: 애플리케이션이 조회와 모델 문맥 포함 여부를 결정하는 기능 영역으로 정의된다.
- **식별 축(Identification Axis)**: URI와 URI Template로 컨텍스트를 식별하는 기능 영역.
- **최신성 축(Recency Axis)**: 변경 알림 구독으로 선택 리소스의 갱신을 추적하는 기능 영역.

</details>

- **제어 축**: 앱이 조회•모델 문맥 포함 여부 결정
- **식별 축**: URI•URI Template 기반 문맥 식별
- **최신성 축**: 구독한 리소스 변경 알림 전달

#### 한줄 요약
- **URI**•**MIME** 기반 자료 읽기와 변경 알림 수신

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **통합 자원 식별자 템플릿(Uniform Resource Identifier Template, URI Template)**: 변수 자리를 포함해 여러 관련 리소스의 URI를 생성하는 주소 규칙으로 정의된다.
- **다목적 인터넷 우편 확장 형식(Multipurpose Internet Mail Extensions Type, MIME Type)**: 리소스 내용의 데이터 유형과 해석 방식을 나타내는 표기로 정의된다.
- **자바스크립트 객체 표기법 원격 절차 호출(JavaScript Object Notation Remote Procedure Call, JSON-RPC)**: 리소스 조회 요청과 결과를 교환하는 메시지 형식을 뜻하며, 복잡한 문제 해결과 동적 환경 적응에 필수적인 역할을 수행한다.

</details>

```text
[MCP Resource 아키텍처] ── [URI 기반 읽기 컨텍스트 엔진]
├── [식별 및 템플릿 계층]
│   ├── 고유 자원 식별자 (URI)
│   └── 동적 파라미터 매핑 (URI Template)
├── [메타데이터 및 형식]
│   ├── 리소스 이름 및 설명 명세
│   └── MIME Type (Text / Binary Blob)
├── [데이터 제공 엔진]
│   ├── 읽기 전용 콘텐츠 프로바이더
│   └── 접근 권한 및 테넌트 인가 검증
└── [실시간 구독 및 갱신]
    ├── 변경 알림 구독 (resources/subscribe)
    └── 갱신 통지 이벤트 (updated 알림)
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 MCP Resource 아키텍처 계층과 세부 요소 간의 계층적 포함 관계를 나타냄

| 구성요소 | 책임 |
|:---|:---|
| 리소스 명세 | 고유 URI 정의, 자원 설명 및 MIME Type(텍스트/바이너리) 명시 |
| URI 템플릿 | 동적 매개변수를 포함하는 URI Template 규칙 및 매핑 관리 |
| 내용 제공기 | 요청된 URI에 대응하는 읽기 전용 콘텐츠 추출 및 직렬화 반환 |
| 변경 알림 관리자 | resources/subscribe 구독 관리 및 자원 변경 시 updated 이벤트 통지 |

#### 한줄 요약
- **리소스 명세•내용•변경 알림** URI로 연결

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **리소스 읽기(Resource Read)**: 클라이언트가 URI를 지정하고 서버가 MIME 형식과 함께 텍스트 또는 바이너리 내용을 반환하는 요청 흐름으로 정의된다.
- **모델 컨텍스트 프로토콜 클라이언트(Model Context Protocol Client, MCP Client)**: 서버와 리소스 명세•내용을 교환하는 구성요소.
- **모델 컨텍스트 프로토콜 서버(Model Context Protocol Server, MCP Server)**: 권한 범위의 리소스 명세와 내용을 제공하는 구성요소이다.
- **리소스 목록•템플릿 요청(Resource List/Template Request)**: 권한 범위의 URI와 템플릿을 조회하는 단계이다.
- **URI 읽기 요청(URI Read Request)**: 선택한 리소스의 텍스트•바이너리 내용을 요구하는 단계를 지칭한다.
- **URI 해석•권한 검증 후 내용 반환(URI Execution)**: URI와 테넌트 권한을 확인해 MIME 정보와 내용을 제공하는 단계.
- **변경 알림 구독 등록(Notification Subscription)**: 선택한 리소스의 갱신 알림 유형을 등록하는 단계.
- **구독 리소스 변경 알림(Subscribed Notification)**: 변경 URI의 재조회 필요성을 클라이언트에 알리는 단계로 정의된다.

</details>

```text
[리소스 목록 탐색] (① MCP 클라이언트의 resources/list 요청 및 등록된 URI 템플릿 반환)
       │
       ▼
[자원 읽기 요청] (② 특정 리소스 URI 지정을 통한 resources/read JSON-RPC 요청 인입)
       │
       ▼
[URI 해석/인가 검증] (③ 경로 순회 방어, 테넌트 데이터 접근 권한 및 MIME 타입 확인)
       │
       ▼
[데이터 추출/반환] (④ 읽기 전용 텍스트 또는 바이너리 Blob 콘텐츠 추출 및 호스트 반환)
       │
       ▼
[변경 알림/구독] (⑤ resources/subscribe 기반 실시간 데이터 변경 감지 시 updated 알림 통지)
```

- 분기 결과: URI 권한 검증 통과 시 MIME 및 본문 반환, 리소스 부재 또는 비인가 접근 시 표준 에러 반환

#### 한줄 요약
- **URI 읽기•변경 알림** 기반 필요한 문맥만 최신화

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **직접 리소스(Direct Resource)**: 고정 URI 하나로 특정 파일•레코드•문서 같은 컨텍스트를 식별해 제공하는 리소스 유형.
- **도구(Tool)**: 모델이 외부 기능을 실행하도록 호출하는 MCP 기능으로 정의된다.
- **프롬프트(Prompt)**: 사용자가 선택해 재사용할 수 있는 메시지•작업 틀을 제공하는 MCP 기능.

</details>

| 구분 | Resource | Tool | Prompt |
|:---|:---|:---|:---|
| 적용 기준 | 읽기 전용 비즈니스 문맥 데이터 주입 | 시스템 상태 변경 및 외부 API 기능 실행 | 사용자 상호작용 및 작업 템플릿 구성 |
| 핵심 특징 | 애플리케이션 제어 및 URI 기반 식별 | 모델 주도적 호출 및 JSON 스키마 제안 | 사용자 선택 및 템플릿 매개변수 바인딩 |
| 한계 | 직접적인 상태 변경 및 시스템 조작 불가 | 부작용 발생 위험 및 명시적 인가 통제 필수 | 정적 메시지 구조 중심의 상호작용 한계 |

#### 한줄 요약
- 고정 URI 문맥은 **Resource**, 행동 실행은 **Tool**

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **변경 알림 갱신(Notification Update)**: 구독한 변경 알림을 받아 필요한 리소스만 재조회하는 운영 방식을 지칭한다.
- **리소스 통제 원칙(Resource Control Principle)**: URI 기반 문맥 제공 시 템플릿•테넌트•목적별 최소 필드로 노출 범위를 통제하는 원칙.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| URI 조작과 범위 밖 조회 | URI 템플릿 파싱 시 경로 순회 필터링 및 테넌트 인가 검증 | 경로 조작 및 타 테넌트 자원 노출 방지 |
| 과다 제공에 따른 컨텍스트 오염 | 목적별 리소스 분할 및 필드 단위 최소화 조회 | 컨텍스트 윈도우 효율화 및 기밀 보호 |
| 빈번한 데이터 변경에 따른 지연 | resources/subscribe 알림 기반 변경 리소스만 선별 재조회 | 불필요한 폴링 부하 제거 및 최신성 보장 |

#### 한줄 요약
- **URI•테넌트 권한** 검증으로 교차 접근 차단

## Ⅶ. 결론

- **기술 위상/발전**: MCP Resource는 부작용 없는 순수 읽기 데이터를 표준화된 URI 체계로 AI 컨텍스트에 주입하는 **컨텍스트 데이터 제공의 핵심 표준**
- **실무 적용/통제**: 계층적 URI Template 및 MIME 타입 명시, **경로 순회 방어 및 테넌트 권한 검증**, resources/subscribe 기반 실시간 변경 갱신 필수

#### 한줄 요약
- **데이터 용도•행동 필요성** 대상 따라 Resource•Tool 결정

