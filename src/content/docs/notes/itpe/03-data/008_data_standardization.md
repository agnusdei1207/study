---
title: "데이터 표준화(공공 DB 표준화 지침·테이블 정의서 포함)"
category: "03-data"
tags:
  - "데이터표준화"
  - "표준단어"
  - "표준용어"
  - "표준도메인"
  - "표준코드"
  - "테이블정의서"
  - "공공DB표준화지침"
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
extra:
  model: "GPT-6"
  keyword_grade: "A"
sidebar:
  badge:
    text: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 관리에서 메타데이터 표준 및 데이터 표준화로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 표준·메타데이터</span>
  <strong>데이터 표준화(공공 DB 표준화 지침·테이블 정의서 포함)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 데이터의 명칭·정의·형식·규칙을 전사적으로 통일하여 이음동의어와 동음이의어를 배제하고, 시스템 간 상호운용성과 데이터 품질을 보증하는 핵심 기준선(Baseline)
- 메커니즘: 현업 비즈니스 용어 수집 $\rightarrow$ 4대 사전(단어·용어·도메인·코드) 정의 $\rightarrow$ 명명 규칙(단어 조합+분류어) 수립 $\rightarrow$ 테이블 정의서 및 물리 모델 매핑 $\rightarrow$ DDL Linter 검증
- 산출물: 표준 단어·용어·도메인·코드 4대 사전 · 테이블 정의서 · DDL 스키마 스크립트 · 범정부 메타데이터 연계 등록부

<div class="itpe-flow-map" role="img" aria-label="데이터 표준화 4대 사전 및 DDL 적합성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 비즈니스 용어 수집 및 4대 사전 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>사전화</strong><span>표준단어(약어·금칙어) + 표준도메인(타입·길이) + 표준코드(공통코드) 정의</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 표준용어 조합 및 명명 규칙 적용</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>조합</strong><span>표준단어의 논리적 결합 + 최우측 분류어(예: 고객 + 가입 + 일자) 결합</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 테이블 정의서 매핑 및 DDL 생성</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>설계</strong><span>엔티티/속성 1:1 매핑, 물리 테이블명·컬럼명·PK/FK 및 Nullable 제약 명세</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 표준 준수율 및 DDL 드리프트 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>모든 물리 컬럼이 4대 사전에 등록되어 있으며, CI/CD DDL Linter 검증을 100% 통과했는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (물리 스키마 배포 승인)</strong>
      <span>운영 DB 배포 허용 $\rightarrow$ 범정부 메타데이터 관리시스템 동기화 및 공공데이터 개방</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (비표준 컬럼 / 스키마 왜곡)</strong>
      <span>배포 즉시 차단 $\rightarrow$ 표준 심의 위원회 신규 용어 신청 및 테이블 정의서 수정</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `표준단어(Word)`: 데이터 명칭을 구성하는 최소 의미 단위로, 표준 영문 약어와 금칙어를 엄격히 관리
- `표준용어(Term)`: 하나 이상의 표준단어가 조합되고 최우측에 반드시 '분류어'가 결합된 업무적 속성 명칭
- `표준도메인(Domain)`: 속성이 가질 수 있는 데이터 타입, 허용 길이, 소수점 자릿수, 출력 형식의 묶음 규칙
- `표준코드(Code)`: 도메인 중 선택 가능한 고유 범주값과 명칭의 목록으로, 국가 표준 및 행정표준코드 준수 필수
- `테이블 정의서`: 논리 속성과 물리 컬럼 간 1:1 매핑, 데이터 타입, 제약조건을 명세한 데이터 아키텍처의 공식 기준선(Baseline)
- `공공데이터베이스 표준화 관리지침`: 행정안전부 고시로 공공기관의 행정표준용어, 표준코드 준수 및 메타데이터 등록 의무 규정

</details>

---

## 1교시 예상문제 (10점)

> 데이터 표준화(공공 DB 표준화 지침·테이블 정의서 포함)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

### 1. 데이터 표준화의 정의 및 추진 목적

- **정의**: 조직 내 데이터의 명칭, 정의, 형식, 규칙을 통일하여 동음이의어와 이음동의어를 배제하고 상호운용성을 보증하는 거버넌스 기준선
- **목적**: 데이터 의미 일관성 확보, 시스템 연계 매핑 비용 절감, 행안부 공공 DB 표준화 관리지침 준수

### 2. 데이터 표준 4대 핵심 사전 및 명명 규칙

| 사전 구분 | 핵심 관리 내용 | 실무 예시 |
|---|---|---|
| **표준단어 (Word)** | 데이터 명칭의 최소 의미 단위, 공인 영문 약어 부여 | 고객(CUST), 일자(DT) |
| **표준용어 (Term)** | 단어 조합 + 최우측 필수 분류어(Classifier) 결합 | 고객가입일자 (CUST_JOIN_DT) |
| **표준도메인 (Domain)** | 속성의 데이터 타입, 허용 길이, 포맷 규칙 그룹 | 날짜 (VARCHAR2(8), YYYYMMDD) |
| **표준코드 (Code)** | 도메인 내 허용 가능한 유효 범주값 목록 | 고객상태코드 (01:정상, 02:휴면) |

- **명명 규칙**: `[수식단어] + [핵심단어] + [분류어]` (분류어는 일자, 일시, 코드, 번호, 금액, 여부 등 도메인 결정)

### 3. 기술사적 실무 제언: Schema-as-Code 파이프라인

- 엑셀 기반 수기 관리의 한계를 극복하기 위해, 메타데이터 관리 시스템과 Git 및 CI/CD DDL Linter를 연동하여 비표준 컬럼의 운영 DB 배포를 원천 차단해야 함.
---

## 2~4교시 예상문제 (25점)

> 전사 데이터 거버넌스 및 행정안전부 '공공데이터베이스 표준화 관리지침'에 따른 데이터 표준화의 개념, 4대 핵심 구성요소(단어, 용어, 도메인, 코드), 명명 규칙 및 테이블 정의서 작성 시 표준 매핑 방안을 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **공공데이터베이스 표준화 관리지침** | 행정안전부 고시, 행정표준용어 및 공통코드 의무 준수, 범정부 메타데이터 등록 | Ⅴ 지침 및 규제 |
| **테이블 정의서** | 물리 데이터 모델의 테이블명, 컬럼명, 타입, PK/FK, 표준용어 매핑 정보를 명세한 공식 설계 문서 | Ⅳ 설계 및 산출물 |
| **명명 규칙(Naming Convention)** | 표준단어 조합 원칙, 분류어(Classifier) 필수 부여, 파스칼/스네이크 표기법 | Ⅲ 명명 체계 |

### Ⅰ. 데이터 상호운용성의 주춧돌, 데이터 표준화의 개요

> 데이터 표준화는 전사 데이터의 명칭·정의·형식·코드를 통일해 데이터 해석 왜곡을 방지하는 관리 활동임.

- 정의: 조직 내에서 사용하는 데이터의 명칭, 의미, 도메인, 규칙을 일관되게 정의하고, 이를 정보시스템 설계·구축·운영 및 공공데이터 개방 전반에 강제하는 엔지니어링 활동
- 배경: 부서별 독자적 개발로 인한 이음동의어(Synonym), 동음이의어(Homonym) 만연, 시스템 간 데이터 연계 시 막대한 ETL 매핑 비용 발생 및 통계 왜곡
- 목적: 데이터 명칭과 의미의 일관성(Semantic Consistency) 확보, 데이터 재사용성 증대, 공공 DB 표준화 지침 준수를 통한 범정부 데이터 개방 및 연계성 보장

### Ⅱ. 데이터 표준 4대 핵심 구성요소(사전 체계)

> 단어, 용어, 도메인, 코드가 유기적으로 연결되어 단일한 메타데이터 기준선을 형성함.

<svg viewBox="0 0 520 195" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="데이터 표준 4대 사전 및 물리 모델 매핑 구조" role="img">
  <defs>
    <marker id="std-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#58a6ff"/>
    </marker>
  </defs>
  <!-- Standard Word -->
  <g transform="translate(15, 20)">
    <rect width="145" height="65" rx="5" fill="#21262d" stroke="#58a6ff" stroke-width="1.5"/>
    <text x="72" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#58a6ff" text-anchor="middle">표준단어 (Word)</text>
    <text x="12" y="42" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 최소 의미 단위 (고객, 일자)</text>
    <text x="12" y="56" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e">• 공인 영문 약어: CUST, DT</text>
  </g>

  <!-- Arrow: Word to Term -->
  <path d="M 160 52 L 188 52" stroke="#58a6ff" stroke-width="2" marker-end="url(#std-arrow)"/>
  <text x="174" y="45" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e" text-anchor="middle">조합</text>

  <!-- Standard Term -->
  <g transform="translate(192, 15)">
    <rect width="150" height="75" rx="5" fill="#21262d" stroke="#3fb950" stroke-width="1.5"/>
    <text x="75" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#3fb950" text-anchor="middle">표준용어 (Term)</text>
    <text x="12" y="42" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 단어 결합 + 필수 분류어</text>
    <text x="12" y="56" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 예: 고객가입일자</text>
    <text x="12" y="70" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e">• 컬럼명: CUST_JOIN_DT</text>
  </g>

  <!-- Arrow: Term to Physical -->
  <path d="M 342 52 L 370 52" stroke="#3fb950" stroke-width="2" marker-end="url(#std-arrow)"/>
  <text x="356" y="45" font-family="system-ui, sans-serif" font-size="8" fill="#8b949e" text-anchor="middle">1:1 매핑</text>

  <!-- Physical Model -->
  <g transform="translate(374, 15)">
    <rect width="130" height="75" rx="5" fill="#21262d" stroke="#d29922" stroke-width="1.5"/>
    <text x="65" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#d29922" text-anchor="middle">테이블 정의서</text>
    <text x="10" y="42" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• 물리 컬럼 매핑</text>
    <text x="10" y="56" font-family="system-ui, sans-serif" font-size="8.5" fill="#c9d1d9">• PK/FK 및 제약</text>
    <text x="10" y="70" font-family="system-ui, sans-serif" font-size="8.5" fill="#8b949e">• DDL 자동 생성</text>
  </g>

  <!-- Arrow down from Term to Domain -->
  <path d="M 267 90 L 267 114" stroke="#8b949e" stroke-width="1.5" marker-end="url(#std-arrow)"/>

  <!-- Standard Domain & Code Box -->
  <g transform="translate(100, 120)">
    <rect width="320" height="60" rx="5" fill="rgba(163,113,247,0.08)" stroke="#a371f7" stroke-width="1.5"/>
    <text x="160" y="20" font-family="system-ui, sans-serif" font-size="11" font-weight="bold" fill="#a371f7" text-anchor="middle">표준도메인 (Domain) &amp; 표준코드 (Code)</text>
    <text x="20" y="38" font-family="system-ui, sans-serif" font-size="9" fill="#c9d1d9">• 도메인: 자료형/길이/포맷 규정 (날짜 $\to$ VARCHAR2(8), 금액 $\to$ NUMBER(15,2))</text>
    <text x="20" y="52" font-family="system-ui, sans-serif" font-size="9" fill="#8b949e">• 공통코드: 범주값 통일 (국가 행정표준코드, ISO 코드 우선 준수)</text>
  </g>
</svg>

| 표준 요소 | 개념 및 정의 | 구성 및 관리 규칙 | 실무 작성 예시 |
|---|---|---|---|
| **표준단어 (Word)** | 데이터 명칭을 구성하는 최소 의미 단위 | 1단어 1의미 원칙, 표준 영문 약어 부여, 동의어/유의어/금칙어 사전 관리 | 단어: '고객'(CUST), '일자'(DT) |
| **표준용어 (Term)** | 비즈니스 목적을 나타내는 표준단어들의 조합 | 2개 이상의 단어 조합 시 최우측에 반드시 '분류어' 결합, 완전한 업무 의미 부여 | 용어: '고객가입일자' (CUST_JOIN_DT) |
| **표준도메인 (Domain)**| 속성이 취할 수 있는 값의 형식과 범위 묶음 | 데이터 타입(VARCHAR, NUMBER), 길이, 포맷(YYYY-MM-DD), 허용 범위 규정 | 도메인: '날짜' (VARCHAR2(8), YYYYMMDD) |
| **표준코드 (Code)** | 도메인 내에서 선택 가능한 범주형 코드값 집합 | 코드값, 코드명, 코드설명, 유효기간 관리 (국가 행정표준코드 우선 적용) | 코드: '고객상태코드' (01:정상, 02:휴면) |

### Ⅲ. 데이터 명명 규칙 및 분류어 체계

> 분류어를 쓰는 표준용어 체계에서는 끝 단어가 자료형·도메인 판단을 일관되게 드러내도록 명명 규칙을 검증함.

<svg viewBox="0 0 520 155" class="w-full max-w-[520px] mx-auto block select-none my-4" style="background: var(--sl-color-bg-sidebar, #161b22); border-radius: 8px; border: 1px solid var(--sl-color-hairline, #30363d);" aria-label="표준용어 생성 규칙 및 분류어 결합 메커니즘" role="img">
  <!-- Formula Container -->
  <g transform="translate(15, 15)">
    <rect width="490" height="60" rx="5" fill="#21262d" stroke="#30363d"/>
    <text x="20" y="24" font-family="system-ui, sans-serif" font-size="10.5" font-weight="bold" fill="#58a6ff">표준용어 생성 공식</text>
    <rect x="20" y="32" width="120" height="22" rx="3" fill="#161b22" stroke="#58a6ff"/>
    <text x="80" y="47" font-family="system-ui, sans-serif" font-size="9.5" fill="#c9d1d9" text-anchor="middle">수식단어 [단어 A]</text>
    <text x="148" y="47" font-family="system-ui, sans-serif" font-size="12" fill="#8b949e" text-anchor="middle">+</text>
    <rect x="156" y="32" width="120" height="22" rx="3" fill="#161b22" stroke="#58a6ff"/>
    <text x="216" y="47" font-family="system-ui, sans-serif" font-size="9.5" fill="#c9d1d9" text-anchor="middle">핵심단어 [단어 B]</text>
    <text x="284" y="47" font-family="system-ui, sans-serif" font-size="12" fill="#8b949e" text-anchor="middle">+</text>
    <rect x="292" y="32" width="180" height="22" rx="3" fill="rgba(63,185,80,0.15)" stroke="#3fb950"/>
    <text x="382" y="47" font-family="system-ui, sans-serif" font-size="9.5" font-weight="bold" fill="#3fb950" text-anchor="middle">필수 분류어 (Classifier)</text>
  </g>

  <!-- Example Mapping Box -->
  <g transform="translate(15, 85)">
    <rect width="490" height="55" rx="5" fill="rgba(56,189,248,0.06)" stroke="rgba(56,189,248,0.3)"/>
    <text x="20" y="22" font-family="system-ui, sans-serif" font-size="10" font-weight="bold" fill="#58a6ff">실무 조합 예시</text>
    <text x="20" y="42" font-family="system-ui, sans-serif" font-size="9.5" fill="#c9d1d9">
      "고객(CUST)" + "최종(LAST)" + "접속(CONN)" + <tspan fill="#3fb950" font-weight="bold">"일시(DTM)"</tspan>
      $\rightarrow$ 물리 컬럼명: <tspan fill="#58a6ff" font-weight="bold">CUST_LAST_CONN_DTM</tspan> (VARCHAR2(14))
    </text>
  </g>
</svg>

- **분류어(Classifier)의 역할**: 용어의 물리적 데이터 타입과 도메인을 결정하는 기준 (예: 일자, 일시, 번호, 코드, 명, 금액, 율, 량, 여부, 내용)
- **명명 제한 사항**:
  - 특수문자, 띄어쓰기 금지 (물리명은 언더스코어 `_` 구분)
  - 한글 음절을 억지로 자른 비직관적 약어 생성 금지 (공인 약어 사전 준수)
  - 테이블명 접두사(Prefix)는 업무 영역 식별자로 한정 (예: `TB_COM_` 공통, `TB_ORD_` 주문)

### Ⅳ. 테이블 정의서와 표준 사전 간의 1:1 매핑 구조

> 테이블 정의서와 운영 스키마를 항목별로 대조하여 비표준 명칭·타입 불일치를 찾아냄.

| 테이블 정의서 주요 항목 | 표준 사전 매핑 관계 | 기술사적 설계 점검 기준 |
|---|---|---|
| **테이블 논리명 / 물리명** | 표준 엔티티명 및 명명 규칙 매핑 | 테이블명만 보고도 업무 목적과 소속 도메인 식별 가능 여부 |
| **컬럼 논리명 / 물리명** | **표준용어사전**과 1:1 일치 | 표준단어 조합 규칙 준수 및 비표준 영문 축약 사용 금지 |
| **데이터 타입 및 길이** | **표준도메인사전**과 1:1 일치 | 동일 분류어(예: 금액)에 대해 컬럼마다 타입/길이가 다른 모순 배제 |
| **PK / FK / 제약조건** | 식별자 및 참조 무결성 규칙 | 인조키 남용 방지 및 필수 외래키 참조 무결성 명시 |
| **기본값 (Default Value)** | 비즈니스 업무 규칙 | Null 허용 여부와 결합하여 기본값(`SYSDATE`, `'01'`) 일관성 유지 |

### Ⅴ. 행정안전부 '공공데이터베이스 표준화 관리지침' 주요 준수 의무

> 공공 정보화 사업에서는 행정안전부 고시를 엄격히 준수하여 감리 및 표준화 점검을 통과해야 함.

| 요구 영역 | 세부 지침 내용 | 공공 정보화 사업 적용 방안 |
|---|---|---|
| **행정표준용어 준수** | 범정부 데이터 표준용어(행안부 고시) 우선 사용 의무화 | 신규 사업 시 공통표준용어사전 매핑 후 기관 고유 용어 정의 |
| **행정표준코드 적용** | 법정동코드, 행정기관코드, 성별 등 국가 표준코드 필수 적용 | 사설 코드 생성 금지, 연계 API 기반 실시간 코드 동기화 |
| **도메인 및 데이터 형식** | 날짜(YYYY-MM-DD), 시간(HH:MM:SS), 좌표계 등 공통 형식 준수 | 비정형 표현 배제 및 대국민 공공데이터 개방 호환성 확보 |
| **메타데이터 등록·현행화** | 범정부 메타데이터 관리시스템에 기관 DB 테이블 정의서 및 스키마 등록 | 사업 완료 감리 시 공공데이터 포털 메타 연계 일치율 검증 |

### Ⅵ. 데이터 표준화 문제점·대응책

> 비표준 레거시와의 충돌과 자의적 약어 생성을 메타관리 솔루션 기반 CI/CD 게이트로 방어함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 자의적 DDL·비표준 컬럼 배포 | CI/CD에 DDL 표준 검사 연계 | 비표준 변경 조기 탐지·배포 보류 |
| 무리한 한글 음절 축약으로 가독성 훼손 | 공식 IT 표준 약어(ISO/IEC 및 공공 용어사전) 기반 표준단어 은행 사전 구축 | 소스코드 및 SQL 가독성 극대화 및 유지보수 비용 절감 |
| 레거시 마이그레이션 시 단일 컬럼 복합 속성 혼재 | 데이터 프로파일링 기반 속성 분화 및 원천 정제 선행 | 1원자 1속성 원칙 준수 및 마이그레이션 정합성 확보 |
| 테이블 정의서·운영 스키마 불일치 | 형상관리 기반 Schema-as-Code·정기 대조 | 문서 진부화·영향분석 누락 감소 |

### Ⅶ. 기술사적 제언: 설계도에서 코드로의 자동화 파이프라인 구축

> "데이터 표준화는 관리자의 엑셀 문서 속에 머무는 순간 사장된다. CI/CD 파이프라인과 결합된 살아있는 메타데이터만이 시스템을 지킨다."

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 표준화의 핵심은 이름을 예쁘게 맞추는 것이 아니라, 전사 시스템 간에 '동일한 비즈니스 의미가 동일한 데이터 타입과 검증 규칙으로 구현'되게 보장하는 것이다.
>
> **[나라면 이렇게 쓴다]**
> 엑셀 기반의 수작업 메타 관리를 폐기하고, 메타데이터 관리 시스템과 Git 형상관리, CI/CD 배포 파이프라인을 연동하는 Schema-as-Code 체계를 구축하여 스키마 드리프트(Drift)를 원천 차단하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 데이터 표준화의 성패는 표준 사전의 단어 개수가 아니라 **표준용어와 테이블 정의서, 실제 운영 DDL 간의 100% 추적성(Traceability)**으로 판정
- **대응 방안**: 메타데이터 관리 시스템 $\rightarrow$ 테이블 정의서 자동 생성 $\rightarrow$ Git 기반 DDL 버전 관리 $\rightarrow$ CI/CD 배포 전 표준 Linter 검증 파이프라인 정착
- **검증 체계**: 물리 컬럼 표준 준수율 100%, 테이블 정의서-실제 운영 DB 스키마 일치율 100% 감리 통과
- **기대 효과**: 이음동의어/동음이의어 전면 제거 및 범정부 공공데이터 개방·이기종 연계 시 매핑 비용 제로화 달성

<div class="itpe-flow-map" role="img" aria-label="데이터 표준화 고도화 실행 로드맵">
  <div class="itpe-flow-node">
    <strong>1단계: 현행 한계 인식</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-fail"><strong>문제</strong><span>수작업 엑셀 관리로 인한 문서 진부화 및 운영 DB와 설계서 간 스키마 드리프트 발생</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 아키텍처 개선 방안</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>기술 적용</strong><span>Schema-as-Code 파이프라인 구축 + CI/CD DDL Linter 표준 자동 검사 강제</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: 정량 검증 기준</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>KPI 지표</strong><span>전사 물리 컬럼 표준 준수율 100%, 테이블 정의서-DB 스키마 일치율 100%</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>4단계: 궁극적 실행 효과</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch is-pass"><strong>가치 창출</strong><span>동음이의어/이음동의어 원천 배제 및 범정부 데이터 개방 연계 TCO 절감 달성</span></div>
    </div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 근거**: Q-Net 공식 문제지 제132회 확인 · 제126·131회는 KPC 보조자료이며 공식 원문 미확보
- **공식 근거**: [국가법령정보센터 행정규칙 검색](https://www.law.go.kr/admRulLsInfoP.do), [공공데이터포털](https://www.data.go.kr/)

## 연결 토픽

- [데이터 품질관리](./003_data_quality_management.md) · [데이터 거버넌스](./006_data_governance.md) · [데이터 모델링](./042_data_modeling.md) · [ERD](./028_erd.md)
