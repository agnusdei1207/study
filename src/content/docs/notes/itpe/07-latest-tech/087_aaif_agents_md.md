---
title: "AAIF (Agentic AI Foundation)·AGENTS.md"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "서브"
extra:
  model: "GPT-6"
  keyword_grade: "서브"
---

## 지식 로드맵 내 현재 위치
IT 소프트웨어 개발 → 코딩 에이전트 → 프로젝트 지침·상호운용 생태계 → AAIF·AGENTS.md

## 30초 인출
- **본질:** AGENTS.md는 코딩 에이전트에 프로젝트별 지침을 전달하는 열린 Markdown 형식이다.
- **맥락:** AAIF는 MCP·goose·AGENTS.md를 초기 기여 프로젝트로 둔 Linux Foundation 산하 재단이다.
- **메커니즘:** 에이전트가 파일 지침을 참고할 수 있지만, 지침 파일 자체는 권한을 강제하는 보안 통제가 아니다.

<details><summary>핵심 용어</summary>

- **AAIF(Agentic AI Foundation):** Linux Foundation이 2025년 12월 설립을 발표한, 에이전트 AI 관련 개방형 프로젝트의 협력 기반이다.
- **AGENTS.md:** 저장소의 구조·개발 절차·기여 규칙 등 프로젝트 맥락을 에이전트에 전달하는 Markdown 파일이다.
- **Model Context Protocol (MCP):** AI 앱이 외부 도구·자료와 연동하는 프로토콜이다. 프로젝트 지침 파일과는 역할이 다르다.
</details>

---

## 1교시 예상문제 (10점)
> AAIF와 AGENTS.md의 개념·역할 및 에이전트 운영에서의 적용 관계를 설명하시오. (예상)

---

## 1교시 10점 답안
### Ⅰ. 개요
| 구분 | 핵심 |
|---|---|
| 정의 | AAIF는 관련 프로젝트의 협력 기반이며, AGENTS.md는 코딩 에이전트에 프로젝트 지침을 전하는 열린 Markdown 형식 |
| 목적 | 에이전트 관련 개방 프로젝트의 협력과 프로젝트 지침의 재사용 지원 |

### Ⅱ. 지침과 실행 권한의 구분
```text
[저장소 AGENTS.md]
          | 프로젝트 지침 제공
          v
[에이전트 작업 판단]
          | 도구 요청
          v
[런타임 권한·샌드박스 검사]
          | 허용된 요청만 실행
          v
[대상 시스템 변경]
```

에이전트가 파일을 읽고 따르는 방식은 도구별로 다를 수 있다. 파일 안의 금지 문구만으로 시스템 접근을 차단할 수는 없다.

### Ⅲ. 생태계 구성
| 요소 | 역할 |
|---|---|
| AAIF | 관련 오픈소스 프로젝트의 개방적 개발·협력 기반 |
| AGENTS.md | 프로젝트 지침을 전달하는 Markdown 형식 |
| MCP | 도구·자료 연동 프로토콜 |
| goose | 오픈소스 에이전트 프로젝트 |

**제언:** 중요 권한은 지침 문구가 아니라 런타임 정책과 샌드박스로 강제한다.

---

## 2~4교시 예상문제 (25점)
> AAIF 출범 배경과 주요 기여 프로젝트를 설명하고, AGENTS.md의 활용 범위·한계 및 안전한 에이전트 운영 방안을 제시하시오. (예상)

---

## 2~4교시 25점 답안
## Ⅰ. 개요와 AAIF
| 구분 | 핵심 |
|---|---|
| 정의 | AAIF는 관련 프로젝트의 협력 기반이며, AGENTS.md는 코딩 에이전트에 프로젝트 지침을 전하는 열린 Markdown 형식 |
| 목적 | 에이전트 관련 개방 프로젝트의 협력과 프로젝트 지침의 재사용 지원 |

AAIF는 Linux Foundation이 2025년 12월 설립을 발표한 재단으로, 초기 기여 프로젝트로 Anthropic의 MCP, Block의 goose, OpenAI의 AGENTS.md를 포함한다. 재단 참여만으로 각 프로젝트가 하나의 기술 표준이나 상호운용 규격으로 완성됐다고 볼 수는 없다.

| 프로젝트 | 하는 일 |
|---|---|
| AGENTS.md | 저장소별 작업 맥락·지침을 Markdown으로 제공 |
| MCP | AI 앱과 도구·자료 사이의 연동 규약 |
| goose | MCP 연동을 지원하는 오픈소스 에이전트 프레임워크 |

## Ⅱ. AGENTS.md 적용 구조
```text
[저장소 AGENTS.md]
          | 프로젝트 지침 제공
          v
[에이전트 작업 판단]
          | 도구 요청
          v
[런타임 권한·샌드박스 검사]
          | 허용된 요청만 실행
          v
[대상 시스템 변경]
```

파일은 일반 Markdown이며 보편적으로 정해진 권한 스키마나 JSON Schema가 있는 것은 아니다. 지원 여부·파일 탐색 범위·중첩 지침 우선순위는 에이전트 구현을 확인한다.

## Ⅲ. 활용 한계와 안전 통제
| 위험·한계 | 대응 방안 |
|---|---|
| 지침을 에이전트가 읽지 않거나 잘못 해석 | 도구별 지원·우선순위 확인, 중요한 규칙은 자동 검사로 보완 |
| 지침 문서만으로 파일·네트워크 접근을 막을 수 없음 | OS·컨테이너 샌드박스, 최소 권한 토큰, 명시적 승인 적용 |
| 모호하거나 상충하는 지침 | 파일을 간결하게 유지하고 테스트·명령·금지 영역을 구체화 |
| 악성 저장소 내용의 프롬프트 주입 | 외부 콘텐츠를 신뢰 경계 밖에서 처리하고 위험 도구 호출을 검증 |

## Ⅳ. 기술사적 제언
| 한계 | 해결 방안 |
|---|---|
| 저장소마다 지침 파일의 위치·우선순위가 달라 에이전트가 작업 규칙을 놓칠 수 있음 | 한 프로젝트에서 지침 상속 경로와 우선순위를 확인하고, 필수 작업 규칙이 실제 요청에서 적용되는지 시험한 뒤 확산한다. |

## 출제 이력과 검증 출처
- 현재 확인된 기출 없음. 문항은 AAIF·AGENTS.md의 역할과 운영 통제를 바탕으로 한 예상문제.
- Linux Foundation, [Agentic AI Foundation 설립 발표](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation?hs_amp=true), 2025-12-09.
- AGENTS.md project, [A simple, open format for guiding coding agents](https://github.com/agentsmd/agents.md).

## 연결 토픽
- 에이전트 실행 흐름: [AI 에이전트 오케스트레이션](./088_ai_agent_orchestration.md)
