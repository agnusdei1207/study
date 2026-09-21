---
title: "화이트박스 테스트(White Box Test)"
author: "Antigravity"
date: "2026-09-20T23:49:42+09:00"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "A"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "A"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="소프트웨어 공학에서 테스트·검증을 거쳐 화이트박스 테스트로 이어지는 지식 위치">
  <span>소프트웨어 공학</span>
  <span>테스트·검증</span>
  <strong>화이트박스 테스트(White Box Test)</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **화이트박스 테스트(White-box Testing)**는 소스코드 내부 논리 구조와 제어 흐름을 직접 분석하여 모든 실행 경로의 정확성을 검증하는 구조 기반 테스트
- 메커니즘: **제어 흐름 그래프(CFG)** 도출 → 테스트 커버리지 기준 선정(구문, 결정, 조건, **MC/DC**) → 입력 케이스 생성
- 산출/효과: 미실행 데드코드(Dead Code) 적발 · 내부 로직 오류 및 메모리 누수 격리 · 고신뢰성 안전 등급 보증

<div class="itpe-flow-map" role="img" aria-label="화이트박스 테스트 제어 흐름 분석도">
  <div class="itpe-flow-node"><strong>소스코드 분석</strong><div class="itpe-step-detail"><span>AST 및 제어 흐름 파악</span></div></div>
  <div class="itpe-flow-arrow">→ 그래프 모델링 →</div>
  <div class="itpe-flow-node is-current">
    <strong>제어 흐름 그래프(CFG)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>구문 커버리지</strong><span>모든 문장 최소 1회 실행</span></div>
      <div class="itpe-flow-branch"><strong>결정 커버리지</strong><span><span class="itpe-keyword"><strong>분기 참/거짓 최소 1회</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>MC/DC</strong><span><span class="itpe-keyword"><strong>개별 조건식 독립 영향력 검증</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">→ 경로 기반 테스트 도출 →</div>
  <div class="itpe-flow-node"><strong>테스트 스위트</strong><div class="itpe-step-detail"><span>미실행 경로 제로화 달성</span></div></div>
</div>

<details>
<summary>핵심 용어</summary>

- **White-box Testing**: 소스코드의 내부 구조, 루프, 조건 분기, 데이터 흐름을 직접 관찰하며 테스트 케이스를 설계하는 기법
- **CFG(Control Flow Graph)**: 프로그램의 실행 흐름을 노드(기본 블록)와 엣지(제어 이동)로 표현한 방향 그래프
- **Statement Coverage(구문 커버리지, C0)**: 소스코드의 모든 실행 가능한 문장이 최소 한 번 실행되는 비율
- **Branch/Decision Coverage(결정 커버리지, C1)**: 프로그램 내 모든 조건문의 전체 결과(True/False)가 최소 한 번씩 실행되는 비율
- **MC/DC(Modified Condition/Decision Coverage)**: 복합 조건식 내 각 개별 조건이 다른 조건과 무관하게 전체 결정 결과에 독립적인 영향을 미치는지 검증하는 기법 (항공 DO-178C Level A 표준)

</details>

## 예상문제

> 화이트박스 테스트(White-box Testing)의 개념과 특징을 설명하고, 제어 흐름 기반 커버리지 5단계(구문, 결정, 조건, 조건/결정, MC/DC)의 포함 관계 및 복합 조건식 예제를 통해 MC/DC의 테스트 케이스 도출 원리를 제시하시오. (25점)

## Ⅰ. 내부 로직의 무결성을 입증하는 화이트박스 테스트의 개요

> 소스코드를 보지 않는 블랙박스 테스트로는 숨겨진 악성 로직이나 실행 불가능한 데드코드를 결코 찾아낼 수 없다.

- 정의: 소프트웨어 내부 소스코드의 **논리적 구조, 제어 흐름(Control Flow), 데이터 흐름(Data Flow)**을 분석하여 모든 실행 경로의 정확성을 검증하는 **구조 기반 테스트 기법**
- 목적: 미실행 코드(Dead Code) 제거, 무한 루프 등 제어 흐름 결함 적발 및 경계 조건의 논리 오류 조기 차단

## Ⅱ. 제어 흐름 테스트 커버리지 5단계 체계 및 포함 관계

> 커버리지 기준의 포함 관계를 구분하되, 높은 커버리지를 결함 부재의 증거로 오인하지 않아야 함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="화이트박스 커버리지 계층도">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>1. 구문 커버리지 (Statement, C0)</strong></span>
    <div class="itpe-step-detail"><strong>문장 실행</strong><span>모든 실행 가능한 문장(Statement)을 최소 1회 실행</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓ 포함 (상위 커버리지)</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>2. 결정/분기 커버리지 (Decision/Branch, C1)</strong></span>
    <div class="itpe-step-detail"><strong>분기 실행</strong><span>모든 조건문의 참(True)/거짓(False) 분기 전체를 최소 1회 실행</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>3. 조건 커버리지 (Condition, C2)</strong></span>
    <div class="itpe-step-detail"><strong>조건 실행</strong><span>복합 조건식 내부의 각 개별 조건이 참/거짓을 최소 1회 만족</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓ 결합</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>4. 조건/결정 커버리지 (Condition/Decision)</strong></span>
    <div class="itpe-step-detail"><strong>조건·분기 동시</strong><span>개별 조건 참/거짓 + 전체 결정 참/거짓을 동시에 만족</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓ 실용적 최적화</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>5. MC/DC (Modified Condition/Decision)</strong></span>
    <div class="itpe-step-detail"><strong>독립 영향력</strong><span>N+1개 케이스로 각 개별 조건의 독립적 영향력 증명</span></div>
  </div>
</div>

### 제어 흐름 그래프(CFG) 및 커버리지 검증 스펙트럼

<div class="itpe-svg-wrapper">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" class="itpe-svg">
    <!-- Background -->
    <rect width="520" height="220" fill="var(--sl-color-bg-subtle, #f8fafc)" rx="8" />
    
    <!-- Left: CFG Diagram -->
    <text x="25" y="24" class="itpe-svg-label" fill="var(--sl-color-text-accent, #2563eb)">[제어 흐름 그래프(CFG) 모델링]</text>
    
    <!-- Node 1: Entry/Stmt -->
    <circle cx="120" cy="48" r="14" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="2" />
    <text x="120" y="52" class="itpe-svg-sub" font-size="11" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">1</text>
    
    <!-- Flow arrow down -->
    <line x1="120" y1="62" x2="120" y2="82" stroke="var(--sl-color-text-muted, #94a3b8)" stroke-width="1.5" />

    <!-- Node 2: Decision (Diamond/Circle) -->
    <polygon points="120,84 146,104 120,124 94,104" fill="var(--sl-color-bg-accent, #eff6ff)" stroke="var(--sl-color-accent, #8b5cf6)" stroke-width="1.5" />
    <text x="120" y="108" class="itpe-svg-sub" font-size="11" font-weight="700" fill="var(--sl-color-accent, #8b5cf6)" text-anchor="middle">2: If</text>

    <!-- Branch True (Left) -->
    <line x1="94" y1="104" x2="60" y2="135" stroke="var(--sl-color-success, #10b981)" stroke-width="1.5" />
    <text x="66" y="115" class="itpe-svg-label" font-size="10" fill="var(--sl-color-success, #10b981)">True</text>
    <circle cx="60" cy="145" r="12" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.5" />
    <text x="60" y="149" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text, #334155)" text-anchor="middle">3</text>

    <!-- Branch False (Right) -->
    <line x1="146" y1="104" x2="180" y2="135" stroke="var(--sl-color-danger, #ef4444)" stroke-width="1.5" />
    <text x="175" y="115" class="itpe-svg-label" font-size="10" fill="var(--sl-color-danger, #ef4444)">False</text>
    <circle cx="180" cy="145" r="12" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.5" />
    <text x="180" y="149" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text, #334155)" text-anchor="middle">4</text>

    <!-- Merge to Node 5 -->
    <line x1="60" y1="157" x2="110" y2="185" stroke="var(--sl-color-text-muted, #94a3b8)" stroke-width="1.5" />
    <line x1="180" y1="157" x2="130" y2="185" stroke="var(--sl-color-text-muted, #94a3b8)" stroke-width="1.5" />
    <circle cx="120" cy="192" r="14" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="2" />
    <text x="120" y="196" class="itpe-svg-sub" font-size="11" font-weight="700" fill="var(--sl-color-primary, #3b82f6)" text-anchor="middle">5</text>

    <!-- Right: Coverage Levels Spectrum -->
    <text x="245" y="24" class="itpe-svg-label" fill="var(--sl-color-text-accent, #2563eb)">[커버리지 검증 기준 비교]</text>

    <!-- Level 1: C0 -->
    <rect x="245" y="42" width="255" height="46" rx="5" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-border, #cbd5e1)" stroke-width="1.2" />
    <text x="255" y="60" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-text, #1e293b)">C0 구문(Statement) 커버리지</text>
    <text x="255" y="76" class="itpe-svg-sub" font-size="10.5" fill="var(--sl-color-text-muted, #64748b)">모든 실행 문장 1회 이상 통과 (최소 기준)</text>

    <!-- Level 2: C1 -->
    <rect x="245" y="96" width="255" height="46" rx="5" fill="var(--sl-color-bg, #fff)" stroke="var(--sl-color-primary, #3b82f6)" stroke-width="1.2" />
    <text x="255" y="114" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-primary, #3b82f6)">C1 결정(Decision/Branch) 커버리지</text>
    <text x="255" y="130" class="itpe-svg-sub" font-size="10.5" fill="var(--sl-color-text-muted, #64748b)">모든 분기의 True/False 경로 최소 1회 실행</text>

    <!-- Level 3: MC/DC -->
    <rect x="245" y="150" width="255" height="52" rx="5" fill="var(--sl-color-bg-accent, #eff6ff)" stroke="var(--sl-color-accent, #8b5cf6)" stroke-width="1.5" />
    <text x="255" y="168" class="itpe-svg-title" font-size="12" font-weight="700" fill="var(--sl-color-accent, #8b5cf6)">MC/DC (N+1 최적화 검증)</text>
    <text x="255" y="184" class="itpe-svg-sub" font-size="10.5" fill="var(--sl-color-text, #334155)">각 개별 조건의 독립적 영향력 입증</text>
    <text x="255" y="196" class="itpe-svg-sub" font-size="10" fill="var(--sl-color-text-muted, #64748b)">항공(DO-178C Level A), 차량(ISO 26262 ASIL-D)</text>
  </svg>
</div>

| 커버리지 유형 | 핵심 정의 | 최소 필요 케이스 수 | 특징 및 한계 |
|---|---|---|---|
| **구문(C0)** | 실행 문장 1회 실행 | 최소 | 분기문의 반대쪽 경로 미실행 위험 |
| **결정(C1)** | 전체 조건문 True/False 1회 실행 | 중간 | 개별 조건의 결함 간과 가능 |
| **조건(C2)** | 개별 조건 True/False 1회 실행 | 중간 | 전체 조건문 결과가 True/False 둘 다 안 될 수 있음 |
| **조건/결정** | C1과 C2를 동시 만족 | 중간~높음 | 조건 간 독립성 미보증 |
| **다중 조건(MCC)** | 개별 조건의 모든 가능한 조합(2^N) | 2^N (조합 폭발) | 완벽하나 케이스 폭증으로 실무 적용 불가 |
| **MC/DC** | 개별 조건의 독립적 영향력 검증 | **N + 1 개** | 항공(DO-178C), 차량(ISO 26262) 기능안전 표준 채택 |

## Ⅲ. MC/DC 테스트 케이스 도출 원리: `(A OR B) AND C`

> MC/DC는 각 원자 조건이 결정 결과에 독립적으로 영향을 줌을 보이며, 최소 N+1 사례가 가능한 경우에도 식 구조·결합 조건에 따라 추가 사례가 필요함.

### 조건식: `Result = (A OR B) AND C`

1. **A의 독립성 검증 조건**: B는 False, C는 True로 고정하고 A를 True/False로 변경했을 때 Result가 바뀌는지 확인
   - 케이스 1: `A=True, B=False, C=True` → Result = **True**
   - 케이스 2: `A=False, B=False, C=True` → Result = **False** (쌍 {1, 2})
2. **B의 독립성 검증 조건**: A는 False, C는 True로 고정하고 B를 True/False로 변경
   - 케이스 3: `A=False, B=True, C=True` → Result = **True**
   - 케이스 2와 비교: `A=False, B=False, C=True` → Result = **False** (쌍 {3, 2})
3. **C의 독립성 검증 조건**: (A OR B)를 True로 고정하고 C를 True/False로 변경
   - 케이스 4: `A=True, B=False, C=False` → Result = **False**
   - 케이스 1과 비교: `A=True, B=False, C=True` → Result = **True** (쌍 {1, 4})
- **최종 도출된 최소 테스트 슈트**: 케이스 1, 2, 3, 4 (총 4개 = N+1개로 증명 완료)

## Ⅳ. 화이트박스 테스트 문제점·대응책

> 단위 테스트 프레임워크와 정적/동적 분석 도구를 CI/CD 파이프라인에 결합하여 커버리지를 지속 측정한다.

### 화이트박스 도구 분류

| 도구 분류 | 대표 도구 | 주 검증 내용 |
|---|---|---|
| **코드 커버리지 분석** | JaCoCo, Cobertura, Istanbul | 구문(C0), 브랜치(C1) 커버리지 백분율 측정 |
| **정적 코드 분석** | SonarQube, Fortify, Coverity | 코딩 표준 준수, 널 참조, 잠재적 런타임 오류, 보안 취약점 |
| **기능안전 전문 도구** | VectorCAST, LDRA, Cantata | 임베디드 대상 MC/DC 커버리지 자동 측정 및 리포팅 |

### 실무 위험 및 거버넌스 대책

| 위험 | 대책 | 효과 |
|---|---|---|
| **C0(구문) 편중으로 인한 분기 누락** | 단순 구문 측정을 지양하고 **결정 커버리지(C1) 80% 이상** 강제 | `else` 누락 등 미실행 분기 결함 적발 |
| **복합 조건식 조합 폭발(2^N)** | 안전 필수 시스템 대상 **MC/DC(N+1개 케이스)** 검증 적용 | 최소 비용으로 다중조건 수준의 신뢰성 확보 |
| **테스트 코드 유지보수 부채** | 내부 구현 종속적 테스트 지양, 행위 기반 검증 및 Mocking 최소화 | 리팩토링 시 테스트 깨짐 방지 및 유지보수성 향상 |

## Ⅴ. 구조·명세 상호보완 검증의 결론

> 100% 구문 커버리지가 무결함을 의미하지 않으며, 요구사항 명세 검증(블랙박스)과의 결합이 필수적이다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 구문 커버리지(C0) 100%는 단순한 최소 조건일 뿐임. `if (a > 0)`에서 `else` 블록이 누락된 경우 C0는 100%가 나오지만 심각한 분기 누락 버그가 존재함. 따라서 상용 시스템에서는 최소한 결정 커버리지(C1) 80% 이상, 안전 필수(Safety-critical) 시스템에서는 MC/DC를 필히 강제해야 함.
- 나라면: 자율주행, 철도, 의료기기 프로젝트 수행 시 ISO 26262 ASIL-D 수준을 만족하도록 전문 동적 검증 도구(VectorCAST)를 도입하여 단위/통합 테스트에서 MC/DC 100%를 통과 기준선(Quality Gate)으로 설정하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: 시스템 위험 등급(기능안전 ASIL, SIL)에 따른 차등 커버리지 목표선 설정 (일반: C1 80%, 안전 필수: MC/DC 100%)
- **대응 방안**: **MC/DC(N+1)** 알고리즘 기반 조합 폭발 통제 및 **정적 분석 도구(SonarQube)** 병행을 통한 데드코드 원천 격리
- **검증 체계**: CI/CD 파이프라인 내 JaCoCo/VectorCAST 연동 Quality Gate 강제 (커버리지 미달 시 배포 빌드 실패 차단)
- **기대 효과**: 제어 경로 및 복합 조건 내부 논리 오류 완전 적발, 기능안전 최고 안전 무결성 등급(DO-178C Level A) 공인 인증 통과

<div class="itpe-pipeline is-vertical" role="img" aria-label="화이트박스 테스팅 고도화 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>형식적 C0</strong><span>형식적 C0 구문 커버리지 위주 및 분기 결함 간과</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>MC/DC 강제</strong><span>결정 커버리지(C1) 표준화 및 핵심 모듈 MC/DC 강제</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>품질 게이트</strong><span>CI Quality Gate 연동 및 커버리지 미달 시 빌드 중단</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>안전 등급</strong><span>내부 논리 오류 차단 및 기능안전 최고 등급 달성</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: **화이트박스 테스트**는 프로그램의 소스코드 논리 구조를 제어 흐름 그래프로 모델링하여 내부 경로를 검증하는 구조 기반 테스트
- 목적: 미실행 경로 및 데드코드를 제거하고 고신뢰성 제어 무결성 보증

### 2. 주요 커버리지 계층

<div class="itpe-pipeline is-vertical" role="img" aria-label="커버리지 계층 요약">
  <div class="itpe-pipeline-node"><strong>구문(C0)</strong><div class="itpe-step-detail"><span>모든 문장 1회 실행</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>결정(C1)</strong><div class="itpe-step-detail"><span>모든 분기 True/False 실행</span></div></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>MC/DC</strong><div class="itpe-step-detail"><span>N+1개 케이스로 개별 조건 독립 영향력 검증</span></div></div>
</div>

### 3. 핵심 통제

- **MC/DC 통제**: 다중조건 조합 폭발(2^N)을 N+1개로 최적화하여 안전 기준선 충족
- **Quality Gate**: CI 환경에서 브랜치 커버리지 미달 시 프로덕션 배포 차단

## 출제 이력과 검증 출처

- 제134회 정보관리기술사 1교시: 화이트박스 테스트 기법 및 제어 흐름 커버리지
- ISO 26262 Road vehicles - Functional safety, Part 6: Software development
- RTCA DO-178C Software Considerations in Airborne Systems and Equipment

## 학습 체크

- [ ] 구문, 결정, 조건, 조건/결정 커버리지의 상호 포함 관계를 설명할 수 있는가?
- [ ] MC/DC가 필요한 이유와 테스트 케이스 수가 N+1이 되는 원리를 설명할 수 있는가?
- [ ] 제어 흐름 그래프(CFG)에서 분기 노드와 경로 도출법을 설명할 수 있는가?

## 연결 토픽

- 이전 토픽: [형상관리](./011_configuration_management.md)
- 연관 토픽: [블랙박스 테스트](./008_black_box_test.md), [McCabe 순환복잡도](./036_mccabe_cyclomatic_complexity.md)
- 다음 토픽: [ATAM](./014_atam.md)
