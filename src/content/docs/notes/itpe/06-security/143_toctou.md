---
title: "TOCTOU(Time Of Check To Time Of Use)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. TOCTOU(Time Of Check To Time Of Use)의 개요

- 개념 : 소프트웨어가 특정 자원(파일, 메모리, 권한)의 상태를 검사(Check)하는 시점과 해당 자원을 실제로 접근하여 사용하는(Use) 시점 사이에 발생하는 **미세한 시간차** (Race Window)를 악용하여 자원을 바꿔치거나 변조하는 **경쟁 상태** (Race Condition) 취약점.
- 배경 및 필요성 : 멀티태스킹 운영체제는 **시분할** (Time-sharing) 방식으로 프로세스를 스케줄링하므로, 검사 함수 실행 후 사용 함수 실행 직전에 다른 프로세스로 **컨텍스트 스위칭** (Context Switching)이 발생할 수 있는 구조적 맹점에서 기인함.
- 핵심 목적 : 자원의 상태 검증 로직을 무력화하여 비인가자가 시스템 관리자 권한(SetUID root)으로 임의의 시스템 핵심 파일(/etc/passwd)을 덮어쓰거나 무단 열람.

## Ⅱ. TOCTOU(Time Of Check To Time Of Use)의 핵심 아키텍처 및 동작 메커니즘

TOCTOU는 통상 **심볼릭 링크** (Symbolic Link)를 악용하여 발생하며, 권한 검사(access)와 파일 열기(open) 사이의 틈새에 공격자가 링크 대상을 시스템 파일로 치환하는 메커니즘을 가짐.

```text
[ TOCTOU(Time Of Check To Time Of Use) 공격 흐름 및 경쟁 구간 ]

  [ 취약한 SetUID 특권 프로그램 ]                  [ 공격자 프로세스 (Race Runner) ]
  (1) Check 단계:
      if (access("/tmp/userfile", W_OK) == 0)
      * 일반 사용자 쓰기 권한 정상 확인!
                |
                |  ==========================================
                +-- [ 경쟁 상태 구간 (Race Window) ] --------+
                |   * OS가 공격자 프로세스로 CPU 제어권 넘김 |
                |  ==========================================
                |                                            v
                |                                    (2) 공격자의 자원 바꿔치기:
                |                                        unlink("/tmp/userfile");
                |                                        symlink("/etc/shadow", "/tmp/userfile");
                |                                        * 정상 파일을 핵심 시스템 파일로 교체!
                |                                            |
                | <------------------------------------------+
                v (다시 특권 프로그램 실행)
  (3) Use 단계:
      fd = open("/tmp/userfile", O_WRONLY);
      write(fd, payload, len);
      * 특권 권한(root)으로 /etc/shadow를
        성공적으로 덮어써서 루트 권한 획득!
```

- **경쟁 구간(Race Window)** : 자원 검사 시스템 콜(access, stat)과 자원 사용 시스템 콜(open, unlink) 사이에 존재하는 수 마이크로초~밀리초 단위의 취약한 시간적 간극.
- **심볼릭 링크 레이스(Symlink Race)** : 공격자가 임시 디렉토리(/tmp)에 일반 파일을 생성해 두고 검사를 통과시킨 직후, 해당 파일을 삭제하고 타깃 시스템 파일로 향하는 심볼릭 링크를 초고속으로 생성하는 수법.
- **원자성(Atomicity) 결여** : 검사와 사용이 단일한 불가분의 하드웨어/OS 원자적 트랜잭션으로 묶여 있지 않고 두 개의 개별 시스템 콜로 분리되어 있는 구조적 결함.
- **동시성 프로그래밍 취약성** : 단순 파일 I/O뿐만 아니라 데이터베이스 트랜잭션의 잔액 조회 후 인출(Double Spending), 메모리 플래그 검사 후 포인터 역참조 등 동시성 전반에 걸쳐 광범위하게 발생.

## Ⅲ. TOCTOU(Time Of Check To Time Of Use)의 세부 구성 요소 및 비교 분석

| 비교 항목 | **TOCTOU** (경쟁 취약점) | **버퍼 오버플로우** (BOF) | **교착 상태** (Deadlock) |
| --- | --- | --- | --- |
| 발생 원인 | 검사 시점과 사용 시점의 시간차 및 원자성 결여 | 경계 검사 부실로 메모리 버퍼 초과 쓰기 | 다중 프로세스 간 상호 배제적 자원 대기 |
| 악용 기법 | 심볼릭 링크 바꿔치기, 동시성 스레드 레이스 | 스택 덮어쓰기, ROP(리턴 지향 프로그래밍) | 서비스 지연 또는 거부 유발 (DoS) |
| 보안 영향 | 권한 상승(Privilege Escalation), 임의 파일 덮어쓰기 | 원격 임의 코드 실행(RCE), 쉘 획득 | 시스템 교착 및 서비스 영구 정지 |
| 해결 원리 | 원자적 시스템 콜, 파일 디스크립터 기반 조작 | ASLR, DEP, 스택 카나리, 안전한 함수 | 자원 할당 순서 고정, 타임아웃, 점유 대기 방지 |
| 재현성 | 확률적(Non-deterministic, 경쟁 승리 필요) | 결정론적(공격 페이로드 주입 시 안정적으로 재현) | 동시성 타이밍에 따른 간헐적 발생 |

- TOCTOU는 경로명 기반의 비원자적 파일 시스템 조작에서 주로 기인하므로, 파일 경로 대신 이미 열려 있는 **파일 디스크립터** (File Descriptor) 기반 API를 사용하는 것이 근본 해법임.

## Ⅳ. TOCTOU(Time Of Check To Time Of Use)의 주요 한계점 및 해결 방안

- 공격 성공의 확률적 특성으로 인한 동적 탐지 및 재현의 어려움 :
  - 한계점 : 공격자가 파일 치환 경쟁에서 승리해야만 취약점이 트리거되므로 일반적인 단위 테스트나 동적 취약점 스캐너로 감지 불가능.
  - 해결 방안 : 소스코드 정적 분석(SAST) 도구를 통해 'access() -> open()'과 같은 안티 패턴을 정적 룰로 전수 스캔 및 사전 차단.
- 공용 임시 디렉토리(/tmp)의 본질적 멀티유저 공유 위험 :
  - 한계점 : 모든 로컬 사용자가 쓰기 권한을 가지는 공용 디렉토리 구조상 심볼릭 링크 공격 표면이 상시 노출.
  - 해결 방안 : 리눅스 커널의 'fs.protected_symlinks' 및 'fs.protected_hardlinks' sysctl 보안 파라미터를 활성화하여 타인 소유 디렉토리 내 링크 추적 원천 차단.
- 분산 클라우드 환경의 비동기 마이크로서비스 간 동시성 충돌 :
  - 한계점 : DB 레코드 잔액을 검사하고 차감하는 비동기 API 요청이 병렬 분산 인스턴스에서 동시 실행 시 이중 출금(Double Spending) 사고 발생.
  - 해결 방안 : 비관적 잠금(SELECT FOR UPDATE), 분산 락(Redis Redlock), 원자적 조건부 업데이트(Atomic CAS: Compare-And-Swap) 적용.

## Ⅴ. TOCTOU(Time Of Check To Time Of Use) 적용 및 발전을 위한 기술사적 제언

- 원자적(Atomic) 파일 생성 플래그 준수 : 'open(filepath, O_CREAT | O_EXCL, mode)' 플래그를 사용하여 파일이 존재하지 않을 때만 원자적으로 생성하도록 강제.
- 파일 디스크립터 기반 시스템 콜(fstat, fchmod, fchown) 전면 전환 : 경로명을 반복 사용하는 대신 최초 open() 성공 후 반환된 안전한 파일 디스크립터(fd)를 매개변수로 상태 검증 및 조작 수행.
- Linux O_TMPFILE 및 O_NOFOLLOW 플래그 채택 : 임시 파일 생성 시 파일시스템 네임스페이스에 노출되지 않는 고유 O_TMPFILE 플래그를 사용하고, 심볼릭 링크 열기를 거부하는 O_NOFOLLOW 플래그 적용.
