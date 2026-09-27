---
title: "NOMA(Non-Orthogonal Multiple Access)"
author: "Codex"
date: "2026-09-24T21:25:00+09:00"
tags:
  - "notes-network"
sidebar:
  label: "054. NOMA(Non-Orthogonal Multiple Access)"
  badge:
    text: "응용"
    variant: note
extra:
  keyword_grade: "응용"
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 핵심 개념 → NOMA

## 30초 인출

- 본질: **NOMA (Non-Orthogonal Multiple Access)** 는 여러 사용자가 일부 무선 자원을 비직교 방식으로 공유하는 다중접속 계열
- 메커니즘: 전력 도메인 NOMA에서는 같은 시간·주파수 자원에 신호를 중첩하고 수신기가 SIC 등으로 신호를 분리
- 통찰: 한계: 신호 중첩만으로 사용자 처리량이 늘지는 않고 채널 추정·SIC 오류가 후속 복호에 전파됨 → 방안: 실제 채널 분포와 복호 순서별 오류율을 OMA 기준과 비교

<details>
<summary>핵심 용어</summary>

- **NOMA (Non-Orthogonal Multiple Access)** : 일부 시간·주파수·코드 자원을 비직교 공유하는 다중접속 방식의 총칭
- **Power-domain NOMA** : 같은 시간·주파수 자원에 사용자 신호를 서로 다른 전력으로 중첩하는 방식
- **SIC (Successive Interference Cancellation)** : 신호를 순차 복호하고 재구성한 간섭 성분을 빼며 다음 신호를 복호하는 기법
- **OMA (Orthogonal Multiple Access)** : 사용자별 자원을 직교 분할해 동일 차원에서 겹침을 줄이는 다중접속 방식

</details>

---

## 2~4교시 예상문제 (25점)

> NOMA의 비직교 자원 공유와 SIC 동작을 설명하고, OMA와 비교하여 채널 추정·복호 오류의 한계와 대응책을 제시하시오. (예상·25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **NOMA (Non-Orthogonal Multiple Access)** 은 여러 사용자가 무선 자원을 비직교 방식으로 공유하는 다중접속 계열 |
| 목적 | 직교 자원 분할과 다른 신호 중첩·복호 방식을 통해 자원 이용 대안을 제공 |

## Ⅱ. 전력 도메인 NOMA와 SIC

```text
기지국: s = √p₁·s₁ + √p₂·s₂
                 ↓ 동일 시간·주파수 자원
수신기: 중첩 신호
   └─ 복호 가능한 간섭 성분 복호·재구성·제거
                 ↓
         목표 사용자 신호 복호
```

## Ⅲ. 관련 개념과 구분

### 설계 요소와 한계

| 요소 | 설계 내용 | 한계 |
|---|---|---|
| 사용자 자원 공유 | 같은 자원에 신호 중첩; 구체 구조는 NOMA 유형에 따라 다름 | 사용자 간 간섭 발생 |
| 전력 할당 | 전력 도메인에서 채널·수신 조건을 고려해 할당 | 채널 추정 오차가 복호 순서·성능에 영향 |
| SIC 수신 | 복호한 간섭 신호를 재구성해 수신 신호에서 제거 | 복호 오류가 뒤 단계로 전파될 수 있음 |

| 구분 | OMA | 전력 도메인 NOMA |
|---|---|---|
| 자원 배치 | 사용자별 직교 자원 할당 | 같은 시간·주파수 자원에 신호 중첩 가능 |
| 수신 처리 | 직교성 기반 분리 | 수신기에서 간섭 처리; SIC가 한 방법 |
| 판단점 | 자원 효율·스케줄링 | 채널 조건·수신 복잡도·오류 전파 |

## Ⅳ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 불완전한 채널 추정·복호 실패가 SIC 잔여 간섭을 키울 수 있음 | 수신 품질·복호 순서별 오류율을 측정하고 전력 할당·사용자 묶음을 조정 |
| 사용자 수·수신 처리 단계가 커지면 계산 부담 증가 | 실제 단말 처리 능력과 서비스 요구를 반영해 사용자 그룹 크기를 결정 |

## Ⅴ. 제언

- NOMA는 이론상 신호 중첩 이득보다 실제 채널의 SIC 오류와 OMA 대비 처리량을 먼저 검증한다.

## 출제 이력과 검증 출처

- 제129회 1교시 관련 문항은 공식 문제지 원문을 확보하지 못해 회차·문구를 검증하지 못함.
- [3GPP TR 38.812, Study on Non-Orthogonal Multiple Access for NR](https://portal.3gpp.org/Specifications.aspx?WiUid=750046&q=1)
- [ETSI GR MAT 001 V1.1.1, Multiple Access Techniques](https://www.etsi.org/deliver/etsi_gr/MAT/001_099/001/01.01.01_60/gr_MAT001v010101p.pdf)
