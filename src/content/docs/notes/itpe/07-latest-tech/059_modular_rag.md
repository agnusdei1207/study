---
title: "모듈러 RAG(Modular RAG)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "059. Modular RAG"
  order: 59
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>자연어 처리</span><span>검색 증강 생성</span><strong>모듈러 RAG(Modular RAG)</strong></div>

## 30초 인출

- 본질: **모듈러 RAG(Modular RAG)** 는 전통적인 선형적 '검색-생성' 파이프라인을 탈피하여 질의 변환, 라우팅, 다중 검색, 리랭킹, 자체 평가 등의 기능을 독립 모듈로 세분화하고 레고처럼 유연하게 조립하는 아키텍처
- 메커니즘: 질의 분석 및 확장 → 시맨틱 라우터를 통한 최적 검색 경로 선택 → 하이브리드 검색 및 융합(Fusion) → 문맥 압축 및 자체 성찰(Self-Reflection) → 답변 생성
- 통찰: 다단계 모듈 호출로 인한 엔드투엔드 응답 지연(Latency)이 발생하므로 질의 복잡도별 바이패스(Bypass) 라우팅과 비동기 병렬 검색 파이프라인 구축 필수

<details><summary>핵심 용어</summary>

- **모듈러 RAG(Modular RAG)** : RAG의 핵심 단계들을 독립 컴포넌트로 분리하여 작업에 맞춰 동적으로 재구성하는 프레임워크.
- **시맨틱 라우팅(Semantic Routing)** : 사용자 질의의 의도와 복잡도를 분석하여 RAG 검색 경로, 웹 검색, 또는 순수 LLM 답변으로 분기하는 기술.
- **RAG-Fusion** : 다중 쿼리로 변환된 검색 결과들을 상호 순위 융합(RRF, Reciprocal Rank Fusion) 알고리즘으로 통합 재정렬하는 기법.
- **Self-RAG** : 모델이 검색의 필요성 여부와 검색된 문서의 적합성을 스스로 판정(Reflection Token)하며 적응적으로 생성하는 방식.
- **문맥 압축(Context Compression)** : 긴 검색 문서에서 질의와 무관한 토큰을 제거하고 핵심 단락만 선별하여 LLM 프롬프트에 주입하는 기법.

</details>

---

## 2~4교시 예상문제 (25점)

> 생성형 AI 서비스의 환각을 해결하기 위한 RAG 기술의 진화 단계(Naive, Advanced, Modular RAG)를 비교하고, 모듈러 RAG의 핵심 구성 모듈 및 다단계 파이프라인 적용 시의 레이턴시·비용 최적화 방안을 논하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 모듈러 RAG(Modular RAG)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **모듈러 RAG(Modular RAG)** 는 고정된 선형 파이프라인을 벗어나 질의 분석, 검색, 라우팅, 융합, 문맥 정제, 자체 평가 모듈을 독립적으로 구성하여 문제에 맞게 동적으로 조합하는 차세대 RAG 프레임워크 |
| 목적 | 단일 벡터 검색의 재현율 한계 극복, 복잡한 다단계 추론(Multi-hop Reasoning) 지원 및 질의별 최적 경로 매핑을 통한 API 비용 및 환각 억제 |

## Ⅱ. 모듈러 RAG의 핵심 특징

| 구분 | 주요 특징 | 기술적 메커니즘 및 엔지니어링 구현 |
|---|---|---|
| **아키텍처 유연성** | 레고형 교체 가능성 (Pluggable) | 개별 모듈(임베딩, 리랭커, LLM)을 시스템 전체 중단 없이 핫스왑(Hot-swap) 방식으로 교체 및 업그레이드 |
| **지능형 분기** | 적응형 동적 라우팅 (Routing) | 단순 질문은 즉각 생성, 전문 법률 질문은 하이브리드 검색과 리랭킹 모듈로 연결하는 동적 경로 선택 |
| **반복적 추론** | 다중 턴 순환 패턴 (Iterative/Loop) | 초기 검색 결과가 불충분할 경우 스스로 하위 질의(Sub-query)를 생성하여 반복 검색하는 에이전틱 피드백 |
| **문맥 정제** | 정보 밀도 극대화 (Refinement) | 검색된 청크 중 중복 및 노이즈 문장을 필터링하여 프롬프트 컨텍스트 윈도우 낭비 원천 차단 |

## Ⅲ. 모듈러 RAG의 아키텍처 및 6대 핵심 모듈 체계

```text
┌────────────────────────────────────────────────────────────────────────┐
│             [ 모듈러 RAG(Modular RAG) 동적 오케스트레이션 체계 ]            │
└────────────────────────────────────────────────────────────────────────┘
      │
      ▼
 [ 질의 입력 ]
      │
      ▼
 [ 1. Query 모듈 ] ── 하위 질의 분해(Sub-queries) / 가상 문서 생성(HyDE)
      │
      ▼
 [ 2. Router 모듈 ] ─ 질의 의도 분류 ──┬─ 단순 상식 ──────────> [ 직접 LLM 답변 ]
      │                                 └─ 전문 지식 요구       (검색 모듈 바이패스)
      ▼                                         │
 [ 3. Search 모듈 ] ◄───────────────────────────┘
      ├── Dense Retrieval (Milvus 벡터 유사도)
      ├── Sparse Retrieval (BM25 키워드 매칭)
      └── Knowledge Graph (엔티티 관계 탐색)
      │
      ▼
 [ 4. Fusion & Rerank 모듈 ] ── RRF(Reciprocal Rank Fusion) + Cross-Encoder 재순위화
      │
      ▼
 [ 5. Refinement 모듈 ] ────── LongLLMLingua 기반 문맥 토큰 압축 및 노이즈 제거
      │
      ▼
 [ 6. Generator & Eval 모듈 ] ─ LLM 최종 생성 및 Self-RAG 사실성 평가 ──> [ 고신뢰 답변 ]
```

| 모듈 분류 | 세부 기능 및 역할 | 핵심 기술 요소 |
|---|---|---|
| **Query Module** | 모호한 사용자 질문을 검색 친화적 형태로 재구성 | HyDE, Multi-Query Expansion, Step-back Prompting |
| **Router Module** | 질문 성격에 따라 가장 적합한 검색 엔진 및 모듈 선택 | Semantic Router, Intent Classifier, LLM Function Calling |
| **Search Module** | 다차원 소스에서 후보 문서 청크 수집 | Hybrid Search (Dense + Sparse), GraphRAG |
| **Fusion & Rerank** | 여러 검색 결과의 점수를 결합하고 정밀도 순 정렬 | RRF 알고리즘, BGE-Reranker, Cohere Rerank |
| **Refinement** | LLM 입력 전 토큰 압축 및 문맥 재구성 | Context Compression, Selective Context, Chunk Merging |
| **Evaluation** | 답변의 근거 충실도 및 환각 실시간 자체 검증 | Self-RAG Reflection Token, Ragas Faithfulness |

## Ⅳ. Naive RAG, Advanced RAG, Modular RAG 비교

| 비교 항목 | Naive RAG (전통적 1세대) | Advanced RAG (개선된 2세대) | Modular RAG (차세대 3세대) |
|---|---|---|---|
| **파이프라인 형태** | 고정된 선형 구조 (Retrieve-Read) | 고정된 전/후처리 확장 구조 | 동적 그래프 및 순환형 모듈러 구조 |
| **질의 처리** | 원본 질의 그대로 임베딩 검색 | 쿼리 재작성, 확장 적용 | 복합 질의 분해 및 시맨틱 라우팅 |
| **검색 전략** | 단일 벡터 유사도(Dense) 검색 | 사전/사후 필터링, 하이브리드 | 벡터+키워드+지식그래프 다중 융합 |
| **실행 흐름** | 1회성 순차 실행 | 1회성 파이프라인 실행 | 조건부 분기, 반복(Iterative), 자기 성찰 |
| **시스템 복잡도** | 매우 낮음 | 보통 | 높음 (오케스트레이션 레이어 필요) |
| **주요 적용 대상** | 단순 FAQ 챗봇, PoC 프로토타입 | 표준 문서 기반 사내 Q&A 시스템 | 복잡한 금융/의료 추론, 자율 에이전트 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 다단계 모듈(하위 질의 분해, 다중 검색, 리랭킹, 문맥 압축) 연쇄 실행으로 인한 서빙 레이턴시 급증 | 임베딩 기반 시맨틱 라우터로 단순 질의 시 고비용 모듈을 바이패스(Bypass)하고 비동기 코루틴 병렬 검색(Async I/O) 적용 |
| 복잡한 모듈 간 데이터 규격 불일치 및 특정 모듈 장애 시 전체 파이프라인이 중단되는 카스케이딩 오류 | Pydantic 기반 표준 입출력 스키마 강제, 모듈별 서킷 브레이커(Circuit Breaker) 및 실패 시 기본 Naive RAG 자동 폴백 |
| 지식 그래프, 벡터 DB, 웹 검색 모듈 간 스코어 정규화 기준 차이로 인한 비효율적 순위 융합 | 정규화가 불필요한 상호 순위 융합(RRF, Reciprocal Rank Fusion) 알고리즘 표준 채택 및 Cross-Encoder 리랭커 후처리 |

## Ⅵ. 제언

지능형 시맨틱 라우터와 셀프 리플렉션(Self-RAG) 모듈을 결합하여 질의 난이도에 따라 동적으로 최적 경로를 선택하는 비용·성능 적응형 모듈러 RAG 아키텍처 구축.

```text
[ 사용자 질의 유입 ] ──> [ 시맨틱 라우터 (Semantic Router) ]
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼ (단순 질의)             ▼ (표준 질의)             ▼ (복합 추론 질의)
   [ 경로 A: Fast Path ]     [ 경로 B: Standard Path ]  [ 경로 C: Deep Multi-Hop Path ]
   - RAG 바이패스            - 하이브리드 검색          - 하위 질의 분해 (Sub-queries)
   - 캐시 / 직접 LLM 응답    - 고속 Reranker            - GraphRAG + 벡터 융합 검색
         │                         │                    - 문맥 압축 및 반복 Self-RAG
         ▼                         ▼                         ▼
   [ 200ms 초고속 응답 ]     [ 800ms 고정밀 응답 ]      [ 2.5s 심층 분석 고신뢰 보고서 ]
```

| 구분 | 단일 경로 고정형 RAG | 제언: 적응형 모듈러 RAG 플랫폼 |
|---|---|---|
| **평균 응답 지연** | 모든 질의가 2~3초 소요 | 단순 질의 80%는 0.3초 이내 응답 |
| **토큰 및 컴퓨팅 비용** | 일괄 고비용 모듈 통과로 비용 낭비 | 질의 난이도별 최적 모듈 활성화로 TCO 50% 절감 |
| **복합 질의 정확도** | 단일 검색 한계로 답변 실패 | 하위 질의 분해 및 지식그래프 융합으로 해결 |

## 출제 이력과 검증 출처

- 제139회 정보관리기술사 1교시: Advanced RAG와 Modular RAG의 구조적 차이점 비교
- Yunfan Gao et al., Modular RAG: Transforming RAG Systems into LEGO-like Reconfigurable Frameworks
- Akari Asai et al., Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection
- LangChain & LlamaIndex Architecture Guides, Advanced Retrieval Patterns

## 연결 토픽

- 상위 토픽: [071 초거대 AI](./071_hyperscale_ai.md)
- 연관 토픽: [068 하이브리드 검색](./068_hybrid_search.md), [053 LLMOps](./053_llmops.md), [052 DSLM](./052_dslm.md)
