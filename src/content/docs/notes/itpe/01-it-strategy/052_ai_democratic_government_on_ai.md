---
title: "AI 민주정부·온AI"
author: "OpenAI Codex"
date: "2026-09-22T02:25:00+09:00"
tags: ["notes-it-strategy"]
sidebar:
  badge:
    text: "B"
extra:
  keyword_grade: "B"
  model: "GPT-5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략 관리에서 디지털정부와 공공 AI를 거쳐 AI 민주정부 온AI로 이어지는 지식 위치">
  <span>IT 전략·관리</span><span>디지털정부·공공 AI</span><strong>AI 민주정부·온AI</strong>
</div>

## 큰 그림과 30초 인출

- 본질: AI로 국민서비스·정책참여·공무원 업무를 개선하는 공공 AX 모델
- 구조: 대국민 서비스 → 공무원 업무지원 → 범정부 AI 공통기반
- 통제: 적법한 데이터·근거 제시·Human Oversight·이의제기·감사추적

<div class="itpe-svg-map">
<svg viewBox="0 0 760 590" role="img" aria-label="범정부 AI 공통기반 위에서 공무원 업무지원과 대국민 서비스가 운영되는 AI 민주정부 구조">
  <defs><marker id="arrow-ai-govt" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <rect class="itpe-svg-node" x="120" y="25" width="520" height="86" rx="14" />
  <text class="itpe-svg-title" x="380" y="58" text-anchor="middle">대국민 AI 서비스</text>
  <text class="itpe-svg-sub" x="380" y="87" text-anchor="middle">맞춤 안내 · 민원 지원 · 안전정보 · 정책참여</text>
  <path class="itpe-svg-link" d="M380 111 V158" marker-end="url(#arrow-ai-govt)" />
  <rect class="itpe-svg-node is-current" x="120" y="166" width="520" height="86" rx="14" />
  <text class="itpe-svg-title" x="380" y="199" text-anchor="middle">공무원 온AI 업무지원</text>
  <text class="itpe-svg-sub" x="380" y="228" text-anchor="middle">법령 검토 · 검색 · 보고서 초안 · 업무자동화</text>
  <path class="itpe-svg-link" d="M380 252 V299" marker-end="url(#arrow-ai-govt)" />
  <rect class="itpe-svg-node" x="120" y="307" width="520" height="86" rx="14" />
  <text class="itpe-svg-title" x="380" y="340" text-anchor="middle">범정부 AI 공통기반</text>
  <text class="itpe-svg-sub" x="380" y="369" text-anchor="middle">모델 · RAG · 데이터 · 보안 · 평가 · 관제</text>
  <path class="itpe-svg-link" d="M380 393 V440" marker-end="url(#arrow-ai-govt)" />
  <rect class="itpe-svg-node" x="120" y="448" width="520" height="102" rx="14" />
  <text class="itpe-svg-title" x="380" y="482" text-anchor="middle">공공 책임 통제</text>
  <text class="itpe-svg-sub" x="380" y="510" text-anchor="middle">법적 근거 · Human Oversight · 이의제기</text>
  <text class="itpe-svg-sub" x="380" y="536" text-anchor="middle">개인정보 보호 · 기록 · 감사</text>
</svg>
</div>

<details>
<summary>핵심 용어</summary>

- **온AI**: 공무원의 법령 검토·문서 작성·협업 등을 AI로 지원하는 지능형 업무관리 플랫폼
- **RAG(Retrieval-Augmented Generation)**: 검색한 근거정보를 생성모델 입력에 결합하는 방식
- **Human Oversight**: AI 결과를 사람이 검토·승인·중단할 수 있도록 한 통제
- **Contestability**: AI가 영향을 준 결정에 대해 설명을 요구하고 이의를 제기할 수 있는 성질
- **DPG(Digital Platform Government)**: 데이터와 서비스를 연계해 국민 중심 서비스를 제공하는 디지털플랫폼정부

</details>

## 예상문제

> AI 민주정부의 개념과 구성체계를 설명하고, 공공부문 AI 서비스의 추진절차 및 문제점·대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 국민서비스와 행정업무를 AI로 혁신하는 정부 모델

> AI 민주정부는 자동처분 정부가 아니라, 공공서비스의 접근성과 행정 생산성을 높이면서 민주적 책임을 유지하는 정부 모델임.

- 정의: AI를 활용하여 국민서비스·정책참여·공무원 업무를 개선하고 공공 의사결정의 책임성과 투명성을 강화하는 정부 운영모델
- 목적: **선제 안내·행정 생산성·정책 대응성·국민 신뢰** 향상

## Ⅱ. AI 민주정부 구성체계

| 계층 | 핵심 기능 | 책임 통제 |
|---|---|---|
| 대국민 | 맞춤 안내·민원·안전·참여 | 고지·접근성·이의제기 |
| 공무원 | 검색·법령검토·초안·업무지원 | 사용자 확인·최종책임 |
| 공통기반 | 모델·RAG·데이터·API·관제 | 평가·권한·기록·보안 |
| 거버넌스 | 정책·위험등급·조달·감사 | 책임자·승인·사고대응 |

## Ⅲ. 공공 AI 서비스 추진절차

> 서비스 편의보다 법적 근거와 국민 권리에 미치는 영향을 먼저 확인해야 함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="공공 AI 서비스의 과제 발굴부터 운영 개선까지 추진절차">
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>① 과제 발굴</strong><strong>활동</strong><span>국민 불편·업무 병목·이해관계자 식별</span><strong>산출</strong><span>Use Case · 서비스 목표</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>② 영향·적법성 평가</strong><strong>활동</strong><span>법적 근거·개인정보·권리·오류영향 검토</span><strong>산출</strong><span>영향평가 · 위험등급</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>③ 설계·개발</strong><strong>활동</strong><span>데이터·RAG·모델·인적감독·이의제기 설계</span><strong>산출</strong><span>서비스 설계 · 통제계획</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>④ 검증·도입</strong><strong>활동</strong><span>정확성·공정성·보안·사용성·접근성 평가</span><strong>산출</strong><span>평가결과 · 승인기록</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><div class="itpe-step-detail"><strong>⑤ 운영·개선</strong><strong>활동</strong><span>오류·민원·이의제기·사고·변경 감시</span><strong>산출</strong><span>운영로그 · 개선조치</span></div></div>
</div>

## Ⅳ. 전자정부·DPG·AI 민주정부 비교

| 기준 | 전자정부 | DPG | AI 민주정부 |
|---|---|---|---|
| 초점 | 업무·민원 전산화 | 데이터·서비스 연계 | AI 기반 서비스·업무 혁신 |
| 제공방식 | 온라인 신청 | 통합·맞춤 서비스 | 선제 안내·지능형 지원 |
| 기반 | 정보시스템·포털 | API·Cloud·데이터 | AI 공통기반·RAG·Agent |
| 핵심통제 | 보안·개인정보 | 데이터 책임·상호운용 | 영향평가·인적감독·이의제기 |

## Ⅴ. 문제점·대응책

| 위험 | 대책 | 효과 |
|---|---|---|
| 부정확한 안내·초안 | 근거검색·출처표시·사용자 확인 | 오사용 감소 |
| 편향·서비스 배제 | 영향평가·대표성 검토·대체채널 | 접근권 보호 |
| 자동결정 책임 불명확 | Human Oversight·승인기록 | 책임소재 확보 |
| 개인정보 과다결합 | 목적제한·최소처리·접근통제 | 침해위험 완화 |
| 기관별 중복구축 | 범정부 공통기반 우선 검토 | 비용·파편화 감소 |

## Ⅵ. 설명·이의제기 가능한 행정 Quality Gate

`[핵심 통찰]` 공공 AI의 품질은 답변 정확도만으로 결정되지 않으며, 국민이 AI 사용 사실과 근거를 알고 오류를 정정하거나 이의를 제기할 수 있어야 완성됨.

`나라면` 권리·의무에 영향을 주는 서비스에는 AI 역할·근거·담당자를 표시하고, 인간 재검토와 대체 절차가 확인되어야 운영을 승인하는 Quality Gate를 적용하겠음.

<div class="itpe-svg-map">
<svg viewBox="0 0 760 470" role="img" aria-label="AI 추천과 인간 검토 및 국민 이의제기를 연결한 공공 AI 책임 구조">
  <defs><marker id="arrow-ai-public" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" /></marker></defs>
  <rect class="itpe-svg-node" x="190" y="25" width="380" height="72" rx="14" />
  <text class="itpe-svg-title" x="380" y="57" text-anchor="middle">AI 분석·추천</text>
  <text class="itpe-svg-sub" x="380" y="82" text-anchor="middle">근거 · 한계 · 불확실성 표시</text>
  <path class="itpe-svg-link" d="M380 97 V145" marker-end="url(#arrow-ai-public)" />
  <rect class="itpe-svg-node is-current" x="190" y="153" width="380" height="72" rx="14" />
  <text class="itpe-svg-title" x="380" y="185" text-anchor="middle">공무원 검토·결정</text>
  <text class="itpe-svg-sub" x="380" y="210" text-anchor="middle">법적 근거 확인 · 승인기록</text>
  <path class="itpe-svg-link" d="M380 225 V273" marker-end="url(#arrow-ai-public)" />
  <rect class="itpe-svg-node" x="190" y="281" width="380" height="72" rx="14" />
  <text class="itpe-svg-title" x="380" y="313" text-anchor="middle">통지·서비스 제공</text>
  <text class="itpe-svg-sub" x="380" y="338" text-anchor="middle">AI 사용 · 근거 · 담당자 안내</text>
  <path class="itpe-svg-link" d="M380 353 V401" marker-end="url(#arrow-ai-public)" />
  <rect class="itpe-svg-node" x="190" y="409" width="380" height="48" rx="14" />
  <text class="itpe-svg-title" x="380" y="440" text-anchor="middle">정정·이의제기·인간 재검토</text>
</svg>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: AI로 국민서비스·정책참여·공무원 업무를 개선하고 공공 의사결정의 책임성과 투명성을 강화하는 정부 운영모델
- 목적: **선제 안내·행정 생산성·정책 대응성·국민 신뢰** 향상

### 2. 구성

| 영역 | 핵심 |
|---|---|
| 대국민 | 맞춤 안내·민원·안전·참여 |
| 공무원 | 검색·법령검토·초안·업무지원 |
| 공통기반 | 모델·RAG·데이터·보안·평가 |
| 책임통제 | 영향평가·인적감독·이의제기 |

### 3. 핵심 통제

- **Grounded Assistance**: 근거검색·출처표시·사용자 확인
- **Contestability**: 통지·정정·이의제기·인간 재검토

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [행정안전부, AI 민주정부 실현 본격 추진](https://mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=128980)
- [NIA, 공공부문 AI 도입·활용 가이드](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=29526&cbIdx=37989)
- [행정안전부, 온AI 모바일 서비스](https://www.mois.go.kr/video/bbs/type019/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000255&nttId=125757)

## 학습 체크

- [ ] Ⅰ: AI 민주정부의 정의·목적을 설명할 수 있는가?
- [ ] Ⅱ: 대국민·공무원·공통기반·거버넌스 계층을 구분할 수 있는가?
- [ ] Ⅲ: 과제 발굴부터 운영까지 활동과 산출물을 연결할 수 있는가?
- [ ] Ⅳ: 전자정부·DPG·AI 민주정부를 비교할 수 있는가?
- [ ] Ⅴ: 정확성·편향·책임·개인정보 위험의 대응책을 제시할 수 있는가?
- [ ] Ⅵ: 설명·이의제기 가능한 Quality Gate를 제언할 수 있는가?

## 연결 토픽

- 이전 토픽: [AI 고속도로](./051_ai_highway.md)
- 연관 토픽: [범정부 AI 공통기반](./025_pan_government_ai_common_infrastructure.md), [공공 클라우드 전환](./021_public_cloud_native_transition.md)
- 다음 토픽: [AI 프라이버시 위험관리 모델](./054_ai_privacy_risk_management_model.md)
