---
title: "벡터 데이터베이스"
author: "Antigravity"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## Ⅰ. 생성형 AI 시대를 지탱하는 벡터 데이터베이스(Vector DB) 개요

### 가. 벡터 데이터베이스의 정의
- 텍스트, 이미지, 음성 등 비정형 데이터를 AI 임베딩 모델(Embedding Model)을 통해 고차원 밀집 벡터(Dense Vector)로 변환한 후, 이를 효율적으로 저장하고 초고속으로 **근사 최근접 이웃(ANN, Approximate Nearest Neighbor)** 검색을 수행할 수 있도록 특화된 데이터베이스.
- 거대언어모델(LLM)의 컨텍스트 창 한계와 환각(Hallucination) 현상을 극복하기 위한 검색 증강 생성(RAG)의 핵심 장기 기억(Long-term Memory) 인프라.

### 나. 전통적 RDBMS 인덱스 vs 벡터 데이터베이스 인덱스
- **RDBMS (B-Tree)** : 단차원 스칼라 값의 정확한 일치(Exact Match) 또는 범위 검색($O(\log n)$).
- **Vector DB (ANN)** : 수백~수천 차원 공간에서 벡터 간 각도 및 거리 기반의 의미론적 유사도(Semantic Similarity) 검색.

---

## Ⅱ. 벡터 데이터베이스의 핵심 유사도 척도 및 ANN 인덱싱 알고리즘

### 가. 3대 벡터 거리 측정 척도

```text
[ 고차원 벡터 유사도 측정 방식 ]
1. 코사인 유사도 (Cosine)     : cos(	heta) = (A cdot B) / (||A|| * ||B||) -> 방향성 일치 측정 (-1 ~ 1)
2. 유클리디안 거리 (L2)       : d(A, B) = sqrt{sum (A_i - B_i)^2}         -> 절대적 직선 거리
3. 내적 (Dot Product / IP)   : A cdot B = sum A_i * B_i                  -> 정규화 벡터 시 코사인과 동일
```

### 나. 핵심 ANN(Approximate Nearest Neighbor) 인덱싱 알고리즘 비교

| 알고리즘 계열 | 대표 기술 | 동작 원리 및 메커니즘 | 장점 | 트레이드오프 (한계) |
| :--- | :--- | :--- | :--- | :--- |
| **그래프 기반** | **HNSW** (Hierarchical Navigable Small World) | 다계층 스킵리스트 개념을 그래프로 확장하여 상위 계층에서 거친 탐색 후 하위 계층에서 정밀 탐색 | 현존 최고 수준의 검색 속도 및 높은 재현율(Recall) | 인덱스 빌드 시간 오래 걸림, 막대한 메모리(RAM) 소모 |
| **양자화 기반** | **IVF-PQ** (Inverted File Product Quantization) | 고차원 공간을 보로노이 셀로 분할(IVF)하고 벡터를 저용량 바이트 코드로 압축(PQ) | 압축을 통한 획기적인 메모리 절감, 대규모 스케일 | 양자화 오차로 인한 재현율(Recall) 손실 발생 |
| **트리 기반** | **ANNOY** (Spotify) | 초평면(Hyperplane)을 사용하여 고차원 공간을 반복적으로 이등분하는 다중 이진 트리 구성 | 가볍고 직관적, 읽기 전용 정적 데이터에 우수 | 실시간 동적 벡터 추가/갱신 불가 (재구축 필요) |
| **해시 기반** | **LSH** (Locality Sensitive Hashing) | 거리가 가까운 벡터일수록 동일한 버킷에 해싱될 확률이 높은 특수 해시 함수 사용 | 알고리즘 단순 | 차원이 높아질수록 재현율 급락 |

---

## Ⅲ. RAG 파이프라인에서의 벡터 DB 아키텍처 및 메타데이터 필터링

### 가. RAG 아키텍처 내 벡터 DB의 역할

```text
[ RAG(검색 증강 생성) 동작 흐름 ]
[문서 청킹] ---> [임베딩 모델] ---> [고차원 벡터 저장] (Vector DB)
                                           ^
                                           | (ANN 유사도 검색)
[사용자 질문] -> [질문 임베딩] -------------+
                                           |
                                           v
[Top-K 유사 청크 추출] + [원본 질문] ---> [LLM 프롬프트 주입] ---> [정확한 답변 생성]
```

### 나. 하이브리드 검색(Hybrid Search)의 필수성
- 순수 벡터 검색은 '의미론적 맥락'은 잘 찾지만 고유명사, 제품 품번, 법조문 번호 등 **정확한 키워드 매칭(Exact Match)** 에 실패하는 취약점이 존재.
- **해법** : 전통적 역색인(BM25) 키워드 검색과 밀집 벡터(Dense) 검색을 결합하고, RRF(Reciprocal Rank Fusion) 알고리즘으로 순위를 재조정하는 하이브리드 검색 구현.

---

## Ⅳ. 벡터 데이터베이스 도입 및 운영을 위한 실무 제언

- **전용 Vector DB vs 범용 DB 확장 모듈 선택 기준** :
  - **전용 DB (Milvus, Pinecone, Qdrant, Weaviate)** : 수천만 건 이상의 대규모 임베딩 벡터, 초당 수천 QPS 처리, 고급 분산 샤딩이 필요한 경우 적합.
  - **범용 확장 (PostgreSQL + pgvector)** : 기존 RDBMS 인프라 재활용, 메타데이터와의 복합 트랜잭션 조인이 핵심이고 수백만 건 이하인 경우 TCO 관점에서 최적.
- **임베딩 모델 변경에 따른 재인덱싱 비용 사전 대비** : 최신 임베딩 모델로 교체 시 기존의 모든 문서를 다시 임베딩하고 Vector DB를 전면 재구축해야 하므로, 원천 청크 텍스트를 안전하게 보관하는 스토리지 계층을 반드시 분리 운영할 것을 제언함.
