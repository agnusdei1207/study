---
title: "기술수용모델(Technology Acceptance Model)"
author: "Codex"
date: "2026-09-20T19:32:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 조직 변화 및 사용자 수용을 거쳐 기술수용모델로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>조직 변화·사용자 수용</span>
  <strong>기술수용모델(Technology Acceptance Model)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 신기술 수용 여부를 **인지된 용이성(PEOU)**과 **인지된 유용성(PU)**이라는 2대 핵심 신념의 인과 사슬로 설명하는 행동과학 이론
- 메커니즘: 시스템 외생 변수 → 용이성 체감(PEOU) → 유용성 확신(PU) → **행동 의도(Behavioral Intention)** 형성 → **실제 사용(Actual Use)** 정착
- 산출: 수용성 진단 지표 · 사용자 여정 맵 · 직무 적합성 분석서 · 변화관리 가이드라인

<div class="itpe-flow-map" role="img" aria-label="외부 변수에서 인지된 용이성과 유용성을 거쳐 실제 시스템 사용으로 이어지는 TAM 인과 흐름">
  <div class="itpe-flow-node">
    <strong>외부 변수 (External Variables)</strong>
    <small>시스템 품질 · 인터페이스 직관성 · 조직적 교육 지원</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>신념 형성</small></div>
  <div class="itpe-flow-node is-current">
    <strong>2대 핵심 인지 신념</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>용이성</strong><span><span class="itpe-keyword"><strong>PEOU</strong></span> (Perceived Ease of Use: 쓰기 쉽다)</span></div>
      <div class="itpe-flow-branch"><strong>유용성</strong><span><span class="itpe-keyword"><strong>PU</strong></span> (Perceived Usefulness: 일에 도움된다)</span></div>
      <div class="itpe-flow-branch"><strong>상호작용</strong><span>PEOU가 PU를 강화하는 핵심 매개 인자</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>태도 및 의도 형성</small></div>
  <div class="itpe-flow-node">
    <strong>행동 의도 (BI) 및 실제 시스템 사용</strong>
    <small><span class="itpe-keyword"><strong>BI(Behavioral Intention)</strong></span> → 일상 업무 적용 및 정착(Actual Use)</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **TAM(Technology Acceptance Model)**: Fred Davis가 합리적 행위이론(TRA)을 발전시켜 정보기술(IT) 사용자 수용을 설명하기 위해 제안한 모형
- **PU(Perceived Usefulness)**: 시스템을 사용하는 것이 자신의 직무 수행 성과나 생산성을 향상시킬 것이라고 믿는 정도
- **PEOU(Perceived Ease of Use)**: 시스템을 배우고 조작하는 데 육체적·정신적 노력이 최소화될 것이라고 믿는 정도
- **BI(Behavioral Intention)**: 향후 시스템을 지속적이고 자발적으로 사용하겠다는 사용자의 주관적 의지
- **TRA(Theory of Reasoned Action)**: 태도와 주관적 규범이 행동 의도를 결정한다는 아젠(Ajzen)과 피시바인(Fishbein)의 사회심리학 이론
- **TPB(Theory of Planned Behavior)**: TRA에 개인이 행동을 제어할 수 있는 '지각된 행동 통제력'을 추가한 확장 모형
- **UTAUT(Unified Theory of Acceptance and Use of Technology)**: 성과기대, 노력기대, 사회적영향, 촉진조건의 4대 변수를 통합한 최신 기술수용이론

</details>

## 예상문제

> 조직 내 새로운 정보시스템 도입 시 사용자 저항을 최소화하고 채택을 촉진하기 위한 기술수용모델(TAM, Technology Acceptance Model)의 개념, 인과적 구조 및 구성요소, 확장 모델(UTAUT 등)과의 비교, 실무 적용 시 고려사항을 설명하시오. (10점/25점)

## Ⅰ. 사용자 관점의 IT 채택 나침반, 기술수용모델(TAM)의 개요

> 신기술 채택 성패는 기능 수가 아니라 **인지된 용이성(PEOU)**과 **인지된 유용성(PU)**이 형성하는 **행동 의도(BI)**로 결정됨.

- 정의: 사용자가 새로운 정보기술을 채택하는 심리적 태도와 이용 행동을 **인지된 유용성(PU)**과 **인지된 용이성(PEOU)**의 인과 관계로 설명하는 **행동과학 기반 기술 수용 이론**
- 목적: 신규 시스템 도입 시 발생하는 사용자 저항 요인을 과학적으로 진단하고, UI/UX 개선 및 체계적 변화관리를 통해 **실제 시스템 사용(Actual Use)**을 극대화

## Ⅱ. TAM 인과 구조 및 4단계 수용 촉진 방법론

> 외부 변수가 용이성을 자극하고, 용이성이 유용성을 강화하여 행동 의도와 실제 사용으로 이어지는 인과 파이프라인을 구축함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="기술수용모델 4단계 사용자 수용 촉진 프로세스">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 외부 변수 최적화 (External Variables)</strong></span>
    <small>사용자 중심 디자인(UCD) · 응답 속도 최적화 · 단일 인증(SSO)<br />→ UI/UX 설계 명세서 · 접근성 가이드라인</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 인지된 용이성 확보 (PEOU 제고)</strong></span>
    <small>직관적 온보딩 튜토리얼 · 마이크로 러닝 · 업무 템플릿 기본 제공<br />→ 사용성 평가 보고서 · PEOU 지수 측정</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 인지된 유용성 실증 (PU 확증)</strong></span>
    <small>반복 수작업 자동화 전후 비교 · 조기 성과(Quick-Win) 지표 가시화<br />→ 생산성 향상 대시보드 · ROI 실증 보고서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 행동 의도(BI) 및 실제 사용 정착 (Actual Use)</strong></span>
    <small>사내 챔피언 육성 · 동료 학습 · 부서별 활용도 인센티브 연계<br />→ 실제 시스템 가동률(Actual Use) 95% 달성</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>인과 연계</strong></span> · PEOU(용이성) ↔ PU(유용성) ↔ BI(의도) ↔ Actual Use(정착) 선순환 추적</div>

## Ⅲ. TAM 핵심 구성요소 및 이론적 발전 계보

> 합리적 행위이론(TRA)에서 출발하여 IT 환경에 특화된 TAM을 거쳐 포괄적 요인을 아우르는 UTAUT로 발전함.

### 1. TAM 5대 핵심 구성요소

| 구성요소 | 영문 명칭 | 개념 정의 | 역할 및 영향 경로 |
|---|---|---|---|
| **외부 변수** | External Variables | 시스템 디자인, 인터페이스 품질, 사용자 교육, 조직적 지원 | PEOU와 PU를 결정하는 선행 외생 요인 |
| **인지된 용이성** | **PEOU(Perceived Ease of Use)** | 시스템 사용에 육체적·정신적 노력이 들지 않는다고 믿는 정도 | **PU를 촉진**하고 사용 태도 형성에 긍정적 기여 |
| **인지된 유용성** | **PU(Perceived Usefulness)** | 시스템 사용이 직무 성과와 생산성을 높여줄 것이라고 믿는 정도 | **행동 의도(BI)에 가장 직접적이고 결정적인 영향** |
| **행동 의도** | **BI(Behavioral Intention)** | 향후 시스템을 지속적·능동적으로 사용하겠다는 주관적 의지 | 실제 시스템 사용을 직접 유발하는 최종 관문 |
| **실제 사용** | Actual System Use | 실제 업무 현장에서의 시스템 로그인 빈도, 체류 시간, 기능 활용도 | 프로젝트의 최종 비즈니스 가치 실현 상태 |

### 2. 기술수용 관련 주요 이론 비교 (TRA vs TPB vs TAM vs UTAUT)

| 비교 항목 | 합리적 행위이론 (TRA) | 계획된 행동이론 (TPB) | 기술수용모델 (TAM) | 통합기술수용이론 (UTAUT) |
|---|---|---|---|---|
| **제안자 및 연도** | Fishbein & Ajzen (1975) | Ajzen (1985) | Davis (1989) | Venkatesh et al. (2003) |
| **적용 도메인** | 일반 인간 행동 심리학 | 행동 통제가 제한된 환경 | **정보기술(IT) 및 IS 수용** | 기업 및 공공 IT 통합 수용 |
| **핵심 독립/매개 변수**| 태도, 주관적 규범 | 태도, 주관적 규범, 지각된 행동통제 | **인지된 용이성(PEOU), 인지된 유용성(PU)** | 성과기대, 노력기대, 사회적영향, 촉진조건 |
| **조절 변수 유무** | 없음 | 없음 | 없음 | 성별, 연령, 경험, 자발성 |
| **설명력 ($R^2$)** | 약 30~40% | 약 40% | 약 40~50% | **약 70% 수준 (가장 강력함)** |

## Ⅳ. 실무 적용 시 주요 왜곡 요인과 통제 대책

> 고기능을 구현했음에도 현업이 외면하는 현상을 타파하기 위해 UX 직관성과 직무 성과 연계를 통제해야 함.

| 문제점 | 발생 원인 | 공학적·관리적 통제 대책 | 기대 효과 |
|---|---|---|---|
| **고기능 구현 후 현업 외면** | 개발자 관점의 복잡한 UI 구성으로 **PEOU** 급락 | 노코드 템플릿 제공, 인라인 툴팁, 최소 클릭(3-Click) 설계 | 진입 장벽 제거 및 초기 이탈 방지 |
| **기존 워크플로우와의 괴리** | 현업 업무 흐름을 무시한 프로세스 강요로 **PU** 미흡 | 부서별 핵심 페인포인트 기반 맞춤형 Use Case 사전 정의 | 직무 직접 기여도 체감 및 유용성 극대화 |
| **신기술(AI) 보안 거부감** | 데이터 유출 및 환각에 대한 두려움으로 심리적 저항 | 기업 전용 프라이빗 테넌트 구축 및 보안·윤리 가이드라인 배포 | 심리적 안전감 확보 및 자발적 채택 유도 |

## Ⅴ. 성공적 신기술 안착을 위한 기술사적 제언

> 시스템 릴리즈 단계에 수용성 품질 게이트를 두고 사내 챔피언 기반 전파 체계를 가동해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 아무리 막대한 예산을 투입한 차세대 AI 시스템이라도 현업 사용자가 로그인하지 않으면 그 가치는 0임. TAM의 본질은 '용이성(PEOU)은 유용성(PU)으로 진입하는 문턱을 낮추는 수단'이며, 최종 안착을 결정하는 본질은 '내 업무 성과가 진짜 올라가는가(PU)'에 있음.
- 나라면: 시스템 오픈 전 파일럿 단계에서 'TAM 기반 사용자 수용성 진단'을 실시하여, PEOU 또는 PU 점수가 80점 미만인 기능은 배포를 차단(Quality Gate)하고, 부서별 '변화관리 챔피언'을 지정해 동료 학습(Peer Learning)을 통한 사회적 영향을 극대화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 기능 개발 완료 중심에서 사용자 수용성 검증 중심의 오픈 판정으로 전환
- 대안: **TAM 기반 릴리즈 Quality Gate** 및 부서별 변화관리 챔피언 제도 도입
- 검증: 파일럿 단계 PEOU/PU 지수 85점 이상 달성 · 3개월 내 주간 활성 사용자(WAU) 90%
- 효과: 사용자 저항 사전 해소 · 신규 시스템 조기 안착 및 IT 투자 효과(ROI) 실현

<div class="itpe-pipeline is-vertical" role="img" aria-label="TAM 기반 사용자 수용성 제고 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>개발 기능 납기만 통제 · 현업 UI 조작 불편 및 업무 불일치로 외면</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>TAM 설문 기반 배포 Quality Gate + 부서별 변화관리 챔피언 육성</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>PEOU/PU 점수 85점 이상 검증 · 조기 성과(Quick-Win) 지표 시각화</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>사용자 거부감 극복 · 시스템 조기 정착 및 IT 투자 ROI 극대화</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 정보기술 채택 행동을 **인지된 용이성(PEOU)**과 **인지된 유용성(PU)**의 2대 핵심 신념을 매개로 설명하는 **행동과학 기반 기술 수용 이론**
- 목적: 신규 시스템 도입 시 발생하는 현업 저항을 최소화하고 자발적 **실제 시스템 사용(Actual Use)**을 유도

### 2. 구성체계 및 인과 메커니즘

<div class="itpe-pipeline is-vertical" role="img" aria-label="TAM 인과 메커니즘 요약">
  <div class="itpe-pipeline-node"><strong>외부 변수</strong><small>시스템 품질 · 조직 지원</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>PEOU (인지된 용이성)</strong><small>학습 노력 최소화 (쓰기 편하다)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>PU (인지된 유용성)</strong><small>직무 성과·생산성 향상 (도움이 된다)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>BI & Actual Use</strong><small>행동 의도 형성 → 실제 시스템 사용 정착</small></div>
</div>

### 3. 핵심 통제

- **2대 핵심 신념**: PEOU가 PU를 견인하며, 최종 사용 의도는 업무 직접 기여도인 PU가 결정
- **UTAUT 확장 통제**: 성과기대, 노력기대 외에 조직적 촉진조건과 사회적 영향력을 함께 관리

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 1교시: 신기술 수용을 설명하는 기술수용모델(TAM)의 개념 및 구성요소
- [Fred Davis(1989), Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology, MIS Quarterly](https://misq.org)
- [Venkatesh et al.(2003), User Acceptance of Information Technology: Toward a Unified View (UTAUT)](https://misq.org)

## 학습 체크

- [ ] 인지된 유용성(PU)과 인지된 용이성(PEOU)의 개념 및 상호 인과관계를 설명할 수 있는가?
- [ ] TAM의 발전 계보(TRA → TPB → TAM → UTAUT)의 차이점을 설명할 수 있는가?
- [ ] 신규 생성형 AI 시스템 도입 시 TAM을 활용한 실무 변화관리 전략을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [과업심의(과업변경·사업기간 적정성)](./091_public_sw_cost_and_scope_change_criteria.md)
- 연관 토픽: [디자인 씽킹](./047_design_thinking.md), [TAM-SAM-SOM](./089_tam_sam_som.md)
- 다음 토픽: [소프트웨어산업진흥법 하도급 구조](./097_software_industry_subcontracting_structure.md)
