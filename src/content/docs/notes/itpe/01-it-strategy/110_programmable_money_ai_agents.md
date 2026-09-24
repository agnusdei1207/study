---
title: "Programmable Money·AI Agent 결제"
author: "OpenAI"
date: "2026-09-24T00:00:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-6"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치
현재 위치: IT 전략·관리 → Programmable Money·AI Agent 결제


## 30초 인출

- 본질: Programmable Money·AI Agent 결제는 조건부 결제 처리와 AI 에이전트의 거래 권한을 통제하는 지급 방식
- 메커니즘: 사용자의 목적·한도 설정과 제한된 권한 위임 → 에이전트의 결제 요청 검증 → 지급결제 절차로 전달

<details>
<summary>핵심 용어</summary>

- **Programmable Money·AI Agent 결제** : 결제 조건을 자동 처리하고 에이전트의 거래 권한을 통제하는 지급 방식
- **Programmable Money** : 사용 목적·시점·상대방 등에 제약을 둔 디지털 화폐
- **Programmable Payment** : 정한 조건이 충족될 때 결제 지시가 자동 실행되는 지급 방식
- **AI Agent** : 목표를 받아 도구를 선택·호출하고, 설정된 권한 안에서 여러 작업을 수행하는 소프트웨어 시스템
- **PSP(Payment Service Provider)** : 이용자·가맹점에 지급결제 서비스를 제공하거나 결제망을 연결하는 사업자
- **Conditional Payment** : 상품 인도나 서비스 조건 확인 뒤 대금을 지급하도록 설계한 조건부 결제

</details>

---

## 1교시 예상문제 (10점)

> AI Agent 결제의 권한 위임 구조와 주요 통제를 설명하시오. (예상·10점)

---

## 1교시 10점 답안

### Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Programmable Money·AI Agent 결제**는 조건부 결제 처리와 에이전트의 거래 권한을 통제하는 지급 방식 |
| 목적 | 반복·조건부 거래의 자동화와 위임된 권한 범위 안에서의 결제 실행 |

### Ⅱ. 결제 권한과 실행 흐름

```mermaid
flowchart TD
    U["사용자: 목적·한도·기간 설정"] -->|제한된 권한 위임| A["AI Agent: 거래 요청"]
    A --> P{"정책·한도·수취인 확인"}
    P -->|허용| R["결제 서비스·지급결제망"]
    P -->|거부| X["요청 중단·기록"]
    R --> M["상태·거래기록 반환"]
```

### Ⅲ. 권한 통제

| 통제 지점 | 설계 기준 |
|---|---|
| 위임 권한 | 거래 목적·금액 한도·유효기간·취소 방법을 사전에 설정 |
| 요청 검증 | 수취인·중복 요청·잔액·위험 신호를 지급 전에 확인 |
| 실패 처리 | 거부·시간초과·외부 시스템 오류 시 자동 재시도 범위와 사람 승인 조건의 사전 설정 |

제언: 결제 권한의 한도·유효기간·회수 방법을 먼저 정하고 조건 위반 시 사람 승인으로 전환

---

## 2~4교시 예상문제 (25점)

> Programmable Money와 Programmable Payment의 차이를 설명하고, AI Agent 결제의 권한 위임 구조와 주요 위험·통제방안을 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Programmable Money·AI Agent 결제**는 조건부 결제 처리와 에이전트의 거래 권한을 통제하는 지급 방식 |
| 목적 | 반복·조건부 거래의 자동화와 위임된 권한 범위 안에서의 결제 실행 |

## Ⅱ. Money·Payment 비교

| 구분 | Programmable Money | Programmable Payment |
|---|---|---|
| 규칙이 적용되는 곳 | 화폐 자체의 사용 가능 목적·조건 | 결제 지시와 이체가 실행되는 조건 |
| 예 | 사용처·기간이 제한된 바우처 | 배송 확인 뒤 대금을 지급하는 조건부 결제 |
| 주의점 | 제한된 용도의 화폐가 범용 화폐와 혼동되지 않도록 설계 | 조건 확인·분쟁·환급 절차를 설계 |

디지털 화폐의 형태와 사용처 제한은 별개의 속성. ECB의 디지털 유로 설명에서도 제한된 용도의 화폐와 조건부 결제 지원을 구분.

## Ⅲ. 에이전트 권한 위임과 결제 요청

```mermaid
flowchart TD
    U["사용자: 목적·한도·기간 설정"] -->|제한된 권한 위임| A["AI Agent: 거래 요청"]
    A --> P{"정책·한도·수취인 확인"}
    P -->|허용| R["결제 서비스·지급결제망"]
    P -->|거부| X["요청 중단·기록"]
    R --> M["상태·거래기록 반환"]
```

사용자의 거래 목적·한도·기간·중지 방법 사전 설정. 에이전트 요청의 인증·사기방지 검증과 결제 결과·실패 사유의 사용자 반환. 그림은 제안 아키텍처로, 특정 표준이나 단일 결제망을 뜻하지 않는 구조.

## Ⅳ. 결제 실행 전후의 책임 구분

| 참여자 | 책임 |
|---|---|---|
| 사용자·기관 | 위임할 목적과 한도 설정, 계정·권한 회수 |
| 에이전트 운영자 | 모델·도구 접근 통제, 요청·결과 기록 |
| PSP·결제 서비스 | 본인확인·거래 승인·정산·분쟁 절차 수행 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 |
|---|---|---|
| 에이전트 오류·중복 요청 | 금액·빈도 제한, 요청 식별자와 중복 검사 |
| 자격정보 탈취 | 최소 권한, 안전한 자격정보 저장, 즉시 회수 절차 |
| 수취인·조건 오류 | 승인된 수취인 목록, 독립된 조건 확인, 중요 거래 사람 승인 |
| 분쟁·오결제 | 취소·환급 가능 범위와 이의제기 창구 사전 안내 |

## Ⅵ. 권한 회수와 사람 승인 기준을 먼저 정하는 기술사적 제언

| 문제 | 해결 방안 |
|---|---|
| 포괄적 권한 또는 만료·회수 절차 부재로 인한 오류 거래의 반복 위험 | 시범 적용에서 목적·수취인·건별 한도·유효기간 제한, 조건 위반 시 거래 중지와 사람 승인, 취소·권한 회수 및 책임자 지정 후 단계적 확대 |

## 출제 이력과 검증 출처

- 공식 문제지 원문 확인 전까지 직접 기출로 단정하지 않음
- European Central Bank, [FAQs on the digital euro, Q20: Would the digital euro be programmable money?](https://www.ecb.europa.eu/euro/digital_euro/faqs/html/ecb.faq_digital_euro.en.html)
- European Central Bank, [Preparation phase of a digital euro: Closing report](https://www.ecb.europa.eu/euro/digital_euro/progress/html/ecb.deprp202510.en.html)
- Bank for International Settlements, [AI agents for cash management in payment systems](https://www.bis.org/publ/work1310.pdf)

## 연결 토픽

- 이전: [107. EA·ITA](./107_ea_ita.md)
- 관련: [050. AI 거버넌스 플랫폼](./050_ai_governance_platform.md) · [036. NIST AI RMF](./036_nist_ai_rmf.md)
- 다음: [111. Six Sigma DMAIC](./111_six_sigma_dmaic.md)
