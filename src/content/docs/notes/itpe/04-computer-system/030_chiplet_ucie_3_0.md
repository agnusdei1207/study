---
title: "칩렛과 UCIe 3.0 (UCIe: Universal Chiplet Interconnect Express)"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- 칩렛(Chiplet), UCIe(Universal Chiplet Interconnect Express), 단일 거대 다이(Monolithic Die), 레티클 한계(Reticle Limit)
- 이종 집적(Heterogeneous Integration), 물리 계층(Physical Layer), D2D 어댑터(Die-to-Die Adapter), 프로토콜 계층(Protocol Layer)
- UCIe-S, UCIe-A, UCIe-3D, KGD(Known Good Die), 열팽창계수(CTE, Coefficient of Thermal Expansion), 유리기판(Glass Substrate), OSAT(Outsourced Semiconductor Assembly and Test)

## Ⅰ. 칩렛·UCIe 3.0의 개요

- 핵심 요약 : 거대 단일 다이의 수율 한계를 넘기 위해 기능별 다이를 개방형 인터커넥트 표준 UCIe로 결합하는 모듈형 반도체 구조.
- 개념 : **칩렛** (Chiplet)은 연산, 입출력, 메모리 제어 같은 기능을 나눠 만든 소형 다이로, 패키지 안에서 결합해 하나의 시스템처럼 동작하게 하는 구성 단위.
- 배경 및 필요성 : 한 장의 실리콘에 모든 기능을 넣는 **단일 거대 다이** (Monolithic Die)는 면적이 **레티클 한계** (Reticle Limit)에 가까울수록 불량 확률이 커져 수율이 급락하고, 무어의 법칙(Moore's Law) 둔화로 공정 미세화만으로 성능을 끌어올리기 어려워 **이종 집적** (Heterogeneous Integration)이 대안으로 부상함.
- 주요 목적 : 수율과 원가 개선, 공정별 최적화, 개방형 표준 **UCIe** (Universal Chiplet Interconnect Express)를 통한 벤더 간 상호운용성 확보.

## Ⅱ. 칩렛·UCIe의 특징 및 장점

- 핵심 요약 : 3계층 인터페이스와 이종 공정 결합, 개방형 표준이 맞물려 여러 공급자의 칩렛을 조립하는 설계를 가능하게 하는 구조.

1. **물리 계층** (Physical Layer) : 미세 범프와 고속 신호 인터페이스로 데이터 레인과 사이드밴드를 구동 → 칩렛 사이 전송의 물리 기반 확보.
2. **D2D 어댑터** (Die-to-Die Adapter) : CRC(Cyclic Redundancy Check) 검증, 재전송 버퍼링, 흐름 제어를 담당 → 칩렛 링크의 신뢰성 보장.
3. **프로토콜 계층** (Protocol Layer) : PCIe(Peripheral Component Interconnect Express)와 CXL(Compute Express Link) 같은 검증된 프로토콜을 그대로 실어 나름 → 기존 소프트웨어 자산의 재사용.
4. 패키지 등급의 다양성 : 표준 패키지용 **UCIe-S**, 첨단 2.5D용 **UCIe-A**, 3D 적층용 **UCIe-3D**로 구분 → 비용과 대역폭 밀도에 따른 선택 가능.
5. UCIe 3.0 세대 기능 : 2025년 공개된 UCIe 3.0은 회선 속도를 48·64 GT/s로 두 배 높이고, 동작 중 재보정과 100mm까지 확장된 사이드밴드 도달 범위, 우선순위 사이드밴드 패킷을 지원 → 대역폭 밀도와 시스템 관리성의 동시 확대.

## Ⅲ. 칩렛·UCIe의 구조 (흐름)

- 핵심 요약 : 프로토콜, 어댑터, 물리 계층의 세 층이 표준 인터페이스로 이어지고, 칩렛은 패키지 등급에 따라 실장 경로가 나뉘는 구조.
- 세 계층 사이에는 FDI(Flit-aware Die-to-Die Interface)와 RDI(Raw Die-to-Die Interface)라는 표준 경계 인터페이스가 위치함.

```text
[ UCIe 3계층 구조 ]

프로토콜 계층 (PCIe, CXL, Streaming)
   ↓ FDI
D2D 어댑터 (CRC, 재전송, 흐름 제어)
   ↓ RDI
물리 계층 (데이터 레인, 사이드밴드)
```

```text
[ 칩렛 패키징 경로 ]

칩렛 다이 (UCIe 인터페이스 탑재)
   ↓ 배치 방식에 따라 선택
UCIe-S : 표준 유기 기판
UCIe-A : 실리콘 인터포저 (2.5D)
UCIe-3D : 미세 접합 직접 적층 (3D)
```

## Ⅳ. 단일 거대 다이와 칩렛 구조의 비교

- 핵심 요약 : 수율, 호환성, 설계 유연성에서 단일 거대 다이, 독자 규격 칩렛, UCIe 개방형 칩렛의 차이가 뚜렷함.

| 비교 항목 | 단일 거대 다이 | 독자 규격 칩렛 | UCIe 개방형 칩렛 |
| --- | --- | --- | --- |
| 제조 수율 | 면적이 커질수록 급락 | 다이 분할로 양호 | 기능별 최적 공정으로 유지 |
| 벤더 호환성 | 칩 내부로 한정 | 동일 제조사끼리 결합 | 여러 제조사 칩렛 조립 |
| 인터페이스 | 칩 내부 전용 버스 | 자체 규격 | 공개 표준, PCIe·CXL 호환 |
| 대역폭 밀도 | 단일 실리콘 기준 유리 | 자체 설계 최적화 | 고급 패키지에서 높은 밀도 |
| 설계 유연성 | 공정 전환 시 전면 재설계 | 일부 모듈 재사용 | 모듈 교체와 조합 용이 |

- 선택 기준 : 최고 성능 단일 제품은 단일 거대 다이, 자사 제품군 내 최적화는 독자 규격, 공급망 다변화와 조립형 설계는 UCIe 개방형 표준을 선택하는 기준이 합리적.

## Ⅴ. 칩렛·UCIe의 한계와 방안

- 핵심 요약 : 다이 경계 지연, 개별 다이 불량, 열팽창 불일치를 저전력 설계, 자가 시험, 소재 정합 관리로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 다이 경계의 지연과 전력 | 단일 실리콘과 달리 인터페이스를 거치며 지연과 전송 전력 증가 | 저전력 SerDes(Serializer/Deserializer) 설계와 접합 밀도 개선 | 링크 지연, pJ/bit |
| **KGD** (Known Good Die) 선별 부담 | 칩렛 하나만 불량이어도 패키지 전체 폐기 → 수율 결합 리스크 | 다이 단위 테스트와 UCIe 내장 자가 시험, 레인 리페어 회로 | 다이 통과율, 패키지 폐기율 |
| **열팽창계수** (CTE, Coefficient of Thermal Expansion) 불일치 | 소재가 다른 칩렛이 열에 따라 다르게 팽창해 접합부 균열 발생 | 열팽창 정합성이 좋은 **유리기판** (Glass Substrate) 검토, 언더필 소재 고도화 | 기판 휨량, 균열률 |

## Ⅵ. 칩렛·UCIe에 대한 기술사적 제언

- 핵심 요약 : 핵심 다이 자체 개발, 후공정 역량 육성, 상호운용성 시험 참여를 묶어 칩렛 전략을 실행 체계로 전환.

1. 시스템 반도체 기업은 연산 다이만 자체 개발하고 입출력 같은 범용 칩렛은 검증된 공급처에서 조달해 설계 자원을 핵심 기능에 집중한다.
2. 반도체 생태계는 첨단 패키징을 감당할 **OSAT** (Outsourced Semiconductor Assembly and Test)의 투자 계획을 공동으로 세워 후공정이 공급 병목이 되지 않게 한다.
3. 표준 참여 조직은 UCIe 준수성 시험과 상호운용성 행사에 참여해 자사 칩렛의 생태계 호환성을 조기에 검증한다.

## Ⅶ. 결론

- 핵심 요약 : 칩렛과 UCIe는 거대 단일 다이의 한계를 넘는 모듈형 반도체 구조로 수율, 원가, 상호운용성을 함께 확보하는 기술.
- 다이 간 인터페이스 품질과 양품 다이 선별, 열 정합 관리가 제품 신뢰성의 관건이 됨.
