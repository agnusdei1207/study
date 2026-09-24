---
title: "텍스트 마이닝 (Text Mining)"
category: "03-data"
tags:
  - "텍스트마이닝"
  - "NLP"
  - "TF_IDF"
  - "임베딩"
  - "토픽모델링"
  - "감성분석"
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
sidebar:
  badge:
    text: "기초"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 분석에서 비정형 데이터 분석 및 텍스트 마이닝으로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>비정형 분석·자연어처리</span>
  <strong>텍스트 마이닝 (Text Mining)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 자연어로 작성된 대규모 비정형 텍스트 데이터로부터 자연어 처리(NLP), 정보 추출, 기계학습 기술을 결합하여 유의미한 패턴, 숨겨진 토픽, 감성, 개체 간의 관계를 발굴하는 데이터 엔지니어링 및 마이닝 기법
- 메커니즘: 비정형 코퍼스 수집 $\rightarrow$ 형태소 분석 및 전처리 $\rightarrow$ 텍스트 특징 벡터화(TF-IDF / 임베딩) $\rightarrow$ 고급 마이닝(분류·군집·LDA 토픽·감성분석) $\rightarrow$ 인사이트 시각화
- 산출물: 전처리된 토큰 코퍼스 · 단어-문서 행렬(DTM) / 밀집 임베딩 벡터 · 토픽 분포 모델(LDA) · 감성 지수 및 개체명(NER) 추출 결과서

<div class="itpe-flow-map" role="img" aria-label="텍스트 마이닝 처리 파이프라인 및 품질 판정 게이트">
  <div class="itpe-flow-node">
    <strong>1단계: 비정형 텍스트 수집 및 개인정보 비식별화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>수집</strong><span>고객 VOC, 뉴스, SNS, 상담 녹취록 수집 및 정규식 기반 주민번호/전화번호 마스킹</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 자연어 전처리(NLP) 및 형태소 분석</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>전처리</strong><span>토큰화(Tokenization), 표제어 추출(Lemmatization), 불용어(Stopwords) 제거, 품사 태깅(PoS)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 수치적 벡터 표현 (Feature Representation)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>희소 벡터</strong><span>단어 빈도-역문서 빈도(TF-IDF) 가중치 매트릭스(DTM)</span></div>
      <div class="itpe-flow-branch"><strong>밀집 벡터</strong><span>Word2Vec, FastText, 사전학습 언어모델(BERT) 문맥 임베딩</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 데이터 무결성 및 도메인 정합성 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>개인정보(PII) 누출이 완벽히 차단되었으며, 도메인 전문 용어 오탈자/신조어가 사전에 등록되었는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (마이닝 모델링 수행)</strong>
      <span>정제 코퍼스 확정 $\rightarrow$ 문서 분류(F1), 토픽 모델링(LDA), 감성분석 및 서비스 연동</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (PII 유출 / 문맥 왜곡)</strong>
      <span>모델링 중단 $\rightarrow$ 비식별화 파이프라인 재실행 및 도메인 사용자 정의 사전(User Dict) 보완</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `TF-IDF(Term Frequency-Inverse Document Frequency)`: 특정 문서 내 단어 빈도(TF)와 전체 문서군 내 희소성(IDF)을 곱하여 단어의 고유 중요도를 산출하는 기법
- `Word Embedding`: 단어를 고차원 희소 벡터가 아닌 저차원의 연속적인 실수 벡터 공간에 매핑하여 단어 간의 의미적 유사도를 보존하는 기법 (Word2Vec 등)
- `LDA(Latent Dirichlet Allocation)`: 문서가 잠재된 여러 토픽의 혼합체로 구성되어 있다는 가정 하에 토픽별 단어 분포를 확률적으로 추론하는 토픽 모델링 기법
- `NER(Named Entity Recognition, 개체명 인식)`: 텍스트 내에서 인명, 지명, 기관명, 날짜 등 고유한 의미를 갖는 개체명을 식별하고 분류하는 작업
- `Sentiment Analysis(감성분석)`: 텍스트에 나타난 작성자의 의견, 감정, 태도(긍정, 부정, 중립)를 오피니언 마이닝을 통해 정량적으로 판정하는 기법

</details>

---

## 1교시 예상문제 (10점)

> 텍스트 마이닝 (Text Mining)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 텍스트 마이닝(Text Mining)의 정의 및 목적

- **정의**: 대규모 비정형 자연어 텍스트에서 형태소 분석, 수치 벡터화, 머신러닝 기법을 결합하여 의미 있는 패턴, 주제, 감성을 발굴하는 데이터 마이닝 기술
- **목적**: 비정형 데이터의 지식화, 고객 VOC 자동 분류, 소셜 여론 트렌드 분석

### 2. TF-IDF vs Word Embedding 비교

| 비교 항목 | TF-IDF | Word Embedding |
|---|---|---|
| **표현 형태** | 고차원 희소 벡터 (단어-문서 행렬 DTM) | 저차원 밀집 벡터 (100~768차원 연속 공간) |
| **핵심 원리** | 단어 빈도(TF) $\times$ 역문서 빈도(IDF) | 신경망 기반 문맥 학습 (Word2Vec, BERT) |
| **의미 보존** | 단어 간 유사도 미반영 (독립 직교) | 코사인 거리 기반 의미적 유사도 완벽 보존 |
| **적용 영역** | 키워드 검색, 법률 색인 | 감성 분석, 챗봇, 최신 LLM RAG 검색 |

### 3. 기술사적 실무 제언: 한국어 특수성 극복과 RAG 연계

- 한국어 교착어(어근+조사) 특성을 극복하기 위해 도메인 사용자 정의 사전을 필수 주입하고, TF-IDF의 키워드 색인과 임베딩의 의미 검색을 결합한 하이브리드 RAG 검색 아키텍처를 구축해야 함.
---

## 2~4교시 예상문제 (25점)

> 기업의 비정형 데이터 분석 및 인공지능(AI) 고도화를 위한 텍스트 마이닝(Text Mining)의 개념, 단계별 분석 절차, 특징 표현 기법(TF-IDF vs Word Embedding)을 비교하고, 한국어 텍스트 처리의 특수성 및 실무 도입 시 한계 극복 방안을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **TF-IDF 특징 추출** | 문서 내 단어 빈도(TF)와 역문서 빈도(IDF)의 곱, 희소 행렬 표현의 한계 | Ⅲ 표현 기법 |
| **토픽 모델링 (LDA)** | 디리클레 분포 기반 잠재 토픽 추론, 코히어런스(Coherence) 평가 | Ⅳ 마이닝 기법 |
| **한국어 형태소 분석 특수성** | 교착어 특성(어근+조사), 띄어쓰기 오류, 사용자 정의 사전의 중요성 | Ⅴ·Ⅵ |

### Ⅰ. 비정형 언어 데이터를 비즈니스 통찰로 바꾸는 텍스트 마이닝 개요

> 텍스트 마이닝은 자연어 문장에 내재된 의미와 감성을 기계가 이해할 수 있는 수치 벡터로 변환하여 패턴을 발견하는 과정임.

- 정의: 데이터베이스에 정형화되지 않은 텍스트 문서군으로부터 자연어 처리(NLP), 텍스트 분석, 패턴 인식을 결합하여 의미 있는 인사이트와 새로운 지식을 추출하는 분석 기법
- 필요성: 기업 내 데이터의 80% 이상을 차지하는 비정형 문서(고객 상담 내역, 계약서, 리뷰, SNS)의 분석을 통한 고객 경험 혁신 및 리스크 조기 감지
- 데이터 마이닝과의 차이: 전통적 데이터 마이닝이 정형 관계형 테이블을 분석 대상으로 삼는 반면, 텍스트 마이닝은 문맥, 다의어, 문법 구조가 얽힌 비정형 텍스트를 전처리 및 벡터화하여 분석함

### Ⅱ. 텍스트 마이닝 표준 5단계 분석 절차

> 수집에서 전처리, 특징 추출, 모델링, 평가 및 서빙으로 이어지는 파이프라인을 구축함.

<svg viewBox="0 0 520 150" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="텍스트 마이닝 5단계 표준 파이프라인" role="img">
  <defs>
    <marker id="nlp-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <!-- 5 Nodes in sequence -->
  <g transform="translate(10, 20)">
    <!-- Step 1 -->
    <rect width="90" height="75" rx="5" fill="#21262d" stroke="#30363d"/>
    <text x="45" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#c9d1d9" text-anchor="middle">1. 수집·정제</text>
    <text x="45" y="42" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e" text-anchor="middle">크롤링/API</text>
    <text x="45" y="58" font-family="system-ui, sans-serif" font-size="8" fill="#f85149" text-anchor="middle">PII 비식별화</text>
    <path d="M 92 48 L 100 48" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#nlp-arrow)"/>

    <!-- Step 2 -->
    <g transform="translate(102, 0)">
      <rect width="90" height="75" rx="5" fill="#21262d" stroke="#58a6ff"/>
      <text x="45" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#58a6ff" text-anchor="middle">2. 형태소 분석</text>
      <text x="45" y="42" font-family="system-ui, sans-serif" font-size="8" fill="#c9d1d9" text-anchor="middle">토큰화/불용어</text>
      <text x="45" y="58" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e" text-anchor="middle">PoS 품사태깅</text>
    </g>
    <path d="M 194 48 L 202 48" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#nlp-arrow)"/>

    <!-- Step 3 -->
    <g transform="translate(204, 0)">
      <rect width="90" height="75" rx="5" fill="#21262d" stroke="#3fb950"/>
      <text x="45" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#3fb950" text-anchor="middle">3. 벡터화</text>
      <text x="45" y="42" font-family="system-ui, sans-serif" font-size="8" fill="#c9d1d9" text-anchor="middle">TF-IDF 희소</text>
      <text x="45" y="58" font-family="system-ui, sans-serif" font-size="8" fill="#3fb950" text-anchor="middle">임베딩 밀집</text>
    </g>
    <path d="M 296 48 L 304 48" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#nlp-arrow)"/>

    <!-- Step 4 -->
    <g transform="translate(306, 0)">
      <rect width="90" height="75" rx="5" fill="#21262d" stroke="#d29922"/>
      <text x="45" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#d29922" text-anchor="middle">4. 모델링</text>
      <text x="45" y="42" font-family="system-ui, sans-serif" font-size="8" fill="#c9d1d9" text-anchor="middle">LDA 토픽/분류</text>
      <text x="45" y="58" font-family="system-ui, sans-serif" font-size="8" fill="#d29922" text-anchor="middle">감성/NER추출</text>
    </g>
    <path d="M 398 48 L 406 48" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#nlp-arrow)"/>

    <!-- Step 5 -->
    <g transform="translate(408, 0)">
      <rect width="90" height="75" rx="5" fill="#21262d" stroke="#a371f7"/>
      <text x="45" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#a371f7" text-anchor="middle">5. 평가·활용</text>
      <text x="45" y="42" font-family="system-ui, sans-serif" font-size="8" fill="#c9d1d9" text-anchor="middle">F1 / Coherence</text>
      <text x="45" y="58" font-family="system-ui, sans-serif" font-size="8" fill="#a371f7" text-anchor="middle">VOC 대시보드</text>
    </g>
  </g>

  <!-- Bottom Bar -->
  <g transform="translate(10, 105)">
    <rect width="498" height="32" rx="4" fill="rgba(56,189,248,0.08)" stroke="rgba(56,189,248,0.3)"/>
    <text x="249" y="20" font-family="system-ui, sans-serif" font-size="9" fill="#58a6ff" text-anchor="middle">핵심 원칙: 철저한 PII 비식별화 선행 $\to$ 도메인 사용자 정의 사전 주입 $\to$ F1/Coherence 검증</text>
  </g>
</svg>

1. **텍스트 수집 및 정제**: 웹 크롤링, 로그 수집기 연동, HTML 태그 및 특수문자 제거, 개인정보(PII) 마스킹
2. **형태소 분석 및 토큰화**: 단어를 최소 의미 단위로 분할, 명사/동사 등 유효 품사 추출, 조사 및 불용어(Stopwords) 필터링
3. **특징 벡터화(Feature Representation)**: 텍스트를 머신러닝 모델이 연산 가능한 수치 행렬(DTM, 임베딩)로 변환
4. **마이닝 모델링**: 비지도학습(토픽 모델링, 군집) 또는 지도학습(문서 분류, 감성 분석) 알고리즘 학습
5. **평가 및 활용**: 분류 정확도(F1-score), 토픽 일관성(Coherence) 평가 후 전사 VOC 대시보드 및 검색 엔진 연계

### Ⅲ. 텍스트 특징 표현 기법: TF-IDF vs Word Embedding 비교

> 전통적인 단어 빈도 기반 방식과 딥러닝 기반 밀집 임베딩 방식의 장단점을 절충하여 선택함.

<svg viewBox="0 0 520 160" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="TF-IDF 희소 행렬과 Word Embedding 밀집 벡터 구조 비교" role="img">
  <!-- Left: TF-IDF -->
  <g transform="translate(15, 15)">
    <rect width="235" height="130" rx="5" fill="#21262d" stroke="#f0883e" stroke-width="1"/>
    <text x="117" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#f0883e" text-anchor="middle">TF-IDF (고차원 희소 벡터)</text>
    <rect x="15" y="32" width="205" height="26" rx="4" fill="#161b22" stroke="#30363d"/>
    <text x="117" y="49" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9" text-anchor="middle">수식: TF(단어빈도) × IDF(역문서빈도)</text>
    <text x="15" y="74" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 차원: 전체 어휘 사전 크기 (수만 차원)</text>
    <text x="15" y="90" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 행렬: 대부분 값이 0인 Sparse Matrix</text>
    <rect x="15" y="100" width="205" height="20" rx="3" fill="rgba(240,136,62,0.12)"/>
    <text x="117" y="114" font-family="system-ui, sans-serif" font-size="8" font-weight="bold" fill="#f0883e" text-anchor="middle">문맥/유사도 미반영, 키워드 검색에 최적</text>
  </g>

  <!-- Right: Word Embedding -->
  <g transform="translate(270, 15)">
    <rect width="235" height="130" rx="5" fill="#21262d" stroke="#3fb950" stroke-width="1"/>
    <text x="117" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#3fb950" text-anchor="middle">Word Embedding (저차원 밀집 벡터)</text>
    <rect x="15" y="32" width="205" height="26" rx="4" fill="#161b22" stroke="#30363d"/>
    <text x="117" y="49" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9" text-anchor="middle">모델: Word2Vec, FastText, BERT</text>
    <text x="15" y="74" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 차원: 저차원 실수 벡터 (100~768차원)</text>
    <text x="15" y="90" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 특성: 코사인 유사도 및 의미적 연산 보존</text>
    <rect x="15" y="100" width="205" height="20" rx="3" fill="rgba(63,185,80,0.12)"/>
    <text x="117" y="114" font-family="system-ui, sans-serif" font-size="8" font-weight="bold" fill="#3fb950" text-anchor="middle">문맥 완벽 반영, 감성분석/LLM RAG 최적</text>
  </g>
</svg>

| 비교 항목 | TF-IDF (Term Frequency-IDF) | Word Embedding (Word2Vec, BERT) |
|---|---|---|
| **표현 방식** | 고차원 희소 벡터 (Sparse Vector) | 저차원 밀집 벡터 (Dense Vector, 통상 100~768차원) |
| **차원의 크기** | 전체 어휘 사전 크기 (수만~수십만 차원) | 고정된 작은 차원 크기 |
| **문맥 및 의미 보존** | 단어 간 의미적 유사도 미반영 (직교성) | 단어 간 유사도(코사인 거리) 및 유추(King-Man+Woman=Queen) 보존 |
| **단어 순서 반영** | Bag-of-Words 기반으로 어순 완전 손실 | 트랜스포머/RNN 연계 시 문맥과 어순 완벽 반영 |
| **계산 비용 및 설명력**| 계산이 매우 가볍고 직관적 해석 가능 | 학습 비용 및 GPU 자원 요구, 벡터 자체의 해석 난해 |
| **적합 분석 도메인** | 전통 키워드 검색, 대규모 문서 검색, 법률 문서 색인 | 감성 분석, 챗봇, 기계 번역, 최신 LLM RAG 검색 |

### Ⅳ. 텍스트 마이닝 4대 핵심 분석 기법

> 분석 목적에 따라 지도학습과 비지도학습 알고리즘을 적절히 결합함.

| 마이닝 기법 | 핵심 분석 목적 | 대표 알고리즘 | 실무 적용 사례 |
|---|---|---|---|
| **문서 분류 (Classification)** | 문서를 사전에 정의된 카테고리로 자동 분류 | Naive Bayes, SVM, LightGBM, BERT | 고객 인바운드 문의 자동 부서 배정, 스팸 메일 필터링 |
| **토픽 모델링 (Topic Modeling)**| 문서군에 내재된 잠재 주제를 확률적으로 추출 | **LDA (Latent Dirichlet Allocation)**, BERTopic | 분기별 고객 불만 핵심 이슈 도출, 학술 논문 트렌드 분석 |
| **감성 분석 (Sentiment)** | 문장에 나타난 소비자의 긍정/부정/중립 태도 판정 | 감성 사전 기반 점수화, LSTM, RoBERTa | 신제품 출시 후 소셜 여론 모니터링, 상품 리뷰 평점 예측 |
| **정보 추출 (Information Extraction)**| 비정형 문장에서 핵심 개체명 및 관계 추출 | **NER (Named Entity Recognition)**, 의존 구문 분석 | 금융 공시 문서에서 매출액/기업명 자동 추출, 계약서 검토 |

### Ⅴ. 한국어 텍스트 처리의 특수성과 형태소 분석 난제

> 영어와 다른 한국어 고유의 언어적 특성을 고려한 전처리 파이프라인 설계가 필수적임.

1. **교착어(Agglutinative Language) 특성**:
   - 어간에 조사, 어미, 접사가 결합하여 단어를 형성하므로 단순 띄어쓰기(Whitespace) 기반 분할 시 단어 수가 무한히 팽창함
   - 대책: KoNLPy(Mecab, Okt) 등 고성능 한국어 형태소 분석기를 통해 어근과 조사를 철저히 분리
2. **자유로운 띄어쓰기와 신조어·줄임말**:
   - 띄어쓰기 오류가 만연하며, 고객 상담 데이터에는 '환불점여', '안드감' 등 맞춤법 파괴 표현 다수 존재
   - 대책: 도메인 특화 '사용자 정의 사전(User Dictionary)'을 형태소 분석기에 주입하고 맞춤법 교정기(PyKoSpacing) 선행 연동

### Ⅵ. 텍스트 마이닝 실무 위험 관리 및 통제 방안

> 언어 데이터 특유의 프라이버시 침해와 도메인 편향을 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 비정형 텍스트 내 개인정보(PII) 유출 | 정규식 기반 패턴 매칭 및 개체명 인식(NER) 기반 자동 마스킹 파이프라인 | 개인정보보호법 컴플라이언스 준수 및 데이터 유출 원천 차단 |
| 도메인 전문 용어 오인식 및 형태소 쪼개짐 | 도메인 사용자 정의 사전(User Dictionary) 사전 구축 및 주기적 현행화 | '내시경적역행성담췌관조영술' 등 전문 복합 명사 보존 |
| 데이터 누수(Data Leakage)로 인한 모델 과적합 | 시간축(Time-based) 기준 Train/Validation/Test 셋 엄격 분할 | 실시간 운영 환경에서의 일반화 분류 성능 확보 |
| 블랙박스 딥러닝 임베딩의 설명 불가능성 | LIME, SHAP, 어텐션 맵(Attention Map) 기반 중요 단어 기여도 시각화 | 판정 근거 제시로 현업 실무자의 결과 수용성 극대화 |

### Ⅶ. 기술사적 제언: LLM 시대 텍스트 마이닝의 진화와 RAG 결합

> "전통 텍스트 마이닝의 통계적 지표와 거대언어모델(LLM)의 생성 능력이 결합할 때, 진정한 엔터프라이즈 인텔리전스가 완성된다."

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 모델의 파라미터 크기보다 말뭉치 정의·라벨링 기준·전처리 재현성이 텍스트 분석 품질의 성패를 결정한다. 최신 생성형 AI 도입에 앞서 신뢰할 수 있는 텍스트 정제 파이프라인 구축이 선행되어야 한다.
>
> **[나라면 이렇게 쓴다]**
> 전통적인 텍스트 마이닝(TF-IDF, LDA)으로 사내 지식 문서를 고속 색인 및 클러스터링하고, LLM 기반 RAG(검색 증강 생성) 아키텍처와 결합하여 환각 현상을 억제하는 고정밀 엔터프라이즈 검색 시스템을 구축하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 텍스트 마이닝의 성패는 고난도 딥러닝 모델의 복잡성이 아니라 **도메인 말뭉치 전처리의 정밀도**와 **비즈니스 실행 가능성(Actionability)**으로 판정
- **대응 방안**: 한국어 교착어 특화 형태소 전처리 $\rightarrow$ TF-IDF/임베딩 하이브리드 특징 추출 $\rightarrow$ LDA 토픽 모델링 $\rightarrow$ RAG 벡터 DB 색인 연계
- **검증 체계**: 토픽 일관성 점수(Coherence Score $\ge 0.6$) 및 문서 분류 F1-Score 90% 이상 확보
- **기대 효과**: 수작업 모니터링 비용 80% 절감 및 실시간 고객 VOC 이상 징후 조기 감지 체계 확립

<div class="itpe-flow-map" role="img" aria-label="텍스트 마이닝 고도화 실행 로드맵">
  <div class="itpe-flow-node">
    <strong>1단계: 현행 한계 인식</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-fail"><strong>문제</strong><span>수작업 VOC 분석 지연 및 한국어 신조어·전문용어 형태소 오분절 발생</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 아키텍처 개선 방안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>기술 적용</strong><span>도메인 사용자 사전 주입 + 형태소 전처리 자동화 + RAG 벡터 DB 결합</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 정량 검증 기준</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>KPI 지표</strong><span>문서 분류 F1-Score 90% 이상, 토픽 Coherence 0.6 이상 달성</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 궁극적 실행 효과</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>가치 창출</strong><span>고객 VOC 리드타임 80% 단축 및 이상 징후 선제적 대응 체계 완성</span></div>
    </div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **공식 출제 이력**: 정보관리기술사 제131회 1교시 단답형 (TF-IDF와 단어 임베딩), 제124회 2교시 논술형 (텍스트 마이닝 절차와 토픽 모델링)
- **표준 및 레퍼런스**: [NIST Natural Language Processing Guide](https://www.nist.gov/), Christopher D. Manning, Foundations of Statistical Natural Language Processing

## 연결 토픽

- [중심극한정리](./014_central_limit_theorem.md) · [데이터 시각화](./016_data_visualization.md) · [오피니언 마이닝](./090_opinion_mining.md) · [데이터 마이닝](./043_data_mining.md)
