---
title: "안드로이드(Android)"
author: "Gemini 3.8 Flash"
date: "2026-09-24T21:00:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  label: "118. 안드로이드(Android)"
  order: 118
  badge:
    text: "응용"
extra:
  keyword_grade: "응용"
  model: "GPT-6"

---

## 지식 로드맵 내 현재 위치

컴퓨터 시스템 및 네트워크 → 모바일 운영체제 → Android 플랫폼

## 30초 인출

- 본질: Android는 Linux 기반 커널·런타임·프레임워크·앱으로 구성된 모바일 소프트웨어 플랫폼
- 메커니즘: 앱이 프레임워크 API를 호출하면 권한 경계를 거친 시스템 서비스가 Binder·HAL을 통해 장치 기능을 제공
- 통찰: 한계: 앱 API만 보면 프로세스·권한·장치 구현 차이를 놓침 → 방안: Binder·서비스·HAL 경계를 따라 호출과 실패를 검증한다.

<details>
<summary>핵심 용어</summary>

- **Android** : Linux 커널 기반의 오픈소스 모바일 소프트웨어 플랫폼
- **ART (Android Runtime)** : Android 앱 코드를 실행하는 런타임 환경
- **HAL (Hardware Abstraction Layer)** : 하드웨어 기능을 상위 프레임워크에 표준 인터페이스로 제공하는 계층
- **Binder IPC (Binder Interprocess Communication)** : Android 프로세스·서비스 사이의 프로세스 간 통신 메커니즘
- **Zygote** : 앱 프로세스 생성에 활용되는 Android 시스템 프로세스

</details>

---
## 2~4교시 예상문제 (25점)

> Android 플랫폼의 계층 구조와 주요 동작을 설명하고, 앱 안정성·하드웨어 추상화 관점의 운영 고려사항을 제시하시오. (예상)

---
## 2~4교시 25점 답안

### Ⅰ. Android의 개요

| 구분 | 핵심 |
|---|---|
| 정의 | **Android는** Linux 커널 기반의 오픈소스 모바일 소프트웨어 플랫폼 |
| 목적 | 다양한 장치에서 앱 실행·시스템 서비스·하드웨어 접근 제공 |

### Ⅱ. Android 플랫폼의 특징

| 특징 | 의미 |
|---|---|
| 계층형 API | 앱은 하드웨어를 직접 제어하지 않고 프레임워크를 이용 |
| 프로세스·권한 격리 | 앱별 실행 경계와 시스템 서비스 접근 조건을 분리 |
| 장치 추상화 | HAL 계약으로 장치별 구현을 상위 기능에서 분리 |

### Ⅲ. 플랫폼 체계·동작 프로세스

**핵심 계층 프레임**

```text
사용자·시스템 앱 → Java/Kotlin 프레임워크 API
                 → 시스템 서비스 ↔ ART·네이티브 라이브러리
                 → Binder IPC·HAL → Linux 커널·드라이버
                 → 장치 하드웨어
```

**하위 메커니즘: 카메라 등 장치 기능 호출**

```text
앱 API 요청 → 권한 확인 → Binder로 시스템 서비스 호출
            → HAL 인터페이스 → 제조사 장치 구현·드라이버
            → 결과를 서비스·Binder 경유해 앱에 반환
```

**하위 메커니즘: 앱 프로세스 재생성**

```text
자원 압박으로 프로세스 종료 → 앱 상태 저장분 확인
                          → 프로세스·컴포넌트 재생성 → 상태 복구
```

### Ⅳ. 주요 경계의 역할 비교

| 경계 | 역할 | 확인할 문제 |
|---|---|---|
| ART·앱 프로세스 | 앱 코드 실행·생명주기 | 종료 후 상태 복구 |
| Binder·서비스 | 프로세스 간 요청·권한 처리 | 호출 실패·전송 부담 |
| HAL·드라이버 | 공통 인터페이스와 장치 구현 연결 | 제조사별 호환성 |

### Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 자원 압박으로 앱 프로세스가 종료될 수 있음 | 중요 상태를 저장하고 재생성 경로 시험 |
| Binder IPC 전송 크기·성능 제약 | 큰 데이터는 파일·URI 등 참조로 전달 |
| 장치별 HAL 구현이 다를 수 있음 | 표준 API 계약과 지원 장치별 회귀시험 |

### Ⅵ. 제언

동일한 앱 API라도 장치 구현·OS 버전·프로세스 상태에 따라 결과가 달라진다. **지원 장치 범위를 먼저 정하고**, 권한 거절·IPC 실패·프로세스 재생성·HAL 동작을 실제 기기에서 함께 검증해야 한다.

## 출제 이력과 검증 출처

- [Android platform architecture](https://developer.android.com/guide/platform): 플랫폼 계층·ART·HAL
- [Android Binder overview](https://source.android.com/docs/core/architecture/ipc/binder-overview): Binder IPC
