---
title: "데이터 거버넌스(Data Governance)"
category: "03-data"
tags:
  - "데이터거버넌스"
  - "DataGovernance"
  - "DAMA_DMBOK"
  - "DataOwner"
  - "DataSteward"
  - "FederatedGovernance"
date: "2026-09-24T00:00:00+09:00"
author: "Antigravity"
extra:
  model: "GPT-6"
  keyword_grade: "기초"
sidebar:
  badge:
    text: "기초"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 관리에서 전사 의사결정 및 데이터 거버넌스로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 거버넌스·품질</span>
  <strong>데이터 거버넌스(Data Governance)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 기업의 데이터 자산에 대해 의사결정권(Decision Rights), 책임(Accountability), 관리 원칙을 정의하여 데이터 활용 가치를 극대화하고 보안·컴플라이언스 리스크를 통제하는 전사적 지휘·통제 프레임워크
- 메커니즘: 거버넌스 전략 수립 $\rightarrow$ 조직(CDO·Owner·Steward·Custodian) 및 R&R 구성 $\rightarrow$ 표준·품질·보안 프로세스 정립 $\rightarrow$ Policy as Code 및 카탈로그 자동화 $\rightarrow$ 연합형 거버넌스 실행 및 성숙도 평가
- 산출물: 전사 데이터 거버넌스 정책서 · RACI 책임 매트릭스 · 메타데이터 카탈로그 및 계보(Lineage) 맵 · 데이터 성숙도(DMM) 평가 보고서

<div class="itpe-flow-map" role="img" aria-label="데이터 거버넌스 의사결정 체계 및 거버넌스 적합성 판정 파이프라인">
  <div class="itpe-flow-node">
    <strong>1단계: 비즈니스 전략 및 컴플라이언스 요건 분석</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>분석</strong><span>디지털 전환 전략, 개인정보보호법(PIPA), EU AI Act 규제 준수 요건 수집</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>2단계: 거버넌스 위원회 및 도메인 R&R 구성</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>수립</strong><span>CDO 주관 위원회, Data Owner(승인), Data Steward(품질/표준), Custodian(인프라)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>3단계: Policy as Code 및 자동화 카탈로그 구현</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>자동화</strong><span>접근 제어(ABAC) 규칙 코드화, CI/CD 스키마 검증, 자동 Lineage 수집기 연동</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <span class="itpe-keyword"><strong>4단계: 거버넌스 성숙도 및 책임 이행 판정 (Quality Gate)</strong></span>
    <div class="itpe-step-detail">
      <strong>판정 질문</strong><span>모든 데이터 도메인에 Data Owner가 지정되고, Policy as Code 자동 승인이 작동하는가?</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-branches">
    <div class="itpe-flow-branch is-pass">
      <strong>통과 (연합형 자율 거버넌스 가동)</strong>
      <span>도메인 자율 Data Product 발행 허용 $\rightarrow$ 전사 카탈로그 공유 및 실시간 감사 관제</span>
    </div>
    <div class="itpe-flow-branch is-fail">
      <strong>미통과 (사일로 방치 / 책임 공백)</strong>
      <span>배포 차단 $\rightarrow$ CDO 위원회 소집, RACI 매트릭스 재할당 및 보안 가드레일 강화</span>
    </div>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- `Decision Rights(의사결정권)`: 데이터의 분류, 접근 허용, 보존 주기, 아키텍처 변경을 최종 결정할 수 있는 공식적 권한
- `Accountability(책무성)`: 데이터 품질, 보안 침해, 법적 컴플라이언스 준수 결과에 대해 책임을 지는 구조
- `Data Owner`: 비즈니스 도메인의 데이터 정의, 사용 승인, 가치 평가에 대한 전권을 가진 현업 임원/부서장
- `Data Steward`: 현업 비즈니스 부서에서 메타데이터 표준화, 품질 측정, 비즈니스 룰 정의를 수행하는 실무 담당자
- `Data Custodian`: 데이터베이스 관리자(DBA) 및 데이터 엔지니어로, 물리적 저장, 백업, 암호화, 성능을 담당하는 기술 주체
- `Federated Governance(연합형 거버넌스)`: 중앙 거버넌스 위원회는 공통 보안·표준 정책만 수립하고, 실제 관리는 분산 도메인 팀이 자율적으로 수행하는 운영 모델

</details>

---

## 1교시 예상문제 (10점)

> 데이터 거버넌스(Data Governance)의 정의와 목적, 핵심 구조와 작동 원리를 설명하시오. (예상)

---

## 1교시 10점 답안

```text
1. 데이터 거버넌스의 정의 및 목적
- 정의: 전사 데이터 자산의 가치 극대화와 리스크 통제를 위해 의사결정권(Decision Rights)과 책임(Accountability) 체계를 규정한 관리 체계
- 목적: 데이터 사일로 해소, 신뢰성 있는 고품질 데이터 확보, 컴플라이언스 준수

2. 거버넌스 핵심 R&R 및 프레임워크 5대 요소
- 핵심 R&R:
  · CDO 위원회: 전사 거버넌스 전략 및 공통 정책 승인
  · Data Owner: 비즈니스 도메인 데이터 승인 및 최종 책임
  · Data Steward: 데이터 표준화 및 실무 품질 진단
  · Data Custodian: DB 인프라 구축, 암호화, 백업/성능 관리
- 5대 요소: 원칙·정책, 조직, 프로세스, 기술 도구, 성과 지표

3. 최신 트렌드: Data Mesh 기반 연합형 거버넌스(Federated Governance)
- 중앙은 보안/표준 가드레일(Policy as Code) 제공, 도메인은 Data Product 자율 운영
```
---

### 핵심 관계

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **연합형 거버넌스(Federated Governance)** | Data Mesh, 도메인 자율성, Policy as Code, 전사 공통 가드레일 | Ⅴ 운영모델, Ⅶ 결론 |
| **Data Steward의 역할** | 비즈니스 스튜어드, 테크니컬 스튜어드, 데이터 프로파일링, 표준화 전담 | Ⅲ 조직 체계 |
| **Policy as Code** | OPA(Open Policy Agent), CI/CD 보안 검증, ABAC 접근 제어 자동화 | Ⅳ·Ⅵ |

---

## 2~4교시 예상문제 (25점)

> 전사 데이터 사일로 해소 및 신뢰성 있는 AI 활용을 위한 데이터 거버넌스(Data Governance)의 개념, DAMA DMBOK 기반 프레임워크 5대 구성요소, 조직 체계(CDO, Owner, Steward, Custodian)의 R&R을 설명하고, Data Mesh 환경에서의 연합형 거버넌스(Federated Governance) 구축 방안을 제시하시오. (25점)

> (25점, 예상)

---

## 2~4교시 25점 답안

### 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| **연합형 거버넌스(Federated Governance)** | Data Mesh, 도메인 자율성, Policy as Code, 전사 공통 가드레일 | Ⅴ 운영모델, Ⅶ 결론 |
| **Data Steward의 역할** | 비즈니스 스튜어드, 테크니컬 스튜어드, 데이터 프로파일링, 표준화 전담 | Ⅲ 조직 체계 |
| **Policy as Code** | OPA(Open Policy Agent), CI/CD 보안 검증, ABAC 접근 제어 자동화 | Ⅳ·Ⅵ |

### Ⅰ. 데이터 자산의 지휘·통제 사령탑, 데이터 거버넌스의 개요

> 데이터 거버넌스는 데이터 자산의 비즈니스 가치 창출과 리스크 통제를 위한 전사 의사결정권 및 책임 규약임.

- 정의: 데이터의 가용성, 유용성, 무결성, 보안성을 보증하기 위해 전사적 차원에서 데이터 의사결정 권한(Decision Rights)과 책임(Accountability) 체계를 규정하고 실행하는 활동 (DAMA DMBOK 2.0 정의)
- 목적: 데이터 사일로 해소, 일관된 고품질 데이터 확보, 규제 준수(컴플라이언스) 및 데이터 자산 가치 극대화
- 관리(Data Management)와의 차이: 관리가 '데이터를 어떻게 수집·저장·운영할 것인가'의 실행 기술(Execution)이라면, 거버넌스는 '누가 어떤 원칙과 책임으로 의사결정할 것인가'의 지휘·통제(Command & Control) 체계임

### Ⅱ. 데이터 거버넌스 프레임워크 5대 핵심 구성요소

> 원칙, 조직, 프로세스, 기술 도구, 성과 관리가 유기적으로 결합되어 전사 데이터 문화를 조성함.

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 220" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <rect x="5" y="5" width="510" height="210" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Layer 1: Principles -->
    <rect x="15" y="15" width="490" height="32" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.2"/>
    <text x="35" y="35" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">1. 원칙 및 정책</text>
    <text x="130" y="35" font-size="7.5" fill="var(--color-text, #334155)">데이터 자산 소유권 규정, 공개 등급(기밀/대외비/공개), 수명주기 보존 지침</text>

    <!-- Layer 2: Organization -->
    <rect x="15" y="53" width="490" height="32" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="35" y="73" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">2. 조직 체계 및 R&amp;R</text>
    <text x="130" y="73" font-size="7.5" fill="var(--color-text, #334155)">거버넌스 위원회(CDO), Data Owner(도메인 책임), Steward(실무), Custodian(IT)</text>

    <!-- Layer 3: Process -->
    <rect x="15" y="91" width="490" height="32" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="35" y="111" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">3. 관리 프로세스</text>
    <text x="130" y="111" font-size="7.5" fill="var(--color-text, #334155)">데이터 요구 승인 워크플로우, 스키마 변경 통제, 품질 진단 및 에스컬레이션</text>

    <!-- Layer 4: Tech & Tools -->
    <rect x="15" y="129" width="490" height="32" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <text x="35" y="149" font-size="8" font-weight="bold" fill="var(--color-text, #1e293b)">4. 기술 및 도구</text>
    <text x="130" y="149" font-size="7.5" fill="var(--color-text, #334155)">메타데이터 카탈로그, Data Lineage 자동 수집, Policy as Code (OPA, ABAC)</text>

    <!-- Layer 5: Metrics & Maturity -->
    <rect x="15" y="167" width="490" height="32" rx="5" fill="var(--color-card-bg, #ffffff)" stroke="#16a34a" stroke-width="1.2"/>
    <text x="35" y="187" font-size="8" font-weight="bold" fill="#16a34a">5. 성과 및 성숙도</text>
    <text x="130" y="187" font-size="7.5" fill="var(--color-text, #334155)">품질 SLA 준수율, CMMI/DMM 성숙도 진단, 비즈니스 가치 환산 피드백 루프</text>
  </svg>
</div>

- **원칙 및 정책**: 전사 데이터 소유권, 공개 등급(기밀/대외비/공개), 데이터 생명주기 관리 지침 제정
- **조직 체계**: 의사결정 기구(CDO 주관 위원회)와 도메인 실무 책임자 간 명확한 RACI 책임 할당
- **관리 프로세스**: 표준 제정, 품질 이슈 보고, 데이터 접근 승인의 표준 워크플로우 운영
- **기술 인프라**: 수작업 관리를 탈피하고 메타데이터 수집, 계보 추적, 보안 검증을 자동화하는 플랫폼
- **성과 지표**: 거버넌스 성숙도 평가(DMM)를 통해 투자 대비 효익을 가시화하고 지속적 환류 수행

### Ⅲ. 거버넌스 조직 체계 및 핵심 역할(R&R) 비교

> 비즈니스 책임(Owner), 실무 표준화(Steward), 기술적 인프라(Custodian)의 3자 균형을 확립함.

| 조직 역할 | 주체 및 소속 | 핵심 임무 및 의사결정 권한 | 주요 산출물 |
|---|---|---|---|
| **데이터 거버넌스 위원회** | 최고데이터책임자(CDO), 각 사업부 임원 | 전사 데이터 전략 승인, 도메인 간 분쟁 조정, 예산 배분 | 전사 데이터 전략서, 정책 결의서 |
| **Data Owner (데이터 소유자)** | 비즈니스 도메인 부서장 (현업) | 도메인 데이터 정의, 접근 승인 권한, 품질 SLA 최종 책임 | 도메인 비즈니스 용어 정의서, 승인 이력 |
| **Data Steward (데이터 관리자)** | 비즈니스 도메인 실무자 | 데이터 표준화(단어/도메인), 프로파일링, 품질 개선 실행 | 데이터 표준사전, 품질 진단 보고서 |
| **Data Custodian (데이터 관리원)** | DBA, 데이터 엔지니어 (IT 전담 부서) | 데이터베이스 인프라 구축, 백업/복구, 암호화, 튜닝 | 물리 스키마 정의서, 인프라 성능 보고서 |

### Ⅳ. 중앙집중형 vs 분산형 vs 연합형(Federated) 운영 모델

> 연합형 모델은 공통 정책은 중앙에서, 도메인 데이터 판단은 현장에서 담당하여 통일성과 자율성을 절충함.

| 비교 항목 | 중앙집중형 (Centralized) | 분산형 (Decentralized) | 연합형 (Federated Governance) |
|---|---|---|---|
| **아키텍처 모델** | 전사 단일 데이터 레이크/DW | 도메인별 독립 데이터 마트 | Data Mesh 기반 도메인 분산 노드 |
| **의사결정 주체** | 중앙 CDO 및 전담 거버넌스 팀 | 각 사업부서별 독립 결정 | 중앙 위원회(공통) + 도메인 팀(자율) |
| **장점** | 전사 표준·보안 통일 | 도메인 판단 속도 | 공통 규칙·도메인 자율 절충 |
| **한계 및 단점** | 중앙 승인 병목 발생, 도메인 이해 부족 | 데이터 사일로 심화, 전사 정합성 상실 | 도메인 팀의 거버넌스 역량 및 자동화 도구 필수 |
| **적합 조직** | 금융, 공공 등 규제 중심 전통 기업 | 스타트업, 독립 사업부 체제 조직 | 대규모 클라우드 네이티브 엔터프라이즈 |

### Ⅴ. Data Mesh 환경의 연합형 거버넌스 아키텍처

> "자율성은 최대로, 공통 통제는 코드로 자동화(Automated Platform Guardrail)한다."

<div style="max-width: 520px; margin: 1rem auto;">
  <svg viewBox="0 0 520 200" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="fed-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="var(--color-primary, #2563eb)"/>
      </marker>
    </defs>
    <rect x="5" y="5" width="510" height="190" rx="8" fill="var(--color-bg-subtle, #f8fafc)" stroke="var(--color-border, #cbd5e1)" stroke-width="1.2"/>

    <!-- Central Governance -->
    <rect x="35" y="15" width="450" height="42" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-primary, #2563eb)" stroke-width="1.5"/>
    <text x="260" y="32" text-anchor="middle" font-size="8.5" font-weight="bold" fill="var(--color-primary, #2563eb)">중앙 거버넌스 협의회 (Global Governance Council)</text>
    <text x="260" y="46" text-anchor="middle" font-size="7" fill="var(--color-text-muted, #64748b)">공통 보안 Baseline, 표준 식별자 체계, Policy as Code (OPA) 자동 가드레일 배포</text>

    <!-- 2 Downward Arrows -->
    <line x1="140" y1="57" x2="140" y2="80" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#fed-arrow)"/>
    <line x1="380" y1="57" x2="380" y2="80" stroke="var(--color-primary, #2563eb)" stroke-width="1.5" marker-end="url(#fed-arrow)"/>
    <text x="260" y="73" text-anchor="middle" font-size="6.5" font-weight="bold" fill="var(--color-primary, #2563eb)">자동화된 정책 가드레일 (Policy as Code)</text>

    <!-- Domain A -->
    <rect x="25" y="82" width="220" height="95" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="25" y="82" width="220" height="20" rx="6" fill="var(--color-bg-subtle, #eff6ff)"/>
    <text x="135" y="96" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--color-primary, #2563eb)">[도메인 A] 주문·결제 도메인</text>
    <text x="35" y="115" font-size="7" fill="var(--color-text, #334155)">· Data Owner: 결제비즈니스 부서장</text>
    <text x="35" y="130" font-size="7" fill="var(--color-text, #334155)">· Data Steward: 거래 정합성 관리자</text>
    <text x="35" y="145" font-size="7" fill="var(--color-text, #334155)">· Data Product: 결제 원장 API 및 스트림</text>
    <text x="35" y="165" font-size="6.5" font-weight="bold" fill="#16a34a">[자율 운영 + 자체 CI/CD 게이트]</text>

    <!-- Domain B -->
    <rect x="275" y="82" width="220" height="95" rx="6" fill="var(--color-card-bg, #ffffff)" stroke="var(--color-border, #cbd5e1)" stroke-width="1"/>
    <rect x="275" y="82" width="220" height="20" rx="6" fill="var(--color-bg-subtle, #f0fdf4)"/>
    <text x="385" y="96" text-anchor="middle" font-size="8" font-weight="bold" fill="#16a34a">[도메인 B] 마케팅·추천 도메인</text>
    <text x="285" y="115" font-size="7" fill="var(--color-text, #334155)">· Data Owner: CRM 마케팅 부서장</text>
    <text x="285" y="130" font-size="7" fill="var(--color-text, #334155)">· Data Steward: 고객 행동 분석가</text>
    <text x="285" y="145" font-size="7" fill="var(--color-text, #334155)">· Data Product: 유저 선호 세그먼트</text>
    <text x="285" y="165" font-size="6.5" font-weight="bold" fill="#16a34a">[자율 운영 + 자체 CI/CD 게이트]</text>

    <!-- Center Lineage/Catalog link -->
    <line x1="245" y1="130" x2="273" y2="130" stroke="var(--color-primary, #2563eb)" stroke-width="1.2" stroke-dasharray="3,2"/>
    <text x="260" y="125" text-anchor="middle" font-size="6" fill="var(--color-text-muted, #64748b)">카탈로그</text>
  </svg>
</div>

### Ⅵ. 데이터 거버넌스 문제점·대응책

> 관료주의적 통제로 인한 분석 지연과 형식적 문서화를 방지함.

| 위험 | 대책 | 효과 |
|---|---|---|
| 현업 부서의 거버넌스 외면 및 책임 회피 | Data Steward 직무 공식화 및 도메인 데이터 품질 KPI 인사 반영 | 현업 주도의 능동적 데이터 정제 및 오너십 정착 |
| 수작업 승인으로 인한 분석 지연 | 속성 기반 접근제어(ABAC) 및 OPA 기반 정책 자동 승인 파이프라인 구현 | 반복 승인 대기 시간 제거 및 데이터 접근성 개선 |
| 시스템 변경 시 메타데이터 카탈로그 사장 | CI/CD 배포 파이프라인과 Data Lineage 자동 추출 도구 연동 | 메타데이터 최신성 100% 실시간 동기화 |
| 전사 데이터 거버넌스의 과도한 중앙 통제 | 중앙은 가드레일만 규정하고 도메인은 자율화하는 연합형 거버넌스 전환 | 병목 현상 해소 및 비즈니스 변화 대응력 극대화 |

### Ⅶ. 기술사적 제언: 통제의 족쇄에서 비즈니스 인에이블러(Enabler)로

### 학습자 통찰 메모 — 답안 밖

> **[핵심 통찰]**
> 데이터 거버넌스의 목적은 '데이터 사용을 금지하고 감시하는 경찰'이 아니라, '누구나 신뢰할 수 있는 데이터를 가장 빠르고 안전하게 쓰도록 돕는 안내자(Enabler)'가 되는 것이다. 수작업 승인 서류와 관료주의적 위원회에 의존하는 거버넌스는 데이터 분석을 마비시키고 개발자의 우회로(그림자 IT)를 낳는다. 성공적인 거버넌스는 **코드로 자동화된 정책(Policy as Code)**과 **도메인 자율성**이 결합된 연합형 거버넌스(Federated Governance)로 진화해야 한다.

> **[나라면 이렇게 쓴다]**
> 2교시 논술 문제라면 기존 중앙집중형 거버넌스의 실패 요인(중앙 승인 병목, 도메인 맥락 상실)을 지적하고, Data Mesh 기반의 **'연합형 컴퓨터 거버넌스(Federated Computational Governance)'**를 해법으로 제시하겠다. 중앙 CDO 협의회는 OPA(Open Policy Agent)를 통해 공통 보안·접근 가드레일을 코드로 배포하고, 도메인 팀은 Data Owner의 책임 아래 독립적인 Data Product를 생성·배포하는 자율 분산 운영 체계를 구체화하겠다.

### 실전 답안용 기술사적 제언

- **판정 기준**: 거버넌스 문서의 방대함보다 **Policy as Code 기반의 자동화 통제율**과 **도메인 Data Owner의 실질적 작동 여부**를 성공 판정 기준으로 확립.
- **대응 방안**: 중앙 가드레일 제정 $\rightarrow$ 도메인별 Owner/Steward 지정 $\rightarrow$ 전사 카탈로그 셀프서비스 개방 $\rightarrow$ CI/CD 정책 검증 자동화.
- **검증 체계**: 도메인별 Data Owner 지정률 100%, 데이터 접근 요청 자동 승인율 80% 이상, 메타데이터 현행화율 99% 달성 관제.
- **기대 효과**: 중앙 결재 병목과 데이터 사일로를 동시에 제거하고, 신뢰성 있는 AI 및 엔터프라이즈 실시간 의사결정 인프라 확립.

<div class="itpe-flow-map" role="img" aria-label="연합형 데이터 거버넌스 실행 파이프라인">
  <div class="itpe-flow-node">
    <strong>중앙 가드레일 제정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>규약</strong><span>보안 기준 및 Policy as Code 수립</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>도메인 Data Owner 지정</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>할당</strong><span>도메인 책임주의 및 Steward 배치</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node is-current">
    <strong>자동 승인 게이트</strong>
    <div class="itpe-step-detail">
      <strong>통제</strong><span>ABAC 자동화 승인율 &ge; 80%</span>
    </div>
  </div>
  <div class="itpe-flow-arrow">→</div>
  <div class="itpe-flow-node">
    <strong>Data Product 자율 개방</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>결과</strong><span>안전한 셀프서비스 데이터 분석</span></div>
    </div>
  </div>
</div>

---

## 출제 이력과 검증 출처

- **기출 근거**: 제124·127·130회는 KPC 보조자료이며 Q-Net 공식 원문 미확보
- **검증 출처**: [DAMA International DMBOK](https://www.dama.org/cpages/body-of-knowledge), [EDM Council DCAM](https://edmcouncil.org/frameworks/dcam/)

## 연결 토픽

- [데이터 품질관리](./003_data_quality_management.md) · [데이터 표준화](./008_data_standardization.md) · [MDM](./083_mdm.md) · [데이터 레이크](./007_data_lake.md)
