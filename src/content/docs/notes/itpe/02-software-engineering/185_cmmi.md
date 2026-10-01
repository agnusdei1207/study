---
title: "CMMI(Capability Maturity Model Integration)"
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

## Ⅰ. CMMI의 개요

- **개념** : 미국 카네기멜론 대학교 소프트웨어 공학 연구소(SEI)에서 조직의 소프트웨어 개발 및 엔지니어링 프로세스 성숙도를 평가하고 지속적으로 개선하기 위해 기존의 개별 능력 성숙도 모델(SW-CMM, SE-CMM, IPD-CMM)들을 하나로 통합한 세계적인 소프트웨어 프로세스 개선 및 성숙도 평가 모델.
- **배경 및 필요성** : 개발자의 개인적 영웅주의에 의존하던 혼돈 상태의 프로젝트 관행을 탈피하여, 조직 차원에서 표준화되고 반복 가능하며 정량적으로 통제되는 예측 가능한 엔지니어링 프로세스 확립.
- **평가 구조** : 5단계 성숙도 레벨(Maturity Level)을 가진 단계적 표현(Staged)과 능력 레벨(Capability Level)을 가진 연속적 표현(Continuous).

## Ⅱ. CMMI 5단계 성숙도 모델(Maturity Level) 계층 구조

```text
   [ Level 5: 최적화 단계 (Optimizing) ] ── 통계적 프로세스 제어 기반의 지속적 혁신 및 결함 예방
                       ▲
                       │
   [ Level 4: 정량적 관리 (Quantitatively Managed) ] ─ 프로세스와 제품 품질의 정량적 측정 및 통계적 통제
                       ▲
                       │
   [ Level 3: 정의 단계 (Defined) ] ─────── 조직 차원의 전사 표준 프로세스 정립 및 테일러링
                       ▲
                       │
   [ Level 2: 관리 단계 (Managed) ] ──────── 프로젝트 단위의 기본적 관리 (요구관리, 계획, 형상관리)
                       ▲
                       │
   [ Level 1: 초기 단계 (Initial) ] ──────── 프로세스 부재, 혼돈(Chaos), 개인의 역량에 전적 의존
```

## Ⅲ. CMMI 핵심 프로세스 영역(PA) 및 단계별 활동

| 성숙도 레벨 | 핵심 포커스 | 대표 프로세스 영역 (PA, Process Areas) |
|---|---|---|
| Level 1: Initial | 예측 불가능한 결과, 위기 관리 | 특정 프로세스 영역 없음 |
| Level 2: Managed | 프로젝트 단위의 체계화 및 반복성 | REQM(요구관리), PP(프로젝트계획), PMC(프로젝트감시통제), CM(형상관리), PPQA(품질보증) |
| Level 3: Defined | 전사적 표준화 및 프로세스 자산화 | RD(요구개발), TS(기술솔루션), VER(검증), VAL(확인), DAR(의사결정분석), OT(조직훈련) |
| Level 4: Quantitatively Managed | 데이터에 기반한 통계적 통제 | QPM(정량적 프로젝트관리), OPP(조직 프로세스 성과) |
| Level 5: Optimizing | 지속적 혁신 및 프로세스 자가 최적화 | CAR(원인분석과 해결), OPM(조직 성과관리) |

## Ⅳ. 현대 엔지니어링 환경에서의 기술사적 제언

- **CMMI 2.0 버전과 애자일/DevOps의 실용적 조화** : 과거 CMMI 1.3의 무거운 문서주의와 관료주의적 감사에 대한 비판을 수용하여 개정된 CMMI 2.0은 스크럼, CI/CD, 자동화 테스트와의 연계를 적극 수용하고 있으므로, '문서를 위한 프로세스'가 아닌 '품질 속도를 높이는 엔지니어링 프로세스'로 테일러링해야 함.
- **국방 및 공공 SW 수주 경쟁력 확보와 실질적 프로세스 내재화** : CMMI 인증이 입찰 참여를 위한 형식적 스펙 쌓기에 그치지 않도록, 실제 형상관리(Git)와 ALM 도구(Jira)에 CMMI의 요구사항 추적성 및 리스크 관리 기준을 워크플로우로 자동 구현하여 전사적 엔지니어링 성숙도 체질 개선.
