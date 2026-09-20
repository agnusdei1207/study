---
title: "소프트웨어 비용 산정(Software Cost Estimation)"
author: "Codex"
date: "2026-09-20T19:33:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 공공 SW 사업 제도 및 비용 관리를 거쳐 소프트웨어 비용 산정으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>공공 SW 제도·비용 관리</span>
  <strong>소프트웨어 비용 산정(Software Cost Estimation)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: SW 규모(Size)를 객관적으로 측정하고 통계 알고리즘(**FP/COCOMO/Putnam**)을 적용해 소요 공수(M/M)와 개발 예산을 과학적으로 산출하는 원가 공학
- 메커니즘: 시스템 경계 정의 → 5대 기능 식별(데이터/트랜잭션) → 가중치 적용(UFP) → 보정계수 반영 → **FP(기능점수)** 단가 연계 예산 확정
- 산출: 기능점수 산정 명세서 · COCOMO 모형 분석서 · SW 사업 대가 산출 내역서 · 과업 변경 계약 조정서

<div class="itpe-flow-map" role="img" aria-label="SW 비용 산정 3대 접근 방식과 기능점수 기반 대가 산정 흐름">
  <div class="itpe-flow-node">
    <strong>비용 산정 3대 접근 방식</strong>
    <small>하향식 (전문가/델파이) · 상향식 (LOC/WBS) · 수학적 모형</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>공공 조달 표준 적용</small></div>
  <div class="itpe-flow-node is-current">
    <strong>기능점수 (FP, Function Point) 산정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>데이터</strong><span>내부논리(ILF) · 외부연계(EIF)</span></div>
      <div class="itpe-flow-branch"><strong>트랜잭션</strong><span>외부입력(EI) · 외부출력(EO) · 외부조회(EQ)</span></div>
      <div class="itpe-flow-branch"><strong>보정</strong><span>규모 · 연계 · 성능 · 다중사이트 보정계수</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>법정 대가 고시</small></div>
  <div class="itpe-flow-node">
    <strong>SW 개발비 확정 (제값받기)</strong>
    <small>보정 FP × 고시 단가 + 직접경비 및 이윤 합산</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **FP(Function Point)**: 사용자 관점에서 소프트웨어가 제공하는 논리적 기능 수량을 독립적으로 측정하는 기능점수 표준
- **COCOMO(Constructive Cost Model)**: Barry Boehm이 정립한 모델로, 소스코드 라인 수(KLOC)와 15개 노력조정승수(EAF)를 결합한 회귀 비용 산정식
- **Putnam 모형**: Rayleigh-Norden 곡선을 바탕으로 프로젝트 전 생애주기 동안의 시간과 인력 배분 관계를 산출하는 동적 비용 모델
- **Delphi 기법**: 복수 전문가의 주관적 편향을 제거하기 위해 익명 설문과 피드백을 반복 수렴하여 견적을 도출하는 하향식 기법
- **EAF(Effort Adjustment Factor)**: COCOMO 모형에서 시스템의 신뢰도, 데이터베이스 크기, 개발자 역량 등 환경 요인을 보정하는 승수
- **UFP(Unadjusted Function Point)**: 5대 기능 유형별 개수에 평균 복잡도 가중치를 곱해 단순 합산한 미조정 기능점수

</details>

## 예상문제

> 소프트웨어 개발 프로젝트의 예산 책정 및 대가 산정을 위한 비용 산정 기법의 3대 분류(하향식, 상향식, 수학적 모형)와 주요 모델(LOC, COCOMO, Putnam, 기능점수 FP)의 특징, 장단점 및 실무 적용 방안을 설명하시오. (10점/25점)

## Ⅰ. 공정 계약과 예산 건전성의 초석, SW 비용 산정의 개요

> 주먹구구식 덤핑과 예산 삭감을 탈피하고, **기능점수(FP)**와 **수학적 알고리즘 모델**로 투입 공수와 **적정 대가**를 산정함.

- 정의: SW 개발 및 유지관리 사업에서 프로젝트 규모(Size)를 객관적으로 측정하고, 과거 실적 데이터와 공학적 모형(**FP**, **COCOMO**)을 통해 필요한 공수(Effort)와 예산(Cost)을 과학적으로 도출하는 **원가 공학 프로세스**
- 목적: 발주처의 객관적 예산 확보 근거 마련, 수급인의 **적정 개발 대가** 보장 및 요구사항 변경에 따른 계약금액 조정 기준선 제공

## Ⅱ. SW 비용 산정 3대 접근 방식 및 5단계 기능점수 산정 프로세스

> 요구사항 분석에서 5대 기능 도출, 가중치 산정, 보정계수 반영, 대가 확정으로 이어지는 표준 파이프라인을 가동함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="기능점수(FP) 기반 공공 SW 개발비 산정 5단계 프로세스">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 요구사항 분석 및 시스템 경계 확정</strong></span>
    <small>RFP 및 과업지시서 기반 사용자 관점 기능/비기능 경계 정의<br />→ 시스템 경계 정의서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 5대 기능 유형 식별 및 분류</strong></span>
    <small>데이터 기능(ILF, EIF) 및 트랜잭션 기능(EI, EO, EQ) 도출<br />→ 기능 분류 매트릭스</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 미조정 기능점수(UFP) 산출</strong></span>
    <small>기능 유형별 표준 가중치(간이법 기준: ILF 7.5, EIF 5.4 등) 합산<br />→ UFP 계산 명세서 ($UFP = \sum 기능수 \times 가중치$)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 4대 보정계수 적용</strong></span>
    <small>프로젝트 규모, 연계 복잡성, 성능 요구, 다중 사이트 보정계수 반영<br />→ 최종 보정 기능점수 ($보정 FP = UFP \times \prod 보정계수$)</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ SW 개발비 확정</strong></span>
    <small>KOSA 고시 기능당 단가(약 55만 원/FP) 적용 및 직접경비/이윤 합산<br />→ 최종 개발비 산출 내역서</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>대가 정합성</strong></span> · 기능 요구명세 ↔ UFP 측정 ↔ 보정계수 ↔ KOSA 고시단가 100% 매핑</div>

### SW 비용 산정 3대 접근 방식 비교

| 접근 방식 | 대표 세부 기법 | 산출 메커니즘 | 장단점 및 추천 적용 시점 |
|---|---|---|---|
| **하향식 기법**<br>(Top-Down) | 전문가 판단,<br>**델파이 기법(Delphi)** | 시니어 엔지니어의 직관 또는 복수 전문가의 익명 피드백을 반복 수렴하여 견적 도출 | 신속한 개략 견적 가능하나 주관적 편향 존재 (사업 초기 예비타당성/기획 단계) |
| **상향식 기법**<br>(Bottom-Up) | 원천 코드 라인 수(LOC),<br>WBS 공수 산정 | WBS 최하위 작업 패키지별 라인 수 또는 세부 M/M 공수를 개별 집계 후 합산 | 정확도는 높으나 기획 초기 상세 WBS 도출 불가, 언어 종속적 (설계 완료 단계) |
| **수학적 모형**<br>(Algorithmic) | **COCOMO, Putnam**,<br>**기능점수(FP)** | 과거 프로젝트 축적 통계 데이터를 기반으로 규모, 공수, 기간 간의 수학 공식 적용 | 객관적 검증 가능 및 공공 표준이나 보정계수 산정 오버헤드 (발주 및 계약 단계) |

## Ⅲ. 대표적 수학적 모형 비교 (COCOMO vs Putnam vs 기능점수 FP)

> 소스코드 종속성 여부와 측정 관점에 따라 모델별 공학적 특성이 구분됨.

| 비교 항목 | COCOMO 모형 | Putnam 모형 | 기능점수 (FP, Function Point) |
|---|---|---|---|
| **제안자 및 기반** | Barry Boehm (KLOC 기반 통계 회귀) | Lawrence Putnam (Rayleigh 곡선) | Allan Albrecht (논리 기능 크기) |
| **산출 기준 변수** | 소스코드 라인 수 (KLOC), 15개 EAF | 생애주기 소요 시간($t$), 인력 투입 곡선 | **사용자 관점 5대 기능 (데이터/트랜잭션)** |
| **언어 독립성** | **종속적** (프로그래밍 언어별 편차 심함) | 종속적 (코드 규모 추정에 연계) | **완전 독립적 (언어와 무관한 기능 크기 측정)** |
| **개발 모드 구분** | 단순형(Organic), 중간형(Semi), 내장형(Embedded) | 전 수명주기에 걸친 동적 인력 배분 곡선 | 간이법(평균 복잡도), 정규법(상세 복잡도) |
| **주요 활용 영역** | 전통적 C/C++ 시스템 및 패키지 개발 견적 | 대형 프로젝트의 최적 개발 기간·인력 배분 | **공공 SW 조달, 발주 예산 및 법정 대가 표준** |

## Ⅳ. 실무 적용 시 주요 왜곡 요인과 통제 대책

> 기획 초기 기능 모호성과 임의적 예산 삭감을 방지하기 위해 간이 FP와 롤링 웨이브 계약을 적용해야 함.

| 왜곡 문제점 | 발생 원인 | 공학적·제도적 해결 대책 | 기대 효과 |
|---|---|---|---|
| **기획 초기 상세 스펙 미확정** | ISP/ISMP 단계에서 DB 테이블과 트랜잭션 속성이 미확정되어 정규 FP 측정 불가 | 화면 및 엔티티 수 기반 **간이 기능점수 산정법(Average Complexity)** 적용 | 조기 예산 확보 및 기획 오차 최소화 |
| **발주처의 임의 예산 삭감** | 예산 부처의 통계적 근거 없는 획일적 삭감 및 덤핑 발주 관행 | 과거 공공 SW 사업 실적 통계 및 **KOSA 공인 대가 가이드라인** 증빙 강제 | 적정 개발 예산 보장 |
| **과업 변경 시 추가 대가 미지급** | 구축 중 발주처 요구 추가 시 정량적 FP 재산정 체계 부재 | **RTM(요구사항 추적표)** 연동 형상관리 기반 증분 FP 자동 측정 및 과업심의 연계 | 공정한 계약금액 증액 (SW진흥법 제50조) |

## Ⅴ. 제값받기 실현을 위한 기술사적 제언

> 초기 불확실성을 극복하기 위해 간이 FP로 예산 범위를 잡고 분석 후 확정하는 단계적 정밀화 계약 모델을 도입해야 함.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: SW 비용 산정의 성패는 정교한 수학 공식이 아니라 '요구사항의 명확성'에 달려 있음. 요구사항이 안갯속인 상태에서 아무리 복잡한 FP나 COCOMO 공식을 돌려봐야 '정교하게 포장된 쓰레기 견적'이 나올 뿐임.
- 나라면: 기획/발주 단계에서는 간이 FP를 적용해 예산의 범위(Band: $\pm 15\%$)를 유연하게 설정하고, 본 사업 착수 후 3개월 시점에 요구사항 정의서가 동결되면 '정규 FP 확정 게이트'를 거쳐 최종 계약금액을 확정 정산하는 '단계적 정밀화(Rolling Wave FP) 계약 제도'를 도입하겠음.

### 실전 답안용 기술사적 제언

- 판정: 일회성 고정 총액 계약에서 요구사항 상세화에 맞춘 단계적 정밀화 정산으로 전환
- 대안: **Rolling Wave FP 계약 모델** 및 **RTM 기반 증분 FP 자동 산정 체계** 도입
- 검증: 기획-분석 단계 간 FP 변동률 15% 이내 관리 · 과업변경 시 증분 FP 100% 반영
- 효과: 덤핑 수주 및 무상 과업 근절 · 개발사 적정 대가 보장 및 공공 SW 품질 확보

<div class="itpe-pipeline is-vertical" role="img" aria-label="SW 비용 산정 현실화 및 제값받기를 위한 기술사적 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>기획 단계 모호한 요구로 주먹구구 예산 산정 · 과업 추가 시 대가 미반영</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>간이 FP 예산 밴드(±15%) + 착수 후 정규 FP 확정 게이트웨이 제도화</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>KOSA 공인 단가 준수 · RTM 기반 과업 변경 시 증분 FP 재산정</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>SW 제값받기 실현 · 잦은 납기 지연 및 개발자 야근 악순환 종식</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 소프트웨어 규모(Size)를 객관적으로 측정하고 통계 공학 모형(**FP**, **COCOMO**)을 적용하여 투입 공수(M/M)와 개발 예산을 과학적으로 산출하는 **원가 공학 체계**
- 목적: 발주처의 객관적 예산 확보 근거를 수립하고 개발사의 **적정 대가**를 보장하여 SW 산업 생태계 건전성 확보

### 2. 구성체계 및 기능점수(FP) 5대 기능

<div class="itpe-pipeline is-vertical" role="img" aria-label="기능점수 대가 산정 요약">
  <div class="itpe-pipeline-node"><strong>데이터 기능</strong><small>내부논리파일(ILF) · 외부연계파일(EIF)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>트랜잭션 기능</strong><small>외부입력(EI) · 외부출력(EO) · 외부조회(EQ)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>보정 및 개발비</strong><small>UFP × 4대 보정계수 × FP 고시단가 (원)</small></div>
</div>

### 3. 핵심 통제

- **언어 독립성 보장**: 코드 라인 수(LOC) 종속성을 극복하고 사용자 관점의 논리적 업무 기능으로 측정
- **과업 변경 연계**: 구축 중 추가 요구 발생 시 증분 FP를 측정하여 계약금액 증액 의결(SW진흥법 제50조)

## 출제 이력과 검증 출처

- 제117회, 제86회 KPC 기출: 소프트웨어 비용 산정 기법의 분류 및 기능점수(FP) 산정
- [과학기술정보통신부, 소프트웨어사업 대가산정 가이드라인](https://www.msit.go.kr)
- [한국소프트웨어산업협회(KOSA), SW사업 대가산정 해설서](https://www.sw.or.kr)

## 학습 체크

- [ ] SW 비용 산정 3대 접근 방식(하향식, 상향식, 수학적 모형)의 특징을 설명할 수 있는가?
- [ ] 기능점수(FP)의 5대 기능 유형과 간이법 산출 공식을 제시할 수 있는가?
- [ ] COCOMO 모형의 3대 개발 모드(Organic, Semi-detached, Embedded)를 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [CCPM(Critical Chain, TOC)](./112_critical_chain_toc.md)
- 연관 토픽: [과업심의(과업변경·사업기간 적정성)](./091_public_sw_cost_and_scope_change_criteria.md), [품질비용(Cost of Quality)](./106_cost_of_quality_coq.md)
- 다음 토픽: [개방형 혁신(Open Innovation)](./114_open_innovation.md)
