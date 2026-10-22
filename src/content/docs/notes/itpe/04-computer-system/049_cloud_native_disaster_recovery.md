---
title: "클라우드 네이티브 재해복구"
author: "agnusdei1207"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 클라우드 네이티브 재해복구의 개요

- 핵심 요약 : **클라우드 네이티브 DR**은 IaC·GitOps·크로스 리전 복제로 RTO 분 단위·RPO 제로를 달성하는 차세대 재해복구.
- 개념 : 지진, 화재 등 물리적 데이터센터 재난 및 **클라우드 CSP(Cloud Service Provider) 리전(Region)** 전면 장애 발생 시, 클라우드 네이티브 기술(컨테이너, 마이크로서비스, IaC(Infrastructure as Code) 선언적 인프라, GitOps)을 활용하여 원격지에 온디맨드로 인프라를 신속히 재현하고 비즈니스 연속성을 수호하는 차세대 재해복구(DR, Disaster Recovery) 아키텍처.
- 배경 및 필요성 : 전통적인 온프레미스 DR 센터의 막대한 유휴 하드웨어 비용(막대한 비용), 느린 수동 복구 속도(수 시간~수일), 그리고 **환경 구성 불일치(Drift)** 문제를 해결하기 위해 클라우드의 탄력성과 코드형 인프라를 결합함.
- 핵심 목적 : **목표 복구 시간(RTO, Recovery Time Objective)** 분 단위 단축, **목표 복구 시점(RPO, Recovery Point Objective)** 제로(Zero)화, 인프라 상시 대기 비용을 극소화하는 Pilot Light / Warm Standby 최적화 달성.

## Ⅱ. 클라우드 네이티브 재해복구의 특징 및 장점

- 핵심 요약 : **GitOps 선언적 재현·글로벌 DB 복제·동적 오토스케일링·GSLB 자동 컷오버**.
1. **GitOps 기반 선언적 재현 (Infrastructure as Code)** : 인프라(Terraform)와 K8s 매니페스트(ArgoCD)를 단일 Git 리포지토리에 보관하여 명령어 하나로 원격 리전에 동일 환경 즉시 구축.
2. **글로벌 분산 데이터베이스 복제** : Aurora Global Database, DynamoDB Global Tables 등을 활용하여 1초 미만의 지연으로 스토리지 계층을 원격 리전에 상시 동기화.
3. **동적 오토스케일링 확장** : 평상시 DR 리전은 최소 파드와 최소 노드만 유지(Pilot Light)하다가, 페일오버 감지 시 Karpenter 및 HPA(Horizontal Pod Autoscaler)로 수 분 내에 100% 용량으로 스케일아웃.
4. **GSLB 자동 헬스체크 및 컷오버** : 주 리전 엔드포인트 무응답 시 DNS(Domain Name System) TTL(Time to Live) 만료와 동시에 전 세계 사용자 트래픽을 DR 리전 게이트웨이로 자동 재라우팅.

## Ⅲ. 클라우드 네이티브 재해복구의 구조 및 동작 메커니즘

- 핵심 요약 : **GSLB → 주/DR 리전 → GitOps → Aurora Global DB**.
- 클라우드 네이티브 DR은 GitOps 기반의 선언적 인프라/애플리케이션 배포 파이프라인, 스토리지 크로스 리전 비동기 복제, 그리고 글로벌 GSLB(Global Server Load Balancing) 트래픽 스위칭 메커니즘으로 동작함.

```text
[ 클라우드 네이티브 크로스 리전 DR 아키텍처 ]

[글로벌 사용자 트래픽]
           │
           ▼
+---------------------------------------------------------------+
| Global Traffic Management (Anycast DNS / AWS Route 53 / GSLB)  |
|   - 실시간 주 리전 헬스체크 실패 시 60초 내 DR 리전으로 자동 전환|
+---------------------------------------------------------------+
           │                                           │
           ▼ (정상 시: 100% 트래픽)                   │ (장애 시: Failover)
+---------------------------+                          ▼
| 주 리전 (Primary Region)  |               +---------------------------+
|                           |               | DR 리전 (Secondary Region)|
| +-----------------------+ |  GitOps Sync  | +-----------------------+ |
| | EKS / K8s Cluster     | | <───────────> | | EKS Cluster (최소 노드) | |
| | (Production Scale)    | |  (Terraform / | | (장애 시 Karpenter 확장)| |
| +-----------------------+ |    ArgoCD)    | +-----------------------+ |
|             │             |               |             ▲             |
|             ▼             |               |             │             |
| +-----------------------+ |  Cross-Region | +-----------------------+ |
| | Aurora Global DB      | | ────────────> | | Aurora Global DB      | |
| | (Read / Write)        | |  Replication  | | (Read-Only Replica)   | |
| +-----------------------+ | (Latency < 1s)| +-----------------------+ |
+---------------------------+               +---------------------------+
```

## Ⅳ. 클라우드 네이티브 재해복구의 비교

- 핵심 요약 : **Backup & Restore·Pilot Light·Warm Standby·Active-Active** RTO/RPO/비용 비교.

| 클라우드 DR 전략 | 아키텍처 구성 및 특징 | 복구 시간 (RTO) | 데이터 손실 (RPO) | 평상시 인프라 비용 |
|---|---|---|---|---|
| Backup & Restore | 정기 스냅샷을 원격 S3에 보관, 재난 시 신규 프로비저닝 | 수 시간 ~ 수일 | 수 시간 (백업 주기) | 최저 (스토리지 비용만) |
| Pilot Light | 핵심 DB만 원격 복제 유지, 컴퓨팅은 장애 시 자동 생성 | 수십 분 이내 | 수 초 ~ 수 분 | 낮음 (DB 인스턴스만) |
| Warm Standby | 축소된 규모의 컴퓨팅/앱이 상시 가동 대기 | 수 분 이내 | 수 초 이하 | 중간 (상시 축소 클러스터) |
| Active-Active | 두 리전 모두 100% 트래픽 분산 처리 및 양방향 동기화 | 0초 (무중단 즉시) | 0초 (Zero RPO) | 최고 (완전 이중화 비용) |

- 클라우드 네이티브 DR은 과거 온프레미스의 All-or-Nothing 방식과 달리, 워크로드의 중요도에 따라 Pilot Light와 Warm Standby를 정밀하게 조합하여 비용 대비 가용성을 극대화함.

## Ⅴ. 클라우드 네이티브 재해복구의 한계와 방안

- 핵심 요약 : **용량 부족·스플릿 브레인·DNS 캐싱**을 ODCR·쿼럼·Anycast로 대응.

- 리전 장애 시 타 리전의 인스턴스 **용량 부족(Capacity Stockout)** :
  - 한계점 : 주 리전 대규모 정전 시 모든 기업이 동시에 보조 리전으로 몰려 해당 리전의 특정 GPU(Graphics Processing Unit)/인스턴스 타입 품절 발생.
  - 해결 방안 : DR 리전에 온디맨드 용량 예약(ODCR: On-Demand Capacity Reservation) 사전 확보, 이종 인스턴스 패밀리 유연 배포 설정.
- 데이터베이스 페일오버 시 스플릿 브레인 및 데이터 분기 :
  - 한계점 : 일시적 네트워크 단절을 리전 재난으로 오판하여 보조 리전 DB를 Master로 승격시킬 경우 양쪽 DB 데이터 분기(Split-brain) 발생.
  - 해결 방안 : 스토리지 레벨의 쿼럼 기반 마스터 승격 검증, 사가 패턴 및 보상 트랜잭션 정합성 복구 파이프라인 수립.
- **DNS** 캐싱으로 인한 엔드포인트 전환 지연 :
  - 한계점 : 글로벌 ISP(Internet Service Provider) 및 클라이언트 브라우저가 DNS 응답을 임의로 오래 캐싱하여 GSLB 레코드 변경 후에도 구 리전으로 트래픽 유입.
  - 해결 방안 : DNS TTL을 10~30초로 극도로 낮추고, Anycast 고정 IP(Internet Protocol) 기반의 AWS(Amazon Web Services) Global Accelerator 또는 Cloudflare 전환.

## Ⅵ. 클라우드 네이티브 재해복구 적용 제언

- 핵심 요약 : **카오스 게임데이·DR 티어링·스테이트리스**.
- 카오스 게임데이(Chaos GameDay) 정기 훈련 의무화 : 예고 없는 주 리전 강제 격리 훈련.
- FinOps 관점 DR 티어링(Tiering) 거버넌스 : Tier-1/2/3 차등화.
- 스테이트리스(Stateless) 컨테이너화 철저 준수 : 12-Factor 원칙.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 네이티브 DR은 **IaC·GitOps·크로스 리전 복제**로 RTO/RPO를 최적화하나 용량 부족·스플릿 브레인·DNS 캐싱 리스크 관리가 필수.
- 클라우드 네이티브 DR은 GitOps·크로스 리전 복제·GSLB로 RTO 분 단위/RPO 제로를 달성하지만, 용량 부족·스플릿 브레인·DNS 캐싱 리스크를 ODCR·쿼럼·Anycast로 관리해야 함.
- 답안에는 DR 4전략 비교, 한계·대응, 카오스 게임데이·티어링·스테이트리스 제언을 연결.