---
title: "AI 생성 코드·오픈웨이트 라이선스 준수"
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

## Ⅰ. AI 생성 코드 및 오픈웨이트 라이선스 준수의 개요

- 개념 : **대형 언어 모델** (LLM, Large Language Model) 기반의 코딩 도우미가 생성한 소스코드와 LLaMA 등 **오픈웨이트** (Open-Weight) AI(Artificial Intelligence) 모델을 기업 시스템에 도입할 때 발생하는 저작권 침해, 오픈소스 **카피레프트** 라이선스 전염, 모델 사용 조건 위반 리스크를 식별하고 법적·기술적 컴플라이언스를 확보하는 거버넌스 체계.
- 배경 및 필요성 : AI 모델이 GPL(GNU General Public License)/AGPL(GNU Affero General Public License) 등 엄격한 카피레프트 라이선스가 부여된 코드를 학습한 후 그대로 암기하여 출력(Ghostwriting)하거나, 상업적 사용이 제한된 오픈웨이트 모델을 무단 배포함으로써 발생할 수 있는 저작권 소송 및 기업 **지적재산권** (IP, Intellectual Property) 침해 위험 대두.
- 핵심 통제 대상 : AI 생성 코드의 저작권 귀속 여부, 학습 데이터 내 라이선스 오염, 오픈웨이트 모델의 라이선스 제약(Community/Commercial Use 제약).

## Ⅱ. AI 생성 코드의 위험 전파 경로 및 컴플라이언스 파이프라인

```text
   [ 오픈소스 학습 데이터 (GPL 등) ] ──> [ LLM 모델 학습 ] ──> [ AI 코딩 도구 (Copilot 등) ]
                                                                       │
                                                                       ▼
   [ 개발자 프롬프트 입력 ] ──────────────────────────────────> [ AI 생성 코드 제안 ]
                                                                       │
                                   ┌───────────────────────────────────┴───────────────────────────────────┐
                                   ▼                                                                       ▼
                 [ 코드 유사도 및 스니펫 매칭 검사 ]                                      [ SAST(Static Application Security Testing) 보안 약점 자동 진단 ]
                 - Black Duck, FOSSID, GitHub 필터링                                      - SonarQube, Snyk 보안 검사
                                   │                                                                       │
                                   ▼                                                                       ▼
                 [ 합격: 코드베이스 병합 (Merge) ] <────────────────────────────────────── [ 품질 및 라이선스 승인 ]
```

- **유령 작성** (Ghostwriting) 및 무단 복제 검출 : AI가 생성한 코드가 특정 오픈소스 원본과 100% 일치할 경우를 대비하여 **공용 코드 매칭 필터** (Public Code Match Filter) 작동.
- 오픈웨이트 라이선스의 비(非) 오픈소스성 인지 : LLaMA, Mistral 등 다수의 모델은 **OSI** (Open Source Initiative) 승인을 받지 않은 자체 라이선스를 채택하고 있어(월간 활성 사용자 수 제한, 경쟁 AI 학습 금지 등), 상용 서비스 적용 시 법적 조건 면밀 검토 필수.

## Ⅲ. 전통적 오픈소스 컴플라이언스와 AI 환경 컴플라이언스 비교

| 비교 항목 | 전통적 오픈소스 라이선스 | AI 생성 코드 및 오픈웨이트 모델 |
|---|---|---|
| 법적 저작권 인정 여부 | 인간 창작물로서 저작권 명확히 인정 | 인간의 창작적 기여 없는 순수 AI 결과물은 저작권 불인정 추세 |
| 오염 경로 | 개발자가 명시적으로 다운로드 및 라이브러리 링크 | AI 프롬프트 응답으로 무의식적 스니펫 유입 (암묵적 오염) |
| 라이선스 조건 | OSI 인증 표준 (MIT, Apache, GPL 등) | 오픈웨이트 모델별 비표준 제약조건 (예: LLaMA 3 Community License) |
| 검증 도구 | 패키지 의존성 파일(pom.xml, package.json) 분석 | **소스코드 유사도 비교** (Snippet Matching) 및 프롬프트 추적 |
| 법적 분쟁 리스크 | 전염성 라이선스에 따른 상용 소스코드 강제 공개 | 학습 데이터 저작권 침해 손해배상 및 영업비밀 유출 위험 |

## Ⅳ. AI 생성 코드 및 라이선스 준수의 주요 한계점 및 해결 방안

- AI 모델 학습 데이터의 블랙박스 특성으로 인한 저작권 침해 위험 :
  - 한계점 : LLM이 학습한 수십억 라인의 공개 코드 중 엄격한 카피레프트(GPL/AGPL) 코드가 포함되어 있어, AI가 생성한 코드가 원본을 거의 그대로 출력할 경우 기업 소스코드 공개 의무 등 법적 분쟁 초래.
  - 해결 방안 : AI 코딩 도구 내 '공개 코드 일치 제안 차단(Block suggestions matching public code)' 설정을 강제 활성화하고, CI(Continuous Integration) 파이프라인에 코드 유사도 검색 엔진(Black Duck, GitHub Copilot Scanner) 전수 스캔 연동.
- 오픈웨이트(Open-Weight) 모델의 특수 사용 제약 조건 위반 :
  - 한계점 : Llama, DeepSeek 등 오픈웨이트 모델 라이선스에 포함된 상업적 사용자 수 상한(월간 활성 사용자 7억 명 등), 타 모델 증류(Distillation) 학습 금지 등 특수 라이선스 조항을 간과하여 라이선스 위반 발생.
  - 해결 방안 : 기업 내 AI 거버넌스 위원회를 통해 도입 전 모델별 특수 라이선스 약관을 법률 검토하고, 사내 활용 목적(상용 서비스, 내부 도구, 파인튜닝)에 따른 허용 모델 화이트리스트 운영.
- 소프트웨어 자재명세서(SBOM, Software Bill of Materials) 내 AI 생성 자산 추적성 누락 :
  - 한계점 : 개발자가 AI를 활용해 작성한 코드 스니펫, 프롬프트 엔지니어링 이력, 활용된 모델 버전이 기존 형상관리 및 SBOM에 기록되지 않아 향후 라이선스 감사 시 증빙 불가.
  - 해결 방안 : AI 생성 코드에 대한 메타데이터 태깅(AIGC, AI-Generated Content Tagging)을 의무화하고, AI-SBOM(AIBOM, AI Bill of Materials) 생성 파이프라인을 구축하여 프롬프트, LLM 버전, 생성 일자 및 의존성 계보(Provenance) 추적성 확보.

## Ⅴ. 기업 AI 거버넌스 확립을 위한 기술사적 제언

- 코드 스니펫 매칭 필터 활성화 및 SCA(Software Composition Analysis) 도구 통합 : GitHub Copilot의 'Match public code' 차단 설정을 전사적으로 강제 활성화하고, 커밋 파이프라인에 Black Duck 등 스니펫 매칭 기능을 연동하여 무단 복제 코드의 유입 차단.
- AI 활용 가이드라인 수립 및 인체 개입(Human-in-the-Loop) 원칙 제도화 : AI 생성 코드는 초안(Draft)으로만 취급하고, 반드시 숙련된 개발자가 직접 검토·수정 및 서명(Sign-off)하여 배포하도록 함으로써 저작권 인정 가능성을 확보하고 품질 결함에 대한 인간의 최종 책무성 확립.
