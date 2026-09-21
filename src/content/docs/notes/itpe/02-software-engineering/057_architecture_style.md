---
title: "아키텍처 스타일"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
author: "Antigravity"
date: "2026-09-21T16:36:00+09:00"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 아키텍처 설계를 거쳐 아키텍처 스타일로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>아키텍처 설계</span>
  <strong>아키텍처 스타일</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **아키텍처 스타일(Architecture Style)**은 소프트웨어 시스템의 거시적 골격을 정의하는 재사용 가능한 패턴으로, 컴포넌트의 유형, 상호작용 커넥터, 그리고 배치와 동작을 규정하는 제약조건(Constraints)의 집합
- 메커니즘: **4대 고전 계열(데이터 흐름 · 호출/복귀 · 독립 컴포넌트 · 데이터 중심)** + **품질속성 트레이드오프(ATAM)** + **하이브리드 조합(EDA + 헥사고날)**
- 산출/효과: 비기능 요구사항(성능/확장성/유지보수성) 사전 예측 · 아키텍처 설계 재사용 · 시스템 결합도 최소화

<div class="itpe-flow-map" role="img" aria-label="소프트웨어 아키텍처 스타일 체계도">
  <div class="itpe-flow-node"><strong>비즈니스·품질 요구</strong><span>성능·확장성·변경성</span></div>
  <div class="itpe-flow-arrow">→ 4대 계열 패턴 선정 →</div>
  <div class="itpe-flow-node is-current">
    <strong>대표 아키텍처 스타일</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>데이터 흐름</strong><span><span class="itpe-keyword"><strong>파이프-필터 (Pipes & Filters)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>호출 및 복귀</strong><span><span class="itpe-keyword"><strong>계층화 아키텍처 (Layered)</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>독립 컴포넌트</strong><span><span class="itpe-keyword"><strong>이벤트 주도 (EDA) · MSA</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>데이터 중심</strong><span>블랙보드 (Blackboard) · 저장소</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 트레이드오프 분석 및 최적화 →</div>
  <div class="itpe-flow-node"><strong>하이브리드 구현</strong><span>도메인 격리 및 고확장성 달성</span></div>
</div>

<details>
<summary>핵심 용어</summary>

- **Architecture Style**: 시스템의 거시적 구조를 규정하는 컴포넌트, 커넥터, 제약조건의 검증된 배치 양식
- **Pipes and Filters**: 데이터 변환을 담당하는 Filter와 단방향 데이터 통로 Pipe를 결합한 데이터 흐름 스타일
- **Layered Architecture**: 컴포넌트를 수평 계층으로 분할하여 상위 계층이 직하위 계층에만 의존하는 구조
- **Event-Driven Architecture (EDA)**: 생산자가 이벤트를 발행하고 소비자가 비동기로 수신 처리하는 결합도 제로 스타일
- **Hexagonal Architecture (Ports & Adapters)**: 비즈니스 도메인 로직을 코어에 두고 외부 인프라와의 상호작용을 포트와 어댑터로 격리하는 현대적 스타일

</details>

## 예상문제

> 소프트웨어 시스템의 거시적 구조 템플릿인 아키텍처 스타일(Architecture Style)의 개념을 설명하고, 쇼 & 갈란(Shaw & Garlan)의 4대 고전 계열 및 대표 스타일을 비교하며, 도메인 특성에 맞지 않는 스타일 도입 위험 및 통제 방안을 제시하시오. (25점)

## Ⅰ. 시스템 거시적 골격 정형화, 아키텍처 스타일의 개요

> 모든 비기능 품질을 동시에 만족하는 만능 아키텍처 스타일은 없으며, 핵심 품질 목표에 맞는 최적의 양식을 선택해야 한다.

- 정의: 소프트웨어 시스템의 거시적 구조를 정의하는 템플릿으로, 컴포넌트(계산 단위), 커넥터(상호작용 메커니즘), 그리고 이들의 배치와 동작을 규정하는 제약조건들의 집합
- 목적:
  - **품질속성 조기 예측**: 스타일 선정만으로도 성능, 유지보수성, 확장성의 유불리를 선제 파악
  - **설계 의사결정 재사용**: 검증된 산업계 표준 골격을 차용하여 설계 오류와 비용 최소화
  - **이해관계자 간 공통 어휘 제공**: 시스템의 상위 구조에 대한 직관적이고 일관된 멘탈 모델 공유

## Ⅱ. 쇼 & 갈란(Shaw & Garlan)의 4대 고전 계열 및 대표 스타일

> 데이터 전달 방식과 제어 흐름에 따라 4대 고전 계열로 체계화된다.

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" style="max-width: 520px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="style-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- 1. Pipes & Filters -->
  <rect x="15" y="15" width="235" height="90" rx="6" fill="var(--sl-color-blue-subtle, #eff6ff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1.5" filter="url(#style-shadow)"/>
  <text x="25" y="34" font-size="11" font-weight="700" fill="var(--sl-color-blue-high, #2563eb)">1. 데이터 흐름: Pipes &amp; Filters</text>
  <rect x="25" y="44" width="48" height="28" rx="3" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="49" y="62" text-anchor="middle" font-size="9" font-weight="700" fill="var(--sl-color-text, #1f2937)">Filter1</text>
  <path d="M 73 58 L 93 58" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1.5"/>
  <rect x="93" y="44" width="48" height="28" rx="3" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="117" y="62" text-anchor="middle" font-size="9" font-weight="700" fill="var(--sl-color-text, #1f2937)">Filter2</text>
  <path d="M 141 58 L 161 58" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1.5"/>
  <rect x="161" y="44" width="48" height="28" rx="3" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1"/>
  <text x="185" y="62" text-anchor="middle" font-size="9" font-weight="700" fill="var(--sl-color-text, #1f2937)">Filter3</text>
  <text x="25" y="92" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">단방향 순차 스트리밍 변환 (Unix 파이프, ETL)</text>

  <!-- 2. Layered Architecture -->
  <rect x="270" y="15" width="235" height="90" rx="6" fill="var(--sl-color-green-subtle, #f0fdf4)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="1.5" filter="url(#style-shadow)"/>
  <text x="280" y="34" font-size="11" font-weight="700" fill="var(--sl-color-green-high, #16a34a)">2. 호출/복귀: Layered (계층형)</text>
  <rect x="280" y="44" width="215" height="15" rx="2" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="0.8"/>
  <text x="387" y="55" text-anchor="middle" font-size="8" fill="var(--sl-color-text, #1f2937)">표현 계층 (Presentation Layer)</text>
  <rect x="280" y="61" width="215" height="15" rx="2" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="0.8"/>
  <text x="387" y="72" text-anchor="middle" font-size="8" fill="var(--sl-color-text, #1f2937)">비즈니스 계층 (Business Logic)</text>
  <rect x="280" y="78" width="215" height="15" rx="2" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="0.8"/>
  <text x="387" y="89" text-anchor="middle" font-size="8" fill="var(--sl-color-text, #1f2937)">데이터 영속 계층 (Persistence Layer)</text>
  <text x="280" y="101" font-size="7.5" fill="var(--sl-color-text-muted, #4b5563)">상위가 직하위에만 의존하는 수평 분할</text>

  <!-- 3. Event-Driven Architecture (EDA) -->
  <rect x="15" y="115" width="235" height="90" rx="6" fill="var(--sl-color-purple-subtle, #f5f3ff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1.5" filter="url(#style-shadow)"/>
  <text x="25" y="134" font-size="11" font-weight="700" fill="var(--sl-color-accent, #7c3aed)">3. 독립 컴포넌트: Event-Driven (EDA)</text>
  <rect x="25" y="144" width="55" height="26" rx="3" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1"/>
  <text x="52" y="161" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1f2937)">Producer</text>
  <path d="M 80 157 L 98 157" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1.5"/>
  <rect x="98" y="142" width="70" height="30" rx="3" fill="var(--sl-color-accent, #7c3aed)"/>
  <text x="133" y="161" text-anchor="middle" font-size="9" font-weight="700" fill="#ffffff">Broker/Topic</text>
  <path d="M 168 157 L 186 157" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1.5"/>
  <rect x="186" y="144" width="55" height="26" rx="3" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1"/>
  <text x="213" y="161" text-anchor="middle" font-size="8.5" fill="var(--sl-color-text, #1f2937)">Consumer</text>
  <text x="25" y="193" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">비동기 발행-구독 기반 결합도 제로 (Kafka)</text>

  <!-- 4. Blackboard / Repository -->
  <rect x="270" y="115" width="235" height="90" rx="6" fill="var(--sl-color-orange-subtle, #fffbeb)" stroke="var(--sl-color-orange-high, #d97706)" stroke-width="1.5" filter="url(#style-shadow)"/>
  <text x="280" y="134" font-size="11" font-weight="700" fill="var(--sl-color-orange-high, #d97706)">4. 데이터 중심: Blackboard (저장소)</text>
  <rect x="345" y="145" width="85" height="30" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-orange-high, #d97706)" stroke-width="1.5"/>
  <text x="387" y="164" text-anchor="middle" font-size="9.5" font-weight="700" fill="var(--sl-color-orange-high, #d97706)">Blackboard</text>
  <text x="300" y="160" font-size="8.5" fill="var(--sl-color-text, #1f2937)">KS1 ⇄</text>
  <text x="440" y="160" font-size="8.5" fill="var(--sl-color-text, #1f2937)">⇄ KS2</text>
  <text x="280" y="193" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">중앙 공유 저장소와 독립 지식원 협업 (AI/음성)</text>
</svg>
</div>

<div class="itpe-pipeline is-vertical" role="img" aria-label="4대 고전 아키텍처 스타일 체계">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. 데이터 흐름 계열: 파이프 앤 필터 (Pipes & Filters)</strong></span>
    <span>데이터를 순차 변환하는 독립적 Filter와 단방향 데이터 통로 Pipe의 연결 · 재사용성 및 병렬성 우수 (Unix 쉘, ETL)</span>
  </div>
  <div class="itpe-pipeline-arrow">↕</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. 호출 및 복귀 계열: 계층화 아키텍처 (Layered Architecture)</strong></span>
    <span>기능을 수평 계층으로 분할하여 상위가 직하위 계층에만 의존 · 추상화 및 유지보수성 우수 (OSI 7계층, 웹 3계층)</span>
  </div>
  <div class="itpe-pipeline-arrow">↕</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. 독립 컴포넌트 계열: 이벤트 주도 아키텍처 (EDA)</strong></span>
    <span>발행자가 이벤트를 메시지 채널에 게시하고 구독자가 비동기 수신 · 확장성 극대화 및 결합도 최소화 (Kafka, IoT)</span>
  </div>
  <div class="itpe-pipeline-arrow">↕</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>4. 데이터 중심 계열: 블랙보드 (Blackboard / Repository)</strong></span>
    <span>중앙 공유 저장소(Blackboard)를 두고 독립 에이전트(지식원)들이 협업하여 비결정적 해 도출 (음성인식, AI 추론)</span>
  </div>
</div>

## Ⅲ. 아키텍처 추상화 3단계 비교: 스타일 vs 디자인 패턴 vs 관용구

> 소프트웨어 설계는 추상화 수준과 영향 범위에 따라 3단계 계층으로 분화된다.

| 구분 | 아키텍처 스타일 (Style) | 디자인 패턴 (Design Pattern) | 관용구 (Idiom) |
|---|---|---|---|
| **영향 범위** | **시스템 전체**의 거시적 구조 | 특정 서브시스템 및 컴포넌트 내부 | 단일 클래스 및 소스코드 레벨 |
| **주요 관심사** | 컴포넌트 간 물리적/논리적 배치 | 객체와 클래스 간의 관계 및 역할 분담 | 특정 언어 문법 및 런타임 관례 |
| **품질 속성 영향**| 시스템 전체 비기능 속성(성능, 확장성) | 컴포넌트 단위 변경성, 유연성 | 코드 가독성, 메모리 누수 방지 |
| **대표 사례** | Layered, Pipes & Filters, EDA, MSA | Factory, Strategy, Observer, Adapter | Java try-with-resources, Go defer |

## Ⅳ. 아키텍처 스타일 오적용 위험 및 실무 통제 대책

> 시스템 특성과 맞지 않는 무리한 최신 스타일 강제는 치명적인 운영 복잡도와 장애를 야기한다.

| 위험 | 대책 | 효과 |
|---|---|---|
| **스트리밍 대량 유실 (계층형 오적용)** | 데이터 흐름 시스템에 **파이프-필터(Kafka Streams)** 파이프라인 전환 | 직렬화 오버헤드 제거 및 초당 10만 건 무손실 처리 보장 |
| **분산 트랜잭션 파탄 (과도한 EDA)** | 단순 도메인은 **모듈러 모놀리스** 회귀 및 비동기 알림만 EDA 격리 | 시스템 가시성 회복 및 불필요한 운영 복잡도 70% 절감 |
| **도메인 로직 오염 (DB 종속성)** | 비즈니스 코어를 중심에 두는 **헥사고날(Ports & Adapters)** 적용 | 데이터베이스/외부 프레임워크 변경 시에도 비즈니스 로직 보호 |

## Ⅴ. 품질속성 트레이드오프 기반 하이브리드 아키텍처 관점의 기술사적 제언

> 단일 스타일의 교조적 채택을 벗어나, 외부와 내부의 관심사를 분리하는 하이브리드 진화 모델을 채택해야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 아키텍처 스타일을 선택할 때 가장 위험한 태도는 "최신 트렌드니까 무조건 MSA와 EDA를 써야 한다"는 기술적 허영심임. EDA는 높은 확장성(Scalability)과 유연성을 주지만, 데이터 최종 일관성(Eventual Consistency), 분산 디버깅의 지옥, 네트워크 오버헤드라는 막대한 기회비용을 요구함. 따라서 시스템 외부는 비동기 메시징 기반의 EDA로 결합도를 낮추고, 서비스 내부는 헥사고날 아키텍처로 도메인 무결성을 지키는 '하이브리드 다계층 아키텍처'가 실무의 정답임.
- 나라면: 아키텍처 선정 시 ATAM 워크숍을 통해 시스템의 최우선 품질속성(예: 대용량 트래픽 수용 vs 즉각적 금융 정합성)을 도출하고, 외부 트래픽 처리 구간에는 파이프-필터와 EDA를 배치하되, 코어 원장 처리 구간에는 엄격한 계층형 트랜잭션 아키텍처를 결합하는 하이브리드 아키텍처 청사진을 제시하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 단일 스타일 맹신 탈피, 도메인별 최우선 품질속성(확장성 vs 일관성) 트레이드오프 판정
- **대응 방안**: 시스템 외부(비동기 EDA/파이프-필터)와 시스템 내부(도메인 격리 헥사고날 아키텍처)의 하이브리드 조합 적용
- **검증 체계**: ATAM 기반 품질 시나리오 평가 및 비즈니스 코어와 인프라 간 결합도 ArchUnit 정적 검증
- **기대 효과**: 트래픽 스파이크 완벽 흡수, 분산 복잡도 최소화 및 비즈니스 로직 변경 비용 60% 절감

<div class="itpe-pipeline is-vertical" role="img" aria-label="하이브리드 아키텍처 스타일 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>단일 스타일 맹신으로 인한 데이터 유실 또는 과도한 분산 복잡도 발생</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>경계별 하이브리드 조합 (외부: EDA/파이프-필터, 내부: 헥사고날 코어)</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>ATAM 절충점 충족도 및 비즈니스 로직의 외부 인프라 비의존성 검증</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>트래픽 스파이크 완벽 흡수 · 도메인 변경 비용 60% 절감 달성</span>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **아키텍처 스타일(Architecture Style)**은 컴포넌트, 커넥터, 제약조건의 배치를 통해 시스템 거시 구조를 규정하는 재사용 가능한 패턴
- 목적: 시스템 품질속성 조기 예측, 설계 의사결정 재사용, 공통 의사소통 표준화

### 2. 쇼 & 갈란 4대 고전 계열 요약

<div class="itpe-pipeline is-vertical" role="img" aria-label="4대 계열 요약">
  <div class="itpe-pipeline-node"><strong>데이터 흐름 & 호출/복귀</strong><span>Pipes & Filters (순차 변환) · Layered (수평 계층 추상화)</span></div>
  <div class="itpe-pipeline-arrow">↕</div>
  <div class="itpe-pipeline-node"><strong>독립 컴포넌트 & 데이터 중심</strong><span>Event-Driven (비동기 디커플링) · Blackboard (중앙 저장소 공유 협업)</span></div>
</div>

### 3. 핵심 통제

- **ATAM 평가**: 품질속성(확장성 vs 일관성) 간의 트레이드오프 분석을 통한 최적 스타일 선정
- **하이브리드 설계**: 외부 EDA(확장성) + 내부 헥사고날(유지보수성) 결합

## 출제 이력과 검증 출처

- 제120회 정보관리기술사 1교시: 소프트웨어 아키텍처 모델 유형
- Mary Shaw and David Garlan, Software Architecture: Perspectives on an Emerging Discipline
- Mark Richards & Neal Ford, Fundamentals of Software Architecture (O'Reilly)

## 학습 체크

- [ ] 아키텍처 스타일의 3대 구성요소(컴포넌트, 커넥터, 제약조건)를 설명할 수 있는가?
- [ ] 쇼 & 갈란의 4대 고전 계열(데이터 흐름, 호출/복귀, 독립 컴포넌트, 데이터 중심)을 비교할 수 있는가?
- [ ] 아키텍처 스타일, 디자인 패턴, 코딩 관용구의 차이점을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [SW 아키텍처](./056_software_architecture.md)
- 연관 토픽: [MSA](./035_msa.md), [REST](./015_rest.md), [SW 아키텍처 평가](./124_software_architecture_analysis.md)
- 다음 토픽: [모델 기반 테스트(MBT)](./058_mbt.md)
