---
sidebar:
  order: 158
  label: "158. Kubernetes (쿠버네티스)"
  badge:
    text: "기출 · 80%"
    variant: note
title: "Kubernetes (쿠버네티스)"
date: "2026-09-15T11:20:00+09:00"
tags:
  - "notes-latest_tech"
weight: 158
extra:
  question_no: "158"
  source_status: "기출"
  source_history: "135회, 137회"
  priority: 80
  priority_note: "쿠버네티스 제어 루프•스케줄링이 반복 출제됨"
---

## Ⅰ. 개요

- **정의**: 컨테이너화된 대규모 분산 애플리케이션의 배포, 스케줄링, 서비스 디스커버리, 탄력적 자동 확장 및 자가 치유(Self-Healing)를 자동화하는 클라우드 네이티브 기반 오픈소스 컨테이너 오케스트레이션 플랫폼
- **배경 및 필요성**: 마이크로서비스 아키텍처(MSA) 확산으로 수천~수만 개의 분산 컨테이너 인스턴스가 동적으로 증감하는 환경에서, 수동 호스트 관리는 서버 장애 시 컨테이너 재배치 지연, 동적 IP 변경에 따른 서비스 단절, 자원 불균형 문제를 유발하므로, 선언적 명세(YAML)와 제어 루프(Reconciliation Loop)를 통해 목표 상태(Desired State)를 클러스터에 상시 자동 수렴시킬 필요성 대두

## Ⅱ. 특징

- **선언적 상태 관리**: 사용자가 원하는 목표 상태를 YAML로 기술하면 컨트롤러가 실제 상태(Actual State)를 지속적으로 감시 및 일치시킴
- **자가 치유(Self-Healing)**: 컨테이너 장애 시 자동 재기동, 노드 고장 시 타 정상 노드로 파드 재스케줄링, 비정상 인스턴스 서비스 제외 자동화
- **서비스 디스커버리 및 로드밸런싱**: 고유 DNS 이름과 단일 IP(ClusterIP)를 부여하여 컨테이너 IP 변경과 무관하게 안정적인 L4/L7 트래픽 분산 제공
- **표준 플러그인 생태계**: CRI(컨테이너 런타임), CNI(네트워크), CSI(스토리지) 표준 인터페이스를 통해 다양한 벤더 기술 유연하게 통합

## Ⅲ. 구조 및 구성요소

```text
[Kubernetes 아키텍처]
├── [Control Plane (마스터)] ── kube-apiserver, etcd, kube-scheduler, kube-controller-manager
├── [Worker Node (워커)] ────── kubelet, kube-proxy, Container Runtime (CRI)
├── [표준 인터페이스] ──────── CNI (Container Network), CSI (Container Storage)
└── [워크로드 리소스] ──────── Pod, Deployment, StatefulSet, DaemonSet, Service, Ingress
```

- 선들의 의미: 실선(──)과 가지선(├──, └──)은 계층적 하위 관계를 의미함

| 구성요소 | 설명 | 주요 역할 |
|:---|:---|:---|
| kube-apiserver | 제어면의 중앙 REST 통신 게이트웨이 | 모든 객체 요청에 대한 인증·인가, 유효성 검증 및 etcd 연계 |
| etcd | 고가용성 분산 키-값 저장소 | 클러스터의 모든 상태 정보, 메타데이터, 선언 명세 영속 저장 |
| kube-scheduler | 파드 스케줄링 엔진 | 노드의 가용 자원, 제약 조건, 어피니티를 분석하여 파드-노드 바인딩 결정 |
| kube-controller-manager | 제어 루프 데몬 프로세스 집합 | Node, ReplicaSet, Deployment 등 컨트롤러를 실행하여 목표 상태 유지 |
| kubelet | 워커 노드의 핵심 상주 에이전트 | CRI를 통해 컨테이너 생명주기 관리 및 주기적 상태를 API 서버에 보고 |
| kube-proxy | 노드별 가상 네트워크 프록시 | iptables 또는 IPVS 규칙을 조작하여 Service IP 트래픽을 파드로 부하분산 |

## Ⅳ. 흐름도

```text
[선언적 매니페스트 수신] (① kubectl 또는 GitOps를 통해 배포 YAML 제출)
│
▼
[API 서버 검증 및 저장] (② kube-apiserver가 요청 인증·인가 후 분산 저장소 etcd에 상태 기록)
│
▼
[컨트롤러 상태 조정] (③ Controller Manager가 Desired State와 Actual State 간 불일치 감지)
│
▼
[스케줄러 노드 바인딩] (④ kube-scheduler가 노드 가용 자원 및 라벨을 분석하여 최적 노드 할당)
│
▼
[Kubelet 컨테이너 기동] (⑤ 할당된 노드의 kubelet이 CRI를 호출하여 컨테이너 기동 및 CNI 설정)
│
▼
[상태 보고 및 서비스 등록] (⑥ 헬스체크(Readiness/Liveness) 통과 후 Service 엔드포인트 트래픽 유입)
```

- 분기 결과: 파드 비정상 종료 시 kubelet이 자동 재기동, 노드 장애 지속 시 컨트롤러가 타 노드로 파드 축출 및 재스케줄링 수행

## Ⅴ. 종류 및 비교

| 구분 | Deployment | StatefulSet | DaemonSet |
|:---|:---|:---|:---|
| 주 대상 워크로드 | 무상태(Stateless) 웹 및 API 서버 | 데이터베이스 등 상태 저장(Stateful) 서비스 | 로깅, 모니터링, 네트워킹 등 노드 인프라 데몬 |
| 파드 식별자 | 임의의 해시 문자열 (교체 가능) | 순차적 고정 인덱스 (예: pod-0, pod-1) | 노드 이름 기반 또는 독립 인스턴스 |
| 스토리지 바인딩 | 공유 스토리지 또는 임시 스토리지 | VolumeClaimTemplate 기반 개별 전용 영속 볼륨 | 호스트 경로(hostPath) 또는 노드 로컬 스토리지 |
| 스케일링 특성 | 무순서 병렬 스케일 인/아웃 | 지정된 순서대로 순차 생성 및 역순 삭제 | 클러스터 노드 추가/제거 시 노드당 1개씩 자동 동기화 |

## Ⅵ. 실무 고려사항 및 대책

| 문제점 | 대책 | 효과 |
|:---|:---|:---|
| 기동 중인 파드로의 조기 트래픽 유입 장애 | Readiness Probe 및 Liveness Probe 임계치 정밀 설정 | 애플리케이션 초기화 완료 전 트래픽 차단 및 오류 방지 |
| 리소스 미지정으로 인한 단일 노드 OOM 발생 | 컨테이너별 Resources Request 및 Limit 명시 (LimitRange 강제) | 노드 간 균등 스케줄링 보장 및 인접 파드 자원 고갈 방지 |
| 노드 점검 및 배포 시 무중단 서비스 단절 | PodDisruptionBudget(PDB) 설정 및 다중 가용영역(AZ) 분산 | 예기치 않은 파드 동시 종료 방지 및 무중단 고가용성 유지 |

## Ⅶ. 결론

- **기술 위상/발전**: 클라우드 네이티브 컴퓨팅(CNCF) 생태계의 절대적 사실상 표준(De facto Standard) 인프라 OS로 안착하였으며 최근에는 vLLM/KServe 기반의 AI 추론 서빙 및 Kueue, Volcano를 통한 대규모 GPU 분산 학습 오케스트레이션의 핵심 기반으로 진화 중
- **실무 적용/통제**: 무상태 워크로드는 Deployment로, 상태성 DB는 StatefulSet 및 전문 Operator 패턴으로 격리 배포하며, ArgoCD 기반의 선언적 GitOps 파이프라인과 엄격한 RBAC/네트워크 정책을 결합한 통합 운영체계 구축 필수
