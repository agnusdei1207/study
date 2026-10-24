---
title: "시큐어 코딩(Secure Coding)"
author: "agnusdei1207"
date: "2026-10-24T22:58:47+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 시큐어 코딩(Secure Coding), 보안약점(CWE, Common Weakness Enumeration), SDLC(Software Development Life Cycle)
- SAST, DAST, IAST, SCA, 도달 가능성 분석(Reachability Analysis)
- SQL 삽입(SQL Injection), 크로스 사이트 스크립팅(XSS), TOCTOU, IDOR
- 위협 모델링(STRIDE), 시큐어 코딩 린터(Linter), 보안 품질 게이트(Quality Gate)

## Ⅰ. 시큐어 코딩(Secure Coding)의 개요

- 핵심 요약 : 설계와 구현 단계에서 보안약점을 원천 배제하는 안전한 코딩 규칙 준수 기법.
- 개념 : **소프트웨어 개발 생명주기** (SDLC, Software Development Life Cycle)의 설계와 구현 단계에서 **보안약점** (CWE, Common Weakness Enumeration)이 생기지 않도록 안전한 코딩 규칙과 표준을 지키며 프로그래밍하는 소프트웨어 개발보안 기법.
- 배경 및 필요성 : 배포 후 방화벽, 침입 방지 시스템(IPS, Intrusion Prevention System) 같은 외부 솔루션으로 애플리케이션 취약점을 막는 방식은 비용이 크고 근본적 한계가 있어, 행정안전부가 'SW 개발보안 가이드'로 개발 단계의 보안 기준을 제시함.
- 주요 목적 : 소프트웨어 결함과 제로데이 공격을 예방하고, 사후 패치 비용을 줄이며(Shift-Left), 컴플라이언스를 준수하는 것.

## Ⅱ. 시큐어 코딩(Secure Coding)의 특징 및 장점

- 핵심 요약 : 행정안전부 보안약점 7대 분야를 코드 단계에서 제거해 사후 대응 비용을 낮추는 구조.

1. 입력데이터 검증 및 표현 : SQL 삽입(SQL Injection), 크로스 사이트 스크립팅(XSS), 경로 조작 → 외부 입력을 신뢰하지 않고 화이트리스트로 검증.
2. 보안 기능 : 취약한 암호 알고리즘, 소스코드 내 키·비밀번호 하드코딩 → 표준 암호 알고리즘과 키 외부화.
3. 시간 및 상태 : 경쟁 조건, 검사 시점과 사용 시점 차이(TOCTOU, Time-of-Check to Time-of-Use) → 자원 접근 동기화.
4. 에러 처리 : 상세 스택 트레이스와 DB 오류의 화면 노출 → 일반화된 오류 페이지만 반환.
5. 코드 오류 : 널 포인터 역참조, 자원 미해제 → 예외 처리와 자원 해제 규칙 준수.
6. 캡슐화 : 잘못된 세션 관리, 중요 필드 노출 → 접근 제어와 세션 무효화 적용.
7. API 오용 : 길이 검사 없는 함수 호출(strcpy, gets) → 경계를 확인하는 대체 함수 사용.

## Ⅲ. 시큐어 코딩(Secure Coding)의 구조 (흐름)

- 핵심 요약 : 설계 단계의 위협 모델링에서 시작해, 구현 규칙과 자동 진단 게이트를 거쳐 배포로 이어지는 흐름.
- **정적 분석** (SAST, Static Application Security Testing)은 소스코드를 실행하지 않고 검사하고, **동적 분석** (DAST, Dynamic Application Security Testing)은 실행 중인 애플리케이션을 외부에서 공격해 검사한다.

```text
[ 시큐어 코딩 적용 흐름 ]

요구사항·설계
        ↓ 위협 모델링 (STRIDE)
구현 (코딩)
        ↓ 보안약점 제거 규칙 적용
테스트·검증
        ↓ SAST·DAST 게이트 통과
배포
```

```text
[ 파이프라인 보안 게이트 ]

코드 커밋
        ↓
SAST 정적 진단 (빌드 전)
        ↓ 높은 등급 취약점 잔존 시 차단
스테이징 배포
        ↓
DAST 동적 진단 (모의 침투)
```

## Ⅳ. 시큐어 코딩(Secure Coding)의 분석 기법 비교

- 핵심 요약 : SAST는 코딩 시점, DAST는 실행 환경에서 각각 강점이 있어 단계별로 함께 쓰는 구조.

| 비교 항목 | SAST | DAST | IAST(Interactive Application Security Testing) |
| --- | --- | --- | --- |
| 분석 대상 | 소스코드와 바이트코드 | 실행 중인 애플리케이션의 HTTP(Hypertext Transfer Protocol) 입출력 | 런타임 에이전트가 수집한 실행 흐름 |
| 적용 단계 | 개발과 빌드 시점 | 테스트와 스테이징 단계 | QA(Quality Assurance) 통합 테스트, CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인 |
| 장점 | 모든 코드 경로 검사, 수정 위치 명확 | 실제 악용 가능성 검증, 설정 오류 탐지 | 오탐이 적고 코드와 실행 흐름을 함께 추적 |
| 단점 | 오탐(False Positive)이 많고 비즈니스 로직 결함 탐지 난항 | 코드 내부 위치 식별 불가, 스캔 시간 소요 | 특정 언어에 종속, 런타임 성능 부담 |

- SAST는 코딩 시점에 즉각적인 수정을 유도하는 Shift-Left의 핵심이고, DAST는 운영 환경 구성 오류를 찾으므로 두 방식과 **SCA** (Software Composition Analysis, 오픈소스 구성요소 분석)를 함께 운영하는 것이 일반적이다.

## Ⅴ. 시큐어 코딩(Secure Coding)의 한계와 방안

- 핵심 요약 : 과다한 경고, 생성형 AI 코드의 취약점 유입, 로직 결함 탐지 한계를 경고 필터링, IDE 통제, 설계 단계 점검으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| SAST 도구의 경고 과다 | 실행되지 않는 경로까지 경고를 쏟아내 개발자가 도구 신뢰를 잃음 | **도달 가능성 분석** (Reachability Analysis)으로 실제 실행 경로에 있는 경고를 우선 표시 | 오탐 비율, 경고 처리 시간 |
| 생성형 인공지능(AI, Artificial Intelligence) 코드의 취약점 유입 | AI 추천 코드에 구형 라이브러리, 버퍼 오버플로, 입력 검증 누락이 섞여 들어옴 | IDE 단계에서 생성 코드를 실시간 진단하는 **시큐어 코딩 린터** (Linter)와 자동 교정 도구 도입 | 생성 코드의 진단 경고 건수 |
| **비즈니스 로직 결함** (Broken Access Control) | 권한 검사 우회(IDOR, Insecure Direct Object Reference)나 금액 조작은 정적 분석이 놓침 | 개발 초기에 **위협 모델링** (STRIDE, Spoofing·Tampering·Repudiation·Information Disclosure·Denial of Service·Elevation of Privilege)을 수행하고 시나리오 기반 보안 테스트 작성 | 로직 결함 테스트 커버리지 |

## Ⅵ. 시큐어 코딩(Secure Coding)에 대한 기술사적 제언

- 핵심 요약 : 보안 품질 게이트, 개발 환경 내 실시간 피드백, 감리 기준 정합성을 시큐어 코딩 체계의 기본으로 제시.

1. **보안 품질 게이트** (Quality Gate) : CI/CD 파이프라인에 두어 높은 등급의 취약점이 남아 있으면 빌드와 배포를 자동으로 막는 정책을 세우는 것이 바람직하다.
2. 개발 환경 실시간 피드백 : 배포 직전에 감사하는 대신 IDE(Integrated Development Environment, 통합 개발 환경)에서 코딩하는 순간 약점을 알려주는 체계를 두는 것이 필요하다.
3. 감리 기준 정합성 : 행정안전부 SW 개발보안 가이드의 보안약점 진단 기준을 사내 코딩 표준으로 수용하고, 정기 진단 보고서를 자동 생성하는 체계를 두는 것이 좋다.

## Ⅶ. 결론

- 핵심 요약 : 시큐어 코딩은 취약점을 배포 후에 막는 대신 코드 작성 단계에서 없애는 보안 개발 방식.
- 시사점 : 정적·동적 진단과 개발자 피드백이 파이프라인에 내재될 때 보안 점검이 개발 속도와 함께 지속될 수 있다.
