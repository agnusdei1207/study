---
title: "세그먼테이션 오류 (Segmentation Fault)"
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

## Ⅰ. 세그멘테이션 오류(Segmentation Fault)의 개요

- 개념 : 운영체제의 가상 메모리 관리 환경에서 프로세스가 자신에게 할당되지 않은 메모리 영역을 참조하거나, 할당된 영역일지라도 허용되지 않은 권한(읽기 전용 영역에 쓰기, 실행 불가 영역에서 코드 실행 등)으로 접근할 때 하드웨어(MMU, Memory Management Unit)와 커널에 의해 발생하는 **메모리 보호 예외(Memory Protection Exception)** 및 비정상 종료 시그널(SIGSEGV, Signal 11).
- 배경 및 필요성 : 다중 프로그래밍 환경에서 프로세스 간 메모리 간섭을 원천 격리하고 커널 및 중요 시스템 데이터 구조를 보호하기 위한 하드웨어 기반 메모리 보호 아키텍처의 핵심 방어 기제.
- 핵심 목적 : 시스템 메모리 무결성 보호, 타 프로세스 공간 침범 방지, 소프트웨어 결함 발생 시 즉각적인 **결함 격리(Fail-Fast)** 및 **디버깅 증적(Core Dump)** 제공.

## Ⅱ. 세그멘테이션 오류의 하드웨어/커널 감지 메커니즘

```text
┌────────────────────────────────────────────────────────────────────────┐
│ [ CPU 명령 실행 (Instruction: MOV [0x00000000], EAX 등) ]              │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Virtual Address Access
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 하드웨어 MMU (Memory Management Unit) ]                              │
│  - TLB (Translation Lookaside Buffer) 탐색 및 Page Table Walk          │
│  - 유효성 비트(Valid Bit == 0) 확인 -> 존재하지 않는 페이지            │
│  - 권한 비트(R/W/X) 검사 -> Read-Only 페이지에 쓰기 시도               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Hardware Page Fault Exception
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ OS 커널 페이지 폴트 핸들러 (do_page_fault) ]                         │
│  - 프로세스 가상 메모리 영역(vm_area_struct) 탐색                      │
│  - 정상적 가상 메모리 확장(Demand Paging/Stack Growth) 여부 판정       │
│  - 유효하지 않은 접근 판정 -> force_sig_info(SIGSEGV) 호출             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ Signal Delivery (Signal 11)
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ [ 프로세스 종료 및 코어 덤프 생성 (Default Action: Terminate & Core) ]  │
└────────────────────────────────────────────────────────────────────────┘
```

- **하드웨어 검증 단계** : CPU(Central Processing Unit)가 가상 주소를 물리 주소로 변환할 때 MMU가 **페이지 테이블 엔트리** (PTE, Page Table Entry)의 Present 비트와 권한 플래그를 검사하여 위반 시 즉각 하드웨어 트랩(Trap) 유발.
- **커널 처리 단계** : 커널의 `do_page_fault()` 함수는 해당 주소가 프로세스의 `vma(vm_area_struct)` 목록에 속하는지 확인하고, 유효하지 않은 접근일 경우 `SIGSEGV` 시그널을 발행하여 프로세스를 강제 종료하고 디버깅용 코어 덤프(Core Dump)를 파일시스템에 기록.

## Ⅲ. 세그멘테이션 오류의 주요 발생 원인 비교 분석

| 원인 분류 | 대표적인 코드 패턴 | 세그멘테이션 오류 발생 원리 | 예방 및 검출 기법 |
| :--- | :--- | :--- | :--- |
| **널 포인터 역참조 (Null Pointer)** | `int *p = NULL; *p = 10;` | 0번지(0x0)를 포함한 최하위 가상 주소 영역의 비매핑 페이지 접근 | 포인터 유효성 사전 검사, 옵셔널 타입 |
| **읽기 전용 메모리 쓰기 (RO Violation)** | `char *str = "hello"; str[0] = 'H';` | 텍스트(Text)/코드 세그먼트의 Read-Only 페이지에 쓰기 권한 위반 | `const` 키워드 강제, 정적 코드 분석 |
| **스택 오버플로우 (Stack Overflow)** | 종료 조건 없는 무한 재귀 호출 | 스택 가드 페이지(Stack Guard Page) 침범 및 비매핑 영역 도달 | 재귀 깊이 제한, 컴파일러 스택 보호기 |
| **버퍼 오버런 (Buffer Overrun)** | 정적/동적 배열 경계를 크게 벗어난 쓰기 | 할당된 세그먼트 바운더리를 벗어나 보호된 메모리 페이지 침범 | 바운드 체킹(Bounds Checking), ASan |
| **해제된 메모리 역참조 (UAF, Use-After-Free/Dangling)** | `free(ptr); ptr->data = 100;` | OS(Operating System)에 이미 반환되어 할당 해제된 익명 가상 메모리 주소 접근 | 스마트 포인터, 메모리 할당자 가드 |

## Ⅳ. 세그멘테이션 오류 대응의 주요 한계점 및 해결 방안

- 크래시 시점과 버그 유발 시점 간의 **비동기성(Latent Corruption)** :
  - 한계점 : 메모리 오염이 발생한 즉시 크래시되지 않고 한참 뒤 전혀 다른 로직 수행 중 SIGSEGV가 발생하여 원인 추적이 극도로 난해.
  - 해결 방안 : 디버깅 빌드에 LLVM AddressSanitizer(ASan) 및 UndefinedBehaviorSanitizer(UBSan)를 상시 활성화하여 메모리 오염 발생 즉시 정밀 콜스택 출력.
- 운영 환경에서의 코어 덤프 용량 폭증 및 디스크 **I/O** 병목 :
  - 한계점 : 수십 GB의 메모리를 사용하는 고성능 서버 데몬에서 SIGSEGV 발생 시 대용량 코어 덤프 쓰기로 인해 디스크가 고갈되고 연속 장애 유발.
  - 해결 방안 : `core_pattern` 설정을 통해 압축 코어 덤프 스트리밍 적용, `coredumpctl` 연동 및 필수 메모리 세그먼트만 덤프하는 `coredump_filter` 최적화.
- 시그널 핸들러 내 비동기 안전하지 않은 함수 호출 위험 :
  - 한계점 : `SIGSEGV` 핸들러 내에서 `printf()`, `malloc()` 등 비동기 시그널에 안전하지 않은(Async-Signal-Unsafe) 함수 호출 시 데드락(Deadlock) 유발.
  - 해결 방안 : 시그널 핸들러를 임의 재정의하지 않고 커널 기본 덤프 동작을 유지하거나, 핸들러 내부에서는 저수준 `write()` 시스템 콜만 사용하는 미니멀 로거 적용.

## Ⅴ. 세그멘테이션 오류 근절을 위한 기술사적 제언

- 컴파일러 경계 보호 및 현대적 툴체인 파이프라인 구축 : C/C++ 프로젝트 빌드 시 `-fstack-protector-strong`, `-D_FORTIFY_SOURCE=3`, `-Wformat-security` 등 컴파일러 보안 플래그를 필수화하고, 정적 분석(SonarQube, Coverity)을 CI(Continuous Integration)/CD(Continuous Delivery) 품질 게이트로 강제해야 함.
- **메모리 안전성(Memory-Safety)** 중심의 아키텍처 전환 : 장기적으로 비즈니스 로직 및 네트워크 인터페이싱 계층을 Rust, Go, Java 등 자동 메모리 관리 또는 소유권 모델 언어로 전환하여 런타임 세그멘테이션 오류를 컴파일 타임에 원천 제거할 것을 제언함.
