---
title: "AAIF (Agentic AI Foundation)·AGENTS.md"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "087. AAIF (Agentic AI Foundation)·AGENTS.md"
  order: 87
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

<div class="itpe-topic-path" aria-label="지식 경로">
소프트웨어 공학 > 자율 코딩 에이전트 > 컨텍스트 표준화 > AAIF·AGENTS.md
</div>

## 30초 인출

- 본질: Linux Foundation 산하의 자율 AI 에이전트 오픈소스 연합체(AAIF)와, 소프트웨어 저장소 내에서 코딩 에이전트가 준수해야 할 빌드 규칙, 테스트 지침, 보안 제약 등의 프로젝트 컨텍스트를 마크다운(Markdown)으로 표준화한 선언 파일 규격.
- 메커니즘: 저장소 루트/하위 경로의 AGENTS.md 탐색 $\rightarrow$ 에이전트 컨텍스트 윈도우에 지침 주입 $\rightarrow$ 모델의 계획 수립 및 MCP(Model Context Protocol) 도구 호출 $\rightarrow$ 런타임 보안 샌드박스 정책 검증 $\rightarrow$ 격리 환경 내 코드 변경 집행.
- 통찰: 단순 마크다운 선언문은 법적·물리적 강제력이 없어 간접 프롬프트 주입(Indirect Prompt Injection)에 취약하므로 OS 컨테이너 샌드박스 격리, RBAC 도구 실행 권한 통제, 정적 코드 분석 CI 게이트 병용 필수.

<details><summary>핵심 용어</summary>

- **AAIF(Agentic AI Foundation):** 리눅스 재단(Linux Foundation) 주도로 Anthropic, OpenAI, Block 등이 참여하여 자율 에이전트 표준과 상호운용성을 주도하는 글로벌 오픈소스 재단.
- **AGENTS.md:** AI 코딩 에이전트(Cursor, Devin, Copilot Workspace 등)가 프로젝트의 아키텍처 규칙, 빌드/테스트 명령어, 코딩 스타일을 일관되게 이해하도록 돕는 오픈 마크다운 표준.
- **MCP(Model Context Protocol):** AI 모델과 로컬 개발 환경(파일, 깃, 디버거) 및 외부 SaaS API를 표준 JSON-RPC로 연결하는 Anthropic 주도의 오픈 프로토콜.
- **Goose:** Block(Square)에서 개발하여 AAIF에 기여한 오픈소스 온디바이스 개발자 자동화 AI 에이전트 프레임워크.
- **간접 프롬프트 주입(Indirect Prompt Injection):** 소스코드 주석이나 이슈 티켓 내에 악의적인 명령어를 심어 에이전트가 이를 시스템 지침으로 오인하여 임의 코드를 실행하게 만드는 공격 기법.
</details>

---

## 2~4교시 예상문제 (25점)

> 자율 AI 에이전트의 소프트웨어 개발 생태계 확산에 대응하기 위한 AAIF(Agentic AI Foundation)의 출범 배경과 핵심 프로젝트를 설명하고, 프로젝트 컨텍스트 표준인 AGENTS.md의 작성 체계, 실제 적용 아키텍처, 런타임 보안 취약점 및 엔지니어링 방어 전략을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 자율 코딩 에이전트의 오픈 표준화, AAIF 및 AGENTS.md의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 자율 AI 에이전트 생태계의 상호운용성을 위한 Linux Foundation 산하 재단(AAIF)과, 소프트웨어 저장소의 개발 맥락을 에이전트에 전달하는 표준 마크다운 규격(AGENTS.md) |
| 목적 | 에이전트 벤더 종속(Lock-in) 탈피, 프로젝트별 컨텍스트 파편화 해소, AI 코딩 에이전트의 환각 방지 및 안전하고 일관된 코드 생성 보장 |

- 다양한 AI 코딩 도구(Cursor, Cline, Windsurf, Copilot 등)마다 각기 다른 설정 파일(`.cursorrules`, `.github/copilot-instructions.md`)을 요구하던 파편화 문제 해결.
- 개발 환경(IDE), 도구 연동 규격(MCP), 오픈소스 에이전트(Goose), 프로젝트 지침(AGENTS.md)을 결합하여 개방형 에이전트 엔지니어링 표준 구축.

## Ⅱ. AAIF의 3대 핵심 프로젝트 및 AGENTS.md의 구조적 특징

| AAIF 3대 프로젝트 | 기여 주체 | 핵심 역할 및 기능 |
|---|---|---|
| AGENTS.md | OpenAI 주도 오픈소스 | 저장소의 아키텍처 지침, 코딩 컨벤션, 빌드/테스트 명령의 표준 마크다운 선언 규격 |
| MCP (Model Context Protocol) | Anthropic 주도 오픈소스 | LLM과 로컬 개발 툴, IDE, 데이터베이스, GitHub API 간의 표준 클라이언트-서버 통신 규약 |
| Goose | Block (Square) 기여 | 개발자의 로컬 머신에서 CLI/GUI로 구동되며 MCP를 지원하는 확장형 자율 코딩 에이전트 엔진 |

| AGENTS.md 구조적 특징 | 세부 설명 | 실제 작성 예시 |
|---|---|---|
| 인간-기계 이중 가독성 | LLM뿐 아니라 신규 합류한 인간 개발자도 즉시 이해 가능한 표준 Markdown 채택 | 표준 헤더 `# Project Guidelines for Agents` |
| 계층적 컨텍스트 상속 | 루트 디렉터리의 전역 지침과 하위 패키지의 지역 지침이 유기적으로 중첩 상속 | `/AGENTS.md` (전역) + `/services/auth/AGENTS.md` (인증 특화) |
| 실행 명령어 명시 | 에이전트가 직접 실행해야 할 빌드, 린트, 테스트 스크립트를 코드 블록으로 표준화 | `npm run test:unit`, `pytest --cov` |
| 금지 및 제약 영역 선언 | 에이전트가 임의로 수정하거나 삭제해서는 안 되는 보호 파일 및 민감 영역 명시 | `Do NOT edit .env or credentials.json` |

## Ⅲ. AGENTS.md 기반 코딩 에이전트 실행 및 런타임 보안 프로세스

```text
+-------------------------------------------------------------------------------------------------+
|                           Agent Execution & Security Boundary Pipeline                          |
+-------------------------------------------------------------------------------------------------+
 [Repo Root / Subdir] ---> [AGENTS.md Ingestion] ---> [Agent Context Builder]
   - Architecture Rules      - Parse Markdown Specs     - System Prompt + Repo Rules
   - Test Command List       - Inheritance Merge        - Working Objective
                                                                |
                                                                v
 [Target Repository] <--- [Runtime Policy Enforcement] <--- [Autonomous Agent Engine]
   - File Modifications     - OS Container Sandbox       - Task Decomposition
   - Git Commit / PR        - File Write Whitelist       - MCP Tool Call (Read/Exec)
   - Verified Unit Tests    - Disallowed Command Block   - Self-Correction Loop
```

| 프로세스 단계 | 핵심 처리 내용 | 주요 검증 및 제어 |
|---|---|---|
| 1. 지침 탐색 및 상속 병합 | 에이전트가 작업 대상 파일 경로를 분석하여 루트 및 상위 경로의 AGENTS.md를 파싱 | 충돌 규칙 발생 시 최하위 디렉터리 지침 우선 적용 |
| 2. 컨텍스트 구성 및 계획 | 시스템 프롬프트에 AGENTS.md의 코딩 컨벤션과 제약사항을 주입하고 작업 단계 분해 | 불필요한 토큰 낭비 방지를 위한 지침 압축(Pruning) |
| 3. MCP 도구 기반 탐색·작업 | 표준 MCP 프로토콜을 호출하여 파일 읽기, 정적 분석 도구 실행, 코드 리팩토링 | 읽기 전용(Read-only) 모드에서 영향 범위 사전 분석 |
| 4. 런타임 샌드박스 검증 | 에이전트가 제출한 셸 명령 및 파일 변경 요청을 호스트 보안 정책 엔진이 검사 | 허용되지 않은 외부 네트워크 호출 및 루트 권한 차단 |
| 5. 자동화 테스트 및 커밋 | AGENTS.md에 지정된 테스트 명령어를 실행하여 통과 확인 후 Git 변경사항 스테이징 | 회귀 테스트 실패 시 에이전트 자체 디버깅 루프 재호출 |

## Ⅳ. 에이전트 컨텍스트 주입 체계 비교

| 비교 항목 | AGENTS.md | System Prompt | Cursor Rules (.cursorrules) | MCP Resources |
|---|---|---|---|---|
| 표준화 주체 | Linux Foundation (AAIF) | 각 LLM 벤더 독자 규격 | Cursor IDE 독자 규격 | Anthropic / AAIF |
| 저장 위치 | Git 저장소 내부 루트/서브폴더 | API 파라미터 또는 챗봇 설정 | 프로젝트 루트 또는 유저 설정 | 외부 MCP 서버 엔드포인트 |
| 범용 호환성 | 에이전트 엔진 독립적 (오픈 규격) | API 호출 클라이언트에 종속 | Cursor 생태계에 제한 | MCP 지원 에이전트에 호환 |
| 표현 형식 | 순수 Markdown 문서 | 자연어 텍스트 / JSON | Markdown 또는 독자 DSL | JSON-RPC 2.0 구조화 데이터 |
| 주 용도 | 프로젝트 아키텍처 및 작업 규칙 | 모델의 페르소나 및 기본 역할 | IDE 맞춤형 코드 스타일 지침 | 파일/DB 등 실시간 동적 데이터 주입 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 마크다운 지침의 법적·기술적 강제력 부재로 인해 LLM이 복잡한 지침을 망각하거나 무시하는 현상 | 중요한 코딩 표준 및 금지 규칙은 Git Pre-commit 훅, CI 린터(ESLint, SonarQube), AST 기반 자동 검증 도구로 이중 강제 |
| 저장소 내 오염된 서드파티 코드나 PR 주석을 통해 에이전트를 조작하는 간접 프롬프트 주입 공격 | 외부 입력(이슈, 커밋 로그)과 시스템 지침의 신뢰 경계 분리, 격리된 가상 컨테이너(Docker/Firecracker) 내 실행 강제 |
| 대규모 모노레포에서 AGENTS.md가 방대해져 LLM의 유효 컨텍스트 윈도우를 과도하게 점유하는 문제 | 작업 연관 디렉터리의 지침만 동적으로 청킹하여 주입하는 계층형 지침 캐싱 및 RAG 기반 지침 검색 기법 도입 |

## Ⅵ. 제언

AGENTS.md는 단순 프롬프트 문서를 넘어 'AI 네이티브 소프트웨어 엔지니어링(AI-Native SE)'을 완성하는 코어 거버넌스 규격으로 정착.

```text
[Standard Declaration] ---> [Zero-Trust Runtime Sandbox] ---> [Deterministic CI Gates]
  - AGENTS.md Format          - Restricted MCP Servers          - Automated Unit Tests
  - Hierarchical Scoping      - Isolated Ephemeral Workspaces   - Static Analysis Enforcement
```

| 구현 관점 | 단기 구축 과제 | 중장기 성숙 과제 |
|---|---|---|
| 저장소 거버넌스 | 전사 깃허브 템플릿에 표준 AGENTS.md 배포 및 팀별 템플릿화 | IDE-에이전트-CI 파이프라인 전반의 AGENTS.md 자동 유효성 검사기 내재화 |
| 보안 아키텍처 | 로컬 에이전트 실행을 위한 최소 권한(Least Privilege) 계정 발급 | eBPF 기반의 에이전트 시스템 콜 실시간 감시 및 비인가 파일 수정 즉시 차단 |

## 출제 이력과 검증 출처

- 최신 기술 동향 출제 예상 주제: Agentic AI 표준화, Linux Foundation AAIF 출범, AGENTS.md 및 MCP 상호운용성.
- Linux Foundation, Announcement of Agentic AI Foundation (AAIF) Formation.
- OpenAI & AGENTS.md Open Project, A Simple, Open Format for Guiding Coding Agents.
- Anthropic, Model Context Protocol (MCP) Specification.

## 연결 토픽

- 오케스트레이션 체계: [AI 에이전트 오케스트레이션](./088_ai_agent_orchestration.md)
- 에이전트 개발 문화: [바이브 코딩(Vibe Coding)](./057_vibe_coding.md)
- 데이터 준비성: [AI Ready Data](./089_ai_ready_data.md)
