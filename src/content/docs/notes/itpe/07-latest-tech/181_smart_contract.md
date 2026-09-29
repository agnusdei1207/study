---
title: "스마트 계약(Smart Contract)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "181. 스마트 계약"
  order: 181
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

<div class="itpe-topic-path" aria-label="지식 경로">
  <span class="itpe-path-step">07 최신기술</span>
  <span class="itpe-path-step">블록체인·분산원장</span>
  <span class="itpe-path-step">스마트 계약</span>
</div>

## 30초 인출

- 본질: 분산원장(블록체인) 상에 불변의 바이트코드로 배포되어 사전 정의된 조건이 충족되면 신뢰할 수 있는 제3자(TTP) 없이 코드가 자율 실행되고 원장 상태를 갱신하는 결정론적(Deterministic) 프로그램.
- 메커니즘: 고수준 언어(Solidity) 작성 및 컴파일 → 서명된 배포 트랜잭션 전파 → EVM 가상머신 바이트코드 적재 → 조건 충족 트랜잭션 호출 → 가스(Gas) 한도 검증 및 상태 전이 합의 기록.
- 통찰: 배포 후 코드 수정이 불가능한 블록체인의 불변성으로 인해 취약점 노출 시 영구적 자산 탈취가 발생하므로 CEI 패턴 강제화 및 탈중앙 오라클(DON) 연계 기반 형식 검증 체계 확립 필수.

<details><summary>핵심 용어</summary>

- **가스(Gas) :** 스마트 계약의 연산 및 스토리지 사용량을 측정하는 기본 단위로 악의적인 무한 루프 공격(정지 문제)을 방지하는 경제적 억제 메커니즘.
- **오라클 문제(Oracle Problem) :** 온체인 분산원장이 폐쇄적 결정론 환경에 갇혀 실세계 외부 데이터(주가, 날씨, 물류)의 진실성을 자체 증명하지 못하는 한계.
- **재진입 공격(Reentrancy Attack) :** 외부 컨트랙트로 이더를 전송하는 과정에서 상태 변수 차감 전에 호출자 컨트랙트가 재귀적으로 인출 함수를 재호출하여 잔고를 탈취하는 취약점.
- **CEI 패턴(Checks-Effects-Interactions) :** 함수의 유효성 검사(Checks) 후 내부 상태를 먼저 변경(Effects)하고 마지막에 외부 호출(Interactions)을 수행하는 안전 코딩 규칙.

</details>

---

## 2~4교시 예상문제 (25점)

블록체인 스마트 계약(Smart Contract)의 개념, 작동 아키텍처 및 EVM 실행 원리, 비트코인 스크립트와의 차이점, 오라클 문제(Oracle Problem)와 재진입 공격(Reentrancy) 등 주요 보안 취약점의 엔지니어링 해결 방안을 설명하시오.

---

## 2~4교시 25점 답안

## Ⅰ. 스마트 계약(Smart Contract)의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 블록체인 네트워크에 분산 저장되어 특정 조건이 만족되었을 때 중개자 없이 자동으로 계약 조항을 실행하고 상태를 확정하는 튜링 완전(Turing-Complete) 컴퓨터 프로그램. |
| 목적 | 중앙화된 중개 기관 배제를 통한 거래 비용 절감, 계약 집행의 즉시성 및 투명성 확보, 탈중앙화 금융(DeFi) 및 자율조직(DAO) 구동 기반 제공. |

## Ⅱ. 스마트 계약의 핵심 특징 및 EVM 실행 모델

### 1. 스마트 계약의 4대 핵심 특징

- **결정론적 실행(Determinism) :** 동일한 트랜잭션 입력과 이전 상태가 주어지면 모든 네트워크 참여 노드에서 완전히 동일한 결과 상태 산출.
- **불가변성(Immutability) :** 블록체인에 배포된 컨트랙트 바이트코드는 사후 임의 수정 및 삭제가 불가능하여 위변조 원천 방지.
- **자율 실행성(Autonomous Execution) :** 트랜잭션 호출 조건이 충족되면 사람의 개입 없이 코드가 프로그래밍된 로직대로 자동 집행.
- **가스 메커니즘 기반 자원 제약 :** 튜링 완전성으로 인한 튜링의 정지 문제(Halting Problem)를 해결하기 위해 모든 연산마다 Gas 소모 강제.

### 2. EVM(Ethereum Virtual Machine) 스택 머신 아키텍처

- **스택(Stack) :** 256비트 워드 크기를 지원하는 1024 레벨 깊이의 LIFO 연산 공간.
- **메모리(Memory) :** 트랜잭션 실행 중에만 휘발성으로 유지되는 바이트 단위 선형 메모리 공간.
- **스토리지(Storage) :** 256비트 키-값(Key-Value) 형태로 블록체인 원장에 영구 보존되는 상태 저장소(가장 높은 가스 비용 발생).

## Ⅲ. 스마트 계약 라이프사이클 및 실행 프로세스

### 1. 스마트 계약 개발·배포·실행 아키텍처

```text
[개발자 작성: Solidity] ──► [Solc 컴파일러] ──► [Bytecode + ABI 생성]
                                                      │
                                                      ▼ (서명된 배포 트랜잭션)
[블록체인 노드 검증] ◄── [P2P 전파] ◄── [트랜잭션 풀(Mempool) 투입]
       │
       ▼ (블록 채굴 및 합의)
[컨트랙트 계정(CA) 생성] ──► [EVM 상태 머신 적재]
                                    ▲
[외부 사용자 호출: Tx] ─────────────┤ (트랜잭션 실행)
                                    ▼
       +-------------------------------------------------------------+
       | EVM 실행: Opcode 순차 디코딩 및 Stack/Memory 연산             |
       | - Checks: 가스 한도, 호출자 권한, 인자 유효성 검증          |
       | - Effects: 컨트랙트 내부 Storage 변수(잔액, 소유권) 갱신     |
       | - Interactions: 외부 계정 및 타 컨트랙트 송금/메시지 호출  |
       +-------------------------------------------------------------+
                                    │
                                    ▼ (월드 스테이트 Merkle Patricia Trie 갱신)
                             [새로운 블록 확정]
```

### 2. 주요 단계별 세부 기술요소

| 단계 | 핵심 기술 요소 | 엔지니어링 역할 |
|---|---|---|
| **저작 및 컴파일** | Solidity, Vyper, Solc, Hardhat | 고수준 로직 검증 및 EVM 호환 저수준 옵코드(Opcode) 변환. |
| **인터페이스 정의** | ABI (Application Binary Interface) | DApp 프론트엔드가 컨트랙트 함수를 올바른 바이트스트림으로 인코딩/디코딩하도록 매핑. |
| **가상머신 실행** | EVM JIT/AOT 런타임, Gas Metering | 연산 단계마다 가스를 차감하고 가스 고갈 시 상태 롤백(Out-of-Gas Revert). |
| **상태 영구화** | Merkle Patricia Trie, LevelDB/RocksDB | 계정 상태(Nonce, Balance, StorageRoot, CodeHash)를 암호학적 해시 트리로 원장에 동기화. |

## Ⅳ. 비트코인 스크립트와 이더리움 스마트 계약 비교

| 비교 항목 | 비트코인 스크립트 (Bitcoin Script) | 이더리움 스마트 계약 (EVM Smart Contract) |
|---|---|---|
| **언어 특성** | 튜링 불완전(Turing Incomplete), 루프 반복문 부재 | 튜링 완전(Turing Complete), For/While 루프 지원 |
| **실행 모델** | 단순 스택 기반 조건식 평가 (Forth 유사) | 범용 가상머신(EVM) 기반 바이트코드 해석 |
| **상태 관리 (State)** | 무상태(Stateless) UTXO 검증 모델 | 상태 기반(Stateful) 어카운트/스토리지 모델 |
| **연산 제약 기법** | 연산자(Opcode) 수 및 스크립트 크기 제한 | 동적 가스(Gas) 소비 메커니즘을 통한 무한 루프 방지 |
| **표현력 및 확장성** | 단순 멀티시그, 타임락 지출 조건에 국한 | 복잡한 금융 로직, 토큰 발행(ERC-20/721), DAO 구현 |
| **보안 공격 표면** | 공격 표면 극소화 (논리적 단순성) | 복잡한 로직 및 재진입 취약점 등 높은 공격 표면 노출 |

## Ⅴ. 스마트 계약 엔지니어링 한계와 해결 방안

| 한계 | 방안 |
|---|---|
| **오라클 문제(Oracle Problem)로 인한 외부 데이터 조작**<br />- 금융 청산 및 스포츠 베팅 컨트랙트가 단일 API에 의존하여 가짜 데이터 주입 시 자산 탈취 위험. | **탈중앙화 오라클 네트워크(DON: Chainlink) 구축**<br />- 다수의 독립적인 오라클 노드가 데이터를 수집하고 이상치 제거 후 중앙값(Median) 합의 제공.<br />- 영지식 증명(zk-Oracle) 및 하드웨어 보안 영역(SGX)을 결합하여 데이터 출처 무결성 보증. |
| **배포 후 코드 수정 불가로 인한 취약점 패치 한계**<br />- 릴리즈된 컨트랙트에 심각한 로직 버그 발견 시 소스코드 교체가 불가능하여 서비스 중단 위기. | **프록시 패턴(Proxy Pattern: ERC-1967) 업그레이드 체계 구현**<br />- 사용자는 영구적인 프록시 컨트랙트(Proxy)를 호출하고, 프록시는 `delegatecall`로 로직 컨트랙트 위임 실행.<br />- 로직 버그 발생 시 다중서명 거버넌스를 거쳐 프록시가 가리키는 구현체 주소만 안전 교체. |
| **재진입(Reentrancy) 및 비인가 상태 변경 공격**<br />- 상태 업데이트 전에 외부 함수를 호출하여 재귀적 인출로 풀 잔액 고갈 유발(The DAO 해킹 유형). | **CEI 패턴 엄격 준수 및 재진입 방지 락(ReentrancyGuard) 적용**<br />- 상태 변수 변경(잔액 차감)을 외부 송금 호출보다 반드시 선행 처리.<br />- OpenZeppelin의 `nonReentrant` 뮤텍스 제어자를 적용하여 동시 재진입 함수 차단. |

## Ⅵ. 안전한 스마트 계약 배포 및 운영을 위한 제언

메인넷 배포 전 형식 검증(Formal Verification)과 동적 퍼징(Fuzzing) 테스트를 의무화하고, 비상 상황 시 트랜잭션을 즉시 중단할 수 있는 서킷 브레이커(Circuit Breaker) 아키텍처 필수 구축.

```text
[정적 분석] ────────► [동적 퍼징/형식검증] ──► [다중 감사(Audit)] ──► [타임락/멀티시그 배포] ──► [온체인 실시간 감시]
- Slither/Mythril       - Echidna/Certora       - 전문 보안업체 검증     - 48시간 지연 실행         - 이상 트랜잭션 일시 정지
```

| 검증 단계 | 주요 점검 항목 | 통과 기준 |
|---|---|---|
| **정적 분석** | 정수 오버플로우, 접근제어 누락, Reentrancy | Slither 고위험(High) 취약점 0건 |
| **형식 검증** | 수학적 불변식(Invariant) 만족 여부 증명 | 핵심 불변식 수학적 증명 100% 완료 |
| **비상 제어** | 해킹 징후 감지 시 컨트랙트 일시 정지(Pause) | 멀티시그 승인 후 단일 트랜잭션 중단 가능 |

## 출제 이력과 검증 출처

- **정보관리기술사 제117회 1교시 :** 이더리움 스마트 계약의 가스(Gas) 개념과 역할
- **컴퓨터시스템응용기술사 제123회 2교시 :** 스마트 계약의 보안 취약점(재진입 공격 등)과 오라클 문제(Oracle Problem)
- **Ethereum Whitepaper / Yellowpaper :** Ethereum: A Secure Decentralised Generalised Transaction Ledger
- **NIST IR 8408 :** Understanding the Security of Smart Contracts in Blockchain

## 연결 토픽

- [semantic web](182_semantic_web.md)
- [ontology](183_ontology.md)
- [blockchain consensus algorithms](151_blockchain_consensus_algorithms.md)
