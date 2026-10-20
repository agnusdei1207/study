---
title: "고가용성 아키텍처(HA, High Availability)"
author: "agnusdei1207"
date: "2026-03-30T09:00:00+09:00"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Antigravity Professional Engine"
---

## 연관 키워드

- 고가용성(HA, High Availability), 이중화, 페일오버(Failover), 하트비트(Heartbeat), 스플릿 브레인(Split-Brain)
- 쿼럼(Quorum), 펜싱(Fencing, STONITH), MTBF·MTTR, RPO·RTO, 로드밸런서(Load Balancer), Multi-AZ, 재해복구(DR, Disaster Recovery)

## Ⅰ. 고가용성 아키텍처의 개요

- 핵심 요약 : 하드웨어·소프트웨어 장애 상황에서도 무중단 서비스를 지속하는 이중화 및 장애 복구 체계.
- 개념 : 고가용성(HA, High Availability)은 시스템·네트워크·애플리케이션·데이터베이스에 하드웨어 결함이나 소프트웨어 장애가 발생하더라도 정상적인 서비스 제공 상태를 지속 유지하도록 이중화 및 장애 복구 체계를 갖춘 아키텍처.
- 배경 및 필요성 :
  1. 무중단 비즈니스 요구 : 서비스 중단이 매출과 신뢰도 손실로 직결되는 환경의 확대.
  2. 단일 장애점(SPOF, Single Point of Failure) 제거와 자동 장애 조치 체계의 필요.
  3. 'Five Nines'(99.999%, 연간 장애 시간 5.26분 이내) 수준 가용성 목표의 대두.
- 주요 목적 : 장애 감지부터 자동 페일오버(Failover)까지의 가용성 확보 및 데이터 정합성 유지.

## Ⅱ. 고가용성 아키텍처의 특징

- 핵심 요약 : 이중화 토폴로지와 하트비트 감지, 쿼럼·펜싱 방어, RPO·RTO 관리의 조합 체계.

1. 이중화 구성 : Active-Standby 또는 Active-Active 토폴로지 기반의 결함 내성 확보.
2. 정량 평가 지표 : MTBF(Mean Time Between Failures)와 MTTR(Mean Time To Repair) 기반의 가용도 공식 적용.
3. 자동 장애 감지 : 노드 간 전용 네트워크 링크를 통한 하트비트(Heartbeat) 신호의 주기적 교환.
4. 스플릿 브레인 방어 : 쿼럼(Quorum, 과반수 합의) 투표와 펜싱(Fencing) 메커니즘의 적용.
5. 복구 목표 관리 : RPO(Recovery Point Objective)와 RTO(Recovery Time Objective)의 사전 정의 및 검증.

```text
[ HA 핵심 평가 공식 ]
                MTBF (평균 무고장 시간)
  가용도 (A) = -----------------------------
               MTBF + MTTR (평균 수리 복구 시간)
  * MTBF : 시스템이 정상 작동한 평균 시간 (극대화 필요)
  * MTTR : 장애 발생 후 정상 복구까지 소요 시간 (극소화 필요)
```

## Ⅲ. 고가용성 아키텍처의 구조 (흐름)

- 핵심 요약 : 클러스터 구성 모델과 장애 감지·페일오버 흐름, RPO·RTO 타임라인의 통합 구조.

```text
[ HA 클러스터 구성 모델 ]
(A) Active-Standby
 [Active Node] ===(Heartbeat / Data Sync)===> [Standby Node]
 (정상 시 전체 트래픽 처리)                   (장애 시 페일오버 대기)

(B) Active-Active
 [Active Node 1] <--- [L4/L7(OSI Layer 4/7) Load Balancer] ---> [Active Node 2]
 (양 노드 동시 서비스 처리, 상호 백업)
```

```text
[ 재해 복구 타임라인 (RPO / RTO) ]
 ---[정상 운영]---> [재해 발생] ---[복구 작업]---> [서비스 정상화]
                        |<------- RTO ------->|   (복구 소요 시간)
          |<--- RPO --->|                         (데이터 유실 허용 시점)
```

- 장애 감지 및 페일오버 흐름 :
  1. 하트비트 단절 또는 헬스체크 임계치 초과에 따른 장애 판정.
  2. 쿼럼 투표 기반의 신규 Active 노드 승격.
  3. 펜싱(STONITH, Shoot The Other Node In The Head)을 통한 구 노드 격리.
  4. DNS(Domain Name System)·VIP(Virtual IP) 스위칭에 따른 트래픽 전환.

## Ⅳ. HA 구성 모델 및 RPO·RTO의 비교

- 핵심 요약 : RTO·비용·자원 효율의 트레이드오프에 따른 구성 모델 선택과 RPO·RTO의 역할 구분.

| 구성 모델 | 동작 메커니즘 | 장점 | 트레이드오프 및 한계 |
|---|---|---|---|
| Active-Hot Standby | Standby 노드가 가동 상태로 데이터 실시간 동기화하며 대기 | 페일오버 시간(RTO) 수초 이내 | Standby 노드 자원의 유휴 방치로 인한 비용 비효율 |
| Active-Active | 복수 노드가 트래픽 분산 처리, 서로의 예비 노드 역할 수행 | 자원 활용률 극대화, 전체 처리량(Throughput) 증대 | 노드 간 동기화 오버헤드, 한 노드 장애 시 잔여 노드 부하 급증 |
| Active-Warm Standby | Standby 노드 가동, 애플리케이션은 비활성 상태 | Hot 대비 인프라 비용 절감 | 앱 기동·캐시 로딩에 따른 수분 수준의 RTO 소요 |

| 구분 | RPO (Recovery Point Objective) | RTO (Recovery Time Objective) |
|---|---|---|
| 정의 | 장애 시 감내 가능한 최대 데이터 손실 시점(데이터 유실량) | 서비스 중단부터 정상 복구까지의 최대 허용 중단 시간 |
| 측정 대상 | 데이터 유실 허용치 | 서비스 중단 시간 |
| 관리 수단 | 동기식 복제, 로그 전송 주기 단축 | 자동 페일오버, 헬스체크 임계치 튜닝 |

- 선택 기준 :
  1. RTO 수초 수준 요구 : Active-Hot Standby.
  2. 자원 효율과 처리량 우선 : Active-Active.
  3. 비용 최소화 및 수분 수준 중단 허용 : Active-Warm Standby.

## Ⅴ. 고가용성 아키텍처의 장점과 한계

- 핵심 요약 : 무중단 서비스와 자동 복구의 장점, 스플릿 브레인·복구 지연·자원 유휴화의 한계.

- 장점
  1. 하드웨어·소프트웨어 결함에도 지속되는 무중단 서비스 연속성.
  2. 하트비트 기반 자동 페일오버에 따른 복구 시간 단축.
  3. Five Nines 수준 가용성 목표의 정량 관리 가능.

- 한계점 1 : 스플릿 브레인(Split-Brain)에 따른 데이터 정합성 파괴
  - 한계점 : 클러스터 노드 간 하트비트 네트워크 단절 시 양측 모두 활성(Active) 마스터로 승격, 상이한 쓰기 수행으로 데이터 분기 및 손실 발생.
  - 해결 방안 : 홀수 노드 구성의 쿼럼(과반수 합의) 메커니즘 필수 적용, 펜싱(STONITH) 하드웨어 차단 장치 연동.
- 한계점 2 : 페일오버 시점의 RPO·RTO 지연 및 세션 유실
  - 한계점 : 비동기 복제 환경에서 미복제 트랜잭션 유실(RPO > 0), 헬스체크 판정 및 승격 시간 동안의 서비스 중단(RTO 지연) 발생.
  - 해결 방안 : 동기식 복제(Sync Replication) 또는 Raft 기반 합의 엔진 적용, 자동 DNS·VIP 스위칭 및 클라이언트 자동 재연결(Reconnection) 풀 구성.
- 한계점 3 : Active-Standby 자원 유휴화 및 클라우드 비용 낭비
  - 한계점 : 정상 운영 시 스탠바이 서버의 트래픽 미처리 대기로 인한 인프라 비용 효율성 저하.
  - 해결 방안 : Active-Active 멀티 리전 아키텍처 전환, 읽기 전용 쿼리 분산용 세컨더리 복제본(Read Replica) 활용.

## Ⅵ. 고가용성 아키텍처에 대한 기술사적 제언

- 핵심 요약 : 다중 가용영역 액티브-액티브 배포와 카오스 엔지니어링 기반의 상시 검증 체계.
- 다중 가용영역(Multi-AZ, Availability Zone) 배포 : 3개 이상 가용영역에 상태 비저장(Stateless) 웹·앱 컨테이너 분산 배치, DB(Database)의 Multi-AZ 자동 동기식 복제 적용.
- 카오스 엔지니어링(Chaos Engineering) 상시화 : Chaos Mesh, Chaos Monkey 도입을 통한 운영 환경 무작위 인스턴스 강제 종료 테스트의 정례화.
- 가용성 지표 상시 관리 : MTBF 극대화·MTTR 극소화 지표의 대시보드 모니터링 및 재해복구(DR) 연계 훈련의 정례화.

## Ⅶ. 결론

- 핵심 요약 : HA는 가용도 공식 기반의 정량 관리와 이중화·합의 메커니즘의 결합으로 완성.
- 요약 : Active-Standby·Active-Active 토폴로지, 하트비트 감지, 쿼럼·펜싱 방어, RPO·RTO 관리의 통합 체계.
- 시사점 : 클라우드 네이티브 환경의 Multi-AZ 설계와 카오스 테스트 기반의 상시 검증 필요.
