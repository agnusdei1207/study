---
title: "Programmable Money·AI Agent 결제"
author: "OpenAI Codex"
date: "2026-09-22T11:05:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 디지털 금융과 AI Agent를 거쳐 Programmable Money로 이어지는 위치">
  <span>IT 전략·관리</span><span>디지털 금융·AI(Artificial Intelligence) Agent</span><strong>Programmable Money·Payment</strong>
</div>

## 큰 그림과 30초 인출

- **구분**: 화폐 사용조건을 제한하는 Programmable Money ≠ 결제 실행조건을 자동화하는 Programmable Payment
- **구조**: Agent 권한 → 정책검사 → 조건부 결제 → 원장 정산 → 감사
- **통제**: 소유자 책임·최소권한·지출한도·거래상대방·취소·분쟁처리

<div class="itpe-svg-map">
<svg viewBox="0 0 760 520" role="img" aria-label="AI Agent 조건부 결제 구조">
  <defs><marker id="pay-arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" class="itpe-svg-link"></path></marker></defs>
  <rect x="250" y="25" width="260" height="80" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="58" text-anchor="middle" class="itpe-svg-title">인간·법인 소유자</text><text x="380" y="86" text-anchor="middle" class="itpe-svg-sub">목적·예산·책임 위임</text>
  <rect x="250" y="155" width="260" height="80" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="188" text-anchor="middle" class="itpe-svg-title">AI Agent</text><text x="380" y="216" text-anchor="middle" class="itpe-svg-sub">탐색·선택·결제 요청</text>
  <rect x="250" y="285" width="260" height="95" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="380" y="320" text-anchor="middle" class="itpe-svg-title">Policy Engine</text><text x="380" y="350" text-anchor="middle" class="itpe-svg-sub">한도·상대방·목적·승인</text>
  <rect x="55" y="425" width="280" height="70" rx="14" class="itpe-svg-node"></rect>
  <text x="195" y="468" text-anchor="middle" class="itpe-svg-title">조건부 결제 실행</text>
  <rect x="425" y="425" width="280" height="70" rx="14" class="itpe-svg-node"></rect>
  <text x="565" y="468" text-anchor="middle" class="itpe-svg-title">원장 정산·감사로그</text>
  <path d="M380 105 L380 155" class="itpe-svg-link" marker-end="url(#pay-arrow)"></path>
  <path d="M380 235 L380 285" class="itpe-svg-link" marker-end="url(#pay-arrow)"></path>
  <path d="M330 380 L195 425" class="itpe-svg-link" marker-end="url(#pay-arrow)"></path>
  <path d="M430 380 L565 425" class="itpe-svg-link" marker-end="url(#pay-arrow)"></path>
</svg>
</div>

<details>
<summary>약어·전문용어</summary>

- **Programmable Money**: 화폐 단위 자체의 사용처·기간·지역 등에 조건이 부여된 디지털 화폐
- **Programmable Payment**: 조건 충족 시 결제지시를 자동 실행하는 기능
- **AI(Artificial Intelligence) Agent**: 목표와 권한 범위에서 도구를 사용해 과업을 수행하는 인공지능 시스템
- **CBDC(Central Bank Digital Currency)**: 중앙은행이 발행하는 디지털 형태의 중앙은행 화폐
- **DvP(Delivery versus Payment)**: 자산 인도와 대금 지급을 조건부로 연계하는 결제 방식
- **KYC(Know Your Customer)**: 고객 신원 확인 절차
- **AML(Anti-Money Laundering)**: 자금세탁 방지 통제
- **PSP(Payment Service Provider)**: 지급결제 서비스를 제공하는 사업자
- **RACI(Responsible, Accountable, Consulted, Informed)**: 역할별 수행·책임·협의·통보 관계를 정한 표

</details>

## 예상문제

> **(미출제 예상·25점)** Programmable Money와 Programmable Payment의 차이를 설명하고, AI Agent 결제 구조와 위험·통제방안을 제시하시오.

## Ⅰ. 개요

> AI Agent는 독립적 법적 주체라기보다 인간·법인이 정한 권한 안에서 결제 요청을 실행하는 대리 시스템으로 설계해야 함

- **정의**: Programmable Money는 화폐의 사용조건을, Programmable Payment는 결제지시의 실행조건을 코드로 통제하는 방식
- **목적**: 조건부 거래 자동화·정산 효율화·기계 간 소액거래 지원

## Ⅱ. Money·Payment 비교

| 기준 | Programmable Money | Programmable Payment |
|---|---|---|
| 조건 대상 | 화폐 단위 | 결제지시·업무규칙 |
| 제약 | 사용처·기간·지역 등 | 지급시점·검수·승인 등 |
| 쟁점 | 화폐 단일성·범용성 | 오류·취소·분쟁·책임 |
| 예시 | 목적 제한형 Voucher | Pay-on-delivery·Escrow |

CBDC·토큰화 예금·Stablecoin은 구현 가능한 결제자산의 유형이며, 그 자체만으로 Programmable Money라고 단정하지 않음.

## Ⅲ. AI Agent 결제 절차

> Agent 판단과 자금 집행을 분리하고 독립 Policy Engine이 최종 권한을 검사함

<div class="itpe-pipeline is-vertical" role="img" aria-label="AI Agent 조건부 결제 절차">
  <div class="itpe-flow-node"><strong>① 권한 위임</strong><div class="itpe-step-detail"><strong>활동</strong><span>목적·한도·상대방·기간 정의</span></div><div class="itpe-step-detail"><strong>산출</strong><span>위임정책·승인규칙</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>② 거래 요청</strong><div class="itpe-step-detail"><strong>활동</strong><span>서비스·가격·조건 선택</span></div><div class="itpe-step-detail"><strong>산출</strong><span>결제요청·거래문맥</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current"><strong>③ 정책·위험 검사</strong><div class="itpe-step-detail"><strong>판정</strong><span>한도·KYC·AML·Fraud·추가승인</span></div><div class="itpe-step-detail"><strong>산출</strong><span>승인·차단·보류</span></div></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>④ 조건부 실행·정산</strong><div class="itpe-step-detail"><strong>활동</strong><span>조건 검증·지급·원장 기록</span></div><div class="itpe-step-detail"><strong>산출</strong><span>영수증·감사로그</span></div></div>
</div>

## Ⅳ. 결제수단별 특성

| 수단 | 강점 | 주요 위험 |
|---|---|---|
| Tokenised Deposit | 은행 예금 기반·액면 상환 | 은행 간 상호운용성 |
| Stablecoin | 개방형 네트워크 활용 | 준비자산·가격·규제 |
| Wholesale CBDC | 중앙은행 화폐 결제 | 접근범위·시스템 연계 |
| 기존 지급결제망 | 법·운영체계 성숙 | API·소액거래 제약 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| Agent 오판·반복 결제 | 한도·속도제한·Circuit Breaker | 손실 범위 제한 |
| 권한 탈취 | 단기자격·키 격리·거래서명 | 자금 접근 보호 |
| 상대방·서비스 사기 | Allowlist·평판·Escrow | 거래위험 감소 |
| 책임 불명확 | 소유자·운영자·PSP의 RACI | 분쟁 책임 명확화 |
| 취소 불가·오라클 오류 | 보류·취소·이의제기 절차 | 소비자·기업 보호 |

## Ⅵ. 결론·기술사적 제언

> **[핵심 통찰]** Agent의 자율성은 지갑 보유가 아니라, 책임주체가 승인한 정책 안에서 취소·감사 가능한 결제를 수행하는 능력으로 정의해야 함.

> **나라면** Agent에 Master Key를 주지 않고 거래별 단기 권한을 발급하며, 금액·상대방·목적·위험도에 따라 자동승인·추가승인·차단을 분기하겠음.

<div class="itpe-svg-map">
<svg viewBox="0 0 760 470" role="img" aria-label="AI Agent 결제 위험도별 승인 분기">
  <rect x="250" y="25" width="260" height="85" rx="14" class="itpe-svg-node is-current"></rect>
  <text x="380" y="60" text-anchor="middle" class="itpe-svg-title">Policy·Risk 판정</text><text x="380" y="88" text-anchor="middle" class="itpe-svg-sub">금액·상대방·목적·행동</text>
  <rect x="25" y="300" width="210" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="130" y="338" text-anchor="middle" class="itpe-svg-title">저위험</text><text x="130" y="366" text-anchor="middle" class="itpe-svg-sub">자동승인</text>
  <rect x="275" y="300" width="210" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="380" y="338" text-anchor="middle" class="itpe-svg-title">중위험</text><text x="380" y="366" text-anchor="middle" class="itpe-svg-sub">인간 추가승인</text>
  <rect x="525" y="300" width="210" height="90" rx="14" class="itpe-svg-node"></rect>
  <text x="630" y="338" text-anchor="middle" class="itpe-svg-title">고위험</text><text x="630" y="366" text-anchor="middle" class="itpe-svg-sub">차단·조사</text>
  <path d="M330 110 L130 300 M380 110 L380 300 M430 110 L630 300" class="itpe-svg-link"></path>
</svg>
</div>

## 1교시 10점 답안 발췌

- **정의**: Programmable Money는 화폐 사용조건을, Programmable Payment는 결제 실행조건을 코드로 통제하는 방식
- **목적**: 조건부 거래 자동화·정산 효율화·기계 간 소액거래 지원

| 통제층 | 핵심 |
|---|---|
| 권한 | 목적·한도·상대방·기간 |
| 위험 | KYC·AML·Fraud·추가승인 |
| 정산 | 조건검증·지급·원장·감사 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- [ECB, Progress on the investigation phase of a digital euro](https://www.ecb.europa.eu/euro/digital_euro/timeline/profuse/shared/pdf/ecb.degov230424_progress.en.pdf)
- [BIS, Pushing the monetary frontier: stablecoins and tokenised deposits](https://www.bis.org/speeches/20260828-pushing-monetary-frontier-stablecoins-and-tokenised-deposits)
- [Ethereum, ERC-4337](https://eips.ethereum.org/EIPS/eip-4337)

## 학습 체크

- [ ] Ⅰ: Programmable Money·Payment의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: Money와 Payment의 조건 대상·쟁점을 비교할 수 있는가?
- [ ] Ⅲ: 권한 위임부터 정산까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅳ: 결제수단별 강점·위험을 비교할 수 있는가?
- [ ] Ⅴ: 오판·탈취·사기·책임·취소 위험의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: 위험도별 승인 분기를 그릴 수 있는가?

## 연결 토픽

- 이전: [107. EA·ITA](./107_ea_ita/)
- 관련: [050. AI 거버넌스 플랫폼](./050_ai_governance_platform/) · [036. NIST AI RMF](./036_nist_ai_rmf/)
- 다음: [111. Six Sigma DMAIC](./111_six_sigma_dmaic/)
