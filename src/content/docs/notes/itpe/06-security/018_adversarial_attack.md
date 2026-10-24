---
title: "적대적 공격(Adversarial Attack)"
author: "agnusdei1207"
date: "2026-10-24T22:56:12+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 적대적 공격(Adversarial Attack), 적대적 예제(Adversarial Example), 적대적 섭동(Perturbation)
- FGSM(Fast Gradient Sign Method), PGD(Projected Gradient Descent), C&W 공격(Carlini & Wagner)
- 화이트박스, 블랙박스, 데이터 중독(Data Poisoning), 백도어 공격(Backdoor Attack)
- 전이성(Transferability), 적대적 훈련(Adversarial Training), TRADES
- 랜덤 변환(Random Transformation), 적대적 패치(Adversarial Patch), 오토인코더(Autoencoder)
- 결정 경계(Decision Boundary), 모델 강건성(Robustness), 기울기(Gradient), 손실 함수(Loss Function)

## Ⅰ. 적대적 공격(Adversarial Attack)의 개요

- 핵심 요약 : 사람이 알아채기 어려운 미세 노이즈로 AI 모델의 판단을 빗나가게 만드는 공격.
- 개념 : 입력 데이터에 사람이 거의 인지하지 못하는 **적대적 섭동** (Perturbation, 미세 노이즈)을 의도적으로 더해 인공지능(AI, Artificial Intelligence) 모델이 오분류하도록 유도하는 사이버 공격 (**적대적 공격**, Adversarial Attack).
- 배경 및 필요성 : 자율주행의 표지판 인식, 금융 이상거래 탐지(FDS, Fraud Detection System), 의료 영상 판독, 안면 인식 등 AI가 실제 환경에 배포되면서 오판이 곧 물리적·경제적 피해로 이어지는 위험이 커짐.
- 주요 목적 : 딥러닝 모델의 **결정 경계** (Decision Boundary) 취약성을 이해하고, **모델 강건성** (Robustness)을 평가해 방어 체계를 갖추는 것.

## Ⅱ. 적대적 공격(Adversarial Attack)의 특징 및 장점

- 핵심 요약 : 기울기 기반 계산, 불가시성, 전이성이 결합되어 공격 효율과 은닉성이 높아지는 구조.

1. **기울기** (Gradient) 활용 : 손실 함수의 기울기 방향을 역이용해 노이즈를 계산 → 적은 변화로도 오분류를 유도하는 효율이 높음.
2. 불가시성 : 사람 눈으로는 구분되지 않는 미세 섭동을 사용 → 육안 검수로는 걸러내기 어려움.
3. **전이성** (Transferability) : 대리 모델에서 만든 예제가 다른 모델에서도 작동 → 내부 구조를 모르는 블랙박스 환경에서도 공격 가능.

## Ⅲ. 적대적 공격(Adversarial Attack)의 구조 (흐름)

- 핵심 요약 : 입력을 변조하는 추론 단계 공격과 학습 파이프라인을 오염시키는 학습 단계 공격으로 나뉘는 흐름.

```text
[ FGSM 공격 흐름 ]

원본 입력 x (정상 분류)
        ↓
손실 함수의 기울기 부호 계산
        ↓
x_adv = x + ε · sign(∇x J(θ, x, y))
        ↓
적대적 예제 x_adv 입력 → 오분류
```

- **FGSM** (Fast Gradient Sign Method) : 기울기 부호 방향으로 엡실론(ε)만큼 노이즈를 한 번 더해 빠르게 적대적 예제를 생성하는 기법.
- **PGD** (Projected Gradient Descent) : 작은 스텝으로 여러 번 갱신하면서 허용 범위 안으로 되돌리는 방식으로, FGSM보다 강력한 화이트박스 공격으로 알려짐.
- **C&W 공격** (Carlini & Wagner) : 섭동 크기를 최소화하면서 오분류를 만드는 최적화 기반 공격으로, 여러 방어 기법을 우회한 사례로 알려짐.
- 화이트박스와 블랙박스 : 모델 구조와 가중치를 아는 상태에서 공격하는 것이 화이트박스이고, 입출력 결과만 보고 대리 모델(Surrogate Model)을 만들어 공격하는 것이 블랙박스이다.

```text
[ 공격 시점별 흐름 ]

학습 데이터 수집
        ↓ 데이터 중독·백도어 삽입
모델 학습
        ↓
모델 배포
        ↓ 적대적 예제 주입
추론 (입력 단계)
```

- **데이터 중독** (Data Poisoning)과 **백도어 공격** (Backdoor Attack)은 학습 단계에서 파이프라인을 오염시키고, 적대적 예제는 배포된 모델을 추론 단계에서 속인다.

## Ⅳ. 적대적 공격(Adversarial Attack)의 유형 비교

- 핵심 요약 : 적대적 예제는 서빙 중인 모델을, 포이즈닝과 백도어는 학습 파이프라인을 겨냥하는 상이한 공격 유형.

| 비교 항목 | 적대적 예제 (Adversarial Example) | 데이터 중독 (Data Poisoning) | 백도어 공격 (Backdoor Attack) |
| --- | --- | --- | --- |
| 공격 수행 시점 | 추론 단계 (Inference Time) | 학습 단계 (Training Time) | 학습 단계 (Training Time) |
| 조작 대상 | 입력 데이터에 섭동 주입 | 학습 데이터셋 전체 또는 일부 | 학습 데이터와 특정 트리거(Trigger) |
| 모델 파라미터 | 변경되지 않음 | 오염됨 | 트리거에 반응하도록 변조됨 |
| 공격 목적 | 개별 입력의 예측 오분류 | 전반적인 정확도 저하 | 평시에는 정상, 트리거 시 악성 동작 |
| 대표 방어 기법 | **적대적 훈련** (Adversarial Training) | 데이터 위생화(Data Sanitization) | Neural Cleanse 기반 트리거 탐지 |

## Ⅴ. 적대적 공격(Adversarial Attack)의 한계와 방안

- 핵심 요약 : 정확도 저하, 전이성 악용, 물리 세계 패치 공격을 학습 설계, 입력 변환, 다중 센서 융합으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 정상 데이터 정확도 저하 | 강건성을 높이려는 적대적 훈련으로 결정 경계가 완만해져 정상 입력 인식 성능이 떨어짐 | TRADES 계열 손실 함수로 정확도와 강건성의 균형점 탐색 | 정상 데이터 정확도, 강건 정확도 |
| 전이성 악용 | 공격자 자체 모델에서 만든 예제가 상용 모델에서도 작동해 타깃 구조를 몰라도 공격 가능 | **랜덤 변환** (Random Transformation, 무작위 리사이징·패딩·압축)으로 섭동 구조 무력화 | 변환 후 오분류율 |
| **적대적 패치** (Adversarial Patch) | 정지 표지판 스티커나 의류 패턴으로 CCTV(Closed-Circuit Television)와 자율주행 센서를 물리적으로 기만 | 카메라 외에 라이다(LiDAR, Light Detection and Ranging), 레이더 등을 결합하는 **다중 모달** (Multi-modal) 교차 검증 | 센서 간 판단 불일치율 |

## Ⅵ. 적대적 공격(Adversarial Attack)에 대한 기술사적 제언

- 핵심 요약 : 강건성 평가의 배포 게이트 내재화, 적대적 훈련 표준화, 입력 정제 계층 도입을 AI 보안 체계의 기본으로 제시.

1. **적대적 강건성 평가** (Robustness Testing) 내재화 : CI(Continuous Integration)·CD(Continuous Delivery) 파이프라인에 ART(Adversarial Robustness Toolbox) 같은 도구로 공격 저항성을 측정하고, 기준에 미달하면 배포를 막는 게이트를 두는 것이 바람직하다.
2. 적대적 훈련 표준화 : 미션 크리티컬 분야의 학습에는 PGD로 만든 적대적 샘플을 일정 비율 섞어 학습하는 절차를 기준으로 삼는 것이 필요하다.
3. 입력 정제 계층 : 추론 직전에 비정상 고주파 노이즈를 걸러내는 **오토인코더** (Autoencoder) 기반 전처리 계층을 두는 방안을 검토하는 것이 좋다.

## Ⅶ. 결론

- 핵심 요약 : 적대적 공격은 인간이 알아챌 수 없는 미세 변화로 AI 판단의 신뢰를 흔드는 공격 유형.
- 시사점 : 모델 성능 지표와 함께 강건성 지표를 배포 전후로 측정하는 체계가 AI 신뢰성의 전제가 된다.
