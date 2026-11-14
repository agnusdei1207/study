---
title: "디지털 아티팩트(Digital Artifact)"
author: "agnusdei1207"
date: "2026-10-24T22:53:05+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  question_no: "008"
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 디지털 아티팩트(Digital Artifact), 포렌식(Forensics), 슈퍼 타임라인(Super Timeline)
- Prefetch, Amcache, Shimcache, MFT, $UsnJrnl, 타임스톰프(Timestomp)
- SSD TRIM, 파일리스 악성코드(Fileless Malware), 부인 방지(Non-repudiation), Sysmon

## Ⅰ. 디지털 아티팩트의 개요

- 핵심 요약 : 운영체제와 응용 프로그램이 정상 동작하며 남기는 흔적을 시간순으로 재구성해 침해사고를 입증하는 포렌식 증거 자원.
- 개념 : 운영체제(OS, Operating System), 파일시스템, 응용 프로그램이 동작하는 과정에서 저장장치와 레지스트리에 자동으로 남는 흔적을 **디지털 아티팩트** (Digital Artifact)라 하며, 이를 수집·분석하는 활동이 포렌식(Forensics)임.
- 배경 및 필요성 : 침해사고 조사와 법적 분쟁에서는 과거의 프로그램 실행, 파일 접근, USB(Universal Serial Bus) 장치 연결 순서를 재구성해야 하며, 사용자가 의도적으로 남기지 않은 흔적이 사실 확인의 근거가 됨.
- 주요 목적 : 침해 유입 경로와 악성코드 실행 이력 규명, 데이터 유출 행위의 **부인 방지** (Non-repudiation, 행위 사실을 행위자가 부정하기 어렵게 하는 성질) 근거 확보, 침해 타임라인 복원.

## Ⅱ. 디지털 아티팩트의 특징 및 장점

- 핵심 요약 : 자동 기록이라는 생성 방식이 행위의 객관적 증거가 되고, 여러 계층의 기록을 교차하면 조작에 강한 재구성이 가능해지는 구조.

1. 자동 생성 : 사용자가 의도하지 않아도 운영체제가 캐시와 저널에 기록 → 행위자가 남기지 않으려 한 흔적까지 확보 가능.
2. 다계층 분산 저장 : 실행, 파일, 장치, 계정 기록이 서로 다른 위치에 남음 → 한 계층이 지워져도 다른 계층으로 행위를 재구성.
3. 시계열 상관 분석 : 여러 아티팩트의 시각을 하나의 타임라인으로 정렬 → 침해 순서와 범위를 복원하고 개별 기록의 신뢰도를 보완.

## Ⅲ. 디지털 아티팩트의 구조 (흐름)

- 핵심 요약 : 행위가 여러 아티팩트 계층에 흩어져 기록되고, 이를 **슈퍼 타임라인** (Super Timeline)으로 통합해 분석하는 두 단계 구조.
- **프리페치** (Prefetch) : 응용 프로그램 로딩 가속용 캐시 파일로 실행 파일명, 실행 횟수, 최초·최종 실행 시각을 보존.
- **암캐시** (Amcache.hve) : 프로그램 설치와 실행 정보, 파일의 SHA(Secure Hash Algorithm)-1 해시를 별도 하이브 파일에 보존.
- **심캐시** (Shimcache, AppCompatCache) : 호환성 유지를 위한 커널 캐시로 파일 경로와 수정 시각을 기록.
- **MFT** (Master File Table) : NTFS(New Technology File System)의 파일 메타데이터 테이블로, $STANDARD_INFORMATION과 $FILE_NAME 두 종류의 타임스탬프를 보유.
- **저널 로그** ($UsnJrnl) : 파일 생성, 이름 변경, 삭제 이력을 연속으로 기록하는 변경 저널.

```text
[ 행위 → 아티팩트 계층 ]

사용자·공격자 행위
      ↓
1. 실행 흔적: Prefetch, Amcache, Shimcache
      ↓
2. 파일 흔적: MFT, $UsnJrnl, LNK, Shellbags
      ↓
3. 장치·계정: USBSTOR, 보안 이벤트 로그
      ↓
슈퍼 타임라인 통합 (Plaso)
```

```text
[ 상관 분석 절차 ]

단일 아티팩트 확인
      ↓
다른 계층 기록과 시각 대조
      ↓
시계열 정렬 (슈퍼 타임라인)
      ↓
침해 순서 재구성
```

## Ⅳ. 디지털 아티팩트의 비교

- 핵심 요약 : 아티팩트마다 저장 위치와 보존 정보가 달라, 단일 기록만으로 결론을 내리지 않고 목적에 따라 대조하는 것이 원칙.

| 아티팩트 | 저장 위치 | 보존 정보 | 분석 활용 목적 |
| --- | --- | --- | --- |
| Prefetch | C:\Windows\Prefetch | 실행 파일명, 실행 횟수, 실행 시각 | 악성 프로그램 실행 여부와 빈도 입증 |
| Amcache | Amcache.hve | 파일 해시, 설치 경로, 컴파일 시각 | 악성코드 해시 확보와 변종 판별 |
| Shimcache | SYSTEM 하이브 | 파일 경로, 수정 시각 | 삭제된 파일의 과거 존재 입증 |
| Shellbags | NTUSER.DAT, UsrClass.dat | 폴더 탐색 기록 | 특정 폴더 탐색 행위 입증 |
| LNK·점프 목록 | 최근 항목 폴더 | 원본 경로, 볼륨 일련번호 | 외장 장치에서 열어본 문서 역추적 |

- 선택 기준 : 단일 아티팩트는 위변조 가능성이 있으므로, 시각과 실행 기록을 교차 확인한 결과만 증거로 채택.

## Ⅴ. 디지털 아티팩트의 한계와 방안

- 핵심 요약 : 시각 조작, 저장 매체 특성에 따른 증거 소멸, 디스크 흔적이 없는 공격을 교차 분석과 선제 수집으로 보완.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| **타임스톰프** (Timestomp) 시각 조작 | 악성 파일의 MFT 시각을 정상 파일과 같게 바꿔 시계열 정렬 회피 | $STANDARD_INFORMATION과 $FILE_NAME 타임스탬프 불일치 탐지, $UsnJrnl과 대조 | 불일치 탐지 건수 |
| SSD(Solid-State Drive)의 TRIM 명령에 따른 증거 소멸 | 삭제 후 TRIM으로 셀이 초기화되어 카빙 복구 가능성이 크게 낮아짐 | MFT 메타데이터 우선 분석, VSS(Volume Shadow Copy Service) 스냅샷과 메모리 덤프 선제 수집 | 증거 수집 소요 시간 |
| **파일리스 악성코드** (Fileless Malware) | 디스크 기록 없이 WMI(Windows Management Instrumentation)나 레지스트리로 실행되어 디스크 아티팩트 부재 | WMI 리포지토리 분석, ASEP(Auto-Start Extensibility Point) 점검, 메모리의 VAD(Virtual Address Descriptor) 트리 분석 | 자동 실행 항목 변경 건수 |

## Ⅵ. 디지털 아티팩트에 대한 기술사적 제언

- 핵심 요약 : 단말 로그 삭제와 분석 지연에 대비해 로그 중앙 전송, 표준 수집 도구, 자동화된 타임라인 절차를 갖추는 방향.

단말의 로컬 로그가 공격자에 의해 삭제되더라도 증거가 남도록, 보안관제 조직은 보안 이벤트를 SIEM(Security Information and Event Management)으로 실시간 전송하는 구조를 기본으로 삼아야 한다.

기업 단말 전체에 **Sysmon** (System Monitor)을 표준으로 배포해 프로세스 생성 해시, 네트워크 연결, 파일 생성 기록을 확보해 두는 것이 기본 준비다.

사고 대응 절차에는 여러 단말의 아티팩트를 원격으로 수집해 Plaso와 Timesketch로 단일 타임라인을 만드는 과정을 SOAR(Security Orchestration, Automation and Response) 플레이북으로 정형화하면, 분석 인력의 수작업 의존을 줄이고 대응 속도를 높일 수 있다.

## Ⅶ. 결론

- 핵심 요약 : 디지털 아티팩트는 자동으로 남는 흔적을 여러 계층에서 교차해 사실을 입증하는 포렌식의 기본 자원.
- 시사점 : 개별 기록은 지워지거나 조작될 수 있으므로, 수집 범위를 넓히고 시간 정렬을 자동화하는 것이 증거 신뢰도를 지키는 방법임.
