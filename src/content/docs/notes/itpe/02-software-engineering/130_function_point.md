---
title: "기능점수(Function Point)"
category: "02-software-engineering"
tags:
  - "기능점수"
  - "FP"
  - "IFPUG"
  - "소프트웨어대가산정"
  - "데이터기능"
  - "트랜잭션기능"
date: "2026-09-20"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어공학에서 프로젝트 관리 및 비용 산정을 거쳐 기능점수로 이어지는 지식 위치">
  <span>소프트웨어공학</span>
  <span>프로젝트 관리·비용 산정</span>
  <strong>기능점수(Function Point)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 프로그래밍 언어나 개발 도구에 따라 들쭉날쭉한 소스코드 라인 수(LOC)의 왜곡을 방지하기 위해, 사용자 관점에서 시스템이 제공하는 논리적 데이터 저장 기능과 트랜잭션 처리 기능을 표준 규격으로 계량화하여 소프트웨어 규모와 적정 대가를 산정하는 국제표준(IFPUG, ISO/IEC 14143) 기능 규모 측정법
- 메커니즘: 측정 범위 설정 → 5대 기능 식별(데이터 2종, 트랜잭션 3종) → 복잡도 인자(RET, DET, FTR) 측정 → 미조정 기능점수(UFP) 산출 → 5대 보정계수 적용 → 최종 보정 기능점수 및 사업 대가 산출
- 산출물: 기능점수 산정 명세서 · 기능 식별 목록표(ILF/EIF/EI/EO/EQ) · 소프트웨어 사업 대가 산정서

<div class="itpe-flow-map" role="img" aria-label="기능점수 산정 절차 및 대가 산정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 측정 대상 및 애플리케이션 경계 식별</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>경계</strong><span>측정 대상 시스템의 내부 범위와 외부 시스템 경계 정의</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 5대 기능 식별 및 복잡도 매트릭스 적용</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>데이터(2종)</strong><span>ILF(내부논리파일), EIF(외부연계파일) $\rightarrow$ RET, DET</span></div>
      <div class="itpe-flow-branch"><strong>트랜잭션(3종)</strong><span>EI(외부입력), EO(외부출력), EQ(외부조회) $\rightarrow$ FTR, DET</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>3단계: 산정 정확도 검증 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>임시/캐시 테이블이 제외되고 비즈니스 논리 단위로 식별되었는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (Pass)</strong>
      <span>미조정 FP 합산 $\rightarrow$ 보정계수(규모, 연계 등) 적용 및 최종 대가 확정</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (Fail)</strong>
      <span>중복 계수/단순 조회 왜곡 탐지 $\rightarrow$ 데이터 모델 정규화 재검토</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **ILF(Internal Logical File)**: 애플리케이션 내부에서 유지·관리되며 비즈니스 로직에 의해 지속적으로 등록, 수정, 삭제되는 논리적 데이터 그룹
- **EIF(External Interface File)**: 타 시스템에서 유지·관리되지만, 현재 애플리케이션에서 오직 참조(Read-only) 목적으로 사용하는 외부 연계 데이터 그룹
- **EI / EO / EQ**: 외부입력(EI, 내부 파일 갱신), 외부출력(EO, 파생 데이터 계산/통계 출력), 외부조회(EQ, 단순 데이터 검색 및 표시)
- **DET(Data Element Type)**: 사용자가 식별할 수 있는 고유하고 반복되지 않는 필드(컬럼) 단위 데이터 항목
- **RET(Record Element Type)**: ILF나 EIF 내부에서 사용자가 인식 가능한 하위 레코드 데이터 서브그룹(예: 마스터-디테일 테이블)
- **FTR(File Type Referenced)**: 트랜잭션 기능(EI, EO, EQ)을 수행하는 과정에서 읽거나 갱신하는 ILF 또는 EIF의 개수
</details>

## 1. 개요 및 필요성

### LOC(코드 라인 수)의 한계와 사용자 관점 기능 측정

과거의 소프트웨어 비용 산정 방식인 LOC(Lines of Code)는 프로그래밍 언어의 특성에 따라 심각한 모순을 낳았다. 동일한 기능을 구현하더라도 어셈블리어로는 수천 라인이 필요하지만 파이썬으로는 수십 라인으로 끝나므로, 비효율적인 코드를 길게 작성할수록 더 높은 대가를 받는 왜곡이 발생했다.

기능점수(Function Point)는 **구현 기술이나 언어와 완전히 독립적으로, 소프트웨어가 사용자에게 제공하는 논리적 기능의 양**을 측정한다. 발주자와 수주자가 모두 이해할 수 있는 공통 척도를 제공하여, 국내 공공 소프트웨어 사업 대가 산정의 공식 법정 표준으로 정착되었다.

### 정규법(상세 산정) vs 간이법(평균 복잡도) 비교

| 구분 | 정규법 (Detailed Function Point) | 간이법 (Average Weight Function Point) |
|---|---|---|
| **적용 시점** | 분석 및 상세설계 완료 후 (사업 구축/정산 단계) | 사업 기획, 예산 편성, 발주 준비 단계 |
| **복잡도 판정** | 기능별 RET, DET, FTR을 전수 계수하여 상/중/하 가중치 적용 | 각 기능 유형별 사전에 정의된 **평균 가중치** 일괄 곱셈 |
| **평균 가중치** | 기능마다 상이 (ILF: 7/10/15, EI: 3/4/6 등) | ILF: 7.5, EIF: 5.4, EI: 4.6, EO: 5.2, EQ: 3.9 |
| **정확도** | 매우 높음 (실제 설계서 기반 오차 최소) | 상대적으로 낮음 (초기 개략적 예산 산정용) |
| **산정 소요 공수** | 데이터 모델 및 상세 화면 분석으로 많은 시간 소요 | 화면/테이블 개수 추정만으로 신속 산정 가능 |

## 2. 아키텍처 및 핵심 메커니즘

### 기능점수 5대 기능 분류 체계

```text
+-------------------------------------------------------------------------+
|                  기능점수(Function Point) 5대 기능 분류 구조            |
+-------------------------------------------------------------------------+
|                                                                         |
|                          [ 사용자 요구사항 ]                            |
|                                   │                                     |
|         ┌─────────────────────────┴─────────────────────────┐           |
|         v                                                   v           |
|  [ 데이터 기능 (Data Functions) ]             [ 트랜잭션 기능 (Transactions) ]|
|  논리적 데이터 저장 및 참조                   데이터 입력, 가공, 출력, 조회     |
|                                                                         |
|  - ILF (내부논리파일) :                       - EI (외부입력) :                 |
|    경계 내부에서 유지/수정되는 파일               내부 DB 등록/수정/삭제 처리   |
|    (복잡도 결정: RET 서브그룹, DET 필드)         (복잡도: FTR 참조파일, DET)    |
|                                                                         |
|  - EIF (외부연계파일) :                       - EO (외부출력) :                 |
|    타 시스템 파일이나 단순 참조용 파일            파생 계산, 통계 로직 포함 출력|
|    (복잡도 결정: RET 서브그룹, DET 필드)      - EQ (외부조회) :                 |
|                                                   계산 없는 단순 검색/조회 출력 |
+-------------------------------------------------------------------------+
```

### 기능점수 산정 공식 및 보정 체계

1. **미조정 기능점수(UFP) 계산**:
   $$UFP = \sum (\text{기능 유형별 개수} \times \text{복잡도 가중치})$$
2. **보정계수 적용 (공공 SW 대가산정 가이드 기준)**:
   $$최종 보정 FP = UFP \times (규모 보정) \times (연계 복잡도) \times (성능 요구수준) \times (운영환경) \times (보안성 수준)$$
3. **최종 소프트웨어 개발비 산출**:
   $$개발비 = 최종 보정 FP \times FP당 단가 (원/FP)$$

## 3. 실무 적용 및 고려사항

### 위험 대응 매트릭스

| 위험 | 대책 | 효과 |
|---|---|---|
| 공통 코드 테이블 및 임시 백업 테이블을 개별 ILF로 과다 산정하여 감사 지적 및 대가 삭감 | 데이터 모델의 제3정규화를 검증하고 단일 비즈니스 엔터티 관점에서 마스터-디테일은 1개 ILF로 통합 | 산정 적법성 확보 및 감사 리스크 완전 제거 |
| 단순 검색 조회를 계산 로직이 있는 EO(외부출력)로 둔갑시켜 기능점수를 부풀리는 행위 | 파생 데이터 계산(집계, 세금 계산 등) 여부를 검증하여 계산이 없는 건은 EQ(외부조회)로 재분류 | 기능 유형 식별의 객관성 및 신뢰성 확보 |
| 기획 단계 간이법 예산이 확정된 후 구축 단계에서 비즈니스 요구사항 폭증으로 사업자 적자 | 설계·구축 분할 발주 또는 과업심의위원회를 통해 상세설계 시점의 정규 FP 기준으로 계약 변경 증액 | 적정 대가 보장 및 사업 유찰/품질 부실 방지 |

## 4. 기술사 답안 차별화 포인트

### 기획 단계와 구축 단계의 FP 단절 문제와 정산 계약 제언

국내 공공 SW 사업의 고질적인 분쟁은 **"기획 단계 간이법으로 확정된 예산으로 구축 단계의 방대한 요구사항을 강요하는 구조"**에서 발생한다. 이를 해결하기 위해 기본설계 완료 시점에 산출된 정규 기능점수(Detailed FP) 결과를 바탕으로 계약 금액을 $\pm 10\%$ 범위 내에서 유연하게 사후 정산하는 **'가변형 계약 제도'** 및 과업심의위원회 정례화 방안을 3단락 또는 전문가 제언으로 제시한다.

### 자동화된 소스코드 기반 FP 산정 도구(Automated FP) 동향

기존 기능점수 산정은 산정자의 주관과 역량에 따라 동일 시스템에서도 최대 20~30%의 편차가 발생하는 한계가 있었다. 최근에는 형상관리(Git)와 정적 분석기를 연계하여 소스코드의 엔터티 클래스와 API 컨트롤러 매핑을 파싱하여 OMG Automated Function Points(AFP) 표준으로 자동 계측하는 **"Automated FP 파이프라인"**을 소개하여 신뢰성 혁신 방안을 제시한다.

## 5. 참고 및 연계 학습

- [ISMP(정보시스템 마스터플랜)](../../01-it-strategy/001_ismp.md)
- [요구사항 추적표(RTM)](./102_requirement_traceability_matrix.md)
- [상용SW 직접구매 제도](./101_commercial_sw_direct_purchase.md)
- [소프트웨어 품질 비용(COQ)](./150_software_quality_cost.md)
