---
title: "DevSecOps"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:45:00+09:00"
tags:
  - "notes-security"
sidebar:
  badge:
    text: "기출 · 81%"
extra:
  model: "Gemini 3.8 Flash"
  source_status: "기출"
  source_history: "135회"
  priority: 81
  priority_note: "[출제:135]"
---

## 답안 골격
```text
[DevSecOps] ◀━━ 머리: Ⅶ 내 의견 (사후 보안 감사 탈피 → CI/CD 전 단계 보안 자동화 및 시프트 레프트(Shift-Left) 문화 정착)
 ┃
 ┣━ Ⅰ 개요 ───── 빠른 배포를 추구하는 DevOps와 사후 통제 위주의 보안 간 마찰 해소 → 개발·운영 파이프라인 전 주기에 보안을 내재화(Shift-Left)
 ┣━ Ⅱ 특징 ───── 보안 좌측 이동(Shift-Left) · 보안 코드화(Security as Code) · 자동화된 품질 게이트 · 협업 및 책임 공유 문화
 ┣━ Ⅲ 구조 ───── 계획(위협모델링) · 코딩(사전커밋/IDE 린트) · 빌드(SAST/SCA) · 테스트(DAST/IAST) · 릴리즈/배포(IaC/컨테이너 스캔) · 운영(RASP)
 ┣━ Ⅳ 흐름 ───── ① 코드 커밋 시 시크릿 스캔 → ② PR 빌드 시 정적분석(SAST) 및 오픈소스 점검(SCA) → ③ 통합 테스트 시 동적분석(DAST) → ④ 취약점 차단 게이트 통과 시 자동 배포
 ┣━ Ⅴ 비교 ───── 전통 개발 보안(배포 직전 수동 침투테스트, 출시 지연 유발) vs DevSecOps(파이프라인 단계별 자동 점검 및 즉각 피드백)
 ┗━ Ⅵ 실무 ───── 과도한 오탐으로 인한 빌드 중단(개발자 피로) / 오픈소스 공급망 취약점 / IaC 설정 오류 / 런타임 보안 연계
```
- 필수 키워드: DevSecOps · 시프트 레프트(Shift-Left) · CI/CD 파이프라인 · SAST · DAST · SCA · IaC 보안 · RASP
- 배점 전략: 10점 = Ⅰ 정의 및 필요성 → Ⅲ CI/CD 단계별 보안 도구 매핑 도식 → Ⅴ 전통 보안 대비 비교 / 25점 = Ⅰ~Ⅶ 전개, 파이프라인 단계별 보안 통제 기법과 Ⅵ 오탐 완화 및 개발자 경험(DX) 개선 방안 집중
- 기출: 135회 2교시 2번 `CI/CD 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오.` → Ⅲ CI/CD 연계 아키텍처 + Ⅳ 절차 + Ⅵ 실무 적용 방안

## 한 줄 본질
- 배포 직전 마지막 관문에서 수동으로 수행하던 보안 진단으로 인한 출시 지연 병목 → 소프트웨어 개발 생애주기(SDLC) 초기부터 CI/CD 파이프라인에 자동화된 보안 검증 도구를 결합 → 결함 조기 발견 및 수정 비용 최소화 / 파이프라인 빌드 시간 증가 및 도구 관리 비용 발생

## 핵심 그림
```text
[CI/CD 파이프라인 단계별 DevSecOps 도구 및 보안 활동 매핑]

 [Code] ─────> [Build] ─────> [Test] ─────> [Deploy] ─────> [Operate]
   │             │              │              │               │
   ├─ IDE 린터   ├─ SAST        ├─ DAST        ├─ IaC 스캔     ├─ RASP
   ├─ 시크릿검사 ├─ SCA         ├─ IAST        ├─ 이미지 서명  ├─ WAF
   └─ Pre-commit └─ SBOM 생성   └─ 모의침투    └─ 정책 검증    └─ SIEM/SOAR
   (Shift-Left)                                             (Shift-Right)
```

## 핵심 용어
- SAST(Static Application Security Testing): 실행하지 않고 소스코드 텍스트를 파싱하여 잠재적 보안 취약점(CWE)을 찾는 정적 분석 도구
- DAST(Dynamic Application Security Testing): 실행 중인 애플리케이션 외부에 가상 공격 요청을 전송하여 실제 응답을 분석하는 동적 분석 도구
- SCA(Software Composition Analysis): 프로젝트가 의존하는 오픈소스 라이브러리 목록을 식별하고 알려진 취약점(CVE)과 라이선스 위험을 검사하는 도구

## 핵심 통찰
- 보안 도구를 파이프라인에 넣었다고 DevSecOps가 아님 → 매 빌드마다 수십 개의 오탐(False Positive)으로 빌드가 실패하면 개발팀은 보안 도구를 비활성화함
- 취약점 수정 비용은 배포 후 운영 단계가 개발 단계보다 30배 이상 큼 → 개발자가 코드를 작성하는 IDE 단계에서 즉시 경고해 주는 것이 비용 절감의 핵심
- '완벽한 차단'보다 '위험 허용 기준의 코드화(Policy as Code)'가 중요함 → Critical 취약점만 빌드를 중단(Block)시키고, 나머지는 이슈 트래커(Jira)로 자동 발권해 협업 속도를 유지해야 함

## 이웃 토픽과 구분
- DevOps vs DevSecOps: DevOps = 개발과 운영의 통합으로 배포 속도 극대화 / DevSecOps = 배포 속도를 희생하지 않고 파이프라인 전 과정에 보안 검증을 내재화

## 문제·원인·대책
- 사례: CI/CD에 SAST 도구를 도입했으나 수백 건의 경미한 취약점 오탐으로 매번 배포가 중단되어 개발 부서의 거센 반발에 직면한 사례
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 잦은 오탐으로 인한 개발 파이프라인 병목 | 일률적 기본 룰셋 적용 및 조직 맥락을 고려하지 않은 차단 설정 | High/Critical 취약점만 차단하는 품질 게이트(Quality Gate) 테일러링 | 빌드 성공률 유지 및 핵심 보안 취약점 선별 대응 |
| 배포된 클라우드 인프라의 보안 설정 오류 | Terraform 등 IaC 템플릿의 보안 취약 설정 검증 부재 | Checkov, tfsec 등 IaC 정적 스캔을 PR 단계에 자동화 | S3 버킷 공개 등 인프라 설정 오류 사전 차단 |

## 이렇게 출제된다
- 제135회 2교시 2번: "CI/CD(Continuous Integration/Continuous Delivery or Continuous Deployment) 파이프라인에서 DevSecOps 적용방안에 대하여 설명하시오." → 요구 포인트: Ⅰ DevSecOps 필요성 + Ⅲ CI/CD 단계별 보안 도구 연계 방안 + Ⅵ 성공적인 조직 도입 전략

## 내 의견
- [보안팀의 경찰관 마인드 잔존 문제] 보안팀이 파이프라인에 도구만 강제 삽입하고 결함 수정 책임을 전적으로 개발자에게 떠넘겨 부서 간 장벽이 고착화됨 → 나라면: 보안 챔피언(Security Champion) 제도를 도입해 개발팀마다 보안 전담 개발자를 육성하고, 취약점 발견 시 원클릭 패치 가이드 및 코드 수정 제안(Autofix PR)을 자동 생성해 개발자 생산성을 보장

## 찾아볼 것
- OpenSSF Scorecard를 활용한 오픈소스 의존성 보안 건전성 자동 평가
