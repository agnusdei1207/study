---
title: "성능 요구사항(Performance Requirement)"
author: "agnusdei1207"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## 연관 키워드

- 성능 요구사항(Performance Requirement), 비기능 요구사항(NFR, Non-Functional Requirement), 응답시간(Response Time)
- 처리량(Throughput/TPS), 백분위수 지표(P95/P99), SLA(Service Level Agreement)/SLO(Service Level Objective)/SLI(Service Level Indicator), 부하 테스트, 용량 산정(Capacity Planning)

## Ⅰ. 성능 요구사항의 개요

- 핵심 요약 : 시스템이 만족해야 하는 반응성·처리량·자원 소모율의 정량적 검증 가능 비기능 요구사항.
- 개념 : 성능 요구사항(Performance Requirement)이란 소프트웨어 시스템이 특정 워크로드 및 운영 환경 하에서 비즈니스 기능을 수행할 때 만족해야 하는 시간적 반응성(응답시간), 작업 처리량(Throughput), 시스템 자원 소모율(CPU(Central Processing Unit), 메모리, 네트워크 대역폭)에 대한 정량적이고 검증 가능한 비기능 요구사항(NFR, Non-Functional Requirement).
- 배경 및 필요성 : 시스템의 기능이 완벽히 동작하더라도 응답 지연이 길어지면 사용자가 이탈하고, 대규모 동시 접속 상황에서 서버가 뻗는 성능 병목은 막대한 금전적 손실과 대외 신뢰도 추락을 초래하므로 설계 초기부터 엄격한 통제 필수.
- 표준 기준 : ISO(International Organization for Standardization)/IEC(International Electrotechnical Commission) 25010 성능 효율성(Performance Efficiency) 모델, SLA(Service Level Agreement)/SLO(Service Level Objective)/SLI(Service Level Indicator) 체계.

## Ⅱ. 성능 요구사항의 특징

- 핵심 요약 : 4대 핵심 지표와 백분위수 기반 측정, 부하 테스트 유형별 검증으로 구성되는 정량 성능 체계.

1. 응답시간(Response Time) : 요청 전송 후 첫/마지막 바이트 수신까지의 시간.
2. 처리량(Throughput/TPS) : 단위 시간(1초)당 처리 트랜잭션 수.
3. 자원 사용률(Utilization) : 피크 부하 시 CPU·메모리 사용률의 임계치 이하 유지.
4. 턴어라운드 시간(Turnaround) : 배치 작업 제출 후 완료까지의 시간.
5. 백분위수 기반 측정(P95, P99) : 산술 평균의 왜곡을 배제한 사용자 체감 지표 관리.
6. 부하(Load)·스트레스(Stress)·내구성(Soak/Endurance) 테스트의 유형별 검증.

- 응답시간(Response Time) vs 지연시간(Latency) : 지연시간은 네트워크 전송 대기 시간이며, 응답시간은 네트워크 왕복 시간에 서버 내부의 처리 및 DB(Database) 쿼리 시간이 모두 포함된 사용자 체감 시간.
- 백분위수 기반 응답시간(P95, P99) : 산술 평균 응답시간은 극단적인 긴 지연을 감추는 왜곡이 발생하므로, 전체 사용자의 95%, 99%가 경험하는 지연시간을 SLO 기준으로 수립.

## Ⅲ. 성능 요구사항의 구조 (흐름)

- 핵심 요약 : 4대 지표 정의에서 부하 테스트 3대 유형 검증으로 이어지는 성능 검증 체계.

```text
[ 성능 요구사항 4대 핵심 지표 ]
 1. 응답시간 (Response Time)
    - 요청 전송 후 첫/마지막 바이트 수신
 2. 처리량 (Throughput / TPS)
    - 단위 시간(1초)당 처리 트랜잭션
 3. 자원 사용률 (Utilization)
    - 피크 부하 시 CPU·메모리 사용률
      임계치 이하 유지
 4. 턴어라운드 시간 (Turnaround)
    - 배치 작업 제출 후 완료까지의 시간
   │ (성능 검증 테스팅)
   ▼
[ 부하 테스팅 3대 유형 ]
 - 부하 테스트 (Load): 정상 예측
   트래픽 하 성능 목표 달성 검증
 - 스트레스 테스트 (Stress): 임계치
   초과하여 다운 시점 확인
 - 내구성 테스트 (Soak/Endurance):
   장시간 연속 실행 시 메모리 누수
```

- 성능 요구사항의 정립 및 검증 프로세스.

```text
[ 1. 성능 목표 정량화 ]
 (SMART 원칙, SLO 수립)
   │
   ▼
[ 2. 아키텍처 설계 반영 ]
 (인프라 규모, 캐시, 인덱스)
   │
   ▼
[ 3. 조기 성능 PoC ]
   │
   ▼
[ 4. 부하·스트레스 테스트 ]
 (nGrinder, JMeter)
   │
   ▼
[ 5. CI 기반 지속 검증 ]
```

- 지표 표준화 : SLA(Service Level Agreement) 계약 수준의 성능 목표를 SLO(Service Level Objective)로 세분화하고 SLI(Service Level Indicator)로 측정.

## Ⅳ. 기능 요구사항과 성능 요구사항의 비교

- 핵심 요약 : '무엇을 한다'와 '얼마나 빠르게 한다'의 요구사항 유형별 차이.

| 비교 항목 | 기능 요구사항 (Functional) | 성능 요구사항 (Performance / NFR) |
|---|---|---|
| 정의 | 시스템이 제공해야 하는 특정 업무 행위 (What to do) | 시스템이 동작할 때 발휘해야 하는 처리 속도와 용량 (How fast) |
| 기술 방식 | '사용자는 신용카드로 결제할 수 있어야 한다' | '동시 5,000명 접속 시 결제 승인 응답시간은 P95 기준 1.5초 이하' |
| 영향 범위 | 개별 비즈니스 로직 클래스, 엔티티, 화면 UI(User Interface) | 전체 인프라 규모(서버 대수), DB 인덱스, 분산 캐시 아키텍처 |
| 결함의 징후 | 오작동, 기능 실패, 예외 메시지 출력 | 타임아웃(HTTP(Hypertext Transfer Protocol) 504), CPU 100% 포화, 스레드 고갈, 서버 다운 |
| 검증 도구 | JUnit, Postman, Selenium | nGrinder, Apache JMeter, Locust, k6 |

## Ⅴ. 성능 요구사항의 장점과 한계

- 핵심 요약 : 사용자 경험·안정성 보장의 장점, 모호한 기술·비현실적 피크 설정·조기 검증 부재 측면의 한계.

- 장점
  1. 정량 목표 기반 인수 판정을 통한 발주자·사업자 분쟁 예방.
  2. 설계 초기 인프라 규모 산정의 과학화.
  3. SLA 기반 운영 품질의 계약적 보장.

- 한계점 1 : 모호하고 정성적인 성능 요구사항 기술로 인한 검증 불가
  - 한계점 : '시스템은 신속하게 응답해야 한다'와 같은 추상적 기술로 인해 개발 완료 후 발주자와 사업자 간 인수 테스트 통과 기준 분쟁 발생.
  - 해결 방안 : SMART 원칙(Specific, Measurable, Achievable, Relevant, Time-bound) 기반 정량화, 퍼센타일 기준 응답시간(p95 1초 이내, p99 2초 이내), 동시 접속자 수(CCU), 초당 트랜잭션 수(TPS, Transactions Per Second) 등 구체적 SLO 명문화.
- 한계점 2 : 비현실적 피크 부하 설정으로 인한 인프라 비용 과다 계상
  - 한계점 : 연중 드물게 발생하는 극단적 스파이크 트래픽을 상시 성능 요구사항으로 설정하여 고정 온프레미스 인프라 구축 비용의 기하급수적 폭증.
  - 해결 방안 : 평상시와 피크 시 성능 목표 분리, 클라우드 오토스케일링(HPA, Horizontal Pod Autoscaler) 및 큐 기반 버퍼링 아키텍처를 전제로 한 탄력적 성능 목표 수립.
- 한계점 3 : 아키텍처 설계와 성능 요구사항 간의 조기 검증 체계 부재
  - 한계점 : 프로젝트 후반 통합 테스트 단계에서 성능 요구사항을 처음 검증하다가 아키텍처 결함이 발견되어 납기 내 수정 불가 상황 직면.
  - 해결 방안 : 개발 초기 단계부터 핵심 트랜잭션에 대한 아키텍처 PoC(Proof of Concept) 및 지속적 성능 테스트(Continuous Performance Testing)를 CI(Continuous Integration) 파이프라인에 통합.

## Ⅵ. 시스템 엔지니어링 관점에서의 기술사적 제언

- 핵심 요약 : SMART 원칙 기반 정량화와 대기행렬 이론 기반 선제적 용량 산정의 병행.
- 모호한 표현 배제 및 SMART 원칙(Specific, Measurable, Achievable, Relevant, Time-bound) 기반 정량화 : '시스템은 신속해야 한다'는 식의 주관적 기술을 철저히 금지하고, '피크 시간대 기준 동시 사용자 10,000명, 초당 트랜잭션 2,500 TPS 환경에서 평균 응답시간 0.8초 이하, P99 응답시간 2.0초 이하'와 같은 정량적 SLA 지표 명시 필수.
- 선제적 용량 산정(Capacity Planning) 및 성능 튜닝 거버넌스 수립 : 개발 완료 후 사후 튜닝은 아키텍처적 한계로 실패하기 쉬우므로, 아키텍처 설계 단계에서 대기행렬 이론(Little's Law, M/M/c 모델)을 적용하여 WAS(Web Application Server) 스레드 풀, DB 커넥션 풀(HikariCP), 네트워크 대역폭을 이론적으로 사전 계산하고 부하 시험으로 실측 검증 병행.

## Ⅶ. 결론

- 핵심 요약 : 성능 요구사항은 정량·검증 가능해야만 성립하며, 조기 검증과 선제 용량 산정이 실패 방지의 핵심.
- 요약 : 4대 핵심 지표와 백분위수 SLO 체계를 통한 사용자 체감 성능의 계약적·공학적 관리.
- 시사점 : SMART 정량화, 탄력적 피크 설계, CI 기반 지속 성능 테스트의 병행이 성능 품질 확보의 표준 방향.
