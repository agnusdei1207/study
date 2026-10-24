---
title: "칩렛과 UCIe 3.0 (UCIe: Universal Chiplet Interconnect Express)"
author: "agnusdei1207"
date: "2026-10-24T22:24:38+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 칩렛(Chiplet), UCIe, 단일 거대 다이(Monolithic Die), 레티클 한계(Reticle Limit), 무어의 법칙(Moore's Law)
- 이종 집적(Heterogeneous Integration), D2D 어댑터(Die-to-Die Adapter), 물리 계층(Physical Layer)
- 2.5D 패키징, KGD(Known Good Die), 열팽창계수(CTE, Coefficient of Thermal Expansion), 언더필(Underfill), 유리기판(Glass Substrate), OSAT

## Ⅰ. 칩렛·UCIe 3.0의 개요

- 핵심 요약 : **칩렛** (Chiplet)은 거대 단일 다이의 수율 한계를 넘기 위해 기능별 다이를 개방형 인터커넥트 UCIe(Universal Chiplet Interconnect Express)로 결합하는 모듈형 반도체 구조.
- 개념 : 한 장의 큰 실리콘에 모든 기능을 담는 **단일 거대 다이** (Monolithic Die)는 면적이 **레티클 한계** (Reticle Limit)에 가까울수록 수율이 떨어지므로, CPU(Central Processing Unit), GPU(Graphics Processing Unit), I/O, SRAM(Static Random-Access Memory) 등을 나눠 제조한 다이를 **2.5D·3D 패키징**으로 잇는 방식.
- 배경 및 필요성 : 무어의 법칙(Moore's Law)이 둔화되고 첨단 공정의 웨이퍼 비용과 다이 면적이 커지면서 수율이 급격히 떨어져, 공정별로 최적화된 다이를 조합하는 **이종 집적** (Heterogeneous Integration)이 대안으로 부상함.
- 주요 목적 : 수율과 원가 개선, 다이 크기의 물리적 한계 극복, 개방형 표준을 통한 벤더 간 칩렛 상호운용성 확보.

## Ⅱ. 칩렛·UCIe 3.0의 특징 및 장점

- 핵심 요약 : 3계층 구조와 이종 공정 결합, 개방형 표준이 맞물려 칩렛을 여러 공급자가 조립하는 모듈형 설계를 가능하게 하는 구조.

1. **물리 계층** (Physical Layer) : 미세 피치 범프와 고속 신호 인터페이스로 데이터 레인과 사이드밴드를 구동 → 칩렛 사이 신호 전송 기반 확보.
2. **D2D 어댑터** (Die-to-Die Adapter) : CRC(Cyclic Redundancy Check) 검증, 재전송 버퍼링, 플릿(Flit) 정렬을 담당 → 칩렛 사이 링크 신뢰성 보장.
3. 프로토콜 계층 : PCIe(Peripheral Component Interconnect Express)와 CXL(Compute Express Link) 같은 검증된 프로토콜을 그대로 실어 나름 → 기존 소프트웨어 자산을 재사용.
4. 이종 공정 결합 : 연산 코어는 최신 공정으로, I/O와 아날로그 회로는 성숙 공정으로 나눠 제작 → 공정별 원가와 수율을 함께 최적화.

## Ⅲ. 칩렛·UCIe 3.0의 구조 및 동작 메커니즘

- 핵심 요약 : 프로토콜, 어댑터, 물리 계층의 세 층이 인터페이스로 이어지고, 패키지 경로에 따라 표준과 첨단 2.5D로 나뉘는 구조.

```text
[ UCIe 3계층 구조 ]

프로토콜 계층 (PCIe, CXL, Streaming)
        ↓ FDI (Flit-aware D2D Interface)
D2D 어댑터 계층 (CRC, 재전송, 흐름 제어)
        ↓ RDI (Raw D2D Interface)
물리 계층 (데이터 레인, 사이드밴드)
```

```text
[ 칩렛 패키징 경로 ]

칩렛 다이 (UCIe 물리 계층 탑재)
        ↓
표준 패키지 (유기 기판, 비용 최적화)
        ↓ 또는
첨단 2.5D 패키지 (실리콘 인터포저, 미세 범프)
```

## Ⅳ. 칩렛·UCIe 3.0의 비교

- 핵심 요약 : 단일 거대 다이, 독자 규격 칩렛, UCIe 개방형 칩렛을 수율, 호환성, 인터페이스 표준 측면에서 비교.

| 비교 항목 | 단일 거대 다이 (Monolithic) | 독자 규격 칩렛 (Proprietary) | UCIe 개방형 칩렛 |
| --- | --- | --- | --- |
| 제조 수율 | 면적이 커질수록 급락 | 다이 분할로 양호 | 기능별 최적 공정으로 높게 유지 |
| 벤더 호환성 | 칩 내부로 한정 | 동일 제조사 칩렛끼리 결합 | 여러 제조사 칩렛을 조립 가능 |
| 인터페이스 | 칩 내부 전용 버스 | 자체 규격 인터페이스 | 공개 표준, PCIe·CXL 프로토콜 호환 |
| 대역폭 밀도 | 단일 실리콘 기준으로 유리 | 자체 설계로 최적화 | 고급 패키징에서 높은 밀도 |
| 설계 유연성 | 공정 전환 시 전체 재설계 | 일부 모듈 재사용 | 모듈 교체와 조합이 용이 |

- 주요 반도체 기업이 참여한 개방형 표준이라는 점에서, UCIe는 폐쇄적 칩렛 시장을 여러 공급자가 참여하는 조립 시장으로 바꾸는 계기로 평가됨.

## Ⅴ. 칩렛·UCIe 3.0의 한계와 방안

- 핵심 요약 : 칩렛 경계의 지연, 개별 다이 불량, 열팽창 불일치를 미세 접합, 자체 테스트, 유리기판으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 다이 경계의 신호 지연과 전력 | 단일 실리콘과 달리 칩렛 인터페이스를 거쳐 지연과 전송 전력이 증가 | 미세 범프와 Cu-Cu 직접 접합 적용, 저전력 SerDes(Serializer/Deserializer) 설계로 pJ/bit 단위 소비 억제 | 링크 지연 시간, pJ/bit |
| **KGD** (Known Good Die) 선별 어려움 | 칩렛 하나만 불량이어도 고가 패키지 전체가 폐기되는 수율 결합 리스크 | 다이 단위 테스트를 위한 프로브 기술, UCIe 내장 BIST(Built-In Self-Test)와 레인 리페어(Lane Repair) 회로 | 다이 선별 통과율, 패키지 폐기율 |
| **열팽창계수** (CTE, Coefficient of Thermal Expansion) 불일치와 휨 | 소재와 공정이 다른 칩렛이 열에 따라 서로 다르게 팽창해 접합부 균열 발생 | 열팽창 정합성이 좋은 유리기판(Glass Substrate) 도입, **언더필** (Underfill) 소재 고도화 | 기판 휨량, 접합부 균열률 |

## Ⅵ. 칩렛·UCIe 3.0에 대한 기술사적 제언

- 핵심 요약 : 연산 다이 중심의 자체 개발, 패키징 역량의 국가적 육성, 유리기판 로드맵을 묶어 칩렛 전략을 실행 가능한 체계로 전환.

1. 시스템 반도체 기업은 연산 다이만 자체 개발하고, I/O나 메모리 컨트롤러 같은 범용 기능은 검증된 칩렛을 구매하는 조달 전략을 세워 설계 자원을 핵심 연산에 집중한다.
2. 국가와 반도체 생태계는 첨단 2.5D 패키징을 감당할 **OSAT** (Outsourced Semiconductor Assembly and Test, 반도체 후공정 위탁 생산)의 투자 계획을 함께 세워, 패키징이 공급 병목으로 떠오르지 않도록 한다.
3. 패키징 연구 조직은 대면적 유리기판의 공정 로드맵을 작성하고, 열팽창 정합 문제를 검증하는 시험 라인을 미리 준비한다.

## Ⅶ. 결론

- 핵심 요약 : 칩렛과 UCIe는 거대 단일 다이의 한계를 넘는 모듈형 반도체 구조로 수율, 원가, 상호운용성을 확보하는 기술.
- 시사점 : 다이 간 지연, KGD 수율, 열팽창 관리가 제품 신뢰성을 좌우하므로, 설계와 패키징, 테스트를 하나의 계획으로 묶는 것이 전제 조건임.
