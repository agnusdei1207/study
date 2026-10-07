---
title: "형상관리(베이스라인)"
author: "Antigravity"
date: "2026-10-01T23:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기초"
extra:
  keyword_grade: "기초"
  model: "Gemini 3.8 Flash"
---

## Ⅰ. 형상관리의 개요

- 개념 : 소프트웨어 생명주기 전반에 걸쳐 요구사항, 설계서, 소스코드, 빌드 스크립트 등 모든 **형상 항목** (Configuration Item)의 변경 사항을 체계적으로 식별, 통제, 기록, 감사하는 소프트웨어 공학 관리 프로세스.
- 배경 및 필요성 : 다수의 개발자 협업 시 발생하는 코드 충돌 방지, 무분별한 요구사항 변경으로 인한 프로젝트 실패 예방, 과거 특정 시점의 산출물 복원 보장.
- 표준 근거 : **IEEE(Institute of Electrical and Electronics Engineers) 828** (형상관리 계획 표준), **CMMI**(Capability Maturity Model Integration) 형상관리(CM) 프로세스 영역.

## Ⅱ. 형상관리 4대 활동 및 변경 통제 프로세스

```text
   [ 형상 식별 ] ──> [ 형상 통제 ] ──> [ 형상 감사 ] ──> [ 형상 기록 ]
    - CI 선정         - 변경 요청(CR)     - 물리적/기능적      - 상태 보고
    - 베이스라인 확정  - CCB(Change Control Board) 심의·승인      베이스라인 검증     - 이력 추적성
```

- **형상 식별 (Identification)** : 관리 대상 산출물(CI, Configuration Item)을 정의하고 식별 체계(버전, 명명 규칙) 부여.
- **형상 통제 (Control)** : **변경요청서** (CR) 접수, **형상통제위원회** (CCB) 심의 승인 후 변경 수행.
- **형상 감사 (Audit)** : 베이스라인과 실제 산출물의 일치성을 **기능적 형상감사** (FCA, Functional Configuration Audit), **물리적 형상감사** (PCA, Physical Configuration Audit)로 검증.
- **형상 상태 보고 (Status Accounting)** : 모든 변경 이력과 현재 형상 상태를 이해관계자에게 투명하게 공유.

## Ⅲ. 베이스라인(Baseline)의 계층 체계 및 비교

| 베이스라인 종류 | 수립 단계 | 포함되는 주요 형상 항목 (CI) |
|---|---|---|
| **기능 베이스라인** (Functional) | 요구사항 분석 완료 시점 | 시스템 요구사항 명세서(SRS, Software Requirements Specification), 제안요청서(RFP, Request for Proposal), 업무 정의서 |
| **분배 베이스라인** (Allocated) | 기본/논리 설계 완료 시점 | 시스템 아키텍처 설계서, 서브시스템 기능 배분 명세서 |
| **설계 베이스라인** (Design) | 상세 설계 완료 시점 | 클래스 다이어그램, DB(Database) ERD(Entity-Relationship Diagram), 인터페이스 연동 정의서 |
| **제품 베이스라인** (Product) | 시스템 통합 및 검증 완료 시점 | 최종 릴리스 소스코드, 실행 파일, 운영 매뉴얼, 배포 산출물 |

## Ⅳ. 형상관리의 주요 한계점 및 해결 방안

- 장기 브랜치 운영으로 인한 대규모 통합 충돌(Merge Hell) :
  - 한계점 : 개발자가 별도의 기능 브랜치에서 수주~수개월간 독립적으로 개발을 진행한 후 메인 브랜치로 병합하려 할 때 방대한 코드 충돌과 회귀 결함이 발생.
  - 해결 방안 : 트렁크 기반 개발(Trunk-Based Development) 전략을 도입하여 매일 메인 브랜치로 지속적 통합(CI)을 수행하고, 미완성 기능은 기능 플래그(Feature Toggle)를 통해 배포 격리.
- 전통적 베이스라인 동결 절차와 클라우드 지속 배포(CD, Continuous Delivery) 간 충돌 :
  - 한계점 : 변경통제위원회(CCB)의 수작업 문서 승인을 거치는 정적 베이스라인 통제 방식은 일 수십 회의 릴리스를 수행하는 현대 마이크로서비스 및 클라우드 배포 속도를 저해.
  - 해결 방안 : GitOps 프레임워크를 적용하여 Git 커밋 해시와 태그 자체를 감사 가능한 베이스라인으로 활용하고, 자동화된 정책 검증(OPA: Open Policy Agent) 기반 CI/CD 파이프라인 승인 간소화.
- 인프라 및 환경 구성요소의 형상 누락(Configuration Drift) :
  - 한계점 : 소스코드만 버전 관리되고 OS(Operating System) 패치, 네트워크 방화벽, DB 스키마, 클라우드 리소스 설정 등이 수작업으로 변경되어 개발·스테이징·운영 환경 간 불일치 발생.
  - 해결 방안 : 인프라를 코드로 관리(IaC, Infrastructure as Code: Terraform, Ansible)하고, DVC(Data Version Control)를 통해 데이터 및 AI(Artificial Intelligence) 모델 버전까지 단일 형상 관리 체계로 통합하며 Drift 자동 탐지 도구 운영.

## Ⅴ. 현대 클라우드·DevOps 환경에서의 기술사적 제언

- Trunk-Based Development 및 단기 브랜치 전략 채택 : 전통적 Git Flow의 장기 브랜치는 대규모 머지 충돌을 유발하므로, 짧은 주기 내에 메인 트렁크로 병합하는 Trunk-Based 전략과 기능 플래그(Feature Flag)를 결합하여 지속적 통합 속도 극대화.
- 코드 기반 형상(Everything as Code)의 형상관리 범위 확대 : 애플리케이션 소스뿐만 아니라 인프라(Terraform), 파이프라인(Jenkinsfile), 보안 정책(OPA, Open Policy Agent)까지 형상 항목으로 통합 등록하여 완전한 재현성(Reproducibility) 확보 필요.
