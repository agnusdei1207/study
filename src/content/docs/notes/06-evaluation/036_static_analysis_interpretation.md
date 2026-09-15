---
sidebar:
  order: 36
  label: "036. 정적 분석 결과 해석 (Static Analysis Result Interpretation)"
  badge:
    text: "기출 · 50%"
    variant: note
title: "보안 취약점 판별 및 오탐 제어 : 정적 분석 결과 해석 (SAST Taint Analysis & 트리아지)"
date: "2026-09-15T09:25:00+09:00"
tags:
  - "notes-evaluation"
weight: 36
extra:
  question_no: "036"
  source_status: "기출"
  source_history: "128회"
  priority: 50
  priority_note: "128회 기출, 정적 애플리케이션 보안 테스트(SAST: Static Application Security Testing) 결과 해석, 오염 분석(Taint Analysis: Source ➔ Sanitizer ➔ Sink), 오탐(False Positive) vs 진탐(True Positive) 판별 기준, 보안 트리아지(Triage) 절차, 기한부 위험 수용(Time-bound Waiver) 및 DevSecOps 품질 게이트(Quality Gate) 연계"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **정적 분석 결과 해석 및 보안 트리아지(Static Analysis Result Interpretation & Triage)**: 정적 분석 도구(SAST: Fortify, SonarQube, Checkmarx 등)가 소스코드를 스캔하여 출력한 수천 건의 원시 보안 경고(Raw Alerts)에 대해, 외부 입력(Source)에서 위험 실행점(Sink)까지의 오염 데이터 흐름(Taint Flow), 살균 함수(Sanitizer)의 유효성, 그리고 런타임 도달 가능성(Reachability)을 정밀 분석하여, 실제 공격 가능한 참 양성(True Positive, TP: 진탐)과 도구의 한계로 인한 거짓 양성(False Positive, FP: 오탐)을 과학적으로 선별·분류하는 전문 보안 엔지니어링 활동.
- **경고 피로증 및 무분별한 예외 억제 결함(Alert Fatigue & Blind Suppression Defect)**: 수천 건의 정적 분석 오탐 경고에 지친 개발팀이 경고를 전면 무시하거나 소스코드에 `@SuppressWarnings` 주석을 남발하여 실제 치명적인 SQL Injection 및 RCE(원격 코드 실행) 참 양성 취약점까지 통째로 은폐시켜 상용 환경에서 대규모 해킹을 당하는 구조적 결함.

</details>

- 정의/개념: SAST 경고의 공격 가능성을 판정하는 **보안 트리아지**
- 배경/필요성: 소프트웨어 개발 생명주기에서 SAST 정적 분석 도구가 출력하는 수천 건의 원시 보안 경고에 대해 오탐(False Positive)과 진탐(True Positive)을 과학적으로 선별하지 못할 경우, 극심한 경고 피로증(Alert Fatigue)으로 인해 개발자가 `@SuppressWarnings` 주석 등으로 경고를 일괄 억제하여 실제 치명적인 SQL Injection 및 원격 코드 실행(RCE) 결함이 상용 환경으로 유출되는 치명적 보안 사고가 발생함에 따라, 외부 입력(Source)에서 위험 실행점(Sink)까지의 오염 데이터 흐름(Taint Flow), 살균 함수(Sanitizer)의 유효성 및 런타임 도달 가능성(Reachability)을 정밀 판별하는 보안 트리아지(Triage) 해석 체계를 도입하여 **참 양성(TP) 취약점의 즉각적 빌드 차단, 도구 한계에 의한 거짓 양성(FP)의 룰셋 튜닝 및 기한부 위험 수용(Time-bound Waiver) 기반의 안전한 DevSecOps 품질 게이트**를 달성할 필요

#### 한줄 요약
- 정적 분석 결과 해석은 Taint 오염 분석과 도달 가능성 검증을 통해 진짜 결함(TP)과 단순 오탐(FP)을 판별한다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **오염 분석 3대 핵심 모델 (Taint Analysis Model)**:
  - **오염원 (Source)**: 신뢰할 수 없는 외부 사용자 입력이 시스템으로 유입되는 진입점 (예: `request.getParameter()`, HTTP Body).
  - **정화/살균기 (Sanitizer / Validator)**: 악의적인 특수문자를 무해화하거나 화이트리스트를 검증하는 방어 로직 (예: `PreparedStatement`, HTML Escape).
  - **취약점 실행점 (Sink)**: 정화되지 않은 입력값이 주입될 경우 치명적 명령이 실행되는 위험 함수 (예: `Statement.executeQuery()`, `Runtime.exec()`).

</details>

- Source부터 Sink까지 추적하는 **오염 데이터 흐름**
- 경고 코드의 실행 여부를 확인하는 **도달 가능성 분석**
- 보완 통제와 만료일을 요구하는 **기한부 위험 수용**

#### 한줄 요약
- Source-Sanitizer-Sink 오염 분석, 런타임 도달 가능성 검증, 진탐(TP)/오탐(FP) 판별, 기한부 Waiver 통제를 제공한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **정적 분석 결과 4분면 분류 매트릭스 (Confusion Matrix)**:
  1. **참 양성 (True Positive, TP / 진탐)**: 실제 취약점이며 도구도 취약점으로 정확히 경고 (즉각 패치 대상).
  2. **거짓 양성 (False Positive, FP / 오탐)**: 실제로는 안전하나 도구가 취약점으로 잘못 경고 (예외 룰셋 등록).
  3. **거짓 음성 (False Negative, FN / 미탐)**: 실제 취약점이나 도구가 탐지하지 못하고 놓침 (최악의 보안 사고).
  4. **참 음성 (True Negative, TN / 정상)**: 안전한 코드이며 도구도 경고를 발생시키지 않음 (정상).

</details>

```text
[정적 분석 결과 해석 및 트리아지]
├── [Taint Flow 오염 분석]
│   ├── [Source] 외부 입력 유입점
│   ├── [Sanitizer] 정화·살균 로직 검증
│   └── [Sink] 취약점 실행 도달점
├── [결과 분류 판정]
│   ├── [참 양성(TP)] 미정화 취약점 (진탐)
│   └── [거짓 양성(FP)] 정화됨/도달불가 (오탐)
└── [품질 게이트 대응]
    ├── 진탐(TP) ➔ 빌드 즉시 차단(Block)
    ├── 오탐(FP) ➔ 룰셋 예외 등록(Dismiss)
    └── 위험수용 ➔ 조건부 기한부 승인(Waiver)
```

- 선들의 의미:
  - `──`: 보안 분석 절차 연계
  - `├──`, `└──`: 분석 단계 및 대응 조치 분기

| 구성요소 | 책임 |
|:---|:---|
| SAST 스캔 엔진 | AST·CFG 기반 보안 경고 생성 |
| 오염 분석기 | Source부터 Sink까지 Taint Flow 추적 |
| 보안 트리아지 | 도달 가능성과 Sanitizer 유효성 판정 |
| Waiver 대장 | 보완 통제와 만료 기한 관리 |
| 품질 게이트 | 미해결 고위험 진탐 배포 차단 |

#### 한줄 요약
- 오염 분석기와 보안 트리아지가 실제 공격 도달 가능성을 판별하고, 진탐은 즉각 차단하며 오탐과 기한부 Waiver는 예외 대장으로 통제한다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **정적 분석 결과 해석 및 조치 5단계 프로세스**:
  1. 개발자가 코드를 Git에 푸시하면 CI 파이프라인에서 SAST 도구가 소스코드 자동 스캔
  2. 도구가 검출한 경고 목록 중 Critical/High 등급 취약점 자동 추출
  3. 보안 엔지니어가 Taint Flow 및 Sanitizer 유효성을 검토하여 TP vs FP 트리아지 수행
  4. 확인된 진탐(TP)은 개발팀에 즉각 수정 요청하고 CI/CD 파이프라인에서 빌드 머지 차단
  5. 수정 코드 재스캔 후 진탐 0건 확인 시 품질 게이트 통과 및 안전한 프로덕션 배포

</details>

```text
[SAST Scanner Alert] (① SonarQube/Fortify 스캔 및 원시 보안 경고 수집)
└── [Taint Flow Tracker] (② Source-Sanitizer-Sink 오염 경로 및 도달 가능성 추적)
    └── [Security Triage Board] (③ 진탐(TP) vs 오탐(FP) vs 기한부 수용(Waiver) 분류 판정)
        └── [DevSecOps Quality Gate] (④ 진탐 발생 시 PR 머지 차단 및 개발팀 긴급 패치 인계)
            └── [Re-scan & Production Release] (⑤ 취약점 수정 재스캔 통과 및 상용 안전 배포 승인)

- 분기 결과: 진탐(TP) 0건 달성 시 품질 게이트 통과 및 상용 배포, 오탐(FP)은 커스텀 룰셋 예외 처리, 미해결 취약점은 TTL 90일 Waiver 조건부 통과
```

#### 한줄 요약
- 원시 경고의 Taint 경로를 추적해 진탐과 오탐을 가려내고, 진탐을 제거한 뒤 품질 게이트를 통과시킨다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **정적 분석 트리아지 판정 3대 상태 비교**:
  - 참 양성 (True Positive): 실제 익스플로잇 가능한 결함 (즉각 수정).
  - 거짓 양성 (False Positive): 도구의 한계로 인한 오탐 (예외 등록 및 룰 튜닝).
  - 기한부 위험 수용 (Waiver): 즉각 수정 불가하나 보완 통제 적용 (기한부 허용).

</details>

| 비교 항목 | 진탐 (TP) | 오탐 (FP) | 기한부 위험 수용 (Waiver) |
|:---|:---|:---|:---|
| 적용 기준 | 공격 가능 경로 확인 | 안전 경로 확인 (살균됨) | 즉시 수정 불가한 실제 위험 |
| 처리 조치 | 즉각 코드 패치 | 근거 기반 룰셋 예외 등록 | 보완 통제와 만료일(TTL) 설정 |
| 파이프라인 | 품질 게이트 차단 | 정상 빌드 통과 | 조건부 한시 승인 |
| 관리 위험 | 미조치 시 보안 침해 | 오판 시 취약점 은폐 | 만료 방치 시 보안 부채 누적 |

#### 한줄 요약
- 진탐(TP)은 배포 차단 및 즉각 패치, 오탐(FP)은 룰셋 예외 처리, Waiver는 90일 기한부 조건부 승인이다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **중앙 예외 승인(Centralized Waiver Approval)**: 개별 개발자의 임의적인 주석 억제를 방지하고 전사 보안 담당자가 오탐 여부와 잔존 위험을 검토하여 예외를 공인하는 통제 절차.
- **커스텀 룰셋(Custom Rule Set)**: 사내 자체 프레임워크나 살균(Sanitizer) 함수를 SAST 도구가 올바르게 인식하도록 등록하는 맞춤형 분석 규칙.
- **Waiver TTL(Time-To-Live)**: 즉각 조치하기 어려운 취약점에 대해 한시적으로 배포를 허용하되 설정된 유효기간(통상 90일)이 만료되면 빌드를 다시 차단하는 만료 기한.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 개발자의 임의 예외 처리로 진탐 은폐 | 보안 담당자의 중앙 집중식 예외 승인 강제 | 임의 주석 남용 및 취약점 은폐 방지 |
| 사내 자체 필터 미인식으로 오탐 폭증 | 자체 Sanitizer 함수의 커스텀 룰셋 등록 | 도구의 오염 분석 정확도 향상 |
| 위험 수용(Waiver) 만료 후 위험 방치 | Waiver TTL(90일) 만료 시 파이프라인 자동 재차단 | 보안 부채 방치 방지 및 적시 조치 |

#### 한줄 요약
- 중앙 승인으로 주석 남용을 막고, 커스텀 룰셋으로 오탐을 줄이며, 90일 만료제로 Waiver 방치를 차단한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **SAST(Static Application Security Testing)**: 소스코드나 바이트코드를 실행하지 않고 잠재적 보안 취약점과 결함을 정적으로 검출하는 보안 시험 기법.
- **보안 트리아지(Security Triage)**: 정적 분석 결과 중 실제 공격 가능한 진탐(TP)과 도구 한계에 의한 오탐(FP)을 분류하고 조치 우선순위를 결정하는 절차.
- **DevSecOps 품질 게이트(Quality Gate)**: 보안 취약점 점검 결과를 빌드 및 배포 파이프라인의 합격/불합격 판정에 직접 연계하는 자동화 통제 관문.

</details>

- **기술 위상/발전**: SAST Taint Analysis 및 보안 트리아지 기반 DevSecOps 품질 게이트 표준 확립
- **실무 적용/통제**: 보안팀 중앙 집중 오탐 승인, 커스텀 Sanitizer 룰셋 튜닝 및 Waiver TTL(90일) 통제

#### 한줄 요약
- 오염 분석과 보안 트리아지를 통해 오탐을 최소화하고 진탐을 신속히 조치하여 DevSecOps 품질 게이트를 완성한다.
