---
title: "가상화(Virtualization)"
author: "OpenAI Codex"
date: "2026-09-20T00:30:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "A · 기초 · 핵심"
extra:
  model: "OpenAI Codex"
  keyword_grade: "A"
  grade_basis: "04-computer-system canonical 목록 A"
  source_status: "학습핵심"
  source_history: "정보관리 공식 기출 미확인"
  priority: 96
  priority_note: "canonical A · 하이퍼바이저·가상머신 통합 토픽"
---

## 전체 로드맵 내 현재 위치

```text
[01 IT 전략] → [02 SW 공학] → [03 데이터] → [▶ 04 컴퓨터 시스템]
      → [05 네트워크] → [06 보안] → [07 최신기술] → [08 법규·정책]
```

과목 내 현재 키워드: 04 컴퓨터 시스템 → 가상화

## 큰 그림과 30초 인출

```text
 [VM A: App+Guest OS] [VM B: App+Guest OS]
           │                     │
           └───────┬─────────────┘
                   ▼
       [Hypervisor / VMM / Management]
          │ CPU │ Memory │ I/O │
                   ▼
             [Physical HW]

Type 1: HW→Hypervisor→VM / Type 2: HW→Host OS→Hypervisor→VM
```

```text
가상화 = 물리 자원을 논리 자원으로 추상화·분할·격리
구조 = VM + Hypervisor + Management + Physical Resource
기술 = CPU Trap/HW Assist, Memory Mapping, I/O Emulation·Pass-through
통제 = 격리·관리면·이미지·자원경합·백업·복구
```

## 예상문제

> 가상화의 개념·특징과 하이퍼바이저 구조 및 자원 가상화 원리를 설명하고, 컨테이너와 비교하여 도입 고려사항을 제시하시오.

## Ⅰ. 개요 ───── 정의·목적

가상화는 **물리 컴퓨팅 자원을 추상화하여 복수의 논리 실행환경에 할당하고, 하이퍼바이저가 접근을 중재해 격리·공유·이동성을 제공하는 기술**이다.

| 목적 | 내용 |
|---|---|
| 통합 | 유휴 물리 자원을 논리적으로 배분 |
| 격리 | VM별 장애·보안 경계 형성 |
| 민첩성 | 이미지 기반 배포·복제·이동 |
| 운영성 | 중앙 프로비저닝·계측·회수 |

## Ⅱ. 특징 ───── 추상화·격리·캡슐화

| 특징 | 의미 | 유의점 |
|---|---|---|
| 추상화 | HW 차이를 가상 자원으로 표현 | 기능·성능 차이 검증 |
| 격리 | VM별 주소·장치·권한 분리 | 하이퍼바이저 취약점 |
| 캡슐화 | VM 상태를 이미지·메타데이터로 관리 | 이미지·스냅샷 확산 |
| 자원 공유 | CPU·메모리·I/O를 스케줄링 | Noisy Neighbor |
| 이동성 | 물리 호스트 간 이전 지원 가능 | 공유 스토리지·호환성 |

## Ⅲ. 구조 ───── Type 1·Type 2와 관리면

```text
Type 1                              Type 2
┌────── VM ──────┐                  ┌────── VM ──────┐
├── Hypervisor ──┤                  ├── Hypervisor ──┤
├── Physical HW ─┤                  ├──── Host OS ───┤
└────────────────┘                  ├── Physical HW ─┤
                                    └────────────────┘

Management Plane ─ API·IAM·Image·Network·Storage·Monitoring
```

| 자원 | 원리 | 대표 통제 |
|---|---|---|
| CPU | 특권 명령 중재, HW 지원, vCPU 스케줄 | Overcommit·Affinity |
| 메모리 | Guest→Host→Physical 주소 매핑 | 격리·Ballooning 정책 |
| I/O | 에뮬레이션·준가상 드라이버·직접 할당 | 성능과 이동성 절충 |
| Network | vNIC·vSwitch·Overlay | 세그먼트·정책 |
| Storage | 가상 Disk·Volume·Snapshot | 일관 백업·수명주기 |

## Ⅳ. 동작 ───── 생성부터 폐기까지

```text
① 이미지 검증 → ② VM 정의(vCPU·RAM·Disk·NIC)
 → ③ 자원 매핑 → ④ Guest 부팅 → ⑤ 스케줄·중재
 → ⑥ 계측·이동·백업 → ⑦ 안전한 폐기
```

CPU·메모리·I/O 경로마다 추상화 비용과 격리 수준이 다르므로 종단 워크로드로 측정한다.

## Ⅴ. 비교 ───── VM·컨테이너

| 구분 | VM | 컨테이너 |
|---|---|---|
| 격리 단위 | Guest OS 포함 VM | 호스트 커널 공유 프로세스 |
| 이미지 | OS 포함, 상대적으로 큼 | App·의존성 중심 |
| 기동 | Guest 부팅 필요 | 프로세스 기동 중심 |
| 커널 선택 | VM별 가능 | 호스트 커널 제약 |
| 적합 | 강한 격리·이종 OS·레거시 | 빠른 배포·마이크로서비스 |
| 공통 통제 | 이미지 공급망, 자원 제한, 네트워크 분리, 관측 |

## Ⅵ. 고려 ───── 보안·성능·운영 통제

| 문제 | 원인 | 대응 | 검증 |
|---|---|---|---|
| VM Escape | 하이퍼바이저·장치 취약점 | 최소 기능, 패치, 격리 등급 | 취약점·침투 시험 |
| 관리면 탈취 | 고권한 API 집중 | MFA, 최소권한, 별도 관리망 | 권한·감사 로그 |
| 자원 경합 | Overcommit·공유 I/O | 예약·한도·QoS·용량 계획 | P95 지연·Steal |
| 이미지 오염 | 장기 미패치·출처 불명 | Golden Image, 서명, SBOM | 이미지 준수율 |
| 스냅샷 오해 | 메모리·애플리케이션 정합성 | 앱 일관 백업·복구 시험 | RPO·RTO 달성 |
| 종속성 | 전용 포맷·관리 API | 표준 포맷 검토, Exit Plan | 이전 리허설 |

NIST는 하이퍼바이저 보안뿐 아니라 VM 네트워크 분리·트래픽 통제를 별도 설계 대상으로 본다.

## Ⅶ. 결론 ───── 자원 효율보다 격리와 관리성 우선

가상화는 물리 자원 통합 수단을 넘어 클라우드의 격리·자동화 기반이다. 도입 시 **자원 경합, 관리면, 이미지 공급망, 애플리케이션 일관 복구**를 함께 통제해야 한다.

## 1교시 10점 발췌

```text
가상화는 물리 자원을 추상화하여 복수 논리 환경에 할당하고
Hypervisor가 CPU·Memory·I/O 접근을 중재하는 기술이다.

구조: VM → Hypervisor → Physical HW + Management Plane
특징: 추상화·격리·캡슐화·공유·이동성
고려: Escape·관리면·Noisy Neighbor·Image·정합 백업
```

## 공식 검증 출처

- [NIST SP 800-125 — Full Virtualization Security](https://csrc.nist.gov/pubs/sp/800/125/final)
- [NIST SP 800-125A Rev.1 — Virtual Network Security](https://csrc.nist.gov/pubs/sp/800/125/a/r1/final)

## 답안 체크

- [ ] Type 1·Type 2를 계층도로 구분했는가
- [ ] CPU·메모리·I/O 가상화를 각각 설명했는가
- [ ] VM과 컨테이너의 커널 격리 차이를 썼는가
- [ ] 근거 없는 이용률·오버헤드 수치를 제거했는가

## 연결 토픽

- [서버리스 컴퓨팅](./003_serverless_computing/)
- [멀티클라우드](./009_multi_cloud/)
- [스레드](./010_thread/)
