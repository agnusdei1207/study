---
title: "MCP(Model Context Protocol) 보안 취약점"
author: "agnusdei1207"
date: "2026-10-24T22:56:54+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "019"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- MCP(Model Context Protocol), 신뢰 경계(Trust Boundary), 에이전틱(Agentic)
- 간접 프롬프트 주입(Indirect Prompt Injection), 혼동된 대리인(Confused Deputy), 도구 오염(Tool Poisoning)
- 도구 실행 승인 창, STDIO, SSE(Server-Sent Events), WebAssembly(Wasm), 상호 TLS(mTLS)
- HITL(Human in the Loop), 이중 LLM(Dual LLM), 볼트(Vault)

## Ⅰ. MCP(Model Context Protocol) 보안 취약점의 개요

- 핵심 요약 : LLM 앱이 외부 도구를 자율 호출하면서 생기는 신뢰 경계 붕괴와 권한 남용 위험.
- 개념 : Anthropic이 공개한 오픈 프로토콜로, LLM 앱(Host·Client)과 파일시스템, 데이터베이스, 외부 API(Application Programming Interface) 도구(Server)를 잇는 통신 표준인 **MCP** (Model Context Protocol) 환경에서 신뢰 경계 붕괴, 비인가 도구 실행, 데이터 유출을 일으키는 결함과 공격 기법.
- 배경 및 필요성 : LLM이 텍스트 생성을 넘어 로컬 터미널 명령을 실행하고 내부 데이터베이스를 조회하는 **에이전틱** (Agentic) 구조로 진화하면서, 신뢰되지 않은 MCP 서버 연결을 통한 운영체제(OS, Operating System) 침해 위협이 커짐.
- 주요 목적 : MCP의 신뢰 경계를 명확히 하고, 도구 실행 권한을 최소화하며, 간접 프롬프트 주입을 막는 안전한 에이전트 확장 체계를 세우는 것.

## Ⅱ. MCP(Model Context Protocol) 보안 취약점의 특징 및 장점

- 핵심 요약 : 외부 데이터 속 명령이 모델 판단을 바꾸고 고권한 도구로 이어지는 구조가 공격 효율을 높임.

1. **간접 프롬프트 주입** (Indirect Prompt Injection) : 조회한 웹페이지나 문서에 숨긴 악성 프롬프트가 호스트 LLM의 지침을 덮어씀 → 사용자가 모르는 사이 에이전트 행동이 바뀜.
2. **혼동된 대리인** (Confused Deputy) : LLM이 사용자의 높은 권한을 대신 행사하는 점을 이용 → 권한이 없는 공격자가 셸 명령 도구를 간접 실행.
3. **도구 오염** (Tool Poisoning) : 악성 서버가 도구 설명을 조작해 특정 작업 때 자신의 도구를 우선 호출하게 함 → 모델의 자율 판단이 악용됨.
4. 자격증명 유출 : 설정 파일(JSON, JavaScript Object Notation)에 평문으로 둔 API 토큰이 서버 침해 시 일괄 노출됨.

## Ⅲ. MCP(Model Context Protocol) 보안 취약점의 구조 (흐름)

- 핵심 요약 : 악성 문서가 LLM을 속이고, MCP 서버의 고권한 도구로 이어지는 연쇄 흐름.

```text
[ 간접 프롬프트 주입 공격 흐름 ]

비신뢰 웹·문서에 악성 프롬프트 은닉
        ↓
Host 앱이 문서 조회 → LLM이 지침으로 오인
        ↓
MCP Client가 도구 호출 요청 전달
        ↓
MCP Server가 고권한 도구 실행 (혼동된 대리인)
        ↓
파일 탈취·셸 실행·외부 유출
```

```text
[ 신뢰 경계 붕괴 구조 ]

신뢰 영역: 사용자 지시, 호스트 정책
-----------------------------------
비신뢰 영역: 외부 문서, 웹페이지, 도구 설명
        ↓ 하나의 컨텍스트로 합쳐짐
LLM 입력 (지시와 데이터 구분 없음)
        ↓
고권한 도구 호출 권한 행사
```

- 수신된 지시는 LLM 입장에서 정상 사용자 요청과 구별되기 어려워, 모델의 판단 단계에서 차단하기 힘들다.

## Ⅳ. MCP(Model Context Protocol)와 기존 연동 방식의 비교

- 핵심 요약 : 정형화된 호출을 통제하던 기존 API와 달리, MCP는 자율 판단하는 모델의 호출 경계를 관리해야 함.

| 비교 축 | REST(Representational State Transfer) API 통신 | 웹훅(Webhook) 연동 | MCP |
| --- | --- | --- | --- |
| 호출 주체 | 개발자가 작성한 결정론적 코드 | 외부 이벤트에 따른 서버 푸시 | 자율 LLM 에이전트의 판단 |
| 인터페이스 정의 | OpenAPI(Swagger) 명세 | JSON 페이로드 스키마 | **JSON-RPC** (JSON Remote Procedure Call) 기반 Tools·Resources·Prompts |
| 신뢰 경계 | 인가된 API 키 기반 통제 | HMAC(Hash-based Message Authentication Code) 서명 검증 | 자연어 프롬프트와 데이터가 혼재 |
| 주요 공격 | 파라미터 변조, 인증 우회 | 재전송 공격, 스푸핑 | 간접 프롬프트 주입, 도구 오염 |
| 격리 통제 | API 게이트웨이, WAF(Web Application Firewall) | 허용 IP 목록 검증 | **WebAssembly** (Wasm) 샌드박싱, **HITL** (Human in the Loop) 승인 |

- 기존 API 연동은 정형화된 코드와 엄격한 인증으로 통제되지만, MCP는 LLM이 도구 설명을 읽고 호출 여부를 스스로 정하므로 신뢰 경계 관리가 더 까다로움.

## Ⅴ. MCP(Model Context Protocol) 보안 취약점의 한계와 방안

- 핵심 요약 : 승인 피로, 권한 분리 부재, 원격 채널 위·변조를 위험도 분류, 샌드박싱, 채널 인증으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 도구 실행 승인 창 피로 | 호출마다 확인 팝업이 뜨면 사용자가 내용을 보지 않고 항상 허용을 눌러 악성 명령 실행을 허용 | 도구를 읽기 전용, 파일 수정, 시스템 명령으로 위험도 분류하고 고위험 명령에만 파라미터를 보여주며 엄격 승인 강제 | 고위험 도구 승인 비율, 항상 허용 설정 수 |
| 권한 분리 부재 | **STDIO** (Standard Input/Output) 기반 로컬 서버가 호스트와 같은 OS 권한으로 실행되어 파일 전체와 환경변수에 접근 | 서버 실행 환경을 **WebAssembly** (Wasm) 또는 루트리스 컨테이너로 샌드박싱해 파일·네트워크 접근 격리 | 서버별 접근 허용 경로 수 |
| 원격 채널 위·변조 | 원격 서버와 **SSE** (Server-Sent Events) 연동 시 악성 도구 정의 주입이나 중간자 공격에 노출 | **상호 TLS** (mTLS, Mutual TLS)를 필수화하고 서명 검증된 서버만 연결 허용 | 미서명 서버 연결 시도 건수 |

## Ⅵ. MCP(Model Context Protocol) 보안 취약점에 대한 기술사적 제언

- 핵심 요약 : 읽기·쓰기 권한 분리, 독립 검증 모델 배치, 시크릿 외부화를 MCP 보안 설계의 기본으로 제시.

1. 최소 권한 설계 : 파일 읽기 서버와 쓰기 서버를 분리하고, 명령 실행 도구에는 허용 목록 기반의 **안전 인수** (Safe Argument)만 넘기도록 설계하는 것이 바람직하다.
2. 이중 LLM 가드레일 : 실행 명령을 만드는 모델과 그 명령의 안전성을 독립적으로 검증하는 **이중 LLM** (Dual LLM) 구조를 두어 생성 모델의 판단을 한 번 더 확인하는 것이 필요하다.
3. 시크릿 외부화 : 설정 파일에 키를 하드코딩하지 않고, **볼트** (Vault)나 클라우드 KMS(Key Management Service)에서 임시 세션 토큰을 주입받는 체계를 갖추는 것이 좋다.

## Ⅶ. 결론

- 핵심 요약 : MCP 보안은 LLM의 자율 판단을 신뢰 경계 안에 가두는 권한 설계의 문제.
- 시사점 : 모델의 판단을 믿기보다 도구의 권한과 격리를 기준으로 통제하는 구조가 에이전트 확산의 전제가 된다.
