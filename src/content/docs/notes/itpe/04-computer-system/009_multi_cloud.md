---
title: "멀티클라우드(Multi-Cloud)"
author: "Codex"
date: "2026-09-20T20:09:00+09:00"
tags: ["notes-computer-system"]
sidebar:
  badge:
    text: "A"
extra:
  model: "GPT-5.6 Sol"
  keyword_grade: "A"

---

<p class="itpe-byline">작성 모델 · GPT-5.6 Sol<br />작성 · 2026.09.20 20:09 KST</p>

## 지식 로드맵 내 현재 위치

<div class="itpe-topic-path" aria-label="지식 경로"><span>클라우드 컴퓨팅</span><span>클라우드 운영전략</span><strong>멀티클라우드</strong></div>

## 큰 그림과 30초 인출

```text
                 [Business·Policy·SLO]
                           │
       ┌──────── Unified Governance ────────┐
       │ IAM Federation │ Policy │ FinOps   │
       │ IaC/CI-CD │ Observability │ CMDB   │
       └───────────────┬─────────────────────┘
          ┌────────────┼────────────┐
          ▼            ▼            ▼
      [Cloud A]    [Cloud B]    [Cloud C]
        App/Data     App/Data      App/Data
          └──── Network·Data·Trust ────┘
```

```text
Multi-Cloud = 둘 이상의 클라우드 서비스를 목적별로 조합·운영
핵심 = 배치 전략 + 통합 거버넌스 + 연결 + 관측 + 비용
주의 = 모든 워크로드의 이식성·Active-Active를 뜻하지 않음
통제 = ID·정책 불일치, Data Gravity, Egress, 지연, 책임 경계
```

## 예상문제

> 멀티클라우드의 개념과 구성요소, 하이브리드 클라우드와의 차이를 설명하고 도입 절차 및 고려사항을 제시하시오.

## Ⅰ. 개요 ───── 정의·목적

멀티클라우드는 **단일 조직이 둘 이상의 클라우드 공급자 또는 클라우드 서비스를 업무 목적에 따라 선택·조합하고 공통 거버넌스로 운영하는 전략과 환경**이다.

| 목적 | 설명 |
|---|---|
| 적합 서비스 선택 | 데이터·지역·기능·규제에 맞춘 배치 |
| 회복탄력성 | 장애 도메인과 공급망 위험 분산 |
| 종속 관리 | 계약·기술 집중 위험 완화 |
| 협상·비용 | 단위비용과 운영비를 함께 최적화 |

## Ⅱ. 특징 ───── 선택성·분산성·복잡성

| 특징 | 가치 | 상충 요소 |
|---|---|---|
| Best-fit 배치 | 서비스·지역 선택 | 기술 스택 다양화 |
| 장애 도메인 분산 | 연속성 강화 가능 | 데이터 동기화 복잡성 |
| 공통 자동화 | 정책 일관성 | 최소공통분모 위험 |
| 통합 관측·비용 | 전사 가시성 | 계정·태그·지표 정규화 |

## Ⅲ. 구조 ───── 세 평면과 공통 통제

```text
Governance Plane : Portfolio│Policy│Risk│Compliance│FinOps
Management Plane : Broker/CMP│IaC│CI/CD│Inventory│Observability
Resource Plane   : Cloud A ─ Cloud B ─ Cloud C
                   Compute│Network│Data│Managed Service

횡단 통제: Federated IAM · Key/Secret · Connectivity · Audit · DR
```

NIST Cloud Federation Reference Architecture의 관점처럼 서비스 배포·오케스트레이션·관리·보안과 참여 주체의 책임을 분리해 그린다.

## Ⅳ. 동작 ───── 전략부터 지속 최적화까지

```text
① 목표/SLO·규제 정의 → ② 워크로드·데이터 분류
 → ③ 공급자·지역·서비스 배치 → ④ Landing Zone·IAM·Network
 → ⑤ IaC/Policy 기반 배포 → ⑥ 통합 관측·FinOps
 → ⑦ 장애·복구·이전 리허설 → ⑧ 지속 재배치
```

| 단계 | 핵심 산출물 |
|---|---|
| 전략 | 배치 원칙, 공급자 역할, Exit 기준 |
| 설계 | 계정 구조, 신뢰, 연결, 데이터 흐름 |
| 구축 | Landing Zone, IaC, 정책·파이프라인 |
| 운영 | SLO, 통합 로그, 비용 배분, DR 결과 |

## Ⅴ. 비교 ───── 멀티클라우드·하이브리드

| 구분 | 멀티클라우드 | 하이브리드 클라우드 |
|---|---|---|
| 중심 | 복수 클라우드의 조합 | Private/On-prem과 Public의 결합 |
| 목적 | 선택성·위험 분산 | 기존 자산 연계·단계적 전환 |
| 필수 조건 | 클라우드가 둘 이상 | 서로 다른 배치 환경의 연동 |
| 공통 과제 | IAM·Network·Data·Policy·Observability |

멀티클라우드가 곧 동일 워크로드의 실시간 양쪽 실행을 뜻하지 않으며, 목적에 따라 분리 배치·백업·대체·동시 실행을 선택한다.

## Ⅵ. 고려 ───── 복잡성을 통제 가능한 표준으로 전환

| 문제 | 원인 | 대응 | 검증 |
|---|---|---|---|
| ID·권한 불일치 | 계정·역할 모델 상이 | 연합 ID, 공통 역할 모델, JIT 권한 | 권한 경로·회수 시간 |
| 정책 편차 | 서비스별 설정 차이 | Policy as Code, 기준선·예외 절차 | 준수율·예외 수 |
| 데이터 중력·비용 | 대량 이동·Egress | 데이터 배치 우선, 복제 범위 최소화 | 이동량·총비용 |
| 지연·가용성 | 사업자 간 네트워크 | 연결 다중화, 캐시, SLO별 배치 | 종단 지연·장애 시험 |
| 관측 단절 | 로그·지표 모델 상이 | 공통 스키마·상관 ID·통합 대시보드 | 추적 완결률 |
| 허위 이식성 | 전용 관리형 서비스 | 경계 API, 데이터 Export, Exit 리허설 | 복구·이전 시간 |

## Ⅶ. 결론 ───── 공급자 수가 아닌 운영모델의 통합

멀티클라우드의 성패는 여러 계정을 보유하는 데 있지 않고 **워크로드 배치 원칙과 ID·정책·데이터·관측·비용의 공통 운영모델**을 만드는 데 있다. 필요한 영역만 이식성을 확보하고 실전 복구·이전 시험으로 검증해야 한다.

## 1교시 10점 발췌

```text
멀티클라우드는 둘 이상의 클라우드 서비스를 목적별로 조합하고
공통 거버넌스로 운영하는 전략·환경이다.

구조: Governance Plane → Management Plane → Multi-Cloud Resource Plane
통제: Federated IAM·Policy as Code·Connectivity·Data·Observability·FinOps
주의: Multi-Cloud ≠ 모든 워크로드 Portable/Active-Active
```

## 공식 검증 출처

- [NIST SP 500-332 — Cloud Federation Reference Architecture](https://www.nist.gov/publications/nist-cloud-federation-reference-architecture-0)
- 공식 기출 근거: 한국산업인력공단 Q-Net 정보관리기술사 135회 문제지

## 답안 체크

- [ ] 전체 지도에서 거버넌스·관리·자원 평면을 분리했는가
- [ ] 하이브리드와 차이를 중심축으로 비교했는가
- [ ] 데이터 이동과 Egress를 함께 고려했는가
- [ ] ‘모든 워크로드 이식’으로 과장하지 않았는가

## 연결 토픽

- [서버리스 컴퓨팅](./003_serverless_computing/)
- [스토리지 유형 비교](./123_storage_type_comparison/)
- [가상화](./008_virtualization/)
