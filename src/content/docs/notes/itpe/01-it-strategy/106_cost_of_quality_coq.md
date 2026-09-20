---
title: "품질비용(COQ)"
author: "OpenAI Codex"
date: "2026-09-22T10:25:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 품질관리를 거쳐 품질비용으로 이어지는 위치">
  <span>IT 전략·관리</span><span>품질관리·경제성</span><strong>COQ</strong>
</div>

## 큰 그림과 30초 인출

- **본질**: 품질 확보 비용과 품질 실패 손실을 함께 측정
- **구조**: 예방·평가 + 내부실패·외부실패
- **활용**: 실패비용의 원인을 예방활동으로 전환해 총비용 최적화

<div class="itpe-svg-map">
<svg viewBox="0 0 760 500" role="img" aria-label="품질비용의 PAF 분류">
  <rect x="45" y="35" width="300" height="85" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="195" y="70" text-anchor="middle" class="itpe-svg-title">예방비용</text><text x="195" y="98" text-anchor="middle" class="itpe-svg-sub">표준·교육·설계검토</text>
  <rect x="415" y="35" width="300" height="85" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="565" y="70" text-anchor="middle" class="itpe-svg-title">평가비용</text><text x="565" y="98" text-anchor="middle" class="itpe-svg-sub">검토·시험·감사</text>
  <rect x="45" y="300" width="300" height="85" rx="14" class="itpe-svg-node"></rect>
  <text x="195" y="335" text-anchor="middle" class="itpe-svg-title">내부실패비용</text><text x="195" y="363" text-anchor="middle" class="itpe-svg-sub">재작업·재시험·폐기</text>
  <rect x="415" y="300" width="300" height="85" rx="14" class="itpe-svg-node"></rect>
  <text x="565" y="335" text-anchor="middle" class="itpe-svg-title">외부실패비용</text><text x="565" y="363" text-anchor="middle" class="itpe-svg-sub">장애·보상·신뢰손실</text>
  <text x="380" y="190" text-anchor="middle" class="itpe-svg-title">COQ = 적합비용 + 부적합비용</text>
  <text x="380" y="225" text-anchor="middle" class="itpe-svg-sub">예방·평가 투자 ↔ 실패비용 감소</text>
  <path d="M195 120 L195 300 M565 120 L565 300" class="itpe-svg-link"></path>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **COQ(Cost of Quality)**: 품질 문제 예방·평가 비용과 내부·외부 실패비용의 총합
- **PAF(Prevention, Appraisal, Failure)**: 예방·평가·실패로 품질비용을 분류하는 모델
- **COPQ(Cost of Poor Quality)**: 내부·외부 실패로 발생하는 부적합 비용
- **Shift-Left**: 검토·시험·보안활동을 개발 초기로 이동하는 접근
- **Quality Gate**: 정의된 품질기준을 충족해야 다음 단계로 진행하게 하는 통제

</details>

## 예상문제

> **(미출제 예상·25점)** 품질비용의 개념과 PAF 구성요소를 설명하고, 소프트웨어 사업에서 품질비용을 측정·최적화하는 방안을 제시하시오.

## Ⅰ. 품질비용 개요

> COQ는 품질부서 예산이 아니라 품질을 확보하거나 확보하지 못해 발생한 전체 비용임

- **정의**: 품질 문제를 예방·평가하는 비용과 내부·외부 실패로 발생하는 손실을 분류·측정하는 관리기법
- **목적**: 숨은 실패비용 가시화·개선 투자 우선순위 결정·총비용 최적화

## Ⅱ. PAF 구성체계

| 구분 | 의미 | 소프트웨어 예시 |
|---|---|---|
| 예방 | 결함 발생 방지 | 표준·교육·Architecture Review |
| 평가 | 적합성 확인 | Review·Test·정적분석·감리 |
| 내부실패 | 배포 전 발견 결함 | 수정·재시험·빌드 실패 |
| 외부실패 | 배포 후 발견 결함 | 장애·보상·긴급패치·신뢰손실 |

## Ⅲ. 측정·개선 절차

> 비용 분류 자체보다 반복되는 실패비용을 어떤 예방활동으로 전환할지가 핵심임

<div class="itpe-pipeline is-vertical" role="img" aria-label="품질비용 측정과 개선 절차">
  <div class="itpe-flow-node"><strong>① 분류기준 정의</strong><div class="itpe-step-detail"><strong>활동</strong><span>예방·평가·내부·외부 계정 정의</span></div><div class="itpe-step-detail"><strong>산출</strong><span>COQ 분류표</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>② 비용 수집</strong><div class="itpe-step-detail"><strong>활동</strong><span>공수·도구·장애·보상 데이터 집계</span></div><div class="itpe-step-detail"><strong>산출</strong><span>COQ 현황표</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>③ 원인·우선순위 분석</strong><div class="itpe-step-detail"><strong>활동</strong><span>실패비용·결함원인 Pareto 분석</span></div><div class="itpe-step-detail"><strong>산출</strong><span>개선 후보·Business Case</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>④ 예방·평가 개선</strong><div class="itpe-step-detail"><strong>활동</strong><span>Review·자동시험·Quality Gate 적용</span></div><div class="itpe-step-detail"><strong>검증</strong><span>COQ 추세·재발결함 확인</span></div></div>
</div>

## Ⅳ. 적합비용·부적합비용 균형

| 기준 | 적합비용 중심 | 부적합비용 중심 |
|---|---|---|
| 시점 | 결함 전·배포 전 | 결함 발생·배포 후 |
| 성격 | 계획 가능한 투자 | 변동성 큰 손실 |
| 관리 | 예방·자동화·검증 | 복구·보상·원인제거 |
| 판단 | 투자 대비 실패감소 | 손실 규모·재발 위험 |

초기 품질활동의 효과는 제품·도메인·결함 유형에 따라 달라지므로 고정 배수나 일률적 최적점을 적용하지 않음.

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 품질비용 누락 | 공수·장애·보상 계정 연계 | 숨은 비용 가시화 |
| 분류 중복 | 사건별 주비용 분류·기준 명시 | 이중계상 방지 |
| 지표 목표화 | 비용·결함·고객영향 함께 평가 | 숫자 맞추기 방지 |
| 예방투자 효과 불명 | 전후 추세·재발률 검증 | 투자 근거 확보 |

## Ⅵ. 결론·기술사적 제언

> **[핵심 통찰]** 품질비용의 목적은 테스트 예산을 늘리는 것이 아니라 가장 큰 실패손실을 가장 경제적인 예방 통제로 바꾸는 것임.

> **나라면** 장애·재작업 비용을 원인별로 집계하고, 상위 원인에만 Review·자동시험·Quality Gate를 적용한 뒤 실패비용 감소로 투자를 재평가하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="실패비용을 예방통제로 전환하는 품질비용 폐루프">
  <div class="itpe-flow-node"><strong>실패비용</strong><div class="itpe-step-detail"><strong>증거</strong><span>장애·재작업·보상</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>원인 Pareto</strong><div class="itpe-step-detail"><strong>판정</strong><span>비용·빈도·고객영향</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>예방·평가 통제</strong><div class="itpe-step-detail"><strong>실행</strong><span>Review·Test·Gate</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>COQ 재측정</strong><div class="itpe-step-detail"><strong>검증</strong><span>실패비용·재발결함 추세</span></div></div>
</div>

## 1교시 10점 답안 발췌

- **정의**: 품질 문제를 예방·평가하는 비용과 내부·외부 실패로 발생하는 손실을 분류·측정하는 관리기법
- **목적**: 숨은 실패비용 가시화·개선 투자 우선순위 결정·총비용 최적화

| 적합비용 | 부적합비용 |
|---|---|
| 예방·평가 | 내부실패·외부실패 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [ASQ, Cost of Quality](https://asq.org/quality-resources/cost-of-quality)

## 학습 체크

- [ ] Ⅰ: COQ 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 예방·평가·내부실패·외부실패를 예시와 분류할 수 있는가?
- [ ] Ⅲ: 분류부터 개선 검증까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅳ: 적합비용·부적합비용의 관리 차이를 비교할 수 있는가?
- [ ] Ⅴ: 누락·중복·지표 목표화의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: 실패비용을 예방통제로 전환하는 폐루프를 그릴 수 있는가?

## 연결 토픽

- 이전: [104. 클라우드 전환사업 감리](./104_cloud_migration_project_audit/)
- 관련: [111. Six Sigma DMAIC](./111_six_sigma_dmaic/) · [113. SW 비용 산정](./113_software_cost_estimation/)
- 다음: [107. EA·ITA](./107_ea_ita/)
