---
title: "텍스트 마이닝"
author: "agnusdei1207"
date: "2026-10-25T00:09:02+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 텍스트 마이닝(Text Mining), 자연어 처리(NLP, Natural Language Processing), 정보 검색(IR, Information Retrieval), 형태소 분석, 토큰화(Tokenization)
- TF-IDF(Term Frequency-Inverse Document Frequency), Word2Vec, BERT(Bidirectional Encoder Representations from Transformers), LDA(Latent Dirichlet Allocation), 개체명 인식(NER, Named Entity Recognition), LLM(Large Language Model), RAG(Retrieval-Augmented Generation)

## Ⅰ. 텍스트 마이닝의 개요

- 핵심 요약 : 비정형 텍스트에서 NLP·IR·통계·머신러닝 기법으로 의미 있는 패턴과 관계를 찾아내는 기술.
- 개념 : 자연어로 작성된 대규모 비정형 텍스트에 자연어 처리(NLP), 정보 검색(IR), 통계 및 머신러닝 기법을 적용해 패턴, 관계, 트렌드 같은 가치 있는 정보를 발굴하는 기술 (**텍스트 마이닝** (Text Mining)).
- 배경 및 필요성 : 뉴스, 리뷰, SNS 등 비정형 텍스트가 크게 늘었으나, 단순 키워드 검색으로는 문맥, 감정, 개체 간 관계를 파악하기 어려움.
- 주요 목적 : 텍스트를 정량적 구조 데이터로 바꿔 감성 분석, 토픽 모델링, 문서 분류 같은 분석을 자동화하고 인사이트를 도출.

## Ⅱ. 텍스트 마이닝의 특징

- 핵심 요약 : 비구조성·모호성·고차원 희소성이라는 난제를, 여러 기술을 단계적으로 결합해 해결하는 분석 체계.

1. 비구조성과 모호성 : 다의어, 동음이의어, 신조어, 문맥 의존성 때문에 같은 단어도 의미가 달라짐 → 문맥을 읽는 모델이 필요.
2. **고차원 희소성** (Sparsity) : 수만 개 어휘로 차원이 커져 대부분의 값이 0인 행렬이 생김 → 차원 축소나 밀집 표현이 필요.
3. 융합 기술 체계 : NLP, IR, 통계, 머신러닝을 결합 → 한 기법으로는 얻기 어려운 정확도 확보.
4. 정량적 변환 : 감정과 개체 관계를 구조화 데이터로 바꿔 집계·비교가 가능해짐.
5. 기술의 단계적 발전 : 규칙·사전 기반에서 **TF-IDF** (Term Frequency-Inverse Document Frequency)와 LDA(Latent Dirichlet Allocation) 같은 통계 기법을 거쳐, Word2Vec과 **BERT** (Bidirectional Encoder Representations from Transformers) 같은 임베딩 기법, 그리고 **LLM** (Large Language Model)과 **RAG** (Retrieval-Augmented Generation)로 발전함.

## Ⅲ. 텍스트 마이닝의 구조 (흐름)

- 핵심 요약 : 원천 텍스트를 전처리하고, 특성을 추출한 뒤 마이닝 모델을 적용하는 네 단계 파이프라인.

```text
[ 텍스트 마이닝 파이프라인 ]
원천 텍스트 (뉴스, 리뷰, SNS)
      ↓
전처리
  토큰화, 형태소 분석, 불용어 제거
      ↓
특성 추출 (임베딩)
  TF-IDF, Word2Vec, BERT
      ↓
마이닝 모델링
  감성 분석, 토픽 모델링, 개체명 인식
```

- 검색 기반 활용 흐름은 다음과 같다. 사내 규정이나 계약서 같은 문서를 잘게 나눠(청킹, Chunking) 벡터 데이터베이스에 색인해 두고, 질문이 들어오면 유사한 조각을 찾아 LLM 프롬프트에 넣는다. 이렇게 하면 근거 없는 답변인 환각(Hallucination)을 억제할 수 있다.

```text
[ RAG 질의응답 흐름 ]
사용자 질문
      ↓
유사 문서 조각 검색 (벡터 색인)
      ↓
질문 + 검색 결과를 LLM에 입력
      ↓
근거 기반 답변 생성
```

## Ⅳ. 텍스트 마이닝 핵심 기술 요소의 비교

- 핵심 요약 : 형태소 분석에서 문맥 기반 임베딩, 마이닝 태스크에 이르기까지 단계별 메커니즘과 산출물이 다름.

| 단계 | 핵심 기술 | 메커니즘 | 주요 산출물 |
| --- | --- | --- | --- |
| 형태소 분석·토큰화 | KoNLPy(Mecab, Okt), SentencePiece | 어절을 형태소·서브워드로 나누고 품사(POS, Part of Speech)를 태깅 | 불용어를 뺀 핵심 명사·동사 토큰 |
| 통계 기반 표현 | BoW(Bag of Words), TF-IDF | 단어 빈도와 역문서 빈도를 곱해 단어 가중치를 부여 | 희소 행렬, 문서 간 유사도 계산 |
| 분산 표상 | Word2Vec, FastText | CBOW(Continuous Bag of Words)나 Skip-Gram으로 주변 문맥을 예측하며 저차원 밀집 벡터 학습 | 의미 유사도 (King - Man + Woman ≈ Queen) |
| 문맥 기반 임베딩 | BERT, RoBERTa | 양방향 트랜스포머 인코더의 자기 주의(Self-Attention)로 문맥에 따라 달라지는 벡터 생성 | 동적 문맥 임베딩 |
| 토픽 모델링 | LDA | 디리클레 분포를 가정한 확률적 생성 모델로 잠재 토픽 도출 | 문서별 토픽 비율, 토픽별 핵심 키워드 |
| 정보 추출 | **개체명 인식** (NER, Named Entity Recognition) | 인명, 기관명, 지명, 날짜 같은 고유명사 태깅 | 지식 그래프의 노드와 관계 데이터 |

## Ⅴ. 텍스트 마이닝의 장점과 한계

- 핵심 요약 : 비정형 데이터의 가치 발굴과 문서 지능화라는 장점과 달리, 다의성 처리, 연산 자원, 환각과 보안에서 한계를 가짐.

장점은 세 가지다.
1. 정형 분석으로는 접근할 수 없는 비정형 텍스트에서 가치를 찾아냄.
2. 감정, 트렌드, 개체 관계를 정량화해 의사결정 자료를 제공함.
3. LLM과 RAG를 결합해 문서 질의응답과 요약을 자동화함.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 다의성과 도메인 은어 처리 | 동음이의어, 풍자, 전문 약어를 BoW·TF-IDF 방식은 문맥으로 구분하지 못해 분석 오류가 생김 | 사전학습 언어모델(BERT, RoBERTa) 사용, 도메인 어휘집 구축, 도메인 적응(Domain Adaptation) 미세조정 | 개체 인식 정확도, 오분류율 |
| 연산 자원과 서빙 지연 | 대규모 말뭉치의 임베딩과 유사도 검색에 GPU(Graphics Processing Unit) 메모리가 많이 쓰이고 응답 지연이 커짐 | 양자화(Quantization)와 지식 증류(Knowledge Distillation), 벡터 데이터베이스(DB, Database)의 근사 최근접 이웃(ANN, Approximate Nearest Neighbor) 색인 | 99백분위(P99) 지연, GPU 사용률 |
| 환각과 보안 유출 | LLM이 사실이 아닌 내용을 그럴듯하게 생성하고, 프롬프트 인젝션으로 기밀이 노출될 수 있음 | RAG 기반 근거 검증(Fact-checking), 지식 그래프 연계, 개인정보 가명 처리 필터 적용 | 근거 인용률, 민감정보 탐지 건수 |

## Ⅵ. 텍스트 마이닝에 대한 기술사적 제언

- 핵심 요약 : 분석 품질을 지키려면 도메인 어휘집을 지속해서 갱신하고, 편향과 유해 표현을 걸러내는 정제 단계를 파이프라인 안에 두어야 함.
- 금융, 의료, 제조처럼 전문 용어가 많은 분야에서는 형태소 분석기의 사용자 사전을 현업과 함께 정기적으로 갱신해야 한다. 사전을 방치하면 새 약어와 제품명이 오인식되어 이후 모든 분석 결과가 함께 흔들린다.
- 웹에서 수집한 텍스트에는 혐오 표현과 개인정보가 섞여 있으므로, 개인정보(PII, Personally Identifiable Information)의 비식별화와 유해 표현 정제를 수집 직후 단계에 강제로 넣는 것이 바람직하다. 이 단계를 생략한 데이터는 어떤 분석 모델을 쓰더라도 그대로 위험을 옮긴다.

## Ⅶ. 결론

- 핵심 요약 : 텍스트 마이닝은 비정형 텍스트를 구조화해 지능화하는 핵심 기술이며, 언어의 모호성과 자원·신뢰성 관리가 함께 따라야 함.
- 시사점 : 사전 정제와 근거 검증을 갖춘 파이프라인이 있어야 분석 결과의 정확성과 효율을 함께 확보할 수 있음.
