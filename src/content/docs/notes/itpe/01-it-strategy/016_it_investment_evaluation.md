---
title: "IT 투자평가·투자관리"
author: "OpenAI Codex"
date: "2026-09-21T10:55:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5"
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

<div class="itpe-flow-map" role="img" aria-label="IT 투자평가 생애주기 3단계 및 가치 환류 체계">
  <div class="itpe-flow-node">
    <strong>1. 사전 평가 (Ex-Ante)</strong>
    <div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>활동</strong><span>타당성 검토 · 우선순위 도출 · TCO 산출 · 재무 분석</span></div></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>2. 중간 평가 (In-Itinere)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>통제</strong><span>EVM 공정/예산 실측 · 일정 지연 및 비용 초과(Overrun) 방어</span></div>
      <div class="itpe-flow-branch"><strong>판단</strong><span>사업 지속 여부 심의(Go/No-Go) · 자원 재배분</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3. 사후 평가 (Ex-Post)</strong>
    <div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>산출</strong><span>편익 실현율(ROI) 검증 · 생산성 역설 진단 · 교훈 환류</span></div></div>
  </div>
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

> 초기 구축비뿐 아니라 운영·전환·중단 비용과 화폐의 시간가치를 함께 반영해야 함.

| 관점 | 포함 항목 | 판정 |
|---|---|---|
| **TCO(Total Cost of Ownership)** | 구축 · 운영 · 전환 · 중단 비용 | 생애주기 총비용 |
| **NPV(Net Present Value)** | 할인 현금유입 − 할인 현금유출 | NPV > 0 |
| **IRR(Internal Rate of Return)** | NPV를 0으로 만드는 할인율 | IRR > 자본비용 |
| **IT-BSC(IT Balanced Scorecard)** | 재무 · 고객 · 프로세스 · 학습 | 전략 정렬 보완 |

## Ⅳ. IT 생산성 역설의 원인·대응

> IT 투자가 성과로 보이지 않는 원인을 측정·시차·업무혁신 관점에서 분리해야 함.

| 원인 | 대응 | 효과 |
|---|---|---|
| **측정 누락** | IT-BSC로 품질·고객 가치 보완 | 비재무 편익 가시화 |
| **성과 시차** | 단계별 목표와 사후 편익 추적 | 조기 단정 방지 |
| **업무혁신 부재** | BPR·변화관리 병행 | 자동화 효과 실현 |

## Ⅴ. IT 투자관리의 문제점·대응책

> 사전 평가의 장밋빛 왜곡과 사후 평가 부재를 방지하기 위해 5개년 누적 TCO와 편익 실현 감사를 제도화해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **구축 후 운영비 폭증** | 5개년 누적 TCO(직접비+간접비+숨은비용) 산정 템플릿 의무화 | 총소유비용 예측 오차 최소화 |
| **사후 편익 평가 부재** | 운영 안정화 후 편익 실현 검토 시점·책임자 지정 | 목표 대비 편익 편차 확인 |
| **무형 가치 산정 왜곡** | AHP 다기준 평가 · IT-BSC로 평가 근거 기록 | 정성 평가의 일관성 향상 |

## Ⅵ. 결론 — 가치 거버넌스 중심의 투자관리

> IT 투자평가의 본질은 사업 착수를 승인받기 위한 장밋빛 보고서가 아니라 시스템 수명주기 내내 실제 업무 생산성과 비즈니스 편익을 증명하는 거버넌스 과정임.

`[핵심 통찰]` IT 투자 실패는 기술 부족보다 승인 당시 Business Case와 운영 후 실측 편익이 단절되는 데서 발생함.

`나라면` 투자 승인 시 편익 책임자·측정 시점·중단 기준을 함께 확정하고, 사후 결과를 다음 포트폴리오 우선순위에 반영하겠음.

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

### 2. 구성체계 및 방법론

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

- [ ] Ⅰ 개요: IT 투자평가를 전 생애주기 비용·편익 관리로 정의할 수 있는가?
- [ ] Ⅱ 생애주기: 사전·중간·사후 평가의 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ TCO: 직접비·간접비·숨은 비용의 범위를 설명할 수 있는가?
- [ ] Ⅳ 평가: 생산성 역설 원인과 ROI·NPV·IRR·IT-BSC의 판정 차이를 설명할 수 있는가?
- [ ] Ⅴ 문제점·대응책: 운영비 누락·사후평가 부재·무형가치 왜곡의 위험·대책·효과를 연결할 수 있는가?
- [ ] Ⅵ 결론: Business Case와 실측 편익을 연결한 판정·대안·검증·효과를 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [애자일 대응 전략](./013_agile_response_strategy.md)
- 연관 토픽: [BSC](./017_bsc.md), [FinOps](./012_finops.md), [ISMP](./001_ismp.md)
- 다음 토픽: [BSC](./017_bsc.md)
