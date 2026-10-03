---
title: "측면 이동(Lateral Movement)"
author: "Antigravity"
date: "2026-10-01T23:50:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 측면 이동(Lateral Movement)의 개요

- 개념 : 공격자가 최초 침투한 단말(피싱 감염 PC 등)에서 멈추지 않고, 네트워크 내부를 정찰하고 **자격증명**을 탈취하여 최종 목표인 핵심 서버(AD DC, 고객 DB)로 이동해 나가는 침해 확산 단계.
- 배경 및 필요성 : 경계 방화벽을 뚫고 내부망에 침투한 공격자가 로컬 관리자 **권한 상승** 및 **자격증명 탈취**를 통해 핵심 데이터베이스와 **도메인 컨트롤러** (DC)로 침투를 확대하는 전사 마비 피해를 조기에 격리·차단하기 위해 출현함.
- 핵심 목적 : 초기 침투 지점의 격리 방어를 무력화하고, 전사 권한(도메인 관리자) 탈취 및 랜섬웨어 전사 배포를 위한 횡적 장악 거점 확보.

## Ⅱ. 측면 이동(Lateral Movement)의 핵심 아키텍처 및 동작 메커니즘

측면 이동(Lateral Movement)은(는) 신뢰할 수 있는 보안 구조와 표준화된 절차를 기반으로 동작하며, 세부적인 아키텍처와 구성요소 간의 상호작용 메커니즘은 다음과 같음.

```text
[ 1. 최초 침투 (Initial Access) ] ── 일반 사용자 PC 악성코드 감염
       │
       ▼
[ 2. 내부 정찰 (Discovery) ] ────── AD 쿼리(BloodHound), 네트워크 포트 스캔
       │
       ▼
[ 3. 자격증명 탈취 (Credential Access) ]
       ├── LSASS 메모리 덤프 (Mimikatz) ──▶ NTLM Hash / Kerberos Ticket 획득
       └── SAM 레지스트리 탈취 ──────────▶ 로컬 관리자 비밀번호 해시 추출
       │
       ▼
[ 4. 측면 이동 실행 (Lateral Movement) ]
       ├─ Pass-the-Hash (PtH) ──────────▶ 파일 서버 (SMB 445) 무인증 로그인
       ├─ Pass-the-Ticket (PtT) ────────▶ 결제 서버 (Kerberos 포트 88) 사칭
       └─ WMI / WinRM 원격 명령어 실행 ──▶ 백업 서버에 악성 페이로드 주입
       │
       ▼
[ 5. 최종 목표 장악 (Domain Controller / DB 암호화 및 데이터 유출) ]
```

- **1. 내부 정찰** : 네트워크 토폴로지, 활성 호스트, AD 도메인 신뢰 관계 탐색 (BloodHound, AdFind, net view).
- **2. 자격증명 탈취** : 메모리 내 로그인 세션 정보 및 Kerberos 티켓 추출 (Mimikatz, Procdump, LSASS 프로세스).
- **3. 자격증명 재사용** : 평문 복호화 없이 해시나 티켓으로 원격 시스템 인증 통과 (Pass-the-Hash, Golden/Silver Ticket).
- **4. 원격 명령 실행** : 관리 프로토콜을 경유하여 타깃 시스템에 셸 및 악성코드 실행 (SMB (445), WMI (135), RDP (3389)).
- **5. 거점 영속화** : 대상 시스템에 서비스 등록 또는 작업 스케줄러 등록 (schtasks, sc create, 레지스트리 Run).

## Ⅲ. 측면 이동(Lateral Movement)의 세부 구성 요소 및 비교 분석

| 구분 | **Pass-the-Hash** (PtH) | **Pass-the-Ticket** (PtT) | 원격 서비스 악용 (RDP / WMI) |
|---|---|---|---|
| 탈취 대상 자격증명 | NTLM 암호 해시 (NT Hash) | Kerberos TGT / TGS 티켓 | 탈취된 계정 ID / 평문 패스워드 |
| 인증 프로토콜 | NTLM 인증 프로토콜 | Kerberos 인증 프로토콜 | RDP(3389), WMI/RPC(135), SMB(445) |
| 공격 메커니즘 | 해시값을 NTLM Challenge-Response에 직접 주입 | 탈취한 티켓을 메모리에 삽입(Inject)하여 접근 | 정상 GUI/CLI 세션을 원격 생성하여 제어 |
| 탐지 지점 | 비정상 NTLM 인증 이벤트(ID 4624 Type 3) | 비정상 서비스 티켓 요청(이벤트 ID 4769) | 원격 로그인 로그, 비정상 원격 프로세스 트리 |
| 대표 방어 기술 | NTLM v1 비활성화, Windows LAPS | Kerberos 보호(Protected Users), 짧은 TGT 수명 | 원격 포트 차단, Bastion Host, ZTNA |

- 측면 이동(Lateral Movement)은(는) 상기 핵심 비교 지표와 아키텍처 구성을 바탕으로 보안 위협에 대한 방어 효과성을 극대화하며, 기존 레거시 통제 기법 대비 우수한 신뢰성과 운영 효율성을 제공함.

## Ⅳ. 측면 이동(Lateral Movement)의 주요 한계점 및 해결 방안

- 한계점 : 내부 서브넷 간 통제가 없는 **평면 네트워크** (Flat Network) 환경으로 인해 1대 단말 감염 시 동일 대역 전체가 무방비 노출.
  - 해결 방안 : **소프트웨어 정의 경계** (SDP) 및 하이퍼바이저 기반 마이크로 세그멘테이션(Micro-segmentation)을 적용하여 호스트 간(East-West) 통신 원천 격리.
- 한계점 : 도메인 내 다수 워크스테이션에 동일한 로컬 관리자(Administrator) 암호가 설정되어 있어 단 1회 덤프로 전사 장악.
  - 해결 방안 : Windows LAPS(Local Administrator Password Solution)를 의무 도입하여 엔드포인트별 고유 난수 암호 강제 부여 및 주기적 자동 회전.
- 한계점 : WMI, PowerShell, RDP 등 정상 시스템 관리 도구(LOLBins)를 악용하므로 단순 포트 차단 시 사내 정상 IT 운영 마비 초래.
  - 해결 방안 : EDR 기반 **부모-자식 프로세스 인과관계** (Parent-Child Tree) 행위 분석을 도입하고 시스템 관리 접속은 MFA가 강제된 전용 **점프 호스트** (Bastion)만 허용.

## Ⅴ. 측면 이동(Lateral Movement) 적용 및 발전을 위한 기술사적 제언

- **마이크로 세그멘테이션** (East-West 통신 차단) 체계 도입 : 마이크로 세그멘테이션 (East-West 통신 차단) 기술을 적극 적용하여 보안 취약점을 차단하고 시스템 신뢰성을 보장해야 함.
- **Windows LAPS 및 Credential Guard** 체계 도입 : Windows LAPS 및 Credential Guard 기술을 적극 적용하여 보안 취약점을 차단하고 시스템 신뢰성을 보장해야 함.
- **EDR 기반 실시간 프로세스 체인 이상 감시** 체계 도입 : EDR 기반 실시간 프로세스 체인 이상 감시 기술을 적극 적용하여 보안 취약점을 차단하고 시스템 신뢰성을 보장해야 함.
