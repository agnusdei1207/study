---
title: "SW 신뢰성 성장 모델(SRGM)"
category: "02-software-engineering"
tags:
  - "SRGM"
  - "신뢰성성장모델"
  - "NHPP"
  - "Goel-Okumoto"
  - "Yamada"
  - "소프트웨어품질"
date: "2026-09-20"
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 테스팅 및 신뢰성 공학을 거쳐 SRGM으로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>테스팅·신뢰성 공학</span>
  <strong>SW 신뢰성 성장 모델(SRGM)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 테스트 종료 시점을 관리자의 주관적 감이나 납기 일정에 타협하여 조기 출시 후 대규모 운영 장애가 터지는 참사를 방지하기 위해, 테스트 기간 동안 발견·제거된 결함의 시계열 데이터를 수학적 확률 모델(NHPP)에 대입하여 잔존 결함 수와 목표 신뢰도 달성 시점(최적 릴리스 시기)을 과학적으로 예측하는 신뢰성 평가 기법
- 메커니즘: 테스트 결함 데이터(시간/건수) 수집 → 통계 모델 선정(지수형 G-O vs 지연 S자형 Yamada) → 파라미터 추정(MLE) 및 곡선 적합도 검정 → 잔존 결함 및 평균 고장 시간(MTTF) 산출 → 최적 출시 판정
- 산출물: 누적 결함 발견 곡선($m(t)$) · 잔존 결함 추정서 · 목표 신뢰도(MTTF) 달성 평가서

<div class="itpe-flow-map" role="img" aria-label="SRGM 기반 신뢰도 예측 및 최적 릴리스 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 테스트 결함 시계열 데이터 수집</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>데이터</strong><span>일별/주별 테스트 시간($t$) 대비 누적 발견 결함 수($m(t)$) 기록</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: NHPP 수학 모델 피팅 및 모수 추정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>모델</strong><span>Goel-Okumoto(오목 지수형) 또는 Yamada(지연 S자형) 선택 $\rightarrow$ MLE 추정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: 릴리스 신뢰도 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>누적 결함 곡선이 포화 상태에 도달하고 목표 MTTF를 달성했는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (출시 승인)</strong>
      <span>최적 릴리스 시점 도달 $\rightarrow$ 운영 배포 및 상용화 승인</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (테스트 지속)</strong>
      <span>결함 발견율 미포화/잔존 결함 과다 $\rightarrow$ 추가 테스트 기간 확보</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **SRGM(Software Reliability Growth Model)**: 소프트웨어 테스트 과정에서 결함이 발견되고 수정됨에 따라 시스템의 신뢰도가 점진적으로 향상되는 과정을 표현한 통계적 수학 모델
- **NHPP(Non-Homogeneous Poisson Process)**: 단위 시간당 결함 발생률이 일정한 상수가 아니라, 테스트가 진행되고 결함이 제거됨에 따라 점차 감소하는 비동차 포아송 확률 과정
- **Goel-Okumoto 모델**: 테스트 초기부터 결함이 빠르게 발견되다가 시간이 지날수록 발견율이 지수 함수적으로 감소하여 포화되는 오목(Concave) 지수형 모델
- **Yamada S자형 모델**: 테스트 초기에는 테스터의 학습 및 환경 적응으로 결함 발견이 완만하다가, 적응 후 급증한 뒤 최종 포화되는 변곡점을 가진 지연 S자형(Delayed S-shaped) 모델
</details>

## 1. 개요 및 필요성

### 주관적 감에 의한 릴리스와 출시 후 참사

대다수 소프트웨어 프로젝트에서 출시(Release) 시점은 사전에 정해진 납기 일정이나 관리자의 주관적 판단에 의해 졸속 결정된다. 테스트 기간이 끝났다는 이유만으로 결함이 여전히 쏟아지는 상태에서 제품을 시장에 출시하면, 운영 오픈 첫날 시스템 마비, 대규모 리콜, 기업 신뢰도 추락이라는 파국을 맞이한다.

SRGM은 결함 발견 이력을 바탕으로 **"시스템에 잠재된 총 결함 수가 몇 개이며, 현재 몇 %의 결함이 제거되었고, 목표 신뢰도(MTTF)에 도달하려면 테스트를 며칠 더 수행해야 하는가"**를 수학적으로 계산하여, 가장 경제적이고 안전한 **최적 릴리스 시점(Optimal Release Time)**을 제시한다.

### 대표 SRGM 모델 비교 (Goel-Okumoto vs Yamada)

| 구분 | Goel-Okumoto (오목 지수형) | Yamada S-shaped (지연 S자형) |
|---|---|---|
| **곡선 형태** | 오목형 (Concave, $m(t) = a(1 - e^{-bt})$) | S자형 (S-shaped, $m(t) = a(1 - (1 + bt)e^{-bt})$) |
| **초기 결함 발견 속도** | 테스트 초기부터 결함 발견율이 매우 높음 | 테스트 초기에는 발견율이 낮고 완만함 |
| **학습 효과 반영** | **미반영** (테스터가 처음부터 시스템을 완벽히 안다고 가정) | **반영** (테스터의 시스템 학습 곡선 및 환경 적응 기간 고려) |
| **적합한 시스템** | 구조가 단순하거나 테스터가 매우 숙련된 시스템 | **복잡한 대규모 엔터프라이즈 시스템, 신규 도메인** |
| **모수 의미** | $a$: 잠재 결함 총량, $b$: 결함 검출률 | $a$: 잠재 결함 총량, $b$: 결함 검출/격리율 |

## 2. 아키텍처 및 핵심 메커니즘

### 누적 결함 발견 곡선 비교 (G-O vs Yamada)

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <!-- Frame -->
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">SRGM 누적 결함 발견 곡선 ($m(t)$) 및 포화 임계선</text>

    <!-- Axes -->
    <line x1="55" y1="180" x2="480" y2="180" stroke="var(--color-border, #64748b)" stroke-width="1.5"/>
    <line x1="55" y1="180" x2="55" y2="40" stroke="var(--color-border, #64748b)" stroke-width="1.5"/>
    <text x="480" y="195" font-size="7.5" fill="var(--color-text, #334155)">테스트 시간 (t)</text>
    <text x="25" y="45" font-size="7.5" fill="var(--color-text, #334155)">결함 수</text>

    <!-- Asymptote (Total Defects a) -->
    <line x1="55" y1="65" x2="475" y2="65" stroke="#ef4444" stroke-width="1" stroke-dasharray="4,3"/>
    <text x="475" y="62" text-anchor="end" font-size="7" font-weight="bold" fill="#dc2626">잠재 결함 총량 (a)</text>

    <!-- G-O Curve (Concave exponential) -->
    <path d="M 55 180 Q 130 90 460 70" fill="none" stroke="var(--color-primary, #2563eb)" stroke-width="2"/>
    <text x="220" y="90" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">Goel-Okumoto (오목 지수형)</text>

    <!-- Yamada Curve (S-shaped) -->
    <path d="M 55 180 Q 150 178 220 135 T 460 75" fill="none" stroke="#ca8a04" stroke-width="2"/>
    <text x="320" y="140" font-size="7.5" font-weight="bold" fill="#ca8a04">Yamada (지연 S자형)</text>

    <!-- Annotations -->
    <rect x="70" y="135" width="90" height="28" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="115" y="148" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">초기 학습 구간</text>
    <text x="115" y="158" text-anchor="middle" font-size="6.5" fill="#ca8a04">(발견율 완만)</text>

    <!-- Optimal Release Zone -->
    <rect x="400" y="80" width="85" height="40" rx="4" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1"/>
    <text x="442" y="95" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">최적 릴리스</text>
    <text x="442" y="108" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">기울기 0 수렴 구간</text>
  </svg>
</div>

### 비용 최적화 기반 릴리스 판정 모델 구조

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="srgm-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Background Frame -->
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">SRGM 기반 최적 릴리스 판정 4대 프로세스</text>

    <!-- Step 1 -->
    <rect x="15" y="40" width="105" height="95" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="15" y="40" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="67" y="55" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">① 데이터 수집</text>
    <text x="67" y="78" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">테스트 시간 ($t$)</text>
    <text x="67" y="93" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">결함 발견 건수</text>
    <text x="67" y="112" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">[중복 결함 정제]</text>

    <line x1="120" y1="87" x2="138" y2="87" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#srgm-arrow)"/>

    <!-- Step 2 -->
    <rect x="140" y="40" width="105" height="95" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="140" y="40" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="192" y="55" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">② 모수 추정</text>
    <text x="192" y="78" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">NHPP 모델 적합</text>
    <text x="192" y="93" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">최우도추정(MLE)</text>
    <text x="192" y="112" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">[파라미터 a, b 산출]</text>

    <line x1="245" y1="87" x2="263" y2="87" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#srgm-arrow)"/>

    <!-- Step 3 -->
    <rect x="265" y="40" width="110" height="95" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="265" y="40" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="320" y="55" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">③ 신뢰도 계산</text>
    <text x="320" y="78" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">잔존 결함 수 ($a - m$)</text>
    <text x="320" y="93" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">고장률 $\lambda(t)$ / MTTF</text>
    <text x="320" y="112" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-accent, #0284c7)">[목표 신뢰도 검증]</text>

    <line x1="375" y1="87" x2="393" y2="87" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#srgm-arrow)"/>

    <!-- Step 4 -->
    <rect x="395" y="40" width="110" height="95" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.4"/>
    <rect x="395" y="40" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="450" y="55" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">④ 최적 릴리스</text>
    <text x="450" y="78" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">총비용 최소점 ($t^*$)</text>
    <text x="450" y="93" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">테스트비용 vs 장애손실</text>
    <text x="450" y="112" text-anchor="middle" font-size="6.5" font-weight="bold" fill="#16a34a">[출시 최종 승인]</text>

    <!-- Bottom Result Formula -->
    <rect x="15" y="145" width="490" height="35" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="260" y="166" text-anchor="middle" font-size="7.5" fill="var(--color-text, #1e293b)">비용 목적함수: $C(t) = C_1 \cdot t + C_2 \cdot m(t) + C_3 \cdot (a - m(t))$ 의 극솟값 시점 도출</text>
  </svg>
</div>

### SRGM 분석 및 적용 4대 핵심 절차

<div class="itpe-component-grid">
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>① 데이터 수집 및 정제</strong></span>
      <span class="itpe-badge">실측 데이터</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>일별/주별 테스트 투입 시간, 실행 건수, 발견된 결함 건수 로깅</li>
        <li>단순 환경 문제나 중복 결함은 필터링하여 순수 소프트웨어 결함만 추출</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>② 모델 선정 및 모수 추정</strong></span>
      <span class="itpe-badge">수학적 피팅</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>초기 결함 발생 추세에 따라 G-O 지수형 또는 Yamada S자형 모델 선택</li>
        <li>최우도추정법(MLE) 또는 최소제곱법(LSE)을 활용하여 모수 $a, b$ 산출</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>③ 신뢰도 지표 계산</strong></span>
      <span class="itpe-badge">정량 평가</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>잔존 결함 수: 총 결함 추정치($a$) - 현재까지 발견된 결함 수($m(t)$)</li>
        <li>순간 고장률 $\lambda(t)$ 및 평균 고장 시간(MTTF) 수학적 산출</li>
      </ul>
    </div>
  </div>
  <div class="itpe-component-card">
    <div class="itpe-component-header">
      <span class="itpe-keyword"><strong>④ 최적 릴리스 시점 도출</strong></span>
      <span class="itpe-badge">비용 최적화</span>
    </div>
    <div class="itpe-component-body">
      <ul>
        <li>테스트 지속 비용(인건비)과 출시 후 결함 발생 손실 비용의 합 최소화</li>
        <li>목표 신뢰도와 비용 곡선의 교차점에서 공식 배포 승인</li>
      </ul>
    </div>
  </div>
</div>

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 납기에 쫓겨 결함이 지속적으로 발생하는 상태에서 임의 릴리스 후 대규모 장애 및 리콜 발생 | SRGM(Yamada 모델) 기반 잔존 결함률 및 목표 MTTF 충족 여부를 릴리스 필수 조건으로 지정 | 치명적 잔존 결함 사전 차단 및 상용 안정성 확보 |
| 결함 수정 과정에서 새로운 결함이 추가 유입되어 기존 모델의 예측 오차가 커지는 현상 | 완전 디버깅 가정 대신 신규 결함 유입률을 반영하는 '불완전 디버깅(Imperfect Debugging)' 모델 적용 | 모델 신뢰도 보정 및 실제 운영 결함 예측 정확도 향상 |
| 수작업 통계 분석 지연으로 개발팀이 실시간 신뢰도 지표를 공유받지 못함 | Jira/Git 이슈 트래커의 결함 타임스탬프를 Python 라이브러리와 연동하여 자동 곡선 피팅 대시보드 구축 | 매일 아침 전사 프로젝트 신뢰도 성장 추세 실시간 가시화 |

## 4. 기술사 답안 차별화 포인트

### 불완전 디버깅(Imperfect Debugging) 현실 모델 제시

전통적인 고전 SRGM(G-O 모델 등)의 가장 큰 이론적 취약점은 **"결함을 한 번 고치면 100% 완벽히 제거되며, 새로운 결함이 절대 생기지 않는다(Perfect Debugging)"**는 비현실적 가정이다. 실무에서는 버그 수정 코드의 15~20%에서 사이드 이펙트로 인한 신규 결함이 다시 유입된다. 따라서 결함 수정 시 신규 결함이 생성되는 확률 파라미터를 추가한 **불완전 디버깅 모델**을 언급하고, 회귀 테스트(Regression Test) 자동화와의 결합 필요성을 제시하면 실무 통찰력을 강력히 드러낼 수 있다.

### 총비용 곡선(Cost Curve) 기반 최적 릴리스 결정식 도출

단순히 결함 수만 따지는 것이 아니라, **비용 최적화 모델(Cost Optimization Model)**을 결합하여 설명한다.
$$C(t) = C_1(t) \times t + C_2 \times m(t) + C_3 \times (a - m(t))$$
($C_1$: 단위 시간당 테스트 비용, $C_2$: 테스트 중 결함 수정 비용, $C_3$: 출시 후 장애 처리 비용)
출시 후 결함 수정 비용($C_3$)은 테스트 중 비용($C_2$)의 수십 배에 달하므로, 총비용 $C(t)$를 미분하여 최소가 되는 시점 $t^*$를 도출하는 수리적 접근을 3단락 또는 결론으로 제시한다.

## 5. 결론 및 종합 제언

### 학습자 통찰 메모 — 답안 밖

[핵심 통찰]
SRGM의 가장 강력한 실무 가치는 '테스트를 언제 끝낼 것인가'라는 소프트웨어 프로젝트 최고의 난제에 **주관적 직관이 아닌 객관적 수학 공식**을 제공한다는 점이다. 특히 결함이 줄어들지 않는 초기 학습 단계를 지나 급증 후 포화되는 변곡점을 가진 Yamada 모델은 대규모 엔터프라이즈 프로젝트의 실제 현상을 매우 정밀하게 설명한다.

나라면:
본 시험에서 SRGM이 출제되면, 단순히 G-O와 Yamada 곡선 수식을 암기해 나열하는 데 그치지 않고 **(1) 현실의 버그 재유입을 반영한 불완전 디버깅(Imperfect Debugging) 모델로의 확장, (2) 테스트 인건비와 출시 후 장애 손실액을 절충한 총비용 함수 $C(t)$의 최적 릴리스 시점 수리 모델, (3) CI/CD 파이프라인의 이슈 트래커와 연동된 실시간 품질 게이트(Quality Gate)**의 3단계 실천 로드맵을 3단락에 명쾌하게 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 테스트 종료 예정일 기준 결함 검출률 기울기($dm/dt$)가 임계치 이상이거나 목표 MTTF 미달 시 릴리스 보류
- **대응 방안**: 불완전 디버깅 파라미터를 반영하여 잔존 결함 수를 재추정하고 고위험 모듈 집중 회귀 테스팅 수행
- **검증 체계**: Jira/GitLab 웹훅을 통해 결함 로그를 SRGM 분석 엔진에 실시간 피팅하여 품질 게이트 대시보드 운영
- **기대 효과**: 출시 후 치명적 운영 장애율 70% 감소 및 비용 최소화 기반 최적 릴리스 일정 확정

<div class="itpe-pipeline-container" role="region" aria-label="SRGM 기반 데이터 주도적 품질 게이트 파이프라인">
  <div class="itpe-pipeline-header">
    <span class="itpe-pipeline-title">SRGM 기반 데이터 주도적 품질 게이트 파이프라인</span>
    <span class="itpe-pipeline-badge">품질 거버넌스</span>
  </div>
  <div class="itpe-pipeline-grid">
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">1단계: 실시간 집계</div>
      <div class="itpe-card-title">결함 로그 수집</div>
      <div class="itpe-card-body">테스트 실행 시간 대비 결함 건수 실시간 웹훅 파이프라인 적재</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">2단계: 확률 피팅</div>
      <div class="itpe-card-title">Yamada NHPP 적합</div>
      <div class="itpe-card-body">MLE 기법 기반 잠재 결함 총량($a$) 및 결함 검출률($b$) 실시간 산출</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">3단계: 비용 최적화</div>
      <div class="itpe-card-title">총비용 곡선 도출</div>
      <div class="itpe-card-body">테스트 투입 비용과 출시 후 결함 손실액의 합이 최소가 되는 $t^*$ 산정</div>
    </div>
    <div class="itpe-pipeline-card">
      <div class="itpe-card-badge">4단계: 품질 승인</div>
      <div class="itpe-card-title">릴리스 판정 배포</div>
      <div class="itpe-card-body">목표 MTTF 충족 및 결함 포화 확인 시 운영 배포 승인</div>
    </div>
  </div>
</div>

## 6. 참고 및 연계 학습

- [테스트 커버리지(Test Coverage)](./118_test_coverage.md)
- [회귀 테스팅(Regression Test)](./061_regression_test.md)
- [소프트웨어 품질 비용(COQ)](./150_software_quality_cost.md)
- [소프트웨어 안전성 진단 가이드라인](./137_sw_safety_diagnosis_guide.md)
