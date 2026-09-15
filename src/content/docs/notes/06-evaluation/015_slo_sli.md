---
sidebar:
  order: 15
  label: "015. SLO•SLI (Service Level Objective•Indicator)"
  badge:
    text: "기출 · 50%"
    variant: note
title: "사이트 신뢰성 공학(SRE) 품질 지표 및 목표 거버넌스 : SLI 및 SLO (Google SRE & CUJ 기반)"
date: "2026-09-15T09:27:00+09:00"
tags:
  - "notes-evaluation"
weight: 15
extra:
  question_no: "015"
  source_status: "기출"
  source_history: "137회, 138회"
  priority: 50
  priority_note: "137회·138회 연속 출제, Google SRE(Site Reliability Engineering) 핵심 신뢰성 지표, 서비스 수준 지표(SLI: Service Level Indicator, SLI=Good Events / Valid Total Events), 서비스 수준 목표(SLO: Service Level Objective), 핵심 사용자 여정(CUJ: Critical User Journey), 이동 측정 창(Rolling Window), 다중 윈도우 다중 번레이트(Multi-Window Multi-Burn-Rate) 경보"
---

## Ⅰ. 개요

<details><summary>용어 설명</summary>

- **서비스 수준 지표 및 목표(SLI & SLO / Google Site Reliability Engineering)**:
  - **SLI (Service Level Indicator)**: 서비스가 제공하는 품질의 수준을 사용자 관점에서 정량적으로 계측한 실측 비율 ($\text{SLI} = \frac{\text{Good Events (성공/정상 지연 이벤트 수)}}{\text{Valid Total Events (유효 전체 이벤트 수)}} \times 100\%$).
  - **SLO (Service Level Objective)**: 개발팀(Dev)과 운영팀(SRE)이 시스템의 안정성과 출시 속도의 균형을 맞추기 위해 내부적으로 합의한 정량적 목표 기준선 (예: "30일 이동 창 동안 결제 요청의 99.9%가 500ms 이내에 완료되어야 함").
- **인프라 중심 모니터링 및 주관적 품질 판단 결함(Host-centric & Subjective Reliability Defect)**: 서버 CPU 80% 가동률 같은 단순 하드웨어 지표에만 매몰되어 실제 사용자 결제 실패나 화면 멈춤을 조기에 감지하지 못하고, 개발팀의 신규 배포 요구와 운영팀의 변경 거부 간의 소모적 갈등을 유발하는 구조적 결함.

</details>

- 정의/개념: 데이터 기반의 신뢰성 거버넌스를 확립하기 위해 **핵심 사용자 여정(CUJ) 정의 $\rightarrow$ 좋은 이벤트(Good Events) 기준 수립 $\rightarrow$ 이동 측정 창(Rolling Window) 기반 SLI 산출 $\rightarrow$ 에러 예산($1-\text{SLO}$) 연계 내부 목표(SLO) 설정 $\rightarrow$ 번레이트(Burn Rate) 기반 배포 통제** 를 집행하는 **SRE 정량 품질 관리 체계**
- 배경/필요성: 시스템 가용성 목표를 비현실적인 무결점으로 설정하거나 단순 서버 CPU 가동률 등 인프라 중심 지표에만 매몰될 경우, 실제 최종 사용자가 겪는 결제 실패나 응답 지연을 감지하지 못하고 신속한 기능 출시를 원하는 개발팀(Dev)과 시스템 안정을 추구하는 운영팀(Ops) 간의 끝없는 소모적 갈등이 유발되는 구조적 결함이 발생함에 따라, Google SRE 표준에 기반하여 핵심 사용자 여정(CUJ)을 중심으로 유효 전체 이벤트 대비 성공 이벤트 비율($\text{SLI} = \frac{\text{Good}}{\text{Valid Total}}$)을 계측하고 내부 엔지니어링 목표(SLO) 및 에러 예산($1-\text{SLO}$)을 수립하는 SLI/SLO 거버넌스를 도입하여 **사용자 체감 품질의 정밀 계측, 데이터 주도적 서비스 신뢰성 관리 및 번레이트(Burn Rate) 기반의 객관적 배포 승인·동결 의사결정**을 달성할 필요

#### 한줄 요약
- SLI는 사용자 관점의 품질 실측치이고, SLO는 에러 예산과 연계된 내부 엔지니어링 목표 기준선이다.

## Ⅱ. 특징

<details><summary>용어 설명</summary>

- **SLI/SLO 3대 핵심 설계 원칙**:
  - **사용자 중심주의 (User-Centric / CUJ)**: 백엔드 서버 상태가 아닌 실제 사용자가 겪는 체감 품질(성공률, 지연시간)을 측정.
  - **단순하고 명확한 이벤트 비율 (Good / Total)**: 모든 SLI를 $0\% \sim 100\%$ 범위의 백분율 비율 공식으로 통일.
  - **이동 측정 창 (Rolling Time Window)**: 고정된 월초~월말이 아닌 최근 7일, 28일, 30일간의 연속된 기간을 슬라이딩 윈도우로 평가.

</details>

- 성공·지연 준수 비율에 기반한 **SLI 수식화**
- SLO에서 허용 실패량을 구하는 **에러 예산**
- 급격·완만한 소진을 잡는 **다중 윈도우 번레이트**

#### 한줄 요약
- 사용자 중심 CUJ 계측, Good/Total 백분율 공식, 이동 측정 창, 에러 예산 및 번레이트 연계를 제공한다.

## Ⅲ. 구조 및 구성요소

<details><summary>용어 설명</summary>

- **SLI & SLO 4대 아키텍처 계층**:
  1. **CUJ Layer**: 핵심 사용자 여정(로그인, 상품 검색, 장바구니, 결제 승인) 식별.
  2. **SLI Specification Layer**: 좋은 이벤트(Good), 유효 이벤트(Valid Total), 측정 위치 정의.
  3. **Aggregation & Window Layer**: Prometheus/Datadog 기반 30일 이동 집계 윈도우.
  4. **Governance & Decision Layer**: 잔여 에러 예산 산출, 배포 동결(Freeze) 또는 롤아웃 승인.

</details>

```text
[SLI·SLO 관리 체계]
├── [CUJ Layer]
│   └── 핵심 사용자 여정 식별
├── [SLI Specification Layer]
│   └── Good·Valid Total 이벤트 명세
├── [Aggregation·Window Layer]
│   └── 이동 측정 창(Rolling Window) 집계
└── [Governance·Decision Layer]
    └── 에러 예산 연계 배포 승인·동결
```

- 선의 의미: 계층 구조 및 상하위 포함 관계를 나타낸다.

| 구성요소 | 책임 |
|:---|:---|
| CUJ Layer | 사용자 핵심 여정과 측정 우선순위 정의 |
| SLI Specification Layer | Good·Valid Total·측정 위치 명세 |
| Aggregation·Window Layer | 이동 창에서 SLI 집계 |
| Governance·Decision Layer | 에러 예산에 따라 배포 승인·동결 |

#### 한줄 요약
- CUJ 계층이 맨 앞에서 측정 대상을 핵심 여정으로 좁혀 주므로 모든 엔드포인트를 계측하고도 사용자 체감과 무관한 지표만 쌓이는 낭비가 줄고, 그렇게 남긴 SLI만 이동 창 집계를 거쳐 배포 승인과 동결의 근거가 된다.

## Ⅳ. 흐름도

<details><summary>용어 설명</summary>

- **SLI/SLO 수립 및 운영 5단계 수명주기**:
  1. 핵심 사용자 여정(CUJ: 주문 결제) 및 측정 지점(API Gateway) 선정
  2. 좋은 이벤트 기준(HTTP 5xx 미발생 및 응답시간 300ms 이하) 명세화
  3. 최근 30일 이동 창 기반으로 실측 SLI 데이터베이스 집계
  4. 과거 데이터와 비즈니스 요구를 반영하여 SLO 목표치(99.9%) 확정
  5. 일일 에러 예산 소진율(Burn Rate)을 감시하여 배포 승인 또는 동결 집행

</details>

```text
[요구사항 분석] (핵심 사용자 여정 CUJ 및 결제 엔드포인트 식별)
 └── [판정 공식 정의] (① Good Event 및 Valid Total 명세화)
      └── [목표치 수립] (② 30일 이동 창 SLO 99.9% 및 에러 예산 확정)
           └── [실시간 계측] (③ Prometheus 메트릭 수집 및 번레이트 감시)
                └── [정책 집행] (④ 에러 급증 시 자동 롤백 및 배포 동결)
                     └── [환류 및 개선] (⑤ 안정화 스프린트 수행 및 회고)
```

- 분기 결과: 에러 예산 잔여 시 신규 배포 승인, 번레이트 초과 소진 시 즉시 배포 동결 및 안정화 스프린트 전환.

#### 한줄 요약
- 30일 창 SLI가 99.94%로 양호해도 1시간 번레이트 14.4배가 잡히면 배포가 즉시 차단되므로, 판정 갈래는 누적 달성률이 아니라 에러 예산의 소진 속도에서 갈린다.

## Ⅴ. 종류 및 비교

<details><summary>용어 설명</summary>

- **주요 SLI 지표 4대 유형 비교**:
  - 가용성 SLI (Availability): 요청 성공률 ($\frac{\text{Status} < 500}{\text{Total}}$).
  - 지연시간 SLI (Latency): 응답 시간 준수율 ($\frac{\text{Latency} \le T}{\text{Total}}$).
  - 품질 저하 SLI (Quality): 기능 저하(Graceful Degradation) 없는 완전 응답률.
  - 신선도 SLI (Freshness): 데이터 파이프라인의 실시간 동기화 지연 준수율.

</details>

| SLI 지표 유형 | Good Event 판정 기준 | 주요 측정 대상 시스템 | 핵심 사용자 경험 |
|:---|:---|:---|:---|
| 가용성 (Availability) | HTTP 상태 코드가 5xx가 아닌 경우 | **웹 서버, API 게이트웨이, 결제 서버** | "서비스가 에러 없이 작동하는가?" |
| 지연시간 (Latency) | 왕복 응답시간이 $T\text{ms}$ 이하인 경우 | **검색 엔진, 대화형 웹 화면, DB 쿼리** | "화면이 버벅거림 없이 빠른가?" |
| 처리율 (Throughput) | 초당 처리 건수가 최소 기준 이상인 경우 | **비디오 스트리밍, 대용량 파일 다운로드** | "다운로드가 끊김 없이 전송되는가?" |
| 품질 (Quality) | Fallback 응답이 아닌 온전한 데이터 반환 | **AI 추천 엔진, 개인화 배너 서버** | "임시 데이터가 아닌 정확한 결과인가?" |
| 신선도 (Freshness) | 데이터 생성 후 DB 반영까지의 지연 $\le T$ | **실시간 주가 파이프라인, 대시보드** | "지금 보는 데이터가 최신 정보인가?" |

#### 한줄 요약
- 가용성(성공률), 지연시간(응답 속도), 처리율(전송량), 품질(완전성), 신선도(최신성)로 분류된다.

## Ⅵ. 실무 고려사항 및 대책

<details><summary>용어 설명</summary>

- **RUM(Real User Monitoring)**: 실제 사용자의 웹 브라우저나 모바일 앱에 스크립트를 삽입하여 페이지 로드 시간, 렌더링 지연, 클라이언트 에러를 실시간으로 계측하는 방식이다.
- **Edge API Gateway**: 사용자와 지리적으로 가까운 네트워크 엣지(Edge)에 위치하여 트래픽 진입을 관리하고 인증, 라우팅, 가용성 메트릭을 계측하는 관문 시스템이다.
- **다중 윈도우 다중 번레이트(Multi-Window Multi-Burn-Rate)**: 단일 기간 대신 짧은 윈도우(예: 1시간)와 긴 윈도우(예: 6시간)를 동시에 감시하여 급격한 에러 폭증과 서서히 누적되는 예산 소진을 놓치지 않고 경보하는 SRE 기법이다.

</details>

| 문제 | 대책 | 효과 |
|:---|:---|:---|
| 클라이언트 4xx를 장애로 취급해 **부당한 SLO 위반 발생** | 4xx를 Good Event로 분류하고 **5xx 서버 오류만 Bad 집계** | **사용자 오입력 편향** 배제 |
| 백엔드만 측정하여 **CDN/LB 앞단 장애 사각지대 발생** | 사용자 접점의 **Edge Gateway 및 RUM 계측** 채택 | **체감 품질 가시성** 확보 |
| 100% 무결점 목표로 **신규 기능 배포 무기한 동결** | 포 나인(99.99%) 이하 **현실적 SLO와 에러 예산 협약** | **출시 속도와 안정성** 균형 |

#### 한줄 요약
- 4xx 에러를 정상으로 분리하고, Edge Gateway에서 체감 품질을 측정하며, 현실적 SLO로 배포 유연성을 확보한다.

## Ⅶ. 결론

<details><summary>용어 설명</summary>

- **배포 동결(Deployment Freeze)**: 에러 예산이 소진되었을 때 시스템 안정성을 회복하기 위해 신규 기능 릴리스를 일시 중단하고 버그 수정 및 인프라 개선 작업에만 집중하도록 강제하는 SRE 정책이다.
- **오픈텔레메트리(OpenTelemetry)**: 클라우드 네이티브 환경에서 메트릭, 로그, 분산 추적 데이터를 표준화된 방식으로 수집하고 내보내는 오픈소스 관측성 프레임워크이다.
- **핵심 사용자 여정(CUJ, Critical User Journey)**: 사용자가 비즈니스 목적(예: 로그인, 상품 검색, 결제)을 달성하기 위해 거치는 가장 핵심적인 일련의 상호작용 흐름이다.

</details>

- **기술 위상/발전**: 사용자 관점의 실측 품질과 엔지니어링 목표를 데이터로 정합화하여 배포 균형을 잡는 **SRE 핵심 신뢰성 지표 표준**으로 안착, OpenTelemetry 관측성 및 AIOps 파이프라인과 연계 발전
- **실무 적용/통제**: SRE 운영 시 **사용자 접점 Edge Gateway 및 RUM 기반 SLI 수집**, 4xx와 5xx의 **엄격한 오류 분류** 및 **다중 윈도우 다중 번레이트(Multi-Window Multi-Burn-Rate) 기반 배포 동결 정책** 필수

#### 한줄 요약
- 사용자 중심 SLI/SLO 지표 체계와 에러 예산 거버넌스를 통해 시스템 신뢰성과 출시 속도의 최적 균형을 체계적으로 달성해야 한다.
