---
title: "오토스케일링(Auto Scaling)"
author: "Codex"
date: "2026-09-24T20:54:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  label: "025. 오토스케일링(Auto Scaling)"
  order: 25
  badge:
    text: "기초"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
---

## 지식 로드맵 내 현재 위치

지식 위치: 컴퓨터 시스템 → 클라우드 자원 운영 → **오토스케일링**

## 30초 인출

- 본질: **오토스케일링 (Auto Scaling)** 은 관측한 부하와 정책에 따라 실행 자원의 수나 크기를 자동 조정하는 기능
- 메커니즘: 부하 지표 관측 → 목표·한도 비교 → 자원 조정 → 실제 서비스 상태 확인
- 통찰: 한계: 복제본 증가가 즉시 처리 용량을 높이지 않음 → 방안: 기동·준비 시간과 후단 한도를 함께 고려해 확장 기준 설정

<details>
<summary>핵심 용어</summary>

- **오토스케일링 (Auto Scaling)** : 관측 지표와 정책에 따라 실행 자원의 수나 크기를 자동 조정하는 기능.
- **HPA (Horizontal Pod Autoscaler)** : 관측 지표에 따라 Kubernetes 워크로드의 Pod 복제본 수를 조정하는 컨트롤러.
- **VPA (Vertical Pod Autoscaler)** : 사용량을 분석해 Pod 자원 요청·제한 값을 권고하거나 설정에 따라 적용하는 추가 구성요소.
- **KEDA (Kubernetes Event-Driven Autoscaling)** : 이벤트 원천을 트리거로 Kubernetes 워크로드를 확장하는 도구.
- **Pod** : 하나 이상의 컨테이너를 함께 배치·관리하는 Kubernetes 실행 단위.
- **CPU (Central Processing Unit)** : 프로그램 명령을 실행하는 중앙 처리 장치.
- **수평 확장** : 실행 인스턴스나 Pod의 수를 늘리는 방식
- **수직 확장** : 실행 단위에 할당한 CPU·메모리 등 자원 크기를 늘리는 방식
- **안정화 기간** : 지표 변동에 따라 확장·축소가 반복되지 않도록 최근 계산 결과를 고려하는 시간 범위

</details>

---

## 2~4교시 예상문제 (25점)

> 오토스케일링의 피드백 과정을 설명하고 HPA·VPA·이벤트 기반 확장의 차이, 확장 지연과 반복 증감에 대한 대응을 제시하시오. (예상)

---

## 2~4교시 25점 답안

## Ⅰ. 오토스케일링의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **오토스케일링 (Auto Scaling)** 은 관측한 부하와 정책에 따라 실행 자원의 수나 크기를 자동 조정하는 기능 |
| 목적 | 수요 변동에 맞는 처리 용량 확보와 과잉 자원 할당 억제 |

## Ⅱ. 오토스케일링의 특징

| 특징 | 의미 |
|---|---|
| 지표 기반 피드백 | 부하·지연 등을 목표와 비교해 자원 조정 |
| 지연된 효과 | 판정 뒤 기동·준비까지 처리 용량 증가에 시간 필요 |
| 후단 의존 | 복제본 수보다 DB·큐·외부 API 한도가 실제 상한 |

## Ⅲ. 관측·조정·검증의 피드백

```text
지표 수집 → 목표·최소/최대 한도 비교 → 확장·축소 결정
  ↑                                  │
  └── 서비스 지연·후단 포화 확인 ← 준비 상태 확인
```

복제본 수 증가 뒤 이미지 준비·기동·준비 상태 확인까지 필요한 시간. 실제 처리 용량의 증가는 이 절차 완료 후 발생.

```text
부하 급증 → 확장 결정 → 이미지 준비·기동 → 준비 완료
                │                             ↓
                └─ 그 사이 큐 증가 가능 ← 실제 용량 증가
후단 포화 시 → 복제본 추가 중단·대기열/요청 속도 조정
```

## Ⅳ. 확장 대상과 신호의 차이

| 방식 | 바뀌는 것 | 적합한 신호·주의점 |
|---|---|---|
| **HPA (Horizontal Pod Autoscaler)** | Pod 복제본 수 | **CPU (Central Processing Unit)** ·메모리·사용자 지정 지표, 최소·최대 복제본 |
| **VPA (Vertical Pod Autoscaler)** | Pod 자원 요청·제한 | 사용량 기반 권고, 적용 방식에 따른 재생성 가능성 |
| **KEDA (Kubernetes Event-Driven Autoscaling)** | 외부 사건에 따른 복제본 수 | 큐 길이 등 사건 원천, HPA와의 연계 확인 |

**HPA (Horizontal Pod Autoscaler)** 와 **VPA (Vertical Pod Autoscaler)** 의 조정 대상 차이. **KEDA (Kubernetes Event-Driven Autoscaling)** 는 필수 구성요소가 아니라 사건 기반 부하에 맞는 선택지.

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 지표 수집·판정·기동·준비로 확장 지연 | 전체 준비 시간을 측정하고 예측 가능한 이벤트는 사전 확장 |
| 부하 진동에 따른 반복 증감 | 안정화 기간과 증감 속도를 조정 |
| 데이터베이스·큐·외부 API의 후단 병목 | 애플리케이션 전체 처리 한도를 확인해 복제본 상한 결정 |

CPU 사용률만으로 대기 요청·큐 길이를 파악하기 어려운 한계. 실제 서비스 지연과 연관된 지표 선택.

## Ⅵ. 제언

복제본 증가는 기동 지연과 후단 한도 때문에 즉시 용량을 높이지 못하므로 변동이 큰 워크로드 한 개에서 준비 시간·후단 용량을 측정해 확장 기준을 정한다.

## 출제 이력과 검증 출처

- 기존 노트의 제121회·제131회 문항 원문 미확인으로 예상문제 표기
- [Kubernetes 공식 문서, Autoscaling Workloads](https://kubernetes.io/docs/concepts/workloads/autoscaling/)
- [Kubernetes 공식 문서, Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)
- [Kubernetes 공식 문서, Vertical Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)
- [KEDA 공식 문서](https://keda.sh/docs/)

## 연결 토픽

- 연관 토픽: [쿠버네티스](./012_kubernetes.md), [클라우드 컴퓨팅](./013_cloud_computing.md)
