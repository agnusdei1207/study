---
sidebar:
  order: 97
  label: "097. AI·데이터 기반 행정"
  badge:
    text: "A"
    variant: note
title: "데이터기반행정 및 AI 기반 공공의사결정 거버넌스 체계"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 97
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "097"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>데이터 거버넌스·공공데이터</span><strong>데이터기반행정</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-container" style="max-width: 520px; margin: 1rem auto;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" role="img" aria-label="전통 데이터 행정에서 AI 데이터 기반 선제 행정으로의 진화">
  <defs>
    <marker id="admArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #3b82f6)"/>
    </marker>
  </defs>
  <!-- Background Card -->
  <rect width="520" height="220" rx="10" fill="var(--sl-color-bg-sidebar, #f8fafc)" stroke="var(--sl-color-hairline, #e2e8f0)" stroke-width="1.5"/>

  <!-- Left: Traditional Administration -->
  <g transform="translate(20, 20)">
    <rect width="215" height="180" rx="8" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-hairline, #cbd5e1)"/>
    <rect width="215" height="32" rx="8" fill="#f1f5f9"/>
    <text x="107" y="21" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-2, #475569)">과거: 전통 데이터 행정</text>

    <text x="18" y="58" font-size="10" font-weight="700" fill="var(--sl-color-text, #1e293b)">• 정형 데이터 중심</text>
    <text x="28" y="75" font-size="9" fill="var(--sl-color-gray-2, #64748b)">RDBMS 통계표, 인구 센서스</text>

    <text x="18" y="105" font-size="10" font-weight="700" fill="var(--sl-color-text, #1e293b)">• 사후 통계 집계</text>
    <text x="28" y="122" font-size="9" fill="var(--sl-color-gray-2, #64748b)">"작년 복지 사각지대 보고서"</text>

    <text x="18" y="152" font-size="10" font-weight="700" fill="var(--sl-color-text, #1e293b)">• 수동적 신청주의</text>
    <text x="28" y="169" font-size="9" fill="var(--sl-color-gray-2, #64748b)">국민이 직접 증명서류 제출</text>
  </g>

  <!-- Center Arrow -->
  <path d="M 240 110 L 275 110" stroke="var(--sl-color-accent, #3b82f6)" stroke-width="2" marker-end="url(#admArr)"/>
  <text x="258" y="98" text-anchor="middle" font-size="8.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)">초거대 AI</text>
  <text x="258" y="128" text-anchor="middle" font-size="8.5" fill="var(--sl-color-gray-2, #64748b)">다차원 융합</text>

  <!-- Right: AI & Data Driven Administration -->
  <g transform="translate(285, 20)">
    <rect width="215" height="180" rx="8" fill="var(--sl-color-accent, #eff6ff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
    <rect width="215" height="32" rx="8" fill="var(--sl-color-accent, #dbeafe)"/>
    <text x="107" y="21" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-accent, #1e40af)">미래: AI·데이터 기반 행정</text>

    <text x="18" y="58" font-size="10" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">• 다차원 이종 데이터 융합</text>
    <text x="28" y="75" font-size="9" fill="var(--sl-color-text, #334155)">단전/수도/통신 + 민원 VoC + GIS</text>

    <text x="18" y="105" font-size="10" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">• 선제적 예측 시뮬레이션</text>
    <text x="28" y="122" font-size="9" fill="var(--sl-color-text, #334155)">"위기 위험 가구 AI 사전 발굴"</text>

    <text x="18" y="152" font-size="10" font-weight="700" fill="var(--sl-color-accent, #1d4ed8)">• 능동적 선제주의 (HITL)</text>
    <text x="28" y="169" font-size="9" fill="var(--sl-color-text, #334155)">맞춤형 혜택 추천 + 인간 감독관</text>
  </g>
</svg>
</div>

- 본질: **공공기관이 보유한 행정 데이터와 외부 민간 데이터를 상호 연계·분석하여 직관과 경험 중심의 관행적 행정을 탈피하고, 초거대 AI(sLLM)와 예측 모델을 결합하여 복지 사각지대 발굴, 재난 대응, 정책 시뮬레이션 등 국민 중심의 선제적(Proactive) 공공서비스를 제공하는 지능형 정부 혁신 체계**
- 암기: `수-연-분-활-평` (데이터기반행정 5대 생명주기: 수집, 연계, 분석, 활용, 평가) / `선-비-인-윤` (핵심요소: 선제적 예측, 비정형 융합, 인간개입 HITL, AI 윤리)
- 판단축:
  - **전통적 데이터기반행정**: 사후 통계 집계 및 실적 모니터링 중심, 정형 데이터 위주, 수동적 신청주의
  - **AI·데이터 기반 행정**: 생성형 AI 및 머신러닝 기반 미래 위험 선제 예측, 비정형(민원 텍스트, 음성, 영상) 융합, 자동 추천 선제주의
- 주의: 행정 처분과 복지 혜택 산정 시 AI 모델의 편향(Bias)이나 환각(Hallucination)으로 인한 위법 처분을 방지하기 위해 반드시 **Human-in-the-Loop(인간 감독관 최종 승인)** 원칙과 설명 가능한 AI(XAI) 체계가 전제되어야 함
---

## 1교시 예상문제 (10점)

> 데이터기반행정 및 AI 기반 공공의사결정 거버넌스 체계의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### [문제] AI·데이터 기반 행정

#### 1. AI·데이터 기반 행정의 정의
- 공공·민간 데이터를 연계 분석하고 초거대 AI(sLLM) 및 예측 모델을 정책 전주기에 적용하여 선제적 국민 맞춤 서비스를 제공하는 지능형 국정 운영 체계

#### 2. 추진 아키텍처 및 전통 행정과의 차이점

| 구분 | 전통적 데이터기반행정 | AI·데이터 기반 행정 |
|:---|:---|:---|
| **의사결정 시점** | 사후 통계 분석 (Descriptive) | 실시간 미래 예측 및 처방 (Predictive) |
| **서비스 방식** | 국민 신청주의 (수동적) | 능동적 선제주의 (사전 발굴 및 추천) |
| **핵심 기술** | RDBMS, 통계 패키지, BI | sLLM, 머신러닝, RAG, 디지털 트윈 |
| **데이터 범위** | 기관 내부 정형 데이터 | 범정부 행정 + 민원 VoC + 통신/IoT 비정형 |

- **4단 참조 아키텍처**: 대국민 선제 서비스 $\rightarrow$ 공공 sLLM/정책 시뮬레이터 $\rightarrow$ 통합 데이터 레이크하우스 $\rightarrow$ 범정부 연계 허브

#### 3. 성공 요건 및 신뢰성 확보 방안
- 부처 간 사일로 타파를 위한 법적 면책, 공공 폐쇄망 sLLM 구축, Human-in-the-Loop 기반 오류 검증 체계 확립
---

### 핵심 관계

| 아키텍처 계층 | 핵심 구성 요소 | 수행 역할 및 핵심 기술 |
|:---|:---|:---|
| **1. 서비스 계층** | 마이데이터(MyData), 혜택 알리미 | 국민이 일일이 신청하지 않아도 자격을 사전 판별하여 맞춤형 서비스 원스톱 제공 |
| **2. 정책 지원 계층** | 공공 sLLM, 정책 시뮬레이터 | 인구 소멸, 교통 흐름, 세수 예측 등 다차원 정책 효과 사전 시뮬레이션 및 보고서 초안 작성 |
| **3. AI 인프라 계층** | 공공 GPU 클러스터, RAG 파이프라인 | 정부 법령·지침 데이터 기반 검색증강생성(RAG) 구축으로 환각 차단 및 모델 파인튜닝 |
| **4. 연계·수집 계층** | 범정부 데이터 연계 플랫폼 | 부처 간 칸막이(사일로)를 제거하고 API 기반 메타데이터 표준화 및 가명정보 결합 지원 |

---

## 2~4교시 예상문제 (25점)

> 「데이터기반행정 활성화에 관한 법률」의 발전 흐름에 따른 'AI·데이터 기반 행정'의 개념과 추진 아키텍처를 제시하고, 전통적 데이터 행정과의 비교 및 범정부 데이터 연계와 AI 도입 시 실무 고려사항을 설명하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### Ⅰ. 지능형 디지털플랫폼정부를 실현하는 AI·데이터 기반 행정 개요

#### 한줄 요약: 축적된 공공데이터와 초거대 AI 기술을 결합하여 사후 집계형 행정을 미래 예측형·국민 맞춤형 선제 행정으로 전환하는 패러다임

- **배경**: 복잡다단한 사회적 위험(이상기후 재난, 고독사, 신종 사기 범죄 등)이 증가함에 따라 과거 사후 대증적 행정 방식으로는 선제적 예방 한계 봉착
- **정의**: 공공기관 등이 보유·관리하는 행정 데이터와 민간 데이터를 과학적으로 수집·연계·분석하고, 초거대 AI(sLLM) 및 예측 알고리즘을 정책 수립부터 집행, 사후 환류까지 전주기에 적용하는 지능형 국정 운영 모델
- **법적 근거**: 「데이터기반행정 활성화에 관한 법률」(데이터기반행정법) 및 「디지털플랫폼정부 실현계획」

### Ⅱ. AI·데이터 기반 행정의 범정부 참조 아키텍처

#### 한줄 요약: 범정부 데이터 연계 허브, 공공 특화 AI 모델, 대국민 선제 서비스 계층의 4단 구조

| 아키텍처 계층 | 핵심 구성 요소 | 수행 역할 및 핵심 기술 |
|:---|:---|:---|
| **1. 서비스 계층** | 마이데이터(MyData), 혜택 알리미 | 국민이 일일이 신청하지 않아도 자격을 사전 판별하여 맞춤형 서비스 원스톱 제공 |
| **2. 정책 지원 계층** | 공공 sLLM, 정책 시뮬레이터 | 인구 소멸, 교통 흐름, 세수 예측 등 다차원 정책 효과 사전 시뮬레이션 및 보고서 초안 작성 |
| **3. AI 인프라 계층** | 공공 GPU 클러스터, RAG 파이프라인 | 정부 법령·지침 데이터 기반 검색증강생성(RAG) 구축으로 환각 차단 및 모델 파인튜닝 |
| **4. 연계·수집 계층** | 범정부 데이터 연계 플랫폼 | 부처 간 칸막이(사일로)를 제거하고 API 기반 메타데이터 표준화 및 가명정보 결합 지원 |

### Ⅲ. 전통적 데이터기반행정 vs AI·데이터 기반 행정 비교

#### 한줄 요약: 단순 통계 분석에서 비정형 데이터 융합과 초거대 AI 예측 자동화로의 진화

| 비교 항목 | 전통적 데이터기반행정 | AI·데이터 기반 행정 |
|:---|:---|:---|
| **주요 분석 대상** | 공공기관 내부의 정형 행정 통계 (RDBMS) | 정형 행정 데이터 + 민원 VoC, CCTV, 통신 유동인구, SNS 비정형 데이터 |
| **의사결정 시점** | **사후 분석 (Descriptive / Diagnostic)** | **실시간 예측 및 처방 (Predictive / Prescriptive)** |
| **서비스 제공 방식** | 국민 신청주의 (국민이 신청해야 지급) | 선제적 능동주의 (위기 징후 감지 시 정부가 선제 발굴 및 지원) |
| **핵심 적용 기술** | 통계 패키지(SPSS, SAS), OLAP, BI 대시보드 | 초거대 AI(sLLM), 머신러닝, RAG, 디지털 트윈, 공간 빅데이터 |
| **공무원 업무 형태** | 수작업 데이터 취합 및 수동 보고서 작성 | 공공 AI 어시스턴트를 통한 초안 작성, 검색 및 요약 자동화 |
| **데이터 결합** | 기관 내부 또는 동일 부처 내 제한적 결합 | 이종 부처 간 행정정보 공동이용 및 민·관 가명정보 대규모 결합 |

### Ⅳ. 핵심 메커니즘: 선제적 위기 가구 발굴 파이프라인

#### 한줄 요약: 다기관 복합 신호(Signal)를 감지하여 고독사 및 복지 사각지대를 자동 식별하는 실사례

- **다기관 이종 데이터 연계 신호**:
  - 한국전력: 3개월 연속 단전 징후
  - 상하수도: 수도 사용량 0L
  - 건강보험공단: 건보료 6개월 체납
  - 통신사: 통신요금 연체 및 위치 신호 부재
- **가명결합 및 머신러닝 스코어링**:
  - 개인식별정보 가명화 후 XGBoost/Random Forest 위험도 예측 모델 실행 $\rightarrow$ 위기 지수(Score) 산출
- **선제적 현장 복지 출동**:
  - 읍면동 사회복지사 모바일 앱으로 고위험 가구 위치 및 사유 자동 전송 $\rightarrow$ 긴급 복지 지원 집행
- **성과**: 복지 사각지대 발굴 기간을 기존 2~3개월에서 수일 이내로 단축하여 인명 사고 예방

### Ⅴ. 성공적 추진을 위한 공공 데이터 거버넌스 3대 축

#### 한줄 요약: 데이터 품질 표준화, 범정부 메타데이터 공유, 개인정보 보호의 제도적 정착

1. **공공데이터 표준화 및 품질 관리**:
   - 행정안전부 '공공데이터 공통표준용어' 준수
   - 기관별 상이한 코드(예: 성별, 행정구역코드) 표준 매핑
2. **범정부 메타데이터 등록 의무화**:
   - 국가데이터맵을 통한 공공 보유 데이터의 존재 여부 및 스키마 실시간 탐색
   - 부처 간 공유 요청 시 특별한 사유가 없는 한 제공 의무화
3. **가명정보 결합 전문기관 활성화**:
   - 개인정보보호법 기반 안전한 가명처리 후 공공-민간 데이터 융합 분석 인프라 제공

### Ⅵ. 실무 장애 요인과 극복 방안 (Troubleshooting)

#### 한줄 요약: 부처 간 데이터 칸막이, AI 환각 및 행정 오류, 개인정보 침해를 해결하는 전략

| 장애 요인 | 발생 원인 | 제도적·기술적 극복 대책 |
|:---|:---|:---|
| **부처 간 데이터 칸막이 (Silo)** | 타 부처 제공 시 감사 부담 및 개별 법령(과세정보 비밀유지 등) 충돌 | 데이터기반행정법 책임 면책 조항 강화, 공동활용 데이터 카탈로그 법제화 |
| **AI 행정 오류 및 환각** | 일반 LLM 활용 시 존재하지 않는 법령을 인용하거나 잘못된 복지 산정 | **공공 전용 sLLM 구축 + RAG 기반 법령 검증**, Human-in-the-Loop 최종 승인 의무화 |
| **민감 개인정보 유출** | 대규모 행정 데이터 결합 시 재식별(Re-identification) 위험 | 차분 프라이버시(Differential Privacy), 동형암호 적용, 폐쇄망 AI 인프라 |

### Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 공공 행정에 AI를 도입할 때 가장 경계해야 할 것은 '자동화의 맹신'이다. 민간 서비스의 추천 알고리즘 오류는 단순 불만에 그치지만, 공공 영역의 복지 대상 탈락이나 과세 행정 오류는 헌법상 기본권 침해와 국가 배상 책임으로 직결된다. 따라서 AI는 공무원의 의사결정을 보조(Copilot)하는 도구로 제한하고, 최종 처분권은 반드시 인간 공무원이 행사하는 'Human-in-the-Loop(HITL)'와 '설명 가능한 AI(XAI)' 거버넌스가 법제화되어야 한다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 전통 데이터 행정과의 대조 다이어그램 및 4단 참조 아키텍처를 제시하겠다. 2교시 25점형이라면 위기 가구 선제 발굴 파이프라인 실사례를 도식화하고, 공공 폐쇄망(G-Cloud) 기반 국산 sLLM 구축 전략과 함께 부처 간 데이터 칸막이 해소를 위한 제도적 면책 조항, 그리고 AI 윤리 및 프라이버시 보호(가명정보 결합, 차분 프라이버시) 체계를 제언에 강조하겠다.

### 실전 답안용 기술사적 제언

- **판정 (현행 한계)**: 상용 글로벌 퍼블릭 AI 호출 시 국가 안보 및 민감 행정정보 유출 위험이 존재하며, 범정부 부처 간 데이터 사일로와 감사 부담으로 인해 기관 간 데이터 연계율이 저조함.
- **대응 (개선 방안)**: 국가정보자원관리원 G-Cloud 내 공공 전용 소형 파운데이션 모델(sLLM)과 RAG 파이프라인을 온프레미스로 구축하고, 공공데이터 연계에 대한 공무원 면책권 법제화 및 차분 프라이버시 기반 가명정보 결합 허브 운영.
- **검증 (검증 기준)**: 법령 인용 환각률 0% 달성(RAG 팩트체킹), 공공 서비스 응답 정확도 95% 이상 검증, 외부망 유출 차단(Air-Gapped) 보안 감사 통과.
- **효과 (실행 효과)**: 복지 사각지대 발굴 기간 90% 단축, 공무원 단순 행정문서 작성 시간 50% 절감, 국민 체감형 선제 공공서비스 만족도 90% 이상 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">현행 한계</div>
    <div class="itpe-flow-step__content">부처 간 데이터 칸막이, 퍼블릭 AI 활용 시 민감 개인정보 유출 위험</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">개선 방안</div>
    <div class="itpe-flow-step__content">공공 폐쇄망 sLLM + RAG 도입 및 데이터 연계 공무원 면책 법제화</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">검증 기준</div>
    <div class="itpe-flow-step__content">법령 환각 0%, 행정 응답 정확도 95% 이상, 망분리 보안 통제 준수</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__label">실행 효과</div>
    <div class="itpe-flow-step__content">위기 가구 선제 발굴 기간 90% 단축, 행정 공수 50% 절감, 신뢰성 제고</div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 데이터기반행정법 제정 및 디지털플랫폼정부 핵심 아젠다
- **검증 출처**:
  - 행정안전부, "제1차·제2차 데이터기반행정 활성화 기본계획"
  - 디지털플랫폼정부위원회, "디지털플랫폼정부 실현계획(DPG Roadmap)"
---

## 연결 토픽

- 상위 토픽: [006. 데이터 거버넌스 (Data Governance)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/006_data_governance.md)
- 연관 토픽: [008. 데이터 표준화 (Data Standardization)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/008_data_standardization.md), [034. 가명정보 처리 가이드라인](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/034_pseudonymized_data_guidelines_unstructured.md)
