---
title: "CCPM·TOC (CCPM: Critical Chain Project Management; TOC: Theory of Constraints)"
author: "agnusdei1207"
date: "2026-10-01T22:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "LongCat 2.5 Preview Free"
---

## 연관 키워드

- CCPM(Critical Chain Project Management, 크리티컬 체인 프로젝트 관리)
- TOC(Theory of Constraints, 제약이론), 골드랫(Goldratt)
- CPM(Critical Path Method, 주공정법), PERT(Program Evaluation and Review Technique)
- 파킨슨의 법칙(Parkinson's Law), 학생 증후군(Student Syndrome)
- 프로젝트 버퍼(PB, Project Buffer), 피딩 버퍼(FB, Feeding Buffer), 자원 버퍼(RB, Resource Buffer)
- 버퍼 관리(Buffer Management), 피버 차트(Fever Chart)
- 드럼-버퍼-로프(DBR, Drum-Buffer-Rope), EVM(Earned Value Management)
- SV(Schedule Variance), SPI(Schedule Performance Index), 멀티태스킹(Multitasking)
- 크리티컬 체인(Critical Chain), 자원 제약(Resource Dependencies)

## Ⅰ. CCPM·TOC의 개요

- 핵심 요약 : 제약이론(TOC)을 프로젝트 일정 관리에 적용하여 자원 제약을 고려하고 안전 여유를 버퍼로 집중 관리하는 크리티컬 체인 프로젝트 관리 기법.
- 개념 : 골드랫(Goldratt) 박사의 제약이론(TOC, Theory of Constraints)을 프로젝트 일정 관리에 적용한 기법으로 작업 경로 간의 자원 제약(Resource Dependencies)을 고려하고 개별 작업의 안전 여유(Safety Time)를 제거하여 프로젝트 말단과 합류 지점에 버퍼(Buffer)로 집중 관리하는 크리티컬 체인 프로젝트 관리(CCPM, Critical Chain Project Management).
- 배경 및 필요성 : 전통적 CPM(Critical Path Method)/PERT(Program Evaluation and Review Technique) 방식에서 개별 작업자마다 안전 시간을 부여함에도 불구하고 파킨슨의 법칙과 학생 증후군으로 인해 프로젝트가 항상 지연되는 모순을 극복하기 위해 창안.
- 주요 목적 : 프로젝트 전체 납기 대폭 단축, 자원 충돌 방지, 버퍼 관리(Buffer Management)를 통한 조기 지연 경보.

## Ⅱ. CCPM·TOC의 특징 및 장점

- 핵심 요약 : 자원 제약 기반 크리티컬 체인 설정과 안전 여유 제거 후 버퍼 집중 관리, 인간 행동 법칙 극복.

1. **자원 제약 반영** : 작업 선후관계와 핵심 인력의 사용 가능 시점을 함께 고려해 일정 충돌을 줄인다.
2. **크리티컬 체인 식별** : 자원 의존성을 포함한 제약 경로를 찾아 관리 대상을 집중한다.
3. **버퍼 집중 배치** : 분산된 안전 여유를 프로젝트·피딩 버퍼로 모아 전체 납기 보호에 활용한다.
4. **조기 인계** : 작업을 끝낸 즉시 다음 단계로 전달하여 학생 증후군·파킨슨 법칙의 영향을 줄인다.
5. **버퍼 소진율 관리** : 진척 대비 남은 버퍼를 관찰하여 지연 징후에 일찍 대응한다.

## Ⅲ. CCPM·TOC의 구조 (흐름)

- 핵심 요약 : 안전 여유 제거와 버퍼 배치, 크리티컬 체인 식별 후 버퍼 소진율 모니터링 흐름.
- CCPM 버퍼 집약 메커니즘.

```text
[전통적 방식: 안전 여유의 낭비]
  - 파킨슨의 법칙 (Parkinson's Law) :
    작업에 주어진 시간만큼 업무가 늘어남
  - 학생 증후군 (Student Syndrome) :
    마감 직전까지 작업을 미루다가 시작함
  - 조기 완료 미반영 : 일찍 끝나도
    다음 작업에 조기 인계하지 않음
        ↓
[CCPM 방식: 공격적 일정 추정 + 버퍼 집중]
  - 개별 작업의 기간을 50% 확률 수준
    (낙관적 추정)으로 대폭 축소
  - 깎아낸 안전 여유의 50%를 모아서
    프로젝트 맨 뒤에 [프로젝트 버퍼(PB)]로 일괄 배치
  - 비주공정 경로가 합류하는 지점에
    [피딩 버퍼(FB)] 배치,
    자원 경합에 [자원 버퍼(RB)] 배치
```

```text
[버퍼 관리 모니터링 흐름]
  버퍼 소진율 측정
        │
        ├─ 녹색(안전) : 관리 불필요
        ├─ 황색(주시) : 대책 수립
        └─ 적색(위험) : 즉각 시정 조치
               │
               └─ 피버 차트(Fever Chart) 시각화
```

- 파킨슨의 법칙 : 작업에 주어진 시간만큼 업무가 늘어남.
- 학생 증후군 : 마감 직전까지 작업을 미루다가 시작함.
- 프로젝트 버퍼(PB, Project Buffer) : 깎아낸 안전 여유를 모아 프로젝트 맨 뒤에 일괄 배치.
- 피딩 버퍼(FB, Feeding Buffer) : 비주공정 경로가 합류하는 지점에 배치.

## Ⅳ. CPM과 CCPM의 비교

- 핵심 요약 : 논리 의존관계만 고려하는 CPM과 자원 제약·버퍼 관리를 결합한 CCPM의 비교.
- CPM(Critical Path Method)과 CCPM(Critical Chain Project Management)의 대비.

| 비교 항목 | CPM (Critical Path Method) | CCPM (Critical Chain Project Management) |
|---|---|---|
| 경로 결정 기준 | 작업 간의 논리적 선후 의존관계만 고려 | 작업 의존관계 + 한정된 인적/물적 자원의 제약 동시 고려 |
| 안전 여유(안전시간) | 각 작업 패키지마다 개별적으로 분산 배치 | 개별 작업에서 제거하여 프로젝트/피딩 버퍼로 통합 배치 |
| 진척 관리 지표 | 계획 대비 완료율(%), EVM(Earned Value Management) 기반 SV(Schedule Variance)·SPI(Schedule Performance Index) | 버퍼 소진율(Buffer Burn Rate) 대비 공정 진척도 |
| 작업 시작 태도 | 늦은 시작일(Late Start)까지 지연 가능 | 작업이 가능해지는 즉시 신속 착수(Relay Runner 태도) |

## Ⅴ. CCPM·TOC 적용의 한계와 방안

- 핵심 요약 : **버퍼에 대한 신뢰**, 제약 자원 경합, 요구 변경을 함께 관리해야 일정 예측력이 유지된다.

| 한계 | 방안 |
|---|---|
| 작업별 안전 여유 제거를 **개인 일정 압박**으로 받아들일 수 있음 | 버퍼를 팀 공동 자산으로 설명하고 개인 마감 준수보다 전체 흐름을 평가 |
| 여러 프로젝트가 같은 **병목 자원**을 요구하면 우선순위 충돌 발생 | 포트폴리오 단위 우선순위를 정하고 병목 인력의 동시 작업을 제한 |
| 잦은 요구 변경은 계획한 **버퍼를 조기 소진**시킴 | 변경 영향에 따라 체인을 재산정하고 피버 차트로 소진율·진척률을 함께 감시 |

## Ⅵ. CCPM 버퍼 관리의 실무 적용을 위한 기술사적 제언

- 핵심 요약 : 3색 버퍼 관리 신호등, 멀티태스킹 금지, 문화적 신뢰 구축.

- 3색 버퍼 관리 신호등 체계 운영 : 버퍼 소진율에 따라 녹색(안전), 황색(주시/대책 수립), 적색(즉각적 시정 조치 발동)의 3단계 동적 통제 확립.
- 멀티태스킹(Multitasking)의 엄격한 금지 : 여러 프로젝트에 인력을 쪼개어 배정할 경우 발생하는 잦은 컨텍스트 스위칭(Context Switching) 낭비를 차단하고 단일 과업 집중 환경 보장.
- 문화적 신뢰 구축(Blameless Culture) : 공격적인 50% 추정 일정으로 인해 개별 작업이 마감일을 넘기더라도 개발자를 문책하지 않고 전체 버퍼 소진 여부로 평가하는 심리적 안전감 제공 필수.

## Ⅶ. 결론

- 핵심 요약 : CCPM은 자원 제약과 안전 여유 제거 후 버퍼 집중 관리로 프로젝트 납기를 단축하는 기법으로 조직 문화 정착이 관건.
- 요약 : CCPM은 제약이론(TOC)을 프로젝트 일정 관리에 적용하여 자원 제약을 고려하고 안전 여유를 버퍼로 집중 관리하는 프로젝트 관리 기법.
- 시사점 : 3색 버퍼 관리 신호등, 멀티태스킹 금지, 블램리스 문화 구축을 통해 조직적 수용성과 실무 정착 필요.
