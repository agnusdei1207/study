---
title: "중심극한정리 (Central Limit Theorem)"
category: "03-data"
tags:
  - "중심극한정리"
  - "CLT"
  - "대수의법칙"
  - "LLN"
  - "표준오차"
  - "정규근사"
  - "표집분포"
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
extra:
  model: "GPT-6"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 분석에서 통계 추론 및 중심극한정리로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>통계 분석·추론</span>
  <strong>중심극한정리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 모집단의 고유 분포 형태와 무관하게, 표본 크기($n$)가 충분히 크면 독립적으로 추출된 표본평균들의 표집분포가 정규분포($\mathcal{N}(\mu, \sigma^2/n)$)에 수렴한다는 추론통계학의 핵심 정리
- 메커니즘: 임의 모집단($\mu, \sigma^2$) $\rightarrow$ 독립 표본 추출($n \ge 30$) $\rightarrow$ 표본평균 산출 $\rightarrow$ 표준화($Z = (\bar{X} - \mu)/(\sigma/\sqrt{n})$) $\rightarrow$ 표준정규분포 $\mathcal{N}(0, 1)$ 수렴
- 산출물: 표본평균 표집분포 곡선 · 표준오차($SE = \sigma/\sqrt{n}$) 수식 · 정규근사 신뢰구간(CI) · 부트스트랩 교차검증서

<div class="itpe-flow-map" role="img" aria-label="중심극한정리 정규근사 및 추론 타당성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 임의의 모집단 데이터 수집</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>원천</strong><span>균등, 지수, 포아송 등 비정규 분포를 갖는 모집단 (평균 $\mu$, 유한분산 $\sigma^2$)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 독립 표본 무작위 추출 및 표준화</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>추출</strong><span>크기 $n$의 표본평균 $\bar{X}$ 산출 및 $Z = (\bar{X} - \mu) / (\sigma / \sqrt{n})$ 표준화</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: 정규근사 전제조건 및 수렴 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>표본의 독립성(IID)과 유한분산이 보장되며, 표본 크기가 왜도를 극복할 만큼 충분한가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (정규근사 성립)</strong>
      <span>표준정규분포 $\mathcal{N}(0, 1)$ 수렴 $\rightarrow$ z-검정, t-검정 및 95% 신뢰구간 모수 추론 적용</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (중꼬리 / 무한분산 / 소표본)</strong>
      <span>정규근사 배제 $\rightarrow$ 윌콕슨 비모수 검정 또는 부트스트랩(Bootstrap) 재표본추출 전환</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `CLT(Central Limit Theorem)`: 표본의 크기가 커질수록 표본평균의 표준화 분포가 표준정규분포로 수렴하는 정리
- `LLN(Law of Large Numbers, 대수의 법칙)`: 표본 크기가 무한히 증가할 때 표본평균 '값' 자체가 모평균으로 수렴한다는 법칙
- `Standard Error(표준오차)`: 표본평균 표집분포의 표준편차 ($SE = \sigma / \sqrt{n}$)로, 표본 크기가 4배 증가하면 오차는 절반으로 감소
- `Sampling Distribution(표집분포)`: 동일한 크기의 표본을 반복 추출했을 때 계산되는 표본통계량(평균 등)들이 이루는 확률분포
- `Bootstrap`: 복원추출을 통한 대량의 재표본으로 정규성 가정 없이 표집분포와 신뢰구간을 비모수적으로 직접 근사하는 기법

</details>
---

## 1교시 예상문제 (10점)

> 중심극한정리 (Central Limit Theorem)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

### 1. 중심극한정리(CLT)의 정의 및 수학적 표현

- **정의**: 모집단의 분포 형태와 무관하게 표본 크기($n$)가 충분히 크면, 독립적으로 추출된 표본평균의 표집분포가 정규분포로 수렴하는 정리
- **수식**:
  $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1) \quad (n \to \infty)$$

### 2. CLT vs 대수의 법칙(LLN) 비교

| 비교 항목 | 대수의 법칙 (LLN) | 중심극한정리 (CLT) |
|---|---|---|
| **수렴 대상** | 표본평균 통계량의 수치적 값 ($\bar{X}$) | 표준화된 표본평균의 확률 분포 ($Z$) |
| **수렴 형태** | $\bar{X} \xrightarrow{P} \mu$ (값의 확률 수렴) | $Z \xrightarrow{d} \mathcal{N}(0, 1)$ (분포 수렴) |
| **통계적 기여** | 추정량의 일치성(Consistency) 보증 | 가설검정(z/t-test) 및 신뢰구간 산출 |

### 3. 기술사적 실무 제언: 한계 극복 대책

- 중꼬리 분포(Heavy-tailed)나 시계열 자기상관이 존재하는 경우 정규근사가 실패하므로, 부트스트랩(Bootstrap) 재표본추출 및 비모수 검정을 병행하여 검정 결론의 신뢰성을 교차검증해야 함.
---

## 2~4교시 예상문제 (25점)

> 추론통계학의 근간을 이루는 중심극한정리(CLT)의 개념, 수학적 정의, 성립 전제조건을 설명하고, 대수의 법칙(LLN)과의 차이점 및 빅데이터 환경에서 정규근사 실패(Heavy-tailed, 비독립성) 시의 보완 대책을 논하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **대수의 법칙(LLN)** | 표본평균 값의 모평균 수렴(약대수/강대수의 법칙), 일치성(Consistency)의 근거 | Ⅴ LLN 비교 |
| **표준오차(Standard Error)** | 표집분포의 산포도, $SE = \sigma/\sqrt{n}$, 표본 수 증가에 따른 오차 축소율 | Ⅲ 근사 분포 |
| **정규근사 한계와 부트스트랩** | 중꼬리 분포(Heavy-tailed), 시계열 의존성, 붓스트랩 재표본추출 보완 | Ⅵ 한계 및 대책 |

### Ⅰ. 추론통계학의 절대적 초석, 중심극한정리 개요

> 중심극한정리는 원 데이터의 분포가 아니라, '표본평균들의 분포(표집분포)'가 정규분포로 수렴함을 증명하는 수학적 정리임.

- 정의: 평균이 $\mu$이고 유한한 분산 $\sigma^2$을 갖는 임의의 모집단으로부터 독립적으로 추출된 크기 $n$의 표본평균 $\bar{X}$에 대해, 표본 크기 $n$이 충분히 크면 표준화 변수 $Z$는 모집단 분포와 무관하게 표준정규분포 $\mathcal{N}(0, 1)$에 확률 수렴한다는 정리
- 수학적 표현:
  $$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1) \quad (\text{as } n \to \infty)$$
- 통계적 의의:
  1. 현실의 모집단이 정규분포가 아니더라도(비대칭, 편향 분포 등), 표본 수만 충분하면 정규분포 기반의 모수 검정(z-검정, 신뢰구간 추정)을 가능하게 함
  2. 표본오차의 한계를 정량화하여 필요한 최소 표본 크기($n$)를 수학적으로 산정할 수 있는 기준선 제공

### Ⅱ. 중심극한정리의 성립 전제조건

> 표본 크기 수치보다 독립성과 유한분산 조건이 정규근사의 성패를 좌우함.

| 전제조건 | 상세 내용 | 조건 위배 시 현상 및 점검 방안 |
|---|---|---|
| **독립 동일 분포 (IID)** | 표본들이 상호 독립적이며 동일한 확률분포에서 추출되어야 함 | 시계열 자기상관이나 군집 표본일 경우 표준오차 과소추정 |
| **유한한 모분산 ($\sigma^2 < \infty$)** | 모집단의 분산이 수학적으로 유한한 상수로 수렴해야 함 | 파레토 분포, 코시 분포 등 중꼬리 분포에서는 정규 수렴 실패 |
| **충분한 표본 크기 ($n$)** | 통상 $n \ge 30$ 이상 권장 (단, 왜도에 따라 차등) | 왜도(Skewness)가 극심한 경우 $n=100$ 이상 필요 (시뮬레이션 확인) |

### Ⅲ. 표본평균의 표집분포와 표준오차($SE$)

> 표본평균의 분산은 원 모집단 분산의 $1/n$로 축소되므로 표본이 커질수록 평균 추정의 정확도가 급상승함.

<svg viewBox="0 0 520 155" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="표본 크기 증가에 따른 표준오차 반감 메커니즘" role="img">
  <defs>
    <marker id="se-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <!-- Step 1: n = 25 -->
  <g transform="translate(15, 20)">
    <rect width="140" height="75" rx="5" fill="#21262d" stroke="#30363d"/>
    <text x="70" y="24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold" fill="#c9d1d9" text-anchor="middle">표본 n = 25</text>
    <text x="70" y="46" font-family="system-ui, sans-serif" font-size="10" fill="#f0883e" text-anchor="middle">SE = σ / 5</text>
    <text x="70" y="62" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e" text-anchor="middle">기준 표준오차</text>
  </g>
  <path d="M 158 57 L 187 57" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#se-arrow)"/>
  <text x="172" y="48" font-family="system-ui, sans-serif" font-size="8" fill="#58a6ff" text-anchor="middle">4배↑</text>

  <!-- Step 2: n = 100 -->
  <g transform="translate(190, 20)">
    <rect width="140" height="75" rx="5" fill="#21262d" stroke="#58a6ff"/>
    <text x="70" y="24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold" fill="#58a6ff" text-anchor="middle">표본 n = 100</text>
    <text x="70" y="46" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#3fb950" text-anchor="middle">SE = σ / 10</text>
    <text x="70" y="62" font-family="system-ui, sans-serif" font-size="8.5" fill="#3fb950" text-anchor="middle">오차 1/2로 반감!</text>
  </g>
  <path d="M 333 57 L 362 57" stroke="#58a6ff" stroke-width="1.5" marker-end="url(#se-arrow)"/>
  <text x="347" y="48" font-family="system-ui, sans-serif" font-size="8" fill="#58a6ff" text-anchor="middle">4배↑</text>

  <!-- Step 3: n = 400 -->
  <g transform="translate(365, 20)">
    <rect width="140" height="75" rx="5" fill="#21262d" stroke="#3fb950"/>
    <text x="70" y="24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold" fill="#3fb950" text-anchor="middle">표본 n = 400</text>
    <text x="70" y="46" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#3fb950" text-anchor="middle">SE = σ / 20</text>
    <text x="70" y="62" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e" text-anchor="middle">오차 다시 1/2 반감</text>
  </g>

  <!-- Bottom Principle Rule -->
  <g transform="translate(15, 105)">
    <rect width="490" height="34" rx="4" fill="rgba(88,166,255,0.08)" stroke="rgba(88,166,255,0.3)"/>
    <text x="245" y="21" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9" text-anchor="middle">
      표준오차 법칙: <tspan fill="#58a6ff" font-weight="bold">SE = σ / √n</tspan> $\implies$ 표본 크기가 4배 증가해야 추정 정밀도(오차 축소)는 2배 향상됨
    </text>
  </g>
</svg>

- **표준편차(SD) vs 표준오차(SE)**:
  - **표준편차(SD, $\sigma$)**: 개별 데이터 포인트들이 모평균 주변에 흩어진 산포도 (자연적 변동성)
  - **표준오차(SE, $\sigma/\sqrt{n}$)**: 표본평균이라는 통계량 자체가 얼마나 정확한지를 나타내는 오차 척도

### Ⅳ. 중심극한정리(CLT) vs 대수의 법칙(LLN) 비교

> 두 정리는 상호 보완적이며 통계적 추론의 양대 기둥을 이룸.

<svg viewBox="0 0 520 160" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="대수의 법칙과 중심극한정리의 수렴 메커니즘 대비" role="img">
  <!-- LLN Box -->
  <g transform="translate(15, 15)">
    <rect width="235" height="130" rx="5" fill="#21262d" stroke="#58a6ff" stroke-width="1"/>
    <text x="117" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#58a6ff" text-anchor="middle">대수의 법칙 (LLN)</text>
    <rect x="15" y="34" width="205" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
    <text x="117" y="52" font-family="system-ui, sans-serif" font-size="9.5" fill="#c9d1d9" text-anchor="middle">수렴 대상: 표본평균 "값 (X̄)"</text>
    <text x="15" y="80" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 형태: X̄ $\xrightarrow{P}$ μ (확률 수렴)</text>
    <text x="15" y="96" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 의미: "표본 늘리면 참값을 맞춘다"</text>
    <rect x="15" y="106" width="205" height="20" rx="3" fill="rgba(88,166,255,0.15)"/>
    <text x="117" y="120" font-family="system-ui, sans-serif" font-size="8" font-weight="bold" fill="#58a6ff" text-anchor="middle">추정량의 일치성(Consistency) 보장</text>
  </g>

  <!-- CLT Box -->
  <g transform="translate(270, 15)">
    <rect width="235" height="130" rx="5" fill="#21262d" stroke="#3fb950" stroke-width="1"/>
    <text x="117" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#3fb950" text-anchor="middle">중심극한정리 (CLT)</text>
    <rect x="15" y="34" width="205" height="28" rx="4" fill="#161b22" stroke="#30363d"/>
    <text x="117" y="52" font-family="system-ui, sans-serif" font-size="9.5" fill="#c9d1d9" text-anchor="middle">수렴 대상: 오차의 "분포 (Z)"</text>
    <text x="15" y="80" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 형태: Z $\xrightarrow{d} \mathcal{N}(0, 1)$ (분포 수렴)</text>
    <text x="15" y="96" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 의미: "오차의 확률적 흩어짐을 안다"</text>
    <rect x="15" y="106" width="205" height="20" rx="3" fill="rgba(63,185,80,0.15)"/>
    <text x="117" y="120" font-family="system-ui, sans-serif" font-size="8" font-weight="bold" fill="#3fb950" text-anchor="middle">가설검정·신뢰구간 도출의 근거</text>
  </g>
</svg>

| 비교 항목 | 대수의 법칙 (Law of Large Numbers) | 중심극한정리 (Central Limit Theorem) |
|---|---|---|
| **수렴의 대상** | 표본평균 통계량의 **수치적 값 ($\bar{X}$)** | 표준화된 표본평균의 **확률 분포 ($Z$)** |
| **수렴의 형태** | 값의 확률 수렴 ($\bar{X} \xrightarrow{P} \mu$) | 분포 수렴 ($Z \xrightarrow{d} \mathcal{N}(0, 1)$) |
| **핵심 질문** | "표본을 무한히 모으면 모평균을 맞출 수 있는가?" | "표본평균이 모평균에서 벗어난 오차는 어떤 분포를 띠는가?" |
| **통계적 기여** | 추정량의 **일치성(Consistency)** 보증 | 신뢰구간 산출 및 **가설검정(z-test, t-test)**의 근거 |

### Ⅴ. 정규 모집단 vs 비정규 모집단에서의 CLT 동작

> 정규 모집단은 표본 크기에 무관하게 정규분포를 따르며, 비정규 모집단은 $n$이 증가함에 따라 단계적으로 정규화됨.

| 모집단 형태 | 표본 크기 $n < 30$ | 표본 크기 $n \ge 30$ | 적용 검정 기법 |
|---|---|---|---|
| **정규 모집단** | 표본평균은 항상 정규분포 따름 | 당연히 완벽한 정규분포 따름 | 모분산 기지: z-검정 / 모분산 미지: t-검정 |
| **완만한 비정규 (균등분포 등)** | $n=10$ 수준에서도 정규분포에 근접 | 완벽한 정규분포로 수렴 | CLT 기반 t-검정 및 z-검정 |
| **극단적 비정규 (지수, 로그정규)**| 강한 비대칭 왜도 유지 (근사 왜곡) | $n \ge 50 \sim 100$ 이상에서 수렴 | 충분한 표본 확보 후 검정 또는 부트스트랩 |
| **중꼬리 분포 (코시, 멱법칙)** | 무한분산으로 인해 영원히 정규 수렴 불가 | 중심극한정리 성립 불가 | 윌콕슨 순위합 검정 등 비모수 검정 필수 |

### Ⅵ. 중심극한정리 실무 위험 관리 및 한계 극복 대책

> 기계적인 $n \ge 30$ 맹신을 탈피하고 데이터 생성과정의 위배 요인을 통제함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 심한 왜도 데이터에서 $n=30$ 기계적 맹신 | Q-Q Plot 시각화 및 부트스트랩(Bootstrap) 재표본추출 교차검증 | 표본 크기 부족으로 인한 1종 오류 팽창 방지 |
| 시계열·공간 데이터의 비독립성 (자기상관) | Newey-West 강건 표준오차 또는 군집 표준오차(Clustered SE) 적용 | 독립성 위배로 인한 분산 과소평가 및 가설검정 왜곡 차단 |
| 멱법칙/중꼬리(Heavy-tailed) 분포 위배 | 극단값 이론(EVT, Generalized Pareto) 및 비모수 검정 전환 | 무한 분산 모집단에서의 잘못된 정규근사 원천 배제 |
| 표본추출 편향 (선택 편향) | 확률표본추출(Random Sampling) 및 사후 성향점수 매칭(PSM) | 표본 크기만 크고 대표성이 결여된 '거짓 CLT' 방지 |

### Ⅶ. 기술사적 제언: 표본 크기보다 데이터 생성 메커니즘을 먼저 보라

> "아무리 표본 수가 1,000만 건이어도 데이터가 편향되었거나 독립성이 깨져 있다면 중심극한정리는 당신을 구원하지 못한다."

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 중심극한정리는 원자료 자체가 정규분포가 된다는 뜻이 아니라, 표준화한 '표본평균들의 표집분포'가 정규분포로 수렴한다는 정리다.
>
> **[나라면 이렇게 쓴다]**
> 표본 크기($n \ge 30$)를 기계적으로 적용하지 않고, 데이터의 왜도와 첨도, 시계열 의존성을 먼저 진단한 뒤 부트스트랩(Bootstrap) 재표본추출로 정규근사 신뢰구간의 신뢰도를 교차검증하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 표본 크기($n \ge 30$)에만 의존하지 않고, **독립성(IID), 왜도/첨도, 유한분산**의 3대 전제조건 충족 여부로 정규근사 적합성을 판정
- **대안**: 탐색적 데이터 분석(EDA)으로 Q-Q Plot 검증 $\rightarrow$ 정규근사 의심 시 부트스트랩(1,000회 재표본) 신뢰구간과 대조
- **검증 체계**: 정규근사 신뢰구간과 부트스트랩 신뢰구간의 일치율 95% 이상 확인
- **기대 효과**: 과도한 정규성 확신으로 인한 통계적 오류를 방지하고 신뢰성 높은 A/B 테스트 및 모수 추론 체계 완성

<div class="itpe-flow-map" role="img" aria-label="중심극한정리 정규근사 검증 로드맵">
  <div class="itpe-flow-node">
    <strong>1단계: 현행 한계 인식</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-fail"><strong>문제</strong><span>n ≥ 30 기계적 맹신으로 인한 심한 왜도/비독립 데이터의 1종 오류 급증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 정규근사 검증 방안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>기술 적용</strong><span>Q-Q Plot 진단 + Newey-West 군집 표준오차 + 부트스트랩(Bootstrap) 교차검증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 정량 검증 기준</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>KPI 지표</strong><span>정규근사 신뢰구간과 부트스트랩 신뢰구간 일치율 95% 이상 확인</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 궁극적 실행 효과</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>가치 창출</strong><span>표본 추출 왜곡 원천 차단 및 신뢰할 수 있는 데이터 기반 의사결정 수립</span></div>
    </div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **공식 출제 이력**: 정보관리기술사 제129회 1교시 단답형 (중심극한정리와 대수의 법칙 비교), 제121회 2교시 논술형 (추론통계의 정규성 가정과 표집분포)
- **표준 및 레퍼런스**: NIST/SEMATECH e-Handbook of Statistical Methods, OpenStax Introductory Statistics (Central Limit Theorem Chapter)

## 연결 토픽

- [z-검정](./012_z_test.md) · [불편추정량](./011_unbiased_estimator.md) · [잭나이프·부트스트랩](./068_jackknife_bootstrap.md) · [무결성 제약](./013_integrity_constraint.md)
