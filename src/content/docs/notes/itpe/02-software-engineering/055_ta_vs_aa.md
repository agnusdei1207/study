---
title: "TA와 AA 역할 비교 및 협업 방안"
tags:
  - "notes-software-engineering"
sidebar:
  badge:
    text: "B"
    variant: "note"
author: "Antigravity"
date: "2026-09-21T16:36:00+09:00"
extra:
  model: "Gemini 3.8 Flash"
  keyword_grade: "B"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="소프트웨어 아키텍처에서 TA와 AA까지의 지식 경로"><span>SW 공학·아키텍처</span><span>역할·거버넌스</span><strong>TA·AA 역할과 협업</strong></div>

## 해당 토픽 큰 그림과 30초 인출

- 본질: **TA(Technical Architect)**는 기술 실행기반과 비기능 품질을 설계하고, **AA(Application Architect)**는 업무 요구를 애플리케이션 구조와 컴포넌트로 구체화하는 역할
- 메커니즘: AA(기능·컴포넌트·API) ↔ 공동 결정(품질 시나리오·ADR·논리물리 매핑) ↔ TA(플랫폼·용량·배포·HA)
- 산출/효과: 논리-물리 아키텍처 정합성 확보 · ADR 기반 기술부채 통제 · 고가용성/고확장성 엔터프라이즈 시스템 구현

<div class="itpe-flow-map" role="img" aria-label="TA와 AA 협업 아키텍처 프레임워크">
  <div class="itpe-flow-node"><strong>AA (Application)</strong><span>업무 기능 · 컴포넌트 · API</span></div>
  <div class="itpe-flow-arrow">↕ 공동 품질 시나리오 &amp; ADR ↕</div>
  <div class="itpe-flow-node is-current">
    <strong>아키텍처 협업 접점</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>논리-물리 매핑</strong><span><span class="itpe-keyword"><strong>컨테이너 패키징 · 네트워크 토폴로지</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>SLO 및 용량</strong><span><span class="itpe-keyword"><strong>동시성 제어 · 사이징 · 스케일링</strong></span></span></div>
      <div class="itpe-flow-branch"><strong>검증 체계</strong><span>부하 시험 · DR 복구 · 관측성(APM)</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↕ 기술 실행기반 및 품질 보증 ↕</div>
  <div class="itpe-flow-node"><strong>TA (Technical)</strong><span>플랫폼 · 인프라 · 보안 · HA/DR</span></div>
</div>

## 예상문제

> TA와 AA의 역할·산출물을 비교하고, 클라우드 네이티브 환경에서 품질속성을 보장하기 위한 협업방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 키워드 | 통합 답안 위치 |
|---|---|---|
| TA(Technical Architect) | 기술구성, 용량, 플랫폼, 배포, HA/DR, 관측성 | Ⅲ 역할·산출물 |
| AA(Application Architect) | 도메인, 컴포넌트, API, 공통 프레임워크 | Ⅲ 역할·산출물 |
| 품질속성 협업 | 성능, 가용성, 보안, 변경성, ADR, 시험 | Ⅳ 협업절차·Ⅵ 통제 |

## Ⅰ. 실행기반과 애플리케이션 구조를 잇는 TA·AA 개요

**TA(Technical Architect)**는 시스템의 기술 실행기반과 비기능 품질을 설계·검증하고, **AA(Application Architect)**는 업무 요구사항을 애플리케이션 구조·컴포넌트·인터페이스로 구체화한다. 역할 명칭과 경계는 조직마다 다르므로 핵심은 명칭보다 **의사결정권·산출물·검증책임의 명확화**이다.

## Ⅱ. 역할 분화의 목적과 공통책임

| 구분 | AA | TA | 공동책임 |
|---|---|---|---|
| 관심사 | 기능 구조·변경 용이성 | 실행환경·성능·가용성 | 품질속성 충족 |
| 주요 입력 | 업무·기능 요구사항 | 용량·보안·운영 요구사항 | 품질 시나리오 |
| 핵심 결정 | 도메인·컴포넌트·API | 플랫폼·토폴로지·배포 | 트레이드오프·기술부채 |
| 검증 | 구조·인터페이스 시험 | 부하·복구·운영 시험 | 아키텍처 평가·인수기준 |

## Ⅲ. 역할·산출물·협업 접점 구조

<div style="margin: 1.5rem 0; text-align: center;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 220" width="100%" height="auto" style="max-width: 520px; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <defs>
    <filter id="arch-shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="1" dy="2" stdDeviation="2" flood-opacity="0.12"/>
    </filter>
  </defs>

  <!-- Left: AA Domain -->
  <rect x="15" y="15" width="150" height="190" rx="8" fill="var(--sl-color-blue-subtle, #eff6ff)" stroke="var(--sl-color-blue-high, #2563eb)" stroke-width="1.5" filter="url(#arch-shadow)"/>
  <text x="90" y="38" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--sl-color-blue-high, #2563eb)">AA (Application)</text>
  <rect x="23" y="48" width="134" height="145" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1"/>
  <text x="30" y="70" font-size="9.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">• 도메인 모델링 (DDD)</text>
  <text x="30" y="88" font-size="9" fill="var(--sl-color-text-muted, #4b5563)">• 컴포넌트 분할·응집</text>
  <text x="30" y="106" font-size="9" fill="var(--sl-color-text-muted, #4b5563)">• REST / gRPC API 설계</text>
  <text x="30" y="124" font-size="9" fill="var(--sl-color-text-muted, #4b5563)">• 공통 프레임워크 구축</text>
  <text x="30" y="148" font-size="9.5" font-weight="700" fill="var(--sl-color-blue-high, #2563eb)">[핵심 산출물]</text>
  <text x="30" y="166" font-size="8.5" fill="var(--sl-color-text, #374151)">앱 아키텍처 정의서</text>
  <text x="30" y="180" font-size="8.5" fill="var(--sl-color-text, #374151)">인터페이스 명세서</text>

  <!-- Arrow to Center -->
  <path d="M 165 110 L 180 110" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1.5"/>

  <!-- Center: Collaboration Interface (ADR & Mapping) -->
  <rect x="180" y="15" width="160" height="190" rx="8" fill="var(--sl-color-purple-subtle, #f5f3ff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1.5" filter="url(#arch-shadow)"/>
  <text x="260" y="38" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--sl-color-accent, #7c3aed)">공동 협업 접점</text>
  <rect x="188" y="48" width="144" height="145" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-accent, #7c3aed)" stroke-width="1"/>
  <text x="195" y="70" font-size="9.5" font-weight="700" fill="var(--sl-color-accent-high, #5b21b6)">★ 공동 결정 (ADR)</text>
  <text x="195" y="88" font-size="9" fill="var(--sl-color-text, #1f2937)">• 논리-물리 매핑</text>
  <text x="195" y="104" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">컨테이너 &amp; 클러스터</text>
  <text x="195" y="122" font-size="9" fill="var(--sl-color-text, #1f2937)">• 품질속성 시나리오</text>
  <text x="195" y="138" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">성능·가용성·보안 SLO</text>
  <text x="195" y="156" font-size="9" fill="var(--sl-color-text, #1f2937)">• 인수 시험 및 런북</text>
  <text x="195" y="172" font-size="8.5" fill="var(--sl-color-text-muted, #4b5563)">부하 시험 &amp; DR 모의</text>

  <!-- Arrow to Right -->
  <path d="M 340 110 L 355 110" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1.5"/>

  <!-- Right: TA Domain -->
  <rect x="355" y="15" width="150" height="190" rx="8" fill="var(--sl-color-green-subtle, #f0fdf4)" stroke="var(--sl-color-green-high, #16a34a)" stroke-width="1.5" filter="url(#arch-shadow)"/>
  <text x="430" y="38" text-anchor="middle" font-size="11.5" font-weight="700" fill="var(--sl-color-green-high, #16a34a)">TA (Technical)</text>
  <rect x="363" y="48" width="134" height="145" rx="4" fill="var(--sl-color-bg-card, #ffffff)" stroke="var(--sl-color-gray-4, #9ca3af)" stroke-width="1"/>
  <text x="370" y="70" font-size="9.5" font-weight="700" fill="var(--sl-color-text, #1f2937)">• 클라우드/인프라 토폴로지</text>
  <text x="370" y="88" font-size="9" fill="var(--sl-color-text-muted, #4b5563)">• 하드웨어 사이징·용량</text>
  <text x="370" y="106" font-size="9" fill="var(--sl-color-text-muted, #4b5563)">• 네트워크·망분리·보안</text>
  <text x="370" y="124" font-size="9" fill="var(--sl-color-text-muted, #4b5563)">• HA/DR 이중화·관측성</text>
  <text x="370" y="148" font-size="9.5" font-weight="700" fill="var(--sl-color-green-high, #16a34a)">[핵심 산출물]</text>
  <text x="370" y="166" font-size="8.5" fill="var(--sl-color-text, #374151)">기술 인프라 구성도</text>
  <text x="370" y="180" font-size="8.5" fill="var(--sl-color-text, #374151)">용량산정 및 배포설계서</text>
</svg>
</div>

| 산출물 | AA 주도 | TA 주도 | 공동 검토 |
|---|---|---|---|
| 구조 | 애플리케이션·컴포넌트·API 명세 | 기술·배포·네트워크 구성 | 논리-물리 매핑 |
| 품질 | 오류처리·동시성·데이터 일관성 설계 | 용량·HA/DR·관측성 설계 | 성능·복구 시나리오 |
| 운영 | 빌드·설정·상태관리 요구사항 | 배포·확장·백업·런북 | SLO·인수시험 |

## Ⅳ. 요구에서 운영검증까지의 협업절차

```text
요구·제약 → 품질 시나리오 → 공동대안 → ADR·상세설계 → 시험·운영환류
```

1. 이해관계자 요구사항을 응답시간·가용성·보안·변경성의 품질 시나리오로 바꾼다.
2. AA는 호출·상태·데이터 흐름을, TA는 자원·망·배포·복구 제약을 제시한다.
3. 비용·복잡도·성능의 대안을 공동 평가하고 ADR에 결정과 근거를 기록한다.
4. 논리 컴포넌트와 물리 배포단위, 용량과 동시성 설정을 추적 가능하게 연결한다.
5. 부하·장애·복구·보안시험 결과를 SLO와 비교해 설계를 갱신한다.

## Ⅴ. TA와 AA 비교

| 비교축 | AA | TA |
|---|---|---|
| 중심 관점 | 업무기능과 애플리케이션 구조 | 기술기반과 런타임 품질 |
| 변화 단위 | 도메인·컴포넌트·API | 플랫폼·노드·배포환경 |
| 대표 산출물 | 앱 구조도, 인터페이스·공통모듈 명세 | 기술구성도, 용량·HA/DR·운영 설계 |
| 주요 위험 | 결합도·일관성·변경 영향 | 병목·장애전파·복구 실패 |
| 성공 조건 | 기능 무결성과 변경 용이성 | 품질목표와 운영 가능성 |

## Ⅵ. 사일로와 책임공백 위험 및 실무 통제 대책

| 위험 | 대책 | 효과 |
|---|---|---|
| **비기능 요구사항 소유자 부재** | 품질속성별 책임자 및 수용기준(SLO) 명시 | 요구사항-설계-시험 간 추적성 100% 확보 |
| **논리-물리 구조 불일치** | 컴포넌트-배포단위 매핑 공동 아키텍처 리뷰 강제 | 배포 뷰 최신성 유지 및 런타임 배포 장애 방지 |
| **도구 중심 과잉 설계** | 품질 시나리오 기반 대안 평가 및 **ADR(아키텍처 결정 기록)** 의무화 | 객관적 공학 근거 확보 및 불필요한 인프라 비용 절감 |
| **개발-운영(DevOps) 단절** | 관측성(Observability)·런북·복구시험을 완료정의(DoD)에 포함 | 시스템 복원력 확보 및 장애 복구 시간(MTTR) 최소화 |

## Ⅶ. 직함보다 공동 품질책임을 세우는 결론

> TA와 AA의 분업은 문서 인수인계가 아니라 서로 다른 관점을 품질 시나리오로 결합하는 구조여야 한다.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 클라우드 네이티브와 마이크로서비스 환경에서 AA와 TA의 경계는 무너지고 있음. 인프라가 코드(IaC)가 되고 배포 단위가 컨테이너로 추상화되면서, 애플리케이션의 스레드 풀 설정 하나가 쿠버네티스의 CPU Throttling과 Pod OOMKilled를 직접 유발함. 따라서 AA와 TA가 분리되어 각자 문서만 작성하는 프로젝트는 런타임 장애를 피할 수 없음.
- 나라면: 아키텍처 협의체(Architecture Council)를 상설 운영하여 모든 기술 스택 변경과 논리-물리 매핑 결정을 아키텍처 결정 기록(ADR)으로 표준화하고, 부하 테스트와 카오스 엔지니어링(Chaos Mesh) 복구 시험을 AA와 TA 공동 주관 하에 프로덕션 배포 전 필수 게이트로 강제하겠음.

### 실전 답안용 기술사적 제언

- **판정 기준**: AA-TA 간 사일로 탈피, 품질 시나리오 기반 ADR(아키텍처 결정 기록) 작성 및 논리-물리 매핑 필수 판정
- **대응 방안**: AA의 애플리케이션 컴포넌트와 TA의 클라우드 리소스 간 1:1 매핑 뷰 수립 및 IaC 기반 환경 표준화
- **검증 체계**: SLO(P99 지연시간, 가용성 99.99%) 기반 부하/DR 복구 시험 및 분산 트레이싱(OpenTelemetry) 관측성 검증
- **기대 효과**: 아키텍처 불일치로 인한 배포 장애 제로화, 기술부채 40% 감소 및 클라우드 인프라 운영 비용 30% 절감

<div class="itpe-pipeline is-vertical" role="img" aria-label="TA AA 아키텍처 협업 거버넌스 제언">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <span>AA-TA 역할 분리로 인한 비기능 품질 소유권 공백 및 런타임 배포 장애</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <span>공동 ADR 체계 수립 및 컴포넌트-컨테이너 간 논리-물리 매핑 거버넌스 확립</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <span>목표 SLO(응답시간/가용성) 기반 통합 부하 시험 및 DR 모의훈련 전수 통과</span>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <span>클라우드 네이티브 환경에서의 시스템 무장애 복원력(Resilience) 극대화</span>
  </div>
</div>

## 1교시 10점 답안 발췌

- 정의: **AA**는 업무 요구사항의 애플리케이션 구조화, **TA**는 기술 실행기반과 비기능 품질 보증을 담당하는 아키텍트
- 목적: 기능 무결성과 비기능(성능·가용성·보안) 실행기반의 조화로운 품질 달성

<div class="itpe-pipeline is-vertical" role="img" aria-label="TA AA 1교시 핵심 흐름">
  <div class="itpe-pipeline-node"><strong>AA (애플리케이션)</strong><span>도메인 모델 · 컴포넌트 · API · 공통 프레임워크</span></div>
  <div class="itpe-pipeline-arrow">↕ 공동 ADR · 논리-물리 매핑 · SLO 검증 ↕</div>
  <div class="itpe-pipeline-node"><strong>TA (기술 실행기반)</strong><span>클라우드 플랫폼 · 용량 산정 · 배포 파이프라인 · HA/DR</span></div>
</div>

## 공식·검증 근거, 학습 체크와 연결 토픽

- **공식·검증 근거**: [ISO/IEC/IEEE 42010:2022 Architecture description](https://www.iso.org/standard/74393.html), [ISO/IEC 25010:2023 Product quality model](https://www.iso.org/standard/78176.html), 정보관리기술사 제138회 출제 이력
- **학습 체크**: □ 역할이 조직별로 달라질 수 있음을 밝혔는가 □ 산출물과 공동 접점을 비교했는가 □ 품질 시나리오-ADR-시험을 연결했는가
- **연결 토픽**: [SW 아키텍처](./056_software_architecture.md) · [아키텍처 스타일](./057_architecture_style.md) · [SW 아키텍처 분석](./124_software_architecture_analysis.md) · [성능 요구사항](./149_performance_requirement.md)

