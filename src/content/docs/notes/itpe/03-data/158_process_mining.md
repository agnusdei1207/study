---
title: "프로세스 마이닝 (Process Mining)"
author: "agnusdei1207"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Antigravity Professional Engine"
---

## 연관 키워드

**프로세스 마이닝(Process Mining)**, **이벤트 로그(Event Log)**, **Discovery/Conformance/Enhancement**, **Alpha Miner**, **Heuristic Miner**, **RPA**, **EMS**

## Ⅰ. 개요

- 핵심 요약 : **프로세스 마이닝**은 이벤트 로그로부터 실제 업무 프로세스를 자동 추출·검증·개선하는 데이터 과학 기법.
- 목적 : 사실 기반 프로세스 분석, 병목 진단.
- 배경 : 인터뷰·설문 기반 BPR의 주관성 극복.
- 특징 : 3대 유형, C-A-T 로그, Alpha/Heuristic Miner, 적합도 척도.

## Ⅱ. 특징 및 장점

- 핵심 요약 : **발견·적합성·향상** 3유형으로 프로세스 가시화·검증·최적화.
- **Discovery** : 로그만으로 실제 프로세스 모델 자동 도출.
- **Conformance** : 표준 모델 vs 실제 로그 불일치 탐지.
- **Enhancement** : 병목 제거·RPA·재설계.
- **C-A-T 로그** : Case ID, Activity, Timestamp.
- **4대 품질** : 재현율·정밀도·일반화·간결성.

## Ⅲ. 3대 유형 흐름

- 핵심 요약 : **Discovery → Conformance → Enhancement**.
- C-A-T 최소 로그 구조.

```text
[ 프로세스 마이닝 3대 유형 ]

[Discovery]  [Conformance]  [Enhancement]
 사전 모델    표준 vs 실제   병목 제거·
 없이 로그로  불일치 탐지     RPA·재설계
 모델 자동 도출
```

```text
[ 이벤트 로그 (C-A-T) ]

Case ID | Activity | Timestamp
-------+----------+-----------
Order  | 주문 접수 | 09:00:00
Order  | 결제 승인 | 09:05:00
Order  | 배송 준비 | 11:00:00
```

## Ⅳ. 발견 알고리즘·품질 척도 비교

- 핵심 요약 : **Alpha/Heuristic/DFG** 알고리즘과 **4대 품질 척도**.

| 알고리즘 | 특징 | 적합 상황 |
|---|---|---|
| Alpha Miner | 페트리 넷 변환, 노이즈 취약 | 이론적 기초 |
| Heuristic Miner | 빈도 기반 노이즈 필터링 | 실무 복잡 프로세스 |
| DFG | 직관적 전이 그래프 | 상용 툴 (Celonis) |

- 4대 품질 : 재현율(Fitness), 정밀도(Precision), 일반화(Generalization), 간결성(Simplicity).

## Ⅴ. 한계와 방안

- 핵심 요약 : **스파게티 프로세스·로그 품질·컨포먼스 괴리**를 필터링·전처리·얼라인먼트로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
|---|---|---|---|
| 스파게티 프로세스 | 예외 경로 노출로 판독 불가 | 빈도 기반 필터링, Fuzzy Miner | 경로 수 |
| 로그 품질 불량 | Case ID 누락·타임스탬프 역전 | 전처리 파이프라인, ms 표준화 | 데이터 품질 |
| 컨포먼스 괴리 | 합리적 예외까지 위반 판정 | Alignment 페널티 튜닝, 표준 모델 개정 | 적합도 |

## Ⅵ. 기술사적 제언

- 핵심 요약 : **RPA 대상 발굴·실시간 EMS**로 디지털 전환.
- RPA : Happy Path 정량 도출로 ROI 극대화.
- EMS : Kafka + Celonis 실시간 연동, 자동 티켓 발행.

## Ⅶ. 결론

- 핵심 요약 : 프로세스 마이닝은 **사실 기반 프로세스 분석**으로 Discovery/Conformance/Enhancement가 핵심.
- 답안에는 3대 유형, C-A-T 로그, 4대 품질, 한계·대응을 연결.
- 참고 : [Process Mining (van der Aalst)](https://www.processmining.org/).