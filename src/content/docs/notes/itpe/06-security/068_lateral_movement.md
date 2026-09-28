---
title: "측면 이동(Lateral Movement)"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  label: "068. 측면 이동(Lateral Movement)"
  badge:
    text: "서브"
    variant: note
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "서브"
---

## 지식 로드맵 내 현재 위치

정보보안 → 침해 대응 → 내부망 측면 이동(Lateral Movement: TA0008)

## 30초 인출

- **본질:** 공격자가 초기 침투 거점을 확보한 후, 내부망의 다른 시스템으로 접근 권한을 확장하고 최종 목표 자산(DC, DB 등)에 도달하기 위해 횡적으로 침투하는 공격 단계
- **메커니즘:** 내부 자산 정찰 → 자격증명 탈취(LSASS 덤프) → 자격증명 재사용(Pass-the-Hash / Ticket) → 원격 프로토콜 악용(RDP/WMI/SMB/SSH) → 목표 자산 장악
- 통찰: 평면 네트워크와 로컬 관리자 비밀번호 공유로 인한 연쇄 감염을 차단하기 위해 마이크로 세그멘테이션, Windows LAPS, 자격증명 보호(Credential Guard), ZTA 기반 지속적 검증 결합 필수

<details><summary>핵심 용어</summary>

- **측면 이동 (Lateral Movement, TA0008):** MITRE ATT&CK 전술 중 하나로, 네트워크 내 시스템 간을 이동하며 통제 범위를 넓히는 행위.
- **Pass-the-Hash (PtH):** 평문 비밀번호를 복호화하지 않고 NTLM 해시값을 그대로 인증 서버에 전송하여 세션을 획득하는 공격.
- **Pass-the-Ticket (PtT):** Kerberos TGT(티켓 발급 티켓)를 메모리에서 덤프하여 다른 시스템에 무단 접근하는 공격.
- **LOLBins (Living-off-the-Land Binaries):** 악성 바이너리 대신 OS 기본 탑재 정상 관리 도구(WMI, PowerShell, PsExec)를 악용하는 기법.
- **Windows LAPS:** 도메인 내 개별 단말의 로컬 관리자 비밀번호를 서로 다르게 무작위 생성하고 주기적으로 자동 회전시키는 솔루션.
- **마이크로 세그멘테이션(Micro-segmentation):** 동일 서브넷 내 호스트 간(East-West) 트래픽까지 소프트웨어 기반으로 세분화하여 격리하는 제로 트러스트 기술.

</details>

---

## 2~4교시 예상문제 (25점)

> 사이버 킬체인의 핵심 단계인 측면 이동(Lateral Movement)의 개념과 주요 공격 기법(Pass-the-Hash, Pass-the-Ticket, LOLBins)을 설명하고, 평면 네트워크 환경에서의 확산 한계 극복을 위한 마이크로 세그멘테이션 및 제로 트러스트(ZTA) 방어 전략을 제시하시오. (기출·제138회 3교시 5번)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | 공격자가 최초 침투한 단말(피싱 감염 PC 등)에서 멈추지 않고, 네트워크 내부를 정찰하고 자격증명을 탈취하여 최종 목표인 핵심 서버(AD DC, 고객 DB)로 이동해 나가는 침해 확산 단계 |
| 목적 | 초기 침투 지점의 격리 방어를 무력화하고, 전사 권한(도메인 관리자) 탈취 및 랜섬웨어 전사 배포를 위한 횡적 장악 거점 확보 |

## Ⅱ. 측면 이동의 주요 특징

| 특징 | 세부 내용 | 구현 요소 |
|---|---|---|
| 정상 관리 도구의 악용 (LotL) | 백신 탐지를 회피하기 위해 WMI, PowerShell, RDP, SMB 등 정상 윈도우 프로토콜 사용 | PsExec, WMI, WinRM |
| 자격증명 재사용 공격 | 침해 단말 메모리(LSASS)에서 관리자 해시/티켓을 덤프하여 타 시스템에 무인증 접근 | Mimikatz, NTLM/Kerberos |
| 내부 경계선 통제 취약점 악용 | 외부-내부(North-South) 방화벽은 견고하나 내부 간(East-West) 트래픽 통제가 전무한 구조 악용 | Flat Network (평면망) |
| 단계적 권한 상승과의 결합 | 일반 사용자 PC 탈취 $\rightarrow$ 로컬 관리자 탈취 $\rightarrow$ 도메인 관리자 권한 획득으로 연쇄 증폭 | 권한 에스컬레이션 체인 |

## Ⅲ. 측면 이동 공격 체계 및 단계별 실행 프로세스

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

| 단계 | 수행 작업 | 주요 악용 프로토콜 및 도구 |
|---|---|---|
| 1. 내부 정찰 | 네트워크 토폴로지, 활성 호스트, AD 도메인 신뢰 관계 탐색 | BloodHound, AdFind, net view |
| 2. 자격증명 탈취 | 메모리 내 로그인 세션 정보 및 Kerberos 티켓 추출 | Mimikatz, Procdump, LSASS 프로세스 |
| 3. 자격증명 재사용 | 평문 복호화 없이 해시나 티켓으로 원격 시스템 인증 통과 | Pass-the-Hash, Golden/Silver Ticket |
| 4. 원격 명령 실행 | 관리 프로토콜을 경유하여 타깃 시스템에 셸 및 악성코드 실행 | SMB (445), WMI (135), RDP (3389) |
| 5. 거점 영속화 | 대상 시스템에 서비스 등록 또는 작업 스케줄러 등록 | schtasks, sc create, 레지스트리 Run |

## Ⅳ. 측면 이동 주요 공격 기법 비교

| 구분 | Pass-the-Hash (PtH) | Pass-the-Ticket (PtT) | 원격 서비스 악용 (RDP / WMI) |
|---|---|---|---|
| 탈취 대상 자격증명 | NTLM 암호 해시 (NT Hash) | Kerberos TGT / TGS 티켓 | 탈취된 계정 ID / 평문 패스워드 |
| 인증 프로토콜 | NTLM 인증 프로토콜 | Kerberos 인증 프로토콜 | RDP(3389), WMI/RPC(135), SMB(445) |
| 공격 메커니즘 | 해시값을 NTLM Challenge-Response에 직접 주입 | 탈취한 티켓을 메모리에 삽입(Inject)하여 접근 | 정상 GUI/CLI 세션을 원격 생성하여 제어 |
| 탐지 지점 | 비정상 NTLM 인증 이벤트(ID 4624 Type 3) | 비정상 서비스 티켓 요청(이벤트 ID 4769) | 원격 로그인 로그, 비정상 원격 프로세스 트리 |
| 대표 방어 기술 | NTLM v1 비활성화, Windows LAPS | Kerberos 보호(Protected Users), 짧은 TGT 수명 | 원격 포트 차단, Bastion Host, ZTNA |

## Ⅴ. 측면 이동 차단의 한계와 방안

| 한계 | 방안 |
|---|---|
| 내부 서브넷 간 통제가 없는 평면 네트워크(Flat Network) 환경으로 인해 1대 단말 감염 시 동일 대역 전체가 무방비 노출 | 소프트웨어 정의 경계(SDP) 및 하이퍼바이저 기반 마이크로 세그멘테이션(Micro-segmentation)을 적용하여 호스트 간(East-West) 통신 원천 격리 |
| 도메인 내 수천 대 워크스테이션에 동일한 로컬 관리자(Administrator) 암호가 설정되어 있어 단 1회 덤프로 전사 장악 | Windows LAPS(Local Administrator Password Solution)를 의무 도입하여 엔드포인트별 고유 난수 암호 강제 부여 및 주기적 자동 회전 |
| WMI, PowerShell, RDP 등 정상 시스템 관리 도구(LOLBins)를 악용하므로 단순 포트 차단 시 사내 정상 IT 운영 마비 초래 | EDR 기반 부모-자식 프로세스 인과관계(Parent-Child Tree) 행위 분석을 도입하고 시스템 관리 접속은 MFA가 강제된 전용 점프 호스트(Bastion)만 허용 |

## Ⅵ. 제언

```text
[ 전통적 경계 보안망 (평면망) ]       [ 제로 트러스트 마이크로 세그멘테이션 ]
외곽 방화벽 통과 후 ──┐               ┌── 마이크로 세그멘테이션 (East-West 통신 차단)
내부 호스트 자유 접근 ┼─→ [ 전사 마비 ] ─┼── Windows LAPS 및 Credential Guard
공통 로컬 관리자 암호 ┘               └── EDR 기반 실시간 프로세스 체인 이상 감시
```

| 평가 영역 | 레거시 내부망 환경 | 제로 트러스트 방어 환경 | 향후 발전 방향 |
|---|---|---|---|
| 내부 트래픽 제어 | 통제 부재 (Any-Any 허용) | 호스트/프로세스 단위 격리 | eBPF 기반 초경량 커널 레벨 세그멘테이션 |
| 자격증명 방어 | 메모리 평문/해시 노출 | VBS 기반 메모리 가상화 격리 | 무시크릿(Secretless) FIDO2 패스키 전면 적용 |
| 사고 대응 속도 | 수일~수개월 잠복(Dwell Time) | 침투 즉시 단말 자동 격리 | SOAR 기반 비정상 횡적이동 세션 자동 킬(Kill) |

측면 이동은 침해 사고가 단순 감염을 넘어 전사적 대규모 랜섬웨어 피해로 확대되는 결정적 트리거이며, 네트워크 평면성을 제거하는 마이크로 세그멘테이션과 엔드포인트 자격증명 보호가 현대 내부망 보안의 필수 전략.

## 출제 이력과 검증 출처

- 정보관리기술사 제138회 3교시 5번 (IT 인프라 확장에 따른 사이버 위협: 측면 이동)
- 정보관리기술사 제126회 2교시 (사이버 킬체인 및 내부 횡적이동 기법과 대응 방안)
- MITRE ATT&CK Framework: Lateral Movement (TA0008)
- Microsoft Learn: Windows Local Administrator Password Solution (LAPS) Architecture
- CISA: Protecting Against Lateral Movement in Enterprise Networks
