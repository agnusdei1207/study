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
author: "Antigravity"
extra:
  model: "Gemini 3.8 Flash"
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

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="fp-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Background Frame -->
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    <text x="260" y="24" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--color-text, #1e293b)">기능점수(Function Point) 5대 기능 및 경계(Boundary) 구조</text>

    <!-- Application Boundary Line -->
    <rect x="15" y="38" width="340" height="165" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" stroke-dasharray="6,4"/>
    <text x="30" y="54" font-size="7.5" font-weight="bold" fill="var(--color-primary, #2563eb)">[애플리케이션 경계 내부]</text>

    <!-- Internal Data: ILF -->
    <rect x="25" y="65" width="145" height="60" rx="4" fill="var(--color-bg-subtle, #eff6ff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="97" y="82" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">ILF (내부논리파일)</text>
    <text x="97" y="97" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">내부 등록/수정/관리</text>
    <text x="97" y="112" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">복잡도: RET × DET</text>

    <!-- Transactions: EI, EO, EQ inside boundary -->
    <rect x="190" y="65" width="155" height="125" rx="4" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="267" y="80" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">트랜잭션 기능 (3종)</text>
    
    <!-- EI -->
    <rect x="200" y="88" width="135" height="28" rx="3" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="267" y="101" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">EI (외부입력)</text>
    <text x="267" y="112" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">내부 ILF 변경 (등록/수정/삭제)</text>

    <!-- EO -->
    <rect x="200" y="120" width="135" height="28" rx="3" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="267" y="133" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">EO (외부출력)</text>
    <text x="267" y="144" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">파생 계산/통계 포함 출력</text>

    <!-- EQ -->
    <rect x="200" y="152" width="135" height="28" rx="3" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="267" y="165" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text, #1e293b)">EQ (외부조회)</text>
    <text x="267" y="176" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">단순 검색/데이터 조회 표시</text>

    <!-- External System & EIF -->
    <rect x="365" y="38" width="140" height="165" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="435" y="54" text-anchor="middle" font-size="7.5" font-weight="bold" fill="var(--color-text-muted, #64748b)">[외부 시스템 영역]</text>

    <rect x="375" y="65" width="120" height="85" rx="4" fill="var(--color-bg-subtle, #fefce8)" stroke="#ca8a04" stroke-width="1"/>
    <text x="435" y="85" text-anchor="middle" font-size="8" font-weight="bold" fill="#ca8a04">EIF (외부연계파일)</text>
    <text x="435" y="105" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">타 시스템 관리</text>
    <text x="435" y="120" text-anchor="middle" font-size="7" fill="var(--color-text, #334155)">단순 참조(Read)</text>
    <text x="435" y="138" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">복잡도: RET × DET</text>

    <!-- Interaction Line between EI and ILF -->
    <line x1="200" y1="100" x2="170" y2="100" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#fp-arrow)"/>
  </svg>
</div>

### 기능점수 산정 공식 및 보정 체계

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="calc-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <!-- Background -->
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>
    
    <!-- Step 1 -->
    <rect x="15" y="20" width="105" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="15" y="20" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="67" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">① 기능 식별</text>
    <text x="67" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">5대 기능 분류</text>
    <text x="67" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">경계 내외 식별</text>
    <text x="67" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[ILF/EIF/EI/EO/EQ]</text>

    <!-- Arrow 1 -> 2 -->
    <line x1="120" y1="72" x2="138" y2="72" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#calc-arrow)"/>

    <!-- Step 2 -->
    <rect x="140" y="20" width="105" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="140" y="20" width="105" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="192" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">② 복잡도 매트릭스</text>
    <text x="192" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">RET/DET/FTR 계수</text>
    <text x="192" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">상/중/하 가중치</text>
    <text x="192" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[간이법은 평균적용]</text>

    <!-- Arrow 2 -> 3 -->
    <line x1="245" y1="72" x2="263" y2="72" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#calc-arrow)"/>

    <!-- Step 3 -->
    <rect x="265" y="20" width="110" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <rect x="265" y="20" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="320" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">③ 미조정 FP(UFP)</text>
    <text x="320" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">기능별 FP 총합</text>
    <text x="320" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">Σ(기능수 × 가중치)</text>
    <text x="320" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-primary, #2563eb)">[순수 기능 규모]</text>

    <!-- Arrow 3 -> 4 -->
    <line x1="375" y1="72" x2="393" y2="72" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#calc-arrow)"/>

    <!-- Step 4 -->
    <rect x="395" y="20" width="110" height="105" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="395" y="20" width="110" height="22" rx="6" fill="var(--color-bg-subtle, #f1f5f9)"/>
    <text x="450" y="35" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">④ 보정 개발비</text>
    <text x="450" y="58" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">5대 보정계수 곱셈</text>
    <text x="450" y="74" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">FP 단가(원/FP) 적용</text>
    <text x="450" y="94" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-accent, #0284c7)">[최종 계약 대가]</text>

    <!-- Bottom Result Formula -->
    <rect x="15" y="140" width="490" height="42" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="260" y="157" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">공식: 최종 보정 FP = UFP × (규모) × (연계복잡도) × (성능요구수준) × (운영환경) × (보안성)</text>
    <text x="260" y="172" text-anchor="middle" font-size="7.5" fill="var(--color-text-muted, #64748b)">개발비 = 최종 보정 FP × FP당 단가 (공공 SW 대가산정 가이드라인 법정 표준)</text>
  </svg>
</div>

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

## 4. 점검 및 합격 기준 (Checklist & Exit Criteria)

### 기능점수 산정 적정성 검증 체크리스트

| 검증 영역 | 상세 점검 항목 | 판정 기준 |
|---|---|---|
| **경계 식별** | 배치/인터페이스/서브시스템 간 경계 중복 정의 여부 | 단일 애플리케이션 경계 원칙 준수 |
| **데이터 기능** | 임시 테이블(Temp, Log), 코드성 테이블의 ILF 포함 여부 | 비즈니스 논리 엔터티만 ILF 계수 |
| **트랜잭션 기능** | 단순 조회(EQ)와 파생 계산 출력(EO)의 명확한 구분 | 집계/통계/파생 로직 부재 시 EQ 분류 |
| **보정계수** | 5대 보정계수(규모, 연계, 성능, 운영, 보안) 증빙 충족 | 가이드라인 상한선(0.85~1.15) 준수 |

## 5. 기대 효과 및 미래 전망

- **기대 효과**:
  - **발주자-수주자 신뢰 회복**: 주관적 공수 산정을 배제하고 객관적 기능 규모 기반의 법정 대가 산정.
  - **소프트웨어 제값주기 정착**: 과도한 저가 낙찰 및 무상 과업 추가 관행 차단.
- **미래 전망**:
  - 소스코드 AST 정적 분석 도구와 연계한 Automated Function Points(AFP) 자동 산정 파이프라인 도입.
  - 마이크로서비스(MSA) 및 클라우드 네이티브 환경에 맞춘 API 단위 기능점수 산정 가이드 고도화.

## 6. 결론 및 실전 팁

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**  
> 기능점수는 단순한 '돈 계산 공식'이 아니라, 소프트웨어 공학에서 "기술 종속적 코딩(LOC)으로부터 비즈니스 가치(Function)를 분리해낸 위대한 표준 척도"이다. 그러나 현실 공공 프로젝트에서는 기획 단계 간이법으로 묶인 고정 예산과 구축 단계의 요구사항 폭증이 충돌하는 분쟁의 온상이 된다. 기술사는 산정 공식 암기에 그치지 않고, **설계 완료 후 정규 FP로 계약 금액을 조정하는 '과업심의위원회 사후 정산 거버넌스'**를 해결책으로 제시해야 한다.

> **[나라면 이렇게 쓴다]**  
> 2교시형 문제로 출제된다면, 1단락에 5대 기능(ILF/EIF/EI/EO/EQ)과 경계 다이어그램을 명쾌하게 배치하고, 2단락에서 정규법과 간이법의 차이를 비교하겠다. 그리고 3단락 실무 제언에서는 **"Git 형상관리와 정적 분석기를 결합하여 엔터티 클래스와 컨트롤러 API를 파싱하는 Automated Function Points(AFP) 자동 계측 체계"**를 제안하여 전통적 수작업 산정의 주관성 한계를 돌파하는 현대적 아키텍처 통찰을 보여주겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 기획 단계 예산 편성 시 간이법을 적용하되, 상세설계 완료 시점에 전수 정규 기능점수를 재산정하여 $\pm 10\%$ 초과 변동 시 과업 변경 심의 필수 판정.
- **대응 방안**: 데이터 모델 정규화 검토를 통해 코드 테이블 및 임시 백업 테이블의 ILF 중복 계수를 사전 필터링하고, 단순 조회의 EO 왜곡 전면 방지.
- **검증 체계**: 외부 전문 감리 및 기능점수 공인 검증 기관의 교차 실사를 수행하여 산정 오차율을 $5\%$ 이내로 통제.
- **기대 효과**: 개발 사업자의 부당한 과업 추가 및 적자 리스크를 원천 차단하고, 공공 SW 프로젝트 납기 준수율 95% 이상 달성.

<div class="itpe-flow-map" role="img" aria-label="기능점수 산정 및 적정 대가 보증 거버넌스 파이프라인">
  <div class="itpe-flow-node">
    <strong>기획 단계 간이법 산정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>예산</strong><span>평균 가중치 기반 발주 예산</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>상세설계 정규법 재산정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>실측</strong><span>RET/DET/FTR 전수 계수</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node is-current">
    <strong>과업심의위원회 조정</strong>
    <div class="itpe-step-detail">
      <strong>판정</strong><span>사업 범위 및 예산 적정 정산</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>소프트웨어 제값주기 달성</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>결과</strong><span>고품질 무결 시스템 인도</span></div>
    </div>
  </div>
</div>

## 7. 참고 및 연계 학습

- [ISMP(정보시스템 마스터플랜)](../../01-it-strategy/001_ismp.md)
- [요구사항 추적표(RTM)](./102_requirement_traceability_matrix.md)
- [상용SW 직접구매 제도](./101_commercial_sw_direct_purchase.md)
- [소프트웨어 품질 비용(COQ)](./150_software_quality_cost.md)
