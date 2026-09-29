---
title: "술어 논리(Predicate Logic)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags: ["notes-latest-tech"]
sidebar:
  label: "152. 술어 논리(Predicate Logic)"
  order: 152
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>인공지능·기호주의</span><span>지식 표현 및 자동 추론</span><strong>술어 논리(Predicate Logic)</strong></div>

## 30초 인출

- 본질: **술어 논리** (Predicate Logic)는 세계의 대상(개체)과 대상 간의 속성 및 관계를 술어와 한정자($\forall, \exists$)로 정형화하여 기계적 연역 추론을 가능하게 하는 정밀 수리 논리 체계
- 메커니즘: 사실과 규칙을 1차 술어 논리(FOL) 정규형(CNF)으로 변환 → 스콜렘화 및 단일화(Unification) → 분해 증명(Resolution Refutation)을 통한 모순 도출로 결론 입증
- 통찰: 1차 술어 논리는 참인 명제만 유한 단계 내 증명 가능하고 거짓인 명제는 무한 루프에 빠지는 반결정성(Semi-decidability) 한계가 있으므로 절(Clause) 표현을 호른 절(Horn Clause)로 제약하거나 기술 논리(Description Logic) 기반 서브셋 적용 필요

<details><summary>핵심 용어</summary>

- **술어 (Predicate)** : 대상의 성질이나 개체들 간의 상호 관계를 나타내는 함수형 논리 표현식 ($P(x, y)$).
- **한정자 (Quantifier)** : 전칭 한정자($\forall$: 모든)와 존재 한정자($\exists$: 어떤/존재하는)로 변수의 유효 범위를 한정하는 기호.
- **단일화 (Unification)** : 두 개 이상의 논리 표현식이 일치하도록 변수에 적절한 텀(Term)을 치환하는 패턴 매칭 알고리즘.
- **분해 규칙 (Resolution Rule)** : 모순되는 두 절($P \lor Q$ 와 $\neg P \lor R$)을 결합하여 새로운 유도절($Q \lor R$)을 도출하는 자동 정리 증명 규칙.
- **반결정성 (Semi-decidability)** : 타당한 문장은 유한한 시간 내 증명 가능하나, 타당하지 않은 문장의 판정은 영원히 종료되지 않을 수 있는 성질.

</details>

---

## 2~4교시 예상문제 (25점)

> 인공지능 지식 기반 시스템 및 시맨틱 웹의 논리적 기반인 술어 논리(Predicate Logic)의 정의와 구성요소를 설명하고, 명제 논리와의 차이점을 비교한 후, 1차 술어 논리의 자동 추론 메커니즘(단일화, 분해 증명)과 계산 복잡도 한계 극복 방안을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 술어 논리의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 단순 명제의 참·거짓만을 다루는 명제 논리의 한계를 극복하여, 개체(Object), 속성(Property), 관계(Relation)를 변수와 양화사($\forall, \exists$)를 통해 심층 표현하는 1차 수리 논리 체계 |
| 목적 | 지식 베이스(KB)의 의미론적 모호성 제거, 자동 정리 증명(Automated Theorem Proving) 및 전문가 시스템의 연역적 규칙 추론 수행 |

## Ⅱ. 술어 논리의 핵심 구성요소 및 문법적 특징

| 구성 요소 | 구문 표기 및 기호 | 주요 의미 및 특징 |
|---|---|---|
| **상수 (Constants)** | $John, Apple, 3$ | 도메인 내의 특정한 단일 개체 지칭 |
| **변수 (Variables)** | $x, y, z$ | 도메인 내의 임의의 대상을 대신하는 기호 |
| **술어 (Predicates)** | $Human(x), Brother(x, y)$ | 개체의 특성이나 개체 간의 다항 관계(True/False 반환) 표현 |
| **함수 (Functions)** | $FatherOf(x), Sqrt(x)$ | 개체를 입력받아 다른 고유 개체를 반환하는 연산자 |
| **한정자 (Quantifiers)** | $\forall$ (전칭), $\exists$ (존재) | 명제의 적용 대상 범위를 전역 또는 일부로 지정 |
| **논리 연결사 (Connectives)**| $\land, \lor, \neg, \rightarrow, \leftrightarrow$ | 복합 논리식을 구성하기 위한 연산자 |

## Ⅲ. 1차 술어 논리 분해 증명 추론 프로세스

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 1차 술어 논리(FOL) 분해 증명법(Resolution Refutation) 파이프라인 ]   │
└────────────────────────────────────────────────────────────────────────┘

  [ 전제 사실 및 규칙 집합 (KB) ]         [ 증명하고자 하는 질의 (Query $\alpha$) ]
                 │                                        │
                 │ ── 1. 함축 기호 제거 및 부정 도입 ─── │ ($\neg \alpha$)
                 ▼                                        ▼
  [ 절 정규형 변환 (CNF: Conjunctive Normal Form Conversion) ]
   ├── Step 1: 드모르간 법칙 적용 (부정 기호 안쪽 이동)
   ├── Step 2: 변수 표준화 (중복 변수명 분리)
   ├── Step 3: 스콜렘화 (Skolemization: $\exists$ 제거 및 스콜렘 상수/함수 대체)
   └── Step 4: 전칭 한정자($\forall$) 탈락 및 논리곱 표준형 전개
                 │
                 ▼
  [ 절(Clause) 집합 도출 ]
                 │
                 ▼
  [ 가장 일반적인 단일화 (MGU: Most General Unifier) ]
   - 서로 반대 부호를 가진 동일 술어 매칭 (예: $Human(x)$ 와 $\neg Human(socrates)$)
   - 치환집합 생성: $\theta = \{x / socrates\}$
                 │
                 ▼
  [ 분해 규칙 적용 및 소거 (Resolution Step) ]
                 │
                 ▼ (반복 수행)
  [ 공백절 도출 (Empty Clause $\square$ = Contradiction) ] ──> Query $\alpha$는 참(True) 입증
```

| 추론 단계 | 세부 동작 메커니즘 | 공학적 의미 및 산출물 |
|---|---|---|
| **부정 추가** | 증명할 목표 명제 $\alpha$를 부정($\neg \alpha$)하여 지식 베이스에 추가 | 귀류법(Reductio ad Absurdum) 환경 조성 |
| **CNF 변환** | 9단계 정규화 절차를 통해 모든 논리식을 논리합(OR)의 논리곱(AND) 형태로 표준화 | 표준 절 집합(Clauses) |
| **단일화 (Unify)** | 변수와 상수의 바인딩을 통해 두 리터럴이 상쇄될 수 있는 최소 치환 $\theta$ 탐색 | MGU(가장 일반적인 단일화자) |
| **분해 연산** | 상보적 리터럴($L, \neg L$)을 제거하고 나머지 잔여식을 결합하여 새 절 생성 | 유도절(Resolvent) |
| **모순 판정** | 빈 절(NIL)이 생성되면 가정이 거짓임이 밝혀져 원래 목표 명제가 증명 완료 | 증명 트리(Proof Tree) |

## Ⅳ. 명제 논리 vs 1차 술어 논리(FOL) vs 기술 논리(DL) 비교

| 비교 항목 | 명제 논리 (Propositional Logic) | 1차 술어 논리 (FOL) | 기술 논리 (Description Logic) |
|---|---|---|---|
| **기본 단위** | 원자 명제 (P, Q 등 단일 진위값) | 개체, 함수, 술어, 양화사($\forall, \exists$) | 개념(Concept), 역할(Role), 개체(Individual)|
| **표현력** | 매우 낮음 (내부 구조 표현 불가) | 매우 높음 (일반 수학 체계 표현 가능) | 중간 (FOL의 결정 가능한 서브셋) |
| **추론 결정성** | 완벽히 결정 가능 (Decidable) | 반결정 가능 (Semi-decidable) | 결정 가능 (Decidable, 다항 시간~지수 시간) |
| **계산 복잡도** | NP-Complete (SAT 문제) | 언디사이더블 (증명 불가능한 경우 존재) | ExpTime ~ NExpTime (계산 가능성 보장) |
| **대표 활용** | 디지털 회로 설계, SAT 솔버 | 전통 인공지능, Prolog, 정리 증명기 | W3C OWL, 시맨틱 웹 온톨로지, 지식 그래프 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 1차 술어 논리의 반결정성으로 인해 증명되지 않는 거짓 질의 요청 시 분해 증명 루프가 무한 루프에 진입 | 역방향 체이닝(Backward Chaining) 시 탐색 깊이 제한(Depth Limit) 설정 및 긍정 호른 절(Horn Clause) 제약 기반 SLD 분해 적용 |
| 도메인 내 개체 수 증가 시 단일화(Unification) 연산 및 탐색 분기 계수가 기하급수적으로 폭증하는 조합 폭발 발생 | Rete 알고리즘을 도입하여 이전 추론 상태를 메모리에 캐싱하고 조건 노드 네트워크를 공유하여 중복 연산 방지 |
| 참과 거짓의 이분법적 논리 구조로 인해 현실 세계의 불확실성과 확률적 예외 사실 표현 불가능 | 마르코프 로직 네트워크(MLN) 또는 베이지안 확률 네트워크와 결합한 확률적 술어 논리(Probabilistic Soft Logic) 도입 |

## Ⅵ. 제언

현대 지식 기반 AI 아키텍처에서는 FOL의 과도한 복잡도를 지양하고, W3C 표준인 기술 논리(Description Logic) 기반 온톨로지와 벡터 임베딩을 결합한 하이브리드 지식 그래프 검색 체계 구축 필요.

```text
[ 비정형 텍스트 & 엔티티 데이터 ]
              │
              ▼
[ 기술 논리(DL) 기반 온톨로지 지식 그래프 (RDF/OWL Triplet) ]
   ├── Step 1: <Entity-Relation-Entity> 정형 트리플 구축
   ├── Step 2: 결정 가능한 서브셋(OWL 2 DL) 기반 자동 일관성 검증
   └── Step 3: Graph RAG 엔진과 연계하여 심볼릭 추론 경로 생성
              │
              ▼
[ LLM 프롬프트 그라운딩 (환각 없는 연역적 사실 기반 생성) ]
```

| 구분 | 순수 1차 술어 논리 (Prolog 방식) | 제언: DL 기반 온톨로지 + Graph RAG |
|---|---|---|
| **추론 완료 보장** | 무한 루프로 인한 중단 불가 위험 | 결정 가능한 범위 내에서 반드시 추론 종료 |
| **확장성** | 대규모 데이터베이스 연동 곤란 | 대용량 트리플 스토어(Graph DB) 고속 쿼리 |
| **모호성 대응** | 규칙에 없는 예외 발생 시 에러 | LLM의 의미론적 임베딩과 연계하여 유연 대응 |
| **상용 표준** | 비표준 독자 룰 엔진 구동 | W3C RDF/SPARQL 글로벌 표준 인터페이스 준수 |

## 출제 이력과 검증 출처

- Stuart Russell & Peter Norvig, "Artificial Intelligence: A Modern Approach" Ch 8 First-Order Logic & Ch 9 Inference in First-Order Logic
- John Alan Robinson, "A Machine-Oriented Logic Based on the Resolution Principle" (JACM 1965)
- W3C Recommendation, "OWL 2 Web Ontology Language Document Overview"

## 연결 토픽

- 상위 토픽: [143 귀납적 추론](./143_inductive_reasoning.md)
- 연관 토픽: [182 시맨틱 웹](./182_semantic_web.md), [183 온톨로지](./183_ontology.md)
