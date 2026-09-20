---
title: "클래스 다이어그램(Class Diagram)"
author: "Codex"
date: "2026-09-20T19:39:00+09:00"
tags: ["notes-software-engineering"]
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 UML 정적 모델과 객체지향 구조를 거쳐 클래스 다이어그램으로 이어지는 지식 위치"><span>소프트웨어 공학</span><span>UML · 정적 구조 모델</span><strong>클래스 다이어그램</strong></div>

## 큰 그림과 30초 인출

- 본질: **UML(Unified Modeling Language) Class Diagram**은 분류자의 특성과 관계를 표현하는 정적 구조 모델
- 메커니즘: 클래스의 이름·속성·오퍼레이션을 구획하고 연관·일반화·실체화·의존 관계를 연결함
- 산출: 책임·다중성·탐색 방향·생명주기 소유권이 명시된 설계 모델

<div class="itpe-pipeline is-vertical" role="img" aria-label="클래스 다이어그램의 클래스 내부와 외부 관계">
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>클래스 구획</strong></span><small><b>구성</b> 이름 · 속성 · 오퍼레이션<br /><b>표기</b> 가시성 · 타입 · 매개변수</small></div><div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>관계 명세</strong></span><small><b>구성</b> 연관 · 일반화 · 실체화 · 의존<br /><b>표기</b> 다중성 · 역할 · 탐색 방향</small></div><div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>소유권 판정</strong></span><small><b>구성</b> 집약 · 합성<br /><b>판정</b> 공유 여부 · 생명주기 종속</small></div>
</div>

<details><summary>핵심 용어</summary>

- **UML(Unified Modeling Language)**: 소프트웨어 구조와 행위를 공통 기호로 명세·시각화하는 모델링 언어
- **Multiplicity(다중성)**: 관계 끝에서 허용되는 인스턴스 수 범위를 나타내는 제약
- **Generalization(일반화)**: 하위 분류자가 상위 분류자의 특성을 상속하는 is-a 관계
- **Realization(실체화)**: 구현 분류자가 명세 분류자의 계약을 수행하는 관계
- **Aggregation(집약)**: 부분이 전체와 독립적으로 존재하고 공유될 수 있는 약한 전체-부분 관계
- **Composition(합성)**: 부분이 한 전체에 배타적으로 속하고 생명주기를 함께하는 강한 전체-부분 관계

</details>

## 예상문제

> UML 클래스 다이어그램의 구성요소와 관계 표기법을 설명하고, 집약과 합성을 비교한 후 정적 구조 모델의 품질 확보 방안을 제시하시오.

## Ⅰ. 객체지향 시스템의 정적 구조 모델

> 클래스 다이어그램은 코드 목록이 아니라 책임과 관계 제약을 합의하는 모델이며, 정확성은 기호 수보다 다중성과 소유권의 일관성으로 판정함.

- 정의: **클래스**의 특성과 **정적 관계**를 **UML 표기법**으로 명세하는 구조 다이어그램
- 목적: 책임·타입·관계 제약의 공통 이해 확보 → 설계·구현·검증 간 구조 정합성 유지

## Ⅱ. 클래스의 3단 구획과 가시성

> 구획에는 의사결정에 필요한 도메인 특성만 남기고 기계적으로 생성되는 접근자는 생략해야 모델의 책임 경계가 보임.

| 구획 | 표기 | 판정 |
|---|---|---|
| 이름 | 스테레오타입 · 클래스명 | 추상화 수준과 역할 식별 |
| 속성 | `가시성 이름: 타입` | 상태와 정보은닉 경계 |
| 오퍼레이션 | `가시성 이름(매개변수): 반환타입` | 외부에 제공하는 책임 |

- **가시성**: Public `+` · Private `-` · Protected `#` · Package `~`
- **추상 표기**: 추상 클래스·오퍼레이션은 이탤릭체, 인터페이스는 스테레오타입 등 UML 표기 적용

## Ⅲ. 관계의 의미와 표기

> 관계는 선 모양을 외우는 데서 끝나지 않고 참조 지속성·계약 이행·상속·소유권 중 무엇을 뜻하는지 코드와 일치해야 함.

| 관계 | 표기 | 의미 | 검증 질문 |
|---|---|---|---|
| **Association** | 실선 | 구조적 참조 | 다중성·역할·탐색 방향이 맞는가 |
| **Dependency** | 점선 화살표 | 일시적 사용 | 매개변수·지역 사용에 그치는가 |
| **Generalization** | 실선·빈 삼각형 | 특성 상속 | 치환 가능한 is-a 관계인가 |
| **Realization** | 점선·빈 삼각형 | 계약 구현 | 명세의 오퍼레이션을 이행하는가 |
| **Aggregation** | 전체 쪽 빈 마름모 | 공유 가능한 부분 | 부분이 독립·공유 가능한가 |
| **Composition** | 전체 쪽 채운 마름모 | 배타적 소유 | 부분의 생명주기가 전체에 종속되는가 |

## Ⅳ. 집약과 합성의 경계 판정

> 전체-부분이라는 말만으로 합성을 선택하면 안 되며, 배타적 소유와 생성·삭제 책임이 모두 성립할 때만 강한 생명주기 관계를 표시함.

| 기준 | 집약 | 합성 |
|---|---|---|
| 소유 | 공유 가능 | 한 전체에 배타적 |
| 생명주기 | 부분 독립 | 전체에 종속 |
| 이동 | 다른 전체로 이전 가능 | 소유 경계 안에서 관리 |
| 표기 | 빈 마름모 | 채운 마름모 |
| 구현 판단 | 일반 참조로 충분한지 확인 | 생성·삭제·무결성 규칙 동반 |

## Ⅴ. 모델과 구현의 양방향 정합성

> 클래스 다이어그램의 가치는 문서 완성이 아니라 구현 변화 뒤에도 핵심 책임·다중성·소유권이 유지되는 데 있음.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 집약과 합성의 차이는 마름모 색이 아니라 누가 부분의 생명주기를 소유하는가에 있다. 소유권이 모호하면 삭제와 무결성 정책도 모호해진다.
- `나라면`: 핵심 도메인 클래스와 관계 제약만 모델링하고, 코드 리뷰에서 다중성·상속·합성의 구현 정합성을 함께 확인하겠다.

### 실전 답안용 기술사적 제언

- 판정: 장식적 관계선과 불명확한 다중성이 구현 해석 차이의 원인
- 대안: 관계별 의미 질문과 소유권 규칙을 모델 리뷰 체크리스트로 적용
- 검증: 코드의 참조·상속·생성·삭제 규칙과 다이어그램 양방향 대조
- 효과: 과도한 상속 억제 · 생명주기 오류 예방 · 구조 의사소통 향상

<div class="itpe-pipeline is-vertical" role="img" aria-label="클래스 다이어그램 품질 개선 제언"><div class="itpe-pipeline-node"><strong>표기 중심 모델</strong><small><b>문제</b> 다중성·역할·소유권 해석 불일치</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>관계 의미 규칙</strong><small><b>대안</b> 참조 지속성·치환성·생명주기 질문 적용</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>모델-코드 대조</strong><small><b>판정</b> 관계·다중성·생성·삭제 규칙 일치</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>정적 구조 정합성</strong><small><b>효과</b> 변경 영향과 무결성 경계 명료화</small></div></div>

## 1교시 10점 답안 발췌

- 정의: **UML(Unified Modeling Language) Class Diagram**은 **클래스**의 특성과 **정적 관계**를 명세하는 구조 다이어그램
- 목적: 책임·타입·관계 제약의 공통 이해 확보 → 설계와 구현의 구조 정합성 유지
- 구성: 이름·속성·오퍼레이션의 3단 구획, `+`·`-`·`#`·`~` 가시성
- 관계: Association·Dependency·Generalization·Realization·Aggregation·Composition
- 결론: **Multiplicity(다중성)**와 생명주기 소유권을 코드와 대조하여 관계의 의미를 보존함

## 출제 이력과 검증 출처

- [Object Management Group, UML 2.5.1 Specification](https://www.omg.org/spec/UML/2.5.1/About-UML)
- [Object Management Group, UML resources](https://www.omg.org/uml/)

## 학습 체크

- [ ] Ⅰ·정의와 목적: 클래스·정적 관계·UML 표기법의 관계를 두 줄로 재현할 수 있는가
- [ ] Ⅱ·구획: 이름·속성·오퍼레이션 형식과 네 가시성 기호를 쓸 수 있는가
- [ ] Ⅲ·관계: 여섯 관계의 선 표기·의미·검증 질문을 연결할 수 있는가
- [ ] Ⅳ·비교: 집약과 합성을 소유·생명주기·이동·구현으로 비교할 수 있는가
- [ ] Ⅴ·제언: 모델과 코드의 네 대조 대상을 설명할 수 있는가

## 연결 토픽

- [UML 다이어그램](./020_uml_diagrams/)
- [객체지향 설계원칙 SOLID](./082_solid/)
- [모듈성(결합도·응집도)](./190_modularity/)
- [추상 클래스와 인터페이스](./205_abstract_class_and_interface/)
