---
title: "갈등관리"
author: "Codex"
date: "2026-09-20T19:31:00+09:00"
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

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 프로젝트 조직과 이해관계자 관리를 거쳐 갈등관리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>프로젝트 관리·이해관계자</span>
  <strong>갈등관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **갈등관리(Conflict Management)**는 프로젝트 수행 중 발생하는 목표·자원·기술적 견해차를 조기 식별하고, 과업 갈등은 건설적 혁신으로 유도하며 관계 갈등은 최소화하는 이해관계자 통제 프로세스
- 메커니즘: **Thomas-Kilmann 모델**의 2대 축(**Assertiveness**, **Cooperativeness**)을 기준으로 5대 모드(협력, 경쟁, 타협, 회피, 수용)를 적용하고, '사람'과 '문제'를 분리하여 합의안 도출
- 산출: 이해관계자 이슈 로그 · 기술 검증(**PoC**) 및 아키텍처 결정 기록(**ADR**) · 갈등 중재 합의안 · 갱신된 **WBS/RACI**

<div class="itpe-flow-map" role="img" aria-label="갈등 발생 감지부터 Thomas-Kilmann 모델 적용 및 기준선 반영 흐름">
  <div class="itpe-flow-node">
    <strong>갈등 발생 징후 감지</strong>
    <small>요구사항 범위 · 자원 경합 · 아키텍처 견해차</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>사람과 문제의 분리 (Fact 규명)</small></div>
  <div class="itpe-flow-node is-current">
    <strong>Thomas-Kilmann 5대 갈등 대응 모델</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>협력</strong><span><span class="itpe-keyword"><strong>Collaborating</strong></span>: Win-Win 통합 해결책 모색 (최우선)</span></div>
      <div class="itpe-flow-branch"><strong>경쟁</strong><span><span class="itpe-keyword"><strong>Competing</strong></span>: 긴급·보안·안전 원칙 관철 (Zero-sum)</span></div>
      <div class="itpe-flow-branch"><strong>타협</strong><span><span class="itpe-keyword"><strong>Compromising</strong></span>: 상호 양보를 통한 현실적 절충</span></div>
      <div class="itpe-flow-branch"><strong>회피</strong><span><span class="itpe-keyword"><strong>Avoiding</strong></span>: 사소한 이슈 방치 및 감정 냉각기 확보</span></div>
      <div class="itpe-flow-branch"><strong>수용</strong><span><span class="itpe-keyword"><strong>Accommodating</strong></span>: 장기 파트너십 보호를 위한 양보</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>기술 검증(PoC) 및 합의 도출</small></div>
  <div class="itpe-flow-node">
    <strong>프로젝트 기준선 반영</strong>
    <small><span class="itpe-keyword"><strong>ADR</strong></span> 문서화 · WBS 및 RACI 갱신 · 재발 방지 모니터링</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **갈등관리(Conflict Management)**: 프로젝트 이해관계자 간의 충돌과 견해차를 조기에 진단하고 조직의 목표 달성에 기여하도록 조정하는 관리 기법
- **Thomas-Kilmann 모델(TKI)**: 자기주장성과 협조성의 2차원 축을 기반으로 갈등 대응 행동을 5가지 유형(협력, 경쟁, 타협, 회피, 수용)으로 구조화한 프레임워크
- **Assertiveness(자기주장성)**: 갈등 상황에서 자신의 입장, 목표, 관심사를 관철하려는 성향의 강도
- **Cooperativeness(협조성)**: 갈등 상황에서 타인의 관심사와 요구를 배려하고 충족시키려는 성향의 강도
- **과업 갈등(Task Conflict)**: 프로젝트 목표, 요구사항 범위, 아키텍처 기술 스택 등에 대한 생산적이고 건설적인 업무상 이견
- **관계 갈등(Relationship Conflict)**: 성격 차이, 의사소통 스타일, 상호 불신에서 기인하는 파괴적인 감정적 대립
- **프로세스 갈등(Process Conflict)**: 역할 분담(R&R)과 업무 수행 절차, 자원 배분 방식을 둘러싼 절차적 마찰
- **ADR(Architectural Decision Record)**: 기술 아키텍처 갈등 발생 시 최종 의사결정의 맥락, 대안 비교, 채택 이유를 명시한 공학적 의사결정 문서
- **하버드 협상 원칙(PON)**: 사람과 문제를 분리하고, 입장이 아닌 본질적 이해관계에 집중하여 객관적 기준을 통해 상호 이익을 창출하는 협상 프레임워크

</details>

## 예상문제

> 소프트웨어 프로젝트 진행 중 발생하는 갈등의 주요 원인과 3대 유형을 설명하고, 토마스-킬만(Thomas-Kilmann)의 5대 갈등 대응 모델과 상황별 적용 방안 및 PM의 공학적 중재 전략을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **프로젝트 갈등관리** | 과업·관계·프로세스 갈등의 원인 규명 및 Thomas-Kilmann 5대 모드 기반의 공학적 통제 | Ⅱ 유형, Ⅲ 모델, Ⅳ 절차 |
| **하버드 협상 원칙(PON)** | 사람과 문제의 분리, 입장이 아닌 이해관계 집중, 객관적 기준을 활용한 합의 도출 | Ⅳ 절차, Ⅴ 비교, Ⅶ 결론 |

## Ⅰ. 위기를 팀 성장의 기회로 전환하는 갈등관리의 개요

> 갈등관리는 갈등의 완전한 소멸이 아니라 감정적 **관계 갈등**을 차단하고 건설적 **과업 갈등**을 유도하는 활동이며, 성패는 객관적 팩트 기반의 **합의 기준선(Baseline)** 확립으로 판정함.

- 정의: 프로젝트 목표 달성 과정에서 발생하는 이해관계자 간의 대립과 이견을 조기에 식별하고 **Thomas-Kilmann 모델**을 통해 조정하는 **프로젝트 관리 프로세스**
- 목적: 파괴적인 **관계 갈등(Relationship Conflict)** 조기 차단 및 생산적인 **과업 갈등(Task Conflict)** 유도 → 팀 응집력 강화 및 시스템 품질 극대화

## Ⅱ. 갈등의 3대 유형과 주요 발생 원인

> 과업 갈등은 적정 수준으로 유도하여 품질을 높이고, 관계 갈등은 무관용 원칙으로 조기 차단하며, 프로세스 갈등은 룰(Rule)로 해결함.

| 갈등 유형 | 핵심 원인 및 성격 | 프로젝트에 미치는 영향 | 관리 및 통제 방향 |
|---|---|---|---|
| **과업 갈등 (Task)** | 요구사항 범위, 아키텍처 설계, 기술 스택 선정에 대한 이견 | 적정 수준 유지 시 창의적 대안 발굴 및 품질 향상 | 적극적 기술 토론 및 **PoC** 실증 검증 유도 |
| **관계 갈등 (Relationship)** | 성격 차이, 의사소통 스타일 불일치, 상호 불신 및 감정 대립 | 팀 사기 저하, 의사소통 단절, 생산성 급락 | 감정 분리 1:1 상담 및 무관용 중재 원칙 적용 |
| **프로세스 갈등 (Process)** | 과업 수행 절차, 책임 할당(R&R), 자원 배분 기준에 대한 마찰 | 작업 지연, 책임 전가(핑퐁), 일정 병목 발생 | **RACI 매트릭스** 정립 및 공식 워크플로우 확정 |

## Ⅲ. Thomas-Kilmann 5대 갈등 해결 모델 아키텍처

> **자기주장성(Assertiveness)**과 **협조성(Cooperativeness)**의 2차원 축을 기준으로 상황에 맞는 최적의 모드를 선택함.

| 대응 모드 | 행동적 특성 | 최적 적용 상황 (Best Practice) | 주의점 및 부작용 |
|---|---|---|---|
| **협력 (Collaborating)** | 자기주장과 협조성이 모두 높은 Win-Win 대안 추구 | 양측의 쟁점이 모두 중요하여 타협할 수 없고 시간이 충분할 때 | 많은 시간과 높은 신뢰, 커뮤니케이션 비용 소요 |
| **경쟁 (Competing)** | 자신의 입장을 강하게 관철하는 독단적·비협조적 접근 | 보안 규정 준수, 긴급 장애 복구 등 타협 불가능한 원칙 준수 시 | 패자의 반발, 팀워크 훼손 및 적대감 유발 위험 |
| **타협 (Compromising)** | 중간 수준의 주장과 협조를 통한 상호 절충안 마련 | 마감 시한이 임박하고 동등한 권한을 가진 당사자 간 대립 시 | 미봉책에 그쳐 차후 동일 이슈가 재발할 위험 |
| **회피 (Avoiding)** | 갈등을 인지하고도 개입을 유예하거나 뒤로 미룸 | 쟁점이 사소하거나 당사자들의 격앙된 감정 냉각이 필요할 때 | 방치 시 문제가 확대되어 통제 불능 상태 초래 |
| **수용 (Accommodating)** | 자신의 주장을 접고 상대방의 요구를 전폭 수용 | 자신이 틀렸음을 인정하거나 장기적 파트너십 보호가 우선일 때 | 수용자의 발언권 위축 및 박탈감 누적 |

## Ⅳ. 갈등 중재와 해결의 5단계 엔지니어링 프로세스

> 비언어적 징후 포착에서 출발하여 사람과 문제를 분리하고, 팩트 기반의 합의안을 프로젝트 기준선에 반영하여 사후 재발을 차단함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="갈등 중재 5단계 엔지니어링 프로세스 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 갈등 조기 감지 (Detection)</strong></span>
    <small>스탠드업 미팅 · PR 리뷰 코멘트 모니터링<br />→ 커뮤니케이션 이상 징후 포착</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 사람과 문제의 분리 (Separation)</strong></span>
    <small>감정적 비난 차단 · 객관적 기술 팩트(Fact)만 추출<br />→ 이슈 로그(Issue Log) 등록</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 본질적 이해관계 분석 (Analysis)</strong></span>
    <small>5-Why 기법 적용 · 표면 입장(Position) 뒤의 숨은 니즈(Interest) 규명<br />→ 이해관계자 매트릭스</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 상황별 대응모드 실행 (Resolution)</strong></span>
    <small>Thomas-Kilmann 모드 적용 · PoC 실증 · 의사결정 기록(ADR) 작성<br />→ 갈등 합의안 및 ADR</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 제도화 및 기준선 반영 (Institutionalization)</strong></span>
    <small>합의 내용을 WBS 및 RACI에 갱신 · 재발 방지 모니터링<br />→ 프로젝트 계획 변경 승인서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Fact-based Decision</strong></span> · 사람과 문제를 분리하고 PoC 실증 데이터와 ADR 문서로 객관적 합의 도출</div>

## Ⅴ. Thomas-Kilmann 모델 vs 하버드 협상 원칙(PON) 비교

> TKI가 상황에 따른 '행동 양식의 선택'이라면, 하버드 협상 원칙은 '협력(Collaborating)을 구체적으로 실천하는 기술'임.

| 비교 항목 | Thomas-Kilmann 모델 (TKI) | 하버드 협상 원칙 (PON) |
|---|---|---|
| 기본 관점 | 상황과 성향에 따른 5가지 행동 양식의 유연한 선택 | 원칙 기반의 접근을 통해 상호 윈-윈(Win-Win) 창출 |
| 핵심 메시지 | 모든 모드는 고유의 쓰임새가 있으며 상황에 맞춰야 함 | 입장에 얽매이지 말고 상호 숨겨진 이익에 집중하라 |
| 접근 메커니즘 | 자기주장성(Assertiveness) vs 협조성(Cooperativeness) 매트릭스 | 4대 원칙 (사람 분리, 이해관계 집중, 대안 개발, 객관적 기준) |
| 주 활용 상황 | 팀 내부의 일상적 성향 진단 및 갈등 국면 판정 | 복잡한 계약 협상, 대규모 범위 변경, 대외 이해관계 분쟁 |
| 상호 관계 | 갈등의 현재 위치와 최적 모드를 진단하는 도구 | 협력(Collaborating) 모드를 실행하기 위한 실천 방법론 |

## Ⅵ. 실무 갈등관리 실패 요인과 공학적 통제 방안

> 감정 대립과 구두 합의의 번복을 방어하지 못하면 프로젝트는 치명적인 정치적 소모전에 휘말림.

| 위험 요인 | 발생 원인 | 공학적·관리적 통제 대책 | 검증 지점 |
|---|---|---|---|
| 감정적 비난 전이 | 기술적 견해차를 개인의 역량이나 태도 문제로 공격 | 비동기 문서 기반 토론(**ADR**) 및 코드 리뷰 가이드라인 제정 | 감정 배제 및 기술적 팩트 기반 논의 확인 |
| PM의 일방적 강요 | 납기 압박을 이유로 충분한 검토 없이 상명하달 지시 | 부하 테스트, 벤치마크 결과 등 객관적 수치 기반 의사결정 | 팀원의 심리적 저항 및 태업 방지 확인 |
| 결정 장애 및 방임 | 만장일치를 추구하다가 의사결정이 지연되어 납기 파탄 | **Disagree and Commit(동의하지 않아도 헌신)** 원칙 제도화 | 타임박스 내 최종 의사결정 완료율 100% |
| 합의안 사후 파기 | 구두 합의에 그쳐 돌아서서 상호 다른 주장 제기 | 중재 회의 직후 액션 아이템, 책임자, 기한 명시 회의록 배포 | WBS 및 RACI 기준선 공식 반영 완료 |

## Ⅶ. 심리적 안전감과 데이터 기반 중재 중심의 기술사적 제언

> 갈등의 부재는 평화가 아닌 무관심의 증거이며, 진정한 고성과 팀은 과업 갈등을 자유롭게 분출할 수 있는 심리적 안전감 위에서 탄생함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 프로젝트에서 갈등을 무조건 없애려 하면 구성원들은 침묵을 선택하고 잠재된 위험은 오픈 직전 폭발하게 됨. 기술적 이견(과업 갈등)은 PoC와 아키텍처 결정 기록(ADR)을 통해 건설적 토론으로 승화시키고, 감정적 충돌(관계 갈등)만 단호하게 분리 차단해야 함.
- 나라면: 프로젝트 킥오프 시 `갈등 에스컬레이션 3단계 경로 정의 → 아키텍처 분쟁 시 48시간 타임박스 PoC 룰 의무화 → 합의 불발 시 단일 의사결정권자(Sponsor) 직권 결정 후 Disagree and Commit 강제`를 거버넌스 헌장에 못박아 정쟁을 원천 차단하겠음.

### 실전 답안용 기술사적 제언

- 판정: 주관적 감정 대립 탈피 및 데이터 기반 공학적 중재 거버넌스 확립
- 대안: **PoC-ADR-Disagree and Commit** 3단계 갈등 해결 메커니즘 수립
- 검증: 아키텍처 분쟁의 ADR 문서화율 100% · 중재 후 일정 지연 0건
- 효과: 건설적인 기술 혁신 유도 및 팀 내 심리적 안전감(Psychological Safety) 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="갈등관리 거버넌스 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>감정 대립 전이 · 권위적 강요 · 결정 장애로 인한 납기 지연</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>사람/문제 분리 + ADR 문서화 + Disagree and Commit 원칙</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>타임박스 내 의사결정 완료 · WBS/RACI 기준선 일치</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>과업 갈등의 품질 개선 승화 · 팀 결속력 및 프로젝트 완주성 보장</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **갈등관리(Conflict Management)**는 프로젝트 목표 달성 과정에서 발생하는 이해관계자 간의 대립과 이견을 조기에 식별하고 **Thomas-Kilmann 모델**을 통해 조정하는 **프로젝트 관리 프로세스**
- 목적: 파괴적인 **관계 갈등** 조기 차단 및 생산적인 **과업 갈등** 유도 → 팀 응집력 강화 및 시스템 품질 극대화

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="갈등관리 프로세스 요약">
  <div class="itpe-pipeline-node"><strong>징후 감지</strong><small>PR 리뷰 · 스탠드업 미팅</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>사람·문제 분리</strong><small>감정 배제 · 이슈 로그 등록</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>모드 실행</strong><small>Thomas-Kilmann 5대 모드</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>공학적 검증</strong><small>PoC 실증 · ADR 기록</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>제도화</strong><small>WBS · RACI 기준선 반영</small></div>
</div>

### 3. 핵심 통제

- **Thomas-Kilmann 5대 모드**: 협력(Win-Win), 경쟁(긴급 원칙), 타협(절충), 회피(사소한 문제), 수용(관계 보존)
- **공학적 통제**: **ADR(Architectural Decision Record)** 작성 및 **Disagree and Commit** 원칙 적용으로 결정 장애 극복

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 2교시: 프로젝트 팀 개발 및 갈등 해결 기법
- Kenneth W. Thomas & Ralph H. Kilmann, [Thomas-Kilmann Conflict Mode Instrument (TKI)](https://www.kilmanndiagnostics.com)
- PMI, [A Guide to the Project Management Body of Knowledge (PMBOK Guide) 7th Edition](https://www.pmi.org)
- Fisher, Ury & Patton, [Getting to Yes: Negotiating Agreement Without Giving In (Harvard PON)](https://www.pon.harvard.edu)

## 학습 체크

- [ ] 과업 갈등, 관계 갈등, 프로세스 갈등의 차이점과 관리 방향을 설명할 수 있는가?
- [ ] Thomas-Kilmann 모델의 2대 축(자기주장성, 협조성)과 5대 모드를 도식화할 수 있는가?
- [ ] 협력(Collaborating)과 타협(Compromising)의 근본적 차이와 적합한 상황을 비교할 수 있는가?
- [ ] 아키텍처 결정 기록(ADR)과 PoC를 연계한 공학적 갈등 중재 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [SWOT 분석](./034_swot_analysis.md)
- 연관 토픽: [터크만 팀 발달 모델](./028_tuckman_team_development_model.md), [PMO](./004_pmo.md), [프로젝트 관리](./065_project_management.md), [부정적 위험 대응 전략](./040_negative_risk_response_strategy.md)
- 다음 토픽: [NIST AI RMF](./036_nist_ai_rmf.md)
