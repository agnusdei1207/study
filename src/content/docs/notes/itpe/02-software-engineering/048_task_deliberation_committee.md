---
title: "소프트웨어사업 과업심의위원회"
author: "Codex"
date: "2026-09-20T20:06:00+09:00"
tags: ["notes-software-engineering"]
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 공공 소프트웨어사업 관리와 과업 통제를 거쳐 과업심의위원회로 이어지는 지식 위치"><span>소프트웨어 공학</span><span>공공 SW 사업관리 · 과업 통제</span><strong>과업심의위원회</strong></div>

## 큰 그림과 30초 인출

- 본질: **과업심의위원회**는 국가기관등의 소프트웨어사업에서 과업내용의 확정·변경과 계약금액·계약기간 조정을 심의하는 법정 위원회
- 메커니즘: 과업 확정 또는 변경 요청 → 외부위원 과반의 심의·의결 → 결과와 조치계획 통보 → 계약 반영
- 산출: 확정 과업내용 · 변경 타당성 판단 · 계약금액·기간 조정안 · 조치계획

<div class="itpe-pipeline is-vertical" role="img" aria-label="과업심의위원회의 과업 통제 흐름"><div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>심의 사유</strong></span><small><b>입력</b> 과업내용 확정·변경 · 계약 조정 필요<br /><b>주체</b> 국가기관등 또는 계약 사업자</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>심의·의결</strong></span><small><b>활동</b> 범위·대가·기간·근거 검토<br /><b>통제</b> 외부위원 과반 · 제척·기피·회피</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><span class="itpe-keyword"><strong>통보·반영</strong></span><small><b>산출</b> 심의결과 · 조치계획<br /><b>효과</b> 계약금액·기간과 과업 Baseline 정합화</small></div></div>

<details><summary>핵심 용어</summary>

- **과업내용**: 법령이 정한 공식 용어로, 계약에서 수행할 소프트웨어사업의 범위와 내용을 식별하는 기준
- **Baseline(기준선)**: 승인된 과업 범위와 계약조건을 변경 통제의 비교 기준으로 고정한 상태
- **제척·기피·회피**: 이해충돌 위원을 심의에서 배제해 의결의 공정성을 확보하는 통제
- **계약금액·계약기간 조정**: 과업내용 변경의 영향을 대가와 일정에 함께 반영하는 후속 조치

</details>

## 예상문제

> 소프트웨어사업 과업심의위원회의 법적 근거와 구성·운영 및 심의 절차를 설명하고, 과업 변경 통제의 실효성 확보 방안을 제시하시오.

## Ⅰ. 과업과 계약조건을 함께 통제하는 법정 위원회

> 과업심의는 변경 허용 여부만 판단하는 절차가 아니라 변경된 범위에 맞춰 대가와 기간을 정합화하는 계약 통제임.

- 정의: 국가기관등의 **과업내용 확정·변경**과 **계약금액·계약기간 조정**을 심의하는 **법정 위원회**
- 목적: 구두 지시·무상 과업 확대 방지 → 발주자와 사업자가 확인할 객관적 계약 Baseline 유지
- 근거: 「소프트웨어 진흥법」 제50조, 같은 법 시행령 제45조부터 제47조

## Ⅱ. 심의 대상과 구성·운영

> 위원회의 독립성은 외부위원 비율과 이해충돌 배제에서, 실효성은 결과를 계약에 반영하는 후속 조치에서 확보됨.

| 구분 | 법정 내용 | 통제점 |
|---|---|---|
| 대상 | 과업내용 확정 | 입찰 전 범위 명료화 |
| 변경 | 과업내용 변경 확정 | 변경 사유·범위·영향 증거화 |
| 조정 | 계약금액·계약기간 | 범위 변경과 대가·일정 연동 |
| 구성 | 위원장 포함 5명 이상 10명 이내 | 소속기관 외 위원 과반 |
| 의결 | 재적 과반 출석·출석 과반 찬성 | 제척·기피·회피 적용 |

## Ⅲ. 사업자 개최 요청부터 계약 반영까지

> 사업자의 개최 요청권이 실제 변경 통제로 이어지려면 요청서·영향분석·결과 통보·계약 변경이 하나의 추적 경로로 남아야 함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="사업자의 과업심의위원회 개최 요청 절차"><div class="itpe-pipeline-node"><strong>변경 요청</strong><small><b>활동</b> 변경 사유·범위·비용·기간 영향 제출<br /><b>산출</b> 과업내용 변경요청서와 근거</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>요청 수용·소집</strong><small><b>활동</b> 국가기관등이 위원장에게 개최 통보<br /><b>산출</b> 안건·위원·심의자료</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>심의·의결</strong><small><b>활동</b> 타당성·영향·계약 조정 검토<br /><b>산출</b> 위원별 결과와 종합 결과</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>결과 통보·조치</strong><small><b>활동</b> 요청일부터 14일 이내 결과·조치계획 통보<br /><b>산출</b> 계약 변경 또는 미반영 사유</small></div></div>

- 불가피한 추가 조사 시 사업자와 협의하여 한 차례, 14일 이내 범위에서 통보기한 연기 가능
- 입찰공고에 사업자의 개최 요청권과 과업 변경 절차를 명시

## Ⅳ. 형식적 심의를 막는 운영 통제

> 위원회 개최 건수보다 변경 근거와 계약 반영의 추적성이 중요하며, 미반영 시 특별한 사정의 근거가 남아야 함.

| 문제 | 원인 | 대안 | 판정 |
|---|---|---|---|
| 사후 승인 | 변경 착수 후 안건 상정 | 변경 전 작업중지점과 영향분석 | 의결 전 변경 작업 미착수 |
| 대가 누락 | 기능만 심의 | 범위·금액·기간 묶음 안건 | 세 요소의 동시 의결 |
| 형식 의결 | 근거 없는 요약자료 | 요구사항·산출물·일정 추적표 첨부 | 변경 영향의 양방향 추적 |
| 이해충돌 | 당사자 중심 구성 | 외부위원 과반·제척·기피·회피 | 의결 참여 적정성 기록 |

## Ⅴ. 변경 증거와 계약 실행을 잇는 거버넌스

> 과업심의의 종료점은 회의록 작성이 아니라 승인된 변경이 계약·일정·검수 기준에 일관되게 반영된 상태임.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 과업 변경은 기술 범위만의 문제가 아니다. 범위가 바뀌면 대가·기간·검수 기준도 함께 바뀌어야 Baseline이 다시 성립한다.
- `나라면`: 변경요청서에 요구사항 ID, 영향 산출물, 비용·기간 근거를 묶고 심의 결과가 계약 변경까지 이어지는지를 추적하겠다.

### 실전 답안용 기술사적 제언

- 판정: 사후 상정과 계약 미반영이 과업심의의 실효성을 훼손
- 대안: 변경 전 Gate와 범위·금액·기간 통합 안건, 결과-계약 추적표 적용
- 검증: 의결 전 착수 여부, 외부위원·이해충돌 기록, 계약·검수 기준 반영 확인
- 효과: 무상 과업 확대 억제 · 분쟁 근거 명료화 · 계약 이행 가능성 향상

<div class="itpe-pipeline is-vertical" role="img" aria-label="과업심의 실효성 개선 제언"><div class="itpe-pipeline-node"><strong>사후·형식 심의</strong><small><b>문제</b> 변경 실행 뒤 범위만 승인</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>변경 전 Gate</strong><small><b>대안</b> 범위·금액·기간과 증거를 한 안건으로 심의</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>계약 추적</strong><small><b>판정</b> 의결 결과와 계약·일정·검수 기준 일치</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>공정한 변경 통제</strong><small><b>효과</b> 책임·대가·납기 분쟁 예방</small></div></div>

## 1교시 10점 답안 발췌

- 정의: **과업심의위원회**는 국가기관등의 **과업내용 확정·변경**과 **계약금액·계약기간 조정**을 심의하는 법정 위원회
- 목적: 과업 확대와 계약조건 불일치 방지 → 객관적 과업 Baseline 유지

<div class="itpe-pipeline is-vertical" role="img" aria-label="과업심의위원회 1교시 핵심 흐름"><div class="itpe-pipeline-node"><strong>확정·변경 요청</strong><small><b>입력</b> 과업·금액·기간 영향 근거</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>심의·의결</strong><small><b>통제</b> 외부위원 과반·이해충돌 배제</small></div><div class="itpe-pipeline-arrow">↓</div><div class="itpe-pipeline-node"><strong>통보·계약 반영</strong><small><b>산출</b> 결과·조치계획·변경 계약</small></div></div>

| 구분 | 핵심 내용 |
|---|---|
| 구성 | 위원장 포함 5~10명, 소속기관 외 위원 과반 |
| 운영 | 재적 과반 출석·출석 과반 찬성 |
| 요청 | 사업자 요청일부터 14일 이내 결과·조치계획 통보 |

- 결론: 변경 범위와 대가·기간을 함께 심의하고 결과를 계약·검수 기준까지 추적함

## 출제 이력과 검증 출처

- [국가법령정보센터, 소프트웨어 진흥법 제50조](https://www.law.go.kr/lsLinkCommonInfo.do?lsJoLnkSeq=1031614471)
- [국가법령정보센터, 소프트웨어 진흥법 시행령 제45조~제47조](https://law.go.kr/LSW/lumLsLinkPop.do?chrClsCd=010202&lspttninfSeq=162563)

## 학습 체크

- [ ] Ⅰ·근거: 법 제50조의 심의 대상 세 가지와 목적을 재현할 수 있는가
- [ ] Ⅱ·구성: 위원 수·외부위원 비율·의결·이해충돌 통제를 연결할 수 있는가
- [ ] Ⅲ·절차: 네 단계의 활동·산출과 14일 통보기한을 설명할 수 있는가
- [ ] Ⅳ·운영: 네 문제의 원인·대안·판정 기준을 연결할 수 있는가
- [ ] Ⅴ·제언: 변경 결과를 계약·일정·검수 기준에 추적하는 이유를 설명할 수 있는가

## 연결 토픽

- [요구공학](./040_requirements_engineering/)
- [요구사항 명세](./054_requirements_specification/)
- [요구사항 추적표](./102_requirement_traceability_matrix/)
- [FP(Function Point)](./113_function_point/)
