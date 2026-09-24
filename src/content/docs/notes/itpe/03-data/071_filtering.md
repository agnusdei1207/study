---
sidebar:
  order: 71
  label: "071. 필터링 (Filtering)"
  badge:
    text: "기초"
    variant: note
title: "필터링 기법 (Filtering) 및 추천 시스템과 데이터 엔지니어링"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
category: "03-data"
weight: 71
extra:
  model: "GPT-6"
  keyword_grade: "기초"
  question_no: "071"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>빅데이터 분석·추천 시스템</span><strong>필터링 (Filtering)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 280" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="260" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="32" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">추천 시스템 필터링: 협업 &middot; 콘텐츠 기반 및 2-Stage 아키텍처</text>

  <!-- Top: 2 Main Paradigms -->
  <g transform="translate(30, 48)">
    <!-- CF Box -->
    <rect x="0" y="0" width="220" height="95" rx="5" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <rect x="0" y="0" width="220" height="24" rx="5" fill="#eff6ff"/>
    <text x="110" y="16" font-size="10" font-weight="bold" fill="#1e40af" text-anchor="middle">협업 필터링 (Collaborative Filtering)</text>
    <text x="15" y="42" font-size="8.5" fill="#334155">&bull; 유저 기반: 나와 유사한 타인의 소비 추천</text>
    <text x="15" y="58" font-size="8.5" fill="#334155">&bull; 아이템 기반: 자주 함께 구매된 상품 추천</text>
    <text x="15" y="74" font-size="8.5" fill="#334155">&bull; 잠재 요인 모델: 행렬 분해 (R &approx; P &middot; Qᵀ)</text>
    <text x="15" y="88" font-size="8" fill="#2563eb">우연한 발견(Serendipity) &middot; 콜드스타트 취약</text>

    <!-- CBF Box -->
    <rect x="240" y="0" width="220" height="95" rx="5" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <rect x="240" y="0" width="220" height="24" rx="5" fill="#ecfdf5"/>
    <text x="350" y="16" font-size="10" font-weight="bold" fill="#065f46" text-anchor="middle">콘텐츠 기반 필터링 (Content-based)</text>
    <text x="255" y="42" font-size="8.5" fill="#334155">&bull; 메타데이터 분석: 장르, 태그, 감독 등</text>
    <text x="255" y="58" font-size="8.5" fill="#334155">&bull; 텍스트/임베딩: TF-IDF, BERT 벡터 유사도</text>
    <text x="255" y="74" font-size="8.5" fill="#334155">&bull; 유저 프로파일과 코사인 유사도 매칭</text>
    <text x="255" y="88" font-size="8" fill="#059669">신규 아이템 추천 가능 &middot; 다양성 부족 한계</text>
  </g>

  <!-- Bottom: 2-Stage Modern Pipeline -->
  <g transform="translate(30, 155)">
    <rect x="0" y="0" width="460" height="100" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
    <text x="15" y="18" font-size="10" font-weight="bold" fill="#0f172a">실무 엔터프라이즈 2-Stage 추천 파이프라인</text>

    <!-- Stage 1: Retrieval -->
    <rect x="15" y="30" width="130" height="58" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="80" y="47" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1. 후보군 추출 (Retrieval)</text>
    <text x="80" y="63" font-size="8" fill="#334155" text-anchor="middle">수백만 개 &rarr; 수백 개 압축</text>
    <text x="80" y="77" font-size="7.5" fill="#64748b" text-anchor="middle">Two-Tower DNN / ANN 벡터</text>

    <!-- Arrow 1 -->
    <path d="M 150 59 L 165 59" stroke="#64748b" stroke-width="1.5"/>

    <!-- Stage 2: Ranking -->
    <rect x="170" y="30" width="135" height="58" rx="4" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="237" y="47" font-size="9" font-weight="bold" fill="#5b21b6" text-anchor="middle">2. 정밀 순위화 (Ranking)</text>
    <text x="237" y="63" font-size="8" fill="#334155" text-anchor="middle">수백 개 &rarr; Top-100 정렬</text>
    <text x="237" y="77" font-size="7.5" fill="#64748b" text-anchor="middle">DLRM / CTR 예측 심층 신경망</text>

    <!-- Arrow 2 -->
    <path d="M 310 59 L 325 59" stroke="#64748b" stroke-width="1.5"/>

    <!-- Stage 3: Re-ranking -->
    <rect x="330" y="30" width="115" height="58" rx="4" fill="#fef2f2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="387" y="47" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">3. 재순위화 &amp; 룰</text>
    <text x="387" y="63" font-size="8" fill="#334155" text-anchor="middle">최종 Top-N 표출</text>
    <text x="387" y="77" font-size="7.5" fill="#64748b" text-anchor="middle">품절제거 / 다양성 보장</text>
  </g>
</svg>
</div>

- 본질: **수억 개의 방대한 데이터 및 아이템 속에서 사용자의 탐색 비용(Search Cost)과 정보 과부하(Information Overload)를 해소하기 위해, 사용자 간 행동 이력(협업)이나 아이템 고유 메타데이터(콘텐츠 기반)를 분석하여 사용자가 선호할 가능성이 높은 상위 유의미 데이터만을 선별·추출하는 알고리즘 체계**
- 암기: `유-아-잠` (협업 필터링: 사용자 기반, 아이템 기반, 잠재 요인 모델) / `콜-희-확-필` (추천 4대 난제: 콜드 스타트, 희소성, 확장성, 필터 버블)
- 판단축:
  - **협업 필터링(CF)**: 아이템 내용(속성)을 몰라도 행동 패턴만으로 취향 저격 가능하나, 데이터가 없는 신규 유저에게 무력함
  - **콘텐츠 기반 필터링(CBF)**: 신규 아이템에 대해 즉시 추천이 가능하여 콜드 스타트를 극복하나, 사용자의 새로운 잠재적 취향을 발견하기 어려움
- 주의: 대규모 실무 플랫폼에서는 단일 알고리즘만으로 수백만 개 아이템을 실시간 채점할 수 없으므로, 수백 개로 압축하는 **후보 추출(Filtering/Retrieval)**과 정밀 채점하는 **순위화(Ranking)**의 2단계 파이프라인으로 아키텍처를 분리해야 함

## Ⅰ. 정보 과부하를 해소하는 데이터 필터링(Filtering) 개요

#### 한줄 요약: 방대한 빅데이터에서 불필요한 노이즈를 제거하고 사용자 취향이나 시스템 조건에 부합하는 가치 있는 정보를 정제·추출하는 기술

- **필터링의 추진 배경**:
  - 데이터의 폭발적 증가로 사용자는 수많은 선택지 속에서 원하는 정보를 찾기 어려운 **'선택의 역설(Paradox of Choice)'**과 정보 과부하에 직면함
  - 기업은 사용자의 체류 시간과 전환율(CVR)을 극대화하기 위해 개인 맞춤형 필터링 추천 엔진을 핵심 비즈니스 경쟁력으로 도입함
- **데이터 필터링의 정의**:
  - 사용자-아이템 상호작용 로그(평점, 클릭, 구매) 또는 아이템 자체의 속성 벡터를 수학적으로 분석하여, 관심도가 높은 데이터만을 통과시키고 무관한 데이터를 걸러내는 정보 검색 및 머신러닝 기법

## Ⅱ. 추천 시스템의 3대 핵심 필터링 기법

#### 한줄 요약: 사용자 행동 기반의 협업 필터링, 아이템 속성 기반의 콘텐츠 필터링, 그리고 둘을 결합한 하이브리드 필터링

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 120" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="100" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">추천 필터링 기법 3대 분류 체계</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="145" height="55" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="72" y="18" font-size="9.5" font-weight="bold" fill="#1e40af" text-anchor="middle">협업 필터링 (CF)</text>
    <text x="72" y="34" font-size="8" fill="#334155" text-anchor="middle">User/Item-based 유사도</text>
    <text x="72" y="47" font-size="8" fill="#475569" text-anchor="middle">행렬 분해 (MF / ALS)</text>

    <rect x="160" y="0" width="145" height="55" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <text x="232" y="18" font-size="9.5" font-weight="bold" fill="#065f46" text-anchor="middle">콘텐츠 필터링 (CBF)</text>
    <text x="232" y="34" font-size="8" fill="#334155" text-anchor="middle">TF-IDF &middot; 메타 프로파일</text>
    <text x="232" y="47" font-size="8" fill="#475569" text-anchor="middle">BERT / LLM 임베딩</text>

    <rect x="320" y="0" width="145" height="55" rx="4" fill="#ffffff" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="392" y="18" font-size="9.5" font-weight="bold" fill="#5b21b6" text-anchor="middle">하이브리드 필터링</text>
    <text x="392" y="34" font-size="8" fill="#334155" text-anchor="middle">스위칭 (Switching)</text>
    <text x="392" y="47" font-size="8" fill="#475569" text-anchor="middle">가중합 &middot; 2-Stage 파이프라인</text>
  </g>
</svg>
</div>

### 1. 협업 필터링 (Collaborative Filtering, CF)
- **개념**: "많은 사용자로부터 얻은 선호도 정보를 바탕으로, 비슷한 취향을 가진 사람들은 미래에도 비슷한 선택을 할 것이다"라는 전제
- **메모리 기반 (Memory-based)**:
  - **사용자 기반 (User-based)**: 사용자 간의 코사인 유사도(Cosine)나 피어슨 상관계수를 계산하여, 유사한 이웃 유저들이 소비한 아이템 추천
  - **아이템 기반 (Item-based)**: 아이템 간의 공통 소비자 평점 벡터 유사도를 계산하여 추천 (아이템 간 관계가 더 안정적이어서 실무 선호)
- **모델 기반 (Model-based: 잠재 요인 모델)**:
  - 사용자-아이템 평점 행렬 $R_{m \times n}$을 저차원 잠재 공간(Latent Factor)으로 분해:
    $$R \approx P \times Q^T \quad (P: m \times k \text{ 유저 행렬}, Q: n \times k \text{ 아이템 행렬})$$
  - 비어있는 평점(결측치)을 최적화 알고리즘(ALS, 경사하강법)으로 예측하여 채워 넣음

### 2. 콘텐츠 기반 필터링 (Content-based Filtering, CBF)
- **개념**: 사용자가 과거에 선호했던 아이템의 **속성(텍스트 설명, 카테고리, 감독, 키워드 등)**을 분석하여, 유사한 메타데이터 속성을 지닌 다른 아이템을 탐색
- **동작 방식**: 아이템의 속성을 TF-IDF 또는 사전 학습된 LLM 임베딩 벡터로 변환하고, 사용자의 취향 벡터(User Profile)와의 코사인 유사도를 계산하여 상위 아이템 추천

### 3. 하이브리드 필터링 (Hybrid Filtering)
- 협업 필터링과 콘텐츠 기반 필터링을 결합하여 상호 단점을 보완:
  - **스위칭(Switching)**: 신규 가입자(콜드 스타트)는 콘텐츠 기반으로 추천하다가, 활동 로그가 $N$건 이상 누적되면 협업 필터링으로 자동 전환
  - **가중합(Weighted)**: 두 모델의 예측 점수를 가중합($Score = w_1 \cdot Score_{CF} + w_2 \cdot Score_{CBF}$)하여 최종 순위 산출

## Ⅲ. 협업 필터링 vs 콘텐츠 기반 필터링 심층 비교

#### 한줄 요약: 행동 데이터 기반의 우연한 발견(CF)과 메타데이터 기반의 설명 가능한 안정성(CBF) 간의 종합 비교

| 비교 항목 | 협업 필터링 (Collaborative Filtering) | 콘텐츠 기반 필터링 (Content-based) |
|:---|:---|:---|
| **기반 데이터** | 다수 사용자들의 **행동 이력 (평점, 클릭, 구매)** | 아이템의 **텍스트, 장르, 태그 등 메타데이터** |
| **도메인 독립성** | **완전 독립적** (상품의 기술적 내용을 몰라도 작동) | **도메인 종속적** (정교한 피처 엔지니어링 필요) |
| **신규 아이템 콜드스타트**| **치명적 취약** (아무도 안 본 신상품은 추천 불가) | **우수함** (메타데이터만 있으면 즉시 추천 가능) |
| **추천 다양성 / 발견성** | **탁월 (Serendipity)** (전혀 다른 장르의 취향 발견) | **제한적 (Over-specialization)** (보던 것만 추천) |
| **행렬 희소성 (Sparsity)**| 극도로 취약 (평점 데이터가 1% 미만일 때 저하) | 영향 없음 (아이템 자체 속성만으로 비교) |
| **대표 기술** | Matrix Factorization, ALS, BPR, Item2Vec | TF-IDF, Word2Vec, BERT 임베딩, 코사인 유사도 |

## Ⅳ. 추천 필터링의 4대 기술적 난제와 해결 전략

#### 한줄 요약: 콜드 스타트, 행렬 희소성, 실시간 확장성, 필터 버블을 극복하기 위한 엔지니어링 해법

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 135" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="115" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">추천 필터링 4대 난제 및 엔지니어링 대응 체계</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="110" height="70" rx="4" fill="#ffffff" stroke="#ef4444" stroke-width="1.2"/>
    <text x="55" y="18" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">1. 콜드 스타트</text>
    <text x="55" y="36" font-size="8" fill="#334155" text-anchor="middle">신규 유저 로그 전무</text>
    <text x="55" y="52" font-size="7.5" fill="#dc2626" text-anchor="middle">&rarr; 온보딩 설문 조사</text>
    <text x="55" y="64" font-size="7.5" fill="#dc2626" text-anchor="middle">&rarr; 인기도 Top-N 노출</text>

    <rect x="120" y="0" width="110" height="70" rx="4" fill="#ffffff" stroke="#f59e0b" stroke-width="1.2"/>
    <text x="175" y="18" font-size="9" font-weight="bold" fill="#b45309" text-anchor="middle">2. 행렬 희소성</text>
    <text x="175" y="36" font-size="8" fill="#334155" text-anchor="middle">희소율 99.9% 이상</text>
    <text x="175" y="52" font-size="7.5" fill="#d97706" text-anchor="middle">&rarr; 암묵적 로그(클릭)</text>
    <text x="175" y="64" font-size="7.5" fill="#d97706" text-anchor="middle">&rarr; 잠재요인 ALS 분해</text>

    <rect x="240" y="0" width="110" height="70" rx="4" fill="#ffffff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="295" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">3. 확장성 한계</text>
    <text x="295" y="36" font-size="8" fill="#334155" text-anchor="middle">수억 건 실시간 연산</text>
    <text x="295" y="52" font-size="7.5" fill="#2563eb" text-anchor="middle">&rarr; Two-Tower DNN</text>
    <text x="295" y="64" font-size="7.5" fill="#2563eb" text-anchor="middle">&rarr; HNSW 벡터 색인</text>

    <rect x="360" y="0" width="110" height="70" rx="4" fill="#ffffff" stroke="#10b981" stroke-width="1.2"/>
    <text x="415" y="18" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">4. 필터 버블</text>
    <text x="415" y="36" font-size="8" fill="#334155" text-anchor="middle">동일 장르 매몰 현상</text>
    <text x="415" y="52" font-size="7.5" fill="#059669" text-anchor="middle">&rarr; 멀티암드밴딧(MAB)</text>
    <text x="415" y="64" font-size="7.5" fill="#059669" text-anchor="middle">&rarr; 20% 무작위 탐색</text>
  </g>
</svg>
</div>

### 1. 콜드 스타트 (Cold Start)
- **원인**: 신규 진입한 유저나 아이템은 상호작용 로그가 전무하여 유사도 계산 불가
- **해결책**: 가입 즉시 관심사 3가지 선택 유도, 또는 전체 플랫폼에서 가장 인기 있는 베스트셀러(Top-N)를 기본 노출

### 2. 행렬 희소성 (Sparsity)
- **원인**: 수백만 개의 상품 중 개별 사용자가 소비하는 상품은 극소수(희소율 99.9% 이상)
- **해결책**: 별점(Explicit) 대신 클릭, 페이지 체류 시간, 장바구니 담기 등 **암묵적 피드백(Implicit Feedback)**을 수집하여 결측치를 데이터로 전환

### 3. 필터 버블 (Filter Bubble)
- **원인**: 과거 선호 아이템과 지나치게 유사한 것만 반복 추천하여 사용자의 시야를 가둠
- **해결책**: 멀티암드 밴딧(MAB, Multi-Armed Bandit) 알고리즘을 도입하여 80%는 확실한 취향(활용)을 추천하고, 20%는 새로운 카테고리를 무작위 추천(탐색)

## Ⅴ. 빅데이터 엔지니어링 관점의 필터링: 블룸 필터(Bloom Filter)

#### 한줄 요약: 추천 알고리즘 외에 데이터 파이프라인에서 중복과 부존재를 초고속 판별하는 공간 효율적 확률 자료구조

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 125" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="105" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">블룸 필터(Bloom Filter) 해시 비트 매핑 및 판정 메커니즘</text>

  <g transform="translate(30, 42)">
    <rect x="0" y="10" width="80" height="28" rx="3" fill="#eff6ff" stroke="#3b82f6"/>
    <text x="40" y="27" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">원소 "apple"</text>

    <!-- Hash Arrows -->
    <path d="M 80 24 L 140 10" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 80 24 L 140 24" stroke="#64748b" stroke-width="1.2"/>
    <path d="M 80 24 L 140 38" stroke="#64748b" stroke-width="1.2"/>

    <!-- Bit Array -->
    <g transform="translate(140, 10)">
      <rect x="0" y="0" width="22" height="28" fill="#ffffff" stroke="#94a3b8"/>
      <text x="11" y="18" font-size="9" text-anchor="middle">0</text>
      <rect x="22" y="0" width="22" height="28" fill="#dbeafe" stroke="#3b82f6"/>
      <text x="33" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1</text>
      <rect x="44" y="0" width="22" height="28" fill="#ffffff" stroke="#94a3b8"/>
      <text x="55" y="18" font-size="9" text-anchor="middle">0</text>
      <rect x="66" y="0" width="22" height="28" fill="#dbeafe" stroke="#3b82f6"/>
      <text x="77" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1</text>
      <rect x="88" y="0" width="22" height="28" fill="#ffffff" stroke="#94a3b8"/>
      <text x="99" y="18" font-size="9" text-anchor="middle">0</text>
      <rect x="110" y="0" width="22" height="28" fill="#dbeafe" stroke="#3b82f6"/>
      <text x="121" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">1</text>
    </g>

    <!-- Verdict -->
    <rect x="290" y="0" width="165" height="52" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
    <text x="300" y="20" font-size="8" font-weight="bold" fill="#dc2626">&bull; 0이 하나라도 있음 &rarr; "절대 없음(100%)"</text>
    <text x="300" y="38" font-size="8" font-weight="bold" fill="#2563eb">&bull; 모두 1로 세팅됨 &rarr; "있을 가능성 높음"</text>
  </g>
</svg>
</div>

- **블룸 필터의 핵심 특성**:
  - **False Negative(거짓 음성)가 없음**: 블룸 필터가 "이 키는 데이터베이스에 없다"고 판정하면 100% 없음 보장 $\rightarrow$ 불필요한 디스크 I/O를 원천 차단
  - **False Positive(거짓 양성)는 존재**: "있을 수도 있다"고 판정했으나 실제로는 없을 확률이 미세하게 존재 (비트 배열 크기와 해시 함수 수로 통제)
- **실무 적용**: Cassandra, RocksDB, Bigtable에서 읽기 질의 시 디스크 SSTable을 읽기 전 블룸 필터로 사전 필터링하여 디스크 I/O 90% 절감

## Ⅵ. 산업별 실무 추천 아키텍처: 2-Stage 파이프라인

#### 한줄 요약: 수백만 개 후보군을 압축하는 Retrieval 단계와 초단위 클릭률을 예측하는 Ranking 단계의 분리 설계

<div class="itpe-svg-wrapper">
<svg viewBox="0 0 520 125" width="100%" height="auto" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
  <rect x="15" y="10" width="490" height="105" rx="8" fill="var(--color-bg-secondary, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
  <text x="30" y="30" font-size="12" font-weight="bold" fill="var(--color-text-primary, #0f172a)">2-Stage 추천 파이프라인 레이턴시 &middot; 모델 분리 구조</text>

  <g transform="translate(25, 42)">
    <rect x="0" y="0" width="145" height="55" rx="4" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.2"/>
    <text x="72" y="18" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">Retrieval (10ms 이내)</text>
    <text x="72" y="34" font-size="8" fill="#334155" text-anchor="middle">Two-Tower &middot; HNSW ANN</text>
    <text x="72" y="47" font-size="7.5" fill="#2563eb" text-anchor="middle">수백만 개 &rarr; 수백 개 압축</text>

    <path d="M 150 27 L 165 27" stroke="#64748b" stroke-width="1.5"/>

    <rect x="170" y="0" width="145" height="55" rx="4" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.2"/>
    <text x="242" y="18" font-size="9" font-weight="bold" fill="#5b21b6" text-anchor="middle">Ranking (30ms 이내)</text>
    <text x="242" y="34" font-size="8" fill="#334155" text-anchor="middle">DLRM &middot; DCN 심층신경망</text>
    <text x="242" y="47" font-size="7.5" fill="#7c3aed" text-anchor="middle">CTR/CVR 예측 정밀 스코어</text>

    <path d="M 320 27 L 335 27" stroke="#64748b" stroke-width="1.5"/>

    <rect x="340" y="0" width="125" height="55" rx="4" fill="#fef2f2" stroke="#ef4444" stroke-width="1.2"/>
    <text x="402" y="18" font-size="9" font-weight="bold" fill="#991b1b" text-anchor="middle">Re-ranking (5ms 이내)</text>
    <text x="402" y="34" font-size="8" fill="#334155" text-anchor="middle">다양성 &middot; 비즈니스 룰</text>
    <text x="402" y="47" font-size="7.5" fill="#dc2626" text-anchor="middle">최종 Top-10 사용자 노출</text>
  </g>
</svg>
</div>

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 추천 필터링의 실무 아키텍처는 "단일 고성능 모델"이 아니라 **"계층화된 2-Stage 파이프라인(Retrieval + Ranking)"**으로 귀결된다. 수백만 개의 상품 카탈로그 전체에 대해 심층 신경망(DLRM)을 직접 돌리면 초당 응답 SLA(50ms)를 절대 맞출 수 없다. 따라서 Two-Tower 벡터 인덱싱(HNSW/Faiss)으로 10ms 내에 500개 후보를 1차 필터링하고, GPU 워커에서 정밀 신경망으로 30ms 내에 10개를 골라내는 분리 구조가 글로벌 빅테크의 공통 표준이다.

> **[나라면 이렇게 쓴다]**
> 10점형이라면 협업 필터링(User-Item 행동 이력)과 콘텐츠 기반 필터링(아이템 메타데이터)의 메커니즘 대조표를 명쾌하게 작성하겠다. 25점형이라면 콜드 스타트와 필터 버블 극복을 위한 MAB(멀티암드 밴딧) 전략 및 2-Stage 실시간 서빙 아키텍처를 4단 제언으로 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 단일 추천 모델 전수 채점 시 서빙 레이턴시 급증 및 신규 진입 시 콜드스타트·필터버블로 인한 이탈 증가
- **대응 (개선 방안)**: Two-Tower 벡터 검색(Retrieval)과 DLRM 심층 채점(Ranking)의 2-Stage 아키텍처 구축 및 MAB 기반 탐색-활용 균형 유지
- **검증 (검증 기준)**: 엔드투엔드 추천 응답 시간 50ms 이내 보장, 신규 유저 7일 리텐션 20% 향상, 추천 카테고리 다양성 지표(Entropy) 검증
- **효과 (실행 효과)**: 대규모 트래픽 하 실시간 맞춤 서빙 달성, 클릭 전환율(CTR) 25% 상승 및 개인화 추천 생태계의 건강성 확보

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">1</div>
    <div class="itpe-flow-step-title">현행 한계</div>
    <div class="itpe-flow-step-desc">단일 모델 추론 지연 폭증 및 콜드스타트&middot;필터버블 한계</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">2</div>
    <div class="itpe-flow-step-title">개선 방안</div>
    <div class="itpe-flow-step-desc">2-Stage 파이프라인 (Two-Tower Retrieval + DLRM Ranking) + MAB</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">3</div>
    <div class="itpe-flow-step-title">검증 기준</div>
    <div class="itpe-flow-step-desc">응답 지연 &le; 50ms, 신규 유저 리텐션 20% 향상, 다양성 지표 검증</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step-num">4</div>
    <div class="itpe-flow-step-title">실행 효과</div>
    <div class="itpe-flow-step-desc">클릭 전환율 25% 향상 및 초저지연 실시간 개인화 서빙 실현</div>
  </div>
</div>

---

## 1교시 예상문제 (10점)

> 필터링 기법 (Filtering) 및 추천 시스템과 데이터 엔지니어링의 정의, 목적, 핵심 메커니즘을 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 정의·목적

- 정의: 사용자 행동 패턴(협업) 및 콘텐츠 속성(메타데이터)을 분석하여 최적의 아이템 선별
- 목적: 대규모 후보에서 사용자나 맥락에 맞는 항목을 골라 추천의 관련성을 높인다.

### 2. 핵심 관계

| 비교 항목 | 협업 필터링 (CF) | 콘텐츠 기반 필터링 (CBF) |
|:---|:---|:---|
| **기반 데이터** | User-Item 상호작용 (평점, 클릭) | Item 텍스트/장르 메타데이터 |
| **도메인 종속성** | 완전 독립적 (아이템 내용 몰라도 됨) | 도메인 종속적 (속성 피처 정의 필수) |
| **콜드 스타트** | 치명적 취약 (신규 유저/아이템 무력) | 우수함 (신규 아이템 즉시 추천 가능) |
| **추천 다양성** | 탁월 (우연한 취향 발견) | 제한적 (보던 장르에만 갇힘) |
| **핵심 알고리즘** | SVD, ALS, Item-based 코사인 | TF-IDF, BERT 임베딩 유사도 |

### 핵심 관계

| 비교 항목 | 협업 필터링 (CF) | 콘텐츠 기반 필터링 (CBF) |
|:---|:---|:---|
| **기반 데이터** | User-Item 상호작용 (평점, 클릭) | Item 텍스트/장르 메타데이터 |
| **도메인 종속성** | 완전 독립적 (아이템 내용 몰라도 됨) | 도메인 종속적 (속성 피처 정의 필수) |
| **콜드 스타트** | 치명적 취약 (신규 유저/아이템 무력) | 우수함 (신규 아이템 즉시 추천 가능) |
| **추천 다양성** | 탁월 (우연한 취향 발견) | 제한적 (보던 장르에만 갇힘) |
| **핵심 알고리즘** | SVD, ALS, Item-based 코사인 | TF-IDF, BERT 임베딩 유사도 |

- 제언: 후보 생성과 순위화를 나누고 협업·콘텐츠 신호, 콜드스타트와 다양성 지표를 함께 점검한다.
---

## 2~4교시 예상문제 (25점)

> 빅데이터 분석 및 인공지능 추천 시스템의 핵심 기제인 필터링(Filtering)의 개념을 설명하고, 협업 필터링(Collaborative Filtering)과 콘텐츠 기반 필터링(Content-based Filtering)의 동작 메커니즘, 장단점 및 기술적 한계점(콜드 스타트, 희소성)을 극복하기 위한 하이브리드 추천 방안을 설명하시오. (25점)

---

## 2~4교시 25점 답안

### Ⅰ. 정보 과부하를 극복하는 필터링(Filtering)의 개요

1. **배경**: 수억 개 데이터 속 선택의 역설 극복 및 사용자 맞춤형 개인화 경험 제공
2. **정의**: 사용자 행동 패턴(협업) 및 콘텐츠 속성(메타데이터)을 분석하여 최적의 아이템 선별

### Ⅱ. 협업 필터링 vs 콘텐츠 기반 필터링 심층 비교

| 비교 항목 | 협업 필터링 (CF) | 콘텐츠 기반 필터링 (CBF) |
|:---|:---|:---|
| **기반 데이터** | User-Item 상호작용 (평점, 클릭) | Item 텍스트/장르 메타데이터 |
| **도메인 종속성** | 완전 독립적 (아이템 내용 몰라도 됨) | 도메인 종속적 (속성 피처 정의 필수) |
| **콜드 스타트** | 치명적 취약 (신규 유저/아이템 무력) | 우수함 (신규 아이템 즉시 추천 가능) |
| **추천 다양성** | 탁월 (우연한 취향 발견) | 제한적 (보던 장르에만 갇힘) |
| **핵심 알고리즘** | SVD, ALS, Item-based 코사인 | TF-IDF, BERT 임베딩 유사도 |

### Ⅲ. 추천 필터링 핵심 난제 극복을 위한 하이브리드 방안

1. **콜드 스타트 극복**: 신규 진입 시 콘텐츠 기반 추천 $\to$ 로그 축적 시 협업 필터링 스위칭
2. **필터 버블 해소**: 멀티암드 밴딧(MAB) 적용으로 20% 미탐색 영역 무작위 탐색 보장

### Ⅳ. 엔터프라이즈 실무 아키텍처: 2-Stage 추천 파이프라인

1. **1단계 (Retrieval)**: HNSW 벡터 색인과 Two-Tower 모델로 수백만 개 $\to$ 수백 개 고속 압축
2. **2단계 (Ranking)**: 딥러닝 DLRM 모델을 통해 실시간 클릭률(CTR)을 예측하여 최종 Top-10 노출
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 정보관리기술사 제139회 4교시 1번 (빅데이터 분석기법 중 클러스터링, 필터링, 이상치 탐지)
  - 컴퓨터시스템응용기술사 제124회 2교시 (추천 시스템의 협업 필터링과 행렬 분해 기법)
  - 정보관리기술사 제116회 1교시 (콘텐츠 기반 필터링과 협업 필터링의 비교)
- **표준 및 검증 출처**:
  - Francesco Ricci et al., *Recommender Systems Handbook (3rd Edition)*, Springer
  - Yehuda Koren, Robert Bell, Chris Volinsky (2009), "Matrix Factorization Techniques for Recommender Systems", *IEEE Computer*
  - Paul Covington et al. (2016), "Deep Neural Networks for YouTube Recommendations", *ACM RecSys*
---

## 연결 토픽

- [005. 군집분석 (Cluster Analysis)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/005_cluster_analysis.md)
- [044. 벡터 데이터베이스 (Vector Database)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/044_vector_database.md)
- [061. 시계열 실시간 이상치 탐지 (Time Series Realtime Anomaly Detection)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/061_time_series_realtime_anomaly_detection.md)
