---
title: "형상관리(베이스라인)"
author: "agnusdei1207"
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

## 연관 키워드

- 형상관리(Configuration Management), 형상 항목(CI, Configuration Item), 베이스라인(Baseline)
- 형상통제위원회(CCB, Change Control Board), 트렁크 기반 개발(Trunk-Based Development), GitOps, IaC(Infrastructure as Code)

## Ⅰ. 형상관리의 개요

- 핵심 요약 : 생명주기 전반의 형상 항목 변경을 식별·통제·기록·감사하는 소프트웨어 공학 관리 프로세스.
- 개념 : 소프트웨어 생명주기 전반에 걸쳐 요구사항, 설계서, 소스코드, 빌드 스크립트 등 모든 형상 항목(CI, Configuration Item)의 변경 사항을 체계적으로 식별, 통제, 기록, 감사하는 소프트웨어 공학 관리 프로세스.
- 배경 및 필요성 : 다수 개발자 협업 시 발생하는 코드 충돌 방지, 무분별한 요구사항 변경으로 인한 프로젝트 실패 예방, 과거 특정 시점 산출물 복원 보장 필요.
- 표준 근거 : IEEE(Institute of Electrical and Electronics Engineers) 828(형상관리 계획 표준), CMMI(Capability Maturity Model Integration) 형상관리(CM, Configuration Management) 프로세스 영역.

## Ⅱ. 형상관리의 특징

- 핵심 요약 : 베이스라인 중심 통제와 변경 추적성, 감사 기반 품질 보장이 결합된 관리 체계.

1. 요구사항부터 릴리스 산출물까지 형상 항목(CI)의 전수 관리 대상화.
2. 베이스라인(Baseline) 확정을 통한 변경 기준점 관리.
3. 형상통제위원회(CCB, Change Control Board) 중심의 공식적 변경 통제.
4. 기능적·물리적 형상감사를 통한 산출물 일치성 검증.
5. 변경 이력의 상태 보고 및 이해관계자 추적성 확보.

## Ⅲ. 형상관리의 구조 (흐름)

- 핵심 요약 : 식별 → 통제 → 감사 → 기록의 4대 활동 순환 구조.
- 형상관리 4대 활동 흐름.

```text
[ 형상 식별 ] : 형상 항목 선정, 베이스라인 확정
     │
     ▼
[ 형상 통제 ] : 변경요청(CR) 접수, CCB 심의·승인
     │
     ▼
[ 형상 감사 ] : 물리적/기능적 베이스라인 검증
     │
     ▼
[ 형상 기록 ] : 상태 보고, 이력 추적성
```

- 형상 식별(Identification) : 관리 대상 산출물(CI, Configuration Item)의 정의 및 식별 체계(버전, 명명 규칙) 부여.
- 형상 통제(Control) : 변경요청서(CR, Change Request) 접수 및 형상통제위원회(CCB) 심의 승인 후 변경 수행.
- 형상 감사(Audit) : 베이스라인과 실제 산출물의 일치성을 기능적 형상감사(FCA, Functional Configuration Audit)와 물리적 형상감사(PCA, Physical Configuration Audit)로 검증.
- 형상 상태 보고(Status Accounting) : 모든 변경 이력과 현재 형상 상태의 이해관계자 투명 공유.

## Ⅳ. 베이스라인 종류별 비교

- 핵심 요약 : 수립 시점과 포함 형상 항목이 단계별로 구분되는 4계층 베이스라인 체계.
- 베이스라인 계층 진행 흐름.

```text
[ 베이스라인 계층 진행 흐름 ]
기능 베이스라인 → 분배 베이스라인 → 설계 베이스라인 → 제품 베이스라인
 (요구사항)       (기본/논리 설계)    (상세 설계)        (통합·검증 완료)
```

| 베이스라인 종류 | 수립 단계 | 포함되는 주요 형상 항목(CI) |
|---|---|---|
| 기능 베이스라인(Functional) | 요구사항 분석 완료 시점 | 시스템 요구사항 명세서(SRS, Software Requirements Specification), 제안요청서(RFP, Request for Proposal), 업무 정의서 |
| 분배 베이스라인(Allocated) | 기본/논리 설계 완료 시점 | 시스템 아키텍처 설계서, 서브시스템 기능 배분 명세서 |
| 설계 베이스라인(Design) | 상세 설계 완료 시점 | 클래스 다이어그램, DB(Database) ERD(Entity-Relationship Diagram), 인터페이스 연동 정의서 |
| 제품 베이스라인(Product) | 시스템 통합 및 검증 완료 시점 | 최종 릴리스 소스코드, 실행 파일, 운영 매뉴얼, 배포 산출물 |

## Ⅴ. 형상관리의 장점과 한계

- 핵심 요약 : 변경 추적·복원 보장의 장점, 브랜치 통합·승인 병목·형상 누락의 한계.
- 장점
  1. 협업 코드 충돌 방지 및 변경 이력의 완전 추적.
  2. 과거 특정 시점 산출물 복원을 통한 안정성 보장.
  3. 베이스라인·감사 기반의 품질 및 인증 대응력 확보.
- 한계점 1 : 장기 브랜치 운영으로 인한 대규모 통합 충돌(Merge Hell)
  - 한계점 : 별도 기능 브랜치의 수주~수개월 독립 개발 후 메인 브랜치 병합 시 방대한 코드 충돌 및 회귀 결함 발생.
  - 해결 방안 : 트렁크 기반 개발(Trunk-Based Development) 도입을 통한 메인 브랜치 지속적 통합(CI, Continuous Integration), 미완성 기능의 기능 플래그(Feature Toggle) 배포 격리.
- 한계점 2 : 전통적 베이스라인 동결 절차와 클라우드 지속 배포(CD, Continuous Delivery) 간 충돌
  - 한계점 : 변경통제위원회(CCB) 수작업 문서 승인 기반 정적 베이스라인 통제 방식의 일 수십 회 릴리스 마이크로서비스·클라우드 배포 속도 저해.
  - 해결 방안 : GitOps 프레임워크 기반 Git 커밋 해시·태그의 감사 가능 베이스라인 활용, 자동화된 정책 검증(OPA, Open Policy Agent) 기반 CI/CD 파이프라인 승인 간소화.
- 한계점 3 : 인프라 및 환경 구성요소의 형상 누락(Configuration Drift)
  - 한계점 : 소스코드만 버전 관리되고 OS(Operating System) 패치, 네트워크 방화벽, DB 스키마, 클라우드 리소스 설정의 수작업 변경으로 개발·스테이징·운영 환경 간 불일치 발생.
  - 해결 방안 : IaC(Infrastructure as Code, Terraform/Ansible) 기반 인프라 코드화, DVC(Data Version Control)를 통한 데이터 및 AI(Artificial Intelligence) 모델 버전의 단일 형상 관리 체계 통합, Drift 자동 탐지 도구 운영.

## Ⅵ. 현대 클라우드·DevOps 환경에서의 기술사적 제언

- 핵심 요약 : 단기 브랜치 전략 채택과 Everything as Code 기반 형상관리 범위 확대.
- Trunk-Based Development 및 단기 브랜치 전략 채택 : 전통적 Git Flow 장기 브랜치의 대규모 머지 충돌 유발성 감안, 짧은 주기 메인 트렁크 병합 전략과 기능 플래그의 결합을 통한 지속적 통합 속도 극대화.
- 코드 기반 형상(Everything as Code)의 형상관리 범위 확대 : 애플리케이션 소스뿐만 아니라 인프라(Terraform), 파이프라인(Jenkinsfile), 보안 정책(OPA, Open Policy Agent)까지 형상 항목 통합 등록을 통한 완전한 재현성(Reproducibility) 확보.

## Ⅶ. 결론

- 핵심 요약 : 형상관리는 베이스라인 통제와 변경 추적으로 품질·재현성을 보장하는 관리 프로세스.
- 요약 : 4대 활동(식별·통제·감사·기록)과 4계층 베이스라인 체계가 형상관리의 골격.
- 시사점 : Trunk-Based Development, GitOps, IaC로의 확장이 클라우드 시대 형상관리 성숙도의 핵심 전환점.
