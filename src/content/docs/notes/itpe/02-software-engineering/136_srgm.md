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

### SRGM 2대 대표 모델의 누적 결함 곡선

```text
+-------------------------------------------------------------------------+
|                  SRGM 대표 모델 누적 결함 발견 곡선 비교                |
+-------------------------------------------------------------------------+
|  누적 결함 수 (m(t))                                                    |
|     ▲                                    [ 총 잠재 결함 수 a ]           |
|     ├ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -     |
|     │                                 _.-''''' (지수형: G-O 모델)       |
|     │                          _.-''''                                  |
|     │                    _.-'''         _.-'''' (S자형: Yamada 모델)    |
|     │               _.-''          _.-''                                |
|     │          _.-''          _.-'' (결함 급증 구간)                    |
|     │     _.-''          _.-''                                          |
|     │_.-''          _.-'' (초기 학습 구간)                              |
|     └──────────┴────────────────────────────────────────────────▶       |
|     0          t1 (학습 기간)                          시간 (t)         |
|                                                                         |
|  * 출시 판단 시점: 곡선의 기울기(결함 발견율)가 0에 수렴하여 수평선에  |
|                   도달했을 때가 공학적인 최적의 테스트 종료 시점임       |
+-------------------------------------------------------------------------+
```

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

## 5. 참고 및 연계 학습

- [테스트 커버리지(Test Coverage)](./118_test_coverage.md)
- [회귀 테스팅(Regression Test)](./061_regression_test.md)
- [소프트웨어 품질 비용(COQ)](./150_software_quality_cost.md)
- [소프트웨어 안전성 진단 가이드라인](./137_sw_safety_diagnosis_guide.md)
