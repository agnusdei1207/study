---
title: "데이터 거버넌스(Data Governance)"
tags:
  - "notes-data"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="데이터 관리에서 전사 의사결정 및 데이터 거버넌스로 이어지는 지식 위치">
  <span>자료처리·데이터</span>
  <span>데이터 거버넌스·품질</span>
  <strong>데이터 거버넌스(Data Governance)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 기업의 데이터 자산에 대해 의사결정권(Decision Rights), 책임(Accountability), 관리 원칙을 정의하여, 데이터 활용 가치를 극대화하고 보안·컴플라이언스 리스크를 통제하는 전사적 운영 체계
- 5대 구성요소: 원칙·정책(Principle), 조직·책임(Organization), 프로세스(Process), 기술·도구(Technology), 성과관리(Metric)
- 운영 모델: 중앙집중형, 분산형, 연합형(Federated Governance)

<div class="itpe-flow-map" role="img" aria-label="데이터 거버넌스 의사결정 및 실행 프레임워크">
  <div class="itpe-flow-node"><strong>비즈니스 전략 및 컴플라이언스</strong><small>디지털 전환 · 개인정보보호법 · AI 윤리</small></div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>데이터 거버넌스 위원회 (CDO)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>원칙·정책</strong><span>데이터 소유권 · 접근 통제 · 보존 주기</span></div>
      <div class="itpe-flow-branch"><strong>표준·품질</strong><span>공통 메타데이터 · 용어사전 · DQM 규칙</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>도메인별 실행 조직 (R&R)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>Data Owner</strong><span>비즈니스 도메인 데이터 승인 및 최종 책임</span></div>
      <div class="itpe-flow-branch"><strong>Data Steward</strong><span>데이터 품질 측정 · 표준 준수 실무 관리</span></div>
      <div class="itpe-flow-branch"><strong>Data Custodian</strong><span>DBA · 인프라 엔지니어링 및 기술 지원</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node"><strong>지속적 성과 측정 (Data Maturity)</strong></div>
</div>

## 예상문제

> 전사 데이터 사일로 해소 및 신뢰성 있는 AI 활용을 위한 데이터 거버넌스(Data Governance)의 개념, DAMA DMBOK 기반 프레임워크 5대 구성요소, 조직 체계(CDO, Owner, Steward, Custodian)의 R&R을 설명하고, Data Mesh 환경에서의 연합형 거버넌스(Federated Governance) 구축 방안을 제시하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **연합형 거버넌스(Federated Governance)** | Data Mesh의 분산 도메인 자율성과 전사 공통 표준·보안 통제를 양립시키는 자동화 거버넌스 | Ⅴ 운영모델, Ⅶ 결론 |
| **Data Steward** | 현업 비즈니스 부서에서 데이터 정의, 품질 진단, 메타데이터 현행화를 전담하는 실무 책임자 | Ⅲ 조직 체계 |

## Ⅰ. 데이터 자산의 지휘·통제 사령탑, 데이터 거버넌스의 개요

> **한줄 요약:** 데이터 거버넌스는 데이터 자산의 비즈니스 가치 창출과 리스크 통제를 위한 전사 의사결정권 및 책임 규약임.

- 정의: 데이터의 가용성, 유용성, 무결성, 보안성을 보증하기 위해 전사적 차원에서 데이터 의사결정 권한(Decision Rights)과 책임(Accountability) 체계를 규정하고 실행하는 활동 (DAMA DMBOK 2.0 정의)
- 필요성: 시스템별 데이터 중복 및 불일치(사일로 심화), 데이터 소유권 불분명으로 인한 품질 저하 방치, 개인정보 유출 및 AI 편향 등 법적·윤리적 컴플라이언스 리스크 급증
- 데이터 관리(Data Management)와의 차이: 데이터 관리가 '어떻게 데이터를 수집·저장·처리할 것인가'라는 실행 기술(Execution)이라면, 거버넌스는 '누가 어떤 원칙과 권한으로 결정할 것인가'라는 통제 정책(Strategy & Control)임

## Ⅱ. 데이터 거버넌스의 5대 핵심 특징

> **한줄 요약:** 비즈니스 전략 정렬, 전 생명주기 통제, 다차원 R&R 분리, 자동화 플랫폼 지원을 특징으로 함.

| 특징 | 동작 원리 및 세부 내용 | 실무적 기여 |
|---|---|---|
| **전사 전략 정렬** | 데이터 전략을 조직의 경영 목표 및 디지털 전환(DX) 과제와 직접 연계 | 데이터 투자의 비즈니스 ROI 입증 |
| **책임성(Accountability)** | 데이터 도메인별 Owner 및 Steward를 지정하고 RACI 매트릭스 확립 | 데이터 품질 저하 및 보안 사고 시 즉각적 원인 규명 |
| **원칙 및 정책 기반** | 예외 처리가 아닌 사전 승인된 데이터 원칙(데이터 민주화, 보안 우선 등) 적용 | 부서 간 데이터 공유 시 불필요한 분쟁 차단 |
| **생명주기(Lifecycle) 통제** | 데이터의 생성 $\to$ 저장 $\to$ 공유 $\to$ 아카이빙 $\to$ 영구 폐기 전 단계 감사 추적 | 컴플라이언스 준수 증빙 및 스토리지 비용 절감 |
| **플랫폼 기반 자동화** | 데이터 카탈로그, 계보(Lineage), 자동 태깅 솔루션을 거버넌스에 결합 | 수작업 규정 준수 검토의 한계 극복 |

## Ⅲ. DAMA DMBOK 기반 거버넌스 5대 구성요소 및 조직 체계

> **한줄 요약:** 원칙, 조직, 프로세스, 기술, 성과의 5대 요소와 CDO 중심의 3계층 조직이 상호 연동됨.

<div class="itpe-pipeline" role="img" aria-label="데이터 거버넌스 5대 구성요소">
  <div class="itpe-pipeline-node"><strong>원칙·정책</strong><small>데이터 헌장 · 지침</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>조직·R&R</strong><small>위원장 · Owner · Steward</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>프로세스</strong><small>표준 · 품질 · 변경</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>기술·도구</strong><small>Catalog · Lineage</small></div>
  <div class="itpe-pipeline-arrow">→</div>
  <div class="itpe-pipeline-node"><strong>성과·감사</strong><small>성숙도 · DQI 모니터링</small></div>
</div>

| 역할 | 소속 및 직무 권한 | 주요 책임 및 활동 |
|---|---|---|
| **데이터 거버넌스 위원회 (CDO)** | 전사 최고 경영진 및 사업본부장 | 전사 데이터 전략 수립, 예산 배분, 데이터 소유권 분쟁 최종 중재 |
| **Data Owner (데이터 소유자)** | 비즈니스 부서장 (영업, 마케팅, 여신 등) | 해당 도메인 데이터의 비즈니스 정의, 접근 권한 승인, 품질 최종 책임 |
| **Data Steward (데이터 관리자)** | 도메인 실무 리더 및 데이터 분석가 | 표준 단어/도메인 정의, 품질 측정 지표 수립, 메타데이터 카탈로그 현행화 |
| **Data Custodian (데이터 수탁자)** | IT 인프라팀, DBA, 데이터 엔지니어 | 물리 DB 구축, 백업/복구, 암호화, 접근제어(RBAC/ABAC) 기술 구현 |

## Ⅳ. 데이터 거버넌스 5단계 구축 절차

> **한줄 요약:** 현황 진단에서 비전 수립, 조직/정책 설계, 핵심 도메인 파일럿, 전사 확산으로 순차 진행함.

| 단계 | 활동 내용 | 주요 산출물 |
|---|---|---|
| **1. 현황 및 성숙도 진단** | 데이터 사일로 수준, 품질 오류율, 규제 위험 평가, CMMI 진단 | 거버넌스 성숙도 평가서 |
| **2. 비전 및 원칙 수립** | 전사 데이터 헌장, 거버넌스 로드맵, 핵심 성공요소(CSF) 도출 | 데이터 전략 로드맵 |
| **3. 조직 체계 및 정책 설계** | 거버넌스 위원회 규정, Data Owner/Steward 지정, RACI 매트릭스 확립 | 거버넌스 운영 규정집 |
| **4. 파일럿 적용 및 도구 구축** | 핵심 데이터(CDE) 대상 데이터 카탈로그 및 DQM 솔루션 구축 | 데이터 표준사전, 카탈로그 |
| **5. 전사 확산 및 성과 환류** | 전 도메인 확산, 분기별 DQI 평가, 감사 및 정책 지속 개정 | 데이터 거버넌스 성과보고서 |

## Ⅴ. 중앙집중형 vs 분산형 vs 연합형(Federated) 거버넌스 비교

> **한줄 요약:** 전통적 중앙집중형의 병목과 분산형의 무질서를 극복하기 위해 연합형(Data Mesh) 거버넌스가 부상함.

| 구분 | 중앙집중형 거버넌스 | 분산형 거버넌스 | 연합형 거버넌스 (Federated Governance) |
|---|---|---|---|
| **운영 주체** | 중앙 CDO 및 전사 데이터 거버넌스 전담팀 | 각 비즈니스 부서 자율 운영 | 도메인별 소유권 + 중앙 연합 협의체 |
| **장점** | 강력한 표준 준수 및 일관된 보안 통제 | 현업 요구에 대한 신속한 대응 및 민첩성 | 도메인의 자율성과 전사적 상호운용성(Interoperability) 양립 |
| **단점** | 중앙 부서 병목으로 인한 신규 분석 지연 | 데이터 사일로 재발 및 전사 표준 파손 | 플랫폼 기반 자동화(Policy as Code) 인프라 구축 난이도 높음 |
| **적용 환경** | 금융·공공 등 규제 중심 전통적 엔터프라이즈 | 신속한 실험이 중요한 초기 스타트업 | 대규모 MSA 및 Data Mesh 아키텍처 도입 기업 |

## Ⅵ. 실무 고려사항 및 구축 실패 방지 대책

> **한줄 요약:** 관료주의적 문서화를 배제하고 메타데이터 플랫폼 자동화와 인센티브 제도로 현업 참여를 견인함.

- 적용 상황: 글로벌 제조/유통 기업의 전사 데이터 레이크하우스 거버넌스 재구축

| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| **현업의 거버넌스 외면** | 데이터 입력·정의 부담 전가 및 현업 KPI 미반영 | Data Steward 직무 공식화 및 인사 평가 가점 부여 | 현업 주도적 데이터 품질 관리 활성화 |
| **승인 절차에 따른 분석 지연** | 모든 데이터 접근 요청을 수작업 결재로 처리 | ABAC(속성기반 접근제어) 및 정책 기반 자동 승인 파이프라인 도입 | 데이터 조회 리드타임 획기적 단축 |
| **메타데이터 카탈로그 사장** | 시스템 변경 시 카탈로그 수동 업데이트 누락 | CI/CD 파이프라인과 Data Lineage 자동 추출 도구 연동 | 메타데이터 최신성 100% 실시간 유지 |

## Ⅶ. 결론 및 기술사적 제언

> **한줄 요약:** 데이터 거버넌스는 규제와 통제의 족쇄가 아니라 데이터를 자산으로 만드는 인에이블러(Enabler)여야 함.

- [핵심 통찰]: 과거의 데이터 거버넌스가 '데이터를 사용하지 못하게 잠그는 보안 경찰' 역할이었다면, 현대의 거버넌스는 '누구나 믿을 수 있는 데이터를 찾아 즉시 활용하게 돕는 신뢰 플랫폼'이어야 함. 거버넌스가 개발 생산성을 저해하면 구성원들은 섀도우 IT(Shadow IT)로 이탈함.
- 나라면: Data Mesh 패러다임에 맞춰 'Federated Computational Governance'를 구축하고, OpenLineage와 dbt를 활용해 데이터 계약(Data Contract) 검증 및 보안 마스킹 정책을 코드화(Policy-as-Code)하여, 배포 파이프라인 내에서 거버넌스 규칙이 사람의 개입 없이 자동으로 강제되도록 구현하겠음.

## 1교시 10점 답안 발췌

### 1. 정의 및 핵심 개념
- 데이터 거버넌스는 전사 데이터 자산의 가치 창출과 리스크 통제를 위해 의사결정권(Decision Rights)과 책임(Accountability) 체계를 규정한 전사 운영 프레임워크임.

### 2. 핵심 메커니즘 / 체계
```text
[CDO 위원회] 전략·정책 수립
     │
     ▼
[도메인] Data Owner (승인) ─ Data Steward (품질/표준) ─ Custodian (DBA)
     │
     ▼
[기술] Data Catalog + Lineage + Automated Policy (Policy-as-Code)
```
- 원칙, 조직, 프로세스, 기술, 성과 5대 요소를 기반으로 운영됨.

### 3. 차별화 제언
- 중앙집중형 병목을 해소하기 위해 Data Mesh 기반 연합형 거버넌스(Federated Governance)와 정책의 코드화(Policy as Code)를 구현해야 함.

## 출제 이력과 검증 출처

- 출제 이력: 제130회·127회·124회 KPC 모의고사, 제114회 기출
- 검증 출처: DAMA International 'DAMA-DMBOK 2.0 (Data Management Body of Knowledge)', 한국데이터산업진흥원

## 학습 체크

- [ ] 데이터 거버넌스와 데이터 관리(Data Management)의 차이를 설명할 수 있는가?
- [ ] DAMA DMBOK 기반 거버넌스 5대 구성요소와 조직별 R&R(Owner, Steward 등)을 제시할 수 있는가?
- [ ] 중앙집중형, 분산형, 연합형(Federated) 거버넌스의 장단점을 비교할 수 있는가?

## 연결 토픽

- 이전 토픽: [군집분석(Clustering)](./005_cluster_analysis.md)
- 연관 토픽: [데이터 품질관리](./003_data_quality_management.md), [데이터 표준화](./008_data_standardization.md), [MDM](./083_mdm.md)
- 다음 토픽: [데이터 레이크(데이터 늪 포함)](./007_data_lake.md)
