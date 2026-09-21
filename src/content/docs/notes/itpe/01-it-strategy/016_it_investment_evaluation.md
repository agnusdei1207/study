---
title: "IT 투자평가·투자관리"
author: "Claude Code"
date: "2026-09-21T11:20:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Claude Opus 5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 투자·포트폴리오 관리를 거쳐 IT 투자평가·투자관리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>투자·포트폴리오 관리</span>
  <strong>IT 투자평가·투자관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 투자 승인보다 **비용·위험·편익**을 전 생애주기에서 검증하는 가치관리
- 메커니즘: 사전 타당성 → 중간 집행통제 → 사후 편익검증 → 차기 투자 환류
- 통제: **TCO·NPV·IRR**로 재무성을 판단하고 **IT-BSC**로 비재무 가치를 보완

<div class="itpe-svg-map">
<svg viewBox="0 0 520 460" role="img" aria-label="사전 평가, 중간 평가, 사후 평가가 삼각으로 배치되어 같은 방향으로 순환하고 중앙에 투자 환류 루프 허브가 놓인 IT 투자평가 생애주기">
  <defs><marker id="arrow-itev-cycle" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <text class="itpe-svg-title" x="260" y="30">IT 투자평가 생애주기 · 3단계 환류</text>
  <path class="itpe-svg-link" d="M306 216 Q 400 224 418 284" marker-end="url(#arrow-itev-cycle)" />
  <path class="itpe-svg-link" d="M368 394 Q 268 442 168 390" marker-end="url(#arrow-itev-cycle)" />
  <path class="itpe-svg-link" d="M78 306 Q 86 196 198 168" marker-end="url(#arrow-itev-cycle)" />
  <circle class="itpe-svg-node" cx="260" cy="184" r="56" />
  <text class="itpe-svg-title" x="260" y="176">사전 평가</text><text class="itpe-svg-sub" x="260" y="200">타당성 검토</text>
  <circle class="itpe-svg-node" cx="400" cy="346" r="56" />
  <text class="itpe-svg-title" x="400" y="338">중간 평가</text><text class="itpe-svg-sub" x="400" y="362">집행 통제</text>
  <circle class="itpe-svg-node" cx="119" cy="346" r="56" />
  <text class="itpe-svg-title" x="119" y="338">사후 평가</text><text class="itpe-svg-sub" x="119" y="362">편익 검증</text>
  <circle class="itpe-svg-node is-current" cx="260" cy="315" r="54" />
  <text class="itpe-svg-title" x="260" y="306">투자 환류</text><text class="itpe-svg-title" x="260" y="328">Loop</text>
</svg>
</div>

<details>
<summary>핵심 용어</summary>

- **IT 투자평가**: 전 생애주기 동안 IT 비용(TCO)과 기대 편익을 측정하고 지속 관리하는 활동
- **Productivity Paradox(생산성의 역설)**: 막대한 IT 투자에도 불구하고 거시적 생산성 향상이 통계상 나타나지 않는 현상
- **TCO(Total Cost of Ownership)**: 도입 초기 구매비(직접비)와 운영·유지보수·다운타임 등 간접비의 총합
- **ROI(Return on Investment)**: 투자 비용 대비 창출된 순편익의 비율로 직관적이나 화폐 시간가치를 무시함
- **NPV(Net Present Value)**: 미래 현금유입의 현재가치에서 현금유출 현재가치를 차감한 순현재가치
- **IRR(Internal Rate of Return)**: 순현재가치(NPV)를 0으로 만드는 할인율로 자본비용보다 높을 때 채택
- **EVM(Earned Value Management)**: 계획 가치(PV), 획득 가치(EV), 실제 원가(AC)를 대비하여 공정·예산을 실측 통제하는 기법
- **Val IT**: IT 투자의 비즈니스 가치 창출을 보증하기 위해 ISACA가 제정한 거버넌스 프레임워크
- **Benefits Realization Review(편익 실현 감사)**: 시스템 오픈 후 실제 ROI와 비즈니스 목표 달성 여부를 의무 검증하는 사후 평가

</details>

## 예상문제

> IT 투자평가의 생애주기와 평가기법을 설명하고, IT 생산성 역설의 문제점과 대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. IT 생산성 역설을 극복하는 IT 투자평가의 개요

> IT 투자평가는 IT 자본 배분의 정당성을 입증하고 전 생애주기 편익을 통제하며, 성패는 단순 시스템 개통이 아닌 **비즈니스 가치 실현율**로 판정함.

- 정의: 투자 대안의 **비용·위험·편익**을 비교하고 생애주기 동안 가치 실현을 통제하는 활동
- 목적: 투자 우선순위 결정 · 예산 낭비 방지 · 편익 실현

## Ⅱ. IT 투자평가의 대표 생애주기

> 사전·중간·사후 평가는 투자관리의 대표 흐름이며, 조직의 의사결정 체계에 맞춰 활동·산출을 구체화함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 투자평가 생애주기 3단계 구성체계 및 활동">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 사전 평가 (Ex-Ante)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>타당성 검토 · 우선순위 도출 · TCO 산출 · 재무 분석(NPV/IRR)</span>
      <strong>산출</strong><span>사업계획서 · 투자 타당성 분석서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 중간 평가 (In-Itinere)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>EVM 공정/예산 실측 · 마일스톤 감리 · 사업 지속성 심의</span>
      <strong>산출</strong><span>공정 현황 보고서 · 위험 대장</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 사후 평가 (Ex-Post)</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>비즈니스 편익 실현율 검증 · 생산성 역설 진단 · 차기 계획 환류</span>
      <strong>산출</strong><span>편익 실현 평가서 · 교훈(Lessons Learned) 원장</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Val IT</strong></span> · 투자 타당성 Business Case ↔ EVM 공정 통제 ↔ 사후 편익 실현율 양방향 추적</div>

## Ⅲ. 비용·편익 평가체계

> 초기 구축비뿐 아니라 운영·전환·중단 비용과 화폐의 시간가치를 함께 반영해야 하며, 재무 3축만으로는 잡히지 않는 가치는 **IT-BSC(IT Balanced Scorecard)**로 보완해야 판정이 닫힘.

<div class="itpe-svg-map">
<svg viewBox="0 0 520 415" role="img" aria-label="비용·편익 평가체계 네 축을 재무 평가 세 개와 비재무 보완 하나로 나누고 각 기법의 산식과 판정 기준을 하위 박스로 분기한 트리">
  <rect class="itpe-svg-node" x="110" y="8" width="300" height="44" rx="12" />
  <text class="itpe-svg-title" x="260" y="30">비용·편익 평가체계 4축</text>
  <path class="itpe-svg-link" d="M260 52 V64 H36 V324 M36 98 H66 M36 324 H66" />
  <rect class="itpe-svg-node is-current" x="66" y="78" width="444" height="40" rx="12" />
  <text class="itpe-svg-title" x="288" y="98">재무 평가 3 · 화폐 단위 판정</text>
  <path class="itpe-svg-link" d="M96 118 V261 M96 153 H126 M96 207 H126 M96 261 H126" />
  <rect class="itpe-svg-node" x="126" y="130" width="384" height="46" rx="10" />
  <text class="itpe-svg-label" x="318" y="144">TCO(Total Cost of Ownership) · 총소유비용</text>
  <text class="itpe-svg-sub" x="318" y="165">구축·운영·전환·중단 → 판정: 생애주기 총비용</text>
  <rect class="itpe-svg-node" x="126" y="184" width="384" height="46" rx="10" />
  <text class="itpe-svg-label" x="318" y="198">NPV(Net Present Value) · 순현재가치</text>
  <text class="itpe-svg-sub" x="318" y="219">할인 현금유입 − 유출 → 판정: NPV &gt; 0</text>
  <rect class="itpe-svg-node" x="126" y="238" width="384" height="46" rx="10" />
  <text class="itpe-svg-label" x="318" y="252">IRR(Internal Rate of Return) · 내부수익률</text>
  <text class="itpe-svg-sub" x="318" y="273">NPV=0이 되는 할인율 → 판정: IRR &gt; 자본비용</text>
  <rect class="itpe-svg-node" x="66" y="304" width="444" height="40" rx="12" />
  <text class="itpe-svg-title" x="288" y="324">비재무 보완 1 · 전략 정렬</text>
  <path class="itpe-svg-link" d="M96 344 V379 M96 379 H126" />
  <rect class="itpe-svg-node" x="126" y="356" width="384" height="46" rx="10" />
  <text class="itpe-svg-label" x="318" y="370">IT-BSC(IT Balanced Scorecard) · 균형성과표</text>
  <text class="itpe-svg-sub" x="318" y="391">재무·고객·프로세스·학습 → 판정: 전략 정렬</text>
</svg>
</div>

## Ⅳ. IT 생산성 역설의 원인·대응

> IT 투자가 성과로 보이지 않는 원인을 측정·시차·업무혁신 관점에서 분리해야 하며, 세 지점 중 어디가 끊겼는지 지목하지 못하면 대응은 구호로 끝남.

<div class="itpe-svg-map">
<svg viewBox="0 0 520 352" role="img" aria-label="IT 투자 집행에서 기대 편익이 성과로 관측되기까지 측정 누락, 성과 시차, 업무혁신 부재의 세 지점이 끊겨 생산성 역설로 이어지는 인과 흐름">
  <defs><marker id="arrow-itev-paradox" viewBox="0 0 10 10" refX="9" refY="5" markerUnits="userSpaceOnUse" markerWidth="16" markerHeight="16" orient="auto"><path d="M0,0 L10,5 L0,10 z" /></marker></defs>
  <rect class="itpe-svg-node" x="110" y="8" width="300" height="44" rx="12" />
  <text class="itpe-svg-title" x="260" y="30">IT 투자 집행 · 기대 편익</text>
  <path class="itpe-svg-link" d="M260 52 V74" marker-end="url(#arrow-itev-paradox)" />
  <rect class="itpe-svg-node" x="66" y="80" width="388" height="40" rx="12" />
  <text class="itpe-svg-title" x="260" y="100">편익 실현 경로 단절 3</text>
  <path class="itpe-svg-link" d="M96 120 V238 M96 150 H126 M96 194 H126 M96 238 H126" />
  <rect class="itpe-svg-node" x="126" y="132" width="384" height="36" rx="10" />
  <text class="itpe-svg-sub" x="318" y="150">측정 누락 · 비재무 편익 미포착</text>
  <rect class="itpe-svg-node" x="126" y="176" width="384" height="36" rx="10" />
  <text class="itpe-svg-sub" x="318" y="194">성과 시차 · 편익 실현 지연</text>
  <rect class="itpe-svg-node" x="126" y="220" width="384" height="36" rx="10" />
  <text class="itpe-svg-sub" x="318" y="238">업무혁신 부재 · 자동화 효과 미발생</text>
  <path class="itpe-svg-link" d="M260 256 V278" marker-end="url(#arrow-itev-paradox)" />
  <rect class="itpe-svg-node is-current" x="80" y="284" width="360" height="56" rx="12" />
  <text class="itpe-svg-title" x="260" y="306">생산성 역설</text>
  <text class="itpe-svg-sub" x="260" y="328">Productivity Paradox · 통계상 성과 미가시</text>
</svg>
</div>

| 원인 | 대응 | 효과 |
|---|---|---|
| **측정 누락** | IT-BSC로 품질·고객 가치 보완 | 비재무 편익 가시화 |
| **성과 시차** | 단계별 목표와 사후 편익 추적 | 조기 단정 방지 |
| **업무혁신 부재** | BPR·변화관리 병행 | 자동화 효과 실현 |

## Ⅴ. IT 투자관리의 문제점·대응책

> 사전 평가의 장밋빛 왜곡과 사후 평가 부재를 방지하려면 승인 시 Business Case를 운영 후 실측 편익과 대조하는 판정 지점을 제도화해야 함.

<div class="itpe-flow-map" role="img" aria-label="승인 시 Business Case를 기준으로 편익 실현 검토에서 통과와 미통과로 갈라지는 투자관리 판정 분기">
  <div class="itpe-flow-node">
    <strong>승인 시 Business Case</strong>
    <div class="itpe-step-detail"><strong>기준</strong><span>목표 편익 · 누적 TCO · 편익 책임자</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>편익 실현 검토</strong>
    <div class="itpe-step-detail"><strong>판정 질문</strong><span>운영 후 실측 편익이 승인 시 목표에 도달했는가?</span></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass"><strong>통과</strong><span>차기 포트폴리오 우선순위 유지</span></div>
    <div class="itpe-flow-branch is-fail"><strong>미통과</strong><span>편차 원인 분석 → 개선·중단 결정</span></div>
  </div>
</div>

| 위험 | 대책 | 효과 |
|---|---|---|
| **구축 후 운영비 폭증** | 5개년 누적 TCO(직접비+간접비+숨은비용) 산정 템플릿 의무화 | 총소유비용 예측 오차 최소화 |
| **사후 편익 평가 부재** | 운영 안정화 후 편익 실현 검토 시점·책임자 지정 | 목표 대비 편익 편차 확인 |
| **무형 가치 산정 왜곡** | AHP 다기준 평가 · IT-BSC로 평가 근거 기록 | 정성 평가의 일관성 향상 |

## Ⅵ. 결론 — 가치 거버넌스 중심의 투자관리

> IT 투자평가의 본질은 사업 착수를 승인받기 위한 장밋빛 보고서가 아니라 시스템 수명주기 내내 실제 업무 생산성과 비즈니스 편익을 증명하는 거버넌스 과정임.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: IT 투자 실패는 기술 부족보다 승인 당시 Business Case와 운영 후 실측 편익이 단절되는 데서 발생한다. 승인 문서와 실측 결과를 대조할 주체가 없으면 생산성 역설은 원인 규명 없이 반복된다.
- `나라면`: 투자 승인 시 편익 책임자·측정 시점·중단 기준을 함께 확정하고, 사후 검토 결과를 다음 포트폴리오 우선순위 심의의 필수 입력으로 쓰겠다.

### 실전 답안용 기술사적 제언

- 판정: 승인 시 Business Case와 운영 후 실측 편익이 하나의 환류 고리로 이어지는지 여부
- 대안: 생애주기 누적 TCO 산정 · 편익 책임자·측정 시점·중단 기준의 승인 시 확정
- 검증: 사전 목표 대비 비용·편익·위험 편차와 편익 실현 검토 통과 여부
- 효과: 예산 낭비 방지 · 차기 투자 우선순위 환류

<div class="itpe-pipeline is-vertical" role="img" aria-label="Val IT 기반 IT 투자 생애주기 가치 관리 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>사전 승인용 장밋빛 ROI · 사후 편익 추적 부재 · 생산성 역설</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>생애주기 TCO · 편익 책임자 · 사후 검토 제도화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>사전 목표 대비 비용·편익·위험 편차</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>예산 낭비 방지 · 차기 투자 우선순위 개선</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **비용·위험·편익**을 비교하고 생애주기 동안 가치 실현을 통제하는 활동
- 목적: 투자 우선순위 결정 · 예산 낭비 방지 · 편익 실현

### 2. 투자평가 3단계와 산출

<div class="itpe-pipeline is-vertical" role="img" aria-label="IT 투자평가 생애주기 3단계 요약">
  <div class="itpe-pipeline-node">
    <strong>사전 평가</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>타당성 · TCO 산정</span><strong>산출</strong><span>투자 타당성서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>중간 평가</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>EVM 공정/비용 실측</span><strong>산출</strong><span>공정 보고서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>사후 평가</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>편익 실현율 감사</span><strong>산출</strong><span>교훈 원장</span></div>
  </div>
</div>

### 3. 핵심 통제

- **TCO(Total Cost of Ownership)**: 도입 직접비 외에 5개년 누적 간접비·숨은 비용(교육, 다운타임) 전수 계상
- 편익 실현 감사: 시스템 오픈 1년 후 Business Case 편익 달성도를 의무 실측하여 생산성 역설 차단

## 출제 이력과 검증 출처

- [ISACA Glossary: Val IT](https://www.isaca.org/resources/glossary)
- [NIA 국가정보화백서: 기획·예산·평가 연계](https://www.nia.or.kr/files/ko/nia2009/download/it/87.pdf)

## 학습 체크

- [ ] Ⅰ 개요: IT 투자평가를 전 생애주기 비용·위험·편익 통제로 정의하고 목적을 제시할 수 있는가?
- [ ] Ⅱ 생애주기: 사전·중간·사후 평가를 삼각 순환으로 그리고 각 단계의 활동·산출을 한 쌍으로 재현할 수 있는가?
- [ ] Ⅲ 평가체계: 재무 3축(TCO·NPV·IRR)과 비재무 보완 1축(IT-BSC)을 트리로 묶고 축별 판정 기준을 쓸 수 있는가?
- [ ] Ⅳ 생산성 역설: 측정 누락·성과 시차·업무혁신 부재의 세 단절 지점과 대응·효과를 연결할 수 있는가?
- [ ] Ⅴ 문제점·대응책: 편익 실현 검토의 통과·미통과 분기를 그리고 운영비 누락·사후평가 부재·무형가치 왜곡의 위험·대책·효과를 연결할 수 있는가?
- [ ] Ⅵ 결론: Business Case와 실측 편익을 연결한 판정·대안·검증·효과를 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [애자일 대응 전략](./013_agile_response_strategy.md)
- 연관 토픽: [BSC](./017_bsc.md), [FinOps](./012_finops.md), [ISMP](./001_ismp.md)
- 다음 토픽: [BSC](./017_bsc.md)
