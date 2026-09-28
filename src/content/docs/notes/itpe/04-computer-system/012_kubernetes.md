---
title: "쿠버네티스(Kubernetes)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  label: "012. 쿠버네티스(Kubernetes)"
  order: 12
  badge:
    text: "기초"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

지식 위치: 컴퓨터 시스템 → 컨테이너 오케스트레이션 → **쿠버네티스**

## 30초 인출

- 본질: **쿠버네티스 (Kubernetes)** 는 선언한 목표 상태에 맞게 컨테이너 워크로드를 조정하는 플랫폼
- 메커니즘: API에 기록한 목표 상태와 실제 상태를 컨트롤러가 비교하고, 스케줄러·kubelet이 배치·실행 작업을 수행
- 통찰: 선언적 API와 제어 루프를 기반으로 대규모 분산 컨테이너의 배포, 스케줄링, 롤링 업데이트, 자가 치유를 자동화하는 클라우드 네이티브 플랫폼임.

<details>
<summary>핵심 용어</summary>

- **Pod** : 같은 네트워크·스토리지 자원을 공유하며 함께 배치되는 컨테이너의 최소 실행 단위
- **쿠버네티스 (Kubernetes)** : 컨테이너 워크로드의 배포와 실행을 선언한 목표 상태에 맞춰 조정하는 오케스트레이션 플랫폼.
- **API (Application Programming Interface)** : 소프트웨어 구성요소가 기능·데이터를 요청하고 응답받는 호출 규약.
- **kube-apiserver** : 클러스터 상태를 읽고 변경하는 Kubernetes API의 진입점
- **etcd** : 클러스터의 API 데이터를 저장하는 분산 키·값 저장소
- **kube-scheduler** : 아직 노드에 배정되지 않은 Pod에 적합한 노드를 선택하는 구성요소
- **kube-controller-manager** : 목표 상태와 현재 상태의 차이를 줄이는 컨트롤러를 실행하는 구성요소
- **kubelet** : 노드에서 할당된 Pod의 실행 상태를 관리하는 에이전트
- **HPA (Horizontal Pod Autoscaler)** : 관측 지표에 따라 워크로드의 Pod 복제본 수를 조정하는 Kubernetes 리소스.

</details>

---

## 2~4교시 예상문제 (25점)

> 쿠버네티스의 클러스터 구조와 선언형 상태 조정 방식을 설명하고, 배포·확장·장애 대응 시 확인할 사항을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 쿠버네티스의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **쿠버네티스 (Kubernetes)** 는 컨테이너 워크로드를 선언한 목표 상태에 맞게 스케줄·실행·복구하는 컨테이너 오케스트레이션 플랫폼 |
| 목적 | 여러 노드의 애플리케이션 배포와 실행 상태 관리 |

## Ⅱ. 선언형 상태 관리의 특징

| 특징 | 의미 |
|---|---|
| 목표 상태 선언 | 사용자가 원하는 복제본·배치·배포 조건을 API에 기록 |
| 지속적 조정 | 컨트롤러가 관찰 상태와 목표의 차이를 반복 해소 |
| 실행 책임 분리 | 스케줄러가 노드를 선택하고 kubelet이 Pod 실행 관리 |

## Ⅲ. 클러스터 구성요소와 조정 체계

```text
사용자 선언 → kube-apiserver ↔ etcd(클러스터 상태)
                    ↑                 ↑ 상태 관찰
              컨트롤러           스케줄러(노드 선택)
                    └── Pod 조정 ───→ kubelet(노드 실행)
```

목표 상태를 선언적 API에 기록하면 컨트롤러가 실제 상태와 비교해 Pod 생성 및 교체를 요청하고, 스케줄러가 노드를 배정한 뒤 kubelet이 실행. 관찰된 상태와 목표의 차이 발생 시 지속적인 피드백 조정 반복.

```text
목표 복제본 수 ≠ 준비된 Pod 수
          ↓ 컨트롤러가 부족분 생성 요청
스케줄러: 자원·제약 충족 노드 선택
          ↓ kubelet 실행·상태 보고
준비 상태 재관찰 → 목표 달성까지 반복
```

## Ⅳ. 배포·확장·가용성의 운영 방식 비교

| 상황 | 확인할 구성 | 판단 기준 |
|---|---|---|
| 버전 배포 | Deployment의 RollingUpdate | `maxUnavailable`·`maxSurge`와 준비 상태 |
| 부하 변화 | HPA | 관측 지표와 최소·최대 복제본 수 |
| 노드·영역 장애 | 복제본·Topology Spread Constraints | Pod가 여러 장애 영역에 분산되는지 |
| 제어 평면 복구 | etcd 백업·복원 절차 | 상태 데이터의 복구 가능 여부 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 복제본이 한 노드·영역에 집중 | Topology Spread Constraints와 복제본 수를 함께 설정하고 실제 배치를 확인 |
| 배포 중 가용 Pod 부족 | RollingUpdate의 `maxUnavailable`·`maxSurge`와 준비 상태를 서비스 목표에 맞게 검증 |
| 제어 평면 상태 손실 | etcd 백업·복원 절차를 시험해 상태 복구 가능성을 확인 |

## Ⅵ. 도입/구축/운영 관점 제언

### 1. 실무 적용 가이드 및 핵심 고려사항
노드 장애 시 파드 퇴거 지연을 통제하고 클러스터 연쇄 부하를 차단하기 위해 Pod 경합 방지용 리소스 Requests/Limits를 필수 지정하며 HPA와 Cluster Autoscaler를 연계 구성.

### 2. 아키텍처 및 상세 메커니즘
```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ Control Plane (마스터 노드) ]                                        │
│   - kube-apiserver   : 모든 컴포넌트의 유일한 통신 게이트웨이         │
│   - etcd             : 클러스터의 모든 상태를 저장하는 일관성 분산 KV  │
│   - kube-scheduler   : 미할당 Pod에 대해 리소스 기반 최적 노드 선별    │
│   - controller-mgr   : 원하는 상태(Desired)와 현재 상태(Actual) 동기화│
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │ (gRPC / TLS 통신)
       ┌───────────────────────────┴───────────────────────────┐
       ▼                                                       ▼
┌──────────────────────────────┐        ┌──────────────────────────────┐
│ [ Worker Node 1 ]            │        │ [ Worker Node 2 ]            │
│   - kubelet (노드 에이전트)  │        │   - kubelet (노드 에이전트)  │
│   - kube-proxy (네트워크 룰) │        │   - kube-proxy (네트워크 룰) │
│   - Container Runtime (CRI)  │        │   - Container Runtime (CRI)  │
│   ┌────────────────────────┐ │        │   ┌────────────────────────┐ │
│   │ [ Pod (App Container) ]│ │        │   │ [ Pod (App Container) ]│ │
│   └────────────────────────┘ │        │   └────────────────────────┘ │
└──────────────────────────────┘        └──────────────────────────────┘
```

### 3. 기술 유형 및 비교 평가
| 핵심 컴포넌트 | 소속 계층 | 주요 역할 및 메커니즘 | 장애 발생 시 파급 효과 |
|---|---|---|---|
| **kube-apiserver** | Control Plane | RESTful API 제공 및 인증/인가/입장 제어 | 신규 배포 및 kubectl 제어 불가 (기존 파드는 동작) |
| **etcd** | Control Plane | 클러스터 메타데이터의 Raft 합의 분산 저장 | 데이터 유실 시 클러스터 복구 불가능 (다중화 필수) |
| **kube-scheduler** | Control Plane | 노드 필터링(Predicates) 및 점수(Priorities) 평가 | 신규 Pod가 배정되지 못하고 Pending 상태 지속 |
| **kubelet** | Worker Node | PodSpec을 전달받아 CRI 컨테이너 기동 및 헬스체크 | 해당 워커 노드가 NotReady 상태로 전이, 파드 재배정 |
| **kube-proxy** | Worker Node | iptables/IPVS 기반 서비스 가상 IP 라우팅 | 서비스 엔드포인트 트래픽 분산 실패 |

## 출제 이력과 검증 출처

- CNCF Kubernetes Core Documentation & Architecture Whitepaper
- Brendan Burns et al. - Kubernetes: Up and Running (O'Reilly)
- Google Cloud Architecture Center: Enterprise Kubernetes Best Practices

## 연결 토픽

- 상위 토픽: [032 컨테이너](./032_container.md)
- 연관 토픽: [064 HPA](./064_hpa.md), [003 서버리스 컴퓨팅](./003_serverless_computing.md)
