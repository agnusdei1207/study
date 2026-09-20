---
title: "범정부 AI 공통기반"
author: "Codex"
date: "2026-09-21T13:25:00+09:00"
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

- 본질: AI 모델·GPU 등 AI 자원을 범부처가 공동 활용하는 공공 AI 도입·활용 체계
- 메커니즘: 업무기획 → 공통자원 선택 → 데이터·서비스 구현 → 검증 → 운영
- 통제: 기관별 데이터 격리 · 근거 확인 · 사람의 최종 책임 · 이용기록

<div class="itpe-flow-map" role="img" aria-label="행정 수요에서 범정부 AI 공통기반 및 지능형 행정서비스로 이어지는 흐름">
  <div class="itpe-flow-node">
    <strong>행정기관 서비스 수요</strong>
    <small>민원 챗봇 · 행정문서 요약 · 복지 혜택 추천</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>범정부 AI 공통기반 플랫폼</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>공통자원</strong><span>AI 모델 · GPU · API</span></div>
      <div class="itpe-flow-branch"><strong>서비스구현</strong><span>RAG · Workflow · 기관 지식</span></div>
      <div class="itpe-flow-branch"><strong>안전통제</strong><span>권한 · 데이터 격리 · Guardrail · Log</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>파운데이션 모델 및 인프라</strong>
    <small>공동 활용 AI 모델 · GPU 등 연산자원</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>신뢰받는 공공 서비스</strong>
    <small>중복투자 완화 · 신속한 도입 · 행정 책임성 확보</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **LLM(Large Language Model)**: 대규모 텍스트 데이터를 사전 학습하여 언어 생성 및 추론 능력을 제공하는 거대 모델
- **sLLM(Small Large Language Model)**: 특정 공공 도메인에 파인튜닝되어 경량화·저비용으로 운영 가능한 소형 언어모델
- **RAG(Retrieval-Augmented Generation)**: 외부 공공 행정 지식베이스를 실시간 검색하여 근거 기반으로 답변을 생성하는 기법
- **Model Gateway**: 다중 모델에 대한 단일 진입점으로 라우팅, 부하분산, 캐싱, 장애 대체(Fallback)를 수행
- **Guardrail(가드레일)**: 입력·출력·도구사용이 정해진 정책을 벗어나지 않도록 검사·제어하는 안전장치
- **API(Application Programming Interface)**: 개별 공공시스템이 공통 플랫폼의 AI 기능을 손쉽게 호출하는 표준 연계 규격
- **Human-in-the-loop**: 고영향 행정 처분 시 AI 추천 결과를 공무원이 최종 검토·승인하도록 강제하는 통제 체계
- **TCO(Total Cost of Ownership)**: 정보시스템 도입부터 운영·유지보수·폐기까지 수명주기 전반에 걸친 총 소유비용
- **RACI**: 업무 수행 시 Responsible(실무자), Accountable(최종책임자), Consulted(자문자), Informed(통보대상자)를 명확히 지정하는 책임 매트릭스

</details>

## 예상문제

> 범정부 AI 공통기반의 개념과 활용 절차를 설명하고, 데이터 보호·결과 검증·행정 책임 관점의 문제점과 대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 공공 AX 촉진과 중복투자 방지를 위한 범정부 AI 공통기반의 개요

> 개별 기관의 자체 LLM 구축에 따른 예산 낭비를 차단하며, 성패는 단순 API 제공이 아닌 **공공 RAG 정확도**와 **행정 데이터 격리**로 판정함.

- 정의: 행정·공공기관이 AI 모델·GPU 등 AI 자원을 공동 활용하도록 지원하는 도입·활용 체계
- 목적: 중복투자 완화 · 도입기간 단축 · 안전한 공공 활용

## Ⅱ. 범정부 AI 공통기반의 대표 활용 흐름

> 다음은 공공부문 AI 도입·활용 가이드를 답안용으로 압축한 대표 흐름임.

<div class="itpe-pipeline is-vertical" role="img" aria-label="범정부 AI 공통기반 온보딩 5단계 방법론의 활동 및 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 대상 업무 선정</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>행정 수요 발굴 · 생성형 AI 적합성 및 ROI 분석</span>
      <strong>산출</strong><span>업무 적용 타당성 평가서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 데이터 정제 및 등급화</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>공공문서 수집 · 개인정보 비식별화 및 벡터화</span>
      <strong>산출</strong><span>공공 지식 데이터셋 · 보안 등급표</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 파이프라인 연계 및 설정</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>공통 API 연동 · 프롬프트 엔지니어링 및 Guardrail 설정</span>
      <strong>산출</strong><span>서비스 연계 설정서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 실증 평가 및 보안 승인</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>환각 발생률 · 편향성 시험 및 보안성 검토 승인</span>
      <strong>산출</strong><span>신뢰성 평가 보고서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 운영 모니터링 및 감사</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>모델 드리프트 감시 · 토큰 FinOps 및 감사로그 추적</span>
      <strong>산출</strong><span>월간 운영 및 비용 분석서</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · 행정 수요 ↔ 공통 API 연동 ↔ RAG 근거 검증 ↔ 감사로그 추적 양방향 연계</div>

## Ⅲ. 답안용 참조 아키텍처

> 실제 구성은 제공서비스에 따라 달라지며, 답안에서는 서비스·AI 기능·자원·거버넌스로 구분함.

| 계층 | 구성 | 통제 |
|---|---|---|
| **서비스** | 행정업무·대민서비스 | 이용자 확인 · 사람의 검토 |
| **AI 기능** | 모델 호출 · RAG · Workflow | 출처·품질 검증 |
| **공통자원** | AI 모델 · GPU · API | 기관·데이터 격리 |
| **거버넌스** | Guardrail · 권한 · Log | 보안·감사·책임 |

## Ⅳ. 개별 기관 독자 구축 vs 범정부 AI 공통기반 활용 비교

> 공통자원 재사용의 효율과 기관별 최적화·책임 요구를 함께 비교해야 함.

| 기준 | 개별 구축 | 공통기반 활용 |
|---|---|---|
| **자원** | 기관별 조달·운영 | 모델·GPU 공동 활용 |
| **도입** | 기관별 기반 구축 | 공통기능 재사용 |
| **통제** | 기관 책임에 집중 | 플랫폼·이용기관 책임 분담 |
| **유연성** | 업무별 최적화 용이 | 공통규격 제약 가능 |

## Ⅴ. 공공 AI 실무 위험 및 거버넌스 통제 방안

> 공공 행정 특유의 법적·윤리적 부작용을 통제하기 위해 공학적 안전망과 관리적 책임을 결합해야 함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **근거 없는 응답** | RAG·출처 표시 · 기준 미달 응답 제한 · 사람 검토 | 오류 영향 축소 |
| **개인정보 유출** | 입력 단계에서 정규식 및 NER 기반 자동 마스킹, DLP 연동 | 법령 위반 차단 및 개인정보 침해 원천 차단 |
| **프롬프트 인젝션** | 이중 **Guardrail** 배치 및 시스템 프롬프트 변조 방지 | 비인가 행정 데이터 접근 및 오남용 방지 |
| **책임 소재 모호** | 플랫폼·이용기관의 역할과 최종 결정권 명시 | 책임 추적성 확보 |

## Ⅵ. Human-in-the-loop 중심의 기술사적 제언

> 공통기반은 기술적 수단일 뿐이며, 행정 처분의 법적 책임은 해당 기관에 귀속되므로 **공무원 최종 검인**과 **RACI 매트릭스** 정립이 필수적임.

`[핵심 통찰]` 공통기반은 모델의 답을 보증하지 않으며, 공동 자원을 쓰더라도 행정 결과의 적법성·정확성 책임은 이용기관의 업무절차에 남음.

`나라면` 공통기반이 기술 통제를 제공하고 이용기관이 지식·품질·최종결정을 책임하도록 RACI를 정한 뒤, 고위험 업무는 사람의 승인 없이는 실행되지 않게 하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="범정부 AI 공통기반 거버넌스 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>기관별 독자 구축 예산 낭비 · 환각 및 개인정보 유출 위험 잔존</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>범정부 AI 공통기반 연계 · 공공 RAG 표준화 및 Guardrail 내재화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>출처 확인 · 개인정보 차단 · 최종 승인 기록</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>중복투자 완화 · 행정 책임성 확보</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 행정·공공기관이 AI 모델·GPU 등 AI 자원을 공동 활용하도록 지원하는 도입·활용 체계
- 목적: 중복투자 완화 · 도입기간 단축 · 안전한 공공 활용

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="1교시 10점용 범정부 AI 공통기반 아키텍처 요약">
  <div class="itpe-pipeline-node">
    <strong>서비스 인터페이스</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>민원 챗봇 · 행정비서 UI</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>오케스트레이션 / RAG</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>공공문서 벡터검색 · 근거 기반 답변 합성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Model Gateway</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>최적 모델 라우팅 · Fallback · 토큰 캐싱</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>파운데이션 인프라</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>상용 LLM · 공공 sLLM · NPU 클러스터</span></div>
  </div>
</div>

### 3. 핵심 통제

- **RAG(Retrieval-Augmented Generation)**: 공공 행정 문서 기반 지식 검색 결합을 통한 환각 방지
- **Guardrail**: 유해 프롬프트, 개인정보(PII) 유출, 적대적 공격 실시간 필터링
- **Human-in-the-loop**: 고영향 행정 처분 시 최종 판단권자의 확인을 강제하는 책임성 보장

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- [NIA: 공공부문 AI 도입·활용 가이드](https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=29526&cbIdx=37989)
- [행정안전부: 범정부 AI 공통기반 서비스 개시](https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=121943)
- [행정안전부: AI 법령 비서 시범 개시](https://www.mois.go.kr/frt/bbs/type010/commonSelectBoardArticle.do?bbsId=BBSMSTR_000000000008&nttId=127770)

## 학습 체크

- [ ] 범정부 AI 공통기반의 도입 필요성과 TCO 절감 효과를 설명할 수 있는가?
- [ ] 오케스트레이션, RAG, 모델 게이트웨이, 가드레일의 5계층 아키텍처를 도식화할 수 있는가?
- [ ] 독자 구축 대비 공통기반의 장단점을 5개 이상의 비교축으로 대조할 수 있는가?
- [ ] 환각 방지, 개인정보 보호, RACI 책임 분담을 위한 거버넌스 대책을 서술할 수 있는가?

## 연결 토픽

- 이전 토픽: [국가 AI 전략과 인공지능 행동계획](./024_korea_ai_action_plan.md)
- 연관 토픽: [AI 거버넌스 플랫폼](./050_ai_governance_platform.md), [AI 고속도로](./051_ai_highway.md), [공공부문 클라우드 네이티브 전환](./021_public_cloud_native_transition.md)
- 다음 토픽: [소프트웨어 사업 대가산정](./026_software_cost_estimation.md)
