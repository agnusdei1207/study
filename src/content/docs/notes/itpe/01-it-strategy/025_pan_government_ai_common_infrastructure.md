---
title: "범정부 AI 공통기반"
author: "Codex"
date: "2026-09-20T19:20:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5.6 Sol"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 디지털정책·AI 플랫폼을 거쳐 범정부 AI 공통기반으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 디지털정책·AI 플랫폼</span>
  <strong>범정부 AI 공통기반</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **범정부 AI 공통기반**은 행정·공공기관이 **LLM(Large Language Model)**과 연산 인프라를 개별 중복 구축하지 않고 표준 **API(Application Programming Interface)**로 공동 활용하는 공공 AI 공유 플랫폼
- 메커니즘: 행정 수요 입력 → **Model Gateway** 최적 모델 라우팅 → **RAG(Retrieval-Augmented Generation)** 지식 검색 결합 → **Guardrail** 보안·윤리 필터링 → 행정 서비스 산출
- 산출: 범정부 AI 표준 서비스 모델 · 행정 특화 **sLLM(Small Large Language Model)** · 기관별 안전한 멀티 테넌트 환경

<div class="itpe-flow-map" role="img" aria-label="행정 수요에서 범정부 AI 공통기반 및 지능형 행정서비스로 이어지는 흐름">
  <div class="itpe-flow-node">
    <strong>행정기관 서비스 수요</strong>
    <small>민원 챗봇 · 행정문서 요약 · 복지 혜택 추천</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>범정부 AI 공통기반 플랫폼</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>게이트웨이</strong><span><span class="itpe-keyword"><strong>Model Gateway</strong></span> 기반 부하분산·라우팅</span></div>
      <div class="itpe-flow-branch"><strong>지식 결합</strong><span>공공 행정 데이터 기반 <span class="itpe-keyword"><strong>RAG</strong></span> 검색 증강</span></div>
      <div class="itpe-flow-branch"><strong>안전 통제</strong><span>입출력 <span class="itpe-keyword"><strong>Guardrail</strong></span> 및 PII 마스킹</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>파운데이션 모델 및 인프라</strong>
    <small>상용 LLM · 공공 특화 <span class="itpe-keyword"><strong>sLLM</strong></span> · 국산 NPU 클러스터</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>신뢰받는 공공 서비스</strong>
    <small><span class="itpe-keyword"><strong>TCO</strong></span> 절감 · 환각 차단 · 행정 책임성 확보</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **LLM(Large Language Model)**: 대규모 텍스트 데이터를 사전 학습하여 언어 생성 및 추론 능력을 제공하는 거대 모델
- **sLLM(Small Large Language Model)**: 특정 공공 도메인에 파인튜닝되어 경량화·저비용으로 운영 가능한 소형 언어모델
- **RAG(Retrieval-Augmented Generation)**: 외부 공공 행정 지식베이스를 실시간 검색하여 근거 기반으로 답변을 생성하는 기법
- **Model Gateway**: 다중 모델에 대한 단일 진입점으로 라우팅, 부하분산, 캐싱, 장애 대체(Fallback)를 수행
- **Guardrail**: 프롬프트 인젝션, 개인정보 유출, 유해 답변을 입출력 단계에서 실시간 탐지·차단하는 보안 장비
- **API(Application Programming Interface)**: 개별 공공시스템이 공통 플랫폼의 AI 기능을 손쉽게 호출하는 표준 연계 규격
- **Human-in-the-loop**: 고영향 행정 처분 시 AI 추천 결과를 공무원이 최종 검토·승인하도록 강제하는 통제 체계
- **TCO(Total Cost of Ownership)**: 정보시스템 도입부터 운영·유지보수·폐기까지 수명주기 전반에 걸친 총 소유비용

</details>

## 예상문제

> 범정부 AI 공통기반의 추진 배경과 계층별 아키텍처를 설명하고, 환각(Hallucination) 억제·개인정보 보호·행정 책임 소재(RACI) 관점의 거버넌스 통제 방안을 논하시오. (25점)

## Ⅰ. 공공 AX 촉진과 중복투자 방지를 위한 범정부 AI 공통기반의 개요

> 개별 기관의 자체 LLM 구축에 따른 예산 낭비를 차단하며, 성패는 단순 API 제공이 아닌 **공공 RAG 정확도**와 **행정 데이터 격리**로 판정함.

- 정의: 행정·공공기관이 독자 구축 없이 표준 **API(Application Programming Interface)**로 고성능 AI 모델과 인프라를 활용하도록 지원하는 **국가 공통 플랫폼**
- 목적: 인프라 중복투자 방지, 공공 예산 절감 및 행정 서비스 신뢰성 확보

## Ⅱ. 범정부 AI 공통기반 5단계 온보딩 및 운영 파이프라인

> `업무선정 → 데이터준비 → 파이프라인구성 → 검증승인 → 운영환류`의 5단계 수명주기를 거쳐 안전하게 공공 서비스로 안착시킴.

<div class="itpe-pipeline is-vertical" role="img" aria-label="범정부 AI 공통기반 온보딩 5단계 방법론의 활동 및 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 대상 업무 선정</strong></span>
    <small>행정 수요 발굴 · 생성형 AI 적합성 및 ROI 분석<br />→ 업무 적용 타당성 평가서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 데이터 정제 및 등급화</strong></span>
    <small>공공문서 수집 · 개인정보 비식별화 및 벡터화<br />→ 공공 지식 데이터셋 · 보안 등급표</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 파이프라인 연계 및 설정</strong></span>
    <small>공통 API 연동 · 프롬프트 엔지니어링 및 Guardrail 설정<br />→ 서비스 연계 설정서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 실증 평가 및 보안 승인</strong></span>
    <small>환각 발생률 · 편향성 시험 및 보안성 검토 승인<br />→ 신뢰성 평가 보고서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 운영 모니터링 및 감사</strong></span>
    <small>모델 드리프트 감시 · 토큰 FinOps 및 감사로그 추적<br />→ 월간 운영 및 비용 분석서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · 행정 수요 ↔ 공통 API 연동 ↔ RAG 근거 검증 ↔ 감사로그 추적 양방향 연계</div>

## Ⅲ. 범정부 AI 공통기반 5계층 아키텍처

> 서비스부터 인프라까지 계층화하고 전 영역에 가드레일과 감사로그를 관통시켜 보안과 성능을 보장함.

| 계층 | 주요 구성요소 | 핵심 역할 및 통제 기준 |
|---|---|---|
| **1. 서비스 계층** | 공공 포털, 모바일 행정 앱, OpenAPI | 기관별 UI/UX 제공 및 **Human-in-the-loop** 검토 화면 |
| **2. 오케스트레이션** | LangChain/LlamaIndex 기반 워크플로우, **RAG** | 행정문서 청킹·임베딩 및 출처 기반 정답 합성 |
| **3. 모델 게이트웨이** | **Model Gateway**, 토큰 라우터, 캐시 | 질의 복잡도별 최적 모델 분기 및 대체 라우팅 |
| **4. 파운데이션 인프라** | 공공 클라우드 클러스터, 상용 LLM, **sLLM** | 국산 NPU 탑재 및 멀티 테넌트 자원 격리 |
| **5. 횡단 거버넌스** | **Guardrail**, 개인정보 마스킹, 불변 감사로그 | 적대적 프롬프트 차단 및 전 질의·응답 증빙 보존 |

## Ⅳ. 개별 기관 독자 구축 vs 범정부 AI 공통기반 활용 비교

> 독자 구축 대비 비용과 구축 기간을 대폭 단축하며, 국가 표준 보안 거버넌스를 즉시 수용할 수 있음.

| 비교 기준 | 개별 기관 독자 구축 | 범정부 AI 공통기반 활용 |
|---|---|---|
| **소요 비용** | 하드웨어·소프트웨어 중복 도입으로 막대한 예산 낭비 | 공통 인프라·라이선스 공동 활용으로 **TCO** 대폭 절감 |
| **도입 기간** | 인프라 조달부터 검증까지 수개월 이상 장기 소요 | 기 구축된 공통 **API**를 통해 즉시 개발 및 서비스 롤아웃 |
| **보안 수준** | 기관별 보안 역량 편차로 데이터 유출 위험 노출 | 국가 표준 보안 가이드라인 및 공통 **Guardrail** 일괄 적용 |
| **벤더 종속** | 특정 상용 솔루션 및 외산 LLM에 Lock-in 발생 | 게이트웨이를 통한 멀티 벤더 및 오픈소스 자유 전환 |
| **데이터 격리** | 자체 전산실 내 격리는 용이하나 유지비 과다 | 멀티 테넌트 VPC 및 암호화 격리로 완벽한 기밀성 보장 |
| **유지보수** | 전문 인력 부족으로 모델 노후화 및 장애 위험 | 중앙 전문기관(NIA 등)의 지속적 플랫폼 업그레이드 수혜 |

## Ⅴ. 공공 AI 실무 위험 및 거버넌스 통제 방안

> 공공 행정 특유의 법적·윤리적 부작용을 통제하기 위해 공학적 안전망과 관리적 책임을 결합해야 함.

| 위험 요인 | 발생 원인 | 공학적·관리적 해결 대책 | 기대 효과 |
|---|---|---|---|
| **행정 오류 (환각)** | 학습 데이터 외 최신 법령 누락 및 모델 추론 한계 | **RAG** 연계 의무화, 출처 문서 링크 표시, 신뢰도 미달 시 응답 거부 | 허위 행정 정보 제공 방지 및 대국민 신뢰 확보 |
| **개인정보 유출** | 프롬프트 입력창을 통한 주민번호 등 민감정보 유출 | 입력 단계에서 정규식 및 NER 기반 자동 마스킹, DLP 연동 | 법령 위반 차단 및 개인정보 침해 원천 차단 |
| **프롬프트 인젝션** | 시스템 탈옥 프롬프트를 통한 보안 지침 무력화 | 이중 **Guardrail** 배치 및 시스템 프롬프트 변조 방지 | 비인가 행정 데이터 접근 및 오남용 방지 |
| **책임 소재 모호** | AI 오답으로 인한 행정 피해 발생 시 책임 공백 | 플랫폼 제공자(기술)와 이용기관(내용) 간 **RACI 매트릭스** 확립 | 명확한 손해배상 및 행정 구제 체계 수립 |

## Ⅵ. Human-in-the-loop 중심의 기술사적 제언

> 공통기반은 기술적 수단일 뿐이며, 행정 처분의 법적 책임은 해당 기관에 귀속되므로 **공무원 최종 검인**과 **RACI 매트릭스** 정립이 필수적임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 범정부 AI 공통기반이 제공하는 거대 모델과 RAG는 행정 효율을 극대화하는 보조 수단에 불과함. 공공 행정에서 AI의 환각은 단순 오류가 아니라 국민의 권익 침해와 직결되므로, 모델 성능보다 '출처 근거 제시(Grounding)'와 '공무원 최종 승인(Human-in-the-loop)' 체계가 거버넌스의 핵심 축이 되어야 함.
- 나라면: 기관 서비스 연계 시 '공공 RAG 출처 문서 100% 매핑'을 API 호출 필수 파라미터로 강제하고, 공무원의 최종 확인 없이 대국민 행정 처분이 자동 발송되지 않도록 워크플로우 게이트를 시스템적으로 하드코딩하겠음.

### 실전 답안용 기술사적 제언

- 판정: 공통 플랫폼의 기술 재사용과 이용 기관의 행정적 책임 분리 확립
- 대안: **공공 RAG** 출처 증명 연계 및 **Human-in-the-loop** 의사결정 게이트 강제
- 검증: 미검증 프롬프트 차단율 100% · 출처 없는 환각 응답률 0% 달성
- 효과: 예산 중복투자 방지 및 대국민 행정 신뢰성 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="범정부 AI 공통기반 거버넌스 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>기관별 독자 구축 예산 낭비 · 환각 및 개인정보 유출 위험 잔존</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>범정부 AI 공통기반 연계 · 공공 RAG 표준화 및 Guardrail 내재화</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>입출력 보안 필터링 통과 · Human-in-the-loop 공무원 검인 완료</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>TCO 대폭 절감 · 신뢰받는 지능형 공공 행정 서비스 실현</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 행정·공공기관이 거대언어모델(**LLM**)과 연산 인프라를 독자 구축 없이 표준 **API(Application Programming Interface)**로 공동 활용하는 클라우드 기반 **국가 공공 AI 공유 플랫폼**
- 목적: 인프라 중복투자 방지, 공공 예산 절감 및 행정 서비스 신뢰성 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="1교시 10점용 범정부 AI 공통기반 아키텍처 요약">
  <div class="itpe-pipeline-node"><strong>서비스 인터페이스</strong><small>민원 챗봇 · 행정비서 UI</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>오케스트레이션 / RAG</strong><small>공공문서 벡터검색 · 근거 기반 답변 합성</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>Model Gateway</strong><small>최적 모델 라우팅 · Fallback · 토큰 캐싱</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>파운데이션 모델/인프라</strong><small>상용 LLM · 공공 sLLM · NPU 클러스터</small></div>
</div>

### 3. 핵심 통제

- **RAG(Retrieval-Augmented Generation)**: 공공 행정 문서 기반 지식 검색 결합을 통한 환각 방지
- **Guardrail**: 유해 프롬프트, 개인정보(PII) 유출, 적대적 공격 실시간 필터링
- **Human-in-the-loop**: 고영향 행정 처분 시 최종 판단권자의 확인을 강제하는 책임성 보장

## 출제 이력과 검증 출처

- 시사·트렌드 집중 토픽 (디지털플랫폼정부 핵심 인프라 구현 과제)
- 제136회 정보관리기술사 2교시: 공공부문 초거대 AI 도입 및 활용 전략
- 제138회 정보관리기술사 1교시: 검색 증강 생성(RAG)의 원리와 공공 데이터 활용
- 행정안전부, [공공부문 초거대 인공지능(AI) 도입·활용 가이드라인](https://www.mois.go.kr)
- 한국지능정보사회진흥원(NIA), [범정부 초거대 AI 공통기반 구현 및 운영 현황](https://www.nia.or.kr)

## 학습 체크

- [ ] 범정부 AI 공통기반의 도입 필요성과 TCO 절감 효과를 설명할 수 있는가?
- [ ] 오케스트레이션, RAG, 모델 게이트웨이, 가드레일의 5계층 아키텍처를 도식화할 수 있는가?
- [ ] 독자 구축 대비 공통기반의 장단점을 5개 이상의 비교축으로 대조할 수 있는가?
- [ ] 환각 방지, 개인정보 보호, RACI 책임 분담을 위한 거버넌스 대책을 서술할 수 있는가?

## 연결 토픽

- 이전 토픽: [국가 AI 전략과 인공지능 행동계획](./024_korea_ai_action_plan.md)
- 연관 토픽: [AI 거버넌스 플랫폼](./050_ai_governance_platform.md), [AI 고속도로](./051_ai_highway.md), [공공부문 클라우드 네이티브 전환](./021_public_cloud_native_transition.md)
- 다음 토픽: [소프트웨어 사업 대가산정](./026_software_cost_estimation.md)
