---
title: "프로젝트 위험관리"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 관리를 거쳐 프로젝트 위험관리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 관리</span>
  <strong>프로젝트 위험관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **프로젝트 위험관리(Project Risk Management)**는 프로젝트 목표에 영향을 미치는 미래 불확실성을 식별·분석하여 부정적 위협은 억제하고 긍정적 기회는 극대화하는 선제적 통제 활동
- 메커니즘: 위험 식별 ──▶ 정성적 분석(**P×I 매트릭스**) ──▶ 정량적 분석(**EMV** · **몬테카를로**) ──▶ 대응 전략 수립(위협 5대 · 기회 5대) ──▶ 감시
- 산출: 위험 등록부(Risk Register), 위협 대응(**회피·완화·전가·수용·상향**), 기회 대응(**활용·공유·증대·수용·상향**), **우발예비비** 및 **관리예비비** 통제

<div class="itpe-flow-map" role="img" aria-label="프로젝트 위험관리 식별·분석 및 대응 체계">
  <div class="itpe-flow-node">
    <strong>위험 식별 및 분석</strong>
    <small>위험 등록부 · P×I 정성 분석 · EMV/몬테카를로 정량 시뮬레이션</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>위험 성격에 따른 대응 전략 분기</small></div>
  <div class="itpe-flow-node is-current">
    <strong>위험 대응 전략 수립</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>위협(부정적)</strong><span><span class="itpe-keyword"><strong>회피</strong></span> · <span class="itpe-keyword"><strong>완화</strong></span> · <span class="itpe-keyword"><strong>전가</strong></span> · <span class="itpe-keyword"><strong>수용</strong></span> · <span class="itpe-keyword"><strong>상향</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>기회(긍정적)</strong><span><span class="itpe-keyword"><strong>활용</strong></span> · <span class="itpe-keyword"><strong>공유</strong></span> · <span class="itpe-keyword"><strong>증대</strong></span> · <span class="itpe-keyword"><strong>수용</strong></span> · <span class="itpe-keyword"><strong>상향</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>잔여 위험 감시 및 예비비 집행 통제</small></div>
  <div class="itpe-flow-node">
    <strong>우발예비비(Known-Unknowns) · 관리예비비(Unknown-Unknowns)</strong>
    <small>2차 위험(Secondary Risk) 방어 및 원가 기준선 사수</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **프로젝트 위험관리**: 프로젝트 생애주기 동안의 불확실성을 체계적으로 식별·분석하여 성공을 보증하는 활동
- **위험 등록부(Risk Register)**: 식별된 모든 위험의 원인, 사건, 영향, 확률, 영향도, 대응책, 담당자를 기록하는 문서
- **P×I 매트릭스**: 발생 확률(Probability)과 영향도(Impact)의 곱으로 위험 점수를 산출하여 우선순위를 등급화하는 정성적 도구
- **EMV(Expected Monetary Value)**: 각 시나리오의 발생 확률과 재무적 결과를 곱하여 가중 평균 기댓값을 산출하는 정량적 분석 기법
- **몬테카를로 시뮬레이션**: 난수 기반 컴퓨터 시뮬레이션으로 수천 회 반복 연산하여 공기 및 예산 달성 확률을 예측하는 기법
- **위협 5대 대응 전략**: 회피(Avoid), 완화(Mitigate), 전가(Transfer), 수용(Accept), 상향(Escalate)
- **기회 5대 대응 전략**: 활용(Exploit), 공유(Share), 증대(Enhance), 수용(Accept), 상향(Escalate)
- **우발예비비(Contingency Reserve)**: 식별된 잔여 위험(Known-Unknowns)에 대비하여 PM 권한으로 원가 기준선에 배정하는 예비비
- **관리예비비(Management Reserve)**: 미식별 위험(Unknown-Unknowns)에 대비하여 최고경영진 권한으로 총예산에 배정하는 예비비
- **2차 위험(Secondary Risk)**: 특정 위험 대응책을 실행함으로써 부수적으로 새롭게 발생하는 또 다른 위험

</details>

## 예상문제

> 프로젝트 위험관리의 개념 및 6단계 절차를 설명하고, 부정적 위험(위협) 대응 전략 5가지와 긍정적 위험(기회) 대응 전략 5가지를 비교 설명한 후, 예비비(Reserve) 관리 및 2차 위험(Secondary Risk) 통제 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **위험관리(Risk Management)** | 프로젝트 목표를 위협하는 불확실성을 식별·분석·대응·감시하는 전사 및 프로젝트 위험 통제 체계 | Ⅱ. 6단계 프로세스, Ⅳ. 위협·기회 대응 |

## Ⅰ. 불확실성을 선제적으로 통제하는 프로젝트 위험관리의 개요

> 위험관리는 사후 수습이 아닌 미래 불확실성에 대한 선제적 개입이며, 성패는 단순 등록부 작성이 아닌 **실질적 조기경보 트리거**와 **예비비 통제력**으로 판정한다.

- 정의: 프로젝트 생애주기 동안 목표 달성에 영향을 미치는 불확실성을 식별·분석하여 **위협(Threat)**의 악영향은 최소화하고 **기회(Opportunity)**는 극대화하는 **선제적 통제 활동**
- 목적: 소방수식 사후 수습(Fire-fighting) 탈피 및 프로젝트 성공률 제고 → 일정 지연 및 원가 초과 방지, **원가 기준선(Cost Baseline)** 사수

## Ⅱ. 위험관리 구성체계 및 6단계 프로세스

> 계획부터 감시까지 단계별 폐루프 통제를 통해 잠재 위험이 현실의 이슈로 비화되는 것을 차단한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="위험관리 6단계 프로세스 활동 및 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 위험관리 계획 수립</strong></span>
    <small>관리 방법론 · RACI 책임 매트릭스 · 예비비 책정 기준 정의<br />→ 위험관리 계획서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 위험 식별</strong></span>
    <small>잠재 위험 요인 도출 · 위험의 원인-사건-영향 구조화<br />→ 위험 등록부(초안)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 정성적 위험 분석</strong></span>
    <small>발생 확률(P)과 영향도(I) 평가 · 우선순위 등급화(상·중·하)<br />→ P×I 매트릭스 · 감시대상 목록</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 정량적 위험 분석</strong></span>
    <small>기대화폐가치(EMV) 산출 · 몬테카를로 일정/비용 확률 시뮬레이션<br />→ 정량 분석 보고서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 위험 대응 계획 수립</strong></span>
    <small>위협 5대 전략 및 기회 5대 전략 확정 · 트리거 설정 및 예비비 할당<br />→ 위험 등록부(대응계획 반영)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑥ 위험 감시 및 통제</strong></span>
    <small>조기경보 트리거 모니터링 · 비상대책(Workaround) 실행 · 위험 재평가<br />→ 위험 감사 보고서 · 프로젝트 교훈집</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>위험 통제 루프</strong></span> · P×I 정성 분석 ↔ EMV 정량 분석 ↔ 위협/기회 대응 ↔ 우발/관리예비비 집행 통제</div>

## Ⅲ. 위험 분석 기법: 정성적 분석 vs 정량적 분석

> P×I 정성 분석으로 신속히 우선순위를 좁히고, EMV와 몬테카를로 정량 분석으로 객관적 예비비 규모를 산출한다.

| 분석 기법 | 주요 분석 도구 | 분석 메커니즘 | 실무 적용 목적 |
|---|---|---|---|
| **정성적 분석** | **P×I 매트릭스**, 위험 데이터 품질 평가 | 확률과 영향도를 등급(1~5점)으로 평가하여 위험 점수 산출 | 위험 우선순위 지정 및 고위험군 집중 관리 |
| **정량적 분석** | **기대화폐가치(EMV)**, **몬테카를로 시뮬레이션** | 확률 분포 난수 기반 반복 연산 및 확률 $\times$ 금액 가중평균 | 필요 예비비 산출 및 준공 확률 구간 도출 |

## Ⅳ. 위험 대응 전략: 부정적 위험(위협) vs 긍정적 위험(기회) 대칭 비교

> 위협은 회피·완화·전가·수용·상향으로 차단하고, 기회는 활용·공유·증대·수용·상향으로 비즈니스 가치를 극대화한다.

| 전략 관점 | 부정적 위험 (위협: Threat) 대응 전략 | 긍정적 위험 (기회: Opportunity) 대응 전략 |
|---|---|---|
| **원인 통제** | **회피 (Avoid)**: 계획을 변경하여 위협 원인을 원천 제거 (예: 미검증 솔루션 제외) | **활용 (Exploit)**: 기회의 실현 가능성을 100% 확정 (예: 최우수 핵심 인력 조기 투입) |
| **영향 조절** | **완화 (Mitigate)**: 발생 확률이나 악영향을 임계치 이하로 축소 (예: 다중화 구성) | **증대 (Enhance)**: 기회의 발생 확률이나 긍정적 영향을 적극 확대 (예: 자원 추가 집중) |
| **제3자 협업** | **전가 (Transfer)**: 위험의 책임과 손실을 제3자에게 이전 (예: 보험 가입, 외주 계약) | **공유 (Share)**: 이익을 극대화할 제3자와 협력 (예: 전문사와 컨소시엄 구성) |
| **자연 대응** | **수용 (Accept)**: 계획 변경 없이 인정 (능동적: 우발예비비 편성, 수동적: 사후 조치) | **수용 (Accept)**: 추가 조치 없이 기회가 발생하면 그 이익을 자연 취득 |
| **권한 상향** | **상향 (Escalate)**: PM 권한을 초과하는 리스크를 최고경영진/PMO로 이관 | **상향 (Escalate)**: 조직 전체에 이익이 되는 대형 기회를 경영진으로 이관 |

## Ⅴ. 위험관리 실효성 확보를 위한 실무 위험과 통제 대책

> 등록부 사장화와 2차 위험을 차단하기 위해 실시간 트리거 모니터링과 예비비 엄격 분리가 필수적이다.

| 위험 현상 | 발생 원인 | 통제 대책 | 검증 기준 |
|---|---|---|---|
| **위험 등록부의 사장화** | 사업 초기에 일회성 작성 후 주간 회의 점검 생략 | 주간 PMO 회의 의무 안건 상정 및 실시간 트리거 관제 연동 | 미식별 돌발 장애 0건 |
| **예비비 관리 혼선** | 예비비 성격 구분 부재로 임의 지출 및 분쟁 발생 | **우발예비비(PM 권한: 잔여위험)**와 **관리예비비(경영진 권한: 미지의 위험)** 분리 | 예비비 승인 전결권 준수 |
| **2차 위험 (Secondary Risk)** | 외주 전가 등 대응책 실행 과정에서 새로운 위험 파생 | 대응 전략 수립 시 2차 위험 영향 평가를 선결 조건으로 의무화 | 대응책 파생 결함 0건 |

## Ⅵ. AI 기반 지능형 위험 관제를 위한 기술사적 제언

> 수기 작성을 탈피하여 코드 커밋과 결함 추이에 기반한 **실시간 AI 조기경보 위험 관제** 체계로 전환해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 뛰어난 프로젝트 관리자는 위험이 전혀 없는 환경을 만드는 사람이 아니라, 불확실성을 정량화하여 '수용 가능한 범위 내로 길들이는(Taming the Risks)' 리스크 엔지니어임. 또한 위협 방어를 넘어 시장 기회를 적극 포착하는 것이 프로젝트 ROI를 극대화하는 열쇠임.
- 나라면: Jira 및 Git 형상 관리와 연동된 실시간 위험 관제 대시보드를 구축하고, 빌드 실패율과 결함 잔존 추이를 AI로 분석하여 위험 임계치를 초과할 때 우발예비비 집행과 PMO 에스컬레이션이 자동으로 트리거되는 '지능형 자동화 위험 감시 체계'를 구현하겠음.

### 실전 답안용 기술사적 제언

- 판정: 정적 문서 중심의 사후 대응을 탈피하고 데이터 기반 실시간 사전 위험 조기경보 체계 확립
- 대안: **지능형 자동화 위험 관제 플랫폼** 및 **2차 위험 사전 평가 프로세스** 제도화
- 검증: 위험 트리거 감지 즉시 대응 개시율 100% · 예비비 한도 내 원가 집행 완결
- 효과: 돌발 장애 및 프로젝트 납기 지연 원천 차단, 원가 기준선 사수

<div class="itpe-pipeline is-vertical" role="img" aria-label="지능형 위험관리 체계 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>문서 사장화 · 소방수식 사후 수습 · 2차 위험 미식별로 인한 파행</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>AI 기반 위험 조기경보 관제 + 우발/관리 예비비 엄격 분리 운용</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>위험 등록부 실시간 동기화 · 2차 위험 사전 영향 평가율 100%</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>일정 지연 및 원가 초과 차단 · 프로젝트 기준선 사수 및 성공 완주</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **프로젝트 위험관리**는 프로젝트 생애주기 동안의 불확실성을 식별·분석하여 **위협은 최소화**하고 **기회는 극대화**하는 **선제적 통제 활동**
- 목적: 소방수식 대응 탈피 및 프로젝트 성공률 제고 → **원가 기준선(Cost Baseline)** 및 납기 사수

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="위험관리 6단계 요약">
  <div class="itpe-pipeline-node"><strong>위험 식별</strong><small>위험 등록부 작성</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>정성적 분석</strong><small>P×I 매트릭스</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>정량적 분석</strong><small>EMV · 몬테카를로</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>대응 전략 수립</strong><small>위협 5대 · 기회 5대</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>위험 감시</strong><small>트리거 관제 · 예비비 통제</small></div>
</div>

### 3. 핵심 통제

- **대응 전략**: 위협(**회피·완화·전가·수용·상향**) ↔ 기회(**활용·공유·증대·수용·상향**)
- **예비비 통제**: **우발예비비(Known-Unknowns, PM)** ↔ **관리예비비(Unknown-Unknowns, 경영진)**

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 1교시: 위험관리 계획 및 P×I 정성적 분석
- 제138회 정보관리기술사 2교시: 부정적 위험(위협)과 긍정적 위험(기회) 대응 전략 비교
- 제139회 정보관리기술사 1교시: 우발예비비와 관리예비비의 차이점 및 관리 방안
- PMI, PMBOK Guide 7th Edition, Project Risk Management Knowledge Area

## 학습 체크

- [ ] 위험(Risk)과 이슈(Issue)의 본질적 차이점을 설명할 수 있는가?
- [ ] 부정적 위험 대응 전략 5가지와 긍정적 위험 대응 전략 5가지를 대칭적으로 비교할 수 있는가?
- [ ] 우발예비비(Contingency Reserve)와 관리예비비(Management Reserve)의 차이점을 통제 주체와 대상 관점에서 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [IT 감리](./008_it_audit.md)
- 연관 토픽: [WBS](./007_wbs.md), [PMO](./004_pmo.md), [CCPM](./086_ccpm.md)
- 다음 토픽: [BPR](./010_bpr.md)
