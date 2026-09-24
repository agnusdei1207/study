---
sidebar:
  order: 159
  label: "159. 함수적 종속성(Functional Dependency)"
  badge:
    text: "A"
    variant: note
title: "함수적 종속성 (Functional Dependency, FD)"
author: "Antigravity"
date: "2026-09-24T00:00:00+09:00"
tags:
  - "notes-data"
weight: 159
extra:
  model: "GPT-6"
  keyword_grade: "A"
  question_no: "159"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>관계형 데이터 모델</span><span>정규화 이론</span><strong>함수적 종속성(FD)과 암스트롱 공리</strong></div>

## 큰 그림과 30초 인출

```text
[함수적 종속성(FD) 3대 유형 및 정규화 단계별 해소 매핑]

  [1. 완전 함수 종속 (FFD)]           [2. 부분 함수 종속 (PFD)]       [3. 이행적 함수 종속 (TFD)]
   복합키 전체에 종속                 복합키 일부에 종속 (2NF 위배)    A -> B 이고 B -> C (3NF 위배)

     {학번, 과목코드}                    {학번, 과목코드}                  [학번]
      │        │                          │      │                           │
      │        ▼                          │      ▼                           ▼
      └──────► 성적                       └────► [학생이름]                 [학과코드]
     (학번+과목코드 전체가                (오직 '학번'에만 종속되므로        │
      있어야 성적이 결정됨)                복합키 전체에 완전 종속 X)         ▼
     ==> 2NF 달성 상태                    ==> 제2정규화 분해 대상!           [학과이름]
                                                                            ==> 제3정규화 분해 대상!
```

- 본질: **관계형 데이터베이스 릴레이션 내에서 어떤 속성 집합($X$)의 값이 다른 속성 집합($Y$)의 값을 고유하게 결정할 때 성립하는 속성 간의 의미론적 제약조건($X \rightarrow Y$)이자, 데이터 중복과 갱신 이상(Anomaly)을 수학적으로 분해·제거하기 위한 정규화의 핵심 이론적 토대**
- 암기: `결-종` (결정자 X, 종속자 Y) / `완-부-이` (3대 종속성: 완전, 부분, 이행적 함수 종속) / `반-첨-이-분-결-의` (암스트롱 공리: 반사, 첨가, 이행, 분해, 결합, 의사이행)
- 판단축:
  - **완전 함수 종속(FFD)**: 종속자가 복합키의 '모든 속성'에 온전히 종속되는 정상 상태 $\rightarrow$ 2NF 만족.
  - **부분 함수 종속(PFD)**: 종속자가 복합키의 '일부 속성'에만 종속되는 상태 $\rightarrow$ 제2정규화(2NF) 분해 대상.
  - **이행적 함수 종속(TFD)**: $X \rightarrow Y$이고 $Y \rightarrow Z$인 간접 종속 상태 $\rightarrow$ 제3정규화(3NF) 분해 대상.
- 주의: 함수적 종속성은 현재 저장된 인스턴스 데이터의 우연한 일치가 아니라, 비즈니스 도메인 업무 규칙(Business Rules)에 의해 영구적으로 정의되는 불변의 제약조건임
---

## 1교시 예상문제 (10점)

> 함수적 종속성 (Functional Dependency, FD)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

| 항목 | 핵심 서술 내용 |
|:---|:---|
| **정의** | 릴레이션 내에서 속성 집합 $X$의 값이 다른 속성 집합 $Y$의 값을 고유하게 결정하는 의미론적 제약조건 ($X \rightarrow Y$) |
| **3대 종속성 유형** | ① 완전 함수 종속(FFD: 복합키 전체에 종속, 2NF 기준) ② 부분 함수 종속(PFD: 복합키 일부에 종속, 2NF 대상) ③ 이행적 함수 종속(TFD: $X \rightarrow Y \rightarrow Z$, 3NF 대상) |
| **암스트롱 3대 기본 공리** | ① 반사 규칙($Y \subseteq X \implies X \rightarrow Y$) ② 첨가 규칙($X \rightarrow Y \implies XZ \rightarrow YZ$) ③ 이행 규칙($X \rightarrow Y, Y \rightarrow Z \implies X \rightarrow Z$) |
| **확장 3대 규칙** | 분해 규칙($X \rightarrow YZ \implies X \rightarrow Y, X \rightarrow Z$), 결합 규칙, 의사이행 규칙 |
| **실무 제언** | 논리 모델링 시 함수 종속 다이어그램(FDD) 작성을 의무화하여 PFD/TFD를 시각적으로 검증 후 물리 스키마로 이관 |
---

### 핵심 관계

| 종속성 유형 | 학술적 정의 및 조건 | 위배 시 이상현상 | 정규화 조치 |
|:---|:---|:---|:---|
| **완전 함수 종속 (FFD)** | $X \rightarrow Y$에서 $X$의 임의의 진부분집합 $X'$에 대해 $X' \rightarrow Y$가 성립하지 않음 | 정상 (데이터 이상현상 없음) | 제2정규형(2NF) 만족 기준 |
| **부분 함수 종속 (PFD)** | $X \rightarrow Y$에서 $X$의 진부분집합 $X'$에 대해 $X' \rightarrow Y$가 성립함 | 학생 이름 변경 시 수강 과목마다 중복 수정 발생 | **제2정규화 (2NF)**: 복합키 분해 |
| **이행적 함수 종속 (TFD)** | $X \rightarrow Y$이고 $Y \rightarrow Z$일 때 $X \rightarrow Z$가 성립 ($Y$는 비후보키) | 학과명 변경 시 모든 학생 튜플 수정, 학생 없는 학과 등록 불가 | **제3정규화 (3NF)**: $X-Y$, $Y-Z$ 분해 |

---

## 2~4교시 예상문제 (25점)

> 관계 데이터 모델에서 정규화의 기초가 되는 함수적 종속성(Functional Dependency)의 개념과 표기법을 설명하고, 3대 종속성 유형(완전, 부분, 이행적)의 특징 및 정규화 단계와의 연계성, 그리고 함수 종속성을 추론하기 위한 암스트롱의 공리(Armstrong's Axioms)를 설명하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### Ⅰ. 정규화의 수학적 기초인 함수적 종속성(FD) 개요

#### 한줄 요약: 한 속성의 값이 정해지면 다른 속성의 값이 오직 하나로 결정되는 속성 간의 종속 관계

- **등장 배경**:
  - 데이터베이스 스키마 설계 시 속성들이 아무런 규칙 없이 단일 테이블에 뭉쳐 있으면, 튜플 삽입·삭제·수정 시 데이터 불일치(이상현상) 발생
  - 테이블을 어떤 기준으로 쪼개야 중복이 사라지고 무손실 복원이 보장되는가를 판별하기 위한 수학적 기준 마련
- **정의**:
  - 릴레이션 $R$의 속성 부분집합 $X$와 $Y$에 대하여, 임의의 튜플 $t_1, t_2 \in R$이 $t_1[X] = t_2[X]$일 때 항상 $t_1[Y] = t_2[Y]$를 만족하면, "속성 집합 $Y$는 속성 집합 $X$에 함수적으로 종속된다"고 정의함
- **표기법**:
  $$X \rightarrow Y$$
  - $X$: **결정자 (Determinant)** — 다른 속성의 값을 고유하게 결정짓는 속성 집합
  - $Y$: **종속자 (Dependent)** — 결정자에 의해 종속되는 속성 집합

### Ⅱ. 함수적 종속성의 3대 핵심 유형

#### 한줄 요약: 복합키 전체에 걸리는 '완전', 일부에 걸리는 '부분', 징검다리를 건너는 '이행적' 종속성

<div class="itpe-diagram-box">
  <div class="itpe-diagram-header">
    <span class="itpe-tag">아키텍처 다이어그램</span>
    <span class="itpe-title">함수적 종속성 3대 유형(FFD, PFD, TFD) 구조 및 정규화 분해 매핑</span>
  </div>
  <div class="itpe-diagram-body">
    <svg class="itpe-svg" viewBox="0 0 520 280" width="100%" height="280" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arrow-fd" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 8 5 L 0 9 z" fill="var(--color-text, #333)" />
        </marker>
      </defs>
      <!-- 1. 완전 함수 종속 (FFD) -->
      <rect x="15" y="15" width="235" height="120" rx="5" fill="var(--color-bg-secondary, #f0f4f8)" stroke="var(--color-border, #0284c7)" stroke-width="1.5" />
      <text x="132" y="35" font-size="11" font-weight="bold" text-anchor="middle" fill="var(--color-primary, #0284c7)">1. 완전 함수 종속 (FFD)</text>
      <text x="132" y="50" font-size="9" text-anchor="middle" fill="var(--color-text-muted, #555)">복합키 전체 속성에 종속 ┃ 2NF 만족 상태</text>
      <!-- 복합키 박스 -->
      <rect x="35" y="62" width="90" height="25" rx="3" fill="#ffffff" stroke="#0284c7" stroke-width="1" />
      <text x="80" y="78" font-size="10" font-weight="bold" text-anchor="middle" fill="#0369a1">{학번, 과목코드}</text>
      <!-- 화살표 -->
      <path d="M 125 74 L 160 74" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arrow-fd)" />
      <!-- 종속자 -->
      <rect x="165" y="62" width="65" height="25" rx="3" fill="#eff6ff" stroke="#0284c7" stroke-width="1" />
      <text x="197" y="78" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">성적</text>
      <text x="132" y="112" font-size="9" text-anchor="middle" fill="#059669">둘 중 하나라도 빠지면 성적 결정 불가</text>

      <!-- 2. 부분 함수 종속 (PFD) -->
      <rect x="270" y="15" width="235" height="120" rx="5" fill="var(--color-bg-secondary, #f0f4f8)" stroke="var(--color-border, #0284c7)" stroke-width="1.5" />
      <text x="387" y="35" font-size="11" font-weight="bold" text-anchor="middle" fill="#dc2626">2. 부분 함수 종속 (PFD)</text>
      <text x="387" y="50" font-size="9" text-anchor="middle" fill="#dc2626">복합키 일부 속성에만 종속 ┃ 2NF 위배!</text>
      <!-- 복합키 박스 -->
      <rect x="285" y="62" width="95" height="25" rx="3" fill="#ffffff" stroke="#64748b" stroke-width="1" />
      <text x="332" y="78" font-size="10" text-anchor="middle" fill="#1e293b">{학번, 과목코드}</text>
      <!-- 부분 추출 화살표 -->
      <path d="M 310 87 L 310 105 L 390 105" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow-fd)" />
      <text x="315" y="100" font-size="8" fill="#dc2626">학번만으로 결정</text>
      <!-- 종속자 -->
      <rect x="395" y="93" width="75" height="25" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1" />
      <text x="432" y="109" font-size="10" font-weight="bold" text-anchor="middle" fill="#991b1b">학생이름</text>
      <text x="387" y="125" font-size="8" text-anchor="middle" fill="#b91c1c">==► 제2정규화 분해 대상</text>

      <!-- 3. 이행적 함수 종속 (TFD) -->
      <rect x="15" y="145" width="490" height="120" rx="5" fill="var(--color-bg-secondary, #f0f4f8)" stroke="var(--color-border, #0284c7)" stroke-width="1.5" />
      <text x="260" y="165" font-size="11" font-weight="bold" text-anchor="middle" fill="#d97706">3. 이행적 함수 종속 (TFD: Transitive Functional Dependency)</text>
      <text x="260" y="180" font-size="9" text-anchor="middle" fill="#b45309">X ──► Y 이고 Y ──► Z (Y는 비후보키) 일 때 X ──► Z 성립 ┃ 3NF 위배!</text>

      <!-- X -> Y -> Z 시퀀스 -->
      <rect x="40" y="195" width="90" height="30" rx="3" fill="#ffffff" stroke="#2563eb" stroke-width="1.5" />
      <text x="85" y="214" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e40af">X (학번)</text>

      <path d="M 130 210 L 175 210" stroke="#2563eb" stroke-width="1.8" marker-end="url(#arrow-fd)" />
      <text x="152" y="204" font-size="8" text-anchor="middle" fill="#2563eb">직접 결정</text>

      <rect x="180" y="195" width="110" height="30" rx="3" fill="#ffffff" stroke="#f59e0b" stroke-width="1.5" />
      <text x="235" y="214" font-size="10" font-weight="bold" text-anchor="middle" fill="#b45309">Y (학과코드)</text>

      <path d="M 290 210 L 335 210" stroke="#f59e0b" stroke-width="1.8" marker-end="url(#arrow-fd)" />
      <text x="312" y="204" font-size="8" text-anchor="middle" fill="#b45309">직접 결정</text>

      <rect x="340" y="195" width="110" height="30" rx="3" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
      <text x="395" y="214" font-size="10" font-weight="bold" text-anchor="middle" fill="#991b1b">Z (학과이름)</text>

      <!-- 간접 이행 화살표 -->
      <path d="M 85 225 L 85 250 L 395 250 L 395 225" fill="none" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="4" marker-end="url(#arrow-fd)" />
      <text x="240" y="246" font-size="9" font-weight="bold" text-anchor="middle" fill="#dc2626">이행 종속 (X ──► Z) ==> 제3정규화 분해 대상!</text>
    </svg>
  </div>
  <div class="itpe-diagram-footer">
    2NF는 복합키의 부분 함수 종속(PFD)을 제거하고, 3NF는 비주요 속성 간의 이행적 함수 종속(TFD)을 분해함
  </div>
</div>

| 종속성 유형 | 학술적 정의 및 조건 | 위배 시 이상현상 | 정규화 조치 |
|:---|:---|:---|:---|
| **완전 함수 종속 (FFD)** | $X \rightarrow Y$에서 $X$의 임의의 진부분집합 $X'$에 대해 $X' \rightarrow Y$가 성립하지 않음 | 정상 (데이터 이상현상 없음) | 제2정규형(2NF) 만족 기준 |
| **부분 함수 종속 (PFD)** | $X \rightarrow Y$에서 $X$의 진부분집합 $X'$에 대해 $X' \rightarrow Y$가 성립함 | 학생 이름 변경 시 수강 과목마다 중복 수정 발생 | **제2정규화 (2NF)**: 복합키 분해 |
| **이행적 함수 종속 (TFD)** | $X \rightarrow Y$이고 $Y \rightarrow Z$일 때 $X \rightarrow Z$가 성립 ($Y$는 비후보키) | 학과명 변경 시 모든 학생 튜플 수정, 학생 없는 학과 등록 불가 | **제3정규화 (3NF)**: $X-Y$, $Y-Z$ 분해 |

### Ⅲ. 암스트롱의 공리 (Armstrong's Axioms)

#### 한줄 요약: 주어진 함수 종속성 집합으로부터 새로운 모든 참인 종속성을 논리적으로 유도하는 6대 공리

```text
[암스트롱 공리의 3대 기본 규칙 및 3대 확장 규칙]

  [기본 3대 규칙 (Sound & Complete)]
  1. 반사 규칙 (Reflexivity)   : Y ⊆ X 이면 X ──► Y
  2. 첨가 규칙 (Augmentation)  : X ──► Y 이면 XZ ──► YZ
  3. 이행 규칙 (Transitivity)  : X ──► Y 이고 Y ──► Z 이면 X ──► Z
            │
            ▼ 기본 규칙으로부터 수학적으로 유도됨
  [확장 3대 규칙]
  4. 분해 규칙 (Decomposition) : X ──► YZ 이면 X ──► Y 이고 X ──► Z
  5. 결합 규칙 (Union)         : X ──► Y 이고 X ──► Z 이면 X ──► YZ
  6. 의사이행 (Pseudo-transitivity) : X ──► Y 이고 WY ──► Z 이면 WX ──► Z
```

### 1. 기본 3대 규칙 (기초 공리계)
- **건전성(Soundness)**: 공리를 통해 유도된 모든 종속성은 참임
- **완전성(Completeness)**: 주어진 집합 $F$로부터 논리적으로 도출 가능한 모든 참인 종속성을 이 3대 규칙만으로 남김없이 유도 가능함

### 2. 폐포 (Closure, $X^+$)
- 속성 집합 $X$에 의해 결정될 수 있는 모든 속성들의 집합을 $X$의 폐포($X^+$)라 함
- $X^+ = R$ 전체 속성 집합이면, $X$는 해당 릴레이션의 **슈퍼키(Super Key)**임

### Ⅳ. 함수 종속 다이어그램(FDD) 작성 및 정규화 절차

#### 한줄 요약: 속성 간 결정 화살표를 시각화하여 비정규형에서 BCNF까지 단계별 무손실 분해 진행

```text
[함수 종속 다이어그램 기반 정규화 4단계 흐름]

  [1단계: FDD 작성] ──► 엔터티 내 모든 속성 간 결정자-종속자 화살표 도식화
           │
           ▼
  [2단계: 2NF 분해] ──► 복합 기본키의 일부에서 뻗어나가는 PFD 화살표 절단
           │            - R1(학번, 과목, 성적), R2(학번, 이름) 분해
           ▼
  [3단계: 3NF 분해] ──► 기본키가 아닌 일반 속성에서 뻗어나가는 TFD 화살표 절단
           │            - R1(학번, 학과코드), R2(학과코드, 학과명) 분해
           ▼
  [4단계: BCNF 분해] ──► 후보키가 아닌 결정자(화살표 출발점)를 독립 릴레이션으로 분해
```

### Ⅴ. 실무 아키텍처 장애 및 설계 지침

#### 한줄 요약: 데이터 모델링 시 FDD 검증 누락으로 인한 대규모 갱신 이상과 성능 저하 방지

- **이행적 종속 방치로 인한 연쇄 락 장애**:
  - 주문 테이블에 `(주문번호, 고객ID, 배송지주소, 배송지우편번호)`를 한데 모아둠으로써, 우편번호 체계 개편 시 수천만 건의 주문 레코드를 갱신하느라 DB 전체 커넥션 고갈
  - **대응**: 고객 주소 및 우편번호는 별도의 `CUSTOMER_ADDRESS` 테이블로 3NF 분해하고 주문에는 `배송지_스냅샷_ID`만 보관
- **함수 종속성 보존 손실 주의**:
  - BCNF 분해 시 기존 복합키에 걸려 있던 업무 규칙이 분실되지 않도록 외래키 및 체크 제약조건을 신중히 설계

### Ⅵ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 함수적 종속성(FD)은 관계형 데이터베이스 정규화 이론의 '수학적 뼈대'이다. 많은 수험생들이 1NF~BCNF의 정규화 단계를 단순히 "도-부-이-결" 두문자로 암기하지만, 채점관이 진짜 보고 싶어 하는 것은 "그 분해의 학술적 근거가 바로 암스트롱의 공리와 함수 종속성 유형(PFD, TFD)"이라는 점이다. 답안을 작성할 때 FFD, PFD, TFD의 세 가지 종속성을 명확한 수식과 FDD(함수종속 다이어그램)로 시각화하고, 암스트롱 공리의 건전성·완전성 개념을 서술한 뒤, 실무에서 FDD를 활용하여 갱신 이상을 사전에 원천 차단하는 데이터 모델러의 실무 전략을 제언해야 최상위 득점이 보장된다.

> **[나라면 이렇게 쓴다]**
> 1교시형이라면 함수종속 정의 수식과 3대 종속성(FFD, PFD, TFD) 다이어그램, 2NF/3NF 정규화 매핑 표, 암스트롱 6대 공리를 정갈하게 구조화하겠다. 2교시형이라면 복합 엔터티의 이상현상 시나리오를 제시하고, 암스트롱 공리를 바탕으로 속성 폐포($X^+$)를 계산하여 후보키를 찾는 수학적 절차를 보인 후, 엔터프라이즈 논리 모델링 단계에서 FDD를 산출물로 의무화하는 거버넌스 체계를 제언하겠다.

### 실전 답안용 기술사적 제언

- **판정**: 논리 데이터 모델링 시 함수적 종속성 분석(FDD)을 생략한 채 감에 의존해 테이블을 설계하면, 운영 단계에서 부분/이행 종속성에 의한 대규모 갱신 이상(Anomaly)이 발생함.
- **대응**: 복합키를 가진 핵심 엔터티는 함수 종속 다이어그램(FDD)을 의무 작성하여 PFD를 분해(2NF)하고, 비주요 속성 간의 TFD를 격리(3NF)하는 정규화 프로세스를 표준화함.
- **검증**: 속성 폐포($X^+$) 계산 알고리즘을 적용하여 후보키 누락 여부를 검증하고, 체이스(Chase) 알고리즘을 통해 릴레이션 무손실 분해를 수학적으로 입증함.
- **효과**: 데이터 중복 최소화를 통한 스토리지 40% 절감 및 데이터 갱신 시 모순 발생률 0% 달성.

<div class="itpe-flow-map">
  <div class="itpe-flow-step">
    <span class="step-num">1. 현행 한계</span>
    <span class="step-title">FDD 생략 & 이상현상</span>
    <span class="step-desc">함수 종속성 미식별로 단일 테이블 내 PFD/TFD 방치 및 갱신·삭제 이상 발생</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">2. 개선 방안</span>
    <span class="step-title">FDD 도출 및 단계별 정규화</span>
    <span class="step-desc">속성 간 결정자-종속자 화살표를 도식화하여 2NF(PFD 제거) 및 3NF(TFD 제거) 무손실 분해</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">3. 검증 기준</span>
    <span class="step-title">암스트롱 공리 & 폐포 검증</span>
    <span class="step-desc">속성 폐포(X+) 계산으로 슈퍼키/후보키를 판별하고 Chase 기법 무손실 조인 검증</span>
  </div>
  <div class="itpe-flow-arrow">▶</div>
  <div class="itpe-flow-step">
    <span class="step-num">4. 실행 효과</span>
    <span class="step-title">수학적 무결성 완성</span>
    <span class="step-desc">이상현상 원천 차단 및 비즈니스 룰을 100% 반영한 고신뢰 관계형 스키마 구축</span>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 이력**:
  - 제84회 정보관리 1교시: 관계 데이터 모델에서 함수적 종속성(FD)의 개념, 유형(완전, 부분, 이행) 및 암스트롱의 공리
  - 제114회 컴퓨터시스템응용 1교시: 함수적 종속성과 제2정규형, 제3정규형의 관계
- **검증 출처**:
  - W.W. Armstrong, "Dependency Structures of Data Base Relationships", IFIP Congress, 1974
  - Abraham Silberschatz et al., "Database System Concepts 7th Edition", Chapter 14 Relational Database Design
  - C.J. Date, "An Introduction to Database Systems 8th Edition", Functional Dependencies
---

## 연결 토픽

- 상위 토픽: [03-024 정규화 종합](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/024_normalization_overview.md)
- 선수 토픽: [03-157 키(Key)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/157_key.md)
- 후속 토픽: [03-028 제2정규형(2NF)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/028_2nf.md), [03-029 제3정규형(3NF)](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/029_3nf.md), [03-153 BCNF](file:///C:/workspace/study/src/content/docs/notes/itpe/03-data/153_bcnf.md)
