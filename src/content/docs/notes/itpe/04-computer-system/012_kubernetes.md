---
title: "쿠버네티스(Kubernetes)"
author: "agnusdei1207"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 쿠버네티스(Kubernetes)의 개요

- 핵심 요약 : **쿠버네티스**는 컨테이너 애플리케이션의 자동 배포·스케일링·자가 치유를 제공하는 클라우드 네이티브 오케스트레이션 플랫폼.
- 개념 : 컨테이너화된 애플리케이션의 대규모 자동 배포, 스케일링, 서비스 디스커버리 및 무중단 운영 관리를 **선언적(Declarative)** 구성 방식으로 제공하는 클라우드 네이티브 표준 컨테이너 오케스트레이션 플랫폼.
- 배경 및 필요성 : 마이크로서비스 아키텍처(MSA, Microservice Architecture) 확산으로 관리해야 할 컨테이너 인스턴스가 수만 개로 급증하면서, 수동 배포의 한계와 장애 복구 자동화, 하드웨어 자원 집약도 향상을 위해 구글 Borg 프로젝트의 경험을 바탕으로 탄생함.
- 핵심 목적 : 선언적 API(Application Programming Interface)와 **자가 치유** (Self-healing)를 통한 고가용성 보장, 인프라 추상화를 통한 멀티/하이브리드 클라우드 이식성 확보, 리소스 활용률 극대화.

## Ⅱ. 쿠버네티스(Kubernetes)의 특징 및 장점

- 핵심 요약 : **선언적 구성·자가 치유·인프라 추상화**로 대규모 컨테이너 운영 자동화.
1. **선언적 구성** : Desired State를 선언하면 컨트롤 플레인이 자동으로 Current State로 수렴.
2. **자가 치유(Self-healing)** : 파드 장애 시 자동 재시작·재스케줄.
3. **서비스 디스커버리** : ClusterIP/Ingress로 동적 파드 IP 추상화.
4. **수평 확장** : HPA/VPA로 메트릭 기반 자동 스케일링.
5. **인프라 추상화** : 멀티/하이브리드 클라우드 이식성.

## Ⅲ. 쿠버네티스(Kubernetes)의 구조 및 동작 메커니즘

- 핵심 요약 : **컨트롤 플레인(etcd/apiserver/scheduler/controller) + 워커 노드(kubelet/proxy/runtime)**.
- 쿠버네티스는 클러스터 전체 상태를 관리하는 **컨트롤 플레인** (Control Plane)과 실제 워크로드가 실행되는 **워커 노드** (Worker Node)로 구성되며, '선언된 의도(Desired State)'와 '실제 상태(Current State)'를 지속적으로 일치시키는 **Reconcile Loop**로 동작함.

```text
[ 쿠버네티스 클러스터 아키텍처 ]

+---------------------------------------------------------------+
| Control Plane (마스터 노드)                                    |
|                                                               |
|  +------------------+     +------------------+                |
|  | kube-apiserver   | <── | etcd (분산 KV)   |                |
|  +------------------+     +------------------+                |
|           │                         │                         |
|           ▼                         ▼                         |
|  +------------------+     +------------------+                |
|  | kube-scheduler   |     | kube-controller- |                |
|  +------------------+     | manager          |                |
|                           +------------------+                |
+---------------------------------------------------------------+
         │                                      │
         ▼ (HTTPS / gRPC)                       ▼
+-------------------------------+      +-------------------------------+
| Worker Node 1                 |      | Worker Node 2                 |
|                               |      |                               |
| +---------------------------+ |      | +---------------------------+ |
| | kubelet                   | |      | | kubelet                   | |
| +---------------------------+ |      | +---------------------------+ |
| | kube-proxy (iptables/IPVS)| |      | | kube-proxy                | |
| +---------------------------+ |      | +---------------------------+ |
| | Container Runtime (CRI)   | |      | | Container Runtime (CRI)   | |
| | (containerd / CRI-O)      | |      | | (containerd / CRI-O)      | |
| +---------------------------+ |      | +---------------------------+ |
|   [Pod A]      [Pod B]        |      |   [Pod C]      [Pod D]        |
+-------------------------------+      +-------------------------------+
```

- **kube-apiserver** : 모든 컴포넌트 간 통신의 허브이자 인증, 인가(RBAC, Role-Based Access Control), 유효성 검증을 담당하는 선언적 REST(Representational State Transfer) API 엔드포인트.
- **etcd 분산 저장소** : Raft 합의 알고리즘 기반으로 클러스터의 모든 상태, 명세, 메타데이터를 영속화하는 단일 진실 공급원(SSOT, Single Source of Truth).
- **kube-scheduler** : 파드의 요구 자원(CPU(Central Processing Unit)/메모리), 노드 어피니티(Affinity), 톨러레이션(Toleration)을 평가하여 최적의 워커 노드에 바인딩.
- **kube-controller-manager** : 레플리카셋, 노드, 엔드포인트 컨트롤러 등을 구동하며 Desired State로 상태를 수렴시키는 핵심 루프.
- **kubelet & kube-proxy** : 워커 노드에서 컨테이너 라이프사이클을 감시하고, 클러스터 내부 가상 IP(Service ClusterIP) 라우팅 규칙을 커널에 주입.

## Ⅳ. 쿠버네티스(Kubernetes)의 비교

- 핵심 요약 : **Pod·Deployment·Service·Ingress·CRD** 리소스 역할 비교.

| 핵심 리소스 / 컴포넌트 | 기능 및 기술 메커니즘 | 기술사적 설계 고려사항 |
|---|---|---|
| Pod | 1개 이상의 컨테이너가 네트워크(IP)와 스토리지를 공유하는 최소 실행 단위 | 사이드카 패턴(로그 수집, 프록시) 적용 시 수명주기 동기화 |
| Deployment / ReplicaSet | 선언적 파드 개수 유지 및 롤링 업데이트, 롤백 제어 | MaxSurge / MaxUnavailable 파라미터 튜닝을 통한 무중단 보장 |
| Service (ClusterIP/NodePort/LB) | 파드의 동적 IP 변경을 추상화하여 고정 가상 IP 및 부하 분산 제공 | IPVS 모드 또는 eBPF 기반 CNI(Container Network Interface) 적용으로 iptables 룰 한계 극복 |
| Ingress / Gateway API | 외부 HTTP(Hypertext Transfer Protocol)/HTTPS(Hypertext Transfer Protocol Secure) 트래픽의 L7 라우팅, SSL(Secure Sockets Layer) 종료, 호스트 기반 포워딩 | Gateway API 표준 채택으로 멀티테넌시 라우팅 분리 |
| CRD(Custom Resource Definition) & Operator | 도메인 특화 로직(DB(Database) 장애복구 등)을 쿠버네티스 네이티브 API로 확장 | 커스텀 컨트롤러의 에러 핸들링 및 과도한 API 호출 방지 |

## Ⅴ. 쿠버네티스(Kubernetes)의 한계와 방안

- 핵심 요약 : **etcd 병목·네트워크 오버레이·설정 오류**를 NVMe 분리·eBPF CNI·GitOps로 대응.

- 대규모 클러스터에서 **etcd I/O** 및 Raft 합의 병목 :
  - 한계점 : 노드 수가 수천 대를 초과하거나 이벤트 빈도가 급증할 때 etcd 쓰기 지연 발생으로 전체 API 서버 응답 지연 및 장애 전파.
  - 해결 방안 : etcd 전용 초고속 NVMe(Non-Volatile Memory Express) 스토리지 분리 배정, 이벤트 리소스 etcd 분리 클러스터 구성, 가상 클러스터(vcluster) 도입.
- 네트워크 오버레이 성능 저하 및 보안 가시성 부족 :
  - 한계점 : VXLAN(Virtual Extensible LAN)/Geneve 터널링 기반 오버레이 네트워크 구성 시 패킷 캡슐화 오버헤드로 인한 처리량 저하 및 네트워크 트레이싱 난제.
  - 해결 방안 : eBPF 기반 CNI(Cilium)를 도입하여 커널 레벨 직접 패킷 라우팅 및 실시간 네트워크 보안 가시성(Hubble) 확보.
- 설정 **오류(Misconfiguration)** 및 가파른 학습 곡선 :
  - 한계점 : 복잡한 YAML(YAML Ain't Markup Language) 정의, 과도한 권한 부여(ClusterRoleBinding), 취약한 시크릿 관리로 인한 보안 침해 위험 노출.
  - 해결 방안 : GitOps(ArgoCD) 파이프라인 강제화, OPA(Open Policy Agent) Gatekeeper / Kyverno를 통한 선언적 정책 검증, External Secrets Operator 연계.

## Ⅵ. 쿠버네티스(Kubernetes) 적용 제언

- 핵심 요약 : **IDP·KEDA·GPU 슬라이싱**으로 개발자 생산성·AI 워크로드 지원.
- 플랫폼 엔지니어링(IDP) : Backstage 기반 셀프서비스 포털.
- KEDA : Kafka Lag·비즈니스 메트릭 기반 선제적 스케일링.
- GPU 슬라이싱 : MIG/vGPU로 AI 워크로드 자원 가동률 극대화.

## Ⅶ. 결론

- 핵심 요약 : 쿠버네티스는 **선언적 오케스트레이션**으로 컨테이너 운영을 자동화하나 etcd·네트워크·설정 리스크를 관리해야 함.
- 쿠버네티스는 선언적 API와 자가 치유로 대규모 컨테이너 배포·스케일링·무중단 운영을 자동화하지만, etcd 병목·오버레이 성능·설정 오류 리스크를 NVMe 분리·eBPF CNI·GitOps로 관리해야 함.
- 답안에는 컨트롤 플레인/워커 구조, 리소스 비교, 한계·대응, IDP·KEDA·GPU 제언을 연결.