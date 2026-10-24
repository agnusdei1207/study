---
title: "BERT(Bidirectional Encoder Representations from Transformers)"
author: "agnusdei1207"
date: "2026-10-24T23:23:43+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- BERT(Bidirectional Encoder Representations from Transformers), 트랜스포머(Transformer), 양방향 인코더(Bidirectional Encoder)
- 마스크 언어 모델(MLM, Masked Language Model), 다음 문장 예측(NSP, Next Sentence Prediction), 미세조정(Fine-Tuning)
- WordPiece, 3중 임베딩(Triple Embedding), RoBERTa, ELECTRA
- Longformer, BigBird, 트렁케이션(Truncation), 검색 리랭커(Reranker)

## Ⅰ. BERT(Bidirectional Encoder Representations from Transformers)의 개요

- 핵심 요약 : 트랜스포머 인코더를 쌍방향 문맥으로 사전학습하여 문장 이해와 분류에 특화된 언어 모델.
- 개념 : **트랜스포머** (Transformer)의 인코더 블록을 쌓아, 입력 문장의 좌우 **양방향 문맥**을 동시에 참조하도록 사전학습한 언어 이해(NLU, Natural Language Understanding) 특화 모델 **BERT**.
- 배경 및 필요성 : 기존 단방향 언어 모델은 앞 문맥만 보고 판단하여 문장 중간의 의미를 놓치기 쉬웠다. 한편 BERT는 자기회귀 생성에는 맞지 않아 문서 이해와 검색 리랭킹 같은 이해 중심 업무에 배치하는 것이 일반적이다.
- 주요 목적 : 단방향 문맥의 한계를 넘어 범용 언어 표현을 학습하고, 분류, 개체명 인식, 검색 등 다운스트림 과업의 성능을 높이는 것.

## Ⅱ. BERT(Bidirectional Encoder Representations from Transformers)의 특징 및 장점

- 핵심 요약 : 양방향 인코딩과 두 가지 사전학습 과제가 범용 표현을 만들고, 적은 데이터로 미세조정하여 여러 과업에 재사용하는 구조.

1. **양방향 인코딩** (Deep Bidirectional, 모든 층에서 좌우 문맥을 동시에 참조하는 표현) : 단어의 의미를 앞뒤 문맥으로 함께 판단 → 동음이의어와 문맥 의존 표현 해석 향상.
2. **마스크 언어 모델** (MLM, Masked Language Model, 일부 토큰을 가리고 원래 단어를 맞히는 과제) : 문맥 단어 맞히기로 어휘 의미를 학습 → 비지도 데이터만으로 대규모 사전학습 가능.
3. **다음 문장 예측** (NSP, Next Sentence Prediction, 두 문장이 연속인지 판별하는 과제) : 문장 간 관계를 학습 → 질의응답과 문장쌍 분류에 유리.
4. **미세조정** (Fine-Tuning, 사전학습 모델에 과업별 출력 층을 붙여 소량 데이터로 재학습) : 과업마다 모델을 처음부터 만들지 않아도 높은 성능을 기대 → 개발 비용 절감.

## Ⅲ. BERT(Bidirectional Encoder Representations from Transformers)의 구조 (흐름)

- 핵심 요약 : 세 종류의 임베딩을 더한 토큰열이 양방향 인코더를 거쳐 MLM과 NSP 두 과제로 갈라지는 사전학습 구조.
- **3중 임베딩** (Triple Embedding, 토큰 임베딩, 문장 구분 임베딩, 위치 임베딩의 합) : 입력 표현에 단어, 문장 소속, 순서 정보를 함께 담는다.
- **두 과제의 분기** : 특수 토큰 출력은 NSP 분류에, 가려진 토큰 출력은 MLM 복원에 쓰인다.

```text
[ 입력 토큰열 ]
[CLS] 사과 [MASK] 맛있는 과일 [SEP]
        ↓
[ 3중 임베딩 합산 ]
  토큰 + 문장 구분 + 위치
        ↓
[ 다층 양방향 트랜스포머 인코더 ]
  모든 토큰이 서로를 참조
```

```text
[ 인코더 출력 ]
  [CLS] 출력 → 다음 문장 예측
               (연속 여부 이진 분류)
  [MASK] 출력 → 마스크 언어 모델
               (가려진 단어를 소프트맥스로 복원)
```

## Ⅳ. BERT(Bidirectional Encoder Representations from Transformers)의 비교

- 핵심 요약 : BERT는 이해 중심의 인코더 구조이고, GPT는 생성 중심의 디코더, T5는 두 구조를 합친 인코더-디코더 구조로 역할이 나뉜다.

| 비교 축 | BERT (인코더) | GPT (디코더) | T5 (인코더-디코더) |
| --- | --- | --- | --- |
| 기본 구조 | 양방향 인코더 | 단방향 자기회귀 디코더 | 인코더와 디코더 결합 |
| 어텐션 | 양쪽 문맥을 모두 참조 | 과거 토큰만 참조 | 인코더는 양방향, 디코더는 단방향 |
| 사전학습 과제 | 마스크 언어 모델 | 다음 토큰 예측 | 텍스트 변환형 빈칸 복원 |
| 주요 업무 | 텍스트 분류, 개체명 인식, 검색 | 대화, 글쓰기, 코드 생성 | 번역, 요약, 조건부 변환 |
| 자유 생성 | 어려움 (빈칸 채우기 중심) | 강함 | 조건부 생성에 강함 |

- 선택 기준 : 결과가 정해진 라벨이나 순위인지, 자유로운 문장 생성인지에 따라 구조를 고름.

## Ⅴ. BERT(Bidirectional Encoder Representations from Transformers)의 한계와 방안

- 핵심 요약 : 사전학습과 미세조정 간 마스크 불일치, 생성 능력 부재, 입력 길이 제한을 학습 방식 개선, 역할 분리, 긴 문서 구조로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 마스크 토큰 불일치 | 사전학습에만 있는 [MASK] 토큰이 미세조정 데이터에 없어 표현이 왜곡 | 가짜 토큰을 판별하는 **ELECTRA** 방식 채택, **RoBERTa**의 동적 마스킹 적용 | 과업별 미세조정 정확도 |
| 자유 형식 생성 불가 | 자기회귀 디코더가 없어 장문 생성 과업을 수행할 수 없음 | 생성 과업은 디코더 모델로 분리하고 BERT는 분류와 리랭킹 전담 | 과업별 모델 배치 적합도 |
| 입력 길이 제한 | 최대 512 토큰을 넘는 문서는 잘려 문맥이 끊기는 **트렁케이션** (Truncation) 발생 | 윈도우 기반 희소 어텐션을 쓰는 **Longformer**, **BigBird** 계열 모델 도입 | 잘림 발생 문서 비율 |

## Ⅵ. BERT(Bidirectional Encoder Representations from Transformers)에 대한 기술사적 제언

- 핵심 요약 : 이해 과업은 경량 인코더로 처리하고 생성 과업은 별도 모델로 분리하여 비용과 지연을 함께 줄이는 역할 설계.

1. 서비스 개발 팀은 의도 분류와 같이 정해진 라벨을 고르는 과업을 BERT 계열 인코더로 옮겨, 생성형 모델 호출에 따른 지연과 비용을 줄이는 것이 바람직하다.
2. 검색 조직은 검색 결과의 재정렬을 사내에서 운영하는 리랭커로 구성하고, 리랭커의 정답 데이터를 주기적으로 갱신하여 품질 저하를 막는다.
3. 운영 조직은 분류 결과를 소프트맥스의 확률값과 함께 기록하여, 확률이 낮은 응답은 사람의 검토로 넘기는 기준을 마련한다.

## Ⅶ. 결론

- 핵심 요약 : BERT는 양방향 문맥으로 사전학습한 이해 특화 인코더로, 분류와 검색 같은 과업에서 여전히 실용적인 기반 모델이다.
- 시사점 : 생성형 모델이 확산되어도 이해 과업은 경량 인코더로 분담하는 구성이 비용과 신뢰성 측면에서 합리적이다.
