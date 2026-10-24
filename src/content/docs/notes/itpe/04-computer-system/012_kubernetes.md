---
title: "쿠버네티스(Kubernetes)"
author: "agnusdei1207"
date: "2026-10-24T22:27:31+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 쿠버네티스(Kubernetes), 컨테이너 오케스트레이션(Container Orchestration), 컨트롤 플레인(Control Plane), 워커 노드(Worker Node)
- 선언적 구성(Declarative Configuration), 조정 루프(Reconcile Loop), 자가 치유(Self-healing), etcd
- 파드(Pod), 디플로이먼트(Deployment), 서비스(Service), 인그레스(Ingress), CRD(Custom Resource Definition), 오퍼레이터(Operator)
- 컨테이너 네트워크 인터페이스(CNI, Container Network Interface), eBPF, 정책 엔진, GitOps

## Ⅰ. 쿠버네티스의 개요

- 핵심 요약 : 선언된 상태를 유지하며 컨테이너의 배포, 확장, 복구를 자동화하는 **컨테이너 오케스트레이션** (Container Orchestration) 플랫폼.
- 개념 : 컨테이너 애플리케이션의 배포, 스케일링, 서비스 탐색, 무중단 운영을 원하는 상태를 선언하는 **선언적 구성** (Declarative Configuration) 방식으로 관리하는 플랫폼 (쿠버네티스, Kubernetes).
- 배경 및 필요성 : 마이크로서비스 아키텍처(MSA, Microservice Architecture)의 확산으로 관리할 컨테이너 인스턴스가 급증하면서 수동 배포와 장애 복구의 한계가 드러났고, 구글 내부 클러스터 관리 경험(Borg)을 바탕으로 이를 자동화하는 도구로 등장함.
- 주요 목적 : 선언적 API(Application Programming Interface)와 **자가 치유** (Self-healing)로 고가용성을 확보하고, 인프라 추상화로 이식성과 자원 활용률을 높이는 것.

## Ⅱ. 쿠버네티스의 특징 및 장점

- 핵심 요약 : 선언적 구성, 자가 치유, 인프라 추상화가 결합되어 대규모 컨테이너 운영을 자동화하는 구조.

1. 선언적 구성 : 원하는 상태(Desired State)를 명세로 제출 → 컨트롤 플레인이 현재 상태(Current State)를 원하는 상태에 맞춰 수렴 → 수동 개입 감소.
2. 자가 치유 : 파드 장애를 감지해 재시작하거나 다른 노드에 재배치 → 장애 복구 시간 단축.
3. 서비스 디스커버리 : 서비스 객체가 변동하는 파드 주소를 고정 가상 주소로 추상화 → 클라이언트 설정 변경 없이 연결 유지.
4. 수평 확장 : 메트릭을 기준으로 파드 수를 자동 조정하는 HPA(Horizontal Pod Autoscaler) → 부하 변화에 대응.
5. 인프라 추상화 : 워크로드 명세가 하부 인프라 세부 사항과 분리 → 멀티·하이브리드 클라우드 환경에서 이식성 확보.

## Ⅲ. 쿠버네티스의 구조 및 동작 메커니즘

- 핵심 요약 : 컨트롤 플레인이 상태를 저장하고 판단하며 워커 노드가 실행을 맡고, 조정 루프가 두 상태를 일치시키는 구조.
- **컨트롤 플레인** (Control Plane) : 클러스터 전체 상태를 관리하는 구성 요소 집합.
- **워커 노드** (Worker Node) : 실제 워크로드인 파드가 실행되는 노드.
- **조정 루프** (Reconcile Loop) : 원하는 상태와 현재 상태를 지속적으로 비교하여 차이를 줄이는 핵심 메커니즘.

1. kube-apiserver : 모든 컴포넌트 통신의 허브이자 인증, 인가(RBAC, Role-Based Access Control), 검증을 담당하는 REST(Representational State Transfer) API 엔드포인트.
2. etcd : Raft 합의 알고리즘 기반의 분산 저장소로, 클러스터의 모든 상태와 명세를 보관하는 단일 진실 공급원(SSOT, Single Source of Truth).
3. kube-scheduler : 파드의 자원 요구, 노드 어피니티(Affinity), 톨러레이션(Toleration)을 평가해 적합한 워커 노드에 배치.
4. kube-controller-manager : 레플리카셋, 노드 컨트롤러 등을 구동하며 원하는 상태로 수렴시키는 조정 루프의 실행 주체.
5. kubelet · kube-proxy : kubelet은 컨테이너 런타임 인터페이스(CRI, Container Runtime Interface)를 통해 컨테이너 생명주기를 관리하고, kube-proxy는 서비스 라우팅 규칙을 노드에 적용.

```text
[ 선언 요청의 처리 흐름 ]

사용자 (선언 명세 제출)
   ↓
kube-apiserver (인증·검증·저장)
   ↓
etcd (상태 기록)
   ↓
컨트롤러·스케줄러 (차이 감지, 배치)
   ↓
워커 노드 kubelet (파드 실행)
```

```text
[ 조정 루프 ]

원하는 상태 (Desired State)
   ↓
현재 상태 관찰 (Current State)
   ↓
차이 판정
   ├─ 차이 있음 → 파드 생성·삭제·갱신
   ├─ 차이 없음 → 대기 후 재관찰
```

## Ⅳ. 쿠버네티스의 리소스 비교

- 핵심 요약 : 파드, 디플로이먼트, 서비스, 인그레스, CRD는 실행, 배포, 연결, 외부 진입, 기능 확장을 각각 담당하는 역할 차이.

| 핵심 리소스 | 기능 및 메커니즘 | 설계 고려사항 |
| --- | --- | --- |
| 파드 (Pod) | 하나 이상의 컨테이너가 네트워크 주소와 스토리지를 공유하는 최소 실행 단위 | 사이드카 패턴(로그 수집, 프록시) 적용 시 수명주기 동기화 |
| 디플로이먼트 (Deployment) | 선언된 파드 수 유지, 롤링 업데이트와 롤백 제어 | 최대 추가 수(maxSurge)와 최대 불가용 수(maxUnavailable) 조정으로 무중단 확보 |
| 서비스 (Service) | 파드의 변동 주소를 고정 가상 주소와 부하 분산으로 추상화 | 대규모 환경에서는 eBPF(extended Berkeley Packet Filter) 기반 네트워크 적용 검토 |
| 인그레스 (Ingress) / 게이트웨이 API (Gateway API) | 외부 HTTP(Hypertext Transfer Protocol)·HTTPS 트래픽의 경로 라우팅, TLS(Transport Layer Security) 종료 | 게이트웨이 API 표준 채택으로 멀티테넌트 라우팅 분리 |
| CRD (Custom Resource Definition) & 오퍼레이터 (Operator) | 데이터베이스 장애 복구 같은 도메인 로직을 쿠버네티스 API로 확장 | 커스텀 컨트롤러의 오류 처리와 과도한 API 호출 방지 |

## Ⅴ. 쿠버네티스의 한계와 방안

- 핵심 요약 : etcd 병목, 네트워크 오버레이 부담, 설정 오류를 저장소 분리, eBPF 기반 네트워크, GitOps 정책 검증으로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| etcd 병목 | 노드 수 증가와 이벤트 폭증으로 쓰기 지연이 생겨 API 서버 응답이 저하되고 장애가 확산 | etcd 전용 고속 저장소 배정, 이벤트 저장소 분리, 가상 클러스터(vcluster) 도입 | etcd 쓰기 지연 시간, API 응답 시간 |
| 네트워크 오버레이 부담 | VXLAN(Virtual Extensible LAN), Geneve 캡슐화로 처리량이 떨어지고 트래픽 추적이 어려움 | eBPF 기반 **컨테이너 네트워크 인터페이스** (CNI, Container Network Interface) 플러그인과 네트워크 가시성 도구 활용 | 패킷 처리량, 정책 위반 탐지 건수 |
| 설정 오류와 과도한 권한 | 복잡한 매니페스트, 광범위한 클러스터 역할 바인딩, 취약한 비밀 값 관리로 침해 위험 노출 | **GitOps** 기반 배포 강제, 정책 엔진인 OPA(Open Policy Agent) Gatekeeper나 Kyverno로 선언 검증, 외부 비밀 값 관리 연계 | 정책 위반 건수, 과권한 계정 수 |

## Ⅵ. 쿠버네티스의 적용 제언

- 핵심 요약 : 내부 개발자 플랫폼, 이벤트 기반 자동 확장, 가속기 분할을 결합해 개발 생산성과 인공지능 워크로드 지원을 높이는 방향.

- 여러 팀이 클러스터를 공유하는 조직은 내부 개발자 플랫폼(IDP, Internal Developer Platform)을 두어 개발자가 표준 템플릿으로 환경을 직접 구성하도록 하는 것이 생산성에 유리함.
- 메시지 대기열의 적체량 같은 비즈니스 지표로 파드 수를 조정하는 KEDA(Kubernetes Event-driven Autoscaling)를 도입하면 급증하는 부하에 선제적으로 대응할 수 있음.
- 인공지능(AI, Artificial Intelligence) 워크로드가 많은 클러스터에서는 그래픽 처리 장치(GPU, Graphics Processing Unit)를 다중 인스턴스 GPU(MIG, Multi-Instance GPU)나 가상 GPU(vGPU, virtual GPU) 방식으로 나눠 쓰면 자원 가동률을 높일 수 있음.

## Ⅶ. 결론

- 핵심 요약 : 쿠버네티스는 선언적 오케스트레이션으로 배포와 복구를 자동화하지만, etcd 성능, 네트워크, 설정 위험을 함께 다뤄야 실효성이 확보되는 플랫폼.
- 대규모 운영에서는 제어 평면의 안정성과 정책의 자동 검증이 플랫폼 신뢰도를 좌우함.
