---
title: "A/B 테스트"
author: "OpenAI Codex"
date: "2026-09-21T16:55:00+09:00"
tags:
  - "notes-it-strategy"
sidebar:
  badge:
    text: "A"
extra:
  keyword_grade: "A"
  model: "GPT-5"
---

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" role="img" aria-label="IT 전략·관리에서 데이터 기반 의사결정과 제품 실험을 거쳐 A/B 테스트로 이어지는 지식 위치">
  <span>IT 전략·관리</span>
  <span>데이터 기반 의사결정·제품 실험</span>
  <strong>A/B 테스트</strong>
</div>

## 큰 그림과 30초 인출

- 본질: 대조군과 실험군을 무작위 배정하여 변경안의 인과효과를 검증하는 온라인 통제실험
- 메커니즘: 가설·지표 정의 → 표본설계 → 무작위 배정 → 계측검증 → 통계검정 → 배포판정
- 통제: SRM 진단 · Peeking 방지 · 효과크기·신뢰구간 · Guardrail Metrics

<div class="itpe-flow-map" role="img" aria-label="사용자 트래픽 분할에서 통계적 가설검정 및 롤아웃 결정으로 이어지는 흐름">
  <div class="itpe-flow-node">
    <strong>전체 사용자 트래픽</strong>
    <small>디지털 서비스 방문자 · 무작위 해시 기반 분할</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node is-current">
    <strong>통제 실험 환경 (Feature Flag)</strong>
    <div class="itpe-flow-branches">
      <div class="itpe-flow-branch"><strong>대조군 (Group A)</strong><span>기존 원본 서비스 노출 (Control)</span></div>
      <div class="itpe-flow-branch"><strong>실험군 (Group B)</strong><span>단일 기능 변경 적용 노출 (Variant)</span></div>
      <div class="itpe-flow-branch"><strong>관측 조건</strong><span>동일 기간 동시 관측 및 계절성 배제</span></div>
    </div>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>통계적 가설검정</strong>
    <small><span class="itpe-keyword"><strong>SRM</strong></span> 카이제곱 검사 · <span class="itpe-keyword"><strong>p-value</strong></span> 및 신뢰구간 도출</small>
  </div>
  <div class="itpe-flow-arrow">↓</div>
  <div class="itpe-flow-node">
    <strong>출시 및 롤아웃 결정</strong>
    <small><span class="itpe-keyword"><strong>Guardrail</strong></span> 지표 통과 · 효과 크기 확인 후 전면 배포</small>
  </div>
</div>

<details>
<summary>핵심 용어</summary>

- **A/B 테스트(A/B Test)**: 기존 버전(A)과 변경 버전(B)을 무작위로 노출해 통계적 유의성을 검증하는 무작위 통제 실험
- **Causality(인과관계)**: 특정 기능 변경이 사용자 행동 변화를 직접적으로 유발했음을 입증하는 관계
- **SRM(Sample Ratio Mismatch)**: 설계된 의도와 달리 실제 유입된 A/B 표본 비율이 통계적으로 유의하게 왜곡된 현상
- **Peeking(피킹)**: 실험 완료 전 수시로 p-value를 확인하여 조기 종료함으로써 1종 오류를 증폭시키는 편향
- **Feature Flag**: 코드 재배포 없이 특정 사용자 그룹에 기능을 동적으로 켜고 끄는 제어 플래그
- **p-value**: 귀무가설이 참이라는 가정하에 현재 관측된 차이 이상의 극단적 결과가 우연히 나타날 확률
- **MDE(Minimum Detectable Effect)**: 실험을 통해 통계적으로 감지해내고자 하는 최소한의 개선 효과 크기
- **Guardrail Metrics(보호 지표)**: 주 성과지표 상승 시 희생될 수 있는 시스템 레이턴시, 오류율 등 핵심 안정성 지표

</details>

## 예상문제

> A/B 테스트의 개념과 실험 절차를 설명하고, SRM·Peeking 등 통계적 왜곡과 대응책을 제시하시오. **(미출제 예상·25점)**

## Ⅰ. 직관이 아닌 데이터 기반 의사결정, A/B 테스트의 개요

> 주관적 직관(HiPPO)을 배제하고 인과관계를 입증하며, 성패는 단순 클릭률이 아닌 **SRM 편향 제거**와 **보호 지표(Guardrail) 검증**으로 판정함.

- 정의: 사용자를 무작위 배정하여 대조군(A)과 실험군(B) 간의 단일 변수 변경 효과를 통계적으로 검증하는 **무작위 통제 시험(RCT)**
- 목적: 변경효과 검증 · 의사결정 불확실성 축소 · 안전한 단계적 배포

## Ⅱ. A/B 테스트 5단계 실험 프로세스 및 계측 파이프라인

> 가설 수립에서 배포 판정까지 `가설수립 → 표본설계 → 계측검증 → 실험실행 → 가설검정` 파이프라인을 거쳐 객관적 의사결정을 완성함.

<div class="itpe-pipeline is-vertical" role="img" aria-label="A/B 테스트 5단계 실험 프로세스 및 단계별 활동과 산출물">
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>① 문제 정의 및 가설 수립</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>독립변수 정의 · 귀무가설($H_0$) 및 대립가설($H_1$) 설정</span>
      <strong>산출</strong><span>가설 정의서 · 핵심 성과지표 명세서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>② 표본수 및 실험 기간 산정</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>유의수준 · 검정력 · MDE 기준 표본수 계산</span>
      <strong>산출</strong><span>실험 계획서 · 필요 표본수 계산서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>③ 계측 구축 및 A/A 무편향 검증</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>Feature Flag 연동 · A/A 테스트로 그룹 간 사전 편향 부재 확인</span>
      <strong>산출</strong><span>배정 파이프라인 검증서 · 트래킹 코드</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>④ 무작위 실험 실행 및 모니터링</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>동일 기간 동시 노출 · 조기 종료 금지 및 SRM 실시간 감시</span>
      <strong>산출</strong><span>일별 전환 로그 · 가드레일 모니터링 보고서</span>
    </div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <span class="itpe-keyword"><strong>⑤ 통계적 가설검정 및 배포 결정</strong></span>
    <div class="itpe-step-detail">
      <strong>활동</strong><span>카이제곱 SRM 검사 · p-value 및 신뢰구간 평가 후 롤아웃 결정</span>
      <strong>산출</strong><span>실험 결과 보고서 · 기능 배포 결정문</span>
    </div>
  </div>
</div>
<div class="itpe-trace-band"><span class="itpe-keyword"><strong>Traceability</strong></span> · 사전 가설 ↔ Feature Flag 배정 ↔ SRM 적합도 ↔ 최종 롤아웃 양방향 연계</div>

## Ⅲ. A/B 테스트 아키텍처 및 계측 파이프라인

> 사용자 배정부터 통계 분석까지 계층화된 파이프라인을 구축해야 데이터 왜곡을 사전에 방어할 수 있음.

| 계층 | 주요 구성요소 | 핵심 역할 및 통제 기능 |
|---|---|---|
| **배정 계층** | Consistent Hashing, **Feature Flag** | 사용자 ID 기반 일관된 군 배정 및 세션 튕김 방지 |
| **수집 계층** | 클라이언트 로깅 SDK, 이벤트 게이트웨이 | 클릭, 체류시간, 구매 등 핵심 이벤트 실시간 수집 |
| **가공 계층** | 스트리밍 파이프라인(Kafka/Flink), 데이터 레이크 | 봇 트래픽 필터링, 결측치 보정, 분산감소(CUPED) 적용 |
| **분석 계층** | 통계 검정기(t-test, 카이제곱), Bayesian 엔진 | **p-value** 산출, 신뢰구간 계산, **SRM** 이상 감지 경보 |
| **시각화 계층**| 의사결정 대시보드 | 효과 크기, **Guardrail Metrics** 표시 및 롤아웃 트리거 |

## Ⅳ. A/B 테스트 vs 다변량 테스트(MVT) vs 멀티암드 밴딧(MAB) 비교

> 인과관계 규명에는 A/B 테스트가 가장 적합하며, 단기 기회비용 최소화에는 MAB가 유리함.

| 비교 기준 | A/B 테스트 (A/B Test) | 다변량 테스트 (MVT) | 멀티암드 밴딧 (MAB) |
|---|---|---|---|
| **실험 목적** | 단일 요인 변경의 명확한 인과효과 검증 | 복수 요인의 조합 및 상호작용 분석 | 탐색과 활용 균형을 통한 단기 수익 극대화 |
| **변수** | 단일 변경안 | 복수 요인·조합 | 복수 대안 |
| **배정** | 사전 정한 비율 유지 | 조합별 고정 배정 | 관측성과에 따라 적응 배정 |
| **강점** | 인과효과 해석 용이 | 상호작용 분석 | 탐색·활용 동시 최적화 |

## Ⅴ. 실무 통계적 함정과 공학적·통계적 통제 방안

> 피킹 편향과 SRM은 잘못된 의사결정을 유발하는 가장 위험한 함정으로 엄격한 통제가 요구됨.

| 위험 | 대책 | 효과 |
|---|---|---|
| **표본비율 불일치(SRM)** | 적합도 검정 후 배정·계측 원인 규명 전 판정 보류 | 편향 표본의 오판 방지 |
| **피킹 문제(Peeking)** | 정해진 표본수 도달 전 분석 금지 또는 순차 검정(Sequential) 적용 | 1종 오류(거짓 양성) 급증 차단 |
| **다중 검정 오류** | 본페로니(Bonferroni) 교정 또는 FDR(False Discovery Rate) 통제 | 우연에 의한 가짜 개선 효과 배제 |
| **간섭 효과(Spillover)** | 사용자 단위 대신 지역(Cluster) 또는 시간 단위 무작위 배정 | 네트워크 효과로 인한 데이터 오염 방지 |
| **신규성 효과(Novelty)** | 충분한 관측기간 확보 · 신규·기존 사용자 코호트 분리 | 일시적 착시 식별 |

## Ⅵ. 실험 문화와 신뢰성 거버넌스 중심의 기술사적 제언

> 단순 A/B 테스트 툴 도입을 넘어, 실패한 실험 데이터를 자산화하고 카나리 배포와 연동하는 **실험 거버넌스 체계** 정립이 핵심임.

`[핵심 통찰]` 유의한 p-value만으로 배포를 결정하면 효과크기가 작거나 안정성을 훼손한 변경안을 채택할 수 있으므로, 배정 무결성·효과크기·Guardrail을 함께 판정해야 함.

`나라면` 실험 시작 전에 가설·표본수·종료조건·Guardrail을 등록하고, SRM 발생 시 결과 해석보다 배정·계측 파이프라인을 먼저 복구하겠음.

<div class="itpe-pipeline is-vertical" role="img" aria-label="A/B 테스트 통계적 신뢰성 확보 제언 파이프라인">
  <div class="itpe-pipeline-node">
    <strong>현행 한계</strong>
    <div class="itpe-step-detail"><strong>문제</strong><span>직관 의존 출시 · 피킹 편향 및 SRM 표본 왜곡 방치</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>개선 대안</strong>
    <div class="itpe-step-detail"><strong>대안</strong><span>A/B 테스트 표준 파이프라인 · SRM 자동 진단 및 순차 검정 도입</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>검증 기준</strong>
    <div class="itpe-step-detail"><strong>판정</strong><span>SRM 없음 · 종료조건 충족 · 효과크기·신뢰구간 · Guardrail</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>실행 효과</strong>
    <div class="itpe-step-detail"><strong>효과</strong><span>거짓 양성 축소 · 재현 가능한 배포 의사결정</span></div>
  </div>
</div>

## 1교시 10점 답안 발췌

### 1. 정의·목적

- 정의: 사용자를 대조군(A)과 실험군(B)에 무작위 배정하여 단일 변수의 변경이 성과지표에 미친 영향을 검증하는 **무작위 통제 실험(RCT)**
- 목적: 변경효과 검증 · 의사결정 불확실성 축소 · 안전한 단계적 배포

### 2. 구성체계 및 방법론

<div class="itpe-pipeline is-vertical" role="img" aria-label="1교시 10점용 A/B 테스트 메커니즘 요약">
  <div class="itpe-pipeline-node">
    <strong>가설 수립</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>귀무/대립가설 · 성과지표</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>Feature Flag 배정</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>사용자 단위 무작위 배정</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>동일 기간 관측</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>Control vs Variant 동시 노출</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>통계 검정</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>SRM 진단 · p-value 및 신뢰구간</span></div>
  </div>
  <div class="itpe-pipeline-arrow">↓</div>
  <div class="itpe-pipeline-node">
    <strong>롤아웃 결정</strong>
    <div class="itpe-step-detail"><strong>역할</strong><span>Guardrail 지표 점검 후 배포</span></div>
  </div>
</div>

### 3. 핵심 통제

- **SRM(Sample Ratio Mismatch)**: 표본 배정 왜곡 감지 시 원인 규명 전 결과 판정 보류
- **Peeking 방지**: 정해진 표본수 도달 전 조기 종료 금지 및 순차 검정(Sequential Testing) 적용
- **Guardrail Metrics**: 전환율 상승 이면에 숨은 시스템 장애 및 응답 지연율 병행 감시

## 출제 이력과 검증 출처

- 공식 문제지 원문으로 확인한 직접 기출 없음
- Ron Kohavi et al., [Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing](https://experimentguide.com)
- NIST/SEMATECH, [e-Handbook of Statistical Methods, Comparing Two Proportions](https://www.itl.nist.gov)

## 학습 체크

- [ ] Ⅰ. A/B 테스트의 정의·목적과 무작위 배정의 역할을 설명할 수 있는가?
- [ ] Ⅱ. 가설 수립부터 배포 판정까지 활동·산출을 연결할 수 있는가?
- [ ] Ⅲ. 배정·수집·가공·분석·시각화 계층의 통제를 설명할 수 있는가?
- [ ] Ⅳ. A/B·MVT·MAB를 변수·배정·강점으로 비교할 수 있는가?
- [ ] Ⅴ~Ⅵ. SRM·Peeking·다중검정·간섭·신규성 효과의 대응책을 제시할 수 있는가?

## 연결 토픽

- 이전 토픽: [터크만 팀 발달 모델](./028_tuckman_team_development_model.md)
- 연관 토픽: [그로스 해킹](./046_growth_hacking.md), [디자인 씽킹](./047_design_thinking.md), [CRM](./031_crm.md)
- 다음 토픽: [BCP](./030_bcp.md)
