---
title: "테스트 커버리지(Test Coverage)"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- Test Coverage, 테스트 커버리지, 테스트 충실도 메트릭
- 구문 커버리지(Statement Coverage), 결정 커버리지(Decision/Branch Coverage)
- MC/DC(Modified Condition/Decision Coverage), 전 경로 커버리지(All-Path)
- ISO/IEC/IEEE 29119, DO-178C
- 뮤테이션 점수(Mutation Score), 커버리지 래칫(Coverage Ratchet)

## Ⅰ. 테스트 커버리지의 개요

- 핵심 요약 : 테스트 케이스가 소스코드 구조·요구사항을 실행·검증한 충실도를 백분율로 정량화한 메트릭.
- 개념 : **테스트 커버리지** (Test Coverage) 란 소프트웨어 테스트 수행 시 작성된 테스트 케이스 스위트에 의해 소스코드의 특정 구조적 요소(문장, 분기, 조건, 경로) 또는 요구사항 명세가 충실하게 실행·검증되었는가를 백분율(%)로 정량화한 소프트웨어 테스트 충실도 측정 메트릭.
- 배경 및 필요성 : 테스트 활동이 잠재 결함을 탐색한 충실도의 객관적 평가, 미실행 영역(Dead Code, 테스트 사각지대) 식별과 테스트 케이스 보강을 위한 필수 척도 확보.
- 주요 목적 : 테스트 충실도의 정량 평가, 테스트 사각지대 제거, 품질 게이트 기준 제공.
- 표준 체계 : ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission)/IEEE(Institute of Electrical and Electronics Engineers) 29119(소프트웨어 테스팅 표준), DO-178C(항공 소프트웨어 표준).

## Ⅱ. 테스트 커버리지의 특징

- 핵심 요약 : 구조적 실행 기준의 계층적 강도 체계와 초고신뢰성 MC/DC를 갖춘 정량 메트릭.
1. **구문 커버리지** (Statement Coverage) : 소스코드의 모든 문장이 최소 1회 실행되었는지 측정 ($실행된 문장 수 / 전체 문장 수 \times 100\%$).
2. **결정 커버리지** (Decision/Branch Coverage) : 조건식의 전체 평가 결과가 참(True)·거짓(False)이 되는 모든 분기를 최소 1회씩 실행.
3. **조건 커버리지** (Condition Coverage) : 복합 조건 내 개별 조건의 참·거짓 결과를 각각 확보.
4. **MC/DC** (Modified Condition/Decision Coverage) : 각 개별 조건식이 다른 조건식의 영향 없이 독립적으로 결정문 결과에 직접 영향을 미침을 입증하는 초고신뢰성 커버리지.
5. **정량화 척도** : 백분율 기반 측정으로 품질 게이트 기준·목표 관리와 직결.

## Ⅲ. 테스트 커버리지의 구조 (흐름)

- 핵심 요약 : 구문 → 분기 → 조건/결정 → MC/DC → 다중 조건으로 강해지는 계층 구조.
- 제어 흐름 기반 화이트박스 커버리지 계층과 CI 품질 게이트 측정 흐름.

```text
[ 다중 조건 커버리지 (Multiple Condition) ]
 - 모든 진리표 조합 실행 (2^N)
   ▲
[ MC/DC 커버리지 ]
 - 각 조건이 독립적으로 결과 결정 (N+1)
   ▲
[ 조건/결정 커버리지 (Condition/Decision) ]
 - 개별 조건 + 전체 결정 참/거짓
   ▲
[ 분기/결정 커버리지 (Branch/Decision, L2) ]
 - 각 조건문의 True/False 분기 실행
   ▲
[ 구문 커버리지 (Statement, L1) ]
 - 코드 내 모든 실행 가능 문장 1회 실행
```

```text
[ CI 커버리지 측정 흐름 ]
 소스코드 + 테스트 코드 실행
        ↓
 JaCoCo 런타임 에이전트 계측
  - 라인·브랜치 실행 정보 수집
        ↓
 커버리지 리포트 생성
        ↓
 SonarQube 품질 게이트 판정
        ↓
 목표 미달 시 병합 차단
  (커버리지 래칫: Coverage Ratchet)
```

## Ⅳ. 주요 테스트 커버리지 유형의 비교

- 핵심 요약 : 검증 기준·필요 케이스 수·적용 분야에 따른 커버리지 강도의 차이.
- 검증 기준, 최소 필요 케이스 수, 주요 적용 분야 축 비교.

| 커버리지 유형 | 검증 기준 및 규칙 | 최소 필요 케이스 수 | 주요 적용 분야 |
|---|---|---|---|
| 구문 커버리지 (L1) | 모든 코드 라인 1회 이상 실행 | 최소 | 일반 상용 웹/모바일 소프트웨어 (목표 커버리지 기준) |
| 결정 커버리지 (L2) | if/switch 모든 분기 경로 1회 이상 실행 | 적음 | 일반 엔터프라이즈 업무 시스템 |
| 조건 커버리지 | 복합 조건 내 개별 조건의 True/False 1회 | 적음 | 모듈 내부 세부 조건 검증 |
| MC/DC 커버리지 | 개별 조건의 독립적 영향 입증 | $N+1$개 (조건 수 $N$) | 항공(DO-178C Level A), 자율주행(ISO 26262 ASIL(Automotive Safety Integrity Level) D) |
| 전 경로 커버리지 (All-Path) | 프로그램 내 실행 가능한 모든 실행 경로 | 조합 폭발 ($2^N$ 초과) | 루프가 없는 초소형 크리티컬 알고리즘 |

## Ⅴ. 테스트 커버리지의 장점과 한계

- 핵심 요약 : 충실도 정량화·사각지대 식별의 장점, 허위 안도감·무의미 테스트 양산·측정 사각지대의 한계.
- 장점
  1. 테스트 충실도의 객관적 정량화와 목표 관리.
  2. 미실행 영역·죽은 코드(Dead Code) 식별.
  3. CI/CD 품질 게이트 자동화 연동.
- 한계점 1 : 구문 커버리지의 허위 안도감(False Sense of Security)
  - 한계점 : 100% 문장 커버리지(Statement Coverage) 달성에도 복합 조건문의 경계값 오류, 예외 처리 누락, 논리적 결함 보장 불가.
  - 해결 방안 : 분기(Branch) 및 조건/결정 커버리지(MC/DC) 병행 측정, 테스트 케이스 유효성을 실질 검증하는 뮤테이션 점수(Mutation Score) 복합 도입.
- 한계점 2 : 커버리지 목표 달성을 위한 무의미한 단언 없는(Assertion-Free) 테스트 양산
  - 한계점 : 커버리지 수치 강제로 `assert` 없이 메서드만 호출하는 무가치한 테스트 양산, 유지보수 부담 가중.
  - 해결 방안 : SonarQube 등 정적 분석 도구의 Assertion 검출 룰 적용, 단순 코드 라인 비율이 아닌 비즈니스 위험도 기반 테스트(Risk-Based Testing) 우선순위 평가.
- 한계점 3 : 비동기·멀티스레드·외부 분산 호출 구간의 측정 한계
  - 한계점 : 분산 마이크로서비스 간 비동기 메시지 수신, 외부 3rd Party API(Application Programming Interface) 호출 구간은 표준 코드 커버리지 에이전트(JaCoCo 등)로 추적 불가.
  - 해결 방안 : 분산 추적(Distributed Tracing) 기반 엔드투엔드 시나리오 커버리지 측정, 컨트랙트 테스팅(Pact) 기반 서비스 경계 인터페이스 커버리지 보완.

## Ⅵ. 테스트 커버리지에 대한 기술사적 제언

- 핵심 요약 : 가짜 커버리지의 함정 경계와 커버리지 래칫 기반 품질 게이트 정착.
- '가짜 커버리지(Fake Coverage)'의 함정 경계 : 어설션(Assertion) 검증문 없이 코드 라인만 호출하는 테스트도 구문 커버리지 100% 달성이 가능하므로, 단순 수치 달성에 안주하지 않고 결함 검출 능력을 실질 검증하는 뮤테이션 테스트(Mutation Test) 병행 도입 필수.
- CI/CD(Continuous Integration/Continuous Delivery) 파이프라인 품질 게이트 연동 : SonarQube, JaCoCo를 활용하여 신규 추가·수정 코드(New Code)가 브랜치 커버리지 목표 수준을 만족하지 못하면 메인 브랜치 병합을 원천 차단하는 커버리지 래칫(Coverage Ratchet) 정책 정착 필수.

## Ⅶ. 결론

- 핵심 요약 : 커버리지는 테스트 충실도의 표준 척도이나 결함 검출 능력의 별도 검증 필요.
- 요약 : 테스트 커버리지는 구문·결정·MC/DC 계층 체계로 테스트 충실도를 정량화하는 메트릭.
- 시사점 : 뮤테이션 기반 실효성 검증과 품질 게이트 연동으로 수치 관리의 한계를 보완해야 실질 품질 보증 달성.
