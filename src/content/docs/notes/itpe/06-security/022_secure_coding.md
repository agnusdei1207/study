---
title: "시큐어 코딩(Secure Coding)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 시큐어 코딩(Secure Coding)의 개요

- 개념 : **소프트웨어 개발 생명주기** (SDLC, Software Development Life Cycle)의 설계 및 구현 단계에서 발생할 수 있는 잠재적 **보안 취약점** (Security Flaws)과 **약점** (CWE)을 원천 배제하기 위해 안전한 코딩 규칙과 표준을 준수하여 프로그래밍하는 소프트웨어 개발보안 기법.
- 배경 및 필요성 : 배포 후 운영 단계에서 방화벽, IPS(Intrusion Prevention System) 등 외부 보안 솔루션으로 애플리케이션 취약점을 방어하는 방식은 비용이 막대하고 근본적 한계가 존재함에 따라, 행정안전부를 중심으로 전자정부 SW(Software) 개발보안 기준이 법제화됨.
- 핵심 목적 : 소프트웨어 결함 및 제로데이 공격 예방, 사후 보안 패치 비용 획기적 절감(Shift-Left Security), 컴플라이언스 준수 및 서비스 연속성 보장.

## Ⅱ. 시큐어 코딩(Secure Coding)의 핵심 아키텍처 및 동작 메커니즘

행정안전부 'SW 개발보안 가이드'는 보안약점을 정의하고 있으며, **정적 분석** (SAST, Static Application Security Testing) 및 **동적 분석** (DAST, Dynamic Application Security Testing) 도구를 통해 소스코드의 취약성을 검증함.

```text
[ 행정안전부 SW 개발보안 7대 분야 및 시큐어 코딩 프로세스 ]

  [ 요구사항/설계 ] -> 위협 모델링 (STRIDE), 보안 설계 검토
          │
          ▼
  [ 구현 (코딩)   ] -> 7대 보안약점 제거 표준 코딩 규칙 적용
  +-------------------------------------------------------------+
  | 1. 입력데이터 검증 및 표현 : SQLi, XSS, 경로 조작(Path Traversal)|
  | 2. 보안 기능              : 취약한 암호화, 하드코딩된 패스워드 |
  | 3. 시간 및 상태           : 경쟁 조건(Race Condition), TOCTOU  |
  | 4. 에러 처리              : 시스템 정보 노출, 오류 메시지 미처리|
  | 5. 코드 오류              : 널 포인터 역참조, 자원 미해제     |
  | 6. 캡슐화                 : 잘못된 세션 관리, 중요 필드 노출  |
  | 7. API 악용               : 취약한 함수 호출 (strcpy, gets)     |
  +-------------------------------------------------------------+
          │
          ▼
  [ 테스트/검증   ] -> SAST(정적 소스 진단) + DAST(동적 모의침투) 게이트 통과
```

- **입력데이터 검증 및 표현** : 모든 외부 입력값을 신뢰하지 않고 화이트리스트 검증, **Prepared Statement** (SQL(Structured Query Language) Injection 방어), **HTML(HyperText Markup Language) 치환** (XSS(Cross-Site Scripting) 방어).
- **보안 기능** : 표준화된 안전한 암호화 알고리즘(AES(Advanced Encryption Standard)-256, SHA(Secure Hash Algorithm)-256) 사용, 소스코드 내 비밀번호/API(Application Programming Interface) 키 하드코딩 절대 금지.
- **시간 및 상태 통제** : 멀티스레드 환경에서 자원 접근 시 동기화(Synchronization) 보장, **검사 시점과 사용 시점** (TOCTOU) 간 간극 제거.
- **에러 처리 및 정보 노출 방지** : 예외 발생 시 상세 스택 트레이스나 DB(Database) 오류를 사용자 화면에 출력하지 않고 일반적인 사용자 정의 에러 페이지 반환.

## Ⅲ. 시큐어 코딩(Secure Coding)의 세부 구성 요소 및 비교 분석

| 분석 기법 | SAST (정적 애플리케이션 보안 테스팅) | DAST (동적 애플리케이션 보안 테스팅) | IAST (대화형 애플리케이션 보안 테스팅) |
| --- | --- | --- | --- |
| 분석 대상 | 소스코드 (Source Code) 및 바이트코드 | 실행 중인 애플리케이션 (HTTP(Hypertext Transfer Protocol) 입출력) | 런타임 에이전트 + 소스코드 실행 흐름 |
| 적용 단계 | 개발 단계 (컴파일/빌드 시점) | 테스트 및 스테이징 운영 단계 | QA(Quality Assurance) 통합 테스트 및 CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인 |
| 실행 필요성 | 코드 실행 불필요 | 애플리케이션 구동 필수 | 서버 구동 및 테스트 트래픽 발생 필수 |
| 장점 | 모든 코드 경로 스캔, 수정 위치 정확 | 실제 악용 가능성 검증, 환경 설정 탐지 | 오탐률 극저, 코드-런타임 동시 추적 |
| 단점 | 높은 오탐률(False Positive), 비즈니스 로직 취약성 탐지 난항 | 코드의 내부 취약 위치 식별 불가, 스캔 시간 소요 | 특정 언어 종속성, 런타임 성능 오버헤드 |

- SAST는 코딩 시점에 즉각적인 수정을 유도하는 Shift-Left의 핵심이며, DAST는 런타임 환경 구성 오류를 탐지하므로 현대 DevSecOps에서는 SAST+DAST+SCA(Software Composition Analysis)가 상호 보완적으로 통합 운영됨.

## Ⅳ. 시큐어 코딩(Secure Coding)의 주요 한계점 및 해결 방안

- **SAST** 도구의 막대한 오탐(False Positive)으로 인한 개발자 피로도 :
  - 한계점 : 정적 분석 도구가 수천 건의 경고를 쏟아내지만 실제 실행 불가능한 경로(Unreachable)인 경우가 많아 개발자의 도구 신뢰도 추락.
  - 해결 방안 : **도달 가능성 분석** (Reachability Analysis) 및 코드 맥락을 이해하는 AI(Artificial Intelligence) 기반 SAST 보조 엔진을 도입하여 오탐 자동 필터링.
- 생성형 AI(GitHub Copilot 등) 코딩 보조 도구에 의한 취약 코드 유입 :
  - 한계점 : 개발자가 복사한 AI 추천 코드에 구형 라이브러리 사용, 버퍼 오버플로, 검증 누락 등의 보안 약점이 포함되는 신종 리스크.
  - 해결 방안 : IDE(Integrated Development Environment) 플러그인 레벨에서 AI가 생성한 코드 블록을 실시간 진단하는 **시큐어 코딩 린터** (Linter) 및 **자동 교정** (Auto-Remediation) 도구 의무화.
- **비즈니스 로직 결함** (Broken Access Control) 탐지 불가 :
  - 한계점 : 정적 분석 도구는 문법적 결함(SQLi, SQL Injection)은 잘 잡지만, 권한 체크 우회(IDOR)나 금액 조작 등 비즈니스 논리 결함을 식별하지 못함.
  - 해결 방안 : 개발 초기 **위협 모델링** (STRIDE)을 필히 수행하고, 비즈니스 시나리오 기반의 단위 보안 테스트 코드 작성을 의무화.

## Ⅴ. 시큐어 코딩(Secure Coding) 적용 및 발전을 위한 기술사적 제언

- CI/CD 파이프라인 내 **보안 품질 게이트** (Quality Gate) 강제 : 시큐어 코딩 진단 결과 Critical/High 등급 취약점 잔존 시 빌드 및 배포를 자동 차단하는 정책 수립.
- 개발자 친화적 피드백 체계(IDE 실시간 진단) 구축 : 배포 직전 감사가 아닌 개발자 IDE(VS Code, IntelliJ) 코딩 순간에 실시간으로 보안 약점을 경고하는 체계 확립.
- 공공·금융 소프트웨어 감리 기준과의 정합성 유지 : 행안부 SW 개발보안 가이드 49개 기준을 사내 코딩 표준으로 수용하고 정기 진단 보고서 작성 자동화.
