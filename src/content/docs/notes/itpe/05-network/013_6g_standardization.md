---
title: "6G 표준화 (3GPP Rel-20·21, IMT-2030)"
author: "Gemini 3.8 Flash"
date: "2026-09-24T21:00:00+09:00"
tags:
  - "notes-network"
extra:
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 핵심 개념 → 6G 표준화

## 30초 인출

- 본질: 5G의 지상망 한계와 단순 파이프 전송 구조를 넘어선 완전한 디지털 트윈·AI 시대의 물리-가상 결합 요구
- 메커니즘: ITU-R IMT-2030 프레임워크 기반 3GPP Rel-20/21에서 AI·센싱·초공간을 아우르는 글로벌 단일 표준 제정

## 핵심 용어

- IMT-2030: 국제전기통신연합(ITU-R)이 확정한 2030년대 상용화를 목표로 하는 차세대 6G 이동통신 공식 명칭 및 프레임워크 권고안
- ISAC(Integrated Sensing and Communication): 무선 통신 반송파 신호로 데이터를 주고받는 동시에 레이더처럼 주변 사물의 위치, 속도, 형상을 감지하는 기술
- 3GPP Rel-20/21: 6G 연구 단계(Study Item, Rel-20, 2025~2027)를 거쳐 2028년경 정식 6G 기술 규격(Work Item, Rel-21)을 동결하는 표준화 마일스톤

---

## 1교시 예상문제 (10점)

> 6G 표준화의 개념과 핵심 구조 또는 동작을 설명하시오. (예상)

---

## 1교시 10점 답안

### 정의·목적

- 정의: 6G 표준화은/는 ITU-R IMT-2030 프레임워크 기반 3GPP Rel-20/21에서 AI·센싱·초공간을 아우르는 글로벌 단일 표준 제정 방식이다.
- 목적: 전 지구적 무결점 초연결과 신규 센싱 가치 창출에 기여한다.

### 핵심 구조와 작동

```text
[ ITU-R IMT-2030 6대 사용 시나리오 (Usage Scenarios) ]

                     몰입형 통신 (Immersive Communication)
                                   /\
                                  /  \
     통신-센싱 융합               /    \             초광대역 저지연 통신
  (Integrated Sensing <---------+------+---------> (Hyper-Reliable and Low-
   and Communication)          /        \           Latency Communication)
                              /  IMT-    \
                             /   2030     \
  통신-AI 융합              /              \        유비쿼터스 연결
  (Integrated AI <---------+----------------+-----> (Ubiquitous Connectivity,
   and Communication)       \              /         위성-지상 초공간 NTN)
                             \            /
                              \          /
                               \        /
                                \      /
                                 \    /
                                  \  /
                                   \/
                        대규모 연결 (Massive Communication)
```

---

## 2~4교시 예상문제 (25점)

> 6G 표준화의 구조와 동작을 설명하고, 주요 비교 또는 적용 시 문제와 대응책을 제시하시오. (예상)

---

## 2~4교시 25점 답안

### Ⅰ. 핵심 구조와 작동

```text
[ ITU-R IMT-2030 6대 사용 시나리오 (Usage Scenarios) ]

                     몰입형 통신 (Immersive Communication)
                                   /\
                                  /  \
     통신-센싱 융합               /    \             초광대역 저지연 통신
  (Integrated Sensing <---------+------+---------> (Hyper-Reliable and Low-
   and Communication)          /        \           Latency Communication)
                              /  IMT-    \
                             /   2030     \
  통신-AI 융합              /              \        유비쿼터스 연결
  (Integrated AI <---------+----------------+-----> (Ubiquitous Connectivity,
   and Communication)       \              /         위성-지상 초공간 NTN)
                             \            /
                              \          /
                               \        /
                                \      /
                                 \    /
                                  \  /
                                   \/
                        대규모 연결 (Massive Communication)
```

### Ⅱ. 핵심 특성

- 5G의 3대 축(eMBB, URLLC, mMTC)이 6G에서는 더욱 고도화되는 동시에, "AI 융합", "센싱 융합(ISAC)", "초공간 연결(Ubiquitous/NTN)"이라는 3대 신규 차원이 결합
- 5G 28GHz 상용화 실패의 뼈아픈 교훈으로 인해, 6G 표준화는 100GHz 이상의 서브 THz 올인 대신 7~15GHz 대역(Upper Mid-Band / FR3)을 광역 커버리지의 실질적 핵심으로 선정
- 하드웨어 통신 칩셋 중심의 표준화에서 벗어나, 프로토콜 전 계층에 기계학습 모델 교환 및 지능형 무선 인터페이스(AI-Native Air Interface)를 내재화하는 방향으로 진화

### Ⅲ. 관련 개념과 구분

- 5G-Advanced vs 6G: 5G-Advanced(3GPP Rel-18/19, 5G 구조를 유지하며 AI/NTN 기반 기술 도입) / 6G(3GPP Rel-20/21, IMT-2030 기반 새로운 무선 인터페이스 및 AI 네이티브 아키텍처 정립)

### Ⅳ. 적용 문제와 대응

- 적용 상황: 6G 테라헤르츠(THz) 대역 전송 시 신호 도달거리 급감
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 100GHz 초고주파 대역의 대기 분자 흡수 손실 | 극도로 짧은 파장으로 인한 산소·수증기 분자 공진 흡수 | Upper Mid-Band(7~15GHz) 메인 커버리지 활용 및 RIS(지능형 반사 표면) 배치 | 도심 빌딩 뒤 음영지역 신호 반사 유도로 커버리지 보완 |
| 천문학적인 기지국 고밀도화 투자비 | 커버리지 축소로 인한 기지국 수십 배 증설 요구 | O-RAN 및 AI-RAN 기반 COTS 하드웨어 인프라 공유 | 통신망 인프라 구축비(CapEx) 30% 이상 절감 |

### Ⅴ. 기술사적 제언

| 문제 | 해결 방안 |
|---|---|
| 적용 환경에서 발생하는 핵심 제약 | 기존 대책을 적용하고 핵심 운영 지표를 확인해 개선한다. |

## 출제 이력과 검증 출처

- 미출제. 예상: "ITU-R의 IMT-2030 프레임워크에서 제시한 6G 6대 사용 시나리오와 3GPP Release 20·21 표준화 추진 로드맵, 그리고 5G 대비 주요 요구 성능 지표를 비교 설명하시오." → 요구 포인트: Ⅲ 6대 시나리오 + Ⅳ 표준화 일정 + Ⅴ 성능 비교표(속도, 지연, 신뢰도 등)

## 찾아볼 것
- WRC-23(세계전파통신회의)에서 합의된 6G 후보 주파수 대역과 2027년 WRC-27 의제
