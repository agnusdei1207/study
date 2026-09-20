---
title: "소프트웨어 사업 대가산정"
author: "Antigravity"
date: "2026-09-20T21:12:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "Gemini 3.8 Flash (High)"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 사업관리와 원가·규모 산정을 거쳐 소프트웨어 사업 대가산정으로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>사업관리·원가 산정</span>
  <strong>소프트웨어 사업 대가산정</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **소프트웨어 사업 대가산정**은 **소프트웨어 진흥법 제46조**에 근거하여 기획·개발·유지관리 등 SW 생명주기 제반 비용을 **기능점수(FP)**, **투입공수(M/M)**, 요율로 객관화하는 원가산정 체계
- 메커니즘: 사업 유형 판별 → 표준 산정식 적용(개발비=보정 **FP** × 단가, 기획=**M/M**, 운영=**SLA**) → **과업심의위원회** 통한 변경 대가 반영
- 산출: 기능점수 산정서 · **SW 개발원가** 내역서 · 직접경비 및 유지관리 대가 기준선

<div class="itpe-flow-map" role="img" aria-label="사업 유형 식별에서 산정 모델 적용 및 과업 변경 통제로 이어지는 흐름">
  <div class="itpe-flow-node">
    <strong>사업 유형 식별</strong>
    <small>기획/컨설팅 · 신규/재개발 · 유지관리 · 운영위탁</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>표준 산정 모델 적용</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>개발/재개발</strong><span><span class="itpe-keyword"><strong>기능점수(FP)</strong></span> 기반 개발원가</span></div>
      <div class="itpe-flow-branch"><strong>기획/컨설팅</strong><span><span class="itpe-keyword"><strong>투입공수(M/M)</strong></span> 기반 인건비</span></div>
      <div class="itpe-flow-branch"><strong>유지관리/운영</strong><span>산정요율 및 <span class="itpe-keyword"><strong>SLA</strong></span> 연계 대가</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>대가 구조 확정</strong>
    <small>직접인건비 + 제경비 + 기술료 + 직접경비</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>계약 및 과업 변경 통제</strong>
    <small>RFP 발주 기준선 확정 · <span class="itpe-keyword"><strong>과업심의위원회</strong></span> 변경 정산</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **FP(Function Point)**: 소프트웨어가 사용자에게 제공하는 논리적 기능량을 측정하는 객관적 규모 단위
- **M/M(Man-Month)**: 프로젝트에 투입되는 기술인력 1인이 1개월 동안 수행하는 업무량을 기준으로 산정하는 방식
- **ILF(Internal Logical File)**: 대상 시스템 내부에서 유지·관리되는 논리적 데이터 그룹
- **EIF(External Interface File)**: 타 시스템에서 유지되며 대상 시스템이 참조 목적으로 활용하는 외부 데이터 그룹
- **EI(External Input)**: 시스템 경계 외부에서 유입되어 내부논리파일을 갱신하거나 동작을 제어하는 트랜잭션 기능
- **EO(External Output)**: 계산 및 데이터 파생 처리를 거쳐 경계 외부로 정보를 출력하는 트랜잭션 기능
- **EQ(External Inquiry)**: 계산 과정 없이 단순 검색을 통해 즉시 데이터를 조회·출력하는 트랜잭션 기능
- **과업심의위원회**: 공공 SW 사업에서 발주자의 부당한 과업 변경을 심의하고 계약금액을 조정하는 법정 기구

</details>

## 예상문제

> 소프트웨어 진흥법 및 SW사업 대가산정 가이드에 따른 사업 유형별 대가산정 체계를 설명하고, 기능점수(FP) 기반 개발비 산정 6단계 절차와 5대 보정계수, 과업 변경 시 대가 조정 방안을 논하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **SW사업 대가산정 가이드** | 과기정통부 고시 근거, 기능점수 단가 및 유지관리 요율 등 법정 산정기준 | Ⅰ 개요, Ⅲ 체계 |
| **기능점수(FP) 모형** | 데이터 기능(ILF/EIF)과 트랜잭션 기능(EI/EO/EQ) 기반 SW 규모 산정 | Ⅱ 절차, Ⅳ 비교 |
| **과업변경 대가 조정** | 과업심의위원회를 통한 범위 변경 승인 및 FP 기반 적정 대가 조정 | Ⅴ 대책, Ⅵ 결론 |

## Ⅰ. 적정 대가 지급과 SW 품질 확보를 위한 소프트웨어 사업 대가산정의 개요

> 기능점수와 표준 산식을 통해 주관적 견적 마찰을 차단하며, 성패는 단순 초기 예산 확보가 아닌 **과업 변경에 따른 Traceability**로 판정함.

- 정의: **소프트웨어 진흥법 제46조**에 따라 기획·구현·운영·유지관리 수명주기 전반의 투입 가치를 표준화된 산식으로 산출하는 **원가산정 체계**
- 목적: 예산 과소 책정 방지, 무상 과업 근절, SW 품질 확보

## Ⅱ. 기능점수(FP) 기반 SW 개발비 산정 6단계 프로세스

> 경계 정의부터 개발원가 확정까지 `경계식별 → 데이터기능 → 트랜잭션기능 → 미조정FP → 보정계수 → 원가확정`의 6단계를 거쳐 과학적으로 산출함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="기능점수 기반 SW 개발비 산정 6단계 절차 및 단계별 활동과 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 측정 유형 및 경계 확정</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>신규/재개발 구분 · 애플리케이션 경계 및 외부 인터페이스 식별</span>
      <strong>산출</strong><span>애플리케이션 경계 정의서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 데이터 기능 식별</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>내부논리파일(ILF) · 외부연계파일(EIF) 식별 및 DET/RET 복잡도 산정</span>
      <strong>산출</strong><span>데이터 기능점수 집계표</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 트랜잭션 기능 식별</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>외부입력(EI) · 외부출력(EO) · 외부조회(EQ) 식별 및 FTR/DET 복잡도 산정</span>
      <strong>산출</strong><span>트랜잭션 기능점수 집계표</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 미조정 기능점수(UFP) 산출</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>데이터 기능점수 총합과 트랜잭션 기능점수 총합 단순 합산</span>
      <strong>산출</strong><span>미조정 기능점수(UFP) 총괄표</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 5대 보정계수 적용</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>규모 · 연계복잡성 · 성능요구수준 · 다중사이트 · 품질요건 계수 곱연산</span>
      <strong>산출</strong><span>보정 기능점수(AFP) 계산서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑥ SW 개발원가 확정</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>보정 FP × 고시 단가 산정 및 직접경비 합산</span>
      <strong>산출</strong><span>최종 SW 개발비 산정서</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · 요구사항 목록 ↔ WBS ↔ ILF/EIF/EI/EO/EQ ↔ FP 산출 내역 양방향 추적</div>

## Ⅲ. 사업 유형별 SW 사업 대가산정 체계

> 사업 특성에 부합하는 표준 산정 모델을 적용해야 예산의 왜곡과 사업 실패를 예방할 수 있음.

| 사업 유형 | 주 적용 방식 | 세부 산정 공식 및 핵심 구성요소 |
|---|---|---|
| **기획·컨설팅** | **투입공수(M/M)** 방식 | `직접인건비(M/M × 평균임금) + 제경비(110~120%) + 기술료(20~40%) + 직접경비` |
| **SW 신규개발** | **기능점수(FP)** 방식 | `[보정후 FP × FP단가] + 직접경비` (규모·연계·복잡도·성능·품질 5대 보정계수) |
| **SW 재개발** | FP 기반 영향도 | `변경/재사용 FP × 변경영향도 계수 × FP단가 + 직접경비` |
| **SW 유지관리** | 산정요율 방식 | `SW 도입가격 × 기본요율(10~15%) × 유지관리 난이도 보정계수` |
| **SW 운영위탁** | 업무량 / SLA 방식 | `운영업무량 투입공수 + SLA 달성도 인센티브/페널티(Service Credit)` |

## Ⅳ. 기능점수(FP) vs 투입공수(M/M) vs SLA 성과기반 비교

> 개발은 기능 규모(FP), 불확실한 기획은 공수(M/M), 지속적 운영은 성과(SLA) 기준이 가장 적합함.

| 비교 기준 | 기능점수(FP) 방식 | 투입공수(M/M) 방식 | SLA 성과기반 방식 |
|---|---|---|---|
| **산정 기준** | 논리적 사용자 기능 규모 (기능량) | 투입 인력의 기술등급 및 투입 기간 | 합의된 서비스 수준 목표(SLA) 달성도 |
| **적용 영역** | 요구사항이 명세화된 신규/재개발 | ISP/ISMP, 컨설팅, 연구개발 | ITO 운영위탁, 클라우드 인프라 운영 |
| **장점** | 개발 언어·기술에 독립적, 객관적 측정 | 직관적 산정 가능, 유연한 계약 변경 | 서비스 품질 중심 관리, 생산성 혁신 유도 |
| **단점** | 초기 요구사항 모호 시 산정 오차 발생 | 머릿수 채우기 유발, 개발 생산성 저하 | SLA 지표 설계 난이도, 계측 분쟁 위험 |
| **통제 장치** | **RTM**, 공인 FP 심의관 검증 | WBS 공수 내역서, 근태 및 공정 관리 | Service Credit, 정기 제3자 성과평가 |

## Ⅴ. 실무 대가산정 왜곡 요인과 공학적·제도적 통제 방안

> 초기 간이법 예산 고정과 무상 과업 추가는 SW 산업의 핵심 고질병으로 제도적 통제가 필요함.

| 위험 | 대책 | 효과 |
|---|---|---|
| **예산 결손 발생** | **ISMP** 정밀 FP 산정 의무화 및 본 예산 재산정 | 현실적 예산 확보 및 조달 유찰 방지 |
| **자의적 계수 조작** | 객관적 요구 증빙 첨부 의무화 및 감리 검증 | 산정 데이터 신뢰성 및 감사 정당성 확보 |
| **무상 과업 요구** | **과업심의위원회** 개최 의무화 및 대가 조정 | 개발사 권익 보호 및 과업 변경 분쟁 예방 |
| **비기능 요구사항 배제** | 비기능 요구사항을 직접경비 또는 독립 컨설팅으로 분리 | SW 품질 및 엔터프라이즈 안정성 확보 |

## Ⅵ. 계약 기준선 유지와 사후 정산 중심의 기술사적 제언

> 초기 산정은 조달의 출발점일 뿐이며, 구축 단계의 요구사항 변경을 **과업심의위원회**와 **RTM**으로 추적 정산해야 제값 주기가 완성됨.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 소프트웨어 대가산정에서 가장 빈번한 실패는 초기 기획(ISP/ISMP) 단계의 개략 산정(간이법) 예산이 본 사업 RFP에 그대로 고정되어, 실제 요구사항 상세화 과정에서 발생하는 기능 추가를 무상으로 개발사에 전가하는 관행임. 대가산정은 초기 예산 확정이 아니라 사업 생명주기 전반의 변경 통제 기준선(Baseline)이어야 함.
- 나라면: 제안요청서(RFP) 작성 시 요구사항 명세서와 FP 기능 항목 간 1:1 Traceability를 의무화하고, 과업 범위가 10% 이상 변동할 경우 '과업심의위원회' 소집을 자동 발동하는 계약 특약 조항을 명문화하겠음.

### 실전 답안용 기술사적 제언

- 판정: 일회성 예산 편성용 견적에서 라이프사이클 계약 기준선으로 전환
- 대안: **ISMP** 정밀 FP 산정 의무화 및 **과업심의위원회** 기반 변경 대가 정산
- 검증: 요구사항-FP 매핑 추적률 100% · 과업 변경 심의 적정 대가 반영률 100%
- 효과: 공공 SW 사업의 유찰·분쟁 예방 및 개발 생태계 상생 도모

<div class="itpe-pipeline is-vertical" role="img" aria-label="SW 대가산정 기준선 정착을 위한 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>간이법 예산 고정 · 무상 과업 추가 강요 및 대가 미지급</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>ISMP 정밀 FP 산정 의무화 · 과업심의위원회 정례화</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>요구사항-FP 1:1 매핑 RTM · 과업 변경 계약금액 공식 조정</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>적정 소프트웨어 대가 보장 · 공공 SW 고품질 개발 유도</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **소프트웨어 진흥법 제46조**에 따라 기획·개발·유지관리 전반의 투입 가치를 **기능점수(FP)**, **투입공수(M/M)** 등 객관적 기준으로 산출하는 **원가산정 체계**
- 목적: 예산 과소 책정 방지, 무상 과업 근절, SW 품질 확보

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="1교시 10점용 기능점수 개발비 산정 메커니즘">
  <div class="itpe-pipeline-node">
    <strong>경계 확정</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>애플리케이션 경계 · 인터페이스</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>기능 식별</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>데이터(ILF/EIF) + 트랜잭션(EI/EO/EQ)</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>미조정 FP</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>기능 복잡도별 가중치 합산</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>보정계수 적용</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>규모 · 연계 · 성능 · 사이트 · 품질</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개발원가 확정</strong>
    <div class="itpe-step-detail"><strong>활동</strong><span>보정 FP × 고시 단가 + 직접경비</span></div>
  </div>
</div>

### 3. 핵심 통제

- **기능점수 5대 보정계수**: 규모, 연계복잡성, 성능요구수준, 다중사이트, 품질요건을 통한 현실화
- **과업심의위원회**: 과업 범위 변경 시 계약금액 및 기간 연장의 법적 구속력 보장
- **사업 유형 분리 산정**: 개발비(FP), 기획비(M/M), 유지관리비(요율)의 혼용 금지

## 출제 이력과 검증 출처

- 제132회 정보관리기술사 1교시: 기능점수(Function Point) 산정 방식 및 구성요소
- 제137회 정보관리기술사 2교시: 소프트웨어 사업 대가산정 가이드 개정 방향 및 공공 발주 실무 적용
- 제139회 정보관리기술사 1교시: 소프트웨어 과업 변경 심의 및 대가 조정 기준
- 한국AI·SW산업협회, [SW사업 대가산정 가이드](https://www.sw.or.kr)
- 과학기술정보통신부, [소프트웨어 진흥법 및 공공 소프트웨어사업 적정대가 지급 지침](https://www.msit.go.kr)

## 학습 체크

- [ ] 사업 유형(기획, 개발, 재개발, 유지관리, 운영)별 산정 방식을 구분할 수 있는가?
- [ ] 데이터 기능(ILF, EIF)과 트랜잭션 기능(EI, EO, EQ)의 식별 기준을 설명할 수 있는가?
- [ ] FP 방식, M/M 방식, SLA 성과기반 방식을 5개 이상의 비교축으로 대조할 수 있는가?
- [ ] 과업 변경 시 과업심의위원회를 통한 대가 조정 절차와 필요성을 논술할 수 있는가?

## 연결 토픽

- 이전 토픽: [범정부 AI 공통기반](./025_pan_government_ai_common_infrastructure.md)
- 연관 토픽: [ISMP](./001_ismp.md), [제안요청서(RFP)](./049_rfp.md), [공공 SW 사업 발주·계약](./039_public_sw_contract.md), [EVM](./032_evm.md)
- 다음 토픽: [액티브-액티브 스토리지 DR](./027_active_active_storage_dr.md)
