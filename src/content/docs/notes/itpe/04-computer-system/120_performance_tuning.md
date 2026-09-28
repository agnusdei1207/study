---
title: "성능 튜닝(Performance Tuning)"
author: "Antigravity"
date: "2026-09-24T21:00:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  label: "120. 성능 튜닝(Performance Tuning)"
  order: 120
  badge:
    text: "응용"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "응용"
---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 → 성능 관리 → 성능 튜닝

## 30초 인출

- 본질: 성능 튜닝은 측정 자료를 바탕으로 서비스 병목을 찾아 개선하는 반복 활동
- 메커니즘: 기준선 계측→병목 가설→한 가지 변경→동일 부하 재측정의 폐루프를 반복
- 통찰: 시스템의 처리량(Throughput)을 극대화하고 응답 시간(Latency)을 단축하기 위해 하드웨어, OS 커널, 데이터베이스, 애플리케이션 전 계층의 병목을 진단하고 최적화함.

<details>
<summary>핵심 용어</summary>

- **성능 튜닝(Performance Tuning):** 측정된 성능 병목의 원인을 개선하고 동일 조건에서 효과를 확인하는 활동
- **병목(Bottleneck):** 처리 경로에서 전체 성능을 제한하는 자원 또는 단계
- **기준선(Baseline):** 비교를 위해 기록한 시스템 성능과 부하 조건
- **처리량(Throughput):** 단위 시간에 완료한 작업량
- **응답 시간(Response Time):** 요청부터 응답 완료까지 걸린 시간

</details>

---

## 2~4교시 예상문제 (25점)

> 성능 튜닝의 개념과 절차를 설명하고, 계층별 병목 분석 및 개선 시 고려사항을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 성능 튜닝의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **성능 튜닝(Performance Tuning):** 측정 자료로 병목을 찾아 구성을 개선하고 결과를 검증하는 활동 |
| 목적 | 정해진 서비스 목표를 만족하도록 응답 시간·처리량·자원 사용을 개선 |

## Ⅱ. 성능 튜닝의 특징

| 특징 | 의미 |
|---|---|
| 목표 기준 | 업무 지연·처리량·오류율 목표를 먼저 고정 |
| 원인 기반 | 관측된 대기와 실제 병목을 구분해 변경 |
| 반복 검증 | 같은 부하·데이터·환경에서 전후 차이를 확인 |

## Ⅲ. 튜닝 체계·프로세스

**핵심 반복 프레임**

```text
업무 목표·대표 부하 → 기준선 계측 → 병목 가설
       → 한 가지 변경·롤백 준비 → 동일 조건 재측정
       → 종단 지연·처리량·오류 비교 → 채택/복원 → 반복
```

**하위 메커니즘: 요청 경로의 병목 추적**

```text
요청 추적 → 앱 처리·WAS 대기·DB 질의·OS/I/O 지연 분해
          → 최초 포화 지점과 후속 대기 구분
          → 원인 계층 변경 → 같은 요청 경로 재추적
```

## Ⅳ. 계층별 관측·개선 비교

| 계층 | 관측 대상 | 개선 방향 예 |
|---|---|---|
| 앱 | 호출 경로·외부 호출 | 불필요한 계산·호출 감소 |
| 런타임·WAS | 스레드 큐·GC | 동시성·메모리 조정 |
| DB | 실행계획·잠금·I/O | 질의·인덱스·트랜잭션 범위 점검 |
| OS·인프라 | CPU·메모리·디스크·네트워크 | 포화 원인과 용량 병목 구분 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 평균 지연만 보면 긴 꼬리 지연을 놓침 | 지연 분포·처리량·오류율을 함께 비교 |
| 부하 조건이 다르면 전후 비교가 왜곡 | 데이터·동시성·환경을 고정하고 기준선 기록 |
| 한 계층 변경이 다른 계층의 병목을 유발 | 요청 추적과 자원 지표로 변경 후 병목 이동 확인 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
브렌던 그레그의 USE(Utilization, Saturation, Errors) 방법론에 입각하여 병목 자원을 과학적으로 식별하고, 단일 파라미터 변경 후 전후 성능을 정량 대조 검증.

### 2. 아키텍처 및 상세 메커니즘
```text
[ 엔드투엔드 시스템 계층별 성능 튜닝 및 진단 파이프라인 ]

  [ 1. 애플리케이션 계층 ] ──> 알고리즘 복잡도 개선, 락 경합 완화, 비동기 논블로킹 I/O
            │
            ▼
  [ 2. 미들웨어/DB 계층 ] ──> 인덱스 최적화, 쿼리 리팩토링, 커넥션 풀(DBCP) 사이징
            │
            ▼
  [ 3. OS 및 커널 계층 ]  ──> TCP 버퍼 크기, 파일 디스크립터 한도, vm.swappiness 튜닝
            │
            ▼
  [ 4. 하드웨어/인프라 ]  ──> CPU 거버너 고성능 설정, NUMA 인터리빙, All-NVMe 교체
```

### 3. 기술 유형 및 비교 평가
| 성능 분석 방법론 | 창안자/원칙 | 핵심 진단 지표 | 적용 대상 |
|---|---|---|---|
| **USE 방법론** | Brendan Gregg | **이용률(Utilization), 포화도(Saturation), 오류(Errors)** | CPU, 메모리, 디스크 등 하드웨어 자원 분석 |
| **RED 방법론** | Tom Wilkie | **요청율(Rate), 오류율(Errors), 지속시간(Duration)** | 마이크로서비스, 웹 API 요청 성능 분석 |
| **Four Golden Signals** | Google SRE | **지연시간(Latency), 트래픽(Traffic), 오류(Errors), 포화도(Saturation)** | 대규모 분산 시스템 모니터링 표준 |

## 출제 이력과 검증 출처

- Brendan Gregg - Systems Performance: Enterprise and the Cloud 2nd Edition (Addison-Wesley)
- Google Site Reliability Engineering (SRE) Handbook: Monitoring Distributed Systems
- Computer Systems: A Programmer's Perspective (CS:APP) - Optimizing Program Performance

## 연결 토픽

- 상위 토픽: [117 하드웨어 사이징](./117_hardware_sizing.md)
- 연관 토픽: [076 CPU](./076_cpu.md), [024 디스크 스케줄링](./024_disk_scheduling.md)
