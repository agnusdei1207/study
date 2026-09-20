---
title: "CI/CD(Continuous Integration/Continuous Delivery)"
author: "Gemini 3.8 Flash"
date: "2026-09-20T01:00:00+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "기출 · 75%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "135회"
  priority: 75
  priority_note: "[출제:135]"
---

## 답안 골격
```text
[CI/CD] ◀━━ 머리: Ⅶ 내 의견 (Shift-Left 기반 DevSecOps 내재화와 카나리 배포 자동 롤백을 결합한 신뢰 중심 파이프라인 구축)
 ┃
 ┣━ Ⅰ 개요 ───── 장기간 격리 브랜치 개발로 인한 '통합의 지옥(Integration Hell)' → 소스 자동 빌드·테스트 및 무인 배포
 ┣━ Ⅱ 특징 ───── 빈번한 소스 통합(일 1회 이상) · 빌드/테스트 자동화 피드백 · 배포 파이프라인 가시화 · 점진적 배포
 ┣━ Ⅲ 구조 ───── 형상관리(Git) / CI 서버(GitHub Actions, GitLab CI, Jenkins) / 아티팩트 저장소 / CD 엔진(ArgoCD)
 ┣━ Ⅳ 흐름 ───── 코드 커밋 → 정적 분석(SAST) 및 단위 테스트 → 아티팩트 빌드 → 스테이징 자동 배포 → 승인/자동 프로덕션 롤아웃
 ┣━ Ⅴ 비교 ───── 지속적 배포(Continuous Delivery, 수동 승인) vs 지속적 배포(Continuous Deployment, 완전 무인)
 ┗━ Ⅵ 실무 ───── 배포 파이프라인 보안 취약점(시크릿 유출, 오염된 의존성) / DevSecOps 도구 체인(SCA, DAST, 서명) 연계
```
- 필수 키워드: 지속적 통합(CI) · 지속적 제공(CD) · 지속적 배포 · 파이프라인 · 테스트 자동화 · GitOps(ArgoCD) · DevSecOps · 무중단 배포
- 배점 전략: 10점 = Ⅰ 통합 지옥과 CI/CD 정의 → Ⅲ 파이프라인 구성요소 도식 → Ⅴ Delivery vs Deployment 비교 / 25점 = Ⅰ~Ⅶ 전개, 135회 기출 CI/CD 파이프라인 단계별 DevSecOps(SAST/DAST/SCA) 적용 방안
- 기출: 135회 2교시 2번 `CI/CD 파이프라인에서 DevSecOps 적용방안` → Ⅰ~Ⅵ

## 한 줄 본질
- 수개월 치 변경사항을 한 번에 병합할 때 발생하는 충돌과 수작업 배포 장애 병목 → 작은 단위 커밋을 중앙 저장소에 매일 자동 통합하고 테스트를 통과한 아티팩트를 스테이징/운영에 즉시 릴리스하는 자동화 파이프라인 → 리드 타임 단축 및 장애 복구 가속 / 테스트 자동화 구축 비용 수반

## 핵심 그림
```text
+-------------------------------------------------------------------------+
|                  CI/CD + DevSecOps 파이프라인 단계별 흐름               |
+-------------------------------------------------------------------------+
| [Code] ----> [Build & Test] ----> [Package] ----> [Deploy] ----> [Monitor]|
|   |                 |                 |              |              |    |
| IDE 보안 플러그인    SAST(정적 분석)   컨테이너 빌드  GitOps 배포    런타임 보안|
| 시크릿 스캔         단위/통합 테스트   SCA(오픈소스)  (Blue/Green,   (APM, Log) |
| (TruffleHog)       (SonarQube)       이미지 서명    Canary)       (Falco)    |
|                                      (Cosign)      DAST(동적)                |
+-------------------------------------------------------------------------+
```

## 핵심 용어
- 지속적 통합(Continuous Integration): 개발자가 작성한 코드를 중앙 코드 저장소에 빈번하게 병합하고, 매 커밋마다 자동 빌드와 테스트를 실행하여 결함을 조기에 발견하는 프랙티스
- 지속적 제공(Continuous Delivery) vs 지속적 배포(Continuous Deployment): Delivery = 언제든 배포 가능한 빌드 산출물을 프로덕션 직전까지 자동 검증 후 최종 배포는 비즈니스 승인으로 수행 / Deployment = 프로덕션 배포까지 사람의 개입 없이 100% 완전 자동화

## 핵심 통찰
- CI/CD의 성패는 도구(Jenkins, GitHub Actions)가 아니라 "개발자가 기능 브랜치를 오래 유지하지 않고 메인 브랜치에 매일 합치는 트렁크 기반 개발(Trunk-Based Development) 문화"에 달려 있음
- 테스트가 없는 CI/CD는 "결함이 있는 코드를 프로덕션에 더 빠르게 배포하는 재앙 촉진기"에 불과하므로, 철저한 테스트 자동화 게이트가 파이프라인의 전제 조건임
- 현대 CD는 클러스터 외부에서 밀어넣는 푸시(Push) 방식에서, 쿠버네티스 내부 에이전트가 Git의 선언적 명세를 감시하고 일치시키는 GitOps 풀(Pull) 방식으로 진화함

## 이웃 토픽과 구분
- CI/CD vs DevOps: DevOps = 개발과 운영 간의 사일로를 허물고 협업하는 문화이자 조직 철학 / CI/CD = DevOps 철학을 실현하기 위한 기술적 자동화 실행 파이프라인

## 문제·원인·대책
- 적용 상황: 하루 수십 회 배포를 수행하는 이커머스 마이크로서비스 환경
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 배포 스크립트 로그 및 소스코드에 클라우드 API Key 등 자격증명 노출 | 개발 편의를 위한 환경변수 하드코딩 및 로그 마스킹 부재 | HashiCorp Vault 및 Secret Scanner(TruffleHog, Gitleaks) 사전 차단 훅 구성 | 자격증명 유출 사고 100% 원천 예방 |
| 신규 배포 후 치명적 런타임 오류로 인해 전사 서비스 장애 발생 | 전체 인스턴스 일괄 교체(Big-Bang) 방식의 수동 배포 | 카나리(Canary) 배포 및 Prometheus 에러율 기반 자동 롤백(Argo Rollouts) | 장애 영향도 5% 미만 사용자 격리 및 1분 내 자동 복구 |

## 이렇게 출제된다
- 제135회 2교시 2번: "CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오." → 요구 포인트: CI/CD 기본 개념 및 Delivery와 Deployment의 차이 + 단계별(Code, Build, Test, Release, Deploy, Monitor) DevSecOps 도구 및 보안 활동(SAST, DAST, SCA, 이미지 무결성)

## 내 의견
- [배포 속도에만 치중하여 보안 검증을 우회하는 섀도우 파이프라인 위험] 빠른 배포를 이유로 보안 검토를 사후로 미루다 치명적인 오픈소스 공급망 침해(예: Log4j 사태)를 겪는 개발 현장의 딜레마 경계 → 나라면: CI 파이프라인에 SBOM(Software Bill of Materials) 자동 생성 및 SCA(의존성 취약점 스캔)를 필수 품질 게이트로 강제하고, Critical 보안 취약점 발견 시 빌드를 즉시 Fail 처리하는 보안 자동화 가드레일 확립
