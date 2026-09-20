---
title: "지능정보기술 감리 실무 가이드"
author: "OpenAI Codex"
date: "2026-09-22T09:25:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 정보시스템 감리를 거쳐 지능정보기술 감리 실무 가이드로 이어지는 위치">
  <span>IT 전략·관리</span><span>정보시스템 감리</span><strong>지능정보기술 감리 실무 가이드</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 기존 감리기준에 빅데이터·클라우드·운영·유지관리 특화 점검항목을 보완
- **메커니즘**: 사업 특성 식별 → 적용 영역 선택 → 단계별 점검 → 개선권고·시정 확인
- **산출**: 감리계획·점검결과·개선권고·시정조치 확인

<div class="itpe-svg-map">
<svg viewBox="0 0 760 500" role="img" aria-label="지능정보기술 감리 실무 가이드의 적용 영역">
  <rect x="250" y="30" width="260" height="85" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="380" y="66" text-anchor="middle" class="itpe-svg-title">정보시스템 감리기준</text>
  <text x="380" y="95" text-anchor="middle" class="itpe-svg-sub">기본점검표·사업유형·감리시점</text>
  <rect x="40" y="270" width="200" height="105" rx="14" class="itpe-svg-node"></rect>
  <text x="140" y="310" text-anchor="middle" class="itpe-svg-title">빅데이터</text>
  <text x="140" y="340" text-anchor="middle" class="itpe-svg-sub">수집·저장·분석·활용</text>
  <rect x="280" y="270" width="200" height="105" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="310" text-anchor="middle" class="itpe-svg-title">클라우드</text>
  <text x="380" y="340" text-anchor="middle" class="itpe-svg-sub">전환·서비스·보안·운영</text>
  <rect x="520" y="270" width="200" height="105" rx="14" class="itpe-svg-node"></rect>
  <text x="620" y="310" text-anchor="middle" class="itpe-svg-title">운영·유지관리</text>
  <text x="620" y="340" text-anchor="middle" class="itpe-svg-sub">서비스·변경·장애·성과</text>
  <path d="M310 115 L140 270 M380 115 L380 270 M450 115 L620 270" class="itpe-svg-link"></path>
  <text x="180" y="205" class="itpe-svg-label">특화 점검</text><text x="395" y="205" class="itpe-svg-label">보완</text><text x="555" y="205" class="itpe-svg-label">적용</text>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **NIA(National Information Society Agency)**: 한국지능정보사회진흥원
- **감리 점검항목**: 감리 대상의 적정성·준거성·효율성 등을 확인하는 기준
- **개선권고**: 감리 결과 확인된 문제에 대해 제시하는 시정·개선 요구
- **시정조치**: 개선권고에 따라 사업자가 수행한 보완 활동과 결과

</details>

## 예상문제

> **(미출제 예상·25점)** NIA 지능정보기술 감리 실무 가이드의 목적·적용영역을 설명하고, 기존 정보시스템 감리와 연계한 수행방안과 문제점·대응책을 제시하시오.

## Ⅰ. 가이드 개요

> 별도 AI 모델 인증기준이 아니라 기존 감리체계에 신기술 사업의 점검항목을 보완하는 실무 가이드임

- **정의**: NIA(National Information Society Agency)가 빅데이터·클라우드·운영·유지관리 사업의 감리 점검항목을 제시한 실무 가이드
- **목적**: 기술 특성을 반영한 감리 일관성·현장 적용성 확보

## Ⅱ. 적용영역·핵심 점검

| 영역 | 점검 대상 | 핵심 확인 |
|---|---|---|
| 빅데이터 | 수집·저장·처리·분석·활용 | 데이터 품질·보안·분석 적정성 |
| 클라우드 | 도입·전환·서비스·운영 | 아키텍처·이식성·보안·SLA |
| 운영·유지관리 | 서비스·변경·장애·성과 | 운영절차·형상·연속성·성과관리 |

## Ⅲ. 감리 적용 절차

> 기본점검표를 그대로 복제하지 않고 사업 특성에 맞는 점검항목과 증적을 선택함

<div class="itpe-pipeline is-vertical" role="img" aria-label="지능정보기술 감리 실무 가이드 적용 절차">
  <div class="itpe-flow-node"><strong>① 특성 분석</strong><div class="itpe-step-detail"><strong>활동</strong><span>사업유형·기술·감리시점 식별</span></div><div class="itpe-step-detail"><strong>산출</strong><span>감리 범위·중점사항</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>② 점검 설계</strong><div class="itpe-step-detail"><strong>활동</strong><span>기본·특화 점검항목 선택</span></div><div class="itpe-step-detail"><strong>산출</strong><span>감리계획·점검표</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>③ 증적 점검</strong><div class="itpe-step-detail"><strong>활동</strong><span>문서·설정·로그·시험결과 확인</span></div><div class="itpe-step-detail"><strong>산출</strong><span>점검결과·문제점</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>④ 권고·시정 확인</strong><div class="itpe-step-detail"><strong>판정</strong><span>적정·보완·미흡</span></div><div class="itpe-step-detail"><strong>산출</strong><span>감리보고서·시정조치 확인서</span></div></div>
</div>

## Ⅳ. 기존 감리와 연계

| 기준 | 기존 감리기준 | 실무 가이드 |
|---|---|---|
| 역할 | 공통 절차·점검체계 | 기술별 점검항목 보완 |
| 적용 | 사업유형·감리시점 | 빅데이터·클라우드·운영 특성 |
| 활용 | 기본점검표 구성 | 중점항목·증적 구체화 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 전 항목 기계 적용 | 사업 위험 기반 Tailoring | 핵심 위험 집중 |
| 문서 위주 확인 | 설정·로그·시험 증적 병행 | 실질 상태 검증 |
| 기술별 사일로 점검 | 데이터·서비스·운영 연계 추적 | 경계 누락 방지 |
| 권고 후 미조치 | 책임·기한·재확인 명시 | 개선 폐루프 확보 |

## Ⅵ. 결론·기술사적 제언

> **[핵심 통찰]** 특화 가이드의 가치는 점검항목 수가 아니라 사업 위험과 증적을 정확히 연결하는 데 있음.

> **나라면** 착수 단계에서 기술별 위험·점검항목·증적·책임자를 추적표로 확정하고, 종료 감리에서는 문서가 아닌 운영 증적으로 시정 완료를 판정하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="위험 기반 감리 폐루프">
  <div class="itpe-flow-node"><strong>기술 위험</strong><div class="itpe-step-detail"><strong>식별</strong><span>빅데이터·클라우드·운영</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>점검항목·증적</strong><div class="itpe-step-detail"><strong>연결</strong><span>문서·설정·로그·시험</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>개선권고</strong><div class="itpe-step-detail"><strong>조치</strong><span>책임자·기한·완료조건</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>시정 확인</strong><div class="itpe-step-detail"><strong>검증</strong><span>운영 증적·잔여위험</span></div></div>
</div>

## 1교시 10점 답안 발췌

- **정의**: NIA가 빅데이터·클라우드·운영·유지관리 사업의 감리 점검항목을 제시한 실무 가이드
- **목적**: 기술 특성을 반영한 감리 일관성·현장 적용성 확보

| 영역 | 핵심 점검 |
|---|---|
| 빅데이터 | 데이터 품질·보안·분석 |
| 클라우드 | 아키텍처·이식성·보안·SLA |
| 운영·유지관리 | 서비스·변경·장애·성과 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [NIA, 지능정보기술 감리 실무 가이드](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=25211&cbIdx=99860&parentSeq=25211)

## 학습 체크

- [ ] Ⅰ: 가이드의 성격·목적을 설명할 수 있는가?
- [ ] Ⅱ: 빅데이터·클라우드·운영 영역의 점검 대상을 구분할 수 있는가?
- [ ] Ⅲ: 특성 분석부터 시정 확인까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅳ: 기존 감리기준과 실무 가이드의 역할을 비교할 수 있는가?
- [ ] Ⅴ: 기계적 점검·문서 중심 감리의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: 위험·증적·권고·시정을 폐루프로 제시할 수 있는가?

## 연결 토픽

- 이전: [098. 전문성의 민주화](./098_democratization_of_expertise/)
- 관련: [008. 정보시스템 감리](./008_it_audit/) · [104. 클라우드 전환사업 감리](./104_cloud_migration_project_audit/)
- 다음: [103. 차세대 시스템 오픈 리스크](./103_next_generation_system_open_risk/)
