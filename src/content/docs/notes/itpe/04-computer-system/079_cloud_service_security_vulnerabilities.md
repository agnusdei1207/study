---
title: "클라우드 서비스 보안 취약점과 대응"
author: "agnusdei1207"
date: "2026-10-25T14:20:00+09:00"
tags:
  - "notes-computer-system"
sidebar:
  badge:
    text: "응용"
extra:
  question_no: "079"
  keyword_grade: "응용"
  model: "GLM-5.3-Flash"
---

## 연관 키워드

- 클라우드 보안, 공유 책임 모델(Shared Responsibility Model), 권한 상승(Privilege Escalation)
- CSPM(Cloud Security Posture Management), CWPP(Cloud Workload Protection Platform), CIEM(Cloud Infrastructure Entitlement Management), CNAPP(Cloud-Native Application Protection Platform)
- 섀도우 클라우드(Shadow Cloud), 설정 드리프트(Configuration Drift)
- 제로 트러스트(Zero Trust), PoLP(Principle of Least Privilege), 기밀 컴퓨팅(Confidential Computing)
- DevSecOps, CSA CCM(Cloud Controls Matrix)

## Ⅰ. 클라우드 서비스 보안 취약점과 대응의 개요

- 핵심 요약 : **클라우드 보안**은 공유 책임 모델을 전제로 설정 오류·권한 결함·계정 탈취로부터 자산과 데이터를 보호하는 전 계층 방어 체계.
- 개념 : 가상화·멀티테넌시·API 기반 환경에서 **공유 책임 모델** (Shared Responsibility Model)에 따라 CSP(Cloud Service Provider)와 고객의 책임을 구분하고, 고객 측 취약점을 통제하는 다층 보안 체계.
- 배경 및 필요성 : 경계 중심의 전통 보안 패러다임이 클라우드 전환으로 약화되었고, 보안 사고의 주원인이 CSP 결함보다 고객 측 설정 오류와 자격 증명 관리 부실로 지목됨.
- 주요 목적 : **제로 트러스트** (Zero Trust) 원칙 기반의 접근 통제 확립, 설정 오류·취약점의 자동 탐지, 규제와 표준의 준수, 데이터 침해 방지.

## Ⅱ. 클라우드 서비스 보안 취약점과 대응의 특징 및 장점

- 핵심 요약 : 책임 분계선의 명확화와 주요 침해 경로의 구조 이해가 방어 우선순위의 근거가 되는 구조.

1. 공유 책임 분계선 : IaaS(Infrastructure as a Service)에서 OS 이상이 고객 책임, PaaS(Platform as a Service)·SaaS(Software as a Service)로 갈수록 CSP 책임 확대 → 통제 가능 영역의 명확한 투자 판단 효과.
2. 고정된 고객 책임 영역 : 데이터 분류·암호화와 IAM(Identity and Access Management) 계정 관리는 모든 서비스 모델에서 고객 책임 유지 → 운영 규율의 상시 필요성 인식 효과.
3. 연쇄 침해 구조 : 자격 증명 유출이 관리자 권한 획득과 **권한 상승** (Privilege Escalation)으로 이어지는 연쇄 → 최초 유출 지점 차단의 방어 효율 효과.

## Ⅲ. 클라우드 서비스 보안 취약점과 대응의 구조 (흐름)

- 핵심 요약 : 고객 책임 영역의 설정과 자격 증명 결함이 주된 침해 경로이며, 분계선 너머 CSP 영역은 인프라 자체의 보호를 담당하는 구조.
- 자격 증명 : 접근 키, 토큰, 인증서처럼 클라우드 자원 접근을 허가하는 신원 증명 수단.

```text
[ 공유 책임 모델의 분계선 ]

고객 책임 (데이터 · IAM · 설정 · 패치)
      ↓ 책임 분계선
CSP 책임 (물리 인프라 · 하이퍼바이저 · 네트워크)
```

```text
[ 연쇄 침해 경로 ]

노출된 자격 증명 (코드 저장소 · 설정 파일)
      ↓
계정 탈취
      ↓
권한 상승 (Privilege Escalation)
      ↓
미암호화 데이터 유출 · 랜섬웨어 피해
```

## Ⅳ. 클라우드 보안 솔루션 4종의 비교

- 핵심 요약 : CSPM·CWPP·CIEM·CNAPP은 탐지 대상과 적용 시점이 달라 단일 도구로 전 계층을 대체할 수 없는 상보 구조.

| 솔루션 | 핵심 역할 | 방어 영역 | 적용 시점 |
| :--- | :--- | :--- | :--- |
| **CSPM** (Cloud Security Posture Management) | 설정 오류 탐지와 보안 태세 관리 | 제어 평면 설정 (공개 버킷, 과도 개방 포트) | 배포 후 지속 점검 |
| **CWPP** (Cloud Workload Protection Platform) | 워크로드 런타임 보호 | VM·컨테이너의 악성 행위, 비정상 프로세스 | 운영 중 런타임 |
| **CIEM** (Cloud Infrastructure Entitlement Management) | 클라우드 권한 관리 | 최소 권한 위반, 미사용 관리자 권한 | IAM 거버넌스 |
| **CNAPP** (Cloud-Native Application Protection Platform) | 상기 기능과 코드 스캔의 통합 | 개발부터 런타임까지의 전 수명주기 | 개발부터 운영까지 |

- 선택 기준 :
  1. 설정 오류가 주된 위험이면 CSPM 우선 도입
  2. 런타임 위협 노출이 큰 업무면 CWPP 보강
  3. 통합 운영과 개발 단계 연계가 필요하면 CNAPP 통합

## Ⅴ. 클라우드 서비스 보안 취약점과 대응의 한계와 방안

- 핵심 요약 : 과도 권한과 설정 괴리, 공유 인프라 노출을 최소 권한 자동화, 형상 감시, 격리 배치로 대응.

| 한계 | 원인·영향 | 대응 방안 | 관리 지표 |
| :--- | :--- | :--- | :--- |
| 과도 권한과 키 탈취 | 와일드카드(*) 정책·장기 키의 만연 → 토큰 하나의 유출로 전 인프라 노출 | CIEM 기반 **PoLP** (Principle of Least Privilege) 자동 점검, 장기 키 폐기와 OIDC(OpenID Connect) 임시 토큰 전환 | 와일드카드 정책 수 |
| **섀도우 클라우드** (Shadow Cloud)와 **설정 드리프트** (Configuration Drift) | 미승인 자원과 수동 변경의 템플릿과의 괴리 → 보안 격차 발생 | CSPM 기반 형상 감시, 변경의 GitOps 승인 반영 강제 | 드리프트 탐지 건수 |
| 멀티테넌시의 부채널 리스크 | 공유 물리 서버의 CPU 부채널(Spectre 등) 악용 가능성 | 민감 워크로드의 전용 호스트 배치, **기밀 컴퓨팅** (Confidential Computing) 적용 | 공유 호스트 배치 비율 |

## Ⅵ. 클라우드 서비스 보안 취약점과 대응에 대한 기술사적 제언

- 핵심 요약 : 보안 검증의 개발 단계 이전 이동, 계정 거버넌스, 표준 기반 통제 체계가 필요.

1. 개발 조직은 DevSecOps 파이프라인으로 IaC 템플릿과 컨테이너 이미지를 빌드 단계에서 검사하고 치명 결함의 배포 차단 정책을 표준화.
2. 보안 거버넌스 조직은 계정 생성·권한 승인 주체를 소수로 집중하고 기준을 문서화하는 계정 거버넌스 체계 구축.
3. 컴플라이언스 조직은 ISMS-P(정보보호 및 개인정보보호 관리체계)와 CSA CCM(Cloud Controls Matrix) 통제 항목의 사내 통제 체계 매핑 운영.

## Ⅶ. 결론

- 핵심 요약 : 클라우드 보안은 공유 책임 모델 위에서 4종 솔루션으로 전 계층을 방어하는 상보적 체계.
- 시사점 : 사고의 출발점이 설정 오류와 자격 증명 관리인 만큼, 도구 도입보다 고객 책임 영역의 운영 규율이 보안 수준을 결정.
