---
title: "스토리지 가상화 (Storage Virtualization)"
author: "Antigravity"
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

## Ⅰ. 스토리지 가상화(Storage Virtualization)의 개요

- 개념 : 서로 다른 물리적 스토리지 장비(DAS(Direct-Attached Storage), SAN(Storage Area Network), NAS(Network-Attached Storage) 및 이기종 벤더 어레이)의 물리적 저장 공간을 논리적 계층으로 **추상화(Abstraction)** 하여, 단일의 통합된 **가상 스토리지 풀** (Logical Storage Pool)로 결합하고 중앙에서 동적으로 할당·관리하는 인프라 기술.
- 배경 및 필요성 : 스토리지 벤더별 사일로화로 인한 자원 파편화, 용량 불균형(특정 장비는 포화, 타 장비는 유휴), 무중단 데이터 마이그레이션의 어려움 및 스토리지 TCO(Total Cost of Ownership) 폭증을 해결하기 위해 발전.
- 핵심 목적 : 이기종 스토리지 통합 관리를 통한 활용률 극대화, **씬 프로비저닝(Thin Provisioning)** 및 자동 계층화(Auto-Tiering), 무중단 용량 확장 및 비즈니스 연속성 보장.

## Ⅱ. 스토리지 가상화의 구현 계층별 아키텍처 및 동작 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ 스토리지 가상화 구현 3대 계층 아키텍처 ]                             │
│                                                                        │
│   [ 1. 호스트 기반 (Host-Based) ]                                      │
│    - 호스트 OS 커널 레벨 LVM (Logical Volume Manager) / SDS 에이전트   │
│    - 서버 CPU/메모리 부하 발생, 이종 OS 간 관리 파편화                │
│                     │ I/O 요청 (SCSI / NVMe Commands)                  │
│                     ▼                                                  │
│   [ 2. 네트워크/패브릭 기반 (Network/Fabric-Based) ]                   │
│    - SAN 스위치 또는 전용 인라인(In-Band) / 아웃오브밴드(Out-of-Band) 가상화 어플라이언스│
│    - 스토리지 전송 경로 상에서 메타데이터 매핑 및 가상 LUN 제공        │
│                     │ Physical I/O                                     │
│                     ▼                                                  │
│   [ 3. 스토리지 어레이 기반 (Storage-Array Based) ]                    │
│    - 마스터 스토리지 컨트롤러가 백엔드의 타사 스토리지 LUN을 가상화   │
│    - 벤더 종속성 존재, 컨트롤러 캐시 및 고급 기능(스냅샷) 상속         │
└────────────────────────────────────────────────────────────────────────┘
```

- **인밴드(In-Band) 가상화 메커니즘** : 데이터 경로(Data Path)와 제어 경로(Control Path)가 동일한 가상화 엔진을 통과하여 단순하고 강력한 캐싱/보안을 제공하나 어플라이언스가 병목 및 단일 장애점이 될 수 있음.
- **아웃오브밴드(Out-of-Band) 가상화 메커니즘** : 제어 메타데이터는 별도 서버에서 처리하고 실제 데이터 입출력은 호스트와 스토리지 간 직접 전송하여 고성능을 유지하나 호스트 에이전트 설치 필요.

## Ⅲ. 스토리지 가상화 구현 방식별 비교 분석

| 비교 항목 | 호스트 기반 가상화 (Host-Based) | 네트워크 기반 가상화 (Network-Based) | 스토리지 제어기 기반 (Array-Based) |
| :--- | :--- | :--- | :--- |
| **구현 위치** | 각 호스트 서버의 OS(Operating System) 볼륨 매니저 | SAN 스위치 또는 독립 가상화 엔진 | 메인 스토리지 컨트롤러 펌웨어 |
| **대표 기술** | Linux LVM(Logical Volume Manager), Veritas Volume Manager | IBM(International Business Machines) SAN Volume Controller(SVC) | Hitachi USP/VSP 가상화, NetApp FlexArray|
| **이기종 지원성** | 높음 (호스트 OS 지원 범위 내) | 매우 높음 (대부분의 SAN 스토리지) | 중간 (인증된 타사 스토리지 어레이만)|
| **호스트 영향** | 서버 CPU(Central Processing Unit)/메모리 자원 점유 발생 | 호스트에 무부하 (호스트 투명성) | 호스트에 무부하 |
| **주요 장점** | 추가 하드웨어 구매 불필요 | 중앙 집중식 단일 뷰 통합 관리 | 컨트롤러의 고성능 캐시 활용 극대화|

## Ⅳ. 스토리지 가상화의 주요 한계점 및 해결 방안

- 중앙 가상화 어플라이언스의 I/O 병목 및 단일 **장애점(SPOF, Single Point of Failure)** :
  - 한계점 : 전사 스토리지 트래픽이 특정 인밴드 가상화 엔진에 집중될 경우 레이턴시 급증 및 컨트롤러 장애 시 전사 서비스 중단.
  - 해결 방안 : 액티브-액티브 클러스터링 기반 다중 노드 스케일아웃 가상화 엔진 구성, 다중 경로 I/O(MPIO, Multipathing) 페일오버 필수 적용.
- 이기종 스토리지 고유 기능(스냅샷, 원격 복제)의 비호환성 :
  - 한계점 : 하부 물리 스토리지들이 제공하는 하드웨어 가속 기능이 상위 가상화 계층의 공통 메타데이터로 일원화되면서 고유 기능 비활성화.
  - 해결 방안 : 가상화 계층에서 제공하는 벤더 독립적 통합 스냅샷/CDP(Continuous Data Protection) 엔진으로 기능 대체 및 표준 API(Application Programming Interface) 연계.
- 메타데이터 손상 시 전사 볼륨 붕괴 위험 :
  - 한계점 : 논리-물리 주소 매핑 테이블(Mapping Table)이 손상될 경우 연결된 모든 물리 스토리지의 데이터 블록을 식별 불가.
  - 해결 방안 : 분산 합의 기반 메타데이터 삼중화(3-Way Mirroring), 주기적 NVRAM 스냅샷 백업 및 트랜잭션 저널링 체계 확립.

## Ⅴ. 차세대 스토리지 인프라를 위한 기술사적 제언

- 소프트웨어 정의 **스토리지(SDS, Software-Defined Storage)** 및 클라우드 네이티브 스토리지(CSI, Container Storage Interface)로의 진화 : 전통적인 전용 하드웨어 가상화 장비에서 탈피하여 범용 x86 서버 풀을 스토리지로 묶는 SDS(Ceph, VMware vSAN) 및 쿠버네티스 표준 CSI(Container Storage Interface) 기반의 동적 볼륨 오케스트레이션으로 전환해야 함.
- **NVMe(Non-Volatile Memory Express)-oF** 기반 가상화 패브릭 구축 : 레거시 FC-SAN 기반 가상화의 한계를 극복하기 위해 RDMA(Remote Direct Memory Access) over Converged Ethernet(RoCE(Remote Direct Memory Access over Converged Ethernet) v2) 기반의 NVMe-oF 스토리지 가상화를 적용하여 마이크로초 단위의 엔드투엔드 올플래시 성능을 보장할 것을 제언함.
