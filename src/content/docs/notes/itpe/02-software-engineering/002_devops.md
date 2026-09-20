---
title: "DevOps"
author: "Gemini 3.8 Flash"
date: "2026-09-20T00:25:00+09:00"
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

<div class="itpe-topic-path" aria-label="소프트웨어 생명주기에서 데브옵스까지의 지식 경로"><span>SW 공학</span><span>개발·운영 통합</span><strong>DevOps</strong></div>

## 큰 그림과 30초 인출

```text
Plan → Code → Build → Test → Release → Deploy → Operate → Observe
  ▲                                                        │
  └──────────────────── Feedback ──────────────────────────┘

Culture + Automation + Measurement + Sharing
CI/CD + IaC + Observability + DevSecOps
```

## 예상문제

> DevOps의 개념과 원칙, 생명주기와 CI/CD 구조를 설명하고 Agile과 비교한 후 도구 중심 도입의 문제와 개선방안을 제시하시오. (25점)

## 답안 골격
```text
[DevOps] ◀━━ 머리: Ⅶ 내 의견 (조직 사일로 해소 없는 도구 만능주의 경계 및 관측성 내재화)
 ┃
 ┣━ Ⅰ 개요 ───── 개발-운영 간 상충된 목표로 인한 배포 지연 → 문화·자동화 협업 체계로 리드타임 단축
 ┣━ Ⅱ 특징 ───── CAMS 원칙(Culture, Automation, Measurement, Sharing) · 피드백 루프 단축
 ┣━ Ⅲ 구조 ───── Plan → Code → Build → Test → Release → Deploy → Operate → Monitor
 ┣━ Ⅳ 흐름 ───── ① 코드 커밋 → ② CI 빌드/테스트 → ③ 아티팩트 저장 → ④ CD 자동 배포 → ⑤ 모니터링
 ┣━ Ⅴ 비교 ───── 애자일(소프트웨어 개발 집중) vs DevOps(릴리스 및 운영 전 주기 확장)
 ┗━ Ⅵ 실무 ───── 조직 장벽 및 섀도우 IT 위험 / IaC 및 DevSecOps 파이프라인 정착
```
- 필수 키워드: CAMS · CI/CD · 파이프라인 · IaC · 관측성(Observability) · 피드백 루프
- 기출: 136회 1교시 `DevOps 장점과 단점` → Ⅱ·Ⅵ / 120회 2교시 `모놀리스 vs MSA와 DevOps` → Ⅲ·Ⅴ

## 한 줄 본질
- 신속한 기능 출시를 원하는 개발과 시스템 안정을 중시하는 운영 간의 목표 분열(사일로) → CI/CD 자동화 도구와 협업 문화를 통해 개발부터 배포·운영 피드백까지 하나의 흐름으로 통합 → 출시 주기 단축 및 서비스 복구 속도 향상 / 보안 통제 약화 및 도구 복잡도 증가 비용

## 핵심 그림
```text
      [ Plan ]  --->  [ Code ]  --->  [ Build ]  --->  [ Test ]
         ^                                                |
         |         === Continuous Feedback Loop ===        v
      [ Monitor ] <--- [ Operate ] <--- [ Deploy ] <--- [ Release ]
```

## 핵심 용어
- CAMS: DevOps의 4대 핵심 축인 문화(Culture), 자동화(Automation), 측정(Measurement), 공유(Sharing)
- IaC(Infrastructure as a Code): 인프라 구성을 코드로 정의해 버전 관리와 재현성을 보장하고 수동 설정 오차를 제거하는 기법

## 핵심 통찰
- DevOps는 Jenkins나 Kubernetes 도입 같은 도구의 문제가 아니라 실패를 허용하고 책임 경계를 지우는 조직 문화의 전환임
- 빈번한 소규모 배포는 변경 범위를 좁혀 장애 원인 규명과 롤백을 용이하게 하는 통제 수단이 될 수 있음
- 측정 지표(DORA 메트릭: 배포 빈도, 변경 리드타임, 서비스 복구 시간, 변경 실패율)가 없으면 프로세스 개선 여부를 증명할 수 없음

## 이웃 토픽과 구분
- 애자일 vs DevOps: 애자일 = 고객 요구 변화에 맞춘 개발 이터레이션 반복 / DevOps = 개발된 결과물의 릴리스, 배포, 인프라 운영까지 파이프라인 확장

## 문제·원인·대책
- 적용 상황: 변경 빈도가 높고 지속적 배포가 필요한 디지털 서비스 환경
| 문제 | 원인 | 대책 | 효과 |
|---|---|---|---|
| 배포 주기 단축에 따른 보안 취약점 운영 환경 유입 | 파이프라인 내 수동 보안 검수로 인한 병목 또는 검수 누락 | 파이프라인 초기 SAST/DAST 자동화 도구 연동(DevSecOps) | 배포 지연 없이 빌드 단계에서 취약점 조기 차단 |
| 개발팀의 임의 인프라 프로비저닝으로 인한 비용 급증 | IaC 거버넌스 부재 및 클라우드 리소스 가시성 결여 | 플랫폼 엔지니어링 기반 내부 개발자 플랫폼(IDP) 제공 | 승인 템플릿 기반 리소스 할당 및 비용 가시성 확보 |

## 이렇게 출제된다
- 제136회 1교시 6번: "DevOps 장점과 단점" → 요구 포인트: Ⅱ CAMS 및 속도·품질 장점 + Ⅵ 조직 갈등·보안 취약 단점과 극복 방안
- 제120회 2교시 3번: "모놀리스(Monolith)와 마이크로서비스(Microservice) 아키텍처의 개념을 비교하여 설명하고 데브옵스(DevOps) 구현시의 장단점" → 요구 포인트: Ⅲ MSA 분할 배포 + Ⅳ CI/CD 파이프라인 + Ⅵ 운영 복잡도 통제

## 내 의견
- [도구만 도입하고 책임은 분리된 가짜 DevOps] 사내에 CI/CD 파이프라인만 깔아두고 장애 발생 시 여전히 개발과 운영이 로그 분석 책임을 미루는 현상 다수 목격 → 나라면: 장애 1차 대응에 개발자를 참여시키는 온콜(On-call) 순환 근무를 제도화하고, DORA 메트릭을 분기별 핵심 성과지표(KPI)로 연동하여 배포 속도와 복구 시간의 균형 측정

## Ⅰ. 개발과 운영의 흐름을 통합하는 DevOps 개요

- 정의: **DevOps**는 개발·운영·보안 등 이해관계자가 문화·자동화·측정·공유를 통해 기획부터 운영 피드백까지 하나의 가치흐름으로 협업하는 방식
- 목적: 인수인계·수작업·대기 시간을 줄이면서 작은 변경을 안전하고 반복 가능하게 배포하고 복구
- 핵심: 도구 도입 자체가 아니라 공동 책임, 빠른 피드백, 자동화된 품질게이트, 관측 가능한 운영의 결합

## Ⅱ. CAMS와 지속적 피드백의 특징

| 축 | 실천 | 효과 |
|---|---|---|
| **Culture** | 공동 목표·Blameless 회고·제품팀 책임 | 사일로·책임전가 완화 |
| **Automation** | CI/CD·IaC·자동 테스트·정책 코드화 | 반복성·재현성 확보 |
| **Measurement** | 흐름·안정성·사용자 결과 측정 | 개선 효과와 병목 식별 |
| **Sharing** | 코드·운영지식·런북·사고교훈 공유 | 피드백과 학습 확산 |

## Ⅲ. 가치흐름과 자동화 파이프라인 구조

```text
Plan → Code → Build → Test → Security/Quality Gate
                              │
                              ▼
Artifact Repository → Release → Deploy → Operate → Observe
       ▲                                               │
       └──────────── Feedback·Learning ────────────────┘

IaC·Policy as Code / Version Control / Traceability
```

| 구성 | 책임 |
|---|---|
| **CI** | 변경 통합, 빌드·단위테스트·정적검사 자동화 |
| **CD** | 검증된 아티팩트를 환경별 일관된 절차로 전달·배포 |
| **IaC** | 인프라 구성을 버전관리해 재현·검토·복구 가능하게 함 |
| **Observability** | 로그·메트릭·트레이스로 행위와 실패 원인 관찰 |
| **Feedback** | 사용자·운영·사고 결과를 백로그와 설계에 환류 |

## Ⅳ. 커밋에서 운영 피드백까지의 동작

```text
① 코드·설정 변경과 리뷰
 → ② 자동 빌드·단위/통합 테스트
 → ③ 보안·품질 정책 검증
 → ④ 불변 아티팩트 생성·서명·보관
 → ⑤ 단계적 배포·상태 확인
 → ⑥ SLI·로그·트레이스 관측
 → ⑦ 이상 시 롤백·완화, 정상 시 점진 확대
 → ⑧ 결과를 백로그·런북·플랫폼 표준에 환류
```

## Ⅴ. Agile·DevOps·DevSecOps 비교

| 기준 | Agile | DevOps | DevSecOps |
|---|---|---|---|
| 초점 | 요구 변화와 반복 개발 | 개발-배포-운영 가치흐름 | 전 주기 보안 책임 내재화 |
| 범위 | 백로그·개발팀·고객 피드백 | 제품팀·운영·플랫폼 | 개발·운영·보안·공급망 |
| 핵심 실천 | 짧은 반복·점진적 전달 | CI/CD·IaC·관측·공동운영 | Threat Modeling·SAST/SCA·정책 코드화 |
| 성과 | 고객가치·변화 대응 | 흐름 속도와 안정성 | 위험 기반 배포·취약점 대응 |

## Ⅵ. 도구 중심 도입의 문제와 개선

| 문제 | 원인 | 대책 | 검증지표 |
|---|---|---|---|
| **도구 사일로** | 팀별 파이프라인·권한·표준 분리 | 공통 플랫폼과 셀프서비스 골든패스 | 대기시간·우회 배포율 |
| **속도 편향** | 배포횟수만 KPI화 | 배포빈도·리드타임과 변경실패·복구를 함께 측정 | 흐름·안정성 균형 |
| **보안 후행** | 릴리스 직전 수동 심사 | 위협모델·SAST/SCA·Secret·서명 검증 자동화 | 차단·예외·수정시간 |
| **관측 공백** | 배포 성공을 서비스 성공으로 오인 | SLI/SLO·분산추적·배포표식 연계 | 오류예산·탐지·복구시간 |
| **인지부하** | 팀마다 인프라·도구를 직접 조립 | 플랫폼 엔지니어링·표준 템플릿 | 개발자 대기·지원 요청 |

## Ⅶ. 빠른 배포보다 빠르고 안전한 학습을 만드는 결론

- DevOps의 목표는 배포횟수 자체가 아니라 **변경을 작게 만들고 자동 검증·관측·복구하여 학습 주기를 단축하는 것**
- 공동 소유 문화와 플랫폼 표준, 보안 내재화, 흐름·안정성 지표를 함께 운영해야 도구 자동화가 실제 서비스 가치로 연결됨

## 1교시 10점 답안 발췌

```text
DevOps = Culture + Automation + Measurement + Sharing
Plan→Code→Build→Test→Release→Deploy→Operate→Observe→Feedback
핵심 구현 = CI/CD + IaC + Observability + DevSecOps
```

## 검증 출처와 학습 체크

- 제136회 정보관리기술사 1교시: DevOps 장점과 단점
- [Google Cloud, DORA research program](https://cloud.google.com/devops)
- [ ] CAMS 네 축을 실천·효과와 연결
- [ ] CI/CD·IaC·관측성의 책임을 구조도에 배치
- [ ] Agile·DevOps·DevSecOps를 같은 기준으로 비교

## 연결 토픽

- [CI/CD](./095_ci_cd/) · [Platform Engineering](./033_platform_engineering/) · [OpenTelemetry](./096_opentelemetry/) · [형상관리](./011_configuration_management/)
