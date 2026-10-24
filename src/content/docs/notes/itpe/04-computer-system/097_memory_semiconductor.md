---
title: "메모리 반도체"
author: "agnusdei1207"
date: "2026-10-24T22:33:46+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 메모리 반도체, DRAM(Dynamic Random-Access Memory), SRAM(Static Random-Access Memory), NAND 플래시(NAND Flash), MRAM(Magnetoresistive RAM)
- 휘발성 메모리(Volatile Memory), 비휘발성 메모리(Non-Volatile Memory), 리프레시(Refresh), 전하 포획(Charge Trap)
- 3D 적층, HBM(High Bandwidth Memory), CXL(Compute Express Link), PIM(Processing-In-Memory), 메모리 월(Memory Wall)
- P/E 사이클(Program/Erase Cycle), 읽기 방해(Read Disturb), LDPC(Low-Density Parity Check), 웨어 레벨링(Wear Leveling)

## Ⅰ. 메모리 반도체의 개요

- 핵심 요약 : 전원 공급 여부에 따라 휘발성과 비휘발성으로 나뉘는 데이터 저장의 핵심 반도체 소자.
- 개념 : 실리콘 웨이퍼 위에 트랜지스터와 커패시터 등을 집적해 데이터를 저장하는 **메모리 반도체**. 전원이 꺼지면 데이터가 사라지는 **휘발성 메모리** (Volatile Memory)에는 **DRAM**(Dynamic Random-Access Memory)과 **SRAM**(Static Random-Access Memory)이 있고, 전원과 무관하게 데이터가 남는 **비휘발성 메모리** (Non-Volatile Memory)에는 **NAND 플래시** (NAND Flash)와 차세대 **MRAM** (Magnetoresistive RAM) 등이 있음.
- 배경 및 필요성 : AI, 빅데이터, 클라우드 워크로드가 커지면서 대용량 데이터를 병목 없이 프로세서에 공급하고, 저전력으로 안정적으로 보관할 고집적·고대역폭 메모리 수요가 크게 늘어남.
- 주요 목적 : 비트당 제조 비용 절감, 미세화 한계를 넘기 위한 **3차원 적층** (3D Stacking) 구조, 고속 데이터 전송을 위한 **HBM** (High Bandwidth Memory), 시스템 메모리 확장을 위한 **CXL** (Compute Express Link) 지원.

## Ⅱ. 메모리 반도체의 특징 및 장점

- 핵심 요약 : DRAM은 단순한 셀 구조로 집적도를 높이고, 비휘발성 플래시는 전하 포획으로 수직 적층을 가능하게 하는 소자별 원리.

1. DRAM의 1T-1C 셀 구조 : 트랜지스터 하나와 커패시터 하나로 셀을 구성 → 집적도가 매우 높지만, 커패시터 전하가 새어 나가므로 **리프레시** (Refresh)를 주기적으로 수행해야 함.
2. **전하 포획** (Charge Trap) 방식의 **CTF** (Charge Trap Flash) : 절연층 사이의 질화막 트랩에 전자를 가두고 문턱 전압 변화로 비트를 저장 → 평면 미세화의 한계를 넘어 셀을 수직으로 적층하는 3D NAND 구조 실현.

## Ⅲ. 메모리 반도체의 구조 및 동작 메커니즘

- 핵심 요약 : 휘발성은 커패시터 전하나 플립플롭으로, 비휘발성은 전하 포획이나 자기·상변화 물질로 데이터를 유지함.
- 휘발성 소자는 전원이 있는 동안만 상태를 유지하고, 비휘발성 소자는 셀의 물리 상태가 전원 차단 후에도 남는 방식으로 동작함.

```text
[ 메모리 반도체 분류 ]

휘발성 (전원 차단 시 소멸)
  - DRAM: 커패시터 전하로 비트 저장
  - SRAM: 플립플롭으로 상태 유지
비휘발성 (전원 차단 후에도 유지)
  - NAND: 전하 포획 또는 플로팅 게이트
  - 차세대: PRAM, MRAM, ReRAM
```

```text
[ DRAM 셀 데이터 유지 흐름 ]

커패시터에 전하 저장 (1)
      ↓ 시간 경과에 따른 누설
전하 감소
      ↓ 센스 앰프가 읽고 재충전
리프레시로 값 회복
```

## Ⅳ. 메모리 반도체의 비교

- 핵심 요약 : 속도는 SRAM, 집적도와 비트당 비용은 NAND 플래시, 비휘발성과 속도의 균형은 MRAM이 강점을 가짐.
- 비교 대상은 SRAM, DRAM, NAND 플래시, MRAM이며, 주로 셀 구성, 속도, 휘발성, 집적도, 비용, 적용처를 기준으로 본다.

| 비교 축 | SRAM | DRAM | NAND 플래시 | MRAM |
| :--- | :--- | :--- | :--- | :--- |
| 셀 구성 | 트랜지스터 여러 개의 플립플롭 | 트랜지스터 1개와 커패시터 1개 | 플로팅 게이트 또는 전하 포획 트랜지스터 | 트랜지스터 1개와 자기터널접합(MTJ, Magnetic Tunnel Junction) |
| 접근 속도 | 가장 빠름 | 빠름 | 가장 느림 | 빠름 |
| 휘발성 여부 | 휘발성 | 휘발성 | 비휘발성 | 비휘발성 |
| 집적도 | 낮음 | 높음 | 매우 높음 | 중간 |
| 비트당 비용 | 가장 높음 | 중간 | 가장 낮음 | 높음 |
| 주요 적용처 | 중앙처리장치(CPU, Central Processing Unit) 캐시 | 메인 메모리, HBM | SSD(Solid-State Drive), 모바일 저장장치 | 특수 목적 비휘발성 메모리 |

## Ⅴ. 메모리 반도체의 한계와 방안

- 핵심 요약 : 미세 공정 누설, NAND 수명과 간섭, 메모리 월을 소자 구조 전환과 오류 정정, 연산 근접 설계로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| 10나노급 이하 DRAM의 커패시터 종횡비 붕괴 | 커패시터 간격이 좁아져 누설 전류와 브리지 쇼트가 생기고 구조물이 쓰러짐 | **High-k** 유전막 도입, EUV(Extreme Ultraviolet, 극자외선) 다중 패터닝, 2차원 트랜지스터를 수직으로 세우는 3D DRAM 구조 전환 | 셀 누설 전류, 수율 |
| **P/E 사이클** (Program/Erase Cycle) 수명과 **읽기 방해** (Read Disturb) | QLC(Quad-Level Cell, 셀당 4비트) 전환 시 전하 마진이 좁아져 산화막 열화와 인접 셀 간섭이 발생 | **LDPC** (Low-Density Parity Check) 오류 정정 고도화, 웨어 레벨링, 오버 프로비저닝 확대 | 쓰기·지우기 횟수 대비 열화율 |
| **메모리 월** (Memory Wall) | 연산 성능 증가율에 비해 D램 버스의 대역폭 확장이 물리적으로 뒤처짐 | 실리콘 관통 전극(TSV, Through-Silicon Via) 기반 3차원 적층 HBM 도입, CXL 연계, 메모리 내부 연산인 **PIM** (Processing-In-Memory) | 메모리 대역폭 대비 연산 활용률 |

## Ⅵ. 메모리 반도체 적용에 대한 기술사적 제언

- 핵심 요약 : 고대역폭 메모리의 공동 설계 체계와 메모리를 연산 자원으로 다루는 소프트웨어 생태계를 함께 키우는 방향.
- 고대역폭 메모리 수요가 커지면서, 메모리 기업과 설계 기업이 초기 단계부터 함께 설계하는 파운드리 협력 모델이 경쟁력의 한 축이 된다.
- 메모리를 단순 저장 부품이 아닌 연산 자원으로 활용하려면, OS의 메모리 티어링 지원, CXL 오케스트레이션, PIM용 컴파일러 체계를 오픈소스 생태계에서 함께 키우는 전략이 필요하다.
- 기술 로드맵에서는 미세 공정 전환 속도만 보지 말고, 소자 구조 전환과 소프트웨어 대응을 같은 일정표에 올려 리스크를 줄이는 방식이 바람직하다.

## Ⅶ. 결론

- 핵심 요약 : 메모리 반도체는 휘발성과 비휘발성 소자로 데이터 저장의 기반이며, 미세화와 대역폭 한계를 구조 전환으로 넘는 산업.
- 10나노급 DRAM, NAND 수명, 메모리 월 리스크는 소자 구조와 소프트웨어 생태계를 함께 바꾸는 방식으로 관리해야 한다.
