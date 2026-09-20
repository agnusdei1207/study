---
title: "정보시스템 운영 성과관리"
author: "Codex"
date: "2026-09-20T19:32:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "C"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "C"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 시스템 운영 관리 및 IT 거버넌스를 거쳐 정보시스템 운영 성과관리로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>시스템 운영 관리·IT 거버넌스</span>
  <strong>정보시스템 운영 성과관리</strong>
</div>

## 큰 그림과 30초 인출

- 본질: **정보시스템 운영 성과관리**는 가동 중인 정보시스템의 타당성을 **비용 관점**과 **업무 관점** 2개 축으로 계량 평가하여 유지·개선·폐기를 결정하는 사후 거버넌스 제도
- 메커니즘: 유지관리비 적정도와 실질 이용률을 2차원 매트릭스에 매핑하여 **유지·기능개선·재개발·폐기(통폐합)**의 4대 의사결정을 도출
- 산출: 운영 성과측정 종합 보고서 · 2차원 의사결정 매트릭스 · 폐기/재개발 의결서

<div class="itpe-flow-map" role="img" aria-label="정보시스템 운영 성과관리 평가 및 의사결정 흐름">
  <div class="itpe-flow-node">
    <strong>운영 시스템 인벤토리</strong>
    <small>전사 가동 중인 공공·기업 정보시스템 전수 조사</small>
  </div>
  <div class="itpe-flow-arrow">↓<small>2대 관점 지표 실측</small></div>
  <div class="itpe-flow-node is-current">
    <strong>2차원 성과측정 모델</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>비용</strong><span><span class="itpe-keyword"><strong>유지관리비 적정도</strong></span> (대가기준 대비 계약액)</span></div>
      <div class="itpe-flow-branch"><strong>업무</strong><span><span class="itpe-keyword"><strong>업무 기여도</strong></span> (실사용 MAU · 법정 업무 지원율)</span></div>
      <div class="itpe-flow-branch"><strong>판정</strong><span>2차원 4분면 매트릭스 기반 <span class="itpe-keyword"><strong>4대 의사결정</strong></span></span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓<small>심의 의결 및 후속 조치</small></div>
  <div class="itpe-flow-node">
    <strong>구조조정 및 예산 반영</strong>
    <small>유지 · 클라우드 재개발 · 데이터 아카이빙 후 폐기(Retire)</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **정보시스템 운영 성과관리**: 전자정부법 제56조에 따라 운영 중인 정보시스템의 효율성과 업무 기여도를 측정하는 제도
- **비용 관점(비용 적정도)**: 소프트웨어 사업 대가산정 가이드 대비 실제 유지관리비와 인프라 운영비의 적정성을 평가
- **업무 관점(업무 적합성)**: 시스템의 실제 이용률(접속 건수, MAU)과 법정 필수 업무 기여도, 사용자 만족도를 평가
- **좀비 시스템**: 이용자나 트랜잭션이 거의 없으면서 매년 유지보수비와 서버 자원을 지속 낭비하는 노후 시스템
- **데이터 아카이빙(Data Archiving)**: 폐기 대상 시스템의 법정 보존 의무 데이터를 장기 보관용 콜드 스토리지로 안전 이관하는 활동
- **통폐합**: 유사·중복 기능을 수행하는 둘 이상의 시스템을 단일 플랫폼으로 통합 흡수하는 조치

</details>

## 예상문제

> 행정안전부 '정보시스템 운영 성과관리 지침'에 따른 정보시스템 운영 성과측정의 개념, 비용 관점 및 업무 관점의 핵심 지표, 2차원 매트릭스 기반 4대 의사결정(유지, 기능개선, 재개발, 폐기) 판단 기준 및 실무 정착 방안을 설명하시오. (25점)

## 딸려 나오는 하위 토픽

| 하위 토픽 | 핵심 내용 | 본문 답안 위치 |
|---|---|---|
| **01-100 정보시스템 운영 성과측정** | 비용 적정도와 업무 기여도 2개 축으로 계량화하여 4분면 매트릭스 진단 수행 | 본문 전반 (Ⅱ, Ⅲ, Ⅳ) |

## Ⅰ. IT 운영 효율화와 시스템 합리화의 기준, 성과관리의 개요

> 정보시스템 운영 성과관리는 '만드는 IT'에서 **운영 중인 IT의 지속 가치 평가**로 패러다임을 전환하며, 성패는 단순 서류 작성이 아닌 **저이용 좀비 시스템의 과감한 폐기·통폐합**으로 판정함.

- 정의: 전자정부법 제56조에 근거하여 운영 중인 정보시스템을 대상으로 **비용 적정도**와 **업무 기여도**를 계량 평가하여 존속 여부를 결정하는 **사후 성과평가 거버넌스**
- 목적: 저이용·중복 '좀비 시스템' 퇴출 및 예산 낭비 차단 → **유지·기능개선·재개발·폐기**의 객관적 의사결정을 통한 **IT 운영 효율화** 달성

## Ⅱ. 성과관리 4단계 추진 파이프라인

> 전수 인벤토리 조사에서 실측 데이터 수집, 2차원 매트릭스 분석, 심의 의결로 이어지는 행정·공학적 파이프라인으로 수행됨.

<div class="itpe-pipeline is-vertical" role="img" aria-label="정보시스템 운영 성과관리 4단계 추진 파이프라인">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 성과측정 계획 수립</strong></span>
    <small>운영 중인 시스템 인벤토리 실사 · 성과측정 대상군 확정<br />→ 성과측정 추진계획서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 실측 데이터 수집 및 검증</strong></span>
    <small>웹 로그(MAU) · 계약서 원장 · 인프라 리소스 실측<br />→ 지표별 실측 증빙자료</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 종합 점수 산출 및 매핑</strong></span>
    <small>비용 관점 점수 + 업무 관점 점수 환산 후 4분면 매트릭스 배치<br />→ 2차원 매트릭스 진단 보고서</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 심의 의결 및 예산 환류</strong></span>
    <small>정보화심의위원회 의결 · 폐기/통폐합/재개발 집행 및 차년도 예산 연계<br />→ 운영 개선 계획서 · 예산 조정안</small>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>2차원 의사결정</strong></span> · 비용 적정도 축과 업무 기여도 축의 교차 지점에서 최적의 구조조정 방향 확정</div>

## Ⅲ. 성과측정 2대 평가 관점 및 세부 지표

> 소프트웨어 대가 기준 기반의 비용 검증과 실사용 기반의 업무 효익을 균형 있게 계량화함.

| 평가 관점 | 세부 지표 | 측정 내용 및 산식 기준 | 비고 |
|---|---|---|---|
| **비용 관점 (Cost)** | **유지관리비 적정도** | SW 사업 대가산정 가이드 기준 대비 실제 계약 금액 비율 | 비용 과다 투입 여부 검증 |
| **비용 관점 (Cost)** | **운영비용 효율성** | 기능점수(FP) 단위당 소비되는 인프라(서버, 스토리지) 비용 | 클라우드 전환 타당성 검토 |
| **업무 관점 (Business)** | **시스템 이용도** | 실 사용자 본인인증 기반 월간 활성 이용자 수(MAU), 트랜잭션 수 | 허위 호출 배제 실사용 검증 |
| **업무 관점 (Business)** | **업무 기여도** | 조직 고유 핵심 업무 및 법정 의무 사무 처리 지원율 | 대체 불가능성 평가 |
| **업무 관점 (Business)** | **사용자 만족도** | 내·외부 실제 사용자를 대상으로 실시한 연례 정량 만족도 | 체감 서비스 품질 측정 |

## Ⅳ. 2차원 매트릭스 기반 4대 의사결정 판정 체계

> 두 개 축의 평가 점수를 바탕으로 4개 분면에 배치하여 명확한 조치 경로를 도출함.

| 4대 의사결정 | 매트릭스 영역 | 핵심 판정 사유 | 실무 추진 조치 |
|---|---|---|---|
| **유지 (Maintain)** | 업무 기여도 높음 / 비용 적정 | 업무 기여도가 높고 비용 집행이 적정한 가장 이상적인 상태 | 현행 운영 체계 및 SLA 유지, 보안 패치 |
| **기능개선 / 재개발** | 업무 기여도 높음 / 비용 과다 | 핵심 업무를 지원하나 시스템 노후화로 유지비가 폭증한 상태 | **클라우드 네이티브 전환**, MSA 재개발 추진 |
| **폐기 / 통폐합** | 업무 기여도 낮음 / 비용 적정 | 이용률이 미미하여 비즈니스 존속 가치를 상실한 저이용 상태 | 데이터 아카이빙 후 **서비스 종료 및 타 시스템 통합** |
| **운영효율화 / 폐기** | 업무 기여도 낮음 / 비용 과다 | 이용자도 없으면서 막대한 인프라 비용을 축내는 최악의 상태 | 즉각적 인프라 회수, **차년도 예산 전액 삭감 및 즉시 폐기** |

## Ⅴ. 시스템 폐기 및 클라우드 아카이빙 연계를 위한 기술사적 제언

> 시스템 폐기 시 공공 기록물 보존 규정을 위반하지 않도록 콜드 스토리지 아카이빙과 상시 자동 관제 거버넌스가 필수적임.

### 학습자 통찰 메모 — 답안 밖

- [핵심 통찰]: 정보시스템 운영 성과관리의 최대 걸림돌은 부서 이기주의임. 시스템이 폐기되면 부서의 권한과 예산이 줄어든다고 판단해 매크로로 가짜 트래픽을 만들어 점수를 조작함. 따라서 인증 기반의 고유 트랜잭션을 실측하고, 자진 폐기 부서에 신규 R&D 예산을 우선 배정하는 제도적 인센티브가 병행되어야 함.
- 나라면: 클라우드 통합 관제 센터의 APM 데이터를 직접 파이프라인으로 연결하여 `연간 트래픽 미달 시스템을 '좀비 후보군'으로 자동 지정 → 2차원 매트릭스 자동 계산 → 폐기 결정 시 법정 데이터를 클라우드 WORM(Write Once Read Many) 스토리지로 자동 아카이빙`하는 무중단 폐기 거버넌스를 구축하겠음.

### 실전 답안용 기술사적 제언

- 판정: 연례 서류 취합을 탈피하고 APM 실측 기반 상시 평가 체계 확립
- 대안: **클라우드 APM 연계 자동 성과측정 및 WORM 아카이빙 기반 폐기 파이프라인** 가동
- 검증: 본인인증 실사용자 MAU 실측률 100% · 폐기 데이터 법정 보존 무결성 검증
- 효과: 유령 시스템 퇴출을 통한 전사 IT 운영비 20% 절감 및 클라우드 전환 가속화

<div class="itpe-pipeline is-vertical" role="img" aria-label="운영 성과관리 및 시스템 합리화 제언 흐름">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <small>연 1회 엑셀 서류 취합 · 매크로를 통한 트래픽 조작 · 부서 이기주의로 폐기 거부</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <small>APM 로그 실측 파이프라인 + 2차원 매트릭스 자동 판정 + 클라우드 WORM 콜드 아카이빙</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <small>허위 PV 필터링 100% · 폐기 의결 시스템의 법정 데이터 영구 보존 무결성 검증</small>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <small>좀비 시스템 낭비 예산 전면 회수 · 신규 디지털 혁신 사업으로 예산 전략적 재배분</small>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 가동 중인 정보시스템의 타당성을 **비용 적정도**와 **업무 기여도** 관점에서 계량 평가하여 유지·개선·폐기를 결정하는 **사후 성과 거버넌스**
- 목적: 저이용 좀비 시스템 퇴출 및 IT 예산 낭비 차단 → **유지·기능개선·재개발·폐기** 의사결정을 통한 운영 효율화

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="정보시스템 운영 성과관리 2차원 매트릭스 요약">
  <div class="itpe-pipeline-node"><strong>유지 (Maintain)</strong><small>업무 기여도 우수 / 비용 적정 (현행 SLA 유지)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>기능개선/재개발</strong><small>업무 기여도 우수 / 비용 과다 (클라우드 MSA 재개발)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>폐기/통폐합</strong><small>업무 기여도 저조 / 비용 적정 (데이터 아카이빙 후 통합)</small></div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node"><strong>운영효율화/폐기</strong><small>업무 기여도 저조 / 비용 과다 (예산 삭감 및 즉시 폐기)</small></div>
</div>

### 3. 핵심 통제

- **2차원 4분면 매트릭스**: 업무 적합성과 비용 적정도의 교차 지점에서 객관적 조치 확정
- **데이터 아카이빙**: 폐기 결정 시스템의 법정 원장 데이터를 클라우드 WORM 스토리지로 안전 이관

## 출제 이력과 검증 출처

- 제121회 정보관리기술사(KPC) 1교시: 전자정부 정보시스템 운영 성과관리 지침에 따른 성과측정 및 판단 기준
- 행정안전부, [정보시스템 운영 성과관리 지침](https://www.mois.go.kr)
- 한국지능정보사회진흥원(NIA), [공공 정보시스템 운영 성과관리 실무 매뉴얼](https://www.nia.or.kr)

## 학습 체크

- [ ] 정보시스템 운영 성과관리의 법적 근거(전자정부법 제56조)를 제시할 수 있는가?
- [ ] 비용 관점과 업무 관점의 세부 측정 지표를 설명할 수 있는가?
- [ ] 2차원 매트릭스 상의 4대 의사결정(유지, 기능개선, 재개발, 폐기)의 판정 기준을 설명할 수 있는가?
- [ ] 저이용 시스템 폐기 시 데이터 보존 및 아카이빙 대책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [SEM](./078_sem.md)
- 연관 토픽: [시스템 운영 감리](./059_system_operation_audit.md), [IT 투자평가](./016_it_investment_evaluation.md), [공공 클라우드 네이티브 전환](./021_public_cloud_native_transition.md)
- 다음 토픽: [CPM](./081_cpm.md)
