---
title: "협상계약 제안서 평가"
author: "OpenAI Codex"
date: "2026-09-22T04:00:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "B"
extra:
  model: "GPT-5"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="정보 전략과 관리에서 투자와 조달을 거쳐 협상에 의한 계약 제안서평가 세부기준으로 이어지는 지식 위치">
  <span>정보 전략·관리</span>
  <span>투자·조달</span>
  <strong>협상에 의한 계약 제안서평가 세부기준</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **협상에 의한 계약 제안서평가 세부기준**은 조달청이 물품·용역 제안서를 평가할 때 위원 구성·평가 방법·항목·배점·결과 처리를 적용하는 집행 기준
- 메커니즘: 제안서 접수 → 공통·전문 평가 → 점수 합산 → 평가 결과 통보로 이어지며, 대형 SW 사업은 전문영역을 별도 심층 평가하여 수요기관의 부족한 전문성을 보완
- 산출물: 공통평가 점수 · 전문평가 점수 · 종합 기술능력평가 결과 · 협상대상자 선정 근거

<div class="itpe-pipeline is-vertical" role="img" aria-label="대형 소프트웨어 사업 제안서 전문평가 흐름">
  <div class="itpe-pipeline-node">
    <strong>제안서 접수</strong>
    <div class="itpe-step-detail"><strong>입력</strong><span>제안요청서 · 입찰자 제안서 · 평가항목</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current">
    <strong>평가축 분리</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>공통평가 60%</strong><span>전체 사업 수행 역량</span></div>
      <div class="itpe-flow-branch"><strong>전문평가 40%</strong><span>4개 전문영역의 기술성</span></div>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>기술능력평가 결과</strong>
    <div class="itpe-step-detail"><strong>산출</strong><span>공통평가·전문평가 점수 합산</span></div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **SW(Software)**: 전문평가 대상 사업의 기술적 실체이며, 유지관리 사업은 별도 적용금액을 가짐
- **제안서 평가**: 평가위원이 정해진 평가항목에 따라 제안서의 기술능력을 종합 평가하는 절차
- **공통평가**: 사업 전반의 수행 역량을 평가하는 축 → 전문평가와 합산하여 기술능력평가 결과 산출
- **전문평가**: 전문영역별 위원이 심층 기술성을 평가하는 축 → 대규모·고난도 사업의 평가 전문성 보완

</details>

## 예상문제

> 대규모 중요 소프트웨어 사업 평가의 전문성을 높이고 수요기관의 전문성을 보완해 공정한 경쟁을 유도하기 위하여 '조달청 협상에 의한 계약 제안서평가 세부기준'이 2024년 9월 개정·시행되었다. 이와 관련하여 다음을 설명하시오.
> - 가. 계약 제안서평가 세부기준 개정 주요 내용
> - 나. 대형소프트웨어 사업 전문평가제도

## Ⅰ. 평가 전문성·공정경쟁을 강화한 제안서평가 기준

> 세부기준 개정은 대형 SW 사업에는 전문평가를 더하고 소규모 사업에는 발표 부담을 줄여, 사업 규모·난도에 맞는 평가 통제를 적용한 것이 핵심임.

- 정의: **제안서 평가**의 위원 구성·방법·항목·배점·결과 처리에 필요한 세부사항을 정한 **조달청 집행 기준**
- 목적: 평가 전문성 보완 · 입찰 분쟁 예방 · 기업 부담 경감
- 적용: 개별 입찰은 공고일 기준 **현행 세부기준·제안요청서**를 우선 적용

## Ⅱ. 2024년 9월 개정사항

> 개정은 전문성·수요기관 지원·공정성·입찰비용·적용영역의 다섯 문제를 각각 독립된 제도 장치로 보완함.

- 적용 시점: 아래 내용은 **2024년 9월 개정 당시의 주요 변경사항**이며, 개별 사업에는 공고일 기준 최신 행정규칙을 재확인

| 축 | 개정 내용 | 판정 효과 |
|---|---|---|
| 전문성 | 대형 SW 사업 **전문평가제도** 도입 | 고난도 기술 심층 검증 |
| 기관 지원 | 요청 시 조달청의 **수의계약 제안서 적합성 평가** 대행 | 수요기관 평가역량 보완 |
| 공정경쟁 | 내부 심의로 허위 내용·입찰 영향 판단, 타 업체 비방 시 감점 | 분쟁·비방 억제 |
| 부담 경감 | 온라인평가 제안서 발표 기준금액을 5억 원 이상으로 상향 | 소규모 사업 발표비용 축소 |
| 적용 확대 | 엔지니어링·건설엔지니어링의 협상계약 평가기준 신설 | 기술용역 평가 근거 마련 |

## Ⅲ. 대형소프트웨어 사업 전문평가제도

> 전문평가제도는 모든 항목을 같은 위원이 평가하던 구조를 공통 60%·전문 40%로 분리하여, 전문영역 기술성을 전체 수행 역량과 함께 판정함.

### 1. 적용대상·전문영역

| 구분 | 기준 |
|---|---|
| 적용대상 | 사업금액 40억 원 이상 SW 사업 · 유지관리 사업 100억 원 이상 |
| 전문영역 | **정보기술개발** · **정보보호** · **데이터구축** · **디지털기술** |
| 평가조건 | 심층평가 필요 사업을 관련 분야 전문가가 전담 평가 |

### 2. 평가·합산 구조

<div class="itpe-pipeline is-vertical" role="img" aria-label="대형 소프트웨어 사업 전문평가제도의 적용과 판정 흐름">
  <div class="itpe-pipeline-node">
    <strong>대형 SW 사업 식별</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>적용금액 · 사업유형 · 심층평가 필요성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>평가위원 구성</strong>
    <div class="itpe-step-detail"><strong>공통 역할</strong><span>사업 전반의 수행 역량</span></div>
    <div class="itpe-step-detail"><strong>전문 역할</strong><span>선정 전문영역의 기술성</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current">
    <strong>독립 평가</strong>
    <div class="itpe-step-detail"><strong>평가</strong><span><span class="itpe-keyword"><strong>공통평가 60%</strong></span> · <span class="itpe-keyword"><strong>전문평가 40%</strong></span></span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>기술능력평가 확정</strong>
    <div class="itpe-step-detail"><strong>산출</strong><span>두 평가점수의 가중 합산 결과</span></div>
  </div>
</div>

## Ⅳ. 문제점·대응책

> 제도의 실효성은 전문위원을 추가했다는 사실보다 전문영역 선택, 평가축 분리, 판단 증적이 일관되는지로 판정함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 전문영역과 사업 핵심기술 불일치 | 제안요청서 요구사항과 4개 전문영역 매핑 | 핵심기술 평가 누락 방지 |
| 공통·전문 항목 중복 채점 | 평가항목별 책임·배점 사전 분리 | 특정 역량의 이중 반영 방지 |
| 허위·비방 판단의 자의성 | 증적 확보 · 내부 심의 · 영향도 기록 | 감점 판단의 재현성 확보 |

## Ⅴ. 요구사항 추적 기반 평가설계 결론

> 전문평가의 품질은 위원 수가 아니라 제안요청서 요구사항부터 평가항목·위원 의견·합산 결과까지의 추적 가능성으로 결정됨.

### 학습자 통찰 메모 — 답안 밖

- `[핵심 통찰]`: 전문평가는 공통평가를 대체하지 않는다. 사업 전반의 수행 가능성과 특정 기술의 깊이를 서로 다른 축으로 평가한 뒤 합산하는 보완 구조다.
- `나라면`: 제안요청서 확정 때 요구사항별 공통·전문 평가 책임을 먼저 배정하고, 평가 후에는 위원 의견이 해당 요구사항과 연결되는지 점검하겠다.

### 실전 답안용 기술사적 제언

- 판정: 전문영역·평가항목·위원 의견 사이의 추적 가능성
- 대안: **RFP(Request for Proposal)** 요구사항별 공통·전문 평가 책임 매핑
- 검증: 중복 평가 · 미평가 요구사항 · 근거 없는 감점 여부 확인
- 효과: 심층평가의 일관성 · 이의제기 대응력 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="요구사항 추적 기반 제안서 평가 개선 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>공통·전문 항목 중복 또는 핵심기술 누락</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node is-current">
    <strong>평가 책임 매핑</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>RFP 요구사항 ↔ 평가항목 ↔ 담당 평가축 연결</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>평가 증적 점검</strong>
    <div class="itpe-step-detail"><strong>검증</strong><span>위원 의견 · 점수 · 요구사항의 연결 확인</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>평가 결과 확정</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>중복·누락 억제 · 판단 근거 보존</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **협상에 의한 계약 제안서평가 세부기준**은 조달청이 물품·용역 제안서의 위원 구성·평가 방법·항목·배점·결과 처리를 일관되게 집행하는 기준
- 목적: 평가 전문성 보완 · 공정경쟁 · 입찰 부담 경감

### 2. 2024년 개정 핵심

| 구분 | 내용 |
|---|---|
| 전문성 | 대형 SW 사업 **전문평가제도** 도입 |
| 공정성 | 허위 판단절차 명확화 · 타사 비방 감점 |
| 지원 | 수의계약 적합성 평가 대행 |
| 부담 | 발표 기준금액 5억 원 이상으로 상향 |
| 범위 | 기술용역 협상계약 평가기준 신설 |

## 출제 이력과 검증 출처

- 제136회 정보관리기술사 2교시 3번: 위 `예상문제`에 공식 원문 수록
- [조달청, 「조달청 협상계약 평가… 기업 부담 낮추고 공정성 높인다」, 2024. 9. 11.](https://www.pps.go.kr/kor/bbs/view.do?bbsSn=2409110017&key=00318)
- [조달청, 「협상에 의한 계약 제안서평가 세부기준 주요 개정사항」, 2024. 9. 19.](https://www.pps.go.kr/kor/bbs/view.do?bbsSn=2409190019&key=00638)
- [국가법령정보센터, 「조달청 협상에 의한 계약 제안서평가 세부기준」 2024년 9월 시행 연혁](https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000247024)
- [국가법령정보센터, 현행 「조달청 협상에 의한 계약 제안서평가 세부기준」](https://law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000273638)

## 학습 체크

- [ ] Ⅰ 개요: 세부기준의 정의와 목적 세 가지를 재현할 수 있는가?
- [ ] Ⅱ 개정 내용: 전문성·기관 지원·공정경쟁·부담 경감·적용 확대의 다섯 축을 개정 장치와 연결할 수 있는가?
- [ ] Ⅲ 전문평가: 적용금액 두 기준, 전문영역 네 가지, 공통 60%·전문 40% 합산 구조를 그릴 수 있는가?
- [ ] Ⅳ 위험·통제: 전문영역 불일치·중복 채점·자의적 판단의 대책과 효과를 1:1로 연결할 수 있는가?
- [ ] Ⅴ 제언: RFP 요구사항 ↔ 평가항목 ↔ 담당 평가축의 추적 경로와 검증 항목을 설명할 수 있는가?

## 연결 토픽

- 선행 토픽: [공공 SW 사업 발주·계약](./039_public_sw_contract.md) · [제안요청서(RFP)](./049_rfp.md)
- 연관 토픽: [PMO(PMC 비교 포함)](./004_pmo.md) · [소프트웨어 사업 대가산정](./026_software_cost_estimation.md)
