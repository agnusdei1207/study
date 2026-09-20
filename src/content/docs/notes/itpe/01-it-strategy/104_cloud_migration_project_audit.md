---
title: "클라우드 전환사업 감리"
author: "OpenAI Codex"
date: "2026-09-22T10:05:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "B"
extra:
  model: "GPT-5"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 정보시스템 감리를 거쳐 클라우드 전환사업 감리로 이어지는 위치">
  <span>IT 전략·관리</span><span>정보시스템 감리</span><strong>클라우드 전환사업 감리</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 클라우드 전환 전략·설계·이행·운영의 적정성을 독립 검증
- **메커니즘**: 전환대상·전략 → Cloud Architecture → Migration → 운영·비용
- **통제**: 공유책임·데이터 정합성·복구 가능성·비용 가시성

<div class="itpe-pipeline is-vertical" role="img" aria-label="클라우드 전환사업 감리 흐름">
  <div class="itpe-flow-node"><strong>전략</strong><div class="itpe-step-detail"><strong>점검</strong><span>대상·전환방식·규제·TCO</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>설계</strong><div class="itpe-step-detail"><strong>점검</strong><span>가용성·IAM·망·암호화·백업</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>이행</strong><div class="itpe-step-detail"><strong>점검</strong><span>데이터·Cut-over·Rollback·IaC</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>운영</strong><div class="itpe-step-detail"><strong>점검</strong><span>SLA·모니터링·FinOps·DR</span></div></div>
</div>

<details>
<summary>약어·전문용어</summary>

- **TCO(Total Cost of Ownership)**: 도입·이행·운영·종료를 포함한 총소유비용
- **IAM(Identity and Access Management)**: 사용자·서비스의 신원과 접근권한 관리
- **IaC(Infrastructure as Code)**: 인프라 구성을 코드로 정의·배포·변경하는 방식
- **SLA(Service Level Agreement)**: 서비스 수준과 책임을 정한 합의
- **FinOps(Financial Operations)**: 기술·재무·업무가 함께 클라우드 비용과 가치를 관리하는 운영방식
- **DR(Disaster Recovery)**: 재해 발생 후 시스템·데이터를 복구하는 체계

</details>

## 예상문제

> **(미출제 예상·25점)** 클라우드 전환사업 감리의 필요성과 단계별 점검사항을 설명하고, 주요 문제점과 대응책을 제시하시오.

## Ⅰ. 클라우드 전환사업 감리 개요

> 서버 이전 여부보다 선택한 전환방식이 업무·규제·가용성·비용 조건에 적합한지를 검증함

- **정의**: 온프레미스 정보시스템의 클라우드 전환 과정에서 전략·설계·이행·운영의 적정성을 독립 점검하는 감리 활동
- **목적**: 전환 실패·보안책임 누락·데이터 오류·비용 통제 실패 예방

## Ⅱ. 단계별 점검사항

| 단계 | 주요 활동 | 감리 증적 |
|---|---|---|
| 전략 | 대상분류·전환방식·규제·TCO 분석 | 전환계획·타당성 분석 |
| 설계 | 가용성·IAM·네트워크·암호화·백업 | 목표 Architecture·권한표 |
| 이행 | 데이터 복제·대사·Cut-over·Rollback | 이행로그·대사·리허설 결과 |
| 운영 | SLA·관측성·DR·FinOps·Exit Plan | 운영계획·시험·비용보고 |

## Ⅲ. 전환 전략 점검

> Rehost·Replatform·Refactor 중 하나를 우월한 방식으로 정하지 않고 업무 가치와 제약으로 선택함

| 전략 | 핵심 | 점검 기준 |
|---|---|---|
| Rehost | 구조 변경 없이 이전 | 속도·호환성·비용효과 |
| Replatform | 일부 관리형 서비스 전환 | 기능호환·운영책임 변화 |
| Refactor | Cloud Native 재설계 | 복잡도·분산구조·운영역량 |
| Repurchase | SaaS 등으로 대체 | Fit-Gap·데이터 이동·종속성 |
| Retain | 현행 유지 | 규제·기술제약·연계 |
| Retire | 시스템 종료 | 의존성·보존·폐기 절차 |

## Ⅳ. 온프레미스·클라우드 감리 비교

| 기준 | 온프레미스 | 클라우드 |
|---|---|---|
| 자원 | 물리·가상 장비 | API 기반 가상자원·IaC |
| 보안 | 기관 중심 책임 | CSP·이용자 공유책임 |
| 가용성 | 장비·센터 이중화 | Zone·Region·서비스 조합 |
| 비용 | 구매·감가상각 | 사용량·약정·태그·단가 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 전략 없는 일괄 이전 | 업무별 전환전략·Exit 조건 | 부적합 이전 방지 |
| 공유책임 공백 | 서비스모델별 RACI·통제 매핑 | 보안책임 명확화 |
| 데이터 불일치 | 원천·목표 대사·복구 리허설 | 이행 무결성 확보 |
| 비용 가시성 부족 | 태깅·예산·이상비용 경보 | 비용 책임성 강화 |
| 특정 CSP 종속 | 표준 API·데이터 반출·Exit Plan | 전환 선택권 확보 |

## Ⅵ. 결론·기술사적 제언

> **[핵심 통찰]** 클라우드 전환 감리는 자원 존재 여부가 아니라 전환 후 책임·복구·비용을 지속 관리할 수 있는지를 검증해야 함.

> **나라면** 요구사항별 전환전략·Architecture·IaC·시험·운영 통제를 추적하고, Cut-over 전에 보안·복구·비용·Exit Plan을 함께 통과시키는 Quality Gate를 운영하겠음.

<div class="itpe-svg-map">
<svg viewBox="0 0 760 500" role="img" aria-label="클라우드 전환 품질 게이트">
  <rect x="250" y="25" width="260" height="85" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="60" text-anchor="middle" class="itpe-svg-title">전환 증적</text><text x="380" y="88" text-anchor="middle" class="itpe-svg-sub">전략·설계·IaC·시험</text>
  <rect x="250" y="175" width="260" height="100" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="380" y="212" text-anchor="middle" class="itpe-svg-title">Quality Gate</text><text x="380" y="242" text-anchor="middle" class="itpe-svg-sub">보안·복구·비용·Exit</text>
  <rect x="70" y="355" width="240" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="190" y="392" text-anchor="middle" class="itpe-svg-title">통과</text><text x="190" y="420" text-anchor="middle" class="itpe-svg-sub">Cut-over·운영 전환</text>
  <rect x="450" y="355" width="240" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="570" y="392" text-anchor="middle" class="itpe-svg-title">미통과</text><text x="570" y="420" text-anchor="middle" class="itpe-svg-sub">보완·재검증</text>
  <path d="M380 110 L380 175 M315 275 L190 355 M445 275 L570 355" class="itpe-svg-link"></path>
</svg>
</div>

## 1교시 10점 답안 발췌

- **정의**: 클라우드 전환 과정에서 전략·설계·이행·운영의 적정성을 독립 점검하는 감리 활동
- **목적**: 전환 실패·보안책임 누락·데이터 오류·비용 통제 실패 예방

| 단계 | 점검 |
|---|---|
| 전략·설계 | 전환방식·규제·Architecture·공유책임 |
| 이행 | 데이터 대사·Cut-over·Rollback·IaC |
| 운영 | SLA·DR·FinOps·Exit Plan |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [NIA, 지능정보기술 감리 실무 가이드](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=25211&cbIdx=99860&parentSeq=25211)
- [NIST SP 800-146, Cloud Computing Synopsis and Recommendations](https://csrc.nist.gov/pubs/sp/800/146/final)
- [FinOps Foundation, FinOps Framework](https://www.finops.org/framework/)

## 학습 체크

- [ ] Ⅰ: 클라우드 전환 감리의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 전략부터 운영까지 활동·증적을 연결할 수 있는가?
- [ ] Ⅲ: 전환 전략의 선택기준을 비교할 수 있는가?
- [ ] Ⅳ: 온프레미스와 클라우드 감리 차이를 설명할 수 있는가?
- [ ] Ⅴ: 공유책임·정합성·비용·종속 위험의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: 전환 Quality Gate를 시각화할 수 있는가?

## 연결 토픽

- 이전: [103. 차세대 시스템 오픈 리스크](./103_next_generation_system_open_risk/)
- 관련: [102. 지능정보기술 감리 실무 가이드](./102_intelligent_information_technology_audit_guide/) · [012. FinOps](./012_finops/)
- 다음: [106. 품질비용](./106_cost_of_quality_coq/)
