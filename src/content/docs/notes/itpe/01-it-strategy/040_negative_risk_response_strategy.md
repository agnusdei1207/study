---
title: "부정적 위험 대응 전략"
author: "Codex"
date: "2026-09-20T19:35:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 위험관리를 거쳐 부정적 위험 대응 전략으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 위험관리</span>
  <strong>부정적 위험 대응 전략</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **부정적 위험 대응 전략(Negative Risk Response Strategy)**은 프로젝트 목표를 저해하는 위협(Threat)에 대응하여 발생 확률과 충격을 억제하기 위해 **회피, 완화, 전가, 수용, 상위보고** 5대 전략을 수립하는 **PMBOK** 위험관리 체계
- 메커니즘: 확률-영향 매트릭스(**P-I Matrix**)로 위협 등급을 평가하고 최적 전략을 선정한 뒤, 대책 실행 후 남은 **잔여 위험(Residual Risk)**과 파생된 **2차 위험(Secondary Risk)**을 지속 통제
- 산출: 위험 관리대장(**Risk Register**) · 비상대책(**Contingency Plan**) · 비상예비비 배정 명세서 · 갱신된 **WBS**

<div class="itpe-flow-map" role="img" aria-label="부정적 위험 식별 및 P-I 매트릭스 기반 5대 전략 선택과 모니터링 흐름">
  <div class="itpe-flow-node">
    <strong>위험 식별 및 정량 분석</strong>
    <small>리스크 레지스터 등록 · P-I 매트릭스 · EMV 산출</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>위험 등급 및 비용-편익 평가</small></div>
  <div class="itpe-flow-node is-current">
    <strong>부정적 위험 5대 대응 전략</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>회피</strong><span><span class="itpe-keyword"><strong>Avoid</strong></span>: 근본 원인 제거 · 불확실한 기능 범위 제외</span></div>
      <div class="itpe-flow-branch"><strong>완화</strong><span><span class="itpe-keyword"><strong>Mitigate</strong></span>: 발생 확률 축소 · 프로토타입 조기 검증</span></div>
      <div class="itpe-flow-branch"><strong>전가</strong><span><span class="itpe-keyword"><strong>Transfer</strong></span>: 손실 책임 제3자 이전 · 고정가 계약 · 보험</span></div>
      <div class="itpe-flow-branch"><strong>수용</strong><span><span class="itpe-keyword"><strong>Accept</strong></span>: 비상예비비(<span class="itpe-keyword"><strong>Contingency</strong></span>) 배정 및 우회 감수</span></div>
      <div class="itpe-flow-branch"><strong>보고</strong><span><span class="itpe-keyword"><strong>Escalate</strong></span>: PM 권한 초과 외생 위험 상위 이관</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>대책 실행 및 사후 감시</small></div>
  <div class="itpe-flow-node">
    <strong>잔여 및 2차 위험 통제</strong>
    <small><span class="itpe-keyword"><strong>Residual Risk</strong></span> 감시 · <span class="itpe-keyword"><strong>Secondary Risk</strong></span> 조기 통제</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **부정적 위험 대응 전략(Negative Risk Response Strategy)**: 프로젝트에 부정적 영향을 미치는 위협을 억제·통제하기 위해 PMBOK이 정의한 5대 대응 메커니즘
- **회피(Avoid)**: 위험을 유발하는 근본 원인을 제거하거나 프로젝트 범위를 변경하여 위험 발생 확률을 완전히 0으로 만드는 전략
- **완화(Mitigate)**: 위험의 발생 확률을 낮추거나 현실화 시 영향도를 조직의 수용 가능한 한도 내로 축소하는 전략
- **전가(Transfer)**: 위험의 결과와 재무적 책임을 제3자에게 이전하고 리스크 프리미엄을 지불하는 전략(외주 턴키 계약, 하자보증보험 등)
- **수용(Accept)**: 대응 비용이 잠재 손실보다 크거나 대안이 없을 때 위험을 인정하고 능동적(예비비 편성) 또는 수동적으로 감수하는 전략
- **상위보고(Escalate)**: 프로젝트 관리자의 통제 권한을 벗어나는 프로그램/조직 레벨의 외생적 위협을 스폰서나 경영진에 공식 이관하는 전략
- **잔여 위험(Residual Risk)**: 위험 대응 전략을 실행한 후에도 완전히 소멸되지 않고 여전히 남아 있는 잔존 위험
- **2차 위험(Secondary Risk)**: 특정 위험 대응책을 실행함으로써 새로운 부작용으로 파생되어 발생하는 2차적 위험
- **EMV(Expected Monetary Value)**: 위험의 발생 확률과 발생 시 재무적 영향도를 곱하여 산출하는 기대화폐가치
- **Contingency Reserve(비상예비비)**: 식별되어 능동적으로 수용된 위험(Known-Unknowns)에 대비하여 사전에 배정한 예산 및 일정 버퍼

</details>

## 예상문제

> IT 프로젝트 관리에서 발생할 수 있는 부정적 위험(Negative Risk / Threat)의 개념과 PMBOK 7th 기준 5대 대응 전략을 설명하고, 잔여 위험(Residual Risk) 및 2차 위험(Secondary Risk)의 공학적 관리 방안을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **리스크 대응 (Risk Response)** | 위협과 기회에 대한 선제적 처리 계획 수립 및 위험 책임자(Risk Owner) 지정 | Ⅱ 전략, Ⅳ 절차 |
| **비상예비비 (Contingency Reserve)** | 식별되어 수용된 위험이 현실화되었을 때 투입하기 위해 사전 배정된 예산 및 공기 버퍼 | Ⅲ 매트릭스, Ⅵ 통제 |

## Ⅰ. 프로젝트 성공을 위한 선제적 방어선, 부정적 위험 대응 전략의 개요

> 위험 대응은 엑셀 대장에 기록하는 요식 행위가 아니라 위협의 조기 무력화 활동이며, 성패는 대응책 실행 후 파생되는 **2차 위험(Secondary Risk)**과 **잔여 위험(Residual Risk)**의 폐쇄 루프 통제로 판정함.

- 정의: 프로젝트 목표 달성을 저해하는 불확실한 사건(위협)에 대해 발생 확률을 낮추거나 피해를 줄이기 위해 **회피, 완화, 전가, 수용, 상위보고**를 수립·실행하는 **PMBOK 위험관리 체계**
- 목적: 위협의 조기 무력화 및 충격 최소화 → 조직의 위험 허용 한도(**Risk Tolerance**) 내에서 안정적인 프로젝트 완주 보증

## Ⅱ. PMBOK 5대 부정적 위험 대응 전략 체계

> 위험의 성격, 통제 가능 여부, 비용 대비 효과를 고려하여 최적 전략을 선택함.

| 전략 유형 | 핵심 행동 메커니즘 | 실무 적용 사례 | 의사결정 기준 |
|---|---|---|---|
| **1. 회피 (Avoid)** | 위협을 유발하는 근본 원인을 제거하거나 프로젝트 계획을 변경 | 불확실한 요구사항 기능 범위 제외, 미검증 신기술 도입 철회 | 확률과 영향도가 모두 치명적인 위험 |
| **2. 완화 (Mitigate)** | 위협의 발생 확률을 낮추거나 발생 시 충격(영향도)을 축소 | 사전 프로토타입(PoC) 검증, 테스트 자동화, 장비 이중화 | 발생 확률이 높으나 공학적 통제가 가능한 위험 |
| **3. 전가 (Transfer)** | 위협의 결과와 책임을 제3자에게 이전하고 리스크 프리미엄 지불 | 고정가(FP) 턴키 계약, 하자이행보증보험 가입, 클라우드 SLA 연계 | 영향도는 크나 발생 빈도가 낮은 재무적 위험 |
| **4. 수용 (Accept)** | 위험을 인지하되 별도의 사전 조치를 취하지 않고 감수 | 능동적 수용: 비상예비비(Contingency) 배정 / 수동적: 사후 우회 | 대응 비용이 기대 손실(**EMV**)보다 클 때 |
| **5. 상위보고 (Escalate)** | PM의 권한 범위를 초과하는 외생적 위협을 상위 조직에 이관 | 관련 법령 개정, 전사 예산 삭감 이슈를 스폰서에게 이관 | 프로젝트 경계를 벗어난 거시적 환경 위험 |

## Ⅲ. 확률-영향 매트릭스(P-I Matrix) 기반 전략 선택 매핑

> P-I 매트릭스 상의 위험 등급에 따라 비용 대비 효과가 가장 높은 전략을 매핑함.

| 영역 구분 | 발생확률 / 영향도 | 권장 전략 | 위험 처리 가이드라인 |
|---|---|---|---|
| **고위험 영역 (Red Zone)** | 고확률 / 고영향 | **회피 (Avoid)** | 설계를 변경하거나 범위를 축소하여 위험 발생 경로를 원천 차단 |
| **재무위험 영역 (Yellow)** | 저확률 / 고영향 | **전가 (Transfer)** | 계약 및 보험 제도를 활용하여 재정적 피해를 외부에 이전 |
| **공정위험 영역 (Yellow)** | 고확률 / 저영향 | **완화 (Mitigate)** | 단위테스트, 코드리뷰, 교육 등 엔지니어링 통제를 통해 위험도 감축 |
| **저위험 영역 (Green Zone)** | 저확률 / 저영향 | **수용 (Accept)** | 주기적 감시만 수행하고 발생 시 **비상예비비(Contingency)**로 대응 |
| **외생위험 영역 (External)** | 권한 초과 위험 | **상위보고 (Escalate)** | 프로젝트 관리자 권한 밖의 이슈를 스폰서 및 프로그램 레벨로 공식 이관 |

## Ⅳ. 부정적 위험 대응 5단계 엔지니어링 프로세스

> 위험 식별에서 출발하여 전략 선정, 실행 계획 수립, 조치 실행, 잔여·2차 위험 모니터링으로 이어지는 폐쇄 루프를 구성함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="부정적 위험 대응 5단계 엔지니어링 프로세스 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 위험 식별 및 정량 분석</strong></span>
    <small>정성적·정량적 분석 · 기대화폐가치(EMV = 확률 × 영향) 도출<br />→ 위험 관리대장(Risk Register)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 최적 대응전략 선정</strong></span>
    <small>비용 편익(Cost-Benefit) 평가 · 회피/완화/전가/수용/보고 결정<br />→ 리스크 대응 전략 명세서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 실행 계획 수립 및 WBS 반영</strong></span>
    <small>대응 활동 WBS 패키지 추가 · 위험 책임자(Risk Owner) 지정<br />→ 갱신된 WBS · 책임할당표(RACI)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 비상대책 실행</strong></span>
    <small>비상예비비(Contingency Reserve) 투입 · 우회 대책(Workaround) 가동<br />→ 예비비 집행 전표 · 작업 승인서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 잔여 및 2차 위험 모니터링</strong></span>
    <small>조치 후 잔여 위험(Residual) 추적 · 파생된 2차 위험(Secondary) 재평가<br />→ 리스크 감사 보고서 · 추세 차트</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Closed-Loop Risk Control</strong></span> · 대책 실행 후 남은 잔여 위험과 파생된 2차 위험을 위험 대장에 재등록하여 지속 감시</div>

## Ⅴ. 부정적 위험(위협) vs 긍정적 위험(기회) 대응 전략 비교

> 위협 대응과 기회 대응은 손실 최소화와 이익 극대화라는 동전의 양면 관계를 이룸.

| 구분 기준 | 부정적 위험 (Threats / 위협) | 긍정적 위험 (Opportunities / 기회) | 대칭 메커니즘 |
|---|---|---|---|
| 적극 대책 | **회피 (Avoid)**: 불확실성 원천 제거로 영향 차단 | **활용 (Exploit)**: 기회가 반드시 발생하도록 불확실성 제거 | 발생 여부의 확실성 통제 |
| 확률 조정 | **완화 (Mitigate)**: 발생 확률이나 부정적 충격 감소 | **증대 (Enhance)**: 발생 확률이나 긍정적 영향 규모 확대 | 영향도 및 빈도 통제 |
| 파트너십 | **전가 (Transfer)**: 손실 책임을 제3자에게 이전 (외주, 보험) | **공유 (Share)**: 기회 포착을 위해 제3자와 파트너십/합작 | 제3자 역량 레버리지 |
| 소극 대책 | **수용 (Accept)**: 손실을 인정하고 비상예비비 배정 | **수용 (Accept)**: 별도 조치 없이 기회가 오면 누림 | 현상 유지 및 사후 대응 |
| 권한 초과 | **상위보고 (Escalate)**: 스폰서 레벨로 위험 이관 | **상위보고 (Escalate)**: 스폰서 레벨로 기회 이관 | 프로젝트 경계 초과 처리 |

## Ⅵ. 실무 위험관리 실패 요인과 공학적 통제 방안

> 2차 위험과 무분별한 수동적 수용을 통제하지 못하면 프로젝트는 치명적 장애에 직면함.

| 위험 요인 | 발생 원인 | 공학적·관리적 통제 대책 | 검증 지점 |
|---|---|---|---|
| 수동적 수용 방치 | 위험 수용을 무대책으로 오해하여 장애 발생 시 패닉 | **비상예비비(Contingency)** 편성 및 우회 매뉴얼(**Workaround**) 수립 | 장애 발생 즉시 복구 절차 가동 확인 |
| 외주 전가 2차 위험 | 핵심 개발을 외주 전가했으나 협력사 부실로 납기 지연 | **2차 위험 분석** 의무화 및 외주사에 대한 상시 품질 감리 병행 | 협력사 품질 지표 및 공정 진척 확인 |
| 완화 비용 역전 | 위험 발생 잠재 손실보다 완화 조치 비용이 더 큼 | **EMV** 분석 기반 `완화 투입 비용 < 기대 손실` 기준 엄격 적용 | 비용 대비 위험 절감 효율성 검증 |
| 상위보고 회피 | 인사 고과 불이익 우려로 중대 위험을 내부 은폐 | 에스컬레이션 임계치(일정 지연 2주 등)를 프로젝트 헌장에 명문화 | 조기 보고 및 전사 지원 확보율 100% |

## Ⅶ. 잔여 위험 통제와 데이터 기반 리스크 관리 중심의 기술사적 제언

> 위험 관리는 한 번 수립하고 덮어두는 문서가 아니며, 조치 후 남은 잔여 위험과 새로 태어난 2차 위험을 끝까지 추적 통제하는 동적 엔지니어링이어야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 위험 대응에서 가장 흔한 실패는 '전가'와 '완화'를 실행한 후 위험이 완전히 끝났다고 방심하는 데 있음. 핵심 모듈을 외주사로 전가하면 '협력사 부실'이라는 2차 위험이 태어나고, 아키텍처를 완화하면 '복잡도 증가'라는 잔여 위험이 남으므로 이를 다시 리스크 대장에 등록해 감시해야 함.
- 나라면: 프로젝트 착수 단계에서 `위험별 단일 책임자(Risk Owner) 지정 → Jira/Git 연동 실시간 리스크 대시보드 구축 → 매 스프린트 종료 시 잔여 위험 재평가 및 비상예비비 잔액 리뷰 의무화`를 프로젝트 거버넌스 헌장에 명문화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 단발성 위험 등록 탈피 및 잔여·2차 위험의 지속적 폐쇄 루프 통제
- 대안: **P-I Matrix-EMV-Closed Loop Dashboard** 3단계 위험 거버넌스 구현
- 검증: 리스크 오너 100% 지정 · 2차 위험 사전 식별률 100% · 비상예비비 소진율 통제
- 효과: 프로젝트 납기 및 예산 리스크 원천 차단과 안정적 완주성 담보

<div class="itpe-pipeline is-vertical" role="img" aria-label="부정적 위험 대응 거버넌스 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>문서상 대장 방치 · 수동적 수용 패닉 · 외주 전가에 따른 2차 위험 미인지</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>P-I 기반 5대 전략 매핑 + 비상예비비 편성 + 2차 위험 폐쇄 루프 감시</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>EMV 기반 비용 효율성 확인 · 에스컬레이션 임계치 준수</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>위험의 조기 무력화 · 예산 및 공기 보호 · 성공적 프로젝트 완주</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **부정적 위험 대응 전략(Negative Risk Response Strategy)**은 프로젝트 목표를 저해하는 위협에 대해 발생 확률과 충격을 억제하기 위해 **회피, 완화, 전가, 수용, 상위보고** 5대 전략을 수립하는 **PMBOK 위험관리 체계**
- 목적: 위협의 조기 무력화 및 피해 최소화 → 위험 허용 한도 내 안정적 프로젝트 완주 보증

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="부정적 위험 대응 프로세스 요약">
  <div class="itpe-pipeline-node"><strong>위험 분석</strong><small>P-I 매트릭스 · EMV 산출</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>전략 선정</strong><small>회피 · 완화 · 전가 · 수용 · 보고</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>계획 반영</strong><small>WBS 추가 · 리스크 오너 지정</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>대책 실행</strong><small>비상예비비 투입 · 우회 대책</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>사후 감시</strong><small>잔여 위험 · 2차 위험 통제</small></div>
</div>

### 3. 핵심 통제

- **5대 대응 전략**: 회피(원인 제거), 완화(확률/영향 축소), 전가(제3자 이전), 수용(비상예비비 운용), 상위보고(스폰서 이관)
- **사후 폐쇄 루프**: 대책 실행 후 남은 **잔여 위험(Residual Risk)**과 파생된 **2차 위험(Secondary Risk)**을 위험 대장에 재등록하여 지속 감시

## 출제 이력과 검증 출처

- 제139회 정보관리기술사 1교시 4번: IT 프로젝트에서 발생할 수 있는 부정적 위험과 대응 전략
- 제134회 정보관리기술사 1교시: 프로젝트 위험 대응 전략
- PMI, [A Guide to the Project Management Body of Knowledge (PMBOK Guide) 7th Edition](https://www.pmi.org)
- ISO, [ISO 31000:2018, Risk management — Guidelines](https://www.iso.org)

## 학습 체크

- [ ] PMBOK 7th 기준 5대 부정적 위험 대응 전략(회피, 완화, 전가, 수용, 상위보고)을 설명할 수 있는가?
- [ ] 확률-영향 매트릭스(P-I Matrix)의 각 분면별 최적 전략을 제시할 수 있는가?
- [ ] 잔여 위험(Residual Risk)과 2차 위험(Secondary Risk)의 차이점과 관리 방안을 기술할 수 있는가?
- [ ] 부정적 위험 대응 전략과 긍정적 위험 대응 전략을 대칭적으로 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [공공 SW 사업 발주·계약](./039_public_sw_contract.md)
- 연관 토픽: [프로젝트 위험관리](./009_project_risk_management_negative.md), [ISO 31000](./069_iso_31000.md), [정량적 위험분석](./073_quantitative_risk_analysis.md), [갈등관리](./035_conflict_management.md), [EVM](./032_evm.md)
- 다음 토픽: [린 소프트웨어 개발](./041_lean_software_development.md)
