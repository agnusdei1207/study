---
sidebar:
  order: 43
  label: "043. 데이터마이닝 (Data Mining)"
  badge:
    text: "A"
    variant: note
title: "데이터마이닝 (Data Mining)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 43
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "043"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터 분석·활용</span><span>빅데이터 분석·지식 발견(KDD)</span><strong>데이터마이닝</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-box" role="img" aria-label="데이터마이닝 4대 분석 기법 및 지식 발견 흐름도">
<svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-dm" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
    <filter id="shadow-dm" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="rgba(0,0,0,0.1)"/>
    </filter>
  </defs>

  <rect x="15" y="15" width="490" height="40" rx="8" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5" filter="url(#shadow-dm)"/>
  <text x="260" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">대용량 원천 데이터 (DW / Data Lake / NoSQL / Stream)</text>
  <text x="260" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="10" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">KDD 5단계 / CRISP-DM 6단계 지식 발견 프로세스 적용</text>

  <path d="M 260 55 L 260 75" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2" marker-end="url(#arrow-dm)"/>

  <rect x="15" y="80" width="490" height="85" rx="8" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" stroke-dasharray="3 3"/>
  <text x="30" y="98" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">데이터마이닝 4대 핵심 분석 기법</text>

  <!-- 분류 -->
  <rect x="25" y="105" width="110" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="80" y="123" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">분류 (Classification)</text>
  <text x="80" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">지도학습 · 범주형</text>
  <text x="80" y="149" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">의사결정나무, RF, SVM</text>

  <!-- 예측 -->
  <rect x="145" y="105" width="110" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="200" y="123" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">예측 (Regression)</text>
  <text x="200" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">지도학습 · 연속형</text>
  <text x="200" y="149" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">선형회귀, Ridge, Lasso</text>

  <!-- 군집화 -->
  <rect x="265" y="105" width="110" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="320" y="123" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">군집 (Clustering)</text>
  <text x="320" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">비지도학습 · 자율화</text>
  <text x="320" y="149" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">K-Means, DBSCAN</text>

  <!-- 연관분석 -->
  <rect x="385" y="105" width="110" height="50" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="440" y="123" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">연관 (Association)</text>
  <text x="440" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">비지도학습 · 장바구니</text>
  <text x="440" y="149" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">Apriori, FP-Growth</text>

  <path d="M 260 165 L 260 180" stroke="var(--sl-color-accent, #2563eb)" stroke-width="2" marker-end="url(#arrow-dm)"/>

  <rect x="15" y="185" width="490" height="28" rx="6" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5"/>
  <text x="260" y="203" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">실행 가능한 비즈니스 통찰 (Actionable Insight) — FDS 탐지, 초개인화 추천, 공정 최적화</text>
</svg>
</div>

- 본질: **대용량 데이터베이스에 은닉된 비명시적(Implicit), 사전 미인지(Previously Unknown), 잠재적으로 유용한(Potentially Useful) 패턴과 규칙을 통계학, 인공지능, 기계학습 알고리즘을 융합하여 자동으로 발굴하는 지식 발견(KDD)의 핵심 공정**
- 암기: `분-예-군-연` (4대 기법: 분류 · 예측 · 군집 · 연관) / `비-데-준-모-평-배` (CRISP-DM 6단계: 비즈니스이해 $\rightarrow$ 데이터이해 $\rightarrow$ 데이터준비 $\rightarrow$ 모델링 $\rightarrow$ 평가 $\rightarrow$ 배포)
- 연관분석 3대 평가 척도: `지-신-향` = 지지도(Support, 동시발생확률) · 신뢰도(Confidence, 조건부확률) · 향상도(Lift, 독립 대비 상관성, >1 유의)
- OLAP와의 차이: OLAP는 사용자가 가설을 세우고 질의로 검증하는 **가설 검증형(Verification-driven)**인 반면, 데이터마이닝은 알고리즘이 가설을 스스로 찾아내는 **가설 발견형(Discovery-driven)**임
---

## 1교시 예상문제 (10점)

> 데이터마이닝 (Data Mining)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. 데이터마이닝의 정의

- 대용량 데이터베이스로부터 통계·기계학습 알고리즘을 융합하여 실행 가능한 패턴과 지식을 자동으로 발굴하는 **가설 발견형(Discovery-driven) 지식 발견(KDD) 핵심 기법**

### 2. 4대 주요 기법 및 연관분석 3대 지표

- **4대 기법 분류 체계**:
  - 지도학습: 분류(Classification, 범주형 판정) / 예측(Regression, 연속형 수치 예측)
  - 비지도학습: 군집화(Clustering, 자율 그룹화) / 연관분석(Association, 장바구니 패턴)

| 연관분석 3대 지표 | 수학적 수식 | 핵심 의미 | 판정 기준 |
|---|---|---|---|
| **지지도 (Support)** | $P(A \cap B)$ | 전체 거래 중 동시 발생 비율 | 규칙의 보편성 판정 (최소 지지도 필터) |
| **신뢰도 (Confidence)** | $P(B \mid A) = \frac{P(A \cap B)}{P(A)}$ | $A$ 구매 시 $B$도 함께 구매할 조건부 확률 | 규칙의 강도 및 조건부 신뢰성 |
| **향상도 (Lift)** | $\frac{P(A \cap B)}{P(A) \cdot P(B)}$ | 독립 대비 연관 발생 강도 | $Lift > 1$ (유의미), $=1$ (독립), $<1$ (음의 상관) |

### 3. 차별화 제언

- 단순한 블랙박스 모델 배포를 지양하고, **SHAP/LIME 기반 설명 가능한 AI(XAI)** 및 **MLOps 드리프트 실시간 감시 체계**를 결합하여 모델 수용성과 신뢰도를 극대화함
---

## 2~4교시 예상문제 (25점)

> 빅데이터 환경에서 데이터마이닝(Data Mining)의 개념과 지식 발견 프로세스(KDD 및 CRISP-DM)를 설명하고, 데이터마이닝의 4대 주요 분석 기법(분류, 예측, 군집, 연관규칙)의 특징 및 연관분석의 3대 평가 지표를 논하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 데이터 속에 숨겨진 금맥을 찾는 지식 발견, 데이터마이닝 개요

- 정의: **데이터마이닝(Data Mining)**은 방대한 양의 정형·비정형 데이터베이스로부터 통계적 기법, 인공지능(AI), 패턴 인식, 기계학습 알고리즘을 동원하여 의사결정에 활용 가능한 패턴, 상관관계, 추세를 추출하는 지식 발견(KDD, Knowledge Discovery in Databases)의 중심 단계
- 목적: 복잡하고 방대한 원천 데이터를 실행 가능한 비즈니스 통찰(Actionable Insight)로 전환하여 고객 이탈 방지, 사기 탐지(FDS), 정밀 타겟 마케팅, 설비 고장 예측 등 비즈니스 경쟁력 극대화
- 필요성: 데이터의 양이 기하급수적으로 폭증함에 따라 전통적인 SQL 질의나 인간의 직관적 분석만으로는 고차원 비선형 상관관계를 찾아내는 것이 불가능해짐

#### 한줄 요약

- 데이터마이닝은 대규모 데이터에서 인간의 가설 없이도 유의미한 비즈니스 패턴을 수학적으로 자동 채굴하는 공학 기술임

### Ⅱ. 데이터마이닝 표준 방법론: KDD 5단계 vs CRISP-DM 6단계

<div class="itpe-diagram-box" role="img" aria-label="KDD 5단계 및 CRISP-DM 6단계 프로세스 비교도">
<svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-kdd" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
  </defs>

  <!-- KDD 파이프라인 -->
  <text x="15" y="20" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">[KDD 5단계 순차 파이프라인 (학술 표준)]</text>

  <rect x="15" y="30" width="85" height="40" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="57" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">1. 데이터 선택</text>
  <text x="57" y="61" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">Selection</text>

  <path d="M 100 50 L 115 50" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>

  <rect x="115" y="30" width="85" height="40" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="157" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">2. 전처리 정제</text>
  <text x="157" y="61" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">Preprocessing</text>

  <path d="M 200 50 L 215 50" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>

  <rect x="215" y="30" width="85" height="40" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="257" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">3. 데이터 변환</text>
  <text x="257" y="61" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">Transformation</text>

  <path d="M 300 50 L 315 50" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>

  <rect x="315" y="30" width="85" height="40" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="357" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">4. 마이닝</text>
  <text x="357" y="61" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">Data Mining</text>

  <path d="M 400 50 L 415 50" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>

  <rect x="415" y="30" width="90" height="40" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="460" y="47" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">5. 해석 및 평가</text>
  <text x="460" y="61" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">Evaluation</text>

  <!-- CRISP-DM 순환 모델 -->
  <text x="15" y="105" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">[CRISP-DM 6단계 순환 모델 (산업계 표준)]</text>

  <rect x="15" y="120" width="145" height="38" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="87" y="136" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">1. 비즈니스 이해</text>
  <text x="87" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">목표 정의 및 기준 수립</text>

  <path d="M 160 134 L 185 134" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>
  <path d="M 185 144 L 160 144" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1" marker-end="url(#arrow-kdd)"/>

  <rect x="185" y="120" width="145" height="38" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="257" y="136" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">2. 데이터 이해</text>
  <text x="257" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">데이터 수집 및 EDA 탐색</text>

  <path d="M 330 139 L 355 139" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>

  <rect x="355" y="120" width="150" height="38" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="430" y="136" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">3. 데이터 준비 (70~80%)</text>
  <text x="430" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">정제, 결합, 피처 엔지니어링</text>

  <!-- 하단 순환 -->
  <path d="M 430 158 L 430 175" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>

  <rect x="355" y="175" width="150" height="38" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="430" y="191" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">4. 모델링 (Modeling)</text>
  <text x="430" y="205" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">알고리즘 선정 및 튜닝</text>

  <path d="M 355 189 L 330 189" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>
  <path d="M 330 199 L 355 199" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1" marker-end="url(#arrow-kdd)"/>

  <rect x="185" y="175" width="145" height="38" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="257" y="191" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">5. 평가 (Evaluation)</text>
  <text x="257" y="205" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">비즈니스 목표 달성 검증</text>

  <path d="M 185 194 L 160 194" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-kdd)"/>

  <rect x="15" y="175" width="145" height="38" rx="6" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="87" y="191" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">6. 배포 (Deployment)</text>
  <text x="87" y="205" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">운영 서빙 및 MLOps 감시</text>

  <!-- 5단계 평가에서 1단계 비즈니스이해로의 피드백 화살표 -->
  <path d="M 230 175 C 210 162 130 162 110 158" fill="none" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1" stroke-dasharray="2 2" marker-end="url(#arrow-kdd)"/>
</svg>
</div>

| 방법론 | 단계별 세부 수행 활동 | 핵심 특징 및 비교 |
|---|---|---|
| **KDD 5단계<br>(학술 표준)** | 1. **선택 (Selection)**: 분석 목적에 부합하는 타깃 데이터셋 추출<br>2. **전처리 (Preprocessing)**: 노이즈, 결측치, 이상치 정제 및 무결성 확보<br>3. **변환 (Transformation)**: 정규화, 차원 축소, 피처 엔지니어링<br>4. **마이닝 (Data Mining)**: 분류, 군집, 연관 분석 알고리즘 적용<br>5. **해석/평가 (Evaluation)**: 패턴 시각화 및 지식 유효성 검증 | 데이터 중심의 순차적 공학 파이프라인에 초점을 둔 전통적 지식 발견 프로세스 |
| **CRISP-DM 6단계<br>(산업 표준)** | 1. **비즈니스 이해**: 문제 정의, 프로젝트 목표, 성공 기준 수립<br>2. **데이터 이해**: 원천 수집, 탐색적 분석(EDA), 품질 식별<br>3. **데이터 준비**: 데이터셋 편성, 레코드 정제, 피처 생성 (전체 공수 70~80%)<br>4. **모델링**: 머신러닝 알고리즘 선정, 하이퍼파라미터 튜닝<br>5. **평가**: 비즈니스 목표 달성도 평가 및 모델 검증<br>6. **배포**: 운영 환경 시스템 서빙, 모니터링 체계 구축 | 비즈니스 가치를 최우선으로 두며, 단계 간의 피드백과 반복(Iteration)을 허용하는 산업계 표준 |

#### 한줄 요약

- KDD가 데이터 중심의 5단계 순차 파이프라인이라면, CRISP-DM은 비즈니스 목표 중심의 6단계 순환형 산업 방법론임

### Ⅲ. 데이터마이닝 4대 핵심 분석 기법 및 세부 알고리즘

| 기법 | 분석 목적 및 입력 데이터 | 대표 알고리즘 | 적용 사례 |
|---|---|---|---|
| **분류<br>(Classification)** | 과거 레이블 데이터를 학습하여 새로운 데이터의 범주(Class) 판정 (지도학습) | 의사결정나무(C4.5, CART), 랜덤 포레스트, XGBoost, 로지스틱 회귀, SVM | 카드 결제 이상 거래 탐지(FDS), 대출 심사 부도 예측, 스팸 메일 필터링 |
| **수치 예측<br>(Regression)** | 독립변수와 종속변수 간의 함수적 인과관계를 학습하여 연속값 예측 (지도학습) | 선형 회귀, 릿지/라쏘, 서포트 벡터 회귀(SVR), 딥러닝 MLP | 분기별 제품 수요량 예측, 부동산 실거래가 산정, 주행 배터리 잔량 예측 |
| **군집화<br>(Clustering)** | 사전 지식 없이 데이터 간 거리·유사도 기반으로 자율적 그룹 분할 (비지도학습) | K-Means, K-Medoids, DBSCAN, 병합형 계층 군집(Agglomerative) | 신규 앱 고객 라이프스타일 세분화, 악성코드 유사 패밀리 분류 |
| **연관분석<br>(Association)** | 대규모 트랜잭션 내에서 특정 항목 간의 동시 발생 패턴 탐색 (비지도학습) | Apriori, FP-Growth, ECLAT | 마트 장바구니 상품 진열 최적화, 온라인 쇼핑몰 추천 시스템 |

#### 한줄 요약

- 데이터마이닝 기법은 정답 유무에 따라 분류/예측(지도)과 군집/연관(비지도)으로 대별되며, 업무 목적에 맞게 복합 결합됨

### Ⅳ. 장바구니 분석(Market Basket Analysis)과 연관분석 3대 평가 지표

<div class="itpe-diagram-box" role="img" aria-label="연관규칙 3대 평가 지표 도해">
<svg viewBox="0 0 520 160" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <!-- 전체 거래 공간 -->
  <rect x="20" y="20" width="220" height="120" rx="8" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5"/>
  <text x="35" y="38" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-gray-3, #64748b)">전체 거래 집합 (N)</text>

  <!-- 원 A -->
  <circle cx="95" cy="85" r="45" fill="rgba(37, 99, 235, 0.15)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="70" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="var(--sl-color-accent, #2563eb)">A 구매</text>

  <!-- 원 B -->
  <circle cx="160" cy="85" r="45" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1.5"/>
  <text x="180" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="11" font-weight="700" fill="#10b981">B 구매</text>

  <!-- 교집합 -->
  <text x="127" y="88" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">A ∩ B</text>

  <!-- 우측 설명 카드 -->
  <rect x="260" y="20" width="240" height="36" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="270" y="36" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">지지도 (Support)</text>
  <text x="270" y="49" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">P(A ∩ B) : 전체 거래 중 동시 발생 비율 (보편성 검증)</text>

  <rect x="260" y="62" width="240" height="36" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="270" y="78" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="#10b981">신뢰도 (Confidence)</text>
  <text x="270" y="91" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">P(B|A) = P(A ∩ B) / P(A) : A 구매 시 B 수반 확률</text>

  <rect x="260" y="104" width="240" height="36" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="270" y="120" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">향상도 (Lift)</text>
  <text x="270" y="133" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)">P(A ∩ B) / [P(A)·P(B)] : 독립 대비 연관성 (> 1 유효)</text>
</svg>
</div>

| 평가 지표 | 수학적 수식 정의 | 의미 및 해석 | 실무 판정 기준 |
|---|---|---|---|
| **지지도<br>(Support)** | $Support(A \rightarrow B) = P(A \cap B) = \frac{n(A \cap B)}{N}$ | 전체 거래 중 항목 $A$와 $B$가 **동시에 포함될 확률** | 규칙의 중요도와 보편성 판정 (최소 지지도 미달 시 규칙 탈락) |
| **신뢰도<br>(Confidence)** | $Confidence(A \rightarrow B) = P(B \mid A) = \frac{P(A \cap B)}{P(A)}$ | 항목 $A$를 구매한 거래 중 항목 $B$도 **함께 구매했을 조건부 확률** | 규칙의 신뢰성 및 강도 판정 (인과 방향성 검증) |
| **향상도<br>(Lift)** | $Lift(A \rightarrow B) = \frac{P(A \cap B)}{P(A) \cdot P(B)} = \frac{Confidence(A \rightarrow B)}{P(B)}$ | $A$의 구매가 $B$의 구매 확률을 **독립 대비 몇 배나 증가시켰는지**의 비율 | - **$Lift > 1$**: 양의 상관관계 (의미 있는 규칙)<br>- **$Lift = 1$**: 독립 (우연한 동시 발생)<br>- **$Lift < 1$**: 음의 상관관계 (상충 배제) |

#### 한줄 요약

- 연관분석은 지지도(충분한 발생 빈도)와 신뢰도(높은 수반 확률)를 통과한 후, 향상도($Lift > 1$)를 통해 진짜 연관 관계를 판정함

### Ⅴ. 데이터마이닝 vs OLAP 심층 비교

| 비교 항목 | 데이터마이닝 (Data Mining) | OLAP (Online Analytical Processing) |
|---|---|---|
| **분석 패러다임** | **가설 발견형 (Discovery-driven)** | **가설 검증형 (Verification-driven)** |
| **접근 방식** | 귀납적 (데이터 패턴으로부터 규칙 자동 도출) | 연역적 (사용자가 설정한 가설을 데이터를 통해 확인) |
| **주도 주체** | 기계학습 알고리즘, 통계 엔진 | 사용자, 비즈니스 분석가 (인간의 직관) |
| **사용자 개입** | 모델링 파라미터 조정 후 알고리즘 실행 | 다차원 축 슬라이싱, 다이싱, 드릴다운 수동 조작 |
| **결과 산출물** | 숨겨진 비선형 규칙, 클러스터, 예측 모델 | 집계된 다차원 요약 차트, 피벗 테이블 |
| **상호 보완성** | 데이터마이닝으로 새로운 패턴을 발견하고, OLAP로 해당 패턴의 세부 원인을 드릴다운 검증함 |

#### 한줄 요약

- OLAP는 인간이 세운 가설을 확인하고, 데이터마이닝은 인간이 생각지 못한 새로운 가설을 데이터에서 발굴함

### Ⅵ. 데이터마이닝 실무 장애 요인 및 엔지니어링 대책

| 문제 상황 | 근본 원인 | 실무 엔지니어링 대책 | 개선 효과 |
|---|---|---|---|
| **거짓 상관관계(Spurious Correlation) 채택** | 수만 개 피처 중 우연히 통계적 유의성이 나온 무의미한 규칙 채택 | 도메인 전문가 검증 필터 및 교차 검증(Cross-Validation), 홀드아웃 테스트 | 현업 적용 가능한 실제 인과 지식 확보 |
| **극심한 클래스 불균형에 따른 예측 실패** | 사기 거래율 0.05% 환경에서 단순 정확도(Accuracy)만 최적화 | **SMOTE 오버샘플링** 및 **F1-Score, AUPRC(PR곡선) 평가 척도** 적용 | 소수 희귀 패턴 탐지율 대폭 개선 |
| **블랙박스 모델로 인한 현업 적용 거부** | 딥러닝/앙상블 모델의 높은 정확도 대비 판정 근거 설명 불능 | **XAI(설명 가능한 AI, SHAP·LIME)** 대시보드 연계로 피처 중요도 시각화 | 모델 해석력 및 비즈니스 수용성 확보 |
| **시간 경과에 따른 모델 성능 저하** | 소비자 트렌드 및 외부 거시환경 변화로 인한 **데이터 드리프트(Drift)** | **MLOps 기반 모델 드리프트 실시간 감시** 및 성능 임계치 미달 시 자동 재학습 | 상시 고성능 예측 유지 |

#### 한줄 요약

- 가짜 상관 배제, 클래스 불균형 보정, XAI 설명력 확보, MLOps 모니터링이 실무 마이닝의 4대 핵심 성공 요인임

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 데이터마이닝의 본질은 "알고리즘의 화려함"이 아니라 "비즈니스 의사결정으로의 전환율"에 있다. 아무리 정교한 딥러닝/XGBoost 모델이라도 현업 도메인 전문가가 판정 근거를 이해하지 못하면 현장에 배포되지 못하고 사장된다. 따라서 엔지니어링의 성패는 모델의 F1-score 0.01을 올리는 것보다, 전처리 파이프라인의 견고성(CRISP-DM의 70~80% 비중)과 XAI(SHAP)를 통한 신뢰성 확보, 그리고 실시간 데이터 파이프라인에 모델을 무중단 서빙하는 MLOps 체계 구축에 달려 있다.

> **[나라면 이렇게 쓴다]**
> 답안 3단락 차별화 전략으로 "전통적 통계 마이닝 + 생성형 AI(에이전틱 LLM)의 하이브리드 지식 발견 체계"를 제시하겠다. 정형 DW 수치 데이터는 XGBoost와 연관분석으로 패턴을 1차 채굴하고, 도출된 통계 규칙을 RAG의 지식 청크로 변환하여 LLM 에이전트가 "특정 고객군의 이탈 원인 및 맞춤형 프로모션 전략 보고서"를 자연어로 자동 기안하도록 설계하는 파이프라인을 제시하여 실무 아키텍처 역량을 피력한다.

### 실전 답안용 기술사적 제언

- **[전통적 배치 마이닝의 한계와 실시간 인텔리전스 전환]**: 정적 DW 기반의 사후 배치 분석은 급변하는 온라인 트랜잭션의 이상 거래나 이탈 징후를 실시간으로 방어하기 어려움
- **[실무 대응 방안]**: 카프카(Kafka) 기반 스트리밍 데이터 파이프라인과 실시간 피처 스토어(Feast)를 결합하고, 추론 엔진에 경량 ONNX 모델을 서빙하여 밀리초 단위 즉각 추론 구현
- **[XAI 및 거버넌스 검증]**: 금융·의료 분야 배포 시 SHAP/LIME을 통한 특징 기여도 산출 및 데이터 편향성(Bias) 모니터링을 표준화하여 모델 신뢰도 보증

<div class="itpe-flow-map" role="group" aria-label="데이터마이닝 현행 한계 극복 4단계 흐름">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">1</div>
    <div class="itpe-flow-step__title">현행 한계</div>
    <div class="itpe-flow-step__desc">정적 배치 마이닝 지연 및 블랙박스 모델 판정 근거 설명 불능</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">2</div>
    <div class="itpe-flow-step__title">개선 방안</div>
    <div class="itpe-flow-step__desc">Kafka 스트리밍 + 피처 스토어 결합 및 SHAP 기반 실시간 XAI 서빙</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">3</div>
    <div class="itpe-flow-step__title">검증 기준</div>
    <div class="itpe-flow-step__desc">추론 지연시간 &lt; 50ms, F1-Score &gt; 0.92, 설명력 대시보드 100% 매핑</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">4</div>
    <div class="itpe-flow-step__title">실행 효과</div>
    <div class="itpe-flow-step__desc">FDS 실시간 방어율 35% 향상 및 현업 의사결정 리드타임 80% 단축</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- 제129회 공식 문제지: 빅데이터 환경에서 데이터마이닝의 개념, 주요 분석 기법 및 수행 절차
- [Han, J., Kamber, M., & Pei, J. (2011). Data Mining: Concepts and Techniques (3rd ed.)](https://www.elsevier.com/books/data-mining-concepts-and-techniques/han/978-0-12-381479-1)
- [CRISP-DM 1.0: Step-by-step data mining guide (SPSS)](https://www.the-modeling-agency.com/crisp-dm.pdf)

## 연결 토픽

- [군집 분석(K-Means)](./029_k_means/) · [텍스트 마이닝](./015_text_mining/) · [OLAP](./039_olap/) · [차원 축소(PCA)](./069_dimensionality_reduction_pca_mds/)
