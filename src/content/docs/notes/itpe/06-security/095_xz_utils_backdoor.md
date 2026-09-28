---
title: "XZ Utils 백도어 (CVE-2024-3094)"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  order: 95
  label: "095. XZ Utils 백도어 (CVE-2024-3094)"
  badge:
    text: "기초"
    variant: note
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"

---

## 지식 로드맵 내 현재 위치

소프트웨어 공급망 보안 → 오픈소스 신뢰 체인 위협 → XZ Utils 백도어 (CVE-2024-3094)

## 30초 인출

- **본질:** 2년 이상의 장기 잠복 사회공학 기법으로 오픈소스 메인테이너 권한을 획득한 공격자가 공식 배포 tarball의 빌드 스크립트를 변조하여 OpenSSH 데몬(sshd)에 원격 코드 실행(RCE) 백도어를 주입한 공급망 침해 참사.
- **메커니즘:** Git 저장소에는 정상 테스트 파일로 위장 → 릴리스 tarball 패키징 시 악성 m4 매크로와 셸 스크립트 결합 → liblzma 컴파일 시 IFUNC를 통해 OpenSSH의 `RSA_public_decrypt` 함수를 후킹하여 임의 명령 실행 백도어 활성화.
- 통찰: Git 소스코드 검토만으로는 릴리스 빌드 산출물 변조를 적발할 수 없으므로 재현 가능한 빌드(Reproducible Builds), SLSA 기반 출처 증명, 메인테이너 다자 승인 거버넌스 확립 필수.

<details><summary>핵심 용어</summary>

- **XZ Utils (liblzma)**: 리눅스 전반에서 널리 쓰이는 무손실 데이터 압축 라이브러리 및 유틸리티.
- **CVE-2024-3094**: XZ Utils 버전 5.6.0 및 5.6.1의 배포 tarball에 포함된 백도어에 부여된 CVSS 10.0 만점의 치명적 취약점.
- **IFUNC(Indirect Function)**: GNU C 라이브러리(glibc)의 기능으로, 런타임에 CPU 아키텍처에 가장 적합한 최적화 함수 구현을 동적으로 바인딩하는 메커니즘.
- **릴리스 Tarball(Release Tarball)**: Git 리포지토리의 소스 외에 `autotools`로 사전 생성된 `configure` 스크립트를 포함하여 배포되는 압축 아카이브.
- **재현 가능한 빌드(Reproducible Builds)**: 동일한 소스코드와 빌드 환경이 주어지면 바이트 단위로 100% 일치하는 바이너리를 생성할 수 있도록 보장하는 빌드 검증 기법.
</details>

---

## 2~4교시 예상문제 (25점)

> 오픈소스 소프트웨어 공급망의 구조적 취약성을 드러낸 XZ Utils 백도어(CVE-2024-3094)의 침투 및 실행 메커니즘을 사회공학, 빌드 파이프라인, 동적 링킹 관점에서 분석하고, 오픈소스 공급망 신뢰 체계(SLSA, SBOM, 재현 가능한 빌드) 관점에서의 엔지니어링 방어 방안을 제시하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 리눅스 배포판의 표준 압축 라이브러리(liblzma) 공식 릴리스 tarball에 은닉되어 OpenSSH 데몬을 하이재킹하고 사전 인증 RCE를 허용했던 고도화된 공급망 백도어 |
| 목적 | 전 세계 엔터프라이즈 리눅스 서버의 원격 접속 통로인 SSH 데몬에 은밀한 백도어를 구축하여 국가급 사이버 첩보 및 임의 시스템 제어권 획득 |

## Ⅱ. XZ Utils 백도어(CVE-2024-3094)의 핵심 특징

| 특징 | 세부 공격 내용 | 엔지니어링 파급 효과 |
|---|---|---|
| 장기 사회공학 침투 | 가상 계정(Jia Tan)을 생성하여 수년간 성실히 기여한 후 단독 유지관리자 권한 인수 | 단일 개발자(1인 메인테이너) 번아웃 프로젝트의 구조적 취약점 입증 |
| Git 소스와 Tarball 괴리 | 공개된 Git 리포지토리에는 악성 코드를 올리지 않고 배포용 .tar.gz에만 악성 셸 스크립트 은닉 | GitHub 소스코드 정적 분석(SAST) 및 보안 감사 전면 무력화 |
| 빌드 타임 스테가노그래피 | 테스트용 바이너리 파일(`.xz`) 속에 다단계로 암호화/압축된 백도어 오브젝트 은닉 | 일반적인 코드 리뷰 과정에서 단순 테스트 데이터로 오인 |
| IFUNC 동적 링킹 악용 | glibc의 IFUNC 해석 시점에 주입되어 주 프로그램(sshd) 시작 전 메모리 후킹 완료 | 메모리 보호 및 기존 안티바이러스의 정적 함수 시그니처 우회 |
| 간접 의존성 연쇄 체인 | sshd -> libsystemd -> liblzma로 이어지는 불필요한 라이브러리 링크 구조 악용 | 최소 의존성 설계 원칙 부재로 인한 공격 표면 확장 증명 |

## Ⅲ. 백도어 주입 및 실행 메커니즘 아키텍처

```text
[ 1. 소스 및 빌드 조작 단계 ]
Git 저장소 (정상 소스 + 위장된 테스트 파일 bad-3-corrupt_lzma2.xz)
       │
       ▼
공식 배포 Tarball 생성 시 악성 m4 매크로 및 configure 주입
       │
       ▼
[ 2. 배포판 패키징 빌드 단계 (Debian/RPM Build) ]
배포판 빌드 러너에서 configure 실행 ──▶ x86-64 리눅스 GCC 환경 검사
       │
       ▼
조건 충족 시 테스트 파일에서 복호화된 악성 liblzma_la-crc64-fast.o 추출 및 컴파일 링크
       │
       ▼
[ 3. 호스트 시스템 로드 및 후킹 단계 ]
OpenSSH sshd 데몬 실행 ──▶ libsystemd 로드 ──▶ 악성 liblzma.so 동적 로드
       │
       ▼
glibc IFUNC 리졸브 실행: crc64_fast() 초기화 단계에서 메모리 조작
       │
       ▼
GOT(Global Offset Table) 내 RSA_public_decrypt 함수 주소를 공격자 함수로 변조
       │
       ▼
[ 4. 원격 백도어 공격 트리거 단계 ]
공격자가 조작된 서명 키를 포함한 SSH 접속 요청 전송 ──▶ 인증 없이 백도어 실행 (RCE)
```

| 공격 계층 | 기술적 상세 동작 | 악용된 기술 메커니즘 |
|---|---|---|
| 빌드 스크립트 | `m4/build-to-host.m4` 내 난독화된 셸 스크립트가 빌드 환경(x86_64, Linux, GCC) 검사 | Autotools 빌드 파이프라인 |
| 페이로드 은닉 | 테스트 케이스 디렉터리의 정상 위장 파일에서 `sed`와 `tr` 명령으로 바이너리 추출 | 스테가노그래피 및 난독화 |
| 메모리 인터셉트 | 심볼 해석 시점(Dynamic Symbol Resolution)에 ELF 심볼 테이블 가로채기 | GNU IFUNC(Indirect Functions) |
| 인증 우회 후킹 | OpenSSH의 인증 확인 함수인 `RSA_public_decrypt`의 포인터를 백도어 루틴으로 교체 | GOT(Global Offset Table) 오염 |
| 페이로드 실행 | 수신된 SSH 인증 패킷의 페이로드가 공격자 ED448 개인키로 서명된 경우 명령 셸 실행 | 비대칭 암호 서명 기반 인증 |

## Ⅳ. 일반 코드 취약점 vs XZ Utils 빌드 파이프라인 공격 비교

| 비교 항목 | 일반 소스코드 취약점 (CWE-119 등) | XZ Utils 공급망 백도어 (CVE-2024-3094) |
|---|---|---|
| 결함의 성격 | 개발자의 실수나 부주의로 인한 버그 | 국가급 행위자가 의도적으로 설계한 악의적 백도어 |
| 코드 위치 | Git 리포지토리의 소스코드 파일(.c, .h) | 공식 배포 압축파일(tarball) 내 빌드 스크립트 및 테스트 바이너리 |
| 탐지 방법 | 정적 코드 분석 도구(SAST), 퍼징(Fuzzing) | Git과 Tarball 간 차이점(Diff) 검증, 재현 빌드 |
| 권한 획득 경로 | 외부 침투 또는 계정 피싱 | 수년간의 정상 기여를 통한 합법적 메인테이너 권한 위임 |
| 보안 영향 | 로컬 권한 상승 또는 서비스 거부(DoS) | 전 세계 리눅스 서버에 대한 무조건적 원격 루트 셸 장악 |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 오픈소스 프로젝트에서 Git 리포지토리 코드와 다운로드 배포물(tarball)의 일치 여부를 검증하지 않는 관행 | CI/CD 단계에서 소스 리포지토리로부터 직접 컴파일하는 재현 가능한 빌드(Reproducible Builds)를 의무화하고 Git-Tarball 간 SHA-256 및 Diff 검증 자동화 |
| 1인 메인테이너 프로젝트의 자원 고갈과 고립을 틈탄 사회공학적 기여(Social Engineering) 방어 불가 | OpenSSF 기반의 오픈소스 다자간 유지보수(Multi-Maintainer) 거버넌스를 정립하고, 크리티컬 프로젝트에 대한 재정 지원 및 서명키 다중 제어 강제 |
| SSH 데몬이 통지 기능 하나 때문에 libsystemd를 링크하고 연쇄적으로 압축 라이브러리(liblzma)까지 로드하는 비대한 의존성 구조 | 소프트웨어 최소 권한 원칙(Principle of Least Privilege)에 따라 sshd에서 libsystemd 의존성을 전면 분리하고 IPC 소켓 기반 비동기 통지로 아키텍처 단순화 |
| glibc의 IFUNC 기능이 보안 검증 없이 로딩 초기에 임의의 메모리 코드를 실행할 수 있는 구조적 맹점 | 컴파일러 보안 플래그(`-Wl,-z,now`, Full RELRO)를 강제 적용하여 GOT 영역을 읽기 전용으로 잠그고 런타임 심볼 하이재킹 차단 |

## Ⅵ. 제언

```text
[ 오픈소스 공급망 신뢰 체인 보호 모델 (SLSA 4단계) ]

+-------------------------+      +-------------------------+      +-------------------------+
|     1. 출처 증명        | ---> |     2. 재현 빌드        | ---> |     3. 최소 의존성      |
| (Sigstore / in-toto 서명|      | (바이트 단위 일치 검증) |      | (의존성 디커플링/Full RELRO)
+-------------------------+      +-------------------------+      +-------------------------+
```

| 추진 영역 | 엔지니어링 구현 과제 | 비즈니스 가치 |
|---|---|---|
| 빌드 무결성 | SLSA(Supply-chain Levels for Software Artifacts) Level 3 이상 달성 및 빌드 파이프라인 불변화 | 비인가 스크립트 주입 및 배포 아티팩트 변조 원천 봉쇄 |
| 의존성 거버넌스 | 배포판 패키징 시 Git Commit 태그 기반 자동 빌드 강제 및 서드파티 tarball 수동 반입 금지 | 소스 저장소와 배포 산출물 간의 괴리 100% 제거 |
| 시스템 하드닝 | OS 배포판 전반에 Full RELRO, BIND_NOW 링크 옵션 기본 강제화 | IFUNC 및 GOT 덮어쓰기 메모리 익스플로잇 무력화 |

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 (오픈소스 공급망 침해 위협 및 대책)
- Red Hat Security Advisory, Urgent Security Alert for Fedora Linux (CVE-2024-3094)
- CISA Alert on Compromised XZ Utils Library
- OpenSSF Best Practices for Open Source Maintainers and Reproducible Builds

## 연결 토픽

- 소프트웨어 공급망 보안(SLSA/SBOM)
- Shai-Hulud npm 웜
- EU CRA (사이버복원력법)
- CrowdStrike 대규모 장애
