---
title: "Programmable Money·AI Agent 결제"
author: "Claude Code"
date: "2026-09-29T22:52:04+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Sonnet 5.5"
---

## 지식 로드맵 내 현재 위치

IT 전략·관리 → 디지털 트렌드 → **Programmable Money·AI Agent 결제**

## 30초 인출

- 본질: AI 에이전트 결제는 사용자를 대신해 AI 에이전트가 구매·결제를 수행하도록 권한을 위임하는 방식이며, 프로그래머블 머니는 사용처·시기·상대에 제한이 붙은 디지털 화폐
- 메커니즘: 제약을 프로그래머블 머니는 화폐에 붙이고, AP2는 사용자가 서명한 Mandate에 붙여 에이전트의 권한 범위를 정하고 가맹점·결제사가 검증
- 통찰: LLM 기반 에이전트는 비결정적이어서 그 자체가 잠재적 공격자가 되므로, 결제 권한을 서명된 제약과 짧은 만료로 좁혀 위임하고 검증은 결정론적 코드에서 수행

<details>
<summary>핵심 용어</summary>

- **프로그래머블 머니(Programmable money)** : 미리 정한 용도(바우처처럼)로 쓰이며 사용 장소·시기·상대에 제한이 붙은 디지털 형태의 화폐
- **조건부 결제(Conditional payment)** : 배송 확인 뒤 대금을 이체하는 것처럼 조건이 충족될 때 결제가 이뤄지는 방식이며, 화폐 자체가 아닌 결제 절차의 조건
- **AI 에이전트(AI agent)** : 사용자를 대신해 상품 탐색·결제 구성·구매를 수행하는 소프트웨어이며, AP2에서는 LLM이 통신을 처리하면 에이전트형 역할로 분류
- **AP2(Agent Payments Protocol)** : 에이전트가 수행하는 결제 거래를 보호하기 위한 개방형 프로토콜이며 카드·스테이블코인·실시간 계좌이체 등 결제 수단에 독립적
- **Mandate** : 사용자의 지시에 대한 검증 가능한 증거가 되는, 암호학적으로 서명한 디지털 계약이며 Checkout Mandate와 Payment Mandate 두 종류
- **Shopping Agent** : 상품 탐색, 체크아웃 구성, 구매 실행을 수행하는 AP2의 핵심 에이전트
- **Credential Provider** : 결제 자격증명(Payment Credential)의 출처이며 에이전트의 사용 권한을 검증하고 범위를 한정
- **Merchant Payment Processor** : 가맹점 결제를 처리하며 자격증명이 해당 체크아웃에 승인됐는지 검증
- **Trusted Surface** : 사용자의 동의를 받아 서명된 Mandate를 만드는 신뢰된 화면이며 결정론적 코드로 동작해야 하는 역할
- **Human Present·Human Not Present** : 사용자가 체크아웃을 직접 승인하는 방식과, 조건만 미리 승인하고 에이전트가 자율 수행하는 방식

</details>

---

## 2~4교시 예상문제 (25점)

> 프로그래머블 머니와 AI 에이전트 결제의 개념을 설명하고, AI 에이전트 결제의 구조와 보안상 고려사항을 설명하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 프로그래머블 머니와 AI 에이전트 결제의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **프로그래머블 머니** 의 사용처·시기·상대 제한과, 사용자를 대신한 **AI 에이전트** 의 결제 권한을 검증 가능한 증거로 위임하는 결제 |
| 목적 | 자동화된 결제에서 사용자 지시의 범위 보장과 사고 시 책임 소재 확인 |

## Ⅱ. 사람의 클릭을 전제하지 않는 AI 에이전트 결제의 특징

| 특징 | 의미 |
|---|---|
| 클릭 없는 결제 개시 | 기존 결제는 신뢰된 화면에서 사람이 구매를 누른다고 가정하지만, 에이전트가 결제를 개시하면 무너지는 이 가정 |
| 세 가지 물음 | 에이전트에 부여한 구체적 권한의 증명(Authorization), 에이전트 요청과 사용자 의도의 일치(Authenticity), 사고 시 책임 소재(Accountability) |
| 에이전트의 잠재적 위협 | 통신 상대가 LLM 에이전트면 에이전트 자체가 공격자가 될 수 있어 변조 방지 수단 추가 필요 |
| 결제 수단 독립 | 카드·스테이블코인·실시간 계좌이체 등을 같은 프로토콜로 수용 |

## Ⅲ. AI 에이전트 결제의 AP2 체계

### 사용자 승인 방식(Human Present)의 결제 흐름

```text
사용자 ⇄ Trusted Surface ⇄ Shopping Agent
                                ↓ (1) Checkout·Payment Mandate 구성 → 사용자 승인·서명
Credential Provider ← (2) Payment Mandate 검증 → 결제 자격증명 발급
                                ↓
Merchant ← (3) 자격증명 + Checkout Mandate 제출 → 자신이 만든 체크아웃과 대조
                                ↓
Merchant Payment Processor ← (4) 가맹점 개시 결제인 경우 결제 개시
                                ↓
(5) Checkout Receipt·Payment Receipt 반환
```

### 자율 방식(Human Not Present) 확대: 열린 Mandate와 닫힌 Mandate

```text
사용자: 조건(제약)만 승인 → Trusted Surface가 열린 Mandate 서명
        (에이전트 공개키 포함, 만료 시각 설정)
    ↓
Shopping Agent: 체크아웃을 만들고 에이전트 키로 닫힌 Mandate 서명
    ↓
검증자(가맹점·Credential Provider): 열린 Mandate의 제약과 닫힌 Mandate 대조
    ├─ 제약 충족 → 승인, 영수증 반환
    └─ 제약 위반 → 오류 영수증 반환
```

## Ⅳ. 제약을 붙이는 위치의 비교

| 비교축 | 프로그래머블 머니 | 조건부 결제 | AP2의 Mandate 제약 |
|---|---|---|---|
| 제약이 붙는 대상 | 화폐 자체 | 결제 절차 | 에이전트의 권한 |
| 제약 내용 | 사용 장소·시기·상대 | 이체 조건(예: 배송 확인) | 체크아웃·결제가 사용자 의도에 부합하는지 |
| 화폐의 성질 | 용도가 정해진 바우처형 | 일반 화폐 | 결제 수단에 독립 |
| 공식 입장 | ECB는 디지털유로를 프로그래머블 머니로 만들지 않고 조건부 결제만 지원 | ECB가 지원 대상으로 언급 | AP2는 결제 수단이 아닌 권한 검증 프로토콜 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| LLM 에이전트의 비결정성으로 에이전트 자체가 잠재적 공격자가 되는 구조 | 검증·처리는 에이전트형 역할이라도 결정론적 코드에서 수행하고 Trusted Surface는 비에이전트형으로 구성 |
| 자율 방식에서 한 번 서명한 열린 Mandate로 여러 체크아웃이 승인될 위험 | 열린 Mandate에 제약과 에이전트 공개키를 담고 만료를 과업 완료에 필요한 최소값으로 설정하며 직전 Mandate의 거부 영수증 없이는 다음 Mandate 제시 금지 |
| 분쟁 해결·증거 보관·조회 요건이 프로토콜의 범위 밖 | Checkout·Payment Mandate와 영수증을 분쟁 증거로 묶어 쓰되 보관·조회 정책은 이용 기관이 별도 마련 |

## Ⅵ. 제언

에이전트에 위임하는 결제 권한을 서명된 제약과 짧은 만료로 좁히고 검증은 결정론적 코드에 맡기는 최소 권한 위임

### 신뢰 경계

```text
[신뢰하지 않는 영역]  LLM 기반 Shopping Agent
        │  닫힌 Mandate + 열린 Mandate(제약·만료)
        ▼
[신뢰 영역]  결정론적 코드의 검증
        ├─ 서명·해시 검증
        ├─ 제약 충족 평가
        └─ 영수증 반환
```

### 제약 검증 확대: 열린 Mandate 사용 판정

```text
닫힌 Mandate 수신
    ↓
열린 Mandate의 사용자 서명 검증
    ├─ 실패 → 거부 영수증
    └─ 성공
         ↓
체크아웃·결제가 제약에 부합
    ├─ 아니오 → 거부 영수증 (에이전트는 이 영수증을 받은 뒤에야 다음 Mandate 제시 가능)
    └─ 예 → 승인 영수증
```

| 구분 | 에이전트에 포괄 위임 | 제언: 제약·만료를 붙인 위임 |
|---|---|---|
| 권한 범위 | 에이전트 판단에 의존 | 사용자가 서명한 제약 |
| 검증 주체 | 에이전트의 자기 보고 | 결정론적 코드 |
| 사고 시 근거 | 에이전트 로그 | 서명된 Mandate와 영수증 |

## 출제 이력과 검증 출처

- Q-net 제132~140회 문제지에서 프로그래머블 머니·AI 에이전트 결제를 직접 묻는 문항 없음
- 유럽중앙은행(ECB), FAQs on the digital euro, Q20 — 프로그래머블 머니의 정의와 조건부 결제(2026.8.17. 갱신본)
- AP2(Agent Payments Protocol) Specification v0.2 — 역할·Mandate·Human Present·Human Not Present·검증 규칙
- Google Cloud Blog, Announcing Agent Payments Protocol (AP2), 2025.9.17. — 권한·진위·책임의 세 물음과 지원 결제 수단

## 연결 토픽

- 이전 토픽: [EA·ITA](./107_ea_ita.md)
- 연관 토픽: [AI 거버넌스 플랫폼](./050_ai_governance_platform.md), [NIST AI RMF](./036_nist_ai_rmf.md)
- 다음 토픽: [Six Sigma DMAIC](./111_six_sigma_dmaic.md)
