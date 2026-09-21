---
title: "Programmable Money·AI Agent 결제"
author: "Antigravity"
date: "2026-09-22T11:05:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "Gemini 3.8 Flash"
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

## Ⅲ. AI Agent 결제 아키텍처 및 절차

```
[인간 소유자] ──(세션키/예산/한도 위임)──> [AI Agent] ──(결제지시)──> [Policy Engine]
                                                                        │
┌─────────────────────────── 조건 검증 통과 시 ─────────────────────────┘
▼
[조건부 실행 (스마트컨트랙트/Escrow)] ──(DvP 정산)──> [결제원장(CBDC/토큰예금)] + 감사로그
```

<div class="itpe-svg-map">
<svg viewBox="0 0 520 220" role="img" aria-label="AI Agent 프로그래머블 결제 아키텍처">
  <!-- 배경 바운더리 -->
  <rect x="10" y="10" width="500" height="200" rx="8" fill="var(--sl-color-bg)" stroke="var(--sl-color-hairline)" stroke-width="1.5" />

  <!-- 1. 소유자 위임 -->
  <rect x="25" y="25" width="135" height="75" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="92" y="47" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">인간·법인 소유자</text>
  <text x="92" y="65" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">Session Key 위임</text>
  <text x="92" y="82" text-anchor="middle" font-size="9" fill="var(--sl-color-accent)">최대 한도·사용처 지정</text>

  <!-- 화살표 1 -> 2 -->
  <line x1="160" y1="62" x2="190" y2="62" stroke="var(--sl-color-accent)" stroke-width="1.5" />

  <!-- 2. AI Agent -->
  <rect x="190" y="25" width="140" height="75" rx="6" fill="var(--sl-color-accent-low)" stroke="var(--sl-color-accent)" stroke-width="1.5" />
  <text x="260" y="47" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-accent-high)">AI Agent (대리인)</text>
  <text x="260" y="65" text-anchor="middle" font-size="9" fill="var(--sl-color-text)">API 기반 가격/조건 탐색</text>
  <text x="260" y="82" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">단기 권한 서명 트랜잭션</text>

  <!-- 화살표 2 -> 3 -->
  <line x1="330" y1="62" x2="360" y2="62" stroke="var(--sl-color-accent)" stroke-width="1.5" />

  <!-- 3. Policy Engine (가드레일) -->
  <rect x="360" y="25" width="135" height="75" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="427" y="47" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">Policy Engine (Gate)</text>
  <text x="427" y="65" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">AML / KYC / 한도 검증</text>
  <text x="427" y="82" text-anchor="middle" font-size="9" fill="var(--sl-color-accent)">Circuit Breaker 가동</text>

  <!-- 수직 연결선 -->
  <line x1="427" y1="100" x2="427" y2="125" stroke="var(--sl-color-accent)" stroke-width="1.5" />

  <!-- 하단 1. 조건부 스마트 컨트랙트 -->
  <rect x="25" y="125" width="240" height="70" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="145" y="147" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">조건부 실행 (Smart Contract)</text>
  <text x="145" y="165" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">DvP(인도-대금동시지급) &amp; 에스크로</text>
  <text x="145" y="182" text-anchor="middle" font-size="9" fill="var(--sl-color-accent)">오라클 검증(배송완료 등)</text>

  <!-- 연결선 -->
  <line x1="265" y1="160" x2="285" y2="160" stroke="var(--sl-color-accent)" stroke-width="1.5" />

  <!-- 하단 2. 결제 정산 원장 & 감사 -->
  <rect x="285" y="125" width="210" height="70" rx="6" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-4)" stroke-width="1" />
  <text x="390" y="147" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--sl-color-text)">결제원장 및 감사로그</text>
  <text x="390" y="165" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-2)">CBDC / 토큰예금 확정 정산</text>
  <text x="390" y="182" text-anchor="middle" font-size="9" fill="var(--sl-color-accent)">불가역 감사 추적 (Audit Trail)</text>
</svg>
</div>

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

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]** Agent의 자율성은 자체 지갑 보유가 아니라, 책임주체(Principal)가 부여한 정책 범위 안에서 실시간 차단·취소·감사가 가능한 통제 거버넌스 위에서만 성립한다.
> 
> **나라면** AI Agent에 Master Key를 절대 위임하지 않고 ERC-4337 기반의 계정 추상화(Smart Account)와 세션 키(Session Key)를 적용하겠음. 이를 통해 건당 $50 미만 반복 결제는 허용하되 이상 패턴 탐지 시 서킷 브레이커로 자동 동결하는 안전망을 구축하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: AI Agent 결제 시스템 구축 시 1건당 결제액 $100 초과 또는 이상 탐지 점수 70점 이상 시 인간 승인(Human-in-the-Loop) 필수 전환
- **대응 방안**: ERC-4337 계정 추상화 기반 권한 위임, 화이트리스트(Allowlist) 가맹점 한정 결제 허용 및 자동 서킷 브레이커(Circuit Breaker) 탑재
- **검증 체계**: 스마트 컨트랙트 보안 감사(Audit) 3중 교차 검증 및 트랜잭션 단위 불가역 WORM 감사로그 정합성 실시간 검증
- **기대 효과**: 기계 간(M2M) 초소액 결제(Micro-payment) 자동화 효율 90% 달성 및 비정상 오발주·금융 사고 리스크 제로화

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

- 이전: [107. EA·ITA](./107_ea_ita.md)
- 관련: [050. AI 거버넌스 플랫폼](./050_ai_governance_platform.md) · [036. NIST AI RMF](./036_nist_ai_rmf.md)
- 다음: [111. Six Sigma DMAIC](./111_six_sigma_dmaic.md)

