---
title: "6G 표준화 (3GPP Rel-20·21, IMT-2030)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:25:00+09:00"
tags:
  - "notes-network"
sidebar:
  badge:
    text: "미출 · 85%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "미출"
  source_history: ""
  priority: 85
  priority_note: "시사·트렌드"
---

## 답안 골격
```text
[6G 표준화] ◀━━ 머리: Ⅶ 내 의견 (초기 Sub-7GHz·Upper-6GHz 중심 진화 후 THz 국소망 선별 도입)
 ┃
 ┣━ Ⅰ 개요 ───── 5G 한계 극복 및 초공간·AI 융합 요구 → ITU-R IMT-2030 및 3GPP 표준화
 ┣━ Ⅱ 특징 ───── 최고 1Tbps, 체감 1Gbps, 0.1ms 지연, 100배 연결 밀도, 통신-센싱 융합(ISAC)
 ┣━ Ⅲ 구조 ───── ITU-R 6대 시나리오(eMBB+·URLLC+·mMTC+ 확장 + AI 융합·ISAC·유비쿼터스 연결)
 ┣━ Ⅳ 흐름 ───── ① IMT-2030 비전(2023) → ② 3GPP Rel-20 Study(2025~2027) → ③ Rel-21 Normative(2028~) → ④ 상용화(2030)
 ┣━ Ⅴ 비교 ───── 5G(IMT-2020) vs 6G(IMT-2030) (20Gbps vs 1Tbps, 1ms vs 0.1ms, 지상망 vs NTN 입체)
 ┗━ Ⅵ 실무 ───── 서브 테라헤르츠(sub-THz) 극심한 경로 손실 / 천문학적 기지국 구축비 / 킬러 서비스 부재
```
- 필수 키워드: ITU-R IMT-2030 · 3GPP Rel-20 · Rel-21 · ISAC(통신·센싱 융합) · AI-Native · NTN(초공간 입체) · sub-THz
- 배점 전략: 10점 = Ⅰ → Ⅲ IMT-2030 6대 사용 시나리오 레이더 차트/도식 → Ⅴ 5G/6G 비교표 / 25점 = Ⅰ~Ⅶ, 3GPP 표준화 일정 로드맵과 6G 6대 목표 성능 지표 상세
- 기출: 미출제. 6G 표준화 로드맵 및 핵심 기술 프레임워크 25점 서술형 출제 유력

## 한 줄 본질
- 5G의 지상망 한계와 단순 파이프 전송 구조를 넘어선 완전한 디지털 트윈·AI 시대의 물리-가상 결합 요구 → ITU-R IMT-2030 프레임워크 기반 3GPP Rel-20/21에서 AI·센싱·초공간을 아우르는 글로벌 단일 표준 제정 → 전 지구적 무결점 초연결과 신규 센싱 가치 창출 / 서브 테라헤르츠(sub-THz) 고주파 전파의 극단적 직진성 및 망 구축 투자비 폭증

## 핵심 그림
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

## 핵심 용어
- IMT-2030: 국제전기통신연합(ITU-R)이 확정한 2030년대 상용화를 목표로 하는 차세대 6G 이동통신 공식 명칭 및 프레임워크 권고안
- ISAC(Integrated Sensing and Communication): 무선 통신 반송파 신호로 데이터를 주고받는 동시에 레이더처럼 주변 사물의 위치, 속도, 형상을 감지하는 기술
- 3GPP Rel-20/21: 6G 연구 단계(Study Item, Rel-20, 2025~2027)를 거쳐 2028년경 정식 6G 기술 규격(Work Item, Rel-21)을 동결하는 표준화 마일스톤

## 핵심 통찰
- 5G의 3대 축(eMBB, URLLC, mMTC)이 6G에서는 더욱 고도화되는 동시에, "AI 융합", "센싱 융합(ISAC)", "초공간 연결(Ubiquitous/NTN)"이라는 3대 신규 차원이 결합
- 5G 28GHz 상용화 실패의 뼈아픈 교훈으로 인해, 6G 표준화는 100GHz 이상의 서브 THz 올인 대신 7~15GHz 대역(Upper Mid-Band / FR3)을 광역 커버리지의 실질적 핵심으로 선정
- 하드웨어 통신 칩셋 중심의 표준화에서 벗어나, 프로토콜 전 계층에 기계학습 모델 교환 및 지능형 무선 인터페이스(AI-Native Air Interface)를 내재화하는 방향으로 진화

## 이웃 토픽과 구분
- 5G-Advanced vs 6G: 5G-Advanced(3GPP Rel-18/19, 5G 구조를 유지하며 AI/NTN 기반 기술 도입) / 6G(3GPP Rel-20/21, IMT-2030 기반 새로운 무선 인터페이스 및 AI 네이티브 아키텍처 정립)

## 문제·원인·대책
- 적용 상황: 6G 테라헤르츠(THz) 대역 전송 시 신호 도달거리 급감
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 100GHz 초고주파 대역의 대기 분자 흡수 손실 | 극도로 짧은 파장으로 인한 산소·수증기 분자 공진 흡수 | Upper Mid-Band(7~15GHz) 메인 커버리지 활용 및 RIS(지능형 반사 표면) 배치 | 도심 빌딩 뒤 음영지역 신호 반사 유도로 커버리지 보완 |
| 천문학적인 기지국 고밀도화 투자비 | 커버리지 축소로 인한 기지국 수십 배 증설 요구 | O-RAN 및 AI-RAN 기반 COTS 하드웨어 인프라 공유 | 통신망 인프라 구축비(CapEx) 30% 이상 절감 |

## 이렇게 출제된다
- 미출제. 예상: "ITU-R의 IMT-2030 프레임워크에서 제시한 6G 6대 사용 시나리오와 3GPP Release 20·21 표준화 추진 로드맵, 그리고 5G 대비 주요 요구 성능 지표를 비교 설명하시오." → 요구 포인트: Ⅲ 6대 시나리오 + Ⅳ 표준화 일정 + Ⅴ 성능 비교표(속도, 지연, 신뢰도 등)

## 내 의견
- [5G 28GHz 전철을 밟지 않기 위한 현실적 주파수 정책] 초고주파(THz) 환상에 매몰되어 인프라 투자를 강요하면 5G와 같은 시장 외면 반복 위험 → 나라면: 7~15GHz(FR3) 대역을 기반으로 기존 5G 기지국 사이트를 재활용하여 비용을 통제하고, THz 대역은 데이터센터 내 초고속 광무선 링크나 단거리 키오스크 고속 다운로드 같은 특화 B2B 구역에 국한해 단계적으로 상용화

## 찾아볼 것
- WRC-23(세계전파통신회의)에서 합의된 6G 후보 주파수 대역과 2027년 WRC-27 의제
