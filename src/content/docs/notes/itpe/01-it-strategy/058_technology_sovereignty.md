---
title: "기술 주권"
author: "OpenAI Codex"
date: "2026-09-22T03:00:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "GPT-5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략 관리에서 국가 기술 전략과 공급망을 거쳐 기술 주권으로 이어지는 지식 위치">
  <span>IT 전략·관리</span><span>국가 기술전략·공급망</span><strong>기술 주권</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 핵심기술을 직접 개발하거나 신뢰 가능한 경로로 조달할 **선택권·통제력·회복력**
- 전략: 취약성 식별 → 보호(Protect) → 육성(Promote) → 대외확산(Project)
- 균형: 전면 자급이 아니라 선택적 내재화·다변화·표준·동맹의 조합

<div class="itpe-svg-map">
<svg viewBox="0 0 760 590" role="img" aria-label="기술 주권을 보호 육성 대외확산으로 달성하는 3P 구조">
  <defs><marker id="arrow-tech-sovereignty" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <circle class="itpe-svg-node is-current" cx="380" cy="295" r="105" />
  <text class="itpe-svg-title" x="380" y="282" text-anchor="middle">Technology</text>
  <text class="itpe-svg-title" x="380" y="310" text-anchor="middle">Sovereignty</text>
  <text class="itpe-svg-sub" x="380" y="342" text-anchor="middle">선택권 · 통제력 · 회복력</text>
  <rect class="itpe-svg-node" x="270" y="25" width="220" height="82" rx="14" />
  <text class="itpe-svg-title" x="380" y="59" text-anchor="middle">Protect</text><text class="itpe-svg-sub" x="380" y="86" text-anchor="middle">핵심자산·공급망 보호</text>
  <path class="itpe-svg-link" d="M380 107 V180" marker-end="url(#arrow-tech-sovereignty)" />
  <rect class="itpe-svg-node" x="35" y="460" width="250" height="82" rx="14" />
  <text class="itpe-svg-title" x="160" y="494" text-anchor="middle">Promote</text><text class="itpe-svg-sub" x="160" y="521" text-anchor="middle">R&amp;D·인재·시장 육성</text>
  <path class="itpe-svg-link" d="M248 460 L310 397" marker-end="url(#arrow-tech-sovereignty)" />
  <rect class="itpe-svg-node" x="475" y="460" width="250" height="82" rx="14" />
  <text class="itpe-svg-title" x="600" y="494" text-anchor="middle">Project</text><text class="itpe-svg-sub" x="600" y="521" text-anchor="middle">표준·동맹·시장 확산</text>
  <path class="itpe-svg-link" d="M512 460 L450 397" marker-end="url(#arrow-tech-sovereignty)" />
</svg>
</div>

<details>
<summary>핵심 용어</summary>

- **Technology Sovereignty**: 핵심기술을 개발하거나 일방적 의존 없이 확보·운용할 수 있는 역량
- **Strategic Autonomy**: 외부 충격 속에서도 국가가 필요한 행동을 선택·지속할 수 있는 능력
- **GVC(Global Value Chain)**: 연구·부품·생산·서비스가 국가 간 분업되는 가치사슬
- **Friend-shoring**: 공급망을 신뢰 가능한 국가·지역 중심으로 재편하는 전략
- **Open Strategic Autonomy**: 개방성과 국제협력을 유지하면서 핵심 의존 위험을 줄이는 접근
- **SBOM(Software Bill of Materials)**: SW 구성요소·버전·의존관계를 기록한 명세

</details>

## 예상문제

> 기술 주권의 개념과 확보전략을 설명하고, 디지털 기술 공급망의 문제점과 대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 일방적 기술 의존을 줄이는 전략적 역량

> 기술 주권은 모든 기술을 국산화하는 폐쇄전략이 아니라, 핵심 기능을 스스로 선택·통제·복구할 수 있도록 의존구조를 관리하는 역량임.

- 정의: 국가가 복지·경쟁력·안보에 중요한 기술을 개발하거나 일방적 구조 의존 없이 조달·운용할 수 있는 역량
- 목적: **공급망 회복력·전략적 자율성·산업경쟁력·공공서비스 연속성** 확보

## Ⅱ. 기술 주권 대상과 통제수단

| 대상 | 주요 의존위험 | 통제수단 |
|---|---|---|
| 반도체·가속기 | 특정 공급자·장비·소재 | 다변화·비축·대체설계·공동 R&D |
| Cloud·Data | 관할권·Lock-in·역외이전 | Portability·암호화·계약·Exit Plan |
| AI·SW | 모델·Library·API 종속 | Open Standard·SBOM·대체모델·평가 |
| Network·보안 | 장비·업데이트·취약점 | 다중공급·인증·패치권한·관제 |
| 인재·지식재산 | 핵심인력·특허 집중 | 인재양성·공동연구·IP 전략 |

## Ⅲ. 기술 주권 확보 절차

<div class="itpe-pipeline is-vertical" role="img" aria-label="기술 주권 확보를 위한 자산 식별부터 재평가까지 절차">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>① 핵심기능 식별</strong><strong>활동</strong><span>국가·산업·서비스 영향과 대체시간 분석</span><strong>산출</strong><span>Critical Function 목록</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>② 의존성 분석</strong><strong>활동</strong><span>공급자·국가·기술·인력·계약 의존 파악</span><strong>산출</strong><span>Dependency Map · 집중도</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>③ 전략 선택</strong><strong>활동</strong><span>내재화·다변화·비축·동맹·수용 결정</span><strong>산출</strong><span>Sovereignty Roadmap</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>④ 실행·실증</strong><strong>활동</strong><span>R&amp;D·조달·표준화·대체전환 시험</span><strong>산출</strong><span>대체기술 · 전환결과</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>⑤ 감시·재평가</strong><strong>활동</strong><span>지정학·시장·취약점·비용 변화 반영</span><strong>산출</strong><span>Risk Dashboard · 개선계획</span></div></div>
</div>

## Ⅳ. 효율성 중심 조달과 기술 주권 조달 비교

| 기준 | 효율성 중심 | 기술 주권 중심 |
|---|---|---|
| 우선가치 | 단기 비용·성능 | 연속성·통제력·대체가능성 |
| 공급구조 | 최적 단일공급 | 다중공급·동맹·내재화 |
| 계약 | 구매·SLA 중심 | Portability·Escrow·Exit 포함 |
| 평가 | 가격·기능 | TCO·집중도·전환시간·회복력 |
| 위험 | 외부충격 취약 | 비용증가·보호주의·고립 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 전면 국산화로 자원 분산 | 핵심기능·병목 중심 선택과 집중 | 투자 효율 향상 |
| 독자규격·갈라파고스화 | 국제표준·Open Source·상호운용 시험 | 생태계 호환 |
| 보조금 의존·시장성 부족 | 공공실증 후 민간 경쟁·성과평가 | 자생력 강화 |
| 공급자 Lock-in | Portability·SBOM·Exit Plan | 전환 가능성 확보 |
| 보호주의·통상마찰 | 위험기반·기술중립·국제공조 | 정책 정당성 강화 |

## Ⅵ. Dependency Budget 기반 제언

`[핵심 통찰]` 기술 주권은 국산 비율이 아니라 특정 공급자가 중단돼도 핵심 기능을 얼마나 빨리 대체·복구할 수 있는가로 평가해야 함.

`나라면` 핵심서비스마다 허용 가능한 공급집중도와 전환시간을 Dependency Budget으로 정하고, 초과 시 다중공급·Portability·대체훈련을 조달조건에 반영하겠음.

<div class="itpe-svg-map">
<svg viewBox="0 0 760 430" role="img" aria-label="기술 의존도 예산을 이용해 유지와 완화를 결정하는 구조">
  <defs><marker id="arrow-dependency-budget" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <rect class="itpe-svg-node" x="170" y="24" width="420" height="72" rx="14" />
  <text class="itpe-svg-title" x="380" y="56" text-anchor="middle">Dependency Map</text><text class="itpe-svg-sub" x="380" y="81" text-anchor="middle">집중도 · 대체성 · 전환시간 · 영향</text>
  <path class="itpe-svg-link" d="M380 96 V142" marker-end="url(#arrow-dependency-budget)" />
  <rect class="itpe-svg-node is-current" x="170" y="150" width="420" height="82" rx="14" />
  <text class="itpe-svg-title" x="380" y="182" text-anchor="middle">Dependency Budget</text><text class="itpe-svg-sub" x="380" y="208" text-anchor="middle">허용 집중도 · 목표 전환시간</text>
  <path class="itpe-svg-link" d="M300 232 V275 H170 V315" marker-end="url(#arrow-dependency-budget)" />
  <path class="itpe-svg-link" d="M460 232 V275 H590 V315" marker-end="url(#arrow-dependency-budget)" />
  <text class="itpe-svg-label" x="210" y="269" text-anchor="middle">이내</text><text class="itpe-svg-label" x="550" y="269" text-anchor="middle">초과</text>
  <rect class="itpe-svg-node" x="50" y="323" width="240" height="70" rx="14" />
  <text class="itpe-svg-title" x="170" y="354" text-anchor="middle">유지·감시</text><text class="itpe-svg-sub" x="170" y="379" text-anchor="middle">비용·성능 최적화</text>
  <rect class="itpe-svg-node" x="470" y="323" width="240" height="70" rx="14" />
  <text class="itpe-svg-title" x="590" y="354" text-anchor="middle">의존 완화</text><text class="itpe-svg-sub" x="590" y="379" text-anchor="middle">다변화 · 대체 · 내재화</text>
</svg>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 핵심기술을 개발하거나 일방적 구조 의존 없이 조달·운용할 수 있는 국가 역량
- 목적: **공급망 회복력·전략적 자율성·산업경쟁력·서비스 연속성** 확보

### 2. 전략

| 전략 | 핵심 |
|---|---|
| Protect | 핵심자산·공급망·IP 보호 |
| Promote | R&amp;D·인재·시장 육성 |
| Project | 표준·동맹·시장 확산 |

### 3. 핵심 통제

- **Dependency Map**: 공급자·국가·기술·계약 의존 가시화
- **Dependency Budget**: 허용 집중도·목표 전환시간 기반 완화 투자

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [OECD, Strategic autonomy and promotion of critical technologies](https://stip.oecd.org/stip/interactive-dashboards/themes/TH111)
- [OECD, Science, technology and innovation policy in times of strategic competition](https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2023_0b55736e-en/full-report/component-6.html)
- [OECD, Digital public goods: Enablers of digital sovereignty](https://www.oecd.org/en/publications/development-co-operation-report-2021_ce08832f-en/full-report/component-41.html)

## 학습 체크

- [ ] Ⅰ: 기술 주권의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 반도체·Cloud·AI·Network·인재의 의존위험을 구분할 수 있는가?
- [ ] Ⅲ: 핵심기능 식별부터 재평가까지 활동과 산출물을 연결할 수 있는가?
- [ ] Ⅳ: 효율성 중심 조달과 기술 주권 조달을 비교할 수 있는가?
- [ ] Ⅴ: 자원분산·고립·Lock-in 위험의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: Dependency Budget을 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [AI 프라이버시 리스크 관리 모델](./054_ai_privacy_risk_management_model.md)
- 연관 토픽: [AI 고속도로](./051_ai_highway.md), [AI 에너지 인프라](./060_ai_energy_infrastructure.md)
- 다음 토픽: [시스템 운영 감리](./059_system_operation_audit.md)
