---
title: "요구사항 추적표(Requirement Traceability Matrix)"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
extra:
  model: "Gemini 3.8 Flash (High)"
author: "Antigravity"
lastModified: "2026-03-30T10:00:00+09:00"
---

## 큰 그림과 30초 인출

- **본질**: 고객의 초기 요구사항부터 시스템 설계, 소스코드 모듈, 테스트 케이스까지 SDLC 전 단계 산출물을 고유 식별자(ID)로 상호 연결하여, 기능 누락과 불필요한 군더더기 개발(Gold Plating)을 방지하는 추적 공학 매트릭스이다.
- **메커니즘**: 요구사항 고유 ID 부여 $\rightarrow$ 설계/코드/테스트 산출물 1:N 매핑 $\rightarrow$ 정방향 추적(누락 차단) 및 역방향 추적(고아 코드 차단) $\rightarrow$ 요구사항 변경 시 영향 범위(Impact) 산출 순으로 제어한다.
- **산출물**: 요구사항 추적표(RTM), 양방향 추적성 보고서, 변경 영향도 분석서, 프로젝트 감리 적합성 증빙.

<div class="itpe-flow">
  <div class="itpe-flow-steps">
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>1. 요구사항 ID화</strong></span>
      <div class="itpe-step-detail">RFP 및 SRS 기반 기능/비기능 요구사항 고유 ID 부여</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>2. 설계·구현 매핑</strong></span>
      <div class="itpe-step-detail">UML 모델(클래스/시퀀스) 및 소스코드 파일 매핑</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node">
      <span class="itpe-keyword"><strong>3. 테스트 케이스 연계</strong></span>
      <div class="itpe-step-detail">단위/통합/인수 테스트 시나리오 및 통과 여부 연결</div>
    </div>
    <div class="itpe-flow-arrow">→</div>
    <div class="itpe-flow-node is-current">
      <span class="itpe-keyword"><strong>Quality Gate</strong></span>
      <div class="itpe-step-detail"><strong>판정 질문</strong><span>모든 요구사항이 테스트까지 양방향 추적되고 미매핑 항목이 0건인가?</span></div>
      <div class="itpe-flow-branches">
        <div class="itpe-flow-branch"><strong>통과</strong><span>베이스라인 확정 및 개발 단계 승인</span></div>
        <div class="itpe-flow-branch"><strong>미통과</strong><span>누락·중복 제거 및 산출물 보완 매핑</span></div>
      </div>
    </div>
  </div>
</div>

---

## 핵심 메커니즘

### (1) 정방향 추적성(Forward) vs 역방향 추적성(Backward)

| 구분 | 정방향 추적성 (Forward Traceability) | 역방향 추적성 (Backward Traceability) |
|---|---|---|
| **추적 방향** | **요구사항 $\rightarrow$ 설계 $\rightarrow$ 소스코드 $\rightarrow$ 테스트 케이스** | **테스트 케이스 $\rightarrow$ 소스코드 $\rightarrow$ 설계 $\rightarrow$ 요구사항** |
| **핵심 목적** | **요구사항의 구현 누락 방지 (완전성, Completeness)** | **불필요한 기능(Gold Plating) 및 고아 산출물 방지** |
| **판정 질문** | "발주자가 요청한 기능이 빠짐없이 설계되고 테스트되었는가?" | "현재 작성된 코드와 테스트가 어떤 요구사항을 위해 존재하는가?" |
| **결함 유형** | **미구현 결함(Missing Feature)** | **고아 산출물(Orphan Artifact), 범위 크립(Scope Creep)** |

### (2) 요구사항 추적표(RTM) 표준 구성 체계

| 요구사항 ID | 요구사항 명세 | 설계 ID | 소스코드 ID | 테스트 케이스 ID | 검증 상태 |
|---|---|---|---|---|---|
| **REQ-001** | 사용자 생체 인증 로그인 | DSN-101 (아키텍처)<br>DSN-102 (화면) | `AuthService.java`<br>`LoginView.vue` | TC-001 (단위)<br>TC-002 (통합) | 통과 (Pass) |
| **REQ-002** | 해외 결제 이상 탐지 | DSN-201 (FDS 모델) | `FdsEngine.py` | TC-010 (E2E) | 진행 중 |

### (3) 변경 영향도 분석(Impact Analysis) 나침반
- 프로젝트 진행 도중 고객의 요구사항 변경 요청(CR)이 발생했을 때, RTM을 통해 해당 요구사항과 연결된 **설계 클래스, 수정 대상 소스코드 파일, 재실행해야 할 회귀 테스트 케이스 목록**을 즉시 식별하여 공수와 리스크를 사전에 정량 산출함.

---

## 실무 적용 및 도입 체크리스트

1. **식별자 체계 표준화**: 요구사항(REQ), 아키텍처(ARC), 상세설계(DSN), 프로그램(SRC), 테스트(TC) 간 계층적 ID 명명 규칙이 수립되어 있는가?
2. **미할당 및 고아 산출물 제로화**: 하위 설계로 이어지지 않는 요구사항(누락 결함)이나 상위 요구사항이 없는 임의의 코드(고아 코드)가 0건인지 주기적으로 검증하는가?
3. **ALM 도구 자동 연계**: 엑셀 수작업 대신 Jira, Confluence, Git 저장소(GitLab/GitHub)를 연동하여 커밋 메시지에 요구사항 ID 기재 시 RTM이 실시간 자동 갱신되는가?
4. **단계별 검수 마일스톤 필수 산출물 지정**: 설계 완료, 개발 완료, 시험 완료 시점마다 감리 및 발주자 품질 게이트 통과 기준으로 RTM 최신화를 강제하고 있는가?

---

## 실패 시나리오 및 트러블슈팅

| 위험 | 대책 | 효과 |
|---|---|---|
| **인수 테스트 단계에서 핵심 요구사항 미구현 뒤늦게 발견** | 단계별 RTM 정방향 추적성 전수 점검 및 미매핑 항목 품질 게이트 차단 | 요구사항 구현 누락률 0% 달성 및 납기 지연 방지 |
| **요구사항 1건 변경 시 수정 모듈 파악에 수주일 소요** | ALM 도구(Jira-GitLab) 기반 역방향 RTM 자동화 파이프라인 구축 | 변경 영향도 분석 시간 2주에서 1시간 이내로 단축 |
| **감리 직전 수작업 엑셀 짜맞추기로 RTM 고아화** | Git 커밋 시 REQ 번호 검증(Commitlint) 및 Living RTM 자동 배포 | RTM 현행화 공수 80% 절감 및 실시간 감사 증적 확보 |

---

## 차세대 확장 및 융합

- **Living RTM (살아있는 추적성 파이프라인)**: 정적인 스프레드시트 작성을 탈피하여, 개발자가 Git 커밋 메시지와 PR에 이슈 키를 태깅하면 CI/CD 빌드 시점에 자동으로 요구사항-코드-테스트 매핑 웹 리포트가 생성되는 Living RTM 체계가 확산되고 있다.
- **AI 기반 요구사항 매핑 및 누락 탐지**: 대규모 자연어 SRS 문서와 소스코드를 LLM 임베딩 벡터로 분석하여, 의미론적으로 연결되지 않은 요구사항이나 누락된 테스트 케이스를 자동으로 찾아내어 매핑을 추천하는 AI ALM 기술이 도입되고 있다.

---

## 25점형 실전 답안 프레임워크

### 1단락: 요구사항 추적표(RTM)의 등장 배경 및 개념
- **배경**: 시스템 복잡도 증가에 따라 개발 진행 중 요구사항 누락 및 통제되지 않은 코드(Gold Plating) 삽입으로 인한 프로젝트 실패 방지.
- **정의**: 요구사항부터 설계, 구현, 시험까지 SDLC 전 과정 산출물의 연결 관계를 고유 ID로 명시하여 개발 완전성을 보증하는 매핑 매트릭스.

### 2단락: 양방향 추적성 구조 및 RTM 핵심 구성 요소
- **양방향 추적성 구조도**: REQ $\rightarrow$ DSN $\rightarrow$ SRC $\rightarrow$ TC (정방향: 완전성) $\leftrightarrow$ TC $\rightarrow$ SRC $\rightarrow$ DSN $\rightarrow$ REQ (역방향: 순수성).
- **RTM 표준 테이블 레이아웃**: 요구사항 ID, 요구명세, 설계 산출물, 소스 모듈, 테스트 케이스 ID, 검증 상태.
- **변경 영향도 분석(Impact Analysis) 메커니즘**: 요구사항 변경 시 영향받는 코드 및 테스트 범위 산출 원리.

### 3단락: 실무 적용 실패 방지를 위한 Living RTM 구축 방안
- **엑셀 수작업 문서의 고아화 극복**: 개발 현실과 문서의 불일치를 해결하기 위한 도구(Jira, Confluence, Git) 연계.
- **Commitlint 및 CI 파이프라인 연계**: 소스 커밋 시 요구사항 ID 입력을 강제하고 배포 시 RTM 대시보드 자동 렌더링.

### 4단락: 프로젝트 성공을 위한 기술사적 품질 거버넌스 제언
- **사후 감리 통과용 RTM 날조 관행 근절**: 납품 직전 외주 인력을 투입해 가짜 ID를 끼워맞추는 악습을 타파하고, 마일스톤별 양방향 추적성 통과율 100%를 다음 단계 착수의 필수 Quality Gate로 엄격 집행할 것을 제언함.

---

## 10점형 핵심 요약

1. **정의**: 요구사항부터 설계, 소스코드, 테스트 케이스까지의 산출물 관계를 고유 ID로 연결하여 완전성을 입증하는 공학 매트릭스.
2. **핵심 기능**:
   - **정방향 추적성**: 요구사항 구현 누락 차단 (완전성).
   - **역방향 추적성**: 고아 코드 및 불필요한 기능(Gold Plating) 차단 (순수성).
3. **실무 핵심**: 엑셀 수작업 작성을 배제하고, ALM 및 Git 커밋 린터와 연동된 실시간 'Living RTM' 파이프라인으로 운영함.
