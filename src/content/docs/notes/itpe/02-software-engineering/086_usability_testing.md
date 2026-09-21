---
title: "사용성 평가 및 사용성 테스트(Usability Testing)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
date: "2026-09-20T22:00:00+09:00"
lastmod: "2026-09-20T22:00:00+09:00"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

> **소프트웨어공학 > 요구분석 및 UI/UX > 사용성 평가 및 사용성 테스트(Usability Testing)**

---

## 1. 큰 그림 및 30초 인출 공식

```
               [ ISO 9241-11 사용성(Usability) 측정 체계 ]
  ┌────────────────────────────────────────────────────────┐
  │ 1. 효과성 (Effectiveness) : 과업 완수 성공률 및 정확도 │
  │ 2. 효율성 (Efficiency)    : 소요 시간 및 투입 자원 대비│
  │ 3. 만족도 (Satisfaction)  : 주관적 편의성 및 수용도   │
  └────────────────────────────────────────────────────────┘
```

> **30초 인출 공식 (키워드 체인)**:  
> **ISO 9241-11** ➔ **효과성·효율성·만족도** ➔ **닐슨 5명 법칙 (85% 결함 발견)** ➔ **Think-Aloud (발성 사고법)** ➔ **휴리스틱 vs 실험실 UT vs A/B 테스트** ➔ **지속적 UX 엔지니어링**

- **본질**: **사용성 테스트(UT)**는 "내 눈엔 직관적인데 사용자는 왜 못 찾지?"라는 개발자·기획자의 주관적 착각을 깨기 위해, **실제 사용자 5명을 데려다 과업을 시켜보고 어디서 헤매고 이탈하는지를 객관적으로 관찰·측정하는 UX 검증 활동**
- **메커니즘**: 대표 과업 시나리오 부여 ➔ 사용자 발성 사고(Think-Aloud) 및 조작 행동 관찰 ➔ 효과성(완수율)·효율성(시간)·만족도(SUS) 정량 측정 ➔ 병목 UI 개선
- **산출물**: 과업 완수 소요시간/오류율 측정표 · SUS 설문 점수표 · UI 병목 구간 개선 백로그

---

## 2. 핵심 용어 정리

| 용어 | 영문 표기 | 핵심 정의 및 설명 |
|---|---|---|
| **사용성 테스트** | Usability Testing (UT) | 대표 사용자가 실제 제품이나 프로토타입으로 정해진 과업을 수행하게 하고 이를 관찰·기록하여 문제점을 찾는 기법 |
| **ISO 9241-11** | Usability Definition Standard | 사용성을 효과성(Effectiveness), 효율성(Efficiency), 만족도(Satisfaction)의 3대 속성으로 정의한 국제표준 |
| **효과성** | Effectiveness | 사용자가 명시된 목표 과업을 얼마나 정확하고 완전하게 달성했는지를 나타내는 척도(완수율, 오류율) |
| **효율성** | Efficiency | 목표를 달성하기 위해 투입된 자원(시간, 클릭 수, 인지적 노력) 대비 산출 성과를 나타내는 척도 |
| **만족도** | Satisfaction | 시스템을 사용하는 과정 및 결과에 대해 사용자가 주관적으로 느끼는 편안함과 긍정적 수용 태도 |
| **발성 사고법** | Think-Aloud Protocol | 사용자가 과업을 수행하면서 머릿속에 떠오르는 생각과 감정을 소리 내어 말하게 하여 무의식적 인지 과정을 파악하는 기법 |
| **닐슨 10대 휴리스틱** | Nielsen's 10 Heuristics | UI/UX 전문가가 사용성 결함을 신속하게 사전 스크리닝하기 위해 준수해야 할 10가지 보편적 설계 원칙 |
| **SUS** | System Usability Scale | 10개 문항의 리커트 척도 설문 조사를 통해 사용성을 0~100점 점수로 정량 환산하는 표준화 설문 도구 |
| **A/B 테스트** | A/B Testing | 두 가지 이상의 인터페이스 시안을 실제 트래픽에 무작위 노출하여 정량적 전환율(CVR) 지표를 비교 검증하는 기법 |
| **닐슨 5명 법칙** | Nielsen's Rule of 5 | 단 5명의 대표 사용자만으로 전체 사용성 문제의 약 85%를 조기에 발견할 수 있다는 비용효율성 경험 법칙 |

---

## 3. 25점형 답안 프레임워크

### Ⅰ. 사용성 평가 및 사용성 테스트의 개요

#### 1. 사용성 평가의 정의 및 필요성
- **정의**: 특정 사용자가 특정 사용 환경에서 시스템을 이용하여 정해진 목표를 얼마나 효과적, 효율적, 만족스럽게 달성할 수 있는지를 과학적으로 측정·개선하는 공학적 평가 체계(ISO 9241-11).
- **필요성**:
  - **사용자 이탈 방지 및 전환율(CVR) 제고**: 복잡한 인터페이스로 인한 인지적 마찰(Friction) 제거.
  - **재작업 비용의 조기 차단**: 요구사항 및 프로토타입 단계에서 5명 피험자 테스트로 결함의 85% 사전 식별.
  - **데이터 주도 의사결정**: 이해관계자 간의 주관적 취향 다툼을 배제하고 완수 시간과 SUS 실측 데이터로 UI 개편.

```
   [사용자 관찰 및 과업 수행]            [ISO 9241-11 3대 측정]           [데이터 기반 UI 개선]
 ┌───────────────────────────┐         ┌───────────────────────────┐      ┌───────────────────────────┐
 │ 대표 사용자 5명 선발      │ ──────▶ │ 효과성 (과업 완수율)      │ ───▶ │ 인지 병목 구간 제거       │
 │ 대표 과업(Task) 시나리오   │         │ 효율성 (소요 시간/클릭 수)│      │ 최적 클릭 경로 단축       │
 │ Think-Aloud 발성 사고 녹화 │         │ 만족도 (SUS 표준 점수)    │      │ 전환율(CVR) 극대화        │
 └───────────────────────────┘         └───────────────────────────┘      └───────────────────────────┘
```

---

### Ⅱ. ISO 9241-11 사용성 측정 체계 및 정량 지표

#### 1. 사용성 평가 3대 품질 속성 및 측정 프레임워크

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="220" style="background: var(--vp-c-bg-alt); border: 1px solid var(--vp-c-border); border-radius: 8px;">
  <defs>
    <marker id="ut-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="var(--vp-c-brand)" />
    </marker>
  </defs>

  <!-- Title Header -->
  <rect x="15" y="10" width="490" height="24" rx="4" fill="var(--vp-c-bg)" stroke="var(--vp-c-border)" />
  <text x="260" y="26" font-size="10.5" font-weight="700" fill="var(--vp-c-brand)" text-anchor="middle">ISO 9241-11 사용성 3대 품질 속성 및 측정 프레임워크</text>

  <!-- Left: Context of Use -->
  <rect x="15" y="42" width="115" height="125" rx="5" fill="var(--vp-c-bg)" stroke="var(--vp-c-border)" stroke-width="1.2" />
  <text x="72" y="58" font-size="9" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">사용 맥락 (Context)</text>
  <line x1="25" y1="64" x2="120" y2="64" stroke="var(--vp-c-border)" stroke-dasharray="2 2" />
  <text x="72" y="80" font-size="8" fill="var(--vp-c-brand)" text-anchor="middle">타깃 사용자 프로필</text>
  <text x="72" y="98" font-size="8" fill="var(--vp-c-text-2)" text-anchor="middle">대표 과업 시나리오</text>
  <text x="72" y="116" font-size="8" fill="var(--vp-c-text-2)" text-anchor="middle">사용 환경 (기기/네트워크)</text>
  <text x="72" y="140" font-size="7.5" fill="#e06c75" text-anchor="middle">Think-Aloud 발성 관찰</text>

  <!-- Arrow Left -> Center -->
  <line x1="130" y1="104" x2="148" y2="104" stroke="var(--vp-c-brand)" stroke-width="1.8" marker-end="url(#ut-arrow)" />

  <!-- Center: 3 Quality Attributes Matrix -->
  <!-- Col 1: Effectiveness -->
  <rect x="152" y="42" width="110" height="125" rx="5" fill="var(--vp-c-bg)" stroke="var(--vp-c-brand)" stroke-width="1.2" />
  <text x="207" y="58" font-size="9" font-weight="700" fill="var(--vp-c-brand)" text-anchor="middle">1. 효과성 (완수)</text>
  <line x1="160" y1="64" x2="254" y2="64" stroke="var(--vp-c-border)" stroke-dasharray="2 2" />
  <text x="207" y="80" font-size="8" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">과업 완료율 (%)</text>
  <text x="207" y="94" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">성공 참가자/전체</text>
  <text x="207" y="115" font-size="8" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">오류 발생률 (건)</text>
  <text x="207" y="129" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">조작 실수 및 역행</text>
  <text x="207" y="152" font-size="7.5" fill="#10b981" text-anchor="middle">목표치: 완료율 &gt; 90%</text>

  <!-- Col 2: Efficiency -->
  <rect x="268" y="42" width="110" height="125" rx="5" fill="var(--vp-c-bg)" stroke="var(--vp-c-brand)" stroke-width="1.2" />
  <text x="323" y="58" font-size="9" font-weight="700" fill="var(--vp-c-brand)" text-anchor="middle">2. 효율성 (자원)</text>
  <line x1="276" y1="64" x2="370" y2="64" stroke="var(--vp-c-border)" stroke-dasharray="2 2" />
  <text x="323" y="80" font-size="8" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">과업 소요 시간 (초)</text>
  <text x="323" y="94" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">시작부터 완료까지</text>
  <text x="323" y="115" font-size="8" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">상대적 효율성</text>
  <text x="323" y="129" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">최적 클릭/실제 클릭</text>
  <text x="323" y="152" font-size="7.5" fill="#10b981" text-anchor="middle">목표치: 소요시간 -30%</text>

  <!-- Col 3: Satisfaction -->
  <rect x="384" y="42" width="120" height="125" rx="5" fill="var(--vp-c-bg)" stroke="var(--vp-c-brand)" stroke-width="1.2" />
  <text x="444" y="58" font-size="9" font-weight="700" fill="var(--vp-c-brand)" text-anchor="middle">3. 만족도 (수용성)</text>
  <line x1="392" y1="64" x2="496" y2="64" stroke="var(--vp-c-border)" stroke-dasharray="2 2" />
  <text x="444" y="80" font-size="8" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">SUS 표준 척도</text>
  <text x="444" y="94" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">10개 문항 (0~100점)</text>
  <text x="444" y="115" font-size="8" font-weight="700" fill="var(--vp-c-text-1)" text-anchor="middle">NPS 추천 점수</text>
  <text x="444" y="129" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">추천 의향 순수 추천율</text>
  <text x="444" y="152" font-size="7.5" fill="#10b981" text-anchor="middle">목표치: SUS &gt; 68점</text>

  <!-- Bottom Result Bar -->
  <rect x="15" y="176" width="490" height="34" rx="4" fill="var(--vp-c-bg)" stroke="#10b981" stroke-width="1.2" />
  <text x="260" y="191" font-size="8.5" font-weight="700" fill="#10b981" text-anchor="middle">통합 분석: 정량 지표 + Think-Aloud 발성 피드백 ➔ UI 인지 마찰 제거</text>
  <text x="260" y="203" font-size="7.5" fill="var(--vp-c-text-2)" text-anchor="middle">닐슨 5명 법칙: 5명의 테스트로 전체 사용성 문제 85% 조기 색출</text>
</svg>
</div>

#### 2. 핵심 측정 지표 상세
| 품질 속성 | 측정 지표 (Metrics) | 계산 방식 및 측정 메커니즘 | 목표 기준치 예시 |
|---|---|---|---|
| **효과성** | **과업 완료율** (Completion Rate) | (성공 완료 사용자 수 / 전체 참가자 수) $\times$ 100 | 핵심 과업 90% 이상 |
| | **오류 발생률** (Error Rate) | 과업 수행 중 발생한 오동작, 클릭 미스, 재시도 횟수 | 과업당 0.5회 미만 |
| **효율성** | **과업 소요 시간** (Time on Task) | 과업 시작부터 완료까지 실측된 초(sec) 단위 시간 | 기존 버전 대비 30% 단축 |
| | **상대적 효율성** (Relative Efficiency) | 최적 이상적 경로 클릭 수 / 실제 사용자의 클릭 수 | 1.2배 이내 유지 |
| **만족도** | **SUS 척도 점수** (System Usability Scale) | 10개 문항의 5점 척도 설문 값을 0~100점으로 환산 | 68점 이상 (우수 등급) |
| | **NPS 점수** (Net Promoter Score) | 추천 의향 10점 척도 (추천자 비율 - 비추천자 비율) | 양수(+) 이상 유지 |

---

### Ⅲ. 사용성 평가 방법론 비교 (휴리스틱 vs 실험실 UT vs A/B 테스트)

| 비교 항목 | 휴리스틱 평가 (Heuristic) | 실험실 사용성 테스트 (UT) | A/B 테스트 (A/B Testing) |
|---|---|---|---|
| **평가 주체** | **UI/UX 전문가 (3~5명)** | **실제 엔드 유저 (5명 내외)** | **실서비스 접속 전 사용자 (대규모)** |
| **수행 시점** | 기획, 와이어프레임 초기 단계 | 프로토타입, MVP 개발 단계 | 상용 서버 배포 후 운영 단계 |
| **핵심 기법** | 닐슨 10대 가이드라인 체크리스트 | **발성 사고법(Think-Aloud)**, 행동 관찰 | 무작위 트래픽 분할, 통계적 유의성 검정 |
| **수집 데이터**| 전문가 관점의 잠재 결함 목록 | 과업 성공률, 완수 시간, 정성 피드백 | 클릭률(CTR), 전환율(CVR), 이탈률 |
| **비용 및 기간**| **매우 저렴, 1~2일 내 신속 완료** | 피험자 섭외 비용, 1~2주 소요 | 대규모 트래픽 확보 및 인프라 필요 |

---

### Ⅳ. 사용성 테스트 실무 적용 시 3대 위험 및 대응 전략

| 위험 | 대책 | 효과 |
|---|---|---|
| **주관적 취향 논쟁으로 인한 의사결정 파행** | ISO 9241-11 기반 정량 지표(완수율, 시간, SUS) 측정 프레임워크 의무화 | 개선안 우선순위 합의 기간 3주에서 1일로 단축 |
| **대면 실험실 환경의 관찰자 의식 왜곡(호손 효과)** | 비동기 원격 UT 도구(Maze 등) 및 실제 프로덕션 히트맵 데이터 교차 분석 | 자연스러운 실사용 조작 행동 데이터 100% 확보 |
| **출시 직전 1회성 검사로 인한 재작업 비용 폭증** | Figma 프로토타입 기반 스프린트별 5명 마이크로 UT 정례화 | 출시 전 중대 사용성 결함 85% 사전 제거 |

---

### Ⅴ. 결론: Lean UX와 데이터 주도 지속적 사용성 엔지니어링

### 학습자 통찰 메모 — 답안 밖

```text
[핵심 통찰]
소프트웨어 엔지니어링에서 기능적 버그는 단위 테스트와 정적 분석으로 완벽히 통제할 수 있지만,
"사용자가 화면을 보고 무엇을 눌러야 할지 몰라 이탈하는 사용성 결함"은 오직 사람을 통해서만 발견된다.
과거의 사용성 평가는 수천만 원짜리 일면경 실험실과 수개월의 리서치를 요구하여 무거운 관료주의로 전락했으나,
현대의 사용성 공학은 "Figma 프로토타입 5명 마이크로 UT ➔ 출시 후 A/B 테스트 ➔ 프로덕트 분석"으로 이어지는 Lean UX 루프를 탄다.
기술사 답안에서는 ISO 9241-11의 3대 정량 척도(효과성, 효율성, 만족도)를 정확히 명시하고,
HiPPO(최고 직급자의 주관적 취향)를 배제하는 데이터 주도 의사결정 체계를 결론에서 강력히 제언해야 한다.

[나라면 이렇게 쓴다]
1단락: ISO 9241-11 기반 사용성 정의 및 인지 마찰 제거 필요성 제시.
2단락: 3대 속성(효과성, 효율성, 만족도)과 측정 지표 상세, 휴리스틱 vs UT vs A/B 테스트 비교표.
3단락: 닐슨 5명 법칙 기반의 Lean UX 파이프라인과 프로덕션 A/B 테스트 연계 거버넌스 제언.
```

### 실전 답안용 기술사적 제언

- **판정 기준**: 신규 기능 릴리스 전, 대표 과업 성공률이 85% 미만이거나 SUS 점수가 68점 미만인 경우, 프로덕션 배포를 중단하고 인터페이스 재설계를 결정해야 함.
- **대응 방안**: 스프린트마다 거대한 테스트베드를 꾸리는 대신, **Figma 프로토타입 단계에서 5명의 대표 사용자를 대상으로 30분 단위의 마이크로 발성사고(Think-Aloud) UT**를 일상화해야 함.
- **검증 체계**: 배포 이후에는 무작위 트래픽 50:50 분할 기반의 **A/B 테스트와 히트맵/세션 리플레이 분석 도구**를 파이프라인에 연동하여 통계적 유의성(p-value < 0.05)을 지속 검증해야 함.
- **기대 효과**: UI 개편에 따른 개발 재작업 비용을 70% 절감하고, 사용자 이탈률을 40% 이상 개선하여 서비스 전환율(CVR) 극대화를 달성함.

<div style="margin: 1rem 0; padding: 0.8rem 1rem; background: var(--vp-c-bg-alt); border-left: 4px solid var(--vp-c-brand); border-radius: 4px; font-size: 0.88rem; line-height: 1.6;">
<strong>사용성 엔지니어링 파이프라인</strong>: <code>프로토타입 5명 UT</code> ➔ <code>ISO 3대 속성 실측</code> ➔ <code>인지 마찰 제거</code> ➔ <code>A/B 테스트 배포</code> ➔ <code>데이터 기반 CVR 극대화</code>
</div>

---

## 4. 1교시 10점형 대비 핵심 요약

```text
- 정의: 특정 맥락에서 목표 과업의 효과성, 효율성, 만족도를 측정·개선하는 활동 (ISO 9241-11)
- 3대 속성: 효과성 (과업 성공률, 오류율), 효율성 (완수 시간, 클릭 수), 만족도 (SUS 점수, 편의성)
- 닐슨 5명 법칙: 5명의 테스트만으로 사용성 결함의 약 85%를 조기 발견 가능
- 주요 기법: 전문가 휴리스틱(사전 스크리닝), 발성 사고법(Think-Aloud), 라이브 A/B 테스트
```

---

## 5. 기출 분석 및 출제 경향

| 회차 및 교시 | 문제 유형 | 핵심 출제 포인트 |
|---|---|---|
| **제114회 1교시** | 단답형 | 사용성 평가의 3대 속성(효과성, 효율성, 만족도) 및 측정 지표 |
| **제121회 4교시** | 서술형 | 소프트웨어 사용성 테스트(Usability Testing)의 절차 및 휴리스틱 평가와의 비교 분석 |
| **제126회 1교시** | 단답형 | 닐슨의 10대 휴리스틱 원칙과 사용성 테스트에서의 역할 |
| **제132회 2교시** | 서술형 | 애자일 개발 환경에서 Lean UX 및 지속적 사용성 엔지니어링 실천 방안 |

---

## 6. 실전 시험 팁

- **ISO 9241-11 3대 지표 수식 도해**: 답안 2단락에 효과성(성공률), 효율성(완수시간), 만족도(SUS)를 3열 매트릭스로 깔끔하게 도식화할 것.
- **Think-Aloud 키워드 명시**: 사용자 테스트의 핵심 정성 관찰 기법인 '발성 사고법(사용자가 속마음을 말하며 조작)'을 반드시 언급해야 전문성이 부각됨.
- **닐슨 5명 법칙 공식 기재**: $1 - (1-L)^n$ (여기서 $L$은 한 명의 사용자가 발견하는 문제 비율 약 31%) 공식을 가볍게 병기하면 이론적 깊이를 입증할 수 있음.

---

## 7. 연관 토픽 맵

- **선행 토픽**: 요구공학, HCI(Human Computer Interaction)
- **유사/비교 토픽**: 휴리스틱 평가(Heuristic), A/B 테스트, 고객 여정 지도(Customer Journey Map)
- **후속/연계 토픽**: 웹 접근성(KWCAG 2.2), 디자인 시스템, Lean UX, 제품 분석(Product Analytics)
