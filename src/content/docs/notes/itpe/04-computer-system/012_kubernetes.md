---
title: "쿠버네티스(Kubernetes)"
author: "Codex"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  label: "012. 쿠버네티스(Kubernetes)"
  order: 12
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
- 통찰: 한계: 복제본을 늘려도 같은 장애 영역에 몰릴 수 있음 → 방안: 배포 전 자원 요구량과 장애 영역 분산 조건을 함께 검증

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

목표 상태를 API에 기록하면 컨트롤러가 실제 상태와 비교해 Pod 생성·교체를 요청하고, 스케줄러가 노드를 배정한 뒤 kubelet이 실행한다. 관찰된 상태와 목표의 차이가 남으면 조정을 반복한다.

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

## Ⅵ. 제언

복제본이 같은 장애 영역에 몰리면 함께 중단될 수 있으므로 서비스 한 개에서 영역별 Pod 배치와 배포 중 최소 가용 수를 확인한 뒤 정책을 확대한다.

## 출제 이력과 검증 출처

- 제133회 정보관리기술사 1교시 12번: 쿠버네티스 설명. 제137회 4교시 3번: 개념·특징, 주요 컴포넌트, HPA 설명(공식 Q-Net 문제지 대조). 아래 예상문제는 원문 문항과 구분.
- [Kubernetes 공식 문서, 클러스터 아키텍처](https://kubernetes.io/docs/concepts/architecture/)
- [Kubernetes 공식 문서, Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes 공식 문서, Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
- [Kubernetes 공식 문서, Pod Topology Spread Constraints](https://kubernetes.io/docs/concepts/scheduling-eviction/topology-spread-constraints/)

## 연결 토픽

- 연관 토픽: [컨테이너](./032_container.md), [오토스케일링](./025_auto_scaling.md)
