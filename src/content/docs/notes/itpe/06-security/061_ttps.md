---
title: "TTPs(Tactics, Techniques and Procedures)"
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

## Ⅰ. TTPs(Tactics, Techniques and Procedures)의 개요

- 개념 : 공격자가 사이버 공격 목표를 달성하기 위해 사용하는 **전술** (Tactics, 목적), **기법** (Techniques, 수단), **절차** (Procedures, 실행 도구/명령어)의 복합적 행동 패턴 체계.
- 배경 및 필요성 : IP(Internet Protocol), 도메인, 파일 해시 등 정적 **침해지표** (IoC)는 공격자가 손쉽게 변경하여 보안 장비를 무력화하므로, 공격자의 전략·기법·절차 자체를 프로파일링하여 **지능형 지속 위협** (APT, Advanced Persistent Threat)에 선제 대응하기 위해 **MITRE ATT&CK** 기반으로 체계화됨.
- 핵심 목적 : IP, 해시 등 쉽게 변조되는 단편적 지표를 넘어 공격자의 본질적 공격 행위 패턴을 식별·차단함으로써 공격자의 침투 비용을 극대화하고 사전 예방 역량 확보.

## Ⅱ. TTPs(Tactics, Techniques and Procedures)의 핵심 아키텍처 및 동작 메커니즘

TTPs(Tactics, Techniques and Procedures)은(는) 신뢰할 수 있는 보안 구조와 표준화된 절차를 기반으로 동작하며, 세부적인 아키텍처와 구성요소 간의 상호작용 메커니즘은 다음과 같음.

```text
[ 1. 보안 로그 및 이벤트 수집 ]
EDR 텔레메트리 / Sysmon / 네트워크 패킷 / 클라우드 감사 로그
       │
       ▼
[ 2. 공격 행위 식별 및 추출 ] ── 비정상 프로세스 생성, 자격증명 덤프 포착
       │
       ▼
[ 3. MITRE ATT&CK 프레임워크 매핑 ]
   ┌────────────────────────────────────────────────────────┐
   │ 전술: 자격증명 접근 (Credential Access, TA0006)         │
   │  └── 기법: OS 자격증명 덤프 (OS Credential Dumping, T1003)│
   │       └── 하위기법: LSASS 메모리 (T1003.001)           │
   │            └── 절차: Mimikatz "sekurlsa::logonpasswords"│
   └────────────────────────────────────────────────────────┘
       │
       ▼
[ 4. 행위 기반 탐지 룰화 ] ── Sigma / YARA-L / Splunk SPL 룰 작성
       │
       ▼
[ 5. 위협 헌팅 (Threat Hunting) 및 공격 시뮬레이션(BAS) 유효성 검증 ]
```

- **1. 데이터 수집** : 프로세스 계층, 명령행 인수(CLI, Command-Line Interface), 레지스트리 수정 로그 확보 (**Sysmon** 이벤트 ID 1, EDR(Endpoint Detection and Response) 프로세스 트리).
- **2. 행위 역공학** : 악성코드 분석 및 사고 조사에서 발견된 TTPs 도출 (정적/동적 샌드박스 분석 보고서).
- **3. ATT&CK 매핑** : 관측된 공격 동작을 ATT&CK 매트릭스의 기법 ID로 표준화 매핑 (Enterprise Matrix v15, Navigator 레이어).
- **4. 탐지 룰 개발** : 개별 파일명이 아닌 API(Application Programming Interface) 호출 순서 및 부모-자식 관계 기반 룰셋 작성 (**Sigma** 룰, EDR 커스텀 탐지 정책).
- **5. 모의 검증** : 원자적 공격 스크립트로 방어 통제가 실제 기법을 탐지하는지 실증 (Atomic Red Team, Caldera 시뮬레이터).

## Ⅲ. TTPs(Tactics, Techniques and Procedures)의 세부 구성 요소 및 비교 분석

| 구분 | 침해지표 (IoC: Indicators of Compromise) | 침해행위 (TTPs: Tactics, Techniques & Procedures) |
|---|---|---|
| 데이터 성격 | IP 주소, URL(Uniform Resource Locator), 도메인, 파일 해시값 등 정적 데이터 | 공격자의 전술적 목표, 공격 기법, 구체적 실행 명령어 패턴 |
| 방어 효과 | 이미 알려진 동일 공격체의 즉각적 차단 | 변종 악성코드 및 신규 제로데이 공격의 행위 기반 탐지 |
| 공격자 회피 난이도 | 사소함 (Trivial): 코드 재컴파일만으로 해시값 즉시 변조 | 극도로 고통스러움 (Tough): 침투 전략 및 개발 도구 전면 재구축 |
| 방어자 구축 난이도 | 쉬움: 방화벽 블랙리스트 IP 등록, 백신 시그니처 배포 | 높음: 전사 EDR 로그 상관분석, 정밀 행위 분석 룰셋 설계 필요 |
| 주 활용 분야 | 방화벽 차단 정책, 안티바이러스, SIEM(Security Information and Event Management) 단순 매칭 | 위협 헌팅, SOC(Security Operations Center) 관제 고도화, BAS 모의 침투 시뮬레이션 |

- TTPs(Tactics, Techniques and Procedures)은(는) 상기 핵심 비교 지표와 아키텍처 구성을 바탕으로 보안 위협에 대한 방어 효과성을 극대화하며, 기존 레거시 통제 기법 대비 우수한 신뢰성과 운영 효율성을 제공함.

## Ⅳ. TTPs(Tactics, Techniques and Procedures)의 주요 한계점 및 해결 방안

- 한계점 : MITRE ATT&CK 매트릭스의 다수 기법을 단순히 엑셀로 체크하는 '체크리스트식 색칠'에 매몰되어 실제 데이터 수집 사각지대 간과.
  - 해결 방안 : ATT&CK의 데이터 컴포넌트(Data Components)를 역추적하여 조직의 EDR/Sysmon 로그가 해당 기법을 감시할 수 있는지 데이터 가시성(Data Coverage) 우선 검증.
- 한계점 : 공격자가 정상 운영체제 내장 도구(PowerShell, WMI, Certutil)를 악용하는 **LOLBins** (Living off the Land) 구사 시 정상 업무와 오탐 혼선.
  - 해결 방안 : 단일 명령어 매칭을 지양하고 부모-자식 프로세스 실행 계통 트리(Process Tree Context) 및 비정상 네트워크 아웃바운드 결합 상관분석 적용.
- 한계점 : 동일한 ATT&CK 기법 번호라도 공격 그룹마다 컴파일 옵션이나 스크립트 절차(Procedures)를 변형하여 정적 탐지 룰 우회 발생.
  - 해결 방안 : **Atomic Red Team** 및 Caldera 기반 오픈소스 모의 공격 프레임워크를 연동하여 기법별 변종 절차에 대한 자동화 회귀 테스트 상시 가동.

## Ⅴ. TTPs(Tactics, Techniques and Procedures) 적용 및 발전을 위한 기술사적 제언

- **MITRE ATT&CK 전술/기법 매핑** 체계 도입 : MITRE ATT&CK 전술/기법 매핑 기술을 적극 적용하여 보안 취약점을 차단하고 시스템 신뢰성을 보장해야 함.
- **부모-자식 프로세스 인과관계 추적** 체계 도입 : 부모-자식 프로세스 인과관계 추적 기술을 적극 적용하여 보안 취약점을 차단하고 시스템 신뢰성을 보장해야 함.
- **원자적 공격 시뮬레이션(BAS) 지속 검증** 체계 도입 : 원자적 공격 시뮬레이션(BAS) 지속 검증 기술을 적극 적용하여 보안 취약점을 차단하고 시스템 신뢰성을 보장해야 함.
