---
sidebar:
  order: 50
  label: "050. 확장성 해싱 (Extendible Hashing)"
  badge:
    text: "A"
    variant: note
title: "확장성 해싱 (Extendible Hashing) 및 동적 해싱 메커니즘"
author: "Antigravity"
date: "2026-09-20T17:35:00+09:00"
tags:
  - "notes-data"
weight: 50
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
  question_no: "050"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>데이터베이스</span><span>물리적 데이터베이스 설계·튜닝</span><strong>확장성 해싱 (Extendible Hashing)</strong></div>

## 큰 그림과 30초 인출

<div class="itpe-diagram-box" role="img" aria-label="확장성 해싱 디렉터리 및 버킷 오버플로우 분할 구조도">
<svg viewBox="0 0 520 230" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-eh" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
    <filter id="shadow-eh" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-color="rgba(0,0,0,0.1)"/>
    </filter>
  </defs>

  <!-- 디렉터리 테이블 -->
  <rect x="25" y="15" width="120" height="155" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" filter="url(#shadow-eh)"/>
  <rect x="25" y="15" width="120" height="28" rx="6" fill="rgba(37, 99, 235, 0.1)"/>
  <text x="85" y="33" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">글로벌 깊이 d=2</text>

  <rect x="35" y="50" width="100" height="24" rx="3" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="50" y="66" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)">00</text>

  <rect x="35" y="78" width="100" height="24" rx="3" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="50" y="94" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)">01</text>

  <rect x="35" y="106" width="100" height="24" rx="3" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="50" y="122" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)">10</text>

  <rect x="35" y="134" width="100" height="24" rx="3" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #cbd5e1)" stroke-width="1"/>
  <text x="50" y="150" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-foreground, #0f172a)">11</text>

  <!-- 포인터 선 -->
  <path d="M 135 62 L 230 62" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-eh)"/>
  <path d="M 135 90 L 230 115" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-eh)"/>
  <path d="M 135 118 L 230 62" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-eh)"/>
  <path d="M 135 146 L 230 125" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-eh)"/>

  <!-- 버킷 A (d'=2) -->
  <rect x="235" y="40" width="145" height="44" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5"/>
  <text x="245" y="56" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)">버킷 A (로컬 d' = 2)</text>
  <text x="245" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-accent, #2563eb)">레코드: [0010, 0011]</text>

  <!-- 버킷 B (d'=1) -->
  <rect x="235" y="105" width="145" height="44" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="#10b981" stroke-width="1.5"/>
  <text x="245" y="121" font-family="system-ui, -apple-system, sans-serif" font-size="9.5" font-weight="700" fill="#10b981">버킷 B (로컬 d' = 1)</text>
  <text x="245" y="137" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)">레코드: [0101, 1100] (공유)</text>

  <!-- 우측 2대 시나리오 카드 -->
  <rect x="395" y="15" width="115" height="74" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="#10b981" stroke-width="1"/>
  <text x="402" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="#10b981">[시나리오 1: d' &lt; d]</text>
  <text x="402" y="46" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-foreground, #0f172a)">버킷 B 넘침</text>
  <text x="402" y="59" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)">디렉터리 확장 없이</text>
  <text x="402" y="72" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)">해당 버킷만 2개 분할</text>

  <rect x="395" y="96" width="115" height="74" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="#ef4444" stroke-width="1"/>
  <text x="402" y="113" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="#ef4444">[시나리오 2: d' = d]</text>
  <text x="402" y="127" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-foreground, #0f172a)">버킷 A 넘침</text>
  <text x="402" y="140" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#ef4444">디렉터리 2배 팽창!</text>
  <text x="402" y="153" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)">d&larr;3 후 버킷 분할</text>

  <!-- 하단 트레이드오프 바 -->
  <rect x="15" y="185" width="490" height="34" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="260" y="200" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">핵심 가치: 전체 재해싱(Full Rehashing) 없는 O(1) 탐색 보장 (RAM 상주 시 1회 디스크 I/O)</text>
  <text x="260" y="213" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">위험 요인: 해시 충돌 편향 시 디렉터리 2^d 지수 폭증(Directory Explosion)</text>
</svg>
</div>

- 본질: **데이터 증가 시 전체 파일의 재해싱(Rehashing) 없이, 해시값의 비트 접두사를 가리키는 디렉터리(Directory)를 두고 오버플로우가 발생한 특정 버킷(Bucket)만 국소적으로 분할하는 동적 해싱(Dynamic Hashing) 기법**
- 암기: `디-버-글-로` (디렉터리, 버킷, 글로벌 깊이, 로컬 깊이) / `국-이-모-균` (국소 분할, 최대 2회 디스크 I/O, 모조키 비트열, 균일한 $O(1)$ 탐색)
- 판단축:
  - **$d' < d$ (로컬 깊이 < 글로벌 깊이)**: 디렉터리는 가만히 두고 넘친 버킷만 분할, 포인터만 재연결 (비용 극소)
  - **$d' = d$ (로컬 깊이 = 글로벌 깊이)**: 디렉터리 엔트리를 2배($2^{d+1}$)로 확장한 후 넘친 버킷 분할 (디렉터리 팽창 비용 발생)
- 주의: 디렉터리 크기가 $2^d$로 지수적으로 증가하므로, 특정 버킷에만 동일 비트 해시가 몰릴 경우 디렉터리 폭증(Directory Explosion) 및 메모리 고갈 위험이 존재함

## 예상문제

> 대용량 데이터베이스의 인덱싱 기법 중 정적 해싱의 한계와 이를 극복하기 위한 확장성 해싱(Extendible Hashing)의 개념, 구성요소, 동작 메커니즘을 설명하고, 버킷 오버플로우 발생 시의 2가지 분할 시나리오 및 선형 해싱(Linear Hashing)과의 차이점을 비교하시오. (25점)

## Ⅰ. 정적 해싱의 한계를 극복하는 확장성 해싱(Extendible Hashing) 개요

- **정적 해싱(Static Hashing)의 구조적 한계**:
  - 고정된 수의 버킷을 사용하므로 데이터가 증가하면 오버플로우 체인(Overflow Chain)이 길어져 탐색 성능이 $O(N)$으로 급격히 퇴화함
  - 이를 해결하기 위해 버킷 수를 늘리려면 전체 테이블을 다시 해싱(Full Rehashing)해야 하므로 대규모 서비스 중단 및 막대한 디스크 I/O 부하가 발생함
- **확장성 해싱의 정의**:
  - 검색 키를 해시 함수에 통과시켜 얻은 이진 비트열(모조키)의 접두사(Prefix)를 인덱스로 사용하는 **디렉터리(Directory)**와 실제 데이터가 저장되는 **버킷(Bucket)**을 분리 운용하는 동적 해싱 기법
  - 버킷이 가득 찼을 때 전체가 아닌 **해당 버킷만 독립적으로 분할(Local Split)**하고, 필요 시에만 디렉터리를 2배로 확장하여 항상 고른 $O(1)$의 탐색 성능을 보장함

#### 한줄 요약

- 고정 버킷 정적 해싱의 전수 재해싱 병목을 해결하고 모조키 비트 접두사와 디렉터리를 통해 버킷을 국소 분할하는 동적 해싱 기법임

## Ⅱ. 확장성 해싱의 핵심 구조 및 구성 요소

<div class="itpe-diagram-box" role="img" aria-label="확장성 해싱 논리 물리 계층 구성도">
<svg viewBox="0 0 520 180" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <marker id="arrow-ehcomp" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--sl-color-accent, #2563eb)"/>
    </marker>
  </defs>

  <!-- 검색 키 -->
  <rect x="15" y="30" width="90" height="35" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="60" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">검색 키 (K)</text>

  <path d="M 105 47 L 130 47" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-ehcomp)"/>

  <!-- 해시 함수 -->
  <rect x="130" y="30" width="100" height="35" rx="5" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="180" y="52" font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">해시 함수 h(K)</text>

  <path d="M 230 47 L 255 47" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-ehcomp)"/>

  <!-- 모조키 비트열 -->
  <rect x="255" y="30" width="130" height="35" rx="5" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1"/>
  <text x="320" y="46" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">모조키 (Pseudo Key)</text>
  <text x="320" y="58" font-family="system-ui, -apple-system, sans-serif" font-size="8.5" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">비트열: 1011001...</text>

  <!-- 상위 d 비트 추출 -->
  <path d="M 320 65 L 320 90" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-ehcomp)"/>
  <text x="340" y="80" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-accent, #2563eb)">상위 d비트</text>

  <!-- 디렉터리 -->
  <rect x="15" y="100" width="220" height="60" rx="6" fill="var(--sl-color-bg, #ffffff)" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5"/>
  <text x="125" y="118" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-accent, #2563eb)" text-anchor="middle">디렉터리 (Directory, RAM 상주)</text>
  <text x="125" y="134" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">글로벌 깊이 d (크기: 2^d 엔트리 배열)</text>
  <text x="125" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">접두사 비트 패턴으로 버킷 물리 포인터 매핑</text>

  <path d="M 235 130 L 275 130" stroke="var(--sl-color-accent, #2563eb)" stroke-width="1.5" marker-end="url(#arrow-ehcomp)"/>

  <!-- 데이터 버킷 -->
  <rect x="275" y="100" width="230" height="60" rx="6" fill="var(--sl-color-gray-6, #f8fafc)" stroke="var(--sl-color-gray-4, #94a3b8)" stroke-width="1.5"/>
  <text x="390" y="118" font-family="system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="700" fill="var(--sl-color-foreground, #0f172a)" text-anchor="middle">데이터 버킷 (Data Buckets, Disk)</text>
  <text x="390" y="134" font-family="system-ui, -apple-system, sans-serif" font-size="9" fill="#10b981" text-anchor="middle">로컬 깊이 d' (d' &le; d, 공유 비트 수)</text>
  <text x="390" y="148" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="var(--sl-color-gray-3, #64748b)" text-anchor="middle">고정 슬롯 B개 보관 / 버킷당 포인터 수: 2^(d - d')</text>
</svg>
</div>

### 1. 주요 구성 요소 상세

| 구성 요소 | 역할 및 핵심 특징 | 비고 / 수식 |
|:---|:---|:---|
| **모조키 (Pseudo Key)** | 원본 키를 해시 함수에 입력하여 생성한 고정 길이 이진 비트열 | $h(K) \in \{0, 1\}^*$ |
| **디렉터리 (Directory)** | 모조키의 접두사 비트 패턴을 인덱스로 하여 각 버킷의 물리 주소를 가리키는 포인터 배열 | 주기억장치(RAM)에 상주 권장 |
| **글로벌 깊이 (Global Depth, $d$)** | 디렉터리에서 버킷을 구분하기 위해 현재 사용 중인 유효 접두사 비트 수 | 디렉터리 엔트리 수 = $2^d$ |
| **버킷 (Bucket)** | 실제 데이터 레코드가 저장되는 고정 크기의 디스크 블록 (또는 메모리 페이지) | 용량 $B$ (레코드 수) |
| **로컬 깊이 (Local Depth, $d'$)** | 해당 버킷에 속한 모든 레코드의 모조키가 공통으로 공유하는 접두사 비트 수 | 항상 $d' \le d$ 성립 |

### 2. 깊이(Depth) 간의 수학적 상관관계

- **버킷을 가리키는 디렉터리 포인터 수**: $2^{d - d'}$개
  - 예: $d = 3$이고 특정 버킷의 $d' = 1$이면, 디렉터리 내 $2^{3-1} = 4$개의 엔트리가 해당 버킷 하나를 동시에 가리킴
- **동일 깊이($d' = d$)**: 디렉터리의 정확히 1개 엔트리가 해당 버킷을 일대일로 가리킴

#### 한줄 요약

- 글로벌 깊이 $d$의 디렉터리 엔트리 $2^d$개가 로컬 깊이 $d'$의 버킷들을 가리키며, 버킷당 포인터 수는 $2^{d-d'}$개임

## Ⅲ. 확장성 해싱 동작 메커니즘 및 2대 분할 시나리오

### 1. 데이터 탐색(Search) 및 삽입(Insert) 기본 절차

1. **해시 비트 추출**: 검색 키 $K$에 대해 $h(K)$를 계산하고 상위 $d$개 비트를 추출함
2. **디렉터리 조회**: 해당 $d$개 비트를 정수로 환산하여 디렉터리의 인덱스로 접근, 연결된 버킷 포인터 획득
3. **버킷 읽기**: 버킷 포인터를 통해 실제 데이터 블록을 읽고 레코드 인출 (**디렉터리가 RAM에 있으면 단 1회의 디스크 I/O**)
4. **삽입 시 여유 공간 검사**: 버킷에 빈 슬롯이 있으면 삽입 완료. 슬롯이 꽉 찼다면 **오버플로우 분할 프로토콜** 진입

### 2. 버킷 오버플로우 발생 시 2대 분할 시나리오

| 구분 | 시나리오 1: 로컬 깊이 &lt; 글로벌 깊이 ($d' < d$) | 시나리오 2: 로컬 깊이 = 글로벌 깊이 ($d' = d$) |
|---|---|---|
| **발생 상황** | 디렉터리의 복수 엔트리가 해당 버킷을 공유 중 | 디렉터리의 단 1개 엔트리만 해당 버킷을 매핑 중 |
| **디렉터리 확장 여부** | **디렉터리 확장 없음** (크기 유지) | **디렉터리 2배 확장 필수** ($d \leftarrow d + 1$, 엔트리 $2^{d+1}$) |
| **버킷 분할 절차** | 1. 신규 버킷 1개 할당<br>2. 넘친 버킷과 신규 버킷의 로컬 깊이 $d' \leftarrow d' + 1$<br>3. $(d'+1)$번째 비트(0/1) 기준으로 레코드 재분배<br>4. 디렉터리 포인터 재배정 | 1. 글로벌 깊이 $d \leftarrow d + 1$ 증가 및 디렉터리 2배 복제<br>2. 기존 엔트리 $i$를 $i$와 $i + 2^d$에 복사<br>3. $d' < d_{new}$ 상태가 되었으므로 시나리오 1 절차 수행 |
| **수반 비용** | 디스크 블록 1개 할당 및 재기록 (매우 경량) | 디렉터리 복제 메모리 비용 + 버킷 분할 I/O |

#### 한줄 요약

- $d' < d$이면 디렉터리 확장 없이 버킷만 쪼개고, $d' = d$이면 디렉터리를 2배로 늘린 후 버킷을 분할함

## Ⅳ. 확장성 해싱 vs 선형 해싱 (Linear Hashing) 상세 비교

| 비교 항목 | 확장성 해싱 (Extendible Hashing) | 선형 해싱 (Linear Hashing) |
|:---|:---|:---|
| **디렉터리 존재 유무** | **필수** (글로벌 깊이 기반 포인터 배열 필요) | **불필요** (디렉터리 없이 수식으로 버킷 번호 산출) |
| **버킷 분할 대상** | **오버플로우가 발생한 해당 버킷만 분할** | 오버플로우 발생 위치와 무관하게 **분할 포인터($P$)가 가리키는 버킷 분할** |
| **공간 확장 형태** | 디렉터리가 $2^d$로 **지수적(Exponential) 2배 도약** | 버킷이 라운드 로빈 방식으로 **1개씩 선형(Linear) 증가** |
| **임시 체인 발생** | 동일 해시값 과밀 시 외에는 오버플로우 체인 없음 | 분할 포인터가 도달할 때까지 임시 오버플로우 체인 연결 불가피 |
| **탐색 디스크 I/O** | 디렉터리 RAM 상주 시 **최대 1~2회 디스크 I/O** 보장 | 오버플로우 체인이 길어질 경우 일시적으로 I/O 횟수 증가 |
| **저장 효율성** | 디렉터리 메모리 오버헤드 존재, 버킷 사용률 약 69% | 디렉터리가 없어 메모리 효율 우수, 버킷 사용률 약 60~70% |

#### 한줄 요약

- 확장성 해싱은 디렉터리를 써서 넘친 버킷만 즉시 쪼개고, 선형 해싱은 디렉터리 없이 포인터 순서대로 차례차례 쪼갬

## Ⅴ. B+Tree 인덱스 vs 확장성 해싱 아키텍처 비교

| 비교 항목 | 확장성 해싱 (Extendible Hashing) | B+Tree 인덱스 (B+Tree Index) |
|:---|:---|:---|
| **기본 시간 복잡도** | **$O(1)$ (상수 시간)** | **$O(\log N)$ (트리 높이 비례)** |
| **점 검색 (Point Query)** | 극도로 빠름 (단 1~2회 블록 접근) | 우수하나 루트-브랜치-리프 수직 탐색 필요 |
| **범위 검색 (Range Scan)** | **불가능** (해시 순서는 키 순서와 완전 무관) | **최적** (리프 블록 간 양방향 링크드 리스트 순회) |
| **정렬 결과 반환** | 불가 (별도 정렬 연산 필요) | 기 정렬 상태이므로 ORDER BY 비용 제로 |
| **동적 확장 메커니즘** | 디렉터리 2배 확장 및 버킷 국소 분할 | 노드 분할(Node Split) 및 트리 높이 증가 |
| **주요 활용 분야** | 세션 스토어, 키-값 저장소(NoSQL), 심볼 테이블 | RDBMS 기본 인덱스, 파일 시스템 색인 |

#### 한줄 요약

- 단건 점 검색($O(1)$)에는 확장성 해싱이 탁월하지만, 범위 검색과 정렬이 필요한 일반 업무에는 B+Tree가 필수적임

## Ⅵ. 실무 적용 시 문제점, 장애 패턴 및 대응 전략

| 문제 상황 | 근본 원인 | 실무 엔지니어링 대책 | 개선 효과 |
|---|---|---|---|
| **디렉터리 폭증 (Directory Explosion)** | 해시 비트 편향 또는 동일 키 대량 인입 시 연속 $d'=d$ 분할 트리거 | 비트 분포가 극도로 균일한 고성능 해시(**MurmurHash3, xxHash**) 적용 | 디렉터리 지수 팽창 방지 |
| **동시성 락 병목 발생** | 디렉터리 2배 확장 시 디렉터리 전체에 배타적 락(X-Lock) 설정 | **최대 글로벌 깊이 상한($d_{max}$)** 설정 후 초과 시 임시 오버플로우 체인 비동기 소화 | 읽기/쓰기 중단 시간 제거 |
| **메모리 고갈 (OOM)** | 버킷 크기가 너무 작아(2~4개) 빈번한 분할로 디렉터리 크기 급증 | OS 페이지 크기(4KB~8KB)에 맞추어 **버킷 슬롯 수 수십~수백 개로 튜닝** | 디렉터리 메모리 점유율 80% 절감 |
| **디렉터리 디스크 스왑 지연** | 디렉터리가 RAM 한계를 초과하여 디스크로 스왑 아웃 | 디렉터리 인메모리 피닝(Pinning) 및 레디스 등 외부 캐시 분리 | $O(1)$ 초저지연 탐색 보증 |

#### 한줄 요약

- MurmurHash3 적용, 버킷 크기 OS 페이지 맞춤, $d_{max}$ 상한 설정이 디렉터리 폭증을 막는 3대 엔지니어링 수칙임

## Ⅶ. 기술사적 제언

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 확장성 해싱의 본질은 "해시 검색의 $O(1)$ 신속성을 유지하면서도 전수 재해싱의 대재앙을 피하는 국소 분할의 지혜"에 있다. 하지만 실무에서 디렉터리가 주기억장치에 100% 상주하지 못하고 디스크로 밀려나는 순간, 디렉터리 I/O 1회 + 버킷 I/O 1회로 총 2회 디스크 I/O가 발생하여 B+Tree 대비 비교우위가 급격히 사라진다. 엔지니어의 핵심 판단 기준은 (1) 디렉터리 메모리 상주성 보장, (2) MurmurHash3를 통한 비트 편향 제거, (3) 범위 검색 여부에 따른 B+Tree와의 엄격한 역할 분담에 있다.

> **[나라면 이렇게 쓴다]**
> 25점 답안 4단락 차별화로 "하이브리드 인덱싱 티어링(Hybrid Indexing Tiering) 아키텍처"를 제시하겠다. 사용자 세션, OAuth 토큰, URL 단축키 등 순수 단건 Point Query(95% 이상) 영역에는 확장성 해싱 기반의 In-Memory NoSQL(Redis/Memcached)을 전진 배치하고, 범위 검색과 복합 조건이 필수적인 주문·결제 도메인은 B+Tree 클러스터드 인덱스로 이원화하는 계층형 데이터 파이프라인 설계를 제언한다.

### 실전 답안용 기술사적 제언

- **[정적 해싱 재해싱 병목과 디렉터리 지수 팽창 한계]**: 데이터 폭증 시 전수 재해싱 I/O 마비 및 해시 편향으로 인한 $2^d$ 디렉터리 메모리 고갈 위험
- **[실무 최적화 방안]**: MurmurHash3/xxHash 기반 비트 균등 분산, OS 페이지(4KB~8KB) 단위 버킷 용량 최적화, 글로벌 깊이 상한($d_{max}$) 설정
- **[워크로드별 인덱스 선별 적용]**: 범위 검색과 정렬이 필요한 관계형 업무는 B+Tree를 적용하고, 초고속 단건 점 검색 중심의 세션/토큰 계층에 확장성 해싱을 집중 배치

<div class="itpe-flow-map" role="group" aria-label="확장성 해싱 한계 극복 및 최적화 4단계 흐름">
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">1</div>
    <div class="itpe-flow-step__title">현행 한계</div>
    <div class="itpe-flow-step__desc">정적 해싱 전수 재해싱 I/O 병목 및 비트 편향 시 디렉터리 폭증 발생</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">2</div>
    <div class="itpe-flow-step__title">개선 방안</div>
    <div class="itpe-flow-step__desc">Extendible Hashing 국소 분할 + MurmurHash3 및 d_max 상한선 제어</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">3</div>
    <div class="itpe-flow-step__title">검증 기준</div>
    <div class="itpe-flow-step__desc">디스크 I/O &le; 1~2회, 버킷 사용률 &gt; 68%, 디렉터리 메모리 &lt; 50MB 유지</div>
  </div>
  <div class="itpe-flow-step">
    <div class="itpe-flow-step__num">4</div>
    <div class="itpe-flow-step__title">실행 효과</div>
    <div class="itpe-flow-step__desc">단건 점 검색 TPS 5배 향상 및 무중단 동적 데이터 수용성 확보</div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 확장성 해싱(Extendible Hashing)의 정의

- 검색 키의 해시 비트 접두사를 가리키는 **디렉터리(Directory)**를 두고, 데이터 증가 시 전체 재해싱 없이 오버플로우가 발생한 **해당 버킷만 국소 분할(Local Split)**하는 동적 해싱 기법

### 2. 2대 구성 요소 및 분할 시나리오 비교

- **핵심 구성 요소**:
  - 글로벌 깊이 ($d$): 디렉터리 식별 접두사 비트 수 (디렉터리 크기 = $2^d$)
  - 로컬 깊이 ($d'$): 해당 버킷 레코드들이 공유하는 공통 접두사 비트 수 ($d' \le d$)

| 구분 | 시나리오 1: $d' < d$ | 시나리오 2: $d' = d$ |
|---|---|---|
| **디렉터리 조작** | 디렉터리 크기 유지 (확장 없음) | **디렉터리 2배 확장** ($d \leftarrow d + 1$, 엔트리 $2^{d+1}$) |
| **버킷 분할** | 넘친 버킷만 2개 분할 후 $d' \leftarrow d' + 1$ | 디렉터리 확장 후 시나리오 1 절차 동일 수행 |
| **처리 비용** | 디스크 블록 1개 할당 (경량) | 디렉터리 메모리 복제 비용 수반 |

### 3. 차별화 제언

- 해시 편향으로 인한 디렉터리 폭증(Directory Explosion)을 방지하기 위해 **MurmurHash3** 균등 해시 함수와 **글로벌 깊이 상한($d_{max}$)**을 적용하고, 순수 Point Query 워크로드에 한정하여 선별 배치함

## 출제 이력과 검증 출처

- 정보관리기술사 제135회 4교시 1번: 확장성 해싱(Extendible Hashing) 기법
- 컴퓨터시스템응용기술사 제120회 1교시: 정적 해싱과 동적 해싱 비교
- Ronald Fagin et al. (1979), "Extendible Hashing - A Fast Access Method for Dynamic Files", *ACM TODS*
- Abraham Silberschatz et al., *Database System Concepts (7th Edition)*, Chapter 14

## 학습 체크

- [ ] 정적 해싱 대비 확장성 해싱이 갖는 본질적인 개선점(재해싱 회피, 국소 분할)을 설명할 수 있는가
- [ ] 글로벌 깊이($d$)와 로컬 깊이($d'$)의 정의와 둘 사이의 수학적 관계식을 제시할 수 있는가
- [ ] 버킷 오버플로우 시 $d' < d$인 경우와 $d' = d$인 경우의 2가지 처리 절차를 도식화하여 구분할 수 있는가
- [ ] 선형 해싱(Linear Hashing)과의 핵심 차이점(디렉터리 유무, 분할 기준)을 비교 설명할 수 있는가
- [ ] Ⅶ 결론에서 디렉터리 폭증 방지 엔지니어링 및 하이브리드 티어링 전략을 제시할 수 있는가

## 연결 토픽

- [인덱스(Index)](./047_index/) · [팬텀 충돌](./049_phantom_conflict/) · [데이터베이스 분할](./021_db_partitioning_sharding/) · [샤딩](./045_sharding/)
