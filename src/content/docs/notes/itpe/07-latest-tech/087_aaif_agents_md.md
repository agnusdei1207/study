---
title: "AAIF (Agentic AI Foundation)·AGENTS.md"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. AAIF (Agentic AI Foundation)·AGENTS.md의 개요

- 개념 : 자율 AI 에이전트 생태계의 상호운용성을 위한 **Linux Foundation** 산하 재단(AAIF)과, 소프트웨어 저장소의 개발 맥락을 에이전트에 전달하는 **표준 마크다운 규격** (AGENTS.md)
- 배경 및 필요성 : 단순 마크다운 선언문은 법적·물리적 강제력이 없어 **간접 프롬프트 주입** (Indirect Prompt Injection)에 취약하므로 OS 컨테이너 **샌드박스** 격리, **RBAC** 도구 실행 권한 통제, 정적 코드 분석 **CI 게이트** 병용 필수.
- 핵심 목적 : 에이전트 벤더 종속(Lock-in) 탈피, 프로젝트별 컨텍스트 파편화 해소, AI 코딩 에이전트의 환각 방지 및 안전하고 일관된 코드 생성 보장

## Ⅱ. AAIF (Agentic AI Foundation)·AGENTS.md의 핵심 아키텍처 및 동작 메커니즘

AAIF는 저장소 루트/하위 경로의 AGENTS.md 탐색 $\rightarrow$ 에이전트 컨텍스트 윈도우에 지침 주입 $\rightarrow$ 모델의 계획 수립 및 MCP(Model Context Protocol) 도구 호출 $\rightarrow$ 런타임 보안 샌드박스 정책 검증 $\rightarrow$ 격리 환경 내 코드 변경 집행 메커니즘을 기반으로 동작하며, 세부적인 아키텍처와 핵심 컴포넌트 간 상호작용 프로세스는 다음과 같음.

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

- **AGENTS.md** : OpenAI 주도 오픈소스 - 저장소의 아키텍처 지침, 코딩 컨벤션, 빌드/테스트 명령의 표준 마크다운 선언 규격
- **MCP** (Model Context Protocol) : Anthropic 주도 오픈소스 - LLM과 로컬 개발 툴, IDE, 데이터베이스, GitHub API 간의 표준 클라이언트-서버 통신 규약
- **Goose** : Block (Square) 기여 - 개발자의 로컬 머신에서 CLI/GUI로 구동되며 MCP를 지원하는 확장형 자율 코딩 에이전트 엔진

## Ⅲ. AAIF (Agentic AI Foundation)·AGENTS.md의 세부 구성 요소 및 비교 분석

| 비교 항목 | AGENTS.md | System Prompt | Cursor Rules (.cursorrules) | MCP Resources |
|---|---|---|---|---|
| 표준화 주체 | Linux Foundation (AAIF) | 각 LLM 벤더 독자 규격 | Cursor IDE 독자 규격 | Anthropic / AAIF |
| 저장 위치 | Git 저장소 내부 루트/서브폴더 | API 파라미터 또는 챗봇 설정 | 프로젝트 루트 또는 유저 설정 | 외부 MCP 서버 엔드포인트 |
| 범용 호환성 | 에이전트 엔진 독립적 (오픈 규격) | API 호출 클라이언트에 종속 | Cursor 생태계에 제한 | MCP 지원 에이전트에 호환 |
| 표현 형식 | 순수 Markdown 문서 | 자연어 텍스트 / JSON | Markdown 또는 독자 DSL | JSON-RPC 2.0 구조화 데이터 |

- AAIF는 상기 비교 지표를 바탕으로 비즈니스 요구사항과 운영 인프라 환경을 고려한 최적의 아키텍처를 선정하고, 확장성과 안정성을 균형 있게 확보해야 함.

## Ⅳ. AAIF (Agentic AI Foundation)·AGENTS.md의 주요 한계점 및 해결 방안

- 마크다운 지침의 강제력 부재로 인한 LLM의 복잡한 룰 망각 및 무시 :
  - 한계점 : 마크다운 지침의 법적·기술적 강제력 부재로 인해 LLM이 복잡한 지침을 망각하거나 무시하는 현상.
  - 해결 방안 : 중요한 코딩 표준 및 금지 규칙은 Git Pre-commit 훅, CI 린터(ESLint, SonarQube), AST 기반 자동 검증 도구로 이중 강제.
- 저장소 내 오염된 코드나 PR 주석을 통한 간접 프롬프트 주입 공격 :
  - 한계점 : 저장소 내 오염된 서드파티 코드나 PR 주석을 통해 에이전트를 조작하는 간접 프롬프트 주입 공격.
  - 해결 방안 : 외부 입력(이슈, 커밋 로그)과 시스템 지침의 신뢰 경계 분리, 격리된 가상 컨테이너(Docker/Firecracker) 내 실행 강제.
- 대규모 모노레포에서 AGENTS.md 비대화에 따른 컨텍스트 윈도우 잠식 :
  - 한계점 : 대규모 모노레포에서 AGENTS.md가 방대해져 LLM의 유효 컨텍스트 윈도우를 과도하게 점유하는 문제.
  - 해결 방안 : 작업 연관 디렉터리의 지침만 동적으로 청킹하여 주입하는 계층형 지침 캐싱 및 RAG 기반 지침 검색 기법 도입.

## Ⅴ. AAIF (Agentic AI Foundation)·AGENTS.md 적용 및 발전을 위한 기술사적 제언

- AAIF 기반 엔터프라이즈 아키텍처 전환 : AGENTS.md는 단순 프롬프트 문서를 넘어 'AI 네이티브 소프트웨어 엔지니어링(AI-Native SE)'을 완성하는 코어 거버넌스 규격으로 정착의 기조 하에 전사 아키텍처 표준화와 단계적 도입 로드맵을 체계적으로 수립해야 함.
- 저장소 거버넌스 최적화 및 지속 발전 체계 구축 : 단기적으로 전사 깃허브 템플릿에 표준 AGENTS.md 배포 및 팀별 템플릿화를 완수하고, 중장기적으로 IDE-에이전트-CI 파이프라인 전반의 AGENTS.md 자동 유효성 검사기 내재화를 체계적으로 추진하여 실무 운영 효율성과 기술 내재화를 극대화해야 함.
- 보안 아키텍처 최적화 및 지속 발전 체계 구축 : 단기적으로 로컬 에이전트 실행을 위한 최소 권한(Least Privilege) 계정 발급을 완수하고, 중장기적으로 eBPF 기반의 에이전트 시스템 콜 실시간 감시 및 비인가 파일 수정 즉시 차단을 체계적으로 추진하여 실무 운영 효율성과 기술 내재화를 극대화해야 함.
