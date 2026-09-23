---
title: "데이터 품질관리"
category: "03-data"
tags:
  - "DQM"
  - "데이터품질"
  - "CDE"
  - "DataContract"
  - "프로파일링"
  - "품질6대차원"
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

<div class="itpe-topic-path" role="img" aria-label="데이터 관리에서 데이터 거버넌스와 품질로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 거버넌스·품질</span>
  <strong>데이터 품질관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 데이터가 비즈니스 목적에 부합하도록 정책·조직·프로세스·기술 도구를 결합하여 데이터 생명주기 전반의 품질을 계획·진단·개선·통제하는 지속적 엔지니어링 프레임워크
- 메커니즘: CDE(핵심데이터) 식별 $\rightarrow$ 품질 표준·규칙 정의 $\rightarrow$ 프로파일링 및 6대 차원 진단 $\rightarrow$ 오류 원인 분석 및 정제 $\rightarrow$ Data Contract 기반 원천 예방
- 산출물: 데이터 품질관리 정책서 · CDE 정의서 · 품질 진단 보고서 · Data Contract 명세서

<div class="itpe-flow-map" role="img" aria-label="데이터 품질관리 프레임워크 및 원천 예방 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: CDE 선정 및 품질 규칙 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>수립</strong><span>핵심 데이터 항목(CDE) 식별, 도메인 허용값 및 유효성 검증 규칙 정의</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 데이터 프로파일링 및 품질 진단</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>진단</strong><span>값·구조·업무규칙 기반 6대 차원(정확성·완전성·유효성·일관성·적시성·유일성) 측정</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: Data Contract 기반 원천 검증</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>예방</strong><span>생산자-소비자 간 스키마 규약 준수 및 CI/CD 파이프라인 내 사전 테스트</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 데이터 품질 및 계약 준수 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>CDE 오류율이 허용 임계치 이하이며, 상류 스키마 변경이 Data Contract를 충족하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (파이프라인 적재 승인)</strong>
      <span>운영 DW/Data Lake 적재 허용 $\rightarrow$ Data Observability 실시간 지표 관제</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (오류 데이터 유입 차단)</strong>
      <span>파이프라인 자동 차단(Circuit Breaker) $\rightarrow$ 원천 데이터 정제 및 생산자 스키마 롤백</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `DQM(Data Quality Management)`: 업무 목적에 맞는 품질을 데이터 생명주기 전반에서 측정·개선·통제하는 관리체계
- `CDE(Critical Data Element)`: 비즈니스 오류 영향도가 커서 우선적으로 품질 규칙과 전담 책임자를 지정하는 핵심 데이터 항목
- `Data Contract`: 데이터 생산자와 소비자 간에 합의된 스키마, SLA, 품질 임계치를 명시하여 배포 전에 자동 검증하는 약속
- `Data SLO(Service Level Objective)`: 데이터 품질 차원(정확성, 적시성 등)을 정량적 수치로 약정하는 서비스 수준 목표
- `Data Observability`: 데이터 파이프라인 전반에서 이상 징후, 스키마 변경, 지연(Freshness)을 실시간 추적·모니터링하는 기술
- `6대 품질 차원`: 정확성(Accuracy), 완전성(Completeness), 일관성(Consistency), 유효성(Validity), 적시성(Timeliness), 유일성(Uniqueness)

</details>
---

## 1교시 예상문제 (10점)

> 데이터 품질관리의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)
---

## 1교시 10점 답안

```text
1. 데이터 품질관리(DQM)의 정의 및 목적
- 정의: 비즈니스 목적에 부합하도록 데이터 생명주기 전반의 품질을 계획·진단·개선·통제하는 관리체계
- 목적: 의사결정 신뢰도 확보 및 오류 정제 비용 증폭(1:10:100의 법칙) 원천 차단

2. DQM 프레임워크 4대 구성요소 및 6대 차원
- 4대 프레임워크: 조직(Owner/Steward), 프로세스(진단/개선), 표준(표준사전/업무규칙), 도구(프로파일링)
- 6대 품질 차원 : 정확성(Fact 일치), 완전성(Null 부재), 일관성(상호 모순 부재),
                  유효성(규칙 준수), 적시성(Freshness), 유일성(중복 부재)

3. 원천 예방을 위한 핵심 전략
- 사후 배치 정제 탈피 → CDE(핵심데이터) 선정 및 Data Contract 사전 규약 체결
- CI/CD 파이프라인 통합: 스키마 위반 시 빌드 자동 실패 및 런타임 서킷 브레이커 가동
```
---

### 핵심 관계

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **DQM 프레임워크** | K-DATA DQC(M/V), 조직(Steward), 프로세스(진단·개선), 표준, 도구 | Ⅲ 구조·체계 |
| **품질 진단 6대 차원** | 정확성, 완전성, 일관성, 유효성, 적시성, 유일성 | Ⅳ 진단 차원 |
| **원천 예방 거버넌스** | Data Contract, CI/CD 스키마 테스트, Data Observability, 서킷 브레이커 | Ⅵ·Ⅶ |

---

## 2~4교시 예상문제 (25점)

> 전사 데이터 자산의 신뢰성 확보 및 AI 모델 왜곡 방지를 위한 데이터 품질관리(DQM) 프레임워크 구성요소(조직, 프로세스, 표준, 도구)와 데이터 품질 진단 6대 차원을 제시하고, 사후 정제 한계를 극복하기 위한 원천 예방 통제 전략을 설명하시오. (25점)

> (25점, 예상)
---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **DQM 프레임워크** | K-DATA DQC(M/V), 조직(Steward), 프로세스(진단·개선), 표준, 도구 | Ⅲ 구조·체계 |
| **품질 진단 6대 차원** | 정확성, 완전성, 일관성, 유효성, 적시성, 유일성 | Ⅳ 진단 차원 |
| **원천 예방 거버넌스** | Data Contract, CI/CD 스키마 테스트, Data Observability, 서킷 브레이커 | Ⅵ·Ⅶ |

### Ⅰ. 신뢰할 수 있는 데이터 생태계의 기반, 데이터 품질관리 개요

> 데이터 품질관리는 사후적 오류 정제를 넘어, 데이터 생산 단계부터 유효성을 강제하여 오류의 전파와 비용 낭비를 원천 차단하는 엔지니어링 체계임.

- 정의: 데이터의 활용 목적(Fitness for Use)을 달성하기 위해 조직, 프로세스, 표준, 도구를 결합하여 데이터의 생성부터 폐기까지 전 생명주기에 걸쳐 품질을 통제하는 관리 활동
- 목적: 의사결정 신뢰도 제고·시스템 연계 오류·하류 재작업 감소
- 배경: AI 모델 학습 데이터 오염(Garbage In, Garbage Out) 방지 및 실시간 스트리밍 분석의 안정성 확보 요구

### Ⅱ. 데이터 결함의 하류 전파와 예방 통제 (1:10:100의 법칙)

> 생성 단계의 결함을 늦게 발견할수록 연계 재처리·의사결정 정정 비용이 기하급수적으로 폭증하므로 원천 예방(Data Contract)이 필수적임.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 210" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="dq-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <rect x="5" y="5" width="510" height="200" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Step 1: Generation -->
    <rect x="15" y="15" width="150" height="110" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#16a34a" stroke-width="1.5"/>
    <rect x="15" y="15" width="150" height="24" rx="6" fill="var(--color-bg-subtle, #f0fdf4)"/>
    <text x="90" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#16a34a">① 생성 단계 (원천)</text>
    <text x="90" y="52" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">업무 시스템 입력/API</text>
    <text x="90" y="68" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">Data Contract 검증</text>
    <rect x="30" y="85" width="120" height="25" rx="4" fill="var(--color-bg-subtle, #f0fdf4)" stroke="#16a34a" stroke-width="0.8"/>
    <text x="90" y="101" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#16a34a">오류 조치 비용: 1배</text>

    <!-- Arrow 1->2 -->
    <line x1="165" y1="70" x2="183" y2="70" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#dq-arrow)"/>

    <!-- Step 2: Processing -->
    <rect x="185" y="15" width="150" height="110" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#ca8a04" stroke-width="1.5"/>
    <rect x="185" y="15" width="150" height="24" rx="6" fill="var(--color-bg-subtle, #fefce8)"/>
    <text x="260" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#ca8a04">② 연계·가공 (중류)</text>
    <text x="260" y="52" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">ETL / DW / Lakehouse</text>
    <text x="260" y="68" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">프로파일링 &amp; 정제</text>
    <rect x="200" y="85" width="120" height="25" rx="4" fill="var(--color-bg-subtle, #fefce8)" stroke="#ca8a04" stroke-width="0.8"/>
    <text x="260" y="101" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#ca8a04">오류 조치 비용: 10배</text>

    <!-- Arrow 2->3 -->
    <line x1="335" y1="70" x2="353" y2="70" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#dq-arrow)"/>

    <!-- Step 3: Consumption -->
    <rect x="355" y="15" width="150" height="110" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="#dc2626" stroke-width="1.5"/>
    <rect x="355" y="15" width="150" height="24" rx="6" fill="var(--color-bg-subtle, #fef2f2)"/>
    <text x="430" y="31" text-anchor="middle" font-size="8.5" font-weight="bold" fill="#dc2626">③ 분석·활용 (하류)</text>
    <text x="430" y="52" text-anchor="middle" font-size="7.5" fill="var(--color-text, #334155)">AI 모델 / 경영 리포트</text>
    <text x="430" y="68" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">의사결정 왜곡·GIGO</text>
    <rect x="370" y="85" width="120" height="25" rx="4" fill="var(--color-bg-subtle, #fef2f2)" stroke="#dc2626" stroke-width="0.8"/>
    <text x="430" y="101" text-anchor="middle" font-size="7.5" font-weight="bold" fill="#dc2626">오류 조치 비용: 100배</text>

    <!-- Bottom summary bar -->
    <rect x="15" y="140" width="490" height="50" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1"/>
    <text x="260" y="158" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">원천 차단 패러다임: Data Contract + CI/CD 스키마 테스트 + Circuit Breaker</text>
    <text x="260" y="174" text-anchor="middle" font-size="7.5" fill="var(--color-primary, #2563eb)">사후 배치 정제의 한계를 탈피하고, 생산 단계에서 검증되지 않은 데이터의 파이프라인 유입을 원천 봉쇄</text>
  </svg>
</div>

### Ⅲ. 데이터 품질관리(DQM) 프레임워크 4대 구성요소

> 조직, 프로세스, 표준, 기술 도구가 상호 유기적으로 결합되어 선순환 피드백 루프를 형성함.

| 구성요소 | 주요 역할 및 책임 | 핵심 산출물 |
|---|---|---|
| **조직 (Organization)** | Data Owner(비즈니스 책임자), Data Steward(품질 관리 실무자), 품질 심의 위원회 운영 | 품질 R&R 정의서, 거버넌스 규정집 |
| **프로세스 (Process)** | CDE 식별 $\rightarrow$ 품질 진단 $\rightarrow$ 원인 분석 $\rightarrow$ 정제 $\rightarrow$ 모니터링 선순환 | 품질 진단 절차서, 이슈 조치 이력부 |
| **표준 (Standards)** | 전사 표준 단어·용어·도메인·코드 정의 및 비즈니스 유효성 검증 규칙 수립 | 데이터 표준사전, 비즈니스 룰북 |
| **도구 (Tools)** | 데이터 프로파일링, 메타데이터 관리, 실시간 Observability 모니터링 시스템 | 프로파일링 리포트, 품질 대시보드 |

### Ⅳ. 데이터 품질 진단 6대 차원 체계

> 정량적 측정이 가능한 6가지 핵심 품질 차원을 기준으로 시스템 무결성을 판정함.

| 품질 차원 | 개념 및 정의 | 대표 진단 지표 및 질문 |
|---|---|---|
| **정확성 (Accuracy)** | 실제 세계의 사실(Fact)과 일치하는 정도 | 주민번호 유효성 검증, GPS 좌표 현실 부합 여부 |
| **완전성 (Completeness)** | 필수 요구 항목이 누락되지 않고 채워진 정도 | 필수 입력 필드의 Null 값 비율, Foreign Key 미할당률 |
| **일관성 (Consistency)** | 서로 다른 저장소 간 데이터가 상호 모순 없이 일치하는 정도 | CRM 고객 주소와 ERP 배송지 주소의 일치율 |
| **유효성 (Validity)** | 정의된 도메인 형식, 범위, 비즈니스 규칙을 충족하는 정도 | 이메일 정규식 포맷 일치, 주문금액 0원 초과 여부 |
| **적시성 (Timeliness)** | 필요한 시점에 지연 없이 데이터가 제공되는 정도 | 원천 DB 커밋 후 분석 DW 적재까지의 지연시간(Freshness) |
| **유일성 (Uniqueness)** | 동일 개체에 대한 중복 레코드가 존재하지 않는 정도 | 단일 고객에 대한 고유 식별자 중복 레코드 비율 |

### Ⅴ. 데이터 거버넌스 · 데이터 표준화 · 데이터 품질관리 관계

> 세 영역은 독립된 사업이 아니며, 거버넌스의 지휘 아래 표준을 기준으로 삼아 품질을 통제하는 상호 보완 관계임.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="gov-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Top: Governance -->
    <rect x="150" y="15" width="220" height="50" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <text x="260" y="34" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">데이터 거버넌스 (Data Governance)</text>
    <text x="260" y="50" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">[지휘·통제] 조직 R&amp;R, 정책, 품질 위원회, 예산</text>

    <!-- 2 Diagonal Arrows Down -->
    <line x1="210" y1="65" x2="130" y2="100" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#gov-arrow)"/>
    <line x1="310" y1="65" x2="390" y2="100" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#gov-arrow)"/>
    <text x="150" y="80" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">원칙 제시</text>
    <text x="350" y="80" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">통제 위임</text>

    <!-- Left: Standardization -->
    <rect x="25" y="105" width="210" height="70" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="25" y="105" width="210" height="20" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="130" y="119" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">데이터 표준화 (Standardization)</text>
    <text x="130" y="137" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">[판정 기준선 제공]</text>
    <text x="130" y="152" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">표준 단어·용어·도메인·코드</text>
    <text x="130" y="165" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">비즈니스 규칙 및 검증 룰북</text>

    <!-- Right: Quality Management -->
    <rect x="285" y="105" width="210" height="70" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="285" y="105" width="210" height="20" rx="6" fill="var(--color-bg-subtle, #f0fdf4)"/>
    <text x="390" y="119" text-anchor="middle" font-size="8" font-weight="bold" fill="#16a34a">데이터 품질관리 (Quality Mgmt)</text>
    <text x="390" y="137" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--color-text, #1e293b)">[실행 및 측정·환류]</text>
    <text x="390" y="152" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">프로파일링, 6대 차원 진단</text>
    <text x="390" y="165" text-anchor="middle" font-size="6.5" fill="var(--color-text-muted, #64748b)">Data Contract 원천 검증 &amp; 정제</text>

    <!-- Horizontal Bidirectional Arrow -->
    <line x1="235" y1="140" x2="277" y2="140" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#gov-arrow)"/>
    <line x1="285" y1="145" x2="243" y2="145" stroke="#16a34a" stroke-width="1.5" marker-end="url(#gov-arrow)"/>
    <text x="260" y="135" text-anchor="middle" font-size="6" fill="var(--color-text-muted, #64748b)">기준적용</text>
    <text x="260" y="157" text-anchor="middle" font-size="6" fill="var(--color-text-muted, #64748b)">오류환류</text>
  </svg>
</div>

### Ⅵ. 데이터 품질관리 문제점·대응책

> 단순 스크립트 정제의 한계를 극복하고 데이터 파이프라인의 영속적 무결성을 보장함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 정제 후 동일 오류 지속 재발 | 원인 분석(5-Why) 수행 및 원천 입력 폼에 정규식 검증 강제 | 배치성 반복 정제 비용 제거 및 원천 무결성 확보 |
| 업스트림 스키마 변경으로 인한 파이프라인 중단 | Data Contract 체계 도입 및 CI/CD에 스키마 호환성 테스트 통합 | 다운스트림 분석 대시보드 장애 원천 차단 |
| 전수 검사로 인한 인프라 부하 | 업무 영향도 기반 핵심 데이터(CDE) 선별·적응형 샘플링 | 고위험 데이터에 검사 자원 집중 |
| 소유자 부재로 인한 품질 방치 | Data Domain별 비즈니스 Data Owner 지정 및 품질 KPI 반영 | 도메인 책임주의 정착 및 능동적 품질 개선 |

### Ⅶ. 기술사적 제언: 사후 정제에서 Data Contract 기반 원천 예방으로

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 데이터 정제는 '고장 난 수도꼭지 아래에서 바닥을 닦는 행위'이며, 진정한 품질관리는 수도꼭지를 고치는 원천 예방이다. 데이터 품질을 IT 전담 부서의 전유물로 보거나 일회성 배치 정제 사업으로 끝내는 조직은 필연적으로 수개월 내 품질 퇴행을 겪는다. 품질의 성패는 사후 에러 수집이 아니라, 데이터를 생산하는 비즈니스 도메인이 책임을 지는 **도메인 중심 책임주의(Domain Ownership)와 Data Contract 체결**에 달려 있다.

> **[나라면 이렇게 쓴다]**
> 2교시형 문제라면 전사 CDE(Critical Data Element)를 선정하고, 데이터 생산자와 소비자 간에 **Data Contract(스키마 버전, SLA, Null 허용률)**를 명시적으로 체결하겠다. 이를 GitHub Actions와 같은 CI/CD 파이프라인에 통합하여 스키마 브레이킹 체인지 발생 시 빌드를 자동 차단하고, 런타임에는 Data Observability 도구를 연계하여 Data SLO 위반 시 파이프라인을 멈추는 **서킷 브레이커(Circuit Breaker)** 무결성 게이트를 제시하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 사후 오류 조치 건수의 감소보다 **원천 생산 단계에서 스키마 위반 및 무결성 결함을 자동 차단**하고 있는가로 성숙도를 판정.
- **대응 방안**: CDE별 Data Owner 지정 $\rightarrow$ Data Contract 규약 체결 $\rightarrow$ CI/CD 스키마 회귀 테스트 $\rightarrow$ Data Observability 서킷 브레이커 가동.
- **검증 체계**: Great Expectations 및 Soda Core를 활용하여 데이터 파이프라인 적재 전 6대 품질 차원 자동 검증 및 CDE 오류율 0.01% 이하 관리.
- **기대 효과**: 데이터 결함 하류 전파 차단(1:10:100 법칙 극복), 다운스트림 분석 파이프라인 장애 90% 예방 및 재처리 비용 절감.

<div class="itpe-flow-map" role="img" aria-label="Data Contract 기반 원천 예방 및 서킷 브레이커 거버넌스 파이프라인">
  <div class="itpe-flow-node">
    <strong>CDE 선정 및 규약 정의</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>협약</strong><span>Data Owner 지정 + Data Contract 체결</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>CI/CD 스키마 테스트</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>배포</strong><span>생산자 스키마 하위호환성 검증</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node is-current">
    <strong>런타임 서킷 브레이커</strong>
    <div class="itpe-step-detail">
      <strong>통제</strong><span>SLO 위반 시 파이프라인 즉시 차단</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>무결 데이터 DW 적재</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>결과</strong><span>신뢰 기반 AI 분석 및 의사결정</span></div>
    </div>
  </div>
</div>
---

## 출제 이력과 검증 출처

- **기출 근거**: 제123·129·131회는 KPC 보조자료이며 Q-Net 공식 원문 미확보
- **표준 및 가이드라인**: 한국데이터산업진흥원(K-DATA) 데이터 품질인증(DQC) 기준, DAMA DMBOK 2.0 (Data Quality Chapter)

## 연결 토픽

- [데이터 거버넌스](./006_data_governance.md) · [데이터 표준화](./008_data_standardization.md) · [데이터 프로파일링](./105_data_profiling.md) · [데이터 가치평가](./002_data_valuation.md)
