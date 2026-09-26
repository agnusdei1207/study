---
title: "쿠버네티스(Kubernetes)"
author: "Codex"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

지식 위치: 컴퓨터 시스템 → 컨테이너 오케스트레이션 → **쿠버네티스**

## 30초 인출

- 본질: **쿠버네티스 (Kubernetes)** 는 선언한 목표 상태에 맞게 컨테이너 워크로드를 조정하는 플랫폼
- 메커니즘: API에 기록한 목표 상태와 실제 상태를 컨트롤러가 비교하고, 스케줄러·kubelet이 배치·실행 작업을 수행

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

## 1교시 예상문제 (10점)

> 쿠버네티스의 개념과 주요 구성요소, 선언형 상태 관리 방식을 설명하시오. (예상)

---

## 1교시 10점 답안

### Ⅰ. 쿠버네티스의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **쿠버네티스 (Kubernetes)** 는 컨테이너 워크로드를 선언한 목표 상태에 맞게 스케줄·실행·복구하는 컨테이너 오케스트레이션 플랫폼 |
| 목적 | 여러 노드의 애플리케이션 배포와 실행 상태 관리 |

### Ⅱ. 핵심 구성

```mermaid
flowchart TD
    API["kube-apiserver"] ---|"상태 저장·조회"| ETCD["etcd"]
    CTRL["컨트롤러"] -->|"상태 조정 요청"| API
    SCHED["스케줄러"] -->|"Pod 노드 배정"| API
    NODE["노드의 kubelet"] -->|"Pod 상태 보고"| API
    NODE -->|"할당된 Pod 실행"| POD["Pod"]
```

### Ⅲ. 선언형 관리

| 입력 | 쿠버네티스의 동작 |
|---|---|
| 목표 상태: 복제본 3개 | 컨트롤러가 현재 복제본 수와 비교 |
| 현재 상태: 2개 | 부족한 Pod를 만들고 스케줄러가 노드를 배정 |

제언: 배포 전 복제본 수·자원 요구량·장애 영역을 함께 지정해 가용성 목표와 배치 조건을 확인

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

## Ⅱ. 클러스터 구성요소와 역할

```mermaid
flowchart TD
    API["kube-apiserver"] ---|"상태 저장·조회"| ETCD["etcd"]
    CTRL["컨트롤러"] -->|"상태 조정 요청"| API
    SCHED["스케줄러"] -->|"Pod 노드 배정"| API
    NODE["노드의 kubelet"] -->|"Pod 상태 보고"| API
    NODE -->|"할당된 Pod 실행"| POD["Pod"]
```

## Ⅲ. 목표 상태를 맞추는 조정 과정

```mermaid
flowchart TD
    DESIRED["목표 상태 선언"] --> API["API에 기록"]
    API --> COMPARE["컨트롤러가 현재 상태와 비교"]
    COMPARE -->|"차이 발견"| ACTION["Pod 생성·교체 등 조정"]
    ACTION --> OBSERVE["실제 상태 관찰"]
    OBSERVE --> COMPARE
```

복제본 부족 시 조정: 컨트롤러의 Pod 생성, 스케줄러의 노드 배정, 해당 노드 kubelet의 실행.

## Ⅳ. 배포·확장·가용성의 운영 기준

| 상황 | 확인할 구성 | 판단 기준 |
|---|---|---|
| 버전 배포 | Deployment의 RollingUpdate | `maxUnavailable`·`maxSurge`와 준비 상태 |
| 부하 변화 | HPA | 관측 지표와 최소·최대 복제본 수 |
| 노드·영역 장애 | 복제본·Topology Spread Constraints | Pod가 여러 장애 영역에 분산되는지 |
| 제어 평면 복구 | etcd 백업·복원 절차 | 상태 데이터의 복구 가능 여부 |

## Ⅴ. 기술사적 제언

| 한계 | 해결 방안 |
|---|---|
| 복제본이 한 노드나 영역에 몰림 | Topology Spread Constraints와 충분한 복제본을 함께 설정하고 실제 배치를 확인 |
| 배포 중 가용 Pod가 부족해짐 | RollingUpdate 설정과 준비 상태 검사를 서비스 가용성 목표에 맞춰 검증 |

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 1교시 12번: 쿠버네티스 설명. 제137회 4교시 3번: 개념·특징, 주요 컴포넌트, HPA 설명(공식 Q-Net 문제지 대조). 아래 예상문제는 원문 문항과 구분.
- [Kubernetes 공식 문서, 클러스터 아키텍처](https://kubernetes.io/docs/concepts/architecture/)
- [Kubernetes 공식 문서, Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes 공식 문서, Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
- [Kubernetes 공식 문서, Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)

## 연결 토픽

- 연관 토픽: [컨테이너](./032_container.md), [오토스케일링](./025_auto_scaling.md)
