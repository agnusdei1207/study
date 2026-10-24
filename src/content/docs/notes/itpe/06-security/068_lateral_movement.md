---
title: "측면 이동(Lateral Movement)"
author: "agnusdei1207"
date: "2026-10-24T23:01:31+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "서브"
extra:
  keyword_grade: "서브"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 측면 이동(Lateral Movement), 자격증명, 권한 상승, 도메인 컨트롤러, 평면 네트워크
- Pass-the-Hash, Pass-the-Ticket, NTLM, Kerberos, LSASS, Mimikatz, BloodHound
- Windows LAPS, LOLBins, EDR, 점프 호스트, 마이크로 세그멘테이션

## Ⅰ. 측면 이동(Lateral Movement)의 개요

- 핵심 요약 : 최초 침투 이후 내부망에서 자격증명을 빼앗아 핵심 서버로 확산하는 침해 단계.
- 개념 : 공격자가 최초 침투 단말에 머무르지 않고 내부망을 정찰하며 자격증명을 탈취해 핵심 서버로 옮겨 가는 **측면 이동** (Lateral Movement).
- 배경 및 필요성 : 경계 방화벽을 통과한 공격자가 로컬 관리자 권한을 얻고 Active Directory(AD) 도메인 컨트롤러(DC, Domain Controller)와 고객 데이터베이스까지 도달하면 전사 업무가 마비되므로, 내부 확산을 조기에 차단하는 방안이 필요해짐.
- 주요 목적 : 확산 경로 차단, 도메인 관리자 권한 탈취 방지, 침해 탐지 시간 단축.

## Ⅱ. 측면 이동(Lateral Movement)의 특징 및 장점

- 핵심 요약 : 정상 관리 도구와 인증 체계를 악용하기 때문에, 탐지와 차단을 동시에 어렵게 만드는 구조.

1. 정상 도구 악용 : WMI, PowerShell, RDP 같은 시스템 관리 도구를 사용 → 악성 행위가 정상 운영과 섞여 탐지가 지연.
2. 자격증명 재사용 : 평문 암호 대신 NTLM(NT LAN Manager) 해시나 Kerberos 티켓을 제시 → 암호를 몰라도 원격 인증 통과.
3. 신뢰 관계 악용 : AD 도메인의 신뢰 구조를 따라 이동 → 한 번 장악된 권한이 여러 시스템으로 확산.
4. 거점 영속화 : 서비스나 예약 작업 등록 → 재부팅 이후에도 침입 상태가 유지.

## Ⅲ. 측면 이동(Lateral Movement)의 구조 (흐름)

- 핵심 요약 : 정찰, 자격증명 탈취, 재사용, 원격 실행, 영속화로 이어지는 다섯 단계 흐름.
- **내부 정찰** (Discovery) : 네트워크 구조, 활성 호스트, AD 신뢰 관계 탐색 (BloodHound 등 분석 도구 활용).
- **자격증명 탈취** (Credential Access) : LSASS(Local Security Authority Subsystem Service) 메모리 덤프와 Mimikatz 같은 도구로 로그인 세션과 티켓 추출.
- **자격증명 재사용** (Credential Reuse) : 복호화 없이 해시나 티켓을 제시해 원격 시스템 인증 통과.
- **원격 명령 실행** : SMB(Server Message Block, 445), WMI(Windows Management Instrumentation, 135), RDP(Remote Desktop Protocol, 3389)로 악성 코드 실행.
- **거점 영속화** : 서비스 등록, 작업 스케줄러, 레지스트리 Run 키 등록.

```text
[ 측면 이동 흐름 ]

최초 침투 (피싱 감염 PC)
   ↓
내부 정찰 (AD 쿼리, 포트 스캔)
   ↓
자격증명 탈취 (LSASS 메모리)
   ↓
자격증명 재사용 (해시·티켓 제시)
   ↓
핵심 서버 장악 (DC, DB 유출)
```

```text
[ 자격증명 재사용 경로 ]

NTLM 해시 탈취 → 해시 직접 인증
Kerberos 티켓 탈취 → 티켓 메모리 삽입
          ↓
원격 시스템 무인증 접근
```

## Ⅳ. 측면 이동(Lateral Movement)의 비교

- 핵심 요약 : 해시 재사용, 티켓 재사용, 원격 서비스 악용은 탈취 대상과 탐지 지점이 달라 방어책도 달라지는 구조.

| 비교 축 | Pass-the-Hash(PtH) | Pass-the-Ticket(PtT) | 원격 서비스 악용 (RDP, WMI) |
| --- | --- | --- | --- |
| 탈취 대상 | NTLM 암호 해시 | Kerberos TGT, TGS 티켓 | 탈취된 계정과 평문 암호 |
| 인증 프로토콜 | NTLM | Kerberos | RDP(3389), WMI·RPC(135), SMB(445) |
| 공격 방식 | 해시를 NTLM 인증 과정에 직접 주입 | 탈취한 티켓을 메모리에 삽입 | 정상 원격 세션을 열어 제어 |
| 탐지 지점 | 비정상 NTLM 로그온 이벤트(ID 4624, 로그온 유형 3) | 비정상 서비스 티켓 요청(이벤트 ID 4769) | 원격 로그인 기록, 비정상 원격 프로세스 트리 |
| 대표 방어 기술 | NTLM 사용 축소, Windows LAPS(Local Administrator Password Solution) | Kerberos 보호(Protected Users), 짧은 TGT 수명 | 원격 포트 통제, 점프 호스트, ZTNA(Zero Trust Network Access) |

- 선택 기준 : 탈취 대상(해시, 티켓, 평문 계정)에 따라 탐지 로그와 차단 정책을 나눠 설계.

## Ⅴ. 측면 이동(Lateral Movement)의 한계와 방안

- 핵심 요약 : 평면 네트워크, 공통 관리자 암호, 정상 도구 악용이라는 세 한계를 경계 분할, 암호 고유화, 행위 기반 탐지로 통제하는 구조.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 평면 네트워크 (Flat Network) | 서브넷 간 통제가 없어 한 대가 감염되면 같은 대역 전체가 노출 | 소프트웨어 정의 경계(SDP, Software-Defined Perimeter)와 마이크로 세그멘테이션으로 동서 방향 통신 제한 | 허용되지 않은 내부 통신 차단 건수 |
| 공통 로컬 관리자 암호 | 다수 워크스테이션이 같은 관리자 암호를 써서 한 번의 덤프로 전사 장악 | Windows LAPS 도입으로 단말마다 고유한 암호를 부여하고 주기적으로 자동 교체 | LAPS 적용 단말 비율 |
| 정상 도구 악용 (LOLBins, Living Off the Land Binaries) | 단순 포트 차단은 정상 IT 운영까지 마비시킴 | EDR(Endpoint Detection and Response)의 부모-자식 프로세스 인과 분석 적용, 관리 접속은 MFA(Multi-Factor Authentication)가 강제된 점프 호스트(Bastion)로만 허용 | 비정상 원격 프로세스 탐지 건수 |

## Ⅵ. 측면 이동(Lateral Movement)에 대한 기술사적 제언

- 핵심 요약 : 내부망을 신뢰 영역으로 보지 않는 전제와 관리 권한의 계층 분리를 조직 운영 원칙으로 정착.

1. 조직은 내부망 전체를 신뢰하지 않는 제로 트러스트 원칙을 채택하고, 신원과 단말 상태를 함께 검증하는 접근 정책을 전사 표준으로 정한다.
2. 도메인 관리 권한을 계층별로 나누는 관리 계층 분리 모델을 도입해, 도메인 관리자 계정이 일반 단말에 로그온하지 못하도록 운영 절차로 고정한다.
3. 보안관제 조직은 내부 이동 행위를 침해 시나리오 단위로 탐지 규칙에 반영하고, 정기 모의 침투 점검으로 탐지 공백을 측정하는 체계를 마련한다.

## Ⅶ. 결론

- 핵심 요약 : 측면 이동은 정상 관리 도구와 자격증명 재사용을 노려 내부 확산을 일으키므로, 확산 경로의 격리가 방어의 핵심.
- 시사점 : 평면 네트워크 축소, 자격증명 보호, 행위 기반 탐지를 함께 갖출 때 침해가 초기 단말에서 멈추는 구조가 만들어짐.
