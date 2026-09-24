---
title: "디자인 씽킹"
author: "Codex"
date: "2026-09-24"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "GPT-6"
---

## 지식 로드맵 내 현재 위치

지식 위치: IT 전략·관리 → 인간중심 혁신·문제해결 → **디자인 씽킹**


## 30초 인출

- 본질: 디자인 씽킹은 사용자의 문제를 관찰·재정의하고 시제품을 시험하며 해법을 찾는 방법이다.
- 메커니즘: Discover에서 관찰하고 **Define** 에서 문제를 재정의한 뒤 Develop·Deliver에서 시제품을 시험하며 피드백을 환류한다.
- 판정 기준: 실제 사용자 관찰과 테스트 결과가 문제 정의와 가설의 수정·채택 근거로 남는지 확인한다.

<details>
<summary>핵심 용어</summary>

- **디자인 씽킹(Design Thinking)** : 사용자 맥락을 이해하고 문제를 재정의해 시제품으로 해법을 시험하는 인간 중심 접근법
- **Design Thinking** : 사용자 공감과 문제 재정의, 시제품 시험을 반복하는 인간 중심 문제해결 방법론
- **Empathize** : 관찰·인터뷰를 통해 사용자의 맥락과 잠재적 니즈를 파악하는 공감 단계
- **Define** : 조사 결과를 종합해 해결할 핵심 문제를 POV 형식으로 재정의하는 문제 정의 단계
- **Ideate** : HMW 질문을 바탕으로 다양한 대안을 발산하고 검증 가설을 도출하는 아이디어 도출 단계
- **POV(Point of View)** : 사용자·니즈·인사이트를 결합하여 정의한 핵심 문제 관점 진술문
- **HMW(How Might We)** : 정의된 문제를 실행 가능한 질문 형태로 전환하는 아이디어 발산 기법
- **Persona** : 사용자 조사 데이터를 바탕으로 목표·행동 양식을 유형화한 가상 대표 사용자 모델
- **CJM(Customer Journey Map)** : 사용자 경험 여정 전반의 터치포인트·감정·페인포인트를 시각화한 분석 도구
- **Prototype** : 핵심 가설과 인터랙션을 빠르게 검증하기 위해 제작한 시험용 시제품
- **UT(Usability Test)** : 실제 사용자의 과업 수행 과정을 관찰하여 인터페이스와 사용성 결함을 발견하는 평가 기법

</details>

---

## 1교시 예상문제 (10점)

> 디자인 씽킹의 주요 단계와 문제 정의·검증 흐름을 설명하시오. (예상·10점)

---

## 1교시 10점 답안

### Ⅰ. **디자인 씽킹** 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **디자인 씽킹**은 사용자 맥락을 파악하고 문제를 재정의해 시제품으로 해법을 시험하는 접근법이다. |
| 목적 | 실제 사용자 필요에 맞는 해법을 찾고 초기 오류를 줄인다. |

### Ⅱ. 핵심 구조 및 체계

- 핵심 메커니즘: 공감(**Empathize**) → 문제정의(**Define**) → 아이디어(**Ideate**) → 시제품(**Prototype**) → 테스트(Test)의 5단계 반복 및 더블 다이아몬드(발산/수렴) 구조

```mermaid
flowchart TD
    E["Empathize"] --> D["Define"]
    D --> I["Ideate"]
    I --> P["Prototype"]
    P --> T["Test"]

    T -.->|심층 재이해| E
    T -.->|문제 재정의| D
    P -.->|아이디어 재발견| I
```

---

## 2~4교시 예상문제 (25점)

> 디자인 씽킹의 개념과 5개 Mode·Double Diamond를 설명하고, 디지털 서비스 개발 적용절차와 고려사항을 제시하시오. **(미출제 예상·25점)**

---

## 2~4교시 25점 답안

## Ⅰ. **디자인 씽킹** 개요

> 디자인 씽킹의 핵심은 아이디어 수가 아니라 사용자 증거로 문제와 해법의 가정을 빠르게 수정하는 데 있음.



| 구분 | 핵심 |
|---|---|
| 정의 | **디자인 씽킹**은 사용자 맥락을 파악하고 문제를 재정의해 시제품으로 해법을 시험하는 접근법이다. |
| 목적 | 실제 사용자 필요에 맞는 해법을 찾고 초기 오류를 줄인다. |

## Ⅱ. 5개 Mode의 활동·산출

> 5개 Mode는 필요에 따라 앞뒤로 이동하며 병렬·반복 수행할 수 있음.

```mermaid
flowchart TD
    E["Empathize"] --> D["Define"]
    D --> I["Ideate"]
    I --> P["Prototype"]
    P --> T["Test"]

    T -.->|심층 재이해| E
    T -.->|문제 재정의| D
    P -.->|아이디어 재발견| I
```

| Mode | 주요 활동 | 산출 |
|---|---|---|
| **Empathize** | 관찰·인터뷰·맥락 탐색 | 관찰기록 · Empathy Map |
| **Define** | 패턴·인사이트·필요 종합 | **Persona** · **CJM** · **POV** |
| **Ideate** | **HMW**·발산·대안 선정 | 아이디어 · 가설 |
| **Prototype** | 핵심 가정의 저비용 표현 | Storyboard · Mock-up |
| **Test** | 사용자 과업 관찰·피드백 | 관찰결과 · 수정 가설 |

## Ⅲ. Double Diamond와 5 Modes 관계

> Double Diamond는 발산·수렴의 큰 구조, 5 Modes는 각 구간에서 활용하는 사고·실행 방식임.

```mermaid
flowchart LR
    subgraph PROBLEM["문제 영역 (Problem Space)"]
        direction LR
        DISC["Discover(발산)"] --> DEF["Define(수렴)"]
    end

    subgraph SOLUTION["해법 영역 (Solution Space)"]
        direction LR
        DEV["Develop(발산)"] --> DEL["Deliver(수렴)"]
    end

    PROBLEM -->|Problem Definition| SOLUTION
```

| Double Diamond | 사고 | 연계 Mode | 판정 |
|---|---|---|---|
| **Discover** | 문제영역 발산 | Empathize | 충분한 사용자·맥락을 탐색했는가? |
| **Define** | 문제영역 수렴 | Define | 근거 있는 문제정의인가? |
| **Develop** | 해법영역 발산 | Ideate·Prototype | 복수 대안을 시험했는가? |
| **Deliver** | 해법영역 수렴 | Prototype·Test | 가치·사용성·실현성을 검증했는가? |

## Ⅳ. 디지털 서비스 적용 절차

> 조사자료가 POV·Prototype·Backlog까지 추적되어야 워크숍 결과가 구현으로 이어짐.

```mermaid
flowchart TD
    S1["사용자 조사"] --> S2["문제 재정의"]
    S2 --> S3["대안·Prototype"]
    S3 --> S4["사용자 Test"]
    S4 --> S5["구현 연결"]
```

## Ⅴ. 문제점·대응책

> 워크숍의 산출물이 사용자 증거와 개발 의사결정으로 이어지지 않으면 형식 활동에 머묾.

| 위험 | 대책 | 효과 |
|---|---|---|
| **내부자 추측** | 실제 사용자·극단 사용자 조사 | 편향 완화 |
| **해법 조기 고정** | Problem Space와 Solution Space 분리 | 문제 재정의 확보 |
| **고충실도 집착** | 검증가정별 최소 Prototype | 학습비용 절감 |
| **개발 단절** | Finding–POV–Backlog 추적 | 구현 정합성 향상 |

## Ⅵ. 출시 후 사용자 증거 환류 제언

| 문제 | 해결 방안 |
|---|---|
| 시제품 시험이 출시 전에 끝나면 실제 이용환경에서 생긴 접근성·과업완료 문제를 놓칠 수 있다. | 핵심 과업과 사용자군을 정해 출시 후 사용성·지원요청 자료를 주기적으로 검토하고, 변화가 필요한 가정을 다음 조사·개선 주기에 반영한다. |

이는 사용자 조사 결과를 서비스 운영으로 연결하기 위한 제안이다.

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [Stanford d.school: Design Thinking Bootleg](https://dschool.stanford.edu/tools/design-thinking-bootleg)
- [Design Council: Double Diamond](https://www.designcouncil.org.uk/resources/the-double-diamond/)

## 연결 토픽

- 이전 토픽: [그로스 해킹](./046_growth_hacking.md)
- 연관 토픽: [애자일 대응 전략](./013_agile_response_strategy.md), [A/B 테스트](./029_ab_testing.md), [MECE](./045_mece.md)
- 다음 토픽: [제안요청서(RFP)](./049_rfp.md)
