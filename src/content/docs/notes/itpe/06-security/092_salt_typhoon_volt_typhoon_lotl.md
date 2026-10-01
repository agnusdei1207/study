---
title: "Salt Typhoon / Volt Typhoon (LotL)"
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

## Ⅰ. Salt Typhoon / Volt Typhoon (LotL)의 개요

- ** 개념** : OS 내장 관리 도구(PowerShell, WMI, netsh 등)와 유효한 관리자 자격증명을 악용하여 악성 바이너리 없이 표적망에 장기 잠복하는 LotL 기반 국가 배후 APT 위협.
- ** 배경 및 필요성** : 국가 지원 해킹 그룹이 별도의 악성코드를 설치하지 않고 타깃 시스템에 기설치된 정상 관리 도구(PowerShell, WMI 등)를 악용하는 Living-off-the-Land(LotL) 기법으로 장기 잠복함에 따라, 행위 기반 심층 탐지의 필요성이 급증함.
- ** 핵심 목적** : 전통적인 안티바이러스 및 파일 기반 EDR 탐지를 무력화하고, 중요 기반시설 파괴 준비(Volt) 및 통신 백본 도청(Salt)을 위한 은밀한 지속성(Persistence) 유지.

## Ⅱ. Salt Typhoon / Volt Typhoon (LotL)의 핵심 아키텍처 및 동작 메커니즘

Salt Typhoon / Volt Typhoon (LotL)은(는) 신뢰할 수 있는 보안 구조와 표준화된 절차를 기반으로 동작하며, 세부적인 아키텍처와 구성요소 간의 상호작용 메커니즘은 다음과 같음.

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

- ** 정찰 및 검색** : `whoami`, `net user`, `nltest /dclist` (도메인 컨트롤러 및 관리자 그룹 인벤토리 파악).
- ** 자격증명 탈취** : `comsvcs.dll` (MiniDump), `ntdsutil` (LSASS 프로세스 메모리 덤프로 패스워드 해시 추출).
- ** 트래픽 터널링** : `netsh interface portproxy` (외부 C2와 내부 호스트 간의 포트포워딩 경로 구축).
- ** 원격 코드 실행** : `wmic process call create`, `WinRM` (도메인 관리자 계정으로 내부 워크스테이션 원격 실행).
- ** 스크립트 실행** : `powershell.exe -enc <Base64>` (난독화된 인메모리 스크립트 실행).

## Ⅲ. Salt Typhoon / Volt Typhoon (LotL)의 세부 구성 요소 및 비교 분석

| 비교 항목 | 전통적 악성코드 공격 (Malware-based) | LotL 기반 은닉 공격 (Living-off-the-Land) |
|---|---|---|
| 페이로드 존재 | 디스크에 커스텀 악성 실행 파일(.exe/.dll) 생성 | 디스크 파일 미생성 (무파일/메모리 전용 실행) |
| 탐지 기술 | 시그니처 해시(MD5/SHA256), YARA 룰, AV 엔진 | 프로세스 계층 트리, 부모-자식 관계, 실행 인자 행위 분석 |
| 권한 및 계정 | 취약점을 통한 시스템 서비스 익스플로잇 | 탈취된 유효 관리자 계정(Valid Accounts) 사용 |
| 네트워크 트래픽 | 비표준 포트를 통한 외부 C2 통신 (탐지 용이) | 80/443 정상 관리 프로토콜 및 VPN 세션 위장 |
| 방어자 대응 난이도 | 상대적으로 용이 (파일 격리 및 백신 업데이트) | 극도로 어려움 (정상 관리자 작업과 공격 행위의 모호성) |

- Salt Typhoon / Volt Typhoon (LotL)은(는) 상기 핵심 비교 지표와 아키텍처 구성을 바탕으로 보안 위협에 대한 방어 효과성을 극대화하며, 기존 레거시 통제 기법 대비 우수한 신뢰성과 운영 효율성을 제공함.

## Ⅳ. Salt Typhoon / Volt Typhoon (LotL)의 주요 한계점 및 해결 방안

- ** OS 내장 도구(LotL) 악용 시 정상 명령과 악성 행위의 식별 난제** : - ** 한계점** : 관리자의 정상적인 유지보수 스크립트와 공격자의 LotL 명령 인자가 거의 동일하여 대량의 오탐 발생.
  - ** 해결 방안** : 사용자·엔티티 행위 분석(UEBA)을 도입하여 비업무 시간(새벽 등), 비인가 IP 대역, 최초 실행된 명령 인자 조합에 대해서만 고위험 경보 발령.
- ** 펌웨어 기반의 통신사 라우터나 SOHO 엣지 장비는 취약점** : - ** 한계점** : 펌웨어 기반의 통신사 라우터나 SOHO 엣지 장비는 상용 EDR 에이전트 설치 불가로 인한 감시 사각지대 존재.
  - ** 해결 방안** : 엣지 장비 대상 NetFlow/IPFIX 트래픽 메타데이터를 전수 수집하여 비인가 외부 포트포워딩 및 장기 유지 세션의 이상 흐름 감시.
- ** 공격자가 증적을 남기지 않기 위해 메모리에서만 동작 취약점** : - ** 한계점** : 공격자가 증적을 남기지 않기 위해 메모리에서만 동작하고 이벤트 로그를 선별 삭제(wevtutil cl)하는 행위.
  - ** 해결 방안** : 중앙 Syslog 서버로 이벤트를 실시간 원격 포워딩(WEC/WEF)하고 로그 저장소에 WORM 불변 설정을 적용하여 로컬 로그 삭제 무력화.
- ** 탈취된 유효 관리자 계정 위험** : - ** 한계점** : 탈취된 유효 관리자 계정(Valid Account)으로 로그인할 경우 다단계 인증(MFA) 우회 및 합법 세션으로 오인.
  - ** 해결 방안** : FIDO2 기반 피싱 저항 MFA(Hardware Passkey)를 전사 의무화하고 장치 상태(Device Compliance) 검증 없는 세션 즉시 차단.

## Ⅴ. Salt Typhoon / Volt Typhoon (LotL) 적용 및 발전을 위한 기술사적 제언

- ** 노출면 최소화 중심의 거버넌스 및 실행 체계 구축** : 인터넷 노출 방화벽/VPN의 관리자 콘솔을 사설망으로만 제한(No Direct Internet Access)을(를) 적극 추진하여, 제로데이 기반 엣지 장비 침투 경로 원천 차단 효과를 극대화해야 함.
- ** 실행 통제 중심의 거버넌스 및 실행 체계 구축** : Windows Defender Application Control(WDAC)을 적용해 불필요한 LOLBins 전면 차단을(를) 적극 추진하여, 호스트 침투 후 측면 이동 및 정찰 실행 무력화 효과를 극대화해야 함.
- ** 행위 가시성 중심의 거버넌스 및 실행 체계 구축** : PowerShell 스크립트 블록 로깅 및 Sysmon 중앙 집약 상관분석 체계 가동을(를) 적극 추진하여, 시그니처 없는 무파일 침해의 골든타임 내 가시화 효과를 극대화해야 함.
