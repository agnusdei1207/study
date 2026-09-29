---
title: "연합학습(Federated Learning)"
author: "Antigravity"
date: "2026-09-29T10:00:00+09:00"
tags:
  - "notes-latest-tech"
sidebar:
  label: "082. 연합학습(Federated Learning)"
  order: 82
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

<p class="itpe-byline">작성 모델 · Gemini 3.8 Flash<br />작성 · 2026.09.29 10:00 KST</p>

<div class="itpe-topic-path" aria-label="지식 경로">
인공지능 > 분산 머신러닝 > 프라이버시 보존 AI > 연합학습(Federated Learning)
</div>

## 30초 인출

- 본질: 원본 데이터를 중앙 서버로 전송하지 않고 각 로컬 디바이스(엣지/기관)에 유지한 채, 로컬에서 학습된 모델 파라미터(가중치/기울기)만을 중앙 서버로 전송하여 전역 모델(Global Model)을 공동 구축하는 탈중앙형 분산 머신러닝 기법.
- 메커니즘: 글로벌 모델 다운로드 $\rightarrow$ 로컬 비공개 데이터 기반 학습 $\rightarrow$ 암호화된 가중치 업데이트 전송 $\rightarrow$ 중앙 서버의 연합 평균(FedAvg) 집계 $\rightarrow$ 갱신된 전역 모델 재배포 라운드 반복.
- 통찰: 원본 데이터 비이동성에도 불구하고 가중치 역추론 공격(Inversion Attack)과 비IID(Non-IID) 데이터 편향 및 통신 병목이 발생하므로 차분 프라이버시(DP), 동형암호 안전 집계(SecAgg), FedProx 최적화 결합 필수.

<details><summary>핵심 용어</summary>

- **연합학습(Federated Learning):** 데이터 주권을 보장하며 개인정보 유출 없이 다수의 참여자 간 공동 AI 모델을 협력 학습하는 분산 AI 아키텍처.
- **연합 평균(FedAvg, Federated Averaging):** 각 로컬 클라이언트의 데이터 표본 수에 비례하여 가중치를 부여하고 산술 평균으로 전역 모델 파라미터를 갱신하는 기본 집계 알고리즘.
- **비IID(Non-IID, Non-Independent and Identically Distributed):** 참여 클라이언트마다 보유한 데이터의 클래스 분포, 양, 특성이 균일하지 않고 극심하게 편향된 현실적 데이터 상태.
- **안전 집계(Secure Aggregation):** 다자간 보안 컴퓨팅(SMC)을 활용하여 중앙 집계 서버조차 개별 클라이언트의 가중치 원본을 볼 수 없고 오직 최종 합산 값만 복호화하도록 보장하는 암호화 프로토콜.
- **차분 프라이버시(Differential Privacy):** 가중치 업데이트 벡터에 수학적으로 계산된 통계적 노이즈(Laplace/Gaussian)를 주입하여 특정 개인의 데이터 포함 여부를 역추적하지 못하게 차단하는 기법.
</details>

---

## 2~4교시 예상문제 (25점)

> 데이터 3법 및 프라이버시 보호 규제가 강화됨에 따라 주목받고 있는 연합학습(Federated Learning)과 관련하여 다음을 설명하시오.
> 가. 연합학습의 개념 및 필요성
> 나. 연합학습의 전체 동작 프로세스 및 FedAvg 알고리즘 수식 원리
> 다. 연합학습의 3대 분류 유형(수평, 수직, 연합 전이 학습)
> 라. 운영 시 직면하는 기술적 한계(Non-IID, 보안 공격, 통신 부하)와 엔지니어링 극복 방안

---

## 2~4교시 25점 답안

## Ⅰ. 프라이버시 보존형 협업 머신러닝, 연합학습의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 개별 디바이스나 기관이 보유한 원시 데이터(Raw Data)를 외부로 반출하지 않고, 로컬에서 학습한 가중치 파라미터만 교환하여 중앙 전역 모델을 최적화하는 분산 기계학습 체계 |
| 목적 | GDPR·데이터 3법 등 개인정보 규제 준수, 민감 데이터 사일로(Silo) 문제 해결, 대용량 원시 데이터 전송 비용 절감 및 네트워크 대역폭 한계 극복 |

- "데이터는 머무르고, 모델이 이동한다(Bring code to data, not data to code)"는 패러다임 구현.
- 의료, 금융, 자율주행 등 데이터의 외부 공유가 법적·보안상 불가능한 도메인에서 연합 생태계를 구축하는 핵심 동인.

## Ⅱ. 연합학습의 핵심 특징 및 FedAvg 수학적 원리

| 핵심 특징 | 세부 내용 | 구현 메커니즘 |
|---|---|---|
| 온디바이스 로컬 연산 | 원시 데이터가 사용자 스마트폰, 병원 EMR 서버 등 로컬 경계 내 잔류 | 엣지 디바이스 NPU/GPU 활용 온디바이스 학습 파이프라인 |
| 모델 파라미터 통신 | 수 기가바이트의 원시 데이터 대신 수십 메가바이트의 가중치 텐서만 전송 | 통신 압축(양자화, Top-k Sparsification) 기법 적용 |
| 비동기·이종 환경 대응 | 네트워크 끊김, 연산 능력 격차 등 클라이언트의 극심한 이종성 수용 | 참여 클라이언트 무작위 샘플링 및 스트래글러(Straggler) 드롭 |
| 수학적 프라이버시 보장 | 가중치 역공학 방지를 위한 암호학적 마스킹 및 통계적 노이즈 주입 | Secure Aggregation(SMC) 및 Local Differential Privacy(LDP) |

| FedAvg 수식 원리 | 수식 표현 | 단계별 수학적 작용 |
|---|---|---|
| 로컬 손실 함수 최소화 | $w_k^{t+1} \leftarrow w^t - \eta \nabla F_k(w^t)$ | 각 클라이언트 $k$가 로컬 데이터 $D_k$에 대해 $E$ 에포크 동안 경사하강법 수행 |
| 데이터량 가중 비율 | $p_k = \frac{n_k}{n}$, 단 $n = \sum_{k=1}^K n_k$ | 전체 데이터 수 $n$ 중 개별 클라이언트가 보유한 샘플 수 $n_k$의 비중 산출 |
| 전역 모델 파라미터 집계 | $w^{t+1} = \sum_{k=1}^K \frac{n_k}{n} w_k^{t+1}$ | 중앙 서버가 수집된 로컬 가중치들을 데이터 샘플 비율로 가중 평균하여 합성 |

## Ⅲ. 연합학습 전체 아키텍처 및 라운드별 프로세스

```text
+-------------------------------------------------------------------------------------------------+
|                                Federated Learning Round Architecture                            |
+-------------------------------------------------------------------------------------------------+
                          [Central Orchestration Server]
                          - Global Model: w_t
                          - Secure Aggregator (FedAvg)
                                  |         ^
             1. Broadcast w_t     |         | 3. Upload Local Weights (Encrypted)
                                  v         |
     +----------------------------+---------+----------------------------+
     |                                      |                            |
     v                                      v                            v
 [Client A (Hospital)]             [Client B (Bank)]            [Client C (Mobile)]
  - Local Data D_A (EMR)            - Local Data D_B (Finance)   - Local Data D_C (Sensor)
  - Train: w_A^(t+1)                - Train: w_B^(t+1)           - Train: w_C^(t+1)
  - Add DP Noise & Mask             - Add DP Noise & Mask        - Add DP Noise & Mask
```

| 프로세스 단계 | 핵심 처리 내용 |
|---|---|
| 1. 클라이언트 선발 및 배포 | 중앙 서버가 가용 클라이언트 중 일부를 무작위 선택 후 현재 전역 모델 가중치($w_t$) 브로드캐스트 |
| 2. 로컬 데이터 학습 | 각 클라이언트는 로컬 GPU/NPU를 구동하여 자신의 개인 데이터셋으로 로컬 에포크 학습 수행 |
| 3. 프라이버시 처리 및 업로드 | 가중치 변화량($\Delta w_k$)에 노이즈를 주입(DP)하고 암호화 마스크를 씌워 중앙 서버로 전송 |
| 4. 보안 집계(SecAgg) | 중앙 서버는 개별 모델을 열람하지 않고 합산 상태에서 복호화하여 FedAvg 가중 평균 연산 |
| 5. 전역 모델 갱신 및 평가 | 수렴 조건 달성 여부를 검증하고, 수렴할 때까지 다음 통신 라운드(Next Round) 반복 진행 |

## Ⅳ. 연합학습의 3대 분류 유형 및 중앙집중 학습 비교

| 분류 유형 | 사용자(ID) 중복성 | 데이터 특징(Feature) 중복성 | 대표 적용 사례 |
|---|---|---|---|
| 수평 연합학습 (Horizontal FL) | 거의 다름 (사용자 중복 낮음) | 동일함 (피처 공간 공유) | 여러 지역 병원의 동일 질병 EMR, 스마트폰 키보드 예측 |
| 수직 연합학습 (Vertical FL) | 동일함 (동일 사용자 공유) | 다름 (서로 다른 속성 보유) | 같은 도시 내 은행(금융)과 이커머스(구매) 간 신용평가 모델 |
| 연합 전이학습 (Federated TL) | 다름 (서로 다른 사용자) | 다름 (서로 다른 도메인) | 국내 은행과 해외 의료기관 간 소수 샘플 전이 학습 |

| 비교 항목 | 중앙집중식 머신러닝 (Centralized ML) | 연합학습 (Federated Learning) |
|---|---|---|
| 데이터 위치 | 대규모 중앙 데이터 레이크/클라우드로 전송 | 개별 엣지 기기 및 기관 내부 온프레미스에 보관 |
| 프라이버시 위험 | 전송 및 중앙 저장 중 대규모 해킹·유출 위험 | 원본 미반출로 데이터 유출 위험 원천 최소화 |
| 통신 비용 | 테라바이트급 대용량 원시 데이터 전송 부하 | 모델 파라미터 텐서만 전송하므로 대역폭 대폭 절감 |
| 데이터 분포 가정 | 독립 동일 분포(IID) 가정 충족 용이 | 현실적 극심한 비독립 동일 분포(Non-IID) 직면 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 참여자별 데이터 분포 불균일로 인해 전역 모델이 수렴하지 못하고 진동하는 Non-IID 병목 | 로컬 손실 함수에 전역 모델과의 거리 페널티 항을 추가하는 FedProx 알고리즘 및 클라이언트별 맞춤 레이어를 두는 개인화 연합학습(pFedMe) 적용 |
| 전송되는 가중치 기울기 변화량을 역추적하여 원본 훈련 이미지를 복원하는 모델 전도(Inversion) 공격 | 통계적 차분 프라이버시(DP) 노이즈 주입 및 동형암호 기반 안전 집계(Secure Aggregation) 프로토콜 강제화 |
| 악의적 클라이언트가 의도적으로 오염된 가중치를 제출하여 전역 모델을 파괴하는 포이즈닝(Poisoning) 공격 | 중앙 서버 집계 시 이상치 가중치 벡터를 필터링하는 강건 집계 알고리즘(Krum, Trimmed-Mean) 및 영지식 증명(ZKP) 검증 체계 도입 |

## Ⅵ. 제언

연합학습은 단순 프라이버시 도구를 넘어 데이터 경제 시대의 '프라이버시 보존형 AI 협업 생태계'를 실현하는 코어 인프라로 안착.

```text
[Edge Client Privacy] ---> [Robust / Secure Aggregation] ---> [Incentive & Governance]
  - Local Differential Privacy - FedProx / Krum Algorithm     - Data Contribution Valuation
  - Secure Enclave (TEE)       - Secure Multi-Party Compute    - Shapley Value Token Reward
```

| 구현 관점 | 단기 구축 과제 | 중장기 성숙 과제 |
|---|---|---|
| 알고리즘 최적화 | FedAvg 한계 극복을 위한 FedProx 및 통신 압축(QSGD) 적용 | 클라이언트별 기여도에 비례한 섀플리 값(Shapley Value) 기반 보상 모델 설계 |
| 보안·인프라 | TEE(신뢰 실행 환경) 기반 안전 집계 서버 구축 | 블록체인 연계 탈중앙화 연합학습(Decentralized FL) 및 스마트 계약 오케스트레이션 |

## 출제 이력과 검증 출처

- 제128회 정보관리기술사 1교시: 연합학습(Federated Learning)의 개념, 동작 절차, 프라이버시 보호 기술.
- McMahan, B. et al., Communication-Efficient Learning of Deep Networks from Decentralized Data, AISTATS (FedAvg 원 논문).
- Yang, Q. et al., Federated Machine Learning: Concept and Applications, ACM TIST.
- Li, T. et al., Federated Optimization in Heterogeneous Networks (FedProx), MLSys.

## 연결 토픽

- 분산 머신러닝 파이프라인: [MLOps](./077_mlops.md)
- 최적화 알고리즘: [오차역전파(Backpropagation)](./081_backpropagation.md)
- 보안 암호화 기술: [동형암호 및 차분 프라이버시](../08-law-policy/001_ai_ethics_standards.md)
