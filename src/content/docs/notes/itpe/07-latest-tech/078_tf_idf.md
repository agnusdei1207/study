---
title: "TF-IDF(Term Frequency-Inverse Document Frequency)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "078. TF-IDF(Term Frequency-Inverse Document Frequency)"
  order: 78
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

<div class="itpe-topic-path" aria-label="지식 경로">
인공지능·자연어처리 > 정보 검색·텍스트 벡터화 > 어휘 빈도 가중치 > TF-IDF
</div>

## 30초 인출

- 본질: 개별 문서 내 단어 출현 빈도(TF)와 전체 말뭉치에서의 희소성(IDF)을 결합하여 특정 문서 내 단어의 정보적 중요도를 수치화하는 고전 통계적 가중치 산출 알고리즘.
- 메커니즘: 문서 내 단어 출현 횟수 기반 TF 계산 $\rightarrow$ 전체 문서 수 대비 해당 단어 포함 문서 비율의 역수 로그 취득(IDF) $\rightarrow$ TF와 IDF의 곱($TF \times IDF$)을 통한 가중치 행렬 생성 $\rightarrow$ 벡터 공간 모델(VSM) 기반 코사인 유사도 검색.
- 통찰: 단순 어휘 일치 기반 가중치 부여 방식으로 인해 동음이의어 및 문맥적 의미 파악이 불가능하고 고차원 희소 행렬(Sparse Matrix) 메모리 비효율이 발생하므로 BM25 정규화 및 Dense Embedding과의 하이브리드 검색 결합 필수.

<details><summary>핵심 용어</summary>

- **TF(Term Frequency):** 특정 문서 $d$ 안에서 특정 단어 $t$가 등장하는 빈도수 또는 문서 길이로 정규화한 상대 빈도.
- **DF(Document Frequency):** 전체 말뭉치(Corpus) 중에서 단어 $t$를 하나 이상 포함하고 있는 문서의 총 개수.
- **IDF(Inverse Document Frequency):** 전체 문서 수 $N$을 $DF(t)$로 나눈 후 로그를 취한 값으로, 모든 문서에 흔하게 등장하는 불용어의 가중치를 억제하는 역빈도 지표.
- **희소 표현(Sparse Representation):** 어휘 사전 크기만큼의 고차원 벡터 공간에서 대부분의 원소가 0으로 채워지는 벡터 표현 방식.
- **스무딩(Smoothing):** 특정 단어가 말뭉치에 아예 등장하지 않거나 모든 문서에 등장할 때 분모가 0이 되거나 IDF가 0이 되는 현상을 방지하기 위해 상수를 가산하는 기법.
- **BM25(Best Matching 25):** TF-IDF를 기반으로 문서 길이 정규화 계수와 단어 빈도 포화(Saturation) 매개변수를 도입한 진화형 검색 랭킹 알고리즘.
</details>

---

## 2~4교시 예상문제 (25점)

> 자연어 처리 및 정보 검색에서 널리 활용되는 TF-IDF(Term Frequency-Inverse Document Frequency)의 개념, 수학적 산출 수식, 계산 절차를 구체적 예시와 함께 설명하고, 현대 검색 엔진(RAG 포함) 환경에서 나타나는 한계점과 이를 극복하기 위한 하이브리드 검색 발전 방안을 제시하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 단어 중요도 수치화 기법, TF-IDF의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 개별 문서 내 단어 빈도(TF)와 전체 말뭉치 내 역문서 빈도(IDF)를 곱하여 특정 문서 내 단어의 차별적 중요도를 산출하는 통계 기반 텍스트 가중치 모델 |
| 목적 | 단순 불용어(Stopwords) 가중치 제거, 문서의 핵심 주제 단어 추출, 벡터 공간 모델(VSM) 기반 문서 분류 및 유사도 검색 수행 |

- 텍스트 말뭉치를 컴퓨터가 처리 가능한 수치 벡터(Document-Term Matrix)로 변환하는 BoW(Bag-of-Words) 모델의 대표적 가중치 부여 방식.
- 관사나 조사처럼 빈도는 높으나 의미가 없는 단어의 영향력을 수학적으로 억제하고, 특정 문서에만 집중 등장하는 차별화 단어에 높은 가중치 부여.

## Ⅱ. TF-IDF의 핵심 수식 및 원리 특성

| 핵심 수식 항목 | 산출 공식 | 수식의 수학적 의미 및 특성 |
|---|---|---|
| 단어 빈도(TF) | $TF(t, d) = \frac{f(t, d)}{\sum_{t' \in d} f(t', d)}$ | 문서 $d$ 내에서 단어 $t$가 많이 등장할수록 해당 문서의 주제와 직결된다는 비례 특성 |
| 역문서 빈도(IDF) | $IDF(t, D) = \log\left(\frac{|D|}{1 + |\{d \in D : t \in d\}|}\right)$ | 전체 문서 $|D|$ 대비 단어 $t$를 포함하는 문서 수가 많을수록 정보량이 적다고 판정하여 가중치 감쇄 |
| TF-IDF 결합 | $TF\text{-}IDF(t, d, D) = TF(t, d) \times IDF(t, D)$ | 문서 국소적 빈도와 말뭉치 전역적 희소성의 기하학적 결합으로 차별적 중요도 결정 |
| 평활화(Smoothing) | $IDF_{smooth}(t) = \log\left(\frac{1 + |D|}{1 + DF(t)}\right) + 1$ | 분모 0에 의한 발산 방지 및 전체 문서 등장 단어의 IDF 0화(무시) 방지 특성 |

| 원리 특성 | 세부 내용 |
|---|---|
| 정보 엔트로피 반영 | 널리 퍼진 보편적 단어는 엔트로피가 높아 가중치를 낮추고, 희소한 전문 용어는 높은 가중치 획득 |
| 어휘 순서 무시(Unigram) | 문장 내 단어의 순서(Order)나 문맥(Context)을 고려하지 않는 독립성 가정(Bag-of-Words) 전제 |
| 결정론적 계산 | 확률적 근사 없이 주어진 말뭉치 통계에 의해 수학적으로 유일한 벡터 값이 즉시 산출되는 결정론적 특성 |

## Ⅲ. TF-IDF 행렬 계산 프로세스 및 예시

```text
+-------------------------------------------------------------------------------------------------+
|                                TF-IDF Matrix Calculation Pipeline                               |
+-------------------------------------------------------------------------------------------------+
 [Corpus Documents] ---> [Tokenization & Cleansing] ---> [Term-Document Matrix (Raw Count)]
   Doc 1: 사과 바나나        형태소 분석 및 토큰 추출        Doc 1: 사과=1, 바나나=1, 과일=0
   Doc 2: 사과 과일          불용어 정제 완료                Doc 2: 사과=1, 바나나=0, 과일=1
                                                                     |
                                                                     v
 [TF-IDF Vector Space] <--- [Multiplication] <--- [TF Matrix] & [IDF Vector]
   Doc 1: [0.00, 0.69, 0.00]   TF(t,d) x IDF(t)     TF: Doc별 상대빈도   IDF: log(N / DF(t))
   Doc 2: [0.00, 0.00, 0.69]                        - Doc1 사과: 0.5     - 사과: log(2/2) = 0
   (바나나/과일이 핵심 키워드)                      - Doc1 바나나: 0.5   - 바나나: log(2/1) = 0.69
```

| 계산 프로세스 단계 | 주요 수행 내용 및 산출물 |
|---|---|
| 1. 토큰화 및 정제 | 텍스트 입력 문서를 어절·형태소 단위로 분할하고 특수문자 제거 및 표제어 추출(Lemmatization) |
| 2. 문서-단어 빈도 행렬 구축 | 문서 $d$별 단어 $t$의 단순 출현 횟수 카운트 및 문서 길이 정규화 TF 산출 |
| 3. 말뭉치 전역 DF 및 IDF 산출 | 전체 문서 수 $N$에 대해 단어 $t$가 등장한 문서 수 $DF(t)$ 집계 후 로그 역수 계산 |
| 4. TF-IDF 가중치 행렬 계산 | 각 셀의 원소에 대해 $TF \times IDF$ 연산 수행 후 L2 정규화를 통해 단위 벡터 변환 |
| 5. 유사도 계산 및 인덱싱 | 질의어(Query) 벡터와 문서 벡터 간의 코사인 유사도(Cosine Similarity) 측정 후 랭킹 산출 |

## Ⅳ. 텍스트 표현 및 검색 기법 비교

| 비교 항목 | TF-IDF | BM25 | Dense Embedding |
|---|---|---|---|
| 모델 성격 | 고전 통계 기반 BoW | 통계 기반 확률적 검색 랭킹 | 딥러닝 신경망 기반 밀집 표현 |
| 단어 빈도 포화 | 선형 증가 (TF 급증 시 왜곡) | $k_1$ 파라미터로 상한선 포화 | 어텐션 메커니즘 기반 문맥 반영 |
| 문서 길이 정규화 | L2 정규화 등 사후 처리 | $b$ 파라미터로 수식 내 직접 보정 | 청크 분할 및 고정 차원 축약 |
| 의미·문맥 반영 | 불가 (어휘 완전 일치 기반) | 불가 (어휘 빈도 및 길이 중심) | 가능 (동의어, 문맥, 의미론적 유사도) |
| 계산 복잡도 및 자원 | 극히 낮음 (CPU 단독 고속 처리) | 극히 낮음 (역색인 구조 최적화) | 높음 (GPU 기반 추론 및 벡터 DB) |
| 주 활용 분야 | 키워드 검색, 텍스트 기초 분류 | 대규모 검색 엔진(Elasticsearch) | LLM RAG, 시맨틱 검색, 질의응답 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 어휘 불일치(Vocabulary Mismatch) 및 동음이의어·다의어 구분 불가로 인한 검색 재현율(Recall) 저하 | 의미 기반 밀집 벡터(Dense Retrieval)와 어휘 기반 역색인(Sparse Retrieval)을 상호보완 결합하는 RRF(Reciprocal Rank Fusion) 하이브리드 검색 적용 |
| 긴 문서에서 특정 단어가 반복 등장할 경우 TF 가중치가 비정상적으로 과대 계상되는 왜곡 현상 | 단어 빈도의 무한 증가를 억제하는 포화 함수 및 문서 평균 길이를 반영하는 Okapi BM25 알고리즘으로 전환 |
| 전체 어휘 사전에 비례하여 차원이 폭증하고 99% 이상이 0으로 채워지는 고차원 희소성(Sparsity) | 역색인(Inverted Index) 전치 파일 압축 알고리즘(Elias-Fano, Roaring Bitmaps) 및 상위 유의미 키워드 필터링 적용 |

## Ⅵ. 제언

현대 생성형 AI 및 RAG 파이프라인에서 TF-IDF/BM25는 밀집 벡터 검색의 고유 명사 검색 누락을 보완하는 필수 하이브리드 축으로 재정립.

```text
[User Query] ---> [Sparse Search (TF-IDF/BM25)] --(Top-K)--> [RRF Fusion] ---> [Cross-Encoder]
             ---> [Dense Search (Vector DB)]    --(Top-K)--/    (랭킹 결합)      (정밀 재순위화)
```

| 최적화 관점 | 엔지니어링 실행 방안 | 기대 효과 |
|---|---|---|
| 검색 정확도 | BM25 + Dense Embedding 가중치 배분 하이브리드 파이프라인 구축 | 단어 완전 일치와 문맥 의미 탐색 동시 만족 |
| 인프라 효율성 | 형태소 분석기 튜닝 및 불용어 사전의 도메인 특화 동적 업데이트 | 불필요한 차원 낭비 제거 및 인덱싱 처리 지연 단축 |

## 출제 이력과 검증 출처

- 제132회 정보관리기술사 2교시 3번: 주어진 문서 집합에 대한 TF-IDF 계산 과정, IDF 수식 정의, 행렬 도출 및 검색 적용 한계.
- Salton, G., Buckley, C., Term-weighting approaches in automatic text retrieval, Information Processing & Management.
- Robertson, S., Zaragoza, H., The Probabilistic Relevance Framework: BM25 and Beyond, Foundations and Trends in Information Retrieval.

## 연결 토픽

- 검색 증강 생성: [모듈러 RAG(Modular RAG)](./059_modular_rag.md)
- 검색 고도화: [하이브리드 검색(Hybrid Search)](./068_hybrid_search.md)
- 의미 벡터화 기법: [임베딩(Embedding)](./085_embedding.md)
