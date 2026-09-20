---
title: "프로그래머블 머니 (AI 에이전트의 경제 주체화)"
author: "Codex"
date: "2026-09-20T19:33:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 미래 금융 혁신 및 AI 트렌드를 거쳐 프로그래머블 머니로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>미래 금융 혁신·AI 트렌드</span>
  <strong>프로그래머블 머니 (AI 에이전트의 경제 주체화)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 화폐에 **스마트 계약** 코드를 심어 사람의 수동 개입 없이 자율 **AI 에이전트** 간 실시간 가치 교환과 정산을 가능하게 하는 디지털 통화
- 메커니즘: AI 간 서비스 협상 → 조건부 에스크로 락업 → **ERC-4337(계정 추상화)** 지출 서명 → **초미세 결제(Micro-payment)** 및 원장 동시 정산
- 산출: 에이전트 스마트 지갑 명세서 · 조건부 에스크로 컨트랙트 · 온체인 거래 영수증 · 지출 한도 가드레일 정책서

<div class="itpe-flow-map" role="img" aria-label="AI 에이전트 경제에서 스마트 계약과 프로그래머블 머니를 통한 실시간 결제 정산 아키텍처">
  <div class="itpe-flow-node">
    <strong>AI 에이전트 경제 (Agentic Economy)</strong>
    <small>구매 AI (GPU/데이터 요청) ↔ 판매 AI (API 엔드포인트 제공)</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>자율 서명 및 정책 가드레일</small></div>
  <div class="itpe-flow-node is-current">
    <strong>스마트 계약 및 지출 가드레일</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>지갑</strong><span><span class="itpe-keyword"><strong>ERC-4337</strong></span> 계정 추상화 (세션 키 기반 위임)</span></div>
      <div class="itpe-flow-branch"><strong>통제</strong><span>시간당/일일 지출 쿼터(Rate-limit) · SLA 검증</span></div>
      <div class="itpe-flow-branch"><strong>실행</strong><span>조건 충족 시 조건부 에스크로 자금 자동 릴리스</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>원장 기록</small></div>
  <div class="itpe-flow-node">
    <strong>프로그래머블 머니 결제 원장</strong>
    <small>토큰화 예금 · 스테이블코인 · <span class="itpe-keyword"><strong>CBDC</strong></span> 실시간 동시 정산(DvP)</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **프로그래머블 머니(Programmable Money)**: 화폐 단위 자체에 비즈니스 로직(스마트 계약)을 내장하여 사전 정의된 조건 만족 시 자동으로 결제·정산되는 디지털 화폐
- **Agentic Economy(에이전트 경제)**: 자율 AI 에이전트가 소프트웨어 API, 컴퓨팅 파워, 데이터 자산을 직접 구매·소비하는 기계 중심 경제 체계
- **스마트 계약(Smart Contract)**: 블록체인 상에서 사전 정의된 조건이 충족되면 제3자의 중개 없이 자동으로 실행되는 불변의 프로그램 코드
- **ERC-4337(Account Abstraction)**: 스마트 컨트랙트를 지갑으로 활용하여 세션 키 기반 소액 자동 결제와 지출 한도 설정을 가능케 하는 이더리움 표준
- **CBDC(Central Bank Digital Currency)**: 중앙은행이 직접 발행하는 디지털 형태의 법정 통화로, 도매형(기관 간 결제)과 소매형으로 구분
- **Micro-payment(초미세 결제)**: 신용카드 고정 수수료 체계로는 불가능한 $0.001 이하 센트 단위의 초소액 실시간 거래

</details>

## 예상문제

> 생성형 AI 에이전트가 자율적으로 API 및 컴퓨팅 자원을 구매·소비하는 경제 주체로 부상함에 따라 주목받는 '프로그래머블 머니(Programmable Money)'의 개념, 핵심 기술 아키텍처, 스마트 계약 기반의 자율 결제 메커니즘, 보안 및 규제 이슈와 대응 방안을 설명하시오. (25점)

## Ⅰ. 기계 경제(Machine Economy)의 혈관, 프로그래머블 머니의 개요

> 인간 개입 없는 **기계 간 자율 상거래(M2M)**를 위해 화폐에 **스마트 계약**을 내장하여 **초미세 결제(Micro-payment)**와 동시 정산을 실현함.

- 정의: 화폐 단위 자체에 프로그래밍 코드(**스마트 계약**)와 실행 조건을 내장하여, 특정 조건 충족 시 사람의 개입 없이 자율적으로 결제·정산이 집행되는 **기계 경제(Machine Economy) 특화 디지털 화폐 체계**
- 목적: 전통 금융망의 인간 인증 병목과 고정 수수료를 제거하고, 자율 **AI 에이전트** 간 실시간 가치 교환 및 **원장 동시 정산(DvP)**을 구현

## Ⅱ. 프로그래머블 머니 3계층 아키텍처 및 4단계 자율 결제 프로세스

> 에이전트 간 협상에서 조건부 에스크로 예치, 서비스 수행, 결과 검증 후 즉시 정산으로 이어지는 파이프라인을 운영함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="프로그래머블 머니 기반 AI 에이전트 자율 결제 4단계 프로세스">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 서비스 탐색 및 온체인 협상</strong></span>
    <small>서비스 레지스트리 검색, 단가/SLA 협상 및 스마트 계약 초안 생성<br />→ 자율 계약 조건 명세서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 조건부 에스크로 자금 예치</strong></span>
    <small>ERC-4337 지갑 서명, 스마트 계약에 대금 락업 및 지출 한도 검증<br />→ 에스크로 스마트 컨트랙트 생성</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 서비스 수행 및 페이로드 전달</strong></span>
    <small>약정된 SLA에 맞춰 GPU 추론 연산 결과 반환 또는 데이터 스트리밍<br />→ 암호화된 결과 페이로드 수신</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 암호학적 검증 및 즉시 정산</strong></span>
    <small>결과물 해시 및 SLA 무결성 확인 시 판매자 지갑으로 자금 즉시 릴리스<br />→ 온체인 트랜잭션 영수증 (DvP 정산 완결)</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>정산 무결성</strong></span> · 에이전트 계약 ↔ 스마트 계약 가드레일 ↔ 블록체인 최종성(Finality) 100% 보증</div>

### 3계층 아키텍처 구성요소

| 아키텍처 계층 | 핵심 기술 및 구성요소 | 주요 기능 및 역할 |
|---|---|---|
| **1. 에이전트 계층** | LLM 오케스트레이터, Agent Protocol, 온체인 서비스 레지스트리 | 자율 서비스 탐색, 실시간 가격 협상, API 호출 계약 발주 |
| **2. 가드레일 계층** | **ERC-4337(계정 추상화) 지갑**, 지출 쿼터 모듈, 오라클(Chainlink) | AI 오작동 지출 방어, SLA 충족 여부 검증, 조건부 에스크로 집행 |
| **3. 결제 원장 계층** | 이더리움 L2 롤업, 토큰화 예금, 중앙은행 도매형 **CBDC** 네트워크 | 가스비 최소화 초미세 결제 지원 및 실시간 동시 정산(DvP) |

## Ⅲ. 전통 전자화폐 vs 프로그래머블 머니 비교

> 전통 화폐는 인간의 수동 인증과 배치 정산 중심이나, 프로그래머블 머니는 코드 실행과 실시간 동시 정산 중심임.

| 비교 항목 | 전통 전자화폐 (신용카드, 간편결제) | 프로그래머블 머니 (Smart Money) |
|---|---|---|
| **주요 결제 주체** | 사람 (사용자 본인 인증 및 OTP 필수) | **소프트웨어 코드, 자율 AI 에이전트, 기계** |
| **실행 메커니즘** | 중앙 집중형 금융 결제망 (PG사, 은행망) | **스마트 계약(Smart Contract)** 기반 조건부 자동 실행 |
| **거래 수수료** | 건당 고정 수수료 + 정률 (마이크로 결제 불가) | L2 블록체인 기반 극소 가스비 (**마이크로센트 결제 실현**) |
| **정산 주기** | 영업일 기준 T+1 ~ T+3일 배치 정산 | **결제와 동시에 원장에 최종 기록되는 실시간 정산(DvP)** |
| **화폐의 상태성** | 정적 가치 저장 및 단순 잔고 이동 | **지출 조건, 유효기간, SLA 제약이 화폐 코드 내 내장** |

## Ⅳ. 실무 적용 시 보안·규제 위험 요인 및 통제 대책

> AI 환각으로 인한 무한 결제 루프와 스마트 계약 취약점을 방어하기 위해 지출 쿼터와 DID를 결합해야 함.

| 위험 문제점 | 발생 원인 | 공학적·제도적 해결 대책 | 기대 효과 |
|---|---|---|---|
| **AI 환각에 의한 잔고 탕진** | 프롬프트 루프 오류로 불필요한 고비용 API를 초당 수백 회 무한 호출 | ERC-4337 지갑 내 **Session Key 기반 시간당/일일 지출 한도(Rate-limit)** 및 서킷브레이커 | 돌발적 재정 손실 원천 차단 |
| **스마트 계약 해킹** | 에스크로 컨트랙트의 재진입(Reentrancy) 결함으로 예치 자금 탈취 | 정적 분석 도구(Slither) 검증 및 다중 서명(Multi-sig) 오라클 합의 강제 | 금융 자산 탈취 방지 |
| **법인격 부재에 따른 규제 위반** | 법적 주체가 아닌 AI의 거래로 인한 자금세탁(AML) 및 실명 확인(KYC) 위반 | AI 에이전트와 법인/인간 소유자를 1:1 매핑하는 **탈중앙 식별자(DID)** 발급 의무화 | 금융 법률 준수 및 법적 책임 명확화 |

## Ⅴ. 안전한 기계 경제 구축을 위한 기술사적 제언

> 무제한 자율성을 차단하기 위해 세션 키 기반 권한 위임과 제도권 토큰화 예금을 결제 레일로 채택해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: AI 에이전트가 고도화될수록 기계는 인간에게 신용카드 OTP 번호를 묻지 않을 것임. AI가 진정한 자율성을 갖춘 경제 주체로 도약하기 위한 마지막 퍼즐 조각은 바로 '기계 친화적 네이티브 화폐'인 프로그래머블 머니임.
- 나라면: AI 에이전트에 지갑 마스터 키를 주지 않고, [ERC-4337의 Session Key] 기술을 활용하여 지정된 기간 동안 사전 승인된 화이트리스트 스마트 계약에만 소액 지출을 허용하는 '권한 위임 샌드박스'를 구축하고, 암호화폐 가격 변동성 위험을 차단하기 위해 중앙은행 도매형 CBDC 및 인가된 토큰화 예금만을 결제 통화로 강제하겠음.

### 실전 답안용 기술사적 제언

- 판정: 무제한적 자율 결제를 배제하고 세션 키 기반 지출 가드레일과 제도권 통화 레일로 전환
- 대안: **ERC-4337 Session Key 지출 한도 제어** 및 **도매형 CBDC/토큰화 예금 연계**
- 검증: 일일 지출 한도 초과 차단율 100% · 스마트 계약 정적 취약점 0건
- 효과: AI 에이전트 폭주 손실 원천 차단 · 규제 준수 기반 안전한 기계 경제(Machine Economy) 구현

<div class="itpe-pipeline is-vertical" role="img" aria-label="프로그래머블 머니 기반 안전한 AI 경제 구축 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>인간 본인인증 필수 · 신용카드 고정 수수료로 AI 초미세 결제 수용 불가</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>스마트 계약 내장형 프로그래머블 머니 + ERC-4337 계정 추상화 도입</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>Session Key 기반 지출 쿼터 통제 · DID 연계 소유자 실명 추적성</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>API 센트 단위 초미세 결제 실현 · 마찰 없는 자율 기계 경제 안착</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 화폐 단위 자체에 **스마트 계약** 코드를 내장하여 특정 비즈니스 조건 충족 시 사람 개입 없이 자동 결제·정산되는 **기계 경제(Machine Economy) 특화 디지털 화폐**
- 목적: 인간 인증 병목과 고정 수수료를 제거하고 자율 **AI 에이전트** 간 **초미세 결제(Micro-payment)** 및 실시간 정산을 실현

### 2. 구성체계 및 결제 파이프라인

<div class="itpe-pipeline is-vertical" role="img" aria-label="프로그래머블 머니 자율 결제 요약">
  <div class="itpe-pipeline-node"><strong>에이전트 계층</strong><small>온체인 서비스 탐색 · 가격/SLA 자율 협상</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>가드레일 계층</strong><small>ERC-4337 세션 키 · 지출 쿼터 · 에스크로</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>결제 원장 계층</strong><small>토큰화 예금 · 도매형 CBDC · 실시간 동시 정산(DvP)</small></div>
</div>

### 3. 핵심 통제

- **Session Key 지출 쿼터**: AI 에이전트의 오작동 및 무한 루프 호출 시 일일 지출 한도 차단
- **DID 연계 책임성**: AI 에이전트를 인간/법인 소유자와 온체인 DID로 매핑하여 금융 규제(AML/KYC) 준수

## 출제 이력과 검증 출처

- 시사·트렌드 출제 예상 토픽: AI 에이전트의 경제 주체화 및 프로그래머블 머니
- [Bank for International Settlements(BIS), Blueprint for the future monetary system](https://www.bis.org)
- [Ethereum Foundation, ERC-4337: Account Abstraction Using Alt Mempool](https://eips.ethereum.org)

## 학습 체크

- [ ] 프로그래머블 머니의 4대 핵심 특징과 전통 전자화폐와의 차이점을 설명할 수 있는가?
- [ ] AI 에이전트 자율 결제 아키텍처의 3계층 구조를 도식화할 수 있는가?
- [ ] ERC-4337(계정 추상화)과 Session Key를 활용한 지출 가드레일 설계 방안을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [EA/ITA](./107_ea_ita.md)
- 연관 토픽: [AI 거버넌스 플랫폼](./050_ai_governance_platform.md), [NIST AI RMF](./036_nist_ai_rmf.md)
- 다음 토픽: [6시그마(Six Sigma) DMAIC](./111_six_sigma_dmaic.md)
