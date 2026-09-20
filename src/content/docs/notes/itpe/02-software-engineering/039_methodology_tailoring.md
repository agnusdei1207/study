---
title: "개발방법론 테일러링"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 개발 방법론을 거쳐 개발방법론 테일러링으로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>개발 방법론</span>
  <strong>개발방법론 테일러링</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **개발방법론 테일러링(Methodology Tailoring)**은 표준 소프트웨어 개발방법론을 특정 프로젝트의 규모, 성격, 기술 환경, 발주자 요구에 맞게 활동, 절차, 산출물을 가감·조정하는 최적화 활동
- 메커니즘: 프로젝트 특성 분석 → 베이스라인 방법론 선정 → 테일러링 기준 수립 → 절차/산출물 가감 조정 → **테일러링 승인 및 형상화**
- 산출/효과: 불필요한 형식적 문서 작업 제거 · 프로젝트 적합도 향상 · 개발 생산성 극대화 · 예산/일정 낭비 방지

<div class="itpe-flow-map" role="img" aria-label="개발방법론 테일러링 프로세스">
  <div class="itpe-flow-node"><strong>조직 표준 방법론</strong><small>폭포수, 애자일, CBD 등</small></div>
  <div class="itpe-flow-arrow">→ 프로젝트 환경 분석 →</div>
  <div class="itpe-flow-node is-current">
    <strong>테일러링 매트릭스</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>내부 기준</strong><span>규모, 기간, 기술 난이도, 팀 역량</span></div>
      <div class="itpe-flow-branch"><strong>외부 기준</strong><span><span class="itpe-keyword"><strong>법제도, 규제, 발주자 요구</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>가감 조정</strong><span><span class="itpe-keyword"><strong>단계/활동/산출물 통합 및 생략</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 이해관계자 공식 승인 →</div>
  <div class="itpe-flow-node"><strong>프로젝트 맞춤형 방법론</strong><small>사업수행계획서 반영</small></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Methodology Tailoring(방법론 테일러링)**: 범용적인 표준 개발방법론을 특정 프로젝트의 현실적 제약과 특성에 맞도록 수정·보완하는 공학적 프로세스
- **Internal Factors(내부적 요건)**: 프로젝트 규모, 사업 기간, 기술 성숙도, 참여 인력의 도메인 지식, 개발 환경
- **External Factors(외부적 요건)**: 관련 법령, 산업 표준 규제, 보안 등급, 발주기관의 산출물 지침
- **Tailoring Matrix(테일러링 매트릭스)**: 프로젝트 특성별로 필수, 선택, 생략할 산출물과 활동을 명시한 기준표
- **Golden Rule of Tailoring**: 아무리 테일러링을 하더라도 소프트웨어의 핵심 품질 보증 및 추적성(Traceability)은 결코 생략할 수 없다는 원칙

</details>

## 예상문제

> 소프트웨어 개발 프로젝트에서 개발방법론 테일러링(Tailoring)의 개념과 필요성을 설명하고, 테일러링 시 고려해야 할 내부적/외부적 기준 요소, 표준 5단계 테일러링 절차 및 과도한 테일러링(Under/Over-tailoring) 방지를 위한 통제 방안을 제시하시오. (25점)

## Ⅰ. 프로젝트 성공을 위한 맞춤형 최적화, 개발방법론 테일러링의 개요

> 모든 신발이 모든 발에 맞을 수 없듯이, 모든 프로젝트에 일률적으로 적용되는 단 하나의 완벽한 방법론은 존재하지 않는다.

- 정의: 조직의 공통 표준 소프트웨어 프로세스를 개별 프로젝트의 특성(규모, 위험도, 기술, 납기)에 맞게 **단계, 활동, 태스크, 산출물을 선별적으로 조정·최적화**하는 활동
- 목적: 프로젝트 오버헤드(불필요한 형식적 문서) 제거, 자원의 효율적 집중, 프로젝트 위험 사전 완화, 납기 준수율 향상

## Ⅱ. 테일러링 시 고려해야 할 내부적 및 외부적 기준

> 테일러링은 직관이나 편의에 의해 결정되는 것이 아니며, 객관적 다차원 기준표에 의해 평가되어야 한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="테일러링 고려 기준">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>내부적 요건 (Internal Factors) — 프로젝트 내부 특성</strong></span>
    <small>1. 사업 규모 및 복잡도 (소규모/중규모/대규모 FP)<br />2. 일정 및 예산 제약 (단기 집중 vs 장기 단계적)<br />3. 기술 난이도 및 신기술 적용 여부 (검증된 기술 vs AI/클라우드)<br />4. 개발팀 성숙도 및 도메인 지식 수준</small>
  </div>
  <div class="itpe-pipeline-arrow">↕ 상호 작용</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>외부적 요건 (External Factors) — 외부 환경 및 규제</strong></span>
    <small>1. 법적/제도적 규제 (전자정부법, 공공 SW사업 가이드, 개인정보보호법)<br />2. 기능안전 및 표준 인증 (ISO 26262, CMMI, GS인증 요건)<br />3. 발주기관 및 고객의 감리/품질 요구조건<br />4. 타 시스템과의 연계 복잡성 및 보안 감사 등급</small>
  </div>
</div>

## Ⅲ. 개발방법론 테일러링 5단계 표준 절차

> 테일러링 결과는 반드시 공식적인 사업수행계획서에 반영되어 발주자와 감리원의 승인을 득해야 한다.

<div class="itpe-pipeline is-vertical" role="img" aria-label="테일러링 5단계 수행 절차">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. 프로젝트 특성 정의 (Project Characterization)</strong></span>
    <small>규모, 일정, 기술, 인력, 규제 등 내/외부 영향 요소를 객관적으로 파악</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. 기본 표준 방법론 선정 (Base Methodology Selection)</strong></span>
    <small>조직 자산 중 가장 적합한 모델(폭포수, 애자일, 하이브리드 등)을 기본 틀로 선정</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. 테일러링 가감 조정 (Tailoring Customization)</strong></span>
    <small>테일러링 매트릭스를 기반으로 WBS 활동 및 산출물의 통합, 분할, 생략 수행</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>4. 테일러링 결과 문서화 및 검토 (Documentation &amp; Review)</strong></span>
    <small>가감 사유와 대체 방안을 '방법론 테일러링 계획서'로 명시하고 품질팀 검토</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>5. 공식 승인 및 베이스라인 확정 (Approval &amp; Baseling)</strong></span>
    <small>발주자, PMO, 감리원의 공식 승인을 획득하여 사업수행계획서 베이스라인 등록</small>
  </div>
</div>

## Ⅳ. 테일러링 오류 유형과 실무 방어 대책

> 테일러링이 지나치면 품질이 붕괴되고, 너무 소극적이면 문서 작업에 치여 개발이 마비된다.

| 오류 유형 | 발생 현상 | 초래되는 위험 | 실무 방어 대책 |
|---|---|---|---|
| **언더 테일러링 (Under-tailoring)** | 개발자의 귀찮음을 이유로 필수 산출물 대폭 생략 | **품질 보증 실패**, 유지보수 불가, 감리 지적 | **최소 필수 산출물 기준선(Do Not Tailor List)** 강제 |
| **오버 테일러링 (Over-tailoring)** | 표준의 모든 문서와 절차를 형식적으로 전수 강요 | 개발 생산성 급락, 페이퍼 워크로 일정 지연 | 프로젝트 규모별(소/중/대) 표준 **간이 템플릿** 사전 제공 |
| **비인가 테일러링 (Unauthorized)** | 발주자 승인 없이 개발팀 독단으로 산출물 누락 | 검수 분쟁, 계약 불이행, 과업 변경 시 책임 소지 | **형상관리 CCB 및 변경 승인 절차**와 직결 |

## Ⅴ. 애자일-하이브리드 시대의 테일러링을 위한 기술사적 제언

> 공공 SW 및 엔터프라이즈 환경에서는 폭포수의 '거버넌스'와 애자일의 '실행력'을 결합한 하이브리드 테일러링이 대세이다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 테일러링의 가장 큰 함정은 "바쁘니까 설계서와 테스트 결과서는 나중에 한꺼번에 쓰겠다"는 식의 생략임. 이는 테일러링이 아니라 태만임. 아무리 초경량 프로젝트라도 '요구사항 추적표(RTM)'와 '인수 테스트 결과서'는 결코 생략할 수 없는 절대 기준선임. 문서의 분량을 줄일지언정 추적성 자체를 잘라내서는 안 됨.
- 나라면: 착수 단계(착수보고회)에서 발주자 및 수탁 감리법인과 함께 '산출물 테일러링 협의체'를 가동하여, 20종의 표준 산출물 중 8종으로 통합 압축하고, 대신 프로토타입 시연과 CI/CD 자동화 보고서로 품질 증적을 대체하도록 서면 합의하겠음.

### 실전 답안용 기술사적 제언

- 판정: 프로젝트 특성 기반의 객관적 테일러링 기준 수립 및 공식 승인 판정
- 대안: **공공 발주 거버넌스(폭포수 단계) + 스프린트 개발(애자일)** 하이브리드 테일러링
- 검증: 생략 산출물에 대한 대체 검증 수단 확보 · RTM 추적성 100% 유지
- 효과: 행정 공수 40% 절감 · 본질적 코딩 및 테스트 집중을 통한 프로젝트 성공률 제고

<div class="itpe-pipeline is-vertical" role="img" aria-label="방법론 테일러링 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>획일적 산출물 강요로 인한 페이퍼워크 낭비 또는 무단 생략으로 인한 품질 붕괴</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>내/외부 기준 매트릭스에 기반한 정량적 테일러링 및 대체 증적(CI) 인정</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>발주자·감리원 서면 승인 및 요구사항-설계-시험 간 추적성 100%</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>프로젝트 납기 준수율 극대화 · 실질적 품질 보증 중심의 사업 수행 달성</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **개발방법론 테일러링**은 조직의 표준 소프트웨어 프로세스를 개별 프로젝트의 특성에 맞게 활동과 산출물을 가감 조정하는 활동
- 목적: 형식적 문서 낭비를 제거하고 프로젝트 납기 및 품질 최적화 달성

### 2. 테일러링 2대 고려 기준

<div class="itpe-pipeline is-vertical" role="img" aria-label="테일러링 2대 기준 요약">
  <div class="itpe-pipeline-node"><strong>내부적 기준</strong><small>사업 규모, 기간, 기술 난이도, 팀 역량</small></div>
  <div class="itpe-pipeline-arrow">↕ 상호 조율</div>
  <div class="itpe-pipeline-node"><strong>외부적 기준</strong><small>법제도, 규제, 기능안전 표준, 발주자 요구</small></div>
</div>

### 3. 핵심 통제

- **Do Not Tailor**: 요구사항 추적성(RTM) 및 핵심 테스트 산출물 생략 절대 불가
- **공식 승인**: 사업수행계획서에 테일러링 사유를 명시하고 발주자/감리 승인 획득

## 출제 이력과 검증 출처

- 제138회 정보관리기술사 1교시: 소프트웨어 개발방법론 테일러링의 개념 및 고려사항
- ISO/IEC/IEEE 12207 Systems and software engineering - Software life cycle processes
- 한국지능정보사회진흥원(NIA), 정보시스템 구축·운영 지침 및 방법론 테일러링 가이드

## 학습 체크

- [ ] 방법론 테일러링의 정의와 수행 목적을 명확히 설명할 수 있는가?
- [ ] 테일러링 시 고려해야 할 내부적 기준과 외부적 기준을 각각 3가지 이상 제시할 수 있는가?
- [ ] 언더 테일러링과 오버 테일러링의 위험 및 이를 방지하기 위한 통제 방안을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [SOAP](./037_soap.md)
- 연관 토픽: [SW 개발방법론 비교](./139_sw_development_methodologies.md), [형상관리](./011_configuration_management.md)
- 다음 토픽: [요구공학](./040_requirements_engineering.md)
