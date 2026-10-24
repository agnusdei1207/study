---
title: "컨테이너(Container)"
author: "agnusdei1207"
date: "2026-10-24T22:24:38+09:00"
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

- 컨테이너(Container), 네임스페이스(Namespaces), 제어 그룹(cgroups), OverlayFS, OCI(Open Container Initiative)
- 가상머신(VM, Virtual Machine), 샌드박스 컨테이너(gVisor, Kata Containers), 루트리스(Rootless) 컨테이너, Seccomp(Secure Computing Mode)
- 멀티스테이지 빌드(Multi-stage Build), CVE(Common Vulnerabilities and Exposures), SBOM(Software Bill of Materials), Cosign

## Ⅰ. 컨테이너(Container)의 개요

- 핵심 요약 : **컨테이너** (Container)는 호스트 OS 커널을 공유하며 네임스페이스와 cgroups로 애플리케이션을 격리 패키징하는 OS 레벨 가상화 기술.
- 개념 : 호스트 OS(Operating System)의 커널을 공유하면서, **리눅스 네임스페이스** (Namespaces)로 프로세스가 보는 자원의 범위를 나누고 **제어 그룹** (cgroups)으로 사용할 수 있는 자원의 상한을 정해, 코드·런타임·라이브러리·설정을 하나의 격리 실행 단위로 묶는 기술.
- 배경 및 필요성 : 하이퍼바이저 기반 가상머신(VM, Virtual Machine)은 Guest OS 전체를 띄우므로 자원 낭비, 큰 이미지 크기, 긴 부팅 시간이 따르고, 마이크로서비스의 빠른 배포 주기를 수용하기 어려워 경량 격리 방식이 필요해짐.
- 주요 목적 : 즉각적인 기동, 호스트 커널을 직접 활용한 네이티브에 가까운 성능, 개발·테스트·운영 환경의 일치.

## Ⅱ. 컨테이너(Container)의 특징 및 장점

- 핵심 요약 : 프로세스 뷰 분리, 자원 상한 제어, 레이어형 파일 시스템, 공개 표준이 결합되어 경량·고속·이식성을 얻는 구조.

1. 네임스페이스 (Namespaces) : PID(Process ID), 네트워크, 마운트, IPC(Inter-Process Communication), UTS(UNIX Time-Sharing System), 사용자 ID 공간을 프로세스 단위로 분리 → 컨테이너마다 독립된 프로세스 트리와 네트워크 뷰 제공.
2. 제어 그룹 (cgroups, Control Groups) : CPU 사용 시간, 메모리 상한, 디스크 I/O, 네트워크 대역폭을 프로세스 그룹 단위로 강제 → 특정 컨테이너가 호스트 자원을 독점하지 못하도록 막음.
3. **OverlayFS** (Overlay File System) : 읽기 전용 이미지 레이어 위에 쓰기 가능한 컨테이너 레이어를 덧씌움 → 같은 이미지 레이어를 여러 컨테이너가 공유해 저장 공간 절약.
4. **OCI** (Open Container Initiative) 표준 : 이미지 형식을 정한 image-spec과 실행 방식을 정한 runtime-spec → 엔진과 런타임을 교체해도 같은 이미지를 쓸 수 있어 벤더 종속이 줄어듦.

## Ⅲ. 컨테이너(Container)의 구조 및 동작 메커니즘

- 핵심 요약 : 컨테이너 엔진이 런타임을 호출하면 격리 설정, 자원 상한, 파일 계층이 한 커널 위에서 함께 동작하는 구조.
- 컨테이너 엔진(Docker, containerd 등)은 OCI 런타임인 runc를 호출하여 커널에 격리 설정을 요청하고, 이미지 레이어는 OverlayFS가 합쳐서 파일 시스템으로 제공함.

```text
[ 컨테이너 실행 흐름 ]

컨테이너 엔진 (Docker, containerd)
        ↓ OCI 런타임 호출 (runc)
리눅스 커널 시스템 콜
        ↓
네임스페이스 (보이는 범위 격리)
        ↓
cgroups (자원 상한 강제)
        ↓
OverlayFS (이미지 레이어 + 쓰기 레이어)
```

```text
[ OverlayFS 레이어 구조 ]

컨테이너 쓰기 레이어 (읽기·쓰기 가능)
        ↓ 아래 레이어 위에 덮어씀
이미지 레이어 N (읽기 전용)
        ↓
이미지 레이어 1 (베이스 OS, 읽기 전용)
```

## Ⅳ. 컨테이너(Container)의 비교

- 핵심 요약 : 가상머신, 일반 컨테이너, 샌드박스 컨테이너는 가상화 수준과 기동 속도, 격리 강도가 달라 워크로드의 신뢰 수준에 맞춰 선택.

| 비교 항목 | 가상머신 (VM) | 컨테이너 (Container) | 샌드박스 컨테이너 (gVisor, Kata Containers) |
| --- | --- | --- | --- |
| 가상화 수준 | 하드웨어 수준 가상화 (하이퍼바이저) | OS 커널 수준 프로세스 격리 | 커널 분리 또는 경량 가상머신 결합 |
| Guest OS | 독립된 Guest OS를 완전히 구동 | 별도 Guest OS 없이 호스트 커널 공유 | 독립 커널 또는 경량 VM 구동 |
| 기동 시간 | 상대적으로 긴 편 | 매우 빠름 | 빠른 편 |
| 자원 오버헤드와 집적도 | 오버헤드가 크고 집적도가 낮음 | 가볍고 집적도가 높음 | 중간 수준 |
| 보안 격리 강도 | 하드웨어 수준의 강한 격리 | 커널 공유에 따른 취약점 파급 위험 | 커널 분리로 격리 강화 |

- 컨테이너는 집적도와 기동 속도에서 강점이 있으나, 호스트 커널을 공유하므로 멀티테넌트 환경에서는 커널 취약점에 대한 방어가 필수적임.

## Ⅴ. 컨테이너(Container)의 한계와 방안

- 핵심 요약 : 권한 상승, 파일 시스템 쓰기 성능, 이미지 비대화를 루트리스 실행, 볼륨 마운트, 이미지 경량화로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 호스트 커널 공유에 따른 권한 상승과 **탈옥** (Escape) | 루트 권한 컨테이너가 커널 취약점을 악용하면 호스트 전체 제어권 탈취 가능 | 루트리스(Rootless) 실행, **Seccomp** (Secure Computing Mode) 시스템 콜 필터링과 AppArmor 적용, gVisor 등 샌드박스 런타임 도입 | 권한 상승 시도 탐지 건수, 차단된 시스템 콜 수 |
| OverlayFS의 쓰기 성능 저하 | 복사 후 쓰기(Copy-on-Write) 구조 때문에 대용량 쓰기와 데이터베이스 실행 시 I/O 병목 발생 | I/O 집약 워크로드는 볼륨 마운트(Bind Mount, Persistent Volume)로 호스트 파일 시스템을 직접 사용 | 쓰기 지연 시간, IOPS |
| 이미지 비대화와 공급망 취약점 | 불필요한 패키지로 이미지가 커지고 **CVE** (Common Vulnerabilities and Exposures) 취약점이 누적 | **멀티스테이지 빌드** (Multi-stage Build), Distroless나 Alpine 같은 경량 베이스 이미지, Trivy 스캔 자동화 | 이미지 크기, CVE 건수 |

## Ⅵ. 컨테이너(Container)에 대한 기술사적 제언

- 핵심 요약 : 공급망 서명, 자원 튜닝, 커널 기능 전환을 묶어 컨테이너를 신뢰 가능한 운영 기반으로 정착.

1. DevSecOps 파이프라인 관리자는 빌드된 이미지마다 **SBOM** (Software Bill of Materials, 소프트웨어 구성 명세서)을 생성하고 Cosign으로 서명하며, 쿠버네티스 Admission Controller가 서명 검증을 통과한 이미지만 배포하도록 한다.
2. 플랫폼 운영팀은 컨테이너별 Requests와 Limits를 실제 사용량 기준으로 튜닝하여 OOM 종료와 CPU 스로틀링을 줄이고, 그 지표를 상시 대시보드로 관리한다.
3. 인프라팀은 cgroups v2로 전환하여 PSI(Pressure Stall Information) 기반으로 메모리 압력을 감지하고, 루트리스 방식의 멀티테넌시 구성을 기본 표준으로 정한다.

## Ⅶ. 결론

- 핵심 요약 : 컨테이너는 네임스페이스, cgroups, OverlayFS로 애플리케이션을 경량 격리하여 빠른 기동과 높은 집적도를 실현하는 OS 레벨 가상화 기술.
- 시사점 : 커널 공유에 따른 보안 위험을 루트리스 실행, 샌드박스, 공급망 검증으로 함께 관리해야 도입 효과가 유지됨.
