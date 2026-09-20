---
title: "디자인 씽킹"
author: "Antigravity"
date: "2026-09-20T19:41:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 문제 해결 방법론을 거쳐 디자인 씽킹으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>사용자 중심 혁신 방법론</span>
  <strong>디자인 씽킹</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **디자인 씽킹(Design Thinking)**은 디자이너의 작업 방식을 차용하여 사용자의 잠재적 결핍(Unmet Needs)을 깊이 공감하고, 발산과 수렴의 반복을 통해 인간 중심의 혁신 솔루션을 도출하는 문제해결 방법론
- 메커니즘: 스탠퍼드 **d.school 5단계(공감·정의·아이디어·시제품·테스트)**와 **더블 다이아몬드(Double Diamond)** 모델의 비선형 반복 피드백 순환
- 산출: 페르소나(Persona) · **고객여정지도(Customer Journey Map)** · POV(Point of View) 명세 · 저충실도 프로토타입(Low-fi Mockup) · UT(Usability Test) 검증서

<div class="itpe-flow-map" role="img" aria-label="디자인 씽킹 5단계 및 비선형 피드백 루프 흐름">
  <div class="itpe-flow-node">
    <strong>사용자 공감 및 관찰</strong>
    <small>현장 인터뷰 · 섀도잉(Shadowing) · 페인포인트 발굴</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>d.school 5단계 반복 체계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>문제 영역</strong><span>Empathize(공감) → Define(정의/POV 도출)</span></div>
      <div class="itpe-flow-branch"><strong>해법 영역</strong><span>Ideate(HMW 질문) → Prototype(신속 시제품) → Test(사용성 검증)</span></div>
      <div class="itpe-flow-branch"><strong>수렴·발산</strong><span><span class="itpe-keyword"><strong>더블 다이아몬드</strong></span> 모델 기반 비선형 피드백 회귀</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>애자일 백로그 전환 및 가치 실현</strong>
    <small>검증된 프로토타입 → 스프린트 에픽·스토리 반영</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **Design Thinking(디자인 씽킹)**: 사용자 경험에 깊이 공감하여 올바른 문제를 정의하고 프로토타이핑을 통해 혁신 대안을 도출하는 인간 중심 문제해결 프레임워크
- **Double Diamond(더블 다이아몬드)**: 문제 발견·정의의 다이아몬드 1과 솔루션 개발·전달의 다이아몬드 2로 구성된 발산과 수렴의 설계 모델
- **Persona(페르소나)**: 사용자의 행동 패턴, 목표, 동기, 고통점을 집약하여 모델링한 대표 가상 인물
- **CJM(Customer Journey Map)**: 고객이 서비스를 이용하며 경험하는 모든 터치포인트의 감정 변화와 불편을 시각화한 지도
- **POV(Point of View)**: "사용자(User)는 인사이트(Insight) 때문에 니즈(Need)가 필요하다" 형태로 문제를 정의하는 관점 진술문
- **HMW(How Might We)**: 문제 정의를 창의적 아이디어 도출로 전환하기 위해 질문 형태로 전환하는 발문 기법
- **Low-fidelity Prototype**: 페이퍼 목업 등 최소 비용으로 핵심 아이디어의 가설만을 검증하기 위한 저충실도 시제품
- **UT(Usability Test)**: 실제 사용자에게 시제품을 사용하게 한 후 수행 과정의 장애와 행동 반응을 관찰·측정하는 평가

</details>

## 예상문제

> 디지털 혁신 환경에서 요구되는 디자인 씽킹(Design Thinking)의 개념, 더블 다이아몬드 모델 기반 5단계 프로세스, 주요 수행 기법 및 실무 적용 시 한계 극복 방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 번호 | 하위 토픽 | 핵심 내용 | 본문 반영 위치 |
|---|---|---|---|
| **01-093** | **디자인 싱킹** | 디자인 씽킹의 표준 국문 표기 차이 동의어이며, 사용자 공감 기반의 d.school 5단계 및 더블 다이아몬드와 동일 체계 | Ⅱ 구성체계 및 Ⅲ 실행 절차 |

## Ⅰ. 인간 중심 혁신의 출발점, 디자인 씽킹의 개요

> 디자인 씽킹은 기술 주도 공급자 마인드를 탈피하여 사용자 결핍을 올바른 문제로 재정의하는 프레임워크이며, 성패는 **POV**의 구체성과 **시제품(Prototype)** 기반의 조기 검증으로 판정함.

- 정의: 디자이너의 감수성과 방식을 적용하여 사용자의 잠재 욕구를 깊이 공감하고, 기술적 실현 가능성과 사업성을 결합하는 **인간 중심 문제해결 방법론(Design Thinking)**
- 목적: 문제 오정의 개발 낭비 방지, **사용자 경험(UX)** 혁신 통한 **비즈니스 가치 창출**

## Ⅱ. 스탠퍼드 d.school 5단계 구성체계 및 방법론

> 공감에서 시작하여 테스트로 끝나지 않고, 피드백에 따라 선행 단계로 유연하게 역행하는 비선형 피드백 루프로 작동함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="디자인 씽킹 d.school 5단계 방법론 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① Empathize (공감)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>사용자 심층 인터뷰, 현장 섀도잉, 미충족 욕구(Unmet Needs) 발굴</span></div>
    <div class="itpe-step-detail"><strong>주요 산출물</strong><span>공감 지도(Empathy Map), 인터뷰 전사록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② Define (정의)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>관찰 데이터 분석, 페르소나 및 고객여정지도(CJM) 구축</span></div>
    <div class="itpe-step-detail"><strong>주요 산출물</strong><span>POV(Point of View) 문제 진술문 확정</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ Ideate (아이디어 도출)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>HMW(How Might We) 질문법, 브레인스토밍, 비판 배제 발산</span></div>
    <div class="itpe-step-detail"><strong>주요 산출물</strong><span>아이디어 우선순위 매트릭스</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ Prototype (시제품 제작)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>손으로 만질 수 있는 빠른 가시화, 저충실도(Low-fi) 제작</span></div>
    <div class="itpe-step-detail"><strong>주요 산출물</strong><span>페이퍼 목업, 클릭형 와이어프레임</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ Test (사용자 테스트)</strong></span>
    <div class="itpe-step-detail"><strong>핵심 활동</strong><span>실사용자 UT 수행, 피드백 수집 및 가설 검증</span></div>
    <div class="itpe-step-detail"><strong>주요 산출물</strong><span>사용성 평가 보고서, 피드백 그리드</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>비선형 회귀 루프</strong></span> · 테스트 결과 가설 기각 시 즉각 문제 정의(Define) 또는 아이디어(Ideate) 단계로 재순환</div>

## Ⅲ. 더블 다이아몬드(Double Diamond) 모델과 3대 성공 축

> '올바른 문제를 찾는 것(다이아몬드 1)'과 '문제를 올바르게 푸는 것(다이아몬드 2)'의 2회 발산·수렴 구조를 이룸.

| 다이아몬드 영역 | 단계 | 사고 방식 | 주요 활동 및 산출물 | 품질 검증 기준 |
|---|---|---|---|---|
| **다이아몬드 1<br>(올바른 문제 찾기)** | **발견 (Discover)** | 발산 (Divergence) | 폭넓은 사용자 관찰, 섀도잉, 극단적 사용자 행동 탐색 | 선입견 없는 데이터 수집 |
| | **정의 (Define)** | 수렴 (Convergence) | 페인포인트 정제, 페르소나, **POV(Point of View)** 도출 | "올바른 문제를 정의했는가?" |
| **다이아몬드 2<br>(올바른 해법 만들기)** | **개발 (Develop)** | 발산 (Divergence) | 다학제 팀 **HMW 질문**, 브레인스토밍, 다양한 대안 탐색 | 비판 없는 아이디어 풍부성 |
| | **전달 (Deliver)** | 수렴 (Convergence) | **저충실도 프로토타입**, 실사용자 UT, 솔루션 확정 | "실제 문제를 해결하는가?" |

- 3대 핵심 성공 축: **Desirability(인간 중심 욕구)** ∩ **Feasibility(기술적 실현성)** ∩ **Viability(사업적 타당성)**의 교집합에서 지속 가능한 혁신이 탄생함.

## Ⅳ. 디자인 씽킹 vs 린 스타트업 vs 애자일 3단계 연계 모델

> 세 방법론은 상호 배타적이지 않으며, 제품 개발 전 수명주기에 걸쳐 순차적·유기적 파이프라인을 형성함.

| 비교 항목 | 디자인 씽킹 (Design Thinking) | 린 스타트업 (Lean Startup) | 애자일 (Agile) |
|---|---|---|---|
| **핵심 질문** | "어떤 문제를 해결해야 하는가?" (**What & Why**) | "사업적으로 지속 가능한가?" (**Viability**) | "어떻게 빠르고 유연하게 구현할 것인가?" (**How**) |
| **방법론 초점** | 고객 공감 및 올바른 문제 정의 | 비즈니스 모델 가설 검증 | 동작하는 소프트웨어의 점진적 인도 |
| **반복 메커니즘** | 발산과 수렴의 비선형 피드백 루프 | **만들기-측정-학습(Build-Measure-Learn)** | **스프린트(Sprint)** 타임박스 반복 개발 |
| **대표 산출물** | 페르소나, 고객여정지도(CJM), 목업 | **최소 기능 제품(MVP)**, 피벗(Pivot) 결정 | 실행 가능한 소프트웨어, 스프린트 백로그 |
| **수명주기 위치** | **문제 탐색 단계** (기획 및 개념화) | **비즈니스 검증 단계** (시장성 확인) | **엔지니어링 구현 단계** (개발 및 배포) |

## Ⅴ. 실무 적용 실패 요인과 공학적 통제 방안

> 일회성 포스트잇 행사에 그치는 형식주의를 극복하고 엔지니어링 백로그와 연계해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **형식적 워크숍 전락** | 도출된 페인포인트를 **Jira 에픽·스토리 백로그**로 필수 연동 | 기획과 실무 개발의 정합성 확보 |
| **문제 정의 건너뛰기** | **POV 승인 게이트웨이(Quality Gate)**를 두어 문제 검증 | 불필요한 기능 개발 낭비 차단 |
| **고충실도 목업 집착** | 페이퍼 목업 등 **저충실도(Low-fi) 프로토타입** 의무화 | 실패 비용 최소화 및 빠른 검증 |
| **다학제 협업 결여** | PO + 디자이너 + **소프트웨어 아키텍트** 공동 스쿼드 운영 | 기술적·사업적으로 실현 가능한 해법 도출 |

## Ⅵ. 삼위일체 파이프라인 구축 중심의 기술사적 제언

> 디자인 씽킹은 독자적인 사일로에 머물지 않고 린 스타트업의 가설 검증과 애자일의 스프린트 배포로 연결될 때 완성됨.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 디자인 씽킹의 성패는 예쁜 포스트잇에 있지 않고, '사용자가 말하지 않은 숨겨진 고통(Pain Point)'을 관찰로 찾아내어 올바른 POV 문장으로 수렴시키는 데 있음. 문제를 잘못 짚으면 아무리 애자일로 기민하게 개발해도 쓸모없는 소프트웨어가 양산됨.
- 나라면: 차세대 시스템 개발 프로세스에서 `Sprint 0 단계에 디자인 씽킹 프로세스 배치 → 저충실도 프로토타입으로 실사용자 UT 3회 통과를 통과 기준으로 지정 → 검증된 프로토타입만 제품 백로그(Product Backlog)로 승격`하는 품질 관문을 수립하겠음.

### 실전 답안용 기술사적 제언

- 판정: 일회성 워크숍 탈피 및 엔지니어링 개발 파이프라인과의 직결
- 대안: **디자인 씽킹(탐색) → 린 스타트업(검증) → 애자일(구현)** 삼위일체 연계 모델
- 검증: **POV 승인율** 100% · UT 기반 사용성 결함 식별률 및 백로그 전환율
- 효과: 요구사항 오정의에 따른 프로젝트 재작업 비용 원천 방지 및 고객 만족 극대화

<div class="itpe-pipeline is-vertical" role="img" aria-label="디자인 씽킹 기반 삼위일체 개발 파이프라인 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제점</strong><span>공급자 중심 개발, 형식적 워크숍 행사, 엔지니어링 백로그와의 단절</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>추진 전략</strong><span>Sprint 0 디자인 씽킹 도입, 저충실도 프로토타입 기반 백로그 승격제</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>관리 지표</strong><span>POV 타당성 검토, 실사용자 UT 통과율, 애자일 스토리 연결성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>최종 효과</strong><span>개발 재작업 비용 절감, 사용자 중심 디지털 서비스 혁신 완성</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **디자인 씽킹(Design Thinking)**은 사용자의 잠재된 미충족 결핍을 공감하여 문제를 올바르게 재정의하고, **프로토타입(Prototype)**과 테스트의 반복을 통해 혁신적 대안을 창출하는 인간 중심 문제해결 방법론
- 목적: 문제 오정의 개발 낭비 차단, **사용자 경험(UX)** 혁신 통한 비즈니스 가치 실현

### 2. 구성체계 및 d.school 5단계

<div class="itpe-pipeline is-vertical" role="img" aria-label="디자인 씽킹 5단계 요약">
  <div class="itpe-pipeline-node">
    <strong>Empathize (공감)</strong>
    <div class="itpe-step-detail"><strong>사용자 관찰</strong><span>인터뷰 및 현장 섀도잉 관찰</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Define (정의)</strong>
    <div class="itpe-step-detail"><strong>문제 재정의</strong><span>페르소나, 고객여정지도(CJM), POV 명세</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Ideate (아이디어)</strong>
    <div class="itpe-step-detail"><strong>창의적 발산</strong><span>HMW 발문 및 브레인스토밍 발산</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Prototype (시제품)</strong>
    <div class="itpe-step-detail"><strong>신속 가시화</strong><span>저충실도(Low-fi) 페이퍼 목업 제작</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Test (사용자 테스트)</strong>
    <div class="itpe-step-detail"><strong>가설 검증</strong><span>실사용자 UT 및 피드백 회귀 루프</span></div>
  </div>
</div>

### 3. 핵심 통제

- **더블 다이아몬드**: 문제 탐색(다이아몬드 1)과 솔루션 개발(다이아몬드 2)의 발산·수렴 통제
- **3대 성공 축**: Desirability(욕구), Feasibility(기술), Viability(사업성)의 교집합 달성

## 출제 이력과 검증 출처

- 제124회 KPC 1교시: 디자인 씽킹(Design Thinking)의 5단계 프로세스와 주요 기법
- [Stanford d.school, An Introduction to Design Thinking Process Guide](https://dschool.stanford.edu)
- [British Design Council, The Double Diamond Design Process](https://www.designcouncil.org.uk)

## 학습 체크

- [ ] 디자인 씽킹의 3대 핵심 축(인간 중심성, 실현 가능성, 사업 타당성)을 설명할 수 있는가?
- [ ] d.school 5단계의 명칭과 각 단계별 주요 산출물을 제시할 수 있는가?
- [ ] 더블 다이아몬드 모델의 발산과 수렴 메커니즘을 도식화할 수 있는가?
- [ ] 디자인 씽킹, 린 스타트업, 애자일의 상호 연계 구조를 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [그로스 해킹](./046_growth_hacking.md)
- 연관 토픽: [애자일 대응 전략](./013_agile_response_strategy.md), [A/B 테스트](./029_ab_testing.md), [MECE](./045_mece.md)
- 다음 토픽: [제안요청서(RFP)](./049_rfp.md)
