---
title: "프로젝트 위험관리"
author: "Antigravity"
date: "2026-09-20T20:37:01+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.1 Pro (High)"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → 프로젝트 관리 → **프로젝트 위험관리**

## 큰 그림과 30초 인출

- 본질: **프로젝트 위험관리(Project Risk Management)**는 프로젝트 목표에 영향을 미치는 미래 불확실성을 식별·분석하여 부정적 위협은 억제하고 긍정적 기회는 극대화하는 선제적 통제 활동
- 메커니즘: 위험 식별 ──▶ 정성적 분석(**P×I 매트릭스**) ──▶ 정량적 분석(**EMV** · 몬테카를로) ──▶ 대응 전략 수립(위협 5대 · 기회 5대) ──▶ 감시
- 산출물: 위험 등록부(Risk Register), 위협 대응(회피·완화·전가·수용·상향), 기회 대응(활용·공유·증대·수용·상향), **우발예비비** 및 **관리예비비** 통제

<div class="itpe-flow-map" role="img" aria-label="프로젝트 위험관리 식별·분석 및 대응 체계">
  <div class="itpe-flow-node">
    <strong>위험 식별 및 분석</strong>
    <div class="itpe-flow-branches"><div class="itpe-flow-branch"><strong>산출</strong><span>위험 등록부 · P×I · EMV · 몬테카를로 분석</span></div></div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>위험 대응 전략 수립</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>위협(부정적)</strong><span><span class="itpe-keyword"><strong>회피</strong></span> · <span class="itpe-keyword"><strong>완화</strong></span> · <span class="itpe-keyword"><strong>전가</strong></span> · <span class="itpe-keyword"><strong>수용</strong></span> · <span class="itpe-keyword"><strong>상향</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>기회(긍정적)</strong><span><span class="itpe-keyword"><strong>활용</strong></span> · <span class="itpe-keyword"><strong>공유</strong></span> · <span class="itpe-keyword"><strong>증대</strong></span> · <span class="itpe-keyword"><strong>수용</strong></span> · <span class="itpe-keyword"><strong>상향</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>잔여 위험 감시 및 예비비 통제</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>식별 위험</strong><span>우발예비비 배정 · PM 직접 통제</span></div>
      <div class="itpe-flow-branch"><strong>미식별 위험</strong><span>관리예비비 배정 · 경영진 승인 통제</span></div>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **프로젝트 위험관리(Project Risk Management)**: 프로젝트 생애주기 동안의 불확실성을 체계적으로 식별·분석하여 성공을 보증하는 핵심 사업관리 활동
- **위험 등록부(Risk Register)**: 식별된 모든 위험의 원인, 사건, 영향, 확률, 영향도, 대응책, 담당자를 종합 기록하는 살아있는 문서
- **P×I 매트릭스(Probability and Impact Matrix)**: 발생 확률과 영향도의 곱으로 위험 점수를 산출하여 우선순위를 등급화하는 정성적 분석 도구
- **EMV(Expected Monetary Value)**: 각 시나리오의 발생 확률과 재무적 결과를 곱하여 가중 평균 기댓값을 산출하는 정량적 분석 기법
- **몬테카를로 시뮬레이션(Monte Carlo Simulation)**: 확률 분포 난수 기반 컴퓨터 시뮬레이션으로 수천 회 반복 연산하여 공기 및 예산 달성 확률을 예측하는 기법
- **우발예비비(Contingency Reserve)**: 식별된 잔여 위험(Known-Unknowns)에 대비하여 PM 권한으로 원가 기준선 내에 사전 배정하는 예비비
- **관리예비비(Management Reserve)**: 미식별 위험(Unknown-Unknowns)에 대비하여 최고경영진 권한으로 총예산 외곽에 배정하는 예비비
- **2차 위험(Secondary Risk)**: 특정 위험 대응책을 실행함으로써 부수적으로 새롭게 파생되어 발생하는 또 다른 위험

</details>

## 예상문제

> 프로젝트 위험관리의 개념 및 7개 프로세스를 설명하고, 부정적 위험(위협) 대응 전략 5가지와 긍정적 위험(기회) 대응 전략 5가지를 비교 설명한 후, 예비비(Reserve) 관리 및 2차 위험(Secondary Risk) 통제 방안을 제시하시오. (25점)

## Ⅰ. 불확실성을 선제적으로 통제하는 프로젝트 위험관리의 개요

> 위험관리는 사후 수습이 아닌 미래 불확실성에 대한 선제적 개입이며, 성패는 단순 등록부 작성이 아닌 실질적 조기경보 트리거와 예비비 통제력으로 판정함

- 정의: 프로젝트 생애주기 동안 목표 달성에 영향을 미치는 불확실성을 식별·분석하여 위협(Threat)의 악영향은 최소화하고 기회(Opportunity)는 극대화하는 선제적 통제 활동
- 목적: 일정 지연 및 원가 초과 선제 방어, 최종 프로젝트 성공률 제고

## Ⅱ. 위험관리 구성체계 및 7개 프로세스

> 계획부터 감시까지 단계별 폐루프(Closed Loop) 통제를 통해 잠재 위험이 현실의 이슈로 비화되는 것을 원천 차단함

<div class="itpe-pipeline is-vertical" role="img" aria-label="위험관리 7개 프로세스 활동 및 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 위험관리 계획 수립</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>관리 방법론 정의 · RACI 확정 · 예비비 할당 기준 수립</span>
      <strong>산출</strong><span>위험관리 계획서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 위험 식별</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>위험 원인 · 발생 사건 · 미치는 파급 영향 구조화</span>
      <strong>산출</strong><span>초기 위험 등록부(Risk Register)</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 정성적 위험 분석</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>발생 확률 · 영향도 주관적 평가 및 우선순위 지정</span>
      <strong>산출</strong><span>P×I 매트릭스 · 우선순위 감시대상 목록</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 정량적 위험 분석</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>EMV · 몬테카를로 활용 일정 및 비용 객관적 수치 분석</span>
      <strong>산출</strong><span>정량적 분석 보고서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 위험 대응 계획 수립</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>위협/기회 대응 전략 · 발동 트리거 · 소요 예비비 결정</span>
      <strong>산출</strong><span>대응계획이 반영된 위험 등록부</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑥ 위험 대응 실행</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>대응책 현장 실행 · 예비비 지출 승인 · 2차 위험 등록</span>
      <strong>산출</strong><span>공식 변경 요청(CR) · 갱신된 위험 등록부</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑦ 위험 감시</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>트리거 상시 감시 · 위험 대응 감사 · 주기적 재평가 수행</span>
      <strong>산출</strong><span>위험 성과 정보 · 프로젝트 교훈집(Lessons Learned)</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>위험 통제 루프</strong></span> 경로: P×I 분석 → EMV 분석 → 위협·기회 대응 수립 → 예비비 통제 → 등록부 상시 갱신</div>

## Ⅲ. 위험 분석 기법: 정성적 분석 vs 정량적 분석

> P×I 정성 분석으로 신속히 1차 우선순위를 좁히고, EMV와 몬테카를로 정량 분석으로 객관적 예비비 규모를 정밀 산출함

| 분석 기법 유형 | 주요 분석 기법 도구 | 핵심 분석 메커니즘 | 실무 적용 목적 |
|---|---|---|---|
| **정성적 분석** | **P×I 매트릭스**, 위험 데이터 품질 평가 | 확률과 영향도를 등급화(예: 1~5점)하여 위험 점수 단순 산출 | 신속한 위험 우선순위 지정 및 고위험군 집중 관리 표적화 |
| **정량적 분석** | **기대화폐가치(EMV)**, **몬테카를로 시뮬레이션** | 확률 분포 난수 기반 반복 연산 및 확률 $\times$ 금액의 가중평균 | 필요 재무 예비비 산출 및 프로젝트 일정 준공 확률 구간 도출 |

## Ⅳ. 위험 대응 전략: 부정적 위험(위협) vs 긍정적 위험(기회) 대칭 비교

> 위협은 회피·완화·전가·수용·상향으로 피해를 차단하고, 기회는 활용·공유·증대·수용·상향으로 비즈니스 가치를 극대화함

| 통제 전략 관점 | 부정적 위험 (위협: Threat) 대응 | 긍정적 위험 (기회: Opportunity) 대응 |
|---|---|---|
| **원인 근본 통제** | **회피 (Avoid)**: 계획을 변경하여 위협 원인 자체를 제거 (예: 미검증 솔루션 전면 배제) | **활용 (Exploit)**: 기회 실현 조건을 확정적으로 확보 (예: 핵심 A급 인력 최우선 투입) |
| **영향 및 확률 조절** | **완화 (Mitigate)**: 발생 확률이나 악영향을 수용 임계치 이하로 축소 (예: 서버 다중화 구성) | **증대 (Enhance)**: 기회의 발생 확률이나 긍정적 파급 영향을 적극 확대 (예: 자원 추가 집중 배분) |
| **제3자 외부 협업** | **전가 (Transfer)**: 위험 발생 책임과 재무 손실을 제3자에게 이전 (예: 손해보험 가입, 하도급 외주) | **공유 (Share)**: 이익을 극대화할 제3자와 선제적으로 협력 (예: 전문사와 컨소시엄 구성) |
| **자연적 발생 대응** | **수용 (Accept)**: 계획 변경 없이 현 상태 인정 (능동적: 우발예비비 편성, 수동적: 사후 조치) | **수용 (Accept)**: 추가 투자 없이 기회가 발생하면 그 긍정적 이익을 자연 취득 |
| **권한 및 책임 상향** | **상향 (Escalate)**: 현장 PM 권한을 초과하는 리스크를 최고경영진/PMO로 이관 보고 | **상향 (Escalate)**: 프로젝트 범위를 넘어 전사에 이익이 되는 대형 사업 기회를 경영진으로 이관 |

## Ⅴ. 위험관리 실효성 확보를 위한 실무 위험과 통제 대책

> 위험 등록부 사장화와 통제 없는 2차 위험 파생을 차단하기 위해, 실시간 트리거 모니터링과 권한별 예비비 엄격 분리가 필수적임

| 실무 통제 위험 현상 | 주요 발생 원인 | 대책 (통제 방안) | 효과 (검증 기준) |
|---|---|---|---|
| **위험 등록부의 사장화** | 사업 초기에 일회성으로 문서를 작성한 후 주간 회의 등에서 점검 상시화 생략 | 주간 PMO 회의 핵심 안건화 및 사전 **경고 트리거** 연동 필수화 | 위험 등록부 갱신 주기 및 트리거 조치 이력 확인 |
| 예비비 관리 권한 혼선 | 예비비 성격 구분 부재로 임의 지출 남발 및 집행 분쟁 발생 | **우발예비비**(PM 권한: 잔여위험)와 **관리예비비**(경영진 권한: 미식별 위험) 엄격 분리 | 예비비 승인 전결권 준수 및 집행 내역 일치 |
| **2차 위험(Secondary Risk)** 누락 | 외주 전가 등 1차 대응책 실행 과정에서 새로운 부수적 위험이 파생됨 | 최초 대응 전략 승인 전 2차 위험 파급 영향 사전 의무 평가 | 2차 위험 식별·책임 할당·대응 기록 갱신 여부 |

## Ⅵ. 선행지표 기반 위험 조기경보를 위한 기술사적 제언

> 위험 등록부는 단순 문서가 아니라 선행지표와 트리거가 실시간 연결된 의사결정 장치이며, 책임자와 임계치의 명확화가 필수적임

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 위험 관리는 불확실성을 완벽히 0으로 없애겠다는 비현실적 목표가 아니라, 프로젝트의 허용 수용 수준(Risk Tolerance)과 대응 책임을 명확히 하는 과정이다. 위험 등록부가 공정 지연율, 결함 증가율, 요구사항 변경 건수 같은 정량적 선행지표와 연결되지 않으면, 결국 위험은 통제 불능의 '이슈(장애)'가 터진 뒤에야 사후 수습의 대상이 된다.
- `나라면`: 단순 엑셀 관리에 머물지 않고, 일정 지연 임계치, 결함 임계치, 변경 요청 누적 건수를 시스템 선행지표로 자동 연결하겠다. 임계치 초과 시 담당자에게 즉시 확인을 요구하고 PMO로 자동 상향 통지되는 체계를 만들겠다. 다만 우발예비비 집행 자체는 자동화하지 않고 철저히 PM의 명시적 판단과 근거 기록을 남기도록 통제하겠다.

### 실전 답안용 기술사적 제언

- 판정: 일회성 등록부 갱신 여부가 아니라 선행지표·책임자·대응기한의 실질적 연결 상태로 위험관리 성숙도 판단
- 대안: **실시간 위험 조기경보 대시보드** 구축 및 **2차 위험 사전 평가 프로세스** 운영
- 검증: 핵심 선행지표 임계치 초과 이력 · 담당자 승인 확인 · 대응기한 준수율 · 예비비 승인 근거 추적
- 효과: 잠재 위험의 이슈 전환 조기 탐지 방어 · 무근거 예비비 집행 원천 억제 및 예산 효율화

<div class="itpe-pipeline is-vertical" role="img" aria-label="선행지표 기반 위험 조기경보 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>위험 문서 사장화 · 소방수식 사후 수습 반복 · 2차 위험 미식별로 인한 프로젝트 파행</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>정량적 선행지표 임계치 설정 · 위험 책임자(Owner) 명시 · 자동 트리거 대응기한 연결</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>임계치 초과 알림 확인율 · 조치 기한 준수율 · 예비비 승인 근거 및 2차 위험 식별 이력</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>잠재 위험 조기 노출 및 대응 지연 원천 감소 · 예비비 집행의 사업적 책임성 확보</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 프로젝트 위험관리 정의 및 목적

- 정의: **프로젝트 위험관리**는 프로젝트 생애주기 동안의 불확실성을 식별·분석하여 위협(Threat)은 최소화하고 기회(Opportunity)는 극대화하는 선제적 통제 활동
- 목적: 일정 지연 및 원가 초과 선제 방어, 프로젝트 최종 성공률 제고

### 2. 위험관리 7단계 프로세스

<div class="itpe-pipeline is-vertical" role="img" aria-label="위험관리 7개 프로세스 요약">
  <div class="itpe-pipeline-node">
    <strong>위험 식별</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>위험 원인 · 파급 영향 도출</span><strong>산출</strong><span>위험 등록부 초안</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>정성적 분석</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>발생가능성 · 영향 주관적 평가</span><strong>산출</strong><span>P×I 매트릭스 우선순위</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>정량적 분석</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>비용 · 일정 파급 영향을 수치화</span><strong>산출</strong><span>EMV · 몬테카를로 실측</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>대응 전략 수립</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>대응책 및 트리거 · 책임자 지정</span><strong>산출</strong><span>위협/기회 상세 대응계획</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>대응 실행 및 감시</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>대응책 수행 · 예비비 승인 · 상시 점검</span><strong>산출</strong><span>등록부 갱신 · 위험 조치보고서</span></div>
  </div>
</div>

### 3. 대응 전략 및 예비비 통제 주체

| 통제 구분 | 대응 전략 및 적용 대상 | 핵심 통제 권한 주체 |
|---|---|---|
| 부정적 위협 | 회피 · 완화 · 전가 · 수용 · 상향 | 위험 담당 책임자 · 현장 PM |
| 긍정적 기회 | 활용 · 공유 · 증대 · 수용 · 상향 | 위험 담당 책임자 · 현장 PM |
| **우발예비비** | 식별된 잔여 위험 (Known-Unknowns) | 현장 PM (프로젝트 통제선) |
| **관리예비비** | 미식별 위험 (Unknown-Unknowns) | 최고경영진 (경영 통제선) |

## 출제 이력과 검증 출처

- 제138회 정보관리기술사 1교시: "프로젝트 위험관리"
- PMI, A Guide to the Project Management Body of Knowledge (PMBOK Guide) 7th Edition

## 학습 체크

- [ ] Ⅰ 개요: 위험(불확실성 예측)과 이슈(이미 발생한 문제)를 통제 시점과 관리 방식으로 명확히 구분할 수 있는가?
- [ ] Ⅱ 절차: 위험 식별부터 감시까지 7개 프로세스의 활동과 핵심 산출물을 연결할 수 있는가?
- [ ] Ⅲ~Ⅳ 분석·대응: 정성/정량 분석 기법의 차이와 위협 5대(회피·완화 등) / 기회 5대(활용·증대 등) 전략을 대칭적으로 비교할 수 있는가?
- [ ] Ⅴ~Ⅵ 통제: 우발예비비와 관리예비비의 적용 대상 및 권한 차이를 설명하고, 2차 위험(Secondary Risk) 방어 수단을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [IT 감리](./008_it_audit.md)
- 연관 토픽: [WBS](./007_wbs.md), [PMO](./004_pmo.md), [CCPM](./112_critical_chain_toc.md)
- 다음 토픽: [BPR](./010_bpr.md)
