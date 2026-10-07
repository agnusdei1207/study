---
title: "NIST AI RMF"
author: "Antigravity"
date: "2026-10-01T22:50:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "기초"
extra:
    keyword_grade: "기초"
    model: "Gemini 3.8 Flash"
---

## Ⅰ. NIST AI RMF의 개요

- 개념 : **미국 국립표준기술연구소** (NIST, National Institute of Standards and Technology)가 제정한 **인공지능 위험관리 프레임워크** (AI RMF, Artificial Intelligence Risk Management Framework 1.0)로, 신뢰할 수 있고 책임 있는 AI(Artificial Intelligence) 시스템을 설계·개발·배포하기 위한 **자발적 지침**
- 배경 및 필요성 : AI 시스템의 블랙박스 특성, 환각(Hallucination), 편향성, 프라이버시 침해, 보안 취약점 등 새로운 AI 고유 위험을 체계적으로 통제할 글로벌 표준 체계 필요.
- 주요 목적 : AI 위험의 조기 식별 및 완화, 신뢰성 있는 AI 특성(유효성, 신뢰성, 안전성, 투명성, 공정성, 프라이버시) 내재화, 책임성 있는 AI 거버넌스 확립.

## Ⅱ. NIST AI RMF의 4대 핵심 기능 (Functions)

```text
               ┌─────────────── GOVERN (거버넌스) ───────────────┐
               │    AI 위험관리 문화, 정책, 책임 및 프로세스 수립  │
               └───────────────────────┬────────────────────────┘
                                       │
         ┌─────────────────────────────┼─────────────────────────────┐
         ▼                             ▼                             ▼
   [MAP (맥락 파악)]            [MEASURE (측정 및 평가)]       [MANAGE (위험 완화)]
  - 시스템 맥락 및 한계 식별     - 정량/정성 위험 지표 측정     - 우선순위 기반 위험 대응
  - 잠재적 위험 및 영향 분석    - 모델 편향/정확도 평가        - 지속적 모니터링 및 개선
```

- **GOVERN** (거버넌스) : AI 위험관리 문화, 정책, 책임 및 프로세스 수립.
- **MAP** (맥락 파악) : 시스템 맥락 및 한계 식별, 잠재적 위험 및 영향 분석.
- **MEASURE** (측정 및 평가) : 정량·정성 위험 지표 측정, 모델 편향·정확도 평가.
- **MANAGE** (위험 완화) : 우선순위 기반 위험 대응, 지속적 모니터링 및 개선.

| 핵심 기능 | 영문 명칭 | 주요 활동 내용 |
|---|---|---|
| 거버넌스 | GOVERN | 전사적 AI 위험관리 정책 수립, R&R(Roles and Responsibilities) 정의, 위험 수용 한도 설정 및 조직 문화 조성 |
| 맥락 파악 | MAP | 비즈니스 맥락 분석, 배포 환경 정의, 이해관계자 영향 및 잠재 위험 목록화 |
| 측정 및 평가 | MEASURE | AI 성능, 공정성, 견고성 지표 측정, 감사 도구 활용 실측 및 지속적 평가 |
| 위험 관리 | MANAGE | 식별·측정된 위험의 완화 조치 수행, 비상대책 수립, 사고 대응 및 잔여위험 관리 |

## Ⅲ. 생성형 AI 프로파일 (NIST AI 600-1)의 주요 위험 대응

- 2024년 발표된 **NIST AI 600-1** (Generative AI Profile)은 생성형 AI 특화 12대 위험(환각, 유해 콘텐츠, 악의적 사용, 지식재산권 침해, 프라이버시 침해 등)을 규정.
- **프롬프트 인젝션** (Prompt Injection) 방어, RAG(Retrieval-Augmented Generation) 기반 환각 억제, **워터마킹** (Watermarking) 및 **출력 필터링**을 필수 완화 조치로 제시.

## Ⅳ. NIST AI RMF 적용 시 주요 한계점 및 해결 방안

- 프레임워크의 자율 규제적 성격과 강제성 부재 :
  - 한계점 : 체크리스트 형태의 포괄적 가이드라인으로 법적 구속력이 없어 기업들이 비용 부담을 이유로 형식적 도입에 그칠 위험.
  - 해결 방안 : AI 서비스 조달 및 공공 사업 제안 시 NIST AI RMF(Risk Management Framework) 준수 여부를 평가 지표에 연계, 내부 AI 규정 및 업무 감사에 반영.
- 정량적 위험 측정 지표의 표준화 미비 :
  - 한계점 : 신뢰성, 공정성, 투명성 등 정성적 가치를 엔지니어링 수준에서 통과/실패(Pass/Fail)로 판정할 정량 기준 모호.
  - 해결 방안 : 벤치마크 데이터셋(HELM 등)을 활용한 정량 평가 파이프라인 구축, 설명가능성(XAI, Explainable Artificial Intelligence) 및 편향 지표의 임계치 수치화.
- AI 생애주기 전반의 지속적 모니터링 공수 과다 :
  - 한계점 : 모델 배포 후에도 데이터 드리프트, 적대적 공격, 환각을 실시간 추적해야 하므로 MLOps(Machine Learning Operations) 운영 비용 급증.
  - 해결 방안 : 자동화된 AI 관측성(Observability) 솔루션 도입, CI(Continuous Integration)/CD(Continuous Delivery) 파이프라인에 AI 거버넌스 가드레일 자동 검증 결합.

## Ⅴ. NIST AI RMF 적용을 위한 기술사적 제언

- 조직 내 AI 윤리 및 거버넌스 위원회 설치 : GOVERN 기능의 실질적 작동을 위해 법무, 기술, 비즈니스, 보안 부서가 참여하는 협의체를 구성하여 고위험 AI 도입 심의.
- MLOps 파이프라인과 RMF 기능의 통합 자동화 : 모델 개발부터 배포까지 CI/CD 파이프라인 내에 편향성 검사, 적대적 공격 테스트, 모델 드리프트 감지를 자동화.
- 국내외 규제(EU(European Union) AI Act, 한국 AI 기본법)와의 정합성 유지 : 위험 기반 접근법(Risk-based approach)에 입각하여 시스템 등급에 따른 차등화된 통제 기준 적용.
