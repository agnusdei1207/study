---
title: "Salt Typhoon / Volt Typhoon (LotL)"
author: "Antigravity"
date: "2026-03-31T00:00:00+09:00"
tags:
  - "notes-security"
sidebar:
  order: 92
  label: "092. Salt Typhoon / Volt Typhoon (LotL)"
  badge:
    text: "서브"
    variant: note
extra:
  keyword_grade: "서브"
  model: "Gemini 3.8 Flash"

---

## 지식 로드맵 내 현재 위치

위협 인텔리전스 → 국가 배후 APT 및 정상 도구 악용 → Salt Typhoon / Volt Typhoon (LotL)

## 30초 인출

- **본질:** 국가 지원 APT 그룹인 Volt Typhoon(핵심 인프라 사전 침투)과 Salt Typhoon(글로벌 통신망 도청)이 활용하는, 악성 파일 유포 대신 OS 내장 정상 도구를 악용하는 Living-off-the-Land(LotL) 공격 전술.
- **메커니즘:** 인터넷 노출 엣지 장비(방화벽/VPN) 취약점 침투 → 내장 도구(PowerShell, WMI, netsh) 기반 메모리 실행 및 측면 이동 → 유효 자격증명 탈취 및 정상 관리 트래픽 위장 통신.
- 통찰: 시그니처 백신 탐지가 무력화되므로 사용자·엔티티 행위 분석(UEBA)과 엣지 장비 제로 트러스트 접근 통제(ZTNA), 스크립트 블록 로깅 체계 구축 필수.

<details><summary>핵심 용어</summary>

- **LotL(Living-off-the-Land)**: 표적 시스템에 새로운 악성 파일을 생성하지 않고, OS 내장 유틸리티나 관리 도구(LOLBins)를 악용하여 탐지를 우회하는 공격 기법.
- **Volt Typhoon**: 미국 및 글로벌 핵심 기반시설(수도, 전력, 교통, 통신)에 장기 은닉하여 유사시 물리적 운영 중단 및 파괴를 노리는 국가 배후 공격 그룹.
- **Salt Typhoon**: 글로벌 주요 통신사(Telco) 및 인터넷 서비스 제공업체(ISP)의 백본 라우터를 침투하여 고위직 통신 도청 및 첩보를 수집하는 국가 배후 공격 그룹.
- **LOLBins(Living off the Land Binaries)**: Certutil, PowerShell, WMI, Bitsadmin 등 정상 관리 목적으로 제공되지만 공격자에 의해 악용되는 내장 바이너리.
- **UEBA(User and Entity Behavior Analytics)**: 정상 기준선(Baseline)을 학습하고 비정상적인 시간대, 비정상적인 명령 인자, 비정상적 트래픽을 탐지하는 머신러닝 분석.
</details>

---

## 2~4교시 예상문제 (25점)

> 국가 배후 지능형 지속 위협(APT) 그룹인 Volt Typhoon과 Salt Typhoon의 침해 목적 및 공격 전술을 비교 분석하고, Living-off-the-Land(LotL) 기법을 통한 보안 회피 메커니즘과 이를 방어하기 위한 엔지니어링 통제 방안을 제시하시오. (25점)

---

## 2~4교시 25점 답안

## Ⅰ. 개요

| 구분 | 핵심 |
|---|---|
| 정의 | OS 내장 관리 도구(PowerShell, WMI, netsh 등)와 유효한 관리자 자격증명을 악용하여 악성 바이너리 없이 표적망에 장기 잠복하는 LotL 기반 국가 배후 APT 위협 |
| 목적 | 전통적인 안티바이러스 및 파일 기반 EDR 탐지를 무력화하고, 중요 기반시설 파괴 준비(Volt) 및 통신 백본 도청(Salt)을 위한 은밀한 지속성(Persistence) 유지 |

## Ⅱ. Volt Typhoon vs Salt Typhoon 핵심 특징 비교

| 비교 항목 | Volt Typhoon (볼트 타이푼) | Salt Typhoon (솔트 타이푼) |
|---|---|---|
| 주 표적 인프라 | 통신, 에너지, 수도, 교통 등 핵심 기반시설(Critical Infrastructure) | 글로벌 이동통신사(AT&T, Verizon 등), 인터넷 백본 ISP, 라우팅 인프라 |
| 침해 궁극 목표 | 유사시(대만 해협 등 군사 충돌 시) 기반시설 기능 마비 및 물리적 파괴 사전 배치 | 법원 영장 감청 시스템(CALEA) 접근, 정부 고위층 통화 기록 및 실시간 패킷 도청 |
| 초기 침투 경로 | EOL/패치 미적용 SOHO 라우터(Fortinet, Netgear, Cisco) 취약점 | 통신 사업자 코어 라우터 취약점(Cisco, Juniper 등) 및 제로데이 익스플로잇 |
| 은닉 인프라 | 가정용/소규모 라우터로 구성된 KV-botnet을 프록시로 활용하여 지리적 위장 | 감염된 통신사 네트워크 장비 간 터널링 및 정상 BGP/MPLS 트래픽 은닉 |
| 대표적 LotL 전술 | `netsh portproxy`, `wmic`, `certutil`을 통한 내부 스캔 및 프록시 설정 | 라우터 설정 변경, 패킷 미러링 활성화, 원격 관리 프로토콜(SSH/SNMP) 탈취 |

## Ⅲ. LotL(Living-off-the-Land) 공격 메커니즘 및 탐지 아키텍처

```text
[ 1. 초기 침투 (Initial Access) ]
인터넷 노출 엣지 장비 (VPN / 라우터 취약점 CVE-2024-xxxx) ──▶ 웹셸 또는 백도어 설치 없이 메모리 침투
                                                                     │
                                                                     ▼
[ 2. 정찰 및 신원 탈취 (Credential Dumping) ]
LOLBins 실행: ntdsutil / comsvcs.dll 악용 ─────────────────────────▶ LSASS 메모리 덤프 (유효 NTLM/Kerberos 해시 탈취)
                                                                     │
                                                                     ▼
[ 3. 측면 이동 및 포트포워딩 (Lateral Movement) ]
정상 도구 실행: netsh interface portproxy add v4tov4 ──────────────▶ 내부 폐쇄망 코어 서버로 비인가 트래픽 터널링
                                                                     │
                                                                     ▼
[ 4. 탐지 회피 및 장기 지속성 (Persistence) ]
파일 생성 제로화(Fileless) + 예약 작업(schtasks) 등록 ───────────▶ 백신 시그니처 100% 우회 및 은밀 잠복

[ 5. 다계층 엔지니어링 방어선 구축 ]
├── [엣지 계층]: 엣지 장비 외부 관리 인터페이스 차단, EOL 장비 전면 퇴역, 펌웨어 무결성 점검
├── [호스트 계층]: AppLocker/WDAC 기반 LOLBins 실행 제한, PowerShell Constrained Language Mode
└── [분석 계층]: Sysmon Event ID 1(프로세스 트리), 4104(스크립트 블록), UEBA 행위 상관분석
```

| 공격 단계 | 악용되는 내장 도구(LOLBins) | 공격 행위 상세 | 탐지 및 차단 통제 |
|---|---|---|---|
| 정찰 및 검색 | `whoami`, `net user`, `nltest /dclist` | 도메인 컨트롤러 및 관리자 그룹 인벤토리 파악 | 실행 인자 감시, 일반 직군 실행 전면 차단 |
| 자격증명 탈취 | `comsvcs.dll` (MiniDump), `ntdsutil` | LSASS 프로세스 메모리 덤프로 패스워드 해시 추출 | LSA Protection(RunAsPPL) 활성화, ASR 룰 적용 |
| 트래픽 터널링 | `netsh interface portproxy` | 외부 C2와 내부 호스트 간의 포트포워딩 경로 구축 | 포트프록시 레지스트리 키 변경 실시간 이벤트 경보 |
| 원격 코드 실행 | `wmic process call create`, `WinRM` | 도메인 관리자 계정으로 내부 워크스테이션 원격 실행 | RPC/SMB 네트워크 세그멘테이션, 원격 WMI 차단 |
| 스크립트 실행 | `powershell.exe -enc <Base64>` | 난독화된 인메모리 스크립트 실행 | ScriptBlock 로깅(4104), AMSI 연동 실시간 검사 |

## Ⅳ. 전통적 악성코드 공격 vs LotL 공격 기법 비교

| 비교 항목 | 전통적 악성코드 공격 (Malware-based) | LotL 기반 은닉 공격 (Living-off-the-Land) |
|---|---|---|
| 페이로드 존재 | 디스크에 커스텀 악성 실행 파일(.exe/.dll) 생성 | 디스크 파일 미생성 (무파일/메모리 전용 실행) |
| 탐지 기술 | 시그니처 해시(MD5/SHA256), YARA 룰, AV 엔진 | 프로세스 계층 트리, 부모-자식 관계, 실행 인자 행위 분석 |
| 권한 및 계정 | 취약점을 통한 시스템 서비스 익스플로잇 | 탈취된 유효 관리자 계정(Valid Accounts) 사용 |
| 네트워크 트래픽 | 비표준 포트를 통한 외부 C2 통신 (탐지 용이) | 80/443 정상 관리 프로토콜 및 VPN 세션 위장 |
| 방어자 대응 난이도 | 상대적으로 용이 (파일 격리 및 백신 업데이트) | 극도로 어려움 (정상 관리자 작업과 공격 행위의 모호성) |

## Ⅴ. 한계와 방안

| 한계 | 방안 |
|---|---|
| 관리자의 정상적인 유지보수 스크립트와 공격자의 LotL 명령 인자가 거의 동일하여 대량의 오탐 발생 | 사용자·엔티티 행위 분석(UEBA)을 도입하여 비업무 시간(새벽 등), 비인가 IP 대역, 최초 실행된 명령 인자 조합에 대해서만 고위험 경보 발령 |
| 펌웨어 기반의 통신사 라우터나 SOHO 엣지 장비는 상용 EDR 에이전트 설치 불가로 인한 감시 사각지대 존재 | 엣지 장비 대상 NetFlow/IPFIX 트래픽 메타데이터를 전수 수집하여 비인가 외부 포트포워딩 및 장기 유지 세션의 이상 흐름 감시 |
| 공격자가 증적을 남기지 않기 위해 메모리에서만 동작하고 이벤트 로그를 선별 삭제(wevtutil cl)하는 행위 | 중앙 Syslog 서버로 이벤트를 실시간 원격 포워딩(WEC/WEF)하고 로그 저장소에 WORM 불변 설정을 적용하여 로컬 로그 삭제 무력화 |
| 탈취된 유효 관리자 계정(Valid Account)으로 로그인할 경우 다단계 인증(MFA) 우회 및 합법 세션으로 오인 | FIDO2 기반 피싱 저항 MFA(Hardware Passkey)를 전사 의무화하고 장치 상태(Device Compliance) 검증 없는 세션 즉시 차단 |

## Ⅵ. 제언

```text
[ 국가 배후 LotL 공격 대응 3대 심층 방어 모델 ]

+-------------------------+      +-------------------------+      +-------------------------+
|     엣지 표면 제거      | ---> |     스크립트 실행 격리  | ---> |     행위 기반 제로트러스트
| (공개 엣지 인터페이스)  |      | (WDAC / Constrained Mode|      | (UEBA + 무결성 로깅)    |
+-------------------------+      +-------------------------+      +-------------------------+
```

| 방어 축 | 중점 엔지니어링 구현 과제 | 비즈니스 가치 |
|---|---|---|
| 노출면 최소화 | 인터넷 노출 방화벽/VPN의 관리자 콘솔을 사설망으로만 제한(No Direct Internet Access) | 제로데이 기반 엣지 장비 침투 경로 원천 차단 |
| 실행 통제 | Windows Defender Application Control(WDAC)을 적용해 불필요한 LOLBins 전면 차단 | 호스트 침투 후 측면 이동 및 정찰 실행 무력화 |
| 행위 가시성 | PowerShell 스크립트 블록 로깅 및 Sysmon 중앙 집약 상관분석 체계 가동 | 시그니처 없는 무파일 침해의 골든타임 내 가시화 |

## 출제 이력과 검증 출처

- 제134회 컴퓨터시스템응용기술사 (무파일 악성코드 및 Living-off-the-Land 기법)
- CISA/NSA/FBI Joint Cybersecurity Advisory, PRC State-Sponsored Actors Compromise US Critical Infrastructure (Volt Typhoon)
- CISA/FBI Advisory, Salt Typhoon Compromises of US Telecommunications Infrastructure
- MITRE ATT&CK Framework: T1059 (Command and Scripting Interpreter), T1036 (Masquerading)

## 연결 토픽

- 2026 상반기 침해사고 위협 점검
- 제로 트러스트(Zero Trust)
- EDR(엔드포인트 탐지 및 대응)
- 비인간 신원(NHI)
