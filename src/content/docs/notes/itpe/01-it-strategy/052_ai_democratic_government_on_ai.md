---
title: "AI 민주정부 / 온AI"
author: "Antigravity"
date: "2026-09-20T19:45:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "Gemini 3.8 Flash (High)"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 디지털 혁신 및 전자정부를 거쳐 AI 민주정부와 온AI로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 디지털 혁신·전자정부</span>
  <strong>AI 민주정부 / 온AI</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **AI 민주정부(온AI)**는 국민이 혜택을 찾아 신청하기 전에 AI가 알아서 필요한 복지·행정 서비스를 선제 공급하고, 공무원의 정책 기획을 인공지능이 보조하는 전 공공 프로세스 내재화 정부 모델
- 메커니즘: `대국민 선제 서비스 + 공무원 온AI 워크스페이스 + 범정부 AI 공통 인프라` 3계층을 구축하고, **sLLM(Small Large Language Model)**과 **RAG(Retrieval-Augmented Generation)**로 행정 환각 억제
- 산출: 맞춤형 혜택알리미 · 공무원 온나라 AI 플러그인 · 법령 행정 RAG 벡터 지식베이스 · **MLS(Multi-Level Security)** 기반 보안 격리 환경

<div class="itpe-flow-map" role="img" aria-label="AI 민주정부 온AI 추진 모델 및 3대 계층 구조">
  <div class="itpe-flow-node">
    <strong>신청주의 행정 패러다임 극복</strong>
    <small>복지 사각지대 해소 · 단순 반복 공문서 업무 혁신</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>AI 민주정부(온AI) 3대 계층 체계</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>대국민</strong><span><span class="itpe-keyword"><strong>혜택알리미</strong></span> · 24/365 맞춤형 지능형 민원 상담</span></div>
      <div class="itpe-flow-branch"><strong>공무원</strong><span>온AI 워크스페이스 · 기안문 초안 작성 · 정책 시뮬레이션</span></div>
      <div class="itpe-flow-branch"><strong>인프라</strong><span>공공 특화 <span class="itpe-keyword"><strong>sLLM</strong></span> · 법령 <span class="itpe-keyword"><strong>RAG</strong></span> · 다층 보안 체계(<span class="itpe-keyword"><strong>MLS</strong></span>)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>선제적 지능 행정 및 투명한 공공 의사결정</strong>
    <small>Human-in-the-loop 최종 검인 · 대국민 신뢰 행정 달성</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **온AI(On-AI)**: 특정 부가 서비스가 아닌 공공 행정 및 시스템 프로세스 전반에 AI를 기본 탑재하는 내재화 원칙
- **sLLM(Small Large Language Model)**: 공공 행정 도메인 문서에 특화하여 파인튜닝된 저비용·고효율 경량 거대언어모델
- **RAG(Retrieval-Augmented Generation)**: 외부 공공 법령 및 행정 지침 벡터 DB를 실시간 검색하여 환각 현상을 억제하는 생성 기술
- **MLS(Multi-Level Security)**: 국가정보원이 주도하는 기밀(C), 민감(S), 공개(O) 등급별 데이터 차등 보호 및 보안 통제 체계
- **DPG(Digital Platform Government)**: 부처 간 데이터 칸막이를 해소하고 하나의 플랫폼으로 국민에게 서비스하는 디지털플랫폼정부
- **혜택알리미**: 정부가 보유한 공공 마이데이터를 분석하여 국민 상황에 맞는 수혜 서비스를 추천·선제 알림하는 지능형 대민 서비스
- **Human-in-the-loop**: 인공지능이 생성한 기안문과 복지 처분 추천을 인간 공무원이 최종 검토·서명하는 법적 책임 보장 장치

</details>

## 예상문제

> 공공 행정의 생산성 혁신과 대국민 맞춤형 복지 서비스 제공을 위한 'AI 민주정부(온AI)'의 추진 배경과 3대 계층 아키텍처, 기존 전자정부·디지털플랫폼정부(DPG)와의 차이점, 행정 sLLM 및 RAG 기반 구현 방안과 다층 보안 체계(MLS) 연계 대책을 설명하시오. (25점)

## Ⅰ. 신청주의 행정 극복과 지능형 공공 혁신, AI 민주정부의 개요

> AI 민주정부는 **온AI(On-AI)** 내재화를 통해 국민이 찾기 전에 복지를 공급하는 선제 행정 모델이며, 성패는 **행정 환각(Hallucination) 억제**와 **다층 보안 체계(MLS)** 준수로 판정함.

- 정의: 정부의 모든 행정 업무와 대국민 서비스 접점에 인공지능을 기본 탑재(On-AI)하여, 맞춤형 혜택을 선제 제공하고 공무원의 초지능 업무 보조를 실현하는 **차세대 공공 거버넌스 모델**
- 목적: 복지 사각지대 해소, 공공 데이터 기반 정책 수립 통한 **선제적 맞춤 행정** 구현 및 대국민 신뢰 회복

## Ⅱ. 전자정부 vs 디지털플랫폼정부(DPG) vs AI 민주정부(온AI) 비교

> 단순 오프라인 문서 전산화(전자정부)와 부처 간 데이터 칸막이 연계(DPG)를 넘어, 인공지능이 스스로 맥락을 분석하고 선제 처분하는 온AI 체계로 진화함.

| 비교 항목 | 전자정부 (e-Government) | 디지털플랫폼정부 (DPG) | AI 민주정부 (On-AI Government) |
|---|---|---|---|
| **행정 패러다임** | 종이 문서의 디지털 전산화 | 부처 간 데이터 연계 및 칸막이 해소 | 전 행정 프로세스에 AI 상시 내재화 |
| **서비스 공급 방식** | 대국민 온라인 신청주의 (창구 일원화) | 통합 포털 기반의 원스톱 연계 | **선제적 맞춤형 서비스(혜택알리미)** |
| **핵심 기술 기반** | 웹 포털 · RDBMS · 전자정부 프레임워크 | 클라우드 네이티브 · 오픈 API · 데이터 댐 | **생성형 AI** · **공공 sLLM** · **행정 RAG** |
| **의사결정 주체** | 담당 공무원의 직관 및 서류 심사 | 부처 결합 정량 데이터 분석 | AI 정책 시뮬레이션 및 인간 최종 검인 |
| **보안 체계** | 물리적 망분리 (내부망/인터넷망 분리) | 공공 클라우드 CSAP 보안 인증 | **다층 보안 체계(MLS)** 데이터 등급 통제 |
| **대표 서비스** | 정부24 · 홈택스 · 나라장터 | 공공 마이데이터 · 복지멤버십 | 온AI 워크스페이스 · AI 국민비서 |

## Ⅲ. 온AI 공공 행정 서비스 3대 계층 아키텍처

> 공무원의 일상 업무와 대국민 서비스가 공통 AI 플랫폼 및 안전한 다층 보안 체계 위에서 단절 없이 유기적으로 연동되어야 함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="AI 민주정부 온AI 3대 계층 아키텍처">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 대국민 선제적 서비스 계층</strong></span>
    <div class="itpe-step-detail"><strong>핵심 기능</strong><span>맞춤형 혜택알리미, 24/365 대화형 민원 상담, 위기가구 발굴</span></div>
    <div class="itpe-step-detail"><strong>목표·효과</strong><span>신청주의 탈피 및 취약계층 선제적 복지 공급</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 공무원 온AI 워크스페이스 계층</strong></span>
    <div class="itpe-step-detail"><strong>핵심 기능</strong><span>온나라 전자결재 AI 플러그인, 기안문 초안 작성, 법령 RAG 검색</span></div>
    <div class="itpe-step-detail"><strong>목표·효과</strong><span>공무원 단순 서류 작업 경감 및 데이터 기반 정책 기획</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 범정부 AI 공통 인프라 계층</strong></span>
    <div class="itpe-step-detail"><strong>핵심 기능</strong><span>공공 특화 sLLM, 법령·지침 벡터 지식베이스, MLS 보안 게이트웨이</span></div>
    <div class="itpe-step-detail"><strong>목표·효과</strong><span>행정 환각 억제, 개인정보 마스킹 및 보안 등급별 차등 통제</span></div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Trust & Security Loop</strong></span> · 행정 데이터 가명화 ↔ sLLM/RAG 검색 ↔ 공무원 최종 승인 ↔ 대민 처분</div>

## Ⅳ. 공공 폐쇄망 구축형(sLLM) vs 상용 클라우드 연계형 LLM 비교

> 행정 기밀과 민감 정보를 다루는 내부 업무는 폐쇄망 sLLM을 적용하고, 공개 대민 서비스는 상용 클라우드를 연계하는 하이브리드 전략이 요구됨.

| 비교 항목 | 공공 폐쇄망 구축형 (**sLLM**) | 상용 클라우드 연계형 (Public LLM) |
|---|---|---|
| **데이터 보안성** | 행정망 내부 격리로 국가 기밀 유출 원천 차단 | 외부 API 호출 시 프롬프트 데이터 유출 리스크 |
| **망분리 규제 부합** | 폐쇄망 내부 온프레미스 인프라로 완벽 준수 | **다층 보안 체계(MLS)** 적용 시 공개(O) 데이터만 연동 가능 |
| **추론 능력** | 행정 도메인 특화 작업에 강력하나 범용 상식 한계 | 방대한 파라미터 기반의 압도적 범용 지능 및 다국어 지원 |
| **TCO 및 구축 비용** | GPU 서버 구매 및 초기 클러스터 구축 고비용 | 토큰 사용량 기반 종량제 과금으로 초기 비용 저렴 |
| **적용 권장 업무** | 비공개 기안문 작성 · 내부 감사 · 국방·외교 정책 | 대국민 민원 질의응답 · 공개 보도자료 배포 · 관광 안내 |

## Ⅴ. 실무 추진 시 장애 요인 및 기술사적 통제 대책

> 행정 시스템의 AI 적용은 거짓 정보 처분 시 법적 분쟁을 야기하므로 기술적 검증과 거버넌스 통제가 필수적임.

| 위험 | 대책 | 효과 |
|---|---|---|
| **행정 기밀 외부 유출** | 행정망 내 **프라이빗 sLLM** 구축 및 PII 마스킹 게이트웨이 강제 | 외부 트래픽 차단, 개인식별정보 유출 방지 |
| **환각(Hallucination)에 의한 오처분** | 법령 조항 원문 임베딩 기반 **행정 RAG** 구축 및 원본 출처 각주 강제 | 인용 법령 조항 일치율 100% 확보, 환각 오처분 억제 |
| **알고리즘 편향에 따른 복지 누락** | **설명가능한 AI(XAI)** 판정 근거 제시 및 이의신청 절차 의무화 | 복지 대상자 선정 공정성 확보, 소외계층 누락 방지 |
| **물리적 망분리로 인한 혁신 지연** | 국가정보원 **다층 보안 체계(MLS)** 기반 데이터 등급별 차등 접근 | 기밀·민감·공개 등급별 유연한 AI 활용 및 망연계 보안 |

## Ⅵ. 인간 최종 책임(Human-in-the-loop) 중심의 결론

> 인공지능은 공무원의 판단을 돕는 초지능 보조자이며, 대국민 처분의 궁극적 법적 책임은 인간 공무원이 지는 **Human-in-the-loop** 거버넌스가 확립되어야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 온AI 정부의 본질은 기술 도입 자체가 아니라, AI의 생성 결과물에 대해 공무원이 법적 책임을 질 수 있도록 투명한 근거 추적성과 서명 프로세스를 시스템적으로 강제하는 데 있음.
- 나라면: 모든 AI 생성 행정 문서에 `프롬프트 버전 + 참조 법령 RAG 출처 + 신뢰도 점수`를 메타데이터로 영구 결합하고 공무원의 전자서명 없이는 결재 진행이 불가능한 강제 Quality Gate를 설계하겠음.

### 실전 답안용 기술사적 제언

- 판정: AI 추천을 자동 처분하지 않고 공무원 최종 검인 프로세스 확립 여부로 성패 판정
- 대안: **온나라 전자결재 연동 Human-in-the-loop 게이트웨이** 및 **법령 RAG 감사 로그** 구축
- 검증: 모든 AI 행정 처분 문서의 출처 각주 매핑률 100% · 담당관 전자서명 필수 통과
- 효과: 행정 처분 무결성 확보 · 법적 소송 리스크 차단 · 선제적 대국민 복지 신뢰 증대

<div class="itpe-pipeline is-vertical" role="img" aria-label="온AI 정부 신뢰성 및 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제점</strong><span>신청주의 복지 사각지대, 환각 오처분 리스크, 망분리 규제 경직</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>추진 전략</strong><span>공공 sLLM/RAG 기반 온AI 워크스페이스 구축 및 MLS 보안 체계 적용</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>관리 지표</strong><span>법령 출처 각주 매핑 100%, Human-in-the-loop 최종 검인 의무화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>최종 효과</strong><span>선제적 맞춤 행정 실현, 행정 무결성 보증, 대국민 신뢰 회복</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **AI 민주정부(온AI)**는 정부 행정 시스템 전반에 AI를 기본 내재화하여 대국민 맞춤 혜택을 선제 공급하고 공무원 업무를 지능화하는 차세대 공공 거버넌스 모델
- 목적: 신청주의 행정 한계 극복, 행정 오류 감소 통한 **선제적 맞춤 행정** 구현 및 공공 생산성 혁신

### 2. 온AI 3대 계층 체계

<div class="itpe-pipeline is-vertical" role="img" aria-label="온AI 핵심 3계층 요약 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>대국민 계층</strong>
    <div class="itpe-step-detail"><strong>선제 서비스</strong><span>혜택알리미 및 24/365 AI 민원 비서</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>공무원 업무 계층</strong>
    <div class="itpe-step-detail"><strong>지능형 보조</strong><span>온AI 워크스페이스, 기안 초안 및 법령 질의</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>공통 인프라 계층</strong>
    <div class="itpe-step-detail"><strong>기반 기술</strong><span>행정 특화 sLLM, 법령 RAG, 다층 보안(MLS)</span></div>
  </div>
</div>

### 3. 핵심 통제

- **행정 RAG 환각 억제**: 법령 및 행정규칙 원문 벡터 데이터베이스를 실시간 검색 인용하여 가짜 법조문 인용 원천 차단
- **Human-in-the-loop 원칙**: AI는 초안 작성 보조자로 제한하고, 최종 결재 및 대국민 처분의 법적 책임은 공무원이 직접 서명 검인

## 출제 이력과 검증 출처

- 디지털플랫폼정부위원회 및 행정안전부, '온AI 정부 추진계획 및 대국민 혜택알리미 로드맵'
- 국가정보원, '국가 망보안체계 다층보안체계(MLS) 전환 종합계획' (2024)
- 한국지능정보사회진흥원(NIA), '생성형 AI 공공부문 도입 가이드라인'

## 학습 체크

- [ ] 전자정부, 디지털플랫폼정부(DPG), AI 민주정부(온AI)의 핵심 차이를 비교할 수 있는가?
- [ ] 온AI 정부의 3대 계층(대국민, 공무원, 공통 인프라)을 도식화할 수 있는가?
- [ ] 공공 폐쇄망 sLLM과 상용 LLM의 장단점 및 적용 기준을 제시할 수 있는가?
- [ ] 행정 RAG와 Human-in-the-loop가 갖는 공학적·법적 의미를 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [AI 고속도로](./051_ai_highway.md)
- 연관 토픽: [범정부 AI 공통기반](./025_pan_government_ai_common_infrastructure.md), [공공 클라우드 전환](./021_public_cloud_native_transition.md)
- 다음 토픽: [AI 프라이버시 위험관리 모델](./054_ai_privacy_risk_management_model.md)
