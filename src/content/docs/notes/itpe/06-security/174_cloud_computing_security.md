---
title: "클라우드 컴퓨팅 보안(Cloud Security)"
author: "agnusdei1207"
date: "2026-10-24T23:12:46+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Claude Haiku 5.5"
---

## 연관 키워드

- 클라우드 컴퓨팅 보안(Cloud Security), CNAPP(Cloud Native Application Protection Platform), CSPM(Cloud Security Posture Management), CWPP(Cloud Workload Protection Platform)
- CIEM(Cloud Infrastructure Entitlement Management), CASB(Cloud Access Security Broker), IaC(Infrastructure as Code), DevSecOps
- 설정 오류(Misconfiguration), 최소 권한 원칙, 제로 트러스트(Zero Trust), 기밀 컴퓨팅(Confidential Computing), SBOM

## Ⅰ. 클라우드 컴퓨팅 보안의 개요

- 핵심 요약 : 클라우드의 민첩성을 해치지 않으면서 인프라, 워크로드, 권한, 데이터를 자동화된 통제로 보호하는 보안 체계.
- 개념 : IaaS(Infrastructure as a Service), PaaS(Platform as a Service), SaaS(Software as a Service)와 하이브리드·멀티 클라우드 환경에서 가상화 인프라, 컨테이너, 서버리스 워크로드와 데이터를 위협으로부터 지키는 **클라우드 보안** (Cloud Security) 아키텍처와 거버넌스.
- 배경 및 필요성 : 온프레미스에서 멀티 클라우드로 전환되며 네트워크 경계가 사라졌고, 코드형 인프라(IaC, Infrastructure as Code) 배포 오류와 과도한 IAM(Identity and Access Management) 권한 부여로 인한 대규모 데이터 침해가 빈발함.
- 주요 목적 : 멀티 테넌트 환경의 자원 격리와 규제 준수를 확보하고, 코드형 보안(Security as Code)으로 **제로 트러스트** (Zero Trust, 모든 접근을 매번 검증하는 보안 원칙)를 실현.

## Ⅱ. 클라우드 컴퓨팅 보안의 특징 및 장점

- 핵심 요약 : 보안 설정을 코드로 관리하고 네 영역을 하나의 플랫폼에서 보므로, 설정 오류와 권한 과잉을 배포 전후 모두에서 잡을 수 있음.

1. **CSPM** (Cloud Security Posture Management, 클라우드 설정 상태를 상시 감사하는 자세 관리) : 공개된 스토리지나 개방된 보안 그룹을 탐지 → 설정 오류로 인한 노출 기간 단축.
2. **CIEM** (Cloud Infrastructure Entitlement Management, 클라우드 권한을 식별하고 회수하는 관리) : 미사용 권한과 권한 상승 경로를 제거 → 과잉 권한 악용 차단.
3. **CWPP** (Cloud Workload Protection Platform, 가상머신·컨테이너 등 실행 중 워크로드 보호) : 런타임 행위와 파일 무결성을 감시 → 익스플로잇과 랜섬웨어 조기 차단.
4. **Shift-Left** (배포 전 단계로 보안 점검을 앞당기는 방식) : Terraform과 매니페스트를 빌드 단계에서 정적 검사 → 결함 수정 비용 절감.

## Ⅲ. 클라우드 컴퓨팅 보안의 구조 (흐름)

- 핵심 요약 : 개발 단계의 코드 검사와 런타임의 자세, 권한, 워크로드 감시가 **CNAPP** 한 플랫폼에서 이어지는 전주기 구조.
- **CNAPP** (Cloud Native Application Protection Platform, CSPM, CWPP, CIEM, IaC 스캐닝을 단일 플랫폼으로 통합한 보안 도구) : 파편화된 도구를 하나의 가시성으로 묶음.

```text
[ 개발 단계 ]
  IaC(Terraform) 정적 검사
  시크릿 유출 사전 차단
        ↓
[ 배포 단계 ]
  이미지 취약점 점검, SBOM 검증
        ↓
[ 운영 단계 ]
  CSPM: 설정 오류 자동 치유
  CIEM: 과잉 권한 회수
  CWPP: 워크로드 런타임 차단
        ↓
[ 공격 경로 분석 ]
  복합 위험을 우선순위로 정리
```

```text
[ 설정 오류 발생 (공개 스토리지 등) ]
        ↓
[ CSPM 탐지 ]
        ↓
[ 자동 복구 규칙 실행 또는 담당자 알림 ]
        ↓
[ CIEM으로 연계된 권한 과잉 점검 ]
```

## Ⅳ. 클라우드 보안 구성 요소의 비교

- 핵심 요약 : 설정, 워크로드, 권한, SaaS 접근은 통제 계층이 달라 각각 전용 도구가 필요함.

| 비교 항목 | CSPM (자세 관리) | CWPP (워크로드 보호) | CIEM (권한 관리) | CASB (접근 중개) |
| --- | --- | --- | --- | --- |
| 통제 계층 | 클라우드 제어 평면 | 실행 중인 워크로드 | 신원과 권한 (IAM) | 사용자와 SaaS 사이 |
| 수집 방식 | 제공자 API 기반 (에이전트 없음) | OS·컨테이너 에이전트 또는 eBPF | IAM 정책과 로그 분석 | 프록시 및 API 연동 |
| 핵심 목적 | 설정 오류와 규제 감사 | 런타임 악성코드와 침입 차단 | 과잉 권한 회수 | SaaS 데이터 유출 방지 |
| 주요 대상 | 스토리지 버킷, 보안 그룹, IAM 설정 | VM, 컨테이너, 서버리스 | IAM 역할, 서비스 계정 | 메일, 협업, CRM SaaS |

- 선택 기준 : 사고 원인이 설정인지, 실행 중 공격인지, 권한인지, SaaS 데이터 흐름인지에 따라 도구를 배치함.

## Ⅴ. 클라우드 컴퓨팅 보안의 한계와 방안

- 핵심 요약 : 설정 오류 노출, 멀티 클라우드 정책 파편화, 격리 경계 붕괴를 코드형 점검, 통합 플랫폼, 격리 런타임으로 통제.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| --- | --- | --- | --- |
| 설정 오류에 따른 노출 | 스토리지를 실수로 공개하면 공격자의 자동 스캔에 빠르게 발견되어 기밀 유출 | IaC 파이프라인에서 사전 정적 분석을 강제하고 CSPM 자동 복구 규칙 운영 | 설정 오류 건수, 자동 복구 비율 |
| 멀티 클라우드 정책 파편화 | 클라우드마다 용어, 대시보드, IAM 구조가 달라 일관된 거버넌스 유지가 어려움 | 이종 클라우드 API를 단일 질의 체계로 통합 감사하는 CNAPP 구축 | 정책 일관성 점검률 |
| 샌드박스 탈출 위험 | 공동 테넌트에서 악성 컨테이너가 커널 취약점으로 호스트를 장악할 수 있음 | gVisor, Kata Containers 같은 격리형 런타임과 seccomp·AppArmor 프로파일 적용 | 격리 런타임 적용률 |

## Ⅵ. 클라우드 컴퓨팅 보안에 대한 기술사적 제언

- 핵심 요약 : 배포 후 점검에서 벗어나 코드 단계의 자동 검사, 임시 자격증명, 데이터 사용 중 보호를 결합한 체계로 전환.
- Terraform 코드와 Dockerfile을 빌드 파이프라인에서 자동 검사하여, 배포 후에 발견되는 결함을 줄이는 **DevSecOps** (개발, 보안, 운영을 한 흐름에서 통합하는 방식) 문화를 정착시켜야 한다.
- 소스코드나 서버에 고정된 영구 액세스 키 사용을 금지하고, 수명이 짧은 임시 자격증명(STS, Security Token Service)만 사용하도록 IAM 역할 체계를 정비해야 한다.
- 메모리에서 데이터가 처리되는 동안에도 보호하기 위해 **기밀 컴퓨팅** (Confidential Computing, 하드웨어 기반 신뢰 실행 환경에서 데이터를 처리하는 기술)을 민감 워크로드에 적용하면 클라우드 사업자 내부자의 접근을 줄일 수 있다.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 보안 사고 대부분은 클라우드 자체보다 고객의 설정 오류와 부실한 권한 관리에서 발생함.
- 시사점 : 코드형 보안과 통합 플랫폼을 기본값으로 삼는 조직이 클라우드의 확장성과 보안을 동시에 확보할 수 있음.
